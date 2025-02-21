# Create the device objects
from Facade_question_3.ac import AC
from Facade_question_3.lights import Lights
from Facade_question_3.popcorn_machine import PopcornMachine
from Facade_question_3.smart_home_facade import SmartHomeFacade
from Facade_question_3.tv import TV

lights = Lights()
tv = TV()
ac = AC()
popcorn_machine = PopcornMachine()

# Create the facade
smart_home = SmartHomeFacade(lights, tv, ac, popcorn_machine)

# Using the facade to perform actions
smart_home.say_good_morning()  # Morning routine
smart_home.say_watch_movie()  # Movie time routine
smart_home.say_good_night()  # Nighttime routine
