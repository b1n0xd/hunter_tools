import os
from repo import repositoriesGolang
from repo import repositoriesPython


def main():
    print('[+] Hunter Tools by b1n0xd [+]')
    print('==============================')
    print("[+] 1 - Install essentials OS [+]")
    print("[+] 2 - Install Golang Tools Based [+]")
    print("[+] 3 - Install Python Tools Based [+]")
    print("[+] 4 - Install Wordlists [+]")
    print("[+] 5 - Install All Tools")

    try:
        option_received = int(input("Enter option number: "))
        installer(option_received)
    except ValueError:
        print("Invalid Input. Please enter a number.")


def install_essentials():
    print("[+] Installing essentials OS... [+]")
    os.system("sudo apt-get -y update")
    os.system("sudo apt-get -y upgrade")
    os.system("sudo apt-get install -y git")
    os.system("sudo apt-get install -y xargs")
    os.system("apt install golang -y")
    os.system("apt install python3-full -y")
    os.system("py -3 -m pip install --user pipx")
    os.system("pipx install bbot -y")
    os.system("echo [+] Create folders [+]")
    os.system("mkdir ~/tools")
    os.system("mkdir ~/tools/zip")
    os.system("mkdir ~/bugbounty")
    os.system("mkdir ~/bugbounty/target")
    os.system("mkdir ~/bugbounty/lists")
    os.system("git clone https://github.com/devanshbatham/paramspider")
    os.system("cd paramspider")
    os.system("pip3 install .")
    os.system("cd ~")
    os.system("clear")


def install_golang_tools():
    print("[+] Installing Golang Tools Based [+]")
    for repo in repositoriesGolang:
        os.system(f"go install {repo}@latest")

    for repo in repositoriesGolang:
        tool_name = repo.split("/")[-1]
        os.system(f"echo {tool_name}")
        os.system("clear")
        os.system("echo '[+] Installed Tools Golang(based) [+]'")


def install_python_tools():
    print("[+] Installing Python Tools Based [+]")
    for repo in repositoriesPython:
        os.system(f"pip3 install {repo}")
        os.system("clear")
        os.system("echo '[+] Installed tools Python(based) [+]")

    for repo in repositoriesPython:
        tool_name = repo.rsplit('/', maxsplit=1)[-1]
        os.system(f"echo {tool_name}")
        os.system('sudo mv ~/go/bin/* /usr/bin/ ')
        os.system("clear")
        os.system("[+] All Worldlists Successfully installed. [+]")


def install_wordlists():
    print("[+] Installing All Worldlists [+]")
    os.system("mkdir ~/worldlists")
    os.system("cd ~/worldlists")
    os.system("git clone https://github.com/trickest/wordlists.git")
    os.system(
        "git clone https://github.com/fuzzdb-project/fuzzdb.git --depth 1")
    os.system(
        "git clone https://gitlab.com/kalilinux/packages/wordlists.git")
    os.system("cd ~")
    os.system("clear")
    os.system("[+] All Worldlists Successfully installed. [+]")


def install_all_tools():
    print("[+] Installing All Tools Based [+]")
    os.system("sudo apt-get -y update")
    os.system("sudo apt-get -y upgrade")
    os.system("sudo apt-get install -y git")
    os.system("sudo apt-get install -y xargs")
    os.system("apt install golang -y")
    os.system("apt install python3-full -y")
    os.system("py -3 -m pip install --user pipx")
    os.system("pipx install bbot -y")
    os.system("echo [+] Create folders [+]")
    os.system("mkdir ~/tools")
    os.system("mkdir ~/tools/zip")
    os.system("mkdir ~/bugbounty")
    os.system("mkdir ~/bugbounty/target")
    os.system("mkdir ~/bugbounty/lists")
    os.system("git clone https://github.com/devanshbatham/paramspider")
    os.system("cd paramspider")
    os.system("pip3 install .")
    os.system("cd ~")
    os.system("clear")
    os.system("echo '[+] Installing Wordlists at ~/wordlists [+]  ")
    os.system("mkdir ~/worldlists")
    os.system("cd ~/worldlists")
    os.system("git clone https://github.com/trickest/wordlists.git")
    os.system(
        "git clone https://github.com/fuzzdb-project/fuzzdb.git --depth 1")
    os.system(
        "git clone https://gitlab.com/kalilinux/packages/wordlists.git")
    os.system("cd ~")

    print("[+] Installing Python Tools Based [+]")
    for repo in repositoriesPython:
        os.system(f"pip3 install {repo}")
        os.system("clear")
        os.system("echo '[+] Installed tools Python(based) [+]")

    for repo in repositoriesPython:
        tool_name = repo.rsplit('/', maxsplit=1)[-1]
        os.system(f"echo {tool_name}")
        os.system('sudo mv ~/go/bin/* /usr/bin/ ')
        os.system("clear")
        os.system("[+] All Worldlists Successfully installed. [+]")


def installer(option_received):
    match option_received:
        case 1:
            install_essentials()
        case 2:
            install_golang_tools()
        case 3:
            install_python_tools()
        case 4:
            install_wordlists()
        case 5:
            install_all_tools()
        case _:
            print("[+] Invalid option,Only numbers!!! [+]")


if __name__ == "__main__":
    main()
