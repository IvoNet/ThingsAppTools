#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
from things.Things import ThingsApp


if __name__ == "__main__":
    Things = ThingsApp()
    # print Things.tags()

    # for tag in Things.tags():
    #     print tag, tag.toDos()

    # x = Things.areas()
    # print x

    Things.logCompleted()

    for item in Things["Today"]:
        print 80 * "="
        print item
        print "id              :", item.id()
        print "name            :", item.name()
        print "notes           :", item.notes()
        print "area            :", item.area(), item.area().id()
        print "project         :", item.project()
        print "is open item    :", item.is_open()
        print "tagNames        :", item.tags()
        print "creationDate    :", item.creationDate()
        print "activationDate  :", item.activationDate()
        print "completionDate  :", item.completionDate()
        print "dueDate         :", item.dueDate()
        print "cancellationDate:", item.cancellationDate()



        # for item in dir(Things):
        #     if not item.endswith("_"):
        #         print item

        # print help(Things)

        # todos Things.toDos()
        # sys.exit()

        # print help(Things.lists())

        # print help(Things.lists().objectWithName_("Today"))
        # print Things.lists().objectWithName_("Today").toDos()
        # todos = Things.toDos()

        # for item in  dir(todos[0]):
        #     if not item.endswith("_"):
        #         print item

        # for todo in todos:
        #     print todo