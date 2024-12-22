import random
import string
import os
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)

# Clear the terminal screen function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Title function
def display_title():
    print(Fore.RED + """
██████╗░██████╗░██╗███╗░░░███╗███████╗
██╔══██╗██╔══██╗██║████╗░████║██╔════╝
██████╔╝██████╔╝██║██╔████╔██║█████╗░░
██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░
██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝
    """)
    print(Fore.YELLOW + "Join our Discord: https://discord.gg/MPKNp9h6Hj")  # Your Discord link

# Random Email Generator (more realistic format)
def generate_fake_email():
    domains = ["gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "fiza.uk.co"]
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))  # Random name with digits
    domain = random.choice(domains)  # Random domain
    return f"{name}@{domain}"

# Simple Password Generator (realistic format)
def generate_simple_password():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))  # Simpler password of 12 characters

# Random IP Generator (valid format)
def generate_fake_ip():
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))  # Ensure each section is a valid number (1-255)
    return ip

# Crunchyroll Generator (Random email and password)
def generate_crunchyroll():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# Mcfa Generator (Random email and password)
def generate_mcfa():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# Spotify Generator (Random email and password)
def generate_spotify():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# Netflix Generator (Random email and password)
def generate_netflix():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# NordVPN Generator (Random email and password)
def generate_nordvpn():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# Steam Generator (Random email and password)
def generate_steam():
    email = generate_fake_email()
    password = generate_simple_password()
    return f"{email}:{password}"

# Discord Nitro Gift Link Generator
def generate_nitro_gift_link():
    gift_link = "https://discord.gift/" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return gift_link

# Discord Nitro Promo Code Generator
def generate_nitro_promo():
    promo_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # Nitro promo code format
    return promo_code

# Discord Token Generator
def generate_discord_token():
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=59))  # Discord token length
    return token

# Menu function to display options
def display_menu():
    print(Fore.RED + "1. Generate Email")
    print(Fore.RED + "2. Generate Password")
    print(Fore.RED + "3. Generate IP Address")
    print(Fore.RED + "4. Generate Crunchyroll Account")
    print(Fore.RED + "5. Generate Mcfa Account")
    print(Fore.RED + "6. Generate Spotify Account")
    print(Fore.RED + "7. Generate Netflix Account")
    print(Fore.RED + "8. Generate NordVPN Account")
    print(Fore.RED + "9. Generate Steam Account")
    print(Fore.RED + "10. Generate Discord Nitro Gift Link")
    print(Fore.RED + "11. Generate Discord Nitro Promo Code")
    print(Fore.RED + "12. Generate Discord Token")
    print(Fore.RED + "13. Exit")

# Main Function to run the tool
def main():
    clear_terminal()
    display_title()

    while True:
        display_menu()
        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == '13':
            print(Fore.RED + "Exiting tool...")
            break

        count = int(input(Fore.YELLOW + "How many would you like to generate? "))
        
        if choice == '1':
            for _ in range(count):
                fake_email = generate_fake_email()
                print(Fore.RED + f"Email: {fake_email}")
        elif choice == '2':
            for _ in range(count):
                fake_password = generate_simple_password()
                print(Fore.RED + f"Password: {fake_password}")
        elif choice == '3':
            for _ in range(count):
                fake_ip = generate_fake_ip()
                print(Fore.RED + f"IP Address: {fake_ip}")
        elif choice == '4':
            for _ in range(count):
                crunchyroll_account = generate_crunchyroll()
                print(Fore.RED + f"Crunchyroll Account: {crunchyroll_account}")
        elif choice == '5':
            for _ in range(count):
                mcfa_account = generate_mcfa()
                print(Fore.RED + f"Mcfa Account: {mcfa_account}")
        elif choice == '6':
            for _ in range(count):
                spotify_account = generate_spotify()
                print(Fore.RED + f"Spotify Account: {spotify_account}")
        elif choice == '7':
            for _ in range(count):
                netflix_account = generate_netflix()
                print(Fore.RED + f"Netflix Account: {netflix_account}")
        elif choice == '8':
            for _ in range(count):
                nordvpn_account = generate_nordvpn()
                print(Fore.RED + f"NordVPN Account: {nordvpn_account}")
        elif choice == '9':
            for _ in range(count):
                steam_account = generate_steam()
                print(Fore.RED + f"Steam Account: {steam_account}")
        elif choice == '10':
            for _ in range(count):
                nitro_gift_link = generate_nitro_gift_link()
                print(Fore.RED + f"Discord Nitro Gift Link: {nitro_gift_link}")
        elif choice == '11':
            for _ in range(count):
                nitro_promo_code = generate_nitro_promo()
                print(Fore.RED + f"Discord Nitro Promo Code: {nitro_promo_code}")
        elif choice == '12':
            for _ in range(count):
                discord_token = generate_discord_token()
                print(Fore.RED + f"Discord Token: {discord_token}")
        else:
            print(Fore.RED + "Invalid option, try again.")
        
        input(Fore.YELLOW + "Press Enter to continue...")  # Wait for the user to press Enter before clearing the terminal

        clear_terminal()  # Clear terminal before showing the next menu
        display_title()  # Display title again

if __name__ == "__main__":
    main()
