import grpc
import measurement_service_old3_pb2 as ms
import measurement_service_old3_pb2_grpc as msgrpc

serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
result = measurementServer.PerformOCVMeasurement(ms.OCVRequest())
print("Voltage 1:" + str(result.data[0].battery1voltage))
print("Voltage 2:" + str(result.data[0].battery2voltage))
print("Voltage 3:" + str(result.data[0].battery3voltage))
print("Voltage 4:" + str(result.data[0].battery4voltage))
print("Voltage 5:" + str(result.data[0].battery5voltage))
print("Voltage 6:" + str(result.data[0].battery6voltage))
print("Voltage 7:" + str(result.data[0].battery7voltage))
print("Voltage 8:" + str(result.data[0].battery8voltage))
print("Voltage 9:" + str(result.data[0].battery9voltage))
print("Voltage 10:" + str(result.data[0].battery10voltage))

print("Voltage 11:" + str(result.data[0].battery11voltage))
print("Voltage 12:" + str(result.data[0].battery12voltage))
print("Voltage 13:" + str(result.data[0].battery13voltage))
print("Voltage 14:" + str(result.data[0].battery14voltage))
print("Voltage 15:" + str(result.data[0].battery15voltage))
print("Voltage 16:" + str(result.data[0].battery16voltage))
print("Voltage 17:" + str(result.data[0].battery17voltage))
print("Voltage 18:" + str(result.data[0].battery18voltage))
print("Voltage 19:" + str(result.data[0].battery19voltage))
print("Voltage 20:" + str(result.data[0].battery20voltage))

print("Voltage 21:" + str(result.data[0].battery21voltage))
print("Voltage 22:" + str(result.data[0].battery22voltage))
print("Voltage 23:" + str(result.data[0].battery23voltage))
# print("Voltage 24:" + str(result.data[0].battery24voltage))

# print("Error Code:" + str(result.data[0].error.errCode))
# print("Error Message:" + str(result.data[0].error.errMessage))
