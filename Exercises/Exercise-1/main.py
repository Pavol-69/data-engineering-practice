import requests
import os
import os.path

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # Création du dossier downloads s'il n'existe pas
    path = "downloads"
    if os.path.exists(path) :
        print("Chemin" , path, "existe déjà")
    else:
        os.mkdir(path)
        print("Chemin" , path, "créé")

    # Téléchargement de chacun des fichiers
    for i in range(len(download_uris)) :
        response = requests.get(download_uris[i])
        name = download_uris[i].split("/")[-1]
        with open(path + "/" + name, "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    main()
