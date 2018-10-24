from items import *
location_landspeeder = {
    "name": "Landspeeder",

    "description":
    """You have found a very aged Landspeeder, buried in the warm sand. It is rough and course, and keeps getting everywhere. 
It needs power converters to fly. You remember your uncle telling you that they sell power converters at the local Tosche Station.""",
    
    "items": [],

    "exits": {"north": "Farm"},

}

location_toschestation = {
    "name": "Tosche Station",

    "description":
    """You have travelled to Tosche station. You take a goosey gander through the window, only to find...Huzzah! Power Converters!
    It seems that the station has been abandoned however, so it would be wise to steal them in these financially bleak times...""",

    "items": [item_powerconverter],

    "exits":  {"west": "Farm"},

    
}

location_cantina = {
    "name": "Cantina",

    "description":
    """You are at the Cantina. The place is lively and the band is jazzy. To the west, you see a comfy booth.""",
    
    "items": [],

    "exits": {"east": "Farm", "west": "booth", "north": "bar", "south": "TIE Fighter" },

}

location_booth = {
    "name": "Booth",

    "description":
    """You have entered a nearby booth. You feel safe from the menacing atmosphere of the bar. To the east of you is the centre of the centre 
of the Cantina.""",
    
    "items": [],

    "exits": {"east": "Cantina"},

}

location_farm = {
    "name": "Farm",

    "description":
    """The farm is desolate. The harvest hasn't been great this year. The dried soil 
crunches beneath your feet. The hot sun beats down on you.""",
    
    "items": [],

    "exits": {"west": "Cantina", "south": "Landspeeder", "east": "Tosche Station"},

}

location_bar = {
    "name": "Bar",

    "description":
    """The bar is oddly sticky and crowded. There are many frightening goons about, most you recognise to be deadly bounty
hunters.""",
    
    "items": [],

    "exits": {"south": "Cantina"}

}

location_tiefighter = {
    "name": "TIE Fighter",

    "description":
    """The TIE Fighter is very advanced with the newest technology, as expected of Darth Vader's equipment.
The cabin smells of strong a tobacco. The vast open space ahead is intimidating, even for experienced
pilots.""",
    
    "items": [],
        
    "exits": {"north": "Cantina", "south": "Death Star"}

}

location_deathstar = {
    "name": "Death Star",

    "description":
    """The Death Star is a large, brightly-lit ship. You can hear the faint noise of Stromtroopers marching in the distance.
You are very tense as you are about to approach your final battle.""",

    "items": [],

    "exits": {"south": "N/4.07", "north": "TIE Fighter", "east": "Leia's Cell"}

}

location_leiascell = {
    "name": "Leia's Cell",

    "description":
    """Leia's cell, you can see her through the window. She looks back at you in relief and rushes
to the door.""",
    
    "items": [],

    "exits": {"west": "Death Star"}
}

location_n407 = {
    "name": "N/4.07",

    "description":
    """A place where good people go to die""",
    
    "items": [item_key],

    "exits": {"south": "Death Star"}

}

locations = {
    "Landspeeder": location_landspeeder,
    "Tosche Station": location_toschestation,
    "Farm": location_farm,
    "Cantina": location_cantina,
    "Booth": location_booth,
    "Bar": location_bar,
    "TIE Fighter": location_tiefighter,
    "Death Star": location_deathstar,
    "Leia's Cell": location_leiascell,
    "N/4.07": location_n407
    }
    
