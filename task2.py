good = r"""
 _           _ _           _             
| |         | | |         (_)            
| |__   __ _| | | ___ _ __ _ _ __   __ _ 
| '_ \ / _` | | |/ _ \ '__| | '_ \ / _` |
| |_) | (_| | | |  __/ |  | | | | | (_| |
|_.__/ \__,_|_|_|\___|_|  |_|_| |_|\__,_|
"""

bad = r"""
88                     88 88                       88                         
88                     88 88                       ""                         
88                     88 88                                                  
88,dPPYba,  ,adPPYYba, 88 88  ,adPPYba, 8b,dPPYba, 88 8b,dPPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88 88 a8P_____88 88P'   "Y8 88 88P'   `"8a ""     `Y8  
88       d8 ,adPPPPP88 88 88 8PP""""""" 88         88 88       88 ,adPPPPP88  
88b,   ,a8" 88,    ,88 88 88 "8b,   ,aa 88         88 88       88 88,    ,88  
8Y"Ybbd8"'  `"8bbdP"Y8 88 88  `"Ybbd8"' 88         88 88       88 `"8bbdP"Y8 
"""
torch_lit = False
if torch_lit:
    outcome = "Flicker: I can see!"
    print(good)
else:
    outcome = "Doom: I can't see!"
    print(bad)
    print(outcome)