import time
import grpc
import ctet_smu_measurement_service_pb2 as ms
import ctet_smu_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "192.168.1.20:50051"
#192.168.1.x (prefer 20-30) (not 5, 10, 60)
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# # Open SMU Session
# smu_open_session_response = measurementServer.OpenSMUSession(ms.SMUOpenSessionRequest(SMUName = "SMU"))
# print ("SMU Open Session")
# print (smu_open_session_response)
# print("")

# # SMU Reset
# # Must have session open to the SMU
# print ("SMU Reset")
# print("Performing SMU Reset - this may take a few seconds...")
# smu_reset_response = measurementServer.ResetSMU(ms.SMUResetRequest())
# print (smu_reset_response)
# print("")

# # Open SMU Session
# smu_open_session_response = measurementServer.OpenSMUSession(ms.SMUOpenSessionRequest(SMUName = "SMU"))
# print ("SMU Open Session")
# print (smu_open_session_response)
# print("")

# # SMU Self Calibration
# # Must have session open to the SMU
# print ("SMU Self Calibration")
# print("Performing SMU Self Calibration - this may take a few seconds...")
# smu_self_cal_response = measurementServer.SelfCalibrateSMU(ms.SMUSelfCalRequest())
# print (smu_self_cal_response)
# print("")

# # Open SMU Session
# smu_open_session_response = measurementServer.OpenSMUSession(ms.SMUOpenSessionRequest(SMUName = "SMU"))
# print ("SMU Open Session")
# print (smu_open_session_response)
# print("")

# # Configure SMU
# # SMUChannels = "0" 
# # SMUSourceMode = 1020 (Single Point), 1021 (Sequence)
# # SMUOutputFunction = 1006 (DC Voltage), 1007 (DC Current), 1049 (Pulse Voltage), 1050 (Pulse Current)
# # SMUSourceTransientResponse = 1041 (Slow), 1038 (Normal), 1039 (Fast), 1042 (Custom)
# # SMUCurrent = Current Level
# # SMUCurrentLevelRange = Current Level Range (up to 3 A with NI 4139)
# # SMUMeasurementSense = 1008 (Local), 1009 (Remote)
# # SMUMeasurementApertureTime = Aperture Time in seconds
# # SMUSourceAdvancedSourceDelay = Source Delay in seconds
# # SMUVoltage = Voltage Limit and Voltage Limit Range
# # SMUMeasurementAdvancedDCNoiseRejection = 1044 (Normal), 1043 (Second-Order)

# smu_config_response = measurementServer.ConfigureSMU(ms.SMUConfigRequest(
#     SMUChannels = "0",
#     SMUSourceMode = 1020,
#     SMUOutputFunction = 1007,
#     SMUSourceTransientResponse = 1038,
#     SMUCurrent = -1,
#     SMUCurrentLevelRange = 3,
#     SMUMeasurementSense = 1008,
#     SMUMeasurementApertureTime = 0.033,
#     SMUSourceAdvancedSourceDelay = 0.001,
#     SMUVoltage = 12,
#     SMUMeasurementAdvancedDCNoiseRejection = 1044))
# print("Channels: " + str(smu_config_response.SMUChannels))
# print("Source Mode: " + str(smu_config_response.SMUSourceMode))
# print("Output Function: " + str(smu_config_response.SMUOutputFunction))
# print("Source Transient Response: " + str(smu_config_response.SMUSourceTransientResponse))
# print("Current Level: " + str(smu_config_response.SMUCurrent))
# print("Current Level Range: " + str(smu_config_response.SMUCurrentLevelRange))
# print("Measurement Sense: " + str(smu_config_response.SMUMeasurementSense))
# print("Measurement Aperture Time: " + str(smu_config_response.SMUMeasurementApertureTime))
# print("Source Delay: " + str(smu_config_response.SMUSourceAdvancedSourceDelay))
# print("Voltage Level and Limit: " + str(smu_config_response.SMUVoltage))
# print("DC Noise Rejection: " + str(smu_config_response.SMUMeasurementAdvancedDCNoiseRejection))
# print("Error Code: " + str(smu_config_response.error.errCode))
# print("Error Message: " + str(smu_config_response.error.errMessage))
# print(smu_config_response.error)
# # print(smu_config_response)
# print("")

# #Perform SMU Current Measurement
# smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
# print("Perform SMU Current Measurement")
# print(smu_current_result)
# print("")
# time.sleep(10)

# # Disable SMU Output
# smu_disable_result = measurementServer.DisableSMUOutput(ms.SMUDisableRequest())
# print("Disable SMU Output")
# print(smu_disable_result)
# print("")

# smu_config_response = measurementServer.ConfigureSMU(ms.SMUConfigRequest(
#     SMUChannels = "0",
#     SMUSourceMode = 1020,
#     SMUOutputFunction = 1007,
#     SMUSourceTransientResponse = 1038,
#     SMUCurrent = -1.6,
#     SMUCurrentLevelRange = 3,
#     SMUMeasurementSense = 1008,
#     SMUMeasurementApertureTime = 0.033,
#     SMUSourceAdvancedSourceDelay = 0.001,
#     SMUVoltage = 12,
#     SMUMeasurementAdvancedDCNoiseRejection = 1044))
# print("Channels: " + str(smu_config_response.SMUChannels))
# print("Source Mode: " + str(smu_config_response.SMUSourceMode))
# print("Output Function: " + str(smu_config_response.SMUOutputFunction))
# print("Source Transient Response: " + str(smu_config_response.SMUSourceTransientResponse))
# print("Current Level: " + str(smu_config_response.SMUCurrent))
# print("Current Level Range: " + str(smu_config_response.SMUCurrentLevelRange))
# print("Measurement Sense: " + str(smu_config_response.SMUMeasurementSense))
# print("Measurement Aperture Time: " + str(smu_config_response.SMUMeasurementApertureTime))
# print("Source Delay: " + str(smu_config_response.SMUSourceAdvancedSourceDelay))
# print("Voltage Level and Limit: " + str(smu_config_response.SMUVoltage))
# print("DC Noise Rejection: " + str(smu_config_response.SMUMeasurementAdvancedDCNoiseRejection))
# print("Error Code: " + str(smu_config_response.error.errCode))
# print("Error Message: " + str(smu_config_response.error.errMessage))
# print(smu_config_response.error)
# # print(smu_config_response)
# print("")

# # #Perform SMU Current Measurement
# # smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
# # print("Perform SMU Current Measurement")
# # print(smu_current_result)
# # print("")

# # Enable SMU Output
# smu_enable_result = measurementServer.EnableSMUOutput(ms.SMUEnableRequest())
# print("Enable SMU Output")
# print(smu_enable_result)
# print("")

# #Perform SMU Current Measurement
# smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
# print("Perform SMU Current Measurement")
# print(smu_current_result)
# print("")