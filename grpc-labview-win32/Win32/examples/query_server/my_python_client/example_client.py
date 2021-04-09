import grpc
import measurement_service_pb2 as ms
import measurement_service_pb2_grpc as msgrpc

serverAddress = "localhost:50051"
channel = grpc.insecure_channel(serverAddress)
measurementServer = msgrpc.MeasurementServiceStub(channel)

# Get the server uptime
uptime = measurementServer.Query(ms.QueryRequest(query = "Uptime"))
print("Server Uptime: " + uptime.message)

# Perform OCV
ocv_result = measurementServer.PerformOCVMeasurement(ms.OCVRequest())
print("Voltage 1:" + str(ocv_result.data[0].battery1voltage))
print("Voltage 2:" + str(ocv_result.data[0].battery2voltage))
print("Voltage 3:" + str(ocv_result.data[0].battery3voltage))
print("Error Code:" + str(ocv_result.data[0].error.errCode))
print("Error Message:" + str(ocv_result.data[0].error.errMessage))

# Perform ACIR
acir_result = measurementServer.PerformACIRMeasurement(ms.ACIRRequest())
print("Impedance:" + str(acir_result.data[0].Impedance))
print("Real:" + str(acir_result.data[0].Real))
print("Imaginery:" + str(acir_result.data[0].Imaginery))
print("Error Code:" + str(acir_result.data[0].error.errCode))
print("Error Message:" + str(acir_result.data[0].error.errMessage))
