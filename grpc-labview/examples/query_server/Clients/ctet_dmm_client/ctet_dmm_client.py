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

# Open DMM Session
dmm_open_session_response = measurementServer.OpenDMMSession(ms.DMMOpenSessionRequest(DMMName = "DMM"))
print ("DMM Open Session")
print (dmm_open_session_response)
print("")

# DMM Reset
# Must have session open to the DMM
print ("DMM Reset")
dmm_reset_response = measurementServer.ResetDMM(ms.DMMResetRequest())
print (dmm_reset_response)
print("")

# # Open DMM Session
# dmm_open_session_response = measurementServer.OpenDMMSession(ms.DMMOpenSessionRequest(DMMName = "DMM"))
# print ("DMM Open Session")
# print (dmm_open_session_response)
# print("")

# # DMM Self Calibration
# # Must have session open to the DMM
# print ("DMM Self Calibration")
# print("Performing DMM Self Calibration - this may take a minute or two...")
# dmm_self_cal_response = measurementServer.SelfCalibrateDMM(ms.DMMSelfCalRequest())
# print (dmm_self_cal_response)
# print("")

# Open DMM Session
dmm_open_session_response = measurementServer.OpenDMMSession(ms.DMMOpenSessionRequest(DMMName = "DMM"))
print ("DMM Open Session")
print (dmm_open_session_response)
print("")

# Configure DMM
# DMMFunction = 0 (DC Volts), 1 (AC Volts), 2 (DC Current), 3 (AC Current), 4 (2-Wire Resistance), 5 (4-Wire Resistance)
# DMMResoluton = Resolution in Digits
# DMMRange = Range
# DMMSampleCount = Number of Measurements = 1
# DMMApertureTimeUnit = 0 (Seconds), 1 (Power Line Cycles)
# DMMApertureTime = Number of Apertures in Seconds or PLCs, if less than zero, then Resolution applies instead
# DMMNumberofAverages = Number of times a measurement is sampled and averaged before being placed on the buffer
# DMMAutoZero = -1 (Auto), 0 (Off), 1 (On), 2 (Once)
# DMMADCCalibration = -1 (Auto), 0 (Off), 1 (On)
# DMMSettleTime = Settle time in seconds
print ("DMM Configure")
dmm_config_response = measurementServer.ConfigureDMM(ms.DMMConfigRequest(
    DMMFunction = 2,
    DMMResolution = 5.5,
    DMMRange = 3,
    DMMSampleCount = 5,
    DMMApertureTimeUnit = 1,
    DMMApertureTime = 2,
    DMMNumberofAverages = 1,
    DMMAutoZero = 0,
    DMMADCCalibration = 0,
    DMMSettleTime = 0.0))
print("Function: " + str(dmm_config_response.DMMFunction))
print("Resolution: " + str(dmm_config_response.DMMResolution))
print("Range: " + str(dmm_config_response.DMMRange))
print("Sample Count: " + str(dmm_config_response.DMMSampleCount))
print("Aperture Time Unit: " + str(dmm_config_response.DMMApertureTimeUnit))
print("Aperture Time: " + str(dmm_config_response.DMMApertureTime))
print("Number of Averages: " + str(dmm_config_response.DMMNumberofAverages))
print("Auto Zero: " + str(dmm_config_response.DMMAutoZero))
print("ADC Calibration: " + str(dmm_config_response.DMMADCCalibration))
print("Settle Time: " + str(dmm_config_response.DMMSettleTime))
print("Error Code: " + str(dmm_config_response.error.errCode))
print("Error Message: " + str(dmm_config_response.error.errMessage))
# print(dmm_config_response.error)
# print(dmm_config_response)
print("")

#Perform DMM Voltage Measurement
dmm_result = measurementServer.PerformDMMMeasurement(ms.DMMMeasurementRequest())
print(dmm_result)
print ("")

# Close DMM Session
dmm_close_session_response = measurementServer.CloseDMMSession(ms.DMMCloseSessionRequest())
print ("DMM Close Session")
print (dmm_close_session_response)
print("")

# reader = measurementServer.Register(ms.RegistrationRequest(eventName = "Heartbeat"))

# for x in range(0, 5):
#     event = reader.next()
#     print ("Server Event: " + event.eventData)

# measurementServer.Invoke(ms.InvokeRequest(command = "Reset"))

print("Done")