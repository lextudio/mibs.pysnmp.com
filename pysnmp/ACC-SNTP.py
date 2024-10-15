# SNMP MIB module (ACC-SNTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SNTP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:01 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccSntp_ObjectIdentity = ObjectIdentity
accSntp = _AccSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88)
)
_AccSntpGeneralScalars_ObjectIdentity = ObjectIdentity
accSntpGeneralScalars = _AccSntpGeneralScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1)
)


class _AccSntpAdminState_Type(Integer32):
    """Custom type accSntpAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AccSntpAdminState_Type.__name__ = "Integer32"
_AccSntpAdminState_Object = MibScalar
accSntpAdminState = _AccSntpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 1),
    _AccSntpAdminState_Type()
)
accSntpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpAdminState.setStatus("mandatory")


class _AccSntpBroadcastMode_Type(Integer32):
    """Custom type accSntpBroadcastMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AccSntpBroadcastMode_Type.__name__ = "Integer32"
_AccSntpBroadcastMode_Object = MibScalar
accSntpBroadcastMode = _AccSntpBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 2),
    _AccSntpBroadcastMode_Type()
)
accSntpBroadcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpBroadcastMode.setStatus("mandatory")


class _AccSntpMessageLevel_Type(Integer32):
    """Custom type accSntpMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccSntpMessageLevel_Type.__name__ = "Integer32"
_AccSntpMessageLevel_Object = MibScalar
accSntpMessageLevel = _AccSntpMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 3),
    _AccSntpMessageLevel_Type()
)
accSntpMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpMessageLevel.setStatus("mandatory")


class _AccSntpDebugMask_Type(Integer32):
    """Custom type accSntpDebugMask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccSntpDebugMask_Type.__name__ = "Integer32"
_AccSntpDebugMask_Object = MibScalar
accSntpDebugMask = _AccSntpDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 4),
    _AccSntpDebugMask_Type()
)
accSntpDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpDebugMask.setStatus("mandatory")
_AccSntpStatInPackets_Type = Counter32
_AccSntpStatInPackets_Object = MibScalar
accSntpStatInPackets = _AccSntpStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 5),
    _AccSntpStatInPackets_Type()
)
accSntpStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpStatInPackets.setStatus("mandatory")
_AccSntpStatOutPackets_Type = Counter32
_AccSntpStatOutPackets_Object = MibScalar
accSntpStatOutPackets = _AccSntpStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 6),
    _AccSntpStatOutPackets_Type()
)
accSntpStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpStatOutPackets.setStatus("mandatory")
_AccSntpStatInDiscards_Type = Counter32
_AccSntpStatInDiscards_Object = MibScalar
accSntpStatInDiscards = _AccSntpStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 7),
    _AccSntpStatInDiscards_Type()
)
accSntpStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpStatInDiscards.setStatus("mandatory")
_AccSntpStatInBcastPackets_Type = Counter32
_AccSntpStatInBcastPackets_Object = MibScalar
accSntpStatInBcastPackets = _AccSntpStatInBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 8),
    _AccSntpStatInBcastPackets_Type()
)
accSntpStatInBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpStatInBcastPackets.setStatus("mandatory")
_AccSntpLastBcastPacTime_Type = OctetString
_AccSntpLastBcastPacTime_Object = MibScalar
accSntpLastBcastPacTime = _AccSntpLastBcastPacTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 9),
    _AccSntpLastBcastPacTime_Type()
)
accSntpLastBcastPacTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpLastBcastPacTime.setStatus("mandatory")
_AccSntpLastBcastPacSrcAddr_Type = IpAddress
_AccSntpLastBcastPacSrcAddr_Object = MibScalar
accSntpLastBcastPacSrcAddr = _AccSntpLastBcastPacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 10),
    _AccSntpLastBcastPacSrcAddr_Type()
)
accSntpLastBcastPacSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpLastBcastPacSrcAddr.setStatus("mandatory")
_AccSntpStatQueryTimeouts_Type = Counter32
_AccSntpStatQueryTimeouts_Object = MibScalar
accSntpStatQueryTimeouts = _AccSntpStatQueryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 1, 11),
    _AccSntpStatQueryTimeouts_Type()
)
accSntpStatQueryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpStatQueryTimeouts.setStatus("mandatory")
_AccSntpSever_ObjectIdentity = ObjectIdentity
accSntpSever = _AccSntpSever_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2)
)
_AccSntpSeverTable_Object = MibTable
accSntpSeverTable = _AccSntpSeverTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1)
)
if mibBuilder.loadTexts:
    accSntpSeverTable.setStatus("mandatory")
_AccSntpSeverEntry_Object = MibTableRow
accSntpSeverEntry = _AccSntpSeverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1)
)
accSntpSeverEntry.setIndexNames(
    (0, "ACC-SNTP", "accSntpServIndex"),
)
if mibBuilder.loadTexts:
    accSntpSeverEntry.setStatus("mandatory")


class _AccSntpServIndex_Type(Integer32):
    """Custom type accSntpServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AccSntpServIndex_Type.__name__ = "Integer32"
_AccSntpServIndex_Object = MibTableColumn
accSntpServIndex = _AccSntpServIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 1),
    _AccSntpServIndex_Type()
)
accSntpServIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServIndex.setStatus("mandatory")
_AccSntpServAddr_Type = IpAddress
_AccSntpServAddr_Object = MibTableColumn
accSntpServAddr = _AccSntpServAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 2),
    _AccSntpServAddr_Type()
)
accSntpServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServAddr.setStatus("mandatory")


class _AccSntpServAdminState_Type(Integer32):
    """Custom type accSntpServAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AccSntpServAdminState_Type.__name__ = "Integer32"
_AccSntpServAdminState_Object = MibTableColumn
accSntpServAdminState = _AccSntpServAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 3),
    _AccSntpServAdminState_Type()
)
accSntpServAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServAdminState.setStatus("mandatory")


class _AccSntpServPollInt_Type(Integer32):
    """Custom type accSntpServPollInt based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16284),
    )


_AccSntpServPollInt_Type.__name__ = "Integer32"
_AccSntpServPollInt_Object = MibTableColumn
accSntpServPollInt = _AccSntpServPollInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 4),
    _AccSntpServPollInt_Type()
)
accSntpServPollInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServPollInt.setStatus("mandatory")


class _AccSntpServRetryCnt_Type(Integer32):
    """Custom type accSntpServRetryCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AccSntpServRetryCnt_Type.__name__ = "Integer32"
_AccSntpServRetryCnt_Object = MibTableColumn
accSntpServRetryCnt = _AccSntpServRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 5),
    _AccSntpServRetryCnt_Type()
)
accSntpServRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServRetryCnt.setStatus("mandatory")


class _AccSntpServRetryInt_Type(Integer32):
    """Custom type accSntpServRetryInt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AccSntpServRetryInt_Type.__name__ = "Integer32"
_AccSntpServRetryInt_Object = MibTableColumn
accSntpServRetryInt = _AccSntpServRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 6),
    _AccSntpServRetryInt_Type()
)
accSntpServRetryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServRetryInt.setStatus("mandatory")


class _AccSntpServRecInt_Type(Integer32):
    """Custom type accSntpServRecInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3600),
    )


_AccSntpServRecInt_Type.__name__ = "Integer32"
_AccSntpServRecInt_Object = MibTableColumn
accSntpServRecInt = _AccSntpServRecInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 7),
    _AccSntpServRecInt_Type()
)
accSntpServRecInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServRecInt.setStatus("mandatory")


class _AccSntpServUdpPort_Type(Integer32):
    """Custom type accSntpServUdpPort based on Integer32"""
    defaultValue = 123

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_AccSntpServUdpPort_Type.__name__ = "Integer32"
_AccSntpServUdpPort_Object = MibTableColumn
accSntpServUdpPort = _AccSntpServUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 8),
    _AccSntpServUdpPort_Type()
)
accSntpServUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServUdpPort.setStatus("mandatory")
_AccSntpServLastResp_Type = OctetString
_AccSntpServLastResp_Object = MibTableColumn
accSntpServLastResp = _AccSntpServLastResp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 9),
    _AccSntpServLastResp_Type()
)
accSntpServLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpServLastResp.setStatus("mandatory")


class _AccSntpServOperState_Type(Integer32):
    """Custom type accSntpServOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("trying", 2),
          ("unknown", 1),
          ("up", 3))
    )


_AccSntpServOperState_Type.__name__ = "Integer32"
_AccSntpServOperState_Object = MibTableColumn
accSntpServOperState = _AccSntpServOperState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 10),
    _AccSntpServOperState_Type()
)
accSntpServOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServOperState.setStatus("mandatory")
_AccSntpServInPackets_Type = Counter32
_AccSntpServInPackets_Object = MibTableColumn
accSntpServInPackets = _AccSntpServInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 11),
    _AccSntpServInPackets_Type()
)
accSntpServInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpServInPackets.setStatus("mandatory")
_AccSntpServOutPackets_Type = Counter32
_AccSntpServOutPackets_Object = MibTableColumn
accSntpServOutPackets = _AccSntpServOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 12),
    _AccSntpServOutPackets_Type()
)
accSntpServOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpServOutPackets.setStatus("mandatory")
_AccSntpServInDiscards_Type = Counter32
_AccSntpServInDiscards_Object = MibTableColumn
accSntpServInDiscards = _AccSntpServInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 13),
    _AccSntpServInDiscards_Type()
)
accSntpServInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpServInDiscards.setStatus("mandatory")
_AccSntpServEntryStatus_Type = RowStatus
_AccSntpServEntryStatus_Object = MibTableColumn
accSntpServEntryStatus = _AccSntpServEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 2, 1, 1, 14),
    _AccSntpServEntryStatus_Type()
)
accSntpServEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSntpServEntryStatus.setStatus("mandatory")
_AccSntpTraps_ObjectIdentity = ObjectIdentity
accSntpTraps = _AccSntpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 3)
)
_AccSntpTrapMsg_Type = DisplayString
_AccSntpTrapMsg_Object = MibScalar
accSntpTrapMsg = _AccSntpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 3, 1),
    _AccSntpTrapMsg_Type()
)
accSntpTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSntpTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accSntpUdpBindFailTrap1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 3, 0, 1)
)
accSntpUdpBindFailTrap1.setObjects(
      *(("ACC-SNTP", "accSntpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accSntpUdpBindFailTrap1.setStatus(
        ""
    )

accSntpUdpUnBindFailTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 3, 0, 2)
)
accSntpUdpUnBindFailTrap2.setObjects(
      *(("ACC-SNTP", "accSntpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accSntpUdpUnBindFailTrap2.setStatus(
        ""
    )

accSntpServerDownTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 88, 3, 0, 3)
)
accSntpServerDownTrap3.setObjects(
      *(("ACC-SNTP", "accSntpTrapMsg"),
        ("ACC-SNTP", "accSntpServAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accSntpServerDownTrap3.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SNTP",
    **{"accSntp": accSntp,
       "accSntpGeneralScalars": accSntpGeneralScalars,
       "accSntpAdminState": accSntpAdminState,
       "accSntpBroadcastMode": accSntpBroadcastMode,
       "accSntpMessageLevel": accSntpMessageLevel,
       "accSntpDebugMask": accSntpDebugMask,
       "accSntpStatInPackets": accSntpStatInPackets,
       "accSntpStatOutPackets": accSntpStatOutPackets,
       "accSntpStatInDiscards": accSntpStatInDiscards,
       "accSntpStatInBcastPackets": accSntpStatInBcastPackets,
       "accSntpLastBcastPacTime": accSntpLastBcastPacTime,
       "accSntpLastBcastPacSrcAddr": accSntpLastBcastPacSrcAddr,
       "accSntpStatQueryTimeouts": accSntpStatQueryTimeouts,
       "accSntpSever": accSntpSever,
       "accSntpSeverTable": accSntpSeverTable,
       "accSntpSeverEntry": accSntpSeverEntry,
       "accSntpServIndex": accSntpServIndex,
       "accSntpServAddr": accSntpServAddr,
       "accSntpServAdminState": accSntpServAdminState,
       "accSntpServPollInt": accSntpServPollInt,
       "accSntpServRetryCnt": accSntpServRetryCnt,
       "accSntpServRetryInt": accSntpServRetryInt,
       "accSntpServRecInt": accSntpServRecInt,
       "accSntpServUdpPort": accSntpServUdpPort,
       "accSntpServLastResp": accSntpServLastResp,
       "accSntpServOperState": accSntpServOperState,
       "accSntpServInPackets": accSntpServInPackets,
       "accSntpServOutPackets": accSntpServOutPackets,
       "accSntpServInDiscards": accSntpServInDiscards,
       "accSntpServEntryStatus": accSntpServEntryStatus,
       "accSntpTraps": accSntpTraps,
       "accSntpUdpBindFailTrap1": accSntpUdpBindFailTrap1,
       "accSntpUdpUnBindFailTrap2": accSntpUdpUnBindFailTrap2,
       "accSntpServerDownTrap3": accSntpServerDownTrap3,
       "accSntpTrapMsg": accSntpTrapMsg}
)
