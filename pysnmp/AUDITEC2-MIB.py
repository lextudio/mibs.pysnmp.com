# SNMP MIB module (AUDITEC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AUDITEC2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:23 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

auditec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1774)
)
auditec.setRevisions(
        ("2001-11-23 10:00",
         "2001-12-11 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Probe_ObjectIdentity = ObjectIdentity
probe = _Probe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1774, 1)
)


class _PrbIpAddr_Type(DisplayString):
    """Custom type prbIpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PrbIpAddr_Type.__name__ = "DisplayString"
_PrbIpAddr_Object = MibScalar
prbIpAddr = _PrbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 1),
    _PrbIpAddr_Type()
)
prbIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbIpAddr.setStatus("mandatory")


class _PrbState_Type(Integer32):
    """Custom type prbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 0),
          ("suspended", 3),
          ("waiting", 1))
    )


_PrbState_Type.__name__ = "Integer32"
_PrbState_Object = MibScalar
prbState = _PrbState_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 2),
    _PrbState_Type()
)
prbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbState.setStatus("mandatory")


class _PrbBasePath_Type(DisplayString):
    """Custom type prbBasePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_PrbBasePath_Type.__name__ = "DisplayString"
_PrbBasePath_Object = MibScalar
prbBasePath = _PrbBasePath_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 3),
    _PrbBasePath_Type()
)
prbBasePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbBasePath.setStatus("mandatory")


class _PrbGrpList_Type(DisplayString):
    """Custom type prbGrpList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_PrbGrpList_Type.__name__ = "DisplayString"
_PrbGrpList_Object = MibScalar
prbGrpList = _PrbGrpList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 4),
    _PrbGrpList_Type()
)
prbGrpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbGrpList.setStatus("mandatory")


class _PrbServerConnection_Type(Integer32):
    """Custom type prbServerConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("disconnected", 2),
          ("notConfigured", 1))
    )


_PrbServerConnection_Type.__name__ = "Integer32"
_PrbServerConnection_Object = MibScalar
prbServerConnection = _PrbServerConnection_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 5),
    _PrbServerConnection_Type()
)
prbServerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbServerConnection.setStatus("mandatory")
_PrbDiffGMT_Type = Integer32
_PrbDiffGMT_Object = MibScalar
prbDiffGMT = _PrbDiffGMT_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 6),
    _PrbDiffGMT_Type()
)
prbDiffGMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbDiffGMT.setStatus("mandatory")
_PrbNewtestMemory_Type = Integer32
_PrbNewtestMemory_Object = MibScalar
prbNewtestMemory = _PrbNewtestMemory_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 7),
    _PrbNewtestMemory_Type()
)
prbNewtestMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbNewtestMemory.setStatus("mandatory")
_PrbGrpStartTime_Type = TimeTicks
_PrbGrpStartTime_Object = MibScalar
prbGrpStartTime = _PrbGrpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 8),
    _PrbGrpStartTime_Type()
)
prbGrpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbGrpStartTime.setStatus("mandatory")
_PrbLastHeartBeat_Type = TimeTicks
_PrbLastHeartBeat_Object = MibScalar
prbLastHeartBeat = _PrbLastHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 1774, 1, 9),
    _PrbLastHeartBeat_Type()
)
prbLastHeartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prbLastHeartBeat.setStatus("mandatory")
_Action_ObjectIdentity = ObjectIdentity
action = _Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1774, 2)
)


class _ActType_Type(Integer32):
    """Custom type actType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(230,
              231,
              232,
              234,
              238,
              239,
              240,
              241,
              242,
              243)
        )
    )
    namedValues = NamedValues(
        *(("ackAlm", 238),
          ("changeGroup", 234),
          ("reboot", 232),
          ("resume", 231),
          ("resumeSce", 241),
          ("runSce", 239),
          ("startGroup", 243),
          ("stopGroup", 242),
          ("suspend", 230),
          ("suspendSce", 240))
    )


_ActType_Type.__name__ = "Integer32"
_ActType_Object = MibScalar
actType = _ActType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 2, 1),
    _ActType_Type()
)
actType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actType.setStatus("mandatory")


class _ActParam_Type(DisplayString):
    """Custom type actParam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ActParam_Type.__name__ = "DisplayString"
_ActParam_Object = MibScalar
actParam = _ActParam_Object(
    (1, 3, 6, 1, 4, 1, 1774, 2, 2),
    _ActParam_Type()
)
actParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actParam.setStatus("mandatory")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1774, 3)
)


class _AlmSce_Type(DisplayString):
    """Custom type almSce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_AlmSce_Type.__name__ = "DisplayString"
_AlmSce_Object = MibScalar
almSce = _AlmSce_Object(
    (1, 3, 6, 1, 4, 1, 1774, 3, 1),
    _AlmSce_Type()
)
almSce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almSce.setStatus("mandatory")


class _AlmMsg_Type(DisplayString):
    """Custom type almMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_AlmMsg_Type.__name__ = "DisplayString"
_AlmMsg_Object = MibScalar
almMsg = _AlmMsg_Object(
    (1, 3, 6, 1, 4, 1, 1774, 3, 2),
    _AlmMsg_Type()
)
almMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almMsg.setStatus("mandatory")


class _AlmCode_Type(DisplayString):
    """Custom type almCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_AlmCode_Type.__name__ = "DisplayString"
_AlmCode_Object = MibScalar
almCode = _AlmCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 3, 3),
    _AlmCode_Type()
)
almCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almCode.setStatus("mandatory")
_AlmLevel_Type = Integer32
_AlmLevel_Object = MibScalar
almLevel = _AlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 1774, 3, 4),
    _AlmLevel_Type()
)
almLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almLevel.setStatus("mandatory")


class _AlmOrd_Type(DisplayString):
    """Custom type almOrd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_AlmOrd_Type.__name__ = "DisplayString"
_AlmOrd_Object = MibScalar
almOrd = _AlmOrd_Object(
    (1, 3, 6, 1, 4, 1, 1774, 3, 5),
    _AlmOrd_Type()
)
almOrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almOrd.setStatus("mandatory")
_Group_ObjectIdentity = ObjectIdentity
group = _Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1774, 4)
)


class _GrpName_Type(DisplayString):
    """Custom type grpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_GrpName_Type.__name__ = "DisplayString"
_GrpName_Object = MibScalar
grpName = _GrpName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 1),
    _GrpName_Type()
)
grpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grpName.setStatus("mandatory")


class _GrpNbQueue_Type(Integer32):
    """Custom type grpNbQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GrpNbQueue_Type.__name__ = "Integer32"
_GrpNbQueue_Object = MibScalar
grpNbQueue = _GrpNbQueue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 2),
    _GrpNbQueue_Type()
)
grpNbQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grpNbQueue.setStatus("mandatory")
_GrpNextTime_Type = TimeTicks
_GrpNextTime_Object = MibScalar
grpNextTime = _GrpNextTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 3),
    _GrpNextTime_Type()
)
grpNextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grpNextTime.setStatus("mandatory")
_GrpQueueList_Object = MibTable
grpQueueList = _GrpQueueList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4)
)
if mibBuilder.loadTexts:
    grpQueueList.setStatus("mandatory")
_Queue_Object = MibTableRow
queue = _Queue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4, 1)
)
queue.setIndexNames(
    (0, "AUDITEC2-MIB", "queIndex"),
)
if mibBuilder.loadTexts:
    queue.setStatus("mandatory")
_QueIndex_Type = Integer32
_QueIndex_Object = MibTableColumn
queIndex = _QueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4, 1, 1),
    _QueIndex_Type()
)
queIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queIndex.setStatus("mandatory")


class _QueName_Type(DisplayString):
    """Custom type queName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_QueName_Type.__name__ = "DisplayString"
_QueName_Object = MibTableColumn
queName = _QueName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4, 1, 2),
    _QueName_Type()
)
queName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queName.setStatus("mandatory")


class _QueType_Type(Integer32):
    """Custom type queType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("user", 1))
    )


_QueType_Type.__name__ = "Integer32"
_QueType_Object = MibTableColumn
queType = _QueType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4, 1, 3),
    _QueType_Type()
)
queType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queType.setStatus("mandatory")
_QueNbSce_Type = Integer32
_QueNbSce_Object = MibTableColumn
queNbSce = _QueNbSce_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 4, 1, 4),
    _QueNbSce_Type()
)
queNbSce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queNbSce.setStatus("mandatory")
_GrpSceList_Object = MibTable
grpSceList = _GrpSceList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5)
)
if mibBuilder.loadTexts:
    grpSceList.setStatus("mandatory")
_Scenario_Object = MibTableRow
scenario = _Scenario_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1)
)
scenario.setIndexNames(
    (0, "AUDITEC2-MIB", "sceQueIndex"),
    (0, "AUDITEC2-MIB", "sceIndex"),
)
if mibBuilder.loadTexts:
    scenario.setStatus("mandatory")
_SceIndex_Type = Integer32
_SceIndex_Object = MibTableColumn
sceIndex = _SceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 1),
    _SceIndex_Type()
)
sceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceIndex.setStatus("mandatory")
_SceQueIndex_Type = Integer32
_SceQueIndex_Object = MibTableColumn
sceQueIndex = _SceQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 2),
    _SceQueIndex_Type()
)
sceQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceQueIndex.setStatus("mandatory")


class _SceName_Type(DisplayString):
    """Custom type sceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_SceName_Type.__name__ = "DisplayString"
_SceName_Object = MibTableColumn
sceName = _SceName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 3),
    _SceName_Type()
)
sceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceName.setStatus("mandatory")


class _SceType_Type(Integer32):
    """Custom type sceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("service", 1),
          ("user", 0))
    )


_SceType_Type.__name__ = "Integer32"
_SceType_Object = MibTableColumn
sceType = _SceType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 4),
    _SceType_Type()
)
sceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceType.setStatus("mandatory")


class _SceUnavailObj_Type(Integer32):
    """Custom type sceUnavailObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SceUnavailObj_Type.__name__ = "Integer32"
_SceUnavailObj_Object = MibTableColumn
sceUnavailObj = _SceUnavailObj_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 5),
    _SceUnavailObj_Type()
)
sceUnavailObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceUnavailObj.setStatus("mandatory")


class _SceState_Type(Integer32):
    """Custom type sceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("ok", 0),
          ("suspended", 4),
          ("unavailable", 1))
    )


_SceState_Type.__name__ = "Integer32"
_SceState_Object = MibTableColumn
sceState = _SceState_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 6),
    _SceState_Type()
)
sceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceState.setStatus("mandatory")
_SceNbExec_Type = Counter32
_SceNbExec_Object = MibTableColumn
sceNbExec = _SceNbExec_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 7),
    _SceNbExec_Type()
)
sceNbExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceNbExec.setStatus("mandatory")
_SceNbUnAvailExec_Type = Counter32
_SceNbUnAvailExec_Object = MibTableColumn
sceNbUnAvailExec = _SceNbUnAvailExec_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 8),
    _SceNbUnAvailExec_Type()
)
sceNbUnAvailExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceNbUnAvailExec.setStatus("mandatory")
_SceStartTime_Type = TimeTicks
_SceStartTime_Object = MibTableColumn
sceStartTime = _SceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 9),
    _SceStartTime_Type()
)
sceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceStartTime.setStatus("mandatory")
_SceAccumulationMeasureDuration_Type = Counter32
_SceAccumulationMeasureDuration_Object = MibTableColumn
sceAccumulationMeasureDuration = _SceAccumulationMeasureDuration_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 10),
    _SceAccumulationMeasureDuration_Type()
)
sceAccumulationMeasureDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceAccumulationMeasureDuration.setStatus("mandatory")
_SceAccumulationUnavailDuration_Type = Counter32
_SceAccumulationUnavailDuration_Object = MibTableColumn
sceAccumulationUnavailDuration = _SceAccumulationUnavailDuration_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 11),
    _SceAccumulationUnavailDuration_Type()
)
sceAccumulationUnavailDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceAccumulationUnavailDuration.setStatus("mandatory")
_SceNbOrd_Type = Integer32
_SceNbOrd_Object = MibTableColumn
sceNbOrd = _SceNbOrd_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 12),
    _SceNbOrd_Type()
)
sceNbOrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceNbOrd.setStatus("mandatory")


class _SceState2_Type(Integer32):
    """Custom type sceState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("outOfRange", 2),
          ("suspended", 4),
          ("unavailable", 8))
    )


_SceState2_Type.__name__ = "Integer32"
_SceState2_Object = MibTableColumn
sceState2 = _SceState2_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 5, 1, 13),
    _SceState2_Type()
)
sceState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceState2.setStatus("mandatory")
_GrpOrdList_Object = MibTable
grpOrdList = _GrpOrdList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6)
)
if mibBuilder.loadTexts:
    grpOrdList.setStatus("mandatory")
_Order_Object = MibTableRow
order = _Order_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1)
)
order.setIndexNames(
    (0, "AUDITEC2-MIB", "ordQueIndex"),
    (0, "AUDITEC2-MIB", "ordSceIndex"),
    (0, "AUDITEC2-MIB", "ordIndex"),
)
if mibBuilder.loadTexts:
    order.setStatus("mandatory")
_OrdIndex_Type = Integer32
_OrdIndex_Object = MibTableColumn
ordIndex = _OrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 1),
    _OrdIndex_Type()
)
ordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordIndex.setStatus("mandatory")
_OrdSceIndex_Type = Integer32
_OrdSceIndex_Object = MibTableColumn
ordSceIndex = _OrdSceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 2),
    _OrdSceIndex_Type()
)
ordSceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordSceIndex.setStatus("mandatory")
_OrdQueIndex_Type = Integer32
_OrdQueIndex_Object = MibTableColumn
ordQueIndex = _OrdQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 3),
    _OrdQueIndex_Type()
)
ordQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordQueIndex.setStatus("mandatory")


class _OrdName_Type(DisplayString):
    """Custom type ordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdName_Type.__name__ = "DisplayString"
_OrdName_Object = MibTableColumn
ordName = _OrdName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 4),
    _OrdName_Type()
)
ordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordName.setStatus("mandatory")


class _OrdType_Type(Integer32):
    """Custom type ordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("num", 2),
          ("tps", 0))
    )


_OrdType_Type.__name__ = "Integer32"
_OrdType_Object = MibTableColumn
ordType = _OrdType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 5),
    _OrdType_Type()
)
ordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordType.setStatus("mandatory")


class _OrdObjNbRef_Type(Integer32):
    """Custom type ordObjNbRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OrdObjNbRef_Type.__name__ = "Integer32"
_OrdObjNbRef_Object = MibTableColumn
ordObjNbRef = _OrdObjNbRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 6),
    _OrdObjNbRef_Type()
)
ordObjNbRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordObjNbRef.setStatus("mandatory")


class _OrdRef_Type(Integer32):
    """Custom type ordRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdRef_Type.__name__ = "Integer32"
_OrdRef_Object = MibTableColumn
ordRef = _OrdRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 7),
    _OrdRef_Type()
)
ordRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordRef.setStatus("mandatory")
_OrdAccumulationNbRef_Type = Counter32
_OrdAccumulationNbRef_Object = MibTableColumn
ordAccumulationNbRef = _OrdAccumulationNbRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 8),
    _OrdAccumulationNbRef_Type()
)
ordAccumulationNbRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNbRef.setStatus("mandatory")


class _OrdCoef_Type(Integer32):
    """Custom type ordCoef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdCoef_Type.__name__ = "Integer32"
_OrdCoef_Object = MibTableColumn
ordCoef = _OrdCoef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 9),
    _OrdCoef_Type()
)
ordCoef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordCoef.setStatus("mandatory")


class _OrdUnit_Type(DisplayString):
    """Custom type ordUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdUnit_Type.__name__ = "DisplayString"
_OrdUnit_Object = MibTableColumn
ordUnit = _OrdUnit_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 10),
    _OrdUnit_Type()
)
ordUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordUnit.setStatus("mandatory")


class _OrdMin_Type(Integer32):
    """Custom type ordMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdMin_Type.__name__ = "Integer32"
_OrdMin_Object = MibTableColumn
ordMin = _OrdMin_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 11),
    _OrdMin_Type()
)
ordMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordMin.setStatus("mandatory")


class _OrdMax_Type(Integer32):
    """Custom type ordMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdMax_Type.__name__ = "Integer32"
_OrdMax_Object = MibTableColumn
ordMax = _OrdMax_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 12),
    _OrdMax_Type()
)
ordMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordMax.setStatus("mandatory")
_OrdAccumulation_Type = Counter32
_OrdAccumulation_Object = MibTableColumn
ordAccumulation = _OrdAccumulation_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 13),
    _OrdAccumulation_Type()
)
ordAccumulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulation.setStatus("mandatory")


class _OrdAverage6_Type(Integer32):
    """Custom type ordAverage6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdAverage6_Type.__name__ = "Integer32"
_OrdAverage6_Object = MibTableColumn
ordAverage6 = _OrdAverage6_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 14),
    _OrdAverage6_Type()
)
ordAverage6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAverage6.setStatus("mandatory")
_OrdNbSamples_Type = Counter32
_OrdNbSamples_Object = MibTableColumn
ordNbSamples = _OrdNbSamples_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 15),
    _OrdNbSamples_Type()
)
ordNbSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordNbSamples.setStatus("mandatory")


class _OrdThreashold1_Type(Integer32):
    """Custom type ordThreashold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdThreashold1_Type.__name__ = "Integer32"
_OrdThreashold1_Object = MibTableColumn
ordThreashold1 = _OrdThreashold1_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 16),
    _OrdThreashold1_Type()
)
ordThreashold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordThreashold1.setStatus("mandatory")


class _OrdThreashold2_Type(Integer32):
    """Custom type ordThreashold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdThreashold2_Type.__name__ = "Integer32"
_OrdThreashold2_Object = MibTableColumn
ordThreashold2 = _OrdThreashold2_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 17),
    _OrdThreashold2_Type()
)
ordThreashold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordThreashold2.setStatus("mandatory")


class _OrdThreashold3_Type(Integer32):
    """Custom type ordThreashold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdThreashold3_Type.__name__ = "Integer32"
_OrdThreashold3_Object = MibTableColumn
ordThreashold3 = _OrdThreashold3_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 18),
    _OrdThreashold3_Type()
)
ordThreashold3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordThreashold3.setStatus("mandatory")


class _OrdThreashold4_Type(Integer32):
    """Custom type ordThreashold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdThreashold4_Type.__name__ = "Integer32"
_OrdThreashold4_Object = MibTableColumn
ordThreashold4 = _OrdThreashold4_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 19),
    _OrdThreashold4_Type()
)
ordThreashold4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordThreashold4.setStatus("mandatory")
_OrdAccumulationNb1_Type = Counter32
_OrdAccumulationNb1_Object = MibTableColumn
ordAccumulationNb1 = _OrdAccumulationNb1_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 20),
    _OrdAccumulationNb1_Type()
)
ordAccumulationNb1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNb1.setStatus("mandatory")
_OrdAccumulationNb2_Type = Counter32
_OrdAccumulationNb2_Object = MibTableColumn
ordAccumulationNb2 = _OrdAccumulationNb2_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 21),
    _OrdAccumulationNb2_Type()
)
ordAccumulationNb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNb2.setStatus("mandatory")
_OrdAccumulationNb3_Type = Counter32
_OrdAccumulationNb3_Object = MibTableColumn
ordAccumulationNb3 = _OrdAccumulationNb3_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 22),
    _OrdAccumulationNb3_Type()
)
ordAccumulationNb3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNb3.setStatus("mandatory")
_OrdAccumulationNb4_Type = Counter32
_OrdAccumulationNb4_Object = MibTableColumn
ordAccumulationNb4 = _OrdAccumulationNb4_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 23),
    _OrdAccumulationNb4_Type()
)
ordAccumulationNb4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNb4.setStatus("mandatory")
_OrdAccumulationNb5_Type = Counter32
_OrdAccumulationNb5_Object = MibTableColumn
ordAccumulationNb5 = _OrdAccumulationNb5_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 24),
    _OrdAccumulationNb5_Type()
)
ordAccumulationNb5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordAccumulationNb5.setStatus("mandatory")
_OrdNbUnavail_Type = Counter32
_OrdNbUnavail_Object = MibTableColumn
ordNbUnavail = _OrdNbUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 25),
    _OrdNbUnavail_Type()
)
ordNbUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordNbUnavail.setStatus("mandatory")
_OrdTime_Type = TimeTicks
_OrdTime_Object = MibTableColumn
ordTime = _OrdTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 26),
    _OrdTime_Type()
)
ordTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordTime.setStatus("mandatory")


class _OrdValue_Type(Integer32):
    """Custom type ordValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdValue_Type.__name__ = "Integer32"
_OrdValue_Object = MibTableColumn
ordValue = _OrdValue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 27),
    _OrdValue_Type()
)
ordValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordValue.setStatus("mandatory")


class _OrdErrCode_Type(DisplayString):
    """Custom type ordErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdErrCode_Type.__name__ = "DisplayString"
_OrdErrCode_Object = MibTableColumn
ordErrCode = _OrdErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 28),
    _OrdErrCode_Type()
)
ordErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordErrCode.setStatus("mandatory")
_OrdPrev1Time_Type = TimeTicks
_OrdPrev1Time_Object = MibTableColumn
ordPrev1Time = _OrdPrev1Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 29),
    _OrdPrev1Time_Type()
)
ordPrev1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev1Time.setStatus("mandatory")


class _OrdPrev1Value_Type(Integer32):
    """Custom type ordPrev1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdPrev1Value_Type.__name__ = "Integer32"
_OrdPrev1Value_Object = MibTableColumn
ordPrev1Value = _OrdPrev1Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 30),
    _OrdPrev1Value_Type()
)
ordPrev1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev1Value.setStatus("mandatory")


class _OrdPrev1ErrCode_Type(DisplayString):
    """Custom type ordPrev1ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdPrev1ErrCode_Type.__name__ = "DisplayString"
_OrdPrev1ErrCode_Object = MibTableColumn
ordPrev1ErrCode = _OrdPrev1ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 31),
    _OrdPrev1ErrCode_Type()
)
ordPrev1ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev1ErrCode.setStatus("mandatory")
_OrdPrev2Time_Type = TimeTicks
_OrdPrev2Time_Object = MibTableColumn
ordPrev2Time = _OrdPrev2Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 32),
    _OrdPrev2Time_Type()
)
ordPrev2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev2Time.setStatus("mandatory")


class _OrdPrev2Value_Type(Integer32):
    """Custom type ordPrev2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdPrev2Value_Type.__name__ = "Integer32"
_OrdPrev2Value_Object = MibTableColumn
ordPrev2Value = _OrdPrev2Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 33),
    _OrdPrev2Value_Type()
)
ordPrev2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev2Value.setStatus("mandatory")


class _OrdPrev2ErrCode_Type(DisplayString):
    """Custom type ordPrev2ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdPrev2ErrCode_Type.__name__ = "DisplayString"
_OrdPrev2ErrCode_Object = MibTableColumn
ordPrev2ErrCode = _OrdPrev2ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 34),
    _OrdPrev2ErrCode_Type()
)
ordPrev2ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev2ErrCode.setStatus("mandatory")
_OrdPrev3Time_Type = TimeTicks
_OrdPrev3Time_Object = MibTableColumn
ordPrev3Time = _OrdPrev3Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 35),
    _OrdPrev3Time_Type()
)
ordPrev3Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev3Time.setStatus("mandatory")


class _OrdPrev3Value_Type(Integer32):
    """Custom type ordPrev3Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdPrev3Value_Type.__name__ = "Integer32"
_OrdPrev3Value_Object = MibTableColumn
ordPrev3Value = _OrdPrev3Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 36),
    _OrdPrev3Value_Type()
)
ordPrev3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev3Value.setStatus("mandatory")


class _OrdPrev3ErrCode_Type(DisplayString):
    """Custom type ordPrev3ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdPrev3ErrCode_Type.__name__ = "DisplayString"
_OrdPrev3ErrCode_Object = MibTableColumn
ordPrev3ErrCode = _OrdPrev3ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 37),
    _OrdPrev3ErrCode_Type()
)
ordPrev3ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev3ErrCode.setStatus("mandatory")
_OrdPrev4Time_Type = TimeTicks
_OrdPrev4Time_Object = MibTableColumn
ordPrev4Time = _OrdPrev4Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 38),
    _OrdPrev4Time_Type()
)
ordPrev4Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev4Time.setStatus("mandatory")


class _OrdPrev4Value_Type(Integer32):
    """Custom type ordPrev4Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdPrev4Value_Type.__name__ = "Integer32"
_OrdPrev4Value_Object = MibTableColumn
ordPrev4Value = _OrdPrev4Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 39),
    _OrdPrev4Value_Type()
)
ordPrev4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev4Value.setStatus("mandatory")


class _OrdPrev4ErrCode_Type(DisplayString):
    """Custom type ordPrev4ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdPrev4ErrCode_Type.__name__ = "DisplayString"
_OrdPrev4ErrCode_Object = MibTableColumn
ordPrev4ErrCode = _OrdPrev4ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 40),
    _OrdPrev4ErrCode_Type()
)
ordPrev4ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev4ErrCode.setStatus("mandatory")
_OrdPrev5Time_Type = TimeTicks
_OrdPrev5Time_Object = MibTableColumn
ordPrev5Time = _OrdPrev5Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 41),
    _OrdPrev5Time_Type()
)
ordPrev5Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev5Time.setStatus("mandatory")


class _OrdPrev5Value_Type(Integer32):
    """Custom type ordPrev5Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdPrev5Value_Type.__name__ = "Integer32"
_OrdPrev5Value_Object = MibTableColumn
ordPrev5Value = _OrdPrev5Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 42),
    _OrdPrev5Value_Type()
)
ordPrev5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev5Value.setStatus("mandatory")


class _OrdPrev5ErrCode_Type(DisplayString):
    """Custom type ordPrev5ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdPrev5ErrCode_Type.__name__ = "DisplayString"
_OrdPrev5ErrCode_Object = MibTableColumn
ordPrev5ErrCode = _OrdPrev5ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 6, 1, 43),
    _OrdPrev5ErrCode_Type()
)
ordPrev5ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordPrev5ErrCode.setStatus("mandatory")
_GrpOrdTxtList_Object = MibTable
grpOrdTxtList = _GrpOrdTxtList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7)
)
if mibBuilder.loadTexts:
    grpOrdTxtList.setStatus("mandatory")
_OrderTxt_Object = MibTableRow
orderTxt = _OrderTxt_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1)
)
orderTxt.setIndexNames(
    (0, "AUDITEC2-MIB", "otxQueIndex"),
    (0, "AUDITEC2-MIB", "otxSceIndex"),
    (0, "AUDITEC2-MIB", "otxIndex"),
)
if mibBuilder.loadTexts:
    orderTxt.setStatus("mandatory")
_OtxIndex_Type = Integer32
_OtxIndex_Object = MibTableColumn
otxIndex = _OtxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 1),
    _OtxIndex_Type()
)
otxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxIndex.setStatus("mandatory")
_OtxSceIndex_Type = Integer32
_OtxSceIndex_Object = MibTableColumn
otxSceIndex = _OtxSceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 2),
    _OtxSceIndex_Type()
)
otxSceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxSceIndex.setStatus("mandatory")
_OtxQueIndex_Type = Integer32
_OtxQueIndex_Object = MibTableColumn
otxQueIndex = _OtxQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 3),
    _OtxQueIndex_Type()
)
otxQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxQueIndex.setStatus("mandatory")


class _OtxName_Type(DisplayString):
    """Custom type otxName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxName_Type.__name__ = "DisplayString"
_OtxName_Object = MibTableColumn
otxName = _OtxName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 4),
    _OtxName_Type()
)
otxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxName.setStatus("mandatory")
_OtxNbSamples_Type = Counter32
_OtxNbSamples_Object = MibTableColumn
otxNbSamples = _OtxNbSamples_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 5),
    _OtxNbSamples_Type()
)
otxNbSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxNbSamples.setStatus("mandatory")
_OtxNbUnavail_Type = Counter32
_OtxNbUnavail_Object = MibTableColumn
otxNbUnavail = _OtxNbUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 6),
    _OtxNbUnavail_Type()
)
otxNbUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxNbUnavail.setStatus("mandatory")
_OtxTime_Type = TimeTicks
_OtxTime_Object = MibTableColumn
otxTime = _OtxTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 7),
    _OtxTime_Type()
)
otxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxTime.setStatus("mandatory")


class _OtxValue_Type(DisplayString):
    """Custom type otxValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxValue_Type.__name__ = "DisplayString"
_OtxValue_Object = MibTableColumn
otxValue = _OtxValue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 8),
    _OtxValue_Type()
)
otxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxValue.setStatus("mandatory")


class _OtxErrCode_Type(DisplayString):
    """Custom type otxErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxErrCode_Type.__name__ = "DisplayString"
_OtxErrCode_Object = MibTableColumn
otxErrCode = _OtxErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 9),
    _OtxErrCode_Type()
)
otxErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxErrCode.setStatus("mandatory")
_OtxPrev1Time_Type = TimeTicks
_OtxPrev1Time_Object = MibTableColumn
otxPrev1Time = _OtxPrev1Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 10),
    _OtxPrev1Time_Type()
)
otxPrev1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev1Time.setStatus("mandatory")


class _OtxPrev1Value_Type(DisplayString):
    """Custom type otxPrev1Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxPrev1Value_Type.__name__ = "DisplayString"
_OtxPrev1Value_Object = MibTableColumn
otxPrev1Value = _OtxPrev1Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 11),
    _OtxPrev1Value_Type()
)
otxPrev1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev1Value.setStatus("mandatory")


class _OtxPrev1ErrCode_Type(DisplayString):
    """Custom type otxPrev1ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxPrev1ErrCode_Type.__name__ = "DisplayString"
_OtxPrev1ErrCode_Object = MibTableColumn
otxPrev1ErrCode = _OtxPrev1ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 12),
    _OtxPrev1ErrCode_Type()
)
otxPrev1ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev1ErrCode.setStatus("mandatory")
_OtxPrev2Time_Type = TimeTicks
_OtxPrev2Time_Object = MibTableColumn
otxPrev2Time = _OtxPrev2Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 13),
    _OtxPrev2Time_Type()
)
otxPrev2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev2Time.setStatus("mandatory")


class _OtxPrev2Value_Type(DisplayString):
    """Custom type otxPrev2Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxPrev2Value_Type.__name__ = "DisplayString"
_OtxPrev2Value_Object = MibTableColumn
otxPrev2Value = _OtxPrev2Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 14),
    _OtxPrev2Value_Type()
)
otxPrev2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev2Value.setStatus("mandatory")


class _OtxPrev2ErrCode_Type(DisplayString):
    """Custom type otxPrev2ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxPrev2ErrCode_Type.__name__ = "DisplayString"
_OtxPrev2ErrCode_Object = MibTableColumn
otxPrev2ErrCode = _OtxPrev2ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 15),
    _OtxPrev2ErrCode_Type()
)
otxPrev2ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev2ErrCode.setStatus("mandatory")
_OtxPrev3Time_Type = TimeTicks
_OtxPrev3Time_Object = MibTableColumn
otxPrev3Time = _OtxPrev3Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 16),
    _OtxPrev3Time_Type()
)
otxPrev3Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev3Time.setStatus("mandatory")


class _OtxPrev3Value_Type(DisplayString):
    """Custom type otxPrev3Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxPrev3Value_Type.__name__ = "DisplayString"
_OtxPrev3Value_Object = MibTableColumn
otxPrev3Value = _OtxPrev3Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 17),
    _OtxPrev3Value_Type()
)
otxPrev3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev3Value.setStatus("mandatory")


class _OtxPrev3ErrCode_Type(DisplayString):
    """Custom type otxPrev3ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxPrev3ErrCode_Type.__name__ = "DisplayString"
_OtxPrev3ErrCode_Object = MibTableColumn
otxPrev3ErrCode = _OtxPrev3ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 18),
    _OtxPrev3ErrCode_Type()
)
otxPrev3ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev3ErrCode.setStatus("mandatory")
_OtxPrev4Time_Type = TimeTicks
_OtxPrev4Time_Object = MibTableColumn
otxPrev4Time = _OtxPrev4Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 19),
    _OtxPrev4Time_Type()
)
otxPrev4Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev4Time.setStatus("mandatory")


class _OtxPrev4Value_Type(DisplayString):
    """Custom type otxPrev4Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxPrev4Value_Type.__name__ = "DisplayString"
_OtxPrev4Value_Object = MibTableColumn
otxPrev4Value = _OtxPrev4Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 20),
    _OtxPrev4Value_Type()
)
otxPrev4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev4Value.setStatus("mandatory")


class _OtxPrev4ErrCode_Type(DisplayString):
    """Custom type otxPrev4ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxPrev4ErrCode_Type.__name__ = "DisplayString"
_OtxPrev4ErrCode_Object = MibTableColumn
otxPrev4ErrCode = _OtxPrev4ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 21),
    _OtxPrev4ErrCode_Type()
)
otxPrev4ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev4ErrCode.setStatus("mandatory")
_OtxPrev5Time_Type = TimeTicks
_OtxPrev5Time_Object = MibTableColumn
otxPrev5Time = _OtxPrev5Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 22),
    _OtxPrev5Time_Type()
)
otxPrev5Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev5Time.setStatus("mandatory")


class _OtxPrev5Value_Type(DisplayString):
    """Custom type otxPrev5Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxPrev5Value_Type.__name__ = "DisplayString"
_OtxPrev5Value_Object = MibTableColumn
otxPrev5Value = _OtxPrev5Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 23),
    _OtxPrev5Value_Type()
)
otxPrev5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev5Value.setStatus("mandatory")


class _OtxPrev5ErrCode_Type(DisplayString):
    """Custom type otxPrev5ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxPrev5ErrCode_Type.__name__ = "DisplayString"
_OtxPrev5ErrCode_Object = MibTableColumn
otxPrev5ErrCode = _OtxPrev5ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 7, 1, 24),
    _OtxPrev5ErrCode_Type()
)
otxPrev5ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxPrev5ErrCode.setStatus("mandatory")
_GrpQueueByNameList_Object = MibTable
grpQueueByNameList = _GrpQueueByNameList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 8)
)
if mibBuilder.loadTexts:
    grpQueueByNameList.setStatus("mandatory")
_QueueBN_Object = MibTableRow
queueBN = _QueueBN_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 8, 1)
)
queueBN.setIndexNames(
    (0, "AUDITEC2-MIB", "queBNName"),
)
if mibBuilder.loadTexts:
    queueBN.setStatus("mandatory")


class _QueBNName_Type(DisplayString):
    """Custom type queBNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_QueBNName_Type.__name__ = "DisplayString"
_QueBNName_Object = MibTableColumn
queBNName = _QueBNName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 8, 1, 1),
    _QueBNName_Type()
)
queBNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queBNName.setStatus("mandatory")


class _QueBNType_Type(Integer32):
    """Custom type queBNType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("user", 1))
    )


_QueBNType_Type.__name__ = "Integer32"
_QueBNType_Object = MibTableColumn
queBNType = _QueBNType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 8, 1, 2),
    _QueBNType_Type()
)
queBNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queBNType.setStatus("mandatory")
_QueBNNbSce_Type = Integer32
_QueBNNbSce_Object = MibTableColumn
queBNNbSce = _QueBNNbSce_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 8, 1, 3),
    _QueBNNbSce_Type()
)
queBNNbSce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queBNNbSce.setStatus("mandatory")
_GrpSceByNameList_Object = MibTable
grpSceByNameList = _GrpSceByNameList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9)
)
if mibBuilder.loadTexts:
    grpSceByNameList.setStatus("mandatory")
_ScenarioBN_Object = MibTableRow
scenarioBN = _ScenarioBN_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1)
)
scenarioBN.setIndexNames(
    (0, "AUDITEC2-MIB", "sceBNQueName"),
    (0, "AUDITEC2-MIB", "sceBNName"),
)
if mibBuilder.loadTexts:
    scenarioBN.setStatus("mandatory")


class _SceBNName_Type(DisplayString):
    """Custom type sceBNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_SceBNName_Type.__name__ = "DisplayString"
_SceBNName_Object = MibTableColumn
sceBNName = _SceBNName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 1),
    _SceBNName_Type()
)
sceBNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNName.setStatus("mandatory")


class _SceBNQueName_Type(DisplayString):
    """Custom type sceBNQueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_SceBNQueName_Type.__name__ = "DisplayString"
_SceBNQueName_Object = MibTableColumn
sceBNQueName = _SceBNQueName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 2),
    _SceBNQueName_Type()
)
sceBNQueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNQueName.setStatus("mandatory")


class _SceBNType_Type(Integer32):
    """Custom type sceBNType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("service", 1),
          ("user", 0))
    )


_SceBNType_Type.__name__ = "Integer32"
_SceBNType_Object = MibTableColumn
sceBNType = _SceBNType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 3),
    _SceBNType_Type()
)
sceBNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNType.setStatus("mandatory")


class _SceBNUnavailObj_Type(Integer32):
    """Custom type sceBNUnavailObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SceBNUnavailObj_Type.__name__ = "Integer32"
_SceBNUnavailObj_Object = MibTableColumn
sceBNUnavailObj = _SceBNUnavailObj_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 4),
    _SceBNUnavailObj_Type()
)
sceBNUnavailObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNUnavailObj.setStatus("mandatory")


class _SceBNState_Type(Integer32):
    """Custom type sceBNState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("outOfRange", 2),
          ("suspended", 4),
          ("unavailable", 8))
    )


_SceBNState_Type.__name__ = "Integer32"
_SceBNState_Object = MibTableColumn
sceBNState = _SceBNState_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 5),
    _SceBNState_Type()
)
sceBNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNState.setStatus("mandatory")
_SceBNNbExec_Type = Counter32
_SceBNNbExec_Object = MibTableColumn
sceBNNbExec = _SceBNNbExec_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 6),
    _SceBNNbExec_Type()
)
sceBNNbExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNNbExec.setStatus("mandatory")
_SceBNNbUnAvailExec_Type = Counter32
_SceBNNbUnAvailExec_Object = MibTableColumn
sceBNNbUnAvailExec = _SceBNNbUnAvailExec_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 7),
    _SceBNNbUnAvailExec_Type()
)
sceBNNbUnAvailExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNNbUnAvailExec.setStatus("mandatory")
_SceBNStartTime_Type = TimeTicks
_SceBNStartTime_Object = MibTableColumn
sceBNStartTime = _SceBNStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 8),
    _SceBNStartTime_Type()
)
sceBNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNStartTime.setStatus("mandatory")
_SceBNAccumulationMeasureDuration_Type = Counter32
_SceBNAccumulationMeasureDuration_Object = MibTableColumn
sceBNAccumulationMeasureDuration = _SceBNAccumulationMeasureDuration_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 9),
    _SceBNAccumulationMeasureDuration_Type()
)
sceBNAccumulationMeasureDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNAccumulationMeasureDuration.setStatus("mandatory")
_SceBNAccumulationUnavailDuration_Type = Counter32
_SceBNAccumulationUnavailDuration_Object = MibTableColumn
sceBNAccumulationUnavailDuration = _SceBNAccumulationUnavailDuration_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 10),
    _SceBNAccumulationUnavailDuration_Type()
)
sceBNAccumulationUnavailDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNAccumulationUnavailDuration.setStatus("mandatory")
_SceBNNbOrd_Type = Integer32
_SceBNNbOrd_Object = MibTableColumn
sceBNNbOrd = _SceBNNbOrd_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 9, 1, 11),
    _SceBNNbOrd_Type()
)
sceBNNbOrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sceBNNbOrd.setStatus("mandatory")
_GrpOrdByNameList_Object = MibTable
grpOrdByNameList = _GrpOrdByNameList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10)
)
if mibBuilder.loadTexts:
    grpOrdByNameList.setStatus("mandatory")
_OrderBN_Object = MibTableRow
orderBN = _OrderBN_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1)
)
orderBN.setIndexNames(
    (0, "AUDITEC2-MIB", "ordBNQueName"),
    (0, "AUDITEC2-MIB", "ordBNSceName"),
    (0, "AUDITEC2-MIB", "ordBNName"),
)
if mibBuilder.loadTexts:
    orderBN.setStatus("mandatory")


class _OrdBNName_Type(DisplayString):
    """Custom type ordBNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNName_Type.__name__ = "DisplayString"
_OrdBNName_Object = MibTableColumn
ordBNName = _OrdBNName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 1),
    _OrdBNName_Type()
)
ordBNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNName.setStatus("mandatory")


class _OrdBNSceName_Type(DisplayString):
    """Custom type ordBNSceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNSceName_Type.__name__ = "DisplayString"
_OrdBNSceName_Object = MibTableColumn
ordBNSceName = _OrdBNSceName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 2),
    _OrdBNSceName_Type()
)
ordBNSceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNSceName.setStatus("mandatory")


class _OrdBNQueName_Type(DisplayString):
    """Custom type ordBNQueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNQueName_Type.__name__ = "DisplayString"
_OrdBNQueName_Object = MibTableColumn
ordBNQueName = _OrdBNQueName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 3),
    _OrdBNQueName_Type()
)
ordBNQueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNQueName.setStatus("mandatory")


class _OrdBNType_Type(Integer32):
    """Custom type ordBNType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("num", 2),
          ("tps", 0))
    )


_OrdBNType_Type.__name__ = "Integer32"
_OrdBNType_Object = MibTableColumn
ordBNType = _OrdBNType_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 4),
    _OrdBNType_Type()
)
ordBNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNType.setStatus("mandatory")


class _OrdBNObjNbRef_Type(Integer32):
    """Custom type ordBNObjNbRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OrdBNObjNbRef_Type.__name__ = "Integer32"
_OrdBNObjNbRef_Object = MibTableColumn
ordBNObjNbRef = _OrdBNObjNbRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 5),
    _OrdBNObjNbRef_Type()
)
ordBNObjNbRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNObjNbRef.setStatus("mandatory")


class _OrdBNRef_Type(Integer32):
    """Custom type ordBNRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNRef_Type.__name__ = "Integer32"
_OrdBNRef_Object = MibTableColumn
ordBNRef = _OrdBNRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 6),
    _OrdBNRef_Type()
)
ordBNRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNRef.setStatus("mandatory")
_OrdBNAccumulationNbRef_Type = Counter32
_OrdBNAccumulationNbRef_Object = MibTableColumn
ordBNAccumulationNbRef = _OrdBNAccumulationNbRef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 7),
    _OrdBNAccumulationNbRef_Type()
)
ordBNAccumulationNbRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNbRef.setStatus("mandatory")


class _OrdBNCoef_Type(Integer32):
    """Custom type ordBNCoef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNCoef_Type.__name__ = "Integer32"
_OrdBNCoef_Object = MibTableColumn
ordBNCoef = _OrdBNCoef_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 8),
    _OrdBNCoef_Type()
)
ordBNCoef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNCoef.setStatus("mandatory")


class _OrdBNUnit_Type(DisplayString):
    """Custom type ordBNUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNUnit_Type.__name__ = "DisplayString"
_OrdBNUnit_Object = MibTableColumn
ordBNUnit = _OrdBNUnit_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 9),
    _OrdBNUnit_Type()
)
ordBNUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNUnit.setStatus("mandatory")


class _OrdBNMin_Type(Integer32):
    """Custom type ordBNMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNMin_Type.__name__ = "Integer32"
_OrdBNMin_Object = MibTableColumn
ordBNMin = _OrdBNMin_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 10),
    _OrdBNMin_Type()
)
ordBNMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNMin.setStatus("mandatory")


class _OrdBNMax_Type(Integer32):
    """Custom type ordBNMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNMax_Type.__name__ = "Integer32"
_OrdBNMax_Object = MibTableColumn
ordBNMax = _OrdBNMax_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 11),
    _OrdBNMax_Type()
)
ordBNMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNMax.setStatus("mandatory")
_OrdBNAccumulation_Type = Counter32
_OrdBNAccumulation_Object = MibTableColumn
ordBNAccumulation = _OrdBNAccumulation_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 12),
    _OrdBNAccumulation_Type()
)
ordBNAccumulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulation.setStatus("mandatory")


class _OrdBNAverage6_Type(Integer32):
    """Custom type ordBNAverage6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNAverage6_Type.__name__ = "Integer32"
_OrdBNAverage6_Object = MibTableColumn
ordBNAverage6 = _OrdBNAverage6_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 13),
    _OrdBNAverage6_Type()
)
ordBNAverage6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAverage6.setStatus("mandatory")
_OrdBNNbSamples_Type = Counter32
_OrdBNNbSamples_Object = MibTableColumn
ordBNNbSamples = _OrdBNNbSamples_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 14),
    _OrdBNNbSamples_Type()
)
ordBNNbSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNNbSamples.setStatus("mandatory")


class _OrdBNThreashold1_Type(Integer32):
    """Custom type ordBNThreashold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNThreashold1_Type.__name__ = "Integer32"
_OrdBNThreashold1_Object = MibTableColumn
ordBNThreashold1 = _OrdBNThreashold1_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 15),
    _OrdBNThreashold1_Type()
)
ordBNThreashold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNThreashold1.setStatus("mandatory")


class _OrdBNThreashold2_Type(Integer32):
    """Custom type ordBNThreashold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNThreashold2_Type.__name__ = "Integer32"
_OrdBNThreashold2_Object = MibTableColumn
ordBNThreashold2 = _OrdBNThreashold2_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 16),
    _OrdBNThreashold2_Type()
)
ordBNThreashold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNThreashold2.setStatus("mandatory")


class _OrdBNThreashold3_Type(Integer32):
    """Custom type ordBNThreashold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNThreashold3_Type.__name__ = "Integer32"
_OrdBNThreashold3_Object = MibTableColumn
ordBNThreashold3 = _OrdBNThreashold3_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 17),
    _OrdBNThreashold3_Type()
)
ordBNThreashold3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNThreashold3.setStatus("mandatory")


class _OrdBNThreashold4_Type(Integer32):
    """Custom type ordBNThreashold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNThreashold4_Type.__name__ = "Integer32"
_OrdBNThreashold4_Object = MibTableColumn
ordBNThreashold4 = _OrdBNThreashold4_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 18),
    _OrdBNThreashold4_Type()
)
ordBNThreashold4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNThreashold4.setStatus("mandatory")
_OrdBNAccumulationNb1_Type = Counter32
_OrdBNAccumulationNb1_Object = MibTableColumn
ordBNAccumulationNb1 = _OrdBNAccumulationNb1_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 19),
    _OrdBNAccumulationNb1_Type()
)
ordBNAccumulationNb1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNb1.setStatus("mandatory")
_OrdBNAccumulationNb2_Type = Counter32
_OrdBNAccumulationNb2_Object = MibTableColumn
ordBNAccumulationNb2 = _OrdBNAccumulationNb2_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 20),
    _OrdBNAccumulationNb2_Type()
)
ordBNAccumulationNb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNb2.setStatus("mandatory")
_OrdBNAccumulationNb3_Type = Counter32
_OrdBNAccumulationNb3_Object = MibTableColumn
ordBNAccumulationNb3 = _OrdBNAccumulationNb3_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 21),
    _OrdBNAccumulationNb3_Type()
)
ordBNAccumulationNb3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNb3.setStatus("mandatory")
_OrdBNAccumulationNb4_Type = Counter32
_OrdBNAccumulationNb4_Object = MibTableColumn
ordBNAccumulationNb4 = _OrdBNAccumulationNb4_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 22),
    _OrdBNAccumulationNb4_Type()
)
ordBNAccumulationNb4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNb4.setStatus("mandatory")
_OrdBNAccumulationNb5_Type = Counter32
_OrdBNAccumulationNb5_Object = MibTableColumn
ordBNAccumulationNb5 = _OrdBNAccumulationNb5_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 23),
    _OrdBNAccumulationNb5_Type()
)
ordBNAccumulationNb5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNAccumulationNb5.setStatus("mandatory")
_OrdBNNbUnavail_Type = Counter32
_OrdBNNbUnavail_Object = MibTableColumn
ordBNNbUnavail = _OrdBNNbUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 24),
    _OrdBNNbUnavail_Type()
)
ordBNNbUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNNbUnavail.setStatus("mandatory")
_OrdBNTime_Type = TimeTicks
_OrdBNTime_Object = MibTableColumn
ordBNTime = _OrdBNTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 25),
    _OrdBNTime_Type()
)
ordBNTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNTime.setStatus("mandatory")


class _OrdBNValue_Type(Integer32):
    """Custom type ordBNValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNValue_Type.__name__ = "Integer32"
_OrdBNValue_Object = MibTableColumn
ordBNValue = _OrdBNValue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 26),
    _OrdBNValue_Type()
)
ordBNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNValue.setStatus("mandatory")


class _OrdBNErrCode_Type(DisplayString):
    """Custom type ordBNErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNErrCode_Type.__name__ = "DisplayString"
_OrdBNErrCode_Object = MibTableColumn
ordBNErrCode = _OrdBNErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 27),
    _OrdBNErrCode_Type()
)
ordBNErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNErrCode.setStatus("mandatory")
_OrdBNPrev1Time_Type = TimeTicks
_OrdBNPrev1Time_Object = MibTableColumn
ordBNPrev1Time = _OrdBNPrev1Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 28),
    _OrdBNPrev1Time_Type()
)
ordBNPrev1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev1Time.setStatus("mandatory")


class _OrdBNPrev1Value_Type(Integer32):
    """Custom type ordBNPrev1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNPrev1Value_Type.__name__ = "Integer32"
_OrdBNPrev1Value_Object = MibTableColumn
ordBNPrev1Value = _OrdBNPrev1Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 29),
    _OrdBNPrev1Value_Type()
)
ordBNPrev1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev1Value.setStatus("mandatory")


class _OrdBNPrev1ErrCode_Type(DisplayString):
    """Custom type ordBNPrev1ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNPrev1ErrCode_Type.__name__ = "DisplayString"
_OrdBNPrev1ErrCode_Object = MibTableColumn
ordBNPrev1ErrCode = _OrdBNPrev1ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 30),
    _OrdBNPrev1ErrCode_Type()
)
ordBNPrev1ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev1ErrCode.setStatus("mandatory")
_OrdBNPrev2Time_Type = TimeTicks
_OrdBNPrev2Time_Object = MibTableColumn
ordBNPrev2Time = _OrdBNPrev2Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 31),
    _OrdBNPrev2Time_Type()
)
ordBNPrev2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev2Time.setStatus("mandatory")


class _OrdBNPrev2Value_Type(Integer32):
    """Custom type ordBNPrev2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNPrev2Value_Type.__name__ = "Integer32"
_OrdBNPrev2Value_Object = MibTableColumn
ordBNPrev2Value = _OrdBNPrev2Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 32),
    _OrdBNPrev2Value_Type()
)
ordBNPrev2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev2Value.setStatus("mandatory")


class _OrdBNPrev2ErrCode_Type(DisplayString):
    """Custom type ordBNPrev2ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNPrev2ErrCode_Type.__name__ = "DisplayString"
_OrdBNPrev2ErrCode_Object = MibTableColumn
ordBNPrev2ErrCode = _OrdBNPrev2ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 33),
    _OrdBNPrev2ErrCode_Type()
)
ordBNPrev2ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev2ErrCode.setStatus("mandatory")
_OrdBNPrev3Time_Type = TimeTicks
_OrdBNPrev3Time_Object = MibTableColumn
ordBNPrev3Time = _OrdBNPrev3Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 34),
    _OrdBNPrev3Time_Type()
)
ordBNPrev3Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev3Time.setStatus("mandatory")


class _OrdBNPrev3Value_Type(Integer32):
    """Custom type ordBNPrev3Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNPrev3Value_Type.__name__ = "Integer32"
_OrdBNPrev3Value_Object = MibTableColumn
ordBNPrev3Value = _OrdBNPrev3Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 35),
    _OrdBNPrev3Value_Type()
)
ordBNPrev3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev3Value.setStatus("mandatory")


class _OrdBNPrev3ErrCode_Type(DisplayString):
    """Custom type ordBNPrev3ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNPrev3ErrCode_Type.__name__ = "DisplayString"
_OrdBNPrev3ErrCode_Object = MibTableColumn
ordBNPrev3ErrCode = _OrdBNPrev3ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 36),
    _OrdBNPrev3ErrCode_Type()
)
ordBNPrev3ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev3ErrCode.setStatus("mandatory")
_OrdBNPrev4Time_Type = TimeTicks
_OrdBNPrev4Time_Object = MibTableColumn
ordBNPrev4Time = _OrdBNPrev4Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 37),
    _OrdBNPrev4Time_Type()
)
ordBNPrev4Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev4Time.setStatus("mandatory")


class _OrdBNPrev4Value_Type(Integer32):
    """Custom type ordBNPrev4Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNPrev4Value_Type.__name__ = "Integer32"
_OrdBNPrev4Value_Object = MibTableColumn
ordBNPrev4Value = _OrdBNPrev4Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 38),
    _OrdBNPrev4Value_Type()
)
ordBNPrev4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev4Value.setStatus("mandatory")


class _OrdBNPrev4ErrCode_Type(DisplayString):
    """Custom type ordBNPrev4ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNPrev4ErrCode_Type.__name__ = "DisplayString"
_OrdBNPrev4ErrCode_Object = MibTableColumn
ordBNPrev4ErrCode = _OrdBNPrev4ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 39),
    _OrdBNPrev4ErrCode_Type()
)
ordBNPrev4ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev4ErrCode.setStatus("mandatory")
_OrdBNPrev5Time_Type = TimeTicks
_OrdBNPrev5Time_Object = MibTableColumn
ordBNPrev5Time = _OrdBNPrev5Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 40),
    _OrdBNPrev5Time_Type()
)
ordBNPrev5Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev5Time.setStatus("mandatory")


class _OrdBNPrev5Value_Type(Integer32):
    """Custom type ordBNPrev5Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OrdBNPrev5Value_Type.__name__ = "Integer32"
_OrdBNPrev5Value_Object = MibTableColumn
ordBNPrev5Value = _OrdBNPrev5Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 41),
    _OrdBNPrev5Value_Type()
)
ordBNPrev5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev5Value.setStatus("mandatory")


class _OrdBNPrev5ErrCode_Type(DisplayString):
    """Custom type ordBNPrev5ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OrdBNPrev5ErrCode_Type.__name__ = "DisplayString"
_OrdBNPrev5ErrCode_Object = MibTableColumn
ordBNPrev5ErrCode = _OrdBNPrev5ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 10, 1, 42),
    _OrdBNPrev5ErrCode_Type()
)
ordBNPrev5ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ordBNPrev5ErrCode.setStatus("mandatory")
_GrpOrdTxtByNameList_Object = MibTable
grpOrdTxtByNameList = _GrpOrdTxtByNameList_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11)
)
if mibBuilder.loadTexts:
    grpOrdTxtByNameList.setStatus("mandatory")
_OrderTxtBN_Object = MibTableRow
orderTxtBN = _OrderTxtBN_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1)
)
orderTxtBN.setIndexNames(
    (0, "AUDITEC2-MIB", "otxBNQueName"),
    (0, "AUDITEC2-MIB", "otxBNSceName"),
    (0, "AUDITEC2-MIB", "otxBNName"),
)
if mibBuilder.loadTexts:
    orderTxtBN.setStatus("mandatory")


class _OtxBNName_Type(DisplayString):
    """Custom type otxBNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNName_Type.__name__ = "DisplayString"
_OtxBNName_Object = MibTableColumn
otxBNName = _OtxBNName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 1),
    _OtxBNName_Type()
)
otxBNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNName.setStatus("mandatory")


class _OtxBNSceName_Type(DisplayString):
    """Custom type otxBNSceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNSceName_Type.__name__ = "DisplayString"
_OtxBNSceName_Object = MibTableColumn
otxBNSceName = _OtxBNSceName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 2),
    _OtxBNSceName_Type()
)
otxBNSceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNSceName.setStatus("mandatory")


class _OtxBNQueName_Type(DisplayString):
    """Custom type otxBNQueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNQueName_Type.__name__ = "DisplayString"
_OtxBNQueName_Object = MibTableColumn
otxBNQueName = _OtxBNQueName_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 3),
    _OtxBNQueName_Type()
)
otxBNQueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNQueName.setStatus("mandatory")
_OtxBNNbSamples_Type = Counter32
_OtxBNNbSamples_Object = MibTableColumn
otxBNNbSamples = _OtxBNNbSamples_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 4),
    _OtxBNNbSamples_Type()
)
otxBNNbSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNNbSamples.setStatus("mandatory")
_OtxBNNbUnavail_Type = Counter32
_OtxBNNbUnavail_Object = MibTableColumn
otxBNNbUnavail = _OtxBNNbUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 5),
    _OtxBNNbUnavail_Type()
)
otxBNNbUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNNbUnavail.setStatus("mandatory")
_OtxBNTime_Type = TimeTicks
_OtxBNTime_Object = MibTableColumn
otxBNTime = _OtxBNTime_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 6),
    _OtxBNTime_Type()
)
otxBNTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNTime.setStatus("mandatory")


class _OtxBNValue_Type(DisplayString):
    """Custom type otxBNValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNValue_Type.__name__ = "DisplayString"
_OtxBNValue_Object = MibTableColumn
otxBNValue = _OtxBNValue_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 7),
    _OtxBNValue_Type()
)
otxBNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNValue.setStatus("mandatory")


class _OtxBNErrCode_Type(DisplayString):
    """Custom type otxBNErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNErrCode_Type.__name__ = "DisplayString"
_OtxBNErrCode_Object = MibTableColumn
otxBNErrCode = _OtxBNErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 8),
    _OtxBNErrCode_Type()
)
otxBNErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNErrCode.setStatus("mandatory")
_OtxBNPrev1Time_Type = TimeTicks
_OtxBNPrev1Time_Object = MibTableColumn
otxBNPrev1Time = _OtxBNPrev1Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 9),
    _OtxBNPrev1Time_Type()
)
otxBNPrev1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev1Time.setStatus("mandatory")


class _OtxBNPrev1Value_Type(DisplayString):
    """Custom type otxBNPrev1Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNPrev1Value_Type.__name__ = "DisplayString"
_OtxBNPrev1Value_Object = MibTableColumn
otxBNPrev1Value = _OtxBNPrev1Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 10),
    _OtxBNPrev1Value_Type()
)
otxBNPrev1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev1Value.setStatus("mandatory")


class _OtxBNPrev1ErrCode_Type(DisplayString):
    """Custom type otxBNPrev1ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNPrev1ErrCode_Type.__name__ = "DisplayString"
_OtxBNPrev1ErrCode_Object = MibTableColumn
otxBNPrev1ErrCode = _OtxBNPrev1ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 11),
    _OtxBNPrev1ErrCode_Type()
)
otxBNPrev1ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev1ErrCode.setStatus("mandatory")
_OtxBNPrev2Time_Type = TimeTicks
_OtxBNPrev2Time_Object = MibTableColumn
otxBNPrev2Time = _OtxBNPrev2Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 12),
    _OtxBNPrev2Time_Type()
)
otxBNPrev2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev2Time.setStatus("mandatory")


class _OtxBNPrev2Value_Type(DisplayString):
    """Custom type otxBNPrev2Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNPrev2Value_Type.__name__ = "DisplayString"
_OtxBNPrev2Value_Object = MibTableColumn
otxBNPrev2Value = _OtxBNPrev2Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 13),
    _OtxBNPrev2Value_Type()
)
otxBNPrev2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev2Value.setStatus("mandatory")


class _OtxBNPrev2ErrCode_Type(DisplayString):
    """Custom type otxBNPrev2ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNPrev2ErrCode_Type.__name__ = "DisplayString"
_OtxBNPrev2ErrCode_Object = MibTableColumn
otxBNPrev2ErrCode = _OtxBNPrev2ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 14),
    _OtxBNPrev2ErrCode_Type()
)
otxBNPrev2ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev2ErrCode.setStatus("mandatory")
_OtxBNPrev3Time_Type = TimeTicks
_OtxBNPrev3Time_Object = MibTableColumn
otxBNPrev3Time = _OtxBNPrev3Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 15),
    _OtxBNPrev3Time_Type()
)
otxBNPrev3Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev3Time.setStatus("mandatory")


class _OtxBNPrev3Value_Type(DisplayString):
    """Custom type otxBNPrev3Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNPrev3Value_Type.__name__ = "DisplayString"
_OtxBNPrev3Value_Object = MibTableColumn
otxBNPrev3Value = _OtxBNPrev3Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 16),
    _OtxBNPrev3Value_Type()
)
otxBNPrev3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev3Value.setStatus("mandatory")


class _OtxBNPrev3ErrCode_Type(DisplayString):
    """Custom type otxBNPrev3ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNPrev3ErrCode_Type.__name__ = "DisplayString"
_OtxBNPrev3ErrCode_Object = MibTableColumn
otxBNPrev3ErrCode = _OtxBNPrev3ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 17),
    _OtxBNPrev3ErrCode_Type()
)
otxBNPrev3ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev3ErrCode.setStatus("mandatory")
_OtxBNPrev4Time_Type = TimeTicks
_OtxBNPrev4Time_Object = MibTableColumn
otxBNPrev4Time = _OtxBNPrev4Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 18),
    _OtxBNPrev4Time_Type()
)
otxBNPrev4Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev4Time.setStatus("mandatory")


class _OtxBNPrev4Value_Type(DisplayString):
    """Custom type otxBNPrev4Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNPrev4Value_Type.__name__ = "DisplayString"
_OtxBNPrev4Value_Object = MibTableColumn
otxBNPrev4Value = _OtxBNPrev4Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 19),
    _OtxBNPrev4Value_Type()
)
otxBNPrev4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev4Value.setStatus("mandatory")


class _OtxBNPrev4ErrCode_Type(DisplayString):
    """Custom type otxBNPrev4ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNPrev4ErrCode_Type.__name__ = "DisplayString"
_OtxBNPrev4ErrCode_Object = MibTableColumn
otxBNPrev4ErrCode = _OtxBNPrev4ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 20),
    _OtxBNPrev4ErrCode_Type()
)
otxBNPrev4ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev4ErrCode.setStatus("mandatory")
_OtxBNPrev5Time_Type = TimeTicks
_OtxBNPrev5Time_Object = MibTableColumn
otxBNPrev5Time = _OtxBNPrev5Time_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 21),
    _OtxBNPrev5Time_Type()
)
otxBNPrev5Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev5Time.setStatus("mandatory")


class _OtxBNPrev5Value_Type(DisplayString):
    """Custom type otxBNPrev5Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_OtxBNPrev5Value_Type.__name__ = "DisplayString"
_OtxBNPrev5Value_Object = MibTableColumn
otxBNPrev5Value = _OtxBNPrev5Value_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 22),
    _OtxBNPrev5Value_Type()
)
otxBNPrev5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev5Value.setStatus("mandatory")


class _OtxBNPrev5ErrCode_Type(DisplayString):
    """Custom type otxBNPrev5ErrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_OtxBNPrev5ErrCode_Type.__name__ = "DisplayString"
_OtxBNPrev5ErrCode_Object = MibTableColumn
otxBNPrev5ErrCode = _OtxBNPrev5ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1774, 4, 11, 1, 23),
    _OtxBNPrev5ErrCode_Type()
)
otxBNPrev5ErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otxBNPrev5ErrCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects

probeAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1774, 0, 1)
)
probeAlarmEvent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("AUDITEC2-MIB", "almSce"),
        ("AUDITEC2-MIB", "almMsg"))
)
if mibBuilder.loadTexts:
    probeAlarmEvent.setStatus(
        "current"
    )

probeAlarmEvent2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1774, 0, 3)
)
probeAlarmEvent2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("AUDITEC2-MIB", "almSce"),
        ("AUDITEC2-MIB", "almOrd"),
        ("AUDITEC2-MIB", "almCode"),
        ("AUDITEC2-MIB", "almLevel"),
        ("AUDITEC2-MIB", "almMsg"))
)
if mibBuilder.loadTexts:
    probeAlarmEvent2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUDITEC2-MIB",
    **{"internet": internet,
       "private": private,
       "enterprises": enterprises,
       "auditec": auditec,
       "probeAlarmEvent": probeAlarmEvent,
       "probeAlarmEvent2": probeAlarmEvent2,
       "probe": probe,
       "prbIpAddr": prbIpAddr,
       "prbState": prbState,
       "prbBasePath": prbBasePath,
       "prbGrpList": prbGrpList,
       "prbServerConnection": prbServerConnection,
       "prbDiffGMT": prbDiffGMT,
       "prbNewtestMemory": prbNewtestMemory,
       "prbGrpStartTime": prbGrpStartTime,
       "prbLastHeartBeat": prbLastHeartBeat,
       "action": action,
       "actType": actType,
       "actParam": actParam,
       "alarm": alarm,
       "almSce": almSce,
       "almMsg": almMsg,
       "almCode": almCode,
       "almLevel": almLevel,
       "almOrd": almOrd,
       "group": group,
       "grpName": grpName,
       "grpNbQueue": grpNbQueue,
       "grpNextTime": grpNextTime,
       "grpQueueList": grpQueueList,
       "queue": queue,
       "queIndex": queIndex,
       "queName": queName,
       "queType": queType,
       "queNbSce": queNbSce,
       "grpSceList": grpSceList,
       "scenario": scenario,
       "sceIndex": sceIndex,
       "sceQueIndex": sceQueIndex,
       "sceName": sceName,
       "sceType": sceType,
       "sceUnavailObj": sceUnavailObj,
       "sceState": sceState,
       "sceNbExec": sceNbExec,
       "sceNbUnAvailExec": sceNbUnAvailExec,
       "sceStartTime": sceStartTime,
       "sceAccumulationMeasureDuration": sceAccumulationMeasureDuration,
       "sceAccumulationUnavailDuration": sceAccumulationUnavailDuration,
       "sceNbOrd": sceNbOrd,
       "sceState2": sceState2,
       "grpOrdList": grpOrdList,
       "order": order,
       "ordIndex": ordIndex,
       "ordSceIndex": ordSceIndex,
       "ordQueIndex": ordQueIndex,
       "ordName": ordName,
       "ordType": ordType,
       "ordObjNbRef": ordObjNbRef,
       "ordRef": ordRef,
       "ordAccumulationNbRef": ordAccumulationNbRef,
       "ordCoef": ordCoef,
       "ordUnit": ordUnit,
       "ordMin": ordMin,
       "ordMax": ordMax,
       "ordAccumulation": ordAccumulation,
       "ordAverage6": ordAverage6,
       "ordNbSamples": ordNbSamples,
       "ordThreashold1": ordThreashold1,
       "ordThreashold2": ordThreashold2,
       "ordThreashold3": ordThreashold3,
       "ordThreashold4": ordThreashold4,
       "ordAccumulationNb1": ordAccumulationNb1,
       "ordAccumulationNb2": ordAccumulationNb2,
       "ordAccumulationNb3": ordAccumulationNb3,
       "ordAccumulationNb4": ordAccumulationNb4,
       "ordAccumulationNb5": ordAccumulationNb5,
       "ordNbUnavail": ordNbUnavail,
       "ordTime": ordTime,
       "ordValue": ordValue,
       "ordErrCode": ordErrCode,
       "ordPrev1Time": ordPrev1Time,
       "ordPrev1Value": ordPrev1Value,
       "ordPrev1ErrCode": ordPrev1ErrCode,
       "ordPrev2Time": ordPrev2Time,
       "ordPrev2Value": ordPrev2Value,
       "ordPrev2ErrCode": ordPrev2ErrCode,
       "ordPrev3Time": ordPrev3Time,
       "ordPrev3Value": ordPrev3Value,
       "ordPrev3ErrCode": ordPrev3ErrCode,
       "ordPrev4Time": ordPrev4Time,
       "ordPrev4Value": ordPrev4Value,
       "ordPrev4ErrCode": ordPrev4ErrCode,
       "ordPrev5Time": ordPrev5Time,
       "ordPrev5Value": ordPrev5Value,
       "ordPrev5ErrCode": ordPrev5ErrCode,
       "grpOrdTxtList": grpOrdTxtList,
       "orderTxt": orderTxt,
       "otxIndex": otxIndex,
       "otxSceIndex": otxSceIndex,
       "otxQueIndex": otxQueIndex,
       "otxName": otxName,
       "otxNbSamples": otxNbSamples,
       "otxNbUnavail": otxNbUnavail,
       "otxTime": otxTime,
       "otxValue": otxValue,
       "otxErrCode": otxErrCode,
       "otxPrev1Time": otxPrev1Time,
       "otxPrev1Value": otxPrev1Value,
       "otxPrev1ErrCode": otxPrev1ErrCode,
       "otxPrev2Time": otxPrev2Time,
       "otxPrev2Value": otxPrev2Value,
       "otxPrev2ErrCode": otxPrev2ErrCode,
       "otxPrev3Time": otxPrev3Time,
       "otxPrev3Value": otxPrev3Value,
       "otxPrev3ErrCode": otxPrev3ErrCode,
       "otxPrev4Time": otxPrev4Time,
       "otxPrev4Value": otxPrev4Value,
       "otxPrev4ErrCode": otxPrev4ErrCode,
       "otxPrev5Time": otxPrev5Time,
       "otxPrev5Value": otxPrev5Value,
       "otxPrev5ErrCode": otxPrev5ErrCode,
       "grpQueueByNameList": grpQueueByNameList,
       "queueBN": queueBN,
       "queBNName": queBNName,
       "queBNType": queBNType,
       "queBNNbSce": queBNNbSce,
       "grpSceByNameList": grpSceByNameList,
       "scenarioBN": scenarioBN,
       "sceBNName": sceBNName,
       "sceBNQueName": sceBNQueName,
       "sceBNType": sceBNType,
       "sceBNUnavailObj": sceBNUnavailObj,
       "sceBNState": sceBNState,
       "sceBNNbExec": sceBNNbExec,
       "sceBNNbUnAvailExec": sceBNNbUnAvailExec,
       "sceBNStartTime": sceBNStartTime,
       "sceBNAccumulationMeasureDuration": sceBNAccumulationMeasureDuration,
       "sceBNAccumulationUnavailDuration": sceBNAccumulationUnavailDuration,
       "sceBNNbOrd": sceBNNbOrd,
       "grpOrdByNameList": grpOrdByNameList,
       "orderBN": orderBN,
       "ordBNName": ordBNName,
       "ordBNSceName": ordBNSceName,
       "ordBNQueName": ordBNQueName,
       "ordBNType": ordBNType,
       "ordBNObjNbRef": ordBNObjNbRef,
       "ordBNRef": ordBNRef,
       "ordBNAccumulationNbRef": ordBNAccumulationNbRef,
       "ordBNCoef": ordBNCoef,
       "ordBNUnit": ordBNUnit,
       "ordBNMin": ordBNMin,
       "ordBNMax": ordBNMax,
       "ordBNAccumulation": ordBNAccumulation,
       "ordBNAverage6": ordBNAverage6,
       "ordBNNbSamples": ordBNNbSamples,
       "ordBNThreashold1": ordBNThreashold1,
       "ordBNThreashold2": ordBNThreashold2,
       "ordBNThreashold3": ordBNThreashold3,
       "ordBNThreashold4": ordBNThreashold4,
       "ordBNAccumulationNb1": ordBNAccumulationNb1,
       "ordBNAccumulationNb2": ordBNAccumulationNb2,
       "ordBNAccumulationNb3": ordBNAccumulationNb3,
       "ordBNAccumulationNb4": ordBNAccumulationNb4,
       "ordBNAccumulationNb5": ordBNAccumulationNb5,
       "ordBNNbUnavail": ordBNNbUnavail,
       "ordBNTime": ordBNTime,
       "ordBNValue": ordBNValue,
       "ordBNErrCode": ordBNErrCode,
       "ordBNPrev1Time": ordBNPrev1Time,
       "ordBNPrev1Value": ordBNPrev1Value,
       "ordBNPrev1ErrCode": ordBNPrev1ErrCode,
       "ordBNPrev2Time": ordBNPrev2Time,
       "ordBNPrev2Value": ordBNPrev2Value,
       "ordBNPrev2ErrCode": ordBNPrev2ErrCode,
       "ordBNPrev3Time": ordBNPrev3Time,
       "ordBNPrev3Value": ordBNPrev3Value,
       "ordBNPrev3ErrCode": ordBNPrev3ErrCode,
       "ordBNPrev4Time": ordBNPrev4Time,
       "ordBNPrev4Value": ordBNPrev4Value,
       "ordBNPrev4ErrCode": ordBNPrev4ErrCode,
       "ordBNPrev5Time": ordBNPrev5Time,
       "ordBNPrev5Value": ordBNPrev5Value,
       "ordBNPrev5ErrCode": ordBNPrev5ErrCode,
       "grpOrdTxtByNameList": grpOrdTxtByNameList,
       "orderTxtBN": orderTxtBN,
       "otxBNName": otxBNName,
       "otxBNSceName": otxBNSceName,
       "otxBNQueName": otxBNQueName,
       "otxBNNbSamples": otxBNNbSamples,
       "otxBNNbUnavail": otxBNNbUnavail,
       "otxBNTime": otxBNTime,
       "otxBNValue": otxBNValue,
       "otxBNErrCode": otxBNErrCode,
       "otxBNPrev1Time": otxBNPrev1Time,
       "otxBNPrev1Value": otxBNPrev1Value,
       "otxBNPrev1ErrCode": otxBNPrev1ErrCode,
       "otxBNPrev2Time": otxBNPrev2Time,
       "otxBNPrev2Value": otxBNPrev2Value,
       "otxBNPrev2ErrCode": otxBNPrev2ErrCode,
       "otxBNPrev3Time": otxBNPrev3Time,
       "otxBNPrev3Value": otxBNPrev3Value,
       "otxBNPrev3ErrCode": otxBNPrev3ErrCode,
       "otxBNPrev4Time": otxBNPrev4Time,
       "otxBNPrev4Value": otxBNPrev4Value,
       "otxBNPrev4ErrCode": otxBNPrev4ErrCode,
       "otxBNPrev5Time": otxBNPrev5Time,
       "otxBNPrev5Value": otxBNPrev5Value,
       "otxBNPrev5ErrCode": otxBNPrev5ErrCode}
)
