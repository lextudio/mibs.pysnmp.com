# SNMP MIB module (CISCO-WDS-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WDS-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:33 2024
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

(CDot11SecAuthKeyMgmtType,
 CDot11SsidString) = mibBuilder.importSymbols(
    "CISCO-DOT11-SSID-SECURITY-MIB",
    "CDot11SecAuthKeyMgmtType",
    "CDot11SsidString")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoWdsInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509)
)
ciscoWdsInfoMIB.setRevisions(
        ("2005-09-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CWdsClientTrackingStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 3),
          ("inactive", 2))
    )



class CWdsDeviceAuthType(Bits, TextualConvention):
    status = "current"


class CWdsDeviceState(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("authFailed", 4),
          ("authInProgress", 3),
          ("authenticated", 5),
          ("detached", 8),
          ("initial", 2),
          ("registered", 7),
          ("securityKeysSetup", 6),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWdsInfoMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMIBNotifs = _CiscoWdsInfoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 0)
)
_CiscoWdsInfoMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMIBObjects = _CiscoWdsInfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1)
)
_CiscoWdsInfoMacAuthCache_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMacAuthCache = _CiscoWdsInfoMacAuthCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1)
)
_CwdsiMacAuthCacheTable_Object = MibTable
cwdsiMacAuthCacheTable = _CwdsiMacAuthCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwdsiMacAuthCacheTable.setStatus("current")
_CwdsiMacAuthCacheEntry_Object = MibTableRow
cwdsiMacAuthCacheEntry = _CwdsiMacAuthCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1)
)
cwdsiMacAuthCacheEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiMacAuthCacheMacAddr"),
)
if mibBuilder.loadTexts:
    cwdsiMacAuthCacheEntry.setStatus("current")
_CwdsiMacAuthCacheMacAddr_Type = MacAddress
_CwdsiMacAuthCacheMacAddr_Object = MibTableColumn
cwdsiMacAuthCacheMacAddr = _CwdsiMacAuthCacheMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1, 1),
    _CwdsiMacAuthCacheMacAddr_Type()
)
cwdsiMacAuthCacheMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiMacAuthCacheMacAddr.setStatus("current")
_CwdsiMacAuthCacheAge_Type = Unsigned32
_CwdsiMacAuthCacheAge_Object = MibTableColumn
cwdsiMacAuthCacheAge = _CwdsiMacAuthCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1, 2),
    _CwdsiMacAuthCacheAge_Type()
)
cwdsiMacAuthCacheAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMacAuthCacheAge.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiMacAuthCacheAge.setUnits("minutes")
_CiscoWdsInfoAccessPoint_ObjectIdentity = ObjectIdentity
ciscoWdsInfoAccessPoint = _CiscoWdsInfoAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2)
)
_CwdsiApTable_Object = MibTable
cwdsiApTable = _CwdsiApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwdsiApTable.setStatus("current")
_CwdsiApEntry_Object = MibTableRow
cwdsiApEntry = _CwdsiApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1)
)
cwdsiApEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiApMacAddr"),
)
if mibBuilder.loadTexts:
    cwdsiApEntry.setStatus("current")
_CwdsiApMacAddr_Type = MacAddress
_CwdsiApMacAddr_Object = MibTableColumn
cwdsiApMacAddr = _CwdsiApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 1),
    _CwdsiApMacAddr_Type()
)
cwdsiApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiApMacAddr.setStatus("current")
_CwdsiApAddrType_Type = InetAddressType
_CwdsiApAddrType_Object = MibTableColumn
cwdsiApAddrType = _CwdsiApAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 2),
    _CwdsiApAddrType_Type()
)
cwdsiApAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApAddrType.setStatus("current")
_CwdsiApAddr_Type = InetAddress
_CwdsiApAddr_Object = MibTableColumn
cwdsiApAddr = _CwdsiApAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 3),
    _CwdsiApAddr_Type()
)
cwdsiApAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApAddr.setStatus("current")
_CwdsiApName_Type = SnmpAdminString
_CwdsiApName_Object = MibTableColumn
cwdsiApName = _CwdsiApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 4),
    _CwdsiApName_Type()
)
cwdsiApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApName.setStatus("current")
_CwdsiApState_Type = CWdsDeviceState
_CwdsiApState_Object = MibTableColumn
cwdsiApState = _CwdsiApState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 5),
    _CwdsiApState_Type()
)
cwdsiApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApState.setStatus("current")
_CwdsiApLifeTime_Type = Unsigned32
_CwdsiApLifeTime_Object = MibTableColumn
cwdsiApLifeTime = _CwdsiApLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 6),
    _CwdsiApLifeTime_Type()
)
cwdsiApLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiApLifeTime.setUnits("seconds")
_CwdsiApNeighborAddrType_Type = InetAddressType
_CwdsiApNeighborAddrType_Object = MibTableColumn
cwdsiApNeighborAddrType = _CwdsiApNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 7),
    _CwdsiApNeighborAddrType_Type()
)
cwdsiApNeighborAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApNeighborAddrType.setStatus("current")
_CwdsiApNeighborAddr_Type = InetAddress
_CwdsiApNeighborAddr_Object = MibTableColumn
cwdsiApNeighborAddr = _CwdsiApNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 8),
    _CwdsiApNeighborAddr_Type()
)
cwdsiApNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApNeighborAddr.setStatus("current")
_CwdsiApNeighborName_Type = SnmpAdminString
_CwdsiApNeighborName_Object = MibTableColumn
cwdsiApNeighborName = _CwdsiApNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 9),
    _CwdsiApNeighborName_Type()
)
cwdsiApNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApNeighborName.setStatus("current")
_CwdsiApNeighborPortName_Type = SnmpAdminString
_CwdsiApNeighborPortName_Object = MibTableColumn
cwdsiApNeighborPortName = _CwdsiApNeighborPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 10),
    _CwdsiApNeighborPortName_Type()
)
cwdsiApNeighborPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApNeighborPortName.setStatus("current")
_CiscoWdsInfoMobileNode_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMobileNode = _CiscoWdsInfoMobileNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3)
)
_CwdsiMnTable_Object = MibTable
cwdsiMnTable = _CwdsiMnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwdsiMnTable.setStatus("current")
_CwdsiMnEntry_Object = MibTableRow
cwdsiMnEntry = _CwdsiMnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1)
)
cwdsiMnEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiMnMacAddr"),
)
if mibBuilder.loadTexts:
    cwdsiMnEntry.setStatus("current")
_CwdsiMnMacAddr_Type = MacAddress
_CwdsiMnMacAddr_Object = MibTableColumn
cwdsiMnMacAddr = _CwdsiMnMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 1),
    _CwdsiMnMacAddr_Type()
)
cwdsiMnMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiMnMacAddr.setStatus("current")
_CwdsiMnAddrType_Type = InetAddressType
_CwdsiMnAddrType_Object = MibTableColumn
cwdsiMnAddrType = _CwdsiMnAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 2),
    _CwdsiMnAddrType_Type()
)
cwdsiMnAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnAddrType.setStatus("current")
_CwdsiMnAddr_Type = InetAddress
_CwdsiMnAddr_Object = MibTableColumn
cwdsiMnAddr = _CwdsiMnAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 3),
    _CwdsiMnAddr_Type()
)
cwdsiMnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnAddr.setStatus("current")
_CwdsiMnApMacAddr_Type = MacAddress
_CwdsiMnApMacAddr_Object = MibTableColumn
cwdsiMnApMacAddr = _CwdsiMnApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 4),
    _CwdsiMnApMacAddr_Type()
)
cwdsiMnApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnApMacAddr.setStatus("current")
_CwdsiMnApAddrType_Type = InetAddressType
_CwdsiMnApAddrType_Object = MibTableColumn
cwdsiMnApAddrType = _CwdsiMnApAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 5),
    _CwdsiMnApAddrType_Type()
)
cwdsiMnApAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnApAddrType.setStatus("current")
_CwdsiMnApAddr_Type = InetAddress
_CwdsiMnApAddr_Object = MibTableColumn
cwdsiMnApAddr = _CwdsiMnApAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 6),
    _CwdsiMnApAddr_Type()
)
cwdsiMnApAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnApAddr.setStatus("current")


class _CwdsiMnMobilityNetworkId_Type(Unsigned32):
    """Custom type cwdsiMnMobilityNetworkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CwdsiMnMobilityNetworkId_Type.__name__ = "Unsigned32"
_CwdsiMnMobilityNetworkId_Object = MibTableColumn
cwdsiMnMobilityNetworkId = _CwdsiMnMobilityNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 7),
    _CwdsiMnMobilityNetworkId_Type()
)
cwdsiMnMobilityNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnMobilityNetworkId.setStatus("current")
_CwdsiMnState_Type = CWdsDeviceState
_CwdsiMnState_Object = MibTableColumn
cwdsiMnState = _CwdsiMnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 8),
    _CwdsiMnState_Type()
)
cwdsiMnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnState.setStatus("current")
_CwdsiMnSsid_Type = CDot11SsidString
_CwdsiMnSsid_Object = MibTableColumn
cwdsiMnSsid = _CwdsiMnSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 9),
    _CwdsiMnSsid_Type()
)
cwdsiMnSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnSsid.setStatus("current")
_CwdsiMnBssid_Type = MacAddress
_CwdsiMnBssid_Object = MibTableColumn
cwdsiMnBssid = _CwdsiMnBssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 10),
    _CwdsiMnBssid_Type()
)
cwdsiMnBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnBssid.setStatus("current")
_CwdsiMnVlan_Type = CDot11IfVlanIdOrZero
_CwdsiMnVlan_Object = MibTableColumn
cwdsiMnVlan = _CwdsiMnVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 11),
    _CwdsiMnVlan_Type()
)
cwdsiMnVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnVlan.setStatus("current")
_CwdsiMnKeyMgmt_Type = CDot11SecAuthKeyMgmtType
_CwdsiMnKeyMgmt_Object = MibTableColumn
cwdsiMnKeyMgmt = _CwdsiMnKeyMgmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 12),
    _CwdsiMnKeyMgmt_Type()
)
cwdsiMnKeyMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnKeyMgmt.setStatus("current")
_CwdsiMnAuthType_Type = CWdsDeviceAuthType
_CwdsiMnAuthType_Object = MibTableColumn
cwdsiMnAuthType = _CwdsiMnAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 13),
    _CwdsiMnAuthType_Type()
)
cwdsiMnAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnAuthType.setStatus("current")
_CwdsiMnUptime_Type = TimeStamp
_CwdsiMnUptime_Object = MibTableColumn
cwdsiMnUptime = _CwdsiMnUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 14),
    _CwdsiMnUptime_Type()
)
cwdsiMnUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnUptime.setStatus("current")
_CwdsiMnLifetime_Type = Unsigned32
_CwdsiMnLifetime_Object = MibTableColumn
cwdsiMnLifetime = _CwdsiMnLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 15),
    _CwdsiMnLifetime_Type()
)
cwdsiMnLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiMnLifetime.setUnits("seconds")
_CiscoWdsInfoNetworkManager_ObjectIdentity = ObjectIdentity
ciscoWdsInfoNetworkManager = _CiscoWdsInfoNetworkManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4)
)
_CwdsiWnmTable_Object = MibTable
cwdsiWnmTable = _CwdsiWnmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwdsiWnmTable.setStatus("current")
_CwdsiWnmEntry_Object = MibTableRow
cwdsiWnmEntry = _CwdsiWnmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1)
)
cwdsiWnmEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiWnmAddrType"),
    (0, "CISCO-WDS-INFO-MIB", "cwdsiWnmAddr"),
)
if mibBuilder.loadTexts:
    cwdsiWnmEntry.setStatus("current")
_CwdsiWnmAddrType_Type = InetAddressType
_CwdsiWnmAddrType_Object = MibTableColumn
cwdsiWnmAddrType = _CwdsiWnmAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 1),
    _CwdsiWnmAddrType_Type()
)
cwdsiWnmAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiWnmAddrType.setStatus("current")


class _CwdsiWnmAddr_Type(InetAddress):
    """Custom type cwdsiWnmAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CwdsiWnmAddr_Type.__name__ = "InetAddress"
_CwdsiWnmAddr_Object = MibTableColumn
cwdsiWnmAddr = _CwdsiWnmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 2),
    _CwdsiWnmAddr_Type()
)
cwdsiWnmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiWnmAddr.setStatus("current")
_CwdsiWnmState_Type = CWdsDeviceState
_CwdsiWnmState_Object = MibTableColumn
cwdsiWnmState = _CwdsiWnmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 3),
    _CwdsiWnmState_Type()
)
cwdsiWnmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmState.setStatus("current")


class _CwdsiWnmLinkStatus_Type(Integer32):
    """Custom type cwdsiWnmLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CwdsiWnmLinkStatus_Type.__name__ = "Integer32"
_CwdsiWnmLinkStatus_Object = MibTableColumn
cwdsiWnmLinkStatus = _CwdsiWnmLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 4),
    _CwdsiWnmLinkStatus_Type()
)
cwdsiWnmLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmLinkStatus.setStatus("current")
_CwdsiWnmClientTracking_Type = CWdsClientTrackingStatus
_CwdsiWnmClientTracking_Object = MibTableColumn
cwdsiWnmClientTracking = _CwdsiWnmClientTracking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 5),
    _CwdsiWnmClientTracking_Type()
)
cwdsiWnmClientTracking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmClientTracking.setStatus("current")
_CwdsiWnmReqMsgCount_Type = Counter32
_CwdsiWnmReqMsgCount_Object = MibTableColumn
cwdsiWnmReqMsgCount = _CwdsiWnmReqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 6),
    _CwdsiWnmReqMsgCount_Type()
)
cwdsiWnmReqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmReqMsgCount.setStatus("current")
_CwdsiWnmSentMsgCount_Type = Counter32
_CwdsiWnmSentMsgCount_Object = MibTableColumn
cwdsiWnmSentMsgCount = _CwdsiWnmSentMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 7),
    _CwdsiWnmSentMsgCount_Type()
)
cwdsiWnmSentMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmSentMsgCount.setStatus("current")
_CwdsiWnmRetryTxMsgCount_Type = Counter32
_CwdsiWnmRetryTxMsgCount_Object = MibTableColumn
cwdsiWnmRetryTxMsgCount = _CwdsiWnmRetryTxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 8),
    _CwdsiWnmRetryTxMsgCount_Type()
)
cwdsiWnmRetryTxMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmRetryTxMsgCount.setStatus("current")
_CwdsiWnmWaitingAckMsgCount_Type = Counter32
_CwdsiWnmWaitingAckMsgCount_Object = MibTableColumn
cwdsiWnmWaitingAckMsgCount = _CwdsiWnmWaitingAckMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 9),
    _CwdsiWnmWaitingAckMsgCount_Type()
)
cwdsiWnmWaitingAckMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmWaitingAckMsgCount.setStatus("current")
_CwdsiWnmDropMicTxMsgCount_Type = Counter32
_CwdsiWnmDropMicTxMsgCount_Object = MibTableColumn
cwdsiWnmDropMicTxMsgCount = _CwdsiWnmDropMicTxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 10),
    _CwdsiWnmDropMicTxMsgCount_Type()
)
cwdsiWnmDropMicTxMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmDropMicTxMsgCount.setStatus("current")
_CwdsiWnmDropUmdTxMsgCount_Type = Counter32
_CwdsiWnmDropUmdTxMsgCount_Object = MibTableColumn
cwdsiWnmDropUmdTxMsgCount = _CwdsiWnmDropUmdTxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 11),
    _CwdsiWnmDropUmdTxMsgCount_Type()
)
cwdsiWnmDropUmdTxMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmDropUmdTxMsgCount.setStatus("current")
_CwdsiWnmIndicatedMsgCount_Type = Counter32
_CwdsiWnmIndicatedMsgCount_Object = MibTableColumn
cwdsiWnmIndicatedMsgCount = _CwdsiWnmIndicatedMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 12),
    _CwdsiWnmIndicatedMsgCount_Type()
)
cwdsiWnmIndicatedMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmIndicatedMsgCount.setStatus("current")
_CwdsiWnmRxMsgCount_Type = Counter32
_CwdsiWnmRxMsgCount_Object = MibTableColumn
cwdsiWnmRxMsgCount = _CwdsiWnmRxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 13),
    _CwdsiWnmRxMsgCount_Type()
)
cwdsiWnmRxMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmRxMsgCount.setStatus("current")
_CwdsiWnmDropRxMsgCount_Type = Counter32
_CwdsiWnmDropRxMsgCount_Object = MibTableColumn
cwdsiWnmDropRxMsgCount = _CwdsiWnmDropRxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 14),
    _CwdsiWnmDropRxMsgCount_Type()
)
cwdsiWnmDropRxMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmDropRxMsgCount.setStatus("current")
_CwdsiWnmDiscontinuityTime_Type = TimeStamp
_CwdsiWnmDiscontinuityTime_Object = MibTableColumn
cwdsiWnmDiscontinuityTime = _CwdsiWnmDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 15),
    _CwdsiWnmDiscontinuityTime_Type()
)
cwdsiWnmDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWnmDiscontinuityTime.setStatus("current")
_CiscoWdsInfoStatistics_ObjectIdentity = ObjectIdentity
ciscoWdsInfoStatistics = _CiscoWdsInfoStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5)
)
_CwdsiApNum_Type = Gauge32
_CwdsiApNum_Object = MibScalar
cwdsiApNum = _CwdsiApNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 1),
    _CwdsiApNum_Type()
)
cwdsiApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiApNum.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiApNum.setUnits("access-points")
_CwdsiMnNum_Type = Gauge32
_CwdsiMnNum_Object = MibScalar
cwdsiMnNum = _CwdsiMnNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 2),
    _CwdsiMnNum_Type()
)
cwdsiMnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMnNum.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiMnNum.setUnits("mobile-nodes")
_CwdsiAaaAuthAttemptCount_Type = Counter32
_CwdsiAaaAuthAttemptCount_Object = MibScalar
cwdsiAaaAuthAttemptCount = _CwdsiAaaAuthAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 3),
    _CwdsiAaaAuthAttemptCount_Type()
)
cwdsiAaaAuthAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiAaaAuthAttemptCount.setStatus("current")
_CwdsiAaaAuthSuccessCount_Type = Counter32
_CwdsiAaaAuthSuccessCount_Object = MibScalar
cwdsiAaaAuthSuccessCount = _CwdsiAaaAuthSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 4),
    _CwdsiAaaAuthSuccessCount_Type()
)
cwdsiAaaAuthSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiAaaAuthSuccessCount.setStatus("current")
_CwdsiAaaAuthFailureCount_Type = Counter32
_CwdsiAaaAuthFailureCount_Object = MibScalar
cwdsiAaaAuthFailureCount = _CwdsiAaaAuthFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 5),
    _CwdsiAaaAuthFailureCount_Type()
)
cwdsiAaaAuthFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiAaaAuthFailureCount.setStatus("current")
_CwdsiMacSpoofingBlockCount_Type = Counter32
_CwdsiMacSpoofingBlockCount_Object = MibScalar
cwdsiMacSpoofingBlockCount = _CwdsiMacSpoofingBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 6),
    _CwdsiMacSpoofingBlockCount_Type()
)
cwdsiMacSpoofingBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMacSpoofingBlockCount.setStatus("current")
_CwdsiRoamsWithoutAaaAuthCount_Type = Counter32
_CwdsiRoamsWithoutAaaAuthCount_Object = MibScalar
cwdsiRoamsWithoutAaaAuthCount = _CwdsiRoamsWithoutAaaAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 7),
    _CwdsiRoamsWithoutAaaAuthCount_Type()
)
cwdsiRoamsWithoutAaaAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamsWithoutAaaAuthCount.setStatus("current")
_CwdsiRoamsWithFullAaaAuthCount_Type = Counter32
_CwdsiRoamsWithFullAaaAuthCount_Object = MibScalar
cwdsiRoamsWithFullAaaAuthCount = _CwdsiRoamsWithFullAaaAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 8),
    _CwdsiRoamsWithFullAaaAuthCount_Type()
)
cwdsiRoamsWithFullAaaAuthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamsWithFullAaaAuthCount.setStatus("current")
_CwdsiRoamsFastSecuredCount_Type = Counter32
_CwdsiRoamsFastSecuredCount_Object = MibScalar
cwdsiRoamsFastSecuredCount = _CwdsiRoamsFastSecuredCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 9),
    _CwdsiRoamsFastSecuredCount_Type()
)
cwdsiRoamsFastSecuredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamsFastSecuredCount.setStatus("current")
_CwdsiMscMismatchCount_Type = Counter32
_CwdsiMscMismatchCount_Object = MibScalar
cwdsiMscMismatchCount = _CwdsiMscMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 10),
    _CwdsiMscMismatchCount_Type()
)
cwdsiMscMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMscMismatchCount.setStatus("current")
_CwdsiKscFailureCount_Type = Counter32
_CwdsiKscFailureCount_Object = MibScalar
cwdsiKscFailureCount = _CwdsiKscFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 11),
    _CwdsiKscFailureCount_Type()
)
cwdsiKscFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiKscFailureCount.setStatus("current")
_CwdsiMicFailureCount_Type = Counter32
_CwdsiMicFailureCount_Object = MibScalar
cwdsiMicFailureCount = _CwdsiMicFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 12),
    _CwdsiMicFailureCount_Type()
)
cwdsiMicFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMicFailureCount.setStatus("current")
_CwdsiRnMismatchCount_Type = Counter32
_CwdsiRnMismatchCount_Object = MibScalar
cwdsiRnMismatchCount = _CwdsiRnMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 13),
    _CwdsiRnMismatchCount_Type()
)
cwdsiRnMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRnMismatchCount.setStatus("current")
_CiscoWdsInfoMobility_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMobility = _CiscoWdsInfoMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6)
)


class _CwdsiLcpStatus_Type(Integer32):
    """Custom type cwdsiLcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("inTransition", 3),
          ("up", 2))
    )


_CwdsiLcpStatus_Type.__name__ = "Integer32"
_CwdsiLcpStatus_Object = MibScalar
cwdsiLcpStatus = _CwdsiLcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 1),
    _CwdsiLcpStatus_Type()
)
cwdsiLcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiLcpStatus.setStatus("current")
_CwdsiCsMgmtAddrType_Type = InetAddressType
_CwdsiCsMgmtAddrType_Object = MibScalar
cwdsiCsMgmtAddrType = _CwdsiCsMgmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 2),
    _CwdsiCsMgmtAddrType_Type()
)
cwdsiCsMgmtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiCsMgmtAddrType.setStatus("current")


class _CwdsiCsMgmtAddr_Type(InetAddress):
    """Custom type cwdsiCsMgmtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CwdsiCsMgmtAddr_Type.__name__ = "InetAddress"
_CwdsiCsMgmtAddr_Object = MibScalar
cwdsiCsMgmtAddr = _CwdsiCsMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 3),
    _CwdsiCsMgmtAddr_Type()
)
cwdsiCsMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiCsMgmtAddr.setStatus("current")
_CwdsiWdsAddrType_Type = InetAddressType
_CwdsiWdsAddrType_Object = MibScalar
cwdsiWdsAddrType = _CwdsiWdsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 4),
    _CwdsiWdsAddrType_Type()
)
cwdsiWdsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWdsAddrType.setStatus("current")


class _CwdsiWdsAddr_Type(InetAddress):
    """Custom type cwdsiWdsAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CwdsiWdsAddr_Type.__name__ = "InetAddress"
_CwdsiWdsAddr_Object = MibScalar
cwdsiWdsAddr = _CwdsiWdsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 5),
    _CwdsiWdsAddr_Type()
)
cwdsiWdsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWdsAddr.setStatus("current")
_CwdsiWdsHsrpVirtualAddrType_Type = InetAddressType
_CwdsiWdsHsrpVirtualAddrType_Object = MibScalar
cwdsiWdsHsrpVirtualAddrType = _CwdsiWdsHsrpVirtualAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 6),
    _CwdsiWdsHsrpVirtualAddrType_Type()
)
cwdsiWdsHsrpVirtualAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWdsHsrpVirtualAddrType.setStatus("current")


class _CwdsiWdsHsrpVirtualAddr_Type(InetAddress):
    """Custom type cwdsiWdsHsrpVirtualAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CwdsiWdsHsrpVirtualAddr_Type.__name__ = "InetAddress"
_CwdsiWdsHsrpVirtualAddr_Object = MibScalar
cwdsiWdsHsrpVirtualAddr = _CwdsiWdsHsrpVirtualAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 7),
    _CwdsiWdsHsrpVirtualAddr_Type()
)
cwdsiWdsHsrpVirtualAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiWdsHsrpVirtualAddr.setStatus("current")


class _CwdsiHsrpState_Type(Integer32):
    """Custom type cwdsiHsrpState based on Integer32"""
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
        *(("active", 8),
          ("backup", 5),
          ("disabled", 2),
          ("initial", 3),
          ("learn", 4),
          ("speak", 6),
          ("standby", 7),
          ("unknown", 1))
    )


_CwdsiHsrpState_Type.__name__ = "Integer32"
_CwdsiHsrpState_Object = MibScalar
cwdsiHsrpState = _CwdsiHsrpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 8),
    _CwdsiHsrpState_Type()
)
cwdsiHsrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiHsrpState.setStatus("current")
_CwdsiMobilityGroupTable_Object = MibTable
cwdsiMobilityGroupTable = _CwdsiMobilityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9)
)
if mibBuilder.loadTexts:
    cwdsiMobilityGroupTable.setStatus("current")
_CwdsiMobilityGroupEntry_Object = MibTableRow
cwdsiMobilityGroupEntry = _CwdsiMobilityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1)
)
cwdsiMobilityGroupEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpNetworkId"),
)
if mibBuilder.loadTexts:
    cwdsiMobilityGroupEntry.setStatus("current")
_CwdsiMobilityGrpNetworkId_Type = Unsigned32
_CwdsiMobilityGrpNetworkId_Object = MibTableColumn
cwdsiMobilityGrpNetworkId = _CwdsiMobilityGrpNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 1),
    _CwdsiMobilityGrpNetworkId_Type()
)
cwdsiMobilityGrpNetworkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpNetworkId.setStatus("current")
_CwdsiMobilityGrpTunnelAddrType_Type = InetAddressType
_CwdsiMobilityGrpTunnelAddrType_Object = MibTableColumn
cwdsiMobilityGrpTunnelAddrType = _CwdsiMobilityGrpTunnelAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 2),
    _CwdsiMobilityGrpTunnelAddrType_Type()
)
cwdsiMobilityGrpTunnelAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpTunnelAddrType.setStatus("current")
_CwdsiMobilityGrpTunnelAddr_Type = InetAddress
_CwdsiMobilityGrpTunnelAddr_Object = MibTableColumn
cwdsiMobilityGrpTunnelAddr = _CwdsiMobilityGrpTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 3),
    _CwdsiMobilityGrpTunnelAddr_Type()
)
cwdsiMobilityGrpTunnelAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpTunnelAddr.setStatus("current")
_CwdsiMobilityGrpTunnelMtu_Type = Unsigned32
_CwdsiMobilityGrpTunnelMtu_Object = MibTableColumn
cwdsiMobilityGrpTunnelMtu = _CwdsiMobilityGrpTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 4),
    _CwdsiMobilityGrpTunnelMtu_Type()
)
cwdsiMobilityGrpTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpTunnelMtu.setStatus("current")


class _CwdsiMobilityGrpFlags_Type(Bits):
    """Custom type cwdsiMobilityGrpFlags based on Bits"""
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("dynamic", 4),
          ("ipDiscovery", 6),
          ("multicast", 5),
          ("none", 0),
          ("tcpMssAdjust", 3),
          ("trusted", 1))
    )

_CwdsiMobilityGrpFlags_Type.__name__ = "Bits"
_CwdsiMobilityGrpFlags_Object = MibTableColumn
cwdsiMobilityGrpFlags = _CwdsiMobilityGrpFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 5),
    _CwdsiMobilityGrpFlags_Type()
)
cwdsiMobilityGrpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpFlags.setStatus("current")
_CwdsiMobilityGrpMnNum_Type = Gauge32
_CwdsiMobilityGrpMnNum_Object = MibTableColumn
cwdsiMobilityGrpMnNum = _CwdsiMobilityGrpMnNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 6),
    _CwdsiMobilityGrpMnNum_Type()
)
cwdsiMobilityGrpMnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpMnNum.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiMobilityGrpMnNum.setUnits("mobile-nodes")
_CiscoWdsInfoRoamStatistics_ObjectIdentity = ObjectIdentity
ciscoWdsInfoRoamStatistics = _CiscoWdsInfoRoamStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7)
)
_CwdsiRoamStatsStartTime_Type = DateAndTime
_CwdsiRoamStatsStartTime_Object = MibScalar
cwdsiRoamStatsStartTime = _CwdsiRoamStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 1),
    _CwdsiRoamStatsStartTime_Type()
)
cwdsiRoamStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamStatsStartTime.setStatus("current")
_CwdsiRoamStatsAvgFiveSeconds_Type = Gauge32
_CwdsiRoamStatsAvgFiveSeconds_Object = MibScalar
cwdsiRoamStatsAvgFiveSeconds = _CwdsiRoamStatsAvgFiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 2),
    _CwdsiRoamStatsAvgFiveSeconds_Type()
)
cwdsiRoamStatsAvgFiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgFiveSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgFiveSeconds.setUnits("roams-per-second")
_CwdsiRoamStatsAvgOneMinute_Type = Gauge32
_CwdsiRoamStatsAvgOneMinute_Object = MibScalar
cwdsiRoamStatsAvgOneMinute = _CwdsiRoamStatsAvgOneMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 3),
    _CwdsiRoamStatsAvgOneMinute_Type()
)
cwdsiRoamStatsAvgOneMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgOneMinute.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgOneMinute.setUnits("roams-per-second")
_CwdsiRoamStatsAvgFiveMinutes_Type = Gauge32
_CwdsiRoamStatsAvgFiveMinutes_Object = MibScalar
cwdsiRoamStatsAvgFiveMinutes = _CwdsiRoamStatsAvgFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 4),
    _CwdsiRoamStatsAvgFiveMinutes_Type()
)
cwdsiRoamStatsAvgFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgFiveMinutes.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamStatsAvgFiveMinutes.setUnits("roams-per-second")
_CwdsiRoamMblGrpStatsTable_Object = MibTable
cwdsiRoamMblGrpStatsTable = _CwdsiRoamMblGrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5)
)
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsTable.setStatus("current")
_CwdsiRoamMblGrpStatsEntry_Object = MibTableRow
cwdsiRoamMblGrpStatsEntry = _CwdsiRoamMblGrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1)
)
cwdsiRoamMblGrpStatsEntry.setIndexNames(
    (0, "CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsNetworkId"),
)
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsEntry.setStatus("current")


class _CwdsiRoamMblGrpStatsNetworkId_Type(Unsigned32):
    """Custom type cwdsiRoamMblGrpStatsNetworkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CwdsiRoamMblGrpStatsNetworkId_Type.__name__ = "Unsigned32"
_CwdsiRoamMblGrpStatsNetworkId_Object = MibTableColumn
cwdsiRoamMblGrpStatsNetworkId = _CwdsiRoamMblGrpStatsNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 1),
    _CwdsiRoamMblGrpStatsNetworkId_Type()
)
cwdsiRoamMblGrpStatsNetworkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsNetworkId.setStatus("current")
_CwdsiRoamMblGrpStatsTotal_Type = Counter32
_CwdsiRoamMblGrpStatsTotal_Object = MibTableColumn
cwdsiRoamMblGrpStatsTotal = _CwdsiRoamMblGrpStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 2),
    _CwdsiRoamMblGrpStatsTotal_Type()
)
cwdsiRoamMblGrpStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsTotal.setStatus("current")
_CwdsiRoamMblGrpStatsNoAuthAaa_Type = Counter32
_CwdsiRoamMblGrpStatsNoAuthAaa_Object = MibTableColumn
cwdsiRoamMblGrpStatsNoAuthAaa = _CwdsiRoamMblGrpStatsNoAuthAaa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 3),
    _CwdsiRoamMblGrpStatsNoAuthAaa_Type()
)
cwdsiRoamMblGrpStatsNoAuthAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsNoAuthAaa.setStatus("current")
_CwdsiRoamMblGrpStatsAuthAaa_Type = Counter32
_CwdsiRoamMblGrpStatsAuthAaa_Object = MibTableColumn
cwdsiRoamMblGrpStatsAuthAaa = _CwdsiRoamMblGrpStatsAuthAaa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 4),
    _CwdsiRoamMblGrpStatsAuthAaa_Type()
)
cwdsiRoamMblGrpStatsAuthAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsAuthAaa.setStatus("current")
_CwdsiRoamMblGrpStatsFastSecured_Type = Counter32
_CwdsiRoamMblGrpStatsFastSecured_Object = MibTableColumn
cwdsiRoamMblGrpStatsFastSecured = _CwdsiRoamMblGrpStatsFastSecured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 5),
    _CwdsiRoamMblGrpStatsFastSecured_Type()
)
cwdsiRoamMblGrpStatsFastSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsFastSecured.setStatus("current")
_CwdsiRoamMblGrpStatsFiveSeconds_Type = Gauge32
_CwdsiRoamMblGrpStatsFiveSeconds_Object = MibTableColumn
cwdsiRoamMblGrpStatsFiveSeconds = _CwdsiRoamMblGrpStatsFiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 6),
    _CwdsiRoamMblGrpStatsFiveSeconds_Type()
)
cwdsiRoamMblGrpStatsFiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsFiveSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsFiveSeconds.setUnits("roams-per-second")
_CwdsiRoamMblGrpStatsOneMinute_Type = Gauge32
_CwdsiRoamMblGrpStatsOneMinute_Object = MibTableColumn
cwdsiRoamMblGrpStatsOneMinute = _CwdsiRoamMblGrpStatsOneMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 7),
    _CwdsiRoamMblGrpStatsOneMinute_Type()
)
cwdsiRoamMblGrpStatsOneMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsOneMinute.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsOneMinute.setUnits("roams-per-second")
_CwdsiRoamMblGrpStatsFiveMinutes_Type = Gauge32
_CwdsiRoamMblGrpStatsFiveMinutes_Object = MibTableColumn
cwdsiRoamMblGrpStatsFiveMinutes = _CwdsiRoamMblGrpStatsFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 8),
    _CwdsiRoamMblGrpStatsFiveMinutes_Type()
)
cwdsiRoamMblGrpStatsFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsFiveMinutes.setStatus("current")
if mibBuilder.loadTexts:
    cwdsiRoamMblGrpStatsFiveMinutes.setUnits("roams-per-second")
_CiscoWdsInfoMIBConform_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMIBConform = _CiscoWdsInfoMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2)
)
_CiscoWdsInfoMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMIBCompliances = _CiscoWdsInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 1)
)
_CiscoWdsInfoMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWdsInfoMIBGroups = _CiscoWdsInfoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2)
)

# Managed Objects groups

ciscoWdsInfoMacAuthCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 1)
)
ciscoWdsInfoMacAuthCacheGroup.setObjects(
    ("CISCO-WDS-INFO-MIB", "cwdsiMacAuthCacheAge")
)
if mibBuilder.loadTexts:
    ciscoWdsInfoMacAuthCacheGroup.setStatus("current")

ciscoWdsInfoAccessPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 2)
)
ciscoWdsInfoAccessPointGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiApAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApName"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApState"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApLifeTime"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborName"),
        ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborPortName"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoAccessPointGroup.setStatus("current")

ciscoWdsInfoMobileNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 3)
)
ciscoWdsInfoMobileNodeGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiMnAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnApMacAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnApAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnApAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnMobilityNetworkId"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnState"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnBssid"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnVlan"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnSsid"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnKeyMgmt"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnAuthType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnUptime"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnLifetime"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoMobileNodeGroup.setStatus("current")

ciscoWdsInfoNetworkManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 4)
)
ciscoWdsInfoNetworkManagerGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiWnmState"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmLinkStatus"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmClientTracking"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmReqMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmSentMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmRetryTxMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmWaitingAckMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropMicTxMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropUmdTxMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmIndicatedMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmRxMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropRxMsgCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWnmDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoNetworkManagerGroup.setStatus("current")

ciscoWdsInfoStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 5)
)
ciscoWdsInfoStatisticsGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiApNum"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMnNum"),
        ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthAttemptCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthSuccessCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthFailureCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMacSpoofingBlockCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamsWithoutAaaAuthCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamsWithFullAaaAuthCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamsFastSecuredCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMscMismatchCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiKscFailureCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMicFailureCount"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRnMismatchCount"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoStatisticsGroup.setStatus("current")

ciscoWdsInfoMobilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 6)
)
ciscoWdsInfoMobilityGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiLcpStatus"),
        ("CISCO-WDS-INFO-MIB", "cwdsiCsMgmtAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiCsMgmtAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWdsAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWdsAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWdsHsrpVirtualAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiWdsHsrpVirtualAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiHsrpState"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelAddrType"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelAddr"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelMtu"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpFlags"),
        ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpMnNum"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoMobilityGroup.setStatus("current")

ciscoWdsInfoRoamStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 7)
)
ciscoWdsInfoRoamStatisticsGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsStartTime"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgFiveSeconds"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgOneMinute"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgFiveMinutes"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsTotal"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsNoAuthAaa"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsAuthAaa"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFastSecured"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFiveSeconds"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsOneMinute"),
        ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFiveMinutes"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoRoamStatisticsGroup.setStatus("current")


# Notification objects

cwdsiLcpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 0, 1)
)
cwdsiLcpStatusChange.setObjects(
    ("CISCO-WDS-INFO-MIB", "cwdsiLcpStatus")
)
if mibBuilder.loadTexts:
    cwdsiLcpStatusChange.setStatus(
        "current"
    )

cwdsiHsrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 0, 2)
)
cwdsiHsrpStateChange.setObjects(
    ("CISCO-WDS-INFO-MIB", "cwdsiHsrpState")
)
if mibBuilder.loadTexts:
    cwdsiHsrpStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoWdsInfoNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 8)
)
ciscoWdsInfoNotifGroup.setObjects(
      *(("CISCO-WDS-INFO-MIB", "cwdsiLcpStatusChange"),
        ("CISCO-WDS-INFO-MIB", "cwdsiHsrpStateChange"))
)
if mibBuilder.loadTexts:
    ciscoWdsInfoNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWdsInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWdsInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WDS-INFO-MIB",
    **{"CWdsClientTrackingStatus": CWdsClientTrackingStatus,
       "CWdsDeviceAuthType": CWdsDeviceAuthType,
       "CWdsDeviceState": CWdsDeviceState,
       "ciscoWdsInfoMIB": ciscoWdsInfoMIB,
       "ciscoWdsInfoMIBNotifs": ciscoWdsInfoMIBNotifs,
       "cwdsiLcpStatusChange": cwdsiLcpStatusChange,
       "cwdsiHsrpStateChange": cwdsiHsrpStateChange,
       "ciscoWdsInfoMIBObjects": ciscoWdsInfoMIBObjects,
       "ciscoWdsInfoMacAuthCache": ciscoWdsInfoMacAuthCache,
       "cwdsiMacAuthCacheTable": cwdsiMacAuthCacheTable,
       "cwdsiMacAuthCacheEntry": cwdsiMacAuthCacheEntry,
       "cwdsiMacAuthCacheMacAddr": cwdsiMacAuthCacheMacAddr,
       "cwdsiMacAuthCacheAge": cwdsiMacAuthCacheAge,
       "ciscoWdsInfoAccessPoint": ciscoWdsInfoAccessPoint,
       "cwdsiApTable": cwdsiApTable,
       "cwdsiApEntry": cwdsiApEntry,
       "cwdsiApMacAddr": cwdsiApMacAddr,
       "cwdsiApAddrType": cwdsiApAddrType,
       "cwdsiApAddr": cwdsiApAddr,
       "cwdsiApName": cwdsiApName,
       "cwdsiApState": cwdsiApState,
       "cwdsiApLifeTime": cwdsiApLifeTime,
       "cwdsiApNeighborAddrType": cwdsiApNeighborAddrType,
       "cwdsiApNeighborAddr": cwdsiApNeighborAddr,
       "cwdsiApNeighborName": cwdsiApNeighborName,
       "cwdsiApNeighborPortName": cwdsiApNeighborPortName,
       "ciscoWdsInfoMobileNode": ciscoWdsInfoMobileNode,
       "cwdsiMnTable": cwdsiMnTable,
       "cwdsiMnEntry": cwdsiMnEntry,
       "cwdsiMnMacAddr": cwdsiMnMacAddr,
       "cwdsiMnAddrType": cwdsiMnAddrType,
       "cwdsiMnAddr": cwdsiMnAddr,
       "cwdsiMnApMacAddr": cwdsiMnApMacAddr,
       "cwdsiMnApAddrType": cwdsiMnApAddrType,
       "cwdsiMnApAddr": cwdsiMnApAddr,
       "cwdsiMnMobilityNetworkId": cwdsiMnMobilityNetworkId,
       "cwdsiMnState": cwdsiMnState,
       "cwdsiMnSsid": cwdsiMnSsid,
       "cwdsiMnBssid": cwdsiMnBssid,
       "cwdsiMnVlan": cwdsiMnVlan,
       "cwdsiMnKeyMgmt": cwdsiMnKeyMgmt,
       "cwdsiMnAuthType": cwdsiMnAuthType,
       "cwdsiMnUptime": cwdsiMnUptime,
       "cwdsiMnLifetime": cwdsiMnLifetime,
       "ciscoWdsInfoNetworkManager": ciscoWdsInfoNetworkManager,
       "cwdsiWnmTable": cwdsiWnmTable,
       "cwdsiWnmEntry": cwdsiWnmEntry,
       "cwdsiWnmAddrType": cwdsiWnmAddrType,
       "cwdsiWnmAddr": cwdsiWnmAddr,
       "cwdsiWnmState": cwdsiWnmState,
       "cwdsiWnmLinkStatus": cwdsiWnmLinkStatus,
       "cwdsiWnmClientTracking": cwdsiWnmClientTracking,
       "cwdsiWnmReqMsgCount": cwdsiWnmReqMsgCount,
       "cwdsiWnmSentMsgCount": cwdsiWnmSentMsgCount,
       "cwdsiWnmRetryTxMsgCount": cwdsiWnmRetryTxMsgCount,
       "cwdsiWnmWaitingAckMsgCount": cwdsiWnmWaitingAckMsgCount,
       "cwdsiWnmDropMicTxMsgCount": cwdsiWnmDropMicTxMsgCount,
       "cwdsiWnmDropUmdTxMsgCount": cwdsiWnmDropUmdTxMsgCount,
       "cwdsiWnmIndicatedMsgCount": cwdsiWnmIndicatedMsgCount,
       "cwdsiWnmRxMsgCount": cwdsiWnmRxMsgCount,
       "cwdsiWnmDropRxMsgCount": cwdsiWnmDropRxMsgCount,
       "cwdsiWnmDiscontinuityTime": cwdsiWnmDiscontinuityTime,
       "ciscoWdsInfoStatistics": ciscoWdsInfoStatistics,
       "cwdsiApNum": cwdsiApNum,
       "cwdsiMnNum": cwdsiMnNum,
       "cwdsiAaaAuthAttemptCount": cwdsiAaaAuthAttemptCount,
       "cwdsiAaaAuthSuccessCount": cwdsiAaaAuthSuccessCount,
       "cwdsiAaaAuthFailureCount": cwdsiAaaAuthFailureCount,
       "cwdsiMacSpoofingBlockCount": cwdsiMacSpoofingBlockCount,
       "cwdsiRoamsWithoutAaaAuthCount": cwdsiRoamsWithoutAaaAuthCount,
       "cwdsiRoamsWithFullAaaAuthCount": cwdsiRoamsWithFullAaaAuthCount,
       "cwdsiRoamsFastSecuredCount": cwdsiRoamsFastSecuredCount,
       "cwdsiMscMismatchCount": cwdsiMscMismatchCount,
       "cwdsiKscFailureCount": cwdsiKscFailureCount,
       "cwdsiMicFailureCount": cwdsiMicFailureCount,
       "cwdsiRnMismatchCount": cwdsiRnMismatchCount,
       "ciscoWdsInfoMobility": ciscoWdsInfoMobility,
       "cwdsiLcpStatus": cwdsiLcpStatus,
       "cwdsiCsMgmtAddrType": cwdsiCsMgmtAddrType,
       "cwdsiCsMgmtAddr": cwdsiCsMgmtAddr,
       "cwdsiWdsAddrType": cwdsiWdsAddrType,
       "cwdsiWdsAddr": cwdsiWdsAddr,
       "cwdsiWdsHsrpVirtualAddrType": cwdsiWdsHsrpVirtualAddrType,
       "cwdsiWdsHsrpVirtualAddr": cwdsiWdsHsrpVirtualAddr,
       "cwdsiHsrpState": cwdsiHsrpState,
       "cwdsiMobilityGroupTable": cwdsiMobilityGroupTable,
       "cwdsiMobilityGroupEntry": cwdsiMobilityGroupEntry,
       "cwdsiMobilityGrpNetworkId": cwdsiMobilityGrpNetworkId,
       "cwdsiMobilityGrpTunnelAddrType": cwdsiMobilityGrpTunnelAddrType,
       "cwdsiMobilityGrpTunnelAddr": cwdsiMobilityGrpTunnelAddr,
       "cwdsiMobilityGrpTunnelMtu": cwdsiMobilityGrpTunnelMtu,
       "cwdsiMobilityGrpFlags": cwdsiMobilityGrpFlags,
       "cwdsiMobilityGrpMnNum": cwdsiMobilityGrpMnNum,
       "ciscoWdsInfoRoamStatistics": ciscoWdsInfoRoamStatistics,
       "cwdsiRoamStatsStartTime": cwdsiRoamStatsStartTime,
       "cwdsiRoamStatsAvgFiveSeconds": cwdsiRoamStatsAvgFiveSeconds,
       "cwdsiRoamStatsAvgOneMinute": cwdsiRoamStatsAvgOneMinute,
       "cwdsiRoamStatsAvgFiveMinutes": cwdsiRoamStatsAvgFiveMinutes,
       "cwdsiRoamMblGrpStatsTable": cwdsiRoamMblGrpStatsTable,
       "cwdsiRoamMblGrpStatsEntry": cwdsiRoamMblGrpStatsEntry,
       "cwdsiRoamMblGrpStatsNetworkId": cwdsiRoamMblGrpStatsNetworkId,
       "cwdsiRoamMblGrpStatsTotal": cwdsiRoamMblGrpStatsTotal,
       "cwdsiRoamMblGrpStatsNoAuthAaa": cwdsiRoamMblGrpStatsNoAuthAaa,
       "cwdsiRoamMblGrpStatsAuthAaa": cwdsiRoamMblGrpStatsAuthAaa,
       "cwdsiRoamMblGrpStatsFastSecured": cwdsiRoamMblGrpStatsFastSecured,
       "cwdsiRoamMblGrpStatsFiveSeconds": cwdsiRoamMblGrpStatsFiveSeconds,
       "cwdsiRoamMblGrpStatsOneMinute": cwdsiRoamMblGrpStatsOneMinute,
       "cwdsiRoamMblGrpStatsFiveMinutes": cwdsiRoamMblGrpStatsFiveMinutes,
       "ciscoWdsInfoMIBConform": ciscoWdsInfoMIBConform,
       "ciscoWdsInfoMIBCompliances": ciscoWdsInfoMIBCompliances,
       "ciscoWdsInfoMIBCompliance": ciscoWdsInfoMIBCompliance,
       "ciscoWdsInfoMIBGroups": ciscoWdsInfoMIBGroups,
       "ciscoWdsInfoMacAuthCacheGroup": ciscoWdsInfoMacAuthCacheGroup,
       "ciscoWdsInfoAccessPointGroup": ciscoWdsInfoAccessPointGroup,
       "ciscoWdsInfoMobileNodeGroup": ciscoWdsInfoMobileNodeGroup,
       "ciscoWdsInfoNetworkManagerGroup": ciscoWdsInfoNetworkManagerGroup,
       "ciscoWdsInfoStatisticsGroup": ciscoWdsInfoStatisticsGroup,
       "ciscoWdsInfoMobilityGroup": ciscoWdsInfoMobilityGroup,
       "ciscoWdsInfoRoamStatisticsGroup": ciscoWdsInfoRoamStatisticsGroup,
       "ciscoWdsInfoNotifGroup": ciscoWdsInfoNotifGroup}
)
