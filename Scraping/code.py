import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

GS_faculty_url = "https://docs.google.com/spreadsheets/d/1Otz0LtypZ5C_NEOsIuION2nL__IuE-T8iTh6NQf7-aE/edit#gid=2043681081"
df_faculty = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                   '1Otz0LtypZ5C_NEOsIuION2nL__IuE-T8iTh6NQf7-aE' +
                   '/export?gid=2043681081&format=csv',
                  )
df_faculty

faculty_names_list = df_faculty.Name.values.tolist()

faculty_URLs_list = df_faculty.Link.values.tolist()
#print(faculty_URLs_list)

len(faculty_URLs_list)
print(len(faculty_URLs_list))

faculty_bios_list = []
faculty_bios_list.clear()

bio_text = []
for faculty in faculty_URLs_list:
    #print("https://www.hks.harvard.edu" + faculty)
    result = requests.get("https://www.hks.harvard.edu" + faculty)
    c = result.content
    soup = BeautifulSoup(c)
    bio_text.clear()
    PTag = soup.find_all('p')
    len(PTag)
    for tags in PTag:
        if len(str(tags.string)) > 30:
            bio_text.append(str(tags.text.strip()))
    bio = '\n'.join(bio_text)
    if bio == "":
        bio = "No bio found."
    faculty_bios_list.append(bio)
    #print(bio)

# Save the faculty bios list to a JSON file
with open('faculty_directory.json', 'w') as f:
    json.dump(faculty_bios_list, f, indent=4, ensure_ascii=False)