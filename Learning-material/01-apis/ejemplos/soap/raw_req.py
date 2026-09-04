import requests
envelope = """<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:tns="http://ejemplo.com/cotiz">
  <soap:Body>
    <tns:GetCotizacion>
      <moneda>USD</moneda>
    </tns:GetCotizacion>
  </soap:Body>
</soap:Envelope>"""
r = requests.post("http://127.0.0.1:8007/cotiz",
                  data=envelope,
                  headers={"Content-Type": "text/xml; charset=utf-8", "SOAPAction": "GetCotizacion"})
print("HTTP", r.status_code)
print(r.text.strip())
