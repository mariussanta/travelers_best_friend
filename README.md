#
[Traveler's best friend](https://github.com/mariussanta/travelers_best_friend)

#### Description
Traveler's best friend is a web app that comes to your help, when in need for an "escape" plan from the daily routine. Regardless of time, duration, destination 
s.a we provide solution to manage with easy and efficiency your travel plan down to the last detail.

#### Setup
* install [Python 3.8](https://www.python.org/downloads/)
* set up [pip](https://pip.pypa.io/en/stable/installing/) if needed
* install any IDE. ([PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
* clone the [repository](https://github.com/mariussanta/travelers_best_friend):
    * git clone git@github.com:mariussanta/travelers_best_friend.git
* configure your venv, [Pycharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html?gclid=CjwKCAiAv4n9BRA9EiwA30WNDw26q6dRbQghfY8I5E3sP8qHn1gTgw0fBCWV39qHoIm64cKCV0eO2hoCMhMQAvD_BwE).
* install all libraries from requirements.txt by either following a [guide](https://note.nkmk.me/en/python-pip-install-requirements/) or installing them one by one or googling how-to
    * pip install -r requirements.txt
* run the server
    * python manage.py runserver
    
#### Project Roadmap

|Status|Nr|Feature|Details|
|:---|:---|:---:|:---:|
|**Completed**|1|Basic functionalities|register, login, logout
| |2|Premium membership|add free/ multi user support/ custom UI (change background color, etc.)|
| |3|Sticky notes|custom notes that can be simple messages like “Can wait the trip to start!”, or warnings like “Note that place x is in renovation” or informative like “Medical assurance per person is x ron”/ will have a simple dismiss button|
| |4|Add the weather forecast for any searched city, including the prediction for the next 7 days|real time weather report|
| |5|Provide the local time for the searched city, besides the weather|set up multiple time zones clocks/  customizable with different sizes|
| |6|Alert the user if there is bad weather|real time alert for rain or temperatures drop below/ above a certain desired limit|
| |8|Background color customization|premium users only|
| |9|Convert/ show temperature both in celsius and/or fahrenheit|possibility to have an input/output values in any desired unit measure|
| |10|Do not disturb periods|mutes alarms for specified period|
| |11|Create an itinerary for the trip|multiple functionalities, a short summary for every option/stop, when expanded it will show accommodation, transport, entertainment, extra fees (entrances, concerts)|
| |12|Alarm to not miss trips or rides|basic warnings to respect schedules before and during the trip/ optional(send phone message)|
| |13|Multiple users can edit the same pages and share the trip information|premium users only: a group of user can join the same plan trip|
| |14|Voting section|premium users only: when user suggests a certain accommodation or itinerary and the other participants can vote or comment around the proposal/ vote pass or fail functionality when all participants have voted|
| |15|Total cost of the trip|a final expenses evaluation in real time( with alarm when overstepping budget)|



