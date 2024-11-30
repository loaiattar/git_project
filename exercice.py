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
