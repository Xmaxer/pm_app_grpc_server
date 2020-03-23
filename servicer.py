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
                print("Remaining: " + str(len(self.data[request.id])))
                yield pm_app_pb2.DataPoint(id=request.id, data=res["data"], settings=res["settings"])

    def SendData(self, request_iterator, context):
        influx = InfluxDBClient('localhost', 8086, 'kevin', 'root', 'data')
        for request in request_iterator:
            print(request)
            data = list(request.data)
            field_values = {k: v for k, v in enumerate(data)}
            tags = {"asset_id": request.id}
            measurement = "asset_" + str(request.id)
            body = [
                {
                    "measurement": measurement,
                    "tags": tags,
                    "fields": field_values
                }
            ]
            influx.write_points(body)
            self.data.setdefault(request.id, [])
            self.data[request.id].append({"data": request.data, "settings": request.settings})
        return pm_app_pb2.Empty()

    def SaveData(self, request, context):
        influx = InfluxDBClient('localhost', 8086, 'kevin', 'root', 'results')
        data = list(request.data)
        field_values = {k: v for k, v in enumerate(data)}
        tags = {"asset_id": request.id}
        measurement = "asset_" + str(request.id)
        body = [
            {
                "measurement": measurement,
                "tags": tags,
                "fields": field_values
            }
        ]
        influx.write_points(body)
        return pm_app_pb2.Empty()
