import time
import grpc
import ni2564_dual_measurement_service_pb2 as ms
import ni2564_dual_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "192.168.1.20:50051"
#192.168.1.x (prefer 20-30) (not 5, 10, 60)
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# Open NI 2564A Session
ni2564A_open_session_response = measurementServer.OpenNI2564ASession(ms.NI2564OpenSessionRequest(
    NI2564Name = "2564A",
    NI2564Topology = "2564/16-SPST"))
print ("NI 2564A Open Session")
print (ni2564A_open_session_response)
print("")

# Open NI 2564B Session
ni2564B_open_session_response = measurementServer.OpenNI2564BSession(ms.NI2564OpenSessionRequest(
    NI2564Name = "2564B",
    NI2564Topology = "2564/16-SPST"))
print ("NI 2564B Open Session")
print (ni2564B_open_session_response)
print("")

# # Reset NI 2564A
# ni2564A_reset_response = measurementServer.ResetNI2564A(ms.NI2564ResetRequest())
# print ("NI 2564A Reset")
# print (ni2564A_reset_response)
# print ("")

# # Reset NI 2564B
# ni2564B_reset_response = measurementServer.ResetNI2564B(ms.NI2564ResetRequest())
# print ("NI 2564B Reset")
# print (ni2564B_reset_response)
# print ("")

# Disconnect All NI 2564A
ni2564A_disconnect_all_response = measurementServer.DisconnectAllNI2564AChannels(ms.NI2564DisconnectAllRequest())
print ("NI 2564A Disconnect All")
print (ni2564A_disconnect_all_response)
print ("")

# Disconnect All NI 2564B
ni2564B_disconnect_all_response = measurementServer.DisconnectAllNI2564BChannels(ms.NI2564DisconnectAllRequest())
print ("NI 2564B Disconnect All")
print (ni2564B_disconnect_all_response)
print ("")

# Close NI 2564A Session
ni2564A_close_session_response = measurementServer.CloseNI2564ASession(ms.NI2564CloseSessionRequest())
print ("NI 2564A Close Session")
print (ni2564A_close_session_response)
print("")

# Close NI 2564B Session
ni2564B_close_session_response = measurementServer.CloseNI2564BSession(ms.NI2564CloseSessionRequest())
print ("NI 2564B Close Session")
print (ni2564B_close_session_response)
print("")

# Open NI 2564A Session
ni2564A_open_session_response = measurementServer.OpenNI2564ASession(ms.NI2564OpenSessionRequest(
    NI2564Name = "2564A",
    NI2564Topology = "2564/16-SPST"))
print ("NI 2564A Open Session")
print (ni2564A_open_session_response)
print("")

# Open NI 2564B Session
ni2564B_open_session_response = measurementServer.OpenNI2564BSession(ms.NI2564OpenSessionRequest(
    NI2564Name = "2564B",
    NI2564Topology = "2564/16-SPST"))
print ("NI 2564B Open Session")
print (ni2564B_open_session_response)
print("")

# # Open NI 2564 Session
# ni2564_open_session_response = measurementServer.OpenNI2564Session(ms.NI2564OpenSessionRequest(
#     NI2564Name = "2564A",
#     NI2564Topology = "2564/16-SPST"))
# print ("NI 2564 Open Session")
# print (ni2564_open_session_response)
# print("")

# # Close NI 2564A Channel
# # Channel1 = "ch0" (chx)
# # Channel2 = "com0" (comx)

# # Close NI 2564B Channel
# # Channel1 = "ch0" (chx)
# # Channel2 = "com0" (comx)

for x in range (0, 15):

    ni2564A_close_channel_response = measurementServer.CloseNI2564AChannel(ms.NI2564CloseChannelRequest(
        Channel1 = "ch" + str(x),
        Channel2 = "com" + str(x)
    ))
    print ("NI 2564A Close ch" + str(x) + "->com" + str(x))
    print (ni2564A_close_channel_response)
    ni2564B_close_channel_response = measurementServer.CloseNI2564BChannel(ms.NI2564CloseChannelRequest(
        Channel1 = "ch" + str(x),
        Channel2 = "com" + str(x)
    ))
    print ("NI 2564B Close ch" + str(x) + "->com" + str(x))
    print (ni2564B_close_channel_response)
    time.sleep(1)

print ("")

# Open NI 2564A Channel
# Channel1 = "ch0" (chx)
# Channel2 = "com0" (com0)

# Open NI 2564B Channel
# Channel1 = "ch0" (chx)
# Channel2 = "com0" (com0)

for x in range (0, 15):

    ni2564A_open_channel_response = measurementServer.OpenNI2564AChannel(ms.NI2564OpenChannelRequest(
        Channel1 = "ch" + str(x),
        Channel2 = "com" + str(x)
    ))
    print ("NI 2564A Open ch" + str(x) + "->com" + str(x))
    print (ni2564A_open_channel_response)
    ni2564B_open_channel_response = measurementServer.OpenNI2564BChannel(ms.NI2564OpenChannelRequest(
        Channel1 = "ch" + str(x),
        Channel2 = "com" + str(x)
    ))
    print ("NI 2564B Open ch" + str(x) + "->com" + str(x))
    print (ni2564B_open_channel_response)
    time.sleep(1)

print ("")

# Close NI 2564A Session
ni2564A_close_session_response = measurementServer.CloseNI2564ASession(ms.NI2564CloseSessionRequest())
print ("NI 2564A Close Session")
print (ni2564A_close_session_response)
print("")

# Close NI 2564B Session
ni2564B_close_session_response = measurementServer.CloseNI2564BSession(ms.NI2564CloseSessionRequest())
print ("NI 2564B Close Session")
print (ni2564B_close_session_response)
print("")