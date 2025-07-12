import os
import shutil
import subprocess

# Fonts!

os.mkdir("~/.fonts")
os.symlink("~/dotfiles/NotoSansMono_SemiCondensed-SemiBold.ttf", "~/.fonts/NotoSansMono.ttf")
os.symlink("~/dotfiles/OpenSans-VariableFont_wdth,wght.ttf", "~/.fonts/OpenSans.ttf")

input("""HEY! From the main menu, go to system settings > Font Selection, and set:
Default font --------------------------- Open Sans Regular -- 11
Desktop font --------------------------- Open Sans Regular -- 11
Document font -------------------------- Open Sans Regular -- 11
Monospace font ----- Noto Sans Mono SemiCondensed SemiBold -- 11
Window title font -- Noto Sans Mono SemiCondensed SemiBold -- 11

(press enter to continue)
""")

input("""
From your system settings, go to themes, advanced, and select Mint-L-Purple fo Icons, And Orchis-Dark for Applications and Desktop.
(press enter to continue)
""")

print("If you've got spicetify installed, it's getting themed!!")

try:
    shutil.copytree("./catpuccin-spicetify/catppuccin", "~/.config/spicetify/Themes")
    subprocess.run("~/.spicetify/spicetify config current_theme catppuccin", shell=True, env=os.environ.copy())
    subprocess.run("~/.spicetify/spicetify config color_scheme macchiato", shell=True, env=os.environ.copy())
    subprocess.run("~/.spicetify/spicetify config inject_css 1 inject_theme_js 1 replace_colors 1 overwrite_assets 1", shell=True, env=os.environ.copy())
    subprocess.run("~/.spicetify/spicetify apply", shell=True, env=os.environ.copy())
except:
    pass

input("""Turns out i can't automatically theme pycharm and other jetbrain IDEs from the terminal, so instead you'll have to:
Go to settings (Ctrl+Alt+S)
Go to plugins, marketplace, and search for catppuccin, then install it.
Also in settings, go to Appearance & Behaviour > Appearance > Theme = Catppuccin Macchiato

(press enter to continue)
""")


input("""
I also can't theme chrome/edge for you, so install this extension:
https://chromewebstore.google.com/detail/catppuccin-chrome-theme-m/cmpdlhmnmjhihmcfnigoememnffkimlk
""")

input(f"""
I'd also suggest installing the darkreader extension, and on sites you want it active on press static, press the little orange circle with a pencil and paste in:
{open("darkreader.css", "r").read()}
""")

input("""
I also can't install the kicad theme for you, so:
Top bar: Tools > Plugin and content manager
Bottom left, Install from file, select ~/dotfiles/catppuccin-kicad-0.1.1.zip

Then go to Top bar: Preferences > Preferences
Schematic Editor > Colors > Theme = catppuccin macchiato
Footprint Editor > Colors > Theme = catppuccin macchiato
PCB Editor > Colors > Theme = catppuccin macchiato
""")

