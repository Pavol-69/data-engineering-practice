import requests
import pandas
import os

def createDownload() :
    # Création du dossier downloads s'il n'existe pas
    path = "downloads"
    if os.path.exists(path) :
        print("Chemin" , path, "existe déjà")
    else:
        os.mkdir(path)
        print("Chemin" , path, "créé")

def downloadInFolder(url, folder) :
    response = requests.get(url)
    name = url.split("/")[-1]
    with open(folder + "/" + name, "wb") as f:
        f.write(response.content)
    print("Téléchargement réussi")


def main():

    # Récupération du HTML
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    html = response = requests.get(url).text

    # Récupération du fichier que l'on souhaite
    time = "2024-01-19 15:18"
    data = html.split("<tbody>")[1]
    data = data.split("</tbody>")[0]
    data = data.split("<tr>")
    line = ""
    for i in range(len(data)) :
        if time in data[i] :
            line = data[i]
            break
    file = line.split(">")[2].split("<")[0]

    # Création dossier downloads
    createDownload()

    # Téléchargement dans downloads
    folder = "downloads"
    downloadInFolder(url + file, folder)

    # Ouverture avec Pandas
    dataPandas = pandas.read_csv(folder + "/" + file)
    print("HourlyDryBulbTemperature : " + str(dataPandas["HourlyDryBulbTemperature"].idxmax()))

if __name__ == "__main__":
    main()
