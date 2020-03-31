# TsuserverDR, a Danganronpa Online server based on tsuserver3, an Attorney Online server
#
# Copyright (C) 2016 argoneus <argoneuscze@gmail.com> (original tsuserver3)
# Current project leader: 2018-20 Chrezm/Iuvee <thechrezm@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import ipaddress
import json

from server.constants import Constants
from server.exceptions import ServerError

class BanManager:
    def __init__(self, server):
        self.bans = []
        self.load_banlist()
        self.server = server

    def load_banlist(self):
        try:
            with Constants.fopen('storage/banlist.json', 'r') as banlist_file:
                self.bans = json.load(banlist_file)
        except ServerError as ex:
            if ex.code == 'FileNotFound':
                return
            raise

    def write_banlist(self):
        with open('storage/banlist.json', 'w') as banlist_file:
            json.dump(self.bans, banlist_file)

    def add_ban(self, ip):
        try:
            try:
                int(ip)
            except ValueError:
                ipaddress.ip_address(ip)
                ip = self.server.get_ipid(ip)
        except ValueError:
            raise ServerError('Argument must be an IP address or IPID.')
        if ip not in self.bans:
            self.bans.append(ip)
        else:
            raise ServerError('User is already banned.')
        self.write_banlist()

    def remove_ban(self, ip):
        try:
            try:
                int(ip)
            except ValueError:
                ipaddress.ip_address(ip)
                ip = self.server.get_ipid(ip)
        except ValueError:
            raise ServerError('Argument must be an IP address or IPID.')
        if ip in self.bans:
            self.bans.remove(ip)
        else:
            raise ServerError('User is already not banned.')
        self.write_banlist()

    def is_banned(self, ipid):
        return ipid in self.bans
