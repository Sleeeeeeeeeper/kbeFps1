# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GameConfigs

TIMER_TYPE_DESTROY = 1

class Avatar(KBEngine.Proxy):

    def __init__(self):
        KBEngine.Proxy.__init__(self)

        self.cellData["name"] = "Ori" + str(self.id)
        self.cellData["position"] = (0.0, 0.0, 0.0)
        self.cellData["health"] = 100
        self._destroyTimer = 0

    def createCell(self, space, roomKey):
        self.roomKey = roomKey
        self.createCellEntity(space)

    def onClientEnabled(self):
        if self._destroyTimer > 0:
            self.delTimer(self._destroyTimer)
            self._destroyTimer = 0
        
        if self.cell is None:
            self.cellData["position"] = (0.0, 0.0, 0.0)
            self.cellData["moveVelocity"] = (0.0, 0.0, 0.0)
            KBEngine.globalData["Halls"].enterRoom(self, self.cellData["position"], self.cellData["direction"], self.roomKey)

    def onTimer(self, id, userArg):
        if TIMER_TYPE_DESTROY == userArg:
            self.onDestroyTimer()

    def destroySelf(self):
        if self.client is not None:
            return
        if self.cell is not None:
            self.destroyCellEntity()
            return

        KBEngine.globalData["Halls"].leaveRoom(self.id, self.roomKey)
        # destroy base
        self.destroy()
        self._destroyTimer = 0

    def onGetCell(self):
        DEBUG_MSG('Avatar::onGetCell: %s' % self.cell)

    def onLoseCell(self):
        if self._destroyTimer > 0:
            self.destroySelf()

    def onClientDeath(self):
        DEBUG_MSG("Avatar[%i].onClientDeath:" % self.id)
        self.destroySelf()
        #self._destroyTimer = self.addTimer(15, 0, TIMER_TYPE_DESTROY)

    def onDestroyTimer(self):   
        self.destroySelf()

    def onLogOnAttempt(self, ip, port, password):
        INFO_MSG(ip, port, password)
        return KBEngine.LOG_ON_ACCEPT
    
    