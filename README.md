# Devsible

I've got anxiety about computers. I loathe the moment that I have to reinstall my computer 
from scratch when moving companies, when performing disaster recovery. It's not about forgetting
to install `Emacs`, or about forgetting to copy my specialized config file into it's rightful place.

It's about forgetting that in order to use emacs, I need to do things in a special order. I need to run commands in certain orders.  
It's about forgetting to reload the systemd service after I added my configuration file  

And so much more.

## Why?
So this project has gone through a few different iterations over the past ten years:
- https://github.com/kallekrantz/puppet-personal
- https://github.com/kallekrantz/boxen

Being just two of the ones. They were pretty good for what I knew at the time, and while I 
could probably have written `devsible` using puppet, I thought it was time to try something new.

Enter: Ansible!

This project contains a *very* plain playbook, targetting the local host to run it's set of plays. 
It's extremely opinionated, and I would not recommend running it unless you've verified that my views 
on how a computer should behave matches yours.

## Get Started
First up, verify that you have `git` and `ansible` installed. That's how we start the process.
```
mkdir -p Code/Own/devsible
git clone https://github.com/kallekrantz/devsible Code/Own/devsible
cd Code/Own/devsible
bash bootstrap.bash
```

Now your system is prepared to run the playbook, so fire it away:
```
ansible-playbook -i inventory/work.ini playbook.yml
```
