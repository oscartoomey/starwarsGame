from map import *
from items import *

# TODO: everything in here.

luke = {"luke_inventory" : [], # Luke's items.
        "luke_max_mass" : 10, # The amount Luke can carry.
        "luke_start_location" : location_alderaan, # The location Luke starts in.
        "luke_max_health": 100, # Luke's maximum health.
        "luke_damage": 6 #luke's damage, goes up if picks up weapons
         }

han = {"han_inventory" : [], # Luke's items.
       "han_max_mass" : 5, # The amount Luke can carry.
       "han_start_location" : {}, # The location Luke starts in.
       "han_max_health" : 1} # Han's maximum health.

inventory = []
max_mass = -1
current_location = {}
max_health = -1
health = -1
