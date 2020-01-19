# TsuserverDR, a Danganronpa Online server based on tsuserver3, an Attorney Online server
#
# Copyright (C) 2016 argoneus <argoneuscze@gmail.com> (original tsuserver3)
# Current project leader: 2018-19 Chrezm/Iuvee <thechrezm@gmail.com>
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

"""
This module holds all the commands that are either deprecated or are meant to
act as aliases for existing commands in commands.py
"""

def do_command(command, client, arg):
    """
    Wrapper function for calling commands.
    """
    source = client.server.commands
    adapted_command = 'ooc_cmd_{}'.format(command)
    function = getattr(source, adapted_command)
    function(client, arg)

def do_command_deprecated(command, client, arg):
    """
    Wrapper function for commands that are deprecated and pending removal.
    """
    client.send_ooc('This command is deprecated and pending removal in 4.3. '
                    'Please use /{} next time.'.format(command))
    do_command(command, client, arg)

def ooc_cmd_showname_list(client, arg):
    """
    Alias for /showname_areas.
    """

    do_command('showname_areas', client, arg)

def ooc_cmd_zg(client, arg):
    """
    Alias for /zone_global.
    """

    do_command('zone_global', client, arg)
