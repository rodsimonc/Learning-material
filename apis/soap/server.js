const http = require("http");
const soap = require("soap");
const fs = require("fs");
const wsdl = fs.readFileSync("cotizaciones.wsdl", "utf8");

const service = {
  CotizacionesService: {
    CotizacionesPort: {
      GetCotizacion: (args) => {
        const tabla = { USD: 1350.5, EUR: 1465.2 };
        return { valor: tabla[args.moneda] ?? 0 };
      },
    },
  },
};

const server = http.createServer((req, res) => { res.end("404"); });
server.listen(8007, () => {
  soap.listen(server, "/cotiz", service, wsdl);
  console.log("SOAP en http://127.0.0.1:8007/cotiz?wsdl");
});
