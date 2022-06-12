# modules
import subprocess

# autorun
# readme.md
readme = str(input("Do you want to read the documentaries? ['y'/'n']: "))
if readme == 'y':
    subprocess.run("nano README.txt", shell=True)

elif readme == 'n':
    print("OK, Enjoy")