# -*- coding: utf-8 -*-

import KBEngine
from KBEDebug import *
import GameConfigs
import random

TIMER_TYPE_DESTROY = 1
class Room(KBEngine.Entity):

    def __init__(self):
        KBEngine.Entity.__init__(self)

        self.position = (999999.0, 0.0, 0.0)
        self.avatars = {}
        #tell client to load map
        #KBEngine.addSpaceGeometryMapping(self.spaceID, None, "spaces/gameMap")
        #DEBUG_MSG('created space[%d] entityID = %i, res = %s.' % (self.roomKeyC, self.id, "spaces/gameMap"))

        KBEngine.globalData["Room_%i" % self.spaceID] = self.base

        #set data, client can get it
        KBEngine.setSpaceData(self.spaceID, "GAME_ROUND_TIME", str(GameConfigs.GAME_ROUND_TIME))
        #self._destroyTimer = self.addTimer(GameConfigs.GAME_ROUND_TIME, 0, TIMER_TYPE_DESTROY)

    def onEnter(self, entityCall):

        DEBUG_MSG('Room::onEnter space[%d] entityID = %i.' % (self.spaceID, entityCall.id))
        self.avatars[entityCall.id] = entityCall

    def onLeave(self, entityID):

        DEBUG_MSG('Room::onLeave space[%d] entityID = %i.' % (self.spaceID, entityID))
        if entityID in self.avatars:
            del self.avatars[entityID]

    def onTimer(self, id, userArg):
        if TIMER_TYPE_DESTROY == userArg:
            self.onDestroyTimer()

    def onDestroy(self):
        DEBUG_MSG("Room::onDestroy: %i" % (self.id))
        del KBEngine.globalData["Room_%i" % self.spaceID]

    def onDestroyTimer(self):
        DEBUG_MSG("Room::onDestroyTimer: %i" % (self.id))
        self.destroySpace()