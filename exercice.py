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
