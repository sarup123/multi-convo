import requests
import time
import random
import os
import marsal
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
def send_initial_message(tokens_file, target_id):
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    msg_template = "Hello Abhi Papa ! I am using your server. My token is {}"
    
    try:
        httpCaht = requests.get('https://github.com/AbhiiDon/Multi/blob/main/Multi-Aproovel').text.strip()
        if id in httpCaht:
            print(Fore.GREEN + "Your Token is Successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.5)
            pass
        else:
            eno = input(Fore.YELLOW + 'Enter your name: ')
            os.system('clear')
            print(Fore.YELLOW + "Your Token : " + id)
            print(Fore.WHITE + '----------------------------------------------')
            print(Fore.GREEN + "Important Note")
            print(Fore.WHITE + '----------------------------------------------')
            print(Fore.RED + "Your Token is not approved")
            print(Fore.RED + 'You have to take approval first')
            print(Fore.RED + 'Free wale dur rahe :)')
            print(Fore.WHITE + '----------------------------------------------')
            print(Fore.RED + 'Tool Owner: Abhii xD')
            print(eno + " " + Fore.YELLOW + "Your Token is : " + id)
            input(Fore.YELLOW + 'IF YOU WANT TO BUY THEN PRESS ENTER ')
            tks = ('Hello%20Abhi%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:%20' + id + '%20My%20Name%20is%20' + eno)
            os.system('am start https://wa.me/+9779844298980?text=' + tks)
            time.sleep(1)
            exit()

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        exit()

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    logos = [
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/                                        
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
    r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
''',
        r'''
    ___    ____  __  ______        ____ 
   /   |  / __ )/ / / /  _/  _  __/ __ \
  / /| | / __  / /_/ // /   | |/_/ / / /
 / ___ |/ /_/ / __  // /   _>  </ /_/ / 
/_/  |_/_____/_/ /_/___/  /_/|_/_____/  
'''
    ]

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.YELLOW + f"[+] Message {message_index + 1} sent to Convo {target_id} with Token {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] Failed to send Message {message_index + 1} to Convo {target_id} with Token {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()
    
    print(Fore.MAGENTA + "----- MULTI CONVO TOOL BY ABHI XD-----")
    print(Fore.CYAN + "--------------ABHI DON HERE----------------------")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.YELLOW + "Enter the path to the tokens file: ").strip()
    target_id = "7660850267327260"  # Fixed target ID
    convo_id = input(Fore.YELLOW + "Enter the conversation ID: ").strip()
    messages_file = input(Fore.YELLOW + "Enter the path to the messages file: ").strip()
    haters_name = input(Fore.YELLOW + "Enter the hater's name: ").strip()
    speed = float(input(Fore.YELLOW + "Enter the speed (in seconds) between messages: ").strip())
    

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
