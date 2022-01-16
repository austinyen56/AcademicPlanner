# SlugPlanning

***Making planning easier and stress-free***

## About:
This program is a python command line application that helps streamline the
class registration process. Using info given by students who have already taken
the class in the past and the flowchart given by the school, the program generates
a custom schedule according to your preferences. This way students don't have
to worry about scrambling the last day to find what classes to take. This also
allows for major advisors to answer more specialized questions rather than basic
information about class scheduling.

## How to run this application:
This is intended to be run in the terminal in either a Unix or Windows based
operating system. The program will prompt you to enter some information and generate the schedule based on the information given.

## Requirements and Dependencies
A text file (classes.txt) that includes all your past coursework will be required.

project is made in Python and these libraries are required in order for it to work (run SlugPlanning.py):

* **[platform](https://docs.python.org/3/library/platform.html)** :This library is used to obtain the user's OS type.
* **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** : Web scrapes data for each course in the database.
* **[colorama](https://pypi.org/project/colorama/)** : Creates colored output text in the commandline.
* **requests** : Allows HTTP requests for retrieving HTTP data.
* **os** : Allows terminal screen clearing and file handling.
* Obtained all courses from the UCSC course catalog [here](https://catalog.ucsc.edu/en/Current/General-Catalog/Courses/)




## Improvements
There are many components that we are looking to improve with this program. This
includes:

* Creating and adding an attractive UX/UI
* Extending this application to include more majors and minor classes
* Being able to retrieve difficulty of classes through online sources and posts (ratemyprof, reddit...) to improve and optimize this service
* Having the ability to store individual user data through an actual database


![slug] 