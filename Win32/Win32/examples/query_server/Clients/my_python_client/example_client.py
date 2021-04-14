import time
import grpc
import hvc_measurement_service_pb2 as ms
import hvc_measurement_service_pb2_grpc as msgrpc
 
serverAddress = "192.168.1.20:50051"
#192.168.1.x (prefer 20-30) (not 5, 10, 60)
# serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
 
# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)
print("")

# # Open DMM Session
# dmm_open_session_response = measurementServer.OpenDMMSession(ms.DMMOpenSessionRequest(DMMName = "DMM"))
# print ("DMM Open Session")
# print (dmm_open_session_response)
# print("")

# # DMM Reset
# # Must have session open to the DMM
# print ("DMM Reset")
# dmm_reset_response = measurementServer.ResetDMM(ms.DMMResetRequest())
# print (dmm_reset_response)
# print("")

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

# # Open DMM Session
# dmm_open_session_response = measurementServer.OpenDMMSession(ms.DMMOpenSessionRequest(DMMName = "DMM"))
# print ("DMM Open Session")
# print (dmm_open_session_response)
# print("")

# # Configure DMM
# # DMMFunction = 0 (DC Volts), 1 (AC Volts), 2 (DC Current), 3 (AC Current), 4 (2-Wire Resistance), 5 (4-Wire Resistance)
# # DMMResoluton = Resolution in Digits
# # DMMRange = Range in Volts
# # DMMSampleCount = Number of Measurements = 1
# # DMMApertureTimeUnit = 0 (Seconds), 1 (Power Line Cycles)
# # DMMApertureTime = Number of Apertures in Seconds or PLCs, if less than zero, then Resolution applies instead
# # DMMNumberofAverages = Number of times a measurement is sampled and averaged before being placed on the buffer
# # DMMAutoZero = -1 (Auto), 0 (Off), 1 (On), 2 (Once)
# # DMMADCCalibration = -1 (Auto), 0 (Off), 1 (On)
# # DMMSettleTime = Settle time in seconds
# dmm_config_response = measurementServer.ConfigureDMM(ms.DMMConfigRequest(
#     DMMFunction = 0,
#     DMMResolution = 5.5,
#     DMMRange = 8.0,
#     DMMSampleCount = 10,
#     DMMApertureTimeUnit = 1,
#     DMMApertureTime = 2,
#     DMMNumberofAverages = 1,
#     DMMAutoZero = 0,
#     DMMADCCalibration = 0,
#     DMMSettleTime = 0.0))
# print("Function: " + str(dmm_config_response.DMMFunction))
# print("Resolution: " + str(dmm_config_response.DMMResolution))
# print("Range: " + str(dmm_config_response.DMMRange))
# print("Sample Count: " + str(dmm_config_response.DMMSampleCount))
# print("Aperture Time Unit: " + str(dmm_config_response.DMMApertureTimeUnit))
# print("Aperture Time: " + str(dmm_config_response.DMMApertureTime))
# print("Number of Averages: " + str(dmm_config_response.DMMNumberofAverages))
# print("Auto Zero: " + str(dmm_config_response.DMMAutoZero))
# print("ADC Calibration: " + str(dmm_config_response.DMMADCCalibration))
# print("Settle Time: " + str(dmm_config_response.DMMSettleTime))
# print("Error Code: " + str(dmm_config_response.error.errCode))
# print("Error Message: " + str(dmm_config_response.error.errMessage))
# # print(dmm_config_response.error)
# # print(dmm_config_response)
# print("")

# #Perform DMM Voltage Measurement
# dmm_voltage_result = measurementServer.PerformDMMVoltageMeasurement(ms.DMMVoltageRequest())
# print(dmm_voltage_result)
# print ("")

# # Close DMM Session
# dmm_close_session_response = measurementServer.CloseDMMSession(ms.DMMCloseSessionRequest())
# print ("DMM Close Session")
# print (dmm_close_session_response)
# print("")

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

# Open SMU Session
smu_open_session_response = measurementServer.OpenSMUSession(ms.SMUOpenSessionRequest(SMUName = "SMU"))
print ("SMU Open Session")
print (smu_open_session_response)
print("")

# SMU Self Calibration
# Must have session open to the SMU
print ("SMU Self Calibration")
print("Performing SMU Self Calibration - this may take a few seconds...")
smu_self_cal_response = measurementServer.SelfCalibrateSMU(ms.SMUSelfCalRequest())
print (smu_self_cal_response)
print("")

# Open SMU Session
smu_open_session_response = measurementServer.OpenSMUSession(ms.SMUOpenSessionRequest(SMUName = "SMU"))
print ("SMU Open Session")
print (smu_open_session_response)
print("")

# Configure SMU
# SMUChannels = "0" 
# SMUSourceMode = 1020 (Single Point), 1021 (Sequence)
# SMUOutputFunction = 1006 (DC Voltage), 1007 (DC Current), 1049 (Pulse Voltage), 1050 (Pulse Current)
# SMUSourceTransientResponse = 1041 (Slow), 1038 (Normal), 1039 (Fast), 1042 (Custom)
# SMUCurrent = Current Level
# SMUCurrentLevelRange = Current Level Range (up to 3 A with NI 4139)
# SMUMeasurementSense = 1008 (Local), 1009 (Remote)
# SMUMeasurementApertureTime = Aperture Time in seconds
# SMUSourceAdvancedSourceDelay = Source Delay in seconds
# SMUVoltage = Voltage Limit and Voltage Limit Range
# SMUMeasurementAdvancedDCNoiseRejection = 1044 (Normal), 1043 (Second-Order)

smu_config_response = measurementServer.ConfigureSMU(ms.SMUConfigRequest(
    SMUChannels = "0",
    SMUSourceMode = 1020,
    SMUOutputFunction = 1007,
    SMUSourceTransientResponse = 1038,
    SMUCurrent = 0.020,
    SMUCurrentLevelRange = 0.020,
    SMUMeasurementSense = 1008,
    SMUMeasurementApertureTime = 0.033,
    SMUSourceAdvancedSourceDelay = 0.001,
    SMUVoltage = 6,
    SMUMeasurementAdvancedDCNoiseRejection = 1044))
print("Channels: " + str(smu_config_response.SMUChannels))
print("Source Mode: " + str(smu_config_response.SMUSourceMode))
print("Output Function: " + str(smu_config_response.SMUOutputFunction))
print("Source Transient Response: " + str(smu_config_response.SMUSourceTransientResponse))
print("Current Level: " + str(smu_config_response.SMUCurrent))
print("Current Level Range: " + str(smu_config_response.SMUCurrentLevelRange))
print("Measurement Sense: " + str(smu_config_response.SMUMeasurementSense))
print("Measurement Aperture Time: " + str(smu_config_response.SMUMeasurementApertureTime))
print("Source Delay: " + str(smu_config_response.SMUSourceAdvancedSourceDelay))
print("Voltage Level and Limit: " + str(smu_config_response.SMUVoltage))
print("DC Noise Rejection: " + str(smu_config_response.SMUMeasurementAdvancedDCNoiseRejection))
print("Error Code: " + str(smu_config_response.error.errCode))
print("Error Message: " + str(smu_config_response.error.errMessage))
print(smu_config_response.error)
# print(smu_config_response)
print("")

#Perform SMU Current Measurement
smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
print("Perform SMU Current Measurement")
print(smu_current_result)
print("")
time.sleep(1)

# Disable SMU Output
smu_disable_result = measurementServer.DisableSMUOutput(ms.SMUDisableRequest())
print("Disable SMU Output")
print(smu_disable_result)
print("")

smu_config_response = measurementServer.ConfigureSMU(ms.SMUConfigRequest(
    SMUChannels = "0",
    SMUSourceMode = 1020,
    SMUOutputFunction = 1007,
    SMUSourceTransientResponse = 1038,
    SMUCurrent = 0.020,
    SMUCurrentLevelRange = 0.020,
    SMUMeasurementSense = 1008,
    SMUMeasurementApertureTime = 0.033,
    SMUSourceAdvancedSourceDelay = 0.001,
    SMUVoltage = 6,
    SMUMeasurementAdvancedDCNoiseRejection = 1044))
print("Channels: " + str(smu_config_response.SMUChannels))
print("Source Mode: " + str(smu_config_response.SMUSourceMode))
print("Output Function: " + str(smu_config_response.SMUOutputFunction))
print("Source Transient Response: " + str(smu_config_response.SMUSourceTransientResponse))
print("Current Level: " + str(smu_config_response.SMUCurrent))
print("Current Level Range: " + str(smu_config_response.SMUCurrentLevelRange))
print("Measurement Sense: " + str(smu_config_response.SMUMeasurementSense))
print("Measurement Aperture Time: " + str(smu_config_response.SMUMeasurementApertureTime))
print("Source Delay: " + str(smu_config_response.SMUSourceAdvancedSourceDelay))
print("Voltage Level and Limit: " + str(smu_config_response.SMUVoltage))
print("DC Noise Rejection: " + str(smu_config_response.SMUMeasurementAdvancedDCNoiseRejection))
print("Error Code: " + str(smu_config_response.error.errCode))
print("Error Message: " + str(smu_config_response.error.errMessage))
print(smu_config_response.error)
# print(smu_config_response)
print("")

# #Perform SMU Current Measurement
# smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
# print("Perform SMU Current Measurement")
# print(smu_current_result)
# print("")

# Enable SMU Output
smu_enable_result = measurementServer.EnableSMUOutput(ms.SMUEnableRequest())
print("Enable SMU Output")
print(smu_enable_result)
print("")

#Perform SMU Current Measurement
smu_current_result = measurementServer.PerformSMUCurrentMeasurement(ms.SMUCurrentRequest())
print("Perform SMU Current Measurement")
print(smu_current_result)
print("")

# Close SMU Session
smu_close_session_response = measurementServer.CloseSMUSession(ms.SMUCloseSessionRequest())
print ("SMU Close Session")
print (smu_close_session_response)
print("")

# # Open NI 2576 Session
# ni2576_open_session_response = measurementServer.OpenNI2576MUXSession(ms.NI2576MUXOpenSessionRequest(
#     NI2576MUXName = "2576",
#     NI2576MUXTopology = "2576/2-Wire 64x1 Mux"))
# print ("NI 2576 Open Session")
# print (ni2576_open_session_response)
# print("")

# # Reset NI 2576
# ni2576_reset_response = measurementServer.ResetNI2576MUX(ms.NI2576MUXResetRequest())
# print ("NI 2576 Reset")
# print (ni2576_reset_response)
# print ("")

# # Close NI 2576 Session
# ni2576_close_session_response = measurementServer.CloseNI2576MUXSession(ms.NI2576MUXCloseSessionRequest())
# print ("NI 2576 Close Session")
# print (ni2576_close_session_response)
# print("")

# # Open NI 2576 Session
# ni2576_open_session_response = measurementServer.OpenNI2576MUXSession(ms.NI2576MUXOpenSessionRequest(
#     NI2576MUXName = "2576",
#     NI2576MUXTopology = "2576/2-Wire 64x1 Mux"))
# print ("NI 2576 Open Session")
# print (ni2576_open_session_response)
# print("")

# # Close NI 2576 Channel
# # Channel1 = "ch0" (chx)
# # Channel2 = "com0"
# ni2576_close_channel_response = measurementServer.CloseNI2576MUXChannel(ms.NI2576MUXCloseChannelRequest(
#     Channel1 = "ch0",
#     Channel2 = "com0"
# ))
# print ("NI 2576 Close ch0->com0")
# print (ni2576_close_channel_response)
# print ("")

# # Open NI 2576 Channel
# # Channel1 = "ch0" (chx)
# # Channel2 = "com0"
# ni2576_open_channel_response = measurementServer.OpenNI2576MUXChannel(ms.NI2576MUXOpenChannelRequest(
#     Channel1 = "ch0",
#     Channel2 = "com0"
# ))
# print ("NI 2576 Open ch0->com0")
# print (ni2576_open_channel_response)
# print ("")

# # Disconnect All NI 2576
# ni2576_disconnect_all_response = measurementServer.DisconnectAllNI2576MUXChannels(ms.NI2576MUXDisconnectAllRequest())
# print ("NI 2576 Disconnect All")
# print (ni2576_disconnect_all_response)
# print ("")

# # Close NI 2576 Session
# ni2576_close_session_response = measurementServer.CloseNI2576MUXSession(ms.NI2576MUXCloseSessionRequest())
# print ("NI 2576 Close Session")
# print (ni2576_close_session_response)
# print("")