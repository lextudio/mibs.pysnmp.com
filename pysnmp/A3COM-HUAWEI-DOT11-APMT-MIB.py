# SNMP MIB module (A3COM-HUAWEI-DOT11-APMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-APMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:36 2024
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

(H3cDot11ChannelScopeType,
 H3cDot11MACModeType,
 H3cDot11NotifyReasonType,
 H3cDot11ObjectIDType,
 H3cDot11RFModeType,
 H3cDot11RadioElementIndex,
 H3cDot11RadioScopeType,
 H3cDot11SSIDStringType,
 H3cDot11ServicePolicyIDType,
 H3cDot11TxPwrLevelScopeType,
 h3cDot11,
 h3cDot11APElementIndex) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    "H3cDot11ChannelScopeType",
    "H3cDot11MACModeType",
    "H3cDot11NotifyReasonType",
    "H3cDot11ObjectIDType",
    "H3cDot11RFModeType",
    "H3cDot11RadioElementIndex",
    "H3cDot11RadioScopeType",
    "H3cDot11SSIDStringType",
    "H3cDot11ServicePolicyIDType",
    "H3cDot11TxPwrLevelScopeType",
    "h3cDot11",
    "h3cDot11APElementIndex")

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

h3cDot11APMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2)
)
h3cDot11APMT.setRevisions(
        ("2010-10-11 18:00",
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

_H3cDot11APObjectGroup_ObjectIdentity = ObjectIdentity
h3cDot11APObjectGroup = _H3cDot11APObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1)
)
_H3cDot11APObjectStatusTable_Object = MibTable
h3cDot11APObjectStatusTable = _H3cDot11APObjectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11APObjectStatusTable.setStatus("current")
_H3cDot11APObjectStatusEntry_Object = MibTableRow
h3cDot11APObjectStatusEntry = _H3cDot11APObjectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1)
)
h3cDot11APObjectStatusEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
)
if mibBuilder.loadTexts:
    h3cDot11APObjectStatusEntry.setStatus("current")
_H3cDot11APID_Type = H3cDot11ObjectIDType
_H3cDot11APID_Object = MibTableColumn
h3cDot11APID = _H3cDot11APID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 1),
    _H3cDot11APID_Type()
)
h3cDot11APID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APID.setStatus("current")
_H3cDot11APIPAddress_Type = IpAddress
_H3cDot11APIPAddress_Object = MibTableColumn
h3cDot11APIPAddress = _H3cDot11APIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 2),
    _H3cDot11APIPAddress_Type()
)
h3cDot11APIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIPAddress.setStatus("current")
_H3cDot11APMacAddress_Type = MacAddress
_H3cDot11APMacAddress_Object = MibTableColumn
h3cDot11APMacAddress = _H3cDot11APMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 3),
    _H3cDot11APMacAddress_Type()
)
h3cDot11APMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMacAddress.setStatus("current")


class _H3cDot11APOperationStatus_Type(Integer32):
    """Custom type h3cDot11APOperationStatus based on Integer32"""
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


_H3cDot11APOperationStatus_Type.__name__ = "Integer32"
_H3cDot11APOperationStatus_Object = MibTableColumn
h3cDot11APOperationStatus = _H3cDot11APOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 4),
    _H3cDot11APOperationStatus_Type()
)
h3cDot11APOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APOperationStatus.setStatus("current")
_H3cDot11APTemplateNameOfAP_Type = OctetString
_H3cDot11APTemplateNameOfAP_Object = MibTableColumn
h3cDot11APTemplateNameOfAP = _H3cDot11APTemplateNameOfAP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 5),
    _H3cDot11APTemplateNameOfAP_Type()
)
h3cDot11APTemplateNameOfAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTemplateNameOfAP.setStatus("current")
_H3cDot11APReset_Type = TruthValue
_H3cDot11APReset_Object = MibTableColumn
h3cDot11APReset = _H3cDot11APReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 6),
    _H3cDot11APReset_Type()
)
h3cDot11APReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APReset.setStatus("current")


class _H3cDot11APCpuUsage_Type(Integer32):
    """Custom type h3cDot11APCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCpuUsage_Type.__name__ = "Integer32"
_H3cDot11APCpuUsage_Object = MibTableColumn
h3cDot11APCpuUsage = _H3cDot11APCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 7),
    _H3cDot11APCpuUsage_Type()
)
h3cDot11APCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCpuUsage.setUnits("onepercent")


class _H3cDot11APConnectionType_Type(Integer32):
    """Custom type h3cDot11APConnectionType based on Integer32"""
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


_H3cDot11APConnectionType_Type.__name__ = "Integer32"
_H3cDot11APConnectionType_Object = MibTableColumn
h3cDot11APConnectionType = _H3cDot11APConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 8),
    _H3cDot11APConnectionType_Type()
)
h3cDot11APConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APConnectionType.setStatus("current")
_H3cDot11APLastImgDownloadTime_Type = DateAndTime
_H3cDot11APLastImgDownloadTime_Object = MibTableColumn
h3cDot11APLastImgDownloadTime = _H3cDot11APLastImgDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 9),
    _H3cDot11APLastImgDownloadTime_Type()
)
h3cDot11APLastImgDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APLastImgDownloadTime.setStatus("current")
_H3cDot11APIPv6Address_Type = OctetString
_H3cDot11APIPv6Address_Object = MibTableColumn
h3cDot11APIPv6Address = _H3cDot11APIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 10),
    _H3cDot11APIPv6Address_Type()
)
h3cDot11APIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIPv6Address.setStatus("current")
_H3cDot11APLastRegisterTime_Type = DateAndTime
_H3cDot11APLastRegisterTime_Object = MibTableColumn
h3cDot11APLastRegisterTime = _H3cDot11APLastRegisterTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 1, 1, 11),
    _H3cDot11APLastRegisterTime_Type()
)
h3cDot11APLastRegisterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APLastRegisterTime.setStatus("current")
_H3cDot11APObjectTable_Object = MibTable
h3cDot11APObjectTable = _H3cDot11APObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11APObjectTable.setStatus("current")
_H3cDot11APObjectEntry_Object = MibTableRow
h3cDot11APObjectEntry = _H3cDot11APObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1)
)
h3cDot11APObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APObjID"),
)
if mibBuilder.loadTexts:
    h3cDot11APObjectEntry.setStatus("current")
_H3cDot11APObjID_Type = H3cDot11ObjectIDType
_H3cDot11APObjID_Object = MibTableColumn
h3cDot11APObjID = _H3cDot11APObjID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 1),
    _H3cDot11APObjID_Type()
)
h3cDot11APObjID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APObjID.setStatus("current")
_H3cDot11CurrAPIPAddress_Type = IpAddress
_H3cDot11CurrAPIPAddress_Object = MibTableColumn
h3cDot11CurrAPIPAddress = _H3cDot11CurrAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 2),
    _H3cDot11CurrAPIPAddress_Type()
)
h3cDot11CurrAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPIPAddress.setStatus("current")
_H3cDot11CurrAPMacAddress_Type = MacAddress
_H3cDot11CurrAPMacAddress_Object = MibTableColumn
h3cDot11CurrAPMacAddress = _H3cDot11CurrAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 3),
    _H3cDot11CurrAPMacAddress_Type()
)
h3cDot11CurrAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMacAddress.setStatus("current")
_H3cDot11CurrACPortIndex_Type = Integer32
_H3cDot11CurrACPortIndex_Object = MibTableColumn
h3cDot11CurrACPortIndex = _H3cDot11CurrACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 4),
    _H3cDot11CurrACPortIndex_Type()
)
h3cDot11CurrACPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrACPortIndex.setStatus("current")
_H3cDot11CurrAPMACMode_Type = H3cDot11MACModeType
_H3cDot11CurrAPMACMode_Object = MibTableColumn
h3cDot11CurrAPMACMode = _H3cDot11CurrAPMACMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 5),
    _H3cDot11CurrAPMACMode_Type()
)
h3cDot11CurrAPMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMACMode.setStatus("current")
_H3cDot11CurrAPTemplateName_Type = OctetString
_H3cDot11CurrAPTemplateName_Object = MibTableColumn
h3cDot11CurrAPTemplateName = _H3cDot11CurrAPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 6),
    _H3cDot11CurrAPTemplateName_Type()
)
h3cDot11CurrAPTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPTemplateName.setStatus("current")
_H3cDot11CurrAPStationAssocCount_Type = Integer32
_H3cDot11CurrAPStationAssocCount_Object = MibTableColumn
h3cDot11CurrAPStationAssocCount = _H3cDot11CurrAPStationAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 7),
    _H3cDot11CurrAPStationAssocCount_Type()
)
h3cDot11CurrAPStationAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPStationAssocCount.setStatus("current")
_H3cDot11CurrAPName_Type = OctetString
_H3cDot11CurrAPName_Object = MibTableColumn
h3cDot11CurrAPName = _H3cDot11CurrAPName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 8),
    _H3cDot11CurrAPName_Type()
)
h3cDot11CurrAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPName.setStatus("current")
_H3cDot11CurrAPModelName_Type = OctetString
_H3cDot11CurrAPModelName_Object = MibTableColumn
h3cDot11CurrAPModelName = _H3cDot11CurrAPModelName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 9),
    _H3cDot11CurrAPModelName_Type()
)
h3cDot11CurrAPModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPModelName.setStatus("current")
_H3cDot11CurrAPImageName_Type = OctetString
_H3cDot11CurrAPImageName_Object = MibTableColumn
h3cDot11CurrAPImageName = _H3cDot11CurrAPImageName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 10),
    _H3cDot11CurrAPImageName_Type()
)
h3cDot11CurrAPImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPImageName.setStatus("current")
_H3cDot11CurrAPSoftwareVersion_Type = OctetString
_H3cDot11CurrAPSoftwareVersion_Object = MibTableColumn
h3cDot11CurrAPSoftwareVersion = _H3cDot11CurrAPSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 11),
    _H3cDot11CurrAPSoftwareVersion_Type()
)
h3cDot11CurrAPSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPSoftwareVersion.setStatus("current")
_H3cDot11CurrAPIPNetMask_Type = IpAddress
_H3cDot11CurrAPIPNetMask_Object = MibTableColumn
h3cDot11CurrAPIPNetMask = _H3cDot11CurrAPIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 12),
    _H3cDot11CurrAPIPNetMask_Type()
)
h3cDot11CurrAPIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPIPNetMask.setStatus("current")
_H3cDot11CurrRadioModeSupport_Type = Integer32
_H3cDot11CurrRadioModeSupport_Object = MibTableColumn
h3cDot11CurrRadioModeSupport = _H3cDot11CurrRadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 13),
    _H3cDot11CurrRadioModeSupport_Type()
)
h3cDot11CurrRadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrRadioModeSupport.setStatus("current")
_H3cDot11CurrIfNumber_Type = Integer32
_H3cDot11CurrIfNumber_Object = MibTableColumn
h3cDot11CurrIfNumber = _H3cDot11CurrIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 14),
    _H3cDot11CurrIfNumber_Type()
)
h3cDot11CurrIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrIfNumber.setStatus("current")
_H3cDot11CurrAPElementID_Type = Integer32
_H3cDot11CurrAPElementID_Object = MibTableColumn
h3cDot11CurrAPElementID = _H3cDot11CurrAPElementID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 15),
    _H3cDot11CurrAPElementID_Type()
)
h3cDot11CurrAPElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPElementID.setStatus("current")


class _H3cDot11CurrAPMode_Type(Integer32):
    """Custom type h3cDot11CurrAPMode based on Integer32"""
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


_H3cDot11CurrAPMode_Type.__name__ = "Integer32"
_H3cDot11CurrAPMode_Object = MibTableColumn
h3cDot11CurrAPMode = _H3cDot11CurrAPMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 16),
    _H3cDot11CurrAPMode_Type()
)
h3cDot11CurrAPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMode.setStatus("current")
_H3cDot11CurrAPIPv6Address_Type = OctetString
_H3cDot11CurrAPIPv6Address_Object = MibTableColumn
h3cDot11CurrAPIPv6Address = _H3cDot11CurrAPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 17),
    _H3cDot11CurrAPIPv6Address_Type()
)
h3cDot11CurrAPIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPIPv6Address.setStatus("current")
_H3cDot11CurrAPSSIDNumber_Type = Integer32
_H3cDot11CurrAPSSIDNumber_Object = MibTableColumn
h3cDot11CurrAPSSIDNumber = _H3cDot11CurrAPSSIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 18),
    _H3cDot11CurrAPSSIDNumber_Type()
)
h3cDot11CurrAPSSIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPSSIDNumber.setStatus("current")
_H3cDot11CurrAPManufacturer_Type = OctetString
_H3cDot11CurrAPManufacturer_Object = MibTableColumn
h3cDot11CurrAPManufacturer = _H3cDot11CurrAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 19),
    _H3cDot11CurrAPManufacturer_Type()
)
h3cDot11CurrAPManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPManufacturer.setStatus("current")
_H3cDot11CurrAPMemorySize_Type = Integer32
_H3cDot11CurrAPMemorySize_Object = MibTableColumn
h3cDot11CurrAPMemorySize = _H3cDot11CurrAPMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 20),
    _H3cDot11CurrAPMemorySize_Type()
)
h3cDot11CurrAPMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMemorySize.setUnits("kbytes")
_H3cDot11CurrAPMemSizeInBytes_Type = Integer32
_H3cDot11CurrAPMemSizeInBytes_Object = MibTableColumn
h3cDot11CurrAPMemSizeInBytes = _H3cDot11CurrAPMemSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 21),
    _H3cDot11CurrAPMemSizeInBytes_Type()
)
h3cDot11CurrAPMemSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMemSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CurrAPMemSizeInBytes.setUnits("bytes")
_H3cDot11CurrAPFlashSize_Type = Integer32
_H3cDot11CurrAPFlashSize_Object = MibTableColumn
h3cDot11CurrAPFlashSize = _H3cDot11CurrAPFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 22),
    _H3cDot11CurrAPFlashSize_Type()
)
h3cDot11CurrAPFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CurrAPFlashSize.setUnits("Kbytes")
_H3cDot11CurrAPFlashSizeInBytes_Type = Integer32
_H3cDot11CurrAPFlashSizeInBytes_Object = MibTableColumn
h3cDot11CurrAPFlashSizeInBytes = _H3cDot11CurrAPFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 23),
    _H3cDot11CurrAPFlashSizeInBytes_Type()
)
h3cDot11CurrAPFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CurrAPFlashSizeInBytes.setUnits("bytes")
_H3cDot11CurrAPReleasedVersion_Type = OctetString
_H3cDot11CurrAPReleasedVersion_Object = MibTableColumn
h3cDot11CurrAPReleasedVersion = _H3cDot11CurrAPReleasedVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 24),
    _H3cDot11CurrAPReleasedVersion_Type()
)
h3cDot11CurrAPReleasedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrAPReleasedVersion.setStatus("current")
_H3cDot11CurrRadioModeSupport2_Type = Integer32
_H3cDot11CurrRadioModeSupport2_Object = MibTableColumn
h3cDot11CurrRadioModeSupport2 = _H3cDot11CurrRadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 2, 1, 25),
    _H3cDot11CurrRadioModeSupport2_Type()
)
h3cDot11CurrRadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrRadioModeSupport2.setStatus("current")
_H3cDot11APRadioTable_Object = MibTable
h3cDot11APRadioTable = _H3cDot11APRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11APRadioTable.setStatus("current")
_H3cDot11APRadioEntry_Object = MibTableRow
h3cDot11APRadioEntry = _H3cDot11APRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1)
)
h3cDot11APRadioEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11APRadioEntry.setStatus("current")
_H3cDot11CurAPID_Type = H3cDot11ObjectIDType
_H3cDot11CurAPID_Object = MibTableColumn
h3cDot11CurAPID = _H3cDot11CurAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 1),
    _H3cDot11CurAPID_Type()
)
h3cDot11CurAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11CurAPID.setStatus("current")
_H3cDot11RadioID_Type = H3cDot11RadioScopeType
_H3cDot11RadioID_Object = MibTableColumn
h3cDot11RadioID = _H3cDot11RadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 2),
    _H3cDot11RadioID_Type()
)
h3cDot11RadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11RadioID.setStatus("current")
_H3cDot11AdminStatus_Type = TruthValue
_H3cDot11AdminStatus_Object = MibTableColumn
h3cDot11AdminStatus = _H3cDot11AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 3),
    _H3cDot11AdminStatus_Type()
)
h3cDot11AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AdminStatus.setStatus("current")
_H3cDot11OperStatus_Type = TruthValue
_H3cDot11OperStatus_Object = MibTableColumn
h3cDot11OperStatus = _H3cDot11OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 4),
    _H3cDot11OperStatus_Type()
)
h3cDot11OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11OperStatus.setStatus("current")
_H3cDot11Channel_Type = H3cDot11ChannelScopeType
_H3cDot11Channel_Object = MibTableColumn
h3cDot11Channel = _H3cDot11Channel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 5),
    _H3cDot11Channel_Type()
)
h3cDot11Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11Channel.setStatus("current")
_H3cDot11TxPowerLevel_Type = H3cDot11TxPwrLevelScopeType
_H3cDot11TxPowerLevel_Object = MibTableColumn
h3cDot11TxPowerLevel = _H3cDot11TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 6),
    _H3cDot11TxPowerLevel_Type()
)
h3cDot11TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11TxPowerLevel.setUnits("dbm")
_H3cDot11APRadioIfIndex_Type = Integer32
_H3cDot11APRadioIfIndex_Object = MibTableColumn
h3cDot11APRadioIfIndex = _H3cDot11APRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 7),
    _H3cDot11APRadioIfIndex_Type()
)
h3cDot11APRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APRadioIfIndex.setStatus("current")
_H3cDot11AntennaGain_Type = Integer32
_H3cDot11AntennaGain_Object = MibTableColumn
h3cDot11AntennaGain = _H3cDot11AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 8),
    _H3cDot11AntennaGain_Type()
)
h3cDot11AntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AntennaGain.setUnits("dBi")
_H3cDot11MaxBandwidth_Type = Integer32
_H3cDot11MaxBandwidth_Object = MibTableColumn
h3cDot11MaxBandwidth = _H3cDot11MaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 9),
    _H3cDot11MaxBandwidth_Type()
)
h3cDot11MaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11MaxBandwidth.setUnits("Mbps")
_H3cDot11ResourceUseRatio_Type = Integer32
_H3cDot11ResourceUseRatio_Object = MibTableColumn
h3cDot11ResourceUseRatio = _H3cDot11ResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 10),
    _H3cDot11ResourceUseRatio_Type()
)
h3cDot11ResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ResourceUseRatio.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11ResourceUseRatio.setUnits("onepercent")
_H3cDot11RadioModeSupport_Type = Unsigned32
_H3cDot11RadioModeSupport_Object = MibTableColumn
h3cDot11RadioModeSupport = _H3cDot11RadioModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 11),
    _H3cDot11RadioModeSupport_Type()
)
h3cDot11RadioModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioModeSupport.setStatus("current")


class _H3cDot11TxPowerLevel2_Type(Integer32):
    """Custom type h3cDot11TxPowerLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_H3cDot11TxPowerLevel2_Type.__name__ = "Integer32"
_H3cDot11TxPowerLevel2_Object = MibTableColumn
h3cDot11TxPowerLevel2 = _H3cDot11TxPowerLevel2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 12),
    _H3cDot11TxPowerLevel2_Type()
)
h3cDot11TxPowerLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxPowerLevel2.setStatus("current")
_H3cDot11PowerMgmtStatus_Type = TruthValue
_H3cDot11PowerMgmtStatus_Object = MibTableColumn
h3cDot11PowerMgmtStatus = _H3cDot11PowerMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 13),
    _H3cDot11PowerMgmtStatus_Type()
)
h3cDot11PowerMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PowerMgmtStatus.setStatus("current")
_H3cDot11ChannelSwitchTimes_Type = Counter32
_H3cDot11ChannelSwitchTimes_Object = MibTableColumn
h3cDot11ChannelSwitchTimes = _H3cDot11ChannelSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 14),
    _H3cDot11ChannelSwitchTimes_Type()
)
h3cDot11ChannelSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ChannelSwitchTimes.setStatus("current")
_H3cDot11AntennaType_Type = OctetString
_H3cDot11AntennaType_Object = MibTableColumn
h3cDot11AntennaType = _H3cDot11AntennaType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 15),
    _H3cDot11AntennaType_Type()
)
h3cDot11AntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AntennaType.setStatus("current")
_H3cDot11DiversitySelectionRx_Type = TruthValue
_H3cDot11DiversitySelectionRx_Object = MibTableColumn
h3cDot11DiversitySelectionRx = _H3cDot11DiversitySelectionRx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 16),
    _H3cDot11DiversitySelectionRx_Type()
)
h3cDot11DiversitySelectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DiversitySelectionRx.setStatus("current")
_H3cDot11MaxTxPwrLvl_Type = OctetString
_H3cDot11MaxTxPwrLvl_Object = MibTableColumn
h3cDot11MaxTxPwrLvl = _H3cDot11MaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 17),
    _H3cDot11MaxTxPwrLvl_Type()
)
h3cDot11MaxTxPwrLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MaxTxPwrLvl.setStatus("current")
_H3cDot11PwrAttRange_Type = Integer32
_H3cDot11PwrAttRange_Object = MibTableColumn
h3cDot11PwrAttRange = _H3cDot11PwrAttRange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 18),
    _H3cDot11PwrAttRange_Type()
)
h3cDot11PwrAttRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11PwrAttRange.setStatus("current")
_H3cDot11AvgRxSignalStrength_Type = Integer32
_H3cDot11AvgRxSignalStrength_Object = MibTableColumn
h3cDot11AvgRxSignalStrength = _H3cDot11AvgRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 19),
    _H3cDot11AvgRxSignalStrength_Type()
)
h3cDot11AvgRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AvgRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AvgRxSignalStrength.setUnits("dBm")
_H3cDot11HighestRxSignalStrength_Type = Integer32
_H3cDot11HighestRxSignalStrength_Object = MibTableColumn
h3cDot11HighestRxSignalStrength = _H3cDot11HighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 20),
    _H3cDot11HighestRxSignalStrength_Type()
)
h3cDot11HighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11HighestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11HighestRxSignalStrength.setUnits("dBm")
_H3cDot11LowestRxSignalStrength_Type = Integer32
_H3cDot11LowestRxSignalStrength_Object = MibTableColumn
h3cDot11LowestRxSignalStrength = _H3cDot11LowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 21),
    _H3cDot11LowestRxSignalStrength_Type()
)
h3cDot11LowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LowestRxSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11LowestRxSignalStrength.setUnits("dBm")
_H3cDot11RadioIfUpdownTimes_Type = Counter32
_H3cDot11RadioIfUpdownTimes_Object = MibTableColumn
h3cDot11RadioIfUpdownTimes = _H3cDot11RadioIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 22),
    _H3cDot11RadioIfUpdownTimes_Type()
)
h3cDot11RadioIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioIfUpdownTimes.setStatus("current")
_H3cDot11RadioIfLastChange_Type = TimeTicks
_H3cDot11RadioIfLastChange_Object = MibTableColumn
h3cDot11RadioIfLastChange = _H3cDot11RadioIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 23),
    _H3cDot11RadioIfLastChange_Type()
)
h3cDot11RadioIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioIfLastChange.setStatus("current")
_H3cDot11RadioModeSupport2_Type = Unsigned32
_H3cDot11RadioModeSupport2_Object = MibTableColumn
h3cDot11RadioModeSupport2 = _H3cDot11RadioModeSupport2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 3, 1, 24),
    _H3cDot11RadioModeSupport2_Type()
)
h3cDot11RadioModeSupport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioModeSupport2.setStatus("current")
_H3cDot11APBSSTable_Object = MibTable
h3cDot11APBSSTable = _H3cDot11APBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot11APBSSTable.setStatus("current")
_H3cDot11APBSSEntry_Object = MibTableRow
h3cDot11APBSSEntry = _H3cDot11APBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1)
)
h3cDot11APBSSEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    h3cDot11APBSSEntry.setStatus("current")
_H3cDot11WlanID_Type = Integer32
_H3cDot11WlanID_Object = MibTableColumn
h3cDot11WlanID = _H3cDot11WlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 1),
    _H3cDot11WlanID_Type()
)
h3cDot11WlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WlanID.setStatus("current")
_H3cDot11BSSID_Type = MacAddress
_H3cDot11BSSID_Object = MibTableColumn
h3cDot11BSSID = _H3cDot11BSSID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 2),
    _H3cDot11BSSID_Type()
)
h3cDot11BSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSID.setStatus("current")
_H3cDot11CurrSvcPolicyID_Type = H3cDot11ServicePolicyIDType
_H3cDot11CurrSvcPolicyID_Object = MibTableColumn
h3cDot11CurrSvcPolicyID = _H3cDot11CurrSvcPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 3),
    _H3cDot11CurrSvcPolicyID_Type()
)
h3cDot11CurrSvcPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrSvcPolicyID.setStatus("current")
_H3cDot11SSID_Type = OctetString
_H3cDot11SSID_Object = MibTableColumn
h3cDot11SSID = _H3cDot11SSID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 4),
    _H3cDot11SSID_Type()
)
h3cDot11SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SSID.setStatus("current")
_H3cDot11CurrSSIDResourceUseRatio_Type = Integer32
_H3cDot11CurrSSIDResourceUseRatio_Object = MibTableColumn
h3cDot11CurrSSIDResourceUseRatio = _H3cDot11CurrSSIDResourceUseRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 5),
    _H3cDot11CurrSSIDResourceUseRatio_Type()
)
h3cDot11CurrSSIDResourceUseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CurrSSIDResourceUseRatio.setStatus("current")
_H3cDot11APEssVlanId_Type = Integer32
_H3cDot11APEssVlanId_Object = MibTableColumn
h3cDot11APEssVlanId = _H3cDot11APEssVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 4, 1, 6),
    _H3cDot11APEssVlanId_Type()
)
h3cDot11APEssVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APEssVlanId.setStatus("current")
_H3cDot11APModelTable_Object = MibTable
h3cDot11APModelTable = _H3cDot11APModelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot11APModelTable.setStatus("current")
_H3cDot11APModelEntry_Object = MibTableRow
h3cDot11APModelEntry = _H3cDot11APModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1)
)
h3cDot11APModelEntry.setIndexNames(
    (1, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APModelAlias"),
)
if mibBuilder.loadTexts:
    h3cDot11APModelEntry.setStatus("current")


class _H3cDot11APModelAlias_Type(OctetString):
    """Custom type h3cDot11APModelAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11APModelAlias_Type.__name__ = "OctetString"
_H3cDot11APModelAlias_Object = MibTableColumn
h3cDot11APModelAlias = _H3cDot11APModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 1),
    _H3cDot11APModelAlias_Type()
)
h3cDot11APModelAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APModelAlias.setStatus("current")
_H3cDot11APModelName_Type = OctetString
_H3cDot11APModelName_Object = MibTableColumn
h3cDot11APModelName = _H3cDot11APModelName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 2),
    _H3cDot11APModelName_Type()
)
h3cDot11APModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APModelName.setStatus("current")
_H3cDot11RadioNumSupport_Type = H3cDot11RadioScopeType
_H3cDot11RadioNumSupport_Object = MibTableColumn
h3cDot11RadioNumSupport = _H3cDot11RadioNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 3),
    _H3cDot11RadioNumSupport_Type()
)
h3cDot11RadioNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioNumSupport.setStatus("current")
_H3cDot11StationNumSupport_Type = Integer32
_H3cDot11StationNumSupport_Object = MibTableColumn
h3cDot11StationNumSupport = _H3cDot11StationNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 4),
    _H3cDot11StationNumSupport_Type()
)
h3cDot11StationNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11StationNumSupport.setStatus("current")


class _H3cDot11MACModeSupport_Type(H3cDot11MACModeType):
    """Custom type h3cDot11MACModeSupport based on H3cDot11MACModeType"""


_H3cDot11MACModeSupport_Object = MibTableColumn
h3cDot11MACModeSupport = _H3cDot11MACModeSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 5),
    _H3cDot11MACModeSupport_Type()
)
h3cDot11MACModeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MACModeSupport.setStatus("current")
_H3cDot11APManufacturer_Type = OctetString
_H3cDot11APManufacturer_Object = MibTableColumn
h3cDot11APManufacturer = _H3cDot11APManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 6),
    _H3cDot11APManufacturer_Type()
)
h3cDot11APManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APManufacturer.setStatus("current")
_H3cDot11APCPUType_Type = OctetString
_H3cDot11APCPUType_Object = MibTableColumn
h3cDot11APCPUType = _H3cDot11APCPUType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 7),
    _H3cDot11APCPUType_Type()
)
h3cDot11APCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPUType.setStatus("current")
_H3cDot11APCPUClockSpeed_Type = Unsigned32
_H3cDot11APCPUClockSpeed_Object = MibTableColumn
h3cDot11APCPUClockSpeed = _H3cDot11APCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 8),
    _H3cDot11APCPUClockSpeed_Type()
)
h3cDot11APCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPUClockSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCPUClockSpeed.setUnits("Hz")
_H3cDot11APMemoryType_Type = OctetString
_H3cDot11APMemoryType_Object = MibTableColumn
h3cDot11APMemoryType = _H3cDot11APMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 9),
    _H3cDot11APMemoryType_Type()
)
h3cDot11APMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemoryType.setStatus("current")
_H3cDot11APFlashType_Type = OctetString
_H3cDot11APFlashType_Object = MibTableColumn
h3cDot11APFlashType = _H3cDot11APFlashType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 11),
    _H3cDot11APFlashType_Type()
)
h3cDot11APFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APFlashType.setStatus("current")
_H3cDot11APFlashSize_Type = Unsigned32
_H3cDot11APFlashSize_Object = MibTableColumn
h3cDot11APFlashSize = _H3cDot11APFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 12),
    _H3cDot11APFlashSize_Type()
)
h3cDot11APFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APFlashSize.setUnits("kbytes")
_H3cDot11APMemSize_Type = Gauge32
_H3cDot11APMemSize_Object = MibTableColumn
h3cDot11APMemSize = _H3cDot11APMemSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 13),
    _H3cDot11APMemSize_Type()
)
h3cDot11APMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemSize.setUnits("bytes")
_H3cDot11APFlashSizeInBytes_Type = Unsigned32
_H3cDot11APFlashSizeInBytes_Object = MibTableColumn
h3cDot11APFlashSizeInBytes = _H3cDot11APFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 14),
    _H3cDot11APFlashSizeInBytes_Type()
)
h3cDot11APFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APFlashSizeInBytes.setUnits("bytes")
_H3cDot11APMemorySize_Type = Unsigned32
_H3cDot11APMemorySize_Object = MibTableColumn
h3cDot11APMemorySize = _H3cDot11APMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 5, 1, 20),
    _H3cDot11APMemorySize_Type()
)
h3cDot11APMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemorySize.setUnits("kbytes")
_H3cDot11APIfTable_Object = MibTable
h3cDot11APIfTable = _H3cDot11APIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6)
)
if mibBuilder.loadTexts:
    h3cDot11APIfTable.setStatus("current")
_H3cDot11APIfEntry_Object = MibTableRow
h3cDot11APIfEntry = _H3cDot11APIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1)
)
h3cDot11APIfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APObjID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APIfEntry.setStatus("current")
_H3cDot11APIfIndex_Type = Integer32
_H3cDot11APIfIndex_Object = MibTableColumn
h3cDot11APIfIndex = _H3cDot11APIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 1),
    _H3cDot11APIfIndex_Type()
)
h3cDot11APIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APIfIndex.setStatus("current")
_H3cDot11APIfDescr_Type = OctetString
_H3cDot11APIfDescr_Object = MibTableColumn
h3cDot11APIfDescr = _H3cDot11APIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 2),
    _H3cDot11APIfDescr_Type()
)
h3cDot11APIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfDescr.setStatus("current")
_H3cDot11APIfType_Type = Integer32
_H3cDot11APIfType_Object = MibTableColumn
h3cDot11APIfType = _H3cDot11APIfType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 3),
    _H3cDot11APIfType_Type()
)
h3cDot11APIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfType.setStatus("current")
_H3cDot11APIfMtu_Type = Integer32
_H3cDot11APIfMtu_Object = MibTableColumn
h3cDot11APIfMtu = _H3cDot11APIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 4),
    _H3cDot11APIfMtu_Type()
)
h3cDot11APIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APIfMtu.setStatus("current")
_H3cDot11APIfPHYAddress_Type = OctetString
_H3cDot11APIfPHYAddress_Object = MibTableColumn
h3cDot11APIfPHYAddress = _H3cDot11APIfPHYAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 5),
    _H3cDot11APIfPHYAddress_Type()
)
h3cDot11APIfPHYAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfPHYAddress.setStatus("current")
_H3cDot11APIfSpeed_Type = Integer32
_H3cDot11APIfSpeed_Object = MibTableColumn
h3cDot11APIfSpeed = _H3cDot11APIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 6),
    _H3cDot11APIfSpeed_Type()
)
h3cDot11APIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APIfSpeed.setUnits("Mbps")
_H3cDot11APIfInDataRate_Type = Integer32
_H3cDot11APIfInDataRate_Object = MibTableColumn
h3cDot11APIfInDataRate = _H3cDot11APIfInDataRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 7),
    _H3cDot11APIfInDataRate_Type()
)
h3cDot11APIfInDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInDataRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APIfInDataRate.setUnits("Kbps")
_H3cDot11APIfOutDataRate_Type = Integer32
_H3cDot11APIfOutDataRate_Object = MibTableColumn
h3cDot11APIfOutDataRate = _H3cDot11APIfOutDataRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 8),
    _H3cDot11APIfOutDataRate_Type()
)
h3cDot11APIfOutDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutDataRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APIfOutDataRate.setUnits("Kbps")
_H3cDot11APIfSpeedKbps_Type = Gauge32
_H3cDot11APIfSpeedKbps_Object = MibTableColumn
h3cDot11APIfSpeedKbps = _H3cDot11APIfSpeedKbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 6, 1, 9),
    _H3cDot11APIfSpeedKbps_Type()
)
h3cDot11APIfSpeedKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfSpeedKbps.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APIfSpeedKbps.setUnits("kbps")
_H3cDot11APSSIDObjectTable_Object = MibTable
h3cDot11APSSIDObjectTable = _H3cDot11APSSIDObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7)
)
if mibBuilder.loadTexts:
    h3cDot11APSSIDObjectTable.setStatus("current")
_H3cDot11APSSIDObjectEntry_Object = MibTableRow
h3cDot11APSSIDObjectEntry = _H3cDot11APSSIDObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7, 1)
)
h3cDot11APSSIDObjectEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APConfigSPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APSSIDObjectEntry.setStatus("current")
_H3cDot11APConfigSPID_Type = H3cDot11ServicePolicyIDType
_H3cDot11APConfigSPID_Object = MibTableColumn
h3cDot11APConfigSPID = _H3cDot11APConfigSPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7, 1, 1),
    _H3cDot11APConfigSPID_Type()
)
h3cDot11APConfigSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APConfigSPID.setStatus("current")
_H3cDot11APConfigSSIDName_Type = H3cDot11SSIDStringType
_H3cDot11APConfigSSIDName_Object = MibTableColumn
h3cDot11APConfigSSIDName = _H3cDot11APConfigSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7, 1, 2),
    _H3cDot11APConfigSSIDName_Type()
)
h3cDot11APConfigSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APConfigSSIDName.setStatus("current")
_H3cDot11APConfigBSSIDNum_Type = Integer32
_H3cDot11APConfigBSSIDNum_Object = MibTableColumn
h3cDot11APConfigBSSIDNum = _H3cDot11APConfigBSSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7, 1, 3),
    _H3cDot11APConfigBSSIDNum_Type()
)
h3cDot11APConfigBSSIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APConfigBSSIDNum.setStatus("current")
_H3cDot11APConfigPortalStaNum_Type = Integer32
_H3cDot11APConfigPortalStaNum_Object = MibTableColumn
h3cDot11APConfigPortalStaNum = _H3cDot11APConfigPortalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 7, 1, 4),
    _H3cDot11APConfigPortalStaNum_Type()
)
h3cDot11APConfigPortalStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APConfigPortalStaNum.setStatus("current")
_H3cDot11APSysInfoTable_Object = MibTable
h3cDot11APSysInfoTable = _H3cDot11APSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8)
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoTable.setStatus("current")
_H3cDot11APSysInfoEntry_Object = MibTableRow
h3cDot11APSysInfoEntry = _H3cDot11APSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1)
)
h3cDot11APSysInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoEntry.setStatus("current")
_H3cDot11APSysUpTime_Type = TimeTicks
_H3cDot11APSysUpTime_Object = MibTableColumn
h3cDot11APSysUpTime = _H3cDot11APSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 1),
    _H3cDot11APSysUpTime_Type()
)
h3cDot11APSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APSysUpTime.setStatus("current")


class _H3cDot11APCPURTUsage_Type(Integer32):
    """Custom type h3cDot11APCPURTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCPURTUsage_Type.__name__ = "Integer32"
_H3cDot11APCPURTUsage_Object = MibTableColumn
h3cDot11APCPURTUsage = _H3cDot11APCPURTUsage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 2),
    _H3cDot11APCPURTUsage_Type()
)
h3cDot11APCPURTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPURTUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCPURTUsage.setUnits("onepercent")


class _H3cDot11APCPUAvgUsage_Type(Integer32):
    """Custom type h3cDot11APCPUAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCPUAvgUsage_Type.__name__ = "Integer32"
_H3cDot11APCPUAvgUsage_Object = MibTableColumn
h3cDot11APCPUAvgUsage = _H3cDot11APCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 3),
    _H3cDot11APCPUAvgUsage_Type()
)
h3cDot11APCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPUAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCPUAvgUsage.setUnits("onepercent")


class _H3cDot11APMemRTUsage_Type(Integer32):
    """Custom type h3cDot11APMemRTUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APMemRTUsage_Type.__name__ = "Integer32"
_H3cDot11APMemRTUsage_Object = MibTableColumn
h3cDot11APMemRTUsage = _H3cDot11APMemRTUsage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 4),
    _H3cDot11APMemRTUsage_Type()
)
h3cDot11APMemRTUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemRTUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemRTUsage.setUnits("onepercent")


class _H3cDot11APMemAvgUsage_Type(Integer32):
    """Custom type h3cDot11APMemAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APMemAvgUsage_Type.__name__ = "Integer32"
_H3cDot11APMemAvgUsage_Object = MibTableColumn
h3cDot11APMemAvgUsage = _H3cDot11APMemAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 5),
    _H3cDot11APMemAvgUsage_Type()
)
h3cDot11APMemAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemAvgUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemAvgUsage.setUnits("onepercent")
_H3cDot11APIPAddressGateway_Type = IpAddress
_H3cDot11APIPAddressGateway_Object = MibTableColumn
h3cDot11APIPAddressGateway = _H3cDot11APIPAddressGateway_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 6),
    _H3cDot11APIPAddressGateway_Type()
)
h3cDot11APIPAddressGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIPAddressGateway.setStatus("current")


class _H3cDot11APACAssociateStatus_Type(Integer32):
    """Custom type h3cDot11APACAssociateStatus based on Integer32"""
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


_H3cDot11APACAssociateStatus_Type.__name__ = "Integer32"
_H3cDot11APACAssociateStatus_Object = MibTableColumn
h3cDot11APACAssociateStatus = _H3cDot11APACAssociateStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 7),
    _H3cDot11APACAssociateStatus_Type()
)
h3cDot11APACAssociateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APACAssociateStatus.setStatus("current")


class _H3cDot11APManuBuildInfo_Type(OctetString):
    """Custom type h3cDot11APManuBuildInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11APManuBuildInfo_Type.__name__ = "OctetString"
_H3cDot11APManuBuildInfo_Object = MibTableColumn
h3cDot11APManuBuildInfo = _H3cDot11APManuBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 8),
    _H3cDot11APManuBuildInfo_Type()
)
h3cDot11APManuBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APManuBuildInfo.setStatus("current")
_H3cDot11APFlashFreeSize_Type = Unsigned32
_H3cDot11APFlashFreeSize_Object = MibTableColumn
h3cDot11APFlashFreeSize = _H3cDot11APFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 9),
    _H3cDot11APFlashFreeSize_Type()
)
h3cDot11APFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APFlashFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APFlashFreeSize.setUnits("bytes")
_H3cDot11APTemperature_Type = Integer32
_H3cDot11APTemperature_Object = MibTableColumn
h3cDot11APTemperature = _H3cDot11APTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 8, 1, 10),
    _H3cDot11APTemperature_Type()
)
h3cDot11APTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTemperature.setStatus("current")
_H3cDot11APIdleListTable_Object = MibTable
h3cDot11APIdleListTable = _H3cDot11APIdleListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 9)
)
if mibBuilder.loadTexts:
    h3cDot11APIdleListTable.setStatus("current")
_H3cDot11APIdleListEntry_Object = MibTableRow
h3cDot11APIdleListEntry = _H3cDot11APIdleListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 9, 1)
)
h3cDot11APIdleListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIdleTemplateName"),
)
if mibBuilder.loadTexts:
    h3cDot11APIdleListEntry.setStatus("current")


class _H3cDot11APIdleTemplateName_Type(OctetString):
    """Custom type h3cDot11APIdleTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11APIdleTemplateName_Type.__name__ = "OctetString"
_H3cDot11APIdleTemplateName_Object = MibTableColumn
h3cDot11APIdleTemplateName = _H3cDot11APIdleTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 9, 1, 1),
    _H3cDot11APIdleTemplateName_Type()
)
h3cDot11APIdleTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APIdleTemplateName.setStatus("current")
_H3cDot11APIdleSerialID_Type = OctetString
_H3cDot11APIdleSerialID_Object = MibTableColumn
h3cDot11APIdleSerialID = _H3cDot11APIdleSerialID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 9, 1, 2),
    _H3cDot11APIdleSerialID_Type()
)
h3cDot11APIdleSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIdleSerialID.setStatus("current")
_H3cDot11APSysInfoByAPIDTable_Object = MibTable
h3cDot11APSysInfoByAPIDTable = _H3cDot11APSysInfoByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10)
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoByAPIDTable.setStatus("current")
_H3cDot11APSysInfoByAPIDEntry_Object = MibTableRow
h3cDot11APSysInfoByAPIDEntry = _H3cDot11APSysInfoByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1)
)
h3cDot11APSysInfoByAPIDEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APObjID"),
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoByAPIDEntry.setStatus("current")
_H3cDot11APSysUpTime2_Type = TimeTicks
_H3cDot11APSysUpTime2_Object = MibTableColumn
h3cDot11APSysUpTime2 = _H3cDot11APSysUpTime2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 1),
    _H3cDot11APSysUpTime2_Type()
)
h3cDot11APSysUpTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APSysUpTime2.setStatus("current")


class _H3cDot11APCPURTUsage2_Type(Integer32):
    """Custom type h3cDot11APCPURTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCPURTUsage2_Type.__name__ = "Integer32"
_H3cDot11APCPURTUsage2_Object = MibTableColumn
h3cDot11APCPURTUsage2 = _H3cDot11APCPURTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 2),
    _H3cDot11APCPURTUsage2_Type()
)
h3cDot11APCPURTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPURTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCPURTUsage2.setUnits("onepercent")


class _H3cDot11APCPUAvgUsage2_Type(Integer32):
    """Custom type h3cDot11APCPUAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCPUAvgUsage2_Type.__name__ = "Integer32"
_H3cDot11APCPUAvgUsage2_Object = MibTableColumn
h3cDot11APCPUAvgUsage2 = _H3cDot11APCPUAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 3),
    _H3cDot11APCPUAvgUsage2_Type()
)
h3cDot11APCPUAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APCPUAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCPUAvgUsage2.setUnits("onepercent")


class _H3cDot11APMemRTUsage2_Type(Integer32):
    """Custom type h3cDot11APMemRTUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APMemRTUsage2_Type.__name__ = "Integer32"
_H3cDot11APMemRTUsage2_Object = MibTableColumn
h3cDot11APMemRTUsage2 = _H3cDot11APMemRTUsage2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 4),
    _H3cDot11APMemRTUsage2_Type()
)
h3cDot11APMemRTUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemRTUsage2.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemRTUsage2.setUnits("onepercent")


class _H3cDot11APMemAvgUsage2_Type(Integer32):
    """Custom type h3cDot11APMemAvgUsage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APMemAvgUsage2_Type.__name__ = "Integer32"
_H3cDot11APMemAvgUsage2_Object = MibTableColumn
h3cDot11APMemAvgUsage2 = _H3cDot11APMemAvgUsage2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 5),
    _H3cDot11APMemAvgUsage2_Type()
)
h3cDot11APMemAvgUsage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMemAvgUsage2.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemAvgUsage2.setUnits("onepercent")
_H3cDot11APIPAddressGateway2_Type = IpAddress
_H3cDot11APIPAddressGateway2_Object = MibTableColumn
h3cDot11APIPAddressGateway2 = _H3cDot11APIPAddressGateway2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 6),
    _H3cDot11APIPAddressGateway2_Type()
)
h3cDot11APIPAddressGateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIPAddressGateway2.setStatus("current")


class _H3cDot11APACAssociateStatus2_Type(Integer32):
    """Custom type h3cDot11APACAssociateStatus2 based on Integer32"""
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


_H3cDot11APACAssociateStatus2_Type.__name__ = "Integer32"
_H3cDot11APACAssociateStatus2_Object = MibTableColumn
h3cDot11APACAssociateStatus2 = _H3cDot11APACAssociateStatus2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 7),
    _H3cDot11APACAssociateStatus2_Type()
)
h3cDot11APACAssociateStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APACAssociateStatus2.setStatus("current")


class _H3cDot11APManuBuildInfo2_Type(OctetString):
    """Custom type h3cDot11APManuBuildInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11APManuBuildInfo2_Type.__name__ = "OctetString"
_H3cDot11APManuBuildInfo2_Object = MibTableColumn
h3cDot11APManuBuildInfo2 = _H3cDot11APManuBuildInfo2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 8),
    _H3cDot11APManuBuildInfo2_Type()
)
h3cDot11APManuBuildInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APManuBuildInfo2.setStatus("current")
_H3cDot11APFlashFreeSize2_Type = Unsigned32
_H3cDot11APFlashFreeSize2_Object = MibTableColumn
h3cDot11APFlashFreeSize2 = _H3cDot11APFlashFreeSize2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 9),
    _H3cDot11APFlashFreeSize2_Type()
)
h3cDot11APFlashFreeSize2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APFlashFreeSize2.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APFlashFreeSize2.setUnits("bytes")
_H3cDot11APTemperature2_Type = Integer32
_H3cDot11APTemperature2_Object = MibTableColumn
h3cDot11APTemperature2 = _H3cDot11APTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 10),
    _H3cDot11APTemperature2_Type()
)
h3cDot11APTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTemperature2.setStatus("current")
_H3cDot11APMacAddress2_Type = MacAddress
_H3cDot11APMacAddress2_Object = MibTableColumn
h3cDot11APMacAddress2 = _H3cDot11APMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 1, 10, 1, 11),
    _H3cDot11APMacAddress2_Type()
)
h3cDot11APMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APMacAddress2.setStatus("current")
_H3cDot11APStatisGroup_ObjectIdentity = ObjectIdentity
h3cDot11APStatisGroup = _H3cDot11APStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2)
)
_H3cDot11APRxStatisTable_Object = MibTable
h3cDot11APRxStatisTable = _H3cDot11APRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11APRxStatisTable.setStatus("current")
_H3cDot11APRxStatisEntry_Object = MibTableRow
h3cDot11APRxStatisEntry = _H3cDot11APRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1)
)
h3cDot11APRxStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11APRxStatisEntry.setStatus("current")
_H3cDot11RxFrameDupCnt_Type = Counter32
_H3cDot11RxFrameDupCnt_Object = MibTableColumn
h3cDot11RxFrameDupCnt = _H3cDot11RxFrameDupCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 1),
    _H3cDot11RxFrameDupCnt_Type()
)
h3cDot11RxFrameDupCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFrameDupCnt.setStatus("current")
_H3cDot11RxFrameCnt_Type = Counter32
_H3cDot11RxFrameCnt_Object = MibTableColumn
h3cDot11RxFrameCnt = _H3cDot11RxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 2),
    _H3cDot11RxFrameCnt_Type()
)
h3cDot11RxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFrameCnt.setStatus("current")
_H3cDot11RxUcastFrameCnt_Type = Counter32
_H3cDot11RxUcastFrameCnt_Object = MibTableColumn
h3cDot11RxUcastFrameCnt = _H3cDot11RxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 3),
    _H3cDot11RxUcastFrameCnt_Type()
)
h3cDot11RxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxUcastFrameCnt.setStatus("current")
_H3cDot11RxBcastFrameCnt_Type = Counter32
_H3cDot11RxBcastFrameCnt_Object = MibTableColumn
h3cDot11RxBcastFrameCnt = _H3cDot11RxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 4),
    _H3cDot11RxBcastFrameCnt_Type()
)
h3cDot11RxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxBcastFrameCnt.setStatus("current")
_H3cDot11RxMcastFrameCnt_Type = Counter32
_H3cDot11RxMcastFrameCnt_Object = MibTableColumn
h3cDot11RxMcastFrameCnt = _H3cDot11RxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 5),
    _H3cDot11RxMcastFrameCnt_Type()
)
h3cDot11RxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxMcastFrameCnt.setStatus("current")
_H3cDot11RxDiscardFrameCnt_Type = Counter32
_H3cDot11RxDiscardFrameCnt_Object = MibTableColumn
h3cDot11RxDiscardFrameCnt = _H3cDot11RxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 6),
    _H3cDot11RxDiscardFrameCnt_Type()
)
h3cDot11RxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxDiscardFrameCnt.setStatus("current")
_H3cDot11RxFragCnt_Type = Counter32
_H3cDot11RxFragCnt_Object = MibTableColumn
h3cDot11RxFragCnt = _H3cDot11RxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 7),
    _H3cDot11RxFragCnt_Type()
)
h3cDot11RxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFragCnt.setStatus("current")
_H3cDot11RxFcsErrCnt_Type = Counter32
_H3cDot11RxFcsErrCnt_Object = MibTableColumn
h3cDot11RxFcsErrCnt = _H3cDot11RxFcsErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 8),
    _H3cDot11RxFcsErrCnt_Type()
)
h3cDot11RxFcsErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFcsErrCnt.setStatus("current")
_H3cDot11RxFrameBytes_Type = Counter32
_H3cDot11RxFrameBytes_Object = MibTableColumn
h3cDot11RxFrameBytes = _H3cDot11RxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 9),
    _H3cDot11RxFrameBytes_Type()
)
h3cDot11RxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFrameBytes.setStatus("current")
_H3cDot11RxUcastFrameBytes_Type = Counter32
_H3cDot11RxUcastFrameBytes_Object = MibTableColumn
h3cDot11RxUcastFrameBytes = _H3cDot11RxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 10),
    _H3cDot11RxUcastFrameBytes_Type()
)
h3cDot11RxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxUcastFrameBytes.setStatus("current")
_H3cDot11RxBcastFrameBytes_Type = Counter32
_H3cDot11RxBcastFrameBytes_Object = MibTableColumn
h3cDot11RxBcastFrameBytes = _H3cDot11RxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 11),
    _H3cDot11RxBcastFrameBytes_Type()
)
h3cDot11RxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxBcastFrameBytes.setStatus("current")
_H3cDot11RxMcastFrameBytes_Type = Counter32
_H3cDot11RxMcastFrameBytes_Object = MibTableColumn
h3cDot11RxMcastFrameBytes = _H3cDot11RxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 12),
    _H3cDot11RxMcastFrameBytes_Type()
)
h3cDot11RxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxMcastFrameBytes.setStatus("current")
_H3cDot11RxDiscardFrameBytes_Type = Counter32
_H3cDot11RxDiscardFrameBytes_Object = MibTableColumn
h3cDot11RxDiscardFrameBytes = _H3cDot11RxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 13),
    _H3cDot11RxDiscardFrameBytes_Type()
)
h3cDot11RxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxDiscardFrameBytes.setStatus("current")
_H3cDot11RxMgmtFrameCnt_Type = Counter32
_H3cDot11RxMgmtFrameCnt_Object = MibTableColumn
h3cDot11RxMgmtFrameCnt = _H3cDot11RxMgmtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 14),
    _H3cDot11RxMgmtFrameCnt_Type()
)
h3cDot11RxMgmtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxMgmtFrameCnt.setStatus("current")
_H3cDot11RxCtrlFrameCnt_Type = Counter32
_H3cDot11RxCtrlFrameCnt_Object = MibTableColumn
h3cDot11RxCtrlFrameCnt = _H3cDot11RxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 15),
    _H3cDot11RxCtrlFrameCnt_Type()
)
h3cDot11RxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxCtrlFrameCnt.setStatus("current")
_H3cDot11RxDataFrameCnt_Type = Counter32
_H3cDot11RxDataFrameCnt_Object = MibTableColumn
h3cDot11RxDataFrameCnt = _H3cDot11RxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 16),
    _H3cDot11RxDataFrameCnt_Type()
)
h3cDot11RxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxDataFrameCnt.setStatus("current")
_H3cDot11RxDecryptErrorCnt_Type = Counter32
_H3cDot11RxDecryptErrorCnt_Object = MibTableColumn
h3cDot11RxDecryptErrorCnt = _H3cDot11RxDecryptErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 17),
    _H3cDot11RxDecryptErrorCnt_Type()
)
h3cDot11RxDecryptErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxDecryptErrorCnt.setStatus("current")
_H3cDot11RxAuthenFrameCnt_Type = Counter32
_H3cDot11RxAuthenFrameCnt_Object = MibTableColumn
h3cDot11RxAuthenFrameCnt = _H3cDot11RxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 18),
    _H3cDot11RxAuthenFrameCnt_Type()
)
h3cDot11RxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxAuthenFrameCnt.setStatus("current")
_H3cDot11RxAssociateFrameCnt_Type = Counter32
_H3cDot11RxAssociateFrameCnt_Object = MibTableColumn
h3cDot11RxAssociateFrameCnt = _H3cDot11RxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 19),
    _H3cDot11RxAssociateFrameCnt_Type()
)
h3cDot11RxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxAssociateFrameCnt.setStatus("current")
_H3cDot11RxFrameErrorRatio_Type = Integer32
_H3cDot11RxFrameErrorRatio_Object = MibTableColumn
h3cDot11RxFrameErrorRatio = _H3cDot11RxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 20),
    _H3cDot11RxFrameErrorRatio_Type()
)
h3cDot11RxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RxFrameErrorRatio.setUnits("onepercent")
_H3cDot11RxPhyErrorCnt_Type = Counter32
_H3cDot11RxPhyErrorCnt_Object = MibTableColumn
h3cDot11RxPhyErrorCnt = _H3cDot11RxPhyErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 21),
    _H3cDot11RxPhyErrorCnt_Type()
)
h3cDot11RxPhyErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxPhyErrorCnt.setStatus("current")
_H3cDot11RxMICErrorCnt_Type = Counter32
_H3cDot11RxMICErrorCnt_Object = MibTableColumn
h3cDot11RxMICErrorCnt = _H3cDot11RxMICErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 22),
    _H3cDot11RxMICErrorCnt_Type()
)
h3cDot11RxMICErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxMICErrorCnt.setStatus("current")
_H3cDot11RxDataFrameBytes_Type = Counter32
_H3cDot11RxDataFrameBytes_Object = MibTableColumn
h3cDot11RxDataFrameBytes = _H3cDot11RxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 23),
    _H3cDot11RxDataFrameBytes_Type()
)
h3cDot11RxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxDataFrameBytes.setStatus("current")
_H3cDot11RadioRxAverSnr_Type = Integer32
_H3cDot11RadioRxAverSnr_Object = MibTableColumn
h3cDot11RadioRxAverSnr = _H3cDot11RadioRxAverSnr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 24),
    _H3cDot11RadioRxAverSnr_Type()
)
h3cDot11RadioRxAverSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioRxAverSnr.setStatus("current")
_H3cDot11RxPayloadBytes_Type = Counter32
_H3cDot11RxPayloadBytes_Object = MibTableColumn
h3cDot11RxPayloadBytes = _H3cDot11RxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 25),
    _H3cDot11RxPayloadBytes_Type()
)
h3cDot11RxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxPayloadBytes.setStatus("current")
_H3cDot11RxTrafficSpeed_Type = Integer32
_H3cDot11RxTrafficSpeed_Object = MibTableColumn
h3cDot11RxTrafficSpeed = _H3cDot11RxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 26),
    _H3cDot11RxTrafficSpeed_Type()
)
h3cDot11RxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RxTrafficSpeed.setUnits("byte/s")
_H3cDot11RxUcastDataFrameCnt_Type = Counter64
_H3cDot11RxUcastDataFrameCnt_Object = MibTableColumn
h3cDot11RxUcastDataFrameCnt = _H3cDot11RxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 27),
    _H3cDot11RxUcastDataFrameCnt_Type()
)
h3cDot11RxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxUcastDataFrameCnt.setStatus("current")
_H3cDot11RxNUcastDataFrameCnt_Type = Counter64
_H3cDot11RxNUcastDataFrameCnt_Object = MibTableColumn
h3cDot11RxNUcastDataFrameCnt = _H3cDot11RxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 28),
    _H3cDot11RxNUcastDataFrameCnt_Type()
)
h3cDot11RxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxNUcastDataFrameCnt.setStatus("current")
_H3cDot11RxTotalDiscardFrameCnt_Type = Counter64
_H3cDot11RxTotalDiscardFrameCnt_Object = MibTableColumn
h3cDot11RxTotalDiscardFrameCnt = _H3cDot11RxTotalDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 29),
    _H3cDot11RxTotalDiscardFrameCnt_Type()
)
h3cDot11RxTotalDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxTotalDiscardFrameCnt.setStatus("current")
_H3cDot11RxTotalIPCheckErrPacketCnt_Type = Counter64
_H3cDot11RxTotalIPCheckErrPacketCnt_Object = MibTableColumn
h3cDot11RxTotalIPCheckErrPacketCnt = _H3cDot11RxTotalIPCheckErrPacketCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 1, 1, 30),
    _H3cDot11RxTotalIPCheckErrPacketCnt_Type()
)
h3cDot11RxTotalIPCheckErrPacketCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RxTotalIPCheckErrPacketCnt.setStatus("current")
_H3cDot11APTxStatisTable_Object = MibTable
h3cDot11APTxStatisTable = _H3cDot11APTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11APTxStatisTable.setStatus("current")
_H3cDot11APTxStatisEntry_Object = MibTableRow
h3cDot11APTxStatisEntry = _H3cDot11APTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1)
)
h3cDot11APTxStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11APTxStatisEntry.setStatus("current")
_H3cDot11TxFragCnt_Type = Counter32
_H3cDot11TxFragCnt_Object = MibTableColumn
h3cDot11TxFragCnt = _H3cDot11TxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 1),
    _H3cDot11TxFragCnt_Type()
)
h3cDot11TxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxFragCnt.setStatus("current")
_H3cDot11FailedCnt_Type = Counter32
_H3cDot11FailedCnt_Object = MibTableColumn
h3cDot11FailedCnt = _H3cDot11FailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 2),
    _H3cDot11FailedCnt_Type()
)
h3cDot11FailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11FailedCnt.setStatus("current")
_H3cDot11RetryCnt_Type = Counter32
_H3cDot11RetryCnt_Object = MibTableColumn
h3cDot11RetryCnt = _H3cDot11RetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 3),
    _H3cDot11RetryCnt_Type()
)
h3cDot11RetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RetryCnt.setStatus("current")
_H3cDot11MultiRetryCnt_Type = Counter32
_H3cDot11MultiRetryCnt_Object = MibTableColumn
h3cDot11MultiRetryCnt = _H3cDot11MultiRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 4),
    _H3cDot11MultiRetryCnt_Type()
)
h3cDot11MultiRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MultiRetryCnt.setStatus("current")
_H3cDot11RtsSuccessCnt_Type = Counter32
_H3cDot11RtsSuccessCnt_Object = MibTableColumn
h3cDot11RtsSuccessCnt = _H3cDot11RtsSuccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 5),
    _H3cDot11RtsSuccessCnt_Type()
)
h3cDot11RtsSuccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RtsSuccessCnt.setStatus("current")
_H3cDot11RtsFailCnt_Type = Counter32
_H3cDot11RtsFailCnt_Object = MibTableColumn
h3cDot11RtsFailCnt = _H3cDot11RtsFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 6),
    _H3cDot11RtsFailCnt_Type()
)
h3cDot11RtsFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RtsFailCnt.setStatus("current")
_H3cDot11AckFailCnt_Type = Counter32
_H3cDot11AckFailCnt_Object = MibTableColumn
h3cDot11AckFailCnt = _H3cDot11AckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 7),
    _H3cDot11AckFailCnt_Type()
)
h3cDot11AckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AckFailCnt.setStatus("current")
_H3cDot11TxFrameCnt_Type = Counter32
_H3cDot11TxFrameCnt_Object = MibTableColumn
h3cDot11TxFrameCnt = _H3cDot11TxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 8),
    _H3cDot11TxFrameCnt_Type()
)
h3cDot11TxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxFrameCnt.setStatus("current")
_H3cDot11TxUcastFrameCnt_Type = Counter32
_H3cDot11TxUcastFrameCnt_Object = MibTableColumn
h3cDot11TxUcastFrameCnt = _H3cDot11TxUcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 9),
    _H3cDot11TxUcastFrameCnt_Type()
)
h3cDot11TxUcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxUcastFrameCnt.setStatus("current")
_H3cDot11TxBcastFrameCnt_Type = Counter32
_H3cDot11TxBcastFrameCnt_Object = MibTableColumn
h3cDot11TxBcastFrameCnt = _H3cDot11TxBcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 10),
    _H3cDot11TxBcastFrameCnt_Type()
)
h3cDot11TxBcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxBcastFrameCnt.setStatus("current")
_H3cDot11TxMcastFrameCnt_Type = Counter32
_H3cDot11TxMcastFrameCnt_Object = MibTableColumn
h3cDot11TxMcastFrameCnt = _H3cDot11TxMcastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 11),
    _H3cDot11TxMcastFrameCnt_Type()
)
h3cDot11TxMcastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxMcastFrameCnt.setStatus("current")
_H3cDot11TxDiscardFrameCnt_Type = Counter32
_H3cDot11TxDiscardFrameCnt_Object = MibTableColumn
h3cDot11TxDiscardFrameCnt = _H3cDot11TxDiscardFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 12),
    _H3cDot11TxDiscardFrameCnt_Type()
)
h3cDot11TxDiscardFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxDiscardFrameCnt.setStatus("current")
_H3cDot11TxFrameBytes_Type = Counter32
_H3cDot11TxFrameBytes_Object = MibTableColumn
h3cDot11TxFrameBytes = _H3cDot11TxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 13),
    _H3cDot11TxFrameBytes_Type()
)
h3cDot11TxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxFrameBytes.setStatus("current")
_H3cDot11TxUcastFrameBytes_Type = Counter32
_H3cDot11TxUcastFrameBytes_Object = MibTableColumn
h3cDot11TxUcastFrameBytes = _H3cDot11TxUcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 14),
    _H3cDot11TxUcastFrameBytes_Type()
)
h3cDot11TxUcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxUcastFrameBytes.setStatus("current")
_H3cDot11TxBcastFrameBytes_Type = Counter32
_H3cDot11TxBcastFrameBytes_Object = MibTableColumn
h3cDot11TxBcastFrameBytes = _H3cDot11TxBcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 15),
    _H3cDot11TxBcastFrameBytes_Type()
)
h3cDot11TxBcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxBcastFrameBytes.setStatus("current")
_H3cDot11TxMcastFrameBytes_Type = Counter32
_H3cDot11TxMcastFrameBytes_Object = MibTableColumn
h3cDot11TxMcastFrameBytes = _H3cDot11TxMcastFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 16),
    _H3cDot11TxMcastFrameBytes_Type()
)
h3cDot11TxMcastFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxMcastFrameBytes.setStatus("current")
_H3cDot11TxDiscardFrameBytes_Type = Counter32
_H3cDot11TxDiscardFrameBytes_Object = MibTableColumn
h3cDot11TxDiscardFrameBytes = _H3cDot11TxDiscardFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 17),
    _H3cDot11TxDiscardFrameBytes_Type()
)
h3cDot11TxDiscardFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxDiscardFrameBytes.setStatus("current")
_H3cDot11TxAuthenFrameCnt_Type = Counter32
_H3cDot11TxAuthenFrameCnt_Object = MibTableColumn
h3cDot11TxAuthenFrameCnt = _H3cDot11TxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 18),
    _H3cDot11TxAuthenFrameCnt_Type()
)
h3cDot11TxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxAuthenFrameCnt.setStatus("current")
_H3cDot11TxAssociateFrameCnt_Type = Counter32
_H3cDot11TxAssociateFrameCnt_Object = MibTableColumn
h3cDot11TxAssociateFrameCnt = _H3cDot11TxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 19),
    _H3cDot11TxAssociateFrameCnt_Type()
)
h3cDot11TxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxAssociateFrameCnt.setStatus("current")
_H3cDot11TxFrameRetryRatio_Type = Integer32
_H3cDot11TxFrameRetryRatio_Object = MibTableColumn
h3cDot11TxFrameRetryRatio = _H3cDot11TxFrameRetryRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 20),
    _H3cDot11TxFrameRetryRatio_Type()
)
h3cDot11TxFrameRetryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxFrameRetryRatio.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11TxFrameRetryRatio.setUnits("onepercent")
_H3cDot11TxDataFrameCnt_Type = Counter32
_H3cDot11TxDataFrameCnt_Object = MibTableColumn
h3cDot11TxDataFrameCnt = _H3cDot11TxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 21),
    _H3cDot11TxDataFrameCnt_Type()
)
h3cDot11TxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxDataFrameCnt.setStatus("current")
_H3cDot11TxDataFrameBytes_Type = Counter32
_H3cDot11TxDataFrameBytes_Object = MibTableColumn
h3cDot11TxDataFrameBytes = _H3cDot11TxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 22),
    _H3cDot11TxDataFrameBytes_Type()
)
h3cDot11TxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxDataFrameBytes.setStatus("current")
_H3cDot11TxMSDUCnt_Type = Counter32
_H3cDot11TxMSDUCnt_Object = MibTableColumn
h3cDot11TxMSDUCnt = _H3cDot11TxMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 23),
    _H3cDot11TxMSDUCnt_Type()
)
h3cDot11TxMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxMSDUCnt.setStatus("current")
_H3cDot11TxDiscardMSDUCnt_Type = Counter32
_H3cDot11TxDiscardMSDUCnt_Object = MibTableColumn
h3cDot11TxDiscardMSDUCnt = _H3cDot11TxDiscardMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 24),
    _H3cDot11TxDiscardMSDUCnt_Type()
)
h3cDot11TxDiscardMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxDiscardMSDUCnt.setStatus("current")
_H3cDot11RetryMSDUCnt_Type = Counter32
_H3cDot11RetryMSDUCnt_Object = MibTableColumn
h3cDot11RetryMSDUCnt = _H3cDot11RetryMSDUCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 25),
    _H3cDot11RetryMSDUCnt_Type()
)
h3cDot11RetryMSDUCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RetryMSDUCnt.setStatus("current")
_H3cDot11TxPayloadBytes_Type = Counter32
_H3cDot11TxPayloadBytes_Object = MibTableColumn
h3cDot11TxPayloadBytes = _H3cDot11TxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 26),
    _H3cDot11TxPayloadBytes_Type()
)
h3cDot11TxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxPayloadBytes.setStatus("current")
_H3cDot11TxTrafficSpeed_Type = Integer32
_H3cDot11TxTrafficSpeed_Object = MibTableColumn
h3cDot11TxTrafficSpeed = _H3cDot11TxTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 27),
    _H3cDot11TxTrafficSpeed_Type()
)
h3cDot11TxTrafficSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11TxTrafficSpeed.setUnits("byte/s")
_H3cDot11TxErrFrameRatio_Type = Integer32
_H3cDot11TxErrFrameRatio_Object = MibTableColumn
h3cDot11TxErrFrameRatio = _H3cDot11TxErrFrameRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 28),
    _H3cDot11TxErrFrameRatio_Type()
)
h3cDot11TxErrFrameRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxErrFrameRatio.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11TxErrFrameRatio.setUnits("onepercent")
_H3cDot11TxFrameRate_Type = Integer32
_H3cDot11TxFrameRate_Object = MibTableColumn
h3cDot11TxFrameRate = _H3cDot11TxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 29),
    _H3cDot11TxFrameRate_Type()
)
h3cDot11TxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxFrameRate.setStatus("current")
_H3cDot11TxMgtFrameCnt_Type = Counter32
_H3cDot11TxMgtFrameCnt_Object = MibTableColumn
h3cDot11TxMgtFrameCnt = _H3cDot11TxMgtFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 30),
    _H3cDot11TxMgtFrameCnt_Type()
)
h3cDot11TxMgtFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxMgtFrameCnt.setStatus("current")
_H3cDot11TxCtrlFrameCnt_Type = Counter32
_H3cDot11TxCtrlFrameCnt_Object = MibTableColumn
h3cDot11TxCtrlFrameCnt = _H3cDot11TxCtrlFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 31),
    _H3cDot11TxCtrlFrameCnt_Type()
)
h3cDot11TxCtrlFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxCtrlFrameCnt.setStatus("current")
_H3cDot11TxMACErrCnt_Type = Counter32
_H3cDot11TxMACErrCnt_Object = MibTableColumn
h3cDot11TxMACErrCnt = _H3cDot11TxMACErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 32),
    _H3cDot11TxMACErrCnt_Type()
)
h3cDot11TxMACErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxMACErrCnt.setStatus("current")
_H3cDot11TxErrFrameCnt_Type = Counter32
_H3cDot11TxErrFrameCnt_Object = MibTableColumn
h3cDot11TxErrFrameCnt = _H3cDot11TxErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 33),
    _H3cDot11TxErrFrameCnt_Type()
)
h3cDot11TxErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxErrFrameCnt.setStatus("current")
_H3cDot11TxUcastDataFrameCnt_Type = Counter64
_H3cDot11TxUcastDataFrameCnt_Object = MibTableColumn
h3cDot11TxUcastDataFrameCnt = _H3cDot11TxUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 34),
    _H3cDot11TxUcastDataFrameCnt_Type()
)
h3cDot11TxUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxUcastDataFrameCnt.setStatus("current")
_H3cDot11TxNUcastDataFrameCnt_Type = Counter64
_H3cDot11TxNUcastDataFrameCnt_Object = MibTableColumn
h3cDot11TxNUcastDataFrameCnt = _H3cDot11TxNUcastDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 2, 1, 35),
    _H3cDot11TxNUcastDataFrameCnt_Type()
)
h3cDot11TxNUcastDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11TxNUcastDataFrameCnt.setStatus("current")
_H3cDot11APAssocStatisTable_Object = MibTable
h3cDot11APAssocStatisTable = _H3cDot11APAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11APAssocStatisTable.setStatus("current")
_H3cDot11APAssocStatisEntry_Object = MibTableRow
h3cDot11APAssocStatisEntry = _H3cDot11APAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1)
)
h3cDot11APAssocStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APAssocStatisEntry.setStatus("current")
_H3cDot11ApStationAssocSum_Type = Counter32
_H3cDot11ApStationAssocSum_Object = MibTableColumn
h3cDot11ApStationAssocSum = _H3cDot11ApStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 1),
    _H3cDot11ApStationAssocSum_Type()
)
h3cDot11ApStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationAssocSum.setStatus("current")
_H3cDot11ApStationAssocFailSum_Type = Counter32
_H3cDot11ApStationAssocFailSum_Object = MibTableColumn
h3cDot11ApStationAssocFailSum = _H3cDot11ApStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 2),
    _H3cDot11ApStationAssocFailSum_Type()
)
h3cDot11ApStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationAssocFailSum.setStatus("current")
_H3cDot11ApStationReassocSum_Type = Counter32
_H3cDot11ApStationReassocSum_Object = MibTableColumn
h3cDot11ApStationReassocSum = _H3cDot11ApStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 3),
    _H3cDot11ApStationReassocSum_Type()
)
h3cDot11ApStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationReassocSum.setStatus("current")
_H3cDot11ApStationAssocRejectSum_Type = Counter32
_H3cDot11ApStationAssocRejectSum_Object = MibTableColumn
h3cDot11ApStationAssocRejectSum = _H3cDot11ApStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 4),
    _H3cDot11ApStationAssocRejectSum_Type()
)
h3cDot11ApStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationAssocRejectSum.setStatus("current")
_H3cDot11ApStationExDeAuthenSum_Type = Counter32
_H3cDot11ApStationExDeAuthenSum_Object = MibTableColumn
h3cDot11ApStationExDeAuthenSum = _H3cDot11ApStationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 5),
    _H3cDot11ApStationExDeAuthenSum_Type()
)
h3cDot11ApStationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationExDeAuthenSum.setStatus("current")
_H3cDot11ApStationCurAssocSum_Type = Integer32
_H3cDot11ApStationCurAssocSum_Object = MibTableColumn
h3cDot11ApStationCurAssocSum = _H3cDot11ApStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 6),
    _H3cDot11ApStationCurAssocSum_Type()
)
h3cDot11ApStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationCurAssocSum.setStatus("current")
_H3cDot11ApStaCurAuthSuccSum_Type = Integer32
_H3cDot11ApStaCurAuthSuccSum_Object = MibTableColumn
h3cDot11ApStaCurAuthSuccSum = _H3cDot11ApStaCurAuthSuccSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 7),
    _H3cDot11ApStaCurAuthSuccSum_Type()
)
h3cDot11ApStaCurAuthSuccSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStaCurAuthSuccSum.setStatus("current")
_H3cDot11AllStationUpSumTime_Type = Counter32
_H3cDot11AllStationUpSumTime_Object = MibTableColumn
h3cDot11AllStationUpSumTime = _H3cDot11AllStationUpSumTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 8),
    _H3cDot11AllStationUpSumTime_Type()
)
h3cDot11AllStationUpSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AllStationUpSumTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AllStationUpSumTime.setUnits("minute")
_H3cDot11ApStationAssocReqSum_Type = Counter32
_H3cDot11ApStationAssocReqSum_Object = MibTableColumn
h3cDot11ApStationAssocReqSum = _H3cDot11ApStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 9),
    _H3cDot11ApStationAssocReqSum_Type()
)
h3cDot11ApStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11ApStationAssocReqSum.setStatus("current")
_H3cDot11AllStationUpSumTimeTicks_Type = TimeTicks
_H3cDot11AllStationUpSumTimeTicks_Object = MibTableColumn
h3cDot11AllStationUpSumTimeTicks = _H3cDot11AllStationUpSumTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 3, 1, 10),
    _H3cDot11AllStationUpSumTimeTicks_Type()
)
h3cDot11AllStationUpSumTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AllStationUpSumTimeTicks.setStatus("current")
_H3cDot11BSSRxStatisTable_Object = MibTable
h3cDot11BSSRxStatisTable = _H3cDot11BSSRxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDot11BSSRxStatisTable.setStatus("current")
_H3cDot11BSSRxStatisEntry_Object = MibTableRow
h3cDot11BSSRxStatisEntry = _H3cDot11BSSRxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1)
)
h3cDot11BSSRxStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    h3cDot11BSSRxStatisEntry.setStatus("current")
_H3cDot11BSSRxFrameCnt_Type = Counter32
_H3cDot11BSSRxFrameCnt_Object = MibTableColumn
h3cDot11BSSRxFrameCnt = _H3cDot11BSSRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 1),
    _H3cDot11BSSRxFrameCnt_Type()
)
h3cDot11BSSRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxFrameCnt.setStatus("current")
_H3cDot11BSSRxFrameBytes_Type = Counter32
_H3cDot11BSSRxFrameBytes_Object = MibTableColumn
h3cDot11BSSRxFrameBytes = _H3cDot11BSSRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 2),
    _H3cDot11BSSRxFrameBytes_Type()
)
h3cDot11BSSRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxFrameBytes.setStatus("current")
_H3cDot11BSSRxDataFrameCnt_Type = Counter32
_H3cDot11BSSRxDataFrameCnt_Object = MibTableColumn
h3cDot11BSSRxDataFrameCnt = _H3cDot11BSSRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 3),
    _H3cDot11BSSRxDataFrameCnt_Type()
)
h3cDot11BSSRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxDataFrameCnt.setStatus("current")
_H3cDot11BSSRxDataFrameBytes_Type = Counter32
_H3cDot11BSSRxDataFrameBytes_Object = MibTableColumn
h3cDot11BSSRxDataFrameBytes = _H3cDot11BSSRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 4),
    _H3cDot11BSSRxDataFrameBytes_Type()
)
h3cDot11BSSRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxDataFrameBytes.setStatus("current")
_H3cDot11BSSRxAssociateFrameCnt_Type = Counter32
_H3cDot11BSSRxAssociateFrameCnt_Object = MibTableColumn
h3cDot11BSSRxAssociateFrameCnt = _H3cDot11BSSRxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 5),
    _H3cDot11BSSRxAssociateFrameCnt_Type()
)
h3cDot11BSSRxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxAssociateFrameCnt.setStatus("current")
_H3cDot11BSSRxFrameErrorRatio_Type = Integer32
_H3cDot11BSSRxFrameErrorRatio_Object = MibTableColumn
h3cDot11BSSRxFrameErrorRatio = _H3cDot11BSSRxFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 6),
    _H3cDot11BSSRxFrameErrorRatio_Type()
)
h3cDot11BSSRxFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxFrameErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11BSSRxFrameErrorRatio.setUnits("percent")
_H3cDot11BSSRxPayloadBytes_Type = Counter32
_H3cDot11BSSRxPayloadBytes_Object = MibTableColumn
h3cDot11BSSRxPayloadBytes = _H3cDot11BSSRxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 7),
    _H3cDot11BSSRxPayloadBytes_Type()
)
h3cDot11BSSRxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxPayloadBytes.setStatus("current")
_H3cDot11BSSRxUniFrameCnt_Type = Counter32
_H3cDot11BSSRxUniFrameCnt_Object = MibTableColumn
h3cDot11BSSRxUniFrameCnt = _H3cDot11BSSRxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 8),
    _H3cDot11BSSRxUniFrameCnt_Type()
)
h3cDot11BSSRxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxUniFrameCnt.setStatus("current")
_H3cDot11BSSRxNonUniFrameCnt_Type = Integer32
_H3cDot11BSSRxNonUniFrameCnt_Object = MibTableColumn
h3cDot11BSSRxNonUniFrameCnt = _H3cDot11BSSRxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 9),
    _H3cDot11BSSRxNonUniFrameCnt_Type()
)
h3cDot11BSSRxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxNonUniFrameCnt.setStatus("current")
_H3cDot11BSSRxAuthenFrameCnt_Type = Counter32
_H3cDot11BSSRxAuthenFrameCnt_Object = MibTableColumn
h3cDot11BSSRxAuthenFrameCnt = _H3cDot11BSSRxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 4, 1, 10),
    _H3cDot11BSSRxAuthenFrameCnt_Type()
)
h3cDot11BSSRxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSRxAuthenFrameCnt.setStatus("current")
_H3cDot11BSSTxStatisTable_Object = MibTable
h3cDot11BSSTxStatisTable = _H3cDot11BSSTxStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDot11BSSTxStatisTable.setStatus("current")
_H3cDot11BSSTxStatisEntry_Object = MibTableRow
h3cDot11BSSTxStatisEntry = _H3cDot11BSSTxStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1)
)
h3cDot11BSSTxStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    h3cDot11BSSTxStatisEntry.setStatus("current")
_H3cDot11BSSTxFrameCnt_Type = Counter32
_H3cDot11BSSTxFrameCnt_Object = MibTableColumn
h3cDot11BSSTxFrameCnt = _H3cDot11BSSTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 1),
    _H3cDot11BSSTxFrameCnt_Type()
)
h3cDot11BSSTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxFrameCnt.setStatus("current")
_H3cDot11BSSTxFrameBytes_Type = Counter32
_H3cDot11BSSTxFrameBytes_Object = MibTableColumn
h3cDot11BSSTxFrameBytes = _H3cDot11BSSTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 2),
    _H3cDot11BSSTxFrameBytes_Type()
)
h3cDot11BSSTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxFrameBytes.setStatus("current")
_H3cDot11BSSTxDataFrameCnt_Type = Counter32
_H3cDot11BSSTxDataFrameCnt_Object = MibTableColumn
h3cDot11BSSTxDataFrameCnt = _H3cDot11BSSTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 3),
    _H3cDot11BSSTxDataFrameCnt_Type()
)
h3cDot11BSSTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxDataFrameCnt.setStatus("current")
_H3cDot11BSSTxDataFrameBytes_Type = Counter32
_H3cDot11BSSTxDataFrameBytes_Object = MibTableColumn
h3cDot11BSSTxDataFrameBytes = _H3cDot11BSSTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 4),
    _H3cDot11BSSTxDataFrameBytes_Type()
)
h3cDot11BSSTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxDataFrameBytes.setStatus("current")
_H3cDot11BSSTxAssociateFrameCnt_Type = Counter32
_H3cDot11BSSTxAssociateFrameCnt_Object = MibTableColumn
h3cDot11BSSTxAssociateFrameCnt = _H3cDot11BSSTxAssociateFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 5),
    _H3cDot11BSSTxAssociateFrameCnt_Type()
)
h3cDot11BSSTxAssociateFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxAssociateFrameCnt.setStatus("current")
_H3cDot11BSSTxPayloadBytes_Type = Counter32
_H3cDot11BSSTxPayloadBytes_Object = MibTableColumn
h3cDot11BSSTxPayloadBytes = _H3cDot11BSSTxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 6),
    _H3cDot11BSSTxPayloadBytes_Type()
)
h3cDot11BSSTxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxPayloadBytes.setStatus("current")
_H3cDot11BSSTxRetryCnt_Type = Counter32
_H3cDot11BSSTxRetryCnt_Object = MibTableColumn
h3cDot11BSSTxRetryCnt = _H3cDot11BSSTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 7),
    _H3cDot11BSSTxRetryCnt_Type()
)
h3cDot11BSSTxRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxRetryCnt.setStatus("current")
_H3cDot11BSSTxUniFrameCnt_Type = Counter32
_H3cDot11BSSTxUniFrameCnt_Object = MibTableColumn
h3cDot11BSSTxUniFrameCnt = _H3cDot11BSSTxUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 8),
    _H3cDot11BSSTxUniFrameCnt_Type()
)
h3cDot11BSSTxUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxUniFrameCnt.setStatus("current")
_H3cDot11BSSTxNonUniFrameCnt_Type = Integer32
_H3cDot11BSSTxNonUniFrameCnt_Object = MibTableColumn
h3cDot11BSSTxNonUniFrameCnt = _H3cDot11BSSTxNonUniFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 9),
    _H3cDot11BSSTxNonUniFrameCnt_Type()
)
h3cDot11BSSTxNonUniFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxNonUniFrameCnt.setStatus("current")
_H3cDot11BSSTxAuthenFrameCnt_Type = Counter32
_H3cDot11BSSTxAuthenFrameCnt_Object = MibTableColumn
h3cDot11BSSTxAuthenFrameCnt = _H3cDot11BSSTxAuthenFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 5, 1, 10),
    _H3cDot11BSSTxAuthenFrameCnt_Type()
)
h3cDot11BSSTxAuthenFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSTxAuthenFrameCnt.setStatus("current")
_H3cDot11BSSAssocStatisTable_Object = MibTable
h3cDot11BSSAssocStatisTable = _H3cDot11BSSAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6)
)
if mibBuilder.loadTexts:
    h3cDot11BSSAssocStatisTable.setStatus("current")
_H3cDot11BSSAssocStatisEntry_Object = MibTableRow
h3cDot11BSSAssocStatisEntry = _H3cDot11BSSAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1)
)
h3cDot11BSSAssocStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11WlanID"),
)
if mibBuilder.loadTexts:
    h3cDot11BSSAssocStatisEntry.setStatus("current")
_H3cDot11BSSStationAssocSum_Type = Counter32
_H3cDot11BSSStationAssocSum_Object = MibTableColumn
h3cDot11BSSStationAssocSum = _H3cDot11BSSStationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 1),
    _H3cDot11BSSStationAssocSum_Type()
)
h3cDot11BSSStationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationAssocSum.setStatus("current")
_H3cDot11BSSStationAssocFailSum_Type = Counter32
_H3cDot11BSSStationAssocFailSum_Object = MibTableColumn
h3cDot11BSSStationAssocFailSum = _H3cDot11BSSStationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 2),
    _H3cDot11BSSStationAssocFailSum_Type()
)
h3cDot11BSSStationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationAssocFailSum.setStatus("current")
_H3cDot11BSSStationReassocSum_Type = Counter32
_H3cDot11BSSStationReassocSum_Object = MibTableColumn
h3cDot11BSSStationReassocSum = _H3cDot11BSSStationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 3),
    _H3cDot11BSSStationReassocSum_Type()
)
h3cDot11BSSStationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationReassocSum.setStatus("current")
_H3cDot11BSSStationAssocRejectSum_Type = Counter32
_H3cDot11BSSStationAssocRejectSum_Object = MibTableColumn
h3cDot11BSSStationAssocRejectSum = _H3cDot11BSSStationAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 4),
    _H3cDot11BSSStationAssocRejectSum_Type()
)
h3cDot11BSSStationAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationAssocRejectSum.setStatus("current")
_H3cDot11BSSStationExDeAssocSum_Type = Counter32
_H3cDot11BSSStationExDeAssocSum_Object = MibTableColumn
h3cDot11BSSStationExDeAssocSum = _H3cDot11BSSStationExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 5),
    _H3cDot11BSSStationExDeAssocSum_Type()
)
h3cDot11BSSStationExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationExDeAssocSum.setStatus("current")
_H3cDot11BSSStationCurAssocSum_Type = Integer32
_H3cDot11BSSStationCurAssocSum_Object = MibTableColumn
h3cDot11BSSStationCurAssocSum = _H3cDot11BSSStationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 6),
    _H3cDot11BSSStationCurAssocSum_Type()
)
h3cDot11BSSStationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationCurAssocSum.setStatus("current")
_H3cDot11BSSStationAssocReqSum_Type = Counter32
_H3cDot11BSSStationAssocReqSum_Object = MibTableColumn
h3cDot11BSSStationAssocReqSum = _H3cDot11BSSStationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 7),
    _H3cDot11BSSStationAssocReqSum_Type()
)
h3cDot11BSSStationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationAssocReqSum.setStatus("current")
_H3cDot11BSSStationCurAuthSum_Type = Integer32
_H3cDot11BSSStationCurAuthSum_Object = MibTableColumn
h3cDot11BSSStationCurAuthSum = _H3cDot11BSSStationCurAuthSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 6, 1, 8),
    _H3cDot11BSSStationCurAuthSum_Type()
)
h3cDot11BSSStationCurAuthSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11BSSStationCurAuthSum.setStatus("current")
_H3cDot11APLinkStatisTable_Object = MibTable
h3cDot11APLinkStatisTable = _H3cDot11APLinkStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 7)
)
if mibBuilder.loadTexts:
    h3cDot11APLinkStatisTable.setStatus("current")
_H3cDot11APLinkStatisEntry_Object = MibTableRow
h3cDot11APLinkStatisEntry = _H3cDot11APLinkStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 7, 1)
)
h3cDot11APLinkStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APLinkStatisEntry.setStatus("current")
_H3cDot11UpLinkUpDownTimes_Type = Counter32
_H3cDot11UpLinkUpDownTimes_Object = MibTableColumn
h3cDot11UpLinkUpDownTimes = _H3cDot11UpLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 7, 1, 1),
    _H3cDot11UpLinkUpDownTimes_Type()
)
h3cDot11UpLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11UpLinkUpDownTimes.setStatus("current")
_H3cDot11DownLinkUpDownTimes_Type = Counter32
_H3cDot11DownLinkUpDownTimes_Object = MibTableColumn
h3cDot11DownLinkUpDownTimes = _H3cDot11DownLinkUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 7, 1, 2),
    _H3cDot11DownLinkUpDownTimes_Type()
)
h3cDot11DownLinkUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DownLinkUpDownTimes.setStatus("current")
_H3cDot11RadioAssocStatisTable_Object = MibTable
h3cDot11RadioAssocStatisTable = _H3cDot11RadioAssocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8)
)
if mibBuilder.loadTexts:
    h3cDot11RadioAssocStatisTable.setStatus("current")
_H3cDot11RadioAssocStatisEntry_Object = MibTableRow
h3cDot11RadioAssocStatisEntry = _H3cDot11RadioAssocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1)
)
h3cDot11RadioAssocStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioAssocStatisEntry.setStatus("current")
_H3cDot11RadioStaAssocSum_Type = Counter32
_H3cDot11RadioStaAssocSum_Object = MibTableColumn
h3cDot11RadioStaAssocSum = _H3cDot11RadioStaAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 1),
    _H3cDot11RadioStaAssocSum_Type()
)
h3cDot11RadioStaAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaAssocSum.setStatus("current")
_H3cDot11RadioStaAssocFailSum_Type = Counter32
_H3cDot11RadioStaAssocFailSum_Object = MibTableColumn
h3cDot11RadioStaAssocFailSum = _H3cDot11RadioStaAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 2),
    _H3cDot11RadioStaAssocFailSum_Type()
)
h3cDot11RadioStaAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaAssocFailSum.setStatus("current")
_H3cDot11RadioStaReassocSum_Type = Counter32
_H3cDot11RadioStaReassocSum_Object = MibTableColumn
h3cDot11RadioStaReassocSum = _H3cDot11RadioStaReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 3),
    _H3cDot11RadioStaReassocSum_Type()
)
h3cDot11RadioStaReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaReassocSum.setStatus("current")
_H3cDot11RadioStaAssocRejectSum_Type = Counter32
_H3cDot11RadioStaAssocRejectSum_Object = MibTableColumn
h3cDot11RadioStaAssocRejectSum = _H3cDot11RadioStaAssocRejectSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 4),
    _H3cDot11RadioStaAssocRejectSum_Type()
)
h3cDot11RadioStaAssocRejectSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaAssocRejectSum.setStatus("current")
_H3cDot11RadioStaExDeAssocSum_Type = Counter32
_H3cDot11RadioStaExDeAssocSum_Object = MibTableColumn
h3cDot11RadioStaExDeAssocSum = _H3cDot11RadioStaExDeAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 5),
    _H3cDot11RadioStaExDeAssocSum_Type()
)
h3cDot11RadioStaExDeAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaExDeAssocSum.setStatus("current")
_H3cDot11RadioStaCurAssocSum_Type = Integer32
_H3cDot11RadioStaCurAssocSum_Object = MibTableColumn
h3cDot11RadioStaCurAssocSum = _H3cDot11RadioStaCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 8, 1, 6),
    _H3cDot11RadioStaCurAssocSum_Type()
)
h3cDot11RadioStaCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioStaCurAssocSum.setStatus("current")
_H3cDot11RadioMngFrameStatisTable_Object = MibTable
h3cDot11RadioMngFrameStatisTable = _H3cDot11RadioMngFrameStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 9)
)
if mibBuilder.loadTexts:
    h3cDot11RadioMngFrameStatisTable.setStatus("current")
_H3cDot11RadioMngFrameStatisEntry_Object = MibTableRow
h3cDot11RadioMngFrameStatisEntry = _H3cDot11RadioMngFrameStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 9, 1)
)
h3cDot11RadioMngFrameStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioStatisIndex"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11MngFrameType"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioMngFrameStatisEntry.setStatus("current")
_H3cDot11RadioStatisIndex_Type = H3cDot11RadioElementIndex
_H3cDot11RadioStatisIndex_Object = MibTableColumn
h3cDot11RadioStatisIndex = _H3cDot11RadioStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 9, 1, 1),
    _H3cDot11RadioStatisIndex_Type()
)
h3cDot11RadioStatisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioStatisIndex.setStatus("current")


class _H3cDot11MngFrameType_Type(Integer32):
    """Custom type h3cDot11MngFrameType based on Integer32"""
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


_H3cDot11MngFrameType_Type.__name__ = "Integer32"
_H3cDot11MngFrameType_Object = MibTableColumn
h3cDot11MngFrameType = _H3cDot11MngFrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 9, 1, 2),
    _H3cDot11MngFrameType_Type()
)
h3cDot11MngFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11MngFrameType.setStatus("current")
_H3cDot11MngFrameCnt_Type = Counter32
_H3cDot11MngFrameCnt_Object = MibTableColumn
h3cDot11MngFrameCnt = _H3cDot11MngFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 9, 1, 3),
    _H3cDot11MngFrameCnt_Type()
)
h3cDot11MngFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MngFrameCnt.setStatus("current")
_H3cDot11APAuthFailStatisTable_Object = MibTable
h3cDot11APAuthFailStatisTable = _H3cDot11APAuthFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 10)
)
if mibBuilder.loadTexts:
    h3cDot11APAuthFailStatisTable.setStatus("current")
_H3cDot11APAuthFailStatisEntry_Object = MibTableRow
h3cDot11APAuthFailStatisEntry = _H3cDot11APAuthFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 10, 1)
)
h3cDot11APAuthFailStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APAuthFailStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APAuthFailStatisEntry.setStatus("current")


class _H3cDot11APAuthFailStatisType_Type(Integer32):
    """Custom type h3cDot11APAuthFailStatisType based on Integer32"""
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


_H3cDot11APAuthFailStatisType_Type.__name__ = "Integer32"
_H3cDot11APAuthFailStatisType_Object = MibTableColumn
h3cDot11APAuthFailStatisType = _H3cDot11APAuthFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 10, 1, 1),
    _H3cDot11APAuthFailStatisType_Type()
)
h3cDot11APAuthFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APAuthFailStatisType.setStatus("current")
_H3cDot11APAuthFailStatisCnt_Type = Counter32
_H3cDot11APAuthFailStatisCnt_Object = MibTableColumn
h3cDot11APAuthFailStatisCnt = _H3cDot11APAuthFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 10, 1, 2),
    _H3cDot11APAuthFailStatisCnt_Type()
)
h3cDot11APAuthFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAuthFailStatisCnt.setStatus("current")
_H3cDot11APAssocFailStatisTable_Object = MibTable
h3cDot11APAssocFailStatisTable = _H3cDot11APAssocFailStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 11)
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatisTable.setStatus("current")
_H3cDot11APAssocFailStatisEntry_Object = MibTableRow
h3cDot11APAssocFailStatisEntry = _H3cDot11APAssocFailStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 11, 1)
)
h3cDot11APAssocFailStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APAssocFailStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatisEntry.setStatus("current")


class _H3cDot11APAssocFailStatisType_Type(Integer32):
    """Custom type h3cDot11APAssocFailStatisType based on Integer32"""
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


_H3cDot11APAssocFailStatisType_Type.__name__ = "Integer32"
_H3cDot11APAssocFailStatisType_Object = MibTableColumn
h3cDot11APAssocFailStatisType = _H3cDot11APAssocFailStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 11, 1, 1),
    _H3cDot11APAssocFailStatisType_Type()
)
h3cDot11APAssocFailStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatisType.setStatus("current")
_H3cDot11APAssocFailStatisCnt_Type = Counter32
_H3cDot11APAssocFailStatisCnt_Object = MibTableColumn
h3cDot11APAssocFailStatisCnt = _H3cDot11APAssocFailStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 11, 1, 2),
    _H3cDot11APAssocFailStatisCnt_Type()
)
h3cDot11APAssocFailStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatisCnt.setStatus("current")
_H3cDot11APReassocStatisTable_Object = MibTable
h3cDot11APReassocStatisTable = _H3cDot11APReassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 12)
)
if mibBuilder.loadTexts:
    h3cDot11APReassocStatisTable.setStatus("current")
_H3cDot11APReassocStatisEntry_Object = MibTableRow
h3cDot11APReassocStatisEntry = _H3cDot11APReassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 12, 1)
)
h3cDot11APReassocStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APReassocStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APReassocStatisEntry.setStatus("current")


class _H3cDot11APReassocStatisType_Type(Integer32):
    """Custom type h3cDot11APReassocStatisType based on Integer32"""
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


_H3cDot11APReassocStatisType_Type.__name__ = "Integer32"
_H3cDot11APReassocStatisType_Object = MibTableColumn
h3cDot11APReassocStatisType = _H3cDot11APReassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 12, 1, 1),
    _H3cDot11APReassocStatisType_Type()
)
h3cDot11APReassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APReassocStatisType.setStatus("current")
_H3cDot11APReassocStatisCnt_Type = Counter32
_H3cDot11APReassocStatisCnt_Object = MibTableColumn
h3cDot11APReassocStatisCnt = _H3cDot11APReassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 12, 1, 2),
    _H3cDot11APReassocStatisCnt_Type()
)
h3cDot11APReassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APReassocStatisCnt.setStatus("current")
_H3cDot11APUserAuthStatisTable_Object = MibTable
h3cDot11APUserAuthStatisTable = _H3cDot11APUserAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 13)
)
if mibBuilder.loadTexts:
    h3cDot11APUserAuthStatisTable.setStatus("current")
_H3cDot11APUserAuthStatisEntry_Object = MibTableRow
h3cDot11APUserAuthStatisEntry = _H3cDot11APUserAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 13, 1)
)
h3cDot11APUserAuthStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11UserAuthStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APUserAuthStatisEntry.setStatus("current")


class _H3cDot11UserAuthStatisType_Type(Integer32):
    """Custom type h3cDot11UserAuthStatisType based on Integer32"""
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


_H3cDot11UserAuthStatisType_Type.__name__ = "Integer32"
_H3cDot11UserAuthStatisType_Object = MibTableColumn
h3cDot11UserAuthStatisType = _H3cDot11UserAuthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 13, 1, 1),
    _H3cDot11UserAuthStatisType_Type()
)
h3cDot11UserAuthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11UserAuthStatisType.setStatus("current")
_H3cDot11UserAuthStatisCnt_Type = Counter32
_H3cDot11UserAuthStatisCnt_Object = MibTableColumn
h3cDot11UserAuthStatisCnt = _H3cDot11UserAuthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 13, 1, 2),
    _H3cDot11UserAuthStatisCnt_Type()
)
h3cDot11UserAuthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11UserAuthStatisCnt.setStatus("current")
_H3cDot11APDeauthStatisTable_Object = MibTable
h3cDot11APDeauthStatisTable = _H3cDot11APDeauthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 14)
)
if mibBuilder.loadTexts:
    h3cDot11APDeauthStatisTable.setStatus("current")
_H3cDot11APDeauthStatisEntry_Object = MibTableRow
h3cDot11APDeauthStatisEntry = _H3cDot11APDeauthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 14, 1)
)
h3cDot11APDeauthStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APDeauthStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APDeauthStatisEntry.setStatus("current")


class _H3cDot11APDeauthStatisType_Type(Integer32):
    """Custom type h3cDot11APDeauthStatisType based on Integer32"""
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


_H3cDot11APDeauthStatisType_Type.__name__ = "Integer32"
_H3cDot11APDeauthStatisType_Object = MibTableColumn
h3cDot11APDeauthStatisType = _H3cDot11APDeauthStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 14, 1, 1),
    _H3cDot11APDeauthStatisType_Type()
)
h3cDot11APDeauthStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APDeauthStatisType.setStatus("current")
_H3cDot11APDeauthStatisCnt_Type = Counter32
_H3cDot11APDeauthStatisCnt_Object = MibTableColumn
h3cDot11APDeauthStatisCnt = _H3cDot11APDeauthStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 14, 1, 2),
    _H3cDot11APDeauthStatisCnt_Type()
)
h3cDot11APDeauthStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APDeauthStatisCnt.setStatus("current")
_H3cDot11APDeassocStatisTable_Object = MibTable
h3cDot11APDeassocStatisTable = _H3cDot11APDeassocStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 15)
)
if mibBuilder.loadTexts:
    h3cDot11APDeassocStatisTable.setStatus("current")
_H3cDot11APDeassocStatisEntry_Object = MibTableRow
h3cDot11APDeassocStatisEntry = _H3cDot11APDeassocStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 15, 1)
)
h3cDot11APDeassocStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APDeassocStatisType"),
)
if mibBuilder.loadTexts:
    h3cDot11APDeassocStatisEntry.setStatus("current")


class _H3cDot11APDeassocStatisType_Type(Integer32):
    """Custom type h3cDot11APDeassocStatisType based on Integer32"""
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


_H3cDot11APDeassocStatisType_Type.__name__ = "Integer32"
_H3cDot11APDeassocStatisType_Object = MibTableColumn
h3cDot11APDeassocStatisType = _H3cDot11APDeassocStatisType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 15, 1, 1),
    _H3cDot11APDeassocStatisType_Type()
)
h3cDot11APDeassocStatisType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APDeassocStatisType.setStatus("current")
_H3cDot11APDeassocStatisCnt_Type = Counter32
_H3cDot11APDeassocStatisCnt_Object = MibTableColumn
h3cDot11APDeassocStatisCnt = _H3cDot11APDeassocStatisCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 15, 1, 2),
    _H3cDot11APDeassocStatisCnt_Type()
)
h3cDot11APDeassocStatisCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APDeassocStatisCnt.setStatus("current")
_H3cDot11APAssocFailStatis2Table_Object = MibTable
h3cDot11APAssocFailStatis2Table = _H3cDot11APAssocFailStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 16)
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis2Table.setStatus("current")
_H3cDot11APAssocFailStatis2Entry_Object = MibTableRow
h3cDot11APAssocFailStatis2Entry = _H3cDot11APAssocFailStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 16, 1)
)
h3cDot11APAssocFailStatis2Entry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APAssocFailStatis2Type"),
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis2Entry.setStatus("current")


class _H3cDot11APAssocFailStatis2Type_Type(Integer32):
    """Custom type h3cDot11APAssocFailStatis2Type based on Integer32"""
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


_H3cDot11APAssocFailStatis2Type_Type.__name__ = "Integer32"
_H3cDot11APAssocFailStatis2Type_Object = MibTableColumn
h3cDot11APAssocFailStatis2Type = _H3cDot11APAssocFailStatis2Type_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 16, 1, 1),
    _H3cDot11APAssocFailStatis2Type_Type()
)
h3cDot11APAssocFailStatis2Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis2Type.setStatus("current")
_H3cDot11APAssocFailStatis2Cnt_Type = Counter32
_H3cDot11APAssocFailStatis2Cnt_Object = MibTableColumn
h3cDot11APAssocFailStatis2Cnt = _H3cDot11APAssocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 16, 1, 2),
    _H3cDot11APAssocFailStatis2Cnt_Type()
)
h3cDot11APAssocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis2Cnt.setStatus("current")
_H3cDot11APIfStatisTable_Object = MibTable
h3cDot11APIfStatisTable = _H3cDot11APIfStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17)
)
if mibBuilder.loadTexts:
    h3cDot11APIfStatisTable.setStatus("current")
_H3cDot11APIfStatisEntry_Object = MibTableRow
h3cDot11APIfStatisEntry = _H3cDot11APIfStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1)
)
h3cDot11APIfStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APIfStatisEntry.setStatus("current")
_H3cDot11APIfInPkts_Type = Counter32
_H3cDot11APIfInPkts_Object = MibTableColumn
h3cDot11APIfInPkts = _H3cDot11APIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 1),
    _H3cDot11APIfInPkts_Type()
)
h3cDot11APIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInPkts.setStatus("current")
_H3cDot11APIfInNormalPkts_Type = Counter32
_H3cDot11APIfInNormalPkts_Object = MibTableColumn
h3cDot11APIfInNormalPkts = _H3cDot11APIfInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 2),
    _H3cDot11APIfInNormalPkts_Type()
)
h3cDot11APIfInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInNormalPkts.setStatus("current")
_H3cDot11APIfInErrorPkts_Type = Counter32
_H3cDot11APIfInErrorPkts_Object = MibTableColumn
h3cDot11APIfInErrorPkts = _H3cDot11APIfInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 3),
    _H3cDot11APIfInErrorPkts_Type()
)
h3cDot11APIfInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInErrorPkts.setStatus("current")
_H3cDot11APIfOutPkts_Type = Counter32
_H3cDot11APIfOutPkts_Object = MibTableColumn
h3cDot11APIfOutPkts = _H3cDot11APIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 4),
    _H3cDot11APIfOutPkts_Type()
)
h3cDot11APIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutPkts.setStatus("current")
_H3cDot11APIfInOctets_Type = Counter32
_H3cDot11APIfInOctets_Object = MibTableColumn
h3cDot11APIfInOctets = _H3cDot11APIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 5),
    _H3cDot11APIfInOctets_Type()
)
h3cDot11APIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInOctets.setStatus("current")
_H3cDot11APIfOutOctets_Type = Counter32
_H3cDot11APIfOutOctets_Object = MibTableColumn
h3cDot11APIfOutOctets = _H3cDot11APIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 6),
    _H3cDot11APIfOutOctets_Type()
)
h3cDot11APIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutOctets.setStatus("current")
_H3cDot11APIfFlowOut_Type = Unsigned32
_H3cDot11APIfFlowOut_Object = MibTableColumn
h3cDot11APIfFlowOut = _H3cDot11APIfFlowOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 7),
    _H3cDot11APIfFlowOut_Type()
)
h3cDot11APIfFlowOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfFlowOut.setStatus("current")
_H3cDot11APIfFlowIN_Type = Unsigned32
_H3cDot11APIfFlowIN_Object = MibTableColumn
h3cDot11APIfFlowIN = _H3cDot11APIfFlowIN_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 8),
    _H3cDot11APIfFlowIN_Type()
)
h3cDot11APIfFlowIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfFlowIN.setStatus("current")
_H3cDot11APIfInUcastPkts_Type = Counter32
_H3cDot11APIfInUcastPkts_Object = MibTableColumn
h3cDot11APIfInUcastPkts = _H3cDot11APIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 9),
    _H3cDot11APIfInUcastPkts_Type()
)
h3cDot11APIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInUcastPkts.setStatus("current")
_H3cDot11APIfInNUcastPkts_Type = Counter32
_H3cDot11APIfInNUcastPkts_Object = MibTableColumn
h3cDot11APIfInNUcastPkts = _H3cDot11APIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 10),
    _H3cDot11APIfInNUcastPkts_Type()
)
h3cDot11APIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInNUcastPkts.setStatus("current")
_H3cDot11APIfInDiscardPkts_Type = Counter32
_H3cDot11APIfInDiscardPkts_Object = MibTableColumn
h3cDot11APIfInDiscardPkts = _H3cDot11APIfInDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 11),
    _H3cDot11APIfInDiscardPkts_Type()
)
h3cDot11APIfInDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInDiscardPkts.setStatus("current")
_H3cDot11APIfOutUcastPkts_Type = Counter32
_H3cDot11APIfOutUcastPkts_Object = MibTableColumn
h3cDot11APIfOutUcastPkts = _H3cDot11APIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 12),
    _H3cDot11APIfOutUcastPkts_Type()
)
h3cDot11APIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutUcastPkts.setStatus("current")
_H3cDot11APIfOutNUcastPkts_Type = Counter32
_H3cDot11APIfOutNUcastPkts_Object = MibTableColumn
h3cDot11APIfOutNUcastPkts = _H3cDot11APIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 13),
    _H3cDot11APIfOutNUcastPkts_Type()
)
h3cDot11APIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutNUcastPkts.setStatus("current")
_H3cDot11APIfOutDiscardPkts_Type = Counter32
_H3cDot11APIfOutDiscardPkts_Object = MibTableColumn
h3cDot11APIfOutDiscardPkts = _H3cDot11APIfOutDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 14),
    _H3cDot11APIfOutDiscardPkts_Type()
)
h3cDot11APIfOutDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutDiscardPkts.setStatus("current")
_H3cDot11APIfOutErrorPkts_Type = Counter32
_H3cDot11APIfOutErrorPkts_Object = MibTableColumn
h3cDot11APIfOutErrorPkts = _H3cDot11APIfOutErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 15),
    _H3cDot11APIfOutErrorPkts_Type()
)
h3cDot11APIfOutErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutErrorPkts.setStatus("current")
_H3cDot11APIfUpdownTimes_Type = Counter32
_H3cDot11APIfUpdownTimes_Object = MibTableColumn
h3cDot11APIfUpdownTimes = _H3cDot11APIfUpdownTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 16),
    _H3cDot11APIfUpdownTimes_Type()
)
h3cDot11APIfUpdownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfUpdownTimes.setStatus("current")
_H3cDot11APIfStatusKeepTime_Type = TimeTicks
_H3cDot11APIfStatusKeepTime_Object = MibTableColumn
h3cDot11APIfStatusKeepTime = _H3cDot11APIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 17),
    _H3cDot11APIfStatusKeepTime_Type()
)
h3cDot11APIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfStatusKeepTime.setStatus("current")


class _H3cDot11APIfOperStatus_Type(Integer32):
    """Custom type h3cDot11APIfOperStatus based on Integer32"""
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


_H3cDot11APIfOperStatus_Type.__name__ = "Integer32"
_H3cDot11APIfOperStatus_Object = MibTableColumn
h3cDot11APIfOperStatus = _H3cDot11APIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 18),
    _H3cDot11APIfOperStatus_Type()
)
h3cDot11APIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOperStatus.setStatus("current")
_H3cDot11APIfInBrdcastPkts_Type = Counter64
_H3cDot11APIfInBrdcastPkts_Object = MibTableColumn
h3cDot11APIfInBrdcastPkts = _H3cDot11APIfInBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 19),
    _H3cDot11APIfInBrdcastPkts_Type()
)
h3cDot11APIfInBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInBrdcastPkts.setStatus("current")
_H3cDot11APIfOutBrdcastPkts_Type = Counter64
_H3cDot11APIfOutBrdcastPkts_Object = MibTableColumn
h3cDot11APIfOutBrdcastPkts = _H3cDot11APIfOutBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 20),
    _H3cDot11APIfOutBrdcastPkts_Type()
)
h3cDot11APIfOutBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutBrdcastPkts.setStatus("current")
_H3cDot11APIfInMulcastPkts_Type = Counter64
_H3cDot11APIfInMulcastPkts_Object = MibTableColumn
h3cDot11APIfInMulcastPkts = _H3cDot11APIfInMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 21),
    _H3cDot11APIfInMulcastPkts_Type()
)
h3cDot11APIfInMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInMulcastPkts.setStatus("current")
_H3cDot11APIfOutMulcastPkts_Type = Counter64
_H3cDot11APIfOutMulcastPkts_Object = MibTableColumn
h3cDot11APIfOutMulcastPkts = _H3cDot11APIfOutMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 22),
    _H3cDot11APIfOutMulcastPkts_Type()
)
h3cDot11APIfOutMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutMulcastPkts.setStatus("current")
_H3cDot11APIfInPayloadOctets_Type = Counter64
_H3cDot11APIfInPayloadOctets_Object = MibTableColumn
h3cDot11APIfInPayloadOctets = _H3cDot11APIfInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 23),
    _H3cDot11APIfInPayloadOctets_Type()
)
h3cDot11APIfInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInPayloadOctets.setStatus("current")
_H3cDot11APIfOutPayloadOctets_Type = Counter64
_H3cDot11APIfOutPayloadOctets_Object = MibTableColumn
h3cDot11APIfOutPayloadOctets = _H3cDot11APIfOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 17, 1, 24),
    _H3cDot11APIfOutPayloadOctets_Type()
)
h3cDot11APIfOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutPayloadOctets.setStatus("current")
_H3cDot11RadioMngFrmStatisTable_Object = MibTable
h3cDot11RadioMngFrmStatisTable = _H3cDot11RadioMngFrmStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 18)
)
if mibBuilder.loadTexts:
    h3cDot11RadioMngFrmStatisTable.setStatus("current")
_H3cDot11RadioMngFrmStatisEntry_Object = MibTableRow
h3cDot11RadioMngFrmStatisEntry = _H3cDot11RadioMngFrmStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 18, 1)
)
h3cDot11RadioMngFrmStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11MngFrmType"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioMngFrmStatisEntry.setStatus("current")


class _H3cDot11MngFrmType_Type(Integer32):
    """Custom type h3cDot11MngFrmType based on Integer32"""
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


_H3cDot11MngFrmType_Type.__name__ = "Integer32"
_H3cDot11MngFrmType_Object = MibTableColumn
h3cDot11MngFrmType = _H3cDot11MngFrmType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 18, 1, 1),
    _H3cDot11MngFrmType_Type()
)
h3cDot11MngFrmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11MngFrmType.setStatus("current")
_H3cDot11MngFrmCnt_Type = Counter32
_H3cDot11MngFrmCnt_Object = MibTableColumn
h3cDot11MngFrmCnt = _H3cDot11MngFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 18, 1, 2),
    _H3cDot11MngFrmCnt_Type()
)
h3cDot11MngFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11MngFrmCnt.setStatus("current")
_H3cDot11APPacketSizeStatisTable_Object = MibTable
h3cDot11APPacketSizeStatisTable = _H3cDot11APPacketSizeStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 19)
)
if mibBuilder.loadTexts:
    h3cDot11APPacketSizeStatisTable.setStatus("current")
_H3cDot11APPacketSizeStatisEntry_Object = MibTableRow
h3cDot11APPacketSizeStatisEntry = _H3cDot11APPacketSizeStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 19, 1)
)
h3cDot11APPacketSizeStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APPacketSize"),
)
if mibBuilder.loadTexts:
    h3cDot11APPacketSizeStatisEntry.setStatus("current")


class _H3cDot11APPacketSize_Type(Integer32):
    """Custom type h3cDot11APPacketSize based on Integer32"""
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


_H3cDot11APPacketSize_Type.__name__ = "Integer32"
_H3cDot11APPacketSize_Object = MibTableColumn
h3cDot11APPacketSize = _H3cDot11APPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 19, 1, 1),
    _H3cDot11APPacketSize_Type()
)
h3cDot11APPacketSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APPacketSize.setStatus("current")
_H3cDot11APRXPacketSizeCount_Type = Counter64
_H3cDot11APRXPacketSizeCount_Object = MibTableColumn
h3cDot11APRXPacketSizeCount = _H3cDot11APRXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 19, 1, 2),
    _H3cDot11APRXPacketSizeCount_Type()
)
h3cDot11APRXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APRXPacketSizeCount.setStatus("current")
_H3cDot11APTXPacketSizeCount_Type = Counter64
_H3cDot11APTXPacketSizeCount_Object = MibTableColumn
h3cDot11APTXPacketSizeCount = _H3cDot11APTXPacketSizeCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 19, 1, 3),
    _H3cDot11APTXPacketSizeCount_Type()
)
h3cDot11APTXPacketSizeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTXPacketSizeCount.setStatus("current")
_H3cDot11APPacketRateStatisTable_Object = MibTable
h3cDot11APPacketRateStatisTable = _H3cDot11APPacketRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 20)
)
if mibBuilder.loadTexts:
    h3cDot11APPacketRateStatisTable.setStatus("current")
_H3cDot11APPacketRateStatisEntry_Object = MibTableRow
h3cDot11APPacketRateStatisEntry = _H3cDot11APPacketRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 20, 1)
)
h3cDot11APPacketRateStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APPacketRate"),
)
if mibBuilder.loadTexts:
    h3cDot11APPacketRateStatisEntry.setStatus("current")
_H3cDot11APPacketRate_Type = Integer32
_H3cDot11APPacketRate_Object = MibTableColumn
h3cDot11APPacketRate = _H3cDot11APPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 20, 1, 1),
    _H3cDot11APPacketRate_Type()
)
h3cDot11APPacketRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APPacketRate.setStatus("current")
_H3cDot11APRXPacketRateCount_Type = Counter64
_H3cDot11APRXPacketRateCount_Object = MibTableColumn
h3cDot11APRXPacketRateCount = _H3cDot11APRXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 20, 1, 2),
    _H3cDot11APRXPacketRateCount_Type()
)
h3cDot11APRXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APRXPacketRateCount.setStatus("current")
_H3cDot11APTXPacketRateCount_Type = Counter64
_H3cDot11APTXPacketRateCount_Object = MibTableColumn
h3cDot11APTXPacketRateCount = _H3cDot11APTXPacketRateCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 20, 1, 3),
    _H3cDot11APTXPacketRateCount_Type()
)
h3cDot11APTXPacketRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTXPacketRateCount.setStatus("current")
_H3cDot11APPacketMCSRateStatisTable_Object = MibTable
h3cDot11APPacketMCSRateStatisTable = _H3cDot11APPacketMCSRateStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 21)
)
if mibBuilder.loadTexts:
    h3cDot11APPacketMCSRateStatisTable.setStatus("current")
_H3cDot11APPacketMCSRateStatisEntry_Object = MibTableRow
h3cDot11APPacketMCSRateStatisEntry = _H3cDot11APPacketMCSRateStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 21, 1)
)
h3cDot11APPacketMCSRateStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APPacketMCSRate"),
)
if mibBuilder.loadTexts:
    h3cDot11APPacketMCSRateStatisEntry.setStatus("current")
_H3cDot11APPacketMCSRate_Type = Integer32
_H3cDot11APPacketMCSRate_Object = MibTableColumn
h3cDot11APPacketMCSRate = _H3cDot11APPacketMCSRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 21, 1, 1),
    _H3cDot11APPacketMCSRate_Type()
)
h3cDot11APPacketMCSRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APPacketMCSRate.setStatus("current")
_H3cDot11APRXPacketMCSRateCount_Type = Counter64
_H3cDot11APRXPacketMCSRateCount_Object = MibTableColumn
h3cDot11APRXPacketMCSRateCount = _H3cDot11APRXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 21, 1, 2),
    _H3cDot11APRXPacketMCSRateCount_Type()
)
h3cDot11APRXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APRXPacketMCSRateCount.setStatus("current")
_H3cDot11APTXPacketMCSRateCount_Type = Counter64
_H3cDot11APTXPacketMCSRateCount_Object = MibTableColumn
h3cDot11APTXPacketMCSRateCount = _H3cDot11APTXPacketMCSRateCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 21, 1, 3),
    _H3cDot11APTXPacketMCSRateCount_Type()
)
h3cDot11APTXPacketMCSRateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APTXPacketMCSRateCount.setStatus("current")
_H3cDot11APAssocFailStatis3Table_Object = MibTable
h3cDot11APAssocFailStatis3Table = _H3cDot11APAssocFailStatis3Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22)
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3Table.setStatus("current")
_H3cDot11APAssocFailStatis3Entry_Object = MibTableRow
h3cDot11APAssocFailStatis3Entry = _H3cDot11APAssocFailStatis3Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1)
)
h3cDot11APAssocFailStatis3Entry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3Entry.setStatus("current")
_H3cDot11APAssocFailStatis3SRCnt_Type = Counter32
_H3cDot11APAssocFailStatis3SRCnt_Object = MibTableColumn
h3cDot11APAssocFailStatis3SRCnt = _H3cDot11APAssocFailStatis3SRCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1, 1),
    _H3cDot11APAssocFailStatis3SRCnt_Type()
)
h3cDot11APAssocFailStatis3SRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3SRCnt.setStatus("current")
_H3cDot11APAssocFailStatis3NSRCnt_Type = Counter32
_H3cDot11APAssocFailStatis3NSRCnt_Object = MibTableColumn
h3cDot11APAssocFailStatis3NSRCnt = _H3cDot11APAssocFailStatis3NSRCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1, 2),
    _H3cDot11APAssocFailStatis3NSRCnt_Type()
)
h3cDot11APAssocFailStatis3NSRCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3NSRCnt.setStatus("current")
_H3cDot11APAssocFailStatis3URCCnt_Type = Counter32
_H3cDot11APAssocFailStatis3URCCnt_Object = MibTableColumn
h3cDot11APAssocFailStatis3URCCnt = _H3cDot11APAssocFailStatis3URCCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1, 3),
    _H3cDot11APAssocFailStatis3URCCnt_Type()
)
h3cDot11APAssocFailStatis3URCCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3URCCnt.setStatus("current")
_H3cDot11APAssocFailStatis3RFCnt_Type = Counter32
_H3cDot11APAssocFailStatis3RFCnt_Object = MibTableColumn
h3cDot11APAssocFailStatis3RFCnt = _H3cDot11APAssocFailStatis3RFCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1, 4),
    _H3cDot11APAssocFailStatis3RFCnt_Type()
)
h3cDot11APAssocFailStatis3RFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3RFCnt.setStatus("current")
_H3cDot11APAssocFailStatis3OtherCnt_Type = Counter32
_H3cDot11APAssocFailStatis3OtherCnt_Object = MibTableColumn
h3cDot11APAssocFailStatis3OtherCnt = _H3cDot11APAssocFailStatis3OtherCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 22, 1, 5),
    _H3cDot11APAssocFailStatis3OtherCnt_Type()
)
h3cDot11APAssocFailStatis3OtherCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APAssocFailStatis3OtherCnt.setStatus("current")
_H3cDot11APIfStatisByAPIDTable_Object = MibTable
h3cDot11APIfStatisByAPIDTable = _H3cDot11APIfStatisByAPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23)
)
if mibBuilder.loadTexts:
    h3cDot11APIfStatisByAPIDTable.setStatus("current")
_H3cDot11APIfStatisByAPIDEntry_Object = MibTableRow
h3cDot11APIfStatisByAPIDEntry = _H3cDot11APIfStatisByAPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1)
)
h3cDot11APIfStatisByAPIDEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APIfStatisByAPIDEntry.setStatus("current")
_H3cDot11APIfInPkts2_Type = Counter64
_H3cDot11APIfInPkts2_Object = MibTableColumn
h3cDot11APIfInPkts2 = _H3cDot11APIfInPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 1),
    _H3cDot11APIfInPkts2_Type()
)
h3cDot11APIfInPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInPkts2.setStatus("current")
_H3cDot11APIfInNormalPkts2_Type = Counter64
_H3cDot11APIfInNormalPkts2_Object = MibTableColumn
h3cDot11APIfInNormalPkts2 = _H3cDot11APIfInNormalPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 2),
    _H3cDot11APIfInNormalPkts2_Type()
)
h3cDot11APIfInNormalPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInNormalPkts2.setStatus("current")
_H3cDot11APIfInErrorPkts2_Type = Counter64
_H3cDot11APIfInErrorPkts2_Object = MibTableColumn
h3cDot11APIfInErrorPkts2 = _H3cDot11APIfInErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 3),
    _H3cDot11APIfInErrorPkts2_Type()
)
h3cDot11APIfInErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInErrorPkts2.setStatus("current")
_H3cDot11APIfOutPkts2_Type = Counter64
_H3cDot11APIfOutPkts2_Object = MibTableColumn
h3cDot11APIfOutPkts2 = _H3cDot11APIfOutPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 4),
    _H3cDot11APIfOutPkts2_Type()
)
h3cDot11APIfOutPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutPkts2.setStatus("current")
_H3cDot11APIfInOctets2_Type = Counter64
_H3cDot11APIfInOctets2_Object = MibTableColumn
h3cDot11APIfInOctets2 = _H3cDot11APIfInOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 5),
    _H3cDot11APIfInOctets2_Type()
)
h3cDot11APIfInOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInOctets2.setStatus("current")
_H3cDot11APIfOutOctets2_Type = Counter64
_H3cDot11APIfOutOctets2_Object = MibTableColumn
h3cDot11APIfOutOctets2 = _H3cDot11APIfOutOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 6),
    _H3cDot11APIfOutOctets2_Type()
)
h3cDot11APIfOutOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutOctets2.setStatus("current")
_H3cDot11APIfFlowOut2_Type = Unsigned32
_H3cDot11APIfFlowOut2_Object = MibTableColumn
h3cDot11APIfFlowOut2 = _H3cDot11APIfFlowOut2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 7),
    _H3cDot11APIfFlowOut2_Type()
)
h3cDot11APIfFlowOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfFlowOut2.setStatus("current")
_H3cDot11APIfFlowIN2_Type = Unsigned32
_H3cDot11APIfFlowIN2_Object = MibTableColumn
h3cDot11APIfFlowIN2 = _H3cDot11APIfFlowIN2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 8),
    _H3cDot11APIfFlowIN2_Type()
)
h3cDot11APIfFlowIN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfFlowIN2.setStatus("current")
_H3cDot11APIfInUcastPkts2_Type = Counter64
_H3cDot11APIfInUcastPkts2_Object = MibTableColumn
h3cDot11APIfInUcastPkts2 = _H3cDot11APIfInUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 9),
    _H3cDot11APIfInUcastPkts2_Type()
)
h3cDot11APIfInUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInUcastPkts2.setStatus("current")
_H3cDot11APIfInNUcastPkts2_Type = Counter64
_H3cDot11APIfInNUcastPkts2_Object = MibTableColumn
h3cDot11APIfInNUcastPkts2 = _H3cDot11APIfInNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 10),
    _H3cDot11APIfInNUcastPkts2_Type()
)
h3cDot11APIfInNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInNUcastPkts2.setStatus("current")
_H3cDot11APIfInDiscardPkts2_Type = Counter64
_H3cDot11APIfInDiscardPkts2_Object = MibTableColumn
h3cDot11APIfInDiscardPkts2 = _H3cDot11APIfInDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 11),
    _H3cDot11APIfInDiscardPkts2_Type()
)
h3cDot11APIfInDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInDiscardPkts2.setStatus("current")
_H3cDot11APIfOutUcastPkts2_Type = Counter64
_H3cDot11APIfOutUcastPkts2_Object = MibTableColumn
h3cDot11APIfOutUcastPkts2 = _H3cDot11APIfOutUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 12),
    _H3cDot11APIfOutUcastPkts2_Type()
)
h3cDot11APIfOutUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutUcastPkts2.setStatus("current")
_H3cDot11APIfOutNUcastPkts2_Type = Counter64
_H3cDot11APIfOutNUcastPkts2_Object = MibTableColumn
h3cDot11APIfOutNUcastPkts2 = _H3cDot11APIfOutNUcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 13),
    _H3cDot11APIfOutNUcastPkts2_Type()
)
h3cDot11APIfOutNUcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutNUcastPkts2.setStatus("current")
_H3cDot11APIfOutDiscardPkts2_Type = Counter64
_H3cDot11APIfOutDiscardPkts2_Object = MibTableColumn
h3cDot11APIfOutDiscardPkts2 = _H3cDot11APIfOutDiscardPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 14),
    _H3cDot11APIfOutDiscardPkts2_Type()
)
h3cDot11APIfOutDiscardPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutDiscardPkts2.setStatus("current")
_H3cDot11APIfOutErrorPkts2_Type = Counter64
_H3cDot11APIfOutErrorPkts2_Object = MibTableColumn
h3cDot11APIfOutErrorPkts2 = _H3cDot11APIfOutErrorPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 15),
    _H3cDot11APIfOutErrorPkts2_Type()
)
h3cDot11APIfOutErrorPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutErrorPkts2.setStatus("current")
_H3cDot11APIfUpdownTimes2_Type = Counter32
_H3cDot11APIfUpdownTimes2_Object = MibTableColumn
h3cDot11APIfUpdownTimes2 = _H3cDot11APIfUpdownTimes2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 16),
    _H3cDot11APIfUpdownTimes2_Type()
)
h3cDot11APIfUpdownTimes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfUpdownTimes2.setStatus("current")
_H3cDot11APIfStatusKeepTime2_Type = TimeTicks
_H3cDot11APIfStatusKeepTime2_Object = MibTableColumn
h3cDot11APIfStatusKeepTime2 = _H3cDot11APIfStatusKeepTime2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 17),
    _H3cDot11APIfStatusKeepTime2_Type()
)
h3cDot11APIfStatusKeepTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfStatusKeepTime2.setStatus("current")


class _H3cDot11APIfOperStatus2_Type(Integer32):
    """Custom type h3cDot11APIfOperStatus2 based on Integer32"""
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


_H3cDot11APIfOperStatus2_Type.__name__ = "Integer32"
_H3cDot11APIfOperStatus2_Object = MibTableColumn
h3cDot11APIfOperStatus2 = _H3cDot11APIfOperStatus2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 18),
    _H3cDot11APIfOperStatus2_Type()
)
h3cDot11APIfOperStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOperStatus2.setStatus("current")
_H3cDot11APIfInBrdcastPkts2_Type = Counter64
_H3cDot11APIfInBrdcastPkts2_Object = MibTableColumn
h3cDot11APIfInBrdcastPkts2 = _H3cDot11APIfInBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 19),
    _H3cDot11APIfInBrdcastPkts2_Type()
)
h3cDot11APIfInBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInBrdcastPkts2.setStatus("current")
_H3cDot11APIfOutBrdcastPkts2_Type = Counter64
_H3cDot11APIfOutBrdcastPkts2_Object = MibTableColumn
h3cDot11APIfOutBrdcastPkts2 = _H3cDot11APIfOutBrdcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 20),
    _H3cDot11APIfOutBrdcastPkts2_Type()
)
h3cDot11APIfOutBrdcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutBrdcastPkts2.setStatus("current")
_H3cDot11APIfInMulcastPkts2_Type = Counter64
_H3cDot11APIfInMulcastPkts2_Object = MibTableColumn
h3cDot11APIfInMulcastPkts2 = _H3cDot11APIfInMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 21),
    _H3cDot11APIfInMulcastPkts2_Type()
)
h3cDot11APIfInMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInMulcastPkts2.setStatus("current")
_H3cDot11APIfOutMulcastPkts2_Type = Counter64
_H3cDot11APIfOutMulcastPkts2_Object = MibTableColumn
h3cDot11APIfOutMulcastPkts2 = _H3cDot11APIfOutMulcastPkts2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 22),
    _H3cDot11APIfOutMulcastPkts2_Type()
)
h3cDot11APIfOutMulcastPkts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutMulcastPkts2.setStatus("current")
_H3cDot11APIfInPayloadOctets2_Type = Counter64
_H3cDot11APIfInPayloadOctets2_Object = MibTableColumn
h3cDot11APIfInPayloadOctets2 = _H3cDot11APIfInPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 23),
    _H3cDot11APIfInPayloadOctets2_Type()
)
h3cDot11APIfInPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInPayloadOctets2.setStatus("current")
_H3cDot11APIfOutPayloadOctets2_Type = Counter64
_H3cDot11APIfOutPayloadOctets2_Object = MibTableColumn
h3cDot11APIfOutPayloadOctets2 = _H3cDot11APIfOutPayloadOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 24),
    _H3cDot11APIfOutPayloadOctets2_Type()
)
h3cDot11APIfOutPayloadOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutPayloadOctets2.setStatus("current")
_H3cDot11APIfInDataOctets2_Type = Counter64
_H3cDot11APIfInDataOctets2_Object = MibTableColumn
h3cDot11APIfInDataOctets2 = _H3cDot11APIfInDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 25),
    _H3cDot11APIfInDataOctets2_Type()
)
h3cDot11APIfInDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfInDataOctets2.setStatus("current")
_H3cDot11APIfOutDataOctets2_Type = Counter64
_H3cDot11APIfOutDataOctets2_Object = MibTableColumn
h3cDot11APIfOutDataOctets2 = _H3cDot11APIfOutDataOctets2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 23, 1, 26),
    _H3cDot11APIfOutDataOctets2_Type()
)
h3cDot11APIfOutDataOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APIfOutDataOctets2.setStatus("current")
_H3cDot11APUserSecAuthStatisTable_Object = MibTable
h3cDot11APUserSecAuthStatisTable = _H3cDot11APUserSecAuthStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24)
)
if mibBuilder.loadTexts:
    h3cDot11APUserSecAuthStatisTable.setStatus("current")
_H3cDot11APUserSecAuthStatisEntry_Object = MibTableRow
h3cDot11APUserSecAuthStatisEntry = _H3cDot11APUserSecAuthStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1)
)
h3cDot11APUserSecAuthStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APUserSecAuthStatisEntry.setStatus("current")
_H3cDot11APUserAuthCurNumber_Type = Integer32
_H3cDot11APUserAuthCurNumber_Object = MibTableColumn
h3cDot11APUserAuthCurNumber = _H3cDot11APUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 1),
    _H3cDot11APUserAuthCurNumber_Type()
)
h3cDot11APUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserAuthCurNumber.setStatus("current")
_H3cDot11APUserConnFailCnt_Type = Counter32
_H3cDot11APUserConnFailCnt_Object = MibTableColumn
h3cDot11APUserConnFailCnt = _H3cDot11APUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 2),
    _H3cDot11APUserConnFailCnt_Type()
)
h3cDot11APUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserConnFailCnt.setStatus("current")
_H3cDot11APUserAuthReqCnt_Type = Counter32
_H3cDot11APUserAuthReqCnt_Object = MibTableColumn
h3cDot11APUserAuthReqCnt = _H3cDot11APUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 3),
    _H3cDot11APUserAuthReqCnt_Type()
)
h3cDot11APUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserAuthReqCnt.setStatus("current")
_H3cDot11APUserAuthSuccCnt_Type = Counter32
_H3cDot11APUserAuthSuccCnt_Object = MibTableColumn
h3cDot11APUserAuthSuccCnt = _H3cDot11APUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 4),
    _H3cDot11APUserAuthSuccCnt_Type()
)
h3cDot11APUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserAuthSuccCnt.setStatus("current")
_H3cDot11APUserAuthFailCnt_Type = Counter32
_H3cDot11APUserAuthFailCnt_Object = MibTableColumn
h3cDot11APUserAuthFailCnt = _H3cDot11APUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 5),
    _H3cDot11APUserAuthFailCnt_Type()
)
h3cDot11APUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserAuthFailCnt.setStatus("current")
_H3cDot11AllUserOnlineTime_Type = TimeTicks
_H3cDot11AllUserOnlineTime_Object = MibTableColumn
h3cDot11AllUserOnlineTime = _H3cDot11AllUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 24, 1, 6),
    _H3cDot11AllUserOnlineTime_Type()
)
h3cDot11AllUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11AllUserOnlineTime.setStatus("current")
_H3cDot11APUserInfoStatisTable_Object = MibTable
h3cDot11APUserInfoStatisTable = _H3cDot11APUserInfoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25)
)
if mibBuilder.loadTexts:
    h3cDot11APUserInfoStatisTable.setStatus("current")
_H3cDot11APUserInfoStatisEntry_Object = MibTableRow
h3cDot11APUserInfoStatisEntry = _H3cDot11APUserInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1)
)
h3cDot11APUserInfoStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APUserMacAddr"),
)
if mibBuilder.loadTexts:
    h3cDot11APUserInfoStatisEntry.setStatus("current")
_H3cDot11APUserMacAddr_Type = MacAddress
_H3cDot11APUserMacAddr_Object = MibTableColumn
h3cDot11APUserMacAddr = _H3cDot11APUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1, 1),
    _H3cDot11APUserMacAddr_Type()
)
h3cDot11APUserMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APUserMacAddr.setStatus("current")
_H3cDot11APUserIpAddr_Type = IpAddress
_H3cDot11APUserIpAddr_Object = MibTableColumn
h3cDot11APUserIpAddr = _H3cDot11APUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1, 2),
    _H3cDot11APUserIpAddr_Type()
)
h3cDot11APUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserIpAddr.setStatus("current")
_H3cDot11APUserLoginName_Type = OctetString
_H3cDot11APUserLoginName_Object = MibTableColumn
h3cDot11APUserLoginName = _H3cDot11APUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1, 3),
    _H3cDot11APUserLoginName_Type()
)
h3cDot11APUserLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserLoginName.setStatus("current")
_H3cDot11APUserLoginTime_Type = OctetString
_H3cDot11APUserLoginTime_Object = MibTableColumn
h3cDot11APUserLoginTime = _H3cDot11APUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1, 4),
    _H3cDot11APUserLoginTime_Type()
)
h3cDot11APUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserLoginTime.setStatus("current")
_H3cDot11APUserOnlineTime_Type = TimeTicks
_H3cDot11APUserOnlineTime_Object = MibTableColumn
h3cDot11APUserOnlineTime = _H3cDot11APUserOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 25, 1, 5),
    _H3cDot11APUserOnlineTime_Type()
)
h3cDot11APUserOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APUserOnlineTime.setStatus("current")
_H3cDot11APReassocStatis2Table_Object = MibTable
h3cDot11APReassocStatis2Table = _H3cDot11APReassocStatis2Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 26)
)
if mibBuilder.loadTexts:
    h3cDot11APReassocStatis2Table.setStatus("current")
_H3cDot11APReassocStatis2Entry_Object = MibTableRow
h3cDot11APReassocStatis2Entry = _H3cDot11APReassocStatis2Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 26, 1)
)
h3cDot11APReassocStatis2Entry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APReassocStatis2Entry.setStatus("current")
_H3cDot11APReassocFailStatis2Cnt_Type = Counter32
_H3cDot11APReassocFailStatis2Cnt_Object = MibTableColumn
h3cDot11APReassocFailStatis2Cnt = _H3cDot11APReassocFailStatis2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 26, 1, 1),
    _H3cDot11APReassocFailStatis2Cnt_Type()
)
h3cDot11APReassocFailStatis2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APReassocFailStatis2Cnt.setStatus("current")
_H3cDot11TrafficTable_Object = MibTable
h3cDot11TrafficTable = _H3cDot11TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27)
)
if mibBuilder.loadTexts:
    h3cDot11TrafficTable.setStatus("current")
_H3cDot11TrafficEntry_Object = MibTableRow
h3cDot11TrafficEntry = _H3cDot11TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1)
)
h3cDot11TrafficEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11SSIDIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11TrafficEntry.setStatus("current")
_H3cDot11SSIDIndex_Type = OctetString
_H3cDot11SSIDIndex_Object = MibTableColumn
h3cDot11SSIDIndex = _H3cDot11SSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1, 1),
    _H3cDot11SSIDIndex_Type()
)
h3cDot11SSIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SSIDIndex.setStatus("current")
_H3cDot11UpPacketNumber_Type = Counter64
_H3cDot11UpPacketNumber_Object = MibTableColumn
h3cDot11UpPacketNumber = _H3cDot11UpPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1, 2),
    _H3cDot11UpPacketNumber_Type()
)
h3cDot11UpPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11UpPacketNumber.setStatus("current")
_H3cDot11UpByteNumber_Type = Counter64
_H3cDot11UpByteNumber_Object = MibTableColumn
h3cDot11UpByteNumber = _H3cDot11UpByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1, 3),
    _H3cDot11UpByteNumber_Type()
)
h3cDot11UpByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11UpByteNumber.setStatus("current")
_H3cDot11DownPacketNumber_Type = Counter64
_H3cDot11DownPacketNumber_Object = MibTableColumn
h3cDot11DownPacketNumber = _H3cDot11DownPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1, 4),
    _H3cDot11DownPacketNumber_Type()
)
h3cDot11DownPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DownPacketNumber.setStatus("current")
_H3cDot11DownByteNumber_Type = Counter64
_H3cDot11DownByteNumber_Object = MibTableColumn
h3cDot11DownByteNumber = _H3cDot11DownByteNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 27, 1, 5),
    _H3cDot11DownByteNumber_Type()
)
h3cDot11DownByteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11DownByteNumber.setStatus("current")
_H3cDot11APEchoStatisTable_Object = MibTable
h3cDot11APEchoStatisTable = _H3cDot11APEchoStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 28)
)
if mibBuilder.loadTexts:
    h3cDot11APEchoStatisTable.setStatus("current")
_H3cDot11APEchoInfoStatisEntry_Object = MibTableRow
h3cDot11APEchoInfoStatisEntry = _H3cDot11APEchoInfoStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 28, 1)
)
h3cDot11APEchoInfoStatisEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurAPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APEchoInfoStatisEntry.setStatus("current")
_H3cDot11APEchoAvgDelay_Type = Integer32
_H3cDot11APEchoAvgDelay_Object = MibTableColumn
h3cDot11APEchoAvgDelay = _H3cDot11APEchoAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 28, 1, 1),
    _H3cDot11APEchoAvgDelay_Type()
)
h3cDot11APEchoAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APEchoAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APEchoAvgDelay.setUnits("millisecond")
_H3cDot11APEchoRequestCnt_Type = Counter64
_H3cDot11APEchoRequestCnt_Object = MibTableColumn
h3cDot11APEchoRequestCnt = _H3cDot11APEchoRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 28, 1, 2),
    _H3cDot11APEchoRequestCnt_Type()
)
h3cDot11APEchoRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APEchoRequestCnt.setStatus("current")
_H3cDot11APEchoRespLossCnt_Type = Counter64
_H3cDot11APEchoRespLossCnt_Object = MibTableColumn
h3cDot11APEchoRespLossCnt = _H3cDot11APEchoRespLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 2, 28, 1, 3),
    _H3cDot11APEchoRespLossCnt_Type()
)
h3cDot11APEchoRespLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APEchoRespLossCnt.setStatus("current")
_H3cDot11APMtNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11APMtNotifyGroup = _H3cDot11APMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3)
)
_H3cDot11APMtTraps_ObjectIdentity = ObjectIdentity
h3cDot11APMtTraps = _H3cDot11APMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0)
)
_H3cDot11APMtTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cDot11APMtTrapVarObjects = _H3cDot11APMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1)
)
_H3cDot11APMtTrapCfgErrReason_Type = H3cDot11NotifyReasonType
_H3cDot11APMtTrapCfgErrReason_Object = MibScalar
h3cDot11APMtTrapCfgErrReason = _H3cDot11APMtTrapCfgErrReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 1),
    _H3cDot11APMtTrapCfgErrReason_Type()
)
h3cDot11APMtTrapCfgErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtTrapCfgErrReason.setStatus("current")


class _H3cDot11APMtTrapRadioFailReason_Type(Integer32):
    """Custom type h3cDot11APMtTrapRadioFailReason based on Integer32"""
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
          ("hwerror", 2),
          ("radar", 4),
          ("swerror", 3),
          ("unknown", 8))
    )


_H3cDot11APMtTrapRadioFailReason_Type.__name__ = "Integer32"
_H3cDot11APMtTrapRadioFailReason_Object = MibScalar
h3cDot11APMtTrapRadioFailReason = _H3cDot11APMtTrapRadioFailReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 2),
    _H3cDot11APMtTrapRadioFailReason_Type()
)
h3cDot11APMtTrapRadioFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtTrapRadioFailReason.setStatus("current")
_H3cDot11APMtTrapOldChannel_Type = H3cDot11ChannelScopeType
_H3cDot11APMtTrapOldChannel_Object = MibScalar
h3cDot11APMtTrapOldChannel = _H3cDot11APMtTrapOldChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 3),
    _H3cDot11APMtTrapOldChannel_Type()
)
h3cDot11APMtTrapOldChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtTrapOldChannel.setStatus("current")
_H3cDot11APMtTrapNewChannel_Type = H3cDot11ChannelScopeType
_H3cDot11APMtTrapNewChannel_Object = MibScalar
h3cDot11APMtTrapNewChannel = _H3cDot11APMtTrapNewChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 4),
    _H3cDot11APMtTrapNewChannel_Type()
)
h3cDot11APMtTrapNewChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtTrapNewChannel.setStatus("current")
_H3cDot11APChannelChgMode_Type = H3cDot11RFModeType
_H3cDot11APChannelChgMode_Object = MibScalar
h3cDot11APChannelChgMode = _H3cDot11APChannelChgMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 5),
    _H3cDot11APChannelChgMode_Type()
)
h3cDot11APChannelChgMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APChannelChgMode.setStatus("current")


class _H3cDot11APChgWorkMode_Type(Integer32):
    """Custom type h3cDot11APChgWorkMode based on Integer32"""
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


_H3cDot11APChgWorkMode_Type.__name__ = "Integer32"
_H3cDot11APChgWorkMode_Object = MibScalar
h3cDot11APChgWorkMode = _H3cDot11APChgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 6),
    _H3cDot11APChgWorkMode_Type()
)
h3cDot11APChgWorkMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APChgWorkMode.setStatus("current")
_H3cDot11APIntfDevMACAddress_Type = MacAddress
_H3cDot11APIntfDevMACAddress_Object = MibScalar
h3cDot11APIntfDevMACAddress = _H3cDot11APIntfDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 7),
    _H3cDot11APIntfDevMACAddress_Type()
)
h3cDot11APIntfDevMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APIntfDevMACAddress.setStatus("current")
_H3cDot11APMtTrapOldIPAddr_Type = IpAddress
_H3cDot11APMtTrapOldIPAddr_Object = MibScalar
h3cDot11APMtTrapOldIPAddr = _H3cDot11APMtTrapOldIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 8),
    _H3cDot11APMtTrapOldIPAddr_Type()
)
h3cDot11APMtTrapOldIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtTrapOldIPAddr.setStatus("current")
_H3cDot11CurrInterfDetectedNum_Type = Integer32
_H3cDot11CurrInterfDetectedNum_Object = MibScalar
h3cDot11CurrInterfDetectedNum = _H3cDot11CurrInterfDetectedNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 9),
    _H3cDot11CurrInterfDetectedNum_Type()
)
h3cDot11CurrInterfDetectedNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11CurrInterfDetectedNum.setStatus("current")


class _H3cDot11StaFullReason_Type(Integer32):
    """Custom type h3cDot11StaFullReason based on Integer32"""
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


_H3cDot11StaFullReason_Type.__name__ = "Integer32"
_H3cDot11StaFullReason_Object = MibScalar
h3cDot11StaFullReason = _H3cDot11StaFullReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 10),
    _H3cDot11StaFullReason_Type()
)
h3cDot11StaFullReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StaFullReason.setStatus("current")
_H3cDot11StaLimitNumber_Type = Integer32
_H3cDot11StaLimitNumber_Object = MibScalar
h3cDot11StaLimitNumber = _H3cDot11StaLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 11),
    _H3cDot11StaLimitNumber_Type()
)
h3cDot11StaLimitNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11StaLimitNumber.setStatus("current")


class _H3cDot11APRadioDownReason_Type(Integer32):
    """Custom type h3cDot11APRadioDownReason based on Integer32"""
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


_H3cDot11APRadioDownReason_Type.__name__ = "Integer32"
_H3cDot11APRadioDownReason_Object = MibScalar
h3cDot11APRadioDownReason = _H3cDot11APRadioDownReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 12),
    _H3cDot11APRadioDownReason_Type()
)
h3cDot11APRadioDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APRadioDownReason.setStatus("current")
_H3cDot11InterfMacList_Type = OctetString
_H3cDot11InterfMacList_Object = MibScalar
h3cDot11InterfMacList = _H3cDot11InterfMacList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 13),
    _H3cDot11InterfMacList_Type()
)
h3cDot11InterfMacList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11InterfMacList.setStatus("current")
_H3cDot11APTrapUserCnt_Type = Integer32
_H3cDot11APTrapUserCnt_Object = MibScalar
h3cDot11APTrapUserCnt = _H3cDot11APTrapUserCnt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 14),
    _H3cDot11APTrapUserCnt_Type()
)
h3cDot11APTrapUserCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapUserCnt.setStatus("current")
_H3cDot11APTrapUserThreshold_Type = Integer32
_H3cDot11APTrapUserThreshold_Object = MibScalar
h3cDot11APTrapUserThreshold = _H3cDot11APTrapUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 15),
    _H3cDot11APTrapUserThreshold_Type()
)
h3cDot11APTrapUserThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APTrapUserThreshold.setStatus("current")
_H3cDot11APMtChanlChgCount_Type = Integer32
_H3cDot11APMtChanlChgCount_Object = MibScalar
h3cDot11APMtChanlChgCount = _H3cDot11APMtChanlChgCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 16),
    _H3cDot11APMtChanlChgCount_Type()
)
h3cDot11APMtChanlChgCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtChanlChgCount.setStatus("current")
_H3cDot11APMtFormerApVersion_Type = OctetString
_H3cDot11APMtFormerApVersion_Object = MibScalar
h3cDot11APMtFormerApVersion = _H3cDot11APMtFormerApVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 17),
    _H3cDot11APMtFormerApVersion_Type()
)
h3cDot11APMtFormerApVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtFormerApVersion.setStatus("current")
_H3cDot11APMtAPID_Type = H3cDot11ObjectIDType
_H3cDot11APMtAPID_Object = MibScalar
h3cDot11APMtAPID = _H3cDot11APMtAPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 18),
    _H3cDot11APMtAPID_Type()
)
h3cDot11APMtAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtAPID.setStatus("current")
_H3cDot11APMtRadioID_Type = H3cDot11RadioScopeType
_H3cDot11APMtRadioID_Object = MibScalar
h3cDot11APMtRadioID = _H3cDot11APMtRadioID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 19),
    _H3cDot11APMtRadioID_Type()
)
h3cDot11APMtRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtRadioID.setStatus("current")
_H3cDot11APMtChannel_Type = H3cDot11ChannelScopeType
_H3cDot11APMtChannel_Object = MibScalar
h3cDot11APMtChannel = _H3cDot11APMtChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 20),
    _H3cDot11APMtChannel_Type()
)
h3cDot11APMtChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtChannel.setStatus("current")
_H3cDot11APMtInterfMacAdd_Type = MacAddress
_H3cDot11APMtInterfMacAdd_Object = MibScalar
h3cDot11APMtInterfMacAdd = _H3cDot11APMtInterfMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 21),
    _H3cDot11APMtInterfMacAdd_Type()
)
h3cDot11APMtInterfMacAdd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtInterfMacAdd.setStatus("current")
_H3cDot11APMtAdjChannel_Type = H3cDot11ChannelScopeType
_H3cDot11APMtAdjChannel_Object = MibScalar
h3cDot11APMtAdjChannel = _H3cDot11APMtAdjChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 22),
    _H3cDot11APMtAdjChannel_Type()
)
h3cDot11APMtAdjChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtAdjChannel.setStatus("current")
_H3cDot11APMtFirstTrapTime_Type = TimeTicks
_H3cDot11APMtFirstTrapTime_Object = MibScalar
h3cDot11APMtFirstTrapTime = _H3cDot11APMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 1, 23),
    _H3cDot11APMtFirstTrapTime_Type()
)
h3cDot11APMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11APMtFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDot11APMtWorkModeChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 1)
)
h3cDot11APMtWorkModeChgTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APChgWorkMode"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtWorkModeChgTrap.setStatus(
        "current"
    )

h3cDot11APMtCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 2)
)
h3cDot11APMtCfgErrorTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtTrapCfgErrReason"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtCfgErrorTrap.setStatus(
        "current"
    )

h3cDot11APMtRadioFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 3)
)
h3cDot11APMtRadioFailTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtTrapRadioFailReason"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtRadioFailTrap.setStatus(
        "current"
    )

h3cDot11APMtRadioFailRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 4)
)
h3cDot11APMtRadioFailRecoverTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtRadioFailRecoverTrap.setStatus(
        "current"
    )

h3cDot11APMtRdoChanlChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 5)
)
h3cDot11APMtRdoChanlChgTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APChannelChgMode"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtTrapOldChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtTrapNewChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChanlChgCount"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtRdoChanlChgTrap.setStatus(
        "current"
    )

h3cDot11APMtTimeSynFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 6)
)
h3cDot11APMtTimeSynFail.setObjects(
    ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID")
)
if mibBuilder.loadTexts:
    h3cDot11APMtTimeSynFail.setStatus(
        "current"
    )

h3cDot11APMtChlIntfDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 7)
)
h3cDot11APMtChlIntfDetected.setObjects(
    ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel")
)
if mibBuilder.loadTexts:
    h3cDot11APMtChlIntfDetected.setStatus(
        "current"
    )

h3cDot11APMtIntfAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 8)
)
h3cDot11APMtIntfAPDetected.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtIntfAPDetected.setStatus(
        "current"
    )

h3cDot11APMtIntfStaDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 9)
)
h3cDot11APMtIntfStaDetected.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIntfDevMACAddress"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtIntfStaDetected.setStatus(
        "current"
    )

h3cDot11APMtIPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 10)
)
h3cDot11APMtIPChange.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APIPAddress"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtTrapOldIPAddr"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtIPChange.setStatus(
        "current"
    )

h3cDot11APFlashWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 11)
)
h3cDot11APFlashWriteFailure.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFormerApVersion"))
)
if mibBuilder.loadTexts:
    h3cDot11APFlashWriteFailure.setStatus(
        "current"
    )

h3cDot11APSysReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 12)
)
h3cDot11APSysReboot.setObjects(
    ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID")
)
if mibBuilder.loadTexts:
    h3cDot11APSysReboot.setStatus(
        "current"
    )

h3cDot11APMtAvailChlTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 13)
)
h3cDot11APMtAvailChlTooLow.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtAvailChlTooLow.setStatus(
        "current"
    )

h3cDot11APImgDwldSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 14)
)
h3cDot11APImgDwldSuccess.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurrAPName"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurrAPIPAddress"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurrAPSoftwareVersion"))
)
if mibBuilder.loadTexts:
    h3cDot11APImgDwldSuccess.setStatus(
        "current"
    )

h3cDot11APInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 15)
)
h3cDot11APInterfDetectedTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurrInterfDetectedNum"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11InterfMacList"))
)
if mibBuilder.loadTexts:
    h3cDot11APInterfDetectedTrap.setStatus(
        "current"
    )

h3cDot11APInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 16)
)
h3cDot11APInterfClearTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APInterfClearTrap.setStatus(
        "current"
    )

h3cDot11StaInterfDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 17)
)
h3cDot11StaInterfDetectedTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11CurrInterfDetectedNum"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11InterfMacList"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11StaInterfDetectedTrap.setStatus(
        "current"
    )

h3cDot11StaInterfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 18)
)
h3cDot11StaInterfClearTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11StaInterfClearTrap.setStatus(
        "current"
    )

h3cDot11OtherDevIntDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 19)
)
h3cDot11OtherDevIntDetectedTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11OtherDevIntDetectedTrap.setStatus(
        "current"
    )

h3cDot11OtherDevIntClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 20)
)
h3cDot11OtherDevIntClearTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11Channel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11OtherDevIntClearTrap.setStatus(
        "current"
    )

h3cDot11APModuleTroubleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 21)
)
h3cDot11APModuleTroubleTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"))
)
if mibBuilder.loadTexts:
    h3cDot11APModuleTroubleTrap.setStatus(
        "current"
    )

h3cDot11APModuleTroubleClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 22)
)
h3cDot11APModuleTroubleClearTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"))
)
if mibBuilder.loadTexts:
    h3cDot11APModuleTroubleClearTrap.setStatus(
        "current"
    )

h3cDot11APRadioDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 23)
)
h3cDot11APRadioDownTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APRadioDownReason"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APRadioDownTrap.setStatus(
        "current"
    )

h3cDot11APRadioDownRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 24)
)
h3cDot11APRadioDownRecovTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APRadioDownRecovTrap.setStatus(
        "current"
    )

h3cDot11APStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 25)
)
h3cDot11APStaFullTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11StaLimitNumber"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11StaFullReason"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APStaFullTrap.setStatus(
        "current"
    )

h3cDot11APStaFullRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 26)
)
h3cDot11APStaFullRecoverTrap.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11StaLimitNumber"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11StaFullReason"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APStaFullRecoverTrap.setStatus(
        "current"
    )

h3cDot11DFSFreeCntBelowThrRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 27)
)
h3cDot11DFSFreeCntBelowThrRecov.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11RadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"))
)
if mibBuilder.loadTexts:
    h3cDot11DFSFreeCntBelowThrRecov.setStatus(
        "current"
    )

h3cDot11APCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 28)
)
h3cDot11APCpuUsageHigh.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APCPURTUsage"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APCpuUsageHigh.setStatus(
        "current"
    )

h3cDot11APCpuUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 29)
)
h3cDot11APCpuUsageHighRecover.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APCPURTUsage"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APCpuUsageHighRecover.setStatus(
        "current"
    )

h3cDot11APMemUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 30)
)
h3cDot11APMemUsageHigh.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMemRTUsage"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APMemUsageHigh.setStatus(
        "current"
    )

h3cDot11APMemUsageHighRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 31)
)
h3cDot11APMemUsageHighRecover.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMemRTUsage"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APMemUsageHighRecover.setStatus(
        "current"
    )

h3cDot11APTrapUserCntExceedThre = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 32)
)
h3cDot11APTrapUserCntExceedThre.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APTrapUserCnt"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APTrapUserThreshold"))
)
if mibBuilder.loadTexts:
    h3cDot11APTrapUserCntExceedThre.setStatus(
        "current"
    )

h3cDot11APMtDetectedIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 33)
)
h3cDot11APMtDetectedIntfAP.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtDetectedIntfAP.setStatus(
        "current"
    )

h3cDot11APMtDetectedIntfSTA = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 34)
)
h3cDot11APMtDetectedIntfSTA.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtDetectedIntfSTA.setStatus(
        "current"
    )

h3cDot11APMtDetectedIntfOtherDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 35)
)
h3cDot11APMtDetectedIntfOtherDev.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChannel"))
)
if mibBuilder.loadTexts:
    h3cDot11APMtDetectedIntfOtherDev.setStatus(
        "current"
    )

h3cDot11DetcAdjChlIntfAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 36)
)
h3cDot11DetcAdjChlIntfAP.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAdjChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11DetcAdjChlIntfAP.setStatus(
        "current"
    )

h3cDot11DetcAdjChlIntfAPClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 2, 3, 0, 37)
)
h3cDot11DetcAdjChlIntfAPClear.setObjects(
      *(("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAPID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtRadioID"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtAdjChannel"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtInterfMacAdd"),
        ("A3COM-HUAWEI-DOT11-APMT-MIB", "h3cDot11APMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cDot11DetcAdjChlIntfAPClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-APMT-MIB",
    **{"h3cDot11APMT": h3cDot11APMT,
       "h3cDot11APObjectGroup": h3cDot11APObjectGroup,
       "h3cDot11APObjectStatusTable": h3cDot11APObjectStatusTable,
       "h3cDot11APObjectStatusEntry": h3cDot11APObjectStatusEntry,
       "h3cDot11APID": h3cDot11APID,
       "h3cDot11APIPAddress": h3cDot11APIPAddress,
       "h3cDot11APMacAddress": h3cDot11APMacAddress,
       "h3cDot11APOperationStatus": h3cDot11APOperationStatus,
       "h3cDot11APTemplateNameOfAP": h3cDot11APTemplateNameOfAP,
       "h3cDot11APReset": h3cDot11APReset,
       "h3cDot11APCpuUsage": h3cDot11APCpuUsage,
       "h3cDot11APConnectionType": h3cDot11APConnectionType,
       "h3cDot11APLastImgDownloadTime": h3cDot11APLastImgDownloadTime,
       "h3cDot11APIPv6Address": h3cDot11APIPv6Address,
       "h3cDot11APLastRegisterTime": h3cDot11APLastRegisterTime,
       "h3cDot11APObjectTable": h3cDot11APObjectTable,
       "h3cDot11APObjectEntry": h3cDot11APObjectEntry,
       "h3cDot11APObjID": h3cDot11APObjID,
       "h3cDot11CurrAPIPAddress": h3cDot11CurrAPIPAddress,
       "h3cDot11CurrAPMacAddress": h3cDot11CurrAPMacAddress,
       "h3cDot11CurrACPortIndex": h3cDot11CurrACPortIndex,
       "h3cDot11CurrAPMACMode": h3cDot11CurrAPMACMode,
       "h3cDot11CurrAPTemplateName": h3cDot11CurrAPTemplateName,
       "h3cDot11CurrAPStationAssocCount": h3cDot11CurrAPStationAssocCount,
       "h3cDot11CurrAPName": h3cDot11CurrAPName,
       "h3cDot11CurrAPModelName": h3cDot11CurrAPModelName,
       "h3cDot11CurrAPImageName": h3cDot11CurrAPImageName,
       "h3cDot11CurrAPSoftwareVersion": h3cDot11CurrAPSoftwareVersion,
       "h3cDot11CurrAPIPNetMask": h3cDot11CurrAPIPNetMask,
       "h3cDot11CurrRadioModeSupport": h3cDot11CurrRadioModeSupport,
       "h3cDot11CurrIfNumber": h3cDot11CurrIfNumber,
       "h3cDot11CurrAPElementID": h3cDot11CurrAPElementID,
       "h3cDot11CurrAPMode": h3cDot11CurrAPMode,
       "h3cDot11CurrAPIPv6Address": h3cDot11CurrAPIPv6Address,
       "h3cDot11CurrAPSSIDNumber": h3cDot11CurrAPSSIDNumber,
       "h3cDot11CurrAPManufacturer": h3cDot11CurrAPManufacturer,
       "h3cDot11CurrAPMemorySize": h3cDot11CurrAPMemorySize,
       "h3cDot11CurrAPMemSizeInBytes": h3cDot11CurrAPMemSizeInBytes,
       "h3cDot11CurrAPFlashSize": h3cDot11CurrAPFlashSize,
       "h3cDot11CurrAPFlashSizeInBytes": h3cDot11CurrAPFlashSizeInBytes,
       "h3cDot11CurrAPReleasedVersion": h3cDot11CurrAPReleasedVersion,
       "h3cDot11CurrRadioModeSupport2": h3cDot11CurrRadioModeSupport2,
       "h3cDot11APRadioTable": h3cDot11APRadioTable,
       "h3cDot11APRadioEntry": h3cDot11APRadioEntry,
       "h3cDot11CurAPID": h3cDot11CurAPID,
       "h3cDot11RadioID": h3cDot11RadioID,
       "h3cDot11AdminStatus": h3cDot11AdminStatus,
       "h3cDot11OperStatus": h3cDot11OperStatus,
       "h3cDot11Channel": h3cDot11Channel,
       "h3cDot11TxPowerLevel": h3cDot11TxPowerLevel,
       "h3cDot11APRadioIfIndex": h3cDot11APRadioIfIndex,
       "h3cDot11AntennaGain": h3cDot11AntennaGain,
       "h3cDot11MaxBandwidth": h3cDot11MaxBandwidth,
       "h3cDot11ResourceUseRatio": h3cDot11ResourceUseRatio,
       "h3cDot11RadioModeSupport": h3cDot11RadioModeSupport,
       "h3cDot11TxPowerLevel2": h3cDot11TxPowerLevel2,
       "h3cDot11PowerMgmtStatus": h3cDot11PowerMgmtStatus,
       "h3cDot11ChannelSwitchTimes": h3cDot11ChannelSwitchTimes,
       "h3cDot11AntennaType": h3cDot11AntennaType,
       "h3cDot11DiversitySelectionRx": h3cDot11DiversitySelectionRx,
       "h3cDot11MaxTxPwrLvl": h3cDot11MaxTxPwrLvl,
       "h3cDot11PwrAttRange": h3cDot11PwrAttRange,
       "h3cDot11AvgRxSignalStrength": h3cDot11AvgRxSignalStrength,
       "h3cDot11HighestRxSignalStrength": h3cDot11HighestRxSignalStrength,
       "h3cDot11LowestRxSignalStrength": h3cDot11LowestRxSignalStrength,
       "h3cDot11RadioIfUpdownTimes": h3cDot11RadioIfUpdownTimes,
       "h3cDot11RadioIfLastChange": h3cDot11RadioIfLastChange,
       "h3cDot11RadioModeSupport2": h3cDot11RadioModeSupport2,
       "h3cDot11APBSSTable": h3cDot11APBSSTable,
       "h3cDot11APBSSEntry": h3cDot11APBSSEntry,
       "h3cDot11WlanID": h3cDot11WlanID,
       "h3cDot11BSSID": h3cDot11BSSID,
       "h3cDot11CurrSvcPolicyID": h3cDot11CurrSvcPolicyID,
       "h3cDot11SSID": h3cDot11SSID,
       "h3cDot11CurrSSIDResourceUseRatio": h3cDot11CurrSSIDResourceUseRatio,
       "h3cDot11APEssVlanId": h3cDot11APEssVlanId,
       "h3cDot11APModelTable": h3cDot11APModelTable,
       "h3cDot11APModelEntry": h3cDot11APModelEntry,
       "h3cDot11APModelAlias": h3cDot11APModelAlias,
       "h3cDot11APModelName": h3cDot11APModelName,
       "h3cDot11RadioNumSupport": h3cDot11RadioNumSupport,
       "h3cDot11StationNumSupport": h3cDot11StationNumSupport,
       "h3cDot11MACModeSupport": h3cDot11MACModeSupport,
       "h3cDot11APManufacturer": h3cDot11APManufacturer,
       "h3cDot11APCPUType": h3cDot11APCPUType,
       "h3cDot11APCPUClockSpeed": h3cDot11APCPUClockSpeed,
       "h3cDot11APMemoryType": h3cDot11APMemoryType,
       "h3cDot11APFlashType": h3cDot11APFlashType,
       "h3cDot11APFlashSize": h3cDot11APFlashSize,
       "h3cDot11APMemSize": h3cDot11APMemSize,
       "h3cDot11APFlashSizeInBytes": h3cDot11APFlashSizeInBytes,
       "h3cDot11APMemorySize": h3cDot11APMemorySize,
       "h3cDot11APIfTable": h3cDot11APIfTable,
       "h3cDot11APIfEntry": h3cDot11APIfEntry,
       "h3cDot11APIfIndex": h3cDot11APIfIndex,
       "h3cDot11APIfDescr": h3cDot11APIfDescr,
       "h3cDot11APIfType": h3cDot11APIfType,
       "h3cDot11APIfMtu": h3cDot11APIfMtu,
       "h3cDot11APIfPHYAddress": h3cDot11APIfPHYAddress,
       "h3cDot11APIfSpeed": h3cDot11APIfSpeed,
       "h3cDot11APIfInDataRate": h3cDot11APIfInDataRate,
       "h3cDot11APIfOutDataRate": h3cDot11APIfOutDataRate,
       "h3cDot11APIfSpeedKbps": h3cDot11APIfSpeedKbps,
       "h3cDot11APSSIDObjectTable": h3cDot11APSSIDObjectTable,
       "h3cDot11APSSIDObjectEntry": h3cDot11APSSIDObjectEntry,
       "h3cDot11APConfigSPID": h3cDot11APConfigSPID,
       "h3cDot11APConfigSSIDName": h3cDot11APConfigSSIDName,
       "h3cDot11APConfigBSSIDNum": h3cDot11APConfigBSSIDNum,
       "h3cDot11APConfigPortalStaNum": h3cDot11APConfigPortalStaNum,
       "h3cDot11APSysInfoTable": h3cDot11APSysInfoTable,
       "h3cDot11APSysInfoEntry": h3cDot11APSysInfoEntry,
       "h3cDot11APSysUpTime": h3cDot11APSysUpTime,
       "h3cDot11APCPURTUsage": h3cDot11APCPURTUsage,
       "h3cDot11APCPUAvgUsage": h3cDot11APCPUAvgUsage,
       "h3cDot11APMemRTUsage": h3cDot11APMemRTUsage,
       "h3cDot11APMemAvgUsage": h3cDot11APMemAvgUsage,
       "h3cDot11APIPAddressGateway": h3cDot11APIPAddressGateway,
       "h3cDot11APACAssociateStatus": h3cDot11APACAssociateStatus,
       "h3cDot11APManuBuildInfo": h3cDot11APManuBuildInfo,
       "h3cDot11APFlashFreeSize": h3cDot11APFlashFreeSize,
       "h3cDot11APTemperature": h3cDot11APTemperature,
       "h3cDot11APIdleListTable": h3cDot11APIdleListTable,
       "h3cDot11APIdleListEntry": h3cDot11APIdleListEntry,
       "h3cDot11APIdleTemplateName": h3cDot11APIdleTemplateName,
       "h3cDot11APIdleSerialID": h3cDot11APIdleSerialID,
       "h3cDot11APSysInfoByAPIDTable": h3cDot11APSysInfoByAPIDTable,
       "h3cDot11APSysInfoByAPIDEntry": h3cDot11APSysInfoByAPIDEntry,
       "h3cDot11APSysUpTime2": h3cDot11APSysUpTime2,
       "h3cDot11APCPURTUsage2": h3cDot11APCPURTUsage2,
       "h3cDot11APCPUAvgUsage2": h3cDot11APCPUAvgUsage2,
       "h3cDot11APMemRTUsage2": h3cDot11APMemRTUsage2,
       "h3cDot11APMemAvgUsage2": h3cDot11APMemAvgUsage2,
       "h3cDot11APIPAddressGateway2": h3cDot11APIPAddressGateway2,
       "h3cDot11APACAssociateStatus2": h3cDot11APACAssociateStatus2,
       "h3cDot11APManuBuildInfo2": h3cDot11APManuBuildInfo2,
       "h3cDot11APFlashFreeSize2": h3cDot11APFlashFreeSize2,
       "h3cDot11APTemperature2": h3cDot11APTemperature2,
       "h3cDot11APMacAddress2": h3cDot11APMacAddress2,
       "h3cDot11APStatisGroup": h3cDot11APStatisGroup,
       "h3cDot11APRxStatisTable": h3cDot11APRxStatisTable,
       "h3cDot11APRxStatisEntry": h3cDot11APRxStatisEntry,
       "h3cDot11RxFrameDupCnt": h3cDot11RxFrameDupCnt,
       "h3cDot11RxFrameCnt": h3cDot11RxFrameCnt,
       "h3cDot11RxUcastFrameCnt": h3cDot11RxUcastFrameCnt,
       "h3cDot11RxBcastFrameCnt": h3cDot11RxBcastFrameCnt,
       "h3cDot11RxMcastFrameCnt": h3cDot11RxMcastFrameCnt,
       "h3cDot11RxDiscardFrameCnt": h3cDot11RxDiscardFrameCnt,
       "h3cDot11RxFragCnt": h3cDot11RxFragCnt,
       "h3cDot11RxFcsErrCnt": h3cDot11RxFcsErrCnt,
       "h3cDot11RxFrameBytes": h3cDot11RxFrameBytes,
       "h3cDot11RxUcastFrameBytes": h3cDot11RxUcastFrameBytes,
       "h3cDot11RxBcastFrameBytes": h3cDot11RxBcastFrameBytes,
       "h3cDot11RxMcastFrameBytes": h3cDot11RxMcastFrameBytes,
       "h3cDot11RxDiscardFrameBytes": h3cDot11RxDiscardFrameBytes,
       "h3cDot11RxMgmtFrameCnt": h3cDot11RxMgmtFrameCnt,
       "h3cDot11RxCtrlFrameCnt": h3cDot11RxCtrlFrameCnt,
       "h3cDot11RxDataFrameCnt": h3cDot11RxDataFrameCnt,
       "h3cDot11RxDecryptErrorCnt": h3cDot11RxDecryptErrorCnt,
       "h3cDot11RxAuthenFrameCnt": h3cDot11RxAuthenFrameCnt,
       "h3cDot11RxAssociateFrameCnt": h3cDot11RxAssociateFrameCnt,
       "h3cDot11RxFrameErrorRatio": h3cDot11RxFrameErrorRatio,
       "h3cDot11RxPhyErrorCnt": h3cDot11RxPhyErrorCnt,
       "h3cDot11RxMICErrorCnt": h3cDot11RxMICErrorCnt,
       "h3cDot11RxDataFrameBytes": h3cDot11RxDataFrameBytes,
       "h3cDot11RadioRxAverSnr": h3cDot11RadioRxAverSnr,
       "h3cDot11RxPayloadBytes": h3cDot11RxPayloadBytes,
       "h3cDot11RxTrafficSpeed": h3cDot11RxTrafficSpeed,
       "h3cDot11RxUcastDataFrameCnt": h3cDot11RxUcastDataFrameCnt,
       "h3cDot11RxNUcastDataFrameCnt": h3cDot11RxNUcastDataFrameCnt,
       "h3cDot11RxTotalDiscardFrameCnt": h3cDot11RxTotalDiscardFrameCnt,
       "h3cDot11RxTotalIPCheckErrPacketCnt": h3cDot11RxTotalIPCheckErrPacketCnt,
       "h3cDot11APTxStatisTable": h3cDot11APTxStatisTable,
       "h3cDot11APTxStatisEntry": h3cDot11APTxStatisEntry,
       "h3cDot11TxFragCnt": h3cDot11TxFragCnt,
       "h3cDot11FailedCnt": h3cDot11FailedCnt,
       "h3cDot11RetryCnt": h3cDot11RetryCnt,
       "h3cDot11MultiRetryCnt": h3cDot11MultiRetryCnt,
       "h3cDot11RtsSuccessCnt": h3cDot11RtsSuccessCnt,
       "h3cDot11RtsFailCnt": h3cDot11RtsFailCnt,
       "h3cDot11AckFailCnt": h3cDot11AckFailCnt,
       "h3cDot11TxFrameCnt": h3cDot11TxFrameCnt,
       "h3cDot11TxUcastFrameCnt": h3cDot11TxUcastFrameCnt,
       "h3cDot11TxBcastFrameCnt": h3cDot11TxBcastFrameCnt,
       "h3cDot11TxMcastFrameCnt": h3cDot11TxMcastFrameCnt,
       "h3cDot11TxDiscardFrameCnt": h3cDot11TxDiscardFrameCnt,
       "h3cDot11TxFrameBytes": h3cDot11TxFrameBytes,
       "h3cDot11TxUcastFrameBytes": h3cDot11TxUcastFrameBytes,
       "h3cDot11TxBcastFrameBytes": h3cDot11TxBcastFrameBytes,
       "h3cDot11TxMcastFrameBytes": h3cDot11TxMcastFrameBytes,
       "h3cDot11TxDiscardFrameBytes": h3cDot11TxDiscardFrameBytes,
       "h3cDot11TxAuthenFrameCnt": h3cDot11TxAuthenFrameCnt,
       "h3cDot11TxAssociateFrameCnt": h3cDot11TxAssociateFrameCnt,
       "h3cDot11TxFrameRetryRatio": h3cDot11TxFrameRetryRatio,
       "h3cDot11TxDataFrameCnt": h3cDot11TxDataFrameCnt,
       "h3cDot11TxDataFrameBytes": h3cDot11TxDataFrameBytes,
       "h3cDot11TxMSDUCnt": h3cDot11TxMSDUCnt,
       "h3cDot11TxDiscardMSDUCnt": h3cDot11TxDiscardMSDUCnt,
       "h3cDot11RetryMSDUCnt": h3cDot11RetryMSDUCnt,
       "h3cDot11TxPayloadBytes": h3cDot11TxPayloadBytes,
       "h3cDot11TxTrafficSpeed": h3cDot11TxTrafficSpeed,
       "h3cDot11TxErrFrameRatio": h3cDot11TxErrFrameRatio,
       "h3cDot11TxFrameRate": h3cDot11TxFrameRate,
       "h3cDot11TxMgtFrameCnt": h3cDot11TxMgtFrameCnt,
       "h3cDot11TxCtrlFrameCnt": h3cDot11TxCtrlFrameCnt,
       "h3cDot11TxMACErrCnt": h3cDot11TxMACErrCnt,
       "h3cDot11TxErrFrameCnt": h3cDot11TxErrFrameCnt,
       "h3cDot11TxUcastDataFrameCnt": h3cDot11TxUcastDataFrameCnt,
       "h3cDot11TxNUcastDataFrameCnt": h3cDot11TxNUcastDataFrameCnt,
       "h3cDot11APAssocStatisTable": h3cDot11APAssocStatisTable,
       "h3cDot11APAssocStatisEntry": h3cDot11APAssocStatisEntry,
       "h3cDot11ApStationAssocSum": h3cDot11ApStationAssocSum,
       "h3cDot11ApStationAssocFailSum": h3cDot11ApStationAssocFailSum,
       "h3cDot11ApStationReassocSum": h3cDot11ApStationReassocSum,
       "h3cDot11ApStationAssocRejectSum": h3cDot11ApStationAssocRejectSum,
       "h3cDot11ApStationExDeAuthenSum": h3cDot11ApStationExDeAuthenSum,
       "h3cDot11ApStationCurAssocSum": h3cDot11ApStationCurAssocSum,
       "h3cDot11ApStaCurAuthSuccSum": h3cDot11ApStaCurAuthSuccSum,
       "h3cDot11AllStationUpSumTime": h3cDot11AllStationUpSumTime,
       "h3cDot11ApStationAssocReqSum": h3cDot11ApStationAssocReqSum,
       "h3cDot11AllStationUpSumTimeTicks": h3cDot11AllStationUpSumTimeTicks,
       "h3cDot11BSSRxStatisTable": h3cDot11BSSRxStatisTable,
       "h3cDot11BSSRxStatisEntry": h3cDot11BSSRxStatisEntry,
       "h3cDot11BSSRxFrameCnt": h3cDot11BSSRxFrameCnt,
       "h3cDot11BSSRxFrameBytes": h3cDot11BSSRxFrameBytes,
       "h3cDot11BSSRxDataFrameCnt": h3cDot11BSSRxDataFrameCnt,
       "h3cDot11BSSRxDataFrameBytes": h3cDot11BSSRxDataFrameBytes,
       "h3cDot11BSSRxAssociateFrameCnt": h3cDot11BSSRxAssociateFrameCnt,
       "h3cDot11BSSRxFrameErrorRatio": h3cDot11BSSRxFrameErrorRatio,
       "h3cDot11BSSRxPayloadBytes": h3cDot11BSSRxPayloadBytes,
       "h3cDot11BSSRxUniFrameCnt": h3cDot11BSSRxUniFrameCnt,
       "h3cDot11BSSRxNonUniFrameCnt": h3cDot11BSSRxNonUniFrameCnt,
       "h3cDot11BSSRxAuthenFrameCnt": h3cDot11BSSRxAuthenFrameCnt,
       "h3cDot11BSSTxStatisTable": h3cDot11BSSTxStatisTable,
       "h3cDot11BSSTxStatisEntry": h3cDot11BSSTxStatisEntry,
       "h3cDot11BSSTxFrameCnt": h3cDot11BSSTxFrameCnt,
       "h3cDot11BSSTxFrameBytes": h3cDot11BSSTxFrameBytes,
       "h3cDot11BSSTxDataFrameCnt": h3cDot11BSSTxDataFrameCnt,
       "h3cDot11BSSTxDataFrameBytes": h3cDot11BSSTxDataFrameBytes,
       "h3cDot11BSSTxAssociateFrameCnt": h3cDot11BSSTxAssociateFrameCnt,
       "h3cDot11BSSTxPayloadBytes": h3cDot11BSSTxPayloadBytes,
       "h3cDot11BSSTxRetryCnt": h3cDot11BSSTxRetryCnt,
       "h3cDot11BSSTxUniFrameCnt": h3cDot11BSSTxUniFrameCnt,
       "h3cDot11BSSTxNonUniFrameCnt": h3cDot11BSSTxNonUniFrameCnt,
       "h3cDot11BSSTxAuthenFrameCnt": h3cDot11BSSTxAuthenFrameCnt,
       "h3cDot11BSSAssocStatisTable": h3cDot11BSSAssocStatisTable,
       "h3cDot11BSSAssocStatisEntry": h3cDot11BSSAssocStatisEntry,
       "h3cDot11BSSStationAssocSum": h3cDot11BSSStationAssocSum,
       "h3cDot11BSSStationAssocFailSum": h3cDot11BSSStationAssocFailSum,
       "h3cDot11BSSStationReassocSum": h3cDot11BSSStationReassocSum,
       "h3cDot11BSSStationAssocRejectSum": h3cDot11BSSStationAssocRejectSum,
       "h3cDot11BSSStationExDeAssocSum": h3cDot11BSSStationExDeAssocSum,
       "h3cDot11BSSStationCurAssocSum": h3cDot11BSSStationCurAssocSum,
       "h3cDot11BSSStationAssocReqSum": h3cDot11BSSStationAssocReqSum,
       "h3cDot11BSSStationCurAuthSum": h3cDot11BSSStationCurAuthSum,
       "h3cDot11APLinkStatisTable": h3cDot11APLinkStatisTable,
       "h3cDot11APLinkStatisEntry": h3cDot11APLinkStatisEntry,
       "h3cDot11UpLinkUpDownTimes": h3cDot11UpLinkUpDownTimes,
       "h3cDot11DownLinkUpDownTimes": h3cDot11DownLinkUpDownTimes,
       "h3cDot11RadioAssocStatisTable": h3cDot11RadioAssocStatisTable,
       "h3cDot11RadioAssocStatisEntry": h3cDot11RadioAssocStatisEntry,
       "h3cDot11RadioStaAssocSum": h3cDot11RadioStaAssocSum,
       "h3cDot11RadioStaAssocFailSum": h3cDot11RadioStaAssocFailSum,
       "h3cDot11RadioStaReassocSum": h3cDot11RadioStaReassocSum,
       "h3cDot11RadioStaAssocRejectSum": h3cDot11RadioStaAssocRejectSum,
       "h3cDot11RadioStaExDeAssocSum": h3cDot11RadioStaExDeAssocSum,
       "h3cDot11RadioStaCurAssocSum": h3cDot11RadioStaCurAssocSum,
       "h3cDot11RadioMngFrameStatisTable": h3cDot11RadioMngFrameStatisTable,
       "h3cDot11RadioMngFrameStatisEntry": h3cDot11RadioMngFrameStatisEntry,
       "h3cDot11RadioStatisIndex": h3cDot11RadioStatisIndex,
       "h3cDot11MngFrameType": h3cDot11MngFrameType,
       "h3cDot11MngFrameCnt": h3cDot11MngFrameCnt,
       "h3cDot11APAuthFailStatisTable": h3cDot11APAuthFailStatisTable,
       "h3cDot11APAuthFailStatisEntry": h3cDot11APAuthFailStatisEntry,
       "h3cDot11APAuthFailStatisType": h3cDot11APAuthFailStatisType,
       "h3cDot11APAuthFailStatisCnt": h3cDot11APAuthFailStatisCnt,
       "h3cDot11APAssocFailStatisTable": h3cDot11APAssocFailStatisTable,
       "h3cDot11APAssocFailStatisEntry": h3cDot11APAssocFailStatisEntry,
       "h3cDot11APAssocFailStatisType": h3cDot11APAssocFailStatisType,
       "h3cDot11APAssocFailStatisCnt": h3cDot11APAssocFailStatisCnt,
       "h3cDot11APReassocStatisTable": h3cDot11APReassocStatisTable,
       "h3cDot11APReassocStatisEntry": h3cDot11APReassocStatisEntry,
       "h3cDot11APReassocStatisType": h3cDot11APReassocStatisType,
       "h3cDot11APReassocStatisCnt": h3cDot11APReassocStatisCnt,
       "h3cDot11APUserAuthStatisTable": h3cDot11APUserAuthStatisTable,
       "h3cDot11APUserAuthStatisEntry": h3cDot11APUserAuthStatisEntry,
       "h3cDot11UserAuthStatisType": h3cDot11UserAuthStatisType,
       "h3cDot11UserAuthStatisCnt": h3cDot11UserAuthStatisCnt,
       "h3cDot11APDeauthStatisTable": h3cDot11APDeauthStatisTable,
       "h3cDot11APDeauthStatisEntry": h3cDot11APDeauthStatisEntry,
       "h3cDot11APDeauthStatisType": h3cDot11APDeauthStatisType,
       "h3cDot11APDeauthStatisCnt": h3cDot11APDeauthStatisCnt,
       "h3cDot11APDeassocStatisTable": h3cDot11APDeassocStatisTable,
       "h3cDot11APDeassocStatisEntry": h3cDot11APDeassocStatisEntry,
       "h3cDot11APDeassocStatisType": h3cDot11APDeassocStatisType,
       "h3cDot11APDeassocStatisCnt": h3cDot11APDeassocStatisCnt,
       "h3cDot11APAssocFailStatis2Table": h3cDot11APAssocFailStatis2Table,
       "h3cDot11APAssocFailStatis2Entry": h3cDot11APAssocFailStatis2Entry,
       "h3cDot11APAssocFailStatis2Type": h3cDot11APAssocFailStatis2Type,
       "h3cDot11APAssocFailStatis2Cnt": h3cDot11APAssocFailStatis2Cnt,
       "h3cDot11APIfStatisTable": h3cDot11APIfStatisTable,
       "h3cDot11APIfStatisEntry": h3cDot11APIfStatisEntry,
       "h3cDot11APIfInPkts": h3cDot11APIfInPkts,
       "h3cDot11APIfInNormalPkts": h3cDot11APIfInNormalPkts,
       "h3cDot11APIfInErrorPkts": h3cDot11APIfInErrorPkts,
       "h3cDot11APIfOutPkts": h3cDot11APIfOutPkts,
       "h3cDot11APIfInOctets": h3cDot11APIfInOctets,
       "h3cDot11APIfOutOctets": h3cDot11APIfOutOctets,
       "h3cDot11APIfFlowOut": h3cDot11APIfFlowOut,
       "h3cDot11APIfFlowIN": h3cDot11APIfFlowIN,
       "h3cDot11APIfInUcastPkts": h3cDot11APIfInUcastPkts,
       "h3cDot11APIfInNUcastPkts": h3cDot11APIfInNUcastPkts,
       "h3cDot11APIfInDiscardPkts": h3cDot11APIfInDiscardPkts,
       "h3cDot11APIfOutUcastPkts": h3cDot11APIfOutUcastPkts,
       "h3cDot11APIfOutNUcastPkts": h3cDot11APIfOutNUcastPkts,
       "h3cDot11APIfOutDiscardPkts": h3cDot11APIfOutDiscardPkts,
       "h3cDot11APIfOutErrorPkts": h3cDot11APIfOutErrorPkts,
       "h3cDot11APIfUpdownTimes": h3cDot11APIfUpdownTimes,
       "h3cDot11APIfStatusKeepTime": h3cDot11APIfStatusKeepTime,
       "h3cDot11APIfOperStatus": h3cDot11APIfOperStatus,
       "h3cDot11APIfInBrdcastPkts": h3cDot11APIfInBrdcastPkts,
       "h3cDot11APIfOutBrdcastPkts": h3cDot11APIfOutBrdcastPkts,
       "h3cDot11APIfInMulcastPkts": h3cDot11APIfInMulcastPkts,
       "h3cDot11APIfOutMulcastPkts": h3cDot11APIfOutMulcastPkts,
       "h3cDot11APIfInPayloadOctets": h3cDot11APIfInPayloadOctets,
       "h3cDot11APIfOutPayloadOctets": h3cDot11APIfOutPayloadOctets,
       "h3cDot11RadioMngFrmStatisTable": h3cDot11RadioMngFrmStatisTable,
       "h3cDot11RadioMngFrmStatisEntry": h3cDot11RadioMngFrmStatisEntry,
       "h3cDot11MngFrmType": h3cDot11MngFrmType,
       "h3cDot11MngFrmCnt": h3cDot11MngFrmCnt,
       "h3cDot11APPacketSizeStatisTable": h3cDot11APPacketSizeStatisTable,
       "h3cDot11APPacketSizeStatisEntry": h3cDot11APPacketSizeStatisEntry,
       "h3cDot11APPacketSize": h3cDot11APPacketSize,
       "h3cDot11APRXPacketSizeCount": h3cDot11APRXPacketSizeCount,
       "h3cDot11APTXPacketSizeCount": h3cDot11APTXPacketSizeCount,
       "h3cDot11APPacketRateStatisTable": h3cDot11APPacketRateStatisTable,
       "h3cDot11APPacketRateStatisEntry": h3cDot11APPacketRateStatisEntry,
       "h3cDot11APPacketRate": h3cDot11APPacketRate,
       "h3cDot11APRXPacketRateCount": h3cDot11APRXPacketRateCount,
       "h3cDot11APTXPacketRateCount": h3cDot11APTXPacketRateCount,
       "h3cDot11APPacketMCSRateStatisTable": h3cDot11APPacketMCSRateStatisTable,
       "h3cDot11APPacketMCSRateStatisEntry": h3cDot11APPacketMCSRateStatisEntry,
       "h3cDot11APPacketMCSRate": h3cDot11APPacketMCSRate,
       "h3cDot11APRXPacketMCSRateCount": h3cDot11APRXPacketMCSRateCount,
       "h3cDot11APTXPacketMCSRateCount": h3cDot11APTXPacketMCSRateCount,
       "h3cDot11APAssocFailStatis3Table": h3cDot11APAssocFailStatis3Table,
       "h3cDot11APAssocFailStatis3Entry": h3cDot11APAssocFailStatis3Entry,
       "h3cDot11APAssocFailStatis3SRCnt": h3cDot11APAssocFailStatis3SRCnt,
       "h3cDot11APAssocFailStatis3NSRCnt": h3cDot11APAssocFailStatis3NSRCnt,
       "h3cDot11APAssocFailStatis3URCCnt": h3cDot11APAssocFailStatis3URCCnt,
       "h3cDot11APAssocFailStatis3RFCnt": h3cDot11APAssocFailStatis3RFCnt,
       "h3cDot11APAssocFailStatis3OtherCnt": h3cDot11APAssocFailStatis3OtherCnt,
       "h3cDot11APIfStatisByAPIDTable": h3cDot11APIfStatisByAPIDTable,
       "h3cDot11APIfStatisByAPIDEntry": h3cDot11APIfStatisByAPIDEntry,
       "h3cDot11APIfInPkts2": h3cDot11APIfInPkts2,
       "h3cDot11APIfInNormalPkts2": h3cDot11APIfInNormalPkts2,
       "h3cDot11APIfInErrorPkts2": h3cDot11APIfInErrorPkts2,
       "h3cDot11APIfOutPkts2": h3cDot11APIfOutPkts2,
       "h3cDot11APIfInOctets2": h3cDot11APIfInOctets2,
       "h3cDot11APIfOutOctets2": h3cDot11APIfOutOctets2,
       "h3cDot11APIfFlowOut2": h3cDot11APIfFlowOut2,
       "h3cDot11APIfFlowIN2": h3cDot11APIfFlowIN2,
       "h3cDot11APIfInUcastPkts2": h3cDot11APIfInUcastPkts2,
       "h3cDot11APIfInNUcastPkts2": h3cDot11APIfInNUcastPkts2,
       "h3cDot11APIfInDiscardPkts2": h3cDot11APIfInDiscardPkts2,
       "h3cDot11APIfOutUcastPkts2": h3cDot11APIfOutUcastPkts2,
       "h3cDot11APIfOutNUcastPkts2": h3cDot11APIfOutNUcastPkts2,
       "h3cDot11APIfOutDiscardPkts2": h3cDot11APIfOutDiscardPkts2,
       "h3cDot11APIfOutErrorPkts2": h3cDot11APIfOutErrorPkts2,
       "h3cDot11APIfUpdownTimes2": h3cDot11APIfUpdownTimes2,
       "h3cDot11APIfStatusKeepTime2": h3cDot11APIfStatusKeepTime2,
       "h3cDot11APIfOperStatus2": h3cDot11APIfOperStatus2,
       "h3cDot11APIfInBrdcastPkts2": h3cDot11APIfInBrdcastPkts2,
       "h3cDot11APIfOutBrdcastPkts2": h3cDot11APIfOutBrdcastPkts2,
       "h3cDot11APIfInMulcastPkts2": h3cDot11APIfInMulcastPkts2,
       "h3cDot11APIfOutMulcastPkts2": h3cDot11APIfOutMulcastPkts2,
       "h3cDot11APIfInPayloadOctets2": h3cDot11APIfInPayloadOctets2,
       "h3cDot11APIfOutPayloadOctets2": h3cDot11APIfOutPayloadOctets2,
       "h3cDot11APIfInDataOctets2": h3cDot11APIfInDataOctets2,
       "h3cDot11APIfOutDataOctets2": h3cDot11APIfOutDataOctets2,
       "h3cDot11APUserSecAuthStatisTable": h3cDot11APUserSecAuthStatisTable,
       "h3cDot11APUserSecAuthStatisEntry": h3cDot11APUserSecAuthStatisEntry,
       "h3cDot11APUserAuthCurNumber": h3cDot11APUserAuthCurNumber,
       "h3cDot11APUserConnFailCnt": h3cDot11APUserConnFailCnt,
       "h3cDot11APUserAuthReqCnt": h3cDot11APUserAuthReqCnt,
       "h3cDot11APUserAuthSuccCnt": h3cDot11APUserAuthSuccCnt,
       "h3cDot11APUserAuthFailCnt": h3cDot11APUserAuthFailCnt,
       "h3cDot11AllUserOnlineTime": h3cDot11AllUserOnlineTime,
       "h3cDot11APUserInfoStatisTable": h3cDot11APUserInfoStatisTable,
       "h3cDot11APUserInfoStatisEntry": h3cDot11APUserInfoStatisEntry,
       "h3cDot11APUserMacAddr": h3cDot11APUserMacAddr,
       "h3cDot11APUserIpAddr": h3cDot11APUserIpAddr,
       "h3cDot11APUserLoginName": h3cDot11APUserLoginName,
       "h3cDot11APUserLoginTime": h3cDot11APUserLoginTime,
       "h3cDot11APUserOnlineTime": h3cDot11APUserOnlineTime,
       "h3cDot11APReassocStatis2Table": h3cDot11APReassocStatis2Table,
       "h3cDot11APReassocStatis2Entry": h3cDot11APReassocStatis2Entry,
       "h3cDot11APReassocFailStatis2Cnt": h3cDot11APReassocFailStatis2Cnt,
       "h3cDot11TrafficTable": h3cDot11TrafficTable,
       "h3cDot11TrafficEntry": h3cDot11TrafficEntry,
       "h3cDot11SSIDIndex": h3cDot11SSIDIndex,
       "h3cDot11UpPacketNumber": h3cDot11UpPacketNumber,
       "h3cDot11UpByteNumber": h3cDot11UpByteNumber,
       "h3cDot11DownPacketNumber": h3cDot11DownPacketNumber,
       "h3cDot11DownByteNumber": h3cDot11DownByteNumber,
       "h3cDot11APEchoStatisTable": h3cDot11APEchoStatisTable,
       "h3cDot11APEchoInfoStatisEntry": h3cDot11APEchoInfoStatisEntry,
       "h3cDot11APEchoAvgDelay": h3cDot11APEchoAvgDelay,
       "h3cDot11APEchoRequestCnt": h3cDot11APEchoRequestCnt,
       "h3cDot11APEchoRespLossCnt": h3cDot11APEchoRespLossCnt,
       "h3cDot11APMtNotifyGroup": h3cDot11APMtNotifyGroup,
       "h3cDot11APMtTraps": h3cDot11APMtTraps,
       "h3cDot11APMtWorkModeChgTrap": h3cDot11APMtWorkModeChgTrap,
       "h3cDot11APMtCfgErrorTrap": h3cDot11APMtCfgErrorTrap,
       "h3cDot11APMtRadioFailTrap": h3cDot11APMtRadioFailTrap,
       "h3cDot11APMtRadioFailRecoverTrap": h3cDot11APMtRadioFailRecoverTrap,
       "h3cDot11APMtRdoChanlChgTrap": h3cDot11APMtRdoChanlChgTrap,
       "h3cDot11APMtTimeSynFail": h3cDot11APMtTimeSynFail,
       "h3cDot11APMtChlIntfDetected": h3cDot11APMtChlIntfDetected,
       "h3cDot11APMtIntfAPDetected": h3cDot11APMtIntfAPDetected,
       "h3cDot11APMtIntfStaDetected": h3cDot11APMtIntfStaDetected,
       "h3cDot11APMtIPChange": h3cDot11APMtIPChange,
       "h3cDot11APFlashWriteFailure": h3cDot11APFlashWriteFailure,
       "h3cDot11APSysReboot": h3cDot11APSysReboot,
       "h3cDot11APMtAvailChlTooLow": h3cDot11APMtAvailChlTooLow,
       "h3cDot11APImgDwldSuccess": h3cDot11APImgDwldSuccess,
       "h3cDot11APInterfDetectedTrap": h3cDot11APInterfDetectedTrap,
       "h3cDot11APInterfClearTrap": h3cDot11APInterfClearTrap,
       "h3cDot11StaInterfDetectedTrap": h3cDot11StaInterfDetectedTrap,
       "h3cDot11StaInterfClearTrap": h3cDot11StaInterfClearTrap,
       "h3cDot11OtherDevIntDetectedTrap": h3cDot11OtherDevIntDetectedTrap,
       "h3cDot11OtherDevIntClearTrap": h3cDot11OtherDevIntClearTrap,
       "h3cDot11APModuleTroubleTrap": h3cDot11APModuleTroubleTrap,
       "h3cDot11APModuleTroubleClearTrap": h3cDot11APModuleTroubleClearTrap,
       "h3cDot11APRadioDownTrap": h3cDot11APRadioDownTrap,
       "h3cDot11APRadioDownRecovTrap": h3cDot11APRadioDownRecovTrap,
       "h3cDot11APStaFullTrap": h3cDot11APStaFullTrap,
       "h3cDot11APStaFullRecoverTrap": h3cDot11APStaFullRecoverTrap,
       "h3cDot11DFSFreeCntBelowThrRecov": h3cDot11DFSFreeCntBelowThrRecov,
       "h3cDot11APCpuUsageHigh": h3cDot11APCpuUsageHigh,
       "h3cDot11APCpuUsageHighRecover": h3cDot11APCpuUsageHighRecover,
       "h3cDot11APMemUsageHigh": h3cDot11APMemUsageHigh,
       "h3cDot11APMemUsageHighRecover": h3cDot11APMemUsageHighRecover,
       "h3cDot11APTrapUserCntExceedThre": h3cDot11APTrapUserCntExceedThre,
       "h3cDot11APMtDetectedIntfAP": h3cDot11APMtDetectedIntfAP,
       "h3cDot11APMtDetectedIntfSTA": h3cDot11APMtDetectedIntfSTA,
       "h3cDot11APMtDetectedIntfOtherDev": h3cDot11APMtDetectedIntfOtherDev,
       "h3cDot11DetcAdjChlIntfAP": h3cDot11DetcAdjChlIntfAP,
       "h3cDot11DetcAdjChlIntfAPClear": h3cDot11DetcAdjChlIntfAPClear,
       "h3cDot11APMtTrapVarObjects": h3cDot11APMtTrapVarObjects,
       "h3cDot11APMtTrapCfgErrReason": h3cDot11APMtTrapCfgErrReason,
       "h3cDot11APMtTrapRadioFailReason": h3cDot11APMtTrapRadioFailReason,
       "h3cDot11APMtTrapOldChannel": h3cDot11APMtTrapOldChannel,
       "h3cDot11APMtTrapNewChannel": h3cDot11APMtTrapNewChannel,
       "h3cDot11APChannelChgMode": h3cDot11APChannelChgMode,
       "h3cDot11APChgWorkMode": h3cDot11APChgWorkMode,
       "h3cDot11APIntfDevMACAddress": h3cDot11APIntfDevMACAddress,
       "h3cDot11APMtTrapOldIPAddr": h3cDot11APMtTrapOldIPAddr,
       "h3cDot11CurrInterfDetectedNum": h3cDot11CurrInterfDetectedNum,
       "h3cDot11StaFullReason": h3cDot11StaFullReason,
       "h3cDot11StaLimitNumber": h3cDot11StaLimitNumber,
       "h3cDot11APRadioDownReason": h3cDot11APRadioDownReason,
       "h3cDot11InterfMacList": h3cDot11InterfMacList,
       "h3cDot11APTrapUserCnt": h3cDot11APTrapUserCnt,
       "h3cDot11APTrapUserThreshold": h3cDot11APTrapUserThreshold,
       "h3cDot11APMtChanlChgCount": h3cDot11APMtChanlChgCount,
       "h3cDot11APMtFormerApVersion": h3cDot11APMtFormerApVersion,
       "h3cDot11APMtAPID": h3cDot11APMtAPID,
       "h3cDot11APMtRadioID": h3cDot11APMtRadioID,
       "h3cDot11APMtChannel": h3cDot11APMtChannel,
       "h3cDot11APMtInterfMacAdd": h3cDot11APMtInterfMacAdd,
       "h3cDot11APMtAdjChannel": h3cDot11APMtAdjChannel,
       "h3cDot11APMtFirstTrapTime": h3cDot11APMtFirstTrapTime}
)
