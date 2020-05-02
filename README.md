# Envio de Notificaciones a Twitter usando Ethos Integration

Esta pequeña aplicación de python ayuda a demostrar cómo una institución puede aprovechar el Marco Ethos y publicar mensajes en tiempo real en una red social, como Twitter. Aunque no es una pieza "oficial" de software de Ellucian, pensé que incluyendo ellucian en el nombre podría acortarlo fácilmente y llamarlo la aplicación principal eet.py

## La Historia destras de la Historia

Imagina por instante que la demanda de los estudiantes por nuevos cursos supera con creces las proyecciones establecidad y es necesario añadir nuevas secciones de cursos. Mientras se notifica a los estudiantes que se encuentran en una la lista de espera, el Director o Coordinador del programa académico le preocupa que no todos los estudiantes interesados puedan estar en la lista de espera que se ha creado y quiere asegurarse de que la mayoria de los estudiantes estén al tanto de las nuevas ofertas de cursos. En este caso, la cuenta de Twitter del programa académico puede ser usada para mostrar esa información.

The Ethos Framework provides a real-time integration scenario that allows for authoritative systems to publish information matching the Ethos Data Model definitions. Taking advantage of this integration paradigm, a small python app that subscribes to newly created course section data can turn around and post a tweet immediately. This application doesn't need to know how to talk to the SIS (in fact, this app has been tested to work exactly the same between both Banner and Colleague), nor does it need to know how to translate the data from whatever back-end system is publishing the information, and instead can use the common, well-defined, Ethos APIs for the integration. 

This app will also consume and tweet about newly created or updated Academic Programs with the idea that as soon as you make that change in your SIS then it will share that information out with your current and prospective students following the school's Twitter account. 

## Setup for Ethos 

This application needs a valid API key for Ethos that is associated with a configuration which is set up to subscribe to 'sections' based on the above described story and it is also designed to work with 'academic-programs'. This API key needs to be included in a config.ini file (you should rename config-template.ini to be config.ini). 

## Setup for Twitter

This application needs several valid values from Twitter, including: a consumer key, a consumer secret, an access token, and an access token secret. These bits of information are provided by Twitter once you have been accepted into their developer program and created a Twitter application within the context of that program. 

## Setup for Computer

This application is written in Python so you will need python installed on the computer from which you plan to run this app. It will need access to the Internet. As described above, you will need certain API keys and such pasted into a config.ini file which has been provided in template form (config-template.ini) with this code repository. The application is meant to be a learning exercise so it is rather chatty and the console log messages could be commented out to relieve that burden should you deem it appropriate. I developed it with Python3 although I'm still new to python and not sure, yet, if there is anything here that would necessarily require a specific version. It is taking advantage of two python libraries: Requests and Tweepy, so you will want to use pip and install those prior to starting the app. 

## Usage

The app is configured to check Ethos every 30 seconds, which can be modified, obviously. Once you start up the app, it will check to see if there are any queued messages for it, without any changes it will print out a message regarding what it found in the queue, and if it finds any messages then it will process through those, print out notes, and finally tweet a message as appropriate. 

For Banner, you can go to the Schedule (SSASECT) page to add a new course section. Once you've saved the new section, Banner will publish that through BEP to Ethos, which will route the message to your application's queue, this application will consume that change, process it, and post the tweet. 

For Colleague, you can go to the SECT page to add a new course section. Again, once you've saved the new section, Colleague will publish that through EDX to Ethos, which will route the message to your application's queue, this application will consume that change, process it, and post the tweet. 

