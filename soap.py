import requests

# define a function to send a SOAP request
def soap_post(url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso", body = 'body.xml', headers = { 'Content-Type': 'text/xml; charset=utf-8'}, params = None):
    data = open(body).read()
    response = requests.post(url, data=data, headers=headers, params=params)
    return response.content

obj = soap_post()
print(obj)

with open('response.xml', 'wb') as f:
    f.write(obj)