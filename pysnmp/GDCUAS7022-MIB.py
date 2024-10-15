# SNMP MIB module (GDCUAS7022-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCUAS7022-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:22 2024
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
_Uas7022_ObjectIdentity = ObjectIdentity
uas7022 = _Uas7022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13)
)
_Uas7022Version_ObjectIdentity = ObjectIdentity
uas7022Version = _Uas7022Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1)
)


class _Uas7022MIBversion_Type(DisplayString):
    """Custom type uas7022MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Uas7022MIBversion_Type.__name__ = "DisplayString"
_Uas7022MIBversion_Object = MibScalar
uas7022MIBversion = _Uas7022MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 1),
    _Uas7022MIBversion_Type()
)
uas7022MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022MIBversion.setStatus("mandatory")
_Uas7022VersionTable_Object = MibTable
uas7022VersionTable = _Uas7022VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2)
)
if mibBuilder.loadTexts:
    uas7022VersionTable.setStatus("mandatory")
_Uas7022VersionEntry_Object = MibTableRow
uas7022VersionEntry = _Uas7022VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1)
)
uas7022VersionEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022VersionIndex"),
)
if mibBuilder.loadTexts:
    uas7022VersionEntry.setStatus("mandatory")
_Uas7022VersionIndex_Type = SCinstance
_Uas7022VersionIndex_Object = MibTableColumn
uas7022VersionIndex = _Uas7022VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 1),
    _Uas7022VersionIndex_Type()
)
uas7022VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022VersionIndex.setStatus("mandatory")


class _Uas7022ActiveFirmwareRev_Type(DisplayString):
    """Custom type uas7022ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Uas7022ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Uas7022ActiveFirmwareRev_Object = MibTableColumn
uas7022ActiveFirmwareRev = _Uas7022ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 2),
    _Uas7022ActiveFirmwareRev_Type()
)
uas7022ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022ActiveFirmwareRev.setStatus("mandatory")


class _Uas7022StoredFirmwareRev_Type(DisplayString):
    """Custom type uas7022StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Uas7022StoredFirmwareRev_Type.__name__ = "DisplayString"
_Uas7022StoredFirmwareRev_Object = MibTableColumn
uas7022StoredFirmwareRev = _Uas7022StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 3),
    _Uas7022StoredFirmwareRev_Type()
)
uas7022StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022StoredFirmwareRev.setStatus("mandatory")


class _Uas7022StoredFirmwareStatus_Type(Integer32):
    """Custom type uas7022StoredFirmwareStatus based on Integer32"""
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


_Uas7022StoredFirmwareStatus_Type.__name__ = "Integer32"
_Uas7022StoredFirmwareStatus_Object = MibTableColumn
uas7022StoredFirmwareStatus = _Uas7022StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 4),
    _Uas7022StoredFirmwareStatus_Type()
)
uas7022StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022StoredFirmwareStatus.setStatus("mandatory")


class _Uas7022SwitchActiveFirmware_Type(Integer32):
    """Custom type uas7022SwitchActiveFirmware based on Integer32"""
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


_Uas7022SwitchActiveFirmware_Type.__name__ = "Integer32"
_Uas7022SwitchActiveFirmware_Object = MibTableColumn
uas7022SwitchActiveFirmware = _Uas7022SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 5),
    _Uas7022SwitchActiveFirmware_Type()
)
uas7022SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022SwitchActiveFirmware.setStatus("mandatory")


class _Uas7022DownloadingMode_Type(Integer32):
    """Custom type uas7022DownloadingMode based on Integer32"""
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


_Uas7022DownloadingMode_Type.__name__ = "Integer32"
_Uas7022DownloadingMode_Object = MibTableColumn
uas7022DownloadingMode = _Uas7022DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 1, 2, 1, 6),
    _Uas7022DownloadingMode_Type()
)
uas7022DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022DownloadingMode.setStatus("mandatory")
_Uas7022Maintenance_ObjectIdentity = ObjectIdentity
uas7022Maintenance = _Uas7022Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2)
)
_Uas7022MaintenanceTable_Object = MibTable
uas7022MaintenanceTable = _Uas7022MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1)
)
if mibBuilder.loadTexts:
    uas7022MaintenanceTable.setStatus("mandatory")
_Uas7022MaintenanceEntry_Object = MibTableRow
uas7022MaintenanceEntry = _Uas7022MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1)
)
uas7022MaintenanceEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    uas7022MaintenanceEntry.setStatus("mandatory")
_Uas7022MaintenanceLineIndex_Type = SCinstance
_Uas7022MaintenanceLineIndex_Object = MibTableColumn
uas7022MaintenanceLineIndex = _Uas7022MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 1),
    _Uas7022MaintenanceLineIndex_Type()
)
uas7022MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022MaintenanceLineIndex.setStatus("mandatory")


class _Uas7022SoftReset_Type(Integer32):
    """Custom type uas7022SoftReset based on Integer32"""
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


_Uas7022SoftReset_Type.__name__ = "Integer32"
_Uas7022SoftReset_Object = MibTableColumn
uas7022SoftReset = _Uas7022SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 2),
    _Uas7022SoftReset_Type()
)
uas7022SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022SoftReset.setStatus("mandatory")


class _Uas7022SysUpTime_Type(Integer32):
    """Custom type uas7022SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022SysUpTime_Type.__name__ = "Integer32"
_Uas7022SysUpTime_Object = MibTableColumn
uas7022SysUpTime = _Uas7022SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 3),
    _Uas7022SysUpTime_Type()
)
uas7022SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022SysUpTime.setStatus("mandatory")


class _Uas7022DefaultInit_Type(Integer32):
    """Custom type uas7022DefaultInit based on Integer32"""
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


_Uas7022DefaultInit_Type.__name__ = "Integer32"
_Uas7022DefaultInit_Object = MibTableColumn
uas7022DefaultInit = _Uas7022DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 4),
    _Uas7022DefaultInit_Type()
)
uas7022DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022DefaultInit.setStatus("mandatory")


class _Uas7022LedStatus_Type(OctetString):
    """Custom type uas7022LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Uas7022LedStatus_Type.__name__ = "OctetString"
_Uas7022LedStatus_Object = MibTableColumn
uas7022LedStatus = _Uas7022LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 5),
    _Uas7022LedStatus_Type()
)
uas7022LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022LedStatus.setStatus("mandatory")


class _Uas7022AlarmStatus_Type(OctetString):
    """Custom type uas7022AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Uas7022AlarmStatus_Type.__name__ = "OctetString"
_Uas7022AlarmStatus_Object = MibTableColumn
uas7022AlarmStatus = _Uas7022AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 6),
    _Uas7022AlarmStatus_Type()
)
uas7022AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022AlarmStatus.setStatus("mandatory")


class _Uas7022NearEndResetStats_Type(Integer32):
    """Custom type uas7022NearEndResetStats based on Integer32"""
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


_Uas7022NearEndResetStats_Type.__name__ = "Integer32"
_Uas7022NearEndResetStats_Object = MibTableColumn
uas7022NearEndResetStats = _Uas7022NearEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 7),
    _Uas7022NearEndResetStats_Type()
)
uas7022NearEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NearEndResetStats.setStatus("mandatory")


class _Uas7022FarEndResetStats_Type(Integer32):
    """Custom type uas7022FarEndResetStats based on Integer32"""
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


_Uas7022FarEndResetStats_Type.__name__ = "Integer32"
_Uas7022FarEndResetStats_Object = MibTableColumn
uas7022FarEndResetStats = _Uas7022FarEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 8),
    _Uas7022FarEndResetStats_Type()
)
uas7022FarEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022FarEndResetStats.setStatus("mandatory")


class _Uas7022NearEndStatLastInit_Type(Integer32):
    """Custom type uas7022NearEndStatLastInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022NearEndStatLastInit_Type.__name__ = "Integer32"
_Uas7022NearEndStatLastInit_Object = MibTableColumn
uas7022NearEndStatLastInit = _Uas7022NearEndStatLastInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 9),
    _Uas7022NearEndStatLastInit_Type()
)
uas7022NearEndStatLastInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndStatLastInit.setStatus("mandatory")


class _Uas7022FarEndStatLastInit_Type(Integer32):
    """Custom type uas7022FarEndStatLastInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022FarEndStatLastInit_Type.__name__ = "Integer32"
_Uas7022FarEndStatLastInit_Object = MibTableColumn
uas7022FarEndStatLastInit = _Uas7022FarEndStatLastInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 10),
    _Uas7022FarEndStatLastInit_Type()
)
uas7022FarEndStatLastInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndStatLastInit.setStatus("mandatory")


class _Uas7022NearEndValidIntervals_Type(Integer32):
    """Custom type uas7022NearEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Uas7022NearEndValidIntervals_Type.__name__ = "Integer32"
_Uas7022NearEndValidIntervals_Object = MibTableColumn
uas7022NearEndValidIntervals = _Uas7022NearEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 11),
    _Uas7022NearEndValidIntervals_Type()
)
uas7022NearEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndValidIntervals.setStatus("mandatory")


class _Uas7022FarEndValidIntervals_Type(Integer32):
    """Custom type uas7022FarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Uas7022FarEndValidIntervals_Type.__name__ = "Integer32"
_Uas7022FarEndValidIntervals_Object = MibTableColumn
uas7022FarEndValidIntervals = _Uas7022FarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 12),
    _Uas7022FarEndValidIntervals_Type()
)
uas7022FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndValidIntervals.setStatus("mandatory")


class _Uas7022NIUaCircuitID_Type(DisplayString):
    """Custom type uas7022NIUaCircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Uas7022NIUaCircuitID_Type.__name__ = "DisplayString"
_Uas7022NIUaCircuitID_Object = MibTableColumn
uas7022NIUaCircuitID = _Uas7022NIUaCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 13),
    _Uas7022NIUaCircuitID_Type()
)
uas7022NIUaCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NIUaCircuitID.setStatus("mandatory")


class _Uas7022SystemTimingGenStatus_Type(Integer32):
    """Custom type uas7022SystemTimingGenStatus based on Integer32"""
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


_Uas7022SystemTimingGenStatus_Type.__name__ = "Integer32"
_Uas7022SystemTimingGenStatus_Object = MibTableColumn
uas7022SystemTimingGenStatus = _Uas7022SystemTimingGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 14),
    _Uas7022SystemTimingGenStatus_Type()
)
uas7022SystemTimingGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022SystemTimingGenStatus.setStatus("mandatory")


class _Uas7022NIUbCircuitID_Type(DisplayString):
    """Custom type uas7022NIUbCircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Uas7022NIUbCircuitID_Type.__name__ = "DisplayString"
_Uas7022NIUbCircuitID_Object = MibTableColumn
uas7022NIUbCircuitID = _Uas7022NIUbCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 2, 1, 1, 15),
    _Uas7022NIUbCircuitID_Type()
)
uas7022NIUbCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NIUbCircuitID.setStatus("mandatory")
_Uas7022Configuration_ObjectIdentity = ObjectIdentity
uas7022Configuration = _Uas7022Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3)
)
_Uas7022ConfigTable_Object = MibTable
uas7022ConfigTable = _Uas7022ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1)
)
if mibBuilder.loadTexts:
    uas7022ConfigTable.setStatus("mandatory")
_Uas7022ConfigEntry_Object = MibTableRow
uas7022ConfigEntry = _Uas7022ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1)
)
uas7022ConfigEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022ConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7022ConfigEntry.setStatus("mandatory")
_Uas7022ConfigIndex_Type = SCinstance
_Uas7022ConfigIndex_Object = MibTableColumn
uas7022ConfigIndex = _Uas7022ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 1),
    _Uas7022ConfigIndex_Type()
)
uas7022ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022ConfigIndex.setStatus("mandatory")


class _Uas7022RcvrRange_Type(Integer32):
    """Custom type uas7022RcvrRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_Uas7022RcvrRange_Type.__name__ = "Integer32"
_Uas7022RcvrRange_Object = MibTableColumn
uas7022RcvrRange = _Uas7022RcvrRange_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 2),
    _Uas7022RcvrRange_Type()
)
uas7022RcvrRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022RcvrRange.setStatus("mandatory")


class _Uas7022Framing_Type(Integer32):
    """Custom type uas7022Framing based on Integer32"""
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
        *(("cASwithCRC4", 4),
          ("cASwithoutCRC4", 2),
          ("cCSwithCRC4", 3),
          ("cCSwithoutCRC4", 1))
    )


_Uas7022Framing_Type.__name__ = "Integer32"
_Uas7022Framing_Object = MibTableColumn
uas7022Framing = _Uas7022Framing_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 3),
    _Uas7022Framing_Type()
)
uas7022Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022Framing.setStatus("mandatory")


class _Uas7022SysTimingGen_Type(Integer32):
    """Custom type uas7022SysTimingGen based on Integer32"""
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


_Uas7022SysTimingGen_Type.__name__ = "Integer32"
_Uas7022SysTimingGen_Object = MibTableColumn
uas7022SysTimingGen = _Uas7022SysTimingGen_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 4),
    _Uas7022SysTimingGen_Type()
)
uas7022SysTimingGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022SysTimingGen.setStatus("mandatory")


class _Uas7022Highway_Type(Integer32):
    """Custom type uas7022Highway based on Integer32"""
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


_Uas7022Highway_Type.__name__ = "Integer32"
_Uas7022Highway_Object = MibTableColumn
uas7022Highway = _Uas7022Highway_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 5),
    _Uas7022Highway_Type()
)
uas7022Highway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022Highway.setStatus("mandatory")


class _Uas7022TransmitClockSource_Type(Integer32):
    """Custom type uas7022TransmitClockSource based on Integer32"""
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


_Uas7022TransmitClockSource_Type.__name__ = "Integer32"
_Uas7022TransmitClockSource_Object = MibTableColumn
uas7022TransmitClockSource = _Uas7022TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 6),
    _Uas7022TransmitClockSource_Type()
)
uas7022TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022TransmitClockSource.setStatus("mandatory")


class _Uas7022FallbackClockSource_Type(Integer32):
    """Custom type uas7022FallbackClockSource based on Integer32"""
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


_Uas7022FallbackClockSource_Type.__name__ = "Integer32"
_Uas7022FallbackClockSource_Object = MibTableColumn
uas7022FallbackClockSource = _Uas7022FallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 7),
    _Uas7022FallbackClockSource_Type()
)
uas7022FallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022FallbackClockSource.setStatus("mandatory")


class _Uas7022InterfaceType_Type(Integer32):
    """Custom type uas7022InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("unassigned", 2))
    )


_Uas7022InterfaceType_Type.__name__ = "Integer32"
_Uas7022InterfaceType_Object = MibTableColumn
uas7022InterfaceType = _Uas7022InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 8),
    _Uas7022InterfaceType_Type()
)
uas7022InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022InterfaceType.setStatus("mandatory")


class _Uas7022FDLMode_Type(Integer32):
    """Custom type uas7022FDLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("none", 1))
    )


_Uas7022FDLMode_Type.__name__ = "Integer32"
_Uas7022FDLMode_Object = MibTableColumn
uas7022FDLMode = _Uas7022FDLMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 9),
    _Uas7022FDLMode_Type()
)
uas7022FDLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022FDLMode.setStatus("mandatory")


class _Uas7022TimeSlot16Content_Type(Integer32):
    """Custom type uas7022TimeSlot16Content based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 3),
          ("idle", 1),
          ("marks", 2))
    )


_Uas7022TimeSlot16Content_Type.__name__ = "Integer32"
_Uas7022TimeSlot16Content_Object = MibTableColumn
uas7022TimeSlot16Content = _Uas7022TimeSlot16Content_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 10),
    _Uas7022TimeSlot16Content_Type()
)
uas7022TimeSlot16Content.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022TimeSlot16Content.setStatus("mandatory")


class _Uas7022Impedance_Type(Integer32):
    """Custom type uas7022Impedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impedance120Ohm", 1),
          ("impedance75Ohm", 2))
    )


_Uas7022Impedance_Type.__name__ = "Integer32"
_Uas7022Impedance_Object = MibTableColumn
uas7022Impedance = _Uas7022Impedance_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 3, 1, 1, 11),
    _Uas7022Impedance_Type()
)
uas7022Impedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022Impedance.setStatus("mandatory")
_Uas7022Diagnostics_ObjectIdentity = ObjectIdentity
uas7022Diagnostics = _Uas7022Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4)
)
_Uas7022DiagTable_Object = MibTable
uas7022DiagTable = _Uas7022DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1)
)
if mibBuilder.loadTexts:
    uas7022DiagTable.setStatus("mandatory")
_Uas7022DiagEntry_Object = MibTableRow
uas7022DiagEntry = _Uas7022DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1)
)
uas7022DiagEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022DiagIndex"),
)
if mibBuilder.loadTexts:
    uas7022DiagEntry.setStatus("mandatory")
_Uas7022DiagIndex_Type = SCinstance
_Uas7022DiagIndex_Object = MibTableColumn
uas7022DiagIndex = _Uas7022DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1, 1),
    _Uas7022DiagIndex_Type()
)
uas7022DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022DiagIndex.setStatus("mandatory")


class _Uas7022DiagConfig_Type(Integer32):
    """Custom type uas7022DiagConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineLoopback", 2),
          ("noLoop", 1),
          ("payloadLoopback", 3))
    )


_Uas7022DiagConfig_Type.__name__ = "Integer32"
_Uas7022DiagConfig_Object = MibTableColumn
uas7022DiagConfig = _Uas7022DiagConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1, 2),
    _Uas7022DiagConfig_Type()
)
uas7022DiagConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022DiagConfig.setStatus("mandatory")


class _Uas7022TestLimit_Type(Integer32):
    """Custom type uas7022TestLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 3),
          ("testTime10Mins", 1),
          ("testTime20Mins", 2))
    )


_Uas7022TestLimit_Type.__name__ = "Integer32"
_Uas7022TestLimit_Object = MibTableColumn
uas7022TestLimit = _Uas7022TestLimit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1, 3),
    _Uas7022TestLimit_Type()
)
uas7022TestLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022TestLimit.setStatus("mandatory")


class _Uas7022TestExecutionStatus_Type(Integer32):
    """Custom type uas7022TestExecutionStatus based on Integer32"""
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


_Uas7022TestExecutionStatus_Type.__name__ = "Integer32"
_Uas7022TestExecutionStatus_Object = MibTableColumn
uas7022TestExecutionStatus = _Uas7022TestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1, 4),
    _Uas7022TestExecutionStatus_Type()
)
uas7022TestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022TestExecutionStatus.setStatus("mandatory")


class _Uas7022TestExceptions_Type(Integer32):
    """Custom type uas7022TestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Uas7022TestExceptions_Type.__name__ = "Integer32"
_Uas7022TestExceptions_Object = MibTableColumn
uas7022TestExceptions = _Uas7022TestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 4, 1, 1, 5),
    _Uas7022TestExceptions_Type()
)
uas7022TestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022TestExceptions.setStatus("mandatory")
_Uas7022Performance_ObjectIdentity = ObjectIdentity
uas7022Performance = _Uas7022Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5)
)
_Uas7022NearEndCurrent15MinTable_Object = MibTable
uas7022NearEndCurrent15MinTable = _Uas7022NearEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 1)
)
if mibBuilder.loadTexts:
    uas7022NearEndCurrent15MinTable.setStatus("mandatory")
_Uas7022NearEndCurrent15MinEntry_Object = MibTableRow
uas7022NearEndCurrent15MinEntry = _Uas7022NearEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 1, 1)
)
uas7022NearEndCurrent15MinEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    uas7022NearEndCurrent15MinEntry.setStatus("mandatory")
_Uas7022NearEndCurrent15MinIndex_Type = SCinstance
_Uas7022NearEndCurrent15MinIndex_Object = MibTableColumn
uas7022NearEndCurrent15MinIndex = _Uas7022NearEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 1, 1, 1),
    _Uas7022NearEndCurrent15MinIndex_Type()
)
uas7022NearEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndCurrent15MinIndex.setStatus("mandatory")


class _Uas7022NearEndCurrent15MinStat_Type(OctetString):
    """Custom type uas7022NearEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Uas7022NearEndCurrent15MinStat_Type.__name__ = "OctetString"
_Uas7022NearEndCurrent15MinStat_Object = MibTableColumn
uas7022NearEndCurrent15MinStat = _Uas7022NearEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 1, 1, 2),
    _Uas7022NearEndCurrent15MinStat_Type()
)
uas7022NearEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndCurrent15MinStat.setStatus("mandatory")
_Uas7022NearEndIntervalTable_Object = MibTable
uas7022NearEndIntervalTable = _Uas7022NearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 2)
)
if mibBuilder.loadTexts:
    uas7022NearEndIntervalTable.setStatus("mandatory")
_Uas7022NearEndIntervalEntry_Object = MibTableRow
uas7022NearEndIntervalEntry = _Uas7022NearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 2, 1)
)
uas7022NearEndIntervalEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndIntervalIndex"),
    (0, "GDCUAS7022-MIB", "uas7022NearEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    uas7022NearEndIntervalEntry.setStatus("mandatory")
_Uas7022NearEndIntervalIndex_Type = SCinstance
_Uas7022NearEndIntervalIndex_Object = MibTableColumn
uas7022NearEndIntervalIndex = _Uas7022NearEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 2, 1, 1),
    _Uas7022NearEndIntervalIndex_Type()
)
uas7022NearEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndIntervalIndex.setStatus("mandatory")


class _Uas7022NearEndIntervalNumber_Type(Integer32):
    """Custom type uas7022NearEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7022NearEndIntervalNumber_Type.__name__ = "Integer32"
_Uas7022NearEndIntervalNumber_Object = MibTableColumn
uas7022NearEndIntervalNumber = _Uas7022NearEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 2, 1, 2),
    _Uas7022NearEndIntervalNumber_Type()
)
uas7022NearEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndIntervalNumber.setStatus("mandatory")


class _Uas7022NearEndIntervalStat_Type(OctetString):
    """Custom type uas7022NearEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Uas7022NearEndIntervalStat_Type.__name__ = "OctetString"
_Uas7022NearEndIntervalStat_Object = MibTableColumn
uas7022NearEndIntervalStat = _Uas7022NearEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 2, 1, 3),
    _Uas7022NearEndIntervalStat_Type()
)
uas7022NearEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndIntervalStat.setStatus("mandatory")
_Uas7022NearEndCurrent24HrTable_Object = MibTable
uas7022NearEndCurrent24HrTable = _Uas7022NearEndCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 3)
)
if mibBuilder.loadTexts:
    uas7022NearEndCurrent24HrTable.setStatus("mandatory")
_Uas7022NearEndCurrent24HrEntry_Object = MibTableRow
uas7022NearEndCurrent24HrEntry = _Uas7022NearEndCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 3, 1)
)
uas7022NearEndCurrent24HrEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndCurrent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7022NearEndCurrent24HrEntry.setStatus("mandatory")
_Uas7022NearEndCurrent24HrIndex_Type = SCinstance
_Uas7022NearEndCurrent24HrIndex_Object = MibTableColumn
uas7022NearEndCurrent24HrIndex = _Uas7022NearEndCurrent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 3, 1, 1),
    _Uas7022NearEndCurrent24HrIndex_Type()
)
uas7022NearEndCurrent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndCurrent24HrIndex.setStatus("mandatory")


class _Uas7022NearEndCurrent24HrStat_Type(OctetString):
    """Custom type uas7022NearEndCurrent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Uas7022NearEndCurrent24HrStat_Type.__name__ = "OctetString"
_Uas7022NearEndCurrent24HrStat_Object = MibTableColumn
uas7022NearEndCurrent24HrStat = _Uas7022NearEndCurrent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 3, 1, 2),
    _Uas7022NearEndCurrent24HrStat_Type()
)
uas7022NearEndCurrent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndCurrent24HrStat.setStatus("mandatory")
_Uas7022NearEndRecent24HrTable_Object = MibTable
uas7022NearEndRecent24HrTable = _Uas7022NearEndRecent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 4)
)
if mibBuilder.loadTexts:
    uas7022NearEndRecent24HrTable.setStatus("mandatory")
_Uas7022NearEndRecent24HrEntry_Object = MibTableRow
uas7022NearEndRecent24HrEntry = _Uas7022NearEndRecent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 4, 1)
)
uas7022NearEndRecent24HrEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndRecent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7022NearEndRecent24HrEntry.setStatus("mandatory")
_Uas7022NearEndRecent24HrIndex_Type = SCinstance
_Uas7022NearEndRecent24HrIndex_Object = MibTableColumn
uas7022NearEndRecent24HrIndex = _Uas7022NearEndRecent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 4, 1, 1),
    _Uas7022NearEndRecent24HrIndex_Type()
)
uas7022NearEndRecent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndRecent24HrIndex.setStatus("mandatory")


class _Uas7022NearEndRecent24HrStat_Type(OctetString):
    """Custom type uas7022NearEndRecent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Uas7022NearEndRecent24HrStat_Type.__name__ = "OctetString"
_Uas7022NearEndRecent24HrStat_Object = MibTableColumn
uas7022NearEndRecent24HrStat = _Uas7022NearEndRecent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 4, 1, 2),
    _Uas7022NearEndRecent24HrStat_Type()
)
uas7022NearEndRecent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndRecent24HrStat.setStatus("mandatory")
_Uas7022FarEndCurrent15MinTable_Object = MibTable
uas7022FarEndCurrent15MinTable = _Uas7022FarEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 5)
)
if mibBuilder.loadTexts:
    uas7022FarEndCurrent15MinTable.setStatus("mandatory")
_Uas7022FarEndCurrent15MinEntry_Object = MibTableRow
uas7022FarEndCurrent15MinEntry = _Uas7022FarEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 5, 1)
)
uas7022FarEndCurrent15MinEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    uas7022FarEndCurrent15MinEntry.setStatus("mandatory")
_Uas7022FarEndCurrent15MinIndex_Type = SCinstance
_Uas7022FarEndCurrent15MinIndex_Object = MibTableColumn
uas7022FarEndCurrent15MinIndex = _Uas7022FarEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 5, 1, 1),
    _Uas7022FarEndCurrent15MinIndex_Type()
)
uas7022FarEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndCurrent15MinIndex.setStatus("mandatory")


class _Uas7022FarEndCurrent15MinStat_Type(OctetString):
    """Custom type uas7022FarEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Uas7022FarEndCurrent15MinStat_Type.__name__ = "OctetString"
_Uas7022FarEndCurrent15MinStat_Object = MibTableColumn
uas7022FarEndCurrent15MinStat = _Uas7022FarEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 5, 1, 2),
    _Uas7022FarEndCurrent15MinStat_Type()
)
uas7022FarEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndCurrent15MinStat.setStatus("mandatory")
_Uas7022FarEndIntervalTable_Object = MibTable
uas7022FarEndIntervalTable = _Uas7022FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 6)
)
if mibBuilder.loadTexts:
    uas7022FarEndIntervalTable.setStatus("mandatory")
_Uas7022FarEndIntervalEntry_Object = MibTableRow
uas7022FarEndIntervalEntry = _Uas7022FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 6, 1)
)
uas7022FarEndIntervalEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndIntervalIndex"),
    (0, "GDCUAS7022-MIB", "uas7022FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    uas7022FarEndIntervalEntry.setStatus("mandatory")
_Uas7022FarEndIntervalIndex_Type = SCinstance
_Uas7022FarEndIntervalIndex_Object = MibTableColumn
uas7022FarEndIntervalIndex = _Uas7022FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 6, 1, 1),
    _Uas7022FarEndIntervalIndex_Type()
)
uas7022FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndIntervalIndex.setStatus("mandatory")


class _Uas7022FarEndIntervalNumber_Type(Integer32):
    """Custom type uas7022FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7022FarEndIntervalNumber_Type.__name__ = "Integer32"
_Uas7022FarEndIntervalNumber_Object = MibTableColumn
uas7022FarEndIntervalNumber = _Uas7022FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 6, 1, 2),
    _Uas7022FarEndIntervalNumber_Type()
)
uas7022FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndIntervalNumber.setStatus("mandatory")


class _Uas7022FarEndIntervalStat_Type(OctetString):
    """Custom type uas7022FarEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Uas7022FarEndIntervalStat_Type.__name__ = "OctetString"
_Uas7022FarEndIntervalStat_Object = MibTableColumn
uas7022FarEndIntervalStat = _Uas7022FarEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 6, 1, 3),
    _Uas7022FarEndIntervalStat_Type()
)
uas7022FarEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndIntervalStat.setStatus("mandatory")
_Uas7022FarEndCurrent24HrTable_Object = MibTable
uas7022FarEndCurrent24HrTable = _Uas7022FarEndCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 7)
)
if mibBuilder.loadTexts:
    uas7022FarEndCurrent24HrTable.setStatus("mandatory")
_Uas7022FarEndCurrent24HrEntry_Object = MibTableRow
uas7022FarEndCurrent24HrEntry = _Uas7022FarEndCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 7, 1)
)
uas7022FarEndCurrent24HrEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndCurrent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7022FarEndCurrent24HrEntry.setStatus("mandatory")
_Uas7022FarEndCurrent24HrIndex_Type = SCinstance
_Uas7022FarEndCurrent24HrIndex_Object = MibTableColumn
uas7022FarEndCurrent24HrIndex = _Uas7022FarEndCurrent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 7, 1, 1),
    _Uas7022FarEndCurrent24HrIndex_Type()
)
uas7022FarEndCurrent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndCurrent24HrIndex.setStatus("mandatory")


class _Uas7022FarEndCurrent24HrStat_Type(OctetString):
    """Custom type uas7022FarEndCurrent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Uas7022FarEndCurrent24HrStat_Type.__name__ = "OctetString"
_Uas7022FarEndCurrent24HrStat_Object = MibTableColumn
uas7022FarEndCurrent24HrStat = _Uas7022FarEndCurrent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 7, 1, 2),
    _Uas7022FarEndCurrent24HrStat_Type()
)
uas7022FarEndCurrent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndCurrent24HrStat.setStatus("mandatory")
_Uas7022FarEndRecent24HrTable_Object = MibTable
uas7022FarEndRecent24HrTable = _Uas7022FarEndRecent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 8)
)
if mibBuilder.loadTexts:
    uas7022FarEndRecent24HrTable.setStatus("mandatory")
_Uas7022FarEndRecent24HrEntry_Object = MibTableRow
uas7022FarEndRecent24HrEntry = _Uas7022FarEndRecent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 8, 1)
)
uas7022FarEndRecent24HrEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndRecent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7022FarEndRecent24HrEntry.setStatus("mandatory")
_Uas7022FarEndRecent24HrIndex_Type = SCinstance
_Uas7022FarEndRecent24HrIndex_Object = MibTableColumn
uas7022FarEndRecent24HrIndex = _Uas7022FarEndRecent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 8, 1, 1),
    _Uas7022FarEndRecent24HrIndex_Type()
)
uas7022FarEndRecent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndRecent24HrIndex.setStatus("mandatory")


class _Uas7022FarEndRecent24HrStat_Type(OctetString):
    """Custom type uas7022FarEndRecent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Uas7022FarEndRecent24HrStat_Type.__name__ = "OctetString"
_Uas7022FarEndRecent24HrStat_Object = MibTableColumn
uas7022FarEndRecent24HrStat = _Uas7022FarEndRecent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 8, 1, 2),
    _Uas7022FarEndRecent24HrStat_Type()
)
uas7022FarEndRecent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndRecent24HrStat.setStatus("mandatory")
_Uas7022NearEndUnavailableTimeRegTable_Object = MibTable
uas7022NearEndUnavailableTimeRegTable = _Uas7022NearEndUnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9)
)
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegTable.setStatus("mandatory")
_Uas7022NearEndUnavailableTimeRegEntry_Object = MibTableRow
uas7022NearEndUnavailableTimeRegEntry = _Uas7022NearEndUnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9, 1)
)
uas7022NearEndUnavailableTimeRegEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndUnavailableTimeRegIndex"),
    (0, "GDCUAS7022-MIB", "uas7022NearEndUnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegEntry.setStatus("mandatory")
_Uas7022NearEndUnavailableTimeRegIndex_Type = SCinstance
_Uas7022NearEndUnavailableTimeRegIndex_Object = MibTableColumn
uas7022NearEndUnavailableTimeRegIndex = _Uas7022NearEndUnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9, 1, 1),
    _Uas7022NearEndUnavailableTimeRegIndex_Type()
)
uas7022NearEndUnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegIndex.setStatus("mandatory")


class _Uas7022NearEndUnavailableTimeRegNumber_Type(Integer32):
    """Custom type uas7022NearEndUnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Uas7022NearEndUnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Uas7022NearEndUnavailableTimeRegNumber_Object = MibTableColumn
uas7022NearEndUnavailableTimeRegNumber = _Uas7022NearEndUnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9, 1, 2),
    _Uas7022NearEndUnavailableTimeRegNumber_Type()
)
uas7022NearEndUnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegNumber.setStatus("mandatory")


class _Uas7022NearEndUnavailableTimeRegStart_Type(Integer32):
    """Custom type uas7022NearEndUnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022NearEndUnavailableTimeRegStart_Type.__name__ = "Integer32"
_Uas7022NearEndUnavailableTimeRegStart_Object = MibTableColumn
uas7022NearEndUnavailableTimeRegStart = _Uas7022NearEndUnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9, 1, 3),
    _Uas7022NearEndUnavailableTimeRegStart_Type()
)
uas7022NearEndUnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegStart.setStatus("mandatory")


class _Uas7022NearEndUnavailableTimeRegStop_Type(Integer32):
    """Custom type uas7022NearEndUnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022NearEndUnavailableTimeRegStop_Type.__name__ = "Integer32"
_Uas7022NearEndUnavailableTimeRegStop_Object = MibTableColumn
uas7022NearEndUnavailableTimeRegStop = _Uas7022NearEndUnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 9, 1, 4),
    _Uas7022NearEndUnavailableTimeRegStop_Type()
)
uas7022NearEndUnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndUnavailableTimeRegStop.setStatus("mandatory")
_Uas7022FarEndUnavailableTimeRegTable_Object = MibTable
uas7022FarEndUnavailableTimeRegTable = _Uas7022FarEndUnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10)
)
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegTable.setStatus("mandatory")
_Uas7022FarEndUnavailableTimeRegEntry_Object = MibTableRow
uas7022FarEndUnavailableTimeRegEntry = _Uas7022FarEndUnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10, 1)
)
uas7022FarEndUnavailableTimeRegEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndUnavailableTimeRegIndex"),
    (0, "GDCUAS7022-MIB", "uas7022FarEndUnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegEntry.setStatus("mandatory")
_Uas7022FarEndUnavailableTimeRegIndex_Type = SCinstance
_Uas7022FarEndUnavailableTimeRegIndex_Object = MibTableColumn
uas7022FarEndUnavailableTimeRegIndex = _Uas7022FarEndUnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10, 1, 1),
    _Uas7022FarEndUnavailableTimeRegIndex_Type()
)
uas7022FarEndUnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegIndex.setStatus("mandatory")


class _Uas7022FarEndUnavailableTimeRegNumber_Type(Integer32):
    """Custom type uas7022FarEndUnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Uas7022FarEndUnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Uas7022FarEndUnavailableTimeRegNumber_Object = MibTableColumn
uas7022FarEndUnavailableTimeRegNumber = _Uas7022FarEndUnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10, 1, 2),
    _Uas7022FarEndUnavailableTimeRegNumber_Type()
)
uas7022FarEndUnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegNumber.setStatus("mandatory")


class _Uas7022FarEndUnavailableTimeRegStart_Type(Integer32):
    """Custom type uas7022FarEndUnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022FarEndUnavailableTimeRegStart_Type.__name__ = "Integer32"
_Uas7022FarEndUnavailableTimeRegStart_Object = MibTableColumn
uas7022FarEndUnavailableTimeRegStart = _Uas7022FarEndUnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10, 1, 3),
    _Uas7022FarEndUnavailableTimeRegStart_Type()
)
uas7022FarEndUnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegStart.setStatus("mandatory")


class _Uas7022FarEndUnavailableTimeRegStop_Type(Integer32):
    """Custom type uas7022FarEndUnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7022FarEndUnavailableTimeRegStop_Type.__name__ = "Integer32"
_Uas7022FarEndUnavailableTimeRegStop_Object = MibTableColumn
uas7022FarEndUnavailableTimeRegStop = _Uas7022FarEndUnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 5, 10, 1, 4),
    _Uas7022FarEndUnavailableTimeRegStop_Type()
)
uas7022FarEndUnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndUnavailableTimeRegStop.setStatus("mandatory")
_Uas7022Alarms_ObjectIdentity = ObjectIdentity
uas7022Alarms = _Uas7022Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6)
)
_Uas7022NoResponseAlm_ObjectIdentity = ObjectIdentity
uas7022NoResponseAlm = _Uas7022NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 1)
)
_Uas7022DiagRxErrAlm_ObjectIdentity = ObjectIdentity
uas7022DiagRxErrAlm = _Uas7022DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 2)
)
_Uas7022PowerUpAlm_ObjectIdentity = ObjectIdentity
uas7022PowerUpAlm = _Uas7022PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 3)
)
_Uas7022TimingLoss_ObjectIdentity = ObjectIdentity
uas7022TimingLoss = _Uas7022TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 4)
)
_Uas7022LCV_ObjectIdentity = ObjectIdentity
uas7022LCV = _Uas7022LCV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 5)
)
_Uas7022LossOfSignal_ObjectIdentity = ObjectIdentity
uas7022LossOfSignal = _Uas7022LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 6)
)
_Uas7022LossOfFrame_ObjectIdentity = ObjectIdentity
uas7022LossOfFrame = _Uas7022LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 7)
)
_Uas7022AlarmIndSignal_ObjectIdentity = ObjectIdentity
uas7022AlarmIndSignal = _Uas7022AlarmIndSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 8)
)
_Uas7022NEES_ObjectIdentity = ObjectIdentity
uas7022NEES = _Uas7022NEES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 9)
)
_Uas7022NEBBE_ObjectIdentity = ObjectIdentity
uas7022NEBBE = _Uas7022NEBBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 10)
)
_Uas7022NESES_ObjectIdentity = ObjectIdentity
uas7022NESES = _Uas7022NESES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 11)
)
_Uas7022NEUAS_ObjectIdentity = ObjectIdentity
uas7022NEUAS = _Uas7022NEUAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 12)
)
_Uas7022FEES_ObjectIdentity = ObjectIdentity
uas7022FEES = _Uas7022FEES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 13)
)
_Uas7022FEBBE_ObjectIdentity = ObjectIdentity
uas7022FEBBE = _Uas7022FEBBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 14)
)
_Uas7022FESES_ObjectIdentity = ObjectIdentity
uas7022FESES = _Uas7022FESES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 15)
)
_Uas7022FEUAS_ObjectIdentity = ObjectIdentity
uas7022FEUAS = _Uas7022FEUAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 16)
)
_Uas7022RAI_ObjectIdentity = ObjectIdentity
uas7022RAI = _Uas7022RAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 6, 17)
)
_Uas7022AlarmConfig_ObjectIdentity = ObjectIdentity
uas7022AlarmConfig = _Uas7022AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7)
)
_Uas7022NearEndAlarmConfigTable_Object = MibTable
uas7022NearEndAlarmConfigTable = _Uas7022NearEndAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1)
)
if mibBuilder.loadTexts:
    uas7022NearEndAlarmConfigTable.setStatus("mandatory")
_Uas7022NearEndAlarmConfigEntry_Object = MibTableRow
uas7022NearEndAlarmConfigEntry = _Uas7022NearEndAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1, 1)
)
uas7022NearEndAlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022NearEndAlarmConfigIndex"),
    (0, "GDCUAS7022-MIB", "uas7022NearEndAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7022NearEndAlarmConfigEntry.setStatus("mandatory")
_Uas7022NearEndAlarmConfigIndex_Type = SCinstance
_Uas7022NearEndAlarmConfigIndex_Object = MibTableColumn
uas7022NearEndAlarmConfigIndex = _Uas7022NearEndAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1, 1, 1),
    _Uas7022NearEndAlarmConfigIndex_Type()
)
uas7022NearEndAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndAlarmConfigIndex.setStatus("mandatory")
_Uas7022NearEndAlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7022NearEndAlarmConfigIdentifier_Object = MibTableColumn
uas7022NearEndAlarmConfigIdentifier = _Uas7022NearEndAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1, 1, 2),
    _Uas7022NearEndAlarmConfigIdentifier_Type()
)
uas7022NearEndAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022NearEndAlarmConfigIdentifier.setStatus("mandatory")


class _Uas7022NearEndAlarmCountWindow_Type(Integer32):
    """Custom type uas7022NearEndAlarmCountWindow based on Integer32"""
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


_Uas7022NearEndAlarmCountWindow_Type.__name__ = "Integer32"
_Uas7022NearEndAlarmCountWindow_Object = MibTableColumn
uas7022NearEndAlarmCountWindow = _Uas7022NearEndAlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1, 1, 3),
    _Uas7022NearEndAlarmCountWindow_Type()
)
uas7022NearEndAlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NearEndAlarmCountWindow.setStatus("mandatory")


class _Uas7022NearEndAlarmCountThreshold_Type(Integer32):
    """Custom type uas7022NearEndAlarmCountThreshold based on Integer32"""
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


_Uas7022NearEndAlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7022NearEndAlarmCountThreshold_Object = MibTableColumn
uas7022NearEndAlarmCountThreshold = _Uas7022NearEndAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 1, 1, 4),
    _Uas7022NearEndAlarmCountThreshold_Type()
)
uas7022NearEndAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NearEndAlarmCountThreshold.setStatus("mandatory")
_Uas7022FarEndAlarmConfigTable_Object = MibTable
uas7022FarEndAlarmConfigTable = _Uas7022FarEndAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2)
)
if mibBuilder.loadTexts:
    uas7022FarEndAlarmConfigTable.setStatus("mandatory")
_Uas7022FarEndAlarmConfigEntry_Object = MibTableRow
uas7022FarEndAlarmConfigEntry = _Uas7022FarEndAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2, 1)
)
uas7022FarEndAlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022FarEndAlarmConfigIndex"),
    (0, "GDCUAS7022-MIB", "uas7022FarEndAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7022FarEndAlarmConfigEntry.setStatus("mandatory")
_Uas7022FarEndAlarmConfigIndex_Type = SCinstance
_Uas7022FarEndAlarmConfigIndex_Object = MibTableColumn
uas7022FarEndAlarmConfigIndex = _Uas7022FarEndAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2, 1, 1),
    _Uas7022FarEndAlarmConfigIndex_Type()
)
uas7022FarEndAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndAlarmConfigIndex.setStatus("mandatory")
_Uas7022FarEndAlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7022FarEndAlarmConfigIdentifier_Object = MibTableColumn
uas7022FarEndAlarmConfigIdentifier = _Uas7022FarEndAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2, 1, 2),
    _Uas7022FarEndAlarmConfigIdentifier_Type()
)
uas7022FarEndAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022FarEndAlarmConfigIdentifier.setStatus("mandatory")


class _Uas7022FarEndAlarmCountWindow_Type(Integer32):
    """Custom type uas7022FarEndAlarmCountWindow based on Integer32"""
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


_Uas7022FarEndAlarmCountWindow_Type.__name__ = "Integer32"
_Uas7022FarEndAlarmCountWindow_Object = MibTableColumn
uas7022FarEndAlarmCountWindow = _Uas7022FarEndAlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2, 1, 3),
    _Uas7022FarEndAlarmCountWindow_Type()
)
uas7022FarEndAlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022FarEndAlarmCountWindow.setStatus("mandatory")


class _Uas7022FarEndAlarmCountThreshold_Type(Integer32):
    """Custom type uas7022FarEndAlarmCountThreshold based on Integer32"""
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


_Uas7022FarEndAlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7022FarEndAlarmCountThreshold_Object = MibTableColumn
uas7022FarEndAlarmCountThreshold = _Uas7022FarEndAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 2, 1, 4),
    _Uas7022FarEndAlarmCountThreshold_Type()
)
uas7022FarEndAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022FarEndAlarmCountThreshold.setStatus("mandatory")
_Uas7022LocalAlarmConfigTable_Object = MibTable
uas7022LocalAlarmConfigTable = _Uas7022LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3)
)
if mibBuilder.loadTexts:
    uas7022LocalAlarmConfigTable.setStatus("mandatory")
_Uas7022LocalAlarmConfigEntry_Object = MibTableRow
uas7022LocalAlarmConfigEntry = _Uas7022LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1)
)
uas7022LocalAlarmConfigEntry.setIndexNames(
    (0, "GDCUAS7022-MIB", "uas7022LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7022LocalAlarmConfigEntry.setStatus("mandatory")
_Uas7022LocalAlarmConfigIndex_Type = SCinstance
_Uas7022LocalAlarmConfigIndex_Object = MibTableColumn
uas7022LocalAlarmConfigIndex = _Uas7022LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 1),
    _Uas7022LocalAlarmConfigIndex_Type()
)
uas7022LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7022LocalAlarmConfigIndex.setStatus("mandatory")


class _Uas7022UASNE_Type(Integer32):
    """Custom type uas7022UASNE based on Integer32"""
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


_Uas7022UASNE_Type.__name__ = "Integer32"
_Uas7022UASNE_Object = MibTableColumn
uas7022UASNE = _Uas7022UASNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 2),
    _Uas7022UASNE_Type()
)
uas7022UASNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022UASNE.setStatus("mandatory")


class _Uas7022SESNE_Type(Integer32):
    """Custom type uas7022SESNE based on Integer32"""
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


_Uas7022SESNE_Type.__name__ = "Integer32"
_Uas7022SESNE_Object = MibTableColumn
uas7022SESNE = _Uas7022SESNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 3),
    _Uas7022SESNE_Type()
)
uas7022SESNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022SESNE.setStatus("mandatory")


class _Uas7022BBENE_Type(Integer32):
    """Custom type uas7022BBENE based on Integer32"""
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


_Uas7022BBENE_Type.__name__ = "Integer32"
_Uas7022BBENE_Object = MibTableColumn
uas7022BBENE = _Uas7022BBENE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 4),
    _Uas7022BBENE_Type()
)
uas7022BBENE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022BBENE.setStatus("mandatory")


class _Uas7022ESNE_Type(Integer32):
    """Custom type uas7022ESNE based on Integer32"""
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


_Uas7022ESNE_Type.__name__ = "Integer32"
_Uas7022ESNE_Object = MibTableColumn
uas7022ESNE = _Uas7022ESNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 5),
    _Uas7022ESNE_Type()
)
uas7022ESNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022ESNE.setStatus("mandatory")


class _Uas7022UASFE_Type(Integer32):
    """Custom type uas7022UASFE based on Integer32"""
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


_Uas7022UASFE_Type.__name__ = "Integer32"
_Uas7022UASFE_Object = MibTableColumn
uas7022UASFE = _Uas7022UASFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 6),
    _Uas7022UASFE_Type()
)
uas7022UASFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022UASFE.setStatus("mandatory")


class _Uas7022SESFE_Type(Integer32):
    """Custom type uas7022SESFE based on Integer32"""
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


_Uas7022SESFE_Type.__name__ = "Integer32"
_Uas7022SESFE_Object = MibTableColumn
uas7022SESFE = _Uas7022SESFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 7),
    _Uas7022SESFE_Type()
)
uas7022SESFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022SESFE.setStatus("mandatory")


class _Uas7022BBEFE_Type(Integer32):
    """Custom type uas7022BBEFE based on Integer32"""
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


_Uas7022BBEFE_Type.__name__ = "Integer32"
_Uas7022BBEFE_Object = MibTableColumn
uas7022BBEFE = _Uas7022BBEFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 8),
    _Uas7022BBEFE_Type()
)
uas7022BBEFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022BBEFE.setStatus("mandatory")


class _Uas7022ESFE_Type(Integer32):
    """Custom type uas7022ESFE based on Integer32"""
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


_Uas7022ESFE_Type.__name__ = "Integer32"
_Uas7022ESFE_Object = MibTableColumn
uas7022ESFE = _Uas7022ESFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 9),
    _Uas7022ESFE_Type()
)
uas7022ESFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022ESFE.setStatus("mandatory")


class _Uas7022LOS_Type(Integer32):
    """Custom type uas7022LOS based on Integer32"""
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


_Uas7022LOS_Type.__name__ = "Integer32"
_Uas7022LOS_Object = MibTableColumn
uas7022LOS = _Uas7022LOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 10),
    _Uas7022LOS_Type()
)
uas7022LOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022LOS.setStatus("mandatory")


class _Uas7022LOF_Type(Integer32):
    """Custom type uas7022LOF based on Integer32"""
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


_Uas7022LOF_Type.__name__ = "Integer32"
_Uas7022LOF_Object = MibTableColumn
uas7022LOF = _Uas7022LOF_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 11),
    _Uas7022LOF_Type()
)
uas7022LOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022LOF.setStatus("mandatory")


class _Uas7022AIS_Type(Integer32):
    """Custom type uas7022AIS based on Integer32"""
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


_Uas7022AIS_Type.__name__ = "Integer32"
_Uas7022AIS_Object = MibTableColumn
uas7022AIS = _Uas7022AIS_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 12),
    _Uas7022AIS_Type()
)
uas7022AIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022AIS.setStatus("mandatory")


class _Uas7022TmgLoss_Type(Integer32):
    """Custom type uas7022TmgLoss based on Integer32"""
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


_Uas7022TmgLoss_Type.__name__ = "Integer32"
_Uas7022TmgLoss_Object = MibTableColumn
uas7022TmgLoss = _Uas7022TmgLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 13),
    _Uas7022TmgLoss_Type()
)
uas7022TmgLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022TmgLoss.setStatus("mandatory")


class _Uas7022LCVs_Type(Integer32):
    """Custom type uas7022LCVs based on Integer32"""
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


_Uas7022LCVs_Type.__name__ = "Integer32"
_Uas7022LCVs_Object = MibTableColumn
uas7022LCVs = _Uas7022LCVs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 14),
    _Uas7022LCVs_Type()
)
uas7022LCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022LCVs.setStatus("mandatory")


class _Uas7022NtwkRAI_Type(Integer32):
    """Custom type uas7022NtwkRAI based on Integer32"""
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


_Uas7022NtwkRAI_Type.__name__ = "Integer32"
_Uas7022NtwkRAI_Object = MibTableColumn
uas7022NtwkRAI = _Uas7022NtwkRAI_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 13, 7, 3, 1, 15),
    _Uas7022NtwkRAI_Type()
)
uas7022NtwkRAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7022NtwkRAI.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCUAS7022-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "uas7022": uas7022,
       "uas7022Version": uas7022Version,
       "uas7022MIBversion": uas7022MIBversion,
       "uas7022VersionTable": uas7022VersionTable,
       "uas7022VersionEntry": uas7022VersionEntry,
       "uas7022VersionIndex": uas7022VersionIndex,
       "uas7022ActiveFirmwareRev": uas7022ActiveFirmwareRev,
       "uas7022StoredFirmwareRev": uas7022StoredFirmwareRev,
       "uas7022StoredFirmwareStatus": uas7022StoredFirmwareStatus,
       "uas7022SwitchActiveFirmware": uas7022SwitchActiveFirmware,
       "uas7022DownloadingMode": uas7022DownloadingMode,
       "uas7022Maintenance": uas7022Maintenance,
       "uas7022MaintenanceTable": uas7022MaintenanceTable,
       "uas7022MaintenanceEntry": uas7022MaintenanceEntry,
       "uas7022MaintenanceLineIndex": uas7022MaintenanceLineIndex,
       "uas7022SoftReset": uas7022SoftReset,
       "uas7022SysUpTime": uas7022SysUpTime,
       "uas7022DefaultInit": uas7022DefaultInit,
       "uas7022LedStatus": uas7022LedStatus,
       "uas7022AlarmStatus": uas7022AlarmStatus,
       "uas7022NearEndResetStats": uas7022NearEndResetStats,
       "uas7022FarEndResetStats": uas7022FarEndResetStats,
       "uas7022NearEndStatLastInit": uas7022NearEndStatLastInit,
       "uas7022FarEndStatLastInit": uas7022FarEndStatLastInit,
       "uas7022NearEndValidIntervals": uas7022NearEndValidIntervals,
       "uas7022FarEndValidIntervals": uas7022FarEndValidIntervals,
       "uas7022NIUaCircuitID": uas7022NIUaCircuitID,
       "uas7022SystemTimingGenStatus": uas7022SystemTimingGenStatus,
       "uas7022NIUbCircuitID": uas7022NIUbCircuitID,
       "uas7022Configuration": uas7022Configuration,
       "uas7022ConfigTable": uas7022ConfigTable,
       "uas7022ConfigEntry": uas7022ConfigEntry,
       "uas7022ConfigIndex": uas7022ConfigIndex,
       "uas7022RcvrRange": uas7022RcvrRange,
       "uas7022Framing": uas7022Framing,
       "uas7022SysTimingGen": uas7022SysTimingGen,
       "uas7022Highway": uas7022Highway,
       "uas7022TransmitClockSource": uas7022TransmitClockSource,
       "uas7022FallbackClockSource": uas7022FallbackClockSource,
       "uas7022InterfaceType": uas7022InterfaceType,
       "uas7022FDLMode": uas7022FDLMode,
       "uas7022TimeSlot16Content": uas7022TimeSlot16Content,
       "uas7022Impedance": uas7022Impedance,
       "uas7022Diagnostics": uas7022Diagnostics,
       "uas7022DiagTable": uas7022DiagTable,
       "uas7022DiagEntry": uas7022DiagEntry,
       "uas7022DiagIndex": uas7022DiagIndex,
       "uas7022DiagConfig": uas7022DiagConfig,
       "uas7022TestLimit": uas7022TestLimit,
       "uas7022TestExecutionStatus": uas7022TestExecutionStatus,
       "uas7022TestExceptions": uas7022TestExceptions,
       "uas7022Performance": uas7022Performance,
       "uas7022NearEndCurrent15MinTable": uas7022NearEndCurrent15MinTable,
       "uas7022NearEndCurrent15MinEntry": uas7022NearEndCurrent15MinEntry,
       "uas7022NearEndCurrent15MinIndex": uas7022NearEndCurrent15MinIndex,
       "uas7022NearEndCurrent15MinStat": uas7022NearEndCurrent15MinStat,
       "uas7022NearEndIntervalTable": uas7022NearEndIntervalTable,
       "uas7022NearEndIntervalEntry": uas7022NearEndIntervalEntry,
       "uas7022NearEndIntervalIndex": uas7022NearEndIntervalIndex,
       "uas7022NearEndIntervalNumber": uas7022NearEndIntervalNumber,
       "uas7022NearEndIntervalStat": uas7022NearEndIntervalStat,
       "uas7022NearEndCurrent24HrTable": uas7022NearEndCurrent24HrTable,
       "uas7022NearEndCurrent24HrEntry": uas7022NearEndCurrent24HrEntry,
       "uas7022NearEndCurrent24HrIndex": uas7022NearEndCurrent24HrIndex,
       "uas7022NearEndCurrent24HrStat": uas7022NearEndCurrent24HrStat,
       "uas7022NearEndRecent24HrTable": uas7022NearEndRecent24HrTable,
       "uas7022NearEndRecent24HrEntry": uas7022NearEndRecent24HrEntry,
       "uas7022NearEndRecent24HrIndex": uas7022NearEndRecent24HrIndex,
       "uas7022NearEndRecent24HrStat": uas7022NearEndRecent24HrStat,
       "uas7022FarEndCurrent15MinTable": uas7022FarEndCurrent15MinTable,
       "uas7022FarEndCurrent15MinEntry": uas7022FarEndCurrent15MinEntry,
       "uas7022FarEndCurrent15MinIndex": uas7022FarEndCurrent15MinIndex,
       "uas7022FarEndCurrent15MinStat": uas7022FarEndCurrent15MinStat,
       "uas7022FarEndIntervalTable": uas7022FarEndIntervalTable,
       "uas7022FarEndIntervalEntry": uas7022FarEndIntervalEntry,
       "uas7022FarEndIntervalIndex": uas7022FarEndIntervalIndex,
       "uas7022FarEndIntervalNumber": uas7022FarEndIntervalNumber,
       "uas7022FarEndIntervalStat": uas7022FarEndIntervalStat,
       "uas7022FarEndCurrent24HrTable": uas7022FarEndCurrent24HrTable,
       "uas7022FarEndCurrent24HrEntry": uas7022FarEndCurrent24HrEntry,
       "uas7022FarEndCurrent24HrIndex": uas7022FarEndCurrent24HrIndex,
       "uas7022FarEndCurrent24HrStat": uas7022FarEndCurrent24HrStat,
       "uas7022FarEndRecent24HrTable": uas7022FarEndRecent24HrTable,
       "uas7022FarEndRecent24HrEntry": uas7022FarEndRecent24HrEntry,
       "uas7022FarEndRecent24HrIndex": uas7022FarEndRecent24HrIndex,
       "uas7022FarEndRecent24HrStat": uas7022FarEndRecent24HrStat,
       "uas7022NearEndUnavailableTimeRegTable": uas7022NearEndUnavailableTimeRegTable,
       "uas7022NearEndUnavailableTimeRegEntry": uas7022NearEndUnavailableTimeRegEntry,
       "uas7022NearEndUnavailableTimeRegIndex": uas7022NearEndUnavailableTimeRegIndex,
       "uas7022NearEndUnavailableTimeRegNumber": uas7022NearEndUnavailableTimeRegNumber,
       "uas7022NearEndUnavailableTimeRegStart": uas7022NearEndUnavailableTimeRegStart,
       "uas7022NearEndUnavailableTimeRegStop": uas7022NearEndUnavailableTimeRegStop,
       "uas7022FarEndUnavailableTimeRegTable": uas7022FarEndUnavailableTimeRegTable,
       "uas7022FarEndUnavailableTimeRegEntry": uas7022FarEndUnavailableTimeRegEntry,
       "uas7022FarEndUnavailableTimeRegIndex": uas7022FarEndUnavailableTimeRegIndex,
       "uas7022FarEndUnavailableTimeRegNumber": uas7022FarEndUnavailableTimeRegNumber,
       "uas7022FarEndUnavailableTimeRegStart": uas7022FarEndUnavailableTimeRegStart,
       "uas7022FarEndUnavailableTimeRegStop": uas7022FarEndUnavailableTimeRegStop,
       "uas7022Alarms": uas7022Alarms,
       "uas7022NoResponseAlm": uas7022NoResponseAlm,
       "uas7022DiagRxErrAlm": uas7022DiagRxErrAlm,
       "uas7022PowerUpAlm": uas7022PowerUpAlm,
       "uas7022TimingLoss": uas7022TimingLoss,
       "uas7022LCV": uas7022LCV,
       "uas7022LossOfSignal": uas7022LossOfSignal,
       "uas7022LossOfFrame": uas7022LossOfFrame,
       "uas7022AlarmIndSignal": uas7022AlarmIndSignal,
       "uas7022NEES": uas7022NEES,
       "uas7022NEBBE": uas7022NEBBE,
       "uas7022NESES": uas7022NESES,
       "uas7022NEUAS": uas7022NEUAS,
       "uas7022FEES": uas7022FEES,
       "uas7022FEBBE": uas7022FEBBE,
       "uas7022FESES": uas7022FESES,
       "uas7022FEUAS": uas7022FEUAS,
       "uas7022RAI": uas7022RAI,
       "uas7022AlarmConfig": uas7022AlarmConfig,
       "uas7022NearEndAlarmConfigTable": uas7022NearEndAlarmConfigTable,
       "uas7022NearEndAlarmConfigEntry": uas7022NearEndAlarmConfigEntry,
       "uas7022NearEndAlarmConfigIndex": uas7022NearEndAlarmConfigIndex,
       "uas7022NearEndAlarmConfigIdentifier": uas7022NearEndAlarmConfigIdentifier,
       "uas7022NearEndAlarmCountWindow": uas7022NearEndAlarmCountWindow,
       "uas7022NearEndAlarmCountThreshold": uas7022NearEndAlarmCountThreshold,
       "uas7022FarEndAlarmConfigTable": uas7022FarEndAlarmConfigTable,
       "uas7022FarEndAlarmConfigEntry": uas7022FarEndAlarmConfigEntry,
       "uas7022FarEndAlarmConfigIndex": uas7022FarEndAlarmConfigIndex,
       "uas7022FarEndAlarmConfigIdentifier": uas7022FarEndAlarmConfigIdentifier,
       "uas7022FarEndAlarmCountWindow": uas7022FarEndAlarmCountWindow,
       "uas7022FarEndAlarmCountThreshold": uas7022FarEndAlarmCountThreshold,
       "uas7022LocalAlarmConfigTable": uas7022LocalAlarmConfigTable,
       "uas7022LocalAlarmConfigEntry": uas7022LocalAlarmConfigEntry,
       "uas7022LocalAlarmConfigIndex": uas7022LocalAlarmConfigIndex,
       "uas7022UASNE": uas7022UASNE,
       "uas7022SESNE": uas7022SESNE,
       "uas7022BBENE": uas7022BBENE,
       "uas7022ESNE": uas7022ESNE,
       "uas7022UASFE": uas7022UASFE,
       "uas7022SESFE": uas7022SESFE,
       "uas7022BBEFE": uas7022BBEFE,
       "uas7022ESFE": uas7022ESFE,
       "uas7022LOS": uas7022LOS,
       "uas7022LOF": uas7022LOF,
       "uas7022AIS": uas7022AIS,
       "uas7022TmgLoss": uas7022TmgLoss,
       "uas7022LCVs": uas7022LCVs,
       "uas7022NtwkRAI": uas7022NtwkRAI}
)
