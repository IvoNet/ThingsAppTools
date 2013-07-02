try:
    from Foundation import *
    from ScriptingBridge import *
except:
    print "Please install the pyobjc package to make this script work."
    print "Working on a Mac and having Things installed is also a must :-)."

import Null

UTF_8 = "utf-8"


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
        #TODO wrap this lists in my own ThingsLists
        return self.Things.lists()


class ThingsLists(object):
    def __init__(self, items):
        self.lists = items

    def __iter__(self):
        return self.lists.__iter__()


class ThingsToDos(object):
    def __init__(self, todoList):
        self.todos = []
        [self.todos.append(ThingsToDo(x)) for x in todoList]

    def __iter__(self):
        return self.todos.__iter__()


class ThingsToDo(object):
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
        if self.todo.area().name() is None:
            return Null
        return ThingsArea(self.todo.area())


class ThingsArea(object):
    def __init__(self, item):
        self.area = item

    def __str__(self):
        return self.area.name().encode(UTF_8)

    def id(self):
        return self.area.id().encode(UTF_8)