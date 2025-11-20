import os
import json
import csv

def main() :
    jsonList = []

    # Parcours de tous les répertoires
    for (root,dirs,files) in os.walk(os.getcwd(),topdown=True):

        # On regarde s'il y a des fichiers, puis s'ils se terminent par ".json"
        if len(files) > 0 :
            for file in files :
                if file.endswith('.json') :

                    # On ouvre le fichier, et on ajoute le contenu à notre liste
                    jsonList.append(json.load(open(root + "/" + file)))
    
    # Création du fichier .csv
    df = open('data_file.csv', 'w')

    # Création du writer
    cw = csv.writer(df)
    c = 0
    for jsonObject in jsonList :
        if c == 0 :

            # Writing headers of CSV file
            h = jsonObject.keys()
            cw.writerow(h)
            c += 1

        # Writing data of CSV file
        cw.writerow(jsonObject.values())
    df.close()

if __name__ == "__main__" :
    main()
