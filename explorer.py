import inquirer
import os

def explorer() -> str:
    """
    Simple function to select one of several file/folder, In single mode you can navigate easily with up,down, and enter to go in the folder selected
    but if you choose an file the func gonna return his path.

    Instead in "several mode" you can choose one or multiple file/folder at one time ,(right arrow to select),
    in the current directory. 
    And if you choose nothing it loop,
    but if you have "<-> Return to navigation mode" in your selection its gonna just return in the single mode

    Returns:
        str: Return the path of the selected file/folder(s)
    """
    several_mode = False

    while True:
        # for windows
        if os.name == "nt":
            os.system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system("clear")

        # Display of current directory
        wdir = os.getcwd()

        print("\n" * 5)
        print(f"→ {wdir}\\")
        choices = []
        for each in os.listdir():
            if os.path.isdir(each):
                choices.append(f"🗀 {each}")
            elif os.path.islink(each):
                choices.append(f"L {each}")
            elif os.path.isfile(each):
                choices.append(f"🗎 {each}")
            else:
                choices.append(f"? {each}")

        # Single/Navigation mode
        if not several_mode:
            choices += ["↰ 🗀 .. (go to parent folder)"]
            choices.sort()
            choices.insert(1, "<-> Go to several mode")

            selected = inquirer.list_input(
                "Navigate in the current directory Select file in the current directory oror ",
                choices=choices,
            )
            print(selected)
            if selected == "↰ 🗀 .. (go to parent folder)":
                os.chdir("..")
            elif selected == "<-> Go to several mode":
                several_mode = True
            else:
                if os.path.isdir(selected[2:]) or os.path.islink(selected[2:]):
                    try:
                        os.chdir(selected[2:])
                    except PermissionError as e:
                        print("Yout dont have the permissions to go here.\n>", e)
                else:
                    file_path = os.path.join(wdir, selected[2:])
                    return file_path
        # Several mode (that u can select folder in this mode)
        else:
            choices.sort()
            choices.insert(0, "<-> Return to navigation mode")
            selected = inquirer.checkbox(
                "Select file in the current directory", choices=choices
            )
            if selected:
                if "<-> Return to navigation mode" in selected:
                    several_mode = False
                else:
                    return [os.path.join(wdir, i[2:]) for i in selected]
            else:
                pass
