#           +-------------------------+                   +------------+
#           |   SmartHomeFacade       | <>----------------|  Lights    |
#           +-------------------------+                   +------------+
#           | - lights: Lights        |                   | +turn_on() |
#           | - tv: TV                |                   | +turn_off()|
#           | - ac: AC                |                   +------------+
#           | - popcorn_machine: PopcornMachine |
# +-------------------------+
# | +say_good_morning()     |
# | +say_watch_movie()      |
# | +say_good_night()       |
# +-------------------------+
#         |
#         |
#         |
# +-------+--------+      +-----------+      +----------------+
# |     TV         |      |    AC     |      | PopcornMachine |
# +----------------+      +-----------+      +----------------+
# | +turn_on_music_channel()  | +set_temperature()   | +turn_on()      |
# | +turn_on_netflix()        |                       | +dispense_popcorn() |
# | +turn_off()               |                       | +turn_off()     |
# +----------------+          +----------------+      +----------------+

#------------------------------------------------------------------------------------

#********* Facade UML Diagram Overview:


# The diagram should include:
#
# SmartHomeFacade
#
# Attributes: lights, tv, ac, popcorn_machine
# Methods:
# say_good_morning()
# say_watch_movie()
# say_good_night()
# Lights
#
# Methods:
# turn_on()
# turn_off()
# TV
#
# Methods:
# turn_on_music_channel()
# turn_on_netflix()
# turn_off()
# AC (Air Conditioner)
#
# Methods:
# set_temperature(temperature)
# PopcornMachine
#
# Methods:
# turn_on()
# dispense_popcorn()
# turn_off()
