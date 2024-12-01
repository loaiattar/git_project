 Liste de todos initiale, chaque todo est un dictionnaire avec un titre et un statut
todos = []

# Fonction pour lister les todos avec leur statut
def lister_todos():
    if not todos:
        print("Aucun todo à afficher.")
        return
    print("\n==== Liste des todos ====")
    for index, todo in enumerate(todos, 1):
        print(f"{index}: {todo['titre']} - Statut: {todo['statut']}")
    print("=========================")

# Fonction pour créer un todo avec statut "À faire"
def creer_todo():
    titre = input("Entrez le titre du todo: ")
    todo = {
        'titre': titre,
        'statut': 'À faire'  # Par défaut, le statut est "À faire"
    }
    todos.append(todo)
    print(f"Todo '{titre}' créé avec le statut 'À faire'..")

# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    lister_todos()
    if not todos:
        print("Aucun todo à modifier.")
        return
    
    try:
        choix = int(input("Entrez le numéro du todo à modifier (0 pour annuler): "))
        if choix == 0:
            return
        
        todo = todos[choix - 1]
        if todo['statut'] == 'À faire':
            todo['statut'] = 'Fait'
            print(f"Le todo '{todo['titre']}' est maintenant marqué comme 'Fait'.")
        elif todo['statut'] == 'Fait':
            # correction l'erreur :
            todo['statut'] = 'À faire'  # Provoque un comportement normal
            print(f"Le todo '{todo['titre']}' est maintenant marqué comme 'À faire'.") #correction de status
    except (ValueError, IndexError):
        print("Choix invalide, veuillez entrer un numéro valide.")

# Fonction pour supprimer un todo
def supprimer_todo():
    lister_todos()
    if not todos:
        print("Aucun todo à supprimer.")
        return
    
    try:
        choix = int(input("Entrez le numéro du todo à supprimer (0 pour annuler): "))
        if choix == 0:
            return
        
        todo = todos.pop(choix - 1)
        print(f"Le todo '{todo['titre']}' a été supprimé.")
    except (ValueError, IndexError):
        print("Choix invalide, veuillez entrer un numéro valide.")

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')
    
    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')
