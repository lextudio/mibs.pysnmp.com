# SNMP MIB module (APPIAN-LPORT-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-LPORT-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:33 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 acLport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "acLport")

(PerfIntervalCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfIntervalCount")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

acLogicalDs3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcLogicalDs3Traps_ObjectIdentity = ObjectIdentity
acLogicalDs3Traps = _AcLogicalDs3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0)
)
_AcLogicalDs3ConfigTable_Object = MibTable
acLogicalDs3ConfigTable = _AcLogicalDs3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTable.setStatus("current")
_AcLogicalDs3ConfigEntry_Object = MibTableRow
acLogicalDs3ConfigEntry = _AcLogicalDs3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1)
)
acLogicalDs3ConfigEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"),
)
if mibBuilder.loadTexts:
    acLogicalDs3ConfigEntry.setStatus("current")
_AcLogicalDs3ConfigNodeId_Type = AcNodeId
_AcLogicalDs3ConfigNodeId_Object = MibTableColumn
acLogicalDs3ConfigNodeId = _AcLogicalDs3ConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 1),
    _AcLogicalDs3ConfigNodeId_Type()
)
acLogicalDs3ConfigNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigNodeId.setStatus("current")
_AcLogicalDs3ConfigIndex_Type = Integer32
_AcLogicalDs3ConfigIndex_Object = MibTableColumn
acLogicalDs3ConfigIndex = _AcLogicalDs3ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 2),
    _AcLogicalDs3ConfigIndex_Type()
)
acLogicalDs3ConfigIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigIndex.setStatus("current")


class _AcLogicalDs3ConfigAdminStatus_Type(AcAdminStatus):
    """Custom type acLogicalDs3ConfigAdminStatus based on AcAdminStatus"""


_AcLogicalDs3ConfigAdminStatus_Object = MibTableColumn
acLogicalDs3ConfigAdminStatus = _AcLogicalDs3ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 3),
    _AcLogicalDs3ConfigAdminStatus_Type()
)
acLogicalDs3ConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigAdminStatus.setStatus("current")


class _AcLogicalDs3ConfigTimeElapsedInterval_Type(Integer32):
    """Custom type acLogicalDs3ConfigTimeElapsedInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcLogicalDs3ConfigTimeElapsedInterval_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigTimeElapsedInterval_Object = MibTableColumn
acLogicalDs3ConfigTimeElapsedInterval = _AcLogicalDs3ConfigTimeElapsedInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 4),
    _AcLogicalDs3ConfigTimeElapsedInterval_Type()
)
acLogicalDs3ConfigTimeElapsedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTimeElapsedInterval.setStatus("current")


class _AcLogicalDs3ConfigValidIntervals_Type(Integer32):
    """Custom type acLogicalDs3ConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs3ConfigValidIntervals_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigValidIntervals_Object = MibTableColumn
acLogicalDs3ConfigValidIntervals = _AcLogicalDs3ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 5),
    _AcLogicalDs3ConfigValidIntervals_Type()
)
acLogicalDs3ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigValidIntervals.setStatus("current")


class _AcLogicalDs3ConfigTimeElapsedDay_Type(Integer32):
    """Custom type acLogicalDs3ConfigTimeElapsedDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcLogicalDs3ConfigTimeElapsedDay_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigTimeElapsedDay_Object = MibTableColumn
acLogicalDs3ConfigTimeElapsedDay = _AcLogicalDs3ConfigTimeElapsedDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 6),
    _AcLogicalDs3ConfigTimeElapsedDay_Type()
)
acLogicalDs3ConfigTimeElapsedDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTimeElapsedDay.setStatus("current")


class _AcLogicalDs3ConfigValidDays_Type(Integer32):
    """Custom type acLogicalDs3ConfigValidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs3ConfigValidDays_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigValidDays_Object = MibTableColumn
acLogicalDs3ConfigValidDays = _AcLogicalDs3ConfigValidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 7),
    _AcLogicalDs3ConfigValidDays_Type()
)
acLogicalDs3ConfigValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigValidDays.setStatus("current")


class _AcLogicalDs3ConfigTimeElapsedFarEndInterval_Type(Integer32):
    """Custom type acLogicalDs3ConfigTimeElapsedFarEndInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcLogicalDs3ConfigTimeElapsedFarEndInterval_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigTimeElapsedFarEndInterval_Object = MibTableColumn
acLogicalDs3ConfigTimeElapsedFarEndInterval = _AcLogicalDs3ConfigTimeElapsedFarEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 8),
    _AcLogicalDs3ConfigTimeElapsedFarEndInterval_Type()
)
acLogicalDs3ConfigTimeElapsedFarEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTimeElapsedFarEndInterval.setStatus("current")


class _AcLogicalDs3ConfigValidFarEndIntervals_Type(Integer32):
    """Custom type acLogicalDs3ConfigValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs3ConfigValidFarEndIntervals_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigValidFarEndIntervals_Object = MibTableColumn
acLogicalDs3ConfigValidFarEndIntervals = _AcLogicalDs3ConfigValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 9),
    _AcLogicalDs3ConfigValidFarEndIntervals_Type()
)
acLogicalDs3ConfigValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigValidFarEndIntervals.setStatus("current")


class _AcLogicalDs3ConfigTimeElapsedFarEndDay_Type(Integer32):
    """Custom type acLogicalDs3ConfigTimeElapsedFarEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcLogicalDs3ConfigTimeElapsedFarEndDay_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigTimeElapsedFarEndDay_Object = MibTableColumn
acLogicalDs3ConfigTimeElapsedFarEndDay = _AcLogicalDs3ConfigTimeElapsedFarEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 10),
    _AcLogicalDs3ConfigTimeElapsedFarEndDay_Type()
)
acLogicalDs3ConfigTimeElapsedFarEndDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTimeElapsedFarEndDay.setStatus("current")


class _AcLogicalDs3ConfigValidFarEndDays_Type(Integer32):
    """Custom type acLogicalDs3ConfigValidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs3ConfigValidFarEndDays_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigValidFarEndDays_Object = MibTableColumn
acLogicalDs3ConfigValidFarEndDays = _AcLogicalDs3ConfigValidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 11),
    _AcLogicalDs3ConfigValidFarEndDays_Type()
)
acLogicalDs3ConfigValidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigValidFarEndDays.setStatus("current")


class _AcLogicalDs3ConfigSendCode_Type(Integer32):
    """Custom type acLogicalDs3ConfigSendCode based on Integer32"""
    defaultValue = 1

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
        *(("ds3SendLineCode", 2),
          ("ds3SendNoCode", 1),
          ("ds3SendPayloadCode", 3),
          ("ds3SendResetCode", 4),
          ("ds3SendTestPattern", 5))
    )


_AcLogicalDs3ConfigSendCode_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigSendCode_Object = MibTableColumn
acLogicalDs3ConfigSendCode = _AcLogicalDs3ConfigSendCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 12),
    _AcLogicalDs3ConfigSendCode_Type()
)
acLogicalDs3ConfigSendCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigSendCode.setStatus("current")


class _AcLogicalDs3ConfigCircuitIdentifier_Type(DisplayString):
    """Custom type acLogicalDs3ConfigCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcLogicalDs3ConfigCircuitIdentifier_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigCircuitIdentifier_Object = MibTableColumn
acLogicalDs3ConfigCircuitIdentifier = _AcLogicalDs3ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 13),
    _AcLogicalDs3ConfigCircuitIdentifier_Type()
)
acLogicalDs3ConfigCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigCircuitIdentifier.setStatus("current")


class _AcLogicalDs3ConfigLoopbackConfig_Type(Integer32):
    """Custom type acLogicalDs3ConfigLoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("ds3InwardLoop", 5),
          ("ds3LineLoop", 3),
          ("ds3NoLoop", 1),
          ("ds3OtherLoop", 4),
          ("ds3PayloadLoop", 2))
    )


_AcLogicalDs3ConfigLoopbackConfig_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigLoopbackConfig_Object = MibTableColumn
acLogicalDs3ConfigLoopbackConfig = _AcLogicalDs3ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 14),
    _AcLogicalDs3ConfigLoopbackConfig_Type()
)
acLogicalDs3ConfigLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigLoopbackConfig.setStatus("current")


class _AcLogicalDs3ConfigLineStatus_Type(Integer32):
    """Custom type acLogicalDs3ConfigLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AcLogicalDs3ConfigLineStatus_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigLineStatus_Object = MibTableColumn
acLogicalDs3ConfigLineStatus = _AcLogicalDs3ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 15),
    _AcLogicalDs3ConfigLineStatus_Type()
)
acLogicalDs3ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigLineStatus.setStatus("current")


class _AcLogicalDs3ConfigTransmitClockSource_Type(Integer32):
    """Custom type acLogicalDs3ConfigTransmitClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_AcLogicalDs3ConfigTransmitClockSource_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigTransmitClockSource_Object = MibTableColumn
acLogicalDs3ConfigTransmitClockSource = _AcLogicalDs3ConfigTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 16),
    _AcLogicalDs3ConfigTransmitClockSource_Type()
)
acLogicalDs3ConfigTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigTransmitClockSource.setStatus("current")


class _AcLogicalDs3ConfigInvalidIntervals_Type(Integer32):
    """Custom type acLogicalDs3ConfigInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs3ConfigInvalidIntervals_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigInvalidIntervals_Object = MibTableColumn
acLogicalDs3ConfigInvalidIntervals = _AcLogicalDs3ConfigInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 17),
    _AcLogicalDs3ConfigInvalidIntervals_Type()
)
acLogicalDs3ConfigInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigInvalidIntervals.setStatus("current")


class _AcLogicalDs3ConfigInvalidDays_Type(Integer32):
    """Custom type acLogicalDs3ConfigInvalidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs3ConfigInvalidDays_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigInvalidDays_Object = MibTableColumn
acLogicalDs3ConfigInvalidDays = _AcLogicalDs3ConfigInvalidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 18),
    _AcLogicalDs3ConfigInvalidDays_Type()
)
acLogicalDs3ConfigInvalidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigInvalidDays.setStatus("current")


class _AcLogicalDs3ConfigInvalidFarEndIntervals_Type(Integer32):
    """Custom type acLogicalDs3ConfigInvalidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs3ConfigInvalidFarEndIntervals_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigInvalidFarEndIntervals_Object = MibTableColumn
acLogicalDs3ConfigInvalidFarEndIntervals = _AcLogicalDs3ConfigInvalidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 19),
    _AcLogicalDs3ConfigInvalidFarEndIntervals_Type()
)
acLogicalDs3ConfigInvalidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigInvalidFarEndIntervals.setStatus("current")


class _AcLogicalDs3ConfigInvalidFarEndDays_Type(Integer32):
    """Custom type acLogicalDs3ConfigInvalidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs3ConfigInvalidFarEndDays_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigInvalidFarEndDays_Object = MibTableColumn
acLogicalDs3ConfigInvalidFarEndDays = _AcLogicalDs3ConfigInvalidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 20),
    _AcLogicalDs3ConfigInvalidFarEndDays_Type()
)
acLogicalDs3ConfigInvalidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigInvalidFarEndDays.setStatus("current")
_AcLogicalDs3ConfigLineStatusLastChange_Type = TimeStamp
_AcLogicalDs3ConfigLineStatusLastChange_Object = MibTableColumn
acLogicalDs3ConfigLineStatusLastChange = _AcLogicalDs3ConfigLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 21),
    _AcLogicalDs3ConfigLineStatusLastChange_Type()
)
acLogicalDs3ConfigLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigLineStatusLastChange.setStatus("current")


class _AcLogicalDs3ConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type acLogicalDs3ConfigLineStatusChangeTrapEnable based on Integer32"""
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


_AcLogicalDs3ConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigLineStatusChangeTrapEnable_Object = MibTableColumn
acLogicalDs3ConfigLineStatusChangeTrapEnable = _AcLogicalDs3ConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 22),
    _AcLogicalDs3ConfigLineStatusChangeTrapEnable_Type()
)
acLogicalDs3ConfigLineStatusChangeTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigLineStatusChangeTrapEnable.setStatus("current")


class _AcLogicalDs3ConfigLoopbackStatus_Type(Integer32):
    """Custom type acLogicalDs3ConfigLoopbackStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AcLogicalDs3ConfigLoopbackStatus_Type.__name__ = "Integer32"
_AcLogicalDs3ConfigLoopbackStatus_Object = MibTableColumn
acLogicalDs3ConfigLoopbackStatus = _AcLogicalDs3ConfigLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 23),
    _AcLogicalDs3ConfigLoopbackStatus_Type()
)
acLogicalDs3ConfigLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigLoopbackStatus.setStatus("current")


class _AcLogicalDs3ConfigFarEndEquipCode_Type(DisplayString):
    """Custom type acLogicalDs3ConfigFarEndEquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcLogicalDs3ConfigFarEndEquipCode_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigFarEndEquipCode_Object = MibTableColumn
acLogicalDs3ConfigFarEndEquipCode = _AcLogicalDs3ConfigFarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 24),
    _AcLogicalDs3ConfigFarEndEquipCode_Type()
)
acLogicalDs3ConfigFarEndEquipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigFarEndEquipCode.setStatus("current")


class _AcLogicalDs3ConfigFarEndLocationIDCode_Type(DisplayString):
    """Custom type acLogicalDs3ConfigFarEndLocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AcLogicalDs3ConfigFarEndLocationIDCode_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigFarEndLocationIDCode_Object = MibTableColumn
acLogicalDs3ConfigFarEndLocationIDCode = _AcLogicalDs3ConfigFarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 25),
    _AcLogicalDs3ConfigFarEndLocationIDCode_Type()
)
acLogicalDs3ConfigFarEndLocationIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigFarEndLocationIDCode.setStatus("current")


class _AcLogicalDs3ConfigFarEndFrameIDCode_Type(DisplayString):
    """Custom type acLogicalDs3ConfigFarEndFrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcLogicalDs3ConfigFarEndFrameIDCode_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigFarEndFrameIDCode_Object = MibTableColumn
acLogicalDs3ConfigFarEndFrameIDCode = _AcLogicalDs3ConfigFarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 26),
    _AcLogicalDs3ConfigFarEndFrameIDCode_Type()
)
acLogicalDs3ConfigFarEndFrameIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigFarEndFrameIDCode.setStatus("current")


class _AcLogicalDs3ConfigFarEndUnitCode_Type(DisplayString):
    """Custom type acLogicalDs3ConfigFarEndUnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AcLogicalDs3ConfigFarEndUnitCode_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigFarEndUnitCode_Object = MibTableColumn
acLogicalDs3ConfigFarEndUnitCode = _AcLogicalDs3ConfigFarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 27),
    _AcLogicalDs3ConfigFarEndUnitCode_Type()
)
acLogicalDs3ConfigFarEndUnitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigFarEndUnitCode.setStatus("current")


class _AcLogicalDs3ConfigFarEndFacilityIDCode_Type(DisplayString):
    """Custom type acLogicalDs3ConfigFarEndFacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_AcLogicalDs3ConfigFarEndFacilityIDCode_Type.__name__ = "DisplayString"
_AcLogicalDs3ConfigFarEndFacilityIDCode_Object = MibTableColumn
acLogicalDs3ConfigFarEndFacilityIDCode = _AcLogicalDs3ConfigFarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 1, 1, 28),
    _AcLogicalDs3ConfigFarEndFacilityIDCode_Type()
)
acLogicalDs3ConfigFarEndFacilityIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3ConfigFarEndFacilityIDCode.setStatus("current")
_AcLogicalDs3IntervalTable_Object = MibTable
acLogicalDs3IntervalTable = _AcLogicalDs3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    acLogicalDs3IntervalTable.setStatus("current")
_AcLogicalDs3IntervalEntry_Object = MibTableRow
acLogicalDs3IntervalEntry = _AcLogicalDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1)
)
acLogicalDs3IntervalEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3IntervalNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3IntervalIndex"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs3IntervalEntry.setStatus("current")
_AcLogicalDs3IntervalNodeId_Type = AcNodeId
_AcLogicalDs3IntervalNodeId_Object = MibTableColumn
acLogicalDs3IntervalNodeId = _AcLogicalDs3IntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 1),
    _AcLogicalDs3IntervalNodeId_Type()
)
acLogicalDs3IntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalNodeId.setStatus("current")
_AcLogicalDs3IntervalIndex_Type = Integer32
_AcLogicalDs3IntervalIndex_Object = MibTableColumn
acLogicalDs3IntervalIndex = _AcLogicalDs3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 2),
    _AcLogicalDs3IntervalIndex_Type()
)
acLogicalDs3IntervalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalIndex.setStatus("current")


class _AcLogicalDs3IntervalNumber_Type(Integer32):
    """Custom type acLogicalDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcLogicalDs3IntervalNumber_Type.__name__ = "Integer32"
_AcLogicalDs3IntervalNumber_Object = MibTableColumn
acLogicalDs3IntervalNumber = _AcLogicalDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 3),
    _AcLogicalDs3IntervalNumber_Type()
)
acLogicalDs3IntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalNumber.setStatus("current")
_AcLogicalDs3IntervalValidStats_Type = TruthValue
_AcLogicalDs3IntervalValidStats_Object = MibTableColumn
acLogicalDs3IntervalValidStats = _AcLogicalDs3IntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 4),
    _AcLogicalDs3IntervalValidStats_Type()
)
acLogicalDs3IntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalValidStats.setStatus("current")
_AcLogicalDs3IntervalResetStats_Type = TruthValue
_AcLogicalDs3IntervalResetStats_Object = MibTableColumn
acLogicalDs3IntervalResetStats = _AcLogicalDs3IntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 5),
    _AcLogicalDs3IntervalResetStats_Type()
)
acLogicalDs3IntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalResetStats.setStatus("current")
_AcLogicalDs3IntervalPESs_Type = PerfIntervalCount
_AcLogicalDs3IntervalPESs_Object = MibTableColumn
acLogicalDs3IntervalPESs = _AcLogicalDs3IntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 6),
    _AcLogicalDs3IntervalPESs_Type()
)
acLogicalDs3IntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalPESs.setStatus("current")
_AcLogicalDs3IntervalPSESs_Type = PerfIntervalCount
_AcLogicalDs3IntervalPSESs_Object = MibTableColumn
acLogicalDs3IntervalPSESs = _AcLogicalDs3IntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 7),
    _AcLogicalDs3IntervalPSESs_Type()
)
acLogicalDs3IntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalPSESs.setStatus("current")
_AcLogicalDs3IntervalSEFSs_Type = PerfIntervalCount
_AcLogicalDs3IntervalSEFSs_Object = MibTableColumn
acLogicalDs3IntervalSEFSs = _AcLogicalDs3IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 8),
    _AcLogicalDs3IntervalSEFSs_Type()
)
acLogicalDs3IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalSEFSs.setStatus("current")
_AcLogicalDs3IntervalUASs_Type = PerfIntervalCount
_AcLogicalDs3IntervalUASs_Object = MibTableColumn
acLogicalDs3IntervalUASs = _AcLogicalDs3IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 9),
    _AcLogicalDs3IntervalUASs_Type()
)
acLogicalDs3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalUASs.setStatus("current")
_AcLogicalDs3IntervalLCVs_Type = PerfIntervalCount
_AcLogicalDs3IntervalLCVs_Object = MibTableColumn
acLogicalDs3IntervalLCVs = _AcLogicalDs3IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 10),
    _AcLogicalDs3IntervalLCVs_Type()
)
acLogicalDs3IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalLCVs.setStatus("current")
_AcLogicalDs3IntervalPCVs_Type = PerfIntervalCount
_AcLogicalDs3IntervalPCVs_Object = MibTableColumn
acLogicalDs3IntervalPCVs = _AcLogicalDs3IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 11),
    _AcLogicalDs3IntervalPCVs_Type()
)
acLogicalDs3IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalPCVs.setStatus("current")
_AcLogicalDs3IntervalLESs_Type = PerfIntervalCount
_AcLogicalDs3IntervalLESs_Object = MibTableColumn
acLogicalDs3IntervalLESs = _AcLogicalDs3IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 12),
    _AcLogicalDs3IntervalLESs_Type()
)
acLogicalDs3IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalLESs.setStatus("current")
_AcLogicalDs3IntervalCCVs_Type = PerfIntervalCount
_AcLogicalDs3IntervalCCVs_Object = MibTableColumn
acLogicalDs3IntervalCCVs = _AcLogicalDs3IntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 13),
    _AcLogicalDs3IntervalCCVs_Type()
)
acLogicalDs3IntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalCCVs.setStatus("current")
_AcLogicalDs3IntervalCESs_Type = PerfIntervalCount
_AcLogicalDs3IntervalCESs_Object = MibTableColumn
acLogicalDs3IntervalCESs = _AcLogicalDs3IntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 14),
    _AcLogicalDs3IntervalCESs_Type()
)
acLogicalDs3IntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalCESs.setStatus("current")
_AcLogicalDs3IntervalCSESs_Type = PerfIntervalCount
_AcLogicalDs3IntervalCSESs_Object = MibTableColumn
acLogicalDs3IntervalCSESs = _AcLogicalDs3IntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 2, 1, 15),
    _AcLogicalDs3IntervalCSESs_Type()
)
acLogicalDs3IntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3IntervalCSESs.setStatus("current")
_AcLogicalDs3DayTable_Object = MibTable
acLogicalDs3DayTable = _AcLogicalDs3DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3)
)
if mibBuilder.loadTexts:
    acLogicalDs3DayTable.setStatus("current")
_AcLogicalDs3DayEntry_Object = MibTableRow
acLogicalDs3DayEntry = _AcLogicalDs3DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1)
)
acLogicalDs3DayEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3DayNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3DayIndex"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3DayNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs3DayEntry.setStatus("current")
_AcLogicalDs3DayNodeId_Type = AcNodeId
_AcLogicalDs3DayNodeId_Object = MibTableColumn
acLogicalDs3DayNodeId = _AcLogicalDs3DayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 1),
    _AcLogicalDs3DayNodeId_Type()
)
acLogicalDs3DayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3DayNodeId.setStatus("current")
_AcLogicalDs3DayIndex_Type = Integer32
_AcLogicalDs3DayIndex_Object = MibTableColumn
acLogicalDs3DayIndex = _AcLogicalDs3DayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 2),
    _AcLogicalDs3DayIndex_Type()
)
acLogicalDs3DayIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3DayIndex.setStatus("current")


class _AcLogicalDs3DayNumber_Type(Integer32):
    """Custom type acLogicalDs3DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcLogicalDs3DayNumber_Type.__name__ = "Integer32"
_AcLogicalDs3DayNumber_Object = MibTableColumn
acLogicalDs3DayNumber = _AcLogicalDs3DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 3),
    _AcLogicalDs3DayNumber_Type()
)
acLogicalDs3DayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3DayNumber.setStatus("current")
_AcLogicalDs3DayValidStats_Type = TruthValue
_AcLogicalDs3DayValidStats_Object = MibTableColumn
acLogicalDs3DayValidStats = _AcLogicalDs3DayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 4),
    _AcLogicalDs3DayValidStats_Type()
)
acLogicalDs3DayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayValidStats.setStatus("current")
_AcLogicalDs3DayResetStats_Type = TruthValue
_AcLogicalDs3DayResetStats_Object = MibTableColumn
acLogicalDs3DayResetStats = _AcLogicalDs3DayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 5),
    _AcLogicalDs3DayResetStats_Type()
)
acLogicalDs3DayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3DayResetStats.setStatus("current")
_AcLogicalDs3DayPESs_Type = PerfIntervalCount
_AcLogicalDs3DayPESs_Object = MibTableColumn
acLogicalDs3DayPESs = _AcLogicalDs3DayPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 6),
    _AcLogicalDs3DayPESs_Type()
)
acLogicalDs3DayPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayPESs.setStatus("current")
_AcLogicalDs3DayPSESs_Type = PerfIntervalCount
_AcLogicalDs3DayPSESs_Object = MibTableColumn
acLogicalDs3DayPSESs = _AcLogicalDs3DayPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 7),
    _AcLogicalDs3DayPSESs_Type()
)
acLogicalDs3DayPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayPSESs.setStatus("current")
_AcLogicalDs3DaySEFSs_Type = PerfIntervalCount
_AcLogicalDs3DaySEFSs_Object = MibTableColumn
acLogicalDs3DaySEFSs = _AcLogicalDs3DaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 8),
    _AcLogicalDs3DaySEFSs_Type()
)
acLogicalDs3DaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DaySEFSs.setStatus("current")
_AcLogicalDs3DayUASs_Type = PerfIntervalCount
_AcLogicalDs3DayUASs_Object = MibTableColumn
acLogicalDs3DayUASs = _AcLogicalDs3DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 9),
    _AcLogicalDs3DayUASs_Type()
)
acLogicalDs3DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayUASs.setStatus("current")
_AcLogicalDs3DayLCVs_Type = PerfIntervalCount
_AcLogicalDs3DayLCVs_Object = MibTableColumn
acLogicalDs3DayLCVs = _AcLogicalDs3DayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 10),
    _AcLogicalDs3DayLCVs_Type()
)
acLogicalDs3DayLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayLCVs.setStatus("current")
_AcLogicalDs3DayPCVs_Type = PerfIntervalCount
_AcLogicalDs3DayPCVs_Object = MibTableColumn
acLogicalDs3DayPCVs = _AcLogicalDs3DayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 11),
    _AcLogicalDs3DayPCVs_Type()
)
acLogicalDs3DayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayPCVs.setStatus("current")
_AcLogicalDs3DayLESs_Type = PerfIntervalCount
_AcLogicalDs3DayLESs_Object = MibTableColumn
acLogicalDs3DayLESs = _AcLogicalDs3DayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 12),
    _AcLogicalDs3DayLESs_Type()
)
acLogicalDs3DayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayLESs.setStatus("current")
_AcLogicalDs3DayCCVs_Type = PerfIntervalCount
_AcLogicalDs3DayCCVs_Object = MibTableColumn
acLogicalDs3DayCCVs = _AcLogicalDs3DayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 13),
    _AcLogicalDs3DayCCVs_Type()
)
acLogicalDs3DayCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayCCVs.setStatus("current")
_AcLogicalDs3DayCESs_Type = PerfIntervalCount
_AcLogicalDs3DayCESs_Object = MibTableColumn
acLogicalDs3DayCESs = _AcLogicalDs3DayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 14),
    _AcLogicalDs3DayCESs_Type()
)
acLogicalDs3DayCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayCESs.setStatus("current")
_AcLogicalDs3DayCSESs_Type = PerfIntervalCount
_AcLogicalDs3DayCSESs_Object = MibTableColumn
acLogicalDs3DayCSESs = _AcLogicalDs3DayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 3, 1, 15),
    _AcLogicalDs3DayCSESs_Type()
)
acLogicalDs3DayCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3DayCSESs.setStatus("current")
_AcLogicalDs3FarEndIntervalTable_Object = MibTable
acLogicalDs3FarEndIntervalTable = _AcLogicalDs3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5)
)
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalTable.setStatus("current")
_AcLogicalDs3FarEndIntervalEntry_Object = MibTableRow
acLogicalDs3FarEndIntervalEntry = _AcLogicalDs3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1)
)
acLogicalDs3FarEndIntervalEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndIntervalNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndIntervalIndex"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalEntry.setStatus("current")
_AcLogicalDs3FarEndIntervalNodeId_Type = AcNodeId
_AcLogicalDs3FarEndIntervalNodeId_Object = MibTableColumn
acLogicalDs3FarEndIntervalNodeId = _AcLogicalDs3FarEndIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 1),
    _AcLogicalDs3FarEndIntervalNodeId_Type()
)
acLogicalDs3FarEndIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalNodeId.setStatus("current")
_AcLogicalDs3FarEndIntervalIndex_Type = Integer32
_AcLogicalDs3FarEndIntervalIndex_Object = MibTableColumn
acLogicalDs3FarEndIntervalIndex = _AcLogicalDs3FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 2),
    _AcLogicalDs3FarEndIntervalIndex_Type()
)
acLogicalDs3FarEndIntervalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalIndex.setStatus("current")


class _AcLogicalDs3FarEndIntervalNumber_Type(Integer32):
    """Custom type acLogicalDs3FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcLogicalDs3FarEndIntervalNumber_Type.__name__ = "Integer32"
_AcLogicalDs3FarEndIntervalNumber_Object = MibTableColumn
acLogicalDs3FarEndIntervalNumber = _AcLogicalDs3FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 3),
    _AcLogicalDs3FarEndIntervalNumber_Type()
)
acLogicalDs3FarEndIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalNumber.setStatus("current")
_AcLogicalDs3FarEndIntervalValidStats_Type = TruthValue
_AcLogicalDs3FarEndIntervalValidStats_Object = MibTableColumn
acLogicalDs3FarEndIntervalValidStats = _AcLogicalDs3FarEndIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 4),
    _AcLogicalDs3FarEndIntervalValidStats_Type()
)
acLogicalDs3FarEndIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalValidStats.setStatus("current")
_AcLogicalDs3FarEndIntervalResetStats_Type = TruthValue
_AcLogicalDs3FarEndIntervalResetStats_Object = MibTableColumn
acLogicalDs3FarEndIntervalResetStats = _AcLogicalDs3FarEndIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 5),
    _AcLogicalDs3FarEndIntervalResetStats_Type()
)
acLogicalDs3FarEndIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalResetStats.setStatus("current")
_AcLogicalDs3FarEndIntervalCESs_Type = PerfIntervalCount
_AcLogicalDs3FarEndIntervalCESs_Object = MibTableColumn
acLogicalDs3FarEndIntervalCESs = _AcLogicalDs3FarEndIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 6),
    _AcLogicalDs3FarEndIntervalCESs_Type()
)
acLogicalDs3FarEndIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalCESs.setStatus("current")
_AcLogicalDs3FarEndIntervalCSESs_Type = PerfIntervalCount
_AcLogicalDs3FarEndIntervalCSESs_Object = MibTableColumn
acLogicalDs3FarEndIntervalCSESs = _AcLogicalDs3FarEndIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 7),
    _AcLogicalDs3FarEndIntervalCSESs_Type()
)
acLogicalDs3FarEndIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalCSESs.setStatus("current")
_AcLogicalDs3FarEndIntervalCCVs_Type = PerfIntervalCount
_AcLogicalDs3FarEndIntervalCCVs_Object = MibTableColumn
acLogicalDs3FarEndIntervalCCVs = _AcLogicalDs3FarEndIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 8),
    _AcLogicalDs3FarEndIntervalCCVs_Type()
)
acLogicalDs3FarEndIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalCCVs.setStatus("current")
_AcLogicalDs3FarEndIntervalUASs_Type = PerfIntervalCount
_AcLogicalDs3FarEndIntervalUASs_Object = MibTableColumn
acLogicalDs3FarEndIntervalUASs = _AcLogicalDs3FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 5, 1, 9),
    _AcLogicalDs3FarEndIntervalUASs_Type()
)
acLogicalDs3FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndIntervalUASs.setStatus("current")
_AcLogicalDs3FarEndDayTable_Object = MibTable
acLogicalDs3FarEndDayTable = _AcLogicalDs3FarEndDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6)
)
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayTable.setStatus("current")
_AcLogicalDs3FarEndDayEntry_Object = MibTableRow
acLogicalDs3FarEndDayEntry = _AcLogicalDs3FarEndDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1)
)
acLogicalDs3FarEndDayEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndDayNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndDayIndex"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3FarEndDayNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayEntry.setStatus("current")
_AcLogicalDs3FarEndDayNodeId_Type = AcNodeId
_AcLogicalDs3FarEndDayNodeId_Object = MibTableColumn
acLogicalDs3FarEndDayNodeId = _AcLogicalDs3FarEndDayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 1),
    _AcLogicalDs3FarEndDayNodeId_Type()
)
acLogicalDs3FarEndDayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayNodeId.setStatus("current")
_AcLogicalDs3FarEndDayIndex_Type = Integer32
_AcLogicalDs3FarEndDayIndex_Object = MibTableColumn
acLogicalDs3FarEndDayIndex = _AcLogicalDs3FarEndDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 2),
    _AcLogicalDs3FarEndDayIndex_Type()
)
acLogicalDs3FarEndDayIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayIndex.setStatus("current")


class _AcLogicalDs3FarEndDayNumber_Type(Integer32):
    """Custom type acLogicalDs3FarEndDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcLogicalDs3FarEndDayNumber_Type.__name__ = "Integer32"
_AcLogicalDs3FarEndDayNumber_Object = MibTableColumn
acLogicalDs3FarEndDayNumber = _AcLogicalDs3FarEndDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 3),
    _AcLogicalDs3FarEndDayNumber_Type()
)
acLogicalDs3FarEndDayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayNumber.setStatus("current")
_AcLogicalDs3FarEndDayValidStats_Type = TruthValue
_AcLogicalDs3FarEndDayValidStats_Object = MibTableColumn
acLogicalDs3FarEndDayValidStats = _AcLogicalDs3FarEndDayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 4),
    _AcLogicalDs3FarEndDayValidStats_Type()
)
acLogicalDs3FarEndDayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayValidStats.setStatus("current")
_AcLogicalDs3FarEndDayResetStats_Type = TruthValue
_AcLogicalDs3FarEndDayResetStats_Object = MibTableColumn
acLogicalDs3FarEndDayResetStats = _AcLogicalDs3FarEndDayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 5),
    _AcLogicalDs3FarEndDayResetStats_Type()
)
acLogicalDs3FarEndDayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayResetStats.setStatus("current")
_AcLogicalDs3FarEndDayCESs_Type = PerfIntervalCount
_AcLogicalDs3FarEndDayCESs_Object = MibTableColumn
acLogicalDs3FarEndDayCESs = _AcLogicalDs3FarEndDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 6),
    _AcLogicalDs3FarEndDayCESs_Type()
)
acLogicalDs3FarEndDayCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayCESs.setStatus("current")
_AcLogicalDs3FarEndDayCSESs_Type = PerfIntervalCount
_AcLogicalDs3FarEndDayCSESs_Object = MibTableColumn
acLogicalDs3FarEndDayCSESs = _AcLogicalDs3FarEndDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 7),
    _AcLogicalDs3FarEndDayCSESs_Type()
)
acLogicalDs3FarEndDayCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayCSESs.setStatus("current")
_AcLogicalDs3FarEndDayCCVs_Type = PerfIntervalCount
_AcLogicalDs3FarEndDayCCVs_Object = MibTableColumn
acLogicalDs3FarEndDayCCVs = _AcLogicalDs3FarEndDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 8),
    _AcLogicalDs3FarEndDayCCVs_Type()
)
acLogicalDs3FarEndDayCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayCCVs.setStatus("current")
_AcLogicalDs3FarEndDayUASs_Type = PerfIntervalCount
_AcLogicalDs3FarEndDayUASs_Object = MibTableColumn
acLogicalDs3FarEndDayUASs = _AcLogicalDs3FarEndDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 6, 1, 9),
    _AcLogicalDs3FarEndDayUASs_Type()
)
acLogicalDs3FarEndDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs3FarEndDayUASs.setStatus("current")
_AcLogicalDs3ThresholdTable_Object = MibTable
acLogicalDs3ThresholdTable = _AcLogicalDs3ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7)
)
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdTable.setStatus("current")
_AcLogicalDs3ThresholdEntry_Object = MibTableRow
acLogicalDs3ThresholdEntry = _AcLogicalDs3ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1)
)
acLogicalDs3ThresholdEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
    (0, "APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"),
)
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdEntry.setStatus("current")
_AcLogicalDs3ThresholdNodeId_Type = AcNodeId
_AcLogicalDs3ThresholdNodeId_Object = MibTableColumn
acLogicalDs3ThresholdNodeId = _AcLogicalDs3ThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 1),
    _AcLogicalDs3ThresholdNodeId_Type()
)
acLogicalDs3ThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNodeId.setStatus("current")
_AcLogicalDs3ThresholdIndex_Type = Integer32
_AcLogicalDs3ThresholdIndex_Object = MibTableColumn
acLogicalDs3ThresholdIndex = _AcLogicalDs3ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 2),
    _AcLogicalDs3ThresholdIndex_Type()
)
acLogicalDs3ThresholdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdIndex.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalPESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalPESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalPESs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalPESs = _AcLogicalDs3ThresholdNEIntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 3),
    _AcLogicalDs3ThresholdNEIntervalPESs_Type()
)
acLogicalDs3ThresholdNEIntervalPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalPESs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalPSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalPSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalPSESs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalPSESs = _AcLogicalDs3ThresholdNEIntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 4),
    _AcLogicalDs3ThresholdNEIntervalPSESs_Type()
)
acLogicalDs3ThresholdNEIntervalPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalPSESs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalSEFSs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalSEFSs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalSEFSs = _AcLogicalDs3ThresholdNEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 5),
    _AcLogicalDs3ThresholdNEIntervalSEFSs_Type()
)
acLogicalDs3ThresholdNEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalSEFSs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalUASs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalUASs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalUASs = _AcLogicalDs3ThresholdNEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 6),
    _AcLogicalDs3ThresholdNEIntervalUASs_Type()
)
acLogicalDs3ThresholdNEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalUASs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalLCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalLCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalLCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalLCVs = _AcLogicalDs3ThresholdNEIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 7),
    _AcLogicalDs3ThresholdNEIntervalLCVs_Type()
)
acLogicalDs3ThresholdNEIntervalLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalLCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalPCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalPCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalPCVs = _AcLogicalDs3ThresholdNEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 8),
    _AcLogicalDs3ThresholdNEIntervalPCVs_Type()
)
acLogicalDs3ThresholdNEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalPCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalLESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalLESs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalLESs = _AcLogicalDs3ThresholdNEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 9),
    _AcLogicalDs3ThresholdNEIntervalLESs_Type()
)
acLogicalDs3ThresholdNEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalLESs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalCCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalCCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalCCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalCCVs = _AcLogicalDs3ThresholdNEIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 10),
    _AcLogicalDs3ThresholdNEIntervalCCVs_Type()
)
acLogicalDs3ThresholdNEIntervalCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalCCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalCESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalCESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalCESs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalCESs = _AcLogicalDs3ThresholdNEIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 11),
    _AcLogicalDs3ThresholdNEIntervalCESs_Type()
)
acLogicalDs3ThresholdNEIntervalCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalCESs.setStatus("current")


class _AcLogicalDs3ThresholdNEIntervalCSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEIntervalCSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEIntervalCSESs_Object = MibTableColumn
acLogicalDs3ThresholdNEIntervalCSESs = _AcLogicalDs3ThresholdNEIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 12),
    _AcLogicalDs3ThresholdNEIntervalCSESs_Type()
)
acLogicalDs3ThresholdNEIntervalCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEIntervalCSESs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayPESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayPESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayPESs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayPESs = _AcLogicalDs3ThresholdNEDayPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 13),
    _AcLogicalDs3ThresholdNEDayPESs_Type()
)
acLogicalDs3ThresholdNEDayPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayPESs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayPSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayPSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayPSESs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayPSESs = _AcLogicalDs3ThresholdNEDayPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 14),
    _AcLogicalDs3ThresholdNEDayPSESs_Type()
)
acLogicalDs3ThresholdNEDayPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayPSESs.setStatus("current")


class _AcLogicalDs3ThresholdNEDaySEFSs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDaySEFSs_Object = MibTableColumn
acLogicalDs3ThresholdNEDaySEFSs = _AcLogicalDs3ThresholdNEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 15),
    _AcLogicalDs3ThresholdNEDaySEFSs_Type()
)
acLogicalDs3ThresholdNEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDaySEFSs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayUASs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayUASs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayUASs = _AcLogicalDs3ThresholdNEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 16),
    _AcLogicalDs3ThresholdNEDayUASs_Type()
)
acLogicalDs3ThresholdNEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayUASs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayLCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayLCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayLCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayLCVs = _AcLogicalDs3ThresholdNEDayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 17),
    _AcLogicalDs3ThresholdNEDayLCVs_Type()
)
acLogicalDs3ThresholdNEDayLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayLCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayPCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayPCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayPCVs = _AcLogicalDs3ThresholdNEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 18),
    _AcLogicalDs3ThresholdNEDayPCVs_Type()
)
acLogicalDs3ThresholdNEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayPCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayLESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayLESs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayLESs = _AcLogicalDs3ThresholdNEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 19),
    _AcLogicalDs3ThresholdNEDayLESs_Type()
)
acLogicalDs3ThresholdNEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayLESs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayCCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayCCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayCCVs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayCCVs = _AcLogicalDs3ThresholdNEDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 20),
    _AcLogicalDs3ThresholdNEDayCCVs_Type()
)
acLogicalDs3ThresholdNEDayCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayCCVs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayCESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayCESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayCESs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayCESs = _AcLogicalDs3ThresholdNEDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 21),
    _AcLogicalDs3ThresholdNEDayCESs_Type()
)
acLogicalDs3ThresholdNEDayCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayCESs.setStatus("current")


class _AcLogicalDs3ThresholdNEDayCSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdNEDayCSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdNEDayCSESs_Object = MibTableColumn
acLogicalDs3ThresholdNEDayCSESs = _AcLogicalDs3ThresholdNEDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 22),
    _AcLogicalDs3ThresholdNEDayCSESs_Type()
)
acLogicalDs3ThresholdNEDayCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdNEDayCSESs.setStatus("current")


class _AcLogicalDs3ThresholdFEIntervalCESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEIntervalCESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEIntervalCESs_Object = MibTableColumn
acLogicalDs3ThresholdFEIntervalCESs = _AcLogicalDs3ThresholdFEIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 23),
    _AcLogicalDs3ThresholdFEIntervalCESs_Type()
)
acLogicalDs3ThresholdFEIntervalCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEIntervalCESs.setStatus("current")


class _AcLogicalDs3ThresholdFEIntervalCSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEIntervalCSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEIntervalCSESs_Object = MibTableColumn
acLogicalDs3ThresholdFEIntervalCSESs = _AcLogicalDs3ThresholdFEIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 24),
    _AcLogicalDs3ThresholdFEIntervalCSESs_Type()
)
acLogicalDs3ThresholdFEIntervalCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEIntervalCSESs.setStatus("current")


class _AcLogicalDs3ThresholdFEIntervalCCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEIntervalCCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEIntervalCCVs_Object = MibTableColumn
acLogicalDs3ThresholdFEIntervalCCVs = _AcLogicalDs3ThresholdFEIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 25),
    _AcLogicalDs3ThresholdFEIntervalCCVs_Type()
)
acLogicalDs3ThresholdFEIntervalCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEIntervalCCVs.setStatus("current")


class _AcLogicalDs3ThresholdFEIntervalUASs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEIntervalUASs_Object = MibTableColumn
acLogicalDs3ThresholdFEIntervalUASs = _AcLogicalDs3ThresholdFEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 26),
    _AcLogicalDs3ThresholdFEIntervalUASs_Type()
)
acLogicalDs3ThresholdFEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEIntervalUASs.setStatus("current")


class _AcLogicalDs3ThresholdFEDayCESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEDayCESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEDayCESs_Object = MibTableColumn
acLogicalDs3ThresholdFEDayCESs = _AcLogicalDs3ThresholdFEDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 27),
    _AcLogicalDs3ThresholdFEDayCESs_Type()
)
acLogicalDs3ThresholdFEDayCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEDayCESs.setStatus("current")


class _AcLogicalDs3ThresholdFEDayCSESs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEDayCSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEDayCSESs_Object = MibTableColumn
acLogicalDs3ThresholdFEDayCSESs = _AcLogicalDs3ThresholdFEDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 28),
    _AcLogicalDs3ThresholdFEDayCSESs_Type()
)
acLogicalDs3ThresholdFEDayCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEDayCSESs.setStatus("current")


class _AcLogicalDs3ThresholdFEDayCCVs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEDayCCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEDayCCVs_Object = MibTableColumn
acLogicalDs3ThresholdFEDayCCVs = _AcLogicalDs3ThresholdFEDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 29),
    _AcLogicalDs3ThresholdFEDayCCVs_Type()
)
acLogicalDs3ThresholdFEDayCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEDayCCVs.setStatus("current")


class _AcLogicalDs3ThresholdFEDayUASs_Type(Integer32):
    """Custom type acLogicalDs3ThresholdFEDayUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs3ThresholdFEDayUASs_Object = MibTableColumn
acLogicalDs3ThresholdFEDayUASs = _AcLogicalDs3ThresholdFEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 7, 1, 30),
    _AcLogicalDs3ThresholdFEDayUASs_Type()
)
acLogicalDs3ThresholdFEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs3ThresholdFEDayUASs.setStatus("current")

# Managed Objects groups


# Notification objects

acLogicalDs3LineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 1)
)
acLogicalDs3LineStatusChangeTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigLineStatus"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigLineStatusLastChange"))
)
if mibBuilder.loadTexts:
    acLogicalDs3LineStatusChangeTrap.setStatus(
        "current"
    )

acLogicalDs3StatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 2)
)
acLogicalDs3StatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3StatsResetTrap.setStatus(
        "current"
    )

acLogicalDs3CfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 3)
)
acLogicalDs3CfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3CfgErrorTrap.setStatus(
        "current"
    )

acLogicalDs3LinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 4)
)
acLogicalDs3LinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3LinkDownTrap.setStatus(
        "current"
    )

acLogicalDs3LinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 5)
)
acLogicalDs3LinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3LinkUpTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalPESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 6)
)
acLogicalDs3ExceededThresholdNEIntervalPESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalPESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalPSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 7)
)
acLogicalDs3ExceededThresholdNEIntervalPSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalPSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 8)
)
acLogicalDs3ExceededThresholdNEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalSEFSsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 9)
)
acLogicalDs3ExceededThresholdNEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalUASsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 10)
)
acLogicalDs3ExceededThresholdNEIntervalLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalLCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 11)
)
acLogicalDs3ExceededThresholdNEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalPCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 12)
)
acLogicalDs3ExceededThresholdNEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalLESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 13)
)
acLogicalDs3ExceededThresholdNEIntervalCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalCCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 14)
)
acLogicalDs3ExceededThresholdNEIntervalCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalCESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEIntervalCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 15)
)
acLogicalDs3ExceededThresholdNEIntervalCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEIntervalCSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayPESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 16)
)
acLogicalDs3ExceededThresholdNEDayPESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayPESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayPSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 17)
)
acLogicalDs3ExceededThresholdNEDayPSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayPSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDaySEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 18)
)
acLogicalDs3ExceededThresholdNEDaySEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDaySEFSsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 19)
)
acLogicalDs3ExceededThresholdNEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayUASsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 20)
)
acLogicalDs3ExceededThresholdNEDayLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayLCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 21)
)
acLogicalDs3ExceededThresholdNEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayPCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 22)
)
acLogicalDs3ExceededThresholdNEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayLESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 23)
)
acLogicalDs3ExceededThresholdNEDayCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayCCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 24)
)
acLogicalDs3ExceededThresholdNEDayCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayCESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdNEDayCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 25)
)
acLogicalDs3ExceededThresholdNEDayCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdNEDayCSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEIntervalCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 26)
)
acLogicalDs3ExceededThresholdFEIntervalCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEIntervalCESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEIntervalCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 27)
)
acLogicalDs3ExceededThresholdFEIntervalCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEIntervalCSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEIntervalCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 28)
)
acLogicalDs3ExceededThresholdFEIntervalCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEIntervalCCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 29)
)
acLogicalDs3ExceededThresholdFEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEIntervalUASsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEDayCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 30)
)
acLogicalDs3ExceededThresholdFEDayCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEDayCESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEDayCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 31)
)
acLogicalDs3ExceededThresholdFEDayCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEDayCSESsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEDayCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 32)
)
acLogicalDs3ExceededThresholdFEDayCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEDayCCVsTrap.setStatus(
        "current"
    )

acLogicalDs3ExceededThresholdFEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 3, 0, 33)
)
acLogicalDs3ExceededThresholdFEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdNodeId"),
        ("APPIAN-LPORT-DS3-MIB", "acLogicalDs3ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs3ExceededThresholdFEDayUASsTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-LPORT-DS3-MIB",
    **{"acLogicalDs3": acLogicalDs3,
       "acLogicalDs3Traps": acLogicalDs3Traps,
       "acLogicalDs3LineStatusChangeTrap": acLogicalDs3LineStatusChangeTrap,
       "acLogicalDs3StatsResetTrap": acLogicalDs3StatsResetTrap,
       "acLogicalDs3CfgErrorTrap": acLogicalDs3CfgErrorTrap,
       "acLogicalDs3LinkDownTrap": acLogicalDs3LinkDownTrap,
       "acLogicalDs3LinkUpTrap": acLogicalDs3LinkUpTrap,
       "acLogicalDs3ExceededThresholdNEIntervalPESsTrap": acLogicalDs3ExceededThresholdNEIntervalPESsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalPSESsTrap": acLogicalDs3ExceededThresholdNEIntervalPSESsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalSEFSsTrap": acLogicalDs3ExceededThresholdNEIntervalSEFSsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalUASsTrap": acLogicalDs3ExceededThresholdNEIntervalUASsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalLCVsTrap": acLogicalDs3ExceededThresholdNEIntervalLCVsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalPCVsTrap": acLogicalDs3ExceededThresholdNEIntervalPCVsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalLESsTrap": acLogicalDs3ExceededThresholdNEIntervalLESsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalCCVsTrap": acLogicalDs3ExceededThresholdNEIntervalCCVsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalCESsTrap": acLogicalDs3ExceededThresholdNEIntervalCESsTrap,
       "acLogicalDs3ExceededThresholdNEIntervalCSESsTrap": acLogicalDs3ExceededThresholdNEIntervalCSESsTrap,
       "acLogicalDs3ExceededThresholdNEDayPESsTrap": acLogicalDs3ExceededThresholdNEDayPESsTrap,
       "acLogicalDs3ExceededThresholdNEDayPSESsTrap": acLogicalDs3ExceededThresholdNEDayPSESsTrap,
       "acLogicalDs3ExceededThresholdNEDaySEFSsTrap": acLogicalDs3ExceededThresholdNEDaySEFSsTrap,
       "acLogicalDs3ExceededThresholdNEDayUASsTrap": acLogicalDs3ExceededThresholdNEDayUASsTrap,
       "acLogicalDs3ExceededThresholdNEDayLCVsTrap": acLogicalDs3ExceededThresholdNEDayLCVsTrap,
       "acLogicalDs3ExceededThresholdNEDayPCVsTrap": acLogicalDs3ExceededThresholdNEDayPCVsTrap,
       "acLogicalDs3ExceededThresholdNEDayLESsTrap": acLogicalDs3ExceededThresholdNEDayLESsTrap,
       "acLogicalDs3ExceededThresholdNEDayCCVsTrap": acLogicalDs3ExceededThresholdNEDayCCVsTrap,
       "acLogicalDs3ExceededThresholdNEDayCESsTrap": acLogicalDs3ExceededThresholdNEDayCESsTrap,
       "acLogicalDs3ExceededThresholdNEDayCSESsTrap": acLogicalDs3ExceededThresholdNEDayCSESsTrap,
       "acLogicalDs3ExceededThresholdFEIntervalCESsTrap": acLogicalDs3ExceededThresholdFEIntervalCESsTrap,
       "acLogicalDs3ExceededThresholdFEIntervalCSESsTrap": acLogicalDs3ExceededThresholdFEIntervalCSESsTrap,
       "acLogicalDs3ExceededThresholdFEIntervalCCVsTrap": acLogicalDs3ExceededThresholdFEIntervalCCVsTrap,
       "acLogicalDs3ExceededThresholdFEIntervalUASsTrap": acLogicalDs3ExceededThresholdFEIntervalUASsTrap,
       "acLogicalDs3ExceededThresholdFEDayCESsTrap": acLogicalDs3ExceededThresholdFEDayCESsTrap,
       "acLogicalDs3ExceededThresholdFEDayCSESsTrap": acLogicalDs3ExceededThresholdFEDayCSESsTrap,
       "acLogicalDs3ExceededThresholdFEDayCCVsTrap": acLogicalDs3ExceededThresholdFEDayCCVsTrap,
       "acLogicalDs3ExceededThresholdFEDayUASsTrap": acLogicalDs3ExceededThresholdFEDayUASsTrap,
       "acLogicalDs3ConfigTable": acLogicalDs3ConfigTable,
       "acLogicalDs3ConfigEntry": acLogicalDs3ConfigEntry,
       "acLogicalDs3ConfigNodeId": acLogicalDs3ConfigNodeId,
       "acLogicalDs3ConfigIndex": acLogicalDs3ConfigIndex,
       "acLogicalDs3ConfigAdminStatus": acLogicalDs3ConfigAdminStatus,
       "acLogicalDs3ConfigTimeElapsedInterval": acLogicalDs3ConfigTimeElapsedInterval,
       "acLogicalDs3ConfigValidIntervals": acLogicalDs3ConfigValidIntervals,
       "acLogicalDs3ConfigTimeElapsedDay": acLogicalDs3ConfigTimeElapsedDay,
       "acLogicalDs3ConfigValidDays": acLogicalDs3ConfigValidDays,
       "acLogicalDs3ConfigTimeElapsedFarEndInterval": acLogicalDs3ConfigTimeElapsedFarEndInterval,
       "acLogicalDs3ConfigValidFarEndIntervals": acLogicalDs3ConfigValidFarEndIntervals,
       "acLogicalDs3ConfigTimeElapsedFarEndDay": acLogicalDs3ConfigTimeElapsedFarEndDay,
       "acLogicalDs3ConfigValidFarEndDays": acLogicalDs3ConfigValidFarEndDays,
       "acLogicalDs3ConfigSendCode": acLogicalDs3ConfigSendCode,
       "acLogicalDs3ConfigCircuitIdentifier": acLogicalDs3ConfigCircuitIdentifier,
       "acLogicalDs3ConfigLoopbackConfig": acLogicalDs3ConfigLoopbackConfig,
       "acLogicalDs3ConfigLineStatus": acLogicalDs3ConfigLineStatus,
       "acLogicalDs3ConfigTransmitClockSource": acLogicalDs3ConfigTransmitClockSource,
       "acLogicalDs3ConfigInvalidIntervals": acLogicalDs3ConfigInvalidIntervals,
       "acLogicalDs3ConfigInvalidDays": acLogicalDs3ConfigInvalidDays,
       "acLogicalDs3ConfigInvalidFarEndIntervals": acLogicalDs3ConfigInvalidFarEndIntervals,
       "acLogicalDs3ConfigInvalidFarEndDays": acLogicalDs3ConfigInvalidFarEndDays,
       "acLogicalDs3ConfigLineStatusLastChange": acLogicalDs3ConfigLineStatusLastChange,
       "acLogicalDs3ConfigLineStatusChangeTrapEnable": acLogicalDs3ConfigLineStatusChangeTrapEnable,
       "acLogicalDs3ConfigLoopbackStatus": acLogicalDs3ConfigLoopbackStatus,
       "acLogicalDs3ConfigFarEndEquipCode": acLogicalDs3ConfigFarEndEquipCode,
       "acLogicalDs3ConfigFarEndLocationIDCode": acLogicalDs3ConfigFarEndLocationIDCode,
       "acLogicalDs3ConfigFarEndFrameIDCode": acLogicalDs3ConfigFarEndFrameIDCode,
       "acLogicalDs3ConfigFarEndUnitCode": acLogicalDs3ConfigFarEndUnitCode,
       "acLogicalDs3ConfigFarEndFacilityIDCode": acLogicalDs3ConfigFarEndFacilityIDCode,
       "acLogicalDs3IntervalTable": acLogicalDs3IntervalTable,
       "acLogicalDs3IntervalEntry": acLogicalDs3IntervalEntry,
       "acLogicalDs3IntervalNodeId": acLogicalDs3IntervalNodeId,
       "acLogicalDs3IntervalIndex": acLogicalDs3IntervalIndex,
       "acLogicalDs3IntervalNumber": acLogicalDs3IntervalNumber,
       "acLogicalDs3IntervalValidStats": acLogicalDs3IntervalValidStats,
       "acLogicalDs3IntervalResetStats": acLogicalDs3IntervalResetStats,
       "acLogicalDs3IntervalPESs": acLogicalDs3IntervalPESs,
       "acLogicalDs3IntervalPSESs": acLogicalDs3IntervalPSESs,
       "acLogicalDs3IntervalSEFSs": acLogicalDs3IntervalSEFSs,
       "acLogicalDs3IntervalUASs": acLogicalDs3IntervalUASs,
       "acLogicalDs3IntervalLCVs": acLogicalDs3IntervalLCVs,
       "acLogicalDs3IntervalPCVs": acLogicalDs3IntervalPCVs,
       "acLogicalDs3IntervalLESs": acLogicalDs3IntervalLESs,
       "acLogicalDs3IntervalCCVs": acLogicalDs3IntervalCCVs,
       "acLogicalDs3IntervalCESs": acLogicalDs3IntervalCESs,
       "acLogicalDs3IntervalCSESs": acLogicalDs3IntervalCSESs,
       "acLogicalDs3DayTable": acLogicalDs3DayTable,
       "acLogicalDs3DayEntry": acLogicalDs3DayEntry,
       "acLogicalDs3DayNodeId": acLogicalDs3DayNodeId,
       "acLogicalDs3DayIndex": acLogicalDs3DayIndex,
       "acLogicalDs3DayNumber": acLogicalDs3DayNumber,
       "acLogicalDs3DayValidStats": acLogicalDs3DayValidStats,
       "acLogicalDs3DayResetStats": acLogicalDs3DayResetStats,
       "acLogicalDs3DayPESs": acLogicalDs3DayPESs,
       "acLogicalDs3DayPSESs": acLogicalDs3DayPSESs,
       "acLogicalDs3DaySEFSs": acLogicalDs3DaySEFSs,
       "acLogicalDs3DayUASs": acLogicalDs3DayUASs,
       "acLogicalDs3DayLCVs": acLogicalDs3DayLCVs,
       "acLogicalDs3DayPCVs": acLogicalDs3DayPCVs,
       "acLogicalDs3DayLESs": acLogicalDs3DayLESs,
       "acLogicalDs3DayCCVs": acLogicalDs3DayCCVs,
       "acLogicalDs3DayCESs": acLogicalDs3DayCESs,
       "acLogicalDs3DayCSESs": acLogicalDs3DayCSESs,
       "acLogicalDs3FarEndIntervalTable": acLogicalDs3FarEndIntervalTable,
       "acLogicalDs3FarEndIntervalEntry": acLogicalDs3FarEndIntervalEntry,
       "acLogicalDs3FarEndIntervalNodeId": acLogicalDs3FarEndIntervalNodeId,
       "acLogicalDs3FarEndIntervalIndex": acLogicalDs3FarEndIntervalIndex,
       "acLogicalDs3FarEndIntervalNumber": acLogicalDs3FarEndIntervalNumber,
       "acLogicalDs3FarEndIntervalValidStats": acLogicalDs3FarEndIntervalValidStats,
       "acLogicalDs3FarEndIntervalResetStats": acLogicalDs3FarEndIntervalResetStats,
       "acLogicalDs3FarEndIntervalCESs": acLogicalDs3FarEndIntervalCESs,
       "acLogicalDs3FarEndIntervalCSESs": acLogicalDs3FarEndIntervalCSESs,
       "acLogicalDs3FarEndIntervalCCVs": acLogicalDs3FarEndIntervalCCVs,
       "acLogicalDs3FarEndIntervalUASs": acLogicalDs3FarEndIntervalUASs,
       "acLogicalDs3FarEndDayTable": acLogicalDs3FarEndDayTable,
       "acLogicalDs3FarEndDayEntry": acLogicalDs3FarEndDayEntry,
       "acLogicalDs3FarEndDayNodeId": acLogicalDs3FarEndDayNodeId,
       "acLogicalDs3FarEndDayIndex": acLogicalDs3FarEndDayIndex,
       "acLogicalDs3FarEndDayNumber": acLogicalDs3FarEndDayNumber,
       "acLogicalDs3FarEndDayValidStats": acLogicalDs3FarEndDayValidStats,
       "acLogicalDs3FarEndDayResetStats": acLogicalDs3FarEndDayResetStats,
       "acLogicalDs3FarEndDayCESs": acLogicalDs3FarEndDayCESs,
       "acLogicalDs3FarEndDayCSESs": acLogicalDs3FarEndDayCSESs,
       "acLogicalDs3FarEndDayCCVs": acLogicalDs3FarEndDayCCVs,
       "acLogicalDs3FarEndDayUASs": acLogicalDs3FarEndDayUASs,
       "acLogicalDs3ThresholdTable": acLogicalDs3ThresholdTable,
       "acLogicalDs3ThresholdEntry": acLogicalDs3ThresholdEntry,
       "acLogicalDs3ThresholdNodeId": acLogicalDs3ThresholdNodeId,
       "acLogicalDs3ThresholdIndex": acLogicalDs3ThresholdIndex,
       "acLogicalDs3ThresholdNEIntervalPESs": acLogicalDs3ThresholdNEIntervalPESs,
       "acLogicalDs3ThresholdNEIntervalPSESs": acLogicalDs3ThresholdNEIntervalPSESs,
       "acLogicalDs3ThresholdNEIntervalSEFSs": acLogicalDs3ThresholdNEIntervalSEFSs,
       "acLogicalDs3ThresholdNEIntervalUASs": acLogicalDs3ThresholdNEIntervalUASs,
       "acLogicalDs3ThresholdNEIntervalLCVs": acLogicalDs3ThresholdNEIntervalLCVs,
       "acLogicalDs3ThresholdNEIntervalPCVs": acLogicalDs3ThresholdNEIntervalPCVs,
       "acLogicalDs3ThresholdNEIntervalLESs": acLogicalDs3ThresholdNEIntervalLESs,
       "acLogicalDs3ThresholdNEIntervalCCVs": acLogicalDs3ThresholdNEIntervalCCVs,
       "acLogicalDs3ThresholdNEIntervalCESs": acLogicalDs3ThresholdNEIntervalCESs,
       "acLogicalDs3ThresholdNEIntervalCSESs": acLogicalDs3ThresholdNEIntervalCSESs,
       "acLogicalDs3ThresholdNEDayPESs": acLogicalDs3ThresholdNEDayPESs,
       "acLogicalDs3ThresholdNEDayPSESs": acLogicalDs3ThresholdNEDayPSESs,
       "acLogicalDs3ThresholdNEDaySEFSs": acLogicalDs3ThresholdNEDaySEFSs,
       "acLogicalDs3ThresholdNEDayUASs": acLogicalDs3ThresholdNEDayUASs,
       "acLogicalDs3ThresholdNEDayLCVs": acLogicalDs3ThresholdNEDayLCVs,
       "acLogicalDs3ThresholdNEDayPCVs": acLogicalDs3ThresholdNEDayPCVs,
       "acLogicalDs3ThresholdNEDayLESs": acLogicalDs3ThresholdNEDayLESs,
       "acLogicalDs3ThresholdNEDayCCVs": acLogicalDs3ThresholdNEDayCCVs,
       "acLogicalDs3ThresholdNEDayCESs": acLogicalDs3ThresholdNEDayCESs,
       "acLogicalDs3ThresholdNEDayCSESs": acLogicalDs3ThresholdNEDayCSESs,
       "acLogicalDs3ThresholdFEIntervalCESs": acLogicalDs3ThresholdFEIntervalCESs,
       "acLogicalDs3ThresholdFEIntervalCSESs": acLogicalDs3ThresholdFEIntervalCSESs,
       "acLogicalDs3ThresholdFEIntervalCCVs": acLogicalDs3ThresholdFEIntervalCCVs,
       "acLogicalDs3ThresholdFEIntervalUASs": acLogicalDs3ThresholdFEIntervalUASs,
       "acLogicalDs3ThresholdFEDayCESs": acLogicalDs3ThresholdFEDayCESs,
       "acLogicalDs3ThresholdFEDayCSESs": acLogicalDs3ThresholdFEDayCSESs,
       "acLogicalDs3ThresholdFEDayCCVs": acLogicalDs3ThresholdFEDayCCVs,
       "acLogicalDs3ThresholdFEDayUASs": acLogicalDs3ThresholdFEDayUASs}
)
