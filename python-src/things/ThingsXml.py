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

STATUS_CLOSED = "CLOSED"
STATUS_OPEN = "OPEN"


def Xml():
    """
        Initializes a xmlwitch Builder instance.
    :rtype : xmlwitch.Builder
    :return: xmlwitch.Builder
    """
    return xmlwitch.Builder(version='1.0', encoding='utf-8', indent=' ' * 4)


def __printTagsIds(thingsTags, xml=Xml()):
    if not isinstance(thingsTags, ThingsTags):
        raise TypeError("Input parameter should be a ThingsTags but is a " + str(type(thingsTags)))
    if len(thingsTags) <= 0:
        return xml
    with xml.tagIds():
        for tag in thingsTags:
            print "Processing tag :", tag.name()
            xml.id(tag.id())
    return xml


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


def __printAreaId(thingsArea, xml=Xml()):
    if thingsArea is Null:
        return xml
    if not isinstance(thingsArea, ThingsArea):
        raise TypeError("Input parameter should be a ThingsArea but is a " + str(type(thingsArea)))
    xml.areaId(thingsArea.id())
    return xml


def __printProjectId(thingsProject, xml=Xml()):
    if thingsProject is Null:
        return xml
    if not isinstance(thingsProject, ThingsProject):
        raise TypeError("Input parameter should be a ThingsProject but is a " + str(type(thingsProject)))
    xml.projectId(thingsProject.id())
    return xml


def __printProject(thingsProject, openOnly=True, xml=Xml()):
    if thingsProject is Null:
        return xml
    if not isinstance(thingsProject, ThingsProject):
        raise TypeError("Input parameter should be a ThingsProject but is a " + str(type(thingsProject)))
    with xml.project(title=thingsProject.name()):
        xml.id(thingsProject.id())
        xml.name(thingsProject.name())
        if len(thingsProject.notes()) > 0:
            xml.notes(thingsProject.notes())
        if thingsProject.is_active():
            xml.status(STATUS_OPEN)
        else:
            xml.status(STATUS_CLOSED)
        __printTags(thingsProject.tags(), xml)
        __printToDos(thingsProject.toDos(), openOnly, xml)

    return xml


def __printTodo(thingsToDo, xml=Xml()):
    xml.id(thingsToDo.id())
    xml.name(thingsToDo.name())
    todo_notes = thingsToDo.notes()
    if len(todo_notes) > 0:
        xml.notes(todo_notes)
    xml.creationDate(str(thingsToDo.creationDate()))
    __printAreaId(thingsToDo.area(), xml)
    __printProjectId(thingsToDo.project(), xml)
    __printTagsIds(thingsToDo.tags(), xml)
    if thingsToDo.is_open():
        xml.status("OPEN")
    elif thingsToDo.is_closed():
        xml.status("CLOSED")
    else:
        xml.status("CANCELLED")
    if not thingsToDo.activationDate() is Null:
        xml.activationDate(str(thingsToDo.activationDate()))
    if not thingsToDo.completionDate() is Null:
        xml.completionDate(str(thingsToDo.completionDate()))
    if not thingsToDo.dueDate() is Null:
        xml.dueDate(str(thingsToDo.dueDate()))
    if not thingsToDo.cancellationDate() is Null:
        xml.cancellationDate(str(thingsToDo.cancellationDate()))
    return xml


def __printToDos(thingsToDos, openOnly=True, xml=Xml()):
    """
    Print a ThingsToDos item as Xml.

    :param thingsToDos: the ToDos to convert to Xml
    :param xml: the xml Builder to manipulate
    :return: the xml
    :raise: TypeError if the wrong type is fed to this method
    """
    if not isinstance(thingsToDos, ThingsToDos):
        raise TypeError("Input parameter should be a ThingsToDos")
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.todos():
        for todo in thingsToDos:
            print "Processing todo:", todo.name()
            if openOnly:
                if not todo.is_open():
                    continue
            with xml.todo():
                __printTodo(todo, xml)
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


def __printToday(thingsToDos, openOnly=True, xml=Xml()):
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.today():
        __printToDos(thingsToDos, openOnly, xml)
    return xml


def __printInbox(thingsToDos, openOnly=True, xml=Xml()):
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.inbox():
        __printToDos(thingsToDos, openOnly, xml)
    return xml


def __printNext(thingsToDos, openOnly=True, xml=Xml()):
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.next():
        __printToDos(thingsToDos, openOnly, xml)
    return xml


def __printScheduled(thingsToDos, openOnly=True, xml=Xml()):
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.scheduled():
        __printToDos(thingsToDos, openOnly, xml)
    return xml


def __printSomeday(thingsToDos, openOnly=True, xml=Xml()):
    if openOnly and not thingsToDos.hasOpen():
        return xml
    with xml.someday():
        __printToDos(thingsToDos, openOnly, xml)
    return xml


def __printProjects(thingsProjects, openOnly=True, xml=Xml()):
    if openOnly and not thingsProjects.has_active():
        return xml
    with xml.projects():
        for project in thingsProjects:
            __printProject(project, openOnly, xml)
    return xml


def __printAreas(thingsAreas, openOnly=True, xml=Xml()):
    if openOnly and not thingsAreas.has_active():
        return xml
    with xml.areas():
        for area in thingsAreas:
            print "Processing area:", area.name()
            if area.suspended():
                continue
            with xml.area(title=area.name()):
                xml.id(area.id())
                xml.name(area.name())
                __printToDos(area.toDos(), openOnly, xml)
    return xml


def activeListsToXml(statusOpenOnly=True):
    """Generates an XML representation of all active lists in Things"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printInbox(Things["Inbox"], statusOpenOnly, xml)
        __printToday(Things["Today"], statusOpenOnly, xml)
        __printNext(Things["Next"], statusOpenOnly, xml)
        __printScheduled(Things["Scheduled"], statusOpenOnly, xml)
        __printSomeday(Things["Someday"], statusOpenOnly, xml)
        __printProjects(Things.projects(), statusOpenOnly, xml)
        __printAreas(Things.areas(), statusOpenOnly, xml)
        __printTags(Things.tags(), xml)
    return str(xml)


def tagsToXml():
    """Generates an XML representation of the Things "Tags"."""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printTags(Things.tags(), xml)
    return str(xml)


def inboxToXml(statusOpenOnly=True):
    """Generates an XML representation of the Things "Inbox" list"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printInbox(Things["Inbox"], statusOpenOnly, xml)
    return str(xml)


def todayToXml(statusOpenOnly=True):
    """Generates an XML representation of the Things "Today" list"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://things.ivonet.nl'):
        __printToday(Things["Today"], statusOpenOnly, xml)
    return str(xml)


if __name__ == "__main__":
    print todayToXml()