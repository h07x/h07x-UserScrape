import requests
import sys

try:
    from colorama import init, Fore, Style
    init()
    c1 = Fore.CYAN
    c2 = Fore.GREEN
    c3 = Fore.YELLOW
    c4 = Fore.MAGENTA
    c5 = Fore.RED
    c6 = Fore.WHITE
    cr = Fore.RESET
    bold = Style.BRIGHT
except ImportError:
    c1 = c2 = c3 = c4 = c5 = c6 = cr = bold = ""

def githubuserinfo(username):
    url = f"https://api.github.com/users/{username}"

    try:
        r = requests.get(url, timeout=10)
    except:
        print(f"\n{c5}{bold}error | scrape failed - network issue{cr}\n")
        return

    if r.status_code == 404:
        print(f"\n{c5}{bold}error | scrape failed - user {username} not found{cr}\n")
        return
    elif r.status_code == 403:
        print(f"\n{c5}{bold}error | scrape failed - rate limit hit (60 per hour){cr}\n")
        return
    elif r.status_code != 200:
        print(f"\n{c5}{bold}error | scrape failed - http {r.status_code}{cr}\n")
        return

    d = r.json()

    print(f"\n{c1}{bold}╔════════════════════════════════════════════════════════╗{cr}")
    print(f"{c1}{bold}║{cr} {c2}{bold}GITHUB USER INFO{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}╠════════════════════════════════════════════════════════╣{cr}")
    print(f"{c1}{bold}║{cr} {c3}login:{cr}     {c6}{d.get('login', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}name:{cr}      {c6}{d.get('name', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}id:{cr}        {c6}{d.get('id', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}bio:{cr}       {c6}{d.get('bio', 'n/a')[:60]}{cr}                                 {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}location:{cr}  {c6}{d.get('location', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}company:{cr}   {c6}{d.get('company', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}email:{cr}     {c6}{d.get('email', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}twitter:{cr}   {c6}{d.get('twitter_username', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}blog:{cr}      {c6}{d.get('blog', 'n/a')}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}followers:{cr} {c2}{d.get('followers', 0)}{cr}    {c3}following:{cr} {c2}{d.get('following', 0)}{cr}                                 {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}repos:{cr}     {c2}{d.get('public_repos', 0)}{cr}    {c3}gists:{cr} {c2}{d.get('public_gists', 0)}{cr}                                  {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}created:{cr}   {c6}{d.get('created_at', 'n/a')[:10]}{cr}                                      {c1}{bold}║{cr}")
    print(f"{c1}{bold}║{cr} {c3}profile:{cr}   {c3}{d.get('html_url', 'n/a')}{cr}                            {c1}{bold}║{cr}")
    print(f"{c1}{bold}╚════════════════════════════════════════════════════════╝{cr}\n")

def main():
    print(f"{c2}{bold}")
    print(""" 
    ╔═══════════════════════════════════════════╗
    ║         h07x GITHUB TOOL               ║
    ╚═══════════════════════════════════════════╝
    """)
    print(f"{cr}")

    while True:
        print(f"{c1}{bold}┌─────────────────────────────────────────┐{cr}")
        print(f"{c1}{bold}│{cr}  {c2}[1]{cr} github user info                   {c1}{bold}│{cr}")
        print(f"{c1}{bold}│{cr}  {c5}[2]{cr} exit                                 {c1}{bold}│{cr}")
        print(f"{c1}{bold}└─────────────────────────────────────────┘{cr}")

        choice = input(f"\n{c3}{bold}→{cr} {c6}select: {cr}")

        if choice == "1":
            name = input(f"{c3}{bold}→{cr} {c6}username: {cr}").strip()
            if name:
                githubuserinfo(name)
            else:
                print(f"\n{c5}{bold}error | scrape failed - username empty{cr}\n")
        elif choice == "2":
            print(f"\n{c2}{bold}[+] goodbye{cr}\n")
            sys.exit(0)
        else:
            print(f"\n{c5}{bold}error | scrape failed - invalid option{cr}\n")

if __name__ == "__main__":
    main()