__doc__ = "Python module wrapping the Things API in convenient Python classes."
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
try:
    from Foundation import *
    from ScriptingBridge import *
except ImportError:
    print "Please install the pyobjc package to make this script work."
    print "Working on a Mac and having Things installed is also a must :-)."
    sys.exit(1)

import Null

STATUS_OPEN = 1952737647
STATUS_CANCELLED = 1952736108
STATUS_CLOSED = 1952736109
UTF_8 = "utf-8"


class ThingsToDo(object):
    """
        A representation of a Todo within Things.
    """

    def __init__(self, todo):
        self.todo = todo

    def __str__(self):
        return self.todo.name().encode(UTF_8)

    def id(self):
        """
        :return: The id of the todo
        """
        return self.todo.id()

    def name(self):
        """
        :return: the name of the todo
        """
        return self.todo.name()

    def notes(self):
        """
        :return: the notes of the todo
        """
        return self.todo.notes().encode(UTF_8).strip()

    def tags(self):
        """
        :return: ThingsTags element representing the tags of the todo
        """
        return ThingsTags(self.todo.tags())

    def area(self):
        """
        :return: the ThingsArea of the todo or Null of not present
        """
        if self.todo.area().id() is None:
            return Null
        return ThingsArea(self.todo.area())

    def project(self):
        """
        :return: ThingsProject the todo belongs to or Null of it does not belong to a project
        """
        if self.todo.project().id() is None:
            return Null
        return ThingsProject(self.todo.project())

    def is_open(self):
        """
        :return: True of status is OPEN else False
        """
        return self.todo.status() == STATUS_OPEN

    def is_canceled(self):
        """
        :return: True of status is CANCELLED else False
        """
        return self.todo.status() == STATUS_CANCELLED

    def is_closed(self):
        """
        :return: True of status is CLOSED else False
        """
        return self.todo.status() == STATUS_CLOSED

    def __check_date__(self, date):
        if date is None:
            return Null
        return date

    def creationDate(self):
        """
        :return: string representation of a the creation date
        """
        return str(self.todo.creationDate())

    def activationDate(self):
        """
        :return: Null if not filled or a date of the item is in Today
        """
        return self.__check_date__(self.todo.activationDate())

    def completionDate(self):
        """
        :return: Null if not filled or a date of the item is in marked as completed
        """
        return self.__check_date__(self.todo.completionDate())

    def dueDate(self):
        """
        :return: Null if not filled or a date of the item is in marked with a due Date
        """
        return self.__check_date__(self.todo.dueDate())

    def cancellationDate(self):
        """
        :return: Null if not filled or a date of the item is in marked as cancelled
        """
        return self.__check_date__(self.todo.cancellationDate())


class ThingsToDos(object):
    """
        Wraps all the ToDos from a specific Things list.
    """

    def __init__(self, todoList):
        self.todos = []
        [self.todos.append(ThingsToDo(x)) for x in todoList]

    def __str__(self):
        ret = "ToDos = {"
        ret += ", ".join([str(x) for x in self.todos])
        ret += "}"
        return ret

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.todos.__iter__()


class ThingsProject(object):
    """
        Represents a Things project
    """

    def __init__(self, item):
        self.project = item

    def __str__(self):
        return self.project.name().encode(UTF_8)

    def __repr__(self):
        return self.project.name().encode(UTF_8)

    def id(self):
        """
        :return: the project id
        """
        return self.project.id()

    def name(self):
        """
        :return: utf-8 representation of the name of the project
        """
        return self.project.name().encode(UTF_8)

    def tags(self):
        """
        :return: ThingsTags representation of the tags belonging to this project
        """
        return ThingsTags(self.project.tags())

    def notes(self):
        """
        :return: the notes of the project as a string
        """
        return self.project.notes().encode(UTF_8).strip()

    def toDos(self):
        """
        :return: ThingsToDos representation of the todos in this project
        """
        return ThingsToDos(self.project.toDos())

    def is_active(self):
        """
        :return: True if the project is active else False
        """
        return self.project.status() == STATUS_OPEN


class ThingsProjects(object):
    """
        The list of ThingProject items
    """

    def __init__(self, items):
        self.projects = []
        if len(items) > 0:
            if type(items[0]) is ThingsProject:
                self.projects = items
            else:
                [self.projects.append(ThingsProject(x)) for x in items]

    def __getitem__(self, item):
        """
            return the ThingsProject based on a name
        """
        return self.projects.objectWithName_(item)

    def __iter__(self):
        return self.projects.__iter__()

    def __str__(self):
        ret = "Projects = {"
        ret += ", ".join([str(x) for x in self.projects])
        ret += "}"
        return ret

    def __repr__(self):
        return self.__str__()

    def __active_projects__(self):
        ret = []
        [ret.append(x) for x in self.projects if x.is_active()]
        return ThingsProjects(ret)


class ThingsArea(object):
    """
        Represents a Things area item.
    """

    def __init__(self, item):
        self.area = item

    def __str__(self):
        return self.area.name().encode(UTF_8)

    def id(self):
        """
        :return: the area id
        """
        return self.area.id().encode(UTF_8)

    def name(self):
        """
        :return: the area name
        """
        return self.area.name().encode(UTF_8)

    def suspended(self):
        """
        :return: True of the area has been suspendec else False
        """
        return self.area.suspended()

    def toDos(self):
        """
        :return: ThingsToDos representation of the todos belonging to this area
        """
        return ThingsToDos(self.area.toDos())


class ThingsAreas(object):
    """
    Wrapper class for the Things areas
    """

    def __init__(self, items):
        self.areas = []
        if len(items) > 0:
            if type(items[0]) is ThingsArea:
                self.areas = items
            else:
                [self.areas.append(ThingsArea(x)) for x in items]

    def __str__(self):
        ret = "Areas = {"
        ret += ", ".join([str(x) for x in self.areas])
        ret += "}"
        return ret

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.areas.__iter__()

    def __active_areas__(self):
        ret = []
        [ret.append(x) for x in self.areas if not x.suspended()]
        return ThingsAreas(ret)


class ThingsTag(object):
    """
        Wrapper class representing a Things tag.
    """

    def __init__(self, item):
        self.tag = item

    def __str__(self):
        return self.tag.name().encode(UTF_8)

    def __repr__(self):
        return self.__str__()

    def name(self):
        """
        :return: the name of a tag
        """
        return self.tag.name().encode(UTF_8)

    def id(self):
        """
        :return: the tag id
        """
        return self.tag.id().encode(UTF_8)

    def parentTag(self):
        """
        TODO remove me??
        :return: the parent tag
        """
        return self.tag.parentTag()

    def toDos(self):
        """
        :return: ThingsToDos representation of the todos associated to this tag
        """
        return ThingsToDos(self.tag.toDos())


class ThingsTags(object):
    """
        Wrapper class for all Things tags
    """

    def __init__(self, items):
        self.tags = []
        if len(items) > 0:
            if type(items[0]) is ThingsTag:
                self.tags = items
            else:
                [self.tags.append(ThingsTag(x)) for x in items]

    def __str__(self):
        ret = "Tags = {"
        ret += ", ".join([str(x) for x in self.tags])
        ret += "}"
        return ret

    def __len__(self):
        return len(self.tags)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.tags.__iter__()

    def __getitem__(self, item):
        for tag in self.tags:
            if tag.name is item.encode(UTF_8):
                return tag
        return Null


class ThingsList(object):
    """
        Wrapper class for a Things list
    """

    def __init__(self, item):
        self.list = item

    def __str__(self):
        return self.list.name().encode(UTF_8)

    def __repr__(self):
        return self.__str__()

    def id(self):
        """
        :return: the list id
        """
        return self.list.id().encode(UTF_8)

    def name(self):
        """
        :return: the name of the list
        """
        return self.list.name().encode(UTF_8)

    def toDos(self):
        """
        :return: ThingsToDos representing the todos belonging to this list
        """
        return ThingsToDos(self.list.toDos())


class ThingsLists(object):
    """
        Wraps the lists of Things
    """

    def __init__(self, items):
        self.lists = []
        if len(items) > 0:
            if type(items[0]) is ThingsList:
                self.lists = items
            else:
                [self.lists.append(ThingsList(x)) for x in items]

    def __iter__(self):
        return self.lists.__iter__()

    def __str__(self):
        ret = "Lists = {"
        ret += ", ".join([str(x) for x in self.lists])
        ret += "}"
        return ret

    def __repr__(self):
        return self.__str__()

    def byId(self, identifier):
        """
        Find a list by providing the id of the list
        :param identifier: the id of the list to get
        :return: the List belonging to the provided identifier
        """
        #TODO should return ThingsList??
        return self.lists.objectWithID_(identifier)

    def byName(self, identifier):
        """
        Find a list by providing the name of the list
        :param identifier: the name of the list to get
        :return: the List belonging to the provided identifier
        """
        #TODO should return ThingsList??
        return self.lists.objectWithName_(identifier)


class ThingsApp(object):
    """Wrapper for Things.app"""

    def __init__(self):
        self.Things = SBApplication.applicationWithBundleIdentifier_("com.culturedcode.things")
        if not self.Things.isRunning():
            print "Things does not appear to be running. Activating it now..."
            self.Things.activate()

    def __getitem__(self, item):
        """returns all todo's in a specific list"""
        return ThingsToDos(self.Things.lists().objectWithName_(item).toDos())

    def emptyTrash(self):
        """Empties the trash in Things"""
        self.Things.emptyTrash()

    def logCompleted(self):
        """Archives completed items"""
        self.Things.logCompletedNow()

    def lists(self):
        """
        returns all the lists in the Things app. Even the obsolete and done ones.
        :return: ThingsList representing all the lists in Things
        """
        return ThingsLists(self.Things.lists())

    def projects(self):
        """retrieve all the active projects from Things"""
        return ThingsProjects(self.Things.projects()).__active_projects__()

    def all_projects(self):
        """retrieve all projects from Things"""
        return ThingsProjects(self.Things.projects())

    def areas(self):
        """retrieve all active (non suspended) areas from Things"""
        return ThingsAreas(self.Things.areas()).__active_areas__()

    def all_areas(self):
        """retrieve all areas from Things"""
        return ThingsAreas(self.Things.areas())

    def tags(self):
        """
        :return: ThingsTags representation of all tags used in Things
        """
        return ThingsTags(self.Things.tags())
