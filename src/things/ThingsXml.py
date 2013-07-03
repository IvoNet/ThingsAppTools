__author__ = 'ivonet'

from Things import ThingsToDos, ThingsArea, ThingsTags, ThingsProject, ThingsApp
import Null
import xmlwitch


def Xml():
    """
        Initializes a xmlwitch Builder instance.
    :return: xmlwitch.Builder
    """
    return xmlwitch.Builder(version='1.0', encoding='utf-8', indent=' ' * 4)


def printTags(thingsTags, xml=Xml()):
    if not isinstance(thingsTags, ThingsTags):
        raise TypeError("Input parameter should be a ThingsArea")
    if len(thingsTags) <= 0:
        return xml
    with xml.tags():
        for tag in thingsTags:
            print "Processing tag :", tag.name()
            with xml.tag():
                xml.id(tag.id())
                xml.name(tag.name())
    return xml


def printArea(thingsArea, xml=Xml()):
    if thingsArea is Null:
        return xml
    if not isinstance(thingsArea, ThingsArea):
        raise TypeError("Input parameter should be a ThingsArea")
    with xml.area():
        xml.id(thingsArea.id())
        xml.name(thingsArea.name())
        xml.suspended(str(thingsArea.suspended()))
    return xml


def printProject(thingsProject, xml=Xml()):
    if thingsProject is Null:
        return xml
    if not isinstance(thingsProject, ThingsProject):
        raise TypeError("Input parameter should be a ThingsProject")
    with xml.project():
        xml.id(thingsProject.id())
        xml.name(thingsProject.name())
        xml.active(str(thingsProject.is_active()))
    return xml


def printToDos(thingsToDos, xml=Xml()):
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
                printArea(todo.area(), xml)
                printProject(todo.project(), xml)
                printTags(todo.tags(), xml)
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


def printToday(thingsToDos, xml=Xml()):
    with xml.today():
        printToDos(thingsToDos, xml)
    return xml


def printInbox(thingsToDos, xml=Xml()):
    with xml.inbox():
        printToDos(thingsToDos, xml)
    return xml


def printProjects(thingsProjects, xml=Xml()):
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
                printTags(project.tags(), xml)
                printToDos(project.toDos(), xml)
    return xml


def printAreas(thingsAreas, xml=Xml()):
    with xml.areas():
        for area in thingsAreas:
            print "Processing area:", area.name()
            if area.suspended():
                continue
            with xml.area(title=area.name()):
                xml.id(area.id())
                xml.name(area.name())
                printToDos(area.toDos(), xml)
    return xml


def activeListsToXml():
    """Generates an XML representation of all lists in Tings"""
    Things = ThingsApp()
    xml = Xml()
    with xml.things(xmlns='http://com.culturedcode.things'):
        printToday(Things["Today"], xml)
        printInbox(Things["Inbox"], xml)
        printProjects(Things.projects(), xml)
        printAreas(Things.areas(), xml)
        printTags(Things.tags(), xml)
    return str(xml)


if __name__ == "__main__":
    Things = ThingsApp()
    today = Things["Today"]

    myXml = Xml()
    with myXml.things(xmlns='http://com.culturedcode.things'):
        myXml = printToDos(today, myXml)
    print myXml
