#!/usr/bin/env bash
set -euo pipefail


git clone https://github.com/kewlfft/ansible-aur ~/.ansible/plugins/modules/aur
ansible-galaxy collection install community.general
