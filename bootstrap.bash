#!/usr/bin/env bash
set -euo pipefail

if [[ $OSTYPE == 'darwin'* ]]
then
	export PATH="/opt/homebrew/bin:$PATH"
	brew install ansible
else
ansible-galaxy collection install kewlfft.aur
ansible-galaxy collection install community.general
