from ctypes import alignment
import urllib.parse
import requests
from tabulate import tabulate
from colorama import Fore, Style, Back

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "z1P3gykOzfNMSPTKFF9nGTmmobAG19A0"
#creates a list for the menu to be displayed
menu = [[Fore.BLUE  + Style.BRIGHT + "WELCOME TO MAPQUEST"], [Style.RESET_ALL+Fore.BLUE+"Please enter your Starting Location and Destination"],["enter " + Fore.RED +Style.BRIGHT + 'quit' +Style.RESET_ALL+ Fore.BLUE+" or " + Fore.RED + Style.BRIGHT +'q'+ Style.RESET_ALL+Fore.BLUE+" to quit program"]]
#creates lists for the measurement options
mesmenu=[[Style.RESET_ALL+Fore.CYAN+"1","2"],[Style.RESET_ALL+Fore.CYAN+Style.BRIGHT +" METRIC ","IMPERIAL"]]
mesme=[[Fore.YELLOW+Style.BRIGHT+"MEASUREMENT MENU"+Style.RESET_ALL]]


while True:
 #sets the nav list for the directions. this variable is in the loop so it can reset after a trip has finished.
 nav=[[Style.RESET_ALL+Fore.GREEN+"DIRECTIONS FOR NAVIGATION"+Style.RESET_ALL]]
 print("\n\n\n")
 #displays the menu and asks for the starting loc and destination
 print(tabulate(menu,headers="firstrow",stralign="center",tablefmt="fancy_grid"))
 orig = input(Style.RESET_ALL+Style.BRIGHT +"Starting Location: ")
 if orig == "quit" or orig == "q":
    break
 dest = input(Style.BRIGHT +"Destination: ")
 if dest == "quit" or dest == "q":
    break
 print("\n\n\n")

 #displays measurement menu and asks for 1 or 2 to select which measurement
 print(tabulate(mesme,headers="firstrow",stralign="center",tablefmt="fancy_grid"))
 print(tabulate(mesmenu,stralign="center",tablefmt="fancy_grid"))
 mes= int(input(Style.RESET_ALL+Style.BRIGHT +"ENTER 1 OR 2:"))

 #this while loop repeats itself until 1 or 2 is entered
 while mes<1 or mes>2:
    mes=int(input("INPUT NOT VALID. ENTER 1 FOR METRIC OR 2 FOR IMPERIAL MEASUREMENTS:"))
 
 url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
 print("\n\n\nURL: " + (url))
 json_data = requests.get(url).json()
 json_status = json_data["info"]["statuscode"]

 #if statement is for the metric system. all values displayed here will be in metric measurements
 if (mes==1):
    if json_status == 0:
        #this is when a route is confirmed, the code stores the infos in a list so it can be displaed in tabular form. 
        tinfo = [[Fore.MAGENTA+Style.BRIGHT+"DIRECTIONS FROM:",Style.RESET_ALL+Fore.MAGENTA+(orig) + " to " + (dest)],[Fore.MAGENTA+Style.BRIGHT+"TRIP DURATION:",Style.RESET_ALL+Fore.MAGENTA+(json_data["route"]["formattedTime"])],
        [Fore.MAGENTA+Style.BRIGHT+"TRIP DISTANCE:",Style.RESET_ALL+Fore.MAGENTA+str("{:.2f}".format((json_data["route"]["distance"])*1.61))+"km"],
        #["ESTIMATED FUEL USAGE:", str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)+" LITERS")],
        [Fore.MAGENTA+Style.BRIGHT+"STARTING COORDINATES:",Style.RESET_ALL+Fore.MAGENTA+str(json_data["route"]["boundingBox"]["lr"]["lat"])+", "+str(json_data["route"]["boundingBox"]["lr"]["lng"])],
        [Fore.MAGENTA+Style.BRIGHT+"DESTINATION COORDINATES:",Style.RESET_ALL+Fore.MAGENTA+str(json_data["route"]["boundingBox"]["ul"]["lat"])+", "+str(json_data["route"]["boundingBox"]["ul"]["lng"])]]
        print (tabulate(tinfo,tablefmt="fancy_grid"))
        #for loop stores the narratives in a list so it can be displayed in tabular form
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            nav.append([(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")])
        print(tabulate(nav,headers="firstrow",tablefmt="github"))
    #elif statements are error codes for the entries. 
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
#else statement is for the imperial system, all values displayed here will be in imperial measurements
 else:
     if json_status == 0:
      #if a route is found, the infos of the trip are stored in a list to display it in a tabular format
        tinfo = [["DIRECTIONS FROM:",(orig) + " to " + (dest)],["TRIP DURATION:",(json_data["route"]["formattedTime"])],
        ["TRIP DISTANCE:",str("{:.2f}".format((json_data["route"]["distance"]))+" miles")],
        ["ESTIMATED FUEL USAGE:", str("{:.2f}".format((json_data["route"]["fuelUsed"]))+" gallons")],
        ["STARTING COORDINATES:",str(json_data["route"]["boundingBox"]["lr"]["lat"])+", "+str(json_data["route"]["boundingBox"]["lr"]["lng"])],
        ["DESTINATION COORDINATES:",str(json_data["route"]["boundingBox"]["ul"]["lat"])+", "+str(json_data["route"]["boundingBox"]["ul"]["lng"])]]
        print (tabulate(tinfo,tablefmt="fancy_grid"))
        #for loop stores narratives in a list to be able to display it in tabular form
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            nav.append([(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)")])
        print(tabulate(nav,headers="firstrow",tablefmt="github"))
        print("=============================================\n")
        #elif statements are also error codes when there are no routes for the locations or if there is An error with the input
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
    
        
