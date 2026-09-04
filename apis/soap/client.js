const soap = require("soap");
soap.createClient("http://127.0.0.1:8007/cotiz?wsdl", (err, client) => {
  if (err) return console.error(err.message);
  client.GetCotizacion({ moneda: "USD" }, (err, result, rawResponse) => {
    if (err) return console.error(err.message);
    console.log("valor devuelto:", result.valor);
    console.log("--- envelope XML que volvio del server ---");
    console.log(rawResponse.trim());
  });
});
