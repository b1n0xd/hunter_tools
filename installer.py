import os
from repo import repositoriesGolang
from repo import repositoriesPython


optionSelected = int(input("Insert number option:  "))


def installer(optionSelected):
    match optionSelected:
        case 1:
            print("[+] Instaling essentials OS... [+]")
        case 2:
            print("[+] Instaling Golang Tools Based [+]")
        case 3:
            print("[+] Instaling Python Tools Based [+]")
            for repo in repositoriesPython:
                os.system(f"pip3 install {repo}")
                os.system("echo '[+] Installed tools Python(based) [+]'")
            for repo in repositoriesPython:
                tool_name = repo.rsplit('/', maxsplit=1)[-1]
                os.system(f"echo {tool_name}")
                os.system('sudo mv ~/go/bin/* /usr/bin/ ')
                os.system("[+] All Worldlists Successfully installed. [+]")
        case 4:
            print("[+] Instaling All Worldlists [+]")
            os.system("mkdir ~/worldlists")
            os.system("cd ~/worldlists")
            os.system("git clone https://github.com/trickest/wordlists.git")
            os.system("wget -r --no-parent -R "index.html*" https://wordlists-cdn.assetnote.io/data/ -nH -e robots=of")
            os.system("git clone https://github.com/fuzzdb-project/fuzzdb.git --depth 1")
            os.system("git clone https://gitlab.com/kalilinux/packages/wordlists.git")
            os.system("cd ~")
            os.system("clear")
            os.system("[+] All Worldlists Successfully installed. [+]")
        case _:
            print("[+] Instaling All Tools Based [+]")
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
            os.system("echo '[+] Installing Wordlists at ~/wordlists [+]'  ")
            os.system("mkdir ~/worldlists")
            os.system("cd ~/worldlists")
            os.system("git clone https://github.com/trickest/wordlists.git")
            os.system("wget -r --no-parent -R "index.html*" https://wordlists-cdn.assetnote.io/data/ -nH -e robots=of")
            os.system("git clone https://github.com/fuzzdb-project/fuzzdb.git --depth 1")
            os.system("git clone https://gitlab.com/kalilinux/packages/wordlists.git")
            os.system("cd ~")


# Install tools Golang Based
for repo in repositoriesGolang:
    os.system(f"go install {repo}@latest")

# Install tools Python Based
for repo in repositoriesPython:
    os.system(f"pip3 install {repo}")


os.system("echo '[+] Installed Tools Golang(based) [+]'")
for repo in repositoriesGolang:
    tool_name = repo.split("/")[-1]
    os.system(f"echo {tool_name}")

os.system("echo '[+] Installed tools Python(based) [+]'")
for repo in repositoriesPython:
    tool_name = repo.rsplit('/', maxsplit=1)[-1]
    os.system(f"echo {tool_name}")
    os.system('sudo mv ~/go/bin/* /usr/bin/ ')


installer(optionSelected)
