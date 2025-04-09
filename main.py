name = input("What is your name: ") 

print("hello "+name)

age = input("What is your Age: ")

print("so your name is "+name + " and you are "+Age)

role = int(input("Choose your clase Type the correct number for your classe    1 Mage - 2 Warrior - 3 Thief    : "))

if role == 1:
    print("You are now a Mysterious  Mage and You have 100 hp")
    weapon= int(input("now choose your weapon : 1 White wood staff - 2 Necromantique Staff - 3 Fire grimoire    : "))
    if weapon==1:
        print("you are now a all rounded mage with both defensive skills and offensive skills !")
        subrole = ("Necroman")

    if weapon==2:
        print("you are now a Curse Master and you can now raise your own army of undeads !")
        subrole = ("Curse Master")

    if weapon==3:
        print("you are now a powerfull Spell Caster and you can set Hearts Ablaze !")
        subrole = ("Fire Apprentice")


if role == 2:
    print("You are now a Powerful Warrior and you have 150 hp")
    weapon= int(input("now choose your weapon : 1 Sword - 2 War Axe - 3 Hammer And Shield"))
    if weapon==1:
        print("You are now a All rounded Warrior, You're agile,strong and you cast spell !")
        subrole = ("hero")
        
    if weapon==2:
        print("you are now a GREAT Brute, what is brain and defense.. you only have.. muscle strong.")
        subrole = ("brute")
    if weapon==3:
        print("you are now a Paladin, youre now the final wall between you and your team, you can cast spell and defend with your shield")
        subrole = ("paladin")

if role ==3:
    print("You are now a Stealhy Thief and you have 120 hp")
    weapon = int(input("now choose your weapon : 1 Dagger - 2 Gauntlets - 3 Bow and Arrows"))
    if weapon==1:
        print("You are now a Great Ghost, enemies wont even get to see you before you striker them down")
        subrole = ("Ghost")
    if weapon==2:
        print("You are now a Martial Artist, Hands to Hands combats have no Secret to you")
        subrole = ("Martial Figher")
    if weapon==3:
        print("you are now an archer hiding in the shadows , hiding in plain sight they wont see your arrow coming.")
        subrole = ("Archer")



print("You are "+ name +" you are "+ age +" you role is "+ str(role) + " and you choose the path of the "+ subrole)




      

