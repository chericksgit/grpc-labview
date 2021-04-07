//---------------------------------------------------------------------
//---------------------------------------------------------------------
#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <data_marshal.grpc.pb.h>
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
    request.set_rootfloat(37.56f);

    request.mutable_repeateddoublevalue()->Add(1.1f);
    request.mutable_repeateddoublevalue()->Add(2.2f);
    request.mutable_repeateddoublevalue()->Add(3.3f);
    request.mutable_repeateddoublevalue()->Add(4.4f);
    request.mutable_repeateddoublevalue()->Add(5.5f);
    request.mutable_repeateddoublevalue()->Add(6.6f);

    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(false);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(true);
    request.mutable_repeatedboolvalue()->Add(false);

    request.mutable_repeatedfloatvalue()->Add(1.23f);
    request.mutable_repeatedfloatvalue()->Add(2.23f);
    request.mutable_repeatedfloatvalue()->Add(3.23f);
    request.mutable_repeatedfloatvalue()->Add(4.23f);
    request.mutable_repeatedfloatvalue()->Add(5.23f);
    request.mutable_repeatedfloatvalue()->Add(6.23f);

    request.mutable_nested()->set_boolvalaue(true);
    request.mutable_nested()->set_doublevalue(12.12);
    request.mutable_nested()->set_intvalue(4242);
    request.mutable_nested()->set_floatvalue(15.14f);

    auto nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(true);
    nested->set_floatvalue(1.1f);
    nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(false);
    nested->set_floatvalue(2.2f);
    nested = request.mutable_repeatednested()->Add();
    nested->set_boolvalaue(true);
    nested->set_floatvalue(3.3f);

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

    DoDataTypeTest(client);

    auto result = client.Query("Uptime");
    cout << "Server uptime: " << result << endl;

    auto reader = client.Register("Heartbeat");
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
}
