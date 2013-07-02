try:
    from Foundation import *
    from ScriptingBridge import *
except:
    print "Please install the pyobjc package to make this script work."
    print "Working on a Mac and having Things installed is also a must :-)."

import Null

STATUS_OPEN = 1952737647
STATUS_CANCELED = 1952736108
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
        return self.todo.id()

    def name(self):
        return self.todo.name()

    def notes(self):
        return self.todo.notes().strip()

    def area(self):
        if self.todo.area().id() is None:
            return Null
        return ThingsArea(self.todo.area())

    def project(self):
        if self.todo.project().id() is None:
            return Null
        return ThingsProject(self.todo.project())

    def is_open(self):
        return self.todo.status() == STATUS_OPEN

    def is_canceled(self):
        return self.todo.status() == STATUS_CANCELED

    def is_closed(self):
        return self.todo.status() == STATUS_CLOSED


class ThingsToDos(object):
    """
        Wraps all the ToDos from a specific Things list.
    """

    def __init__(self, todoList):
        self.todos = []
        [self.todos.append(ThingsToDo(x)) for x in todoList]

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
        return self.project.id()

    def name(self):
        return self.project.name().encode(UTF_8)

    def is_active(self):
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
        return self.area.id().encode(UTF_8)

    def suspended(self):
        return self.area.suspended()


class ThingsAreas(object):
    def __init__(self, items):
        self.areas = []
        if len(items) > 0:
            if type(items[0]) is ThingsArea:
                print "!!!"
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


class ThingsLists(object):
    """
        Wraps the lists of Things
    """

    def __init__(self, items):
        self.lists = items

    def __iter__(self):
        return self.lists.__iter__()

    def byId(self, identifier):
        return self.lists.objectWithID_(identifier)


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






