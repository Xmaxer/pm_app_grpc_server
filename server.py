from concurrent import futures
import pm_app_pb2_grpc
from servicer import PmAppServicer
import grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pm_app_pb2_grpc.add_PMAppServicer_to_server(PmAppServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
