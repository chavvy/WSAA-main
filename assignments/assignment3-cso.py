#A program that retrieves the dataset for the "exchequer account(historical series)" from cso.ie
import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def get_cso_data():
    response = requests.get(url)

    if response.status_code == 200:
        with open("cso.json", "w") as data:
            data.write(response.text)
        print("Data has been saved to cso.json.")
    else:
        print(f"Error retrieving data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_cso_data()