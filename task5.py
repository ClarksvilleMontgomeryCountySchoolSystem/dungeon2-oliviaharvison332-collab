good = r"""
88                     88 88                     
88                     88 88              ,d     
88                     88 88              88     
88,dPPYba,  ,adPPYYba, 88 88  ,adPPYba, MM88MMM  
88P'    "8a ""     `Y8 88 88 a8P_____88   88     
88       d8 ,adPPPPP88 88 88 8PP"""""""   88     
88b,   ,a8" 88,    ,88 88 88 "8b,   ,aa   88,    
8Y"Ybbd8"'  `"8bbdP"Y8 88 88  `"Ybbd8"'   "Y88
"""

bad = r"""
 _           _ _      _   
| |         | | |    | |  
| |__   __ _| | | ___| |_ 
| '_ \ / _` | | |/ _ \ __|
| |_) | (_| | | |  __/ |_ 
|_.__/ \__,_|_|_|\___|\__|
"""
escaped = True
if escaped:
    outcome = "Legend: We got out!!"
    print(good)
else:
    outcome = "Doom: OH NO! The exit disappeared"
    print(bad)
    print(outcome)