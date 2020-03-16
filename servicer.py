import pm_app_pb2
import pm_app_pb2_grpc
from influxdb import InfluxDBClient
import json


class PmAppServicer(pm_app_pb2_grpc.PMAppServicer):

    def __init__(self):
        self.data = {}

    def GetData(self, request, context):
        print("Made request")
        while True:
            while request.id in self.data and len(self.data[request.id]) > 0:
                res = self.data[request.id].pop(0)
                print("Popping: ")
                print(res)
                print("Remaining: " + str(len(self.data[request.id])))
                yield pm_app_pb2.DataPoint(id=request.id, data=res)

    def SendData(self, request, context):
        # influx = InfluxDBClient('localhost', 8086, 'kevin', 'root', 'data')
        # data = json.loads(request.data)
        # field_values = {k: v for k, v in enumerate(data)}
        # tags = {"asset_id": request.asset_id}
        # measurement = "asset_" + str(request.asset_id)
        # body = [
        #     {
        #         "measurement": measurement,
        #         "tags": tags,
        #         "fields": field_values
        #     }
        # ]
        # influx.write_points(body)
        print("Request: ")
        print(request)
        self.data.setdefault(request.id, [])
        self.data[request.id].append(request.data)
        return pm_app_pb2.Empty()
