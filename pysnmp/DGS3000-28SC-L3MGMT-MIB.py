# SNMP MIB module (DGS3000-28SC-L3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS3000-28SC-L3MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:19 2024
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

(dlink_Dgs3000Proj_DGS3000_28SCax,) = mibBuilder.importSymbols(
    "SWDGS3000PRIMGMT-MIB",
    "dlink-Dgs3000Proj-DGS3000-28SCax")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3)
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

_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3IpCtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 6),
    _SwL3IpCtrlProxyArp_Type()
)
swL3IpCtrlProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlProxyArp.setStatus("current")
_SwL3IpCtrlSecondary_Type = TruthValue
_SwL3IpCtrlSecondary_Object = MibTableColumn
swL3IpCtrlSecondary = _SwL3IpCtrlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 7),
    _SwL3IpCtrlSecondary_Type()
)
swL3IpCtrlSecondary.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 12),
    _SwL3IpCtrlIpv6AdminState_Type()
)
swL3IpCtrlIpv6AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 18),
    _SwL3IpCtrlLocalProxyArp_Type()
)
swL3IpCtrlLocalProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlLocalProxyArp.setStatus("current")


class _SwL3IpCtrlIpMtu_Type(Integer32):
    """Custom type swL3IpCtrlIpMtu based on Integer32"""
    defaultValue = 1500


_SwL3IpCtrlIpMtu_Object = MibTableColumn
swL3IpCtrlIpMtu = _SwL3IpCtrlIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 19),
    _SwL3IpCtrlIpMtu_Type()
)
swL3IpCtrlIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpCtrlIpMtu.setStatus("current")
if mibBuilder.loadTexts:
    swL3IpCtrlIpMtu.setUnits("bytes")


class _SwL3IpCtrlDhcpv6ClientState_Type(Integer32):
    """Custom type swL3IpCtrlDhcpv6ClientState based on Integer32"""
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


_SwL3IpCtrlDhcpv6ClientState_Type.__name__ = "Integer32"
_SwL3IpCtrlDhcpv6ClientState_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientState = _SwL3IpCtrlDhcpv6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 20),
    _SwL3IpCtrlDhcpv6ClientState_Type()
)
swL3IpCtrlDhcpv6ClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientState.setStatus("current")


class _SwL3IpCtrlIpDirectedBroadcastState_Type(Integer32):
    """Custom type swL3IpCtrlIpDirectedBroadcastState based on Integer32"""
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


_SwL3IpCtrlIpDirectedBroadcastState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpDirectedBroadcastState_Object = MibTableColumn
swL3IpCtrlIpDirectedBroadcastState = _SwL3IpCtrlIpDirectedBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 21),
    _SwL3IpCtrlIpDirectedBroadcastState_Type()
)
swL3IpCtrlIpDirectedBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDirectedBroadcastState.setStatus("current")


class _SwL3IpCtrlIpDhcpOption12State_Type(Integer32):
    """Custom type swL3IpCtrlIpDhcpOption12State based on Integer32"""
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


_SwL3IpCtrlIpDhcpOption12State_Type.__name__ = "Integer32"
_SwL3IpCtrlIpDhcpOption12State_Object = MibTableColumn
swL3IpCtrlIpDhcpOption12State = _SwL3IpCtrlIpDhcpOption12State_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 22),
    _SwL3IpCtrlIpDhcpOption12State_Type()
)
swL3IpCtrlIpDhcpOption12State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12State.setStatus("current")


class _SwL3IpCtrlIpDhcpOption12HostName_Type(DisplayString):
    """Custom type swL3IpCtrlIpDhcpOption12HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SwL3IpCtrlIpDhcpOption12HostName_Type.__name__ = "DisplayString"
_SwL3IpCtrlIpDhcpOption12HostName_Object = MibTableColumn
swL3IpCtrlIpDhcpOption12HostName = _SwL3IpCtrlIpDhcpOption12HostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 23),
    _SwL3IpCtrlIpDhcpOption12HostName_Type()
)
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12HostName.setStatus("current")


class _SwL3IpCtrlDhcpv6ClientPDState_Type(Integer32):
    """Custom type swL3IpCtrlDhcpv6ClientPDState based on Integer32"""
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


_SwL3IpCtrlDhcpv6ClientPDState_Type.__name__ = "Integer32"
_SwL3IpCtrlDhcpv6ClientPDState_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDState = _SwL3IpCtrlDhcpv6ClientPDState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 24),
    _SwL3IpCtrlDhcpv6ClientPDState_Type()
)
swL3IpCtrlDhcpv6ClientPDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDState.setStatus("current")


class _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type(DisplayString):
    """Custom type swL3IpCtrlDhcpv6ClientPDPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL3IpCtrlDhcpv6ClientPDPrefixName_Type.__name__ = "DisplayString"
_SwL3IpCtrlDhcpv6ClientPDPrefixName_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixName = _SwL3IpCtrlDhcpv6ClientPDPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 25),
    _SwL3IpCtrlDhcpv6ClientPDPrefixName_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefixName.setStatus("current")
_SwL3IpCtrlDhcpv6ClientPDPrefix_Type = Ipv6Address
_SwL3IpCtrlDhcpv6ClientPDPrefix_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefix = _SwL3IpCtrlDhcpv6ClientPDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 26),
    _SwL3IpCtrlDhcpv6ClientPDPrefix_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefix.setStatus("current")
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type = Integer32
_SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDPrefixLen = _SwL3IpCtrlDhcpv6ClientPDPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 27),
    _SwL3IpCtrlDhcpv6ClientPDPrefixLen_Type()
)
swL3IpCtrlDhcpv6ClientPDPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDPrefixLen.setStatus("current")


class _SwL3IpCtrlIpv6AutoConfigState_Type(Integer32):
    """Custom type swL3IpCtrlIpv6AutoConfigState based on Integer32"""
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


_SwL3IpCtrlIpv6AutoConfigState_Type.__name__ = "Integer32"
_SwL3IpCtrlIpv6AutoConfigState_Object = MibTableColumn
swL3IpCtrlIpv6AutoConfigState = _SwL3IpCtrlIpv6AutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 28),
    _SwL3IpCtrlIpv6AutoConfigState_Type()
)
swL3IpCtrlIpv6AutoConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AutoConfigState.setStatus("current")
_SwL3IpCtrlIpv6AutoConfigDefault_Type = TruthValue
_SwL3IpCtrlIpv6AutoConfigDefault_Object = MibTableColumn
swL3IpCtrlIpv6AutoConfigDefault = _SwL3IpCtrlIpv6AutoConfigDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 29),
    _SwL3IpCtrlIpv6AutoConfigDefault_Type()
)
swL3IpCtrlIpv6AutoConfigDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AutoConfigDefault.setStatus("current")
_SwL3IpCtrlDhcpv6ClientRapidCommit_Type = TruthValue
_SwL3IpCtrlDhcpv6ClientRapidCommit_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientRapidCommit = _SwL3IpCtrlDhcpv6ClientRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 30),
    _SwL3IpCtrlDhcpv6ClientRapidCommit_Type()
)
swL3IpCtrlDhcpv6ClientRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientRapidCommit.setStatus("current")
_SwL3IpCtrlDhcpv6ClientPDRapidCommit_Type = TruthValue
_SwL3IpCtrlDhcpv6ClientPDRapidCommit_Object = MibTableColumn
swL3IpCtrlDhcpv6ClientPDRapidCommit = _SwL3IpCtrlDhcpv6ClientPDRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 3, 1, 31),
    _SwL3IpCtrlDhcpv6ClientPDRapidCommit_Type()
)
swL3IpCtrlDhcpv6ClientPDRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientPDRapidCommit.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")
_SwL3Ipv6CtrlMaxReassmblySize_Type = Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object = MibTableColumn
swL3Ipv6CtrlMaxReassmblySize = _SwL3Ipv6CtrlMaxReassmblySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 13),
    _SwL3Ipv6CtrlRaOtherConfigFlag_Type()
)
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaOtherConfigFlag.setStatus("current")


class _SwL3Ipv6CtrlDadRetransNum_Type(Integer32):
    """Custom type swL3Ipv6CtrlDadRetransNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL3Ipv6CtrlDadRetransNum_Type.__name__ = "Integer32"
_SwL3Ipv6CtrlDadRetransNum_Object = MibTableColumn
swL3Ipv6CtrlDadRetransNum = _SwL3Ipv6CtrlDadRetransNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 4, 1, 14),
    _SwL3Ipv6CtrlDadRetransNum_Type()
)
swL3Ipv6CtrlDadRetransNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlDadRetransNum.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 7),
    _SwL3Ipv6AddressCtrlAutonomousFlag_Type()
)
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAutonomousFlag.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 8),
    _SwL3Ipv6AddressCtrlState_Type()
)
swL3Ipv6AddressCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlState.setStatus("current")


class _SwL3Ipv6AddressCtrlAddressType_Type(Integer32):
    """Custom type swL3Ipv6AddressCtrlAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcpv6", 2),
          ("manual", 1),
          ("stateless", 3))
    )


_SwL3Ipv6AddressCtrlAddressType_Type.__name__ = "Integer32"
_SwL3Ipv6AddressCtrlAddressType_Object = MibTableColumn
swL3Ipv6AddressCtrlAddressType = _SwL3Ipv6AddressCtrlAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 5, 1, 9),
    _SwL3Ipv6AddressCtrlAddressType_Type()
)
swL3Ipv6AddressCtrlAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAddressType.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object = MibTable
swL3Ipv6DHCPv6CPDAddrCtrlTable = _SwL3Ipv6DHCPv6CPDAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlTable.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object = MibTableRow
swL3Ipv6DHCPv6CPDAddrCtrlEntry = _SwL3Ipv6DHCPv6CPDAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1)
)
swL3Ipv6DHCPv6CPDAddrCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlPrefixName"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen"),
)
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlEntry.setStatus("current")


class _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type(DisplayString):
    """Custom type swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName = _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1, 1),
    _SwL3Ipv6DHCPv6CPDAddrCtrlInterfaceName_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName.setStatus("current")


class _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type(DisplayString):
    """Custom type swL3Ipv6DHCPv6CPDAddrCtrlPrefixName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type.__name__ = "DisplayString"
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName = _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1, 2),
    _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixName_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlPrefixName.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type = Ipv6Address
_SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr = _SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1, 3),
    _SwL3Ipv6DHCPv6CPDAddrCtrlIPv6addr_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type = Integer32
_SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen = _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1, 4),
    _SwL3Ipv6DHCPv6CPDAddrCtrlPrefixLen_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen.setStatus("current")
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Type = RowStatus
_SwL3Ipv6DHCPv6CPDAddrCtrlState_Object = MibTableColumn
swL3Ipv6DHCPv6CPDAddrCtrlState = _SwL3Ipv6DHCPv6CPDAddrCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 6, 1, 5),
    _SwL3Ipv6DHCPv6CPDAddrCtrlState_Type()
)
swL3Ipv6DHCPv6CPDAddrCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3Ipv6DHCPv6CPDAddrCtrlState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")
_SwL3LoopBackIpCtrlTable_Object = MibTable
swL3LoopBackIpCtrlTable = _SwL3LoopBackIpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlTable.setStatus("current")
_SwL3LoopBackIpCtrlEntry_Object = MibTableRow
swL3LoopBackIpCtrlEntry = _SwL3LoopBackIpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1)
)
swL3LoopBackIpCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3LoopBackIpCtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 2),
    _SwL3LoopBackIpCtrlIfIndex_Type()
)
swL3LoopBackIpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIfIndex.setStatus("current")
_SwL3LoopBackIpCtrlIpAddr_Type = IpAddress
_SwL3LoopBackIpCtrlIpAddr_Object = MibTableColumn
swL3LoopBackIpCtrlIpAddr = _SwL3LoopBackIpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 3),
    _SwL3LoopBackIpCtrlIpAddr_Type()
)
swL3LoopBackIpCtrlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlIpAddr.setStatus("current")
_SwL3LoopBackIpCtrlIpSubnetMask_Type = IpAddress
_SwL3LoopBackIpCtrlIpSubnetMask_Object = MibTableColumn
swL3LoopBackIpCtrlIpSubnetMask = _SwL3LoopBackIpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 5),
    _SwL3LoopBackIpCtrlAdminState_Type()
)
swL3LoopBackIpCtrlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlAdminState.setStatus("current")
_SwL3LoopBackIpCtrlRowStatus_Type = RowStatus
_SwL3LoopBackIpCtrlRowStatus_Object = MibTableColumn
swL3LoopBackIpCtrlRowStatus = _SwL3LoopBackIpCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 1, 8, 1, 6),
    _SwL3LoopBackIpCtrlRowStatus_Type()
)
swL3LoopBackIpCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3LoopBackIpCtrlRowStatus.setStatus("current")
_SwL3IpFdbMgmt_ObjectIdentity = ObjectIdentity
swL3IpFdbMgmt = _SwL3IpFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2)
)
_SwL3IpFdbInfoTable_Object = MibTable
swL3IpFdbInfoTable = _SwL3IpFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoTable.setStatus("current")
_SwL3IpFdbInfoEntry_Object = MibTableRow
swL3IpFdbInfoEntry = _SwL3IpFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1, 1)
)
swL3IpFdbInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3IpFdbInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoEntry.setStatus("current")
_SwL3IpFdbInfoIpAddr_Type = IpAddress
_SwL3IpFdbInfoIpAddr_Object = MibTableColumn
swL3IpFdbInfoIpAddr = _SwL3IpFdbInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1, 1, 1),
    _SwL3IpFdbInfoIpAddr_Type()
)
swL3IpFdbInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpAddr.setStatus("current")
_SwL3IpFdbInfoIpSubnetMask_Type = IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object = MibTableColumn
swL3IpFdbInfoIpSubnetMask = _SwL3IpFdbInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 4),
    _SwL3IpArpAgingTime_Type()
)
swL3IpArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpAgingTime.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteBkupState_Type()
)
swL3IpStaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteBkupState.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 6),
    _SwL3IpStaticRouteStatus_Type()
)
swL3IpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteStatus.setStatus("current")


class _SwL3IpStaticRouteWeight_Type(Integer32):
    """Custom type swL3IpStaticRouteWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SwL3IpStaticRouteWeight_Type.__name__ = "Integer32"
_SwL3IpStaticRouteWeight_Object = MibTableColumn
swL3IpStaticRouteWeight = _SwL3IpStaticRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 7),
    _SwL3IpStaticRouteWeight_Type()
)
swL3IpStaticRouteWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteWeight.setStatus("current")
_SwL3IpStaticRouteInterfaceName_Type = DisplayString
_SwL3IpStaticRouteInterfaceName_Object = MibTableColumn
swL3IpStaticRouteInterfaceName = _SwL3IpStaticRouteInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 8),
    _SwL3IpStaticRouteInterfaceName_Type()
)
swL3IpStaticRouteInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteInterfaceName.setStatus("current")
_SwL3IpStaticRouteCost_Type = Integer32
_SwL3IpStaticRouteCost_Object = MibTableColumn
swL3IpStaticRouteCost = _SwL3IpStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 2, 5, 1, 9),
    _SwL3IpStaticRouteCost_Type()
)
swL3IpStaticRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteCost.setStatus("current")
_SwL3RelayMgmt_ObjectIdentity = ObjectIdentity
swL3RelayMgmt = _SwL3RelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3)
)
_SwL3RelayDnsMgmt_ObjectIdentity = ObjectIdentity
swL3RelayDnsMgmt = _SwL3RelayDnsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 1),
    _SwL3RelayDnsState_Type()
)
swL3RelayDnsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsState.setStatus("current")
_SwL3RelayDnsPrimaryServer_Type = IpAddress
_SwL3RelayDnsPrimaryServer_Object = MibScalar
swL3RelayDnsPrimaryServer = _SwL3RelayDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 2),
    _SwL3RelayDnsPrimaryServer_Type()
)
swL3RelayDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsPrimaryServer.setStatus("current")
_SwL3RelayDnsSecondaryServer_Type = IpAddress
_SwL3RelayDnsSecondaryServer_Object = MibScalar
swL3RelayDnsSecondaryServer = _SwL3RelayDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 5),
    _SwL3RelayDnsStaticTableState_Type()
)
swL3RelayDnsStaticTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsStaticTableState.setStatus("current")
_SwL3RelayDnsCtrlTable_Object = MibTable
swL3RelayDnsCtrlTable = _SwL3RelayDnsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlTable.setStatus("current")
_SwL3RelayDnsCtrlEntry_Object = MibTableRow
swL3RelayDnsCtrlEntry = _SwL3RelayDnsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 6, 1)
)
swL3RelayDnsCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3RelayDnsCtrlDomainName"),
    (0, "DGS3000-28SC-L3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 6, 1, 1),
    _SwL3RelayDnsCtrlDomainName_Type()
)
swL3RelayDnsCtrlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlDomainName.setStatus("current")
_SwL3RelayDnsCtrlIpAddr_Type = IpAddress
_SwL3RelayDnsCtrlIpAddr_Object = MibTableColumn
swL3RelayDnsCtrlIpAddr = _SwL3RelayDnsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 3, 3, 2, 6, 1, 3),
    _SwL3RelayDnsCtrlState_Type()
)
swL3RelayDnsCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3RelayDnsCtrlState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS3000-28SC-L3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "VrId": VrId,
       "swL3MgmtMIB": swL3MgmtMIB,
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
       "swL3IpCtrlIpMtu": swL3IpCtrlIpMtu,
       "swL3IpCtrlDhcpv6ClientState": swL3IpCtrlDhcpv6ClientState,
       "swL3IpCtrlIpDirectedBroadcastState": swL3IpCtrlIpDirectedBroadcastState,
       "swL3IpCtrlIpDhcpOption12State": swL3IpCtrlIpDhcpOption12State,
       "swL3IpCtrlIpDhcpOption12HostName": swL3IpCtrlIpDhcpOption12HostName,
       "swL3IpCtrlDhcpv6ClientPDState": swL3IpCtrlDhcpv6ClientPDState,
       "swL3IpCtrlDhcpv6ClientPDPrefixName": swL3IpCtrlDhcpv6ClientPDPrefixName,
       "swL3IpCtrlDhcpv6ClientPDPrefix": swL3IpCtrlDhcpv6ClientPDPrefix,
       "swL3IpCtrlDhcpv6ClientPDPrefixLen": swL3IpCtrlDhcpv6ClientPDPrefixLen,
       "swL3IpCtrlIpv6AutoConfigState": swL3IpCtrlIpv6AutoConfigState,
       "swL3IpCtrlIpv6AutoConfigDefault": swL3IpCtrlIpv6AutoConfigDefault,
       "swL3IpCtrlDhcpv6ClientRapidCommit": swL3IpCtrlDhcpv6ClientRapidCommit,
       "swL3IpCtrlDhcpv6ClientPDRapidCommit": swL3IpCtrlDhcpv6ClientPDRapidCommit,
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
       "swL3Ipv6CtrlDadRetransNum": swL3Ipv6CtrlDadRetransNum,
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
       "swL3Ipv6AddressCtrlAddressType": swL3Ipv6AddressCtrlAddressType,
       "swL3Ipv6DHCPv6CPDAddrCtrlTable": swL3Ipv6DHCPv6CPDAddrCtrlTable,
       "swL3Ipv6DHCPv6CPDAddrCtrlEntry": swL3Ipv6DHCPv6CPDAddrCtrlEntry,
       "swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName": swL3Ipv6DHCPv6CPDAddrCtrlInterfaceName,
       "swL3Ipv6DHCPv6CPDAddrCtrlPrefixName": swL3Ipv6DHCPv6CPDAddrCtrlPrefixName,
       "swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr": swL3Ipv6DHCPv6CPDAddrCtrlIPv6addr,
       "swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen": swL3Ipv6DHCPv6CPDAddrCtrlPrefixLen,
       "swL3Ipv6DHCPv6CPDAddrCtrlState": swL3Ipv6DHCPv6CPDAddrCtrlState,
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
       "swL3IpStaticRouteInterfaceName": swL3IpStaticRouteInterfaceName,
       "swL3IpStaticRouteCost": swL3IpStaticRouteCost,
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
       "swL3RelayDnsCtrlState": swL3RelayDnsCtrlState}
)
