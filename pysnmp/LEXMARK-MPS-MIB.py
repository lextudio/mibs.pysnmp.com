# SNMP MIB module (LEXMARK-MPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEXMARK-MPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:49 2024
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

(lexmark,
 lexmarkModules) = mibBuilder.importSymbols(
    "LEXMARK-ROOT-MIB",
    "lexmark",
    "lexmarkModules")

(AdminStatusTC,
 KeyValueTC,
 PaperSizeTC,
 PaperTypeTC,
 StatusTC,
 UnitsTC) = mibBuilder.importSymbols(
    "LEXMARK-TC-MIB",
    "AdminStatusTC",
    "KeyValueTC",
    "PaperSizeTC",
    "PaperTypeTC",
    "StatusTC",
    "UnitsTC")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mpsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 641, 4, 4)
)
mpsMibModule.setRevisions(
        ("2011-04-04 12:57",
         "2010-12-22 20:06",
         "2010-12-01 23:00",
         "2009-11-24 20:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SupplyTypeTC(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("fuser", 9),
          ("holepunchBox", 12),
          ("inkBottle", 4),
          ("inkCartridge", 3),
          ("inkPrinthead", 5),
          ("other", 2),
          ("photoconductor", 7),
          ("staples", 11),
          ("toner", 6),
          ("transferModule", 8),
          ("unknown", 1),
          ("wastetonerBox", 10))
    )



class CartridgeTypeTC(Integer32, TextualConvention):
    status = "current"
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
              21,
              22,
              23,
              37,
              38,
              39,
              53,
              54,
              55)
        )
    )
    namedValues = NamedValues(
        *(("extraHighYieldReturnProgram", 23),
          ("extraHighYieldStandard", 7),
          ("highYieldReturnProgram", 22),
          ("highYieldStandard", 6),
          ("invalid", 3),
          ("other", 2),
          ("refilledExtraHighYieldReturnProgram", 55),
          ("refilledExtraHighYieldStandard", 39),
          ("refilledHighYieldReturnProgram", 54),
          ("refilledHighYieldStandard", 38),
          ("refilledReturnProgram", 53),
          ("refilledStandard", 37),
          ("returnProgram", 21),
          ("shipWith", 4),
          ("standard", 5),
          ("unknown", 1))
    )



class SeverityTC(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 5),
          ("informational", 3),
          ("other", 2),
          ("serviceRequired", 6),
          ("unknown", 1),
          ("warning", 4))
    )



class AlertCodeTC(Integer32, TextualConvention):
    status = "current"
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              200,
              201,
              202,
              203,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              300,
              301,
              302,
              303,
              304,
              305,
              400,
              401,
              402,
              403,
              404,
              500,
              501,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              700,
              701,
              702,
              703,
              704,
              705,
              706,
              707,
              708,
              709,
              800,
              801,
              802,
              803,
              804,
              805,
              900,
              901,
              1000,
              1001,
              1002,
              20000)
        )
    )
    namedValues = NamedValues(
        *(("alignmentFailed", 10),
          ("busy", 14),
          ("calibrating", 9),
          ("coverClosed", 4),
          ("coverOpen", 3),
          ("doorClosed", 8),
          ("doorOpen", 7),
          ("emailConfigurationError", 901),
          ("emailErrorOther", 900),
          ("faxConfigurationError", 709),
          ("faxDisabled", 708),
          ("faxErrorOther", 700),
          ("faxPhoneLineDisconnected", 707),
          ("faxStorageFull", 702),
          ("faxStorageNearFull", 701),
          ("faxStorageReceiveFull", 706),
          ("faxStorageReceiveNearFull", 705),
          ("faxStorageSendFull", 704),
          ("faxStorageSendNearFull", 703),
          ("heldJobsMayNotBeRestored", 13),
          ("inputMediaChangeRequest", 304),
          ("inputMediaErrorOther", 300),
          ("inputMediaLoadRequest", 305),
          ("inputMediaSupplyEmpty", 303),
          ("inputMediaSupplyLow", 302),
          ("inputMediaTrayMissing", 301),
          ("interlockClosed", 6),
          ("interlockOpen", 5),
          ("interpreterComplexPage", 803),
          ("interpreterErrorOther", 800),
          ("interpreterInsufficientMemory", 801),
          ("interpreterJobHardwareMismatch", 804),
          ("interpreterOutOfMemory", 802),
          ("interpreterPrintDataExceedsMediaSize", 805),
          ("mediaPathErrorOther", 500),
          ("mediaPathPaperJam", 501),
          ("neverError", 20000),
          ("other", 2),
          ("outputMediaEmptyRequest", 404),
          ("outputMediaErrorOther", 400),
          ("outputMediaFull", 403),
          ("outputMediaNearFull", 402),
          ("outputMediaTrayMissing", 401),
          ("printHeadCarrierPathObstructed", 12),
          ("scannerADFJam", 604),
          ("scannerDisabled", 607),
          ("scannerErrorOther", 600),
          ("scannerLampError", 603),
          ("scannerLampLifeWarning", 602),
          ("scannerLampWarming", 601),
          ("scannerLocked", 606),
          ("scannerStalled", 605),
          ("storageErrorOther", 1000),
          ("storageFull", 1002),
          ("storageUnformatted", 1001),
          ("subunitCommunicationError", 110),
          ("subunitDisabled", 109),
          ("subunitErrorOther", 100),
          ("subunitInsufficientMemory", 106),
          ("subunitJammed", 103),
          ("subunitLifeAlmostOver", 101),
          ("subunitLifeOver", 102),
          ("subunitMemoryFull", 107),
          ("subunitNVFailure", 108),
          ("subunitOverTemperature", 105),
          ("subunitUnderTemperature", 104),
          ("supplyDefective", 216),
          ("supplyEarlyWarning", 202),
          ("supplyEmpty", 209),
          ("supplyErrorOther", 200),
          ("supplyFull", 205),
          ("supplyImproperInstall", 217),
          ("supplyInvalid", 215),
          ("supplyLifeAlmostOver", 210),
          ("supplyLifeOver", 211),
          ("supplyLow", 207),
          ("supplyMissing", 214),
          ("supplyNearEmpty", 208),
          ("supplyNearFull", 203),
          ("supplyNearLow", 206),
          ("supplyNearReplace", 212),
          ("supplyOk", 201),
          ("supplyReplace", 213),
          ("supplyUncalibrated", 219),
          ("supplyUnsupported", 218),
          ("unknown", 1),
          ("waiting", 15),
          ("warrantyOverrideRequired", 11))
    )



# MIB Managed Objects in the order of their OIDs

_Mps_ObjectIdentity = ObjectIdentity
mps = _Mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6)
)
_MpsMIBAdminInfo_ObjectIdentity = ObjectIdentity
mpsMIBAdminInfo = _MpsMIBAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 1)
)
_MpsMIBCompliances_ObjectIdentity = ObjectIdentity
mpsMIBCompliances = _MpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 1)
)
_MpsMIBGroups_ObjectIdentity = ObjectIdentity
mpsMIBGroups = _MpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 2)
)
_DeviceMibLocalization_Type = Integer32
_DeviceMibLocalization_Object = MibScalar
deviceMibLocalization = _DeviceMibLocalization_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 1),
    _DeviceMibLocalization_Type()
)
deviceMibLocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMibLocalization.setStatus("current")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("current")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1)
)
deviceEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("current")


class _DeviceIndex_Type(Integer32):
    """Custom type deviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceIndex_Type.__name__ = "Integer32"
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("current")
_DevicePort_Type = Integer32
_DevicePort_Object = MibTableColumn
devicePort = _DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 2),
    _DevicePort_Type()
)
devicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePort.setStatus("current")
_DeviceHrDeviceIndex_Type = Integer32
_DeviceHrDeviceIndex_Object = MibTableColumn
deviceHrDeviceIndex = _DeviceHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 3),
    _DeviceHrDeviceIndex_Type()
)
deviceHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHrDeviceIndex.setStatus("current")


class _DeviceModel_Type(SnmpAdminString):
    """Custom type deviceModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DeviceModel_Type.__name__ = "SnmpAdminString"
_DeviceModel_Object = MibTableColumn
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 4),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")


class _DeviceSerialNumber_Type(DisplayString):
    """Custom type deviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DeviceSerialNumber_Type.__name__ = "DisplayString"
_DeviceSerialNumber_Object = MibTableColumn
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 5),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")


class _DeviceMibVersion_Type(DisplayString):
    """Custom type deviceMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceMibVersion_Type.__name__ = "DisplayString"
_DeviceMibVersion_Object = MibTableColumn
deviceMibVersion = _DeviceMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 6),
    _DeviceMibVersion_Type()
)
deviceMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMibVersion.setStatus("current")
_DeviceInstallDate_Type = DateAndTime
_DeviceInstallDate_Object = MibTableColumn
deviceInstallDate = _DeviceInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 7),
    _DeviceInstallDate_Type()
)
deviceInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInstallDate.setStatus("current")


class _DeviceMibSupportLevel_Type(Integer32):
    """Custom type deviceMibSupportLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              16,
              32,
              48)
        )
    )
    namedValues = NamedValues(
        *(("enterprise", 48),
          ("feature", 32),
          ("minimum", 1),
          ("none", 0),
          ("value", 16))
    )


_DeviceMibSupportLevel_Type.__name__ = "Integer32"
_DeviceMibSupportLevel_Object = MibTableColumn
deviceMibSupportLevel = _DeviceMibSupportLevel_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 2, 3, 1, 8),
    _DeviceMibSupportLevel_Type()
)
deviceMibSupportLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMibSupportLevel.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 3)
)
_HwInventoryTable_Object = MibTable
hwInventoryTable = _HwInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1)
)
if mibBuilder.loadTexts:
    hwInventoryTable.setStatus("current")
_HwInventoryEntry_Object = MibTableRow
hwInventoryEntry = _HwInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1)
)
hwInventoryEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "hwInventoryIndex"),
)
if mibBuilder.loadTexts:
    hwInventoryEntry.setStatus("current")


class _HwInventoryIndex_Type(Integer32):
    """Custom type hwInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwInventoryIndex_Type.__name__ = "Integer32"
_HwInventoryIndex_Object = MibTableColumn
hwInventoryIndex = _HwInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 1),
    _HwInventoryIndex_Type()
)
hwInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwInventoryIndex.setStatus("current")


class _HwInventoryParentIndex_Type(Integer32):
    """Custom type hwInventoryParentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwInventoryParentIndex_Type.__name__ = "Integer32"
_HwInventoryParentIndex_Object = MibTableColumn
hwInventoryParentIndex = _HwInventoryParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 2),
    _HwInventoryParentIndex_Type()
)
hwInventoryParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryParentIndex.setStatus("current")


class _HwInventoryType_Type(Integer32):
    """Custom type hwInventoryType based on Integer32"""
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
              257,
              258,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272)
        )
    )
    namedValues = NamedValues(
        *(("cardSwipe", 15),
          ("duplexer", 5),
          ("electronicCard", 4),
          ("faxCard", 10),
          ("finishingDevice", 8),
          ("inputTray", 6),
          ("keyboard", 13),
          ("memory", 11),
          ("nonVolitileMemory", 12),
          ("optionCardSwipe", 271),
          ("optionDuplexer", 261),
          ("optionFaxCard", 266),
          ("optionFinishingDevice", 264),
          ("optionInputTray", 262),
          ("optionKeyboard", 269),
          ("optionMemory", 267),
          ("optionNonVolitileMemory", 268),
          ("optionOther", 258),
          ("optionOutputTray", 263),
          ("optionPanel", 270),
          ("optionScanner", 265),
          ("optionTransferUnit", 272),
          ("optionUnknown", 257),
          ("other", 2),
          ("outputTray", 7),
          ("panel", 14),
          ("printEngine", 3),
          ("scanner", 9),
          ("transferUnit", 16),
          ("unknown", 1))
    )


_HwInventoryType_Type.__name__ = "Integer32"
_HwInventoryType_Object = MibTableColumn
hwInventoryType = _HwInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 3),
    _HwInventoryType_Type()
)
hwInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryType.setStatus("current")
_HwInventoryAdminStatus_Type = AdminStatusTC
_HwInventoryAdminStatus_Object = MibTableColumn
hwInventoryAdminStatus = _HwInventoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 4),
    _HwInventoryAdminStatus_Type()
)
hwInventoryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwInventoryAdminStatus.setStatus("current")
_HwInventoryStatus_Type = StatusTC
_HwInventoryStatus_Object = MibTableColumn
hwInventoryStatus = _HwInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 5),
    _HwInventoryStatus_Type()
)
hwInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryStatus.setStatus("current")
_HwInventoryPartNumber_Type = DisplayString
_HwInventoryPartNumber_Object = MibTableColumn
hwInventoryPartNumber = _HwInventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 6),
    _HwInventoryPartNumber_Type()
)
hwInventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryPartNumber.setStatus("current")
_HwInventorySerialNumber_Type = DisplayString
_HwInventorySerialNumber_Object = MibTableColumn
hwInventorySerialNumber = _HwInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 7),
    _HwInventorySerialNumber_Type()
)
hwInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventorySerialNumber.setStatus("current")
_HwInventoryDescription_Type = SnmpAdminString
_HwInventoryDescription_Object = MibTableColumn
hwInventoryDescription = _HwInventoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 8),
    _HwInventoryDescription_Type()
)
hwInventoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryDescription.setStatus("current")
_HwInventoryData_Type = KeyValueTC
_HwInventoryData_Object = MibTableColumn
hwInventoryData = _HwInventoryData_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 1, 1, 9),
    _HwInventoryData_Type()
)
hwInventoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInventoryData.setStatus("current")
_SupplyInventoryTable_Object = MibTable
supplyInventoryTable = _SupplyInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2)
)
if mibBuilder.loadTexts:
    supplyInventoryTable.setStatus("current")
_SupplyInventoryEntry_Object = MibTableRow
supplyInventoryEntry = _SupplyInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2, 1)
)
supplyInventoryEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "supplyInventoryIndex"),
)
if mibBuilder.loadTexts:
    supplyInventoryEntry.setStatus("current")


class _SupplyInventoryIndex_Type(Integer32):
    """Custom type supplyInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SupplyInventoryIndex_Type.__name__ = "Integer32"
_SupplyInventoryIndex_Object = MibTableColumn
supplyInventoryIndex = _SupplyInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2, 1, 1),
    _SupplyInventoryIndex_Type()
)
supplyInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supplyInventoryIndex.setStatus("current")
_SupplyInventoryType_Type = SupplyTypeTC
_SupplyInventoryType_Object = MibTableColumn
supplyInventoryType = _SupplyInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2, 1, 2),
    _SupplyInventoryType_Type()
)
supplyInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyInventoryType.setStatus("current")
_SupplyInventoryColorantValue_Type = DisplayString
_SupplyInventoryColorantValue_Object = MibTableColumn
supplyInventoryColorantValue = _SupplyInventoryColorantValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2, 1, 3),
    _SupplyInventoryColorantValue_Type()
)
supplyInventoryColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyInventoryColorantValue.setStatus("current")
_SupplyInventoryDescription_Type = SnmpAdminString
_SupplyInventoryDescription_Object = MibTableColumn
supplyInventoryDescription = _SupplyInventoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 2, 1, 4),
    _SupplyInventoryDescription_Type()
)
supplyInventoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyInventoryDescription.setStatus("current")
_SwInventoryTable_Object = MibTable
swInventoryTable = _SwInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3)
)
if mibBuilder.loadTexts:
    swInventoryTable.setStatus("current")
_SwInventoryEntry_Object = MibTableRow
swInventoryEntry = _SwInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1)
)
swInventoryEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "swInventoryIndex"),
)
if mibBuilder.loadTexts:
    swInventoryEntry.setStatus("current")


class _SwInventoryIndex_Type(Integer32):
    """Custom type swInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwInventoryIndex_Type.__name__ = "Integer32"
_SwInventoryIndex_Object = MibTableColumn
swInventoryIndex = _SwInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 1),
    _SwInventoryIndex_Type()
)
swInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swInventoryIndex.setStatus("current")


class _SwInventoryParentIndex_Type(Integer32):
    """Custom type swInventoryParentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwInventoryParentIndex_Type.__name__ = "Integer32"
_SwInventoryParentIndex_Object = MibTableColumn
swInventoryParentIndex = _SwInventoryParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 2),
    _SwInventoryParentIndex_Type()
)
swInventoryParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryParentIndex.setStatus("current")


class _SwInventoryType_Type(Integer32):
    """Custom type swInventoryType based on Integer32"""
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
        *(("application", 5),
          ("hardware", 4),
          ("operatingSystem", 3),
          ("other", 2),
          ("unknown", 1))
    )


_SwInventoryType_Type.__name__ = "Integer32"
_SwInventoryType_Object = MibTableColumn
swInventoryType = _SwInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 3),
    _SwInventoryType_Type()
)
swInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryType.setStatus("current")
_SwInventoryAdminStatus_Type = AdminStatusTC
_SwInventoryAdminStatus_Object = MibTableColumn
swInventoryAdminStatus = _SwInventoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 4),
    _SwInventoryAdminStatus_Type()
)
swInventoryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swInventoryAdminStatus.setStatus("current")
_SwInventoryStatus_Type = StatusTC
_SwInventoryStatus_Object = MibTableColumn
swInventoryStatus = _SwInventoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 5),
    _SwInventoryStatus_Type()
)
swInventoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryStatus.setStatus("current")
_SwInventoryName_Type = DisplayString
_SwInventoryName_Object = MibTableColumn
swInventoryName = _SwInventoryName_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 6),
    _SwInventoryName_Type()
)
swInventoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryName.setStatus("current")
_SwInventoryRevision_Type = DisplayString
_SwInventoryRevision_Object = MibTableColumn
swInventoryRevision = _SwInventoryRevision_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 7),
    _SwInventoryRevision_Type()
)
swInventoryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryRevision.setStatus("current")
_SwInventoryDescription_Type = SnmpAdminString
_SwInventoryDescription_Object = MibTableColumn
swInventoryDescription = _SwInventoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 8),
    _SwInventoryDescription_Type()
)
swInventoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryDescription.setStatus("current")


class _SwInventoryHWIndex_Type(Integer32):
    """Custom type swInventoryHWIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwInventoryHWIndex_Type.__name__ = "Integer32"
_SwInventoryHWIndex_Object = MibTableColumn
swInventoryHWIndex = _SwInventoryHWIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 9),
    _SwInventoryHWIndex_Type()
)
swInventoryHWIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryHWIndex.setStatus("current")
_SwInventoryData_Type = KeyValueTC
_SwInventoryData_Object = MibTableColumn
swInventoryData = _SwInventoryData_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 3, 3, 1, 10),
    _SwInventoryData_Type()
)
swInventoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swInventoryData.setStatus("current")
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 4)
)
_GeneralStats_ObjectIdentity = ObjectIdentity
generalStats = _GeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1)
)
_GenCountTable_Object = MibTable
genCountTable = _GenCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    genCountTable.setStatus("current")
_GenCountEntry_Object = MibTableRow
genCountEntry = _GenCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1, 1)
)
genCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "genCountIndex"),
)
if mibBuilder.loadTexts:
    genCountEntry.setStatus("current")


class _GenCountIndex_Type(Integer32):
    """Custom type genCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GenCountIndex_Type.__name__ = "Integer32"
_GenCountIndex_Object = MibTableColumn
genCountIndex = _GenCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1, 1, 1),
    _GenCountIndex_Type()
)
genCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genCountIndex.setStatus("current")


class _GenCountType_Type(Integer32):
    """Custom type genCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              64,
              65,
              66,
              67,
              96,
              97,
              98,
              99,
              100,
              101,
              128)
        )
    )
    namedValues = NamedValues(
        *(("changePaperPrompts", 100),
          ("coverOpens", 101),
          ("faxesSent", 96),
          ("hibernateCount", 3),
          ("lifetimeBlackCoverage", 64),
          ("lifetimeCyanCoverage", 65),
          ("lifetimeMagentaCoverage", 67),
          ("lifetimeYellowCoverage", 66),
          ("loadPaperPrompts", 99),
          ("paperJams", 97),
          ("porCount", 1),
          ("powerActiveTime", 33),
          ("powerHibernateTime", 36),
          ("powerIdleTime", 34),
          ("powerOffTime", 37),
          ("powerOnTime", 32),
          ("powerSleepTime", 35),
          ("printCalibrateCount", 4),
          ("scannerJams", 98),
          ("sleepCount", 2),
          ("usbInsertions", 128),
          ("warmupTotalTime", 38))
    )


_GenCountType_Type.__name__ = "Integer32"
_GenCountType_Object = MibTableColumn
genCountType = _GenCountType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1, 1, 2),
    _GenCountType_Type()
)
genCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCountType.setStatus("current")
_GenCountUnits_Type = UnitsTC
_GenCountUnits_Object = MibTableColumn
genCountUnits = _GenCountUnits_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1, 1, 3),
    _GenCountUnits_Type()
)
genCountUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCountUnits.setStatus("current")
_GenCountValue_Type = Counter32
_GenCountValue_Object = MibTableColumn
genCountValue = _GenCountValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 1, 1, 1, 4),
    _GenCountValue_Type()
)
genCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCountValue.setStatus("current")
_PaperStats_ObjectIdentity = ObjectIdentity
paperStats = _PaperStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2)
)
_PaperGeneralCountTable_Object = MibTable
paperGeneralCountTable = _PaperGeneralCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    paperGeneralCountTable.setStatus("current")
_PaperGeneralCountEntry_Object = MibTableRow
paperGeneralCountEntry = _PaperGeneralCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1, 1)
)
paperGeneralCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "paperGeneralCountIndex"),
)
if mibBuilder.loadTexts:
    paperGeneralCountEntry.setStatus("current")


class _PaperGeneralCountIndex_Type(Integer32):
    """Custom type paperGeneralCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperGeneralCountIndex_Type.__name__ = "Integer32"
_PaperGeneralCountIndex_Object = MibTableColumn
paperGeneralCountIndex = _PaperGeneralCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1, 1, 1),
    _PaperGeneralCountIndex_Type()
)
paperGeneralCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paperGeneralCountIndex.setStatus("current")


class _PaperGeneralCountType_Type(Integer32):
    """Custom type paperGeneralCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              16,
              17,
              18,
              32,
              33,
              34,
              48,
              49,
              50,
              64,
              65,
              66,
              67,
              80,
              81)
        )
    )
    namedValues = NamedValues(
        *(("blankCopy", 66),
          ("blankFax", 67),
          ("blankPrint", 65),
          ("blankTotal", 64),
          ("copyColor", 34),
          ("copyMono", 33),
          ("copyTotal", 32),
          ("faxColor", 50),
          ("faxMono", 49),
          ("faxTotal", 48),
          ("modularPageCount", 81),
          ("printColor", 18),
          ("printMono", 17),
          ("printNHold", 5),
          ("printTotal", 16),
          ("printerPageCount", 80),
          ("totalColorSafe", 4),
          ("totalMonoSafe", 3),
          ("totalPicked", 1),
          ("totalSafe", 2),
          ("usbDirect", 6))
    )


_PaperGeneralCountType_Type.__name__ = "Integer32"
_PaperGeneralCountType_Object = MibTableColumn
paperGeneralCountType = _PaperGeneralCountType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1, 1, 2),
    _PaperGeneralCountType_Type()
)
paperGeneralCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperGeneralCountType.setStatus("current")
_PaperGeneralCountUnits_Type = UnitsTC
_PaperGeneralCountUnits_Object = MibTableColumn
paperGeneralCountUnits = _PaperGeneralCountUnits_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1, 1, 3),
    _PaperGeneralCountUnits_Type()
)
paperGeneralCountUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperGeneralCountUnits.setStatus("current")
_PaperGeneralCountValue_Type = Counter32
_PaperGeneralCountValue_Object = MibTableColumn
paperGeneralCountValue = _PaperGeneralCountValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 1, 1, 4),
    _PaperGeneralCountValue_Type()
)
paperGeneralCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperGeneralCountValue.setStatus("current")
_PaperSidesCountTable_Object = MibTable
paperSidesCountTable = _PaperSidesCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    paperSidesCountTable.setStatus("current")
_PaperSidesCountEntry_Object = MibTableRow
paperSidesCountEntry = _PaperSidesCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1)
)
paperSidesCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "paperSidesCountIndex"),
)
if mibBuilder.loadTexts:
    paperSidesCountEntry.setStatus("current")


class _PaperSidesCountIndex_Type(Integer32):
    """Custom type paperSidesCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperSidesCountIndex_Type.__name__ = "Integer32"
_PaperSidesCountIndex_Object = MibTableColumn
paperSidesCountIndex = _PaperSidesCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 1),
    _PaperSidesCountIndex_Type()
)
paperSidesCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paperSidesCountIndex.setStatus("current")
_PaperSidesPaperSize_Type = PaperSizeTC
_PaperSidesPaperSize_Object = MibTableColumn
paperSidesPaperSize = _PaperSidesPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 2),
    _PaperSidesPaperSize_Type()
)
paperSidesPaperSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesPaperSize.setStatus("current")
_PaperSidesPaperType_Type = PaperTypeTC
_PaperSidesPaperType_Object = MibTableColumn
paperSidesPaperType = _PaperSidesPaperType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 3),
    _PaperSidesPaperType_Type()
)
paperSidesPaperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesPaperType.setStatus("current")
_PaperSidesMonoPicked_Type = Counter32
_PaperSidesMonoPicked_Object = MibTableColumn
paperSidesMonoPicked = _PaperSidesMonoPicked_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 4),
    _PaperSidesMonoPicked_Type()
)
paperSidesMonoPicked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesMonoPicked.setStatus("current")
_PaperSidesColorPicked_Type = Counter32
_PaperSidesColorPicked_Object = MibTableColumn
paperSidesColorPicked = _PaperSidesColorPicked_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 5),
    _PaperSidesColorPicked_Type()
)
paperSidesColorPicked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesColorPicked.setStatus("current")
_PaperSidesMonoSafe_Type = Counter32
_PaperSidesMonoSafe_Object = MibTableColumn
paperSidesMonoSafe = _PaperSidesMonoSafe_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 6),
    _PaperSidesMonoSafe_Type()
)
paperSidesMonoSafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesMonoSafe.setStatus("current")
_PaperSidesColorSafe_Type = Counter32
_PaperSidesColorSafe_Object = MibTableColumn
paperSidesColorSafe = _PaperSidesColorSafe_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 2, 1, 7),
    _PaperSidesColorSafe_Type()
)
paperSidesColorSafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSidesColorSafe.setStatus("current")
_PaperSheetsCountTable_Object = MibTable
paperSheetsCountTable = _PaperSheetsCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3)
)
if mibBuilder.loadTexts:
    paperSheetsCountTable.setStatus("current")
_PaperSheetsCountEntry_Object = MibTableRow
paperSheetsCountEntry = _PaperSheetsCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1)
)
paperSheetsCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "paperSheetsCountIndex"),
)
if mibBuilder.loadTexts:
    paperSheetsCountEntry.setStatus("current")


class _PaperSheetsCountIndex_Type(Integer32):
    """Custom type paperSheetsCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperSheetsCountIndex_Type.__name__ = "Integer32"
_PaperSheetsCountIndex_Object = MibTableColumn
paperSheetsCountIndex = _PaperSheetsCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1, 1),
    _PaperSheetsCountIndex_Type()
)
paperSheetsCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paperSheetsCountIndex.setStatus("current")
_PaperSheetsPaperSize_Type = PaperSizeTC
_PaperSheetsPaperSize_Object = MibTableColumn
paperSheetsPaperSize = _PaperSheetsPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1, 2),
    _PaperSheetsPaperSize_Type()
)
paperSheetsPaperSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSheetsPaperSize.setStatus("current")
_PaperSheetsPaperType_Type = PaperTypeTC
_PaperSheetsPaperType_Object = MibTableColumn
paperSheetsPaperType = _PaperSheetsPaperType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1, 3),
    _PaperSheetsPaperType_Type()
)
paperSheetsPaperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSheetsPaperType.setStatus("current")
_PaperSheetsPicked_Type = Counter32
_PaperSheetsPicked_Object = MibTableColumn
paperSheetsPicked = _PaperSheetsPicked_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1, 4),
    _PaperSheetsPicked_Type()
)
paperSheetsPicked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSheetsPicked.setStatus("current")
_PaperSheetsSafe_Type = Counter32
_PaperSheetsSafe_Object = MibTableColumn
paperSheetsSafe = _PaperSheetsSafe_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 3, 1, 5),
    _PaperSheetsSafe_Type()
)
paperSheetsSafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperSheetsSafe.setStatus("current")
_PaperNupCountTable_Object = MibTable
paperNupCountTable = _PaperNupCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4)
)
if mibBuilder.loadTexts:
    paperNupCountTable.setStatus("current")
_PaperNupCountEntry_Object = MibTableRow
paperNupCountEntry = _PaperNupCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4, 1)
)
paperNupCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "paperNupCountIndex"),
)
if mibBuilder.loadTexts:
    paperNupCountEntry.setStatus("current")


class _PaperNupCountIndex_Type(Integer32):
    """Custom type paperNupCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperNupCountIndex_Type.__name__ = "Integer32"
_PaperNupCountIndex_Object = MibTableColumn
paperNupCountIndex = _PaperNupCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4, 1, 1),
    _PaperNupCountIndex_Type()
)
paperNupCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paperNupCountIndex.setStatus("current")


class _PaperNupNumber_Type(Integer32):
    """Custom type paperNupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              9,
              12,
              16)
        )
    )
    namedValues = NamedValues(
        *(("fourUp", 4),
          ("nineUp", 9),
          ("off", 1),
          ("sixUp", 6),
          ("sixteenUp", 16),
          ("threeUp", 3),
          ("twelveUp", 12),
          ("twoUp", 2))
    )


_PaperNupNumber_Type.__name__ = "Integer32"
_PaperNupNumber_Object = MibTableColumn
paperNupNumber = _PaperNupNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4, 1, 2),
    _PaperNupNumber_Type()
)
paperNupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperNupNumber.setStatus("current")
_PaperNupSides_Type = Counter32
_PaperNupSides_Object = MibTableColumn
paperNupSides = _PaperNupSides_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4, 1, 3),
    _PaperNupSides_Type()
)
paperNupSides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperNupSides.setStatus("current")
_PaperNupLogicalSides_Type = Counter32
_PaperNupLogicalSides_Object = MibTableColumn
paperNupLogicalSides = _PaperNupLogicalSides_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 4, 1, 4),
    _PaperNupLogicalSides_Type()
)
paperNupLogicalSides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperNupLogicalSides.setStatus("current")
_PaperJobSizeTable_Object = MibTable
paperJobSizeTable = _PaperJobSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5)
)
if mibBuilder.loadTexts:
    paperJobSizeTable.setStatus("current")
_PaperJobSizeEntry_Object = MibTableRow
paperJobSizeEntry = _PaperJobSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1)
)
paperJobSizeEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "paperJobSizeIndex"),
)
if mibBuilder.loadTexts:
    paperJobSizeEntry.setStatus("current")


class _PaperJobSizeIndex_Type(Integer32):
    """Custom type paperJobSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperJobSizeIndex_Type.__name__ = "Integer32"
_PaperJobSizeIndex_Object = MibTableColumn
paperJobSizeIndex = _PaperJobSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1, 1),
    _PaperJobSizeIndex_Type()
)
paperJobSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    paperJobSizeIndex.setStatus("current")


class _PaperJobSizeMinimum_Type(Integer32):
    """Custom type paperJobSizeMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PaperJobSizeMinimum_Type.__name__ = "Integer32"
_PaperJobSizeMinimum_Object = MibTableColumn
paperJobSizeMinimum = _PaperJobSizeMinimum_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1, 2),
    _PaperJobSizeMinimum_Type()
)
paperJobSizeMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperJobSizeMinimum.setStatus("current")


class _PaperJobSizeMaximum_Type(Integer32):
    """Custom type paperJobSizeMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PaperJobSizeMaximum_Type.__name__ = "Integer32"
_PaperJobSizeMaximum_Object = MibTableColumn
paperJobSizeMaximum = _PaperJobSizeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1, 3),
    _PaperJobSizeMaximum_Type()
)
paperJobSizeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperJobSizeMaximum.setStatus("current")
_PaperJobSizeSideCount_Type = Counter32
_PaperJobSizeSideCount_Object = MibTableColumn
paperJobSizeSideCount = _PaperJobSizeSideCount_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1, 4),
    _PaperJobSizeSideCount_Type()
)
paperJobSizeSideCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperJobSizeSideCount.setStatus("current")
_PaperJobSizeJobCount_Type = Counter32
_PaperJobSizeJobCount_Object = MibTableColumn
paperJobSizeJobCount = _PaperJobSizeJobCount_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 2, 5, 1, 5),
    _PaperJobSizeJobCount_Type()
)
paperJobSizeJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paperJobSizeJobCount.setStatus("current")
_ScanStats_ObjectIdentity = ObjectIdentity
scanStats = _ScanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3)
)
_ScanCountTable_Object = MibTable
scanCountTable = _ScanCountTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    scanCountTable.setStatus("current")
_ScanCountEntry_Object = MibTableRow
scanCountEntry = _ScanCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1)
)
scanCountEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "scanCountIndex"),
)
if mibBuilder.loadTexts:
    scanCountEntry.setStatus("current")


class _ScanCountIndex_Type(Integer32):
    """Custom type scanCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScanCountIndex_Type.__name__ = "Integer32"
_ScanCountIndex_Object = MibTableColumn
scanCountIndex = _ScanCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1, 1),
    _ScanCountIndex_Type()
)
scanCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scanCountIndex.setStatus("current")


class _ScanCountType_Type(Integer32):
    """Custom type scanCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              257,
              258,
              259,
              260,
              261,
              769,
              770,
              771,
              772,
              773)
        )
    )
    namedValues = NamedValues(
        *(("copyAdf", 1),
          ("copyDuplex", 769),
          ("copyFlatbed", 257),
          ("faxAdf", 2),
          ("faxDuplex", 770),
          ("faxFlatbed", 258),
          ("scanToEmailAdf", 3),
          ("scanToEmailDuplex", 771),
          ("scanToEmailFlatbed", 259),
          ("scanToLocalHostAdf", 5),
          ("scanToLocalHostDuplex", 773),
          ("scanToLocalHostFlatbed", 261),
          ("scanToNetAdf", 4),
          ("scanToNetDuplex", 772),
          ("scanToNetFlatbed", 260))
    )


_ScanCountType_Type.__name__ = "Integer32"
_ScanCountType_Object = MibTableColumn
scanCountType = _ScanCountType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1, 2),
    _ScanCountType_Type()
)
scanCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanCountType.setStatus("current")
_ScanCountSize_Type = PaperSizeTC
_ScanCountSize_Object = MibTableColumn
scanCountSize = _ScanCountSize_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1, 3),
    _ScanCountSize_Type()
)
scanCountSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanCountSize.setStatus("current")
_ScanCountSides_Type = Counter32
_ScanCountSides_Object = MibTableColumn
scanCountSides = _ScanCountSides_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1, 4),
    _ScanCountSides_Type()
)
scanCountSides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanCountSides.setStatus("current")
_ScanCountSheets_Type = Counter32
_ScanCountSheets_Object = MibTableColumn
scanCountSheets = _ScanCountSheets_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 3, 1, 1, 5),
    _ScanCountSheets_Type()
)
scanCountSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanCountSheets.setStatus("current")
_SupplyStats_ObjectIdentity = ObjectIdentity
supplyStats = _SupplyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4)
)
_CurrentSuppliesTable_Object = MibTable
currentSuppliesTable = _CurrentSuppliesTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1)
)
if mibBuilder.loadTexts:
    currentSuppliesTable.setStatus("current")
_CurrentSuppliesEntry_Object = MibTableRow
currentSuppliesEntry = _CurrentSuppliesEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1)
)
currentSuppliesEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "currentSupplyIndex"),
)
if mibBuilder.loadTexts:
    currentSuppliesEntry.setStatus("current")


class _CurrentSupplyIndex_Type(Integer32):
    """Custom type currentSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentSupplyIndex_Type.__name__ = "Integer32"
_CurrentSupplyIndex_Object = MibTableColumn
currentSupplyIndex = _CurrentSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 1),
    _CurrentSupplyIndex_Type()
)
currentSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentSupplyIndex.setStatus("current")


class _CurrentSupplyInventoryIndex_Type(Integer32):
    """Custom type currentSupplyInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentSupplyInventoryIndex_Type.__name__ = "Integer32"
_CurrentSupplyInventoryIndex_Object = MibTableColumn
currentSupplyInventoryIndex = _CurrentSupplyInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 2),
    _CurrentSupplyInventoryIndex_Type()
)
currentSupplyInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyInventoryIndex.setStatus("current")
_CurrentSupplyType_Type = SupplyTypeTC
_CurrentSupplyType_Object = MibTableColumn
currentSupplyType = _CurrentSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 3),
    _CurrentSupplyType_Type()
)
currentSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyType.setStatus("current")
_CurrentSupplyColorantValue_Type = DisplayString
_CurrentSupplyColorantValue_Object = MibTableColumn
currentSupplyColorantValue = _CurrentSupplyColorantValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 4),
    _CurrentSupplyColorantValue_Type()
)
currentSupplyColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyColorantValue.setStatus("current")
_CurrentSupplyDescription_Type = SnmpAdminString
_CurrentSupplyDescription_Object = MibTableColumn
currentSupplyDescription = _CurrentSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 5),
    _CurrentSupplyDescription_Type()
)
currentSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyDescription.setStatus("current")


class _CurrentSupplySerialNumber_Type(DisplayString):
    """Custom type currentSupplySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CurrentSupplySerialNumber_Type.__name__ = "DisplayString"
_CurrentSupplySerialNumber_Object = MibTableColumn
currentSupplySerialNumber = _CurrentSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 6),
    _CurrentSupplySerialNumber_Type()
)
currentSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplySerialNumber.setStatus("current")


class _CurrentSupplyPartNumber_Type(DisplayString):
    """Custom type currentSupplyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CurrentSupplyPartNumber_Type.__name__ = "DisplayString"
_CurrentSupplyPartNumber_Object = MibTableColumn
currentSupplyPartNumber = _CurrentSupplyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 7),
    _CurrentSupplyPartNumber_Type()
)
currentSupplyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyPartNumber.setStatus("current")


class _CurrentSupplyClass_Type(Integer32):
    """Custom type currentSupplyClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("consumed", 2),
          ("filled", 1))
    )


_CurrentSupplyClass_Type.__name__ = "Integer32"
_CurrentSupplyClass_Object = MibTableColumn
currentSupplyClass = _CurrentSupplyClass_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 8),
    _CurrentSupplyClass_Type()
)
currentSupplyClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyClass.setStatus("current")
_CurrentSupplyCartridgeType_Type = CartridgeTypeTC
_CurrentSupplyCartridgeType_Object = MibTableColumn
currentSupplyCartridgeType = _CurrentSupplyCartridgeType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 9),
    _CurrentSupplyCartridgeType_Type()
)
currentSupplyCartridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCartridgeType.setStatus("current")
_CurrentSupplyInstallDate_Type = DateAndTime
_CurrentSupplyInstallDate_Object = MibTableColumn
currentSupplyInstallDate = _CurrentSupplyInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 10),
    _CurrentSupplyInstallDate_Type()
)
currentSupplyInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyInstallDate.setStatus("current")
_CurrentSupplyPageCountAtInstall_Type = Counter32
_CurrentSupplyPageCountAtInstall_Object = MibTableColumn
currentSupplyPageCountAtInstall = _CurrentSupplyPageCountAtInstall_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 11),
    _CurrentSupplyPageCountAtInstall_Type()
)
currentSupplyPageCountAtInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyPageCountAtInstall.setStatus("current")


class _CurrentSupplyCurrentStatus_Type(Integer32):
    """Custom type currentSupplyCurrentStatus based on Integer32"""
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
        *(("empty", 5),
          ("invalid", 6),
          ("low", 4),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_CurrentSupplyCurrentStatus_Type.__name__ = "Integer32"
_CurrentSupplyCurrentStatus_Object = MibTableColumn
currentSupplyCurrentStatus = _CurrentSupplyCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 12),
    _CurrentSupplyCurrentStatus_Type()
)
currentSupplyCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCurrentStatus.setStatus("current")
_CurrentSupplyCapacityUnit_Type = UnitsTC
_CurrentSupplyCapacityUnit_Object = MibTableColumn
currentSupplyCapacityUnit = _CurrentSupplyCapacityUnit_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 13),
    _CurrentSupplyCapacityUnit_Type()
)
currentSupplyCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCapacityUnit.setStatus("current")


class _CurrentSupplyCapacity_Type(Integer32):
    """Custom type currentSupplyCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CurrentSupplyCapacity_Type.__name__ = "Integer32"
_CurrentSupplyCapacity_Object = MibTableColumn
currentSupplyCapacity = _CurrentSupplyCapacity_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 14),
    _CurrentSupplyCapacity_Type()
)
currentSupplyCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCapacity.setStatus("current")
_CurrentSupplyFirstKnownLevel_Type = Counter32
_CurrentSupplyFirstKnownLevel_Object = MibTableColumn
currentSupplyFirstKnownLevel = _CurrentSupplyFirstKnownLevel_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 15),
    _CurrentSupplyFirstKnownLevel_Type()
)
currentSupplyFirstKnownLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyFirstKnownLevel.setStatus("current")
_CurrentSupplyCurrentLevel_Type = Counter32
_CurrentSupplyCurrentLevel_Object = MibTableColumn
currentSupplyCurrentLevel = _CurrentSupplyCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 16),
    _CurrentSupplyCurrentLevel_Type()
)
currentSupplyCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCurrentLevel.setStatus("current")
_CurrentSupplyUsage_Type = Counter32
_CurrentSupplyUsage_Object = MibTableColumn
currentSupplyUsage = _CurrentSupplyUsage_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 17),
    _CurrentSupplyUsage_Type()
)
currentSupplyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyUsage.setStatus("current")
_CurrentSupplyCalibrations_Type = Counter32
_CurrentSupplyCalibrations_Object = MibTableColumn
currentSupplyCalibrations = _CurrentSupplyCalibrations_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 18),
    _CurrentSupplyCalibrations_Type()
)
currentSupplyCalibrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCalibrations.setStatus("current")
_CurrentSupplyCoverage_Type = Counter32
_CurrentSupplyCoverage_Object = MibTableColumn
currentSupplyCoverage = _CurrentSupplyCoverage_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 1, 1, 19),
    _CurrentSupplyCoverage_Type()
)
currentSupplyCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSupplyCoverage.setStatus("current")
_SupplyHistoryTable_Object = MibTable
supplyHistoryTable = _SupplyHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2)
)
if mibBuilder.loadTexts:
    supplyHistoryTable.setStatus("current")
_SupplyHistoryEntry_Object = MibTableRow
supplyHistoryEntry = _SupplyHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1)
)
supplyHistoryEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "supplyHistoryIndex"),
)
if mibBuilder.loadTexts:
    supplyHistoryEntry.setStatus("current")


class _SupplyHistoryIndex_Type(Integer32):
    """Custom type supplyHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SupplyHistoryIndex_Type.__name__ = "Integer32"
_SupplyHistoryIndex_Object = MibTableColumn
supplyHistoryIndex = _SupplyHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 1),
    _SupplyHistoryIndex_Type()
)
supplyHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supplyHistoryIndex.setStatus("current")


class _SupplyHistoryInventoryIndex_Type(Integer32):
    """Custom type supplyHistoryInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SupplyHistoryInventoryIndex_Type.__name__ = "Integer32"
_SupplyHistoryInventoryIndex_Object = MibTableColumn
supplyHistoryInventoryIndex = _SupplyHistoryInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 2),
    _SupplyHistoryInventoryIndex_Type()
)
supplyHistoryInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryInventoryIndex.setStatus("current")
_SupplyHistorySupplyType_Type = SupplyTypeTC
_SupplyHistorySupplyType_Object = MibTableColumn
supplyHistorySupplyType = _SupplyHistorySupplyType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 3),
    _SupplyHistorySupplyType_Type()
)
supplyHistorySupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistorySupplyType.setStatus("current")
_SupplyHistoryColorantValue_Type = DisplayString
_SupplyHistoryColorantValue_Object = MibTableColumn
supplyHistoryColorantValue = _SupplyHistoryColorantValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 4),
    _SupplyHistoryColorantValue_Type()
)
supplyHistoryColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryColorantValue.setStatus("current")
_SupplyHistoryDescription_Type = SnmpAdminString
_SupplyHistoryDescription_Object = MibTableColumn
supplyHistoryDescription = _SupplyHistoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 5),
    _SupplyHistoryDescription_Type()
)
supplyHistoryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryDescription.setStatus("current")


class _SupplyHistorySerialNumber_Type(DisplayString):
    """Custom type supplyHistorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SupplyHistorySerialNumber_Type.__name__ = "DisplayString"
_SupplyHistorySerialNumber_Object = MibTableColumn
supplyHistorySerialNumber = _SupplyHistorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 6),
    _SupplyHistorySerialNumber_Type()
)
supplyHistorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistorySerialNumber.setStatus("current")
_SupplyHistoryCartridgeType_Type = CartridgeTypeTC
_SupplyHistoryCartridgeType_Object = MibTableColumn
supplyHistoryCartridgeType = _SupplyHistoryCartridgeType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 7),
    _SupplyHistoryCartridgeType_Type()
)
supplyHistoryCartridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryCartridgeType.setStatus("current")
_SupplyHistoryInstallDate_Type = DateAndTime
_SupplyHistoryInstallDate_Object = MibTableColumn
supplyHistoryInstallDate = _SupplyHistoryInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 8),
    _SupplyHistoryInstallDate_Type()
)
supplyHistoryInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryInstallDate.setStatus("current")
_SupplyHistoryPageCount_Type = Counter32
_SupplyHistoryPageCount_Object = MibTableColumn
supplyHistoryPageCount = _SupplyHistoryPageCount_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 9),
    _SupplyHistoryPageCount_Type()
)
supplyHistoryPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryPageCount.setStatus("current")
_SupplyHistoryCapacityUnit_Type = UnitsTC
_SupplyHistoryCapacityUnit_Object = MibTableColumn
supplyHistoryCapacityUnit = _SupplyHistoryCapacityUnit_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 10),
    _SupplyHistoryCapacityUnit_Type()
)
supplyHistoryCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryCapacityUnit.setStatus("current")


class _SupplyHistoryCapacity_Type(Integer32):
    """Custom type supplyHistoryCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SupplyHistoryCapacity_Type.__name__ = "Integer32"
_SupplyHistoryCapacity_Object = MibTableColumn
supplyHistoryCapacity = _SupplyHistoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 11),
    _SupplyHistoryCapacity_Type()
)
supplyHistoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryCapacity.setStatus("current")
_SupplyHistoryLastLevel_Type = Counter32
_SupplyHistoryLastLevel_Object = MibTableColumn
supplyHistoryLastLevel = _SupplyHistoryLastLevel_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 12),
    _SupplyHistoryLastLevel_Type()
)
supplyHistoryLastLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryLastLevel.setStatus("current")
_SupplyHistoryUsage_Type = Counter32
_SupplyHistoryUsage_Object = MibTableColumn
supplyHistoryUsage = _SupplyHistoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 13),
    _SupplyHistoryUsage_Type()
)
supplyHistoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryUsage.setStatus("current")
_SupplyHistoryCalibrations_Type = Counter32
_SupplyHistoryCalibrations_Object = MibTableColumn
supplyHistoryCalibrations = _SupplyHistoryCalibrations_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 14),
    _SupplyHistoryCalibrations_Type()
)
supplyHistoryCalibrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryCalibrations.setStatus("current")
_SupplyHistoryCoverage_Type = Counter32
_SupplyHistoryCoverage_Object = MibTableColumn
supplyHistoryCoverage = _SupplyHistoryCoverage_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 2, 1, 15),
    _SupplyHistoryCoverage_Type()
)
supplyHistoryCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistoryCoverage.setStatus("current")
_SupplyHistogramTable_Object = MibTable
supplyHistogramTable = _SupplyHistogramTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3)
)
if mibBuilder.loadTexts:
    supplyHistogramTable.setStatus("current")
_SupplyHistogramEntry_Object = MibTableRow
supplyHistogramEntry = _SupplyHistogramEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1)
)
supplyHistogramEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "supplyHistogramIndex"),
)
if mibBuilder.loadTexts:
    supplyHistogramEntry.setStatus("current")


class _SupplyHistogramIndex_Type(Integer32):
    """Custom type supplyHistogramIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SupplyHistogramIndex_Type.__name__ = "Integer32"
_SupplyHistogramIndex_Object = MibTableColumn
supplyHistogramIndex = _SupplyHistogramIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 1),
    _SupplyHistogramIndex_Type()
)
supplyHistogramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supplyHistogramIndex.setStatus("current")


class _SupplyHistogramInventoryIndex_Type(Integer32):
    """Custom type supplyHistogramInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SupplyHistogramInventoryIndex_Type.__name__ = "Integer32"
_SupplyHistogramInventoryIndex_Object = MibTableColumn
supplyHistogramInventoryIndex = _SupplyHistogramInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 2),
    _SupplyHistogramInventoryIndex_Type()
)
supplyHistogramInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramInventoryIndex.setStatus("current")
_SupplyHistogramSupplyType_Type = SupplyTypeTC
_SupplyHistogramSupplyType_Object = MibTableColumn
supplyHistogramSupplyType = _SupplyHistogramSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 3),
    _SupplyHistogramSupplyType_Type()
)
supplyHistogramSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramSupplyType.setStatus("current")
_SupplyHistogramColorantValue_Type = DisplayString
_SupplyHistogramColorantValue_Object = MibTableColumn
supplyHistogramColorantValue = _SupplyHistogramColorantValue_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 4),
    _SupplyHistogramColorantValue_Type()
)
supplyHistogramColorantValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramColorantValue.setStatus("current")
_SupplyHistogramDescription_Type = SnmpAdminString
_SupplyHistogramDescription_Object = MibTableColumn
supplyHistogramDescription = _SupplyHistogramDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 5),
    _SupplyHistogramDescription_Type()
)
supplyHistogramDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramDescription.setStatus("current")
_SupplyHistogramCapacityUnit_Type = UnitsTC
_SupplyHistogramCapacityUnit_Object = MibTableColumn
supplyHistogramCapacityUnit = _SupplyHistogramCapacityUnit_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 6),
    _SupplyHistogramCapacityUnit_Type()
)
supplyHistogramCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramCapacityUnit.setStatus("current")


class _SupplyHistogramCapacity_Type(Integer32):
    """Custom type supplyHistogramCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SupplyHistogramCapacity_Type.__name__ = "Integer32"
_SupplyHistogramCapacity_Object = MibTableColumn
supplyHistogramCapacity = _SupplyHistogramCapacity_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 7),
    _SupplyHistogramCapacity_Type()
)
supplyHistogramCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramCapacity.setStatus("current")
_SupplyHistogramCount_Type = Counter32
_SupplyHistogramCount_Object = MibTableColumn
supplyHistogramCount = _SupplyHistogramCount_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 8),
    _SupplyHistogramCount_Type()
)
supplyHistogramCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramCount.setStatus("current")
_SupplyHistogramCountUnits_Type = UnitsTC
_SupplyHistogramCountUnits_Object = MibTableColumn
supplyHistogramCountUnits = _SupplyHistogramCountUnits_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 4, 4, 3, 1, 9),
    _SupplyHistogramCountUnits_Type()
)
supplyHistogramCountUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyHistogramCountUnits.setStatus("current")
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 5)
)
_DeviceAlertTable_Object = MibTable
deviceAlertTable = _DeviceAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1)
)
if mibBuilder.loadTexts:
    deviceAlertTable.setStatus("current")
_DeviceAlertEntry_Object = MibTableRow
deviceAlertEntry = _DeviceAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1)
)
deviceAlertEntry.setIndexNames(
    (0, "LEXMARK-MPS-MIB", "deviceIndex"),
    (0, "LEXMARK-MPS-MIB", "deviceAlertIndex"),
)
if mibBuilder.loadTexts:
    deviceAlertEntry.setStatus("current")


class _DeviceAlertIndex_Type(Integer32):
    """Custom type deviceAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceAlertIndex_Type.__name__ = "Integer32"
_DeviceAlertIndex_Object = MibTableColumn
deviceAlertIndex = _DeviceAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 1),
    _DeviceAlertIndex_Type()
)
deviceAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertIndex.setStatus("current")


class _DeviceAlertConfigTableNode_Type(Integer32):
    """Custom type deviceAlertConfigTableNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hwInventoryTable", 2),
          ("supplyInventoryTable", 3),
          ("swInventoryTable", 4),
          ("unknown", 0))
    )


_DeviceAlertConfigTableNode_Type.__name__ = "Integer32"
_DeviceAlertConfigTableNode_Object = MibTableColumn
deviceAlertConfigTableNode = _DeviceAlertConfigTableNode_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 2),
    _DeviceAlertConfigTableNode_Type()
)
deviceAlertConfigTableNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertConfigTableNode.setStatus("current")


class _DeviceAlertConfigTableIndex_Type(Integer32):
    """Custom type deviceAlertConfigTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceAlertConfigTableIndex_Type.__name__ = "Integer32"
_DeviceAlertConfigTableIndex_Object = MibTableColumn
deviceAlertConfigTableIndex = _DeviceAlertConfigTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 3),
    _DeviceAlertConfigTableIndex_Type()
)
deviceAlertConfigTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertConfigTableIndex.setStatus("current")
_DeviceAlertSeverity_Type = SeverityTC
_DeviceAlertSeverity_Object = MibTableColumn
deviceAlertSeverity = _DeviceAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 4),
    _DeviceAlertSeverity_Type()
)
deviceAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertSeverity.setStatus("current")
_DeviceAlertCode_Type = AlertCodeTC
_DeviceAlertCode_Object = MibTableColumn
deviceAlertCode = _DeviceAlertCode_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 5),
    _DeviceAlertCode_Type()
)
deviceAlertCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertCode.setStatus("current")
_DeviceAlertDescription_Type = SnmpAdminString
_DeviceAlertDescription_Object = MibTableColumn
deviceAlertDescription = _DeviceAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 6),
    _DeviceAlertDescription_Type()
)
deviceAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertDescription.setStatus("current")
_DeviceAlertData_Type = KeyValueTC
_DeviceAlertData_Object = MibTableColumn
deviceAlertData = _DeviceAlertData_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 7),
    _DeviceAlertData_Type()
)
deviceAlertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertData.setStatus("current")
_DeviceAlertTime_Type = DateAndTime
_DeviceAlertTime_Object = MibTableColumn
deviceAlertTime = _DeviceAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 1, 1, 8),
    _DeviceAlertTime_Type()
)
deviceAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlertTime.setStatus("current")
_DeviceV1AlertMPS_ObjectIdentity = ObjectIdentity
deviceV1AlertMPS = _DeviceV1AlertMPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 2)
)
_DeviceV2AlertMPSPrefix_ObjectIdentity = ObjectIdentity
deviceV2AlertMPSPrefix = _DeviceV2AlertMPSPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 2, 0)
)
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 6)
)
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 6, 7)
)

# Managed Objects groups

deviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 1)
)
deviceGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "deviceMibLocalization"),
        ("LEXMARK-MPS-MIB", "devicePort"),
        ("LEXMARK-MPS-MIB", "deviceHrDeviceIndex"),
        ("LEXMARK-MPS-MIB", "deviceModel"),
        ("LEXMARK-MPS-MIB", "deviceSerialNumber"),
        ("LEXMARK-MPS-MIB", "deviceMibVersion"),
        ("LEXMARK-MPS-MIB", "deviceInstallDate"),
        ("LEXMARK-MPS-MIB", "deviceMibSupportLevel"))
)
if mibBuilder.loadTexts:
    deviceGroup.setStatus("current")

hwInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 2)
)
hwInventoryGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "hwInventoryParentIndex"),
        ("LEXMARK-MPS-MIB", "hwInventoryType"),
        ("LEXMARK-MPS-MIB", "hwInventoryAdminStatus"),
        ("LEXMARK-MPS-MIB", "hwInventoryStatus"),
        ("LEXMARK-MPS-MIB", "hwInventoryPartNumber"),
        ("LEXMARK-MPS-MIB", "hwInventorySerialNumber"),
        ("LEXMARK-MPS-MIB", "hwInventoryDescription"),
        ("LEXMARK-MPS-MIB", "hwInventoryData"))
)
if mibBuilder.loadTexts:
    hwInventoryGroup.setStatus("current")

supplyInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 3)
)
supplyInventoryGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "supplyInventoryType"),
        ("LEXMARK-MPS-MIB", "supplyInventoryColorantValue"),
        ("LEXMARK-MPS-MIB", "supplyInventoryDescription"))
)
if mibBuilder.loadTexts:
    supplyInventoryGroup.setStatus("current")

swInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 4)
)
swInventoryGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "swInventoryParentIndex"),
        ("LEXMARK-MPS-MIB", "swInventoryType"),
        ("LEXMARK-MPS-MIB", "swInventoryName"),
        ("LEXMARK-MPS-MIB", "swInventoryRevision"),
        ("LEXMARK-MPS-MIB", "swInventoryAdminStatus"),
        ("LEXMARK-MPS-MIB", "swInventoryStatus"),
        ("LEXMARK-MPS-MIB", "swInventoryDescription"),
        ("LEXMARK-MPS-MIB", "swInventoryHWIndex"),
        ("LEXMARK-MPS-MIB", "swInventoryData"))
)
if mibBuilder.loadTexts:
    swInventoryGroup.setStatus("current")

statsGeneralCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 5)
)
statsGeneralCountGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "genCountType"),
        ("LEXMARK-MPS-MIB", "genCountUnits"),
        ("LEXMARK-MPS-MIB", "genCountValue"))
)
if mibBuilder.loadTexts:
    statsGeneralCountGroup.setStatus("current")

statsPaperGeneralCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 6)
)
statsPaperGeneralCountGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "paperGeneralCountType"),
        ("LEXMARK-MPS-MIB", "paperGeneralCountUnits"),
        ("LEXMARK-MPS-MIB", "paperGeneralCountValue"))
)
if mibBuilder.loadTexts:
    statsPaperGeneralCountGroup.setStatus("current")

statsPaperSidesCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 7)
)
statsPaperSidesCountGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "paperSidesPaperSize"),
        ("LEXMARK-MPS-MIB", "paperSidesPaperType"),
        ("LEXMARK-MPS-MIB", "paperSidesMonoPicked"),
        ("LEXMARK-MPS-MIB", "paperSidesColorPicked"),
        ("LEXMARK-MPS-MIB", "paperSidesMonoSafe"),
        ("LEXMARK-MPS-MIB", "paperSidesColorSafe"))
)
if mibBuilder.loadTexts:
    statsPaperSidesCountGroup.setStatus("current")

statsPaperSheetsCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 8)
)
statsPaperSheetsCountGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "paperSheetsPaperSize"),
        ("LEXMARK-MPS-MIB", "paperSheetsPaperType"),
        ("LEXMARK-MPS-MIB", "paperSheetsPicked"),
        ("LEXMARK-MPS-MIB", "paperSheetsSafe"))
)
if mibBuilder.loadTexts:
    statsPaperSheetsCountGroup.setStatus("current")

statsPaperNupCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 9)
)
statsPaperNupCountGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "paperNupNumber"),
        ("LEXMARK-MPS-MIB", "paperNupSides"),
        ("LEXMARK-MPS-MIB", "paperNupLogicalSides"))
)
if mibBuilder.loadTexts:
    statsPaperNupCountGroup.setStatus("current")

statsPaperJobSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 10)
)
statsPaperJobSizeGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "paperJobSizeMinimum"),
        ("LEXMARK-MPS-MIB", "paperJobSizeMaximum"),
        ("LEXMARK-MPS-MIB", "paperJobSizeSideCount"),
        ("LEXMARK-MPS-MIB", "paperJobSizeJobCount"))
)
if mibBuilder.loadTexts:
    statsPaperJobSizeGroup.setStatus("current")

statsScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 11)
)
statsScanGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "scanCountType"),
        ("LEXMARK-MPS-MIB", "scanCountSize"),
        ("LEXMARK-MPS-MIB", "scanCountSides"),
        ("LEXMARK-MPS-MIB", "scanCountSheets"))
)
if mibBuilder.loadTexts:
    statsScanGroup.setStatus("current")

statsCurrentSuppliesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 12)
)
statsCurrentSuppliesGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "currentSupplyInventoryIndex"),
        ("LEXMARK-MPS-MIB", "currentSupplyType"),
        ("LEXMARK-MPS-MIB", "currentSupplyColorantValue"),
        ("LEXMARK-MPS-MIB", "currentSupplySerialNumber"),
        ("LEXMARK-MPS-MIB", "currentSupplyPartNumber"),
        ("LEXMARK-MPS-MIB", "currentSupplyCapacity"),
        ("LEXMARK-MPS-MIB", "currentSupplyPageCountAtInstall"),
        ("LEXMARK-MPS-MIB", "currentSupplyCapacityUnit"),
        ("LEXMARK-MPS-MIB", "currentSupplyClass"),
        ("LEXMARK-MPS-MIB", "currentSupplyCartridgeType"),
        ("LEXMARK-MPS-MIB", "currentSupplyInstallDate"),
        ("LEXMARK-MPS-MIB", "currentSupplyDescription"),
        ("LEXMARK-MPS-MIB", "currentSupplyCurrentLevel"),
        ("LEXMARK-MPS-MIB", "currentSupplyCurrentStatus"),
        ("LEXMARK-MPS-MIB", "currentSupplyUsage"),
        ("LEXMARK-MPS-MIB", "currentSupplyCoverage"),
        ("LEXMARK-MPS-MIB", "currentSupplyCalibrations"),
        ("LEXMARK-MPS-MIB", "currentSupplyFirstKnownLevel"))
)
if mibBuilder.loadTexts:
    statsCurrentSuppliesGroup.setStatus("current")

statsSupplyHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 13)
)
statsSupplyHistoryGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "supplyHistoryInventoryIndex"),
        ("LEXMARK-MPS-MIB", "supplyHistorySupplyType"),
        ("LEXMARK-MPS-MIB", "supplyHistoryColorantValue"),
        ("LEXMARK-MPS-MIB", "supplyHistoryDescription"),
        ("LEXMARK-MPS-MIB", "supplyHistorySerialNumber"),
        ("LEXMARK-MPS-MIB", "supplyHistoryCartridgeType"),
        ("LEXMARK-MPS-MIB", "supplyHistoryInstallDate"),
        ("LEXMARK-MPS-MIB", "supplyHistoryPageCount"),
        ("LEXMARK-MPS-MIB", "supplyHistoryCapacityUnit"),
        ("LEXMARK-MPS-MIB", "supplyHistoryCapacity"),
        ("LEXMARK-MPS-MIB", "supplyHistoryLastLevel"),
        ("LEXMARK-MPS-MIB", "supplyHistoryUsage"),
        ("LEXMARK-MPS-MIB", "supplyHistoryCalibrations"),
        ("LEXMARK-MPS-MIB", "supplyHistoryCoverage"))
)
if mibBuilder.loadTexts:
    statsSupplyHistoryGroup.setStatus("current")

statsSupplyHistogramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 14)
)
statsSupplyHistogramGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "supplyHistogramInventoryIndex"),
        ("LEXMARK-MPS-MIB", "supplyHistogramSupplyType"),
        ("LEXMARK-MPS-MIB", "supplyHistogramColorantValue"),
        ("LEXMARK-MPS-MIB", "supplyHistogramDescription"),
        ("LEXMARK-MPS-MIB", "supplyHistogramCapacityUnit"),
        ("LEXMARK-MPS-MIB", "supplyHistogramCapacity"),
        ("LEXMARK-MPS-MIB", "supplyHistogramCount"),
        ("LEXMARK-MPS-MIB", "supplyHistogramCountUnits"))
)
if mibBuilder.loadTexts:
    statsSupplyHistogramGroup.setStatus("current")

deviceAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 2, 16)
)
deviceAlertGroup.setObjects(
      *(("LEXMARK-MPS-MIB", "deviceAlertIndex"),
        ("LEXMARK-MPS-MIB", "deviceAlertConfigTableNode"),
        ("LEXMARK-MPS-MIB", "deviceAlertConfigTableIndex"),
        ("LEXMARK-MPS-MIB", "deviceAlertSeverity"),
        ("LEXMARK-MPS-MIB", "deviceAlertCode"),
        ("LEXMARK-MPS-MIB", "deviceAlertDescription"),
        ("LEXMARK-MPS-MIB", "deviceAlertData"),
        ("LEXMARK-MPS-MIB", "deviceAlertTime"))
)
if mibBuilder.loadTexts:
    deviceAlertGroup.setStatus("current")


# Notification objects

deviceV2AlertMPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 641, 6, 5, 2, 0, 1)
)
deviceV2AlertMPS.setObjects(
      *(("LEXMARK-MPS-MIB", "deviceAlertIndex"),
        ("LEXMARK-MPS-MIB", "deviceAlertConfigTableNode"),
        ("LEXMARK-MPS-MIB", "deviceAlertConfigTableIndex"),
        ("LEXMARK-MPS-MIB", "deviceAlertSeverity"),
        ("LEXMARK-MPS-MIB", "deviceAlertCode"),
        ("LEXMARK-MPS-MIB", "deviceAlertDescription"),
        ("LEXMARK-MPS-MIB", "deviceAlertData"),
        ("LEXMARK-MPS-MIB", "deviceAlertTime"))
)
if mibBuilder.loadTexts:
    deviceV2AlertMPS.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

mpsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 641, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEXMARK-MPS-MIB",
    **{"SupplyTypeTC": SupplyTypeTC,
       "CartridgeTypeTC": CartridgeTypeTC,
       "SeverityTC": SeverityTC,
       "AlertCodeTC": AlertCodeTC,
       "mpsMibModule": mpsMibModule,
       "mps": mps,
       "mpsMIBAdminInfo": mpsMIBAdminInfo,
       "mpsMIBCompliances": mpsMIBCompliances,
       "mpsMIBCompliance": mpsMIBCompliance,
       "mpsMIBGroups": mpsMIBGroups,
       "deviceGroup": deviceGroup,
       "hwInventoryGroup": hwInventoryGroup,
       "supplyInventoryGroup": supplyInventoryGroup,
       "swInventoryGroup": swInventoryGroup,
       "statsGeneralCountGroup": statsGeneralCountGroup,
       "statsPaperGeneralCountGroup": statsPaperGeneralCountGroup,
       "statsPaperSidesCountGroup": statsPaperSidesCountGroup,
       "statsPaperSheetsCountGroup": statsPaperSheetsCountGroup,
       "statsPaperNupCountGroup": statsPaperNupCountGroup,
       "statsPaperJobSizeGroup": statsPaperJobSizeGroup,
       "statsScanGroup": statsScanGroup,
       "statsCurrentSuppliesGroup": statsCurrentSuppliesGroup,
       "statsSupplyHistoryGroup": statsSupplyHistoryGroup,
       "statsSupplyHistogramGroup": statsSupplyHistogramGroup,
       "deviceAlertGroup": deviceAlertGroup,
       "device": device,
       "deviceMibLocalization": deviceMibLocalization,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "devicePort": devicePort,
       "deviceHrDeviceIndex": deviceHrDeviceIndex,
       "deviceModel": deviceModel,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceMibVersion": deviceMibVersion,
       "deviceInstallDate": deviceInstallDate,
       "deviceMibSupportLevel": deviceMibSupportLevel,
       "inventory": inventory,
       "hwInventoryTable": hwInventoryTable,
       "hwInventoryEntry": hwInventoryEntry,
       "hwInventoryIndex": hwInventoryIndex,
       "hwInventoryParentIndex": hwInventoryParentIndex,
       "hwInventoryType": hwInventoryType,
       "hwInventoryAdminStatus": hwInventoryAdminStatus,
       "hwInventoryStatus": hwInventoryStatus,
       "hwInventoryPartNumber": hwInventoryPartNumber,
       "hwInventorySerialNumber": hwInventorySerialNumber,
       "hwInventoryDescription": hwInventoryDescription,
       "hwInventoryData": hwInventoryData,
       "supplyInventoryTable": supplyInventoryTable,
       "supplyInventoryEntry": supplyInventoryEntry,
       "supplyInventoryIndex": supplyInventoryIndex,
       "supplyInventoryType": supplyInventoryType,
       "supplyInventoryColorantValue": supplyInventoryColorantValue,
       "supplyInventoryDescription": supplyInventoryDescription,
       "swInventoryTable": swInventoryTable,
       "swInventoryEntry": swInventoryEntry,
       "swInventoryIndex": swInventoryIndex,
       "swInventoryParentIndex": swInventoryParentIndex,
       "swInventoryType": swInventoryType,
       "swInventoryAdminStatus": swInventoryAdminStatus,
       "swInventoryStatus": swInventoryStatus,
       "swInventoryName": swInventoryName,
       "swInventoryRevision": swInventoryRevision,
       "swInventoryDescription": swInventoryDescription,
       "swInventoryHWIndex": swInventoryHWIndex,
       "swInventoryData": swInventoryData,
       "stats": stats,
       "generalStats": generalStats,
       "genCountTable": genCountTable,
       "genCountEntry": genCountEntry,
       "genCountIndex": genCountIndex,
       "genCountType": genCountType,
       "genCountUnits": genCountUnits,
       "genCountValue": genCountValue,
       "paperStats": paperStats,
       "paperGeneralCountTable": paperGeneralCountTable,
       "paperGeneralCountEntry": paperGeneralCountEntry,
       "paperGeneralCountIndex": paperGeneralCountIndex,
       "paperGeneralCountType": paperGeneralCountType,
       "paperGeneralCountUnits": paperGeneralCountUnits,
       "paperGeneralCountValue": paperGeneralCountValue,
       "paperSidesCountTable": paperSidesCountTable,
       "paperSidesCountEntry": paperSidesCountEntry,
       "paperSidesCountIndex": paperSidesCountIndex,
       "paperSidesPaperSize": paperSidesPaperSize,
       "paperSidesPaperType": paperSidesPaperType,
       "paperSidesMonoPicked": paperSidesMonoPicked,
       "paperSidesColorPicked": paperSidesColorPicked,
       "paperSidesMonoSafe": paperSidesMonoSafe,
       "paperSidesColorSafe": paperSidesColorSafe,
       "paperSheetsCountTable": paperSheetsCountTable,
       "paperSheetsCountEntry": paperSheetsCountEntry,
       "paperSheetsCountIndex": paperSheetsCountIndex,
       "paperSheetsPaperSize": paperSheetsPaperSize,
       "paperSheetsPaperType": paperSheetsPaperType,
       "paperSheetsPicked": paperSheetsPicked,
       "paperSheetsSafe": paperSheetsSafe,
       "paperNupCountTable": paperNupCountTable,
       "paperNupCountEntry": paperNupCountEntry,
       "paperNupCountIndex": paperNupCountIndex,
       "paperNupNumber": paperNupNumber,
       "paperNupSides": paperNupSides,
       "paperNupLogicalSides": paperNupLogicalSides,
       "paperJobSizeTable": paperJobSizeTable,
       "paperJobSizeEntry": paperJobSizeEntry,
       "paperJobSizeIndex": paperJobSizeIndex,
       "paperJobSizeMinimum": paperJobSizeMinimum,
       "paperJobSizeMaximum": paperJobSizeMaximum,
       "paperJobSizeSideCount": paperJobSizeSideCount,
       "paperJobSizeJobCount": paperJobSizeJobCount,
       "scanStats": scanStats,
       "scanCountTable": scanCountTable,
       "scanCountEntry": scanCountEntry,
       "scanCountIndex": scanCountIndex,
       "scanCountType": scanCountType,
       "scanCountSize": scanCountSize,
       "scanCountSides": scanCountSides,
       "scanCountSheets": scanCountSheets,
       "supplyStats": supplyStats,
       "currentSuppliesTable": currentSuppliesTable,
       "currentSuppliesEntry": currentSuppliesEntry,
       "currentSupplyIndex": currentSupplyIndex,
       "currentSupplyInventoryIndex": currentSupplyInventoryIndex,
       "currentSupplyType": currentSupplyType,
       "currentSupplyColorantValue": currentSupplyColorantValue,
       "currentSupplyDescription": currentSupplyDescription,
       "currentSupplySerialNumber": currentSupplySerialNumber,
       "currentSupplyPartNumber": currentSupplyPartNumber,
       "currentSupplyClass": currentSupplyClass,
       "currentSupplyCartridgeType": currentSupplyCartridgeType,
       "currentSupplyInstallDate": currentSupplyInstallDate,
       "currentSupplyPageCountAtInstall": currentSupplyPageCountAtInstall,
       "currentSupplyCurrentStatus": currentSupplyCurrentStatus,
       "currentSupplyCapacityUnit": currentSupplyCapacityUnit,
       "currentSupplyCapacity": currentSupplyCapacity,
       "currentSupplyFirstKnownLevel": currentSupplyFirstKnownLevel,
       "currentSupplyCurrentLevel": currentSupplyCurrentLevel,
       "currentSupplyUsage": currentSupplyUsage,
       "currentSupplyCalibrations": currentSupplyCalibrations,
       "currentSupplyCoverage": currentSupplyCoverage,
       "supplyHistoryTable": supplyHistoryTable,
       "supplyHistoryEntry": supplyHistoryEntry,
       "supplyHistoryIndex": supplyHistoryIndex,
       "supplyHistoryInventoryIndex": supplyHistoryInventoryIndex,
       "supplyHistorySupplyType": supplyHistorySupplyType,
       "supplyHistoryColorantValue": supplyHistoryColorantValue,
       "supplyHistoryDescription": supplyHistoryDescription,
       "supplyHistorySerialNumber": supplyHistorySerialNumber,
       "supplyHistoryCartridgeType": supplyHistoryCartridgeType,
       "supplyHistoryInstallDate": supplyHistoryInstallDate,
       "supplyHistoryPageCount": supplyHistoryPageCount,
       "supplyHistoryCapacityUnit": supplyHistoryCapacityUnit,
       "supplyHistoryCapacity": supplyHistoryCapacity,
       "supplyHistoryLastLevel": supplyHistoryLastLevel,
       "supplyHistoryUsage": supplyHistoryUsage,
       "supplyHistoryCalibrations": supplyHistoryCalibrations,
       "supplyHistoryCoverage": supplyHistoryCoverage,
       "supplyHistogramTable": supplyHistogramTable,
       "supplyHistogramEntry": supplyHistogramEntry,
       "supplyHistogramIndex": supplyHistogramIndex,
       "supplyHistogramInventoryIndex": supplyHistogramInventoryIndex,
       "supplyHistogramSupplyType": supplyHistogramSupplyType,
       "supplyHistogramColorantValue": supplyHistogramColorantValue,
       "supplyHistogramDescription": supplyHistogramDescription,
       "supplyHistogramCapacityUnit": supplyHistogramCapacityUnit,
       "supplyHistogramCapacity": supplyHistogramCapacity,
       "supplyHistogramCount": supplyHistogramCount,
       "supplyHistogramCountUnits": supplyHistogramCountUnits,
       "alerts": alerts,
       "deviceAlertTable": deviceAlertTable,
       "deviceAlertEntry": deviceAlertEntry,
       "deviceAlertIndex": deviceAlertIndex,
       "deviceAlertConfigTableNode": deviceAlertConfigTableNode,
       "deviceAlertConfigTableIndex": deviceAlertConfigTableIndex,
       "deviceAlertSeverity": deviceAlertSeverity,
       "deviceAlertCode": deviceAlertCode,
       "deviceAlertDescription": deviceAlertDescription,
       "deviceAlertData": deviceAlertData,
       "deviceAlertTime": deviceAlertTime,
       "deviceV1AlertMPS": deviceV1AlertMPS,
       "deviceV2AlertMPSPrefix": deviceV2AlertMPSPrefix,
       "deviceV2AlertMPS": deviceV2AlertMPS,
       "logs": logs,
       "applications": applications}
)
