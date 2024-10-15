# SNMP MIB module (FASTPATH-ROUTING6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-ROUTING6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:11 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

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
        ("2007-05-23 00:00",
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6RouterAdvertisementIfIndex"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6AddrPrefix"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6AddrPrefixLength"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6InterfaceIfIndex"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6AddrAddress"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6StaticRouteDest"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6StaticRoutePfxLength"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6StaticRouteIfIndex"),
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6StaticRouteNextHop"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6ServicePortPrefixIndex"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6ServicePortDefaultRouterIndex"),
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
    (0, "FASTPATH-ROUTING6-MIB", "agentIpv6ServicePortNbrAddr"),
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-ROUTING6-MIB",
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
       "agentIpv6IcmpControlGroup": agentIpv6IcmpControlGroup,
       "agentIpv6IcmpRateLimitInterval": agentIpv6IcmpRateLimitInterval,
       "agentIpv6IcmpRateLimitBurstSize": agentIpv6IcmpRateLimitBurstSize}
)
