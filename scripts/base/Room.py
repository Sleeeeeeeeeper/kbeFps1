# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
class Room(KBEngine.Entity):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        
        self.cellData["roomKeyC"] = self.roomKey

        self.createCellEntityInNewSpace(None)
        self.avatars = {}

    def enterRoom(self, entityCall, position, direction):
        entityCall.createCell(self.cell, self.roomKey)
        self.onEnter(entityCall)

    def leaveRoom(self, entityID):
        self.onLeave(entityID)

    def onTimer(self, tid, userArg):
        pass

    def onEnter(self, entityCall):
        self.avatars[entityCall.id] = entityCall

    def onLeave(self, entityID):
        if entityID in self.avatars:
            del self.avatars[entityID]

    def onLoseCell(self):
        KBEngine.globalData["Halls"].onRoomLoseCell(self.roomKey)
        self.avatars = {}
        self.destroy()

    def onGetCell(self):
        DEBUG_MSG("Room::onGetCell: %i" % self.id)
        KBEngine.globalData["Halls"].onRoomGetCell(self, self.roomKey)

    
