#n=#of duels
#start=amount of wizards at start
#duels= wizard v wizard
#to-do
    #print number of duels
    #print each indiviual duel
    #tell which wizard won the duel
""" def wizards(n,start,duels):
    owner = start
    changed_hands= 1
    print (duels[0][0])
    if (duels [0][1]) == owner:
        owner == (duels [0][0])
        changed_hands +=1
    print (owner) """

def wizards(n,start,duels):
    owner = start
    changed_hands= 1
    for i in range (n):
        if (duels [i][1]) == owner:
            owner = (duels [i][0])
            changed_hands += 1
    print (owner, changed_hands)

wizards (4, "A", ["BA", "CB", "DA", "AZ"])