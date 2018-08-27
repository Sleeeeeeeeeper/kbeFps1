# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Avatar(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.getCurrRoom().onEnter(self)

    def onGetWitness(self):
        DEBUG_MSG("Avatar::onGetWitness: %i." % self.id)

    def onLoseWitness(self):
        DEBUG_MSG("Avatar::onLoseWitness: %i." % self.id)

    def onDestroy(self):
        
        DEBUG_MSG("Avatar::onDestroy: %i." % self.id)
        room = self.getCurrRoom()
        if room:
            room.onLeave(self.id)


    def getCurrRoom(self):
        roomBase = self.getCurrRoomBase()
        if roomBase is None:
            return roomBase
        return KBEngine.entities.get(roomBase.id, None)

    def getCurrRoomBase(self):
        return KBEngine.globalData.get("Room_%i" % self.spaceID)
    
    def sendVelocity(self, exposed, moveVelocity):
        if exposed != self.id:
            return
        self.moveVelocity = moveVelocity


    def sendPakeageData(self,exposed,vec1,vec2,vec3,vec4,vec5,float1,float2,float3,float4,float5,int1,int2,int3,int4,int5):
        if exposed != self.id:
            return
        self.vec1=vec1
        self.vec2=vec2
        self.vec3=vec3
        self.vec4=vec4
        self.vec5=vec5
        self.float1=float1
        self.float2=float2
        self.float3=float3
        self.float4=float4
        self.float5=float5
        self.int1=int1
        self.int2=int2
        self.int3=int3
        self.int4=int4
        self.int5=int5

    def sendRepMovementData(self,exposed,bpressedJump,bwannaCrouch,bforceMaxAccel,bforceNoCombine,boldTimeStampBeforeReset,timeStamp,deltaTime,cusTimeDilation,jumpKeyHoldTime,jumpMaxCount,jumpCurrentCount,movementMode,startLoc,startRelaLoc,startVel,startRot,startControlRot,startBaseRot4d,startCapRadius,startCapHalfHeight,startBoneName,savedLoc,savedRot,savedVel,savedRelaLoc,savedControlRot,endBoneName,acceleration,accelNormal,accelMag,accelDotThreshold,accelMagThreshold,accelDotThresholdCombine):
        if exposed != self.id:
            return
        self.bpressedJump=bpressedJump
        self.bwannaCrouch=bwannaCrouch
        self.bforceMaxAccel=bforceMaxAccel
        self.bforceNoCombine=bforceNoCombine
        self.boldTimeStampBeforeReset=boldTimeStampBeforeReset
        self.timeStamp=timeStamp
        self.deltaTime=deltaTime
        self.cusTimeDilation=cusTimeDilation
        self.jumpKeyHoldTime=jumpKeyHoldTime
        self.jumpMaxCount=jumpMaxCount
        self.jumpCurrentCount=jumpCurrentCount
        self.movementMode=movementMode
        self.startLoc=startLoc
        self.startRelaLoc=startRelaLoc
        self.startVel=startVel
        self.startRot=startRot
        self.startControlRot=startControlRot
        self.startBaseRot4d=startBaseRot4d
        self.startCapRadius=startCapRadius
        self.startCapHalfHeight=startCapHalfHeight
        self.startBoneName=startBoneName
        self.savedLoc=savedLoc
        self.savedRot=savedRot
        self.savedVel=savedVel
        self.savedRelaLoc=savedRelaLoc
        self.savedControlRot=savedControlRot
        self.endBoneName=endBoneName
        self.acceleration=acceleration
        self.accelNormal=accelNormal
        self.accelMag=accelMag
        self.accelDotThreshold=accelDotThreshold
        self.accelMagThreshold=accelMagThreshold
        self.accelDotThresholdCombine=accelDotThresholdCombine