__author__ = "Ivo Woltring"
__version__ = "$version: 00.01$"
__revised__ = "$revised: 2005-10-23 22:28:18$"
__copyright__ = "Copyright (c) 2005 Ivo Woltring"
__license__ = "Apache 2"

__doc__ = """
Recipe 6.17. Implementing the Null Object Design Pattern
Credit: Dinu C. Gherman, Holger Krekel

from:

Python Cookbook, 2nd Edition
By David Ascher, Alex Martelli, Anna Ravenscroft

Publisher : O'Reilly
Pub Date : March 2005
ISBN : 0-596-00797-3
Pages : 844

Problem:
You want to reduce the need for conditional statements in your
code, particularly the need to keep checking for special cases.

Solution:
The usual placeholder object for "there's nothing here" is None,
but we may be able to do better than that by defining a class
meant exactly to act as such a placeholder

Discussion
You can use an instance of the Null class instead of the primitive value None.
By using such an instance as a placeholder, instead of None, you can avoid many
conditional statements in your code and can often express algorithms with little
or no checking for special values. This recipe is a sample implementation of the
Null Object Design Pattern. (See B. Woolf, "The Null Object Pattern" in Pattern
Languages of Programming [PLoP 96, September 1996].)

This recipe's Null class ignores all parameters passed when constructing or
calling instances, as well as any attempt to set or delete attributes. Any call
or attempt to access an attribute (or a method, since Python does not
distinguish between the two, calling __getattr__ either way) returns the same
Null instance (i.e., selfno reason to create a new instance). For example, if
you have a computation such as:

def compute(x, y):
    try:
        lots of computation here to return some appropriate object
    except SomeError:
        return None


and you use it like this:

for x in xs:
    for y in ys:
        obj = compute(x, y)
        if obj is not None:
            obj.somemethod(y, x)


you can usefully change the computation to:

def compute(x, y):
    try:
        lots of computation here to return some appropriate object
    except SomeError:
        return Null( )


and thus simplify its use down to:

for x in xs:
    for y in ys:
        compute(x, y).somemethod(y, x)


The point is that you don't need to check whether compute has returned a real
result or an instance of Null: even in the latter case, you can safely and
innocuously call on it whatever method you want. Here is another, more specific
use case:

log = err = Null( )
if verbose:
   log = open('/tmp/log', 'w')
   err = open('/tmp/err', 'w')
log.write('blabla')
err.write('blabla error')


This obviously avoids the usual kind of "pollution" of your code from guards
such as if verbose: strewn all over the place. You can now call
log.write('bla'), instead of having to express each such call as if log is not
None: log.write('bla').

In the new object model, Python does not call __getattr__ on an instance for
any special methods needed to perform an operation on the instance (rather, it
looks up such methods in the instance class' slots). You may have to take care
and customize Null to your application's needs regarding operations on null
objects, and therefore special methods of the null objects' class, either
directly in the class' sources or by subclassing it appropriately. For example,
with this recipe's Null, you cannot index Null instances, nor take their length,
nor iterate on them. If this is a problem for your purposes, you can add all the
special methods you need (in Null itself or in an appropriate subclass) and
implement them appropriatelyfor example:

class SeqNull(Null):
    def __len__(self): return 0
    def __iter__(self): return iter(( ))
    def __getitem__(self, i): return self
    def __delitem__(self, i): return self
    def __setitem__(self, i, v): return self


Similar considerations apply to several other operations.

The key goal of Null objects is to provide an intelligent replacement for the
often-used primitive value None in Python. (Other languages represent the lack
of a value using either null or a null pointer.) These nobody-lives-here
markers/placeholders are used for many purposes, including the important case in
which one member of a group of otherwise similar elements is special. This usage
usually results in conditional statements all over the place to distinguish
between ordinary elements and the primitive null (e.g., None) value, but Null
objects help you avoid that.

Among the advantages of using Null objects are the following:

Superfluous conditional statements can be avoided by providing a first-class
object alternative for the primitive value None, thereby improving code
readability.

Null objects can act as placeholders for objects whose behavior is not yet
implemented.

Null objects can be used polymorphically with instances of just about any other
class (perhaps needing suitable subclassing for special methods, as previously
mentioned).

Null objects are very predictable.

The one serious disadvantage of Null is that it can hide bugs. If a function
returns None, and the caller did not expect that return value, the caller most
likely will soon thereafter try to call a method or perform an operation that
None doesn't support, leading to a reasonably prompt exception and traceback. If
the return value that the caller didn't expect is a Null, the problem might stay
hidden for a longer time, and the exception and traceback, when they eventually
happen, may therefore be harder to reconnect to the location of the defect in
the code. Is this problem serious enough to make using Null inadvisable? The
answer is a matter of opinion. If your code has halfway decent unit tests, this
problem will not arise; while, if your code lacks decent unit tests, then using
Null is the least of your problems. But, as I said, it boils down to a matter of
opinions. I use Null very widely, and I'm extremely happy with the effect it has
had on my productivity.

The Null class as presented in this recipe uses a simple variant of the
"Singleton" pattern (shown earlier in Recipe 6.15), strictly for optimization
purposesnamely, to avoid the creation of numerous passive objects that do
nothing but take up memory. Given all the previous remarks about customization
by subclassing, it is, of course, crucial that the specific implementation of
"Singleton" ensures a separate instance exists for each subclass of Null that
gets instantiated. The number of subclasses will no doubt never be so high as to
eat up substantial amounts of memory, and anyway this per-subclass distinction
can be semantically crucial.


"""

from Singleton import Singleton


class _Null(Singleton):
    """ Null objects always and reliably "do nothing." """

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __repr__(self):
        return ""

    def __str__(self):
        return ""

    def __nonzero__(self):
        return False

    def __getattr__(self, name):
        return self

    def __setattr__(self, name, value):
        return self

    def __delattr__(self, name):
        return self

    def __len__(self):
        return 0

    def __iter__(self):
        return iter(( ))

    def __getitem__(self, i):
        return self

    def __delitem__(self, i):
        return self

    def __setitem__(self, i, v):
        return self


if not __name__ == "__main__":
    import sys

    sys.modules[__name__] = _Null() #Import the instantion in stead of the module
else:
    Null = _Null()
    Test = Null
    print Test['a']
    for x in range(10): print Test[x]
    Test.helloworld(1) # No error even though the method does not exist
