# SNMP MIB module (GDCDSX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCDSX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:14 2024
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
_GdcDsx1System_ObjectIdentity = ObjectIdentity
gdcDsx1System = _GdcDsx1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1)
)
_GdcDsx1Version_ObjectIdentity = ObjectIdentity
gdcDsx1Version = _GdcDsx1Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1)
)


class _GdcDsx1SystemMIBversion_Type(DisplayString):
    """Custom type gdcDsx1SystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcDsx1SystemMIBversion_Type.__name__ = "DisplayString"
_GdcDsx1SystemMIBversion_Object = MibScalar
gdcDsx1SystemMIBversion = _GdcDsx1SystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 1),
    _GdcDsx1SystemMIBversion_Type()
)
gdcDsx1SystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1SystemMIBversion.setStatus("mandatory")
_GdcDsx1VersionTable_Object = MibTable
gdcDsx1VersionTable = _GdcDsx1VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gdcDsx1VersionTable.setStatus("mandatory")
_GdcDsx1VersionEntry_Object = MibTableRow
gdcDsx1VersionEntry = _GdcDsx1VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1)
)
gdcDsx1VersionEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1VersionIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1VersionEntry.setStatus("mandatory")
_GdcDsx1VersionIndex_Type = SCinstance
_GdcDsx1VersionIndex_Object = MibTableColumn
gdcDsx1VersionIndex = _GdcDsx1VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 1),
    _GdcDsx1VersionIndex_Type()
)
gdcDsx1VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1VersionIndex.setStatus("mandatory")


class _GdcDsx1FirmwareRev_Type(DisplayString):
    """Custom type gdcDsx1FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GdcDsx1FirmwareRev_Type.__name__ = "DisplayString"
_GdcDsx1FirmwareRev_Object = MibTableColumn
gdcDsx1FirmwareRev = _GdcDsx1FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 2),
    _GdcDsx1FirmwareRev_Type()
)
gdcDsx1FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1FirmwareRev.setStatus("mandatory")


class _GdcDsx1ModelNumber_Type(DisplayString):
    """Custom type gdcDsx1ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GdcDsx1ModelNumber_Type.__name__ = "DisplayString"
_GdcDsx1ModelNumber_Object = MibTableColumn
gdcDsx1ModelNumber = _GdcDsx1ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 3),
    _GdcDsx1ModelNumber_Type()
)
gdcDsx1ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ModelNumber.setStatus("mandatory")


class _GdcDsx1ActiveFirmwareRev_Type(DisplayString):
    """Custom type gdcDsx1ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GdcDsx1ActiveFirmwareRev_Type.__name__ = "DisplayString"
_GdcDsx1ActiveFirmwareRev_Object = MibTableColumn
gdcDsx1ActiveFirmwareRev = _GdcDsx1ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 4),
    _GdcDsx1ActiveFirmwareRev_Type()
)
gdcDsx1ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ActiveFirmwareRev.setStatus("mandatory")


class _GdcDsx1StoredFirmwareRev_Type(DisplayString):
    """Custom type gdcDsx1StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GdcDsx1StoredFirmwareRev_Type.__name__ = "DisplayString"
_GdcDsx1StoredFirmwareRev_Object = MibTableColumn
gdcDsx1StoredFirmwareRev = _GdcDsx1StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 5),
    _GdcDsx1StoredFirmwareRev_Type()
)
gdcDsx1StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1StoredFirmwareRev.setStatus("mandatory")


class _GdcDsx1BootRev_Type(DisplayString):
    """Custom type gdcDsx1BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GdcDsx1BootRev_Type.__name__ = "DisplayString"
_GdcDsx1BootRev_Object = MibTableColumn
gdcDsx1BootRev = _GdcDsx1BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 6),
    _GdcDsx1BootRev_Type()
)
gdcDsx1BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1BootRev.setStatus("mandatory")


class _GdcDsx1StoredFirmwareStatus_Type(Integer32):
    """Custom type gdcDsx1StoredFirmwareStatus based on Integer32"""
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
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_GdcDsx1StoredFirmwareStatus_Type.__name__ = "Integer32"
_GdcDsx1StoredFirmwareStatus_Object = MibTableColumn
gdcDsx1StoredFirmwareStatus = _GdcDsx1StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 7),
    _GdcDsx1StoredFirmwareStatus_Type()
)
gdcDsx1StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1StoredFirmwareStatus.setStatus("mandatory")


class _GdcDsx1SwitchActiveFirmware_Type(Integer32):
    """Custom type gdcDsx1SwitchActiveFirmware based on Integer32"""
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


_GdcDsx1SwitchActiveFirmware_Type.__name__ = "Integer32"
_GdcDsx1SwitchActiveFirmware_Object = MibTableColumn
gdcDsx1SwitchActiveFirmware = _GdcDsx1SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 8),
    _GdcDsx1SwitchActiveFirmware_Type()
)
gdcDsx1SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1SwitchActiveFirmware.setStatus("mandatory")


class _GdcDsx1DownloadingMode_Type(Integer32):
    """Custom type gdcDsx1DownloadingMode based on Integer32"""
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


_GdcDsx1DownloadingMode_Type.__name__ = "Integer32"
_GdcDsx1DownloadingMode_Object = MibTableColumn
gdcDsx1DownloadingMode = _GdcDsx1DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 1, 2, 1, 9),
    _GdcDsx1DownloadingMode_Type()
)
gdcDsx1DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1DownloadingMode.setStatus("mandatory")
_GdcDsx1Maintenance_ObjectIdentity = ObjectIdentity
gdcDsx1Maintenance = _GdcDsx1Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2)
)
_GdcDsx1MaintenanceTable_Object = MibTable
gdcDsx1MaintenanceTable = _GdcDsx1MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1MaintenanceTable.setStatus("mandatory")
_GdcDsx1MaintenanceEntry_Object = MibTableRow
gdcDsx1MaintenanceEntry = _GdcDsx1MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1)
)
gdcDsx1MaintenanceEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1MaintenanceEntry.setStatus("mandatory")
_GdcDsx1MaintenanceLineIndex_Type = SCinstance
_GdcDsx1MaintenanceLineIndex_Object = MibTableColumn
gdcDsx1MaintenanceLineIndex = _GdcDsx1MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 1),
    _GdcDsx1MaintenanceLineIndex_Type()
)
gdcDsx1MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1MaintenanceLineIndex.setStatus("mandatory")


class _GdcDsx1SoftReset_Type(Integer32):
    """Custom type gdcDsx1SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_GdcDsx1SoftReset_Type.__name__ = "Integer32"
_GdcDsx1SoftReset_Object = MibTableColumn
gdcDsx1SoftReset = _GdcDsx1SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 2),
    _GdcDsx1SoftReset_Type()
)
gdcDsx1SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1SoftReset.setStatus("mandatory")


class _GdcDsx1ConfigMode_Type(Integer32):
    """Custom type gdcDsx1ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2))
    )


_GdcDsx1ConfigMode_Type.__name__ = "Integer32"
_GdcDsx1ConfigMode_Object = MibTableColumn
gdcDsx1ConfigMode = _GdcDsx1ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 4),
    _GdcDsx1ConfigMode_Type()
)
gdcDsx1ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ConfigMode.setStatus("mandatory")


class _GdcDsx1FrontPanel_Type(Integer32):
    """Custom type gdcDsx1FrontPanel based on Integer32"""
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


_GdcDsx1FrontPanel_Type.__name__ = "Integer32"
_GdcDsx1FrontPanel_Object = MibTableColumn
gdcDsx1FrontPanel = _GdcDsx1FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 5),
    _GdcDsx1FrontPanel_Type()
)
gdcDsx1FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1FrontPanel.setStatus("mandatory")
_GdcDsx1SysUpTime_Type = TimeTicks
_GdcDsx1SysUpTime_Object = MibTableColumn
gdcDsx1SysUpTime = _GdcDsx1SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 6),
    _GdcDsx1SysUpTime_Type()
)
gdcDsx1SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1SysUpTime.setStatus("mandatory")


class _GdcDsx1DefaultInit_Type(Integer32):
    """Custom type gdcDsx1DefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 1),
          ("normal", 2))
    )


_GdcDsx1DefaultInit_Type.__name__ = "Integer32"
_GdcDsx1DefaultInit_Object = MibTableColumn
gdcDsx1DefaultInit = _GdcDsx1DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 7),
    _GdcDsx1DefaultInit_Type()
)
gdcDsx1DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1DefaultInit.setStatus("mandatory")


class _GdcDsx1ResetStats_Type(Integer32):
    """Custom type gdcDsx1ResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 9))
    )


_GdcDsx1ResetStats_Type.__name__ = "Integer32"
_GdcDsx1ResetStats_Object = MibTableColumn
gdcDsx1ResetStats = _GdcDsx1ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 8),
    _GdcDsx1ResetStats_Type()
)
gdcDsx1ResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1ResetStats.setStatus("mandatory")


class _GdcDsx1LedStatus_Type(OctetString):
    """Custom type gdcDsx1LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GdcDsx1LedStatus_Type.__name__ = "OctetString"
_GdcDsx1LedStatus_Object = MibTableColumn
gdcDsx1LedStatus = _GdcDsx1LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 9),
    _GdcDsx1LedStatus_Type()
)
gdcDsx1LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1LedStatus.setStatus("mandatory")


class _GdcDsx1SetTransmitClkSrc_Type(Integer32):
    """Custom type gdcDsx1SetTransmitClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallBackClkSrc", 2),
          ("txClkSrc", 1))
    )


_GdcDsx1SetTransmitClkSrc_Type.__name__ = "Integer32"
_GdcDsx1SetTransmitClkSrc_Object = MibTableColumn
gdcDsx1SetTransmitClkSrc = _GdcDsx1SetTransmitClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 10),
    _GdcDsx1SetTransmitClkSrc_Type()
)
gdcDsx1SetTransmitClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1SetTransmitClkSrc.setStatus("mandatory")


class _GdcDsx1CsuMode_Type(Integer32):
    """Custom type gdcDsx1CsuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concentratorMode", 2),
          ("csuMode", 1))
    )


_GdcDsx1CsuMode_Type.__name__ = "Integer32"
_GdcDsx1CsuMode_Object = MibTableColumn
gdcDsx1CsuMode = _GdcDsx1CsuMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 11),
    _GdcDsx1CsuMode_Type()
)
gdcDsx1CsuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1CsuMode.setStatus("mandatory")


class _GdcDsx1CircuitIdentifier1_Type(DisplayString):
    """Custom type gdcDsx1CircuitIdentifier1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcDsx1CircuitIdentifier1_Type.__name__ = "DisplayString"
_GdcDsx1CircuitIdentifier1_Object = MibTableColumn
gdcDsx1CircuitIdentifier1 = _GdcDsx1CircuitIdentifier1_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 12),
    _GdcDsx1CircuitIdentifier1_Type()
)
gdcDsx1CircuitIdentifier1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1CircuitIdentifier1.setStatus("mandatory")


class _GdcDsx1CircuitIdentifier2_Type(DisplayString):
    """Custom type gdcDsx1CircuitIdentifier2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcDsx1CircuitIdentifier2_Type.__name__ = "DisplayString"
_GdcDsx1CircuitIdentifier2_Object = MibTableColumn
gdcDsx1CircuitIdentifier2 = _GdcDsx1CircuitIdentifier2_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 2, 1, 1, 13),
    _GdcDsx1CircuitIdentifier2_Type()
)
gdcDsx1CircuitIdentifier2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1CircuitIdentifier2.setStatus("mandatory")
_GdcDsx1Configuration_ObjectIdentity = ObjectIdentity
gdcDsx1Configuration = _GdcDsx1Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3)
)
_GdcDsx1ConfigTable_Object = MibTable
gdcDsx1ConfigTable = _GdcDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1ConfigTable.setStatus("mandatory")
_GdcDsx1ConfigEntry_Object = MibTableRow
gdcDsx1ConfigEntry = _GdcDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1)
)
gdcDsx1ConfigEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1ConfigIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1ConfigEntry.setStatus("mandatory")
_GdcDsx1ConfigIndex_Type = SCinstance
_GdcDsx1ConfigIndex_Object = MibTableColumn
gdcDsx1ConfigIndex = _GdcDsx1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 1),
    _GdcDsx1ConfigIndex_Type()
)
gdcDsx1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ConfigIndex.setStatus("mandatory")


class _GdcDsx1LineType_Type(Integer32):
    """Custom type gdcDsx1LineType based on Integer32"""
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
        *(("auto", 1),
          ("manD4", 3),
          ("manEsf", 2),
          ("unframed", 4))
    )


_GdcDsx1LineType_Type.__name__ = "Integer32"
_GdcDsx1LineType_Object = MibTableColumn
gdcDsx1LineType = _GdcDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 2),
    _GdcDsx1LineType_Type()
)
gdcDsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1LineType.setStatus("mandatory")


class _GdcDsx1InterfaceType_Type(Integer32):
    """Custom type gdcDsx1InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 2),
          ("dsx1", 3),
          ("other", 1))
    )


_GdcDsx1InterfaceType_Type.__name__ = "Integer32"
_GdcDsx1InterfaceType_Object = MibTableColumn
gdcDsx1InterfaceType = _GdcDsx1InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 3),
    _GdcDsx1InterfaceType_Type()
)
gdcDsx1InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1InterfaceType.setStatus("mandatory")


class _GdcDsx1Preequalization_Type(Integer32):
    """Custom type gdcDsx1Preequalization based on Integer32"""
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
        *(("none", 7),
          ("other", 1),
          ("preeq130", 2),
          ("preeq260", 3),
          ("preeq390", 4),
          ("preeq530", 5),
          ("preeq655", 6))
    )


_GdcDsx1Preequalization_Type.__name__ = "Integer32"
_GdcDsx1Preequalization_Object = MibTableColumn
gdcDsx1Preequalization = _GdcDsx1Preequalization_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 4),
    _GdcDsx1Preequalization_Type()
)
gdcDsx1Preequalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1Preequalization.setStatus("mandatory")


class _GdcDsx1AdminLineBuildout_Type(Integer32):
    """Custom type gdcDsx1AdminLineBuildout based on Integer32"""
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
        *(("auto", 1),
          ("man00dB", 2),
          ("man150dB", 4),
          ("man75dB", 3))
    )


_GdcDsx1AdminLineBuildout_Type.__name__ = "Integer32"
_GdcDsx1AdminLineBuildout_Object = MibTableColumn
gdcDsx1AdminLineBuildout = _GdcDsx1AdminLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 5),
    _GdcDsx1AdminLineBuildout_Type()
)
gdcDsx1AdminLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1AdminLineBuildout.setStatus("mandatory")


class _GdcDsx1OperLineBuildout_Type(Integer32):
    """Custom type gdcDsx1OperLineBuildout based on Integer32"""
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
        *(("inProcess", 1),
          ("tx00dB", 2),
          ("tx150dB", 4),
          ("tx75dB", 3))
    )


_GdcDsx1OperLineBuildout_Type.__name__ = "Integer32"
_GdcDsx1OperLineBuildout_Object = MibTableColumn
gdcDsx1OperLineBuildout = _GdcDsx1OperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 6),
    _GdcDsx1OperLineBuildout_Type()
)
gdcDsx1OperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1OperLineBuildout.setStatus("mandatory")


class _GdcDsx1AdminRcvRange_Type(Integer32):
    """Custom type gdcDsx1AdminRcvRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manExt", 3),
          ("manNorm", 2))
    )


_GdcDsx1AdminRcvRange_Type.__name__ = "Integer32"
_GdcDsx1AdminRcvRange_Object = MibTableColumn
gdcDsx1AdminRcvRange = _GdcDsx1AdminRcvRange_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 7),
    _GdcDsx1AdminRcvRange_Type()
)
gdcDsx1AdminRcvRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1AdminRcvRange.setStatus("mandatory")


class _GdcDsx1OperRcvRange_Type(Integer32):
    """Custom type gdcDsx1OperRcvRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ext", 3),
          ("inProcess", 1),
          ("norm", 2))
    )


_GdcDsx1OperRcvRange_Type.__name__ = "Integer32"
_GdcDsx1OperRcvRange_Object = MibTableColumn
gdcDsx1OperRcvRange = _GdcDsx1OperRcvRange_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 8),
    _GdcDsx1OperRcvRange_Type()
)
gdcDsx1OperRcvRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1OperRcvRange.setStatus("mandatory")


class _GdcDsx1OnesDensity_Type(Integer32):
    """Custom type gdcDsx1OnesDensity based on Integer32"""
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
        *(("inhibit", 1),
          ("max15zeros", 2),
          ("max39zeros", 3),
          ("min1in8", 5),
          ("restrict8XNplus1", 4))
    )


_GdcDsx1OnesDensity_Type.__name__ = "Integer32"
_GdcDsx1OnesDensity_Object = MibTableColumn
gdcDsx1OnesDensity = _GdcDsx1OnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 9),
    _GdcDsx1OnesDensity_Type()
)
gdcDsx1OnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1OnesDensity.setStatus("mandatory")


class _GdcDsx1TransmitClockSource_Type(Integer32):
    """Custom type gdcDsx1TransmitClockSource based on Integer32"""
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
        *(("cascade", 3),
          ("channel", 4),
          ("composite", 5),
          ("other", 1),
          ("shelf", 6),
          ("station", 2))
    )


_GdcDsx1TransmitClockSource_Type.__name__ = "Integer32"
_GdcDsx1TransmitClockSource_Object = MibTableColumn
gdcDsx1TransmitClockSource = _GdcDsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 10),
    _GdcDsx1TransmitClockSource_Type()
)
gdcDsx1TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1TransmitClockSource.setStatus("mandatory")


class _GdcDsx1FallbackClockSource_Type(Integer32):
    """Custom type gdcDsx1FallbackClockSource based on Integer32"""
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
        *(("cascade", 6),
          ("channel", 5),
          ("composite", 3),
          ("localTiming", 7),
          ("loopTiming", 4),
          ("none", 2),
          ("other", 1),
          ("shelf", 9),
          ("station", 8))
    )


_GdcDsx1FallbackClockSource_Type.__name__ = "Integer32"
_GdcDsx1FallbackClockSource_Object = MibTableColumn
gdcDsx1FallbackClockSource = _GdcDsx1FallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 11),
    _GdcDsx1FallbackClockSource_Type()
)
gdcDsx1FallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1FallbackClockSource.setStatus("mandatory")


class _GdcDsx1AISLoopdown_Type(Integer32):
    """Custom type gdcDsx1AISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_GdcDsx1AISLoopdown_Type.__name__ = "Integer32"
_GdcDsx1AISLoopdown_Object = MibTableColumn
gdcDsx1AISLoopdown = _GdcDsx1AISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 14),
    _GdcDsx1AISLoopdown_Type()
)
gdcDsx1AISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1AISLoopdown.setStatus("mandatory")


class _GdcDsx1InbandLoopCfg_Type(Integer32):
    """Custom type gdcDsx1InbandLoopCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("lineloop", 3),
          ("payload", 2))
    )


_GdcDsx1InbandLoopCfg_Type.__name__ = "Integer32"
_GdcDsx1InbandLoopCfg_Object = MibTableColumn
gdcDsx1InbandLoopCfg = _GdcDsx1InbandLoopCfg_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 15),
    _GdcDsx1InbandLoopCfg_Type()
)
gdcDsx1InbandLoopCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1InbandLoopCfg.setStatus("mandatory")


class _GdcDsx1Redundancy_Type(Integer32):
    """Custom type gdcDsx1Redundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backUp", 2),
          ("keepAlive", 3),
          ("onLine", 1))
    )


_GdcDsx1Redundancy_Type.__name__ = "Integer32"
_GdcDsx1Redundancy_Object = MibTableColumn
gdcDsx1Redundancy = _GdcDsx1Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 3, 1, 1, 16),
    _GdcDsx1Redundancy_Type()
)
gdcDsx1Redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1Redundancy.setStatus("mandatory")
_GdcDsx1Diagnostics_ObjectIdentity = ObjectIdentity
gdcDsx1Diagnostics = _GdcDsx1Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4)
)
_GdcDsx1DiagTable_Object = MibTable
gdcDsx1DiagTable = _GdcDsx1DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1DiagTable.setStatus("mandatory")
_GdcDsx1DiagEntry_Object = MibTableRow
gdcDsx1DiagEntry = _GdcDsx1DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1)
)
gdcDsx1DiagEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1DiagIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1DiagEntry.setStatus("mandatory")
_GdcDsx1DiagIndex_Type = SCinstance
_GdcDsx1DiagIndex_Object = MibTableColumn
gdcDsx1DiagIndex = _GdcDsx1DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 1),
    _GdcDsx1DiagIndex_Type()
)
gdcDsx1DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1DiagIndex.setStatus("mandatory")


class _GdcDsx1SendCode_Type(Integer32):
    """Custom type gdcDsx1SendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("send2047PatternWithLT", 13),
          ("send2047PatternWithRT", 14),
          ("send2047pattern", 3),
          ("send3in24PatternWithRT", 19),
          ("send511PatternWithLT", 11),
          ("send511PatternWithRT", 12),
          ("sendDS0DelayPattern", 10),
          ("sendInbandCode", 6),
          ("sendInbandCodeReset", 7),
          ("sendNetworkInterfaceCode", 8),
          ("sendNtworkInterfaceResetcode", 9),
          ("sendProgPattern", 2),
          ("sendProgPatternWithLT", 17),
          ("sendProgPatternWithRT", 18),
          ("sendQRSPatternWithLT", 15),
          ("sendQRSPatternWithRT", 16))
    )


_GdcDsx1SendCode_Type.__name__ = "Integer32"
_GdcDsx1SendCode_Object = MibTableColumn
gdcDsx1SendCode = _GdcDsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 2),
    _GdcDsx1SendCode_Type()
)
gdcDsx1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1SendCode.setStatus("mandatory")


class _GdcDsx1LoopbackConfig_Type(Integer32):
    """Custom type gdcDsx1LoopbackConfig based on Integer32"""
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
        *(("cascade", 4),
          ("ds0", 3),
          ("localtest", 2),
          ("other", 1))
    )


_GdcDsx1LoopbackConfig_Type.__name__ = "Integer32"
_GdcDsx1LoopbackConfig_Object = MibTableColumn
gdcDsx1LoopbackConfig = _GdcDsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 4),
    _GdcDsx1LoopbackConfig_Type()
)
gdcDsx1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1LoopbackConfig.setStatus("mandatory")


class _GdcDsx1DS0Diag_Type(Integer32):
    """Custom type gdcDsx1DS0Diag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_GdcDsx1DS0Diag_Type.__name__ = "Integer32"
_GdcDsx1DS0Diag_Object = MibTableColumn
gdcDsx1DS0Diag = _GdcDsx1DS0Diag_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 5),
    _GdcDsx1DS0Diag_Type()
)
gdcDsx1DS0Diag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1DS0Diag.setStatus("mandatory")


class _GdcDsx1TestDuration_Type(Integer32):
    """Custom type gdcDsx1TestDuration based on Integer32"""
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


_GdcDsx1TestDuration_Type.__name__ = "Integer32"
_GdcDsx1TestDuration_Object = MibTableColumn
gdcDsx1TestDuration = _GdcDsx1TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 6),
    _GdcDsx1TestDuration_Type()
)
gdcDsx1TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1TestDuration.setStatus("mandatory")


class _GdcDsx1TestExecutionStatus_Type(Integer32):
    """Custom type gdcDsx1TestExecutionStatus based on Integer32"""
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


_GdcDsx1TestExecutionStatus_Type.__name__ = "Integer32"
_GdcDsx1TestExecutionStatus_Object = MibTableColumn
gdcDsx1TestExecutionStatus = _GdcDsx1TestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 8),
    _GdcDsx1TestExecutionStatus_Type()
)
gdcDsx1TestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1TestExecutionStatus.setStatus("mandatory")


class _GdcDsx1TestExceptions_Type(Integer32):
    """Custom type gdcDsx1TestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GdcDsx1TestExceptions_Type.__name__ = "Integer32"
_GdcDsx1TestExceptions_Object = MibTableColumn
gdcDsx1TestExceptions = _GdcDsx1TestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 9),
    _GdcDsx1TestExceptions_Type()
)
gdcDsx1TestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1TestExceptions.setStatus("mandatory")


class _GdcDsx1TestResults_Type(Integer32):
    """Custom type gdcDsx1TestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_GdcDsx1TestResults_Type.__name__ = "Integer32"
_GdcDsx1TestResults_Object = MibTableColumn
gdcDsx1TestResults = _GdcDsx1TestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 4, 1, 1, 10),
    _GdcDsx1TestResults_Type()
)
gdcDsx1TestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1TestResults.setStatus("mandatory")
_GdcDsx1Performance_ObjectIdentity = ObjectIdentity
gdcDsx1Performance = _GdcDsx1Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5)
)
_GdcDsx1ANSIperfTable_Object = MibTable
gdcDsx1ANSIperfTable = _GdcDsx1ANSIperfTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1ANSIperfTable.setStatus("mandatory")
_GdcDsx1ANSIperfEntry_Object = MibTableRow
gdcDsx1ANSIperfEntry = _GdcDsx1ANSIperfEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1)
)
gdcDsx1ANSIperfEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1ANSIperfIndex"),
    (0, "GDCDSX1-MIB", "gdcDsx1ANSIdirection"),
    (0, "GDCDSX1-MIB", "gdcDsx1ANSIseconds"),
)
if mibBuilder.loadTexts:
    gdcDsx1ANSIperfEntry.setStatus("mandatory")
_GdcDsx1ANSIperfIndex_Type = SCinstance
_GdcDsx1ANSIperfIndex_Object = MibTableColumn
gdcDsx1ANSIperfIndex = _GdcDsx1ANSIperfIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 1),
    _GdcDsx1ANSIperfIndex_Type()
)
gdcDsx1ANSIperfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIperfIndex.setStatus("mandatory")


class _GdcDsx1ANSIdirection_Type(Integer32):
    """Custom type gdcDsx1ANSIdirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 1))
    )


_GdcDsx1ANSIdirection_Type.__name__ = "Integer32"
_GdcDsx1ANSIdirection_Object = MibTableColumn
gdcDsx1ANSIdirection = _GdcDsx1ANSIdirection_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 2),
    _GdcDsx1ANSIdirection_Type()
)
gdcDsx1ANSIdirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIdirection.setStatus("mandatory")


class _GdcDsx1ANSIseconds_Type(Integer32):
    """Custom type gdcDsx1ANSIseconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GdcDsx1ANSIseconds_Type.__name__ = "Integer32"
_GdcDsx1ANSIseconds_Object = MibTableColumn
gdcDsx1ANSIseconds = _GdcDsx1ANSIseconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 3),
    _GdcDsx1ANSIseconds_Type()
)
gdcDsx1ANSIseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIseconds.setStatus("mandatory")


class _GdcDsx1ANSICRCerrorEvents_Type(Integer32):
    """Custom type gdcDsx1ANSICRCerrorEvents based on Integer32"""
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


_GdcDsx1ANSICRCerrorEvents_Type.__name__ = "Integer32"
_GdcDsx1ANSICRCerrorEvents_Object = MibTableColumn
gdcDsx1ANSICRCerrorEvents = _GdcDsx1ANSICRCerrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 4),
    _GdcDsx1ANSICRCerrorEvents_Type()
)
gdcDsx1ANSICRCerrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSICRCerrorEvents.setStatus("mandatory")


class _GdcDsx1ANSIsevereErrors_Type(Integer32):
    """Custom type gdcDsx1ANSIsevereErrors based on Integer32"""
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


_GdcDsx1ANSIsevereErrors_Type.__name__ = "Integer32"
_GdcDsx1ANSIsevereErrors_Object = MibTableColumn
gdcDsx1ANSIsevereErrors = _GdcDsx1ANSIsevereErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 5),
    _GdcDsx1ANSIsevereErrors_Type()
)
gdcDsx1ANSIsevereErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIsevereErrors.setStatus("mandatory")


class _GdcDsx1ANSIframeErrors_Type(Integer32):
    """Custom type gdcDsx1ANSIframeErrors based on Integer32"""
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


_GdcDsx1ANSIframeErrors_Type.__name__ = "Integer32"
_GdcDsx1ANSIframeErrors_Object = MibTableColumn
gdcDsx1ANSIframeErrors = _GdcDsx1ANSIframeErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 6),
    _GdcDsx1ANSIframeErrors_Type()
)
gdcDsx1ANSIframeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIframeErrors.setStatus("mandatory")


class _GdcDsx1ANSIcodeViolations_Type(Integer32):
    """Custom type gdcDsx1ANSIcodeViolations based on Integer32"""
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


_GdcDsx1ANSIcodeViolations_Type.__name__ = "Integer32"
_GdcDsx1ANSIcodeViolations_Object = MibTableColumn
gdcDsx1ANSIcodeViolations = _GdcDsx1ANSIcodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 7),
    _GdcDsx1ANSIcodeViolations_Type()
)
gdcDsx1ANSIcodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIcodeViolations.setStatus("mandatory")


class _GdcDsx1ANSIcontrolledSlips_Type(Integer32):
    """Custom type gdcDsx1ANSIcontrolledSlips based on Integer32"""
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


_GdcDsx1ANSIcontrolledSlips_Type.__name__ = "Integer32"
_GdcDsx1ANSIcontrolledSlips_Object = MibTableColumn
gdcDsx1ANSIcontrolledSlips = _GdcDsx1ANSIcontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 8),
    _GdcDsx1ANSIcontrolledSlips_Type()
)
gdcDsx1ANSIcontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIcontrolledSlips.setStatus("mandatory")


class _GdcDsx1ANSIactivePayloadLoops_Type(Integer32):
    """Custom type gdcDsx1ANSIactivePayloadLoops based on Integer32"""
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


_GdcDsx1ANSIactivePayloadLoops_Type.__name__ = "Integer32"
_GdcDsx1ANSIactivePayloadLoops_Object = MibTableColumn
gdcDsx1ANSIactivePayloadLoops = _GdcDsx1ANSIactivePayloadLoops_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 1, 1, 9),
    _GdcDsx1ANSIactivePayloadLoops_Type()
)
gdcDsx1ANSIactivePayloadLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1ANSIactivePayloadLoops.setStatus("mandatory")
_GdcDsx1CurrentTable_Object = MibTable
gdcDsx1CurrentTable = _GdcDsx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gdcDsx1CurrentTable.setStatus("mandatory")
_GdcDsx1CurrentEntry_Object = MibTableRow
gdcDsx1CurrentEntry = _GdcDsx1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 2, 1)
)
gdcDsx1CurrentEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1CurrentEntry.setStatus("mandatory")
_GdcDsx1CurrentIndex_Type = SCinstance
_GdcDsx1CurrentIndex_Object = MibTableColumn
gdcDsx1CurrentIndex = _GdcDsx1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 2, 1, 1),
    _GdcDsx1CurrentIndex_Type()
)
gdcDsx1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1CurrentIndex.setStatus("mandatory")
_GdcDsx1CurrentLOFCs_Type = Gauge32
_GdcDsx1CurrentLOFCs_Object = MibTableColumn
gdcDsx1CurrentLOFCs = _GdcDsx1CurrentLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 2, 1, 2),
    _GdcDsx1CurrentLOFCs_Type()
)
gdcDsx1CurrentLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1CurrentLOFCs.setStatus("mandatory")


class _GdcDsx1CurrenUserStat_Type(OctetString):
    """Custom type gdcDsx1CurrenUserStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_GdcDsx1CurrenUserStat_Type.__name__ = "OctetString"
_GdcDsx1CurrenUserStat_Object = MibTableColumn
gdcDsx1CurrenUserStat = _GdcDsx1CurrenUserStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 2, 1, 3),
    _GdcDsx1CurrenUserStat_Type()
)
gdcDsx1CurrenUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1CurrenUserStat.setStatus("mandatory")
_GdcDsx1IntervalTable_Object = MibTable
gdcDsx1IntervalTable = _GdcDsx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 3)
)
if mibBuilder.loadTexts:
    gdcDsx1IntervalTable.setStatus("mandatory")
_GdcDsx1IntervalEntry_Object = MibTableRow
gdcDsx1IntervalEntry = _GdcDsx1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 3, 1)
)
gdcDsx1IntervalEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1IntervalIndex"),
    (0, "GDCDSX1-MIB", "gdcDsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    gdcDsx1IntervalEntry.setStatus("mandatory")
_GdcDsx1IntervalIndex_Type = SCinstance
_GdcDsx1IntervalIndex_Object = MibTableColumn
gdcDsx1IntervalIndex = _GdcDsx1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 3, 1, 1),
    _GdcDsx1IntervalIndex_Type()
)
gdcDsx1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1IntervalIndex.setStatus("mandatory")


class _GdcDsx1IntervalNumber_Type(Integer32):
    """Custom type gdcDsx1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GdcDsx1IntervalNumber_Type.__name__ = "Integer32"
_GdcDsx1IntervalNumber_Object = MibTableColumn
gdcDsx1IntervalNumber = _GdcDsx1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 3, 1, 2),
    _GdcDsx1IntervalNumber_Type()
)
gdcDsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1IntervalNumber.setStatus("mandatory")
_GdcDsx1IntervalLOFCs_Type = Gauge32
_GdcDsx1IntervalLOFCs_Object = MibTableColumn
gdcDsx1IntervalLOFCs = _GdcDsx1IntervalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 3, 1, 3),
    _GdcDsx1IntervalLOFCs_Type()
)
gdcDsx1IntervalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1IntervalLOFCs.setStatus("mandatory")
_GdcDsx1TotalTable_Object = MibTable
gdcDsx1TotalTable = _GdcDsx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 4)
)
if mibBuilder.loadTexts:
    gdcDsx1TotalTable.setStatus("mandatory")
_GdcDsx1TotalEntry_Object = MibTableRow
gdcDsx1TotalEntry = _GdcDsx1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 4, 1)
)
gdcDsx1TotalEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1TotalEntry.setStatus("mandatory")
_GdcDsx1TotalIndex_Type = SCinstance
_GdcDsx1TotalIndex_Object = MibTableColumn
gdcDsx1TotalIndex = _GdcDsx1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 4, 1, 1),
    _GdcDsx1TotalIndex_Type()
)
gdcDsx1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1TotalIndex.setStatus("mandatory")
_GdcDsx1TotalLOFCs_Type = Gauge32
_GdcDsx1TotalLOFCs_Object = MibTableColumn
gdcDsx1TotalLOFCs = _GdcDsx1TotalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 5, 4, 1, 2),
    _GdcDsx1TotalLOFCs_Type()
)
gdcDsx1TotalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1TotalLOFCs.setStatus("mandatory")
_GdcDsx1Alarms_ObjectIdentity = ObjectIdentity
gdcDsx1Alarms = _GdcDsx1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6)
)
_GdcDsx1AlarmConfigTable_Object = MibTable
gdcDsx1AlarmConfigTable = _GdcDsx1AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1AlarmConfigTable.setStatus("mandatory")
_GdcDsx1AlarmConfigEntry_Object = MibTableRow
gdcDsx1AlarmConfigEntry = _GdcDsx1AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1, 1)
)
gdcDsx1AlarmConfigEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1AlarmConfigIndex"),
    (0, "GDCDSX1-MIB", "gdcDsx1AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    gdcDsx1AlarmConfigEntry.setStatus("mandatory")
_GdcDsx1AlarmConfigIndex_Type = SCinstance
_GdcDsx1AlarmConfigIndex_Object = MibTableColumn
gdcDsx1AlarmConfigIndex = _GdcDsx1AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1, 1, 1),
    _GdcDsx1AlarmConfigIndex_Type()
)
gdcDsx1AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmConfigIndex.setStatus("mandatory")
_GdcDsx1AlarmConfigIdentifier_Type = ObjectIdentifier
_GdcDsx1AlarmConfigIdentifier_Object = MibTableColumn
gdcDsx1AlarmConfigIdentifier = _GdcDsx1AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1, 1, 2),
    _GdcDsx1AlarmConfigIdentifier_Type()
)
gdcDsx1AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmConfigIdentifier.setStatus("mandatory")


class _GdcDsx1AlarmCountWindow_Type(Integer32):
    """Custom type gdcDsx1AlarmCountWindow based on Integer32"""
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
        *(("disabled", 1),
          ("infinite", 5),
          ("last1hr", 4),
          ("last1min", 3),
          ("last1sec", 2))
    )


_GdcDsx1AlarmCountWindow_Type.__name__ = "Integer32"
_GdcDsx1AlarmCountWindow_Object = MibTableColumn
gdcDsx1AlarmCountWindow = _GdcDsx1AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1, 1, 3),
    _GdcDsx1AlarmCountWindow_Type()
)
gdcDsx1AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1AlarmCountWindow.setStatus("mandatory")


class _GdcDsx1AlarmCountThreshold_Type(Integer32):
    """Custom type gdcDsx1AlarmCountThreshold based on Integer32"""
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
        *(("thresGT10", 1),
          ("thresGT100", 2),
          ("thresGT1000", 3),
          ("thresGT10000", 4))
    )


_GdcDsx1AlarmCountThreshold_Type.__name__ = "Integer32"
_GdcDsx1AlarmCountThreshold_Object = MibTableColumn
gdcDsx1AlarmCountThreshold = _GdcDsx1AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 1, 1, 4),
    _GdcDsx1AlarmCountThreshold_Type()
)
gdcDsx1AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsx1AlarmCountThreshold.setStatus("mandatory")
_GdcDsx1AlarmStatusTable_Object = MibTable
gdcDsx1AlarmStatusTable = _GdcDsx1AlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    gdcDsx1AlarmStatusTable.setStatus("mandatory")
_GdcDsx1AlarmStatusEntry_Object = MibTableRow
gdcDsx1AlarmStatusEntry = _GdcDsx1AlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1)
)
gdcDsx1AlarmStatusEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1AlarmStatusIndex"),
    (0, "GDCDSX1-MIB", "gdcDsx1AlarmStatusIdentifier"),
)
if mibBuilder.loadTexts:
    gdcDsx1AlarmStatusEntry.setStatus("mandatory")
_GdcDsx1AlarmStatusIndex_Type = SCinstance
_GdcDsx1AlarmStatusIndex_Object = MibTableColumn
gdcDsx1AlarmStatusIndex = _GdcDsx1AlarmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1, 1),
    _GdcDsx1AlarmStatusIndex_Type()
)
gdcDsx1AlarmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmStatusIndex.setStatus("mandatory")
_GdcDsx1AlarmStatusIdentifier_Type = ObjectIdentifier
_GdcDsx1AlarmStatusIdentifier_Object = MibTableColumn
gdcDsx1AlarmStatusIdentifier = _GdcDsx1AlarmStatusIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1, 2),
    _GdcDsx1AlarmStatusIdentifier_Type()
)
gdcDsx1AlarmStatusIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmStatusIdentifier.setStatus("mandatory")
_GdcDsx1AlarmCount_Type = Gauge32
_GdcDsx1AlarmCount_Object = MibTableColumn
gdcDsx1AlarmCount = _GdcDsx1AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1, 3),
    _GdcDsx1AlarmCount_Type()
)
gdcDsx1AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmCount.setStatus("mandatory")
_GdcDsx1AlarmFirstOccurrence_Type = TimeTicks
_GdcDsx1AlarmFirstOccurrence_Object = MibTableColumn
gdcDsx1AlarmFirstOccurrence = _GdcDsx1AlarmFirstOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1, 4),
    _GdcDsx1AlarmFirstOccurrence_Type()
)
gdcDsx1AlarmFirstOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmFirstOccurrence.setStatus("mandatory")
_GdcDsx1AlarmLastOccurrence_Type = TimeTicks
_GdcDsx1AlarmLastOccurrence_Object = MibTableColumn
gdcDsx1AlarmLastOccurrence = _GdcDsx1AlarmLastOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 6, 2, 1, 5),
    _GdcDsx1AlarmLastOccurrence_Type()
)
gdcDsx1AlarmLastOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1AlarmLastOccurrence.setStatus("mandatory")
_GdcDsx1NetMaintenance_ObjectIdentity = ObjectIdentity
gdcDsx1NetMaintenance = _GdcDsx1NetMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7)
)
_GdcDsx1NetMaintTable_Object = MibTable
gdcDsx1NetMaintTable = _GdcDsx1NetMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    gdcDsx1NetMaintTable.setStatus("mandatory")
_GdcDsx1NetMaintEntry_Object = MibTableRow
gdcDsx1NetMaintEntry = _GdcDsx1NetMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7, 1, 1)
)
gdcDsx1NetMaintEntry.setIndexNames(
    (0, "GDCDSX1-MIB", "gdcDsx1NetMaintLineIndex"),
)
if mibBuilder.loadTexts:
    gdcDsx1NetMaintEntry.setStatus("mandatory")
_GdcDsx1NetMaintLineIndex_Type = SCinstance
_GdcDsx1NetMaintLineIndex_Object = MibTableColumn
gdcDsx1NetMaintLineIndex = _GdcDsx1NetMaintLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7, 1, 1, 1),
    _GdcDsx1NetMaintLineIndex_Type()
)
gdcDsx1NetMaintLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1NetMaintLineIndex.setStatus("mandatory")


class _GdcDsx1NetMaintReceiveLevel_Type(Integer32):
    """Custom type gdcDsx1NetMaintReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43),
    )


_GdcDsx1NetMaintReceiveLevel_Type.__name__ = "Integer32"
_GdcDsx1NetMaintReceiveLevel_Object = MibTableColumn
gdcDsx1NetMaintReceiveLevel = _GdcDsx1NetMaintReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7, 1, 1, 2),
    _GdcDsx1NetMaintReceiveLevel_Type()
)
gdcDsx1NetMaintReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1NetMaintReceiveLevel.setStatus("mandatory")


class _GdcDsx1NetMaintAttenSense_Type(Integer32):
    """Custom type gdcDsx1NetMaintAttenSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_GdcDsx1NetMaintAttenSense_Type.__name__ = "Integer32"
_GdcDsx1NetMaintAttenSense_Object = MibTableColumn
gdcDsx1NetMaintAttenSense = _GdcDsx1NetMaintAttenSense_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 1, 7, 1, 1, 3),
    _GdcDsx1NetMaintAttenSense_Type()
)
gdcDsx1NetMaintAttenSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsx1NetMaintAttenSense.setStatus("mandatory")
_Sc5001_ObjectIdentity = ObjectIdentity
sc5001 = _Sc5001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2)
)
_Dsx1AlarmData_ObjectIdentity = ObjectIdentity
dsx1AlarmData = _Dsx1AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1)
)
_Dsx1NoResponseAlm_ObjectIdentity = ObjectIdentity
dsx1NoResponseAlm = _Dsx1NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 1)
)
_Dsx1DiagRxErrAlm_ObjectIdentity = ObjectIdentity
dsx1DiagRxErrAlm = _Dsx1DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 2)
)
_Dsx1PowerUpAlm_ObjectIdentity = ObjectIdentity
dsx1PowerUpAlm = _Dsx1PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 3)
)
_Dsx1NvRamCorrupt_ObjectIdentity = ObjectIdentity
dsx1NvRamCorrupt = _Dsx1NvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 4)
)
_Dsx1UnitFailure_ObjectIdentity = ObjectIdentity
dsx1UnitFailure = _Dsx1UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 5)
)
_Dsx1MbiLock_ObjectIdentity = ObjectIdentity
dsx1MbiLock = _Dsx1MbiLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 6)
)
_Dsx1LocalPwrFail_ObjectIdentity = ObjectIdentity
dsx1LocalPwrFail = _Dsx1LocalPwrFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 7)
)
_Dsx1TimingLoss_ObjectIdentity = ObjectIdentity
dsx1TimingLoss = _Dsx1TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 8)
)
_Dsx1StatusChange_ObjectIdentity = ObjectIdentity
dsx1StatusChange = _Dsx1StatusChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 9)
)
_Dsx1UnsoTest_ObjectIdentity = ObjectIdentity
dsx1UnsoTest = _Dsx1UnsoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 10)
)
_Dsx1LossOfSignal_ObjectIdentity = ObjectIdentity
dsx1LossOfSignal = _Dsx1LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 11)
)
_Dsx1LossOfFrame_ObjectIdentity = ObjectIdentity
dsx1LossOfFrame = _Dsx1LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 12)
)
_Dsx1Ais_ObjectIdentity = ObjectIdentity
dsx1Ais = _Dsx1Ais_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 13)
)
_Dsx1ReceivedYellow_ObjectIdentity = ObjectIdentity
dsx1ReceivedYellow = _Dsx1ReceivedYellow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 14)
)
_Dsx1UnavailSignalState_ObjectIdentity = ObjectIdentity
dsx1UnavailSignalState = _Dsx1UnavailSignalState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 15)
)
_Dsx1ExcessiveZeros_ObjectIdentity = ObjectIdentity
dsx1ExcessiveZeros = _Dsx1ExcessiveZeros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 16)
)
_Dsx1LowAverageDensity_ObjectIdentity = ObjectIdentity
dsx1LowAverageDensity = _Dsx1LowAverageDensity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 17)
)
_Dsx1ControlledSlips_ObjectIdentity = ObjectIdentity
dsx1ControlledSlips = _Dsx1ControlledSlips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 18)
)
_Dsx1BipolarViolations_ObjectIdentity = ObjectIdentity
dsx1BipolarViolations = _Dsx1BipolarViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 19)
)
_Dsx1CrcErrors_ObjectIdentity = ObjectIdentity
dsx1CrcErrors = _Dsx1CrcErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 20)
)
_Dsx1FallbackTimingActive_ObjectIdentity = ObjectIdentity
dsx1FallbackTimingActive = _Dsx1FallbackTimingActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 2, 1, 21)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCDSX1-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "gdcDsx1System": gdcDsx1System,
       "gdcDsx1Version": gdcDsx1Version,
       "gdcDsx1SystemMIBversion": gdcDsx1SystemMIBversion,
       "gdcDsx1VersionTable": gdcDsx1VersionTable,
       "gdcDsx1VersionEntry": gdcDsx1VersionEntry,
       "gdcDsx1VersionIndex": gdcDsx1VersionIndex,
       "gdcDsx1FirmwareRev": gdcDsx1FirmwareRev,
       "gdcDsx1ModelNumber": gdcDsx1ModelNumber,
       "gdcDsx1ActiveFirmwareRev": gdcDsx1ActiveFirmwareRev,
       "gdcDsx1StoredFirmwareRev": gdcDsx1StoredFirmwareRev,
       "gdcDsx1BootRev": gdcDsx1BootRev,
       "gdcDsx1StoredFirmwareStatus": gdcDsx1StoredFirmwareStatus,
       "gdcDsx1SwitchActiveFirmware": gdcDsx1SwitchActiveFirmware,
       "gdcDsx1DownloadingMode": gdcDsx1DownloadingMode,
       "gdcDsx1Maintenance": gdcDsx1Maintenance,
       "gdcDsx1MaintenanceTable": gdcDsx1MaintenanceTable,
       "gdcDsx1MaintenanceEntry": gdcDsx1MaintenanceEntry,
       "gdcDsx1MaintenanceLineIndex": gdcDsx1MaintenanceLineIndex,
       "gdcDsx1SoftReset": gdcDsx1SoftReset,
       "gdcDsx1ConfigMode": gdcDsx1ConfigMode,
       "gdcDsx1FrontPanel": gdcDsx1FrontPanel,
       "gdcDsx1SysUpTime": gdcDsx1SysUpTime,
       "gdcDsx1DefaultInit": gdcDsx1DefaultInit,
       "gdcDsx1ResetStats": gdcDsx1ResetStats,
       "gdcDsx1LedStatus": gdcDsx1LedStatus,
       "gdcDsx1SetTransmitClkSrc": gdcDsx1SetTransmitClkSrc,
       "gdcDsx1CsuMode": gdcDsx1CsuMode,
       "gdcDsx1CircuitIdentifier1": gdcDsx1CircuitIdentifier1,
       "gdcDsx1CircuitIdentifier2": gdcDsx1CircuitIdentifier2,
       "gdcDsx1Configuration": gdcDsx1Configuration,
       "gdcDsx1ConfigTable": gdcDsx1ConfigTable,
       "gdcDsx1ConfigEntry": gdcDsx1ConfigEntry,
       "gdcDsx1ConfigIndex": gdcDsx1ConfigIndex,
       "gdcDsx1LineType": gdcDsx1LineType,
       "gdcDsx1InterfaceType": gdcDsx1InterfaceType,
       "gdcDsx1Preequalization": gdcDsx1Preequalization,
       "gdcDsx1AdminLineBuildout": gdcDsx1AdminLineBuildout,
       "gdcDsx1OperLineBuildout": gdcDsx1OperLineBuildout,
       "gdcDsx1AdminRcvRange": gdcDsx1AdminRcvRange,
       "gdcDsx1OperRcvRange": gdcDsx1OperRcvRange,
       "gdcDsx1OnesDensity": gdcDsx1OnesDensity,
       "gdcDsx1TransmitClockSource": gdcDsx1TransmitClockSource,
       "gdcDsx1FallbackClockSource": gdcDsx1FallbackClockSource,
       "gdcDsx1AISLoopdown": gdcDsx1AISLoopdown,
       "gdcDsx1InbandLoopCfg": gdcDsx1InbandLoopCfg,
       "gdcDsx1Redundancy": gdcDsx1Redundancy,
       "gdcDsx1Diagnostics": gdcDsx1Diagnostics,
       "gdcDsx1DiagTable": gdcDsx1DiagTable,
       "gdcDsx1DiagEntry": gdcDsx1DiagEntry,
       "gdcDsx1DiagIndex": gdcDsx1DiagIndex,
       "gdcDsx1SendCode": gdcDsx1SendCode,
       "gdcDsx1LoopbackConfig": gdcDsx1LoopbackConfig,
       "gdcDsx1DS0Diag": gdcDsx1DS0Diag,
       "gdcDsx1TestDuration": gdcDsx1TestDuration,
       "gdcDsx1TestExecutionStatus": gdcDsx1TestExecutionStatus,
       "gdcDsx1TestExceptions": gdcDsx1TestExceptions,
       "gdcDsx1TestResults": gdcDsx1TestResults,
       "gdcDsx1Performance": gdcDsx1Performance,
       "gdcDsx1ANSIperfTable": gdcDsx1ANSIperfTable,
       "gdcDsx1ANSIperfEntry": gdcDsx1ANSIperfEntry,
       "gdcDsx1ANSIperfIndex": gdcDsx1ANSIperfIndex,
       "gdcDsx1ANSIdirection": gdcDsx1ANSIdirection,
       "gdcDsx1ANSIseconds": gdcDsx1ANSIseconds,
       "gdcDsx1ANSICRCerrorEvents": gdcDsx1ANSICRCerrorEvents,
       "gdcDsx1ANSIsevereErrors": gdcDsx1ANSIsevereErrors,
       "gdcDsx1ANSIframeErrors": gdcDsx1ANSIframeErrors,
       "gdcDsx1ANSIcodeViolations": gdcDsx1ANSIcodeViolations,
       "gdcDsx1ANSIcontrolledSlips": gdcDsx1ANSIcontrolledSlips,
       "gdcDsx1ANSIactivePayloadLoops": gdcDsx1ANSIactivePayloadLoops,
       "gdcDsx1CurrentTable": gdcDsx1CurrentTable,
       "gdcDsx1CurrentEntry": gdcDsx1CurrentEntry,
       "gdcDsx1CurrentIndex": gdcDsx1CurrentIndex,
       "gdcDsx1CurrentLOFCs": gdcDsx1CurrentLOFCs,
       "gdcDsx1CurrenUserStat": gdcDsx1CurrenUserStat,
       "gdcDsx1IntervalTable": gdcDsx1IntervalTable,
       "gdcDsx1IntervalEntry": gdcDsx1IntervalEntry,
       "gdcDsx1IntervalIndex": gdcDsx1IntervalIndex,
       "gdcDsx1IntervalNumber": gdcDsx1IntervalNumber,
       "gdcDsx1IntervalLOFCs": gdcDsx1IntervalLOFCs,
       "gdcDsx1TotalTable": gdcDsx1TotalTable,
       "gdcDsx1TotalEntry": gdcDsx1TotalEntry,
       "gdcDsx1TotalIndex": gdcDsx1TotalIndex,
       "gdcDsx1TotalLOFCs": gdcDsx1TotalLOFCs,
       "gdcDsx1Alarms": gdcDsx1Alarms,
       "gdcDsx1AlarmConfigTable": gdcDsx1AlarmConfigTable,
       "gdcDsx1AlarmConfigEntry": gdcDsx1AlarmConfigEntry,
       "gdcDsx1AlarmConfigIndex": gdcDsx1AlarmConfigIndex,
       "gdcDsx1AlarmConfigIdentifier": gdcDsx1AlarmConfigIdentifier,
       "gdcDsx1AlarmCountWindow": gdcDsx1AlarmCountWindow,
       "gdcDsx1AlarmCountThreshold": gdcDsx1AlarmCountThreshold,
       "gdcDsx1AlarmStatusTable": gdcDsx1AlarmStatusTable,
       "gdcDsx1AlarmStatusEntry": gdcDsx1AlarmStatusEntry,
       "gdcDsx1AlarmStatusIndex": gdcDsx1AlarmStatusIndex,
       "gdcDsx1AlarmStatusIdentifier": gdcDsx1AlarmStatusIdentifier,
       "gdcDsx1AlarmCount": gdcDsx1AlarmCount,
       "gdcDsx1AlarmFirstOccurrence": gdcDsx1AlarmFirstOccurrence,
       "gdcDsx1AlarmLastOccurrence": gdcDsx1AlarmLastOccurrence,
       "gdcDsx1NetMaintenance": gdcDsx1NetMaintenance,
       "gdcDsx1NetMaintTable": gdcDsx1NetMaintTable,
       "gdcDsx1NetMaintEntry": gdcDsx1NetMaintEntry,
       "gdcDsx1NetMaintLineIndex": gdcDsx1NetMaintLineIndex,
       "gdcDsx1NetMaintReceiveLevel": gdcDsx1NetMaintReceiveLevel,
       "gdcDsx1NetMaintAttenSense": gdcDsx1NetMaintAttenSense,
       "sc5001": sc5001,
       "dsx1AlarmData": dsx1AlarmData,
       "dsx1NoResponseAlm": dsx1NoResponseAlm,
       "dsx1DiagRxErrAlm": dsx1DiagRxErrAlm,
       "dsx1PowerUpAlm": dsx1PowerUpAlm,
       "dsx1NvRamCorrupt": dsx1NvRamCorrupt,
       "dsx1UnitFailure": dsx1UnitFailure,
       "dsx1MbiLock": dsx1MbiLock,
       "dsx1LocalPwrFail": dsx1LocalPwrFail,
       "dsx1TimingLoss": dsx1TimingLoss,
       "dsx1StatusChange": dsx1StatusChange,
       "dsx1UnsoTest": dsx1UnsoTest,
       "dsx1LossOfSignal": dsx1LossOfSignal,
       "dsx1LossOfFrame": dsx1LossOfFrame,
       "dsx1Ais": dsx1Ais,
       "dsx1ReceivedYellow": dsx1ReceivedYellow,
       "dsx1UnavailSignalState": dsx1UnavailSignalState,
       "dsx1ExcessiveZeros": dsx1ExcessiveZeros,
       "dsx1LowAverageDensity": dsx1LowAverageDensity,
       "dsx1ControlledSlips": dsx1ControlledSlips,
       "dsx1BipolarViolations": dsx1BipolarViolations,
       "dsx1CrcErrors": dsx1CrcErrors,
       "dsx1FallbackTimingActive": dsx1FallbackTimingActive}
)
