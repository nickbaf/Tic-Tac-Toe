

def check(pin):
    emp=[0 for i in range(9)]
    if(counter(pin)==0):
        return -1
    for i in range(0,7,3):
        if pin[i]==pin[i+1]==pin[i+2*1]:
            if pin[i]=='O':
                return 1 #Νίκησε ο παίκτης
            elif pin[i]=='X':
                return 0 #Νίκησε το CPU
    for i in range(3):
        if pin[i]==pin[i+3]==pin[i+2*3]:
            if pin[i]=='O':
                return 1
            elif pin[i]=='X':
                return 0
    if pin[0]==pin[4]==pin[8]:
        if pin[0]=='O':
            return 1
        elif pin[0]=='X':
            return 0
    if pin[2]==pin[4]==pin[6]:
        if pin[2]=='O':
            return 1
        elif pin[2]=='X':
            return 0
    return -2

def display(pin):
     print()
     for i in range(3):
        print(pin[0+i*3],pin[1+i*3],pin[2+i*3])
     print()



def empty(pin,emp): #Βρίσκει πόσες kai poies θέσεις είναι κενές
    count=0
    k=0
    for i in range(9):
        if pin[i]=='_':
          #  print(i)
            emp[k]=i+1
            k=k+1
            count=count+1
    
    return count,emp

def counter(pin): #Βρίσκει πόσες θέσεις είναι κενές
    count=0
    for i in range(9):
        if pin[i]=='_':
            count=count+1
    
    return count







def cpu(pin):
    emp=[0 for i in range(9)]
    choices=empty(pin,emp) #Βρίσκω πόσες θέσεις είναι άδειες, τόσες θα είναι και οι επιλεγμένες κινησεις που μπορώ να κάνω
    ranks=[[-1,0] for i in range(choices[0])]
    m=-10
    p=-1;
    for i in range(choices[0]):
        temp=copier(pin)
        temp[choices[1][i]-1]='X'
        ranks[i][1]=makeRank(temp)
        print(choices[1][i]-1,end=':') #Αυτες οι 2 print τυπώνουν κάθε θέση στη οποία μπορεί να παίξει ο υπολογιστής και το πόσο καλή είναι η λύση αυτή
        print(ranks[i][1])
        if ranks[i][1]>m:
            m=ranks[i][1]
            p=choices[1][i]-1
        ranks[i][0]=choices[1][i]-1
    
    if(p==-1): #Εάν δεν υπάρχει καμία λύση που μπορεί να κάνει ο υπολογιστής στείλε μήνυμα οτι έχασε.
        return 1
    else:
        pin[p]='X'
        #print('--------')
    return -100
    



def copier(pin): #Αντιγράφη πίνακα με όχι και τόσο έξυπνο τρόπο
    temp=['_' for i in range(9)] 
    for i in range(9):
        if pin[i]=='O':
            temp[i]='O'
        elif pin[i]=='_':
            temp[i]='_'
        else:
            temp[i]='X'
    return temp



def makeRank(temp):
    x_1=0
    x_2=0
    o_1=0
    o_2=0
     #ελεγχος γραμμών
    for i in range(0,7,3):
        o=0
        x=0
        for j in range(3):
           if temp[i+j]=='O' :
               o=o+1
           elif temp[i+j]=='X':
               x=x+1
        if x==1:
            if o==0:
               x_1=x_1+1
        if x==2:
            if o==0:
                x_2=x_2+1
        if o==1:
            if x==0:
               o_1=o_1+1
        if o==2:
            if x==0:
                o_2=o_2+1
        if x==3:
            return 100
     #ελεγχος στυλών
    for i in range(3):
        o=0
        x=0
        for j in range(0,7,3):
           if temp[i+j]=='O' :
               o=o+1
           elif temp[i+j]=='X':
               x=x+1



        if x==1:
            if o==0:
               x_1=x_1+1
        if x==2:
            if o==0:
                x_2=x_2+1
        if o==1:
            if x==0:
               o_1=o_1+1
        if o==2:
            if x==0:
                o_2=o_2+1
        if x==3:
            return 100
    #ελεγχος διαγωνίου
    o=0
    x=0
    for j in range(0,8,4):
           if temp[j]=='O' :
               o=o+1
           elif temp[j]=='X':
               x=x+1
    if x==1:
        if o==0:
            x_1=x_1+1
    if x==2:
        if o==0:
             x_2=x_2+1
    if o==1:
        if x==0:
           o_1=o_1+1
    if o==2:
        if x==0:
            o_2=o_2+1
    if x==3:
        return 100       

 #ελεγχος διαγωνίου
    o=0
    x=0
    for j in range(2,6,2):
           if temp[j]=='O' :
               o=o+1
           elif temp[j]=='X':
               x=x+1
    if x==1:
        if o==0:
            x_1=x_1+1
    if x==2:
        if o==0:
             x_2=x_2+1
    if o==1:
        if x==0:
           o_1=o_1+1
    if o==2:
        if x==0:
            o_2=o_2+1
    if x==3:
        return 100




    #print(x_1,x_2,o_1,o_2,end=" ")
    if(o_2>=1):      #εαν υπάρχει πιθανότητα για τρίλιζα
        return -100
    else:
        return 3*x_2+x_1-(3*o_2+o_1)


#############################################################################     
pin = ['_' for i in range(9)] 

game=True

while game:
    # Τρίλιζα
    display(pin)
    # Κίνηση Παίκτη 'Ο'
    try:
        x = int(input('Παίξε (1-9): '))-1
    except BaseException:
        print("Όπς...Λάθος εισαγωγή δεδομένων...ξαναπροσπάθησε")
        continue
    if pin[x] == '_':
        pin[x]='O'
    else:
        print('Λάθος Κίνηση. Ξαναπαίξε!')
        continue

    # Κίνηση Υπολογιστή 'Χ'
    if(cpu(pin)==1 and counter(pin)):
        print('Νίκησε ο Παίκτης!')
        display(pin)
        print('-----END-----')
        break
    
    # Έλεγχος αν τελειωσε παιχνίδι
    c=check(pin)
    if(c==1):
        print('Νίκησε ο Παίκτης!')
        display(pin)
        print('-----END-----')
        break
    elif(c==0):
        print('Νίκησε το CPU')
        display(pin)
        print('-----END-----')
        break
    elif(c==-1):
        print('Ισοπαλία')
        display(pin)
        print('-----END-----')
        break
        continue
    
    


