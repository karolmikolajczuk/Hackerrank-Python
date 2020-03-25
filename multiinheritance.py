# Here's a fun example of what's going on

class Tractor():
    def plow(self):
        print("Plowing regular fields on earth!")

class Farm(Tractor):
    def clean_barn(self):
        print("Mucking the stalls.")
        
    def do_farm_things(self):
        self.plow()
        self.clean_barn()

# Sweet, we have our Farm, and it has a basic tractor
# But I'm moving to the Moon to start a MoonFarm, which is the same as running a regular Farm, but we need to use a MoonTractor that's modified for plowing moondirt.

class MoonTractor(Tractor):
    def plow(self):
        print("Plowing fields on the moon!")

# Now we just need our stub MoonFarm to extend Farm and MoonTractor

class MoonFarm(Farm, MoonTractor):
    pass

# moon farm
farm = MoonFarm()
farm.do_farm_things()

# regular farm
farm = Farm()
farm.do_farm_things()
