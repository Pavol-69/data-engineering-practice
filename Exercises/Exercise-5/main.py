import psycopg2
import csv
import os

def main() :
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)

    sqlScript = []
    
    # Parcours de tous les fichiers présents dans data
    # On sait que ce sont tous des .csv, donc on vérifie pas
    for filename in os.listdir(os.getcwd() + "/data"):

        # Lecture du fichier .csv
        with open("data/" + filename, mode ='r')as file:
            csvFile = csv.reader(file)
            n = 0

            # Parcours de chaque ligne
            for line in csvFile:
                scriptLine = ""
                table = filename.replace(".csv", "")

                # Si c'est la première ligne, on crée la table, en complétant une string au fur et à mesure
                if n == 0 :
                    scriptLine = "CREATE TABLE " + table + " ("

                    # Parcours de chaque élément de l'entête
                    for i, elm in enumerate(line) :
                        if i > 0 :
                            scriptLine = scriptLine + ", "
                        scriptLine = scriptLine + elm

                        # Définition du type de variable
                        if "id" in elm or "code" in elm :
                            scriptLine = scriptLine + " INT"
                        elif "date" in elm :
                            scriptLine = scriptLine + " DATE"
                        else :
                            scriptLine = scriptLine + " VARCHAR(255)"
                else :
                    # Ajout des différents éléments à la table
                    scriptLine = "INSERT INTO " + table + " VALUES ("
                    for i, elm in enumerate(line) :
                        if i > 0 :
                            scriptLine = scriptLine + ", "
                        scriptLine = scriptLine + elm

                # Fermeture de la ligne
                n = n + 1
                scriptLine = scriptLine + ");"

                # Ajout de la ligne de commande au script général
                sqlScript.append(scriptLine)
    print(sqlScript)

    cur = conn.cursor()


if __name__ == "__main__" :
    main()
