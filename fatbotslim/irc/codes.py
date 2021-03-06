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
"""
.. module:: fatbotslim.irc.codes

.. moduleauthor:: Mathieu D. (MatToufoutu)

This module lists the known IRC codes as defined in the :rfc:`1459#section-6`.

---

It also defines some custom codes:

**RPL_CONNECTED** (``001``): Connection established with the server.

**RPL_SERVERVERSION** (``002``): Server's name/version.

**RPL_SERVERCREATED** (``003``): Server's creation date.

**RPL_SERVERMODES** (``004``): Modes supported by the server.

**RPL_ISUPPORT** (``005``): Protocol extensions supported by the server.

**CTCP_VERSION**, **CTCP_PING**, **CTCP_TIME**, **CTCP_SOURCE**: self-explanatory.

**PING**, **PRIVMSG**, **NOTICE**, **JOIN**, **PART**: self-explanatory.

---

Codes are also grouped by type to make matching them easier:

**ERRORS**, **RESPONSES**, **RESERVED**, **CTCP**, **OTHERS**

---

There are also 2 special code sets:

**ALL_CODES**: Matches any code if listed in the groups previously mentionned.

**UNKNOWN_CODE**: Matches any code not listed in ``ALL_CODES``.
"""

# Error replies.
ERR_NOSUCHNICK = '401'
ERR_NOSUCHSERVER = '402'
ERR_NOSUCHCHANNEL = '403'
ERR_CANNOTSENDTOCHAN = '404'
ERR_TOOMANYCHANNELS = '405'
ERR_WASNOSUCHNICK = '406'
ERR_TOOMANYTARGETS = '407'
ERR_NOORIGIN = '409'
ERR_NORECIPIENT = '411'
ERR_NOTEXTTOSEND = '412'
ERR_NOTOPLEVEL = '413'
ERR_WILDTOPLEVEL = '414'
ERR_UNKNOWNCOMMAND = '421'
ERR_NOMOTD = '422'
ERR_NOADMININFO = '423'
ERR_FILEERROR = '424'
ERR_NINICKNAMEGIVEN = '431'
ERR_ERRONEUSNICKNAME = '432'
ERR_NICKNAMEINUSE = '433'
ERR_NICKCOLLISION = '436'
ERR_USERNOTINCHANNEL = '441'
ERR_NOTONCHANNEL = '442'
ERR_USERONCHANNEL = '443'
ERR_NOLOGIN = '444'
ERR_SUMMONDISABLED = '445'
ERR_USERDISABLED = '446'
ERR_NOTREGISTERED = '451'
ERR_NEEDMOREPARAMS = '461'
ERR_ALREADYREGISTERED = '462'
ERR_NOPERMFORHOST = '463'
ERR_PASSWDMISMATCH = '464'
ERR_YOUREBANNEDCREEP = '465'
ERR_KEYSET = '467'
ERR_CHANNELISFULL = '471'
ERR_UNKNOWNMODE = '472'
ERR_INVITEONLYCHAN = '473'
ERR_BANNEDFROMCHAN = '474'
ERR_BADCHANNELKEY = '475'
ERR_NOPRIVILEGES = '481'
ERR_CHANOPRIVSNEEDED = '482'
ERR_CANTKILLSERVER = '483'
ERR_NOOPERHOST = '491'
ERR_UMODEUNKNOWNFLAG = '501'
ERR_USERSDONTMATCH = '502'
ERRORS = set([
    ERR_NOSUCHNICK,
    ERR_NOSUCHSERVER,
    ERR_NOSUCHCHANNEL,
    ERR_CANNOTSENDTOCHAN,
    ERR_TOOMANYCHANNELS,
    ERR_WASNOSUCHNICK,
    ERR_TOOMANYTARGETS,
    ERR_NOORIGIN,
    ERR_NORECIPIENT,
    ERR_NOTEXTTOSEND,
    ERR_NOTOPLEVEL,
    ERR_WILDTOPLEVEL,
    ERR_UNKNOWNCOMMAND,
    ERR_NOMOTD,
    ERR_NOADMININFO,
    ERR_FILEERROR,
    ERR_NINICKNAMEGIVEN,
    ERR_ERRONEUSNICKNAME,
    ERR_NICKNAMEINUSE,
    ERR_NICKCOLLISION,
    ERR_USERNOTINCHANNEL,
    ERR_NOTONCHANNEL,
    ERR_USERONCHANNEL,
    ERR_NOLOGIN,
    ERR_SUMMONDISABLED,
    ERR_USERDISABLED,
    ERR_NOTREGISTERED,
    ERR_NEEDMOREPARAMS,
    ERR_ALREADYREGISTERED,
    ERR_NOPERMFORHOST,
    ERR_PASSWDMISMATCH,
    ERR_YOUREBANNEDCREEP,
    ERR_KEYSET,
    ERR_CHANNELISFULL,
    ERR_UNKNOWNMODE,
    ERR_INVITEONLYCHAN,
    ERR_BANNEDFROMCHAN,
    ERR_BADCHANNELKEY,
    ERR_NOPRIVILEGES,
    ERR_CHANOPRIVSNEEDED,
    ERR_CANTKILLSERVER,
    ERR_NOOPERHOST,
    ERR_UMODEUNKNOWNFLAG,
    ERR_USERSDONTMATCH,
])

# Command responses.
RPL_CONNECTED = '001'
RPL_SERVERVERSION = '002'
RPL_SERVERCREATED = '003'
RPL_SERVERMODES = '004'
RPL_ISUPPORT = '005'
RPL_YOURID = '042'
RPL_LOCALUSERS = '265'
RPL_GLOBALUSERS = '266'
RPL_NONE = '300'
RPL_USERHOST = '302'
RPL_ISON = '303'
RPL_AWAY = '301'
RPL_UNAWAY = '305'
RPL_NOAWAY = '306'
RPL_WHOISUSER = '311'
RPL_WHOISSERVER = '312'
RPL_WHOISOPERATOR = '313'
RPL_WHOISIDLE = '317'
RPL_ENDOFWHOIS = '318'
RPL_WHOISCHANNELS = '319'
RPL_WHOWASUSER = '314'
RPL_ENDOFWHOWAS = '369'
RPL_LISTSTART = '321'
RPL_LIST = '322'
RPL_LISTEND = '323'
RPL_CHANNELMODEIS = '324'
RPL_NOTOPIC = '331'
RPL_TOPIC = '331'
RPL_INVITING = '341'
RPL_SUMMONING = '342'
RPL_VERSION = '351'
RPL_WHOREPLY = '352'
RPL_ENDOFWHO = '315'
RPL_NAMREPLY = '353'
RPL_ENDOFNAMES = '366'
RPL_LINKS = '364'
RPL_ENDOFLINKS = '365'
RPL_BANLIST = '367'
RPL_ENDOFBANLIST = '368'
RPL_INFO = '371'
RPL_ENDOFINFO = '374'
RPL_MOTDSTART = '375'
RPL_MOTD = '372'
RPL_ENDOFMOTD = '376'
RPL_YOUREOPER = '381'
RPL_REHASHING = '382'
RPL_TIME = '391'
RPL_USERSTART = '392'
RPL_USERS = '393'
RPL_ENDOFUSERS = '394'
RPL_NOUSERS = '395'
RPL_TRACELINK = '200'
RPL_TRACECONNECTING = '201'
RPL_TRACEHANDSHAKE = '202'
RPL_TRACEUNKNOWN = '203'
RPL_TRACEOPERATOR = '204'
RPL_TRACEUSER = '205'
RPL_TRACESERVER = '206'
RPL_TRACENEWTYPE = '208'
RPL_TRACELOG = '261'
RPL_STATSLINKINFO = '211'
RPL_STATSCOMMANDS = '212'
RPL_STATSCLINE = '213'
RPL_STATSNLINE = '214'
RPL_STATSILINE = '215'
RPL_STATSKLINE = '216'
RPL_STATSYLINE = '218'
RPL_ENDOFSTATS = '219'
RPL_STATSLLINE = '241'
RPL_STATSUPTIME = '242'
RPL_STATSOLINE = '243'
RPL_STATSHLINE = '244'
RPL_UMODEIS = '221'
RPL_LUSERCLIENT = '251'
RPL_LUSEROP = '252'
RPL_LUSERUNKNOWN = '253'
RPL_LUSERCHANNELS = '254'
RPL_LUSERME = '255'
RPL_ADMINME = '256'
RPL_ADMINLOC1 = '257'
RPL_ADMINLOC2 = '258'
RPL_ADMINEMAIL = '259'
RPL_CONNECTING = '439'
RESPONSES = set([
    RPL_CONNECTED,
    RPL_SERVERVERSION,
    RPL_SERVERCREATED,
    RPL_SERVERMODES,
    RPL_ISUPPORT,
    RPL_YOURID,
    RPL_LOCALUSERS,
    RPL_GLOBALUSERS,
    RPL_NONE,
    RPL_USERHOST,
    RPL_ISON,
    RPL_AWAY,
    RPL_UNAWAY,
    RPL_NOAWAY,
    RPL_WHOISUSER,
    RPL_WHOISSERVER,
    RPL_WHOISOPERATOR,
    RPL_WHOISIDLE,
    RPL_ENDOFWHOIS,
    RPL_WHOISCHANNELS,
    RPL_WHOWASUSER,
    RPL_ENDOFWHOWAS,
    RPL_LISTSTART,
    RPL_LIST,
    RPL_LISTEND,
    RPL_CHANNELMODEIS,
    RPL_NOTOPIC,
    RPL_TOPIC,
    RPL_INVITING,
    RPL_SUMMONING,
    RPL_VERSION,
    RPL_WHOREPLY,
    RPL_ENDOFWHO,
    RPL_NAMREPLY,
    RPL_ENDOFNAMES,
    RPL_LINKS,
    RPL_ENDOFLINKS,
    RPL_BANLIST,
    RPL_ENDOFBANLIST,
    RPL_INFO,
    RPL_ENDOFINFO,
    RPL_MOTDSTART,
    RPL_MOTD,
    RPL_ENDOFMOTD,
    RPL_YOUREOPER,
    RPL_REHASHING,
    RPL_TIME,
    RPL_USERSTART,
    RPL_USERS,
    RPL_ENDOFUSERS,
    RPL_NOUSERS,
    RPL_TRACELINK,
    RPL_TRACECONNECTING,
    RPL_TRACEHANDSHAKE,
    RPL_TRACEUNKNOWN,
    RPL_TRACEOPERATOR,
    RPL_TRACEUSER,
    RPL_TRACESERVER,
    RPL_TRACENEWTYPE,
    RPL_TRACELOG,
    RPL_STATSLINKINFO,
    RPL_STATSCOMMANDS,
    RPL_STATSCLINE,
    RPL_STATSNLINE,
    RPL_STATSILINE,
    RPL_STATSKLINE,
    RPL_STATSYLINE,
    RPL_ENDOFSTATS,
    RPL_STATSLLINE,
    RPL_STATSUPTIME,
    RPL_STATSOLINE,
    RPL_STATSHLINE,
    RPL_UMODEIS,
    RPL_LUSERCLIENT,
    RPL_LUSEROP,
    RPL_LUSERUNKNOWN,
    RPL_LUSERCHANNELS,
    RPL_LUSERME,
    RPL_ADMINME,
    RPL_ADMINLOC1,
    RPL_ADMINLOC2,
    RPL_ADMINEMAIL,
    RPL_CONNECTING,
])

# Reserved numerics.
# These numerics are not described above since they fall into one of the following categories:
# 1) no longer in use;
#    2) reserved for future planned use;
#    3) in current use but are part of a non-generic 'feature' of the current IRC server.
RPL_TRACECLASS = '209'
RPL_SERVICEINFO = '231'
RPL_SERVICE = '233'
RPL_SERVLISTEND = '235'
RPL_WHOISCHANOP = '316'
RPL_CLOSING = '362'
RPL_INFOSTART = '373'
RPL_STATSQLINE = '217'
RPL_ENDOFSERVICES = '232'
RPL_SERVLIST = '234'
RPL_KILLDONE = '361'
RPL_CLOSEEND = '363'
RPL_MYPORTIS = '384'
ERR_BADCHANMASK = '476'
ERR_YOUWILLBEBANNED = '466'
ERR_NOSERVICEHOST = '492'
RESERVED = set([
    RPL_TRACECLASS,
    RPL_SERVICEINFO,
    RPL_SERVICE,
    RPL_SERVLISTEND,
    RPL_WHOISCHANOP,
    RPL_CLOSING,
    RPL_INFOSTART,
    RPL_STATSQLINE,
    RPL_ENDOFSERVICES,
    RPL_SERVLIST,
    RPL_KILLDONE,
    RPL_CLOSEEND,
    RPL_MYPORTIS,
    ERR_BADCHANMASK,
    ERR_YOUWILLBEBANNED,
    ERR_NOSERVICEHOST,
])

# CTCP codes (these are not in the RFC)
CTCP_VERSION = 'CTCP_VERSION'
CTCP_PING = 'CTCP_PING'
CTCP_TIME = 'CTCP_TIME'
CTCP_SOURCE = 'CTCP_SOURCE'
CTCP = set([
    CTCP_VERSION,
    CTCP_PING,
    CTCP_TIME,
    CTCP_SOURCE,
])

# Others:
PRIVMSG = 'PRIVMSG'
PING = 'PING'
NOTICE = 'NOTICE'
JOIN = 'JOIN'
PART = 'PART'
MODE = 'MODE'
KICK = 'KICK'
QUIT = 'QUIT'
OTHERS = set([
    PRIVMSG,
    PING,
    NOTICE,
    JOIN,
    PART,
    MODE,
    KICK,
    QUIT,
])

ALL_CODES = ERRORS | RESPONSES | RESERVED | CTCP | OTHERS


class UnknownCode(object):
    def __init__(self, known_codes):
        self.known_codes = set(known_codes)

    def __eq__(self, other):
        return other not in self.known_codes

    def __ne__(self, other):
        return other in self.known_codes


UNKNOWN_CODE = UnknownCode(ALL_CODES)
