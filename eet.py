<<<<<<< HEAD
# Escrito en Python 3,9
#
# Esta es la aplicación en Ethos como SUBCRIBING que consumira  
# los datos de los recursos sections & academic-program & enviara un twitte a twiiter
#
import time, pprint, json, configparser

# importar las bibliotecas necesarias de twitter que requiere la instalación de pip3
import tweepy

# importamos una clase Custom
=======
# Written for Python 3
#
# This is the SUBSCRIBING Ethos App that will consume Academic Program data changes
# and post a tweet to twitter
#
import time, pprint, json, configparser

# import the twitter required libraries which requires pip3 install
import tweepy

# import custom class
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
from ethos import Ethos

config = configparser.ConfigParser()
config.read('config.ini')

ethosApiKey = config.get('ETHOS','API_KEY')
twitterConsumerKey = config.get('TWITTER','consumer_key')
twitterConsumerSecret = config.get('TWITTER','consumer_secret')
twitterAccessToken = config.get('TWITTER','access_token')
twitterAccessTokenSecret = config.get('TWITTER','access_token_secret')

def main():
<<<<<<< HEAD
    print('Inicia Aplicación para Envio de Tweets desde Ethos Integration')
=======
    print('Starting Ethos Tweeting System')
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618

    ethos = Ethos(ethosApiKey)

    while True:

<<<<<<< HEAD
        print('Comprobación de las notificaciones de cambio en Ethos Integration')
=======
        print('Checking for change notifications in Ethos Integration')
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
        data = ethos.get_change_notifications()

        if data and len(data) > 0:
            process_change_notifications(data)
        else:
<<<<<<< HEAD
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
=======
            print('No change notifications available')

        # uncomment the wait loop for demo purposes    
        wait_seconds = 5
        print('Waiting for {seconds} seconds...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def process_change_notifications(data):
    print('Received {count} change notifications'.format(count=len(data)))
    print('Here is the entire returned data set:')
    print(data)
    print('Now we will iterate through all of those received messages: ')

    # loop through returned data but only tweet new sections
    for d in data:
        print('Here is a message:')
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
        pprint.pprint(d) # changed data to d because upon startup it will print all messages every time this gets looped through
        
        if d['resource']['name'] == 'academic-programs': 
            tweetNewAcademicProgram(d)

        elif d['resource']['name'] == 'sections': 
<<<<<<< HEAD
            #print ('we figured out this is a course section')
            tweetNewCourseSection(d)

        else:
            print ('Hubo un cambio en algún recurso de modelo de datos publicado a través de Ethos, pero no es uno que apoyemos, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente') 
 
def tweetNewAcademicProgram(d):
    if d['operation'] == 'replaced' or d['operation'] == 'created':    #only tweet new and updated Academic Program info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v15.2.0+json': #only want version 15 of this Ethos Data Model 

            print('Se recibe información nueva o actualizada del programa académico de '+d['content']['title']+' con código '+d['content']['code'])
=======
            tweetNewCourseSection(d)

        else:
            print ('There was a change to some data model resource published through Ethos, but it is not one that we support, so we will ignore it. In the future we may handle this differently') 
 
def tweetNewAcademicProgram(d):
    if d['operation'] == 'replaced' or d['operation'] == 'created':    #only tweet new and updated Academic Program info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v15+json': #only want version 15 of this Ethos Data Model 

            print('Received new or updated academic program info for '+d['content']['title']+' with Code '+d['content']['code'])
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
            #TODO: get term code description somehow

            # Pass the required data pieces to the tweet function
            send_tweet('academicProgram',d['content']['title'])
        else: 
<<<<<<< HEAD
            print('Ethos envió una versión del modelo de datos de programas académicos que este programa no soporta. En el futuro obtendremos la versión correcta.')
    else:
        print('Hubo un cambio en un recurso de modelo de datos de programas académicos publicado a través de Ethos, pero no es para una operación nueva o de actualización/reemplazo, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente.')

def tweetNewCourseSection(d):
    if d['operation'] == 'replaced' or d['operation'] == 'created':   #only tweet new Course Section info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v16.0.0+json': #only want version 15 of this Ethos Data Model 

            print('Recibimos información nueva o actualizada de la sección de cursos para '+d['content']['titles'][0]['value']+' con el código de la sección '+d['content']['code'])
=======
            print('Ethos sent a version of the academic-programs data model this program does not support. In the future we will get the correct version.')
    else:
        print('There was a change to an academic-programs data model resource published through Ethos, but it is not for a new or update/replace operation, so we will ignore it. In the future we may handle this differently.')

def tweetNewCourseSection(d):
    if d['operation'] == 'created':    #only tweet new Course Section info
        if d['resource']['version'] == 'application/vnd.hedtech.integration.v16.0.0+json': #only want version 15 of this Ethos Data Model 

            print('Received new or updated course section info for '+d['content']['titles'][0]['value']+' with Section Code '+d['content']['code'])
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
            #TODO: get term code description somehow

            # Pass the required data pieces to the tweet function
            send_tweet('courseSection',d['content']['titles'][0]['value'])
        else: 
<<<<<<< HEAD
            print('Ethos envió una versión del modelo de datos de programas académicos que este programa no soporta. En el futuro obtendremos la versión correcta.')
    else:
        print('Hubo un cambio en un recurso de modelo de datos de secciones publicado a través de Ethos, pero no es para una operación nueva/creada, así que lo ignoraremos. En el futuro podemos manejar esto de manera diferente.')
=======
            print('Ethos sent a version of the sections data model this program does not support. In the future we will get the correct version.')
    else:
        print('There was a change to a sections data model resource published through Ethos, but it is not for a new/created operation, so we will ignore it. In the future we may handle this differently.')
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618

def send_tweet(eeDmResource,eeDmTitle):
    # print('DEBUG entering send_tweet')
    print('DEBUG twitter consumer key: ' + twitterConsumerKey)
    
    # Set up OAuth and integrate with API
    auth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
    auth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)

    api = tweepy.API(auth)

    if eeDmResource == 'courseSection':
<<<<<<< HEAD
        tweet = "Nos complace informarles que una nueva sección de "+eeDmTitle+" ha sido recientemente añadido para el Segundo Semestre del 2020.  Para detalles adicionales o para registrarse, por favor vaya a  https://www.ellucian.com" 

    elif eeDmResource == 'academicProgram':
        tweet ="Nos complace informarle que hemos creado un nuevo programa "+eeDmTitle+" a partir del Segundo Semestre del 2020.  Si necesita más detalles o está interesado en el programa, por favor contacte con su asesor o puedes ir a https://www.ellucian.com/es."

    else:
        print('Recibimos una solicitud para enviar un tweet por algo que no entendimos. El recurso del Modelo de Datos Ethos identificado como '+eeDmResource+' y el título como '+eeDmTitle+'.')
        tweet = 'Algo no funcionó como se esperaba. Por favor, compruebe los registros.'
=======
        tweet = "We are pleased to inform you that a new section of "+eeDmTitle+" has recently been added for the **Fall 2018**.  For additional details or to register, please go to https://www.ellucian.com" 

    elif eeDmResource == 'academicProgram':
        tweet ="We are pleased to offer you a new program in "+eeDmTitle+" beginning in the **Fall 2019**.  If you need additional details or are interested in the program, please contact your advisor."

    else:
        print('We received a request to send a tweet for something we did not understand. The Ethos Data Model resource identified as '+eeDmResource+' and the title as '+eeDmTitle+'.')
        tweet = 'Something did not work as expected. Please check the logs.'
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618
        # In a production environment we may not want to actually post this tweet to the world wide webs on the internets for the kids to see
    
    # send the tweet
    api.update_status(status=tweet)
   
<<<<<<< HEAD
    print('DEBUG salir de la función send_tweet después de la publicación ' + tweet)
=======
    print('DEBUG exiting send_tweet function after posting ' + tweet)
>>>>>>> 6e1bec3f5b44f31aa71d8fead86542cef503b618


if __name__ == '__main__':
    main()
