good = r"""
        (,        ,)
        |  *_      |
        \\ (('^,  //
         \`()) _.'/
          ` )__)-'
            \  )
             )(
            /  `_.'_
           /   /_ , )
          /_.-'  ( /
            \ |  ,/
             \'( /
             ),)/
            ( )`
             \
             , 
 ejm         '|
             \/
"""

bad = r"""
        (,        ,)
        |  *_      |
        \\ (('^,  //
         \`()) _.'/
          ` )__)-'
            \  )
          .__)(_.'___________
          \_    _/_ ,.__,-_,-'
            \`-'   
             \'
             ),
            ( )
             \
             , 
 ejm         '|
             \/
"""
torch_lit = False
if torch_lit:
    outcome = "Flicker: I can see!"
    print(good)
else:
    outcome = "Doom: I can't see!"
    print(bad)
    print(outcome)
