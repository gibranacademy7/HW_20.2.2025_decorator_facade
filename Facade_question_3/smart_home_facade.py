class SmartHomeFacade:
    def __init__(self, lights, tv, ac, popcorn_machine):
        self.lights = lights
        self.tv = tv
        self.ac = ac
        self.popcorn_machine = popcorn_machine

    def say_good_morning(self):
        self.lights.turn_on()
        self.tv.turn_on_music_channel()
        self.ac.set_temperature(22)

    def say_watch_movie(self):
        self.lights.turn_off()
        self.tv.turn_on_netflix()
        self.ac.set_temperature(18)
        self.popcorn_machine.turn_on()
        self.popcorn_machine.dispense_popcorn()
        self.popcorn_machine.turn_off()

    def say_good_night(self):
        self.lights.turn_off()
        self.tv.turn_off()
        self.ac.set_temperature(28)
