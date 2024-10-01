from urllib.request import urlretrieve
import requests
import traceback
import os
import sys

class UpdateCompadiblityLayers:

    def __init__(self):
        self.downloadFile(
            "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot", 
            "./plugins/Geyser-Spigot.jar"
        )
        self.downloadFile(
            "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot", 
            "./plugins/Floodgate-Spigot.jar"
        )
        self.downloadFile(
            self.getLatestURL("https://api.github.com/repos/ViaVersion/ViaVersion/releases/latest"),
            "./plugins/ViaVersion.jar"
        )

    def getLatestURL(self, url):
        try:
            response = requests.get(url).json()
            print("[INFO] Connected to Github API.")
            return response["assets"][0]["browser_download_url"]
        except:
            print("[ERROR] Github API Call Failed, Update Aborted.")
            return None, None

    def downloadFile(self, url, file_path):
        filename = os.path.basename(file_path)
        try:
            urlretrieve(url, file_path)
            print(f"[INFO] Updated Package {filename}.")
            return True
        except:
            print(f"[ERROR] Download Failed, Updated of {filename} Aborted.")
            return False


if __name__ == "__main__":
    UpdateCompadiblityLayers()
