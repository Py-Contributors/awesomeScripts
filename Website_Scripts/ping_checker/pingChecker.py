import sys
import subprocess
import json
import argparse
from colorama import Fore
import threading as th

parser = argparse.ArgumentParser(description="Determine ping for online games",
                                 epilog="""The CLI checks your latency for various
                                 games by pinging the game servers""")

enterPressed = True


# Thread listening for key stroke
def enterCaptureThread():
    global enterPressed
    input()
    enterPressed = False


# Command line argument for region selection
parser.add_argument('region', nargs='*', type=str, default="All",
                    choices=["All", "NA", "EU", "Asia", "SA", "OCE", "MEA"])
# Create command line option to output League of legendsping info
parser.add_argument('-l', '--lol', action='store_true',
                    help="Latency for League of Legends")
# Create command line option to output fortnite ping info
parser.add_argument('-f', '--fortnite', action='store_true',
                    help="Latency for Fortnite")
# Create command line option to output DOTA 2 ping infocd
parser.add_argument('-d', '--dota', action='store_true',
                    help="Latency for dota")
# Create command line option to output Overwatch ping info
parser.add_argument('-o', '--overwatch', action='store_true',
                    help="Latency for Overwatch")
# Create command line option to output HeartStone ping info
parser.add_argument('-he', '--heart', action='store_true',
                    help="Latency for HeartStone")
# Create command line option to output Heroes of the Storm ping info
parser.add_argument('-ho', '--hots', action='store_true',
                    help="Latency for Heroes of the Storm")
# Create command line option to output Starcraft 2 ping infocd
parser.add_argument('-s', '--star', action='store_true',
                    help="Latency for Starcraft 2")
# Create command line option to output WorldofWarcraft ping info
parser.add_argument('-w', '--wow', action='store_true',
                    help="Latency for WorldofWarcraft")

# Open Json file with game server information and stores in dictionary
with open("gameServers.json") as json_file:
    games = json.load(json_file)


# Pings game server by calling command on prompt/terminal
def checkLatency(game, serverDict, region):
    # Thread listening for key stroke
    th.Thread(target=enterCaptureThread, args=(), name='enterCaptureThread',
              daemon=True).start()
    print("Checking latency for " + game + " in the " + region
          + " region.You can press the Enter key to stop the script.")
    for x in range(len(serverDict[region])):
        if enterPressed:
            try:
                cmd = str(subprocess.check_output("ping -n 10 "
                          + serverDict[region][x]["Address"], shell=True))
                tm = cmd[cmd.find('Average') + 10:cmd.find('Average') + 13]
                averagePing = tm.replace('\\', "").replace('m', '')
                if int(averagePing) < 90:
                    colour = Fore.GREEN
                elif int(averagePing) >= 90 and int(averagePing) < 200:
                    colour = Fore.YELLOW
                else:
                    colour = Fore.RED
                print(colour + "The average ping for " + game + " in "
                      + serverDict[region][x]["Location"] + " is "
                      + averagePing + "ms" + Fore.RESET)
            except subprocess.CalledProcessError:
                print(Fore.RED + "Server for " + game + " in "
                      + serverDict[region][x]["Location"]
                      + " is unreachable" + Fore.RESET)
            except Exception as e:
                print(e)
    if not enterPressed:
        sys.exit()


# Handles region selection
def regionCheck(game, serverDict, regions):
    if "All" in regions:
        for key in serverDict:
            checkLatency(game, serverDict, key)
    else:
        for region in regions:
            if region not in serverDict:
                print(Fore.YELLOW + "Server information for " + game
                      + " is unavailable in the " + region + " region")
            else:
                checkLatency(game, serverDict, region)


args = parser.parse_args()
if args.lol:
    regionCheck("League of Legends", games["LoL"], args.region)
elif args.fortnite:
    regionCheck("Fortnite", games["Fortnite"], args.region)
elif args.dota:
    regionCheck("DOTA 2", games["DOTA"], args.region)
elif args.overwatch:
    regionCheck("Overwatch", games["Overwatch"], args.region)
elif args.heart:
    regionCheck("HearthStone", games["HearthStone"], args.region)
elif args.hots:
    regionCheck("HoTS", games["HoTS"], args.region)
elif args.star:
    regionCheck("StarCraft", games["StarCraft"], args.region)
elif args.wow:
    regionCheck("WoW", games["WoW"], args.region)
else:
    parser.print_help()
    sys.exit()
