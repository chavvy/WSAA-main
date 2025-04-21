#A program to fetch a file from a private github repository
#Replaces the text in the txt file in that repository, commits and pushes the changes

import requests
from github import Github
import json
from config import config as cfg

#API URL
url = "https://api.github.com/repos/chavvy/wsaa_a4_repo"
api_key = cfg["githubkey"]

#Github authentication
g = Github(api_key)
repo = g.get_repo("chavvy/wsaa_a4_repo")

#File info and download url
file_info = repo.get_contents("a4_base.txt")
file_dl_url = file_info.download_url

#Requesting the file content
response = requests.get(file_dl_url)
file_content = response.text

#File content and modifications
replace_content = file_content.replace("andrew", "sam")

#Updating the file back to github
github_response = repo.update_file(file_info.path, "replaced 'andrew' with 'sam' in the a4_base.txt file", replace_content, file_info.sha)

#Print the original and updated content
print("Original content:\n", file_content)
print("\nUpdated content:\n", replace_content)





