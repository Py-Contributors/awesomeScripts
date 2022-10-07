import requests

logo = '''
╔═══╗────────────╔╗──╔╗
║╔═╗║────────────║╚╗╔╝║
║║─╚╬══╦═╦══╦═╗╔═╩╗║║╔╬═╦╗╔╦══╗
║║─╔╣╔╗║╔╣╔╗║╔╗╣╔╗║╚╝╠╣╔╣║║║══╣
║╚═╝║╚╝║║║╚╝║║║║╔╗╠╗╔╣║║║╚╝╠══║
╚═══╩══╩╝╚══╩╝╚╩╝╚╝╚╝╚╩╝╚══╩══╝
╔═══╗╔╗───╔╗
║╔═╗╠╝╚╗─╔╝╚╗
║╚══╬╗╔╬═╩╗╔╬══╗
╚══╗║║║║╔╗║║║══╣
║╚═╝║║╚╣╔╗║╚╬══║
╚═══╝╚═╩╝╚╩═╩══╝ @iamlordutkarsh'''

print(logo)
print("\n")
print("Credit :- * Utkarsh \n          * CyberBoySumanjay")
print("\n")
country = input("Enter Country Name --> ")

url = f"https://api.sumanjay.cf/covid/?country={country}"

result = requests.get(url).json()

test = result["countrydata"]
print(" ")
print("Total Active Cases -->", test[0]['total_active_cases'])
print(" ")
print("Rank -->", test[0]['total_danger_rank'])
print(" ")
print("New Cases Today -->", test[0]['total_new_cases_today'])
print(" ")
print("Death Today -->", test[0]['total_new_deaths_today'])
print(" ")
print("Total Recovered -->", test[0]['total_recovered'])
print(" ")
print("Total Serious Cases -->", test[0]['total_serious_cases'])
