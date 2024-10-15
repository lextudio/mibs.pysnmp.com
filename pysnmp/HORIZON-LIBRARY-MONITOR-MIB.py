# SNMP MIB module (HORIZON-LIBRARY-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HORIZON-LIBRARY-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:47 2024
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



class HlmSenseCode(Integer32):
    """Custom type HlmSenseCode based on Integer32"""
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
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("acCommandOverlap", 29),
          ("acInitiator", 28),
          ("acSCSIParity", 27),
          ("hwCap", 9),
          ("hwGeneral", 7),
          ("hwMicroCode", 10),
          ("hwTapeDrive", 8),
          ("irDestEltFull", 20),
          ("irIncompatibleMedia", 17),
          ("irInsufficientReservationResources", 33),
          ("irInvalidCDB", 14),
          ("irInvalidCommand", 12),
          ("irInvalidElt", 13),
          ("irInvalidField", 16),
          ("irInvalidLun", 15),
          ("irInvalidReleaseOfPersistentReservation", 31),
          ("irMediumMagazineRemoved", 32),
          ("irMediumNotPresent", 19),
          ("irParamLength", 11),
          ("irSavingParamNotSupported", 18),
          ("irSrcEltEmpty", 21),
          ("nrCapOpen", 6),
          ("nrCleaningCartridgeInstalled", 30),
          ("nrInProcess", 3),
          ("nrMaintenance", 5),
          ("nrManIntervReq", 4),
          ("nrNotReportable", 2),
          ("uaBusDeviceResetMessageOccured", 39),
          ("uaIoEltAccess", 24),
          ("uaMicroCodeChanged", 26),
          ("uaModeParamChanged", 25),
          ("uaNotReady", 23),
          ("uaPowerOn", 22),
          ("uaPowerOnOccured", 34),
          ("uaRegistrationPreempted", 37),
          ("uaReservationPreempted", 35),
          ("uaReservationReleased", 36),
          ("uaSCSIBusReset", 38),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Storagetek_ObjectIdentity = ObjectIdentity
storagetek = _Storagetek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1)
)
_HorizonLibraryMonitor_ObjectIdentity = ObjectIdentity
horizonLibraryMonitor = _HorizonLibraryMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5)
)
_HlmAgent_ObjectIdentity = ObjectIdentity
hlmAgent = _HlmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 1)
)
_HlmAgtRelease_Type = DisplayString
_HlmAgtRelease_Object = MibScalar
hlmAgtRelease = _HlmAgtRelease_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 1, 1),
    _HlmAgtRelease_Type()
)
hlmAgtRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmAgtRelease.setStatus("mandatory")


class _HlmAgtStatus_Type(Integer32):
    """Custom type hlmAgtStatus based on Integer32"""
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
        *(("expired", 4),
          ("expiring", 3),
          ("initializing", 1),
          ("running", 2))
    )


_HlmAgtStatus_Type.__name__ = "Integer32"
_HlmAgtStatus_Object = MibScalar
hlmAgtStatus = _HlmAgtStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 1, 2),
    _HlmAgtStatus_Type()
)
hlmAgtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmAgtStatus.setStatus("mandatory")
_HlmAgtBootDate_Type = DisplayString
_HlmAgtBootDate_Object = MibScalar
hlmAgtBootDate = _HlmAgtBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 1, 3),
    _HlmAgtBootDate_Type()
)
hlmAgtBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmAgtBootDate.setStatus("mandatory")
_HlmAgtUrl_Type = DisplayString
_HlmAgtUrl_Object = MibScalar
hlmAgtUrl = _HlmAgtUrl_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 1, 4),
    _HlmAgtUrl_Type()
)
hlmAgtUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlmAgtUrl.setStatus("mandatory")
_HlmTrap_ObjectIdentity = ObjectIdentity
hlmTrap = _HlmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2)
)
_HlmTrpMinPollingRate_Type = Integer32
_HlmTrpMinPollingRate_Object = MibScalar
hlmTrpMinPollingRate = _HlmTrpMinPollingRate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2, 1),
    _HlmTrpMinPollingRate_Type()
)
hlmTrpMinPollingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmTrpMinPollingRate.setStatus("mandatory")
_HlmTrpCurPollingRate_Type = Integer32
_HlmTrpCurPollingRate_Object = MibScalar
hlmTrpCurPollingRate = _HlmTrpCurPollingRate_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2, 2),
    _HlmTrpCurPollingRate_Type()
)
hlmTrpCurPollingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlmTrpCurPollingRate.setStatus("mandatory")
_HlmTrpMsg_Type = DisplayString
_HlmTrpMsg_Object = MibScalar
hlmTrpMsg = _HlmTrpMsg_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2, 3),
    _HlmTrpMsg_Type()
)
hlmTrpMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmTrpMsg.setStatus("mandatory")
_HlmTrpOid_Type = ObjectIdentifier
_HlmTrpOid_Object = MibScalar
hlmTrpOid = _HlmTrpOid_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2, 4),
    _HlmTrpOid_Type()
)
hlmTrpOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmTrpOid.setStatus("mandatory")


class _HlmTrpLogReportLevel_Type(Integer32):
    """Custom type hlmTrpLogReportLevel based on Integer32"""
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
        *(("error", 2),
          ("info", 4),
          ("silent", 1),
          ("unclassified", 5),
          ("warning", 3))
    )


_HlmTrpLogReportLevel_Type.__name__ = "Integer32"
_HlmTrpLogReportLevel_Object = MibScalar
hlmTrpLogReportLevel = _HlmTrpLogReportLevel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 2, 5),
    _HlmTrpLogReportLevel_Type()
)
hlmTrpLogReportLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlmTrpLogReportLevel.setStatus("mandatory")
_HlmHardware_ObjectIdentity = ObjectIdentity
hlmHardware = _HlmHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3)
)
_HlmLibrary_ObjectIdentity = ObjectIdentity
hlmLibrary = _HlmLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1)
)
_HlmLibCount_Type = Integer32
_HlmLibCount_Object = MibScalar
hlmLibCount = _HlmLibCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 1),
    _HlmLibCount_Type()
)
hlmLibCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibCount.setStatus("mandatory")
_HlmLibTable_Object = MibTable
hlmLibTable = _HlmLibTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hlmLibTable.setStatus("mandatory")
_HlmLibEntry_Object = MibTableRow
hlmLibEntry = _HlmLibEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1)
)
hlmLibEntry.setIndexNames(
    (0, "HORIZON-LIBRARY-MONITOR-MIB", "hlmLibIndex"),
)
if mibBuilder.loadTexts:
    hlmLibEntry.setStatus("mandatory")
_HlmLibIndex_Type = Integer32
_HlmLibIndex_Object = MibTableColumn
hlmLibIndex = _HlmLibIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 1),
    _HlmLibIndex_Type()
)
hlmLibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibIndex.setStatus("mandatory")
_HlmLibType_Type = DisplayString
_HlmLibType_Object = MibTableColumn
hlmLibType = _HlmLibType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 2),
    _HlmLibType_Type()
)
hlmLibType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibType.setStatus("mandatory")
_HlmLibVendor_Type = DisplayString
_HlmLibVendor_Object = MibTableColumn
hlmLibVendor = _HlmLibVendor_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 3),
    _HlmLibVendor_Type()
)
hlmLibVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibVendor.setStatus("mandatory")


class _HlmLibStatus_Type(Integer32):
    """Custom type hlmLibStatus based on Integer32"""
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
        *(("busy", 4),
          ("error", 3),
          ("ok", 2),
          ("reservConflict", 5),
          ("unknown", 1))
    )


_HlmLibStatus_Type.__name__ = "Integer32"
_HlmLibStatus_Object = MibTableColumn
hlmLibStatus = _HlmLibStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 4),
    _HlmLibStatus_Type()
)
hlmLibStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibStatus.setStatus("mandatory")
_HlmLibSense_Type = HlmSenseCode
_HlmLibSense_Object = MibTableColumn
hlmLibSense = _HlmLibSense_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 5),
    _HlmLibSense_Type()
)
hlmLibSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibSense.setStatus("mandatory")
_HlmLibMicLevel_Type = DisplayString
_HlmLibMicLevel_Object = MibTableColumn
hlmLibMicLevel = _HlmLibMicLevel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 6),
    _HlmLibMicLevel_Type()
)
hlmLibMicLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibMicLevel.setStatus("mandatory")
_HlmLibSlotCount_Type = Integer32
_HlmLibSlotCount_Object = MibTableColumn
hlmLibSlotCount = _HlmLibSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 7),
    _HlmLibSlotCount_Type()
)
hlmLibSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibSlotCount.setStatus("mandatory")
_HlmLibCapCount_Type = Integer32
_HlmLibCapCount_Object = MibTableColumn
hlmLibCapCount = _HlmLibCapCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 8),
    _HlmLibCapCount_Type()
)
hlmLibCapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibCapCount.setStatus("mandatory")
_HlmLibDriveCount_Type = Integer32
_HlmLibDriveCount_Object = MibTableColumn
hlmLibDriveCount = _HlmLibDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 9),
    _HlmLibDriveCount_Type()
)
hlmLibDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibDriveCount.setStatus("mandatory")
_HlmLibSerialNumber_Type = DisplayString
_HlmLibSerialNumber_Object = MibTableColumn
hlmLibSerialNumber = _HlmLibSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 10),
    _HlmLibSerialNumber_Type()
)
hlmLibSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibSerialNumber.setStatus("mandatory")
_HlmLibSenseText_Type = DisplayString
_HlmLibSenseText_Object = MibTableColumn
hlmLibSenseText = _HlmLibSenseText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 11),
    _HlmLibSenseText_Type()
)
hlmLibSenseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmLibSenseText.setStatus("mandatory")
_HlmLibUrl_Type = DisplayString
_HlmLibUrl_Object = MibTableColumn
hlmLibUrl = _HlmLibUrl_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 1, 2, 1, 12),
    _HlmLibUrl_Type()
)
hlmLibUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hlmLibUrl.setStatus("mandatory")
_HlmDrive_ObjectIdentity = ObjectIdentity
hlmDrive = _HlmDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2)
)
_HlmDrvCount_Type = Integer32
_HlmDrvCount_Object = MibScalar
hlmDrvCount = _HlmDrvCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 1),
    _HlmDrvCount_Type()
)
hlmDrvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvCount.setStatus("mandatory")
_HlmDrvTable_Object = MibTable
hlmDrvTable = _HlmDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hlmDrvTable.setStatus("mandatory")
_HlmDrvEntry_Object = MibTableRow
hlmDrvEntry = _HlmDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1)
)
hlmDrvEntry.setIndexNames(
    (0, "HORIZON-LIBRARY-MONITOR-MIB", "hlmDrvLibIndex"),
    (0, "HORIZON-LIBRARY-MONITOR-MIB", "hlmDrvIndex"),
)
if mibBuilder.loadTexts:
    hlmDrvEntry.setStatus("mandatory")
_HlmDrvLibIndex_Type = Integer32
_HlmDrvLibIndex_Object = MibTableColumn
hlmDrvLibIndex = _HlmDrvLibIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 1),
    _HlmDrvLibIndex_Type()
)
hlmDrvLibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvLibIndex.setStatus("mandatory")
_HlmDrvIndex_Type = Integer32
_HlmDrvIndex_Object = MibTableColumn
hlmDrvIndex = _HlmDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 2),
    _HlmDrvIndex_Type()
)
hlmDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvIndex.setStatus("mandatory")


class _HlmDrvType_Type(Integer32):
    """Custom type hlmDrvType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dlt12000", 6),
          ("dlt2000", 2),
          ("dlt20000", 7),
          ("dlt2000XT", 3),
          ("dlt4000", 4),
          ("dlt7000", 5),
          ("dlt8000", 15),
          ("drive9840", 8),
          ("drve4781or4480", 14),
          ("redWoodSD3", 11),
          ("silverton4490or4791", 10),
          ("timberLine9490", 12),
          ("timberLine9491", 13),
          ("twinPeaks4890", 9),
          ("undetermined", 1))
    )


_HlmDrvType_Type.__name__ = "Integer32"
_HlmDrvType_Object = MibTableColumn
hlmDrvType = _HlmDrvType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 3),
    _HlmDrvType_Type()
)
hlmDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvType.setStatus("mandatory")


class _HlmDrvStatus_Type(Integer32):
    """Custom type hlmDrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 2),
          ("unknown", 1))
    )


_HlmDrvStatus_Type.__name__ = "Integer32"
_HlmDrvStatus_Object = MibTableColumn
hlmDrvStatus = _HlmDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 4),
    _HlmDrvStatus_Type()
)
hlmDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvStatus.setStatus("mandatory")
_HlmDrvSense_Type = HlmSenseCode
_HlmDrvSense_Object = MibTableColumn
hlmDrvSense = _HlmDrvSense_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 5),
    _HlmDrvSense_Type()
)
hlmDrvSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvSense.setStatus("mandatory")


class _HlmDrvContent_Type(Integer32):
    """Custom type hlmDrvContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("full", 3),
          ("unknown", 1))
    )


_HlmDrvContent_Type.__name__ = "Integer32"
_HlmDrvContent_Object = MibTableColumn
hlmDrvContent = _HlmDrvContent_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 6),
    _HlmDrvContent_Type()
)
hlmDrvContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvContent.setStatus("mandatory")


class _HlmDrvVolType_Type(Integer32):
    """Custom type hlmDrvVolType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("cleaning9840", 12),
          ("cleaningRedWoodDD3D", 10),
          ("dltCompactIIIOrdltCleaning", 2),
          ("dltCompactIIIXT", 4),
          ("dltCompactIV", 3),
          ("extendedEnhanced3490", 13),
          ("extendedLengthCartridge3490E", 6),
          ("longLengthRedWoodDD3C", 9),
          ("normalOrCleaning3480", 5),
          ("shortLengthRedWoodDD3A", 7),
          ("standard9840", 11),
          ("standardLengthRedWoodDD3B", 8),
          ("undetermined", 1))
    )


_HlmDrvVolType_Type.__name__ = "Integer32"
_HlmDrvVolType_Object = MibTableColumn
hlmDrvVolType = _HlmDrvVolType_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 7),
    _HlmDrvVolType_Type()
)
hlmDrvVolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvVolType.setStatus("mandatory")
_HlmDrvVolLabel_Type = DisplayString
_HlmDrvVolLabel_Object = MibTableColumn
hlmDrvVolLabel = _HlmDrvVolLabel_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 8),
    _HlmDrvVolLabel_Type()
)
hlmDrvVolLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvVolLabel.setStatus("mandatory")
_HlmDrvTypeText_Type = DisplayString
_HlmDrvTypeText_Object = MibTableColumn
hlmDrvTypeText = _HlmDrvTypeText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 9),
    _HlmDrvTypeText_Type()
)
hlmDrvTypeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvTypeText.setStatus("mandatory")
_HlmDrvVolTypeText_Type = DisplayString
_HlmDrvVolTypeText_Object = MibTableColumn
hlmDrvVolTypeText = _HlmDrvVolTypeText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 10),
    _HlmDrvVolTypeText_Type()
)
hlmDrvVolTypeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvVolTypeText.setStatus("mandatory")
_HlmDrvSerialNumber_Type = DisplayString
_HlmDrvSerialNumber_Object = MibTableColumn
hlmDrvSerialNumber = _HlmDrvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 11),
    _HlmDrvSerialNumber_Type()
)
hlmDrvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvSerialNumber.setStatus("mandatory")
_HlmDrvSenseText_Type = DisplayString
_HlmDrvSenseText_Object = MibTableColumn
hlmDrvSenseText = _HlmDrvSenseText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 2, 2, 1, 12),
    _HlmDrvSenseText_Type()
)
hlmDrvSenseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmDrvSenseText.setStatus("mandatory")
_HlmCap_ObjectIdentity = ObjectIdentity
hlmCap = _HlmCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3)
)
_HlmCapCount_Type = Integer32
_HlmCapCount_Object = MibScalar
hlmCapCount = _HlmCapCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 1),
    _HlmCapCount_Type()
)
hlmCapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapCount.setStatus("mandatory")
_HlmCapTable_Object = MibTable
hlmCapTable = _HlmCapTable_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hlmCapTable.setStatus("mandatory")
_HlmCapEntry_Object = MibTableRow
hlmCapEntry = _HlmCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1)
)
hlmCapEntry.setIndexNames(
    (0, "HORIZON-LIBRARY-MONITOR-MIB", "hlmCapLibIndex"),
    (0, "HORIZON-LIBRARY-MONITOR-MIB", "hlmCapIndex"),
)
if mibBuilder.loadTexts:
    hlmCapEntry.setStatus("mandatory")
_HlmCapLibIndex_Type = Integer32
_HlmCapLibIndex_Object = MibTableColumn
hlmCapLibIndex = _HlmCapLibIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 1),
    _HlmCapLibIndex_Type()
)
hlmCapLibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapLibIndex.setStatus("mandatory")
_HlmCapIndex_Type = Integer32
_HlmCapIndex_Object = MibTableColumn
hlmCapIndex = _HlmCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 2),
    _HlmCapIndex_Type()
)
hlmCapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapIndex.setStatus("mandatory")


class _HlmCapHandAccessibility_Type(Integer32):
    """Custom type hlmCapHandAccessibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 3),
          ("open", 2),
          ("unknown", 1))
    )


_HlmCapHandAccessibility_Type.__name__ = "Integer32"
_HlmCapHandAccessibility_Object = MibTableColumn
hlmCapHandAccessibility = _HlmCapHandAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 3),
    _HlmCapHandAccessibility_Type()
)
hlmCapHandAccessibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapHandAccessibility.setStatus("mandatory")


class _HlmCapStatus_Type(Integer32):
    """Custom type hlmCapStatus based on Integer32"""
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
        *(("error", 3),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 4))
    )


_HlmCapStatus_Type.__name__ = "Integer32"
_HlmCapStatus_Object = MibTableColumn
hlmCapStatus = _HlmCapStatus_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 4),
    _HlmCapStatus_Type()
)
hlmCapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapStatus.setStatus("mandatory")
_HlmCapSense_Type = HlmSenseCode
_HlmCapSense_Object = MibTableColumn
hlmCapSense = _HlmCapSense_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 5),
    _HlmCapSense_Type()
)
hlmCapSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapSense.setStatus("mandatory")
_HlmCapCellCount_Type = Integer32
_HlmCapCellCount_Object = MibTableColumn
hlmCapCellCount = _HlmCapCellCount_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 6),
    _HlmCapCellCount_Type()
)
hlmCapCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapCellCount.setStatus("mandatory")
_HlmCapSenseText_Type = DisplayString
_HlmCapSenseText_Object = MibTableColumn
hlmCapSenseText = _HlmCapSenseText_Object(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 3, 3, 2, 1, 7),
    _HlmCapSenseText_Type()
)
hlmCapSenseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hlmCapSenseText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hlmTrpErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 1)
)
hlmTrpErr.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpMsg")
)
if mibBuilder.loadTexts:
    hlmTrpErr.setStatus(
        ""
    )

hlmTrpWar = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 2)
)
hlmTrpWar.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpMsg")
)
if mibBuilder.loadTexts:
    hlmTrpWar.setStatus(
        ""
    )

hlmTrpInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 3)
)
hlmTrpInfo.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpMsg")
)
if mibBuilder.loadTexts:
    hlmTrpInfo.setStatus(
        ""
    )

hlmTrpUncl = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 4)
)
hlmTrpUncl.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpMsg")
)
if mibBuilder.loadTexts:
    hlmTrpUncl.setStatus(
        ""
    )

hlmTrpNorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 5)
)
hlmTrpNorStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpNorStatus.setStatus(
        ""
    )

hlmTrpUnkStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 6)
)
hlmTrpUnkStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpUnkStatus.setStatus(
        ""
    )

hlmTrpWarStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 7)
)
hlmTrpWarStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpWarStatus.setStatus(
        ""
    )

hlmTrpMinStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 8)
)
hlmTrpMinStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpMinStatus.setStatus(
        ""
    )

hlmTrpMajStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 9)
)
hlmTrpMajStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpMajStatus.setStatus(
        ""
    )

hlmTrpCriStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1211, 1, 5, 0, 10)
)
hlmTrpCriStatus.setObjects(
    ("HORIZON-LIBRARY-MONITOR-MIB", "hlmTrpOid")
)
if mibBuilder.loadTexts:
    hlmTrpCriStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HORIZON-LIBRARY-MONITOR-MIB",
    **{"HlmSenseCode": HlmSenseCode,
       "storagetek": storagetek,
       "products": products,
       "horizonLibraryMonitor": horizonLibraryMonitor,
       "hlmTrpErr": hlmTrpErr,
       "hlmTrpWar": hlmTrpWar,
       "hlmTrpInfo": hlmTrpInfo,
       "hlmTrpUncl": hlmTrpUncl,
       "hlmTrpNorStatus": hlmTrpNorStatus,
       "hlmTrpUnkStatus": hlmTrpUnkStatus,
       "hlmTrpWarStatus": hlmTrpWarStatus,
       "hlmTrpMinStatus": hlmTrpMinStatus,
       "hlmTrpMajStatus": hlmTrpMajStatus,
       "hlmTrpCriStatus": hlmTrpCriStatus,
       "hlmAgent": hlmAgent,
       "hlmAgtRelease": hlmAgtRelease,
       "hlmAgtStatus": hlmAgtStatus,
       "hlmAgtBootDate": hlmAgtBootDate,
       "hlmAgtUrl": hlmAgtUrl,
       "hlmTrap": hlmTrap,
       "hlmTrpMinPollingRate": hlmTrpMinPollingRate,
       "hlmTrpCurPollingRate": hlmTrpCurPollingRate,
       "hlmTrpMsg": hlmTrpMsg,
       "hlmTrpOid": hlmTrpOid,
       "hlmTrpLogReportLevel": hlmTrpLogReportLevel,
       "hlmHardware": hlmHardware,
       "hlmLibrary": hlmLibrary,
       "hlmLibCount": hlmLibCount,
       "hlmLibTable": hlmLibTable,
       "hlmLibEntry": hlmLibEntry,
       "hlmLibIndex": hlmLibIndex,
       "hlmLibType": hlmLibType,
       "hlmLibVendor": hlmLibVendor,
       "hlmLibStatus": hlmLibStatus,
       "hlmLibSense": hlmLibSense,
       "hlmLibMicLevel": hlmLibMicLevel,
       "hlmLibSlotCount": hlmLibSlotCount,
       "hlmLibCapCount": hlmLibCapCount,
       "hlmLibDriveCount": hlmLibDriveCount,
       "hlmLibSerialNumber": hlmLibSerialNumber,
       "hlmLibSenseText": hlmLibSenseText,
       "hlmLibUrl": hlmLibUrl,
       "hlmDrive": hlmDrive,
       "hlmDrvCount": hlmDrvCount,
       "hlmDrvTable": hlmDrvTable,
       "hlmDrvEntry": hlmDrvEntry,
       "hlmDrvLibIndex": hlmDrvLibIndex,
       "hlmDrvIndex": hlmDrvIndex,
       "hlmDrvType": hlmDrvType,
       "hlmDrvStatus": hlmDrvStatus,
       "hlmDrvSense": hlmDrvSense,
       "hlmDrvContent": hlmDrvContent,
       "hlmDrvVolType": hlmDrvVolType,
       "hlmDrvVolLabel": hlmDrvVolLabel,
       "hlmDrvTypeText": hlmDrvTypeText,
       "hlmDrvVolTypeText": hlmDrvVolTypeText,
       "hlmDrvSerialNumber": hlmDrvSerialNumber,
       "hlmDrvSenseText": hlmDrvSenseText,
       "hlmCap": hlmCap,
       "hlmCapCount": hlmCapCount,
       "hlmCapTable": hlmCapTable,
       "hlmCapEntry": hlmCapEntry,
       "hlmCapLibIndex": hlmCapLibIndex,
       "hlmCapIndex": hlmCapIndex,
       "hlmCapHandAccessibility": hlmCapHandAccessibility,
       "hlmCapStatus": hlmCapStatus,
       "hlmCapSense": hlmCapSense,
       "hlmCapCellCount": hlmCapCellCount,
       "hlmCapSenseText": hlmCapSenseText}
)
