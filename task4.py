good = r"""
        _/.-
     ../.-'(()
    (( ) )))
     /)- _))
    ( \_  )
     \-\|(__
      \/-'  \
      (_) |\-\
       | (  ) )
       |--\/_'
   _.-'  . \_'._
   '-.'_|_|__\.-'
       | /. \
       |(  '.\
       \ \   \'.
        \_)   \_)
         )| mrf\|
   ___,-'__)___|\
               | )
               '.'
"""
bad = r"""
888             888888        888    
888             888888        888    
888             888888        888    
88888b.  8888b. 888888 .d88b. 888888 
888 "88b    "88b888888d8P  Y8b888    
888  888.d88888888888888888888888    
888 d88P888  888888888Y8b.    Y88b.  
88888P" "Y888888888888 "Y8888  "Y888 
"""
drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: We need to leave!"
    print(good)
else:
    outcome = "Doom: How did that happen?"
    print(bad)
    print(outcome)