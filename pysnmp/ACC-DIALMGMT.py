# SNMP MIB module (ACC-DIALMGMT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-DIALMGMT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:04 2024
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

_AccDl2_ObjectIdentity = ObjectIdentity
accDl2 = _AccDl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70)
)
_AccDl2Sys_ObjectIdentity = ObjectIdentity
accDl2Sys = _AccDl2Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1)
)


class _AccDl2SysCICBase_Type(Integer32):
    """Custom type accDl2SysCICBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccDl2SysCICBase_Type.__name__ = "Integer32"
_AccDl2SysCICBase_Object = MibScalar
accDl2SysCICBase = _AccDl2SysCICBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 1),
    _AccDl2SysCICBase_Type()
)
accDl2SysCICBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysCICBase.setStatus("mandatory")


class _AccDl2SysEvenTCPPort_Type(Integer32):
    """Custom type accDl2SysEvenTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccDl2SysEvenTCPPort_Type.__name__ = "Integer32"
_AccDl2SysEvenTCPPort_Object = MibScalar
accDl2SysEvenTCPPort = _AccDl2SysEvenTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 2),
    _AccDl2SysEvenTCPPort_Type()
)
accDl2SysEvenTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysEvenTCPPort.setStatus("mandatory")


class _AccDl2SysOddTCPPort_Type(Integer32):
    """Custom type accDl2SysOddTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccDl2SysOddTCPPort_Type.__name__ = "Integer32"
_AccDl2SysOddTCPPort_Object = MibScalar
accDl2SysOddTCPPort = _AccDl2SysOddTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 3),
    _AccDl2SysOddTCPPort_Type()
)
accDl2SysOddTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysOddTCPPort.setStatus("mandatory")


class _AccDl2SysRetrasnsmitTime_Type(Integer32):
    """Custom type accDl2SysRetrasnsmitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_AccDl2SysRetrasnsmitTime_Type.__name__ = "Integer32"
_AccDl2SysRetrasnsmitTime_Object = MibScalar
accDl2SysRetrasnsmitTime = _AccDl2SysRetrasnsmitTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 4),
    _AccDl2SysRetrasnsmitTime_Type()
)
accDl2SysRetrasnsmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysRetrasnsmitTime.setStatus("mandatory")


class _AccDl2SysCircuitTimeout_Type(Integer32):
    """Custom type accDl2SysCircuitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AccDl2SysCircuitTimeout_Type.__name__ = "Integer32"
_AccDl2SysCircuitTimeout_Object = MibScalar
accDl2SysCircuitTimeout = _AccDl2SysCircuitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 5),
    _AccDl2SysCircuitTimeout_Type()
)
accDl2SysCircuitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysCircuitTimeout.setStatus("mandatory")


class _AccDl2SysT7_Type(Integer32):
    """Custom type accDl2SysT7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 30),
    )


_AccDl2SysT7_Type.__name__ = "Integer32"
_AccDl2SysT7_Object = MibScalar
accDl2SysT7 = _AccDl2SysT7_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 6),
    _AccDl2SysT7_Type()
)
accDl2SysT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysT7.setStatus("mandatory")


class _AccDl2SysT9_Type(Integer32):
    """Custom type accDl2SysT9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 240),
    )


_AccDl2SysT9_Type.__name__ = "Integer32"
_AccDl2SysT9_Object = MibScalar
accDl2SysT9 = _AccDl2SysT9_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 7),
    _AccDl2SysT9_Type()
)
accDl2SysT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysT9.setStatus("mandatory")
_AccDl2SysTestEvenAddr_Type = IpAddress
_AccDl2SysTestEvenAddr_Object = MibScalar
accDl2SysTestEvenAddr = _AccDl2SysTestEvenAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 8),
    _AccDl2SysTestEvenAddr_Type()
)
accDl2SysTestEvenAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysTestEvenAddr.setStatus("mandatory")
_AccDl2SysTestOddAddr_Type = IpAddress
_AccDl2SysTestOddAddr_Object = MibScalar
accDl2SysTestOddAddr = _AccDl2SysTestOddAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 9),
    _AccDl2SysTestOddAddr_Type()
)
accDl2SysTestOddAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2SysTestOddAddr.setStatus("mandatory")
_AccDl2SysCompletedCalls_Type = Counter32
_AccDl2SysCompletedCalls_Object = MibScalar
accDl2SysCompletedCalls = _AccDl2SysCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 10),
    _AccDl2SysCompletedCalls_Type()
)
accDl2SysCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysCompletedCalls.setStatus("mandatory")
_AccDl2SysClearedCalls_Type = Counter32
_AccDl2SysClearedCalls_Object = MibScalar
accDl2SysClearedCalls = _AccDl2SysClearedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 11),
    _AccDl2SysClearedCalls_Type()
)
accDl2SysClearedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysClearedCalls.setStatus("mandatory")
_AccDl2SysOriginatedCalls_Type = Counter32
_AccDl2SysOriginatedCalls_Object = MibScalar
accDl2SysOriginatedCalls = _AccDl2SysOriginatedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 12),
    _AccDl2SysOriginatedCalls_Type()
)
accDl2SysOriginatedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysOriginatedCalls.setStatus("mandatory")
_AccDl2SysRoutedCalls_Type = Counter32
_AccDl2SysRoutedCalls_Object = MibScalar
accDl2SysRoutedCalls = _AccDl2SysRoutedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 13),
    _AccDl2SysRoutedCalls_Type()
)
accDl2SysRoutedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysRoutedCalls.setStatus("mandatory")
_AccDl2SysOfferedCalls_Type = Counter32
_AccDl2SysOfferedCalls_Object = MibScalar
accDl2SysOfferedCalls = _AccDl2SysOfferedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 14),
    _AccDl2SysOfferedCalls_Type()
)
accDl2SysOfferedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysOfferedCalls.setStatus("mandatory")
_AccDl2SysAcceptedCalls_Type = Counter32
_AccDl2SysAcceptedCalls_Object = MibScalar
accDl2SysAcceptedCalls = _AccDl2SysAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 15),
    _AccDl2SysAcceptedCalls_Type()
)
accDl2SysAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysAcceptedCalls.setStatus("mandatory")
_AccDl2SysRetransmissions_Type = Counter32
_AccDl2SysRetransmissions_Object = MibScalar
accDl2SysRetransmissions = _AccDl2SysRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 16),
    _AccDl2SysRetransmissions_Type()
)
accDl2SysRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysRetransmissions.setStatus("mandatory")
_AccDl2SysTimeouts_Type = Counter32
_AccDl2SysTimeouts_Object = MibScalar
accDl2SysTimeouts = _AccDl2SysTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 17),
    _AccDl2SysTimeouts_Type()
)
accDl2SysTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysTimeouts.setStatus("mandatory")
_AccDl2SysUnexpEvents_Type = Counter32
_AccDl2SysUnexpEvents_Object = MibScalar
accDl2SysUnexpEvents = _AccDl2SysUnexpEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 18),
    _AccDl2SysUnexpEvents_Type()
)
accDl2SysUnexpEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysUnexpEvents.setStatus("mandatory")
_AccDl2SysBadMessages_Type = Counter32
_AccDl2SysBadMessages_Object = MibScalar
accDl2SysBadMessages = _AccDl2SysBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 19),
    _AccDl2SysBadMessages_Type()
)
accDl2SysBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysBadMessages.setStatus("mandatory")
_AccDl2SysBadCICs_Type = Counter32
_AccDl2SysBadCICs_Object = MibScalar
accDl2SysBadCICs = _AccDl2SysBadCICs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 1, 20),
    _AccDl2SysBadCICs_Type()
)
accDl2SysBadCICs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2SysBadCICs.setStatus("mandatory")
_AccDl2InfcTable_Object = MibTable
accDl2InfcTable = _AccDl2InfcTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2)
)
if mibBuilder.loadTexts:
    accDl2InfcTable.setStatus("mandatory")
_AccDl2InfcEntry_Object = MibTableRow
accDl2InfcEntry = _AccDl2InfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1)
)
accDl2InfcEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accDl2InfcIndex"),
)
if mibBuilder.loadTexts:
    accDl2InfcEntry.setStatus("mandatory")
_AccDl2InfcIndex_Type = Integer32
_AccDl2InfcIndex_Object = MibTableColumn
accDl2InfcIndex = _AccDl2InfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1, 1),
    _AccDl2InfcIndex_Type()
)
accDl2InfcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2InfcIndex.setStatus("mandatory")


class _AccDl2InfcAdminStatus_Type(Integer32):
    """Custom type accDl2InfcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drained", 3),
          ("enabled", 1))
    )


_AccDl2InfcAdminStatus_Type.__name__ = "Integer32"
_AccDl2InfcAdminStatus_Object = MibTableColumn
accDl2InfcAdminStatus = _AccDl2InfcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1, 2),
    _AccDl2InfcAdminStatus_Type()
)
accDl2InfcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2InfcAdminStatus.setStatus("mandatory")


class _AccDl2InfcCDNG_Type(Integer32):
    """Custom type accDl2InfcCDNG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccDl2InfcCDNG_Type.__name__ = "Integer32"
_AccDl2InfcCDNG_Object = MibTableColumn
accDl2InfcCDNG = _AccDl2InfcCDNG_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1, 3),
    _AccDl2InfcCDNG_Type()
)
accDl2InfcCDNG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2InfcCDNG.setStatus("mandatory")


class _AccDl2InfcCICBase_Type(Integer32):
    """Custom type accDl2InfcCICBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_AccDl2InfcCICBase_Type.__name__ = "Integer32"
_AccDl2InfcCICBase_Object = MibTableColumn
accDl2InfcCICBase = _AccDl2InfcCICBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1, 4),
    _AccDl2InfcCICBase_Type()
)
accDl2InfcCICBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2InfcCICBase.setStatus("mandatory")


class _AccDl2InfcMsgLvl_Type(Integer32):
    """Custom type accDl2InfcMsgLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccDl2InfcMsgLvl_Type.__name__ = "Integer32"
_AccDl2InfcMsgLvl_Object = MibTableColumn
accDl2InfcMsgLvl = _AccDl2InfcMsgLvl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 2, 1, 5),
    _AccDl2InfcMsgLvl_Type()
)
accDl2InfcMsgLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2InfcMsgLvl.setStatus("mandatory")
_AccDl2CrctTable_Object = MibTable
accDl2CrctTable = _AccDl2CrctTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3)
)
if mibBuilder.loadTexts:
    accDl2CrctTable.setStatus("mandatory")
_AccDl2CrctEntry_Object = MibTableRow
accDl2CrctEntry = _AccDl2CrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1)
)
accDl2CrctEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accDl2CrctIndex"),
)
if mibBuilder.loadTexts:
    accDl2CrctEntry.setStatus("mandatory")
_AccDl2CrctIndex_Type = Integer32
_AccDl2CrctIndex_Object = MibTableColumn
accDl2CrctIndex = _AccDl2CrctIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1, 1),
    _AccDl2CrctIndex_Type()
)
accDl2CrctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CrctIndex.setStatus("mandatory")
_AccDl2CrctInfc_Type = Integer32
_AccDl2CrctInfc_Object = MibTableColumn
accDl2CrctInfc = _AccDl2CrctInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1, 2),
    _AccDl2CrctInfc_Type()
)
accDl2CrctInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CrctInfc.setStatus("mandatory")
_AccDl2CrctTimeslot_Type = Integer32
_AccDl2CrctTimeslot_Object = MibTableColumn
accDl2CrctTimeslot = _AccDl2CrctTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1, 3),
    _AccDl2CrctTimeslot_Type()
)
accDl2CrctTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CrctTimeslot.setStatus("mandatory")


class _AccDl2CrctStatus_Type(Integer32):
    """Custom type accDl2CrctStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("reset", 3),
          ("unblocked", 2))
    )


_AccDl2CrctStatus_Type.__name__ = "Integer32"
_AccDl2CrctStatus_Object = MibTableColumn
accDl2CrctStatus = _AccDl2CrctStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1, 4),
    _AccDl2CrctStatus_Type()
)
accDl2CrctStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2CrctStatus.setStatus("mandatory")


class _AccDl2CrctState_Type(Integer32):
    """Custom type accDl2CrctState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("idle", 2))
    )


_AccDl2CrctState_Type.__name__ = "Integer32"
_AccDl2CrctState_Object = MibTableColumn
accDl2CrctState = _AccDl2CrctState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 3, 1, 5),
    _AccDl2CrctState_Type()
)
accDl2CrctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CrctState.setStatus("mandatory")
_AccDl2CallTable_Object = MibTable
accDl2CallTable = _AccDl2CallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4)
)
if mibBuilder.loadTexts:
    accDl2CallTable.setStatus("mandatory")
_AccDl2CallEntry_Object = MibTableRow
accDl2CallEntry = _AccDl2CallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1)
)
accDl2CallEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accDl2CallIndex"),
)
if mibBuilder.loadTexts:
    accDl2CallEntry.setStatus("mandatory")
_AccDl2CallIndex_Type = Integer32
_AccDl2CallIndex_Object = MibTableColumn
accDl2CallIndex = _AccDl2CallIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 1),
    _AccDl2CallIndex_Type()
)
accDl2CallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallIndex.setStatus("mandatory")
_AccDl2CallInfc_Type = Integer32
_AccDl2CallInfc_Object = MibTableColumn
accDl2CallInfc = _AccDl2CallInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 2),
    _AccDl2CallInfc_Type()
)
accDl2CallInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallInfc.setStatus("mandatory")
_AccDl2CallTimeslot_Type = Integer32
_AccDl2CallTimeslot_Object = MibTableColumn
accDl2CallTimeslot = _AccDl2CallTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 3),
    _AccDl2CallTimeslot_Type()
)
accDl2CallTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallTimeslot.setStatus("mandatory")
_AccDl2CallEndpoint_Type = Integer32
_AccDl2CallEndpoint_Object = MibTableColumn
accDl2CallEndpoint = _AccDl2CallEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 4),
    _AccDl2CallEndpoint_Type()
)
accDl2CallEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDl2CallEndpoint.setStatus("mandatory")


class _AccDl2CallType_Type(Integer32):
    """Custom type accDl2CallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 2),
          ("data", 1),
          ("voice", 3))
    )


_AccDl2CallType_Type.__name__ = "Integer32"
_AccDl2CallType_Object = MibTableColumn
accDl2CallType = _AccDl2CallType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 5),
    _AccDl2CallType_Type()
)
accDl2CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallType.setStatus("mandatory")


class _AccDl2CallDirection_Type(Integer32):
    """Custom type accDl2CallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AccDl2CallDirection_Type.__name__ = "Integer32"
_AccDl2CallDirection_Object = MibTableColumn
accDl2CallDirection = _AccDl2CallDirection_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 6),
    _AccDl2CallDirection_Type()
)
accDl2CallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallDirection.setStatus("mandatory")
_AccDl2CallAddress_Type = OctetString
_AccDl2CallAddress_Object = MibTableColumn
accDl2CallAddress = _AccDl2CallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 7),
    _AccDl2CallAddress_Type()
)
accDl2CallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallAddress.setStatus("mandatory")


class _AccDl2CallState_Type(Integer32):
    """Custom type accDl2CallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("incoming", 1),
          ("outgoing", 2),
          ("releasing", 5),
          ("routing", 3))
    )


_AccDl2CallState_Type.__name__ = "Integer32"
_AccDl2CallState_Object = MibTableColumn
accDl2CallState = _AccDl2CallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 8),
    _AccDl2CallState_Type()
)
accDl2CallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallState.setStatus("mandatory")
_AccDl2CallDuration_Type = TimeTicks
_AccDl2CallDuration_Object = MibTableColumn
accDl2CallDuration = _AccDl2CallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 70, 4, 1, 9),
    _AccDl2CallDuration_Type()
)
accDl2CallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDl2CallDuration.setStatus("mandatory")
_AccDialMgmt_ObjectIdentity = ObjectIdentity
accDialMgmt = _AccDialMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80)
)
_AccSignalingGroups_ObjectIdentity = ObjectIdentity
accSignalingGroups = _AccSignalingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1)
)
_AccSignalGroupTable_Object = MibTable
accSignalGroupTable = _AccSignalGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1)
)
if mibBuilder.loadTexts:
    accSignalGroupTable.setStatus("mandatory")
_AccSignalGroupEntry_Object = MibTableRow
accSignalGroupEntry = _AccSignalGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1)
)
accSignalGroupEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accSignalGroupIndex"),
)
if mibBuilder.loadTexts:
    accSignalGroupEntry.setStatus("mandatory")
_AccSignalGroupIndex_Type = Integer32
_AccSignalGroupIndex_Object = MibTableColumn
accSignalGroupIndex = _AccSignalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 1),
    _AccSignalGroupIndex_Type()
)
accSignalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupIndex.setStatus("mandatory")


class _AccSignalGroupType_Type(Integer32):
    """Custom type accSignalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("vna", 2)
    )


_AccSignalGroupType_Type.__name__ = "Integer32"
_AccSignalGroupType_Object = MibTableColumn
accSignalGroupType = _AccSignalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 2),
    _AccSignalGroupType_Type()
)
accSignalGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupType.setStatus("mandatory")


class _AccSignalGroupEntryStatus_Type(Integer32):
    """Custom type accSignalGroupEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccSignalGroupEntryStatus_Type.__name__ = "Integer32"
_AccSignalGroupEntryStatus_Object = MibTableColumn
accSignalGroupEntryStatus = _AccSignalGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 3),
    _AccSignalGroupEntryStatus_Type()
)
accSignalGroupEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupEntryStatus.setStatus("mandatory")


class _AccSignalGroupAdminStatus_Type(Integer32):
    """Custom type accSignalGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drained", 3),
          ("enabled", 1))
    )


_AccSignalGroupAdminStatus_Type.__name__ = "Integer32"
_AccSignalGroupAdminStatus_Object = MibTableColumn
accSignalGroupAdminStatus = _AccSignalGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 4),
    _AccSignalGroupAdminStatus_Type()
)
accSignalGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupAdminStatus.setStatus("mandatory")
_AccSignalGroupAuthName_Type = OctetString
_AccSignalGroupAuthName_Object = MibTableColumn
accSignalGroupAuthName = _AccSignalGroupAuthName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 5),
    _AccSignalGroupAuthName_Type()
)
accSignalGroupAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupAuthName.setStatus("mandatory")
_AccSignalGroupAuthPassword_Type = OctetString
_AccSignalGroupAuthPassword_Object = MibTableColumn
accSignalGroupAuthPassword = _AccSignalGroupAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 6),
    _AccSignalGroupAuthPassword_Type()
)
accSignalGroupAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupAuthPassword.setStatus("mandatory")


class _AccSignalGroupOperStatus_Type(Integer32):
    """Custom type accSignalGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("activated", 3),
          ("activating", 2),
          ("deactivated", 1),
          ("deactivating", 8),
          ("draining", 6),
          ("engaged", 5),
          ("established", 4),
          ("releasing", 7))
    )


_AccSignalGroupOperStatus_Type.__name__ = "Integer32"
_AccSignalGroupOperStatus_Object = MibTableColumn
accSignalGroupOperStatus = _AccSignalGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 7),
    _AccSignalGroupOperStatus_Type()
)
accSignalGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOperStatus.setStatus("mandatory")
_AccSignalGroupPollInterval_Type = TimeTicks
_AccSignalGroupPollInterval_Object = MibTableColumn
accSignalGroupPollInterval = _AccSignalGroupPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 8),
    _AccSignalGroupPollInterval_Type()
)
accSignalGroupPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupPollInterval.setStatus("mandatory")
_AccSignalGroupWaitInterval_Type = TimeTicks
_AccSignalGroupWaitInterval_Object = MibTableColumn
accSignalGroupWaitInterval = _AccSignalGroupWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 9),
    _AccSignalGroupWaitInterval_Type()
)
accSignalGroupWaitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupWaitInterval.setStatus("mandatory")
_AccSignalGroupRetryCount_Type = Integer32
_AccSignalGroupRetryCount_Object = MibTableColumn
accSignalGroupRetryCount = _AccSignalGroupRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 10),
    _AccSignalGroupRetryCount_Type()
)
accSignalGroupRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupRetryCount.setStatus("mandatory")
_AccSignalGroupRetryInterval_Type = TimeTicks
_AccSignalGroupRetryInterval_Object = MibTableColumn
accSignalGroupRetryInterval = _AccSignalGroupRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 11),
    _AccSignalGroupRetryInterval_Type()
)
accSignalGroupRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupRetryInterval.setStatus("mandatory")
_AccSignalGroupRetryBackoff_Type = TimeTicks
_AccSignalGroupRetryBackoff_Object = MibTableColumn
accSignalGroupRetryBackoff = _AccSignalGroupRetryBackoff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 12),
    _AccSignalGroupRetryBackoff_Type()
)
accSignalGroupRetryBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupRetryBackoff.setStatus("mandatory")
_AccSignalGroupPriIpAddress_Type = OctetString
_AccSignalGroupPriIpAddress_Object = MibTableColumn
accSignalGroupPriIpAddress = _AccSignalGroupPriIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 13),
    _AccSignalGroupPriIpAddress_Type()
)
accSignalGroupPriIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupPriIpAddress.setStatus("mandatory")
_AccSignalGroupPriTcpPort_Type = Integer32
_AccSignalGroupPriTcpPort_Object = MibTableColumn
accSignalGroupPriTcpPort = _AccSignalGroupPriTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 14),
    _AccSignalGroupPriTcpPort_Type()
)
accSignalGroupPriTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupPriTcpPort.setStatus("mandatory")
_AccSignalGroupSecIpAddress_Type = OctetString
_AccSignalGroupSecIpAddress_Object = MibTableColumn
accSignalGroupSecIpAddress = _AccSignalGroupSecIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 15),
    _AccSignalGroupSecIpAddress_Type()
)
accSignalGroupSecIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupSecIpAddress.setStatus("mandatory")
_AccSignalGroupSecTcpPort_Type = Integer32
_AccSignalGroupSecTcpPort_Object = MibTableColumn
accSignalGroupSecTcpPort = _AccSignalGroupSecTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 16),
    _AccSignalGroupSecTcpPort_Type()
)
accSignalGroupSecTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupSecTcpPort.setStatus("mandatory")
_AccSignalGroupCdnGroup_Type = Integer32
_AccSignalGroupCdnGroup_Object = MibTableColumn
accSignalGroupCdnGroup = _AccSignalGroupCdnGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 17),
    _AccSignalGroupCdnGroup_Type()
)
accSignalGroupCdnGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupCdnGroup.setStatus("mandatory")


class _AccSignalGroupLastCause_Type(Integer32):
    """Custom type accSignalGroupLastCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              19,
              21,
              22,
              26,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              41,
              42,
              43,
              44,
              45,
              47,
              49,
              50,
              52,
              54,
              57,
              58,
              63,
              65,
              66,
              69,
              70,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              88,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-available", 58),
          ("bearer-capability-not-implemented", 65),
          ("call-awarded-being-delivered", 7),
          ("call-identity-in-use", 84),
          ("call-identity-non-existent", 83),
          ("call-rejected", 21),
          ("channel-does-not-exist", 82),
          ("channel-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("ciruit-or-channel-preempted", 45),
          ("destination-out-of-order", 27),
          ("facility-not-implemented", 69),
          ("facility-not-subscribed", 50),
          ("facility-rejected", 29),
          ("incoming-call-barred", 54),
          ("incompatible-destination", 88),
          ("incompatible-or-nonexistent-message", 98),
          ("information-element-length-error", 103),
          ("information-element-not-implemented", 99),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-information-element-contents", 100),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network", 91),
          ("manditory-information-element-missing", 96),
          ("message-incompatible-with-call-state", 101),
          ("message-nonexistent-or-not-supported", 97),
          ("network-congestion", 42),
          ("network-out-of-order", 38),
          ("no-call-suspended", 85),
          ("no-circuit-or-channel-available", 34),
          ("no-route-to-destination", 3),
          ("no-route-to-transit-network", 2),
          ("no-user-responding", 18),
          ("non-selected-user-clearing", 26),
          ("normal-call-clearing", 16),
          ("normal-clearing-unspecified", 31),
          ("number-changed", 22),
          ("outgoing-call-barred", 52),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-unavailable", 49),
          ("requested-channel-not-available", 44),
          ("resources-unavailable", 47),
          ("response-to-status-enquiry", 30),
          ("restricted-digital-information-only", 70),
          ("service-not-available", 63),
          ("service-not-implemented", 79),
          ("suspended-call-cleared", 86),
          ("temporary-failure", 41),
          ("timer-expiration", 102),
          ("unassigned-number", 1),
          ("user-alerted-no-answer", 19),
          ("user-busy", 17))
    )


_AccSignalGroupLastCause_Type.__name__ = "Integer32"
_AccSignalGroupLastCause_Object = MibTableColumn
accSignalGroupLastCause = _AccSignalGroupLastCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 18),
    _AccSignalGroupLastCause_Type()
)
accSignalGroupLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupLastCause.setStatus("mandatory")
_AccSignalGroupMsgLevel_Type = Integer32
_AccSignalGroupMsgLevel_Object = MibTableColumn
accSignalGroupMsgLevel = _AccSignalGroupMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 1, 1, 19),
    _AccSignalGroupMsgLevel_Type()
)
accSignalGroupMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSignalGroupMsgLevel.setStatus("mandatory")
_AccSignalGroupStatTable_Object = MibTable
accSignalGroupStatTable = _AccSignalGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2)
)
if mibBuilder.loadTexts:
    accSignalGroupStatTable.setStatus("mandatory")
_AccSignalGroupStatEntry_Object = MibTableRow
accSignalGroupStatEntry = _AccSignalGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1)
)
accSignalGroupStatEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accSignalGroupStatIndex"),
)
if mibBuilder.loadTexts:
    accSignalGroupStatEntry.setStatus("mandatory")
_AccSignalGroupStatIndex_Type = Integer32
_AccSignalGroupStatIndex_Object = MibTableColumn
accSignalGroupStatIndex = _AccSignalGroupStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 1),
    _AccSignalGroupStatIndex_Type()
)
accSignalGroupStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupStatIndex.setStatus("mandatory")
_AccSignalGroupInMessages_Type = Counter32
_AccSignalGroupInMessages_Object = MibTableColumn
accSignalGroupInMessages = _AccSignalGroupInMessages_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 2),
    _AccSignalGroupInMessages_Type()
)
accSignalGroupInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupInMessages.setStatus("mandatory")
_AccSignalGroupInOctets_Type = Counter32
_AccSignalGroupInOctets_Object = MibTableColumn
accSignalGroupInOctets = _AccSignalGroupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 3),
    _AccSignalGroupInOctets_Type()
)
accSignalGroupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupInOctets.setStatus("mandatory")
_AccSignalGroupInErrors_Type = Counter32
_AccSignalGroupInErrors_Object = MibTableColumn
accSignalGroupInErrors = _AccSignalGroupInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 4),
    _AccSignalGroupInErrors_Type()
)
accSignalGroupInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupInErrors.setStatus("mandatory")
_AccSignalGroupOutMessages_Type = Counter32
_AccSignalGroupOutMessages_Object = MibTableColumn
accSignalGroupOutMessages = _AccSignalGroupOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 5),
    _AccSignalGroupOutMessages_Type()
)
accSignalGroupOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOutMessages.setStatus("mandatory")
_AccSignalGroupOutOctets_Type = Counter32
_AccSignalGroupOutOctets_Object = MibTableColumn
accSignalGroupOutOctets = _AccSignalGroupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 6),
    _AccSignalGroupOutOctets_Type()
)
accSignalGroupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOutOctets.setStatus("mandatory")
_AccSignalGroupOutErrors_Type = Counter32
_AccSignalGroupOutErrors_Object = MibTableColumn
accSignalGroupOutErrors = _AccSignalGroupOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 7),
    _AccSignalGroupOutErrors_Type()
)
accSignalGroupOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOutErrors.setStatus("mandatory")
_AccSignalGroupOriginatedCalls_Type = Counter32
_AccSignalGroupOriginatedCalls_Object = MibTableColumn
accSignalGroupOriginatedCalls = _AccSignalGroupOriginatedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 8),
    _AccSignalGroupOriginatedCalls_Type()
)
accSignalGroupOriginatedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOriginatedCalls.setStatus("mandatory")
_AccSignalGroupOfferedCalls_Type = Counter32
_AccSignalGroupOfferedCalls_Object = MibTableColumn
accSignalGroupOfferedCalls = _AccSignalGroupOfferedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 9),
    _AccSignalGroupOfferedCalls_Type()
)
accSignalGroupOfferedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupOfferedCalls.setStatus("mandatory")
_AccSignalGroupRoutedCalls_Type = Counter32
_AccSignalGroupRoutedCalls_Object = MibTableColumn
accSignalGroupRoutedCalls = _AccSignalGroupRoutedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 10),
    _AccSignalGroupRoutedCalls_Type()
)
accSignalGroupRoutedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupRoutedCalls.setStatus("mandatory")
_AccSignalGroupAcceptedCalls_Type = Counter32
_AccSignalGroupAcceptedCalls_Object = MibTableColumn
accSignalGroupAcceptedCalls = _AccSignalGroupAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 11),
    _AccSignalGroupAcceptedCalls_Type()
)
accSignalGroupAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupAcceptedCalls.setStatus("mandatory")
_AccSignalGroupConnectedCalls_Type = Counter32
_AccSignalGroupConnectedCalls_Object = MibTableColumn
accSignalGroupConnectedCalls = _AccSignalGroupConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 12),
    _AccSignalGroupConnectedCalls_Type()
)
accSignalGroupConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupConnectedCalls.setStatus("mandatory")
_AccSignalGroupClearedCalls_Type = Counter32
_AccSignalGroupClearedCalls_Object = MibTableColumn
accSignalGroupClearedCalls = _AccSignalGroupClearedCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 2, 1, 13),
    _AccSignalGroupClearedCalls_Type()
)
accSignalGroupClearedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupClearedCalls.setStatus("mandatory")
_AccSignalGroupCallTable_Object = MibTable
accSignalGroupCallTable = _AccSignalGroupCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3)
)
if mibBuilder.loadTexts:
    accSignalGroupCallTable.setStatus("mandatory")
_AccSignalGroupCallEntry_Object = MibTableRow
accSignalGroupCallEntry = _AccSignalGroupCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1)
)
accSignalGroupCallEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accSignalGroupCallIndex"),
)
if mibBuilder.loadTexts:
    accSignalGroupCallEntry.setStatus("mandatory")
_AccSignalGroupCallIndex_Type = Integer32
_AccSignalGroupCallIndex_Object = MibTableColumn
accSignalGroupCallIndex = _AccSignalGroupCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 1),
    _AccSignalGroupCallIndex_Type()
)
accSignalGroupCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallIndex.setStatus("mandatory")
_AccSignalGroupCallIdent_Type = Integer32
_AccSignalGroupCallIdent_Object = MibTableColumn
accSignalGroupCallIdent = _AccSignalGroupCallIdent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 2),
    _AccSignalGroupCallIdent_Type()
)
accSignalGroupCallIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallIdent.setStatus("mandatory")


class _AccSignalGroupCallDirection_Type(Integer32):
    """Custom type accSignalGroupCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AccSignalGroupCallDirection_Type.__name__ = "Integer32"
_AccSignalGroupCallDirection_Object = MibTableColumn
accSignalGroupCallDirection = _AccSignalGroupCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 3),
    _AccSignalGroupCallDirection_Type()
)
accSignalGroupCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallDirection.setStatus("mandatory")
_AccSignalGroupCallDialEndpt_Type = Integer32
_AccSignalGroupCallDialEndpt_Object = MibTableColumn
accSignalGroupCallDialEndpt = _AccSignalGroupCallDialEndpt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 4),
    _AccSignalGroupCallDialEndpt_Type()
)
accSignalGroupCallDialEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallDialEndpt.setStatus("mandatory")
_AccSignalGroupCallChannelId_Type = Integer32
_AccSignalGroupCallChannelId_Object = MibTableColumn
accSignalGroupCallChannelId = _AccSignalGroupCallChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 5),
    _AccSignalGroupCallChannelId_Type()
)
accSignalGroupCallChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallChannelId.setStatus("mandatory")
_AccSignalGroupCallTermEndpt_Type = Integer32
_AccSignalGroupCallTermEndpt_Object = MibTableColumn
accSignalGroupCallTermEndpt = _AccSignalGroupCallTermEndpt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 6),
    _AccSignalGroupCallTermEndpt_Type()
)
accSignalGroupCallTermEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallTermEndpt.setStatus("mandatory")


class _AccSignalGroupCallState_Type(Integer32):
    """Custom type accSignalGroupCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              17,
              19,
              25,
              99)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 7),
          ("answered", 8),
          ("busy", 99),
          ("connected", 10),
          ("delivered", 4),
          ("disconn-ind", 12),
          ("disconn-req", 11),
          ("initiated", 1),
          ("offered", 6),
          ("proceeding", 3),
          ("receiving", 25),
          ("releasing", 19),
          ("resume", 17),
          ("routing", 9),
          ("sending", 2),
          ("suspend", 15))
    )


_AccSignalGroupCallState_Type.__name__ = "Integer32"
_AccSignalGroupCallState_Object = MibTableColumn
accSignalGroupCallState = _AccSignalGroupCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 7),
    _AccSignalGroupCallState_Type()
)
accSignalGroupCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallState.setStatus("mandatory")


class _AccSignalGroupCallCause_Type(Integer32):
    """Custom type accSignalGroupCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              16,
              17,
              18,
              19,
              21,
              22,
              26,
              27,
              28,
              29,
              30,
              31,
              34,
              38,
              41,
              42,
              43,
              44,
              45,
              47,
              49,
              50,
              52,
              54,
              57,
              58,
              63,
              65,
              66,
              69,
              70,
              79,
              81,
              82,
              83,
              84,
              85,
              86,
              88,
              91,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("access-information-discarded", 43),
          ("bearer-capability-not-authorized", 57),
          ("bearer-capability-not-available", 58),
          ("bearer-capability-not-implemented", 65),
          ("call-awarded-being-delivered", 7),
          ("call-identity-in-use", 84),
          ("call-identity-non-existent", 83),
          ("call-rejected", 21),
          ("channel-does-not-exist", 82),
          ("channel-not-implemented", 66),
          ("channel-unacceptable", 6),
          ("ciruit-or-channel-preempted", 45),
          ("destination-out-of-order", 27),
          ("facility-not-implemented", 69),
          ("facility-not-subscribed", 50),
          ("facility-rejected", 29),
          ("incoming-call-barred", 54),
          ("incompatible-destination", 88),
          ("incompatible-or-nonexistent-message", 98),
          ("information-element-length-error", 103),
          ("information-element-not-implemented", 99),
          ("interworking-unspecified", 127),
          ("invalid-call-reference", 81),
          ("invalid-information-element-contents", 100),
          ("invalid-message-unspecified", 95),
          ("invalid-number-format", 28),
          ("invalid-transit-network", 91),
          ("manditory-information-element-missing", 96),
          ("message-incompatible-with-call-state", 101),
          ("message-nonexistent-or-not-supported", 97),
          ("network-congestion", 42),
          ("network-out-of-order", 38),
          ("no-call-suspended", 85),
          ("no-circuit-or-channel-available", 34),
          ("no-route-to-destination", 3),
          ("no-route-to-transit-network", 2),
          ("no-user-responding", 18),
          ("non-selected-user-clearing", 26),
          ("normal-call-clearing", 16),
          ("normal-clearing-unspecified", 31),
          ("number-changed", 22),
          ("outgoing-call-barred", 52),
          ("protocol-error-unspecified", 111),
          ("quality-of-service-unavailable", 49),
          ("requested-channel-not-available", 44),
          ("resources-unavailable", 47),
          ("response-to-status-enquiry", 30),
          ("restricted-digital-information-only", 70),
          ("service-not-available", 63),
          ("service-not-implemented", 79),
          ("suspended-call-cleared", 86),
          ("temporary-failure", 41),
          ("timer-expiration", 102),
          ("unassigned-number", 1),
          ("user-alerted-no-answer", 19),
          ("user-busy", 17))
    )


_AccSignalGroupCallCause_Type.__name__ = "Integer32"
_AccSignalGroupCallCause_Object = MibTableColumn
accSignalGroupCallCause = _AccSignalGroupCallCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 8),
    _AccSignalGroupCallCause_Type()
)
accSignalGroupCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallCause.setStatus("mandatory")
_AccSignalGroupCallCdNumber_Type = OctetString
_AccSignalGroupCallCdNumber_Object = MibTableColumn
accSignalGroupCallCdNumber = _AccSignalGroupCallCdNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 9),
    _AccSignalGroupCallCdNumber_Type()
)
accSignalGroupCallCdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallCdNumber.setStatus("mandatory")
_AccSignalGroupCallCgNumber_Type = OctetString
_AccSignalGroupCallCgNumber_Object = MibTableColumn
accSignalGroupCallCgNumber = _AccSignalGroupCallCgNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 10),
    _AccSignalGroupCallCgNumber_Type()
)
accSignalGroupCallCgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallCgNumber.setStatus("mandatory")


class _AccSignalGroupCallInfoType_Type(Integer32):
    """Custom type accSignalGroupCallInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("audio3", 4),
          ("audio7", 5),
          ("rdi", 3),
          ("speech", 1),
          ("udi", 2),
          ("video", 6))
    )


_AccSignalGroupCallInfoType_Type.__name__ = "Integer32"
_AccSignalGroupCallInfoType_Object = MibTableColumn
accSignalGroupCallInfoType = _AccSignalGroupCallInfoType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 11),
    _AccSignalGroupCallInfoType_Type()
)
accSignalGroupCallInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallInfoType.setStatus("mandatory")


class _AccSignalGroupCallInfoMode_Type(Integer32):
    """Custom type accSignalGroupCallInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("packet", 2))
    )


_AccSignalGroupCallInfoMode_Type.__name__ = "Integer32"
_AccSignalGroupCallInfoMode_Object = MibTableColumn
accSignalGroupCallInfoMode = _AccSignalGroupCallInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 12),
    _AccSignalGroupCallInfoMode_Type()
)
accSignalGroupCallInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallInfoMode.setStatus("mandatory")
_AccSignalGroupCallInfoRate_Type = Integer32
_AccSignalGroupCallInfoRate_Object = MibTableColumn
accSignalGroupCallInfoRate = _AccSignalGroupCallInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 13),
    _AccSignalGroupCallInfoRate_Type()
)
accSignalGroupCallInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallInfoRate.setStatus("mandatory")


class _AccSignalGroupCallL1Proto_Type(Integer32):
    """Custom type accSignalGroupCallL1Proto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("g-711a", 3),
          ("g-711mu", 2),
          ("g-721", 4),
          ("g-722", 5),
          ("h-261", 6),
          ("non-ccitt", 7),
          ("v-110", 1),
          ("v-120", 8),
          ("x-31", 9))
    )


_AccSignalGroupCallL1Proto_Type.__name__ = "Integer32"
_AccSignalGroupCallL1Proto_Object = MibTableColumn
accSignalGroupCallL1Proto = _AccSignalGroupCallL1Proto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 14),
    _AccSignalGroupCallL1Proto_Type()
)
accSignalGroupCallL1Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallL1Proto.setStatus("mandatory")


class _AccSignalGroupCallL1Framing_Type(Integer32):
    """Custom type accSignalGroupCallL1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1))
    )


_AccSignalGroupCallL1Framing_Type.__name__ = "Integer32"
_AccSignalGroupCallL1Framing_Object = MibTableColumn
accSignalGroupCallL1Framing = _AccSignalGroupCallL1Framing_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 15),
    _AccSignalGroupCallL1Framing_Type()
)
accSignalGroupCallL1Framing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallL1Framing.setStatus("mandatory")
_AccSignalGroupCallUserRate_Type = Integer32
_AccSignalGroupCallUserRate_Object = MibTableColumn
accSignalGroupCallUserRate = _AccSignalGroupCallUserRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 16),
    _AccSignalGroupCallUserRate_Type()
)
accSignalGroupCallUserRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallUserRate.setStatus("mandatory")
_AccSignalGroupCallDuration_Type = TimeTicks
_AccSignalGroupCallDuration_Object = MibTableColumn
accSignalGroupCallDuration = _AccSignalGroupCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 3, 1, 17),
    _AccSignalGroupCallDuration_Type()
)
accSignalGroupCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupCallDuration.setStatus("mandatory")
_AccSignalGroupMediaTable_Object = MibTable
accSignalGroupMediaTable = _AccSignalGroupMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4)
)
if mibBuilder.loadTexts:
    accSignalGroupMediaTable.setStatus("mandatory")
_AccSignalGroupMediaEntry_Object = MibTableRow
accSignalGroupMediaEntry = _AccSignalGroupMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1)
)
accSignalGroupMediaEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accSignalGroupMediaIndex"),
)
if mibBuilder.loadTexts:
    accSignalGroupMediaEntry.setStatus("mandatory")
_AccSignalGroupMediaIndex_Type = Integer32
_AccSignalGroupMediaIndex_Object = MibTableColumn
accSignalGroupMediaIndex = _AccSignalGroupMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 1),
    _AccSignalGroupMediaIndex_Type()
)
accSignalGroupMediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaIndex.setStatus("mandatory")
_AccSignalGroupMediaIdent_Type = Integer32
_AccSignalGroupMediaIdent_Object = MibTableColumn
accSignalGroupMediaIdent = _AccSignalGroupMediaIdent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 2),
    _AccSignalGroupMediaIdent_Type()
)
accSignalGroupMediaIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaIdent.setStatus("mandatory")


class _AccSignalGroupMediaType_Type(Integer32):
    """Custom type accSignalGroupMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 3),
          ("video", 2))
    )


_AccSignalGroupMediaType_Type.__name__ = "Integer32"
_AccSignalGroupMediaType_Object = MibTableColumn
accSignalGroupMediaType = _AccSignalGroupMediaType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 3),
    _AccSignalGroupMediaType_Type()
)
accSignalGroupMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaType.setStatus("mandatory")


class _AccSignalGroupMediaCodecType_Type(Integer32):
    """Custom type accSignalGroupMediaCodecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fax-g3", 5),
          ("g-711", 1),
          ("g-722", 4),
          ("g-723-1a", 8),
          ("g-723-1m", 3),
          ("g-726", 7),
          ("g-729a", 6),
          ("sx7300", 2))
    )


_AccSignalGroupMediaCodecType_Type.__name__ = "Integer32"
_AccSignalGroupMediaCodecType_Object = MibTableColumn
accSignalGroupMediaCodecType = _AccSignalGroupMediaCodecType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 4),
    _AccSignalGroupMediaCodecType_Type()
)
accSignalGroupMediaCodecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaCodecType.setStatus("mandatory")


class _AccSignalGroupMediaPayldType_Type(Integer32):
    """Custom type accSignalGroupMediaPayldType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 2),
          ("tcp", 3),
          ("udp", 1))
    )


_AccSignalGroupMediaPayldType_Type.__name__ = "Integer32"
_AccSignalGroupMediaPayldType_Object = MibTableColumn
accSignalGroupMediaPayldType = _AccSignalGroupMediaPayldType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 5),
    _AccSignalGroupMediaPayldType_Type()
)
accSignalGroupMediaPayldType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaPayldType.setStatus("mandatory")


class _AccSignalGroupMediaPayldTos_Type(Integer32):
    """Custom type accSignalGroupMediaPayldTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-delay", 2),
          ("normal", 1))
    )


_AccSignalGroupMediaPayldTos_Type.__name__ = "Integer32"
_AccSignalGroupMediaPayldTos_Object = MibTableColumn
accSignalGroupMediaPayldTos = _AccSignalGroupMediaPayldTos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 6),
    _AccSignalGroupMediaPayldTos_Type()
)
accSignalGroupMediaPayldTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaPayldTos.setStatus("mandatory")
_AccSignalGroupMediaFrameSize_Type = Integer32
_AccSignalGroupMediaFrameSize_Object = MibTableColumn
accSignalGroupMediaFrameSize = _AccSignalGroupMediaFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 7),
    _AccSignalGroupMediaFrameSize_Type()
)
accSignalGroupMediaFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaFrameSize.setStatus("mandatory")
_AccSignalGroupMediaIpAddress_Type = OctetString
_AccSignalGroupMediaIpAddress_Object = MibTableColumn
accSignalGroupMediaIpAddress = _AccSignalGroupMediaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 8),
    _AccSignalGroupMediaIpAddress_Type()
)
accSignalGroupMediaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaIpAddress.setStatus("mandatory")
_AccSignalGroupMediaUdpPort_Type = Integer32
_AccSignalGroupMediaUdpPort_Object = MibTableColumn
accSignalGroupMediaUdpPort = _AccSignalGroupMediaUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 9),
    _AccSignalGroupMediaUdpPort_Type()
)
accSignalGroupMediaUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaUdpPort.setStatus("mandatory")


class _AccSignalGroupMediaSilSupr_Type(Integer32):
    """Custom type accSignalGroupMediaSilSupr based on Integer32"""
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


_AccSignalGroupMediaSilSupr_Type.__name__ = "Integer32"
_AccSignalGroupMediaSilSupr_Object = MibTableColumn
accSignalGroupMediaSilSupr = _AccSignalGroupMediaSilSupr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 10),
    _AccSignalGroupMediaSilSupr_Type()
)
accSignalGroupMediaSilSupr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaSilSupr.setStatus("mandatory")


class _AccSignalGroupMediaDtmfSupr_Type(Integer32):
    """Custom type accSignalGroupMediaDtmfSupr based on Integer32"""
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


_AccSignalGroupMediaDtmfSupr_Type.__name__ = "Integer32"
_AccSignalGroupMediaDtmfSupr_Object = MibTableColumn
accSignalGroupMediaDtmfSupr = _AccSignalGroupMediaDtmfSupr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 11),
    _AccSignalGroupMediaDtmfSupr_Type()
)
accSignalGroupMediaDtmfSupr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaDtmfSupr.setStatus("mandatory")


class _AccSignalGroupMediaXmitSupr_Type(Integer32):
    """Custom type accSignalGroupMediaXmitSupr based on Integer32"""
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


_AccSignalGroupMediaXmitSupr_Type.__name__ = "Integer32"
_AccSignalGroupMediaXmitSupr_Object = MibTableColumn
accSignalGroupMediaXmitSupr = _AccSignalGroupMediaXmitSupr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 12),
    _AccSignalGroupMediaXmitSupr_Type()
)
accSignalGroupMediaXmitSupr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaXmitSupr.setStatus("mandatory")


class _AccSignalGroupMediaRecvSupr_Type(Integer32):
    """Custom type accSignalGroupMediaRecvSupr based on Integer32"""
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


_AccSignalGroupMediaRecvSupr_Type.__name__ = "Integer32"
_AccSignalGroupMediaRecvSupr_Object = MibTableColumn
accSignalGroupMediaRecvSupr = _AccSignalGroupMediaRecvSupr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 13),
    _AccSignalGroupMediaRecvSupr_Type()
)
accSignalGroupMediaRecvSupr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaRecvSupr.setStatus("mandatory")


class _AccSignalGroupMediaEchoSupr_Type(Integer32):
    """Custom type accSignalGroupMediaEchoSupr based on Integer32"""
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


_AccSignalGroupMediaEchoSupr_Type.__name__ = "Integer32"
_AccSignalGroupMediaEchoSupr_Object = MibTableColumn
accSignalGroupMediaEchoSupr = _AccSignalGroupMediaEchoSupr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 1, 4, 1, 14),
    _AccSignalGroupMediaEchoSupr_Type()
)
accSignalGroupMediaEchoSupr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSignalGroupMediaEchoSupr.setStatus("mandatory")
_AccLineGroups_ObjectIdentity = ObjectIdentity
accLineGroups = _AccLineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2)
)
_AccLineGroupTable_Object = MibTable
accLineGroupTable = _AccLineGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1)
)
if mibBuilder.loadTexts:
    accLineGroupTable.setStatus("mandatory")
_AccLineGroupEntry_Object = MibTableRow
accLineGroupEntry = _AccLineGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1)
)
accLineGroupEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accLineGroupIndex"),
)
if mibBuilder.loadTexts:
    accLineGroupEntry.setStatus("mandatory")
_AccLineGroupIndex_Type = Integer32
_AccLineGroupIndex_Object = MibTableColumn
accLineGroupIndex = _AccLineGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 1),
    _AccLineGroupIndex_Type()
)
accLineGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupIndex.setStatus("mandatory")


class _AccLineGroupType_Type(Integer32):
    """Custom type accLineGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vna", 1)
    )


_AccLineGroupType_Type.__name__ = "Integer32"
_AccLineGroupType_Object = MibTableColumn
accLineGroupType = _AccLineGroupType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 2),
    _AccLineGroupType_Type()
)
accLineGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupType.setStatus("mandatory")


class _AccLineGroupEntryStatus_Type(Integer32):
    """Custom type accLineGroupEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccLineGroupEntryStatus_Type.__name__ = "Integer32"
_AccLineGroupEntryStatus_Object = MibTableColumn
accLineGroupEntryStatus = _AccLineGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 3),
    _AccLineGroupEntryStatus_Type()
)
accLineGroupEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupEntryStatus.setStatus("mandatory")


class _AccLineGroupAdminStatus_Type(Integer32):
    """Custom type accLineGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drained", 3),
          ("enabled", 1))
    )


_AccLineGroupAdminStatus_Type.__name__ = "Integer32"
_AccLineGroupAdminStatus_Object = MibTableColumn
accLineGroupAdminStatus = _AccLineGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 4),
    _AccLineGroupAdminStatus_Type()
)
accLineGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupAdminStatus.setStatus("mandatory")


class _AccLineGroupOperStatus_Type(Integer32):
    """Custom type accLineGroupOperStatus based on Integer32"""
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
        *(("activated", 3),
          ("activating", 2),
          ("deactivated", 1),
          ("deactivating", 4))
    )


_AccLineGroupOperStatus_Type.__name__ = "Integer32"
_AccLineGroupOperStatus_Object = MibTableColumn
accLineGroupOperStatus = _AccLineGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 5),
    _AccLineGroupOperStatus_Type()
)
accLineGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupOperStatus.setStatus("mandatory")
_AccLineGroupLineCount_Type = Integer32
_AccLineGroupLineCount_Object = MibTableColumn
accLineGroupLineCount = _AccLineGroupLineCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 6),
    _AccLineGroupLineCount_Type()
)
accLineGroupLineCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupLineCount.setStatus("mandatory")
_AccLineGroupBaseLic_Type = Integer32
_AccLineGroupBaseLic_Object = MibTableColumn
accLineGroupBaseLic = _AccLineGroupBaseLic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 7),
    _AccLineGroupBaseLic_Type()
)
accLineGroupBaseLic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupBaseLic.setStatus("mandatory")
_AccLineGroupSignalGroup_Type = Integer32
_AccLineGroupSignalGroup_Object = MibTableColumn
accLineGroupSignalGroup = _AccLineGroupSignalGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 8),
    _AccLineGroupSignalGroup_Type()
)
accLineGroupSignalGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupSignalGroup.setStatus("mandatory")
_AccLineGroupCdnGroup_Type = Integer32
_AccLineGroupCdnGroup_Object = MibTableColumn
accLineGroupCdnGroup = _AccLineGroupCdnGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 9),
    _AccLineGroupCdnGroup_Type()
)
accLineGroupCdnGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupCdnGroup.setStatus("mandatory")
_AccLineGroupIpAddress_Type = OctetString
_AccLineGroupIpAddress_Object = MibTableColumn
accLineGroupIpAddress = _AccLineGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 10),
    _AccLineGroupIpAddress_Type()
)
accLineGroupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupIpAddress.setStatus("mandatory")
_AccLineGroupUdpPort_Type = Integer32
_AccLineGroupUdpPort_Object = MibTableColumn
accLineGroupUdpPort = _AccLineGroupUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 11),
    _AccLineGroupUdpPort_Type()
)
accLineGroupUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupUdpPort.setStatus("mandatory")


class _AccLineGroupDefaultTos_Type(Integer32):
    """Custom type accLineGroupDefaultTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-delay", 2),
          ("normal", 1))
    )


_AccLineGroupDefaultTos_Type.__name__ = "Integer32"
_AccLineGroupDefaultTos_Object = MibTableColumn
accLineGroupDefaultTos = _AccLineGroupDefaultTos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 12),
    _AccLineGroupDefaultTos_Type()
)
accLineGroupDefaultTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupDefaultTos.setStatus("mandatory")
_AccLineGroupMsgLevel_Type = Integer32
_AccLineGroupMsgLevel_Object = MibTableColumn
accLineGroupMsgLevel = _AccLineGroupMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 13),
    _AccLineGroupMsgLevel_Type()
)
accLineGroupMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupMsgLevel.setStatus("mandatory")
_AccLineGroupActiveLines_Type = Counter32
_AccLineGroupActiveLines_Object = MibTableColumn
accLineGroupActiveLines = _AccLineGroupActiveLines_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 14),
    _AccLineGroupActiveLines_Type()
)
accLineGroupActiveLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupActiveLines.setStatus("mandatory")


class _AccLineGroupLineStatus_Type(Integer32):
    """Custom type accLineGroupLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 2),
          ("unallocated", 1))
    )


_AccLineGroupLineStatus_Type.__name__ = "Integer32"
_AccLineGroupLineStatus_Object = MibTableColumn
accLineGroupLineStatus = _AccLineGroupLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 15),
    _AccLineGroupLineStatus_Type()
)
accLineGroupLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupLineStatus.setStatus("mandatory")
_AccLineGroupAvailableLines_Type = Counter32
_AccLineGroupAvailableLines_Object = MibTableColumn
accLineGroupAvailableLines = _AccLineGroupAvailableLines_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 1, 1, 16),
    _AccLineGroupAvailableLines_Type()
)
accLineGroupAvailableLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupAvailableLines.setStatus("mandatory")
_AccLineGroupMediaTable_Object = MibTable
accLineGroupMediaTable = _AccLineGroupMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2)
)
if mibBuilder.loadTexts:
    accLineGroupMediaTable.setStatus("mandatory")
_AccLineGroupMediaEntry_Object = MibTableRow
accLineGroupMediaEntry = _AccLineGroupMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1)
)
accLineGroupMediaEntry.setIndexNames(
    (0, "ACC-DIALMGMT", "accLineGroupMediaIndex"),
    (0, "ACC-DIALMGMT", "accLineGroupMediaPreference"),
)
if mibBuilder.loadTexts:
    accLineGroupMediaEntry.setStatus("mandatory")
_AccLineGroupMediaIndex_Type = Integer32
_AccLineGroupMediaIndex_Object = MibTableColumn
accLineGroupMediaIndex = _AccLineGroupMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 1),
    _AccLineGroupMediaIndex_Type()
)
accLineGroupMediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupMediaIndex.setStatus("mandatory")
_AccLineGroupMediaPreference_Type = Integer32
_AccLineGroupMediaPreference_Object = MibTableColumn
accLineGroupMediaPreference = _AccLineGroupMediaPreference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 2),
    _AccLineGroupMediaPreference_Type()
)
accLineGroupMediaPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupMediaPreference.setStatus("mandatory")


class _AccLineGroupMediaType_Type(Integer32):
    """Custom type accLineGroupMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 3),
          ("video", 2))
    )


_AccLineGroupMediaType_Type.__name__ = "Integer32"
_AccLineGroupMediaType_Object = MibTableColumn
accLineGroupMediaType = _AccLineGroupMediaType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 3),
    _AccLineGroupMediaType_Type()
)
accLineGroupMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLineGroupMediaType.setStatus("mandatory")


class _AccLineGroupMediaStatus_Type(Integer32):
    """Custom type accLineGroupMediaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccLineGroupMediaStatus_Type.__name__ = "Integer32"
_AccLineGroupMediaStatus_Object = MibTableColumn
accLineGroupMediaStatus = _AccLineGroupMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 4),
    _AccLineGroupMediaStatus_Type()
)
accLineGroupMediaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupMediaStatus.setStatus("mandatory")


class _AccLineGroupMediaCodecType_Type(Integer32):
    """Custom type accLineGroupMediaCodecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("g-711", 1)
    )


_AccLineGroupMediaCodecType_Type.__name__ = "Integer32"
_AccLineGroupMediaCodecType_Object = MibTableColumn
accLineGroupMediaCodecType = _AccLineGroupMediaCodecType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 5),
    _AccLineGroupMediaCodecType_Type()
)
accLineGroupMediaCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupMediaCodecType.setStatus("mandatory")


class _AccLineGroupMediaPayldType_Type(Integer32):
    """Custom type accLineGroupMediaPayldType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 2),
          ("udp", 1))
    )


_AccLineGroupMediaPayldType_Type.__name__ = "Integer32"
_AccLineGroupMediaPayldType_Object = MibTableColumn
accLineGroupMediaPayldType = _AccLineGroupMediaPayldType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 6),
    _AccLineGroupMediaPayldType_Type()
)
accLineGroupMediaPayldType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupMediaPayldType.setStatus("mandatory")


class _AccLineGroupMediaPayldTos_Type(Integer32):
    """Custom type accLineGroupMediaPayldTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-delay", 2),
          ("normal", 1))
    )


_AccLineGroupMediaPayldTos_Type.__name__ = "Integer32"
_AccLineGroupMediaPayldTos_Object = MibTableColumn
accLineGroupMediaPayldTos = _AccLineGroupMediaPayldTos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 2, 2, 1, 7),
    _AccLineGroupMediaPayldTos_Type()
)
accLineGroupMediaPayldTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLineGroupMediaPayldTos.setStatus("mandatory")
_AccDmTraps_ObjectIdentity = ObjectIdentity
accDmTraps = _AccDmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3)
)
_AccDmTrapMsg_Type = DisplayString
_AccDmTrapMsg_Object = MibScalar
accDmTrapMsg = _AccDmTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 1),
    _AccDmTrapMsg_Type()
)
accDmTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDmTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accDmT7Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 1)
)
accDmT7Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT7Trap.setStatus(
        ""
    )

accDmT9Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 2)
)
accDmT9Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT9Trap.setStatus(
        ""
    )

accDmT5Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 3)
)
accDmT5Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT5Trap.setStatus(
        ""
    )

accDmT17Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 4)
)
accDmT17Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT17Trap.setStatus(
        ""
    )

accDmCmStaleCallCntxtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 5)
)
accDmCmStaleCallCntxtTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCmStaleCallCntxtTrap.setStatus(
        ""
    )

accDmCallCicTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 6)
)
accDmCallCicTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCallCicTrap.setStatus(
        ""
    )

accDmIamTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 7)
)
accDmIamTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmIamTrap.setStatus(
        ""
    )

accDmInvMessTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 8)
)
accDmInvMessTypeTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmInvMessTypeTrap.setStatus(
        ""
    )

accDmIamToAxeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 9)
)
accDmIamToAxeTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmIamToAxeTrap.setStatus(
        ""
    )

accDmBCBAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 10)
)
accDmBCBAllocTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmBCBAllocTrap.setStatus(
        ""
    )

accDmInvUbaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 11)
)
accDmInvUbaTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmInvUbaTrap.setStatus(
        ""
    )

accDmCcbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 12)
)
accDmCcbTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCcbTrap.setStatus(
        ""
    )

accDmBcbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 13)
)
accDmBcbTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmBcbTrap.setStatus(
        ""
    )

accDmInvTmrIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 14)
)
accDmInvTmrIdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmInvTmrIdTrap.setStatus(
        ""
    )

accDmStopTmrCCBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 15)
)
accDmStopTmrCCBTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmStopTmrCCBTrap.setStatus(
        ""
    )

accDmStopTmrBCBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 16)
)
accDmStopTmrBCBTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmStopTmrBCBTrap.setStatus(
        ""
    )

accDmInvStopTmrIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 17)
)
accDmInvStopTmrIdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmInvStopTmrIdTrap.setStatus(
        ""
    )

accDmNonTestCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 18)
)
accDmNonTestCallTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNonTestCallTrap.setStatus(
        ""
    )

accDmT13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 19)
)
accDmT13Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT13Trap.setStatus(
        ""
    )

accDmT15Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 20)
)
accDmT15Trap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmT15Trap.setStatus(
        ""
    )

accDmCbAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 21)
)
accDmCbAllocTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCbAllocTrap.setStatus(
        ""
    )

accDmMblkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 22)
)
accDmMblkTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmMblkTrap.setStatus(
        ""
    )

accDmFsmEvntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 23)
)
accDmFsmEvntTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmFsmEvntTrap.setStatus(
        ""
    )

accDmCicBaseRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 24)
)
accDmCicBaseRangeTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCicBaseRangeTrap.setStatus(
        ""
    )

accDmDisblLineGrpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 25)
)
accDmDisblLineGrpTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupIndex"),
        ("ACC-DIALMGMT", "accLineGroupAdminStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmDisblLineGrpTrap.setStatus(
        ""
    )

accDmLGrpNmsModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 26)
)
accDmLGrpNmsModifyTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupIndex"),
        ("ACC-DIALMGMT", "accLineGroupAdminStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLGrpNmsModifyTrap.setStatus(
        ""
    )

accDmLGrpLicRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 27)
)
accDmLGrpLicRangeTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupBaseLic"),
        ("ACC-DIALMGMT", "accLineGroupLineCount"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLGrpLicRangeTrap.setStatus(
        ""
    )

accDmLGrpNoLinesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 28)
)
accDmLGrpNoLinesTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupIndex"),
        ("ACC-DIALMGMT", "accLineGroupAdminStatus"),
        ("ACC-DIALMGMT", "accLineGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLGrpNoLinesTrap.setStatus(
        ""
    )

accDmLGrpDuplicatesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 29)
)
accDmLGrpDuplicatesTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupIndex"),
        ("ACC-DIALMGMT", "accLineGroupAdminStatus"),
        ("ACC-DIALMGMT", "accLineGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLGrpDuplicatesTrap.setStatus(
        ""
    )

accDmLGrpNoSgrpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 30)
)
accDmLGrpNoSgrpTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accLineGroupIndex"),
        ("ACC-DIALMGMT", "accLineGroupAdminStatus"),
        ("ACC-DIALMGMT", "accLineGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLGrpNoSgrpTrap.setStatus(
        ""
    )

accDmSGrpNmsDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 31)
)
accDmSGrpNmsDeleteTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accSignalGroupIndex"),
        ("ACC-DIALMGMT", "accSignalGroupAdminStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmSGrpNmsDeleteTrap.setStatus(
        ""
    )

accDmSGrpNmsModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 32)
)
accDmSGrpNmsModifyTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accSignalGroupIndex"),
        ("ACC-DIALMGMT", "accSignalGroupAdminStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmSGrpNmsModifyTrap.setStatus(
        ""
    )

accDmSGrpEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 33)
)
accDmSGrpEstablishedTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accSignalGroupIndex"),
        ("ACC-DIALMGMT", "accSignalGroupAdminStatus"),
        ("ACC-DIALMGMT", "accSignalGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmSGrpEstablishedTrap.setStatus(
        ""
    )

accDmSGrpReleasedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 34)
)
accDmSGrpReleasedTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accSignalGroupIndex"),
        ("ACC-DIALMGMT", "accSignalGroupAdminStatus"),
        ("ACC-DIALMGMT", "accSignalGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmSGrpReleasedTrap.setStatus(
        ""
    )

accDmSGrpDrainTmoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 35)
)
accDmSGrpDrainTmoutTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-DIALMGMT", "accSignalGroupIndex"),
        ("ACC-DIALMGMT", "accSignalGroupAdminStatus"),
        ("ACC-DIALMGMT", "accSignalGroupOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmSGrpDrainTmoutTrap.setStatus(
        ""
    )

accDmVdmStaleCmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 36)
)
accDmVdmStaleCmTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmVdmStaleCmTrap.setStatus(
        ""
    )

accDmVdmBadCmMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 37)
)
accDmVdmBadCmMsgTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmVdmBadCmMsgTrap.setStatus(
        ""
    )

accDmStaleDiaConTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 38)
)
accDmStaleDiaConTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmStaleDiaConTrap.setStatus(
        ""
    )

accDmOutGngCallRfsdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 39)
)
accDmOutGngCallRfsdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmOutGngCallRfsdTrap.setStatus(
        ""
    )

accDmCallRfsdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 40)
)
accDmCallRfsdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCallRfsdTrap.setStatus(
        ""
    )

accDmUnblRgstrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 41)
)
accDmUnblRgstrTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmUnblRgstrTrap.setStatus(
        ""
    )

accDmMnyPSTNIFsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 42)
)
accDmMnyPSTNIFsTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmMnyPSTNIFsTrap.setStatus(
        ""
    )

accDmR2regInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 43)
)
accDmR2regInitTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmR2regInitTrap.setStatus(
        ""
    )

accDmDTMFInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 44)
)
accDmDTMFInitTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmDTMFInitTrap.setStatus(
        ""
    )

accDmCallCtxInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 45)
)
accDmCallCtxInit.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCallCtxInit.setStatus(
        ""
    )

accDmPulDiaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 46)
)
accDmPulDiaTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmPulDiaTrap.setStatus(
        ""
    )

accDmDSPDiaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 47)
)
accDmDSPDiaTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmDSPDiaTrap.setStatus(
        ""
    )

accDmTestCallActvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 48)
)
accDmTestCallActvTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmTestCallActvTrap.setStatus(
        ""
    )

accDmNoTestCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 49)
)
accDmNoTestCallTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNoTestCallTrap.setStatus(
        ""
    )

accDmNoActvCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 50)
)
accDmNoActvCallTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNoActvCallTrap.setStatus(
        ""
    )

accDmNoPdngCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 51)
)
accDmNoPdngCallTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNoPdngCallTrap.setStatus(
        ""
    )

accDmNoDiaParamTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 52)
)
accDmNoDiaParamTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNoDiaParamTrap.setStatus(
        ""
    )

accDmISDNDiaInvdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 53)
)
accDmISDNDiaInvdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmISDNDiaInvdTrap.setStatus(
        ""
    )

accDmPSTNDiaInvldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 54)
)
accDmPSTNDiaInvldTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmPSTNDiaInvldTrap.setStatus(
        ""
    )

accDmTstngNotSpprtdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 55)
)
accDmTstngNotSpprtdTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmTstngNotSpprtdTrap.setStatus(
        ""
    )

accDmCmndSpprtNonISDNTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 56)
)
accDmCmndSpprtNonISDNTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmCmndSpprtNonISDNTrap.setStatus(
        ""
    )

accDmNotValdFITTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 57)
)
accDmNotValdFITTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmNotValdFITTrap.setStatus(
        ""
    )

accDmResrcShortageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 58)
)
accDmResrcShortageTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmResrcShortageTrap.setStatus(
        ""
    )

accDmPrvntReinitPpIndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 59)
)
accDmPrvntReinitPpIndTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmPrvntReinitPpIndTrap.setStatus(
        ""
    )

accDmLdspAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 60)
)
accDmLdspAllocTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmLdspAllocTrap.setStatus(
        ""
    )

accDmRegFsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 80, 3, 0, 61)
)
accDmRegFsmTrap.setObjects(
      *(("ACC-DIALMGMT", "accDmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDmRegFsmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-DIALMGMT",
    **{"accDl2": accDl2,
       "accDl2Sys": accDl2Sys,
       "accDl2SysCICBase": accDl2SysCICBase,
       "accDl2SysEvenTCPPort": accDl2SysEvenTCPPort,
       "accDl2SysOddTCPPort": accDl2SysOddTCPPort,
       "accDl2SysRetrasnsmitTime": accDl2SysRetrasnsmitTime,
       "accDl2SysCircuitTimeout": accDl2SysCircuitTimeout,
       "accDl2SysT7": accDl2SysT7,
       "accDl2SysT9": accDl2SysT9,
       "accDl2SysTestEvenAddr": accDl2SysTestEvenAddr,
       "accDl2SysTestOddAddr": accDl2SysTestOddAddr,
       "accDl2SysCompletedCalls": accDl2SysCompletedCalls,
       "accDl2SysClearedCalls": accDl2SysClearedCalls,
       "accDl2SysOriginatedCalls": accDl2SysOriginatedCalls,
       "accDl2SysRoutedCalls": accDl2SysRoutedCalls,
       "accDl2SysOfferedCalls": accDl2SysOfferedCalls,
       "accDl2SysAcceptedCalls": accDl2SysAcceptedCalls,
       "accDl2SysRetransmissions": accDl2SysRetransmissions,
       "accDl2SysTimeouts": accDl2SysTimeouts,
       "accDl2SysUnexpEvents": accDl2SysUnexpEvents,
       "accDl2SysBadMessages": accDl2SysBadMessages,
       "accDl2SysBadCICs": accDl2SysBadCICs,
       "accDl2InfcTable": accDl2InfcTable,
       "accDl2InfcEntry": accDl2InfcEntry,
       "accDl2InfcIndex": accDl2InfcIndex,
       "accDl2InfcAdminStatus": accDl2InfcAdminStatus,
       "accDl2InfcCDNG": accDl2InfcCDNG,
       "accDl2InfcCICBase": accDl2InfcCICBase,
       "accDl2InfcMsgLvl": accDl2InfcMsgLvl,
       "accDl2CrctTable": accDl2CrctTable,
       "accDl2CrctEntry": accDl2CrctEntry,
       "accDl2CrctIndex": accDl2CrctIndex,
       "accDl2CrctInfc": accDl2CrctInfc,
       "accDl2CrctTimeslot": accDl2CrctTimeslot,
       "accDl2CrctStatus": accDl2CrctStatus,
       "accDl2CrctState": accDl2CrctState,
       "accDl2CallTable": accDl2CallTable,
       "accDl2CallEntry": accDl2CallEntry,
       "accDl2CallIndex": accDl2CallIndex,
       "accDl2CallInfc": accDl2CallInfc,
       "accDl2CallTimeslot": accDl2CallTimeslot,
       "accDl2CallEndpoint": accDl2CallEndpoint,
       "accDl2CallType": accDl2CallType,
       "accDl2CallDirection": accDl2CallDirection,
       "accDl2CallAddress": accDl2CallAddress,
       "accDl2CallState": accDl2CallState,
       "accDl2CallDuration": accDl2CallDuration,
       "accDialMgmt": accDialMgmt,
       "accSignalingGroups": accSignalingGroups,
       "accSignalGroupTable": accSignalGroupTable,
       "accSignalGroupEntry": accSignalGroupEntry,
       "accSignalGroupIndex": accSignalGroupIndex,
       "accSignalGroupType": accSignalGroupType,
       "accSignalGroupEntryStatus": accSignalGroupEntryStatus,
       "accSignalGroupAdminStatus": accSignalGroupAdminStatus,
       "accSignalGroupAuthName": accSignalGroupAuthName,
       "accSignalGroupAuthPassword": accSignalGroupAuthPassword,
       "accSignalGroupOperStatus": accSignalGroupOperStatus,
       "accSignalGroupPollInterval": accSignalGroupPollInterval,
       "accSignalGroupWaitInterval": accSignalGroupWaitInterval,
       "accSignalGroupRetryCount": accSignalGroupRetryCount,
       "accSignalGroupRetryInterval": accSignalGroupRetryInterval,
       "accSignalGroupRetryBackoff": accSignalGroupRetryBackoff,
       "accSignalGroupPriIpAddress": accSignalGroupPriIpAddress,
       "accSignalGroupPriTcpPort": accSignalGroupPriTcpPort,
       "accSignalGroupSecIpAddress": accSignalGroupSecIpAddress,
       "accSignalGroupSecTcpPort": accSignalGroupSecTcpPort,
       "accSignalGroupCdnGroup": accSignalGroupCdnGroup,
       "accSignalGroupLastCause": accSignalGroupLastCause,
       "accSignalGroupMsgLevel": accSignalGroupMsgLevel,
       "accSignalGroupStatTable": accSignalGroupStatTable,
       "accSignalGroupStatEntry": accSignalGroupStatEntry,
       "accSignalGroupStatIndex": accSignalGroupStatIndex,
       "accSignalGroupInMessages": accSignalGroupInMessages,
       "accSignalGroupInOctets": accSignalGroupInOctets,
       "accSignalGroupInErrors": accSignalGroupInErrors,
       "accSignalGroupOutMessages": accSignalGroupOutMessages,
       "accSignalGroupOutOctets": accSignalGroupOutOctets,
       "accSignalGroupOutErrors": accSignalGroupOutErrors,
       "accSignalGroupOriginatedCalls": accSignalGroupOriginatedCalls,
       "accSignalGroupOfferedCalls": accSignalGroupOfferedCalls,
       "accSignalGroupRoutedCalls": accSignalGroupRoutedCalls,
       "accSignalGroupAcceptedCalls": accSignalGroupAcceptedCalls,
       "accSignalGroupConnectedCalls": accSignalGroupConnectedCalls,
       "accSignalGroupClearedCalls": accSignalGroupClearedCalls,
       "accSignalGroupCallTable": accSignalGroupCallTable,
       "accSignalGroupCallEntry": accSignalGroupCallEntry,
       "accSignalGroupCallIndex": accSignalGroupCallIndex,
       "accSignalGroupCallIdent": accSignalGroupCallIdent,
       "accSignalGroupCallDirection": accSignalGroupCallDirection,
       "accSignalGroupCallDialEndpt": accSignalGroupCallDialEndpt,
       "accSignalGroupCallChannelId": accSignalGroupCallChannelId,
       "accSignalGroupCallTermEndpt": accSignalGroupCallTermEndpt,
       "accSignalGroupCallState": accSignalGroupCallState,
       "accSignalGroupCallCause": accSignalGroupCallCause,
       "accSignalGroupCallCdNumber": accSignalGroupCallCdNumber,
       "accSignalGroupCallCgNumber": accSignalGroupCallCgNumber,
       "accSignalGroupCallInfoType": accSignalGroupCallInfoType,
       "accSignalGroupCallInfoMode": accSignalGroupCallInfoMode,
       "accSignalGroupCallInfoRate": accSignalGroupCallInfoRate,
       "accSignalGroupCallL1Proto": accSignalGroupCallL1Proto,
       "accSignalGroupCallL1Framing": accSignalGroupCallL1Framing,
       "accSignalGroupCallUserRate": accSignalGroupCallUserRate,
       "accSignalGroupCallDuration": accSignalGroupCallDuration,
       "accSignalGroupMediaTable": accSignalGroupMediaTable,
       "accSignalGroupMediaEntry": accSignalGroupMediaEntry,
       "accSignalGroupMediaIndex": accSignalGroupMediaIndex,
       "accSignalGroupMediaIdent": accSignalGroupMediaIdent,
       "accSignalGroupMediaType": accSignalGroupMediaType,
       "accSignalGroupMediaCodecType": accSignalGroupMediaCodecType,
       "accSignalGroupMediaPayldType": accSignalGroupMediaPayldType,
       "accSignalGroupMediaPayldTos": accSignalGroupMediaPayldTos,
       "accSignalGroupMediaFrameSize": accSignalGroupMediaFrameSize,
       "accSignalGroupMediaIpAddress": accSignalGroupMediaIpAddress,
       "accSignalGroupMediaUdpPort": accSignalGroupMediaUdpPort,
       "accSignalGroupMediaSilSupr": accSignalGroupMediaSilSupr,
       "accSignalGroupMediaDtmfSupr": accSignalGroupMediaDtmfSupr,
       "accSignalGroupMediaXmitSupr": accSignalGroupMediaXmitSupr,
       "accSignalGroupMediaRecvSupr": accSignalGroupMediaRecvSupr,
       "accSignalGroupMediaEchoSupr": accSignalGroupMediaEchoSupr,
       "accLineGroups": accLineGroups,
       "accLineGroupTable": accLineGroupTable,
       "accLineGroupEntry": accLineGroupEntry,
       "accLineGroupIndex": accLineGroupIndex,
       "accLineGroupType": accLineGroupType,
       "accLineGroupEntryStatus": accLineGroupEntryStatus,
       "accLineGroupAdminStatus": accLineGroupAdminStatus,
       "accLineGroupOperStatus": accLineGroupOperStatus,
       "accLineGroupLineCount": accLineGroupLineCount,
       "accLineGroupBaseLic": accLineGroupBaseLic,
       "accLineGroupSignalGroup": accLineGroupSignalGroup,
       "accLineGroupCdnGroup": accLineGroupCdnGroup,
       "accLineGroupIpAddress": accLineGroupIpAddress,
       "accLineGroupUdpPort": accLineGroupUdpPort,
       "accLineGroupDefaultTos": accLineGroupDefaultTos,
       "accLineGroupMsgLevel": accLineGroupMsgLevel,
       "accLineGroupActiveLines": accLineGroupActiveLines,
       "accLineGroupLineStatus": accLineGroupLineStatus,
       "accLineGroupAvailableLines": accLineGroupAvailableLines,
       "accLineGroupMediaTable": accLineGroupMediaTable,
       "accLineGroupMediaEntry": accLineGroupMediaEntry,
       "accLineGroupMediaIndex": accLineGroupMediaIndex,
       "accLineGroupMediaPreference": accLineGroupMediaPreference,
       "accLineGroupMediaType": accLineGroupMediaType,
       "accLineGroupMediaStatus": accLineGroupMediaStatus,
       "accLineGroupMediaCodecType": accLineGroupMediaCodecType,
       "accLineGroupMediaPayldType": accLineGroupMediaPayldType,
       "accLineGroupMediaPayldTos": accLineGroupMediaPayldTos,
       "accDmTraps": accDmTraps,
       "accDmT7Trap": accDmT7Trap,
       "accDmT9Trap": accDmT9Trap,
       "accDmT5Trap": accDmT5Trap,
       "accDmT17Trap": accDmT17Trap,
       "accDmCmStaleCallCntxtTrap": accDmCmStaleCallCntxtTrap,
       "accDmCallCicTrap": accDmCallCicTrap,
       "accDmIamTrap": accDmIamTrap,
       "accDmInvMessTypeTrap": accDmInvMessTypeTrap,
       "accDmIamToAxeTrap": accDmIamToAxeTrap,
       "accDmBCBAllocTrap": accDmBCBAllocTrap,
       "accDmInvUbaTrap": accDmInvUbaTrap,
       "accDmCcbTrap": accDmCcbTrap,
       "accDmBcbTrap": accDmBcbTrap,
       "accDmInvTmrIdTrap": accDmInvTmrIdTrap,
       "accDmStopTmrCCBTrap": accDmStopTmrCCBTrap,
       "accDmStopTmrBCBTrap": accDmStopTmrBCBTrap,
       "accDmInvStopTmrIdTrap": accDmInvStopTmrIdTrap,
       "accDmNonTestCallTrap": accDmNonTestCallTrap,
       "accDmT13Trap": accDmT13Trap,
       "accDmT15Trap": accDmT15Trap,
       "accDmCbAllocTrap": accDmCbAllocTrap,
       "accDmMblkTrap": accDmMblkTrap,
       "accDmFsmEvntTrap": accDmFsmEvntTrap,
       "accDmCicBaseRangeTrap": accDmCicBaseRangeTrap,
       "accDmDisblLineGrpTrap": accDmDisblLineGrpTrap,
       "accDmLGrpNmsModifyTrap": accDmLGrpNmsModifyTrap,
       "accDmLGrpLicRangeTrap": accDmLGrpLicRangeTrap,
       "accDmLGrpNoLinesTrap": accDmLGrpNoLinesTrap,
       "accDmLGrpDuplicatesTrap": accDmLGrpDuplicatesTrap,
       "accDmLGrpNoSgrpTrap": accDmLGrpNoSgrpTrap,
       "accDmSGrpNmsDeleteTrap": accDmSGrpNmsDeleteTrap,
       "accDmSGrpNmsModifyTrap": accDmSGrpNmsModifyTrap,
       "accDmSGrpEstablishedTrap": accDmSGrpEstablishedTrap,
       "accDmSGrpReleasedTrap": accDmSGrpReleasedTrap,
       "accDmSGrpDrainTmoutTrap": accDmSGrpDrainTmoutTrap,
       "accDmVdmStaleCmTrap": accDmVdmStaleCmTrap,
       "accDmVdmBadCmMsgTrap": accDmVdmBadCmMsgTrap,
       "accDmStaleDiaConTrap": accDmStaleDiaConTrap,
       "accDmOutGngCallRfsdTrap": accDmOutGngCallRfsdTrap,
       "accDmCallRfsdTrap": accDmCallRfsdTrap,
       "accDmUnblRgstrTrap": accDmUnblRgstrTrap,
       "accDmMnyPSTNIFsTrap": accDmMnyPSTNIFsTrap,
       "accDmR2regInitTrap": accDmR2regInitTrap,
       "accDmDTMFInitTrap": accDmDTMFInitTrap,
       "accDmCallCtxInit": accDmCallCtxInit,
       "accDmPulDiaTrap": accDmPulDiaTrap,
       "accDmDSPDiaTrap": accDmDSPDiaTrap,
       "accDmTestCallActvTrap": accDmTestCallActvTrap,
       "accDmNoTestCallTrap": accDmNoTestCallTrap,
       "accDmNoActvCallTrap": accDmNoActvCallTrap,
       "accDmNoPdngCallTrap": accDmNoPdngCallTrap,
       "accDmNoDiaParamTrap": accDmNoDiaParamTrap,
       "accDmISDNDiaInvdTrap": accDmISDNDiaInvdTrap,
       "accDmPSTNDiaInvldTrap": accDmPSTNDiaInvldTrap,
       "accDmTstngNotSpprtdTrap": accDmTstngNotSpprtdTrap,
       "accDmCmndSpprtNonISDNTrap": accDmCmndSpprtNonISDNTrap,
       "accDmNotValdFITTrap": accDmNotValdFITTrap,
       "accDmResrcShortageTrap": accDmResrcShortageTrap,
       "accDmPrvntReinitPpIndTrap": accDmPrvntReinitPpIndTrap,
       "accDmLdspAllocTrap": accDmLdspAllocTrap,
       "accDmRegFsmTrap": accDmRegFsmTrap,
       "accDmTrapMsg": accDmTrapMsg}
)
