# SNMP MIB module (APPIAN-PPORT-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:39 2024
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
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

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

acDs1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcDs1Traps_ObjectIdentity = ObjectIdentity
acDs1Traps = _AcDs1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0)
)
_AcDs1ConfigTable_Object = MibTable
acDs1ConfigTable = _AcDs1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    acDs1ConfigTable.setStatus("current")
_AcDs1ConfigEntry_Object = MibTableRow
acDs1ConfigEntry = _AcDs1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1)
)
acDs1ConfigEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"),
)
if mibBuilder.loadTexts:
    acDs1ConfigEntry.setStatus("current")
_AcDs1ConfigNodeId_Type = AcNodeId
_AcDs1ConfigNodeId_Object = MibTableColumn
acDs1ConfigNodeId = _AcDs1ConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 1),
    _AcDs1ConfigNodeId_Type()
)
acDs1ConfigNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ConfigNodeId.setStatus("current")
_AcDs1ConfigSlot_Type = AcSlotNumber
_AcDs1ConfigSlot_Object = MibTableColumn
acDs1ConfigSlot = _AcDs1ConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 2),
    _AcDs1ConfigSlot_Type()
)
acDs1ConfigSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ConfigSlot.setStatus("current")
_AcDs1ConfigPort_Type = AcPortNumber
_AcDs1ConfigPort_Object = MibTableColumn
acDs1ConfigPort = _AcDs1ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 3),
    _AcDs1ConfigPort_Type()
)
acDs1ConfigPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ConfigPort.setStatus("current")


class _AcDs1ConfigAdminStatus_Type(AcAdminStatus):
    """Custom type acDs1ConfigAdminStatus based on AcAdminStatus"""


_AcDs1ConfigAdminStatus_Object = MibTableColumn
acDs1ConfigAdminStatus = _AcDs1ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 4),
    _AcDs1ConfigAdminStatus_Type()
)
acDs1ConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigAdminStatus.setStatus("current")
_AcDs1ConfigOpStatus_Type = AcOpStatus
_AcDs1ConfigOpStatus_Object = MibTableColumn
acDs1ConfigOpStatus = _AcDs1ConfigOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 5),
    _AcDs1ConfigOpStatus_Type()
)
acDs1ConfigOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigOpStatus.setStatus("current")


class _AcDs1ConfigTimeElapsedInterval_Type(Integer32):
    """Custom type acDs1ConfigTimeElapsedInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcDs1ConfigTimeElapsedInterval_Type.__name__ = "Integer32"
_AcDs1ConfigTimeElapsedInterval_Object = MibTableColumn
acDs1ConfigTimeElapsedInterval = _AcDs1ConfigTimeElapsedInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 6),
    _AcDs1ConfigTimeElapsedInterval_Type()
)
acDs1ConfigTimeElapsedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigTimeElapsedInterval.setStatus("current")


class _AcDs1ConfigValidIntervals_Type(Integer32):
    """Custom type acDs1ConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs1ConfigValidIntervals_Type.__name__ = "Integer32"
_AcDs1ConfigValidIntervals_Object = MibTableColumn
acDs1ConfigValidIntervals = _AcDs1ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 7),
    _AcDs1ConfigValidIntervals_Type()
)
acDs1ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigValidIntervals.setStatus("current")


class _AcDs1ConfigTimeElapsedDay_Type(Integer32):
    """Custom type acDs1ConfigTimeElapsedDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcDs1ConfigTimeElapsedDay_Type.__name__ = "Integer32"
_AcDs1ConfigTimeElapsedDay_Object = MibTableColumn
acDs1ConfigTimeElapsedDay = _AcDs1ConfigTimeElapsedDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 8),
    _AcDs1ConfigTimeElapsedDay_Type()
)
acDs1ConfigTimeElapsedDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigTimeElapsedDay.setStatus("current")


class _AcDs1ConfigValidDays_Type(Integer32):
    """Custom type acDs1ConfigValidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs1ConfigValidDays_Type.__name__ = "Integer32"
_AcDs1ConfigValidDays_Object = MibTableColumn
acDs1ConfigValidDays = _AcDs1ConfigValidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 9),
    _AcDs1ConfigValidDays_Type()
)
acDs1ConfigValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigValidDays.setStatus("current")


class _AcDs1ConfigTimeElapsedFarEndInterval_Type(Integer32):
    """Custom type acDs1ConfigTimeElapsedFarEndInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcDs1ConfigTimeElapsedFarEndInterval_Type.__name__ = "Integer32"
_AcDs1ConfigTimeElapsedFarEndInterval_Object = MibTableColumn
acDs1ConfigTimeElapsedFarEndInterval = _AcDs1ConfigTimeElapsedFarEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 10),
    _AcDs1ConfigTimeElapsedFarEndInterval_Type()
)
acDs1ConfigTimeElapsedFarEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigTimeElapsedFarEndInterval.setStatus("current")


class _AcDs1ConfigValidFarEndIntervals_Type(Integer32):
    """Custom type acDs1ConfigValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs1ConfigValidFarEndIntervals_Type.__name__ = "Integer32"
_AcDs1ConfigValidFarEndIntervals_Object = MibTableColumn
acDs1ConfigValidFarEndIntervals = _AcDs1ConfigValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 11),
    _AcDs1ConfigValidFarEndIntervals_Type()
)
acDs1ConfigValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigValidFarEndIntervals.setStatus("current")


class _AcDs1ConfigTimeElapsedFarEndDay_Type(Integer32):
    """Custom type acDs1ConfigTimeElapsedFarEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcDs1ConfigTimeElapsedFarEndDay_Type.__name__ = "Integer32"
_AcDs1ConfigTimeElapsedFarEndDay_Object = MibTableColumn
acDs1ConfigTimeElapsedFarEndDay = _AcDs1ConfigTimeElapsedFarEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 12),
    _AcDs1ConfigTimeElapsedFarEndDay_Type()
)
acDs1ConfigTimeElapsedFarEndDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigTimeElapsedFarEndDay.setStatus("current")


class _AcDs1ConfigValidFarEndDays_Type(Integer32):
    """Custom type acDs1ConfigValidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs1ConfigValidFarEndDays_Type.__name__ = "Integer32"
_AcDs1ConfigValidFarEndDays_Object = MibTableColumn
acDs1ConfigValidFarEndDays = _AcDs1ConfigValidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 13),
    _AcDs1ConfigValidFarEndDays_Type()
)
acDs1ConfigValidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigValidFarEndDays.setStatus("current")


class _AcDs1ConfigLineType_Type(Integer32):
    """Custom type acDs1ConfigLineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esf", 1))
    )


_AcDs1ConfigLineType_Type.__name__ = "Integer32"
_AcDs1ConfigLineType_Object = MibTableColumn
acDs1ConfigLineType = _AcDs1ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 14),
    _AcDs1ConfigLineType_Type()
)
acDs1ConfigLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigLineType.setStatus("current")


class _AcDs1ConfigLineCoding_Type(Integer32):
    """Custom type acDs1ConfigLineCoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_AcDs1ConfigLineCoding_Type.__name__ = "Integer32"
_AcDs1ConfigLineCoding_Object = MibTableColumn
acDs1ConfigLineCoding = _AcDs1ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 15),
    _AcDs1ConfigLineCoding_Type()
)
acDs1ConfigLineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigLineCoding.setStatus("current")


class _AcDs1ConfigCircuitIdentifier_Type(DisplayString):
    """Custom type acDs1ConfigCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcDs1ConfigCircuitIdentifier_Type.__name__ = "DisplayString"
_AcDs1ConfigCircuitIdentifier_Object = MibTableColumn
acDs1ConfigCircuitIdentifier = _AcDs1ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 16),
    _AcDs1ConfigCircuitIdentifier_Type()
)
acDs1ConfigCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigCircuitIdentifier.setStatus("current")


class _AcDs1ConfigLoopbackConfig_Type(Integer32):
    """Custom type acDs1ConfigLoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("dual", 6),
          ("facility", 3),
          ("none", 1),
          ("other", 4),
          ("payload", 2),
          ("terminal", 5))
    )


_AcDs1ConfigLoopbackConfig_Type.__name__ = "Integer32"
_AcDs1ConfigLoopbackConfig_Object = MibTableColumn
acDs1ConfigLoopbackConfig = _AcDs1ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 17),
    _AcDs1ConfigLoopbackConfig_Type()
)
acDs1ConfigLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigLoopbackConfig.setStatus("current")


class _AcDs1ConfigLineStatus_Type(Integer32):
    """Custom type acDs1ConfigLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_AcDs1ConfigLineStatus_Type.__name__ = "Integer32"
_AcDs1ConfigLineStatus_Object = MibTableColumn
acDs1ConfigLineStatus = _AcDs1ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 18),
    _AcDs1ConfigLineStatus_Type()
)
acDs1ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigLineStatus.setStatus("current")


class _AcDs1ConfigSignalMode_Type(Integer32):
    """Custom type acDs1ConfigSignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("message", 2),
          ("none", 1),
          ("other", 3))
    )


_AcDs1ConfigSignalMode_Type.__name__ = "Integer32"
_AcDs1ConfigSignalMode_Object = MibTableColumn
acDs1ConfigSignalMode = _AcDs1ConfigSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 19),
    _AcDs1ConfigSignalMode_Type()
)
acDs1ConfigSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigSignalMode.setStatus("current")


class _AcDs1ConfigTransmitClockSource_Type(Integer32):
    """Custom type acDs1ConfigTransmitClockSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits", 1),
          ("local", 2),
          ("through", 3))
    )


_AcDs1ConfigTransmitClockSource_Type.__name__ = "Integer32"
_AcDs1ConfigTransmitClockSource_Object = MibTableColumn
acDs1ConfigTransmitClockSource = _AcDs1ConfigTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 20),
    _AcDs1ConfigTransmitClockSource_Type()
)
acDs1ConfigTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigTransmitClockSource.setStatus("current")


class _AcDs1ConfigFdl_Type(Integer32):
    """Custom type acDs1ConfigFdl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AcDs1ConfigFdl_Type.__name__ = "Integer32"
_AcDs1ConfigFdl_Object = MibTableColumn
acDs1ConfigFdl = _AcDs1ConfigFdl_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 21),
    _AcDs1ConfigFdl_Type()
)
acDs1ConfigFdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigFdl.setStatus("current")


class _AcDs1ConfigInvalidIntervals_Type(Integer32):
    """Custom type acDs1ConfigInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs1ConfigInvalidIntervals_Type.__name__ = "Integer32"
_AcDs1ConfigInvalidIntervals_Object = MibTableColumn
acDs1ConfigInvalidIntervals = _AcDs1ConfigInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 22),
    _AcDs1ConfigInvalidIntervals_Type()
)
acDs1ConfigInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigInvalidIntervals.setStatus("current")


class _AcDs1ConfigInvalidDays_Type(Integer32):
    """Custom type acDs1ConfigInvalidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs1ConfigInvalidDays_Type.__name__ = "Integer32"
_AcDs1ConfigInvalidDays_Object = MibTableColumn
acDs1ConfigInvalidDays = _AcDs1ConfigInvalidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 23),
    _AcDs1ConfigInvalidDays_Type()
)
acDs1ConfigInvalidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigInvalidDays.setStatus("current")


class _AcDs1ConfigInvalidFarEndIntervals_Type(Integer32):
    """Custom type acDs1ConfigInvalidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs1ConfigInvalidFarEndIntervals_Type.__name__ = "Integer32"
_AcDs1ConfigInvalidFarEndIntervals_Object = MibTableColumn
acDs1ConfigInvalidFarEndIntervals = _AcDs1ConfigInvalidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 24),
    _AcDs1ConfigInvalidFarEndIntervals_Type()
)
acDs1ConfigInvalidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigInvalidFarEndIntervals.setStatus("current")


class _AcDs1ConfigInvalidFarEndDays_Type(Integer32):
    """Custom type acDs1ConfigInvalidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs1ConfigInvalidFarEndDays_Type.__name__ = "Integer32"
_AcDs1ConfigInvalidFarEndDays_Object = MibTableColumn
acDs1ConfigInvalidFarEndDays = _AcDs1ConfigInvalidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 25),
    _AcDs1ConfigInvalidFarEndDays_Type()
)
acDs1ConfigInvalidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigInvalidFarEndDays.setStatus("current")
_AcDs1ConfigLineStatusLastChange_Type = TimeStamp
_AcDs1ConfigLineStatusLastChange_Object = MibTableColumn
acDs1ConfigLineStatusLastChange = _AcDs1ConfigLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 26),
    _AcDs1ConfigLineStatusLastChange_Type()
)
acDs1ConfigLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigLineStatusLastChange.setStatus("current")


class _AcDs1ConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type acDs1ConfigLineStatusChangeTrapEnable based on Integer32"""
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


_AcDs1ConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_AcDs1ConfigLineStatusChangeTrapEnable_Object = MibTableColumn
acDs1ConfigLineStatusChangeTrapEnable = _AcDs1ConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 27),
    _AcDs1ConfigLineStatusChangeTrapEnable_Type()
)
acDs1ConfigLineStatusChangeTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigLineStatusChangeTrapEnable.setStatus("current")


class _AcDs1ConfigLoopbackStatus_Type(Integer32):
    """Custom type acDs1ConfigLoopbackStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AcDs1ConfigLoopbackStatus_Type.__name__ = "Integer32"
_AcDs1ConfigLoopbackStatus_Object = MibTableColumn
acDs1ConfigLoopbackStatus = _AcDs1ConfigLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 28),
    _AcDs1ConfigLoopbackStatus_Type()
)
acDs1ConfigLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1ConfigLoopbackStatus.setStatus("current")


class _AcDs1ConfigInterfaceName_Type(DisplayString):
    """Custom type acDs1ConfigInterfaceName based on DisplayString"""
    defaultValue = OctetString("DS-1/TDM Interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcDs1ConfigInterfaceName_Type.__name__ = "DisplayString"
_AcDs1ConfigInterfaceName_Object = MibTableColumn
acDs1ConfigInterfaceName = _AcDs1ConfigInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 29),
    _AcDs1ConfigInterfaceName_Type()
)
acDs1ConfigInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigInterfaceName.setStatus("current")
_AcDs1ConfigTimeSlotIndex_Type = Integer32
_AcDs1ConfigTimeSlotIndex_Object = MibTableColumn
acDs1ConfigTimeSlotIndex = _AcDs1ConfigTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 1, 1, 30),
    _AcDs1ConfigTimeSlotIndex_Type()
)
acDs1ConfigTimeSlotIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs1ConfigTimeSlotIndex.setStatus("current")
_AcDs1IntervalTable_Object = MibTable
acDs1IntervalTable = _AcDs1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    acDs1IntervalTable.setStatus("current")
_AcDs1IntervalEntry_Object = MibTableRow
acDs1IntervalEntry = _AcDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1)
)
acDs1IntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1IntervalNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1IntervalSlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1IntervalPort"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1IntervalNumber"),
)
if mibBuilder.loadTexts:
    acDs1IntervalEntry.setStatus("current")
_AcDs1IntervalNodeId_Type = AcNodeId
_AcDs1IntervalNodeId_Object = MibTableColumn
acDs1IntervalNodeId = _AcDs1IntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 1),
    _AcDs1IntervalNodeId_Type()
)
acDs1IntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1IntervalNodeId.setStatus("current")
_AcDs1IntervalSlot_Type = AcSlotNumber
_AcDs1IntervalSlot_Object = MibTableColumn
acDs1IntervalSlot = _AcDs1IntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 2),
    _AcDs1IntervalSlot_Type()
)
acDs1IntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1IntervalSlot.setStatus("current")
_AcDs1IntervalPort_Type = AcPortNumber
_AcDs1IntervalPort_Object = MibTableColumn
acDs1IntervalPort = _AcDs1IntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 3),
    _AcDs1IntervalPort_Type()
)
acDs1IntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1IntervalPort.setStatus("current")


class _AcDs1IntervalNumber_Type(Integer32):
    """Custom type acDs1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcDs1IntervalNumber_Type.__name__ = "Integer32"
_AcDs1IntervalNumber_Object = MibTableColumn
acDs1IntervalNumber = _AcDs1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 4),
    _AcDs1IntervalNumber_Type()
)
acDs1IntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1IntervalNumber.setStatus("current")
_AcDs1IntervalValidStats_Type = TruthValue
_AcDs1IntervalValidStats_Object = MibTableColumn
acDs1IntervalValidStats = _AcDs1IntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 5),
    _AcDs1IntervalValidStats_Type()
)
acDs1IntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalValidStats.setStatus("current")
_AcDs1IntervalResetStats_Type = TruthValue
_AcDs1IntervalResetStats_Object = MibTableColumn
acDs1IntervalResetStats = _AcDs1IntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 6),
    _AcDs1IntervalResetStats_Type()
)
acDs1IntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1IntervalResetStats.setStatus("current")
_AcDs1IntervalESs_Type = PerfIntervalCount
_AcDs1IntervalESs_Object = MibTableColumn
acDs1IntervalESs = _AcDs1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 7),
    _AcDs1IntervalESs_Type()
)
acDs1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalESs.setStatus("current")
_AcDs1IntervalSESs_Type = PerfIntervalCount
_AcDs1IntervalSESs_Object = MibTableColumn
acDs1IntervalSESs = _AcDs1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 8),
    _AcDs1IntervalSESs_Type()
)
acDs1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalSESs.setStatus("current")
_AcDs1IntervalSEFSs_Type = PerfIntervalCount
_AcDs1IntervalSEFSs_Object = MibTableColumn
acDs1IntervalSEFSs = _AcDs1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 9),
    _AcDs1IntervalSEFSs_Type()
)
acDs1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalSEFSs.setStatus("current")
_AcDs1IntervalUASs_Type = PerfIntervalCount
_AcDs1IntervalUASs_Object = MibTableColumn
acDs1IntervalUASs = _AcDs1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 10),
    _AcDs1IntervalUASs_Type()
)
acDs1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalUASs.setStatus("current")
_AcDs1IntervalCSSs_Type = PerfIntervalCount
_AcDs1IntervalCSSs_Object = MibTableColumn
acDs1IntervalCSSs = _AcDs1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 11),
    _AcDs1IntervalCSSs_Type()
)
acDs1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalCSSs.setStatus("current")
_AcDs1IntervalPCVs_Type = PerfIntervalCount
_AcDs1IntervalPCVs_Object = MibTableColumn
acDs1IntervalPCVs = _AcDs1IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 12),
    _AcDs1IntervalPCVs_Type()
)
acDs1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalPCVs.setStatus("current")
_AcDs1IntervalLESs_Type = PerfIntervalCount
_AcDs1IntervalLESs_Object = MibTableColumn
acDs1IntervalLESs = _AcDs1IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 13),
    _AcDs1IntervalLESs_Type()
)
acDs1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalLESs.setStatus("current")
_AcDs1IntervalBESs_Type = PerfIntervalCount
_AcDs1IntervalBESs_Object = MibTableColumn
acDs1IntervalBESs = _AcDs1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 14),
    _AcDs1IntervalBESs_Type()
)
acDs1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalBESs.setStatus("current")
_AcDs1IntervalDMs_Type = PerfIntervalCount
_AcDs1IntervalDMs_Object = MibTableColumn
acDs1IntervalDMs = _AcDs1IntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 15),
    _AcDs1IntervalDMs_Type()
)
acDs1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalDMs.setStatus("current")
_AcDs1IntervalLCVs_Type = PerfIntervalCount
_AcDs1IntervalLCVs_Object = MibTableColumn
acDs1IntervalLCVs = _AcDs1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 2, 1, 16),
    _AcDs1IntervalLCVs_Type()
)
acDs1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1IntervalLCVs.setStatus("current")
_AcDs1DayTable_Object = MibTable
acDs1DayTable = _AcDs1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3)
)
if mibBuilder.loadTexts:
    acDs1DayTable.setStatus("current")
_AcDs1DayEntry_Object = MibTableRow
acDs1DayEntry = _AcDs1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1)
)
acDs1DayEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1DayNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1DaySlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1DayPort"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1DayNumber"),
)
if mibBuilder.loadTexts:
    acDs1DayEntry.setStatus("current")
_AcDs1DayNodeId_Type = AcNodeId
_AcDs1DayNodeId_Object = MibTableColumn
acDs1DayNodeId = _AcDs1DayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 1),
    _AcDs1DayNodeId_Type()
)
acDs1DayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1DayNodeId.setStatus("current")
_AcDs1DaySlot_Type = AcSlotNumber
_AcDs1DaySlot_Object = MibTableColumn
acDs1DaySlot = _AcDs1DaySlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 2),
    _AcDs1DaySlot_Type()
)
acDs1DaySlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1DaySlot.setStatus("current")
_AcDs1DayPort_Type = AcPortNumber
_AcDs1DayPort_Object = MibTableColumn
acDs1DayPort = _AcDs1DayPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 3),
    _AcDs1DayPort_Type()
)
acDs1DayPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1DayPort.setStatus("current")


class _AcDs1DayNumber_Type(Integer32):
    """Custom type acDs1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcDs1DayNumber_Type.__name__ = "Integer32"
_AcDs1DayNumber_Object = MibTableColumn
acDs1DayNumber = _AcDs1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 4),
    _AcDs1DayNumber_Type()
)
acDs1DayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1DayNumber.setStatus("current")
_AcDs1DayValidStats_Type = TruthValue
_AcDs1DayValidStats_Object = MibTableColumn
acDs1DayValidStats = _AcDs1DayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 5),
    _AcDs1DayValidStats_Type()
)
acDs1DayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayValidStats.setStatus("current")
_AcDs1DayResetStats_Type = TruthValue
_AcDs1DayResetStats_Object = MibTableColumn
acDs1DayResetStats = _AcDs1DayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 6),
    _AcDs1DayResetStats_Type()
)
acDs1DayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1DayResetStats.setStatus("current")
_AcDs1DayESs_Type = PerfIntervalCount
_AcDs1DayESs_Object = MibTableColumn
acDs1DayESs = _AcDs1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 7),
    _AcDs1DayESs_Type()
)
acDs1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayESs.setStatus("current")
_AcDs1DaySESs_Type = PerfIntervalCount
_AcDs1DaySESs_Object = MibTableColumn
acDs1DaySESs = _AcDs1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 8),
    _AcDs1DaySESs_Type()
)
acDs1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DaySESs.setStatus("current")
_AcDs1DaySEFSs_Type = PerfIntervalCount
_AcDs1DaySEFSs_Object = MibTableColumn
acDs1DaySEFSs = _AcDs1DaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 9),
    _AcDs1DaySEFSs_Type()
)
acDs1DaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DaySEFSs.setStatus("current")
_AcDs1DayUASs_Type = PerfIntervalCount
_AcDs1DayUASs_Object = MibTableColumn
acDs1DayUASs = _AcDs1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 10),
    _AcDs1DayUASs_Type()
)
acDs1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayUASs.setStatus("current")
_AcDs1DayCSSs_Type = PerfIntervalCount
_AcDs1DayCSSs_Object = MibTableColumn
acDs1DayCSSs = _AcDs1DayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 11),
    _AcDs1DayCSSs_Type()
)
acDs1DayCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayCSSs.setStatus("current")
_AcDs1DayPCVs_Type = PerfIntervalCount
_AcDs1DayPCVs_Object = MibTableColumn
acDs1DayPCVs = _AcDs1DayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 12),
    _AcDs1DayPCVs_Type()
)
acDs1DayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayPCVs.setStatus("current")
_AcDs1DayLESs_Type = PerfIntervalCount
_AcDs1DayLESs_Object = MibTableColumn
acDs1DayLESs = _AcDs1DayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 13),
    _AcDs1DayLESs_Type()
)
acDs1DayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayLESs.setStatus("current")
_AcDs1DayBESs_Type = PerfIntervalCount
_AcDs1DayBESs_Object = MibTableColumn
acDs1DayBESs = _AcDs1DayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 14),
    _AcDs1DayBESs_Type()
)
acDs1DayBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayBESs.setStatus("current")
_AcDs1DayDMs_Type = PerfIntervalCount
_AcDs1DayDMs_Object = MibTableColumn
acDs1DayDMs = _AcDs1DayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 15),
    _AcDs1DayDMs_Type()
)
acDs1DayDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayDMs.setStatus("current")
_AcDs1DayLCVs_Type = PerfIntervalCount
_AcDs1DayLCVs_Object = MibTableColumn
acDs1DayLCVs = _AcDs1DayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 3, 1, 16),
    _AcDs1DayLCVs_Type()
)
acDs1DayLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1DayLCVs.setStatus("current")
_AcDs1FarEndIntervalTable_Object = MibTable
acDs1FarEndIntervalTable = _AcDs1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4)
)
if mibBuilder.loadTexts:
    acDs1FarEndIntervalTable.setStatus("current")
_AcDs1FarEndIntervalEntry_Object = MibTableRow
acDs1FarEndIntervalEntry = _AcDs1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1)
)
acDs1FarEndIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndIntervalNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndIntervalSlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndIntervalPort"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    acDs1FarEndIntervalEntry.setStatus("current")
_AcDs1FarEndIntervalNodeId_Type = AcNodeId
_AcDs1FarEndIntervalNodeId_Object = MibTableColumn
acDs1FarEndIntervalNodeId = _AcDs1FarEndIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 1),
    _AcDs1FarEndIntervalNodeId_Type()
)
acDs1FarEndIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalNodeId.setStatus("current")
_AcDs1FarEndIntervalSlot_Type = AcSlotNumber
_AcDs1FarEndIntervalSlot_Object = MibTableColumn
acDs1FarEndIntervalSlot = _AcDs1FarEndIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 2),
    _AcDs1FarEndIntervalSlot_Type()
)
acDs1FarEndIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalSlot.setStatus("current")
_AcDs1FarEndIntervalPort_Type = AcPortNumber
_AcDs1FarEndIntervalPort_Object = MibTableColumn
acDs1FarEndIntervalPort = _AcDs1FarEndIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 3),
    _AcDs1FarEndIntervalPort_Type()
)
acDs1FarEndIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalPort.setStatus("current")


class _AcDs1FarEndIntervalNumber_Type(Integer32):
    """Custom type acDs1FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcDs1FarEndIntervalNumber_Type.__name__ = "Integer32"
_AcDs1FarEndIntervalNumber_Object = MibTableColumn
acDs1FarEndIntervalNumber = _AcDs1FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 4),
    _AcDs1FarEndIntervalNumber_Type()
)
acDs1FarEndIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalNumber.setStatus("current")
_AcDs1FarEndIntervalValidStats_Type = TruthValue
_AcDs1FarEndIntervalValidStats_Object = MibTableColumn
acDs1FarEndIntervalValidStats = _AcDs1FarEndIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 5),
    _AcDs1FarEndIntervalValidStats_Type()
)
acDs1FarEndIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalValidStats.setStatus("current")
_AcDs1FarEndIntervalResetStats_Type = TruthValue
_AcDs1FarEndIntervalResetStats_Object = MibTableColumn
acDs1FarEndIntervalResetStats = _AcDs1FarEndIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 6),
    _AcDs1FarEndIntervalResetStats_Type()
)
acDs1FarEndIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalResetStats.setStatus("current")
_AcDs1FarEndIntervalESs_Type = PerfIntervalCount
_AcDs1FarEndIntervalESs_Object = MibTableColumn
acDs1FarEndIntervalESs = _AcDs1FarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 7),
    _AcDs1FarEndIntervalESs_Type()
)
acDs1FarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalESs.setStatus("current")
_AcDs1FarEndIntervalSESs_Type = PerfIntervalCount
_AcDs1FarEndIntervalSESs_Object = MibTableColumn
acDs1FarEndIntervalSESs = _AcDs1FarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 8),
    _AcDs1FarEndIntervalSESs_Type()
)
acDs1FarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalSESs.setStatus("current")
_AcDs1FarEndIntervalSEFSs_Type = PerfIntervalCount
_AcDs1FarEndIntervalSEFSs_Object = MibTableColumn
acDs1FarEndIntervalSEFSs = _AcDs1FarEndIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 9),
    _AcDs1FarEndIntervalSEFSs_Type()
)
acDs1FarEndIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalSEFSs.setStatus("current")
_AcDs1FarEndIntervalUASs_Type = PerfIntervalCount
_AcDs1FarEndIntervalUASs_Object = MibTableColumn
acDs1FarEndIntervalUASs = _AcDs1FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 10),
    _AcDs1FarEndIntervalUASs_Type()
)
acDs1FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalUASs.setStatus("current")
_AcDs1FarEndIntervalCSSs_Type = PerfIntervalCount
_AcDs1FarEndIntervalCSSs_Object = MibTableColumn
acDs1FarEndIntervalCSSs = _AcDs1FarEndIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 11),
    _AcDs1FarEndIntervalCSSs_Type()
)
acDs1FarEndIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalCSSs.setStatus("current")
_AcDs1FarEndIntervalLESs_Type = PerfIntervalCount
_AcDs1FarEndIntervalLESs_Object = MibTableColumn
acDs1FarEndIntervalLESs = _AcDs1FarEndIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 12),
    _AcDs1FarEndIntervalLESs_Type()
)
acDs1FarEndIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalLESs.setStatus("current")
_AcDs1FarEndIntervalPCVs_Type = PerfIntervalCount
_AcDs1FarEndIntervalPCVs_Object = MibTableColumn
acDs1FarEndIntervalPCVs = _AcDs1FarEndIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 13),
    _AcDs1FarEndIntervalPCVs_Type()
)
acDs1FarEndIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalPCVs.setStatus("current")
_AcDs1FarEndIntervalBESs_Type = PerfIntervalCount
_AcDs1FarEndIntervalBESs_Object = MibTableColumn
acDs1FarEndIntervalBESs = _AcDs1FarEndIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 14),
    _AcDs1FarEndIntervalBESs_Type()
)
acDs1FarEndIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalBESs.setStatus("current")
_AcDs1FarEndIntervalDMs_Type = PerfIntervalCount
_AcDs1FarEndIntervalDMs_Object = MibTableColumn
acDs1FarEndIntervalDMs = _AcDs1FarEndIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 4, 1, 15),
    _AcDs1FarEndIntervalDMs_Type()
)
acDs1FarEndIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndIntervalDMs.setStatus("current")
_AcDs1FarEndDayTable_Object = MibTable
acDs1FarEndDayTable = _AcDs1FarEndDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5)
)
if mibBuilder.loadTexts:
    acDs1FarEndDayTable.setStatus("current")
_AcDs1FarEndDayEntry_Object = MibTableRow
acDs1FarEndDayEntry = _AcDs1FarEndDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1)
)
acDs1FarEndDayEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndDayNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndDaySlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndDayPort"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1FarEndDayNumber"),
)
if mibBuilder.loadTexts:
    acDs1FarEndDayEntry.setStatus("current")
_AcDs1FarEndDayNodeId_Type = AcNodeId
_AcDs1FarEndDayNodeId_Object = MibTableColumn
acDs1FarEndDayNodeId = _AcDs1FarEndDayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 1),
    _AcDs1FarEndDayNodeId_Type()
)
acDs1FarEndDayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndDayNodeId.setStatus("current")
_AcDs1FarEndDaySlot_Type = AcSlotNumber
_AcDs1FarEndDaySlot_Object = MibTableColumn
acDs1FarEndDaySlot = _AcDs1FarEndDaySlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 2),
    _AcDs1FarEndDaySlot_Type()
)
acDs1FarEndDaySlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndDaySlot.setStatus("current")
_AcDs1FarEndDayPort_Type = AcPortNumber
_AcDs1FarEndDayPort_Object = MibTableColumn
acDs1FarEndDayPort = _AcDs1FarEndDayPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 3),
    _AcDs1FarEndDayPort_Type()
)
acDs1FarEndDayPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndDayPort.setStatus("current")


class _AcDs1FarEndDayNumber_Type(Integer32):
    """Custom type acDs1FarEndDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcDs1FarEndDayNumber_Type.__name__ = "Integer32"
_AcDs1FarEndDayNumber_Object = MibTableColumn
acDs1FarEndDayNumber = _AcDs1FarEndDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 4),
    _AcDs1FarEndDayNumber_Type()
)
acDs1FarEndDayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1FarEndDayNumber.setStatus("current")
_AcDs1FarEndDayValidStats_Type = TruthValue
_AcDs1FarEndDayValidStats_Object = MibTableColumn
acDs1FarEndDayValidStats = _AcDs1FarEndDayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 5),
    _AcDs1FarEndDayValidStats_Type()
)
acDs1FarEndDayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayValidStats.setStatus("current")
_AcDs1FarEndDayResetStats_Type = TruthValue
_AcDs1FarEndDayResetStats_Object = MibTableColumn
acDs1FarEndDayResetStats = _AcDs1FarEndDayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 6),
    _AcDs1FarEndDayResetStats_Type()
)
acDs1FarEndDayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1FarEndDayResetStats.setStatus("current")
_AcDs1FarEndDayESs_Type = PerfIntervalCount
_AcDs1FarEndDayESs_Object = MibTableColumn
acDs1FarEndDayESs = _AcDs1FarEndDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 7),
    _AcDs1FarEndDayESs_Type()
)
acDs1FarEndDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayESs.setStatus("current")
_AcDs1FarEndDaySESs_Type = PerfIntervalCount
_AcDs1FarEndDaySESs_Object = MibTableColumn
acDs1FarEndDaySESs = _AcDs1FarEndDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 8),
    _AcDs1FarEndDaySESs_Type()
)
acDs1FarEndDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDaySESs.setStatus("current")
_AcDs1FarEndDaySEFSs_Type = PerfIntervalCount
_AcDs1FarEndDaySEFSs_Object = MibTableColumn
acDs1FarEndDaySEFSs = _AcDs1FarEndDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 9),
    _AcDs1FarEndDaySEFSs_Type()
)
acDs1FarEndDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDaySEFSs.setStatus("current")
_AcDs1FarEndDayUASs_Type = PerfIntervalCount
_AcDs1FarEndDayUASs_Object = MibTableColumn
acDs1FarEndDayUASs = _AcDs1FarEndDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 10),
    _AcDs1FarEndDayUASs_Type()
)
acDs1FarEndDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayUASs.setStatus("current")
_AcDs1FarEndDayCSSs_Type = PerfIntervalCount
_AcDs1FarEndDayCSSs_Object = MibTableColumn
acDs1FarEndDayCSSs = _AcDs1FarEndDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 11),
    _AcDs1FarEndDayCSSs_Type()
)
acDs1FarEndDayCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayCSSs.setStatus("current")
_AcDs1FarEndDayLESs_Type = PerfIntervalCount
_AcDs1FarEndDayLESs_Object = MibTableColumn
acDs1FarEndDayLESs = _AcDs1FarEndDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 12),
    _AcDs1FarEndDayLESs_Type()
)
acDs1FarEndDayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayLESs.setStatus("current")
_AcDs1FarEndDayPCVs_Type = PerfIntervalCount
_AcDs1FarEndDayPCVs_Object = MibTableColumn
acDs1FarEndDayPCVs = _AcDs1FarEndDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 13),
    _AcDs1FarEndDayPCVs_Type()
)
acDs1FarEndDayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayPCVs.setStatus("current")
_AcDs1FarEndDayBESs_Type = PerfIntervalCount
_AcDs1FarEndDayBESs_Object = MibTableColumn
acDs1FarEndDayBESs = _AcDs1FarEndDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 14),
    _AcDs1FarEndDayBESs_Type()
)
acDs1FarEndDayBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayBESs.setStatus("current")
_AcDs1FarEndDayDMs_Type = PerfIntervalCount
_AcDs1FarEndDayDMs_Object = MibTableColumn
acDs1FarEndDayDMs = _AcDs1FarEndDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 5, 1, 15),
    _AcDs1FarEndDayDMs_Type()
)
acDs1FarEndDayDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs1FarEndDayDMs.setStatus("current")
_AcDs1ThresholdTable_Object = MibTable
acDs1ThresholdTable = _AcDs1ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6)
)
if mibBuilder.loadTexts:
    acDs1ThresholdTable.setStatus("current")
_AcDs1ThresholdEntry_Object = MibTableRow
acDs1ThresholdEntry = _AcDs1ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1)
)
acDs1ThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
    (0, "APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"),
)
if mibBuilder.loadTexts:
    acDs1ThresholdEntry.setStatus("current")
_AcDs1ThresholdNodeId_Type = AcNodeId
_AcDs1ThresholdNodeId_Object = MibTableColumn
acDs1ThresholdNodeId = _AcDs1ThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 1),
    _AcDs1ThresholdNodeId_Type()
)
acDs1ThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ThresholdNodeId.setStatus("current")
_AcDs1ThresholdSlot_Type = AcSlotNumber
_AcDs1ThresholdSlot_Object = MibTableColumn
acDs1ThresholdSlot = _AcDs1ThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 2),
    _AcDs1ThresholdSlot_Type()
)
acDs1ThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ThresholdSlot.setStatus("current")
_AcDs1ThresholdPort_Type = AcPortNumber
_AcDs1ThresholdPort_Object = MibTableColumn
acDs1ThresholdPort = _AcDs1ThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 3),
    _AcDs1ThresholdPort_Type()
)
acDs1ThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs1ThresholdPort.setStatus("current")


class _AcDs1ThresholdNEIntervalESs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalESs_Object = MibTableColumn
acDs1ThresholdNEIntervalESs = _AcDs1ThresholdNEIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 4),
    _AcDs1ThresholdNEIntervalESs_Type()
)
acDs1ThresholdNEIntervalESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalESs.setStatus("current")


class _AcDs1ThresholdNEIntervalSESs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalSESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalSESs_Object = MibTableColumn
acDs1ThresholdNEIntervalSESs = _AcDs1ThresholdNEIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 5),
    _AcDs1ThresholdNEIntervalSESs_Type()
)
acDs1ThresholdNEIntervalSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalSESs.setStatus("current")


class _AcDs1ThresholdNEIntervalSEFSs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalSEFSs_Object = MibTableColumn
acDs1ThresholdNEIntervalSEFSs = _AcDs1ThresholdNEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 6),
    _AcDs1ThresholdNEIntervalSEFSs_Type()
)
acDs1ThresholdNEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalSEFSs.setStatus("current")


class _AcDs1ThresholdNEIntervalUASs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalUASs_Object = MibTableColumn
acDs1ThresholdNEIntervalUASs = _AcDs1ThresholdNEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 7),
    _AcDs1ThresholdNEIntervalUASs_Type()
)
acDs1ThresholdNEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalUASs.setStatus("current")


class _AcDs1ThresholdNEIntervalCSSs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalCSSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalCSSs_Object = MibTableColumn
acDs1ThresholdNEIntervalCSSs = _AcDs1ThresholdNEIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 8),
    _AcDs1ThresholdNEIntervalCSSs_Type()
)
acDs1ThresholdNEIntervalCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalCSSs.setStatus("current")


class _AcDs1ThresholdNEIntervalPCVs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalPCVs_Object = MibTableColumn
acDs1ThresholdNEIntervalPCVs = _AcDs1ThresholdNEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 9),
    _AcDs1ThresholdNEIntervalPCVs_Type()
)
acDs1ThresholdNEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalPCVs.setStatus("current")


class _AcDs1ThresholdNEIntervalLESs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalLESs_Object = MibTableColumn
acDs1ThresholdNEIntervalLESs = _AcDs1ThresholdNEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 10),
    _AcDs1ThresholdNEIntervalLESs_Type()
)
acDs1ThresholdNEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalLESs.setStatus("current")


class _AcDs1ThresholdNEIntervalBESs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalBESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalBESs_Object = MibTableColumn
acDs1ThresholdNEIntervalBESs = _AcDs1ThresholdNEIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 11),
    _AcDs1ThresholdNEIntervalBESs_Type()
)
acDs1ThresholdNEIntervalBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalBESs.setStatus("current")


class _AcDs1ThresholdNEIntervalDMs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalDMs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalDMs_Object = MibTableColumn
acDs1ThresholdNEIntervalDMs = _AcDs1ThresholdNEIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 12),
    _AcDs1ThresholdNEIntervalDMs_Type()
)
acDs1ThresholdNEIntervalDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalDMs.setStatus("current")


class _AcDs1ThresholdNEIntervalLCVs_Type(Integer32):
    """Custom type acDs1ThresholdNEIntervalLCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEIntervalLCVs_Object = MibTableColumn
acDs1ThresholdNEIntervalLCVs = _AcDs1ThresholdNEIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 13),
    _AcDs1ThresholdNEIntervalLCVs_Type()
)
acDs1ThresholdNEIntervalLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEIntervalLCVs.setStatus("current")


class _AcDs1ThresholdNEDayESs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayESs_Object = MibTableColumn
acDs1ThresholdNEDayESs = _AcDs1ThresholdNEDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 14),
    _AcDs1ThresholdNEDayESs_Type()
)
acDs1ThresholdNEDayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayESs.setStatus("current")


class _AcDs1ThresholdNEDaySESs_Type(Integer32):
    """Custom type acDs1ThresholdNEDaySESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDaySESs_Object = MibTableColumn
acDs1ThresholdNEDaySESs = _AcDs1ThresholdNEDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 15),
    _AcDs1ThresholdNEDaySESs_Type()
)
acDs1ThresholdNEDaySESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDaySESs.setStatus("current")


class _AcDs1ThresholdNEDaySEFSs_Type(Integer32):
    """Custom type acDs1ThresholdNEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDaySEFSs_Object = MibTableColumn
acDs1ThresholdNEDaySEFSs = _AcDs1ThresholdNEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 16),
    _AcDs1ThresholdNEDaySEFSs_Type()
)
acDs1ThresholdNEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDaySEFSs.setStatus("current")


class _AcDs1ThresholdNEDayUASs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayUASs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayUASs_Object = MibTableColumn
acDs1ThresholdNEDayUASs = _AcDs1ThresholdNEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 17),
    _AcDs1ThresholdNEDayUASs_Type()
)
acDs1ThresholdNEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayUASs.setStatus("current")


class _AcDs1ThresholdNEDayCSSs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayCSSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayCSSs_Object = MibTableColumn
acDs1ThresholdNEDayCSSs = _AcDs1ThresholdNEDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 18),
    _AcDs1ThresholdNEDayCSSs_Type()
)
acDs1ThresholdNEDayCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayCSSs.setStatus("current")


class _AcDs1ThresholdNEDayPCVs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayPCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayPCVs_Object = MibTableColumn
acDs1ThresholdNEDayPCVs = _AcDs1ThresholdNEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 19),
    _AcDs1ThresholdNEDayPCVs_Type()
)
acDs1ThresholdNEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayPCVs.setStatus("current")


class _AcDs1ThresholdNEDayLESs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayLESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayLESs_Object = MibTableColumn
acDs1ThresholdNEDayLESs = _AcDs1ThresholdNEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 20),
    _AcDs1ThresholdNEDayLESs_Type()
)
acDs1ThresholdNEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayLESs.setStatus("current")


class _AcDs1ThresholdNEDayBESs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayBESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayBESs_Object = MibTableColumn
acDs1ThresholdNEDayBESs = _AcDs1ThresholdNEDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 21),
    _AcDs1ThresholdNEDayBESs_Type()
)
acDs1ThresholdNEDayBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayBESs.setStatus("current")


class _AcDs1ThresholdNEDayDMs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayDMs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayDMs_Object = MibTableColumn
acDs1ThresholdNEDayDMs = _AcDs1ThresholdNEDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 22),
    _AcDs1ThresholdNEDayDMs_Type()
)
acDs1ThresholdNEDayDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayDMs.setStatus("current")


class _AcDs1ThresholdNEDayLCVs_Type(Integer32):
    """Custom type acDs1ThresholdNEDayLCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdNEDayLCVs_Object = MibTableColumn
acDs1ThresholdNEDayLCVs = _AcDs1ThresholdNEDayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 23),
    _AcDs1ThresholdNEDayLCVs_Type()
)
acDs1ThresholdNEDayLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdNEDayLCVs.setStatus("current")


class _AcDs1ThresholdFEIntervalESs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalESs_Object = MibTableColumn
acDs1ThresholdFEIntervalESs = _AcDs1ThresholdFEIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 24),
    _AcDs1ThresholdFEIntervalESs_Type()
)
acDs1ThresholdFEIntervalESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalESs.setStatus("current")


class _AcDs1ThresholdFEIntervalSESs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalSESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalSESs_Object = MibTableColumn
acDs1ThresholdFEIntervalSESs = _AcDs1ThresholdFEIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 25),
    _AcDs1ThresholdFEIntervalSESs_Type()
)
acDs1ThresholdFEIntervalSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalSESs.setStatus("current")


class _AcDs1ThresholdFEIntervalSEFSs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalSEFSs_Object = MibTableColumn
acDs1ThresholdFEIntervalSEFSs = _AcDs1ThresholdFEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 26),
    _AcDs1ThresholdFEIntervalSEFSs_Type()
)
acDs1ThresholdFEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalSEFSs.setStatus("current")


class _AcDs1ThresholdFEIntervalUASs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalUASs_Object = MibTableColumn
acDs1ThresholdFEIntervalUASs = _AcDs1ThresholdFEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 27),
    _AcDs1ThresholdFEIntervalUASs_Type()
)
acDs1ThresholdFEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalUASs.setStatus("current")


class _AcDs1ThresholdFEIntervalCSSs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalCSSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalCSSs_Object = MibTableColumn
acDs1ThresholdFEIntervalCSSs = _AcDs1ThresholdFEIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 28),
    _AcDs1ThresholdFEIntervalCSSs_Type()
)
acDs1ThresholdFEIntervalCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalCSSs.setStatus("current")


class _AcDs1ThresholdFEIntervalLESs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalLESs_Object = MibTableColumn
acDs1ThresholdFEIntervalLESs = _AcDs1ThresholdFEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 29),
    _AcDs1ThresholdFEIntervalLESs_Type()
)
acDs1ThresholdFEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalLESs.setStatus("current")


class _AcDs1ThresholdFEIntervalPCVs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalPCVs_Object = MibTableColumn
acDs1ThresholdFEIntervalPCVs = _AcDs1ThresholdFEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 30),
    _AcDs1ThresholdFEIntervalPCVs_Type()
)
acDs1ThresholdFEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalPCVs.setStatus("current")


class _AcDs1ThresholdFEIntervalBESs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalBESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalBESs_Object = MibTableColumn
acDs1ThresholdFEIntervalBESs = _AcDs1ThresholdFEIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 31),
    _AcDs1ThresholdFEIntervalBESs_Type()
)
acDs1ThresholdFEIntervalBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalBESs.setStatus("current")


class _AcDs1ThresholdFEIntervalDMs_Type(Integer32):
    """Custom type acDs1ThresholdFEIntervalDMs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEIntervalDMs_Object = MibTableColumn
acDs1ThresholdFEIntervalDMs = _AcDs1ThresholdFEIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 32),
    _AcDs1ThresholdFEIntervalDMs_Type()
)
acDs1ThresholdFEIntervalDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEIntervalDMs.setStatus("current")


class _AcDs1ThresholdFEDayESs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayESs_Object = MibTableColumn
acDs1ThresholdFEDayESs = _AcDs1ThresholdFEDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 33),
    _AcDs1ThresholdFEDayESs_Type()
)
acDs1ThresholdFEDayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayESs.setStatus("current")


class _AcDs1ThresholdFEDaySESs_Type(Integer32):
    """Custom type acDs1ThresholdFEDaySESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDaySESs_Object = MibTableColumn
acDs1ThresholdFEDaySESs = _AcDs1ThresholdFEDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 34),
    _AcDs1ThresholdFEDaySESs_Type()
)
acDs1ThresholdFEDaySESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDaySESs.setStatus("current")


class _AcDs1ThresholdFEDaySEFSs_Type(Integer32):
    """Custom type acDs1ThresholdFEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDaySEFSs_Object = MibTableColumn
acDs1ThresholdFEDaySEFSs = _AcDs1ThresholdFEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 35),
    _AcDs1ThresholdFEDaySEFSs_Type()
)
acDs1ThresholdFEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDaySEFSs.setStatus("current")


class _AcDs1ThresholdFEDayUASs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayUASs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayUASs_Object = MibTableColumn
acDs1ThresholdFEDayUASs = _AcDs1ThresholdFEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 36),
    _AcDs1ThresholdFEDayUASs_Type()
)
acDs1ThresholdFEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayUASs.setStatus("current")


class _AcDs1ThresholdFEDayCSSs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayCSSs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayCSSs_Object = MibTableColumn
acDs1ThresholdFEDayCSSs = _AcDs1ThresholdFEDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 37),
    _AcDs1ThresholdFEDayCSSs_Type()
)
acDs1ThresholdFEDayCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayCSSs.setStatus("current")


class _AcDs1ThresholdFEDayLESs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayLESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayLESs_Object = MibTableColumn
acDs1ThresholdFEDayLESs = _AcDs1ThresholdFEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 38),
    _AcDs1ThresholdFEDayLESs_Type()
)
acDs1ThresholdFEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayLESs.setStatus("current")


class _AcDs1ThresholdFEDayPCVs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayPCVs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayPCVs_Object = MibTableColumn
acDs1ThresholdFEDayPCVs = _AcDs1ThresholdFEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 39),
    _AcDs1ThresholdFEDayPCVs_Type()
)
acDs1ThresholdFEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayPCVs.setStatus("current")


class _AcDs1ThresholdFEDayBESs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayBESs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayBESs_Object = MibTableColumn
acDs1ThresholdFEDayBESs = _AcDs1ThresholdFEDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 40),
    _AcDs1ThresholdFEDayBESs_Type()
)
acDs1ThresholdFEDayBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayBESs.setStatus("current")


class _AcDs1ThresholdFEDayDMs_Type(Integer32):
    """Custom type acDs1ThresholdFEDayDMs based on Integer32"""
    defaultValue = 0


_AcDs1ThresholdFEDayDMs_Object = MibTableColumn
acDs1ThresholdFEDayDMs = _AcDs1ThresholdFEDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 6, 1, 41),
    _AcDs1ThresholdFEDayDMs_Type()
)
acDs1ThresholdFEDayDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs1ThresholdFEDayDMs.setStatus("current")

# Managed Objects groups


# Notification objects

acDs1LineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 1)
)
acDs1LineStatusChangeTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigLineStatus"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigLineStatusLastChange"))
)
if mibBuilder.loadTexts:
    acDs1LineStatusChangeTrap.setStatus(
        "current"
    )

acDs1StatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 2)
)
acDs1StatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs1StatsResetTrap.setStatus(
        "current"
    )

acDs1CfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 3)
)
acDs1CfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs1CfgErrorTrap.setStatus(
        "current"
    )

acDs1LinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 4)
)
acDs1LinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs1LinkDownTrap.setStatus(
        "current"
    )

acDs1LinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 5)
)
acDs1LinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs1LinkUpTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 7)
)
acDs1ExceededThresholdNEIntervalESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 8)
)
acDs1ExceededThresholdNEIntervalSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalSESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 9)
)
acDs1ExceededThresholdNEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalSEFSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 10)
)
acDs1ExceededThresholdNEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalUASsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 11)
)
acDs1ExceededThresholdNEIntervalCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalCSSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 12)
)
acDs1ExceededThresholdNEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalPCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 13)
)
acDs1ExceededThresholdNEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalLESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 14)
)
acDs1ExceededThresholdNEIntervalBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalBESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 15)
)
acDs1ExceededThresholdNEIntervalDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalDMsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEIntervalLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 16)
)
acDs1ExceededThresholdNEIntervalLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEIntervalLCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 17)
)
acDs1ExceededThresholdNEDayESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDaySESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 18)
)
acDs1ExceededThresholdNEDaySESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDaySESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDaySEFSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 19)
)
acDs1ExceededThresholdNEDaySEFSTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDaySEFSTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 20)
)
acDs1ExceededThresholdNEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayUASsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 21)
)
acDs1ExceededThresholdNEDayCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayCSSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 22)
)
acDs1ExceededThresholdNEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayPCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 23)
)
acDs1ExceededThresholdNEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayLESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 24)
)
acDs1ExceededThresholdNEDayBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayBESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 25)
)
acDs1ExceededThresholdNEDayDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayDMsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdNEDayLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 26)
)
acDs1ExceededThresholdNEDayLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdNEDayLCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 27)
)
acDs1ExceededThresholdFEIntervalESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 28)
)
acDs1ExceededThresholdFEIntervalSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalSESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 29)
)
acDs1ExceededThresholdFEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalSEFSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 30)
)
acDs1ExceededThresholdFEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalUASsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 31)
)
acDs1ExceededThresholdFEIntervalCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalCSSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 32)
)
acDs1ExceededThresholdFEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalLESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 33)
)
acDs1ExceededThresholdFEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalPCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 34)
)
acDs1ExceededThresholdFEIntervalBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalBESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEIntervalDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 35)
)
acDs1ExceededThresholdFEIntervalDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEIntervalDMsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 36)
)
acDs1ExceededThresholdFEDayESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDaySESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 37)
)
acDs1ExceededThresholdFEDaySESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDaySESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDaySEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 38)
)
acDs1ExceededThresholdFEDaySEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDaySEFSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 39)
)
acDs1ExceededThresholdFEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayUASsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 40)
)
acDs1ExceededThresholdFEDayCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayCSSsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 41)
)
acDs1ExceededThresholdFEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayLESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 42)
)
acDs1ExceededThresholdFEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayPCVsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 43)
)
acDs1ExceededThresholdFEDayBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayBESsTrap.setStatus(
        "current"
    )

acDs1ExceededThresholdFEDayDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 4, 0, 44)
)
acDs1ExceededThresholdFEDayDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdNodeId"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdSlot"),
        ("APPIAN-PPORT-DS1-MIB", "acDs1ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs1ExceededThresholdFEDayDMsTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-DS1-MIB",
    **{"acDs1": acDs1,
       "acDs1Traps": acDs1Traps,
       "acDs1LineStatusChangeTrap": acDs1LineStatusChangeTrap,
       "acDs1StatsResetTrap": acDs1StatsResetTrap,
       "acDs1CfgErrorTrap": acDs1CfgErrorTrap,
       "acDs1LinkDownTrap": acDs1LinkDownTrap,
       "acDs1LinkUpTrap": acDs1LinkUpTrap,
       "acDs1ExceededThresholdNEIntervalESsTrap": acDs1ExceededThresholdNEIntervalESsTrap,
       "acDs1ExceededThresholdNEIntervalSESsTrap": acDs1ExceededThresholdNEIntervalSESsTrap,
       "acDs1ExceededThresholdNEIntervalSEFSsTrap": acDs1ExceededThresholdNEIntervalSEFSsTrap,
       "acDs1ExceededThresholdNEIntervalUASsTrap": acDs1ExceededThresholdNEIntervalUASsTrap,
       "acDs1ExceededThresholdNEIntervalCSSsTrap": acDs1ExceededThresholdNEIntervalCSSsTrap,
       "acDs1ExceededThresholdNEIntervalPCVsTrap": acDs1ExceededThresholdNEIntervalPCVsTrap,
       "acDs1ExceededThresholdNEIntervalLESsTrap": acDs1ExceededThresholdNEIntervalLESsTrap,
       "acDs1ExceededThresholdNEIntervalBESsTrap": acDs1ExceededThresholdNEIntervalBESsTrap,
       "acDs1ExceededThresholdNEIntervalDMsTrap": acDs1ExceededThresholdNEIntervalDMsTrap,
       "acDs1ExceededThresholdNEIntervalLCVsTrap": acDs1ExceededThresholdNEIntervalLCVsTrap,
       "acDs1ExceededThresholdNEDayESsTrap": acDs1ExceededThresholdNEDayESsTrap,
       "acDs1ExceededThresholdNEDaySESsTrap": acDs1ExceededThresholdNEDaySESsTrap,
       "acDs1ExceededThresholdNEDaySEFSTrap": acDs1ExceededThresholdNEDaySEFSTrap,
       "acDs1ExceededThresholdNEDayUASsTrap": acDs1ExceededThresholdNEDayUASsTrap,
       "acDs1ExceededThresholdNEDayCSSsTrap": acDs1ExceededThresholdNEDayCSSsTrap,
       "acDs1ExceededThresholdNEDayPCVsTrap": acDs1ExceededThresholdNEDayPCVsTrap,
       "acDs1ExceededThresholdNEDayLESsTrap": acDs1ExceededThresholdNEDayLESsTrap,
       "acDs1ExceededThresholdNEDayBESsTrap": acDs1ExceededThresholdNEDayBESsTrap,
       "acDs1ExceededThresholdNEDayDMsTrap": acDs1ExceededThresholdNEDayDMsTrap,
       "acDs1ExceededThresholdNEDayLCVsTrap": acDs1ExceededThresholdNEDayLCVsTrap,
       "acDs1ExceededThresholdFEIntervalESsTrap": acDs1ExceededThresholdFEIntervalESsTrap,
       "acDs1ExceededThresholdFEIntervalSESsTrap": acDs1ExceededThresholdFEIntervalSESsTrap,
       "acDs1ExceededThresholdFEIntervalSEFSsTrap": acDs1ExceededThresholdFEIntervalSEFSsTrap,
       "acDs1ExceededThresholdFEIntervalUASsTrap": acDs1ExceededThresholdFEIntervalUASsTrap,
       "acDs1ExceededThresholdFEIntervalCSSsTrap": acDs1ExceededThresholdFEIntervalCSSsTrap,
       "acDs1ExceededThresholdFEIntervalLESsTrap": acDs1ExceededThresholdFEIntervalLESsTrap,
       "acDs1ExceededThresholdFEIntervalPCVsTrap": acDs1ExceededThresholdFEIntervalPCVsTrap,
       "acDs1ExceededThresholdFEIntervalBESsTrap": acDs1ExceededThresholdFEIntervalBESsTrap,
       "acDs1ExceededThresholdFEIntervalDMsTrap": acDs1ExceededThresholdFEIntervalDMsTrap,
       "acDs1ExceededThresholdFEDayESsTrap": acDs1ExceededThresholdFEDayESsTrap,
       "acDs1ExceededThresholdFEDaySESsTrap": acDs1ExceededThresholdFEDaySESsTrap,
       "acDs1ExceededThresholdFEDaySEFSsTrap": acDs1ExceededThresholdFEDaySEFSsTrap,
       "acDs1ExceededThresholdFEDayUASsTrap": acDs1ExceededThresholdFEDayUASsTrap,
       "acDs1ExceededThresholdFEDayCSSsTrap": acDs1ExceededThresholdFEDayCSSsTrap,
       "acDs1ExceededThresholdFEDayLESsTrap": acDs1ExceededThresholdFEDayLESsTrap,
       "acDs1ExceededThresholdFEDayPCVsTrap": acDs1ExceededThresholdFEDayPCVsTrap,
       "acDs1ExceededThresholdFEDayBESsTrap": acDs1ExceededThresholdFEDayBESsTrap,
       "acDs1ExceededThresholdFEDayDMsTrap": acDs1ExceededThresholdFEDayDMsTrap,
       "acDs1ConfigTable": acDs1ConfigTable,
       "acDs1ConfigEntry": acDs1ConfigEntry,
       "acDs1ConfigNodeId": acDs1ConfigNodeId,
       "acDs1ConfigSlot": acDs1ConfigSlot,
       "acDs1ConfigPort": acDs1ConfigPort,
       "acDs1ConfigAdminStatus": acDs1ConfigAdminStatus,
       "acDs1ConfigOpStatus": acDs1ConfigOpStatus,
       "acDs1ConfigTimeElapsedInterval": acDs1ConfigTimeElapsedInterval,
       "acDs1ConfigValidIntervals": acDs1ConfigValidIntervals,
       "acDs1ConfigTimeElapsedDay": acDs1ConfigTimeElapsedDay,
       "acDs1ConfigValidDays": acDs1ConfigValidDays,
       "acDs1ConfigTimeElapsedFarEndInterval": acDs1ConfigTimeElapsedFarEndInterval,
       "acDs1ConfigValidFarEndIntervals": acDs1ConfigValidFarEndIntervals,
       "acDs1ConfigTimeElapsedFarEndDay": acDs1ConfigTimeElapsedFarEndDay,
       "acDs1ConfigValidFarEndDays": acDs1ConfigValidFarEndDays,
       "acDs1ConfigLineType": acDs1ConfigLineType,
       "acDs1ConfigLineCoding": acDs1ConfigLineCoding,
       "acDs1ConfigCircuitIdentifier": acDs1ConfigCircuitIdentifier,
       "acDs1ConfigLoopbackConfig": acDs1ConfigLoopbackConfig,
       "acDs1ConfigLineStatus": acDs1ConfigLineStatus,
       "acDs1ConfigSignalMode": acDs1ConfigSignalMode,
       "acDs1ConfigTransmitClockSource": acDs1ConfigTransmitClockSource,
       "acDs1ConfigFdl": acDs1ConfigFdl,
       "acDs1ConfigInvalidIntervals": acDs1ConfigInvalidIntervals,
       "acDs1ConfigInvalidDays": acDs1ConfigInvalidDays,
       "acDs1ConfigInvalidFarEndIntervals": acDs1ConfigInvalidFarEndIntervals,
       "acDs1ConfigInvalidFarEndDays": acDs1ConfigInvalidFarEndDays,
       "acDs1ConfigLineStatusLastChange": acDs1ConfigLineStatusLastChange,
       "acDs1ConfigLineStatusChangeTrapEnable": acDs1ConfigLineStatusChangeTrapEnable,
       "acDs1ConfigLoopbackStatus": acDs1ConfigLoopbackStatus,
       "acDs1ConfigInterfaceName": acDs1ConfigInterfaceName,
       "acDs1ConfigTimeSlotIndex": acDs1ConfigTimeSlotIndex,
       "acDs1IntervalTable": acDs1IntervalTable,
       "acDs1IntervalEntry": acDs1IntervalEntry,
       "acDs1IntervalNodeId": acDs1IntervalNodeId,
       "acDs1IntervalSlot": acDs1IntervalSlot,
       "acDs1IntervalPort": acDs1IntervalPort,
       "acDs1IntervalNumber": acDs1IntervalNumber,
       "acDs1IntervalValidStats": acDs1IntervalValidStats,
       "acDs1IntervalResetStats": acDs1IntervalResetStats,
       "acDs1IntervalESs": acDs1IntervalESs,
       "acDs1IntervalSESs": acDs1IntervalSESs,
       "acDs1IntervalSEFSs": acDs1IntervalSEFSs,
       "acDs1IntervalUASs": acDs1IntervalUASs,
       "acDs1IntervalCSSs": acDs1IntervalCSSs,
       "acDs1IntervalPCVs": acDs1IntervalPCVs,
       "acDs1IntervalLESs": acDs1IntervalLESs,
       "acDs1IntervalBESs": acDs1IntervalBESs,
       "acDs1IntervalDMs": acDs1IntervalDMs,
       "acDs1IntervalLCVs": acDs1IntervalLCVs,
       "acDs1DayTable": acDs1DayTable,
       "acDs1DayEntry": acDs1DayEntry,
       "acDs1DayNodeId": acDs1DayNodeId,
       "acDs1DaySlot": acDs1DaySlot,
       "acDs1DayPort": acDs1DayPort,
       "acDs1DayNumber": acDs1DayNumber,
       "acDs1DayValidStats": acDs1DayValidStats,
       "acDs1DayResetStats": acDs1DayResetStats,
       "acDs1DayESs": acDs1DayESs,
       "acDs1DaySESs": acDs1DaySESs,
       "acDs1DaySEFSs": acDs1DaySEFSs,
       "acDs1DayUASs": acDs1DayUASs,
       "acDs1DayCSSs": acDs1DayCSSs,
       "acDs1DayPCVs": acDs1DayPCVs,
       "acDs1DayLESs": acDs1DayLESs,
       "acDs1DayBESs": acDs1DayBESs,
       "acDs1DayDMs": acDs1DayDMs,
       "acDs1DayLCVs": acDs1DayLCVs,
       "acDs1FarEndIntervalTable": acDs1FarEndIntervalTable,
       "acDs1FarEndIntervalEntry": acDs1FarEndIntervalEntry,
       "acDs1FarEndIntervalNodeId": acDs1FarEndIntervalNodeId,
       "acDs1FarEndIntervalSlot": acDs1FarEndIntervalSlot,
       "acDs1FarEndIntervalPort": acDs1FarEndIntervalPort,
       "acDs1FarEndIntervalNumber": acDs1FarEndIntervalNumber,
       "acDs1FarEndIntervalValidStats": acDs1FarEndIntervalValidStats,
       "acDs1FarEndIntervalResetStats": acDs1FarEndIntervalResetStats,
       "acDs1FarEndIntervalESs": acDs1FarEndIntervalESs,
       "acDs1FarEndIntervalSESs": acDs1FarEndIntervalSESs,
       "acDs1FarEndIntervalSEFSs": acDs1FarEndIntervalSEFSs,
       "acDs1FarEndIntervalUASs": acDs1FarEndIntervalUASs,
       "acDs1FarEndIntervalCSSs": acDs1FarEndIntervalCSSs,
       "acDs1FarEndIntervalLESs": acDs1FarEndIntervalLESs,
       "acDs1FarEndIntervalPCVs": acDs1FarEndIntervalPCVs,
       "acDs1FarEndIntervalBESs": acDs1FarEndIntervalBESs,
       "acDs1FarEndIntervalDMs": acDs1FarEndIntervalDMs,
       "acDs1FarEndDayTable": acDs1FarEndDayTable,
       "acDs1FarEndDayEntry": acDs1FarEndDayEntry,
       "acDs1FarEndDayNodeId": acDs1FarEndDayNodeId,
       "acDs1FarEndDaySlot": acDs1FarEndDaySlot,
       "acDs1FarEndDayPort": acDs1FarEndDayPort,
       "acDs1FarEndDayNumber": acDs1FarEndDayNumber,
       "acDs1FarEndDayValidStats": acDs1FarEndDayValidStats,
       "acDs1FarEndDayResetStats": acDs1FarEndDayResetStats,
       "acDs1FarEndDayESs": acDs1FarEndDayESs,
       "acDs1FarEndDaySESs": acDs1FarEndDaySESs,
       "acDs1FarEndDaySEFSs": acDs1FarEndDaySEFSs,
       "acDs1FarEndDayUASs": acDs1FarEndDayUASs,
       "acDs1FarEndDayCSSs": acDs1FarEndDayCSSs,
       "acDs1FarEndDayLESs": acDs1FarEndDayLESs,
       "acDs1FarEndDayPCVs": acDs1FarEndDayPCVs,
       "acDs1FarEndDayBESs": acDs1FarEndDayBESs,
       "acDs1FarEndDayDMs": acDs1FarEndDayDMs,
       "acDs1ThresholdTable": acDs1ThresholdTable,
       "acDs1ThresholdEntry": acDs1ThresholdEntry,
       "acDs1ThresholdNodeId": acDs1ThresholdNodeId,
       "acDs1ThresholdSlot": acDs1ThresholdSlot,
       "acDs1ThresholdPort": acDs1ThresholdPort,
       "acDs1ThresholdNEIntervalESs": acDs1ThresholdNEIntervalESs,
       "acDs1ThresholdNEIntervalSESs": acDs1ThresholdNEIntervalSESs,
       "acDs1ThresholdNEIntervalSEFSs": acDs1ThresholdNEIntervalSEFSs,
       "acDs1ThresholdNEIntervalUASs": acDs1ThresholdNEIntervalUASs,
       "acDs1ThresholdNEIntervalCSSs": acDs1ThresholdNEIntervalCSSs,
       "acDs1ThresholdNEIntervalPCVs": acDs1ThresholdNEIntervalPCVs,
       "acDs1ThresholdNEIntervalLESs": acDs1ThresholdNEIntervalLESs,
       "acDs1ThresholdNEIntervalBESs": acDs1ThresholdNEIntervalBESs,
       "acDs1ThresholdNEIntervalDMs": acDs1ThresholdNEIntervalDMs,
       "acDs1ThresholdNEIntervalLCVs": acDs1ThresholdNEIntervalLCVs,
       "acDs1ThresholdNEDayESs": acDs1ThresholdNEDayESs,
       "acDs1ThresholdNEDaySESs": acDs1ThresholdNEDaySESs,
       "acDs1ThresholdNEDaySEFSs": acDs1ThresholdNEDaySEFSs,
       "acDs1ThresholdNEDayUASs": acDs1ThresholdNEDayUASs,
       "acDs1ThresholdNEDayCSSs": acDs1ThresholdNEDayCSSs,
       "acDs1ThresholdNEDayPCVs": acDs1ThresholdNEDayPCVs,
       "acDs1ThresholdNEDayLESs": acDs1ThresholdNEDayLESs,
       "acDs1ThresholdNEDayBESs": acDs1ThresholdNEDayBESs,
       "acDs1ThresholdNEDayDMs": acDs1ThresholdNEDayDMs,
       "acDs1ThresholdNEDayLCVs": acDs1ThresholdNEDayLCVs,
       "acDs1ThresholdFEIntervalESs": acDs1ThresholdFEIntervalESs,
       "acDs1ThresholdFEIntervalSESs": acDs1ThresholdFEIntervalSESs,
       "acDs1ThresholdFEIntervalSEFSs": acDs1ThresholdFEIntervalSEFSs,
       "acDs1ThresholdFEIntervalUASs": acDs1ThresholdFEIntervalUASs,
       "acDs1ThresholdFEIntervalCSSs": acDs1ThresholdFEIntervalCSSs,
       "acDs1ThresholdFEIntervalLESs": acDs1ThresholdFEIntervalLESs,
       "acDs1ThresholdFEIntervalPCVs": acDs1ThresholdFEIntervalPCVs,
       "acDs1ThresholdFEIntervalBESs": acDs1ThresholdFEIntervalBESs,
       "acDs1ThresholdFEIntervalDMs": acDs1ThresholdFEIntervalDMs,
       "acDs1ThresholdFEDayESs": acDs1ThresholdFEDayESs,
       "acDs1ThresholdFEDaySESs": acDs1ThresholdFEDaySESs,
       "acDs1ThresholdFEDaySEFSs": acDs1ThresholdFEDaySEFSs,
       "acDs1ThresholdFEDayUASs": acDs1ThresholdFEDayUASs,
       "acDs1ThresholdFEDayCSSs": acDs1ThresholdFEDayCSSs,
       "acDs1ThresholdFEDayLESs": acDs1ThresholdFEDayLESs,
       "acDs1ThresholdFEDayPCVs": acDs1ThresholdFEDayPCVs,
       "acDs1ThresholdFEDayBESs": acDs1ThresholdFEDayBESs,
       "acDs1ThresholdFEDayDMs": acDs1ThresholdFEDayDMs}
)
