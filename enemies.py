import random

stormtrooper = { "name": "stormtrooper",
                 "description": "Can't shoot for shit",
                 "health": random.randint(1,10),
                 "damage": random.randint(1,100),
                 "items":["blaster","helmet"],
                 "killwords":["bang","pew","shoot","kill"]
                 }


gorak = { "name": "gorak",
          "description": "",
          "health": 5,
          "damage": 10,
          "items" : [],
          "killwords":["bang","pew","shoot","kill"]
          }
          

greedo = { "name": "Greedo",
           "description":"Who shot first?",
           "health":50,
           "damage":20,
           "items":["password"],
           "killwords":["bang","pew","shoot","kill"]
           }

darth_kirill = { "name" : "Darth Kirill",
                 "description": "He is your lecturer.",
                 "health" : 100,
                 "damage": 100,
                 "items": ["lightsaber","mask","cigarettes"],
                 "killwords":["clash","strike","force push","force choke","hit"]
                 }
