# SNMP MIB module (DGS3216-SWL3MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS3216-SWL3MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:35 2024
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

(dgs3216,) = mibBuilder.importSymbols(
    "SW3200PRIMGMT-MIB",
    "dgs3216")


# MODULE-IDENTITY

swL3MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3)
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



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class VrId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SwL3IpMgmt_ObjectIdentity = ObjectIdentity
swL3IpMgmt = _SwL3IpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2)
)
_SwL3IpCtrlMgmt_ObjectIdentity = ObjectIdentity
swL3IpCtrlMgmt = _SwL3IpCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1)
)
_SwL3IpCtrlTable_Object = MibTable
swL3IpCtrlTable = _SwL3IpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swL3IpCtrlTable.setStatus("current")
_SwL3IpCtrlEntry_Object = MibTableRow
swL3IpCtrlEntry = _SwL3IpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1)
)
swL3IpCtrlEntry.setIndexNames(
    (0, "DGS3216-SWL3MGMT-MIB", "swL3IpCtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 2),
    _SwL3IpCtrlIfIndex_Type()
)
swL3IpCtrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIfIndex.setStatus("current")
_SwL3IpCtrlIpAddr_Type = IpAddress
_SwL3IpCtrlIpAddr_Object = MibTableColumn
swL3IpCtrlIpAddr = _SwL3IpCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 3),
    _SwL3IpCtrlIpAddr_Type()
)
swL3IpCtrlIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpAddr.setStatus("current")
_SwL3IpCtrlIpSubnetMask_Type = IpAddress
_SwL3IpCtrlIpSubnetMask_Object = MibTableColumn
swL3IpCtrlIpSubnetMask = _SwL3IpCtrlIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 5),
    _SwL3IpCtrlVlanName_Type()
)
swL3IpCtrlVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlVlanName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 9),
    _SwL3IpCtrlAdminState_Type()
)
swL3IpCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAdminState.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalAddress_Type = Ipv6Address
_SwL3IpCtrlIpv6LinkLocalAddress_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalAddress = _SwL3IpCtrlIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 14),
    _SwL3IpCtrlIpv6LinkLocalAddress_Type()
)
swL3IpCtrlIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAddress.setStatus("current")
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Type = Integer32
_SwL3IpCtrlIpv6LinkLocalPrefixLen_Object = MibTableColumn
swL3IpCtrlIpv6LinkLocalPrefixLen = _SwL3IpCtrlIpv6LinkLocalPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 15),
    _SwL3IpCtrlIpv6LinkLocalPrefixLen_Type()
)
swL3IpCtrlIpv6LinkLocalPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus("current")
_SwL3IpCtrlState_Type = RowStatus
_SwL3IpCtrlState_Object = MibTableColumn
swL3IpCtrlState = _SwL3IpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 17),
    _SwL3IpCtrlIpv6LinkLocalAutoState_Type()
)
swL3IpCtrlIpv6LinkLocalAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpv6LinkLocalAutoState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 3, 1, 23),
    _SwL3IpCtrlIpDhcpOption12HostName_Type()
)
swL3IpCtrlIpDhcpOption12HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlIpDhcpOption12HostName.setStatus("current")
_SwL3Ipv6CtrlTable_Object = MibTable
swL3Ipv6CtrlTable = _SwL3Ipv6CtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    swL3Ipv6CtrlTable.setStatus("current")
_SwL3Ipv6CtrlEntry_Object = MibTableRow
swL3Ipv6CtrlEntry = _SwL3Ipv6CtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1)
)
swL3Ipv6CtrlEntry.setIndexNames(
    (0, "DGS3216-SWL3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 1),
    _SwL3Ipv6CtrlInterfaceName_Type()
)
swL3Ipv6CtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlInterfaceName.setStatus("current")
_SwL3Ipv6CtrlMaxReassmblySize_Type = Integer32
_SwL3Ipv6CtrlMaxReassmblySize_Object = MibTableColumn
swL3Ipv6CtrlMaxReassmblySize = _SwL3Ipv6CtrlMaxReassmblySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 4, 1, 13),
    _SwL3Ipv6CtrlRaOtherConfigFlag_Type()
)
swL3Ipv6CtrlRaOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6CtrlRaOtherConfigFlag.setStatus("current")
_SwL3Ipv6AddressCtrlTable_Object = MibTable
swL3Ipv6AddressCtrlTable = _SwL3Ipv6AddressCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlTable.setStatus("current")
_SwL3Ipv6AddressCtrlEntry_Object = MibTableRow
swL3Ipv6AddressCtrlEntry = _SwL3Ipv6AddressCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1)
)
swL3Ipv6AddressCtrlEntry.setIndexNames(
    (0, "DGS3216-SWL3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"),
    (0, "DGS3216-SWL3MGMT-MIB", "swL3Ipv6Address"),
    (0, "DGS3216-SWL3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 1),
    _SwL3Ipv6AddressCtrlInterfaceName_Type()
)
swL3Ipv6AddressCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlInterfaceName.setStatus("current")
_SwL3Ipv6Address_Type = Ipv6Address
_SwL3Ipv6Address_Object = MibTableColumn
swL3Ipv6Address = _SwL3Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 2),
    _SwL3Ipv6Address_Type()
)
swL3Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL3Ipv6Address.setStatus("current")
_SwL3Ipv6AddressCtrlPrefixLen_Type = Integer32
_SwL3Ipv6AddressCtrlPrefixLen_Object = MibTableColumn
swL3Ipv6AddressCtrlPrefixLen = _SwL3Ipv6AddressCtrlPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 7),
    _SwL3Ipv6AddressCtrlAutonomousFlag_Type()
)
swL3Ipv6AddressCtrlAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3Ipv6AddressCtrlAutonomousFlag.setStatus("current")
_SwL3Ipv6AddressCtrlState_Type = RowStatus
_SwL3Ipv6AddressCtrlState_Object = MibTableColumn
swL3Ipv6AddressCtrlState = _SwL3Ipv6AddressCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 5, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2, 3, 2, 1, 7),
    _SwL3IpCtrlAllIpIfState_Type()
)
swL3IpCtrlAllIpIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL3IpCtrlAllIpIfState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS3216-SWL3MGMT-MIB",
    **{"NodeAddress": NodeAddress,
       "NetAddress": NetAddress,
       "Ipv6Address": Ipv6Address,
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
       "swL3IpCtrlMode": swL3IpCtrlMode,
       "swL3IpCtrlAdminState": swL3IpCtrlAdminState,
       "swL3IpCtrlIpv6LinkLocalAddress": swL3IpCtrlIpv6LinkLocalAddress,
       "swL3IpCtrlIpv6LinkLocalPrefixLen": swL3IpCtrlIpv6LinkLocalPrefixLen,
       "swL3IpCtrlState": swL3IpCtrlState,
       "swL3IpCtrlIpv6LinkLocalAutoState": swL3IpCtrlIpv6LinkLocalAutoState,
       "swL3IpCtrlDhcpv6ClientState": swL3IpCtrlDhcpv6ClientState,
       "swL3IpCtrlIpDhcpOption12State": swL3IpCtrlIpDhcpOption12State,
       "swL3IpCtrlIpDhcpOption12HostName": swL3IpCtrlIpDhcpOption12HostName,
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
       "swL3Ipv6AddressCtrlAddressType": swL3Ipv6AddressCtrlAddressType,
       "swL3IpCtrlAllIpIfState": swL3IpCtrlAllIpIfState}
)
