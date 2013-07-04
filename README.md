# ThingsExporter #

This project is a work in progress for exporting ToDos from the Things.app (http://culturedcode.com/things/)
to an xml representation of those todos.
So I can add them to my website periodically and make my things available through the web

This projec will incorporate a bundle of different tools, languages and techniques:
* Python for communication with the Things.app
* Applescript (maybe)
* Java EE 6/7 for exposing Things to the web
* IoC principles
* Code generation (jaxb)
* etc


# Prerequisites for making this script work #
For the python tools we need:

* Python 2.7.x
* the PyObjc package (see install command below)
* Things.app
* A Mac where it all runs on :-)


    sudo pip install pyobjc


For the java applications you may need:

* Java 1.7
* Glassfish 4
* Maven 3.x


# User Stories #

Python Things.app exporter / importer tool:

* (done) As a developer I WANT TO write a Things.app AppleScript API wrapper in Python IN ORDER TO read from todos from Things.app
* (done) As a user I WANT TO be able to export Things.app lists to Xml IN ORDER TO have a usable backup
* (done) As a user I WANT TO be able to import specific Xml to Things.app IN ORDER TO update Things based on external data
* (done) As a user I WANT TO have a contract defined on the Xml IN ORDER TO be use this contract elsewhere (webservice)
* (open) As a developer I WANT TO enhance the Things.app AppleScript API wrapper in Python IN ORDER TO write to Things.app


Java webapplication based on Things exported XML:

* (in progress) As a developer I WANT TO be able generate java code based on the schema IN ORDER TO be able to use it a webapplication
* (open) As a user I WANT TO see the exported **Today** IN ORDER TO view my today todo's anywhere (even on non macs)
* (open) As a user I WANT TO be able to change the status todo's IN ORDER TO be able to provide input for syncing Things.app
* (open) As a user I WANT TO be see the other **Lists** IN ORDER TO view the todos anywhere
* (open) As a user I WANT TO have the same look and feel as Things IN ORDER TO get what I'm used to.
* (open) As a developer I WANT TO be able write to a Xml IN ORDER TO provide data to sync to Things.app


# Copyright #

Copyright (c) 2013 by Ivo Wolring (http://ivonet.nl)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.