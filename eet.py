# Written for Python 3,8
#
# Esta es la aplicación en Ethos como SUBCRIBING que consumira 
# los datos de los recurcos sections & academic-program & enviara un twitte a twiiter
#
import time, pprint, json, configparser

# importar las bibliotecas necesarias de twitter que requiere la instalación de pip3
import tweepy

# importamos una clase Custom
from ethos import Ethos

config = configparser.ConfigParser()
config.read('config.ini')

ethosApiKey = config.get('ETHOS','API_KEY')
twitterConsumerKey = config.get('TWITTER','consumer_key')
twitterConsumerSecret = config.get('TWITTER','consumer_secret')
twitterAccessToken = config.get('TWITTER','access_token')
twitterAccessTokenSecret = config.get('TWITTER','access_token_secret')

def main():
    print('Inicia Aplicación para Envio de Tweets desde Ethos Integration')

    ethos = Ethos(ethosApiKey)

    while True:

        print('Comprobación de las notificaciones de cambio en Ethos Integration')
        data = ethos.get_change_notifications()

        if data and len(data) > 0:
            process_change_notifications(data)
        else:
            print('No hay notificaciones de cambio disponibles')

        # uncomment the wait loop for demo purposes    
        wait_seconds = 5
        print('Esperar {seconds} segundos...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def process_change_notifications(data):
    print('Recibiendo {count} notificaciones'.format(count=len(data)))
    print('Aquí está todo el conjunto de datos devueltos:')
    print(data)
    print('Ahora revisemos todos esos mensajes recibidos: ')

    # loop through returned data but only tweet new sections
    for d in data:
        print('Aquí hay un mensaje:')
        pprint.pprint(d) # changed data to d because upon startup it will print all messages every time this gets looped through
        
        if d['resource']['name'] == 'academic-programs': 
            tweetNewAcademicProgram(d)

        elif d['resource']['name'] == 'sections': 
            #print ('we figured out this is a course section')
            tweetNewCourseSection(d)

        else:
            print ('Hubo un cambio en algún recurso de modelo de datos publicado a través de Ethos, pero no es uno que apoyemos, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente') 
 
def tweetNewAcademicProgram(d):
    if d['operation'] == 'replaced' or d['operation'] == 'created':    #only tweet new and updated Academic Program info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v15.2.0+json': #only want version 15 of this Ethos Data Model 

            print('Se recibe información nueva o actualizada del programa académico de '+d['content']['title']+' con código '+d['content']['code'])
            #TODO: get term code description somehow

            # Pass the required data pieces to the tweet function
            send_tweet('academicProgram',d['content']['title'])
        else: 
            print('Ethos envió una versión del modelo de datos de programas académicos que este programa no soporta. En el futuro obtendremos la versión correcta.')
    else:
        print('Hubo un cambio en un recurso de modelo de datos de programas académicos publicado a través de Ethos, pero no es para una operación nueva o de actualización/reemplazo, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente.')

def tweetNewCourseSection(d):
    if d['operation'] == 'replaced' or d['operation'] == 'created':   #only tweet new Course Section info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v16.0.0+json': #only want version 15 of this Ethos Data Model 

            print('Recibimos información nueva o actualizada de la sección de cursos para '+d['content']['titles'][0]['value']+' con el código de la sección '+d['content']['code'])
            #TODO: get term code description somehow

            # Pass the required data pieces to the tweet function
            send_tweet('courseSection',d['content']['titles'][0]['value'])
        else: 
            print('Ethos envió una versión del modelo de datos de programas académicos que este programa no soporta. En el futuro obtendremos la versión correcta.')
    else:
        print('Hubo un cambio en un recurso de modelo de datos de secciones publicado a través de Ethos, pero no es para una operación nueva/creada, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente.')

def send_tweet(eeDmResource,eeDmTitle):
    # print('DEBUG entering send_tweet')
    print('DEBUG twitter consumer key: ' + twitterConsumerKey)
    
    # Set up OAuth and integrate with API
    auth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
    auth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)

    api = tweepy.API(auth)

    if eeDmResource == 'courseSection':
        tweet = "Nos complace informarles que una nueva sección de "+eeDmTitle+" ha sido recientemente añadido para el Segundo Semestre del 2020.  Para detalles adicionales o para registrarse, por favor vaya a  https://www.ellucian.com" 

    elif eeDmResource == 'academicProgram':
        tweet ="Nos complace informarle que hemos creado un nuevo programa "+eeDmTitle+" a partir del Segundo Semestre del 2020.  Si necesita más detalles o está interesado en el programa, por favor contacte con su asesor o puedes ir a https://www.ellucian.com/es."

    else:
        print('Recibimos una solicitud para enviar un tweet por algo que no entendimos. El recurso del Modelo de Datos Ethos identificado como '+eeDmResource+' y el título como '+eeDmTitle+'.')
        tweet = 'Algo no funcionó como se esperaba. Por favor, compruebe los registros.'
        # In a production environment we may not want to actually post this tweet to the world wide webs on the internets for the kids to see
    
    # send the tweet
    api.update_status(status=tweet)
   
    print('DEBUG salir de la función send_tweet después de la publicación ' + tweet)


if __name__ == '__main__':
    main()

