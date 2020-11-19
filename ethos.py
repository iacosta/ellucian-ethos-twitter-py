# Escrito en Python 3.8
#
# pip install  "requests" es requerido
# 
#
import requests

class Ethos:
    auth_url = "https://integrate.elluciancloud.com"
    ethos_integration_url = "https://integrate.elluciancloud.com"

    # Inicializa variables
    api_key = ''
    jwt = ''

    def __init__(self,api_key):
        self.api_key = api_key

    def get_jwt(self):
        if self.api_key:
            print('La clave de Ethos API Key utilizado es  get_jwt is: {}'.format(self.api_key))
            headers = { 'Authorization': "Bearer " + self.api_key}
            ### TODO: add try/except block here
            response = requests.request("POST", self.auth_url + "/auth", headers=headers)

            if response.status_code == 200:
                self.jwt = response.text
                print(self.jwt)
            elif response.status_code == 406:
                raise Exception('El API Key es invalido',response.status_code,response.text)
            else:
                raise Exception('Error al llamar el Endpoint de Ethos Integration',response.status_code,response.text)
        else:
            raise Exception('API Key aún no definido')

    def get_change_notifications(self,retry=True):
        if not self.jwt:
            self.get_jwt()

        headers = {
            'Authorization': "Bearer " + self.jwt,
            'Accept': 'application/vnd.hedtech.change-notifications.v2+json'}
        ### TODO: add try/except block here
        response = requests.request("GET", self.ethos_integration_url + "/consume", headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401 and retry:
            print('JWT has expired')
            self.get_jwt()
            return self.get_change_notifications(retry=False)
        else:
            raise Exception('Error al llamar el Endpoint de Ethos Integration',response.status_code,response.text)
