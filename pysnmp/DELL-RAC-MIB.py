# SNMP MIB module (DELL-RAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-RAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:02 2024
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



class DellString(DisplayString):
    """Custom type DellString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )





class DellRacType(Integer32):
    """Custom type DellRacType based on Integer32"""
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
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cmc", 8),
          ("drac4", 5),
          ("drac5", 6),
          ("drac5MC", 7),
          ("dracIII", 3),
          ("era", 4),
          ("fx2CMC", 19),
          ("idrac", 9),
          ("other", 1),
          ("unknown", 2),
          ("vrtxCMC", 18))
    )





class DellStatus(Integer32):
    """Custom type DellStatus based on Integer32"""
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
          ("nonCritical", 4),
          ("nonRecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )





class DellPowerReading(DisplayString):
    """Custom type DellPowerReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )





class DellCMCPowerIndexRange(Integer32):
    """Custom type DellCMCPowerIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )





class DellCMCPSUIndexRange(Integer32):
    """Custom type DellCMCPSUIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class DellCMCPSUCapable(Integer32):
    """Custom type DellCMCPSUCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("basic", 3),
          ("none", 2))
    )





class DellTemperatureReading(Integer32):
    """Custom type DellTemperatureReading based on Integer32"""




class DellTimestamp(DisplayString):
    """Custom type DellTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )





class DellCMCServerIndexRange(Integer32):
    """Custom type DellCMCServerIndexRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )





class DellCMCServerCapable(Integer32):
    """Custom type DellCMCServerCapable based on Integer32"""
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
        *(("absent", 1),
          ("basic", 3),
          ("none", 2),
          ("off", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server3_ObjectIdentity = ObjectIdentity
server3 = _Server3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892)
)
_DrsOutofBandGroup_ObjectIdentity = ObjectIdentity
drsOutofBandGroup = _DrsOutofBandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2)
)
_DrsInformationGroup_ObjectIdentity = ObjectIdentity
drsInformationGroup = _DrsInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1)
)
_DrsProductInfoGroup_ObjectIdentity = ObjectIdentity
drsProductInfoGroup = _DrsProductInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1)
)
_DrsProductName_Type = DellString
_DrsProductName_Object = MibScalar
drsProductName = _DrsProductName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 1),
    _DrsProductName_Type()
)
drsProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductName.setStatus("mandatory")
_DrsProductShortName_Type = DellString
_DrsProductShortName_Object = MibScalar
drsProductShortName = _DrsProductShortName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 2),
    _DrsProductShortName_Type()
)
drsProductShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductShortName.setStatus("mandatory")
_DrsProductDescription_Type = DellString
_DrsProductDescription_Object = MibScalar
drsProductDescription = _DrsProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 3),
    _DrsProductDescription_Type()
)
drsProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductDescription.setStatus("mandatory")
_DrsProductManufacturer_Type = DellString
_DrsProductManufacturer_Object = MibScalar
drsProductManufacturer = _DrsProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 4),
    _DrsProductManufacturer_Type()
)
drsProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductManufacturer.setStatus("mandatory")
_DrsProductVersion_Type = DellString
_DrsProductVersion_Object = MibScalar
drsProductVersion = _DrsProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 5),
    _DrsProductVersion_Type()
)
drsProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductVersion.setStatus("mandatory")
_DrsChassisServiceTag_Type = DellString
_DrsChassisServiceTag_Object = MibScalar
drsChassisServiceTag = _DrsChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 6),
    _DrsChassisServiceTag_Type()
)
drsChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisServiceTag.setStatus("mandatory")
_DrsProductURL_Type = DellString
_DrsProductURL_Object = MibScalar
drsProductURL = _DrsProductURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 7),
    _DrsProductURL_Type()
)
drsProductURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductURL.setStatus("mandatory")
_DrsProductChassisAssetTag_Type = DellString
_DrsProductChassisAssetTag_Object = MibScalar
drsProductChassisAssetTag = _DrsProductChassisAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 8),
    _DrsProductChassisAssetTag_Type()
)
drsProductChassisAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisAssetTag.setStatus("mandatory")
_DrsProductChassisLocation_Type = DellString
_DrsProductChassisLocation_Object = MibScalar
drsProductChassisLocation = _DrsProductChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 9),
    _DrsProductChassisLocation_Type()
)
drsProductChassisLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisLocation.setStatus("mandatory")
_DrsProductChassisName_Type = DellString
_DrsProductChassisName_Object = MibScalar
drsProductChassisName = _DrsProductChassisName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 10),
    _DrsProductChassisName_Type()
)
drsProductChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisName.setStatus("mandatory")
_DrsSystemServiceTag_Type = DellString
_DrsSystemServiceTag_Object = MibScalar
drsSystemServiceTag = _DrsSystemServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 11),
    _DrsSystemServiceTag_Type()
)
drsSystemServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsSystemServiceTag.setStatus("mandatory")
_DrsProductSystemAssetTag_Type = DellString
_DrsProductSystemAssetTag_Object = MibScalar
drsProductSystemAssetTag = _DrsProductSystemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 12),
    _DrsProductSystemAssetTag_Type()
)
drsProductSystemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductSystemAssetTag.setStatus("mandatory")
_DrsProductSystemSlot_Type = DellString
_DrsProductSystemSlot_Object = MibScalar
drsProductSystemSlot = _DrsProductSystemSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 13),
    _DrsProductSystemSlot_Type()
)
drsProductSystemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductSystemSlot.setStatus("mandatory")
_DrsProductType_Type = DellRacType
_DrsProductType_Object = MibScalar
drsProductType = _DrsProductType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 14),
    _DrsProductType_Type()
)
drsProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductType.setStatus("mandatory")
_DrsProductChassisDataCenter_Type = DellString
_DrsProductChassisDataCenter_Object = MibScalar
drsProductChassisDataCenter = _DrsProductChassisDataCenter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 15),
    _DrsProductChassisDataCenter_Type()
)
drsProductChassisDataCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisDataCenter.setStatus("mandatory")
_DrsProductChassisAisle_Type = DellString
_DrsProductChassisAisle_Object = MibScalar
drsProductChassisAisle = _DrsProductChassisAisle_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 16),
    _DrsProductChassisAisle_Type()
)
drsProductChassisAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisAisle.setStatus("mandatory")
_DrsProductChassisRack_Type = DellString
_DrsProductChassisRack_Object = MibScalar
drsProductChassisRack = _DrsProductChassisRack_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 17),
    _DrsProductChassisRack_Type()
)
drsProductChassisRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisRack.setStatus("mandatory")
_DrsProductChassisRackSlot_Type = DellString
_DrsProductChassisRackSlot_Object = MibScalar
drsProductChassisRackSlot = _DrsProductChassisRackSlot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 18),
    _DrsProductChassisRackSlot_Type()
)
drsProductChassisRackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisRackSlot.setStatus("mandatory")
_DrsProductChassisModel_Type = DellString
_DrsProductChassisModel_Object = MibScalar
drsProductChassisModel = _DrsProductChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 19),
    _DrsProductChassisModel_Type()
)
drsProductChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisModel.setStatus("mandatory")
_DrsProductChassisExpressServiceCode_Type = DellString
_DrsProductChassisExpressServiceCode_Object = MibScalar
drsProductChassisExpressServiceCode = _DrsProductChassisExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 20),
    _DrsProductChassisExpressServiceCode_Type()
)
drsProductChassisExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisExpressServiceCode.setStatus("mandatory")
_DrsProductChassisSystemID_Type = Integer32
_DrsProductChassisSystemID_Object = MibScalar
drsProductChassisSystemID = _DrsProductChassisSystemID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 21),
    _DrsProductChassisSystemID_Type()
)
drsProductChassisSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisSystemID.setStatus("mandatory")
_DrsProductChassisSize_Type = Integer32
_DrsProductChassisSize_Object = MibScalar
drsProductChassisSize = _DrsProductChassisSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 1, 22),
    _DrsProductChassisSize_Type()
)
drsProductChassisSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsProductChassisSize.setStatus("mandatory")
_DrsFirmwareGroup_ObjectIdentity = ObjectIdentity
drsFirmwareGroup = _DrsFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2)
)
_DrsFirmwareVersion_Type = DellString
_DrsFirmwareVersion_Object = MibScalar
drsFirmwareVersion = _DrsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 1),
    _DrsFirmwareVersion_Type()
)
drsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFirmwareVersion.setStatus("mandatory")
_DrsiKVMFirmwareVersion_Type = DellString
_DrsiKVMFirmwareVersion_Object = MibScalar
drsiKVMFirmwareVersion = _DrsiKVMFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 2),
    _DrsiKVMFirmwareVersion_Type()
)
drsiKVMFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsiKVMFirmwareVersion.setStatus("mandatory")
_DrsFirmwareVersion2_Type = DellString
_DrsFirmwareVersion2_Object = MibScalar
drsFirmwareVersion2 = _DrsFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 1, 2, 3),
    _DrsFirmwareVersion2_Type()
)
drsFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFirmwareVersion2.setStatus("mandatory")
_DrsStatusGroup_ObjectIdentity = ObjectIdentity
drsStatusGroup = _DrsStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 2)
)
_DrsGlobalSystemStatus_Type = DellStatus
_DrsGlobalSystemStatus_Object = MibScalar
drsGlobalSystemStatus = _DrsGlobalSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 2, 1),
    _DrsGlobalSystemStatus_Type()
)
drsGlobalSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalSystemStatus.setStatus("mandatory")
_DrsChassisStatusGroup_ObjectIdentity = ObjectIdentity
drsChassisStatusGroup = _DrsChassisStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3)
)
_DrsStatusNowGroup_ObjectIdentity = ObjectIdentity
drsStatusNowGroup = _DrsStatusNowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1)
)
_DrsGlobalCurrStatus_Type = DellStatus
_DrsGlobalCurrStatus_Object = MibScalar
drsGlobalCurrStatus = _DrsGlobalCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 1),
    _DrsGlobalCurrStatus_Type()
)
drsGlobalCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalCurrStatus.setStatus("mandatory")
_DrsIOMCurrStatus_Type = DellStatus
_DrsIOMCurrStatus_Object = MibScalar
drsIOMCurrStatus = _DrsIOMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 2),
    _DrsIOMCurrStatus_Type()
)
drsIOMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMCurrStatus.setStatus("mandatory")
_DrsKVMCurrStatus_Type = DellStatus
_DrsKVMCurrStatus_Object = MibScalar
drsKVMCurrStatus = _DrsKVMCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 3),
    _DrsKVMCurrStatus_Type()
)
drsKVMCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMCurrStatus.setStatus("mandatory")
_DrsRedCurrStatus_Type = DellStatus
_DrsRedCurrStatus_Object = MibScalar
drsRedCurrStatus = _DrsRedCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 4),
    _DrsRedCurrStatus_Type()
)
drsRedCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedCurrStatus.setStatus("mandatory")
_DrsPowerCurrStatus_Type = DellStatus
_DrsPowerCurrStatus_Object = MibScalar
drsPowerCurrStatus = _DrsPowerCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 5),
    _DrsPowerCurrStatus_Type()
)
drsPowerCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerCurrStatus.setStatus("mandatory")
_DrsFanCurrStatus_Type = DellStatus
_DrsFanCurrStatus_Object = MibScalar
drsFanCurrStatus = _DrsFanCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 6),
    _DrsFanCurrStatus_Type()
)
drsFanCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanCurrStatus.setStatus("mandatory")
_DrsBladeCurrStatus_Type = DellStatus
_DrsBladeCurrStatus_Object = MibScalar
drsBladeCurrStatus = _DrsBladeCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 7),
    _DrsBladeCurrStatus_Type()
)
drsBladeCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladeCurrStatus.setStatus("mandatory")
_DrsTempCurrStatus_Type = DellStatus
_DrsTempCurrStatus_Object = MibScalar
drsTempCurrStatus = _DrsTempCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 8),
    _DrsTempCurrStatus_Type()
)
drsTempCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempCurrStatus.setStatus("mandatory")
_DrsCMCCurrStatus_Type = DellStatus
_DrsCMCCurrStatus_Object = MibScalar
drsCMCCurrStatus = _DrsCMCCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 9),
    _DrsCMCCurrStatus_Type()
)
drsCMCCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCCurrStatus.setStatus("mandatory")
_DrsChassisFrontPanelAmbientTemperature_Type = DellTemperatureReading
_DrsChassisFrontPanelAmbientTemperature_Object = MibScalar
drsChassisFrontPanelAmbientTemperature = _DrsChassisFrontPanelAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 10),
    _DrsChassisFrontPanelAmbientTemperature_Type()
)
drsChassisFrontPanelAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisFrontPanelAmbientTemperature.setStatus("mandatory")
_DrsCMCAmbientTemperature_Type = DellTemperatureReading
_DrsCMCAmbientTemperature_Object = MibScalar
drsCMCAmbientTemperature = _DrsCMCAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 11),
    _DrsCMCAmbientTemperature_Type()
)
drsCMCAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCAmbientTemperature.setStatus("mandatory")
_DrsCMCProcessorTemperature_Type = DellTemperatureReading
_DrsCMCProcessorTemperature_Object = MibScalar
drsCMCProcessorTemperature = _DrsCMCProcessorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 1, 12),
    _DrsCMCProcessorTemperature_Type()
)
drsCMCProcessorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCProcessorTemperature.setStatus("mandatory")
_DrsStatusPrevGroup_ObjectIdentity = ObjectIdentity
drsStatusPrevGroup = _DrsStatusPrevGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2)
)
_DrsGlobalPrevStatus_Type = DellStatus
_DrsGlobalPrevStatus_Object = MibScalar
drsGlobalPrevStatus = _DrsGlobalPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 1),
    _DrsGlobalPrevStatus_Type()
)
drsGlobalPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalPrevStatus.setStatus("mandatory")
_DrsIOMPrevStatus_Type = DellStatus
_DrsIOMPrevStatus_Object = MibScalar
drsIOMPrevStatus = _DrsIOMPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 2),
    _DrsIOMPrevStatus_Type()
)
drsIOMPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMPrevStatus.setStatus("mandatory")
_DrsKVMPrevStatus_Type = DellStatus
_DrsKVMPrevStatus_Object = MibScalar
drsKVMPrevStatus = _DrsKVMPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 3),
    _DrsKVMPrevStatus_Type()
)
drsKVMPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMPrevStatus.setStatus("mandatory")
_DrsRedPrevStatus_Type = DellStatus
_DrsRedPrevStatus_Object = MibScalar
drsRedPrevStatus = _DrsRedPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 4),
    _DrsRedPrevStatus_Type()
)
drsRedPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedPrevStatus.setStatus("mandatory")
_DrsPowerPrevStatus_Type = DellStatus
_DrsPowerPrevStatus_Object = MibScalar
drsPowerPrevStatus = _DrsPowerPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 5),
    _DrsPowerPrevStatus_Type()
)
drsPowerPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerPrevStatus.setStatus("mandatory")
_DrsFanPrevStatus_Type = DellStatus
_DrsFanPrevStatus_Object = MibScalar
drsFanPrevStatus = _DrsFanPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 6),
    _DrsFanPrevStatus_Type()
)
drsFanPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanPrevStatus.setStatus("mandatory")
_DrsBladePrevStatus_Type = DellStatus
_DrsBladePrevStatus_Object = MibScalar
drsBladePrevStatus = _DrsBladePrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 7),
    _DrsBladePrevStatus_Type()
)
drsBladePrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladePrevStatus.setStatus("mandatory")
_DrsTempPrevStatus_Type = DellStatus
_DrsTempPrevStatus_Object = MibScalar
drsTempPrevStatus = _DrsTempPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 8),
    _DrsTempPrevStatus_Type()
)
drsTempPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempPrevStatus.setStatus("mandatory")
_DrsCMCPrevStatus_Type = DellStatus
_DrsCMCPrevStatus_Object = MibScalar
drsCMCPrevStatus = _DrsCMCPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 2, 9),
    _DrsCMCPrevStatus_Type()
)
drsCMCPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCPrevStatus.setStatus("mandatory")
_DrsStatusChangeGroup_ObjectIdentity = ObjectIdentity
drsStatusChangeGroup = _DrsStatusChangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3)
)
_DrsGlobalChangeTime_Type = TimeTicks
_DrsGlobalChangeTime_Object = MibScalar
drsGlobalChangeTime = _DrsGlobalChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 1),
    _DrsGlobalChangeTime_Type()
)
drsGlobalChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsGlobalChangeTime.setStatus("mandatory")
_DrsIOMChangeTime_Type = TimeTicks
_DrsIOMChangeTime_Object = MibScalar
drsIOMChangeTime = _DrsIOMChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 2),
    _DrsIOMChangeTime_Type()
)
drsIOMChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIOMChangeTime.setStatus("mandatory")
_DrsKVMChangeTime_Type = TimeTicks
_DrsKVMChangeTime_Object = MibScalar
drsKVMChangeTime = _DrsKVMChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 3),
    _DrsKVMChangeTime_Type()
)
drsKVMChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKVMChangeTime.setStatus("mandatory")
_DrsRedChangeTime_Type = TimeTicks
_DrsRedChangeTime_Object = MibScalar
drsRedChangeTime = _DrsRedChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 4),
    _DrsRedChangeTime_Type()
)
drsRedChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsRedChangeTime.setStatus("mandatory")
_DrsPowerChangeTime_Type = TimeTicks
_DrsPowerChangeTime_Object = MibScalar
drsPowerChangeTime = _DrsPowerChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 5),
    _DrsPowerChangeTime_Type()
)
drsPowerChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerChangeTime.setStatus("mandatory")
_DrsFanChangeTime_Type = TimeTicks
_DrsFanChangeTime_Object = MibScalar
drsFanChangeTime = _DrsFanChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 6),
    _DrsFanChangeTime_Type()
)
drsFanChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsFanChangeTime.setStatus("mandatory")
_DrsBladeChangeTime_Type = TimeTicks
_DrsBladeChangeTime_Object = MibScalar
drsBladeChangeTime = _DrsBladeChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 7),
    _DrsBladeChangeTime_Type()
)
drsBladeChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsBladeChangeTime.setStatus("mandatory")
_DrsTempChangeTime_Type = TimeTicks
_DrsTempChangeTime_Object = MibScalar
drsTempChangeTime = _DrsTempChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 8),
    _DrsTempChangeTime_Type()
)
drsTempChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsTempChangeTime.setStatus("mandatory")
_DrsCMCChangeTime_Type = TimeTicks
_DrsCMCChangeTime_Object = MibScalar
drsCMCChangeTime = _DrsCMCChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 3, 3, 9),
    _DrsCMCChangeTime_Type()
)
drsCMCChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCMCChangeTime.setStatus("mandatory")
_DrsChassisPowerGroup_ObjectIdentity = ObjectIdentity
drsChassisPowerGroup = _DrsChassisPowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4)
)
_DrsCMCPowerTable_Object = MibTable
drsCMCPowerTable = _DrsCMCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1)
)
if mibBuilder.loadTexts:
    drsCMCPowerTable.setStatus("mandatory")
_DrsCMCPowerTableEntry_Object = MibTableRow
drsCMCPowerTableEntry = _DrsCMCPowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1)
)
drsCMCPowerTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsChassisIndex"),
)
if mibBuilder.loadTexts:
    drsCMCPowerTableEntry.setStatus("mandatory")
_DrsChassisIndex_Type = DellCMCPowerIndexRange
_DrsChassisIndex_Object = MibTableColumn
drsChassisIndex = _DrsChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 1),
    _DrsChassisIndex_Type()
)
drsChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsChassisIndex.setStatus("mandatory")
_DrsPotentialPower_Type = DellPowerReading
_DrsPotentialPower_Object = MibTableColumn
drsPotentialPower = _DrsPotentialPower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 2),
    _DrsPotentialPower_Type()
)
drsPotentialPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPotentialPower.setStatus("mandatory")
_DrsIdlePower_Type = DellPowerReading
_DrsIdlePower_Object = MibTableColumn
drsIdlePower = _DrsIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 3),
    _DrsIdlePower_Type()
)
drsIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsIdlePower.setStatus("mandatory")
_DrsMaxPowerSpecification_Type = DellPowerReading
_DrsMaxPowerSpecification_Object = MibTableColumn
drsMaxPowerSpecification = _DrsMaxPowerSpecification_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 4),
    _DrsMaxPowerSpecification_Type()
)
drsMaxPowerSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsMaxPowerSpecification.setStatus("mandatory")
_DrsPowerSurplus_Type = DellPowerReading
_DrsPowerSurplus_Object = MibTableColumn
drsPowerSurplus = _DrsPowerSurplus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 5),
    _DrsPowerSurplus_Type()
)
drsPowerSurplus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPowerSurplus.setStatus("mandatory")
_DrsKWhCumulative_Type = DellPowerReading
_DrsKWhCumulative_Object = MibTableColumn
drsKWhCumulative = _DrsKWhCumulative_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 6),
    _DrsKWhCumulative_Type()
)
drsKWhCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKWhCumulative.setStatus("mandatory")
_DrsKWhCumulativeTime_Type = DellTimestamp
_DrsKWhCumulativeTime_Object = MibTableColumn
drsKWhCumulativeTime = _DrsKWhCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 7),
    _DrsKWhCumulativeTime_Type()
)
drsKWhCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsKWhCumulativeTime.setStatus("mandatory")
_DrsWattsPeakUsage_Type = DellPowerReading
_DrsWattsPeakUsage_Object = MibTableColumn
drsWattsPeakUsage = _DrsWattsPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 8),
    _DrsWattsPeakUsage_Type()
)
drsWattsPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsPeakUsage.setStatus("mandatory")
_DrsWattsPeakTime_Type = DellTimestamp
_DrsWattsPeakTime_Object = MibTableColumn
drsWattsPeakTime = _DrsWattsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 9),
    _DrsWattsPeakTime_Type()
)
drsWattsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsPeakTime.setStatus("mandatory")
_DrsWattsMinUsage_Type = DellPowerReading
_DrsWattsMinUsage_Object = MibTableColumn
drsWattsMinUsage = _DrsWattsMinUsage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 10),
    _DrsWattsMinUsage_Type()
)
drsWattsMinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsMinUsage.setStatus("mandatory")
_DrsWattsMinTime_Type = DellTimestamp
_DrsWattsMinTime_Object = MibTableColumn
drsWattsMinTime = _DrsWattsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 11),
    _DrsWattsMinTime_Type()
)
drsWattsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsMinTime.setStatus("mandatory")
_DrsWattsResetTime_Type = DellTimestamp
_DrsWattsResetTime_Object = MibTableColumn
drsWattsResetTime = _DrsWattsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 12),
    _DrsWattsResetTime_Type()
)
drsWattsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsResetTime.setStatus("mandatory")
_DrsWattsReading_Type = DellPowerReading
_DrsWattsReading_Object = MibTableColumn
drsWattsReading = _DrsWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 13),
    _DrsWattsReading_Type()
)
drsWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsWattsReading.setStatus("mandatory")
_DrsAmpsReading_Type = DellPowerReading
_DrsAmpsReading_Object = MibTableColumn
drsAmpsReading = _DrsAmpsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 1, 1, 14),
    _DrsAmpsReading_Type()
)
drsAmpsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAmpsReading.setStatus("mandatory")
_DrsCMCPSUTable_Object = MibTable
drsCMCPSUTable = _DrsCMCPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2)
)
if mibBuilder.loadTexts:
    drsCMCPSUTable.setStatus("mandatory")
_DrsCMCPSUTableEntry_Object = MibTableRow
drsCMCPSUTableEntry = _DrsCMCPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1)
)
drsCMCPSUTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsPSUChassisIndex"),
    (0, "DELL-RAC-MIB", "drsPSUIndex"),
)
if mibBuilder.loadTexts:
    drsCMCPSUTableEntry.setStatus("mandatory")
_DrsPSUChassisIndex_Type = DellCMCPowerIndexRange
_DrsPSUChassisIndex_Object = MibTableColumn
drsPSUChassisIndex = _DrsPSUChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 1),
    _DrsPSUChassisIndex_Type()
)
drsPSUChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUChassisIndex.setStatus("mandatory")
_DrsPSUIndex_Type = DellCMCPSUIndexRange
_DrsPSUIndex_Object = MibTableColumn
drsPSUIndex = _DrsPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 2),
    _DrsPSUIndex_Type()
)
drsPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUIndex.setStatus("mandatory")
_DrsPSULocation_Type = DellString
_DrsPSULocation_Object = MibTableColumn
drsPSULocation = _DrsPSULocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 3),
    _DrsPSULocation_Type()
)
drsPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSULocation.setStatus("mandatory")
_DrsPSUMonitoringCapable_Type = DellCMCPSUCapable
_DrsPSUMonitoringCapable_Object = MibTableColumn
drsPSUMonitoringCapable = _DrsPSUMonitoringCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 4),
    _DrsPSUMonitoringCapable_Type()
)
drsPSUMonitoringCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUMonitoringCapable.setStatus("mandatory")
_DrsPSUVoltsReading_Type = DellPowerReading
_DrsPSUVoltsReading_Object = MibTableColumn
drsPSUVoltsReading = _DrsPSUVoltsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 5),
    _DrsPSUVoltsReading_Type()
)
drsPSUVoltsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUVoltsReading.setStatus("mandatory")
_DrsPSUAmpsReading_Type = DellPowerReading
_DrsPSUAmpsReading_Object = MibTableColumn
drsPSUAmpsReading = _DrsPSUAmpsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 6),
    _DrsPSUAmpsReading_Type()
)
drsPSUAmpsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUAmpsReading.setStatus("mandatory")
_DrsPSUWattsReading_Type = DellPowerReading
_DrsPSUWattsReading_Object = MibTableColumn
drsPSUWattsReading = _DrsPSUWattsReading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 4, 2, 1, 7),
    _DrsPSUWattsReading_Type()
)
drsPSUWattsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsPSUWattsReading.setStatus("mandatory")
_DrsChassisServerGroup_ObjectIdentity = ObjectIdentity
drsChassisServerGroup = _DrsChassisServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5)
)
_DrsCMCServerTable_Object = MibTable
drsCMCServerTable = _DrsCMCServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1)
)
if mibBuilder.loadTexts:
    drsCMCServerTable.setStatus("mandatory")
_DrsCMCServerTableEntry_Object = MibTableRow
drsCMCServerTableEntry = _DrsCMCServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1)
)
drsCMCServerTableEntry.setIndexNames(
    (0, "DELL-RAC-MIB", "drsServerIndex"),
)
if mibBuilder.loadTexts:
    drsCMCServerTableEntry.setStatus("mandatory")
_DrsServerIndex_Type = DellCMCServerIndexRange
_DrsServerIndex_Object = MibTableColumn
drsServerIndex = _DrsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 1),
    _DrsServerIndex_Type()
)
drsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerIndex.setStatus("mandatory")
_DrsServerMonitoringCapable_Type = DellCMCServerCapable
_DrsServerMonitoringCapable_Object = MibTableColumn
drsServerMonitoringCapable = _DrsServerMonitoringCapable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 2),
    _DrsServerMonitoringCapable_Type()
)
drsServerMonitoringCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerMonitoringCapable.setStatus("mandatory")
_DrsServerServiceTag_Type = DellString
_DrsServerServiceTag_Object = MibTableColumn
drsServerServiceTag = _DrsServerServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 3),
    _DrsServerServiceTag_Type()
)
drsServerServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerServiceTag.setStatus("mandatory")
_DrsServerSlotName_Type = DellString
_DrsServerSlotName_Object = MibTableColumn
drsServerSlotName = _DrsServerSlotName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 4),
    _DrsServerSlotName_Type()
)
drsServerSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerSlotName.setStatus("mandatory")
_DrsServerSlotNumber_Type = DellString
_DrsServerSlotNumber_Object = MibTableColumn
drsServerSlotNumber = _DrsServerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 5),
    _DrsServerSlotNumber_Type()
)
drsServerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerSlotNumber.setStatus("mandatory")
_DrsServerNodeID_Type = DellString
_DrsServerNodeID_Object = MibTableColumn
drsServerNodeID = _DrsServerNodeID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5, 1, 1, 6),
    _DrsServerNodeID_Type()
)
drsServerNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsServerNodeID.setStatus("mandatory")
_DrsCMCAlertGroup_ObjectIdentity = ObjectIdentity
drsCMCAlertGroup = _DrsCMCAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20)
)
_DrsChassisAlertVariables_ObjectIdentity = ObjectIdentity
drsChassisAlertVariables = _DrsChassisAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10)
)
_DrsCASubSystem_Type = DellString
_DrsCASubSystem_Object = MibScalar
drsCASubSystem = _DrsCASubSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 1),
    _DrsCASubSystem_Type()
)
drsCASubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASubSystem.setStatus("mandatory")
_DrsCASSCurrStatus_Type = DellStatus
_DrsCASSCurrStatus_Object = MibScalar
drsCASSCurrStatus = _DrsCASSCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 2),
    _DrsCASSCurrStatus_Type()
)
drsCASSCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSCurrStatus.setStatus("mandatory")
_DrsCASSPrevStatus_Type = DellStatus
_DrsCASSPrevStatus_Object = MibScalar
drsCASSPrevStatus = _DrsCASSPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 3),
    _DrsCASSPrevStatus_Type()
)
drsCASSPrevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSPrevStatus.setStatus("mandatory")
_DrsCASSChangeTime_Type = TimeTicks
_DrsCASSChangeTime_Object = MibScalar
drsCASSChangeTime = _DrsCASSChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 4),
    _DrsCASSChangeTime_Type()
)
drsCASSChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCASSChangeTime.setStatus("mandatory")
_DrsCAMessage_Type = DellString
_DrsCAMessage_Object = MibScalar
drsCAMessage = _DrsCAMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 20, 10, 5),
    _DrsCAMessage_Type()
)
drsCAMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCAMessage.setStatus("mandatory")
_DrsCMCAlert2Group_ObjectIdentity = ObjectIdentity
drsCMCAlert2Group = _DrsCMCAlert2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21)
)
_DrsChassisAlert2Variables_ObjectIdentity = ObjectIdentity
drsChassisAlert2Variables = _DrsChassisAlert2Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10)
)


class _DrsCA2MessageID_Type(DisplayString):
    """Custom type drsCA2MessageID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DrsCA2MessageID_Type.__name__ = "DisplayString"
_DrsCA2MessageID_Object = MibScalar
drsCA2MessageID = _DrsCA2MessageID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 1),
    _DrsCA2MessageID_Type()
)
drsCA2MessageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2MessageID.setStatus("mandatory")
_DrsCA2Message_Type = DellString
_DrsCA2Message_Object = MibScalar
drsCA2Message = _DrsCA2Message_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 2),
    _DrsCA2Message_Type()
)
drsCA2Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2Message.setStatus("mandatory")
_DrsCA2MessageArgs_Type = DellString
_DrsCA2MessageArgs_Object = MibScalar
drsCA2MessageArgs = _DrsCA2MessageArgs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 3),
    _DrsCA2MessageArgs_Type()
)
drsCA2MessageArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2MessageArgs.setStatus("mandatory")
_DrsCA2AlertStatus_Type = DellStatus
_DrsCA2AlertStatus_Object = MibScalar
drsCA2AlertStatus = _DrsCA2AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 4),
    _DrsCA2AlertStatus_Type()
)
drsCA2AlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2AlertStatus.setStatus("mandatory")


class _DrsCA2FQDD_Type(DisplayString):
    """Custom type drsCA2FQDD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DrsCA2FQDD_Type.__name__ = "DisplayString"
_DrsCA2FQDD_Object = MibScalar
drsCA2FQDD = _DrsCA2FQDD_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 10, 5),
    _DrsCA2FQDD_Type()
)
drsCA2FQDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsCA2FQDD.setStatus("mandatory")
_DrsAlertGroup_ObjectIdentity = ObjectIdentity
drsAlertGroup = _DrsAlertGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000)
)
_DrsAlertVariables_ObjectIdentity = ObjectIdentity
drsAlertVariables = _DrsAlertVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10)
)


class _DrsAlertSystem_Type(OctetString):
    """Custom type drsAlertSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DrsAlertSystem_Type.__name__ = "OctetString"
_DrsAlertSystem_Object = MibScalar
drsAlertSystem = _DrsAlertSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 1),
    _DrsAlertSystem_Type()
)
drsAlertSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertSystem.setStatus("mandatory")
_DrsAlertTableIndexOID_Type = ObjectIdentifier
_DrsAlertTableIndexOID_Object = MibScalar
drsAlertTableIndexOID = _DrsAlertTableIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 2),
    _DrsAlertTableIndexOID_Type()
)
drsAlertTableIndexOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertTableIndexOID.setStatus("mandatory")


class _DrsAlertMessage_Type(OctetString):
    """Custom type drsAlertMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DrsAlertMessage_Type.__name__ = "OctetString"
_DrsAlertMessage_Object = MibScalar
drsAlertMessage = _DrsAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 3),
    _DrsAlertMessage_Type()
)
drsAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertMessage.setStatus("mandatory")
_DrsAlertCurrentStatus_Type = DellStatus
_DrsAlertCurrentStatus_Object = MibScalar
drsAlertCurrentStatus = _DrsAlertCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 4),
    _DrsAlertCurrentStatus_Type()
)
drsAlertCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertCurrentStatus.setStatus("mandatory")
_DrsAlertPreviousStatus_Type = DellStatus
_DrsAlertPreviousStatus_Object = MibScalar
drsAlertPreviousStatus = _DrsAlertPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 5),
    _DrsAlertPreviousStatus_Type()
)
drsAlertPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertPreviousStatus.setStatus("mandatory")


class _DrsAlertData_Type(OctetString):
    """Custom type drsAlertData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_DrsAlertData_Type.__name__ = "OctetString"
_DrsAlertData_Object = MibScalar
drsAlertData = _DrsAlertData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 5000, 10, 6),
    _DrsAlertData_Type()
)
drsAlertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drsAlertData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alertDrscTestTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1001)
)
alertDrscTestTrapEvent.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTestTrapEvent.setStatus(
        ""
    )

alertDrscAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1002)
)
alertDrscAuthError.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscAuthError.setStatus(
        ""
    )

alertDrscLostESM = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1003)
)
alertDrscLostESM.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscLostESM.setStatus(
        ""
    )

alertDrscFoundESM = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1004)
)
alertDrscFoundESM.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscFoundESM.setStatus(
        ""
    )

alertDrscPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1005)
)
alertDrscPowerOff.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscPowerOff.setStatus(
        ""
    )

alertDrscPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1006)
)
alertDrscPowerOn.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscPowerOn.setStatus(
        ""
    )

alertDrscWatchdogExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1007)
)
alertDrscWatchdogExpired.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscWatchdogExpired.setStatus(
        ""
    )

alertDrscBattLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1008)
)
alertDrscBattLow.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscBattLow.setStatus(
        ""
    )

alertDrscTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1009)
)
alertDrscTempNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempNormal.setStatus(
        ""
    )

alertDrscTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1010)
)
alertDrscTempWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempWarning.setStatus(
        ""
    )

alertDrscTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1011)
)
alertDrscTempCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscTempCritical.setStatus(
        ""
    )

alertDrscVoltNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1012)
)
alertDrscVoltNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltNormal.setStatus(
        ""
    )

alertDrscVoltWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1013)
)
alertDrscVoltWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltWarning.setStatus(
        ""
    )

alertDrscVoltCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1014)
)
alertDrscVoltCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscVoltCritical.setStatus(
        ""
    )

alertDrscSELWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1015)
)
alertDrscSELWarning.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELWarning.setStatus(
        ""
    )

alertDrscSELCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1016)
)
alertDrscSELCritical.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELCritical.setStatus(
        ""
    )

alertDrscSEL80percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1017)
)
alertDrscSEL80percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL80percentFull.setStatus(
        ""
    )

alertDrscSEL90percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1018)
)
alertDrscSEL90percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL90percentFull.setStatus(
        ""
    )

alertDrscSEL100percentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1019)
)
alertDrscSEL100percentFull.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSEL100percentFull.setStatus(
        ""
    )

alertDrscSELNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 1020)
)
alertDrscSELNormal.setObjects(
      *(("DELL-RAC-MIB", "drsAlertSystem"),
        ("DELL-RAC-MIB", "drsAlertTableIndexOID"),
        ("DELL-RAC-MIB", "drsAlertMessage"),
        ("DELL-RAC-MIB", "drsAlertCurrentStatus"),
        ("DELL-RAC-MIB", "drsAlertPreviousStatus"),
        ("DELL-RAC-MIB", "drsAlertData"))
)
if mibBuilder.loadTexts:
    alertDrscSELNormal.setStatus(
        ""
    )

alertCMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2000)
)
if mibBuilder.loadTexts:
    alertCMCTestTrap.setStatus(
        ""
    )

alertCMCNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2002)
)
alertCMCNormalTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCNormalTrap.setStatus(
        ""
    )

alertCMCWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2003)
)
alertCMCWarningTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCWarningTrap.setStatus(
        ""
    )

alertCMCCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2004)
)
alertCMCCriticalTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCCriticalTrap.setStatus(
        ""
    )

alertCMCNonRecoverableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 0, 2005)
)
alertCMCNonRecoverableTrap.setObjects(
      *(("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"),
        ("DELL-RAC-MIB", "drsCASubSystem"),
        ("DELL-RAC-MIB", "drsCASSCurrStatus"),
        ("DELL-RAC-MIB", "drsCASSPrevStatus"),
        ("DELL-RAC-MIB", "drsCASSChangeTime"),
        ("DELL-RAC-MIB", "drsCAMessage"))
)
if mibBuilder.loadTexts:
    alertCMCNonRecoverableTrap.setStatus(
        ""
    )

alert2FanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2153)
)
alert2FanFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanFailure.setStatus(
        ""
    )

alert2FanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2154)
)
alert2FanWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanWarning.setStatus(
        ""
    )

alert2FanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2155)
)
alert2FanInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2FanInformation.setStatus(
        ""
    )

alert2TemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2161)
)
alert2TemperatureProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeFailure.setStatus(
        ""
    )

alert2TemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2162)
)
alert2TemperatureProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeWarning.setStatus(
        ""
    )

alert2TemperatureProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2163)
)
alert2TemperatureProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2TemperatureProbeNormal.setStatus(
        ""
    )

alert2VoltageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2169)
)
alert2VoltageProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeFailure.setStatus(
        ""
    )

alert2VoltageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2170)
)
alert2VoltageProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeWarning.setStatus(
        ""
    )

alert2VoltageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2171)
)
alert2VoltageProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2VoltageProbeNormal.setStatus(
        ""
    )

alert2AmperageProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2177)
)
alert2AmperageProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeFailure.setStatus(
        ""
    )

alert2AmperageProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2178)
)
alert2AmperageProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeWarning.setStatus(
        ""
    )

alert2AmperageProbeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2179)
)
alert2AmperageProbeNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2AmperageProbeNormal.setStatus(
        ""
    )

alert2PowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2185)
)
alert2PowerSupplyFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyFailure.setStatus(
        ""
    )

alert2PowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2186)
)
alert2PowerSupplyWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyWarning.setStatus(
        ""
    )

alert2PowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2187)
)
alert2PowerSupplyNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyNormal.setStatus(
        ""
    )

alert2BatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2225)
)
alert2BatteryFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryFailure.setStatus(
        ""
    )

alert2BatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2226)
)
alert2BatteryWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryWarning.setStatus(
        ""
    )

alert2BatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2227)
)
alert2BatteryNormal.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2BatteryNormal.setStatus(
        ""
    )

alert2LinkStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2249)
)
alert2LinkStatusFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusFailure.setStatus(
        ""
    )

alert2LinkStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2250)
)
alert2LinkStatusWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusWarning.setStatus(
        ""
    )

alert2LinkStatusInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2251)
)
alert2LinkStatusInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LinkStatusInformation.setStatus(
        ""
    )

alert2PowerUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2274)
)
alert2PowerUsageWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageWarning.setStatus(
        ""
    )

alert2PowerUsageInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2275)
)
alert2PowerUsageInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageInformation.setStatus(
        ""
    )

alert2HardwareConfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2329)
)
alert2HardwareConfigurationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationFailure.setStatus(
        ""
    )

alert2HardwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2330)
)
alert2HardwareConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationWarning.setStatus(
        ""
    )

alert2HardwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2331)
)
alert2HardwareConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2HardwareConfigurationInformation.setStatus(
        ""
    )

alert2SoftwareConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2338)
)
alert2SoftwareConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationWarning.setStatus(
        ""
    )

alert2SoftwareConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2339)
)
alert2SoftwareConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareConfigurationInformation.setStatus(
        ""
    )

alert2SystemEventLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2377)
)
alert2SystemEventLogFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogFailure.setStatus(
        ""
    )

alert2SystemEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2378)
)
alert2SystemEventLogWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogWarning.setStatus(
        ""
    )

alert2SystemEventLogInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2379)
)
alert2SystemEventLogInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SystemEventLogInformation.setStatus(
        ""
    )

alert2SecurityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2385)
)
alert2SecurityFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityFailure.setStatus(
        ""
    )

alert2SecurityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2386)
)
alert2SecurityWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityWarning.setStatus(
        ""
    )

alert2SecurityInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2387)
)
alert2SecurityInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SecurityInformation.setStatus(
        ""
    )

alert2CableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2393)
)
alert2CableFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CableFailure.setStatus(
        ""
    )

alert2PCIDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2417)
)
alert2PCIDeviceFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceFailure.setStatus(
        ""
    )

alert2PCIDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2418)
)
alert2PCIDeviceWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceWarning.setStatus(
        ""
    )

alert2PCIDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2419)
)
alert2PCIDeviceInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceInformation.setStatus(
        ""
    )

alert2PowerSupplyAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2465)
)
alert2PowerSupplyAbsent.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAbsent.setStatus(
        ""
    )

alert2RedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2473)
)
alert2RedundancyLost.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyLost.setStatus(
        ""
    )

alert2RedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2474)
)
alert2RedundancyDegraded.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyDegraded.setStatus(
        ""
    )

alert2RedundancyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2475)
)
alert2RedundancyInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2RedundancyInformation.setStatus(
        ""
    )

alert2CMCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2545)
)
alert2CMCFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCFailure.setStatus(
        ""
    )

alert2CMCWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2546)
)
alert2CMCWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCWarning.setStatus(
        ""
    )

alert2IOVirtualizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2553)
)
alert2IOVirtualizationFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationFailure.setStatus(
        ""
    )

alert2IOVirtualizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2554)
)
alert2IOVirtualizationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationWarning.setStatus(
        ""
    )

alert2IOVirtualizationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 2555)
)
alert2IOVirtualizationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationInformation.setStatus(
        ""
    )

alert2StorageManagementFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4177)
)
alert2StorageManagementFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementFailure.setStatus(
        ""
    )

alert2StorageManagementWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4178)
)
alert2StorageManagementWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementWarning.setStatus(
        ""
    )

alert2StorageManagementInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4179)
)
alert2StorageManagementInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageManagementInformation.setStatus(
        ""
    )

alert2StorageFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4201)
)
alert2StorageFanFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanFailure.setStatus(
        ""
    )

alert2StorageFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4202)
)
alert2StorageFanWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanWarning.setStatus(
        ""
    )

alert2StorageFanInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4203)
)
alert2StorageFanInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageFanInformation.setStatus(
        ""
    )

alert2StorageTemperatureProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4209)
)
alert2StorageTemperatureProbeFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeFailure.setStatus(
        ""
    )

alert2StorageTemperatureProbeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4210)
)
alert2StorageTemperatureProbeWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeWarning.setStatus(
        ""
    )

alert2StorageTemperatureProbeInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4211)
)
alert2StorageTemperatureProbeInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageTemperatureProbeInformation.setStatus(
        ""
    )

alert2StoragePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4233)
)
alert2StoragePowerSupplyFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyFailure.setStatus(
        ""
    )

alert2StoragePowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4234)
)
alert2StoragePowerSupplyWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyWarning.setStatus(
        ""
    )

alert2StoragePowerSupplyInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4235)
)
alert2StoragePowerSupplyInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePowerSupplyInformation.setStatus(
        ""
    )

alert2StorageBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4273)
)
alert2StorageBatteryFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryFailure.setStatus(
        ""
    )

alert2StorageBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4274)
)
alert2StorageBatteryWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryWarning.setStatus(
        ""
    )

alert2StorageBatteryInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4275)
)
alert2StorageBatteryInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageBatteryInformation.setStatus(
        ""
    )

alert2StorageControllerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4329)
)
alert2StorageControllerFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerFailure.setStatus(
        ""
    )

alert2StorageControllerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4330)
)
alert2StorageControllerWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerWarning.setStatus(
        ""
    )

alert2StorageControllerInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4331)
)
alert2StorageControllerInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageControllerInformation.setStatus(
        ""
    )

alert2StorageEnclosureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4337)
)
alert2StorageEnclosureFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureFailure.setStatus(
        ""
    )

alert2StorageEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4338)
)
alert2StorageEnclosureWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureWarning.setStatus(
        ""
    )

alert2StorageEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4339)
)
alert2StorageEnclosureInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageEnclosureInformation.setStatus(
        ""
    )

alert2StoragePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4345)
)
alert2StoragePhysicalDiskFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskFailure.setStatus(
        ""
    )

alert2StoragePhysicalDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4346)
)
alert2StoragePhysicalDiskWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskWarning.setStatus(
        ""
    )

alert2StoragePhysicalDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4347)
)
alert2StoragePhysicalDiskInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StoragePhysicalDiskInformation.setStatus(
        ""
    )

alert2StorageVirtualDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4353)
)
alert2StorageVirtualDiskFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskFailure.setStatus(
        ""
    )

alert2StorageVirtualDiskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4354)
)
alert2StorageVirtualDiskWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskWarning.setStatus(
        ""
    )

alert2StorageVirtualDiskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 4355)
)
alert2StorageVirtualDiskInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2StorageVirtualDiskInformation.setStatus(
        ""
    )

alert2PowerSupplyAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8329)
)
alert2PowerSupplyAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditFailure.setStatus(
        ""
    )

alert2PowerSupplyAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8330)
)
alert2PowerSupplyAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerSupplyAuditWarning.setStatus(
        ""
    )

alert2SoftwareChangeAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8361)
)
alert2SoftwareChangeAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2SoftwareChangeAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8417)
)
alert2PowerUsageAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditFailure.setStatus(
        ""
    )

alert2PowerUsageAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8418)
)
alert2PowerUsageAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PowerUsageAuditWarning.setStatus(
        ""
    )

alert2LicenseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8513)
)
alert2LicenseFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseFailure.setStatus(
        ""
    )

alert2LicenseWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8514)
)
alert2LicenseWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseWarning.setStatus(
        ""
    )

alert2LicenseInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8515)
)
alert2LicenseInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2LicenseInformation.setStatus(
        ""
    )

alert2PCIDeviceAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8562)
)
alert2PCIDeviceAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceAuditWarning.setStatus(
        ""
    )

alert2CMCAuditFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8689)
)
alert2CMCAuditFailure.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditFailure.setStatus(
        ""
    )

alert2CMCAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8690)
)
alert2CMCAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditWarning.setStatus(
        ""
    )

alert2CMCAuditInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8691)
)
alert2CMCAuditInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCAuditInformation.setStatus(
        ""
    )

alert2IOVirtualizationAuditWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 8698)
)
alert2IOVirtualizationAuditWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVirtualizationAuditWarning.setStatus(
        ""
    )

alert2CMCTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10395)
)
alert2CMCTestTrap.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2CMCTestTrap.setStatus(
        ""
    )

alert2PCIDeviceConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10611)
)
alert2PCIDeviceConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2PCIDeviceConfigurationInformation.setStatus(
        ""
    )

alert2IOVConfigurationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10746)
)
alert2IOVConfigurationWarning.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationWarning.setStatus(
        ""
    )

alert2IOVConfigurationInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10892, 2, 21, 0, 10747)
)
alert2IOVConfigurationInformation.setObjects(
      *(("DELL-RAC-MIB", "drsCA2MessageID"),
        ("DELL-RAC-MIB", "drsCA2Message"),
        ("DELL-RAC-MIB", "drsCA2MessageArgs"),
        ("DELL-RAC-MIB", "drsCA2AlertStatus"),
        ("DELL-RAC-MIB", "drsCA2FQDD"),
        ("DELL-RAC-MIB", "drsProductChassisName"),
        ("DELL-RAC-MIB", "drsProductChassisLocation"),
        ("DELL-RAC-MIB", "drsChassisServiceTag"),
        ("DELL-RAC-MIB", "drsGlobalCurrStatus"))
)
if mibBuilder.loadTexts:
    alert2IOVConfigurationInformation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-RAC-MIB",
    **{"DellString": DellString,
       "DellRacType": DellRacType,
       "DellStatus": DellStatus,
       "DellPowerReading": DellPowerReading,
       "DellCMCPowerIndexRange": DellCMCPowerIndexRange,
       "DellCMCPSUIndexRange": DellCMCPSUIndexRange,
       "DellCMCPSUCapable": DellCMCPSUCapable,
       "DellTemperatureReading": DellTemperatureReading,
       "DellTimestamp": DellTimestamp,
       "DellCMCServerIndexRange": DellCMCServerIndexRange,
       "DellCMCServerCapable": DellCMCServerCapable,
       "dell": dell,
       "server3": server3,
       "drsOutofBandGroup": drsOutofBandGroup,
       "alertDrscTestTrapEvent": alertDrscTestTrapEvent,
       "alertDrscAuthError": alertDrscAuthError,
       "alertDrscLostESM": alertDrscLostESM,
       "alertDrscFoundESM": alertDrscFoundESM,
       "alertDrscPowerOff": alertDrscPowerOff,
       "alertDrscPowerOn": alertDrscPowerOn,
       "alertDrscWatchdogExpired": alertDrscWatchdogExpired,
       "alertDrscBattLow": alertDrscBattLow,
       "alertDrscTempNormal": alertDrscTempNormal,
       "alertDrscTempWarning": alertDrscTempWarning,
       "alertDrscTempCritical": alertDrscTempCritical,
       "alertDrscVoltNormal": alertDrscVoltNormal,
       "alertDrscVoltWarning": alertDrscVoltWarning,
       "alertDrscVoltCritical": alertDrscVoltCritical,
       "alertDrscSELWarning": alertDrscSELWarning,
       "alertDrscSELCritical": alertDrscSELCritical,
       "alertDrscSEL80percentFull": alertDrscSEL80percentFull,
       "alertDrscSEL90percentFull": alertDrscSEL90percentFull,
       "alertDrscSEL100percentFull": alertDrscSEL100percentFull,
       "alertDrscSELNormal": alertDrscSELNormal,
       "alertCMCTestTrap": alertCMCTestTrap,
       "alertCMCNormalTrap": alertCMCNormalTrap,
       "alertCMCWarningTrap": alertCMCWarningTrap,
       "alertCMCCriticalTrap": alertCMCCriticalTrap,
       "alertCMCNonRecoverableTrap": alertCMCNonRecoverableTrap,
       "drsInformationGroup": drsInformationGroup,
       "drsProductInfoGroup": drsProductInfoGroup,
       "drsProductName": drsProductName,
       "drsProductShortName": drsProductShortName,
       "drsProductDescription": drsProductDescription,
       "drsProductManufacturer": drsProductManufacturer,
       "drsProductVersion": drsProductVersion,
       "drsChassisServiceTag": drsChassisServiceTag,
       "drsProductURL": drsProductURL,
       "drsProductChassisAssetTag": drsProductChassisAssetTag,
       "drsProductChassisLocation": drsProductChassisLocation,
       "drsProductChassisName": drsProductChassisName,
       "drsSystemServiceTag": drsSystemServiceTag,
       "drsProductSystemAssetTag": drsProductSystemAssetTag,
       "drsProductSystemSlot": drsProductSystemSlot,
       "drsProductType": drsProductType,
       "drsProductChassisDataCenter": drsProductChassisDataCenter,
       "drsProductChassisAisle": drsProductChassisAisle,
       "drsProductChassisRack": drsProductChassisRack,
       "drsProductChassisRackSlot": drsProductChassisRackSlot,
       "drsProductChassisModel": drsProductChassisModel,
       "drsProductChassisExpressServiceCode": drsProductChassisExpressServiceCode,
       "drsProductChassisSystemID": drsProductChassisSystemID,
       "drsProductChassisSize": drsProductChassisSize,
       "drsFirmwareGroup": drsFirmwareGroup,
       "drsFirmwareVersion": drsFirmwareVersion,
       "drsiKVMFirmwareVersion": drsiKVMFirmwareVersion,
       "drsFirmwareVersion2": drsFirmwareVersion2,
       "drsStatusGroup": drsStatusGroup,
       "drsGlobalSystemStatus": drsGlobalSystemStatus,
       "drsChassisStatusGroup": drsChassisStatusGroup,
       "drsStatusNowGroup": drsStatusNowGroup,
       "drsGlobalCurrStatus": drsGlobalCurrStatus,
       "drsIOMCurrStatus": drsIOMCurrStatus,
       "drsKVMCurrStatus": drsKVMCurrStatus,
       "drsRedCurrStatus": drsRedCurrStatus,
       "drsPowerCurrStatus": drsPowerCurrStatus,
       "drsFanCurrStatus": drsFanCurrStatus,
       "drsBladeCurrStatus": drsBladeCurrStatus,
       "drsTempCurrStatus": drsTempCurrStatus,
       "drsCMCCurrStatus": drsCMCCurrStatus,
       "drsChassisFrontPanelAmbientTemperature": drsChassisFrontPanelAmbientTemperature,
       "drsCMCAmbientTemperature": drsCMCAmbientTemperature,
       "drsCMCProcessorTemperature": drsCMCProcessorTemperature,
       "drsStatusPrevGroup": drsStatusPrevGroup,
       "drsGlobalPrevStatus": drsGlobalPrevStatus,
       "drsIOMPrevStatus": drsIOMPrevStatus,
       "drsKVMPrevStatus": drsKVMPrevStatus,
       "drsRedPrevStatus": drsRedPrevStatus,
       "drsPowerPrevStatus": drsPowerPrevStatus,
       "drsFanPrevStatus": drsFanPrevStatus,
       "drsBladePrevStatus": drsBladePrevStatus,
       "drsTempPrevStatus": drsTempPrevStatus,
       "drsCMCPrevStatus": drsCMCPrevStatus,
       "drsStatusChangeGroup": drsStatusChangeGroup,
       "drsGlobalChangeTime": drsGlobalChangeTime,
       "drsIOMChangeTime": drsIOMChangeTime,
       "drsKVMChangeTime": drsKVMChangeTime,
       "drsRedChangeTime": drsRedChangeTime,
       "drsPowerChangeTime": drsPowerChangeTime,
       "drsFanChangeTime": drsFanChangeTime,
       "drsBladeChangeTime": drsBladeChangeTime,
       "drsTempChangeTime": drsTempChangeTime,
       "drsCMCChangeTime": drsCMCChangeTime,
       "drsChassisPowerGroup": drsChassisPowerGroup,
       "drsCMCPowerTable": drsCMCPowerTable,
       "drsCMCPowerTableEntry": drsCMCPowerTableEntry,
       "drsChassisIndex": drsChassisIndex,
       "drsPotentialPower": drsPotentialPower,
       "drsIdlePower": drsIdlePower,
       "drsMaxPowerSpecification": drsMaxPowerSpecification,
       "drsPowerSurplus": drsPowerSurplus,
       "drsKWhCumulative": drsKWhCumulative,
       "drsKWhCumulativeTime": drsKWhCumulativeTime,
       "drsWattsPeakUsage": drsWattsPeakUsage,
       "drsWattsPeakTime": drsWattsPeakTime,
       "drsWattsMinUsage": drsWattsMinUsage,
       "drsWattsMinTime": drsWattsMinTime,
       "drsWattsResetTime": drsWattsResetTime,
       "drsWattsReading": drsWattsReading,
       "drsAmpsReading": drsAmpsReading,
       "drsCMCPSUTable": drsCMCPSUTable,
       "drsCMCPSUTableEntry": drsCMCPSUTableEntry,
       "drsPSUChassisIndex": drsPSUChassisIndex,
       "drsPSUIndex": drsPSUIndex,
       "drsPSULocation": drsPSULocation,
       "drsPSUMonitoringCapable": drsPSUMonitoringCapable,
       "drsPSUVoltsReading": drsPSUVoltsReading,
       "drsPSUAmpsReading": drsPSUAmpsReading,
       "drsPSUWattsReading": drsPSUWattsReading,
       "drsChassisServerGroup": drsChassisServerGroup,
       "drsCMCServerTable": drsCMCServerTable,
       "drsCMCServerTableEntry": drsCMCServerTableEntry,
       "drsServerIndex": drsServerIndex,
       "drsServerMonitoringCapable": drsServerMonitoringCapable,
       "drsServerServiceTag": drsServerServiceTag,
       "drsServerSlotName": drsServerSlotName,
       "drsServerSlotNumber": drsServerSlotNumber,
       "drsServerNodeID": drsServerNodeID,
       "drsCMCAlertGroup": drsCMCAlertGroup,
       "drsChassisAlertVariables": drsChassisAlertVariables,
       "drsCASubSystem": drsCASubSystem,
       "drsCASSCurrStatus": drsCASSCurrStatus,
       "drsCASSPrevStatus": drsCASSPrevStatus,
       "drsCASSChangeTime": drsCASSChangeTime,
       "drsCAMessage": drsCAMessage,
       "drsCMCAlert2Group": drsCMCAlert2Group,
       "alert2FanFailure": alert2FanFailure,
       "alert2FanWarning": alert2FanWarning,
       "alert2FanInformation": alert2FanInformation,
       "alert2TemperatureProbeFailure": alert2TemperatureProbeFailure,
       "alert2TemperatureProbeWarning": alert2TemperatureProbeWarning,
       "alert2TemperatureProbeNormal": alert2TemperatureProbeNormal,
       "alert2VoltageProbeFailure": alert2VoltageProbeFailure,
       "alert2VoltageProbeWarning": alert2VoltageProbeWarning,
       "alert2VoltageProbeNormal": alert2VoltageProbeNormal,
       "alert2AmperageProbeFailure": alert2AmperageProbeFailure,
       "alert2AmperageProbeWarning": alert2AmperageProbeWarning,
       "alert2AmperageProbeNormal": alert2AmperageProbeNormal,
       "alert2PowerSupplyFailure": alert2PowerSupplyFailure,
       "alert2PowerSupplyWarning": alert2PowerSupplyWarning,
       "alert2PowerSupplyNormal": alert2PowerSupplyNormal,
       "alert2BatteryFailure": alert2BatteryFailure,
       "alert2BatteryWarning": alert2BatteryWarning,
       "alert2BatteryNormal": alert2BatteryNormal,
       "alert2LinkStatusFailure": alert2LinkStatusFailure,
       "alert2LinkStatusWarning": alert2LinkStatusWarning,
       "alert2LinkStatusInformation": alert2LinkStatusInformation,
       "alert2PowerUsageWarning": alert2PowerUsageWarning,
       "alert2PowerUsageInformation": alert2PowerUsageInformation,
       "alert2HardwareConfigurationFailure": alert2HardwareConfigurationFailure,
       "alert2HardwareConfigurationWarning": alert2HardwareConfigurationWarning,
       "alert2HardwareConfigurationInformation": alert2HardwareConfigurationInformation,
       "alert2SoftwareConfigurationWarning": alert2SoftwareConfigurationWarning,
       "alert2SoftwareConfigurationInformation": alert2SoftwareConfigurationInformation,
       "alert2SystemEventLogFailure": alert2SystemEventLogFailure,
       "alert2SystemEventLogWarning": alert2SystemEventLogWarning,
       "alert2SystemEventLogInformation": alert2SystemEventLogInformation,
       "alert2SecurityFailure": alert2SecurityFailure,
       "alert2SecurityWarning": alert2SecurityWarning,
       "alert2SecurityInformation": alert2SecurityInformation,
       "alert2CableFailure": alert2CableFailure,
       "alert2PCIDeviceFailure": alert2PCIDeviceFailure,
       "alert2PCIDeviceWarning": alert2PCIDeviceWarning,
       "alert2PCIDeviceInformation": alert2PCIDeviceInformation,
       "alert2PowerSupplyAbsent": alert2PowerSupplyAbsent,
       "alert2RedundancyLost": alert2RedundancyLost,
       "alert2RedundancyDegraded": alert2RedundancyDegraded,
       "alert2RedundancyInformation": alert2RedundancyInformation,
       "alert2CMCFailure": alert2CMCFailure,
       "alert2CMCWarning": alert2CMCWarning,
       "alert2IOVirtualizationFailure": alert2IOVirtualizationFailure,
       "alert2IOVirtualizationWarning": alert2IOVirtualizationWarning,
       "alert2IOVirtualizationInformation": alert2IOVirtualizationInformation,
       "alert2StorageManagementFailure": alert2StorageManagementFailure,
       "alert2StorageManagementWarning": alert2StorageManagementWarning,
       "alert2StorageManagementInformation": alert2StorageManagementInformation,
       "alert2StorageFanFailure": alert2StorageFanFailure,
       "alert2StorageFanWarning": alert2StorageFanWarning,
       "alert2StorageFanInformation": alert2StorageFanInformation,
       "alert2StorageTemperatureProbeFailure": alert2StorageTemperatureProbeFailure,
       "alert2StorageTemperatureProbeWarning": alert2StorageTemperatureProbeWarning,
       "alert2StorageTemperatureProbeInformation": alert2StorageTemperatureProbeInformation,
       "alert2StoragePowerSupplyFailure": alert2StoragePowerSupplyFailure,
       "alert2StoragePowerSupplyWarning": alert2StoragePowerSupplyWarning,
       "alert2StoragePowerSupplyInformation": alert2StoragePowerSupplyInformation,
       "alert2StorageBatteryFailure": alert2StorageBatteryFailure,
       "alert2StorageBatteryWarning": alert2StorageBatteryWarning,
       "alert2StorageBatteryInformation": alert2StorageBatteryInformation,
       "alert2StorageControllerFailure": alert2StorageControllerFailure,
       "alert2StorageControllerWarning": alert2StorageControllerWarning,
       "alert2StorageControllerInformation": alert2StorageControllerInformation,
       "alert2StorageEnclosureFailure": alert2StorageEnclosureFailure,
       "alert2StorageEnclosureWarning": alert2StorageEnclosureWarning,
       "alert2StorageEnclosureInformation": alert2StorageEnclosureInformation,
       "alert2StoragePhysicalDiskFailure": alert2StoragePhysicalDiskFailure,
       "alert2StoragePhysicalDiskWarning": alert2StoragePhysicalDiskWarning,
       "alert2StoragePhysicalDiskInformation": alert2StoragePhysicalDiskInformation,
       "alert2StorageVirtualDiskFailure": alert2StorageVirtualDiskFailure,
       "alert2StorageVirtualDiskWarning": alert2StorageVirtualDiskWarning,
       "alert2StorageVirtualDiskInformation": alert2StorageVirtualDiskInformation,
       "alert2PowerSupplyAuditFailure": alert2PowerSupplyAuditFailure,
       "alert2PowerSupplyAuditWarning": alert2PowerSupplyAuditWarning,
       "alert2SoftwareChangeAuditFailure": alert2SoftwareChangeAuditFailure,
       "alert2PowerUsageAuditFailure": alert2PowerUsageAuditFailure,
       "alert2PowerUsageAuditWarning": alert2PowerUsageAuditWarning,
       "alert2LicenseFailure": alert2LicenseFailure,
       "alert2LicenseWarning": alert2LicenseWarning,
       "alert2LicenseInformation": alert2LicenseInformation,
       "alert2PCIDeviceAuditWarning": alert2PCIDeviceAuditWarning,
       "alert2CMCAuditFailure": alert2CMCAuditFailure,
       "alert2CMCAuditWarning": alert2CMCAuditWarning,
       "alert2CMCAuditInformation": alert2CMCAuditInformation,
       "alert2IOVirtualizationAuditWarning": alert2IOVirtualizationAuditWarning,
       "alert2CMCTestTrap": alert2CMCTestTrap,
       "alert2PCIDeviceConfigurationInformation": alert2PCIDeviceConfigurationInformation,
       "alert2IOVConfigurationWarning": alert2IOVConfigurationWarning,
       "alert2IOVConfigurationInformation": alert2IOVConfigurationInformation,
       "drsChassisAlert2Variables": drsChassisAlert2Variables,
       "drsCA2MessageID": drsCA2MessageID,
       "drsCA2Message": drsCA2Message,
       "drsCA2MessageArgs": drsCA2MessageArgs,
       "drsCA2AlertStatus": drsCA2AlertStatus,
       "drsCA2FQDD": drsCA2FQDD,
       "drsAlertGroup": drsAlertGroup,
       "drsAlertVariables": drsAlertVariables,
       "drsAlertSystem": drsAlertSystem,
       "drsAlertTableIndexOID": drsAlertTableIndexOID,
       "drsAlertMessage": drsAlertMessage,
       "drsAlertCurrentStatus": drsAlertCurrentStatus,
       "drsAlertPreviousStatus": drsAlertPreviousStatus,
       "drsAlertData": drsAlertData}
)
