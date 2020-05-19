
class Main:
        def __init__(self):
                self.country = 'https://api.kawalcorona.com/{}'
      
                while True:
                        self.menu()
        def clear(self):
                os.system('clear')
                print('\n\n\t[ COVID-19 GLOBAL case by sOlrac . ]\n')
        def help(self):
                print("\n\t         [ INFORMATION ]")
                print("    Command                      Description ")
                print("    -- help                      to display help ") 
                print("    - World                      See a case in world ")
                print("      world <all>                see a case in world")
                print("      world <country>            See a case in <country>")
                print("    - clear                      Clear screen in your terminal")

                print("    - Exit                       Exiting program " )
                print()
                print("[*] Author : sOlrac ")
                print("[*] Team : PlaySafe ")
                print()
                print("[!] This tools using API from https://globalcoronacase.com./api\n")
        def get_data(self,asw):
                data = r.get(asw).text
                return json.loads(data)
        def display(self,data,negara=False,Provinsi=False,world=False):
                if negara:
                        data = data[0]
                        print()
                        print("[*] Region : "+data["name"])
                        print("[*] Positive : "+data["positif"])
                        print(G+"[*] Recovered : "+data["recovered"])
                        print(R+"[*] Deaths: "+data["death"]+W)
                        print()
                if Provinsi:
                        print("[*] Province : "+data["attributes"]["Province"])
                        print("[*] Positive : "+str(data["attributes"]["actual_place"]))
                        print(G+"[*] Recovered : "+str(data["attributes"]["actual_Semb"]))
                        print(R+"[*] Deaths : "+str(data["attributes"]["actual_minute"])+W)
                        print("-"*30)
                if world:
                        print(f"[*] Country : {data['attributes']['Country_Region']}")
                        print(f"[*] Last Update : {data['attributes']['Last_Update']}")
                        print(f"[*] Confirmed : {data['attributes']['Confirmed']}")
                        print(f"[*] Positive : {data['attributes']['Active']}")
                        print(f"{G}[*] Recovered : {data['attributes']['Recovered']}")
                        print(f"{R}[*] Deaths : {data['attributes']['Deaths']}{W}")
                        print("-"*30)
        def menu(self):
                carl = input("sOlrac >>> ").lower()
                if carl in ["?","help"]:
                        self.help()
               
                elif carl == "provinsi":
                        print("\n\t[ CORONA ON PROVINCE ]")
                        data = self.get_data(self.country.format(self.idn))
                        for x in data:
                                self.display(x,Provinsi=True)
                elif carl == "world":
                        print("\n\t[ CORONA IN THE WORLD ]\n")
                        while True:
                                carl = input("sOlrac(GLOBAL) >>> ").title()
                                if carl == "All":
                                        for x in data:
                                                self.display(x)
                                elif "Exit" in carl:
                                        while True:
                                                self.menu()
                                elif carl in ["?","Help"]:
                                        self.help()
                                elif carl == "Clear":
                                        self.clear()
                                else:
                                        data = self.get_data("https://api.kawalcorona.com")
                                        for x in data:
                                                if carl in x["attributes"]["Country_Region"]:
                                                        self.display(x,world=True)
                elif carl == "clear":
                        self.clear()
                elif carl == 'exit':
                        exit()
                else:
                        print(f"{R}[!] No command \"{carl}\" found. Type \"?\" or \"help\" to description {W}\n")
try:
        print('\n\n\t[ CORONA by sOlrac. ]\n')
        import requests as r
        import json
        import os
        R = '\033[31m'
        G = '\033[32m'
        W = "\033[0m"
        Main()
except (KeyboardInterrupt,EOFError):
        exit("[!] User exit! ")
except r.exceptions.ConnectionError:
        exit("[!] no conection/connection error")
