#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
__doc__ = "Empties the trash in Things"
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
from things.Things import ThingsApp

if __name__ == "__main__":
    print "Emptying the trash in Things.app..."
    ThingsApp().emptyTrash()