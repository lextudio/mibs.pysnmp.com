# SNMP MIB module (IPV6-UDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-UDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:31 2024
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

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
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
 experimental,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipv6UdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 87)
)
ipv6UdpMIB.setRevisions(
        ("2017-02-22 00:00",
         "1998-01-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_Ipv6UdpTable_Object = MibTable
ipv6UdpTable = _Ipv6UdpTable_Object(
    (1, 3, 6, 1, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    ipv6UdpTable.setStatus("obsolete")
_Ipv6UdpEntry_Object = MibTableRow
ipv6UdpEntry = _Ipv6UdpEntry_Object(
    (1, 3, 6, 1, 2, 1, 7, 6, 1)
)
ipv6UdpEntry.setIndexNames(
    (0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"),
    (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"),
    (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"),
)
if mibBuilder.loadTexts:
    ipv6UdpEntry.setStatus("obsolete")
_Ipv6UdpLocalAddress_Type = Ipv6Address
_Ipv6UdpLocalAddress_Object = MibTableColumn
ipv6UdpLocalAddress = _Ipv6UdpLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 7, 6, 1, 1),
    _Ipv6UdpLocalAddress_Type()
)
ipv6UdpLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6UdpLocalAddress.setStatus("obsolete")


class _Ipv6UdpLocalPort_Type(Integer32):
    """Custom type ipv6UdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6UdpLocalPort_Type.__name__ = "Integer32"
_Ipv6UdpLocalPort_Object = MibTableColumn
ipv6UdpLocalPort = _Ipv6UdpLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 7, 6, 1, 2),
    _Ipv6UdpLocalPort_Type()
)
ipv6UdpLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6UdpLocalPort.setStatus("obsolete")
_Ipv6UdpIfIndex_Type = Ipv6IfIndexOrZero
_Ipv6UdpIfIndex_Object = MibTableColumn
ipv6UdpIfIndex = _Ipv6UdpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 7, 6, 1, 3),
    _Ipv6UdpIfIndex_Type()
)
ipv6UdpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6UdpIfIndex.setStatus("obsolete")
_Ipv6UdpConformance_ObjectIdentity = ObjectIdentity
ipv6UdpConformance = _Ipv6UdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 87, 2)
)
_Ipv6UdpCompliances_ObjectIdentity = ObjectIdentity
ipv6UdpCompliances = _Ipv6UdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 87, 2, 1)
)
_Ipv6UdpGroups_ObjectIdentity = ObjectIdentity
ipv6UdpGroups = _Ipv6UdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 87, 2, 2)
)

# Managed Objects groups

ipv6UdpGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 87, 2, 2, 1)
)
ipv6UdpGroup.setObjects(
    ("IPV6-UDP-MIB", "ipv6UdpIfIndex")
)
if mibBuilder.loadTexts:
    ipv6UdpGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipv6UdpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 87, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6UdpCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-UDP-MIB",
    **{"udp": udp,
       "ipv6UdpTable": ipv6UdpTable,
       "ipv6UdpEntry": ipv6UdpEntry,
       "ipv6UdpLocalAddress": ipv6UdpLocalAddress,
       "ipv6UdpLocalPort": ipv6UdpLocalPort,
       "ipv6UdpIfIndex": ipv6UdpIfIndex,
       "ipv6UdpMIB": ipv6UdpMIB,
       "ipv6UdpConformance": ipv6UdpConformance,
       "ipv6UdpCompliances": ipv6UdpCompliances,
       "ipv6UdpCompliance": ipv6UdpCompliance,
       "ipv6UdpGroups": ipv6UdpGroups,
       "ipv6UdpGroup": ipv6UdpGroup}
)
