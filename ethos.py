# Escrito en Python 3.9
#
# Pre-requisito instalar 
# pip install "requests" 
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
            print('La Ethos API Key usada en get_jwt es: {}'.format(self.api_key))
            headers = { 'Authorization': "Bearer " + self.api_key}
            ### TODO: add try/except block here
            response = requests.request("POST", self.auth_url + "/auth", headers=headers)

            if response.status_code == 200:
                self.jwt = response.text
                print(self.jwt)
            elif response.status_code == 406:
                raise Exception('La API Key es valida',response.status_code,response.text)
            else:
                raise Exception('Error en el EndPoint de Ethos Integration',response.status_code,response.text)
        else:
            raise Exception('La API Key no ha sido definida')

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
            print('JWT ha expirado')
            self.get_jwt()
            return self.get_change_notifications(retry=False)
        else:
            raise Exception('Error en el EndPoint de Ethos Integration',response.status_code,response.text)