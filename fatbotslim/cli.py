# -*- coding: utf-8 -*-
#
# This file is part of FatBotSlim.
#
# FatBotSlim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FatBotSlim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FatBotSlim. If not, see <http://www.gnu.org/licenses/>.
#

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from fatbotslim import NAME, VERSION
from fatbotslim.irc import spawn_client
from fatbotslim.log import create_logger

log = create_logger(__name__)


def make_parser():
    parser = ArgumentParser(
            description='Start an IRC bot instance from the command line.',
            formatter_class=ArgumentDefaultsHelpFormatter,

        )
    parser.add_argument('-v', '--version', action='version', version='{0} v{1}'.format(NAME, VERSION))
    parser.add_argument('-s', '--server', metavar='HOST', help='the host to connect to', default='irc.freenode.net')
    parser.add_argument('-p', '--port', metavar='PORT', type=int, default=6667, help='the port the server is listening on')
    parser.add_argument('-n', '--nick', metavar='NAME', default=NAME, help="the bot's nickname")
    parser.add_argument('-N', '--name', metavar='NAME', default=NAME, help="the bot's real name")
    parser.add_argument('-c', '--channels', metavar='CHAN', nargs='*', help='join this channel upon connection')
    parser.add_argument('--ssl', action='store_true', help='connect to the server using SSL')
    return parser

def main():
    log.info("Running from the command line")
    parser = make_parser()
    args = parser.parse_args()
    settings = {
        'server': args.server,
        'port': args.port,
        'ssl': args.ssl,
        'nick': args.nick,
        'realname': args.name,
        'channels': args.channels or [],
    }
    greenlet, bot = spawn_client(settings)
    try:
        greenlet.join()
    except KeyboardInterrupt:
        log.info("Killed by user, disconnecting...")
        bot.conn.disconnect()
    finally:
        greenlet.kill()
