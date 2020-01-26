#!/usr/bin/env python

import apt
import json


def update_cache(cache):
    cache.update()
    cache.open()

def upgradable_packages(cache):
    cache = apt.Cache()
    return [pkg.name for pkg in cache if pkg.is_upgradable]

def dump_cache_information(cache):
    info = {
        "upgradable_packages": upgradable_packages(cache)
    }
    with open("/var/lib/devsible/package_info", 'w') as f:
        json.dump(info, f)

cache = apt.Cache()
update_cache(cache)
dump_cache_information(cache)
