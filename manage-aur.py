#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import glob

if len(sys.argv) < 2:
    print("Unknown command, use 'help' to show commands.")
    exit(0)
elif sys.argv[1] == "update":
    for aur_dir in glob.glob("/home/enzo/aur/*"):
        print(aur_dir + " :")
        subprocess.call(["git", "pull"], cwd=aur_dir)
    print("Use 'build <aur name>' to upgrade")
    exit(0)
elif sys.argv[1] == "build":
    if len(sys.argv) < 3 or sys.argv[2] == "all":
        for aur_dir in glob.glob("/home/enzo/aur/*"):
            print("Building for " + aur_dir + " :")
            subprocess.call(["makepkg", "-si"], cwd=aur_dir)
        print("All AUR are builded.")
        exit(0)
    else:
        aur_dir = "/home/enzo/aur/" + sys.argv[2]
        subprocess.call(["makepkg", "-si"], cwd=aur_dir)
        exit(0)
elif sys.argv[1] == "list":
    subprocess.call("ls", cwd="/home/enzo/aur/")
    exit(0)
elif sys.argv[1] == "install":
    if len(sys.argv) < 3:
        print("Unknown command, use 'help' to show commands.")
    else:
        new_aur = sys.argv[2]
        aur_link = "https://aur.archlinux.org/" + new_aur + ".git"
        aur_dir = "/home/enzo/aur/" + new_aur
        print(aur_link)
        subprocess.call(["git", "clone", aur_link], cwd="/home/enzo/aur/")
        subprocess.call(["makepkg", "-si"], cwd=aur_dir)
elif sys.argv[1] == "help":
    print("Usage : manage-aur <command>")
    print("\n")
    print("help: show help")
    print("install <aur name>: install the following aur")
    print("list: list all aur in the directory")
    print("update: Update ALL aur in the directory")
    print("build <aur name>: build the following aur")
    print("build all: build all aur")
    exit(0)
else:
    print("Unknown command, use 'help' to show commands.")
    exit(0)
