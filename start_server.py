#!/usr/bin/env python3

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

import sys
import traceback
import server.logger

from server.tsuserver import TsuserverDR

def main():
    server.logger.log_print('Starting...')

    my_server = None
    try:
        current_python_tuple = sys.version_info
        current_python_simple = 'Python {}.{}.{}'.format(*current_python_tuple[:3])
        if current_python_tuple < (3, 6):
            # This deliberately uses .format() because f-strings were not available prior to
            # Python 3.6
            msg = ('This version of TsuserverDR requires at least Python 3.6. You currently have '
                   '{}. Please refer to README.md for instructions on updating.'
                   .format(current_python_simple))
            raise RuntimeError(msg)
        if current_python_tuple < (3, 7):
            msg = (f'WARNING: The upcoming major release of TsuserverDR (4.3.0) will be requiring '
                   f'at least Python 3.7. You currently have {current_python_simple}. '
                   f'Please consider upgrading to at least Python 3.7 soon. You may find '
                   f'additional instructions on updating in README.md')
            server.logger.log_print(msg)
        my_server = TsuserverDR()
        my_server.start()
    except KeyboardInterrupt:
        raise
    except Exception:
        # Print complete traceback to console
        etype, evalue, etraceback = sys.exc_info()
        info = 'TSUSERVERDR HAS ENCOUNTERED A FATAL PYTHON ERROR.'
        info += "\r\n" + "".join(traceback.format_exception(etype, evalue, etraceback))
        server.logger.log_print(info)
        server.logger.log_error(info, server=my_server, errortype='P')
        server.logger.log_print('Server is shutting down.')
        server.logger.log_server('Server is shutting down due to an unhandled exception.')
        input("Press Enter to continue... ")

if __name__ == '__main__':
    main()
