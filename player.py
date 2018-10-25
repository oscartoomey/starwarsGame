from map import *
from items import *

# TODO: everything in here.

luke = {"inventory": [item_lightsaber], # Luke's items.
        "max_mass": 10, # The amount Luke can carry.
        "location": location_farm, # The location Luke starts in.
        "health": 100, # Luke's current health.
        "max_health": 100, # Luke's maximum health.
        "damage": 0} # Luke's damage, goes up if picks up weapons

han = {"inventory": [item_pistol,item_chewie], # Han's items.
       "max_mass": 5, # The amount Han can carry.
       "location": location_bar, # The location Han starts in.
       "health": 100, # Han's current health.
       "max_health": 100, # Han's maximum health.
       "damage": 0} # Han's damage.
