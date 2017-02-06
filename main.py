#Credit for the football: http://www.chris.com/ascii/joan/www.geocities.com/SoHo/7373/sports.html#football
from time import sleep
from os import system
stages = [
r"""
   ---     _.-=""=-._ 
         .'\\-++++-//'.
   ---  (  ||      ||  )
         './/      \\.'
   ---     `'-=..=-'`
""",
r"""
           _.-=""=-._ 
   ---   .'||      ||'.
        (  //      \\  )
   ---   '.\\      //.'
           `'-=..=-'
""",
r"""
   ---     _.-=""=-._ 
         .'//      \\'.
   ---  (  \\      //  )
         '.||      ||.'
   ---     `'-=..=-'
""",
r"""
           _.-=""=-._ 
   ---   .'\\      //'.
        (  ||      ||  )
   ---   './/      \\.'
           `'-=..=-'`
""",
r"""
   ---     _.-=""=-._ 
         .'||      ||'.
   ---  (  //      \\  )
         '.\\-++++-//.'
   ---     `'-=..=-'
""",
r"""
           _.-=""=-._ 
   ---   .'//      \\'.
        (  \\-++++-//  )
   ---   '.||      ||.'
           `'-=..=-'
"""]
c = 0
while True:
	if c == 6:
		c = 0
	system("clear")
	print stages[c]
	sleep(0.25)
	c += 1
