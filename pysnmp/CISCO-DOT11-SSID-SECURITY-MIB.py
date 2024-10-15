# SNMP MIB module (CISCO-DOT11-SSID-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-SSID-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:58 2024
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

(CDot11IfVlanIdOrZero,) = mibBuilder.importSymbols(
    "CISCO-DOT11-IF-MIB",
    "CDot11IfVlanIdOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(dot11AuthenticationAlgorithmsIndex,) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "dot11AuthenticationAlgorithmsIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11SsidSecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413)
)
ciscoDot11SsidSecMIB.setRevisions(
        ("2007-04-12 00:00",
         "2006-05-16 00:00",
         "2004-09-14 00:00",
         "2004-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDot11SecAuthKeyMgmtType(Bits, TextualConvention):
    status = "current"


class CDot11WiFiPaPreSharedKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CDot11SsidString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CDot11VlanName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CDot11InformationElementType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoDot11SsidSecMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11SsidSecMIBObjects = _CiscoDot11SsidSecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1)
)
_Cdot11SecSsidManagement_ObjectIdentity = ObjectIdentity
cdot11SecSsidManagement = _Cdot11SecSsidManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1)
)
_Cdot11SecAuxSsidTable_Object = MibTable
cdot11SecAuxSsidTable = _Cdot11SecAuxSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdot11SecAuxSsidTable.setStatus("current")
_Cdot11SecAuxSsidEntry_Object = MibTableRow
cdot11SecAuxSsidEntry = _Cdot11SecAuxSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1)
)
cdot11SecAuxSsidEntry.setIndexNames(
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"),
)
if mibBuilder.loadTexts:
    cdot11SecAuxSsidEntry.setStatus("current")
_Cdot11SecAuxSsid_Type = CDot11SsidString
_Cdot11SecAuxSsid_Object = MibTableColumn
cdot11SecAuxSsid = _Cdot11SecAuxSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 1),
    _Cdot11SecAuxSsid_Type()
)
cdot11SecAuxSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11SecAuxSsid.setStatus("current")


class _Cdot11SecAuxSsidBroadcast_Type(TruthValue):
    """Custom type cdot11SecAuxSsidBroadcast based on TruthValue"""


_Cdot11SecAuxSsidBroadcast_Object = MibTableColumn
cdot11SecAuxSsidBroadcast = _Cdot11SecAuxSsidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 2),
    _Cdot11SecAuxSsidBroadcast_Type()
)
cdot11SecAuxSsidBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidBroadcast.setStatus("current")


class _Cdot11SecAuxSsidInfraStruct_Type(Integer32):
    """Custom type cdot11SecAuxSsidInfraStruct based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infraStructure", 1),
          ("nonInfraStructure", 2),
          ("optional", 3))
    )


_Cdot11SecAuxSsidInfraStruct_Type.__name__ = "Integer32"
_Cdot11SecAuxSsidInfraStruct_Object = MibTableColumn
cdot11SecAuxSsidInfraStruct = _Cdot11SecAuxSsidInfraStruct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 3),
    _Cdot11SecAuxSsidInfraStruct_Type()
)
cdot11SecAuxSsidInfraStruct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidInfraStruct.setStatus("current")


class _Cdot11SecAuxSsidProxyMobileIp_Type(TruthValue):
    """Custom type cdot11SecAuxSsidProxyMobileIp based on TruthValue"""


_Cdot11SecAuxSsidProxyMobileIp_Object = MibTableColumn
cdot11SecAuxSsidProxyMobileIp = _Cdot11SecAuxSsidProxyMobileIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 4),
    _Cdot11SecAuxSsidProxyMobileIp_Type()
)
cdot11SecAuxSsidProxyMobileIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidProxyMobileIp.setStatus("current")


class _Cdot11SecAuxSsidMaxStations_Type(Unsigned32):
    """Custom type cdot11SecAuxSsidMaxStations based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_Cdot11SecAuxSsidMaxStations_Type.__name__ = "Unsigned32"
_Cdot11SecAuxSsidMaxStations_Object = MibTableColumn
cdot11SecAuxSsidMaxStations = _Cdot11SecAuxSsidMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 5),
    _Cdot11SecAuxSsidMaxStations_Type()
)
cdot11SecAuxSsidMaxStations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidMaxStations.setStatus("current")


class _Cdot11SecAuxSsidVlan_Type(CDot11IfVlanIdOrZero):
    """Custom type cdot11SecAuxSsidVlan based on CDot11IfVlanIdOrZero"""
    defaultValue = 0


_Cdot11SecAuxSsidVlan_Object = MibTableColumn
cdot11SecAuxSsidVlan = _Cdot11SecAuxSsidVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 6),
    _Cdot11SecAuxSsidVlan_Type()
)
cdot11SecAuxSsidVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidVlan.setStatus("current")


class _Cdot11SecAuxSsidWpaPsk_Type(CDot11WiFiPaPreSharedKey):
    """Custom type cdot11SecAuxSsidWpaPsk based on CDot11WiFiPaPreSharedKey"""
    defaultHexValue = ""


_Cdot11SecAuxSsidWpaPsk_Object = MibTableColumn
cdot11SecAuxSsidWpaPsk = _Cdot11SecAuxSsidWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 7),
    _Cdot11SecAuxSsidWpaPsk_Type()
)
cdot11SecAuxSsidWpaPsk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidWpaPsk.setStatus("current")
_Cdot11SecAuxRadiusAccounting_Type = SnmpAdminString
_Cdot11SecAuxRadiusAccounting_Object = MibTableColumn
cdot11SecAuxRadiusAccounting = _Cdot11SecAuxRadiusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 8),
    _Cdot11SecAuxRadiusAccounting_Type()
)
cdot11SecAuxRadiusAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxRadiusAccounting.setStatus("current")
_Cdot11SecAuxSsidLoginUsername_Type = SnmpAdminString
_Cdot11SecAuxSsidLoginUsername_Object = MibTableColumn
cdot11SecAuxSsidLoginUsername = _Cdot11SecAuxSsidLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 9),
    _Cdot11SecAuxSsidLoginUsername_Type()
)
cdot11SecAuxSsidLoginUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidLoginUsername.setStatus("current")
_Cdot11SecAuxSsidLoginPassword_Type = SnmpAdminString
_Cdot11SecAuxSsidLoginPassword_Object = MibTableColumn
cdot11SecAuxSsidLoginPassword = _Cdot11SecAuxSsidLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 10),
    _Cdot11SecAuxSsidLoginPassword_Type()
)
cdot11SecAuxSsidLoginPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidLoginPassword.setStatus("current")
_Cdot11SecAuxSsidAuthKeyMgmt_Type = CDot11SecAuthKeyMgmtType
_Cdot11SecAuxSsidAuthKeyMgmt_Object = MibTableColumn
cdot11SecAuxSsidAuthKeyMgmt = _Cdot11SecAuxSsidAuthKeyMgmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 11),
    _Cdot11SecAuxSsidAuthKeyMgmt_Type()
)
cdot11SecAuxSsidAuthKeyMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthKeyMgmt.setStatus("current")


class _Cdot11SecAuxSsidAuthKeyMgmtOpt_Type(TruthValue):
    """Custom type cdot11SecAuxSsidAuthKeyMgmtOpt based on TruthValue"""


_Cdot11SecAuxSsidAuthKeyMgmtOpt_Object = MibTableColumn
cdot11SecAuxSsidAuthKeyMgmtOpt = _Cdot11SecAuxSsidAuthKeyMgmtOpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 12),
    _Cdot11SecAuxSsidAuthKeyMgmtOpt_Type()
)
cdot11SecAuxSsidAuthKeyMgmtOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthKeyMgmtOpt.setStatus("current")
_Cdot11SecAuxSsidRowStatus_Type = RowStatus
_Cdot11SecAuxSsidRowStatus_Object = MibTableColumn
cdot11SecAuxSsidRowStatus = _Cdot11SecAuxSsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 13),
    _Cdot11SecAuxSsidRowStatus_Type()
)
cdot11SecAuxSsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidRowStatus.setStatus("current")


class _Cdot11SecAuxSsidWirelessNetId_Type(Integer32):
    """Custom type cdot11SecAuxSsidWirelessNetId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Cdot11SecAuxSsidWirelessNetId_Type.__name__ = "Integer32"
_Cdot11SecAuxSsidWirelessNetId_Object = MibTableColumn
cdot11SecAuxSsidWirelessNetId = _Cdot11SecAuxSsidWirelessNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 14),
    _Cdot11SecAuxSsidWirelessNetId_Type()
)
cdot11SecAuxSsidWirelessNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidWirelessNetId.setStatus("current")


class _Cdot11SecSsidRedirectAddrType_Type(InetAddressType):
    """Custom type cdot11SecSsidRedirectAddrType based on InetAddressType"""


_Cdot11SecSsidRedirectAddrType_Object = MibTableColumn
cdot11SecSsidRedirectAddrType = _Cdot11SecSsidRedirectAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 15),
    _Cdot11SecSsidRedirectAddrType_Type()
)
cdot11SecSsidRedirectAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecSsidRedirectAddrType.setStatus("current")


class _Cdot11SecSsidRedirectDestAddr_Type(InetAddress):
    """Custom type cdot11SecSsidRedirectDestAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Cdot11SecSsidRedirectDestAddr_Object = MibTableColumn
cdot11SecSsidRedirectDestAddr = _Cdot11SecSsidRedirectDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 16),
    _Cdot11SecSsidRedirectDestAddr_Type()
)
cdot11SecSsidRedirectDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecSsidRedirectDestAddr.setStatus("current")
_Cdot11SecSsidRedirectFilter_Type = SnmpAdminString
_Cdot11SecSsidRedirectFilter_Object = MibTableColumn
cdot11SecSsidRedirectFilter = _Cdot11SecSsidRedirectFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 17),
    _Cdot11SecSsidRedirectFilter_Type()
)
cdot11SecSsidRedirectFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecSsidRedirectFilter.setStatus("current")


class _Cdot11SecSsidInformationElement_Type(CDot11InformationElementType):
    """Custom type cdot11SecSsidInformationElement based on CDot11InformationElementType"""
    defaultBinValue = "0"


_Cdot11SecSsidInformationElement_Object = MibTableColumn
cdot11SecSsidInformationElement = _Cdot11SecSsidInformationElement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 18),
    _Cdot11SecSsidInformationElement_Type()
)
cdot11SecSsidInformationElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecSsidInformationElement.setStatus("current")


class _Cdot11SecAuxSsidVlanName_Type(CDot11VlanName):
    """Custom type cdot11SecAuxSsidVlanName based on CDot11VlanName"""
    defaultValue = OctetString(" ")


_Cdot11SecAuxSsidVlanName_Object = MibTableColumn
cdot11SecAuxSsidVlanName = _Cdot11SecAuxSsidVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 19),
    _Cdot11SecAuxSsidVlanName_Type()
)
cdot11SecAuxSsidVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidVlanName.setStatus("current")


class _Cdot11SecAuxSsidMbssidBroadcast_Type(TruthValue):
    """Custom type cdot11SecAuxSsidMbssidBroadcast based on TruthValue"""


_Cdot11SecAuxSsidMbssidBroadcast_Object = MibTableColumn
cdot11SecAuxSsidMbssidBroadcast = _Cdot11SecAuxSsidMbssidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 20),
    _Cdot11SecAuxSsidMbssidBroadcast_Type()
)
cdot11SecAuxSsidMbssidBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidMbssidBroadcast.setStatus("current")


class _Cdot11SecAuxSsidMbssidDtimPeriod_Type(Integer32):
    """Custom type cdot11SecAuxSsidMbssidDtimPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdot11SecAuxSsidMbssidDtimPeriod_Type.__name__ = "Integer32"
_Cdot11SecAuxSsidMbssidDtimPeriod_Object = MibTableColumn
cdot11SecAuxSsidMbssidDtimPeriod = _Cdot11SecAuxSsidMbssidDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 21),
    _Cdot11SecAuxSsidMbssidDtimPeriod_Type()
)
cdot11SecAuxSsidMbssidDtimPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidMbssidDtimPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidMbssidDtimPeriod.setUnits("beacons")
_Cdot11SecAuxSsidAuthTable_Object = MibTable
cdot11SecAuxSsidAuthTable = _Cdot11SecAuxSsidAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthTable.setStatus("current")
_Cdot11SecAuxSsidAuthEntry_Object = MibTableRow
cdot11SecAuxSsidAuthEntry = _Cdot11SecAuxSsidAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1)
)
cdot11SecAuxSsidAuthEntry.setIndexNames(
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"),
    (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthEntry.setStatus("current")
_Cdot11SecAuxSsidAuthEnabled_Type = TruthValue
_Cdot11SecAuxSsidAuthEnabled_Object = MibTableColumn
cdot11SecAuxSsidAuthEnabled = _Cdot11SecAuxSsidAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 1),
    _Cdot11SecAuxSsidAuthEnabled_Type()
)
cdot11SecAuxSsidAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthEnabled.setStatus("current")
_Cdot11SecAuxSsidAuthPlusEap_Type = TruthValue
_Cdot11SecAuxSsidAuthPlusEap_Object = MibTableColumn
cdot11SecAuxSsidAuthPlusEap = _Cdot11SecAuxSsidAuthPlusEap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 2),
    _Cdot11SecAuxSsidAuthPlusEap_Type()
)
cdot11SecAuxSsidAuthPlusEap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthPlusEap.setStatus("current")
_Cdot11SecAuxSsidAuthPlusMac_Type = TruthValue
_Cdot11SecAuxSsidAuthPlusMac_Object = MibTableColumn
cdot11SecAuxSsidAuthPlusMac = _Cdot11SecAuxSsidAuthPlusMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 3),
    _Cdot11SecAuxSsidAuthPlusMac_Type()
)
cdot11SecAuxSsidAuthPlusMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthPlusMac.setStatus("current")
_Cdot11SecAuxSsidAuthEapMethod_Type = SnmpAdminString
_Cdot11SecAuxSsidAuthEapMethod_Object = MibTableColumn
cdot11SecAuxSsidAuthEapMethod = _Cdot11SecAuxSsidAuthEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 4),
    _Cdot11SecAuxSsidAuthEapMethod_Type()
)
cdot11SecAuxSsidAuthEapMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthEapMethod.setStatus("current")
_Cdot11SecAuxSsidAuthMacMethod_Type = SnmpAdminString
_Cdot11SecAuxSsidAuthMacMethod_Object = MibTableColumn
cdot11SecAuxSsidAuthMacMethod = _Cdot11SecAuxSsidAuthMacMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 5),
    _Cdot11SecAuxSsidAuthMacMethod_Type()
)
cdot11SecAuxSsidAuthMacMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthMacMethod.setStatus("current")
_Cdot11SecAuxSsidAuthMacAlternate_Type = TruthValue
_Cdot11SecAuxSsidAuthMacAlternate_Object = MibTableColumn
cdot11SecAuxSsidAuthMacAlternate = _Cdot11SecAuxSsidAuthMacAlternate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 6),
    _Cdot11SecAuxSsidAuthMacAlternate_Type()
)
cdot11SecAuxSsidAuthMacAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecAuxSsidAuthMacAlternate.setStatus("current")
_Cdot11SecInterfSsidTable_Object = MibTable
cdot11SecInterfSsidTable = _Cdot11SecInterfSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdot11SecInterfSsidTable.setStatus("current")
_Cdot11SecInterfSsidEntry_Object = MibTableRow
cdot11SecInterfSsidEntry = _Cdot11SecInterfSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3, 1)
)
cdot11SecInterfSsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"),
)
if mibBuilder.loadTexts:
    cdot11SecInterfSsidEntry.setStatus("current")
_Cdot11SecInterfSsidRowStatus_Type = RowStatus
_Cdot11SecInterfSsidRowStatus_Object = MibTableColumn
cdot11SecInterfSsidRowStatus = _Cdot11SecInterfSsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3, 1, 1),
    _Cdot11SecInterfSsidRowStatus_Type()
)
cdot11SecInterfSsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecInterfSsidRowStatus.setStatus("current")
_Cdot11MbssidMacAddrSupportTable_Object = MibTable
cdot11MbssidMacAddrSupportTable = _Cdot11MbssidMacAddrSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdot11MbssidMacAddrSupportTable.setStatus("current")
_Cdot11MbssidMacAddrSupportEntry_Object = MibTableRow
cdot11MbssidMacAddrSupportEntry = _Cdot11MbssidMacAddrSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1)
)
cdot11MbssidMacAddrSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrIndex"),
)
if mibBuilder.loadTexts:
    cdot11MbssidMacAddrSupportEntry.setStatus("current")


class _Cdot11MbssidMacAddrIndex_Type(Integer32):
    """Custom type cdot11MbssidMacAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdot11MbssidMacAddrIndex_Type.__name__ = "Integer32"
_Cdot11MbssidMacAddrIndex_Object = MibTableColumn
cdot11MbssidMacAddrIndex = _Cdot11MbssidMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1, 1),
    _Cdot11MbssidMacAddrIndex_Type()
)
cdot11MbssidMacAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11MbssidMacAddrIndex.setStatus("current")
_Cdot11MbssidMacAddrSupported_Type = MacAddress
_Cdot11MbssidMacAddrSupported_Object = MibTableColumn
cdot11MbssidMacAddrSupported = _Cdot11MbssidMacAddrSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1, 2),
    _Cdot11MbssidMacAddrSupported_Type()
)
cdot11MbssidMacAddrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11MbssidMacAddrSupported.setStatus("current")
_Cdot11MbssidInterfaceTable_Object = MibTable
cdot11MbssidInterfaceTable = _Cdot11MbssidInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cdot11MbssidInterfaceTable.setStatus("current")
_Cdot11MbssidInterfaceEntry_Object = MibTableRow
cdot11MbssidInterfaceEntry = _Cdot11MbssidInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1)
)
cdot11MbssidInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"),
)
if mibBuilder.loadTexts:
    cdot11MbssidInterfaceEntry.setStatus("current")
_Cdot11MbssidIfMacAddress_Type = MacAddress
_Cdot11MbssidIfMacAddress_Object = MibTableColumn
cdot11MbssidIfMacAddress = _Cdot11MbssidIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1, 1),
    _Cdot11MbssidIfMacAddress_Type()
)
cdot11MbssidIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11MbssidIfMacAddress.setStatus("current")
_Cdot11MbssidIfBroadcast_Type = TruthValue
_Cdot11MbssidIfBroadcast_Object = MibTableColumn
cdot11MbssidIfBroadcast = _Cdot11MbssidIfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1, 2),
    _Cdot11MbssidIfBroadcast_Type()
)
cdot11MbssidIfBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdot11MbssidIfBroadcast.setStatus("current")


class _Cdot11SecSsidMaxBackupVlans_Type(Unsigned32):
    """Custom type cdot11SecSsidMaxBackupVlans based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdot11SecSsidMaxBackupVlans_Type.__name__ = "Unsigned32"
_Cdot11SecSsidMaxBackupVlans_Object = MibScalar
cdot11SecSsidMaxBackupVlans = _Cdot11SecSsidMaxBackupVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 6),
    _Cdot11SecSsidMaxBackupVlans_Type()
)
cdot11SecSsidMaxBackupVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecSsidMaxBackupVlans.setStatus("current")
_Cdot11SecSsidBackupVlanTable_Object = MibTable
cdot11SecSsidBackupVlanTable = _Cdot11SecSsidBackupVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdot11SecSsidBackupVlanTable.setStatus("current")
_Cdot11SecSsidBackupVlanEntry_Object = MibTableRow
cdot11SecSsidBackupVlanEntry = _Cdot11SecSsidBackupVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1)
)
cdot11SecSsidBackupVlanEntry.setIndexNames(
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"),
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidBackupVlan"),
)
if mibBuilder.loadTexts:
    cdot11SecSsidBackupVlanEntry.setStatus("current")


class _Cdot11SecSsidBackupVlan_Type(CDot11IfVlanIdOrZero):
    """Custom type cdot11SecSsidBackupVlan based on CDot11IfVlanIdOrZero"""
    subtypeSpec = CDot11IfVlanIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cdot11SecSsidBackupVlan_Type.__name__ = "CDot11IfVlanIdOrZero"
_Cdot11SecSsidBackupVlan_Object = MibTableColumn
cdot11SecSsidBackupVlan = _Cdot11SecSsidBackupVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1, 1),
    _Cdot11SecSsidBackupVlan_Type()
)
cdot11SecSsidBackupVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11SecSsidBackupVlan.setStatus("current")
_Cdot11SecSsidBackupVlanRowStatus_Type = RowStatus
_Cdot11SecSsidBackupVlanRowStatus_Object = MibTableColumn
cdot11SecSsidBackupVlanRowStatus = _Cdot11SecSsidBackupVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1, 2),
    _Cdot11SecSsidBackupVlanRowStatus_Type()
)
cdot11SecSsidBackupVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecSsidBackupVlanRowStatus.setStatus("current")
_Cdot11SecAuthManagement_ObjectIdentity = ObjectIdentity
cdot11SecAuthManagement = _Cdot11SecAuthManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 2)
)
_Cdot11SecLocalAuthServerEnabled_Type = TruthValue
_Cdot11SecLocalAuthServerEnabled_Object = MibScalar
cdot11SecLocalAuthServerEnabled = _Cdot11SecLocalAuthServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 2, 1),
    _Cdot11SecLocalAuthServerEnabled_Type()
)
cdot11SecLocalAuthServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdot11SecLocalAuthServerEnabled.setStatus("current")
_Cdot11SecStatistics_ObjectIdentity = ObjectIdentity
cdot11SecStatistics = _Cdot11SecStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 3)
)
_Cdot11SecVlanManagement_ObjectIdentity = ObjectIdentity
cdot11SecVlanManagement = _Cdot11SecVlanManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4)
)
_Cdot11SecVlanNameTable_Object = MibTable
cdot11SecVlanNameTable = _Cdot11SecVlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdot11SecVlanNameTable.setStatus("current")
_Cdot11SecVlanNameEntry_Object = MibTableRow
cdot11SecVlanNameEntry = _Cdot11SecVlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1)
)
cdot11SecVlanNameEntry.setIndexNames(
    (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanName"),
)
if mibBuilder.loadTexts:
    cdot11SecVlanNameEntry.setStatus("current")
_Cdot11SecVlanName_Type = CDot11VlanName
_Cdot11SecVlanName_Object = MibTableColumn
cdot11SecVlanName = _Cdot11SecVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 1),
    _Cdot11SecVlanName_Type()
)
cdot11SecVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdot11SecVlanName.setStatus("current")
_Cdot11SecVlanNameId_Type = CDot11IfVlanIdOrZero
_Cdot11SecVlanNameId_Object = MibTableColumn
cdot11SecVlanNameId = _Cdot11SecVlanNameId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 2),
    _Cdot11SecVlanNameId_Type()
)
cdot11SecVlanNameId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecVlanNameId.setStatus("current")
_Cdot11SecVlanNameRowStatus_Type = RowStatus
_Cdot11SecVlanNameRowStatus_Object = MibTableColumn
cdot11SecVlanNameRowStatus = _Cdot11SecVlanNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 3),
    _Cdot11SecVlanNameRowStatus_Type()
)
cdot11SecVlanNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdot11SecVlanNameRowStatus.setStatus("current")
_CiscoDot11SsidSecMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11SsidSecMIBConformance = _CiscoDot11SsidSecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2)
)
_CiscoDot11SsidSecMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11SsidSecMIBCompliances = _CiscoDot11SsidSecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1)
)
_CiscoDot11SsidSecMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11SsidSecMIBGroups = _CiscoDot11SsidSecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2)
)

# Managed Objects groups

cdot11SecSsidManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 1)
)
cdot11SecSsidManagementGroup.setObjects(
      *(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidBroadcast"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidInfraStruct"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidProxyMobileIp"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMaxStations"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidVlan"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidWpaPsk"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxRadiusAccounting"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidLoginUsername"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidLoginPassword"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthKeyMgmt"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthKeyMgmtOpt"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidRowStatus"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidWirelessNetId"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectAddrType"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectDestAddr"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectFilter"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidInformationElement"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidVlanName"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecInterfSsidRowStatus"))
)
if mibBuilder.loadTexts:
    cdot11SecSsidManagementGroup.setStatus("current")

cdot11SsidAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 2)
)
cdot11SsidAuthenticationGroup.setObjects(
      *(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthEnabled"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthPlusEap"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthPlusMac"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthEapMethod"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthMacMethod"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthMacAlternate"))
)
if mibBuilder.loadTexts:
    cdot11SsidAuthenticationGroup.setStatus("current")

cdot11ModuleAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 3)
)
cdot11ModuleAuthenticationGroup.setObjects(
    ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecLocalAuthServerEnabled")
)
if mibBuilder.loadTexts:
    cdot11ModuleAuthenticationGroup.setStatus("current")

cdot11SecVlanManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 4)
)
cdot11SecVlanManagementGroup.setObjects(
      *(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanNameId"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanNameRowStatus"))
)
if mibBuilder.loadTexts:
    cdot11SecVlanManagementGroup.setStatus("current")

cdot11MbssidSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 5)
)
cdot11MbssidSupportGroup.setObjects(
      *(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMbssidBroadcast"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMbssidDtimPeriod"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrIndex"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrSupported"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidIfMacAddress"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidIfBroadcast"))
)
if mibBuilder.loadTexts:
    cdot11MbssidSupportGroup.setStatus("current")

cdot11SecSsidBackupVlanManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 6)
)
cdot11SecSsidBackupVlanManagementGroup.setObjects(
      *(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidBackupVlanRowStatus"),
        ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidMaxBackupVlans"))
)
if mibBuilder.loadTexts:
    cdot11SecSsidBackupVlanManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11SsidSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11SsidSecCompliance.setStatus(
        "deprecated"
    )

ciscoDot11SsidSecComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDot11SsidSecComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-SSID-SECURITY-MIB",
    **{"CDot11SecAuthKeyMgmtType": CDot11SecAuthKeyMgmtType,
       "CDot11WiFiPaPreSharedKey": CDot11WiFiPaPreSharedKey,
       "CDot11SsidString": CDot11SsidString,
       "CDot11VlanName": CDot11VlanName,
       "CDot11InformationElementType": CDot11InformationElementType,
       "ciscoDot11SsidSecMIB": ciscoDot11SsidSecMIB,
       "ciscoDot11SsidSecMIBObjects": ciscoDot11SsidSecMIBObjects,
       "cdot11SecSsidManagement": cdot11SecSsidManagement,
       "cdot11SecAuxSsidTable": cdot11SecAuxSsidTable,
       "cdot11SecAuxSsidEntry": cdot11SecAuxSsidEntry,
       "cdot11SecAuxSsid": cdot11SecAuxSsid,
       "cdot11SecAuxSsidBroadcast": cdot11SecAuxSsidBroadcast,
       "cdot11SecAuxSsidInfraStruct": cdot11SecAuxSsidInfraStruct,
       "cdot11SecAuxSsidProxyMobileIp": cdot11SecAuxSsidProxyMobileIp,
       "cdot11SecAuxSsidMaxStations": cdot11SecAuxSsidMaxStations,
       "cdot11SecAuxSsidVlan": cdot11SecAuxSsidVlan,
       "cdot11SecAuxSsidWpaPsk": cdot11SecAuxSsidWpaPsk,
       "cdot11SecAuxRadiusAccounting": cdot11SecAuxRadiusAccounting,
       "cdot11SecAuxSsidLoginUsername": cdot11SecAuxSsidLoginUsername,
       "cdot11SecAuxSsidLoginPassword": cdot11SecAuxSsidLoginPassword,
       "cdot11SecAuxSsidAuthKeyMgmt": cdot11SecAuxSsidAuthKeyMgmt,
       "cdot11SecAuxSsidAuthKeyMgmtOpt": cdot11SecAuxSsidAuthKeyMgmtOpt,
       "cdot11SecAuxSsidRowStatus": cdot11SecAuxSsidRowStatus,
       "cdot11SecAuxSsidWirelessNetId": cdot11SecAuxSsidWirelessNetId,
       "cdot11SecSsidRedirectAddrType": cdot11SecSsidRedirectAddrType,
       "cdot11SecSsidRedirectDestAddr": cdot11SecSsidRedirectDestAddr,
       "cdot11SecSsidRedirectFilter": cdot11SecSsidRedirectFilter,
       "cdot11SecSsidInformationElement": cdot11SecSsidInformationElement,
       "cdot11SecAuxSsidVlanName": cdot11SecAuxSsidVlanName,
       "cdot11SecAuxSsidMbssidBroadcast": cdot11SecAuxSsidMbssidBroadcast,
       "cdot11SecAuxSsidMbssidDtimPeriod": cdot11SecAuxSsidMbssidDtimPeriod,
       "cdot11SecAuxSsidAuthTable": cdot11SecAuxSsidAuthTable,
       "cdot11SecAuxSsidAuthEntry": cdot11SecAuxSsidAuthEntry,
       "cdot11SecAuxSsidAuthEnabled": cdot11SecAuxSsidAuthEnabled,
       "cdot11SecAuxSsidAuthPlusEap": cdot11SecAuxSsidAuthPlusEap,
       "cdot11SecAuxSsidAuthPlusMac": cdot11SecAuxSsidAuthPlusMac,
       "cdot11SecAuxSsidAuthEapMethod": cdot11SecAuxSsidAuthEapMethod,
       "cdot11SecAuxSsidAuthMacMethod": cdot11SecAuxSsidAuthMacMethod,
       "cdot11SecAuxSsidAuthMacAlternate": cdot11SecAuxSsidAuthMacAlternate,
       "cdot11SecInterfSsidTable": cdot11SecInterfSsidTable,
       "cdot11SecInterfSsidEntry": cdot11SecInterfSsidEntry,
       "cdot11SecInterfSsidRowStatus": cdot11SecInterfSsidRowStatus,
       "cdot11MbssidMacAddrSupportTable": cdot11MbssidMacAddrSupportTable,
       "cdot11MbssidMacAddrSupportEntry": cdot11MbssidMacAddrSupportEntry,
       "cdot11MbssidMacAddrIndex": cdot11MbssidMacAddrIndex,
       "cdot11MbssidMacAddrSupported": cdot11MbssidMacAddrSupported,
       "cdot11MbssidInterfaceTable": cdot11MbssidInterfaceTable,
       "cdot11MbssidInterfaceEntry": cdot11MbssidInterfaceEntry,
       "cdot11MbssidIfMacAddress": cdot11MbssidIfMacAddress,
       "cdot11MbssidIfBroadcast": cdot11MbssidIfBroadcast,
       "cdot11SecSsidMaxBackupVlans": cdot11SecSsidMaxBackupVlans,
       "cdot11SecSsidBackupVlanTable": cdot11SecSsidBackupVlanTable,
       "cdot11SecSsidBackupVlanEntry": cdot11SecSsidBackupVlanEntry,
       "cdot11SecSsidBackupVlan": cdot11SecSsidBackupVlan,
       "cdot11SecSsidBackupVlanRowStatus": cdot11SecSsidBackupVlanRowStatus,
       "cdot11SecAuthManagement": cdot11SecAuthManagement,
       "cdot11SecLocalAuthServerEnabled": cdot11SecLocalAuthServerEnabled,
       "cdot11SecStatistics": cdot11SecStatistics,
       "cdot11SecVlanManagement": cdot11SecVlanManagement,
       "cdot11SecVlanNameTable": cdot11SecVlanNameTable,
       "cdot11SecVlanNameEntry": cdot11SecVlanNameEntry,
       "cdot11SecVlanName": cdot11SecVlanName,
       "cdot11SecVlanNameId": cdot11SecVlanNameId,
       "cdot11SecVlanNameRowStatus": cdot11SecVlanNameRowStatus,
       "ciscoDot11SsidSecMIBConformance": ciscoDot11SsidSecMIBConformance,
       "ciscoDot11SsidSecMIBCompliances": ciscoDot11SsidSecMIBCompliances,
       "ciscoDot11SsidSecCompliance": ciscoDot11SsidSecCompliance,
       "ciscoDot11SsidSecComplianceRev1": ciscoDot11SsidSecComplianceRev1,
       "ciscoDot11SsidSecMIBGroups": ciscoDot11SsidSecMIBGroups,
       "cdot11SecSsidManagementGroup": cdot11SecSsidManagementGroup,
       "cdot11SsidAuthenticationGroup": cdot11SsidAuthenticationGroup,
       "cdot11ModuleAuthenticationGroup": cdot11ModuleAuthenticationGroup,
       "cdot11SecVlanManagementGroup": cdot11SecVlanManagementGroup,
       "cdot11MbssidSupportGroup": cdot11MbssidSupportGroup,
       "cdot11SecSsidBackupVlanManagementGroup": cdot11SecSsidBackupVlanManagementGroup}
)
