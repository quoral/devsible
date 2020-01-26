#!/usr/bin/env python3
import os
import subprocess
import argparse
import apt

from git import Repo
from pathlib import Path

repo_location = Path(os.path.dirname(os.path.realpath(__file__))).parent

parser = argparse.ArgumentParser(description="Devsible shortcut - With shortcuts for syncing change")
parser.add_argument("--ignore-changes", action='store_true', 
                    help="Ensure that all cloned repositories are not checked for changes (Implies they are not cloned either)")
parser.add_argument("--git-check", "-c", action='store_true',
                    help="Check status of all git repositories.")
parser.add_argument("--no-ansible", action='store_false',
                    help="Do not run ansible.")
parser.add_argument("--upgradable-packages", action='store_true', help="Get upgradable packages")

git_repositories = [(repo_location, "devsible"), (Path(repo_location, "roles/dotfiles"), "dotfiles")]

args = parser.parse_args()
command = ["ansible-playbook", "--inventory=inventory/work.ini", "playbook.yml"]

def get_changes(repo, name):
    changed = repo.is_dirty()
    changed_files = repo.git.diff(None, name_only=True).split("\n")
    return {
        "name": name,
        "changed": changed,
        "changed_files": changed_files
    }

def all_changes(repo_list):
    changes = [get_changes(Repo(repo), name) for repo, name in repo_list]
    for change in filter(lambda change: change["changed"],
                         changes):
        print("{}:".format(change["name"]))
        for file in change["changed_files"]:
            print("  - {}".format(file))

def upgradable_packages():
    return []
    cache = apt.Cache()
    return [pkg for pkg in cache if pkg.is_upgradable]

if args.ignore_changes:
    command += ["-e", "check_dotfiles_repo=false"]

if args.git_check:
    all_changes(git_repositories)

if args.upgradable_packages:
    print("packages:")
    for pkg in upgradable_packages():
        print("  - {}".format(pkg))

if args.no_ansible:
    subprocess.run(command, cwd=repo_location)

