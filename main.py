from rich import print
from time import sleep
import os, configparser, datetime, sys, readchar, requests, psutil
from sys import platform
from bs4 import BeautifulSoup

successtxt = ("[green] [SUCCESS] [/green]")
errtxt = ("[red] [ERROR] [/red]")
notext = ("[green_yellow] [NOTE] [/green_yellow]")
sighint = ("[dark_orange] [SIGINT] [/dark_orange]")
errtxt2 = ("[red] Value can't be empty! [/red]")
errtxt3 = ("[red] Invalid VerusAddress! [/red]")
errtxt4 = ("[red] Value can't be a string! [/red]")
errtxt5 = ("[red] Not a valid pool address! [/red]")
minertxt = ("[orange_red1] [MINER] [/orange_red1]")
betasystem = ("[yellow2] [BETA SYSTEM] [/yellow2]")
Systxt = ("[blue3] [SYSTEM] [/blue3]")
config = configparser.ConfigParser()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

def isNumber(s):
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
    return True                            

def countdown(t, statement):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(f"[deep_pink3] {statement}: [/deep_pink3]", timer, end="\r")
        sleep(1)
        t -= 1

def create_pool_stats_page(usraddr):
    pooluri = f"https://luckpool.net/verus/miner.html?{usraddr}"    
    return pooluri
                           
def part_of_day(h):
    return(
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )

if platform == "linux" or platform == "linux2":
    checkFilepath = "assets/configs/config.ini"
elif platform == "darwin":
    checkFilepath = "assets/configs/config.ini"
elif platform == "win32" or platform == "win64":
    checkFilepath = r"assets\configs\config.ini"

def UltimateVerusMiner():
    if os.path.isfile(checkFilepath):
        print("")
        print("""[royal_blue1]
         _   _ _ _   _                 _         _   _                      ___  ____                 
        | | | | | | (_)               | |       | | | |                     |  \/  (_)                
        | | | | | |_ _ _ __ ___   __ _| |_ ___  | | | | ___ _ __ _   _ ___  | .  . |_ _ __   ___ _ __ 
        | | | | | __| | '_ ` _ \ / _` | __/ _ \ | | | |/ _ \ '__| | | / __| | |\/| | | '_ \ / _ \ '__|
        | |_| | | |_| | | | | | | (_| | ||  __/ \ \_/ /  __/ |  | |_| \__ \ | |  | | | | | |  __/ |   
         \___/|_|\__|_|_| |_| |_|\__,_|\__\___|  \___/ \___|_|   \__,_|___/ \_|  |_/_|_| |_|\___|_|   
        [/royal_blue1]""".center(os.get_terminal_size().columns))
        print("[magenta3] Ultimate Verus Miner made by Shreyas-ITB using tpruvot, Monkins Modified CCMiner [/magenta3]".center(os.get_terminal_size().columns))
        print(f"[deep_pink2] Welcome to the Ultimate Verus Miner, please choose the options given below to continue! [/deep_pink2] [medium_spring_green] Have a great {part_of_day(datetime.datetime.now().hour)} [/medium_spring_green]".center(os.get_terminal_size().columns))
        print("")
        print("[blue_violet] 1). Start mining veruscoin [/blue_violet]")
        print("[blue_violet] 2). System load [/blue_violet]")
        print("[blue_violet] 3). Settings [/blue_violet]")
        print("[blue_violet] 4). About miner [/blue_violet]")
        print("[blue_violet] 5). Donate Verus to developer [/blue_violet]")
        #print("[blue_violet] 6). Exchange Verus using Safe.trade [/blue_violet]")
        print("")
        ques = input("Verus@ultimateverusminer >>: ")    
        if isNumber(ques) == False:
            print(f"{errtxt}: [red] This isn't allowed :( [/red] [blue_violet] Please enter the number corresponding to a perticular command without any brackets or a period. [/blue_violet]")
            print("")
            countdown(5, "The Screen will clear in")
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
            return
        config.read(checkFile)
        userinfo = config["USERINFO"]
        usraddr = userinfo["verusaddress"]
        usrthrds = userinfo["nothreads"]
        pooladdr = userinfo["pooladdress"]
        if ques == "1":
            if platform == "linux" or platform == "linux2":
                os.system("clear")
                print("[deep_pink2] Starting the miner... [/deep_pink2]")
                print("")
                os.system("chmod +x /assets/miners/ccminer")
                sleep(3)
                os.system(f"./assets/miners/ccminer -a verus -o {pooladdr} -u {usraddr}.VerusGUIMiner -p x -t {usrthrds}")
            elif platform == "darwin":
                os.system("clear")
                print("[deep_pink2] Starting the miner... [/deep_pink2]")
                print("")
                os.system("chmod +x /assets/miners/ccminer")
                sleep("")
                os.system(f"./assets/miners/ccminer -a verus -o {pooladdr} -u {usraddr}.VerusGUIMiner -p x -t {usrthrds}")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
                print(f"{minertxt} [deep_pink2] Starting the miner... [/deep_pink2]")
                print("")
                sleep(3)
                os.system(f".\\assets\\miners\\ccminer3.7.1.exe -a verus -o {pooladdr} -u {usraddr}.VerusGUIMiner -p x -t {usrthrds}")
        if ques == "2":
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
            print("")
            # pool = create_pool_stats_page(usraddr)
            # reqpage = requests.get(pool, headers=headers)
            # soupfetch = BeautifulSoup(reqpage.content, 'html.parser')
            # immature_balance = soupfetch.find(id="statsImmature").get_text()
            # print(f"[deep_sky_blue3] Your Immature Balance: [/deep_sky_blue3] [blue_violet] {immature_balance} [/blue_violet]")
            print("[royal_blue1] [SYSTEM STATS] [/royal_blue1]".center(os.get_terminal_size().columns))
            print("")
            print(f" {Systxt} [cyan1] RAM Used (in percentage) [/cyan1]: [sea_green1]{psutil.virtual_memory()[2]}%[/sea_green1]")
            print(f" {Systxt} [cyan1] RAM Used (in terms of GB) [/cyan1]: [sea_green1]{psutil.virtual_memory()[3]/1000000000} GB has been used[/sea_green1]")
            print(f" {Systxt} [cyan1] Current CPU Usage (in percentage) [/cyan1]: [sea_green1]{psutil.cpu_percent()}% [/sea_green1]")
            print("")
            countdown(10, "The Screen will clear in")
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
        if ques == "3":
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
            print("")
            print("[royal_blue1] [MINER SETTINGS] [/royal_blue1]".center(os.get_terminal_size().columns))
            print(f"{notext} [gold3] Anything you enter/edit here will change your details in the config file. If you dont want to edit anything then please press n and press enter to the questions this will exit the Settings menu [/gold3]".center(os.get_terminal_size().columns))
            print("")
            updsett = input("Do you want to edit your veruscoin address (Y/n): ")
            if updsett.lower() == "y":
                newvar =  input("Enter your new veruscoin wallet address: ")
                if len(newvar) < 34 or newvar == "Your VerusCoin Address":
                    print(f"{errtxt}: {errtxt3} [magenta] Please put in a valid veruscoin address and then press press enter. [/magenta]")
                    return
                if len(newvar) == 0:
                    print(f"{errtxt}: {errtxt2} [magenta] Please make sure that the input  not left empty. [/magenta]")
                    return
                else:
                    config.set('USERINFO', 'verusaddress', newvar)
                    with open(checkFile, 'w') as configfile:
                            config.write(configfile)
                    print("")
                    print(f"{successtxt}: [green] Config Updated! [/green] [dark_blue] Your values are updated into the miner. The miner will restart in a few seconds. [/dark_blue]")
                countdown(5, "Miner will restart in")
            else:
                updsett1 = input("Do you want to edit your number of mining threads? (Y/n): ")
                if updsett1.lower() == "y":
                    newvar1 = input("Enter the number of mining threads: ")
                    if len(newvar1) > 34:
                        print(f"{errtxt}: {errtxt3} [magenta] Please put in a valid veruscoin address and then press press enter. [/magenta]")
                        return
                    if len(newvar1) == 0:
                        print(f"{errtxt}: {errtxt2} [magenta] Please make sure that the input  not left empty. [/magenta]")    
                        return
                    if isNumber(newvar1) == False or len(newvar1) > 21 or newvar1 == "Number of CPU threads":
                        print(f"{errtxt}: {errtxt4} [magenta] Please make sure that you enter the number of threads which will be used for mining veruscoin. [/magenta]")
                        return
                    else:
                        config.set('USERINFO', 'nothreads', newvar1)
                        with open(checkFile, 'w') as configfile:
                            config.write(configfile)
                        print("")
                        print(f"{successtxt}: [green] Config Updated! [/green] [dark_blue] Your values are updated into the miner. The miner will restart in a few seconds. [/dark_blue]")
                    countdown(5, "Miner will restart in")
                else:
                    updsett2 = input("Do you want to edit the mining pool address (Y/n): ")
                    if updsett2.lower() == "y":
                        newvar2 = input("Enter the new pool address to mine: ")
                        if isNumber(newvar2) == True or newvar2 == "Pool address to mine verus":
                            print(f"{errtxt}: {errtxt5} [magenta] Please make sure that you enter the valid pool address. You can get the pool address from the official verus pool or luckpool [/magenta]")
                            return
                        else:
                            config.set('USERINFO', 'pooladdress', newvar2)
                            with open(checkFile, 'w') as configfile:
                                config.write(configfile)
                            print("")
                            print(f"{successtxt}: [green] Config Updated! [/green] [dark_blue] Your values are updated into the miner. The miner will restart in a few seconds. [/dark_blue]")
                        countdown(5, "Miner will restart in")
                    else:
                        print("")
                        countdown(5, "Miner will restart in")
                        if platform == "linux" or platform == "linux2":
                            os.system("clear")
                        elif platform == "darwin":
                            os.system("clear")
                        elif platform == "win32" or platform == "win64":
                            os.system("cls")
        if ques == "4":
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
            print("")
            print("[royal_blue1] [ABOUT MINER] [/royal_blue1]".center(os.get_terminal_size().columns))
            print("")
            print("[light_salmon1] [Version Specifications] [/light_salmon1]".center(os.get_terminal_size().columns))
            print("")
            print("[dark_orange] Miner version: [/dark_orange] [orchid2] v0.0.1 [/orchid2]")
            print("")
            print("[dark_orange] CCMiner version: [/dark_orange] [orchid2] v3.7.1 [/orchid2]")
            print("")
            print("[dark_orange] CLI Wallet version: [/dark_orange] [orchid2] v0.9.6-1 [/orchid2]")
            print("")
            print("[light_salmon1] [FAQ Questions] [/light_salmon1]".center(os.get_terminal_size().columns))
            print("")
            print("[dark_orange] Exchanging veruscoin supported: [/dark_orange] [orchid2] No not in this version maybe in the next release. [/orchid2]")
            print("")
            print("[dark_orange] Which exchange will be used to exchange verus by the miner: [/dark_orange] [orchid2] Safe.trade exchange as their API is free and opensource. [/orchid2]")
            print("")
            print("[dark_orange] Whats special about this miner: [/dark_orange] [orchid2] This miner is a wrap around miner for CCMiner which uses CCMiner as the base and adds some extra features to it. [/orchid2]")
            print("")
            print("[dark_orange] What are the new features supported on this miner: [/dark_orange] [orchid2] The best thing about this miner is it can transact as a wallet (using official Verus CLI wallet) as well as mine the coin as a miner (using CCMiner) it also adds some extra features like exchange option and exchange to giftcard option which are yet to be added. [/orchid2]")
            print("")
            print("[dark_orange] Where can i find the code of the miner: [/dark_orange] [orchid2] Its in github so if you want to contribute or fork it you can go to (https://github.com/Shreyas-ITB/UltimateVerusMiner). [/orchid2]")
            print("")
            print("[dark_orange] Why is it so colourful: [/dark_orange] [orchid2] Well you know terminal/CMD based apps doesnt look that good so i made it a bit colourful. [/orchid2]")
            print("")
            countdown(30, "This window will automatically close in")
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
        if ques == "5":
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
            print("")
            print("[royal_blue1] [DONATE TO DEVELOPER] [/royal_blue1]".center(os.get_terminal_size().columns))
            print("")
            print("[sea_green2] BTC donation address: [/sea_green2] [gold1] 1AJdfCpLWPNoAMDfHF1wD5y8VgKSSTHxPo [/gold1] [light_coral] (tpruvot) [/light_coral]")
            print("")
            print("[sea_green2] VRSC donation address: [/sea_green2] [blue_violet] RMPE8eWL5ynrdaMDHjMuVEkiEKEjenUdxq [/blue_violet] [light_coral] (Shreyas-ITB) [/light_coral]")
            print("")
            print("[sea_green2] BTC donation address: [/sea_green2] [gold1] 1D7348d3V9zHZZz1pZNnPiRWU3n8z7T78s [/gold1] [light_coral] (Shreyas-ITB) [/light_coral]")
            print("")
            countdown(10, "This window will close in")
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
    # if ques == "6":
    #     if platform == "linux" or platform == "linux2":
    #         os.system("clear")
    #     elif platform == "darwin":
    #         os.system("clear")
    #     elif platform == "win32" or platform == "win64":
    #         os.system("cls")
    #     print(f"{betasystem} [magenta2] This feature will be available in the next update as its being developed. The binaries for the wallet has already been added so expect it soon. Thankyou! [/magenta2]")
    #     print("")
    #     countdown(10, "This window will close in")
    #     if platform == "linux" or platform == "linux2":
    #         os.system("clear")
    #     elif platform == "darwin":
    #         os.system("clear")
    #     elif platform == "win32" or platform == "win64":
    #         os.system("cls")

    else:
        print("")
        print("""[royal_blue1]
         _   _ _ _   _                 _         _   _                      ___  ____                 
        | | | | | | (_)               | |       | | | |                     |  \/  (_)                
        | | | | | |_ _ _ __ ___   __ _| |_ ___  | | | | ___ _ __ _   _ ___  | .  . |_ _ __   ___ _ __ 
        | | | | | __| | '_ ` _ \ / _` | __/ _ \ | | | |/ _ \ '__| | | / __| | |\/| | | '_ \ / _ \ '__|
        | |_| | | |_| | | | | | | (_| | ||  __/ \ \_/ /  __/ |  | |_| \__ \ | |  | | | | | |  __/ |   
         \___/|_|\__|_|_| |_| |_|\__,_|\__\___|  \___/ \___|_|   \__,_|___/ \_|  |_/_|_| |_|\___|_|   
        [/royal_blue1]""".center(os.get_terminal_size().columns))
        print("[magenta3] Ultimate Verus Miner made by Shreyas-ITB using tpruvot, Monkins Modified CCMiner [/magenta3]".center(os.get_terminal_size().columns))
        print("")
        askwall = input("Do you wish to create new wallet address using Verus CLIwallet? This is completely automatic and it helps you in the future to exchange the coins using this miner software itself. Do you wish to continue? (Y/n): ")
        if askwall.lower() == 'y':
            if platform == "linux" or platform == "linux2":
                os.system("clear")
                print("[deep_pink2] Okay! please wait until your wallet gets created.. [/deep_pink2]")
                print("")
                wallcli = os.system("assets/cliwallets/linux/verus getnewaddress")
                print(f"[orchid2] {wallcli} [/orchid2]")
            elif platform == "darwin":
                os.system("clear")
                print("[deep_pink2] Okay! please wait until your wallet gets created.. [/deep_pink2]")
                print("")
                wallcli = os.system("assets/cliwallets/macos/verus getnewaddress")
                print(f"[orchid2] {wallcli} [/orchid2]")
            elif platform == "win32" or platform == "win64":
                os.system("cls")
                print("[deep_pink2] Okay! please wait until your wallet gets created.. [/deep_pink2]")
                print("")
                wallcli = os.system("assets\\cliwallets\\windows\\verus.exe getnewaddress")
                print(f"[orchid2] {wallcli} [/orchid2]")
        else:
            var = input("Enter your existing veruscoin wallet address, if you use external wallet address you wont be able to use the exchange function in the miner : ")
        var1 = input("Enter the number of mining threads: ")
        var2 = input("Enter the pool address to mine verus: ")
        # var2 = input(Do you want to configure GPU Mining? 1;36;40m")
        # if var2.lower() == 'y':
        #     global var3
        #     var3 = input(Enter the GPU Device number: \033[    if len(var) < 34 or len(var1) > 34 or var == "Your VerusCoin Address":
        if len(var) < 34 or len(var) > 34 or var == "Your VerusCoin Address":
            print(f"{errtxt}: {errtxt3} [magenta] Please put in a valid veruscoin address and then press press enter. [/magenta]")
            return
        if len(var) == 0 or len(var1) == 0:
            print(f"{errtxt}: {errtxt2} [magenta] Please make sure that the input  not left empty. [/magenta]")    
        if isNumber(var1) == False or len(var1) > 21 or var1 == "Number of CPU threads":
            print(f"{errtxt}: {errtxt4} [magenta] Please make sure that you enter the number of threads which will be used for mining veruscoin. [/magenta]")
            return
        if isNumber(var2) == True or var2 == "Pool address to mine verus":
            print(f"{errtxt}: {errtxt5} [magenta] Please make sure that you enter the valid pool address. You can get the pool address from the official verus pool or luckpool [/magenta]")
            return
        # if isNumber(var3) == False or len(var3) > 21 or var3 == "Number of GPU threads":
        #     print(f"{errtxt}: {errtxt4} [magenta] Please make sure that you enter the GPU Device number which will be used for mining veruscoin. [/magenta]")
        #     return
        else:
            config.add_section('USERINFO')
            config.set('USERINFO', 'verusaddress', var)
            config.set('USERINFO', 'nothreads', var1)
            config.set('USERINFO', 'pooladdress', var2)
            with open(checkFile, 'w') as configfile:
                config.write(configfile)
            print("")
            print(f"{successtxt}: [green] Config Saved! [/green] [dark_blue] Your values are saved into the miner. The miner will restart in a few seconds. [/dark_blue]")
            countdown(5, "Miner will restart in")
            if platform == "linux" or platform == "linux2":
                os.system("clear")
            elif platform == "darwin":
                os.system("clear")
            elif platform == "win32" or platform == "win64":
                os.system("cls")

try:
    while True:
        UltimateVerusMiner()
except KeyboardInterrupt:
    print("")
    msg = f"{sighint} [yellow] Sigint Recieved...[/yellow] [chartreuse1] Do you wish to quit the miner? (Y/n) [/chartreuse1]"
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        print(f"{minertxt} [orchid] Sorry to see you go![/orchid] [red]Quitting the miner...[/red]")
        print(f"{Systxt} [cyan] Have a great {part_of_day(datetime.datetime.now().hour)} [/cyan]")
        sys.exit(0)
    else:
        if platform == "linux" or platform == "linux2":
            os.system("clear")
            try:
                os.system(f"./UltimateVerusMiner")
            except KeyboardInterrupt:
                    print(f"{minertxt} [purple4] Exiting Gracefully... [/purple4]")
                    print("")
                    sys.exit(0)
        elif platform == "darwin":
            os.system("clear")
            try:
                os.system(f"./UltimateVerusMiner")
            except KeyboardInterrupt:
                    print(f"{minertxt} [purple4] Exiting Gracefully... [/purple4]")
                    print("")
                    sys.exit(0)
        elif platform == "win32" or platform == "win64":
            os.system("cls")
            try:
                os.system(f"UltimateVerusMiner.exe")
            except KeyboardInterrupt:
                    print(f"{minertxt} [purple4] Exiting Gracefully... [/purple4]")
                    print("")
                    sys.exit(0)