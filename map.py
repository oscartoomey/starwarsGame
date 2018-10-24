from items import *
location_landspeeder = {
    "name": "Landspeeder",

    "description":
    """You have found a very aged Landspeeder. It needs power converters to fly""",

    "items": [],

    "exits": {"north": "Farm"},

}

location_toschestation = {
    "name": "Tosche Station",

    "description":
    """You have travelled to Tosche station. The shop seems top sell power converters...""",

    "items": [item_powerconverter],

    "exits":  {"west": "Farm"},

    
}

location_cantina = {
    "name": "Cantina",

    "description":
    """You have arrived at the Cantina. The place is lively and the band is jazzy""",

    "items": [],

    "exits": {"east": "Farm", "west": "booth", "north": "bar", "south": "TIE Fighter" },

}

location_booth = {
    "name": "Booth",

    "description":
    """You have entered a nearby booth""",

    "items": [],

    "exits": {"east": "Cantina"},

}

location_farm = {
    "name": "Farm",

    "description":
    """The farm is desolate. The harvest hasn't been great this year""",

    "items": [],

    "exits": {"west": "Cantina", "south": "Landspeeder", "east": "Tosche Station"},

}

location_bar = {
    "name": "Bar",

    "description":
    """The bar is oddly sticky and crowded""",

    "items": [],

    "exits": {"south": "Cantina"}

}

location_tiefighter = {
    "name": "TIE Fighter",

    "description":
    """The TIE Fighter is very advanced with the newest technology, as expected of Darth Vader's equipment""",

    "items": [],
        
    "exits": {"north": "Cantina", "south": "Death Star"}

}

location_deathstar = {
    "name": "Death Star",

    "description":
    """The Death Star is a large, brightly-lit ship""",

    "items": [],

    "exits": {"north": "N/4.07", "south": "TIE Fighter", "east": "Leia's Cell"}


}

location_leiascell = {
    "name": "Leia's Cell",

    "description":
    """Leia's cell. Just an average jail cell""",

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
