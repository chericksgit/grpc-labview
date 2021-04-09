import grpc
import measurement_service_pb2 as ms
import measurement_service_pb2_grpc as msgrpc

serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)
result = measurementServer.PerformOCVMeasurement(ms.OCVRequest())
print("Voltage 1:" + str(result.data[0].battery1voltage))
print("Voltage 2:" + str(result.data[0].battery2voltage))
print("Voltage 3:" + str(result.data[0].battery3voltage))

print("Error Code:" + str(result.data[0].error.errCode))
print("Error Message:" + str(result.data[0].error.errMessage))
