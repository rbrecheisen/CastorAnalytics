# CastorAnalytics
Desktop application for viewing summary statistics and advanced visualizations for your Castor EDC studies and sites.


## Installation
- If you do not have Python installed yet, first do that
- Go to https://www.python.org and download the installer for Python 3.12 or higher
- Follow the instructions when installing Python
- After successful installation, test the installation by opening a windows terminal (In Windows, search for "cmd")
- Type "python --version". You should the Python version printed


## Running the application
- Extract the CastorAnalytics-1.2.zip file somewhere. It will create a new directory "CastorAnalytics" with all the
files you need to run the program.
- First double-click the "clean-python-environment.bat" file. This is not strictly necessary when you have installed
Python for the first time but it makes sure that the Python environment is clean and has no external packages 
installed.
- Then double-click the "run-castoranalytics.bat" file. This will start the program. 
- Go to File > Settings and in the "API Settings" section specify the API credentials. You can find these in the 
Castor environment (https://data.castoredc.com) under Account > Settings. You can find the Account icon in the bottom 
left corner of the screen (its a little puppet). In the settings, go to "Castor EDC API". It will show your client ID.
If you have never generated a client secret before, do that now. Make sure to copy it and save it in a text file 
somewhere secure. If you loose it, you cannot find it back so you need to create a new one here.
- After you specify the API credentials, you can go back to the main page of the program. It will load all your
studies there. Click a study to view its details. A button "Get sites" allows you to retrieve site data.