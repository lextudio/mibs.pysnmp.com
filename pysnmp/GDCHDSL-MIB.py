# SNMP MIB module (GDCHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCHDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:15 2024
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
_Hdsl_ObjectIdentity = ObjectIdentity
hdsl = _Hdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11)
)
_GdcHdslSystem_ObjectIdentity = ObjectIdentity
gdcHdslSystem = _GdcHdslSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1)
)
_GdcHdslVersion_ObjectIdentity = ObjectIdentity
gdcHdslVersion = _GdcHdslVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1)
)


class _GdcHdslSystemMIBversion_Type(DisplayString):
    """Custom type gdcHdslSystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcHdslSystemMIBversion_Type.__name__ = "DisplayString"
_GdcHdslSystemMIBversion_Object = MibScalar
gdcHdslSystemMIBversion = _GdcHdslSystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 1),
    _GdcHdslSystemMIBversion_Type()
)
gdcHdslSystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslSystemMIBversion.setStatus("mandatory")
_GdcHdslVersionTable_Object = MibTable
gdcHdslVersionTable = _GdcHdslVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gdcHdslVersionTable.setStatus("mandatory")
_GdcHdslVersionEntry_Object = MibTableRow
gdcHdslVersionEntry = _GdcHdslVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 2, 1)
)
gdcHdslVersionEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslVersionIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslVersionEntry.setStatus("mandatory")
_GdcHdslVersionIndex_Type = SCinstance
_GdcHdslVersionIndex_Object = MibTableColumn
gdcHdslVersionIndex = _GdcHdslVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 2, 1, 1),
    _GdcHdslVersionIndex_Type()
)
gdcHdslVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslVersionIndex.setStatus("mandatory")


class _GdcHdslFirmwareRev_Type(DisplayString):
    """Custom type gdcHdslFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GdcHdslFirmwareRev_Type.__name__ = "DisplayString"
_GdcHdslFirmwareRev_Object = MibTableColumn
gdcHdslFirmwareRev = _GdcHdslFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 2, 1, 2),
    _GdcHdslFirmwareRev_Type()
)
gdcHdslFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslFirmwareRev.setStatus("mandatory")


class _GdcHdslModelNumber_Type(DisplayString):
    """Custom type gdcHdslModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GdcHdslModelNumber_Type.__name__ = "DisplayString"
_GdcHdslModelNumber_Object = MibTableColumn
gdcHdslModelNumber = _GdcHdslModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 2, 1, 3),
    _GdcHdslModelNumber_Type()
)
gdcHdslModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslModelNumber.setStatus("mandatory")
_GdcHdslDownloadTable_Object = MibTable
gdcHdslDownloadTable = _GdcHdslDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gdcHdslDownloadTable.setStatus("mandatory")
_GdcHdslDownloadEntry_Object = MibTableRow
gdcHdslDownloadEntry = _GdcHdslDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1)
)
gdcHdslDownloadEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslDownloadIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslDownloadEntry.setStatus("mandatory")
_GdcHdslDownloadIndex_Type = SCinstance
_GdcHdslDownloadIndex_Object = MibTableColumn
gdcHdslDownloadIndex = _GdcHdslDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 1),
    _GdcHdslDownloadIndex_Type()
)
gdcHdslDownloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDownloadIndex.setStatus("mandatory")


class _GdcHdslActiveFirmwareRev_Type(DisplayString):
    """Custom type gdcHdslActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GdcHdslActiveFirmwareRev_Type.__name__ = "DisplayString"
_GdcHdslActiveFirmwareRev_Object = MibTableColumn
gdcHdslActiveFirmwareRev = _GdcHdslActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 2),
    _GdcHdslActiveFirmwareRev_Type()
)
gdcHdslActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslActiveFirmwareRev.setStatus("mandatory")


class _GdcHdslStoredFirmwareRev_Type(DisplayString):
    """Custom type gdcHdslStoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GdcHdslStoredFirmwareRev_Type.__name__ = "DisplayString"
_GdcHdslStoredFirmwareRev_Object = MibTableColumn
gdcHdslStoredFirmwareRev = _GdcHdslStoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 3),
    _GdcHdslStoredFirmwareRev_Type()
)
gdcHdslStoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslStoredFirmwareRev.setStatus("mandatory")


class _GdcHdslStoredFirmwareStatus_Type(Integer32):
    """Custom type gdcHdslStoredFirmwareStatus based on Integer32"""
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


_GdcHdslStoredFirmwareStatus_Type.__name__ = "Integer32"
_GdcHdslStoredFirmwareStatus_Object = MibTableColumn
gdcHdslStoredFirmwareStatus = _GdcHdslStoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 4),
    _GdcHdslStoredFirmwareStatus_Type()
)
gdcHdslStoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslStoredFirmwareStatus.setStatus("mandatory")


class _GdcHdslSwitchActiveFirmware_Type(Integer32):
    """Custom type gdcHdslSwitchActiveFirmware based on Integer32"""
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


_GdcHdslSwitchActiveFirmware_Type.__name__ = "Integer32"
_GdcHdslSwitchActiveFirmware_Object = MibTableColumn
gdcHdslSwitchActiveFirmware = _GdcHdslSwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 5),
    _GdcHdslSwitchActiveFirmware_Type()
)
gdcHdslSwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslSwitchActiveFirmware.setStatus("mandatory")


class _GdcHdslDownloadingMode_Type(Integer32):
    """Custom type gdcHdslDownloadingMode based on Integer32"""
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


_GdcHdslDownloadingMode_Type.__name__ = "Integer32"
_GdcHdslDownloadingMode_Object = MibTableColumn
gdcHdslDownloadingMode = _GdcHdslDownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 6),
    _GdcHdslDownloadingMode_Type()
)
gdcHdslDownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDownloadingMode.setStatus("mandatory")


class _GdcHdslEraseFlash_Type(Integer32):
    """Custom type gdcHdslEraseFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erase", 2),
          ("normal", 1))
    )


_GdcHdslEraseFlash_Type.__name__ = "Integer32"
_GdcHdslEraseFlash_Object = MibTableColumn
gdcHdslEraseFlash = _GdcHdslEraseFlash_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 1, 3, 1, 7),
    _GdcHdslEraseFlash_Type()
)
gdcHdslEraseFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslEraseFlash.setStatus("mandatory")
_GdcHdslMaintenance_ObjectIdentity = ObjectIdentity
gdcHdslMaintenance = _GdcHdslMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2)
)
_GdcHdslMaintenanceTable_Object = MibTable
gdcHdslMaintenanceTable = _GdcHdslMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gdcHdslMaintenanceTable.setStatus("mandatory")
_GdcHdslMaintenanceEntry_Object = MibTableRow
gdcHdslMaintenanceEntry = _GdcHdslMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1)
)
gdcHdslMaintenanceEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslMaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslMaintenanceEntry.setStatus("mandatory")
_GdcHdslMaintenanceLineIndex_Type = SCinstance
_GdcHdslMaintenanceLineIndex_Object = MibTableColumn
gdcHdslMaintenanceLineIndex = _GdcHdslMaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 1),
    _GdcHdslMaintenanceLineIndex_Type()
)
gdcHdslMaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslMaintenanceLineIndex.setStatus("mandatory")


class _GdcHdslSoftReset_Type(Integer32):
    """Custom type gdcHdslSoftReset based on Integer32"""
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


_GdcHdslSoftReset_Type.__name__ = "Integer32"
_GdcHdslSoftReset_Object = MibTableColumn
gdcHdslSoftReset = _GdcHdslSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 2),
    _GdcHdslSoftReset_Type()
)
gdcHdslSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslSoftReset.setStatus("mandatory")


class _GdcHdslConfigMode_Type(Integer32):
    """Custom type gdcHdslConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_GdcHdslConfigMode_Type.__name__ = "Integer32"
_GdcHdslConfigMode_Object = MibTableColumn
gdcHdslConfigMode = _GdcHdslConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 3),
    _GdcHdslConfigMode_Type()
)
gdcHdslConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslConfigMode.setStatus("mandatory")
_GdcHdslSysUpTime_Type = TimeTicks
_GdcHdslSysUpTime_Object = MibTableColumn
gdcHdslSysUpTime = _GdcHdslSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 4),
    _GdcHdslSysUpTime_Type()
)
gdcHdslSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslSysUpTime.setStatus("mandatory")


class _GdcHdslUnitType_Type(Integer32):
    """Custom type gdcHdslUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ltu", 1),
          ("ntu", 2))
    )


_GdcHdslUnitType_Type.__name__ = "Integer32"
_GdcHdslUnitType_Object = MibTableColumn
gdcHdslUnitType = _GdcHdslUnitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 5),
    _GdcHdslUnitType_Type()
)
gdcHdslUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslUnitType.setStatus("mandatory")


class _GdcHdslDefaultInit_Type(Integer32):
    """Custom type gdcHdslDefaultInit based on Integer32"""
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


_GdcHdslDefaultInit_Type.__name__ = "Integer32"
_GdcHdslDefaultInit_Object = MibTableColumn
gdcHdslDefaultInit = _GdcHdslDefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 6),
    _GdcHdslDefaultInit_Type()
)
gdcHdslDefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDefaultInit.setStatus("mandatory")


class _GdcHdslDataType_Type(Integer32):
    """Custom type gdcHdslDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("voice", 1))
    )


_GdcHdslDataType_Type.__name__ = "Integer32"
_GdcHdslDataType_Object = MibTableColumn
gdcHdslDataType = _GdcHdslDataType_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 7),
    _GdcHdslDataType_Type()
)
gdcHdslDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDataType.setStatus("mandatory")


class _GdcHdslLoopProvision_Type(Integer32):
    """Custom type gdcHdslLoopProvision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointomultipoint", 2),
          ("pointopoint", 1))
    )


_GdcHdslLoopProvision_Type.__name__ = "Integer32"
_GdcHdslLoopProvision_Object = MibTableColumn
gdcHdslLoopProvision = _GdcHdslLoopProvision_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 8),
    _GdcHdslLoopProvision_Type()
)
gdcHdslLoopProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslLoopProvision.setStatus("mandatory")


class _GdcHdslNumberofLoops_Type(Integer32):
    """Custom type gdcHdslNumberofLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneLoop", 1),
          ("threeLoops", 3),
          ("twoLoops", 2))
    )


_GdcHdslNumberofLoops_Type.__name__ = "Integer32"
_GdcHdslNumberofLoops_Object = MibTableColumn
gdcHdslNumberofLoops = _GdcHdslNumberofLoops_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 9),
    _GdcHdslNumberofLoops_Type()
)
gdcHdslNumberofLoops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslNumberofLoops.setStatus("mandatory")


class _GdcHdslFrontPanel_Type(Integer32):
    """Custom type gdcHdslFrontPanel based on Integer32"""
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


_GdcHdslFrontPanel_Type.__name__ = "Integer32"
_GdcHdslFrontPanel_Object = MibTableColumn
gdcHdslFrontPanel = _GdcHdslFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 10),
    _GdcHdslFrontPanel_Type()
)
gdcHdslFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslFrontPanel.setStatus("mandatory")


class _GdcHdslRoutingConfig_Type(Integer32):
    """Custom type gdcHdslRoutingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("threeLoops", 2),
          ("twoLoops", 1))
    )


_GdcHdslRoutingConfig_Type.__name__ = "Integer32"
_GdcHdslRoutingConfig_Object = MibTableColumn
gdcHdslRoutingConfig = _GdcHdslRoutingConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 11),
    _GdcHdslRoutingConfig_Type()
)
gdcHdslRoutingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslRoutingConfig.setStatus("mandatory")


class _GdcHdslPrivateStorage1_Type(DisplayString):
    """Custom type gdcHdslPrivateStorage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslPrivateStorage1_Type.__name__ = "DisplayString"
_GdcHdslPrivateStorage1_Object = MibTableColumn
gdcHdslPrivateStorage1 = _GdcHdslPrivateStorage1_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 12),
    _GdcHdslPrivateStorage1_Type()
)
gdcHdslPrivateStorage1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslPrivateStorage1.setStatus("mandatory")


class _GdcHdslPrivateStorage2_Type(DisplayString):
    """Custom type gdcHdslPrivateStorage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslPrivateStorage2_Type.__name__ = "DisplayString"
_GdcHdslPrivateStorage2_Object = MibTableColumn
gdcHdslPrivateStorage2 = _GdcHdslPrivateStorage2_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 13),
    _GdcHdslPrivateStorage2_Type()
)
gdcHdslPrivateStorage2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslPrivateStorage2.setStatus("mandatory")


class _GdcHdslPrivateStorage3_Type(DisplayString):
    """Custom type gdcHdslPrivateStorage3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslPrivateStorage3_Type.__name__ = "DisplayString"
_GdcHdslPrivateStorage3_Object = MibTableColumn
gdcHdslPrivateStorage3 = _GdcHdslPrivateStorage3_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 14),
    _GdcHdslPrivateStorage3_Type()
)
gdcHdslPrivateStorage3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslPrivateStorage3.setStatus("mandatory")


class _GdcHdslLedStatus_Type(OctetString):
    """Custom type gdcHdslLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GdcHdslLedStatus_Type.__name__ = "OctetString"
_GdcHdslLedStatus_Object = MibTableColumn
gdcHdslLedStatus = _GdcHdslLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 15),
    _GdcHdslLedStatus_Type()
)
gdcHdslLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLedStatus.setStatus("mandatory")


class _FracExecution_Type(Integer32):
    """Custom type fracExecution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("norm", 2))
    )


_FracExecution_Type.__name__ = "Integer32"
_FracExecution_Object = MibTableColumn
fracExecution = _FracExecution_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 16),
    _FracExecution_Type()
)
fracExecution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fracExecution.setStatus("mandatory")


class _GdcHdslAlarmStatus_Type(OctetString):
    """Custom type gdcHdslAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_GdcHdslAlarmStatus_Type.__name__ = "OctetString"
_GdcHdslAlarmStatus_Object = MibTableColumn
gdcHdslAlarmStatus = _GdcHdslAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 17),
    _GdcHdslAlarmStatus_Type()
)
gdcHdslAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslAlarmStatus.setStatus("mandatory")


class _GdcHdslV54Config_Type(Integer32):
    """Custom type gdcHdslV54Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("inhibit", 1))
    )


_GdcHdslV54Config_Type.__name__ = "Integer32"
_GdcHdslV54Config_Object = MibTableColumn
gdcHdslV54Config = _GdcHdslV54Config_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 18),
    _GdcHdslV54Config_Type()
)
gdcHdslV54Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslV54Config.setStatus("mandatory")


class _GdcHdslFPRDLConfig_Type(Integer32):
    """Custom type gdcHdslFPRDLConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eoc", 1),
          ("v54", 2))
    )


_GdcHdslFPRDLConfig_Type.__name__ = "Integer32"
_GdcHdslFPRDLConfig_Object = MibTableColumn
gdcHdslFPRDLConfig = _GdcHdslFPRDLConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 19),
    _GdcHdslFPRDLConfig_Type()
)
gdcHdslFPRDLConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslFPRDLConfig.setStatus("mandatory")


class _GdcHdslRLTimeOut_Type(Integer32):
    """Custom type gdcHdslRLTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mins10", 2),
          ("none", 1))
    )


_GdcHdslRLTimeOut_Type.__name__ = "Integer32"
_GdcHdslRLTimeOut_Object = MibTableColumn
gdcHdslRLTimeOut = _GdcHdslRLTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 20),
    _GdcHdslRLTimeOut_Type()
)
gdcHdslRLTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslRLTimeOut.setStatus("mandatory")


class _GdcHdslRPEnable_Type(Integer32):
    """Custom type gdcHdslRPEnable based on Integer32"""
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


_GdcHdslRPEnable_Type.__name__ = "Integer32"
_GdcHdslRPEnable_Object = MibTableColumn
gdcHdslRPEnable = _GdcHdslRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 21),
    _GdcHdslRPEnable_Type()
)
gdcHdslRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslRPEnable.setStatus("mandatory")


class _GdcHdslLedStatus1_Type(OctetString):
    """Custom type gdcHdslLedStatus1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GdcHdslLedStatus1_Type.__name__ = "OctetString"
_GdcHdslLedStatus1_Object = MibTableColumn
gdcHdslLedStatus1 = _GdcHdslLedStatus1_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 2, 1, 1, 22),
    _GdcHdslLedStatus1_Type()
)
gdcHdslLedStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLedStatus1.setStatus("mandatory")
_GdcHdslConfiguration_ObjectIdentity = ObjectIdentity
gdcHdslConfiguration = _GdcHdslConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3)
)
_GdcHdslE1ConfigTable_Object = MibTable
gdcHdslE1ConfigTable = _GdcHdslE1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gdcHdslE1ConfigTable.setStatus("mandatory")
_GdcHdslE1ConfigEntry_Object = MibTableRow
gdcHdslE1ConfigEntry = _GdcHdslE1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1, 1)
)
gdcHdslE1ConfigEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslE1ConfigIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslE1ConfigEntry.setStatus("mandatory")
_GdcHdslE1ConfigIndex_Type = SCinstance
_GdcHdslE1ConfigIndex_Object = MibTableColumn
gdcHdslE1ConfigIndex = _GdcHdslE1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1, 1, 1),
    _GdcHdslE1ConfigIndex_Type()
)
gdcHdslE1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslE1ConfigIndex.setStatus("mandatory")


class _GdcHdslE1FramingMode_Type(Integer32):
    """Custom type gdcHdslE1FramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framed", 1),
          ("unframed", 2))
    )


_GdcHdslE1FramingMode_Type.__name__ = "Integer32"
_GdcHdslE1FramingMode_Object = MibTableColumn
gdcHdslE1FramingMode = _GdcHdslE1FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1, 1, 2),
    _GdcHdslE1FramingMode_Type()
)
gdcHdslE1FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslE1FramingMode.setStatus("mandatory")


class _GdcHdslE1LineUnit_Type(Integer32):
    """Custom type gdcHdslE1LineUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ilu", 2),
          ("tlu", 1))
    )


_GdcHdslE1LineUnit_Type.__name__ = "Integer32"
_GdcHdslE1LineUnit_Object = MibTableColumn
gdcHdslE1LineUnit = _GdcHdslE1LineUnit_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1, 1, 3),
    _GdcHdslE1LineUnit_Type()
)
gdcHdslE1LineUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslE1LineUnit.setStatus("mandatory")


class _GdcHdslE1LineCoding_Type(Integer32):
    """Custom type gdcHdslE1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 2))
    )


_GdcHdslE1LineCoding_Type.__name__ = "Integer32"
_GdcHdslE1LineCoding_Object = MibTableColumn
gdcHdslE1LineCoding = _GdcHdslE1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 1, 1, 4),
    _GdcHdslE1LineCoding_Type()
)
gdcHdslE1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslE1LineCoding.setStatus("mandatory")
_GdcHdslDteConfigTable_Object = MibTable
gdcHdslDteConfigTable = _GdcHdslDteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gdcHdslDteConfigTable.setStatus("mandatory")
_GdcHdslDteConfigEntry_Object = MibTableRow
gdcHdslDteConfigEntry = _GdcHdslDteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2, 1)
)
gdcHdslDteConfigEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslDteConfigIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslDteConfigEntry.setStatus("mandatory")
_GdcHdslDteConfigIndex_Type = SCinstance
_GdcHdslDteConfigIndex_Object = MibTableColumn
gdcHdslDteConfigIndex = _GdcHdslDteConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2, 1, 1),
    _GdcHdslDteConfigIndex_Type()
)
gdcHdslDteConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteConfigIndex.setStatus("mandatory")


class _GdcHdslDteCtsMode_Type(Integer32):
    """Custom type gdcHdslDteCtsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 1),
          ("onWithRts", 2))
    )


_GdcHdslDteCtsMode_Type.__name__ = "Integer32"
_GdcHdslDteCtsMode_Object = MibTableColumn
gdcHdslDteCtsMode = _GdcHdslDteCtsMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2, 1, 2),
    _GdcHdslDteCtsMode_Type()
)
gdcHdslDteCtsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDteCtsMode.setStatus("mandatory")


class _GdcHdslDteDataRate_Type(Integer32):
    """Custom type gdcHdslDteDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_GdcHdslDteDataRate_Type.__name__ = "Integer32"
_GdcHdslDteDataRate_Object = MibTableColumn
gdcHdslDteDataRate = _GdcHdslDteDataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2, 1, 3),
    _GdcHdslDteDataRate_Type()
)
gdcHdslDteDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDteDataRate.setStatus("mandatory")


class _GdcHdslDteTxClkSource_Type(Integer32):
    """Custom type gdcHdslDteTxClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externalTiming", 1),
          ("internalTiming", 2),
          ("loopTiming", 3))
    )


_GdcHdslDteTxClkSource_Type.__name__ = "Integer32"
_GdcHdslDteTxClkSource_Object = MibTableColumn
gdcHdslDteTxClkSource = _GdcHdslDteTxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 2, 1, 4),
    _GdcHdslDteTxClkSource_Type()
)
gdcHdslDteTxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslDteTxClkSource.setStatus("mandatory")
_GdcHdslT1ConfigTable_Object = MibTable
gdcHdslT1ConfigTable = _GdcHdslT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3)
)
if mibBuilder.loadTexts:
    gdcHdslT1ConfigTable.setStatus("mandatory")
_GdcHdslT1ConfigEntry_Object = MibTableRow
gdcHdslT1ConfigEntry = _GdcHdslT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1)
)
gdcHdslT1ConfigEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslT1ConfigIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslT1ConfigEntry.setStatus("mandatory")
_GdcHdslT1ConfigIndex_Type = SCinstance
_GdcHdslT1ConfigIndex_Object = MibTableColumn
gdcHdslT1ConfigIndex = _GdcHdslT1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 1),
    _GdcHdslT1ConfigIndex_Type()
)
gdcHdslT1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1ConfigIndex.setStatus("mandatory")


class _GdcHdslT1InterfaceType_Type(Integer32):
    """Custom type gdcHdslT1InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 2),
          ("dsx1", 1))
    )


_GdcHdslT1InterfaceType_Type.__name__ = "Integer32"
_GdcHdslT1InterfaceType_Object = MibTableColumn
gdcHdslT1InterfaceType = _GdcHdslT1InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 2),
    _GdcHdslT1InterfaceType_Type()
)
gdcHdslT1InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1InterfaceType.setStatus("mandatory")


class _GdcHdslT1FramingMode_Type(Integer32):
    """Custom type gdcHdslT1FramingMode based on Integer32"""
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
        *(("esf54016", 2),
          ("esfANSI", 1),
          ("sf", 3),
          ("unframed", 4))
    )


_GdcHdslT1FramingMode_Type.__name__ = "Integer32"
_GdcHdslT1FramingMode_Object = MibTableColumn
gdcHdslT1FramingMode = _GdcHdslT1FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 3),
    _GdcHdslT1FramingMode_Type()
)
gdcHdslT1FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1FramingMode.setStatus("mandatory")


class _GdcHdslT1TxPreequalization_Type(Integer32):
    """Custom type gdcHdslT1TxPreequalization based on Integer32"""
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
        *(("preq0to133ft", 1),
          ("preq133to266ft", 2),
          ("preq266to399ft", 3),
          ("preq399to533ft", 4),
          ("preq533to655ft", 5))
    )


_GdcHdslT1TxPreequalization_Type.__name__ = "Integer32"
_GdcHdslT1TxPreequalization_Object = MibTableColumn
gdcHdslT1TxPreequalization = _GdcHdslT1TxPreequalization_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 4),
    _GdcHdslT1TxPreequalization_Type()
)
gdcHdslT1TxPreequalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1TxPreequalization.setStatus("mandatory")


class _GdcHdslT1TxBulidOut_Type(Integer32):
    """Custom type gdcHdslT1TxBulidOut based on Integer32"""
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
        *(("bo0dB", 1),
          ("bo150dB", 3),
          ("bo225dB", 4),
          ("bo75dB", 2))
    )


_GdcHdslT1TxBulidOut_Type.__name__ = "Integer32"
_GdcHdslT1TxBulidOut_Object = MibTableColumn
gdcHdslT1TxBulidOut = _GdcHdslT1TxBulidOut_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 5),
    _GdcHdslT1TxBulidOut_Type()
)
gdcHdslT1TxBulidOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1TxBulidOut.setStatus("mandatory")


class _GdcHdslT1InbandLBType_Type(Integer32):
    """Custom type gdcHdslT1InbandLBType based on Integer32"""
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
          ("lineloopback", 2),
          ("payloadloopback", 3))
    )


_GdcHdslT1InbandLBType_Type.__name__ = "Integer32"
_GdcHdslT1InbandLBType_Object = MibTableColumn
gdcHdslT1InbandLBType = _GdcHdslT1InbandLBType_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 6),
    _GdcHdslT1InbandLBType_Type()
)
gdcHdslT1InbandLBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1InbandLBType.setStatus("mandatory")


class _GdcHdslT1FDLMode_Type(Integer32):
    """Custom type gdcHdslT1FDLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_GdcHdslT1FDLMode_Type.__name__ = "Integer32"
_GdcHdslT1FDLMode_Object = MibTableColumn
gdcHdslT1FDLMode = _GdcHdslT1FDLMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 7),
    _GdcHdslT1FDLMode_Type()
)
gdcHdslT1FDLMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1FDLMode.setStatus("mandatory")


class _GdcHdslT1AISLoopdownTime_Type(Integer32):
    """Custom type gdcHdslT1AISLoopdownTime based on Integer32"""
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
        *(("inhibit", 1),
          ("ld10secs", 3),
          ("ld20secs", 4),
          ("ld40secs", 5),
          ("ld5secs", 2),
          ("ld60secs", 6))
    )


_GdcHdslT1AISLoopdownTime_Type.__name__ = "Integer32"
_GdcHdslT1AISLoopdownTime_Object = MibScalar
gdcHdslT1AISLoopdownTime = _GdcHdslT1AISLoopdownTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 8),
    _GdcHdslT1AISLoopdownTime_Type()
)
gdcHdslT1AISLoopdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1AISLoopdownTime.setStatus("mandatory")


class _GdcHdslT1LineCoding_Type(Integer32):
    """Custom type gdcHdslT1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_GdcHdslT1LineCoding_Type.__name__ = "Integer32"
_GdcHdslT1LineCoding_Object = MibTableColumn
gdcHdslT1LineCoding = _GdcHdslT1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 9),
    _GdcHdslT1LineCoding_Type()
)
gdcHdslT1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1LineCoding.setStatus("mandatory")


class _GdcHdslT1TxClkSource_Type(Integer32):
    """Custom type gdcHdslT1TxClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externalTiming", 1),
          ("internalTiming", 2),
          ("loopTiming", 3))
    )


_GdcHdslT1TxClkSource_Type.__name__ = "Integer32"
_GdcHdslT1TxClkSource_Object = MibTableColumn
gdcHdslT1TxClkSource = _GdcHdslT1TxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 3, 3, 1, 10),
    _GdcHdslT1TxClkSource_Type()
)
gdcHdslT1TxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslT1TxClkSource.setStatus("mandatory")
_GdcHdslDiagnostics_ObjectIdentity = ObjectIdentity
gdcHdslDiagnostics = _GdcHdslDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4)
)
_GdcHdslDiagTable_Object = MibTable
gdcHdslDiagTable = _GdcHdslDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gdcHdslDiagTable.setStatus("mandatory")
_GdcHdslDiagEntry_Object = MibTableRow
gdcHdslDiagEntry = _GdcHdslDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4, 1, 1)
)
gdcHdslDiagEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslDiagIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslDiagEntry.setStatus("mandatory")
_GdcHdslDiagIndex_Type = SCinstance
_GdcHdslDiagIndex_Object = MibTableColumn
gdcHdslDiagIndex = _GdcHdslDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4, 1, 1, 1),
    _GdcHdslDiagIndex_Type()
)
gdcHdslDiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDiagIndex.setStatus("mandatory")


class _GdcHdslLoopback_Type(Integer32):
    """Custom type gdcHdslLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dataLoop", 6),
          ("lineLoop", 2),
          ("lineandlocalLoop", 4),
          ("localLoop", 3),
          ("noLoop", 1),
          ("remoteLoop", 7))
    )


_GdcHdslLoopback_Type.__name__ = "Integer32"
_GdcHdslLoopback_Object = MibTableColumn
gdcHdslLoopback = _GdcHdslLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4, 1, 1, 2),
    _GdcHdslLoopback_Type()
)
gdcHdslLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslLoopback.setStatus("mandatory")


class _GdcHdslBertTest_Type(Integer32):
    """Custom type gdcHdslBertTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1),
          ("reset", 3))
    )


_GdcHdslBertTest_Type.__name__ = "Integer32"
_GdcHdslBertTest_Object = MibTableColumn
gdcHdslBertTest = _GdcHdslBertTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 4, 1, 1, 3),
    _GdcHdslBertTest_Type()
)
gdcHdslBertTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslBertTest.setStatus("mandatory")
_GdcHdslPerformance_ObjectIdentity = ObjectIdentity
gdcHdslPerformance = _GdcHdslPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5)
)
_GdcHdslCurrentTable_Object = MibTable
gdcHdslCurrentTable = _GdcHdslCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    gdcHdslCurrentTable.setStatus("mandatory")
_GdcHdslCurrentEntry_Object = MibTableRow
gdcHdslCurrentEntry = _GdcHdslCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1)
)
gdcHdslCurrentEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslCurrentIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslCurrentEntry.setStatus("mandatory")
_GdcHdslCurrentIndex_Type = SCinstance
_GdcHdslCurrentIndex_Object = MibTableColumn
gdcHdslCurrentIndex = _GdcHdslCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 1),
    _GdcHdslCurrentIndex_Type()
)
gdcHdslCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentIndex.setStatus("mandatory")
_GdcHdslCurrentESs_Type = Gauge32
_GdcHdslCurrentESs_Object = MibTableColumn
gdcHdslCurrentESs = _GdcHdslCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 2),
    _GdcHdslCurrentESs_Type()
)
gdcHdslCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentESs.setStatus("mandatory")
_GdcHdslCurrentSESs_Type = Gauge32
_GdcHdslCurrentSESs_Object = MibTableColumn
gdcHdslCurrentSESs = _GdcHdslCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 3),
    _GdcHdslCurrentSESs_Type()
)
gdcHdslCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentSESs.setStatus("mandatory")
_GdcHdslCurrentUASs_Type = Gauge32
_GdcHdslCurrentUASs_Object = MibTableColumn
gdcHdslCurrentUASs = _GdcHdslCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 4),
    _GdcHdslCurrentUASs_Type()
)
gdcHdslCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentUASs.setStatus("mandatory")
_GdcHdslCurrentDMs_Type = Gauge32
_GdcHdslCurrentDMs_Object = MibTableColumn
gdcHdslCurrentDMs = _GdcHdslCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 5),
    _GdcHdslCurrentDMs_Type()
)
gdcHdslCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentDMs.setStatus("mandatory")
_GdcHdslCurrentFEBEs_Type = Gauge32
_GdcHdslCurrentFEBEs_Object = MibTableColumn
gdcHdslCurrentFEBEs = _GdcHdslCurrentFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 6),
    _GdcHdslCurrentFEBEs_Type()
)
gdcHdslCurrentFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentFEBEs.setStatus("mandatory")


class _GdcHdslCurrentStats_Type(OctetString):
    """Custom type gdcHdslCurrentStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GdcHdslCurrentStats_Type.__name__ = "OctetString"
_GdcHdslCurrentStats_Object = MibTableColumn
gdcHdslCurrentStats = _GdcHdslCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 1, 1, 7),
    _GdcHdslCurrentStats_Type()
)
gdcHdslCurrentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslCurrentStats.setStatus("mandatory")
_GdcHdslIntervalTable_Object = MibTable
gdcHdslIntervalTable = _GdcHdslIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gdcHdslIntervalTable.setStatus("mandatory")
_GdcHdslIntervalEntry_Object = MibTableRow
gdcHdslIntervalEntry = _GdcHdslIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1)
)
gdcHdslIntervalEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslIntervalIndex"),
    (0, "GDCHDSL-MIB", "gdcHdslIntervalNumber"),
)
if mibBuilder.loadTexts:
    gdcHdslIntervalEntry.setStatus("mandatory")
_GdcHdslIntervalIndex_Type = SCinstance
_GdcHdslIntervalIndex_Object = MibTableColumn
gdcHdslIntervalIndex = _GdcHdslIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 1),
    _GdcHdslIntervalIndex_Type()
)
gdcHdslIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalIndex.setStatus("mandatory")


class _GdcHdslIntervalNumber_Type(Integer32):
    """Custom type gdcHdslIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GdcHdslIntervalNumber_Type.__name__ = "Integer32"
_GdcHdslIntervalNumber_Object = MibTableColumn
gdcHdslIntervalNumber = _GdcHdslIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 2),
    _GdcHdslIntervalNumber_Type()
)
gdcHdslIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalNumber.setStatus("mandatory")
_GdcHdslIntervalESs_Type = Gauge32
_GdcHdslIntervalESs_Object = MibTableColumn
gdcHdslIntervalESs = _GdcHdslIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 3),
    _GdcHdslIntervalESs_Type()
)
gdcHdslIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalESs.setStatus("mandatory")
_GdcHdslIntervalSESs_Type = Gauge32
_GdcHdslIntervalSESs_Object = MibTableColumn
gdcHdslIntervalSESs = _GdcHdslIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 4),
    _GdcHdslIntervalSESs_Type()
)
gdcHdslIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalSESs.setStatus("mandatory")
_GdcHdslIntervalUASs_Type = Gauge32
_GdcHdslIntervalUASs_Object = MibTableColumn
gdcHdslIntervalUASs = _GdcHdslIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 5),
    _GdcHdslIntervalUASs_Type()
)
gdcHdslIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalUASs.setStatus("mandatory")
_GdcHdslIntervalDMs_Type = Gauge32
_GdcHdslIntervalDMs_Object = MibTableColumn
gdcHdslIntervalDMs = _GdcHdslIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 6),
    _GdcHdslIntervalDMs_Type()
)
gdcHdslIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalDMs.setStatus("mandatory")
_GdcHdslIntervalFEBEs_Type = Gauge32
_GdcHdslIntervalFEBEs_Object = MibTableColumn
gdcHdslIntervalFEBEs = _GdcHdslIntervalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 7),
    _GdcHdslIntervalFEBEs_Type()
)
gdcHdslIntervalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalFEBEs.setStatus("mandatory")


class _GdcHdslIntervalStats_Type(OctetString):
    """Custom type gdcHdslIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GdcHdslIntervalStats_Type.__name__ = "OctetString"
_GdcHdslIntervalStats_Object = MibTableColumn
gdcHdslIntervalStats = _GdcHdslIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 2, 1, 8),
    _GdcHdslIntervalStats_Type()
)
gdcHdslIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalStats.setStatus("mandatory")
_GdcHdslTotalTable_Object = MibTable
gdcHdslTotalTable = _GdcHdslTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3)
)
if mibBuilder.loadTexts:
    gdcHdslTotalTable.setStatus("mandatory")
_GdcHdslTotalEntry_Object = MibTableRow
gdcHdslTotalEntry = _GdcHdslTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1)
)
gdcHdslTotalEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslTotalIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslTotalEntry.setStatus("mandatory")
_GdcHdslTotalIndex_Type = SCinstance
_GdcHdslTotalIndex_Object = MibTableColumn
gdcHdslTotalIndex = _GdcHdslTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 1),
    _GdcHdslTotalIndex_Type()
)
gdcHdslTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalIndex.setStatus("mandatory")
_GdcHdslTotalESs_Type = Gauge32
_GdcHdslTotalESs_Object = MibTableColumn
gdcHdslTotalESs = _GdcHdslTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 2),
    _GdcHdslTotalESs_Type()
)
gdcHdslTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalESs.setStatus("mandatory")
_GdcHdslTotalSESs_Type = Gauge32
_GdcHdslTotalSESs_Object = MibTableColumn
gdcHdslTotalSESs = _GdcHdslTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 3),
    _GdcHdslTotalSESs_Type()
)
gdcHdslTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalSESs.setStatus("mandatory")
_GdcHdslTotalUASs_Type = Gauge32
_GdcHdslTotalUASs_Object = MibTableColumn
gdcHdslTotalUASs = _GdcHdslTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 4),
    _GdcHdslTotalUASs_Type()
)
gdcHdslTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalUASs.setStatus("mandatory")
_GdcHdslTotalDMs_Type = Gauge32
_GdcHdslTotalDMs_Object = MibTableColumn
gdcHdslTotalDMs = _GdcHdslTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 5),
    _GdcHdslTotalDMs_Type()
)
gdcHdslTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalDMs.setStatus("mandatory")
_GdcHdslTotalFEBEs_Type = Gauge32
_GdcHdslTotalFEBEs_Object = MibTableColumn
gdcHdslTotalFEBEs = _GdcHdslTotalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 6),
    _GdcHdslTotalFEBEs_Type()
)
gdcHdslTotalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalFEBEs.setStatus("mandatory")


class _GdcHdslTotalStats_Type(OctetString):
    """Custom type gdcHdslTotalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GdcHdslTotalStats_Type.__name__ = "OctetString"
_GdcHdslTotalStats_Object = MibTableColumn
gdcHdslTotalStats = _GdcHdslTotalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 3, 1, 7),
    _GdcHdslTotalStats_Type()
)
gdcHdslTotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTotalStats.setStatus("mandatory")
_GdcHdslIntervalMaintenanceTable_Object = MibTable
gdcHdslIntervalMaintenanceTable = _GdcHdslIntervalMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4)
)
if mibBuilder.loadTexts:
    gdcHdslIntervalMaintenanceTable.setStatus("mandatory")
_GdcHdslIntervalMaintenanceEntry_Object = MibTableRow
gdcHdslIntervalMaintenanceEntry = _GdcHdslIntervalMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1)
)
gdcHdslIntervalMaintenanceEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslIntervalMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslIntervalMaintenanceEntry.setStatus("mandatory")
_GdcHdslIntervalMaintenanceIndex_Type = SCinstance
_GdcHdslIntervalMaintenanceIndex_Object = MibTableColumn
gdcHdslIntervalMaintenanceIndex = _GdcHdslIntervalMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1, 1),
    _GdcHdslIntervalMaintenanceIndex_Type()
)
gdcHdslIntervalMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslIntervalMaintenanceIndex.setStatus("mandatory")


class _GdcHdslResetIntervals_Type(Integer32):
    """Custom type gdcHdslResetIntervals based on Integer32"""
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


_GdcHdslResetIntervals_Type.__name__ = "Integer32"
_GdcHdslResetIntervals_Object = MibTableColumn
gdcHdslResetIntervals = _GdcHdslResetIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1, 2),
    _GdcHdslResetIntervals_Type()
)
gdcHdslResetIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslResetIntervals.setStatus("mandatory")


class _GdcHdslNumberofValidIntervals_Type(Integer32):
    """Custom type gdcHdslNumberofValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GdcHdslNumberofValidIntervals_Type.__name__ = "Integer32"
_GdcHdslNumberofValidIntervals_Object = MibTableColumn
gdcHdslNumberofValidIntervals = _GdcHdslNumberofValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1, 3),
    _GdcHdslNumberofValidIntervals_Type()
)
gdcHdslNumberofValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslNumberofValidIntervals.setStatus("mandatory")


class _GdcHdslResetMajorAlarm_Type(Integer32):
    """Custom type gdcHdslResetMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarm", 1),
          ("normalAlarm", 2))
    )


_GdcHdslResetMajorAlarm_Type.__name__ = "Integer32"
_GdcHdslResetMajorAlarm_Object = MibTableColumn
gdcHdslResetMajorAlarm = _GdcHdslResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1, 4),
    _GdcHdslResetMajorAlarm_Type()
)
gdcHdslResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslResetMajorAlarm.setStatus("mandatory")


class _GdcHdslResetMinorAlarm_Type(Integer32):
    """Custom type gdcHdslResetMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarm", 1),
          ("normalAlarm", 2))
    )


_GdcHdslResetMinorAlarm_Type.__name__ = "Integer32"
_GdcHdslResetMinorAlarm_Object = MibTableColumn
gdcHdslResetMinorAlarm = _GdcHdslResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 4, 1, 5),
    _GdcHdslResetMinorAlarm_Type()
)
gdcHdslResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslResetMinorAlarm.setStatus("mandatory")
_GdcHdslT1CurrentTable_Object = MibTable
gdcHdslT1CurrentTable = _GdcHdslT1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 5)
)
if mibBuilder.loadTexts:
    gdcHdslT1CurrentTable.setStatus("mandatory")
_GdcHdslT1CurrentEntry_Object = MibTableRow
gdcHdslT1CurrentEntry = _GdcHdslT1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 5, 1)
)
gdcHdslT1CurrentEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslT1CurrentIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslT1CurrentEntry.setStatus("mandatory")
_GdcHdslT1CurrentIndex_Type = SCinstance
_GdcHdslT1CurrentIndex_Object = MibTableColumn
gdcHdslT1CurrentIndex = _GdcHdslT1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 5, 1, 1),
    _GdcHdslT1CurrentIndex_Type()
)
gdcHdslT1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1CurrentIndex.setStatus("mandatory")


class _GdcHdslT1CurrentStats_Type(OctetString):
    """Custom type gdcHdslT1CurrentStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslT1CurrentStats_Type.__name__ = "OctetString"
_GdcHdslT1CurrentStats_Object = MibTableColumn
gdcHdslT1CurrentStats = _GdcHdslT1CurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 5, 1, 2),
    _GdcHdslT1CurrentStats_Type()
)
gdcHdslT1CurrentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1CurrentStats.setStatus("mandatory")
_GdcHdslT1IntervalTable_Object = MibTable
gdcHdslT1IntervalTable = _GdcHdslT1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 6)
)
if mibBuilder.loadTexts:
    gdcHdslT1IntervalTable.setStatus("mandatory")
_GdcHdslT1IntervalEntry_Object = MibTableRow
gdcHdslT1IntervalEntry = _GdcHdslT1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 6, 1)
)
gdcHdslT1IntervalEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslT1IntervalIndex"),
    (0, "GDCHDSL-MIB", "gdcHdslT1IntervalNumber"),
)
if mibBuilder.loadTexts:
    gdcHdslT1IntervalEntry.setStatus("mandatory")
_GdcHdslT1IntervalIndex_Type = SCinstance
_GdcHdslT1IntervalIndex_Object = MibTableColumn
gdcHdslT1IntervalIndex = _GdcHdslT1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 6, 1, 1),
    _GdcHdslT1IntervalIndex_Type()
)
gdcHdslT1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1IntervalIndex.setStatus("mandatory")


class _GdcHdslT1IntervalNumber_Type(Integer32):
    """Custom type gdcHdslT1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GdcHdslT1IntervalNumber_Type.__name__ = "Integer32"
_GdcHdslT1IntervalNumber_Object = MibTableColumn
gdcHdslT1IntervalNumber = _GdcHdslT1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 6, 1, 2),
    _GdcHdslT1IntervalNumber_Type()
)
gdcHdslT1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1IntervalNumber.setStatus("mandatory")


class _GdcHdslT1IntervalStats_Type(OctetString):
    """Custom type gdcHdslT1IntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslT1IntervalStats_Type.__name__ = "OctetString"
_GdcHdslT1IntervalStats_Object = MibTableColumn
gdcHdslT1IntervalStats = _GdcHdslT1IntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 6, 1, 3),
    _GdcHdslT1IntervalStats_Type()
)
gdcHdslT1IntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1IntervalStats.setStatus("mandatory")
_GdcHdslT1TotalTable_Object = MibTable
gdcHdslT1TotalTable = _GdcHdslT1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 7)
)
if mibBuilder.loadTexts:
    gdcHdslT1TotalTable.setStatus("mandatory")
_GdcHdslT1TotalEntry_Object = MibTableRow
gdcHdslT1TotalEntry = _GdcHdslT1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 7, 1)
)
gdcHdslT1TotalEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslT1TotalIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslT1TotalEntry.setStatus("mandatory")
_GdcHdslT1TotalIndex_Type = SCinstance
_GdcHdslT1TotalIndex_Object = MibTableColumn
gdcHdslT1TotalIndex = _GdcHdslT1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 7, 1, 1),
    _GdcHdslT1TotalIndex_Type()
)
gdcHdslT1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1TotalIndex.setStatus("mandatory")


class _GdcHdslT1TotalStats_Type(OctetString):
    """Custom type gdcHdslT1TotalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_GdcHdslT1TotalStats_Type.__name__ = "OctetString"
_GdcHdslT1TotalStats_Object = MibTableColumn
gdcHdslT1TotalStats = _GdcHdslT1TotalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 5, 7, 1, 2),
    _GdcHdslT1TotalStats_Type()
)
gdcHdslT1TotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslT1TotalStats.setStatus("mandatory")
_GdcHdslStatus_ObjectIdentity = ObjectIdentity
gdcHdslStatus = _GdcHdslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6)
)
_GdcHdslLoopStatusTable_Object = MibTable
gdcHdslLoopStatusTable = _GdcHdslLoopStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    gdcHdslLoopStatusTable.setStatus("mandatory")
_GdcHdslLoopStatusEntry_Object = MibTableRow
gdcHdslLoopStatusEntry = _GdcHdslLoopStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1)
)
gdcHdslLoopStatusEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslLoopStatusLineIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslLoopStatusEntry.setStatus("mandatory")
_GdcHdslLoopStatusLineIndex_Type = SCinstance
_GdcHdslLoopStatusLineIndex_Object = MibTableColumn
gdcHdslLoopStatusLineIndex = _GdcHdslLoopStatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 1),
    _GdcHdslLoopStatusLineIndex_Type()
)
gdcHdslLoopStatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopStatusLineIndex.setStatus("mandatory")


class _GdcHdslLoopStartUp_Type(Integer32):
    """Custom type gdcHdslLoopStartUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("norm", 1),
          ("start", 2))
    )


_GdcHdslLoopStartUp_Type.__name__ = "Integer32"
_GdcHdslLoopStartUp_Object = MibTableColumn
gdcHdslLoopStartUp = _GdcHdslLoopStartUp_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 2),
    _GdcHdslLoopStartUp_Type()
)
gdcHdslLoopStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslLoopStartUp.setStatus("mandatory")


class _GdcHdslLoopTipRingReversalMode_Type(Integer32):
    """Custom type gdcHdslLoopTipRingReversalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reversed", 2))
    )


_GdcHdslLoopTipRingReversalMode_Type.__name__ = "Integer32"
_GdcHdslLoopTipRingReversalMode_Object = MibTableColumn
gdcHdslLoopTipRingReversalMode = _GdcHdslLoopTipRingReversalMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 3),
    _GdcHdslLoopTipRingReversalMode_Type()
)
gdcHdslLoopTipRingReversalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopTipRingReversalMode.setStatus("mandatory")


class _GdcHdslLoopSignaltoNoiseMargin_Type(Integer32):
    """Custom type gdcHdslLoopSignaltoNoiseMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GdcHdslLoopSignaltoNoiseMargin_Type.__name__ = "Integer32"
_GdcHdslLoopSignaltoNoiseMargin_Object = MibTableColumn
gdcHdslLoopSignaltoNoiseMargin = _GdcHdslLoopSignaltoNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 4),
    _GdcHdslLoopSignaltoNoiseMargin_Type()
)
gdcHdslLoopSignaltoNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopSignaltoNoiseMargin.setStatus("mandatory")


class _GdcHdslLoopSNFrac_Type(Integer32):
    """Custom type gdcHdslLoopSNFrac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_GdcHdslLoopSNFrac_Type.__name__ = "Integer32"
_GdcHdslLoopSNFrac_Object = MibTableColumn
gdcHdslLoopSNFrac = _GdcHdslLoopSNFrac_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 5),
    _GdcHdslLoopSNFrac_Type()
)
gdcHdslLoopSNFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopSNFrac.setStatus("mandatory")


class _GdcHdslLoopSNAttenSense_Type(Integer32):
    """Custom type gdcHdslLoopSNAttenSense based on Integer32"""
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


_GdcHdslLoopSNAttenSense_Type.__name__ = "Integer32"
_GdcHdslLoopSNAttenSense_Object = MibTableColumn
gdcHdslLoopSNAttenSense = _GdcHdslLoopSNAttenSense_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 6),
    _GdcHdslLoopSNAttenSense_Type()
)
gdcHdslLoopSNAttenSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopSNAttenSense.setStatus("mandatory")


class _GdcHdslLoopPulseAtten_Type(Integer32):
    """Custom type gdcHdslLoopPulseAtten based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GdcHdslLoopPulseAtten_Type.__name__ = "Integer32"
_GdcHdslLoopPulseAtten_Object = MibTableColumn
gdcHdslLoopPulseAtten = _GdcHdslLoopPulseAtten_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 7),
    _GdcHdslLoopPulseAtten_Type()
)
gdcHdslLoopPulseAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopPulseAtten.setStatus("mandatory")


class _GdcHdslLoopPulseAttenFrac_Type(Integer32):
    """Custom type gdcHdslLoopPulseAttenFrac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_GdcHdslLoopPulseAttenFrac_Type.__name__ = "Integer32"
_GdcHdslLoopPulseAttenFrac_Object = MibTableColumn
gdcHdslLoopPulseAttenFrac = _GdcHdslLoopPulseAttenFrac_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 8),
    _GdcHdslLoopPulseAttenFrac_Type()
)
gdcHdslLoopPulseAttenFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopPulseAttenFrac.setStatus("mandatory")


class _GdcHdslLoopGain_Type(Integer32):
    """Custom type gdcHdslLoopGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1),
          ("ok", 3))
    )


_GdcHdslLoopGain_Type.__name__ = "Integer32"
_GdcHdslLoopGain_Object = MibTableColumn
gdcHdslLoopGain = _GdcHdslLoopGain_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 9),
    _GdcHdslLoopGain_Type()
)
gdcHdslLoopGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopGain.setStatus("mandatory")


class _GdcHdslLoopExchange_Type(Integer32):
    """Custom type gdcHdslLoopExchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exchange", 2),
          ("norm", 1))
    )


_GdcHdslLoopExchange_Type.__name__ = "Integer32"
_GdcHdslLoopExchange_Object = MibTableColumn
gdcHdslLoopExchange = _GdcHdslLoopExchange_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 1, 1, 10),
    _GdcHdslLoopExchange_Type()
)
gdcHdslLoopExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslLoopExchange.setStatus("mandatory")
_GdcHdslDteStatusTable_Object = MibTable
gdcHdslDteStatusTable = _GdcHdslDteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2)
)
if mibBuilder.loadTexts:
    gdcHdslDteStatusTable.setStatus("mandatory")
_GdcHdslDteStatusEntry_Object = MibTableRow
gdcHdslDteStatusEntry = _GdcHdslDteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1)
)
gdcHdslDteStatusEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslDteStatusIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslDteStatusEntry.setStatus("mandatory")
_GdcHdslDteStatusIndex_Type = SCinstance
_GdcHdslDteStatusIndex_Object = MibTableColumn
gdcHdslDteStatusIndex = _GdcHdslDteStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 1),
    _GdcHdslDteStatusIndex_Type()
)
gdcHdslDteStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteStatusIndex.setStatus("mandatory")


class _GdcHdslDteDTRstatus_Type(Integer32):
    """Custom type gdcHdslDteDTRstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GdcHdslDteDTRstatus_Type.__name__ = "Integer32"
_GdcHdslDteDTRstatus_Object = MibTableColumn
gdcHdslDteDTRstatus = _GdcHdslDteDTRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 2),
    _GdcHdslDteDTRstatus_Type()
)
gdcHdslDteDTRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteDTRstatus.setStatus("mandatory")


class _GdcHdslDteDCDstatus_Type(Integer32):
    """Custom type gdcHdslDteDCDstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GdcHdslDteDCDstatus_Type.__name__ = "Integer32"
_GdcHdslDteDCDstatus_Object = MibTableColumn
gdcHdslDteDCDstatus = _GdcHdslDteDCDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 3),
    _GdcHdslDteDCDstatus_Type()
)
gdcHdslDteDCDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteDCDstatus.setStatus("mandatory")


class _GdcHdslDteRTSstatus_Type(Integer32):
    """Custom type gdcHdslDteRTSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GdcHdslDteRTSstatus_Type.__name__ = "Integer32"
_GdcHdslDteRTSstatus_Object = MibTableColumn
gdcHdslDteRTSstatus = _GdcHdslDteRTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 4),
    _GdcHdslDteRTSstatus_Type()
)
gdcHdslDteRTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteRTSstatus.setStatus("mandatory")


class _GdcHdslDteDSRstatus_Type(Integer32):
    """Custom type gdcHdslDteDSRstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GdcHdslDteDSRstatus_Type.__name__ = "Integer32"
_GdcHdslDteDSRstatus_Object = MibTableColumn
gdcHdslDteDSRstatus = _GdcHdslDteDSRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 5),
    _GdcHdslDteDSRstatus_Type()
)
gdcHdslDteDSRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteDSRstatus.setStatus("mandatory")


class _GdcHdslDteStatus_Type(OctetString):
    """Custom type gdcHdslDteStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GdcHdslDteStatus_Type.__name__ = "OctetString"
_GdcHdslDteStatus_Object = MibTableColumn
gdcHdslDteStatus = _GdcHdslDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 6, 2, 1, 6),
    _GdcHdslDteStatus_Type()
)
gdcHdslDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDteStatus.setStatus("mandatory")
_GdcHdslDiagnosticResults_ObjectIdentity = ObjectIdentity
gdcHdslDiagnosticResults = _GdcHdslDiagnosticResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7)
)
_GdcHdslDiagResultsTable_Object = MibTable
gdcHdslDiagResultsTable = _GdcHdslDiagResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1)
)
if mibBuilder.loadTexts:
    gdcHdslDiagResultsTable.setStatus("mandatory")
_GdcHdslDiagResultsEntry_Object = MibTableRow
gdcHdslDiagResultsEntry = _GdcHdslDiagResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1)
)
gdcHdslDiagResultsEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "gdcHdslDiagResultsIndex"),
)
if mibBuilder.loadTexts:
    gdcHdslDiagResultsEntry.setStatus("mandatory")
_GdcHdslDiagResultsIndex_Type = SCinstance
_GdcHdslDiagResultsIndex_Object = MibTableColumn
gdcHdslDiagResultsIndex = _GdcHdslDiagResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1, 1),
    _GdcHdslDiagResultsIndex_Type()
)
gdcHdslDiagResultsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDiagResultsIndex.setStatus("mandatory")


class _GdcHdslTestExecutionStatus_Type(Integer32):
    """Custom type gdcHdslTestExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("notInSync", 2))
    )


_GdcHdslTestExecutionStatus_Type.__name__ = "Integer32"
_GdcHdslTestExecutionStatus_Object = MibTableColumn
gdcHdslTestExecutionStatus = _GdcHdslTestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1, 2),
    _GdcHdslTestExecutionStatus_Type()
)
gdcHdslTestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslTestExecutionStatus.setStatus("mandatory")


class _GdcHdslDiagResultErr_Type(Integer32):
    """Custom type gdcHdslDiagResultErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GdcHdslDiagResultErr_Type.__name__ = "Integer32"
_GdcHdslDiagResultErr_Object = MibTableColumn
gdcHdslDiagResultErr = _GdcHdslDiagResultErr_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1, 3),
    _GdcHdslDiagResultErr_Type()
)
gdcHdslDiagResultErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDiagResultErr.setStatus("mandatory")


class _GdcHdslDiagResultInterval_Type(Integer32):
    """Custom type gdcHdslDiagResultInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GdcHdslDiagResultInterval_Type.__name__ = "Integer32"
_GdcHdslDiagResultInterval_Object = MibTableColumn
gdcHdslDiagResultInterval = _GdcHdslDiagResultInterval_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1, 4),
    _GdcHdslDiagResultInterval_Type()
)
gdcHdslDiagResultInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslDiagResultInterval.setStatus("mandatory")


class _GdcHdslV54RDLTest_Type(Integer32):
    """Custom type gdcHdslV54RDLTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInV54Test", 1),
          ("txV54Test", 2))
    )


_GdcHdslV54RDLTest_Type.__name__ = "Integer32"
_GdcHdslV54RDLTest_Object = MibTableColumn
gdcHdslV54RDLTest = _GdcHdslV54RDLTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 7, 1, 1, 5),
    _GdcHdslV54RDLTest_Type()
)
gdcHdslV54RDLTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcHdslV54RDLTest.setStatus("mandatory")
_GdcFractional_ObjectIdentity = ObjectIdentity
gdcFractional = _GdcFractional_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8)
)
_HdslFracTable_Object = MibTable
hdslFracTable = _HdslFracTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hdslFracTable.setStatus("mandatory")
_HdslFracEntry_Object = MibTableRow
hdslFracEntry = _HdslFracEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1, 1)
)
hdslFracEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "hdslFracIndex"),
)
if mibBuilder.loadTexts:
    hdslFracEntry.setStatus("mandatory")
_HdslFracIndex_Type = SCinstance
_HdslFracIndex_Object = MibTableColumn
hdslFracIndex = _HdslFracIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1, 1, 1),
    _HdslFracIndex_Type()
)
hdslFracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslFracIndex.setStatus("mandatory")
_Channelmapping_Type = Integer32
_Channelmapping_Object = MibTableColumn
channelmapping = _Channelmapping_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1, 1, 2),
    _Channelmapping_Type()
)
channelmapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelmapping.setStatus("mandatory")


class _GdcHdslHighway_Type(Integer32):
    """Custom type gdcHdslHighway based on Integer32"""
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


_GdcHdslHighway_Type.__name__ = "Integer32"
_GdcHdslHighway_Object = MibTableColumn
gdcHdslHighway = _GdcHdslHighway_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1, 1, 3),
    _GdcHdslHighway_Type()
)
gdcHdslHighway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslHighway.setStatus("mandatory")


class _GdcHdslTimeSlot16_Type(Integer32):
    """Custom type gdcHdslTimeSlot16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("skipped", 2),
          ("used", 1))
    )


_GdcHdslTimeSlot16_Type.__name__ = "Integer32"
_GdcHdslTimeSlot16_Object = MibTableColumn
gdcHdslTimeSlot16 = _GdcHdslTimeSlot16_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 8, 1, 1, 4),
    _GdcHdslTimeSlot16_Type()
)
gdcHdslTimeSlot16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcHdslTimeSlot16.setStatus("mandatory")
_GdcHdslAlarmThresholds_ObjectIdentity = ObjectIdentity
gdcHdslAlarmThresholds = _GdcHdslAlarmThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9)
)
_HdslAlarmConfigTable_Object = MibTable
hdslAlarmConfigTable = _HdslAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hdslAlarmConfigTable.setStatus("mandatory")
_HdslAlarmConfigEntry_Object = MibTableRow
hdslAlarmConfigEntry = _HdslAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9, 1, 1)
)
hdslAlarmConfigEntry.setIndexNames(
    (0, "GDCHDSL-MIB", "hdslAlarmConfigIndex"),
    (0, "GDCHDSL-MIB", "hdslAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    hdslAlarmConfigEntry.setStatus("mandatory")
_HdslAlarmConfigIndex_Type = SCinstance
_HdslAlarmConfigIndex_Object = MibTableColumn
hdslAlarmConfigIndex = _HdslAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9, 1, 1, 1),
    _HdslAlarmConfigIndex_Type()
)
hdslAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslAlarmConfigIndex.setStatus("mandatory")
_HdslAlarmConfigIdentifier_Type = ObjectIdentifier
_HdslAlarmConfigIdentifier_Object = MibTableColumn
hdslAlarmConfigIdentifier = _HdslAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9, 1, 1, 2),
    _HdslAlarmConfigIdentifier_Type()
)
hdslAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdslAlarmConfigIdentifier.setStatus("mandatory")


class _HdslAlarmThreshold_Type(Integer32):
    """Custom type hdslAlarmThreshold based on Integer32"""
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
        *(("thres1E04", 1),
          ("thres1E05", 2),
          ("thres1E06", 3),
          ("thres1E07", 4),
          ("thres1E08", 5))
    )


_HdslAlarmThreshold_Type.__name__ = "Integer32"
_HdslAlarmThreshold_Object = MibTableColumn
hdslAlarmThreshold = _HdslAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 11, 1, 9, 1, 1, 3),
    _HdslAlarmThreshold_Type()
)
hdslAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdslAlarmThreshold.setStatus("mandatory")
_Hdsl700G2_ObjectIdentity = ObjectIdentity
hdsl700G2 = _Hdsl700G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 2)
)
_Hdsl700G3_ObjectIdentity = ObjectIdentity
hdsl700G3 = _Hdsl700G3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 3)
)
_Hdsl730D1_ObjectIdentity = ObjectIdentity
hdsl730D1 = _Hdsl730D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 4)
)
_Hdsl730D2_ObjectIdentity = ObjectIdentity
hdsl730D2 = _Hdsl730D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 5)
)
_Hdsl720G1_ObjectIdentity = ObjectIdentity
hdsl720G1 = _Hdsl720G1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 6)
)
_Hdsl720G2_ObjectIdentity = ObjectIdentity
hdsl720G2 = _Hdsl720G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 7)
)
_Hdsl702G2_ObjectIdentity = ObjectIdentity
hdsl702G2 = _Hdsl702G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 8)
)
_Hdsl710D2_ObjectIdentity = ObjectIdentity
hdsl710D2 = _Hdsl710D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 9)
)
_Hdsl700G2RP_ObjectIdentity = ObjectIdentity
hdsl700G2RP = _Hdsl700G2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 10)
)
_Hdsl710D2RP_ObjectIdentity = ObjectIdentity
hdsl710D2RP = _Hdsl710D2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 11)
)
_Hdsl720G2RP_ObjectIdentity = ObjectIdentity
hdsl720G2RP = _Hdsl720G2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 12)
)
_Hdsl730D2RP_ObjectIdentity = ObjectIdentity
hdsl730D2RP = _Hdsl730D2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 13)
)
_Hdsl701T2_ObjectIdentity = ObjectIdentity
hdsl701T2 = _Hdsl701T2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 14)
)
_Hdsl701T2RP_ObjectIdentity = ObjectIdentity
hdsl701T2RP = _Hdsl701T2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 15)
)
_Hdsl721T1_ObjectIdentity = ObjectIdentity
hdsl721T1 = _Hdsl721T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 16)
)
_Hdsl721T2_ObjectIdentity = ObjectIdentity
hdsl721T2 = _Hdsl721T2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 17)
)
_Hdsl721T2RP_ObjectIdentity = ObjectIdentity
hdsl721T2RP = _Hdsl721T2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 18)
)
_Hdsl731D1_ObjectIdentity = ObjectIdentity
hdsl731D1 = _Hdsl731D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 19)
)
_Hdsl731D2_ObjectIdentity = ObjectIdentity
hdsl731D2 = _Hdsl731D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 20)
)
_Hdsl731D2RP_ObjectIdentity = ObjectIdentity
hdsl731D2RP = _Hdsl731D2RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 21)
)
_Hdsl700AG2_ObjectIdentity = ObjectIdentity
hdsl700AG2 = _Hdsl700AG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 22)
)
_Hdsl700AG2NZ_ObjectIdentity = ObjectIdentity
hdsl700AG2NZ = _Hdsl700AG2NZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 23)
)
_HdslGT1030_ObjectIdentity = ObjectIdentity
hdslGT1030 = _HdslGT1030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 25)
)
_HdslGT2030_ObjectIdentity = ObjectIdentity
hdslGT2030 = _HdslGT2030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 26)
)
_Uas7722_ObjectIdentity = ObjectIdentity
uas7722 = _Uas7722_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 27)
)
_HdslGT1020_ObjectIdentity = ObjectIdentity
hdslGT1020 = _HdslGT1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 28)
)
_HdslGT2020_ObjectIdentity = ObjectIdentity
hdslGT2020 = _HdslGT2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 29)
)
_Hdsl711D2_ObjectIdentity = ObjectIdentity
hdsl711D2 = _Hdsl711D2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 11, 30)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCHDSL-MIB",
    **{"gdc": gdc,
       "hdsl": hdsl,
       "gdcHdslSystem": gdcHdslSystem,
       "gdcHdslVersion": gdcHdslVersion,
       "gdcHdslSystemMIBversion": gdcHdslSystemMIBversion,
       "gdcHdslVersionTable": gdcHdslVersionTable,
       "gdcHdslVersionEntry": gdcHdslVersionEntry,
       "gdcHdslVersionIndex": gdcHdslVersionIndex,
       "gdcHdslFirmwareRev": gdcHdslFirmwareRev,
       "gdcHdslModelNumber": gdcHdslModelNumber,
       "gdcHdslDownloadTable": gdcHdslDownloadTable,
       "gdcHdslDownloadEntry": gdcHdslDownloadEntry,
       "gdcHdslDownloadIndex": gdcHdslDownloadIndex,
       "gdcHdslActiveFirmwareRev": gdcHdslActiveFirmwareRev,
       "gdcHdslStoredFirmwareRev": gdcHdslStoredFirmwareRev,
       "gdcHdslStoredFirmwareStatus": gdcHdslStoredFirmwareStatus,
       "gdcHdslSwitchActiveFirmware": gdcHdslSwitchActiveFirmware,
       "gdcHdslDownloadingMode": gdcHdslDownloadingMode,
       "gdcHdslEraseFlash": gdcHdslEraseFlash,
       "gdcHdslMaintenance": gdcHdslMaintenance,
       "gdcHdslMaintenanceTable": gdcHdslMaintenanceTable,
       "gdcHdslMaintenanceEntry": gdcHdslMaintenanceEntry,
       "gdcHdslMaintenanceLineIndex": gdcHdslMaintenanceLineIndex,
       "gdcHdslSoftReset": gdcHdslSoftReset,
       "gdcHdslConfigMode": gdcHdslConfigMode,
       "gdcHdslSysUpTime": gdcHdslSysUpTime,
       "gdcHdslUnitType": gdcHdslUnitType,
       "gdcHdslDefaultInit": gdcHdslDefaultInit,
       "gdcHdslDataType": gdcHdslDataType,
       "gdcHdslLoopProvision": gdcHdslLoopProvision,
       "gdcHdslNumberofLoops": gdcHdslNumberofLoops,
       "gdcHdslFrontPanel": gdcHdslFrontPanel,
       "gdcHdslRoutingConfig": gdcHdslRoutingConfig,
       "gdcHdslPrivateStorage1": gdcHdslPrivateStorage1,
       "gdcHdslPrivateStorage2": gdcHdslPrivateStorage2,
       "gdcHdslPrivateStorage3": gdcHdslPrivateStorage3,
       "gdcHdslLedStatus": gdcHdslLedStatus,
       "fracExecution": fracExecution,
       "gdcHdslAlarmStatus": gdcHdslAlarmStatus,
       "gdcHdslV54Config": gdcHdslV54Config,
       "gdcHdslFPRDLConfig": gdcHdslFPRDLConfig,
       "gdcHdslRLTimeOut": gdcHdslRLTimeOut,
       "gdcHdslRPEnable": gdcHdslRPEnable,
       "gdcHdslLedStatus1": gdcHdslLedStatus1,
       "gdcHdslConfiguration": gdcHdslConfiguration,
       "gdcHdslE1ConfigTable": gdcHdslE1ConfigTable,
       "gdcHdslE1ConfigEntry": gdcHdslE1ConfigEntry,
       "gdcHdslE1ConfigIndex": gdcHdslE1ConfigIndex,
       "gdcHdslE1FramingMode": gdcHdslE1FramingMode,
       "gdcHdslE1LineUnit": gdcHdslE1LineUnit,
       "gdcHdslE1LineCoding": gdcHdslE1LineCoding,
       "gdcHdslDteConfigTable": gdcHdslDteConfigTable,
       "gdcHdslDteConfigEntry": gdcHdslDteConfigEntry,
       "gdcHdslDteConfigIndex": gdcHdslDteConfigIndex,
       "gdcHdslDteCtsMode": gdcHdslDteCtsMode,
       "gdcHdslDteDataRate": gdcHdslDteDataRate,
       "gdcHdslDteTxClkSource": gdcHdslDteTxClkSource,
       "gdcHdslT1ConfigTable": gdcHdslT1ConfigTable,
       "gdcHdslT1ConfigEntry": gdcHdslT1ConfigEntry,
       "gdcHdslT1ConfigIndex": gdcHdslT1ConfigIndex,
       "gdcHdslT1InterfaceType": gdcHdslT1InterfaceType,
       "gdcHdslT1FramingMode": gdcHdslT1FramingMode,
       "gdcHdslT1TxPreequalization": gdcHdslT1TxPreequalization,
       "gdcHdslT1TxBulidOut": gdcHdslT1TxBulidOut,
       "gdcHdslT1InbandLBType": gdcHdslT1InbandLBType,
       "gdcHdslT1FDLMode": gdcHdslT1FDLMode,
       "gdcHdslT1AISLoopdownTime": gdcHdslT1AISLoopdownTime,
       "gdcHdslT1LineCoding": gdcHdslT1LineCoding,
       "gdcHdslT1TxClkSource": gdcHdslT1TxClkSource,
       "gdcHdslDiagnostics": gdcHdslDiagnostics,
       "gdcHdslDiagTable": gdcHdslDiagTable,
       "gdcHdslDiagEntry": gdcHdslDiagEntry,
       "gdcHdslDiagIndex": gdcHdslDiagIndex,
       "gdcHdslLoopback": gdcHdslLoopback,
       "gdcHdslBertTest": gdcHdslBertTest,
       "gdcHdslPerformance": gdcHdslPerformance,
       "gdcHdslCurrentTable": gdcHdslCurrentTable,
       "gdcHdslCurrentEntry": gdcHdslCurrentEntry,
       "gdcHdslCurrentIndex": gdcHdslCurrentIndex,
       "gdcHdslCurrentESs": gdcHdslCurrentESs,
       "gdcHdslCurrentSESs": gdcHdslCurrentSESs,
       "gdcHdslCurrentUASs": gdcHdslCurrentUASs,
       "gdcHdslCurrentDMs": gdcHdslCurrentDMs,
       "gdcHdslCurrentFEBEs": gdcHdslCurrentFEBEs,
       "gdcHdslCurrentStats": gdcHdslCurrentStats,
       "gdcHdslIntervalTable": gdcHdslIntervalTable,
       "gdcHdslIntervalEntry": gdcHdslIntervalEntry,
       "gdcHdslIntervalIndex": gdcHdslIntervalIndex,
       "gdcHdslIntervalNumber": gdcHdslIntervalNumber,
       "gdcHdslIntervalESs": gdcHdslIntervalESs,
       "gdcHdslIntervalSESs": gdcHdslIntervalSESs,
       "gdcHdslIntervalUASs": gdcHdslIntervalUASs,
       "gdcHdslIntervalDMs": gdcHdslIntervalDMs,
       "gdcHdslIntervalFEBEs": gdcHdslIntervalFEBEs,
       "gdcHdslIntervalStats": gdcHdslIntervalStats,
       "gdcHdslTotalTable": gdcHdslTotalTable,
       "gdcHdslTotalEntry": gdcHdslTotalEntry,
       "gdcHdslTotalIndex": gdcHdslTotalIndex,
       "gdcHdslTotalESs": gdcHdslTotalESs,
       "gdcHdslTotalSESs": gdcHdslTotalSESs,
       "gdcHdslTotalUASs": gdcHdslTotalUASs,
       "gdcHdslTotalDMs": gdcHdslTotalDMs,
       "gdcHdslTotalFEBEs": gdcHdslTotalFEBEs,
       "gdcHdslTotalStats": gdcHdslTotalStats,
       "gdcHdslIntervalMaintenanceTable": gdcHdslIntervalMaintenanceTable,
       "gdcHdslIntervalMaintenanceEntry": gdcHdslIntervalMaintenanceEntry,
       "gdcHdslIntervalMaintenanceIndex": gdcHdslIntervalMaintenanceIndex,
       "gdcHdslResetIntervals": gdcHdslResetIntervals,
       "gdcHdslNumberofValidIntervals": gdcHdslNumberofValidIntervals,
       "gdcHdslResetMajorAlarm": gdcHdslResetMajorAlarm,
       "gdcHdslResetMinorAlarm": gdcHdslResetMinorAlarm,
       "gdcHdslT1CurrentTable": gdcHdslT1CurrentTable,
       "gdcHdslT1CurrentEntry": gdcHdslT1CurrentEntry,
       "gdcHdslT1CurrentIndex": gdcHdslT1CurrentIndex,
       "gdcHdslT1CurrentStats": gdcHdslT1CurrentStats,
       "gdcHdslT1IntervalTable": gdcHdslT1IntervalTable,
       "gdcHdslT1IntervalEntry": gdcHdslT1IntervalEntry,
       "gdcHdslT1IntervalIndex": gdcHdslT1IntervalIndex,
       "gdcHdslT1IntervalNumber": gdcHdslT1IntervalNumber,
       "gdcHdslT1IntervalStats": gdcHdslT1IntervalStats,
       "gdcHdslT1TotalTable": gdcHdslT1TotalTable,
       "gdcHdslT1TotalEntry": gdcHdslT1TotalEntry,
       "gdcHdslT1TotalIndex": gdcHdslT1TotalIndex,
       "gdcHdslT1TotalStats": gdcHdslT1TotalStats,
       "gdcHdslStatus": gdcHdslStatus,
       "gdcHdslLoopStatusTable": gdcHdslLoopStatusTable,
       "gdcHdslLoopStatusEntry": gdcHdslLoopStatusEntry,
       "gdcHdslLoopStatusLineIndex": gdcHdslLoopStatusLineIndex,
       "gdcHdslLoopStartUp": gdcHdslLoopStartUp,
       "gdcHdslLoopTipRingReversalMode": gdcHdslLoopTipRingReversalMode,
       "gdcHdslLoopSignaltoNoiseMargin": gdcHdslLoopSignaltoNoiseMargin,
       "gdcHdslLoopSNFrac": gdcHdslLoopSNFrac,
       "gdcHdslLoopSNAttenSense": gdcHdslLoopSNAttenSense,
       "gdcHdslLoopPulseAtten": gdcHdslLoopPulseAtten,
       "gdcHdslLoopPulseAttenFrac": gdcHdslLoopPulseAttenFrac,
       "gdcHdslLoopGain": gdcHdslLoopGain,
       "gdcHdslLoopExchange": gdcHdslLoopExchange,
       "gdcHdslDteStatusTable": gdcHdslDteStatusTable,
       "gdcHdslDteStatusEntry": gdcHdslDteStatusEntry,
       "gdcHdslDteStatusIndex": gdcHdslDteStatusIndex,
       "gdcHdslDteDTRstatus": gdcHdslDteDTRstatus,
       "gdcHdslDteDCDstatus": gdcHdslDteDCDstatus,
       "gdcHdslDteRTSstatus": gdcHdslDteRTSstatus,
       "gdcHdslDteDSRstatus": gdcHdslDteDSRstatus,
       "gdcHdslDteStatus": gdcHdslDteStatus,
       "gdcHdslDiagnosticResults": gdcHdslDiagnosticResults,
       "gdcHdslDiagResultsTable": gdcHdslDiagResultsTable,
       "gdcHdslDiagResultsEntry": gdcHdslDiagResultsEntry,
       "gdcHdslDiagResultsIndex": gdcHdslDiagResultsIndex,
       "gdcHdslTestExecutionStatus": gdcHdslTestExecutionStatus,
       "gdcHdslDiagResultErr": gdcHdslDiagResultErr,
       "gdcHdslDiagResultInterval": gdcHdslDiagResultInterval,
       "gdcHdslV54RDLTest": gdcHdslV54RDLTest,
       "gdcFractional": gdcFractional,
       "hdslFracTable": hdslFracTable,
       "hdslFracEntry": hdslFracEntry,
       "hdslFracIndex": hdslFracIndex,
       "channelmapping": channelmapping,
       "gdcHdslHighway": gdcHdslHighway,
       "gdcHdslTimeSlot16": gdcHdslTimeSlot16,
       "gdcHdslAlarmThresholds": gdcHdslAlarmThresholds,
       "hdslAlarmConfigTable": hdslAlarmConfigTable,
       "hdslAlarmConfigEntry": hdslAlarmConfigEntry,
       "hdslAlarmConfigIndex": hdslAlarmConfigIndex,
       "hdslAlarmConfigIdentifier": hdslAlarmConfigIdentifier,
       "hdslAlarmThreshold": hdslAlarmThreshold,
       "hdsl700G2": hdsl700G2,
       "hdsl700G3": hdsl700G3,
       "hdsl730D1": hdsl730D1,
       "hdsl730D2": hdsl730D2,
       "hdsl720G1": hdsl720G1,
       "hdsl720G2": hdsl720G2,
       "hdsl702G2": hdsl702G2,
       "hdsl710D2": hdsl710D2,
       "hdsl700G2RP": hdsl700G2RP,
       "hdsl710D2RP": hdsl710D2RP,
       "hdsl720G2RP": hdsl720G2RP,
       "hdsl730D2RP": hdsl730D2RP,
       "hdsl701T2": hdsl701T2,
       "hdsl701T2RP": hdsl701T2RP,
       "hdsl721T1": hdsl721T1,
       "hdsl721T2": hdsl721T2,
       "hdsl721T2RP": hdsl721T2RP,
       "hdsl731D1": hdsl731D1,
       "hdsl731D2": hdsl731D2,
       "hdsl731D2RP": hdsl731D2RP,
       "hdsl700AG2": hdsl700AG2,
       "hdsl700AG2NZ": hdsl700AG2NZ,
       "hdslGT1030": hdslGT1030,
       "hdslGT2030": hdslGT2030,
       "uas7722": uas7722,
       "hdslGT1020": hdslGT1020,
       "hdslGT2020": hdslGT2020,
       "hdsl711D2": hdsl711D2}
)
