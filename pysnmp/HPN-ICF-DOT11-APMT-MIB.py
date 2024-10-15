# SNMP MIB module (HPN-ICF-DOT11-APMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-APMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:49 2024
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

(HpnicfDot11ChannelScopeType,
 HpnicfDot11MACModeType,
 HpnicfDot11NotifyReasonType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11RFModeType,
 HpnicfDot11RadioElementIndex,
 HpnicfDot11RadioScopeType,
 HpnicfDot11SSIDStringType,
 HpnicfDot11ServicePolicyIDType,
 HpnicfDot11TxPwrLevelScopeType,
 hpnicfDot11,
 hpnicfDot11APElementIndex) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11MACModeType",
    "HpnicfDot11NotifyReasonType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11RFModeType",
    "HpnicfDot11RadioElementIndex",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11SSIDStringType",
    "HpnicfDot11ServicePolicyIDType",
    "HpnicfDot11TxPwrLevelScopeType",
    "hpnicfDot11",
    "hpnicfDot11APElementIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDot11APMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2)
)
hpnicfDot11APMT.setRevisions(
        ("2012-05-07 18:00",
         "2010-10-11 18:00",
         "2010-09-15 12:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-11-07 10:00",
         "2008-07-09 18:00",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-06-19 18:00",
         "2007-04-27 20:00",
         "2007-02-01 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11APObjectGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11APObjectGroup = _HpnicfDot11APObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1)
)
_HpnicfDot11APObjectStatusTable_Object = MibTable
hpnicfDot11APObjectStatusTable = _HpnicfDot11APObjectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11APObjectStatusTable.setStatus("current")
_HpnicfDot11APObjectStatusEntry_Object = MibTableRow
hpnicfDot11APObjectStatusEntry = _HpnicfDot11APObjectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1)
)
hpnicfDot11APObjectStatusEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APObjectStatusEntry.setStatus("current")
_HpnicfDot11APID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11APID_Object = MibTableColumn
hpnicfDot11APID = _HpnicfDot11APID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 1),
    _HpnicfDot11APID_Type()
)
hpnicfDot11APID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APID.setStatus("current")
_HpnicfDot11APIPAddress_Type = IpAddress
_HpnicfDot11APIPAddress_Object = MibTableColumn
hpnicfDot11APIPAddress = _HpnicfDot11APIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 2),
    _HpnicfDot11APIPAddress_Type()
)
hpnicfDot11APIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIPAddress.setStatus("current")
_HpnicfDot11APMacAddress_Type = MacAddress
_HpnicfDot11APMacAddress_Object = MibTableColumn
hpnicfDot11APMacAddress = _HpnicfDot11APMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 3),
    _HpnicfDot11APMacAddress_Type()
)
hpnicfDot11APMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAddress.setStatus("current")


class _HpnicfDot11APOperationStatus_Type(Integer32):
    """Custom type hpnicfDot11APOperationStatus based on Integer32"""
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
        *(("config", 4),
          ("download", 3),
          ("join", 1),
          ("joinConfirm", 2),
          ("run", 5))
    )


_HpnicfDot11APOperationStatus_Type.__name__ = "Integer32"
_HpnicfDot11APOperationStatus_Object = MibTableColumn
hpnicfDot11APOperationStatus = _HpnicfDot11APOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 4),
    _HpnicfDot11APOperationStatus_Type()
)
hpnicfDot11APOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APOperationStatus.setStatus("current")
_HpnicfDot11APTemplateNameOfAP_Type = OctetString
_HpnicfDot11APTemplateNameOfAP_Object = MibTableColumn
hpnicfDot11APTemplateNameOfAP = _HpnicfDot11APTemplateNameOfAP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 5),
    _HpnicfDot11APTemplateNameOfAP_Type()
)
hpnicfDot11APTemplateNameOfAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateNameOfAP.setStatus("current")
_HpnicfDot11APReset_Type = TruthValue
_HpnicfDot11APReset_Object = MibTableColumn
hpnicfDot11APReset = _HpnicfDot11APReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 6),
    _HpnicfDot11APReset_Type()
)
hpnicfDot11APReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APReset.setStatus("current")


class _HpnicfDot11APCpuUsage_Type(Integer32):
    """Custom type hpnicfDot11APCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCpuUsage_Type.__name__ = "Integer32"
_HpnicfDot11APCpuUsage_Object = MibTableColumn
hpnicfDot11APCpuUsage = _HpnicfDot11APCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 7),
    _HpnicfDot11APCpuUsage_Type()
)
hpnicfDot11APCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsage.setUnits("onepercent")


class _HpnicfDot11APConnectionType_Type(Integer32):
    """Custom type hpnicfDot11APConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("notAvailable", 3),
          ("slave", 2))
    )


_HpnicfDot11APConnectionType_Type.__name__ = "Integer32"
_HpnicfDot11APConnectionType_Object = MibTableColumn
hpnicfDot11APConnectionType = _HpnicfDot11APConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 8),
    _HpnicfDot11APConnectionType_Type()
)
hpnicfDot11APConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APConnectionType.setStatus("current")
_HpnicfDot11APLastImgDownloadTime_Type = DateAndTime
_HpnicfDot11APLastImgDownloadTime_Object = MibTableColumn
hpnicfDot11APLastImgDownloadTime = _HpnicfDot11APLastImgDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 9),
    _HpnicfDot11APLastImgDownloadTime_Type()
)
hpnicfDot11APLastImgDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APLastImgDownloadTime.setStatus("current")
_HpnicfDot11APIPv6Address_Type = OctetString
_HpnicfDot11APIPv6Address_Object = MibTableColumn
hpnicfDot11APIPv6Address = _HpnicfDot11APIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 10),
    _HpnicfDot11APIPv6Address_Type()
)
hpnicfDot11APIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIPv6Address.setStatus("current")
_HpnicfDot11APLastRegisterTime_Type = DateAndTime
_HpnicfDot11APLastRegisterTime_Object = MibTableColumn
hpnicfDot11APLastRegisterTime = _HpnicfDot11APLastRegisterTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 11),
    _HpnicfDot11APLastRegisterTime_Type()
)
hpnicfDot11APLastRegisterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APLastRegisterTime.setStatus("current")


class _HpnicfDot11APResetCM_Type(Integer32):
    """Custom type hpnicfDot11APResetCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("restart", 1))
    )


_HpnicfDot11APResetCM_Type.__name__ = "Integer32"
_HpnicfDot11APResetCM_Object = MibTableColumn
hpnicfDot11APResetCM = _HpnicfDot11APResetCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 1, 1, 12),
    _HpnicfDot11APResetCM_Type()
)
hpnicfDot11APResetCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APResetCM.setStatus("current")
_HpnicfDot11APObjectTable_Object = MibTable
hpnicfDot11APObjectTable = _HpnicfDot11APObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11APObjectTable.setStatus("current")
_HpnicfDot11APObjectEntry_Object = MibTableRow
hpnicfDot11APObjectEntry = _HpnicfDot11APObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1)
)
hpnicfDot11APObjectEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APObjID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APObjectEntry.setStatus("current")
_HpnicfDot11APObjID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11APObjID_Object = MibTableColumn
hpnicfDot11APObjID = _HpnicfDot11APObjID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 1),
    _HpnicfDot11APObjID_Type()
)
hpnicfDot11APObjID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APObjID.setStatus("current")
_HpnicfDot11CurrAPIPAddress_Type = IpAddress
_HpnicfDot11CurrAPIPAddress_Object = MibTableColumn
hpnicfDot11CurrAPIPAddress = _HpnicfDot11CurrAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 2),
    _HpnicfDot11CurrAPIPAddress_Type()
)
hpnicfDot11CurrAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPIPAddress.setStatus("current")
_HpnicfDot11CurrAPMacAddress_Type = MacAddress
_HpnicfDot11CurrAPMacAddress_Object = MibTableColumn
hpnicfDot11CurrAPMacAddress = _HpnicfDot11CurrAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 3),
    _HpnicfDot11CurrAPMacAddress_Type()
)
hpnicfDot11CurrAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMacAddress.setStatus("current")
_HpnicfDot11CurrACPortIndex_Type = Integer32
_HpnicfDot11CurrACPortIndex_Object = MibTableColumn
hpnicfDot11CurrACPortIndex = _HpnicfDot11CurrACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 4),
    _HpnicfDot11CurrACPortIndex_Type()
)
hpnicfDot11CurrACPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrACPortIndex.setStatus("current")
_HpnicfDot11CurrAPMACMode_Type = HpnicfDot11MACModeType
_HpnicfDot11CurrAPMACMode_Object = MibTableColumn
hpnicfDot11CurrAPMACMode = _HpnicfDot11CurrAPMACMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 5),
    _HpnicfDot11CurrAPMACMode_Type()
)
hpnicfDot11CurrAPMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMACMode.setStatus("current")
_HpnicfDot11CurrAPTemplateName_Type = OctetString
_HpnicfDot11CurrAPTemplateName_Object = MibTableColumn
hpnicfDot11CurrAPTemplateName = _HpnicfDot11CurrAPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 6),
    _HpnicfDot11CurrAPTemplateName_Type()
)
hpnicfDot11CurrAPTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPTemplateName.setStatus("current")
_HpnicfDot11CurrAPStationAssocCount_Type = Integer32
_HpnicfDot11CurrAPStationAssocCount_Object = MibTableColumn
hpnicfDot11CurrAPStationAssocCount = _HpnicfDot11CurrAPStationAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 7),
    _HpnicfDot11CurrAPStationAssocCount_Type()
)
hpnicfDot11CurrAPStationAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPStationAssocCount.setStatus("current")
_HpnicfDot11CurrAPName_Type = OctetString
_HpnicfDot11CurrAPName_Object = MibTableColumn
hpnicfDot11CurrAPName = _HpnicfDot11CurrAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 8),
    _HpnicfDot11CurrAPName_Type()
)
hpnicfDot11CurrAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPName.setStatus("current")
_HpnicfDot11CurrAPModelName_Type = OctetString
_HpnicfDot11CurrAPModelName_Object = MibTableColumn
hpnicfDot11CurrAPModelName = _HpnicfDot11CurrAPModelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 9),
    _HpnicfDot11CurrAPModelName_Type()
)
hpnicfDot11CurrAPModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPModelName.setStatus("current")
_HpnicfDot11CurrAPImageName_Type = OctetString
_HpnicfDot11CurrAPImageName_Object = MibTableColumn
hpnicfDot11CurrAPImageName = _HpnicfDot11CurrAPImageName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 10),
    _HpnicfDot11CurrAPImageName_Type()
)
hpnicfDot11CurrAPImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPImageName.setStatus("current")
_HpnicfDot11CurrAPSoftwareVersion_Type = OctetString
_HpnicfDot11CurrAPSoftwareVersion_Object = MibTableColumn
hpnicfDot11CurrAPSoftwareVersion = _HpnicfDot11CurrAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 11),
    _HpnicfDot11CurrAPSoftwareVersion_Type()
)
hpnicfDot11CurrAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPSoftwareVersion.setStatus("current")
_HpnicfDot11CurrAPIPNetMask_Type = IpAddress
_HpnicfDot11CurrAPIPNetMask_Object = MibTableColumn
hpnicfDot11CurrAPIPNetMask = _HpnicfDot11CurrAPIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 12),
    _HpnicfDot11CurrAPIPNetMask_Type()
)
hpnicfDot11CurrAPIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPIPNetMask.setStatus("current")
_HpnicfDot11CurrRadioModeSupport_Type = Integer32
_HpnicfDot11CurrRadioModeSupport_Object = MibTableColumn
hpnicfDot11CurrRadioModeSupport = _HpnicfDot11CurrRadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 13),
    _HpnicfDot11CurrRadioModeSupport_Type()
)
hpnicfDot11CurrRadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrRadioModeSupport.setStatus("current")
_HpnicfDot11CurrIfNumber_Type = Integer32
_HpnicfDot11CurrIfNumber_Object = MibTableColumn
hpnicfDot11CurrIfNumber = _HpnicfDot11CurrIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 14),
    _HpnicfDot11CurrIfNumber_Type()
)
hpnicfDot11CurrIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrIfNumber.setStatus("current")
_HpnicfDot11CurrAPElementID_Type = Integer32
_HpnicfDot11CurrAPElementID_Object = MibTableColumn
hpnicfDot11CurrAPElementID = _HpnicfDot11CurrAPElementID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 15),
    _HpnicfDot11CurrAPElementID_Type()
)
hpnicfDot11CurrAPElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPElementID.setStatus("current")


class _HpnicfDot11CurrAPMode_Type(Integer32):
    """Custom type hpnicfDot11CurrAPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("route", 2))
    )


_HpnicfDot11CurrAPMode_Type.__name__ = "Integer32"
_HpnicfDot11CurrAPMode_Object = MibTableColumn
hpnicfDot11CurrAPMode = _HpnicfDot11CurrAPMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 16),
    _HpnicfDot11CurrAPMode_Type()
)
hpnicfDot11CurrAPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMode.setStatus("current")
_HpnicfDot11CurrAPIPv6Address_Type = OctetString
_HpnicfDot11CurrAPIPv6Address_Object = MibTableColumn
hpnicfDot11CurrAPIPv6Address = _HpnicfDot11CurrAPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 17),
    _HpnicfDot11CurrAPIPv6Address_Type()
)
hpnicfDot11CurrAPIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPIPv6Address.setStatus("current")
_HpnicfDot11CurrAPSSIDNumber_Type = Integer32
_HpnicfDot11CurrAPSSIDNumber_Object = MibTableColumn
hpnicfDot11CurrAPSSIDNumber = _HpnicfDot11CurrAPSSIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 18),
    _HpnicfDot11CurrAPSSIDNumber_Type()
)
hpnicfDot11CurrAPSSIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPSSIDNumber.setStatus("current")
_HpnicfDot11CurrAPManufacturer_Type = OctetString
_HpnicfDot11CurrAPManufacturer_Object = MibTableColumn
hpnicfDot11CurrAPManufacturer = _HpnicfDot11CurrAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 19),
    _HpnicfDot11CurrAPManufacturer_Type()
)
hpnicfDot11CurrAPManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPManufacturer.setStatus("current")
_HpnicfDot11CurrAPMemorySize_Type = Integer32
_HpnicfDot11CurrAPMemorySize_Object = MibTableColumn
hpnicfDot11CurrAPMemorySize = _HpnicfDot11CurrAPMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 20),
    _HpnicfDot11CurrAPMemorySize_Type()
)
hpnicfDot11CurrAPMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMemorySize.setUnits("kbytes")
_HpnicfDot11CurrAPMemSizeInBytes_Type = Integer32
_HpnicfDot11CurrAPMemSizeInBytes_Object = MibTableColumn
hpnicfDot11CurrAPMemSizeInBytes = _HpnicfDot11CurrAPMemSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 21),
    _HpnicfDot11CurrAPMemSizeInBytes_Type()
)
hpnicfDot11CurrAPMemSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMemSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMemSizeInBytes.setUnits("bytes")
_HpnicfDot11CurrAPFlashSize_Type = Integer32
_HpnicfDot11CurrAPFlashSize_Object = MibTableColumn
hpnicfDot11CurrAPFlashSize = _HpnicfDot11CurrAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 22),
    _HpnicfDot11CurrAPFlashSize_Type()
)
hpnicfDot11CurrAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPFlashSize.setUnits("Kbytes")
_HpnicfDot11CurrAPFlashSizeInBytes_Type = Integer32
_HpnicfDot11CurrAPFlashSizeInBytes_Object = MibTableColumn
hpnicfDot11CurrAPFlashSizeInBytes = _HpnicfDot11CurrAPFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 23),
    _HpnicfDot11CurrAPFlashSizeInBytes_Type()
)
hpnicfDot11CurrAPFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPFlashSizeInBytes.setUnits("bytes")
_HpnicfDot11CurrAPReleasedVersion_Type = OctetString
_HpnicfDot11CurrAPReleasedVersion_Object = MibTableColumn
hpnicfDot11CurrAPReleasedVersion = _HpnicfDot11CurrAPReleasedVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 24),
    _HpnicfDot11CurrAPReleasedVersion_Type()
)
hpnicfDot11CurrAPReleasedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPReleasedVersion.setStatus("current")
_HpnicfDot11CurrRadioModeSupport2_Type = Integer32
_HpnicfDot11CurrRadioModeSupport2_Object = MibTableColumn
hpnicfDot11CurrRadioModeSupport2 = _HpnicfDot11CurrRadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 25),
    _HpnicfDot11CurrRadioModeSupport2_Type()
)
hpnicfDot11CurrRadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrRadioModeSupport2.setStatus("current")
_HpnicfDot11CurrAPCPUTypeCM_Type = OctetString
_HpnicfDot11CurrAPCPUTypeCM_Object = MibTableColumn
hpnicfDot11CurrAPCPUTypeCM = _HpnicfDot11CurrAPCPUTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 26),
    _HpnicfDot11CurrAPCPUTypeCM_Type()
)
hpnicfDot11CurrAPCPUTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPCPUTypeCM.setStatus("current")
_HpnicfDot11CurrAPMemoryTypeCM_Type = OctetString
_HpnicfDot11CurrAPMemoryTypeCM_Object = MibTableColumn
hpnicfDot11CurrAPMemoryTypeCM = _HpnicfDot11CurrAPMemoryTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 27),
    _HpnicfDot11CurrAPMemoryTypeCM_Type()
)
hpnicfDot11CurrAPMemoryTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPMemoryTypeCM.setStatus("current")
_HpnicfDot11CurrAPBSSIDNumberCM_Type = Integer32
_HpnicfDot11CurrAPBSSIDNumberCM_Object = MibTableColumn
hpnicfDot11CurrAPBSSIDNumberCM = _HpnicfDot11CurrAPBSSIDNumberCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 2, 1, 28),
    _HpnicfDot11CurrAPBSSIDNumberCM_Type()
)
hpnicfDot11CurrAPBSSIDNumberCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPBSSIDNumberCM.setStatus("current")
_HpnicfDot11APRadioTable_Object = MibTable
hpnicfDot11APRadioTable = _HpnicfDot11APRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11APRadioTable.setStatus("current")
_HpnicfDot11APRadioEntry_Object = MibTableRow
hpnicfDot11APRadioEntry = _HpnicfDot11APRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1)
)
hpnicfDot11APRadioEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APRadioEntry.setStatus("current")


class _HpnicfDot11CurAPID_Type(OctetString):
    """Custom type hpnicfDot11CurAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfDot11CurAPID_Type.__name__ = "OctetString"
_HpnicfDot11CurAPID_Object = MibTableColumn
hpnicfDot11CurAPID = _HpnicfDot11CurAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 1),
    _HpnicfDot11CurAPID_Type()
)
hpnicfDot11CurAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11CurAPID.setStatus("current")


class _HpnicfDot11RadioID_Type(Integer32):
    """Custom type hpnicfDot11RadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDot11RadioID_Type.__name__ = "Integer32"
_HpnicfDot11RadioID_Object = MibTableColumn
hpnicfDot11RadioID = _HpnicfDot11RadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 2),
    _HpnicfDot11RadioID_Type()
)
hpnicfDot11RadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11RadioID.setStatus("current")
_HpnicfDot11AdminStatus_Type = TruthValue
_HpnicfDot11AdminStatus_Object = MibTableColumn
hpnicfDot11AdminStatus = _HpnicfDot11AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 3),
    _HpnicfDot11AdminStatus_Type()
)
hpnicfDot11AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AdminStatus.setStatus("current")
_HpnicfDot11OperStatus_Type = TruthValue
_HpnicfDot11OperStatus_Object = MibTableColumn
hpnicfDot11OperStatus = _HpnicfDot11OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 4),
    _HpnicfDot11OperStatus_Type()
)
hpnicfDot11OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11OperStatus.setStatus("current")
_HpnicfDot11Channel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11Channel_Object = MibTableColumn
hpnicfDot11Channel = _HpnicfDot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 5),
    _HpnicfDot11Channel_Type()
)
hpnicfDot11Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Channel.setStatus("current")
_HpnicfDot11TxPowerLevel_Type = HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11TxPowerLevel_Object = MibTableColumn
hpnicfDot11TxPowerLevel = _HpnicfDot11TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 6),
    _HpnicfDot11TxPowerLevel_Type()
)
hpnicfDot11TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11TxPowerLevel.setUnits("dbm")
_HpnicfDot11APRadioIfIndex_Type = Integer32
_HpnicfDot11APRadioIfIndex_Object = MibTableColumn
hpnicfDot11APRadioIfIndex = _HpnicfDot11APRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 7),
    _HpnicfDot11APRadioIfIndex_Type()
)
hpnicfDot11APRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APRadioIfIndex.setStatus("current")
_HpnicfDot11AntennaGain_Type = Integer32
_HpnicfDot11AntennaGain_Object = MibTableColumn
hpnicfDot11AntennaGain = _HpnicfDot11AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 8),
    _HpnicfDot11AntennaGain_Type()
)
hpnicfDot11AntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AntennaGain.setUnits("dBi")
_HpnicfDot11MaxBandwidth_Type = Integer32
_HpnicfDot11MaxBandwidth_Object = MibTableColumn
hpnicfDot11MaxBandwidth = _HpnicfDot11MaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 9),
    _HpnicfDot11MaxBandwidth_Type()
)
hpnicfDot11MaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MaxBandwidth.setUnits("Mbps")
_HpnicfDot11ResourceUseRatio_Type = Integer32
_HpnicfDot11ResourceUseRatio_Object = MibTableColumn
hpnicfDot11ResourceUseRatio = _HpnicfDot11ResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 10),
    _HpnicfDot11ResourceUseRatio_Type()
)
hpnicfDot11ResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ResourceUseRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11ResourceUseRatio.setUnits("onepercent")
_HpnicfDot11RadioModeSupport_Type = Unsigned32
_HpnicfDot11RadioModeSupport_Object = MibTableColumn
hpnicfDot11RadioModeSupport = _HpnicfDot11RadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 11),
    _HpnicfDot11RadioModeSupport_Type()
)
hpnicfDot11RadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioModeSupport.setStatus("current")


class _HpnicfDot11TxPowerLevel2_Type(Integer32):
    """Custom type hpnicfDot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HpnicfDot11TxPowerLevel2_Type.__name__ = "Integer32"
_HpnicfDot11TxPowerLevel2_Object = MibTableColumn
hpnicfDot11TxPowerLevel2 = _HpnicfDot11TxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 12),
    _HpnicfDot11TxPowerLevel2_Type()
)
hpnicfDot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxPowerLevel2.setStatus("current")
_HpnicfDot11PowerMgmtStatus_Type = TruthValue
_HpnicfDot11PowerMgmtStatus_Object = MibTableColumn
hpnicfDot11PowerMgmtStatus = _HpnicfDot11PowerMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 13),
    _HpnicfDot11PowerMgmtStatus_Type()
)
hpnicfDot11PowerMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11PowerMgmtStatus.setStatus("current")
_HpnicfDot11ChannelSwitchTimes_Type = Counter32
_HpnicfDot11ChannelSwitchTimes_Object = MibTableColumn
hpnicfDot11ChannelSwitchTimes = _HpnicfDot11ChannelSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 14),
    _HpnicfDot11ChannelSwitchTimes_Type()
)
hpnicfDot11ChannelSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ChannelSwitchTimes.setStatus("current")
_HpnicfDot11AntennaType_Type = OctetString
_HpnicfDot11AntennaType_Object = MibTableColumn
hpnicfDot11AntennaType = _HpnicfDot11AntennaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 15),
    _HpnicfDot11AntennaType_Type()
)
hpnicfDot11AntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AntennaType.setStatus("current")
_HpnicfDot11DiversitySelectionRx_Type = TruthValue
_HpnicfDot11DiversitySelectionRx_Object = MibTableColumn
hpnicfDot11DiversitySelectionRx = _HpnicfDot11DiversitySelectionRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 16),
    _HpnicfDot11DiversitySelectionRx_Type()
)
hpnicfDot11DiversitySelectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DiversitySelectionRx.setStatus("current")
_HpnicfDot11MaxTxPwrLvl_Type = OctetString
_HpnicfDot11MaxTxPwrLvl_Object = MibTableColumn
hpnicfDot11MaxTxPwrLvl = _HpnicfDot11MaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 17),
    _HpnicfDot11MaxTxPwrLvl_Type()
)
hpnicfDot11MaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MaxTxPwrLvl.setStatus("current")
_HpnicfDot11PwrAttRange_Type = Integer32
_HpnicfDot11PwrAttRange_Object = MibTableColumn
hpnicfDot11PwrAttRange = _HpnicfDot11PwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 18),
    _HpnicfDot11PwrAttRange_Type()
)
hpnicfDot11PwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11PwrAttRange.setStatus("current")
_HpnicfDot11AvgRxSignalStrength_Type = Integer32
_HpnicfDot11AvgRxSignalStrength_Object = MibTableColumn
hpnicfDot11AvgRxSignalStrength = _HpnicfDot11AvgRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 19),
    _HpnicfDot11AvgRxSignalStrength_Type()
)
hpnicfDot11AvgRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AvgRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AvgRxSignalStrength.setUnits("dBm")
_HpnicfDot11HighestRxSignalStrength_Type = Integer32
_HpnicfDot11HighestRxSignalStrength_Object = MibTableColumn
hpnicfDot11HighestRxSignalStrength = _HpnicfDot11HighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 20),
    _HpnicfDot11HighestRxSignalStrength_Type()
)
hpnicfDot11HighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11HighestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11HighestRxSignalStrength.setUnits("dBm")
_HpnicfDot11LowestRxSignalStrength_Type = Integer32
_HpnicfDot11LowestRxSignalStrength_Object = MibTableColumn
hpnicfDot11LowestRxSignalStrength = _HpnicfDot11LowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 21),
    _HpnicfDot11LowestRxSignalStrength_Type()
)
hpnicfDot11LowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11LowestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11LowestRxSignalStrength.setUnits("dBm")
_HpnicfDot11RadioIfUpdownTimes_Type = Counter32
_HpnicfDot11RadioIfUpdownTimes_Object = MibTableColumn
hpnicfDot11RadioIfUpdownTimes = _HpnicfDot11RadioIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 22),
    _HpnicfDot11RadioIfUpdownTimes_Type()
)
hpnicfDot11RadioIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIfUpdownTimes.setStatus("current")
_HpnicfDot11RadioIfLastChange_Type = TimeTicks
_HpnicfDot11RadioIfLastChange_Object = MibTableColumn
hpnicfDot11RadioIfLastChange = _HpnicfDot11RadioIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 23),
    _HpnicfDot11RadioIfLastChange_Type()
)
hpnicfDot11RadioIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIfLastChange.setStatus("current")
_HpnicfDot11RadioModeSupport2_Type = Unsigned32
_HpnicfDot11RadioModeSupport2_Object = MibTableColumn
hpnicfDot11RadioModeSupport2 = _HpnicfDot11RadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 24),
    _HpnicfDot11RadioModeSupport2_Type()
)
hpnicfDot11RadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioModeSupport2.setStatus("current")


class _HpnicfDot11OperStatusCM_Type(Integer32):
    """Custom type hpnicfDot11OperStatusCM based on Integer32"""
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
        *(("admindown", 4),
          ("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HpnicfDot11OperStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11OperStatusCM_Object = MibTableColumn
hpnicfDot11OperStatusCM = _HpnicfDot11OperStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 3, 1, 25),
    _HpnicfDot11OperStatusCM_Type()
)
hpnicfDot11OperStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11OperStatusCM.setStatus("current")
_HpnicfDot11APBSSTable_Object = MibTable
hpnicfDot11APBSSTable = _HpnicfDot11APBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11APBSSTable.setStatus("current")
_HpnicfDot11APBSSEntry_Object = MibTableRow
hpnicfDot11APBSSEntry = _HpnicfDot11APBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1)
)
hpnicfDot11APBSSEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APBSSEntry.setStatus("current")


class _HpnicfDot11WlanID_Type(Integer32):
    """Custom type hpnicfDot11WlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDot11WlanID_Type.__name__ = "Integer32"
_HpnicfDot11WlanID_Object = MibTableColumn
hpnicfDot11WlanID = _HpnicfDot11WlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 1),
    _HpnicfDot11WlanID_Type()
)
hpnicfDot11WlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WlanID.setStatus("current")
_HpnicfDot11BSSID_Type = MacAddress
_HpnicfDot11BSSID_Object = MibTableColumn
hpnicfDot11BSSID = _HpnicfDot11BSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 2),
    _HpnicfDot11BSSID_Type()
)
hpnicfDot11BSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSID.setStatus("current")
_HpnicfDot11CurrSvcPolicyID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11CurrSvcPolicyID_Object = MibTableColumn
hpnicfDot11CurrSvcPolicyID = _HpnicfDot11CurrSvcPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 3),
    _HpnicfDot11CurrSvcPolicyID_Type()
)
hpnicfDot11CurrSvcPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrSvcPolicyID.setStatus("current")
_HpnicfDot11SSID_Type = OctetString
_HpnicfDot11SSID_Object = MibTableColumn
hpnicfDot11SSID = _HpnicfDot11SSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 4),
    _HpnicfDot11SSID_Type()
)
hpnicfDot11SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SSID.setStatus("current")
_HpnicfDot11CurrSSIDResourceUseRatio_Type = Integer32
_HpnicfDot11CurrSSIDResourceUseRatio_Object = MibTableColumn
hpnicfDot11CurrSSIDResourceUseRatio = _HpnicfDot11CurrSSIDResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 5),
    _HpnicfDot11CurrSSIDResourceUseRatio_Type()
)
hpnicfDot11CurrSSIDResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrSSIDResourceUseRatio.setStatus("current")
_HpnicfDot11APEssVlanId_Type = Integer32
_HpnicfDot11APEssVlanId_Object = MibTableColumn
hpnicfDot11APEssVlanId = _HpnicfDot11APEssVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 4, 1, 6),
    _HpnicfDot11APEssVlanId_Type()
)
hpnicfDot11APEssVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APEssVlanId.setStatus("current")
_HpnicfDot11APModelTable_Object = MibTable
hpnicfDot11APModelTable = _HpnicfDot11APModelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11APModelTable.setStatus("current")
_HpnicfDot11APModelEntry_Object = MibTableRow
hpnicfDot11APModelEntry = _HpnicfDot11APModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1)
)
hpnicfDot11APModelEntry.setIndexNames(
    (1, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APModelAlias"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APModelEntry.setStatus("current")


class _HpnicfDot11APModelAlias_Type(OctetString):
    """Custom type hpnicfDot11APModelAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11APModelAlias_Type.__name__ = "OctetString"
_HpnicfDot11APModelAlias_Object = MibTableColumn
hpnicfDot11APModelAlias = _HpnicfDot11APModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 1),
    _HpnicfDot11APModelAlias_Type()
)
hpnicfDot11APModelAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APModelAlias.setStatus("current")
_HpnicfDot11APModelName_Type = OctetString
_HpnicfDot11APModelName_Object = MibTableColumn
hpnicfDot11APModelName = _HpnicfDot11APModelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 2),
    _HpnicfDot11APModelName_Type()
)
hpnicfDot11APModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APModelName.setStatus("current")
_HpnicfDot11RadioNumSupport_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RadioNumSupport_Object = MibTableColumn
hpnicfDot11RadioNumSupport = _HpnicfDot11RadioNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 3),
    _HpnicfDot11RadioNumSupport_Type()
)
hpnicfDot11RadioNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioNumSupport.setStatus("current")
_HpnicfDot11StationNumSupport_Type = Integer32
_HpnicfDot11StationNumSupport_Object = MibTableColumn
hpnicfDot11StationNumSupport = _HpnicfDot11StationNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 4),
    _HpnicfDot11StationNumSupport_Type()
)
hpnicfDot11StationNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationNumSupport.setStatus("current")


class _HpnicfDot11MACModeSupport_Type(HpnicfDot11MACModeType):
    """Custom type hpnicfDot11MACModeSupport based on HpnicfDot11MACModeType"""


_HpnicfDot11MACModeSupport_Object = MibTableColumn
hpnicfDot11MACModeSupport = _HpnicfDot11MACModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 5),
    _HpnicfDot11MACModeSupport_Type()
)
hpnicfDot11MACModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MACModeSupport.setStatus("current")
_HpnicfDot11APManufacturer_Type = OctetString
_HpnicfDot11APManufacturer_Object = MibTableColumn
hpnicfDot11APManufacturer = _HpnicfDot11APManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 6),
    _HpnicfDot11APManufacturer_Type()
)
hpnicfDot11APManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APManufacturer.setStatus("current")
_HpnicfDot11APCPUType_Type = OctetString
_HpnicfDot11APCPUType_Object = MibTableColumn
hpnicfDot11APCPUType = _HpnicfDot11APCPUType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 7),
    _HpnicfDot11APCPUType_Type()
)
hpnicfDot11APCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUType.setStatus("current")
_HpnicfDot11APCPUClockSpeed_Type = Unsigned32
_HpnicfDot11APCPUClockSpeed_Object = MibTableColumn
hpnicfDot11APCPUClockSpeed = _HpnicfDot11APCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 8),
    _HpnicfDot11APCPUClockSpeed_Type()
)
hpnicfDot11APCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUClockSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUClockSpeed.setUnits("Hz")
_HpnicfDot11APMemoryType_Type = OctetString
_HpnicfDot11APMemoryType_Object = MibTableColumn
hpnicfDot11APMemoryType = _HpnicfDot11APMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 9),
    _HpnicfDot11APMemoryType_Type()
)
hpnicfDot11APMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemoryType.setStatus("current")
_HpnicfDot11APFlashType_Type = OctetString
_HpnicfDot11APFlashType_Object = MibTableColumn
hpnicfDot11APFlashType = _HpnicfDot11APFlashType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 11),
    _HpnicfDot11APFlashType_Type()
)
hpnicfDot11APFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashType.setStatus("current")
_HpnicfDot11APFlashSize_Type = Unsigned32
_HpnicfDot11APFlashSize_Object = MibTableColumn
hpnicfDot11APFlashSize = _HpnicfDot11APFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 12),
    _HpnicfDot11APFlashSize_Type()
)
hpnicfDot11APFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashSize.setUnits("kbytes")
_HpnicfDot11APMemSize_Type = Gauge32
_HpnicfDot11APMemSize_Object = MibTableColumn
hpnicfDot11APMemSize = _HpnicfDot11APMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 13),
    _HpnicfDot11APMemSize_Type()
)
hpnicfDot11APMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemSize.setUnits("bytes")
_HpnicfDot11APFlashSizeInBytes_Type = Unsigned32
_HpnicfDot11APFlashSizeInBytes_Object = MibTableColumn
hpnicfDot11APFlashSizeInBytes = _HpnicfDot11APFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 14),
    _HpnicfDot11APFlashSizeInBytes_Type()
)
hpnicfDot11APFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashSizeInBytes.setUnits("bytes")
_HpnicfDot11APMemorySize_Type = Unsigned32
_HpnicfDot11APMemorySize_Object = MibTableColumn
hpnicfDot11APMemorySize = _HpnicfDot11APMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 5, 1, 20),
    _HpnicfDot11APMemorySize_Type()
)
hpnicfDot11APMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemorySize.setUnits("kbytes")
_HpnicfDot11APIfTable_Object = MibTable
hpnicfDot11APIfTable = _HpnicfDot11APIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfTable.setStatus("current")
_HpnicfDot11APIfEntry_Object = MibTableRow
hpnicfDot11APIfEntry = _HpnicfDot11APIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1)
)
hpnicfDot11APIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APObjID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfEntry.setStatus("current")
_HpnicfDot11APIfIndex_Type = Integer32
_HpnicfDot11APIfIndex_Object = MibTableColumn
hpnicfDot11APIfIndex = _HpnicfDot11APIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 1),
    _HpnicfDot11APIfIndex_Type()
)
hpnicfDot11APIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APIfIndex.setStatus("current")
_HpnicfDot11APIfDescr_Type = OctetString
_HpnicfDot11APIfDescr_Object = MibTableColumn
hpnicfDot11APIfDescr = _HpnicfDot11APIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 2),
    _HpnicfDot11APIfDescr_Type()
)
hpnicfDot11APIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfDescr.setStatus("current")
_HpnicfDot11APIfType_Type = Integer32
_HpnicfDot11APIfType_Object = MibTableColumn
hpnicfDot11APIfType = _HpnicfDot11APIfType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 3),
    _HpnicfDot11APIfType_Type()
)
hpnicfDot11APIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfType.setStatus("current")
_HpnicfDot11APIfMtu_Type = Integer32
_HpnicfDot11APIfMtu_Object = MibTableColumn
hpnicfDot11APIfMtu = _HpnicfDot11APIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 4),
    _HpnicfDot11APIfMtu_Type()
)
hpnicfDot11APIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APIfMtu.setStatus("current")
_HpnicfDot11APIfPHYAddress_Type = OctetString
_HpnicfDot11APIfPHYAddress_Object = MibTableColumn
hpnicfDot11APIfPHYAddress = _HpnicfDot11APIfPHYAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 5),
    _HpnicfDot11APIfPHYAddress_Type()
)
hpnicfDot11APIfPHYAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfPHYAddress.setStatus("current")
_HpnicfDot11APIfSpeed_Type = Integer32
_HpnicfDot11APIfSpeed_Object = MibTableColumn
hpnicfDot11APIfSpeed = _HpnicfDot11APIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 6),
    _HpnicfDot11APIfSpeed_Type()
)
hpnicfDot11APIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APIfSpeed.setUnits("Mbps")
_HpnicfDot11APIfInDataRate_Type = Integer32
_HpnicfDot11APIfInDataRate_Object = MibTableColumn
hpnicfDot11APIfInDataRate = _HpnicfDot11APIfInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 7),
    _HpnicfDot11APIfInDataRate_Type()
)
hpnicfDot11APIfInDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInDataRate.setUnits("Kbps")
_HpnicfDot11APIfOutDataRate_Type = Integer32
_HpnicfDot11APIfOutDataRate_Object = MibTableColumn
hpnicfDot11APIfOutDataRate = _HpnicfDot11APIfOutDataRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 8),
    _HpnicfDot11APIfOutDataRate_Type()
)
hpnicfDot11APIfOutDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutDataRate.setUnits("Kbps")
_HpnicfDot11APIfSpeedKbps_Type = Gauge32
_HpnicfDot11APIfSpeedKbps_Object = MibTableColumn
hpnicfDot11APIfSpeedKbps = _HpnicfDot11APIfSpeedKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 9),
    _HpnicfDot11APIfSpeedKbps_Type()
)
hpnicfDot11APIfSpeedKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfSpeedKbps.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APIfSpeedKbps.setUnits("kbps")
_HpnicfDot11APIfTypeCM_Type = Integer32
_HpnicfDot11APIfTypeCM_Object = MibTableColumn
hpnicfDot11APIfTypeCM = _HpnicfDot11APIfTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 6, 1, 10),
    _HpnicfDot11APIfTypeCM_Type()
)
hpnicfDot11APIfTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfTypeCM.setStatus("current")
_HpnicfDot11APSSIDObjectTable_Object = MibTable
hpnicfDot11APSSIDObjectTable = _HpnicfDot11APSSIDObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSSIDObjectTable.setStatus("current")
_HpnicfDot11APSSIDObjectEntry_Object = MibTableRow
hpnicfDot11APSSIDObjectEntry = _HpnicfDot11APSSIDObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7, 1)
)
hpnicfDot11APSSIDObjectEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APConfigSPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSSIDObjectEntry.setStatus("current")
_HpnicfDot11APConfigSPID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11APConfigSPID_Object = MibTableColumn
hpnicfDot11APConfigSPID = _HpnicfDot11APConfigSPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7, 1, 1),
    _HpnicfDot11APConfigSPID_Type()
)
hpnicfDot11APConfigSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APConfigSPID.setStatus("current")
_HpnicfDot11APConfigSSIDName_Type = HpnicfDot11SSIDStringType
_HpnicfDot11APConfigSSIDName_Object = MibTableColumn
hpnicfDot11APConfigSSIDName = _HpnicfDot11APConfigSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7, 1, 2),
    _HpnicfDot11APConfigSSIDName_Type()
)
hpnicfDot11APConfigSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APConfigSSIDName.setStatus("current")
_HpnicfDot11APConfigBSSIDNum_Type = Integer32
_HpnicfDot11APConfigBSSIDNum_Object = MibTableColumn
hpnicfDot11APConfigBSSIDNum = _HpnicfDot11APConfigBSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7, 1, 3),
    _HpnicfDot11APConfigBSSIDNum_Type()
)
hpnicfDot11APConfigBSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APConfigBSSIDNum.setStatus("current")
_HpnicfDot11APConfigPortalStaNum_Type = Integer32
_HpnicfDot11APConfigPortalStaNum_Object = MibTableColumn
hpnicfDot11APConfigPortalStaNum = _HpnicfDot11APConfigPortalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 7, 1, 4),
    _HpnicfDot11APConfigPortalStaNum_Type()
)
hpnicfDot11APConfigPortalStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APConfigPortalStaNum.setStatus("current")
_HpnicfDot11APSysInfoTable_Object = MibTable
hpnicfDot11APSysInfoTable = _HpnicfDot11APSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoTable.setStatus("current")
_HpnicfDot11APSysInfoEntry_Object = MibTableRow
hpnicfDot11APSysInfoEntry = _HpnicfDot11APSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1)
)
hpnicfDot11APSysInfoEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoEntry.setStatus("current")
_HpnicfDot11APSysUpTime_Type = TimeTicks
_HpnicfDot11APSysUpTime_Object = MibTableColumn
hpnicfDot11APSysUpTime = _HpnicfDot11APSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 1),
    _HpnicfDot11APSysUpTime_Type()
)
hpnicfDot11APSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APSysUpTime.setStatus("current")


class _HpnicfDot11APCPURTUsage_Type(Integer32):
    """Custom type hpnicfDot11APCPURTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCPURTUsage_Type.__name__ = "Integer32"
_HpnicfDot11APCPURTUsage_Object = MibTableColumn
hpnicfDot11APCPURTUsage = _HpnicfDot11APCPURTUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 2),
    _HpnicfDot11APCPURTUsage_Type()
)
hpnicfDot11APCPURTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPURTUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCPURTUsage.setUnits("onepercent")


class _HpnicfDot11APCPUAvgUsage_Type(Integer32):
    """Custom type hpnicfDot11APCPUAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCPUAvgUsage_Type.__name__ = "Integer32"
_HpnicfDot11APCPUAvgUsage_Object = MibTableColumn
hpnicfDot11APCPUAvgUsage = _HpnicfDot11APCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 3),
    _HpnicfDot11APCPUAvgUsage_Type()
)
hpnicfDot11APCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUAvgUsage.setUnits("onepercent")


class _HpnicfDot11APMemRTUsage_Type(Integer32):
    """Custom type hpnicfDot11APMemRTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APMemRTUsage_Type.__name__ = "Integer32"
_HpnicfDot11APMemRTUsage_Object = MibTableColumn
hpnicfDot11APMemRTUsage = _HpnicfDot11APMemRTUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 4),
    _HpnicfDot11APMemRTUsage_Type()
)
hpnicfDot11APMemRTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemRTUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemRTUsage.setUnits("onepercent")


class _HpnicfDot11APMemAvgUsage_Type(Integer32):
    """Custom type hpnicfDot11APMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APMemAvgUsage_Type.__name__ = "Integer32"
_HpnicfDot11APMemAvgUsage_Object = MibTableColumn
hpnicfDot11APMemAvgUsage = _HpnicfDot11APMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 5),
    _HpnicfDot11APMemAvgUsage_Type()
)
hpnicfDot11APMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemAvgUsage.setUnits("onepercent")
_HpnicfDot11APIPAddressGateway_Type = IpAddress
_HpnicfDot11APIPAddressGateway_Object = MibTableColumn
hpnicfDot11APIPAddressGateway = _HpnicfDot11APIPAddressGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 6),
    _HpnicfDot11APIPAddressGateway_Type()
)
hpnicfDot11APIPAddressGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIPAddressGateway.setStatus("current")


class _HpnicfDot11APACAssociateStatus_Type(Integer32):
    """Custom type hpnicfDot11APACAssociateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("deassociated", 2),
          ("downloadingImage", 3))
    )


_HpnicfDot11APACAssociateStatus_Type.__name__ = "Integer32"
_HpnicfDot11APACAssociateStatus_Object = MibTableColumn
hpnicfDot11APACAssociateStatus = _HpnicfDot11APACAssociateStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 7),
    _HpnicfDot11APACAssociateStatus_Type()
)
hpnicfDot11APACAssociateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APACAssociateStatus.setStatus("current")


class _HpnicfDot11APManuBuildInfo_Type(OctetString):
    """Custom type hpnicfDot11APManuBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11APManuBuildInfo_Type.__name__ = "OctetString"
_HpnicfDot11APManuBuildInfo_Object = MibTableColumn
hpnicfDot11APManuBuildInfo = _HpnicfDot11APManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 8),
    _HpnicfDot11APManuBuildInfo_Type()
)
hpnicfDot11APManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APManuBuildInfo.setStatus("current")
_HpnicfDot11APFlashFreeSize_Type = Unsigned32
_HpnicfDot11APFlashFreeSize_Object = MibTableColumn
hpnicfDot11APFlashFreeSize = _HpnicfDot11APFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 9),
    _HpnicfDot11APFlashFreeSize_Type()
)
hpnicfDot11APFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashFreeSize.setUnits("bytes")
_HpnicfDot11APTemperature_Type = Integer32
_HpnicfDot11APTemperature_Object = MibTableColumn
hpnicfDot11APTemperature = _HpnicfDot11APTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 8, 1, 10),
    _HpnicfDot11APTemperature_Type()
)
hpnicfDot11APTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTemperature.setStatus("current")
_HpnicfDot11APIdleListTable_Object = MibTable
hpnicfDot11APIdleListTable = _HpnicfDot11APIdleListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfDot11APIdleListTable.setStatus("current")
_HpnicfDot11APIdleListEntry_Object = MibTableRow
hpnicfDot11APIdleListEntry = _HpnicfDot11APIdleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 9, 1)
)
hpnicfDot11APIdleListEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIdleTemplateName"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APIdleListEntry.setStatus("current")


class _HpnicfDot11APIdleTemplateName_Type(OctetString):
    """Custom type hpnicfDot11APIdleTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11APIdleTemplateName_Type.__name__ = "OctetString"
_HpnicfDot11APIdleTemplateName_Object = MibTableColumn
hpnicfDot11APIdleTemplateName = _HpnicfDot11APIdleTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 9, 1, 1),
    _HpnicfDot11APIdleTemplateName_Type()
)
hpnicfDot11APIdleTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APIdleTemplateName.setStatus("current")
_HpnicfDot11APIdleSerialID_Type = OctetString
_HpnicfDot11APIdleSerialID_Object = MibTableColumn
hpnicfDot11APIdleSerialID = _HpnicfDot11APIdleSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 9, 1, 2),
    _HpnicfDot11APIdleSerialID_Type()
)
hpnicfDot11APIdleSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIdleSerialID.setStatus("current")
_HpnicfDot11APSysInfoByAPIDTable_Object = MibTable
hpnicfDot11APSysInfoByAPIDTable = _HpnicfDot11APSysInfoByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoByAPIDTable.setStatus("current")
_HpnicfDot11APSysInfoByAPIDEntry_Object = MibTableRow
hpnicfDot11APSysInfoByAPIDEntry = _HpnicfDot11APSysInfoByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1)
)
hpnicfDot11APSysInfoByAPIDEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APObjID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoByAPIDEntry.setStatus("current")
_HpnicfDot11APSysUpTime2_Type = TimeTicks
_HpnicfDot11APSysUpTime2_Object = MibTableColumn
hpnicfDot11APSysUpTime2 = _HpnicfDot11APSysUpTime2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 1),
    _HpnicfDot11APSysUpTime2_Type()
)
hpnicfDot11APSysUpTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APSysUpTime2.setStatus("current")


class _HpnicfDot11APCPURTUsage2_Type(Integer32):
    """Custom type hpnicfDot11APCPURTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCPURTUsage2_Type.__name__ = "Integer32"
_HpnicfDot11APCPURTUsage2_Object = MibTableColumn
hpnicfDot11APCPURTUsage2 = _HpnicfDot11APCPURTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 2),
    _HpnicfDot11APCPURTUsage2_Type()
)
hpnicfDot11APCPURTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPURTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCPURTUsage2.setUnits("onepercent")


class _HpnicfDot11APCPUAvgUsage2_Type(Integer32):
    """Custom type hpnicfDot11APCPUAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCPUAvgUsage2_Type.__name__ = "Integer32"
_HpnicfDot11APCPUAvgUsage2_Object = MibTableColumn
hpnicfDot11APCPUAvgUsage2 = _HpnicfDot11APCPUAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 3),
    _HpnicfDot11APCPUAvgUsage2_Type()
)
hpnicfDot11APCPUAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCPUAvgUsage2.setUnits("onepercent")


class _HpnicfDot11APMemRTUsage2_Type(Integer32):
    """Custom type hpnicfDot11APMemRTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APMemRTUsage2_Type.__name__ = "Integer32"
_HpnicfDot11APMemRTUsage2_Object = MibTableColumn
hpnicfDot11APMemRTUsage2 = _HpnicfDot11APMemRTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 4),
    _HpnicfDot11APMemRTUsage2_Type()
)
hpnicfDot11APMemRTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemRTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemRTUsage2.setUnits("onepercent")


class _HpnicfDot11APMemAvgUsage2_Type(Integer32):
    """Custom type hpnicfDot11APMemAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APMemAvgUsage2_Type.__name__ = "Integer32"
_HpnicfDot11APMemAvgUsage2_Object = MibTableColumn
hpnicfDot11APMemAvgUsage2 = _HpnicfDot11APMemAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 5),
    _HpnicfDot11APMemAvgUsage2_Type()
)
hpnicfDot11APMemAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMemAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemAvgUsage2.setUnits("onepercent")
_HpnicfDot11APIPAddressGateway2_Type = IpAddress
_HpnicfDot11APIPAddressGateway2_Object = MibTableColumn
hpnicfDot11APIPAddressGateway2 = _HpnicfDot11APIPAddressGateway2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 6),
    _HpnicfDot11APIPAddressGateway2_Type()
)
hpnicfDot11APIPAddressGateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIPAddressGateway2.setStatus("current")


class _HpnicfDot11APACAssociateStatus2_Type(Integer32):
    """Custom type hpnicfDot11APACAssociateStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("deassociated", 2),
          ("downloadingImage", 3))
    )


_HpnicfDot11APACAssociateStatus2_Type.__name__ = "Integer32"
_HpnicfDot11APACAssociateStatus2_Object = MibTableColumn
hpnicfDot11APACAssociateStatus2 = _HpnicfDot11APACAssociateStatus2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 7),
    _HpnicfDot11APACAssociateStatus2_Type()
)
hpnicfDot11APACAssociateStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APACAssociateStatus2.setStatus("current")


class _HpnicfDot11APManuBuildInfo2_Type(OctetString):
    """Custom type hpnicfDot11APManuBuildInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11APManuBuildInfo2_Type.__name__ = "OctetString"
_HpnicfDot11APManuBuildInfo2_Object = MibTableColumn
hpnicfDot11APManuBuildInfo2 = _HpnicfDot11APManuBuildInfo2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 8),
    _HpnicfDot11APManuBuildInfo2_Type()
)
hpnicfDot11APManuBuildInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APManuBuildInfo2.setStatus("current")
_HpnicfDot11APFlashFreeSize2_Type = Unsigned32
_HpnicfDot11APFlashFreeSize2_Object = MibTableColumn
hpnicfDot11APFlashFreeSize2 = _HpnicfDot11APFlashFreeSize2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 9),
    _HpnicfDot11APFlashFreeSize2_Type()
)
hpnicfDot11APFlashFreeSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashFreeSize2.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APFlashFreeSize2.setUnits("bytes")
_HpnicfDot11APTemperature2_Type = Integer32
_HpnicfDot11APTemperature2_Object = MibTableColumn
hpnicfDot11APTemperature2 = _HpnicfDot11APTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 10),
    _HpnicfDot11APTemperature2_Type()
)
hpnicfDot11APTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTemperature2.setStatus("current")
_HpnicfDot11APMacAddress2_Type = MacAddress
_HpnicfDot11APMacAddress2_Object = MibTableColumn
hpnicfDot11APMacAddress2 = _HpnicfDot11APMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 11),
    _HpnicfDot11APMacAddress2_Type()
)
hpnicfDot11APMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAddress2.setStatus("current")


class _HpnicfDot11APACAssociateStatusCM_Type(Integer32):
    """Custom type hpnicfDot11APACAssociateStatusCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("associated", 1),
          ("deassociated", 0))
    )


_HpnicfDot11APACAssociateStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11APACAssociateStatusCM_Object = MibTableColumn
hpnicfDot11APACAssociateStatusCM = _HpnicfDot11APACAssociateStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 1, 10, 1, 12),
    _HpnicfDot11APACAssociateStatusCM_Type()
)
hpnicfDot11APACAssociateStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APACAssociateStatusCM.setStatus("current")
_HpnicfDot11APStatisGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11APStatisGroup = _HpnicfDot11APStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2)
)
_HpnicfDot11APRxStatisTable_Object = MibTable
hpnicfDot11APRxStatisTable = _HpnicfDot11APRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11APRxStatisTable.setStatus("current")
_HpnicfDot11APRxStatisEntry_Object = MibTableRow
hpnicfDot11APRxStatisEntry = _HpnicfDot11APRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1)
)
hpnicfDot11APRxStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APRxStatisEntry.setStatus("current")
_HpnicfDot11RxFrameDupCnt_Type = Counter32
_HpnicfDot11RxFrameDupCnt_Object = MibTableColumn
hpnicfDot11RxFrameDupCnt = _HpnicfDot11RxFrameDupCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 1),
    _HpnicfDot11RxFrameDupCnt_Type()
)
hpnicfDot11RxFrameDupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFrameDupCnt.setStatus("current")
_HpnicfDot11RxFrameCnt_Type = Counter32
_HpnicfDot11RxFrameCnt_Object = MibTableColumn
hpnicfDot11RxFrameCnt = _HpnicfDot11RxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 2),
    _HpnicfDot11RxFrameCnt_Type()
)
hpnicfDot11RxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFrameCnt.setStatus("current")
_HpnicfDot11RxUcastFrameCnt_Type = Counter32
_HpnicfDot11RxUcastFrameCnt_Object = MibTableColumn
hpnicfDot11RxUcastFrameCnt = _HpnicfDot11RxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 3),
    _HpnicfDot11RxUcastFrameCnt_Type()
)
hpnicfDot11RxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxUcastFrameCnt.setStatus("current")
_HpnicfDot11RxBcastFrameCnt_Type = Counter32
_HpnicfDot11RxBcastFrameCnt_Object = MibTableColumn
hpnicfDot11RxBcastFrameCnt = _HpnicfDot11RxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 4),
    _HpnicfDot11RxBcastFrameCnt_Type()
)
hpnicfDot11RxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxBcastFrameCnt.setStatus("current")
_HpnicfDot11RxMcastFrameCnt_Type = Counter32
_HpnicfDot11RxMcastFrameCnt_Object = MibTableColumn
hpnicfDot11RxMcastFrameCnt = _HpnicfDot11RxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 5),
    _HpnicfDot11RxMcastFrameCnt_Type()
)
hpnicfDot11RxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxMcastFrameCnt.setStatus("current")
_HpnicfDot11RxDiscardFrameCnt_Type = Counter32
_HpnicfDot11RxDiscardFrameCnt_Object = MibTableColumn
hpnicfDot11RxDiscardFrameCnt = _HpnicfDot11RxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 6),
    _HpnicfDot11RxDiscardFrameCnt_Type()
)
hpnicfDot11RxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDiscardFrameCnt.setStatus("current")
_HpnicfDot11RxFragCnt_Type = Counter32
_HpnicfDot11RxFragCnt_Object = MibTableColumn
hpnicfDot11RxFragCnt = _HpnicfDot11RxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 7),
    _HpnicfDot11RxFragCnt_Type()
)
hpnicfDot11RxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFragCnt.setStatus("current")
_HpnicfDot11RxFcsErrCnt_Type = Counter32
_HpnicfDot11RxFcsErrCnt_Object = MibTableColumn
hpnicfDot11RxFcsErrCnt = _HpnicfDot11RxFcsErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 8),
    _HpnicfDot11RxFcsErrCnt_Type()
)
hpnicfDot11RxFcsErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFcsErrCnt.setStatus("current")
_HpnicfDot11RxFrameBytes_Type = Counter32
_HpnicfDot11RxFrameBytes_Object = MibTableColumn
hpnicfDot11RxFrameBytes = _HpnicfDot11RxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 9),
    _HpnicfDot11RxFrameBytes_Type()
)
hpnicfDot11RxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFrameBytes.setStatus("current")
_HpnicfDot11RxUcastFrameBytes_Type = Counter32
_HpnicfDot11RxUcastFrameBytes_Object = MibTableColumn
hpnicfDot11RxUcastFrameBytes = _HpnicfDot11RxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 10),
    _HpnicfDot11RxUcastFrameBytes_Type()
)
hpnicfDot11RxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxUcastFrameBytes.setStatus("current")
_HpnicfDot11RxBcastFrameBytes_Type = Counter32
_HpnicfDot11RxBcastFrameBytes_Object = MibTableColumn
hpnicfDot11RxBcastFrameBytes = _HpnicfDot11RxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 11),
    _HpnicfDot11RxBcastFrameBytes_Type()
)
hpnicfDot11RxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxBcastFrameBytes.setStatus("current")
_HpnicfDot11RxMcastFrameBytes_Type = Counter32
_HpnicfDot11RxMcastFrameBytes_Object = MibTableColumn
hpnicfDot11RxMcastFrameBytes = _HpnicfDot11RxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 12),
    _HpnicfDot11RxMcastFrameBytes_Type()
)
hpnicfDot11RxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxMcastFrameBytes.setStatus("current")
_HpnicfDot11RxDiscardFrameBytes_Type = Counter32
_HpnicfDot11RxDiscardFrameBytes_Object = MibTableColumn
hpnicfDot11RxDiscardFrameBytes = _HpnicfDot11RxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 13),
    _HpnicfDot11RxDiscardFrameBytes_Type()
)
hpnicfDot11RxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDiscardFrameBytes.setStatus("current")
_HpnicfDot11RxMgmtFrameCnt_Type = Counter32
_HpnicfDot11RxMgmtFrameCnt_Object = MibTableColumn
hpnicfDot11RxMgmtFrameCnt = _HpnicfDot11RxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 14),
    _HpnicfDot11RxMgmtFrameCnt_Type()
)
hpnicfDot11RxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxMgmtFrameCnt.setStatus("current")
_HpnicfDot11RxCtrlFrameCnt_Type = Counter32
_HpnicfDot11RxCtrlFrameCnt_Object = MibTableColumn
hpnicfDot11RxCtrlFrameCnt = _HpnicfDot11RxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 15),
    _HpnicfDot11RxCtrlFrameCnt_Type()
)
hpnicfDot11RxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxCtrlFrameCnt.setStatus("current")
_HpnicfDot11RxDataFrameCnt_Type = Counter32
_HpnicfDot11RxDataFrameCnt_Object = MibTableColumn
hpnicfDot11RxDataFrameCnt = _HpnicfDot11RxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 16),
    _HpnicfDot11RxDataFrameCnt_Type()
)
hpnicfDot11RxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDataFrameCnt.setStatus("current")
_HpnicfDot11RxDecryptErrorCnt_Type = Counter32
_HpnicfDot11RxDecryptErrorCnt_Object = MibTableColumn
hpnicfDot11RxDecryptErrorCnt = _HpnicfDot11RxDecryptErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 17),
    _HpnicfDot11RxDecryptErrorCnt_Type()
)
hpnicfDot11RxDecryptErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDecryptErrorCnt.setStatus("current")
_HpnicfDot11RxAuthenFrameCnt_Type = Counter32
_HpnicfDot11RxAuthenFrameCnt_Object = MibTableColumn
hpnicfDot11RxAuthenFrameCnt = _HpnicfDot11RxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 18),
    _HpnicfDot11RxAuthenFrameCnt_Type()
)
hpnicfDot11RxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxAuthenFrameCnt.setStatus("current")
_HpnicfDot11RxAssociateFrameCnt_Type = Counter32
_HpnicfDot11RxAssociateFrameCnt_Object = MibTableColumn
hpnicfDot11RxAssociateFrameCnt = _HpnicfDot11RxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 19),
    _HpnicfDot11RxAssociateFrameCnt_Type()
)
hpnicfDot11RxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxAssociateFrameCnt.setStatus("current")
_HpnicfDot11RxFrameErrorRatio_Type = Integer32
_HpnicfDot11RxFrameErrorRatio_Object = MibTableColumn
hpnicfDot11RxFrameErrorRatio = _HpnicfDot11RxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 20),
    _HpnicfDot11RxFrameErrorRatio_Type()
)
hpnicfDot11RxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RxFrameErrorRatio.setUnits("onepercent")
_HpnicfDot11RxPhyErrorCnt_Type = Counter32
_HpnicfDot11RxPhyErrorCnt_Object = MibTableColumn
hpnicfDot11RxPhyErrorCnt = _HpnicfDot11RxPhyErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 21),
    _HpnicfDot11RxPhyErrorCnt_Type()
)
hpnicfDot11RxPhyErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxPhyErrorCnt.setStatus("current")
_HpnicfDot11RxMICErrorCnt_Type = Counter32
_HpnicfDot11RxMICErrorCnt_Object = MibTableColumn
hpnicfDot11RxMICErrorCnt = _HpnicfDot11RxMICErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 22),
    _HpnicfDot11RxMICErrorCnt_Type()
)
hpnicfDot11RxMICErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxMICErrorCnt.setStatus("current")
_HpnicfDot11RxDataFrameBytes_Type = Counter32
_HpnicfDot11RxDataFrameBytes_Object = MibTableColumn
hpnicfDot11RxDataFrameBytes = _HpnicfDot11RxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 23),
    _HpnicfDot11RxDataFrameBytes_Type()
)
hpnicfDot11RxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDataFrameBytes.setStatus("current")
_HpnicfDot11RadioRxAverSnr_Type = Integer32
_HpnicfDot11RadioRxAverSnr_Object = MibTableColumn
hpnicfDot11RadioRxAverSnr = _HpnicfDot11RadioRxAverSnr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 24),
    _HpnicfDot11RadioRxAverSnr_Type()
)
hpnicfDot11RadioRxAverSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioRxAverSnr.setStatus("current")
_HpnicfDot11RxPayloadBytes_Type = Counter32
_HpnicfDot11RxPayloadBytes_Object = MibTableColumn
hpnicfDot11RxPayloadBytes = _HpnicfDot11RxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 25),
    _HpnicfDot11RxPayloadBytes_Type()
)
hpnicfDot11RxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxPayloadBytes.setStatus("current")
_HpnicfDot11RxTrafficSpeed_Type = Integer32
_HpnicfDot11RxTrafficSpeed_Object = MibTableColumn
hpnicfDot11RxTrafficSpeed = _HpnicfDot11RxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 26),
    _HpnicfDot11RxTrafficSpeed_Type()
)
hpnicfDot11RxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RxTrafficSpeed.setUnits("byte/s")
_HpnicfDot11RxUcastDataFrameCnt_Type = Counter64
_HpnicfDot11RxUcastDataFrameCnt_Object = MibTableColumn
hpnicfDot11RxUcastDataFrameCnt = _HpnicfDot11RxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 27),
    _HpnicfDot11RxUcastDataFrameCnt_Type()
)
hpnicfDot11RxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxUcastDataFrameCnt.setStatus("current")
_HpnicfDot11RxNUcastDataFrameCnt_Type = Counter64
_HpnicfDot11RxNUcastDataFrameCnt_Object = MibTableColumn
hpnicfDot11RxNUcastDataFrameCnt = _HpnicfDot11RxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 28),
    _HpnicfDot11RxNUcastDataFrameCnt_Type()
)
hpnicfDot11RxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxNUcastDataFrameCnt.setStatus("current")
_HpnicfDot11RxTotalDiscardFrameCnt_Type = Counter64
_HpnicfDot11RxTotalDiscardFrameCnt_Object = MibTableColumn
hpnicfDot11RxTotalDiscardFrameCnt = _HpnicfDot11RxTotalDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 29),
    _HpnicfDot11RxTotalDiscardFrameCnt_Type()
)
hpnicfDot11RxTotalDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxTotalDiscardFrameCnt.setStatus("current")
_HpnicfDot11RxTotalIPCheckErrPacketCnt_Type = Counter64
_HpnicfDot11RxTotalIPCheckErrPacketCnt_Object = MibTableColumn
hpnicfDot11RxTotalIPCheckErrPacketCnt = _HpnicfDot11RxTotalIPCheckErrPacketCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 30),
    _HpnicfDot11RxTotalIPCheckErrPacketCnt_Type()
)
hpnicfDot11RxTotalIPCheckErrPacketCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxTotalIPCheckErrPacketCnt.setStatus("current")
_HpnicfDot11RxSignalStrengthPacketCntCM_Type = OctetString
_HpnicfDot11RxSignalStrengthPacketCntCM_Object = MibTableColumn
hpnicfDot11RxSignalStrengthPacketCntCM = _HpnicfDot11RxSignalStrengthPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 31),
    _HpnicfDot11RxSignalStrengthPacketCntCM_Type()
)
hpnicfDot11RxSignalStrengthPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxSignalStrengthPacketCntCM.setStatus("current")
_HpnicfDot11RxDataFrameCntCM_Type = Counter32
_HpnicfDot11RxDataFrameCntCM_Object = MibTableColumn
hpnicfDot11RxDataFrameCntCM = _HpnicfDot11RxDataFrameCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 1, 1, 32),
    _HpnicfDot11RxDataFrameCntCM_Type()
)
hpnicfDot11RxDataFrameCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RxDataFrameCntCM.setStatus("current")
_HpnicfDot11APTxStatisTable_Object = MibTable
hpnicfDot11APTxStatisTable = _HpnicfDot11APTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11APTxStatisTable.setStatus("current")
_HpnicfDot11APTxStatisEntry_Object = MibTableRow
hpnicfDot11APTxStatisEntry = _HpnicfDot11APTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1)
)
hpnicfDot11APTxStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APTxStatisEntry.setStatus("current")
_HpnicfDot11TxFragCnt_Type = Counter32
_HpnicfDot11TxFragCnt_Object = MibTableColumn
hpnicfDot11TxFragCnt = _HpnicfDot11TxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 1),
    _HpnicfDot11TxFragCnt_Type()
)
hpnicfDot11TxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxFragCnt.setStatus("current")
_HpnicfDot11FailedCnt_Type = Counter32
_HpnicfDot11FailedCnt_Object = MibTableColumn
hpnicfDot11FailedCnt = _HpnicfDot11FailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 2),
    _HpnicfDot11FailedCnt_Type()
)
hpnicfDot11FailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11FailedCnt.setStatus("current")
_HpnicfDot11RetryCnt_Type = Counter32
_HpnicfDot11RetryCnt_Object = MibTableColumn
hpnicfDot11RetryCnt = _HpnicfDot11RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 3),
    _HpnicfDot11RetryCnt_Type()
)
hpnicfDot11RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RetryCnt.setStatus("current")
_HpnicfDot11MultiRetryCnt_Type = Counter32
_HpnicfDot11MultiRetryCnt_Object = MibTableColumn
hpnicfDot11MultiRetryCnt = _HpnicfDot11MultiRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 4),
    _HpnicfDot11MultiRetryCnt_Type()
)
hpnicfDot11MultiRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MultiRetryCnt.setStatus("current")
_HpnicfDot11RtsSuccessCnt_Type = Counter32
_HpnicfDot11RtsSuccessCnt_Object = MibTableColumn
hpnicfDot11RtsSuccessCnt = _HpnicfDot11RtsSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 5),
    _HpnicfDot11RtsSuccessCnt_Type()
)
hpnicfDot11RtsSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RtsSuccessCnt.setStatus("current")
_HpnicfDot11RtsFailCnt_Type = Counter32
_HpnicfDot11RtsFailCnt_Object = MibTableColumn
hpnicfDot11RtsFailCnt = _HpnicfDot11RtsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 6),
    _HpnicfDot11RtsFailCnt_Type()
)
hpnicfDot11RtsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RtsFailCnt.setStatus("current")
_HpnicfDot11AckFailCnt_Type = Counter32
_HpnicfDot11AckFailCnt_Object = MibTableColumn
hpnicfDot11AckFailCnt = _HpnicfDot11AckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 7),
    _HpnicfDot11AckFailCnt_Type()
)
hpnicfDot11AckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AckFailCnt.setStatus("current")
_HpnicfDot11TxFrameCnt_Type = Counter32
_HpnicfDot11TxFrameCnt_Object = MibTableColumn
hpnicfDot11TxFrameCnt = _HpnicfDot11TxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 8),
    _HpnicfDot11TxFrameCnt_Type()
)
hpnicfDot11TxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxFrameCnt.setStatus("current")
_HpnicfDot11TxUcastFrameCnt_Type = Counter32
_HpnicfDot11TxUcastFrameCnt_Object = MibTableColumn
hpnicfDot11TxUcastFrameCnt = _HpnicfDot11TxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 9),
    _HpnicfDot11TxUcastFrameCnt_Type()
)
hpnicfDot11TxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxUcastFrameCnt.setStatus("current")
_HpnicfDot11TxBcastFrameCnt_Type = Counter32
_HpnicfDot11TxBcastFrameCnt_Object = MibTableColumn
hpnicfDot11TxBcastFrameCnt = _HpnicfDot11TxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 10),
    _HpnicfDot11TxBcastFrameCnt_Type()
)
hpnicfDot11TxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxBcastFrameCnt.setStatus("current")
_HpnicfDot11TxMcastFrameCnt_Type = Counter32
_HpnicfDot11TxMcastFrameCnt_Object = MibTableColumn
hpnicfDot11TxMcastFrameCnt = _HpnicfDot11TxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 11),
    _HpnicfDot11TxMcastFrameCnt_Type()
)
hpnicfDot11TxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxMcastFrameCnt.setStatus("current")
_HpnicfDot11TxDiscardFrameCnt_Type = Counter32
_HpnicfDot11TxDiscardFrameCnt_Object = MibTableColumn
hpnicfDot11TxDiscardFrameCnt = _HpnicfDot11TxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 12),
    _HpnicfDot11TxDiscardFrameCnt_Type()
)
hpnicfDot11TxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxDiscardFrameCnt.setStatus("current")
_HpnicfDot11TxFrameBytes_Type = Counter32
_HpnicfDot11TxFrameBytes_Object = MibTableColumn
hpnicfDot11TxFrameBytes = _HpnicfDot11TxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 13),
    _HpnicfDot11TxFrameBytes_Type()
)
hpnicfDot11TxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxFrameBytes.setStatus("current")
_HpnicfDot11TxUcastFrameBytes_Type = Counter32
_HpnicfDot11TxUcastFrameBytes_Object = MibTableColumn
hpnicfDot11TxUcastFrameBytes = _HpnicfDot11TxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 14),
    _HpnicfDot11TxUcastFrameBytes_Type()
)
hpnicfDot11TxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxUcastFrameBytes.setStatus("current")
_HpnicfDot11TxBcastFrameBytes_Type = Counter32
_HpnicfDot11TxBcastFrameBytes_Object = MibTableColumn
hpnicfDot11TxBcastFrameBytes = _HpnicfDot11TxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 15),
    _HpnicfDot11TxBcastFrameBytes_Type()
)
hpnicfDot11TxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxBcastFrameBytes.setStatus("current")
_HpnicfDot11TxMcastFrameBytes_Type = Counter32
_HpnicfDot11TxMcastFrameBytes_Object = MibTableColumn
hpnicfDot11TxMcastFrameBytes = _HpnicfDot11TxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 16),
    _HpnicfDot11TxMcastFrameBytes_Type()
)
hpnicfDot11TxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxMcastFrameBytes.setStatus("current")
_HpnicfDot11TxDiscardFrameBytes_Type = Counter32
_HpnicfDot11TxDiscardFrameBytes_Object = MibTableColumn
hpnicfDot11TxDiscardFrameBytes = _HpnicfDot11TxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 17),
    _HpnicfDot11TxDiscardFrameBytes_Type()
)
hpnicfDot11TxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxDiscardFrameBytes.setStatus("current")
_HpnicfDot11TxAuthenFrameCnt_Type = Counter32
_HpnicfDot11TxAuthenFrameCnt_Object = MibTableColumn
hpnicfDot11TxAuthenFrameCnt = _HpnicfDot11TxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 18),
    _HpnicfDot11TxAuthenFrameCnt_Type()
)
hpnicfDot11TxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxAuthenFrameCnt.setStatus("current")
_HpnicfDot11TxAssociateFrameCnt_Type = Counter32
_HpnicfDot11TxAssociateFrameCnt_Object = MibTableColumn
hpnicfDot11TxAssociateFrameCnt = _HpnicfDot11TxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 19),
    _HpnicfDot11TxAssociateFrameCnt_Type()
)
hpnicfDot11TxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxAssociateFrameCnt.setStatus("current")
_HpnicfDot11TxFrameRetryRatio_Type = Integer32
_HpnicfDot11TxFrameRetryRatio_Object = MibTableColumn
hpnicfDot11TxFrameRetryRatio = _HpnicfDot11TxFrameRetryRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 20),
    _HpnicfDot11TxFrameRetryRatio_Type()
)
hpnicfDot11TxFrameRetryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxFrameRetryRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11TxFrameRetryRatio.setUnits("onepercent")
_HpnicfDot11TxDataFrameCnt_Type = Counter32
_HpnicfDot11TxDataFrameCnt_Object = MibTableColumn
hpnicfDot11TxDataFrameCnt = _HpnicfDot11TxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 21),
    _HpnicfDot11TxDataFrameCnt_Type()
)
hpnicfDot11TxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxDataFrameCnt.setStatus("current")
_HpnicfDot11TxDataFrameBytes_Type = Counter32
_HpnicfDot11TxDataFrameBytes_Object = MibTableColumn
hpnicfDot11TxDataFrameBytes = _HpnicfDot11TxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 22),
    _HpnicfDot11TxDataFrameBytes_Type()
)
hpnicfDot11TxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxDataFrameBytes.setStatus("current")
_HpnicfDot11TxMSDUCnt_Type = Counter32
_HpnicfDot11TxMSDUCnt_Object = MibTableColumn
hpnicfDot11TxMSDUCnt = _HpnicfDot11TxMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 23),
    _HpnicfDot11TxMSDUCnt_Type()
)
hpnicfDot11TxMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxMSDUCnt.setStatus("current")
_HpnicfDot11TxDiscardMSDUCnt_Type = Counter32
_HpnicfDot11TxDiscardMSDUCnt_Object = MibTableColumn
hpnicfDot11TxDiscardMSDUCnt = _HpnicfDot11TxDiscardMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 24),
    _HpnicfDot11TxDiscardMSDUCnt_Type()
)
hpnicfDot11TxDiscardMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxDiscardMSDUCnt.setStatus("current")
_HpnicfDot11RetryMSDUCnt_Type = Counter32
_HpnicfDot11RetryMSDUCnt_Object = MibTableColumn
hpnicfDot11RetryMSDUCnt = _HpnicfDot11RetryMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 25),
    _HpnicfDot11RetryMSDUCnt_Type()
)
hpnicfDot11RetryMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RetryMSDUCnt.setStatus("current")
_HpnicfDot11TxPayloadBytes_Type = Counter32
_HpnicfDot11TxPayloadBytes_Object = MibTableColumn
hpnicfDot11TxPayloadBytes = _HpnicfDot11TxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 26),
    _HpnicfDot11TxPayloadBytes_Type()
)
hpnicfDot11TxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxPayloadBytes.setStatus("current")
_HpnicfDot11TxTrafficSpeed_Type = Integer32
_HpnicfDot11TxTrafficSpeed_Object = MibTableColumn
hpnicfDot11TxTrafficSpeed = _HpnicfDot11TxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 27),
    _HpnicfDot11TxTrafficSpeed_Type()
)
hpnicfDot11TxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11TxTrafficSpeed.setUnits("byte/s")
_HpnicfDot11TxErrFrameRatio_Type = Integer32
_HpnicfDot11TxErrFrameRatio_Object = MibTableColumn
hpnicfDot11TxErrFrameRatio = _HpnicfDot11TxErrFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 28),
    _HpnicfDot11TxErrFrameRatio_Type()
)
hpnicfDot11TxErrFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxErrFrameRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11TxErrFrameRatio.setUnits("onepercent")
_HpnicfDot11TxFrameRate_Type = Integer32
_HpnicfDot11TxFrameRate_Object = MibTableColumn
hpnicfDot11TxFrameRate = _HpnicfDot11TxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 29),
    _HpnicfDot11TxFrameRate_Type()
)
hpnicfDot11TxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxFrameRate.setStatus("current")
_HpnicfDot11TxMgtFrameCnt_Type = Counter32
_HpnicfDot11TxMgtFrameCnt_Object = MibTableColumn
hpnicfDot11TxMgtFrameCnt = _HpnicfDot11TxMgtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 30),
    _HpnicfDot11TxMgtFrameCnt_Type()
)
hpnicfDot11TxMgtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxMgtFrameCnt.setStatus("current")
_HpnicfDot11TxCtrlFrameCnt_Type = Counter32
_HpnicfDot11TxCtrlFrameCnt_Object = MibTableColumn
hpnicfDot11TxCtrlFrameCnt = _HpnicfDot11TxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 31),
    _HpnicfDot11TxCtrlFrameCnt_Type()
)
hpnicfDot11TxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxCtrlFrameCnt.setStatus("current")
_HpnicfDot11TxMACErrCnt_Type = Counter32
_HpnicfDot11TxMACErrCnt_Object = MibTableColumn
hpnicfDot11TxMACErrCnt = _HpnicfDot11TxMACErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 32),
    _HpnicfDot11TxMACErrCnt_Type()
)
hpnicfDot11TxMACErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxMACErrCnt.setStatus("current")
_HpnicfDot11TxErrFrameCnt_Type = Counter32
_HpnicfDot11TxErrFrameCnt_Object = MibTableColumn
hpnicfDot11TxErrFrameCnt = _HpnicfDot11TxErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 33),
    _HpnicfDot11TxErrFrameCnt_Type()
)
hpnicfDot11TxErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxErrFrameCnt.setStatus("current")
_HpnicfDot11TxUcastDataFrameCnt_Type = Counter64
_HpnicfDot11TxUcastDataFrameCnt_Object = MibTableColumn
hpnicfDot11TxUcastDataFrameCnt = _HpnicfDot11TxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 34),
    _HpnicfDot11TxUcastDataFrameCnt_Type()
)
hpnicfDot11TxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxUcastDataFrameCnt.setStatus("current")
_HpnicfDot11TxNUcastDataFrameCnt_Type = Counter64
_HpnicfDot11TxNUcastDataFrameCnt_Object = MibTableColumn
hpnicfDot11TxNUcastDataFrameCnt = _HpnicfDot11TxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 2, 1, 35),
    _HpnicfDot11TxNUcastDataFrameCnt_Type()
)
hpnicfDot11TxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11TxNUcastDataFrameCnt.setStatus("current")
_HpnicfDot11APAssocStatisTable_Object = MibTable
hpnicfDot11APAssocStatisTable = _HpnicfDot11APAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocStatisTable.setStatus("current")
_HpnicfDot11APAssocStatisEntry_Object = MibTableRow
hpnicfDot11APAssocStatisEntry = _HpnicfDot11APAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1)
)
hpnicfDot11APAssocStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocStatisEntry.setStatus("current")
_HpnicfDot11ApStationAssocSum_Type = Counter32
_HpnicfDot11ApStationAssocSum_Object = MibTableColumn
hpnicfDot11ApStationAssocSum = _HpnicfDot11ApStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 1),
    _HpnicfDot11ApStationAssocSum_Type()
)
hpnicfDot11ApStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationAssocSum.setStatus("current")
_HpnicfDot11ApStationAssocFailSum_Type = Counter32
_HpnicfDot11ApStationAssocFailSum_Object = MibTableColumn
hpnicfDot11ApStationAssocFailSum = _HpnicfDot11ApStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 2),
    _HpnicfDot11ApStationAssocFailSum_Type()
)
hpnicfDot11ApStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationAssocFailSum.setStatus("current")
_HpnicfDot11ApStationReassocSum_Type = Counter32
_HpnicfDot11ApStationReassocSum_Object = MibTableColumn
hpnicfDot11ApStationReassocSum = _HpnicfDot11ApStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 3),
    _HpnicfDot11ApStationReassocSum_Type()
)
hpnicfDot11ApStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationReassocSum.setStatus("current")
_HpnicfDot11ApStationAssocRejectSum_Type = Counter32
_HpnicfDot11ApStationAssocRejectSum_Object = MibTableColumn
hpnicfDot11ApStationAssocRejectSum = _HpnicfDot11ApStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 4),
    _HpnicfDot11ApStationAssocRejectSum_Type()
)
hpnicfDot11ApStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationAssocRejectSum.setStatus("current")
_HpnicfDot11ApStationExDeAuthenSum_Type = Counter32
_HpnicfDot11ApStationExDeAuthenSum_Object = MibTableColumn
hpnicfDot11ApStationExDeAuthenSum = _HpnicfDot11ApStationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 5),
    _HpnicfDot11ApStationExDeAuthenSum_Type()
)
hpnicfDot11ApStationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationExDeAuthenSum.setStatus("current")
_HpnicfDot11ApStationCurAssocSum_Type = Integer32
_HpnicfDot11ApStationCurAssocSum_Object = MibTableColumn
hpnicfDot11ApStationCurAssocSum = _HpnicfDot11ApStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 6),
    _HpnicfDot11ApStationCurAssocSum_Type()
)
hpnicfDot11ApStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationCurAssocSum.setStatus("current")
_HpnicfDot11ApStaCurAuthSuccSum_Type = Integer32
_HpnicfDot11ApStaCurAuthSuccSum_Object = MibTableColumn
hpnicfDot11ApStaCurAuthSuccSum = _HpnicfDot11ApStaCurAuthSuccSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 7),
    _HpnicfDot11ApStaCurAuthSuccSum_Type()
)
hpnicfDot11ApStaCurAuthSuccSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStaCurAuthSuccSum.setStatus("current")
_HpnicfDot11AllStationUpSumTime_Type = Counter32
_HpnicfDot11AllStationUpSumTime_Object = MibTableColumn
hpnicfDot11AllStationUpSumTime = _HpnicfDot11AllStationUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 8),
    _HpnicfDot11AllStationUpSumTime_Type()
)
hpnicfDot11AllStationUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AllStationUpSumTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AllStationUpSumTime.setUnits("minute")
_HpnicfDot11ApStationAssocReqSum_Type = Counter32
_HpnicfDot11ApStationAssocReqSum_Object = MibTableColumn
hpnicfDot11ApStationAssocReqSum = _HpnicfDot11ApStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 9),
    _HpnicfDot11ApStationAssocReqSum_Type()
)
hpnicfDot11ApStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationAssocReqSum.setStatus("current")
_HpnicfDot11AllStationUpSumTimeTicks_Type = TimeTicks
_HpnicfDot11AllStationUpSumTimeTicks_Object = MibTableColumn
hpnicfDot11AllStationUpSumTimeTicks = _HpnicfDot11AllStationUpSumTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 10),
    _HpnicfDot11AllStationUpSumTimeTicks_Type()
)
hpnicfDot11AllStationUpSumTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AllStationUpSumTimeTicks.setStatus("current")
_HpnicfDot11ApStationReassocReqSum_Type = Counter32
_HpnicfDot11ApStationReassocReqSum_Object = MibTableColumn
hpnicfDot11ApStationReassocReqSum = _HpnicfDot11ApStationReassocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 11),
    _HpnicfDot11ApStationReassocReqSum_Type()
)
hpnicfDot11ApStationReassocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationReassocReqSum.setStatus("current")
_HpnicfDot11ApStationReassocFailSum_Type = Counter32
_HpnicfDot11ApStationReassocFailSum_Object = MibTableColumn
hpnicfDot11ApStationReassocFailSum = _HpnicfDot11ApStationReassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 3, 1, 12),
    _HpnicfDot11ApStationReassocFailSum_Type()
)
hpnicfDot11ApStationReassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11ApStationReassocFailSum.setStatus("current")
_HpnicfDot11BSSRxStatisTable_Object = MibTable
hpnicfDot11BSSRxStatisTable = _HpnicfDot11BSSRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxStatisTable.setStatus("current")
_HpnicfDot11BSSRxStatisEntry_Object = MibTableRow
hpnicfDot11BSSRxStatisEntry = _HpnicfDot11BSSRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1)
)
hpnicfDot11BSSRxStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxStatisEntry.setStatus("current")
_HpnicfDot11BSSRxFrameCnt_Type = Counter32
_HpnicfDot11BSSRxFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxFrameCnt = _HpnicfDot11BSSRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 1),
    _HpnicfDot11BSSRxFrameCnt_Type()
)
hpnicfDot11BSSRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxFrameCnt.setStatus("current")
_HpnicfDot11BSSRxFrameBytes_Type = Counter32
_HpnicfDot11BSSRxFrameBytes_Object = MibTableColumn
hpnicfDot11BSSRxFrameBytes = _HpnicfDot11BSSRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 2),
    _HpnicfDot11BSSRxFrameBytes_Type()
)
hpnicfDot11BSSRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxFrameBytes.setStatus("current")
_HpnicfDot11BSSRxDataFrameCnt_Type = Counter32
_HpnicfDot11BSSRxDataFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxDataFrameCnt = _HpnicfDot11BSSRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 3),
    _HpnicfDot11BSSRxDataFrameCnt_Type()
)
hpnicfDot11BSSRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxDataFrameCnt.setStatus("current")
_HpnicfDot11BSSRxDataFrameBytes_Type = Counter32
_HpnicfDot11BSSRxDataFrameBytes_Object = MibTableColumn
hpnicfDot11BSSRxDataFrameBytes = _HpnicfDot11BSSRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 4),
    _HpnicfDot11BSSRxDataFrameBytes_Type()
)
hpnicfDot11BSSRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxDataFrameBytes.setStatus("current")
_HpnicfDot11BSSRxAssociateFrameCnt_Type = Counter32
_HpnicfDot11BSSRxAssociateFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxAssociateFrameCnt = _HpnicfDot11BSSRxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 5),
    _HpnicfDot11BSSRxAssociateFrameCnt_Type()
)
hpnicfDot11BSSRxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxAssociateFrameCnt.setStatus("current")
_HpnicfDot11BSSRxFrameErrorRatio_Type = Integer32
_HpnicfDot11BSSRxFrameErrorRatio_Object = MibTableColumn
hpnicfDot11BSSRxFrameErrorRatio = _HpnicfDot11BSSRxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 6),
    _HpnicfDot11BSSRxFrameErrorRatio_Type()
)
hpnicfDot11BSSRxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxFrameErrorRatio.setUnits("percent")
_HpnicfDot11BSSRxPayloadBytes_Type = Counter32
_HpnicfDot11BSSRxPayloadBytes_Object = MibTableColumn
hpnicfDot11BSSRxPayloadBytes = _HpnicfDot11BSSRxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 7),
    _HpnicfDot11BSSRxPayloadBytes_Type()
)
hpnicfDot11BSSRxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxPayloadBytes.setStatus("current")
_HpnicfDot11BSSRxUniFrameCnt_Type = Counter32
_HpnicfDot11BSSRxUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxUniFrameCnt = _HpnicfDot11BSSRxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 8),
    _HpnicfDot11BSSRxUniFrameCnt_Type()
)
hpnicfDot11BSSRxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxUniFrameCnt.setStatus("current")
_HpnicfDot11BSSRxNonUniFrameCnt_Type = Integer32
_HpnicfDot11BSSRxNonUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxNonUniFrameCnt = _HpnicfDot11BSSRxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 9),
    _HpnicfDot11BSSRxNonUniFrameCnt_Type()
)
hpnicfDot11BSSRxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxNonUniFrameCnt.setStatus("current")
_HpnicfDot11BSSRxAuthenFrameCnt_Type = Counter32
_HpnicfDot11BSSRxAuthenFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRxAuthenFrameCnt = _HpnicfDot11BSSRxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 4, 1, 10),
    _HpnicfDot11BSSRxAuthenFrameCnt_Type()
)
hpnicfDot11BSSRxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxAuthenFrameCnt.setStatus("current")
_HpnicfDot11BSSTxStatisTable_Object = MibTable
hpnicfDot11BSSTxStatisTable = _HpnicfDot11BSSTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxStatisTable.setStatus("current")
_HpnicfDot11BSSTxStatisEntry_Object = MibTableRow
hpnicfDot11BSSTxStatisEntry = _HpnicfDot11BSSTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1)
)
hpnicfDot11BSSTxStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxStatisEntry.setStatus("current")
_HpnicfDot11BSSTxFrameCnt_Type = Counter32
_HpnicfDot11BSSTxFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxFrameCnt = _HpnicfDot11BSSTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 1),
    _HpnicfDot11BSSTxFrameCnt_Type()
)
hpnicfDot11BSSTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxFrameCnt.setStatus("current")
_HpnicfDot11BSSTxFrameBytes_Type = Counter32
_HpnicfDot11BSSTxFrameBytes_Object = MibTableColumn
hpnicfDot11BSSTxFrameBytes = _HpnicfDot11BSSTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 2),
    _HpnicfDot11BSSTxFrameBytes_Type()
)
hpnicfDot11BSSTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxFrameBytes.setStatus("current")
_HpnicfDot11BSSTxDataFrameCnt_Type = Counter32
_HpnicfDot11BSSTxDataFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxDataFrameCnt = _HpnicfDot11BSSTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 3),
    _HpnicfDot11BSSTxDataFrameCnt_Type()
)
hpnicfDot11BSSTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxDataFrameCnt.setStatus("current")
_HpnicfDot11BSSTxDataFrameBytes_Type = Counter32
_HpnicfDot11BSSTxDataFrameBytes_Object = MibTableColumn
hpnicfDot11BSSTxDataFrameBytes = _HpnicfDot11BSSTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 4),
    _HpnicfDot11BSSTxDataFrameBytes_Type()
)
hpnicfDot11BSSTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxDataFrameBytes.setStatus("current")
_HpnicfDot11BSSTxAssociateFrameCnt_Type = Counter32
_HpnicfDot11BSSTxAssociateFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxAssociateFrameCnt = _HpnicfDot11BSSTxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 5),
    _HpnicfDot11BSSTxAssociateFrameCnt_Type()
)
hpnicfDot11BSSTxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxAssociateFrameCnt.setStatus("current")
_HpnicfDot11BSSTxPayloadBytes_Type = Counter32
_HpnicfDot11BSSTxPayloadBytes_Object = MibTableColumn
hpnicfDot11BSSTxPayloadBytes = _HpnicfDot11BSSTxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 6),
    _HpnicfDot11BSSTxPayloadBytes_Type()
)
hpnicfDot11BSSTxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxPayloadBytes.setStatus("current")
_HpnicfDot11BSSTxRetryCnt_Type = Counter32
_HpnicfDot11BSSTxRetryCnt_Object = MibTableColumn
hpnicfDot11BSSTxRetryCnt = _HpnicfDot11BSSTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 7),
    _HpnicfDot11BSSTxRetryCnt_Type()
)
hpnicfDot11BSSTxRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxRetryCnt.setStatus("current")
_HpnicfDot11BSSTxUniFrameCnt_Type = Counter32
_HpnicfDot11BSSTxUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxUniFrameCnt = _HpnicfDot11BSSTxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 8),
    _HpnicfDot11BSSTxUniFrameCnt_Type()
)
hpnicfDot11BSSTxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxUniFrameCnt.setStatus("current")
_HpnicfDot11BSSTxNonUniFrameCnt_Type = Integer32
_HpnicfDot11BSSTxNonUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxNonUniFrameCnt = _HpnicfDot11BSSTxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 9),
    _HpnicfDot11BSSTxNonUniFrameCnt_Type()
)
hpnicfDot11BSSTxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxNonUniFrameCnt.setStatus("current")
_HpnicfDot11BSSTxAuthenFrameCnt_Type = Counter32
_HpnicfDot11BSSTxAuthenFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTxAuthenFrameCnt = _HpnicfDot11BSSTxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 5, 1, 10),
    _HpnicfDot11BSSTxAuthenFrameCnt_Type()
)
hpnicfDot11BSSTxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxAuthenFrameCnt.setStatus("current")
_HpnicfDot11BSSAssocStatisTable_Object = MibTable
hpnicfDot11BSSAssocStatisTable = _HpnicfDot11BSSAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSAssocStatisTable.setStatus("current")
_HpnicfDot11BSSAssocStatisEntry_Object = MibTableRow
hpnicfDot11BSSAssocStatisEntry = _HpnicfDot11BSSAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1)
)
hpnicfDot11BSSAssocStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSAssocStatisEntry.setStatus("current")
_HpnicfDot11BSSStationAssocSum_Type = Counter32
_HpnicfDot11BSSStationAssocSum_Object = MibTableColumn
hpnicfDot11BSSStationAssocSum = _HpnicfDot11BSSStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 1),
    _HpnicfDot11BSSStationAssocSum_Type()
)
hpnicfDot11BSSStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationAssocSum.setStatus("current")
_HpnicfDot11BSSStationAssocFailSum_Type = Counter32
_HpnicfDot11BSSStationAssocFailSum_Object = MibTableColumn
hpnicfDot11BSSStationAssocFailSum = _HpnicfDot11BSSStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 2),
    _HpnicfDot11BSSStationAssocFailSum_Type()
)
hpnicfDot11BSSStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationAssocFailSum.setStatus("current")
_HpnicfDot11BSSStationReassocSum_Type = Counter32
_HpnicfDot11BSSStationReassocSum_Object = MibTableColumn
hpnicfDot11BSSStationReassocSum = _HpnicfDot11BSSStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 3),
    _HpnicfDot11BSSStationReassocSum_Type()
)
hpnicfDot11BSSStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationReassocSum.setStatus("current")
_HpnicfDot11BSSStationAssocRejectSum_Type = Counter32
_HpnicfDot11BSSStationAssocRejectSum_Object = MibTableColumn
hpnicfDot11BSSStationAssocRejectSum = _HpnicfDot11BSSStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 4),
    _HpnicfDot11BSSStationAssocRejectSum_Type()
)
hpnicfDot11BSSStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationAssocRejectSum.setStatus("current")
_HpnicfDot11BSSStationExDeAssocSum_Type = Counter32
_HpnicfDot11BSSStationExDeAssocSum_Object = MibTableColumn
hpnicfDot11BSSStationExDeAssocSum = _HpnicfDot11BSSStationExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 5),
    _HpnicfDot11BSSStationExDeAssocSum_Type()
)
hpnicfDot11BSSStationExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationExDeAssocSum.setStatus("current")
_HpnicfDot11BSSStationCurAssocSum_Type = Integer32
_HpnicfDot11BSSStationCurAssocSum_Object = MibTableColumn
hpnicfDot11BSSStationCurAssocSum = _HpnicfDot11BSSStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 6),
    _HpnicfDot11BSSStationCurAssocSum_Type()
)
hpnicfDot11BSSStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationCurAssocSum.setStatus("current")
_HpnicfDot11BSSStationAssocReqSum_Type = Counter32
_HpnicfDot11BSSStationAssocReqSum_Object = MibTableColumn
hpnicfDot11BSSStationAssocReqSum = _HpnicfDot11BSSStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 7),
    _HpnicfDot11BSSStationAssocReqSum_Type()
)
hpnicfDot11BSSStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationAssocReqSum.setStatus("current")
_HpnicfDot11BSSStationCurAuthSum_Type = Integer32
_HpnicfDot11BSSStationCurAuthSum_Object = MibTableColumn
hpnicfDot11BSSStationCurAuthSum = _HpnicfDot11BSSStationCurAuthSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 6, 1, 8),
    _HpnicfDot11BSSStationCurAuthSum_Type()
)
hpnicfDot11BSSStationCurAuthSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSStationCurAuthSum.setStatus("current")
_HpnicfDot11APLinkStatisTable_Object = MibTable
hpnicfDot11APLinkStatisTable = _HpnicfDot11APLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11APLinkStatisTable.setStatus("current")
_HpnicfDot11APLinkStatisEntry_Object = MibTableRow
hpnicfDot11APLinkStatisEntry = _HpnicfDot11APLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 7, 1)
)
hpnicfDot11APLinkStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APLinkStatisEntry.setStatus("current")
_HpnicfDot11UpLinkUpDownTimes_Type = Counter32
_HpnicfDot11UpLinkUpDownTimes_Object = MibTableColumn
hpnicfDot11UpLinkUpDownTimes = _HpnicfDot11UpLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 7, 1, 1),
    _HpnicfDot11UpLinkUpDownTimes_Type()
)
hpnicfDot11UpLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11UpLinkUpDownTimes.setStatus("current")
_HpnicfDot11DownLinkUpDownTimes_Type = Counter32
_HpnicfDot11DownLinkUpDownTimes_Object = MibTableColumn
hpnicfDot11DownLinkUpDownTimes = _HpnicfDot11DownLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 7, 1, 2),
    _HpnicfDot11DownLinkUpDownTimes_Type()
)
hpnicfDot11DownLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DownLinkUpDownTimes.setStatus("current")
_HpnicfDot11RadioAssocStatisTable_Object = MibTable
hpnicfDot11RadioAssocStatisTable = _HpnicfDot11RadioAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioAssocStatisTable.setStatus("current")
_HpnicfDot11RadioAssocStatisEntry_Object = MibTableRow
hpnicfDot11RadioAssocStatisEntry = _HpnicfDot11RadioAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1)
)
hpnicfDot11RadioAssocStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioAssocStatisEntry.setStatus("current")
_HpnicfDot11RadioStaAssocSum_Type = Counter32
_HpnicfDot11RadioStaAssocSum_Object = MibTableColumn
hpnicfDot11RadioStaAssocSum = _HpnicfDot11RadioStaAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 1),
    _HpnicfDot11RadioStaAssocSum_Type()
)
hpnicfDot11RadioStaAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaAssocSum.setStatus("current")
_HpnicfDot11RadioStaAssocFailSum_Type = Counter32
_HpnicfDot11RadioStaAssocFailSum_Object = MibTableColumn
hpnicfDot11RadioStaAssocFailSum = _HpnicfDot11RadioStaAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 2),
    _HpnicfDot11RadioStaAssocFailSum_Type()
)
hpnicfDot11RadioStaAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaAssocFailSum.setStatus("current")
_HpnicfDot11RadioStaReassocSum_Type = Counter32
_HpnicfDot11RadioStaReassocSum_Object = MibTableColumn
hpnicfDot11RadioStaReassocSum = _HpnicfDot11RadioStaReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 3),
    _HpnicfDot11RadioStaReassocSum_Type()
)
hpnicfDot11RadioStaReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaReassocSum.setStatus("current")
_HpnicfDot11RadioStaAssocRejectSum_Type = Counter32
_HpnicfDot11RadioStaAssocRejectSum_Object = MibTableColumn
hpnicfDot11RadioStaAssocRejectSum = _HpnicfDot11RadioStaAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 4),
    _HpnicfDot11RadioStaAssocRejectSum_Type()
)
hpnicfDot11RadioStaAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaAssocRejectSum.setStatus("current")
_HpnicfDot11RadioStaExDeAssocSum_Type = Counter32
_HpnicfDot11RadioStaExDeAssocSum_Object = MibTableColumn
hpnicfDot11RadioStaExDeAssocSum = _HpnicfDot11RadioStaExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 5),
    _HpnicfDot11RadioStaExDeAssocSum_Type()
)
hpnicfDot11RadioStaExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaExDeAssocSum.setStatus("current")
_HpnicfDot11RadioStaCurAssocSum_Type = Integer32
_HpnicfDot11RadioStaCurAssocSum_Object = MibTableColumn
hpnicfDot11RadioStaCurAssocSum = _HpnicfDot11RadioStaCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 8, 1, 6),
    _HpnicfDot11RadioStaCurAssocSum_Type()
)
hpnicfDot11RadioStaCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStaCurAssocSum.setStatus("current")
_HpnicfDot11RadioMngFrameStatisTable_Object = MibTable
hpnicfDot11RadioMngFrameStatisTable = _HpnicfDot11RadioMngFrameStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioMngFrameStatisTable.setStatus("current")
_HpnicfDot11RadioMngFrameStatisEntry_Object = MibTableRow
hpnicfDot11RadioMngFrameStatisEntry = _HpnicfDot11RadioMngFrameStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 9, 1)
)
hpnicfDot11RadioMngFrameStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioStatisIndex"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11MngFrameType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioMngFrameStatisEntry.setStatus("current")
_HpnicfDot11RadioStatisIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11RadioStatisIndex_Object = MibTableColumn
hpnicfDot11RadioStatisIndex = _HpnicfDot11RadioStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 9, 1, 1),
    _HpnicfDot11RadioStatisIndex_Type()
)
hpnicfDot11RadioStatisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioStatisIndex.setStatus("current")


class _HpnicfDot11MngFrameType_Type(Integer32):
    """Custom type hpnicfDot11MngFrameType based on Integer32"""
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
        *(("action", 12),
          ("assocReq", 1),
          ("assocResp", 2),
          ("atim", 8),
          ("authentication", 10),
          ("beacon", 7),
          ("deauthentication", 11),
          ("disassociation", 9),
          ("probeReq", 5),
          ("probeResp", 6),
          ("reassocReq", 3),
          ("reassocResp", 4))
    )


_HpnicfDot11MngFrameType_Type.__name__ = "Integer32"
_HpnicfDot11MngFrameType_Object = MibTableColumn
hpnicfDot11MngFrameType = _HpnicfDot11MngFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 9, 1, 2),
    _HpnicfDot11MngFrameType_Type()
)
hpnicfDot11MngFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11MngFrameType.setStatus("current")
_HpnicfDot11MngFrameCnt_Type = Counter32
_HpnicfDot11MngFrameCnt_Object = MibTableColumn
hpnicfDot11MngFrameCnt = _HpnicfDot11MngFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 9, 1, 3),
    _HpnicfDot11MngFrameCnt_Type()
)
hpnicfDot11MngFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MngFrameCnt.setStatus("current")
_HpnicfDot11APAuthFailStatisTable_Object = MibTable
hpnicfDot11APAuthFailStatisTable = _HpnicfDot11APAuthFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFailStatisTable.setStatus("current")
_HpnicfDot11APAuthFailStatisEntry_Object = MibTableRow
hpnicfDot11APAuthFailStatisEntry = _HpnicfDot11APAuthFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 10, 1)
)
hpnicfDot11APAuthFailStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APAuthFailStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFailStatisEntry.setStatus("current")


class _HpnicfDot11APAuthFailStatisType_Type(Integer32):
    """Custom type hpnicfDot11APAuthFailStatisType based on Integer32"""
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
        *(("invalidation", 1),
          ("other", 4),
          ("overtime", 2),
          ("rejected", 3))
    )


_HpnicfDot11APAuthFailStatisType_Type.__name__ = "Integer32"
_HpnicfDot11APAuthFailStatisType_Object = MibTableColumn
hpnicfDot11APAuthFailStatisType = _HpnicfDot11APAuthFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 10, 1, 1),
    _HpnicfDot11APAuthFailStatisType_Type()
)
hpnicfDot11APAuthFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFailStatisType.setStatus("current")
_HpnicfDot11APAuthFailStatisCnt_Type = Counter32
_HpnicfDot11APAuthFailStatisCnt_Object = MibTableColumn
hpnicfDot11APAuthFailStatisCnt = _HpnicfDot11APAuthFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 10, 1, 2),
    _HpnicfDot11APAuthFailStatisCnt_Type()
)
hpnicfDot11APAuthFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFailStatisCnt.setStatus("current")
_HpnicfDot11APAssocFailStatisTable_Object = MibTable
hpnicfDot11APAssocFailStatisTable = _HpnicfDot11APAssocFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatisTable.setStatus("current")
_HpnicfDot11APAssocFailStatisEntry_Object = MibTableRow
hpnicfDot11APAssocFailStatisEntry = _HpnicfDot11APAssocFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 11, 1)
)
hpnicfDot11APAssocFailStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APAssocFailStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatisEntry.setStatus("current")


class _HpnicfDot11APAssocFailStatisType_Type(Integer32):
    """Custom type hpnicfDot11APAssocFailStatisType based on Integer32"""
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
        *(("invalidation", 1),
          ("other", 4),
          ("overtime", 2),
          ("rejected", 3))
    )


_HpnicfDot11APAssocFailStatisType_Type.__name__ = "Integer32"
_HpnicfDot11APAssocFailStatisType_Object = MibTableColumn
hpnicfDot11APAssocFailStatisType = _HpnicfDot11APAssocFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 11, 1, 1),
    _HpnicfDot11APAssocFailStatisType_Type()
)
hpnicfDot11APAssocFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatisType.setStatus("current")
_HpnicfDot11APAssocFailStatisCnt_Type = Counter32
_HpnicfDot11APAssocFailStatisCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatisCnt = _HpnicfDot11APAssocFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 11, 1, 2),
    _HpnicfDot11APAssocFailStatisCnt_Type()
)
hpnicfDot11APAssocFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatisCnt.setStatus("current")
_HpnicfDot11APReassocStatisTable_Object = MibTable
hpnicfDot11APReassocStatisTable = _HpnicfDot11APReassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatisTable.setStatus("current")
_HpnicfDot11APReassocStatisEntry_Object = MibTableRow
hpnicfDot11APReassocStatisEntry = _HpnicfDot11APReassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 12, 1)
)
hpnicfDot11APReassocStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APReassocStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatisEntry.setStatus("current")


class _HpnicfDot11APReassocStatisType_Type(Integer32):
    """Custom type hpnicfDot11APReassocStatisType based on Integer32"""
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
        *(("invalidation", 3),
          ("other", 6),
          ("overtime", 4),
          ("rejected", 5),
          ("success", 2),
          ("total", 1))
    )


_HpnicfDot11APReassocStatisType_Type.__name__ = "Integer32"
_HpnicfDot11APReassocStatisType_Object = MibTableColumn
hpnicfDot11APReassocStatisType = _HpnicfDot11APReassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 12, 1, 1),
    _HpnicfDot11APReassocStatisType_Type()
)
hpnicfDot11APReassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatisType.setStatus("current")
_HpnicfDot11APReassocStatisCnt_Type = Counter32
_HpnicfDot11APReassocStatisCnt_Object = MibTableColumn
hpnicfDot11APReassocStatisCnt = _HpnicfDot11APReassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 12, 1, 2),
    _HpnicfDot11APReassocStatisCnt_Type()
)
hpnicfDot11APReassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatisCnt.setStatus("current")
_HpnicfDot11APUserAuthStatisTable_Object = MibTable
hpnicfDot11APUserAuthStatisTable = _HpnicfDot11APUserAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 13)
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthStatisTable.setStatus("current")
_HpnicfDot11APUserAuthStatisEntry_Object = MibTableRow
hpnicfDot11APUserAuthStatisEntry = _HpnicfDot11APUserAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 13, 1)
)
hpnicfDot11APUserAuthStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11UserAuthStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthStatisEntry.setStatus("current")


class _HpnicfDot11UserAuthStatisType_Type(Integer32):
    """Custom type hpnicfDot11UserAuthStatisType based on Integer32"""
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
        *(("invalidation", 4),
          ("keyError", 3),
          ("other", 7),
          ("overtime", 5),
          ("rejected", 6),
          ("success", 2),
          ("total", 1))
    )


_HpnicfDot11UserAuthStatisType_Type.__name__ = "Integer32"
_HpnicfDot11UserAuthStatisType_Object = MibTableColumn
hpnicfDot11UserAuthStatisType = _HpnicfDot11UserAuthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 13, 1, 1),
    _HpnicfDot11UserAuthStatisType_Type()
)
hpnicfDot11UserAuthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11UserAuthStatisType.setStatus("current")
_HpnicfDot11UserAuthStatisCnt_Type = Counter32
_HpnicfDot11UserAuthStatisCnt_Object = MibTableColumn
hpnicfDot11UserAuthStatisCnt = _HpnicfDot11UserAuthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 13, 1, 2),
    _HpnicfDot11UserAuthStatisCnt_Type()
)
hpnicfDot11UserAuthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11UserAuthStatisCnt.setStatus("current")
_HpnicfDot11APDeauthStatisTable_Object = MibTable
hpnicfDot11APDeauthStatisTable = _HpnicfDot11APDeauthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 14)
)
if mibBuilder.loadTexts:
    hpnicfDot11APDeauthStatisTable.setStatus("current")
_HpnicfDot11APDeauthStatisEntry_Object = MibTableRow
hpnicfDot11APDeauthStatisEntry = _HpnicfDot11APDeauthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 14, 1)
)
hpnicfDot11APDeauthStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APDeauthStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APDeauthStatisEntry.setStatus("current")


class _HpnicfDot11APDeauthStatisType_Type(Integer32):
    """Custom type hpnicfDot11APDeauthStatisType based on Integer32"""
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
        *(("exception", 4),
          ("other", 5),
          ("shortResource", 3),
          ("stationLeaving", 2),
          ("total", 1))
    )


_HpnicfDot11APDeauthStatisType_Type.__name__ = "Integer32"
_HpnicfDot11APDeauthStatisType_Object = MibTableColumn
hpnicfDot11APDeauthStatisType = _HpnicfDot11APDeauthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 14, 1, 1),
    _HpnicfDot11APDeauthStatisType_Type()
)
hpnicfDot11APDeauthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APDeauthStatisType.setStatus("current")
_HpnicfDot11APDeauthStatisCnt_Type = Counter32
_HpnicfDot11APDeauthStatisCnt_Object = MibTableColumn
hpnicfDot11APDeauthStatisCnt = _HpnicfDot11APDeauthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 14, 1, 2),
    _HpnicfDot11APDeauthStatisCnt_Type()
)
hpnicfDot11APDeauthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APDeauthStatisCnt.setStatus("current")
_HpnicfDot11APDeassocStatisTable_Object = MibTable
hpnicfDot11APDeassocStatisTable = _HpnicfDot11APDeassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfDot11APDeassocStatisTable.setStatus("current")
_HpnicfDot11APDeassocStatisEntry_Object = MibTableRow
hpnicfDot11APDeassocStatisEntry = _HpnicfDot11APDeassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 15, 1)
)
hpnicfDot11APDeassocStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APDeassocStatisType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APDeassocStatisEntry.setStatus("current")


class _HpnicfDot11APDeassocStatisType_Type(Integer32):
    """Custom type hpnicfDot11APDeassocStatisType based on Integer32"""
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
        *(("exception", 4),
          ("other", 5),
          ("shortResource", 3),
          ("stationLeaving", 2),
          ("total", 1))
    )


_HpnicfDot11APDeassocStatisType_Type.__name__ = "Integer32"
_HpnicfDot11APDeassocStatisType_Object = MibTableColumn
hpnicfDot11APDeassocStatisType = _HpnicfDot11APDeassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 15, 1, 1),
    _HpnicfDot11APDeassocStatisType_Type()
)
hpnicfDot11APDeassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APDeassocStatisType.setStatus("current")
_HpnicfDot11APDeassocStatisCnt_Type = Counter32
_HpnicfDot11APDeassocStatisCnt_Object = MibTableColumn
hpnicfDot11APDeassocStatisCnt = _HpnicfDot11APDeassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 15, 1, 2),
    _HpnicfDot11APDeassocStatisCnt_Type()
)
hpnicfDot11APDeassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APDeassocStatisCnt.setStatus("current")
_HpnicfDot11APAssocFailStatis2Table_Object = MibTable
hpnicfDot11APAssocFailStatis2Table = _HpnicfDot11APAssocFailStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis2Table.setStatus("current")
_HpnicfDot11APAssocFailStatis2Entry_Object = MibTableRow
hpnicfDot11APAssocFailStatis2Entry = _HpnicfDot11APAssocFailStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 16, 1)
)
hpnicfDot11APAssocFailStatis2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APAssocFailStatis2Type"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis2Entry.setStatus("current")


class _HpnicfDot11APAssocFailStatis2Type_Type(Integer32):
    """Custom type hpnicfDot11APAssocFailStatis2Type based on Integer32"""
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
        *(("notSupportRateSet", 2),
          ("other", 4),
          ("shortResource", 1),
          ("unknownReasonCode", 3))
    )


_HpnicfDot11APAssocFailStatis2Type_Type.__name__ = "Integer32"
_HpnicfDot11APAssocFailStatis2Type_Object = MibTableColumn
hpnicfDot11APAssocFailStatis2Type = _HpnicfDot11APAssocFailStatis2Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 16, 1, 1),
    _HpnicfDot11APAssocFailStatis2Type_Type()
)
hpnicfDot11APAssocFailStatis2Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis2Type.setStatus("current")
_HpnicfDot11APAssocFailStatis2Cnt_Type = Counter32
_HpnicfDot11APAssocFailStatis2Cnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis2Cnt = _HpnicfDot11APAssocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 16, 1, 2),
    _HpnicfDot11APAssocFailStatis2Cnt_Type()
)
hpnicfDot11APAssocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis2Cnt.setStatus("current")
_HpnicfDot11APIfStatisTable_Object = MibTable
hpnicfDot11APIfStatisTable = _HpnicfDot11APIfStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17)
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatisTable.setStatus("current")
_HpnicfDot11APIfStatisEntry_Object = MibTableRow
hpnicfDot11APIfStatisEntry = _HpnicfDot11APIfStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1)
)
hpnicfDot11APIfStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatisEntry.setStatus("current")
_HpnicfDot11APIfInPkts_Type = Counter32
_HpnicfDot11APIfInPkts_Object = MibTableColumn
hpnicfDot11APIfInPkts = _HpnicfDot11APIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 1),
    _HpnicfDot11APIfInPkts_Type()
)
hpnicfDot11APIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInPkts.setStatus("current")
_HpnicfDot11APIfInNormalPkts_Type = Counter32
_HpnicfDot11APIfInNormalPkts_Object = MibTableColumn
hpnicfDot11APIfInNormalPkts = _HpnicfDot11APIfInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 2),
    _HpnicfDot11APIfInNormalPkts_Type()
)
hpnicfDot11APIfInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInNormalPkts.setStatus("current")
_HpnicfDot11APIfInErrorPkts_Type = Counter32
_HpnicfDot11APIfInErrorPkts_Object = MibTableColumn
hpnicfDot11APIfInErrorPkts = _HpnicfDot11APIfInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 3),
    _HpnicfDot11APIfInErrorPkts_Type()
)
hpnicfDot11APIfInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInErrorPkts.setStatus("current")
_HpnicfDot11APIfOutPkts_Type = Counter32
_HpnicfDot11APIfOutPkts_Object = MibTableColumn
hpnicfDot11APIfOutPkts = _HpnicfDot11APIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 4),
    _HpnicfDot11APIfOutPkts_Type()
)
hpnicfDot11APIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutPkts.setStatus("current")
_HpnicfDot11APIfInOctets_Type = Counter32
_HpnicfDot11APIfInOctets_Object = MibTableColumn
hpnicfDot11APIfInOctets = _HpnicfDot11APIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 5),
    _HpnicfDot11APIfInOctets_Type()
)
hpnicfDot11APIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInOctets.setStatus("current")
_HpnicfDot11APIfOutOctets_Type = Counter32
_HpnicfDot11APIfOutOctets_Object = MibTableColumn
hpnicfDot11APIfOutOctets = _HpnicfDot11APIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 6),
    _HpnicfDot11APIfOutOctets_Type()
)
hpnicfDot11APIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutOctets.setStatus("current")
_HpnicfDot11APIfFlowOut_Type = Unsigned32
_HpnicfDot11APIfFlowOut_Object = MibTableColumn
hpnicfDot11APIfFlowOut = _HpnicfDot11APIfFlowOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 7),
    _HpnicfDot11APIfFlowOut_Type()
)
hpnicfDot11APIfFlowOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfFlowOut.setStatus("current")
_HpnicfDot11APIfFlowIN_Type = Unsigned32
_HpnicfDot11APIfFlowIN_Object = MibTableColumn
hpnicfDot11APIfFlowIN = _HpnicfDot11APIfFlowIN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 8),
    _HpnicfDot11APIfFlowIN_Type()
)
hpnicfDot11APIfFlowIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfFlowIN.setStatus("current")
_HpnicfDot11APIfInUcastPkts_Type = Counter32
_HpnicfDot11APIfInUcastPkts_Object = MibTableColumn
hpnicfDot11APIfInUcastPkts = _HpnicfDot11APIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 9),
    _HpnicfDot11APIfInUcastPkts_Type()
)
hpnicfDot11APIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInUcastPkts.setStatus("current")
_HpnicfDot11APIfInNUcastPkts_Type = Counter32
_HpnicfDot11APIfInNUcastPkts_Object = MibTableColumn
hpnicfDot11APIfInNUcastPkts = _HpnicfDot11APIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 10),
    _HpnicfDot11APIfInNUcastPkts_Type()
)
hpnicfDot11APIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInNUcastPkts.setStatus("current")
_HpnicfDot11APIfInDiscardPkts_Type = Counter32
_HpnicfDot11APIfInDiscardPkts_Object = MibTableColumn
hpnicfDot11APIfInDiscardPkts = _HpnicfDot11APIfInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 11),
    _HpnicfDot11APIfInDiscardPkts_Type()
)
hpnicfDot11APIfInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInDiscardPkts.setStatus("current")
_HpnicfDot11APIfOutUcastPkts_Type = Counter32
_HpnicfDot11APIfOutUcastPkts_Object = MibTableColumn
hpnicfDot11APIfOutUcastPkts = _HpnicfDot11APIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 12),
    _HpnicfDot11APIfOutUcastPkts_Type()
)
hpnicfDot11APIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutUcastPkts.setStatus("current")
_HpnicfDot11APIfOutNUcastPkts_Type = Counter32
_HpnicfDot11APIfOutNUcastPkts_Object = MibTableColumn
hpnicfDot11APIfOutNUcastPkts = _HpnicfDot11APIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 13),
    _HpnicfDot11APIfOutNUcastPkts_Type()
)
hpnicfDot11APIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutNUcastPkts.setStatus("current")
_HpnicfDot11APIfOutDiscardPkts_Type = Counter32
_HpnicfDot11APIfOutDiscardPkts_Object = MibTableColumn
hpnicfDot11APIfOutDiscardPkts = _HpnicfDot11APIfOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 14),
    _HpnicfDot11APIfOutDiscardPkts_Type()
)
hpnicfDot11APIfOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutDiscardPkts.setStatus("current")
_HpnicfDot11APIfOutErrorPkts_Type = Counter32
_HpnicfDot11APIfOutErrorPkts_Object = MibTableColumn
hpnicfDot11APIfOutErrorPkts = _HpnicfDot11APIfOutErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 15),
    _HpnicfDot11APIfOutErrorPkts_Type()
)
hpnicfDot11APIfOutErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutErrorPkts.setStatus("current")
_HpnicfDot11APIfUpdownTimes_Type = Counter32
_HpnicfDot11APIfUpdownTimes_Object = MibTableColumn
hpnicfDot11APIfUpdownTimes = _HpnicfDot11APIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 16),
    _HpnicfDot11APIfUpdownTimes_Type()
)
hpnicfDot11APIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfUpdownTimes.setStatus("current")
_HpnicfDot11APIfStatusKeepTime_Type = TimeTicks
_HpnicfDot11APIfStatusKeepTime_Object = MibTableColumn
hpnicfDot11APIfStatusKeepTime = _HpnicfDot11APIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 17),
    _HpnicfDot11APIfStatusKeepTime_Type()
)
hpnicfDot11APIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatusKeepTime.setStatus("current")


class _HpnicfDot11APIfOperStatus_Type(Integer32):
    """Custom type hpnicfDot11APIfOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_HpnicfDot11APIfOperStatus_Type.__name__ = "Integer32"
_HpnicfDot11APIfOperStatus_Object = MibTableColumn
hpnicfDot11APIfOperStatus = _HpnicfDot11APIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 18),
    _HpnicfDot11APIfOperStatus_Type()
)
hpnicfDot11APIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOperStatus.setStatus("current")
_HpnicfDot11APIfInBrdcastPkts_Type = Counter64
_HpnicfDot11APIfInBrdcastPkts_Object = MibTableColumn
hpnicfDot11APIfInBrdcastPkts = _HpnicfDot11APIfInBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 19),
    _HpnicfDot11APIfInBrdcastPkts_Type()
)
hpnicfDot11APIfInBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInBrdcastPkts.setStatus("current")
_HpnicfDot11APIfOutBrdcastPkts_Type = Counter64
_HpnicfDot11APIfOutBrdcastPkts_Object = MibTableColumn
hpnicfDot11APIfOutBrdcastPkts = _HpnicfDot11APIfOutBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 20),
    _HpnicfDot11APIfOutBrdcastPkts_Type()
)
hpnicfDot11APIfOutBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutBrdcastPkts.setStatus("current")
_HpnicfDot11APIfInMulcastPkts_Type = Counter64
_HpnicfDot11APIfInMulcastPkts_Object = MibTableColumn
hpnicfDot11APIfInMulcastPkts = _HpnicfDot11APIfInMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 21),
    _HpnicfDot11APIfInMulcastPkts_Type()
)
hpnicfDot11APIfInMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInMulcastPkts.setStatus("current")
_HpnicfDot11APIfOutMulcastPkts_Type = Counter64
_HpnicfDot11APIfOutMulcastPkts_Object = MibTableColumn
hpnicfDot11APIfOutMulcastPkts = _HpnicfDot11APIfOutMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 22),
    _HpnicfDot11APIfOutMulcastPkts_Type()
)
hpnicfDot11APIfOutMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutMulcastPkts.setStatus("current")
_HpnicfDot11APIfInPayloadOctets_Type = Counter64
_HpnicfDot11APIfInPayloadOctets_Object = MibTableColumn
hpnicfDot11APIfInPayloadOctets = _HpnicfDot11APIfInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 23),
    _HpnicfDot11APIfInPayloadOctets_Type()
)
hpnicfDot11APIfInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInPayloadOctets.setStatus("current")
_HpnicfDot11APIfOutPayloadOctets_Type = Counter64
_HpnicfDot11APIfOutPayloadOctets_Object = MibTableColumn
hpnicfDot11APIfOutPayloadOctets = _HpnicfDot11APIfOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 17, 1, 24),
    _HpnicfDot11APIfOutPayloadOctets_Type()
)
hpnicfDot11APIfOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutPayloadOctets.setStatus("current")
_HpnicfDot11RadioMngFrmStatisTable_Object = MibTable
hpnicfDot11RadioMngFrmStatisTable = _HpnicfDot11RadioMngFrmStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 18)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioMngFrmStatisTable.setStatus("current")
_HpnicfDot11RadioMngFrmStatisEntry_Object = MibTableRow
hpnicfDot11RadioMngFrmStatisEntry = _HpnicfDot11RadioMngFrmStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 18, 1)
)
hpnicfDot11RadioMngFrmStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11MngFrmType"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioMngFrmStatisEntry.setStatus("current")


class _HpnicfDot11MngFrmType_Type(Integer32):
    """Custom type hpnicfDot11MngFrmType based on Integer32"""
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
        *(("action", 12),
          ("assocReq", 1),
          ("assocResp", 2),
          ("atim", 8),
          ("authentication", 10),
          ("beacon", 7),
          ("deauthentication", 11),
          ("disassociation", 9),
          ("probeReq", 5),
          ("probeResp", 6),
          ("reassocReq", 3),
          ("reassocResp", 4))
    )


_HpnicfDot11MngFrmType_Type.__name__ = "Integer32"
_HpnicfDot11MngFrmType_Object = MibTableColumn
hpnicfDot11MngFrmType = _HpnicfDot11MngFrmType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 18, 1, 1),
    _HpnicfDot11MngFrmType_Type()
)
hpnicfDot11MngFrmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11MngFrmType.setStatus("current")
_HpnicfDot11MngFrmCnt_Type = Counter32
_HpnicfDot11MngFrmCnt_Object = MibTableColumn
hpnicfDot11MngFrmCnt = _HpnicfDot11MngFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 18, 1, 2),
    _HpnicfDot11MngFrmCnt_Type()
)
hpnicfDot11MngFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11MngFrmCnt.setStatus("current")
_HpnicfDot11APPacketSizeStatisTable_Object = MibTable
hpnicfDot11APPacketSizeStatisTable = _HpnicfDot11APPacketSizeStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 19)
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketSizeStatisTable.setStatus("current")
_HpnicfDot11APPacketSizeStatisEntry_Object = MibTableRow
hpnicfDot11APPacketSizeStatisEntry = _HpnicfDot11APPacketSizeStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 19, 1)
)
hpnicfDot11APPacketSizeStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APPacketSize"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketSizeStatisEntry.setStatus("current")


class _HpnicfDot11APPacketSize_Type(Integer32):
    """Custom type hpnicfDot11APPacketSize based on Integer32"""
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
        *(("sizeLevel1", 1),
          ("sizeLevel2", 2),
          ("sizeLevel3", 3),
          ("sizeLevel4", 4))
    )


_HpnicfDot11APPacketSize_Type.__name__ = "Integer32"
_HpnicfDot11APPacketSize_Object = MibTableColumn
hpnicfDot11APPacketSize = _HpnicfDot11APPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 19, 1, 1),
    _HpnicfDot11APPacketSize_Type()
)
hpnicfDot11APPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APPacketSize.setStatus("current")
_HpnicfDot11APRXPacketSizeCount_Type = Counter64
_HpnicfDot11APRXPacketSizeCount_Object = MibTableColumn
hpnicfDot11APRXPacketSizeCount = _HpnicfDot11APRXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 19, 1, 2),
    _HpnicfDot11APRXPacketSizeCount_Type()
)
hpnicfDot11APRXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APRXPacketSizeCount.setStatus("current")
_HpnicfDot11APTXPacketSizeCount_Type = Counter64
_HpnicfDot11APTXPacketSizeCount_Object = MibTableColumn
hpnicfDot11APTXPacketSizeCount = _HpnicfDot11APTXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 19, 1, 3),
    _HpnicfDot11APTXPacketSizeCount_Type()
)
hpnicfDot11APTXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTXPacketSizeCount.setStatus("current")
_HpnicfDot11APPacketRateStatisTable_Object = MibTable
hpnicfDot11APPacketRateStatisTable = _HpnicfDot11APPacketRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 20)
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketRateStatisTable.setStatus("current")
_HpnicfDot11APPacketRateStatisEntry_Object = MibTableRow
hpnicfDot11APPacketRateStatisEntry = _HpnicfDot11APPacketRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 20, 1)
)
hpnicfDot11APPacketRateStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APPacketRate"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketRateStatisEntry.setStatus("current")
_HpnicfDot11APPacketRate_Type = Integer32
_HpnicfDot11APPacketRate_Object = MibTableColumn
hpnicfDot11APPacketRate = _HpnicfDot11APPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 20, 1, 1),
    _HpnicfDot11APPacketRate_Type()
)
hpnicfDot11APPacketRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APPacketRate.setStatus("current")
_HpnicfDot11APRXPacketRateCount_Type = Counter64
_HpnicfDot11APRXPacketRateCount_Object = MibTableColumn
hpnicfDot11APRXPacketRateCount = _HpnicfDot11APRXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 20, 1, 2),
    _HpnicfDot11APRXPacketRateCount_Type()
)
hpnicfDot11APRXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APRXPacketRateCount.setStatus("current")
_HpnicfDot11APTXPacketRateCount_Type = Counter64
_HpnicfDot11APTXPacketRateCount_Object = MibTableColumn
hpnicfDot11APTXPacketRateCount = _HpnicfDot11APTXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 20, 1, 3),
    _HpnicfDot11APTXPacketRateCount_Type()
)
hpnicfDot11APTXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTXPacketRateCount.setStatus("current")
_HpnicfDot11APPacketMCSRateStatisTable_Object = MibTable
hpnicfDot11APPacketMCSRateStatisTable = _HpnicfDot11APPacketMCSRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 21)
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCSRateStatisTable.setStatus("current")
_HpnicfDot11APPacketMCSRateStatisEntry_Object = MibTableRow
hpnicfDot11APPacketMCSRateStatisEntry = _HpnicfDot11APPacketMCSRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 21, 1)
)
hpnicfDot11APPacketMCSRateStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APPacketMCSRate"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCSRateStatisEntry.setStatus("current")
_HpnicfDot11APPacketMCSRate_Type = Integer32
_HpnicfDot11APPacketMCSRate_Object = MibTableColumn
hpnicfDot11APPacketMCSRate = _HpnicfDot11APPacketMCSRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 21, 1, 1),
    _HpnicfDot11APPacketMCSRate_Type()
)
hpnicfDot11APPacketMCSRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCSRate.setStatus("current")
_HpnicfDot11APRXPacketMCSRateCount_Type = Counter64
_HpnicfDot11APRXPacketMCSRateCount_Object = MibTableColumn
hpnicfDot11APRXPacketMCSRateCount = _HpnicfDot11APRXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 21, 1, 2),
    _HpnicfDot11APRXPacketMCSRateCount_Type()
)
hpnicfDot11APRXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APRXPacketMCSRateCount.setStatus("current")
_HpnicfDot11APTXPacketMCSRateCount_Type = Counter64
_HpnicfDot11APTXPacketMCSRateCount_Object = MibTableColumn
hpnicfDot11APTXPacketMCSRateCount = _HpnicfDot11APTXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 21, 1, 3),
    _HpnicfDot11APTXPacketMCSRateCount_Type()
)
hpnicfDot11APTXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTXPacketMCSRateCount.setStatus("current")
_HpnicfDot11APAssocFailStatis3Table_Object = MibTable
hpnicfDot11APAssocFailStatis3Table = _HpnicfDot11APAssocFailStatis3Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22)
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3Table.setStatus("current")
_HpnicfDot11APAssocFailStatis3Entry_Object = MibTableRow
hpnicfDot11APAssocFailStatis3Entry = _HpnicfDot11APAssocFailStatis3Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1)
)
hpnicfDot11APAssocFailStatis3Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3Entry.setStatus("current")
_HpnicfDot11APAssocFailStatis3SRCnt_Type = Counter32
_HpnicfDot11APAssocFailStatis3SRCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis3SRCnt = _HpnicfDot11APAssocFailStatis3SRCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 1),
    _HpnicfDot11APAssocFailStatis3SRCnt_Type()
)
hpnicfDot11APAssocFailStatis3SRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3SRCnt.setStatus("current")
_HpnicfDot11APAssocFailStatis3NSRCnt_Type = Counter32
_HpnicfDot11APAssocFailStatis3NSRCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis3NSRCnt = _HpnicfDot11APAssocFailStatis3NSRCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 2),
    _HpnicfDot11APAssocFailStatis3NSRCnt_Type()
)
hpnicfDot11APAssocFailStatis3NSRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3NSRCnt.setStatus("current")
_HpnicfDot11APAssocFailStatis3URCCnt_Type = Counter32
_HpnicfDot11APAssocFailStatis3URCCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis3URCCnt = _HpnicfDot11APAssocFailStatis3URCCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 3),
    _HpnicfDot11APAssocFailStatis3URCCnt_Type()
)
hpnicfDot11APAssocFailStatis3URCCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3URCCnt.setStatus("current")
_HpnicfDot11APAssocFailStatis3RFCnt_Type = Counter32
_HpnicfDot11APAssocFailStatis3RFCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis3RFCnt = _HpnicfDot11APAssocFailStatis3RFCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 4),
    _HpnicfDot11APAssocFailStatis3RFCnt_Type()
)
hpnicfDot11APAssocFailStatis3RFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3RFCnt.setStatus("current")
_HpnicfDot11APAssocFailStatis3OtherCnt_Type = Counter32
_HpnicfDot11APAssocFailStatis3OtherCnt_Object = MibTableColumn
hpnicfDot11APAssocFailStatis3OtherCnt = _HpnicfDot11APAssocFailStatis3OtherCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 5),
    _HpnicfDot11APAssocFailStatis3OtherCnt_Type()
)
hpnicfDot11APAssocFailStatis3OtherCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatis3OtherCnt.setStatus("current")
_HpnicfDot11APAssocFailStatisRSSILowCntCM_Type = Counter32
_HpnicfDot11APAssocFailStatisRSSILowCntCM_Object = MibTableColumn
hpnicfDot11APAssocFailStatisRSSILowCntCM = _HpnicfDot11APAssocFailStatisRSSILowCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 22, 1, 6),
    _HpnicfDot11APAssocFailStatisRSSILowCntCM_Type()
)
hpnicfDot11APAssocFailStatisRSSILowCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocFailStatisRSSILowCntCM.setStatus("current")
_HpnicfDot11APIfStatisByAPIDTable_Object = MibTable
hpnicfDot11APIfStatisByAPIDTable = _HpnicfDot11APIfStatisByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23)
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatisByAPIDTable.setStatus("current")
_HpnicfDot11APIfStatisByAPIDEntry_Object = MibTableRow
hpnicfDot11APIfStatisByAPIDEntry = _HpnicfDot11APIfStatisByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1)
)
hpnicfDot11APIfStatisByAPIDEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatisByAPIDEntry.setStatus("current")
_HpnicfDot11APIfInPkts2_Type = Counter64
_HpnicfDot11APIfInPkts2_Object = MibTableColumn
hpnicfDot11APIfInPkts2 = _HpnicfDot11APIfInPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 1),
    _HpnicfDot11APIfInPkts2_Type()
)
hpnicfDot11APIfInPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInPkts2.setStatus("current")
_HpnicfDot11APIfInNormalPkts2_Type = Counter64
_HpnicfDot11APIfInNormalPkts2_Object = MibTableColumn
hpnicfDot11APIfInNormalPkts2 = _HpnicfDot11APIfInNormalPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 2),
    _HpnicfDot11APIfInNormalPkts2_Type()
)
hpnicfDot11APIfInNormalPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInNormalPkts2.setStatus("current")
_HpnicfDot11APIfInErrorPkts2_Type = Counter64
_HpnicfDot11APIfInErrorPkts2_Object = MibTableColumn
hpnicfDot11APIfInErrorPkts2 = _HpnicfDot11APIfInErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 3),
    _HpnicfDot11APIfInErrorPkts2_Type()
)
hpnicfDot11APIfInErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInErrorPkts2.setStatus("current")
_HpnicfDot11APIfOutPkts2_Type = Counter64
_HpnicfDot11APIfOutPkts2_Object = MibTableColumn
hpnicfDot11APIfOutPkts2 = _HpnicfDot11APIfOutPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 4),
    _HpnicfDot11APIfOutPkts2_Type()
)
hpnicfDot11APIfOutPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutPkts2.setStatus("current")
_HpnicfDot11APIfInOctets2_Type = Counter64
_HpnicfDot11APIfInOctets2_Object = MibTableColumn
hpnicfDot11APIfInOctets2 = _HpnicfDot11APIfInOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 5),
    _HpnicfDot11APIfInOctets2_Type()
)
hpnicfDot11APIfInOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInOctets2.setStatus("current")
_HpnicfDot11APIfOutOctets2_Type = Counter64
_HpnicfDot11APIfOutOctets2_Object = MibTableColumn
hpnicfDot11APIfOutOctets2 = _HpnicfDot11APIfOutOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 6),
    _HpnicfDot11APIfOutOctets2_Type()
)
hpnicfDot11APIfOutOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutOctets2.setStatus("current")
_HpnicfDot11APIfFlowOut2_Type = Unsigned32
_HpnicfDot11APIfFlowOut2_Object = MibTableColumn
hpnicfDot11APIfFlowOut2 = _HpnicfDot11APIfFlowOut2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 7),
    _HpnicfDot11APIfFlowOut2_Type()
)
hpnicfDot11APIfFlowOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfFlowOut2.setStatus("current")
_HpnicfDot11APIfFlowIN2_Type = Unsigned32
_HpnicfDot11APIfFlowIN2_Object = MibTableColumn
hpnicfDot11APIfFlowIN2 = _HpnicfDot11APIfFlowIN2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 8),
    _HpnicfDot11APIfFlowIN2_Type()
)
hpnicfDot11APIfFlowIN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfFlowIN2.setStatus("current")
_HpnicfDot11APIfInUcastPkts2_Type = Counter64
_HpnicfDot11APIfInUcastPkts2_Object = MibTableColumn
hpnicfDot11APIfInUcastPkts2 = _HpnicfDot11APIfInUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 9),
    _HpnicfDot11APIfInUcastPkts2_Type()
)
hpnicfDot11APIfInUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInUcastPkts2.setStatus("current")
_HpnicfDot11APIfInNUcastPkts2_Type = Counter64
_HpnicfDot11APIfInNUcastPkts2_Object = MibTableColumn
hpnicfDot11APIfInNUcastPkts2 = _HpnicfDot11APIfInNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 10),
    _HpnicfDot11APIfInNUcastPkts2_Type()
)
hpnicfDot11APIfInNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInNUcastPkts2.setStatus("current")
_HpnicfDot11APIfInDiscardPkts2_Type = Counter64
_HpnicfDot11APIfInDiscardPkts2_Object = MibTableColumn
hpnicfDot11APIfInDiscardPkts2 = _HpnicfDot11APIfInDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 11),
    _HpnicfDot11APIfInDiscardPkts2_Type()
)
hpnicfDot11APIfInDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInDiscardPkts2.setStatus("current")
_HpnicfDot11APIfOutUcastPkts2_Type = Counter64
_HpnicfDot11APIfOutUcastPkts2_Object = MibTableColumn
hpnicfDot11APIfOutUcastPkts2 = _HpnicfDot11APIfOutUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 12),
    _HpnicfDot11APIfOutUcastPkts2_Type()
)
hpnicfDot11APIfOutUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutUcastPkts2.setStatus("current")
_HpnicfDot11APIfOutNUcastPkts2_Type = Counter64
_HpnicfDot11APIfOutNUcastPkts2_Object = MibTableColumn
hpnicfDot11APIfOutNUcastPkts2 = _HpnicfDot11APIfOutNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 13),
    _HpnicfDot11APIfOutNUcastPkts2_Type()
)
hpnicfDot11APIfOutNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutNUcastPkts2.setStatus("current")
_HpnicfDot11APIfOutDiscardPkts2_Type = Counter64
_HpnicfDot11APIfOutDiscardPkts2_Object = MibTableColumn
hpnicfDot11APIfOutDiscardPkts2 = _HpnicfDot11APIfOutDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 14),
    _HpnicfDot11APIfOutDiscardPkts2_Type()
)
hpnicfDot11APIfOutDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutDiscardPkts2.setStatus("current")
_HpnicfDot11APIfOutErrorPkts2_Type = Counter64
_HpnicfDot11APIfOutErrorPkts2_Object = MibTableColumn
hpnicfDot11APIfOutErrorPkts2 = _HpnicfDot11APIfOutErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 15),
    _HpnicfDot11APIfOutErrorPkts2_Type()
)
hpnicfDot11APIfOutErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutErrorPkts2.setStatus("current")
_HpnicfDot11APIfUpdownTimes2_Type = Counter32
_HpnicfDot11APIfUpdownTimes2_Object = MibTableColumn
hpnicfDot11APIfUpdownTimes2 = _HpnicfDot11APIfUpdownTimes2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 16),
    _HpnicfDot11APIfUpdownTimes2_Type()
)
hpnicfDot11APIfUpdownTimes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfUpdownTimes2.setStatus("current")
_HpnicfDot11APIfStatusKeepTime2_Type = TimeTicks
_HpnicfDot11APIfStatusKeepTime2_Object = MibTableColumn
hpnicfDot11APIfStatusKeepTime2 = _HpnicfDot11APIfStatusKeepTime2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 17),
    _HpnicfDot11APIfStatusKeepTime2_Type()
)
hpnicfDot11APIfStatusKeepTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfStatusKeepTime2.setStatus("current")


class _HpnicfDot11APIfOperStatus2_Type(Integer32):
    """Custom type hpnicfDot11APIfOperStatus2 based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_HpnicfDot11APIfOperStatus2_Type.__name__ = "Integer32"
_HpnicfDot11APIfOperStatus2_Object = MibTableColumn
hpnicfDot11APIfOperStatus2 = _HpnicfDot11APIfOperStatus2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 18),
    _HpnicfDot11APIfOperStatus2_Type()
)
hpnicfDot11APIfOperStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOperStatus2.setStatus("current")
_HpnicfDot11APIfInBrdcastPkts2_Type = Counter64
_HpnicfDot11APIfInBrdcastPkts2_Object = MibTableColumn
hpnicfDot11APIfInBrdcastPkts2 = _HpnicfDot11APIfInBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 19),
    _HpnicfDot11APIfInBrdcastPkts2_Type()
)
hpnicfDot11APIfInBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInBrdcastPkts2.setStatus("current")
_HpnicfDot11APIfOutBrdcastPkts2_Type = Counter64
_HpnicfDot11APIfOutBrdcastPkts2_Object = MibTableColumn
hpnicfDot11APIfOutBrdcastPkts2 = _HpnicfDot11APIfOutBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 20),
    _HpnicfDot11APIfOutBrdcastPkts2_Type()
)
hpnicfDot11APIfOutBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutBrdcastPkts2.setStatus("current")
_HpnicfDot11APIfInMulcastPkts2_Type = Counter64
_HpnicfDot11APIfInMulcastPkts2_Object = MibTableColumn
hpnicfDot11APIfInMulcastPkts2 = _HpnicfDot11APIfInMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 21),
    _HpnicfDot11APIfInMulcastPkts2_Type()
)
hpnicfDot11APIfInMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInMulcastPkts2.setStatus("current")
_HpnicfDot11APIfOutMulcastPkts2_Type = Counter64
_HpnicfDot11APIfOutMulcastPkts2_Object = MibTableColumn
hpnicfDot11APIfOutMulcastPkts2 = _HpnicfDot11APIfOutMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 22),
    _HpnicfDot11APIfOutMulcastPkts2_Type()
)
hpnicfDot11APIfOutMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutMulcastPkts2.setStatus("current")
_HpnicfDot11APIfInPayloadOctets2_Type = Counter64
_HpnicfDot11APIfInPayloadOctets2_Object = MibTableColumn
hpnicfDot11APIfInPayloadOctets2 = _HpnicfDot11APIfInPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 23),
    _HpnicfDot11APIfInPayloadOctets2_Type()
)
hpnicfDot11APIfInPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInPayloadOctets2.setStatus("current")
_HpnicfDot11APIfOutPayloadOctets2_Type = Counter64
_HpnicfDot11APIfOutPayloadOctets2_Object = MibTableColumn
hpnicfDot11APIfOutPayloadOctets2 = _HpnicfDot11APIfOutPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 24),
    _HpnicfDot11APIfOutPayloadOctets2_Type()
)
hpnicfDot11APIfOutPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutPayloadOctets2.setStatus("current")
_HpnicfDot11APIfInDataOctets2_Type = Counter64
_HpnicfDot11APIfInDataOctets2_Object = MibTableColumn
hpnicfDot11APIfInDataOctets2 = _HpnicfDot11APIfInDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 25),
    _HpnicfDot11APIfInDataOctets2_Type()
)
hpnicfDot11APIfInDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfInDataOctets2.setStatus("current")
_HpnicfDot11APIfOutDataOctets2_Type = Counter64
_HpnicfDot11APIfOutDataOctets2_Object = MibTableColumn
hpnicfDot11APIfOutDataOctets2 = _HpnicfDot11APIfOutDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 26),
    _HpnicfDot11APIfOutDataOctets2_Type()
)
hpnicfDot11APIfOutDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOutDataOctets2.setStatus("current")


class _HpnicfDot11APIfAdminStatus_Type(Integer32):
    """Custom type hpnicfDot11APIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HpnicfDot11APIfAdminStatus_Type.__name__ = "Integer32"
_HpnicfDot11APIfAdminStatus_Object = MibTableColumn
hpnicfDot11APIfAdminStatus = _HpnicfDot11APIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 27),
    _HpnicfDot11APIfAdminStatus_Type()
)
hpnicfDot11APIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APIfAdminStatus.setStatus("current")


class _HpnicfDot11APIfOperStatusCM_Type(Integer32):
    """Custom type hpnicfDot11APIfOperStatusCM based on Integer32"""
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
        *(("admindown", 4),
          ("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HpnicfDot11APIfOperStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11APIfOperStatusCM_Object = MibTableColumn
hpnicfDot11APIfOperStatusCM = _HpnicfDot11APIfOperStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 23, 1, 28),
    _HpnicfDot11APIfOperStatusCM_Type()
)
hpnicfDot11APIfOperStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APIfOperStatusCM.setStatus("current")
_HpnicfDot11APUserSecAuthStatisTable_Object = MibTable
hpnicfDot11APUserSecAuthStatisTable = _HpnicfDot11APUserSecAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24)
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthStatisTable.setStatus("current")
_HpnicfDot11APUserSecAuthStatisEntry_Object = MibTableRow
hpnicfDot11APUserSecAuthStatisEntry = _HpnicfDot11APUserSecAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1)
)
hpnicfDot11APUserSecAuthStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthStatisEntry.setStatus("current")
_HpnicfDot11APUserAuthCurNumber_Type = Integer32
_HpnicfDot11APUserAuthCurNumber_Object = MibTableColumn
hpnicfDot11APUserAuthCurNumber = _HpnicfDot11APUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 1),
    _HpnicfDot11APUserAuthCurNumber_Type()
)
hpnicfDot11APUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthCurNumber.setStatus("current")
_HpnicfDot11APUserConnFailCnt_Type = Counter32
_HpnicfDot11APUserConnFailCnt_Object = MibTableColumn
hpnicfDot11APUserConnFailCnt = _HpnicfDot11APUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 2),
    _HpnicfDot11APUserConnFailCnt_Type()
)
hpnicfDot11APUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserConnFailCnt.setStatus("current")
_HpnicfDot11APUserAuthReqCnt_Type = Counter32
_HpnicfDot11APUserAuthReqCnt_Object = MibTableColumn
hpnicfDot11APUserAuthReqCnt = _HpnicfDot11APUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 3),
    _HpnicfDot11APUserAuthReqCnt_Type()
)
hpnicfDot11APUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthReqCnt.setStatus("current")
_HpnicfDot11APUserAuthSuccCnt_Type = Counter32
_HpnicfDot11APUserAuthSuccCnt_Object = MibTableColumn
hpnicfDot11APUserAuthSuccCnt = _HpnicfDot11APUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 4),
    _HpnicfDot11APUserAuthSuccCnt_Type()
)
hpnicfDot11APUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthSuccCnt.setStatus("current")
_HpnicfDot11APUserAuthFailCnt_Type = Counter32
_HpnicfDot11APUserAuthFailCnt_Object = MibTableColumn
hpnicfDot11APUserAuthFailCnt = _HpnicfDot11APUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 5),
    _HpnicfDot11APUserAuthFailCnt_Type()
)
hpnicfDot11APUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthFailCnt.setStatus("current")
_HpnicfDot11AllUserOnlineTime_Type = TimeTicks
_HpnicfDot11AllUserOnlineTime_Object = MibTableColumn
hpnicfDot11AllUserOnlineTime = _HpnicfDot11AllUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 24, 1, 6),
    _HpnicfDot11AllUserOnlineTime_Type()
)
hpnicfDot11AllUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AllUserOnlineTime.setStatus("current")
_HpnicfDot11APUserInfoStatisTable_Object = MibTable
hpnicfDot11APUserInfoStatisTable = _HpnicfDot11APUserInfoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25)
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserInfoStatisTable.setStatus("current")
_HpnicfDot11APUserInfoStatisEntry_Object = MibTableRow
hpnicfDot11APUserInfoStatisEntry = _HpnicfDot11APUserInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1)
)
hpnicfDot11APUserInfoStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APUserMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserInfoStatisEntry.setStatus("current")
_HpnicfDot11APUserMacAddr_Type = MacAddress
_HpnicfDot11APUserMacAddr_Object = MibTableColumn
hpnicfDot11APUserMacAddr = _HpnicfDot11APUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 1),
    _HpnicfDot11APUserMacAddr_Type()
)
hpnicfDot11APUserMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APUserMacAddr.setStatus("current")
_HpnicfDot11APUserIpAddr_Type = IpAddress
_HpnicfDot11APUserIpAddr_Object = MibTableColumn
hpnicfDot11APUserIpAddr = _HpnicfDot11APUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 2),
    _HpnicfDot11APUserIpAddr_Type()
)
hpnicfDot11APUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserIpAddr.setStatus("current")
_HpnicfDot11APUserLoginName_Type = OctetString
_HpnicfDot11APUserLoginName_Object = MibTableColumn
hpnicfDot11APUserLoginName = _HpnicfDot11APUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 3),
    _HpnicfDot11APUserLoginName_Type()
)
hpnicfDot11APUserLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserLoginName.setStatus("current")
_HpnicfDot11APUserLoginTime_Type = OctetString
_HpnicfDot11APUserLoginTime_Object = MibTableColumn
hpnicfDot11APUserLoginTime = _HpnicfDot11APUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 4),
    _HpnicfDot11APUserLoginTime_Type()
)
hpnicfDot11APUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserLoginTime.setStatus("current")
_HpnicfDot11APUserOnlineTime_Type = TimeTicks
_HpnicfDot11APUserOnlineTime_Object = MibTableColumn
hpnicfDot11APUserOnlineTime = _HpnicfDot11APUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 5),
    _HpnicfDot11APUserOnlineTime_Type()
)
hpnicfDot11APUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserOnlineTime.setStatus("current")
_HpnicfDot11APUserLoginNameCM_Type = OctetString
_HpnicfDot11APUserLoginNameCM_Object = MibTableColumn
hpnicfDot11APUserLoginNameCM = _HpnicfDot11APUserLoginNameCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 6),
    _HpnicfDot11APUserLoginNameCM_Type()
)
hpnicfDot11APUserLoginNameCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserLoginNameCM.setStatus("current")


class _HpnicfDot11APUserAuthTypeCM_Type(Integer32):
    """Custom type hpnicfDot11APUserAuthTypeCM based on Integer32"""
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
        *(("associateAuth", 2),
          ("authFree", 1),
          ("autoAuth", 4),
          ("portalAuth", 3))
    )


_HpnicfDot11APUserAuthTypeCM_Type.__name__ = "Integer32"
_HpnicfDot11APUserAuthTypeCM_Object = MibTableColumn
hpnicfDot11APUserAuthTypeCM = _HpnicfDot11APUserAuthTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 7),
    _HpnicfDot11APUserAuthTypeCM_Type()
)
hpnicfDot11APUserAuthTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthTypeCM.setStatus("current")
_HpnicfDot11APUserTxPacketCntCM_Type = Counter32
_HpnicfDot11APUserTxPacketCntCM_Object = MibTableColumn
hpnicfDot11APUserTxPacketCntCM = _HpnicfDot11APUserTxPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 8),
    _HpnicfDot11APUserTxPacketCntCM_Type()
)
hpnicfDot11APUserTxPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserTxPacketCntCM.setStatus("current")
_HpnicfDot11APUserTxBytesCM_Type = Counter64
_HpnicfDot11APUserTxBytesCM_Object = MibTableColumn
hpnicfDot11APUserTxBytesCM = _HpnicfDot11APUserTxBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 9),
    _HpnicfDot11APUserTxBytesCM_Type()
)
hpnicfDot11APUserTxBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserTxBytesCM.setStatus("current")
_HpnicfDot11APUserRxPacketCntCM_Type = Counter32
_HpnicfDot11APUserRxPacketCntCM_Object = MibTableColumn
hpnicfDot11APUserRxPacketCntCM = _HpnicfDot11APUserRxPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 10),
    _HpnicfDot11APUserRxPacketCntCM_Type()
)
hpnicfDot11APUserRxPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserRxPacketCntCM.setStatus("current")
_HpnicfDot11APUserRxBytesCM_Type = Counter64
_HpnicfDot11APUserRxBytesCM_Object = MibTableColumn
hpnicfDot11APUserRxBytesCM = _HpnicfDot11APUserRxBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 25, 1, 11),
    _HpnicfDot11APUserRxBytesCM_Type()
)
hpnicfDot11APUserRxBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserRxBytesCM.setStatus("current")
_HpnicfDot11APReassocStatis2Table_Object = MibTable
hpnicfDot11APReassocStatis2Table = _HpnicfDot11APReassocStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 26)
)
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatis2Table.setStatus("current")
_HpnicfDot11APReassocStatis2Entry_Object = MibTableRow
hpnicfDot11APReassocStatis2Entry = _HpnicfDot11APReassocStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 26, 1)
)
hpnicfDot11APReassocStatis2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APReassocStatis2Entry.setStatus("current")
_HpnicfDot11APReassocFailStatis2Cnt_Type = Counter32
_HpnicfDot11APReassocFailStatis2Cnt_Object = MibTableColumn
hpnicfDot11APReassocFailStatis2Cnt = _HpnicfDot11APReassocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 26, 1, 1),
    _HpnicfDot11APReassocFailStatis2Cnt_Type()
)
hpnicfDot11APReassocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APReassocFailStatis2Cnt.setStatus("current")
_HpnicfDot11TrafficTable_Object = MibTable
hpnicfDot11TrafficTable = _HpnicfDot11TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27)
)
if mibBuilder.loadTexts:
    hpnicfDot11TrafficTable.setStatus("current")
_HpnicfDot11TrafficEntry_Object = MibTableRow
hpnicfDot11TrafficEntry = _HpnicfDot11TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1)
)
hpnicfDot11TrafficEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11SSIDIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11TrafficEntry.setStatus("current")
_HpnicfDot11SSIDIndex_Type = OctetString
_HpnicfDot11SSIDIndex_Object = MibTableColumn
hpnicfDot11SSIDIndex = _HpnicfDot11SSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1, 1),
    _HpnicfDot11SSIDIndex_Type()
)
hpnicfDot11SSIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDIndex.setStatus("current")
_HpnicfDot11UpPacketNumber_Type = Counter64
_HpnicfDot11UpPacketNumber_Object = MibTableColumn
hpnicfDot11UpPacketNumber = _HpnicfDot11UpPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1, 2),
    _HpnicfDot11UpPacketNumber_Type()
)
hpnicfDot11UpPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11UpPacketNumber.setStatus("current")
_HpnicfDot11UpByteNumber_Type = Counter64
_HpnicfDot11UpByteNumber_Object = MibTableColumn
hpnicfDot11UpByteNumber = _HpnicfDot11UpByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1, 3),
    _HpnicfDot11UpByteNumber_Type()
)
hpnicfDot11UpByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11UpByteNumber.setStatus("current")
_HpnicfDot11DownPacketNumber_Type = Counter64
_HpnicfDot11DownPacketNumber_Object = MibTableColumn
hpnicfDot11DownPacketNumber = _HpnicfDot11DownPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1, 4),
    _HpnicfDot11DownPacketNumber_Type()
)
hpnicfDot11DownPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DownPacketNumber.setStatus("current")
_HpnicfDot11DownByteNumber_Type = Counter64
_HpnicfDot11DownByteNumber_Object = MibTableColumn
hpnicfDot11DownByteNumber = _HpnicfDot11DownByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 27, 1, 5),
    _HpnicfDot11DownByteNumber_Type()
)
hpnicfDot11DownByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11DownByteNumber.setStatus("current")
_HpnicfDot11APEchoStatisTable_Object = MibTable
hpnicfDot11APEchoStatisTable = _HpnicfDot11APEchoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 28)
)
if mibBuilder.loadTexts:
    hpnicfDot11APEchoStatisTable.setStatus("current")
_HpnicfDot11APEchoInfoStatisEntry_Object = MibTableRow
hpnicfDot11APEchoInfoStatisEntry = _HpnicfDot11APEchoInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 28, 1)
)
hpnicfDot11APEchoInfoStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APEchoInfoStatisEntry.setStatus("current")
_HpnicfDot11APEchoAvgDelay_Type = Integer32
_HpnicfDot11APEchoAvgDelay_Object = MibTableColumn
hpnicfDot11APEchoAvgDelay = _HpnicfDot11APEchoAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 28, 1, 1),
    _HpnicfDot11APEchoAvgDelay_Type()
)
hpnicfDot11APEchoAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APEchoAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APEchoAvgDelay.setUnits("millisecond")
_HpnicfDot11APEchoRequestCnt_Type = Counter64
_HpnicfDot11APEchoRequestCnt_Object = MibTableColumn
hpnicfDot11APEchoRequestCnt = _HpnicfDot11APEchoRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 28, 1, 2),
    _HpnicfDot11APEchoRequestCnt_Type()
)
hpnicfDot11APEchoRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APEchoRequestCnt.setStatus("current")
_HpnicfDot11APEchoRespLossCnt_Type = Counter64
_HpnicfDot11APEchoRespLossCnt_Object = MibTableColumn
hpnicfDot11APEchoRespLossCnt = _HpnicfDot11APEchoRespLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 28, 1, 3),
    _HpnicfDot11APEchoRespLossCnt_Type()
)
hpnicfDot11APEchoRespLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APEchoRespLossCnt.setStatus("current")
_HpnicfDot11APUserSecAuthTypeStatisTable_Object = MibTable
hpnicfDot11APUserSecAuthTypeStatisTable = _HpnicfDot11APUserSecAuthTypeStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29)
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthTypeStatisTable.setStatus("current")
_HpnicfDot11APUserSecAuthTypeStatisEntry_Object = MibTableRow
hpnicfDot11APUserSecAuthTypeStatisEntry = _HpnicfDot11APUserSecAuthTypeStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1)
)
hpnicfDot11APUserSecAuthTypeStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthTypeStatisEntry.setStatus("current")
_HpnicfDot11APPortalOnlineUserNum_Type = Integer32
_HpnicfDot11APPortalOnlineUserNum_Object = MibTableColumn
hpnicfDot11APPortalOnlineUserNum = _HpnicfDot11APPortalOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 1),
    _HpnicfDot11APPortalOnlineUserNum_Type()
)
hpnicfDot11APPortalOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APPortalOnlineUserNum.setStatus("current")
_HpnicfDot11APAuthFreeOnlineUserNum_Type = Integer32
_HpnicfDot11APAuthFreeOnlineUserNum_Object = MibTableColumn
hpnicfDot11APAuthFreeOnlineUserNum = _HpnicfDot11APAuthFreeOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 2),
    _HpnicfDot11APAuthFreeOnlineUserNum_Type()
)
hpnicfDot11APAuthFreeOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFreeOnlineUserNum.setStatus("current")
_HpnicfDot11APAssocAuthOnlineUserNum_Type = Integer32
_HpnicfDot11APAssocAuthOnlineUserNum_Object = MibTableColumn
hpnicfDot11APAssocAuthOnlineUserNum = _HpnicfDot11APAssocAuthOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 3),
    _HpnicfDot11APAssocAuthOnlineUserNum_Type()
)
hpnicfDot11APAssocAuthOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocAuthOnlineUserNum.setStatus("current")
_HpnicfDot11APMacAuthOnlineUserNum_Type = Integer32
_HpnicfDot11APMacAuthOnlineUserNum_Object = MibTableColumn
hpnicfDot11APMacAuthOnlineUserNum = _HpnicfDot11APMacAuthOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 4),
    _HpnicfDot11APMacAuthOnlineUserNum_Type()
)
hpnicfDot11APMacAuthOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAuthOnlineUserNum.setStatus("current")
_HpnicfDot11APAllPortalUserOnlineTime_Type = TimeTicks
_HpnicfDot11APAllPortalUserOnlineTime_Object = MibTableColumn
hpnicfDot11APAllPortalUserOnlineTime = _HpnicfDot11APAllPortalUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 5),
    _HpnicfDot11APAllPortalUserOnlineTime_Type()
)
hpnicfDot11APAllPortalUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAllPortalUserOnlineTime.setStatus("current")
_HpnicfDot11APAllAuthFreeUserOnlineTime_Type = TimeTicks
_HpnicfDot11APAllAuthFreeUserOnlineTime_Object = MibTableColumn
hpnicfDot11APAllAuthFreeUserOnlineTime = _HpnicfDot11APAllAuthFreeUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 6),
    _HpnicfDot11APAllAuthFreeUserOnlineTime_Type()
)
hpnicfDot11APAllAuthFreeUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAllAuthFreeUserOnlineTime.setStatus("current")
_HpnicfDot11APAllAssocAuthUserOnlineTime_Type = TimeTicks
_HpnicfDot11APAllAssocAuthUserOnlineTime_Object = MibTableColumn
hpnicfDot11APAllAssocAuthUserOnlineTime = _HpnicfDot11APAllAssocAuthUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 7),
    _HpnicfDot11APAllAssocAuthUserOnlineTime_Type()
)
hpnicfDot11APAllAssocAuthUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAllAssocAuthUserOnlineTime.setStatus("current")
_HpnicfDot11APAllMacAuthUserOnlineTime_Type = TimeTicks
_HpnicfDot11APAllMacAuthUserOnlineTime_Object = MibTableColumn
hpnicfDot11APAllMacAuthUserOnlineTime = _HpnicfDot11APAllMacAuthUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 8),
    _HpnicfDot11APAllMacAuthUserOnlineTime_Type()
)
hpnicfDot11APAllMacAuthUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAllMacAuthUserOnlineTime.setStatus("current")
_HpnicfDot11APPortalUserLostCnntCnt_Type = Counter32
_HpnicfDot11APPortalUserLostCnntCnt_Object = MibTableColumn
hpnicfDot11APPortalUserLostCnntCnt = _HpnicfDot11APPortalUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 9),
    _HpnicfDot11APPortalUserLostCnntCnt_Type()
)
hpnicfDot11APPortalUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APPortalUserLostCnntCnt.setStatus("current")
_HpnicfDot11APAuthFreeUserLostCnntCnt_Type = Counter32
_HpnicfDot11APAuthFreeUserLostCnntCnt_Object = MibTableColumn
hpnicfDot11APAuthFreeUserLostCnntCnt = _HpnicfDot11APAuthFreeUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 10),
    _HpnicfDot11APAuthFreeUserLostCnntCnt_Type()
)
hpnicfDot11APAuthFreeUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAuthFreeUserLostCnntCnt.setStatus("current")
_HpnicfDot11APAssocAuthUserLostCnntCnt_Type = Counter32
_HpnicfDot11APAssocAuthUserLostCnntCnt_Object = MibTableColumn
hpnicfDot11APAssocAuthUserLostCnntCnt = _HpnicfDot11APAssocAuthUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 11),
    _HpnicfDot11APAssocAuthUserLostCnntCnt_Type()
)
hpnicfDot11APAssocAuthUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocAuthUserLostCnntCnt.setStatus("current")
_HpnicfDot11APMacAuthUserLostCnntCnt_Type = Counter32
_HpnicfDot11APMacAuthUserLostCnntCnt_Object = MibTableColumn
hpnicfDot11APMacAuthUserLostCnntCnt = _HpnicfDot11APMacAuthUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 12),
    _HpnicfDot11APMacAuthUserLostCnntCnt_Type()
)
hpnicfDot11APMacAuthUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAuthUserLostCnntCnt.setStatus("current")
_HpnicfDot11APPortalAuthReqCnt_Type = Counter32
_HpnicfDot11APPortalAuthReqCnt_Object = MibTableColumn
hpnicfDot11APPortalAuthReqCnt = _HpnicfDot11APPortalAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 13),
    _HpnicfDot11APPortalAuthReqCnt_Type()
)
hpnicfDot11APPortalAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APPortalAuthReqCnt.setStatus("current")
_HpnicfDot11APAssocAuthReqCnt_Type = Counter32
_HpnicfDot11APAssocAuthReqCnt_Object = MibTableColumn
hpnicfDot11APAssocAuthReqCnt = _HpnicfDot11APAssocAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 14),
    _HpnicfDot11APAssocAuthReqCnt_Type()
)
hpnicfDot11APAssocAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocAuthReqCnt.setStatus("current")
_HpnicfDot11APMacAuthReqCnt_Type = Counter32
_HpnicfDot11APMacAuthReqCnt_Object = MibTableColumn
hpnicfDot11APMacAuthReqCnt = _HpnicfDot11APMacAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 15),
    _HpnicfDot11APMacAuthReqCnt_Type()
)
hpnicfDot11APMacAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAuthReqCnt.setStatus("current")
_HpnicfDot11APPortalAuthSucCnt_Type = Counter32
_HpnicfDot11APPortalAuthSucCnt_Object = MibTableColumn
hpnicfDot11APPortalAuthSucCnt = _HpnicfDot11APPortalAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 16),
    _HpnicfDot11APPortalAuthSucCnt_Type()
)
hpnicfDot11APPortalAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APPortalAuthSucCnt.setStatus("current")
_HpnicfDot11APAssocAuthSucCnt_Type = Counter32
_HpnicfDot11APAssocAuthSucCnt_Object = MibTableColumn
hpnicfDot11APAssocAuthSucCnt = _HpnicfDot11APAssocAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 17),
    _HpnicfDot11APAssocAuthSucCnt_Type()
)
hpnicfDot11APAssocAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocAuthSucCnt.setStatus("current")
_HpnicfDot11APMacAuthSucCnt_Type = Counter32
_HpnicfDot11APMacAuthSucCnt_Object = MibTableColumn
hpnicfDot11APMacAuthSucCnt = _HpnicfDot11APMacAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 18),
    _HpnicfDot11APMacAuthSucCnt_Type()
)
hpnicfDot11APMacAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAuthSucCnt.setStatus("current")
_HpnicfDot11APPortalAuthReqFailCnt_Type = Counter32
_HpnicfDot11APPortalAuthReqFailCnt_Object = MibTableColumn
hpnicfDot11APPortalAuthReqFailCnt = _HpnicfDot11APPortalAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 19),
    _HpnicfDot11APPortalAuthReqFailCnt_Type()
)
hpnicfDot11APPortalAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APPortalAuthReqFailCnt.setStatus("current")
_HpnicfDot11APAssocAuthReqFailCnt_Type = Counter32
_HpnicfDot11APAssocAuthReqFailCnt_Object = MibTableColumn
hpnicfDot11APAssocAuthReqFailCnt = _HpnicfDot11APAssocAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 20),
    _HpnicfDot11APAssocAuthReqFailCnt_Type()
)
hpnicfDot11APAssocAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAssocAuthReqFailCnt.setStatus("current")
_HpnicfDot11APMacAuthReqFailCnt_Type = Counter32
_HpnicfDot11APMacAuthReqFailCnt_Object = MibTableColumn
hpnicfDot11APMacAuthReqFailCnt = _HpnicfDot11APMacAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 21),
    _HpnicfDot11APMacAuthReqFailCnt_Type()
)
hpnicfDot11APMacAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APMacAuthReqFailCnt.setStatus("current")
_HpnicfDot11APAutoAuthOnlineUserNumCM_Type = Integer32
_HpnicfDot11APAutoAuthOnlineUserNumCM_Object = MibTableColumn
hpnicfDot11APAutoAuthOnlineUserNumCM = _HpnicfDot11APAutoAuthOnlineUserNumCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 22),
    _HpnicfDot11APAutoAuthOnlineUserNumCM_Type()
)
hpnicfDot11APAutoAuthOnlineUserNumCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAutoAuthOnlineUserNumCM.setStatus("current")
_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Type = TimeTicks
_HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Object = MibTableColumn
hpnicfDot11APAllAutoAuthUserOnlineTimeCM = _HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 23),
    _HpnicfDot11APAllAutoAuthUserOnlineTimeCM_Type()
)
hpnicfDot11APAllAutoAuthUserOnlineTimeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAllAutoAuthUserOnlineTimeCM.setStatus("current")
_HpnicfDot11APAutoAuthUserLostCnntCntCM_Type = Counter32
_HpnicfDot11APAutoAuthUserLostCnntCntCM_Object = MibTableColumn
hpnicfDot11APAutoAuthUserLostCnntCntCM = _HpnicfDot11APAutoAuthUserLostCnntCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 24),
    _HpnicfDot11APAutoAuthUserLostCnntCntCM_Type()
)
hpnicfDot11APAutoAuthUserLostCnntCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAutoAuthUserLostCnntCntCM.setStatus("current")
_HpnicfDot11APAutoAuthReqCntCM_Type = Counter32
_HpnicfDot11APAutoAuthReqCntCM_Object = MibTableColumn
hpnicfDot11APAutoAuthReqCntCM = _HpnicfDot11APAutoAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 25),
    _HpnicfDot11APAutoAuthReqCntCM_Type()
)
hpnicfDot11APAutoAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAutoAuthReqCntCM.setStatus("current")
_HpnicfDot11APAutoAuthSucCntCM_Type = Counter32
_HpnicfDot11APAutoAuthSucCntCM_Object = MibTableColumn
hpnicfDot11APAutoAuthSucCntCM = _HpnicfDot11APAutoAuthSucCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 26),
    _HpnicfDot11APAutoAuthSucCntCM_Type()
)
hpnicfDot11APAutoAuthSucCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAutoAuthSucCntCM.setStatus("current")
_HpnicfDot11APAutoAuthReqFailCntCM_Type = Counter32
_HpnicfDot11APAutoAuthReqFailCntCM_Object = MibTableColumn
hpnicfDot11APAutoAuthReqFailCntCM = _HpnicfDot11APAutoAuthReqFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 29, 1, 27),
    _HpnicfDot11APAutoAuthReqFailCntCM_Type()
)
hpnicfDot11APAutoAuthReqFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APAutoAuthReqFailCntCM.setStatus("current")
_HpnicfDot11RadioRxStatis64Table_Object = MibTable
hpnicfDot11RadioRxStatis64Table = _HpnicfDot11RadioRxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioRxStatis64Table.setStatus("current")
_HpnicfDot11RadioRxStatis64Entry_Object = MibTableRow
hpnicfDot11RadioRxStatis64Entry = _HpnicfDot11RadioRxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1)
)
hpnicfDot11RadioRxStatis64Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioRxStatis64Entry.setStatus("current")
_HpnicfDot11Rx64FrameDupCnt_Type = Counter64
_HpnicfDot11Rx64FrameDupCnt_Object = MibTableColumn
hpnicfDot11Rx64FrameDupCnt = _HpnicfDot11Rx64FrameDupCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 1),
    _HpnicfDot11Rx64FrameDupCnt_Type()
)
hpnicfDot11Rx64FrameDupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64FrameDupCnt.setStatus("current")
_HpnicfDot11Rx64FrameCnt_Type = Counter64
_HpnicfDot11Rx64FrameCnt_Object = MibTableColumn
hpnicfDot11Rx64FrameCnt = _HpnicfDot11Rx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 2),
    _HpnicfDot11Rx64FrameCnt_Type()
)
hpnicfDot11Rx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64FrameCnt.setStatus("current")
_HpnicfDot11Rx64UcastFrameCnt_Type = Counter64
_HpnicfDot11Rx64UcastFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64UcastFrameCnt = _HpnicfDot11Rx64UcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 3),
    _HpnicfDot11Rx64UcastFrameCnt_Type()
)
hpnicfDot11Rx64UcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64UcastFrameCnt.setStatus("current")
_HpnicfDot11Rx64BcastFrameCnt_Type = Counter64
_HpnicfDot11Rx64BcastFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64BcastFrameCnt = _HpnicfDot11Rx64BcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 4),
    _HpnicfDot11Rx64BcastFrameCnt_Type()
)
hpnicfDot11Rx64BcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64BcastFrameCnt.setStatus("current")
_HpnicfDot11Rx64McastFrameCnt_Type = Counter64
_HpnicfDot11Rx64McastFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64McastFrameCnt = _HpnicfDot11Rx64McastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 5),
    _HpnicfDot11Rx64McastFrameCnt_Type()
)
hpnicfDot11Rx64McastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64McastFrameCnt.setStatus("current")
_HpnicfDot11Rx64DiscardFrameCnt_Type = Counter64
_HpnicfDot11Rx64DiscardFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64DiscardFrameCnt = _HpnicfDot11Rx64DiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 6),
    _HpnicfDot11Rx64DiscardFrameCnt_Type()
)
hpnicfDot11Rx64DiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DiscardFrameCnt.setStatus("current")
_HpnicfDot11Rx64FragCnt_Type = Counter64
_HpnicfDot11Rx64FragCnt_Object = MibTableColumn
hpnicfDot11Rx64FragCnt = _HpnicfDot11Rx64FragCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 7),
    _HpnicfDot11Rx64FragCnt_Type()
)
hpnicfDot11Rx64FragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64FragCnt.setStatus("current")
_HpnicfDot11Rx64FcsErrCnt_Type = Counter64
_HpnicfDot11Rx64FcsErrCnt_Object = MibTableColumn
hpnicfDot11Rx64FcsErrCnt = _HpnicfDot11Rx64FcsErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 8),
    _HpnicfDot11Rx64FcsErrCnt_Type()
)
hpnicfDot11Rx64FcsErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64FcsErrCnt.setStatus("current")
_HpnicfDot11Rx64FrameBytes_Type = Counter64
_HpnicfDot11Rx64FrameBytes_Object = MibTableColumn
hpnicfDot11Rx64FrameBytes = _HpnicfDot11Rx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 9),
    _HpnicfDot11Rx64FrameBytes_Type()
)
hpnicfDot11Rx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64FrameBytes.setStatus("current")
_HpnicfDot11Rx64UcastFrameBytes_Type = Counter64
_HpnicfDot11Rx64UcastFrameBytes_Object = MibTableColumn
hpnicfDot11Rx64UcastFrameBytes = _HpnicfDot11Rx64UcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 10),
    _HpnicfDot11Rx64UcastFrameBytes_Type()
)
hpnicfDot11Rx64UcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64UcastFrameBytes.setStatus("current")
_HpnicfDot11Rx64BcastFrameBytes_Type = Counter64
_HpnicfDot11Rx64BcastFrameBytes_Object = MibTableColumn
hpnicfDot11Rx64BcastFrameBytes = _HpnicfDot11Rx64BcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 11),
    _HpnicfDot11Rx64BcastFrameBytes_Type()
)
hpnicfDot11Rx64BcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64BcastFrameBytes.setStatus("current")
_HpnicfDot11Rx64McastFrameBytes_Type = Counter64
_HpnicfDot11Rx64McastFrameBytes_Object = MibTableColumn
hpnicfDot11Rx64McastFrameBytes = _HpnicfDot11Rx64McastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 12),
    _HpnicfDot11Rx64McastFrameBytes_Type()
)
hpnicfDot11Rx64McastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64McastFrameBytes.setStatus("current")
_HpnicfDot11Rx64DiscardFrameBytes_Type = Counter64
_HpnicfDot11Rx64DiscardFrameBytes_Object = MibTableColumn
hpnicfDot11Rx64DiscardFrameBytes = _HpnicfDot11Rx64DiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 13),
    _HpnicfDot11Rx64DiscardFrameBytes_Type()
)
hpnicfDot11Rx64DiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DiscardFrameBytes.setStatus("current")
_HpnicfDot11Rx64MgmtFrameCnt_Type = Counter64
_HpnicfDot11Rx64MgmtFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64MgmtFrameCnt = _HpnicfDot11Rx64MgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 14),
    _HpnicfDot11Rx64MgmtFrameCnt_Type()
)
hpnicfDot11Rx64MgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64MgmtFrameCnt.setStatus("current")
_HpnicfDot11Rx64CtrlFrameCnt_Type = Counter64
_HpnicfDot11Rx64CtrlFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64CtrlFrameCnt = _HpnicfDot11Rx64CtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 15),
    _HpnicfDot11Rx64CtrlFrameCnt_Type()
)
hpnicfDot11Rx64CtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64CtrlFrameCnt.setStatus("current")
_HpnicfDot11Rx64DataFrameCnt_Type = Counter64
_HpnicfDot11Rx64DataFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64DataFrameCnt = _HpnicfDot11Rx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 16),
    _HpnicfDot11Rx64DataFrameCnt_Type()
)
hpnicfDot11Rx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DataFrameCnt.setStatus("current")
_HpnicfDot11Rx64DecryptErrorCnt_Type = Counter64
_HpnicfDot11Rx64DecryptErrorCnt_Object = MibTableColumn
hpnicfDot11Rx64DecryptErrorCnt = _HpnicfDot11Rx64DecryptErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 17),
    _HpnicfDot11Rx64DecryptErrorCnt_Type()
)
hpnicfDot11Rx64DecryptErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DecryptErrorCnt.setStatus("current")
_HpnicfDot11Rx64AuthenFrameCnt_Type = Counter64
_HpnicfDot11Rx64AuthenFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64AuthenFrameCnt = _HpnicfDot11Rx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 18),
    _HpnicfDot11Rx64AuthenFrameCnt_Type()
)
hpnicfDot11Rx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64AuthenFrameCnt.setStatus("current")
_HpnicfDot11Rx64AssociateFrameCnt_Type = Counter64
_HpnicfDot11Rx64AssociateFrameCnt_Object = MibTableColumn
hpnicfDot11Rx64AssociateFrameCnt = _HpnicfDot11Rx64AssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 19),
    _HpnicfDot11Rx64AssociateFrameCnt_Type()
)
hpnicfDot11Rx64AssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64AssociateFrameCnt.setStatus("current")
_HpnicfDot11Rx64PhyErrorCnt_Type = Counter64
_HpnicfDot11Rx64PhyErrorCnt_Object = MibTableColumn
hpnicfDot11Rx64PhyErrorCnt = _HpnicfDot11Rx64PhyErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 20),
    _HpnicfDot11Rx64PhyErrorCnt_Type()
)
hpnicfDot11Rx64PhyErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64PhyErrorCnt.setStatus("current")
_HpnicfDot11Rx64MICErrorCnt_Type = Counter64
_HpnicfDot11Rx64MICErrorCnt_Object = MibTableColumn
hpnicfDot11Rx64MICErrorCnt = _HpnicfDot11Rx64MICErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 21),
    _HpnicfDot11Rx64MICErrorCnt_Type()
)
hpnicfDot11Rx64MICErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64MICErrorCnt.setStatus("current")
_HpnicfDot11Rx64DataFrameBytes_Type = Counter64
_HpnicfDot11Rx64DataFrameBytes_Object = MibTableColumn
hpnicfDot11Rx64DataFrameBytes = _HpnicfDot11Rx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 22),
    _HpnicfDot11Rx64DataFrameBytes_Type()
)
hpnicfDot11Rx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DataFrameBytes.setStatus("current")
_HpnicfDot11Rx64PayloadBytes_Type = Counter64
_HpnicfDot11Rx64PayloadBytes_Object = MibTableColumn
hpnicfDot11Rx64PayloadBytes = _HpnicfDot11Rx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 23),
    _HpnicfDot11Rx64PayloadBytes_Type()
)
hpnicfDot11Rx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64PayloadBytes.setStatus("current")
_HpnicfDot11Rx64DataFrameBytesCM_Type = Counter64
_HpnicfDot11Rx64DataFrameBytesCM_Object = MibTableColumn
hpnicfDot11Rx64DataFrameBytesCM = _HpnicfDot11Rx64DataFrameBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 30, 1, 24),
    _HpnicfDot11Rx64DataFrameBytesCM_Type()
)
hpnicfDot11Rx64DataFrameBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Rx64DataFrameBytesCM.setStatus("current")
_HpnicfDot11RadioTxStatis64Table_Object = MibTable
hpnicfDot11RadioTxStatis64Table = _HpnicfDot11RadioTxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioTxStatis64Table.setStatus("current")
_HpnicfDot11RadioTxStatis64Entry_Object = MibTableRow
hpnicfDot11RadioTxStatis64Entry = _HpnicfDot11RadioTxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1)
)
hpnicfDot11RadioTxStatis64Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioTxStatis64Entry.setStatus("current")
_HpnicfDot11Tx64FragCnt_Type = Counter64
_HpnicfDot11Tx64FragCnt_Object = MibTableColumn
hpnicfDot11Tx64FragCnt = _HpnicfDot11Tx64FragCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 1),
    _HpnicfDot11Tx64FragCnt_Type()
)
hpnicfDot11Tx64FragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64FragCnt.setStatus("current")
_HpnicfDot11Tx64FailedCnt_Type = Counter64
_HpnicfDot11Tx64FailedCnt_Object = MibTableColumn
hpnicfDot11Tx64FailedCnt = _HpnicfDot11Tx64FailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 2),
    _HpnicfDot11Tx64FailedCnt_Type()
)
hpnicfDot11Tx64FailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64FailedCnt.setStatus("current")
_HpnicfDot11Tx64RetryCnt_Type = Counter64
_HpnicfDot11Tx64RetryCnt_Object = MibTableColumn
hpnicfDot11Tx64RetryCnt = _HpnicfDot11Tx64RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 3),
    _HpnicfDot11Tx64RetryCnt_Type()
)
hpnicfDot11Tx64RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64RetryCnt.setStatus("current")
_HpnicfDot11Tx64MultiRetryCnt_Type = Counter64
_HpnicfDot11Tx64MultiRetryCnt_Object = MibTableColumn
hpnicfDot11Tx64MultiRetryCnt = _HpnicfDot11Tx64MultiRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 4),
    _HpnicfDot11Tx64MultiRetryCnt_Type()
)
hpnicfDot11Tx64MultiRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64MultiRetryCnt.setStatus("current")
_HpnicfDot11Tx64RtsSuccessCnt_Type = Counter64
_HpnicfDot11Tx64RtsSuccessCnt_Object = MibTableColumn
hpnicfDot11Tx64RtsSuccessCnt = _HpnicfDot11Tx64RtsSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 5),
    _HpnicfDot11Tx64RtsSuccessCnt_Type()
)
hpnicfDot11Tx64RtsSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64RtsSuccessCnt.setStatus("current")
_HpnicfDot11Tx64RtsFailCnt_Type = Counter64
_HpnicfDot11Tx64RtsFailCnt_Object = MibTableColumn
hpnicfDot11Tx64RtsFailCnt = _HpnicfDot11Tx64RtsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 6),
    _HpnicfDot11Tx64RtsFailCnt_Type()
)
hpnicfDot11Tx64RtsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64RtsFailCnt.setStatus("current")
_HpnicfDot11Tx64AckFailCnt_Type = Counter64
_HpnicfDot11Tx64AckFailCnt_Object = MibTableColumn
hpnicfDot11Tx64AckFailCnt = _HpnicfDot11Tx64AckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 7),
    _HpnicfDot11Tx64AckFailCnt_Type()
)
hpnicfDot11Tx64AckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64AckFailCnt.setStatus("current")
_HpnicfDot11Tx64FrameCnt_Type = Counter64
_HpnicfDot11Tx64FrameCnt_Object = MibTableColumn
hpnicfDot11Tx64FrameCnt = _HpnicfDot11Tx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 8),
    _HpnicfDot11Tx64FrameCnt_Type()
)
hpnicfDot11Tx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64FrameCnt.setStatus("current")
_HpnicfDot11Tx64UcastFrameCnt_Type = Counter64
_HpnicfDot11Tx64UcastFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64UcastFrameCnt = _HpnicfDot11Tx64UcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 9),
    _HpnicfDot11Tx64UcastFrameCnt_Type()
)
hpnicfDot11Tx64UcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64UcastFrameCnt.setStatus("current")
_HpnicfDot11Tx64BcastFrameCnt_Type = Counter64
_HpnicfDot11Tx64BcastFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64BcastFrameCnt = _HpnicfDot11Tx64BcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 10),
    _HpnicfDot11Tx64BcastFrameCnt_Type()
)
hpnicfDot11Tx64BcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64BcastFrameCnt.setStatus("current")
_HpnicfDot11Tx64McastFrameCnt_Type = Counter64
_HpnicfDot11Tx64McastFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64McastFrameCnt = _HpnicfDot11Tx64McastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 11),
    _HpnicfDot11Tx64McastFrameCnt_Type()
)
hpnicfDot11Tx64McastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64McastFrameCnt.setStatus("current")
_HpnicfDot11Tx64DiscardFrameCnt_Type = Counter64
_HpnicfDot11Tx64DiscardFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64DiscardFrameCnt = _HpnicfDot11Tx64DiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 12),
    _HpnicfDot11Tx64DiscardFrameCnt_Type()
)
hpnicfDot11Tx64DiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64DiscardFrameCnt.setStatus("current")
_HpnicfDot11Tx64FrameBytes_Type = Counter64
_HpnicfDot11Tx64FrameBytes_Object = MibTableColumn
hpnicfDot11Tx64FrameBytes = _HpnicfDot11Tx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 13),
    _HpnicfDot11Tx64FrameBytes_Type()
)
hpnicfDot11Tx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64FrameBytes.setStatus("current")
_HpnicfDot11Tx64UcastFrameBytes_Type = Counter64
_HpnicfDot11Tx64UcastFrameBytes_Object = MibTableColumn
hpnicfDot11Tx64UcastFrameBytes = _HpnicfDot11Tx64UcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 14),
    _HpnicfDot11Tx64UcastFrameBytes_Type()
)
hpnicfDot11Tx64UcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64UcastFrameBytes.setStatus("current")
_HpnicfDot11Tx64BcastFrameBytes_Type = Counter64
_HpnicfDot11Tx64BcastFrameBytes_Object = MibTableColumn
hpnicfDot11Tx64BcastFrameBytes = _HpnicfDot11Tx64BcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 15),
    _HpnicfDot11Tx64BcastFrameBytes_Type()
)
hpnicfDot11Tx64BcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64BcastFrameBytes.setStatus("current")
_HpnicfDot11Tx64McastFrameBytes_Type = Counter64
_HpnicfDot11Tx64McastFrameBytes_Object = MibTableColumn
hpnicfDot11Tx64McastFrameBytes = _HpnicfDot11Tx64McastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 16),
    _HpnicfDot11Tx64McastFrameBytes_Type()
)
hpnicfDot11Tx64McastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64McastFrameBytes.setStatus("current")
_HpnicfDot11Tx64DiscardFrameBytes_Type = Counter64
_HpnicfDot11Tx64DiscardFrameBytes_Object = MibTableColumn
hpnicfDot11Tx64DiscardFrameBytes = _HpnicfDot11Tx64DiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 17),
    _HpnicfDot11Tx64DiscardFrameBytes_Type()
)
hpnicfDot11Tx64DiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64DiscardFrameBytes.setStatus("current")
_HpnicfDot11Tx64AuthenFrameCnt_Type = Counter64
_HpnicfDot11Tx64AuthenFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64AuthenFrameCnt = _HpnicfDot11Tx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 18),
    _HpnicfDot11Tx64AuthenFrameCnt_Type()
)
hpnicfDot11Tx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64AuthenFrameCnt.setStatus("current")
_HpnicfDot11Tx64AssociateFrameCnt_Type = Counter64
_HpnicfDot11Tx64AssociateFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64AssociateFrameCnt = _HpnicfDot11Tx64AssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 19),
    _HpnicfDot11Tx64AssociateFrameCnt_Type()
)
hpnicfDot11Tx64AssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64AssociateFrameCnt.setStatus("current")
_HpnicfDot11Tx64DataFrameCnt_Type = Counter64
_HpnicfDot11Tx64DataFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64DataFrameCnt = _HpnicfDot11Tx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 20),
    _HpnicfDot11Tx64DataFrameCnt_Type()
)
hpnicfDot11Tx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64DataFrameCnt.setStatus("current")
_HpnicfDot11Tx64DataFrameBytes_Type = Counter64
_HpnicfDot11Tx64DataFrameBytes_Object = MibTableColumn
hpnicfDot11Tx64DataFrameBytes = _HpnicfDot11Tx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 21),
    _HpnicfDot11Tx64DataFrameBytes_Type()
)
hpnicfDot11Tx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64DataFrameBytes.setStatus("current")
_HpnicfDot11Tx64MSDUCnt_Type = Counter64
_HpnicfDot11Tx64MSDUCnt_Object = MibTableColumn
hpnicfDot11Tx64MSDUCnt = _HpnicfDot11Tx64MSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 22),
    _HpnicfDot11Tx64MSDUCnt_Type()
)
hpnicfDot11Tx64MSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64MSDUCnt.setStatus("current")
_HpnicfDot11Tx64DiscardMSDUCnt_Type = Counter64
_HpnicfDot11Tx64DiscardMSDUCnt_Object = MibTableColumn
hpnicfDot11Tx64DiscardMSDUCnt = _HpnicfDot11Tx64DiscardMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 23),
    _HpnicfDot11Tx64DiscardMSDUCnt_Type()
)
hpnicfDot11Tx64DiscardMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64DiscardMSDUCnt.setStatus("current")
_HpnicfDot11Tx64RetryMSDUCnt_Type = Counter64
_HpnicfDot11Tx64RetryMSDUCnt_Object = MibTableColumn
hpnicfDot11Tx64RetryMSDUCnt = _HpnicfDot11Tx64RetryMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 24),
    _HpnicfDot11Tx64RetryMSDUCnt_Type()
)
hpnicfDot11Tx64RetryMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64RetryMSDUCnt.setStatus("current")
_HpnicfDot11Tx64PayloadBytes_Type = Counter64
_HpnicfDot11Tx64PayloadBytes_Object = MibTableColumn
hpnicfDot11Tx64PayloadBytes = _HpnicfDot11Tx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 25),
    _HpnicfDot11Tx64PayloadBytes_Type()
)
hpnicfDot11Tx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64PayloadBytes.setStatus("current")
_HpnicfDot11Tx64MgtFrameCnt_Type = Counter64
_HpnicfDot11Tx64MgtFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64MgtFrameCnt = _HpnicfDot11Tx64MgtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 26),
    _HpnicfDot11Tx64MgtFrameCnt_Type()
)
hpnicfDot11Tx64MgtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64MgtFrameCnt.setStatus("current")
_HpnicfDot11Tx64CtrlFrameCnt_Type = Counter64
_HpnicfDot11Tx64CtrlFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64CtrlFrameCnt = _HpnicfDot11Tx64CtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 27),
    _HpnicfDot11Tx64CtrlFrameCnt_Type()
)
hpnicfDot11Tx64CtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64CtrlFrameCnt.setStatus("current")
_HpnicfDot11Tx64MACErrCnt_Type = Counter64
_HpnicfDot11Tx64MACErrCnt_Object = MibTableColumn
hpnicfDot11Tx64MACErrCnt = _HpnicfDot11Tx64MACErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 28),
    _HpnicfDot11Tx64MACErrCnt_Type()
)
hpnicfDot11Tx64MACErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64MACErrCnt.setStatus("current")
_HpnicfDot11Tx64ErrFrameCnt_Type = Counter64
_HpnicfDot11Tx64ErrFrameCnt_Object = MibTableColumn
hpnicfDot11Tx64ErrFrameCnt = _HpnicfDot11Tx64ErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 31, 1, 29),
    _HpnicfDot11Tx64ErrFrameCnt_Type()
)
hpnicfDot11Tx64ErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11Tx64ErrFrameCnt.setStatus("current")
_HpnicfDot11BSSRxStatis64Table_Object = MibTable
hpnicfDot11BSSRxStatis64Table = _HpnicfDot11BSSRxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32)
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxStatis64Table.setStatus("current")
_HpnicfDot11BSSRxStatis64Entry_Object = MibTableRow
hpnicfDot11BSSRxStatis64Entry = _HpnicfDot11BSSRxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1)
)
hpnicfDot11BSSRxStatis64Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSRxStatis64Entry.setStatus("current")
_HpnicfDot11BSSRx64FrameCnt_Type = Counter64
_HpnicfDot11BSSRx64FrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64FrameCnt = _HpnicfDot11BSSRx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 1),
    _HpnicfDot11BSSRx64FrameCnt_Type()
)
hpnicfDot11BSSRx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64FrameCnt.setStatus("current")
_HpnicfDot11BSSRx64FrameBytes_Type = Counter64
_HpnicfDot11BSSRx64FrameBytes_Object = MibTableColumn
hpnicfDot11BSSRx64FrameBytes = _HpnicfDot11BSSRx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 2),
    _HpnicfDot11BSSRx64FrameBytes_Type()
)
hpnicfDot11BSSRx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64FrameBytes.setStatus("current")
_HpnicfDot11BSSRx64DataFrameCnt_Type = Counter64
_HpnicfDot11BSSRx64DataFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64DataFrameCnt = _HpnicfDot11BSSRx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 3),
    _HpnicfDot11BSSRx64DataFrameCnt_Type()
)
hpnicfDot11BSSRx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64DataFrameCnt.setStatus("current")
_HpnicfDot11BSSRx64DataFrameBytes_Type = Counter64
_HpnicfDot11BSSRx64DataFrameBytes_Object = MibTableColumn
hpnicfDot11BSSRx64DataFrameBytes = _HpnicfDot11BSSRx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 4),
    _HpnicfDot11BSSRx64DataFrameBytes_Type()
)
hpnicfDot11BSSRx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64DataFrameBytes.setStatus("current")
_HpnicfDot11BSSRx64AssocFrameCnt_Type = Counter64
_HpnicfDot11BSSRx64AssocFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64AssocFrameCnt = _HpnicfDot11BSSRx64AssocFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 5),
    _HpnicfDot11BSSRx64AssocFrameCnt_Type()
)
hpnicfDot11BSSRx64AssocFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64AssocFrameCnt.setStatus("current")
_HpnicfDot11BSSRx64PayloadBytes_Type = Counter64
_HpnicfDot11BSSRx64PayloadBytes_Object = MibTableColumn
hpnicfDot11BSSRx64PayloadBytes = _HpnicfDot11BSSRx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 6),
    _HpnicfDot11BSSRx64PayloadBytes_Type()
)
hpnicfDot11BSSRx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64PayloadBytes.setStatus("current")
_HpnicfDot11BSSRx64UniFrameCnt_Type = Counter64
_HpnicfDot11BSSRx64UniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64UniFrameCnt = _HpnicfDot11BSSRx64UniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 7),
    _HpnicfDot11BSSRx64UniFrameCnt_Type()
)
hpnicfDot11BSSRx64UniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64UniFrameCnt.setStatus("current")
_HpnicfDot11BSSRx64NonUniFrameCnt_Type = Counter64
_HpnicfDot11BSSRx64NonUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64NonUniFrameCnt = _HpnicfDot11BSSRx64NonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 8),
    _HpnicfDot11BSSRx64NonUniFrameCnt_Type()
)
hpnicfDot11BSSRx64NonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64NonUniFrameCnt.setStatus("current")
_HpnicfDot11BSSRx64AuthenFrameCnt_Type = Counter64
_HpnicfDot11BSSRx64AuthenFrameCnt_Object = MibTableColumn
hpnicfDot11BSSRx64AuthenFrameCnt = _HpnicfDot11BSSRx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 32, 1, 9),
    _HpnicfDot11BSSRx64AuthenFrameCnt_Type()
)
hpnicfDot11BSSRx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSRx64AuthenFrameCnt.setStatus("current")
_HpnicfDot11BSSTxStatis64Table_Object = MibTable
hpnicfDot11BSSTxStatis64Table = _HpnicfDot11BSSTxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33)
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxStatis64Table.setStatus("current")
_HpnicfDot11BSSTxStatis64Entry_Object = MibTableRow
hpnicfDot11BSSTxStatis64Entry = _HpnicfDot11BSSTxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1)
)
hpnicfDot11BSSTxStatis64Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11BSSTxStatis64Entry.setStatus("current")
_HpnicfDot11BSSTx64FrameCnt_Type = Counter64
_HpnicfDot11BSSTx64FrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64FrameCnt = _HpnicfDot11BSSTx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 1),
    _HpnicfDot11BSSTx64FrameCnt_Type()
)
hpnicfDot11BSSTx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64FrameCnt.setStatus("current")
_HpnicfDot11BSSTx64FrameBytes_Type = Counter64
_HpnicfDot11BSSTx64FrameBytes_Object = MibTableColumn
hpnicfDot11BSSTx64FrameBytes = _HpnicfDot11BSSTx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 2),
    _HpnicfDot11BSSTx64FrameBytes_Type()
)
hpnicfDot11BSSTx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64FrameBytes.setStatus("current")
_HpnicfDot11BSSTx64DataFrameCnt_Type = Counter64
_HpnicfDot11BSSTx64DataFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64DataFrameCnt = _HpnicfDot11BSSTx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 3),
    _HpnicfDot11BSSTx64DataFrameCnt_Type()
)
hpnicfDot11BSSTx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64DataFrameCnt.setStatus("current")
_HpnicfDot11BSSTx64DataFrameBytes_Type = Counter64
_HpnicfDot11BSSTx64DataFrameBytes_Object = MibTableColumn
hpnicfDot11BSSTx64DataFrameBytes = _HpnicfDot11BSSTx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 4),
    _HpnicfDot11BSSTx64DataFrameBytes_Type()
)
hpnicfDot11BSSTx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64DataFrameBytes.setStatus("current")
_HpnicfDot11BSSTx64AssocFrameCnt_Type = Counter64
_HpnicfDot11BSSTx64AssocFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64AssocFrameCnt = _HpnicfDot11BSSTx64AssocFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 5),
    _HpnicfDot11BSSTx64AssocFrameCnt_Type()
)
hpnicfDot11BSSTx64AssocFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64AssocFrameCnt.setStatus("current")
_HpnicfDot11BSSTx64PayloadBytes_Type = Counter64
_HpnicfDot11BSSTx64PayloadBytes_Object = MibTableColumn
hpnicfDot11BSSTx64PayloadBytes = _HpnicfDot11BSSTx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 6),
    _HpnicfDot11BSSTx64PayloadBytes_Type()
)
hpnicfDot11BSSTx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64PayloadBytes.setStatus("current")
_HpnicfDot11BSSTx64RetryCnt_Type = Counter64
_HpnicfDot11BSSTx64RetryCnt_Object = MibTableColumn
hpnicfDot11BSSTx64RetryCnt = _HpnicfDot11BSSTx64RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 7),
    _HpnicfDot11BSSTx64RetryCnt_Type()
)
hpnicfDot11BSSTx64RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64RetryCnt.setStatus("current")
_HpnicfDot11BSSTx64UniFrameCnt_Type = Counter64
_HpnicfDot11BSSTx64UniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64UniFrameCnt = _HpnicfDot11BSSTx64UniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 8),
    _HpnicfDot11BSSTx64UniFrameCnt_Type()
)
hpnicfDot11BSSTx64UniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64UniFrameCnt.setStatus("current")
_HpnicfDot11BSSTx64NonUniFrameCnt_Type = Counter64
_HpnicfDot11BSSTx64NonUniFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64NonUniFrameCnt = _HpnicfDot11BSSTx64NonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 9),
    _HpnicfDot11BSSTx64NonUniFrameCnt_Type()
)
hpnicfDot11BSSTx64NonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64NonUniFrameCnt.setStatus("current")
_HpnicfDot11BSSTx64AuthenFrameCnt_Type = Counter64
_HpnicfDot11BSSTx64AuthenFrameCnt_Object = MibTableColumn
hpnicfDot11BSSTx64AuthenFrameCnt = _HpnicfDot11BSSTx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 33, 1, 10),
    _HpnicfDot11BSSTx64AuthenFrameCnt_Type()
)
hpnicfDot11BSSTx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11BSSTx64AuthenFrameCnt.setStatus("current")
_HpnicfDot11APPacketMCSRateStatis2Table_Object = MibTable
hpnicfDot11APPacketMCSRateStatis2Table = _HpnicfDot11APPacketMCSRateStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 34)
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCSRateStatis2Table.setStatus("current")
_HpnicfDot11APPacketMCSRateStatis2Entry_Object = MibTableRow
hpnicfDot11APPacketMCSRateStatis2Entry = _HpnicfDot11APPacketMCSRateStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 34, 1)
)
hpnicfDot11APPacketMCSRateStatis2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APPacketMCS2Rate"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCSRateStatis2Entry.setStatus("current")


class _HpnicfDot11APPacketMCS2Rate_Type(Integer32):
    """Custom type hpnicfDot11APPacketMCS2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_HpnicfDot11APPacketMCS2Rate_Type.__name__ = "Integer32"
_HpnicfDot11APPacketMCS2Rate_Object = MibTableColumn
hpnicfDot11APPacketMCS2Rate = _HpnicfDot11APPacketMCS2Rate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 34, 1, 1),
    _HpnicfDot11APPacketMCS2Rate_Type()
)
hpnicfDot11APPacketMCS2Rate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APPacketMCS2Rate.setStatus("current")
_HpnicfDot11APRXPacketMCSRate2Count_Type = Counter64
_HpnicfDot11APRXPacketMCSRate2Count_Object = MibTableColumn
hpnicfDot11APRXPacketMCSRate2Count = _HpnicfDot11APRXPacketMCSRate2Count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 34, 1, 2),
    _HpnicfDot11APRXPacketMCSRate2Count_Type()
)
hpnicfDot11APRXPacketMCSRate2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APRXPacketMCSRate2Count.setStatus("current")
_HpnicfDot11APTXPacketMCSRate2Count_Type = Counter64
_HpnicfDot11APTXPacketMCSRate2Count_Object = MibTableColumn
hpnicfDot11APTXPacketMCSRate2Count = _HpnicfDot11APTXPacketMCSRate2Count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 34, 1, 3),
    _HpnicfDot11APTXPacketMCSRate2Count_Type()
)
hpnicfDot11APTXPacketMCSRate2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APTXPacketMCSRate2Count.setStatus("current")
_HpnicfDot11APUserSecAuthStatisCMTable_Object = MibTable
hpnicfDot11APUserSecAuthStatisCMTable = _HpnicfDot11APUserSecAuthStatisCMTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35)
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthStatisCMTable.setStatus("current")
_HpnicfDot11APUserSecAuthStatisCMEntry_Object = MibTableRow
hpnicfDot11APUserSecAuthStatisCMEntry = _HpnicfDot11APUserSecAuthStatisCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1)
)
hpnicfDot11APUserSecAuthStatisCMEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurAPID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
    (0, "HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11WlanID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APUserSecAuthStatisCMEntry.setStatus("current")
_HpnicfDot11APUserConnFailCntCM_Type = Counter32
_HpnicfDot11APUserConnFailCntCM_Object = MibTableColumn
hpnicfDot11APUserConnFailCntCM = _HpnicfDot11APUserConnFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1, 1),
    _HpnicfDot11APUserConnFailCntCM_Type()
)
hpnicfDot11APUserConnFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserConnFailCntCM.setStatus("current")
_HpnicfDot11APUserAuthReqCntCM_Type = Counter32
_HpnicfDot11APUserAuthReqCntCM_Object = MibTableColumn
hpnicfDot11APUserAuthReqCntCM = _HpnicfDot11APUserAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1, 2),
    _HpnicfDot11APUserAuthReqCntCM_Type()
)
hpnicfDot11APUserAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthReqCntCM.setStatus("current")
_HpnicfDot11APUserAuthSuccCntCM_Type = Counter32
_HpnicfDot11APUserAuthSuccCntCM_Object = MibTableColumn
hpnicfDot11APUserAuthSuccCntCM = _HpnicfDot11APUserAuthSuccCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1, 3),
    _HpnicfDot11APUserAuthSuccCntCM_Type()
)
hpnicfDot11APUserAuthSuccCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthSuccCntCM.setStatus("current")
_HpnicfDot11APUserAuthFailCntCM_Type = Counter32
_HpnicfDot11APUserAuthFailCntCM_Object = MibTableColumn
hpnicfDot11APUserAuthFailCntCM = _HpnicfDot11APUserAuthFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1, 4),
    _HpnicfDot11APUserAuthFailCntCM_Type()
)
hpnicfDot11APUserAuthFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APUserAuthFailCntCM.setStatus("current")
_HpnicfDot11AllUserOnlineTimeCM_Type = TimeTicks
_HpnicfDot11AllUserOnlineTimeCM_Object = MibTableColumn
hpnicfDot11AllUserOnlineTimeCM = _HpnicfDot11AllUserOnlineTimeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 2, 35, 1, 5),
    _HpnicfDot11AllUserOnlineTimeCM_Type()
)
hpnicfDot11AllUserOnlineTimeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11AllUserOnlineTimeCM.setStatus("current")
_HpnicfDot11APMtNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11APMtNotifyGroup = _HpnicfDot11APMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3)
)
_HpnicfDot11APMtTraps_ObjectIdentity = ObjectIdentity
hpnicfDot11APMtTraps = _HpnicfDot11APMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0)
)
_HpnicfDot11APMtTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11APMtTrapVarObjects = _HpnicfDot11APMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1)
)
_HpnicfDot11APMtTrapCfgErrReason_Type = HpnicfDot11NotifyReasonType
_HpnicfDot11APMtTrapCfgErrReason_Object = MibScalar
hpnicfDot11APMtTrapCfgErrReason = _HpnicfDot11APMtTrapCfgErrReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 1),
    _HpnicfDot11APMtTrapCfgErrReason_Type()
)
hpnicfDot11APMtTrapCfgErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapCfgErrReason.setStatus("current")


class _HpnicfDot11APMtTrapRadioFailReason_Type(Integer32):
    """Custom type hpnicfDot11APMtTrapRadioFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("hpnicferror", 2),
          ("radar", 4),
          ("swerror", 3),
          ("unknown", 8))
    )


_HpnicfDot11APMtTrapRadioFailReason_Type.__name__ = "Integer32"
_HpnicfDot11APMtTrapRadioFailReason_Object = MibScalar
hpnicfDot11APMtTrapRadioFailReason = _HpnicfDot11APMtTrapRadioFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 2),
    _HpnicfDot11APMtTrapRadioFailReason_Type()
)
hpnicfDot11APMtTrapRadioFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapRadioFailReason.setStatus("current")
_HpnicfDot11APMtTrapOldChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11APMtTrapOldChannel_Object = MibScalar
hpnicfDot11APMtTrapOldChannel = _HpnicfDot11APMtTrapOldChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 3),
    _HpnicfDot11APMtTrapOldChannel_Type()
)
hpnicfDot11APMtTrapOldChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapOldChannel.setStatus("current")
_HpnicfDot11APMtTrapNewChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11APMtTrapNewChannel_Object = MibScalar
hpnicfDot11APMtTrapNewChannel = _HpnicfDot11APMtTrapNewChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 4),
    _HpnicfDot11APMtTrapNewChannel_Type()
)
hpnicfDot11APMtTrapNewChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapNewChannel.setStatus("current")
_HpnicfDot11APChannelChgMode_Type = HpnicfDot11RFModeType
_HpnicfDot11APChannelChgMode_Object = MibScalar
hpnicfDot11APChannelChgMode = _HpnicfDot11APChannelChgMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 5),
    _HpnicfDot11APChannelChgMode_Type()
)
hpnicfDot11APChannelChgMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APChannelChgMode.setStatus("current")


class _HpnicfDot11APChgWorkMode_Type(Integer32):
    """Custom type hpnicfDot11APChgWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HpnicfDot11APChgWorkMode_Type.__name__ = "Integer32"
_HpnicfDot11APChgWorkMode_Object = MibScalar
hpnicfDot11APChgWorkMode = _HpnicfDot11APChgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 6),
    _HpnicfDot11APChgWorkMode_Type()
)
hpnicfDot11APChgWorkMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APChgWorkMode.setStatus("current")
_HpnicfDot11APIntfDevMACAddress_Type = MacAddress
_HpnicfDot11APIntfDevMACAddress_Object = MibScalar
hpnicfDot11APIntfDevMACAddress = _HpnicfDot11APIntfDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 7),
    _HpnicfDot11APIntfDevMACAddress_Type()
)
hpnicfDot11APIntfDevMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APIntfDevMACAddress.setStatus("current")
_HpnicfDot11APMtTrapOldIPAddr_Type = IpAddress
_HpnicfDot11APMtTrapOldIPAddr_Object = MibScalar
hpnicfDot11APMtTrapOldIPAddr = _HpnicfDot11APMtTrapOldIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 8),
    _HpnicfDot11APMtTrapOldIPAddr_Type()
)
hpnicfDot11APMtTrapOldIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapOldIPAddr.setStatus("current")
_HpnicfDot11CurrInterfDetectedNum_Type = Integer32
_HpnicfDot11CurrInterfDetectedNum_Object = MibScalar
hpnicfDot11CurrInterfDetectedNum = _HpnicfDot11CurrInterfDetectedNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 9),
    _HpnicfDot11CurrInterfDetectedNum_Type()
)
hpnicfDot11CurrInterfDetectedNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11CurrInterfDetectedNum.setStatus("current")


class _HpnicfDot11StaFullReason_Type(Integer32):
    """Custom type hpnicfDot11StaFullReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ac", 6),
          ("acConcur", 7),
          ("aid", 8),
          ("ap", 1),
          ("bss", 2),
          ("radio", 3),
          ("radioConcur", 4),
          ("radiopolicy", 5))
    )


_HpnicfDot11StaFullReason_Type.__name__ = "Integer32"
_HpnicfDot11StaFullReason_Object = MibScalar
hpnicfDot11StaFullReason = _HpnicfDot11StaFullReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 10),
    _HpnicfDot11StaFullReason_Type()
)
hpnicfDot11StaFullReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StaFullReason.setStatus("current")
_HpnicfDot11StaLimitNumber_Type = Integer32
_HpnicfDot11StaLimitNumber_Object = MibScalar
hpnicfDot11StaLimitNumber = _HpnicfDot11StaLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 11),
    _HpnicfDot11StaLimitNumber_Type()
)
hpnicfDot11StaLimitNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StaLimitNumber.setStatus("current")


class _HpnicfDot11APRadioDownReason_Type(Integer32):
    """Custom type hpnicfDot11APRadioDownReason based on Integer32"""
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
        *(("apTunnelDown", 4),
          ("configDisable", 2),
          ("operatinUnusable", 3),
          ("phyicalUnusable", 1))
    )


_HpnicfDot11APRadioDownReason_Type.__name__ = "Integer32"
_HpnicfDot11APRadioDownReason_Object = MibScalar
hpnicfDot11APRadioDownReason = _HpnicfDot11APRadioDownReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 12),
    _HpnicfDot11APRadioDownReason_Type()
)
hpnicfDot11APRadioDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APRadioDownReason.setStatus("current")
_HpnicfDot11InterfMacList_Type = OctetString
_HpnicfDot11InterfMacList_Object = MibScalar
hpnicfDot11InterfMacList = _HpnicfDot11InterfMacList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 13),
    _HpnicfDot11InterfMacList_Type()
)
hpnicfDot11InterfMacList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11InterfMacList.setStatus("current")
_HpnicfDot11APTrapUserCnt_Type = Integer32
_HpnicfDot11APTrapUserCnt_Object = MibScalar
hpnicfDot11APTrapUserCnt = _HpnicfDot11APTrapUserCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 14),
    _HpnicfDot11APTrapUserCnt_Type()
)
hpnicfDot11APTrapUserCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapUserCnt.setStatus("current")
_HpnicfDot11APTrapUserThreshold_Type = Integer32
_HpnicfDot11APTrapUserThreshold_Object = MibScalar
hpnicfDot11APTrapUserThreshold = _HpnicfDot11APTrapUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 15),
    _HpnicfDot11APTrapUserThreshold_Type()
)
hpnicfDot11APTrapUserThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APTrapUserThreshold.setStatus("current")
_HpnicfDot11APMtChanlChgCount_Type = Integer32
_HpnicfDot11APMtChanlChgCount_Object = MibScalar
hpnicfDot11APMtChanlChgCount = _HpnicfDot11APMtChanlChgCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 16),
    _HpnicfDot11APMtChanlChgCount_Type()
)
hpnicfDot11APMtChanlChgCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtChanlChgCount.setStatus("current")
_HpnicfDot11APMtFormerApVersion_Type = OctetString
_HpnicfDot11APMtFormerApVersion_Object = MibScalar
hpnicfDot11APMtFormerApVersion = _HpnicfDot11APMtFormerApVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 17),
    _HpnicfDot11APMtFormerApVersion_Type()
)
hpnicfDot11APMtFormerApVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtFormerApVersion.setStatus("current")
_HpnicfDot11APMtAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11APMtAPID_Object = MibScalar
hpnicfDot11APMtAPID = _HpnicfDot11APMtAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 18),
    _HpnicfDot11APMtAPID_Type()
)
hpnicfDot11APMtAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtAPID.setStatus("current")
_HpnicfDot11APMtRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11APMtRadioID_Object = MibScalar
hpnicfDot11APMtRadioID = _HpnicfDot11APMtRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 19),
    _HpnicfDot11APMtRadioID_Type()
)
hpnicfDot11APMtRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtRadioID.setStatus("current")
_HpnicfDot11APMtChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11APMtChannel_Object = MibScalar
hpnicfDot11APMtChannel = _HpnicfDot11APMtChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 20),
    _HpnicfDot11APMtChannel_Type()
)
hpnicfDot11APMtChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtChannel.setStatus("current")
_HpnicfDot11APMtInterfMacAdd_Type = MacAddress
_HpnicfDot11APMtInterfMacAdd_Object = MibScalar
hpnicfDot11APMtInterfMacAdd = _HpnicfDot11APMtInterfMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 21),
    _HpnicfDot11APMtInterfMacAdd_Type()
)
hpnicfDot11APMtInterfMacAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtInterfMacAdd.setStatus("current")
_HpnicfDot11APMtAdjChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11APMtAdjChannel_Object = MibScalar
hpnicfDot11APMtAdjChannel = _HpnicfDot11APMtAdjChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 22),
    _HpnicfDot11APMtAdjChannel_Type()
)
hpnicfDot11APMtAdjChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtAdjChannel.setStatus("current")
_HpnicfDot11APMtFirstTrapTime_Type = TimeTicks
_HpnicfDot11APMtFirstTrapTime_Object = MibScalar
hpnicfDot11APMtFirstTrapTime = _HpnicfDot11APMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 23),
    _HpnicfDot11APMtFirstTrapTime_Type()
)
hpnicfDot11APMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtFirstTrapTime.setStatus("current")
_HpnicfDot11APMtTrapAPMacAddress_Type = MacAddress
_HpnicfDot11APMtTrapAPMacAddress_Object = MibScalar
hpnicfDot11APMtTrapAPMacAddress = _HpnicfDot11APMtTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 1, 24),
    _HpnicfDot11APMtTrapAPMacAddress_Type()
)
hpnicfDot11APMtTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11APMtTrapAPMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11APMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 1)
)
hpnicfDot11APMtWorkModeChgTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APChgWorkMode"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtWorkModeChgTrap.setStatus(
        "current"
    )

hpnicfDot11APMtCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 2)
)
hpnicfDot11APMtCfgErrorTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapCfgErrReason"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtCfgErrorTrap.setStatus(
        "current"
    )

hpnicfDot11APMtRadioFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 3)
)
hpnicfDot11APMtRadioFailTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapRadioFailReason"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtRadioFailTrap.setStatus(
        "current"
    )

hpnicfDot11APMtRadioFailRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 4)
)
hpnicfDot11APMtRadioFailRecoverTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtRadioFailRecoverTrap.setStatus(
        "current"
    )

hpnicfDot11APMtRdoChanlChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 5)
)
hpnicfDot11APMtRdoChanlChgTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APChannelChgMode"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapOldChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapNewChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChanlChgCount"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtRdoChanlChgTrap.setStatus(
        "current"
    )

hpnicfDot11APMtTimeSynFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 6)
)
hpnicfDot11APMtTimeSynFail.setObjects(
    ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID")
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtTimeSynFail.setStatus(
        "current"
    )

hpnicfDot11APMtChlIntfDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 7)
)
hpnicfDot11APMtChlIntfDetected.setObjects(
    ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel")
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtChlIntfDetected.setStatus(
        "current"
    )

hpnicfDot11APMtIntfAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 8)
)
hpnicfDot11APMtIntfAPDetected.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtIntfAPDetected.setStatus(
        "current"
    )

hpnicfDot11APMtIntfStaDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 9)
)
hpnicfDot11APMtIntfStaDetected.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtIntfStaDetected.setStatus(
        "current"
    )

hpnicfDot11APMtIPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 10)
)
hpnicfDot11APMtIPChange.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APIPAddress"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapOldIPAddr"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtIPChange.setStatus(
        "current"
    )

hpnicfDot11APFlashWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 11)
)
hpnicfDot11APFlashWriteFailure.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFormerApVersion"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APFlashWriteFailure.setStatus(
        "current"
    )

hpnicfDot11APSysReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 12)
)
hpnicfDot11APSysReboot.setObjects(
    ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID")
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysReboot.setStatus(
        "current"
    )

hpnicfDot11APMtAvailChlTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 13)
)
hpnicfDot11APMtAvailChlTooLow.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtAvailChlTooLow.setStatus(
        "current"
    )

hpnicfDot11APImgDwldSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 14)
)
hpnicfDot11APImgDwldSuccess.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurrAPName"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurrAPIPAddress"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurrAPSoftwareVersion"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APImgDwldSuccess.setStatus(
        "current"
    )

hpnicfDot11APInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 15)
)
hpnicfDot11APInterfDetectedTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurrInterfDetectedNum"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11InterfMacList"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APInterfDetectedTrap.setStatus(
        "current"
    )

hpnicfDot11APInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 16)
)
hpnicfDot11APInterfClearTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APInterfClearTrap.setStatus(
        "current"
    )

hpnicfDot11StaInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 17)
)
hpnicfDot11StaInterfDetectedTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11CurrInterfDetectedNum"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11InterfMacList"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StaInterfDetectedTrap.setStatus(
        "current"
    )

hpnicfDot11StaInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 18)
)
hpnicfDot11StaInterfClearTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StaInterfClearTrap.setStatus(
        "current"
    )

hpnicfDot11OtherDevIntDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 19)
)
hpnicfDot11OtherDevIntDetectedTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11OtherDevIntDetectedTrap.setStatus(
        "current"
    )

hpnicfDot11OtherDevIntClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 20)
)
hpnicfDot11OtherDevIntClearTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11Channel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11OtherDevIntClearTrap.setStatus(
        "current"
    )

hpnicfDot11APModuleTroubleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 21)
)
hpnicfDot11APModuleTroubleTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APModuleTroubleTrap.setStatus(
        "current"
    )

hpnicfDot11APModuleTroubleClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 22)
)
hpnicfDot11APModuleTroubleClearTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APModuleTroubleClearTrap.setStatus(
        "current"
    )

hpnicfDot11APRadioDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 23)
)
hpnicfDot11APRadioDownTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APRadioDownReason"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APRadioDownTrap.setStatus(
        "current"
    )

hpnicfDot11APRadioDownRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 24)
)
hpnicfDot11APRadioDownRecovTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APRadioDownRecovTrap.setStatus(
        "current"
    )

hpnicfDot11APStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 25)
)
hpnicfDot11APStaFullTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11StaLimitNumber"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11StaFullReason"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APStaFullTrap.setStatus(
        "current"
    )

hpnicfDot11APStaFullRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 26)
)
hpnicfDot11APStaFullRecoverTrap.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11StaLimitNumber"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11StaFullReason"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APStaFullRecoverTrap.setStatus(
        "current"
    )

hpnicfDot11DFSFreeCntBelowThrRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 27)
)
hpnicfDot11DFSFreeCntBelowThrRecov.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11RadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11DFSFreeCntBelowThrRecov.setStatus(
        "current"
    )

hpnicfDot11APCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 28)
)
hpnicfDot11APCpuUsageHigh.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APCPURTUsage"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsageHigh.setStatus(
        "current"
    )

hpnicfDot11APCpuUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 29)
)
hpnicfDot11APCpuUsageHighRecover.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APCPURTUsage"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsageHighRecover.setStatus(
        "current"
    )

hpnicfDot11APMemUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 30)
)
hpnicfDot11APMemUsageHigh.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMemRTUsage"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMemUsageHigh.setStatus(
        "current"
    )

hpnicfDot11APMemUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 31)
)
hpnicfDot11APMemUsageHighRecover.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMemRTUsage"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMemUsageHighRecover.setStatus(
        "current"
    )

hpnicfDot11APTrapUserCntExceedThre = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 32)
)
hpnicfDot11APTrapUserCntExceedThre.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APTrapUserCnt"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APTrapUserThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APTrapUserCntExceedThre.setStatus(
        "current"
    )

hpnicfDot11APMtDetectedIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 33)
)
hpnicfDot11APMtDetectedIntfAP.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtDetectedIntfAP.setStatus(
        "current"
    )

hpnicfDot11APMtDetectedIntfSTA = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 34)
)
hpnicfDot11APMtDetectedIntfSTA.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtDetectedIntfSTA.setStatus(
        "current"
    )

hpnicfDot11APMtDetectedIntfOtherDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 35)
)
hpnicfDot11APMtDetectedIntfOtherDev.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11APMtDetectedIntfOtherDev.setStatus(
        "current"
    )

hpnicfDot11DetcAdjChlIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 36)
)
hpnicfDot11DetcAdjChlIntfAP.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAdjChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11DetcAdjChlIntfAP.setStatus(
        "current"
    )

hpnicfDot11DetcAdjChlIntfAPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 2, 3, 0, 37)
)
hpnicfDot11DetcAdjChlIntfAPClear.setObjects(
      *(("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAPID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtRadioID"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtAdjChannel"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtInterfMacAdd"),
        ("HPN-ICF-DOT11-APMT-MIB", "hpnicfDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfDot11DetcAdjChlIntfAPClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-APMT-MIB",
    **{"hpnicfDot11APMT": hpnicfDot11APMT,
       "hpnicfDot11APObjectGroup": hpnicfDot11APObjectGroup,
       "hpnicfDot11APObjectStatusTable": hpnicfDot11APObjectStatusTable,
       "hpnicfDot11APObjectStatusEntry": hpnicfDot11APObjectStatusEntry,
       "hpnicfDot11APID": hpnicfDot11APID,
       "hpnicfDot11APIPAddress": hpnicfDot11APIPAddress,
       "hpnicfDot11APMacAddress": hpnicfDot11APMacAddress,
       "hpnicfDot11APOperationStatus": hpnicfDot11APOperationStatus,
       "hpnicfDot11APTemplateNameOfAP": hpnicfDot11APTemplateNameOfAP,
       "hpnicfDot11APReset": hpnicfDot11APReset,
       "hpnicfDot11APCpuUsage": hpnicfDot11APCpuUsage,
       "hpnicfDot11APConnectionType": hpnicfDot11APConnectionType,
       "hpnicfDot11APLastImgDownloadTime": hpnicfDot11APLastImgDownloadTime,
       "hpnicfDot11APIPv6Address": hpnicfDot11APIPv6Address,
       "hpnicfDot11APLastRegisterTime": hpnicfDot11APLastRegisterTime,
       "hpnicfDot11APResetCM": hpnicfDot11APResetCM,
       "hpnicfDot11APObjectTable": hpnicfDot11APObjectTable,
       "hpnicfDot11APObjectEntry": hpnicfDot11APObjectEntry,
       "hpnicfDot11APObjID": hpnicfDot11APObjID,
       "hpnicfDot11CurrAPIPAddress": hpnicfDot11CurrAPIPAddress,
       "hpnicfDot11CurrAPMacAddress": hpnicfDot11CurrAPMacAddress,
       "hpnicfDot11CurrACPortIndex": hpnicfDot11CurrACPortIndex,
       "hpnicfDot11CurrAPMACMode": hpnicfDot11CurrAPMACMode,
       "hpnicfDot11CurrAPTemplateName": hpnicfDot11CurrAPTemplateName,
       "hpnicfDot11CurrAPStationAssocCount": hpnicfDot11CurrAPStationAssocCount,
       "hpnicfDot11CurrAPName": hpnicfDot11CurrAPName,
       "hpnicfDot11CurrAPModelName": hpnicfDot11CurrAPModelName,
       "hpnicfDot11CurrAPImageName": hpnicfDot11CurrAPImageName,
       "hpnicfDot11CurrAPSoftwareVersion": hpnicfDot11CurrAPSoftwareVersion,
       "hpnicfDot11CurrAPIPNetMask": hpnicfDot11CurrAPIPNetMask,
       "hpnicfDot11CurrRadioModeSupport": hpnicfDot11CurrRadioModeSupport,
       "hpnicfDot11CurrIfNumber": hpnicfDot11CurrIfNumber,
       "hpnicfDot11CurrAPElementID": hpnicfDot11CurrAPElementID,
       "hpnicfDot11CurrAPMode": hpnicfDot11CurrAPMode,
       "hpnicfDot11CurrAPIPv6Address": hpnicfDot11CurrAPIPv6Address,
       "hpnicfDot11CurrAPSSIDNumber": hpnicfDot11CurrAPSSIDNumber,
       "hpnicfDot11CurrAPManufacturer": hpnicfDot11CurrAPManufacturer,
       "hpnicfDot11CurrAPMemorySize": hpnicfDot11CurrAPMemorySize,
       "hpnicfDot11CurrAPMemSizeInBytes": hpnicfDot11CurrAPMemSizeInBytes,
       "hpnicfDot11CurrAPFlashSize": hpnicfDot11CurrAPFlashSize,
       "hpnicfDot11CurrAPFlashSizeInBytes": hpnicfDot11CurrAPFlashSizeInBytes,
       "hpnicfDot11CurrAPReleasedVersion": hpnicfDot11CurrAPReleasedVersion,
       "hpnicfDot11CurrRadioModeSupport2": hpnicfDot11CurrRadioModeSupport2,
       "hpnicfDot11CurrAPCPUTypeCM": hpnicfDot11CurrAPCPUTypeCM,
       "hpnicfDot11CurrAPMemoryTypeCM": hpnicfDot11CurrAPMemoryTypeCM,
       "hpnicfDot11CurrAPBSSIDNumberCM": hpnicfDot11CurrAPBSSIDNumberCM,
       "hpnicfDot11APRadioTable": hpnicfDot11APRadioTable,
       "hpnicfDot11APRadioEntry": hpnicfDot11APRadioEntry,
       "hpnicfDot11CurAPID": hpnicfDot11CurAPID,
       "hpnicfDot11RadioID": hpnicfDot11RadioID,
       "hpnicfDot11AdminStatus": hpnicfDot11AdminStatus,
       "hpnicfDot11OperStatus": hpnicfDot11OperStatus,
       "hpnicfDot11Channel": hpnicfDot11Channel,
       "hpnicfDot11TxPowerLevel": hpnicfDot11TxPowerLevel,
       "hpnicfDot11APRadioIfIndex": hpnicfDot11APRadioIfIndex,
       "hpnicfDot11AntennaGain": hpnicfDot11AntennaGain,
       "hpnicfDot11MaxBandwidth": hpnicfDot11MaxBandwidth,
       "hpnicfDot11ResourceUseRatio": hpnicfDot11ResourceUseRatio,
       "hpnicfDot11RadioModeSupport": hpnicfDot11RadioModeSupport,
       "hpnicfDot11TxPowerLevel2": hpnicfDot11TxPowerLevel2,
       "hpnicfDot11PowerMgmtStatus": hpnicfDot11PowerMgmtStatus,
       "hpnicfDot11ChannelSwitchTimes": hpnicfDot11ChannelSwitchTimes,
       "hpnicfDot11AntennaType": hpnicfDot11AntennaType,
       "hpnicfDot11DiversitySelectionRx": hpnicfDot11DiversitySelectionRx,
       "hpnicfDot11MaxTxPwrLvl": hpnicfDot11MaxTxPwrLvl,
       "hpnicfDot11PwrAttRange": hpnicfDot11PwrAttRange,
       "hpnicfDot11AvgRxSignalStrength": hpnicfDot11AvgRxSignalStrength,
       "hpnicfDot11HighestRxSignalStrength": hpnicfDot11HighestRxSignalStrength,
       "hpnicfDot11LowestRxSignalStrength": hpnicfDot11LowestRxSignalStrength,
       "hpnicfDot11RadioIfUpdownTimes": hpnicfDot11RadioIfUpdownTimes,
       "hpnicfDot11RadioIfLastChange": hpnicfDot11RadioIfLastChange,
       "hpnicfDot11RadioModeSupport2": hpnicfDot11RadioModeSupport2,
       "hpnicfDot11OperStatusCM": hpnicfDot11OperStatusCM,
       "hpnicfDot11APBSSTable": hpnicfDot11APBSSTable,
       "hpnicfDot11APBSSEntry": hpnicfDot11APBSSEntry,
       "hpnicfDot11WlanID": hpnicfDot11WlanID,
       "hpnicfDot11BSSID": hpnicfDot11BSSID,
       "hpnicfDot11CurrSvcPolicyID": hpnicfDot11CurrSvcPolicyID,
       "hpnicfDot11SSID": hpnicfDot11SSID,
       "hpnicfDot11CurrSSIDResourceUseRatio": hpnicfDot11CurrSSIDResourceUseRatio,
       "hpnicfDot11APEssVlanId": hpnicfDot11APEssVlanId,
       "hpnicfDot11APModelTable": hpnicfDot11APModelTable,
       "hpnicfDot11APModelEntry": hpnicfDot11APModelEntry,
       "hpnicfDot11APModelAlias": hpnicfDot11APModelAlias,
       "hpnicfDot11APModelName": hpnicfDot11APModelName,
       "hpnicfDot11RadioNumSupport": hpnicfDot11RadioNumSupport,
       "hpnicfDot11StationNumSupport": hpnicfDot11StationNumSupport,
       "hpnicfDot11MACModeSupport": hpnicfDot11MACModeSupport,
       "hpnicfDot11APManufacturer": hpnicfDot11APManufacturer,
       "hpnicfDot11APCPUType": hpnicfDot11APCPUType,
       "hpnicfDot11APCPUClockSpeed": hpnicfDot11APCPUClockSpeed,
       "hpnicfDot11APMemoryType": hpnicfDot11APMemoryType,
       "hpnicfDot11APFlashType": hpnicfDot11APFlashType,
       "hpnicfDot11APFlashSize": hpnicfDot11APFlashSize,
       "hpnicfDot11APMemSize": hpnicfDot11APMemSize,
       "hpnicfDot11APFlashSizeInBytes": hpnicfDot11APFlashSizeInBytes,
       "hpnicfDot11APMemorySize": hpnicfDot11APMemorySize,
       "hpnicfDot11APIfTable": hpnicfDot11APIfTable,
       "hpnicfDot11APIfEntry": hpnicfDot11APIfEntry,
       "hpnicfDot11APIfIndex": hpnicfDot11APIfIndex,
       "hpnicfDot11APIfDescr": hpnicfDot11APIfDescr,
       "hpnicfDot11APIfType": hpnicfDot11APIfType,
       "hpnicfDot11APIfMtu": hpnicfDot11APIfMtu,
       "hpnicfDot11APIfPHYAddress": hpnicfDot11APIfPHYAddress,
       "hpnicfDot11APIfSpeed": hpnicfDot11APIfSpeed,
       "hpnicfDot11APIfInDataRate": hpnicfDot11APIfInDataRate,
       "hpnicfDot11APIfOutDataRate": hpnicfDot11APIfOutDataRate,
       "hpnicfDot11APIfSpeedKbps": hpnicfDot11APIfSpeedKbps,
       "hpnicfDot11APIfTypeCM": hpnicfDot11APIfTypeCM,
       "hpnicfDot11APSSIDObjectTable": hpnicfDot11APSSIDObjectTable,
       "hpnicfDot11APSSIDObjectEntry": hpnicfDot11APSSIDObjectEntry,
       "hpnicfDot11APConfigSPID": hpnicfDot11APConfigSPID,
       "hpnicfDot11APConfigSSIDName": hpnicfDot11APConfigSSIDName,
       "hpnicfDot11APConfigBSSIDNum": hpnicfDot11APConfigBSSIDNum,
       "hpnicfDot11APConfigPortalStaNum": hpnicfDot11APConfigPortalStaNum,
       "hpnicfDot11APSysInfoTable": hpnicfDot11APSysInfoTable,
       "hpnicfDot11APSysInfoEntry": hpnicfDot11APSysInfoEntry,
       "hpnicfDot11APSysUpTime": hpnicfDot11APSysUpTime,
       "hpnicfDot11APCPURTUsage": hpnicfDot11APCPURTUsage,
       "hpnicfDot11APCPUAvgUsage": hpnicfDot11APCPUAvgUsage,
       "hpnicfDot11APMemRTUsage": hpnicfDot11APMemRTUsage,
       "hpnicfDot11APMemAvgUsage": hpnicfDot11APMemAvgUsage,
       "hpnicfDot11APIPAddressGateway": hpnicfDot11APIPAddressGateway,
       "hpnicfDot11APACAssociateStatus": hpnicfDot11APACAssociateStatus,
       "hpnicfDot11APManuBuildInfo": hpnicfDot11APManuBuildInfo,
       "hpnicfDot11APFlashFreeSize": hpnicfDot11APFlashFreeSize,
       "hpnicfDot11APTemperature": hpnicfDot11APTemperature,
       "hpnicfDot11APIdleListTable": hpnicfDot11APIdleListTable,
       "hpnicfDot11APIdleListEntry": hpnicfDot11APIdleListEntry,
       "hpnicfDot11APIdleTemplateName": hpnicfDot11APIdleTemplateName,
       "hpnicfDot11APIdleSerialID": hpnicfDot11APIdleSerialID,
       "hpnicfDot11APSysInfoByAPIDTable": hpnicfDot11APSysInfoByAPIDTable,
       "hpnicfDot11APSysInfoByAPIDEntry": hpnicfDot11APSysInfoByAPIDEntry,
       "hpnicfDot11APSysUpTime2": hpnicfDot11APSysUpTime2,
       "hpnicfDot11APCPURTUsage2": hpnicfDot11APCPURTUsage2,
       "hpnicfDot11APCPUAvgUsage2": hpnicfDot11APCPUAvgUsage2,
       "hpnicfDot11APMemRTUsage2": hpnicfDot11APMemRTUsage2,
       "hpnicfDot11APMemAvgUsage2": hpnicfDot11APMemAvgUsage2,
       "hpnicfDot11APIPAddressGateway2": hpnicfDot11APIPAddressGateway2,
       "hpnicfDot11APACAssociateStatus2": hpnicfDot11APACAssociateStatus2,
       "hpnicfDot11APManuBuildInfo2": hpnicfDot11APManuBuildInfo2,
       "hpnicfDot11APFlashFreeSize2": hpnicfDot11APFlashFreeSize2,
       "hpnicfDot11APTemperature2": hpnicfDot11APTemperature2,
       "hpnicfDot11APMacAddress2": hpnicfDot11APMacAddress2,
       "hpnicfDot11APACAssociateStatusCM": hpnicfDot11APACAssociateStatusCM,
       "hpnicfDot11APStatisGroup": hpnicfDot11APStatisGroup,
       "hpnicfDot11APRxStatisTable": hpnicfDot11APRxStatisTable,
       "hpnicfDot11APRxStatisEntry": hpnicfDot11APRxStatisEntry,
       "hpnicfDot11RxFrameDupCnt": hpnicfDot11RxFrameDupCnt,
       "hpnicfDot11RxFrameCnt": hpnicfDot11RxFrameCnt,
       "hpnicfDot11RxUcastFrameCnt": hpnicfDot11RxUcastFrameCnt,
       "hpnicfDot11RxBcastFrameCnt": hpnicfDot11RxBcastFrameCnt,
       "hpnicfDot11RxMcastFrameCnt": hpnicfDot11RxMcastFrameCnt,
       "hpnicfDot11RxDiscardFrameCnt": hpnicfDot11RxDiscardFrameCnt,
       "hpnicfDot11RxFragCnt": hpnicfDot11RxFragCnt,
       "hpnicfDot11RxFcsErrCnt": hpnicfDot11RxFcsErrCnt,
       "hpnicfDot11RxFrameBytes": hpnicfDot11RxFrameBytes,
       "hpnicfDot11RxUcastFrameBytes": hpnicfDot11RxUcastFrameBytes,
       "hpnicfDot11RxBcastFrameBytes": hpnicfDot11RxBcastFrameBytes,
       "hpnicfDot11RxMcastFrameBytes": hpnicfDot11RxMcastFrameBytes,
       "hpnicfDot11RxDiscardFrameBytes": hpnicfDot11RxDiscardFrameBytes,
       "hpnicfDot11RxMgmtFrameCnt": hpnicfDot11RxMgmtFrameCnt,
       "hpnicfDot11RxCtrlFrameCnt": hpnicfDot11RxCtrlFrameCnt,
       "hpnicfDot11RxDataFrameCnt": hpnicfDot11RxDataFrameCnt,
       "hpnicfDot11RxDecryptErrorCnt": hpnicfDot11RxDecryptErrorCnt,
       "hpnicfDot11RxAuthenFrameCnt": hpnicfDot11RxAuthenFrameCnt,
       "hpnicfDot11RxAssociateFrameCnt": hpnicfDot11RxAssociateFrameCnt,
       "hpnicfDot11RxFrameErrorRatio": hpnicfDot11RxFrameErrorRatio,
       "hpnicfDot11RxPhyErrorCnt": hpnicfDot11RxPhyErrorCnt,
       "hpnicfDot11RxMICErrorCnt": hpnicfDot11RxMICErrorCnt,
       "hpnicfDot11RxDataFrameBytes": hpnicfDot11RxDataFrameBytes,
       "hpnicfDot11RadioRxAverSnr": hpnicfDot11RadioRxAverSnr,
       "hpnicfDot11RxPayloadBytes": hpnicfDot11RxPayloadBytes,
       "hpnicfDot11RxTrafficSpeed": hpnicfDot11RxTrafficSpeed,
       "hpnicfDot11RxUcastDataFrameCnt": hpnicfDot11RxUcastDataFrameCnt,
       "hpnicfDot11RxNUcastDataFrameCnt": hpnicfDot11RxNUcastDataFrameCnt,
       "hpnicfDot11RxTotalDiscardFrameCnt": hpnicfDot11RxTotalDiscardFrameCnt,
       "hpnicfDot11RxTotalIPCheckErrPacketCnt": hpnicfDot11RxTotalIPCheckErrPacketCnt,
       "hpnicfDot11RxSignalStrengthPacketCntCM": hpnicfDot11RxSignalStrengthPacketCntCM,
       "hpnicfDot11RxDataFrameCntCM": hpnicfDot11RxDataFrameCntCM,
       "hpnicfDot11APTxStatisTable": hpnicfDot11APTxStatisTable,
       "hpnicfDot11APTxStatisEntry": hpnicfDot11APTxStatisEntry,
       "hpnicfDot11TxFragCnt": hpnicfDot11TxFragCnt,
       "hpnicfDot11FailedCnt": hpnicfDot11FailedCnt,
       "hpnicfDot11RetryCnt": hpnicfDot11RetryCnt,
       "hpnicfDot11MultiRetryCnt": hpnicfDot11MultiRetryCnt,
       "hpnicfDot11RtsSuccessCnt": hpnicfDot11RtsSuccessCnt,
       "hpnicfDot11RtsFailCnt": hpnicfDot11RtsFailCnt,
       "hpnicfDot11AckFailCnt": hpnicfDot11AckFailCnt,
       "hpnicfDot11TxFrameCnt": hpnicfDot11TxFrameCnt,
       "hpnicfDot11TxUcastFrameCnt": hpnicfDot11TxUcastFrameCnt,
       "hpnicfDot11TxBcastFrameCnt": hpnicfDot11TxBcastFrameCnt,
       "hpnicfDot11TxMcastFrameCnt": hpnicfDot11TxMcastFrameCnt,
       "hpnicfDot11TxDiscardFrameCnt": hpnicfDot11TxDiscardFrameCnt,
       "hpnicfDot11TxFrameBytes": hpnicfDot11TxFrameBytes,
       "hpnicfDot11TxUcastFrameBytes": hpnicfDot11TxUcastFrameBytes,
       "hpnicfDot11TxBcastFrameBytes": hpnicfDot11TxBcastFrameBytes,
       "hpnicfDot11TxMcastFrameBytes": hpnicfDot11TxMcastFrameBytes,
       "hpnicfDot11TxDiscardFrameBytes": hpnicfDot11TxDiscardFrameBytes,
       "hpnicfDot11TxAuthenFrameCnt": hpnicfDot11TxAuthenFrameCnt,
       "hpnicfDot11TxAssociateFrameCnt": hpnicfDot11TxAssociateFrameCnt,
       "hpnicfDot11TxFrameRetryRatio": hpnicfDot11TxFrameRetryRatio,
       "hpnicfDot11TxDataFrameCnt": hpnicfDot11TxDataFrameCnt,
       "hpnicfDot11TxDataFrameBytes": hpnicfDot11TxDataFrameBytes,
       "hpnicfDot11TxMSDUCnt": hpnicfDot11TxMSDUCnt,
       "hpnicfDot11TxDiscardMSDUCnt": hpnicfDot11TxDiscardMSDUCnt,
       "hpnicfDot11RetryMSDUCnt": hpnicfDot11RetryMSDUCnt,
       "hpnicfDot11TxPayloadBytes": hpnicfDot11TxPayloadBytes,
       "hpnicfDot11TxTrafficSpeed": hpnicfDot11TxTrafficSpeed,
       "hpnicfDot11TxErrFrameRatio": hpnicfDot11TxErrFrameRatio,
       "hpnicfDot11TxFrameRate": hpnicfDot11TxFrameRate,
       "hpnicfDot11TxMgtFrameCnt": hpnicfDot11TxMgtFrameCnt,
       "hpnicfDot11TxCtrlFrameCnt": hpnicfDot11TxCtrlFrameCnt,
       "hpnicfDot11TxMACErrCnt": hpnicfDot11TxMACErrCnt,
       "hpnicfDot11TxErrFrameCnt": hpnicfDot11TxErrFrameCnt,
       "hpnicfDot11TxUcastDataFrameCnt": hpnicfDot11TxUcastDataFrameCnt,
       "hpnicfDot11TxNUcastDataFrameCnt": hpnicfDot11TxNUcastDataFrameCnt,
       "hpnicfDot11APAssocStatisTable": hpnicfDot11APAssocStatisTable,
       "hpnicfDot11APAssocStatisEntry": hpnicfDot11APAssocStatisEntry,
       "hpnicfDot11ApStationAssocSum": hpnicfDot11ApStationAssocSum,
       "hpnicfDot11ApStationAssocFailSum": hpnicfDot11ApStationAssocFailSum,
       "hpnicfDot11ApStationReassocSum": hpnicfDot11ApStationReassocSum,
       "hpnicfDot11ApStationAssocRejectSum": hpnicfDot11ApStationAssocRejectSum,
       "hpnicfDot11ApStationExDeAuthenSum": hpnicfDot11ApStationExDeAuthenSum,
       "hpnicfDot11ApStationCurAssocSum": hpnicfDot11ApStationCurAssocSum,
       "hpnicfDot11ApStaCurAuthSuccSum": hpnicfDot11ApStaCurAuthSuccSum,
       "hpnicfDot11AllStationUpSumTime": hpnicfDot11AllStationUpSumTime,
       "hpnicfDot11ApStationAssocReqSum": hpnicfDot11ApStationAssocReqSum,
       "hpnicfDot11AllStationUpSumTimeTicks": hpnicfDot11AllStationUpSumTimeTicks,
       "hpnicfDot11ApStationReassocReqSum": hpnicfDot11ApStationReassocReqSum,
       "hpnicfDot11ApStationReassocFailSum": hpnicfDot11ApStationReassocFailSum,
       "hpnicfDot11BSSRxStatisTable": hpnicfDot11BSSRxStatisTable,
       "hpnicfDot11BSSRxStatisEntry": hpnicfDot11BSSRxStatisEntry,
       "hpnicfDot11BSSRxFrameCnt": hpnicfDot11BSSRxFrameCnt,
       "hpnicfDot11BSSRxFrameBytes": hpnicfDot11BSSRxFrameBytes,
       "hpnicfDot11BSSRxDataFrameCnt": hpnicfDot11BSSRxDataFrameCnt,
       "hpnicfDot11BSSRxDataFrameBytes": hpnicfDot11BSSRxDataFrameBytes,
       "hpnicfDot11BSSRxAssociateFrameCnt": hpnicfDot11BSSRxAssociateFrameCnt,
       "hpnicfDot11BSSRxFrameErrorRatio": hpnicfDot11BSSRxFrameErrorRatio,
       "hpnicfDot11BSSRxPayloadBytes": hpnicfDot11BSSRxPayloadBytes,
       "hpnicfDot11BSSRxUniFrameCnt": hpnicfDot11BSSRxUniFrameCnt,
       "hpnicfDot11BSSRxNonUniFrameCnt": hpnicfDot11BSSRxNonUniFrameCnt,
       "hpnicfDot11BSSRxAuthenFrameCnt": hpnicfDot11BSSRxAuthenFrameCnt,
       "hpnicfDot11BSSTxStatisTable": hpnicfDot11BSSTxStatisTable,
       "hpnicfDot11BSSTxStatisEntry": hpnicfDot11BSSTxStatisEntry,
       "hpnicfDot11BSSTxFrameCnt": hpnicfDot11BSSTxFrameCnt,
       "hpnicfDot11BSSTxFrameBytes": hpnicfDot11BSSTxFrameBytes,
       "hpnicfDot11BSSTxDataFrameCnt": hpnicfDot11BSSTxDataFrameCnt,
       "hpnicfDot11BSSTxDataFrameBytes": hpnicfDot11BSSTxDataFrameBytes,
       "hpnicfDot11BSSTxAssociateFrameCnt": hpnicfDot11BSSTxAssociateFrameCnt,
       "hpnicfDot11BSSTxPayloadBytes": hpnicfDot11BSSTxPayloadBytes,
       "hpnicfDot11BSSTxRetryCnt": hpnicfDot11BSSTxRetryCnt,
       "hpnicfDot11BSSTxUniFrameCnt": hpnicfDot11BSSTxUniFrameCnt,
       "hpnicfDot11BSSTxNonUniFrameCnt": hpnicfDot11BSSTxNonUniFrameCnt,
       "hpnicfDot11BSSTxAuthenFrameCnt": hpnicfDot11BSSTxAuthenFrameCnt,
       "hpnicfDot11BSSAssocStatisTable": hpnicfDot11BSSAssocStatisTable,
       "hpnicfDot11BSSAssocStatisEntry": hpnicfDot11BSSAssocStatisEntry,
       "hpnicfDot11BSSStationAssocSum": hpnicfDot11BSSStationAssocSum,
       "hpnicfDot11BSSStationAssocFailSum": hpnicfDot11BSSStationAssocFailSum,
       "hpnicfDot11BSSStationReassocSum": hpnicfDot11BSSStationReassocSum,
       "hpnicfDot11BSSStationAssocRejectSum": hpnicfDot11BSSStationAssocRejectSum,
       "hpnicfDot11BSSStationExDeAssocSum": hpnicfDot11BSSStationExDeAssocSum,
       "hpnicfDot11BSSStationCurAssocSum": hpnicfDot11BSSStationCurAssocSum,
       "hpnicfDot11BSSStationAssocReqSum": hpnicfDot11BSSStationAssocReqSum,
       "hpnicfDot11BSSStationCurAuthSum": hpnicfDot11BSSStationCurAuthSum,
       "hpnicfDot11APLinkStatisTable": hpnicfDot11APLinkStatisTable,
       "hpnicfDot11APLinkStatisEntry": hpnicfDot11APLinkStatisEntry,
       "hpnicfDot11UpLinkUpDownTimes": hpnicfDot11UpLinkUpDownTimes,
       "hpnicfDot11DownLinkUpDownTimes": hpnicfDot11DownLinkUpDownTimes,
       "hpnicfDot11RadioAssocStatisTable": hpnicfDot11RadioAssocStatisTable,
       "hpnicfDot11RadioAssocStatisEntry": hpnicfDot11RadioAssocStatisEntry,
       "hpnicfDot11RadioStaAssocSum": hpnicfDot11RadioStaAssocSum,
       "hpnicfDot11RadioStaAssocFailSum": hpnicfDot11RadioStaAssocFailSum,
       "hpnicfDot11RadioStaReassocSum": hpnicfDot11RadioStaReassocSum,
       "hpnicfDot11RadioStaAssocRejectSum": hpnicfDot11RadioStaAssocRejectSum,
       "hpnicfDot11RadioStaExDeAssocSum": hpnicfDot11RadioStaExDeAssocSum,
       "hpnicfDot11RadioStaCurAssocSum": hpnicfDot11RadioStaCurAssocSum,
       "hpnicfDot11RadioMngFrameStatisTable": hpnicfDot11RadioMngFrameStatisTable,
       "hpnicfDot11RadioMngFrameStatisEntry": hpnicfDot11RadioMngFrameStatisEntry,
       "hpnicfDot11RadioStatisIndex": hpnicfDot11RadioStatisIndex,
       "hpnicfDot11MngFrameType": hpnicfDot11MngFrameType,
       "hpnicfDot11MngFrameCnt": hpnicfDot11MngFrameCnt,
       "hpnicfDot11APAuthFailStatisTable": hpnicfDot11APAuthFailStatisTable,
       "hpnicfDot11APAuthFailStatisEntry": hpnicfDot11APAuthFailStatisEntry,
       "hpnicfDot11APAuthFailStatisType": hpnicfDot11APAuthFailStatisType,
       "hpnicfDot11APAuthFailStatisCnt": hpnicfDot11APAuthFailStatisCnt,
       "hpnicfDot11APAssocFailStatisTable": hpnicfDot11APAssocFailStatisTable,
       "hpnicfDot11APAssocFailStatisEntry": hpnicfDot11APAssocFailStatisEntry,
       "hpnicfDot11APAssocFailStatisType": hpnicfDot11APAssocFailStatisType,
       "hpnicfDot11APAssocFailStatisCnt": hpnicfDot11APAssocFailStatisCnt,
       "hpnicfDot11APReassocStatisTable": hpnicfDot11APReassocStatisTable,
       "hpnicfDot11APReassocStatisEntry": hpnicfDot11APReassocStatisEntry,
       "hpnicfDot11APReassocStatisType": hpnicfDot11APReassocStatisType,
       "hpnicfDot11APReassocStatisCnt": hpnicfDot11APReassocStatisCnt,
       "hpnicfDot11APUserAuthStatisTable": hpnicfDot11APUserAuthStatisTable,
       "hpnicfDot11APUserAuthStatisEntry": hpnicfDot11APUserAuthStatisEntry,
       "hpnicfDot11UserAuthStatisType": hpnicfDot11UserAuthStatisType,
       "hpnicfDot11UserAuthStatisCnt": hpnicfDot11UserAuthStatisCnt,
       "hpnicfDot11APDeauthStatisTable": hpnicfDot11APDeauthStatisTable,
       "hpnicfDot11APDeauthStatisEntry": hpnicfDot11APDeauthStatisEntry,
       "hpnicfDot11APDeauthStatisType": hpnicfDot11APDeauthStatisType,
       "hpnicfDot11APDeauthStatisCnt": hpnicfDot11APDeauthStatisCnt,
       "hpnicfDot11APDeassocStatisTable": hpnicfDot11APDeassocStatisTable,
       "hpnicfDot11APDeassocStatisEntry": hpnicfDot11APDeassocStatisEntry,
       "hpnicfDot11APDeassocStatisType": hpnicfDot11APDeassocStatisType,
       "hpnicfDot11APDeassocStatisCnt": hpnicfDot11APDeassocStatisCnt,
       "hpnicfDot11APAssocFailStatis2Table": hpnicfDot11APAssocFailStatis2Table,
       "hpnicfDot11APAssocFailStatis2Entry": hpnicfDot11APAssocFailStatis2Entry,
       "hpnicfDot11APAssocFailStatis2Type": hpnicfDot11APAssocFailStatis2Type,
       "hpnicfDot11APAssocFailStatis2Cnt": hpnicfDot11APAssocFailStatis2Cnt,
       "hpnicfDot11APIfStatisTable": hpnicfDot11APIfStatisTable,
       "hpnicfDot11APIfStatisEntry": hpnicfDot11APIfStatisEntry,
       "hpnicfDot11APIfInPkts": hpnicfDot11APIfInPkts,
       "hpnicfDot11APIfInNormalPkts": hpnicfDot11APIfInNormalPkts,
       "hpnicfDot11APIfInErrorPkts": hpnicfDot11APIfInErrorPkts,
       "hpnicfDot11APIfOutPkts": hpnicfDot11APIfOutPkts,
       "hpnicfDot11APIfInOctets": hpnicfDot11APIfInOctets,
       "hpnicfDot11APIfOutOctets": hpnicfDot11APIfOutOctets,
       "hpnicfDot11APIfFlowOut": hpnicfDot11APIfFlowOut,
       "hpnicfDot11APIfFlowIN": hpnicfDot11APIfFlowIN,
       "hpnicfDot11APIfInUcastPkts": hpnicfDot11APIfInUcastPkts,
       "hpnicfDot11APIfInNUcastPkts": hpnicfDot11APIfInNUcastPkts,
       "hpnicfDot11APIfInDiscardPkts": hpnicfDot11APIfInDiscardPkts,
       "hpnicfDot11APIfOutUcastPkts": hpnicfDot11APIfOutUcastPkts,
       "hpnicfDot11APIfOutNUcastPkts": hpnicfDot11APIfOutNUcastPkts,
       "hpnicfDot11APIfOutDiscardPkts": hpnicfDot11APIfOutDiscardPkts,
       "hpnicfDot11APIfOutErrorPkts": hpnicfDot11APIfOutErrorPkts,
       "hpnicfDot11APIfUpdownTimes": hpnicfDot11APIfUpdownTimes,
       "hpnicfDot11APIfStatusKeepTime": hpnicfDot11APIfStatusKeepTime,
       "hpnicfDot11APIfOperStatus": hpnicfDot11APIfOperStatus,
       "hpnicfDot11APIfInBrdcastPkts": hpnicfDot11APIfInBrdcastPkts,
       "hpnicfDot11APIfOutBrdcastPkts": hpnicfDot11APIfOutBrdcastPkts,
       "hpnicfDot11APIfInMulcastPkts": hpnicfDot11APIfInMulcastPkts,
       "hpnicfDot11APIfOutMulcastPkts": hpnicfDot11APIfOutMulcastPkts,
       "hpnicfDot11APIfInPayloadOctets": hpnicfDot11APIfInPayloadOctets,
       "hpnicfDot11APIfOutPayloadOctets": hpnicfDot11APIfOutPayloadOctets,
       "hpnicfDot11RadioMngFrmStatisTable": hpnicfDot11RadioMngFrmStatisTable,
       "hpnicfDot11RadioMngFrmStatisEntry": hpnicfDot11RadioMngFrmStatisEntry,
       "hpnicfDot11MngFrmType": hpnicfDot11MngFrmType,
       "hpnicfDot11MngFrmCnt": hpnicfDot11MngFrmCnt,
       "hpnicfDot11APPacketSizeStatisTable": hpnicfDot11APPacketSizeStatisTable,
       "hpnicfDot11APPacketSizeStatisEntry": hpnicfDot11APPacketSizeStatisEntry,
       "hpnicfDot11APPacketSize": hpnicfDot11APPacketSize,
       "hpnicfDot11APRXPacketSizeCount": hpnicfDot11APRXPacketSizeCount,
       "hpnicfDot11APTXPacketSizeCount": hpnicfDot11APTXPacketSizeCount,
       "hpnicfDot11APPacketRateStatisTable": hpnicfDot11APPacketRateStatisTable,
       "hpnicfDot11APPacketRateStatisEntry": hpnicfDot11APPacketRateStatisEntry,
       "hpnicfDot11APPacketRate": hpnicfDot11APPacketRate,
       "hpnicfDot11APRXPacketRateCount": hpnicfDot11APRXPacketRateCount,
       "hpnicfDot11APTXPacketRateCount": hpnicfDot11APTXPacketRateCount,
       "hpnicfDot11APPacketMCSRateStatisTable": hpnicfDot11APPacketMCSRateStatisTable,
       "hpnicfDot11APPacketMCSRateStatisEntry": hpnicfDot11APPacketMCSRateStatisEntry,
       "hpnicfDot11APPacketMCSRate": hpnicfDot11APPacketMCSRate,
       "hpnicfDot11APRXPacketMCSRateCount": hpnicfDot11APRXPacketMCSRateCount,
       "hpnicfDot11APTXPacketMCSRateCount": hpnicfDot11APTXPacketMCSRateCount,
       "hpnicfDot11APAssocFailStatis3Table": hpnicfDot11APAssocFailStatis3Table,
       "hpnicfDot11APAssocFailStatis3Entry": hpnicfDot11APAssocFailStatis3Entry,
       "hpnicfDot11APAssocFailStatis3SRCnt": hpnicfDot11APAssocFailStatis3SRCnt,
       "hpnicfDot11APAssocFailStatis3NSRCnt": hpnicfDot11APAssocFailStatis3NSRCnt,
       "hpnicfDot11APAssocFailStatis3URCCnt": hpnicfDot11APAssocFailStatis3URCCnt,
       "hpnicfDot11APAssocFailStatis3RFCnt": hpnicfDot11APAssocFailStatis3RFCnt,
       "hpnicfDot11APAssocFailStatis3OtherCnt": hpnicfDot11APAssocFailStatis3OtherCnt,
       "hpnicfDot11APAssocFailStatisRSSILowCntCM": hpnicfDot11APAssocFailStatisRSSILowCntCM,
       "hpnicfDot11APIfStatisByAPIDTable": hpnicfDot11APIfStatisByAPIDTable,
       "hpnicfDot11APIfStatisByAPIDEntry": hpnicfDot11APIfStatisByAPIDEntry,
       "hpnicfDot11APIfInPkts2": hpnicfDot11APIfInPkts2,
       "hpnicfDot11APIfInNormalPkts2": hpnicfDot11APIfInNormalPkts2,
       "hpnicfDot11APIfInErrorPkts2": hpnicfDot11APIfInErrorPkts2,
       "hpnicfDot11APIfOutPkts2": hpnicfDot11APIfOutPkts2,
       "hpnicfDot11APIfInOctets2": hpnicfDot11APIfInOctets2,
       "hpnicfDot11APIfOutOctets2": hpnicfDot11APIfOutOctets2,
       "hpnicfDot11APIfFlowOut2": hpnicfDot11APIfFlowOut2,
       "hpnicfDot11APIfFlowIN2": hpnicfDot11APIfFlowIN2,
       "hpnicfDot11APIfInUcastPkts2": hpnicfDot11APIfInUcastPkts2,
       "hpnicfDot11APIfInNUcastPkts2": hpnicfDot11APIfInNUcastPkts2,
       "hpnicfDot11APIfInDiscardPkts2": hpnicfDot11APIfInDiscardPkts2,
       "hpnicfDot11APIfOutUcastPkts2": hpnicfDot11APIfOutUcastPkts2,
       "hpnicfDot11APIfOutNUcastPkts2": hpnicfDot11APIfOutNUcastPkts2,
       "hpnicfDot11APIfOutDiscardPkts2": hpnicfDot11APIfOutDiscardPkts2,
       "hpnicfDot11APIfOutErrorPkts2": hpnicfDot11APIfOutErrorPkts2,
       "hpnicfDot11APIfUpdownTimes2": hpnicfDot11APIfUpdownTimes2,
       "hpnicfDot11APIfStatusKeepTime2": hpnicfDot11APIfStatusKeepTime2,
       "hpnicfDot11APIfOperStatus2": hpnicfDot11APIfOperStatus2,
       "hpnicfDot11APIfInBrdcastPkts2": hpnicfDot11APIfInBrdcastPkts2,
       "hpnicfDot11APIfOutBrdcastPkts2": hpnicfDot11APIfOutBrdcastPkts2,
       "hpnicfDot11APIfInMulcastPkts2": hpnicfDot11APIfInMulcastPkts2,
       "hpnicfDot11APIfOutMulcastPkts2": hpnicfDot11APIfOutMulcastPkts2,
       "hpnicfDot11APIfInPayloadOctets2": hpnicfDot11APIfInPayloadOctets2,
       "hpnicfDot11APIfOutPayloadOctets2": hpnicfDot11APIfOutPayloadOctets2,
       "hpnicfDot11APIfInDataOctets2": hpnicfDot11APIfInDataOctets2,
       "hpnicfDot11APIfOutDataOctets2": hpnicfDot11APIfOutDataOctets2,
       "hpnicfDot11APIfAdminStatus": hpnicfDot11APIfAdminStatus,
       "hpnicfDot11APIfOperStatusCM": hpnicfDot11APIfOperStatusCM,
       "hpnicfDot11APUserSecAuthStatisTable": hpnicfDot11APUserSecAuthStatisTable,
       "hpnicfDot11APUserSecAuthStatisEntry": hpnicfDot11APUserSecAuthStatisEntry,
       "hpnicfDot11APUserAuthCurNumber": hpnicfDot11APUserAuthCurNumber,
       "hpnicfDot11APUserConnFailCnt": hpnicfDot11APUserConnFailCnt,
       "hpnicfDot11APUserAuthReqCnt": hpnicfDot11APUserAuthReqCnt,
       "hpnicfDot11APUserAuthSuccCnt": hpnicfDot11APUserAuthSuccCnt,
       "hpnicfDot11APUserAuthFailCnt": hpnicfDot11APUserAuthFailCnt,
       "hpnicfDot11AllUserOnlineTime": hpnicfDot11AllUserOnlineTime,
       "hpnicfDot11APUserInfoStatisTable": hpnicfDot11APUserInfoStatisTable,
       "hpnicfDot11APUserInfoStatisEntry": hpnicfDot11APUserInfoStatisEntry,
       "hpnicfDot11APUserMacAddr": hpnicfDot11APUserMacAddr,
       "hpnicfDot11APUserIpAddr": hpnicfDot11APUserIpAddr,
       "hpnicfDot11APUserLoginName": hpnicfDot11APUserLoginName,
       "hpnicfDot11APUserLoginTime": hpnicfDot11APUserLoginTime,
       "hpnicfDot11APUserOnlineTime": hpnicfDot11APUserOnlineTime,
       "hpnicfDot11APUserLoginNameCM": hpnicfDot11APUserLoginNameCM,
       "hpnicfDot11APUserAuthTypeCM": hpnicfDot11APUserAuthTypeCM,
       "hpnicfDot11APUserTxPacketCntCM": hpnicfDot11APUserTxPacketCntCM,
       "hpnicfDot11APUserTxBytesCM": hpnicfDot11APUserTxBytesCM,
       "hpnicfDot11APUserRxPacketCntCM": hpnicfDot11APUserRxPacketCntCM,
       "hpnicfDot11APUserRxBytesCM": hpnicfDot11APUserRxBytesCM,
       "hpnicfDot11APReassocStatis2Table": hpnicfDot11APReassocStatis2Table,
       "hpnicfDot11APReassocStatis2Entry": hpnicfDot11APReassocStatis2Entry,
       "hpnicfDot11APReassocFailStatis2Cnt": hpnicfDot11APReassocFailStatis2Cnt,
       "hpnicfDot11TrafficTable": hpnicfDot11TrafficTable,
       "hpnicfDot11TrafficEntry": hpnicfDot11TrafficEntry,
       "hpnicfDot11SSIDIndex": hpnicfDot11SSIDIndex,
       "hpnicfDot11UpPacketNumber": hpnicfDot11UpPacketNumber,
       "hpnicfDot11UpByteNumber": hpnicfDot11UpByteNumber,
       "hpnicfDot11DownPacketNumber": hpnicfDot11DownPacketNumber,
       "hpnicfDot11DownByteNumber": hpnicfDot11DownByteNumber,
       "hpnicfDot11APEchoStatisTable": hpnicfDot11APEchoStatisTable,
       "hpnicfDot11APEchoInfoStatisEntry": hpnicfDot11APEchoInfoStatisEntry,
       "hpnicfDot11APEchoAvgDelay": hpnicfDot11APEchoAvgDelay,
       "hpnicfDot11APEchoRequestCnt": hpnicfDot11APEchoRequestCnt,
       "hpnicfDot11APEchoRespLossCnt": hpnicfDot11APEchoRespLossCnt,
       "hpnicfDot11APUserSecAuthTypeStatisTable": hpnicfDot11APUserSecAuthTypeStatisTable,
       "hpnicfDot11APUserSecAuthTypeStatisEntry": hpnicfDot11APUserSecAuthTypeStatisEntry,
       "hpnicfDot11APPortalOnlineUserNum": hpnicfDot11APPortalOnlineUserNum,
       "hpnicfDot11APAuthFreeOnlineUserNum": hpnicfDot11APAuthFreeOnlineUserNum,
       "hpnicfDot11APAssocAuthOnlineUserNum": hpnicfDot11APAssocAuthOnlineUserNum,
       "hpnicfDot11APMacAuthOnlineUserNum": hpnicfDot11APMacAuthOnlineUserNum,
       "hpnicfDot11APAllPortalUserOnlineTime": hpnicfDot11APAllPortalUserOnlineTime,
       "hpnicfDot11APAllAuthFreeUserOnlineTime": hpnicfDot11APAllAuthFreeUserOnlineTime,
       "hpnicfDot11APAllAssocAuthUserOnlineTime": hpnicfDot11APAllAssocAuthUserOnlineTime,
       "hpnicfDot11APAllMacAuthUserOnlineTime": hpnicfDot11APAllMacAuthUserOnlineTime,
       "hpnicfDot11APPortalUserLostCnntCnt": hpnicfDot11APPortalUserLostCnntCnt,
       "hpnicfDot11APAuthFreeUserLostCnntCnt": hpnicfDot11APAuthFreeUserLostCnntCnt,
       "hpnicfDot11APAssocAuthUserLostCnntCnt": hpnicfDot11APAssocAuthUserLostCnntCnt,
       "hpnicfDot11APMacAuthUserLostCnntCnt": hpnicfDot11APMacAuthUserLostCnntCnt,
       "hpnicfDot11APPortalAuthReqCnt": hpnicfDot11APPortalAuthReqCnt,
       "hpnicfDot11APAssocAuthReqCnt": hpnicfDot11APAssocAuthReqCnt,
       "hpnicfDot11APMacAuthReqCnt": hpnicfDot11APMacAuthReqCnt,
       "hpnicfDot11APPortalAuthSucCnt": hpnicfDot11APPortalAuthSucCnt,
       "hpnicfDot11APAssocAuthSucCnt": hpnicfDot11APAssocAuthSucCnt,
       "hpnicfDot11APMacAuthSucCnt": hpnicfDot11APMacAuthSucCnt,
       "hpnicfDot11APPortalAuthReqFailCnt": hpnicfDot11APPortalAuthReqFailCnt,
       "hpnicfDot11APAssocAuthReqFailCnt": hpnicfDot11APAssocAuthReqFailCnt,
       "hpnicfDot11APMacAuthReqFailCnt": hpnicfDot11APMacAuthReqFailCnt,
       "hpnicfDot11APAutoAuthOnlineUserNumCM": hpnicfDot11APAutoAuthOnlineUserNumCM,
       "hpnicfDot11APAllAutoAuthUserOnlineTimeCM": hpnicfDot11APAllAutoAuthUserOnlineTimeCM,
       "hpnicfDot11APAutoAuthUserLostCnntCntCM": hpnicfDot11APAutoAuthUserLostCnntCntCM,
       "hpnicfDot11APAutoAuthReqCntCM": hpnicfDot11APAutoAuthReqCntCM,
       "hpnicfDot11APAutoAuthSucCntCM": hpnicfDot11APAutoAuthSucCntCM,
       "hpnicfDot11APAutoAuthReqFailCntCM": hpnicfDot11APAutoAuthReqFailCntCM,
       "hpnicfDot11RadioRxStatis64Table": hpnicfDot11RadioRxStatis64Table,
       "hpnicfDot11RadioRxStatis64Entry": hpnicfDot11RadioRxStatis64Entry,
       "hpnicfDot11Rx64FrameDupCnt": hpnicfDot11Rx64FrameDupCnt,
       "hpnicfDot11Rx64FrameCnt": hpnicfDot11Rx64FrameCnt,
       "hpnicfDot11Rx64UcastFrameCnt": hpnicfDot11Rx64UcastFrameCnt,
       "hpnicfDot11Rx64BcastFrameCnt": hpnicfDot11Rx64BcastFrameCnt,
       "hpnicfDot11Rx64McastFrameCnt": hpnicfDot11Rx64McastFrameCnt,
       "hpnicfDot11Rx64DiscardFrameCnt": hpnicfDot11Rx64DiscardFrameCnt,
       "hpnicfDot11Rx64FragCnt": hpnicfDot11Rx64FragCnt,
       "hpnicfDot11Rx64FcsErrCnt": hpnicfDot11Rx64FcsErrCnt,
       "hpnicfDot11Rx64FrameBytes": hpnicfDot11Rx64FrameBytes,
       "hpnicfDot11Rx64UcastFrameBytes": hpnicfDot11Rx64UcastFrameBytes,
       "hpnicfDot11Rx64BcastFrameBytes": hpnicfDot11Rx64BcastFrameBytes,
       "hpnicfDot11Rx64McastFrameBytes": hpnicfDot11Rx64McastFrameBytes,
       "hpnicfDot11Rx64DiscardFrameBytes": hpnicfDot11Rx64DiscardFrameBytes,
       "hpnicfDot11Rx64MgmtFrameCnt": hpnicfDot11Rx64MgmtFrameCnt,
       "hpnicfDot11Rx64CtrlFrameCnt": hpnicfDot11Rx64CtrlFrameCnt,
       "hpnicfDot11Rx64DataFrameCnt": hpnicfDot11Rx64DataFrameCnt,
       "hpnicfDot11Rx64DecryptErrorCnt": hpnicfDot11Rx64DecryptErrorCnt,
       "hpnicfDot11Rx64AuthenFrameCnt": hpnicfDot11Rx64AuthenFrameCnt,
       "hpnicfDot11Rx64AssociateFrameCnt": hpnicfDot11Rx64AssociateFrameCnt,
       "hpnicfDot11Rx64PhyErrorCnt": hpnicfDot11Rx64PhyErrorCnt,
       "hpnicfDot11Rx64MICErrorCnt": hpnicfDot11Rx64MICErrorCnt,
       "hpnicfDot11Rx64DataFrameBytes": hpnicfDot11Rx64DataFrameBytes,
       "hpnicfDot11Rx64PayloadBytes": hpnicfDot11Rx64PayloadBytes,
       "hpnicfDot11Rx64DataFrameBytesCM": hpnicfDot11Rx64DataFrameBytesCM,
       "hpnicfDot11RadioTxStatis64Table": hpnicfDot11RadioTxStatis64Table,
       "hpnicfDot11RadioTxStatis64Entry": hpnicfDot11RadioTxStatis64Entry,
       "hpnicfDot11Tx64FragCnt": hpnicfDot11Tx64FragCnt,
       "hpnicfDot11Tx64FailedCnt": hpnicfDot11Tx64FailedCnt,
       "hpnicfDot11Tx64RetryCnt": hpnicfDot11Tx64RetryCnt,
       "hpnicfDot11Tx64MultiRetryCnt": hpnicfDot11Tx64MultiRetryCnt,
       "hpnicfDot11Tx64RtsSuccessCnt": hpnicfDot11Tx64RtsSuccessCnt,
       "hpnicfDot11Tx64RtsFailCnt": hpnicfDot11Tx64RtsFailCnt,
       "hpnicfDot11Tx64AckFailCnt": hpnicfDot11Tx64AckFailCnt,
       "hpnicfDot11Tx64FrameCnt": hpnicfDot11Tx64FrameCnt,
       "hpnicfDot11Tx64UcastFrameCnt": hpnicfDot11Tx64UcastFrameCnt,
       "hpnicfDot11Tx64BcastFrameCnt": hpnicfDot11Tx64BcastFrameCnt,
       "hpnicfDot11Tx64McastFrameCnt": hpnicfDot11Tx64McastFrameCnt,
       "hpnicfDot11Tx64DiscardFrameCnt": hpnicfDot11Tx64DiscardFrameCnt,
       "hpnicfDot11Tx64FrameBytes": hpnicfDot11Tx64FrameBytes,
       "hpnicfDot11Tx64UcastFrameBytes": hpnicfDot11Tx64UcastFrameBytes,
       "hpnicfDot11Tx64BcastFrameBytes": hpnicfDot11Tx64BcastFrameBytes,
       "hpnicfDot11Tx64McastFrameBytes": hpnicfDot11Tx64McastFrameBytes,
       "hpnicfDot11Tx64DiscardFrameBytes": hpnicfDot11Tx64DiscardFrameBytes,
       "hpnicfDot11Tx64AuthenFrameCnt": hpnicfDot11Tx64AuthenFrameCnt,
       "hpnicfDot11Tx64AssociateFrameCnt": hpnicfDot11Tx64AssociateFrameCnt,
       "hpnicfDot11Tx64DataFrameCnt": hpnicfDot11Tx64DataFrameCnt,
       "hpnicfDot11Tx64DataFrameBytes": hpnicfDot11Tx64DataFrameBytes,
       "hpnicfDot11Tx64MSDUCnt": hpnicfDot11Tx64MSDUCnt,
       "hpnicfDot11Tx64DiscardMSDUCnt": hpnicfDot11Tx64DiscardMSDUCnt,
       "hpnicfDot11Tx64RetryMSDUCnt": hpnicfDot11Tx64RetryMSDUCnt,
       "hpnicfDot11Tx64PayloadBytes": hpnicfDot11Tx64PayloadBytes,
       "hpnicfDot11Tx64MgtFrameCnt": hpnicfDot11Tx64MgtFrameCnt,
       "hpnicfDot11Tx64CtrlFrameCnt": hpnicfDot11Tx64CtrlFrameCnt,
       "hpnicfDot11Tx64MACErrCnt": hpnicfDot11Tx64MACErrCnt,
       "hpnicfDot11Tx64ErrFrameCnt": hpnicfDot11Tx64ErrFrameCnt,
       "hpnicfDot11BSSRxStatis64Table": hpnicfDot11BSSRxStatis64Table,
       "hpnicfDot11BSSRxStatis64Entry": hpnicfDot11BSSRxStatis64Entry,
       "hpnicfDot11BSSRx64FrameCnt": hpnicfDot11BSSRx64FrameCnt,
       "hpnicfDot11BSSRx64FrameBytes": hpnicfDot11BSSRx64FrameBytes,
       "hpnicfDot11BSSRx64DataFrameCnt": hpnicfDot11BSSRx64DataFrameCnt,
       "hpnicfDot11BSSRx64DataFrameBytes": hpnicfDot11BSSRx64DataFrameBytes,
       "hpnicfDot11BSSRx64AssocFrameCnt": hpnicfDot11BSSRx64AssocFrameCnt,
       "hpnicfDot11BSSRx64PayloadBytes": hpnicfDot11BSSRx64PayloadBytes,
       "hpnicfDot11BSSRx64UniFrameCnt": hpnicfDot11BSSRx64UniFrameCnt,
       "hpnicfDot11BSSRx64NonUniFrameCnt": hpnicfDot11BSSRx64NonUniFrameCnt,
       "hpnicfDot11BSSRx64AuthenFrameCnt": hpnicfDot11BSSRx64AuthenFrameCnt,
       "hpnicfDot11BSSTxStatis64Table": hpnicfDot11BSSTxStatis64Table,
       "hpnicfDot11BSSTxStatis64Entry": hpnicfDot11BSSTxStatis64Entry,
       "hpnicfDot11BSSTx64FrameCnt": hpnicfDot11BSSTx64FrameCnt,
       "hpnicfDot11BSSTx64FrameBytes": hpnicfDot11BSSTx64FrameBytes,
       "hpnicfDot11BSSTx64DataFrameCnt": hpnicfDot11BSSTx64DataFrameCnt,
       "hpnicfDot11BSSTx64DataFrameBytes": hpnicfDot11BSSTx64DataFrameBytes,
       "hpnicfDot11BSSTx64AssocFrameCnt": hpnicfDot11BSSTx64AssocFrameCnt,
       "hpnicfDot11BSSTx64PayloadBytes": hpnicfDot11BSSTx64PayloadBytes,
       "hpnicfDot11BSSTx64RetryCnt": hpnicfDot11BSSTx64RetryCnt,
       "hpnicfDot11BSSTx64UniFrameCnt": hpnicfDot11BSSTx64UniFrameCnt,
       "hpnicfDot11BSSTx64NonUniFrameCnt": hpnicfDot11BSSTx64NonUniFrameCnt,
       "hpnicfDot11BSSTx64AuthenFrameCnt": hpnicfDot11BSSTx64AuthenFrameCnt,
       "hpnicfDot11APPacketMCSRateStatis2Table": hpnicfDot11APPacketMCSRateStatis2Table,
       "hpnicfDot11APPacketMCSRateStatis2Entry": hpnicfDot11APPacketMCSRateStatis2Entry,
       "hpnicfDot11APPacketMCS2Rate": hpnicfDot11APPacketMCS2Rate,
       "hpnicfDot11APRXPacketMCSRate2Count": hpnicfDot11APRXPacketMCSRate2Count,
       "hpnicfDot11APTXPacketMCSRate2Count": hpnicfDot11APTXPacketMCSRate2Count,
       "hpnicfDot11APUserSecAuthStatisCMTable": hpnicfDot11APUserSecAuthStatisCMTable,
       "hpnicfDot11APUserSecAuthStatisCMEntry": hpnicfDot11APUserSecAuthStatisCMEntry,
       "hpnicfDot11APUserConnFailCntCM": hpnicfDot11APUserConnFailCntCM,
       "hpnicfDot11APUserAuthReqCntCM": hpnicfDot11APUserAuthReqCntCM,
       "hpnicfDot11APUserAuthSuccCntCM": hpnicfDot11APUserAuthSuccCntCM,
       "hpnicfDot11APUserAuthFailCntCM": hpnicfDot11APUserAuthFailCntCM,
       "hpnicfDot11AllUserOnlineTimeCM": hpnicfDot11AllUserOnlineTimeCM,
       "hpnicfDot11APMtNotifyGroup": hpnicfDot11APMtNotifyGroup,
       "hpnicfDot11APMtTraps": hpnicfDot11APMtTraps,
       "hpnicfDot11APMtWorkModeChgTrap": hpnicfDot11APMtWorkModeChgTrap,
       "hpnicfDot11APMtCfgErrorTrap": hpnicfDot11APMtCfgErrorTrap,
       "hpnicfDot11APMtRadioFailTrap": hpnicfDot11APMtRadioFailTrap,
       "hpnicfDot11APMtRadioFailRecoverTrap": hpnicfDot11APMtRadioFailRecoverTrap,
       "hpnicfDot11APMtRdoChanlChgTrap": hpnicfDot11APMtRdoChanlChgTrap,
       "hpnicfDot11APMtTimeSynFail": hpnicfDot11APMtTimeSynFail,
       "hpnicfDot11APMtChlIntfDetected": hpnicfDot11APMtChlIntfDetected,
       "hpnicfDot11APMtIntfAPDetected": hpnicfDot11APMtIntfAPDetected,
       "hpnicfDot11APMtIntfStaDetected": hpnicfDot11APMtIntfStaDetected,
       "hpnicfDot11APMtIPChange": hpnicfDot11APMtIPChange,
       "hpnicfDot11APFlashWriteFailure": hpnicfDot11APFlashWriteFailure,
       "hpnicfDot11APSysReboot": hpnicfDot11APSysReboot,
       "hpnicfDot11APMtAvailChlTooLow": hpnicfDot11APMtAvailChlTooLow,
       "hpnicfDot11APImgDwldSuccess": hpnicfDot11APImgDwldSuccess,
       "hpnicfDot11APInterfDetectedTrap": hpnicfDot11APInterfDetectedTrap,
       "hpnicfDot11APInterfClearTrap": hpnicfDot11APInterfClearTrap,
       "hpnicfDot11StaInterfDetectedTrap": hpnicfDot11StaInterfDetectedTrap,
       "hpnicfDot11StaInterfClearTrap": hpnicfDot11StaInterfClearTrap,
       "hpnicfDot11OtherDevIntDetectedTrap": hpnicfDot11OtherDevIntDetectedTrap,
       "hpnicfDot11OtherDevIntClearTrap": hpnicfDot11OtherDevIntClearTrap,
       "hpnicfDot11APModuleTroubleTrap": hpnicfDot11APModuleTroubleTrap,
       "hpnicfDot11APModuleTroubleClearTrap": hpnicfDot11APModuleTroubleClearTrap,
       "hpnicfDot11APRadioDownTrap": hpnicfDot11APRadioDownTrap,
       "hpnicfDot11APRadioDownRecovTrap": hpnicfDot11APRadioDownRecovTrap,
       "hpnicfDot11APStaFullTrap": hpnicfDot11APStaFullTrap,
       "hpnicfDot11APStaFullRecoverTrap": hpnicfDot11APStaFullRecoverTrap,
       "hpnicfDot11DFSFreeCntBelowThrRecov": hpnicfDot11DFSFreeCntBelowThrRecov,
       "hpnicfDot11APCpuUsageHigh": hpnicfDot11APCpuUsageHigh,
       "hpnicfDot11APCpuUsageHighRecover": hpnicfDot11APCpuUsageHighRecover,
       "hpnicfDot11APMemUsageHigh": hpnicfDot11APMemUsageHigh,
       "hpnicfDot11APMemUsageHighRecover": hpnicfDot11APMemUsageHighRecover,
       "hpnicfDot11APTrapUserCntExceedThre": hpnicfDot11APTrapUserCntExceedThre,
       "hpnicfDot11APMtDetectedIntfAP": hpnicfDot11APMtDetectedIntfAP,
       "hpnicfDot11APMtDetectedIntfSTA": hpnicfDot11APMtDetectedIntfSTA,
       "hpnicfDot11APMtDetectedIntfOtherDev": hpnicfDot11APMtDetectedIntfOtherDev,
       "hpnicfDot11DetcAdjChlIntfAP": hpnicfDot11DetcAdjChlIntfAP,
       "hpnicfDot11DetcAdjChlIntfAPClear": hpnicfDot11DetcAdjChlIntfAPClear,
       "hpnicfDot11APMtTrapVarObjects": hpnicfDot11APMtTrapVarObjects,
       "hpnicfDot11APMtTrapCfgErrReason": hpnicfDot11APMtTrapCfgErrReason,
       "hpnicfDot11APMtTrapRadioFailReason": hpnicfDot11APMtTrapRadioFailReason,
       "hpnicfDot11APMtTrapOldChannel": hpnicfDot11APMtTrapOldChannel,
       "hpnicfDot11APMtTrapNewChannel": hpnicfDot11APMtTrapNewChannel,
       "hpnicfDot11APChannelChgMode": hpnicfDot11APChannelChgMode,
       "hpnicfDot11APChgWorkMode": hpnicfDot11APChgWorkMode,
       "hpnicfDot11APIntfDevMACAddress": hpnicfDot11APIntfDevMACAddress,
       "hpnicfDot11APMtTrapOldIPAddr": hpnicfDot11APMtTrapOldIPAddr,
       "hpnicfDot11CurrInterfDetectedNum": hpnicfDot11CurrInterfDetectedNum,
       "hpnicfDot11StaFullReason": hpnicfDot11StaFullReason,
       "hpnicfDot11StaLimitNumber": hpnicfDot11StaLimitNumber,
       "hpnicfDot11APRadioDownReason": hpnicfDot11APRadioDownReason,
       "hpnicfDot11InterfMacList": hpnicfDot11InterfMacList,
       "hpnicfDot11APTrapUserCnt": hpnicfDot11APTrapUserCnt,
       "hpnicfDot11APTrapUserThreshold": hpnicfDot11APTrapUserThreshold,
       "hpnicfDot11APMtChanlChgCount": hpnicfDot11APMtChanlChgCount,
       "hpnicfDot11APMtFormerApVersion": hpnicfDot11APMtFormerApVersion,
       "hpnicfDot11APMtAPID": hpnicfDot11APMtAPID,
       "hpnicfDot11APMtRadioID": hpnicfDot11APMtRadioID,
       "hpnicfDot11APMtChannel": hpnicfDot11APMtChannel,
       "hpnicfDot11APMtInterfMacAdd": hpnicfDot11APMtInterfMacAdd,
       "hpnicfDot11APMtAdjChannel": hpnicfDot11APMtAdjChannel,
       "hpnicfDot11APMtFirstTrapTime": hpnicfDot11APMtFirstTrapTime,
       "hpnicfDot11APMtTrapAPMacAddress": hpnicfDot11APMtTrapAPMacAddress}
)
