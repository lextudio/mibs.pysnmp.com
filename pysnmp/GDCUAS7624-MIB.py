# SNMP MIB module (GDCUAS7624-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCUAS7624-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:23 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Niudiu_ObjectIdentity = ObjectIdentity
niudiu = _Niudiu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18)
)
_Uas7624System_ObjectIdentity = ObjectIdentity
uas7624System = _Uas7624System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1)
)
_Uas7624Version_ObjectIdentity = ObjectIdentity
uas7624Version = _Uas7624Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1)
)


class _Uas7624MIBversion_Type(DisplayString):
    """Custom type uas7624MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Uas7624MIBversion_Type.__name__ = "DisplayString"
_Uas7624MIBversion_Object = MibScalar
uas7624MIBversion = _Uas7624MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 1),
    _Uas7624MIBversion_Type()
)
uas7624MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624MIBversion.setStatus("mandatory")
_Uas7624VersionTable_Object = MibTable
uas7624VersionTable = _Uas7624VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    uas7624VersionTable.setStatus("mandatory")
_Uas7624VersionEntry_Object = MibTableRow
uas7624VersionEntry = _Uas7624VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2, 1)
)
uas7624VersionEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624VersionIndex"),
)
if mibBuilder.loadTexts:
    uas7624VersionEntry.setStatus("mandatory")
_Uas7624VersionIndex_Type = SCinstance
_Uas7624VersionIndex_Object = MibTableColumn
uas7624VersionIndex = _Uas7624VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2, 1, 1),
    _Uas7624VersionIndex_Type()
)
uas7624VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624VersionIndex.setStatus("mandatory")


class _Uas7624FirmwareRev_Type(DisplayString):
    """Custom type uas7624FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Uas7624FirmwareRev_Type.__name__ = "DisplayString"
_Uas7624FirmwareRev_Object = MibTableColumn
uas7624FirmwareRev = _Uas7624FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2, 1, 2),
    _Uas7624FirmwareRev_Type()
)
uas7624FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624FirmwareRev.setStatus("mandatory")


class _Uas7624CardType_Type(DisplayString):
    """Custom type uas7624CardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Uas7624CardType_Type.__name__ = "DisplayString"
_Uas7624CardType_Object = MibTableColumn
uas7624CardType = _Uas7624CardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2, 1, 3),
    _Uas7624CardType_Type()
)
uas7624CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624CardType.setStatus("mandatory")


class _Uas7624BootRev_Type(DisplayString):
    """Custom type uas7624BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Uas7624BootRev_Type.__name__ = "DisplayString"
_Uas7624BootRev_Object = MibTableColumn
uas7624BootRev = _Uas7624BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 1, 2, 1, 4),
    _Uas7624BootRev_Type()
)
uas7624BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624BootRev.setStatus("mandatory")
_Uas7624Maintenance_ObjectIdentity = ObjectIdentity
uas7624Maintenance = _Uas7624Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2)
)
_Uas7624MaintenanceTable_Object = MibTable
uas7624MaintenanceTable = _Uas7624MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    uas7624MaintenanceTable.setStatus("mandatory")
_Uas7624MaintenanceEntry_Object = MibTableRow
uas7624MaintenanceEntry = _Uas7624MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1)
)
uas7624MaintenanceEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    uas7624MaintenanceEntry.setStatus("mandatory")
_Uas7624MaintenanceLineIndex_Type = SCinstance
_Uas7624MaintenanceLineIndex_Object = MibTableColumn
uas7624MaintenanceLineIndex = _Uas7624MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 1),
    _Uas7624MaintenanceLineIndex_Type()
)
uas7624MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624MaintenanceLineIndex.setStatus("mandatory")


class _Uas7624SoftReset_Type(Integer32):
    """Custom type uas7624SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Uas7624SoftReset_Type.__name__ = "Integer32"
_Uas7624SoftReset_Object = MibTableColumn
uas7624SoftReset = _Uas7624SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 2),
    _Uas7624SoftReset_Type()
)
uas7624SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624SoftReset.setStatus("mandatory")


class _Uas7624DefaultInit_Type(Integer32):
    """Custom type uas7624DefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 2),
          ("normal", 1))
    )


_Uas7624DefaultInit_Type.__name__ = "Integer32"
_Uas7624DefaultInit_Object = MibTableColumn
uas7624DefaultInit = _Uas7624DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 3),
    _Uas7624DefaultInit_Type()
)
uas7624DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624DefaultInit.setStatus("mandatory")


class _Uas7624ResetMajorAlarm_Type(Integer32):
    """Custom type uas7624ResetMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Uas7624ResetMajorAlarm_Type.__name__ = "Integer32"
_Uas7624ResetMajorAlarm_Object = MibTableColumn
uas7624ResetMajorAlarm = _Uas7624ResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 4),
    _Uas7624ResetMajorAlarm_Type()
)
uas7624ResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624ResetMajorAlarm.setStatus("mandatory")


class _Uas7624ResetMinorAlarm_Type(Integer32):
    """Custom type uas7624ResetMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Uas7624ResetMinorAlarm_Type.__name__ = "Integer32"
_Uas7624ResetMinorAlarm_Object = MibTableColumn
uas7624ResetMinorAlarm = _Uas7624ResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 5),
    _Uas7624ResetMinorAlarm_Type()
)
uas7624ResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624ResetMinorAlarm.setStatus("mandatory")


class _Uas7624ResetStatistics_Type(Integer32):
    """Custom type uas7624ResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Uas7624ResetStatistics_Type.__name__ = "Integer32"
_Uas7624ResetStatistics_Object = MibTableColumn
uas7624ResetStatistics = _Uas7624ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 6),
    _Uas7624ResetStatistics_Type()
)
uas7624ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624ResetStatistics.setStatus("mandatory")
_Uas7624StatLastInitialized_Type = TimeTicks
_Uas7624StatLastInitialized_Object = MibTableColumn
uas7624StatLastInitialized = _Uas7624StatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 7),
    _Uas7624StatLastInitialized_Type()
)
uas7624StatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624StatLastInitialized.setStatus("mandatory")


class _Uas7624ValidIntervals_Type(Integer32):
    """Custom type uas7624ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Uas7624ValidIntervals_Type.__name__ = "Integer32"
_Uas7624ValidIntervals_Object = MibTableColumn
uas7624ValidIntervals = _Uas7624ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 8),
    _Uas7624ValidIntervals_Type()
)
uas7624ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624ValidIntervals.setStatus("mandatory")


class _Uas7624SysUpTime_Type(Integer32):
    """Custom type uas7624SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7624SysUpTime_Type.__name__ = "Integer32"
_Uas7624SysUpTime_Object = MibTableColumn
uas7624SysUpTime = _Uas7624SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 9),
    _Uas7624SysUpTime_Type()
)
uas7624SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624SysUpTime.setStatus("mandatory")


class _Uas7624LedStatus_Type(OctetString):
    """Custom type uas7624LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Uas7624LedStatus_Type.__name__ = "OctetString"
_Uas7624LedStatus_Object = MibTableColumn
uas7624LedStatus = _Uas7624LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 10),
    _Uas7624LedStatus_Type()
)
uas7624LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624LedStatus.setStatus("mandatory")


class _Uas7624AlarmStatus_Type(OctetString):
    """Custom type uas7624AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Uas7624AlarmStatus_Type.__name__ = "OctetString"
_Uas7624AlarmStatus_Object = MibTableColumn
uas7624AlarmStatus = _Uas7624AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 11),
    _Uas7624AlarmStatus_Type()
)
uas7624AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624AlarmStatus.setStatus("mandatory")


class _Uas7624LoopState_Type(Integer32):
    """Custom type uas7624LoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1))
    )


_Uas7624LoopState_Type.__name__ = "Integer32"
_Uas7624LoopState_Object = MibTableColumn
uas7624LoopState = _Uas7624LoopState_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 12),
    _Uas7624LoopState_Type()
)
uas7624LoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LoopState.setStatus("mandatory")


class _Uas7624ConfigMode_Type(Integer32):
    """Custom type uas7624ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardMode", 1),
          ("softMode", 2))
    )


_Uas7624ConfigMode_Type.__name__ = "Integer32"
_Uas7624ConfigMode_Object = MibTableColumn
uas7624ConfigMode = _Uas7624ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 2, 1, 1, 13),
    _Uas7624ConfigMode_Type()
)
uas7624ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624ConfigMode.setStatus("mandatory")
_Uas7624Configuration_ObjectIdentity = ObjectIdentity
uas7624Configuration = _Uas7624Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3)
)
_Uas7624ConfigTable_Object = MibTable
uas7624ConfigTable = _Uas7624ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1)
)
if mibBuilder.loadTexts:
    uas7624ConfigTable.setStatus("mandatory")
_Uas7624ConfigEntry_Object = MibTableRow
uas7624ConfigEntry = _Uas7624ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1)
)
uas7624ConfigEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624ConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7624ConfigEntry.setStatus("mandatory")
_Uas7624ConfigIndex_Type = SCinstance
_Uas7624ConfigIndex_Object = MibTableColumn
uas7624ConfigIndex = _Uas7624ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 1),
    _Uas7624ConfigIndex_Type()
)
uas7624ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624ConfigIndex.setStatus("mandatory")


class _Uas7624NetworkInterfaceType_Type(Integer32):
    """Custom type uas7624NetworkInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("dsx1", 2))
    )


_Uas7624NetworkInterfaceType_Type.__name__ = "Integer32"
_Uas7624NetworkInterfaceType_Object = MibTableColumn
uas7624NetworkInterfaceType = _Uas7624NetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 2),
    _Uas7624NetworkInterfaceType_Type()
)
uas7624NetworkInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624NetworkInterfaceType.setStatus("mandatory")


class _Uas7624TransmitClockSource_Type(Integer32):
    """Custom type uas7624TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("recovered", 1))
    )


_Uas7624TransmitClockSource_Type.__name__ = "Integer32"
_Uas7624TransmitClockSource_Object = MibTableColumn
uas7624TransmitClockSource = _Uas7624TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 3),
    _Uas7624TransmitClockSource_Type()
)
uas7624TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624TransmitClockSource.setStatus("mandatory")


class _Uas7624PreEqualization_Type(Integer32):
    """Custom type uas7624PreEqualization based on Integer32"""
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
        *(("feet130", 2),
          ("feet260", 3),
          ("feet390", 4),
          ("feet530", 5),
          ("feet655", 6),
          ("none", 1))
    )


_Uas7624PreEqualization_Type.__name__ = "Integer32"
_Uas7624PreEqualization_Object = MibTableColumn
uas7624PreEqualization = _Uas7624PreEqualization_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 4),
    _Uas7624PreEqualization_Type()
)
uas7624PreEqualization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624PreEqualization.setStatus("mandatory")


class _Uas7624Framing_Type(Integer32):
    """Custom type uas7624Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("eSF", 1))
    )


_Uas7624Framing_Type.__name__ = "Integer32"
_Uas7624Framing_Object = MibTableColumn
uas7624Framing = _Uas7624Framing_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 5),
    _Uas7624Framing_Type()
)
uas7624Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624Framing.setStatus("mandatory")


class _Uas7624LineCoding_Type(Integer32):
    """Custom type uas7624LineCoding based on Integer32"""
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


_Uas7624LineCoding_Type.__name__ = "Integer32"
_Uas7624LineCoding_Object = MibTableColumn
uas7624LineCoding = _Uas7624LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 6),
    _Uas7624LineCoding_Type()
)
uas7624LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LineCoding.setStatus("mandatory")


class _Uas7624LineBuildout_Type(Integer32):
    """Custom type uas7624LineBuildout based on Integer32"""
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
        *(("dB0", 1),
          ("dB15", 3),
          ("dB22", 4),
          ("dB75", 2))
    )


_Uas7624LineBuildout_Type.__name__ = "Integer32"
_Uas7624LineBuildout_Object = MibTableColumn
uas7624LineBuildout = _Uas7624LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 7),
    _Uas7624LineBuildout_Type()
)
uas7624LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LineBuildout.setStatus("mandatory")


class _Uas7624FDLMode_Type(Integer32):
    """Custom type uas7624FDLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aNSIT1403", 2),
          ("none", 1),
          ("tR54016", 3))
    )


_Uas7624FDLMode_Type.__name__ = "Integer32"
_Uas7624FDLMode_Object = MibTableColumn
uas7624FDLMode = _Uas7624FDLMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 8),
    _Uas7624FDLMode_Type()
)
uas7624FDLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624FDLMode.setStatus("mandatory")


class _Uas7624Loopback_Type(Integer32):
    """Custom type uas7624Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibitloop", 1),
          ("lineloop", 3),
          ("payloadloop", 2))
    )


_Uas7624Loopback_Type.__name__ = "Integer32"
_Uas7624Loopback_Object = MibTableColumn
uas7624Loopback = _Uas7624Loopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 9),
    _Uas7624Loopback_Type()
)
uas7624Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624Loopback.setStatus("mandatory")


class _Uas7624AISLoopdown_Type(Integer32):
    """Custom type uas7624AISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Uas7624AISLoopdown_Type.__name__ = "Integer32"
_Uas7624AISLoopdown_Object = MibTableColumn
uas7624AISLoopdown = _Uas7624AISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 10),
    _Uas7624AISLoopdown_Type()
)
uas7624AISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624AISLoopdown.setStatus("mandatory")


class _Uas7624LineBuildoutMode_Type(Integer32):
    """Custom type uas7624LineBuildoutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Uas7624LineBuildoutMode_Type.__name__ = "Integer32"
_Uas7624LineBuildoutMode_Object = MibTableColumn
uas7624LineBuildoutMode = _Uas7624LineBuildoutMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 11),
    _Uas7624LineBuildoutMode_Type()
)
uas7624LineBuildoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LineBuildoutMode.setStatus("mandatory")


class _Uas7624FramingMode_Type(Integer32):
    """Custom type uas7624FramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Uas7624FramingMode_Type.__name__ = "Integer32"
_Uas7624FramingMode_Object = MibTableColumn
uas7624FramingMode = _Uas7624FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 3, 1, 1, 12),
    _Uas7624FramingMode_Type()
)
uas7624FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624FramingMode.setStatus("mandatory")
_Uas7624Diagnostics_ObjectIdentity = ObjectIdentity
uas7624Diagnostics = _Uas7624Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4)
)
_Uas7624DiagTable_Object = MibTable
uas7624DiagTable = _Uas7624DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    uas7624DiagTable.setStatus("mandatory")
_Uas7624DiagEntry_Object = MibTableRow
uas7624DiagEntry = _Uas7624DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1)
)
uas7624DiagEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624DiagIndex"),
)
if mibBuilder.loadTexts:
    uas7624DiagEntry.setStatus("mandatory")
_Uas7624DiagIndex_Type = SCinstance
_Uas7624DiagIndex_Object = MibTableColumn
uas7624DiagIndex = _Uas7624DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 1),
    _Uas7624DiagIndex_Type()
)
uas7624DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624DiagIndex.setStatus("mandatory")


class _Uas7624DiagConfig_Type(Integer32):
    """Custom type uas7624DiagConfig based on Integer32"""
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
        *(("digitalLoopback", 4),
          ("lineLoopback", 2),
          ("payloadLoopback", 3),
          ("rdl", 6),
          ("rdlSelfTest", 7),
          ("selfTest", 5),
          ("stopTest", 1))
    )


_Uas7624DiagConfig_Type.__name__ = "Integer32"
_Uas7624DiagConfig_Object = MibTableColumn
uas7624DiagConfig = _Uas7624DiagConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 2),
    _Uas7624DiagConfig_Type()
)
uas7624DiagConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624DiagConfig.setStatus("mandatory")


class _Uas7624T1TestLimit_Type(Integer32):
    """Custom type uas7624T1TestLimit based on Integer32"""
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
        *(("noLimit", 1),
          ("testTime10Mins", 11),
          ("testTime15Mins", 12),
          ("testTime1Min", 2),
          ("testTime20Mins", 13),
          ("testTime25Mins", 14),
          ("testTime2Mins", 3),
          ("testTime30Mins", 15),
          ("testTime30Secs", 16),
          ("testTime3Mins", 4),
          ("testTime4Mins", 5),
          ("testTime5Mins", 6),
          ("testTime6Mins", 7),
          ("testTime7Mins", 8),
          ("testTime8Mins", 9),
          ("testTime9Mins", 10))
    )


_Uas7624T1TestLimit_Type.__name__ = "Integer32"
_Uas7624T1TestLimit_Object = MibTableColumn
uas7624T1TestLimit = _Uas7624T1TestLimit_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 3),
    _Uas7624T1TestLimit_Type()
)
uas7624T1TestLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624T1TestLimit.setStatus("mandatory")


class _Uas7624T1TestExecutionStatus_Type(Integer32):
    """Custom type uas7624T1TestExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notInTest", 1),
          ("testCompleted", 4),
          ("testCompletedNotInTest", 5),
          ("testInProgress", 2))
    )


_Uas7624T1TestExecutionStatus_Type.__name__ = "Integer32"
_Uas7624T1TestExecutionStatus_Object = MibTableColumn
uas7624T1TestExecutionStatus = _Uas7624T1TestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 4),
    _Uas7624T1TestExecutionStatus_Type()
)
uas7624T1TestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624T1TestExecutionStatus.setStatus("mandatory")


class _Uas7624T1TestExceptions_Type(Integer32):
    """Custom type uas7624T1TestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Uas7624T1TestExceptions_Type.__name__ = "Integer32"
_Uas7624T1TestExceptions_Object = MibTableColumn
uas7624T1TestExceptions = _Uas7624T1TestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 5),
    _Uas7624T1TestExceptions_Type()
)
uas7624T1TestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624T1TestExceptions.setStatus("mandatory")


class _Uas7624TestResults_Type(Integer32):
    """Custom type uas7624TestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_Uas7624TestResults_Type.__name__ = "Integer32"
_Uas7624TestResults_Object = MibTableColumn
uas7624TestResults = _Uas7624TestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 6),
    _Uas7624TestResults_Type()
)
uas7624TestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624TestResults.setStatus("mandatory")


class _Uas7624ResetTestResults_Type(Integer32):
    """Custom type uas7624ResetTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Uas7624ResetTestResults_Type.__name__ = "Integer32"
_Uas7624ResetTestResults_Object = MibTableColumn
uas7624ResetTestResults = _Uas7624ResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 4, 1, 1, 7),
    _Uas7624ResetTestResults_Type()
)
uas7624ResetTestResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624ResetTestResults.setStatus("mandatory")
_Uas7624Performance_ObjectIdentity = ObjectIdentity
uas7624Performance = _Uas7624Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5)
)
_Uas7624CurrentTable_Object = MibTable
uas7624CurrentTable = _Uas7624CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 3)
)
if mibBuilder.loadTexts:
    uas7624CurrentTable.setStatus("mandatory")
_Uas7624CurrentEntry_Object = MibTableRow
uas7624CurrentEntry = _Uas7624CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 3, 1)
)
uas7624CurrentEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624CurrentIndex"),
)
if mibBuilder.loadTexts:
    uas7624CurrentEntry.setStatus("mandatory")
_Uas7624CurrentIndex_Type = SCinstance
_Uas7624CurrentIndex_Object = MibTableColumn
uas7624CurrentIndex = _Uas7624CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 3, 1, 1),
    _Uas7624CurrentIndex_Type()
)
uas7624CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624CurrentIndex.setStatus("mandatory")


class _Uas7624CurrentStat_Type(OctetString):
    """Custom type uas7624CurrentStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 17),
    )


_Uas7624CurrentStat_Type.__name__ = "OctetString"
_Uas7624CurrentStat_Object = MibTableColumn
uas7624CurrentStat = _Uas7624CurrentStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 3, 1, 2),
    _Uas7624CurrentStat_Type()
)
uas7624CurrentStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624CurrentStat.setStatus("mandatory")
_Uas7624IntervalTable_Object = MibTable
uas7624IntervalTable = _Uas7624IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 4)
)
if mibBuilder.loadTexts:
    uas7624IntervalTable.setStatus("mandatory")
_Uas7624IntervalEntry_Object = MibTableRow
uas7624IntervalEntry = _Uas7624IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 4, 1)
)
uas7624IntervalEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624IntervalIndex"),
    (0, "GDCUAS7624-MIB", "uas7624IntervalNumber"),
)
if mibBuilder.loadTexts:
    uas7624IntervalEntry.setStatus("mandatory")
_Uas7624IntervalIndex_Type = SCinstance
_Uas7624IntervalIndex_Object = MibTableColumn
uas7624IntervalIndex = _Uas7624IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 4, 1, 1),
    _Uas7624IntervalIndex_Type()
)
uas7624IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624IntervalIndex.setStatus("mandatory")


class _Uas7624IntervalNumber_Type(Integer32):
    """Custom type uas7624IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Uas7624IntervalNumber_Type.__name__ = "Integer32"
_Uas7624IntervalNumber_Object = MibTableColumn
uas7624IntervalNumber = _Uas7624IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 4, 1, 2),
    _Uas7624IntervalNumber_Type()
)
uas7624IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624IntervalNumber.setStatus("mandatory")


class _Uas7624IntervalStat_Type(OctetString):
    """Custom type uas7624IntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 16),
    )


_Uas7624IntervalStat_Type.__name__ = "OctetString"
_Uas7624IntervalStat_Object = MibTableColumn
uas7624IntervalStat = _Uas7624IntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 4, 1, 3),
    _Uas7624IntervalStat_Type()
)
uas7624IntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624IntervalStat.setStatus("mandatory")
_Uas7624TotalTable_Object = MibTable
uas7624TotalTable = _Uas7624TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 5)
)
if mibBuilder.loadTexts:
    uas7624TotalTable.setStatus("mandatory")
_Uas7624TotalEntry_Object = MibTableRow
uas7624TotalEntry = _Uas7624TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 5, 1)
)
uas7624TotalEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624TotalIndex"),
)
if mibBuilder.loadTexts:
    uas7624TotalEntry.setStatus("mandatory")
_Uas7624TotalIndex_Type = SCinstance
_Uas7624TotalIndex_Object = MibTableColumn
uas7624TotalIndex = _Uas7624TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 5, 1, 1),
    _Uas7624TotalIndex_Type()
)
uas7624TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624TotalIndex.setStatus("mandatory")


class _Uas7624TotalStat_Type(OctetString):
    """Custom type uas7624TotalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 17),
    )


_Uas7624TotalStat_Type.__name__ = "OctetString"
_Uas7624TotalStat_Object = MibTableColumn
uas7624TotalStat = _Uas7624TotalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 5, 1, 2),
    _Uas7624TotalStat_Type()
)
uas7624TotalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624TotalStat.setStatus("mandatory")
_Uas7624Recent24HrTable_Object = MibTable
uas7624Recent24HrTable = _Uas7624Recent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 6)
)
if mibBuilder.loadTexts:
    uas7624Recent24HrTable.setStatus("mandatory")
_Uas7624Recent24HrEntry_Object = MibTableRow
uas7624Recent24HrEntry = _Uas7624Recent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 6, 1)
)
uas7624Recent24HrEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624Recent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7624Recent24HrEntry.setStatus("mandatory")
_Uas7624Recent24HrIndex_Type = SCinstance
_Uas7624Recent24HrIndex_Object = MibTableColumn
uas7624Recent24HrIndex = _Uas7624Recent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 6, 1, 1),
    _Uas7624Recent24HrIndex_Type()
)
uas7624Recent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624Recent24HrIndex.setStatus("mandatory")


class _Uas7624Recent24HrStat_Type(OctetString):
    """Custom type uas7624Recent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Uas7624Recent24HrStat_Type.__name__ = "OctetString"
_Uas7624Recent24HrStat_Object = MibTableColumn
uas7624Recent24HrStat = _Uas7624Recent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 5, 6, 1, 2),
    _Uas7624Recent24HrStat_Type()
)
uas7624Recent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624Recent24HrStat.setStatus("mandatory")
_Uas7624AlarmConfig_ObjectIdentity = ObjectIdentity
uas7624AlarmConfig = _Uas7624AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6)
)
_Uas7624AlarmConfigTable_Object = MibTable
uas7624AlarmConfigTable = _Uas7624AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1)
)
if mibBuilder.loadTexts:
    uas7624AlarmConfigTable.setStatus("mandatory")
_Uas7624AlarmConfigEntry_Object = MibTableRow
uas7624AlarmConfigEntry = _Uas7624AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1, 1)
)
uas7624AlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624AlarmConfigIndex"),
    (0, "GDCUAS7624-MIB", "uas7624AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7624AlarmConfigEntry.setStatus("mandatory")
_Uas7624AlarmConfigIndex_Type = SCinstance
_Uas7624AlarmConfigIndex_Object = MibTableColumn
uas7624AlarmConfigIndex = _Uas7624AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1, 1, 1),
    _Uas7624AlarmConfigIndex_Type()
)
uas7624AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624AlarmConfigIndex.setStatus("mandatory")
_Uas7624AlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7624AlarmConfigIdentifier_Object = MibTableColumn
uas7624AlarmConfigIdentifier = _Uas7624AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1, 1, 2),
    _Uas7624AlarmConfigIdentifier_Type()
)
uas7624AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624AlarmConfigIdentifier.setStatus("mandatory")


class _Uas7624AlarmCountWindow_Type(Integer32):
    """Custom type uas7624AlarmCountWindow based on Integer32"""
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
        *(("disabled", 1),
          ("infinite", 9),
          ("last10sec", 3),
          ("last15min", 6),
          ("last1hr", 7),
          ("last1min", 5),
          ("last1sec", 2),
          ("last24hr", 8),
          ("last30sec", 4))
    )


_Uas7624AlarmCountWindow_Type.__name__ = "Integer32"
_Uas7624AlarmCountWindow_Object = MibTableColumn
uas7624AlarmCountWindow = _Uas7624AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1, 1, 3),
    _Uas7624AlarmCountWindow_Type()
)
uas7624AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624AlarmCountWindow.setStatus("mandatory")


class _Uas7624AlarmCountThreshold_Type(Integer32):
    """Custom type uas7624AlarmCountThreshold based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("thres10E03", 7),
          ("thres10E04", 8),
          ("thres10E05", 9),
          ("thres10E06", 10),
          ("thresGT1", 1),
          ("thresGT10", 3),
          ("thresGT100", 4),
          ("thresGT1000", 5),
          ("thresGT10000", 6),
          ("thresGT3", 2))
    )


_Uas7624AlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7624AlarmCountThreshold_Object = MibTableColumn
uas7624AlarmCountThreshold = _Uas7624AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 1, 1, 4),
    _Uas7624AlarmCountThreshold_Type()
)
uas7624AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624AlarmCountThreshold.setStatus("mandatory")
_Uas7624LocalAlarmConfigTable_Object = MibTable
uas7624LocalAlarmConfigTable = _Uas7624LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2)
)
if mibBuilder.loadTexts:
    uas7624LocalAlarmConfigTable.setStatus("mandatory")
_Uas7624LocalAlarmConfigEntry_Object = MibTableRow
uas7624LocalAlarmConfigEntry = _Uas7624LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1)
)
uas7624LocalAlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7624-MIB", "uas7624LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7624LocalAlarmConfigEntry.setStatus("mandatory")
_Uas7624LocalAlarmConfigIndex_Type = SCinstance
_Uas7624LocalAlarmConfigIndex_Object = MibTableColumn
uas7624LocalAlarmConfigIndex = _Uas7624LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 1),
    _Uas7624LocalAlarmConfigIndex_Type()
)
uas7624LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7624LocalAlarmConfigIndex.setStatus("mandatory")


class _Uas7624LOSLocal_Type(Integer32):
    """Custom type uas7624LOSLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624LOSLocal_Type.__name__ = "Integer32"
_Uas7624LOSLocal_Object = MibTableColumn
uas7624LOSLocal = _Uas7624LOSLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 2),
    _Uas7624LOSLocal_Type()
)
uas7624LOSLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LOSLocal.setStatus("mandatory")


class _Uas7624LOFLocal_Type(Integer32):
    """Custom type uas7624LOFLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624LOFLocal_Type.__name__ = "Integer32"
_Uas7624LOFLocal_Object = MibTableColumn
uas7624LOFLocal = _Uas7624LOFLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 3),
    _Uas7624LOFLocal_Type()
)
uas7624LOFLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LOFLocal.setStatus("mandatory")


class _Uas7624AISLocal_Type(Integer32):
    """Custom type uas7624AISLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624AISLocal_Type.__name__ = "Integer32"
_Uas7624AISLocal_Object = MibTableColumn
uas7624AISLocal = _Uas7624AISLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 4),
    _Uas7624AISLocal_Type()
)
uas7624AISLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624AISLocal.setStatus("mandatory")


class _Uas7624YELLOWLocal_Type(Integer32):
    """Custom type uas7624YELLOWLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624YELLOWLocal_Type.__name__ = "Integer32"
_Uas7624YELLOWLocal_Object = MibTableColumn
uas7624YELLOWLocal = _Uas7624YELLOWLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 5),
    _Uas7624YELLOWLocal_Type()
)
uas7624YELLOWLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624YELLOWLocal.setStatus("mandatory")


class _Uas7624LineCodeViolationLocal_Type(Integer32):
    """Custom type uas7624LineCodeViolationLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624LineCodeViolationLocal_Type.__name__ = "Integer32"
_Uas7624LineCodeViolationLocal_Object = MibTableColumn
uas7624LineCodeViolationLocal = _Uas7624LineCodeViolationLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 6),
    _Uas7624LineCodeViolationLocal_Type()
)
uas7624LineCodeViolationLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624LineCodeViolationLocal.setStatus("mandatory")


class _Uas7624CRCLocal_Type(Integer32):
    """Custom type uas7624CRCLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624CRCLocal_Type.__name__ = "Integer32"
_Uas7624CRCLocal_Object = MibTableColumn
uas7624CRCLocal = _Uas7624CRCLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 7),
    _Uas7624CRCLocal_Type()
)
uas7624CRCLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624CRCLocal.setStatus("mandatory")


class _Uas7624ESLocal_Type(Integer32):
    """Custom type uas7624ESLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624ESLocal_Type.__name__ = "Integer32"
_Uas7624ESLocal_Object = MibTableColumn
uas7624ESLocal = _Uas7624ESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 10),
    _Uas7624ESLocal_Type()
)
uas7624ESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624ESLocal.setStatus("mandatory")


class _Uas7624BESLocal_Type(Integer32):
    """Custom type uas7624BESLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624BESLocal_Type.__name__ = "Integer32"
_Uas7624BESLocal_Object = MibTableColumn
uas7624BESLocal = _Uas7624BESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 11),
    _Uas7624BESLocal_Type()
)
uas7624BESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624BESLocal.setStatus("mandatory")


class _Uas7624SESLocal_Type(Integer32):
    """Custom type uas7624SESLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624SESLocal_Type.__name__ = "Integer32"
_Uas7624SESLocal_Object = MibTableColumn
uas7624SESLocal = _Uas7624SESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 12),
    _Uas7624SESLocal_Type()
)
uas7624SESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624SESLocal.setStatus("mandatory")


class _Uas7624UASLocal_Type(Integer32):
    """Custom type uas7624UASLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624UASLocal_Type.__name__ = "Integer32"
_Uas7624UASLocal_Object = MibTableColumn
uas7624UASLocal = _Uas7624UASLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 13),
    _Uas7624UASLocal_Type()
)
uas7624UASLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624UASLocal.setStatus("mandatory")


class _Uas7624OutofSyncLocal_Type(Integer32):
    """Custom type uas7624OutofSyncLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624OutofSyncLocal_Type.__name__ = "Integer32"
_Uas7624OutofSyncLocal_Object = MibTableColumn
uas7624OutofSyncLocal = _Uas7624OutofSyncLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 14),
    _Uas7624OutofSyncLocal_Type()
)
uas7624OutofSyncLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624OutofSyncLocal.setStatus("mandatory")


class _Uas7624NoSealingCurrentLocal_Type(Integer32):
    """Custom type uas7624NoSealingCurrentLocal based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7624NoSealingCurrentLocal_Type.__name__ = "Integer32"
_Uas7624NoSealingCurrentLocal_Object = MibTableColumn
uas7624NoSealingCurrentLocal = _Uas7624NoSealingCurrentLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 18, 1, 6, 2, 1, 15),
    _Uas7624NoSealingCurrentLocal_Type()
)
uas7624NoSealingCurrentLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7624NoSealingCurrentLocal.setStatus("mandatory")
_Uas7624_ObjectIdentity = ObjectIdentity
uas7624 = _Uas7624_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2)
)
_Uas7624Alarms_ObjectIdentity = ObjectIdentity
uas7624Alarms = _Uas7624Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1)
)
_Uas7624NoResponseAlm_ObjectIdentity = ObjectIdentity
uas7624NoResponseAlm = _Uas7624NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 1)
)
_Uas7624DiagRxErrAlm_ObjectIdentity = ObjectIdentity
uas7624DiagRxErrAlm = _Uas7624DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 2)
)
_Uas7624PowerUpAlm_ObjectIdentity = ObjectIdentity
uas7624PowerUpAlm = _Uas7624PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 3)
)
_Uas7624LossOfSignalAlm_ObjectIdentity = ObjectIdentity
uas7624LossOfSignalAlm = _Uas7624LossOfSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 4)
)
_Uas7624LossOfFrameAlm_ObjectIdentity = ObjectIdentity
uas7624LossOfFrameAlm = _Uas7624LossOfFrameAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 5)
)
_Uas7624AisAlm_ObjectIdentity = ObjectIdentity
uas7624AisAlm = _Uas7624AisAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 6)
)
_Uas7624YellowAlm_ObjectIdentity = ObjectIdentity
uas7624YellowAlm = _Uas7624YellowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 7)
)
_Uas7624OutofSyncAlm_ObjectIdentity = ObjectIdentity
uas7624OutofSyncAlm = _Uas7624OutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 8)
)
_Uas7624SealingCurrentNoContAlm_ObjectIdentity = ObjectIdentity
uas7624SealingCurrentNoContAlm = _Uas7624SealingCurrentNoContAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 9)
)
_Uas7624UASAlm_ObjectIdentity = ObjectIdentity
uas7624UASAlm = _Uas7624UASAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 10)
)
_Uas7624ESAlm_ObjectIdentity = ObjectIdentity
uas7624ESAlm = _Uas7624ESAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 11)
)
_Uas7624LineCodeViolationAlm_ObjectIdentity = ObjectIdentity
uas7624LineCodeViolationAlm = _Uas7624LineCodeViolationAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 12)
)
_Uas7624CRCAlm_ObjectIdentity = ObjectIdentity
uas7624CRCAlm = _Uas7624CRCAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 13)
)
_Uas7624BESAlm_ObjectIdentity = ObjectIdentity
uas7624BESAlm = _Uas7624BESAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 14)
)
_Uas7624SESAlm_ObjectIdentity = ObjectIdentity
uas7624SESAlm = _Uas7624SESAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 15)
)
_Uas7624MajorBERAlm_ObjectIdentity = ObjectIdentity
uas7624MajorBERAlm = _Uas7624MajorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 16)
)
_Uas7624MinorBERAlm_ObjectIdentity = ObjectIdentity
uas7624MinorBERAlm = _Uas7624MinorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 18, 2, 1, 17)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCUAS7624-MIB",
    **{"gdc": gdc,
       "niudiu": niudiu,
       "uas7624System": uas7624System,
       "uas7624Version": uas7624Version,
       "uas7624MIBversion": uas7624MIBversion,
       "uas7624VersionTable": uas7624VersionTable,
       "uas7624VersionEntry": uas7624VersionEntry,
       "uas7624VersionIndex": uas7624VersionIndex,
       "uas7624FirmwareRev": uas7624FirmwareRev,
       "uas7624CardType": uas7624CardType,
       "uas7624BootRev": uas7624BootRev,
       "uas7624Maintenance": uas7624Maintenance,
       "uas7624MaintenanceTable": uas7624MaintenanceTable,
       "uas7624MaintenanceEntry": uas7624MaintenanceEntry,
       "uas7624MaintenanceLineIndex": uas7624MaintenanceLineIndex,
       "uas7624SoftReset": uas7624SoftReset,
       "uas7624DefaultInit": uas7624DefaultInit,
       "uas7624ResetMajorAlarm": uas7624ResetMajorAlarm,
       "uas7624ResetMinorAlarm": uas7624ResetMinorAlarm,
       "uas7624ResetStatistics": uas7624ResetStatistics,
       "uas7624StatLastInitialized": uas7624StatLastInitialized,
       "uas7624ValidIntervals": uas7624ValidIntervals,
       "uas7624SysUpTime": uas7624SysUpTime,
       "uas7624LedStatus": uas7624LedStatus,
       "uas7624AlarmStatus": uas7624AlarmStatus,
       "uas7624LoopState": uas7624LoopState,
       "uas7624ConfigMode": uas7624ConfigMode,
       "uas7624Configuration": uas7624Configuration,
       "uas7624ConfigTable": uas7624ConfigTable,
       "uas7624ConfigEntry": uas7624ConfigEntry,
       "uas7624ConfigIndex": uas7624ConfigIndex,
       "uas7624NetworkInterfaceType": uas7624NetworkInterfaceType,
       "uas7624TransmitClockSource": uas7624TransmitClockSource,
       "uas7624PreEqualization": uas7624PreEqualization,
       "uas7624Framing": uas7624Framing,
       "uas7624LineCoding": uas7624LineCoding,
       "uas7624LineBuildout": uas7624LineBuildout,
       "uas7624FDLMode": uas7624FDLMode,
       "uas7624Loopback": uas7624Loopback,
       "uas7624AISLoopdown": uas7624AISLoopdown,
       "uas7624LineBuildoutMode": uas7624LineBuildoutMode,
       "uas7624FramingMode": uas7624FramingMode,
       "uas7624Diagnostics": uas7624Diagnostics,
       "uas7624DiagTable": uas7624DiagTable,
       "uas7624DiagEntry": uas7624DiagEntry,
       "uas7624DiagIndex": uas7624DiagIndex,
       "uas7624DiagConfig": uas7624DiagConfig,
       "uas7624T1TestLimit": uas7624T1TestLimit,
       "uas7624T1TestExecutionStatus": uas7624T1TestExecutionStatus,
       "uas7624T1TestExceptions": uas7624T1TestExceptions,
       "uas7624TestResults": uas7624TestResults,
       "uas7624ResetTestResults": uas7624ResetTestResults,
       "uas7624Performance": uas7624Performance,
       "uas7624CurrentTable": uas7624CurrentTable,
       "uas7624CurrentEntry": uas7624CurrentEntry,
       "uas7624CurrentIndex": uas7624CurrentIndex,
       "uas7624CurrentStat": uas7624CurrentStat,
       "uas7624IntervalTable": uas7624IntervalTable,
       "uas7624IntervalEntry": uas7624IntervalEntry,
       "uas7624IntervalIndex": uas7624IntervalIndex,
       "uas7624IntervalNumber": uas7624IntervalNumber,
       "uas7624IntervalStat": uas7624IntervalStat,
       "uas7624TotalTable": uas7624TotalTable,
       "uas7624TotalEntry": uas7624TotalEntry,
       "uas7624TotalIndex": uas7624TotalIndex,
       "uas7624TotalStat": uas7624TotalStat,
       "uas7624Recent24HrTable": uas7624Recent24HrTable,
       "uas7624Recent24HrEntry": uas7624Recent24HrEntry,
       "uas7624Recent24HrIndex": uas7624Recent24HrIndex,
       "uas7624Recent24HrStat": uas7624Recent24HrStat,
       "uas7624AlarmConfig": uas7624AlarmConfig,
       "uas7624AlarmConfigTable": uas7624AlarmConfigTable,
       "uas7624AlarmConfigEntry": uas7624AlarmConfigEntry,
       "uas7624AlarmConfigIndex": uas7624AlarmConfigIndex,
       "uas7624AlarmConfigIdentifier": uas7624AlarmConfigIdentifier,
       "uas7624AlarmCountWindow": uas7624AlarmCountWindow,
       "uas7624AlarmCountThreshold": uas7624AlarmCountThreshold,
       "uas7624LocalAlarmConfigTable": uas7624LocalAlarmConfigTable,
       "uas7624LocalAlarmConfigEntry": uas7624LocalAlarmConfigEntry,
       "uas7624LocalAlarmConfigIndex": uas7624LocalAlarmConfigIndex,
       "uas7624LOSLocal": uas7624LOSLocal,
       "uas7624LOFLocal": uas7624LOFLocal,
       "uas7624AISLocal": uas7624AISLocal,
       "uas7624YELLOWLocal": uas7624YELLOWLocal,
       "uas7624LineCodeViolationLocal": uas7624LineCodeViolationLocal,
       "uas7624CRCLocal": uas7624CRCLocal,
       "uas7624ESLocal": uas7624ESLocal,
       "uas7624BESLocal": uas7624BESLocal,
       "uas7624SESLocal": uas7624SESLocal,
       "uas7624UASLocal": uas7624UASLocal,
       "uas7624OutofSyncLocal": uas7624OutofSyncLocal,
       "uas7624NoSealingCurrentLocal": uas7624NoSealingCurrentLocal,
       "uas7624": uas7624,
       "uas7624Alarms": uas7624Alarms,
       "uas7624NoResponseAlm": uas7624NoResponseAlm,
       "uas7624DiagRxErrAlm": uas7624DiagRxErrAlm,
       "uas7624PowerUpAlm": uas7624PowerUpAlm,
       "uas7624LossOfSignalAlm": uas7624LossOfSignalAlm,
       "uas7624LossOfFrameAlm": uas7624LossOfFrameAlm,
       "uas7624AisAlm": uas7624AisAlm,
       "uas7624YellowAlm": uas7624YellowAlm,
       "uas7624OutofSyncAlm": uas7624OutofSyncAlm,
       "uas7624SealingCurrentNoContAlm": uas7624SealingCurrentNoContAlm,
       "uas7624UASAlm": uas7624UASAlm,
       "uas7624ESAlm": uas7624ESAlm,
       "uas7624LineCodeViolationAlm": uas7624LineCodeViolationAlm,
       "uas7624CRCAlm": uas7624CRCAlm,
       "uas7624BESAlm": uas7624BESAlm,
       "uas7624SESAlm": uas7624SESAlm,
       "uas7624MajorBERAlm": uas7624MajorBERAlm,
       "uas7624MinorBERAlm": uas7624MinorBERAlm}
)
