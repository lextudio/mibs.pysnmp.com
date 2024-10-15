# SNMP MIB module (APPIAN-LPORT-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-LPORT-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:32 2024
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

acLogicalDs1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcLogicalDs1Traps_ObjectIdentity = ObjectIdentity
acLogicalDs1Traps = _AcLogicalDs1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0)
)
_AcLogicalDs1ConfigTable_Object = MibTable
acLogicalDs1ConfigTable = _AcLogicalDs1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTable.setStatus("current")
_AcLogicalDs1ConfigEntry_Object = MibTableRow
acLogicalDs1ConfigEntry = _AcLogicalDs1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1)
)
acLogicalDs1ConfigEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"),
)
if mibBuilder.loadTexts:
    acLogicalDs1ConfigEntry.setStatus("current")
_AcLogicalDs1ConfigNodeId_Type = AcNodeId
_AcLogicalDs1ConfigNodeId_Object = MibTableColumn
acLogicalDs1ConfigNodeId = _AcLogicalDs1ConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 1),
    _AcLogicalDs1ConfigNodeId_Type()
)
acLogicalDs1ConfigNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigNodeId.setStatus("current")
_AcLogicalDs1ConfigIndex_Type = Integer32
_AcLogicalDs1ConfigIndex_Object = MibTableColumn
acLogicalDs1ConfigIndex = _AcLogicalDs1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 2),
    _AcLogicalDs1ConfigIndex_Type()
)
acLogicalDs1ConfigIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigIndex.setStatus("current")


class _AcLogicalDs1ConfigAdminStatus_Type(AcAdminStatus):
    """Custom type acLogicalDs1ConfigAdminStatus based on AcAdminStatus"""


_AcLogicalDs1ConfigAdminStatus_Object = MibTableColumn
acLogicalDs1ConfigAdminStatus = _AcLogicalDs1ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 3),
    _AcLogicalDs1ConfigAdminStatus_Type()
)
acLogicalDs1ConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigAdminStatus.setStatus("current")


class _AcLogicalDs1ConfigTimeElapsedInterval_Type(Integer32):
    """Custom type acLogicalDs1ConfigTimeElapsedInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcLogicalDs1ConfigTimeElapsedInterval_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigTimeElapsedInterval_Object = MibTableColumn
acLogicalDs1ConfigTimeElapsedInterval = _AcLogicalDs1ConfigTimeElapsedInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 4),
    _AcLogicalDs1ConfigTimeElapsedInterval_Type()
)
acLogicalDs1ConfigTimeElapsedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTimeElapsedInterval.setStatus("current")


class _AcLogicalDs1ConfigValidIntervals_Type(Integer32):
    """Custom type acLogicalDs1ConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs1ConfigValidIntervals_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigValidIntervals_Object = MibTableColumn
acLogicalDs1ConfigValidIntervals = _AcLogicalDs1ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 5),
    _AcLogicalDs1ConfigValidIntervals_Type()
)
acLogicalDs1ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigValidIntervals.setStatus("current")


class _AcLogicalDs1ConfigTimeElapsedDay_Type(Integer32):
    """Custom type acLogicalDs1ConfigTimeElapsedDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcLogicalDs1ConfigTimeElapsedDay_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigTimeElapsedDay_Object = MibTableColumn
acLogicalDs1ConfigTimeElapsedDay = _AcLogicalDs1ConfigTimeElapsedDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 6),
    _AcLogicalDs1ConfigTimeElapsedDay_Type()
)
acLogicalDs1ConfigTimeElapsedDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTimeElapsedDay.setStatus("current")


class _AcLogicalDs1ConfigValidDays_Type(Integer32):
    """Custom type acLogicalDs1ConfigValidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs1ConfigValidDays_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigValidDays_Object = MibTableColumn
acLogicalDs1ConfigValidDays = _AcLogicalDs1ConfigValidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 7),
    _AcLogicalDs1ConfigValidDays_Type()
)
acLogicalDs1ConfigValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigValidDays.setStatus("current")


class _AcLogicalDs1ConfigTimeElapsedFarEndInterval_Type(Integer32):
    """Custom type acLogicalDs1ConfigTimeElapsedFarEndInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcLogicalDs1ConfigTimeElapsedFarEndInterval_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigTimeElapsedFarEndInterval_Object = MibTableColumn
acLogicalDs1ConfigTimeElapsedFarEndInterval = _AcLogicalDs1ConfigTimeElapsedFarEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 8),
    _AcLogicalDs1ConfigTimeElapsedFarEndInterval_Type()
)
acLogicalDs1ConfigTimeElapsedFarEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTimeElapsedFarEndInterval.setStatus("current")


class _AcLogicalDs1ConfigValidFarEndIntervals_Type(Integer32):
    """Custom type acLogicalDs1ConfigValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs1ConfigValidFarEndIntervals_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigValidFarEndIntervals_Object = MibTableColumn
acLogicalDs1ConfigValidFarEndIntervals = _AcLogicalDs1ConfigValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 9),
    _AcLogicalDs1ConfigValidFarEndIntervals_Type()
)
acLogicalDs1ConfigValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigValidFarEndIntervals.setStatus("current")


class _AcLogicalDs1ConfigTimeElapsedFarEndDay_Type(Integer32):
    """Custom type acLogicalDs1ConfigTimeElapsedFarEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcLogicalDs1ConfigTimeElapsedFarEndDay_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigTimeElapsedFarEndDay_Object = MibTableColumn
acLogicalDs1ConfigTimeElapsedFarEndDay = _AcLogicalDs1ConfigTimeElapsedFarEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 10),
    _AcLogicalDs1ConfigTimeElapsedFarEndDay_Type()
)
acLogicalDs1ConfigTimeElapsedFarEndDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTimeElapsedFarEndDay.setStatus("current")


class _AcLogicalDs1ConfigValidFarEndDays_Type(Integer32):
    """Custom type acLogicalDs1ConfigValidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs1ConfigValidFarEndDays_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigValidFarEndDays_Object = MibTableColumn
acLogicalDs1ConfigValidFarEndDays = _AcLogicalDs1ConfigValidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 11),
    _AcLogicalDs1ConfigValidFarEndDays_Type()
)
acLogicalDs1ConfigValidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigValidFarEndDays.setStatus("current")


class _AcLogicalDs1ConfigSendCode_Type(Integer32):
    """Custom type acLogicalDs1ConfigSendCode based on Integer32"""
    defaultValue = 1

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
        *(("ds1Send3in24Pattern", 7),
          ("ds1Send511Pattern", 6),
          ("ds1SendLineCode", 2),
          ("ds1SendNoCode", 1),
          ("ds1SendOtherTestPattern", 8),
          ("ds1SendPayloadCode", 3),
          ("ds1SendQRS", 5),
          ("ds1SendResetCode", 4))
    )


_AcLogicalDs1ConfigSendCode_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigSendCode_Object = MibTableColumn
acLogicalDs1ConfigSendCode = _AcLogicalDs1ConfigSendCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 12),
    _AcLogicalDs1ConfigSendCode_Type()
)
acLogicalDs1ConfigSendCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigSendCode.setStatus("current")


class _AcLogicalDs1ConfigCircuitIdentifier_Type(DisplayString):
    """Custom type acLogicalDs1ConfigCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcLogicalDs1ConfigCircuitIdentifier_Type.__name__ = "DisplayString"
_AcLogicalDs1ConfigCircuitIdentifier_Object = MibTableColumn
acLogicalDs1ConfigCircuitIdentifier = _AcLogicalDs1ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 13),
    _AcLogicalDs1ConfigCircuitIdentifier_Type()
)
acLogicalDs1ConfigCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigCircuitIdentifier.setStatus("current")


class _AcLogicalDs1ConfigLoopbackConfig_Type(Integer32):
    """Custom type acLogicalDs1ConfigLoopbackConfig based on Integer32"""
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
        *(("ds1DualLoop", 6),
          ("ds1InwardLoop", 5),
          ("ds1LineLoop", 3),
          ("ds1NoLoop", 1),
          ("ds1OtherLoop", 4),
          ("ds1PayloadLoop", 2))
    )


_AcLogicalDs1ConfigLoopbackConfig_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigLoopbackConfig_Object = MibTableColumn
acLogicalDs1ConfigLoopbackConfig = _AcLogicalDs1ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 14),
    _AcLogicalDs1ConfigLoopbackConfig_Type()
)
acLogicalDs1ConfigLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigLoopbackConfig.setStatus("current")


class _AcLogicalDs1ConfigLineStatus_Type(Integer32):
    """Custom type acLogicalDs1ConfigLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131071),
    )


_AcLogicalDs1ConfigLineStatus_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigLineStatus_Object = MibTableColumn
acLogicalDs1ConfigLineStatus = _AcLogicalDs1ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 15),
    _AcLogicalDs1ConfigLineStatus_Type()
)
acLogicalDs1ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigLineStatus.setStatus("current")


class _AcLogicalDs1ConfigTransmitClockSource_Type(Integer32):
    """Custom type acLogicalDs1ConfigTransmitClockSource based on Integer32"""
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


_AcLogicalDs1ConfigTransmitClockSource_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigTransmitClockSource_Object = MibTableColumn
acLogicalDs1ConfigTransmitClockSource = _AcLogicalDs1ConfigTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 16),
    _AcLogicalDs1ConfigTransmitClockSource_Type()
)
acLogicalDs1ConfigTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigTransmitClockSource.setStatus("current")


class _AcLogicalDs1ConfigInvalidIntervals_Type(Integer32):
    """Custom type acLogicalDs1ConfigInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs1ConfigInvalidIntervals_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigInvalidIntervals_Object = MibTableColumn
acLogicalDs1ConfigInvalidIntervals = _AcLogicalDs1ConfigInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 17),
    _AcLogicalDs1ConfigInvalidIntervals_Type()
)
acLogicalDs1ConfigInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigInvalidIntervals.setStatus("current")


class _AcLogicalDs1ConfigInvalidDays_Type(Integer32):
    """Custom type acLogicalDs1ConfigInvalidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs1ConfigInvalidDays_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigInvalidDays_Object = MibTableColumn
acLogicalDs1ConfigInvalidDays = _AcLogicalDs1ConfigInvalidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 18),
    _AcLogicalDs1ConfigInvalidDays_Type()
)
acLogicalDs1ConfigInvalidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigInvalidDays.setStatus("current")


class _AcLogicalDs1ConfigInvalidFarEndIntervals_Type(Integer32):
    """Custom type acLogicalDs1ConfigInvalidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcLogicalDs1ConfigInvalidFarEndIntervals_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigInvalidFarEndIntervals_Object = MibTableColumn
acLogicalDs1ConfigInvalidFarEndIntervals = _AcLogicalDs1ConfigInvalidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 19),
    _AcLogicalDs1ConfigInvalidFarEndIntervals_Type()
)
acLogicalDs1ConfigInvalidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigInvalidFarEndIntervals.setStatus("current")


class _AcLogicalDs1ConfigInvalidFarEndDays_Type(Integer32):
    """Custom type acLogicalDs1ConfigInvalidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcLogicalDs1ConfigInvalidFarEndDays_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigInvalidFarEndDays_Object = MibTableColumn
acLogicalDs1ConfigInvalidFarEndDays = _AcLogicalDs1ConfigInvalidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 20),
    _AcLogicalDs1ConfigInvalidFarEndDays_Type()
)
acLogicalDs1ConfigInvalidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigInvalidFarEndDays.setStatus("current")
_AcLogicalDs1ConfigLineStatusLastChange_Type = TimeStamp
_AcLogicalDs1ConfigLineStatusLastChange_Object = MibTableColumn
acLogicalDs1ConfigLineStatusLastChange = _AcLogicalDs1ConfigLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 21),
    _AcLogicalDs1ConfigLineStatusLastChange_Type()
)
acLogicalDs1ConfigLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigLineStatusLastChange.setStatus("current")


class _AcLogicalDs1ConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type acLogicalDs1ConfigLineStatusChangeTrapEnable based on Integer32"""
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


_AcLogicalDs1ConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigLineStatusChangeTrapEnable_Object = MibTableColumn
acLogicalDs1ConfigLineStatusChangeTrapEnable = _AcLogicalDs1ConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 22),
    _AcLogicalDs1ConfigLineStatusChangeTrapEnable_Type()
)
acLogicalDs1ConfigLineStatusChangeTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigLineStatusChangeTrapEnable.setStatus("current")


class _AcLogicalDs1ConfigLoopbackStatus_Type(Integer32):
    """Custom type acLogicalDs1ConfigLoopbackStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AcLogicalDs1ConfigLoopbackStatus_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigLoopbackStatus_Object = MibTableColumn
acLogicalDs1ConfigLoopbackStatus = _AcLogicalDs1ConfigLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 23),
    _AcLogicalDs1ConfigLoopbackStatus_Type()
)
acLogicalDs1ConfigLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigLoopbackStatus.setStatus("current")


class _AcLogicalDs1ConfigVTNumber_Type(Integer32):
    """Custom type acLogicalDs1ConfigVTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_AcLogicalDs1ConfigVTNumber_Type.__name__ = "Integer32"
_AcLogicalDs1ConfigVTNumber_Object = MibTableColumn
acLogicalDs1ConfigVTNumber = _AcLogicalDs1ConfigVTNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 1, 1, 24),
    _AcLogicalDs1ConfigVTNumber_Type()
)
acLogicalDs1ConfigVTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1ConfigVTNumber.setStatus("current")
_AcLogicalDs1IntervalTable_Object = MibTable
acLogicalDs1IntervalTable = _AcLogicalDs1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    acLogicalDs1IntervalTable.setStatus("current")
_AcLogicalDs1IntervalEntry_Object = MibTableRow
acLogicalDs1IntervalEntry = _AcLogicalDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1)
)
acLogicalDs1IntervalEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1IntervalNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1IntervalIndex"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1IntervalNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs1IntervalEntry.setStatus("current")
_AcLogicalDs1IntervalNodeId_Type = AcNodeId
_AcLogicalDs1IntervalNodeId_Object = MibTableColumn
acLogicalDs1IntervalNodeId = _AcLogicalDs1IntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 1),
    _AcLogicalDs1IntervalNodeId_Type()
)
acLogicalDs1IntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalNodeId.setStatus("current")
_AcLogicalDs1IntervalIndex_Type = Integer32
_AcLogicalDs1IntervalIndex_Object = MibTableColumn
acLogicalDs1IntervalIndex = _AcLogicalDs1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 2),
    _AcLogicalDs1IntervalIndex_Type()
)
acLogicalDs1IntervalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalIndex.setStatus("current")


class _AcLogicalDs1IntervalNumber_Type(Integer32):
    """Custom type acLogicalDs1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcLogicalDs1IntervalNumber_Type.__name__ = "Integer32"
_AcLogicalDs1IntervalNumber_Object = MibTableColumn
acLogicalDs1IntervalNumber = _AcLogicalDs1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 3),
    _AcLogicalDs1IntervalNumber_Type()
)
acLogicalDs1IntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalNumber.setStatus("current")
_AcLogicalDs1IntervalValidStats_Type = TruthValue
_AcLogicalDs1IntervalValidStats_Object = MibTableColumn
acLogicalDs1IntervalValidStats = _AcLogicalDs1IntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 4),
    _AcLogicalDs1IntervalValidStats_Type()
)
acLogicalDs1IntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalValidStats.setStatus("current")
_AcLogicalDs1IntervalResetStats_Type = TruthValue
_AcLogicalDs1IntervalResetStats_Object = MibTableColumn
acLogicalDs1IntervalResetStats = _AcLogicalDs1IntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 5),
    _AcLogicalDs1IntervalResetStats_Type()
)
acLogicalDs1IntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalResetStats.setStatus("current")
_AcLogicalDs1IntervalESs_Type = PerfIntervalCount
_AcLogicalDs1IntervalESs_Object = MibTableColumn
acLogicalDs1IntervalESs = _AcLogicalDs1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 6),
    _AcLogicalDs1IntervalESs_Type()
)
acLogicalDs1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalESs.setStatus("current")
_AcLogicalDs1IntervalSESs_Type = PerfIntervalCount
_AcLogicalDs1IntervalSESs_Object = MibTableColumn
acLogicalDs1IntervalSESs = _AcLogicalDs1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 7),
    _AcLogicalDs1IntervalSESs_Type()
)
acLogicalDs1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalSESs.setStatus("current")
_AcLogicalDs1IntervalSEFSs_Type = PerfIntervalCount
_AcLogicalDs1IntervalSEFSs_Object = MibTableColumn
acLogicalDs1IntervalSEFSs = _AcLogicalDs1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 8),
    _AcLogicalDs1IntervalSEFSs_Type()
)
acLogicalDs1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalSEFSs.setStatus("current")
_AcLogicalDs1IntervalUASs_Type = PerfIntervalCount
_AcLogicalDs1IntervalUASs_Object = MibTableColumn
acLogicalDs1IntervalUASs = _AcLogicalDs1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 9),
    _AcLogicalDs1IntervalUASs_Type()
)
acLogicalDs1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalUASs.setStatus("current")
_AcLogicalDs1IntervalCSSs_Type = PerfIntervalCount
_AcLogicalDs1IntervalCSSs_Object = MibTableColumn
acLogicalDs1IntervalCSSs = _AcLogicalDs1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 10),
    _AcLogicalDs1IntervalCSSs_Type()
)
acLogicalDs1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalCSSs.setStatus("current")
_AcLogicalDs1IntervalPCVs_Type = PerfIntervalCount
_AcLogicalDs1IntervalPCVs_Object = MibTableColumn
acLogicalDs1IntervalPCVs = _AcLogicalDs1IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 11),
    _AcLogicalDs1IntervalPCVs_Type()
)
acLogicalDs1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalPCVs.setStatus("current")
_AcLogicalDs1IntervalLESs_Type = PerfIntervalCount
_AcLogicalDs1IntervalLESs_Object = MibTableColumn
acLogicalDs1IntervalLESs = _AcLogicalDs1IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 12),
    _AcLogicalDs1IntervalLESs_Type()
)
acLogicalDs1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalLESs.setStatus("current")
_AcLogicalDs1IntervalBESs_Type = PerfIntervalCount
_AcLogicalDs1IntervalBESs_Object = MibTableColumn
acLogicalDs1IntervalBESs = _AcLogicalDs1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 13),
    _AcLogicalDs1IntervalBESs_Type()
)
acLogicalDs1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalBESs.setStatus("current")
_AcLogicalDs1IntervalDMs_Type = PerfIntervalCount
_AcLogicalDs1IntervalDMs_Object = MibTableColumn
acLogicalDs1IntervalDMs = _AcLogicalDs1IntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 14),
    _AcLogicalDs1IntervalDMs_Type()
)
acLogicalDs1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalDMs.setStatus("current")
_AcLogicalDs1IntervalLCVs_Type = PerfIntervalCount
_AcLogicalDs1IntervalLCVs_Object = MibTableColumn
acLogicalDs1IntervalLCVs = _AcLogicalDs1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 2, 1, 15),
    _AcLogicalDs1IntervalLCVs_Type()
)
acLogicalDs1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1IntervalLCVs.setStatus("current")
_AcLogicalDs1DayTable_Object = MibTable
acLogicalDs1DayTable = _AcLogicalDs1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    acLogicalDs1DayTable.setStatus("current")
_AcLogicalDs1DayEntry_Object = MibTableRow
acLogicalDs1DayEntry = _AcLogicalDs1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1)
)
acLogicalDs1DayEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1DayNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1DayIndex"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1DayNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs1DayEntry.setStatus("current")
_AcLogicalDs1DayNodeId_Type = AcNodeId
_AcLogicalDs1DayNodeId_Object = MibTableColumn
acLogicalDs1DayNodeId = _AcLogicalDs1DayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 1),
    _AcLogicalDs1DayNodeId_Type()
)
acLogicalDs1DayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1DayNodeId.setStatus("current")
_AcLogicalDs1DayIndex_Type = Integer32
_AcLogicalDs1DayIndex_Object = MibTableColumn
acLogicalDs1DayIndex = _AcLogicalDs1DayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 2),
    _AcLogicalDs1DayIndex_Type()
)
acLogicalDs1DayIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1DayIndex.setStatus("current")


class _AcLogicalDs1DayNumber_Type(Integer32):
    """Custom type acLogicalDs1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcLogicalDs1DayNumber_Type.__name__ = "Integer32"
_AcLogicalDs1DayNumber_Object = MibTableColumn
acLogicalDs1DayNumber = _AcLogicalDs1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 3),
    _AcLogicalDs1DayNumber_Type()
)
acLogicalDs1DayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1DayNumber.setStatus("current")
_AcLogicalDs1DayValidStats_Type = TruthValue
_AcLogicalDs1DayValidStats_Object = MibTableColumn
acLogicalDs1DayValidStats = _AcLogicalDs1DayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 4),
    _AcLogicalDs1DayValidStats_Type()
)
acLogicalDs1DayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayValidStats.setStatus("current")
_AcLogicalDs1DayResetStats_Type = TruthValue
_AcLogicalDs1DayResetStats_Object = MibTableColumn
acLogicalDs1DayResetStats = _AcLogicalDs1DayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 5),
    _AcLogicalDs1DayResetStats_Type()
)
acLogicalDs1DayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1DayResetStats.setStatus("current")
_AcLogicalDs1DayESs_Type = PerfIntervalCount
_AcLogicalDs1DayESs_Object = MibTableColumn
acLogicalDs1DayESs = _AcLogicalDs1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 6),
    _AcLogicalDs1DayESs_Type()
)
acLogicalDs1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayESs.setStatus("current")
_AcLogicalDs1DaySESs_Type = PerfIntervalCount
_AcLogicalDs1DaySESs_Object = MibTableColumn
acLogicalDs1DaySESs = _AcLogicalDs1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 7),
    _AcLogicalDs1DaySESs_Type()
)
acLogicalDs1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DaySESs.setStatus("current")
_AcLogicalDs1DaySEFSs_Type = PerfIntervalCount
_AcLogicalDs1DaySEFSs_Object = MibTableColumn
acLogicalDs1DaySEFSs = _AcLogicalDs1DaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 8),
    _AcLogicalDs1DaySEFSs_Type()
)
acLogicalDs1DaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DaySEFSs.setStatus("current")
_AcLogicalDs1DayUASs_Type = PerfIntervalCount
_AcLogicalDs1DayUASs_Object = MibTableColumn
acLogicalDs1DayUASs = _AcLogicalDs1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 9),
    _AcLogicalDs1DayUASs_Type()
)
acLogicalDs1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayUASs.setStatus("current")
_AcLogicalDs1DayCSSs_Type = PerfIntervalCount
_AcLogicalDs1DayCSSs_Object = MibTableColumn
acLogicalDs1DayCSSs = _AcLogicalDs1DayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 10),
    _AcLogicalDs1DayCSSs_Type()
)
acLogicalDs1DayCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayCSSs.setStatus("current")
_AcLogicalDs1DayPCVs_Type = PerfIntervalCount
_AcLogicalDs1DayPCVs_Object = MibTableColumn
acLogicalDs1DayPCVs = _AcLogicalDs1DayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 11),
    _AcLogicalDs1DayPCVs_Type()
)
acLogicalDs1DayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayPCVs.setStatus("current")
_AcLogicalDs1DayLESs_Type = PerfIntervalCount
_AcLogicalDs1DayLESs_Object = MibTableColumn
acLogicalDs1DayLESs = _AcLogicalDs1DayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 12),
    _AcLogicalDs1DayLESs_Type()
)
acLogicalDs1DayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayLESs.setStatus("current")
_AcLogicalDs1DayBESs_Type = PerfIntervalCount
_AcLogicalDs1DayBESs_Object = MibTableColumn
acLogicalDs1DayBESs = _AcLogicalDs1DayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 13),
    _AcLogicalDs1DayBESs_Type()
)
acLogicalDs1DayBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayBESs.setStatus("current")
_AcLogicalDs1DayDMs_Type = PerfIntervalCount
_AcLogicalDs1DayDMs_Object = MibTableColumn
acLogicalDs1DayDMs = _AcLogicalDs1DayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 14),
    _AcLogicalDs1DayDMs_Type()
)
acLogicalDs1DayDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayDMs.setStatus("current")
_AcLogicalDs1DayLCVs_Type = PerfIntervalCount
_AcLogicalDs1DayLCVs_Object = MibTableColumn
acLogicalDs1DayLCVs = _AcLogicalDs1DayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 3, 1, 15),
    _AcLogicalDs1DayLCVs_Type()
)
acLogicalDs1DayLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1DayLCVs.setStatus("current")
_AcLogicalDs1FarEndIntervalTable_Object = MibTable
acLogicalDs1FarEndIntervalTable = _AcLogicalDs1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalTable.setStatus("current")
_AcLogicalDs1FarEndIntervalEntry_Object = MibTableRow
acLogicalDs1FarEndIntervalEntry = _AcLogicalDs1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1)
)
acLogicalDs1FarEndIntervalEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndIntervalNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndIntervalIndex"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalEntry.setStatus("current")
_AcLogicalDs1FarEndIntervalNodeId_Type = AcNodeId
_AcLogicalDs1FarEndIntervalNodeId_Object = MibTableColumn
acLogicalDs1FarEndIntervalNodeId = _AcLogicalDs1FarEndIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 1),
    _AcLogicalDs1FarEndIntervalNodeId_Type()
)
acLogicalDs1FarEndIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalNodeId.setStatus("current")
_AcLogicalDs1FarEndIntervalIndex_Type = Integer32
_AcLogicalDs1FarEndIntervalIndex_Object = MibTableColumn
acLogicalDs1FarEndIntervalIndex = _AcLogicalDs1FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 2),
    _AcLogicalDs1FarEndIntervalIndex_Type()
)
acLogicalDs1FarEndIntervalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalIndex.setStatus("current")


class _AcLogicalDs1FarEndIntervalNumber_Type(Integer32):
    """Custom type acLogicalDs1FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcLogicalDs1FarEndIntervalNumber_Type.__name__ = "Integer32"
_AcLogicalDs1FarEndIntervalNumber_Object = MibTableColumn
acLogicalDs1FarEndIntervalNumber = _AcLogicalDs1FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 3),
    _AcLogicalDs1FarEndIntervalNumber_Type()
)
acLogicalDs1FarEndIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalNumber.setStatus("current")
_AcLogicalDs1FarEndIntervalValidStats_Type = TruthValue
_AcLogicalDs1FarEndIntervalValidStats_Object = MibTableColumn
acLogicalDs1FarEndIntervalValidStats = _AcLogicalDs1FarEndIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 4),
    _AcLogicalDs1FarEndIntervalValidStats_Type()
)
acLogicalDs1FarEndIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalValidStats.setStatus("current")
_AcLogicalDs1FarEndIntervalResetStats_Type = TruthValue
_AcLogicalDs1FarEndIntervalResetStats_Object = MibTableColumn
acLogicalDs1FarEndIntervalResetStats = _AcLogicalDs1FarEndIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 5),
    _AcLogicalDs1FarEndIntervalResetStats_Type()
)
acLogicalDs1FarEndIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalResetStats.setStatus("current")
_AcLogicalDs1FarEndIntervalESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalESs_Object = MibTableColumn
acLogicalDs1FarEndIntervalESs = _AcLogicalDs1FarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 6),
    _AcLogicalDs1FarEndIntervalESs_Type()
)
acLogicalDs1FarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalESs.setStatus("current")
_AcLogicalDs1FarEndIntervalSESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalSESs_Object = MibTableColumn
acLogicalDs1FarEndIntervalSESs = _AcLogicalDs1FarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 7),
    _AcLogicalDs1FarEndIntervalSESs_Type()
)
acLogicalDs1FarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalSESs.setStatus("current")
_AcLogicalDs1FarEndIntervalSEFSs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalSEFSs_Object = MibTableColumn
acLogicalDs1FarEndIntervalSEFSs = _AcLogicalDs1FarEndIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 8),
    _AcLogicalDs1FarEndIntervalSEFSs_Type()
)
acLogicalDs1FarEndIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalSEFSs.setStatus("current")
_AcLogicalDs1FarEndIntervalUASs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalUASs_Object = MibTableColumn
acLogicalDs1FarEndIntervalUASs = _AcLogicalDs1FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 9),
    _AcLogicalDs1FarEndIntervalUASs_Type()
)
acLogicalDs1FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalUASs.setStatus("current")
_AcLogicalDs1FarEndIntervalCSSs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalCSSs_Object = MibTableColumn
acLogicalDs1FarEndIntervalCSSs = _AcLogicalDs1FarEndIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 10),
    _AcLogicalDs1FarEndIntervalCSSs_Type()
)
acLogicalDs1FarEndIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalCSSs.setStatus("current")
_AcLogicalDs1FarEndIntervalLESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalLESs_Object = MibTableColumn
acLogicalDs1FarEndIntervalLESs = _AcLogicalDs1FarEndIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 11),
    _AcLogicalDs1FarEndIntervalLESs_Type()
)
acLogicalDs1FarEndIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalLESs.setStatus("current")
_AcLogicalDs1FarEndIntervalPCVs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalPCVs_Object = MibTableColumn
acLogicalDs1FarEndIntervalPCVs = _AcLogicalDs1FarEndIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 12),
    _AcLogicalDs1FarEndIntervalPCVs_Type()
)
acLogicalDs1FarEndIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalPCVs.setStatus("current")
_AcLogicalDs1FarEndIntervalBESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalBESs_Object = MibTableColumn
acLogicalDs1FarEndIntervalBESs = _AcLogicalDs1FarEndIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 13),
    _AcLogicalDs1FarEndIntervalBESs_Type()
)
acLogicalDs1FarEndIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalBESs.setStatus("current")
_AcLogicalDs1FarEndIntervalDMs_Type = PerfIntervalCount
_AcLogicalDs1FarEndIntervalDMs_Object = MibTableColumn
acLogicalDs1FarEndIntervalDMs = _AcLogicalDs1FarEndIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 4, 1, 14),
    _AcLogicalDs1FarEndIntervalDMs_Type()
)
acLogicalDs1FarEndIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndIntervalDMs.setStatus("current")
_AcLogicalDs1FarEndDayTable_Object = MibTable
acLogicalDs1FarEndDayTable = _AcLogicalDs1FarEndDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayTable.setStatus("current")
_AcLogicalDs1FarEndDayEntry_Object = MibTableRow
acLogicalDs1FarEndDayEntry = _AcLogicalDs1FarEndDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1)
)
acLogicalDs1FarEndDayEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndDayNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndDayIndex"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1FarEndDayNumber"),
)
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayEntry.setStatus("current")
_AcLogicalDs1FarEndDayNodeId_Type = AcNodeId
_AcLogicalDs1FarEndDayNodeId_Object = MibTableColumn
acLogicalDs1FarEndDayNodeId = _AcLogicalDs1FarEndDayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 1),
    _AcLogicalDs1FarEndDayNodeId_Type()
)
acLogicalDs1FarEndDayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayNodeId.setStatus("current")
_AcLogicalDs1FarEndDayIndex_Type = Integer32
_AcLogicalDs1FarEndDayIndex_Object = MibTableColumn
acLogicalDs1FarEndDayIndex = _AcLogicalDs1FarEndDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 2),
    _AcLogicalDs1FarEndDayIndex_Type()
)
acLogicalDs1FarEndDayIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayIndex.setStatus("current")


class _AcLogicalDs1FarEndDayNumber_Type(Integer32):
    """Custom type acLogicalDs1FarEndDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcLogicalDs1FarEndDayNumber_Type.__name__ = "Integer32"
_AcLogicalDs1FarEndDayNumber_Object = MibTableColumn
acLogicalDs1FarEndDayNumber = _AcLogicalDs1FarEndDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 3),
    _AcLogicalDs1FarEndDayNumber_Type()
)
acLogicalDs1FarEndDayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayNumber.setStatus("current")
_AcLogicalDs1FarEndDayValidStats_Type = TruthValue
_AcLogicalDs1FarEndDayValidStats_Object = MibTableColumn
acLogicalDs1FarEndDayValidStats = _AcLogicalDs1FarEndDayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 4),
    _AcLogicalDs1FarEndDayValidStats_Type()
)
acLogicalDs1FarEndDayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayValidStats.setStatus("current")
_AcLogicalDs1FarEndDayResetStats_Type = TruthValue
_AcLogicalDs1FarEndDayResetStats_Object = MibTableColumn
acLogicalDs1FarEndDayResetStats = _AcLogicalDs1FarEndDayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 5),
    _AcLogicalDs1FarEndDayResetStats_Type()
)
acLogicalDs1FarEndDayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayResetStats.setStatus("current")
_AcLogicalDs1FarEndDayESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayESs_Object = MibTableColumn
acLogicalDs1FarEndDayESs = _AcLogicalDs1FarEndDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 6),
    _AcLogicalDs1FarEndDayESs_Type()
)
acLogicalDs1FarEndDayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayESs.setStatus("current")
_AcLogicalDs1FarEndDaySESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDaySESs_Object = MibTableColumn
acLogicalDs1FarEndDaySESs = _AcLogicalDs1FarEndDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 7),
    _AcLogicalDs1FarEndDaySESs_Type()
)
acLogicalDs1FarEndDaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDaySESs.setStatus("current")
_AcLogicalDs1FarEndDaySEFSs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDaySEFSs_Object = MibTableColumn
acLogicalDs1FarEndDaySEFSs = _AcLogicalDs1FarEndDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 8),
    _AcLogicalDs1FarEndDaySEFSs_Type()
)
acLogicalDs1FarEndDaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDaySEFSs.setStatus("current")
_AcLogicalDs1FarEndDayUASs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayUASs_Object = MibTableColumn
acLogicalDs1FarEndDayUASs = _AcLogicalDs1FarEndDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 9),
    _AcLogicalDs1FarEndDayUASs_Type()
)
acLogicalDs1FarEndDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayUASs.setStatus("current")
_AcLogicalDs1FarEndDayCSSs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayCSSs_Object = MibTableColumn
acLogicalDs1FarEndDayCSSs = _AcLogicalDs1FarEndDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 10),
    _AcLogicalDs1FarEndDayCSSs_Type()
)
acLogicalDs1FarEndDayCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayCSSs.setStatus("current")
_AcLogicalDs1FarEndDayLESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayLESs_Object = MibTableColumn
acLogicalDs1FarEndDayLESs = _AcLogicalDs1FarEndDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 11),
    _AcLogicalDs1FarEndDayLESs_Type()
)
acLogicalDs1FarEndDayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayLESs.setStatus("current")
_AcLogicalDs1FarEndDayPCVs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayPCVs_Object = MibTableColumn
acLogicalDs1FarEndDayPCVs = _AcLogicalDs1FarEndDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 12),
    _AcLogicalDs1FarEndDayPCVs_Type()
)
acLogicalDs1FarEndDayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayPCVs.setStatus("current")
_AcLogicalDs1FarEndDayBESs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayBESs_Object = MibTableColumn
acLogicalDs1FarEndDayBESs = _AcLogicalDs1FarEndDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 13),
    _AcLogicalDs1FarEndDayBESs_Type()
)
acLogicalDs1FarEndDayBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayBESs.setStatus("current")
_AcLogicalDs1FarEndDayDMs_Type = PerfIntervalCount
_AcLogicalDs1FarEndDayDMs_Object = MibTableColumn
acLogicalDs1FarEndDayDMs = _AcLogicalDs1FarEndDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 5, 1, 14),
    _AcLogicalDs1FarEndDayDMs_Type()
)
acLogicalDs1FarEndDayDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalDs1FarEndDayDMs.setStatus("current")
_AcLogicalDs1ThresholdTable_Object = MibTable
acLogicalDs1ThresholdTable = _AcLogicalDs1ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdTable.setStatus("current")
_AcLogicalDs1ThresholdEntry_Object = MibTableRow
acLogicalDs1ThresholdEntry = _AcLogicalDs1ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1)
)
acLogicalDs1ThresholdEntry.setIndexNames(
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
    (0, "APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"),
)
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdEntry.setStatus("current")
_AcLogicalDs1ThresholdNodeId_Type = AcNodeId
_AcLogicalDs1ThresholdNodeId_Object = MibTableColumn
acLogicalDs1ThresholdNodeId = _AcLogicalDs1ThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 1),
    _AcLogicalDs1ThresholdNodeId_Type()
)
acLogicalDs1ThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNodeId.setStatus("current")
_AcLogicalDs1ThresholdIndex_Type = Integer32
_AcLogicalDs1ThresholdIndex_Object = MibTableColumn
acLogicalDs1ThresholdIndex = _AcLogicalDs1ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 2),
    _AcLogicalDs1ThresholdIndex_Type()
)
acLogicalDs1ThresholdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdIndex.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalESs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalESs = _AcLogicalDs1ThresholdNEIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 3),
    _AcLogicalDs1ThresholdNEIntervalESs_Type()
)
acLogicalDs1ThresholdNEIntervalESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalESs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalSESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalSESs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalSESs = _AcLogicalDs1ThresholdNEIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 4),
    _AcLogicalDs1ThresholdNEIntervalSESs_Type()
)
acLogicalDs1ThresholdNEIntervalSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalSESs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalSEFSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalSEFSs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalSEFSs = _AcLogicalDs1ThresholdNEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 5),
    _AcLogicalDs1ThresholdNEIntervalSEFSs_Type()
)
acLogicalDs1ThresholdNEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalSEFSs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalUASs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalUASs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalUASs = _AcLogicalDs1ThresholdNEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 6),
    _AcLogicalDs1ThresholdNEIntervalUASs_Type()
)
acLogicalDs1ThresholdNEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalUASs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalCSSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalCSSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalCSSs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalCSSs = _AcLogicalDs1ThresholdNEIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 7),
    _AcLogicalDs1ThresholdNEIntervalCSSs_Type()
)
acLogicalDs1ThresholdNEIntervalCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalCSSs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalPCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalPCVs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalPCVs = _AcLogicalDs1ThresholdNEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 8),
    _AcLogicalDs1ThresholdNEIntervalPCVs_Type()
)
acLogicalDs1ThresholdNEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalPCVs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalLESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalLESs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalLESs = _AcLogicalDs1ThresholdNEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 9),
    _AcLogicalDs1ThresholdNEIntervalLESs_Type()
)
acLogicalDs1ThresholdNEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalLESs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalBESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalBESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalBESs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalBESs = _AcLogicalDs1ThresholdNEIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 10),
    _AcLogicalDs1ThresholdNEIntervalBESs_Type()
)
acLogicalDs1ThresholdNEIntervalBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalBESs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalDMs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalDMs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalDMs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalDMs = _AcLogicalDs1ThresholdNEIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 11),
    _AcLogicalDs1ThresholdNEIntervalDMs_Type()
)
acLogicalDs1ThresholdNEIntervalDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalDMs.setStatus("current")


class _AcLogicalDs1ThresholdNEIntervalLCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEIntervalLCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEIntervalLCVs_Object = MibTableColumn
acLogicalDs1ThresholdNEIntervalLCVs = _AcLogicalDs1ThresholdNEIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 12),
    _AcLogicalDs1ThresholdNEIntervalLCVs_Type()
)
acLogicalDs1ThresholdNEIntervalLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEIntervalLCVs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayESs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayESs = _AcLogicalDs1ThresholdNEDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 13),
    _AcLogicalDs1ThresholdNEDayESs_Type()
)
acLogicalDs1ThresholdNEDayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayESs.setStatus("current")


class _AcLogicalDs1ThresholdNEDaySESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDaySESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDaySESs_Object = MibTableColumn
acLogicalDs1ThresholdNEDaySESs = _AcLogicalDs1ThresholdNEDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 14),
    _AcLogicalDs1ThresholdNEDaySESs_Type()
)
acLogicalDs1ThresholdNEDaySESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDaySESs.setStatus("current")


class _AcLogicalDs1ThresholdNEDaySEFSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDaySEFSs_Object = MibTableColumn
acLogicalDs1ThresholdNEDaySEFSs = _AcLogicalDs1ThresholdNEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 15),
    _AcLogicalDs1ThresholdNEDaySEFSs_Type()
)
acLogicalDs1ThresholdNEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDaySEFSs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayUASs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayUASs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayUASs = _AcLogicalDs1ThresholdNEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 16),
    _AcLogicalDs1ThresholdNEDayUASs_Type()
)
acLogicalDs1ThresholdNEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayUASs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayCSSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayCSSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayCSSs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayCSSs = _AcLogicalDs1ThresholdNEDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 17),
    _AcLogicalDs1ThresholdNEDayCSSs_Type()
)
acLogicalDs1ThresholdNEDayCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayCSSs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayPCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayPCVs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayPCVs = _AcLogicalDs1ThresholdNEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 18),
    _AcLogicalDs1ThresholdNEDayPCVs_Type()
)
acLogicalDs1ThresholdNEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayPCVs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayLESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayLESs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayLESs = _AcLogicalDs1ThresholdNEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 19),
    _AcLogicalDs1ThresholdNEDayLESs_Type()
)
acLogicalDs1ThresholdNEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayLESs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayBESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayBESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayBESs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayBESs = _AcLogicalDs1ThresholdNEDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 20),
    _AcLogicalDs1ThresholdNEDayBESs_Type()
)
acLogicalDs1ThresholdNEDayBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayBESs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayDMs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayDMs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayDMs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayDMs = _AcLogicalDs1ThresholdNEDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 21),
    _AcLogicalDs1ThresholdNEDayDMs_Type()
)
acLogicalDs1ThresholdNEDayDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayDMs.setStatus("current")


class _AcLogicalDs1ThresholdNEDayLCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdNEDayLCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdNEDayLCVs_Object = MibTableColumn
acLogicalDs1ThresholdNEDayLCVs = _AcLogicalDs1ThresholdNEDayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 22),
    _AcLogicalDs1ThresholdNEDayLCVs_Type()
)
acLogicalDs1ThresholdNEDayLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdNEDayLCVs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalESs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalESs = _AcLogicalDs1ThresholdFEIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 23),
    _AcLogicalDs1ThresholdFEIntervalESs_Type()
)
acLogicalDs1ThresholdFEIntervalESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalESs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalSESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalSESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalSESs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalSESs = _AcLogicalDs1ThresholdFEIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 24),
    _AcLogicalDs1ThresholdFEIntervalSESs_Type()
)
acLogicalDs1ThresholdFEIntervalSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalSESs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalSEFSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalSEFSs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalSEFSs = _AcLogicalDs1ThresholdFEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 25),
    _AcLogicalDs1ThresholdFEIntervalSEFSs_Type()
)
acLogicalDs1ThresholdFEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalSEFSs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalUASs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalUASs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalUASs = _AcLogicalDs1ThresholdFEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 26),
    _AcLogicalDs1ThresholdFEIntervalUASs_Type()
)
acLogicalDs1ThresholdFEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalUASs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalCSSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalCSSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalCSSs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalCSSs = _AcLogicalDs1ThresholdFEIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 27),
    _AcLogicalDs1ThresholdFEIntervalCSSs_Type()
)
acLogicalDs1ThresholdFEIntervalCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalCSSs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalLESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalLESs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalLESs = _AcLogicalDs1ThresholdFEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 28),
    _AcLogicalDs1ThresholdFEIntervalLESs_Type()
)
acLogicalDs1ThresholdFEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalLESs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalPCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalPCVs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalPCVs = _AcLogicalDs1ThresholdFEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 29),
    _AcLogicalDs1ThresholdFEIntervalPCVs_Type()
)
acLogicalDs1ThresholdFEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalPCVs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalBESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalBESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalBESs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalBESs = _AcLogicalDs1ThresholdFEIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 30),
    _AcLogicalDs1ThresholdFEIntervalBESs_Type()
)
acLogicalDs1ThresholdFEIntervalBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalBESs.setStatus("current")


class _AcLogicalDs1ThresholdFEIntervalDMs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEIntervalDMs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEIntervalDMs_Object = MibTableColumn
acLogicalDs1ThresholdFEIntervalDMs = _AcLogicalDs1ThresholdFEIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 31),
    _AcLogicalDs1ThresholdFEIntervalDMs_Type()
)
acLogicalDs1ThresholdFEIntervalDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEIntervalDMs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayESs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayESs = _AcLogicalDs1ThresholdFEDayESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 32),
    _AcLogicalDs1ThresholdFEDayESs_Type()
)
acLogicalDs1ThresholdFEDayESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayESs.setStatus("current")


class _AcLogicalDs1ThresholdFEDaySESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDaySESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDaySESs_Object = MibTableColumn
acLogicalDs1ThresholdFEDaySESs = _AcLogicalDs1ThresholdFEDaySESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 33),
    _AcLogicalDs1ThresholdFEDaySESs_Type()
)
acLogicalDs1ThresholdFEDaySESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDaySESs.setStatus("current")


class _AcLogicalDs1ThresholdFEDaySEFSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDaySEFSs_Object = MibTableColumn
acLogicalDs1ThresholdFEDaySEFSs = _AcLogicalDs1ThresholdFEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 34),
    _AcLogicalDs1ThresholdFEDaySEFSs_Type()
)
acLogicalDs1ThresholdFEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDaySEFSs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayUASs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayUASs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayUASs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayUASs = _AcLogicalDs1ThresholdFEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 35),
    _AcLogicalDs1ThresholdFEDayUASs_Type()
)
acLogicalDs1ThresholdFEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayUASs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayCSSs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayCSSs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayCSSs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayCSSs = _AcLogicalDs1ThresholdFEDayCSSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 36),
    _AcLogicalDs1ThresholdFEDayCSSs_Type()
)
acLogicalDs1ThresholdFEDayCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayCSSs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayLESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayLESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayLESs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayLESs = _AcLogicalDs1ThresholdFEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 37),
    _AcLogicalDs1ThresholdFEDayLESs_Type()
)
acLogicalDs1ThresholdFEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayLESs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayPCVs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayPCVs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayPCVs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayPCVs = _AcLogicalDs1ThresholdFEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 38),
    _AcLogicalDs1ThresholdFEDayPCVs_Type()
)
acLogicalDs1ThresholdFEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayPCVs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayBESs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayBESs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayBESs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayBESs = _AcLogicalDs1ThresholdFEDayBESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 39),
    _AcLogicalDs1ThresholdFEDayBESs_Type()
)
acLogicalDs1ThresholdFEDayBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayBESs.setStatus("current")


class _AcLogicalDs1ThresholdFEDayDMs_Type(Integer32):
    """Custom type acLogicalDs1ThresholdFEDayDMs based on Integer32"""
    defaultValue = 0


_AcLogicalDs1ThresholdFEDayDMs_Object = MibTableColumn
acLogicalDs1ThresholdFEDayDMs = _AcLogicalDs1ThresholdFEDayDMs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 6, 1, 40),
    _AcLogicalDs1ThresholdFEDayDMs_Type()
)
acLogicalDs1ThresholdFEDayDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalDs1ThresholdFEDayDMs.setStatus("current")

# Managed Objects groups


# Notification objects

acLogicalDs1LineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 1)
)
acLogicalDs1LineStatusChangeTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigLineStatus"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigLineStatusLastChange"))
)
if mibBuilder.loadTexts:
    acLogicalDs1LineStatusChangeTrap.setStatus(
        "current"
    )

acLogicalDs1StatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 2)
)
acLogicalDs1StatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1StatsResetTrap.setStatus(
        "current"
    )

acLogicalDs1CfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 3)
)
acLogicalDs1CfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1CfgErrorTrap.setStatus(
        "current"
    )

acLogicalDs1LinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 4)
)
acLogicalDs1LinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1LinkDownTrap.setStatus(
        "current"
    )

acLogicalDs1LinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 5)
)
acLogicalDs1LinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ConfigIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1LinkUpTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 7)
)
acLogicalDs1ExceededThresholdNEIntervalESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 8)
)
acLogicalDs1ExceededThresholdNEIntervalSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalSESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 9)
)
acLogicalDs1ExceededThresholdNEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalSEFSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 10)
)
acLogicalDs1ExceededThresholdNEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalUASsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 11)
)
acLogicalDs1ExceededThresholdNEIntervalCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalCSSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 12)
)
acLogicalDs1ExceededThresholdNEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalPCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 13)
)
acLogicalDs1ExceededThresholdNEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalLESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 14)
)
acLogicalDs1ExceededThresholdNEIntervalBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalBESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 15)
)
acLogicalDs1ExceededThresholdNEIntervalDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalDMsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEIntervalLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 16)
)
acLogicalDs1ExceededThresholdNEIntervalLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEIntervalLCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 17)
)
acLogicalDs1ExceededThresholdNEDayESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDaySESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 18)
)
acLogicalDs1ExceededThresholdNEDaySESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDaySESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDaySEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 19)
)
acLogicalDs1ExceededThresholdNEDaySEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDaySEFSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 20)
)
acLogicalDs1ExceededThresholdNEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayUASsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 21)
)
acLogicalDs1ExceededThresholdNEDayCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayCSSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 22)
)
acLogicalDs1ExceededThresholdNEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayPCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 23)
)
acLogicalDs1ExceededThresholdNEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayLESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 24)
)
acLogicalDs1ExceededThresholdNEDayBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayBESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 25)
)
acLogicalDs1ExceededThresholdNEDayDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayDMsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdNEDayLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 26)
)
acLogicalDs1ExceededThresholdNEDayLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdNEDayLCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 27)
)
acLogicalDs1ExceededThresholdFEIntervalESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 28)
)
acLogicalDs1ExceededThresholdFEIntervalSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalSESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 29)
)
acLogicalDs1ExceededThresholdFEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalSEFSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 30)
)
acLogicalDs1ExceededThresholdFEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalUASsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 31)
)
acLogicalDs1ExceededThresholdFEIntervalCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalCSSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 32)
)
acLogicalDs1ExceededThresholdFEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalLESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 33)
)
acLogicalDs1ExceededThresholdFEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalPCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 34)
)
acLogicalDs1ExceededThresholdFEIntervalBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalBESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEIntervalDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 35)
)
acLogicalDs1ExceededThresholdFEIntervalDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEIntervalDMsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 36)
)
acLogicalDs1ExceededThresholdFEDayESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDaySESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 37)
)
acLogicalDs1ExceededThresholdFEDaySESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDaySESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDaySEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 38)
)
acLogicalDs1ExceededThresholdFEDaySEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDaySEFSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 39)
)
acLogicalDs1ExceededThresholdFEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayUASsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayCSSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 40)
)
acLogicalDs1ExceededThresholdFEDayCSSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayCSSsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 41)
)
acLogicalDs1ExceededThresholdFEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayLESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 42)
)
acLogicalDs1ExceededThresholdFEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayPCVsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayBESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 43)
)
acLogicalDs1ExceededThresholdFEDayBESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayBESsTrap.setStatus(
        "current"
    )

acLogicalDs1ExceededThresholdFEDayDMsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 2, 0, 44)
)
acLogicalDs1ExceededThresholdFEDayDMsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdNodeId"),
        ("APPIAN-LPORT-DS1-MIB", "acLogicalDs1ThresholdIndex"))
)
if mibBuilder.loadTexts:
    acLogicalDs1ExceededThresholdFEDayDMsTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-LPORT-DS1-MIB",
    **{"acLogicalDs1": acLogicalDs1,
       "acLogicalDs1Traps": acLogicalDs1Traps,
       "acLogicalDs1LineStatusChangeTrap": acLogicalDs1LineStatusChangeTrap,
       "acLogicalDs1StatsResetTrap": acLogicalDs1StatsResetTrap,
       "acLogicalDs1CfgErrorTrap": acLogicalDs1CfgErrorTrap,
       "acLogicalDs1LinkDownTrap": acLogicalDs1LinkDownTrap,
       "acLogicalDs1LinkUpTrap": acLogicalDs1LinkUpTrap,
       "acLogicalDs1ExceededThresholdNEIntervalESsTrap": acLogicalDs1ExceededThresholdNEIntervalESsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalSESsTrap": acLogicalDs1ExceededThresholdNEIntervalSESsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalSEFSsTrap": acLogicalDs1ExceededThresholdNEIntervalSEFSsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalUASsTrap": acLogicalDs1ExceededThresholdNEIntervalUASsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalCSSsTrap": acLogicalDs1ExceededThresholdNEIntervalCSSsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalPCVsTrap": acLogicalDs1ExceededThresholdNEIntervalPCVsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalLESsTrap": acLogicalDs1ExceededThresholdNEIntervalLESsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalBESsTrap": acLogicalDs1ExceededThresholdNEIntervalBESsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalDMsTrap": acLogicalDs1ExceededThresholdNEIntervalDMsTrap,
       "acLogicalDs1ExceededThresholdNEIntervalLCVsTrap": acLogicalDs1ExceededThresholdNEIntervalLCVsTrap,
       "acLogicalDs1ExceededThresholdNEDayESsTrap": acLogicalDs1ExceededThresholdNEDayESsTrap,
       "acLogicalDs1ExceededThresholdNEDaySESsTrap": acLogicalDs1ExceededThresholdNEDaySESsTrap,
       "acLogicalDs1ExceededThresholdNEDaySEFSsTrap": acLogicalDs1ExceededThresholdNEDaySEFSsTrap,
       "acLogicalDs1ExceededThresholdNEDayUASsTrap": acLogicalDs1ExceededThresholdNEDayUASsTrap,
       "acLogicalDs1ExceededThresholdNEDayCSSsTrap": acLogicalDs1ExceededThresholdNEDayCSSsTrap,
       "acLogicalDs1ExceededThresholdNEDayPCVsTrap": acLogicalDs1ExceededThresholdNEDayPCVsTrap,
       "acLogicalDs1ExceededThresholdNEDayLESsTrap": acLogicalDs1ExceededThresholdNEDayLESsTrap,
       "acLogicalDs1ExceededThresholdNEDayBESsTrap": acLogicalDs1ExceededThresholdNEDayBESsTrap,
       "acLogicalDs1ExceededThresholdNEDayDMsTrap": acLogicalDs1ExceededThresholdNEDayDMsTrap,
       "acLogicalDs1ExceededThresholdNEDayLCVsTrap": acLogicalDs1ExceededThresholdNEDayLCVsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalESsTrap": acLogicalDs1ExceededThresholdFEIntervalESsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalSESsTrap": acLogicalDs1ExceededThresholdFEIntervalSESsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalSEFSsTrap": acLogicalDs1ExceededThresholdFEIntervalSEFSsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalUASsTrap": acLogicalDs1ExceededThresholdFEIntervalUASsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalCSSsTrap": acLogicalDs1ExceededThresholdFEIntervalCSSsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalLESsTrap": acLogicalDs1ExceededThresholdFEIntervalLESsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalPCVsTrap": acLogicalDs1ExceededThresholdFEIntervalPCVsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalBESsTrap": acLogicalDs1ExceededThresholdFEIntervalBESsTrap,
       "acLogicalDs1ExceededThresholdFEIntervalDMsTrap": acLogicalDs1ExceededThresholdFEIntervalDMsTrap,
       "acLogicalDs1ExceededThresholdFEDayESsTrap": acLogicalDs1ExceededThresholdFEDayESsTrap,
       "acLogicalDs1ExceededThresholdFEDaySESsTrap": acLogicalDs1ExceededThresholdFEDaySESsTrap,
       "acLogicalDs1ExceededThresholdFEDaySEFSsTrap": acLogicalDs1ExceededThresholdFEDaySEFSsTrap,
       "acLogicalDs1ExceededThresholdFEDayUASsTrap": acLogicalDs1ExceededThresholdFEDayUASsTrap,
       "acLogicalDs1ExceededThresholdFEDayCSSsTrap": acLogicalDs1ExceededThresholdFEDayCSSsTrap,
       "acLogicalDs1ExceededThresholdFEDayLESsTrap": acLogicalDs1ExceededThresholdFEDayLESsTrap,
       "acLogicalDs1ExceededThresholdFEDayPCVsTrap": acLogicalDs1ExceededThresholdFEDayPCVsTrap,
       "acLogicalDs1ExceededThresholdFEDayBESsTrap": acLogicalDs1ExceededThresholdFEDayBESsTrap,
       "acLogicalDs1ExceededThresholdFEDayDMsTrap": acLogicalDs1ExceededThresholdFEDayDMsTrap,
       "acLogicalDs1ConfigTable": acLogicalDs1ConfigTable,
       "acLogicalDs1ConfigEntry": acLogicalDs1ConfigEntry,
       "acLogicalDs1ConfigNodeId": acLogicalDs1ConfigNodeId,
       "acLogicalDs1ConfigIndex": acLogicalDs1ConfigIndex,
       "acLogicalDs1ConfigAdminStatus": acLogicalDs1ConfigAdminStatus,
       "acLogicalDs1ConfigTimeElapsedInterval": acLogicalDs1ConfigTimeElapsedInterval,
       "acLogicalDs1ConfigValidIntervals": acLogicalDs1ConfigValidIntervals,
       "acLogicalDs1ConfigTimeElapsedDay": acLogicalDs1ConfigTimeElapsedDay,
       "acLogicalDs1ConfigValidDays": acLogicalDs1ConfigValidDays,
       "acLogicalDs1ConfigTimeElapsedFarEndInterval": acLogicalDs1ConfigTimeElapsedFarEndInterval,
       "acLogicalDs1ConfigValidFarEndIntervals": acLogicalDs1ConfigValidFarEndIntervals,
       "acLogicalDs1ConfigTimeElapsedFarEndDay": acLogicalDs1ConfigTimeElapsedFarEndDay,
       "acLogicalDs1ConfigValidFarEndDays": acLogicalDs1ConfigValidFarEndDays,
       "acLogicalDs1ConfigSendCode": acLogicalDs1ConfigSendCode,
       "acLogicalDs1ConfigCircuitIdentifier": acLogicalDs1ConfigCircuitIdentifier,
       "acLogicalDs1ConfigLoopbackConfig": acLogicalDs1ConfigLoopbackConfig,
       "acLogicalDs1ConfigLineStatus": acLogicalDs1ConfigLineStatus,
       "acLogicalDs1ConfigTransmitClockSource": acLogicalDs1ConfigTransmitClockSource,
       "acLogicalDs1ConfigInvalidIntervals": acLogicalDs1ConfigInvalidIntervals,
       "acLogicalDs1ConfigInvalidDays": acLogicalDs1ConfigInvalidDays,
       "acLogicalDs1ConfigInvalidFarEndIntervals": acLogicalDs1ConfigInvalidFarEndIntervals,
       "acLogicalDs1ConfigInvalidFarEndDays": acLogicalDs1ConfigInvalidFarEndDays,
       "acLogicalDs1ConfigLineStatusLastChange": acLogicalDs1ConfigLineStatusLastChange,
       "acLogicalDs1ConfigLineStatusChangeTrapEnable": acLogicalDs1ConfigLineStatusChangeTrapEnable,
       "acLogicalDs1ConfigLoopbackStatus": acLogicalDs1ConfigLoopbackStatus,
       "acLogicalDs1ConfigVTNumber": acLogicalDs1ConfigVTNumber,
       "acLogicalDs1IntervalTable": acLogicalDs1IntervalTable,
       "acLogicalDs1IntervalEntry": acLogicalDs1IntervalEntry,
       "acLogicalDs1IntervalNodeId": acLogicalDs1IntervalNodeId,
       "acLogicalDs1IntervalIndex": acLogicalDs1IntervalIndex,
       "acLogicalDs1IntervalNumber": acLogicalDs1IntervalNumber,
       "acLogicalDs1IntervalValidStats": acLogicalDs1IntervalValidStats,
       "acLogicalDs1IntervalResetStats": acLogicalDs1IntervalResetStats,
       "acLogicalDs1IntervalESs": acLogicalDs1IntervalESs,
       "acLogicalDs1IntervalSESs": acLogicalDs1IntervalSESs,
       "acLogicalDs1IntervalSEFSs": acLogicalDs1IntervalSEFSs,
       "acLogicalDs1IntervalUASs": acLogicalDs1IntervalUASs,
       "acLogicalDs1IntervalCSSs": acLogicalDs1IntervalCSSs,
       "acLogicalDs1IntervalPCVs": acLogicalDs1IntervalPCVs,
       "acLogicalDs1IntervalLESs": acLogicalDs1IntervalLESs,
       "acLogicalDs1IntervalBESs": acLogicalDs1IntervalBESs,
       "acLogicalDs1IntervalDMs": acLogicalDs1IntervalDMs,
       "acLogicalDs1IntervalLCVs": acLogicalDs1IntervalLCVs,
       "acLogicalDs1DayTable": acLogicalDs1DayTable,
       "acLogicalDs1DayEntry": acLogicalDs1DayEntry,
       "acLogicalDs1DayNodeId": acLogicalDs1DayNodeId,
       "acLogicalDs1DayIndex": acLogicalDs1DayIndex,
       "acLogicalDs1DayNumber": acLogicalDs1DayNumber,
       "acLogicalDs1DayValidStats": acLogicalDs1DayValidStats,
       "acLogicalDs1DayResetStats": acLogicalDs1DayResetStats,
       "acLogicalDs1DayESs": acLogicalDs1DayESs,
       "acLogicalDs1DaySESs": acLogicalDs1DaySESs,
       "acLogicalDs1DaySEFSs": acLogicalDs1DaySEFSs,
       "acLogicalDs1DayUASs": acLogicalDs1DayUASs,
       "acLogicalDs1DayCSSs": acLogicalDs1DayCSSs,
       "acLogicalDs1DayPCVs": acLogicalDs1DayPCVs,
       "acLogicalDs1DayLESs": acLogicalDs1DayLESs,
       "acLogicalDs1DayBESs": acLogicalDs1DayBESs,
       "acLogicalDs1DayDMs": acLogicalDs1DayDMs,
       "acLogicalDs1DayLCVs": acLogicalDs1DayLCVs,
       "acLogicalDs1FarEndIntervalTable": acLogicalDs1FarEndIntervalTable,
       "acLogicalDs1FarEndIntervalEntry": acLogicalDs1FarEndIntervalEntry,
       "acLogicalDs1FarEndIntervalNodeId": acLogicalDs1FarEndIntervalNodeId,
       "acLogicalDs1FarEndIntervalIndex": acLogicalDs1FarEndIntervalIndex,
       "acLogicalDs1FarEndIntervalNumber": acLogicalDs1FarEndIntervalNumber,
       "acLogicalDs1FarEndIntervalValidStats": acLogicalDs1FarEndIntervalValidStats,
       "acLogicalDs1FarEndIntervalResetStats": acLogicalDs1FarEndIntervalResetStats,
       "acLogicalDs1FarEndIntervalESs": acLogicalDs1FarEndIntervalESs,
       "acLogicalDs1FarEndIntervalSESs": acLogicalDs1FarEndIntervalSESs,
       "acLogicalDs1FarEndIntervalSEFSs": acLogicalDs1FarEndIntervalSEFSs,
       "acLogicalDs1FarEndIntervalUASs": acLogicalDs1FarEndIntervalUASs,
       "acLogicalDs1FarEndIntervalCSSs": acLogicalDs1FarEndIntervalCSSs,
       "acLogicalDs1FarEndIntervalLESs": acLogicalDs1FarEndIntervalLESs,
       "acLogicalDs1FarEndIntervalPCVs": acLogicalDs1FarEndIntervalPCVs,
       "acLogicalDs1FarEndIntervalBESs": acLogicalDs1FarEndIntervalBESs,
       "acLogicalDs1FarEndIntervalDMs": acLogicalDs1FarEndIntervalDMs,
       "acLogicalDs1FarEndDayTable": acLogicalDs1FarEndDayTable,
       "acLogicalDs1FarEndDayEntry": acLogicalDs1FarEndDayEntry,
       "acLogicalDs1FarEndDayNodeId": acLogicalDs1FarEndDayNodeId,
       "acLogicalDs1FarEndDayIndex": acLogicalDs1FarEndDayIndex,
       "acLogicalDs1FarEndDayNumber": acLogicalDs1FarEndDayNumber,
       "acLogicalDs1FarEndDayValidStats": acLogicalDs1FarEndDayValidStats,
       "acLogicalDs1FarEndDayResetStats": acLogicalDs1FarEndDayResetStats,
       "acLogicalDs1FarEndDayESs": acLogicalDs1FarEndDayESs,
       "acLogicalDs1FarEndDaySESs": acLogicalDs1FarEndDaySESs,
       "acLogicalDs1FarEndDaySEFSs": acLogicalDs1FarEndDaySEFSs,
       "acLogicalDs1FarEndDayUASs": acLogicalDs1FarEndDayUASs,
       "acLogicalDs1FarEndDayCSSs": acLogicalDs1FarEndDayCSSs,
       "acLogicalDs1FarEndDayLESs": acLogicalDs1FarEndDayLESs,
       "acLogicalDs1FarEndDayPCVs": acLogicalDs1FarEndDayPCVs,
       "acLogicalDs1FarEndDayBESs": acLogicalDs1FarEndDayBESs,
       "acLogicalDs1FarEndDayDMs": acLogicalDs1FarEndDayDMs,
       "acLogicalDs1ThresholdTable": acLogicalDs1ThresholdTable,
       "acLogicalDs1ThresholdEntry": acLogicalDs1ThresholdEntry,
       "acLogicalDs1ThresholdNodeId": acLogicalDs1ThresholdNodeId,
       "acLogicalDs1ThresholdIndex": acLogicalDs1ThresholdIndex,
       "acLogicalDs1ThresholdNEIntervalESs": acLogicalDs1ThresholdNEIntervalESs,
       "acLogicalDs1ThresholdNEIntervalSESs": acLogicalDs1ThresholdNEIntervalSESs,
       "acLogicalDs1ThresholdNEIntervalSEFSs": acLogicalDs1ThresholdNEIntervalSEFSs,
       "acLogicalDs1ThresholdNEIntervalUASs": acLogicalDs1ThresholdNEIntervalUASs,
       "acLogicalDs1ThresholdNEIntervalCSSs": acLogicalDs1ThresholdNEIntervalCSSs,
       "acLogicalDs1ThresholdNEIntervalPCVs": acLogicalDs1ThresholdNEIntervalPCVs,
       "acLogicalDs1ThresholdNEIntervalLESs": acLogicalDs1ThresholdNEIntervalLESs,
       "acLogicalDs1ThresholdNEIntervalBESs": acLogicalDs1ThresholdNEIntervalBESs,
       "acLogicalDs1ThresholdNEIntervalDMs": acLogicalDs1ThresholdNEIntervalDMs,
       "acLogicalDs1ThresholdNEIntervalLCVs": acLogicalDs1ThresholdNEIntervalLCVs,
       "acLogicalDs1ThresholdNEDayESs": acLogicalDs1ThresholdNEDayESs,
       "acLogicalDs1ThresholdNEDaySESs": acLogicalDs1ThresholdNEDaySESs,
       "acLogicalDs1ThresholdNEDaySEFSs": acLogicalDs1ThresholdNEDaySEFSs,
       "acLogicalDs1ThresholdNEDayUASs": acLogicalDs1ThresholdNEDayUASs,
       "acLogicalDs1ThresholdNEDayCSSs": acLogicalDs1ThresholdNEDayCSSs,
       "acLogicalDs1ThresholdNEDayPCVs": acLogicalDs1ThresholdNEDayPCVs,
       "acLogicalDs1ThresholdNEDayLESs": acLogicalDs1ThresholdNEDayLESs,
       "acLogicalDs1ThresholdNEDayBESs": acLogicalDs1ThresholdNEDayBESs,
       "acLogicalDs1ThresholdNEDayDMs": acLogicalDs1ThresholdNEDayDMs,
       "acLogicalDs1ThresholdNEDayLCVs": acLogicalDs1ThresholdNEDayLCVs,
       "acLogicalDs1ThresholdFEIntervalESs": acLogicalDs1ThresholdFEIntervalESs,
       "acLogicalDs1ThresholdFEIntervalSESs": acLogicalDs1ThresholdFEIntervalSESs,
       "acLogicalDs1ThresholdFEIntervalSEFSs": acLogicalDs1ThresholdFEIntervalSEFSs,
       "acLogicalDs1ThresholdFEIntervalUASs": acLogicalDs1ThresholdFEIntervalUASs,
       "acLogicalDs1ThresholdFEIntervalCSSs": acLogicalDs1ThresholdFEIntervalCSSs,
       "acLogicalDs1ThresholdFEIntervalLESs": acLogicalDs1ThresholdFEIntervalLESs,
       "acLogicalDs1ThresholdFEIntervalPCVs": acLogicalDs1ThresholdFEIntervalPCVs,
       "acLogicalDs1ThresholdFEIntervalBESs": acLogicalDs1ThresholdFEIntervalBESs,
       "acLogicalDs1ThresholdFEIntervalDMs": acLogicalDs1ThresholdFEIntervalDMs,
       "acLogicalDs1ThresholdFEDayESs": acLogicalDs1ThresholdFEDayESs,
       "acLogicalDs1ThresholdFEDaySESs": acLogicalDs1ThresholdFEDaySESs,
       "acLogicalDs1ThresholdFEDaySEFSs": acLogicalDs1ThresholdFEDaySEFSs,
       "acLogicalDs1ThresholdFEDayUASs": acLogicalDs1ThresholdFEDayUASs,
       "acLogicalDs1ThresholdFEDayCSSs": acLogicalDs1ThresholdFEDayCSSs,
       "acLogicalDs1ThresholdFEDayLESs": acLogicalDs1ThresholdFEDayLESs,
       "acLogicalDs1ThresholdFEDayPCVs": acLogicalDs1ThresholdFEDayPCVs,
       "acLogicalDs1ThresholdFEDayBESs": acLogicalDs1ThresholdFEDayBESs,
       "acLogicalDs1ThresholdFEDayDMs": acLogicalDs1ThresholdFEDayDMs}
)
