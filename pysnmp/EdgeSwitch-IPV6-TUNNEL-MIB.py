# SNMP MIB module (EdgeSwitch-IPV6-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-IPV6-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:46 2024
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
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InetAddressIPv4,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressPrefixLength")

(Ipv6Address,
 Ipv6AddressPrefix,
 Ipv6IfIndex) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix",
    "Ipv6IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathIpv6Tunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27)
)
fastPathIpv6Tunnel.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentTunnelIPV6Group_ObjectIdentity = ObjectIdentity
agentTunnelIPV6Group = _AgentTunnelIPV6Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1)
)
_AgentTunnelIPV6Table_Object = MibTable
agentTunnelIPV6Table = _AgentTunnelIPV6Table_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1)
)
if mibBuilder.loadTexts:
    agentTunnelIPV6Table.setStatus("current")
_AgentTunnelIPV6Entry_Object = MibTableRow
agentTunnelIPV6Entry = _AgentTunnelIPV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1)
)
agentTunnelIPV6Entry.setIndexNames(
    (0, "EdgeSwitch-IPV6-TUNNEL-MIB", "agentTunnelID"),
)
if mibBuilder.loadTexts:
    agentTunnelIPV6Entry.setStatus("current")


class _AgentTunnelID_Type(Integer32):
    """Custom type agentTunnelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentTunnelID_Type.__name__ = "Integer32"
_AgentTunnelID_Object = MibTableColumn
agentTunnelID = _AgentTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 1),
    _AgentTunnelID_Type()
)
agentTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTunnelID.setStatus("current")
_AgentTunnelIfIndex_Type = Integer32
_AgentTunnelIfIndex_Object = MibTableColumn
agentTunnelIfIndex = _AgentTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 2),
    _AgentTunnelIfIndex_Type()
)
agentTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTunnelIfIndex.setStatus("current")


class _AgentTunnelMode_Type(Integer32):
    """Custom type agentTunnelMode based on Integer32"""
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
        *(("ip6over4", 2),
          ("ip6to4", 3),
          ("undefined", 1))
    )


_AgentTunnelMode_Type.__name__ = "Integer32"
_AgentTunnelMode_Object = MibTableColumn
agentTunnelMode = _AgentTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 3),
    _AgentTunnelMode_Type()
)
agentTunnelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTunnelMode.setStatus("current")
_AgentTunnelLocalIP4Addr_Type = InetAddressIPv4
_AgentTunnelLocalIP4Addr_Object = MibTableColumn
agentTunnelLocalIP4Addr = _AgentTunnelLocalIP4Addr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 4),
    _AgentTunnelLocalIP4Addr_Type()
)
agentTunnelLocalIP4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTunnelLocalIP4Addr.setStatus("current")
_AgentTunnelRemoteIP4Addr_Type = InetAddressIPv4
_AgentTunnelRemoteIP4Addr_Object = MibTableColumn
agentTunnelRemoteIP4Addr = _AgentTunnelRemoteIP4Addr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 5),
    _AgentTunnelRemoteIP4Addr_Type()
)
agentTunnelRemoteIP4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTunnelRemoteIP4Addr.setStatus("current")
_AgentTunnelLocalIfIndex_Type = Integer32
_AgentTunnelLocalIfIndex_Object = MibTableColumn
agentTunnelLocalIfIndex = _AgentTunnelLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 6),
    _AgentTunnelLocalIfIndex_Type()
)
agentTunnelLocalIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTunnelLocalIfIndex.setStatus("current")
_AgentTunnelStatus_Type = RowStatus
_AgentTunnelStatus_Object = MibTableColumn
agentTunnelStatus = _AgentTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 7),
    _AgentTunnelStatus_Type()
)
agentTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTunnelStatus.setStatus("current")


class _AgentTunnelIcmpUnreachableMode_Type(Integer32):
    """Custom type agentTunnelIcmpUnreachableMode based on Integer32"""
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


_AgentTunnelIcmpUnreachableMode_Type.__name__ = "Integer32"
_AgentTunnelIcmpUnreachableMode_Object = MibTableColumn
agentTunnelIcmpUnreachableMode = _AgentTunnelIcmpUnreachableMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 1, 1, 8),
    _AgentTunnelIcmpUnreachableMode_Type()
)
agentTunnelIcmpUnreachableMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTunnelIcmpUnreachableMode.setStatus("current")
_AgentTunnelIPV6PrefixTable_Object = MibTable
agentTunnelIPV6PrefixTable = _AgentTunnelIPV6PrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 2)
)
if mibBuilder.loadTexts:
    agentTunnelIPV6PrefixTable.setStatus("current")
_AgentTunnelIPV6PrefixEntry_Object = MibTableRow
agentTunnelIPV6PrefixEntry = _AgentTunnelIPV6PrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 2, 1)
)
agentTunnelIPV6PrefixEntry.setIndexNames(
    (0, "EdgeSwitch-IPV6-TUNNEL-MIB", "agentTunnelID"),
    (0, "EdgeSwitch-IPV6-TUNNEL-MIB", "agentTunnelIPV6PrefixPrefix"),
    (0, "EdgeSwitch-IPV6-TUNNEL-MIB", "agentTunnelIPV6PrefixPrefixLen"),
)
if mibBuilder.loadTexts:
    agentTunnelIPV6PrefixEntry.setStatus("current")
_AgentTunnelIPV6PrefixPrefix_Type = Ipv6AddressPrefix
_AgentTunnelIPV6PrefixPrefix_Object = MibTableColumn
agentTunnelIPV6PrefixPrefix = _AgentTunnelIPV6PrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 2, 1, 1),
    _AgentTunnelIPV6PrefixPrefix_Type()
)
agentTunnelIPV6PrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTunnelIPV6PrefixPrefix.setStatus("current")


class _AgentTunnelIPV6PrefixPrefixLen_Type(InetAddressPrefixLength):
    """Custom type agentTunnelIPV6PrefixPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AgentTunnelIPV6PrefixPrefixLen_Object = MibTableColumn
agentTunnelIPV6PrefixPrefixLen = _AgentTunnelIPV6PrefixPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 2, 1, 2),
    _AgentTunnelIPV6PrefixPrefixLen_Type()
)
agentTunnelIPV6PrefixPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTunnelIPV6PrefixPrefixLen.setStatus("current")
_AgentTunnelIPV6PrefixStatus_Type = RowStatus
_AgentTunnelIPV6PrefixStatus_Object = MibTableColumn
agentTunnelIPV6PrefixStatus = _AgentTunnelIPV6PrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 27, 1, 2, 1, 3),
    _AgentTunnelIPV6PrefixStatus_Type()
)
agentTunnelIPV6PrefixStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTunnelIPV6PrefixStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-IPV6-TUNNEL-MIB",
    **{"fastPathIpv6Tunnel": fastPathIpv6Tunnel,
       "agentTunnelIPV6Group": agentTunnelIPV6Group,
       "agentTunnelIPV6Table": agentTunnelIPV6Table,
       "agentTunnelIPV6Entry": agentTunnelIPV6Entry,
       "agentTunnelID": agentTunnelID,
       "agentTunnelIfIndex": agentTunnelIfIndex,
       "agentTunnelMode": agentTunnelMode,
       "agentTunnelLocalIP4Addr": agentTunnelLocalIP4Addr,
       "agentTunnelRemoteIP4Addr": agentTunnelRemoteIP4Addr,
       "agentTunnelLocalIfIndex": agentTunnelLocalIfIndex,
       "agentTunnelStatus": agentTunnelStatus,
       "agentTunnelIcmpUnreachableMode": agentTunnelIcmpUnreachableMode,
       "agentTunnelIPV6PrefixTable": agentTunnelIPV6PrefixTable,
       "agentTunnelIPV6PrefixEntry": agentTunnelIPV6PrefixEntry,
       "agentTunnelIPV6PrefixPrefix": agentTunnelIPV6PrefixPrefix,
       "agentTunnelIPV6PrefixPrefixLen": agentTunnelIPV6PrefixPrefixLen,
       "agentTunnelIPV6PrefixStatus": agentTunnelIPV6PrefixStatus}
)
