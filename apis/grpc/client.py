import grpc, usuarios_pb2, usuarios_pb2_grpc

with grpc.insecure_channel("127.0.0.1:9001") as canal:
    stub = usuarios_pb2_grpc.UsuariosStub(canal)
    resp = stub.GetUsuario(usuarios_pb2.UsuarioReq(id=42))   # llamada como si fuera funcion local
    print("id:", resp.id)
    print("nombre:", resp.nombre)
    print("email:", resp.email)
