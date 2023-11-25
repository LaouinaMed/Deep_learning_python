#Variables

def function():
   note1 = int(input("Entrer la 1er note : "))
   note2 = int(input("Entrer la 2eme note : "))
   note3 = int(input("Entrer la 3eme note : "))
   result = (note1+note2+note3) / note3
   print("resultat moyen : ", int(result) )
    
def function2():
    passe = input("Entrer votre mot de passe : ")
    if len(passe) >= 12 :
        print("password is good")
    elif len(passe) < 12 and len(passe) >= 8 :
        print("password is not good")
    else:
        print("password error")

def function3():
    players = ["med","basma", "badr"]
    print(players[0])
    players.insert(2, "hello")
    print(players)
    
    print(players[2:4])
    players[2:4] = ["Paul" ,"Jack"]
    players.append(2)
    players.extend([5,3,4])
    players.pop(1)
    players.remove("med")
    print(players)
    
    
    textz = input("Entrer une chaine de la forme (email-username-tele) : ").split("-")
    print(textz)
def function4():   
    for num in range(1,10):
        print("num : ",num)
        
    blackList = ["simed@gmail.com"]
    emails = ["simed@gmail.com","hello@gmail.com","chaw@gmail.com"]
    for email in emails:
        if(email in blackList):
            print('email interdit !!!!')
            break
        print("Email envoyé : ",email)  
        
"""
        
class Player:
    
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur : ",pseudo)

    def get_pseudo(self):
        return self.pseudo
        
player1 = Player("moha", 50, 5)
print(player1.get_pseudo())

"""

eleves = {
    'Paul':12,
    'Camille':8,
    'Theo':17
}

print(eleves.get('Camille','Prenom'))

for eleve , moyenne in eleves.items():
    print(f"La moyenne de {eleve} est de {moyenne}")
    
for element in range(10,-10,-1):
    print(element)
    
liste1 = [1,2,3,4]

tuple1 = (1,2,3,4)

print(liste1[0:3])
print(liste1[3:])
print(liste1[:4:2])
print(liste1[::2])

liste1.append("hello")

print(liste1)

liste1.insert(2,'madrid')
print(liste1)

liste2 = ["xx","yy"]

liste1.extend(liste2)
print(liste1)

print(len(liste1))
liste2.sort(reverse=True)
print(liste2)


print(liste1.count(1))


if 1 in liste1:
    print("oui")
else:
    print("non")
