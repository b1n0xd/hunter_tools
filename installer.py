import os
from repo import repositoriesGolang
from repo import repositoriesPython

# Install Go
os.system("echo 'Instalando ferramentas necessárias...'")
os.system("apt install golang")
os.system("apt install golang")
os.system("pipx install bbot")


# Install tools Golang
for repo in repositoriesGolang:
    os.system(f"go install {repo}@latest")

# Install tools Python
for repo in repositoriesPython:
    os.system(f"pip3 install {repo}")


os.system("echo 'Installed tools Golang:'")
for repo in repositoriesGolang:
    os.system('clear')
    tool_name = repo.split("/")[-1]
    os.system(f"echo {tool_name}")

os.system("echo 'Installed tools Python:    '")
for repo in repositoriesPython:
    tool_name = repo.rsplit('/', maxsplit=1)[-1]
    os.system(f"echo {tool_name}")