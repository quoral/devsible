#!/usr/bin/env python3
import os
import subprocess
import argparse
from pathlib import Path

repo_location = Path(os.path.dirname(os.path.realpath(__file__))).parent

parser = argparse.ArgumentParser(description="Devsible shortcut - With shortcuts for syncing change")
parser.add_argument("--ignore-changes", action='store_true', 
                    help="Ensure that all cloned repositories are not checked for changes (Implies they are not cloned either)")

args = parser.parse_args()
command = ["ansible-playbook", "--inventory=inventory/work.ini", "playbook.yml"]

if args.ignore_changes:
    command += ["-e", "check_dotfiles_repo=false"]

subprocess.run(command, cwd=repo_location)