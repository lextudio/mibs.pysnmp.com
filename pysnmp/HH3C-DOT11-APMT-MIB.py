# SNMP MIB module (HH3C-DOT11-APMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-APMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:49 2024
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

(Hh3cDot11ChannelScopeType,
 Hh3cDot11MACModeType,
 Hh3cDot11NotifyReasonType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RFModeType,
 Hh3cDot11RadioElementIndex,
 Hh3cDot11RadioScopeType,
 Hh3cDot11SSIDStringType,
 Hh3cDot11ServicePolicyIDType,
 Hh3cDot11TxPwrLevelScopeType,
 hh3cDot11,
 hh3cDot11APElementIndex) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11MACModeType",
    "Hh3cDot11NotifyReasonType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RFModeType",
    "Hh3cDot11RadioElementIndex",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11SSIDStringType",
    "Hh3cDot11ServicePolicyIDType",
    "Hh3cDot11TxPwrLevelScopeType",
    "hh3cDot11",
    "hh3cDot11APElementIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11APMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2)
)
hh3cDot11APMT.setRevisions(
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

_Hh3cDot11APObjectGroup_ObjectIdentity = ObjectIdentity
hh3cDot11APObjectGroup = _Hh3cDot11APObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1)
)
_Hh3cDot11APObjectStatusTable_Object = MibTable
hh3cDot11APObjectStatusTable = _Hh3cDot11APObjectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APObjectStatusTable.setStatus("current")
_Hh3cDot11APObjectStatusEntry_Object = MibTableRow
hh3cDot11APObjectStatusEntry = _Hh3cDot11APObjectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1)
)
hh3cDot11APObjectStatusEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APObjectStatusEntry.setStatus("current")
_Hh3cDot11APID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11APID_Object = MibTableColumn
hh3cDot11APID = _Hh3cDot11APID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 1),
    _Hh3cDot11APID_Type()
)
hh3cDot11APID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APID.setStatus("current")
_Hh3cDot11APIPAddress_Type = IpAddress
_Hh3cDot11APIPAddress_Object = MibTableColumn
hh3cDot11APIPAddress = _Hh3cDot11APIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 2),
    _Hh3cDot11APIPAddress_Type()
)
hh3cDot11APIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIPAddress.setStatus("current")
_Hh3cDot11APMacAddress_Type = MacAddress
_Hh3cDot11APMacAddress_Object = MibTableColumn
hh3cDot11APMacAddress = _Hh3cDot11APMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 3),
    _Hh3cDot11APMacAddress_Type()
)
hh3cDot11APMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAddress.setStatus("current")


class _Hh3cDot11APOperationStatus_Type(Integer32):
    """Custom type hh3cDot11APOperationStatus based on Integer32"""
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


_Hh3cDot11APOperationStatus_Type.__name__ = "Integer32"
_Hh3cDot11APOperationStatus_Object = MibTableColumn
hh3cDot11APOperationStatus = _Hh3cDot11APOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 4),
    _Hh3cDot11APOperationStatus_Type()
)
hh3cDot11APOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APOperationStatus.setStatus("current")
_Hh3cDot11APTemplateNameOfAP_Type = OctetString
_Hh3cDot11APTemplateNameOfAP_Object = MibTableColumn
hh3cDot11APTemplateNameOfAP = _Hh3cDot11APTemplateNameOfAP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 5),
    _Hh3cDot11APTemplateNameOfAP_Type()
)
hh3cDot11APTemplateNameOfAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateNameOfAP.setStatus("current")
_Hh3cDot11APReset_Type = TruthValue
_Hh3cDot11APReset_Object = MibTableColumn
hh3cDot11APReset = _Hh3cDot11APReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 6),
    _Hh3cDot11APReset_Type()
)
hh3cDot11APReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APReset.setStatus("current")


class _Hh3cDot11APCpuUsage_Type(Integer32):
    """Custom type hh3cDot11APCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCpuUsage_Type.__name__ = "Integer32"
_Hh3cDot11APCpuUsage_Object = MibTableColumn
hh3cDot11APCpuUsage = _Hh3cDot11APCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 7),
    _Hh3cDot11APCpuUsage_Type()
)
hh3cDot11APCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsage.setUnits("onepercent")


class _Hh3cDot11APConnectionType_Type(Integer32):
    """Custom type hh3cDot11APConnectionType based on Integer32"""
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


_Hh3cDot11APConnectionType_Type.__name__ = "Integer32"
_Hh3cDot11APConnectionType_Object = MibTableColumn
hh3cDot11APConnectionType = _Hh3cDot11APConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 8),
    _Hh3cDot11APConnectionType_Type()
)
hh3cDot11APConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConnectionType.setStatus("current")
_Hh3cDot11APLastImgDownloadTime_Type = DateAndTime
_Hh3cDot11APLastImgDownloadTime_Object = MibTableColumn
hh3cDot11APLastImgDownloadTime = _Hh3cDot11APLastImgDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 9),
    _Hh3cDot11APLastImgDownloadTime_Type()
)
hh3cDot11APLastImgDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLastImgDownloadTime.setStatus("current")
_Hh3cDot11APIPv6Address_Type = OctetString
_Hh3cDot11APIPv6Address_Object = MibTableColumn
hh3cDot11APIPv6Address = _Hh3cDot11APIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 10),
    _Hh3cDot11APIPv6Address_Type()
)
hh3cDot11APIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIPv6Address.setStatus("current")
_Hh3cDot11APLastRegisterTime_Type = DateAndTime
_Hh3cDot11APLastRegisterTime_Object = MibTableColumn
hh3cDot11APLastRegisterTime = _Hh3cDot11APLastRegisterTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 11),
    _Hh3cDot11APLastRegisterTime_Type()
)
hh3cDot11APLastRegisterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLastRegisterTime.setStatus("current")


class _Hh3cDot11APResetCM_Type(Integer32):
    """Custom type hh3cDot11APResetCM based on Integer32"""
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


_Hh3cDot11APResetCM_Type.__name__ = "Integer32"
_Hh3cDot11APResetCM_Object = MibTableColumn
hh3cDot11APResetCM = _Hh3cDot11APResetCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 1, 1, 12),
    _Hh3cDot11APResetCM_Type()
)
hh3cDot11APResetCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APResetCM.setStatus("current")
_Hh3cDot11APObjectTable_Object = MibTable
hh3cDot11APObjectTable = _Hh3cDot11APObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11APObjectTable.setStatus("current")
_Hh3cDot11APObjectEntry_Object = MibTableRow
hh3cDot11APObjectEntry = _Hh3cDot11APObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1)
)
hh3cDot11APObjectEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APObjID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APObjectEntry.setStatus("current")
_Hh3cDot11APObjID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11APObjID_Object = MibTableColumn
hh3cDot11APObjID = _Hh3cDot11APObjID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 1),
    _Hh3cDot11APObjID_Type()
)
hh3cDot11APObjID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APObjID.setStatus("current")
_Hh3cDot11CurrAPIPAddress_Type = IpAddress
_Hh3cDot11CurrAPIPAddress_Object = MibTableColumn
hh3cDot11CurrAPIPAddress = _Hh3cDot11CurrAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 2),
    _Hh3cDot11CurrAPIPAddress_Type()
)
hh3cDot11CurrAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPIPAddress.setStatus("current")
_Hh3cDot11CurrAPMacAddress_Type = MacAddress
_Hh3cDot11CurrAPMacAddress_Object = MibTableColumn
hh3cDot11CurrAPMacAddress = _Hh3cDot11CurrAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 3),
    _Hh3cDot11CurrAPMacAddress_Type()
)
hh3cDot11CurrAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMacAddress.setStatus("current")
_Hh3cDot11CurrACPortIndex_Type = Integer32
_Hh3cDot11CurrACPortIndex_Object = MibTableColumn
hh3cDot11CurrACPortIndex = _Hh3cDot11CurrACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 4),
    _Hh3cDot11CurrACPortIndex_Type()
)
hh3cDot11CurrACPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrACPortIndex.setStatus("current")
_Hh3cDot11CurrAPMACMode_Type = Hh3cDot11MACModeType
_Hh3cDot11CurrAPMACMode_Object = MibTableColumn
hh3cDot11CurrAPMACMode = _Hh3cDot11CurrAPMACMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 5),
    _Hh3cDot11CurrAPMACMode_Type()
)
hh3cDot11CurrAPMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMACMode.setStatus("current")
_Hh3cDot11CurrAPTemplateName_Type = OctetString
_Hh3cDot11CurrAPTemplateName_Object = MibTableColumn
hh3cDot11CurrAPTemplateName = _Hh3cDot11CurrAPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 6),
    _Hh3cDot11CurrAPTemplateName_Type()
)
hh3cDot11CurrAPTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPTemplateName.setStatus("current")
_Hh3cDot11CurrAPStationAssocCount_Type = Integer32
_Hh3cDot11CurrAPStationAssocCount_Object = MibTableColumn
hh3cDot11CurrAPStationAssocCount = _Hh3cDot11CurrAPStationAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 7),
    _Hh3cDot11CurrAPStationAssocCount_Type()
)
hh3cDot11CurrAPStationAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPStationAssocCount.setStatus("current")
_Hh3cDot11CurrAPName_Type = OctetString
_Hh3cDot11CurrAPName_Object = MibTableColumn
hh3cDot11CurrAPName = _Hh3cDot11CurrAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 8),
    _Hh3cDot11CurrAPName_Type()
)
hh3cDot11CurrAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPName.setStatus("current")
_Hh3cDot11CurrAPModelName_Type = OctetString
_Hh3cDot11CurrAPModelName_Object = MibTableColumn
hh3cDot11CurrAPModelName = _Hh3cDot11CurrAPModelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 9),
    _Hh3cDot11CurrAPModelName_Type()
)
hh3cDot11CurrAPModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPModelName.setStatus("current")
_Hh3cDot11CurrAPImageName_Type = OctetString
_Hh3cDot11CurrAPImageName_Object = MibTableColumn
hh3cDot11CurrAPImageName = _Hh3cDot11CurrAPImageName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 10),
    _Hh3cDot11CurrAPImageName_Type()
)
hh3cDot11CurrAPImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPImageName.setStatus("current")
_Hh3cDot11CurrAPSoftwareVersion_Type = OctetString
_Hh3cDot11CurrAPSoftwareVersion_Object = MibTableColumn
hh3cDot11CurrAPSoftwareVersion = _Hh3cDot11CurrAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 11),
    _Hh3cDot11CurrAPSoftwareVersion_Type()
)
hh3cDot11CurrAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPSoftwareVersion.setStatus("current")
_Hh3cDot11CurrAPIPNetMask_Type = IpAddress
_Hh3cDot11CurrAPIPNetMask_Object = MibTableColumn
hh3cDot11CurrAPIPNetMask = _Hh3cDot11CurrAPIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 12),
    _Hh3cDot11CurrAPIPNetMask_Type()
)
hh3cDot11CurrAPIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPIPNetMask.setStatus("current")
_Hh3cDot11CurrRadioModeSupport_Type = Integer32
_Hh3cDot11CurrRadioModeSupport_Object = MibTableColumn
hh3cDot11CurrRadioModeSupport = _Hh3cDot11CurrRadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 13),
    _Hh3cDot11CurrRadioModeSupport_Type()
)
hh3cDot11CurrRadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrRadioModeSupport.setStatus("current")
_Hh3cDot11CurrIfNumber_Type = Integer32
_Hh3cDot11CurrIfNumber_Object = MibTableColumn
hh3cDot11CurrIfNumber = _Hh3cDot11CurrIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 14),
    _Hh3cDot11CurrIfNumber_Type()
)
hh3cDot11CurrIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrIfNumber.setStatus("current")
_Hh3cDot11CurrAPElementID_Type = Integer32
_Hh3cDot11CurrAPElementID_Object = MibTableColumn
hh3cDot11CurrAPElementID = _Hh3cDot11CurrAPElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 15),
    _Hh3cDot11CurrAPElementID_Type()
)
hh3cDot11CurrAPElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPElementID.setStatus("current")


class _Hh3cDot11CurrAPMode_Type(Integer32):
    """Custom type hh3cDot11CurrAPMode based on Integer32"""
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


_Hh3cDot11CurrAPMode_Type.__name__ = "Integer32"
_Hh3cDot11CurrAPMode_Object = MibTableColumn
hh3cDot11CurrAPMode = _Hh3cDot11CurrAPMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 16),
    _Hh3cDot11CurrAPMode_Type()
)
hh3cDot11CurrAPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMode.setStatus("current")
_Hh3cDot11CurrAPIPv6Address_Type = OctetString
_Hh3cDot11CurrAPIPv6Address_Object = MibTableColumn
hh3cDot11CurrAPIPv6Address = _Hh3cDot11CurrAPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 17),
    _Hh3cDot11CurrAPIPv6Address_Type()
)
hh3cDot11CurrAPIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPIPv6Address.setStatus("current")
_Hh3cDot11CurrAPSSIDNumber_Type = Integer32
_Hh3cDot11CurrAPSSIDNumber_Object = MibTableColumn
hh3cDot11CurrAPSSIDNumber = _Hh3cDot11CurrAPSSIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 18),
    _Hh3cDot11CurrAPSSIDNumber_Type()
)
hh3cDot11CurrAPSSIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPSSIDNumber.setStatus("current")
_Hh3cDot11CurrAPManufacturer_Type = OctetString
_Hh3cDot11CurrAPManufacturer_Object = MibTableColumn
hh3cDot11CurrAPManufacturer = _Hh3cDot11CurrAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 19),
    _Hh3cDot11CurrAPManufacturer_Type()
)
hh3cDot11CurrAPManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPManufacturer.setStatus("current")
_Hh3cDot11CurrAPMemorySize_Type = Integer32
_Hh3cDot11CurrAPMemorySize_Object = MibTableColumn
hh3cDot11CurrAPMemorySize = _Hh3cDot11CurrAPMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 20),
    _Hh3cDot11CurrAPMemorySize_Type()
)
hh3cDot11CurrAPMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMemorySize.setUnits("kbytes")
_Hh3cDot11CurrAPMemSizeInBytes_Type = Integer32
_Hh3cDot11CurrAPMemSizeInBytes_Object = MibTableColumn
hh3cDot11CurrAPMemSizeInBytes = _Hh3cDot11CurrAPMemSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 21),
    _Hh3cDot11CurrAPMemSizeInBytes_Type()
)
hh3cDot11CurrAPMemSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMemSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMemSizeInBytes.setUnits("bytes")
_Hh3cDot11CurrAPFlashSize_Type = Integer32
_Hh3cDot11CurrAPFlashSize_Object = MibTableColumn
hh3cDot11CurrAPFlashSize = _Hh3cDot11CurrAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 22),
    _Hh3cDot11CurrAPFlashSize_Type()
)
hh3cDot11CurrAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPFlashSize.setUnits("Kbytes")
_Hh3cDot11CurrAPFlashSizeInBytes_Type = Integer32
_Hh3cDot11CurrAPFlashSizeInBytes_Object = MibTableColumn
hh3cDot11CurrAPFlashSizeInBytes = _Hh3cDot11CurrAPFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 23),
    _Hh3cDot11CurrAPFlashSizeInBytes_Type()
)
hh3cDot11CurrAPFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPFlashSizeInBytes.setUnits("bytes")
_Hh3cDot11CurrAPReleasedVersion_Type = OctetString
_Hh3cDot11CurrAPReleasedVersion_Object = MibTableColumn
hh3cDot11CurrAPReleasedVersion = _Hh3cDot11CurrAPReleasedVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 24),
    _Hh3cDot11CurrAPReleasedVersion_Type()
)
hh3cDot11CurrAPReleasedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPReleasedVersion.setStatus("current")
_Hh3cDot11CurrRadioModeSupport2_Type = Integer32
_Hh3cDot11CurrRadioModeSupport2_Object = MibTableColumn
hh3cDot11CurrRadioModeSupport2 = _Hh3cDot11CurrRadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 25),
    _Hh3cDot11CurrRadioModeSupport2_Type()
)
hh3cDot11CurrRadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrRadioModeSupport2.setStatus("current")
_Hh3cDot11CurrAPCPUTypeCM_Type = OctetString
_Hh3cDot11CurrAPCPUTypeCM_Object = MibTableColumn
hh3cDot11CurrAPCPUTypeCM = _Hh3cDot11CurrAPCPUTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 26),
    _Hh3cDot11CurrAPCPUTypeCM_Type()
)
hh3cDot11CurrAPCPUTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPCPUTypeCM.setStatus("current")
_Hh3cDot11CurrAPMemoryTypeCM_Type = OctetString
_Hh3cDot11CurrAPMemoryTypeCM_Object = MibTableColumn
hh3cDot11CurrAPMemoryTypeCM = _Hh3cDot11CurrAPMemoryTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 27),
    _Hh3cDot11CurrAPMemoryTypeCM_Type()
)
hh3cDot11CurrAPMemoryTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPMemoryTypeCM.setStatus("current")
_Hh3cDot11CurrAPBSSIDNumberCM_Type = Integer32
_Hh3cDot11CurrAPBSSIDNumberCM_Object = MibTableColumn
hh3cDot11CurrAPBSSIDNumberCM = _Hh3cDot11CurrAPBSSIDNumberCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 2, 1, 28),
    _Hh3cDot11CurrAPBSSIDNumberCM_Type()
)
hh3cDot11CurrAPBSSIDNumberCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPBSSIDNumberCM.setStatus("current")
_Hh3cDot11APRadioTable_Object = MibTable
hh3cDot11APRadioTable = _Hh3cDot11APRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11APRadioTable.setStatus("current")
_Hh3cDot11APRadioEntry_Object = MibTableRow
hh3cDot11APRadioEntry = _Hh3cDot11APRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1)
)
hh3cDot11APRadioEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APRadioEntry.setStatus("current")


class _Hh3cDot11CurAPID_Type(OctetString):
    """Custom type hh3cDot11CurAPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cDot11CurAPID_Type.__name__ = "OctetString"
_Hh3cDot11CurAPID_Object = MibTableColumn
hh3cDot11CurAPID = _Hh3cDot11CurAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 1),
    _Hh3cDot11CurAPID_Type()
)
hh3cDot11CurAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11CurAPID.setStatus("current")


class _Hh3cDot11RadioID_Type(Integer32):
    """Custom type hh3cDot11RadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11RadioID_Type.__name__ = "Integer32"
_Hh3cDot11RadioID_Object = MibTableColumn
hh3cDot11RadioID = _Hh3cDot11RadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 2),
    _Hh3cDot11RadioID_Type()
)
hh3cDot11RadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11RadioID.setStatus("current")
_Hh3cDot11AdminStatus_Type = TruthValue
_Hh3cDot11AdminStatus_Object = MibTableColumn
hh3cDot11AdminStatus = _Hh3cDot11AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 3),
    _Hh3cDot11AdminStatus_Type()
)
hh3cDot11AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AdminStatus.setStatus("current")
_Hh3cDot11OperStatus_Type = TruthValue
_Hh3cDot11OperStatus_Object = MibTableColumn
hh3cDot11OperStatus = _Hh3cDot11OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 4),
    _Hh3cDot11OperStatus_Type()
)
hh3cDot11OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11OperStatus.setStatus("current")
_Hh3cDot11Channel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11Channel_Object = MibTableColumn
hh3cDot11Channel = _Hh3cDot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 5),
    _Hh3cDot11Channel_Type()
)
hh3cDot11Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Channel.setStatus("current")
_Hh3cDot11TxPowerLevel_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11TxPowerLevel_Object = MibTableColumn
hh3cDot11TxPowerLevel = _Hh3cDot11TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 6),
    _Hh3cDot11TxPowerLevel_Type()
)
hh3cDot11TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11TxPowerLevel.setUnits("dbm")
_Hh3cDot11APRadioIfIndex_Type = Integer32
_Hh3cDot11APRadioIfIndex_Object = MibTableColumn
hh3cDot11APRadioIfIndex = _Hh3cDot11APRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 7),
    _Hh3cDot11APRadioIfIndex_Type()
)
hh3cDot11APRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APRadioIfIndex.setStatus("current")
_Hh3cDot11AntennaGain_Type = Integer32
_Hh3cDot11AntennaGain_Object = MibTableColumn
hh3cDot11AntennaGain = _Hh3cDot11AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 8),
    _Hh3cDot11AntennaGain_Type()
)
hh3cDot11AntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AntennaGain.setUnits("dBi")
_Hh3cDot11MaxBandwidth_Type = Integer32
_Hh3cDot11MaxBandwidth_Object = MibTableColumn
hh3cDot11MaxBandwidth = _Hh3cDot11MaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 9),
    _Hh3cDot11MaxBandwidth_Type()
)
hh3cDot11MaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MaxBandwidth.setUnits("Mbps")
_Hh3cDot11ResourceUseRatio_Type = Integer32
_Hh3cDot11ResourceUseRatio_Object = MibTableColumn
hh3cDot11ResourceUseRatio = _Hh3cDot11ResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 10),
    _Hh3cDot11ResourceUseRatio_Type()
)
hh3cDot11ResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ResourceUseRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11ResourceUseRatio.setUnits("onepercent")
_Hh3cDot11RadioModeSupport_Type = Unsigned32
_Hh3cDot11RadioModeSupport_Object = MibTableColumn
hh3cDot11RadioModeSupport = _Hh3cDot11RadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 11),
    _Hh3cDot11RadioModeSupport_Type()
)
hh3cDot11RadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioModeSupport.setStatus("current")


class _Hh3cDot11TxPowerLevel2_Type(Integer32):
    """Custom type hh3cDot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hh3cDot11TxPowerLevel2_Type.__name__ = "Integer32"
_Hh3cDot11TxPowerLevel2_Object = MibTableColumn
hh3cDot11TxPowerLevel2 = _Hh3cDot11TxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 12),
    _Hh3cDot11TxPowerLevel2_Type()
)
hh3cDot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxPowerLevel2.setStatus("current")
_Hh3cDot11PowerMgmtStatus_Type = TruthValue
_Hh3cDot11PowerMgmtStatus_Object = MibTableColumn
hh3cDot11PowerMgmtStatus = _Hh3cDot11PowerMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 13),
    _Hh3cDot11PowerMgmtStatus_Type()
)
hh3cDot11PowerMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PowerMgmtStatus.setStatus("current")
_Hh3cDot11ChannelSwitchTimes_Type = Counter32
_Hh3cDot11ChannelSwitchTimes_Object = MibTableColumn
hh3cDot11ChannelSwitchTimes = _Hh3cDot11ChannelSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 14),
    _Hh3cDot11ChannelSwitchTimes_Type()
)
hh3cDot11ChannelSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ChannelSwitchTimes.setStatus("current")
_Hh3cDot11AntennaType_Type = OctetString
_Hh3cDot11AntennaType_Object = MibTableColumn
hh3cDot11AntennaType = _Hh3cDot11AntennaType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 15),
    _Hh3cDot11AntennaType_Type()
)
hh3cDot11AntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AntennaType.setStatus("current")
_Hh3cDot11DiversitySelectionRx_Type = TruthValue
_Hh3cDot11DiversitySelectionRx_Object = MibTableColumn
hh3cDot11DiversitySelectionRx = _Hh3cDot11DiversitySelectionRx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 16),
    _Hh3cDot11DiversitySelectionRx_Type()
)
hh3cDot11DiversitySelectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DiversitySelectionRx.setStatus("current")
_Hh3cDot11MaxTxPwrLvl_Type = OctetString
_Hh3cDot11MaxTxPwrLvl_Object = MibTableColumn
hh3cDot11MaxTxPwrLvl = _Hh3cDot11MaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 17),
    _Hh3cDot11MaxTxPwrLvl_Type()
)
hh3cDot11MaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxTxPwrLvl.setStatus("current")
_Hh3cDot11PwrAttRange_Type = Integer32
_Hh3cDot11PwrAttRange_Object = MibTableColumn
hh3cDot11PwrAttRange = _Hh3cDot11PwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 18),
    _Hh3cDot11PwrAttRange_Type()
)
hh3cDot11PwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PwrAttRange.setStatus("current")
_Hh3cDot11AvgRxSignalStrength_Type = Integer32
_Hh3cDot11AvgRxSignalStrength_Object = MibTableColumn
hh3cDot11AvgRxSignalStrength = _Hh3cDot11AvgRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 19),
    _Hh3cDot11AvgRxSignalStrength_Type()
)
hh3cDot11AvgRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AvgRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AvgRxSignalStrength.setUnits("dBm")
_Hh3cDot11HighestRxSignalStrength_Type = Integer32
_Hh3cDot11HighestRxSignalStrength_Object = MibTableColumn
hh3cDot11HighestRxSignalStrength = _Hh3cDot11HighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 20),
    _Hh3cDot11HighestRxSignalStrength_Type()
)
hh3cDot11HighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11HighestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11HighestRxSignalStrength.setUnits("dBm")
_Hh3cDot11LowestRxSignalStrength_Type = Integer32
_Hh3cDot11LowestRxSignalStrength_Object = MibTableColumn
hh3cDot11LowestRxSignalStrength = _Hh3cDot11LowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 21),
    _Hh3cDot11LowestRxSignalStrength_Type()
)
hh3cDot11LowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LowestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LowestRxSignalStrength.setUnits("dBm")
_Hh3cDot11RadioIfUpdownTimes_Type = Counter32
_Hh3cDot11RadioIfUpdownTimes_Object = MibTableColumn
hh3cDot11RadioIfUpdownTimes = _Hh3cDot11RadioIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 22),
    _Hh3cDot11RadioIfUpdownTimes_Type()
)
hh3cDot11RadioIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioIfUpdownTimes.setStatus("current")
_Hh3cDot11RadioIfLastChange_Type = TimeTicks
_Hh3cDot11RadioIfLastChange_Object = MibTableColumn
hh3cDot11RadioIfLastChange = _Hh3cDot11RadioIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 23),
    _Hh3cDot11RadioIfLastChange_Type()
)
hh3cDot11RadioIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioIfLastChange.setStatus("current")
_Hh3cDot11RadioModeSupport2_Type = Unsigned32
_Hh3cDot11RadioModeSupport2_Object = MibTableColumn
hh3cDot11RadioModeSupport2 = _Hh3cDot11RadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 24),
    _Hh3cDot11RadioModeSupport2_Type()
)
hh3cDot11RadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioModeSupport2.setStatus("current")


class _Hh3cDot11OperStatusCM_Type(Integer32):
    """Custom type hh3cDot11OperStatusCM based on Integer32"""
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


_Hh3cDot11OperStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11OperStatusCM_Object = MibTableColumn
hh3cDot11OperStatusCM = _Hh3cDot11OperStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 3, 1, 25),
    _Hh3cDot11OperStatusCM_Type()
)
hh3cDot11OperStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11OperStatusCM.setStatus("current")
_Hh3cDot11APBSSTable_Object = MibTable
hh3cDot11APBSSTable = _Hh3cDot11APBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11APBSSTable.setStatus("current")
_Hh3cDot11APBSSEntry_Object = MibTableRow
hh3cDot11APBSSEntry = _Hh3cDot11APBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1)
)
hh3cDot11APBSSEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APBSSEntry.setStatus("current")


class _Hh3cDot11WlanID_Type(Integer32):
    """Custom type hh3cDot11WlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11WlanID_Type.__name__ = "Integer32"
_Hh3cDot11WlanID_Object = MibTableColumn
hh3cDot11WlanID = _Hh3cDot11WlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 1),
    _Hh3cDot11WlanID_Type()
)
hh3cDot11WlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanID.setStatus("current")
_Hh3cDot11BSSID_Type = MacAddress
_Hh3cDot11BSSID_Object = MibTableColumn
hh3cDot11BSSID = _Hh3cDot11BSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 2),
    _Hh3cDot11BSSID_Type()
)
hh3cDot11BSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSID.setStatus("current")
_Hh3cDot11CurrSvcPolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11CurrSvcPolicyID_Object = MibTableColumn
hh3cDot11CurrSvcPolicyID = _Hh3cDot11CurrSvcPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 3),
    _Hh3cDot11CurrSvcPolicyID_Type()
)
hh3cDot11CurrSvcPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrSvcPolicyID.setStatus("current")
_Hh3cDot11SSID_Type = OctetString
_Hh3cDot11SSID_Object = MibTableColumn
hh3cDot11SSID = _Hh3cDot11SSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 4),
    _Hh3cDot11SSID_Type()
)
hh3cDot11SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SSID.setStatus("current")
_Hh3cDot11CurrSSIDResourceUseRatio_Type = Integer32
_Hh3cDot11CurrSSIDResourceUseRatio_Object = MibTableColumn
hh3cDot11CurrSSIDResourceUseRatio = _Hh3cDot11CurrSSIDResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 5),
    _Hh3cDot11CurrSSIDResourceUseRatio_Type()
)
hh3cDot11CurrSSIDResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrSSIDResourceUseRatio.setStatus("current")
_Hh3cDot11APEssVlanId_Type = Integer32
_Hh3cDot11APEssVlanId_Object = MibTableColumn
hh3cDot11APEssVlanId = _Hh3cDot11APEssVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 4, 1, 6),
    _Hh3cDot11APEssVlanId_Type()
)
hh3cDot11APEssVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APEssVlanId.setStatus("current")
_Hh3cDot11APModelTable_Object = MibTable
hh3cDot11APModelTable = _Hh3cDot11APModelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11APModelTable.setStatus("current")
_Hh3cDot11APModelEntry_Object = MibTableRow
hh3cDot11APModelEntry = _Hh3cDot11APModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1)
)
hh3cDot11APModelEntry.setIndexNames(
    (1, "HH3C-DOT11-APMT-MIB", "hh3cDot11APModelAlias"),
)
if mibBuilder.loadTexts:
    hh3cDot11APModelEntry.setStatus("current")


class _Hh3cDot11APModelAlias_Type(OctetString):
    """Custom type hh3cDot11APModelAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APModelAlias_Type.__name__ = "OctetString"
_Hh3cDot11APModelAlias_Object = MibTableColumn
hh3cDot11APModelAlias = _Hh3cDot11APModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 1),
    _Hh3cDot11APModelAlias_Type()
)
hh3cDot11APModelAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APModelAlias.setStatus("current")
_Hh3cDot11APModelName_Type = OctetString
_Hh3cDot11APModelName_Object = MibTableColumn
hh3cDot11APModelName = _Hh3cDot11APModelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 2),
    _Hh3cDot11APModelName_Type()
)
hh3cDot11APModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APModelName.setStatus("current")
_Hh3cDot11RadioNumSupport_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RadioNumSupport_Object = MibTableColumn
hh3cDot11RadioNumSupport = _Hh3cDot11RadioNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 3),
    _Hh3cDot11RadioNumSupport_Type()
)
hh3cDot11RadioNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioNumSupport.setStatus("current")
_Hh3cDot11StationNumSupport_Type = Integer32
_Hh3cDot11StationNumSupport_Object = MibTableColumn
hh3cDot11StationNumSupport = _Hh3cDot11StationNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 4),
    _Hh3cDot11StationNumSupport_Type()
)
hh3cDot11StationNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationNumSupport.setStatus("current")


class _Hh3cDot11MACModeSupport_Type(Hh3cDot11MACModeType):
    """Custom type hh3cDot11MACModeSupport based on Hh3cDot11MACModeType"""


_Hh3cDot11MACModeSupport_Object = MibTableColumn
hh3cDot11MACModeSupport = _Hh3cDot11MACModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 5),
    _Hh3cDot11MACModeSupport_Type()
)
hh3cDot11MACModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MACModeSupport.setStatus("current")
_Hh3cDot11APManufacturer_Type = OctetString
_Hh3cDot11APManufacturer_Object = MibTableColumn
hh3cDot11APManufacturer = _Hh3cDot11APManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 6),
    _Hh3cDot11APManufacturer_Type()
)
hh3cDot11APManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APManufacturer.setStatus("current")
_Hh3cDot11APCPUType_Type = OctetString
_Hh3cDot11APCPUType_Object = MibTableColumn
hh3cDot11APCPUType = _Hh3cDot11APCPUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 7),
    _Hh3cDot11APCPUType_Type()
)
hh3cDot11APCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPUType.setStatus("current")
_Hh3cDot11APCPUClockSpeed_Type = Unsigned32
_Hh3cDot11APCPUClockSpeed_Object = MibTableColumn
hh3cDot11APCPUClockSpeed = _Hh3cDot11APCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 8),
    _Hh3cDot11APCPUClockSpeed_Type()
)
hh3cDot11APCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPUClockSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCPUClockSpeed.setUnits("Hz")
_Hh3cDot11APMemoryType_Type = OctetString
_Hh3cDot11APMemoryType_Object = MibTableColumn
hh3cDot11APMemoryType = _Hh3cDot11APMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 9),
    _Hh3cDot11APMemoryType_Type()
)
hh3cDot11APMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemoryType.setStatus("current")
_Hh3cDot11APFlashType_Type = OctetString
_Hh3cDot11APFlashType_Object = MibTableColumn
hh3cDot11APFlashType = _Hh3cDot11APFlashType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 11),
    _Hh3cDot11APFlashType_Type()
)
hh3cDot11APFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APFlashType.setStatus("current")
_Hh3cDot11APFlashSize_Type = Unsigned32
_Hh3cDot11APFlashSize_Object = MibTableColumn
hh3cDot11APFlashSize = _Hh3cDot11APFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 12),
    _Hh3cDot11APFlashSize_Type()
)
hh3cDot11APFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APFlashSize.setUnits("kbytes")
_Hh3cDot11APMemSize_Type = Gauge32
_Hh3cDot11APMemSize_Object = MibTableColumn
hh3cDot11APMemSize = _Hh3cDot11APMemSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 13),
    _Hh3cDot11APMemSize_Type()
)
hh3cDot11APMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemSize.setUnits("bytes")
_Hh3cDot11APFlashSizeInBytes_Type = Unsigned32
_Hh3cDot11APFlashSizeInBytes_Object = MibTableColumn
hh3cDot11APFlashSizeInBytes = _Hh3cDot11APFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 14),
    _Hh3cDot11APFlashSizeInBytes_Type()
)
hh3cDot11APFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APFlashSizeInBytes.setUnits("bytes")
_Hh3cDot11APMemorySize_Type = Unsigned32
_Hh3cDot11APMemorySize_Object = MibTableColumn
hh3cDot11APMemorySize = _Hh3cDot11APMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 5, 1, 20),
    _Hh3cDot11APMemorySize_Type()
)
hh3cDot11APMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemorySize.setUnits("kbytes")
_Hh3cDot11APIfTable_Object = MibTable
hh3cDot11APIfTable = _Hh3cDot11APIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11APIfTable.setStatus("current")
_Hh3cDot11APIfEntry_Object = MibTableRow
hh3cDot11APIfEntry = _Hh3cDot11APIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1)
)
hh3cDot11APIfEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APObjID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIfEntry.setStatus("current")
_Hh3cDot11APIfIndex_Type = Integer32
_Hh3cDot11APIfIndex_Object = MibTableColumn
hh3cDot11APIfIndex = _Hh3cDot11APIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 1),
    _Hh3cDot11APIfIndex_Type()
)
hh3cDot11APIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APIfIndex.setStatus("current")
_Hh3cDot11APIfDescr_Type = OctetString
_Hh3cDot11APIfDescr_Object = MibTableColumn
hh3cDot11APIfDescr = _Hh3cDot11APIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 2),
    _Hh3cDot11APIfDescr_Type()
)
hh3cDot11APIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfDescr.setStatus("current")
_Hh3cDot11APIfType_Type = Integer32
_Hh3cDot11APIfType_Object = MibTableColumn
hh3cDot11APIfType = _Hh3cDot11APIfType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 3),
    _Hh3cDot11APIfType_Type()
)
hh3cDot11APIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfType.setStatus("current")
_Hh3cDot11APIfMtu_Type = Integer32
_Hh3cDot11APIfMtu_Object = MibTableColumn
hh3cDot11APIfMtu = _Hh3cDot11APIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 4),
    _Hh3cDot11APIfMtu_Type()
)
hh3cDot11APIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APIfMtu.setStatus("current")
_Hh3cDot11APIfPHYAddress_Type = OctetString
_Hh3cDot11APIfPHYAddress_Object = MibTableColumn
hh3cDot11APIfPHYAddress = _Hh3cDot11APIfPHYAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 5),
    _Hh3cDot11APIfPHYAddress_Type()
)
hh3cDot11APIfPHYAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfPHYAddress.setStatus("current")
_Hh3cDot11APIfSpeed_Type = Integer32
_Hh3cDot11APIfSpeed_Object = MibTableColumn
hh3cDot11APIfSpeed = _Hh3cDot11APIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 6),
    _Hh3cDot11APIfSpeed_Type()
)
hh3cDot11APIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APIfSpeed.setUnits("Mbps")
_Hh3cDot11APIfInDataRate_Type = Integer32
_Hh3cDot11APIfInDataRate_Object = MibTableColumn
hh3cDot11APIfInDataRate = _Hh3cDot11APIfInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 7),
    _Hh3cDot11APIfInDataRate_Type()
)
hh3cDot11APIfInDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APIfInDataRate.setUnits("Kbps")
_Hh3cDot11APIfOutDataRate_Type = Integer32
_Hh3cDot11APIfOutDataRate_Object = MibTableColumn
hh3cDot11APIfOutDataRate = _Hh3cDot11APIfOutDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 8),
    _Hh3cDot11APIfOutDataRate_Type()
)
hh3cDot11APIfOutDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutDataRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutDataRate.setUnits("Kbps")
_Hh3cDot11APIfSpeedKbps_Type = Gauge32
_Hh3cDot11APIfSpeedKbps_Object = MibTableColumn
hh3cDot11APIfSpeedKbps = _Hh3cDot11APIfSpeedKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 9),
    _Hh3cDot11APIfSpeedKbps_Type()
)
hh3cDot11APIfSpeedKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfSpeedKbps.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APIfSpeedKbps.setUnits("kbps")
_Hh3cDot11APIfTypeCM_Type = Integer32
_Hh3cDot11APIfTypeCM_Object = MibTableColumn
hh3cDot11APIfTypeCM = _Hh3cDot11APIfTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 6, 1, 10),
    _Hh3cDot11APIfTypeCM_Type()
)
hh3cDot11APIfTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfTypeCM.setStatus("current")
_Hh3cDot11APSSIDObjectTable_Object = MibTable
hh3cDot11APSSIDObjectTable = _Hh3cDot11APSSIDObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11APSSIDObjectTable.setStatus("current")
_Hh3cDot11APSSIDObjectEntry_Object = MibTableRow
hh3cDot11APSSIDObjectEntry = _Hh3cDot11APSSIDObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7, 1)
)
hh3cDot11APSSIDObjectEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APConfigSPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSSIDObjectEntry.setStatus("current")
_Hh3cDot11APConfigSPID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11APConfigSPID_Object = MibTableColumn
hh3cDot11APConfigSPID = _Hh3cDot11APConfigSPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7, 1, 1),
    _Hh3cDot11APConfigSPID_Type()
)
hh3cDot11APConfigSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APConfigSPID.setStatus("current")
_Hh3cDot11APConfigSSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11APConfigSSIDName_Object = MibTableColumn
hh3cDot11APConfigSSIDName = _Hh3cDot11APConfigSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7, 1, 2),
    _Hh3cDot11APConfigSSIDName_Type()
)
hh3cDot11APConfigSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConfigSSIDName.setStatus("current")
_Hh3cDot11APConfigBSSIDNum_Type = Integer32
_Hh3cDot11APConfigBSSIDNum_Object = MibTableColumn
hh3cDot11APConfigBSSIDNum = _Hh3cDot11APConfigBSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7, 1, 3),
    _Hh3cDot11APConfigBSSIDNum_Type()
)
hh3cDot11APConfigBSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConfigBSSIDNum.setStatus("current")
_Hh3cDot11APConfigPortalStaNum_Type = Integer32
_Hh3cDot11APConfigPortalStaNum_Object = MibTableColumn
hh3cDot11APConfigPortalStaNum = _Hh3cDot11APConfigPortalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 7, 1, 4),
    _Hh3cDot11APConfigPortalStaNum_Type()
)
hh3cDot11APConfigPortalStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConfigPortalStaNum.setStatus("current")
_Hh3cDot11APSysInfoTable_Object = MibTable
hh3cDot11APSysInfoTable = _Hh3cDot11APSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoTable.setStatus("current")
_Hh3cDot11APSysInfoEntry_Object = MibTableRow
hh3cDot11APSysInfoEntry = _Hh3cDot11APSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1)
)
hh3cDot11APSysInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoEntry.setStatus("current")
_Hh3cDot11APSysUpTime_Type = TimeTicks
_Hh3cDot11APSysUpTime_Object = MibTableColumn
hh3cDot11APSysUpTime = _Hh3cDot11APSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 1),
    _Hh3cDot11APSysUpTime_Type()
)
hh3cDot11APSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APSysUpTime.setStatus("current")


class _Hh3cDot11APCPURTUsage_Type(Integer32):
    """Custom type hh3cDot11APCPURTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCPURTUsage_Type.__name__ = "Integer32"
_Hh3cDot11APCPURTUsage_Object = MibTableColumn
hh3cDot11APCPURTUsage = _Hh3cDot11APCPURTUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 2),
    _Hh3cDot11APCPURTUsage_Type()
)
hh3cDot11APCPURTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPURTUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCPURTUsage.setUnits("onepercent")


class _Hh3cDot11APCPUAvgUsage_Type(Integer32):
    """Custom type hh3cDot11APCPUAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCPUAvgUsage_Type.__name__ = "Integer32"
_Hh3cDot11APCPUAvgUsage_Object = MibTableColumn
hh3cDot11APCPUAvgUsage = _Hh3cDot11APCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 3),
    _Hh3cDot11APCPUAvgUsage_Type()
)
hh3cDot11APCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPUAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCPUAvgUsage.setUnits("onepercent")


class _Hh3cDot11APMemRTUsage_Type(Integer32):
    """Custom type hh3cDot11APMemRTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemRTUsage_Type.__name__ = "Integer32"
_Hh3cDot11APMemRTUsage_Object = MibTableColumn
hh3cDot11APMemRTUsage = _Hh3cDot11APMemRTUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 4),
    _Hh3cDot11APMemRTUsage_Type()
)
hh3cDot11APMemRTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemRTUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemRTUsage.setUnits("onepercent")


class _Hh3cDot11APMemAvgUsage_Type(Integer32):
    """Custom type hh3cDot11APMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemAvgUsage_Type.__name__ = "Integer32"
_Hh3cDot11APMemAvgUsage_Object = MibTableColumn
hh3cDot11APMemAvgUsage = _Hh3cDot11APMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 5),
    _Hh3cDot11APMemAvgUsage_Type()
)
hh3cDot11APMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemAvgUsage.setUnits("onepercent")
_Hh3cDot11APIPAddressGateway_Type = IpAddress
_Hh3cDot11APIPAddressGateway_Object = MibTableColumn
hh3cDot11APIPAddressGateway = _Hh3cDot11APIPAddressGateway_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 6),
    _Hh3cDot11APIPAddressGateway_Type()
)
hh3cDot11APIPAddressGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIPAddressGateway.setStatus("current")


class _Hh3cDot11APACAssociateStatus_Type(Integer32):
    """Custom type hh3cDot11APACAssociateStatus based on Integer32"""
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


_Hh3cDot11APACAssociateStatus_Type.__name__ = "Integer32"
_Hh3cDot11APACAssociateStatus_Object = MibTableColumn
hh3cDot11APACAssociateStatus = _Hh3cDot11APACAssociateStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 7),
    _Hh3cDot11APACAssociateStatus_Type()
)
hh3cDot11APACAssociateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APACAssociateStatus.setStatus("current")


class _Hh3cDot11APManuBuildInfo_Type(OctetString):
    """Custom type hh3cDot11APManuBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11APManuBuildInfo_Type.__name__ = "OctetString"
_Hh3cDot11APManuBuildInfo_Object = MibTableColumn
hh3cDot11APManuBuildInfo = _Hh3cDot11APManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 8),
    _Hh3cDot11APManuBuildInfo_Type()
)
hh3cDot11APManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APManuBuildInfo.setStatus("current")
_Hh3cDot11APFlashFreeSize_Type = Unsigned32
_Hh3cDot11APFlashFreeSize_Object = MibTableColumn
hh3cDot11APFlashFreeSize = _Hh3cDot11APFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 9),
    _Hh3cDot11APFlashFreeSize_Type()
)
hh3cDot11APFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APFlashFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APFlashFreeSize.setUnits("bytes")
_Hh3cDot11APTemperature_Type = Integer32
_Hh3cDot11APTemperature_Object = MibTableColumn
hh3cDot11APTemperature = _Hh3cDot11APTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 8, 1, 10),
    _Hh3cDot11APTemperature_Type()
)
hh3cDot11APTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTemperature.setStatus("current")
_Hh3cDot11APIdleListTable_Object = MibTable
hh3cDot11APIdleListTable = _Hh3cDot11APIdleListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11APIdleListTable.setStatus("current")
_Hh3cDot11APIdleListEntry_Object = MibTableRow
hh3cDot11APIdleListEntry = _Hh3cDot11APIdleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 9, 1)
)
hh3cDot11APIdleListEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APIdleTemplateName"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIdleListEntry.setStatus("current")


class _Hh3cDot11APIdleTemplateName_Type(OctetString):
    """Custom type hh3cDot11APIdleTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APIdleTemplateName_Type.__name__ = "OctetString"
_Hh3cDot11APIdleTemplateName_Object = MibTableColumn
hh3cDot11APIdleTemplateName = _Hh3cDot11APIdleTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 9, 1, 1),
    _Hh3cDot11APIdleTemplateName_Type()
)
hh3cDot11APIdleTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APIdleTemplateName.setStatus("current")
_Hh3cDot11APIdleSerialID_Type = OctetString
_Hh3cDot11APIdleSerialID_Object = MibTableColumn
hh3cDot11APIdleSerialID = _Hh3cDot11APIdleSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 9, 1, 2),
    _Hh3cDot11APIdleSerialID_Type()
)
hh3cDot11APIdleSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIdleSerialID.setStatus("current")
_Hh3cDot11APSysInfoByAPIDTable_Object = MibTable
hh3cDot11APSysInfoByAPIDTable = _Hh3cDot11APSysInfoByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoByAPIDTable.setStatus("current")
_Hh3cDot11APSysInfoByAPIDEntry_Object = MibTableRow
hh3cDot11APSysInfoByAPIDEntry = _Hh3cDot11APSysInfoByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1)
)
hh3cDot11APSysInfoByAPIDEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APObjID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoByAPIDEntry.setStatus("current")
_Hh3cDot11APSysUpTime2_Type = TimeTicks
_Hh3cDot11APSysUpTime2_Object = MibTableColumn
hh3cDot11APSysUpTime2 = _Hh3cDot11APSysUpTime2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 1),
    _Hh3cDot11APSysUpTime2_Type()
)
hh3cDot11APSysUpTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APSysUpTime2.setStatus("current")


class _Hh3cDot11APCPURTUsage2_Type(Integer32):
    """Custom type hh3cDot11APCPURTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCPURTUsage2_Type.__name__ = "Integer32"
_Hh3cDot11APCPURTUsage2_Object = MibTableColumn
hh3cDot11APCPURTUsage2 = _Hh3cDot11APCPURTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 2),
    _Hh3cDot11APCPURTUsage2_Type()
)
hh3cDot11APCPURTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPURTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCPURTUsage2.setUnits("onepercent")


class _Hh3cDot11APCPUAvgUsage2_Type(Integer32):
    """Custom type hh3cDot11APCPUAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCPUAvgUsage2_Type.__name__ = "Integer32"
_Hh3cDot11APCPUAvgUsage2_Object = MibTableColumn
hh3cDot11APCPUAvgUsage2 = _Hh3cDot11APCPUAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 3),
    _Hh3cDot11APCPUAvgUsage2_Type()
)
hh3cDot11APCPUAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APCPUAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCPUAvgUsage2.setUnits("onepercent")


class _Hh3cDot11APMemRTUsage2_Type(Integer32):
    """Custom type hh3cDot11APMemRTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemRTUsage2_Type.__name__ = "Integer32"
_Hh3cDot11APMemRTUsage2_Object = MibTableColumn
hh3cDot11APMemRTUsage2 = _Hh3cDot11APMemRTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 4),
    _Hh3cDot11APMemRTUsage2_Type()
)
hh3cDot11APMemRTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemRTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemRTUsage2.setUnits("onepercent")


class _Hh3cDot11APMemAvgUsage2_Type(Integer32):
    """Custom type hh3cDot11APMemAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemAvgUsage2_Type.__name__ = "Integer32"
_Hh3cDot11APMemAvgUsage2_Object = MibTableColumn
hh3cDot11APMemAvgUsage2 = _Hh3cDot11APMemAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 5),
    _Hh3cDot11APMemAvgUsage2_Type()
)
hh3cDot11APMemAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMemAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemAvgUsage2.setUnits("onepercent")
_Hh3cDot11APIPAddressGateway2_Type = IpAddress
_Hh3cDot11APIPAddressGateway2_Object = MibTableColumn
hh3cDot11APIPAddressGateway2 = _Hh3cDot11APIPAddressGateway2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 6),
    _Hh3cDot11APIPAddressGateway2_Type()
)
hh3cDot11APIPAddressGateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIPAddressGateway2.setStatus("current")


class _Hh3cDot11APACAssociateStatus2_Type(Integer32):
    """Custom type hh3cDot11APACAssociateStatus2 based on Integer32"""
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


_Hh3cDot11APACAssociateStatus2_Type.__name__ = "Integer32"
_Hh3cDot11APACAssociateStatus2_Object = MibTableColumn
hh3cDot11APACAssociateStatus2 = _Hh3cDot11APACAssociateStatus2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 7),
    _Hh3cDot11APACAssociateStatus2_Type()
)
hh3cDot11APACAssociateStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APACAssociateStatus2.setStatus("current")


class _Hh3cDot11APManuBuildInfo2_Type(OctetString):
    """Custom type hh3cDot11APManuBuildInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11APManuBuildInfo2_Type.__name__ = "OctetString"
_Hh3cDot11APManuBuildInfo2_Object = MibTableColumn
hh3cDot11APManuBuildInfo2 = _Hh3cDot11APManuBuildInfo2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 8),
    _Hh3cDot11APManuBuildInfo2_Type()
)
hh3cDot11APManuBuildInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APManuBuildInfo2.setStatus("current")
_Hh3cDot11APFlashFreeSize2_Type = Unsigned32
_Hh3cDot11APFlashFreeSize2_Object = MibTableColumn
hh3cDot11APFlashFreeSize2 = _Hh3cDot11APFlashFreeSize2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 9),
    _Hh3cDot11APFlashFreeSize2_Type()
)
hh3cDot11APFlashFreeSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APFlashFreeSize2.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APFlashFreeSize2.setUnits("bytes")
_Hh3cDot11APTemperature2_Type = Integer32
_Hh3cDot11APTemperature2_Object = MibTableColumn
hh3cDot11APTemperature2 = _Hh3cDot11APTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 10),
    _Hh3cDot11APTemperature2_Type()
)
hh3cDot11APTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTemperature2.setStatus("current")
_Hh3cDot11APMacAddress2_Type = MacAddress
_Hh3cDot11APMacAddress2_Object = MibTableColumn
hh3cDot11APMacAddress2 = _Hh3cDot11APMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 11),
    _Hh3cDot11APMacAddress2_Type()
)
hh3cDot11APMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAddress2.setStatus("current")


class _Hh3cDot11APACAssociateStatusCM_Type(Integer32):
    """Custom type hh3cDot11APACAssociateStatusCM based on Integer32"""
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


_Hh3cDot11APACAssociateStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11APACAssociateStatusCM_Object = MibTableColumn
hh3cDot11APACAssociateStatusCM = _Hh3cDot11APACAssociateStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 1, 10, 1, 12),
    _Hh3cDot11APACAssociateStatusCM_Type()
)
hh3cDot11APACAssociateStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APACAssociateStatusCM.setStatus("current")
_Hh3cDot11APStatisGroup_ObjectIdentity = ObjectIdentity
hh3cDot11APStatisGroup = _Hh3cDot11APStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2)
)
_Hh3cDot11APRxStatisTable_Object = MibTable
hh3cDot11APRxStatisTable = _Hh3cDot11APRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APRxStatisTable.setStatus("current")
_Hh3cDot11APRxStatisEntry_Object = MibTableRow
hh3cDot11APRxStatisEntry = _Hh3cDot11APRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1)
)
hh3cDot11APRxStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APRxStatisEntry.setStatus("current")
_Hh3cDot11RxFrameDupCnt_Type = Counter32
_Hh3cDot11RxFrameDupCnt_Object = MibTableColumn
hh3cDot11RxFrameDupCnt = _Hh3cDot11RxFrameDupCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 1),
    _Hh3cDot11RxFrameDupCnt_Type()
)
hh3cDot11RxFrameDupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFrameDupCnt.setStatus("current")
_Hh3cDot11RxFrameCnt_Type = Counter32
_Hh3cDot11RxFrameCnt_Object = MibTableColumn
hh3cDot11RxFrameCnt = _Hh3cDot11RxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 2),
    _Hh3cDot11RxFrameCnt_Type()
)
hh3cDot11RxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFrameCnt.setStatus("current")
_Hh3cDot11RxUcastFrameCnt_Type = Counter32
_Hh3cDot11RxUcastFrameCnt_Object = MibTableColumn
hh3cDot11RxUcastFrameCnt = _Hh3cDot11RxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 3),
    _Hh3cDot11RxUcastFrameCnt_Type()
)
hh3cDot11RxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxUcastFrameCnt.setStatus("current")
_Hh3cDot11RxBcastFrameCnt_Type = Counter32
_Hh3cDot11RxBcastFrameCnt_Object = MibTableColumn
hh3cDot11RxBcastFrameCnt = _Hh3cDot11RxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 4),
    _Hh3cDot11RxBcastFrameCnt_Type()
)
hh3cDot11RxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxBcastFrameCnt.setStatus("current")
_Hh3cDot11RxMcastFrameCnt_Type = Counter32
_Hh3cDot11RxMcastFrameCnt_Object = MibTableColumn
hh3cDot11RxMcastFrameCnt = _Hh3cDot11RxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 5),
    _Hh3cDot11RxMcastFrameCnt_Type()
)
hh3cDot11RxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxMcastFrameCnt.setStatus("current")
_Hh3cDot11RxDiscardFrameCnt_Type = Counter32
_Hh3cDot11RxDiscardFrameCnt_Object = MibTableColumn
hh3cDot11RxDiscardFrameCnt = _Hh3cDot11RxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 6),
    _Hh3cDot11RxDiscardFrameCnt_Type()
)
hh3cDot11RxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDiscardFrameCnt.setStatus("current")
_Hh3cDot11RxFragCnt_Type = Counter32
_Hh3cDot11RxFragCnt_Object = MibTableColumn
hh3cDot11RxFragCnt = _Hh3cDot11RxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 7),
    _Hh3cDot11RxFragCnt_Type()
)
hh3cDot11RxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFragCnt.setStatus("current")
_Hh3cDot11RxFcsErrCnt_Type = Counter32
_Hh3cDot11RxFcsErrCnt_Object = MibTableColumn
hh3cDot11RxFcsErrCnt = _Hh3cDot11RxFcsErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 8),
    _Hh3cDot11RxFcsErrCnt_Type()
)
hh3cDot11RxFcsErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFcsErrCnt.setStatus("current")
_Hh3cDot11RxFrameBytes_Type = Counter32
_Hh3cDot11RxFrameBytes_Object = MibTableColumn
hh3cDot11RxFrameBytes = _Hh3cDot11RxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 9),
    _Hh3cDot11RxFrameBytes_Type()
)
hh3cDot11RxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFrameBytes.setStatus("current")
_Hh3cDot11RxUcastFrameBytes_Type = Counter32
_Hh3cDot11RxUcastFrameBytes_Object = MibTableColumn
hh3cDot11RxUcastFrameBytes = _Hh3cDot11RxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 10),
    _Hh3cDot11RxUcastFrameBytes_Type()
)
hh3cDot11RxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxUcastFrameBytes.setStatus("current")
_Hh3cDot11RxBcastFrameBytes_Type = Counter32
_Hh3cDot11RxBcastFrameBytes_Object = MibTableColumn
hh3cDot11RxBcastFrameBytes = _Hh3cDot11RxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 11),
    _Hh3cDot11RxBcastFrameBytes_Type()
)
hh3cDot11RxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxBcastFrameBytes.setStatus("current")
_Hh3cDot11RxMcastFrameBytes_Type = Counter32
_Hh3cDot11RxMcastFrameBytes_Object = MibTableColumn
hh3cDot11RxMcastFrameBytes = _Hh3cDot11RxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 12),
    _Hh3cDot11RxMcastFrameBytes_Type()
)
hh3cDot11RxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxMcastFrameBytes.setStatus("current")
_Hh3cDot11RxDiscardFrameBytes_Type = Counter32
_Hh3cDot11RxDiscardFrameBytes_Object = MibTableColumn
hh3cDot11RxDiscardFrameBytes = _Hh3cDot11RxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 13),
    _Hh3cDot11RxDiscardFrameBytes_Type()
)
hh3cDot11RxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDiscardFrameBytes.setStatus("current")
_Hh3cDot11RxMgmtFrameCnt_Type = Counter32
_Hh3cDot11RxMgmtFrameCnt_Object = MibTableColumn
hh3cDot11RxMgmtFrameCnt = _Hh3cDot11RxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 14),
    _Hh3cDot11RxMgmtFrameCnt_Type()
)
hh3cDot11RxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxMgmtFrameCnt.setStatus("current")
_Hh3cDot11RxCtrlFrameCnt_Type = Counter32
_Hh3cDot11RxCtrlFrameCnt_Object = MibTableColumn
hh3cDot11RxCtrlFrameCnt = _Hh3cDot11RxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 15),
    _Hh3cDot11RxCtrlFrameCnt_Type()
)
hh3cDot11RxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxCtrlFrameCnt.setStatus("current")
_Hh3cDot11RxDataFrameCnt_Type = Counter32
_Hh3cDot11RxDataFrameCnt_Object = MibTableColumn
hh3cDot11RxDataFrameCnt = _Hh3cDot11RxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 16),
    _Hh3cDot11RxDataFrameCnt_Type()
)
hh3cDot11RxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDataFrameCnt.setStatus("current")
_Hh3cDot11RxDecryptErrorCnt_Type = Counter32
_Hh3cDot11RxDecryptErrorCnt_Object = MibTableColumn
hh3cDot11RxDecryptErrorCnt = _Hh3cDot11RxDecryptErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 17),
    _Hh3cDot11RxDecryptErrorCnt_Type()
)
hh3cDot11RxDecryptErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDecryptErrorCnt.setStatus("current")
_Hh3cDot11RxAuthenFrameCnt_Type = Counter32
_Hh3cDot11RxAuthenFrameCnt_Object = MibTableColumn
hh3cDot11RxAuthenFrameCnt = _Hh3cDot11RxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 18),
    _Hh3cDot11RxAuthenFrameCnt_Type()
)
hh3cDot11RxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxAuthenFrameCnt.setStatus("current")
_Hh3cDot11RxAssociateFrameCnt_Type = Counter32
_Hh3cDot11RxAssociateFrameCnt_Object = MibTableColumn
hh3cDot11RxAssociateFrameCnt = _Hh3cDot11RxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 19),
    _Hh3cDot11RxAssociateFrameCnt_Type()
)
hh3cDot11RxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxAssociateFrameCnt.setStatus("current")
_Hh3cDot11RxFrameErrorRatio_Type = Integer32
_Hh3cDot11RxFrameErrorRatio_Object = MibTableColumn
hh3cDot11RxFrameErrorRatio = _Hh3cDot11RxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 20),
    _Hh3cDot11RxFrameErrorRatio_Type()
)
hh3cDot11RxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RxFrameErrorRatio.setUnits("onepercent")
_Hh3cDot11RxPhyErrorCnt_Type = Counter32
_Hh3cDot11RxPhyErrorCnt_Object = MibTableColumn
hh3cDot11RxPhyErrorCnt = _Hh3cDot11RxPhyErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 21),
    _Hh3cDot11RxPhyErrorCnt_Type()
)
hh3cDot11RxPhyErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxPhyErrorCnt.setStatus("current")
_Hh3cDot11RxMICErrorCnt_Type = Counter32
_Hh3cDot11RxMICErrorCnt_Object = MibTableColumn
hh3cDot11RxMICErrorCnt = _Hh3cDot11RxMICErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 22),
    _Hh3cDot11RxMICErrorCnt_Type()
)
hh3cDot11RxMICErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxMICErrorCnt.setStatus("current")
_Hh3cDot11RxDataFrameBytes_Type = Counter32
_Hh3cDot11RxDataFrameBytes_Object = MibTableColumn
hh3cDot11RxDataFrameBytes = _Hh3cDot11RxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 23),
    _Hh3cDot11RxDataFrameBytes_Type()
)
hh3cDot11RxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDataFrameBytes.setStatus("current")
_Hh3cDot11RadioRxAverSnr_Type = Integer32
_Hh3cDot11RadioRxAverSnr_Object = MibTableColumn
hh3cDot11RadioRxAverSnr = _Hh3cDot11RadioRxAverSnr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 24),
    _Hh3cDot11RadioRxAverSnr_Type()
)
hh3cDot11RadioRxAverSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioRxAverSnr.setStatus("current")
_Hh3cDot11RxPayloadBytes_Type = Counter32
_Hh3cDot11RxPayloadBytes_Object = MibTableColumn
hh3cDot11RxPayloadBytes = _Hh3cDot11RxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 25),
    _Hh3cDot11RxPayloadBytes_Type()
)
hh3cDot11RxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxPayloadBytes.setStatus("current")
_Hh3cDot11RxTrafficSpeed_Type = Integer32
_Hh3cDot11RxTrafficSpeed_Object = MibTableColumn
hh3cDot11RxTrafficSpeed = _Hh3cDot11RxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 26),
    _Hh3cDot11RxTrafficSpeed_Type()
)
hh3cDot11RxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RxTrafficSpeed.setUnits("byte/s")
_Hh3cDot11RxUcastDataFrameCnt_Type = Counter64
_Hh3cDot11RxUcastDataFrameCnt_Object = MibTableColumn
hh3cDot11RxUcastDataFrameCnt = _Hh3cDot11RxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 27),
    _Hh3cDot11RxUcastDataFrameCnt_Type()
)
hh3cDot11RxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxUcastDataFrameCnt.setStatus("current")
_Hh3cDot11RxNUcastDataFrameCnt_Type = Counter64
_Hh3cDot11RxNUcastDataFrameCnt_Object = MibTableColumn
hh3cDot11RxNUcastDataFrameCnt = _Hh3cDot11RxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 28),
    _Hh3cDot11RxNUcastDataFrameCnt_Type()
)
hh3cDot11RxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxNUcastDataFrameCnt.setStatus("current")
_Hh3cDot11RxTotalDiscardFrameCnt_Type = Counter64
_Hh3cDot11RxTotalDiscardFrameCnt_Object = MibTableColumn
hh3cDot11RxTotalDiscardFrameCnt = _Hh3cDot11RxTotalDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 29),
    _Hh3cDot11RxTotalDiscardFrameCnt_Type()
)
hh3cDot11RxTotalDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxTotalDiscardFrameCnt.setStatus("current")
_Hh3cDot11RxTotalIPCheckErrPacketCnt_Type = Counter64
_Hh3cDot11RxTotalIPCheckErrPacketCnt_Object = MibTableColumn
hh3cDot11RxTotalIPCheckErrPacketCnt = _Hh3cDot11RxTotalIPCheckErrPacketCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 30),
    _Hh3cDot11RxTotalIPCheckErrPacketCnt_Type()
)
hh3cDot11RxTotalIPCheckErrPacketCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxTotalIPCheckErrPacketCnt.setStatus("current")
_Hh3cDot11RxSignalStrengthPacketCntCM_Type = OctetString
_Hh3cDot11RxSignalStrengthPacketCntCM_Object = MibTableColumn
hh3cDot11RxSignalStrengthPacketCntCM = _Hh3cDot11RxSignalStrengthPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 31),
    _Hh3cDot11RxSignalStrengthPacketCntCM_Type()
)
hh3cDot11RxSignalStrengthPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxSignalStrengthPacketCntCM.setStatus("current")
_Hh3cDot11RxDataFrameCntCM_Type = Counter32
_Hh3cDot11RxDataFrameCntCM_Object = MibTableColumn
hh3cDot11RxDataFrameCntCM = _Hh3cDot11RxDataFrameCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 32),
    _Hh3cDot11RxDataFrameCntCM_Type()
)
hh3cDot11RxDataFrameCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxDataFrameCntCM.setStatus("current")
_Hh3cDot11RxTotalFrameCnt_Type = Counter64
_Hh3cDot11RxTotalFrameCnt_Object = MibTableColumn
hh3cDot11RxTotalFrameCnt = _Hh3cDot11RxTotalFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 1, 1, 33),
    _Hh3cDot11RxTotalFrameCnt_Type()
)
hh3cDot11RxTotalFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RxTotalFrameCnt.setStatus("current")
_Hh3cDot11APTxStatisTable_Object = MibTable
hh3cDot11APTxStatisTable = _Hh3cDot11APTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11APTxStatisTable.setStatus("current")
_Hh3cDot11APTxStatisEntry_Object = MibTableRow
hh3cDot11APTxStatisEntry = _Hh3cDot11APTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1)
)
hh3cDot11APTxStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APTxStatisEntry.setStatus("current")
_Hh3cDot11TxFragCnt_Type = Counter32
_Hh3cDot11TxFragCnt_Object = MibTableColumn
hh3cDot11TxFragCnt = _Hh3cDot11TxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 1),
    _Hh3cDot11TxFragCnt_Type()
)
hh3cDot11TxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxFragCnt.setStatus("current")
_Hh3cDot11FailedCnt_Type = Counter32
_Hh3cDot11FailedCnt_Object = MibTableColumn
hh3cDot11FailedCnt = _Hh3cDot11FailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 2),
    _Hh3cDot11FailedCnt_Type()
)
hh3cDot11FailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11FailedCnt.setStatus("current")
_Hh3cDot11RetryCnt_Type = Counter32
_Hh3cDot11RetryCnt_Object = MibTableColumn
hh3cDot11RetryCnt = _Hh3cDot11RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 3),
    _Hh3cDot11RetryCnt_Type()
)
hh3cDot11RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RetryCnt.setStatus("current")
_Hh3cDot11MultiRetryCnt_Type = Counter32
_Hh3cDot11MultiRetryCnt_Object = MibTableColumn
hh3cDot11MultiRetryCnt = _Hh3cDot11MultiRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 4),
    _Hh3cDot11MultiRetryCnt_Type()
)
hh3cDot11MultiRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MultiRetryCnt.setStatus("current")
_Hh3cDot11RtsSuccessCnt_Type = Counter32
_Hh3cDot11RtsSuccessCnt_Object = MibTableColumn
hh3cDot11RtsSuccessCnt = _Hh3cDot11RtsSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 5),
    _Hh3cDot11RtsSuccessCnt_Type()
)
hh3cDot11RtsSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RtsSuccessCnt.setStatus("current")
_Hh3cDot11RtsFailCnt_Type = Counter32
_Hh3cDot11RtsFailCnt_Object = MibTableColumn
hh3cDot11RtsFailCnt = _Hh3cDot11RtsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 6),
    _Hh3cDot11RtsFailCnt_Type()
)
hh3cDot11RtsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RtsFailCnt.setStatus("current")
_Hh3cDot11AckFailCnt_Type = Counter32
_Hh3cDot11AckFailCnt_Object = MibTableColumn
hh3cDot11AckFailCnt = _Hh3cDot11AckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 7),
    _Hh3cDot11AckFailCnt_Type()
)
hh3cDot11AckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AckFailCnt.setStatus("current")
_Hh3cDot11TxFrameCnt_Type = Counter32
_Hh3cDot11TxFrameCnt_Object = MibTableColumn
hh3cDot11TxFrameCnt = _Hh3cDot11TxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 8),
    _Hh3cDot11TxFrameCnt_Type()
)
hh3cDot11TxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxFrameCnt.setStatus("current")
_Hh3cDot11TxUcastFrameCnt_Type = Counter32
_Hh3cDot11TxUcastFrameCnt_Object = MibTableColumn
hh3cDot11TxUcastFrameCnt = _Hh3cDot11TxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 9),
    _Hh3cDot11TxUcastFrameCnt_Type()
)
hh3cDot11TxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxUcastFrameCnt.setStatus("current")
_Hh3cDot11TxBcastFrameCnt_Type = Counter32
_Hh3cDot11TxBcastFrameCnt_Object = MibTableColumn
hh3cDot11TxBcastFrameCnt = _Hh3cDot11TxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 10),
    _Hh3cDot11TxBcastFrameCnt_Type()
)
hh3cDot11TxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxBcastFrameCnt.setStatus("current")
_Hh3cDot11TxMcastFrameCnt_Type = Counter32
_Hh3cDot11TxMcastFrameCnt_Object = MibTableColumn
hh3cDot11TxMcastFrameCnt = _Hh3cDot11TxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 11),
    _Hh3cDot11TxMcastFrameCnt_Type()
)
hh3cDot11TxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxMcastFrameCnt.setStatus("current")
_Hh3cDot11TxDiscardFrameCnt_Type = Counter32
_Hh3cDot11TxDiscardFrameCnt_Object = MibTableColumn
hh3cDot11TxDiscardFrameCnt = _Hh3cDot11TxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 12),
    _Hh3cDot11TxDiscardFrameCnt_Type()
)
hh3cDot11TxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxDiscardFrameCnt.setStatus("current")
_Hh3cDot11TxFrameBytes_Type = Counter32
_Hh3cDot11TxFrameBytes_Object = MibTableColumn
hh3cDot11TxFrameBytes = _Hh3cDot11TxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 13),
    _Hh3cDot11TxFrameBytes_Type()
)
hh3cDot11TxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxFrameBytes.setStatus("current")
_Hh3cDot11TxUcastFrameBytes_Type = Counter32
_Hh3cDot11TxUcastFrameBytes_Object = MibTableColumn
hh3cDot11TxUcastFrameBytes = _Hh3cDot11TxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 14),
    _Hh3cDot11TxUcastFrameBytes_Type()
)
hh3cDot11TxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxUcastFrameBytes.setStatus("current")
_Hh3cDot11TxBcastFrameBytes_Type = Counter32
_Hh3cDot11TxBcastFrameBytes_Object = MibTableColumn
hh3cDot11TxBcastFrameBytes = _Hh3cDot11TxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 15),
    _Hh3cDot11TxBcastFrameBytes_Type()
)
hh3cDot11TxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxBcastFrameBytes.setStatus("current")
_Hh3cDot11TxMcastFrameBytes_Type = Counter32
_Hh3cDot11TxMcastFrameBytes_Object = MibTableColumn
hh3cDot11TxMcastFrameBytes = _Hh3cDot11TxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 16),
    _Hh3cDot11TxMcastFrameBytes_Type()
)
hh3cDot11TxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxMcastFrameBytes.setStatus("current")
_Hh3cDot11TxDiscardFrameBytes_Type = Counter32
_Hh3cDot11TxDiscardFrameBytes_Object = MibTableColumn
hh3cDot11TxDiscardFrameBytes = _Hh3cDot11TxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 17),
    _Hh3cDot11TxDiscardFrameBytes_Type()
)
hh3cDot11TxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxDiscardFrameBytes.setStatus("current")
_Hh3cDot11TxAuthenFrameCnt_Type = Counter32
_Hh3cDot11TxAuthenFrameCnt_Object = MibTableColumn
hh3cDot11TxAuthenFrameCnt = _Hh3cDot11TxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 18),
    _Hh3cDot11TxAuthenFrameCnt_Type()
)
hh3cDot11TxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxAuthenFrameCnt.setStatus("current")
_Hh3cDot11TxAssociateFrameCnt_Type = Counter32
_Hh3cDot11TxAssociateFrameCnt_Object = MibTableColumn
hh3cDot11TxAssociateFrameCnt = _Hh3cDot11TxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 19),
    _Hh3cDot11TxAssociateFrameCnt_Type()
)
hh3cDot11TxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxAssociateFrameCnt.setStatus("current")
_Hh3cDot11TxFrameRetryRatio_Type = Integer32
_Hh3cDot11TxFrameRetryRatio_Object = MibTableColumn
hh3cDot11TxFrameRetryRatio = _Hh3cDot11TxFrameRetryRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 20),
    _Hh3cDot11TxFrameRetryRatio_Type()
)
hh3cDot11TxFrameRetryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxFrameRetryRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11TxFrameRetryRatio.setUnits("onepercent")
_Hh3cDot11TxDataFrameCnt_Type = Counter32
_Hh3cDot11TxDataFrameCnt_Object = MibTableColumn
hh3cDot11TxDataFrameCnt = _Hh3cDot11TxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 21),
    _Hh3cDot11TxDataFrameCnt_Type()
)
hh3cDot11TxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxDataFrameCnt.setStatus("current")
_Hh3cDot11TxDataFrameBytes_Type = Counter32
_Hh3cDot11TxDataFrameBytes_Object = MibTableColumn
hh3cDot11TxDataFrameBytes = _Hh3cDot11TxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 22),
    _Hh3cDot11TxDataFrameBytes_Type()
)
hh3cDot11TxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxDataFrameBytes.setStatus("current")
_Hh3cDot11TxMSDUCnt_Type = Counter32
_Hh3cDot11TxMSDUCnt_Object = MibTableColumn
hh3cDot11TxMSDUCnt = _Hh3cDot11TxMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 23),
    _Hh3cDot11TxMSDUCnt_Type()
)
hh3cDot11TxMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxMSDUCnt.setStatus("current")
_Hh3cDot11TxDiscardMSDUCnt_Type = Counter32
_Hh3cDot11TxDiscardMSDUCnt_Object = MibTableColumn
hh3cDot11TxDiscardMSDUCnt = _Hh3cDot11TxDiscardMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 24),
    _Hh3cDot11TxDiscardMSDUCnt_Type()
)
hh3cDot11TxDiscardMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxDiscardMSDUCnt.setStatus("current")
_Hh3cDot11RetryMSDUCnt_Type = Counter32
_Hh3cDot11RetryMSDUCnt_Object = MibTableColumn
hh3cDot11RetryMSDUCnt = _Hh3cDot11RetryMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 25),
    _Hh3cDot11RetryMSDUCnt_Type()
)
hh3cDot11RetryMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RetryMSDUCnt.setStatus("current")
_Hh3cDot11TxPayloadBytes_Type = Counter32
_Hh3cDot11TxPayloadBytes_Object = MibTableColumn
hh3cDot11TxPayloadBytes = _Hh3cDot11TxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 26),
    _Hh3cDot11TxPayloadBytes_Type()
)
hh3cDot11TxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxPayloadBytes.setStatus("current")
_Hh3cDot11TxTrafficSpeed_Type = Integer32
_Hh3cDot11TxTrafficSpeed_Object = MibTableColumn
hh3cDot11TxTrafficSpeed = _Hh3cDot11TxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 27),
    _Hh3cDot11TxTrafficSpeed_Type()
)
hh3cDot11TxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11TxTrafficSpeed.setUnits("byte/s")
_Hh3cDot11TxErrFrameRatio_Type = Integer32
_Hh3cDot11TxErrFrameRatio_Object = MibTableColumn
hh3cDot11TxErrFrameRatio = _Hh3cDot11TxErrFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 28),
    _Hh3cDot11TxErrFrameRatio_Type()
)
hh3cDot11TxErrFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxErrFrameRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11TxErrFrameRatio.setUnits("onepercent")
_Hh3cDot11TxFrameRate_Type = Integer32
_Hh3cDot11TxFrameRate_Object = MibTableColumn
hh3cDot11TxFrameRate = _Hh3cDot11TxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 29),
    _Hh3cDot11TxFrameRate_Type()
)
hh3cDot11TxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxFrameRate.setStatus("current")
_Hh3cDot11TxMgtFrameCnt_Type = Counter32
_Hh3cDot11TxMgtFrameCnt_Object = MibTableColumn
hh3cDot11TxMgtFrameCnt = _Hh3cDot11TxMgtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 30),
    _Hh3cDot11TxMgtFrameCnt_Type()
)
hh3cDot11TxMgtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxMgtFrameCnt.setStatus("current")
_Hh3cDot11TxCtrlFrameCnt_Type = Counter32
_Hh3cDot11TxCtrlFrameCnt_Object = MibTableColumn
hh3cDot11TxCtrlFrameCnt = _Hh3cDot11TxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 31),
    _Hh3cDot11TxCtrlFrameCnt_Type()
)
hh3cDot11TxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxCtrlFrameCnt.setStatus("current")
_Hh3cDot11TxMACErrCnt_Type = Counter32
_Hh3cDot11TxMACErrCnt_Object = MibTableColumn
hh3cDot11TxMACErrCnt = _Hh3cDot11TxMACErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 32),
    _Hh3cDot11TxMACErrCnt_Type()
)
hh3cDot11TxMACErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxMACErrCnt.setStatus("current")
_Hh3cDot11TxErrFrameCnt_Type = Counter32
_Hh3cDot11TxErrFrameCnt_Object = MibTableColumn
hh3cDot11TxErrFrameCnt = _Hh3cDot11TxErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 33),
    _Hh3cDot11TxErrFrameCnt_Type()
)
hh3cDot11TxErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxErrFrameCnt.setStatus("current")
_Hh3cDot11TxUcastDataFrameCnt_Type = Counter64
_Hh3cDot11TxUcastDataFrameCnt_Object = MibTableColumn
hh3cDot11TxUcastDataFrameCnt = _Hh3cDot11TxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 34),
    _Hh3cDot11TxUcastDataFrameCnt_Type()
)
hh3cDot11TxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxUcastDataFrameCnt.setStatus("current")
_Hh3cDot11TxNUcastDataFrameCnt_Type = Counter64
_Hh3cDot11TxNUcastDataFrameCnt_Object = MibTableColumn
hh3cDot11TxNUcastDataFrameCnt = _Hh3cDot11TxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 35),
    _Hh3cDot11TxNUcastDataFrameCnt_Type()
)
hh3cDot11TxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxNUcastDataFrameCnt.setStatus("current")
_Hh3cDot11TxTotalFrameCnt_Type = Counter64
_Hh3cDot11TxTotalFrameCnt_Object = MibTableColumn
hh3cDot11TxTotalFrameCnt = _Hh3cDot11TxTotalFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 2, 1, 36),
    _Hh3cDot11TxTotalFrameCnt_Type()
)
hh3cDot11TxTotalFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TxTotalFrameCnt.setStatus("current")
_Hh3cDot11APAssocStatisTable_Object = MibTable
hh3cDot11APAssocStatisTable = _Hh3cDot11APAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocStatisTable.setStatus("current")
_Hh3cDot11APAssocStatisEntry_Object = MibTableRow
hh3cDot11APAssocStatisEntry = _Hh3cDot11APAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1)
)
hh3cDot11APAssocStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocStatisEntry.setStatus("current")
_Hh3cDot11ApStationAssocSum_Type = Counter32
_Hh3cDot11ApStationAssocSum_Object = MibTableColumn
hh3cDot11ApStationAssocSum = _Hh3cDot11ApStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 1),
    _Hh3cDot11ApStationAssocSum_Type()
)
hh3cDot11ApStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationAssocSum.setStatus("current")
_Hh3cDot11ApStationAssocFailSum_Type = Counter32
_Hh3cDot11ApStationAssocFailSum_Object = MibTableColumn
hh3cDot11ApStationAssocFailSum = _Hh3cDot11ApStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 2),
    _Hh3cDot11ApStationAssocFailSum_Type()
)
hh3cDot11ApStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationAssocFailSum.setStatus("current")
_Hh3cDot11ApStationReassocSum_Type = Counter32
_Hh3cDot11ApStationReassocSum_Object = MibTableColumn
hh3cDot11ApStationReassocSum = _Hh3cDot11ApStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 3),
    _Hh3cDot11ApStationReassocSum_Type()
)
hh3cDot11ApStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationReassocSum.setStatus("current")
_Hh3cDot11ApStationAssocRejectSum_Type = Counter32
_Hh3cDot11ApStationAssocRejectSum_Object = MibTableColumn
hh3cDot11ApStationAssocRejectSum = _Hh3cDot11ApStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 4),
    _Hh3cDot11ApStationAssocRejectSum_Type()
)
hh3cDot11ApStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationAssocRejectSum.setStatus("current")
_Hh3cDot11ApStationExDeAuthenSum_Type = Counter32
_Hh3cDot11ApStationExDeAuthenSum_Object = MibTableColumn
hh3cDot11ApStationExDeAuthenSum = _Hh3cDot11ApStationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 5),
    _Hh3cDot11ApStationExDeAuthenSum_Type()
)
hh3cDot11ApStationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationExDeAuthenSum.setStatus("current")
_Hh3cDot11ApStationCurAssocSum_Type = Integer32
_Hh3cDot11ApStationCurAssocSum_Object = MibTableColumn
hh3cDot11ApStationCurAssocSum = _Hh3cDot11ApStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 6),
    _Hh3cDot11ApStationCurAssocSum_Type()
)
hh3cDot11ApStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationCurAssocSum.setStatus("current")
_Hh3cDot11ApStaCurAuthSuccSum_Type = Integer32
_Hh3cDot11ApStaCurAuthSuccSum_Object = MibTableColumn
hh3cDot11ApStaCurAuthSuccSum = _Hh3cDot11ApStaCurAuthSuccSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 7),
    _Hh3cDot11ApStaCurAuthSuccSum_Type()
)
hh3cDot11ApStaCurAuthSuccSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStaCurAuthSuccSum.setStatus("current")
_Hh3cDot11AllStationUpSumTime_Type = Counter32
_Hh3cDot11AllStationUpSumTime_Object = MibTableColumn
hh3cDot11AllStationUpSumTime = _Hh3cDot11AllStationUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 8),
    _Hh3cDot11AllStationUpSumTime_Type()
)
hh3cDot11AllStationUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AllStationUpSumTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AllStationUpSumTime.setUnits("minute")
_Hh3cDot11ApStationAssocReqSum_Type = Counter32
_Hh3cDot11ApStationAssocReqSum_Object = MibTableColumn
hh3cDot11ApStationAssocReqSum = _Hh3cDot11ApStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 9),
    _Hh3cDot11ApStationAssocReqSum_Type()
)
hh3cDot11ApStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationAssocReqSum.setStatus("current")
_Hh3cDot11AllStationUpSumTimeTicks_Type = TimeTicks
_Hh3cDot11AllStationUpSumTimeTicks_Object = MibTableColumn
hh3cDot11AllStationUpSumTimeTicks = _Hh3cDot11AllStationUpSumTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 10),
    _Hh3cDot11AllStationUpSumTimeTicks_Type()
)
hh3cDot11AllStationUpSumTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AllStationUpSumTimeTicks.setStatus("current")
_Hh3cDot11ApStationReassocReqSum_Type = Counter32
_Hh3cDot11ApStationReassocReqSum_Object = MibTableColumn
hh3cDot11ApStationReassocReqSum = _Hh3cDot11ApStationReassocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 11),
    _Hh3cDot11ApStationReassocReqSum_Type()
)
hh3cDot11ApStationReassocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationReassocReqSum.setStatus("current")
_Hh3cDot11ApStationReassocFailSum_Type = Counter32
_Hh3cDot11ApStationReassocFailSum_Object = MibTableColumn
hh3cDot11ApStationReassocFailSum = _Hh3cDot11ApStationReassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 3, 1, 12),
    _Hh3cDot11ApStationReassocFailSum_Type()
)
hh3cDot11ApStationReassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ApStationReassocFailSum.setStatus("current")
_Hh3cDot11BSSRxStatisTable_Object = MibTable
hh3cDot11BSSRxStatisTable = _Hh3cDot11BSSRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11BSSRxStatisTable.setStatus("current")
_Hh3cDot11BSSRxStatisEntry_Object = MibTableRow
hh3cDot11BSSRxStatisEntry = _Hh3cDot11BSSRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1)
)
hh3cDot11BSSRxStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11BSSRxStatisEntry.setStatus("current")
_Hh3cDot11BSSRxFrameCnt_Type = Counter32
_Hh3cDot11BSSRxFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxFrameCnt = _Hh3cDot11BSSRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 1),
    _Hh3cDot11BSSRxFrameCnt_Type()
)
hh3cDot11BSSRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxFrameCnt.setStatus("current")
_Hh3cDot11BSSRxFrameBytes_Type = Counter32
_Hh3cDot11BSSRxFrameBytes_Object = MibTableColumn
hh3cDot11BSSRxFrameBytes = _Hh3cDot11BSSRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 2),
    _Hh3cDot11BSSRxFrameBytes_Type()
)
hh3cDot11BSSRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxFrameBytes.setStatus("current")
_Hh3cDot11BSSRxDataFrameCnt_Type = Counter32
_Hh3cDot11BSSRxDataFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxDataFrameCnt = _Hh3cDot11BSSRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 3),
    _Hh3cDot11BSSRxDataFrameCnt_Type()
)
hh3cDot11BSSRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxDataFrameCnt.setStatus("current")
_Hh3cDot11BSSRxDataFrameBytes_Type = Counter32
_Hh3cDot11BSSRxDataFrameBytes_Object = MibTableColumn
hh3cDot11BSSRxDataFrameBytes = _Hh3cDot11BSSRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 4),
    _Hh3cDot11BSSRxDataFrameBytes_Type()
)
hh3cDot11BSSRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxDataFrameBytes.setStatus("current")
_Hh3cDot11BSSRxAssociateFrameCnt_Type = Counter32
_Hh3cDot11BSSRxAssociateFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxAssociateFrameCnt = _Hh3cDot11BSSRxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 5),
    _Hh3cDot11BSSRxAssociateFrameCnt_Type()
)
hh3cDot11BSSRxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxAssociateFrameCnt.setStatus("current")
_Hh3cDot11BSSRxFrameErrorRatio_Type = Integer32
_Hh3cDot11BSSRxFrameErrorRatio_Object = MibTableColumn
hh3cDot11BSSRxFrameErrorRatio = _Hh3cDot11BSSRxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 6),
    _Hh3cDot11BSSRxFrameErrorRatio_Type()
)
hh3cDot11BSSRxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxFrameErrorRatio.setUnits("percent")
_Hh3cDot11BSSRxPayloadBytes_Type = Counter32
_Hh3cDot11BSSRxPayloadBytes_Object = MibTableColumn
hh3cDot11BSSRxPayloadBytes = _Hh3cDot11BSSRxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 7),
    _Hh3cDot11BSSRxPayloadBytes_Type()
)
hh3cDot11BSSRxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxPayloadBytes.setStatus("current")
_Hh3cDot11BSSRxUniFrameCnt_Type = Counter32
_Hh3cDot11BSSRxUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxUniFrameCnt = _Hh3cDot11BSSRxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 8),
    _Hh3cDot11BSSRxUniFrameCnt_Type()
)
hh3cDot11BSSRxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxUniFrameCnt.setStatus("current")
_Hh3cDot11BSSRxNonUniFrameCnt_Type = Integer32
_Hh3cDot11BSSRxNonUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxNonUniFrameCnt = _Hh3cDot11BSSRxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 9),
    _Hh3cDot11BSSRxNonUniFrameCnt_Type()
)
hh3cDot11BSSRxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxNonUniFrameCnt.setStatus("current")
_Hh3cDot11BSSRxAuthenFrameCnt_Type = Counter32
_Hh3cDot11BSSRxAuthenFrameCnt_Object = MibTableColumn
hh3cDot11BSSRxAuthenFrameCnt = _Hh3cDot11BSSRxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 4, 1, 10),
    _Hh3cDot11BSSRxAuthenFrameCnt_Type()
)
hh3cDot11BSSRxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRxAuthenFrameCnt.setStatus("current")
_Hh3cDot11BSSTxStatisTable_Object = MibTable
hh3cDot11BSSTxStatisTable = _Hh3cDot11BSSTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11BSSTxStatisTable.setStatus("current")
_Hh3cDot11BSSTxStatisEntry_Object = MibTableRow
hh3cDot11BSSTxStatisEntry = _Hh3cDot11BSSTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1)
)
hh3cDot11BSSTxStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11BSSTxStatisEntry.setStatus("current")
_Hh3cDot11BSSTxFrameCnt_Type = Counter32
_Hh3cDot11BSSTxFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxFrameCnt = _Hh3cDot11BSSTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 1),
    _Hh3cDot11BSSTxFrameCnt_Type()
)
hh3cDot11BSSTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxFrameCnt.setStatus("current")
_Hh3cDot11BSSTxFrameBytes_Type = Counter32
_Hh3cDot11BSSTxFrameBytes_Object = MibTableColumn
hh3cDot11BSSTxFrameBytes = _Hh3cDot11BSSTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 2),
    _Hh3cDot11BSSTxFrameBytes_Type()
)
hh3cDot11BSSTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxFrameBytes.setStatus("current")
_Hh3cDot11BSSTxDataFrameCnt_Type = Counter32
_Hh3cDot11BSSTxDataFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxDataFrameCnt = _Hh3cDot11BSSTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 3),
    _Hh3cDot11BSSTxDataFrameCnt_Type()
)
hh3cDot11BSSTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxDataFrameCnt.setStatus("current")
_Hh3cDot11BSSTxDataFrameBytes_Type = Counter32
_Hh3cDot11BSSTxDataFrameBytes_Object = MibTableColumn
hh3cDot11BSSTxDataFrameBytes = _Hh3cDot11BSSTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 4),
    _Hh3cDot11BSSTxDataFrameBytes_Type()
)
hh3cDot11BSSTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxDataFrameBytes.setStatus("current")
_Hh3cDot11BSSTxAssociateFrameCnt_Type = Counter32
_Hh3cDot11BSSTxAssociateFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxAssociateFrameCnt = _Hh3cDot11BSSTxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 5),
    _Hh3cDot11BSSTxAssociateFrameCnt_Type()
)
hh3cDot11BSSTxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxAssociateFrameCnt.setStatus("current")
_Hh3cDot11BSSTxPayloadBytes_Type = Counter32
_Hh3cDot11BSSTxPayloadBytes_Object = MibTableColumn
hh3cDot11BSSTxPayloadBytes = _Hh3cDot11BSSTxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 6),
    _Hh3cDot11BSSTxPayloadBytes_Type()
)
hh3cDot11BSSTxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxPayloadBytes.setStatus("current")
_Hh3cDot11BSSTxRetryCnt_Type = Counter32
_Hh3cDot11BSSTxRetryCnt_Object = MibTableColumn
hh3cDot11BSSTxRetryCnt = _Hh3cDot11BSSTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 7),
    _Hh3cDot11BSSTxRetryCnt_Type()
)
hh3cDot11BSSTxRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxRetryCnt.setStatus("current")
_Hh3cDot11BSSTxUniFrameCnt_Type = Counter32
_Hh3cDot11BSSTxUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxUniFrameCnt = _Hh3cDot11BSSTxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 8),
    _Hh3cDot11BSSTxUniFrameCnt_Type()
)
hh3cDot11BSSTxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxUniFrameCnt.setStatus("current")
_Hh3cDot11BSSTxNonUniFrameCnt_Type = Integer32
_Hh3cDot11BSSTxNonUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxNonUniFrameCnt = _Hh3cDot11BSSTxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 9),
    _Hh3cDot11BSSTxNonUniFrameCnt_Type()
)
hh3cDot11BSSTxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxNonUniFrameCnt.setStatus("current")
_Hh3cDot11BSSTxAuthenFrameCnt_Type = Counter32
_Hh3cDot11BSSTxAuthenFrameCnt_Object = MibTableColumn
hh3cDot11BSSTxAuthenFrameCnt = _Hh3cDot11BSSTxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 5, 1, 10),
    _Hh3cDot11BSSTxAuthenFrameCnt_Type()
)
hh3cDot11BSSTxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTxAuthenFrameCnt.setStatus("current")
_Hh3cDot11BSSAssocStatisTable_Object = MibTable
hh3cDot11BSSAssocStatisTable = _Hh3cDot11BSSAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11BSSAssocStatisTable.setStatus("current")
_Hh3cDot11BSSAssocStatisEntry_Object = MibTableRow
hh3cDot11BSSAssocStatisEntry = _Hh3cDot11BSSAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1)
)
hh3cDot11BSSAssocStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11BSSAssocStatisEntry.setStatus("current")
_Hh3cDot11BSSStationAssocSum_Type = Counter32
_Hh3cDot11BSSStationAssocSum_Object = MibTableColumn
hh3cDot11BSSStationAssocSum = _Hh3cDot11BSSStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 1),
    _Hh3cDot11BSSStationAssocSum_Type()
)
hh3cDot11BSSStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationAssocSum.setStatus("current")
_Hh3cDot11BSSStationAssocFailSum_Type = Counter32
_Hh3cDot11BSSStationAssocFailSum_Object = MibTableColumn
hh3cDot11BSSStationAssocFailSum = _Hh3cDot11BSSStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 2),
    _Hh3cDot11BSSStationAssocFailSum_Type()
)
hh3cDot11BSSStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationAssocFailSum.setStatus("current")
_Hh3cDot11BSSStationReassocSum_Type = Counter32
_Hh3cDot11BSSStationReassocSum_Object = MibTableColumn
hh3cDot11BSSStationReassocSum = _Hh3cDot11BSSStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 3),
    _Hh3cDot11BSSStationReassocSum_Type()
)
hh3cDot11BSSStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationReassocSum.setStatus("current")
_Hh3cDot11BSSStationAssocRejectSum_Type = Counter32
_Hh3cDot11BSSStationAssocRejectSum_Object = MibTableColumn
hh3cDot11BSSStationAssocRejectSum = _Hh3cDot11BSSStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 4),
    _Hh3cDot11BSSStationAssocRejectSum_Type()
)
hh3cDot11BSSStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationAssocRejectSum.setStatus("current")
_Hh3cDot11BSSStationExDeAssocSum_Type = Counter32
_Hh3cDot11BSSStationExDeAssocSum_Object = MibTableColumn
hh3cDot11BSSStationExDeAssocSum = _Hh3cDot11BSSStationExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 5),
    _Hh3cDot11BSSStationExDeAssocSum_Type()
)
hh3cDot11BSSStationExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationExDeAssocSum.setStatus("current")
_Hh3cDot11BSSStationCurAssocSum_Type = Integer32
_Hh3cDot11BSSStationCurAssocSum_Object = MibTableColumn
hh3cDot11BSSStationCurAssocSum = _Hh3cDot11BSSStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 6),
    _Hh3cDot11BSSStationCurAssocSum_Type()
)
hh3cDot11BSSStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationCurAssocSum.setStatus("current")
_Hh3cDot11BSSStationAssocReqSum_Type = Counter32
_Hh3cDot11BSSStationAssocReqSum_Object = MibTableColumn
hh3cDot11BSSStationAssocReqSum = _Hh3cDot11BSSStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 7),
    _Hh3cDot11BSSStationAssocReqSum_Type()
)
hh3cDot11BSSStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationAssocReqSum.setStatus("current")
_Hh3cDot11BSSStationCurAuthSum_Type = Integer32
_Hh3cDot11BSSStationCurAuthSum_Object = MibTableColumn
hh3cDot11BSSStationCurAuthSum = _Hh3cDot11BSSStationCurAuthSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 6, 1, 8),
    _Hh3cDot11BSSStationCurAuthSum_Type()
)
hh3cDot11BSSStationCurAuthSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSStationCurAuthSum.setStatus("current")
_Hh3cDot11APLinkStatisTable_Object = MibTable
hh3cDot11APLinkStatisTable = _Hh3cDot11APLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11APLinkStatisTable.setStatus("current")
_Hh3cDot11APLinkStatisEntry_Object = MibTableRow
hh3cDot11APLinkStatisEntry = _Hh3cDot11APLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1)
)
hh3cDot11APLinkStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APLinkStatisEntry.setStatus("current")
_Hh3cDot11UpLinkUpDownTimes_Type = Counter32
_Hh3cDot11UpLinkUpDownTimes_Object = MibTableColumn
hh3cDot11UpLinkUpDownTimes = _Hh3cDot11UpLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 1),
    _Hh3cDot11UpLinkUpDownTimes_Type()
)
hh3cDot11UpLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11UpLinkUpDownTimes.setStatus("current")
_Hh3cDot11DownLinkUpDownTimes_Type = Counter32
_Hh3cDot11DownLinkUpDownTimes_Object = MibTableColumn
hh3cDot11DownLinkUpDownTimes = _Hh3cDot11DownLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 2),
    _Hh3cDot11DownLinkUpDownTimes_Type()
)
hh3cDot11DownLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DownLinkUpDownTimes.setStatus("current")
_Hh3cDot11PrivateSrvRxFrameBytes_Type = Counter64
_Hh3cDot11PrivateSrvRxFrameBytes_Object = MibTableColumn
hh3cDot11PrivateSrvRxFrameBytes = _Hh3cDot11PrivateSrvRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 3),
    _Hh3cDot11PrivateSrvRxFrameBytes_Type()
)
hh3cDot11PrivateSrvRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PrivateSrvRxFrameBytes.setStatus("current")
_Hh3cDot11PrivateSrvTxFrameBytes_Type = Counter64
_Hh3cDot11PrivateSrvTxFrameBytes_Object = MibTableColumn
hh3cDot11PrivateSrvTxFrameBytes = _Hh3cDot11PrivateSrvTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 4),
    _Hh3cDot11PrivateSrvTxFrameBytes_Type()
)
hh3cDot11PrivateSrvTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PrivateSrvTxFrameBytes.setStatus("current")
_Hh3cDot11APInternetAllRxBytes_Type = Counter64
_Hh3cDot11APInternetAllRxBytes_Object = MibTableColumn
hh3cDot11APInternetAllRxBytes = _Hh3cDot11APInternetAllRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 5),
    _Hh3cDot11APInternetAllRxBytes_Type()
)
hh3cDot11APInternetAllRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APInternetAllRxBytes.setStatus("current")
_Hh3cDot11APInternetAllTxBytes_Type = Counter64
_Hh3cDot11APInternetAllTxBytes_Object = MibTableColumn
hh3cDot11APInternetAllTxBytes = _Hh3cDot11APInternetAllTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 6),
    _Hh3cDot11APInternetAllTxBytes_Type()
)
hh3cDot11APInternetAllTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APInternetAllTxBytes.setStatus("current")
_Hh3cDot11APLocalAllRxBytes_Type = Counter64
_Hh3cDot11APLocalAllRxBytes_Object = MibTableColumn
hh3cDot11APLocalAllRxBytes = _Hh3cDot11APLocalAllRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 7),
    _Hh3cDot11APLocalAllRxBytes_Type()
)
hh3cDot11APLocalAllRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLocalAllRxBytes.setStatus("current")
_Hh3cDot11APLocalAllTxBytes_Type = Counter64
_Hh3cDot11APLocalAllTxBytes_Object = MibTableColumn
hh3cDot11APLocalAllTxBytes = _Hh3cDot11APLocalAllTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 7, 1, 8),
    _Hh3cDot11APLocalAllTxBytes_Type()
)
hh3cDot11APLocalAllTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLocalAllTxBytes.setStatus("current")
_Hh3cDot11RadioAssocStatisTable_Object = MibTable
hh3cDot11RadioAssocStatisTable = _Hh3cDot11RadioAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioAssocStatisTable.setStatus("current")
_Hh3cDot11RadioAssocStatisEntry_Object = MibTableRow
hh3cDot11RadioAssocStatisEntry = _Hh3cDot11RadioAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1)
)
hh3cDot11RadioAssocStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioAssocStatisEntry.setStatus("current")
_Hh3cDot11RadioStaAssocSum_Type = Counter32
_Hh3cDot11RadioStaAssocSum_Object = MibTableColumn
hh3cDot11RadioStaAssocSum = _Hh3cDot11RadioStaAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 1),
    _Hh3cDot11RadioStaAssocSum_Type()
)
hh3cDot11RadioStaAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaAssocSum.setStatus("current")
_Hh3cDot11RadioStaAssocFailSum_Type = Counter32
_Hh3cDot11RadioStaAssocFailSum_Object = MibTableColumn
hh3cDot11RadioStaAssocFailSum = _Hh3cDot11RadioStaAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 2),
    _Hh3cDot11RadioStaAssocFailSum_Type()
)
hh3cDot11RadioStaAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaAssocFailSum.setStatus("current")
_Hh3cDot11RadioStaReassocSum_Type = Counter32
_Hh3cDot11RadioStaReassocSum_Object = MibTableColumn
hh3cDot11RadioStaReassocSum = _Hh3cDot11RadioStaReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 3),
    _Hh3cDot11RadioStaReassocSum_Type()
)
hh3cDot11RadioStaReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaReassocSum.setStatus("current")
_Hh3cDot11RadioStaAssocRejectSum_Type = Counter32
_Hh3cDot11RadioStaAssocRejectSum_Object = MibTableColumn
hh3cDot11RadioStaAssocRejectSum = _Hh3cDot11RadioStaAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 4),
    _Hh3cDot11RadioStaAssocRejectSum_Type()
)
hh3cDot11RadioStaAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaAssocRejectSum.setStatus("current")
_Hh3cDot11RadioStaExDeAssocSum_Type = Counter32
_Hh3cDot11RadioStaExDeAssocSum_Object = MibTableColumn
hh3cDot11RadioStaExDeAssocSum = _Hh3cDot11RadioStaExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 5),
    _Hh3cDot11RadioStaExDeAssocSum_Type()
)
hh3cDot11RadioStaExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaExDeAssocSum.setStatus("current")
_Hh3cDot11RadioStaCurAssocSum_Type = Integer32
_Hh3cDot11RadioStaCurAssocSum_Object = MibTableColumn
hh3cDot11RadioStaCurAssocSum = _Hh3cDot11RadioStaCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 8, 1, 6),
    _Hh3cDot11RadioStaCurAssocSum_Type()
)
hh3cDot11RadioStaCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioStaCurAssocSum.setStatus("current")
_Hh3cDot11RadioMngFrameStatisTable_Object = MibTable
hh3cDot11RadioMngFrameStatisTable = _Hh3cDot11RadioMngFrameStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioMngFrameStatisTable.setStatus("current")
_Hh3cDot11RadioMngFrameStatisEntry_Object = MibTableRow
hh3cDot11RadioMngFrameStatisEntry = _Hh3cDot11RadioMngFrameStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 9, 1)
)
hh3cDot11RadioMngFrameStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioStatisIndex"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11MngFrameType"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioMngFrameStatisEntry.setStatus("current")
_Hh3cDot11RadioStatisIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11RadioStatisIndex_Object = MibTableColumn
hh3cDot11RadioStatisIndex = _Hh3cDot11RadioStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 9, 1, 1),
    _Hh3cDot11RadioStatisIndex_Type()
)
hh3cDot11RadioStatisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioStatisIndex.setStatus("current")


class _Hh3cDot11MngFrameType_Type(Integer32):
    """Custom type hh3cDot11MngFrameType based on Integer32"""
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


_Hh3cDot11MngFrameType_Type.__name__ = "Integer32"
_Hh3cDot11MngFrameType_Object = MibTableColumn
hh3cDot11MngFrameType = _Hh3cDot11MngFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 9, 1, 2),
    _Hh3cDot11MngFrameType_Type()
)
hh3cDot11MngFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11MngFrameType.setStatus("current")
_Hh3cDot11MngFrameCnt_Type = Counter32
_Hh3cDot11MngFrameCnt_Object = MibTableColumn
hh3cDot11MngFrameCnt = _Hh3cDot11MngFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 9, 1, 3),
    _Hh3cDot11MngFrameCnt_Type()
)
hh3cDot11MngFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MngFrameCnt.setStatus("current")
_Hh3cDot11APAuthFailStatisTable_Object = MibTable
hh3cDot11APAuthFailStatisTable = _Hh3cDot11APAuthFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cDot11APAuthFailStatisTable.setStatus("current")
_Hh3cDot11APAuthFailStatisEntry_Object = MibTableRow
hh3cDot11APAuthFailStatisEntry = _Hh3cDot11APAuthFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 10, 1)
)
hh3cDot11APAuthFailStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APAuthFailStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APAuthFailStatisEntry.setStatus("current")


class _Hh3cDot11APAuthFailStatisType_Type(Integer32):
    """Custom type hh3cDot11APAuthFailStatisType based on Integer32"""
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


_Hh3cDot11APAuthFailStatisType_Type.__name__ = "Integer32"
_Hh3cDot11APAuthFailStatisType_Object = MibTableColumn
hh3cDot11APAuthFailStatisType = _Hh3cDot11APAuthFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 10, 1, 1),
    _Hh3cDot11APAuthFailStatisType_Type()
)
hh3cDot11APAuthFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APAuthFailStatisType.setStatus("current")
_Hh3cDot11APAuthFailStatisCnt_Type = Counter32
_Hh3cDot11APAuthFailStatisCnt_Object = MibTableColumn
hh3cDot11APAuthFailStatisCnt = _Hh3cDot11APAuthFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 10, 1, 2),
    _Hh3cDot11APAuthFailStatisCnt_Type()
)
hh3cDot11APAuthFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAuthFailStatisCnt.setStatus("current")
_Hh3cDot11APAssocFailStatisTable_Object = MibTable
hh3cDot11APAssocFailStatisTable = _Hh3cDot11APAssocFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatisTable.setStatus("current")
_Hh3cDot11APAssocFailStatisEntry_Object = MibTableRow
hh3cDot11APAssocFailStatisEntry = _Hh3cDot11APAssocFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 11, 1)
)
hh3cDot11APAssocFailStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APAssocFailStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatisEntry.setStatus("current")


class _Hh3cDot11APAssocFailStatisType_Type(Integer32):
    """Custom type hh3cDot11APAssocFailStatisType based on Integer32"""
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


_Hh3cDot11APAssocFailStatisType_Type.__name__ = "Integer32"
_Hh3cDot11APAssocFailStatisType_Object = MibTableColumn
hh3cDot11APAssocFailStatisType = _Hh3cDot11APAssocFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 11, 1, 1),
    _Hh3cDot11APAssocFailStatisType_Type()
)
hh3cDot11APAssocFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatisType.setStatus("current")
_Hh3cDot11APAssocFailStatisCnt_Type = Counter32
_Hh3cDot11APAssocFailStatisCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatisCnt = _Hh3cDot11APAssocFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 11, 1, 2),
    _Hh3cDot11APAssocFailStatisCnt_Type()
)
hh3cDot11APAssocFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatisCnt.setStatus("current")
_Hh3cDot11APReassocStatisTable_Object = MibTable
hh3cDot11APReassocStatisTable = _Hh3cDot11APReassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatisTable.setStatus("current")
_Hh3cDot11APReassocStatisEntry_Object = MibTableRow
hh3cDot11APReassocStatisEntry = _Hh3cDot11APReassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 12, 1)
)
hh3cDot11APReassocStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APReassocStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatisEntry.setStatus("current")


class _Hh3cDot11APReassocStatisType_Type(Integer32):
    """Custom type hh3cDot11APReassocStatisType based on Integer32"""
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


_Hh3cDot11APReassocStatisType_Type.__name__ = "Integer32"
_Hh3cDot11APReassocStatisType_Object = MibTableColumn
hh3cDot11APReassocStatisType = _Hh3cDot11APReassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 12, 1, 1),
    _Hh3cDot11APReassocStatisType_Type()
)
hh3cDot11APReassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatisType.setStatus("current")
_Hh3cDot11APReassocStatisCnt_Type = Counter32
_Hh3cDot11APReassocStatisCnt_Object = MibTableColumn
hh3cDot11APReassocStatisCnt = _Hh3cDot11APReassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 12, 1, 2),
    _Hh3cDot11APReassocStatisCnt_Type()
)
hh3cDot11APReassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatisCnt.setStatus("current")
_Hh3cDot11APUserAuthStatisTable_Object = MibTable
hh3cDot11APUserAuthStatisTable = _Hh3cDot11APUserAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthStatisTable.setStatus("current")
_Hh3cDot11APUserAuthStatisEntry_Object = MibTableRow
hh3cDot11APUserAuthStatisEntry = _Hh3cDot11APUserAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 13, 1)
)
hh3cDot11APUserAuthStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11UserAuthStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthStatisEntry.setStatus("current")


class _Hh3cDot11UserAuthStatisType_Type(Integer32):
    """Custom type hh3cDot11UserAuthStatisType based on Integer32"""
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


_Hh3cDot11UserAuthStatisType_Type.__name__ = "Integer32"
_Hh3cDot11UserAuthStatisType_Object = MibTableColumn
hh3cDot11UserAuthStatisType = _Hh3cDot11UserAuthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 13, 1, 1),
    _Hh3cDot11UserAuthStatisType_Type()
)
hh3cDot11UserAuthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11UserAuthStatisType.setStatus("current")
_Hh3cDot11UserAuthStatisCnt_Type = Counter32
_Hh3cDot11UserAuthStatisCnt_Object = MibTableColumn
hh3cDot11UserAuthStatisCnt = _Hh3cDot11UserAuthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 13, 1, 2),
    _Hh3cDot11UserAuthStatisCnt_Type()
)
hh3cDot11UserAuthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11UserAuthStatisCnt.setStatus("current")
_Hh3cDot11APDeauthStatisTable_Object = MibTable
hh3cDot11APDeauthStatisTable = _Hh3cDot11APDeauthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cDot11APDeauthStatisTable.setStatus("current")
_Hh3cDot11APDeauthStatisEntry_Object = MibTableRow
hh3cDot11APDeauthStatisEntry = _Hh3cDot11APDeauthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 14, 1)
)
hh3cDot11APDeauthStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APDeauthStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APDeauthStatisEntry.setStatus("current")


class _Hh3cDot11APDeauthStatisType_Type(Integer32):
    """Custom type hh3cDot11APDeauthStatisType based on Integer32"""
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


_Hh3cDot11APDeauthStatisType_Type.__name__ = "Integer32"
_Hh3cDot11APDeauthStatisType_Object = MibTableColumn
hh3cDot11APDeauthStatisType = _Hh3cDot11APDeauthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 14, 1, 1),
    _Hh3cDot11APDeauthStatisType_Type()
)
hh3cDot11APDeauthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APDeauthStatisType.setStatus("current")
_Hh3cDot11APDeauthStatisCnt_Type = Counter32
_Hh3cDot11APDeauthStatisCnt_Object = MibTableColumn
hh3cDot11APDeauthStatisCnt = _Hh3cDot11APDeauthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 14, 1, 2),
    _Hh3cDot11APDeauthStatisCnt_Type()
)
hh3cDot11APDeauthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APDeauthStatisCnt.setStatus("current")
_Hh3cDot11APDeassocStatisTable_Object = MibTable
hh3cDot11APDeassocStatisTable = _Hh3cDot11APDeassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cDot11APDeassocStatisTable.setStatus("current")
_Hh3cDot11APDeassocStatisEntry_Object = MibTableRow
hh3cDot11APDeassocStatisEntry = _Hh3cDot11APDeassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 15, 1)
)
hh3cDot11APDeassocStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APDeassocStatisType"),
)
if mibBuilder.loadTexts:
    hh3cDot11APDeassocStatisEntry.setStatus("current")


class _Hh3cDot11APDeassocStatisType_Type(Integer32):
    """Custom type hh3cDot11APDeassocStatisType based on Integer32"""
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


_Hh3cDot11APDeassocStatisType_Type.__name__ = "Integer32"
_Hh3cDot11APDeassocStatisType_Object = MibTableColumn
hh3cDot11APDeassocStatisType = _Hh3cDot11APDeassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 15, 1, 1),
    _Hh3cDot11APDeassocStatisType_Type()
)
hh3cDot11APDeassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APDeassocStatisType.setStatus("current")
_Hh3cDot11APDeassocStatisCnt_Type = Counter32
_Hh3cDot11APDeassocStatisCnt_Object = MibTableColumn
hh3cDot11APDeassocStatisCnt = _Hh3cDot11APDeassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 15, 1, 2),
    _Hh3cDot11APDeassocStatisCnt_Type()
)
hh3cDot11APDeassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APDeassocStatisCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis2Table_Object = MibTable
hh3cDot11APAssocFailStatis2Table = _Hh3cDot11APAssocFailStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis2Table.setStatus("current")
_Hh3cDot11APAssocFailStatis2Entry_Object = MibTableRow
hh3cDot11APAssocFailStatis2Entry = _Hh3cDot11APAssocFailStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 16, 1)
)
hh3cDot11APAssocFailStatis2Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APAssocFailStatis2Type"),
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis2Entry.setStatus("current")


class _Hh3cDot11APAssocFailStatis2Type_Type(Integer32):
    """Custom type hh3cDot11APAssocFailStatis2Type based on Integer32"""
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
        *(("notSupportRateSet", 2),
          ("other", 4),
          ("rssiLowness", 5),
          ("shortResource", 1),
          ("unknownReasonCode", 3))
    )


_Hh3cDot11APAssocFailStatis2Type_Type.__name__ = "Integer32"
_Hh3cDot11APAssocFailStatis2Type_Object = MibTableColumn
hh3cDot11APAssocFailStatis2Type = _Hh3cDot11APAssocFailStatis2Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 16, 1, 1),
    _Hh3cDot11APAssocFailStatis2Type_Type()
)
hh3cDot11APAssocFailStatis2Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis2Type.setStatus("current")
_Hh3cDot11APAssocFailStatis2Cnt_Type = Counter32
_Hh3cDot11APAssocFailStatis2Cnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis2Cnt = _Hh3cDot11APAssocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 16, 1, 2),
    _Hh3cDot11APAssocFailStatis2Cnt_Type()
)
hh3cDot11APAssocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis2Cnt.setStatus("current")
_Hh3cDot11APIfStatisTable_Object = MibTable
hh3cDot11APIfStatisTable = _Hh3cDot11APIfStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cDot11APIfStatisTable.setStatus("current")
_Hh3cDot11APIfStatisEntry_Object = MibTableRow
hh3cDot11APIfStatisEntry = _Hh3cDot11APIfStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1)
)
hh3cDot11APIfStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIfStatisEntry.setStatus("current")
_Hh3cDot11APIfInPkts_Type = Counter32
_Hh3cDot11APIfInPkts_Object = MibTableColumn
hh3cDot11APIfInPkts = _Hh3cDot11APIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 1),
    _Hh3cDot11APIfInPkts_Type()
)
hh3cDot11APIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInPkts.setStatus("current")
_Hh3cDot11APIfInNormalPkts_Type = Counter32
_Hh3cDot11APIfInNormalPkts_Object = MibTableColumn
hh3cDot11APIfInNormalPkts = _Hh3cDot11APIfInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 2),
    _Hh3cDot11APIfInNormalPkts_Type()
)
hh3cDot11APIfInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInNormalPkts.setStatus("current")
_Hh3cDot11APIfInErrorPkts_Type = Counter32
_Hh3cDot11APIfInErrorPkts_Object = MibTableColumn
hh3cDot11APIfInErrorPkts = _Hh3cDot11APIfInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 3),
    _Hh3cDot11APIfInErrorPkts_Type()
)
hh3cDot11APIfInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInErrorPkts.setStatus("current")
_Hh3cDot11APIfOutPkts_Type = Counter32
_Hh3cDot11APIfOutPkts_Object = MibTableColumn
hh3cDot11APIfOutPkts = _Hh3cDot11APIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 4),
    _Hh3cDot11APIfOutPkts_Type()
)
hh3cDot11APIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutPkts.setStatus("current")
_Hh3cDot11APIfInOctets_Type = Counter32
_Hh3cDot11APIfInOctets_Object = MibTableColumn
hh3cDot11APIfInOctets = _Hh3cDot11APIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 5),
    _Hh3cDot11APIfInOctets_Type()
)
hh3cDot11APIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInOctets.setStatus("current")
_Hh3cDot11APIfOutOctets_Type = Counter32
_Hh3cDot11APIfOutOctets_Object = MibTableColumn
hh3cDot11APIfOutOctets = _Hh3cDot11APIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 6),
    _Hh3cDot11APIfOutOctets_Type()
)
hh3cDot11APIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutOctets.setStatus("current")
_Hh3cDot11APIfFlowOut_Type = Unsigned32
_Hh3cDot11APIfFlowOut_Object = MibTableColumn
hh3cDot11APIfFlowOut = _Hh3cDot11APIfFlowOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 7),
    _Hh3cDot11APIfFlowOut_Type()
)
hh3cDot11APIfFlowOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfFlowOut.setStatus("current")
_Hh3cDot11APIfFlowIN_Type = Unsigned32
_Hh3cDot11APIfFlowIN_Object = MibTableColumn
hh3cDot11APIfFlowIN = _Hh3cDot11APIfFlowIN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 8),
    _Hh3cDot11APIfFlowIN_Type()
)
hh3cDot11APIfFlowIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfFlowIN.setStatus("current")
_Hh3cDot11APIfInUcastPkts_Type = Counter32
_Hh3cDot11APIfInUcastPkts_Object = MibTableColumn
hh3cDot11APIfInUcastPkts = _Hh3cDot11APIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 9),
    _Hh3cDot11APIfInUcastPkts_Type()
)
hh3cDot11APIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInUcastPkts.setStatus("current")
_Hh3cDot11APIfInNUcastPkts_Type = Counter32
_Hh3cDot11APIfInNUcastPkts_Object = MibTableColumn
hh3cDot11APIfInNUcastPkts = _Hh3cDot11APIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 10),
    _Hh3cDot11APIfInNUcastPkts_Type()
)
hh3cDot11APIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInNUcastPkts.setStatus("current")
_Hh3cDot11APIfInDiscardPkts_Type = Counter32
_Hh3cDot11APIfInDiscardPkts_Object = MibTableColumn
hh3cDot11APIfInDiscardPkts = _Hh3cDot11APIfInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 11),
    _Hh3cDot11APIfInDiscardPkts_Type()
)
hh3cDot11APIfInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInDiscardPkts.setStatus("current")
_Hh3cDot11APIfOutUcastPkts_Type = Counter32
_Hh3cDot11APIfOutUcastPkts_Object = MibTableColumn
hh3cDot11APIfOutUcastPkts = _Hh3cDot11APIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 12),
    _Hh3cDot11APIfOutUcastPkts_Type()
)
hh3cDot11APIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutUcastPkts.setStatus("current")
_Hh3cDot11APIfOutNUcastPkts_Type = Counter32
_Hh3cDot11APIfOutNUcastPkts_Object = MibTableColumn
hh3cDot11APIfOutNUcastPkts = _Hh3cDot11APIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 13),
    _Hh3cDot11APIfOutNUcastPkts_Type()
)
hh3cDot11APIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutNUcastPkts.setStatus("current")
_Hh3cDot11APIfOutDiscardPkts_Type = Counter32
_Hh3cDot11APIfOutDiscardPkts_Object = MibTableColumn
hh3cDot11APIfOutDiscardPkts = _Hh3cDot11APIfOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 14),
    _Hh3cDot11APIfOutDiscardPkts_Type()
)
hh3cDot11APIfOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutDiscardPkts.setStatus("current")
_Hh3cDot11APIfOutErrorPkts_Type = Counter32
_Hh3cDot11APIfOutErrorPkts_Object = MibTableColumn
hh3cDot11APIfOutErrorPkts = _Hh3cDot11APIfOutErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 15),
    _Hh3cDot11APIfOutErrorPkts_Type()
)
hh3cDot11APIfOutErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutErrorPkts.setStatus("current")
_Hh3cDot11APIfUpdownTimes_Type = Counter32
_Hh3cDot11APIfUpdownTimes_Object = MibTableColumn
hh3cDot11APIfUpdownTimes = _Hh3cDot11APIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 16),
    _Hh3cDot11APIfUpdownTimes_Type()
)
hh3cDot11APIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfUpdownTimes.setStatus("current")
_Hh3cDot11APIfStatusKeepTime_Type = TimeTicks
_Hh3cDot11APIfStatusKeepTime_Object = MibTableColumn
hh3cDot11APIfStatusKeepTime = _Hh3cDot11APIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 17),
    _Hh3cDot11APIfStatusKeepTime_Type()
)
hh3cDot11APIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfStatusKeepTime.setStatus("current")


class _Hh3cDot11APIfOperStatus_Type(Integer32):
    """Custom type hh3cDot11APIfOperStatus based on Integer32"""
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


_Hh3cDot11APIfOperStatus_Type.__name__ = "Integer32"
_Hh3cDot11APIfOperStatus_Object = MibTableColumn
hh3cDot11APIfOperStatus = _Hh3cDot11APIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 18),
    _Hh3cDot11APIfOperStatus_Type()
)
hh3cDot11APIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOperStatus.setStatus("current")
_Hh3cDot11APIfInBrdcastPkts_Type = Counter64
_Hh3cDot11APIfInBrdcastPkts_Object = MibTableColumn
hh3cDot11APIfInBrdcastPkts = _Hh3cDot11APIfInBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 19),
    _Hh3cDot11APIfInBrdcastPkts_Type()
)
hh3cDot11APIfInBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInBrdcastPkts.setStatus("current")
_Hh3cDot11APIfOutBrdcastPkts_Type = Counter64
_Hh3cDot11APIfOutBrdcastPkts_Object = MibTableColumn
hh3cDot11APIfOutBrdcastPkts = _Hh3cDot11APIfOutBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 20),
    _Hh3cDot11APIfOutBrdcastPkts_Type()
)
hh3cDot11APIfOutBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutBrdcastPkts.setStatus("current")
_Hh3cDot11APIfInMulcastPkts_Type = Counter64
_Hh3cDot11APIfInMulcastPkts_Object = MibTableColumn
hh3cDot11APIfInMulcastPkts = _Hh3cDot11APIfInMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 21),
    _Hh3cDot11APIfInMulcastPkts_Type()
)
hh3cDot11APIfInMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInMulcastPkts.setStatus("current")
_Hh3cDot11APIfOutMulcastPkts_Type = Counter64
_Hh3cDot11APIfOutMulcastPkts_Object = MibTableColumn
hh3cDot11APIfOutMulcastPkts = _Hh3cDot11APIfOutMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 22),
    _Hh3cDot11APIfOutMulcastPkts_Type()
)
hh3cDot11APIfOutMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutMulcastPkts.setStatus("current")
_Hh3cDot11APIfInPayloadOctets_Type = Counter64
_Hh3cDot11APIfInPayloadOctets_Object = MibTableColumn
hh3cDot11APIfInPayloadOctets = _Hh3cDot11APIfInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 23),
    _Hh3cDot11APIfInPayloadOctets_Type()
)
hh3cDot11APIfInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInPayloadOctets.setStatus("current")
_Hh3cDot11APIfOutPayloadOctets_Type = Counter64
_Hh3cDot11APIfOutPayloadOctets_Object = MibTableColumn
hh3cDot11APIfOutPayloadOctets = _Hh3cDot11APIfOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 17, 1, 24),
    _Hh3cDot11APIfOutPayloadOctets_Type()
)
hh3cDot11APIfOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutPayloadOctets.setStatus("current")
_Hh3cDot11RadioMngFrmStatisTable_Object = MibTable
hh3cDot11RadioMngFrmStatisTable = _Hh3cDot11RadioMngFrmStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioMngFrmStatisTable.setStatus("current")
_Hh3cDot11RadioMngFrmStatisEntry_Object = MibTableRow
hh3cDot11RadioMngFrmStatisEntry = _Hh3cDot11RadioMngFrmStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 18, 1)
)
hh3cDot11RadioMngFrmStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11MngFrmType"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioMngFrmStatisEntry.setStatus("current")


class _Hh3cDot11MngFrmType_Type(Integer32):
    """Custom type hh3cDot11MngFrmType based on Integer32"""
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


_Hh3cDot11MngFrmType_Type.__name__ = "Integer32"
_Hh3cDot11MngFrmType_Object = MibTableColumn
hh3cDot11MngFrmType = _Hh3cDot11MngFrmType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 18, 1, 1),
    _Hh3cDot11MngFrmType_Type()
)
hh3cDot11MngFrmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11MngFrmType.setStatus("current")
_Hh3cDot11MngFrmCnt_Type = Counter32
_Hh3cDot11MngFrmCnt_Object = MibTableColumn
hh3cDot11MngFrmCnt = _Hh3cDot11MngFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 18, 1, 2),
    _Hh3cDot11MngFrmCnt_Type()
)
hh3cDot11MngFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MngFrmCnt.setStatus("current")
_Hh3cDot11APPacketSizeStatisTable_Object = MibTable
hh3cDot11APPacketSizeStatisTable = _Hh3cDot11APPacketSizeStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 19)
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketSizeStatisTable.setStatus("current")
_Hh3cDot11APPacketSizeStatisEntry_Object = MibTableRow
hh3cDot11APPacketSizeStatisEntry = _Hh3cDot11APPacketSizeStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 19, 1)
)
hh3cDot11APPacketSizeStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APPacketSize"),
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketSizeStatisEntry.setStatus("current")


class _Hh3cDot11APPacketSize_Type(Integer32):
    """Custom type hh3cDot11APPacketSize based on Integer32"""
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


_Hh3cDot11APPacketSize_Type.__name__ = "Integer32"
_Hh3cDot11APPacketSize_Object = MibTableColumn
hh3cDot11APPacketSize = _Hh3cDot11APPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 19, 1, 1),
    _Hh3cDot11APPacketSize_Type()
)
hh3cDot11APPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APPacketSize.setStatus("current")
_Hh3cDot11APRXPacketSizeCount_Type = Counter64
_Hh3cDot11APRXPacketSizeCount_Object = MibTableColumn
hh3cDot11APRXPacketSizeCount = _Hh3cDot11APRXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 19, 1, 2),
    _Hh3cDot11APRXPacketSizeCount_Type()
)
hh3cDot11APRXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APRXPacketSizeCount.setStatus("current")
_Hh3cDot11APTXPacketSizeCount_Type = Counter64
_Hh3cDot11APTXPacketSizeCount_Object = MibTableColumn
hh3cDot11APTXPacketSizeCount = _Hh3cDot11APTXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 19, 1, 3),
    _Hh3cDot11APTXPacketSizeCount_Type()
)
hh3cDot11APTXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTXPacketSizeCount.setStatus("current")
_Hh3cDot11APPacketRateStatisTable_Object = MibTable
hh3cDot11APPacketRateStatisTable = _Hh3cDot11APPacketRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 20)
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketRateStatisTable.setStatus("current")
_Hh3cDot11APPacketRateStatisEntry_Object = MibTableRow
hh3cDot11APPacketRateStatisEntry = _Hh3cDot11APPacketRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 20, 1)
)
hh3cDot11APPacketRateStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APPacketRate"),
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketRateStatisEntry.setStatus("current")
_Hh3cDot11APPacketRate_Type = Integer32
_Hh3cDot11APPacketRate_Object = MibTableColumn
hh3cDot11APPacketRate = _Hh3cDot11APPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 20, 1, 1),
    _Hh3cDot11APPacketRate_Type()
)
hh3cDot11APPacketRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APPacketRate.setStatus("current")
_Hh3cDot11APRXPacketRateCount_Type = Counter64
_Hh3cDot11APRXPacketRateCount_Object = MibTableColumn
hh3cDot11APRXPacketRateCount = _Hh3cDot11APRXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 20, 1, 2),
    _Hh3cDot11APRXPacketRateCount_Type()
)
hh3cDot11APRXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APRXPacketRateCount.setStatus("current")
_Hh3cDot11APTXPacketRateCount_Type = Counter64
_Hh3cDot11APTXPacketRateCount_Object = MibTableColumn
hh3cDot11APTXPacketRateCount = _Hh3cDot11APTXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 20, 1, 3),
    _Hh3cDot11APTXPacketRateCount_Type()
)
hh3cDot11APTXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTXPacketRateCount.setStatus("current")
_Hh3cDot11APPacketMCSRateStatisTable_Object = MibTable
hh3cDot11APPacketMCSRateStatisTable = _Hh3cDot11APPacketMCSRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 21)
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCSRateStatisTable.setStatus("current")
_Hh3cDot11APPacketMCSRateStatisEntry_Object = MibTableRow
hh3cDot11APPacketMCSRateStatisEntry = _Hh3cDot11APPacketMCSRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 21, 1)
)
hh3cDot11APPacketMCSRateStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APPacketMCSRate"),
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCSRateStatisEntry.setStatus("current")
_Hh3cDot11APPacketMCSRate_Type = Integer32
_Hh3cDot11APPacketMCSRate_Object = MibTableColumn
hh3cDot11APPacketMCSRate = _Hh3cDot11APPacketMCSRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 21, 1, 1),
    _Hh3cDot11APPacketMCSRate_Type()
)
hh3cDot11APPacketMCSRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCSRate.setStatus("current")
_Hh3cDot11APRXPacketMCSRateCount_Type = Counter64
_Hh3cDot11APRXPacketMCSRateCount_Object = MibTableColumn
hh3cDot11APRXPacketMCSRateCount = _Hh3cDot11APRXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 21, 1, 2),
    _Hh3cDot11APRXPacketMCSRateCount_Type()
)
hh3cDot11APRXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APRXPacketMCSRateCount.setStatus("current")
_Hh3cDot11APTXPacketMCSRateCount_Type = Counter64
_Hh3cDot11APTXPacketMCSRateCount_Object = MibTableColumn
hh3cDot11APTXPacketMCSRateCount = _Hh3cDot11APTXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 21, 1, 3),
    _Hh3cDot11APTXPacketMCSRateCount_Type()
)
hh3cDot11APTXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTXPacketMCSRateCount.setStatus("current")
_Hh3cDot11APAssocFailStatis3Table_Object = MibTable
hh3cDot11APAssocFailStatis3Table = _Hh3cDot11APAssocFailStatis3Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22)
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3Table.setStatus("current")
_Hh3cDot11APAssocFailStatis3Entry_Object = MibTableRow
hh3cDot11APAssocFailStatis3Entry = _Hh3cDot11APAssocFailStatis3Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1)
)
hh3cDot11APAssocFailStatis3Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3Entry.setStatus("current")
_Hh3cDot11APAssocFailStatis3SRCnt_Type = Counter32
_Hh3cDot11APAssocFailStatis3SRCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis3SRCnt = _Hh3cDot11APAssocFailStatis3SRCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 1),
    _Hh3cDot11APAssocFailStatis3SRCnt_Type()
)
hh3cDot11APAssocFailStatis3SRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3SRCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis3NSRCnt_Type = Counter32
_Hh3cDot11APAssocFailStatis3NSRCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis3NSRCnt = _Hh3cDot11APAssocFailStatis3NSRCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 2),
    _Hh3cDot11APAssocFailStatis3NSRCnt_Type()
)
hh3cDot11APAssocFailStatis3NSRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3NSRCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis3URCCnt_Type = Counter32
_Hh3cDot11APAssocFailStatis3URCCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis3URCCnt = _Hh3cDot11APAssocFailStatis3URCCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 3),
    _Hh3cDot11APAssocFailStatis3URCCnt_Type()
)
hh3cDot11APAssocFailStatis3URCCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3URCCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis3RFCnt_Type = Counter32
_Hh3cDot11APAssocFailStatis3RFCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis3RFCnt = _Hh3cDot11APAssocFailStatis3RFCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 4),
    _Hh3cDot11APAssocFailStatis3RFCnt_Type()
)
hh3cDot11APAssocFailStatis3RFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3RFCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis3OtherCnt_Type = Counter32
_Hh3cDot11APAssocFailStatis3OtherCnt_Object = MibTableColumn
hh3cDot11APAssocFailStatis3OtherCnt = _Hh3cDot11APAssocFailStatis3OtherCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 5),
    _Hh3cDot11APAssocFailStatis3OtherCnt_Type()
)
hh3cDot11APAssocFailStatis3OtherCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3OtherCnt.setStatus("current")
_Hh3cDot11APAssocFailStatis3RSSILowCntCM_Type = Counter32
_Hh3cDot11APAssocFailStatis3RSSILowCntCM_Object = MibTableColumn
hh3cDot11APAssocFailStatis3RSSILowCntCM = _Hh3cDot11APAssocFailStatis3RSSILowCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 22, 1, 6),
    _Hh3cDot11APAssocFailStatis3RSSILowCntCM_Type()
)
hh3cDot11APAssocFailStatis3RSSILowCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocFailStatis3RSSILowCntCM.setStatus("current")
_Hh3cDot11APIfStatisByAPIDTable_Object = MibTable
hh3cDot11APIfStatisByAPIDTable = _Hh3cDot11APIfStatisByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23)
)
if mibBuilder.loadTexts:
    hh3cDot11APIfStatisByAPIDTable.setStatus("current")
_Hh3cDot11APIfStatisByAPIDEntry_Object = MibTableRow
hh3cDot11APIfStatisByAPIDEntry = _Hh3cDot11APIfStatisByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1)
)
hh3cDot11APIfStatisByAPIDEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIfStatisByAPIDEntry.setStatus("current")
_Hh3cDot11APIfInPkts2_Type = Counter64
_Hh3cDot11APIfInPkts2_Object = MibTableColumn
hh3cDot11APIfInPkts2 = _Hh3cDot11APIfInPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 1),
    _Hh3cDot11APIfInPkts2_Type()
)
hh3cDot11APIfInPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInPkts2.setStatus("current")
_Hh3cDot11APIfInNormalPkts2_Type = Counter64
_Hh3cDot11APIfInNormalPkts2_Object = MibTableColumn
hh3cDot11APIfInNormalPkts2 = _Hh3cDot11APIfInNormalPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 2),
    _Hh3cDot11APIfInNormalPkts2_Type()
)
hh3cDot11APIfInNormalPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInNormalPkts2.setStatus("current")
_Hh3cDot11APIfInErrorPkts2_Type = Counter64
_Hh3cDot11APIfInErrorPkts2_Object = MibTableColumn
hh3cDot11APIfInErrorPkts2 = _Hh3cDot11APIfInErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 3),
    _Hh3cDot11APIfInErrorPkts2_Type()
)
hh3cDot11APIfInErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInErrorPkts2.setStatus("current")
_Hh3cDot11APIfOutPkts2_Type = Counter64
_Hh3cDot11APIfOutPkts2_Object = MibTableColumn
hh3cDot11APIfOutPkts2 = _Hh3cDot11APIfOutPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 4),
    _Hh3cDot11APIfOutPkts2_Type()
)
hh3cDot11APIfOutPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutPkts2.setStatus("current")
_Hh3cDot11APIfInOctets2_Type = Counter64
_Hh3cDot11APIfInOctets2_Object = MibTableColumn
hh3cDot11APIfInOctets2 = _Hh3cDot11APIfInOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 5),
    _Hh3cDot11APIfInOctets2_Type()
)
hh3cDot11APIfInOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInOctets2.setStatus("current")
_Hh3cDot11APIfOutOctets2_Type = Counter64
_Hh3cDot11APIfOutOctets2_Object = MibTableColumn
hh3cDot11APIfOutOctets2 = _Hh3cDot11APIfOutOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 6),
    _Hh3cDot11APIfOutOctets2_Type()
)
hh3cDot11APIfOutOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutOctets2.setStatus("current")
_Hh3cDot11APIfFlowOut2_Type = Unsigned32
_Hh3cDot11APIfFlowOut2_Object = MibTableColumn
hh3cDot11APIfFlowOut2 = _Hh3cDot11APIfFlowOut2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 7),
    _Hh3cDot11APIfFlowOut2_Type()
)
hh3cDot11APIfFlowOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfFlowOut2.setStatus("current")
_Hh3cDot11APIfFlowIN2_Type = Unsigned32
_Hh3cDot11APIfFlowIN2_Object = MibTableColumn
hh3cDot11APIfFlowIN2 = _Hh3cDot11APIfFlowIN2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 8),
    _Hh3cDot11APIfFlowIN2_Type()
)
hh3cDot11APIfFlowIN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfFlowIN2.setStatus("current")
_Hh3cDot11APIfInUcastPkts2_Type = Counter64
_Hh3cDot11APIfInUcastPkts2_Object = MibTableColumn
hh3cDot11APIfInUcastPkts2 = _Hh3cDot11APIfInUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 9),
    _Hh3cDot11APIfInUcastPkts2_Type()
)
hh3cDot11APIfInUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInUcastPkts2.setStatus("current")
_Hh3cDot11APIfInNUcastPkts2_Type = Counter64
_Hh3cDot11APIfInNUcastPkts2_Object = MibTableColumn
hh3cDot11APIfInNUcastPkts2 = _Hh3cDot11APIfInNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 10),
    _Hh3cDot11APIfInNUcastPkts2_Type()
)
hh3cDot11APIfInNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInNUcastPkts2.setStatus("current")
_Hh3cDot11APIfInDiscardPkts2_Type = Counter64
_Hh3cDot11APIfInDiscardPkts2_Object = MibTableColumn
hh3cDot11APIfInDiscardPkts2 = _Hh3cDot11APIfInDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 11),
    _Hh3cDot11APIfInDiscardPkts2_Type()
)
hh3cDot11APIfInDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInDiscardPkts2.setStatus("current")
_Hh3cDot11APIfOutUcastPkts2_Type = Counter64
_Hh3cDot11APIfOutUcastPkts2_Object = MibTableColumn
hh3cDot11APIfOutUcastPkts2 = _Hh3cDot11APIfOutUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 12),
    _Hh3cDot11APIfOutUcastPkts2_Type()
)
hh3cDot11APIfOutUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutUcastPkts2.setStatus("current")
_Hh3cDot11APIfOutNUcastPkts2_Type = Counter64
_Hh3cDot11APIfOutNUcastPkts2_Object = MibTableColumn
hh3cDot11APIfOutNUcastPkts2 = _Hh3cDot11APIfOutNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 13),
    _Hh3cDot11APIfOutNUcastPkts2_Type()
)
hh3cDot11APIfOutNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutNUcastPkts2.setStatus("current")
_Hh3cDot11APIfOutDiscardPkts2_Type = Counter64
_Hh3cDot11APIfOutDiscardPkts2_Object = MibTableColumn
hh3cDot11APIfOutDiscardPkts2 = _Hh3cDot11APIfOutDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 14),
    _Hh3cDot11APIfOutDiscardPkts2_Type()
)
hh3cDot11APIfOutDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutDiscardPkts2.setStatus("current")
_Hh3cDot11APIfOutErrorPkts2_Type = Counter64
_Hh3cDot11APIfOutErrorPkts2_Object = MibTableColumn
hh3cDot11APIfOutErrorPkts2 = _Hh3cDot11APIfOutErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 15),
    _Hh3cDot11APIfOutErrorPkts2_Type()
)
hh3cDot11APIfOutErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutErrorPkts2.setStatus("current")
_Hh3cDot11APIfUpdownTimes2_Type = Counter32
_Hh3cDot11APIfUpdownTimes2_Object = MibTableColumn
hh3cDot11APIfUpdownTimes2 = _Hh3cDot11APIfUpdownTimes2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 16),
    _Hh3cDot11APIfUpdownTimes2_Type()
)
hh3cDot11APIfUpdownTimes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfUpdownTimes2.setStatus("current")
_Hh3cDot11APIfStatusKeepTime2_Type = TimeTicks
_Hh3cDot11APIfStatusKeepTime2_Object = MibTableColumn
hh3cDot11APIfStatusKeepTime2 = _Hh3cDot11APIfStatusKeepTime2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 17),
    _Hh3cDot11APIfStatusKeepTime2_Type()
)
hh3cDot11APIfStatusKeepTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfStatusKeepTime2.setStatus("current")


class _Hh3cDot11APIfOperStatus2_Type(Integer32):
    """Custom type hh3cDot11APIfOperStatus2 based on Integer32"""
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


_Hh3cDot11APIfOperStatus2_Type.__name__ = "Integer32"
_Hh3cDot11APIfOperStatus2_Object = MibTableColumn
hh3cDot11APIfOperStatus2 = _Hh3cDot11APIfOperStatus2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 18),
    _Hh3cDot11APIfOperStatus2_Type()
)
hh3cDot11APIfOperStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOperStatus2.setStatus("current")
_Hh3cDot11APIfInBrdcastPkts2_Type = Counter64
_Hh3cDot11APIfInBrdcastPkts2_Object = MibTableColumn
hh3cDot11APIfInBrdcastPkts2 = _Hh3cDot11APIfInBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 19),
    _Hh3cDot11APIfInBrdcastPkts2_Type()
)
hh3cDot11APIfInBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInBrdcastPkts2.setStatus("current")
_Hh3cDot11APIfOutBrdcastPkts2_Type = Counter64
_Hh3cDot11APIfOutBrdcastPkts2_Object = MibTableColumn
hh3cDot11APIfOutBrdcastPkts2 = _Hh3cDot11APIfOutBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 20),
    _Hh3cDot11APIfOutBrdcastPkts2_Type()
)
hh3cDot11APIfOutBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutBrdcastPkts2.setStatus("current")
_Hh3cDot11APIfInMulcastPkts2_Type = Counter64
_Hh3cDot11APIfInMulcastPkts2_Object = MibTableColumn
hh3cDot11APIfInMulcastPkts2 = _Hh3cDot11APIfInMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 21),
    _Hh3cDot11APIfInMulcastPkts2_Type()
)
hh3cDot11APIfInMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInMulcastPkts2.setStatus("current")
_Hh3cDot11APIfOutMulcastPkts2_Type = Counter64
_Hh3cDot11APIfOutMulcastPkts2_Object = MibTableColumn
hh3cDot11APIfOutMulcastPkts2 = _Hh3cDot11APIfOutMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 22),
    _Hh3cDot11APIfOutMulcastPkts2_Type()
)
hh3cDot11APIfOutMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutMulcastPkts2.setStatus("current")
_Hh3cDot11APIfInPayloadOctets2_Type = Counter64
_Hh3cDot11APIfInPayloadOctets2_Object = MibTableColumn
hh3cDot11APIfInPayloadOctets2 = _Hh3cDot11APIfInPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 23),
    _Hh3cDot11APIfInPayloadOctets2_Type()
)
hh3cDot11APIfInPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInPayloadOctets2.setStatus("current")
_Hh3cDot11APIfOutPayloadOctets2_Type = Counter64
_Hh3cDot11APIfOutPayloadOctets2_Object = MibTableColumn
hh3cDot11APIfOutPayloadOctets2 = _Hh3cDot11APIfOutPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 24),
    _Hh3cDot11APIfOutPayloadOctets2_Type()
)
hh3cDot11APIfOutPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutPayloadOctets2.setStatus("current")
_Hh3cDot11APIfInDataOctets2_Type = Counter64
_Hh3cDot11APIfInDataOctets2_Object = MibTableColumn
hh3cDot11APIfInDataOctets2 = _Hh3cDot11APIfInDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 25),
    _Hh3cDot11APIfInDataOctets2_Type()
)
hh3cDot11APIfInDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfInDataOctets2.setStatus("current")
_Hh3cDot11APIfOutDataOctets2_Type = Counter64
_Hh3cDot11APIfOutDataOctets2_Object = MibTableColumn
hh3cDot11APIfOutDataOctets2 = _Hh3cDot11APIfOutDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 26),
    _Hh3cDot11APIfOutDataOctets2_Type()
)
hh3cDot11APIfOutDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOutDataOctets2.setStatus("current")


class _Hh3cDot11APIfAdminStatus_Type(Integer32):
    """Custom type hh3cDot11APIfAdminStatus based on Integer32"""
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


_Hh3cDot11APIfAdminStatus_Type.__name__ = "Integer32"
_Hh3cDot11APIfAdminStatus_Object = MibTableColumn
hh3cDot11APIfAdminStatus = _Hh3cDot11APIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 27),
    _Hh3cDot11APIfAdminStatus_Type()
)
hh3cDot11APIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APIfAdminStatus.setStatus("current")


class _Hh3cDot11APIfOperStatusCM_Type(Integer32):
    """Custom type hh3cDot11APIfOperStatusCM based on Integer32"""
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


_Hh3cDot11APIfOperStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11APIfOperStatusCM_Object = MibTableColumn
hh3cDot11APIfOperStatusCM = _Hh3cDot11APIfOperStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 23, 1, 28),
    _Hh3cDot11APIfOperStatusCM_Type()
)
hh3cDot11APIfOperStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APIfOperStatusCM.setStatus("current")
_Hh3cDot11APUserSecAuthStatisTable_Object = MibTable
hh3cDot11APUserSecAuthStatisTable = _Hh3cDot11APUserSecAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthStatisTable.setStatus("current")
_Hh3cDot11APUserSecAuthStatisEntry_Object = MibTableRow
hh3cDot11APUserSecAuthStatisEntry = _Hh3cDot11APUserSecAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1)
)
hh3cDot11APUserSecAuthStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthStatisEntry.setStatus("current")
_Hh3cDot11APUserAuthCurNumber_Type = Integer32
_Hh3cDot11APUserAuthCurNumber_Object = MibTableColumn
hh3cDot11APUserAuthCurNumber = _Hh3cDot11APUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 1),
    _Hh3cDot11APUserAuthCurNumber_Type()
)
hh3cDot11APUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthCurNumber.setStatus("current")
_Hh3cDot11APUserConnFailCnt_Type = Counter32
_Hh3cDot11APUserConnFailCnt_Object = MibTableColumn
hh3cDot11APUserConnFailCnt = _Hh3cDot11APUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 2),
    _Hh3cDot11APUserConnFailCnt_Type()
)
hh3cDot11APUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserConnFailCnt.setStatus("current")
_Hh3cDot11APUserAuthReqCnt_Type = Counter32
_Hh3cDot11APUserAuthReqCnt_Object = MibTableColumn
hh3cDot11APUserAuthReqCnt = _Hh3cDot11APUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 3),
    _Hh3cDot11APUserAuthReqCnt_Type()
)
hh3cDot11APUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthReqCnt.setStatus("current")
_Hh3cDot11APUserAuthSuccCnt_Type = Counter32
_Hh3cDot11APUserAuthSuccCnt_Object = MibTableColumn
hh3cDot11APUserAuthSuccCnt = _Hh3cDot11APUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 4),
    _Hh3cDot11APUserAuthSuccCnt_Type()
)
hh3cDot11APUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthSuccCnt.setStatus("current")
_Hh3cDot11APUserAuthFailCnt_Type = Counter32
_Hh3cDot11APUserAuthFailCnt_Object = MibTableColumn
hh3cDot11APUserAuthFailCnt = _Hh3cDot11APUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 5),
    _Hh3cDot11APUserAuthFailCnt_Type()
)
hh3cDot11APUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthFailCnt.setStatus("current")
_Hh3cDot11AllUserOnlineTime_Type = TimeTicks
_Hh3cDot11AllUserOnlineTime_Object = MibTableColumn
hh3cDot11AllUserOnlineTime = _Hh3cDot11AllUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 24, 1, 6),
    _Hh3cDot11AllUserOnlineTime_Type()
)
hh3cDot11AllUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AllUserOnlineTime.setStatus("current")
_Hh3cDot11APUserInfoStatisTable_Object = MibTable
hh3cDot11APUserInfoStatisTable = _Hh3cDot11APUserInfoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserInfoStatisTable.setStatus("current")
_Hh3cDot11APUserInfoStatisEntry_Object = MibTableRow
hh3cDot11APUserInfoStatisEntry = _Hh3cDot11APUserInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1)
)
hh3cDot11APUserInfoStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APUserMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserInfoStatisEntry.setStatus("current")
_Hh3cDot11APUserMacAddr_Type = MacAddress
_Hh3cDot11APUserMacAddr_Object = MibTableColumn
hh3cDot11APUserMacAddr = _Hh3cDot11APUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 1),
    _Hh3cDot11APUserMacAddr_Type()
)
hh3cDot11APUserMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APUserMacAddr.setStatus("current")
_Hh3cDot11APUserIpAddr_Type = IpAddress
_Hh3cDot11APUserIpAddr_Object = MibTableColumn
hh3cDot11APUserIpAddr = _Hh3cDot11APUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 2),
    _Hh3cDot11APUserIpAddr_Type()
)
hh3cDot11APUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserIpAddr.setStatus("current")
_Hh3cDot11APUserLoginName_Type = OctetString
_Hh3cDot11APUserLoginName_Object = MibTableColumn
hh3cDot11APUserLoginName = _Hh3cDot11APUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 3),
    _Hh3cDot11APUserLoginName_Type()
)
hh3cDot11APUserLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserLoginName.setStatus("current")
_Hh3cDot11APUserLoginTime_Type = OctetString
_Hh3cDot11APUserLoginTime_Object = MibTableColumn
hh3cDot11APUserLoginTime = _Hh3cDot11APUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 4),
    _Hh3cDot11APUserLoginTime_Type()
)
hh3cDot11APUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserLoginTime.setStatus("current")
_Hh3cDot11APUserOnlineTime_Type = TimeTicks
_Hh3cDot11APUserOnlineTime_Object = MibTableColumn
hh3cDot11APUserOnlineTime = _Hh3cDot11APUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 5),
    _Hh3cDot11APUserOnlineTime_Type()
)
hh3cDot11APUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserOnlineTime.setStatus("current")
_Hh3cDot11APUserLoginNameCM_Type = OctetString
_Hh3cDot11APUserLoginNameCM_Object = MibTableColumn
hh3cDot11APUserLoginNameCM = _Hh3cDot11APUserLoginNameCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 6),
    _Hh3cDot11APUserLoginNameCM_Type()
)
hh3cDot11APUserLoginNameCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserLoginNameCM.setStatus("current")


class _Hh3cDot11APUserAuthTypeCM_Type(Integer32):
    """Custom type hh3cDot11APUserAuthTypeCM based on Integer32"""
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


_Hh3cDot11APUserAuthTypeCM_Type.__name__ = "Integer32"
_Hh3cDot11APUserAuthTypeCM_Object = MibTableColumn
hh3cDot11APUserAuthTypeCM = _Hh3cDot11APUserAuthTypeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 7),
    _Hh3cDot11APUserAuthTypeCM_Type()
)
hh3cDot11APUserAuthTypeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthTypeCM.setStatus("current")
_Hh3cDot11APUserTxPacketCntCM_Type = Counter32
_Hh3cDot11APUserTxPacketCntCM_Object = MibTableColumn
hh3cDot11APUserTxPacketCntCM = _Hh3cDot11APUserTxPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 8),
    _Hh3cDot11APUserTxPacketCntCM_Type()
)
hh3cDot11APUserTxPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserTxPacketCntCM.setStatus("current")
_Hh3cDot11APUserTxBytesCM_Type = Counter64
_Hh3cDot11APUserTxBytesCM_Object = MibTableColumn
hh3cDot11APUserTxBytesCM = _Hh3cDot11APUserTxBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 9),
    _Hh3cDot11APUserTxBytesCM_Type()
)
hh3cDot11APUserTxBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserTxBytesCM.setStatus("current")
_Hh3cDot11APUserRxPacketCntCM_Type = Counter32
_Hh3cDot11APUserRxPacketCntCM_Object = MibTableColumn
hh3cDot11APUserRxPacketCntCM = _Hh3cDot11APUserRxPacketCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 10),
    _Hh3cDot11APUserRxPacketCntCM_Type()
)
hh3cDot11APUserRxPacketCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserRxPacketCntCM.setStatus("current")
_Hh3cDot11APUserRxBytesCM_Type = Counter64
_Hh3cDot11APUserRxBytesCM_Object = MibTableColumn
hh3cDot11APUserRxBytesCM = _Hh3cDot11APUserRxBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 25, 1, 11),
    _Hh3cDot11APUserRxBytesCM_Type()
)
hh3cDot11APUserRxBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserRxBytesCM.setStatus("current")
_Hh3cDot11APReassocStatis2Table_Object = MibTable
hh3cDot11APReassocStatis2Table = _Hh3cDot11APReassocStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 26)
)
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatis2Table.setStatus("current")
_Hh3cDot11APReassocStatis2Entry_Object = MibTableRow
hh3cDot11APReassocStatis2Entry = _Hh3cDot11APReassocStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 26, 1)
)
hh3cDot11APReassocStatis2Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APReassocStatis2Entry.setStatus("current")
_Hh3cDot11APReassocFailStatis2Cnt_Type = Counter32
_Hh3cDot11APReassocFailStatis2Cnt_Object = MibTableColumn
hh3cDot11APReassocFailStatis2Cnt = _Hh3cDot11APReassocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 26, 1, 1),
    _Hh3cDot11APReassocFailStatis2Cnt_Type()
)
hh3cDot11APReassocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APReassocFailStatis2Cnt.setStatus("current")
_Hh3cDot11TrafficTable_Object = MibTable
hh3cDot11TrafficTable = _Hh3cDot11TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27)
)
if mibBuilder.loadTexts:
    hh3cDot11TrafficTable.setStatus("current")
_Hh3cDot11TrafficEntry_Object = MibTableRow
hh3cDot11TrafficEntry = _Hh3cDot11TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1)
)
hh3cDot11TrafficEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11SSIDIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11TrafficEntry.setStatus("current")
_Hh3cDot11SSIDIndex_Type = OctetString
_Hh3cDot11SSIDIndex_Object = MibTableColumn
hh3cDot11SSIDIndex = _Hh3cDot11SSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1, 1),
    _Hh3cDot11SSIDIndex_Type()
)
hh3cDot11SSIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SSIDIndex.setStatus("current")
_Hh3cDot11UpPacketNumber_Type = Counter64
_Hh3cDot11UpPacketNumber_Object = MibTableColumn
hh3cDot11UpPacketNumber = _Hh3cDot11UpPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1, 2),
    _Hh3cDot11UpPacketNumber_Type()
)
hh3cDot11UpPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11UpPacketNumber.setStatus("current")
_Hh3cDot11UpByteNumber_Type = Counter64
_Hh3cDot11UpByteNumber_Object = MibTableColumn
hh3cDot11UpByteNumber = _Hh3cDot11UpByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1, 3),
    _Hh3cDot11UpByteNumber_Type()
)
hh3cDot11UpByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11UpByteNumber.setStatus("current")
_Hh3cDot11DownPacketNumber_Type = Counter64
_Hh3cDot11DownPacketNumber_Object = MibTableColumn
hh3cDot11DownPacketNumber = _Hh3cDot11DownPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1, 4),
    _Hh3cDot11DownPacketNumber_Type()
)
hh3cDot11DownPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DownPacketNumber.setStatus("current")
_Hh3cDot11DownByteNumber_Type = Counter64
_Hh3cDot11DownByteNumber_Object = MibTableColumn
hh3cDot11DownByteNumber = _Hh3cDot11DownByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 27, 1, 5),
    _Hh3cDot11DownByteNumber_Type()
)
hh3cDot11DownByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DownByteNumber.setStatus("current")
_Hh3cDot11APEchoStatisTable_Object = MibTable
hh3cDot11APEchoStatisTable = _Hh3cDot11APEchoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 28)
)
if mibBuilder.loadTexts:
    hh3cDot11APEchoStatisTable.setStatus("current")
_Hh3cDot11APEchoInfoStatisEntry_Object = MibTableRow
hh3cDot11APEchoInfoStatisEntry = _Hh3cDot11APEchoInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 28, 1)
)
hh3cDot11APEchoInfoStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APEchoInfoStatisEntry.setStatus("current")
_Hh3cDot11APEchoAvgDelay_Type = Integer32
_Hh3cDot11APEchoAvgDelay_Object = MibTableColumn
hh3cDot11APEchoAvgDelay = _Hh3cDot11APEchoAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 28, 1, 1),
    _Hh3cDot11APEchoAvgDelay_Type()
)
hh3cDot11APEchoAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APEchoAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APEchoAvgDelay.setUnits("millisecond")
_Hh3cDot11APEchoRequestCnt_Type = Counter64
_Hh3cDot11APEchoRequestCnt_Object = MibTableColumn
hh3cDot11APEchoRequestCnt = _Hh3cDot11APEchoRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 28, 1, 2),
    _Hh3cDot11APEchoRequestCnt_Type()
)
hh3cDot11APEchoRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APEchoRequestCnt.setStatus("current")
_Hh3cDot11APEchoRespLossCnt_Type = Counter64
_Hh3cDot11APEchoRespLossCnt_Object = MibTableColumn
hh3cDot11APEchoRespLossCnt = _Hh3cDot11APEchoRespLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 28, 1, 3),
    _Hh3cDot11APEchoRespLossCnt_Type()
)
hh3cDot11APEchoRespLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APEchoRespLossCnt.setStatus("current")
_Hh3cDot11APUserSecAuthTypeStatisTable_Object = MibTable
hh3cDot11APUserSecAuthTypeStatisTable = _Hh3cDot11APUserSecAuthTypeStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthTypeStatisTable.setStatus("current")
_Hh3cDot11APUserSecAuthTypeStatisEntry_Object = MibTableRow
hh3cDot11APUserSecAuthTypeStatisEntry = _Hh3cDot11APUserSecAuthTypeStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1)
)
hh3cDot11APUserSecAuthTypeStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthTypeStatisEntry.setStatus("current")
_Hh3cDot11APPortalOnlineUserNum_Type = Integer32
_Hh3cDot11APPortalOnlineUserNum_Object = MibTableColumn
hh3cDot11APPortalOnlineUserNum = _Hh3cDot11APPortalOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 1),
    _Hh3cDot11APPortalOnlineUserNum_Type()
)
hh3cDot11APPortalOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APPortalOnlineUserNum.setStatus("current")
_Hh3cDot11APAuthFreeOnlineUserNum_Type = Integer32
_Hh3cDot11APAuthFreeOnlineUserNum_Object = MibTableColumn
hh3cDot11APAuthFreeOnlineUserNum = _Hh3cDot11APAuthFreeOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 2),
    _Hh3cDot11APAuthFreeOnlineUserNum_Type()
)
hh3cDot11APAuthFreeOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAuthFreeOnlineUserNum.setStatus("current")
_Hh3cDot11APAssocAuthOnlineUserNum_Type = Integer32
_Hh3cDot11APAssocAuthOnlineUserNum_Object = MibTableColumn
hh3cDot11APAssocAuthOnlineUserNum = _Hh3cDot11APAssocAuthOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 3),
    _Hh3cDot11APAssocAuthOnlineUserNum_Type()
)
hh3cDot11APAssocAuthOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocAuthOnlineUserNum.setStatus("current")
_Hh3cDot11APMacAuthOnlineUserNum_Type = Integer32
_Hh3cDot11APMacAuthOnlineUserNum_Object = MibTableColumn
hh3cDot11APMacAuthOnlineUserNum = _Hh3cDot11APMacAuthOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 4),
    _Hh3cDot11APMacAuthOnlineUserNum_Type()
)
hh3cDot11APMacAuthOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAuthOnlineUserNum.setStatus("current")
_Hh3cDot11APAllPortalUserOnlineTime_Type = TimeTicks
_Hh3cDot11APAllPortalUserOnlineTime_Object = MibTableColumn
hh3cDot11APAllPortalUserOnlineTime = _Hh3cDot11APAllPortalUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 5),
    _Hh3cDot11APAllPortalUserOnlineTime_Type()
)
hh3cDot11APAllPortalUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAllPortalUserOnlineTime.setStatus("current")
_Hh3cDot11APAllAuthFreeUserOnlineTime_Type = TimeTicks
_Hh3cDot11APAllAuthFreeUserOnlineTime_Object = MibTableColumn
hh3cDot11APAllAuthFreeUserOnlineTime = _Hh3cDot11APAllAuthFreeUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 6),
    _Hh3cDot11APAllAuthFreeUserOnlineTime_Type()
)
hh3cDot11APAllAuthFreeUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAllAuthFreeUserOnlineTime.setStatus("current")
_Hh3cDot11APAllAssocAuthUserOnlineTime_Type = TimeTicks
_Hh3cDot11APAllAssocAuthUserOnlineTime_Object = MibTableColumn
hh3cDot11APAllAssocAuthUserOnlineTime = _Hh3cDot11APAllAssocAuthUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 7),
    _Hh3cDot11APAllAssocAuthUserOnlineTime_Type()
)
hh3cDot11APAllAssocAuthUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAllAssocAuthUserOnlineTime.setStatus("current")
_Hh3cDot11APAllMacAuthUserOnlineTime_Type = TimeTicks
_Hh3cDot11APAllMacAuthUserOnlineTime_Object = MibTableColumn
hh3cDot11APAllMacAuthUserOnlineTime = _Hh3cDot11APAllMacAuthUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 8),
    _Hh3cDot11APAllMacAuthUserOnlineTime_Type()
)
hh3cDot11APAllMacAuthUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAllMacAuthUserOnlineTime.setStatus("current")
_Hh3cDot11APPortalUserLostCnntCnt_Type = Counter32
_Hh3cDot11APPortalUserLostCnntCnt_Object = MibTableColumn
hh3cDot11APPortalUserLostCnntCnt = _Hh3cDot11APPortalUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 9),
    _Hh3cDot11APPortalUserLostCnntCnt_Type()
)
hh3cDot11APPortalUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APPortalUserLostCnntCnt.setStatus("current")
_Hh3cDot11APAuthFreeUserLostCnntCnt_Type = Counter32
_Hh3cDot11APAuthFreeUserLostCnntCnt_Object = MibTableColumn
hh3cDot11APAuthFreeUserLostCnntCnt = _Hh3cDot11APAuthFreeUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 10),
    _Hh3cDot11APAuthFreeUserLostCnntCnt_Type()
)
hh3cDot11APAuthFreeUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAuthFreeUserLostCnntCnt.setStatus("current")
_Hh3cDot11APAssocAuthUserLostCnntCnt_Type = Counter32
_Hh3cDot11APAssocAuthUserLostCnntCnt_Object = MibTableColumn
hh3cDot11APAssocAuthUserLostCnntCnt = _Hh3cDot11APAssocAuthUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 11),
    _Hh3cDot11APAssocAuthUserLostCnntCnt_Type()
)
hh3cDot11APAssocAuthUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocAuthUserLostCnntCnt.setStatus("current")
_Hh3cDot11APMacAuthUserLostCnntCnt_Type = Counter32
_Hh3cDot11APMacAuthUserLostCnntCnt_Object = MibTableColumn
hh3cDot11APMacAuthUserLostCnntCnt = _Hh3cDot11APMacAuthUserLostCnntCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 12),
    _Hh3cDot11APMacAuthUserLostCnntCnt_Type()
)
hh3cDot11APMacAuthUserLostCnntCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAuthUserLostCnntCnt.setStatus("current")
_Hh3cDot11APPortalAuthReqCnt_Type = Counter32
_Hh3cDot11APPortalAuthReqCnt_Object = MibTableColumn
hh3cDot11APPortalAuthReqCnt = _Hh3cDot11APPortalAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 13),
    _Hh3cDot11APPortalAuthReqCnt_Type()
)
hh3cDot11APPortalAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APPortalAuthReqCnt.setStatus("current")
_Hh3cDot11APAssocAuthReqCnt_Type = Counter32
_Hh3cDot11APAssocAuthReqCnt_Object = MibTableColumn
hh3cDot11APAssocAuthReqCnt = _Hh3cDot11APAssocAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 14),
    _Hh3cDot11APAssocAuthReqCnt_Type()
)
hh3cDot11APAssocAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocAuthReqCnt.setStatus("current")
_Hh3cDot11APMacAuthReqCnt_Type = Counter32
_Hh3cDot11APMacAuthReqCnt_Object = MibTableColumn
hh3cDot11APMacAuthReqCnt = _Hh3cDot11APMacAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 15),
    _Hh3cDot11APMacAuthReqCnt_Type()
)
hh3cDot11APMacAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAuthReqCnt.setStatus("current")
_Hh3cDot11APPortalAuthSucCnt_Type = Counter32
_Hh3cDot11APPortalAuthSucCnt_Object = MibTableColumn
hh3cDot11APPortalAuthSucCnt = _Hh3cDot11APPortalAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 16),
    _Hh3cDot11APPortalAuthSucCnt_Type()
)
hh3cDot11APPortalAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APPortalAuthSucCnt.setStatus("current")
_Hh3cDot11APAssocAuthSucCnt_Type = Counter32
_Hh3cDot11APAssocAuthSucCnt_Object = MibTableColumn
hh3cDot11APAssocAuthSucCnt = _Hh3cDot11APAssocAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 17),
    _Hh3cDot11APAssocAuthSucCnt_Type()
)
hh3cDot11APAssocAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocAuthSucCnt.setStatus("current")
_Hh3cDot11APMacAuthSucCnt_Type = Counter32
_Hh3cDot11APMacAuthSucCnt_Object = MibTableColumn
hh3cDot11APMacAuthSucCnt = _Hh3cDot11APMacAuthSucCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 18),
    _Hh3cDot11APMacAuthSucCnt_Type()
)
hh3cDot11APMacAuthSucCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAuthSucCnt.setStatus("current")
_Hh3cDot11APPortalAuthReqFailCnt_Type = Counter32
_Hh3cDot11APPortalAuthReqFailCnt_Object = MibTableColumn
hh3cDot11APPortalAuthReqFailCnt = _Hh3cDot11APPortalAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 19),
    _Hh3cDot11APPortalAuthReqFailCnt_Type()
)
hh3cDot11APPortalAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APPortalAuthReqFailCnt.setStatus("current")
_Hh3cDot11APAssocAuthReqFailCnt_Type = Counter32
_Hh3cDot11APAssocAuthReqFailCnt_Object = MibTableColumn
hh3cDot11APAssocAuthReqFailCnt = _Hh3cDot11APAssocAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 20),
    _Hh3cDot11APAssocAuthReqFailCnt_Type()
)
hh3cDot11APAssocAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAssocAuthReqFailCnt.setStatus("current")
_Hh3cDot11APMacAuthReqFailCnt_Type = Counter32
_Hh3cDot11APMacAuthReqFailCnt_Object = MibTableColumn
hh3cDot11APMacAuthReqFailCnt = _Hh3cDot11APMacAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 21),
    _Hh3cDot11APMacAuthReqFailCnt_Type()
)
hh3cDot11APMacAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APMacAuthReqFailCnt.setStatus("current")
_Hh3cDot11APAutoAuthOnlineUserNumCM_Type = Integer32
_Hh3cDot11APAutoAuthOnlineUserNumCM_Object = MibTableColumn
hh3cDot11APAutoAuthOnlineUserNumCM = _Hh3cDot11APAutoAuthOnlineUserNumCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 22),
    _Hh3cDot11APAutoAuthOnlineUserNumCM_Type()
)
hh3cDot11APAutoAuthOnlineUserNumCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAutoAuthOnlineUserNumCM.setStatus("current")
_Hh3cDot11APAllAutoAuthUserOnlineTimeCM_Type = TimeTicks
_Hh3cDot11APAllAutoAuthUserOnlineTimeCM_Object = MibTableColumn
hh3cDot11APAllAutoAuthUserOnlineTimeCM = _Hh3cDot11APAllAutoAuthUserOnlineTimeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 23),
    _Hh3cDot11APAllAutoAuthUserOnlineTimeCM_Type()
)
hh3cDot11APAllAutoAuthUserOnlineTimeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAllAutoAuthUserOnlineTimeCM.setStatus("current")
_Hh3cDot11APAutoAuthUserLostCnntCntCM_Type = Counter32
_Hh3cDot11APAutoAuthUserLostCnntCntCM_Object = MibTableColumn
hh3cDot11APAutoAuthUserLostCnntCntCM = _Hh3cDot11APAutoAuthUserLostCnntCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 24),
    _Hh3cDot11APAutoAuthUserLostCnntCntCM_Type()
)
hh3cDot11APAutoAuthUserLostCnntCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAutoAuthUserLostCnntCntCM.setStatus("current")
_Hh3cDot11APAutoAuthReqCntCM_Type = Counter32
_Hh3cDot11APAutoAuthReqCntCM_Object = MibTableColumn
hh3cDot11APAutoAuthReqCntCM = _Hh3cDot11APAutoAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 25),
    _Hh3cDot11APAutoAuthReqCntCM_Type()
)
hh3cDot11APAutoAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAutoAuthReqCntCM.setStatus("current")
_Hh3cDot11APAutoAuthSucCntCM_Type = Counter32
_Hh3cDot11APAutoAuthSucCntCM_Object = MibTableColumn
hh3cDot11APAutoAuthSucCntCM = _Hh3cDot11APAutoAuthSucCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 26),
    _Hh3cDot11APAutoAuthSucCntCM_Type()
)
hh3cDot11APAutoAuthSucCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAutoAuthSucCntCM.setStatus("current")
_Hh3cDot11APAutoAuthReqFailCntCM_Type = Counter32
_Hh3cDot11APAutoAuthReqFailCntCM_Object = MibTableColumn
hh3cDot11APAutoAuthReqFailCntCM = _Hh3cDot11APAutoAuthReqFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 29, 1, 27),
    _Hh3cDot11APAutoAuthReqFailCntCM_Type()
)
hh3cDot11APAutoAuthReqFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APAutoAuthReqFailCntCM.setStatus("current")
_Hh3cDot11RadioRxStatis64Table_Object = MibTable
hh3cDot11RadioRxStatis64Table = _Hh3cDot11RadioRxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioRxStatis64Table.setStatus("current")
_Hh3cDot11RadioRxStatis64Entry_Object = MibTableRow
hh3cDot11RadioRxStatis64Entry = _Hh3cDot11RadioRxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1)
)
hh3cDot11RadioRxStatis64Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioRxStatis64Entry.setStatus("current")
_Hh3cDot11Rx64FrameDupCnt_Type = Counter64
_Hh3cDot11Rx64FrameDupCnt_Object = MibTableColumn
hh3cDot11Rx64FrameDupCnt = _Hh3cDot11Rx64FrameDupCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 1),
    _Hh3cDot11Rx64FrameDupCnt_Type()
)
hh3cDot11Rx64FrameDupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64FrameDupCnt.setStatus("current")
_Hh3cDot11Rx64FrameCnt_Type = Counter64
_Hh3cDot11Rx64FrameCnt_Object = MibTableColumn
hh3cDot11Rx64FrameCnt = _Hh3cDot11Rx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 2),
    _Hh3cDot11Rx64FrameCnt_Type()
)
hh3cDot11Rx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64FrameCnt.setStatus("current")
_Hh3cDot11Rx64UcastFrameCnt_Type = Counter64
_Hh3cDot11Rx64UcastFrameCnt_Object = MibTableColumn
hh3cDot11Rx64UcastFrameCnt = _Hh3cDot11Rx64UcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 3),
    _Hh3cDot11Rx64UcastFrameCnt_Type()
)
hh3cDot11Rx64UcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64UcastFrameCnt.setStatus("current")
_Hh3cDot11Rx64BcastFrameCnt_Type = Counter64
_Hh3cDot11Rx64BcastFrameCnt_Object = MibTableColumn
hh3cDot11Rx64BcastFrameCnt = _Hh3cDot11Rx64BcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 4),
    _Hh3cDot11Rx64BcastFrameCnt_Type()
)
hh3cDot11Rx64BcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64BcastFrameCnt.setStatus("current")
_Hh3cDot11Rx64McastFrameCnt_Type = Counter64
_Hh3cDot11Rx64McastFrameCnt_Object = MibTableColumn
hh3cDot11Rx64McastFrameCnt = _Hh3cDot11Rx64McastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 5),
    _Hh3cDot11Rx64McastFrameCnt_Type()
)
hh3cDot11Rx64McastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64McastFrameCnt.setStatus("current")
_Hh3cDot11Rx64DiscardFrameCnt_Type = Counter64
_Hh3cDot11Rx64DiscardFrameCnt_Object = MibTableColumn
hh3cDot11Rx64DiscardFrameCnt = _Hh3cDot11Rx64DiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 6),
    _Hh3cDot11Rx64DiscardFrameCnt_Type()
)
hh3cDot11Rx64DiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DiscardFrameCnt.setStatus("current")
_Hh3cDot11Rx64FragCnt_Type = Counter64
_Hh3cDot11Rx64FragCnt_Object = MibTableColumn
hh3cDot11Rx64FragCnt = _Hh3cDot11Rx64FragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 7),
    _Hh3cDot11Rx64FragCnt_Type()
)
hh3cDot11Rx64FragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64FragCnt.setStatus("current")
_Hh3cDot11Rx64FcsErrCnt_Type = Counter64
_Hh3cDot11Rx64FcsErrCnt_Object = MibTableColumn
hh3cDot11Rx64FcsErrCnt = _Hh3cDot11Rx64FcsErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 8),
    _Hh3cDot11Rx64FcsErrCnt_Type()
)
hh3cDot11Rx64FcsErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64FcsErrCnt.setStatus("current")
_Hh3cDot11Rx64FrameBytes_Type = Counter64
_Hh3cDot11Rx64FrameBytes_Object = MibTableColumn
hh3cDot11Rx64FrameBytes = _Hh3cDot11Rx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 9),
    _Hh3cDot11Rx64FrameBytes_Type()
)
hh3cDot11Rx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64FrameBytes.setStatus("current")
_Hh3cDot11Rx64UcastFrameBytes_Type = Counter64
_Hh3cDot11Rx64UcastFrameBytes_Object = MibTableColumn
hh3cDot11Rx64UcastFrameBytes = _Hh3cDot11Rx64UcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 10),
    _Hh3cDot11Rx64UcastFrameBytes_Type()
)
hh3cDot11Rx64UcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64UcastFrameBytes.setStatus("current")
_Hh3cDot11Rx64BcastFrameBytes_Type = Counter64
_Hh3cDot11Rx64BcastFrameBytes_Object = MibTableColumn
hh3cDot11Rx64BcastFrameBytes = _Hh3cDot11Rx64BcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 11),
    _Hh3cDot11Rx64BcastFrameBytes_Type()
)
hh3cDot11Rx64BcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64BcastFrameBytes.setStatus("current")
_Hh3cDot11Rx64McastFrameBytes_Type = Counter64
_Hh3cDot11Rx64McastFrameBytes_Object = MibTableColumn
hh3cDot11Rx64McastFrameBytes = _Hh3cDot11Rx64McastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 12),
    _Hh3cDot11Rx64McastFrameBytes_Type()
)
hh3cDot11Rx64McastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64McastFrameBytes.setStatus("current")
_Hh3cDot11Rx64DiscardFrameBytes_Type = Counter64
_Hh3cDot11Rx64DiscardFrameBytes_Object = MibTableColumn
hh3cDot11Rx64DiscardFrameBytes = _Hh3cDot11Rx64DiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 13),
    _Hh3cDot11Rx64DiscardFrameBytes_Type()
)
hh3cDot11Rx64DiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DiscardFrameBytes.setStatus("current")
_Hh3cDot11Rx64MgmtFrameCnt_Type = Counter64
_Hh3cDot11Rx64MgmtFrameCnt_Object = MibTableColumn
hh3cDot11Rx64MgmtFrameCnt = _Hh3cDot11Rx64MgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 14),
    _Hh3cDot11Rx64MgmtFrameCnt_Type()
)
hh3cDot11Rx64MgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64MgmtFrameCnt.setStatus("current")
_Hh3cDot11Rx64CtrlFrameCnt_Type = Counter64
_Hh3cDot11Rx64CtrlFrameCnt_Object = MibTableColumn
hh3cDot11Rx64CtrlFrameCnt = _Hh3cDot11Rx64CtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 15),
    _Hh3cDot11Rx64CtrlFrameCnt_Type()
)
hh3cDot11Rx64CtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64CtrlFrameCnt.setStatus("current")
_Hh3cDot11Rx64DataFrameCnt_Type = Counter64
_Hh3cDot11Rx64DataFrameCnt_Object = MibTableColumn
hh3cDot11Rx64DataFrameCnt = _Hh3cDot11Rx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 16),
    _Hh3cDot11Rx64DataFrameCnt_Type()
)
hh3cDot11Rx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DataFrameCnt.setStatus("current")
_Hh3cDot11Rx64DecryptErrorCnt_Type = Counter64
_Hh3cDot11Rx64DecryptErrorCnt_Object = MibTableColumn
hh3cDot11Rx64DecryptErrorCnt = _Hh3cDot11Rx64DecryptErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 17),
    _Hh3cDot11Rx64DecryptErrorCnt_Type()
)
hh3cDot11Rx64DecryptErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DecryptErrorCnt.setStatus("current")
_Hh3cDot11Rx64AuthenFrameCnt_Type = Counter64
_Hh3cDot11Rx64AuthenFrameCnt_Object = MibTableColumn
hh3cDot11Rx64AuthenFrameCnt = _Hh3cDot11Rx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 18),
    _Hh3cDot11Rx64AuthenFrameCnt_Type()
)
hh3cDot11Rx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64AuthenFrameCnt.setStatus("current")
_Hh3cDot11Rx64AssociateFrameCnt_Type = Counter64
_Hh3cDot11Rx64AssociateFrameCnt_Object = MibTableColumn
hh3cDot11Rx64AssociateFrameCnt = _Hh3cDot11Rx64AssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 19),
    _Hh3cDot11Rx64AssociateFrameCnt_Type()
)
hh3cDot11Rx64AssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64AssociateFrameCnt.setStatus("current")
_Hh3cDot11Rx64PhyErrorCnt_Type = Counter64
_Hh3cDot11Rx64PhyErrorCnt_Object = MibTableColumn
hh3cDot11Rx64PhyErrorCnt = _Hh3cDot11Rx64PhyErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 20),
    _Hh3cDot11Rx64PhyErrorCnt_Type()
)
hh3cDot11Rx64PhyErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64PhyErrorCnt.setStatus("current")
_Hh3cDot11Rx64MICErrorCnt_Type = Counter64
_Hh3cDot11Rx64MICErrorCnt_Object = MibTableColumn
hh3cDot11Rx64MICErrorCnt = _Hh3cDot11Rx64MICErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 21),
    _Hh3cDot11Rx64MICErrorCnt_Type()
)
hh3cDot11Rx64MICErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64MICErrorCnt.setStatus("current")
_Hh3cDot11Rx64DataFrameBytes_Type = Counter64
_Hh3cDot11Rx64DataFrameBytes_Object = MibTableColumn
hh3cDot11Rx64DataFrameBytes = _Hh3cDot11Rx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 22),
    _Hh3cDot11Rx64DataFrameBytes_Type()
)
hh3cDot11Rx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DataFrameBytes.setStatus("current")
_Hh3cDot11Rx64PayloadBytes_Type = Counter64
_Hh3cDot11Rx64PayloadBytes_Object = MibTableColumn
hh3cDot11Rx64PayloadBytes = _Hh3cDot11Rx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 23),
    _Hh3cDot11Rx64PayloadBytes_Type()
)
hh3cDot11Rx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64PayloadBytes.setStatus("current")
_Hh3cDot11Rx64DataFrameBytesCM_Type = Counter64
_Hh3cDot11Rx64DataFrameBytesCM_Object = MibTableColumn
hh3cDot11Rx64DataFrameBytesCM = _Hh3cDot11Rx64DataFrameBytesCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 30, 1, 24),
    _Hh3cDot11Rx64DataFrameBytesCM_Type()
)
hh3cDot11Rx64DataFrameBytesCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Rx64DataFrameBytesCM.setStatus("current")
_Hh3cDot11RadioTxStatis64Table_Object = MibTable
hh3cDot11RadioTxStatis64Table = _Hh3cDot11RadioTxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioTxStatis64Table.setStatus("current")
_Hh3cDot11RadioTxStatis64Entry_Object = MibTableRow
hh3cDot11RadioTxStatis64Entry = _Hh3cDot11RadioTxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1)
)
hh3cDot11RadioTxStatis64Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioTxStatis64Entry.setStatus("current")
_Hh3cDot11Tx64FragCnt_Type = Counter64
_Hh3cDot11Tx64FragCnt_Object = MibTableColumn
hh3cDot11Tx64FragCnt = _Hh3cDot11Tx64FragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 1),
    _Hh3cDot11Tx64FragCnt_Type()
)
hh3cDot11Tx64FragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64FragCnt.setStatus("current")
_Hh3cDot11Tx64FailedCnt_Type = Counter64
_Hh3cDot11Tx64FailedCnt_Object = MibTableColumn
hh3cDot11Tx64FailedCnt = _Hh3cDot11Tx64FailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 2),
    _Hh3cDot11Tx64FailedCnt_Type()
)
hh3cDot11Tx64FailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64FailedCnt.setStatus("current")
_Hh3cDot11Tx64RetryCnt_Type = Counter64
_Hh3cDot11Tx64RetryCnt_Object = MibTableColumn
hh3cDot11Tx64RetryCnt = _Hh3cDot11Tx64RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 3),
    _Hh3cDot11Tx64RetryCnt_Type()
)
hh3cDot11Tx64RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64RetryCnt.setStatus("current")
_Hh3cDot11Tx64MultiRetryCnt_Type = Counter64
_Hh3cDot11Tx64MultiRetryCnt_Object = MibTableColumn
hh3cDot11Tx64MultiRetryCnt = _Hh3cDot11Tx64MultiRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 4),
    _Hh3cDot11Tx64MultiRetryCnt_Type()
)
hh3cDot11Tx64MultiRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64MultiRetryCnt.setStatus("current")
_Hh3cDot11Tx64RtsSuccessCnt_Type = Counter64
_Hh3cDot11Tx64RtsSuccessCnt_Object = MibTableColumn
hh3cDot11Tx64RtsSuccessCnt = _Hh3cDot11Tx64RtsSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 5),
    _Hh3cDot11Tx64RtsSuccessCnt_Type()
)
hh3cDot11Tx64RtsSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64RtsSuccessCnt.setStatus("current")
_Hh3cDot11Tx64RtsFailCnt_Type = Counter64
_Hh3cDot11Tx64RtsFailCnt_Object = MibTableColumn
hh3cDot11Tx64RtsFailCnt = _Hh3cDot11Tx64RtsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 6),
    _Hh3cDot11Tx64RtsFailCnt_Type()
)
hh3cDot11Tx64RtsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64RtsFailCnt.setStatus("current")
_Hh3cDot11Tx64AckFailCnt_Type = Counter64
_Hh3cDot11Tx64AckFailCnt_Object = MibTableColumn
hh3cDot11Tx64AckFailCnt = _Hh3cDot11Tx64AckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 7),
    _Hh3cDot11Tx64AckFailCnt_Type()
)
hh3cDot11Tx64AckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64AckFailCnt.setStatus("current")
_Hh3cDot11Tx64FrameCnt_Type = Counter64
_Hh3cDot11Tx64FrameCnt_Object = MibTableColumn
hh3cDot11Tx64FrameCnt = _Hh3cDot11Tx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 8),
    _Hh3cDot11Tx64FrameCnt_Type()
)
hh3cDot11Tx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64FrameCnt.setStatus("current")
_Hh3cDot11Tx64UcastFrameCnt_Type = Counter64
_Hh3cDot11Tx64UcastFrameCnt_Object = MibTableColumn
hh3cDot11Tx64UcastFrameCnt = _Hh3cDot11Tx64UcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 9),
    _Hh3cDot11Tx64UcastFrameCnt_Type()
)
hh3cDot11Tx64UcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64UcastFrameCnt.setStatus("current")
_Hh3cDot11Tx64BcastFrameCnt_Type = Counter64
_Hh3cDot11Tx64BcastFrameCnt_Object = MibTableColumn
hh3cDot11Tx64BcastFrameCnt = _Hh3cDot11Tx64BcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 10),
    _Hh3cDot11Tx64BcastFrameCnt_Type()
)
hh3cDot11Tx64BcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64BcastFrameCnt.setStatus("current")
_Hh3cDot11Tx64McastFrameCnt_Type = Counter64
_Hh3cDot11Tx64McastFrameCnt_Object = MibTableColumn
hh3cDot11Tx64McastFrameCnt = _Hh3cDot11Tx64McastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 11),
    _Hh3cDot11Tx64McastFrameCnt_Type()
)
hh3cDot11Tx64McastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64McastFrameCnt.setStatus("current")
_Hh3cDot11Tx64DiscardFrameCnt_Type = Counter64
_Hh3cDot11Tx64DiscardFrameCnt_Object = MibTableColumn
hh3cDot11Tx64DiscardFrameCnt = _Hh3cDot11Tx64DiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 12),
    _Hh3cDot11Tx64DiscardFrameCnt_Type()
)
hh3cDot11Tx64DiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64DiscardFrameCnt.setStatus("current")
_Hh3cDot11Tx64FrameBytes_Type = Counter64
_Hh3cDot11Tx64FrameBytes_Object = MibTableColumn
hh3cDot11Tx64FrameBytes = _Hh3cDot11Tx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 13),
    _Hh3cDot11Tx64FrameBytes_Type()
)
hh3cDot11Tx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64FrameBytes.setStatus("current")
_Hh3cDot11Tx64UcastFrameBytes_Type = Counter64
_Hh3cDot11Tx64UcastFrameBytes_Object = MibTableColumn
hh3cDot11Tx64UcastFrameBytes = _Hh3cDot11Tx64UcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 14),
    _Hh3cDot11Tx64UcastFrameBytes_Type()
)
hh3cDot11Tx64UcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64UcastFrameBytes.setStatus("current")
_Hh3cDot11Tx64BcastFrameBytes_Type = Counter64
_Hh3cDot11Tx64BcastFrameBytes_Object = MibTableColumn
hh3cDot11Tx64BcastFrameBytes = _Hh3cDot11Tx64BcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 15),
    _Hh3cDot11Tx64BcastFrameBytes_Type()
)
hh3cDot11Tx64BcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64BcastFrameBytes.setStatus("current")
_Hh3cDot11Tx64McastFrameBytes_Type = Counter64
_Hh3cDot11Tx64McastFrameBytes_Object = MibTableColumn
hh3cDot11Tx64McastFrameBytes = _Hh3cDot11Tx64McastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 16),
    _Hh3cDot11Tx64McastFrameBytes_Type()
)
hh3cDot11Tx64McastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64McastFrameBytes.setStatus("current")
_Hh3cDot11Tx64DiscardFrameBytes_Type = Counter64
_Hh3cDot11Tx64DiscardFrameBytes_Object = MibTableColumn
hh3cDot11Tx64DiscardFrameBytes = _Hh3cDot11Tx64DiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 17),
    _Hh3cDot11Tx64DiscardFrameBytes_Type()
)
hh3cDot11Tx64DiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64DiscardFrameBytes.setStatus("current")
_Hh3cDot11Tx64AuthenFrameCnt_Type = Counter64
_Hh3cDot11Tx64AuthenFrameCnt_Object = MibTableColumn
hh3cDot11Tx64AuthenFrameCnt = _Hh3cDot11Tx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 18),
    _Hh3cDot11Tx64AuthenFrameCnt_Type()
)
hh3cDot11Tx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64AuthenFrameCnt.setStatus("current")
_Hh3cDot11Tx64AssociateFrameCnt_Type = Counter64
_Hh3cDot11Tx64AssociateFrameCnt_Object = MibTableColumn
hh3cDot11Tx64AssociateFrameCnt = _Hh3cDot11Tx64AssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 19),
    _Hh3cDot11Tx64AssociateFrameCnt_Type()
)
hh3cDot11Tx64AssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64AssociateFrameCnt.setStatus("current")
_Hh3cDot11Tx64DataFrameCnt_Type = Counter64
_Hh3cDot11Tx64DataFrameCnt_Object = MibTableColumn
hh3cDot11Tx64DataFrameCnt = _Hh3cDot11Tx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 20),
    _Hh3cDot11Tx64DataFrameCnt_Type()
)
hh3cDot11Tx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64DataFrameCnt.setStatus("current")
_Hh3cDot11Tx64DataFrameBytes_Type = Counter64
_Hh3cDot11Tx64DataFrameBytes_Object = MibTableColumn
hh3cDot11Tx64DataFrameBytes = _Hh3cDot11Tx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 21),
    _Hh3cDot11Tx64DataFrameBytes_Type()
)
hh3cDot11Tx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64DataFrameBytes.setStatus("current")
_Hh3cDot11Tx64MSDUCnt_Type = Counter64
_Hh3cDot11Tx64MSDUCnt_Object = MibTableColumn
hh3cDot11Tx64MSDUCnt = _Hh3cDot11Tx64MSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 22),
    _Hh3cDot11Tx64MSDUCnt_Type()
)
hh3cDot11Tx64MSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64MSDUCnt.setStatus("current")
_Hh3cDot11Tx64DiscardMSDUCnt_Type = Counter64
_Hh3cDot11Tx64DiscardMSDUCnt_Object = MibTableColumn
hh3cDot11Tx64DiscardMSDUCnt = _Hh3cDot11Tx64DiscardMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 23),
    _Hh3cDot11Tx64DiscardMSDUCnt_Type()
)
hh3cDot11Tx64DiscardMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64DiscardMSDUCnt.setStatus("current")
_Hh3cDot11Tx64RetryMSDUCnt_Type = Counter64
_Hh3cDot11Tx64RetryMSDUCnt_Object = MibTableColumn
hh3cDot11Tx64RetryMSDUCnt = _Hh3cDot11Tx64RetryMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 24),
    _Hh3cDot11Tx64RetryMSDUCnt_Type()
)
hh3cDot11Tx64RetryMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64RetryMSDUCnt.setStatus("current")
_Hh3cDot11Tx64PayloadBytes_Type = Counter64
_Hh3cDot11Tx64PayloadBytes_Object = MibTableColumn
hh3cDot11Tx64PayloadBytes = _Hh3cDot11Tx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 25),
    _Hh3cDot11Tx64PayloadBytes_Type()
)
hh3cDot11Tx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64PayloadBytes.setStatus("current")
_Hh3cDot11Tx64MgtFrameCnt_Type = Counter64
_Hh3cDot11Tx64MgtFrameCnt_Object = MibTableColumn
hh3cDot11Tx64MgtFrameCnt = _Hh3cDot11Tx64MgtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 26),
    _Hh3cDot11Tx64MgtFrameCnt_Type()
)
hh3cDot11Tx64MgtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64MgtFrameCnt.setStatus("current")
_Hh3cDot11Tx64CtrlFrameCnt_Type = Counter64
_Hh3cDot11Tx64CtrlFrameCnt_Object = MibTableColumn
hh3cDot11Tx64CtrlFrameCnt = _Hh3cDot11Tx64CtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 27),
    _Hh3cDot11Tx64CtrlFrameCnt_Type()
)
hh3cDot11Tx64CtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64CtrlFrameCnt.setStatus("current")
_Hh3cDot11Tx64MACErrCnt_Type = Counter64
_Hh3cDot11Tx64MACErrCnt_Object = MibTableColumn
hh3cDot11Tx64MACErrCnt = _Hh3cDot11Tx64MACErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 28),
    _Hh3cDot11Tx64MACErrCnt_Type()
)
hh3cDot11Tx64MACErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64MACErrCnt.setStatus("current")
_Hh3cDot11Tx64ErrFrameCnt_Type = Counter64
_Hh3cDot11Tx64ErrFrameCnt_Object = MibTableColumn
hh3cDot11Tx64ErrFrameCnt = _Hh3cDot11Tx64ErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 31, 1, 29),
    _Hh3cDot11Tx64ErrFrameCnt_Type()
)
hh3cDot11Tx64ErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11Tx64ErrFrameCnt.setStatus("current")
_Hh3cDot11BSSRxStatis64Table_Object = MibTable
hh3cDot11BSSRxStatis64Table = _Hh3cDot11BSSRxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32)
)
if mibBuilder.loadTexts:
    hh3cDot11BSSRxStatis64Table.setStatus("current")
_Hh3cDot11BSSRxStatis64Entry_Object = MibTableRow
hh3cDot11BSSRxStatis64Entry = _Hh3cDot11BSSRxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1)
)
hh3cDot11BSSRxStatis64Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11BSSRxStatis64Entry.setStatus("current")
_Hh3cDot11BSSRx64FrameCnt_Type = Counter64
_Hh3cDot11BSSRx64FrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64FrameCnt = _Hh3cDot11BSSRx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 1),
    _Hh3cDot11BSSRx64FrameCnt_Type()
)
hh3cDot11BSSRx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64FrameCnt.setStatus("current")
_Hh3cDot11BSSRx64FrameBytes_Type = Counter64
_Hh3cDot11BSSRx64FrameBytes_Object = MibTableColumn
hh3cDot11BSSRx64FrameBytes = _Hh3cDot11BSSRx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 2),
    _Hh3cDot11BSSRx64FrameBytes_Type()
)
hh3cDot11BSSRx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64FrameBytes.setStatus("current")
_Hh3cDot11BSSRx64DataFrameCnt_Type = Counter64
_Hh3cDot11BSSRx64DataFrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64DataFrameCnt = _Hh3cDot11BSSRx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 3),
    _Hh3cDot11BSSRx64DataFrameCnt_Type()
)
hh3cDot11BSSRx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64DataFrameCnt.setStatus("current")
_Hh3cDot11BSSRx64DataFrameBytes_Type = Counter64
_Hh3cDot11BSSRx64DataFrameBytes_Object = MibTableColumn
hh3cDot11BSSRx64DataFrameBytes = _Hh3cDot11BSSRx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 4),
    _Hh3cDot11BSSRx64DataFrameBytes_Type()
)
hh3cDot11BSSRx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64DataFrameBytes.setStatus("current")
_Hh3cDot11BSSRx64AssocFrameCnt_Type = Counter64
_Hh3cDot11BSSRx64AssocFrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64AssocFrameCnt = _Hh3cDot11BSSRx64AssocFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 5),
    _Hh3cDot11BSSRx64AssocFrameCnt_Type()
)
hh3cDot11BSSRx64AssocFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64AssocFrameCnt.setStatus("current")
_Hh3cDot11BSSRx64PayloadBytes_Type = Counter64
_Hh3cDot11BSSRx64PayloadBytes_Object = MibTableColumn
hh3cDot11BSSRx64PayloadBytes = _Hh3cDot11BSSRx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 6),
    _Hh3cDot11BSSRx64PayloadBytes_Type()
)
hh3cDot11BSSRx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64PayloadBytes.setStatus("current")
_Hh3cDot11BSSRx64UniFrameCnt_Type = Counter64
_Hh3cDot11BSSRx64UniFrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64UniFrameCnt = _Hh3cDot11BSSRx64UniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 7),
    _Hh3cDot11BSSRx64UniFrameCnt_Type()
)
hh3cDot11BSSRx64UniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64UniFrameCnt.setStatus("current")
_Hh3cDot11BSSRx64NonUniFrameCnt_Type = Counter64
_Hh3cDot11BSSRx64NonUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64NonUniFrameCnt = _Hh3cDot11BSSRx64NonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 8),
    _Hh3cDot11BSSRx64NonUniFrameCnt_Type()
)
hh3cDot11BSSRx64NonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64NonUniFrameCnt.setStatus("current")
_Hh3cDot11BSSRx64AuthenFrameCnt_Type = Counter64
_Hh3cDot11BSSRx64AuthenFrameCnt_Object = MibTableColumn
hh3cDot11BSSRx64AuthenFrameCnt = _Hh3cDot11BSSRx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 32, 1, 9),
    _Hh3cDot11BSSRx64AuthenFrameCnt_Type()
)
hh3cDot11BSSRx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSRx64AuthenFrameCnt.setStatus("current")
_Hh3cDot11BSSTxStatis64Table_Object = MibTable
hh3cDot11BSSTxStatis64Table = _Hh3cDot11BSSTxStatis64Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33)
)
if mibBuilder.loadTexts:
    hh3cDot11BSSTxStatis64Table.setStatus("current")
_Hh3cDot11BSSTxStatis64Entry_Object = MibTableRow
hh3cDot11BSSTxStatis64Entry = _Hh3cDot11BSSTxStatis64Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1)
)
hh3cDot11BSSTxStatis64Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11BSSTxStatis64Entry.setStatus("current")
_Hh3cDot11BSSTx64FrameCnt_Type = Counter64
_Hh3cDot11BSSTx64FrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64FrameCnt = _Hh3cDot11BSSTx64FrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 1),
    _Hh3cDot11BSSTx64FrameCnt_Type()
)
hh3cDot11BSSTx64FrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64FrameCnt.setStatus("current")
_Hh3cDot11BSSTx64FrameBytes_Type = Counter64
_Hh3cDot11BSSTx64FrameBytes_Object = MibTableColumn
hh3cDot11BSSTx64FrameBytes = _Hh3cDot11BSSTx64FrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 2),
    _Hh3cDot11BSSTx64FrameBytes_Type()
)
hh3cDot11BSSTx64FrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64FrameBytes.setStatus("current")
_Hh3cDot11BSSTx64DataFrameCnt_Type = Counter64
_Hh3cDot11BSSTx64DataFrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64DataFrameCnt = _Hh3cDot11BSSTx64DataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 3),
    _Hh3cDot11BSSTx64DataFrameCnt_Type()
)
hh3cDot11BSSTx64DataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64DataFrameCnt.setStatus("current")
_Hh3cDot11BSSTx64DataFrameBytes_Type = Counter64
_Hh3cDot11BSSTx64DataFrameBytes_Object = MibTableColumn
hh3cDot11BSSTx64DataFrameBytes = _Hh3cDot11BSSTx64DataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 4),
    _Hh3cDot11BSSTx64DataFrameBytes_Type()
)
hh3cDot11BSSTx64DataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64DataFrameBytes.setStatus("current")
_Hh3cDot11BSSTx64AssocFrameCnt_Type = Counter64
_Hh3cDot11BSSTx64AssocFrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64AssocFrameCnt = _Hh3cDot11BSSTx64AssocFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 5),
    _Hh3cDot11BSSTx64AssocFrameCnt_Type()
)
hh3cDot11BSSTx64AssocFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64AssocFrameCnt.setStatus("current")
_Hh3cDot11BSSTx64PayloadBytes_Type = Counter64
_Hh3cDot11BSSTx64PayloadBytes_Object = MibTableColumn
hh3cDot11BSSTx64PayloadBytes = _Hh3cDot11BSSTx64PayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 6),
    _Hh3cDot11BSSTx64PayloadBytes_Type()
)
hh3cDot11BSSTx64PayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64PayloadBytes.setStatus("current")
_Hh3cDot11BSSTx64RetryCnt_Type = Counter64
_Hh3cDot11BSSTx64RetryCnt_Object = MibTableColumn
hh3cDot11BSSTx64RetryCnt = _Hh3cDot11BSSTx64RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 7),
    _Hh3cDot11BSSTx64RetryCnt_Type()
)
hh3cDot11BSSTx64RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64RetryCnt.setStatus("current")
_Hh3cDot11BSSTx64UniFrameCnt_Type = Counter64
_Hh3cDot11BSSTx64UniFrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64UniFrameCnt = _Hh3cDot11BSSTx64UniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 8),
    _Hh3cDot11BSSTx64UniFrameCnt_Type()
)
hh3cDot11BSSTx64UniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64UniFrameCnt.setStatus("current")
_Hh3cDot11BSSTx64NonUniFrameCnt_Type = Counter64
_Hh3cDot11BSSTx64NonUniFrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64NonUniFrameCnt = _Hh3cDot11BSSTx64NonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 9),
    _Hh3cDot11BSSTx64NonUniFrameCnt_Type()
)
hh3cDot11BSSTx64NonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64NonUniFrameCnt.setStatus("current")
_Hh3cDot11BSSTx64AuthenFrameCnt_Type = Counter64
_Hh3cDot11BSSTx64AuthenFrameCnt_Object = MibTableColumn
hh3cDot11BSSTx64AuthenFrameCnt = _Hh3cDot11BSSTx64AuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 33, 1, 10),
    _Hh3cDot11BSSTx64AuthenFrameCnt_Type()
)
hh3cDot11BSSTx64AuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BSSTx64AuthenFrameCnt.setStatus("current")
_Hh3cDot11APPacketMCSRateStatis2Table_Object = MibTable
hh3cDot11APPacketMCSRateStatis2Table = _Hh3cDot11APPacketMCSRateStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 34)
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCSRateStatis2Table.setStatus("current")
_Hh3cDot11APPacketMCSRateStatis2Entry_Object = MibTableRow
hh3cDot11APPacketMCSRateStatis2Entry = _Hh3cDot11APPacketMCSRateStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 34, 1)
)
hh3cDot11APPacketMCSRateStatis2Entry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APPacketMCS2Rate"),
)
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCSRateStatis2Entry.setStatus("current")


class _Hh3cDot11APPacketMCS2Rate_Type(Integer32):
    """Custom type hh3cDot11APPacketMCS2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_Hh3cDot11APPacketMCS2Rate_Type.__name__ = "Integer32"
_Hh3cDot11APPacketMCS2Rate_Object = MibTableColumn
hh3cDot11APPacketMCS2Rate = _Hh3cDot11APPacketMCS2Rate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 34, 1, 1),
    _Hh3cDot11APPacketMCS2Rate_Type()
)
hh3cDot11APPacketMCS2Rate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APPacketMCS2Rate.setStatus("current")
_Hh3cDot11APRXPacketMCSRate2Count_Type = Counter64
_Hh3cDot11APRXPacketMCSRate2Count_Object = MibTableColumn
hh3cDot11APRXPacketMCSRate2Count = _Hh3cDot11APRXPacketMCSRate2Count_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 34, 1, 2),
    _Hh3cDot11APRXPacketMCSRate2Count_Type()
)
hh3cDot11APRXPacketMCSRate2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APRXPacketMCSRate2Count.setStatus("current")
_Hh3cDot11APTXPacketMCSRate2Count_Type = Counter64
_Hh3cDot11APTXPacketMCSRate2Count_Object = MibTableColumn
hh3cDot11APTXPacketMCSRate2Count = _Hh3cDot11APTXPacketMCSRate2Count_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 34, 1, 3),
    _Hh3cDot11APTXPacketMCSRate2Count_Type()
)
hh3cDot11APTXPacketMCSRate2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APTXPacketMCSRate2Count.setStatus("current")
_Hh3cDot11APUserSecAuthStatisCMTable_Object = MibTable
hh3cDot11APUserSecAuthStatisCMTable = _Hh3cDot11APUserSecAuthStatisCMTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthStatisCMTable.setStatus("current")
_Hh3cDot11APUserSecAuthStatisCMEntry_Object = MibTableRow
hh3cDot11APUserSecAuthStatisCMEntry = _Hh3cDot11APUserSecAuthStatisCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1)
)
hh3cDot11APUserSecAuthStatisCMEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserSecAuthStatisCMEntry.setStatus("current")
_Hh3cDot11APUserConnFailCntCM_Type = Counter32
_Hh3cDot11APUserConnFailCntCM_Object = MibTableColumn
hh3cDot11APUserConnFailCntCM = _Hh3cDot11APUserConnFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1, 1),
    _Hh3cDot11APUserConnFailCntCM_Type()
)
hh3cDot11APUserConnFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserConnFailCntCM.setStatus("current")
_Hh3cDot11APUserAuthReqCntCM_Type = Counter32
_Hh3cDot11APUserAuthReqCntCM_Object = MibTableColumn
hh3cDot11APUserAuthReqCntCM = _Hh3cDot11APUserAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1, 2),
    _Hh3cDot11APUserAuthReqCntCM_Type()
)
hh3cDot11APUserAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthReqCntCM.setStatus("current")
_Hh3cDot11APUserAuthSuccCntCM_Type = Counter32
_Hh3cDot11APUserAuthSuccCntCM_Object = MibTableColumn
hh3cDot11APUserAuthSuccCntCM = _Hh3cDot11APUserAuthSuccCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1, 3),
    _Hh3cDot11APUserAuthSuccCntCM_Type()
)
hh3cDot11APUserAuthSuccCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthSuccCntCM.setStatus("current")
_Hh3cDot11APUserAuthFailCntCM_Type = Counter32
_Hh3cDot11APUserAuthFailCntCM_Object = MibTableColumn
hh3cDot11APUserAuthFailCntCM = _Hh3cDot11APUserAuthFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1, 4),
    _Hh3cDot11APUserAuthFailCntCM_Type()
)
hh3cDot11APUserAuthFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthFailCntCM.setStatus("current")
_Hh3cDot11AllUserOnlineTimeCM_Type = TimeTicks
_Hh3cDot11AllUserOnlineTimeCM_Object = MibTableColumn
hh3cDot11AllUserOnlineTimeCM = _Hh3cDot11AllUserOnlineTimeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 35, 1, 5),
    _Hh3cDot11AllUserOnlineTimeCM_Type()
)
hh3cDot11AllUserOnlineTimeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AllUserOnlineTimeCM.setStatus("current")
_Hh3cDot11APUserInfoStatis2CMTable_Object = MibTable
hh3cDot11APUserInfoStatis2CMTable = _Hh3cDot11APUserInfoStatis2CMTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36)
)
if mibBuilder.loadTexts:
    hh3cDot11APUserInfoStatis2CMTable.setStatus("current")
_Hh3cDot11APUserInfoStatis2CMEntry_Object = MibTableRow
hh3cDot11APUserInfoStatis2CMEntry = _Hh3cDot11APUserInfoStatis2CMEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1)
)
hh3cDot11APUserInfoStatis2CMEntry.setIndexNames(
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11CurAPID"),
    (0, "HH3C-DOT11-APMT-MIB", "hh3cDot11APUserMacAddr2CM"),
)
if mibBuilder.loadTexts:
    hh3cDot11APUserInfoStatis2CMEntry.setStatus("current")
_Hh3cDot11APUserMacAddr2CM_Type = MacAddress
_Hh3cDot11APUserMacAddr2CM_Object = MibTableColumn
hh3cDot11APUserMacAddr2CM = _Hh3cDot11APUserMacAddr2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 1),
    _Hh3cDot11APUserMacAddr2CM_Type()
)
hh3cDot11APUserMacAddr2CM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APUserMacAddr2CM.setStatus("current")
_Hh3cDot11APUserIpAddr2CM_Type = IpAddress
_Hh3cDot11APUserIpAddr2CM_Object = MibTableColumn
hh3cDot11APUserIpAddr2CM = _Hh3cDot11APUserIpAddr2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 2),
    _Hh3cDot11APUserIpAddr2CM_Type()
)
hh3cDot11APUserIpAddr2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserIpAddr2CM.setStatus("current")
_Hh3cDot11APUserLoginName2CM_Type = OctetString
_Hh3cDot11APUserLoginName2CM_Object = MibTableColumn
hh3cDot11APUserLoginName2CM = _Hh3cDot11APUserLoginName2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 3),
    _Hh3cDot11APUserLoginName2CM_Type()
)
hh3cDot11APUserLoginName2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserLoginName2CM.setStatus("current")
_Hh3cDot11APUserLoginTime2CM_Type = OctetString
_Hh3cDot11APUserLoginTime2CM_Object = MibTableColumn
hh3cDot11APUserLoginTime2CM = _Hh3cDot11APUserLoginTime2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 4),
    _Hh3cDot11APUserLoginTime2CM_Type()
)
hh3cDot11APUserLoginTime2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserLoginTime2CM.setStatus("current")
_Hh3cDot11APUserOnlineTime2CM_Type = TimeTicks
_Hh3cDot11APUserOnlineTime2CM_Object = MibTableColumn
hh3cDot11APUserOnlineTime2CM = _Hh3cDot11APUserOnlineTime2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 5),
    _Hh3cDot11APUserOnlineTime2CM_Type()
)
hh3cDot11APUserOnlineTime2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserOnlineTime2CM.setStatus("current")


class _Hh3cDot11APUserAuthType2CM_Type(Integer32):
    """Custom type hh3cDot11APUserAuthType2CM based on Integer32"""
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


_Hh3cDot11APUserAuthType2CM_Type.__name__ = "Integer32"
_Hh3cDot11APUserAuthType2CM_Object = MibTableColumn
hh3cDot11APUserAuthType2CM = _Hh3cDot11APUserAuthType2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 6),
    _Hh3cDot11APUserAuthType2CM_Type()
)
hh3cDot11APUserAuthType2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserAuthType2CM.setStatus("current")
_Hh3cDot11APUserTxPacketCnt2CM_Type = Counter32
_Hh3cDot11APUserTxPacketCnt2CM_Object = MibTableColumn
hh3cDot11APUserTxPacketCnt2CM = _Hh3cDot11APUserTxPacketCnt2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 7),
    _Hh3cDot11APUserTxPacketCnt2CM_Type()
)
hh3cDot11APUserTxPacketCnt2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserTxPacketCnt2CM.setStatus("current")
_Hh3cDot11APUserTxBytes2CM_Type = Counter64
_Hh3cDot11APUserTxBytes2CM_Object = MibTableColumn
hh3cDot11APUserTxBytes2CM = _Hh3cDot11APUserTxBytes2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 8),
    _Hh3cDot11APUserTxBytes2CM_Type()
)
hh3cDot11APUserTxBytes2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserTxBytes2CM.setStatus("current")
_Hh3cDot11APUserRxPacketCnt2CM_Type = Counter32
_Hh3cDot11APUserRxPacketCnt2CM_Object = MibTableColumn
hh3cDot11APUserRxPacketCnt2CM = _Hh3cDot11APUserRxPacketCnt2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 9),
    _Hh3cDot11APUserRxPacketCnt2CM_Type()
)
hh3cDot11APUserRxPacketCnt2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserRxPacketCnt2CM.setStatus("current")
_Hh3cDot11APUserRxBytes2CM_Type = Counter64
_Hh3cDot11APUserRxBytes2CM_Object = MibTableColumn
hh3cDot11APUserRxBytes2CM = _Hh3cDot11APUserRxBytes2CM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 2, 36, 1, 10),
    _Hh3cDot11APUserRxBytes2CM_Type()
)
hh3cDot11APUserRxBytes2CM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APUserRxBytes2CM.setStatus("current")
_Hh3cDot11APMtNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11APMtNotifyGroup = _Hh3cDot11APMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3)
)
_Hh3cDot11APMtTraps_ObjectIdentity = ObjectIdentity
hh3cDot11APMtTraps = _Hh3cDot11APMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0)
)
_Hh3cDot11APMtTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11APMtTrapVarObjects = _Hh3cDot11APMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1)
)
_Hh3cDot11APMtTrapCfgErrReason_Type = Hh3cDot11NotifyReasonType
_Hh3cDot11APMtTrapCfgErrReason_Object = MibScalar
hh3cDot11APMtTrapCfgErrReason = _Hh3cDot11APMtTrapCfgErrReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 1),
    _Hh3cDot11APMtTrapCfgErrReason_Type()
)
hh3cDot11APMtTrapCfgErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapCfgErrReason.setStatus("current")


class _Hh3cDot11APMtTrapRadioFailReason_Type(Integer32):
    """Custom type hh3cDot11APMtTrapRadioFailReason based on Integer32"""
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
          ("hh3cerror", 2),
          ("radar", 4),
          ("swerror", 3),
          ("unknown", 8))
    )


_Hh3cDot11APMtTrapRadioFailReason_Type.__name__ = "Integer32"
_Hh3cDot11APMtTrapRadioFailReason_Object = MibScalar
hh3cDot11APMtTrapRadioFailReason = _Hh3cDot11APMtTrapRadioFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 2),
    _Hh3cDot11APMtTrapRadioFailReason_Type()
)
hh3cDot11APMtTrapRadioFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapRadioFailReason.setStatus("current")
_Hh3cDot11APMtTrapOldChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11APMtTrapOldChannel_Object = MibScalar
hh3cDot11APMtTrapOldChannel = _Hh3cDot11APMtTrapOldChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 3),
    _Hh3cDot11APMtTrapOldChannel_Type()
)
hh3cDot11APMtTrapOldChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapOldChannel.setStatus("current")
_Hh3cDot11APMtTrapNewChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11APMtTrapNewChannel_Object = MibScalar
hh3cDot11APMtTrapNewChannel = _Hh3cDot11APMtTrapNewChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 4),
    _Hh3cDot11APMtTrapNewChannel_Type()
)
hh3cDot11APMtTrapNewChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapNewChannel.setStatus("current")
_Hh3cDot11APChannelChgMode_Type = Hh3cDot11RFModeType
_Hh3cDot11APChannelChgMode_Object = MibScalar
hh3cDot11APChannelChgMode = _Hh3cDot11APChannelChgMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 5),
    _Hh3cDot11APChannelChgMode_Type()
)
hh3cDot11APChannelChgMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APChannelChgMode.setStatus("current")


class _Hh3cDot11APChgWorkMode_Type(Integer32):
    """Custom type hh3cDot11APChgWorkMode based on Integer32"""
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


_Hh3cDot11APChgWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11APChgWorkMode_Object = MibScalar
hh3cDot11APChgWorkMode = _Hh3cDot11APChgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 6),
    _Hh3cDot11APChgWorkMode_Type()
)
hh3cDot11APChgWorkMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APChgWorkMode.setStatus("current")
_Hh3cDot11APIntfDevMACAddress_Type = MacAddress
_Hh3cDot11APIntfDevMACAddress_Object = MibScalar
hh3cDot11APIntfDevMACAddress = _Hh3cDot11APIntfDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 7),
    _Hh3cDot11APIntfDevMACAddress_Type()
)
hh3cDot11APIntfDevMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APIntfDevMACAddress.setStatus("current")
_Hh3cDot11APMtTrapOldIPAddr_Type = IpAddress
_Hh3cDot11APMtTrapOldIPAddr_Object = MibScalar
hh3cDot11APMtTrapOldIPAddr = _Hh3cDot11APMtTrapOldIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 8),
    _Hh3cDot11APMtTrapOldIPAddr_Type()
)
hh3cDot11APMtTrapOldIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapOldIPAddr.setStatus("current")
_Hh3cDot11CurrInterfDetectedNum_Type = Integer32
_Hh3cDot11CurrInterfDetectedNum_Object = MibScalar
hh3cDot11CurrInterfDetectedNum = _Hh3cDot11CurrInterfDetectedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 9),
    _Hh3cDot11CurrInterfDetectedNum_Type()
)
hh3cDot11CurrInterfDetectedNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrInterfDetectedNum.setStatus("current")


class _Hh3cDot11StaFullReason_Type(Integer32):
    """Custom type hh3cDot11StaFullReason based on Integer32"""
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


_Hh3cDot11StaFullReason_Type.__name__ = "Integer32"
_Hh3cDot11StaFullReason_Object = MibScalar
hh3cDot11StaFullReason = _Hh3cDot11StaFullReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 10),
    _Hh3cDot11StaFullReason_Type()
)
hh3cDot11StaFullReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StaFullReason.setStatus("current")
_Hh3cDot11StaLimitNumber_Type = Integer32
_Hh3cDot11StaLimitNumber_Object = MibScalar
hh3cDot11StaLimitNumber = _Hh3cDot11StaLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 11),
    _Hh3cDot11StaLimitNumber_Type()
)
hh3cDot11StaLimitNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StaLimitNumber.setStatus("current")


class _Hh3cDot11APRadioDownReason_Type(Integer32):
    """Custom type hh3cDot11APRadioDownReason based on Integer32"""
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


_Hh3cDot11APRadioDownReason_Type.__name__ = "Integer32"
_Hh3cDot11APRadioDownReason_Object = MibScalar
hh3cDot11APRadioDownReason = _Hh3cDot11APRadioDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 12),
    _Hh3cDot11APRadioDownReason_Type()
)
hh3cDot11APRadioDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APRadioDownReason.setStatus("current")
_Hh3cDot11InterfMacList_Type = OctetString
_Hh3cDot11InterfMacList_Object = MibScalar
hh3cDot11InterfMacList = _Hh3cDot11InterfMacList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 13),
    _Hh3cDot11InterfMacList_Type()
)
hh3cDot11InterfMacList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11InterfMacList.setStatus("current")
_Hh3cDot11APTrapUserCnt_Type = Integer32
_Hh3cDot11APTrapUserCnt_Object = MibScalar
hh3cDot11APTrapUserCnt = _Hh3cDot11APTrapUserCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 14),
    _Hh3cDot11APTrapUserCnt_Type()
)
hh3cDot11APTrapUserCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapUserCnt.setStatus("current")
_Hh3cDot11APTrapUserThreshold_Type = Integer32
_Hh3cDot11APTrapUserThreshold_Object = MibScalar
hh3cDot11APTrapUserThreshold = _Hh3cDot11APTrapUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 15),
    _Hh3cDot11APTrapUserThreshold_Type()
)
hh3cDot11APTrapUserThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APTrapUserThreshold.setStatus("current")
_Hh3cDot11APMtChanlChgCount_Type = Integer32
_Hh3cDot11APMtChanlChgCount_Object = MibScalar
hh3cDot11APMtChanlChgCount = _Hh3cDot11APMtChanlChgCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 16),
    _Hh3cDot11APMtChanlChgCount_Type()
)
hh3cDot11APMtChanlChgCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtChanlChgCount.setStatus("current")
_Hh3cDot11APMtFormerApVersion_Type = OctetString
_Hh3cDot11APMtFormerApVersion_Object = MibScalar
hh3cDot11APMtFormerApVersion = _Hh3cDot11APMtFormerApVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 17),
    _Hh3cDot11APMtFormerApVersion_Type()
)
hh3cDot11APMtFormerApVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtFormerApVersion.setStatus("current")
_Hh3cDot11APMtAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11APMtAPID_Object = MibScalar
hh3cDot11APMtAPID = _Hh3cDot11APMtAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 18),
    _Hh3cDot11APMtAPID_Type()
)
hh3cDot11APMtAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtAPID.setStatus("current")
_Hh3cDot11APMtRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11APMtRadioID_Object = MibScalar
hh3cDot11APMtRadioID = _Hh3cDot11APMtRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 19),
    _Hh3cDot11APMtRadioID_Type()
)
hh3cDot11APMtRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtRadioID.setStatus("current")
_Hh3cDot11APMtChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11APMtChannel_Object = MibScalar
hh3cDot11APMtChannel = _Hh3cDot11APMtChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 20),
    _Hh3cDot11APMtChannel_Type()
)
hh3cDot11APMtChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtChannel.setStatus("current")
_Hh3cDot11APMtInterfMacAdd_Type = MacAddress
_Hh3cDot11APMtInterfMacAdd_Object = MibScalar
hh3cDot11APMtInterfMacAdd = _Hh3cDot11APMtInterfMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 21),
    _Hh3cDot11APMtInterfMacAdd_Type()
)
hh3cDot11APMtInterfMacAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtInterfMacAdd.setStatus("current")
_Hh3cDot11APMtAdjChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11APMtAdjChannel_Object = MibScalar
hh3cDot11APMtAdjChannel = _Hh3cDot11APMtAdjChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 22),
    _Hh3cDot11APMtAdjChannel_Type()
)
hh3cDot11APMtAdjChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtAdjChannel.setStatus("current")
_Hh3cDot11APMtFirstTrapTime_Type = TimeTicks
_Hh3cDot11APMtFirstTrapTime_Object = MibScalar
hh3cDot11APMtFirstTrapTime = _Hh3cDot11APMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 23),
    _Hh3cDot11APMtFirstTrapTime_Type()
)
hh3cDot11APMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtFirstTrapTime.setStatus("current")
_Hh3cDot11APMtTrapAPMacAddress_Type = MacAddress
_Hh3cDot11APMtTrapAPMacAddress_Object = MibScalar
hh3cDot11APMtTrapAPMacAddress = _Hh3cDot11APMtTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 24),
    _Hh3cDot11APMtTrapAPMacAddress_Type()
)
hh3cDot11APMtTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtTrapAPMacAddress.setStatus("current")


class _Hh3cDot11APMtUpLinkSwitchInfo_Type(Integer32):
    """Custom type hh3cDot11APMtUpLinkSwitchInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tdlte", 3),
          ("tdscdma", 2),
          ("unknown", 1))
    )


_Hh3cDot11APMtUpLinkSwitchInfo_Type.__name__ = "Integer32"
_Hh3cDot11APMtUpLinkSwitchInfo_Object = MibScalar
hh3cDot11APMtUpLinkSwitchInfo = _Hh3cDot11APMtUpLinkSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 25),
    _Hh3cDot11APMtUpLinkSwitchInfo_Type()
)
hh3cDot11APMtUpLinkSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtUpLinkSwitchInfo.setStatus("current")
_Hh3cDot11APMtUpLinkSwitchTime_Type = TimeStamp
_Hh3cDot11APMtUpLinkSwitchTime_Object = MibScalar
hh3cDot11APMtUpLinkSwitchTime = _Hh3cDot11APMtUpLinkSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 26),
    _Hh3cDot11APMtUpLinkSwitchTime_Type()
)
hh3cDot11APMtUpLinkSwitchTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtUpLinkSwitchTime.setStatus("current")
_Hh3cDot11APMtOldCellId_Type = Integer32
_Hh3cDot11APMtOldCellId_Object = MibScalar
hh3cDot11APMtOldCellId = _Hh3cDot11APMtOldCellId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 27),
    _Hh3cDot11APMtOldCellId_Type()
)
hh3cDot11APMtOldCellId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtOldCellId.setStatus("current")
_Hh3cDot11APMtCurCellId_Type = Integer32
_Hh3cDot11APMtCurCellId_Object = MibScalar
hh3cDot11APMtCurCellId = _Hh3cDot11APMtCurCellId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 28),
    _Hh3cDot11APMtCurCellId_Type()
)
hh3cDot11APMtCurCellId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtCurCellId.setStatus("current")
_Hh3cDot11APMtOldBand_Type = OctetString
_Hh3cDot11APMtOldBand_Object = MibScalar
hh3cDot11APMtOldBand = _Hh3cDot11APMtOldBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 29),
    _Hh3cDot11APMtOldBand_Type()
)
hh3cDot11APMtOldBand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtOldBand.setStatus("current")
_Hh3cDot11APMtActiveBand_Type = OctetString
_Hh3cDot11APMtActiveBand_Object = MibScalar
hh3cDot11APMtActiveBand = _Hh3cDot11APMtActiveBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 1, 30),
    _Hh3cDot11APMtActiveBand_Type()
)
hh3cDot11APMtActiveBand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11APMtActiveBand.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11APMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 1)
)
hh3cDot11APMtWorkModeChgTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APChgWorkMode"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtWorkModeChgTrap.setStatus(
        "current"
    )

hh3cDot11APMtCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 2)
)
hh3cDot11APMtCfgErrorTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapCfgErrReason"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtCfgErrorTrap.setStatus(
        "current"
    )

hh3cDot11APMtRadioFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 3)
)
hh3cDot11APMtRadioFailTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapRadioFailReason"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtRadioFailTrap.setStatus(
        "current"
    )

hh3cDot11APMtRadioFailRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 4)
)
hh3cDot11APMtRadioFailRecoverTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtRadioFailRecoverTrap.setStatus(
        "current"
    )

hh3cDot11APMtRdoChanlChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 5)
)
hh3cDot11APMtRdoChanlChgTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APChannelChgMode"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapOldChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapNewChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChanlChgCount"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtRdoChanlChgTrap.setStatus(
        "current"
    )

hh3cDot11APMtTimeSynFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 6)
)
hh3cDot11APMtTimeSynFail.setObjects(
    ("HH3C-DOT11-APMT-MIB", "hh3cDot11APID")
)
if mibBuilder.loadTexts:
    hh3cDot11APMtTimeSynFail.setStatus(
        "current"
    )

hh3cDot11APMtChlIntfDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 7)
)
hh3cDot11APMtChlIntfDetected.setObjects(
    ("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel")
)
if mibBuilder.loadTexts:
    hh3cDot11APMtChlIntfDetected.setStatus(
        "current"
    )

hh3cDot11APMtIntfAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 8)
)
hh3cDot11APMtIntfAPDetected.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtIntfAPDetected.setStatus(
        "current"
    )

hh3cDot11APMtIntfStaDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 9)
)
hh3cDot11APMtIntfStaDetected.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtIntfStaDetected.setStatus(
        "current"
    )

hh3cDot11APMtIPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 10)
)
hh3cDot11APMtIPChange.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APIPAddress"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapOldIPAddr"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtIPChange.setStatus(
        "current"
    )

hh3cDot11APFlashWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 11)
)
hh3cDot11APFlashWriteFailure.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFormerApVersion"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APFlashWriteFailure.setStatus(
        "current"
    )

hh3cDot11APSysReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 12)
)
hh3cDot11APSysReboot.setObjects(
    ("HH3C-DOT11-APMT-MIB", "hh3cDot11APID")
)
if mibBuilder.loadTexts:
    hh3cDot11APSysReboot.setStatus(
        "current"
    )

hh3cDot11APMtAvailChlTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 13)
)
hh3cDot11APMtAvailChlTooLow.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtAvailChlTooLow.setStatus(
        "current"
    )

hh3cDot11APImgDwldSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 14)
)
hh3cDot11APImgDwldSuccess.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11CurrAPName"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11CurrAPIPAddress"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11CurrAPSoftwareVersion"))
)
if mibBuilder.loadTexts:
    hh3cDot11APImgDwldSuccess.setStatus(
        "current"
    )

hh3cDot11APInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 15)
)
hh3cDot11APInterfDetectedTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11CurrInterfDetectedNum"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11InterfMacList"))
)
if mibBuilder.loadTexts:
    hh3cDot11APInterfDetectedTrap.setStatus(
        "current"
    )

hh3cDot11APInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 16)
)
hh3cDot11APInterfClearTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APInterfClearTrap.setStatus(
        "current"
    )

hh3cDot11StaInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 17)
)
hh3cDot11StaInterfDetectedTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11CurrInterfDetectedNum"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11InterfMacList"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11StaInterfDetectedTrap.setStatus(
        "current"
    )

hh3cDot11StaInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 18)
)
hh3cDot11StaInterfClearTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11StaInterfClearTrap.setStatus(
        "current"
    )

hh3cDot11OtherDevIntDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 19)
)
hh3cDot11OtherDevIntDetectedTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11OtherDevIntDetectedTrap.setStatus(
        "current"
    )

hh3cDot11OtherDevIntClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 20)
)
hh3cDot11OtherDevIntClearTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11Channel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11OtherDevIntClearTrap.setStatus(
        "current"
    )

hh3cDot11APModuleTroubleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 21)
)
hh3cDot11APModuleTroubleTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APModuleTroubleTrap.setStatus(
        "current"
    )

hh3cDot11APModuleTroubleClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 22)
)
hh3cDot11APModuleTroubleClearTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APModuleTroubleClearTrap.setStatus(
        "current"
    )

hh3cDot11APRadioDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 23)
)
hh3cDot11APRadioDownTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APRadioDownReason"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APRadioDownTrap.setStatus(
        "current"
    )

hh3cDot11APRadioDownRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 24)
)
hh3cDot11APRadioDownRecovTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APRadioDownRecovTrap.setStatus(
        "current"
    )

hh3cDot11APStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 25)
)
hh3cDot11APStaFullTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11StaLimitNumber"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11StaFullReason"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APStaFullTrap.setStatus(
        "current"
    )

hh3cDot11APStaFullRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 26)
)
hh3cDot11APStaFullRecoverTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11StaLimitNumber"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11StaFullReason"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APStaFullRecoverTrap.setStatus(
        "current"
    )

hh3cDot11DFSFreeCntBelowThrRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 27)
)
hh3cDot11DFSFreeCntBelowThrRecov.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11RadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11DFSFreeCntBelowThrRecov.setStatus(
        "current"
    )

hh3cDot11APCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 28)
)
hh3cDot11APCpuUsageHigh.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APCPURTUsage"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageHigh.setStatus(
        "current"
    )

hh3cDot11APCpuUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 29)
)
hh3cDot11APCpuUsageHighRecover.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APCPURTUsage"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageHighRecover.setStatus(
        "current"
    )

hh3cDot11APMemUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 30)
)
hh3cDot11APMemUsageHigh.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMemRTUsage"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageHigh.setStatus(
        "current"
    )

hh3cDot11APMemUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 31)
)
hh3cDot11APMemUsageHighRecover.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMemRTUsage"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageHighRecover.setStatus(
        "current"
    )

hh3cDot11APTrapUserCntExceedThre = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 32)
)
hh3cDot11APTrapUserCntExceedThre.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APTrapUserCnt"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APTrapUserThreshold"))
)
if mibBuilder.loadTexts:
    hh3cDot11APTrapUserCntExceedThre.setStatus(
        "current"
    )

hh3cDot11APMtDetectedIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 33)
)
hh3cDot11APMtDetectedIntfAP.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtDetectedIntfAP.setStatus(
        "current"
    )

hh3cDot11APMtDetectedIntfSTA = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 34)
)
hh3cDot11APMtDetectedIntfSTA.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtDetectedIntfSTA.setStatus(
        "current"
    )

hh3cDot11APMtDetectedIntfOtherDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 35)
)
hh3cDot11APMtDetectedIntfOtherDev.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APMtDetectedIntfOtherDev.setStatus(
        "current"
    )

hh3cDot11DetcAdjChlIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 36)
)
hh3cDot11DetcAdjChlIntfAP.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAdjChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11DetcAdjChlIntfAP.setStatus(
        "current"
    )

hh3cDot11DetcAdjChlIntfAPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 37)
)
hh3cDot11DetcAdjChlIntfAPClear.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtRadioID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAdjChannel"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtInterfMacAdd"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11DetcAdjChlIntfAPClear.setStatus(
        "current"
    )

hh3cDot11APPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 38)
)
hh3cDot11APPowerOffTrap.setObjects(
    ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID")
)
if mibBuilder.loadTexts:
    hh3cDot11APPowerOffTrap.setStatus(
        "current"
    )

hh3cDot11APPowerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 39)
)
hh3cDot11APPowerOnTrap.setObjects(
    ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID")
)
if mibBuilder.loadTexts:
    hh3cDot11APPowerOnTrap.setStatus(
        "current"
    )

hh3cDot11UpLinkSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 2, 3, 0, 40)
)
hh3cDot11UpLinkSwitchTrap.setObjects(
      *(("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtAPID"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtUpLinkSwitchInfo"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtTrapAPMacAddress"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtUpLinkSwitchTime"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtOldCellId"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtCurCellId"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtOldBand"),
        ("HH3C-DOT11-APMT-MIB", "hh3cDot11APMtActiveBand"))
)
if mibBuilder.loadTexts:
    hh3cDot11UpLinkSwitchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-APMT-MIB",
    **{"hh3cDot11APMT": hh3cDot11APMT,
       "hh3cDot11APObjectGroup": hh3cDot11APObjectGroup,
       "hh3cDot11APObjectStatusTable": hh3cDot11APObjectStatusTable,
       "hh3cDot11APObjectStatusEntry": hh3cDot11APObjectStatusEntry,
       "hh3cDot11APID": hh3cDot11APID,
       "hh3cDot11APIPAddress": hh3cDot11APIPAddress,
       "hh3cDot11APMacAddress": hh3cDot11APMacAddress,
       "hh3cDot11APOperationStatus": hh3cDot11APOperationStatus,
       "hh3cDot11APTemplateNameOfAP": hh3cDot11APTemplateNameOfAP,
       "hh3cDot11APReset": hh3cDot11APReset,
       "hh3cDot11APCpuUsage": hh3cDot11APCpuUsage,
       "hh3cDot11APConnectionType": hh3cDot11APConnectionType,
       "hh3cDot11APLastImgDownloadTime": hh3cDot11APLastImgDownloadTime,
       "hh3cDot11APIPv6Address": hh3cDot11APIPv6Address,
       "hh3cDot11APLastRegisterTime": hh3cDot11APLastRegisterTime,
       "hh3cDot11APResetCM": hh3cDot11APResetCM,
       "hh3cDot11APObjectTable": hh3cDot11APObjectTable,
       "hh3cDot11APObjectEntry": hh3cDot11APObjectEntry,
       "hh3cDot11APObjID": hh3cDot11APObjID,
       "hh3cDot11CurrAPIPAddress": hh3cDot11CurrAPIPAddress,
       "hh3cDot11CurrAPMacAddress": hh3cDot11CurrAPMacAddress,
       "hh3cDot11CurrACPortIndex": hh3cDot11CurrACPortIndex,
       "hh3cDot11CurrAPMACMode": hh3cDot11CurrAPMACMode,
       "hh3cDot11CurrAPTemplateName": hh3cDot11CurrAPTemplateName,
       "hh3cDot11CurrAPStationAssocCount": hh3cDot11CurrAPStationAssocCount,
       "hh3cDot11CurrAPName": hh3cDot11CurrAPName,
       "hh3cDot11CurrAPModelName": hh3cDot11CurrAPModelName,
       "hh3cDot11CurrAPImageName": hh3cDot11CurrAPImageName,
       "hh3cDot11CurrAPSoftwareVersion": hh3cDot11CurrAPSoftwareVersion,
       "hh3cDot11CurrAPIPNetMask": hh3cDot11CurrAPIPNetMask,
       "hh3cDot11CurrRadioModeSupport": hh3cDot11CurrRadioModeSupport,
       "hh3cDot11CurrIfNumber": hh3cDot11CurrIfNumber,
       "hh3cDot11CurrAPElementID": hh3cDot11CurrAPElementID,
       "hh3cDot11CurrAPMode": hh3cDot11CurrAPMode,
       "hh3cDot11CurrAPIPv6Address": hh3cDot11CurrAPIPv6Address,
       "hh3cDot11CurrAPSSIDNumber": hh3cDot11CurrAPSSIDNumber,
       "hh3cDot11CurrAPManufacturer": hh3cDot11CurrAPManufacturer,
       "hh3cDot11CurrAPMemorySize": hh3cDot11CurrAPMemorySize,
       "hh3cDot11CurrAPMemSizeInBytes": hh3cDot11CurrAPMemSizeInBytes,
       "hh3cDot11CurrAPFlashSize": hh3cDot11CurrAPFlashSize,
       "hh3cDot11CurrAPFlashSizeInBytes": hh3cDot11CurrAPFlashSizeInBytes,
       "hh3cDot11CurrAPReleasedVersion": hh3cDot11CurrAPReleasedVersion,
       "hh3cDot11CurrRadioModeSupport2": hh3cDot11CurrRadioModeSupport2,
       "hh3cDot11CurrAPCPUTypeCM": hh3cDot11CurrAPCPUTypeCM,
       "hh3cDot11CurrAPMemoryTypeCM": hh3cDot11CurrAPMemoryTypeCM,
       "hh3cDot11CurrAPBSSIDNumberCM": hh3cDot11CurrAPBSSIDNumberCM,
       "hh3cDot11APRadioTable": hh3cDot11APRadioTable,
       "hh3cDot11APRadioEntry": hh3cDot11APRadioEntry,
       "hh3cDot11CurAPID": hh3cDot11CurAPID,
       "hh3cDot11RadioID": hh3cDot11RadioID,
       "hh3cDot11AdminStatus": hh3cDot11AdminStatus,
       "hh3cDot11OperStatus": hh3cDot11OperStatus,
       "hh3cDot11Channel": hh3cDot11Channel,
       "hh3cDot11TxPowerLevel": hh3cDot11TxPowerLevel,
       "hh3cDot11APRadioIfIndex": hh3cDot11APRadioIfIndex,
       "hh3cDot11AntennaGain": hh3cDot11AntennaGain,
       "hh3cDot11MaxBandwidth": hh3cDot11MaxBandwidth,
       "hh3cDot11ResourceUseRatio": hh3cDot11ResourceUseRatio,
       "hh3cDot11RadioModeSupport": hh3cDot11RadioModeSupport,
       "hh3cDot11TxPowerLevel2": hh3cDot11TxPowerLevel2,
       "hh3cDot11PowerMgmtStatus": hh3cDot11PowerMgmtStatus,
       "hh3cDot11ChannelSwitchTimes": hh3cDot11ChannelSwitchTimes,
       "hh3cDot11AntennaType": hh3cDot11AntennaType,
       "hh3cDot11DiversitySelectionRx": hh3cDot11DiversitySelectionRx,
       "hh3cDot11MaxTxPwrLvl": hh3cDot11MaxTxPwrLvl,
       "hh3cDot11PwrAttRange": hh3cDot11PwrAttRange,
       "hh3cDot11AvgRxSignalStrength": hh3cDot11AvgRxSignalStrength,
       "hh3cDot11HighestRxSignalStrength": hh3cDot11HighestRxSignalStrength,
       "hh3cDot11LowestRxSignalStrength": hh3cDot11LowestRxSignalStrength,
       "hh3cDot11RadioIfUpdownTimes": hh3cDot11RadioIfUpdownTimes,
       "hh3cDot11RadioIfLastChange": hh3cDot11RadioIfLastChange,
       "hh3cDot11RadioModeSupport2": hh3cDot11RadioModeSupport2,
       "hh3cDot11OperStatusCM": hh3cDot11OperStatusCM,
       "hh3cDot11APBSSTable": hh3cDot11APBSSTable,
       "hh3cDot11APBSSEntry": hh3cDot11APBSSEntry,
       "hh3cDot11WlanID": hh3cDot11WlanID,
       "hh3cDot11BSSID": hh3cDot11BSSID,
       "hh3cDot11CurrSvcPolicyID": hh3cDot11CurrSvcPolicyID,
       "hh3cDot11SSID": hh3cDot11SSID,
       "hh3cDot11CurrSSIDResourceUseRatio": hh3cDot11CurrSSIDResourceUseRatio,
       "hh3cDot11APEssVlanId": hh3cDot11APEssVlanId,
       "hh3cDot11APModelTable": hh3cDot11APModelTable,
       "hh3cDot11APModelEntry": hh3cDot11APModelEntry,
       "hh3cDot11APModelAlias": hh3cDot11APModelAlias,
       "hh3cDot11APModelName": hh3cDot11APModelName,
       "hh3cDot11RadioNumSupport": hh3cDot11RadioNumSupport,
       "hh3cDot11StationNumSupport": hh3cDot11StationNumSupport,
       "hh3cDot11MACModeSupport": hh3cDot11MACModeSupport,
       "hh3cDot11APManufacturer": hh3cDot11APManufacturer,
       "hh3cDot11APCPUType": hh3cDot11APCPUType,
       "hh3cDot11APCPUClockSpeed": hh3cDot11APCPUClockSpeed,
       "hh3cDot11APMemoryType": hh3cDot11APMemoryType,
       "hh3cDot11APFlashType": hh3cDot11APFlashType,
       "hh3cDot11APFlashSize": hh3cDot11APFlashSize,
       "hh3cDot11APMemSize": hh3cDot11APMemSize,
       "hh3cDot11APFlashSizeInBytes": hh3cDot11APFlashSizeInBytes,
       "hh3cDot11APMemorySize": hh3cDot11APMemorySize,
       "hh3cDot11APIfTable": hh3cDot11APIfTable,
       "hh3cDot11APIfEntry": hh3cDot11APIfEntry,
       "hh3cDot11APIfIndex": hh3cDot11APIfIndex,
       "hh3cDot11APIfDescr": hh3cDot11APIfDescr,
       "hh3cDot11APIfType": hh3cDot11APIfType,
       "hh3cDot11APIfMtu": hh3cDot11APIfMtu,
       "hh3cDot11APIfPHYAddress": hh3cDot11APIfPHYAddress,
       "hh3cDot11APIfSpeed": hh3cDot11APIfSpeed,
       "hh3cDot11APIfInDataRate": hh3cDot11APIfInDataRate,
       "hh3cDot11APIfOutDataRate": hh3cDot11APIfOutDataRate,
       "hh3cDot11APIfSpeedKbps": hh3cDot11APIfSpeedKbps,
       "hh3cDot11APIfTypeCM": hh3cDot11APIfTypeCM,
       "hh3cDot11APSSIDObjectTable": hh3cDot11APSSIDObjectTable,
       "hh3cDot11APSSIDObjectEntry": hh3cDot11APSSIDObjectEntry,
       "hh3cDot11APConfigSPID": hh3cDot11APConfigSPID,
       "hh3cDot11APConfigSSIDName": hh3cDot11APConfigSSIDName,
       "hh3cDot11APConfigBSSIDNum": hh3cDot11APConfigBSSIDNum,
       "hh3cDot11APConfigPortalStaNum": hh3cDot11APConfigPortalStaNum,
       "hh3cDot11APSysInfoTable": hh3cDot11APSysInfoTable,
       "hh3cDot11APSysInfoEntry": hh3cDot11APSysInfoEntry,
       "hh3cDot11APSysUpTime": hh3cDot11APSysUpTime,
       "hh3cDot11APCPURTUsage": hh3cDot11APCPURTUsage,
       "hh3cDot11APCPUAvgUsage": hh3cDot11APCPUAvgUsage,
       "hh3cDot11APMemRTUsage": hh3cDot11APMemRTUsage,
       "hh3cDot11APMemAvgUsage": hh3cDot11APMemAvgUsage,
       "hh3cDot11APIPAddressGateway": hh3cDot11APIPAddressGateway,
       "hh3cDot11APACAssociateStatus": hh3cDot11APACAssociateStatus,
       "hh3cDot11APManuBuildInfo": hh3cDot11APManuBuildInfo,
       "hh3cDot11APFlashFreeSize": hh3cDot11APFlashFreeSize,
       "hh3cDot11APTemperature": hh3cDot11APTemperature,
       "hh3cDot11APIdleListTable": hh3cDot11APIdleListTable,
       "hh3cDot11APIdleListEntry": hh3cDot11APIdleListEntry,
       "hh3cDot11APIdleTemplateName": hh3cDot11APIdleTemplateName,
       "hh3cDot11APIdleSerialID": hh3cDot11APIdleSerialID,
       "hh3cDot11APSysInfoByAPIDTable": hh3cDot11APSysInfoByAPIDTable,
       "hh3cDot11APSysInfoByAPIDEntry": hh3cDot11APSysInfoByAPIDEntry,
       "hh3cDot11APSysUpTime2": hh3cDot11APSysUpTime2,
       "hh3cDot11APCPURTUsage2": hh3cDot11APCPURTUsage2,
       "hh3cDot11APCPUAvgUsage2": hh3cDot11APCPUAvgUsage2,
       "hh3cDot11APMemRTUsage2": hh3cDot11APMemRTUsage2,
       "hh3cDot11APMemAvgUsage2": hh3cDot11APMemAvgUsage2,
       "hh3cDot11APIPAddressGateway2": hh3cDot11APIPAddressGateway2,
       "hh3cDot11APACAssociateStatus2": hh3cDot11APACAssociateStatus2,
       "hh3cDot11APManuBuildInfo2": hh3cDot11APManuBuildInfo2,
       "hh3cDot11APFlashFreeSize2": hh3cDot11APFlashFreeSize2,
       "hh3cDot11APTemperature2": hh3cDot11APTemperature2,
       "hh3cDot11APMacAddress2": hh3cDot11APMacAddress2,
       "hh3cDot11APACAssociateStatusCM": hh3cDot11APACAssociateStatusCM,
       "hh3cDot11APStatisGroup": hh3cDot11APStatisGroup,
       "hh3cDot11APRxStatisTable": hh3cDot11APRxStatisTable,
       "hh3cDot11APRxStatisEntry": hh3cDot11APRxStatisEntry,
       "hh3cDot11RxFrameDupCnt": hh3cDot11RxFrameDupCnt,
       "hh3cDot11RxFrameCnt": hh3cDot11RxFrameCnt,
       "hh3cDot11RxUcastFrameCnt": hh3cDot11RxUcastFrameCnt,
       "hh3cDot11RxBcastFrameCnt": hh3cDot11RxBcastFrameCnt,
       "hh3cDot11RxMcastFrameCnt": hh3cDot11RxMcastFrameCnt,
       "hh3cDot11RxDiscardFrameCnt": hh3cDot11RxDiscardFrameCnt,
       "hh3cDot11RxFragCnt": hh3cDot11RxFragCnt,
       "hh3cDot11RxFcsErrCnt": hh3cDot11RxFcsErrCnt,
       "hh3cDot11RxFrameBytes": hh3cDot11RxFrameBytes,
       "hh3cDot11RxUcastFrameBytes": hh3cDot11RxUcastFrameBytes,
       "hh3cDot11RxBcastFrameBytes": hh3cDot11RxBcastFrameBytes,
       "hh3cDot11RxMcastFrameBytes": hh3cDot11RxMcastFrameBytes,
       "hh3cDot11RxDiscardFrameBytes": hh3cDot11RxDiscardFrameBytes,
       "hh3cDot11RxMgmtFrameCnt": hh3cDot11RxMgmtFrameCnt,
       "hh3cDot11RxCtrlFrameCnt": hh3cDot11RxCtrlFrameCnt,
       "hh3cDot11RxDataFrameCnt": hh3cDot11RxDataFrameCnt,
       "hh3cDot11RxDecryptErrorCnt": hh3cDot11RxDecryptErrorCnt,
       "hh3cDot11RxAuthenFrameCnt": hh3cDot11RxAuthenFrameCnt,
       "hh3cDot11RxAssociateFrameCnt": hh3cDot11RxAssociateFrameCnt,
       "hh3cDot11RxFrameErrorRatio": hh3cDot11RxFrameErrorRatio,
       "hh3cDot11RxPhyErrorCnt": hh3cDot11RxPhyErrorCnt,
       "hh3cDot11RxMICErrorCnt": hh3cDot11RxMICErrorCnt,
       "hh3cDot11RxDataFrameBytes": hh3cDot11RxDataFrameBytes,
       "hh3cDot11RadioRxAverSnr": hh3cDot11RadioRxAverSnr,
       "hh3cDot11RxPayloadBytes": hh3cDot11RxPayloadBytes,
       "hh3cDot11RxTrafficSpeed": hh3cDot11RxTrafficSpeed,
       "hh3cDot11RxUcastDataFrameCnt": hh3cDot11RxUcastDataFrameCnt,
       "hh3cDot11RxNUcastDataFrameCnt": hh3cDot11RxNUcastDataFrameCnt,
       "hh3cDot11RxTotalDiscardFrameCnt": hh3cDot11RxTotalDiscardFrameCnt,
       "hh3cDot11RxTotalIPCheckErrPacketCnt": hh3cDot11RxTotalIPCheckErrPacketCnt,
       "hh3cDot11RxSignalStrengthPacketCntCM": hh3cDot11RxSignalStrengthPacketCntCM,
       "hh3cDot11RxDataFrameCntCM": hh3cDot11RxDataFrameCntCM,
       "hh3cDot11RxTotalFrameCnt": hh3cDot11RxTotalFrameCnt,
       "hh3cDot11APTxStatisTable": hh3cDot11APTxStatisTable,
       "hh3cDot11APTxStatisEntry": hh3cDot11APTxStatisEntry,
       "hh3cDot11TxFragCnt": hh3cDot11TxFragCnt,
       "hh3cDot11FailedCnt": hh3cDot11FailedCnt,
       "hh3cDot11RetryCnt": hh3cDot11RetryCnt,
       "hh3cDot11MultiRetryCnt": hh3cDot11MultiRetryCnt,
       "hh3cDot11RtsSuccessCnt": hh3cDot11RtsSuccessCnt,
       "hh3cDot11RtsFailCnt": hh3cDot11RtsFailCnt,
       "hh3cDot11AckFailCnt": hh3cDot11AckFailCnt,
       "hh3cDot11TxFrameCnt": hh3cDot11TxFrameCnt,
       "hh3cDot11TxUcastFrameCnt": hh3cDot11TxUcastFrameCnt,
       "hh3cDot11TxBcastFrameCnt": hh3cDot11TxBcastFrameCnt,
       "hh3cDot11TxMcastFrameCnt": hh3cDot11TxMcastFrameCnt,
       "hh3cDot11TxDiscardFrameCnt": hh3cDot11TxDiscardFrameCnt,
       "hh3cDot11TxFrameBytes": hh3cDot11TxFrameBytes,
       "hh3cDot11TxUcastFrameBytes": hh3cDot11TxUcastFrameBytes,
       "hh3cDot11TxBcastFrameBytes": hh3cDot11TxBcastFrameBytes,
       "hh3cDot11TxMcastFrameBytes": hh3cDot11TxMcastFrameBytes,
       "hh3cDot11TxDiscardFrameBytes": hh3cDot11TxDiscardFrameBytes,
       "hh3cDot11TxAuthenFrameCnt": hh3cDot11TxAuthenFrameCnt,
       "hh3cDot11TxAssociateFrameCnt": hh3cDot11TxAssociateFrameCnt,
       "hh3cDot11TxFrameRetryRatio": hh3cDot11TxFrameRetryRatio,
       "hh3cDot11TxDataFrameCnt": hh3cDot11TxDataFrameCnt,
       "hh3cDot11TxDataFrameBytes": hh3cDot11TxDataFrameBytes,
       "hh3cDot11TxMSDUCnt": hh3cDot11TxMSDUCnt,
       "hh3cDot11TxDiscardMSDUCnt": hh3cDot11TxDiscardMSDUCnt,
       "hh3cDot11RetryMSDUCnt": hh3cDot11RetryMSDUCnt,
       "hh3cDot11TxPayloadBytes": hh3cDot11TxPayloadBytes,
       "hh3cDot11TxTrafficSpeed": hh3cDot11TxTrafficSpeed,
       "hh3cDot11TxErrFrameRatio": hh3cDot11TxErrFrameRatio,
       "hh3cDot11TxFrameRate": hh3cDot11TxFrameRate,
       "hh3cDot11TxMgtFrameCnt": hh3cDot11TxMgtFrameCnt,
       "hh3cDot11TxCtrlFrameCnt": hh3cDot11TxCtrlFrameCnt,
       "hh3cDot11TxMACErrCnt": hh3cDot11TxMACErrCnt,
       "hh3cDot11TxErrFrameCnt": hh3cDot11TxErrFrameCnt,
       "hh3cDot11TxUcastDataFrameCnt": hh3cDot11TxUcastDataFrameCnt,
       "hh3cDot11TxNUcastDataFrameCnt": hh3cDot11TxNUcastDataFrameCnt,
       "hh3cDot11TxTotalFrameCnt": hh3cDot11TxTotalFrameCnt,
       "hh3cDot11APAssocStatisTable": hh3cDot11APAssocStatisTable,
       "hh3cDot11APAssocStatisEntry": hh3cDot11APAssocStatisEntry,
       "hh3cDot11ApStationAssocSum": hh3cDot11ApStationAssocSum,
       "hh3cDot11ApStationAssocFailSum": hh3cDot11ApStationAssocFailSum,
       "hh3cDot11ApStationReassocSum": hh3cDot11ApStationReassocSum,
       "hh3cDot11ApStationAssocRejectSum": hh3cDot11ApStationAssocRejectSum,
       "hh3cDot11ApStationExDeAuthenSum": hh3cDot11ApStationExDeAuthenSum,
       "hh3cDot11ApStationCurAssocSum": hh3cDot11ApStationCurAssocSum,
       "hh3cDot11ApStaCurAuthSuccSum": hh3cDot11ApStaCurAuthSuccSum,
       "hh3cDot11AllStationUpSumTime": hh3cDot11AllStationUpSumTime,
       "hh3cDot11ApStationAssocReqSum": hh3cDot11ApStationAssocReqSum,
       "hh3cDot11AllStationUpSumTimeTicks": hh3cDot11AllStationUpSumTimeTicks,
       "hh3cDot11ApStationReassocReqSum": hh3cDot11ApStationReassocReqSum,
       "hh3cDot11ApStationReassocFailSum": hh3cDot11ApStationReassocFailSum,
       "hh3cDot11BSSRxStatisTable": hh3cDot11BSSRxStatisTable,
       "hh3cDot11BSSRxStatisEntry": hh3cDot11BSSRxStatisEntry,
       "hh3cDot11BSSRxFrameCnt": hh3cDot11BSSRxFrameCnt,
       "hh3cDot11BSSRxFrameBytes": hh3cDot11BSSRxFrameBytes,
       "hh3cDot11BSSRxDataFrameCnt": hh3cDot11BSSRxDataFrameCnt,
       "hh3cDot11BSSRxDataFrameBytes": hh3cDot11BSSRxDataFrameBytes,
       "hh3cDot11BSSRxAssociateFrameCnt": hh3cDot11BSSRxAssociateFrameCnt,
       "hh3cDot11BSSRxFrameErrorRatio": hh3cDot11BSSRxFrameErrorRatio,
       "hh3cDot11BSSRxPayloadBytes": hh3cDot11BSSRxPayloadBytes,
       "hh3cDot11BSSRxUniFrameCnt": hh3cDot11BSSRxUniFrameCnt,
       "hh3cDot11BSSRxNonUniFrameCnt": hh3cDot11BSSRxNonUniFrameCnt,
       "hh3cDot11BSSRxAuthenFrameCnt": hh3cDot11BSSRxAuthenFrameCnt,
       "hh3cDot11BSSTxStatisTable": hh3cDot11BSSTxStatisTable,
       "hh3cDot11BSSTxStatisEntry": hh3cDot11BSSTxStatisEntry,
       "hh3cDot11BSSTxFrameCnt": hh3cDot11BSSTxFrameCnt,
       "hh3cDot11BSSTxFrameBytes": hh3cDot11BSSTxFrameBytes,
       "hh3cDot11BSSTxDataFrameCnt": hh3cDot11BSSTxDataFrameCnt,
       "hh3cDot11BSSTxDataFrameBytes": hh3cDot11BSSTxDataFrameBytes,
       "hh3cDot11BSSTxAssociateFrameCnt": hh3cDot11BSSTxAssociateFrameCnt,
       "hh3cDot11BSSTxPayloadBytes": hh3cDot11BSSTxPayloadBytes,
       "hh3cDot11BSSTxRetryCnt": hh3cDot11BSSTxRetryCnt,
       "hh3cDot11BSSTxUniFrameCnt": hh3cDot11BSSTxUniFrameCnt,
       "hh3cDot11BSSTxNonUniFrameCnt": hh3cDot11BSSTxNonUniFrameCnt,
       "hh3cDot11BSSTxAuthenFrameCnt": hh3cDot11BSSTxAuthenFrameCnt,
       "hh3cDot11BSSAssocStatisTable": hh3cDot11BSSAssocStatisTable,
       "hh3cDot11BSSAssocStatisEntry": hh3cDot11BSSAssocStatisEntry,
       "hh3cDot11BSSStationAssocSum": hh3cDot11BSSStationAssocSum,
       "hh3cDot11BSSStationAssocFailSum": hh3cDot11BSSStationAssocFailSum,
       "hh3cDot11BSSStationReassocSum": hh3cDot11BSSStationReassocSum,
       "hh3cDot11BSSStationAssocRejectSum": hh3cDot11BSSStationAssocRejectSum,
       "hh3cDot11BSSStationExDeAssocSum": hh3cDot11BSSStationExDeAssocSum,
       "hh3cDot11BSSStationCurAssocSum": hh3cDot11BSSStationCurAssocSum,
       "hh3cDot11BSSStationAssocReqSum": hh3cDot11BSSStationAssocReqSum,
       "hh3cDot11BSSStationCurAuthSum": hh3cDot11BSSStationCurAuthSum,
       "hh3cDot11APLinkStatisTable": hh3cDot11APLinkStatisTable,
       "hh3cDot11APLinkStatisEntry": hh3cDot11APLinkStatisEntry,
       "hh3cDot11UpLinkUpDownTimes": hh3cDot11UpLinkUpDownTimes,
       "hh3cDot11DownLinkUpDownTimes": hh3cDot11DownLinkUpDownTimes,
       "hh3cDot11PrivateSrvRxFrameBytes": hh3cDot11PrivateSrvRxFrameBytes,
       "hh3cDot11PrivateSrvTxFrameBytes": hh3cDot11PrivateSrvTxFrameBytes,
       "hh3cDot11APInternetAllRxBytes": hh3cDot11APInternetAllRxBytes,
       "hh3cDot11APInternetAllTxBytes": hh3cDot11APInternetAllTxBytes,
       "hh3cDot11APLocalAllRxBytes": hh3cDot11APLocalAllRxBytes,
       "hh3cDot11APLocalAllTxBytes": hh3cDot11APLocalAllTxBytes,
       "hh3cDot11RadioAssocStatisTable": hh3cDot11RadioAssocStatisTable,
       "hh3cDot11RadioAssocStatisEntry": hh3cDot11RadioAssocStatisEntry,
       "hh3cDot11RadioStaAssocSum": hh3cDot11RadioStaAssocSum,
       "hh3cDot11RadioStaAssocFailSum": hh3cDot11RadioStaAssocFailSum,
       "hh3cDot11RadioStaReassocSum": hh3cDot11RadioStaReassocSum,
       "hh3cDot11RadioStaAssocRejectSum": hh3cDot11RadioStaAssocRejectSum,
       "hh3cDot11RadioStaExDeAssocSum": hh3cDot11RadioStaExDeAssocSum,
       "hh3cDot11RadioStaCurAssocSum": hh3cDot11RadioStaCurAssocSum,
       "hh3cDot11RadioMngFrameStatisTable": hh3cDot11RadioMngFrameStatisTable,
       "hh3cDot11RadioMngFrameStatisEntry": hh3cDot11RadioMngFrameStatisEntry,
       "hh3cDot11RadioStatisIndex": hh3cDot11RadioStatisIndex,
       "hh3cDot11MngFrameType": hh3cDot11MngFrameType,
       "hh3cDot11MngFrameCnt": hh3cDot11MngFrameCnt,
       "hh3cDot11APAuthFailStatisTable": hh3cDot11APAuthFailStatisTable,
       "hh3cDot11APAuthFailStatisEntry": hh3cDot11APAuthFailStatisEntry,
       "hh3cDot11APAuthFailStatisType": hh3cDot11APAuthFailStatisType,
       "hh3cDot11APAuthFailStatisCnt": hh3cDot11APAuthFailStatisCnt,
       "hh3cDot11APAssocFailStatisTable": hh3cDot11APAssocFailStatisTable,
       "hh3cDot11APAssocFailStatisEntry": hh3cDot11APAssocFailStatisEntry,
       "hh3cDot11APAssocFailStatisType": hh3cDot11APAssocFailStatisType,
       "hh3cDot11APAssocFailStatisCnt": hh3cDot11APAssocFailStatisCnt,
       "hh3cDot11APReassocStatisTable": hh3cDot11APReassocStatisTable,
       "hh3cDot11APReassocStatisEntry": hh3cDot11APReassocStatisEntry,
       "hh3cDot11APReassocStatisType": hh3cDot11APReassocStatisType,
       "hh3cDot11APReassocStatisCnt": hh3cDot11APReassocStatisCnt,
       "hh3cDot11APUserAuthStatisTable": hh3cDot11APUserAuthStatisTable,
       "hh3cDot11APUserAuthStatisEntry": hh3cDot11APUserAuthStatisEntry,
       "hh3cDot11UserAuthStatisType": hh3cDot11UserAuthStatisType,
       "hh3cDot11UserAuthStatisCnt": hh3cDot11UserAuthStatisCnt,
       "hh3cDot11APDeauthStatisTable": hh3cDot11APDeauthStatisTable,
       "hh3cDot11APDeauthStatisEntry": hh3cDot11APDeauthStatisEntry,
       "hh3cDot11APDeauthStatisType": hh3cDot11APDeauthStatisType,
       "hh3cDot11APDeauthStatisCnt": hh3cDot11APDeauthStatisCnt,
       "hh3cDot11APDeassocStatisTable": hh3cDot11APDeassocStatisTable,
       "hh3cDot11APDeassocStatisEntry": hh3cDot11APDeassocStatisEntry,
       "hh3cDot11APDeassocStatisType": hh3cDot11APDeassocStatisType,
       "hh3cDot11APDeassocStatisCnt": hh3cDot11APDeassocStatisCnt,
       "hh3cDot11APAssocFailStatis2Table": hh3cDot11APAssocFailStatis2Table,
       "hh3cDot11APAssocFailStatis2Entry": hh3cDot11APAssocFailStatis2Entry,
       "hh3cDot11APAssocFailStatis2Type": hh3cDot11APAssocFailStatis2Type,
       "hh3cDot11APAssocFailStatis2Cnt": hh3cDot11APAssocFailStatis2Cnt,
       "hh3cDot11APIfStatisTable": hh3cDot11APIfStatisTable,
       "hh3cDot11APIfStatisEntry": hh3cDot11APIfStatisEntry,
       "hh3cDot11APIfInPkts": hh3cDot11APIfInPkts,
       "hh3cDot11APIfInNormalPkts": hh3cDot11APIfInNormalPkts,
       "hh3cDot11APIfInErrorPkts": hh3cDot11APIfInErrorPkts,
       "hh3cDot11APIfOutPkts": hh3cDot11APIfOutPkts,
       "hh3cDot11APIfInOctets": hh3cDot11APIfInOctets,
       "hh3cDot11APIfOutOctets": hh3cDot11APIfOutOctets,
       "hh3cDot11APIfFlowOut": hh3cDot11APIfFlowOut,
       "hh3cDot11APIfFlowIN": hh3cDot11APIfFlowIN,
       "hh3cDot11APIfInUcastPkts": hh3cDot11APIfInUcastPkts,
       "hh3cDot11APIfInNUcastPkts": hh3cDot11APIfInNUcastPkts,
       "hh3cDot11APIfInDiscardPkts": hh3cDot11APIfInDiscardPkts,
       "hh3cDot11APIfOutUcastPkts": hh3cDot11APIfOutUcastPkts,
       "hh3cDot11APIfOutNUcastPkts": hh3cDot11APIfOutNUcastPkts,
       "hh3cDot11APIfOutDiscardPkts": hh3cDot11APIfOutDiscardPkts,
       "hh3cDot11APIfOutErrorPkts": hh3cDot11APIfOutErrorPkts,
       "hh3cDot11APIfUpdownTimes": hh3cDot11APIfUpdownTimes,
       "hh3cDot11APIfStatusKeepTime": hh3cDot11APIfStatusKeepTime,
       "hh3cDot11APIfOperStatus": hh3cDot11APIfOperStatus,
       "hh3cDot11APIfInBrdcastPkts": hh3cDot11APIfInBrdcastPkts,
       "hh3cDot11APIfOutBrdcastPkts": hh3cDot11APIfOutBrdcastPkts,
       "hh3cDot11APIfInMulcastPkts": hh3cDot11APIfInMulcastPkts,
       "hh3cDot11APIfOutMulcastPkts": hh3cDot11APIfOutMulcastPkts,
       "hh3cDot11APIfInPayloadOctets": hh3cDot11APIfInPayloadOctets,
       "hh3cDot11APIfOutPayloadOctets": hh3cDot11APIfOutPayloadOctets,
       "hh3cDot11RadioMngFrmStatisTable": hh3cDot11RadioMngFrmStatisTable,
       "hh3cDot11RadioMngFrmStatisEntry": hh3cDot11RadioMngFrmStatisEntry,
       "hh3cDot11MngFrmType": hh3cDot11MngFrmType,
       "hh3cDot11MngFrmCnt": hh3cDot11MngFrmCnt,
       "hh3cDot11APPacketSizeStatisTable": hh3cDot11APPacketSizeStatisTable,
       "hh3cDot11APPacketSizeStatisEntry": hh3cDot11APPacketSizeStatisEntry,
       "hh3cDot11APPacketSize": hh3cDot11APPacketSize,
       "hh3cDot11APRXPacketSizeCount": hh3cDot11APRXPacketSizeCount,
       "hh3cDot11APTXPacketSizeCount": hh3cDot11APTXPacketSizeCount,
       "hh3cDot11APPacketRateStatisTable": hh3cDot11APPacketRateStatisTable,
       "hh3cDot11APPacketRateStatisEntry": hh3cDot11APPacketRateStatisEntry,
       "hh3cDot11APPacketRate": hh3cDot11APPacketRate,
       "hh3cDot11APRXPacketRateCount": hh3cDot11APRXPacketRateCount,
       "hh3cDot11APTXPacketRateCount": hh3cDot11APTXPacketRateCount,
       "hh3cDot11APPacketMCSRateStatisTable": hh3cDot11APPacketMCSRateStatisTable,
       "hh3cDot11APPacketMCSRateStatisEntry": hh3cDot11APPacketMCSRateStatisEntry,
       "hh3cDot11APPacketMCSRate": hh3cDot11APPacketMCSRate,
       "hh3cDot11APRXPacketMCSRateCount": hh3cDot11APRXPacketMCSRateCount,
       "hh3cDot11APTXPacketMCSRateCount": hh3cDot11APTXPacketMCSRateCount,
       "hh3cDot11APAssocFailStatis3Table": hh3cDot11APAssocFailStatis3Table,
       "hh3cDot11APAssocFailStatis3Entry": hh3cDot11APAssocFailStatis3Entry,
       "hh3cDot11APAssocFailStatis3SRCnt": hh3cDot11APAssocFailStatis3SRCnt,
       "hh3cDot11APAssocFailStatis3NSRCnt": hh3cDot11APAssocFailStatis3NSRCnt,
       "hh3cDot11APAssocFailStatis3URCCnt": hh3cDot11APAssocFailStatis3URCCnt,
       "hh3cDot11APAssocFailStatis3RFCnt": hh3cDot11APAssocFailStatis3RFCnt,
       "hh3cDot11APAssocFailStatis3OtherCnt": hh3cDot11APAssocFailStatis3OtherCnt,
       "hh3cDot11APAssocFailStatis3RSSILowCntCM": hh3cDot11APAssocFailStatis3RSSILowCntCM,
       "hh3cDot11APIfStatisByAPIDTable": hh3cDot11APIfStatisByAPIDTable,
       "hh3cDot11APIfStatisByAPIDEntry": hh3cDot11APIfStatisByAPIDEntry,
       "hh3cDot11APIfInPkts2": hh3cDot11APIfInPkts2,
       "hh3cDot11APIfInNormalPkts2": hh3cDot11APIfInNormalPkts2,
       "hh3cDot11APIfInErrorPkts2": hh3cDot11APIfInErrorPkts2,
       "hh3cDot11APIfOutPkts2": hh3cDot11APIfOutPkts2,
       "hh3cDot11APIfInOctets2": hh3cDot11APIfInOctets2,
       "hh3cDot11APIfOutOctets2": hh3cDot11APIfOutOctets2,
       "hh3cDot11APIfFlowOut2": hh3cDot11APIfFlowOut2,
       "hh3cDot11APIfFlowIN2": hh3cDot11APIfFlowIN2,
       "hh3cDot11APIfInUcastPkts2": hh3cDot11APIfInUcastPkts2,
       "hh3cDot11APIfInNUcastPkts2": hh3cDot11APIfInNUcastPkts2,
       "hh3cDot11APIfInDiscardPkts2": hh3cDot11APIfInDiscardPkts2,
       "hh3cDot11APIfOutUcastPkts2": hh3cDot11APIfOutUcastPkts2,
       "hh3cDot11APIfOutNUcastPkts2": hh3cDot11APIfOutNUcastPkts2,
       "hh3cDot11APIfOutDiscardPkts2": hh3cDot11APIfOutDiscardPkts2,
       "hh3cDot11APIfOutErrorPkts2": hh3cDot11APIfOutErrorPkts2,
       "hh3cDot11APIfUpdownTimes2": hh3cDot11APIfUpdownTimes2,
       "hh3cDot11APIfStatusKeepTime2": hh3cDot11APIfStatusKeepTime2,
       "hh3cDot11APIfOperStatus2": hh3cDot11APIfOperStatus2,
       "hh3cDot11APIfInBrdcastPkts2": hh3cDot11APIfInBrdcastPkts2,
       "hh3cDot11APIfOutBrdcastPkts2": hh3cDot11APIfOutBrdcastPkts2,
       "hh3cDot11APIfInMulcastPkts2": hh3cDot11APIfInMulcastPkts2,
       "hh3cDot11APIfOutMulcastPkts2": hh3cDot11APIfOutMulcastPkts2,
       "hh3cDot11APIfInPayloadOctets2": hh3cDot11APIfInPayloadOctets2,
       "hh3cDot11APIfOutPayloadOctets2": hh3cDot11APIfOutPayloadOctets2,
       "hh3cDot11APIfInDataOctets2": hh3cDot11APIfInDataOctets2,
       "hh3cDot11APIfOutDataOctets2": hh3cDot11APIfOutDataOctets2,
       "hh3cDot11APIfAdminStatus": hh3cDot11APIfAdminStatus,
       "hh3cDot11APIfOperStatusCM": hh3cDot11APIfOperStatusCM,
       "hh3cDot11APUserSecAuthStatisTable": hh3cDot11APUserSecAuthStatisTable,
       "hh3cDot11APUserSecAuthStatisEntry": hh3cDot11APUserSecAuthStatisEntry,
       "hh3cDot11APUserAuthCurNumber": hh3cDot11APUserAuthCurNumber,
       "hh3cDot11APUserConnFailCnt": hh3cDot11APUserConnFailCnt,
       "hh3cDot11APUserAuthReqCnt": hh3cDot11APUserAuthReqCnt,
       "hh3cDot11APUserAuthSuccCnt": hh3cDot11APUserAuthSuccCnt,
       "hh3cDot11APUserAuthFailCnt": hh3cDot11APUserAuthFailCnt,
       "hh3cDot11AllUserOnlineTime": hh3cDot11AllUserOnlineTime,
       "hh3cDot11APUserInfoStatisTable": hh3cDot11APUserInfoStatisTable,
       "hh3cDot11APUserInfoStatisEntry": hh3cDot11APUserInfoStatisEntry,
       "hh3cDot11APUserMacAddr": hh3cDot11APUserMacAddr,
       "hh3cDot11APUserIpAddr": hh3cDot11APUserIpAddr,
       "hh3cDot11APUserLoginName": hh3cDot11APUserLoginName,
       "hh3cDot11APUserLoginTime": hh3cDot11APUserLoginTime,
       "hh3cDot11APUserOnlineTime": hh3cDot11APUserOnlineTime,
       "hh3cDot11APUserLoginNameCM": hh3cDot11APUserLoginNameCM,
       "hh3cDot11APUserAuthTypeCM": hh3cDot11APUserAuthTypeCM,
       "hh3cDot11APUserTxPacketCntCM": hh3cDot11APUserTxPacketCntCM,
       "hh3cDot11APUserTxBytesCM": hh3cDot11APUserTxBytesCM,
       "hh3cDot11APUserRxPacketCntCM": hh3cDot11APUserRxPacketCntCM,
       "hh3cDot11APUserRxBytesCM": hh3cDot11APUserRxBytesCM,
       "hh3cDot11APReassocStatis2Table": hh3cDot11APReassocStatis2Table,
       "hh3cDot11APReassocStatis2Entry": hh3cDot11APReassocStatis2Entry,
       "hh3cDot11APReassocFailStatis2Cnt": hh3cDot11APReassocFailStatis2Cnt,
       "hh3cDot11TrafficTable": hh3cDot11TrafficTable,
       "hh3cDot11TrafficEntry": hh3cDot11TrafficEntry,
       "hh3cDot11SSIDIndex": hh3cDot11SSIDIndex,
       "hh3cDot11UpPacketNumber": hh3cDot11UpPacketNumber,
       "hh3cDot11UpByteNumber": hh3cDot11UpByteNumber,
       "hh3cDot11DownPacketNumber": hh3cDot11DownPacketNumber,
       "hh3cDot11DownByteNumber": hh3cDot11DownByteNumber,
       "hh3cDot11APEchoStatisTable": hh3cDot11APEchoStatisTable,
       "hh3cDot11APEchoInfoStatisEntry": hh3cDot11APEchoInfoStatisEntry,
       "hh3cDot11APEchoAvgDelay": hh3cDot11APEchoAvgDelay,
       "hh3cDot11APEchoRequestCnt": hh3cDot11APEchoRequestCnt,
       "hh3cDot11APEchoRespLossCnt": hh3cDot11APEchoRespLossCnt,
       "hh3cDot11APUserSecAuthTypeStatisTable": hh3cDot11APUserSecAuthTypeStatisTable,
       "hh3cDot11APUserSecAuthTypeStatisEntry": hh3cDot11APUserSecAuthTypeStatisEntry,
       "hh3cDot11APPortalOnlineUserNum": hh3cDot11APPortalOnlineUserNum,
       "hh3cDot11APAuthFreeOnlineUserNum": hh3cDot11APAuthFreeOnlineUserNum,
       "hh3cDot11APAssocAuthOnlineUserNum": hh3cDot11APAssocAuthOnlineUserNum,
       "hh3cDot11APMacAuthOnlineUserNum": hh3cDot11APMacAuthOnlineUserNum,
       "hh3cDot11APAllPortalUserOnlineTime": hh3cDot11APAllPortalUserOnlineTime,
       "hh3cDot11APAllAuthFreeUserOnlineTime": hh3cDot11APAllAuthFreeUserOnlineTime,
       "hh3cDot11APAllAssocAuthUserOnlineTime": hh3cDot11APAllAssocAuthUserOnlineTime,
       "hh3cDot11APAllMacAuthUserOnlineTime": hh3cDot11APAllMacAuthUserOnlineTime,
       "hh3cDot11APPortalUserLostCnntCnt": hh3cDot11APPortalUserLostCnntCnt,
       "hh3cDot11APAuthFreeUserLostCnntCnt": hh3cDot11APAuthFreeUserLostCnntCnt,
       "hh3cDot11APAssocAuthUserLostCnntCnt": hh3cDot11APAssocAuthUserLostCnntCnt,
       "hh3cDot11APMacAuthUserLostCnntCnt": hh3cDot11APMacAuthUserLostCnntCnt,
       "hh3cDot11APPortalAuthReqCnt": hh3cDot11APPortalAuthReqCnt,
       "hh3cDot11APAssocAuthReqCnt": hh3cDot11APAssocAuthReqCnt,
       "hh3cDot11APMacAuthReqCnt": hh3cDot11APMacAuthReqCnt,
       "hh3cDot11APPortalAuthSucCnt": hh3cDot11APPortalAuthSucCnt,
       "hh3cDot11APAssocAuthSucCnt": hh3cDot11APAssocAuthSucCnt,
       "hh3cDot11APMacAuthSucCnt": hh3cDot11APMacAuthSucCnt,
       "hh3cDot11APPortalAuthReqFailCnt": hh3cDot11APPortalAuthReqFailCnt,
       "hh3cDot11APAssocAuthReqFailCnt": hh3cDot11APAssocAuthReqFailCnt,
       "hh3cDot11APMacAuthReqFailCnt": hh3cDot11APMacAuthReqFailCnt,
       "hh3cDot11APAutoAuthOnlineUserNumCM": hh3cDot11APAutoAuthOnlineUserNumCM,
       "hh3cDot11APAllAutoAuthUserOnlineTimeCM": hh3cDot11APAllAutoAuthUserOnlineTimeCM,
       "hh3cDot11APAutoAuthUserLostCnntCntCM": hh3cDot11APAutoAuthUserLostCnntCntCM,
       "hh3cDot11APAutoAuthReqCntCM": hh3cDot11APAutoAuthReqCntCM,
       "hh3cDot11APAutoAuthSucCntCM": hh3cDot11APAutoAuthSucCntCM,
       "hh3cDot11APAutoAuthReqFailCntCM": hh3cDot11APAutoAuthReqFailCntCM,
       "hh3cDot11RadioRxStatis64Table": hh3cDot11RadioRxStatis64Table,
       "hh3cDot11RadioRxStatis64Entry": hh3cDot11RadioRxStatis64Entry,
       "hh3cDot11Rx64FrameDupCnt": hh3cDot11Rx64FrameDupCnt,
       "hh3cDot11Rx64FrameCnt": hh3cDot11Rx64FrameCnt,
       "hh3cDot11Rx64UcastFrameCnt": hh3cDot11Rx64UcastFrameCnt,
       "hh3cDot11Rx64BcastFrameCnt": hh3cDot11Rx64BcastFrameCnt,
       "hh3cDot11Rx64McastFrameCnt": hh3cDot11Rx64McastFrameCnt,
       "hh3cDot11Rx64DiscardFrameCnt": hh3cDot11Rx64DiscardFrameCnt,
       "hh3cDot11Rx64FragCnt": hh3cDot11Rx64FragCnt,
       "hh3cDot11Rx64FcsErrCnt": hh3cDot11Rx64FcsErrCnt,
       "hh3cDot11Rx64FrameBytes": hh3cDot11Rx64FrameBytes,
       "hh3cDot11Rx64UcastFrameBytes": hh3cDot11Rx64UcastFrameBytes,
       "hh3cDot11Rx64BcastFrameBytes": hh3cDot11Rx64BcastFrameBytes,
       "hh3cDot11Rx64McastFrameBytes": hh3cDot11Rx64McastFrameBytes,
       "hh3cDot11Rx64DiscardFrameBytes": hh3cDot11Rx64DiscardFrameBytes,
       "hh3cDot11Rx64MgmtFrameCnt": hh3cDot11Rx64MgmtFrameCnt,
       "hh3cDot11Rx64CtrlFrameCnt": hh3cDot11Rx64CtrlFrameCnt,
       "hh3cDot11Rx64DataFrameCnt": hh3cDot11Rx64DataFrameCnt,
       "hh3cDot11Rx64DecryptErrorCnt": hh3cDot11Rx64DecryptErrorCnt,
       "hh3cDot11Rx64AuthenFrameCnt": hh3cDot11Rx64AuthenFrameCnt,
       "hh3cDot11Rx64AssociateFrameCnt": hh3cDot11Rx64AssociateFrameCnt,
       "hh3cDot11Rx64PhyErrorCnt": hh3cDot11Rx64PhyErrorCnt,
       "hh3cDot11Rx64MICErrorCnt": hh3cDot11Rx64MICErrorCnt,
       "hh3cDot11Rx64DataFrameBytes": hh3cDot11Rx64DataFrameBytes,
       "hh3cDot11Rx64PayloadBytes": hh3cDot11Rx64PayloadBytes,
       "hh3cDot11Rx64DataFrameBytesCM": hh3cDot11Rx64DataFrameBytesCM,
       "hh3cDot11RadioTxStatis64Table": hh3cDot11RadioTxStatis64Table,
       "hh3cDot11RadioTxStatis64Entry": hh3cDot11RadioTxStatis64Entry,
       "hh3cDot11Tx64FragCnt": hh3cDot11Tx64FragCnt,
       "hh3cDot11Tx64FailedCnt": hh3cDot11Tx64FailedCnt,
       "hh3cDot11Tx64RetryCnt": hh3cDot11Tx64RetryCnt,
       "hh3cDot11Tx64MultiRetryCnt": hh3cDot11Tx64MultiRetryCnt,
       "hh3cDot11Tx64RtsSuccessCnt": hh3cDot11Tx64RtsSuccessCnt,
       "hh3cDot11Tx64RtsFailCnt": hh3cDot11Tx64RtsFailCnt,
       "hh3cDot11Tx64AckFailCnt": hh3cDot11Tx64AckFailCnt,
       "hh3cDot11Tx64FrameCnt": hh3cDot11Tx64FrameCnt,
       "hh3cDot11Tx64UcastFrameCnt": hh3cDot11Tx64UcastFrameCnt,
       "hh3cDot11Tx64BcastFrameCnt": hh3cDot11Tx64BcastFrameCnt,
       "hh3cDot11Tx64McastFrameCnt": hh3cDot11Tx64McastFrameCnt,
       "hh3cDot11Tx64DiscardFrameCnt": hh3cDot11Tx64DiscardFrameCnt,
       "hh3cDot11Tx64FrameBytes": hh3cDot11Tx64FrameBytes,
       "hh3cDot11Tx64UcastFrameBytes": hh3cDot11Tx64UcastFrameBytes,
       "hh3cDot11Tx64BcastFrameBytes": hh3cDot11Tx64BcastFrameBytes,
       "hh3cDot11Tx64McastFrameBytes": hh3cDot11Tx64McastFrameBytes,
       "hh3cDot11Tx64DiscardFrameBytes": hh3cDot11Tx64DiscardFrameBytes,
       "hh3cDot11Tx64AuthenFrameCnt": hh3cDot11Tx64AuthenFrameCnt,
       "hh3cDot11Tx64AssociateFrameCnt": hh3cDot11Tx64AssociateFrameCnt,
       "hh3cDot11Tx64DataFrameCnt": hh3cDot11Tx64DataFrameCnt,
       "hh3cDot11Tx64DataFrameBytes": hh3cDot11Tx64DataFrameBytes,
       "hh3cDot11Tx64MSDUCnt": hh3cDot11Tx64MSDUCnt,
       "hh3cDot11Tx64DiscardMSDUCnt": hh3cDot11Tx64DiscardMSDUCnt,
       "hh3cDot11Tx64RetryMSDUCnt": hh3cDot11Tx64RetryMSDUCnt,
       "hh3cDot11Tx64PayloadBytes": hh3cDot11Tx64PayloadBytes,
       "hh3cDot11Tx64MgtFrameCnt": hh3cDot11Tx64MgtFrameCnt,
       "hh3cDot11Tx64CtrlFrameCnt": hh3cDot11Tx64CtrlFrameCnt,
       "hh3cDot11Tx64MACErrCnt": hh3cDot11Tx64MACErrCnt,
       "hh3cDot11Tx64ErrFrameCnt": hh3cDot11Tx64ErrFrameCnt,
       "hh3cDot11BSSRxStatis64Table": hh3cDot11BSSRxStatis64Table,
       "hh3cDot11BSSRxStatis64Entry": hh3cDot11BSSRxStatis64Entry,
       "hh3cDot11BSSRx64FrameCnt": hh3cDot11BSSRx64FrameCnt,
       "hh3cDot11BSSRx64FrameBytes": hh3cDot11BSSRx64FrameBytes,
       "hh3cDot11BSSRx64DataFrameCnt": hh3cDot11BSSRx64DataFrameCnt,
       "hh3cDot11BSSRx64DataFrameBytes": hh3cDot11BSSRx64DataFrameBytes,
       "hh3cDot11BSSRx64AssocFrameCnt": hh3cDot11BSSRx64AssocFrameCnt,
       "hh3cDot11BSSRx64PayloadBytes": hh3cDot11BSSRx64PayloadBytes,
       "hh3cDot11BSSRx64UniFrameCnt": hh3cDot11BSSRx64UniFrameCnt,
       "hh3cDot11BSSRx64NonUniFrameCnt": hh3cDot11BSSRx64NonUniFrameCnt,
       "hh3cDot11BSSRx64AuthenFrameCnt": hh3cDot11BSSRx64AuthenFrameCnt,
       "hh3cDot11BSSTxStatis64Table": hh3cDot11BSSTxStatis64Table,
       "hh3cDot11BSSTxStatis64Entry": hh3cDot11BSSTxStatis64Entry,
       "hh3cDot11BSSTx64FrameCnt": hh3cDot11BSSTx64FrameCnt,
       "hh3cDot11BSSTx64FrameBytes": hh3cDot11BSSTx64FrameBytes,
       "hh3cDot11BSSTx64DataFrameCnt": hh3cDot11BSSTx64DataFrameCnt,
       "hh3cDot11BSSTx64DataFrameBytes": hh3cDot11BSSTx64DataFrameBytes,
       "hh3cDot11BSSTx64AssocFrameCnt": hh3cDot11BSSTx64AssocFrameCnt,
       "hh3cDot11BSSTx64PayloadBytes": hh3cDot11BSSTx64PayloadBytes,
       "hh3cDot11BSSTx64RetryCnt": hh3cDot11BSSTx64RetryCnt,
       "hh3cDot11BSSTx64UniFrameCnt": hh3cDot11BSSTx64UniFrameCnt,
       "hh3cDot11BSSTx64NonUniFrameCnt": hh3cDot11BSSTx64NonUniFrameCnt,
       "hh3cDot11BSSTx64AuthenFrameCnt": hh3cDot11BSSTx64AuthenFrameCnt,
       "hh3cDot11APPacketMCSRateStatis2Table": hh3cDot11APPacketMCSRateStatis2Table,
       "hh3cDot11APPacketMCSRateStatis2Entry": hh3cDot11APPacketMCSRateStatis2Entry,
       "hh3cDot11APPacketMCS2Rate": hh3cDot11APPacketMCS2Rate,
       "hh3cDot11APRXPacketMCSRate2Count": hh3cDot11APRXPacketMCSRate2Count,
       "hh3cDot11APTXPacketMCSRate2Count": hh3cDot11APTXPacketMCSRate2Count,
       "hh3cDot11APUserSecAuthStatisCMTable": hh3cDot11APUserSecAuthStatisCMTable,
       "hh3cDot11APUserSecAuthStatisCMEntry": hh3cDot11APUserSecAuthStatisCMEntry,
       "hh3cDot11APUserConnFailCntCM": hh3cDot11APUserConnFailCntCM,
       "hh3cDot11APUserAuthReqCntCM": hh3cDot11APUserAuthReqCntCM,
       "hh3cDot11APUserAuthSuccCntCM": hh3cDot11APUserAuthSuccCntCM,
       "hh3cDot11APUserAuthFailCntCM": hh3cDot11APUserAuthFailCntCM,
       "hh3cDot11AllUserOnlineTimeCM": hh3cDot11AllUserOnlineTimeCM,
       "hh3cDot11APUserInfoStatis2CMTable": hh3cDot11APUserInfoStatis2CMTable,
       "hh3cDot11APUserInfoStatis2CMEntry": hh3cDot11APUserInfoStatis2CMEntry,
       "hh3cDot11APUserMacAddr2CM": hh3cDot11APUserMacAddr2CM,
       "hh3cDot11APUserIpAddr2CM": hh3cDot11APUserIpAddr2CM,
       "hh3cDot11APUserLoginName2CM": hh3cDot11APUserLoginName2CM,
       "hh3cDot11APUserLoginTime2CM": hh3cDot11APUserLoginTime2CM,
       "hh3cDot11APUserOnlineTime2CM": hh3cDot11APUserOnlineTime2CM,
       "hh3cDot11APUserAuthType2CM": hh3cDot11APUserAuthType2CM,
       "hh3cDot11APUserTxPacketCnt2CM": hh3cDot11APUserTxPacketCnt2CM,
       "hh3cDot11APUserTxBytes2CM": hh3cDot11APUserTxBytes2CM,
       "hh3cDot11APUserRxPacketCnt2CM": hh3cDot11APUserRxPacketCnt2CM,
       "hh3cDot11APUserRxBytes2CM": hh3cDot11APUserRxBytes2CM,
       "hh3cDot11APMtNotifyGroup": hh3cDot11APMtNotifyGroup,
       "hh3cDot11APMtTraps": hh3cDot11APMtTraps,
       "hh3cDot11APMtWorkModeChgTrap": hh3cDot11APMtWorkModeChgTrap,
       "hh3cDot11APMtCfgErrorTrap": hh3cDot11APMtCfgErrorTrap,
       "hh3cDot11APMtRadioFailTrap": hh3cDot11APMtRadioFailTrap,
       "hh3cDot11APMtRadioFailRecoverTrap": hh3cDot11APMtRadioFailRecoverTrap,
       "hh3cDot11APMtRdoChanlChgTrap": hh3cDot11APMtRdoChanlChgTrap,
       "hh3cDot11APMtTimeSynFail": hh3cDot11APMtTimeSynFail,
       "hh3cDot11APMtChlIntfDetected": hh3cDot11APMtChlIntfDetected,
       "hh3cDot11APMtIntfAPDetected": hh3cDot11APMtIntfAPDetected,
       "hh3cDot11APMtIntfStaDetected": hh3cDot11APMtIntfStaDetected,
       "hh3cDot11APMtIPChange": hh3cDot11APMtIPChange,
       "hh3cDot11APFlashWriteFailure": hh3cDot11APFlashWriteFailure,
       "hh3cDot11APSysReboot": hh3cDot11APSysReboot,
       "hh3cDot11APMtAvailChlTooLow": hh3cDot11APMtAvailChlTooLow,
       "hh3cDot11APImgDwldSuccess": hh3cDot11APImgDwldSuccess,
       "hh3cDot11APInterfDetectedTrap": hh3cDot11APInterfDetectedTrap,
       "hh3cDot11APInterfClearTrap": hh3cDot11APInterfClearTrap,
       "hh3cDot11StaInterfDetectedTrap": hh3cDot11StaInterfDetectedTrap,
       "hh3cDot11StaInterfClearTrap": hh3cDot11StaInterfClearTrap,
       "hh3cDot11OtherDevIntDetectedTrap": hh3cDot11OtherDevIntDetectedTrap,
       "hh3cDot11OtherDevIntClearTrap": hh3cDot11OtherDevIntClearTrap,
       "hh3cDot11APModuleTroubleTrap": hh3cDot11APModuleTroubleTrap,
       "hh3cDot11APModuleTroubleClearTrap": hh3cDot11APModuleTroubleClearTrap,
       "hh3cDot11APRadioDownTrap": hh3cDot11APRadioDownTrap,
       "hh3cDot11APRadioDownRecovTrap": hh3cDot11APRadioDownRecovTrap,
       "hh3cDot11APStaFullTrap": hh3cDot11APStaFullTrap,
       "hh3cDot11APStaFullRecoverTrap": hh3cDot11APStaFullRecoverTrap,
       "hh3cDot11DFSFreeCntBelowThrRecov": hh3cDot11DFSFreeCntBelowThrRecov,
       "hh3cDot11APCpuUsageHigh": hh3cDot11APCpuUsageHigh,
       "hh3cDot11APCpuUsageHighRecover": hh3cDot11APCpuUsageHighRecover,
       "hh3cDot11APMemUsageHigh": hh3cDot11APMemUsageHigh,
       "hh3cDot11APMemUsageHighRecover": hh3cDot11APMemUsageHighRecover,
       "hh3cDot11APTrapUserCntExceedThre": hh3cDot11APTrapUserCntExceedThre,
       "hh3cDot11APMtDetectedIntfAP": hh3cDot11APMtDetectedIntfAP,
       "hh3cDot11APMtDetectedIntfSTA": hh3cDot11APMtDetectedIntfSTA,
       "hh3cDot11APMtDetectedIntfOtherDev": hh3cDot11APMtDetectedIntfOtherDev,
       "hh3cDot11DetcAdjChlIntfAP": hh3cDot11DetcAdjChlIntfAP,
       "hh3cDot11DetcAdjChlIntfAPClear": hh3cDot11DetcAdjChlIntfAPClear,
       "hh3cDot11APPowerOffTrap": hh3cDot11APPowerOffTrap,
       "hh3cDot11APPowerOnTrap": hh3cDot11APPowerOnTrap,
       "hh3cDot11UpLinkSwitchTrap": hh3cDot11UpLinkSwitchTrap,
       "hh3cDot11APMtTrapVarObjects": hh3cDot11APMtTrapVarObjects,
       "hh3cDot11APMtTrapCfgErrReason": hh3cDot11APMtTrapCfgErrReason,
       "hh3cDot11APMtTrapRadioFailReason": hh3cDot11APMtTrapRadioFailReason,
       "hh3cDot11APMtTrapOldChannel": hh3cDot11APMtTrapOldChannel,
       "hh3cDot11APMtTrapNewChannel": hh3cDot11APMtTrapNewChannel,
       "hh3cDot11APChannelChgMode": hh3cDot11APChannelChgMode,
       "hh3cDot11APChgWorkMode": hh3cDot11APChgWorkMode,
       "hh3cDot11APIntfDevMACAddress": hh3cDot11APIntfDevMACAddress,
       "hh3cDot11APMtTrapOldIPAddr": hh3cDot11APMtTrapOldIPAddr,
       "hh3cDot11CurrInterfDetectedNum": hh3cDot11CurrInterfDetectedNum,
       "hh3cDot11StaFullReason": hh3cDot11StaFullReason,
       "hh3cDot11StaLimitNumber": hh3cDot11StaLimitNumber,
       "hh3cDot11APRadioDownReason": hh3cDot11APRadioDownReason,
       "hh3cDot11InterfMacList": hh3cDot11InterfMacList,
       "hh3cDot11APTrapUserCnt": hh3cDot11APTrapUserCnt,
       "hh3cDot11APTrapUserThreshold": hh3cDot11APTrapUserThreshold,
       "hh3cDot11APMtChanlChgCount": hh3cDot11APMtChanlChgCount,
       "hh3cDot11APMtFormerApVersion": hh3cDot11APMtFormerApVersion,
       "hh3cDot11APMtAPID": hh3cDot11APMtAPID,
       "hh3cDot11APMtRadioID": hh3cDot11APMtRadioID,
       "hh3cDot11APMtChannel": hh3cDot11APMtChannel,
       "hh3cDot11APMtInterfMacAdd": hh3cDot11APMtInterfMacAdd,
       "hh3cDot11APMtAdjChannel": hh3cDot11APMtAdjChannel,
       "hh3cDot11APMtFirstTrapTime": hh3cDot11APMtFirstTrapTime,
       "hh3cDot11APMtTrapAPMacAddress": hh3cDot11APMtTrapAPMacAddress,
       "hh3cDot11APMtUpLinkSwitchInfo": hh3cDot11APMtUpLinkSwitchInfo,
       "hh3cDot11APMtUpLinkSwitchTime": hh3cDot11APMtUpLinkSwitchTime,
       "hh3cDot11APMtOldCellId": hh3cDot11APMtOldCellId,
       "hh3cDot11APMtCurCellId": hh3cDot11APMtCurCellId,
       "hh3cDot11APMtOldBand": hh3cDot11APMtOldBand,
       "hh3cDot11APMtActiveBand": hh3cDot11APMtActiveBand}
)
