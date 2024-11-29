import inquirer
import os

def explorer()->str:
    while True:
        wdir = os.getcwd()
        print("\n"*5)
        print(f"→ {wdir}\\")
        choices = [f"🗀 {i}" if os.path.isdir(i) 
                #    or os.path.islink(i)
                    else f"🗎 {i}" for i in os.listdir()]
        choices+=["🗀 .. (go up parent folder)"]
        choices.sort()
        selected = inquirer.list_input(
                        "Select file in the current directory",
                        choices=choices
        )
        if selected=="🗀 .. (go up parent folder)":
            os.chdir("..")
        else:
            if os.path.isdir(selected[2:]):
                os.chdir(selected[2:])
            else:
                file_path = os.path.join(wdir, selected[2:])
                return file_path

if __name__ == '__main__':
    print(explorer())