# SNMP MIB module (DNOS-ROUTING6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-ROUTING6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:15 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix,
 Ipv6IfIndex,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix",
    "Ipv6IfIndex",
    "Ipv6IfIndexOrZero")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

fastPathRoutingIpv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30)
)
fastPathRoutingIpv6.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00",
         "2005-09-21 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentIpv6Group_ObjectIdentity = ObjectIdentity
agentIpv6Group = _AgentIpv6Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1)
)


class _AgentIpv6RoutingMode_Type(Integer32):
    """Custom type agentIpv6RoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6RoutingMode_Type.__name__ = "Integer32"
_AgentIpv6RoutingMode_Object = MibScalar
agentIpv6RoutingMode = _AgentIpv6RoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 1),
    _AgentIpv6RoutingMode_Type()
)
agentIpv6RoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RoutingMode.setStatus("current")
_AgentIpv6InterfaceTable_Object = MibTable
agentIpv6InterfaceTable = _AgentIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2)
)
if mibBuilder.loadTexts:
    agentIpv6InterfaceTable.setStatus("current")
_AgentIpv6InterfaceEntry_Object = MibTableRow
agentIpv6InterfaceEntry = _AgentIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1)
)
agentIpv6InterfaceEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentIpv6InterfaceEntry.setStatus("current")


class _AgentIpv6InterfaceIfIndex_Type(Integer32):
    """Custom type agentIpv6InterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentIpv6InterfaceIfIndex_Type.__name__ = "Integer32"
_AgentIpv6InterfaceIfIndex_Object = MibTableColumn
agentIpv6InterfaceIfIndex = _AgentIpv6InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 1),
    _AgentIpv6InterfaceIfIndex_Type()
)
agentIpv6InterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6InterfaceIfIndex.setStatus("current")


class _AgentIpv6InterfaceMtuValue_Type(Unsigned32):
    """Custom type agentIpv6InterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1280, 1500),
    )


_AgentIpv6InterfaceMtuValue_Type.__name__ = "Unsigned32"
_AgentIpv6InterfaceMtuValue_Object = MibTableColumn
agentIpv6InterfaceMtuValue = _AgentIpv6InterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 2),
    _AgentIpv6InterfaceMtuValue_Type()
)
agentIpv6InterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceMtuValue.setStatus("current")


class _AgentIpv6InterfaceDadTransmits_Type(Integer32):
    """Custom type agentIpv6InterfaceDadTransmits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentIpv6InterfaceDadTransmits_Type.__name__ = "Integer32"
_AgentIpv6InterfaceDadTransmits_Object = MibTableColumn
agentIpv6InterfaceDadTransmits = _AgentIpv6InterfaceDadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 3),
    _AgentIpv6InterfaceDadTransmits_Type()
)
agentIpv6InterfaceDadTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceDadTransmits.setStatus("current")


class _AgentIpv6InterfaceLinkLocalOnly_Type(Integer32):
    """Custom type agentIpv6InterfaceLinkLocalOnly based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6InterfaceLinkLocalOnly_Type.__name__ = "Integer32"
_AgentIpv6InterfaceLinkLocalOnly_Object = MibTableColumn
agentIpv6InterfaceLinkLocalOnly = _AgentIpv6InterfaceLinkLocalOnly_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 4),
    _AgentIpv6InterfaceLinkLocalOnly_Type()
)
agentIpv6InterfaceLinkLocalOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceLinkLocalOnly.setStatus("current")


class _AgentIpv6InterfaceIcmpUnreachables_Type(Integer32):
    """Custom type agentIpv6InterfaceIcmpUnreachables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6InterfaceIcmpUnreachables_Type.__name__ = "Integer32"
_AgentIpv6InterfaceIcmpUnreachables_Object = MibTableColumn
agentIpv6InterfaceIcmpUnreachables = _AgentIpv6InterfaceIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 5),
    _AgentIpv6InterfaceIcmpUnreachables_Type()
)
agentIpv6InterfaceIcmpUnreachables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceIcmpUnreachables.setStatus("current")


class _AgentIpv6InterfaceAutoconfig_Type(Integer32):
    """Custom type agentIpv6InterfaceAutoconfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6InterfaceAutoconfig_Type.__name__ = "Integer32"
_AgentIpv6InterfaceAutoconfig_Object = MibTableColumn
agentIpv6InterfaceAutoconfig = _AgentIpv6InterfaceAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 6),
    _AgentIpv6InterfaceAutoconfig_Type()
)
agentIpv6InterfaceAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceAutoconfig.setStatus("current")


class _AgentIpv6InterfaceDhcpClient_Type(Integer32):
    """Custom type agentIpv6InterfaceDhcpClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6InterfaceDhcpClient_Type.__name__ = "Integer32"
_AgentIpv6InterfaceDhcpClient_Object = MibTableColumn
agentIpv6InterfaceDhcpClient = _AgentIpv6InterfaceDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 7),
    _AgentIpv6InterfaceDhcpClient_Type()
)
agentIpv6InterfaceDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceDhcpClient.setStatus("current")


class _AgentIpv6InterfaceIcmpRedirects_Type(Integer32):
    """Custom type agentIpv6InterfaceIcmpRedirects based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6InterfaceIcmpRedirects_Type.__name__ = "Integer32"
_AgentIpv6InterfaceIcmpRedirects_Object = MibTableColumn
agentIpv6InterfaceIcmpRedirects = _AgentIpv6InterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 2, 1, 8),
    _AgentIpv6InterfaceIcmpRedirects_Type()
)
agentIpv6InterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6InterfaceIcmpRedirects.setStatus("current")
_AgentIpv6RouterAdvertisementTable_Object = MibTable
agentIpv6RouterAdvertisementTable = _AgentIpv6RouterAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3)
)
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementTable.setStatus("current")
_AgentIpv6RouterAdvertisementEntry_Object = MibTableRow
agentIpv6RouterAdvertisementEntry = _AgentIpv6RouterAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1)
)
agentIpv6RouterAdvertisementEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6RouterAdvertisementIfIndex"),
)
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementEntry.setStatus("current")


class _AgentIpv6RouterAdvertisementIfIndex_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentIpv6RouterAdvertisementIfIndex_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementIfIndex_Object = MibTableColumn
agentIpv6RouterAdvertisementIfIndex = _AgentIpv6RouterAdvertisementIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 1),
    _AgentIpv6RouterAdvertisementIfIndex_Type()
)
agentIpv6RouterAdvertisementIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementIfIndex.setStatus("current")


class _AgentIpv6RouterAdvertisementSuppressMode_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementSuppressMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6RouterAdvertisementSuppressMode_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementSuppressMode_Object = MibTableColumn
agentIpv6RouterAdvertisementSuppressMode = _AgentIpv6RouterAdvertisementSuppressMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 2),
    _AgentIpv6RouterAdvertisementSuppressMode_Type()
)
agentIpv6RouterAdvertisementSuppressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementSuppressMode.setStatus("current")


class _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object = MibTableColumn
agentIpv6RouterAdvertisementMaxAdvertisementInterval = _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 3),
    _AgentIpv6RouterAdvertisementMaxAdvertisementInterval_Type()
)
agentIpv6RouterAdvertisementMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementMaxAdvertisementInterval.setStatus("current")


class _AgentIpv6RouterAdvertisementAdvertisementLifetime_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 65520),
    )


_AgentIpv6RouterAdvertisementAdvertisementLifetime_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementAdvertisementLifetime_Object = MibTableColumn
agentIpv6RouterAdvertisementAdvertisementLifetime = _AgentIpv6RouterAdvertisementAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 4),
    _AgentIpv6RouterAdvertisementAdvertisementLifetime_Type()
)
agentIpv6RouterAdvertisementAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementAdvertisementLifetime.setStatus("current")


class _AgentIpv6RouterAdvertisementNbrSolicitInterval_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementNbrSolicitInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_AgentIpv6RouterAdvertisementNbrSolicitInterval_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementNbrSolicitInterval_Object = MibTableColumn
agentIpv6RouterAdvertisementNbrSolicitInterval = _AgentIpv6RouterAdvertisementNbrSolicitInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 5),
    _AgentIpv6RouterAdvertisementNbrSolicitInterval_Type()
)
agentIpv6RouterAdvertisementNbrSolicitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementNbrSolicitInterval.setStatus("current")


class _AgentIpv6RouterAdvertisementReachableTime_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementReachableTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_AgentIpv6RouterAdvertisementReachableTime_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementReachableTime_Object = MibTableColumn
agentIpv6RouterAdvertisementReachableTime = _AgentIpv6RouterAdvertisementReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 6),
    _AgentIpv6RouterAdvertisementReachableTime_Type()
)
agentIpv6RouterAdvertisementReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementReachableTime.setStatus("current")


class _AgentIpv6RouterAdvertisementManagedFlag_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementManagedFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6RouterAdvertisementManagedFlag_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementManagedFlag_Object = MibTableColumn
agentIpv6RouterAdvertisementManagedFlag = _AgentIpv6RouterAdvertisementManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 7),
    _AgentIpv6RouterAdvertisementManagedFlag_Type()
)
agentIpv6RouterAdvertisementManagedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementManagedFlag.setStatus("current")


class _AgentIpv6RouterAdvertisementOtherFlag_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementOtherFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6RouterAdvertisementOtherFlag_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementOtherFlag_Object = MibTableColumn
agentIpv6RouterAdvertisementOtherFlag = _AgentIpv6RouterAdvertisementOtherFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 8),
    _AgentIpv6RouterAdvertisementOtherFlag_Type()
)
agentIpv6RouterAdvertisementOtherFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementOtherFlag.setStatus("current")


class _AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type(Integer32):
    """Custom type agentIpv6RouterAdvertisementHopLimitUnspecifiedMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type.__name__ = "Integer32"
_AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Object = MibTableColumn
agentIpv6RouterAdvertisementHopLimitUnspecifiedMode = _AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 3, 1, 9),
    _AgentIpv6RouterAdvertisementHopLimitUnspecifiedMode_Type()
)
agentIpv6RouterAdvertisementHopLimitUnspecifiedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6RouterAdvertisementHopLimitUnspecifiedMode.setStatus("current")
_AgentIpv6AddrPrefixTable_Object = MibTable
agentIpv6AddrPrefixTable = _AgentIpv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4)
)
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixTable.setStatus("current")
_AgentIpv6AddrPrefixEntry_Object = MibTableRow
agentIpv6AddrPrefixEntry = _AgentIpv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1)
)
agentIpv6AddrPrefixEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6AddrPrefix"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6AddrPrefixLength"),
)
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixEntry.setStatus("current")
_AgentIpv6AddrPrefix_Type = Ipv6AddressPrefix
_AgentIpv6AddrPrefix_Object = MibTableColumn
agentIpv6AddrPrefix = _AgentIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 1),
    _AgentIpv6AddrPrefix_Type()
)
agentIpv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefix.setStatus("current")


class _AgentIpv6AddrPrefixLength_Type(Integer32):
    """Custom type agentIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_AgentIpv6AddrPrefixLength_Object = MibTableColumn
agentIpv6AddrPrefixLength = _AgentIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 2),
    _AgentIpv6AddrPrefixLength_Type()
)
agentIpv6AddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixLength.setUnits("bits")
_AgentIpv6AddrPrefixOnLinkFlag_Type = TruthValue
_AgentIpv6AddrPrefixOnLinkFlag_Object = MibTableColumn
agentIpv6AddrPrefixOnLinkFlag = _AgentIpv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 3),
    _AgentIpv6AddrPrefixOnLinkFlag_Type()
)
agentIpv6AddrPrefixOnLinkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixOnLinkFlag.setStatus("current")
_AgentIpv6AddrPrefixAutonomousFlag_Type = TruthValue
_AgentIpv6AddrPrefixAutonomousFlag_Object = MibTableColumn
agentIpv6AddrPrefixAutonomousFlag = _AgentIpv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 4),
    _AgentIpv6AddrPrefixAutonomousFlag_Type()
)
agentIpv6AddrPrefixAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixAutonomousFlag.setStatus("current")
_AgentIpv6AddrPrefixAdvPreferredLifetime_Type = Unsigned32
_AgentIpv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
agentIpv6AddrPrefixAdvPreferredLifetime = _AgentIpv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 5),
    _AgentIpv6AddrPrefixAdvPreferredLifetime_Type()
)
agentIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixAdvPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixAdvPreferredLifetime.setUnits("seconds")
_AgentIpv6AddrPrefixAdvValidLifetime_Type = Unsigned32
_AgentIpv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
agentIpv6AddrPrefixAdvValidLifetime = _AgentIpv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 4, 1, 6),
    _AgentIpv6AddrPrefixAdvValidLifetime_Type()
)
agentIpv6AddrPrefixAdvValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    agentIpv6AddrPrefixAdvValidLifetime.setUnits("seconds")
_AgentIpv6AddrTable_Object = MibTable
agentIpv6AddrTable = _AgentIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5)
)
if mibBuilder.loadTexts:
    agentIpv6AddrTable.setStatus("current")
_AgentIpv6AddrEntry_Object = MibTableRow
agentIpv6AddrEntry = _AgentIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5, 1)
)
agentIpv6AddrEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6AddrAddress"),
)
if mibBuilder.loadTexts:
    agentIpv6AddrEntry.setStatus("current")
_AgentIpv6AddrAddress_Type = Ipv6Address
_AgentIpv6AddrAddress_Object = MibTableColumn
agentIpv6AddrAddress = _AgentIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5, 1, 1),
    _AgentIpv6AddrAddress_Type()
)
agentIpv6AddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6AddrAddress.setStatus("current")


class _AgentIpv6AddrPfxLength_Type(Integer32):
    """Custom type agentIpv6AddrPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentIpv6AddrPfxLength_Type.__name__ = "Integer32"
_AgentIpv6AddrPfxLength_Object = MibTableColumn
agentIpv6AddrPfxLength = _AgentIpv6AddrPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5, 1, 2),
    _AgentIpv6AddrPfxLength_Type()
)
agentIpv6AddrPfxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6AddrPfxLength.setStatus("current")
if mibBuilder.loadTexts:
    agentIpv6AddrPfxLength.setUnits("bits")
_AgentIpv6AddrEui64Flag_Type = TruthValue
_AgentIpv6AddrEui64Flag_Object = MibTableColumn
agentIpv6AddrEui64Flag = _AgentIpv6AddrEui64Flag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5, 1, 3),
    _AgentIpv6AddrEui64Flag_Type()
)
agentIpv6AddrEui64Flag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6AddrEui64Flag.setStatus("current")
_AgentIpv6AddrStatus_Type = RowStatus
_AgentIpv6AddrStatus_Object = MibTableColumn
agentIpv6AddrStatus = _AgentIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 5, 1, 4),
    _AgentIpv6AddrStatus_Type()
)
agentIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6AddrStatus.setStatus("current")
_AgentIpv6StaticRouteTable_Object = MibTable
agentIpv6StaticRouteTable = _AgentIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6)
)
if mibBuilder.loadTexts:
    agentIpv6StaticRouteTable.setStatus("current")
_AgentIpv6StaticRouteEntry_Object = MibTableRow
agentIpv6StaticRouteEntry = _AgentIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1)
)
agentIpv6StaticRouteEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6StaticRouteDest"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6StaticRoutePfxLength"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6StaticRouteIfIndex"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6StaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    agentIpv6StaticRouteEntry.setStatus("current")
_AgentIpv6StaticRouteDest_Type = Ipv6AddressPrefix
_AgentIpv6StaticRouteDest_Object = MibTableColumn
agentIpv6StaticRouteDest = _AgentIpv6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 1),
    _AgentIpv6StaticRouteDest_Type()
)
agentIpv6StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6StaticRouteDest.setStatus("current")


class _AgentIpv6StaticRoutePfxLength_Type(Integer32):
    """Custom type agentIpv6StaticRoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentIpv6StaticRoutePfxLength_Type.__name__ = "Integer32"
_AgentIpv6StaticRoutePfxLength_Object = MibTableColumn
agentIpv6StaticRoutePfxLength = _AgentIpv6StaticRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 2),
    _AgentIpv6StaticRoutePfxLength_Type()
)
agentIpv6StaticRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6StaticRoutePfxLength.setStatus("current")
if mibBuilder.loadTexts:
    agentIpv6StaticRoutePfxLength.setUnits("bits")
_AgentIpv6StaticRouteIfIndex_Type = Ipv6IfIndexOrZero
_AgentIpv6StaticRouteIfIndex_Object = MibTableColumn
agentIpv6StaticRouteIfIndex = _AgentIpv6StaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 3),
    _AgentIpv6StaticRouteIfIndex_Type()
)
agentIpv6StaticRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6StaticRouteIfIndex.setStatus("current")
_AgentIpv6StaticRouteNextHop_Type = Ipv6Address
_AgentIpv6StaticRouteNextHop_Object = MibTableColumn
agentIpv6StaticRouteNextHop = _AgentIpv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 4),
    _AgentIpv6StaticRouteNextHop_Type()
)
agentIpv6StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6StaticRouteNextHop.setStatus("current")


class _AgentIpv6StaticRoutePreference_Type(Integer32):
    """Custom type agentIpv6StaticRoutePreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentIpv6StaticRoutePreference_Type.__name__ = "Integer32"
_AgentIpv6StaticRoutePreference_Object = MibTableColumn
agentIpv6StaticRoutePreference = _AgentIpv6StaticRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 5),
    _AgentIpv6StaticRoutePreference_Type()
)
agentIpv6StaticRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6StaticRoutePreference.setStatus("current")
_AgentIpv6StaticRouteStatus_Type = RowStatus
_AgentIpv6StaticRouteStatus_Object = MibTableColumn
agentIpv6StaticRouteStatus = _AgentIpv6StaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 6, 1, 6),
    _AgentIpv6StaticRouteStatus_Type()
)
agentIpv6StaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6StaticRouteStatus.setStatus("current")
_AgentIpv6ServicePortGroup_ObjectIdentity = ObjectIdentity
agentIpv6ServicePortGroup = _AgentIpv6ServicePortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7)
)
_AgentIpv6ServicePortPrefixTable_Object = MibTable
agentIpv6ServicePortPrefixTable = _AgentIpv6ServicePortPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 1)
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortPrefixTable.setStatus("current")
_AgentIpv6ServicePortPrefixEntry_Object = MibTableRow
agentIpv6ServicePortPrefixEntry = _AgentIpv6ServicePortPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 1, 1)
)
agentIpv6ServicePortPrefixEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6ServicePortPrefixIndex"),
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortPrefixEntry.setStatus("current")
_AgentIpv6ServicePortPrefixIndex_Type = Unsigned32
_AgentIpv6ServicePortPrefixIndex_Object = MibTableColumn
agentIpv6ServicePortPrefixIndex = _AgentIpv6ServicePortPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 1, 1, 1),
    _AgentIpv6ServicePortPrefixIndex_Type()
)
agentIpv6ServicePortPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6ServicePortPrefixIndex.setStatus("current")
_AgentIpv6ServicePortPrefix_Type = Ipv6Address
_AgentIpv6ServicePortPrefix_Object = MibTableColumn
agentIpv6ServicePortPrefix = _AgentIpv6ServicePortPrefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 1, 1, 2),
    _AgentIpv6ServicePortPrefix_Type()
)
agentIpv6ServicePortPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortPrefix.setStatus("current")
_AgentIpv6ServicePortPrefixLength_Type = Unsigned32
_AgentIpv6ServicePortPrefixLength_Object = MibTableColumn
agentIpv6ServicePortPrefixLength = _AgentIpv6ServicePortPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 1, 1, 3),
    _AgentIpv6ServicePortPrefixLength_Type()
)
agentIpv6ServicePortPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortPrefixLength.setStatus("current")
_AgentIpv6ServicePortDefaultRouterTable_Object = MibTable
agentIpv6ServicePortDefaultRouterTable = _AgentIpv6ServicePortDefaultRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 2)
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortDefaultRouterTable.setStatus("current")
_AgentIpv6ServicePortDefaultRouterEntry_Object = MibTableRow
agentIpv6ServicePortDefaultRouterEntry = _AgentIpv6ServicePortDefaultRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 2, 1)
)
agentIpv6ServicePortDefaultRouterEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6ServicePortDefaultRouterIndex"),
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortDefaultRouterEntry.setStatus("current")
_AgentIpv6ServicePortDefaultRouterIndex_Type = Unsigned32
_AgentIpv6ServicePortDefaultRouterIndex_Object = MibTableColumn
agentIpv6ServicePortDefaultRouterIndex = _AgentIpv6ServicePortDefaultRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 2, 1, 1),
    _AgentIpv6ServicePortDefaultRouterIndex_Type()
)
agentIpv6ServicePortDefaultRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6ServicePortDefaultRouterIndex.setStatus("current")
_AgentIpv6ServicePortDefaultRouter_Type = Ipv6Address
_AgentIpv6ServicePortDefaultRouter_Object = MibTableColumn
agentIpv6ServicePortDefaultRouter = _AgentIpv6ServicePortDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 2, 1, 2),
    _AgentIpv6ServicePortDefaultRouter_Type()
)
agentIpv6ServicePortDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortDefaultRouter.setStatus("current")
_AgentIpv6ServicePortNbrTable_Object = MibTable
agentIpv6ServicePortNbrTable = _AgentIpv6ServicePortNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3)
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrTable.setStatus("current")
_AgentIpv6ServicePortNbrEntry_Object = MibTableRow
agentIpv6ServicePortNbrEntry = _AgentIpv6ServicePortNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1)
)
agentIpv6ServicePortNbrEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6ServicePortNbrAddr"),
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrEntry.setStatus("current")
_AgentIpv6ServicePortNbrAddr_Type = Ipv6Address
_AgentIpv6ServicePortNbrAddr_Object = MibTableColumn
agentIpv6ServicePortNbrAddr = _AgentIpv6ServicePortNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 1),
    _AgentIpv6ServicePortNbrAddr_Type()
)
agentIpv6ServicePortNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrAddr.setStatus("current")
_AgentIpv6ServicePortNbrPhysAddr_Type = MacAddress
_AgentIpv6ServicePortNbrPhysAddr_Object = MibTableColumn
agentIpv6ServicePortNbrPhysAddr = _AgentIpv6ServicePortNbrPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 2),
    _AgentIpv6ServicePortNbrPhysAddr_Type()
)
agentIpv6ServicePortNbrPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrPhysAddr.setStatus("current")


class _AgentIpv6ServicePortNbrState_Type(Integer32):
    """Custom type agentIpv6ServicePortNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_AgentIpv6ServicePortNbrState_Type.__name__ = "Integer32"
_AgentIpv6ServicePortNbrState_Object = MibTableColumn
agentIpv6ServicePortNbrState = _AgentIpv6ServicePortNbrState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 3),
    _AgentIpv6ServicePortNbrState_Type()
)
agentIpv6ServicePortNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrState.setStatus("current")
_AgentIpv6ServicePortNbrUpdated_Type = TimeStamp
_AgentIpv6ServicePortNbrUpdated_Object = MibTableColumn
agentIpv6ServicePortNbrUpdated = _AgentIpv6ServicePortNbrUpdated_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 4),
    _AgentIpv6ServicePortNbrUpdated_Type()
)
agentIpv6ServicePortNbrUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrUpdated.setStatus("current")
_AgentIpv6ServicePortNbrIsRouter_Type = TruthValue
_AgentIpv6ServicePortNbrIsRouter_Object = MibTableColumn
agentIpv6ServicePortNbrIsRouter = _AgentIpv6ServicePortNbrIsRouter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 5),
    _AgentIpv6ServicePortNbrIsRouter_Type()
)
agentIpv6ServicePortNbrIsRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrIsRouter.setStatus("current")


class _AgentIpv6ServicePortNbrType_Type(Integer32):
    """Custom type agentIpv6ServicePortNbrType based on Integer32"""
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
        *(("dynamic", 2),
          ("local", 4),
          ("other", 1),
          ("static", 3))
    )


_AgentIpv6ServicePortNbrType_Type.__name__ = "Integer32"
_AgentIpv6ServicePortNbrType_Object = MibTableColumn
agentIpv6ServicePortNbrType = _AgentIpv6ServicePortNbrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 3, 1, 6),
    _AgentIpv6ServicePortNbrType_Type()
)
agentIpv6ServicePortNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrType.setStatus("current")
_AgentIpv6ServicePortNbrCfgTable_Object = MibTable
agentIpv6ServicePortNbrCfgTable = _AgentIpv6ServicePortNbrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 4)
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrCfgTable.setStatus("current")
_AgentIpv6ServicePortNbrCfgEntry_Object = MibTableRow
agentIpv6ServicePortNbrCfgEntry = _AgentIpv6ServicePortNbrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 4, 1)
)
agentIpv6ServicePortNbrCfgEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6ServicePortNbrCfgAddr"),
)
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrCfgEntry.setStatus("current")
_AgentIpv6ServicePortNbrCfgAddr_Type = Ipv6Address
_AgentIpv6ServicePortNbrCfgAddr_Object = MibTableColumn
agentIpv6ServicePortNbrCfgAddr = _AgentIpv6ServicePortNbrCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 4, 1, 1),
    _AgentIpv6ServicePortNbrCfgAddr_Type()
)
agentIpv6ServicePortNbrCfgAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrCfgAddr.setStatus("current")
_AgentIpv6ServicePortNbrCfgPhysAddr_Type = MacAddress
_AgentIpv6ServicePortNbrCfgPhysAddr_Object = MibTableColumn
agentIpv6ServicePortNbrCfgPhysAddr = _AgentIpv6ServicePortNbrCfgPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 4, 1, 2),
    _AgentIpv6ServicePortNbrCfgPhysAddr_Type()
)
agentIpv6ServicePortNbrCfgPhysAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrCfgPhysAddr.setStatus("current")
_AgentIpv6ServicePortNbrCfgEntryStatus_Type = RowStatus
_AgentIpv6ServicePortNbrCfgEntryStatus_Object = MibTableColumn
agentIpv6ServicePortNbrCfgEntryStatus = _AgentIpv6ServicePortNbrCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 7, 4, 1, 3),
    _AgentIpv6ServicePortNbrCfgEntryStatus_Type()
)
agentIpv6ServicePortNbrCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6ServicePortNbrCfgEntryStatus.setStatus("current")
_AgentIpv6IcmpControlGroup_ObjectIdentity = ObjectIdentity
agentIpv6IcmpControlGroup = _AgentIpv6IcmpControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 8)
)


class _AgentIpv6IcmpRateLimitInterval_Type(Integer32):
    """Custom type agentIpv6IcmpRateLimitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentIpv6IcmpRateLimitInterval_Type.__name__ = "Integer32"
_AgentIpv6IcmpRateLimitInterval_Object = MibScalar
agentIpv6IcmpRateLimitInterval = _AgentIpv6IcmpRateLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 8, 1),
    _AgentIpv6IcmpRateLimitInterval_Type()
)
agentIpv6IcmpRateLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6IcmpRateLimitInterval.setStatus("current")


class _AgentIpv6IcmpRateLimitBurstSize_Type(Integer32):
    """Custom type agentIpv6IcmpRateLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AgentIpv6IcmpRateLimitBurstSize_Type.__name__ = "Integer32"
_AgentIpv6IcmpRateLimitBurstSize_Object = MibScalar
agentIpv6IcmpRateLimitBurstSize = _AgentIpv6IcmpRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 8, 2),
    _AgentIpv6IcmpRateLimitBurstSize_Type()
)
agentIpv6IcmpRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6IcmpRateLimitBurstSize.setStatus("current")
_AgentDhcp6ClientParametersTable_Object = MibTable
agentDhcp6ClientParametersTable = _AgentDhcp6ClientParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9)
)
if mibBuilder.loadTexts:
    agentDhcp6ClientParametersTable.setStatus("current")
_AgentDhcp6ClientParametersEntry_Object = MibTableRow
agentDhcp6ClientParametersEntry = _AgentDhcp6ClientParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1)
)
agentDhcp6ClientParametersEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentDhcp6ClientInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentDhcp6ClientParametersEntry.setStatus("current")
_AgentDhcp6ClientInterfaceIndex_Type = Unsigned32
_AgentDhcp6ClientInterfaceIndex_Object = MibTableColumn
agentDhcp6ClientInterfaceIndex = _AgentDhcp6ClientInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 1),
    _AgentDhcp6ClientInterfaceIndex_Type()
)
agentDhcp6ClientInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientInterfaceIndex.setStatus("current")
_AgentDhcp6ClientPrefix_Type = Ipv6AddressPrefix
_AgentDhcp6ClientPrefix_Object = MibTableColumn
agentDhcp6ClientPrefix = _AgentDhcp6ClientPrefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 2),
    _AgentDhcp6ClientPrefix_Type()
)
agentDhcp6ClientPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientPrefix.setStatus("current")
_AgentDhcp6ClientPrefixlength_Type = Integer32
_AgentDhcp6ClientPrefixlength_Object = MibTableColumn
agentDhcp6ClientPrefixlength = _AgentDhcp6ClientPrefixlength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 3),
    _AgentDhcp6ClientPrefixlength_Type()
)
agentDhcp6ClientPrefixlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientPrefixlength.setStatus("current")


class _AgentDhcp6ClientState_Type(Integer32):
    """Custom type agentDhcp6ClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 0),
          ("rebind", 5),
          ("release", 6),
          ("renew", 4),
          ("request", 2),
          ("solicit", 1))
    )


_AgentDhcp6ClientState_Type.__name__ = "Integer32"
_AgentDhcp6ClientState_Object = MibTableColumn
agentDhcp6ClientState = _AgentDhcp6ClientState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 4),
    _AgentDhcp6ClientState_Type()
)
agentDhcp6ClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientState.setStatus("current")


class _AgentDhcp6ClientServerDUID_Type(DisplayString):
    """Custom type agentDhcp6ClientServerDUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AgentDhcp6ClientServerDUID_Type.__name__ = "DisplayString"
_AgentDhcp6ClientServerDUID_Object = MibTableColumn
agentDhcp6ClientServerDUID = _AgentDhcp6ClientServerDUID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 5),
    _AgentDhcp6ClientServerDUID_Type()
)
agentDhcp6ClientServerDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientServerDUID.setStatus("current")
_AgentDhcp6ClientT1Time_Type = Unsigned32
_AgentDhcp6ClientT1Time_Object = MibTableColumn
agentDhcp6ClientT1Time = _AgentDhcp6ClientT1Time_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 6),
    _AgentDhcp6ClientT1Time_Type()
)
agentDhcp6ClientT1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientT1Time.setStatus("current")
_AgentDhcp6ClientT2Time_Type = Unsigned32
_AgentDhcp6ClientT2Time_Object = MibTableColumn
agentDhcp6ClientT2Time = _AgentDhcp6ClientT2Time_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 7),
    _AgentDhcp6ClientT2Time_Type()
)
agentDhcp6ClientT2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientT2Time.setStatus("current")
_AgentDhcp6ClientIAID_Type = Unsigned32
_AgentDhcp6ClientIAID_Object = MibTableColumn
agentDhcp6ClientIAID = _AgentDhcp6ClientIAID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 8),
    _AgentDhcp6ClientIAID_Type()
)
agentDhcp6ClientIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientIAID.setStatus("current")
_AgentDhcp6ClientPreferredLifeTime_Type = Unsigned32
_AgentDhcp6ClientPreferredLifeTime_Object = MibTableColumn
agentDhcp6ClientPreferredLifeTime = _AgentDhcp6ClientPreferredLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 9),
    _AgentDhcp6ClientPreferredLifeTime_Type()
)
agentDhcp6ClientPreferredLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientPreferredLifeTime.setStatus("current")
_AgentDhcp6ClientValidLifeTime_Type = Unsigned32
_AgentDhcp6ClientValidLifeTime_Object = MibTableColumn
agentDhcp6ClientValidLifeTime = _AgentDhcp6ClientValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 10),
    _AgentDhcp6ClientValidLifeTime_Type()
)
agentDhcp6ClientValidLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientValidLifeTime.setStatus("current")
_AgentDhcp6ClientRenewTime_Type = Unsigned32
_AgentDhcp6ClientRenewTime_Object = MibTableColumn
agentDhcp6ClientRenewTime = _AgentDhcp6ClientRenewTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 11),
    _AgentDhcp6ClientRenewTime_Type()
)
agentDhcp6ClientRenewTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientRenewTime.setStatus("current")
_AgentDhcp6ClientExpireTime_Type = Unsigned32
_AgentDhcp6ClientExpireTime_Object = MibTableColumn
agentDhcp6ClientExpireTime = _AgentDhcp6ClientExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 9, 1, 12),
    _AgentDhcp6ClientExpireTime_Type()
)
agentDhcp6ClientExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcp6ClientExpireTime.setStatus("current")
_AgentIpv6RoutingTableSummaryGroup_ObjectIdentity = ObjectIdentity
agentIpv6RoutingTableSummaryGroup = _AgentIpv6RoutingTableSummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10)
)
_AgentIpv6ConnectedRoutes_Type = Gauge32
_AgentIpv6ConnectedRoutes_Object = MibScalar
agentIpv6ConnectedRoutes = _AgentIpv6ConnectedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 1),
    _AgentIpv6ConnectedRoutes_Type()
)
agentIpv6ConnectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ConnectedRoutes.setStatus("current")
_AgentIpv6StaticRoutes_Type = Gauge32
_AgentIpv6StaticRoutes_Object = MibScalar
agentIpv6StaticRoutes = _AgentIpv6StaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 2),
    _AgentIpv6StaticRoutes_Type()
)
agentIpv6StaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6StaticRoutes.setStatus("current")
_AgentIpv66to4Routes_Type = Gauge32
_AgentIpv66to4Routes_Object = MibScalar
agentIpv66to4Routes = _AgentIpv66to4Routes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 3),
    _AgentIpv66to4Routes_Type()
)
agentIpv66to4Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv66to4Routes.setStatus("current")
_AgentIpv6OspfRoutes_Type = Gauge32
_AgentIpv6OspfRoutes_Object = MibScalar
agentIpv6OspfRoutes = _AgentIpv6OspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 4),
    _AgentIpv6OspfRoutes_Type()
)
agentIpv6OspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6OspfRoutes.setStatus("current")
_AgentIpv6OspfIntraRoutes_Type = Gauge32
_AgentIpv6OspfIntraRoutes_Object = MibScalar
agentIpv6OspfIntraRoutes = _AgentIpv6OspfIntraRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 5),
    _AgentIpv6OspfIntraRoutes_Type()
)
agentIpv6OspfIntraRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6OspfIntraRoutes.setStatus("current")
_AgentIpv6OspfInterRoutes_Type = Gauge32
_AgentIpv6OspfInterRoutes_Object = MibScalar
agentIpv6OspfInterRoutes = _AgentIpv6OspfInterRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 6),
    _AgentIpv6OspfInterRoutes_Type()
)
agentIpv6OspfInterRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6OspfInterRoutes.setStatus("current")
_AgentIpv6OspfExt1Routes_Type = Gauge32
_AgentIpv6OspfExt1Routes_Object = MibScalar
agentIpv6OspfExt1Routes = _AgentIpv6OspfExt1Routes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 7),
    _AgentIpv6OspfExt1Routes_Type()
)
agentIpv6OspfExt1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6OspfExt1Routes.setStatus("current")
_AgentIpv6OspfExt2Routes_Type = Gauge32
_AgentIpv6OspfExt2Routes_Object = MibScalar
agentIpv6OspfExt2Routes = _AgentIpv6OspfExt2Routes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 8),
    _AgentIpv6OspfExt2Routes_Type()
)
agentIpv6OspfExt2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6OspfExt2Routes.setStatus("current")
_AgentIpv6BgpRoutes_Type = Gauge32
_AgentIpv6BgpRoutes_Object = MibScalar
agentIpv6BgpRoutes = _AgentIpv6BgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 9),
    _AgentIpv6BgpRoutes_Type()
)
agentIpv6BgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6BgpRoutes.setStatus("current")
_AgentIpv6EbgpRoutes_Type = Gauge32
_AgentIpv6EbgpRoutes_Object = MibScalar
agentIpv6EbgpRoutes = _AgentIpv6EbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 10),
    _AgentIpv6EbgpRoutes_Type()
)
agentIpv6EbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EbgpRoutes.setStatus("current")
_AgentIpv6IbgpRoutes_Type = Gauge32
_AgentIpv6IbgpRoutes_Object = MibScalar
agentIpv6IbgpRoutes = _AgentIpv6IbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 11),
    _AgentIpv6IbgpRoutes_Type()
)
agentIpv6IbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6IbgpRoutes.setStatus("current")
_AgentIpv6LocalBgpRoutes_Type = Gauge32
_AgentIpv6LocalBgpRoutes_Object = MibScalar
agentIpv6LocalBgpRoutes = _AgentIpv6LocalBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 12),
    _AgentIpv6LocalBgpRoutes_Type()
)
agentIpv6LocalBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6LocalBgpRoutes.setStatus("current")
_AgentIpv6RejectRoutes_Type = Gauge32
_AgentIpv6RejectRoutes_Object = MibScalar
agentIpv6RejectRoutes = _AgentIpv6RejectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 13),
    _AgentIpv6RejectRoutes_Type()
)
agentIpv6RejectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6RejectRoutes.setStatus("current")
_AgentIpv6TotalRoutes_Type = Gauge32
_AgentIpv6TotalRoutes_Object = MibScalar
agentIpv6TotalRoutes = _AgentIpv6TotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 14),
    _AgentIpv6TotalRoutes_Type()
)
agentIpv6TotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6TotalRoutes.setStatus("current")
_AgentIpv6BestRoutes_Type = Gauge32
_AgentIpv6BestRoutes_Object = MibScalar
agentIpv6BestRoutes = _AgentIpv6BestRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 15),
    _AgentIpv6BestRoutes_Type()
)
agentIpv6BestRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6BestRoutes.setStatus("current")
_AgentIpv6BestRoutesHigh_Type = Gauge32
_AgentIpv6BestRoutesHigh_Object = MibScalar
agentIpv6BestRoutesHigh = _AgentIpv6BestRoutesHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 16),
    _AgentIpv6BestRoutesHigh_Type()
)
agentIpv6BestRoutesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6BestRoutesHigh.setStatus("current")
_AgentIpv6AlternateRoutes_Type = Gauge32
_AgentIpv6AlternateRoutes_Object = MibScalar
agentIpv6AlternateRoutes = _AgentIpv6AlternateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 17),
    _AgentIpv6AlternateRoutes_Type()
)
agentIpv6AlternateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6AlternateRoutes.setStatus("current")
_AgentIpv6RouteAdds_Type = Counter32
_AgentIpv6RouteAdds_Object = MibScalar
agentIpv6RouteAdds = _AgentIpv6RouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 18),
    _AgentIpv6RouteAdds_Type()
)
agentIpv6RouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6RouteAdds.setStatus("current")
_AgentIpv6RouteModifies_Type = Counter32
_AgentIpv6RouteModifies_Object = MibScalar
agentIpv6RouteModifies = _AgentIpv6RouteModifies_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 19),
    _AgentIpv6RouteModifies_Type()
)
agentIpv6RouteModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6RouteModifies.setStatus("current")
_AgentIpv6RouteDeletes_Type = Counter32
_AgentIpv6RouteDeletes_Object = MibScalar
agentIpv6RouteDeletes = _AgentIpv6RouteDeletes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 20),
    _AgentIpv6RouteDeletes_Type()
)
agentIpv6RouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6RouteDeletes.setStatus("current")
_AgentIpv6UnresolvedRouteAdds_Type = Counter32
_AgentIpv6UnresolvedRouteAdds_Object = MibScalar
agentIpv6UnresolvedRouteAdds = _AgentIpv6UnresolvedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 21),
    _AgentIpv6UnresolvedRouteAdds_Type()
)
agentIpv6UnresolvedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6UnresolvedRouteAdds.setStatus("current")
_AgentIpv6InvalidRouteAdds_Type = Counter32
_AgentIpv6InvalidRouteAdds_Object = MibScalar
agentIpv6InvalidRouteAdds = _AgentIpv6InvalidRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 22),
    _AgentIpv6InvalidRouteAdds_Type()
)
agentIpv6InvalidRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6InvalidRouteAdds.setStatus("current")
_AgentIpv6FailedRouteAdds_Type = Counter32
_AgentIpv6FailedRouteAdds_Object = MibScalar
agentIpv6FailedRouteAdds = _AgentIpv6FailedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 23),
    _AgentIpv6FailedRouteAdds_Type()
)
agentIpv6FailedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6FailedRouteAdds.setStatus("current")
_AgentIpv6ReservedLocals_Type = Gauge32
_AgentIpv6ReservedLocals_Object = MibScalar
agentIpv6ReservedLocals = _AgentIpv6ReservedLocals_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 24),
    _AgentIpv6ReservedLocals_Type()
)
agentIpv6ReservedLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6ReservedLocals.setStatus("current")
_AgentIpv6UniqueNextHops_Type = Gauge32
_AgentIpv6UniqueNextHops_Object = MibScalar
agentIpv6UniqueNextHops = _AgentIpv6UniqueNextHops_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 25),
    _AgentIpv6UniqueNextHops_Type()
)
agentIpv6UniqueNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6UniqueNextHops.setStatus("current")
_AgentIpv6UniqueNextHopsHigh_Type = Gauge32
_AgentIpv6UniqueNextHopsHigh_Object = MibScalar
agentIpv6UniqueNextHopsHigh = _AgentIpv6UniqueNextHopsHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 26),
    _AgentIpv6UniqueNextHopsHigh_Type()
)
agentIpv6UniqueNextHopsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6UniqueNextHopsHigh.setStatus("current")
_AgentIpv6NextHopGroups_Type = Gauge32
_AgentIpv6NextHopGroups_Object = MibScalar
agentIpv6NextHopGroups = _AgentIpv6NextHopGroups_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 27),
    _AgentIpv6NextHopGroups_Type()
)
agentIpv6NextHopGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NextHopGroups.setStatus("current")
_AgentIpv6NextHopGroupsHigh_Type = Gauge32
_AgentIpv6NextHopGroupsHigh_Object = MibScalar
agentIpv6NextHopGroupsHigh = _AgentIpv6NextHopGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 28),
    _AgentIpv6NextHopGroupsHigh_Type()
)
agentIpv6NextHopGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NextHopGroupsHigh.setStatus("current")
_AgentIpv6EcmpGroups_Type = Gauge32
_AgentIpv6EcmpGroups_Object = MibScalar
agentIpv6EcmpGroups = _AgentIpv6EcmpGroups_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 29),
    _AgentIpv6EcmpGroups_Type()
)
agentIpv6EcmpGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EcmpGroups.setStatus("current")
_AgentIpv6EcmpGroupsHigh_Type = Gauge32
_AgentIpv6EcmpGroupsHigh_Object = MibScalar
agentIpv6EcmpGroupsHigh = _AgentIpv6EcmpGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 30),
    _AgentIpv6EcmpGroupsHigh_Type()
)
agentIpv6EcmpGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EcmpGroupsHigh.setStatus("current")
_AgentIpv6EcmpRoutes_Type = Gauge32
_AgentIpv6EcmpRoutes_Object = MibScalar
agentIpv6EcmpRoutes = _AgentIpv6EcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 31),
    _AgentIpv6EcmpRoutes_Type()
)
agentIpv6EcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EcmpRoutes.setStatus("current")
_AgentIpv6TruncEcmpRoutes_Type = Gauge32
_AgentIpv6TruncEcmpRoutes_Object = MibScalar
agentIpv6TruncEcmpRoutes = _AgentIpv6TruncEcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 32),
    _AgentIpv6TruncEcmpRoutes_Type()
)
agentIpv6TruncEcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6TruncEcmpRoutes.setStatus("current")
_AgentIpv6EcmpRetries_Type = Counter32
_AgentIpv6EcmpRetries_Object = MibScalar
agentIpv6EcmpRetries = _AgentIpv6EcmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 10, 33),
    _AgentIpv6EcmpRetries_Type()
)
agentIpv6EcmpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EcmpRetries.setStatus("current")
_AgentIpv6EcmpCountTable_Object = MibTable
agentIpv6EcmpCountTable = _AgentIpv6EcmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 11)
)
if mibBuilder.loadTexts:
    agentIpv6EcmpCountTable.setStatus("current")
_AgentIpv6EcmpCountEntry_Object = MibTableRow
agentIpv6EcmpCountEntry = _AgentIpv6EcmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 11, 1)
)
agentIpv6EcmpCountEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6EcmpNextHopCount"),
)
if mibBuilder.loadTexts:
    agentIpv6EcmpCountEntry.setStatus("current")


class _AgentIpv6EcmpNextHopCount_Type(Unsigned32):
    """Custom type agentIpv6EcmpNextHopCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentIpv6EcmpNextHopCount_Type.__name__ = "Unsigned32"
_AgentIpv6EcmpNextHopCount_Object = MibTableColumn
agentIpv6EcmpNextHopCount = _AgentIpv6EcmpNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 11, 1, 1),
    _AgentIpv6EcmpNextHopCount_Type()
)
agentIpv6EcmpNextHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6EcmpNextHopCount.setStatus("current")
_AgentIpv6EcmpRouteCount_Type = Gauge32
_AgentIpv6EcmpRouteCount_Object = MibTableColumn
agentIpv6EcmpRouteCount = _AgentIpv6EcmpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 11, 1, 2),
    _AgentIpv6EcmpRouteCount_Type()
)
agentIpv6EcmpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6EcmpRouteCount.setStatus("current")
_AgentIpv6NetworkPortGroup_ObjectIdentity = ObjectIdentity
agentIpv6NetworkPortGroup = _AgentIpv6NetworkPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12)
)
_AgentIpv6NetworkPortNbrTable_Object = MibTable
agentIpv6NetworkPortNbrTable = _AgentIpv6NetworkPortNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1)
)
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrTable.setStatus("current")
_AgentIpv6NetworkPortNbrEntry_Object = MibTableRow
agentIpv6NetworkPortNbrEntry = _AgentIpv6NetworkPortNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1)
)
agentIpv6NetworkPortNbrEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6NetworkPortNbrAddr"),
)
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrEntry.setStatus("current")
_AgentIpv6NetworkPortNbrAddr_Type = Ipv6Address
_AgentIpv6NetworkPortNbrAddr_Object = MibTableColumn
agentIpv6NetworkPortNbrAddr = _AgentIpv6NetworkPortNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 1),
    _AgentIpv6NetworkPortNbrAddr_Type()
)
agentIpv6NetworkPortNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrAddr.setStatus("current")
_AgentIpv6NetworkPortNbrPhysAddr_Type = MacAddress
_AgentIpv6NetworkPortNbrPhysAddr_Object = MibTableColumn
agentIpv6NetworkPortNbrPhysAddr = _AgentIpv6NetworkPortNbrPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 2),
    _AgentIpv6NetworkPortNbrPhysAddr_Type()
)
agentIpv6NetworkPortNbrPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrPhysAddr.setStatus("current")


class _AgentIpv6NetworkPortNbrState_Type(Integer32):
    """Custom type agentIpv6NetworkPortNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_AgentIpv6NetworkPortNbrState_Type.__name__ = "Integer32"
_AgentIpv6NetworkPortNbrState_Object = MibTableColumn
agentIpv6NetworkPortNbrState = _AgentIpv6NetworkPortNbrState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 3),
    _AgentIpv6NetworkPortNbrState_Type()
)
agentIpv6NetworkPortNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrState.setStatus("current")
_AgentIpv6NetworkPortNbrUpdated_Type = TimeStamp
_AgentIpv6NetworkPortNbrUpdated_Object = MibTableColumn
agentIpv6NetworkPortNbrUpdated = _AgentIpv6NetworkPortNbrUpdated_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 4),
    _AgentIpv6NetworkPortNbrUpdated_Type()
)
agentIpv6NetworkPortNbrUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrUpdated.setStatus("current")
_AgentIpv6NetworkPortNbrIsRouter_Type = TruthValue
_AgentIpv6NetworkPortNbrIsRouter_Object = MibTableColumn
agentIpv6NetworkPortNbrIsRouter = _AgentIpv6NetworkPortNbrIsRouter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 5),
    _AgentIpv6NetworkPortNbrIsRouter_Type()
)
agentIpv6NetworkPortNbrIsRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrIsRouter.setStatus("current")


class _AgentIpv6NetworkPortNbrType_Type(Integer32):
    """Custom type agentIpv6NetworkPortNbrType based on Integer32"""
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
        *(("dynamic", 2),
          ("local", 4),
          ("other", 1),
          ("static", 3))
    )


_AgentIpv6NetworkPortNbrType_Type.__name__ = "Integer32"
_AgentIpv6NetworkPortNbrType_Object = MibTableColumn
agentIpv6NetworkPortNbrType = _AgentIpv6NetworkPortNbrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 1, 1, 6),
    _AgentIpv6NetworkPortNbrType_Type()
)
agentIpv6NetworkPortNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrType.setStatus("current")
_AgentIpv6NetworkPortNbrCfgTable_Object = MibTable
agentIpv6NetworkPortNbrCfgTable = _AgentIpv6NetworkPortNbrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 2)
)
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrCfgTable.setStatus("current")
_AgentIpv6NetworkPortNbrCfgEntry_Object = MibTableRow
agentIpv6NetworkPortNbrCfgEntry = _AgentIpv6NetworkPortNbrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 2, 1)
)
agentIpv6NetworkPortNbrCfgEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6NetworkPortNbrCfgAddr"),
)
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrCfgEntry.setStatus("current")
_AgentIpv6NetworkPortNbrCfgAddr_Type = Ipv6Address
_AgentIpv6NetworkPortNbrCfgAddr_Object = MibTableColumn
agentIpv6NetworkPortNbrCfgAddr = _AgentIpv6NetworkPortNbrCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 2, 1, 1),
    _AgentIpv6NetworkPortNbrCfgAddr_Type()
)
agentIpv6NetworkPortNbrCfgAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrCfgAddr.setStatus("current")
_AgentIpv6NetworkPortNbrCfgPhysAddr_Type = MacAddress
_AgentIpv6NetworkPortNbrCfgPhysAddr_Object = MibTableColumn
agentIpv6NetworkPortNbrCfgPhysAddr = _AgentIpv6NetworkPortNbrCfgPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 2, 1, 2),
    _AgentIpv6NetworkPortNbrCfgPhysAddr_Type()
)
agentIpv6NetworkPortNbrCfgPhysAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrCfgPhysAddr.setStatus("current")
_AgentIpv6NetworkPortNbrCfgEntryStatus_Type = RowStatus
_AgentIpv6NetworkPortNbrCfgEntryStatus_Object = MibTableColumn
agentIpv6NetworkPortNbrCfgEntryStatus = _AgentIpv6NetworkPortNbrCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 12, 2, 1, 3),
    _AgentIpv6NetworkPortNbrCfgEntryStatus_Type()
)
agentIpv6NetworkPortNbrCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6NetworkPortNbrCfgEntryStatus.setStatus("current")
_AgentIpv6NbrCfgTable_Object = MibTable
agentIpv6NbrCfgTable = _AgentIpv6NbrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13)
)
if mibBuilder.loadTexts:
    agentIpv6NbrCfgTable.setStatus("current")
_AgentIpv6NbrCfgEntry_Object = MibTableRow
agentIpv6NbrCfgEntry = _AgentIpv6NbrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13, 1)
)
agentIpv6NbrCfgEntry.setIndexNames(
    (0, "DNOS-ROUTING6-MIB", "agentIpv6IfIndex"),
    (0, "DNOS-ROUTING6-MIB", "agentIpv6NbrCfgAddr"),
)
if mibBuilder.loadTexts:
    agentIpv6NbrCfgEntry.setStatus("current")
_AgentIpv6IfIndex_Type = Ipv6IfIndex
_AgentIpv6IfIndex_Object = MibTableColumn
agentIpv6IfIndex = _AgentIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13, 1, 1),
    _AgentIpv6IfIndex_Type()
)
agentIpv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6IfIndex.setStatus("current")
_AgentIpv6NbrCfgAddr_Type = Ipv6Address
_AgentIpv6NbrCfgAddr_Object = MibTableColumn
agentIpv6NbrCfgAddr = _AgentIpv6NbrCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13, 1, 2),
    _AgentIpv6NbrCfgAddr_Type()
)
agentIpv6NbrCfgAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentIpv6NbrCfgAddr.setStatus("current")
_AgentIpv6NbrCfgPhysAddr_Type = MacAddress
_AgentIpv6NbrCfgPhysAddr_Object = MibTableColumn
agentIpv6NbrCfgPhysAddr = _AgentIpv6NbrCfgPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13, 1, 3),
    _AgentIpv6NbrCfgPhysAddr_Type()
)
agentIpv6NbrCfgPhysAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6NbrCfgPhysAddr.setStatus("current")
_AgentIpv6NbrCfgEntryStatus_Type = RowStatus
_AgentIpv6NbrCfgEntryStatus_Object = MibTableColumn
agentIpv6NbrCfgEntryStatus = _AgentIpv6NbrCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 13, 1, 4),
    _AgentIpv6NbrCfgEntryStatus_Type()
)
agentIpv6NbrCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIpv6NbrCfgEntryStatus.setStatus("current")


class _AgentIpv6NeighborsDynamicRenew_Type(Integer32):
    """Custom type agentIpv6NeighborsDynamicRenew based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentIpv6NeighborsDynamicRenew_Type.__name__ = "Integer32"
_AgentIpv6NeighborsDynamicRenew_Object = MibScalar
agentIpv6NeighborsDynamicRenew = _AgentIpv6NeighborsDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 14),
    _AgentIpv6NeighborsDynamicRenew_Type()
)
agentIpv6NeighborsDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6NeighborsDynamicRenew.setStatus("current")


class _AgentIpv6UnresolvedDataRateLimit_Type(Integer32):
    """Custom type agentIpv6UnresolvedDataRateLimit based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1024),
    )


_AgentIpv6UnresolvedDataRateLimit_Type.__name__ = "Integer32"
_AgentIpv6UnresolvedDataRateLimit_Object = MibScalar
agentIpv6UnresolvedDataRateLimit = _AgentIpv6UnresolvedDataRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 15),
    _AgentIpv6UnresolvedDataRateLimit_Type()
)
agentIpv6UnresolvedDataRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6UnresolvedDataRateLimit.setStatus("current")


class _AgentIpv6NUDMaxUnicastSolicits_Type(Integer32):
    """Custom type agentIpv6NUDMaxUnicastSolicits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_AgentIpv6NUDMaxUnicastSolicits_Type.__name__ = "Integer32"
_AgentIpv6NUDMaxUnicastSolicits_Object = MibScalar
agentIpv6NUDMaxUnicastSolicits = _AgentIpv6NUDMaxUnicastSolicits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 16),
    _AgentIpv6NUDMaxUnicastSolicits_Type()
)
agentIpv6NUDMaxUnicastSolicits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6NUDMaxUnicastSolicits.setStatus("current")


class _AgentIpv6NUDMaxMulticastSolicits_Type(Integer32):
    """Custom type agentIpv6NUDMaxMulticastSolicits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_AgentIpv6NUDMaxMulticastSolicits_Type.__name__ = "Integer32"
_AgentIpv6NUDMaxMulticastSolicits_Object = MibScalar
agentIpv6NUDMaxMulticastSolicits = _AgentIpv6NUDMaxMulticastSolicits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 17),
    _AgentIpv6NUDMaxMulticastSolicits_Type()
)
agentIpv6NUDMaxMulticastSolicits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6NUDMaxMulticastSolicits.setStatus("current")


class _AgentIpv6NUDBackoffMultiple_Type(Integer32):
    """Custom type agentIpv6NUDBackoffMultiple based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AgentIpv6NUDBackoffMultiple_Type.__name__ = "Integer32"
_AgentIpv6NUDBackoffMultiple_Object = MibScalar
agentIpv6NUDBackoffMultiple = _AgentIpv6NUDBackoffMultiple_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 30, 1, 18),
    _AgentIpv6NUDBackoffMultiple_Type()
)
agentIpv6NUDBackoffMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpv6NUDBackoffMultiple.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-ROUTING6-MIB",
    **{"fastPathRoutingIpv6": fastPathRoutingIpv6,
       "agentIpv6Group": agentIpv6Group,
       "agentIpv6RoutingMode": agentIpv6RoutingMode,
       "agentIpv6InterfaceTable": agentIpv6InterfaceTable,
       "agentIpv6InterfaceEntry": agentIpv6InterfaceEntry,
       "agentIpv6InterfaceIfIndex": agentIpv6InterfaceIfIndex,
       "agentIpv6InterfaceMtuValue": agentIpv6InterfaceMtuValue,
       "agentIpv6InterfaceDadTransmits": agentIpv6InterfaceDadTransmits,
       "agentIpv6InterfaceLinkLocalOnly": agentIpv6InterfaceLinkLocalOnly,
       "agentIpv6InterfaceIcmpUnreachables": agentIpv6InterfaceIcmpUnreachables,
       "agentIpv6InterfaceAutoconfig": agentIpv6InterfaceAutoconfig,
       "agentIpv6InterfaceDhcpClient": agentIpv6InterfaceDhcpClient,
       "agentIpv6InterfaceIcmpRedirects": agentIpv6InterfaceIcmpRedirects,
       "agentIpv6RouterAdvertisementTable": agentIpv6RouterAdvertisementTable,
       "agentIpv6RouterAdvertisementEntry": agentIpv6RouterAdvertisementEntry,
       "agentIpv6RouterAdvertisementIfIndex": agentIpv6RouterAdvertisementIfIndex,
       "agentIpv6RouterAdvertisementSuppressMode": agentIpv6RouterAdvertisementSuppressMode,
       "agentIpv6RouterAdvertisementMaxAdvertisementInterval": agentIpv6RouterAdvertisementMaxAdvertisementInterval,
       "agentIpv6RouterAdvertisementAdvertisementLifetime": agentIpv6RouterAdvertisementAdvertisementLifetime,
       "agentIpv6RouterAdvertisementNbrSolicitInterval": agentIpv6RouterAdvertisementNbrSolicitInterval,
       "agentIpv6RouterAdvertisementReachableTime": agentIpv6RouterAdvertisementReachableTime,
       "agentIpv6RouterAdvertisementManagedFlag": agentIpv6RouterAdvertisementManagedFlag,
       "agentIpv6RouterAdvertisementOtherFlag": agentIpv6RouterAdvertisementOtherFlag,
       "agentIpv6RouterAdvertisementHopLimitUnspecifiedMode": agentIpv6RouterAdvertisementHopLimitUnspecifiedMode,
       "agentIpv6AddrPrefixTable": agentIpv6AddrPrefixTable,
       "agentIpv6AddrPrefixEntry": agentIpv6AddrPrefixEntry,
       "agentIpv6AddrPrefix": agentIpv6AddrPrefix,
       "agentIpv6AddrPrefixLength": agentIpv6AddrPrefixLength,
       "agentIpv6AddrPrefixOnLinkFlag": agentIpv6AddrPrefixOnLinkFlag,
       "agentIpv6AddrPrefixAutonomousFlag": agentIpv6AddrPrefixAutonomousFlag,
       "agentIpv6AddrPrefixAdvPreferredLifetime": agentIpv6AddrPrefixAdvPreferredLifetime,
       "agentIpv6AddrPrefixAdvValidLifetime": agentIpv6AddrPrefixAdvValidLifetime,
       "agentIpv6AddrTable": agentIpv6AddrTable,
       "agentIpv6AddrEntry": agentIpv6AddrEntry,
       "agentIpv6AddrAddress": agentIpv6AddrAddress,
       "agentIpv6AddrPfxLength": agentIpv6AddrPfxLength,
       "agentIpv6AddrEui64Flag": agentIpv6AddrEui64Flag,
       "agentIpv6AddrStatus": agentIpv6AddrStatus,
       "agentIpv6StaticRouteTable": agentIpv6StaticRouteTable,
       "agentIpv6StaticRouteEntry": agentIpv6StaticRouteEntry,
       "agentIpv6StaticRouteDest": agentIpv6StaticRouteDest,
       "agentIpv6StaticRoutePfxLength": agentIpv6StaticRoutePfxLength,
       "agentIpv6StaticRouteIfIndex": agentIpv6StaticRouteIfIndex,
       "agentIpv6StaticRouteNextHop": agentIpv6StaticRouteNextHop,
       "agentIpv6StaticRoutePreference": agentIpv6StaticRoutePreference,
       "agentIpv6StaticRouteStatus": agentIpv6StaticRouteStatus,
       "agentIpv6ServicePortGroup": agentIpv6ServicePortGroup,
       "agentIpv6ServicePortPrefixTable": agentIpv6ServicePortPrefixTable,
       "agentIpv6ServicePortPrefixEntry": agentIpv6ServicePortPrefixEntry,
       "agentIpv6ServicePortPrefixIndex": agentIpv6ServicePortPrefixIndex,
       "agentIpv6ServicePortPrefix": agentIpv6ServicePortPrefix,
       "agentIpv6ServicePortPrefixLength": agentIpv6ServicePortPrefixLength,
       "agentIpv6ServicePortDefaultRouterTable": agentIpv6ServicePortDefaultRouterTable,
       "agentIpv6ServicePortDefaultRouterEntry": agentIpv6ServicePortDefaultRouterEntry,
       "agentIpv6ServicePortDefaultRouterIndex": agentIpv6ServicePortDefaultRouterIndex,
       "agentIpv6ServicePortDefaultRouter": agentIpv6ServicePortDefaultRouter,
       "agentIpv6ServicePortNbrTable": agentIpv6ServicePortNbrTable,
       "agentIpv6ServicePortNbrEntry": agentIpv6ServicePortNbrEntry,
       "agentIpv6ServicePortNbrAddr": agentIpv6ServicePortNbrAddr,
       "agentIpv6ServicePortNbrPhysAddr": agentIpv6ServicePortNbrPhysAddr,
       "agentIpv6ServicePortNbrState": agentIpv6ServicePortNbrState,
       "agentIpv6ServicePortNbrUpdated": agentIpv6ServicePortNbrUpdated,
       "agentIpv6ServicePortNbrIsRouter": agentIpv6ServicePortNbrIsRouter,
       "agentIpv6ServicePortNbrType": agentIpv6ServicePortNbrType,
       "agentIpv6ServicePortNbrCfgTable": agentIpv6ServicePortNbrCfgTable,
       "agentIpv6ServicePortNbrCfgEntry": agentIpv6ServicePortNbrCfgEntry,
       "agentIpv6ServicePortNbrCfgAddr": agentIpv6ServicePortNbrCfgAddr,
       "agentIpv6ServicePortNbrCfgPhysAddr": agentIpv6ServicePortNbrCfgPhysAddr,
       "agentIpv6ServicePortNbrCfgEntryStatus": agentIpv6ServicePortNbrCfgEntryStatus,
       "agentIpv6IcmpControlGroup": agentIpv6IcmpControlGroup,
       "agentIpv6IcmpRateLimitInterval": agentIpv6IcmpRateLimitInterval,
       "agentIpv6IcmpRateLimitBurstSize": agentIpv6IcmpRateLimitBurstSize,
       "agentDhcp6ClientParametersTable": agentDhcp6ClientParametersTable,
       "agentDhcp6ClientParametersEntry": agentDhcp6ClientParametersEntry,
       "agentDhcp6ClientInterfaceIndex": agentDhcp6ClientInterfaceIndex,
       "agentDhcp6ClientPrefix": agentDhcp6ClientPrefix,
       "agentDhcp6ClientPrefixlength": agentDhcp6ClientPrefixlength,
       "agentDhcp6ClientState": agentDhcp6ClientState,
       "agentDhcp6ClientServerDUID": agentDhcp6ClientServerDUID,
       "agentDhcp6ClientT1Time": agentDhcp6ClientT1Time,
       "agentDhcp6ClientT2Time": agentDhcp6ClientT2Time,
       "agentDhcp6ClientIAID": agentDhcp6ClientIAID,
       "agentDhcp6ClientPreferredLifeTime": agentDhcp6ClientPreferredLifeTime,
       "agentDhcp6ClientValidLifeTime": agentDhcp6ClientValidLifeTime,
       "agentDhcp6ClientRenewTime": agentDhcp6ClientRenewTime,
       "agentDhcp6ClientExpireTime": agentDhcp6ClientExpireTime,
       "agentIpv6RoutingTableSummaryGroup": agentIpv6RoutingTableSummaryGroup,
       "agentIpv6ConnectedRoutes": agentIpv6ConnectedRoutes,
       "agentIpv6StaticRoutes": agentIpv6StaticRoutes,
       "agentIpv66to4Routes": agentIpv66to4Routes,
       "agentIpv6OspfRoutes": agentIpv6OspfRoutes,
       "agentIpv6OspfIntraRoutes": agentIpv6OspfIntraRoutes,
       "agentIpv6OspfInterRoutes": agentIpv6OspfInterRoutes,
       "agentIpv6OspfExt1Routes": agentIpv6OspfExt1Routes,
       "agentIpv6OspfExt2Routes": agentIpv6OspfExt2Routes,
       "agentIpv6BgpRoutes": agentIpv6BgpRoutes,
       "agentIpv6EbgpRoutes": agentIpv6EbgpRoutes,
       "agentIpv6IbgpRoutes": agentIpv6IbgpRoutes,
       "agentIpv6LocalBgpRoutes": agentIpv6LocalBgpRoutes,
       "agentIpv6RejectRoutes": agentIpv6RejectRoutes,
       "agentIpv6TotalRoutes": agentIpv6TotalRoutes,
       "agentIpv6BestRoutes": agentIpv6BestRoutes,
       "agentIpv6BestRoutesHigh": agentIpv6BestRoutesHigh,
       "agentIpv6AlternateRoutes": agentIpv6AlternateRoutes,
       "agentIpv6RouteAdds": agentIpv6RouteAdds,
       "agentIpv6RouteModifies": agentIpv6RouteModifies,
       "agentIpv6RouteDeletes": agentIpv6RouteDeletes,
       "agentIpv6UnresolvedRouteAdds": agentIpv6UnresolvedRouteAdds,
       "agentIpv6InvalidRouteAdds": agentIpv6InvalidRouteAdds,
       "agentIpv6FailedRouteAdds": agentIpv6FailedRouteAdds,
       "agentIpv6ReservedLocals": agentIpv6ReservedLocals,
       "agentIpv6UniqueNextHops": agentIpv6UniqueNextHops,
       "agentIpv6UniqueNextHopsHigh": agentIpv6UniqueNextHopsHigh,
       "agentIpv6NextHopGroups": agentIpv6NextHopGroups,
       "agentIpv6NextHopGroupsHigh": agentIpv6NextHopGroupsHigh,
       "agentIpv6EcmpGroups": agentIpv6EcmpGroups,
       "agentIpv6EcmpGroupsHigh": agentIpv6EcmpGroupsHigh,
       "agentIpv6EcmpRoutes": agentIpv6EcmpRoutes,
       "agentIpv6TruncEcmpRoutes": agentIpv6TruncEcmpRoutes,
       "agentIpv6EcmpRetries": agentIpv6EcmpRetries,
       "agentIpv6EcmpCountTable": agentIpv6EcmpCountTable,
       "agentIpv6EcmpCountEntry": agentIpv6EcmpCountEntry,
       "agentIpv6EcmpNextHopCount": agentIpv6EcmpNextHopCount,
       "agentIpv6EcmpRouteCount": agentIpv6EcmpRouteCount,
       "agentIpv6NetworkPortGroup": agentIpv6NetworkPortGroup,
       "agentIpv6NetworkPortNbrTable": agentIpv6NetworkPortNbrTable,
       "agentIpv6NetworkPortNbrEntry": agentIpv6NetworkPortNbrEntry,
       "agentIpv6NetworkPortNbrAddr": agentIpv6NetworkPortNbrAddr,
       "agentIpv6NetworkPortNbrPhysAddr": agentIpv6NetworkPortNbrPhysAddr,
       "agentIpv6NetworkPortNbrState": agentIpv6NetworkPortNbrState,
       "agentIpv6NetworkPortNbrUpdated": agentIpv6NetworkPortNbrUpdated,
       "agentIpv6NetworkPortNbrIsRouter": agentIpv6NetworkPortNbrIsRouter,
       "agentIpv6NetworkPortNbrType": agentIpv6NetworkPortNbrType,
       "agentIpv6NetworkPortNbrCfgTable": agentIpv6NetworkPortNbrCfgTable,
       "agentIpv6NetworkPortNbrCfgEntry": agentIpv6NetworkPortNbrCfgEntry,
       "agentIpv6NetworkPortNbrCfgAddr": agentIpv6NetworkPortNbrCfgAddr,
       "agentIpv6NetworkPortNbrCfgPhysAddr": agentIpv6NetworkPortNbrCfgPhysAddr,
       "agentIpv6NetworkPortNbrCfgEntryStatus": agentIpv6NetworkPortNbrCfgEntryStatus,
       "agentIpv6NbrCfgTable": agentIpv6NbrCfgTable,
       "agentIpv6NbrCfgEntry": agentIpv6NbrCfgEntry,
       "agentIpv6IfIndex": agentIpv6IfIndex,
       "agentIpv6NbrCfgAddr": agentIpv6NbrCfgAddr,
       "agentIpv6NbrCfgPhysAddr": agentIpv6NbrCfgPhysAddr,
       "agentIpv6NbrCfgEntryStatus": agentIpv6NbrCfgEntryStatus,
       "agentIpv6NeighborsDynamicRenew": agentIpv6NeighborsDynamicRenew,
       "agentIpv6UnresolvedDataRateLimit": agentIpv6UnresolvedDataRateLimit,
       "agentIpv6NUDMaxUnicastSolicits": agentIpv6NUDMaxUnicastSolicits,
       "agentIpv6NUDMaxMulticastSolicits": agentIpv6NUDMaxMulticastSolicits,
       "agentIpv6NUDBackoffMultiple": agentIpv6NUDBackoffMultiple}
)
