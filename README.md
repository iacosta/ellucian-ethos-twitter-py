<<<<<<< HEAD
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Licencia][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.ellucian.com/es">
    <img src="images/logo-ethos-connected" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">Notificaciones a Twitter usando Ethos Integration</h1>
</p>

## Contenido

* [Introducción](#Introducción)
  * [Demostración](#Demostración)
* [Necesidades](#Necesidades)
  * [Arquitectura](#Arquitectura)
* [Licencia](#Licencia)
* [Contacto](#Contacto)
* [Agradecimientos](#Agradecimientos)

___
# Introducción
Esta es una pequeña aplicación de desarrollada en Python cuyo objetivo es evidenciar las capacidades que tiene Ethos Integration y cómo una institución puede aprovechar este componente para publicar mensajes en tiempo real en una red social, en esta caso como Twitter. Vale la pena aclarar que no es un desarrollo de software "Oficial" de Ellucian, creemos que este código puede servir como guia inicial para las áreas de TI puedan desarrollar sus propias aplicaciones y tomen ventaja de las bondades de Ethos Platform.


### **Demostración**

A continuación un video corto del funcionamiento de la aplicación. Dentro del video se encuentra la explicación paso a paso sobre el funcionamiento de la aplicación desarrollada. 

**-->Puedes hacer click en la imagen<--**

<p align="center">
<a style="float:center" href="https://youtu.be/4avxPnPJ8V4" target="_blank">
  <img alt="PicSciP Demo Video" src="https://img.youtube.com/vi/4avxPnPJ8V4/maxresdefault.jpg" width="780" height="450" />
</a>

<!--[![Watch the video](https://img.youtube.com/vi/4GcFubPBCq0/maxresdefault.jpg)](https://youtu.be/4GcFubPBCq0) -->

___
## Necesidades

Imaginemos por un momento el siguiente escenario. Los estudiantes demanda nuevos cursos, la institución observa que la proyección de cursos que han realizado no han sido suficiente y es necesario añadir nuevas secciones de cursos. Dada la situación es necesario notificar a los estudiantes que se encuentran en una la lista de espera (Banner), el coordinador del programa académico le preocupa que no todos los estudiantes interesados puedan estar en la lista de espera que se ha definido previamente y quiere asegurarse de que la mayoría de los estudiantes estén al tanto de las nuevas ofertas de cursos. En este caso, la cuenta de Twitter del programa académico puede ser usada para mostrar esa información.

Es aquí donde Ethos Platform proporciona capacidades de integración en tiempo real que permite que los sistemas y/o aplicaciones autorizadas publiquen información que coincida con las definiciones del Modelo de Datos Ethos.

Aprovechando esta capa de integración, esta pequeña aplicación desarrollada en Python se suscribe a los datos del recurso de Secciones de Cursos (SECTIONS) y/o Programas Académicos (ACADEMIC-PROGRAMS) según se el caso toma los datos y publicar un tweet inmediatamente, todo esto es posible dado a que se puede utilizar las APIs definidas de Ethos para la integración. 

### **Arquitectura**

En la siguiente imagen se puede observar en detalle los diferentes elementos que hacen parte de la aplicación.

❮img src="images/Arquitectura.png" width="100" ❯
___
## Licencia
Distribuido bajo licencia BSD 2-Clause. Ver `LICENSE` para más información.
___
## Contacto
Iván Acosta - [@iacostac](https://twitter.com/iacostac) - ivan@acostacontreras.com

Link del Proyecto: [https://github.com/iacosta/ellucian-ethos-twitter-py](https://github.com/iacosta/ellucian-ethos-twitter-py)
___
## Agradecimientos
Thank you both for sharing your time, patience and knowledge. 
* [Chris Fontenot](https://github.com/cfont)
* [Primo Lazar](https://www.linkedin.com/in/primo-lazar/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/iacosta/ellucian-ethos-twitter-py/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/iacosta/ellucian-ethos-twitter-py/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/iacosta/ellucian-ethos-twitter-py/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/iacosta/ellucian-ethos-twitter-py/issues
[license-shield]: https://img.shields.io/github/license/iacosta/ellucian-ethos-twitter-py
[license-url]: https://github.com/iacosta/ellucian-ethos-twitter-py/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/iacostac/
=======
# Envio de Notificaciones a Twitter usando Ethos Integration

Esta pequeña aplicación de python ayuda a demostrar cómo una institución puede aprovechar el Marco Ethos y publicar mensajes en tiempo real en una red social, como Twitter. Aunque no es una pieza "oficial" de software de Ellucian, pensé que incluyendo ellucian en el nombre podría acortarlo fácilmente y llamarlo la aplicación principal eet.py

<p align="center">
<a style="float:center" href="https://youtu.be/4avxPnPJ8V4" target="_blank">
  <img alt="PicSciP Demo Video" src="https://img.youtube.com/vi/4avxPnPJ8V4/maxresdefault.jpg" width="780" height="450" />
</a>


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

>>>>>>> e4772092248634442abc98509d36187e2561037d
