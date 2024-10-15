# SNMP MIB module (ONEACCESS-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:00 2024
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

(atmVclEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(oacExpIMAtmOamStatistics,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMAtmOamStatistics",
    "oacMIBModules")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

oacOamMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 673)
)
oacOamMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacAtmOamStatObjects_ObjectIdentity = ObjectIdentity
oacAtmOamStatObjects = _OacAtmOamStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1)
)
_OacAtmOamStatSwitch_ObjectIdentity = ObjectIdentity
oacAtmOamStatSwitch = _OacAtmOamStatSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1)
)
_OacAtmOamSwitchMaxConnections_Type = Unsigned32
_OacAtmOamSwitchMaxConnections_Object = MibScalar
oacAtmOamSwitchMaxConnections = _OacAtmOamSwitchMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 1),
    _OacAtmOamSwitchMaxConnections_Type()
)
oacAtmOamSwitchMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchMaxConnections.setStatus("current")


class _OacAtmOamSwitchSegLoopback_Type(Integer32):
    """Custom type oacAtmOamSwitchSegLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamSwitchSegLoopback_Type.__name__ = "Integer32"
_OacAtmOamSwitchSegLoopback_Object = MibScalar
oacAtmOamSwitchSegLoopback = _OacAtmOamSwitchSegLoopback_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 2),
    _OacAtmOamSwitchSegLoopback_Type()
)
oacAtmOamSwitchSegLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchSegLoopback.setStatus("current")


class _OacAtmOamSwitchEndLoopback_Type(Integer32):
    """Custom type oacAtmOamSwitchEndLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamSwitchEndLoopback_Type.__name__ = "Integer32"
_OacAtmOamSwitchEndLoopback_Object = MibScalar
oacAtmOamSwitchEndLoopback = _OacAtmOamSwitchEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 3),
    _OacAtmOamSwitchEndLoopback_Type()
)
oacAtmOamSwitchEndLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchEndLoopback.setStatus("current")


class _OacAtmOamSwitchAisRdiEnable_Type(Integer32):
    """Custom type oacAtmOamSwitchAisRdiEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamSwitchAisRdiEnable_Type.__name__ = "Integer32"
_OacAtmOamSwitchAisRdiEnable_Object = MibScalar
oacAtmOamSwitchAisRdiEnable = _OacAtmOamSwitchAisRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 4),
    _OacAtmOamSwitchAisRdiEnable_Type()
)
oacAtmOamSwitchAisRdiEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchAisRdiEnable.setStatus("current")


class _OacAtmOamSwitchSegmentContinuityCheckEnable_Type(Integer32):
    """Custom type oacAtmOamSwitchSegmentContinuityCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamSwitchSegmentContinuityCheckEnable_Type.__name__ = "Integer32"
_OacAtmOamSwitchSegmentContinuityCheckEnable_Object = MibScalar
oacAtmOamSwitchSegmentContinuityCheckEnable = _OacAtmOamSwitchSegmentContinuityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 5),
    _OacAtmOamSwitchSegmentContinuityCheckEnable_Type()
)
oacAtmOamSwitchSegmentContinuityCheckEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchSegmentContinuityCheckEnable.setStatus("current")


class _OacAtmOamSwitchEndContinuityCheckEnable_Type(Integer32):
    """Custom type oacAtmOamSwitchEndContinuityCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamSwitchEndContinuityCheckEnable_Type.__name__ = "Integer32"
_OacAtmOamSwitchEndContinuityCheckEnable_Object = MibScalar
oacAtmOamSwitchEndContinuityCheckEnable = _OacAtmOamSwitchEndContinuityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 6),
    _OacAtmOamSwitchEndContinuityCheckEnable_Type()
)
oacAtmOamSwitchEndContinuityCheckEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchEndContinuityCheckEnable.setStatus("current")
_OacAtmOamSwitchOamCellsReceived_Type = Counter32
_OacAtmOamSwitchOamCellsReceived_Object = MibScalar
oacAtmOamSwitchOamCellsReceived = _OacAtmOamSwitchOamCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 7),
    _OacAtmOamSwitchOamCellsReceived_Type()
)
oacAtmOamSwitchOamCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchOamCellsReceived.setStatus("current")
_OacAtmOamSwitchOamCellsTransmitted_Type = Counter32
_OacAtmOamSwitchOamCellsTransmitted_Object = MibScalar
oacAtmOamSwitchOamCellsTransmitted = _OacAtmOamSwitchOamCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 8),
    _OacAtmOamSwitchOamCellsTransmitted_Type()
)
oacAtmOamSwitchOamCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchOamCellsTransmitted.setStatus("current")
_OacAtmOamSwitchCurrentConnections_Type = Unsigned32
_OacAtmOamSwitchCurrentConnections_Object = MibScalar
oacAtmOamSwitchCurrentConnections = _OacAtmOamSwitchCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 1, 9),
    _OacAtmOamSwitchCurrentConnections_Type()
)
oacAtmOamSwitchCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamSwitchCurrentConnections.setStatus("current")
_OacAtmOamVclTable_Object = MibTable
oacAtmOamVclTable = _OacAtmOamVclTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oacAtmOamVclTable.setStatus("current")
_OacAtmOamVclEntry_Object = MibTableRow
oacAtmOamVclEntry = _OacAtmOamVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oacAtmOamVclEntry.setStatus("current")


class _OacAtmOamVclPvcManage_Type(Integer32):
    """Custom type oacAtmOamVclPvcManage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclPvcManage_Type.__name__ = "Integer32"
_OacAtmOamVclPvcManage_Object = MibTableColumn
oacAtmOamVclPvcManage = _OacAtmOamVclPvcManage_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 1),
    _OacAtmOamVclPvcManage_Type()
)
oacAtmOamVclPvcManage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclPvcManage.setStatus("current")


class _OacAtmOamVclSegmentLoopback_Type(Integer32):
    """Custom type oacAtmOamVclSegmentLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclSegmentLoopback_Type.__name__ = "Integer32"
_OacAtmOamVclSegmentLoopback_Object = MibTableColumn
oacAtmOamVclSegmentLoopback = _OacAtmOamVclSegmentLoopback_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 2),
    _OacAtmOamVclSegmentLoopback_Type()
)
oacAtmOamVclSegmentLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegmentLoopback.setStatus("current")


class _OacAtmOamVclEndLoopback_Type(Integer32):
    """Custom type oacAtmOamVclEndLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclEndLoopback_Type.__name__ = "Integer32"
_OacAtmOamVclEndLoopback_Object = MibTableColumn
oacAtmOamVclEndLoopback = _OacAtmOamVclEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 3),
    _OacAtmOamVclEndLoopback_Type()
)
oacAtmOamVclEndLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndLoopback.setStatus("current")


class _OacAtmOamVclAisRdiEnable_Type(Integer32):
    """Custom type oacAtmOamVclAisRdiEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclAisRdiEnable_Type.__name__ = "Integer32"
_OacAtmOamVclAisRdiEnable_Object = MibTableColumn
oacAtmOamVclAisRdiEnable = _OacAtmOamVclAisRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 4),
    _OacAtmOamVclAisRdiEnable_Type()
)
oacAtmOamVclAisRdiEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAisRdiEnable.setStatus("current")


class _OacAtmOamVclSegmentContinuityCheckEnable_Type(Integer32):
    """Custom type oacAtmOamVclSegmentContinuityCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclSegmentContinuityCheckEnable_Type.__name__ = "Integer32"
_OacAtmOamVclSegmentContinuityCheckEnable_Object = MibTableColumn
oacAtmOamVclSegmentContinuityCheckEnable = _OacAtmOamVclSegmentContinuityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 5),
    _OacAtmOamVclSegmentContinuityCheckEnable_Type()
)
oacAtmOamVclSegmentContinuityCheckEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegmentContinuityCheckEnable.setStatus("current")


class _OacAtmOamVclEndContinuityCheckEnable_Type(Integer32):
    """Custom type oacAtmOamVclEndContinuityCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclEndContinuityCheckEnable_Type.__name__ = "Integer32"
_OacAtmOamVclEndContinuityCheckEnable_Object = MibTableColumn
oacAtmOamVclEndContinuityCheckEnable = _OacAtmOamVclEndContinuityCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 6),
    _OacAtmOamVclEndContinuityCheckEnable_Type()
)
oacAtmOamVclEndContinuityCheckEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndContinuityCheckEnable.setStatus("current")
_OacAtmOamVclLoopbackTxInterval_Type = Integer32
_OacAtmOamVclLoopbackTxInterval_Object = MibTableColumn
oacAtmOamVclLoopbackTxInterval = _OacAtmOamVclLoopbackTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 7),
    _OacAtmOamVclLoopbackTxInterval_Type()
)
oacAtmOamVclLoopbackTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclLoopbackTxInterval.setStatus("current")
_OacAtmOamVclLoopbackTxRetryFrequency_Type = Integer32
_OacAtmOamVclLoopbackTxRetryFrequency_Object = MibTableColumn
oacAtmOamVclLoopbackTxRetryFrequency = _OacAtmOamVclLoopbackTxRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 8),
    _OacAtmOamVclLoopbackTxRetryFrequency_Type()
)
oacAtmOamVclLoopbackTxRetryFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclLoopbackTxRetryFrequency.setStatus("current")
_OacAtmOamVclLoopbackTxRetryUpCount_Type = Integer32
_OacAtmOamVclLoopbackTxRetryUpCount_Object = MibTableColumn
oacAtmOamVclLoopbackTxRetryUpCount = _OacAtmOamVclLoopbackTxRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 9),
    _OacAtmOamVclLoopbackTxRetryUpCount_Type()
)
oacAtmOamVclLoopbackTxRetryUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclLoopbackTxRetryUpCount.setStatus("current")
_OacAtmOamVclLoopbackTxRetryDownCount_Type = Integer32
_OacAtmOamVclLoopbackTxRetryDownCount_Object = MibTableColumn
oacAtmOamVclLoopbackTxRetryDownCount = _OacAtmOamVclLoopbackTxRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 10),
    _OacAtmOamVclLoopbackTxRetryDownCount_Type()
)
oacAtmOamVclLoopbackTxRetryDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclLoopbackTxRetryDownCount.setStatus("current")
_OacAtmOamVclAlarmState_Type = Integer32
_OacAtmOamVclAlarmState_Object = MibTableColumn
oacAtmOamVclAlarmState = _OacAtmOamVclAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 11),
    _OacAtmOamVclAlarmState_Type()
)
oacAtmOamVclAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAlarmState.setStatus("current")
_OacAtmOamVclAlarmStateLastChange_Type = TimeStamp
_OacAtmOamVclAlarmStateLastChange_Object = MibTableColumn
oacAtmOamVclAlarmStateLastChange = _OacAtmOamVclAlarmStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 12),
    _OacAtmOamVclAlarmStateLastChange_Type()
)
oacAtmOamVclAlarmStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAlarmStateLastChange.setStatus("current")
_OacAtmOamVclAisRdiRetryDownCount_Type = Integer32
_OacAtmOamVclAisRdiRetryDownCount_Object = MibTableColumn
oacAtmOamVclAisRdiRetryDownCount = _OacAtmOamVclAisRdiRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 13),
    _OacAtmOamVclAisRdiRetryDownCount_Type()
)
oacAtmOamVclAisRdiRetryDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAisRdiRetryDownCount.setStatus("current")
_OacAtmOamVclAisRdiRetryUpTimer_Type = Integer32
_OacAtmOamVclAisRdiRetryUpTimer_Object = MibTableColumn
oacAtmOamVclAisRdiRetryUpTimer = _OacAtmOamVclAisRdiRetryUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 14),
    _OacAtmOamVclAisRdiRetryUpTimer_Type()
)
oacAtmOamVclAisRdiRetryUpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAisRdiRetryUpTimer.setStatus("current")


class _OacAtmOamVclPvcIntrusive_Type(Integer32):
    """Custom type oacAtmOamVclPvcIntrusive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OacAtmOamVclPvcIntrusive_Type.__name__ = "Integer32"
_OacAtmOamVclPvcIntrusive_Object = MibTableColumn
oacAtmOamVclPvcIntrusive = _OacAtmOamVclPvcIntrusive_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 2, 1, 15),
    _OacAtmOamVclPvcIntrusive_Type()
)
oacAtmOamVclPvcIntrusive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclPvcIntrusive.setStatus("current")
_OacAtmOamVclCountersTable_Object = MibTable
oacAtmOamVclCountersTable = _OacAtmOamVclCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    oacAtmOamVclCountersTable.setStatus("current")
_OacAtmOamVclCountersEntry_Object = MibTableRow
oacAtmOamVclCountersEntry = _OacAtmOamVclCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacAtmOamVclCountersEntry.setStatus("current")
_OacAtmOamVclOamCellsReceived_Type = Counter32
_OacAtmOamVclOamCellsReceived_Object = MibTableColumn
oacAtmOamVclOamCellsReceived = _OacAtmOamVclOamCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 1),
    _OacAtmOamVclOamCellsReceived_Type()
)
oacAtmOamVclOamCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclOamCellsReceived.setStatus("current")
_OacAtmOamVclEndLoopbackIn_Type = Counter32
_OacAtmOamVclEndLoopbackIn_Object = MibTableColumn
oacAtmOamVclEndLoopbackIn = _OacAtmOamVclEndLoopbackIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 2),
    _OacAtmOamVclEndLoopbackIn_Type()
)
oacAtmOamVclEndLoopbackIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndLoopbackIn.setStatus("current")
_OacAtmOamVclSegLoopbackIn_Type = Counter32
_OacAtmOamVclSegLoopbackIn_Object = MibTableColumn
oacAtmOamVclSegLoopbackIn = _OacAtmOamVclSegLoopbackIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 3),
    _OacAtmOamVclSegLoopbackIn_Type()
)
oacAtmOamVclSegLoopbackIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegLoopbackIn.setStatus("current")
_OacAtmOamVclEndLoopIn_Type = Counter32
_OacAtmOamVclEndLoopIn_Object = MibTableColumn
oacAtmOamVclEndLoopIn = _OacAtmOamVclEndLoopIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 4),
    _OacAtmOamVclEndLoopIn_Type()
)
oacAtmOamVclEndLoopIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndLoopIn.setStatus("current")
_OacAtmOamVclSegLoopIn_Type = Counter32
_OacAtmOamVclSegLoopIn_Object = MibTableColumn
oacAtmOamVclSegLoopIn = _OacAtmOamVclSegLoopIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 5),
    _OacAtmOamVclSegLoopIn_Type()
)
oacAtmOamVclSegLoopIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegLoopIn.setStatus("current")
_OacAtmOamVclAisIn_Type = Counter32
_OacAtmOamVclAisIn_Object = MibTableColumn
oacAtmOamVclAisIn = _OacAtmOamVclAisIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 6),
    _OacAtmOamVclAisIn_Type()
)
oacAtmOamVclAisIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAisIn.setStatus("current")
_OacAtmOamVclRdiIn_Type = Counter32
_OacAtmOamVclRdiIn_Object = MibTableColumn
oacAtmOamVclRdiIn = _OacAtmOamVclRdiIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 7),
    _OacAtmOamVclRdiIn_Type()
)
oacAtmOamVclRdiIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclRdiIn.setStatus("current")
_OacAtmOamVclSegCCIn_Type = Counter32
_OacAtmOamVclSegCCIn_Object = MibTableColumn
oacAtmOamVclSegCCIn = _OacAtmOamVclSegCCIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 8),
    _OacAtmOamVclSegCCIn_Type()
)
oacAtmOamVclSegCCIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegCCIn.setStatus("current")
_OacAtmOamVclEndCCIn_Type = Counter32
_OacAtmOamVclEndCCIn_Object = MibTableColumn
oacAtmOamVclEndCCIn = _OacAtmOamVclEndCCIn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 9),
    _OacAtmOamVclEndCCIn_Type()
)
oacAtmOamVclEndCCIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndCCIn.setStatus("current")
_OacAtmOamVclOamCellsSent_Type = Counter32
_OacAtmOamVclOamCellsSent_Object = MibTableColumn
oacAtmOamVclOamCellsSent = _OacAtmOamVclOamCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 10),
    _OacAtmOamVclOamCellsSent_Type()
)
oacAtmOamVclOamCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclOamCellsSent.setStatus("current")
_OacAtmOamVclEndLoopbackOut_Type = Counter32
_OacAtmOamVclEndLoopbackOut_Object = MibTableColumn
oacAtmOamVclEndLoopbackOut = _OacAtmOamVclEndLoopbackOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 11),
    _OacAtmOamVclEndLoopbackOut_Type()
)
oacAtmOamVclEndLoopbackOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndLoopbackOut.setStatus("current")
_OacAtmOamVclSegLoopbackOut_Type = Counter32
_OacAtmOamVclSegLoopbackOut_Object = MibTableColumn
oacAtmOamVclSegLoopbackOut = _OacAtmOamVclSegLoopbackOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 12),
    _OacAtmOamVclSegLoopbackOut_Type()
)
oacAtmOamVclSegLoopbackOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegLoopbackOut.setStatus("current")
_OacAtmOamVclEndLoopOut_Type = Counter32
_OacAtmOamVclEndLoopOut_Object = MibTableColumn
oacAtmOamVclEndLoopOut = _OacAtmOamVclEndLoopOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 13),
    _OacAtmOamVclEndLoopOut_Type()
)
oacAtmOamVclEndLoopOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndLoopOut.setStatus("current")
_OacAtmOamVclSegLoopOut_Type = Counter32
_OacAtmOamVclSegLoopOut_Object = MibTableColumn
oacAtmOamVclSegLoopOut = _OacAtmOamVclSegLoopOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 14),
    _OacAtmOamVclSegLoopOut_Type()
)
oacAtmOamVclSegLoopOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegLoopOut.setStatus("current")
_OacAtmOamVclAisOut_Type = Counter32
_OacAtmOamVclAisOut_Object = MibTableColumn
oacAtmOamVclAisOut = _OacAtmOamVclAisOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 15),
    _OacAtmOamVclAisOut_Type()
)
oacAtmOamVclAisOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclAisOut.setStatus("current")
_OacAtmOamVclRdiOut_Type = Counter32
_OacAtmOamVclRdiOut_Object = MibTableColumn
oacAtmOamVclRdiOut = _OacAtmOamVclRdiOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 16),
    _OacAtmOamVclRdiOut_Type()
)
oacAtmOamVclRdiOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclRdiOut.setStatus("current")
_OacAtmOamVclSegCCOut_Type = Counter32
_OacAtmOamVclSegCCOut_Object = MibTableColumn
oacAtmOamVclSegCCOut = _OacAtmOamVclSegCCOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 17),
    _OacAtmOamVclSegCCOut_Type()
)
oacAtmOamVclSegCCOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclSegCCOut.setStatus("current")
_OacAtmOamVclEndCCOut_Type = Counter32
_OacAtmOamVclEndCCOut_Object = MibTableColumn
oacAtmOamVclEndCCOut = _OacAtmOamVclEndCCOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 18),
    _OacAtmOamVclEndCCOut_Type()
)
oacAtmOamVclEndCCOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclEndCCOut.setStatus("current")
_OacAtmOamVclOamCellsDropped_Type = Counter32
_OacAtmOamVclOamCellsDropped_Object = MibTableColumn
oacAtmOamVclOamCellsDropped = _OacAtmOamVclOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 1, 3, 1, 19),
    _OacAtmOamVclOamCellsDropped_Type()
)
oacAtmOamVclOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmOamVclOamCellsDropped.setStatus("current")
_OacAtmOamStatNotifications_ObjectIdentity = ObjectIdentity
oacAtmOamStatNotifications = _OacAtmOamStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 2)
)
_OacAtmOamStatConformance_ObjectIdentity = ObjectIdentity
oacAtmOamStatConformance = _OacAtmOamStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3)
)
_OacAtmOamStatGroups_ObjectIdentity = ObjectIdentity
oacAtmOamStatGroups = _OacAtmOamStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 1)
)
_OacAtmOamStatCompliances_ObjectIdentity = ObjectIdentity
oacAtmOamStatCompliances = _OacAtmOamStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 2)
)
atmVclEntry.registerAugmentions(
    ("ONEACCESS-OAM-MIB",
     "oacAtmOamVclEntry")
)
oacAtmOamVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ONEACCESS-OAM-MIB",
     "oacAtmOamVclCountersEntry")
)
oacAtmOamVclCountersEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Managed Objects groups

oacAtmOamStatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 1, 1)
)
oacAtmOamStatGeneralGroup.setObjects(
      *(("ONEACCESS-OAM-MIB", "oacAtmOamSwitchMaxConnections"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchSegLoopback"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchEndLoopback"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchAisRdiEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchSegmentContinuityCheckEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchEndContinuityCheckEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchOamCellsReceived"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchOamCellsTransmitted"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamSwitchCurrentConnections"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclPvcManage"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegmentLoopback"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopback"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegmentContinuityCheckEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndContinuityCheckEnable"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxInterval"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryFrequency"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryUpCount"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclLoopbackTxRetryDownCount"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAlarmState"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAlarmStateLastChange"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiRetryDownCount"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisRdiRetryUpTimer"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclPvcIntrusive"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsReceived"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopbackIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopbackIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclRdiIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegCCIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndCCIn"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsSent"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopbackOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopbackOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndLoopOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegLoopOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclAisOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclRdiOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclSegCCOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclEndCCOut"),
        ("ONEACCESS-OAM-MIB", "oacAtmOamVclOamCellsDropped"))
)
if mibBuilder.loadTexts:
    oacAtmOamStatGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacAtmOamStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oacAtmOamStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-OAM-MIB",
    **{"oacOamMIBModule": oacOamMIBModule,
       "oacAtmOamStatObjects": oacAtmOamStatObjects,
       "oacAtmOamStatSwitch": oacAtmOamStatSwitch,
       "oacAtmOamSwitchMaxConnections": oacAtmOamSwitchMaxConnections,
       "oacAtmOamSwitchSegLoopback": oacAtmOamSwitchSegLoopback,
       "oacAtmOamSwitchEndLoopback": oacAtmOamSwitchEndLoopback,
       "oacAtmOamSwitchAisRdiEnable": oacAtmOamSwitchAisRdiEnable,
       "oacAtmOamSwitchSegmentContinuityCheckEnable": oacAtmOamSwitchSegmentContinuityCheckEnable,
       "oacAtmOamSwitchEndContinuityCheckEnable": oacAtmOamSwitchEndContinuityCheckEnable,
       "oacAtmOamSwitchOamCellsReceived": oacAtmOamSwitchOamCellsReceived,
       "oacAtmOamSwitchOamCellsTransmitted": oacAtmOamSwitchOamCellsTransmitted,
       "oacAtmOamSwitchCurrentConnections": oacAtmOamSwitchCurrentConnections,
       "oacAtmOamVclTable": oacAtmOamVclTable,
       "oacAtmOamVclEntry": oacAtmOamVclEntry,
       "oacAtmOamVclPvcManage": oacAtmOamVclPvcManage,
       "oacAtmOamVclSegmentLoopback": oacAtmOamVclSegmentLoopback,
       "oacAtmOamVclEndLoopback": oacAtmOamVclEndLoopback,
       "oacAtmOamVclAisRdiEnable": oacAtmOamVclAisRdiEnable,
       "oacAtmOamVclSegmentContinuityCheckEnable": oacAtmOamVclSegmentContinuityCheckEnable,
       "oacAtmOamVclEndContinuityCheckEnable": oacAtmOamVclEndContinuityCheckEnable,
       "oacAtmOamVclLoopbackTxInterval": oacAtmOamVclLoopbackTxInterval,
       "oacAtmOamVclLoopbackTxRetryFrequency": oacAtmOamVclLoopbackTxRetryFrequency,
       "oacAtmOamVclLoopbackTxRetryUpCount": oacAtmOamVclLoopbackTxRetryUpCount,
       "oacAtmOamVclLoopbackTxRetryDownCount": oacAtmOamVclLoopbackTxRetryDownCount,
       "oacAtmOamVclAlarmState": oacAtmOamVclAlarmState,
       "oacAtmOamVclAlarmStateLastChange": oacAtmOamVclAlarmStateLastChange,
       "oacAtmOamVclAisRdiRetryDownCount": oacAtmOamVclAisRdiRetryDownCount,
       "oacAtmOamVclAisRdiRetryUpTimer": oacAtmOamVclAisRdiRetryUpTimer,
       "oacAtmOamVclPvcIntrusive": oacAtmOamVclPvcIntrusive,
       "oacAtmOamVclCountersTable": oacAtmOamVclCountersTable,
       "oacAtmOamVclCountersEntry": oacAtmOamVclCountersEntry,
       "oacAtmOamVclOamCellsReceived": oacAtmOamVclOamCellsReceived,
       "oacAtmOamVclEndLoopbackIn": oacAtmOamVclEndLoopbackIn,
       "oacAtmOamVclSegLoopbackIn": oacAtmOamVclSegLoopbackIn,
       "oacAtmOamVclEndLoopIn": oacAtmOamVclEndLoopIn,
       "oacAtmOamVclSegLoopIn": oacAtmOamVclSegLoopIn,
       "oacAtmOamVclAisIn": oacAtmOamVclAisIn,
       "oacAtmOamVclRdiIn": oacAtmOamVclRdiIn,
       "oacAtmOamVclSegCCIn": oacAtmOamVclSegCCIn,
       "oacAtmOamVclEndCCIn": oacAtmOamVclEndCCIn,
       "oacAtmOamVclOamCellsSent": oacAtmOamVclOamCellsSent,
       "oacAtmOamVclEndLoopbackOut": oacAtmOamVclEndLoopbackOut,
       "oacAtmOamVclSegLoopbackOut": oacAtmOamVclSegLoopbackOut,
       "oacAtmOamVclEndLoopOut": oacAtmOamVclEndLoopOut,
       "oacAtmOamVclSegLoopOut": oacAtmOamVclSegLoopOut,
       "oacAtmOamVclAisOut": oacAtmOamVclAisOut,
       "oacAtmOamVclRdiOut": oacAtmOamVclRdiOut,
       "oacAtmOamVclSegCCOut": oacAtmOamVclSegCCOut,
       "oacAtmOamVclEndCCOut": oacAtmOamVclEndCCOut,
       "oacAtmOamVclOamCellsDropped": oacAtmOamVclOamCellsDropped,
       "oacAtmOamStatNotifications": oacAtmOamStatNotifications,
       "oacAtmOamStatConformance": oacAtmOamStatConformance,
       "oacAtmOamStatGroups": oacAtmOamStatGroups,
       "oacAtmOamStatGeneralGroup": oacAtmOamStatGeneralGroup,
       "oacAtmOamStatCompliances": oacAtmOamStatCompliances,
       "oacAtmOamStatCompliance": oacAtmOamStatCompliance}
)
