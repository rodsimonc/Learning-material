from zeep import Client

# zeep lee el WSDL y arma el cliente solo
client = Client("http://127.0.0.1:8007/cotiz?wsdl")
valor = client.service.GetCotizacion(moneda="USD")
print("valor devuelto:", valor)
