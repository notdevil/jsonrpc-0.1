			Cambrionix API
			==============

This is some example Python code and supporting modules for
accessing the Cambrionix API.

You will need Python installed on your computer
For Windows this can be downloaded from
https://www.python.org/downloads/
OS/X and Linux will almost certainly have Python already installed.

Cambrionix have tested with Python v2.7.8

You will also need setuptools installed for Python

https://pypi.python.org/pypi/setuptools

The python setup requires a working internet connection to install the
necessary support modules.

Once that is ready extract the contents of this zip file to a directory.
Using a command line enter the directory you created and then enter the jsonrpc-0.1 directory and then execute
python setup.py install

In the examples directory is cbrx_api_quickstart.py which you can use as a
confidence test that everything is installed correctly.
If you have a Cambrionix universal charger attached to the local machine on
executing
python cbrx_api_quickstart.py
you should see it report the number of ports on the Cambrionix charger.

jsonrpc is the python JSON-RPC library

cbrxapi is a helper script that declares cbrxapi and looks up the port number
