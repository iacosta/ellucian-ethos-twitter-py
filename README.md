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