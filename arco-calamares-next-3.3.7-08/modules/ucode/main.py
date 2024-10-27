#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014 - 2019, Philip Müller <philm@manjaro.org>
#   Copyright 2016, Artoo <artoo@manjaro.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import subprocess

from os.path import join, exists
from libcalamares.utils import target_env_call


class ConfigController:
    def __init__(self):
        self.__root = libcalamares.globalstorage.value("rootMountPoint")

    @property
    def root(self):
        return self.__root

    def run(self):

        # ucode
        cpu_ucode = subprocess.getoutput("hwinfo --cpu | grep Vendor: -m1 | cut -d\'\"\' -f2")
        if cpu_ucode == "AuthenticAMD":
            #target_env_call(["pacman", "-S", "amd-ucode", "--noconfirm"])
            target_env_call(["pacman", "-R", "intel-ucode", "--noconfirm"])
        elif cpu_ucode == "GenuineIntel":
            #target_env_call(["pacman", "-S", "intel-ucode", "--noconfirm"])
            target_env_call(["pacman", "-R", "amd-ucode", "--noconfirm"])

        if exists(join(self.root, "usr/bin/snapper")):
            target_env_call(["snapper", "-c", "root", "--no-dbus", "create-config", "/"])
            target_env_call(["btrfs", "subvolume", "create", "/.snapshots"])
            target_env_call(["chmod", "a+rx", "/.snapshots"])
            target_env_call(["chown", ":users", "/.snapshots"])

def run():
    """ Post installation configurations  """

    config = ConfigController()

    return config.run()
