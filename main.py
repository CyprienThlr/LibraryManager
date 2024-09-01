import sqlite3

class Book:

    @staticmethod
    def add_book(title, author, genre):
        conn = sqlite3.connect('LibraryManager.db')
        cursor = conn.cursor()

        cursor.execute('''
            insert into books (title, author, genre)
            values (?, ?, ?)
        ''', (title, author, genre))
        
        conn.commit()
        conn.close()

        print(f"Le livre {title} par {author} a été ajouté avec succès.")

def main():
    print("Commandes :")
    print("1 : ajouter un livre")
    print("2 : ajouter un auteur")
    print("3 : afficher les details d'un livre")
    chose = input("Saisissez une commande : ")

    if int(chose) == 1 :
        title = input("Entrez le titre du livre à ajouter : ")
        author = input("Entrez le nom de l'auteur : ")
        genre = input("Entrez le genre du livre : ")
        Book.add_book(title, author, genre)

if __name__ == "__main__":
    main()
