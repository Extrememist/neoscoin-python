****************************
  Examples
****************************

A basic program that uses ``python-neoscoin`` looks like this:

First, import the library and exceptions.

::

    import neoscoinrpc
    from neoscoinrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``neoscoin`` instance of the current user on the local machine
with one call to
:func:`~neoscoinrpc.connect_to_local`. This returns a :class:`~neoscoinrpc.connection.neoscoinConnection` objects:

::

    conn = neoscoinrpc.connect_to_local()

Try to move one neoscoin from account ``testaccount`` to account ``testaccount2`` using 
:func:`~neoscoinrpc.connection.neoscoinConnection.move`. Catch the :class:`~neoscoinrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~neoscoinrpc.connection.neoscoinConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

