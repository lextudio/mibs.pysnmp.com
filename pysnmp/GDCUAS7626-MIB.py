# SNMP MIB module (GDCUAS7626-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCUAS7626-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:24 2024
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
_Bql2_ObjectIdentity = ObjectIdentity
bql2 = _Bql2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12)
)
_Uas7626_ObjectIdentity = ObjectIdentity
uas7626 = _Uas7626_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12)
)
_Uas7626Version_ObjectIdentity = ObjectIdentity
uas7626Version = _Uas7626Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1)
)


class _Uas7626MIBversion_Type(DisplayString):
    """Custom type uas7626MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Uas7626MIBversion_Type.__name__ = "DisplayString"
_Uas7626MIBversion_Object = MibScalar
uas7626MIBversion = _Uas7626MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 1),
    _Uas7626MIBversion_Type()
)
uas7626MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626MIBversion.setStatus("mandatory")
_Uas7626VersionTable_Object = MibTable
uas7626VersionTable = _Uas7626VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2)
)
if mibBuilder.loadTexts:
    uas7626VersionTable.setStatus("mandatory")
_Uas7626VersionEntry_Object = MibTableRow
uas7626VersionEntry = _Uas7626VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1)
)
uas7626VersionEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626VersionIndex"),
)
if mibBuilder.loadTexts:
    uas7626VersionEntry.setStatus("mandatory")
_Uas7626VersionIndex_Type = SCinstance
_Uas7626VersionIndex_Object = MibTableColumn
uas7626VersionIndex = _Uas7626VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 1),
    _Uas7626VersionIndex_Type()
)
uas7626VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626VersionIndex.setStatus("mandatory")


class _Uas7626ActiveFirmwareRev_Type(DisplayString):
    """Custom type uas7626ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Uas7626ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Uas7626ActiveFirmwareRev_Object = MibTableColumn
uas7626ActiveFirmwareRev = _Uas7626ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 2),
    _Uas7626ActiveFirmwareRev_Type()
)
uas7626ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626ActiveFirmwareRev.setStatus("mandatory")


class _Uas7626StoredFirmwareRev_Type(DisplayString):
    """Custom type uas7626StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Uas7626StoredFirmwareRev_Type.__name__ = "DisplayString"
_Uas7626StoredFirmwareRev_Object = MibTableColumn
uas7626StoredFirmwareRev = _Uas7626StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 3),
    _Uas7626StoredFirmwareRev_Type()
)
uas7626StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626StoredFirmwareRev.setStatus("mandatory")


class _Uas7626StoredFirmwareStatus_Type(Integer32):
    """Custom type uas7626StoredFirmwareStatus based on Integer32"""
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
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statDownloadAborted", 7),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_Uas7626StoredFirmwareStatus_Type.__name__ = "Integer32"
_Uas7626StoredFirmwareStatus_Object = MibTableColumn
uas7626StoredFirmwareStatus = _Uas7626StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 4),
    _Uas7626StoredFirmwareStatus_Type()
)
uas7626StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626StoredFirmwareStatus.setStatus("mandatory")


class _Uas7626SwitchActiveFirmware_Type(Integer32):
    """Custom type uas7626SwitchActiveFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchActive", 2),
          ("switchNorm", 1))
    )


_Uas7626SwitchActiveFirmware_Type.__name__ = "Integer32"
_Uas7626SwitchActiveFirmware_Object = MibTableColumn
uas7626SwitchActiveFirmware = _Uas7626SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 5),
    _Uas7626SwitchActiveFirmware_Type()
)
uas7626SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626SwitchActiveFirmware.setStatus("mandatory")


class _Uas7626DownloadingMode_Type(Integer32):
    """Custom type uas7626DownloadingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableAll", 1),
          ("enableAndSwitch", 3),
          ("enableAndWait", 2))
    )


_Uas7626DownloadingMode_Type.__name__ = "Integer32"
_Uas7626DownloadingMode_Object = MibTableColumn
uas7626DownloadingMode = _Uas7626DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 6),
    _Uas7626DownloadingMode_Type()
)
uas7626DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626DownloadingMode.setStatus("mandatory")
_Uas7626Maintenance_ObjectIdentity = ObjectIdentity
uas7626Maintenance = _Uas7626Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2)
)
_Uas7626MaintenanceTable_Object = MibTable
uas7626MaintenanceTable = _Uas7626MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1)
)
if mibBuilder.loadTexts:
    uas7626MaintenanceTable.setStatus("mandatory")
_Uas7626MaintenanceEntry_Object = MibTableRow
uas7626MaintenanceEntry = _Uas7626MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1)
)
uas7626MaintenanceEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    uas7626MaintenanceEntry.setStatus("mandatory")
_Uas7626MaintenanceLineIndex_Type = SCinstance
_Uas7626MaintenanceLineIndex_Object = MibTableColumn
uas7626MaintenanceLineIndex = _Uas7626MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 1),
    _Uas7626MaintenanceLineIndex_Type()
)
uas7626MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626MaintenanceLineIndex.setStatus("mandatory")


class _Uas7626SoftReset_Type(Integer32):
    """Custom type uas7626SoftReset based on Integer32"""
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


_Uas7626SoftReset_Type.__name__ = "Integer32"
_Uas7626SoftReset_Object = MibTableColumn
uas7626SoftReset = _Uas7626SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 2),
    _Uas7626SoftReset_Type()
)
uas7626SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626SoftReset.setStatus("mandatory")


class _Uas7626DefaultInit_Type(Integer32):
    """Custom type uas7626DefaultInit based on Integer32"""
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


_Uas7626DefaultInit_Type.__name__ = "Integer32"
_Uas7626DefaultInit_Object = MibTableColumn
uas7626DefaultInit = _Uas7626DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 3),
    _Uas7626DefaultInit_Type()
)
uas7626DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626DefaultInit.setStatus("mandatory")


class _Uas7626ResetMajorAlarm_Type(Integer32):
    """Custom type uas7626ResetMajorAlarm based on Integer32"""
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


_Uas7626ResetMajorAlarm_Type.__name__ = "Integer32"
_Uas7626ResetMajorAlarm_Object = MibTableColumn
uas7626ResetMajorAlarm = _Uas7626ResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 4),
    _Uas7626ResetMajorAlarm_Type()
)
uas7626ResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626ResetMajorAlarm.setStatus("mandatory")


class _Uas7626ResetMinorAlarm_Type(Integer32):
    """Custom type uas7626ResetMinorAlarm based on Integer32"""
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


_Uas7626ResetMinorAlarm_Type.__name__ = "Integer32"
_Uas7626ResetMinorAlarm_Object = MibTableColumn
uas7626ResetMinorAlarm = _Uas7626ResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 5),
    _Uas7626ResetMinorAlarm_Type()
)
uas7626ResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626ResetMinorAlarm.setStatus("mandatory")


class _Uas7626ResetStatistics_Type(Integer32):
    """Custom type uas7626ResetStatistics based on Integer32"""
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


_Uas7626ResetStatistics_Type.__name__ = "Integer32"
_Uas7626ResetStatistics_Object = MibTableColumn
uas7626ResetStatistics = _Uas7626ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 6),
    _Uas7626ResetStatistics_Type()
)
uas7626ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626ResetStatistics.setStatus("mandatory")


class _Uas7626ValidIntervals_Type(Integer32):
    """Custom type uas7626ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7626ValidIntervals_Type.__name__ = "Integer32"
_Uas7626ValidIntervals_Object = MibTableColumn
uas7626ValidIntervals = _Uas7626ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 7),
    _Uas7626ValidIntervals_Type()
)
uas7626ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626ValidIntervals.setStatus("mandatory")


class _Uas7626SysUpTime_Type(Integer32):
    """Custom type uas7626SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7626SysUpTime_Type.__name__ = "Integer32"
_Uas7626SysUpTime_Object = MibTableColumn
uas7626SysUpTime = _Uas7626SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 8),
    _Uas7626SysUpTime_Type()
)
uas7626SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626SysUpTime.setStatus("mandatory")


class _Uas7626LedStatus_Type(OctetString):
    """Custom type uas7626LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Uas7626LedStatus_Type.__name__ = "OctetString"
_Uas7626LedStatus_Object = MibTableColumn
uas7626LedStatus = _Uas7626LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 9),
    _Uas7626LedStatus_Type()
)
uas7626LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626LedStatus.setStatus("mandatory")


class _Uas7626AlarmStatus_Type(OctetString):
    """Custom type uas7626AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_Uas7626AlarmStatus_Type.__name__ = "OctetString"
_Uas7626AlarmStatus_Object = MibTableColumn
uas7626AlarmStatus = _Uas7626AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 10),
    _Uas7626AlarmStatus_Type()
)
uas7626AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626AlarmStatus.setStatus("mandatory")
_Uas7626StatLastInitialized_Type = TimeTicks
_Uas7626StatLastInitialized_Object = MibTableColumn
uas7626StatLastInitialized = _Uas7626StatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 11),
    _Uas7626StatLastInitialized_Type()
)
uas7626StatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626StatLastInitialized.setStatus("mandatory")


class _Uas7626CircuitID_Type(DisplayString):
    """Custom type uas7626CircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Uas7626CircuitID_Type.__name__ = "DisplayString"
_Uas7626CircuitID_Object = MibTableColumn
uas7626CircuitID = _Uas7626CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 12),
    _Uas7626CircuitID_Type()
)
uas7626CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626CircuitID.setStatus("mandatory")
_Uas7626Configuration_ObjectIdentity = ObjectIdentity
uas7626Configuration = _Uas7626Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3)
)
_Uas7626ConfigTable_Object = MibTable
uas7626ConfigTable = _Uas7626ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1)
)
if mibBuilder.loadTexts:
    uas7626ConfigTable.setStatus("mandatory")
_Uas7626ConfigEntry_Object = MibTableRow
uas7626ConfigEntry = _Uas7626ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1)
)
uas7626ConfigEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626ConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7626ConfigEntry.setStatus("mandatory")
_Uas7626ConfigIndex_Type = SCinstance
_Uas7626ConfigIndex_Object = MibTableColumn
uas7626ConfigIndex = _Uas7626ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 1),
    _Uas7626ConfigIndex_Type()
)
uas7626ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626ConfigIndex.setStatus("mandatory")


class _Uas7626DataRate_Type(Integer32):
    """Custom type uas7626DataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 3),
          ("kbps128", 2),
          ("kbps64", 1))
    )


_Uas7626DataRate_Type.__name__ = "Integer32"
_Uas7626DataRate_Object = MibTableColumn
uas7626DataRate = _Uas7626DataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 2),
    _Uas7626DataRate_Type()
)
uas7626DataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626DataRate.setStatus("mandatory")


class _Uas7626Highway_Type(Integer32):
    """Custom type uas7626Highway based on Integer32"""
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
        *(("highway1", 2),
          ("highway2", 3),
          ("highway3", 4),
          ("highway4", 5),
          ("highway5", 6),
          ("highway6", 7),
          ("highway7", 8),
          ("highway8", 9),
          ("notAssigned", 1))
    )


_Uas7626Highway_Type.__name__ = "Integer32"
_Uas7626Highway_Object = MibTableColumn
uas7626Highway = _Uas7626Highway_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 3),
    _Uas7626Highway_Type()
)
uas7626Highway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626Highway.setStatus("mandatory")


class _Uas7626TimeSlot_Type(Integer32):
    """Custom type uas7626TimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Uas7626TimeSlot_Type.__name__ = "Integer32"
_Uas7626TimeSlot_Object = MibTableColumn
uas7626TimeSlot = _Uas7626TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 4),
    _Uas7626TimeSlot_Type()
)
uas7626TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626TimeSlot.setStatus("mandatory")
_Uas7626Diagnostics_ObjectIdentity = ObjectIdentity
uas7626Diagnostics = _Uas7626Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4)
)
_Uas7626DiagTable_Object = MibTable
uas7626DiagTable = _Uas7626DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1)
)
if mibBuilder.loadTexts:
    uas7626DiagTable.setStatus("mandatory")
_Uas7626DiagEntry_Object = MibTableRow
uas7626DiagEntry = _Uas7626DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1)
)
uas7626DiagEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626DiagIndex"),
)
if mibBuilder.loadTexts:
    uas7626DiagEntry.setStatus("mandatory")
_Uas7626DiagIndex_Type = SCinstance
_Uas7626DiagIndex_Object = MibTableColumn
uas7626DiagIndex = _Uas7626DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 1),
    _Uas7626DiagIndex_Type()
)
uas7626DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626DiagIndex.setStatus("mandatory")


class _Uas7626TestSelection_Type(Integer32):
    """Custom type uas7626TestSelection based on Integer32"""
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
        *(("digitalLoopback", 2),
          ("rdlSelfTest", 5),
          ("remoteDigitalLoopback", 4),
          ("selfTest", 3),
          ("stopTest", 1))
    )


_Uas7626TestSelection_Type.__name__ = "Integer32"
_Uas7626TestSelection_Object = MibTableColumn
uas7626TestSelection = _Uas7626TestSelection_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 2),
    _Uas7626TestSelection_Type()
)
uas7626TestSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626TestSelection.setStatus("mandatory")


class _Uas7626TestResults_Type(Integer32):
    """Custom type uas7626TestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_Uas7626TestResults_Type.__name__ = "Integer32"
_Uas7626TestResults_Object = MibTableColumn
uas7626TestResults = _Uas7626TestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 3),
    _Uas7626TestResults_Type()
)
uas7626TestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626TestResults.setStatus("mandatory")


class _Uas7626ResetTestResults_Type(Integer32):
    """Custom type uas7626ResetTestResults based on Integer32"""
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


_Uas7626ResetTestResults_Type.__name__ = "Integer32"
_Uas7626ResetTestResults_Object = MibTableColumn
uas7626ResetTestResults = _Uas7626ResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 4),
    _Uas7626ResetTestResults_Type()
)
uas7626ResetTestResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626ResetTestResults.setStatus("mandatory")
_Uas7626Performance_ObjectIdentity = ObjectIdentity
uas7626Performance = _Uas7626Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5)
)
_Uas7626CurrentTable_Object = MibTable
uas7626CurrentTable = _Uas7626CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3)
)
if mibBuilder.loadTexts:
    uas7626CurrentTable.setStatus("mandatory")
_Uas7626CurrentEntry_Object = MibTableRow
uas7626CurrentEntry = _Uas7626CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1)
)
uas7626CurrentEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626CurrentIndex"),
)
if mibBuilder.loadTexts:
    uas7626CurrentEntry.setStatus("mandatory")
_Uas7626CurrentIndex_Type = SCinstance
_Uas7626CurrentIndex_Object = MibTableColumn
uas7626CurrentIndex = _Uas7626CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1, 1),
    _Uas7626CurrentIndex_Type()
)
uas7626CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626CurrentIndex.setStatus("mandatory")


class _Uas7626CurrentStat_Type(OctetString):
    """Custom type uas7626CurrentStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Uas7626CurrentStat_Type.__name__ = "OctetString"
_Uas7626CurrentStat_Object = MibTableColumn
uas7626CurrentStat = _Uas7626CurrentStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1, 2),
    _Uas7626CurrentStat_Type()
)
uas7626CurrentStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626CurrentStat.setStatus("mandatory")
_Uas7626IntervalTable_Object = MibTable
uas7626IntervalTable = _Uas7626IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4)
)
if mibBuilder.loadTexts:
    uas7626IntervalTable.setStatus("mandatory")
_Uas7626IntervalEntry_Object = MibTableRow
uas7626IntervalEntry = _Uas7626IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1)
)
uas7626IntervalEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626IntervalIndex"),
    (0, "GDCUAS7626-MIB", "uas7626IntervalNumber"),
)
if mibBuilder.loadTexts:
    uas7626IntervalEntry.setStatus("mandatory")
_Uas7626IntervalIndex_Type = SCinstance
_Uas7626IntervalIndex_Object = MibTableColumn
uas7626IntervalIndex = _Uas7626IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 1),
    _Uas7626IntervalIndex_Type()
)
uas7626IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626IntervalIndex.setStatus("mandatory")


class _Uas7626IntervalNumber_Type(Integer32):
    """Custom type uas7626IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7626IntervalNumber_Type.__name__ = "Integer32"
_Uas7626IntervalNumber_Object = MibTableColumn
uas7626IntervalNumber = _Uas7626IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 2),
    _Uas7626IntervalNumber_Type()
)
uas7626IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626IntervalNumber.setStatus("mandatory")


class _Uas7626IntervalStat_Type(OctetString):
    """Custom type uas7626IntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Uas7626IntervalStat_Type.__name__ = "OctetString"
_Uas7626IntervalStat_Object = MibTableColumn
uas7626IntervalStat = _Uas7626IntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 3),
    _Uas7626IntervalStat_Type()
)
uas7626IntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626IntervalStat.setStatus("mandatory")
_Uas7626TotalTable_Object = MibTable
uas7626TotalTable = _Uas7626TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5)
)
if mibBuilder.loadTexts:
    uas7626TotalTable.setStatus("mandatory")
_Uas7626TotalEntry_Object = MibTableRow
uas7626TotalEntry = _Uas7626TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1)
)
uas7626TotalEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626TotalIndex"),
)
if mibBuilder.loadTexts:
    uas7626TotalEntry.setStatus("mandatory")
_Uas7626TotalIndex_Type = SCinstance
_Uas7626TotalIndex_Object = MibTableColumn
uas7626TotalIndex = _Uas7626TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1, 1),
    _Uas7626TotalIndex_Type()
)
uas7626TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626TotalIndex.setStatus("mandatory")


class _Uas7626TotalStat_Type(OctetString):
    """Custom type uas7626TotalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Uas7626TotalStat_Type.__name__ = "OctetString"
_Uas7626TotalStat_Object = MibTableColumn
uas7626TotalStat = _Uas7626TotalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1, 2),
    _Uas7626TotalStat_Type()
)
uas7626TotalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626TotalStat.setStatus("mandatory")
_Uas7626Recent24HrTable_Object = MibTable
uas7626Recent24HrTable = _Uas7626Recent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6)
)
if mibBuilder.loadTexts:
    uas7626Recent24HrTable.setStatus("mandatory")
_Uas7626Recent24HrEntry_Object = MibTableRow
uas7626Recent24HrEntry = _Uas7626Recent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1)
)
uas7626Recent24HrEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626Recent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7626Recent24HrEntry.setStatus("mandatory")
_Uas7626Recent24HrIndex_Type = SCinstance
_Uas7626Recent24HrIndex_Object = MibTableColumn
uas7626Recent24HrIndex = _Uas7626Recent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1, 1),
    _Uas7626Recent24HrIndex_Type()
)
uas7626Recent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626Recent24HrIndex.setStatus("mandatory")


class _Uas7626Recent24HrStat_Type(OctetString):
    """Custom type uas7626Recent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Uas7626Recent24HrStat_Type.__name__ = "OctetString"
_Uas7626Recent24HrStat_Object = MibTableColumn
uas7626Recent24HrStat = _Uas7626Recent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1, 2),
    _Uas7626Recent24HrStat_Type()
)
uas7626Recent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626Recent24HrStat.setStatus("mandatory")
_Uas7626UnavailableTimeRegTable_Object = MibTable
uas7626UnavailableTimeRegTable = _Uas7626UnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7)
)
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegTable.setStatus("mandatory")
_Uas7626UnavailableTimeRegEntry_Object = MibTableRow
uas7626UnavailableTimeRegEntry = _Uas7626UnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1)
)
uas7626UnavailableTimeRegEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626UnavailableTimeRegIndex"),
    (0, "GDCUAS7626-MIB", "uas7626UnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegEntry.setStatus("mandatory")
_Uas7626UnavailableTimeRegIndex_Type = SCinstance
_Uas7626UnavailableTimeRegIndex_Object = MibTableColumn
uas7626UnavailableTimeRegIndex = _Uas7626UnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 1),
    _Uas7626UnavailableTimeRegIndex_Type()
)
uas7626UnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegIndex.setStatus("mandatory")


class _Uas7626UnavailableTimeRegNumber_Type(Integer32):
    """Custom type uas7626UnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Uas7626UnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Uas7626UnavailableTimeRegNumber_Object = MibTableColumn
uas7626UnavailableTimeRegNumber = _Uas7626UnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 2),
    _Uas7626UnavailableTimeRegNumber_Type()
)
uas7626UnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegNumber.setStatus("mandatory")


class _Uas7626UnavailableTimeRegStart_Type(Integer32):
    """Custom type uas7626UnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7626UnavailableTimeRegStart_Type.__name__ = "Integer32"
_Uas7626UnavailableTimeRegStart_Object = MibTableColumn
uas7626UnavailableTimeRegStart = _Uas7626UnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 3),
    _Uas7626UnavailableTimeRegStart_Type()
)
uas7626UnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegStart.setStatus("mandatory")


class _Uas7626UnavailableTimeRegStop_Type(Integer32):
    """Custom type uas7626UnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7626UnavailableTimeRegStop_Type.__name__ = "Integer32"
_Uas7626UnavailableTimeRegStop_Object = MibTableColumn
uas7626UnavailableTimeRegStop = _Uas7626UnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 4),
    _Uas7626UnavailableTimeRegStop_Type()
)
uas7626UnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626UnavailableTimeRegStop.setStatus("mandatory")
_Uas7626AlarmConfig_ObjectIdentity = ObjectIdentity
uas7626AlarmConfig = _Uas7626AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6)
)
_Uas7626AlarmConfigTable_Object = MibTable
uas7626AlarmConfigTable = _Uas7626AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1)
)
if mibBuilder.loadTexts:
    uas7626AlarmConfigTable.setStatus("mandatory")
_Uas7626AlarmConfigEntry_Object = MibTableRow
uas7626AlarmConfigEntry = _Uas7626AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1)
)
uas7626AlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626AlarmConfigIndex"),
    (0, "GDCUAS7626-MIB", "uas7626AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7626AlarmConfigEntry.setStatus("mandatory")
_Uas7626AlarmConfigIndex_Type = SCinstance
_Uas7626AlarmConfigIndex_Object = MibTableColumn
uas7626AlarmConfigIndex = _Uas7626AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 1),
    _Uas7626AlarmConfigIndex_Type()
)
uas7626AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626AlarmConfigIndex.setStatus("mandatory")
_Uas7626AlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7626AlarmConfigIdentifier_Object = MibTableColumn
uas7626AlarmConfigIdentifier = _Uas7626AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 2),
    _Uas7626AlarmConfigIdentifier_Type()
)
uas7626AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626AlarmConfigIdentifier.setStatus("mandatory")


class _Uas7626AlarmCountThreshold_Type(Integer32):
    """Custom type uas7626AlarmCountThreshold based on Integer32"""
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
        *(("thres10E03", 1),
          ("thres10E04", 2),
          ("thres10E05", 3),
          ("thres10E06", 4))
    )


_Uas7626AlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7626AlarmCountThreshold_Object = MibTableColumn
uas7626AlarmCountThreshold = _Uas7626AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 3),
    _Uas7626AlarmCountThreshold_Type()
)
uas7626AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626AlarmCountThreshold.setStatus("mandatory")
_Uas7626LocalAlarmConfigTable_Object = MibTable
uas7626LocalAlarmConfigTable = _Uas7626LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2)
)
if mibBuilder.loadTexts:
    uas7626LocalAlarmConfigTable.setStatus("mandatory")
_Uas7626LocalAlarmConfigEntry_Object = MibTableRow
uas7626LocalAlarmConfigEntry = _Uas7626LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1)
)
uas7626LocalAlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7626-MIB", "uas7626LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7626LocalAlarmConfigEntry.setStatus("mandatory")
_Uas7626LocalAlarmConfigIndex_Type = SCinstance
_Uas7626LocalAlarmConfigIndex_Object = MibTableColumn
uas7626LocalAlarmConfigIndex = _Uas7626LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 1),
    _Uas7626LocalAlarmConfigIndex_Type()
)
uas7626LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7626LocalAlarmConfigIndex.setStatus("mandatory")


class _Uas7626LossOfClockLocal_Type(Integer32):
    """Custom type uas7626LossOfClockLocal based on Integer32"""
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
          ("enabledMajor", 3),
          ("enabledMinor", 2))
    )


_Uas7626LossOfClockLocal_Type.__name__ = "Integer32"
_Uas7626LossOfClockLocal_Object = MibTableColumn
uas7626LossOfClockLocal = _Uas7626LossOfClockLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 2),
    _Uas7626LossOfClockLocal_Type()
)
uas7626LossOfClockLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626LossOfClockLocal.setStatus("mandatory")


class _Uas7626ESLocal_Type(Integer32):
    """Custom type uas7626ESLocal based on Integer32"""
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
          ("enabledMajor", 3),
          ("enabledMinor", 2))
    )


_Uas7626ESLocal_Type.__name__ = "Integer32"
_Uas7626ESLocal_Object = MibTableColumn
uas7626ESLocal = _Uas7626ESLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 3),
    _Uas7626ESLocal_Type()
)
uas7626ESLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626ESLocal.setStatus("mandatory")


class _Uas7626UASLocal_Type(Integer32):
    """Custom type uas7626UASLocal based on Integer32"""
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
          ("enabledMajor", 3),
          ("enabledMinor", 2))
    )


_Uas7626UASLocal_Type.__name__ = "Integer32"
_Uas7626UASLocal_Object = MibTableColumn
uas7626UASLocal = _Uas7626UASLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 4),
    _Uas7626UASLocal_Type()
)
uas7626UASLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626UASLocal.setStatus("mandatory")


class _Uas7626OutofSyncLocal_Type(Integer32):
    """Custom type uas7626OutofSyncLocal based on Integer32"""
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
          ("enabledMajor", 3),
          ("enabledMinor", 2))
    )


_Uas7626OutofSyncLocal_Type.__name__ = "Integer32"
_Uas7626OutofSyncLocal_Object = MibTableColumn
uas7626OutofSyncLocal = _Uas7626OutofSyncLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 5),
    _Uas7626OutofSyncLocal_Type()
)
uas7626OutofSyncLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626OutofSyncLocal.setStatus("mandatory")


class _Uas7626NoSealingCurrentLocal_Type(Integer32):
    """Custom type uas7626NoSealingCurrentLocal based on Integer32"""
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
          ("enabledMajor", 3),
          ("enabledMinor", 2))
    )


_Uas7626NoSealingCurrentLocal_Type.__name__ = "Integer32"
_Uas7626NoSealingCurrentLocal_Object = MibTableColumn
uas7626NoSealingCurrentLocal = _Uas7626NoSealingCurrentLocal_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 6),
    _Uas7626NoSealingCurrentLocal_Type()
)
uas7626NoSealingCurrentLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7626NoSealingCurrentLocal.setStatus("mandatory")
_Uas7626Alarms_ObjectIdentity = ObjectIdentity
uas7626Alarms = _Uas7626Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7)
)
_Uas7626NoResponseAlm_ObjectIdentity = ObjectIdentity
uas7626NoResponseAlm = _Uas7626NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 1)
)
_Uas7626DiagRxErrAlm_ObjectIdentity = ObjectIdentity
uas7626DiagRxErrAlm = _Uas7626DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 2)
)
_Uas7626PowerUpAlm_ObjectIdentity = ObjectIdentity
uas7626PowerUpAlm = _Uas7626PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 3)
)
_Uas7626LossofTransmitClockAlm_ObjectIdentity = ObjectIdentity
uas7626LossofTransmitClockAlm = _Uas7626LossofTransmitClockAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 4)
)
_Uas7626OutofSyncAlm_ObjectIdentity = ObjectIdentity
uas7626OutofSyncAlm = _Uas7626OutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 5)
)
_Uas7626SealingCurrentNoContAlm_ObjectIdentity = ObjectIdentity
uas7626SealingCurrentNoContAlm = _Uas7626SealingCurrentNoContAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 6)
)
_Uas7626UASAlm_ObjectIdentity = ObjectIdentity
uas7626UASAlm = _Uas7626UASAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 7)
)
_Uas7626ESAlm_ObjectIdentity = ObjectIdentity
uas7626ESAlm = _Uas7626ESAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 8)
)
_Uas7626MajorBERAlm_ObjectIdentity = ObjectIdentity
uas7626MajorBERAlm = _Uas7626MajorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 9)
)
_Uas7626MinorBERAlm_ObjectIdentity = ObjectIdentity
uas7626MinorBERAlm = _Uas7626MinorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCUAS7626-MIB",
    **{"gdc": gdc,
       "bql2": bql2,
       "uas7626": uas7626,
       "uas7626Version": uas7626Version,
       "uas7626MIBversion": uas7626MIBversion,
       "uas7626VersionTable": uas7626VersionTable,
       "uas7626VersionEntry": uas7626VersionEntry,
       "uas7626VersionIndex": uas7626VersionIndex,
       "uas7626ActiveFirmwareRev": uas7626ActiveFirmwareRev,
       "uas7626StoredFirmwareRev": uas7626StoredFirmwareRev,
       "uas7626StoredFirmwareStatus": uas7626StoredFirmwareStatus,
       "uas7626SwitchActiveFirmware": uas7626SwitchActiveFirmware,
       "uas7626DownloadingMode": uas7626DownloadingMode,
       "uas7626Maintenance": uas7626Maintenance,
       "uas7626MaintenanceTable": uas7626MaintenanceTable,
       "uas7626MaintenanceEntry": uas7626MaintenanceEntry,
       "uas7626MaintenanceLineIndex": uas7626MaintenanceLineIndex,
       "uas7626SoftReset": uas7626SoftReset,
       "uas7626DefaultInit": uas7626DefaultInit,
       "uas7626ResetMajorAlarm": uas7626ResetMajorAlarm,
       "uas7626ResetMinorAlarm": uas7626ResetMinorAlarm,
       "uas7626ResetStatistics": uas7626ResetStatistics,
       "uas7626ValidIntervals": uas7626ValidIntervals,
       "uas7626SysUpTime": uas7626SysUpTime,
       "uas7626LedStatus": uas7626LedStatus,
       "uas7626AlarmStatus": uas7626AlarmStatus,
       "uas7626StatLastInitialized": uas7626StatLastInitialized,
       "uas7626CircuitID": uas7626CircuitID,
       "uas7626Configuration": uas7626Configuration,
       "uas7626ConfigTable": uas7626ConfigTable,
       "uas7626ConfigEntry": uas7626ConfigEntry,
       "uas7626ConfigIndex": uas7626ConfigIndex,
       "uas7626DataRate": uas7626DataRate,
       "uas7626Highway": uas7626Highway,
       "uas7626TimeSlot": uas7626TimeSlot,
       "uas7626Diagnostics": uas7626Diagnostics,
       "uas7626DiagTable": uas7626DiagTable,
       "uas7626DiagEntry": uas7626DiagEntry,
       "uas7626DiagIndex": uas7626DiagIndex,
       "uas7626TestSelection": uas7626TestSelection,
       "uas7626TestResults": uas7626TestResults,
       "uas7626ResetTestResults": uas7626ResetTestResults,
       "uas7626Performance": uas7626Performance,
       "uas7626CurrentTable": uas7626CurrentTable,
       "uas7626CurrentEntry": uas7626CurrentEntry,
       "uas7626CurrentIndex": uas7626CurrentIndex,
       "uas7626CurrentStat": uas7626CurrentStat,
       "uas7626IntervalTable": uas7626IntervalTable,
       "uas7626IntervalEntry": uas7626IntervalEntry,
       "uas7626IntervalIndex": uas7626IntervalIndex,
       "uas7626IntervalNumber": uas7626IntervalNumber,
       "uas7626IntervalStat": uas7626IntervalStat,
       "uas7626TotalTable": uas7626TotalTable,
       "uas7626TotalEntry": uas7626TotalEntry,
       "uas7626TotalIndex": uas7626TotalIndex,
       "uas7626TotalStat": uas7626TotalStat,
       "uas7626Recent24HrTable": uas7626Recent24HrTable,
       "uas7626Recent24HrEntry": uas7626Recent24HrEntry,
       "uas7626Recent24HrIndex": uas7626Recent24HrIndex,
       "uas7626Recent24HrStat": uas7626Recent24HrStat,
       "uas7626UnavailableTimeRegTable": uas7626UnavailableTimeRegTable,
       "uas7626UnavailableTimeRegEntry": uas7626UnavailableTimeRegEntry,
       "uas7626UnavailableTimeRegIndex": uas7626UnavailableTimeRegIndex,
       "uas7626UnavailableTimeRegNumber": uas7626UnavailableTimeRegNumber,
       "uas7626UnavailableTimeRegStart": uas7626UnavailableTimeRegStart,
       "uas7626UnavailableTimeRegStop": uas7626UnavailableTimeRegStop,
       "uas7626AlarmConfig": uas7626AlarmConfig,
       "uas7626AlarmConfigTable": uas7626AlarmConfigTable,
       "uas7626AlarmConfigEntry": uas7626AlarmConfigEntry,
       "uas7626AlarmConfigIndex": uas7626AlarmConfigIndex,
       "uas7626AlarmConfigIdentifier": uas7626AlarmConfigIdentifier,
       "uas7626AlarmCountThreshold": uas7626AlarmCountThreshold,
       "uas7626LocalAlarmConfigTable": uas7626LocalAlarmConfigTable,
       "uas7626LocalAlarmConfigEntry": uas7626LocalAlarmConfigEntry,
       "uas7626LocalAlarmConfigIndex": uas7626LocalAlarmConfigIndex,
       "uas7626LossOfClockLocal": uas7626LossOfClockLocal,
       "uas7626ESLocal": uas7626ESLocal,
       "uas7626UASLocal": uas7626UASLocal,
       "uas7626OutofSyncLocal": uas7626OutofSyncLocal,
       "uas7626NoSealingCurrentLocal": uas7626NoSealingCurrentLocal,
       "uas7626Alarms": uas7626Alarms,
       "uas7626NoResponseAlm": uas7626NoResponseAlm,
       "uas7626DiagRxErrAlm": uas7626DiagRxErrAlm,
       "uas7626PowerUpAlm": uas7626PowerUpAlm,
       "uas7626LossofTransmitClockAlm": uas7626LossofTransmitClockAlm,
       "uas7626OutofSyncAlm": uas7626OutofSyncAlm,
       "uas7626SealingCurrentNoContAlm": uas7626SealingCurrentNoContAlm,
       "uas7626UASAlm": uas7626UASAlm,
       "uas7626ESAlm": uas7626ESAlm,
       "uas7626MajorBERAlm": uas7626MajorBERAlm,
       "uas7626MinorBERAlm": uas7626MinorBERAlm}
)
