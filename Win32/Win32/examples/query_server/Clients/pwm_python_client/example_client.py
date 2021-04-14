import time
import grpc
import pwm_measurement_service_pb2 as ms
import pwm_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "169.254.184.38:50051"
#192.168.1.x (prefer 20-30) (not 5, 10, 60)
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# Open PWM Session
pwm_open_session_response = measurementServer.OpenPWMSession(ms.PWMOpenSessionRequest(PWMlines = "6514/port4/line0"))
print ("PWM Open Session")
print (pwm_open_session_response)
print("")

# Start PWM
# PWMInitialState = (True, False)
# PWMInvertLines = (True, False)
# PWMFrequency = (10 Hz to 1000 Hz)
pwm_start_response = measurementServer.StartPWM(ms.PWMStartRequest(
    PWMInitialState = True,
    PWMInvertLines = True,
    PWMFrequency = 1000))
print ("PWM Start")
print (pwm_start_response)
print("")

Frequencies = [1000, 500, 100, 50, 10]

for x in Frequencies:
    # Modify PWM Frequency
    # PWMFrequency = (10 Hz to 1000 Hz)
    # Duty cycle at 1000 Hz is not 50%, closer to 58%
    pwm_modify_response = measurementServer.ModifyPWM(ms.PWMModifyRequest(PWMFrequency = x))
    print ("Modify PWM Frequency")
    print (pwm_modify_response)
    print("")
    time.sleep(10)

# Stop PWM
pwm_stop_response = measurementServer.StopPWM(ms.PWMStopRequest())
print ("PWM Stop")
print (pwm_stop_response)
print("")

# Close PWM Session
pwm_close_session_response = measurementServer.ClosePWMSession(ms.PWMCloseSessionRequest())
print ("PWM Close Session")
print (pwm_close_session_response)
print("")
