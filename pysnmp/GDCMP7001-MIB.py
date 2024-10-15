# SNMP MIB module (GDCMP7001-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCMP7001-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:17 2024
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
_Dsx1_ObjectIdentity = ObjectIdentity
dsx1 = _Dsx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6)
)
_Mp7001System_ObjectIdentity = ObjectIdentity
mp7001System = _Mp7001System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10)
)
_Mp7001Version_ObjectIdentity = ObjectIdentity
mp7001Version = _Mp7001Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1)
)


class _Mp7001MIBversion_Type(DisplayString):
    """Custom type mp7001MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Mp7001MIBversion_Type.__name__ = "DisplayString"
_Mp7001MIBversion_Object = MibScalar
mp7001MIBversion = _Mp7001MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 1),
    _Mp7001MIBversion_Type()
)
mp7001MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001MIBversion.setStatus("mandatory")
_Mp7001VersionTable_Object = MibTable
mp7001VersionTable = _Mp7001VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2)
)
if mibBuilder.loadTexts:
    mp7001VersionTable.setStatus("mandatory")
_Mp7001VersionEntry_Object = MibTableRow
mp7001VersionEntry = _Mp7001VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2, 1)
)
mp7001VersionEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001VersionIndex"),
)
if mibBuilder.loadTexts:
    mp7001VersionEntry.setStatus("mandatory")
_Mp7001VersionIndex_Type = SCinstance
_Mp7001VersionIndex_Object = MibTableColumn
mp7001VersionIndex = _Mp7001VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2, 1, 1),
    _Mp7001VersionIndex_Type()
)
mp7001VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001VersionIndex.setStatus("mandatory")


class _Mp7001FirmwareRev_Type(DisplayString):
    """Custom type mp7001FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Mp7001FirmwareRev_Type.__name__ = "DisplayString"
_Mp7001FirmwareRev_Object = MibTableColumn
mp7001FirmwareRev = _Mp7001FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2, 1, 2),
    _Mp7001FirmwareRev_Type()
)
mp7001FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001FirmwareRev.setStatus("mandatory")


class _Mp7001CardType_Type(DisplayString):
    """Custom type mp7001CardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Mp7001CardType_Type.__name__ = "DisplayString"
_Mp7001CardType_Object = MibTableColumn
mp7001CardType = _Mp7001CardType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2, 1, 3),
    _Mp7001CardType_Type()
)
mp7001CardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001CardType.setStatus("mandatory")


class _Mp7001BootRev_Type(DisplayString):
    """Custom type mp7001BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Mp7001BootRev_Type.__name__ = "DisplayString"
_Mp7001BootRev_Object = MibTableColumn
mp7001BootRev = _Mp7001BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 1, 2, 1, 4),
    _Mp7001BootRev_Type()
)
mp7001BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001BootRev.setStatus("mandatory")
_Mp7001Maintenance_ObjectIdentity = ObjectIdentity
mp7001Maintenance = _Mp7001Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2)
)
_Mp7001MaintenanceTable_Object = MibTable
mp7001MaintenanceTable = _Mp7001MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mp7001MaintenanceTable.setStatus("mandatory")
_Mp7001MaintenanceEntry_Object = MibTableRow
mp7001MaintenanceEntry = _Mp7001MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1)
)
mp7001MaintenanceEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    mp7001MaintenanceEntry.setStatus("mandatory")
_Mp7001MaintenanceLineIndex_Type = SCinstance
_Mp7001MaintenanceLineIndex_Object = MibTableColumn
mp7001MaintenanceLineIndex = _Mp7001MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 1),
    _Mp7001MaintenanceLineIndex_Type()
)
mp7001MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001MaintenanceLineIndex.setStatus("mandatory")


class _Mp7001SoftReset_Type(Integer32):
    """Custom type mp7001SoftReset based on Integer32"""
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


_Mp7001SoftReset_Type.__name__ = "Integer32"
_Mp7001SoftReset_Object = MibTableColumn
mp7001SoftReset = _Mp7001SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 2),
    _Mp7001SoftReset_Type()
)
mp7001SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001SoftReset.setStatus("mandatory")


class _Mp7001SysUpTime_Type(Integer32):
    """Custom type mp7001SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7001SysUpTime_Type.__name__ = "Integer32"
_Mp7001SysUpTime_Object = MibTableColumn
mp7001SysUpTime = _Mp7001SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 3),
    _Mp7001SysUpTime_Type()
)
mp7001SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001SysUpTime.setStatus("mandatory")


class _Mp7001DefaultInit_Type(Integer32):
    """Custom type mp7001DefaultInit based on Integer32"""
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


_Mp7001DefaultInit_Type.__name__ = "Integer32"
_Mp7001DefaultInit_Object = MibTableColumn
mp7001DefaultInit = _Mp7001DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 4),
    _Mp7001DefaultInit_Type()
)
mp7001DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001DefaultInit.setStatus("mandatory")


class _Mp7001ResetStats_Type(Integer32):
    """Custom type mp7001ResetStats based on Integer32"""
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


_Mp7001ResetStats_Type.__name__ = "Integer32"
_Mp7001ResetStats_Object = MibTableColumn
mp7001ResetStats = _Mp7001ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 5),
    _Mp7001ResetStats_Type()
)
mp7001ResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001ResetStats.setStatus("mandatory")


class _Mp7001LedStatus_Type(OctetString):
    """Custom type mp7001LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Mp7001LedStatus_Type.__name__ = "OctetString"
_Mp7001LedStatus_Object = MibTableColumn
mp7001LedStatus = _Mp7001LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 6),
    _Mp7001LedStatus_Type()
)
mp7001LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001LedStatus.setStatus("mandatory")


class _Mp7001T1CircuitName_Type(DisplayString):
    """Custom type mp7001T1CircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7001T1CircuitName_Type.__name__ = "DisplayString"
_Mp7001T1CircuitName_Object = MibTableColumn
mp7001T1CircuitName = _Mp7001T1CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 7),
    _Mp7001T1CircuitName_Type()
)
mp7001T1CircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001T1CircuitName.setStatus("mandatory")


class _Mp7001SetRealTime_Type(Integer32):
    """Custom type mp7001SetRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7001SetRealTime_Type.__name__ = "Integer32"
_Mp7001SetRealTime_Object = MibTableColumn
mp7001SetRealTime = _Mp7001SetRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 8),
    _Mp7001SetRealTime_Type()
)
mp7001SetRealTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001SetRealTime.setStatus("mandatory")


class _Mp7001AlarmStatus_Type(OctetString):
    """Custom type mp7001AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Mp7001AlarmStatus_Type.__name__ = "OctetString"
_Mp7001AlarmStatus_Object = MibTableColumn
mp7001AlarmStatus = _Mp7001AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 9),
    _Mp7001AlarmStatus_Type()
)
mp7001AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001AlarmStatus.setStatus("mandatory")


class _Mp7001SystemTimingGenStatus_Type(Integer32):
    """Custom type mp7001SystemTimingGenStatus based on Integer32"""
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
        *(("clk4mhz", 3),
          ("clk8khz", 2),
          ("clk8khzand4mhz", 4),
          ("none", 1))
    )


_Mp7001SystemTimingGenStatus_Type.__name__ = "Integer32"
_Mp7001SystemTimingGenStatus_Object = MibTableColumn
mp7001SystemTimingGenStatus = _Mp7001SystemTimingGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 10),
    _Mp7001SystemTimingGenStatus_Type()
)
mp7001SystemTimingGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001SystemTimingGenStatus.setStatus("mandatory")


class _Mp7001StatLastInitialized_Type(Integer32):
    """Custom type mp7001StatLastInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7001StatLastInitialized_Type.__name__ = "Integer32"
_Mp7001StatLastInitialized_Object = MibTableColumn
mp7001StatLastInitialized = _Mp7001StatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 11),
    _Mp7001StatLastInitialized_Type()
)
mp7001StatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001StatLastInitialized.setStatus("mandatory")


class _Mp7001ValidIntervals_Type(Integer32):
    """Custom type mp7001ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Mp7001ValidIntervals_Type.__name__ = "Integer32"
_Mp7001ValidIntervals_Object = MibTableColumn
mp7001ValidIntervals = _Mp7001ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 2, 1, 1, 12),
    _Mp7001ValidIntervals_Type()
)
mp7001ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001ValidIntervals.setStatus("mandatory")
_Mp7001Configuration_ObjectIdentity = ObjectIdentity
mp7001Configuration = _Mp7001Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3)
)
_Mp7001ConfigTable_Object = MibTable
mp7001ConfigTable = _Mp7001ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1)
)
if mibBuilder.loadTexts:
    mp7001ConfigTable.setStatus("mandatory")
_Mp7001ConfigEntry_Object = MibTableRow
mp7001ConfigEntry = _Mp7001ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1)
)
mp7001ConfigEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001ConfigIndex"),
)
if mibBuilder.loadTexts:
    mp7001ConfigEntry.setStatus("mandatory")
_Mp7001ConfigIndex_Type = SCinstance
_Mp7001ConfigIndex_Object = MibTableColumn
mp7001ConfigIndex = _Mp7001ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 1),
    _Mp7001ConfigIndex_Type()
)
mp7001ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001ConfigIndex.setStatus("mandatory")


class _Mp7001NetworkInterfaceType_Type(Integer32):
    """Custom type mp7001NetworkInterfaceType based on Integer32"""
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


_Mp7001NetworkInterfaceType_Type.__name__ = "Integer32"
_Mp7001NetworkInterfaceType_Object = MibTableColumn
mp7001NetworkInterfaceType = _Mp7001NetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 2),
    _Mp7001NetworkInterfaceType_Type()
)
mp7001NetworkInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001NetworkInterfaceType.setStatus("mandatory")


class _Mp7001TransmitClockSource_Type(Integer32):
    """Custom type mp7001TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("recovered", 2),
          ("system", 1))
    )


_Mp7001TransmitClockSource_Type.__name__ = "Integer32"
_Mp7001TransmitClockSource_Object = MibTableColumn
mp7001TransmitClockSource = _Mp7001TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 3),
    _Mp7001TransmitClockSource_Type()
)
mp7001TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001TransmitClockSource.setStatus("mandatory")


class _Mp7001FallbackClockSource_Type(Integer32):
    """Custom type mp7001FallbackClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("recovered", 2),
          ("system", 1))
    )


_Mp7001FallbackClockSource_Type.__name__ = "Integer32"
_Mp7001FallbackClockSource_Object = MibTableColumn
mp7001FallbackClockSource = _Mp7001FallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 4),
    _Mp7001FallbackClockSource_Type()
)
mp7001FallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001FallbackClockSource.setStatus("mandatory")


class _Mp7001PreEqualization_Type(Integer32):
    """Custom type mp7001PreEqualization based on Integer32"""
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


_Mp7001PreEqualization_Type.__name__ = "Integer32"
_Mp7001PreEqualization_Object = MibTableColumn
mp7001PreEqualization = _Mp7001PreEqualization_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 5),
    _Mp7001PreEqualization_Type()
)
mp7001PreEqualization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001PreEqualization.setStatus("mandatory")


class _Mp7001Framing_Type(Integer32):
    """Custom type mp7001Framing based on Integer32"""
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


_Mp7001Framing_Type.__name__ = "Integer32"
_Mp7001Framing_Object = MibTableColumn
mp7001Framing = _Mp7001Framing_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 6),
    _Mp7001Framing_Type()
)
mp7001Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001Framing.setStatus("mandatory")


class _Mp7001LineCoding_Type(Integer32):
    """Custom type mp7001LineCoding based on Integer32"""
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


_Mp7001LineCoding_Type.__name__ = "Integer32"
_Mp7001LineCoding_Object = MibTableColumn
mp7001LineCoding = _Mp7001LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 7),
    _Mp7001LineCoding_Type()
)
mp7001LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001LineCoding.setStatus("mandatory")


class _Mp7001LineBuildout_Type(Integer32):
    """Custom type mp7001LineBuildout based on Integer32"""
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


_Mp7001LineBuildout_Type.__name__ = "Integer32"
_Mp7001LineBuildout_Object = MibTableColumn
mp7001LineBuildout = _Mp7001LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 8),
    _Mp7001LineBuildout_Type()
)
mp7001LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001LineBuildout.setStatus("mandatory")


class _Mp7001FDLMode_Type(Integer32):
    """Custom type mp7001FDLMode based on Integer32"""
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


_Mp7001FDLMode_Type.__name__ = "Integer32"
_Mp7001FDLMode_Object = MibTableColumn
mp7001FDLMode = _Mp7001FDLMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 9),
    _Mp7001FDLMode_Type()
)
mp7001FDLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001FDLMode.setStatus("mandatory")


class _Mp7001FramingMode_Type(Integer32):
    """Custom type mp7001FramingMode based on Integer32"""
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


_Mp7001FramingMode_Type.__name__ = "Integer32"
_Mp7001FramingMode_Object = MibTableColumn
mp7001FramingMode = _Mp7001FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 10),
    _Mp7001FramingMode_Type()
)
mp7001FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001FramingMode.setStatus("mandatory")


class _Mp7001Loopback_Type(Integer32):
    """Custom type mp7001Loopback based on Integer32"""
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


_Mp7001Loopback_Type.__name__ = "Integer32"
_Mp7001Loopback_Object = MibTableColumn
mp7001Loopback = _Mp7001Loopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 11),
    _Mp7001Loopback_Type()
)
mp7001Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001Loopback.setStatus("mandatory")


class _Mp7001AISLoopdown_Type(Integer32):
    """Custom type mp7001AISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Mp7001AISLoopdown_Type.__name__ = "Integer32"
_Mp7001AISLoopdown_Object = MibTableColumn
mp7001AISLoopdown = _Mp7001AISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 12),
    _Mp7001AISLoopdown_Type()
)
mp7001AISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001AISLoopdown.setStatus("mandatory")


class _Mp7001SignalMode_Type(Integer32):
    """Custom type mp7001SignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("robbedbit", 2))
    )


_Mp7001SignalMode_Type.__name__ = "Integer32"
_Mp7001SignalMode_Object = MibTableColumn
mp7001SignalMode = _Mp7001SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 13),
    _Mp7001SignalMode_Type()
)
mp7001SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001SignalMode.setStatus("mandatory")


class _Mp7001LineBuildoutCtrl_Type(Integer32):
    """Custom type mp7001LineBuildoutCtrl based on Integer32"""
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


_Mp7001LineBuildoutCtrl_Type.__name__ = "Integer32"
_Mp7001LineBuildoutCtrl_Object = MibTableColumn
mp7001LineBuildoutCtrl = _Mp7001LineBuildoutCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 1, 1, 14),
    _Mp7001LineBuildoutCtrl_Type()
)
mp7001LineBuildoutCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001LineBuildoutCtrl.setStatus("mandatory")
_Mp7001DCCConfigurationTable_Object = MibTable
mp7001DCCConfigurationTable = _Mp7001DCCConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 2)
)
if mibBuilder.loadTexts:
    mp7001DCCConfigurationTable.setStatus("mandatory")
_Mp7001DCCConfigurationEntry_Object = MibTableRow
mp7001DCCConfigurationEntry = _Mp7001DCCConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 2, 1)
)
mp7001DCCConfigurationEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001DCCConfigurationIndex"),
)
if mibBuilder.loadTexts:
    mp7001DCCConfigurationEntry.setStatus("mandatory")
_Mp7001DCCConfigurationIndex_Type = SCinstance
_Mp7001DCCConfigurationIndex_Object = MibTableColumn
mp7001DCCConfigurationIndex = _Mp7001DCCConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 2, 1, 1),
    _Mp7001DCCConfigurationIndex_Type()
)
mp7001DCCConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001DCCConfigurationIndex.setStatus("mandatory")


class _Mp7001TimeSlot_Type(Integer32):
    """Custom type mp7001TimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Mp7001TimeSlot_Type.__name__ = "Integer32"
_Mp7001TimeSlot_Object = MibTableColumn
mp7001TimeSlot = _Mp7001TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 2, 1, 2),
    _Mp7001TimeSlot_Type()
)
mp7001TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001TimeSlot.setStatus("mandatory")


class _Mp7001Bandwidth_Type(Integer32):
    """Custom type mp7001Bandwidth based on Integer32"""
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
        *(("kbps56", 2),
          ("kbps64", 3),
          ("kbps8", 1),
          ("notAssigned", 4))
    )


_Mp7001Bandwidth_Type.__name__ = "Integer32"
_Mp7001Bandwidth_Object = MibTableColumn
mp7001Bandwidth = _Mp7001Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 3, 2, 1, 3),
    _Mp7001Bandwidth_Type()
)
mp7001Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001Bandwidth.setStatus("mandatory")
_Mp7001Diagnostics_ObjectIdentity = ObjectIdentity
mp7001Diagnostics = _Mp7001Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4)
)
_Mp7001DiagTable_Object = MibTable
mp7001DiagTable = _Mp7001DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1)
)
if mibBuilder.loadTexts:
    mp7001DiagTable.setStatus("mandatory")
_Mp7001DiagEntry_Object = MibTableRow
mp7001DiagEntry = _Mp7001DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1)
)
mp7001DiagEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001DiagIndex"),
)
if mibBuilder.loadTexts:
    mp7001DiagEntry.setStatus("mandatory")
_Mp7001DiagIndex_Type = SCinstance
_Mp7001DiagIndex_Object = MibTableColumn
mp7001DiagIndex = _Mp7001DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 1),
    _Mp7001DiagIndex_Type()
)
mp7001DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001DiagIndex.setStatus("mandatory")


class _Mp7001TestPattern_Type(Integer32):
    """Custom type mp7001TestPattern based on Integer32"""
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
        *(("ds0Delay", 10),
          ("inbandCode", 6),
          ("noCode", 1),
          ("ntwkInterfaceCode", 8),
          ("pat2047", 3),
          ("pat3in24", 5),
          ("pat511", 2),
          ("patQRSS", 4),
          ("resetInband", 7),
          ("resetNtwkInterface", 9))
    )


_Mp7001TestPattern_Type.__name__ = "Integer32"
_Mp7001TestPattern_Object = MibTableColumn
mp7001TestPattern = _Mp7001TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 2),
    _Mp7001TestPattern_Type()
)
mp7001TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001TestPattern.setStatus("mandatory")


class _Mp7001DiagConfig_Type(Integer32):
    """Custom type mp7001DiagConfig based on Integer32"""
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
        *(("cascadeLoopback", 5),
          ("dsoLoopback", 4),
          ("lineLoopback", 2),
          ("localTest", 6),
          ("noLoop", 1),
          ("payloadLoopback", 3))
    )


_Mp7001DiagConfig_Type.__name__ = "Integer32"
_Mp7001DiagConfig_Object = MibTableColumn
mp7001DiagConfig = _Mp7001DiagConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 3),
    _Mp7001DiagConfig_Type()
)
mp7001DiagConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001DiagConfig.setStatus("mandatory")


class _Mp7001TestLimit_Type(Integer32):
    """Custom type mp7001TestLimit based on Integer32"""
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


_Mp7001TestLimit_Type.__name__ = "Integer32"
_Mp7001TestLimit_Object = MibTableColumn
mp7001TestLimit = _Mp7001TestLimit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 4),
    _Mp7001TestLimit_Type()
)
mp7001TestLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001TestLimit.setStatus("mandatory")


class _Mp7001TestExecutionStatus_Type(Integer32):
    """Custom type mp7001TestExecutionStatus based on Integer32"""
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


_Mp7001TestExecutionStatus_Type.__name__ = "Integer32"
_Mp7001TestExecutionStatus_Object = MibTableColumn
mp7001TestExecutionStatus = _Mp7001TestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 5),
    _Mp7001TestExecutionStatus_Type()
)
mp7001TestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001TestExecutionStatus.setStatus("mandatory")


class _Mp7001TestExceptions_Type(Integer32):
    """Custom type mp7001TestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mp7001TestExceptions_Type.__name__ = "Integer32"
_Mp7001TestExceptions_Object = MibTableColumn
mp7001TestExceptions = _Mp7001TestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 6),
    _Mp7001TestExceptions_Type()
)
mp7001TestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001TestExceptions.setStatus("mandatory")


class _Mp7001TestResults_Type(Integer32):
    """Custom type mp7001TestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_Mp7001TestResults_Type.__name__ = "Integer32"
_Mp7001TestResults_Object = MibTableColumn
mp7001TestResults = _Mp7001TestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 7),
    _Mp7001TestResults_Type()
)
mp7001TestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001TestResults.setStatus("mandatory")


class _Mp7001ResetTestResults_Type(Integer32):
    """Custom type mp7001ResetTestResults based on Integer32"""
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


_Mp7001ResetTestResults_Type.__name__ = "Integer32"
_Mp7001ResetTestResults_Object = MibTableColumn
mp7001ResetTestResults = _Mp7001ResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 8),
    _Mp7001ResetTestResults_Type()
)
mp7001ResetTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001ResetTestResults.setStatus("mandatory")


class _Mp7001DS0Diag_Type(Integer32):
    """Custom type mp7001DS0Diag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Mp7001DS0Diag_Type.__name__ = "Integer32"
_Mp7001DS0Diag_Object = MibTableColumn
mp7001DS0Diag = _Mp7001DS0Diag_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 4, 1, 1, 9),
    _Mp7001DS0Diag_Type()
)
mp7001DS0Diag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001DS0Diag.setStatus("mandatory")
_Mp7001Performance_ObjectIdentity = ObjectIdentity
mp7001Performance = _Mp7001Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5)
)
_Mp7001InboundANSIperfTable_Object = MibTable
mp7001InboundANSIperfTable = _Mp7001InboundANSIperfTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1)
)
if mibBuilder.loadTexts:
    mp7001InboundANSIperfTable.setStatus("mandatory")
_Mp7001InboundANSIperfEntry_Object = MibTableRow
mp7001InboundANSIperfEntry = _Mp7001InboundANSIperfEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1)
)
mp7001InboundANSIperfEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001InboundANSIperfIndex"),
    (0, "GDCMP7001-MIB", "mp7001InboundANSIseconds"),
)
if mibBuilder.loadTexts:
    mp7001InboundANSIperfEntry.setStatus("mandatory")
_Mp7001InboundANSIperfIndex_Type = SCinstance
_Mp7001InboundANSIperfIndex_Object = MibTableColumn
mp7001InboundANSIperfIndex = _Mp7001InboundANSIperfIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 1),
    _Mp7001InboundANSIperfIndex_Type()
)
mp7001InboundANSIperfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIperfIndex.setStatus("mandatory")


class _Mp7001InboundANSIseconds_Type(Integer32):
    """Custom type mp7001InboundANSIseconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Mp7001InboundANSIseconds_Type.__name__ = "Integer32"
_Mp7001InboundANSIseconds_Object = MibTableColumn
mp7001InboundANSIseconds = _Mp7001InboundANSIseconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 2),
    _Mp7001InboundANSIseconds_Type()
)
mp7001InboundANSIseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIseconds.setStatus("mandatory")


class _Mp7001InboundANSICRCerrorEvents_Type(Integer32):
    """Custom type mp7001InboundANSICRCerrorEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("errors1", 2),
          ("errors101to320", 32),
          ("errors11to100", 16),
          ("errors2to5", 4),
          ("errors321orMore", 64),
          ("errors6to10", 8),
          ("noErrors", 1))
    )


_Mp7001InboundANSICRCerrorEvents_Type.__name__ = "Integer32"
_Mp7001InboundANSICRCerrorEvents_Object = MibTableColumn
mp7001InboundANSICRCerrorEvents = _Mp7001InboundANSICRCerrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 3),
    _Mp7001InboundANSICRCerrorEvents_Type()
)
mp7001InboundANSICRCerrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSICRCerrorEvents.setStatus("mandatory")


class _Mp7001InboundANSIsevereErrors_Type(Integer32):
    """Custom type mp7001InboundANSIsevereErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001InboundANSIsevereErrors_Type.__name__ = "Integer32"
_Mp7001InboundANSIsevereErrors_Object = MibTableColumn
mp7001InboundANSIsevereErrors = _Mp7001InboundANSIsevereErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 4),
    _Mp7001InboundANSIsevereErrors_Type()
)
mp7001InboundANSIsevereErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIsevereErrors.setStatus("mandatory")


class _Mp7001InboundANSIframeErrors_Type(Integer32):
    """Custom type mp7001InboundANSIframeErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001InboundANSIframeErrors_Type.__name__ = "Integer32"
_Mp7001InboundANSIframeErrors_Object = MibTableColumn
mp7001InboundANSIframeErrors = _Mp7001InboundANSIframeErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 5),
    _Mp7001InboundANSIframeErrors_Type()
)
mp7001InboundANSIframeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIframeErrors.setStatus("mandatory")


class _Mp7001InboundANSIcodeViolations_Type(Integer32):
    """Custom type mp7001InboundANSIcodeViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001InboundANSIcodeViolations_Type.__name__ = "Integer32"
_Mp7001InboundANSIcodeViolations_Object = MibTableColumn
mp7001InboundANSIcodeViolations = _Mp7001InboundANSIcodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 6),
    _Mp7001InboundANSIcodeViolations_Type()
)
mp7001InboundANSIcodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIcodeViolations.setStatus("mandatory")


class _Mp7001InboundANSIcontrolledSlips_Type(Integer32):
    """Custom type mp7001InboundANSIcontrolledSlips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001InboundANSIcontrolledSlips_Type.__name__ = "Integer32"
_Mp7001InboundANSIcontrolledSlips_Object = MibTableColumn
mp7001InboundANSIcontrolledSlips = _Mp7001InboundANSIcontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 7),
    _Mp7001InboundANSIcontrolledSlips_Type()
)
mp7001InboundANSIcontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIcontrolledSlips.setStatus("mandatory")


class _Mp7001InboundANSIactivePayloadLoops_Type(Integer32):
    """Custom type mp7001InboundANSIactivePayloadLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001InboundANSIactivePayloadLoops_Type.__name__ = "Integer32"
_Mp7001InboundANSIactivePayloadLoops_Object = MibTableColumn
mp7001InboundANSIactivePayloadLoops = _Mp7001InboundANSIactivePayloadLoops_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 1, 1, 8),
    _Mp7001InboundANSIactivePayloadLoops_Type()
)
mp7001InboundANSIactivePayloadLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001InboundANSIactivePayloadLoops.setStatus("mandatory")
_Mp7001OutboundANSIperfTable_Object = MibTable
mp7001OutboundANSIperfTable = _Mp7001OutboundANSIperfTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2)
)
if mibBuilder.loadTexts:
    mp7001OutboundANSIperfTable.setStatus("mandatory")
_Mp7001OutboundANSIperfEntry_Object = MibTableRow
mp7001OutboundANSIperfEntry = _Mp7001OutboundANSIperfEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1)
)
mp7001OutboundANSIperfEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001OutboundANSIperfIndex"),
    (0, "GDCMP7001-MIB", "mp7001OutboundANSIseconds"),
)
if mibBuilder.loadTexts:
    mp7001OutboundANSIperfEntry.setStatus("mandatory")
_Mp7001OutboundANSIperfIndex_Type = SCinstance
_Mp7001OutboundANSIperfIndex_Object = MibTableColumn
mp7001OutboundANSIperfIndex = _Mp7001OutboundANSIperfIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 1),
    _Mp7001OutboundANSIperfIndex_Type()
)
mp7001OutboundANSIperfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIperfIndex.setStatus("mandatory")


class _Mp7001OutboundANSIseconds_Type(Integer32):
    """Custom type mp7001OutboundANSIseconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Mp7001OutboundANSIseconds_Type.__name__ = "Integer32"
_Mp7001OutboundANSIseconds_Object = MibTableColumn
mp7001OutboundANSIseconds = _Mp7001OutboundANSIseconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 2),
    _Mp7001OutboundANSIseconds_Type()
)
mp7001OutboundANSIseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIseconds.setStatus("mandatory")


class _Mp7001OutboundANSICRCerrorEvents_Type(Integer32):
    """Custom type mp7001OutboundANSICRCerrorEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("errors1", 2),
          ("errors101to320", 32),
          ("errors11to100", 16),
          ("errors2to5", 4),
          ("errors321orMore", 64),
          ("errors6to10", 8),
          ("noErrors", 1))
    )


_Mp7001OutboundANSICRCerrorEvents_Type.__name__ = "Integer32"
_Mp7001OutboundANSICRCerrorEvents_Object = MibTableColumn
mp7001OutboundANSICRCerrorEvents = _Mp7001OutboundANSICRCerrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 3),
    _Mp7001OutboundANSICRCerrorEvents_Type()
)
mp7001OutboundANSICRCerrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSICRCerrorEvents.setStatus("mandatory")


class _Mp7001OutboundANSIsevereErrors_Type(Integer32):
    """Custom type mp7001OutboundANSIsevereErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001OutboundANSIsevereErrors_Type.__name__ = "Integer32"
_Mp7001OutboundANSIsevereErrors_Object = MibTableColumn
mp7001OutboundANSIsevereErrors = _Mp7001OutboundANSIsevereErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 4),
    _Mp7001OutboundANSIsevereErrors_Type()
)
mp7001OutboundANSIsevereErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIsevereErrors.setStatus("mandatory")


class _Mp7001OutboundANSIframeErrors_Type(Integer32):
    """Custom type mp7001OutboundANSIframeErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001OutboundANSIframeErrors_Type.__name__ = "Integer32"
_Mp7001OutboundANSIframeErrors_Object = MibTableColumn
mp7001OutboundANSIframeErrors = _Mp7001OutboundANSIframeErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 5),
    _Mp7001OutboundANSIframeErrors_Type()
)
mp7001OutboundANSIframeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIframeErrors.setStatus("mandatory")


class _Mp7001OutboundANSIcodeViolations_Type(Integer32):
    """Custom type mp7001OutboundANSIcodeViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001OutboundANSIcodeViolations_Type.__name__ = "Integer32"
_Mp7001OutboundANSIcodeViolations_Object = MibTableColumn
mp7001OutboundANSIcodeViolations = _Mp7001OutboundANSIcodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 6),
    _Mp7001OutboundANSIcodeViolations_Type()
)
mp7001OutboundANSIcodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIcodeViolations.setStatus("mandatory")


class _Mp7001OutboundANSIcontrolledSlips_Type(Integer32):
    """Custom type mp7001OutboundANSIcontrolledSlips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001OutboundANSIcontrolledSlips_Type.__name__ = "Integer32"
_Mp7001OutboundANSIcontrolledSlips_Object = MibTableColumn
mp7001OutboundANSIcontrolledSlips = _Mp7001OutboundANSIcontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 7),
    _Mp7001OutboundANSIcontrolledSlips_Type()
)
mp7001OutboundANSIcontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIcontrolledSlips.setStatus("mandatory")


class _Mp7001OutboundANSIactivePayloadLoops_Type(Integer32):
    """Custom type mp7001OutboundANSIactivePayloadLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventsDetected", 2),
          ("noEventsDetected", 1))
    )


_Mp7001OutboundANSIactivePayloadLoops_Type.__name__ = "Integer32"
_Mp7001OutboundANSIactivePayloadLoops_Object = MibTableColumn
mp7001OutboundANSIactivePayloadLoops = _Mp7001OutboundANSIactivePayloadLoops_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 2, 1, 8),
    _Mp7001OutboundANSIactivePayloadLoops_Type()
)
mp7001OutboundANSIactivePayloadLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001OutboundANSIactivePayloadLoops.setStatus("mandatory")
_Mp7001CurrentTable_Object = MibTable
mp7001CurrentTable = _Mp7001CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 3)
)
if mibBuilder.loadTexts:
    mp7001CurrentTable.setStatus("mandatory")
_Mp7001CurrentEntry_Object = MibTableRow
mp7001CurrentEntry = _Mp7001CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 3, 1)
)
mp7001CurrentEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001CurrentIndex"),
)
if mibBuilder.loadTexts:
    mp7001CurrentEntry.setStatus("mandatory")
_Mp7001CurrentIndex_Type = SCinstance
_Mp7001CurrentIndex_Object = MibTableColumn
mp7001CurrentIndex = _Mp7001CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 3, 1, 1),
    _Mp7001CurrentIndex_Type()
)
mp7001CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001CurrentIndex.setStatus("mandatory")


class _Mp7001CurrentStat_Type(OctetString):
    """Custom type mp7001CurrentStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_Mp7001CurrentStat_Type.__name__ = "OctetString"
_Mp7001CurrentStat_Object = MibTableColumn
mp7001CurrentStat = _Mp7001CurrentStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 3, 1, 2),
    _Mp7001CurrentStat_Type()
)
mp7001CurrentStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001CurrentStat.setStatus("mandatory")
_Mp7001IntervalTable_Object = MibTable
mp7001IntervalTable = _Mp7001IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 4)
)
if mibBuilder.loadTexts:
    mp7001IntervalTable.setStatus("mandatory")
_Mp7001IntervalEntry_Object = MibTableRow
mp7001IntervalEntry = _Mp7001IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 4, 1)
)
mp7001IntervalEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001IntervalIndex"),
    (0, "GDCMP7001-MIB", "mp7001IntervalNumber"),
)
if mibBuilder.loadTexts:
    mp7001IntervalEntry.setStatus("mandatory")
_Mp7001IntervalIndex_Type = SCinstance
_Mp7001IntervalIndex_Object = MibTableColumn
mp7001IntervalIndex = _Mp7001IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 4, 1, 1),
    _Mp7001IntervalIndex_Type()
)
mp7001IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001IntervalIndex.setStatus("mandatory")


class _Mp7001IntervalNumber_Type(Integer32):
    """Custom type mp7001IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Mp7001IntervalNumber_Type.__name__ = "Integer32"
_Mp7001IntervalNumber_Object = MibTableColumn
mp7001IntervalNumber = _Mp7001IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 4, 1, 2),
    _Mp7001IntervalNumber_Type()
)
mp7001IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001IntervalNumber.setStatus("mandatory")


class _Mp7001IntervalStat_Type(OctetString):
    """Custom type mp7001IntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7001IntervalStat_Type.__name__ = "OctetString"
_Mp7001IntervalStat_Object = MibTableColumn
mp7001IntervalStat = _Mp7001IntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 4, 1, 3),
    _Mp7001IntervalStat_Type()
)
mp7001IntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001IntervalStat.setStatus("mandatory")
_Mp7001TotalTable_Object = MibTable
mp7001TotalTable = _Mp7001TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 5)
)
if mibBuilder.loadTexts:
    mp7001TotalTable.setStatus("mandatory")
_Mp7001TotalEntry_Object = MibTableRow
mp7001TotalEntry = _Mp7001TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 5, 1)
)
mp7001TotalEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001TotalIndex"),
)
if mibBuilder.loadTexts:
    mp7001TotalEntry.setStatus("mandatory")
_Mp7001TotalIndex_Type = SCinstance
_Mp7001TotalIndex_Object = MibTableColumn
mp7001TotalIndex = _Mp7001TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 5, 1, 1),
    _Mp7001TotalIndex_Type()
)
mp7001TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001TotalIndex.setStatus("mandatory")


class _Mp7001TotalStat_Type(OctetString):
    """Custom type mp7001TotalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_Mp7001TotalStat_Type.__name__ = "OctetString"
_Mp7001TotalStat_Object = MibTableColumn
mp7001TotalStat = _Mp7001TotalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 5, 5, 1, 2),
    _Mp7001TotalStat_Type()
)
mp7001TotalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001TotalStat.setStatus("mandatory")
_Mp7001AlarmConfig_ObjectIdentity = ObjectIdentity
mp7001AlarmConfig = _Mp7001AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6)
)
_Mp7001NearEndAlarmConfigTable_Object = MibTable
mp7001NearEndAlarmConfigTable = _Mp7001NearEndAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1)
)
if mibBuilder.loadTexts:
    mp7001NearEndAlarmConfigTable.setStatus("mandatory")
_Mp7001NearEndAlarmConfigEntry_Object = MibTableRow
mp7001NearEndAlarmConfigEntry = _Mp7001NearEndAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1, 1)
)
mp7001NearEndAlarmConfigEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001NearEndAlarmConfigIndex"),
    (0, "GDCMP7001-MIB", "mp7001NearEndAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    mp7001NearEndAlarmConfigEntry.setStatus("mandatory")
_Mp7001NearEndAlarmConfigIndex_Type = SCinstance
_Mp7001NearEndAlarmConfigIndex_Object = MibTableColumn
mp7001NearEndAlarmConfigIndex = _Mp7001NearEndAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1, 1, 1),
    _Mp7001NearEndAlarmConfigIndex_Type()
)
mp7001NearEndAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001NearEndAlarmConfigIndex.setStatus("mandatory")
_Mp7001NearEndAlarmConfigIdentifier_Type = ObjectIdentifier
_Mp7001NearEndAlarmConfigIdentifier_Object = MibTableColumn
mp7001NearEndAlarmConfigIdentifier = _Mp7001NearEndAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1, 1, 2),
    _Mp7001NearEndAlarmConfigIdentifier_Type()
)
mp7001NearEndAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001NearEndAlarmConfigIdentifier.setStatus("mandatory")


class _Mp7001NearEndAlarmCountWindow_Type(Integer32):
    """Custom type mp7001NearEndAlarmCountWindow based on Integer32"""
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


_Mp7001NearEndAlarmCountWindow_Type.__name__ = "Integer32"
_Mp7001NearEndAlarmCountWindow_Object = MibTableColumn
mp7001NearEndAlarmCountWindow = _Mp7001NearEndAlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1, 1, 3),
    _Mp7001NearEndAlarmCountWindow_Type()
)
mp7001NearEndAlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001NearEndAlarmCountWindow.setStatus("mandatory")


class _Mp7001NearEndAlarmCountThreshold_Type(Integer32):
    """Custom type mp7001NearEndAlarmCountThreshold based on Integer32"""
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
        *(("thresGT1", 1),
          ("thresGT10", 3),
          ("thresGT100", 4),
          ("thresGT1000", 5),
          ("thresGT10000", 6),
          ("thresGT3", 2))
    )


_Mp7001NearEndAlarmCountThreshold_Type.__name__ = "Integer32"
_Mp7001NearEndAlarmCountThreshold_Object = MibTableColumn
mp7001NearEndAlarmCountThreshold = _Mp7001NearEndAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 1, 1, 4),
    _Mp7001NearEndAlarmCountThreshold_Type()
)
mp7001NearEndAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001NearEndAlarmCountThreshold.setStatus("mandatory")
_Mp7001LocalAlarmConfigTable_Object = MibTable
mp7001LocalAlarmConfigTable = _Mp7001LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2)
)
if mibBuilder.loadTexts:
    mp7001LocalAlarmConfigTable.setStatus("mandatory")
_Mp7001LocalAlarmConfigEntry_Object = MibTableRow
mp7001LocalAlarmConfigEntry = _Mp7001LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1)
)
mp7001LocalAlarmConfigEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    mp7001LocalAlarmConfigEntry.setStatus("mandatory")
_Mp7001LocalAlarmConfigIndex_Type = SCinstance
_Mp7001LocalAlarmConfigIndex_Object = MibTableColumn
mp7001LocalAlarmConfigIndex = _Mp7001LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 1),
    _Mp7001LocalAlarmConfigIndex_Type()
)
mp7001LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001LocalAlarmConfigIndex.setStatus("mandatory")


class _Mp7001LOSLocal_Type(Integer32):
    """Custom type mp7001LOSLocal based on Integer32"""
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


_Mp7001LOSLocal_Type.__name__ = "Integer32"
_Mp7001LOSLocal_Object = MibTableColumn
mp7001LOSLocal = _Mp7001LOSLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 2),
    _Mp7001LOSLocal_Type()
)
mp7001LOSLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001LOSLocal.setStatus("mandatory")


class _Mp7001LOFLocal_Type(Integer32):
    """Custom type mp7001LOFLocal based on Integer32"""
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


_Mp7001LOFLocal_Type.__name__ = "Integer32"
_Mp7001LOFLocal_Object = MibTableColumn
mp7001LOFLocal = _Mp7001LOFLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 3),
    _Mp7001LOFLocal_Type()
)
mp7001LOFLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001LOFLocal.setStatus("mandatory")


class _Mp7001AISLocal_Type(Integer32):
    """Custom type mp7001AISLocal based on Integer32"""
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


_Mp7001AISLocal_Type.__name__ = "Integer32"
_Mp7001AISLocal_Object = MibTableColumn
mp7001AISLocal = _Mp7001AISLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 4),
    _Mp7001AISLocal_Type()
)
mp7001AISLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001AISLocal.setStatus("mandatory")


class _Mp7001RxYELLOWLocal_Type(Integer32):
    """Custom type mp7001RxYELLOWLocal based on Integer32"""
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


_Mp7001RxYELLOWLocal_Type.__name__ = "Integer32"
_Mp7001RxYELLOWLocal_Object = MibTableColumn
mp7001RxYELLOWLocal = _Mp7001RxYELLOWLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 5),
    _Mp7001RxYELLOWLocal_Type()
)
mp7001RxYELLOWLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001RxYELLOWLocal.setStatus("mandatory")


class _Mp7001BPVLocal_Type(Integer32):
    """Custom type mp7001BPVLocal based on Integer32"""
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


_Mp7001BPVLocal_Type.__name__ = "Integer32"
_Mp7001BPVLocal_Object = MibTableColumn
mp7001BPVLocal = _Mp7001BPVLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 6),
    _Mp7001BPVLocal_Type()
)
mp7001BPVLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001BPVLocal.setStatus("mandatory")


class _Mp7001CRCLocal_Type(Integer32):
    """Custom type mp7001CRCLocal based on Integer32"""
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


_Mp7001CRCLocal_Type.__name__ = "Integer32"
_Mp7001CRCLocal_Object = MibTableColumn
mp7001CRCLocal = _Mp7001CRCLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 7),
    _Mp7001CRCLocal_Type()
)
mp7001CRCLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001CRCLocal.setStatus("mandatory")


class _Mp7001UnSigStateLocal_Type(Integer32):
    """Custom type mp7001UnSigStateLocal based on Integer32"""
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


_Mp7001UnSigStateLocal_Type.__name__ = "Integer32"
_Mp7001UnSigStateLocal_Object = MibTableColumn
mp7001UnSigStateLocal = _Mp7001UnSigStateLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 8),
    _Mp7001UnSigStateLocal_Type()
)
mp7001UnSigStateLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001UnSigStateLocal.setStatus("mandatory")


class _Mp7001TiminglossLocal_Type(Integer32):
    """Custom type mp7001TiminglossLocal based on Integer32"""
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


_Mp7001TiminglossLocal_Type.__name__ = "Integer32"
_Mp7001TiminglossLocal_Object = MibTableColumn
mp7001TiminglossLocal = _Mp7001TiminglossLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 9),
    _Mp7001TiminglossLocal_Type()
)
mp7001TiminglossLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001TiminglossLocal.setStatus("mandatory")


class _Mp7001ESLocal_Type(Integer32):
    """Custom type mp7001ESLocal based on Integer32"""
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


_Mp7001ESLocal_Type.__name__ = "Integer32"
_Mp7001ESLocal_Object = MibTableColumn
mp7001ESLocal = _Mp7001ESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 10),
    _Mp7001ESLocal_Type()
)
mp7001ESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001ESLocal.setStatus("mandatory")


class _Mp7001BESLocal_Type(Integer32):
    """Custom type mp7001BESLocal based on Integer32"""
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


_Mp7001BESLocal_Type.__name__ = "Integer32"
_Mp7001BESLocal_Object = MibTableColumn
mp7001BESLocal = _Mp7001BESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 11),
    _Mp7001BESLocal_Type()
)
mp7001BESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001BESLocal.setStatus("mandatory")


class _Mp7001SESLocal_Type(Integer32):
    """Custom type mp7001SESLocal based on Integer32"""
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


_Mp7001SESLocal_Type.__name__ = "Integer32"
_Mp7001SESLocal_Object = MibTableColumn
mp7001SESLocal = _Mp7001SESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 12),
    _Mp7001SESLocal_Type()
)
mp7001SESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001SESLocal.setStatus("mandatory")


class _Mp7001UASLocal_Type(Integer32):
    """Custom type mp7001UASLocal based on Integer32"""
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


_Mp7001UASLocal_Type.__name__ = "Integer32"
_Mp7001UASLocal_Object = MibTableColumn
mp7001UASLocal = _Mp7001UASLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 6, 2, 1, 13),
    _Mp7001UASLocal_Type()
)
mp7001UASLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001UASLocal.setStatus("mandatory")
_Mp7001SysConfig_ObjectIdentity = ObjectIdentity
mp7001SysConfig = _Mp7001SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7)
)
_Mp7001SysTimingTable_Object = MibTable
mp7001SysTimingTable = _Mp7001SysTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 1)
)
if mibBuilder.loadTexts:
    mp7001SysTimingTable.setStatus("mandatory")
_Mp7001SysTimingEntry_Object = MibTableRow
mp7001SysTimingEntry = _Mp7001SysTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 1, 1)
)
mp7001SysTimingEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001SysTimingIndex"),
)
if mibBuilder.loadTexts:
    mp7001SysTimingEntry.setStatus("mandatory")
_Mp7001SysTimingIndex_Type = SCinstance
_Mp7001SysTimingIndex_Object = MibTableColumn
mp7001SysTimingIndex = _Mp7001SysTimingIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 1, 1, 1),
    _Mp7001SysTimingIndex_Type()
)
mp7001SysTimingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001SysTimingIndex.setStatus("mandatory")


class _Mp7001SysTimingGen_Type(Integer32):
    """Custom type mp7001SysTimingGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_Mp7001SysTimingGen_Type.__name__ = "Integer32"
_Mp7001SysTimingGen_Object = MibTableColumn
mp7001SysTimingGen = _Mp7001SysTimingGen_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 1, 1, 2),
    _Mp7001SysTimingGen_Type()
)
mp7001SysTimingGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001SysTimingGen.setStatus("mandatory")
_Mp7001HighwayAssignTable_Object = MibTable
mp7001HighwayAssignTable = _Mp7001HighwayAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2)
)
if mibBuilder.loadTexts:
    mp7001HighwayAssignTable.setStatus("mandatory")
_Mp7001HighwayAssignEntry_Object = MibTableRow
mp7001HighwayAssignEntry = _Mp7001HighwayAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1)
)
mp7001HighwayAssignEntry.setIndexNames(
    (0, "GDCMP7001-MIB", "mp7001HighwayAssignIndex"),
)
if mibBuilder.loadTexts:
    mp7001HighwayAssignEntry.setStatus("mandatory")
_Mp7001HighwayAssignIndex_Type = SCinstance
_Mp7001HighwayAssignIndex_Object = MibTableColumn
mp7001HighwayAssignIndex = _Mp7001HighwayAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1, 1),
    _Mp7001HighwayAssignIndex_Type()
)
mp7001HighwayAssignIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7001HighwayAssignIndex.setStatus("mandatory")


class _Mp7001StartTimeSlot_Type(Integer32):
    """Custom type mp7001StartTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Mp7001StartTimeSlot_Type.__name__ = "Integer32"
_Mp7001StartTimeSlot_Object = MibTableColumn
mp7001StartTimeSlot = _Mp7001StartTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1, 2),
    _Mp7001StartTimeSlot_Type()
)
mp7001StartTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001StartTimeSlot.setStatus("mandatory")


class _Mp7001NumberOfTimeSlots_Type(Integer32):
    """Custom type mp7001NumberOfTimeSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Mp7001NumberOfTimeSlots_Type.__name__ = "Integer32"
_Mp7001NumberOfTimeSlots_Object = MibTableColumn
mp7001NumberOfTimeSlots = _Mp7001NumberOfTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1, 3),
    _Mp7001NumberOfTimeSlots_Type()
)
mp7001NumberOfTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001NumberOfTimeSlots.setStatus("mandatory")


class _Mp7001BundleDestination_Type(Integer32):
    """Custom type mp7001BundleDestination based on Integer32"""
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
        *(("highway1", 2),
          ("highway2", 3),
          ("highway3", 4),
          ("highway4", 5),
          ("notAssigned", 1))
    )


_Mp7001BundleDestination_Type.__name__ = "Integer32"
_Mp7001BundleDestination_Object = MibTableColumn
mp7001BundleDestination = _Mp7001BundleDestination_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1, 4),
    _Mp7001BundleDestination_Type()
)
mp7001BundleDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001BundleDestination.setStatus("mandatory")


class _Mp7001ExecuteAssign_Type(Integer32):
    """Custom type mp7001ExecuteAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("normal", 1))
    )


_Mp7001ExecuteAssign_Type.__name__ = "Integer32"
_Mp7001ExecuteAssign_Object = MibTableColumn
mp7001ExecuteAssign = _Mp7001ExecuteAssign_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 7, 2, 1, 5),
    _Mp7001ExecuteAssign_Type()
)
mp7001ExecuteAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7001ExecuteAssign.setStatus("mandatory")
_Mp7001Alarms_ObjectIdentity = ObjectIdentity
mp7001Alarms = _Mp7001Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8)
)
_Mp7001NoResponseAlm_ObjectIdentity = ObjectIdentity
mp7001NoResponseAlm = _Mp7001NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 1)
)
_Mp7001DiagRxErrAlm_ObjectIdentity = ObjectIdentity
mp7001DiagRxErrAlm = _Mp7001DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 2)
)
_Mp7001PowerUpAlm_ObjectIdentity = ObjectIdentity
mp7001PowerUpAlm = _Mp7001PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 3)
)
_Mp7001NvRamCorrupt_ObjectIdentity = ObjectIdentity
mp7001NvRamCorrupt = _Mp7001NvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 4)
)
_Mp7001UnitFailure_ObjectIdentity = ObjectIdentity
mp7001UnitFailure = _Mp7001UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 5)
)
_Mp7001LossOfSignal_ObjectIdentity = ObjectIdentity
mp7001LossOfSignal = _Mp7001LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 6)
)
_Mp7001LossOfFrame_ObjectIdentity = ObjectIdentity
mp7001LossOfFrame = _Mp7001LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 7)
)
_Mp7001Ais_ObjectIdentity = ObjectIdentity
mp7001Ais = _Mp7001Ais_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 8)
)
_Mp7001YELLOW_ObjectIdentity = ObjectIdentity
mp7001YELLOW = _Mp7001YELLOW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 9)
)
_Mp7001BipolarViolation_ObjectIdentity = ObjectIdentity
mp7001BipolarViolation = _Mp7001BipolarViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 10)
)
_Mp7001CRC_ObjectIdentity = ObjectIdentity
mp7001CRC = _Mp7001CRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 11)
)
_Mp7001UnSigState_ObjectIdentity = ObjectIdentity
mp7001UnSigState = _Mp7001UnSigState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 12)
)
_Mp7001TimingLoss_ObjectIdentity = ObjectIdentity
mp7001TimingLoss = _Mp7001TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 13)
)
_Mp7001ES_ObjectIdentity = ObjectIdentity
mp7001ES = _Mp7001ES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 14)
)
_Mp7001BES_ObjectIdentity = ObjectIdentity
mp7001BES = _Mp7001BES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 15)
)
_Mp7001SES_ObjectIdentity = ObjectIdentity
mp7001SES = _Mp7001SES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 16)
)
_Mp7001UAS_ObjectIdentity = ObjectIdentity
mp7001UAS = _Mp7001UAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 17)
)
_Mp7001ControlSlips_ObjectIdentity = ObjectIdentity
mp7001ControlSlips = _Mp7001ControlSlips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 18)
)
_Mp7001UnsolicitedTest_ObjectIdentity = ObjectIdentity
mp7001UnsolicitedTest = _Mp7001UnsolicitedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 10, 8, 19)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCMP7001-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "mp7001System": mp7001System,
       "mp7001Version": mp7001Version,
       "mp7001MIBversion": mp7001MIBversion,
       "mp7001VersionTable": mp7001VersionTable,
       "mp7001VersionEntry": mp7001VersionEntry,
       "mp7001VersionIndex": mp7001VersionIndex,
       "mp7001FirmwareRev": mp7001FirmwareRev,
       "mp7001CardType": mp7001CardType,
       "mp7001BootRev": mp7001BootRev,
       "mp7001Maintenance": mp7001Maintenance,
       "mp7001MaintenanceTable": mp7001MaintenanceTable,
       "mp7001MaintenanceEntry": mp7001MaintenanceEntry,
       "mp7001MaintenanceLineIndex": mp7001MaintenanceLineIndex,
       "mp7001SoftReset": mp7001SoftReset,
       "mp7001SysUpTime": mp7001SysUpTime,
       "mp7001DefaultInit": mp7001DefaultInit,
       "mp7001ResetStats": mp7001ResetStats,
       "mp7001LedStatus": mp7001LedStatus,
       "mp7001T1CircuitName": mp7001T1CircuitName,
       "mp7001SetRealTime": mp7001SetRealTime,
       "mp7001AlarmStatus": mp7001AlarmStatus,
       "mp7001SystemTimingGenStatus": mp7001SystemTimingGenStatus,
       "mp7001StatLastInitialized": mp7001StatLastInitialized,
       "mp7001ValidIntervals": mp7001ValidIntervals,
       "mp7001Configuration": mp7001Configuration,
       "mp7001ConfigTable": mp7001ConfigTable,
       "mp7001ConfigEntry": mp7001ConfigEntry,
       "mp7001ConfigIndex": mp7001ConfigIndex,
       "mp7001NetworkInterfaceType": mp7001NetworkInterfaceType,
       "mp7001TransmitClockSource": mp7001TransmitClockSource,
       "mp7001FallbackClockSource": mp7001FallbackClockSource,
       "mp7001PreEqualization": mp7001PreEqualization,
       "mp7001Framing": mp7001Framing,
       "mp7001LineCoding": mp7001LineCoding,
       "mp7001LineBuildout": mp7001LineBuildout,
       "mp7001FDLMode": mp7001FDLMode,
       "mp7001FramingMode": mp7001FramingMode,
       "mp7001Loopback": mp7001Loopback,
       "mp7001AISLoopdown": mp7001AISLoopdown,
       "mp7001SignalMode": mp7001SignalMode,
       "mp7001LineBuildoutCtrl": mp7001LineBuildoutCtrl,
       "mp7001DCCConfigurationTable": mp7001DCCConfigurationTable,
       "mp7001DCCConfigurationEntry": mp7001DCCConfigurationEntry,
       "mp7001DCCConfigurationIndex": mp7001DCCConfigurationIndex,
       "mp7001TimeSlot": mp7001TimeSlot,
       "mp7001Bandwidth": mp7001Bandwidth,
       "mp7001Diagnostics": mp7001Diagnostics,
       "mp7001DiagTable": mp7001DiagTable,
       "mp7001DiagEntry": mp7001DiagEntry,
       "mp7001DiagIndex": mp7001DiagIndex,
       "mp7001TestPattern": mp7001TestPattern,
       "mp7001DiagConfig": mp7001DiagConfig,
       "mp7001TestLimit": mp7001TestLimit,
       "mp7001TestExecutionStatus": mp7001TestExecutionStatus,
       "mp7001TestExceptions": mp7001TestExceptions,
       "mp7001TestResults": mp7001TestResults,
       "mp7001ResetTestResults": mp7001ResetTestResults,
       "mp7001DS0Diag": mp7001DS0Diag,
       "mp7001Performance": mp7001Performance,
       "mp7001InboundANSIperfTable": mp7001InboundANSIperfTable,
       "mp7001InboundANSIperfEntry": mp7001InboundANSIperfEntry,
       "mp7001InboundANSIperfIndex": mp7001InboundANSIperfIndex,
       "mp7001InboundANSIseconds": mp7001InboundANSIseconds,
       "mp7001InboundANSICRCerrorEvents": mp7001InboundANSICRCerrorEvents,
       "mp7001InboundANSIsevereErrors": mp7001InboundANSIsevereErrors,
       "mp7001InboundANSIframeErrors": mp7001InboundANSIframeErrors,
       "mp7001InboundANSIcodeViolations": mp7001InboundANSIcodeViolations,
       "mp7001InboundANSIcontrolledSlips": mp7001InboundANSIcontrolledSlips,
       "mp7001InboundANSIactivePayloadLoops": mp7001InboundANSIactivePayloadLoops,
       "mp7001OutboundANSIperfTable": mp7001OutboundANSIperfTable,
       "mp7001OutboundANSIperfEntry": mp7001OutboundANSIperfEntry,
       "mp7001OutboundANSIperfIndex": mp7001OutboundANSIperfIndex,
       "mp7001OutboundANSIseconds": mp7001OutboundANSIseconds,
       "mp7001OutboundANSICRCerrorEvents": mp7001OutboundANSICRCerrorEvents,
       "mp7001OutboundANSIsevereErrors": mp7001OutboundANSIsevereErrors,
       "mp7001OutboundANSIframeErrors": mp7001OutboundANSIframeErrors,
       "mp7001OutboundANSIcodeViolations": mp7001OutboundANSIcodeViolations,
       "mp7001OutboundANSIcontrolledSlips": mp7001OutboundANSIcontrolledSlips,
       "mp7001OutboundANSIactivePayloadLoops": mp7001OutboundANSIactivePayloadLoops,
       "mp7001CurrentTable": mp7001CurrentTable,
       "mp7001CurrentEntry": mp7001CurrentEntry,
       "mp7001CurrentIndex": mp7001CurrentIndex,
       "mp7001CurrentStat": mp7001CurrentStat,
       "mp7001IntervalTable": mp7001IntervalTable,
       "mp7001IntervalEntry": mp7001IntervalEntry,
       "mp7001IntervalIndex": mp7001IntervalIndex,
       "mp7001IntervalNumber": mp7001IntervalNumber,
       "mp7001IntervalStat": mp7001IntervalStat,
       "mp7001TotalTable": mp7001TotalTable,
       "mp7001TotalEntry": mp7001TotalEntry,
       "mp7001TotalIndex": mp7001TotalIndex,
       "mp7001TotalStat": mp7001TotalStat,
       "mp7001AlarmConfig": mp7001AlarmConfig,
       "mp7001NearEndAlarmConfigTable": mp7001NearEndAlarmConfigTable,
       "mp7001NearEndAlarmConfigEntry": mp7001NearEndAlarmConfigEntry,
       "mp7001NearEndAlarmConfigIndex": mp7001NearEndAlarmConfigIndex,
       "mp7001NearEndAlarmConfigIdentifier": mp7001NearEndAlarmConfigIdentifier,
       "mp7001NearEndAlarmCountWindow": mp7001NearEndAlarmCountWindow,
       "mp7001NearEndAlarmCountThreshold": mp7001NearEndAlarmCountThreshold,
       "mp7001LocalAlarmConfigTable": mp7001LocalAlarmConfigTable,
       "mp7001LocalAlarmConfigEntry": mp7001LocalAlarmConfigEntry,
       "mp7001LocalAlarmConfigIndex": mp7001LocalAlarmConfigIndex,
       "mp7001LOSLocal": mp7001LOSLocal,
       "mp7001LOFLocal": mp7001LOFLocal,
       "mp7001AISLocal": mp7001AISLocal,
       "mp7001RxYELLOWLocal": mp7001RxYELLOWLocal,
       "mp7001BPVLocal": mp7001BPVLocal,
       "mp7001CRCLocal": mp7001CRCLocal,
       "mp7001UnSigStateLocal": mp7001UnSigStateLocal,
       "mp7001TiminglossLocal": mp7001TiminglossLocal,
       "mp7001ESLocal": mp7001ESLocal,
       "mp7001BESLocal": mp7001BESLocal,
       "mp7001SESLocal": mp7001SESLocal,
       "mp7001UASLocal": mp7001UASLocal,
       "mp7001SysConfig": mp7001SysConfig,
       "mp7001SysTimingTable": mp7001SysTimingTable,
       "mp7001SysTimingEntry": mp7001SysTimingEntry,
       "mp7001SysTimingIndex": mp7001SysTimingIndex,
       "mp7001SysTimingGen": mp7001SysTimingGen,
       "mp7001HighwayAssignTable": mp7001HighwayAssignTable,
       "mp7001HighwayAssignEntry": mp7001HighwayAssignEntry,
       "mp7001HighwayAssignIndex": mp7001HighwayAssignIndex,
       "mp7001StartTimeSlot": mp7001StartTimeSlot,
       "mp7001NumberOfTimeSlots": mp7001NumberOfTimeSlots,
       "mp7001BundleDestination": mp7001BundleDestination,
       "mp7001ExecuteAssign": mp7001ExecuteAssign,
       "mp7001Alarms": mp7001Alarms,
       "mp7001NoResponseAlm": mp7001NoResponseAlm,
       "mp7001DiagRxErrAlm": mp7001DiagRxErrAlm,
       "mp7001PowerUpAlm": mp7001PowerUpAlm,
       "mp7001NvRamCorrupt": mp7001NvRamCorrupt,
       "mp7001UnitFailure": mp7001UnitFailure,
       "mp7001LossOfSignal": mp7001LossOfSignal,
       "mp7001LossOfFrame": mp7001LossOfFrame,
       "mp7001Ais": mp7001Ais,
       "mp7001YELLOW": mp7001YELLOW,
       "mp7001BipolarViolation": mp7001BipolarViolation,
       "mp7001CRC": mp7001CRC,
       "mp7001UnSigState": mp7001UnSigState,
       "mp7001TimingLoss": mp7001TimingLoss,
       "mp7001ES": mp7001ES,
       "mp7001BES": mp7001BES,
       "mp7001SES": mp7001SES,
       "mp7001UAS": mp7001UAS,
       "mp7001ControlSlips": mp7001ControlSlips,
       "mp7001UnsolicitedTest": mp7001UnsolicitedTest}
)
