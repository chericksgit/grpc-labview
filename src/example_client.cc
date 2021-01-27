//---------------------------------------------------------------------
//---------------------------------------------------------------------
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <query_server.grpc.pb.h>
#include <sstream>
#include <fstream>
#include <iostream>

//---------------------------------------------------------------------
//---------------------------------------------------------------------
using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using namespace std;
using namespace queryserver;

//---------------------------------------------------------------------
//---------------------------------------------------------------------
class QueryClient
{
public:
    QueryClient(shared_ptr<Channel> channel);

public:
    void Invoke(const string& command, const string& parameters);
    string Query(const string &command);
    unique_ptr<grpc::ClientReader<ServerEvent>> Register(const string& eventName);

public:
    ClientContext m_context;
    unique_ptr<QueryServer::Stub> m_Stub;
};

//---------------------------------------------------------------------
//---------------------------------------------------------------------
QueryClient::QueryClient(shared_ptr<Channel> channel)
    : m_Stub(QueryServer::NewStub(channel))
{        
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void QueryClient::Invoke(const string& command, const string& parameters)
{
    InvokeRequest request;
    request.set_command(command);
    request.set_parameter(parameters);

    ClientContext context;
    InvokeResponse reply;
    Status status = m_Stub->Invoke(&context, request, &reply);
    if (!status.ok())
    {
        cout << status.error_code() << ": " << status.error_message() << endl;
    }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
string QueryClient::Query(const string &command)
{
    QueryRequest request;
    request.set_query(command);
    QueryResponse reply;
    ClientContext context;

    Status status = m_Stub->Query(&context, request, &reply);

    if (status.ok())
    {
        return reply.message();
    }
    else
    {
        cout << status.error_code() << ": " << status.error_message() << endl;
        return "RPC failed";
    }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
unique_ptr<grpc::ClientReader<ServerEvent>> QueryClient::Register(const string& eventName)
{
    RegistrationRequest request;
    request.set_eventname(eventName);

    return m_Stub->Register(&m_context, request);
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
string GetServerAddress(int argc, char** argv)
{
    string target_str;
    string arg_str("--target");
    if (argc > 1)
    {
        string arg_val = argv[1];
        size_t start_pos = arg_val.find(arg_str);
        if (start_pos != string::npos)
        {
            start_pos += arg_str.size();
            if (arg_val[start_pos] == '=')
            {
                target_str = arg_val.substr(start_pos + 1);
            }
            else
            {
                cout << "The only correct argument syntax is --target=" << endl;
                return 0;
            }
        }
        else
        {
            cout << "The only acceptable argument is --target=" << endl;
            return 0;
        }
    }
    else
    {
        target_str = "localhost:50051";
    }
    return target_str;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
string GetCertPath(int argc, char** argv)
{
    string cert_str;
    string arg_str("--cert");
    if (argc > 2)
    {
        string arg_val = argv[2];
        size_t start_pos = arg_val.find(arg_str);
        if (start_pos != string::npos)
        {
            start_pos += arg_str.size();
            if (arg_val[start_pos] == '=')
            {
                cert_str = arg_val.substr(start_pos + 1);
            }
            else
            {
                cout << "The only correct argument syntax is --cert=" << endl;
                return 0;
            }
        }
        else
        {
            cout << "The only acceptable argument is --cert=" << endl;
            return 0;
        }
    }
    return cert_str;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
std::string read_keycert( const std::string& filename)
{	
    std::string data;
    std::ifstream file(filename.c_str(), std::ios::in);
    if (file.is_open())
    {
        std::stringstream ss;
        ss << file.rdbuf();
        file.close();
        data = ss.str();
    }
    return data;
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
void DoDataTypeTest(QueryClient& client)
{    
    ClientContext ctx;
    TestDataTypesParameters request;
    request.set_root("Root String");
    request.mutable_repeatedstring()->Add("String 1");
    request.mutable_repeatedstring()->Add("String 2");
    request.mutable_repeatedstring()->Add("String 3");

    request.mutable_repeatedintvalue()->Add(1);
    request.mutable_repeatedintvalue()->Add(2);
    request.mutable_repeatedintvalue()->Add(3);
    request.mutable_repeatedintvalue()->Add(4);
    request.mutable_repeatedintvalue()->Add(5);
    request.mutable_repeatedintvalue()->Add(6);

    request.set_rootint32(42);
    request.set_rootdouble(42.42);
    request.set_rootbool(true);
    request.set_rootfloat(37.56);

    request.mutable_repeateddoublevalue()->Add(1.1);
    request.mutable_repeateddoublevalue()->Add(2.2);
    request.mutable_repeateddoublevalue()->Add(3.3);
    request.mutable_repeateddoublevalue()->Add(4.4);
    request.mutable_repeateddoublevalue()->Add(5.5);
    request.mutable_repeateddoublevalue()->Add(6.6);

    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(false);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(false);

    request.mutable_repeatedfloatvalue()->Add(1.23);
    request.mutable_repeatedfloatvalue()->Add(2.23);
    request.mutable_repeatedfloatvalue()->Add(3.23);
    request.mutable_repeatedfloatvalue()->Add(4.23);
    request.mutable_repeatedfloatvalue()->Add(5.23);
    request.mutable_repeatedfloatvalue()->Add(6.23);

    request.mutable_nested()->set_boolvalaue(true);
    request.mutable_nested()->set_doublevalue(12.12);
    request.mutable_nested()->set_intvalue(4242);
    request.mutable_nested()->set_floatvalue(15.14);

    auto nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(true);
    nested->set_floatvalue(1.1);
    nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(false);
    nested->set_floatvalue(2.2);
    nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(true);
    nested->set_floatvalue(3.3);

    TestDataTypesParameters response;
    auto result = client.m_Stub->TestDataTypes(&ctx, request, &response);

    cout << response.root() << endl;
    for (auto i: response.repeatedstring())
    {
        cout << i << endl;
    }
    for (int x = 0; x < response.mutable_repeatedintvalue()->size(); ++x)
    {
        cout << response.mutable_repeatedintvalue()->data()[x] << endl;
    }

    cout << response.rootint32() << endl;
    cout << response.rootdouble() << endl;
    cout << response.rootbool() << endl;
    cout << response.rootfloat() << endl;

    for (int x = 0; x < response.mutable_repeateddoublevalue()->size(); ++x)
    {
        cout << response.mutable_repeateddoublevalue()->data()[x] << endl;
    }

    for (int x = 0; x < response.mutable_repeatedfloatvalue()->size(); ++x)
    {
        cout << response.mutable_repeatedfloatvalue()->data()[x] << endl;
    }

    for (int x = 0; x < response.mutable_repeatedboolvalue()->size(); ++x)
    {
        cout << response.mutable_repeatedboolvalue()->data()[x] << endl;
    }

    cout << response.nested().boolvalaue() << endl;
    cout << response.nested().doublevalue() << endl;
    cout << response.nested().intvalue() << endl;
    cout << response.nested().floatvalue() << endl;

    for (int x = 0; x < response.repeatednested().size(); ++x)
    {
        cout << response.repeatednested()[x].boolvalaue() << ", " << response.repeatednested()[x].floatvalue() << endl;
    }
}

//---------------------------------------------------------------------
//---------------------------------------------------------------------
int main(int argc, char **argv)
{
    auto target_str = GetServerAddress(argc, argv);
    auto certificatePath = GetCertPath(argc, argv);

    shared_ptr<grpc::ChannelCredentials> creds;
    if (!certificatePath.empty())
    {
        std::string cacert = read_keycert(certificatePath);
        grpc::SslCredentialsOptions ssl_opts;
        ssl_opts.pem_root_certs=cacert;
        creds = grpc::SslCredentials(ssl_opts);
    }
    else
    {
        creds = grpc::InsecureChannelCredentials();
    }
    auto channel = grpc::CreateChannel(target_str, creds);
    QueryClient client(channel);

    //DoDataTypeTest(client);

    auto result = client.Query("Uptime");
    cout << "Server uptime: " << result << endl;

    /*auto reader = client.Register("Heartbeat");
    int count = 0;
    ServerEvent event;
    while (reader->Read(&event))
    {
        cout << "Server Event: " << event.eventdata() << endl;
        count += 1;
        if (count == 10)
        {
            client.Invoke("Reset", "");
        }
    }
    Status status = reader->Finish();
    cout << "Server notifications complete" << endl;
	*/
	
	auto iterations = client.Query("numiterations:100");
    cout << "numiterations: " << iterations << endl;
	
	auto rate = client.Query("samplerate:20000");
    cout << "samplerate: " << rate << endl;
	
	cout << "Performing AI measurements" << endl;
    {
        auto startTime = chrono::steady_clock::now();
        ClientContext ctx;
        AnalogInputRequest request;
        AnalogInputData response;
        client.m_Stub->PerformAnalogInput(&ctx, request, &response);
        auto endTime = chrono::steady_clock::now();
        auto elapsed = chrono::duration_cast<chrono::milliseconds>(endTime - startTime);
        cout << "Analog Input measurements took: " << elapsed.count() << " milliseconds" << endl;
        cout << "Received " << response.daqvalue0().size() << " measurements." << endl;
        cout << "t0 Value: " << response.t0() << ", dt Value: " << response.dt() << endl;
		for (int x = 0; x < 10; ++x)
		{
        cout << "DMM Value: " << response.dmmvalue()[x] << ", DAQ Values: " << response.daqvalue0()[x] << ", " << response.daqvalue1()[x] << ", " << response.daqvalue2()[x] << ", " << response.daqvalue3()[x] << ", " << response.daqvalue4()[x] << ", " << response.daqvalue5()[x] << ", " << response.daqvalue6()[x] << ", " << response.daqvalue7()[x] << endl;
		}
		cout << "Error Status: " << response.errorstatus() << ", Error Code: " << response.errorcode() << ", Error Source: " << response.errorsource() << endl;
    }
	cout << "Streaming AI measurements" << endl;
    {
        auto startTime = chrono::steady_clock::now();
		ClientContext ctx;
        AnalogInputRequest request;
        AnalogInputData response;
		
		auto startstream = client.Query("startstream?");
		cout << "startstream?: " << startstream << endl;
		
        auto measurementReader = client.m_Stub->StreamAnalogInput(&ctx, request);
        int x=0;
        cout << "First Results: "  << endl;
        
		measurementReader->Read(&response);
		cout << "t0 Value: " << response.t0() << ", dt Value: " << response.dt() << endl;
		//cout << "DMM Value: " << response.dmmvalue()[x] << ", DAQ Values: " << response.daqvalue0()[x] << ", " << response.daqvalue1()[x] << ", " << response.daqvalue2()[x] << ", " << response.daqvalue3()[x] << ", " << response.daqvalue4()[x] << ", " << response.daqvalue5()[x] << ", " << response.daqvalue6()[x] << ", " << response.daqvalue7()[x] << endl;
				
		while (measurementReader->Read(&response))
        {
            if (++x <= 48)
            {
				//cout << "DMM Value: " << response.dmmvalue()[x] << ", DAQ Values: " << response.daqvalue0()[x] << ", " << response.daqvalue1()[x] << ", " << response.daqvalue2()[x] << ", " << response.daqvalue3()[x] << ", " << response.daqvalue4()[x] << ", " << response.daqvalue5()[x] << ", " << response.daqvalue6()[x] << ", " << response.daqvalue7()[x] << endl;
				for (int y = 0; y < 10; ++y)
				{
					cout << "DMM Value: " << response.dmmvalue()[y] << ", DAQ Values: " << response.daqvalue0()[y] << ", " << response.daqvalue1()[y] << ", " << response.daqvalue2()[y] << ", " << response.daqvalue3()[y] << ", " << response.daqvalue4()[y] << ", " << response.daqvalue5()[y] << ", " << response.daqvalue6()[y] << ", " << response.daqvalue7()[y] << endl;
				}
            }
			else
			{
				startstream = client.Query("startstream?");
				cout << "startstream?: " << startstream << endl;
				cout << "Error Status: " << response.errorstatus() << ", Error Code: " << response.errorcode() << ", Error Source: " << response.errorsource() << endl;
				cout << "Invoke stopstream" << endl;
				client.Invoke("stopstream", "");
			}
        }
		Status status = measurementReader->Finish();
		auto endTime = chrono::steady_clock::now();
        auto elapsed = chrono::duration_cast<chrono::milliseconds>(endTime - startTime);
		cout << "Analog Input measurements took: " << elapsed.count() << " milliseconds" << endl;
        cout << "Received " << response.daqvalue0().size()*50 << " measurements." << endl;
		
		while (elapsed.count() < 1000)
		{
			endTime = chrono::steady_clock::now();
			elapsed = chrono::duration_cast<chrono::milliseconds>(endTime - startTime);
		}
		startstream = client.Query("startstream?");
		cout << "startstream?: " << startstream << endl;
		cout << "Done!" << endl;
    }
}
