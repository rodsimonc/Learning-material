import grpc, time
from concurrent import futures
import usuarios_pb2, usuarios_pb2_grpc

class UsuariosServicer(usuarios_pb2_grpc.UsuariosServicer):
    def GetUsuario(self, request, context):
        return usuarios_pb2.Usuario(id=request.id, nombre="Carlos", email="carlos@ejemplo.com")

def serve():
    s = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    usuarios_pb2_grpc.add_UsuariosServicer_to_server(UsuariosServicer(), s)
    s.add_insecure_port("[::]:9001")
    s.start()
    s.wait_for_termination()

if __name__ == "__main__":
    serve()
