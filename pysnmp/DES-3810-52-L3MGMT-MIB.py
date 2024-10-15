# SNMP MIB module (DES-3810-52-L3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES-3810-52-L3MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:44 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 PositiveInteger,
 RouterID,
 Status,
 TOSType,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "RouterID",
    "Status",
    "TOSType",
    "UpToMaxAge")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(des3810_52,) = mibBuilder.importSymbols(
    "SW3810PRIMGMT-MIB",
    "des3810-52")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3)
)


# Types definitions



class NodeAddress(OctetString):
    """Custom type NodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class NetAddress(OctetString):
    """Custom type NetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



class VrId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SwL3DevMgmt_ObjectIdentity = ObjectIdentity
swL3DevMgmt = _SwL3DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1)
)
_SwL3DevCtrl_ObjectIdentity = ObjectIdentity
swL3DevCtrl = _SwL3DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1, 1)
)


class _SwL3DevCtrlRIPState_Type(Integer32):
    """Custom type swL3DevCtrlRIPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlRIPState_Type.__name__ = "Integer32"
_SwL3DevCtrlRIPState_Object = MibScalar
swL3DevCtrlRIPState = _SwL3DevCtrlRIPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1, 1, 1),
    _SwL3DevCtrlRIPState_Type()
)
swL3DevCtrlRIPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlRIPState.setStatus("current")


class _SwL3DevCtrlOSPFState_Type(Integer32):
    """Custom type swL3DevCtrlOSPFState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlOSPFState_Type.__name__ = "Integer32"
_SwL3DevCtrlOSPFState_Object = MibScalar
swL3DevCtrlOSPFState = _SwL3DevCtrlOSPFState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1, 1, 2),
    _SwL3DevCtrlOSPFState_Type()
)
swL3DevCtrlOSPFState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlOSPFState.setStatus("current")


class _SwL3DevCtrlVRRPState_Type(Integer32):
    """Custom type swL3DevCtrlVRRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlVRRPState_Type.__name__ = "Integer32"
_SwL3DevCtrlVRRPState_Object = MibScalar
swL3DevCtrlVRRPState = _SwL3DevCtrlVRRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1, 1, 5),
    _SwL3DevCtrlVRRPState_Type()
)
swL3DevCtrlVRRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVRRPState.setStatus("current")


class _SwL3DevCtrlVrrpPingState_Type(Integer32):
    """Custom type swL3DevCtrlVrrpPingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3DevCtrlVrrpPingState_Type.__name__ = "Integer32"
_SwL3DevCtrlVrrpPingState_Object = MibScalar
swL3DevCtrlVrrpPingState = _SwL3DevCtrlVrrpPingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 1, 1, 6),
    _SwL3DevCtrlVrrpPingState_Type()
)
swL3DevCtrlVrrpPingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3DevCtrlVrrpPingState.setStatus("current")
_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3IpCtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3IpCtrlEntry.setStatus("current")


class _SwL3IpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3IpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3IpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3IpCtrlInterfaceName_Object = MibTableColumn
swL3IpCtrlInterfaceName = _SwL3IpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 1),
    _SwL3IpCtrlInterfaceName_Type()
)
swL3IpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlInterfaceName.setStatus("current")


class _SwL3IpCtrlIfIndex_Type(Integer32):
    """Custom type swL3IpCtrlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpCtrlIfIndex_Type.__name__ = "Integer32"
_SwL3IpCtrlIfIndex_Object = MibTableColumn
swL3IpCtrlIfIndex = _SwL3IpCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 4),
    _SwL3IpCtrlIpSubnetMask_Type()
)
swL3IpCtrlIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpSubnetMask.setStatus("current")


class _SwL3IpCtrlVlanName_Type(DisplayString):
    """Custom type swL3IpCtrlVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL3IpCtrlVlanName_Type.__name__ = "DisplayString"
_SwL3IpCtrlVlanName_Object = MibTableColumn
swL3IpCtrlVlanName = _SwL3IpCtrlVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 5),
    _SwL3IpCtrlVlanName_Type()
)
swL3IpCtrlVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlVlanName.setStatus("current")


class _SwL3IpCtrlProxyArp_Type(Integer32):
    """Custom type swL3IpCtrlProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3IpCtrlProxyArp_Type.__name__ = "Integer32"
_SwL3IpCtrlProxyArp_Object = MibTableColumn
swL3IpCtrlProxyArp = _SwL3IpCtrlProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 6),
    _SwL3IpCtrlProxyArp_Type()
)
swL3IpCtrlProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlProxyArp.setStatus("current")
_SwL3IpCtrlSecondary_Type = TruthValue
_SwL3IpCtrlSecondary_Object = MibTableColumn
swL3IpCtrlSecondary = _SwL3IpCtrlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 7),
    _SwL3IpCtrlSecondary_Type()
)
swL3IpCtrlSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlSecondary.setStatus("current")


class _SwL3IpCtrlMode_Type(Integer32):
    """Custom type swL3IpCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 3),
          ("dhcp", 4),
          ("other", 1))
    )


_SwL3IpCtrlMode_Type.__name__ = "Integer32"
_SwL3IpCtrlMode_Object = MibTableColumn
swL3IpCtrlMode = _SwL3IpCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 8),
    _SwL3IpCtrlMode_Type()
)
swL3IpCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlMode.setStatus("current")


class _SwL3IpCtrlAdminState_Type(Integer32):
    """Custom type swL3IpCtrlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3IpCtrlAdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlAdminState_Object = MibTableColumn
swL3IpCtrlAdminState = _SwL3IpCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 9),
    _SwL3IpCtrlAdminState_Type()
)
swL3IpCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAdminState.setStatus("current")


class _SwL3IpCtrlIpv4AdminState_Type(Integer32):
    """Custom type swL3IpCtrlIpv4AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3IpCtrlIpv4AdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv4AdminState_Object = MibTableColumn
swL3IpCtrlIpv4AdminState = _SwL3IpCtrlIpv4AdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 10),
    _SwL3IpCtrlIpv4AdminState_Type()
)
swL3IpCtrlIpv4AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv4AdminState.setStatus("current")


class _SwL3IpCtrlIpv6AdminState_Type(Integer32):
    """Custom type swL3IpCtrlIpv6AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3IpCtrlIpv6AdminState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv6AdminState_Object = MibTableColumn
swL3IpCtrlIpv6AdminState = _SwL3IpCtrlIpv6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 12),
    _SwL3IpCtrlIpv6AdminState_Type()
)
swL3IpCtrlIpv6AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 16),
    _SwL3IpCtrlState_Type()
)
swL3IpCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlState.setStatus("current")


class _SwL3IpCtrlIpv6LinkLocalAutoState_Type(Integer32):
    """Custom type swL3IpCtrlIpv6LinkLocalAutoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SwL3IpCtrlIpv6LinkLocalAutoState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv6LinkLocalAutoState_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAutoState = _SwL3IpCtrlIpv6LinkLocalAutoState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 17),
    _SwL3IpCtrlIpv6LinkLocalAutoState_Type()
)
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAutoState.setStatus("current")


class _SwL3IpCtrlLocalProxyArp_Type(Integer32):
    """Custom type swL3IpCtrlLocalProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3IpCtrlLocalProxyArp_Type.__name__ = "Integer32"
_SwL3IpCtrlLocalProxyArp_Object = MibTableColumn
swL3IpCtrlLocalProxyArp = _SwL3IpCtrlLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 3, 1, 18),
    _SwL3IpCtrlLocalProxyArp_Type()
)
swL3IpCtrlLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlLocalProxyArp.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlEntry.setStatus("current")


class _SwL3Ipv6CtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6CtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6CtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6CtrlInterfaceName_Object = MibTableColumn
swL3Ipv6CtrlInterfaceName = _SwL3Ipv6CtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")
_SwL3Ipv6CtrlMaxReassmblySize_Type = Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object = MibTableColumn
swL3Ipv6CtrlMaxReassmblySize = _SwL3Ipv6CtrlMaxReassmblySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 2),
    _SwL3Ipv6CtrlMaxReassmblySize_Type()
)
swL3Ipv6CtrlMaxReassmblySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlMaxReassmblySize.setStatus("current")


class _SwL3Ipv6CtrlNsRetransTimer_Type(Unsigned32):
    """Custom type swL3Ipv6CtrlNsRetransTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwL3Ipv6CtrlNsRetransTimer_Type.__name__ = "Unsigned32"
_SwL3Ipv6CtrlNsRetransTimer_Object = MibTableColumn
swL3Ipv6CtrlNsRetransTimer = _SwL3Ipv6CtrlNsRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 3),
    _SwL3Ipv6CtrlNsRetransTimer_Type()
)
swL3Ipv6CtrlNsRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlNsRetransTimer.setStatus("current")


class _SwL3Ipv6CtrlRaState_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3Ipv6CtrlRaState_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaState_Object = MibTableColumn
swL3Ipv6CtrlRaState = _SwL3Ipv6CtrlRaState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 5),
    _SwL3Ipv6CtrlRaState_Type()
)
swL3Ipv6CtrlRaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaState.setStatus("current")


class _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaMinRtrAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1350),
    )


_SwL3Ipv6CtrlRaMinRtrAdvInterval_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaMinRtrAdvInterval_Object = MibTableColumn
swL3Ipv6CtrlRaMinRtrAdvInterval = _SwL3Ipv6CtrlRaMinRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 6),
    _SwL3Ipv6CtrlRaMinRtrAdvInterval_Type()
)
swL3Ipv6CtrlRaMinRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaMinRtrAdvInterval.setStatus("current")


class _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaMaxRtrAdvInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object = MibTableColumn
swL3Ipv6CtrlRaMaxRtrAdvInterval = _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 7),
    _SwL3Ipv6CtrlRaMaxRtrAdvInterval_Type()
)
swL3Ipv6CtrlRaMaxRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaMaxRtrAdvInterval.setStatus("current")


class _SwL3Ipv6CtrlRaLifeTime_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_SwL3Ipv6CtrlRaLifeTime_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaLifeTime_Object = MibTableColumn
swL3Ipv6CtrlRaLifeTime = _SwL3Ipv6CtrlRaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 8),
    _SwL3Ipv6CtrlRaLifeTime_Type()
)
swL3Ipv6CtrlRaLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaLifeTime.setStatus("current")


class _SwL3Ipv6CtrlRaReachableTime_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaReachableTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_SwL3Ipv6CtrlRaReachableTime_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaReachableTime_Object = MibTableColumn
swL3Ipv6CtrlRaReachableTime = _SwL3Ipv6CtrlRaReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 9),
    _SwL3Ipv6CtrlRaReachableTime_Type()
)
swL3Ipv6CtrlRaReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaReachableTime.setStatus("current")


class _SwL3Ipv6CtrlRaRetransTime_Type(Unsigned32):
    """Custom type swL3Ipv6CtrlRaRetransTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SwL3Ipv6CtrlRaRetransTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6CtrlRaRetransTime_Object = MibTableColumn
swL3Ipv6CtrlRaRetransTime = _SwL3Ipv6CtrlRaRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 10),
    _SwL3Ipv6CtrlRaRetransTime_Type()
)
swL3Ipv6CtrlRaRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaRetransTime.setStatus("current")


class _SwL3Ipv6CtrlRaHopLimit_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3Ipv6CtrlRaHopLimit_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaHopLimit_Object = MibTableColumn
swL3Ipv6CtrlRaHopLimit = _SwL3Ipv6CtrlRaHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 11),
    _SwL3Ipv6CtrlRaHopLimit_Type()
)
swL3Ipv6CtrlRaHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaHopLimit.setStatus("current")


class _SwL3Ipv6CtrlRaManagedFlag_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaManagedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3Ipv6CtrlRaManagedFlag_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaManagedFlag_Object = MibTableColumn
swL3Ipv6CtrlRaManagedFlag = _SwL3Ipv6CtrlRaManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 12),
    _SwL3Ipv6CtrlRaManagedFlag_Type()
)
swL3Ipv6CtrlRaManagedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaManagedFlag.setStatus("current")


class _SwL3Ipv6CtrlRaOtherConfigFlag_Type(Integer32):
    """Custom type swL3Ipv6CtrlRaOtherConfigFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3Ipv6CtrlRaOtherConfigFlag_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlRaOtherConfigFlag_Object = MibTableColumn
swL3Ipv6CtrlRaOtherConfigFlag = _SwL3Ipv6CtrlRaOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 4, 1, 13),
    _SwL3Ipv6CtrlRaOtherConfigFlag_Type()
)
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaOtherConfigFlag.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlEntry.setStatus("current")


class _SwL3Ipv6AddressCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6AddressCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6AddressCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6AddressCtrlInterfaceName_Object = MibTableColumn
swL3Ipv6AddressCtrlInterfaceName = _SwL3Ipv6AddressCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 3),
    _SwL3Ipv6AddressCtrlPrefixLen_Type()
)
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPrefixLen.setStatus("current")


class _SwL3Ipv6AddressCtrlPreferredLifeTime_Type(Unsigned32):
    """Custom type swL3Ipv6AddressCtrlPreferredLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SwL3Ipv6AddressCtrlPreferredLifeTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6AddressCtrlPreferredLifeTime_Object = MibTableColumn
swL3Ipv6AddressCtrlPreferredLifeTime = _SwL3Ipv6AddressCtrlPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 4),
    _SwL3Ipv6AddressCtrlPreferredLifeTime_Type()
)
swL3Ipv6AddressCtrlPreferredLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPreferredLifeTime.setStatus("current")


class _SwL3Ipv6AddressCtrlValidLifeTime_Type(Unsigned32):
    """Custom type swL3Ipv6AddressCtrlValidLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SwL3Ipv6AddressCtrlValidLifeTime_Type.__name__ = "Unsigned32"
_SwL3Ipv6AddressCtrlValidLifeTime_Object = MibTableColumn
swL3Ipv6AddressCtrlValidLifeTime = _SwL3Ipv6AddressCtrlValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 5),
    _SwL3Ipv6AddressCtrlValidLifeTime_Type()
)
swL3Ipv6AddressCtrlValidLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlValidLifeTime.setStatus("current")


class _SwL3Ipv6AddressCtrlOnLinkFlag_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlOnLinkFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3Ipv6AddressCtrlOnLinkFlag_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlOnLinkFlag_Object = MibTableColumn
swL3Ipv6AddressCtrlOnLinkFlag = _SwL3Ipv6AddressCtrlOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 6),
    _SwL3Ipv6AddressCtrlOnLinkFlag_Type()
)
swL3Ipv6AddressCtrlOnLinkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlOnLinkFlag.setStatus("current")


class _SwL3Ipv6AddressCtrlAutonomousFlag_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlAutonomousFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3Ipv6AddressCtrlAutonomousFlag_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlAutonomousFlag_Object = MibTableColumn
swL3Ipv6AddressCtrlAutonomousFlag = _SwL3Ipv6AddressCtrlAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 7),
    _SwL3Ipv6AddressCtrlAutonomousFlag_Type()
)
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAutonomousFlag.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 5, 1, 8),
    _SwL3Ipv6AddressCtrlState_Type()
)
swL3Ipv6AddressCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlState.setStatus("current")


class _SwL3IpCtrlAllIpIfState_Type(Integer32):
    """Custom type swL3IpCtrlAllIpIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SwL3IpCtrlAllIpIfState_Type.__name__ = "Integer32"
_SwL3IpCtrlAllIpIfState_Object = MibScalar
swL3IpCtrlAllIpIfState = _SwL3IpCtrlAllIpIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")
_SwL3LoopBackIpCtrlTable_Object = MibTable
swL3LoopBackIpCtrlTable = _SwL3LoopBackIpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlTable.setStatus("current")
_SwL3LoopBackIpCtrlEntry_Object = MibTableRow
swL3LoopBackIpCtrlEntry = _SwL3LoopBackIpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1)
)
swL3LoopBackIpCtrlEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3LoopBackIpCtrlInterfaceName"),
)
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlEntry.setStatus("current")


class _SwL3LoopBackIpCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3LoopBackIpCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3LoopBackIpCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3LoopBackIpCtrlInterfaceName_Object = MibTableColumn
swL3LoopBackIpCtrlInterfaceName = _SwL3LoopBackIpCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 1),
    _SwL3LoopBackIpCtrlInterfaceName_Type()
)
swL3LoopBackIpCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlInterfaceName.setStatus("current")


class _SwL3LoopBackIpCtrlIfIndex_Type(Integer32):
    """Custom type swL3LoopBackIpCtrlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3LoopBackIpCtrlIfIndex_Type.__name__ = "Integer32"
_SwL3LoopBackIpCtrlIfIndex_Object = MibTableColumn
swL3LoopBackIpCtrlIfIndex = _SwL3LoopBackIpCtrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 2),
    _SwL3LoopBackIpCtrlIfIndex_Type()
)
swL3LoopBackIpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIfIndex.setStatus("current")
_SwL3LoopBackIpCtrlIpAddr_Type = IpAddress
_SwL3LoopBackIpCtrlIpAddr_Object = MibTableColumn
swL3LoopBackIpCtrlIpAddr = _SwL3LoopBackIpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 3),
    _SwL3LoopBackIpCtrlIpAddr_Type()
)
swL3LoopBackIpCtrlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIpAddr.setStatus("current")
_SwL3LoopBackIpCtrlIpSubnetMask_Type = IpAddress
_SwL3LoopBackIpCtrlIpSubnetMask_Object = MibTableColumn
swL3LoopBackIpCtrlIpSubnetMask = _SwL3LoopBackIpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 4),
    _SwL3LoopBackIpCtrlIpSubnetMask_Type()
)
swL3LoopBackIpCtrlIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIpSubnetMask.setStatus("current")


class _SwL3LoopBackIpCtrlAdminState_Type(Integer32):
    """Custom type swL3LoopBackIpCtrlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3LoopBackIpCtrlAdminState_Type.__name__ = "Integer32"
_SwL3LoopBackIpCtrlAdminState_Object = MibTableColumn
swL3LoopBackIpCtrlAdminState = _SwL3LoopBackIpCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 5),
    _SwL3LoopBackIpCtrlAdminState_Type()
)
swL3LoopBackIpCtrlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlAdminState.setStatus("current")
_SwL3LoopBackIpCtrlRowStatus_Type = RowStatus
_SwL3LoopBackIpCtrlRowStatus_Object = MibTableColumn
swL3LoopBackIpCtrlRowStatus = _SwL3LoopBackIpCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 1, 8, 1, 6),
    _SwL3LoopBackIpCtrlRowStatus_Type()
)
swL3LoopBackIpCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlRowStatus.setStatus("current")
_SwL3IpFdbMgmt_ObjectIdentity = ObjectIdentity
swL3IpFdbMgmt = _SwL3IpFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2)
)
_SwL3IpFdbInfoTable_Object = MibTable
swL3IpFdbInfoTable = _SwL3IpFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoTable.setStatus("current")
_SwL3IpFdbInfoEntry_Object = MibTableRow
swL3IpFdbInfoEntry = _SwL3IpFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1, 1)
)
swL3IpFdbInfoEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3IpFdbInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoEntry.setStatus("current")
_SwL3IpFdbInfoIpAddr_Type = IpAddress
_SwL3IpFdbInfoIpAddr_Object = MibTableColumn
swL3IpFdbInfoIpAddr = _SwL3IpFdbInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1, 1, 1),
    _SwL3IpFdbInfoIpAddr_Type()
)
swL3IpFdbInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpAddr.setStatus("current")
_SwL3IpFdbInfoIpSubnetMask_Type = IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object = MibTableColumn
swL3IpFdbInfoIpSubnetMask = _SwL3IpFdbInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1, 1, 2),
    _SwL3IpFdbInfoIpSubnetMask_Type()
)
swL3IpFdbInfoIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpSubnetMask.setStatus("current")


class _SwL3IpFdbInfoPort_Type(Integer32):
    """Custom type swL3IpFdbInfoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpFdbInfoPort_Type.__name__ = "Integer32"
_SwL3IpFdbInfoPort_Object = MibTableColumn
swL3IpFdbInfoPort = _SwL3IpFdbInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1, 1, 3),
    _SwL3IpFdbInfoPort_Type()
)
swL3IpFdbInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoPort.setStatus("current")


class _SwL3IpFdbInfoType_Type(Integer32):
    """Custom type swL3IpFdbInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("other", 1),
          ("static", 2))
    )


_SwL3IpFdbInfoType_Type.__name__ = "Integer32"
_SwL3IpFdbInfoType_Object = MibTableColumn
swL3IpFdbInfoType = _SwL3IpFdbInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 2, 1, 1, 4),
    _SwL3IpFdbInfoType_Type()
)
swL3IpFdbInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoType.setStatus("current")


class _SwL3IpArpAgingTime_Type(Integer32):
    """Custom type swL3IpArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3IpArpAgingTime_Type.__name__ = "Integer32"
_SwL3IpArpAgingTime_Object = MibScalar
swL3IpArpAgingTime = _SwL3IpArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 4),
    _SwL3IpArpAgingTime_Type()
)
swL3IpArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpAgingTime.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 2),
    _SwL3IpStaticRouteMask_Type()
)
swL3IpStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMask.setStatus("current")


class _SwL3IpStaticRouteBkupState_Type(Integer32):
    """Custom type swL3IpStaticRouteBkupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 3),
          ("primary", 1))
    )


_SwL3IpStaticRouteBkupState_Type.__name__ = "Integer32"
_SwL3IpStaticRouteBkupState_Object = MibTableColumn
swL3IpStaticRouteBkupState = _SwL3IpStaticRouteBkupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteBkupState_Type()
)
swL3IpStaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteBkupState.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 4),
    _SwL3IpStaticRouteNextHop_Type()
)
swL3IpStaticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteNextHop.setStatus("current")


class _SwL3IpStaticRouteMetric_Type(Integer32):
    """Custom type swL3IpStaticRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3IpStaticRouteMetric_Type.__name__ = "Integer32"
_SwL3IpStaticRouteMetric_Object = MibTableColumn
swL3IpStaticRouteMetric = _SwL3IpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 5),
    _SwL3IpStaticRouteMetric_Type()
)
swL3IpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteMetric.setStatus("current")


class _SwL3IpStaticRouteStatus_Type(Integer32):
    """Custom type swL3IpStaticRouteStatus based on Integer32"""
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
        *(("active", 4),
          ("inActive", 5),
          ("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3IpStaticRouteStatus_Type.__name__ = "Integer32"
_SwL3IpStaticRouteStatus_Object = MibTableColumn
swL3IpStaticRouteStatus = _SwL3IpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 6),
    _SwL3IpStaticRouteStatus_Type()
)
swL3IpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteStatus.setStatus("current")


class _SwL3IpStaticRouteWeight_Type(Integer32):
    """Custom type swL3IpStaticRouteWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SwL3IpStaticRouteWeight_Type.__name__ = "Integer32"
_SwL3IpStaticRouteWeight_Object = MibTableColumn
swL3IpStaticRouteWeight = _SwL3IpStaticRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 2, 5, 1, 7),
    _SwL3IpStaticRouteWeight_Type()
)
swL3IpStaticRouteWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteWeight.setStatus("current")
_SwL3RelayMgmt_ObjectIdentity = ObjectIdentity
swL3RelayMgmt = _SwL3RelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3)
)
_SwL3RelayDnsMgmt_ObjectIdentity = ObjectIdentity
swL3RelayDnsMgmt = _SwL3RelayDnsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3)
)


class _SwL3RelayDnsState_Type(Integer32):
    """Custom type swL3RelayDnsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsState_Type.__name__ = "Integer32"
_SwL3RelayDnsState_Object = MibScalar
swL3RelayDnsState = _SwL3RelayDnsState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 1),
    _SwL3RelayDnsState_Type()
)
swL3RelayDnsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsState.setStatus("current")
_SwL3RelayDnsPrimaryServer_Type = IpAddress
_SwL3RelayDnsPrimaryServer_Object = MibScalar
swL3RelayDnsPrimaryServer = _SwL3RelayDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 2),
    _SwL3RelayDnsPrimaryServer_Type()
)
swL3RelayDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsPrimaryServer.setStatus("current")
_SwL3RelayDnsSecondaryServer_Type = IpAddress
_SwL3RelayDnsSecondaryServer_Object = MibScalar
swL3RelayDnsSecondaryServer = _SwL3RelayDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 3),
    _SwL3RelayDnsSecondaryServer_Type()
)
swL3RelayDnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsSecondaryServer.setStatus("current")


class _SwL3RelayDnsCacheState_Type(Integer32):
    """Custom type swL3RelayDnsCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsCacheState_Type.__name__ = "Integer32"
_SwL3RelayDnsCacheState_Object = MibScalar
swL3RelayDnsCacheState = _SwL3RelayDnsCacheState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 4),
    _SwL3RelayDnsCacheState_Type()
)
swL3RelayDnsCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCacheState.setStatus("current")


class _SwL3RelayDnsStaticTableState_Type(Integer32):
    """Custom type swL3RelayDnsStaticTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3RelayDnsStaticTableState_Type.__name__ = "Integer32"
_SwL3RelayDnsStaticTableState_Object = MibScalar
swL3RelayDnsStaticTableState = _SwL3RelayDnsStaticTableState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 5),
    _SwL3RelayDnsStaticTableState_Type()
)
swL3RelayDnsStaticTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsStaticTableState.setStatus("current")
_SwL3RelayDnsCtrlTable_Object = MibTable
swL3RelayDnsCtrlTable = _SwL3RelayDnsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 6)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlTable.setStatus("current")
_SwL3RelayDnsCtrlEntry_Object = MibTableRow
swL3RelayDnsCtrlEntry = _SwL3RelayDnsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 6, 1)
)
swL3RelayDnsCtrlEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RelayDnsCtrlDomainName"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"),
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlEntry.setStatus("current")


class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):
    """Custom type swL3RelayDnsCtrlDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL3RelayDnsCtrlDomainName_Type.__name__ = "DisplayString"
_SwL3RelayDnsCtrlDomainName_Object = MibTableColumn
swL3RelayDnsCtrlDomainName = _SwL3RelayDnsCtrlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 6, 1, 1),
    _SwL3RelayDnsCtrlDomainName_Type()
)
swL3RelayDnsCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlDomainName.setStatus("current")
_SwL3RelayDnsCtrlIpAddr_Type = IpAddress
_SwL3RelayDnsCtrlIpAddr_Object = MibTableColumn
swL3RelayDnsCtrlIpAddr = _SwL3RelayDnsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 6, 1, 2),
    _SwL3RelayDnsCtrlIpAddr_Type()
)
swL3RelayDnsCtrlIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlIpAddr.setStatus("current")


class _SwL3RelayDnsCtrlState_Type(Integer32):
    """Custom type swL3RelayDnsCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL3RelayDnsCtrlState_Type.__name__ = "Integer32"
_SwL3RelayDnsCtrlState_Object = MibTableColumn
swL3RelayDnsCtrlState = _SwL3RelayDnsCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 6, 1, 3),
    _SwL3RelayDnsCtrlState_Type()
)
swL3RelayDnsCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlState.setStatus("current")
_SwL3RelayDnsCtrlHostTable_Object = MibTable
swL3RelayDnsCtrlHostTable = _SwL3RelayDnsCtrlHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostTable.setStatus("current")
_SwL3RelayDnsCtrlHostEntry_Object = MibTableRow
swL3RelayDnsCtrlHostEntry = _SwL3RelayDnsCtrlHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7, 1)
)
swL3RelayDnsCtrlHostEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RelayDnsCtrlHostDomainName"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RelayDnsCtrlHostAddressType"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RelayDnsCtrlHostAddress"),
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostEntry.setStatus("current")


class _SwL3RelayDnsCtrlHostDomainName_Type(DisplayString):
    """Custom type swL3RelayDnsCtrlHostDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL3RelayDnsCtrlHostDomainName_Type.__name__ = "DisplayString"
_SwL3RelayDnsCtrlHostDomainName_Object = MibTableColumn
swL3RelayDnsCtrlHostDomainName = _SwL3RelayDnsCtrlHostDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7, 1, 1),
    _SwL3RelayDnsCtrlHostDomainName_Type()
)
swL3RelayDnsCtrlHostDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostDomainName.setStatus("current")
_SwL3RelayDnsCtrlHostAddressType_Type = InetAddressType
_SwL3RelayDnsCtrlHostAddressType_Object = MibTableColumn
swL3RelayDnsCtrlHostAddressType = _SwL3RelayDnsCtrlHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7, 1, 2),
    _SwL3RelayDnsCtrlHostAddressType_Type()
)
swL3RelayDnsCtrlHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostAddressType.setStatus("current")
_SwL3RelayDnsCtrlHostAddress_Type = InetAddress
_SwL3RelayDnsCtrlHostAddress_Object = MibTableColumn
swL3RelayDnsCtrlHostAddress = _SwL3RelayDnsCtrlHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7, 1, 3),
    _SwL3RelayDnsCtrlHostAddress_Type()
)
swL3RelayDnsCtrlHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostAddress.setStatus("current")
_SwL3RelayDnsCtrlHostRowStatus_Type = RowStatus
_SwL3RelayDnsCtrlHostRowStatus_Object = MibTableColumn
swL3RelayDnsCtrlHostRowStatus = _SwL3RelayDnsCtrlHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 3, 3, 7, 1, 4),
    _SwL3RelayDnsCtrlHostRowStatus_Type()
)
swL3RelayDnsCtrlHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlHostRowStatus.setStatus("current")
_SwL3Md5Table_Object = MibTable
swL3Md5Table = _SwL3Md5Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    swL3Md5Table.setStatus("current")
_SwL3Md5Entry_Object = MibTableRow
swL3Md5Entry = _SwL3Md5Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 4, 1)
)
swL3Md5Entry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3Md5KeyId"),
)
if mibBuilder.loadTexts:
    swL3Md5Entry.setStatus("current")


class _SwL3Md5KeyId_Type(Integer32):
    """Custom type swL3Md5KeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL3Md5KeyId_Type.__name__ = "Integer32"
_SwL3Md5KeyId_Object = MibTableColumn
swL3Md5KeyId = _SwL3Md5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 4, 1, 1),
    _SwL3Md5KeyId_Type()
)
swL3Md5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Md5KeyId.setStatus("current")


class _SwL3Md5Key_Type(DisplayString):
    """Custom type swL3Md5Key based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwL3Md5Key_Type.__name__ = "DisplayString"
_SwL3Md5Key_Object = MibTableColumn
swL3Md5Key = _SwL3Md5Key_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 4, 1, 2),
    _SwL3Md5Key_Type()
)
swL3Md5Key.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Md5Key.setStatus("current")
_SwL3Md5RowStatus_Type = RowStatus
_SwL3Md5RowStatus_Object = MibTableColumn
swL3Md5RowStatus = _SwL3Md5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 4, 1, 3),
    _SwL3Md5RowStatus_Type()
)
swL3Md5RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Md5RowStatus.setStatus("current")
_SwL3RouteRedistriTable_Object = MibTable
swL3RouteRedistriTable = _SwL3RouteRedistriTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    swL3RouteRedistriTable.setStatus("current")
_SwL3RouteRedistriEntry_Object = MibTableRow
swL3RouteRedistriEntry = _SwL3RouteRedistriEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1)
)
swL3RouteRedistriEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RouteRedistriSrcProtocol"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3RouteRedistriDstProtocol"),
)
if mibBuilder.loadTexts:
    swL3RouteRedistriEntry.setStatus("current")


class _SwL3RouteRedistriSrcProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriSrcProtocol based on Integer32"""
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
        *(("local", 5),
          ("ospf", 3),
          ("other", 1),
          ("rip", 2),
          ("static", 4))
    )


_SwL3RouteRedistriSrcProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriSrcProtocol_Object = MibTableColumn
swL3RouteRedistriSrcProtocol = _SwL3RouteRedistriSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1, 1),
    _SwL3RouteRedistriSrcProtocol_Type()
)
swL3RouteRedistriSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriSrcProtocol.setStatus("current")


class _SwL3RouteRedistriDstProtocol_Type(Integer32):
    """Custom type swL3RouteRedistriDstProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospf", 3),
          ("other", 1),
          ("rip", 2))
    )


_SwL3RouteRedistriDstProtocol_Type.__name__ = "Integer32"
_SwL3RouteRedistriDstProtocol_Object = MibTableColumn
swL3RouteRedistriDstProtocol = _SwL3RouteRedistriDstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1, 2),
    _SwL3RouteRedistriDstProtocol_Type()
)
swL3RouteRedistriDstProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RouteRedistriDstProtocol.setStatus("current")


class _SwL3RouteRedistriType_Type(Integer32):
    """Custom type swL3RouteRedistriType based on Integer32"""
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
        *(("all", 2),
          ("extType1", 9),
          ("extType2", 10),
          ("external", 6),
          ("inter-E1", 7),
          ("inter-E2", 8),
          ("internal", 5),
          ("other", 1),
          ("type-1", 3),
          ("type-2", 4))
    )


_SwL3RouteRedistriType_Type.__name__ = "Integer32"
_SwL3RouteRedistriType_Object = MibTableColumn
swL3RouteRedistriType = _SwL3RouteRedistriType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1, 3),
    _SwL3RouteRedistriType_Type()
)
swL3RouteRedistriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriType.setStatus("current")
_SwL3RouteRedistriMetric_Type = Unsigned32
_SwL3RouteRedistriMetric_Object = MibTableColumn
swL3RouteRedistriMetric = _SwL3RouteRedistriMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1, 4),
    _SwL3RouteRedistriMetric_Type()
)
swL3RouteRedistriMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriMetric.setStatus("current")
_SwL3RouteRedistriRowStatus_Type = RowStatus
_SwL3RouteRedistriRowStatus_Object = MibTableColumn
swL3RouteRedistriRowStatus = _SwL3RouteRedistriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 5, 1, 5),
    _SwL3RouteRedistriRowStatus_Type()
)
swL3RouteRedistriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3RouteRedistriRowStatus.setStatus("current")
_SwL3OspfHostTable_Object = MibTable
swL3OspfHostTable = _SwL3OspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    swL3OspfHostTable.setStatus("current")
_SwL3OspfHostEntry_Object = MibTableRow
swL3OspfHostEntry = _SwL3OspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1)
)
swL3OspfHostEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfHostIpAddress"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfHostTOS"),
)
if mibBuilder.loadTexts:
    swL3OspfHostEntry.setStatus("current")
_SwL3OspfHostIpAddress_Type = IpAddress
_SwL3OspfHostIpAddress_Object = MibTableColumn
swL3OspfHostIpAddress = _SwL3OspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1, 1),
    _SwL3OspfHostIpAddress_Type()
)
swL3OspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfHostIpAddress.setStatus("current")
_SwL3OspfHostTOS_Type = TOSType
_SwL3OspfHostTOS_Object = MibTableColumn
swL3OspfHostTOS = _SwL3OspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1, 2),
    _SwL3OspfHostTOS_Type()
)
swL3OspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfHostTOS.setStatus("current")
_SwL3OspfHostMetric_Type = Metric
_SwL3OspfHostMetric_Object = MibTableColumn
swL3OspfHostMetric = _SwL3OspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1, 3),
    _SwL3OspfHostMetric_Type()
)
swL3OspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3OspfHostMetric.setStatus("current")
_SwL3OspfHostAreaID_Type = AreaID
_SwL3OspfHostAreaID_Object = MibTableColumn
swL3OspfHostAreaID = _SwL3OspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1, 4),
    _SwL3OspfHostAreaID_Type()
)
swL3OspfHostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3OspfHostAreaID.setStatus("current")
_SwL3OspfHostStatus_Type = RowStatus
_SwL3OspfHostStatus_Object = MibTableColumn
swL3OspfHostStatus = _SwL3OspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 6, 1, 5),
    _SwL3OspfHostStatus_Type()
)
swL3OspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3OspfHostStatus.setStatus("current")
_SwL3ospfVirtIfTable_Object = MibTable
swL3ospfVirtIfTable = _SwL3ospfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    swL3ospfVirtIfTable.setStatus("current")
_SwL3ospfVirtIfEntry_Object = MibTableRow
swL3ospfVirtIfEntry = _SwL3ospfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1)
)
swL3ospfVirtIfEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3ospfVirtIfAreaId"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3ospfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    swL3ospfVirtIfEntry.setStatus("current")
_SwL3ospfVirtIfAreaId_Type = AreaID
_SwL3ospfVirtIfAreaId_Object = MibTableColumn
swL3ospfVirtIfAreaId = _SwL3ospfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 1),
    _SwL3ospfVirtIfAreaId_Type()
)
swL3ospfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfAreaId.setStatus("current")
_SwL3ospfVirtIfNeighbor_Type = RouterID
_SwL3ospfVirtIfNeighbor_Object = MibTableColumn
swL3ospfVirtIfNeighbor = _SwL3ospfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 2),
    _SwL3ospfVirtIfNeighbor_Type()
)
swL3ospfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfNeighbor.setStatus("current")


class _SwL3ospfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type swL3ospfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SwL3ospfVirtIfTransitDelay_Object = MibTableColumn
swL3ospfVirtIfTransitDelay = _SwL3ospfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 3),
    _SwL3ospfVirtIfTransitDelay_Type()
)
swL3ospfVirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfTransitDelay.setStatus("current")


class _SwL3ospfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type swL3ospfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SwL3ospfVirtIfRetransInterval_Object = MibTableColumn
swL3ospfVirtIfRetransInterval = _SwL3ospfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 4),
    _SwL3ospfVirtIfRetransInterval_Type()
)
swL3ospfVirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfRetransInterval.setStatus("current")


class _SwL3ospfVirtIfHelloInterval_Type(HelloRange):
    """Custom type swL3ospfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_SwL3ospfVirtIfHelloInterval_Object = MibTableColumn
swL3ospfVirtIfHelloInterval = _SwL3ospfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 5),
    _SwL3ospfVirtIfHelloInterval_Type()
)
swL3ospfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfHelloInterval.setStatus("current")


class _SwL3ospfVirtIfRtrDeadInterval_Type(Integer32):
    """Custom type swL3ospfVirtIfRtrDeadInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3ospfVirtIfRtrDeadInterval_Type.__name__ = "Integer32"
_SwL3ospfVirtIfRtrDeadInterval_Object = MibTableColumn
swL3ospfVirtIfRtrDeadInterval = _SwL3ospfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 6),
    _SwL3ospfVirtIfRtrDeadInterval_Type()
)
swL3ospfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfRtrDeadInterval.setStatus("current")


class _SwL3ospfVirtIfState_Type(Integer32):
    """Custom type swL3ospfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_SwL3ospfVirtIfState_Type.__name__ = "Integer32"
_SwL3ospfVirtIfState_Object = MibTableColumn
swL3ospfVirtIfState = _SwL3ospfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 7),
    _SwL3ospfVirtIfState_Type()
)
swL3ospfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfState.setStatus("current")
_SwL3ospfVirtIfEvents_Type = Counter32
_SwL3ospfVirtIfEvents_Object = MibTableColumn
swL3ospfVirtIfEvents = _SwL3ospfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 8),
    _SwL3ospfVirtIfEvents_Type()
)
swL3ospfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfVirtIfEvents.setStatus("current")


class _SwL3ospfVirtIfAuthType_Type(Integer32):
    """Custom type swL3ospfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3ospfVirtIfAuthType_Type.__name__ = "Integer32"
_SwL3ospfVirtIfAuthType_Object = MibTableColumn
swL3ospfVirtIfAuthType = _SwL3ospfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 9),
    _SwL3ospfVirtIfAuthType_Type()
)
swL3ospfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfAuthType.setStatus("current")


class _SwL3ospfVirtIfAuthKey_Type(OctetString):
    """Custom type swL3ospfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwL3ospfVirtIfAuthKey_Type.__name__ = "OctetString"
_SwL3ospfVirtIfAuthKey_Object = MibTableColumn
swL3ospfVirtIfAuthKey = _SwL3ospfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 10),
    _SwL3ospfVirtIfAuthKey_Type()
)
swL3ospfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfAuthKey.setStatus("current")


class _SwL3ospfVirtIfAuthKeyID_Type(Integer32):
    """Custom type swL3ospfVirtIfAuthKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3ospfVirtIfAuthKeyID_Type.__name__ = "Integer32"
_SwL3ospfVirtIfAuthKeyID_Object = MibTableColumn
swL3ospfVirtIfAuthKeyID = _SwL3ospfVirtIfAuthKeyID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 11),
    _SwL3ospfVirtIfAuthKeyID_Type()
)
swL3ospfVirtIfAuthKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfAuthKeyID.setStatus("current")
_SwL3ospfVirtIfStatus_Type = RowStatus
_SwL3ospfVirtIfStatus_Object = MibTableColumn
swL3ospfVirtIfStatus = _SwL3ospfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 7, 1, 12),
    _SwL3ospfVirtIfStatus_Type()
)
swL3ospfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfVirtIfStatus.setStatus("current")
_SwL3ospfIfTable_Object = MibTable
swL3ospfIfTable = _SwL3ospfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    swL3ospfIfTable.setStatus("current")
_SwL3ospfIfEntry_Object = MibTableRow
swL3ospfIfEntry = _SwL3ospfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1)
)
swL3ospfIfEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3ospfIfIpAddress"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    swL3ospfIfEntry.setStatus("current")
_SwL3ospfIfIpAddress_Type = IpAddress
_SwL3ospfIfIpAddress_Object = MibTableColumn
swL3ospfIfIpAddress = _SwL3ospfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 1),
    _SwL3ospfIfIpAddress_Type()
)
swL3ospfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfIpAddress.setStatus("current")
_SwL3ospfAddressLessIf_Type = Integer32
_SwL3ospfAddressLessIf_Object = MibTableColumn
swL3ospfAddressLessIf = _SwL3ospfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 2),
    _SwL3ospfAddressLessIf_Type()
)
swL3ospfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfAddressLessIf.setStatus("current")


class _SwL3ospfIfAreaId_Type(AreaID):
    """Custom type swL3ospfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_SwL3ospfIfAreaId_Object = MibTableColumn
swL3ospfIfAreaId = _SwL3ospfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 3),
    _SwL3ospfIfAreaId_Type()
)
swL3ospfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfAreaId.setStatus("current")


class _SwL3ospfIfType_Type(Integer32):
    """Custom type swL3ospfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToMultipoint", 5),
          ("pointToPoint", 3))
    )


_SwL3ospfIfType_Type.__name__ = "Integer32"
_SwL3ospfIfType_Object = MibTableColumn
swL3ospfIfType = _SwL3ospfIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 4),
    _SwL3ospfIfType_Type()
)
swL3ospfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfType.setStatus("current")


class _SwL3ospfIfAdminStat_Type(Status):
    """Custom type swL3ospfIfAdminStat based on Status"""


_SwL3ospfIfAdminStat_Object = MibTableColumn
swL3ospfIfAdminStat = _SwL3ospfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 5),
    _SwL3ospfIfAdminStat_Type()
)
swL3ospfIfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfAdminStat.setStatus("current")


class _SwL3ospfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type swL3ospfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_SwL3ospfIfRtrPriority_Object = MibTableColumn
swL3ospfIfRtrPriority = _SwL3ospfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 6),
    _SwL3ospfIfRtrPriority_Type()
)
swL3ospfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfRtrPriority.setStatus("current")


class _SwL3ospfIfTransitDelay_Type(UpToMaxAge):
    """Custom type swL3ospfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SwL3ospfIfTransitDelay_Object = MibTableColumn
swL3ospfIfTransitDelay = _SwL3ospfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 7),
    _SwL3ospfIfTransitDelay_Type()
)
swL3ospfIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfTransitDelay.setStatus("current")


class _SwL3ospfIfRetransInterval_Type(UpToMaxAge):
    """Custom type swL3ospfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SwL3ospfIfRetransInterval_Object = MibTableColumn
swL3ospfIfRetransInterval = _SwL3ospfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 8),
    _SwL3ospfIfRetransInterval_Type()
)
swL3ospfIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfRetransInterval.setStatus("current")


class _SwL3ospfIfHelloInterval_Type(HelloRange):
    """Custom type swL3ospfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_SwL3ospfIfHelloInterval_Object = MibTableColumn
swL3ospfIfHelloInterval = _SwL3ospfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 9),
    _SwL3ospfIfHelloInterval_Type()
)
swL3ospfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfHelloInterval.setStatus("current")


class _SwL3ospfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type swL3ospfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_SwL3ospfIfRtrDeadInterval_Object = MibTableColumn
swL3ospfIfRtrDeadInterval = _SwL3ospfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 10),
    _SwL3ospfIfRtrDeadInterval_Type()
)
swL3ospfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfRtrDeadInterval.setStatus("current")


class _SwL3ospfIfPollInterval_Type(PositiveInteger):
    """Custom type swL3ospfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_SwL3ospfIfPollInterval_Object = MibTableColumn
swL3ospfIfPollInterval = _SwL3ospfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 11),
    _SwL3ospfIfPollInterval_Type()
)
swL3ospfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfPollInterval.setStatus("current")


class _SwL3ospfIfState_Type(Integer32):
    """Custom type swL3ospfIfState based on Integer32"""
    defaultValue = 1

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
        *(("backupDesignatedRouter", 6),
          ("designatedRouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherDesignatedRouter", 7),
          ("pointToPoint", 4),
          ("waiting", 3))
    )


_SwL3ospfIfState_Type.__name__ = "Integer32"
_SwL3ospfIfState_Object = MibTableColumn
swL3ospfIfState = _SwL3ospfIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 12),
    _SwL3ospfIfState_Type()
)
swL3ospfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfState.setStatus("current")


class _SwL3ospfIfDesignatedRouter_Type(IpAddress):
    """Custom type swL3ospfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_SwL3ospfIfDesignatedRouter_Object = MibTableColumn
swL3ospfIfDesignatedRouter = _SwL3ospfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 13),
    _SwL3ospfIfDesignatedRouter_Type()
)
swL3ospfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfDesignatedRouter.setStatus("current")


class _SwL3ospfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type swL3ospfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_SwL3ospfIfBackupDesignatedRouter_Object = MibTableColumn
swL3ospfIfBackupDesignatedRouter = _SwL3ospfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 14),
    _SwL3ospfIfBackupDesignatedRouter_Type()
)
swL3ospfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfBackupDesignatedRouter.setStatus("current")
_SwL3ospfIfEvents_Type = Counter32
_SwL3ospfIfEvents_Object = MibTableColumn
swL3ospfIfEvents = _SwL3ospfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 15),
    _SwL3ospfIfEvents_Type()
)
swL3ospfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfEvents.setStatus("current")


class _SwL3ospfIfMulticastForwarding_Type(Integer32):
    """Custom type swL3ospfIfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_SwL3ospfIfMulticastForwarding_Type.__name__ = "Integer32"
_SwL3ospfIfMulticastForwarding_Object = MibTableColumn
swL3ospfIfMulticastForwarding = _SwL3ospfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 16),
    _SwL3ospfIfMulticastForwarding_Type()
)
swL3ospfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfMulticastForwarding.setStatus("current")


class _SwL3ospfIfDemand_Type(TruthValue):
    """Custom type swL3ospfIfDemand based on TruthValue"""


_SwL3ospfIfDemand_Object = MibTableColumn
swL3ospfIfDemand = _SwL3ospfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 17),
    _SwL3ospfIfDemand_Type()
)
swL3ospfIfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfIfDemand.setStatus("current")


class _SwL3ospfIfAuthType_Type(Integer32):
    """Custom type swL3ospfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3ospfIfAuthType_Type.__name__ = "Integer32"
_SwL3ospfIfAuthType_Object = MibTableColumn
swL3ospfIfAuthType = _SwL3ospfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 18),
    _SwL3ospfIfAuthType_Type()
)
swL3ospfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfAuthType.setStatus("current")


class _SwL3ospfIfAuthKey_Type(OctetString):
    """Custom type swL3ospfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwL3ospfIfAuthKey_Type.__name__ = "OctetString"
_SwL3ospfIfAuthKey_Object = MibTableColumn
swL3ospfIfAuthKey = _SwL3ospfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 19),
    _SwL3ospfIfAuthKey_Type()
)
swL3ospfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfAuthKey.setStatus("current")


class _SwL3ospfIfAuthKeyID_Type(Integer32):
    """Custom type swL3ospfIfAuthKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3ospfIfAuthKeyID_Type.__name__ = "Integer32"
_SwL3ospfIfAuthKeyID_Object = MibTableColumn
swL3ospfIfAuthKeyID = _SwL3ospfIfAuthKeyID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 20),
    _SwL3ospfIfAuthKeyID_Type()
)
swL3ospfIfAuthKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfAuthKeyID.setStatus("current")


class _SwL3ospfIfPassiveMode_Type(Integer32):
    """Custom type swL3ospfIfPassiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL3ospfIfPassiveMode_Type.__name__ = "Integer32"
_SwL3ospfIfPassiveMode_Object = MibTableColumn
swL3ospfIfPassiveMode = _SwL3ospfIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 21),
    _SwL3ospfIfPassiveMode_Type()
)
swL3ospfIfPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfPassiveMode.setStatus("current")
_SwL3ospfIfMetric_Type = Metric
_SwL3ospfIfMetric_Object = MibTableColumn
swL3ospfIfMetric = _SwL3ospfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 8, 1, 23),
    _SwL3ospfIfMetric_Type()
)
swL3ospfIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfIfMetric.setStatus("current")
_SwL3RoutePreference_ObjectIdentity = ObjectIdentity
swL3RoutePreference = _SwL3RoutePreference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9)
)


class _SwL3RoutePreferenceRIP_Type(Integer32):
    """Custom type swL3RoutePreferenceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceRIP_Type.__name__ = "Integer32"
_SwL3RoutePreferenceRIP_Object = MibScalar
swL3RoutePreferenceRIP = _SwL3RoutePreferenceRIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 1),
    _SwL3RoutePreferenceRIP_Type()
)
swL3RoutePreferenceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceRIP.setStatus("current")


class _SwL3RoutePreferenceOSPFIntra_Type(Integer32):
    """Custom type swL3RoutePreferenceOSPFIntra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceOSPFIntra_Type.__name__ = "Integer32"
_SwL3RoutePreferenceOSPFIntra_Object = MibScalar
swL3RoutePreferenceOSPFIntra = _SwL3RoutePreferenceOSPFIntra_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 2),
    _SwL3RoutePreferenceOSPFIntra_Type()
)
swL3RoutePreferenceOSPFIntra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceOSPFIntra.setStatus("current")


class _SwL3RoutePreferenceStatic_Type(Integer32):
    """Custom type swL3RoutePreferenceStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceStatic_Type.__name__ = "Integer32"
_SwL3RoutePreferenceStatic_Object = MibScalar
swL3RoutePreferenceStatic = _SwL3RoutePreferenceStatic_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 3),
    _SwL3RoutePreferenceStatic_Type()
)
swL3RoutePreferenceStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceStatic.setStatus("current")


class _SwL3RoutePreferenceLocal_Type(Integer32):
    """Custom type swL3RoutePreferenceLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_SwL3RoutePreferenceLocal_Type.__name__ = "Integer32"
_SwL3RoutePreferenceLocal_Object = MibScalar
swL3RoutePreferenceLocal = _SwL3RoutePreferenceLocal_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 4),
    _SwL3RoutePreferenceLocal_Type()
)
swL3RoutePreferenceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RoutePreferenceLocal.setStatus("current")


class _SwL3RoutePreferenceOSPFInter_Type(Integer32):
    """Custom type swL3RoutePreferenceOSPFInter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceOSPFInter_Type.__name__ = "Integer32"
_SwL3RoutePreferenceOSPFInter_Object = MibScalar
swL3RoutePreferenceOSPFInter = _SwL3RoutePreferenceOSPFInter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 5),
    _SwL3RoutePreferenceOSPFInter_Type()
)
swL3RoutePreferenceOSPFInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceOSPFInter.setStatus("current")


class _SwL3RoutePreferenceOSPFExtT1_Type(Integer32):
    """Custom type swL3RoutePreferenceOSPFExtT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceOSPFExtT1_Type.__name__ = "Integer32"
_SwL3RoutePreferenceOSPFExtT1_Object = MibScalar
swL3RoutePreferenceOSPFExtT1 = _SwL3RoutePreferenceOSPFExtT1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 6),
    _SwL3RoutePreferenceOSPFExtT1_Type()
)
swL3RoutePreferenceOSPFExtT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceOSPFExtT1.setStatus("current")


class _SwL3RoutePreferenceOSPFExtT2_Type(Integer32):
    """Custom type swL3RoutePreferenceOSPFExtT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceOSPFExtT2_Type.__name__ = "Integer32"
_SwL3RoutePreferenceOSPFExtT2_Object = MibScalar
swL3RoutePreferenceOSPFExtT2 = _SwL3RoutePreferenceOSPFExtT2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 7),
    _SwL3RoutePreferenceOSPFExtT2_Type()
)
swL3RoutePreferenceOSPFExtT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceOSPFExtT2.setStatus("current")


class _SwL3RoutePreferenceDefault_Type(Integer32):
    """Custom type swL3RoutePreferenceDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SwL3RoutePreferenceDefault_Type.__name__ = "Integer32"
_SwL3RoutePreferenceDefault_Object = MibScalar
swL3RoutePreferenceDefault = _SwL3RoutePreferenceDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 9, 8),
    _SwL3RoutePreferenceDefault_Type()
)
swL3RoutePreferenceDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RoutePreferenceDefault.setStatus("current")
_SwL3ospfAreaTable_Object = MibTable
swL3ospfAreaTable = _SwL3ospfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10)
)
if mibBuilder.loadTexts:
    swL3ospfAreaTable.setStatus("current")
_SwL3ospfAreaEntry_Object = MibTableRow
swL3ospfAreaEntry = _SwL3ospfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1)
)
swL3ospfAreaEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3ospfAreaId"),
)
if mibBuilder.loadTexts:
    swL3ospfAreaEntry.setStatus("current")
_SwL3ospfAreaId_Type = AreaID
_SwL3ospfAreaId_Object = MibTableColumn
swL3ospfAreaId = _SwL3ospfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 1),
    _SwL3ospfAreaId_Type()
)
swL3ospfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3ospfAreaId.setStatus("current")


class _SwL3ospfAreaType_Type(Integer32):
    """Custom type swL3ospfAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("nssa", 3),
          ("stub", 2))
    )


_SwL3ospfAreaType_Type.__name__ = "Integer32"
_SwL3ospfAreaType_Object = MibTableColumn
swL3ospfAreaType = _SwL3ospfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 2),
    _SwL3ospfAreaType_Type()
)
swL3ospfAreaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfAreaType.setStatus("obsolete")


class _SwL3ospfAreaSummaryState_Type(Integer32):
    """Custom type swL3ospfAreaSummaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("none", 1))
    )


_SwL3ospfAreaSummaryState_Type.__name__ = "Integer32"
_SwL3ospfAreaSummaryState_Object = MibTableColumn
swL3ospfAreaSummaryState = _SwL3ospfAreaSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 3),
    _SwL3ospfAreaSummaryState_Type()
)
swL3ospfAreaSummaryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfAreaSummaryState.setStatus("current")


class _SwL3ospfAreaMetric_Type(Integer32):
    """Custom type swL3ospfAreaMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3ospfAreaMetric_Type.__name__ = "Integer32"
_SwL3ospfAreaMetric_Object = MibTableColumn
swL3ospfAreaMetric = _SwL3ospfAreaMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 4),
    _SwL3ospfAreaMetric_Type()
)
swL3ospfAreaMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3ospfAreaMetric.setStatus("current")


class _SwL3ospfAreaTranslateState_Type(Integer32):
    """Custom type swL3ospfAreaTranslateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("none", 1))
    )


_SwL3ospfAreaTranslateState_Type.__name__ = "Integer32"
_SwL3ospfAreaTranslateState_Object = MibTableColumn
swL3ospfAreaTranslateState = _SwL3ospfAreaTranslateState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 5),
    _SwL3ospfAreaTranslateState_Type()
)
swL3ospfAreaTranslateState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfAreaTranslateState.setStatus("current")
_SwL3ospfAreaStatus_Type = RowStatus
_SwL3ospfAreaStatus_Object = MibTableColumn
swL3ospfAreaStatus = _SwL3ospfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 10, 1, 6),
    _SwL3ospfAreaStatus_Type()
)
swL3ospfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3ospfAreaStatus.setStatus("current")
_SwL3OspfLsdbMgmt_ObjectIdentity = ObjectIdentity
swL3OspfLsdbMgmt = _SwL3OspfLsdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13)
)
_SwL3OspfInternalLsdbTable_Object = MibTable
swL3OspfInternalLsdbTable = _SwL3OspfInternalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1)
)
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbTable.setStatus("current")
_SwL3OspfInternalLsdbEntry_Object = MibTableRow
swL3OspfInternalLsdbEntry = _SwL3OspfInternalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1)
)
swL3OspfInternalLsdbEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfInternalLsdbAreaId"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfInternalLsdbType"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfInternalLsdbLsid"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfInternalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbEntry.setStatus("current")
_SwL3OspfInternalLsdbAreaId_Type = AreaID
_SwL3OspfInternalLsdbAreaId_Object = MibTableColumn
swL3OspfInternalLsdbAreaId = _SwL3OspfInternalLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 1),
    _SwL3OspfInternalLsdbAreaId_Type()
)
swL3OspfInternalLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbAreaId.setStatus("current")


class _SwL3OspfInternalLsdbType_Type(Integer32):
    """Custom type swL3OspfInternalLsdbType based on Integer32"""
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
        *(("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_SwL3OspfInternalLsdbType_Type.__name__ = "Integer32"
_SwL3OspfInternalLsdbType_Object = MibTableColumn
swL3OspfInternalLsdbType = _SwL3OspfInternalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 2),
    _SwL3OspfInternalLsdbType_Type()
)
swL3OspfInternalLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbType.setStatus("current")
_SwL3OspfInternalLsdbLsid_Type = IpAddress
_SwL3OspfInternalLsdbLsid_Object = MibTableColumn
swL3OspfInternalLsdbLsid = _SwL3OspfInternalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 3),
    _SwL3OspfInternalLsdbLsid_Type()
)
swL3OspfInternalLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbLsid.setStatus("current")
_SwL3OspfInternalLsdbRouterId_Type = RouterID
_SwL3OspfInternalLsdbRouterId_Object = MibTableColumn
swL3OspfInternalLsdbRouterId = _SwL3OspfInternalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 4),
    _SwL3OspfInternalLsdbRouterId_Type()
)
swL3OspfInternalLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbRouterId.setStatus("current")


class _SwL3OspfInternalLsdbMetric_Type(Integer32):
    """Custom type swL3OspfInternalLsdbMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3OspfInternalLsdbMetric_Type.__name__ = "Integer32"
_SwL3OspfInternalLsdbMetric_Object = MibTableColumn
swL3OspfInternalLsdbMetric = _SwL3OspfInternalLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 5),
    _SwL3OspfInternalLsdbMetric_Type()
)
swL3OspfInternalLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbMetric.setStatus("current")


class _SwL3OspfInternalLsdbSequenceNo_Type(OctetString):
    """Custom type swL3OspfInternalLsdbSequenceNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwL3OspfInternalLsdbSequenceNo_Type.__name__ = "OctetString"
_SwL3OspfInternalLsdbSequenceNo_Object = MibTableColumn
swL3OspfInternalLsdbSequenceNo = _SwL3OspfInternalLsdbSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 6),
    _SwL3OspfInternalLsdbSequenceNo_Type()
)
swL3OspfInternalLsdbSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbSequenceNo.setStatus("current")
_SwL3OspfInternalLsdbAge_Type = Unsigned32
_SwL3OspfInternalLsdbAge_Object = MibTableColumn
swL3OspfInternalLsdbAge = _SwL3OspfInternalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 7),
    _SwL3OspfInternalLsdbAge_Type()
)
swL3OspfInternalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbAge.setStatus("current")
_SwL3OspfInternalLsdbChecksum_Type = Integer32
_SwL3OspfInternalLsdbChecksum_Object = MibTableColumn
swL3OspfInternalLsdbChecksum = _SwL3OspfInternalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 1, 1, 8),
    _SwL3OspfInternalLsdbChecksum_Type()
)
swL3OspfInternalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfInternalLsdbChecksum.setStatus("current")
_SwL3OspfExternalLsdbTable_Object = MibTable
swL3OspfExternalLsdbTable = _SwL3OspfExternalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2)
)
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbTable.setStatus("current")
_SwL3OspfExternalLsdbEntry_Object = MibTableRow
swL3OspfExternalLsdbEntry = _SwL3OspfExternalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1)
)
swL3OspfExternalLsdbEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfExternalLsdbType"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfExternalLsdbLsid"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3OspfExternalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbEntry.setStatus("current")


class _SwL3OspfExternalLsdbType_Type(Integer32):
    """Custom type swL3OspfExternalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("asExternalLink", 5),
          ("nssaExternalLink", 7))
    )


_SwL3OspfExternalLsdbType_Type.__name__ = "Integer32"
_SwL3OspfExternalLsdbType_Object = MibTableColumn
swL3OspfExternalLsdbType = _SwL3OspfExternalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 1),
    _SwL3OspfExternalLsdbType_Type()
)
swL3OspfExternalLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbType.setStatus("current")
_SwL3OspfExternalLsdbLsid_Type = IpAddress
_SwL3OspfExternalLsdbLsid_Object = MibTableColumn
swL3OspfExternalLsdbLsid = _SwL3OspfExternalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 2),
    _SwL3OspfExternalLsdbLsid_Type()
)
swL3OspfExternalLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbLsid.setStatus("current")
_SwL3OspfExternalLsdbRouterId_Type = RouterID
_SwL3OspfExternalLsdbRouterId_Object = MibTableColumn
swL3OspfExternalLsdbRouterId = _SwL3OspfExternalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 3),
    _SwL3OspfExternalLsdbRouterId_Type()
)
swL3OspfExternalLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbRouterId.setStatus("current")


class _SwL3OspfExternalLsdbMetric_Type(Integer32):
    """Custom type swL3OspfExternalLsdbMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL3OspfExternalLsdbMetric_Type.__name__ = "Integer32"
_SwL3OspfExternalLsdbMetric_Object = MibTableColumn
swL3OspfExternalLsdbMetric = _SwL3OspfExternalLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 4),
    _SwL3OspfExternalLsdbMetric_Type()
)
swL3OspfExternalLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbMetric.setStatus("current")


class _SwL3OspfExternalLsdbMetricType_Type(Integer32):
    """Custom type swL3OspfExternalLsdbMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type-1", 1),
          ("type-2", 2),
          ("unrecognized", 0))
    )


_SwL3OspfExternalLsdbMetricType_Type.__name__ = "Integer32"
_SwL3OspfExternalLsdbMetricType_Object = MibTableColumn
swL3OspfExternalLsdbMetricType = _SwL3OspfExternalLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 5),
    _SwL3OspfExternalLsdbMetricType_Type()
)
swL3OspfExternalLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbMetricType.setStatus("current")


class _SwL3OspfExternalLsdbSequenceNo_Type(OctetString):
    """Custom type swL3OspfExternalLsdbSequenceNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SwL3OspfExternalLsdbSequenceNo_Type.__name__ = "OctetString"
_SwL3OspfExternalLsdbSequenceNo_Object = MibTableColumn
swL3OspfExternalLsdbSequenceNo = _SwL3OspfExternalLsdbSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 6),
    _SwL3OspfExternalLsdbSequenceNo_Type()
)
swL3OspfExternalLsdbSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbSequenceNo.setStatus("current")
_SwL3OspfExternalLsdbAge_Type = Unsigned32
_SwL3OspfExternalLsdbAge_Object = MibTableColumn
swL3OspfExternalLsdbAge = _SwL3OspfExternalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 7),
    _SwL3OspfExternalLsdbAge_Type()
)
swL3OspfExternalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbAge.setStatus("current")
_SwL3OspfExternalLsdbChecksum_Type = Integer32
_SwL3OspfExternalLsdbChecksum_Object = MibTableColumn
swL3OspfExternalLsdbChecksum = _SwL3OspfExternalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 8),
    _SwL3OspfExternalLsdbChecksum_Type()
)
swL3OspfExternalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbChecksum.setStatus("current")
_SwL3OspfExternalLsdbForwardingAddress_Type = IpAddress
_SwL3OspfExternalLsdbForwardingAddress_Object = MibTableColumn
swL3OspfExternalLsdbForwardingAddress = _SwL3OspfExternalLsdbForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 9),
    _SwL3OspfExternalLsdbForwardingAddress_Type()
)
swL3OspfExternalLsdbForwardingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbForwardingAddress.setStatus("current")
_SwL3OspfExternalLsdbRouteTag_Type = OctetString
_SwL3OspfExternalLsdbRouteTag_Object = MibTableColumn
swL3OspfExternalLsdbRouteTag = _SwL3OspfExternalLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 13, 2, 1, 10),
    _SwL3OspfExternalLsdbRouteTag_Type()
)
swL3OspfExternalLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3OspfExternalLsdbRouteTag.setStatus("current")
_SwL3VrrpOperMgmt_ObjectIdentity = ObjectIdentity
swL3VrrpOperMgmt = _SwL3VrrpOperMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14)
)
_SwL3VrrpOperTable_Object = MibTable
swL3VrrpOperTable = _SwL3VrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1)
)
if mibBuilder.loadTexts:
    swL3VrrpOperTable.setStatus("current")
_SwL3VrrpOperEntry_Object = MibTableRow
swL3VrrpOperEntry = _SwL3VrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1)
)
swL3VrrpOperEntry.setIndexNames(
    (0, "DES-3810-52-L3MGMT-MIB", "swL3VrrpOperIfIndex"),
    (0, "DES-3810-52-L3MGMT-MIB", "swL3VrrpOperVrId"),
)
if mibBuilder.loadTexts:
    swL3VrrpOperEntry.setStatus("current")
_SwL3VrrpOperIfIndex_Type = Integer32
_SwL3VrrpOperIfIndex_Object = MibTableColumn
swL3VrrpOperIfIndex = _SwL3VrrpOperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 1),
    _SwL3VrrpOperIfIndex_Type()
)
swL3VrrpOperIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperIfIndex.setStatus("current")
_SwL3VrrpOperVrId_Type = VrId
_SwL3VrrpOperVrId_Object = MibTableColumn
swL3VrrpOperVrId = _SwL3VrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 2),
    _SwL3VrrpOperVrId_Type()
)
swL3VrrpOperVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVrId.setStatus("current")
_SwL3VrrpOperVirtualMacAddr_Type = MacAddress
_SwL3VrrpOperVirtualMacAddr_Object = MibTableColumn
swL3VrrpOperVirtualMacAddr = _SwL3VrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 3),
    _SwL3VrrpOperVirtualMacAddr_Type()
)
swL3VrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualMacAddr.setStatus("current")


class _SwL3VrrpOperState_Type(Integer32):
    """Custom type swL3VrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_SwL3VrrpOperState_Type.__name__ = "Integer32"
_SwL3VrrpOperState_Object = MibTableColumn
swL3VrrpOperState = _SwL3VrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 4),
    _SwL3VrrpOperState_Type()
)
swL3VrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperState.setStatus("current")


class _SwL3VrrpOperAdminState_Type(Integer32):
    """Custom type swL3VrrpOperAdminState based on Integer32"""
    defaultValue = 2

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


_SwL3VrrpOperAdminState_Type.__name__ = "Integer32"
_SwL3VrrpOperAdminState_Object = MibTableColumn
swL3VrrpOperAdminState = _SwL3VrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 5),
    _SwL3VrrpOperAdminState_Type()
)
swL3VrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAdminState.setStatus("current")


class _SwL3VrrpOperPriority_Type(Integer32):
    """Custom type swL3VrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3VrrpOperPriority_Type.__name__ = "Integer32"
_SwL3VrrpOperPriority_Object = MibTableColumn
swL3VrrpOperPriority = _SwL3VrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 6),
    _SwL3VrrpOperPriority_Type()
)
swL3VrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperPriority.setStatus("current")
_SwL3VrrpOperMasterIpAddr_Type = IpAddress
_SwL3VrrpOperMasterIpAddr_Object = MibTableColumn
swL3VrrpOperMasterIpAddr = _SwL3VrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 7),
    _SwL3VrrpOperMasterIpAddr_Type()
)
swL3VrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperMasterIpAddr.setStatus("current")


class _SwL3VrrpOperCriticalIpAddr_Type(IpAddress):
    """Custom type swL3VrrpOperCriticalIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SwL3VrrpOperCriticalIpAddr_Object = MibTableColumn
swL3VrrpOperCriticalIpAddr = _SwL3VrrpOperCriticalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 8),
    _SwL3VrrpOperCriticalIpAddr_Type()
)
swL3VrrpOperCriticalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperCriticalIpAddr.setStatus("current")


class _SwL3VrrpOperCheckCriticalIpState_Type(Integer32):
    """Custom type swL3VrrpOperCheckCriticalIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("other", 0))
    )


_SwL3VrrpOperCheckCriticalIpState_Type.__name__ = "Integer32"
_SwL3VrrpOperCheckCriticalIpState_Object = MibTableColumn
swL3VrrpOperCheckCriticalIpState = _SwL3VrrpOperCheckCriticalIpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 9),
    _SwL3VrrpOperCheckCriticalIpState_Type()
)
swL3VrrpOperCheckCriticalIpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperCheckCriticalIpState.setStatus("current")


class _SwL3VrrpOperAuthType_Type(Integer32):
    """Custom type swL3VrrpOperAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAuthenticationHeader", 3),
          ("noAuthentication", 1),
          ("simpleTextPassword", 2))
    )


_SwL3VrrpOperAuthType_Type.__name__ = "Integer32"
_SwL3VrrpOperAuthType_Object = MibTableColumn
swL3VrrpOperAuthType = _SwL3VrrpOperAuthType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 10),
    _SwL3VrrpOperAuthType_Type()
)
swL3VrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAuthType.setStatus("current")


class _SwL3VrrpOperAuthKey_Type(OctetString):
    """Custom type swL3VrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwL3VrrpOperAuthKey_Type.__name__ = "OctetString"
_SwL3VrrpOperAuthKey_Object = MibTableColumn
swL3VrrpOperAuthKey = _SwL3VrrpOperAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 11),
    _SwL3VrrpOperAuthKey_Type()
)
swL3VrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAuthKey.setStatus("current")


class _SwL3VrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type swL3VrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL3VrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_SwL3VrrpOperAdvertisementInterval_Object = MibTableColumn
swL3VrrpOperAdvertisementInterval = _SwL3VrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 12),
    _SwL3VrrpOperAdvertisementInterval_Type()
)
swL3VrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    swL3VrrpOperAdvertisementInterval.setUnits("seconds")


class _SwL3VrrpOperPreemptMode_Type(TruthValue):
    """Custom type swL3VrrpOperPreemptMode based on TruthValue"""


_SwL3VrrpOperPreemptMode_Object = MibTableColumn
swL3VrrpOperPreemptMode = _SwL3VrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 13),
    _SwL3VrrpOperPreemptMode_Type()
)
swL3VrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperPreemptMode.setStatus("current")
_SwL3VrrpOperVirtualRouterUpTime_Type = TimeStamp
_SwL3VrrpOperVirtualRouterUpTime_Object = MibTableColumn
swL3VrrpOperVirtualRouterUpTime = _SwL3VrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 14),
    _SwL3VrrpOperVirtualRouterUpTime_Type()
)
swL3VrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualRouterUpTime.setStatus("current")
_SwL3VrrpOperVirtualIpAddr_Type = IpAddress
_SwL3VrrpOperVirtualIpAddr_Object = MibTableColumn
swL3VrrpOperVirtualIpAddr = _SwL3VrrpOperVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 15),
    _SwL3VrrpOperVirtualIpAddr_Type()
)
swL3VrrpOperVirtualIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperVirtualIpAddr.setStatus("current")
_SwL3VrrpOperRowStatus_Type = RowStatus
_SwL3VrrpOperRowStatus_Object = MibTableColumn
swL3VrrpOperRowStatus = _SwL3VrrpOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 14, 1, 1, 16),
    _SwL3VrrpOperRowStatus_Type()
)
swL3VrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3VrrpOperRowStatus.setStatus("current")
_SwL3OspfECMPMgmt_ObjectIdentity = ObjectIdentity
swL3OspfECMPMgmt = _SwL3OspfECMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 15)
)


class _SwL3OspfECMPState_Type(Integer32):
    """Custom type swL3OspfECMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL3OspfECMPState_Type.__name__ = "Integer32"
_SwL3OspfECMPState_Object = MibScalar
swL3OspfECMPState = _SwL3OspfECMPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 15, 6),
    _SwL3OspfECMPState_Type()
)
swL3OspfECMPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfECMPState.setStatus("current")
_SwL3OspfDefInfoOrigMgmt_ObjectIdentity = ObjectIdentity
swL3OspfDefInfoOrigMgmt = _SwL3OspfDefInfoOrigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 18)
)


class _SwL3OspfDefInfoOriginate_Type(Integer32):
    """Custom type swL3OspfDefInfoOriginate based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("default", 2),
          ("none", 3))
    )


_SwL3OspfDefInfoOriginate_Type.__name__ = "Integer32"
_SwL3OspfDefInfoOriginate_Object = MibScalar
swL3OspfDefInfoOriginate = _SwL3OspfDefInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 18, 1),
    _SwL3OspfDefInfoOriginate_Type()
)
swL3OspfDefInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfDefInfoOriginate.setStatus("current")


class _SwL3OspfDefInfoOrigMetricType_Type(Integer32):
    """Custom type swL3OspfDefInfoOrigMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type-1", 1),
          ("type-2", 2))
    )


_SwL3OspfDefInfoOrigMetricType_Type.__name__ = "Integer32"
_SwL3OspfDefInfoOrigMetricType_Object = MibScalar
swL3OspfDefInfoOrigMetricType = _SwL3OspfDefInfoOrigMetricType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 18, 2),
    _SwL3OspfDefInfoOrigMetricType_Type()
)
swL3OspfDefInfoOrigMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfDefInfoOrigMetricType.setStatus("current")


class _SwL3OspfDefInfoOrigMetric_Type(Integer32):
    """Custom type swL3OspfDefInfoOrigMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL3OspfDefInfoOrigMetric_Type.__name__ = "Integer32"
_SwL3OspfDefInfoOrigMetric_Object = MibScalar
swL3OspfDefInfoOrigMetric = _SwL3OspfDefInfoOrigMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 3, 18, 3),
    _SwL3OspfDefInfoOrigMetric_Type()
)
swL3OspfDefInfoOrigMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3OspfDefInfoOrigMetric.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES-3810-52-L3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "VrId": VrId,
       "swL3MgmtMIB": swL3MgmtMIB,
       "swL3DevMgmt": swL3DevMgmt,
       "swL3DevCtrl": swL3DevCtrl,
       "swL3DevCtrlRIPState": swL3DevCtrlRIPState,
       "swL3DevCtrlOSPFState": swL3DevCtrlOSPFState,
       "swL3DevCtrlVRRPState": swL3DevCtrlVRRPState,
       "swL3DevCtrlVrrpPingState": swL3DevCtrlVrrpPingState,
       "swL3IpMgmt": swL3IpMgmt,
       "swL3IpCtrlMgmt": swL3IpCtrlMgmt,
       "swL3IpCtrlTable": swL3IpCtrlTable,
       "swL3IpCtrlEntry": swL3IpCtrlEntry,
       "swL3IpCtrlInterfaceName": swL3IpCtrlInterfaceName,
       "swL3IpCtrlIfIndex": swL3IpCtrlIfIndex,
       "swL3IpCtrlIpAddr": swL3IpCtrlIpAddr,
       "swL3IpCtrlIpSubnetMask": swL3IpCtrlIpSubnetMask,
       "swL3IpCtrlVlanName": swL3IpCtrlVlanName,
       "swL3IpCtrlProxyArp": swL3IpCtrlProxyArp,
       "swL3IpCtrlSecondary": swL3IpCtrlSecondary,
       "swL3IpCtrlMode": swL3IpCtrlMode,
       "swL3IpCtrlAdminState": swL3IpCtrlAdminState,
       "swL3IpCtrlIpv4AdminState": swL3IpCtrlIpv4AdminState,
       "swL3IpCtrlIpv6AdminState": swL3IpCtrlIpv6AdminState,
       "swL3IpCtrlIpv6LinkLocalAddress": swL3IpCtrlIpv6LinkLocalAddress,
       "swL3IpCtrlIpv6LinkLocalPrefixLen": swL3IpCtrlIpv6LinkLocalPrefixLen,
       "swL3IpCtrlState": swL3IpCtrlState,
       "swL3IpCtrlIpv6LinkLocalAutoState": swL3IpCtrlIpv6LinkLocalAutoState,
       "swL3IpCtrlLocalProxyArp": swL3IpCtrlLocalProxyArp,
       "swL3Ipv6CtrlTable": swL3Ipv6CtrlTable,
       "swL3Ipv6CtrlEntry": swL3Ipv6CtrlEntry,
       "swL3Ipv6CtrlInterfaceName": swL3Ipv6CtrlInterfaceName,
       "swL3Ipv6CtrlMaxReassmblySize": swL3Ipv6CtrlMaxReassmblySize,
       "swL3Ipv6CtrlNsRetransTimer": swL3Ipv6CtrlNsRetransTimer,
       "swL3Ipv6CtrlRaState": swL3Ipv6CtrlRaState,
       "swL3Ipv6CtrlRaMinRtrAdvInterval": swL3Ipv6CtrlRaMinRtrAdvInterval,
       "swL3Ipv6CtrlRaMaxRtrAdvInterval": swL3Ipv6CtrlRaMaxRtrAdvInterval,
       "swL3Ipv6CtrlRaLifeTime": swL3Ipv6CtrlRaLifeTime,
       "swL3Ipv6CtrlRaReachableTime": swL3Ipv6CtrlRaReachableTime,
       "swL3Ipv6CtrlRaRetransTime": swL3Ipv6CtrlRaRetransTime,
       "swL3Ipv6CtrlRaHopLimit": swL3Ipv6CtrlRaHopLimit,
       "swL3Ipv6CtrlRaManagedFlag": swL3Ipv6CtrlRaManagedFlag,
       "swL3Ipv6CtrlRaOtherConfigFlag": swL3Ipv6CtrlRaOtherConfigFlag,
       "swL3Ipv6AddressCtrlTable": swL3Ipv6AddressCtrlTable,
       "swL3Ipv6AddressCtrlEntry": swL3Ipv6AddressCtrlEntry,
       "swL3Ipv6AddressCtrlInterfaceName": swL3Ipv6AddressCtrlInterfaceName,
       "swL3Ipv6Address": swL3Ipv6Address,
       "swL3Ipv6AddressCtrlPrefixLen": swL3Ipv6AddressCtrlPrefixLen,
       "swL3Ipv6AddressCtrlPreferredLifeTime": swL3Ipv6AddressCtrlPreferredLifeTime,
       "swL3Ipv6AddressCtrlValidLifeTime": swL3Ipv6AddressCtrlValidLifeTime,
       "swL3Ipv6AddressCtrlOnLinkFlag": swL3Ipv6AddressCtrlOnLinkFlag,
       "swL3Ipv6AddressCtrlAutonomousFlag": swL3Ipv6AddressCtrlAutonomousFlag,
       "swL3Ipv6AddressCtrlState": swL3Ipv6AddressCtrlState,
       "swL3IpCtrlAllIpIfState": swL3IpCtrlAllIpIfState,
       "swL3LoopBackIpCtrlTable": swL3LoopBackIpCtrlTable,
       "swL3LoopBackIpCtrlEntry": swL3LoopBackIpCtrlEntry,
       "swL3LoopBackIpCtrlInterfaceName": swL3LoopBackIpCtrlInterfaceName,
       "swL3LoopBackIpCtrlIfIndex": swL3LoopBackIpCtrlIfIndex,
       "swL3LoopBackIpCtrlIpAddr": swL3LoopBackIpCtrlIpAddr,
       "swL3LoopBackIpCtrlIpSubnetMask": swL3LoopBackIpCtrlIpSubnetMask,
       "swL3LoopBackIpCtrlAdminState": swL3LoopBackIpCtrlAdminState,
       "swL3LoopBackIpCtrlRowStatus": swL3LoopBackIpCtrlRowStatus,
       "swL3IpFdbMgmt": swL3IpFdbMgmt,
       "swL3IpFdbInfoTable": swL3IpFdbInfoTable,
       "swL3IpFdbInfoEntry": swL3IpFdbInfoEntry,
       "swL3IpFdbInfoIpAddr": swL3IpFdbInfoIpAddr,
       "swL3IpFdbInfoIpSubnetMask": swL3IpFdbInfoIpSubnetMask,
       "swL3IpFdbInfoPort": swL3IpFdbInfoPort,
       "swL3IpFdbInfoType": swL3IpFdbInfoType,
       "swL3IpArpAgingTime": swL3IpArpAgingTime,
       "swL3IpStaticRouteTable": swL3IpStaticRouteTable,
       "swL3IpStaticRouteEntry": swL3IpStaticRouteEntry,
       "swL3IpStaticRouteDest": swL3IpStaticRouteDest,
       "swL3IpStaticRouteMask": swL3IpStaticRouteMask,
       "swL3IpStaticRouteBkupState": swL3IpStaticRouteBkupState,
       "swL3IpStaticRouteNextHop": swL3IpStaticRouteNextHop,
       "swL3IpStaticRouteMetric": swL3IpStaticRouteMetric,
       "swL3IpStaticRouteStatus": swL3IpStaticRouteStatus,
       "swL3IpStaticRouteWeight": swL3IpStaticRouteWeight,
       "swL3RelayMgmt": swL3RelayMgmt,
       "swL3RelayDnsMgmt": swL3RelayDnsMgmt,
       "swL3RelayDnsState": swL3RelayDnsState,
       "swL3RelayDnsPrimaryServer": swL3RelayDnsPrimaryServer,
       "swL3RelayDnsSecondaryServer": swL3RelayDnsSecondaryServer,
       "swL3RelayDnsCacheState": swL3RelayDnsCacheState,
       "swL3RelayDnsStaticTableState": swL3RelayDnsStaticTableState,
       "swL3RelayDnsCtrlTable": swL3RelayDnsCtrlTable,
       "swL3RelayDnsCtrlEntry": swL3RelayDnsCtrlEntry,
       "swL3RelayDnsCtrlDomainName": swL3RelayDnsCtrlDomainName,
       "swL3RelayDnsCtrlIpAddr": swL3RelayDnsCtrlIpAddr,
       "swL3RelayDnsCtrlState": swL3RelayDnsCtrlState,
       "swL3RelayDnsCtrlHostTable": swL3RelayDnsCtrlHostTable,
       "swL3RelayDnsCtrlHostEntry": swL3RelayDnsCtrlHostEntry,
       "swL3RelayDnsCtrlHostDomainName": swL3RelayDnsCtrlHostDomainName,
       "swL3RelayDnsCtrlHostAddressType": swL3RelayDnsCtrlHostAddressType,
       "swL3RelayDnsCtrlHostAddress": swL3RelayDnsCtrlHostAddress,
       "swL3RelayDnsCtrlHostRowStatus": swL3RelayDnsCtrlHostRowStatus,
       "swL3Md5Table": swL3Md5Table,
       "swL3Md5Entry": swL3Md5Entry,
       "swL3Md5KeyId": swL3Md5KeyId,
       "swL3Md5Key": swL3Md5Key,
       "swL3Md5RowStatus": swL3Md5RowStatus,
       "swL3RouteRedistriTable": swL3RouteRedistriTable,
       "swL3RouteRedistriEntry": swL3RouteRedistriEntry,
       "swL3RouteRedistriSrcProtocol": swL3RouteRedistriSrcProtocol,
       "swL3RouteRedistriDstProtocol": swL3RouteRedistriDstProtocol,
       "swL3RouteRedistriType": swL3RouteRedistriType,
       "swL3RouteRedistriMetric": swL3RouteRedistriMetric,
       "swL3RouteRedistriRowStatus": swL3RouteRedistriRowStatus,
       "swL3OspfHostTable": swL3OspfHostTable,
       "swL3OspfHostEntry": swL3OspfHostEntry,
       "swL3OspfHostIpAddress": swL3OspfHostIpAddress,
       "swL3OspfHostTOS": swL3OspfHostTOS,
       "swL3OspfHostMetric": swL3OspfHostMetric,
       "swL3OspfHostAreaID": swL3OspfHostAreaID,
       "swL3OspfHostStatus": swL3OspfHostStatus,
       "swL3ospfVirtIfTable": swL3ospfVirtIfTable,
       "swL3ospfVirtIfEntry": swL3ospfVirtIfEntry,
       "swL3ospfVirtIfAreaId": swL3ospfVirtIfAreaId,
       "swL3ospfVirtIfNeighbor": swL3ospfVirtIfNeighbor,
       "swL3ospfVirtIfTransitDelay": swL3ospfVirtIfTransitDelay,
       "swL3ospfVirtIfRetransInterval": swL3ospfVirtIfRetransInterval,
       "swL3ospfVirtIfHelloInterval": swL3ospfVirtIfHelloInterval,
       "swL3ospfVirtIfRtrDeadInterval": swL3ospfVirtIfRtrDeadInterval,
       "swL3ospfVirtIfState": swL3ospfVirtIfState,
       "swL3ospfVirtIfEvents": swL3ospfVirtIfEvents,
       "swL3ospfVirtIfAuthType": swL3ospfVirtIfAuthType,
       "swL3ospfVirtIfAuthKey": swL3ospfVirtIfAuthKey,
       "swL3ospfVirtIfAuthKeyID": swL3ospfVirtIfAuthKeyID,
       "swL3ospfVirtIfStatus": swL3ospfVirtIfStatus,
       "swL3ospfIfTable": swL3ospfIfTable,
       "swL3ospfIfEntry": swL3ospfIfEntry,
       "swL3ospfIfIpAddress": swL3ospfIfIpAddress,
       "swL3ospfAddressLessIf": swL3ospfAddressLessIf,
       "swL3ospfIfAreaId": swL3ospfIfAreaId,
       "swL3ospfIfType": swL3ospfIfType,
       "swL3ospfIfAdminStat": swL3ospfIfAdminStat,
       "swL3ospfIfRtrPriority": swL3ospfIfRtrPriority,
       "swL3ospfIfTransitDelay": swL3ospfIfTransitDelay,
       "swL3ospfIfRetransInterval": swL3ospfIfRetransInterval,
       "swL3ospfIfHelloInterval": swL3ospfIfHelloInterval,
       "swL3ospfIfRtrDeadInterval": swL3ospfIfRtrDeadInterval,
       "swL3ospfIfPollInterval": swL3ospfIfPollInterval,
       "swL3ospfIfState": swL3ospfIfState,
       "swL3ospfIfDesignatedRouter": swL3ospfIfDesignatedRouter,
       "swL3ospfIfBackupDesignatedRouter": swL3ospfIfBackupDesignatedRouter,
       "swL3ospfIfEvents": swL3ospfIfEvents,
       "swL3ospfIfMulticastForwarding": swL3ospfIfMulticastForwarding,
       "swL3ospfIfDemand": swL3ospfIfDemand,
       "swL3ospfIfAuthType": swL3ospfIfAuthType,
       "swL3ospfIfAuthKey": swL3ospfIfAuthKey,
       "swL3ospfIfAuthKeyID": swL3ospfIfAuthKeyID,
       "swL3ospfIfPassiveMode": swL3ospfIfPassiveMode,
       "swL3ospfIfMetric": swL3ospfIfMetric,
       "swL3RoutePreference": swL3RoutePreference,
       "swL3RoutePreferenceRIP": swL3RoutePreferenceRIP,
       "swL3RoutePreferenceOSPFIntra": swL3RoutePreferenceOSPFIntra,
       "swL3RoutePreferenceStatic": swL3RoutePreferenceStatic,
       "swL3RoutePreferenceLocal": swL3RoutePreferenceLocal,
       "swL3RoutePreferenceOSPFInter": swL3RoutePreferenceOSPFInter,
       "swL3RoutePreferenceOSPFExtT1": swL3RoutePreferenceOSPFExtT1,
       "swL3RoutePreferenceOSPFExtT2": swL3RoutePreferenceOSPFExtT2,
       "swL3RoutePreferenceDefault": swL3RoutePreferenceDefault,
       "swL3ospfAreaTable": swL3ospfAreaTable,
       "swL3ospfAreaEntry": swL3ospfAreaEntry,
       "swL3ospfAreaId": swL3ospfAreaId,
       "swL3ospfAreaType": swL3ospfAreaType,
       "swL3ospfAreaSummaryState": swL3ospfAreaSummaryState,
       "swL3ospfAreaMetric": swL3ospfAreaMetric,
       "swL3ospfAreaTranslateState": swL3ospfAreaTranslateState,
       "swL3ospfAreaStatus": swL3ospfAreaStatus,
       "swL3OspfLsdbMgmt": swL3OspfLsdbMgmt,
       "swL3OspfInternalLsdbTable": swL3OspfInternalLsdbTable,
       "swL3OspfInternalLsdbEntry": swL3OspfInternalLsdbEntry,
       "swL3OspfInternalLsdbAreaId": swL3OspfInternalLsdbAreaId,
       "swL3OspfInternalLsdbType": swL3OspfInternalLsdbType,
       "swL3OspfInternalLsdbLsid": swL3OspfInternalLsdbLsid,
       "swL3OspfInternalLsdbRouterId": swL3OspfInternalLsdbRouterId,
       "swL3OspfInternalLsdbMetric": swL3OspfInternalLsdbMetric,
       "swL3OspfInternalLsdbSequenceNo": swL3OspfInternalLsdbSequenceNo,
       "swL3OspfInternalLsdbAge": swL3OspfInternalLsdbAge,
       "swL3OspfInternalLsdbChecksum": swL3OspfInternalLsdbChecksum,
       "swL3OspfExternalLsdbTable": swL3OspfExternalLsdbTable,
       "swL3OspfExternalLsdbEntry": swL3OspfExternalLsdbEntry,
       "swL3OspfExternalLsdbType": swL3OspfExternalLsdbType,
       "swL3OspfExternalLsdbLsid": swL3OspfExternalLsdbLsid,
       "swL3OspfExternalLsdbRouterId": swL3OspfExternalLsdbRouterId,
       "swL3OspfExternalLsdbMetric": swL3OspfExternalLsdbMetric,
       "swL3OspfExternalLsdbMetricType": swL3OspfExternalLsdbMetricType,
       "swL3OspfExternalLsdbSequenceNo": swL3OspfExternalLsdbSequenceNo,
       "swL3OspfExternalLsdbAge": swL3OspfExternalLsdbAge,
       "swL3OspfExternalLsdbChecksum": swL3OspfExternalLsdbChecksum,
       "swL3OspfExternalLsdbForwardingAddress": swL3OspfExternalLsdbForwardingAddress,
       "swL3OspfExternalLsdbRouteTag": swL3OspfExternalLsdbRouteTag,
       "swL3VrrpOperMgmt": swL3VrrpOperMgmt,
       "swL3VrrpOperTable": swL3VrrpOperTable,
       "swL3VrrpOperEntry": swL3VrrpOperEntry,
       "swL3VrrpOperIfIndex": swL3VrrpOperIfIndex,
       "swL3VrrpOperVrId": swL3VrrpOperVrId,
       "swL3VrrpOperVirtualMacAddr": swL3VrrpOperVirtualMacAddr,
       "swL3VrrpOperState": swL3VrrpOperState,
       "swL3VrrpOperAdminState": swL3VrrpOperAdminState,
       "swL3VrrpOperPriority": swL3VrrpOperPriority,
       "swL3VrrpOperMasterIpAddr": swL3VrrpOperMasterIpAddr,
       "swL3VrrpOperCriticalIpAddr": swL3VrrpOperCriticalIpAddr,
       "swL3VrrpOperCheckCriticalIpState": swL3VrrpOperCheckCriticalIpState,
       "swL3VrrpOperAuthType": swL3VrrpOperAuthType,
       "swL3VrrpOperAuthKey": swL3VrrpOperAuthKey,
       "swL3VrrpOperAdvertisementInterval": swL3VrrpOperAdvertisementInterval,
       "swL3VrrpOperPreemptMode": swL3VrrpOperPreemptMode,
       "swL3VrrpOperVirtualRouterUpTime": swL3VrrpOperVirtualRouterUpTime,
       "swL3VrrpOperVirtualIpAddr": swL3VrrpOperVirtualIpAddr,
       "swL3VrrpOperRowStatus": swL3VrrpOperRowStatus,
       "swL3OspfECMPMgmt": swL3OspfECMPMgmt,
       "swL3OspfECMPState": swL3OspfECMPState,
       "swL3OspfDefInfoOrigMgmt": swL3OspfDefInfoOrigMgmt,
       "swL3OspfDefInfoOriginate": swL3OspfDefInfoOriginate,
       "swL3OspfDefInfoOrigMetricType": swL3OspfDefInfoOrigMetricType,
       "swL3OspfDefInfoOrigMetric": swL3OspfDefInfoOrigMetric}
)
