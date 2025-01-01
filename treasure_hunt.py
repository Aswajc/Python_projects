# ps.. enlarge your terminal to see the map!
print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    --- /
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/

''')
print("Welcome... Welcome..Explorer!")
print("Your mission is to find the treasure")
lake = input("You are at a cross road.where do you want to go..? type 'left' or 'right'   ")
if lake == "left" :
    print("\n")
    wait_swim = input("Ho Ho Ho..you have come to a lake.There is an island in the middle.Type 'wait' to wait for the boat or 'swim' for an action ")
    if wait_swim == "wait" :
        print("\n")
        door_color = input("You have arrived at the island unharmed.There is a house with 3 doors.'red'  'yellow' and 'blue' .which door you want to open?")
        if door_color == "red" :
            print("oops.You have entered a room full of beasts.game over!")
        elif door_color == "blue" :
            print("oooh noo.The room full of fire.You are dead.")    
        elif door_color == "yellow" : 
            print("Yaay...you got the tresure..Enjooyyy")
        else :
            print("you fool.you typed an invalid door.")
        
    else :
        print("Game over...#the crocodiles got their dinner")
else :
    print("Game Over.. #oops..you are lost in the jungle")        