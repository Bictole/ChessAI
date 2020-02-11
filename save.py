

def save(G, linked):
    fichier = open("save_data.txt", "w")
    for i in G:
        fichier.write(str(i) + "\n")
        
    fichier.write("\n")
    
    for i in linked:
        fichier.write(str(i) + "\n")
        
    fichier.write("\n")
    
    for i in range(len(G)):
        fichier.write(str(G[i].reward) + "\n")
        
    fichier.write("\n")
    
    fichier.close()


def recup():
    fichier = open("save_data.txt", "r")
    F = fichier.read()
    G = []
    linked = []
    qualiState = []
    
    a = 0
    for i in F:
        if(i == "\n"):
            a += 1
            
        if(a == 0):
            G.append(i)
        if(a == 1):
            linked.append(i)
        if(a == 2):
            qualiState.append(i)
            
    return(G, linked, qualiState)
