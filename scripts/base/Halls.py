
# -*- coding: utf-8 -*-
import KBEngine
import Functor
from KBEDebug import *
import traceback
import GameConfigs

FIND_ROOM_NOT_FOUND = 0
FIND_ROOM_CREATING = 1

class Halls(KBEngine.Entity):

    def __init__(self):
        KBEngine.Entity.__init__(self)
        KBEngine.globalData["Halls"] = self

        self.rooms = {}
        self.lastNewRoomKey = 0

    def findRoom(self, roomKey, notFoundCreate = False):

        roomDatas = self.rooms.get(roomKey)

        if not roomDatas:
            if not notFoundCreate:
                return FIND_ROOM_NOT_FOUND
            
            roomDatas = self.rooms.get(self.lastNewRoomKey)
            if roomDatas is not None:
                return roomDatas

            self.lastNewRoomKey = KBEngine.genUUID64()

            KBEngine.createEntityAnywhere("Room", \
                                        {"roomKey" : self.lastNewRoomKey,}, \
                                        Functor.Functor(self.onRoomCreatedCB, self.lastNewRoomKey))
            roomDatas = {"roomEntityCall":None, "PlayerCount": 0, "enterRoomReqs" : [], "roomKey" : self.lastNewRoomKey}
            self.rooms[self.lastNewRoomKey] = roomDatas
            return roomDatas
        
        return roomDatas

    def enterRoom(self, entityCall, position, direction, roomKey):

        roomDatas = self.findRoom(roomKey, True)
        roomDatas["PlayerCount"] += 1
        roomEntityCall = roomDatas["roomEntityCall"]

        if roomEntityCall is not None:
            roomEntityCall.enterRoom(entityCall, position, direction)
        else:
            DEBUG_MSG("Halls::enterRoom: space %i creating..., enter entityID=%i" % (roomDatas["roomKey"], entityCall.id))
            roomDatas["enterRoomReqs"].append((entityCall, position, direction))


    def leaveRoom(self, avatarID, roomKey):

        roomDatas = self.findRoom(roomKey, False)

        if type(roomDatas) is dict:
            roomEntityCall = roomDatas["roomEntityCall"]
            if roomEntityCall:
                roomEntityCall.leaveRoom(avatarID)
        else :
            if roomDatas == FIND_ROOM_CREATING:
                raise Exception("FIND_ROOM_CREATING")

    #---
    #Callback
    #--
    def onTimer(self, tid, userArg):
        pass
        
    def onRoomCreatedCB(self, roomKey, roomEntityCall):
        pass

    def onRoomLoseCell(self, roomKey):
        del self.rooms[roomKey]

    def onRoomGetCell(self, roomEntityCall, roomKey):

        self.rooms[roomKey]["roomEntityCall"] = roomEntityCall

        for infos in self.rooms[roomKey]["enterRoomReqs"]:
            entityCall = infos[0]
            entityCall.createCell(roomEntityCall.cell, roomKey)
        
        self.rooms[roomKey]["enterRoomReqs"] = []
    
