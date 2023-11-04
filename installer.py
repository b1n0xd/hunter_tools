import os
from repo import repositoriesGolang
from repo import repositoriesPython

# Install essentials tools
os.system("echo 'Instalando ferramentas necessárias...'")
os.system("apt install golang")
os.system("apt install golang")
os.system("pipx install bbot")


# Install tools Golang Based
for repo in repositoriesGolang:
    os.system(f"go install {repo}@latest")

# Install tools Python Based
for repo in repositoriesPython:
    os.system(f"pip3 install {repo}")


os.system("echo 'Installed Tools Golang(base):'")
for repo in repositoriesGolang:
    os.system('clear')
    tool_name = repo.split("/")[-1]
    os.system(f"echo {tool_name}")

os.system("echo 'Installed tools Python(base):'")
for repo in repositoriesPython:
    tool_name = repo.rsplit('/', maxsplit=1)[-1]
    os.system(f"echo {tool_name}")