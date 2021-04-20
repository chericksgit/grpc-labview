import grpc
import ctet_dmm_measurement_service_pb2 as ms
import ctet_dmm_measurement_service_pb2_grpc as msgrpc

# This is the location (ipaddress or machine name):(port) of the niDevice server
# serverAddress = "localhost:50051"
serverAddress = "192.168.1.20:50051"

# Create the communcation channel for the remote host (in this case we are connecting to a local server)
# and create a connection to the niScope service
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)

# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)

# reader = measurementServer.Register(ms.RegistrationRequest(eventName = "Heartbeat"))

# for x in range(0, 5):
#     event = reader.next()
#     print ("Server Event: " + event.eventData)

# measurementServer.Invoke(ms.InvokeRequest(command = "Reset"))

print("Done")