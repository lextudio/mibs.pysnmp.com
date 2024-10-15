# SNMP MIB module (CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:26 2024
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

(CiscoLwappDot11ClientAuthMethod,
 CiscoLwappDot11ClientCredentialType,
 CiscoLwappDot11ClientEAPMethod,
 CiscoLwappDot11ClientEncryptionMethod,
 CiscoLwappDot11ClientKeyMgmtMethod,
 CiscoLwappDot11ClientPowerSaveMode,
 CiscoLwappDot11ClientRadioType,
 CiscoLwappDot11ClientReqStatus,
 CiscoLwappDot11ClientSSId,
 CiscoLwappDot11ClientTxPowerMode) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB",
    "CiscoLwappDot11ClientAuthMethod",
    "CiscoLwappDot11ClientCredentialType",
    "CiscoLwappDot11ClientEAPMethod",
    "CiscoLwappDot11ClientEncryptionMethod",
    "CiscoLwappDot11ClientKeyMgmtMethod",
    "CiscoLwappDot11ClientPowerSaveMode",
    "CiscoLwappDot11ClientRadioType",
    "CiscoLwappDot11ClientReqStatus",
    "CiscoLwappDot11ClientSSId",
    "CiscoLwappDot11ClientTxPowerMode")

(ciscoLwappDot11ClientCcxMIBObjects,
 cldcClientMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "ciscoLwappDot11ClientCcxMIBObjects",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvE164Address,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CvE164Address")

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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLwappDot11ClientCCXv5ReportingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4)
)
ciscoLwappDot11ClientCCXv5ReportingMIB.setRevisions(
        ("2006-12-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11ClientCCXv5ReportingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCCXv5ReportingMIBObjects = _CiscoLwappDot11ClientCCXv5ReportingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1)
)
_CiscoClientCcxManuReporting_ObjectIdentity = ObjectIdentity
ciscoClientCcxManuReporting = _CiscoClientCcxManuReporting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1)
)
_CldccManufacturerInfoTable_Object = MibTable
cldccManufacturerInfoTable = _CldccManufacturerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldccManufacturerInfoTable.setStatus("current")
_CldccManufacturerInfoEntry_Object = MibTableRow
cldccManufacturerInfoEntry = _CldccManufacturerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1)
)
cldccManufacturerInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccManufacturerInfoEntry.setStatus("current")
_CldccManufacturerInfoStatus_Type = CiscoLwappDot11ClientReqStatus
_CldccManufacturerInfoStatus_Object = MibTableColumn
cldccManufacturerInfoStatus = _CldccManufacturerInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 1),
    _CldccManufacturerInfoStatus_Type()
)
cldccManufacturerInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccManufacturerInfoStatus.setStatus("current")


class _CldccManufacturerInfoOUI_Type(OctetString):
    """Custom type cldccManufacturerInfoOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CldccManufacturerInfoOUI_Type.__name__ = "OctetString"
_CldccManufacturerInfoOUI_Object = MibTableColumn
cldccManufacturerInfoOUI = _CldccManufacturerInfoOUI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 2),
    _CldccManufacturerInfoOUI_Type()
)
cldccManufacturerInfoOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoOUI.setStatus("current")


class _CldccManufacturerInfoID_Type(DisplayString):
    """Custom type cldccManufacturerInfoID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccManufacturerInfoID_Type.__name__ = "DisplayString"
_CldccManufacturerInfoID_Object = MibTableColumn
cldccManufacturerInfoID = _CldccManufacturerInfoID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 3),
    _CldccManufacturerInfoID_Type()
)
cldccManufacturerInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoID.setStatus("current")


class _CldccManufacturerInfoModel_Type(DisplayString):
    """Custom type cldccManufacturerInfoModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccManufacturerInfoModel_Type.__name__ = "DisplayString"
_CldccManufacturerInfoModel_Object = MibTableColumn
cldccManufacturerInfoModel = _CldccManufacturerInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 4),
    _CldccManufacturerInfoModel_Type()
)
cldccManufacturerInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoModel.setStatus("current")


class _CldccManufacturerInfoSerialNum_Type(DisplayString):
    """Custom type cldccManufacturerInfoSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccManufacturerInfoSerialNum_Type.__name__ = "DisplayString"
_CldccManufacturerInfoSerialNum_Object = MibTableColumn
cldccManufacturerInfoSerialNum = _CldccManufacturerInfoSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 5),
    _CldccManufacturerInfoSerialNum_Type()
)
cldccManufacturerInfoSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoSerialNum.setStatus("current")


class _CldccManufacturerInfoRadioType_Type(DisplayString):
    """Custom type cldccManufacturerInfoRadioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccManufacturerInfoRadioType_Type.__name__ = "DisplayString"
_CldccManufacturerInfoRadioType_Object = MibTableColumn
cldccManufacturerInfoRadioType = _CldccManufacturerInfoRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 6),
    _CldccManufacturerInfoRadioType_Type()
)
cldccManufacturerInfoRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoRadioType.setStatus("current")
_CldccManufacturerInfoMacAddress_Type = MacAddress
_CldccManufacturerInfoMacAddress_Object = MibTableColumn
cldccManufacturerInfoMacAddress = _CldccManufacturerInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 7),
    _CldccManufacturerInfoMacAddress_Type()
)
cldccManufacturerInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoMacAddress.setStatus("current")


class _CldccManufacturerInfoAntennaType_Type(Integer32):
    """Custom type cldccManufacturerInfoAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("directionalOther", 6),
          ("directionalPanel", 4),
          ("directionalSector", 5),
          ("directionalYagi", 3),
          ("omniDirectionalCollinear", 0),
          ("omniDirectionalDiversity", 1),
          ("omniDirectionalOther", 2),
          ("unknown", 7))
    )


_CldccManufacturerInfoAntennaType_Type.__name__ = "Integer32"
_CldccManufacturerInfoAntennaType_Object = MibTableColumn
cldccManufacturerInfoAntennaType = _CldccManufacturerInfoAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 8),
    _CldccManufacturerInfoAntennaType_Type()
)
cldccManufacturerInfoAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoAntennaType.setStatus("current")


class _CldccManufacturerInfoAntennaGain_Type(Unsigned32):
    """Custom type cldccManufacturerInfoAntennaGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_CldccManufacturerInfoAntennaGain_Type.__name__ = "Unsigned32"
_CldccManufacturerInfoAntennaGain_Object = MibTableColumn
cldccManufacturerInfoAntennaGain = _CldccManufacturerInfoAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 1, 1, 9),
    _CldccManufacturerInfoAntennaGain_Type()
)
cldccManufacturerInfoAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManufacturerInfoAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    cldccManufacturerInfoAntennaGain.setUnits("dBm")
_CldccManuRxSensTable_Object = MibTable
cldccManuRxSensTable = _CldccManuRxSensTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cldccManuRxSensTable.setStatus("current")
_CldccManuRxSensEntry_Object = MibTableRow
cldccManuRxSensEntry = _CldccManuRxSensEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1)
)
cldccManuRxSensEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccManuRxSensRadioIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccManuRxSensRadioDataRateIndex"),
)
if mibBuilder.loadTexts:
    cldccManuRxSensEntry.setStatus("current")
_CldccManuRxSensRadioIndex_Type = Unsigned32
_CldccManuRxSensRadioIndex_Object = MibTableColumn
cldccManuRxSensRadioIndex = _CldccManuRxSensRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 1),
    _CldccManuRxSensRadioIndex_Type()
)
cldccManuRxSensRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccManuRxSensRadioIndex.setStatus("current")
_CldccManuRxSensRadioDataRateIndex_Type = Unsigned32
_CldccManuRxSensRadioDataRateIndex_Object = MibTableColumn
cldccManuRxSensRadioDataRateIndex = _CldccManuRxSensRadioDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 2),
    _CldccManuRxSensRadioDataRateIndex_Type()
)
cldccManuRxSensRadioDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccManuRxSensRadioDataRateIndex.setStatus("current")
_CldccManuRxSensRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccManuRxSensRadioType_Object = MibTableColumn
cldccManuRxSensRadioType = _CldccManuRxSensRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 3),
    _CldccManuRxSensRadioType_Type()
)
cldccManuRxSensRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManuRxSensRadioType.setStatus("current")
_CldccManuRxSensRadioDataRate_Type = Unsigned32
_CldccManuRxSensRadioDataRate_Object = MibTableColumn
cldccManuRxSensRadioDataRate = _CldccManuRxSensRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 4),
    _CldccManuRxSensRadioDataRate_Type()
)
cldccManuRxSensRadioDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManuRxSensRadioDataRate.setStatus("current")
_CldccManuRxSensMinRssi_Type = Integer32
_CldccManuRxSensMinRssi_Object = MibTableColumn
cldccManuRxSensMinRssi = _CldccManuRxSensMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 5),
    _CldccManuRxSensMinRssi_Type()
)
cldccManuRxSensMinRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManuRxSensMinRssi.setStatus("current")
_CldccManuRxSensMaxRssi_Type = Integer32
_CldccManuRxSensMaxRssi_Object = MibTableColumn
cldccManuRxSensMaxRssi = _CldccManuRxSensMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 1, 2, 1, 6),
    _CldccManuRxSensMaxRssi_Type()
)
cldccManuRxSensMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccManuRxSensMaxRssi.setStatus("current")
_CiscoClientCcxOperReporting_ObjectIdentity = ObjectIdentity
ciscoClientCcxOperReporting = _CiscoClientCcxOperReporting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2)
)
_CldccOperParamsTable_Object = MibTable
cldccOperParamsTable = _CldccOperParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldccOperParamsTable.setStatus("current")
_CldccOperParamsEntry_Object = MibTableRow
cldccOperParamsEntry = _CldccOperParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1)
)
cldccOperParamsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccOperParamsEntry.setStatus("current")
_CldccOperParamsStatus_Type = CiscoLwappDot11ClientReqStatus
_CldccOperParamsStatus_Object = MibTableColumn
cldccOperParamsStatus = _CldccOperParamsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 1),
    _CldccOperParamsStatus_Type()
)
cldccOperParamsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccOperParamsStatus.setStatus("current")


class _CldccOperParamsRadioType_Type(DisplayString):
    """Custom type cldccOperParamsRadioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsRadioType_Type.__name__ = "DisplayString"
_CldccOperParamsRadioType_Object = MibTableColumn
cldccOperParamsRadioType = _CldccOperParamsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 2),
    _CldccOperParamsRadioType_Type()
)
cldccOperParamsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsRadioType.setStatus("current")
_CldccOperParamsSSId_Type = CiscoLwappDot11ClientSSId
_CldccOperParamsSSId_Object = MibTableColumn
cldccOperParamsSSId = _CldccOperParamsSSId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 7),
    _CldccOperParamsSSId_Type()
)
cldccOperParamsSSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsSSId.setStatus("current")


class _CldccOperParamsDeviceName_Type(DisplayString):
    """Custom type cldccOperParamsDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsDeviceName_Type.__name__ = "DisplayString"
_CldccOperParamsDeviceName_Object = MibTableColumn
cldccOperParamsDeviceName = _CldccOperParamsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 8),
    _CldccOperParamsDeviceName_Type()
)
cldccOperParamsDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDeviceName.setStatus("current")


class _CldccOperParamsDeviceType_Type(Integer32):
    """Custom type cldccOperParamsDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("appSpecific", 18),
          ("camera", 11),
          ("cashRegister", 14),
          ("dot11DeskPhone", 13),
          ("dot11MobilePhone", 3),
          ("dualModePhone", 4),
          ("gamingSystem", 12),
          ("laptop", 0),
          ("pc", 1),
          ("pda", 2),
          ("printer", 8),
          ("projector", 9),
          ("radioTag", 15),
          ("rfidSensor", 16),
          ("scanner", 6),
          ("server", 17),
          ("tabletPc", 7),
          ("unknown", 255),
          ("videoConfSystem", 10),
          ("wgb", 5))
    )


_CldccOperParamsDeviceType_Type.__name__ = "Integer32"
_CldccOperParamsDeviceType_Object = MibTableColumn
cldccOperParamsDeviceType = _CldccOperParamsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 9),
    _CldccOperParamsDeviceType_Type()
)
cldccOperParamsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDeviceType.setStatus("current")


class _CldccOperParamsOSId_Type(DisplayString):
    """Custom type cldccOperParamsOSId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsOSId_Type.__name__ = "DisplayString"
_CldccOperParamsOSId_Object = MibTableColumn
cldccOperParamsOSId = _CldccOperParamsOSId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 10),
    _CldccOperParamsOSId_Type()
)
cldccOperParamsOSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsOSId.setStatus("current")


class _CldccOperParamsOSVersion_Type(DisplayString):
    """Custom type cldccOperParamsOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsOSVersion_Type.__name__ = "DisplayString"
_CldccOperParamsOSVersion_Object = MibTableColumn
cldccOperParamsOSVersion = _CldccOperParamsOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 11),
    _CldccOperParamsOSVersion_Type()
)
cldccOperParamsOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsOSVersion.setStatus("current")


class _CldccOperParamsIpAddressMode_Type(Integer32):
    """Custom type cldccOperParamsIpAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_CldccOperParamsIpAddressMode_Type.__name__ = "Integer32"
_CldccOperParamsIpAddressMode_Object = MibTableColumn
cldccOperParamsIpAddressMode = _CldccOperParamsIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 12),
    _CldccOperParamsIpAddressMode_Type()
)
cldccOperParamsIpAddressMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsIpAddressMode.setStatus("current")
_CldccOperParamsIpv4Address_Type = IpAddress
_CldccOperParamsIpv4Address_Object = MibTableColumn
cldccOperParamsIpv4Address = _CldccOperParamsIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 13),
    _CldccOperParamsIpv4Address_Type()
)
cldccOperParamsIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsIpv4Address.setStatus("current")
_CldccOperParamsIpv4SubnetMask_Type = IpAddress
_CldccOperParamsIpv4SubnetMask_Object = MibTableColumn
cldccOperParamsIpv4SubnetMask = _CldccOperParamsIpv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 14),
    _CldccOperParamsIpv4SubnetMask_Type()
)
cldccOperParamsIpv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsIpv4SubnetMask.setStatus("current")


class _CldccOperParamsIpv6Address_Type(OctetString):
    """Custom type cldccOperParamsIpv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CldccOperParamsIpv6Address_Type.__name__ = "OctetString"
_CldccOperParamsIpv6Address_Object = MibTableColumn
cldccOperParamsIpv6Address = _CldccOperParamsIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 15),
    _CldccOperParamsIpv6Address_Type()
)
cldccOperParamsIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsIpv6Address.setStatus("current")


class _CldccOperParamsIpv6SubnetMask_Type(OctetString):
    """Custom type cldccOperParamsIpv6SubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CldccOperParamsIpv6SubnetMask_Type.__name__ = "OctetString"
_CldccOperParamsIpv6SubnetMask_Object = MibTableColumn
cldccOperParamsIpv6SubnetMask = _CldccOperParamsIpv6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 16),
    _CldccOperParamsIpv6SubnetMask_Type()
)
cldccOperParamsIpv6SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsIpv6SubnetMask.setStatus("current")
_CldccOperParamsDefaultGateway_Type = IpAddress
_CldccOperParamsDefaultGateway_Object = MibTableColumn
cldccOperParamsDefaultGateway = _CldccOperParamsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 17),
    _CldccOperParamsDefaultGateway_Type()
)
cldccOperParamsDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDefaultGateway.setStatus("current")
_CldccOperParamsEntPhone_Type = CvE164Address
_CldccOperParamsEntPhone_Object = MibTableColumn
cldccOperParamsEntPhone = _CldccOperParamsEntPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 18),
    _CldccOperParamsEntPhone_Type()
)
cldccOperParamsEntPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsEntPhone.setStatus("current")
_CldccOperParamsCellPhone_Type = CvE164Address
_CldccOperParamsCellPhone_Object = MibTableColumn
cldccOperParamsCellPhone = _CldccOperParamsCellPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 19),
    _CldccOperParamsCellPhone_Type()
)
cldccOperParamsCellPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsCellPhone.setStatus("current")


class _CldccOperParamsFirmwareVersion_Type(DisplayString):
    """Custom type cldccOperParamsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsFirmwareVersion_Type.__name__ = "DisplayString"
_CldccOperParamsFirmwareVersion_Object = MibTableColumn
cldccOperParamsFirmwareVersion = _CldccOperParamsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 20),
    _CldccOperParamsFirmwareVersion_Type()
)
cldccOperParamsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsFirmwareVersion.setStatus("current")


class _CldccOperParamsDriverVersion_Type(DisplayString):
    """Custom type cldccOperParamsDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsDriverVersion_Type.__name__ = "DisplayString"
_CldccOperParamsDriverVersion_Object = MibTableColumn
cldccOperParamsDriverVersion = _CldccOperParamsDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 21),
    _CldccOperParamsDriverVersion_Type()
)
cldccOperParamsDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDriverVersion.setStatus("current")
_CldccOperParamsPowerSaveMode_Type = CiscoLwappDot11ClientPowerSaveMode
_CldccOperParamsPowerSaveMode_Object = MibTableColumn
cldccOperParamsPowerSaveMode = _CldccOperParamsPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 22),
    _CldccOperParamsPowerSaveMode_Type()
)
cldccOperParamsPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsPowerSaveMode.setStatus("current")
_CldccOperParamsAuthMethod_Type = CiscoLwappDot11ClientAuthMethod
_CldccOperParamsAuthMethod_Object = MibTableColumn
cldccOperParamsAuthMethod = _CldccOperParamsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 23),
    _CldccOperParamsAuthMethod_Type()
)
cldccOperParamsAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsAuthMethod.setStatus("current")
_CldccOperParamsKeyMgmtMethod_Type = CiscoLwappDot11ClientKeyMgmtMethod
_CldccOperParamsKeyMgmtMethod_Object = MibTableColumn
cldccOperParamsKeyMgmtMethod = _CldccOperParamsKeyMgmtMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 25),
    _CldccOperParamsKeyMgmtMethod_Type()
)
cldccOperParamsKeyMgmtMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsKeyMgmtMethod.setStatus("current")
_CldccOperParamsEncrMethod_Type = CiscoLwappDot11ClientEncryptionMethod
_CldccOperParamsEncrMethod_Object = MibTableColumn
cldccOperParamsEncrMethod = _CldccOperParamsEncrMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 26),
    _CldccOperParamsEncrMethod_Type()
)
cldccOperParamsEncrMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsEncrMethod.setStatus("current")


class _CldccOperParamsDot1xSecurity_Type(DisplayString):
    """Custom type cldccOperParamsDot1xSecurity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsDot1xSecurity_Type.__name__ = "DisplayString"
_CldccOperParamsDot1xSecurity_Object = MibTableColumn
cldccOperParamsDot1xSecurity = _CldccOperParamsDot1xSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 27),
    _CldccOperParamsDot1xSecurity_Type()
)
cldccOperParamsDot1xSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDot1xSecurity.setStatus("current")


class _CldccOperParamsSysName_Type(DisplayString):
    """Custom type cldccOperParamsSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsSysName_Type.__name__ = "DisplayString"
_CldccOperParamsSysName_Object = MibTableColumn
cldccOperParamsSysName = _CldccOperParamsSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 28),
    _CldccOperParamsSysName_Type()
)
cldccOperParamsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsSysName.setStatus("current")


class _CldccOperParamsLocalization_Type(DisplayString):
    """Custom type cldccOperParamsLocalization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccOperParamsLocalization_Type.__name__ = "DisplayString"
_CldccOperParamsLocalization_Object = MibTableColumn
cldccOperParamsLocalization = _CldccOperParamsLocalization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 1, 1, 29),
    _CldccOperParamsLocalization_Type()
)
cldccOperParamsLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsLocalization.setStatus("current")
_CldccOperParamsDNSTable_Object = MibTable
cldccOperParamsDNSTable = _CldccOperParamsDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cldccOperParamsDNSTable.setStatus("current")
_CldccOperParamsDNSEntry_Object = MibTableRow
cldccOperParamsDNSEntry = _CldccOperParamsDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 2, 1)
)
cldccOperParamsDNSEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccOperParamsDNSServerIndex"),
)
if mibBuilder.loadTexts:
    cldccOperParamsDNSEntry.setStatus("current")
_CldccOperParamsDNSServerIndex_Type = Unsigned32
_CldccOperParamsDNSServerIndex_Object = MibTableColumn
cldccOperParamsDNSServerIndex = _CldccOperParamsDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 2, 1, 1),
    _CldccOperParamsDNSServerIndex_Type()
)
cldccOperParamsDNSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccOperParamsDNSServerIndex.setStatus("current")
_CldccOperParamsDNSServerAddress_Type = IpAddress
_CldccOperParamsDNSServerAddress_Object = MibTableColumn
cldccOperParamsDNSServerAddress = _CldccOperParamsDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 2, 1, 2),
    _CldccOperParamsDNSServerAddress_Type()
)
cldccOperParamsDNSServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsDNSServerAddress.setStatus("current")
_CldccOperParamsWINSTable_Object = MibTable
cldccOperParamsWINSTable = _CldccOperParamsWINSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cldccOperParamsWINSTable.setStatus("current")
_CldccOperParamsWINSEntry_Object = MibTableRow
cldccOperParamsWINSEntry = _CldccOperParamsWINSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 3, 1)
)
cldccOperParamsWINSEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccOperParamsWINSServerIndex"),
)
if mibBuilder.loadTexts:
    cldccOperParamsWINSEntry.setStatus("current")
_CldccOperParamsWINSServerIndex_Type = Unsigned32
_CldccOperParamsWINSServerIndex_Object = MibTableColumn
cldccOperParamsWINSServerIndex = _CldccOperParamsWINSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 3, 1, 1),
    _CldccOperParamsWINSServerIndex_Type()
)
cldccOperParamsWINSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccOperParamsWINSServerIndex.setStatus("current")
_CldccOperParamsWINSServerAddress_Type = IpAddress
_CldccOperParamsWINSServerAddress_Object = MibTableColumn
cldccOperParamsWINSServerAddress = _CldccOperParamsWINSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 3, 1, 2),
    _CldccOperParamsWINSServerAddress_Type()
)
cldccOperParamsWINSServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperParamsWINSServerAddress.setStatus("current")
_CldccOperChannelsTable_Object = MibTable
cldccOperChannelsTable = _CldccOperChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cldccOperChannelsTable.setStatus("current")
_CldccOperChannelsEntry_Object = MibTableRow
cldccOperChannelsEntry = _CldccOperChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 4, 1)
)
cldccOperChannelsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccOperRadioIndex"),
)
if mibBuilder.loadTexts:
    cldccOperChannelsEntry.setStatus("current")
_CldccOperRadioIndex_Type = Unsigned32
_CldccOperRadioIndex_Object = MibTableColumn
cldccOperRadioIndex = _CldccOperRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 4, 1, 1),
    _CldccOperRadioIndex_Type()
)
cldccOperRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccOperRadioIndex.setStatus("current")
_CldccOperRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccOperRadioType_Object = MibTableColumn
cldccOperRadioType = _CldccOperRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 4, 1, 2),
    _CldccOperRadioType_Type()
)
cldccOperRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperRadioType.setStatus("current")


class _CldccOperRadioChannels_Type(DisplayString):
    """Custom type cldccOperRadioChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccOperRadioChannels_Type.__name__ = "DisplayString"
_CldccOperRadioChannels_Object = MibTableColumn
cldccOperRadioChannels = _CldccOperRadioChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 4, 1, 3),
    _CldccOperRadioChannels_Type()
)
cldccOperRadioChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperRadioChannels.setStatus("current")
_CldccOperTxPowerTable_Object = MibTable
cldccOperTxPowerTable = _CldccOperTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cldccOperTxPowerTable.setStatus("current")
_CldccOperTxPowerEntry_Object = MibTableRow
cldccOperTxPowerEntry = _CldccOperTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5, 1)
)
cldccOperTxPowerEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccOperTxPowerIndex"),
)
if mibBuilder.loadTexts:
    cldccOperTxPowerEntry.setStatus("current")
_CldccOperTxPowerIndex_Type = Unsigned32
_CldccOperTxPowerIndex_Object = MibTableColumn
cldccOperTxPowerIndex = _CldccOperTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5, 1, 1),
    _CldccOperTxPowerIndex_Type()
)
cldccOperTxPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccOperTxPowerIndex.setStatus("current")
_CldccOperTxPowerRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccOperTxPowerRadioType_Object = MibTableColumn
cldccOperTxPowerRadioType = _CldccOperTxPowerRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5, 1, 2),
    _CldccOperTxPowerRadioType_Type()
)
cldccOperTxPowerRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperTxPowerRadioType.setStatus("current")


class _CldccOperTxPowerMode_Type(Integer32):
    """Custom type cldccOperTxPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("fixed", 0))
    )


_CldccOperTxPowerMode_Type.__name__ = "Integer32"
_CldccOperTxPowerMode_Object = MibTableColumn
cldccOperTxPowerMode = _CldccOperTxPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5, 1, 3),
    _CldccOperTxPowerMode_Type()
)
cldccOperTxPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperTxPowerMode.setStatus("current")


class _CldccOperTxPower_Type(OctetString):
    """Custom type cldccOperTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccOperTxPower_Type.__name__ = "OctetString"
_CldccOperTxPower_Object = MibTableColumn
cldccOperTxPower = _CldccOperTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 5, 1, 4),
    _CldccOperTxPower_Type()
)
cldccOperTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperTxPower.setStatus("current")
_CldccOperDataRateTable_Object = MibTable
cldccOperDataRateTable = _CldccOperDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cldccOperDataRateTable.setStatus("current")
_CldccOperDataRateEntry_Object = MibTableRow
cldccOperDataRateEntry = _CldccOperDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 6, 1)
)
cldccOperDataRateEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccOperDataRateIndex"),
)
if mibBuilder.loadTexts:
    cldccOperDataRateEntry.setStatus("current")
_CldccOperDataRateIndex_Type = Unsigned32
_CldccOperDataRateIndex_Object = MibTableColumn
cldccOperDataRateIndex = _CldccOperDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 6, 1, 1),
    _CldccOperDataRateIndex_Type()
)
cldccOperDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccOperDataRateIndex.setStatus("current")
_CldccOperDataRateRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccOperDataRateRadioType_Object = MibTableColumn
cldccOperDataRateRadioType = _CldccOperDataRateRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 6, 1, 2),
    _CldccOperDataRateRadioType_Type()
)
cldccOperDataRateRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperDataRateRadioType.setStatus("current")


class _CldccOperDataRates_Type(DisplayString):
    """Custom type cldccOperDataRates based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccOperDataRates_Type.__name__ = "DisplayString"
_CldccOperDataRates_Object = MibTableColumn
cldccOperDataRates = _CldccOperDataRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 2, 6, 1, 3),
    _CldccOperDataRates_Type()
)
cldccOperDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccOperDataRates.setStatus("current")
_CiscoClientCcxProfileReporting_ObjectIdentity = ObjectIdentity
ciscoClientCcxProfileReporting = _CiscoClientCcxProfileReporting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3)
)
_CldccProfileReqTable_Object = MibTable
cldccProfileReqTable = _CldccProfileReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cldccProfileReqTable.setStatus("current")
_CldccProfileReqEntry_Object = MibTableRow
cldccProfileReqEntry = _CldccProfileReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 1, 1)
)
cldccProfileReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccProfileReqEntry.setStatus("current")


class _CldccProfileReqNumProfiles_Type(Integer32):
    """Custom type cldccProfileReqNumProfiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CldccProfileReqNumProfiles_Type.__name__ = "Integer32"
_CldccProfileReqNumProfiles_Object = MibTableColumn
cldccProfileReqNumProfiles = _CldccProfileReqNumProfiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 1, 1, 1),
    _CldccProfileReqNumProfiles_Type()
)
cldccProfileReqNumProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileReqNumProfiles.setStatus("current")


class _CldccProfileReqCurrentProfile_Type(DisplayString):
    """Custom type cldccProfileReqCurrentProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CldccProfileReqCurrentProfile_Type.__name__ = "DisplayString"
_CldccProfileReqCurrentProfile_Object = MibTableColumn
cldccProfileReqCurrentProfile = _CldccProfileReqCurrentProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 1, 1, 2),
    _CldccProfileReqCurrentProfile_Type()
)
cldccProfileReqCurrentProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileReqCurrentProfile.setStatus("current")
_CldccProfileReqReportingStatus_Type = CiscoLwappDot11ClientReqStatus
_CldccProfileReqReportingStatus_Object = MibTableColumn
cldccProfileReqReportingStatus = _CldccProfileReqReportingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 1, 1, 3),
    _CldccProfileReqReportingStatus_Type()
)
cldccProfileReqReportingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccProfileReqReportingStatus.setStatus("current")
_CldccProfileTable_Object = MibTable
cldccProfileTable = _CldccProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cldccProfileTable.setStatus("current")
_CldccProfileEntry_Object = MibTableRow
cldccProfileEntry = _CldccProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1)
)
cldccProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileEntry.setStatus("current")
_CldccProfileIndex_Type = Unsigned32
_CldccProfileIndex_Object = MibTableColumn
cldccProfileIndex = _CldccProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 1),
    _CldccProfileIndex_Type()
)
cldccProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfileIndex.setStatus("current")


class _CldccProfileName_Type(DisplayString):
    """Custom type cldccProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CldccProfileName_Type.__name__ = "DisplayString"
_CldccProfileName_Object = MibTableColumn
cldccProfileName = _CldccProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 2),
    _CldccProfileName_Type()
)
cldccProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileName.setStatus("current")
_CldccProfileSSId_Type = CiscoLwappDot11ClientSSId
_CldccProfileSSId_Object = MibTableColumn
cldccProfileSSId = _CldccProfileSSId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 4),
    _CldccProfileSSId_Type()
)
cldccProfileSSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileSSId.setStatus("current")
_CldccProfileAuthMethod_Type = CiscoLwappDot11ClientAuthMethod
_CldccProfileAuthMethod_Object = MibTableColumn
cldccProfileAuthMethod = _CldccProfileAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 5),
    _CldccProfileAuthMethod_Type()
)
cldccProfileAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileAuthMethod.setStatus("current")
_CldccProfileKeyMgmtMethod_Type = CiscoLwappDot11ClientKeyMgmtMethod
_CldccProfileKeyMgmtMethod_Object = MibTableColumn
cldccProfileKeyMgmtMethod = _CldccProfileKeyMgmtMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 6),
    _CldccProfileKeyMgmtMethod_Type()
)
cldccProfileKeyMgmtMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileKeyMgmtMethod.setStatus("current")
_CldccProfileEncrMethod_Type = CiscoLwappDot11ClientEncryptionMethod
_CldccProfileEncrMethod_Object = MibTableColumn
cldccProfileEncrMethod = _CldccProfileEncrMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 7),
    _CldccProfileEncrMethod_Type()
)
cldccProfileEncrMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileEncrMethod.setStatus("current")


class _CldccProfileDot1xSecurity_Type(DisplayString):
    """Custom type cldccProfileDot1xSecurity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccProfileDot1xSecurity_Type.__name__ = "DisplayString"
_CldccProfileDot1xSecurity_Object = MibTableColumn
cldccProfileDot1xSecurity = _CldccProfileDot1xSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 8),
    _CldccProfileDot1xSecurity_Type()
)
cldccProfileDot1xSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileDot1xSecurity.setStatus("current")
_CldccProfilePowerSaveMode_Type = CiscoLwappDot11ClientPowerSaveMode
_CldccProfilePowerSaveMode_Object = MibTableColumn
cldccProfilePowerSaveMode = _CldccProfilePowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 9),
    _CldccProfilePowerSaveMode_Type()
)
cldccProfilePowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfilePowerSaveMode.setStatus("current")


class _CldccProfileRadioType_Type(DisplayString):
    """Custom type cldccProfileRadioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccProfileRadioType_Type.__name__ = "DisplayString"
_CldccProfileRadioType_Object = MibTableColumn
cldccProfileRadioType = _CldccProfileRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 10),
    _CldccProfileRadioType_Type()
)
cldccProfileRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileRadioType.setStatus("current")


class _CldccProfileProprietaryOptionName_Type(DisplayString):
    """Custom type cldccProfileProprietaryOptionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccProfileProprietaryOptionName_Type.__name__ = "DisplayString"
_CldccProfileProprietaryOptionName_Object = MibTableColumn
cldccProfileProprietaryOptionName = _CldccProfileProprietaryOptionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 11),
    _CldccProfileProprietaryOptionName_Type()
)
cldccProfileProprietaryOptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileProprietaryOptionName.setStatus("current")


class _CldccProfileProprietaryOptionValue_Type(DisplayString):
    """Custom type cldccProfileProprietaryOptionValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccProfileProprietaryOptionValue_Type.__name__ = "DisplayString"
_CldccProfileProprietaryOptionValue_Object = MibTableColumn
cldccProfileProprietaryOptionValue = _CldccProfileProprietaryOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 2, 1, 12),
    _CldccProfileProprietaryOptionValue_Type()
)
cldccProfileProprietaryOptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileProprietaryOptionValue.setStatus("current")
_CldccProfileAPTable_Object = MibTable
cldccProfileAPTable = _CldccProfileAPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cldccProfileAPTable.setStatus("current")
_CldccProfileAPEntry_Object = MibTableRow
cldccProfileAPEntry = _CldccProfileAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 3, 1)
)
cldccProfileAPEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfilePreferredAPIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileAPEntry.setStatus("current")
_CldccProfilePreferredAPIndex_Type = Unsigned32
_CldccProfilePreferredAPIndex_Object = MibTableColumn
cldccProfilePreferredAPIndex = _CldccProfilePreferredAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 3, 1, 1),
    _CldccProfilePreferredAPIndex_Type()
)
cldccProfilePreferredAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfilePreferredAPIndex.setStatus("current")
_CldccProfilePreferredAP_Type = MacAddress
_CldccProfilePreferredAP_Object = MibTableColumn
cldccProfilePreferredAP = _CldccProfilePreferredAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 3, 1, 2),
    _CldccProfilePreferredAP_Type()
)
cldccProfilePreferredAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfilePreferredAP.setStatus("current")
_CldccProfileTxPowerTable_Object = MibTable
cldccProfileTxPowerTable = _CldccProfileTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cldccProfileTxPowerTable.setStatus("current")
_CldccProfileTxPowerEntry_Object = MibTableRow
cldccProfileTxPowerEntry = _CldccProfileTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4, 1)
)
cldccProfileTxPowerEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileTxPowerIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileTxPowerEntry.setStatus("current")
_CldccProfileTxPowerIndex_Type = Unsigned32
_CldccProfileTxPowerIndex_Object = MibTableColumn
cldccProfileTxPowerIndex = _CldccProfileTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4, 1, 1),
    _CldccProfileTxPowerIndex_Type()
)
cldccProfileTxPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfileTxPowerIndex.setStatus("current")
_CldccProfileTxPowerRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccProfileTxPowerRadioType_Object = MibTableColumn
cldccProfileTxPowerRadioType = _CldccProfileTxPowerRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4, 1, 2),
    _CldccProfileTxPowerRadioType_Type()
)
cldccProfileTxPowerRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileTxPowerRadioType.setStatus("current")


class _CldccProfileTxPowerMode_Type(Integer32):
    """Custom type cldccProfileTxPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("fixed", 0))
    )


_CldccProfileTxPowerMode_Type.__name__ = "Integer32"
_CldccProfileTxPowerMode_Object = MibTableColumn
cldccProfileTxPowerMode = _CldccProfileTxPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4, 1, 3),
    _CldccProfileTxPowerMode_Type()
)
cldccProfileTxPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileTxPowerMode.setStatus("current")


class _CldccProfileTxPower_Type(OctetString):
    """Custom type cldccProfileTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccProfileTxPower_Type.__name__ = "OctetString"
_CldccProfileTxPower_Object = MibTableColumn
cldccProfileTxPower = _CldccProfileTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 4, 1, 4),
    _CldccProfileTxPower_Type()
)
cldccProfileTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileTxPower.setStatus("current")
_CldccProfileChannelTable_Object = MibTable
cldccProfileChannelTable = _CldccProfileChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cldccProfileChannelTable.setStatus("current")
_CldccProfileChannelEntry_Object = MibTableRow
cldccProfileChannelEntry = _CldccProfileChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 5, 1)
)
cldccProfileChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileChannelIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileChannelEntry.setStatus("current")
_CldccProfileChannelIndex_Type = Unsigned32
_CldccProfileChannelIndex_Object = MibTableColumn
cldccProfileChannelIndex = _CldccProfileChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 5, 1, 1),
    _CldccProfileChannelIndex_Type()
)
cldccProfileChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfileChannelIndex.setStatus("current")
_CldccProfileChRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccProfileChRadioType_Object = MibTableColumn
cldccProfileChRadioType = _CldccProfileChRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 5, 1, 2),
    _CldccProfileChRadioType_Type()
)
cldccProfileChRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileChRadioType.setStatus("current")


class _CldccProfileChannels_Type(DisplayString):
    """Custom type cldccProfileChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccProfileChannels_Type.__name__ = "DisplayString"
_CldccProfileChannels_Object = MibTableColumn
cldccProfileChannels = _CldccProfileChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 5, 1, 3),
    _CldccProfileChannels_Type()
)
cldccProfileChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileChannels.setStatus("current")
_CldccProfileDataRateTable_Object = MibTable
cldccProfileDataRateTable = _CldccProfileDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cldccProfileDataRateTable.setStatus("current")
_CldccProfileDataRateEntry_Object = MibTableRow
cldccProfileDataRateEntry = _CldccProfileDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 6, 1)
)
cldccProfileDataRateEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileDataRateIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileDataRateEntry.setStatus("current")
_CldccProfileDataRateIndex_Type = Unsigned32
_CldccProfileDataRateIndex_Object = MibTableColumn
cldccProfileDataRateIndex = _CldccProfileDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 6, 1, 1),
    _CldccProfileDataRateIndex_Type()
)
cldccProfileDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfileDataRateIndex.setStatus("current")
_CldccProfileDataRateRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccProfileDataRateRadioType_Object = MibTableColumn
cldccProfileDataRateRadioType = _CldccProfileDataRateRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 6, 1, 2),
    _CldccProfileDataRateRadioType_Type()
)
cldccProfileDataRateRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileDataRateRadioType.setStatus("current")


class _CldccProfileDataRates_Type(DisplayString):
    """Custom type cldccProfileDataRates based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccProfileDataRates_Type.__name__ = "DisplayString"
_CldccProfileDataRates_Object = MibTableColumn
cldccProfileDataRates = _CldccProfileDataRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 6, 1, 3),
    _CldccProfileDataRates_Type()
)
cldccProfileDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileDataRates.setStatus("current")
_CldccProfileRadioOptionsTable_Object = MibTable
cldccProfileRadioOptionsTable = _CldccProfileRadioOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cldccProfileRadioOptionsTable.setStatus("current")
_CldccProfileRadioOptionsEntry_Object = MibTableRow
cldccProfileRadioOptionsEntry = _CldccProfileRadioOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1)
)
cldccProfileRadioOptionsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileIndex"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccProfileRadioOptionIndex"),
)
if mibBuilder.loadTexts:
    cldccProfileRadioOptionsEntry.setStatus("current")


class _CldccProfileRadioOptionIndex_Type(Integer32):
    """Custom type cldccProfileRadioOptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CldccProfileRadioOptionIndex_Type.__name__ = "Integer32"
_CldccProfileRadioOptionIndex_Object = MibTableColumn
cldccProfileRadioOptionIndex = _CldccProfileRadioOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 1),
    _CldccProfileRadioOptionIndex_Type()
)
cldccProfileRadioOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccProfileRadioOptionIndex.setStatus("current")
_CldccProfileRadioOptionsRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccProfileRadioOptionsRadioType_Object = MibTableColumn
cldccProfileRadioOptionsRadioType = _CldccProfileRadioOptionsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 2),
    _CldccProfileRadioOptionsRadioType_Type()
)
cldccProfileRadioOptionsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileRadioOptionsRadioType.setStatus("current")


class _CldccProfilePreambleType_Type(Integer32):
    """Custom type cldccProfilePreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 0),
          ("unknown", 255))
    )


_CldccProfilePreambleType_Type.__name__ = "Integer32"
_CldccProfilePreambleType_Object = MibTableColumn
cldccProfilePreambleType = _CldccProfilePreambleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 3),
    _CldccProfilePreambleType_Type()
)
cldccProfilePreambleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfilePreambleType.setStatus("current")


class _CldccProfileCCAMethod_Type(Integer32):
    """Custom type cldccProfileCCAMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("carrierDetect", 1),
          ("energyCarrierDetect", 2),
          ("energyDetect", 0),
          ("unknown", 255))
    )


_CldccProfileCCAMethod_Type.__name__ = "Integer32"
_CldccProfileCCAMethod_Object = MibTableColumn
cldccProfileCCAMethod = _CldccProfileCCAMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 4),
    _CldccProfileCCAMethod_Type()
)
cldccProfileCCAMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileCCAMethod.setStatus("current")


class _CldccProfileDataRetries_Type(Integer32):
    """Custom type cldccProfileDataRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CldccProfileDataRetries_Type.__name__ = "Integer32"
_CldccProfileDataRetries_Object = MibTableColumn
cldccProfileDataRetries = _CldccProfileDataRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 5),
    _CldccProfileDataRetries_Type()
)
cldccProfileDataRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileDataRetries.setStatus("current")


class _CldccProfileFragmentThreshold_Type(Integer32):
    """Custom type cldccProfileFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_CldccProfileFragmentThreshold_Type.__name__ = "Integer32"
_CldccProfileFragmentThreshold_Object = MibTableColumn
cldccProfileFragmentThreshold = _CldccProfileFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 3, 7, 1, 6),
    _CldccProfileFragmentThreshold_Type()
)
cldccProfileFragmentThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccProfileFragmentThreshold.setStatus("current")
_CiscoClientCcxCapabilityReporting_ObjectIdentity = ObjectIdentity
ciscoClientCcxCapabilityReporting = _CiscoClientCcxCapabilityReporting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4)
)
_CldccCapabilityTable_Object = MibTable
cldccCapabilityTable = _CldccCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cldccCapabilityTable.setStatus("current")
_CldccCapabilityEntry_Object = MibTableRow
cldccCapabilityEntry = _CldccCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 1, 1)
)
cldccCapabilityEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccCapabilityEntry.setStatus("current")
_CldccCapabilityStatus_Type = CiscoLwappDot11ClientReqStatus
_CldccCapabilityStatus_Object = MibTableColumn
cldccCapabilityStatus = _CldccCapabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 1, 1, 1),
    _CldccCapabilityStatus_Type()
)
cldccCapabilityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccCapabilityStatus.setStatus("current")


class _CldccCapabilityRadioType_Type(DisplayString):
    """Custom type cldccCapabilityRadioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccCapabilityRadioType_Type.__name__ = "DisplayString"
_CldccCapabilityRadioType_Object = MibTableColumn
cldccCapabilityRadioType = _CldccCapabilityRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 1, 1, 2),
    _CldccCapabilityRadioType_Type()
)
cldccCapabilityRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityRadioType.setStatus("current")


class _CldccServiceCapability_Type(DisplayString):
    """Custom type cldccServiceCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccServiceCapability_Type.__name__ = "DisplayString"
_CldccServiceCapability_Object = MibTableColumn
cldccServiceCapability = _CldccServiceCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 1, 1, 4),
    _CldccServiceCapability_Type()
)
cldccServiceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccServiceCapability.setStatus("current")
_CldccCapabilityChannelsTable_Object = MibTable
cldccCapabilityChannelsTable = _CldccCapabilityChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cldccCapabilityChannelsTable.setStatus("current")
_CldccCapabilityChannelsEntry_Object = MibTableRow
cldccCapabilityChannelsEntry = _CldccCapabilityChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 2, 1)
)
cldccCapabilityChannelsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccCapabilityRadioIndex"),
)
if mibBuilder.loadTexts:
    cldccCapabilityChannelsEntry.setStatus("current")
_CldccCapabilityRadioIndex_Type = Unsigned32
_CldccCapabilityRadioIndex_Object = MibTableColumn
cldccCapabilityRadioIndex = _CldccCapabilityRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 2, 1, 1),
    _CldccCapabilityRadioIndex_Type()
)
cldccCapabilityRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccCapabilityRadioIndex.setStatus("current")
_CldccCapabilityChRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccCapabilityChRadioType_Object = MibTableColumn
cldccCapabilityChRadioType = _CldccCapabilityChRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 2, 1, 2),
    _CldccCapabilityChRadioType_Type()
)
cldccCapabilityChRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityChRadioType.setStatus("current")


class _CldccCapabilityRadioChannels_Type(DisplayString):
    """Custom type cldccCapabilityRadioChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CldccCapabilityRadioChannels_Type.__name__ = "DisplayString"
_CldccCapabilityRadioChannels_Object = MibTableColumn
cldccCapabilityRadioChannels = _CldccCapabilityRadioChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 2, 1, 3),
    _CldccCapabilityRadioChannels_Type()
)
cldccCapabilityRadioChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityRadioChannels.setStatus("current")
_CldccCapabilityTxPowerTable_Object = MibTable
cldccCapabilityTxPowerTable = _CldccCapabilityTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cldccCapabilityTxPowerTable.setStatus("current")
_CldccCapabilityTxPowerEntry_Object = MibTableRow
cldccCapabilityTxPowerEntry = _CldccCapabilityTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3, 1)
)
cldccCapabilityTxPowerEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccCapabilityTxPowerIndex"),
)
if mibBuilder.loadTexts:
    cldccCapabilityTxPowerEntry.setStatus("current")
_CldccCapabilityTxPowerIndex_Type = Unsigned32
_CldccCapabilityTxPowerIndex_Object = MibTableColumn
cldccCapabilityTxPowerIndex = _CldccCapabilityTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3, 1, 1),
    _CldccCapabilityTxPowerIndex_Type()
)
cldccCapabilityTxPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccCapabilityTxPowerIndex.setStatus("current")
_CldccCapabilityTxPowerRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccCapabilityTxPowerRadioType_Object = MibTableColumn
cldccCapabilityTxPowerRadioType = _CldccCapabilityTxPowerRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3, 1, 2),
    _CldccCapabilityTxPowerRadioType_Type()
)
cldccCapabilityTxPowerRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityTxPowerRadioType.setStatus("current")


class _CldccCapabilityTxPowerMode_Type(Integer32):
    """Custom type cldccCapabilityTxPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("fixed", 0))
    )


_CldccCapabilityTxPowerMode_Type.__name__ = "Integer32"
_CldccCapabilityTxPowerMode_Object = MibTableColumn
cldccCapabilityTxPowerMode = _CldccCapabilityTxPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3, 1, 3),
    _CldccCapabilityTxPowerMode_Type()
)
cldccCapabilityTxPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityTxPowerMode.setStatus("current")


class _CldccCapabilityTxPower_Type(OctetString):
    """Custom type cldccCapabilityTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccCapabilityTxPower_Type.__name__ = "OctetString"
_CldccCapabilityTxPower_Object = MibTableColumn
cldccCapabilityTxPower = _CldccCapabilityTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 3, 1, 4),
    _CldccCapabilityTxPower_Type()
)
cldccCapabilityTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityTxPower.setStatus("current")
_CldccCapabilityDataRateTable_Object = MibTable
cldccCapabilityDataRateTable = _CldccCapabilityDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cldccCapabilityDataRateTable.setStatus("current")
_CldccCapabilityDataRateEntry_Object = MibTableRow
cldccCapabilityDataRateEntry = _CldccCapabilityDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 4, 1)
)
cldccCapabilityDataRateEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB", "cldccCapabilityDataRateIndex"),
)
if mibBuilder.loadTexts:
    cldccCapabilityDataRateEntry.setStatus("current")
_CldccCapabilityDataRateIndex_Type = Unsigned32
_CldccCapabilityDataRateIndex_Object = MibTableColumn
cldccCapabilityDataRateIndex = _CldccCapabilityDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 4, 1, 1),
    _CldccCapabilityDataRateIndex_Type()
)
cldccCapabilityDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccCapabilityDataRateIndex.setStatus("current")
_CldccCapabilityDataRateRadioType_Type = CiscoLwappDot11ClientRadioType
_CldccCapabilityDataRateRadioType_Object = MibTableColumn
cldccCapabilityDataRateRadioType = _CldccCapabilityDataRateRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 4, 1, 2),
    _CldccCapabilityDataRateRadioType_Type()
)
cldccCapabilityDataRateRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityDataRateRadioType.setStatus("current")


class _CldccCapabilityDataRates_Type(DisplayString):
    """Custom type cldccCapabilityDataRates based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccCapabilityDataRates_Type.__name__ = "DisplayString"
_CldccCapabilityDataRates_Object = MibTableColumn
cldccCapabilityDataRates = _CldccCapabilityDataRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 1, 4, 4, 1, 3),
    _CldccCapabilityDataRates_Type()
)
cldccCapabilityDataRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccCapabilityDataRates.setStatus("current")
_CiscoLwappDot11ClientCCXv5ReportingMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11ClientCCXv5ReportingMIBConform = _CiscoLwappDot11ClientCCXv5ReportingMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CCXV5-REPORTING-MIB",
    **{"ciscoLwappDot11ClientCCXv5ReportingMIB": ciscoLwappDot11ClientCCXv5ReportingMIB,
       "ciscoLwappDot11ClientCCXv5ReportingMIBObjects": ciscoLwappDot11ClientCCXv5ReportingMIBObjects,
       "ciscoClientCcxManuReporting": ciscoClientCcxManuReporting,
       "cldccManufacturerInfoTable": cldccManufacturerInfoTable,
       "cldccManufacturerInfoEntry": cldccManufacturerInfoEntry,
       "cldccManufacturerInfoStatus": cldccManufacturerInfoStatus,
       "cldccManufacturerInfoOUI": cldccManufacturerInfoOUI,
       "cldccManufacturerInfoID": cldccManufacturerInfoID,
       "cldccManufacturerInfoModel": cldccManufacturerInfoModel,
       "cldccManufacturerInfoSerialNum": cldccManufacturerInfoSerialNum,
       "cldccManufacturerInfoRadioType": cldccManufacturerInfoRadioType,
       "cldccManufacturerInfoMacAddress": cldccManufacturerInfoMacAddress,
       "cldccManufacturerInfoAntennaType": cldccManufacturerInfoAntennaType,
       "cldccManufacturerInfoAntennaGain": cldccManufacturerInfoAntennaGain,
       "cldccManuRxSensTable": cldccManuRxSensTable,
       "cldccManuRxSensEntry": cldccManuRxSensEntry,
       "cldccManuRxSensRadioIndex": cldccManuRxSensRadioIndex,
       "cldccManuRxSensRadioDataRateIndex": cldccManuRxSensRadioDataRateIndex,
       "cldccManuRxSensRadioType": cldccManuRxSensRadioType,
       "cldccManuRxSensRadioDataRate": cldccManuRxSensRadioDataRate,
       "cldccManuRxSensMinRssi": cldccManuRxSensMinRssi,
       "cldccManuRxSensMaxRssi": cldccManuRxSensMaxRssi,
       "ciscoClientCcxOperReporting": ciscoClientCcxOperReporting,
       "cldccOperParamsTable": cldccOperParamsTable,
       "cldccOperParamsEntry": cldccOperParamsEntry,
       "cldccOperParamsStatus": cldccOperParamsStatus,
       "cldccOperParamsRadioType": cldccOperParamsRadioType,
       "cldccOperParamsSSId": cldccOperParamsSSId,
       "cldccOperParamsDeviceName": cldccOperParamsDeviceName,
       "cldccOperParamsDeviceType": cldccOperParamsDeviceType,
       "cldccOperParamsOSId": cldccOperParamsOSId,
       "cldccOperParamsOSVersion": cldccOperParamsOSVersion,
       "cldccOperParamsIpAddressMode": cldccOperParamsIpAddressMode,
       "cldccOperParamsIpv4Address": cldccOperParamsIpv4Address,
       "cldccOperParamsIpv4SubnetMask": cldccOperParamsIpv4SubnetMask,
       "cldccOperParamsIpv6Address": cldccOperParamsIpv6Address,
       "cldccOperParamsIpv6SubnetMask": cldccOperParamsIpv6SubnetMask,
       "cldccOperParamsDefaultGateway": cldccOperParamsDefaultGateway,
       "cldccOperParamsEntPhone": cldccOperParamsEntPhone,
       "cldccOperParamsCellPhone": cldccOperParamsCellPhone,
       "cldccOperParamsFirmwareVersion": cldccOperParamsFirmwareVersion,
       "cldccOperParamsDriverVersion": cldccOperParamsDriverVersion,
       "cldccOperParamsPowerSaveMode": cldccOperParamsPowerSaveMode,
       "cldccOperParamsAuthMethod": cldccOperParamsAuthMethod,
       "cldccOperParamsKeyMgmtMethod": cldccOperParamsKeyMgmtMethod,
       "cldccOperParamsEncrMethod": cldccOperParamsEncrMethod,
       "cldccOperParamsDot1xSecurity": cldccOperParamsDot1xSecurity,
       "cldccOperParamsSysName": cldccOperParamsSysName,
       "cldccOperParamsLocalization": cldccOperParamsLocalization,
       "cldccOperParamsDNSTable": cldccOperParamsDNSTable,
       "cldccOperParamsDNSEntry": cldccOperParamsDNSEntry,
       "cldccOperParamsDNSServerIndex": cldccOperParamsDNSServerIndex,
       "cldccOperParamsDNSServerAddress": cldccOperParamsDNSServerAddress,
       "cldccOperParamsWINSTable": cldccOperParamsWINSTable,
       "cldccOperParamsWINSEntry": cldccOperParamsWINSEntry,
       "cldccOperParamsWINSServerIndex": cldccOperParamsWINSServerIndex,
       "cldccOperParamsWINSServerAddress": cldccOperParamsWINSServerAddress,
       "cldccOperChannelsTable": cldccOperChannelsTable,
       "cldccOperChannelsEntry": cldccOperChannelsEntry,
       "cldccOperRadioIndex": cldccOperRadioIndex,
       "cldccOperRadioType": cldccOperRadioType,
       "cldccOperRadioChannels": cldccOperRadioChannels,
       "cldccOperTxPowerTable": cldccOperTxPowerTable,
       "cldccOperTxPowerEntry": cldccOperTxPowerEntry,
       "cldccOperTxPowerIndex": cldccOperTxPowerIndex,
       "cldccOperTxPowerRadioType": cldccOperTxPowerRadioType,
       "cldccOperTxPowerMode": cldccOperTxPowerMode,
       "cldccOperTxPower": cldccOperTxPower,
       "cldccOperDataRateTable": cldccOperDataRateTable,
       "cldccOperDataRateEntry": cldccOperDataRateEntry,
       "cldccOperDataRateIndex": cldccOperDataRateIndex,
       "cldccOperDataRateRadioType": cldccOperDataRateRadioType,
       "cldccOperDataRates": cldccOperDataRates,
       "ciscoClientCcxProfileReporting": ciscoClientCcxProfileReporting,
       "cldccProfileReqTable": cldccProfileReqTable,
       "cldccProfileReqEntry": cldccProfileReqEntry,
       "cldccProfileReqNumProfiles": cldccProfileReqNumProfiles,
       "cldccProfileReqCurrentProfile": cldccProfileReqCurrentProfile,
       "cldccProfileReqReportingStatus": cldccProfileReqReportingStatus,
       "cldccProfileTable": cldccProfileTable,
       "cldccProfileEntry": cldccProfileEntry,
       "cldccProfileIndex": cldccProfileIndex,
       "cldccProfileName": cldccProfileName,
       "cldccProfileSSId": cldccProfileSSId,
       "cldccProfileAuthMethod": cldccProfileAuthMethod,
       "cldccProfileKeyMgmtMethod": cldccProfileKeyMgmtMethod,
       "cldccProfileEncrMethod": cldccProfileEncrMethod,
       "cldccProfileDot1xSecurity": cldccProfileDot1xSecurity,
       "cldccProfilePowerSaveMode": cldccProfilePowerSaveMode,
       "cldccProfileRadioType": cldccProfileRadioType,
       "cldccProfileProprietaryOptionName": cldccProfileProprietaryOptionName,
       "cldccProfileProprietaryOptionValue": cldccProfileProprietaryOptionValue,
       "cldccProfileAPTable": cldccProfileAPTable,
       "cldccProfileAPEntry": cldccProfileAPEntry,
       "cldccProfilePreferredAPIndex": cldccProfilePreferredAPIndex,
       "cldccProfilePreferredAP": cldccProfilePreferredAP,
       "cldccProfileTxPowerTable": cldccProfileTxPowerTable,
       "cldccProfileTxPowerEntry": cldccProfileTxPowerEntry,
       "cldccProfileTxPowerIndex": cldccProfileTxPowerIndex,
       "cldccProfileTxPowerRadioType": cldccProfileTxPowerRadioType,
       "cldccProfileTxPowerMode": cldccProfileTxPowerMode,
       "cldccProfileTxPower": cldccProfileTxPower,
       "cldccProfileChannelTable": cldccProfileChannelTable,
       "cldccProfileChannelEntry": cldccProfileChannelEntry,
       "cldccProfileChannelIndex": cldccProfileChannelIndex,
       "cldccProfileChRadioType": cldccProfileChRadioType,
       "cldccProfileChannels": cldccProfileChannels,
       "cldccProfileDataRateTable": cldccProfileDataRateTable,
       "cldccProfileDataRateEntry": cldccProfileDataRateEntry,
       "cldccProfileDataRateIndex": cldccProfileDataRateIndex,
       "cldccProfileDataRateRadioType": cldccProfileDataRateRadioType,
       "cldccProfileDataRates": cldccProfileDataRates,
       "cldccProfileRadioOptionsTable": cldccProfileRadioOptionsTable,
       "cldccProfileRadioOptionsEntry": cldccProfileRadioOptionsEntry,
       "cldccProfileRadioOptionIndex": cldccProfileRadioOptionIndex,
       "cldccProfileRadioOptionsRadioType": cldccProfileRadioOptionsRadioType,
       "cldccProfilePreambleType": cldccProfilePreambleType,
       "cldccProfileCCAMethod": cldccProfileCCAMethod,
       "cldccProfileDataRetries": cldccProfileDataRetries,
       "cldccProfileFragmentThreshold": cldccProfileFragmentThreshold,
       "ciscoClientCcxCapabilityReporting": ciscoClientCcxCapabilityReporting,
       "cldccCapabilityTable": cldccCapabilityTable,
       "cldccCapabilityEntry": cldccCapabilityEntry,
       "cldccCapabilityStatus": cldccCapabilityStatus,
       "cldccCapabilityRadioType": cldccCapabilityRadioType,
       "cldccServiceCapability": cldccServiceCapability,
       "cldccCapabilityChannelsTable": cldccCapabilityChannelsTable,
       "cldccCapabilityChannelsEntry": cldccCapabilityChannelsEntry,
       "cldccCapabilityRadioIndex": cldccCapabilityRadioIndex,
       "cldccCapabilityChRadioType": cldccCapabilityChRadioType,
       "cldccCapabilityRadioChannels": cldccCapabilityRadioChannels,
       "cldccCapabilityTxPowerTable": cldccCapabilityTxPowerTable,
       "cldccCapabilityTxPowerEntry": cldccCapabilityTxPowerEntry,
       "cldccCapabilityTxPowerIndex": cldccCapabilityTxPowerIndex,
       "cldccCapabilityTxPowerRadioType": cldccCapabilityTxPowerRadioType,
       "cldccCapabilityTxPowerMode": cldccCapabilityTxPowerMode,
       "cldccCapabilityTxPower": cldccCapabilityTxPower,
       "cldccCapabilityDataRateTable": cldccCapabilityDataRateTable,
       "cldccCapabilityDataRateEntry": cldccCapabilityDataRateEntry,
       "cldccCapabilityDataRateIndex": cldccCapabilityDataRateIndex,
       "cldccCapabilityDataRateRadioType": cldccCapabilityDataRateRadioType,
       "cldccCapabilityDataRates": cldccCapabilityDataRates,
       "ciscoLwappDot11ClientCCXv5ReportingMIBConform": ciscoLwappDot11ClientCCXv5ReportingMIBConform}
)
