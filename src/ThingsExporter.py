#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
import sys
from things.Things import ThingsApp
import things.ThingsXml as ThingsXml


if __name__ == "__main__":
    output = ThingsXml.activeListsToXml()
    print output
    fo = open("../tmp/ThingsLists.xml", "w")
    fo.write(output)
    fo.close()
