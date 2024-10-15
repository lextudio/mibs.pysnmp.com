# SNMP MIB module (DGS-3120-24PC-L3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-3120-24PC-L3MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:07 2024
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(dlink_Dgs3120Proj_Dgs3120_24PC,) = mibBuilder.importSymbols(
    "SWDGS3120PRIMGMT-MIB",
    "dlink-Dgs3120Proj-Dgs3120-24PC")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3)
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



# MIB Managed Objects in the order of their OIDs

_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3IpCtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 6),
    _SwL3IpCtrlProxyArp_Type()
)
swL3IpCtrlProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlProxyArp.setStatus("current")
_SwL3IpCtrlSecondary_Type = TruthValue
_SwL3IpCtrlSecondary_Object = MibTableColumn
swL3IpCtrlSecondary = _SwL3IpCtrlSecondary_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 12),
    _SwL3IpCtrlIpv6AdminState_Type()
)
swL3IpCtrlIpv6AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6AdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 18),
    _SwL3IpCtrlLocalProxyArp_Type()
)
swL3IpCtrlLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlLocalProxyArp.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 20),
    _SwL3IpCtrlDhcpv6ClientState_Type()
)
swL3IpCtrlDhcpv6ClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlDhcpv6ClientState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 3, 1, 23),
    _SwL3IpCtrlIpDhcpOption12HostName_Type()
)
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12HostName.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")
_SwL3Ipv6CtrlMaxReassmblySize_Type = Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object = MibTableColumn
swL3Ipv6CtrlMaxReassmblySize = _SwL3Ipv6CtrlMaxReassmblySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 4, 1, 3),
    _SwL3Ipv6CtrlNsRetransTimer_Type()
)
swL3Ipv6CtrlNsRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlNsRetransTimer.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1, 3),
    _SwL3Ipv6AddressCtrlPrefixLen_Type()
)
swL3Ipv6AddressCtrlPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlPrefixLen.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 5, 1, 9),
    _SwL3Ipv6AddressCtrlAddressType_Type()
)
swL3Ipv6AddressCtrlAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAddressType.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")
_SwL3IpFdbMgmt_ObjectIdentity = ObjectIdentity
swL3IpFdbMgmt = _SwL3IpFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2)
)
_SwL3IpFdbInfoTable_Object = MibTable
swL3IpFdbInfoTable = _SwL3IpFdbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoTable.setStatus("current")
_SwL3IpFdbInfoEntry_Object = MibTableRow
swL3IpFdbInfoEntry = _SwL3IpFdbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1, 1)
)
swL3IpFdbInfoEntry.setIndexNames(
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3IpFdbInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swL3IpFdbInfoEntry.setStatus("current")
_SwL3IpFdbInfoIpAddr_Type = IpAddress
_SwL3IpFdbInfoIpAddr_Object = MibTableColumn
swL3IpFdbInfoIpAddr = _SwL3IpFdbInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1, 1, 1),
    _SwL3IpFdbInfoIpAddr_Type()
)
swL3IpFdbInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpFdbInfoIpAddr.setStatus("current")
_SwL3IpFdbInfoIpSubnetMask_Type = IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object = MibTableColumn
swL3IpFdbInfoIpSubnetMask = _SwL3IpFdbInfoIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 4),
    _SwL3IpArpAgingTime_Type()
)
swL3IpArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpArpAgingTime.setStatus("current")
_SwL3IpStaticRouteTable_Object = MibTable
swL3IpStaticRouteTable = _SwL3IpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteTable.setStatus("current")
_SwL3IpStaticRouteEntry_Object = MibTableRow
swL3IpStaticRouteEntry = _SwL3IpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1)
)
swL3IpStaticRouteEntry.setIndexNames(
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3IpStaticRouteDest"),
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3IpStaticRouteMask"),
    (0, "DGS-3120-24PC-L3MGMT-MIB", "swL3IpStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swL3IpStaticRouteEntry.setStatus("current")
_SwL3IpStaticRouteDest_Type = IpAddress
_SwL3IpStaticRouteDest_Object = MibTableColumn
swL3IpStaticRouteDest = _SwL3IpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 1),
    _SwL3IpStaticRouteDest_Type()
)
swL3IpStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteDest.setStatus("current")
_SwL3IpStaticRouteMask_Type = IpAddress
_SwL3IpStaticRouteMask_Object = MibTableColumn
swL3IpStaticRouteMask = _SwL3IpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 3),
    _SwL3IpStaticRouteBkupState_Type()
)
swL3IpStaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteBkupState.setStatus("current")
_SwL3IpStaticRouteNextHop_Type = IpAddress
_SwL3IpStaticRouteNextHop_Object = MibTableColumn
swL3IpStaticRouteNextHop = _SwL3IpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 7),
    _SwL3IpStaticRouteWeight_Type()
)
swL3IpStaticRouteWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL3IpStaticRouteWeight.setStatus("current")
_SwL3IpStaticRouteInterfaceName_Type = DisplayString
_SwL3IpStaticRouteInterfaceName_Object = MibTableColumn
swL3IpStaticRouteInterfaceName = _SwL3IpStaticRouteInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 2, 3, 2, 5, 1, 8),
    _SwL3IpStaticRouteInterfaceName_Type()
)
swL3IpStaticRouteInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpStaticRouteInterfaceName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-3120-24PC-L3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
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
       "swL3IpCtrlDhcpv6ClientState": swL3IpCtrlDhcpv6ClientState,
       "swL3IpCtrlIpDhcpOption12State": swL3IpCtrlIpDhcpOption12State,
       "swL3IpCtrlIpDhcpOption12HostName": swL3IpCtrlIpDhcpOption12HostName,
       "swL3Ipv6CtrlTable": swL3Ipv6CtrlTable,
       "swL3Ipv6CtrlEntry": swL3Ipv6CtrlEntry,
       "swL3Ipv6CtrlInterfaceName": swL3Ipv6CtrlInterfaceName,
       "swL3Ipv6CtrlMaxReassmblySize": swL3Ipv6CtrlMaxReassmblySize,
       "swL3Ipv6CtrlNsRetransTimer": swL3Ipv6CtrlNsRetransTimer,
       "swL3Ipv6AddressCtrlTable": swL3Ipv6AddressCtrlTable,
       "swL3Ipv6AddressCtrlEntry": swL3Ipv6AddressCtrlEntry,
       "swL3Ipv6AddressCtrlInterfaceName": swL3Ipv6AddressCtrlInterfaceName,
       "swL3Ipv6Address": swL3Ipv6Address,
       "swL3Ipv6AddressCtrlPrefixLen": swL3Ipv6AddressCtrlPrefixLen,
       "swL3Ipv6AddressCtrlState": swL3Ipv6AddressCtrlState,
       "swL3Ipv6AddressCtrlAddressType": swL3Ipv6AddressCtrlAddressType,
       "swL3IpCtrlAllIpIfState": swL3IpCtrlAllIpIfState,
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
       "swL3IpStaticRouteInterfaceName": swL3IpStaticRouteInterfaceName}
)
