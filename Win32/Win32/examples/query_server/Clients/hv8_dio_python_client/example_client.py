import time
import grpc
import dio_measurement_service_pb2 as ms
import dio_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "192.168.1.20:50051"
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# Open DI Session
di_open_session_response = measurementServer.OpenDISession(ms.DIOpenSessionRequest(
    DISessionName = "DISession1", 
    DIlines = "6514/port0/line0"))
print ("DI Open Session")
print (di_open_session_response)
print("")

# Read DI 
di_read_response = measurementServer.ReadDI(ms.ReadDIRequest(DIOSessionName = "DISession1"))
print ("DI Read")
print (di_read_response)
print("")

# Close DI Session
di_close_session_response = measurementServer.CloseDISession(ms.DICloseSessionRequest(DISessionName = "DISession1"))
print ("DI Close Session")
print (di_close_session_response)
print("")

# Open DO Session
do_open_session_response = measurementServer.OpenDOSession(ms.DOOpenSessionRequest(
    DOSessionName = "DOSession1",
    DOlines = "6514/port4/line0:5"))
print ("DO Open Session")
print (do_open_session_response)
print("")


# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [True, True, True, True, True, True]))
print ("DO Write")
print (do_write_response)
print("")
time.sleep(1)

# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [False, False, False, False, False, False]))
print ("DO Write")
print (do_write_response)
print("")
time.sleep(1)

# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [True, True, True, True, True, True]))
print ("DO Write")
print (do_write_response)
print("")
time.sleep(1)

# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [False, False, False, False, False, False]))
print ("DO Write")
print (do_write_response)
print("")
time.sleep(1)

# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [True, True, True, True, True, True]))
print ("DO Write")
print (do_write_response)
print("")

# Write DO
do_write_response = measurementServer.WriteDO(ms.WriteDORequest(
    DIOSessionName = "DOSession1",
    DOData = [False, False, False, False, False, False]))
print ("DO Write")
print (do_write_response)
print("")
time.sleep(1)

# Close DO Session
do_close_session_response = measurementServer.CloseDOSession(ms.DOCloseSessionRequest(DOSessionName = "DOSession1"))
print ("DO Close Session")
print (do_close_session_response)
print("")

# # Start PWM
# # PWMInitialState = (True, False)
# # PWMInvertLines = (True, False)
# # PWMFrequency = (10 Hz to 1000 Hz)
# pwm_start_response = measurementServer.StartPWM(ms.PWMStartRequest(
#     PWMInitialState = True,
#     PWMInvertLines = True,
#     PWMFrequency = 1000))
# print ("PWM Start")
# print (pwm_start_response)
# print("")

# Frequencies = [1000, 500, 100, 50, 10]

# for x in Frequencies:
#     # Modify PWM Frequency
#     # PWMFrequency = (10 Hz to 1000 Hz)
#     # Duty cycle at 1000 Hz is not 50%, closer to 58%
#     pwm_modify_response = measurementServer.ModifyPWM(ms.PWMModifyRequest(PWMFrequency = x))
#     print ("Modify PWM Frequency")
#     print (pwm_modify_response)
#     print("")
#     time.sleep(10)

# # Stop PWM
# pwm_stop_response = measurementServer.StopPWM(ms.PWMStopRequest())
# print ("PWM Stop")
# print (pwm_stop_response)
# print("")


