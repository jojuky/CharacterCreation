#Base du perso
xp = 0
name = input("What is your name: ") 
print("-----")
print("hello "+name)
print("-----")
age = input("What is your Age: ")
print("-----")
print("so your name is "+name + " and you are "+age)
print("-----")

#########

# Vérification du rôle
valid_roles = ["Mage", "Warrior", "Thief"]
role = ""

# Demande du rôle jusqu'à ce que l'utilisateur choisisse un rôle valide
while role not in valid_roles:
    role = input("Choose your class: Mage, Warrior, Thief: ")
    if role not in valid_roles:
        print("-----")
        print("Invalid class. Please choose either Mage, Warrior, or Thief.")
        print("-----")

#########

if role == "Mage":
    hp = 100 
    defense = 90
    atk = 70
    xp = xp + 30
    print("You are now a Mysterious Mage and You have 100 hp + ", xp , "!")
    
    # Vérification du choix d'arme
    weapon = 0
    while weapon not in [1, 2, 3]:
        weapon = int(input("Choose your weapon: 1 White wood staff - 2 Necromantic Staff - 3 Fire grimoire: "))
        if weapon not in [1, 2, 3]:
            print("-----")
            print("Invalid weapon choice. Please choose a number between 1 and 3.")
            print("-----")
    
    match weapon:
        case 1:
            print("you are now an all-rounded mage with both defensive skills and offensive skills! ")
            weapon =  ("White Wood Staff")
            subrole = ("Spell Master")
            mana = 250
            atk = atk + 30
            defense = defense + 30
        case 2:
            print("you are now a Curse Master and you can now raise your own army of undeads!")
            weapon =  ("Necromantic Staff")
            subrole = ("Curse Master")
            mana = 200
            atk = atk - 20
        case 3:
            print("you are now a powerful Spell Caster and you can set Hearts Ablaze!")
            weapon =  ("Fire Grimoire")
            subrole = ("Fire Apprentice")
            mana = 230
            atk = atk + 50

if role == "Warrior":
    hp = 150
    defense = 100
    atk = 130
    xp = xp + 30
    print("You are now a Powerfull Warrior and you have 150 hp + ", xp , "!")
    
    # Vérification du choix d'arme
    weapon = 0
    while weapon not in [1, 2, 3]:
        weapon = int(input("Choose your weapon: 1 Sword - 2 War Axe - 3 Hammer And Shield: "))
        if weapon not in [1, 2, 3]:
            print("-----")
            print("Invalid weapon choice. Please choose a number between 1 and 3.")
            print ("-----")
    
    match weapon:
        case 1:
            print("You are now an All-rounded Warrior, You're agile, strong, and you cast spells!")
            weapon =  ("Sword")
            subrole = ("Hero")
            mana = 110
        case 2:
            print("you are now a GREAT Brute, you only have muscle strong!")
            weapon =  ("War Axe")
            subrole = ("Brute")
            mana = 0
            atk = atk + 100
            defense = defense - 30
        case 3:
            print("you are now a Paladin, you're now the final wall between you and your team!")
            weapon =  ("Hammer And Shield")
            subrole = ("Paladin")
            mana = 150
            atk = atk - 30
            defense = atk +  100

if role == "Thief":

    hp = 120
    defense = 70
    atk = 120
    xp = xp + 30
    print("You are now a Stealthy Thief and you have 120 hp + ", xp , "!")

        # Vérification du choix d'arme
    weapon = 0
    while weapon not in [1, 2, 3]:
        weapon = int(input("Choose your weapon: 1 Dagger - 2 Gauntlets - 3 Bow And Arrows "))
        if weapon not in [1, 2, 3]:
            print("-----")
            print("Invalid weapon choice. Please choose a number between 1 and 3.")
            print ("-----")

  
    match weapon:
        case 1:
            print("You are now a Great Ghost, enemies won't even see you before you strike them down!")
            weapon =  ("Dagger")
            subrole = ("Ghost")
            mana = 100
            atk = atk + 30
        case 2:
            print("You are now a Martial Artist, Hands-to-hands combat has no secrets for you!")
            weapon =  ("Gauntlets")
            subrole = ("Martial Fighter")
            mana = 80
            atk = atk + 50
        case 3:
            print("you are now an Archer hiding in the shadows, enemies won't see your arrow coming!")
            weapon =  ("Bow And Arrows")
            subrole = ("Archer")
            mana = 120
            atk = atk + 20




#########

print(f"""
-----
🧙 Character Sheet 🛡️
Name: {name}
Age: {age}
Role: {role} - {subrole}
Weapon: {weapon}
HP: {hp}
Defense: {defense}
Attack: {atk}
Mana: {mana}
xp :
-----
""")

print ("==============")
print ("A monster Monster is Approaching.")
print ("==============")
monsterhp = 100
monsteratk = 30
monsterdef= 100

# Combat
while hp > 0 or monsterhp > 0 :
    choice = int(input("choose an option. 1 attack - 2 magic - 3 heal "))
    print("------")

    match choice :
        case 1 :
            if atk > monsterdef:
                damage = monsterhp - atk
                monsterhp = monsterhp - damage
                damage = 0
                print("------")
                print(f"the monster have ", monsterhp, "health left")
                print("------")

            if atk < monsterdef:
                damage = monsterdef - atk
                monsterhp = monsterhp - damage
                damage = 0
                print("------")
                print(f"the monster have ", monsterhp, "health left")
                print("------")
### vsy flemme de faire un sort pour toute les classes pour l'instant 😭
        case 2:
            manaatk = mana
            if manaatk > 0:
                manaatk = mana - atk
                damage = monsterdef - manaatk + atk
                monsterhp = monsterhp - damage
                manaatk = mana - atk
                print("------")
                print(f"the monster have ", monsterhp, "health left")
                print("------")
            if manaatk < 0:
                print("no mana left.")
        case 3:
            hp = hp + 30
            print("------")
            print(f"you now have ", hp , "health")
            print("------")
    print("the monster attack.")
    print("------")
    damage = defense - monsteratk
    hp = hp - damage
    damage = 0
    print(f"you have now ", hp ,"health left")
    print("------")



    
    if monsterhp < 0:
        print("the Monster has perished")
        xp = xp + 70
        if xp < 99:
            hp = hp = 20
            defense = defense + 20
            atk = atk + 10
            mana = mana + 10
        print(f"""
     -----
    💥Lvl up !💥
     ---
    🧙 Character Sheet 🛡️
    Name: {name}
    Age: {age}
    Role: {role} - {subrole}
    Weapon: {weapon}
    HP: {hp} ⏫
    Defense: {defense} ⏫
    Attack: {atk} ⏫
    Mana: {mana} ⏫
    xp : {xp} ⏫
    -----
""")
        break
            
    if hp < 0:
        print("gg ez you dieded 💀")
        exit()

