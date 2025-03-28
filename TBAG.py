# Cairo Taylor and James Wilcox , Text-Based Adventure Game
import random
def battle(creature, action, location1, location2):                   #written by james, this code is the base combat system, which includes an better chance of victory if you pick up a slingshot
   print(f"The {creature}, positioned in front of you, is ready to strike!")
   print(f"1 is {location1}, 2 is {location2}.")
   move = input(f"Where do you plan to {action}?\n")
   if slingshot == "Yes":
       defense = random.randint(1,2)
   else:
       defense = random.randint(1,5)
   if defense == move:
       print(f"The {creature} dodged your attack!")
       print(dedend)
       exit()
   else:
       print(f"You surprised the {creature} and it fled!")


def split(choice1, choice2):                   #written by cairo, this code is the base decision making system
  print(f"You see 2 pathways that you could take. Do you want to: \n1. {choice1},\nOR\n2. {choice2}?")

sewerdweller = "You live in the sewer until the last of your days. This is a hidden ending!"
dungeondweller = "You live in the dungeon until the last of your days. This is a hidden ending!"
befriend = "You managed to befriend the bird! You managed to get the best ending and you now have a forever friend."                  #these are all the different endings, collaborated by both james and cairo
sneakend = "You manage to sneak to the surface world and not get eaten. Congratulations! However, that bird could have been friendly! You got the default ending."
dedend = """You failed to escape! You got the worst ending.
 ..........                                                              
                                                                                                      ..  .............                                                        
                                                                 ...     .......    .......................-::::................                                               
                                                                 ..........................---::..........:----=..................                                             
                                                                ...... .................:-===========-::---------..................                                            
                                                                ..................::-=+**+=++++++++==+==--------=-:................                                            
                                                           ..............:=++==*===+=====++++====++++-=====--------::..............                                            
                                                           ... .......:-=====+++*==**=====+*====+===+====-----:::----:-::::........                                            
                                      ......    ................:+*+*+=====++=++=++++*=====++==++===+=-=+==-::::---------:::::................                                 
                                ............................-===++===+==+++++++=++*=+++++++++++==+++====-++=-::------------::::::.............                                 
                                ........................:=+*=+=*++==++++++++=+++++++++=++======+=-==----=--=-::--:-----=------::::............                                 
                               .......  ..........:---=+++=++++=+==+++++++====+*+=+=+++++++++*=--::::::::::::::.:::-::--------=-----:.........                                 
                               ................++=+++++**+=++++++=+=++=++++++*++=++=++++++++++=-::::::::::::..::.....::-------=-=-==-:........                                 
                               ............-++*+++++==+=++*++*++==+===+=+++*+=+++++++++++++++===----::--:-------::::::::--=-===-==-==--.......                                 
                     .......   .........:-=+*===*+++==*++**++*+==++++++++++++++++++++++*+++++==---:--=-=====---=--:::::::--=-===+=+=+++=-.......                               
                     ..............-==+*===++===+***=+*+++*+++==+*++=++++++++++++++++++++++++======-=**X**X%X*=--=--:::::-=--===+***XXX*=+..............                       
                     .. ........-=====+===+**===+XX*+**+++++=++=+**++++++++++++++++++++++++==+=+--:=+***XX*XX@%*:--=-::::=====+*+*XXX*++*+=.............                       
                     ...........===+++===+=+++=+++++**+++*=++++++++===++++++++++=*++++=-==----=-::-+**X%XX**%X%X=--=+=::-=+==+**+*X**++*%X*+=:..........                       
                   ...........-+++*=*+====++=+**++==+++=++++++=+++++=+++++++++++*+++====---=----::-+**X%@@%%XXX%*---==--==+===*++***++*%%@X*=-==:.......                       
                ...........:+====+*=+X+==+**===++**+==+=+**+++++*+=++==+*++++++++*+=++======-----::=**XX%%%X%X@X+=-===---=+++*++****+*X+%%*===--===:....                       
........   .........::--==+*+===+**=++*==+**+==+++++=+=+=+**+**+*+++++****++++++++++++=====---:--=--=+**XXXX%X*+--==+==-=++=*+*=****+*+++*++==---====:....  ..   .             
...............:-==+*+=++=+++==+*X*++**+++***+++=+*+++++++++++*+++++++++++++++++++++++===-----::::----==+++++=----==++*===*+=+===++**+====---==========:...........            
......:::---=++==++*+=*+-===++=+*X+++++**+**+**++=++===++++++=**+++++=+++++++++++++++++====---::::::----=---------==++==++====-=++++--=-====---========+=.........             
....:-==++**X+==+***+*X+====++=+*X+==+++*****+**===++===-====+++++=++++++++++++++=++++++=------:::::::-----====+++==-----========++=-====--====---=====+++.... ...             
..:=====++++*+=++++*X***X*+***===+++=+++=**+++*+====++++++++==++=++++=++++++++++++++++====----:---::-::---=====-===-----=====-=++*+---===---::---=======+++...   .             
+++====+*+====+++**+*X++****+*+======+**=++*++++====+++++==+***+++++++++++++++++++++=+=========-----------=--======----===-===+++*+========-----======++=+*+...                
*X***+**++=++++++++*XX*+*****+**=====++*+==+*++++=+=+==++++=+**+*++++++++++*+++++*+++++============-::::-------==-----=-======+**X*==+=+===-==========+=+++**...               
+***X**X*++===++++*X+*XX**XXX*=+**++++++*+=+*+++++++++====+==+**++*******+++++++++++++++++===-======--------=----------=====++*XX%%%X*XX*==+=++++++++=++=++*X-.....            
++*******X*****++++**++**+++*X*+++++++*****+**++++*++++++*+*+*XX*********+++++++++++++++=++==++=====-:-----=--::::-----===++*XXX**++++:.-++XXX**+++++++++++**=.....            
%%%%*++++****XX**+X*X*++*++=+**X*++++++X+=+X*X+++++==++*=+++*+******X*+++****++++**+++**++=++====---======----:::::---==++++**%=....... .....-*XXXXX*********+.....            
++**X**X*+++**XX*****XX***+=+++******+*XX=+++**+++++==+*+*X++*++**XX*+++++++*******++++*+=++**+*+=========----::::----==++***:........  ..... ..:===:=XX*X****.....            
+*+***+++**+*****+++++*XXXXX+=++++++++**%X+=++*XX*++++******+++++**X****+++++********+*X*+++++++=========-----------===+***X:.........  ..............-XXXXX*=.....            
+++++**+++**X*+++**++++**X%%%%X++++++++X%XX+++++*XX+++*X*+***X++++**++***+*********++++++++=++++=+========--------=-==++***+..........  ...............+XXX*X-.....            
=+++===+******X**++****++**X%%%%***+***XX%X*X*++*XX++++*X++*+**++*+++****++++++**+*+**++**++*+++===-======--------===+****X........                   .:*X**X:....             
+++++++++++****X**++=++++****XX%%*++++++**XX+***XXX*++++**++++****++++++++*++++***+**++++*++++===========--------===+*=+++X%*:....                    ..+*XX+.....             
+++++++*++=+=+++++***XX*+*+++***XX*+=++++**+****X%XX*++++**++++***++++++++*+++++++***X+=++==+++=====--=-------=-===+*++++*%%XXX:......                ..-**X......             
==+=+++++*+++=+++++++***X*+====-++***++==+**+**+*XXX*++++=**++++*%X++++++++*++++++++*X**++===+=======------==-=====++*++*+*@***%*... .                ..:*X:......             
+==+++++++**++++=+++==+*****++=====++*++++***++++*X**X++=+++++******+++++=+++++*+==+++++++==+=======-------===-===+**+***++%X*X*X@:....               ..:*.........            
**+==+**+++++*++===++=+=++++***XX==*+++++++***==++**+***+*+++*++++++***+++++++++***++==+==+=======-------===-===+***+**+**+*%XXX*%=....                ...........             
++**X==+=+**++*+++++++==++==**++**+==+=++=++++*+=++**+X+***+***++==++++++++=+++++=++===+===-====----==========++******++++=+@%%%%%=....                                        
++X+**++**********+++++++=+=++++++*X+=*++++*==+*X++***+*+++**+***+++++++++++======+++====+======---=========+++**+****+++=++%@@@@%.....                                        
*%=+***+***X*+**X*++****+=++++++++***X*+++++*===+***+XX*X+++**+++**++++==++++===+===++++++====-==----=====+++*********+++==**@:........                                        
X*++X%+*+***X***X*+++****X=*+*++++*******+***++++=++*X*XXX*++++**+**+++++*++++===+===========-==--=====+=:..-+**XX*XX***++++X*%X+-:....                                        
*%%%%XX%X*++X%X**X++++*****+*++++++******++****+++==+====**XX*+++++++*+*++++==+++=++===================:......:=**XXXX*XX***+*X***+*=..                                        
XX***X%%X%@@@X**XX+++++*+***+++++++**X*+**+*X++*+===+==+++++++**++XX**++***+=================++==++==:............-+*X****XXXXXXX+-....                                        
**X**XXXXX%%X%%XXX*++++*++***X+++++***X++***++++**+=+++==++===+++++*XX*++**X+======++========+++++++....  ..     ........::::.....                                             
X*X*XX**XXX%XXX@%@X*+++++*+**X**++++*+*X**+**X**++****++=+++===++=+=**+++++++++==++++++++++======-.....   ..     ........  ......                                              
X%%X*****XXX**XX%%%%X++***+*+*XX*++++++***+**XX**+++****+=++*===++===+++++=++=+===++=+====+===-:......... ..     .. ....... .  ...                                             
******+**X%XXXXX%X%%X*+++*+++****+++++*+*X*+++*XXX*+***X*+=+*+==++====+*+++================-::....   .....             ...........                                             
*X***XX%%X*X%%****X%%X**+*+*++**X%+++*+++****++***XX*+**X+++*+=+=++=+===++*++++=====+++=--:.......       ...           ...........                                             
******X***X****XXX*X%%XX***X****X****+++++**X******X****X++++++*==+======++++X*-++=-==-:...............  ...           ...........                                             
XXX*******X*X*XX*XXX%%+**X******X***X**++++*****X*XX***XX*+****+++++++===+===*--==:-::...  .                                                                                   
**+**********XX****X%*++****XXXXX**X+%*++++**+****XXX++*X*++*XX***+**+*++++==*.=:..........                                                                                    
X%****XXXX******X*XXX*++++***X***XX*****++++*******XX*+****++*XX*++++++*+*X=*:.=.......   ..                                                                                   
****X*X**XX******XXXXX+++++******+*X*****++++**+++**X*+***+++**X**====+++++*:..:.......                                                                                        
*******X***XXXXXX*XXXX++*+++***X**++***XXX*+++****+****++***+****X+===++=--............                                                                                        
******%%X*X****XX*X*%X*=*++*******++**+***XX**++X******X******XX***++-.................                                                                                        
XX%X*XXX***X*XX*X*XXXX**+**++++**X*+***+++*************XXXX**XX*+**-........                                                                                                   
**XXXXX***XXX***XX%XX*X*+****++++*X*+*X*+++**+**X*X**+******++*+==...........                                                                                                  
*XXXXXXXXX%XXXXXX%@@@%%X*****++++*+**X+*****+*****+****+**X*++...............                                                                                                  
X*XXXXXX*X%*XXX***X*X%%X*+*****++++*+******XX*+***+++++++++*+...............                                                                                                   
X*XXXXXXX*X*XX****XXX%%X+++++*X****+++*+++**********+++++++=.................                                                                                                  
XX**XXXXXXXXX****XX%X%***+++*++*+***++***+++++***+++******=..................                                                                                                  
XX*X*XXXX*********XX%%*+*+++++++++*********++*++***++*++**-.......                                                                                                             
**XX*X******X**XXXXX%X+*X*+*****+++**********************+........                                                                                                             
X**X%*X*****X*%%%%XX%*=XXXX**********++++++***+++++++++*+-.......                                                                                                              
*X**XXX%%%%%%XXXX%%%X++********+++*****++++++++*******+++:.......                                                                                                              
X*XX*********XXXX%%%*+XX**+*****+++++++**+++++++****+++*=........                                                                                                              
XX*XXXX**X%%XXXXX%%X+XXXXX*******+++++++++++*******++*+=........."""

print("You wake up in a large bird cage over lava")
firstpick = split("Go down hamster tube slide", "Jump across the glass bridge(1 in 33554432 success)")                        #this code forms the main structure/plot of the game and was a collaboration between james and cairo
frstchoice = int(input("1 or 2:\n"))
if frstchoice == 1:
  print("You decide to go down the hamster tube slide.")                                                                      #these first 39 lines were written by cairo
  slingshot = input("At the bottom, you see a tiny slingshot and a bag of infinite yummy seeds. Do you pick it up?\n").capitalize()
  if slingshot == "Yes":
      print("You now have a slingshot!")
  else:
      print("You decide to leave it behind.")
  print("Continuing on, you come along another split decision")
  secondpick = split("Unlock sewer gate", "Walk along the side of the dungeon")
  scndchoice = int(input("1 or 2:\n"))
  if scndchoice == 1:
      print("You decide to go through the sewer gate, after you complete the riddle to unlock it first.")
      puzzle1 = ("Yes")
      print("Time flies like an arrow, and fruit flies like a...")
      while puzzle1 == "Yes":
          solution = input("What is the answer?: ").capitalize()
          if solution == "Banana":
              puzzle1 = ("No")
              print("Congratulations! You did it! You can now enter into the sewer. Look out for Ninja Turtles! If you have any pizza on you, it would be a good idea to discard it.")
              thirdpick = split("Go down the flame-lit tunnel", "Crawl through the grate system")
              thrdchoice = int(input("1 or 2:\n"))
              if thrdchoice == 1:
                  print("You decide to go down the flame lit tunnel. You see a figure by the fire. It is tall and skinny, but you can only see the silouette. It turns its head at you, revealing luminous red eyes.\nIt comes after you!")
                  hatman = battle("Hat Man", "swing", "Head", "legs")
                  print("The Hat Man dropped a sword.")
                  print("The ground begins to shake. You see the wall collapse and a giant Dragon Bird emerges through the wall! It is not happy that you defeated the Hat Man!")
                  finalpick = split("Attack the Dragon Bird", "Try to befriend it")
                  lastchoice = int(input("1 or 2:\n"))
                  if lastchoice == 1:
                    print("You Decide to attack the Dragon Bird!")
                    finalbattle = battle("Dragon Bird", "stab", "Head", "Eyes")
                    print(sneakend)
                  else:
                    print("You decide that you want to befriend the Dragon Bird!")
                    friends = input("How will you go about doing that?(Only the action)\n")
                    print(f"You decide that by {friends}, you will befriend the bird! At first the Dragon Bird is unsure, but it ends up being friends with you!")
                    print(befriend)
                    
              else:      #these next 31 lines were written by james
                  print("Deciding that the flame is a little suspicious, you decide to crawl into the sewer grate and sneak below the sewer.\nYou close the sewer grate with a slam. A sound of surprise comes from near the fire, followed by a noise like a snake hissing, and then wet footsteps coming in your direction.")
                  fourthchoice = split("Solve the puzzle and continue under the sewer", "Hide quietly and wait for the entity to pass")
                  frthchoice = int(input("1 or 2:\n"))
                  if frthchoice == 1:
                      print("You decide that this entity will be anything but friendly, and that solving the puzzle will be best for you.")
                      puzzle2 = "Yes"
                      while puzzle2 == "Yes":
                       result = input("I am something people either celebrate or resist. I change people's thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?\n").capitalize()
                       if result == "Age":
                           puzzle2 = 0
                           print("The door opens.")
                           break
                       else:
                           print(f"That is incorrect.")
                      print("You feel like something is lurking behind you...")
                      hatman = battle("Hat Man", "swing", "Head", "legs")
                      print("You feel the ground shaking. A chunk of the wall breaks out, revealing an exit.")
                      fifthchoice = split("Stay in cover where you are", "Try to run and escape")
                      ffthpick = int(input("1 or 2:\n"))
                      if ffthpick == 1:
                        print("You decide that if you go out, a chunk of this place will fall on your head. You wait in the grate until the shaking stops.\nYou try to open the grate door, but something fell on it, making it to oheavy to open.")
                        print(dedend)
                      else:
                        print("You decide to run run out of the hole that just broke in the wall.")
                        print(sneakend)
                         
                  else:
                      print("You decide that this entity is not intelligent enough to find you in the grate and will pass overhead.\nSuddenly, you see the creature to be a very tall and lanky shadow figure with luminous red eyes. It wraps its arm tentacles around you and you start to choke.")
                      choke = random.randint(1,10)
                      chokblok = int(input("Pick a number between 1 and 10 to see if you can survive this creature's attack."))
                      if chokblok == choke:
                          print("You managed to block the creature's attack, and in the process stun it! Deciding that you may no longer go back through the way you came, you continue on, Eventually finding an escape hatch.")
                          print(sneakend)
                      else:
                          print("The creature's grip strengthens. In one last desperate attempt to escape, you try to kick it in the leg, but you miss!")
                          print(dedend)
                          print(dedend)
                   
          else:                                #these 27 lines were written by cairo
              print("No, that is incorrect.")
   
  else:
      print("Because the sewer sounds a little unsafe(or nasty), you decide to keep walking alongside the dungeon. You hear noises coming from each of the cells in the dungeon.")
      scndpick = split("Check out the other dungeon cells", "Walk past them")
      secondchoice = int(input("1 or 2:\n"))
      if secondchoice == 1:
          print("You decide that you want to see what is in the other cells of this dungeon. You walk by the cells and see nothing in them. Confused, you start thinking of something.")
          thrdpick = split("Look closer at the cells", "Ignore them")
          thirdchoice = int(input("1 or 2:\n"))
          if thirdchoice == 1:
              print("A blurry figure seems to materialize. It looks like an old man in chains looking away from you.\n")
              print("You feel a chilly breeze blow through you...")
              ghostman = battle("Prisoner's Ghost", "throw a punch", "Head", "Torso")
              print("The Prisoner's Ghost seems to evaporate, and it drops a block.")
              blok = input("Do you pick it up?\n").capitalize()
              if blok == "Yes":
                print("You now have a block!")
              else:
                print("You leave the block behind.")
              print("A door with a puzzle stands in front of you.")
              lastpick = split("Complete the puzzle","Find a puzzle-free way")
              lstpick = int(input("1 or 2:\n"))
              if lstpick == 1:
                  print("You decide that you want to do the puzzle.")
                  code = input("What is %@$#  + (*#&%\n").capitalize()
                  if code == "No":
                      print("You are correct, this is not a thing. A door opens up to the surface world.")
                      print(sneakend)
                  elif code == "Yes":
                      print("Your skill is beyond power if that means anything to you. You never open the door, and end up living in the dungeon.")
                      print(dungeondweller)
                  else:
                      print("That's incorrect!")
                      print(dedend)  
              else:
                 print("You decide that a puzzle takes up too much energy.")
                 print("You notice a lever in the middle of the floor.")
                 lsa = input("Do you pull it?\n").capitalize()
                 if lsa == "Yes":
                    print("The floor starts opening up in the middle. You try to pull the lever back, but the lever snaps. You fall into the lava")
                    print(dedend)
             
          else:            # these 17 lines were written by james
              print("You decide to continue past them, and run past all the cells. After a few minutes of running, you find yourself exhausted. You also observe that you made it onto a bridge above the lava.")
              print("Something flaps above you...")
          if slingshot == "Yes":
           giantbird = battle("Dragon Bird", "fire a seed", "Head", "Wings")
          else:
           giantbird = battle("Dragon Bird", "throw a seed", "Head", "Wings")
          print("You've scared it off for now, but you have a feeling it'll return.")
          print("The bridge you are standing on starts to collapse.")
          finaldesicion = split("Try to run to the clear exit of the bridge", "Go back into the dungeon")
          fnaldesicion = int(input("1 or 2:\n"))
          if fnaldesicion == 1:
            print("You run across the falling bridge as fast as you can. Just before the last brick falls, you leap onto the ground of the exit.")
            print(sneakend)
          else:
             print("You leap back onto the safe(ish) dungeon ground just before the bridge completely collapses. The Dragon Bird returns!\nIt grabs you by its talons and flies over the lava and drops you in.")
             print(dedend)
                
      else:
          print("Deciding that it might be dangerous to check out what is in the cells, you run past all the cells.\nAfter a few minutes of running, you find yourself exhausted. You also observe that you made it onto a bridge above the lava.")
          print("Something flaps above you...")
          if slingshot == "Yes":
           giantbird = battle("Dragon Bird", "fire a seed", "Head", "Wings")
          else:
           giantbird = battle("Dragon Bird", "throw a seed", "Head", "Wings")
          print("You jump over into a sewer grate to hide from the bird possibly coming back.")
          print("You never make it out, but you start living in the sewer, forgetting to find a way out.")
          print(sewerdweller)

else:              #This last bit was written by cairo
  print("You decide to go on the glass bridge.")
  count = 0
  while count != 26:
      strong = random.randint(1,2)
      print (strong)
      panes = int(input("You are on the glass bridge. Pick 1 or 2.\n"))
      if panes == strong:
          print("You have made it to the next pane.")
          count += 1
      elif count >= 25:
        print(sneakend)
      else:
          print("You have fallen into the lava.")
          print(dedend)
          break