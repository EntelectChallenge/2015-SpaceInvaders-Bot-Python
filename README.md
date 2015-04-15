# Python
If you plan to develop your entry in Python you need to download and install [Python 2.7.9](https://www.python.org/downloads/release/python-279/).

## Get The Code
Download the [zip file](https://github.com/EntelectChallenge/2015-SpaceInvaders-Bot-Python/archive/master.zip) from Github or use Git to clone the repository:
* Start Git Bash
* Change to the directory where you want to checkout the sample bot
* Run: `git clone https://github.com/EntelectChallenge/2015-SpaceInvaders-Bot-Python.git`

## Compile
The easiest way to compile is to open a Command Prompt, change to your bot folder and run `compile.bat`. This will use SetupTools to fetch your dependencies and build your bot. For details on using SetupTools see the section below...

## Run
Once you have compiled you can do a basic test of the bot by simply launching a Command Prompt, changing to the bot directory and running `run.bat output`. This will use the example state and map files in the output folder.

## SetupTools
If you wish to use 3rd party library dependencies you should include ez_setup.py from [SetupTools](https://pypi.python.org/pypi/setuptools) with your project.

You can then write a compile.bat containing the following to fetch your dependencies (in this example we are adding the EasyAI library as in the sample Python bot):
```powershell
python ez_setup.py
easy_install EasyAI
rm *.zip
```