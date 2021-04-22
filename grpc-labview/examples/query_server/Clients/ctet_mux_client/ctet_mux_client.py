import time
import grpc
import ctet_mux_measurement_service_pb2 as ms
import ctet_mux_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "192.168.1.20:50051"
#192.168.1.x (prefer 20-30) (not 5, 10, 60)
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# Open NI 2576 Session
mux_open_session_response = measurementServer.OpenMUXSession(ms.MUXOpenSessionRequest(
    MUXName = "2576",
    MUXTopology = "2576/2-Wire 64x1 Mux"))
print ("NI 2576 Open Session")
print (mux_open_session_response)
print("")

# Reset NI 2576
mux_reset_response = measurementServer.ResetMUX(ms.MUXResetRequest())
print ("NI 2576 Reset")
print (mux_reset_response)
print ("")

# Close NI 2576 Session
mux_close_session_response = measurementServer.CloseMUXSession(ms.MUXCloseSessionRequest())
print ("NI 2576 Close Session")
print (mux_close_session_response)
print("")

# Open NI 2576 Session
mux_open_session_response = measurementServer.OpenMUXSession(ms.MUXOpenSessionRequest(
    MUXName = "2576",
    MUXTopology = "2576/2-Wire 64x1 Mux"))
print ("NI 2576 Open Session")
print (mux_open_session_response)
print("")

# Get MUX Channel Names
mux_channel_names = measurementServer.GetMUXChannelNames(ms.MUXGetChannelNamesRequest())
print ("NI 2576 Channel Names")
print (mux_channel_names)
print ("")

# Close NI 2576 Channel
# Channel1 = "ch0" (chx)
# Channel2 = "com0"
mux_close_channel_response = measurementServer.CloseMUXChannel(ms.MUXCloseChannelRequest(
    Channel1 = "ch0",
    Channel2 = "com0"
))
print ("NI 2576 Close ch0->com0")
print (mux_close_channel_response)
print ("")

# Get MUX Switch Status
mux_status = measurementServer.GetMUXStatus(ms.MUXGetStatusRequest())
print ("NI 2576 Status")
print (mux_status)
print ("")

# Open NI 2576 Channel
# Channel1 = "ch0" (chx)
# Channel2 = "com0"
mux_open_channel_response = measurementServer.OpenMUXChannel(ms.MUXOpenChannelRequest(
    Channel1 = "ch0",
    Channel2 = "com0"
))
print ("NI 2576 Open ch0->com0")
print (mux_open_channel_response)
print ("")

# Disconnect All NI 2576
mux_disconnect_all_response = measurementServer.DisconnectAllMUXChannels(ms.MUXDisconnectAllRequest())
print ("NI 2576 Disconnect All")
print (mux_disconnect_all_response)
print ("")

# Close NI 2576 Session
mux_close_session_response = measurementServer.CloseMUXSession(ms.MUXCloseSessionRequest())
print ("NI 2576 Close Session")
print (mux_close_session_response)
print("")

# Open NI 2576 Session
mux_open_session_response = measurementServer.OpenMUXSession(ms.MUXOpenSessionRequest(
    MUXName = "2576",
    MUXTopology = "2576/2-Wire 64x1 Mux"))
print ("NI 2576 Open Session")
print (mux_open_session_response)
print("")

# Get MUX Relay Info
mux_relay_info = measurementServer.GetMUXRelayInfo(ms.MUXGetRelayInfoRequest())
print ("NI 2576 Relay Info")
print (mux_relay_info)
print ("")

# Close NI 2576 Relay
# RelayName = "k0" (kx)
mux_close_relay_response = measurementServer.CloseMUXRelay(ms.MUXCloseRelayRequest(RelayName = "k0"))
print ("NI 2576 Close k0")
print (mux_close_relay_response)
print ("")

# Get MUX Switch Status
mux_status = measurementServer.GetMUXStatus(ms.MUXGetStatusRequest())
print ("NI 2576 Status")
print (mux_status)
print ("")

# Open NI 2576 Relay
# RelayName = "k0" (kx)
mux_open_relay_response = measurementServer.OpenMUXRelay(ms.MUXOpenRelayRequest(RelayName = "k0"))
print ("NI 2576 Open k0")
print (mux_open_relay_response)
print ("")

# Close All NI 2576 Relays
mux_close_all_relays_response = measurementServer.CloseMUXAllRelays(ms.MUXCloseAllRequest())
print ("NI 2576 Close All Relays")
print (mux_close_all_relays_response)
print ("")

# Get MUX Switch Status
mux_status = measurementServer.GetMUXStatus(ms.MUXGetStatusRequest())
print ("NI 2576 Status")
print (mux_status)
print ("")

# Disconnect All NI 2576
mux_disconnect_all_response = measurementServer.DisconnectAllMUXChannels(ms.MUXDisconnectAllRequest())
print ("NI 2576 Disconnect All")
print (mux_disconnect_all_response)
print ("")

# Get MUX Switch Status
mux_status = measurementServer.GetMUXStatus(ms.MUXGetStatusRequest())
print ("NI 2576 Status")
print (mux_status)
print ("")

# Close NI 2576 Session
mux_close_session_response = measurementServer.CloseMUXSession(ms.MUXCloseSessionRequest())
print ("NI 2576 Close Session")
print (mux_close_session_response)
print("")