__doc__ = "Implementation of a Singleton"
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


class Singleton(object):
    """ A Pythonic Singleton
    Just have your class inherit from Singleton,
    and don't override __new__. Then, all calls to that class
    (normally creations of new instances) return the same instance.
    (The instance is created once, on the first such call to each given
    subclass of Singleton during each run of your program.)
    """

    # noinspection PyArgumentList
    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = object.__new__(cls, *args, **kwargs)
        return cls._inst