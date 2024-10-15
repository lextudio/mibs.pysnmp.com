# SNMP MIB module (WESTERN-MULTIPLEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WESTERN-MULTIPLEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:46 2024
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
 enterprises,
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
    "enterprises",
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

_Western_multiplex_ObjectIdentity = ObjectIdentity
western_multiplex = _Western_multiplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727)
)
_Tsunami100_06_ObjectIdentity = ObjectIdentity
tsunami100_06 = _Tsunami100_06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10)
)
_Component_ObjectIdentity = ObjectIdentity
component = _Component_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1)
)


class _CompSerialNumber_Type(DisplayString):
    """Custom type compSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CompSerialNumber_Type.__name__ = "DisplayString"
_CompSerialNumber_Object = MibScalar
compSerialNumber = _CompSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 1),
    _CompSerialNumber_Type()
)
compSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compSerialNumber.setStatus("mandatory")
_CompIDTable_Object = MibTable
compIDTable = _CompIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10)
)
if mibBuilder.loadTexts:
    compIDTable.setStatus("mandatory")
_CompIDEntry_Object = MibTableRow
compIDEntry = _CompIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10, 1)
)
compIDEntry.setIndexNames(
    (0, "WESTERN-MULTIPLEX-MIB", "compIDSerialNum"),
    (0, "WESTERN-MULTIPLEX-MIB", "compIDType"),
)
if mibBuilder.loadTexts:
    compIDEntry.setStatus("mandatory")


class _CompIDSerialNum_Type(DisplayString):
    """Custom type compIDSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CompIDSerialNum_Type.__name__ = "DisplayString"
_CompIDSerialNum_Object = MibTableColumn
compIDSerialNum = _CompIDSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10, 1, 1),
    _CompIDSerialNum_Type()
)
compIDSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compIDSerialNum.setStatus("mandatory")


class _CompIDType_Type(Integer32):
    """Custom type compIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mux-50200", 2),
          ("network-management-unit-50900", 7),
          ("receiver-50400", 5),
          ("service-channel-unit-50500", 6),
          ("transmitter-50300", 3),
          ("transmitter-pa-50301", 4),
          ("unknown", 1))
    )


_CompIDType_Type.__name__ = "Integer32"
_CompIDType_Object = MibTableColumn
compIDType = _CompIDType_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10, 1, 2),
    _CompIDType_Type()
)
compIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compIDType.setStatus("mandatory")


class _CompIDLocation_Type(Integer32):
    """Custom type compIDLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("integral", 2),
          ("removed", 3),
          ("side-a", 10),
          ("side-b", 11),
          ("unknown", 1))
    )


_CompIDLocation_Type.__name__ = "Integer32"
_CompIDLocation_Object = MibTableColumn
compIDLocation = _CompIDLocation_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10, 1, 3),
    _CompIDLocation_Type()
)
compIDLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compIDLocation.setStatus("mandatory")


class _CompIDState_Type(Integer32):
    """Custom type compIDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 4),
          ("force-reset", 10),
          ("normal", 3),
          ("removed", 1),
          ("unknown", 2))
    )


_CompIDState_Type.__name__ = "Integer32"
_CompIDState_Object = MibTableColumn
compIDState = _CompIDState_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 1, 10, 1, 4),
    _CompIDState_Type()
)
compIDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compIDState.setStatus("mandatory")
_Clock_ObjectIdentity = ObjectIdentity
clock = _Clock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 2)
)


class _ClockDateTime_Type(DisplayString):
    """Custom type clockDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_ClockDateTime_Type.__name__ = "DisplayString"
_ClockDateTime_Object = MibScalar
clockDateTime = _ClockDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 2, 1),
    _ClockDateTime_Type()
)
clockDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockDateTime.setStatus("mandatory")


class _ClockTZOffset_Type(DisplayString):
    """Custom type clockTZOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_ClockTZOffset_Type.__name__ = "DisplayString"
_ClockTZOffset_Object = MibScalar
clockTZOffset = _ClockTZOffset_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 2, 2),
    _ClockTZOffset_Type()
)
clockTZOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockTZOffset.setStatus("mandatory")
_Boot_ObjectIdentity = ObjectIdentity
boot = _Boot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3)
)


class _BootReboot_Type(Integer32):
    """Custom type bootReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("force-reset", 10),
          ("normal", 1))
    )


_BootReboot_Type.__name__ = "Integer32"
_BootReboot_Object = MibScalar
bootReboot = _BootReboot_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3, 1),
    _BootReboot_Type()
)
bootReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootReboot.setStatus("mandatory")


class _BootDate_Type(DisplayString):
    """Custom type bootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_BootDate_Type.__name__ = "DisplayString"
_BootDate_Object = MibScalar
bootDate = _BootDate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3, 2),
    _BootDate_Type()
)
bootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootDate.setStatus("mandatory")


class _BootPreviousDate_Type(DisplayString):
    """Custom type bootPreviousDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_BootPreviousDate_Type.__name__ = "DisplayString"
_BootPreviousDate_Object = MibScalar
bootPreviousDate = _BootPreviousDate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3, 3),
    _BootPreviousDate_Type()
)
bootPreviousDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootPreviousDate.setStatus("mandatory")
_BootRebootCount_Type = Integer32
_BootRebootCount_Object = MibScalar
bootRebootCount = _BootRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3, 4),
    _BootRebootCount_Type()
)
bootRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootRebootCount.setStatus("mandatory")


class _BootClearDate_Type(DisplayString):
    """Custom type bootClearDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_BootClearDate_Type.__name__ = "DisplayString"
_BootClearDate_Object = MibScalar
bootClearDate = _BootClearDate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 3, 5),
    _BootClearDate_Type()
)
bootClearDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootClearDate.setStatus("mandatory")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4)
)
_LogMaxSize_Type = Integer32
_LogMaxSize_Object = MibScalar
logMaxSize = _LogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 1),
    _LogMaxSize_Type()
)
logMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMaxSize.setStatus("mandatory")
_LogCurrentSize_Type = Integer32
_LogCurrentSize_Object = MibScalar
logCurrentSize = _LogCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 2),
    _LogCurrentSize_Type()
)
logCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentSize.setStatus("mandatory")
_LogIndexNumber_Type = Counter32
_LogIndexNumber_Object = MibScalar
logIndexNumber = _LogIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 3),
    _LogIndexNumber_Type()
)
logIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndexNumber.setStatus("mandatory")


class _LogCurrentHEALTH_Type(Integer32):
    """Custom type logCurrentHEALTH based on Integer32"""
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
        *(("critical-health", 5),
          ("major-health", 4),
          ("minor-health", 3),
          ("normal-health", 1),
          ("warning-health", 2))
    )


_LogCurrentHEALTH_Type.__name__ = "Integer32"
_LogCurrentHEALTH_Object = MibScalar
logCurrentHEALTH = _LogCurrentHEALTH_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 4),
    _LogCurrentHEALTH_Type()
)
logCurrentHEALTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentHEALTH.setStatus("mandatory")


class _LogRadioHEALTH_Type(Integer32):
    """Custom type logRadioHEALTH based on Integer32"""
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
        *(("critical-health", 5),
          ("major-health", 4),
          ("minor-health", 3),
          ("normal-health", 1),
          ("warning-health", 2))
    )


_LogRadioHEALTH_Type.__name__ = "Integer32"
_LogRadioHEALTH_Object = MibScalar
logRadioHEALTH = _LogRadioHEALTH_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 5),
    _LogRadioHEALTH_Type()
)
logRadioHEALTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRadioHEALTH.setStatus("mandatory")


class _LogSeverityFilter_Type(Integer32):
    """Custom type logSeverityFilter based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_LogSeverityFilter_Type.__name__ = "Integer32"
_LogSeverityFilter_Object = MibScalar
logSeverityFilter = _LogSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 6),
    _LogSeverityFilter_Type()
)
logSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSeverityFilter.setStatus("mandatory")
_LogFilteredSpecific_Type = Counter32
_LogFilteredSpecific_Object = MibScalar
logFilteredSpecific = _LogFilteredSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 7),
    _LogFilteredSpecific_Type()
)
logFilteredSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFilteredSpecific.setStatus("mandatory")
_LogFilteredSeverity_Type = Counter32
_LogFilteredSeverity_Object = MibScalar
logFilteredSeverity = _LogFilteredSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 8),
    _LogFilteredSeverity_Type()
)
logFilteredSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFilteredSeverity.setStatus("mandatory")
_LogFilteredRules_Type = Counter32
_LogFilteredRules_Object = MibScalar
logFilteredRules = _LogFilteredRules_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 9),
    _LogFilteredRules_Type()
)
logFilteredRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFilteredRules.setStatus("mandatory")
_LogViewPageSize_Type = Integer32
_LogViewPageSize_Object = MibScalar
logViewPageSize = _LogViewPageSize_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 15),
    _LogViewPageSize_Type()
)
logViewPageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewPageSize.setStatus("mandatory")
_LogViewPageControl_Type = Integer32
_LogViewPageControl_Object = MibScalar
logViewPageControl = _LogViewPageControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 16),
    _LogViewPageControl_Type()
)
logViewPageControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewPageControl.setStatus("mandatory")


class _LogViewSeverityFilter_Type(Integer32):
    """Custom type logViewSeverityFilter based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("all", 16),
          ("all-health", 15),
          ("all-health-NORMALIZED", 13),
          ("all-health-not-NORMALIZED", 14),
          ("all-non-health", 12),
          ("critical", 5),
          ("critical-health", 10),
          ("major", 4),
          ("major-health", 9),
          ("minor", 3),
          ("minor-health", 8),
          ("normal", 1),
          ("normal-health", 6),
          ("other", 11),
          ("warning", 2),
          ("warning-health", 7))
    )


_LogViewSeverityFilter_Type.__name__ = "Integer32"
_LogViewSeverityFilter_Object = MibScalar
logViewSeverityFilter = _LogViewSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 17),
    _LogViewSeverityFilter_Type()
)
logViewSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewSeverityFilter.setStatus("mandatory")


class _LogViewMethod_Type(Integer32):
    """Custom type logViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chronological", 1),
          ("severity", 2))
    )


_LogViewMethod_Type.__name__ = "Integer32"
_LogViewMethod_Object = MibScalar
logViewMethod = _LogViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 18),
    _LogViewMethod_Type()
)
logViewMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewMethod.setStatus("mandatory")


class _LogViewDirection_Type(Integer32):
    """Custom type logViewDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical-to-normal", 1),
          ("normal-to-critical", 2))
    )


_LogViewDirection_Type.__name__ = "Integer32"
_LogViewDirection_Object = MibScalar
logViewDirection = _LogViewDirection_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 19),
    _LogViewDirection_Type()
)
logViewDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewDirection.setStatus("mandatory")


class _LogViewAge_Type(Integer32):
    """Custom type logViewAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("newest-to-oldest", 2),
          ("oldest-to-newest", 1))
    )


_LogViewAge_Type.__name__ = "Integer32"
_LogViewAge_Object = MibScalar
logViewAge = _LogViewAge_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 20),
    _LogViewAge_Type()
)
logViewAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logViewAge.setStatus("mandatory")
_LogViewEvents_Type = Integer32
_LogViewEvents_Object = MibScalar
logViewEvents = _LogViewEvents_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 21),
    _LogViewEvents_Type()
)
logViewEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logViewEvents.setStatus("mandatory")


class _LogTrapSeverityFilter_Type(Integer32):
    """Custom type logTrapSeverityFilter based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("all", 13),
          ("all-health", 12),
          ("all-non-health", 11),
          ("critical", 5),
          ("critical-health", 10),
          ("major", 4),
          ("major-health", 9),
          ("minor", 3),
          ("minor-health", 8),
          ("none", 14),
          ("normal", 1),
          ("normal-health", 6),
          ("warning", 2),
          ("warning-health", 7))
    )


_LogTrapSeverityFilter_Type.__name__ = "Integer32"
_LogTrapSeverityFilter_Object = MibScalar
logTrapSeverityFilter = _LogTrapSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 30),
    _LogTrapSeverityFilter_Type()
)
logTrapSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrapSeverityFilter.setStatus("mandatory")


class _LogTrapHysteresis_Type(Integer32):
    """Custom type logTrapHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_LogTrapHysteresis_Type.__name__ = "Integer32"
_LogTrapHysteresis_Object = MibScalar
logTrapHysteresis = _LogTrapHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 31),
    _LogTrapHysteresis_Type()
)
logTrapHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrapHysteresis.setStatus("mandatory")
_LogRecTable_Object = MibTable
logRecTable = _LogRecTable_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40)
)
if mibBuilder.loadTexts:
    logRecTable.setStatus("mandatory")
_LogRecEntry_Object = MibTableRow
logRecEntry = _LogRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40, 1)
)
logRecEntry.setIndexNames(
    (0, "WESTERN-MULTIPLEX-MIB", "logRecIndexNumber"),
)
if mibBuilder.loadTexts:
    logRecEntry.setStatus("mandatory")
_LogRecIndexNumber_Type = Integer32
_LogRecIndexNumber_Object = MibTableColumn
logRecIndexNumber = _LogRecIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40, 1, 1),
    _LogRecIndexNumber_Type()
)
logRecIndexNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logRecIndexNumber.setStatus("mandatory")


class _LogRecSeverity_Type(Integer32):
    """Custom type logRecSeverity based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              50)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("critical-NORMALIZED", 15),
          ("critical-health", 10),
          ("major", 4),
          ("major-NORMALIZED", 14),
          ("major-health", 9),
          ("minor", 3),
          ("minor-NORMALIZED", 13),
          ("minor-health", 8),
          ("normal", 1),
          ("normal-NORMALIZED", 11),
          ("normal-health", 6),
          ("other", 50),
          ("warning", 2),
          ("warning-NORMALIZED", 12),
          ("warning-health", 7))
    )


_LogRecSeverity_Type.__name__ = "Integer32"
_LogRecSeverity_Object = MibTableColumn
logRecSeverity = _LogRecSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40, 1, 2),
    _LogRecSeverity_Type()
)
logRecSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRecSeverity.setStatus("mandatory")


class _LogRecEvent_Type(Integer32):
    """Custom type logRecEvent based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("agent-authen-fail", 11),
          ("agent-intern-err", 4),
          ("agent-oid-err", 3),
          ("buf-pool-err", 8),
          ("dup-route-on-if", 21),
          ("enet-ip-err", 15),
          ("internal-err", 6),
          ("link-ppp-port-down", 18),
          ("link-ppp-port-up", 17),
          ("malloc-err", 7),
          ("nv-read-err", 13),
          ("nv-write-err", 12),
          ("radio-ais", 30),
          ("radio-alarm-summary", 24),
          ("radio-ber", 29),
          ("radio-down", 23),
          ("radio-fan-1-alarm", 31),
          ("radio-fan-2-alarm", 32),
          ("radio-receiver-synth-alarm", 33),
          ("radio-sync-alarm", 28),
          ("radio-t1-code-violation-alarm", 27),
          ("radio-t1-input-alarm", 25),
          ("radio-t1-line-driver-alarm", 26),
          ("radio-transmitter-synth-alarm", 34),
          ("rtc-needs-setting", 14),
          ("rtc-set-via-menu", 20),
          ("rtc-set-via-mib", 19),
          ("socket-err", 22),
          ("trap-encode-err", 5),
          ("trapFlow-closed", 16),
          ("ualarm-alarm-xition", 1),
          ("ualarm-normal-xition", 2),
          ("unreach-trap-mgr", 10))
    )


_LogRecEvent_Type.__name__ = "Integer32"
_LogRecEvent_Object = MibTableColumn
logRecEvent = _LogRecEvent_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40, 1, 3),
    _LogRecEvent_Type()
)
logRecEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRecEvent.setStatus("mandatory")
_LogRecDescription_Type = DisplayString
_LogRecDescription_Object = MibTableColumn
logRecDescription = _LogRecDescription_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 40, 1, 4),
    _LogRecDescription_Type()
)
logRecDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRecDescription.setStatus("mandatory")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5)
)


class _TrapControl_Type(Integer32):
    """Custom type trapControl based on Integer32"""
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
          ("feedbackPinLimited", 3),
          ("unLimited", 2))
    )


_TrapControl_Type.__name__ = "Integer32"
_TrapControl_Object = MibScalar
trapControl = _TrapControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 1),
    _TrapControl_Type()
)
trapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapControl.setStatus("mandatory")


class _TrapClearDate_Type(DisplayString):
    """Custom type trapClearDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_TrapClearDate_Type.__name__ = "DisplayString"
_TrapClearDate_Object = MibScalar
trapClearDate = _TrapClearDate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 2),
    _TrapClearDate_Type()
)
trapClearDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClearDate.setStatus("mandatory")
_TrapMgrTable_Object = MibTable
trapMgrTable = _TrapMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3)
)
if mibBuilder.loadTexts:
    trapMgrTable.setStatus("mandatory")
_TrapMgrEntry_Object = MibTableRow
trapMgrEntry = _TrapMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3, 1)
)
trapMgrEntry.setIndexNames(
    (0, "WESTERN-MULTIPLEX-MIB", "trapMgrIndex"),
)
if mibBuilder.loadTexts:
    trapMgrEntry.setStatus("mandatory")
_TrapMgrIndex_Type = Integer32
_TrapMgrIndex_Object = MibTableColumn
trapMgrIndex = _TrapMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3, 1, 1),
    _TrapMgrIndex_Type()
)
trapMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMgrIndex.setStatus("mandatory")
_TrapMgrAddress_Type = IpAddress
_TrapMgrAddress_Object = MibTableColumn
trapMgrAddress = _TrapMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3, 1, 2),
    _TrapMgrAddress_Type()
)
trapMgrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrAddress.setStatus("mandatory")


class _TrapMgrControl_Type(Integer32):
    """Custom type trapMgrControl based on Integer32"""
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
        *(("both", 1),
          ("enterprise", 3),
          ("none", 4),
          ("standard", 2))
    )


_TrapMgrControl_Type.__name__ = "Integer32"
_TrapMgrControl_Object = MibTableColumn
trapMgrControl = _TrapMgrControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3, 1, 3),
    _TrapMgrControl_Type()
)
trapMgrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrControl.setStatus("mandatory")
_TrapMgrCounter_Type = Counter32
_TrapMgrCounter_Object = MibTableColumn
trapMgrCounter = _TrapMgrCounter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 3, 1, 4),
    _TrapMgrCounter_Type()
)
trapMgrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMgrCounter.setStatus("mandatory")


class _TrapFlow_Type(Integer32):
    """Custom type trapFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_TrapFlow_Type.__name__ = "Integer32"
_TrapFlow_Object = MibScalar
trapFlow = _TrapFlow_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 4),
    _TrapFlow_Type()
)
trapFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFlow.setStatus("mandatory")


class _TrapLastTimestamp_Type(DisplayString):
    """Custom type trapLastTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_TrapLastTimestamp_Type.__name__ = "DisplayString"
_TrapLastTimestamp_Object = MibScalar
trapLastTimestamp = _TrapLastTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 5),
    _TrapLastTimestamp_Type()
)
trapLastTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLastTimestamp.setStatus("mandatory")
_TrapWindowPeriod_Type = Integer32
_TrapWindowPeriod_Object = MibScalar
trapWindowPeriod = _TrapWindowPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 6),
    _TrapWindowPeriod_Type()
)
trapWindowPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWindowPeriod.setStatus("mandatory")
_TrapMaxPerWindow_Type = Integer32
_TrapMaxPerWindow_Object = MibScalar
trapMaxPerWindow = _TrapMaxPerWindow_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 7),
    _TrapMaxPerWindow_Type()
)
trapMaxPerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMaxPerWindow.setStatus("mandatory")


class _TrapSequenceClearDate_Type(DisplayString):
    """Custom type trapSequenceClearDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_TrapSequenceClearDate_Type.__name__ = "DisplayString"
_TrapSequenceClearDate_Object = MibScalar
trapSequenceClearDate = _TrapSequenceClearDate_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 10),
    _TrapSequenceClearDate_Type()
)
trapSequenceClearDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSequenceClearDate.setStatus("mandatory")
_TrapSequenceNumber_Type = Integer32
_TrapSequenceNumber_Object = MibScalar
trapSequenceNumber = _TrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 11),
    _TrapSequenceNumber_Type()
)
trapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNumber.setStatus("mandatory")


class _TrapSeverityFilter_Type(Integer32):
    """Custom type trapSeverityFilter based on Integer32"""
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_TrapSeverityFilter_Type.__name__ = "Integer32"
_TrapSeverityFilter_Object = MibScalar
trapSeverityFilter = _TrapSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 12),
    _TrapSeverityFilter_Type()
)
trapSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSeverityFilter.setStatus("mandatory")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 13),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_TrapFilteredSpecific_Type = Counter32
_TrapFilteredSpecific_Object = MibScalar
trapFilteredSpecific = _TrapFilteredSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 18),
    _TrapFilteredSpecific_Type()
)
trapFilteredSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilteredSpecific.setStatus("mandatory")
_TrapFilteredControl_Type = Counter32
_TrapFilteredControl_Object = MibScalar
trapFilteredControl = _TrapFilteredControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 19),
    _TrapFilteredControl_Type()
)
trapFilteredControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilteredControl.setStatus("mandatory")
_TrapFilteredManager_Type = Counter32
_TrapFilteredManager_Object = MibScalar
trapFilteredManager = _TrapFilteredManager_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 20),
    _TrapFilteredManager_Type()
)
trapFilteredManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilteredManager.setStatus("mandatory")
_TrapFilteredSeverity_Type = Counter32
_TrapFilteredSeverity_Object = MibScalar
trapFilteredSeverity = _TrapFilteredSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 21),
    _TrapFilteredSeverity_Type()
)
trapFilteredSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilteredSeverity.setStatus("mandatory")


class _TrapColdStartControl_Type(Integer32):
    """Custom type trapColdStartControl based on Integer32"""
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


_TrapColdStartControl_Type.__name__ = "Integer32"
_TrapColdStartControl_Object = MibScalar
trapColdStartControl = _TrapColdStartControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 22),
    _TrapColdStartControl_Type()
)
trapColdStartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapColdStartControl.setStatus("mandatory")


class _TrapLinkDownControl_Type(Integer32):
    """Custom type trapLinkDownControl based on Integer32"""
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


_TrapLinkDownControl_Type.__name__ = "Integer32"
_TrapLinkDownControl_Object = MibScalar
trapLinkDownControl = _TrapLinkDownControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 23),
    _TrapLinkDownControl_Type()
)
trapLinkDownControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLinkDownControl.setStatus("mandatory")


class _TrapLinkUpControl_Type(Integer32):
    """Custom type trapLinkUpControl based on Integer32"""
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


_TrapLinkUpControl_Type.__name__ = "Integer32"
_TrapLinkUpControl_Object = MibScalar
trapLinkUpControl = _TrapLinkUpControl_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 24),
    _TrapLinkUpControl_Type()
)
trapLinkUpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLinkUpControl.setStatus("mandatory")
_Auth_ObjectIdentity = ObjectIdentity
auth = _Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 6)
)
_AuthUnAuthIpAddr_Type = IpAddress
_AuthUnAuthIpAddr_Object = MibScalar
authUnAuthIpAddr = _AuthUnAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 6, 1),
    _AuthUnAuthIpAddr_Type()
)
authUnAuthIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUnAuthIpAddr.setStatus("mandatory")


class _AuthUnAuthCommunity_Type(DisplayString):
    """Custom type authUnAuthCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthUnAuthCommunity_Type.__name__ = "DisplayString"
_AuthUnAuthCommunity_Object = MibScalar
authUnAuthCommunity = _AuthUnAuthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 6, 2),
    _AuthUnAuthCommunity_Type()
)
authUnAuthCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUnAuthCommunity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

logGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 4, 0, 1)
)
logGenericTrap.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-MIB", "logRecIndexNumber"),
        ("WESTERN-MULTIPLEX-MIB", "logRecSeverity"),
        ("WESTERN-MULTIPLEX-MIB", "logRecEvent"),
        ("WESTERN-MULTIPLEX-MIB", "logRecDescription"))
)
if mibBuilder.loadTexts:
    logGenericTrap.setStatus(
        ""
    )

trapsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3727, 20, 10, 5, 0, 1)
)
trapsDisabled.setObjects(
      *(("WESTERN-MULTIPLEX-MIB", "trapSequenceNumber"),
        ("WESTERN-MULTIPLEX-MIB", "trapLastTimestamp"),
        ("WESTERN-MULTIPLEX-MIB", "trapWindowPeriod"),
        ("WESTERN-MULTIPLEX-MIB", "trapMaxPerWindow"))
)
if mibBuilder.loadTexts:
    trapsDisabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERN-MULTIPLEX-MIB",
    **{"western-multiplex": western_multiplex,
       "tsunami100-06": tsunami100_06,
       "system": system,
       "component": component,
       "compSerialNumber": compSerialNumber,
       "compIDTable": compIDTable,
       "compIDEntry": compIDEntry,
       "compIDSerialNum": compIDSerialNum,
       "compIDType": compIDType,
       "compIDLocation": compIDLocation,
       "compIDState": compIDState,
       "clock": clock,
       "clockDateTime": clockDateTime,
       "clockTZOffset": clockTZOffset,
       "boot": boot,
       "bootReboot": bootReboot,
       "bootDate": bootDate,
       "bootPreviousDate": bootPreviousDate,
       "bootRebootCount": bootRebootCount,
       "bootClearDate": bootClearDate,
       "log": log,
       "logGenericTrap": logGenericTrap,
       "logMaxSize": logMaxSize,
       "logCurrentSize": logCurrentSize,
       "logIndexNumber": logIndexNumber,
       "logCurrentHEALTH": logCurrentHEALTH,
       "logRadioHEALTH": logRadioHEALTH,
       "logSeverityFilter": logSeverityFilter,
       "logFilteredSpecific": logFilteredSpecific,
       "logFilteredSeverity": logFilteredSeverity,
       "logFilteredRules": logFilteredRules,
       "logViewPageSize": logViewPageSize,
       "logViewPageControl": logViewPageControl,
       "logViewSeverityFilter": logViewSeverityFilter,
       "logViewMethod": logViewMethod,
       "logViewDirection": logViewDirection,
       "logViewAge": logViewAge,
       "logViewEvents": logViewEvents,
       "logTrapSeverityFilter": logTrapSeverityFilter,
       "logTrapHysteresis": logTrapHysteresis,
       "logRecTable": logRecTable,
       "logRecEntry": logRecEntry,
       "logRecIndexNumber": logRecIndexNumber,
       "logRecSeverity": logRecSeverity,
       "logRecEvent": logRecEvent,
       "logRecDescription": logRecDescription,
       "trap": trap,
       "trapsDisabled": trapsDisabled,
       "trapControl": trapControl,
       "trapClearDate": trapClearDate,
       "trapMgrTable": trapMgrTable,
       "trapMgrEntry": trapMgrEntry,
       "trapMgrIndex": trapMgrIndex,
       "trapMgrAddress": trapMgrAddress,
       "trapMgrControl": trapMgrControl,
       "trapMgrCounter": trapMgrCounter,
       "trapFlow": trapFlow,
       "trapLastTimestamp": trapLastTimestamp,
       "trapWindowPeriod": trapWindowPeriod,
       "trapMaxPerWindow": trapMaxPerWindow,
       "trapSequenceClearDate": trapSequenceClearDate,
       "trapSequenceNumber": trapSequenceNumber,
       "trapSeverityFilter": trapSeverityFilter,
       "trapCommunity": trapCommunity,
       "trapFilteredSpecific": trapFilteredSpecific,
       "trapFilteredControl": trapFilteredControl,
       "trapFilteredManager": trapFilteredManager,
       "trapFilteredSeverity": trapFilteredSeverity,
       "trapColdStartControl": trapColdStartControl,
       "trapLinkDownControl": trapLinkDownControl,
       "trapLinkUpControl": trapLinkUpControl,
       "auth": auth,
       "authUnAuthIpAddr": authUnAuthIpAddr,
       "authUnAuthCommunity": authUnAuthCommunity}
)
