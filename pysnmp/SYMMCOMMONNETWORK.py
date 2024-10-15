# SNMP MIB module (SYMMCOMMONNETWORK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMCOMMONNETWORK
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:44 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressIPv6z,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressIPv6z",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(EnableValue,
 symmNetwork) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "symmNetwork")


# MODULE-IDENTITY

symmCommonNetwork = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1)
)
symmCommonNetwork.setRevisions(
        ("2018-04-10 20:53",)
)


# Types definitions



class AutoSpeedValue(Integer32):
    """Custom type AutoSpeedValue based on Integer32"""
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
        *(("all", 3),
          ("eth1000m", 2),
          ("eth100m", 1),
          ("unknown", 4))
    )





class IpAddressOriginTC(Integer32):
    """Custom type IpAddressOriginTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 4),
          ("linklayer", 5),
          ("manual", 2),
          ("other", 1),
          ("random", 6))
    )





class IPPortStateValue(Integer32):
    """Custom type IPPortStateValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("restart", 3))
    )





class FirewallOnOff(Integer32):
    """Custom type FirewallOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )





class ETHAUTOSPEEDTYPE(Integer32):
    """Custom type ETHAUTOSPEEDTYPE based on Integer32"""
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
        *(("all", 3),
          ("eth1000m", 2),
          ("eth100m", 1),
          ("unknown", 4))
    )





class ETHLINKSTATUS(Integer32):
    """Custom type ETHLINKSTATUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethDown", 2),
          ("ethUp", 1))
    )





class TPMODULEID(Integer32):
    """Custom type TPMODULEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
        *(("exp0", 6),
          ("exp1", 7),
          ("exp2", 8),
          ("exp3", 9),
          ("exp4", 10),
          ("exp5", 11),
          ("exp6", 12),
          ("exp7", 13),
          ("exp8", 14),
          ("exp9", 15),
          ("imc", 1),
          ("ioc1", 2),
          ("ioc2", 3))
    )





class IPV6SCOPE(Integer32):
    """Custom type IPV6SCOPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14)
        )
    )
    namedValues = NamedValues(
        *(("global", 14),
          ("interface-local", 1),
          ("link-local", 2),
          ("site-local", 5))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_NetworkEthStatus_ObjectIdentity = ObjectIdentity
networkEthStatus = _NetworkEthStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1)
)
_NetworkEthLinkTable_Object = MibTable
networkEthLinkTable = _NetworkEthLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    networkEthLinkTable.setStatus("current")
_NetworkEthLinkEntry_Object = MibTableRow
networkEthLinkEntry = _NetworkEthLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1, 1, 1)
)
networkEthLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkEthLinkIndex"),
)
if mibBuilder.loadTexts:
    networkEthLinkEntry.setStatus("current")


class _NetworkEthLinkIndex_Type(Integer32):
    """Custom type networkEthLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkEthLinkIndex_Type.__name__ = "Integer32"
_NetworkEthLinkIndex_Object = MibTableColumn
networkEthLinkIndex = _NetworkEthLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1, 1, 1, 1),
    _NetworkEthLinkIndex_Type()
)
networkEthLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkEthLinkIndex.setStatus("current")
_NetworkEthLinkSpeed_Type = ETHAUTOSPEEDTYPE
_NetworkEthLinkSpeed_Object = MibTableColumn
networkEthLinkSpeed = _NetworkEthLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1, 1, 1, 2),
    _NetworkEthLinkSpeed_Type()
)
networkEthLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEthLinkSpeed.setStatus("current")
_NetworkEthLinkStatus_Type = ETHLINKSTATUS
_NetworkEthLinkStatus_Object = MibTableColumn
networkEthLinkStatus = _NetworkEthLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 1, 1, 1, 3),
    _NetworkEthLinkStatus_Type()
)
networkEthLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEthLinkStatus.setStatus("current")
_NetworkEthConfig_ObjectIdentity = ObjectIdentity
networkEthConfig = _NetworkEthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2)
)
_NetworkEthAutoNegTable_Object = MibTable
networkEthAutoNegTable = _NetworkEthAutoNegTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    networkEthAutoNegTable.setStatus("current")
_NetworkEthAutoNegEntry_Object = MibTableRow
networkEthAutoNegEntry = _NetworkEthAutoNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2, 1, 1)
)
networkEthAutoNegEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkEthAutoNegIndex"),
)
if mibBuilder.loadTexts:
    networkEthAutoNegEntry.setStatus("current")


class _NetworkEthAutoNegIndex_Type(Integer32):
    """Custom type networkEthAutoNegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkEthAutoNegIndex_Type.__name__ = "Integer32"
_NetworkEthAutoNegIndex_Object = MibTableColumn
networkEthAutoNegIndex = _NetworkEthAutoNegIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2, 1, 1, 1),
    _NetworkEthAutoNegIndex_Type()
)
networkEthAutoNegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkEthAutoNegIndex.setStatus("current")
_NetworkEthAutoNegState_Type = EnableValue
_NetworkEthAutoNegState_Object = MibTableColumn
networkEthAutoNegState = _NetworkEthAutoNegState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2, 1, 1, 2),
    _NetworkEthAutoNegState_Type()
)
networkEthAutoNegState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkEthAutoNegState.setStatus("current")
_NetworkEthAutoNegSpeed_Type = AutoSpeedValue
_NetworkEthAutoNegSpeed_Object = MibTableColumn
networkEthAutoNegSpeed = _NetworkEthAutoNegSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 2, 1, 1, 3),
    _NetworkEthAutoNegSpeed_Type()
)
networkEthAutoNegSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkEthAutoNegSpeed.setStatus("current")
_NetworkIpConfig_ObjectIdentity = ObjectIdentity
networkIpConfig = _NetworkIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3)
)
_NetworkIPv4ConfigTable_Object = MibTable
networkIPv4ConfigTable = _NetworkIPv4ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    networkIPv4ConfigTable.setStatus("current")
_NetworkIPv4ConfigEntry_Object = MibTableRow
networkIPv4ConfigEntry = _NetworkIPv4ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1)
)
networkIPv4ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv4ConfigIndex"),
)
if mibBuilder.loadTexts:
    networkIPv4ConfigEntry.setStatus("current")


class _NetworkIPv4ConfigIndex_Type(Integer32):
    """Custom type networkIPv4ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkIPv4ConfigIndex_Type.__name__ = "Integer32"
_NetworkIPv4ConfigIndex_Object = MibTableColumn
networkIPv4ConfigIndex = _NetworkIPv4ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 1),
    _NetworkIPv4ConfigIndex_Type()
)
networkIPv4ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPv4ConfigIndex.setStatus("current")
_NetworkIPv4AddressOrigin_Type = IpAddressOriginTC
_NetworkIPv4AddressOrigin_Object = MibTableColumn
networkIPv4AddressOrigin = _NetworkIPv4AddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 2),
    _NetworkIPv4AddressOrigin_Type()
)
networkIPv4AddressOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv4AddressOrigin.setStatus("current")
_NetworkIPv4Address_Type = IpAddress
_NetworkIPv4Address_Object = MibTableColumn
networkIPv4Address = _NetworkIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 3),
    _NetworkIPv4Address_Type()
)
networkIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv4Address.setStatus("current")
_NetworkIPv4DefaultRouteAddr_Type = IpAddress
_NetworkIPv4DefaultRouteAddr_Object = MibTableColumn
networkIPv4DefaultRouteAddr = _NetworkIPv4DefaultRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 4),
    _NetworkIPv4DefaultRouteAddr_Type()
)
networkIPv4DefaultRouteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv4DefaultRouteAddr.setStatus("current")
_NetworkIPv4SubnetMask_Type = IpAddress
_NetworkIPv4SubnetMask_Object = MibTableColumn
networkIPv4SubnetMask = _NetworkIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 5),
    _NetworkIPv4SubnetMask_Type()
)
networkIPv4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv4SubnetMask.setStatus("current")
_NetworkIPv4PortState_Type = IPPortStateValue
_NetworkIPv4PortState_Object = MibTableColumn
networkIPv4PortState = _NetworkIPv4PortState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 1, 1, 6),
    _NetworkIPv4PortState_Type()
)
networkIPv4PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv4PortState.setStatus("current")
_NetworkIPv4StaticRouteTable_Object = MibTable
networkIPv4StaticRouteTable = _NetworkIPv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    networkIPv4StaticRouteTable.setStatus("current")
_NetworkIPv4StaticRouteEntry_Object = MibTableRow
networkIPv4StaticRouteEntry = _NetworkIPv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1)
)
networkIPv4StaticRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv4StaticRouteIndex"),
)
if mibBuilder.loadTexts:
    networkIPv4StaticRouteEntry.setStatus("current")


class _NetworkIPv4StaticRouteIndex_Type(Integer32):
    """Custom type networkIPv4StaticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_NetworkIPv4StaticRouteIndex_Type.__name__ = "Integer32"
_NetworkIPv4StaticRouteIndex_Object = MibTableColumn
networkIPv4StaticRouteIndex = _NetworkIPv4StaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 1),
    _NetworkIPv4StaticRouteIndex_Type()
)
networkIPv4StaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteIndex.setStatus("current")
_NetworkIPv4StaticRouteIfindex_Type = Integer32
_NetworkIPv4StaticRouteIfindex_Object = MibTableColumn
networkIPv4StaticRouteIfindex = _NetworkIPv4StaticRouteIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 2),
    _NetworkIPv4StaticRouteIfindex_Type()
)
networkIPv4StaticRouteIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteIfindex.setStatus("current")
_NetworkIPv4StaticDestAddr_Type = IpAddress
_NetworkIPv4StaticDestAddr_Object = MibTableColumn
networkIPv4StaticDestAddr = _NetworkIPv4StaticDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 3),
    _NetworkIPv4StaticDestAddr_Type()
)
networkIPv4StaticDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticDestAddr.setStatus("current")
_NetworkIPv4StaticRouteMask_Type = IpAddress
_NetworkIPv4StaticRouteMask_Object = MibTableColumn
networkIPv4StaticRouteMask = _NetworkIPv4StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 4),
    _NetworkIPv4StaticRouteMask_Type()
)
networkIPv4StaticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteMask.setStatus("current")
_NetworkIPv4StaticRouteNextHop_Type = IpAddress
_NetworkIPv4StaticRouteNextHop_Object = MibTableColumn
networkIPv4StaticRouteNextHop = _NetworkIPv4StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 5),
    _NetworkIPv4StaticRouteNextHop_Type()
)
networkIPv4StaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteNextHop.setStatus("current")


class _NetworkIPv4StaticRouteMetric1_Type(Integer32):
    """Custom type networkIPv4StaticRouteMetric1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_NetworkIPv4StaticRouteMetric1_Type.__name__ = "Integer32"
_NetworkIPv4StaticRouteMetric1_Object = MibTableColumn
networkIPv4StaticRouteMetric1 = _NetworkIPv4StaticRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 6),
    _NetworkIPv4StaticRouteMetric1_Type()
)
networkIPv4StaticRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteMetric1.setStatus("current")
_NetworkIPv4StaticRouteRowStatus_Type = RowStatus
_NetworkIPv4StaticRouteRowStatus_Object = MibTableColumn
networkIPv4StaticRouteRowStatus = _NetworkIPv4StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 2, 1, 7),
    _NetworkIPv4StaticRouteRowStatus_Type()
)
networkIPv4StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv4StaticRouteRowStatus.setStatus("current")
_NetworkFirewallTable_Object = MibTable
networkFirewallTable = _NetworkFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    networkFirewallTable.setStatus("current")
_NetworkFirewallEntry_Object = MibTableRow
networkFirewallEntry = _NetworkFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1)
)
networkFirewallEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkFirewallIndex"),
)
if mibBuilder.loadTexts:
    networkFirewallEntry.setStatus("current")


class _NetworkFirewallIndex_Type(Integer32):
    """Custom type networkFirewallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkFirewallIndex_Type.__name__ = "Integer32"
_NetworkFirewallIndex_Object = MibTableColumn
networkFirewallIndex = _NetworkFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 1),
    _NetworkFirewallIndex_Type()
)
networkFirewallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkFirewallIndex.setStatus("current")
_NetworkFirewallICMP_Type = FirewallOnOff
_NetworkFirewallICMP_Object = MibTableColumn
networkFirewallICMP = _NetworkFirewallICMP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 2),
    _NetworkFirewallICMP_Type()
)
networkFirewallICMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallICMP.setStatus("current")
_NetworkFirewallTelnet_Type = FirewallOnOff
_NetworkFirewallTelnet_Object = MibTableColumn
networkFirewallTelnet = _NetworkFirewallTelnet_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 3),
    _NetworkFirewallTelnet_Type()
)
networkFirewallTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallTelnet.setStatus("current")
_NetworkFirewallSSH_Type = FirewallOnOff
_NetworkFirewallSSH_Object = MibTableColumn
networkFirewallSSH = _NetworkFirewallSSH_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 4),
    _NetworkFirewallSSH_Type()
)
networkFirewallSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallSSH.setStatus("current")
_NetworkFirewallSFTP_Type = FirewallOnOff
_NetworkFirewallSFTP_Object = MibTableColumn
networkFirewallSFTP = _NetworkFirewallSFTP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 5),
    _NetworkFirewallSFTP_Type()
)
networkFirewallSFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallSFTP.setStatus("current")
_NetworkFirewallSNMP_Type = FirewallOnOff
_NetworkFirewallSNMP_Object = MibTableColumn
networkFirewallSNMP = _NetworkFirewallSNMP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 6),
    _NetworkFirewallSNMP_Type()
)
networkFirewallSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallSNMP.setStatus("current")
_NetworkFirewallFTP_Type = FirewallOnOff
_NetworkFirewallFTP_Object = MibTableColumn
networkFirewallFTP = _NetworkFirewallFTP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 7),
    _NetworkFirewallFTP_Type()
)
networkFirewallFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallFTP.setStatus("current")
_NetworkFirewallNTP_Type = FirewallOnOff
_NetworkFirewallNTP_Object = MibTableColumn
networkFirewallNTP = _NetworkFirewallNTP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 3, 1, 8),
    _NetworkFirewallNTP_Type()
)
networkFirewallNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkFirewallNTP.setStatus("current")
_NetworkIPv6ConfigTable_Object = MibTable
networkIPv6ConfigTable = _NetworkIPv6ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    networkIPv6ConfigTable.setStatus("current")
_NetworkIPv6ConfigEntry_Object = MibTableRow
networkIPv6ConfigEntry = _NetworkIPv6ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1)
)
networkIPv6ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv6ConfigIndex"),
)
if mibBuilder.loadTexts:
    networkIPv6ConfigEntry.setStatus("current")


class _NetworkIPv6ConfigIndex_Type(Integer32):
    """Custom type networkIPv6ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkIPv6ConfigIndex_Type.__name__ = "Integer32"
_NetworkIPv6ConfigIndex_Object = MibTableColumn
networkIPv6ConfigIndex = _NetworkIPv6ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 1),
    _NetworkIPv6ConfigIndex_Type()
)
networkIPv6ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPv6ConfigIndex.setStatus("current")
_NetworkIPv6AddressOrigin_Type = IpAddressOriginTC
_NetworkIPv6AddressOrigin_Object = MibTableColumn
networkIPv6AddressOrigin = _NetworkIPv6AddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 2),
    _NetworkIPv6AddressOrigin_Type()
)
networkIPv6AddressOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6AddressOrigin.setStatus("current")
_NetworkIPv6Address_Type = InetAddressIPv6
_NetworkIPv6Address_Object = MibTableColumn
networkIPv6Address = _NetworkIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 3),
    _NetworkIPv6Address_Type()
)
networkIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6Address.setStatus("current")


class _NetworkIPv6Prefix_Type(Integer32):
    """Custom type networkIPv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NetworkIPv6Prefix_Type.__name__ = "Integer32"
_NetworkIPv6Prefix_Object = MibTableColumn
networkIPv6Prefix = _NetworkIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 4),
    _NetworkIPv6Prefix_Type()
)
networkIPv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6Prefix.setStatus("current")
_NetworkIPv6DefaultRouteAddr_Type = InetAddressIPv6
_NetworkIPv6DefaultRouteAddr_Object = MibTableColumn
networkIPv6DefaultRouteAddr = _NetworkIPv6DefaultRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 5),
    _NetworkIPv6DefaultRouteAddr_Type()
)
networkIPv6DefaultRouteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6DefaultRouteAddr.setStatus("current")
_NetworkIPv6PortState_Type = IPPortStateValue
_NetworkIPv6PortState_Object = MibTableColumn
networkIPv6PortState = _NetworkIPv6PortState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 4, 1, 6),
    _NetworkIPv6PortState_Type()
)
networkIPv6PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6PortState.setStatus("current")
_NetworkIPv6StaticRouteTable_Object = MibTable
networkIPv6StaticRouteTable = _NetworkIPv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    networkIPv6StaticRouteTable.setStatus("current")
_NetworkIPv6StaticRouteEntry_Object = MibTableRow
networkIPv6StaticRouteEntry = _NetworkIPv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1)
)
networkIPv6StaticRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv6StaticRouteIndex"),
)
if mibBuilder.loadTexts:
    networkIPv6StaticRouteEntry.setStatus("current")


class _NetworkIPv6StaticRouteIndex_Type(Integer32):
    """Custom type networkIPv6StaticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_NetworkIPv6StaticRouteIndex_Type.__name__ = "Integer32"
_NetworkIPv6StaticRouteIndex_Object = MibTableColumn
networkIPv6StaticRouteIndex = _NetworkIPv6StaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 1),
    _NetworkIPv6StaticRouteIndex_Type()
)
networkIPv6StaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteIndex.setStatus("current")
_NetworkIPv6StaticRouteIfindex_Type = Integer32
_NetworkIPv6StaticRouteIfindex_Object = MibTableColumn
networkIPv6StaticRouteIfindex = _NetworkIPv6StaticRouteIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 2),
    _NetworkIPv6StaticRouteIfindex_Type()
)
networkIPv6StaticRouteIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteIfindex.setStatus("current")
_NetworkIPv6StaticRouteDestAddr_Type = InetAddressIPv6
_NetworkIPv6StaticRouteDestAddr_Object = MibTableColumn
networkIPv6StaticRouteDestAddr = _NetworkIPv6StaticRouteDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 3),
    _NetworkIPv6StaticRouteDestAddr_Type()
)
networkIPv6StaticRouteDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteDestAddr.setStatus("current")


class _NetworkIPv6StaticRoutePrefix_Type(Integer32):
    """Custom type networkIPv6StaticRoutePrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_NetworkIPv6StaticRoutePrefix_Type.__name__ = "Integer32"
_NetworkIPv6StaticRoutePrefix_Object = MibTableColumn
networkIPv6StaticRoutePrefix = _NetworkIPv6StaticRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 4),
    _NetworkIPv6StaticRoutePrefix_Type()
)
networkIPv6StaticRoutePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRoutePrefix.setStatus("current")
_NetworkIPv6StaticRouteNextHop_Type = InetAddressIPv6z
_NetworkIPv6StaticRouteNextHop_Object = MibTableColumn
networkIPv6StaticRouteNextHop = _NetworkIPv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 5),
    _NetworkIPv6StaticRouteNextHop_Type()
)
networkIPv6StaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteNextHop.setStatus("current")


class _NetworkIPv6StaticRouteMetric1_Type(Integer32):
    """Custom type networkIPv6StaticRouteMetric1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )


_NetworkIPv6StaticRouteMetric1_Type.__name__ = "Integer32"
_NetworkIPv6StaticRouteMetric1_Object = MibTableColumn
networkIPv6StaticRouteMetric1 = _NetworkIPv6StaticRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 6),
    _NetworkIPv6StaticRouteMetric1_Type()
)
networkIPv6StaticRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteMetric1.setStatus("current")
_NetworkIPv6StaticRouteRowStatus_Type = RowStatus
_NetworkIPv6StaticRouteRowStatus_Object = MibTableColumn
networkIPv6StaticRouteRowStatus = _NetworkIPv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 5, 1, 7),
    _NetworkIPv6StaticRouteRowStatus_Type()
)
networkIPv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkIPv6StaticRouteRowStatus.setStatus("current")
_NetworkIPVerTable_Object = MibTable
networkIPVerTable = _NetworkIPVerTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    networkIPVerTable.setStatus("current")
_NetworkIPVerEntry_Object = MibTableRow
networkIPVerEntry = _NetworkIPVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 6, 1)
)
networkIPVerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPVerIndex"),
)
if mibBuilder.loadTexts:
    networkIPVerEntry.setStatus("current")


class _NetworkIPVerIndex_Type(Integer32):
    """Custom type networkIPVerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkIPVerIndex_Type.__name__ = "Integer32"
_NetworkIPVerIndex_Object = MibTableColumn
networkIPVerIndex = _NetworkIPVerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 6, 1, 1),
    _NetworkIPVerIndex_Type()
)
networkIPVerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPVerIndex.setStatus("current")
_NetworkIPVersion_Type = InetAddressType
_NetworkIPVersion_Object = MibTableColumn
networkIPVersion = _NetworkIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 6, 1, 2),
    _NetworkIPVersion_Type()
)
networkIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPVersion.setStatus("current")
_NetworkIPv6AutoConfigTable_Object = MibTable
networkIPv6AutoConfigTable = _NetworkIPv6AutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 7)
)
if mibBuilder.loadTexts:
    networkIPv6AutoConfigTable.setStatus("current")
_NetworkIPv6AutoConfigEntry_Object = MibTableRow
networkIPv6AutoConfigEntry = _NetworkIPv6AutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 7, 1)
)
networkIPv6AutoConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv6AutoConfigIndex"),
)
if mibBuilder.loadTexts:
    networkIPv6AutoConfigEntry.setStatus("current")


class _NetworkIPv6AutoConfigIndex_Type(Integer32):
    """Custom type networkIPv6AutoConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NetworkIPv6AutoConfigIndex_Type.__name__ = "Integer32"
_NetworkIPv6AutoConfigIndex_Object = MibTableColumn
networkIPv6AutoConfigIndex = _NetworkIPv6AutoConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 7, 1, 1),
    _NetworkIPv6AutoConfigIndex_Type()
)
networkIPv6AutoConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPv6AutoConfigIndex.setStatus("current")
_NetworkIPv6AutoConfigMode_Type = EnableValue
_NetworkIPv6AutoConfigMode_Object = MibTableColumn
networkIPv6AutoConfigMode = _NetworkIPv6AutoConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 3, 7, 1, 2),
    _NetworkIPv6AutoConfigMode_Type()
)
networkIPv6AutoConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkIPv6AutoConfigMode.setStatus("current")
_NetworkVlanConfig_ObjectIdentity = ObjectIdentity
networkVlanConfig = _NetworkVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 4)
)
_NetworkIPStatus_ObjectIdentity = ObjectIdentity
networkIPStatus = _NetworkIPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5)
)
_NetworkIPv4StatusTable_Object = MibTable
networkIPv4StatusTable = _NetworkIPv4StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    networkIPv4StatusTable.setStatus("current")
_NetworkIPv4StatusEntry_Object = MibTableRow
networkIPv4StatusEntry = _NetworkIPv4StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1)
)
networkIPv4StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv4StatusIndex"),
)
if mibBuilder.loadTexts:
    networkIPv4StatusEntry.setStatus("current")


class _NetworkIPv4StatusIndex_Type(Integer32):
    """Custom type networkIPv4StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkIPv4StatusIndex_Type.__name__ = "Integer32"
_NetworkIPv4StatusIndex_Object = MibTableColumn
networkIPv4StatusIndex = _NetworkIPv4StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 1),
    _NetworkIPv4StatusIndex_Type()
)
networkIPv4StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPv4StatusIndex.setStatus("current")
_NetworkIPv4Module_Type = TPMODULEID
_NetworkIPv4Module_Object = MibTableColumn
networkIPv4Module = _NetworkIPv4Module_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 2),
    _NetworkIPv4Module_Type()
)
networkIPv4Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4Module.setStatus("current")


class _NetworkIPv4VlanID_Type(Integer32):
    """Custom type networkIPv4VlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NetworkIPv4VlanID_Type.__name__ = "Integer32"
_NetworkIPv4VlanID_Object = MibTableColumn
networkIPv4VlanID = _NetworkIPv4VlanID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 3),
    _NetworkIPv4VlanID_Type()
)
networkIPv4VlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4VlanID.setStatus("current")
_NetworkIPv4Addr_Type = InetAddressIPv4
_NetworkIPv4Addr_Object = MibTableColumn
networkIPv4Addr = _NetworkIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 4),
    _NetworkIPv4Addr_Type()
)
networkIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4Addr.setStatus("current")
_NetworkIPv4Netmask_Type = InetAddressIPv4
_NetworkIPv4Netmask_Object = MibTableColumn
networkIPv4Netmask = _NetworkIPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 5),
    _NetworkIPv4Netmask_Type()
)
networkIPv4Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4Netmask.setStatus("current")
_NetworkIPv4RouteAddr_Type = InetAddressIPv4
_NetworkIPv4RouteAddr_Object = MibTableColumn
networkIPv4RouteAddr = _NetworkIPv4RouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 6),
    _NetworkIPv4RouteAddr_Type()
)
networkIPv4RouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4RouteAddr.setStatus("current")
_NetworkIPv4Mode_Type = IpAddressOriginTC
_NetworkIPv4Mode_Object = MibTableColumn
networkIPv4Mode = _NetworkIPv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 1, 1, 7),
    _NetworkIPv4Mode_Type()
)
networkIPv4Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv4Mode.setStatus("current")
_NetworkIPv6StatusTable_Object = MibTable
networkIPv6StatusTable = _NetworkIPv6StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    networkIPv6StatusTable.setStatus("current")
_NetworkIPv6StatusEntry_Object = MibTableRow
networkIPv6StatusEntry = _NetworkIPv6StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1)
)
networkIPv6StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONNETWORK", "networkIPv6StatusIndex"),
)
if mibBuilder.loadTexts:
    networkIPv6StatusEntry.setStatus("current")


class _NetworkIPv6StatusIndex_Type(Integer32):
    """Custom type networkIPv6StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NetworkIPv6StatusIndex_Type.__name__ = "Integer32"
_NetworkIPv6StatusIndex_Object = MibTableColumn
networkIPv6StatusIndex = _NetworkIPv6StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 1),
    _NetworkIPv6StatusIndex_Type()
)
networkIPv6StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkIPv6StatusIndex.setStatus("current")
_NetworkIPv6Module_Type = TPMODULEID
_NetworkIPv6Module_Object = MibTableColumn
networkIPv6Module = _NetworkIPv6Module_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 2),
    _NetworkIPv6Module_Type()
)
networkIPv6Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6Module.setStatus("current")


class _NetworkIPv6VlanID_Type(Integer32):
    """Custom type networkIPv6VlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_NetworkIPv6VlanID_Type.__name__ = "Integer32"
_NetworkIPv6VlanID_Object = MibTableColumn
networkIPv6VlanID = _NetworkIPv6VlanID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 3),
    _NetworkIPv6VlanID_Type()
)
networkIPv6VlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6VlanID.setStatus("current")
_NetworkIPv6Addr_Type = InetAddressIPv6
_NetworkIPv6Addr_Object = MibTableColumn
networkIPv6Addr = _NetworkIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 4),
    _NetworkIPv6Addr_Type()
)
networkIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6Addr.setStatus("current")
_NetworkIPv6PrefixLength_Type = InetAddressPrefixLength
_NetworkIPv6PrefixLength_Object = MibTableColumn
networkIPv6PrefixLength = _NetworkIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 5),
    _NetworkIPv6PrefixLength_Type()
)
networkIPv6PrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6PrefixLength.setStatus("current")
_NetworkIPv6AddrScope_Type = IPV6SCOPE
_NetworkIPv6AddrScope_Object = MibTableColumn
networkIPv6AddrScope = _NetworkIPv6AddrScope_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 6),
    _NetworkIPv6AddrScope_Type()
)
networkIPv6AddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6AddrScope.setStatus("current")
_NetworkIPv6Mode_Type = IpAddressOriginTC
_NetworkIPv6Mode_Object = MibTableColumn
networkIPv6Mode = _NetworkIPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 5, 2, 1, 7),
    _NetworkIPv6Mode_Type()
)
networkIPv6Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIPv6Mode.setStatus("current")
_NetworkConformance_ObjectIdentity = ObjectIdentity
networkConformance = _NetworkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6)
)
if mibBuilder.loadTexts:
    networkConformance.setStatus("current")
_NetworkCompliances_ObjectIdentity = ObjectIdentity
networkCompliances = _NetworkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 1)
)
_NetworkUocGroups_ObjectIdentity = ObjectIdentity
networkUocGroups = _NetworkUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2)
)

# Managed Objects groups

networkEthAutoNetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 1)
)
networkEthAutoNetGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkEthAutoNegState"),
        ("SYMMCOMMONNETWORK", "networkEthAutoNegSpeed"))
)
if mibBuilder.loadTexts:
    networkEthAutoNetGroup.setStatus("current")

networkIPv4ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 2)
)
networkIPv4ConfigGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv4AddressOrigin"),
        ("SYMMCOMMONNETWORK", "networkIPv4Address"),
        ("SYMMCOMMONNETWORK", "networkIPv4DefaultRouteAddr"),
        ("SYMMCOMMONNETWORK", "networkIPv4SubnetMask"),
        ("SYMMCOMMONNETWORK", "networkIPv4PortState"))
)
if mibBuilder.loadTexts:
    networkIPv4ConfigGroup.setStatus("current")

networkFirewallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 3)
)
networkFirewallGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkFirewallICMP"),
        ("SYMMCOMMONNETWORK", "networkFirewallTelnet"),
        ("SYMMCOMMONNETWORK", "networkFirewallSSH"),
        ("SYMMCOMMONNETWORK", "networkFirewallSFTP"),
        ("SYMMCOMMONNETWORK", "networkFirewallSNMP"),
        ("SYMMCOMMONNETWORK", "networkFirewallFTP"))
)
if mibBuilder.loadTexts:
    networkFirewallGroup.setStatus("current")

networkIPv4StaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 4)
)
networkIPv4StaticRouteGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv4StaticRouteIndex"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticDestAddr"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticRouteMask"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticRouteNextHop"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticRouteMetric1"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticRouteRowStatus"),
        ("SYMMCOMMONNETWORK", "networkIPv4StaticRouteIfindex"))
)
if mibBuilder.loadTexts:
    networkIPv4StaticRouteGroup.setStatus("current")

networkEthStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 5)
)
networkEthStatusGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkEthLinkSpeed"),
        ("SYMMCOMMONNETWORK", "networkEthLinkStatus"))
)
if mibBuilder.loadTexts:
    networkEthStatusGroup.setStatus("current")

networkIPv6ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 6)
)
networkIPv6ConfigGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv6AddressOrigin"),
        ("SYMMCOMMONNETWORK", "networkIPv6Address"),
        ("SYMMCOMMONNETWORK", "networkIPv6Prefix"),
        ("SYMMCOMMONNETWORK", "networkIPv6DefaultRouteAddr"),
        ("SYMMCOMMONNETWORK", "networkIPv6PortState"))
)
if mibBuilder.loadTexts:
    networkIPv6ConfigGroup.setStatus("current")

networkIPv6StaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 7)
)
networkIPv6StaticRouteGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv6StaticRouteDestAddr"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRoutePrefix"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRouteNextHop"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRouteMetric1"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRouteIndex"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRouteRowStatus"),
        ("SYMMCOMMONNETWORK", "networkIPv6StaticRouteIfindex"))
)
if mibBuilder.loadTexts:
    networkIPv6StaticRouteGroup.setStatus("current")

networkIPVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 8)
)
networkIPVersionGroup.setObjects(
    ("SYMMCOMMONNETWORK", "networkIPVersion")
)
if mibBuilder.loadTexts:
    networkIPVersionGroup.setStatus("current")

networkIPv6AutoConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 9)
)
networkIPv6AutoConfigGroup.setObjects(
    ("SYMMCOMMONNETWORK", "networkIPv6AutoConfigMode")
)
if mibBuilder.loadTexts:
    networkIPv6AutoConfigGroup.setStatus("current")

networkIPv4StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 10)
)
networkIPv4StatusGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv4Module"),
        ("SYMMCOMMONNETWORK", "networkIPv4RouteAddr"),
        ("SYMMCOMMONNETWORK", "networkIPv4Netmask"),
        ("SYMMCOMMONNETWORK", "networkIPv4Addr"))
)
if mibBuilder.loadTexts:
    networkIPv4StatusGroup.setStatus("current")

networkIPv6StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 2, 11)
)
networkIPv6StatusGroup.setObjects(
      *(("SYMMCOMMONNETWORK", "networkIPv6Module"),
        ("SYMMCOMMONNETWORK", "networkIPv6Addr"),
        ("SYMMCOMMONNETWORK", "networkIPv6AddrScope"),
        ("SYMMCOMMONNETWORK", "networkIPv6Mode"),
        ("SYMMCOMMONNETWORK", "networkIPv6PrefixLength"))
)
if mibBuilder.loadTexts:
    networkIPv6StatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

networkBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 4, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    networkBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMCOMMONNETWORK",
    **{"AutoSpeedValue": AutoSpeedValue,
       "IpAddressOriginTC": IpAddressOriginTC,
       "IPPortStateValue": IPPortStateValue,
       "FirewallOnOff": FirewallOnOff,
       "ETHAUTOSPEEDTYPE": ETHAUTOSPEEDTYPE,
       "ETHLINKSTATUS": ETHLINKSTATUS,
       "TPMODULEID": TPMODULEID,
       "IPV6SCOPE": IPV6SCOPE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmCommonNetwork": symmCommonNetwork,
       "networkEthStatus": networkEthStatus,
       "networkEthLinkTable": networkEthLinkTable,
       "networkEthLinkEntry": networkEthLinkEntry,
       "networkEthLinkIndex": networkEthLinkIndex,
       "networkEthLinkSpeed": networkEthLinkSpeed,
       "networkEthLinkStatus": networkEthLinkStatus,
       "networkEthConfig": networkEthConfig,
       "networkEthAutoNegTable": networkEthAutoNegTable,
       "networkEthAutoNegEntry": networkEthAutoNegEntry,
       "networkEthAutoNegIndex": networkEthAutoNegIndex,
       "networkEthAutoNegState": networkEthAutoNegState,
       "networkEthAutoNegSpeed": networkEthAutoNegSpeed,
       "networkIpConfig": networkIpConfig,
       "networkIPv4ConfigTable": networkIPv4ConfigTable,
       "networkIPv4ConfigEntry": networkIPv4ConfigEntry,
       "networkIPv4ConfigIndex": networkIPv4ConfigIndex,
       "networkIPv4AddressOrigin": networkIPv4AddressOrigin,
       "networkIPv4Address": networkIPv4Address,
       "networkIPv4DefaultRouteAddr": networkIPv4DefaultRouteAddr,
       "networkIPv4SubnetMask": networkIPv4SubnetMask,
       "networkIPv4PortState": networkIPv4PortState,
       "networkIPv4StaticRouteTable": networkIPv4StaticRouteTable,
       "networkIPv4StaticRouteEntry": networkIPv4StaticRouteEntry,
       "networkIPv4StaticRouteIndex": networkIPv4StaticRouteIndex,
       "networkIPv4StaticRouteIfindex": networkIPv4StaticRouteIfindex,
       "networkIPv4StaticDestAddr": networkIPv4StaticDestAddr,
       "networkIPv4StaticRouteMask": networkIPv4StaticRouteMask,
       "networkIPv4StaticRouteNextHop": networkIPv4StaticRouteNextHop,
       "networkIPv4StaticRouteMetric1": networkIPv4StaticRouteMetric1,
       "networkIPv4StaticRouteRowStatus": networkIPv4StaticRouteRowStatus,
       "networkFirewallTable": networkFirewallTable,
       "networkFirewallEntry": networkFirewallEntry,
       "networkFirewallIndex": networkFirewallIndex,
       "networkFirewallICMP": networkFirewallICMP,
       "networkFirewallTelnet": networkFirewallTelnet,
       "networkFirewallSSH": networkFirewallSSH,
       "networkFirewallSFTP": networkFirewallSFTP,
       "networkFirewallSNMP": networkFirewallSNMP,
       "networkFirewallFTP": networkFirewallFTP,
       "networkFirewallNTP": networkFirewallNTP,
       "networkIPv6ConfigTable": networkIPv6ConfigTable,
       "networkIPv6ConfigEntry": networkIPv6ConfigEntry,
       "networkIPv6ConfigIndex": networkIPv6ConfigIndex,
       "networkIPv6AddressOrigin": networkIPv6AddressOrigin,
       "networkIPv6Address": networkIPv6Address,
       "networkIPv6Prefix": networkIPv6Prefix,
       "networkIPv6DefaultRouteAddr": networkIPv6DefaultRouteAddr,
       "networkIPv6PortState": networkIPv6PortState,
       "networkIPv6StaticRouteTable": networkIPv6StaticRouteTable,
       "networkIPv6StaticRouteEntry": networkIPv6StaticRouteEntry,
       "networkIPv6StaticRouteIndex": networkIPv6StaticRouteIndex,
       "networkIPv6StaticRouteIfindex": networkIPv6StaticRouteIfindex,
       "networkIPv6StaticRouteDestAddr": networkIPv6StaticRouteDestAddr,
       "networkIPv6StaticRoutePrefix": networkIPv6StaticRoutePrefix,
       "networkIPv6StaticRouteNextHop": networkIPv6StaticRouteNextHop,
       "networkIPv6StaticRouteMetric1": networkIPv6StaticRouteMetric1,
       "networkIPv6StaticRouteRowStatus": networkIPv6StaticRouteRowStatus,
       "networkIPVerTable": networkIPVerTable,
       "networkIPVerEntry": networkIPVerEntry,
       "networkIPVerIndex": networkIPVerIndex,
       "networkIPVersion": networkIPVersion,
       "networkIPv6AutoConfigTable": networkIPv6AutoConfigTable,
       "networkIPv6AutoConfigEntry": networkIPv6AutoConfigEntry,
       "networkIPv6AutoConfigIndex": networkIPv6AutoConfigIndex,
       "networkIPv6AutoConfigMode": networkIPv6AutoConfigMode,
       "networkVlanConfig": networkVlanConfig,
       "networkIPStatus": networkIPStatus,
       "networkIPv4StatusTable": networkIPv4StatusTable,
       "networkIPv4StatusEntry": networkIPv4StatusEntry,
       "networkIPv4StatusIndex": networkIPv4StatusIndex,
       "networkIPv4Module": networkIPv4Module,
       "networkIPv4VlanID": networkIPv4VlanID,
       "networkIPv4Addr": networkIPv4Addr,
       "networkIPv4Netmask": networkIPv4Netmask,
       "networkIPv4RouteAddr": networkIPv4RouteAddr,
       "networkIPv4Mode": networkIPv4Mode,
       "networkIPv6StatusTable": networkIPv6StatusTable,
       "networkIPv6StatusEntry": networkIPv6StatusEntry,
       "networkIPv6StatusIndex": networkIPv6StatusIndex,
       "networkIPv6Module": networkIPv6Module,
       "networkIPv6VlanID": networkIPv6VlanID,
       "networkIPv6Addr": networkIPv6Addr,
       "networkIPv6PrefixLength": networkIPv6PrefixLength,
       "networkIPv6AddrScope": networkIPv6AddrScope,
       "networkIPv6Mode": networkIPv6Mode,
       "networkConformance": networkConformance,
       "networkCompliances": networkCompliances,
       "networkBasicCompliance": networkBasicCompliance,
       "networkUocGroups": networkUocGroups,
       "networkEthAutoNetGroup": networkEthAutoNetGroup,
       "networkIPv4ConfigGroup": networkIPv4ConfigGroup,
       "networkFirewallGroup": networkFirewallGroup,
       "networkIPv4StaticRouteGroup": networkIPv4StaticRouteGroup,
       "networkEthStatusGroup": networkEthStatusGroup,
       "networkIPv6ConfigGroup": networkIPv6ConfigGroup,
       "networkIPv6StaticRouteGroup": networkIPv6StaticRouteGroup,
       "networkIPVersionGroup": networkIPVersionGroup,
       "networkIPv6AutoConfigGroup": networkIPv6AutoConfigGroup,
       "networkIPv4StatusGroup": networkIPv4StatusGroup,
       "networkIPv6StatusGroup": networkIPv6StatusGroup}
)
