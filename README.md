# Seating Application

Python flask based implementation of ELSA (ELectronic Seating Application).

## Development machine configuration

Use these steps to get up and running

* Ensure you have Python 3.7 and pip installed
* Clone this repository
* Create a virtual environment with
    * Mac: `python3 -m venv venv`
    * Windows: `py -m venv venv`
* From the root directory run
    * Mac: `source venv/bin/activate`
    * Windows: `source venv/Scripts/activate`
* Install dependencies with `pip install -r requirements.txt`
* Downloading SQLite on
    * Windows: Download the DLL file for your device from https://www.sqlite.org/download.html
    * Extract the files and move them into C:\Users\youruser\Anaconda3\DLLs
    * Mac: ?
* Start the application with `flask run`
* See the command line for the URL to visit
* When finished run deactivate from the virtual environment