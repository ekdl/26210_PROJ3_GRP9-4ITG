import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "z1P3gykOzfNMSPTKFF9nGTmmobAG19A0"

while True:

 orig = input("Starting Location: ")
 if orig == "quit" or orig == "q":
    break
 dest = input("Destination: ")
 if dest == "quit" or dest == "q":
    break
 mes= int(input("ENTER 1 FOR METRIC OR 2 FOR IMPERIAL MEASUREMENTS:"))
 while mes<1 or mes>2:
    mes=int(input("INPUT NOT VALID. ENTER 1 FOR METRIC OR 2 FOR IMPERIAL MEASUREMENTS:"))
 
 url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
 print("URL: " + (url))
 json_data = requests.get(url).json()
 json_status = json_data["info"]["statuscode"]
 
 if (mes==1):
    if json_status == 0:
        print("=============================================\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************\n")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
 else:
     if json_status == 0:
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Miles: " + str("{:.2f}".format((json_data["route"]["distance"]))))
        print("Fuel Used (gal): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]))))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)"))
            print("=============================================\n")
     elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
     elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
     else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
    
        
