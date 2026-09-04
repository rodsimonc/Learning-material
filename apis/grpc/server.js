const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const def = protoLoader.loadSync("usuarios.proto");
const proto = grpc.loadPackageDefinition(def).usuarios;

function getUsuario(call, callback) {
  callback(null, { id: call.request.id, nombre: "Carlos", email: "carlos@ejemplo.com" });
}

const server = new grpc.Server();
server.addService(proto.Usuarios.service, { GetUsuario: getUsuario });
server.bindAsync("0.0.0.0:9002", grpc.ServerCredentials.createInsecure(), () => {
  console.log("gRPC en :9002");
});
