#!/usr/bin/env python
# -*- coding: utf-8 -*-
#~#######################################################################
#~ Copyright (c) 2014 Dmitry Poltavchenko <admin@linuxhub.ru            #
#~                                                                      #
#~ This file is part of FreQ-bot.                                       #
#~                                                                      #
#~ FreQ-bot is free software: you can redistribute it and/or modify     #
#~ it under the terms of the GNU General Public License as published by #
#~ the Free Software Foundation, either version 3 of the License, or    #
#~ (at your option) any later version.                                  #
#~                                                                      #
#~ FreQ-bot is distributed in the hope that it will be useful,          #
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#~ GNU General Public License for more details.                         #
#~                                                                      #
#~ You should have received a copy of the GNU General Public License    #
#~ along with FreQ-bot.  If not, see <http://www.gnu.org/licenses/>.    #
#~#######################################################################

#by zen

import random
from twisted.words.protocols.jabber import jid


PHRASES=[
 u'/me совершил "расправу" над {0} путем установки винды!',
 u'/me подбил глаз и отнял калвиатуру у {0}',
 u'/me вырубил пользователя {0} веслом по голове. {0} очнется минут через 10...',
 u'/me узнал где живет {0} и коварно улыбается...',
 u'/me вызвал гром и молнию на голову пользователя {0}',
 u'/me рекомендует книгу "Начинающий пользователь ПК" для {0}',
 u'/me решил, что парад для {0} на сегодня отменяется',
 u'/me отправил {0} читать гугл',
 u'/me взялся за терминал: sudo su - -c "{0} -- Сделай мне сэндвич!"',
]

LAST=''
STRING=''

def get_jid(source, p):
 if p:
  if source.room:
   if p in source.room.items.keys():
    return source.room[p].jid
   else: return p
  else: return p
 else: return source.jid

def bump_msg(t,s,p):
 global LAST
 global STRING
 while ( STRING==LAST or LAST=='' ):
  STRING=random.choice(PHRASES)
  if len(PHRASES) < 2:
   break
  elif STRING!=LAST:
   LAST=STRING
   break
 nick = p.strip('\r\n ')
 jid = get_jid(s, nick)
 if s.room:
  if nick == jid: s.room.msg(u'Здесь таких нет!')
  elif s.room.bot and (s.room.bot.jid==jid): s.room.msg(u'Не смешная шутка!')
  elif s.jid == jid and nick != "": s.room.msg(nick + u', ты в своем уме?')
  elif s.jid != jid: s.room.msg(STRING.format(nick))
  else: s.room.msg(u'Кого будем троллить?')
 else:
  s.msg(u'Данная команда работает только внутри конференции')

bot.register_cmd_handler(bump_msg, u'.bump', 0, True)

