import pandas as pd

COUNTRY_NAME="India"
# don't update Andhra Pradesh state (No Telangana AP diff)
STATES = { "tn": "Tamilnadu", "kl": "Kerala", "ka": "Karnataka", "mh": "Maharashtra", "mp": "Madhya Pradesh", "ch": "Chattissgargh", "jk": "Jharkhand", "up": "Uttar Pradesh", "bi": "Bihar", "gu": "Gujarat", "ra": "Rajastan", "wb": "West Bengal", "uk": "Uttarkhand", "ha": "Haryana", "od": "Odisha", "cd": "Chandigarh", "pud": "Puducherry", "sik": "Sikkim", "tri": "Tripura", "nag": "Nagaland", "miz": "Mizarom", "meg": "Meghalaya", "ma": "Manipur", "go": "Goa", "del": "Delhi", "arp": "Arunachal Pradesh", "as": "Assam" }

def prep_census_data(csvFilePath, stateName):
    df = pd.read_csv(csvFilePath)

    if "Address" not in df.columns:
        print("adding address column")
        df["Address"] = ""
        df.to_csv(csvFilePath, index=False)
    for index, row in df.iterrows():
        address = ""
        address += str(row['Name']).strip() + "," + str(row['SDTName']).strip() + "," + str(row['DTName']).strip() + "," + stateName + "," + COUNTRY_NAME
        print(address)
        df.loc[index, 'Address'] = address
    df.to_csv(csvFilePath, index=False)
csvFilePath = r'raw/as.csv'
stateName = "Assam"

prep_census_data(csvFilePath, stateName)