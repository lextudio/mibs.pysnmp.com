# SNMP MIB module (APPIAN-PPORT-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:40 2024
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

acDs3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcDs3Traps_ObjectIdentity = ObjectIdentity
acDs3Traps = _AcDs3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0)
)
_AcDs3ConfigTable_Object = MibTable
acDs3ConfigTable = _AcDs3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    acDs3ConfigTable.setStatus("current")
_AcDs3ConfigEntry_Object = MibTableRow
acDs3ConfigEntry = _AcDs3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1)
)
acDs3ConfigEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"),
)
if mibBuilder.loadTexts:
    acDs3ConfigEntry.setStatus("current")
_AcDs3ConfigNodeId_Type = AcNodeId
_AcDs3ConfigNodeId_Object = MibTableColumn
acDs3ConfigNodeId = _AcDs3ConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 1),
    _AcDs3ConfigNodeId_Type()
)
acDs3ConfigNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ConfigNodeId.setStatus("current")
_AcDs3ConfigSlot_Type = AcSlotNumber
_AcDs3ConfigSlot_Object = MibTableColumn
acDs3ConfigSlot = _AcDs3ConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 2),
    _AcDs3ConfigSlot_Type()
)
acDs3ConfigSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ConfigSlot.setStatus("current")
_AcDs3ConfigPort_Type = AcPortNumber
_AcDs3ConfigPort_Object = MibTableColumn
acDs3ConfigPort = _AcDs3ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 3),
    _AcDs3ConfigPort_Type()
)
acDs3ConfigPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ConfigPort.setStatus("current")


class _AcDs3ConfigAdminStatus_Type(AcAdminStatus):
    """Custom type acDs3ConfigAdminStatus based on AcAdminStatus"""


_AcDs3ConfigAdminStatus_Object = MibTableColumn
acDs3ConfigAdminStatus = _AcDs3ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 4),
    _AcDs3ConfigAdminStatus_Type()
)
acDs3ConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigAdminStatus.setStatus("current")
_AcDs3ConfigOpStatus_Type = AcOpStatus
_AcDs3ConfigOpStatus_Object = MibTableColumn
acDs3ConfigOpStatus = _AcDs3ConfigOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 5),
    _AcDs3ConfigOpStatus_Type()
)
acDs3ConfigOpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigOpStatus.setStatus("current")


class _AcDs3ConfigType_Type(Integer32):
    """Custom type acDs3ConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3Access", 1),
          ("ds3Network", 2))
    )


_AcDs3ConfigType_Type.__name__ = "Integer32"
_AcDs3ConfigType_Object = MibTableColumn
acDs3ConfigType = _AcDs3ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 6),
    _AcDs3ConfigType_Type()
)
acDs3ConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigType.setStatus("current")


class _AcDs3ConfigTimeElapsedInterval_Type(Integer32):
    """Custom type acDs3ConfigTimeElapsedInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcDs3ConfigTimeElapsedInterval_Type.__name__ = "Integer32"
_AcDs3ConfigTimeElapsedInterval_Object = MibTableColumn
acDs3ConfigTimeElapsedInterval = _AcDs3ConfigTimeElapsedInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 7),
    _AcDs3ConfigTimeElapsedInterval_Type()
)
acDs3ConfigTimeElapsedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigTimeElapsedInterval.setStatus("current")


class _AcDs3ConfigValidIntervals_Type(Integer32):
    """Custom type acDs3ConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs3ConfigValidIntervals_Type.__name__ = "Integer32"
_AcDs3ConfigValidIntervals_Object = MibTableColumn
acDs3ConfigValidIntervals = _AcDs3ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 8),
    _AcDs3ConfigValidIntervals_Type()
)
acDs3ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigValidIntervals.setStatus("current")


class _AcDs3ConfigTimeElapsedDay_Type(Integer32):
    """Custom type acDs3ConfigTimeElapsedDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcDs3ConfigTimeElapsedDay_Type.__name__ = "Integer32"
_AcDs3ConfigTimeElapsedDay_Object = MibTableColumn
acDs3ConfigTimeElapsedDay = _AcDs3ConfigTimeElapsedDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 9),
    _AcDs3ConfigTimeElapsedDay_Type()
)
acDs3ConfigTimeElapsedDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigTimeElapsedDay.setStatus("current")


class _AcDs3ConfigValidDays_Type(Integer32):
    """Custom type acDs3ConfigValidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs3ConfigValidDays_Type.__name__ = "Integer32"
_AcDs3ConfigValidDays_Object = MibTableColumn
acDs3ConfigValidDays = _AcDs3ConfigValidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 10),
    _AcDs3ConfigValidDays_Type()
)
acDs3ConfigValidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigValidDays.setStatus("current")


class _AcDs3ConfigTimeElapsedFarEndInterval_Type(Integer32):
    """Custom type acDs3ConfigTimeElapsedFarEndInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AcDs3ConfigTimeElapsedFarEndInterval_Type.__name__ = "Integer32"
_AcDs3ConfigTimeElapsedFarEndInterval_Object = MibTableColumn
acDs3ConfigTimeElapsedFarEndInterval = _AcDs3ConfigTimeElapsedFarEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 11),
    _AcDs3ConfigTimeElapsedFarEndInterval_Type()
)
acDs3ConfigTimeElapsedFarEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigTimeElapsedFarEndInterval.setStatus("current")


class _AcDs3ConfigValidFarEndIntervals_Type(Integer32):
    """Custom type acDs3ConfigValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs3ConfigValidFarEndIntervals_Type.__name__ = "Integer32"
_AcDs3ConfigValidFarEndIntervals_Object = MibTableColumn
acDs3ConfigValidFarEndIntervals = _AcDs3ConfigValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 12),
    _AcDs3ConfigValidFarEndIntervals_Type()
)
acDs3ConfigValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigValidFarEndIntervals.setStatus("current")


class _AcDs3ConfigTimeElapsedFarEndDay_Type(Integer32):
    """Custom type acDs3ConfigTimeElapsedFarEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AcDs3ConfigTimeElapsedFarEndDay_Type.__name__ = "Integer32"
_AcDs3ConfigTimeElapsedFarEndDay_Object = MibTableColumn
acDs3ConfigTimeElapsedFarEndDay = _AcDs3ConfigTimeElapsedFarEndDay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 13),
    _AcDs3ConfigTimeElapsedFarEndDay_Type()
)
acDs3ConfigTimeElapsedFarEndDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigTimeElapsedFarEndDay.setStatus("current")


class _AcDs3ConfigValidFarEndDays_Type(Integer32):
    """Custom type acDs3ConfigValidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs3ConfigValidFarEndDays_Type.__name__ = "Integer32"
_AcDs3ConfigValidFarEndDays_Object = MibTableColumn
acDs3ConfigValidFarEndDays = _AcDs3ConfigValidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 14),
    _AcDs3ConfigValidFarEndDays_Type()
)
acDs3ConfigValidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigValidFarEndDays.setStatus("current")


class _AcDs3ConfigLineType_Type(Integer32):
    """Custom type acDs3ConfigLineType based on Integer32"""
    defaultValue = 4

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
        *(("ds3CbitParity", 4),
          ("ds3ClearChannel", 5),
          ("ds3M23", 2),
          ("ds3SYNTRAN", 3),
          ("ds3other", 1))
    )


_AcDs3ConfigLineType_Type.__name__ = "Integer32"
_AcDs3ConfigLineType_Object = MibTableColumn
acDs3ConfigLineType = _AcDs3ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 15),
    _AcDs3ConfigLineType_Type()
)
acDs3ConfigLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigLineType.setStatus("current")


class _AcDs3ConfigLineCoding_Type(Integer32):
    """Custom type acDs3ConfigLineCoding based on Integer32"""
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
        *(("ds3B3ZS", 2),
          ("ds3Other", 1),
          ("e3HDB3", 3))
    )


_AcDs3ConfigLineCoding_Type.__name__ = "Integer32"
_AcDs3ConfigLineCoding_Object = MibTableColumn
acDs3ConfigLineCoding = _AcDs3ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 16),
    _AcDs3ConfigLineCoding_Type()
)
acDs3ConfigLineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigLineCoding.setStatus("current")


class _AcDs3ConfigSendCode_Type(Integer32):
    """Custom type acDs3ConfigSendCode based on Integer32"""
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


_AcDs3ConfigSendCode_Type.__name__ = "Integer32"
_AcDs3ConfigSendCode_Object = MibTableColumn
acDs3ConfigSendCode = _AcDs3ConfigSendCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 17),
    _AcDs3ConfigSendCode_Type()
)
acDs3ConfigSendCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigSendCode.setStatus("current")


class _AcDs3ConfigCircuitIdentifier_Type(DisplayString):
    """Custom type acDs3ConfigCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcDs3ConfigCircuitIdentifier_Type.__name__ = "DisplayString"
_AcDs3ConfigCircuitIdentifier_Object = MibTableColumn
acDs3ConfigCircuitIdentifier = _AcDs3ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 18),
    _AcDs3ConfigCircuitIdentifier_Type()
)
acDs3ConfigCircuitIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigCircuitIdentifier.setStatus("current")


class _AcDs3ConfigLoopbackConfig_Type(Integer32):
    """Custom type acDs3ConfigLoopbackConfig based on Integer32"""
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


_AcDs3ConfigLoopbackConfig_Type.__name__ = "Integer32"
_AcDs3ConfigLoopbackConfig_Object = MibTableColumn
acDs3ConfigLoopbackConfig = _AcDs3ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 19),
    _AcDs3ConfigLoopbackConfig_Type()
)
acDs3ConfigLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigLoopbackConfig.setStatus("current")


class _AcDs3ConfigLineStatus_Type(Integer32):
    """Custom type acDs3ConfigLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AcDs3ConfigLineStatus_Type.__name__ = "Integer32"
_AcDs3ConfigLineStatus_Object = MibTableColumn
acDs3ConfigLineStatus = _AcDs3ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 20),
    _AcDs3ConfigLineStatus_Type()
)
acDs3ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigLineStatus.setStatus("current")


class _AcDs3ConfigTransmitClockSource_Type(Integer32):
    """Custom type acDs3ConfigTransmitClockSource based on Integer32"""
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


_AcDs3ConfigTransmitClockSource_Type.__name__ = "Integer32"
_AcDs3ConfigTransmitClockSource_Object = MibTableColumn
acDs3ConfigTransmitClockSource = _AcDs3ConfigTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 21),
    _AcDs3ConfigTransmitClockSource_Type()
)
acDs3ConfigTransmitClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigTransmitClockSource.setStatus("current")


class _AcDs3ConfigInvalidIntervals_Type(Integer32):
    """Custom type acDs3ConfigInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs3ConfigInvalidIntervals_Type.__name__ = "Integer32"
_AcDs3ConfigInvalidIntervals_Object = MibTableColumn
acDs3ConfigInvalidIntervals = _AcDs3ConfigInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 22),
    _AcDs3ConfigInvalidIntervals_Type()
)
acDs3ConfigInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigInvalidIntervals.setStatus("current")


class _AcDs3ConfigInvalidDays_Type(Integer32):
    """Custom type acDs3ConfigInvalidDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs3ConfigInvalidDays_Type.__name__ = "Integer32"
_AcDs3ConfigInvalidDays_Object = MibTableColumn
acDs3ConfigInvalidDays = _AcDs3ConfigInvalidDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 23),
    _AcDs3ConfigInvalidDays_Type()
)
acDs3ConfigInvalidDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigInvalidDays.setStatus("current")


class _AcDs3ConfigInvalidFarEndIntervals_Type(Integer32):
    """Custom type acDs3ConfigInvalidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AcDs3ConfigInvalidFarEndIntervals_Type.__name__ = "Integer32"
_AcDs3ConfigInvalidFarEndIntervals_Object = MibTableColumn
acDs3ConfigInvalidFarEndIntervals = _AcDs3ConfigInvalidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 24),
    _AcDs3ConfigInvalidFarEndIntervals_Type()
)
acDs3ConfigInvalidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigInvalidFarEndIntervals.setStatus("current")


class _AcDs3ConfigInvalidFarEndDays_Type(Integer32):
    """Custom type acDs3ConfigInvalidFarEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcDs3ConfigInvalidFarEndDays_Type.__name__ = "Integer32"
_AcDs3ConfigInvalidFarEndDays_Object = MibTableColumn
acDs3ConfigInvalidFarEndDays = _AcDs3ConfigInvalidFarEndDays_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 25),
    _AcDs3ConfigInvalidFarEndDays_Type()
)
acDs3ConfigInvalidFarEndDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigInvalidFarEndDays.setStatus("current")


class _AcDs3ConfigLineLength_Type(Integer32):
    """Custom type acDs3ConfigLineLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_AcDs3ConfigLineLength_Type.__name__ = "Integer32"
_AcDs3ConfigLineLength_Object = MibTableColumn
acDs3ConfigLineLength = _AcDs3ConfigLineLength_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 26),
    _AcDs3ConfigLineLength_Type()
)
acDs3ConfigLineLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigLineLength.setStatus("current")
if mibBuilder.loadTexts:
    acDs3ConfigLineLength.setUnits("meters")
_AcDs3ConfigLineStatusLastChange_Type = TimeStamp
_AcDs3ConfigLineStatusLastChange_Object = MibTableColumn
acDs3ConfigLineStatusLastChange = _AcDs3ConfigLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 27),
    _AcDs3ConfigLineStatusLastChange_Type()
)
acDs3ConfigLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigLineStatusLastChange.setStatus("current")


class _AcDs3ConfigLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type acDs3ConfigLineStatusChangeTrapEnable based on Integer32"""
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


_AcDs3ConfigLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_AcDs3ConfigLineStatusChangeTrapEnable_Object = MibTableColumn
acDs3ConfigLineStatusChangeTrapEnable = _AcDs3ConfigLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 28),
    _AcDs3ConfigLineStatusChangeTrapEnable_Type()
)
acDs3ConfigLineStatusChangeTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigLineStatusChangeTrapEnable.setStatus("current")


class _AcDs3ConfigLoopbackStatus_Type(Integer32):
    """Custom type acDs3ConfigLoopbackStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AcDs3ConfigLoopbackStatus_Type.__name__ = "Integer32"
_AcDs3ConfigLoopbackStatus_Object = MibTableColumn
acDs3ConfigLoopbackStatus = _AcDs3ConfigLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 29),
    _AcDs3ConfigLoopbackStatus_Type()
)
acDs3ConfigLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigLoopbackStatus.setStatus("current")


class _AcDs3ConfigChannelization_Type(Integer32):
    """Custom type acDs3ConfigChannelization based on Integer32"""
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
        *(("disabled", 1),
          ("enabledDs1", 2),
          ("enabledDs2", 3))
    )


_AcDs3ConfigChannelization_Type.__name__ = "Integer32"
_AcDs3ConfigChannelization_Object = MibTableColumn
acDs3ConfigChannelization = _AcDs3ConfigChannelization_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 30),
    _AcDs3ConfigChannelization_Type()
)
acDs3ConfigChannelization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigChannelization.setStatus("current")


class _AcDs3ConfigDs1ForRemoteLoop_Type(Integer32):
    """Custom type acDs3ConfigDs1ForRemoteLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_AcDs3ConfigDs1ForRemoteLoop_Type.__name__ = "Integer32"
_AcDs3ConfigDs1ForRemoteLoop_Object = MibTableColumn
acDs3ConfigDs1ForRemoteLoop = _AcDs3ConfigDs1ForRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 31),
    _AcDs3ConfigDs1ForRemoteLoop_Type()
)
acDs3ConfigDs1ForRemoteLoop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigDs1ForRemoteLoop.setStatus("current")


class _AcDs3ConfigFarEndEquipCode_Type(DisplayString):
    """Custom type acDs3ConfigFarEndEquipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcDs3ConfigFarEndEquipCode_Type.__name__ = "DisplayString"
_AcDs3ConfigFarEndEquipCode_Object = MibTableColumn
acDs3ConfigFarEndEquipCode = _AcDs3ConfigFarEndEquipCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 32),
    _AcDs3ConfigFarEndEquipCode_Type()
)
acDs3ConfigFarEndEquipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigFarEndEquipCode.setStatus("current")


class _AcDs3ConfigFarEndLocationIDCode_Type(DisplayString):
    """Custom type acDs3ConfigFarEndLocationIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AcDs3ConfigFarEndLocationIDCode_Type.__name__ = "DisplayString"
_AcDs3ConfigFarEndLocationIDCode_Object = MibTableColumn
acDs3ConfigFarEndLocationIDCode = _AcDs3ConfigFarEndLocationIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 33),
    _AcDs3ConfigFarEndLocationIDCode_Type()
)
acDs3ConfigFarEndLocationIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigFarEndLocationIDCode.setStatus("current")


class _AcDs3ConfigFarEndFrameIDCode_Type(DisplayString):
    """Custom type acDs3ConfigFarEndFrameIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcDs3ConfigFarEndFrameIDCode_Type.__name__ = "DisplayString"
_AcDs3ConfigFarEndFrameIDCode_Object = MibTableColumn
acDs3ConfigFarEndFrameIDCode = _AcDs3ConfigFarEndFrameIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 34),
    _AcDs3ConfigFarEndFrameIDCode_Type()
)
acDs3ConfigFarEndFrameIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigFarEndFrameIDCode.setStatus("current")


class _AcDs3ConfigFarEndUnitCode_Type(DisplayString):
    """Custom type acDs3ConfigFarEndUnitCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AcDs3ConfigFarEndUnitCode_Type.__name__ = "DisplayString"
_AcDs3ConfigFarEndUnitCode_Object = MibTableColumn
acDs3ConfigFarEndUnitCode = _AcDs3ConfigFarEndUnitCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 35),
    _AcDs3ConfigFarEndUnitCode_Type()
)
acDs3ConfigFarEndUnitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigFarEndUnitCode.setStatus("current")


class _AcDs3ConfigFarEndFacilityIDCode_Type(DisplayString):
    """Custom type acDs3ConfigFarEndFacilityIDCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_AcDs3ConfigFarEndFacilityIDCode_Type.__name__ = "DisplayString"
_AcDs3ConfigFarEndFacilityIDCode_Object = MibTableColumn
acDs3ConfigFarEndFacilityIDCode = _AcDs3ConfigFarEndFacilityIDCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 36),
    _AcDs3ConfigFarEndFacilityIDCode_Type()
)
acDs3ConfigFarEndFacilityIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3ConfigFarEndFacilityIDCode.setStatus("current")


class _AcDs3ConfigInterfaceName_Type(DisplayString):
    """Custom type acDs3ConfigInterfaceName based on DisplayString"""
    defaultValue = OctetString("DS-3/TDM Interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcDs3ConfigInterfaceName_Type.__name__ = "DisplayString"
_AcDs3ConfigInterfaceName_Object = MibTableColumn
acDs3ConfigInterfaceName = _AcDs3ConfigInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 1, 1, 37),
    _AcDs3ConfigInterfaceName_Type()
)
acDs3ConfigInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acDs3ConfigInterfaceName.setStatus("current")
_AcDs3IntervalTable_Object = MibTable
acDs3IntervalTable = _AcDs3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    acDs3IntervalTable.setStatus("current")
_AcDs3IntervalEntry_Object = MibTableRow
acDs3IntervalEntry = _AcDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1)
)
acDs3IntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3IntervalNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3IntervalSlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3IntervalPort"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    acDs3IntervalEntry.setStatus("current")
_AcDs3IntervalNodeId_Type = AcNodeId
_AcDs3IntervalNodeId_Object = MibTableColumn
acDs3IntervalNodeId = _AcDs3IntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 1),
    _AcDs3IntervalNodeId_Type()
)
acDs3IntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3IntervalNodeId.setStatus("current")
_AcDs3IntervalSlot_Type = AcSlotNumber
_AcDs3IntervalSlot_Object = MibTableColumn
acDs3IntervalSlot = _AcDs3IntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 2),
    _AcDs3IntervalSlot_Type()
)
acDs3IntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3IntervalSlot.setStatus("current")
_AcDs3IntervalPort_Type = AcPortNumber
_AcDs3IntervalPort_Object = MibTableColumn
acDs3IntervalPort = _AcDs3IntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 3),
    _AcDs3IntervalPort_Type()
)
acDs3IntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3IntervalPort.setStatus("current")


class _AcDs3IntervalNumber_Type(Integer32):
    """Custom type acDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcDs3IntervalNumber_Type.__name__ = "Integer32"
_AcDs3IntervalNumber_Object = MibTableColumn
acDs3IntervalNumber = _AcDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 4),
    _AcDs3IntervalNumber_Type()
)
acDs3IntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3IntervalNumber.setStatus("current")
_AcDs3IntervalValidStats_Type = TruthValue
_AcDs3IntervalValidStats_Object = MibTableColumn
acDs3IntervalValidStats = _AcDs3IntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 5),
    _AcDs3IntervalValidStats_Type()
)
acDs3IntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalValidStats.setStatus("current")
_AcDs3IntervalResetStats_Type = TruthValue
_AcDs3IntervalResetStats_Object = MibTableColumn
acDs3IntervalResetStats = _AcDs3IntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 6),
    _AcDs3IntervalResetStats_Type()
)
acDs3IntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3IntervalResetStats.setStatus("current")
_AcDs3IntervalPESs_Type = PerfIntervalCount
_AcDs3IntervalPESs_Object = MibTableColumn
acDs3IntervalPESs = _AcDs3IntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 7),
    _AcDs3IntervalPESs_Type()
)
acDs3IntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalPESs.setStatus("current")
_AcDs3IntervalPSESs_Type = PerfIntervalCount
_AcDs3IntervalPSESs_Object = MibTableColumn
acDs3IntervalPSESs = _AcDs3IntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 8),
    _AcDs3IntervalPSESs_Type()
)
acDs3IntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalPSESs.setStatus("current")
_AcDs3IntervalSEFSs_Type = PerfIntervalCount
_AcDs3IntervalSEFSs_Object = MibTableColumn
acDs3IntervalSEFSs = _AcDs3IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 9),
    _AcDs3IntervalSEFSs_Type()
)
acDs3IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalSEFSs.setStatus("current")
_AcDs3IntervalUASs_Type = PerfIntervalCount
_AcDs3IntervalUASs_Object = MibTableColumn
acDs3IntervalUASs = _AcDs3IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 10),
    _AcDs3IntervalUASs_Type()
)
acDs3IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalUASs.setStatus("current")
_AcDs3IntervalLCVs_Type = PerfIntervalCount
_AcDs3IntervalLCVs_Object = MibTableColumn
acDs3IntervalLCVs = _AcDs3IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 11),
    _AcDs3IntervalLCVs_Type()
)
acDs3IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalLCVs.setStatus("current")
_AcDs3IntervalPCVs_Type = PerfIntervalCount
_AcDs3IntervalPCVs_Object = MibTableColumn
acDs3IntervalPCVs = _AcDs3IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 12),
    _AcDs3IntervalPCVs_Type()
)
acDs3IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalPCVs.setStatus("current")
_AcDs3IntervalLESs_Type = PerfIntervalCount
_AcDs3IntervalLESs_Object = MibTableColumn
acDs3IntervalLESs = _AcDs3IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 13),
    _AcDs3IntervalLESs_Type()
)
acDs3IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalLESs.setStatus("current")
_AcDs3IntervalCCVs_Type = PerfIntervalCount
_AcDs3IntervalCCVs_Object = MibTableColumn
acDs3IntervalCCVs = _AcDs3IntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 14),
    _AcDs3IntervalCCVs_Type()
)
acDs3IntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalCCVs.setStatus("current")
_AcDs3IntervalCESs_Type = PerfIntervalCount
_AcDs3IntervalCESs_Object = MibTableColumn
acDs3IntervalCESs = _AcDs3IntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 15),
    _AcDs3IntervalCESs_Type()
)
acDs3IntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalCESs.setStatus("current")
_AcDs3IntervalCSESs_Type = PerfIntervalCount
_AcDs3IntervalCSESs_Object = MibTableColumn
acDs3IntervalCSESs = _AcDs3IntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 2, 1, 16),
    _AcDs3IntervalCSESs_Type()
)
acDs3IntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3IntervalCSESs.setStatus("current")
_AcDs3DayTable_Object = MibTable
acDs3DayTable = _AcDs3DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3)
)
if mibBuilder.loadTexts:
    acDs3DayTable.setStatus("current")
_AcDs3DayEntry_Object = MibTableRow
acDs3DayEntry = _AcDs3DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1)
)
acDs3DayEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3DayNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3DaySlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3DayPort"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3DayNumber"),
)
if mibBuilder.loadTexts:
    acDs3DayEntry.setStatus("current")
_AcDs3DayNodeId_Type = AcNodeId
_AcDs3DayNodeId_Object = MibTableColumn
acDs3DayNodeId = _AcDs3DayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 1),
    _AcDs3DayNodeId_Type()
)
acDs3DayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3DayNodeId.setStatus("current")
_AcDs3DaySlot_Type = AcSlotNumber
_AcDs3DaySlot_Object = MibTableColumn
acDs3DaySlot = _AcDs3DaySlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 2),
    _AcDs3DaySlot_Type()
)
acDs3DaySlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3DaySlot.setStatus("current")
_AcDs3DayPort_Type = AcPortNumber
_AcDs3DayPort_Object = MibTableColumn
acDs3DayPort = _AcDs3DayPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 3),
    _AcDs3DayPort_Type()
)
acDs3DayPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3DayPort.setStatus("current")


class _AcDs3DayNumber_Type(Integer32):
    """Custom type acDs3DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcDs3DayNumber_Type.__name__ = "Integer32"
_AcDs3DayNumber_Object = MibTableColumn
acDs3DayNumber = _AcDs3DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 4),
    _AcDs3DayNumber_Type()
)
acDs3DayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3DayNumber.setStatus("current")
_AcDs3DayValidStats_Type = TruthValue
_AcDs3DayValidStats_Object = MibTableColumn
acDs3DayValidStats = _AcDs3DayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 5),
    _AcDs3DayValidStats_Type()
)
acDs3DayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayValidStats.setStatus("current")
_AcDs3DayResetStats_Type = TruthValue
_AcDs3DayResetStats_Object = MibTableColumn
acDs3DayResetStats = _AcDs3DayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 6),
    _AcDs3DayResetStats_Type()
)
acDs3DayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3DayResetStats.setStatus("current")
_AcDs3DayPESs_Type = PerfIntervalCount
_AcDs3DayPESs_Object = MibTableColumn
acDs3DayPESs = _AcDs3DayPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 7),
    _AcDs3DayPESs_Type()
)
acDs3DayPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayPESs.setStatus("current")
_AcDs3DayPSESs_Type = PerfIntervalCount
_AcDs3DayPSESs_Object = MibTableColumn
acDs3DayPSESs = _AcDs3DayPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 8),
    _AcDs3DayPSESs_Type()
)
acDs3DayPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayPSESs.setStatus("current")
_AcDs3DaySEFSs_Type = PerfIntervalCount
_AcDs3DaySEFSs_Object = MibTableColumn
acDs3DaySEFSs = _AcDs3DaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 9),
    _AcDs3DaySEFSs_Type()
)
acDs3DaySEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DaySEFSs.setStatus("current")
_AcDs3DayUASs_Type = PerfIntervalCount
_AcDs3DayUASs_Object = MibTableColumn
acDs3DayUASs = _AcDs3DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 10),
    _AcDs3DayUASs_Type()
)
acDs3DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayUASs.setStatus("current")
_AcDs3DayLCVs_Type = PerfIntervalCount
_AcDs3DayLCVs_Object = MibTableColumn
acDs3DayLCVs = _AcDs3DayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 11),
    _AcDs3DayLCVs_Type()
)
acDs3DayLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayLCVs.setStatus("current")
_AcDs3DayPCVs_Type = PerfIntervalCount
_AcDs3DayPCVs_Object = MibTableColumn
acDs3DayPCVs = _AcDs3DayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 12),
    _AcDs3DayPCVs_Type()
)
acDs3DayPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayPCVs.setStatus("current")
_AcDs3DayLESs_Type = PerfIntervalCount
_AcDs3DayLESs_Object = MibTableColumn
acDs3DayLESs = _AcDs3DayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 13),
    _AcDs3DayLESs_Type()
)
acDs3DayLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayLESs.setStatus("current")
_AcDs3DayCCVs_Type = PerfIntervalCount
_AcDs3DayCCVs_Object = MibTableColumn
acDs3DayCCVs = _AcDs3DayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 14),
    _AcDs3DayCCVs_Type()
)
acDs3DayCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayCCVs.setStatus("current")
_AcDs3DayCESs_Type = PerfIntervalCount
_AcDs3DayCESs_Object = MibTableColumn
acDs3DayCESs = _AcDs3DayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 15),
    _AcDs3DayCESs_Type()
)
acDs3DayCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayCESs.setStatus("current")
_AcDs3DayCSESs_Type = PerfIntervalCount
_AcDs3DayCSESs_Object = MibTableColumn
acDs3DayCSESs = _AcDs3DayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 3, 1, 16),
    _AcDs3DayCSESs_Type()
)
acDs3DayCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3DayCSESs.setStatus("current")
_AcDs3FarEndIntervalTable_Object = MibTable
acDs3FarEndIntervalTable = _AcDs3FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4)
)
if mibBuilder.loadTexts:
    acDs3FarEndIntervalTable.setStatus("current")
_AcDs3FarEndIntervalEntry_Object = MibTableRow
acDs3FarEndIntervalEntry = _AcDs3FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1)
)
acDs3FarEndIntervalEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndIntervalNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndIntervalSlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndIntervalPort"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    acDs3FarEndIntervalEntry.setStatus("current")
_AcDs3FarEndIntervalNodeId_Type = AcNodeId
_AcDs3FarEndIntervalNodeId_Object = MibTableColumn
acDs3FarEndIntervalNodeId = _AcDs3FarEndIntervalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 1),
    _AcDs3FarEndIntervalNodeId_Type()
)
acDs3FarEndIntervalNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalNodeId.setStatus("current")
_AcDs3FarEndIntervalSlot_Type = AcSlotNumber
_AcDs3FarEndIntervalSlot_Object = MibTableColumn
acDs3FarEndIntervalSlot = _AcDs3FarEndIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 2),
    _AcDs3FarEndIntervalSlot_Type()
)
acDs3FarEndIntervalSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalSlot.setStatus("current")
_AcDs3FarEndIntervalPort_Type = AcPortNumber
_AcDs3FarEndIntervalPort_Object = MibTableColumn
acDs3FarEndIntervalPort = _AcDs3FarEndIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 3),
    _AcDs3FarEndIntervalPort_Type()
)
acDs3FarEndIntervalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalPort.setStatus("current")


class _AcDs3FarEndIntervalNumber_Type(Integer32):
    """Custom type acDs3FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 98),
    )


_AcDs3FarEndIntervalNumber_Type.__name__ = "Integer32"
_AcDs3FarEndIntervalNumber_Object = MibTableColumn
acDs3FarEndIntervalNumber = _AcDs3FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 4),
    _AcDs3FarEndIntervalNumber_Type()
)
acDs3FarEndIntervalNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalNumber.setStatus("current")
_AcDs3FarEndIntervalValidStats_Type = TruthValue
_AcDs3FarEndIntervalValidStats_Object = MibTableColumn
acDs3FarEndIntervalValidStats = _AcDs3FarEndIntervalValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 5),
    _AcDs3FarEndIntervalValidStats_Type()
)
acDs3FarEndIntervalValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalValidStats.setStatus("current")
_AcDs3FarEndIntervalResetStats_Type = TruthValue
_AcDs3FarEndIntervalResetStats_Object = MibTableColumn
acDs3FarEndIntervalResetStats = _AcDs3FarEndIntervalResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 6),
    _AcDs3FarEndIntervalResetStats_Type()
)
acDs3FarEndIntervalResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalResetStats.setStatus("current")
_AcDs3FarEndIntervalCESs_Type = PerfIntervalCount
_AcDs3FarEndIntervalCESs_Object = MibTableColumn
acDs3FarEndIntervalCESs = _AcDs3FarEndIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 7),
    _AcDs3FarEndIntervalCESs_Type()
)
acDs3FarEndIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalCESs.setStatus("current")
_AcDs3FarEndIntervalCSESs_Type = PerfIntervalCount
_AcDs3FarEndIntervalCSESs_Object = MibTableColumn
acDs3FarEndIntervalCSESs = _AcDs3FarEndIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 8),
    _AcDs3FarEndIntervalCSESs_Type()
)
acDs3FarEndIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalCSESs.setStatus("current")
_AcDs3FarEndIntervalCCVs_Type = PerfIntervalCount
_AcDs3FarEndIntervalCCVs_Object = MibTableColumn
acDs3FarEndIntervalCCVs = _AcDs3FarEndIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 9),
    _AcDs3FarEndIntervalCCVs_Type()
)
acDs3FarEndIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalCCVs.setStatus("current")
_AcDs3FarEndIntervalUASs_Type = PerfIntervalCount
_AcDs3FarEndIntervalUASs_Object = MibTableColumn
acDs3FarEndIntervalUASs = _AcDs3FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 4, 1, 10),
    _AcDs3FarEndIntervalUASs_Type()
)
acDs3FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndIntervalUASs.setStatus("current")
_AcDs3FarEndDayTable_Object = MibTable
acDs3FarEndDayTable = _AcDs3FarEndDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5)
)
if mibBuilder.loadTexts:
    acDs3FarEndDayTable.setStatus("current")
_AcDs3FarEndDayEntry_Object = MibTableRow
acDs3FarEndDayEntry = _AcDs3FarEndDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1)
)
acDs3FarEndDayEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndDayNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndDaySlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndDayPort"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3FarEndDayNumber"),
)
if mibBuilder.loadTexts:
    acDs3FarEndDayEntry.setStatus("current")
_AcDs3FarEndDayNodeId_Type = AcNodeId
_AcDs3FarEndDayNodeId_Object = MibTableColumn
acDs3FarEndDayNodeId = _AcDs3FarEndDayNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 1),
    _AcDs3FarEndDayNodeId_Type()
)
acDs3FarEndDayNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndDayNodeId.setStatus("current")
_AcDs3FarEndDaySlot_Type = AcSlotNumber
_AcDs3FarEndDaySlot_Object = MibTableColumn
acDs3FarEndDaySlot = _AcDs3FarEndDaySlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 2),
    _AcDs3FarEndDaySlot_Type()
)
acDs3FarEndDaySlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndDaySlot.setStatus("current")
_AcDs3FarEndDayPort_Type = AcPortNumber
_AcDs3FarEndDayPort_Object = MibTableColumn
acDs3FarEndDayPort = _AcDs3FarEndDayPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 3),
    _AcDs3FarEndDayPort_Type()
)
acDs3FarEndDayPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndDayPort.setStatus("current")


class _AcDs3FarEndDayNumber_Type(Integer32):
    """Custom type acDs3FarEndDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcDs3FarEndDayNumber_Type.__name__ = "Integer32"
_AcDs3FarEndDayNumber_Object = MibTableColumn
acDs3FarEndDayNumber = _AcDs3FarEndDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 4),
    _AcDs3FarEndDayNumber_Type()
)
acDs3FarEndDayNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3FarEndDayNumber.setStatus("current")
_AcDs3FarEndDayValidStats_Type = TruthValue
_AcDs3FarEndDayValidStats_Object = MibTableColumn
acDs3FarEndDayValidStats = _AcDs3FarEndDayValidStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 5),
    _AcDs3FarEndDayValidStats_Type()
)
acDs3FarEndDayValidStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndDayValidStats.setStatus("current")
_AcDs3FarEndDayResetStats_Type = TruthValue
_AcDs3FarEndDayResetStats_Object = MibTableColumn
acDs3FarEndDayResetStats = _AcDs3FarEndDayResetStats_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 6),
    _AcDs3FarEndDayResetStats_Type()
)
acDs3FarEndDayResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3FarEndDayResetStats.setStatus("current")
_AcDs3FarEndDayCESs_Type = PerfIntervalCount
_AcDs3FarEndDayCESs_Object = MibTableColumn
acDs3FarEndDayCESs = _AcDs3FarEndDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 7),
    _AcDs3FarEndDayCESs_Type()
)
acDs3FarEndDayCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndDayCESs.setStatus("current")
_AcDs3FarEndDayCSESs_Type = PerfIntervalCount
_AcDs3FarEndDayCSESs_Object = MibTableColumn
acDs3FarEndDayCSESs = _AcDs3FarEndDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 8),
    _AcDs3FarEndDayCSESs_Type()
)
acDs3FarEndDayCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndDayCSESs.setStatus("current")
_AcDs3FarEndDayCCVs_Type = PerfIntervalCount
_AcDs3FarEndDayCCVs_Object = MibTableColumn
acDs3FarEndDayCCVs = _AcDs3FarEndDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 9),
    _AcDs3FarEndDayCCVs_Type()
)
acDs3FarEndDayCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndDayCCVs.setStatus("current")
_AcDs3FarEndDayUASs_Type = PerfIntervalCount
_AcDs3FarEndDayUASs_Object = MibTableColumn
acDs3FarEndDayUASs = _AcDs3FarEndDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 5, 1, 10),
    _AcDs3FarEndDayUASs_Type()
)
acDs3FarEndDayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDs3FarEndDayUASs.setStatus("current")
_AcDs3ThresholdTable_Object = MibTable
acDs3ThresholdTable = _AcDs3ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6)
)
if mibBuilder.loadTexts:
    acDs3ThresholdTable.setStatus("current")
_AcDs3ThresholdEntry_Object = MibTableRow
acDs3ThresholdEntry = _AcDs3ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1)
)
acDs3ThresholdEntry.setIndexNames(
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
    (0, "APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"),
)
if mibBuilder.loadTexts:
    acDs3ThresholdEntry.setStatus("current")
_AcDs3ThresholdNodeId_Type = AcNodeId
_AcDs3ThresholdNodeId_Object = MibTableColumn
acDs3ThresholdNodeId = _AcDs3ThresholdNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 1),
    _AcDs3ThresholdNodeId_Type()
)
acDs3ThresholdNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ThresholdNodeId.setStatus("current")
_AcDs3ThresholdSlot_Type = AcSlotNumber
_AcDs3ThresholdSlot_Object = MibTableColumn
acDs3ThresholdSlot = _AcDs3ThresholdSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 2),
    _AcDs3ThresholdSlot_Type()
)
acDs3ThresholdSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ThresholdSlot.setStatus("current")
_AcDs3ThresholdPort_Type = AcPortNumber
_AcDs3ThresholdPort_Object = MibTableColumn
acDs3ThresholdPort = _AcDs3ThresholdPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 3),
    _AcDs3ThresholdPort_Type()
)
acDs3ThresholdPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acDs3ThresholdPort.setStatus("current")


class _AcDs3ThresholdNEIntervalPESs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalPESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalPESs_Object = MibTableColumn
acDs3ThresholdNEIntervalPESs = _AcDs3ThresholdNEIntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 4),
    _AcDs3ThresholdNEIntervalPESs_Type()
)
acDs3ThresholdNEIntervalPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalPESs.setStatus("current")


class _AcDs3ThresholdNEIntervalPSESs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalPSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalPSESs_Object = MibTableColumn
acDs3ThresholdNEIntervalPSESs = _AcDs3ThresholdNEIntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 5),
    _AcDs3ThresholdNEIntervalPSESs_Type()
)
acDs3ThresholdNEIntervalPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalPSESs.setStatus("current")


class _AcDs3ThresholdNEIntervalSEFSs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalSEFSs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalSEFSs_Object = MibTableColumn
acDs3ThresholdNEIntervalSEFSs = _AcDs3ThresholdNEIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 6),
    _AcDs3ThresholdNEIntervalSEFSs_Type()
)
acDs3ThresholdNEIntervalSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalSEFSs.setStatus("current")


class _AcDs3ThresholdNEIntervalUASs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalUASs_Object = MibTableColumn
acDs3ThresholdNEIntervalUASs = _AcDs3ThresholdNEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 7),
    _AcDs3ThresholdNEIntervalUASs_Type()
)
acDs3ThresholdNEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalUASs.setStatus("current")


class _AcDs3ThresholdNEIntervalLCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalLCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalLCVs_Object = MibTableColumn
acDs3ThresholdNEIntervalLCVs = _AcDs3ThresholdNEIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 8),
    _AcDs3ThresholdNEIntervalLCVs_Type()
)
acDs3ThresholdNEIntervalLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalLCVs.setStatus("current")


class _AcDs3ThresholdNEIntervalPCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalPCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalPCVs_Object = MibTableColumn
acDs3ThresholdNEIntervalPCVs = _AcDs3ThresholdNEIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 9),
    _AcDs3ThresholdNEIntervalPCVs_Type()
)
acDs3ThresholdNEIntervalPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalPCVs.setStatus("current")


class _AcDs3ThresholdNEIntervalLESs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalLESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalLESs_Object = MibTableColumn
acDs3ThresholdNEIntervalLESs = _AcDs3ThresholdNEIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 10),
    _AcDs3ThresholdNEIntervalLESs_Type()
)
acDs3ThresholdNEIntervalLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalLESs.setStatus("current")


class _AcDs3ThresholdNEIntervalCCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalCCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalCCVs_Object = MibTableColumn
acDs3ThresholdNEIntervalCCVs = _AcDs3ThresholdNEIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 11),
    _AcDs3ThresholdNEIntervalCCVs_Type()
)
acDs3ThresholdNEIntervalCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalCCVs.setStatus("current")


class _AcDs3ThresholdNEIntervalCESs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalCESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalCESs_Object = MibTableColumn
acDs3ThresholdNEIntervalCESs = _AcDs3ThresholdNEIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 12),
    _AcDs3ThresholdNEIntervalCESs_Type()
)
acDs3ThresholdNEIntervalCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalCESs.setStatus("current")


class _AcDs3ThresholdNEIntervalCSESs_Type(Integer32):
    """Custom type acDs3ThresholdNEIntervalCSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEIntervalCSESs_Object = MibTableColumn
acDs3ThresholdNEIntervalCSESs = _AcDs3ThresholdNEIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 13),
    _AcDs3ThresholdNEIntervalCSESs_Type()
)
acDs3ThresholdNEIntervalCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEIntervalCSESs.setStatus("current")


class _AcDs3ThresholdNEDayPESs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayPESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayPESs_Object = MibTableColumn
acDs3ThresholdNEDayPESs = _AcDs3ThresholdNEDayPESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 14),
    _AcDs3ThresholdNEDayPESs_Type()
)
acDs3ThresholdNEDayPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayPESs.setStatus("current")


class _AcDs3ThresholdNEDayPSESs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayPSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayPSESs_Object = MibTableColumn
acDs3ThresholdNEDayPSESs = _AcDs3ThresholdNEDayPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 15),
    _AcDs3ThresholdNEDayPSESs_Type()
)
acDs3ThresholdNEDayPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayPSESs.setStatus("current")


class _AcDs3ThresholdNEDaySEFSs_Type(Integer32):
    """Custom type acDs3ThresholdNEDaySEFSs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDaySEFSs_Object = MibTableColumn
acDs3ThresholdNEDaySEFSs = _AcDs3ThresholdNEDaySEFSs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 16),
    _AcDs3ThresholdNEDaySEFSs_Type()
)
acDs3ThresholdNEDaySEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDaySEFSs.setStatus("current")


class _AcDs3ThresholdNEDayUASs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayUASs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayUASs_Object = MibTableColumn
acDs3ThresholdNEDayUASs = _AcDs3ThresholdNEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 17),
    _AcDs3ThresholdNEDayUASs_Type()
)
acDs3ThresholdNEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayUASs.setStatus("current")


class _AcDs3ThresholdNEDayLCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayLCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayLCVs_Object = MibTableColumn
acDs3ThresholdNEDayLCVs = _AcDs3ThresholdNEDayLCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 18),
    _AcDs3ThresholdNEDayLCVs_Type()
)
acDs3ThresholdNEDayLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayLCVs.setStatus("current")


class _AcDs3ThresholdNEDayPCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayPCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayPCVs_Object = MibTableColumn
acDs3ThresholdNEDayPCVs = _AcDs3ThresholdNEDayPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 19),
    _AcDs3ThresholdNEDayPCVs_Type()
)
acDs3ThresholdNEDayPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayPCVs.setStatus("current")


class _AcDs3ThresholdNEDayLESs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayLESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayLESs_Object = MibTableColumn
acDs3ThresholdNEDayLESs = _AcDs3ThresholdNEDayLESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 20),
    _AcDs3ThresholdNEDayLESs_Type()
)
acDs3ThresholdNEDayLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayLESs.setStatus("current")


class _AcDs3ThresholdNEDayCCVs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayCCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayCCVs_Object = MibTableColumn
acDs3ThresholdNEDayCCVs = _AcDs3ThresholdNEDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 21),
    _AcDs3ThresholdNEDayCCVs_Type()
)
acDs3ThresholdNEDayCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayCCVs.setStatus("current")


class _AcDs3ThresholdNEDayCESs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayCESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayCESs_Object = MibTableColumn
acDs3ThresholdNEDayCESs = _AcDs3ThresholdNEDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 22),
    _AcDs3ThresholdNEDayCESs_Type()
)
acDs3ThresholdNEDayCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayCESs.setStatus("current")


class _AcDs3ThresholdNEDayCSESs_Type(Integer32):
    """Custom type acDs3ThresholdNEDayCSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdNEDayCSESs_Object = MibTableColumn
acDs3ThresholdNEDayCSESs = _AcDs3ThresholdNEDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 23),
    _AcDs3ThresholdNEDayCSESs_Type()
)
acDs3ThresholdNEDayCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdNEDayCSESs.setStatus("current")


class _AcDs3ThresholdFEIntervalCESs_Type(Integer32):
    """Custom type acDs3ThresholdFEIntervalCESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEIntervalCESs_Object = MibTableColumn
acDs3ThresholdFEIntervalCESs = _AcDs3ThresholdFEIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 24),
    _AcDs3ThresholdFEIntervalCESs_Type()
)
acDs3ThresholdFEIntervalCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEIntervalCESs.setStatus("current")


class _AcDs3ThresholdFEIntervalCSESs_Type(Integer32):
    """Custom type acDs3ThresholdFEIntervalCSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEIntervalCSESs_Object = MibTableColumn
acDs3ThresholdFEIntervalCSESs = _AcDs3ThresholdFEIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 25),
    _AcDs3ThresholdFEIntervalCSESs_Type()
)
acDs3ThresholdFEIntervalCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEIntervalCSESs.setStatus("current")


class _AcDs3ThresholdFEIntervalCCVs_Type(Integer32):
    """Custom type acDs3ThresholdFEIntervalCCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEIntervalCCVs_Object = MibTableColumn
acDs3ThresholdFEIntervalCCVs = _AcDs3ThresholdFEIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 26),
    _AcDs3ThresholdFEIntervalCCVs_Type()
)
acDs3ThresholdFEIntervalCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEIntervalCCVs.setStatus("current")


class _AcDs3ThresholdFEIntervalUASs_Type(Integer32):
    """Custom type acDs3ThresholdFEIntervalUASs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEIntervalUASs_Object = MibTableColumn
acDs3ThresholdFEIntervalUASs = _AcDs3ThresholdFEIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 27),
    _AcDs3ThresholdFEIntervalUASs_Type()
)
acDs3ThresholdFEIntervalUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEIntervalUASs.setStatus("current")


class _AcDs3ThresholdFEDayCESs_Type(Integer32):
    """Custom type acDs3ThresholdFEDayCESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEDayCESs_Object = MibTableColumn
acDs3ThresholdFEDayCESs = _AcDs3ThresholdFEDayCESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 28),
    _AcDs3ThresholdFEDayCESs_Type()
)
acDs3ThresholdFEDayCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEDayCESs.setStatus("current")


class _AcDs3ThresholdFEDayCSESs_Type(Integer32):
    """Custom type acDs3ThresholdFEDayCSESs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEDayCSESs_Object = MibTableColumn
acDs3ThresholdFEDayCSESs = _AcDs3ThresholdFEDayCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 29),
    _AcDs3ThresholdFEDayCSESs_Type()
)
acDs3ThresholdFEDayCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEDayCSESs.setStatus("current")


class _AcDs3ThresholdFEDayCCVs_Type(Integer32):
    """Custom type acDs3ThresholdFEDayCCVs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEDayCCVs_Object = MibTableColumn
acDs3ThresholdFEDayCCVs = _AcDs3ThresholdFEDayCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 30),
    _AcDs3ThresholdFEDayCCVs_Type()
)
acDs3ThresholdFEDayCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEDayCCVs.setStatus("current")


class _AcDs3ThresholdFEDayUASs_Type(Integer32):
    """Custom type acDs3ThresholdFEDayUASs based on Integer32"""
    defaultValue = 0


_AcDs3ThresholdFEDayUASs_Object = MibTableColumn
acDs3ThresholdFEDayUASs = _AcDs3ThresholdFEDayUASs_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 6, 1, 31),
    _AcDs3ThresholdFEDayUASs_Type()
)
acDs3ThresholdFEDayUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDs3ThresholdFEDayUASs.setStatus("current")

# Managed Objects groups


# Notification objects

acDs3LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 1)
)
acDs3LineStatusChange.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigLineStatus"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigLineStatusLastChange"))
)
if mibBuilder.loadTexts:
    acDs3LineStatusChange.setStatus(
        "current"
    )

acDs3StatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 2)
)
acDs3StatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs3StatsResetTrap.setStatus(
        "current"
    )

acDs3CfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 3)
)
acDs3CfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs3CfgErrorTrap.setStatus(
        "current"
    )

acDs3LinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 4)
)
acDs3LinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs3LinkDownTrap.setStatus(
        "current"
    )

acDs3LinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 5)
)
acDs3LinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ConfigPort"))
)
if mibBuilder.loadTexts:
    acDs3LinkUpTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalPESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 6)
)
acDs3ExceededThresholdNEIntervalPESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalPESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalPSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 7)
)
acDs3ExceededThresholdNEIntervalPSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalPSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalSEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 8)
)
acDs3ExceededThresholdNEIntervalSEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalSEFSsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 9)
)
acDs3ExceededThresholdNEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalUASsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 10)
)
acDs3ExceededThresholdNEIntervalLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalLCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 11)
)
acDs3ExceededThresholdNEIntervalPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalPCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 12)
)
acDs3ExceededThresholdNEIntervalLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalLESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 13)
)
acDs3ExceededThresholdNEIntervalCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalCCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 14)
)
acDs3ExceededThresholdNEIntervalCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalCESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEIntervalCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 15)
)
acDs3ExceededThresholdNEIntervalCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEIntervalCSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayPESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 16)
)
acDs3ExceededThresholdNEDayPESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayPESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayPSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 17)
)
acDs3ExceededThresholdNEDayPSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayPSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDaySEFSsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 18)
)
acDs3ExceededThresholdNEDaySEFSsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDaySEFSsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 19)
)
acDs3ExceededThresholdNEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayUASsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayLCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 20)
)
acDs3ExceededThresholdNEDayLCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayLCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayPCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 21)
)
acDs3ExceededThresholdNEDayPCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayPCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayLESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 22)
)
acDs3ExceededThresholdNEDayLESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayLESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 23)
)
acDs3ExceededThresholdNEDayCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayCCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 24)
)
acDs3ExceededThresholdNEDayCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayCESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdNEDayCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 25)
)
acDs3ExceededThresholdNEDayCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdNEDayCSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEIntervalCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 26)
)
acDs3ExceededThresholdFEIntervalCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEIntervalCESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEIntervalCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 27)
)
acDs3ExceededThresholdFEIntervalCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEIntervalCSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEIntervalCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 28)
)
acDs3ExceededThresholdFEIntervalCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEIntervalCCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEIntervalUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 29)
)
acDs3ExceededThresholdFEIntervalUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEIntervalUASsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEDayCESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 30)
)
acDs3ExceededThresholdFEDayCESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEDayCESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEDayCSESsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 31)
)
acDs3ExceededThresholdFEDayCSESsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEDayCSESsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEDayCCVsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 32)
)
acDs3ExceededThresholdFEDayCCVsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEDayCCVsTrap.setStatus(
        "current"
    )

acDs3ExceededThresholdFEDayUASsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 5, 0, 33)
)
acDs3ExceededThresholdFEDayUASsTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdNodeId"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdSlot"),
        ("APPIAN-PPORT-DS3-MIB", "acDs3ThresholdPort"))
)
if mibBuilder.loadTexts:
    acDs3ExceededThresholdFEDayUASsTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-DS3-MIB",
    **{"acDs3": acDs3,
       "acDs3Traps": acDs3Traps,
       "acDs3LineStatusChange": acDs3LineStatusChange,
       "acDs3StatsResetTrap": acDs3StatsResetTrap,
       "acDs3CfgErrorTrap": acDs3CfgErrorTrap,
       "acDs3LinkDownTrap": acDs3LinkDownTrap,
       "acDs3LinkUpTrap": acDs3LinkUpTrap,
       "acDs3ExceededThresholdNEIntervalPESsTrap": acDs3ExceededThresholdNEIntervalPESsTrap,
       "acDs3ExceededThresholdNEIntervalPSESsTrap": acDs3ExceededThresholdNEIntervalPSESsTrap,
       "acDs3ExceededThresholdNEIntervalSEFSsTrap": acDs3ExceededThresholdNEIntervalSEFSsTrap,
       "acDs3ExceededThresholdNEIntervalUASsTrap": acDs3ExceededThresholdNEIntervalUASsTrap,
       "acDs3ExceededThresholdNEIntervalLCVsTrap": acDs3ExceededThresholdNEIntervalLCVsTrap,
       "acDs3ExceededThresholdNEIntervalPCVsTrap": acDs3ExceededThresholdNEIntervalPCVsTrap,
       "acDs3ExceededThresholdNEIntervalLESsTrap": acDs3ExceededThresholdNEIntervalLESsTrap,
       "acDs3ExceededThresholdNEIntervalCCVsTrap": acDs3ExceededThresholdNEIntervalCCVsTrap,
       "acDs3ExceededThresholdNEIntervalCESsTrap": acDs3ExceededThresholdNEIntervalCESsTrap,
       "acDs3ExceededThresholdNEIntervalCSESsTrap": acDs3ExceededThresholdNEIntervalCSESsTrap,
       "acDs3ExceededThresholdNEDayPESsTrap": acDs3ExceededThresholdNEDayPESsTrap,
       "acDs3ExceededThresholdNEDayPSESsTrap": acDs3ExceededThresholdNEDayPSESsTrap,
       "acDs3ExceededThresholdNEDaySEFSsTrap": acDs3ExceededThresholdNEDaySEFSsTrap,
       "acDs3ExceededThresholdNEDayUASsTrap": acDs3ExceededThresholdNEDayUASsTrap,
       "acDs3ExceededThresholdNEDayLCVsTrap": acDs3ExceededThresholdNEDayLCVsTrap,
       "acDs3ExceededThresholdNEDayPCVsTrap": acDs3ExceededThresholdNEDayPCVsTrap,
       "acDs3ExceededThresholdNEDayLESsTrap": acDs3ExceededThresholdNEDayLESsTrap,
       "acDs3ExceededThresholdNEDayCCVsTrap": acDs3ExceededThresholdNEDayCCVsTrap,
       "acDs3ExceededThresholdNEDayCESsTrap": acDs3ExceededThresholdNEDayCESsTrap,
       "acDs3ExceededThresholdNEDayCSESsTrap": acDs3ExceededThresholdNEDayCSESsTrap,
       "acDs3ExceededThresholdFEIntervalCESsTrap": acDs3ExceededThresholdFEIntervalCESsTrap,
       "acDs3ExceededThresholdFEIntervalCSESsTrap": acDs3ExceededThresholdFEIntervalCSESsTrap,
       "acDs3ExceededThresholdFEIntervalCCVsTrap": acDs3ExceededThresholdFEIntervalCCVsTrap,
       "acDs3ExceededThresholdFEIntervalUASsTrap": acDs3ExceededThresholdFEIntervalUASsTrap,
       "acDs3ExceededThresholdFEDayCESsTrap": acDs3ExceededThresholdFEDayCESsTrap,
       "acDs3ExceededThresholdFEDayCSESsTrap": acDs3ExceededThresholdFEDayCSESsTrap,
       "acDs3ExceededThresholdFEDayCCVsTrap": acDs3ExceededThresholdFEDayCCVsTrap,
       "acDs3ExceededThresholdFEDayUASsTrap": acDs3ExceededThresholdFEDayUASsTrap,
       "acDs3ConfigTable": acDs3ConfigTable,
       "acDs3ConfigEntry": acDs3ConfigEntry,
       "acDs3ConfigNodeId": acDs3ConfigNodeId,
       "acDs3ConfigSlot": acDs3ConfigSlot,
       "acDs3ConfigPort": acDs3ConfigPort,
       "acDs3ConfigAdminStatus": acDs3ConfigAdminStatus,
       "acDs3ConfigOpStatus": acDs3ConfigOpStatus,
       "acDs3ConfigType": acDs3ConfigType,
       "acDs3ConfigTimeElapsedInterval": acDs3ConfigTimeElapsedInterval,
       "acDs3ConfigValidIntervals": acDs3ConfigValidIntervals,
       "acDs3ConfigTimeElapsedDay": acDs3ConfigTimeElapsedDay,
       "acDs3ConfigValidDays": acDs3ConfigValidDays,
       "acDs3ConfigTimeElapsedFarEndInterval": acDs3ConfigTimeElapsedFarEndInterval,
       "acDs3ConfigValidFarEndIntervals": acDs3ConfigValidFarEndIntervals,
       "acDs3ConfigTimeElapsedFarEndDay": acDs3ConfigTimeElapsedFarEndDay,
       "acDs3ConfigValidFarEndDays": acDs3ConfigValidFarEndDays,
       "acDs3ConfigLineType": acDs3ConfigLineType,
       "acDs3ConfigLineCoding": acDs3ConfigLineCoding,
       "acDs3ConfigSendCode": acDs3ConfigSendCode,
       "acDs3ConfigCircuitIdentifier": acDs3ConfigCircuitIdentifier,
       "acDs3ConfigLoopbackConfig": acDs3ConfigLoopbackConfig,
       "acDs3ConfigLineStatus": acDs3ConfigLineStatus,
       "acDs3ConfigTransmitClockSource": acDs3ConfigTransmitClockSource,
       "acDs3ConfigInvalidIntervals": acDs3ConfigInvalidIntervals,
       "acDs3ConfigInvalidDays": acDs3ConfigInvalidDays,
       "acDs3ConfigInvalidFarEndIntervals": acDs3ConfigInvalidFarEndIntervals,
       "acDs3ConfigInvalidFarEndDays": acDs3ConfigInvalidFarEndDays,
       "acDs3ConfigLineLength": acDs3ConfigLineLength,
       "acDs3ConfigLineStatusLastChange": acDs3ConfigLineStatusLastChange,
       "acDs3ConfigLineStatusChangeTrapEnable": acDs3ConfigLineStatusChangeTrapEnable,
       "acDs3ConfigLoopbackStatus": acDs3ConfigLoopbackStatus,
       "acDs3ConfigChannelization": acDs3ConfigChannelization,
       "acDs3ConfigDs1ForRemoteLoop": acDs3ConfigDs1ForRemoteLoop,
       "acDs3ConfigFarEndEquipCode": acDs3ConfigFarEndEquipCode,
       "acDs3ConfigFarEndLocationIDCode": acDs3ConfigFarEndLocationIDCode,
       "acDs3ConfigFarEndFrameIDCode": acDs3ConfigFarEndFrameIDCode,
       "acDs3ConfigFarEndUnitCode": acDs3ConfigFarEndUnitCode,
       "acDs3ConfigFarEndFacilityIDCode": acDs3ConfigFarEndFacilityIDCode,
       "acDs3ConfigInterfaceName": acDs3ConfigInterfaceName,
       "acDs3IntervalTable": acDs3IntervalTable,
       "acDs3IntervalEntry": acDs3IntervalEntry,
       "acDs3IntervalNodeId": acDs3IntervalNodeId,
       "acDs3IntervalSlot": acDs3IntervalSlot,
       "acDs3IntervalPort": acDs3IntervalPort,
       "acDs3IntervalNumber": acDs3IntervalNumber,
       "acDs3IntervalValidStats": acDs3IntervalValidStats,
       "acDs3IntervalResetStats": acDs3IntervalResetStats,
       "acDs3IntervalPESs": acDs3IntervalPESs,
       "acDs3IntervalPSESs": acDs3IntervalPSESs,
       "acDs3IntervalSEFSs": acDs3IntervalSEFSs,
       "acDs3IntervalUASs": acDs3IntervalUASs,
       "acDs3IntervalLCVs": acDs3IntervalLCVs,
       "acDs3IntervalPCVs": acDs3IntervalPCVs,
       "acDs3IntervalLESs": acDs3IntervalLESs,
       "acDs3IntervalCCVs": acDs3IntervalCCVs,
       "acDs3IntervalCESs": acDs3IntervalCESs,
       "acDs3IntervalCSESs": acDs3IntervalCSESs,
       "acDs3DayTable": acDs3DayTable,
       "acDs3DayEntry": acDs3DayEntry,
       "acDs3DayNodeId": acDs3DayNodeId,
       "acDs3DaySlot": acDs3DaySlot,
       "acDs3DayPort": acDs3DayPort,
       "acDs3DayNumber": acDs3DayNumber,
       "acDs3DayValidStats": acDs3DayValidStats,
       "acDs3DayResetStats": acDs3DayResetStats,
       "acDs3DayPESs": acDs3DayPESs,
       "acDs3DayPSESs": acDs3DayPSESs,
       "acDs3DaySEFSs": acDs3DaySEFSs,
       "acDs3DayUASs": acDs3DayUASs,
       "acDs3DayLCVs": acDs3DayLCVs,
       "acDs3DayPCVs": acDs3DayPCVs,
       "acDs3DayLESs": acDs3DayLESs,
       "acDs3DayCCVs": acDs3DayCCVs,
       "acDs3DayCESs": acDs3DayCESs,
       "acDs3DayCSESs": acDs3DayCSESs,
       "acDs3FarEndIntervalTable": acDs3FarEndIntervalTable,
       "acDs3FarEndIntervalEntry": acDs3FarEndIntervalEntry,
       "acDs3FarEndIntervalNodeId": acDs3FarEndIntervalNodeId,
       "acDs3FarEndIntervalSlot": acDs3FarEndIntervalSlot,
       "acDs3FarEndIntervalPort": acDs3FarEndIntervalPort,
       "acDs3FarEndIntervalNumber": acDs3FarEndIntervalNumber,
       "acDs3FarEndIntervalValidStats": acDs3FarEndIntervalValidStats,
       "acDs3FarEndIntervalResetStats": acDs3FarEndIntervalResetStats,
       "acDs3FarEndIntervalCESs": acDs3FarEndIntervalCESs,
       "acDs3FarEndIntervalCSESs": acDs3FarEndIntervalCSESs,
       "acDs3FarEndIntervalCCVs": acDs3FarEndIntervalCCVs,
       "acDs3FarEndIntervalUASs": acDs3FarEndIntervalUASs,
       "acDs3FarEndDayTable": acDs3FarEndDayTable,
       "acDs3FarEndDayEntry": acDs3FarEndDayEntry,
       "acDs3FarEndDayNodeId": acDs3FarEndDayNodeId,
       "acDs3FarEndDaySlot": acDs3FarEndDaySlot,
       "acDs3FarEndDayPort": acDs3FarEndDayPort,
       "acDs3FarEndDayNumber": acDs3FarEndDayNumber,
       "acDs3FarEndDayValidStats": acDs3FarEndDayValidStats,
       "acDs3FarEndDayResetStats": acDs3FarEndDayResetStats,
       "acDs3FarEndDayCESs": acDs3FarEndDayCESs,
       "acDs3FarEndDayCSESs": acDs3FarEndDayCSESs,
       "acDs3FarEndDayCCVs": acDs3FarEndDayCCVs,
       "acDs3FarEndDayUASs": acDs3FarEndDayUASs,
       "acDs3ThresholdTable": acDs3ThresholdTable,
       "acDs3ThresholdEntry": acDs3ThresholdEntry,
       "acDs3ThresholdNodeId": acDs3ThresholdNodeId,
       "acDs3ThresholdSlot": acDs3ThresholdSlot,
       "acDs3ThresholdPort": acDs3ThresholdPort,
       "acDs3ThresholdNEIntervalPESs": acDs3ThresholdNEIntervalPESs,
       "acDs3ThresholdNEIntervalPSESs": acDs3ThresholdNEIntervalPSESs,
       "acDs3ThresholdNEIntervalSEFSs": acDs3ThresholdNEIntervalSEFSs,
       "acDs3ThresholdNEIntervalUASs": acDs3ThresholdNEIntervalUASs,
       "acDs3ThresholdNEIntervalLCVs": acDs3ThresholdNEIntervalLCVs,
       "acDs3ThresholdNEIntervalPCVs": acDs3ThresholdNEIntervalPCVs,
       "acDs3ThresholdNEIntervalLESs": acDs3ThresholdNEIntervalLESs,
       "acDs3ThresholdNEIntervalCCVs": acDs3ThresholdNEIntervalCCVs,
       "acDs3ThresholdNEIntervalCESs": acDs3ThresholdNEIntervalCESs,
       "acDs3ThresholdNEIntervalCSESs": acDs3ThresholdNEIntervalCSESs,
       "acDs3ThresholdNEDayPESs": acDs3ThresholdNEDayPESs,
       "acDs3ThresholdNEDayPSESs": acDs3ThresholdNEDayPSESs,
       "acDs3ThresholdNEDaySEFSs": acDs3ThresholdNEDaySEFSs,
       "acDs3ThresholdNEDayUASs": acDs3ThresholdNEDayUASs,
       "acDs3ThresholdNEDayLCVs": acDs3ThresholdNEDayLCVs,
       "acDs3ThresholdNEDayPCVs": acDs3ThresholdNEDayPCVs,
       "acDs3ThresholdNEDayLESs": acDs3ThresholdNEDayLESs,
       "acDs3ThresholdNEDayCCVs": acDs3ThresholdNEDayCCVs,
       "acDs3ThresholdNEDayCESs": acDs3ThresholdNEDayCESs,
       "acDs3ThresholdNEDayCSESs": acDs3ThresholdNEDayCSESs,
       "acDs3ThresholdFEIntervalCESs": acDs3ThresholdFEIntervalCESs,
       "acDs3ThresholdFEIntervalCSESs": acDs3ThresholdFEIntervalCSESs,
       "acDs3ThresholdFEIntervalCCVs": acDs3ThresholdFEIntervalCCVs,
       "acDs3ThresholdFEIntervalUASs": acDs3ThresholdFEIntervalUASs,
       "acDs3ThresholdFEDayCESs": acDs3ThresholdFEDayCESs,
       "acDs3ThresholdFEDayCSESs": acDs3ThresholdFEDayCSESs,
       "acDs3ThresholdFEDayCCVs": acDs3ThresholdFEDayCCVs,
       "acDs3ThresholdFEDayUASs": acDs3ThresholdFEDayUASs}
)
