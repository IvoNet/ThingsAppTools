__doc__ = """Python module for converting Things classes to XML."""
__author__ = "Ivo Woltring"
__copyright__ = "Copyright (c) 2013 Ivo Woltring"
__license__ = """
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import Null
import xmlwitch
from Things import ThingsToDos, ThingsArea, ThingsTags, ThingsProject, ThingsApp


def Xml():
    """
        Initializes a xmlwitch Builder instance.
    :rtype : xmlwitch.Builder
    :return: xmlwitch.Builder
    """
    return xmlwitch.Builder(version='1.0', encoding='utf-8', indent=' ' * 4)


# def printTagIds(thingsTags, xml=Xml()):
#     if not isinstance(thingsTags, ThingsTags):
#         raise TypeError("Input parameter should be a ThingsTags but is a " + str(type(thingsTags)))
#     if len(thingsTags) <= 0:
#         return xml
#     with xml.tags():
#         for tag in thingsTags:
#             print "Processing tag :", tag.id()
#             xml.id(tag.id())
#     return xml


def __printTags(thingsTags, xml=Xml()):
    if not isinstance(thingsTags, ThingsTags):
        raise TypeError("Input parameter should be a ThingsTags but is a " + str(type(thingsTags)))
    if len(thingsTags) <= 0:
        return xml
    with xml.tags():
        for tag in thingsTags:
            print "Processing tag :", tag.name()
            with xml.tag():
                xml.id(tag.id())
                xml.name(tag.name())
    return xml


def __printArea(thingsArea, xml=Xml()):
    if thingsArea is Null:
        return xml
    if not isinstance(thingsArea, ThingsArea):
        raise TypeError("Input parameter should be a ThingsArea but is a " + str(type(thingsArea)))
    with xml.area():
        xml.id(thingsArea.id())
        xml.name(thingsArea.name())
        xml.suspended(str(thingsArea.suspended()))
    return xml


def __printProject(thingsProject, xml=Xml()):
    if thingsProject is Null:
        return xml
    if not isinstance(thingsProject, ThingsProject):
        raise TypeError("Input parameter should be a ThingsProject but is a " + str(type(thingsProject)))
    with xml.project():
        xml.id(thingsProject.id())
        xml.name(thingsProject.name())
        xml.active(str(thingsProject.is_active()))
    return xml


def __printToDos(thingsToDos, xml=Xml()):
    """
    Print a ThingsToDos item as Xml.

    :param thingsToDos: the ToDos to convert to Xml
    :param xml: the xml Builder to manipulate
    :return: the xml
    :raise: TypeError if the wrong type is fed to this method
    """
    if not isinstance(thingsToDos, ThingsToDos):
        raise TypeError("Input parameter should be a ThingsToDos")
    with xml.todos():
        for todo in thingsToDos:
            print "Processing todo:", todo.name()
            with xml.todo():
                xml.id(todo.id())
                xml.name(todo.name())
                todo_notes = todo.notes()
                if len(todo_notes) > 0:
                    xml.notes(todo_notes)
                xml.creationDate(str(todo.creationDate()))
                __printArea(todo.area(), xml)
                __printProject(todo.project(), xml)
                __printTags(todo.tags(), xml)
                if todo.is_open():
                    xml.status("OPEN")
                elif todo.is_closed():
                    xml.status("CLOSED")
                else:
                    xml.status("CANCELLED")
                if not todo.activationDate() is Null:
                    xml.activationDate(str(todo.activationDate()))
                if not todo.completionDate() is Null:
                    xml.completionDate(str(todo.completionDate()))
                if not todo.dueDate() is Null:
                    xml.dueDate(str(todo.dueDate()))
                if not todo.cancellationDate() is Null:
                    xml.cancellationDate(str(todo.cancellationDate()))
    return xml


# this one will print just about anything and I see no reason for it
# def printLists(thingsLists, xml=Xml()):
#     if not isinstance(thingsLists, ThingsLists):
#         raise TypeError("Input parameter should be a ThingsToDos")
#     with xml.lists():
#         for thingsList in thingsLists:
#             print "Processing list:", thingsList.name()
#             xml.id(thingsList.id())
#             xml.title(thingsList.name())
#             printToDos(thingsList.toDos(), xml)


def __printToday(thingsToDos, xml=Xml()):
    with xml.today():
        __printToDos(thingsToDos, xml)
    return xml


def __printInbox(thingsToDos, xml=Xml()):
    with xml.inbox():
        __printToDos(thingsToDos, xml)
    return xml


def __printNext(thingsToDos, xml=Xml()):
    with xml.next():
        __printToDos(thingsToDos, xml)
    return xml


def __printScheduled(thingsToDos, xml=Xml()):
    with xml.scheduled():
        __printToDos(thingsToDos, xml)
    return xml


def __printSomeday(thingsToDos, xml=Xml()):
    with xml.someday():
        __printToDos(thingsToDos, xml)
    return xml


def __printProjects(thingsProjects, xml=Xml()):
    with xml.projects():
        for project in thingsProjects:
            with xml.project(title=project.name()):
                xml.id(project.id())
                xml.name(project.name())
                if len(project.notes()) > 0:
                    xml.notes(project.notes())
                if project.is_active():
                    xml.status("OPEN")
                else:
                    xml.status("CLOSED")
                __printTags(project.tags(), xml)
                __printToDos(project.toDos(), xml)
    return xml


def __printAreas(thingsAreas, xml=Xml()):
    with xml.areas():
        for area in thingsAreas:
            print "Processing area:", area.name()
            if area.suspended():
                continue
            with xml.area(title=area.name()):
                xml.id(area.id())
                xml.name(area.name())
                __printToDos(area.toDos(), xml)
    return xml


def activeListsToXml():
    """Generates an XML representation of all active lists in Things"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printToday(Things["Today"], xml)
        __printInbox(Things["Inbox"], xml)
        __printNext(Things["Next"], xml)
        __printScheduled(Things["Scheduled"], xml)
        __printSomeday(Things["Someday"], xml)
        __printProjects(Things.projects(), xml)
        __printAreas(Things.areas(), xml)
        __printTags(Things.tags(), xml)
    return str(xml)


def tagsToXml():
    """Generates an XML representation of the Things "Tags"."""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printTags(Things.tags(), xml)
    return str(xml)


def inboxToXml():
    """Generates an XML representation of the Things "Inbox" list"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printInbox(Things["Inbox"], xml)
    return str(xml)


def todayToXml():
    """Generates an XML representation of the Things "Today" list"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printToday(Things["Today"], xml)
    return str(xml)


if __name__ == "__main__":
    print todayToXml()