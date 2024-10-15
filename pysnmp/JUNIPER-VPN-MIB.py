# SNMP MIB module (JUNIPER-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:03 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

jnxVpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26)
)
jnxVpnMIB.setRevisions(
        ("2010-10-15 00:00",
         "2010-08-27 00:00",
         "2002-04-21 21:28")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxVpnName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class JnxVpnType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bgpAtmVpn", 10),
          ("bgpIpVpn", 2),
          ("bgpL2Vpn", 3),
          ("bgpVpls", 4),
          ("ccc", 9),
          ("l2Circuit", 5),
          ("ldpVpls", 6),
          ("opticalVpn", 7),
          ("other", 1),
          ("vpOxc", 8))
    )



class JnxVpnIdentifierType(Integer32, TextualConvention):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("localSwitch", 11),
          ("none", 0),
          ("other", 1),
          ("routeDistinguisher", 2),
          ("routeDistinguisher0", 3),
          ("routeDistinguisher1", 4),
          ("routeDistinguisher2", 5),
          ("routeTarget", 6),
          ("routeTarget0", 7),
          ("routeTarget1", 8),
          ("routeTarget2", 9),
          ("vcId", 10))
    )



class JnxVpnIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class JnxVpnRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x:1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteDistinguisher0(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-2d:4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteDistinguisher1(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteDistinguisher2(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-4d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteTarget(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x:1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteTarget0(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-4d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteTarget1(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnRouteTarget2(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x-2d:4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnVCIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d:4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxVpnMultiplexor(Unsigned32, TextualConvention):
    status = "current"


class JnxVpnLocalSwitchIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



# MIB Managed Objects in the order of their OIDs

_JnxVpnMIBNotifications_ObjectIdentity = ObjectIdentity
jnxVpnMIBNotifications = _JnxVpnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 0)
)
_JnxVpnMibObjects_ObjectIdentity = ObjectIdentity
jnxVpnMibObjects = _JnxVpnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1)
)
_JnxVpnInfo_ObjectIdentity = ObjectIdentity
jnxVpnInfo = _JnxVpnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1)
)
_JnxVpnConfiguredVpns_Type = Gauge32
_JnxVpnConfiguredVpns_Object = MibScalar
jnxVpnConfiguredVpns = _JnxVpnConfiguredVpns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 1),
    _JnxVpnConfiguredVpns_Type()
)
jnxVpnConfiguredVpns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnConfiguredVpns.setStatus("current")
_JnxVpnActiveVpns_Type = Gauge32
_JnxVpnActiveVpns_Object = MibScalar
jnxVpnActiveVpns = _JnxVpnActiveVpns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 2),
    _JnxVpnActiveVpns_Type()
)
jnxVpnActiveVpns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnActiveVpns.setStatus("current")
_JnxVpnNextIfIndex_Type = Unsigned32
_JnxVpnNextIfIndex_Object = MibScalar
jnxVpnNextIfIndex = _JnxVpnNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 3),
    _JnxVpnNextIfIndex_Type()
)
jnxVpnNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnNextIfIndex.setStatus("current")
_JnxVpnNextPwIndex_Type = Unsigned32
_JnxVpnNextPwIndex_Object = MibScalar
jnxVpnNextPwIndex = _JnxVpnNextPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 4),
    _JnxVpnNextPwIndex_Type()
)
jnxVpnNextPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnNextPwIndex.setStatus("current")
_JnxVpnNextRTIndex_Type = Unsigned32
_JnxVpnNextRTIndex_Object = MibScalar
jnxVpnNextRTIndex = _JnxVpnNextRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 1, 5),
    _JnxVpnNextRTIndex_Type()
)
jnxVpnNextRTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnNextRTIndex.setStatus("current")
_JnxVpnTable_Object = MibTable
jnxVpnTable = _JnxVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVpnTable.setStatus("current")
_JnxVpnEntry_Object = MibTableRow
jnxVpnEntry = _JnxVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1)
)
jnxVpnEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnName"),
)
if mibBuilder.loadTexts:
    jnxVpnEntry.setStatus("current")
_JnxVpnType_Type = JnxVpnType
_JnxVpnType_Object = MibTableColumn
jnxVpnType = _JnxVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 1),
    _JnxVpnType_Type()
)
jnxVpnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVpnType.setStatus("current")
_JnxVpnName_Type = JnxVpnName
_JnxVpnName_Object = MibTableColumn
jnxVpnName = _JnxVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 2),
    _JnxVpnName_Type()
)
jnxVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVpnName.setStatus("current")
_JnxVpnRowStatus_Type = RowStatus
_JnxVpnRowStatus_Object = MibTableColumn
jnxVpnRowStatus = _JnxVpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 3),
    _JnxVpnRowStatus_Type()
)
jnxVpnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRowStatus.setStatus("current")
_JnxVpnStorageType_Type = StorageType
_JnxVpnStorageType_Object = MibTableColumn
jnxVpnStorageType = _JnxVpnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 4),
    _JnxVpnStorageType_Type()
)
jnxVpnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnStorageType.setStatus("current")
_JnxVpnDescription_Type = SnmpAdminString
_JnxVpnDescription_Object = MibTableColumn
jnxVpnDescription = _JnxVpnDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 5),
    _JnxVpnDescription_Type()
)
jnxVpnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnDescription.setStatus("current")
_JnxVpnIdentifierType_Type = JnxVpnIdentifierType
_JnxVpnIdentifierType_Object = MibTableColumn
jnxVpnIdentifierType = _JnxVpnIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 6),
    _JnxVpnIdentifierType_Type()
)
jnxVpnIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIdentifierType.setStatus("current")
_JnxVpnIdentifier_Type = JnxVpnIdentifier
_JnxVpnIdentifier_Object = MibTableColumn
jnxVpnIdentifier = _JnxVpnIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 7),
    _JnxVpnIdentifier_Type()
)
jnxVpnIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIdentifier.setStatus("current")
_JnxVpnConfiguredSites_Type = Gauge32
_JnxVpnConfiguredSites_Object = MibTableColumn
jnxVpnConfiguredSites = _JnxVpnConfiguredSites_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 8),
    _JnxVpnConfiguredSites_Type()
)
jnxVpnConfiguredSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnConfiguredSites.setStatus("current")
_JnxVpnActiveSites_Type = Gauge32
_JnxVpnActiveSites_Object = MibTableColumn
jnxVpnActiveSites = _JnxVpnActiveSites_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 9),
    _JnxVpnActiveSites_Type()
)
jnxVpnActiveSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnActiveSites.setStatus("current")
_JnxVpnLocalAddresses_Type = Gauge32
_JnxVpnLocalAddresses_Object = MibTableColumn
jnxVpnLocalAddresses = _JnxVpnLocalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 10),
    _JnxVpnLocalAddresses_Type()
)
jnxVpnLocalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnLocalAddresses.setStatus("current")
_JnxVpnTotalAddresses_Type = Gauge32
_JnxVpnTotalAddresses_Object = MibTableColumn
jnxVpnTotalAddresses = _JnxVpnTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 11),
    _JnxVpnTotalAddresses_Type()
)
jnxVpnTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnTotalAddresses.setStatus("current")
_JnxVpnAge_Type = TimeTicks
_JnxVpnAge_Object = MibTableColumn
jnxVpnAge = _JnxVpnAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 2, 1, 12),
    _JnxVpnAge_Type()
)
jnxVpnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnAge.setStatus("current")
_JnxVpnIfTable_Object = MibTable
jnxVpnIfTable = _JnxVpnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3)
)
if mibBuilder.loadTexts:
    jnxVpnIfTable.setStatus("current")
_JnxVpnIfEntry_Object = MibTableRow
jnxVpnIfEntry = _JnxVpnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1)
)
jnxVpnIfEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnIfVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnIfIndex"),
)
if mibBuilder.loadTexts:
    jnxVpnIfEntry.setStatus("current")
_JnxVpnIfVpnType_Type = JnxVpnType
_JnxVpnIfVpnType_Object = MibTableColumn
jnxVpnIfVpnType = _JnxVpnIfVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 1),
    _JnxVpnIfVpnType_Type()
)
jnxVpnIfVpnType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnIfVpnType.setStatus("current")
_JnxVpnIfVpnName_Type = JnxVpnName
_JnxVpnIfVpnName_Object = MibTableColumn
jnxVpnIfVpnName = _JnxVpnIfVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 2),
    _JnxVpnIfVpnName_Type()
)
jnxVpnIfVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnIfVpnName.setStatus("current")
_JnxVpnIfIndex_Type = Unsigned32
_JnxVpnIfIndex_Object = MibTableColumn
jnxVpnIfIndex = _JnxVpnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 3),
    _JnxVpnIfIndex_Type()
)
jnxVpnIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnIfIndex.setStatus("current")
_JnxVpnIfRowStatus_Type = RowStatus
_JnxVpnIfRowStatus_Object = MibTableColumn
jnxVpnIfRowStatus = _JnxVpnIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 4),
    _JnxVpnIfRowStatus_Type()
)
jnxVpnIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfRowStatus.setStatus("current")
_JnxVpnIfStorageType_Type = StorageType
_JnxVpnIfStorageType_Object = MibTableColumn
jnxVpnIfStorageType = _JnxVpnIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 5),
    _JnxVpnIfStorageType_Type()
)
jnxVpnIfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfStorageType.setStatus("current")
_JnxVpnIfAssociatedPw_Type = Unsigned32
_JnxVpnIfAssociatedPw_Object = MibTableColumn
jnxVpnIfAssociatedPw = _JnxVpnIfAssociatedPw_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 6),
    _JnxVpnIfAssociatedPw_Type()
)
jnxVpnIfAssociatedPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfAssociatedPw.setStatus("current")


class _JnxVpnIfProtocol_Type(Integer32):
    """Custom type jnxVpnIfProtocol based on Integer32"""
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
              15,
              17,
              18,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5", 2),
          ("atmCell", 3),
          ("atmTrunkNNI", 129),
          ("atmTrunkUNI", 130),
          ("atmVcc", 9),
          ("atmVpc", 10),
          ("bgp", 23),
          ("cem", 8),
          ("cesop", 26),
          ("ciscoHdlc", 6),
          ("ethernet", 5),
          ("ethernetVlan", 4),
          ("frameRelay", 1),
          ("frameRelayPort", 15),
          ("ipInterworking", 12),
          ("ospf", 22),
          ("other", 0),
          ("ppp", 7),
          ("rip", 21),
          ("satope1", 17),
          ("satope3", 24),
          ("satopt1", 18),
          ("satopt3", 25),
          ("snapInterworking", 13),
          ("static", 20),
          ("vpls", 11))
    )


_JnxVpnIfProtocol_Type.__name__ = "Integer32"
_JnxVpnIfProtocol_Object = MibTableColumn
jnxVpnIfProtocol = _JnxVpnIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 7),
    _JnxVpnIfProtocol_Type()
)
jnxVpnIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfProtocol.setStatus("current")
_JnxVpnIfInBandwidth_Type = Unsigned32
_JnxVpnIfInBandwidth_Object = MibTableColumn
jnxVpnIfInBandwidth = _JnxVpnIfInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 8),
    _JnxVpnIfInBandwidth_Type()
)
jnxVpnIfInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfInBandwidth.setStatus("current")
_JnxVpnIfOutBandwidth_Type = Unsigned32
_JnxVpnIfOutBandwidth_Object = MibTableColumn
jnxVpnIfOutBandwidth = _JnxVpnIfOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 9),
    _JnxVpnIfOutBandwidth_Type()
)
jnxVpnIfOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfOutBandwidth.setStatus("current")


class _JnxVpnIfStatus_Type(Integer32):
    """Custom type jnxVpnIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("down", 4),
          ("encapsulationMismatch", 3),
          ("noLocalInterface", 1),
          ("unknown", 0),
          ("up", 5))
    )


_JnxVpnIfStatus_Type.__name__ = "Integer32"
_JnxVpnIfStatus_Object = MibTableColumn
jnxVpnIfStatus = _JnxVpnIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 3, 1, 10),
    _JnxVpnIfStatus_Type()
)
jnxVpnIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnIfStatus.setStatus("current")
_JnxVpnPwTable_Object = MibTable
jnxVpnPwTable = _JnxVpnPwTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4)
)
if mibBuilder.loadTexts:
    jnxVpnPwTable.setStatus("current")
_JnxVpnPwEntry_Object = MibTableRow
jnxVpnPwEntry = _JnxVpnPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1)
)
jnxVpnPwEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"),
)
if mibBuilder.loadTexts:
    jnxVpnPwEntry.setStatus("current")
_JnxVpnPwVpnType_Type = JnxVpnType
_JnxVpnPwVpnType_Object = MibTableColumn
jnxVpnPwVpnType = _JnxVpnPwVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 1),
    _JnxVpnPwVpnType_Type()
)
jnxVpnPwVpnType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnPwVpnType.setStatus("current")
_JnxVpnPwVpnName_Type = JnxVpnName
_JnxVpnPwVpnName_Object = MibTableColumn
jnxVpnPwVpnName = _JnxVpnPwVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 2),
    _JnxVpnPwVpnName_Type()
)
jnxVpnPwVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnPwVpnName.setStatus("current")
_JnxVpnPwIndex_Type = Unsigned32
_JnxVpnPwIndex_Object = MibTableColumn
jnxVpnPwIndex = _JnxVpnPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 3),
    _JnxVpnPwIndex_Type()
)
jnxVpnPwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxVpnPwIndex.setStatus("current")
_JnxVpnPwRowStatus_Type = RowStatus
_JnxVpnPwRowStatus_Object = MibTableColumn
jnxVpnPwRowStatus = _JnxVpnPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 4),
    _JnxVpnPwRowStatus_Type()
)
jnxVpnPwRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwRowStatus.setStatus("current")
_JnxVpnPwStorageType_Type = StorageType
_JnxVpnPwStorageType_Object = MibTableColumn
jnxVpnPwStorageType = _JnxVpnPwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 5),
    _JnxVpnPwStorageType_Type()
)
jnxVpnPwStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwStorageType.setStatus("current")
_JnxVpnPwAssociatedInterface_Type = Unsigned32
_JnxVpnPwAssociatedInterface_Object = MibTableColumn
jnxVpnPwAssociatedInterface = _JnxVpnPwAssociatedInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 6),
    _JnxVpnPwAssociatedInterface_Type()
)
jnxVpnPwAssociatedInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwAssociatedInterface.setStatus("current")
_JnxVpnPwLocalSiteId_Type = Unsigned32
_JnxVpnPwLocalSiteId_Object = MibTableColumn
jnxVpnPwLocalSiteId = _JnxVpnPwLocalSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 7),
    _JnxVpnPwLocalSiteId_Type()
)
jnxVpnPwLocalSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLocalSiteId.setStatus("current")
_JnxVpnPwRemoteSiteId_Type = Unsigned32
_JnxVpnPwRemoteSiteId_Object = MibTableColumn
jnxVpnPwRemoteSiteId = _JnxVpnPwRemoteSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 8),
    _JnxVpnPwRemoteSiteId_Type()
)
jnxVpnPwRemoteSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwRemoteSiteId.setStatus("current")
_JnxVpnRemotePeIdAddrType_Type = InetAddressType
_JnxVpnRemotePeIdAddrType_Object = MibTableColumn
jnxVpnRemotePeIdAddrType = _JnxVpnRemotePeIdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 9),
    _JnxVpnRemotePeIdAddrType_Type()
)
jnxVpnRemotePeIdAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRemotePeIdAddrType.setStatus("current")
_JnxVpnRemotePeIdAddress_Type = InetAddress
_JnxVpnRemotePeIdAddress_Object = MibTableColumn
jnxVpnRemotePeIdAddress = _JnxVpnRemotePeIdAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 10),
    _JnxVpnRemotePeIdAddress_Type()
)
jnxVpnRemotePeIdAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRemotePeIdAddress.setStatus("current")


class _JnxVpnPwTunnelType_Type(Integer32):
    """Custom type jnxVpnPwTunnelType based on Integer32"""
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
        *(("crLdp", 7),
          ("gre", 2),
          ("ipSec", 4),
          ("l2tpv3", 3),
          ("ldp", 5),
          ("rsvpTe", 6),
          ("static", 1))
    )


_JnxVpnPwTunnelType_Type.__name__ = "Integer32"
_JnxVpnPwTunnelType_Object = MibTableColumn
jnxVpnPwTunnelType = _JnxVpnPwTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 11),
    _JnxVpnPwTunnelType_Type()
)
jnxVpnPwTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTunnelType.setStatus("current")
_JnxVpnPwTunnelName_Type = SnmpAdminString
_JnxVpnPwTunnelName_Object = MibTableColumn
jnxVpnPwTunnelName = _JnxVpnPwTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 12),
    _JnxVpnPwTunnelName_Type()
)
jnxVpnPwTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTunnelName.setStatus("current")
_JnxVpnPwReceiveDemux_Type = JnxVpnMultiplexor
_JnxVpnPwReceiveDemux_Object = MibTableColumn
jnxVpnPwReceiveDemux = _JnxVpnPwReceiveDemux_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 13),
    _JnxVpnPwReceiveDemux_Type()
)
jnxVpnPwReceiveDemux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwReceiveDemux.setStatus("current")
_JnxVpnPwTransmitDemux_Type = JnxVpnMultiplexor
_JnxVpnPwTransmitDemux_Object = MibTableColumn
jnxVpnPwTransmitDemux = _JnxVpnPwTransmitDemux_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 14),
    _JnxVpnPwTransmitDemux_Type()
)
jnxVpnPwTransmitDemux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTransmitDemux.setStatus("current")


class _JnxVpnPwStatus_Type(Integer32):
    """Custom type jnxVpnPwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("unknown", 0),
          ("up", 2))
    )


_JnxVpnPwStatus_Type.__name__ = "Integer32"
_JnxVpnPwStatus_Object = MibTableColumn
jnxVpnPwStatus = _JnxVpnPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 15),
    _JnxVpnPwStatus_Type()
)
jnxVpnPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwStatus.setStatus("current")


class _JnxVpnPwTunnelStatus_Type(Integer32):
    """Custom type jnxVpnPwTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("testing", 2),
          ("unknown", 0),
          ("up", 3))
    )


_JnxVpnPwTunnelStatus_Type.__name__ = "Integer32"
_JnxVpnPwTunnelStatus_Object = MibTableColumn
jnxVpnPwTunnelStatus = _JnxVpnPwTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 16),
    _JnxVpnPwTunnelStatus_Type()
)
jnxVpnPwTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTunnelStatus.setStatus("current")


class _JnxVpnPwRemoteSiteStatus_Type(Integer32):
    """Custom type jnxVpnPwRemoteSiteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("outOfRange", 1),
          ("unknown", 0),
          ("up", 3))
    )


_JnxVpnPwRemoteSiteStatus_Type.__name__ = "Integer32"
_JnxVpnPwRemoteSiteStatus_Object = MibTableColumn
jnxVpnPwRemoteSiteStatus = _JnxVpnPwRemoteSiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 17),
    _JnxVpnPwRemoteSiteStatus_Type()
)
jnxVpnPwRemoteSiteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwRemoteSiteStatus.setStatus("current")
_JnxVpnPwTimeUp_Type = TimeTicks
_JnxVpnPwTimeUp_Object = MibTableColumn
jnxVpnPwTimeUp = _JnxVpnPwTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 18),
    _JnxVpnPwTimeUp_Type()
)
jnxVpnPwTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTimeUp.setStatus("current")
_JnxVpnPwTransitions_Type = Gauge32
_JnxVpnPwTransitions_Object = MibTableColumn
jnxVpnPwTransitions = _JnxVpnPwTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 19),
    _JnxVpnPwTransitions_Type()
)
jnxVpnPwTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwTransitions.setStatus("current")
_JnxVpnPwLastTransition_Type = TimeTicks
_JnxVpnPwLastTransition_Object = MibTableColumn
jnxVpnPwLastTransition = _JnxVpnPwLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 20),
    _JnxVpnPwLastTransition_Type()
)
jnxVpnPwLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLastTransition.setStatus("current")
_JnxVpnPwPacketsSent_Type = Counter64
_JnxVpnPwPacketsSent_Object = MibTableColumn
jnxVpnPwPacketsSent = _JnxVpnPwPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 21),
    _JnxVpnPwPacketsSent_Type()
)
jnxVpnPwPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwPacketsSent.setStatus("current")
_JnxVpnPwOctetsSent_Type = Counter64
_JnxVpnPwOctetsSent_Object = MibTableColumn
jnxVpnPwOctetsSent = _JnxVpnPwOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 22),
    _JnxVpnPwOctetsSent_Type()
)
jnxVpnPwOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwOctetsSent.setStatus("current")
_JnxVpnPwPacketsReceived_Type = Counter64
_JnxVpnPwPacketsReceived_Object = MibTableColumn
jnxVpnPwPacketsReceived = _JnxVpnPwPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 23),
    _JnxVpnPwPacketsReceived_Type()
)
jnxVpnPwPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwPacketsReceived.setStatus("current")
_JnxVpnPwOctetsReceived_Type = Counter64
_JnxVpnPwOctetsReceived_Object = MibTableColumn
jnxVpnPwOctetsReceived = _JnxVpnPwOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 24),
    _JnxVpnPwOctetsReceived_Type()
)
jnxVpnPwOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwOctetsReceived.setStatus("current")
_JnxVpnPwLRPacketsSent_Type = Counter32
_JnxVpnPwLRPacketsSent_Object = MibTableColumn
jnxVpnPwLRPacketsSent = _JnxVpnPwLRPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 25),
    _JnxVpnPwLRPacketsSent_Type()
)
jnxVpnPwLRPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLRPacketsSent.setStatus("current")
_JnxVpnPwLROctetsSent_Type = Counter32
_JnxVpnPwLROctetsSent_Object = MibTableColumn
jnxVpnPwLROctetsSent = _JnxVpnPwLROctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 26),
    _JnxVpnPwLROctetsSent_Type()
)
jnxVpnPwLROctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLROctetsSent.setStatus("current")
_JnxVpnPwLRPacketsReceived_Type = Counter32
_JnxVpnPwLRPacketsReceived_Object = MibTableColumn
jnxVpnPwLRPacketsReceived = _JnxVpnPwLRPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 27),
    _JnxVpnPwLRPacketsReceived_Type()
)
jnxVpnPwLRPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLRPacketsReceived.setStatus("current")
_JnxVpnPwLROctetsReceived_Type = Counter32
_JnxVpnPwLROctetsReceived_Object = MibTableColumn
jnxVpnPwLROctetsReceived = _JnxVpnPwLROctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 4, 1, 28),
    _JnxVpnPwLROctetsReceived_Type()
)
jnxVpnPwLROctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnPwLROctetsReceived.setStatus("current")
_JnxVpnRTTable_Object = MibTable
jnxVpnRTTable = _JnxVpnRTTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5)
)
if mibBuilder.loadTexts:
    jnxVpnRTTable.setStatus("current")
_JnxVpnRTEntry_Object = MibTableRow
jnxVpnRTEntry = _JnxVpnRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1)
)
jnxVpnRTEntry.setIndexNames(
    (0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnType"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnRTVpnName"),
    (0, "JUNIPER-VPN-MIB", "jnxVpnRTIndex"),
)
if mibBuilder.loadTexts:
    jnxVpnRTEntry.setStatus("current")
_JnxVpnRTVpnType_Type = JnxVpnType
_JnxVpnRTVpnType_Object = MibTableColumn
jnxVpnRTVpnType = _JnxVpnRTVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 1),
    _JnxVpnRTVpnType_Type()
)
jnxVpnRTVpnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVpnRTVpnType.setStatus("current")
_JnxVpnRTVpnName_Type = JnxVpnName
_JnxVpnRTVpnName_Object = MibTableColumn
jnxVpnRTVpnName = _JnxVpnRTVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 2),
    _JnxVpnRTVpnName_Type()
)
jnxVpnRTVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVpnRTVpnName.setStatus("current")
_JnxVpnRTIndex_Type = Unsigned32
_JnxVpnRTIndex_Object = MibTableColumn
jnxVpnRTIndex = _JnxVpnRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 3),
    _JnxVpnRTIndex_Type()
)
jnxVpnRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVpnRTIndex.setStatus("current")
_JnxVpnRTRowStatus_Type = RowStatus
_JnxVpnRTRowStatus_Object = MibTableColumn
jnxVpnRTRowStatus = _JnxVpnRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 4),
    _JnxVpnRTRowStatus_Type()
)
jnxVpnRTRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRTRowStatus.setStatus("current")
_JnxVpnRTStorageType_Type = StorageType
_JnxVpnRTStorageType_Object = MibTableColumn
jnxVpnRTStorageType = _JnxVpnRTStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 5),
    _JnxVpnRTStorageType_Type()
)
jnxVpnRTStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRTStorageType.setStatus("current")
_JnxVpnRTType_Type = JnxVpnIdentifierType
_JnxVpnRTType_Object = MibTableColumn
jnxVpnRTType = _JnxVpnRTType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 6),
    _JnxVpnRTType_Type()
)
jnxVpnRTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRTType.setStatus("current")
_JnxVpnRT_Type = JnxVpnIdentifier
_JnxVpnRT_Object = MibTableColumn
jnxVpnRT = _JnxVpnRT_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 7),
    _JnxVpnRT_Type()
)
jnxVpnRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRT.setStatus("current")


class _JnxVpnRTFunction_Type(Integer32):
    """Custom type jnxVpnRTFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("export", 2),
          ("import", 1))
    )


_JnxVpnRTFunction_Type.__name__ = "Integer32"
_JnxVpnRTFunction_Object = MibTableColumn
jnxVpnRTFunction = _JnxVpnRTFunction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 1, 5, 1, 8),
    _JnxVpnRTFunction_Type()
)
jnxVpnRTFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVpnRTFunction.setStatus("current")
_JnxVpnMIBConformance_ObjectIdentity = ObjectIdentity
jnxVpnMIBConformance = _JnxVpnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 2)
)

# Managed Objects groups


# Notification objects

jnxVpnIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 1)
)
jnxVpnIfUp.setObjects(
      *(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"),
        ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"),
        ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
)
if mibBuilder.loadTexts:
    jnxVpnIfUp.setStatus(
        "current"
    )

jnxVpnIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 2)
)
jnxVpnIfDown.setObjects(
      *(("JUNIPER-VPN-MIB", "jnxVpnIfVpnType"),
        ("JUNIPER-VPN-MIB", "jnxVpnIfVpnName"),
        ("JUNIPER-VPN-MIB", "jnxVpnIfIndex"))
)
if mibBuilder.loadTexts:
    jnxVpnIfDown.setStatus(
        "current"
    )

jnxVpnPwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 3)
)
jnxVpnPwUp.setObjects(
      *(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
        ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
        ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
)
if mibBuilder.loadTexts:
    jnxVpnPwUp.setStatus(
        "current"
    )

jnxVpnPwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 26, 0, 4)
)
jnxVpnPwDown.setObjects(
      *(("JUNIPER-VPN-MIB", "jnxVpnPwVpnType"),
        ("JUNIPER-VPN-MIB", "jnxVpnPwVpnName"),
        ("JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
)
if mibBuilder.loadTexts:
    jnxVpnPwDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-VPN-MIB",
    **{"JnxVpnName": JnxVpnName,
       "JnxVpnType": JnxVpnType,
       "JnxVpnIdentifierType": JnxVpnIdentifierType,
       "JnxVpnIdentifier": JnxVpnIdentifier,
       "JnxVpnRouteDistinguisher": JnxVpnRouteDistinguisher,
       "JnxVpnRouteDistinguisher0": JnxVpnRouteDistinguisher0,
       "JnxVpnRouteDistinguisher1": JnxVpnRouteDistinguisher1,
       "JnxVpnRouteDistinguisher2": JnxVpnRouteDistinguisher2,
       "JnxVpnRouteTarget": JnxVpnRouteTarget,
       "JnxVpnRouteTarget0": JnxVpnRouteTarget0,
       "JnxVpnRouteTarget1": JnxVpnRouteTarget1,
       "JnxVpnRouteTarget2": JnxVpnRouteTarget2,
       "JnxVpnVCIdentifier": JnxVpnVCIdentifier,
       "JnxVpnMultiplexor": JnxVpnMultiplexor,
       "JnxVpnLocalSwitchIdentifier": JnxVpnLocalSwitchIdentifier,
       "jnxVpnMIB": jnxVpnMIB,
       "jnxVpnMIBNotifications": jnxVpnMIBNotifications,
       "jnxVpnIfUp": jnxVpnIfUp,
       "jnxVpnIfDown": jnxVpnIfDown,
       "jnxVpnPwUp": jnxVpnPwUp,
       "jnxVpnPwDown": jnxVpnPwDown,
       "jnxVpnMibObjects": jnxVpnMibObjects,
       "jnxVpnInfo": jnxVpnInfo,
       "jnxVpnConfiguredVpns": jnxVpnConfiguredVpns,
       "jnxVpnActiveVpns": jnxVpnActiveVpns,
       "jnxVpnNextIfIndex": jnxVpnNextIfIndex,
       "jnxVpnNextPwIndex": jnxVpnNextPwIndex,
       "jnxVpnNextRTIndex": jnxVpnNextRTIndex,
       "jnxVpnTable": jnxVpnTable,
       "jnxVpnEntry": jnxVpnEntry,
       "jnxVpnType": jnxVpnType,
       "jnxVpnName": jnxVpnName,
       "jnxVpnRowStatus": jnxVpnRowStatus,
       "jnxVpnStorageType": jnxVpnStorageType,
       "jnxVpnDescription": jnxVpnDescription,
       "jnxVpnIdentifierType": jnxVpnIdentifierType,
       "jnxVpnIdentifier": jnxVpnIdentifier,
       "jnxVpnConfiguredSites": jnxVpnConfiguredSites,
       "jnxVpnActiveSites": jnxVpnActiveSites,
       "jnxVpnLocalAddresses": jnxVpnLocalAddresses,
       "jnxVpnTotalAddresses": jnxVpnTotalAddresses,
       "jnxVpnAge": jnxVpnAge,
       "jnxVpnIfTable": jnxVpnIfTable,
       "jnxVpnIfEntry": jnxVpnIfEntry,
       "jnxVpnIfVpnType": jnxVpnIfVpnType,
       "jnxVpnIfVpnName": jnxVpnIfVpnName,
       "jnxVpnIfIndex": jnxVpnIfIndex,
       "jnxVpnIfRowStatus": jnxVpnIfRowStatus,
       "jnxVpnIfStorageType": jnxVpnIfStorageType,
       "jnxVpnIfAssociatedPw": jnxVpnIfAssociatedPw,
       "jnxVpnIfProtocol": jnxVpnIfProtocol,
       "jnxVpnIfInBandwidth": jnxVpnIfInBandwidth,
       "jnxVpnIfOutBandwidth": jnxVpnIfOutBandwidth,
       "jnxVpnIfStatus": jnxVpnIfStatus,
       "jnxVpnPwTable": jnxVpnPwTable,
       "jnxVpnPwEntry": jnxVpnPwEntry,
       "jnxVpnPwVpnType": jnxVpnPwVpnType,
       "jnxVpnPwVpnName": jnxVpnPwVpnName,
       "jnxVpnPwIndex": jnxVpnPwIndex,
       "jnxVpnPwRowStatus": jnxVpnPwRowStatus,
       "jnxVpnPwStorageType": jnxVpnPwStorageType,
       "jnxVpnPwAssociatedInterface": jnxVpnPwAssociatedInterface,
       "jnxVpnPwLocalSiteId": jnxVpnPwLocalSiteId,
       "jnxVpnPwRemoteSiteId": jnxVpnPwRemoteSiteId,
       "jnxVpnRemotePeIdAddrType": jnxVpnRemotePeIdAddrType,
       "jnxVpnRemotePeIdAddress": jnxVpnRemotePeIdAddress,
       "jnxVpnPwTunnelType": jnxVpnPwTunnelType,
       "jnxVpnPwTunnelName": jnxVpnPwTunnelName,
       "jnxVpnPwReceiveDemux": jnxVpnPwReceiveDemux,
       "jnxVpnPwTransmitDemux": jnxVpnPwTransmitDemux,
       "jnxVpnPwStatus": jnxVpnPwStatus,
       "jnxVpnPwTunnelStatus": jnxVpnPwTunnelStatus,
       "jnxVpnPwRemoteSiteStatus": jnxVpnPwRemoteSiteStatus,
       "jnxVpnPwTimeUp": jnxVpnPwTimeUp,
       "jnxVpnPwTransitions": jnxVpnPwTransitions,
       "jnxVpnPwLastTransition": jnxVpnPwLastTransition,
       "jnxVpnPwPacketsSent": jnxVpnPwPacketsSent,
       "jnxVpnPwOctetsSent": jnxVpnPwOctetsSent,
       "jnxVpnPwPacketsReceived": jnxVpnPwPacketsReceived,
       "jnxVpnPwOctetsReceived": jnxVpnPwOctetsReceived,
       "jnxVpnPwLRPacketsSent": jnxVpnPwLRPacketsSent,
       "jnxVpnPwLROctetsSent": jnxVpnPwLROctetsSent,
       "jnxVpnPwLRPacketsReceived": jnxVpnPwLRPacketsReceived,
       "jnxVpnPwLROctetsReceived": jnxVpnPwLROctetsReceived,
       "jnxVpnRTTable": jnxVpnRTTable,
       "jnxVpnRTEntry": jnxVpnRTEntry,
       "jnxVpnRTVpnType": jnxVpnRTVpnType,
       "jnxVpnRTVpnName": jnxVpnRTVpnName,
       "jnxVpnRTIndex": jnxVpnRTIndex,
       "jnxVpnRTRowStatus": jnxVpnRTRowStatus,
       "jnxVpnRTStorageType": jnxVpnRTStorageType,
       "jnxVpnRTType": jnxVpnRTType,
       "jnxVpnRT": jnxVpnRT,
       "jnxVpnRTFunction": jnxVpnRTFunction,
       "jnxVpnMIBConformance": jnxVpnMIBConformance}
)
