import requests
import json
from datetime import datetime
import os


url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
market = 'classic'
iso_date = datetime.today().strftime('%Y-%m-%d')
federation = 'UEFA'
filename = 'match.txt'


#Check if output file already exists and deletes it
if os.path.exists(filename):
	os.remove(filename)


#Build the query string to fetch API
querystring = {"matket":market,"iso_date":iso_date,"federation":federation}
headers = {
	"X-RapidAPI-Key": "<type your Rapid API Key here>",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

#Create the response file and parse it to JSON
response = requests.get(url, headers=headers, params=querystring)
response = response.json()
i = 1

#Open output file to write football predictions of today
with open(filename,'a') as outfile:
        #Write a header with today's date
        outfile.write("FOOTBALL FIXTURES OF TODAY: " + iso_date + "\n\n")
        for row in response['data']:
                prediction = row['competition_cluster'] + '-' + row['competition_name'] + ': ' \
					 + row['home_team'] + "-" + row['away_team'] + ":" + row['prediction']
                i+=1
                outfile.write(prediction + "\n")
