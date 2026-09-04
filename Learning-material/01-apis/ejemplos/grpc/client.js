const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const proto = grpc.loadPackageDefinition(protoLoader.loadSync("usuarios.proto")).usuarios;

const client = new proto.Usuarios("127.0.0.1:9002", grpc.credentials.createInsecure());
client.GetUsuario({ id: 42 }, (err, resp) => {
  if (err) return console.error(err);
  console.log("id:", resp.id);
  console.log("nombre:", resp.nombre);
  console.log("email:", resp.email);
});
