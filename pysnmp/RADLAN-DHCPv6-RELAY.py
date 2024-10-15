# SNMP MIB module (RADLAN-DHCPv6-RELAY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DHCPv6-RELAY
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:08 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(rlDhcpv6Relay,) = mibBuilder.importSymbols(
    "RADLAN-DHCPv6",
    "rlDhcpv6Relay")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpv6RelayInterfaceListTable_Object = MibTable
rlDhcpv6RelayInterfaceListTable = _RlDhcpv6RelayInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 1)
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceListTable.setStatus("current")
_RlDhcpv6RelayInterfaceListEntry_Object = MibTableRow
rlDhcpv6RelayInterfaceListEntry = _RlDhcpv6RelayInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1)
)
rlDhcpv6RelayInterfaceListEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceListIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceListEntry.setStatus("current")
_RlDhcpv6RelayInterfaceListIfIndex_Type = Unsigned32
_RlDhcpv6RelayInterfaceListIfIndex_Object = MibTableColumn
rlDhcpv6RelayInterfaceListIfIndex = _RlDhcpv6RelayInterfaceListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1, 1),
    _RlDhcpv6RelayInterfaceListIfIndex_Type()
)
rlDhcpv6RelayInterfaceListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceListIfIndex.setStatus("current")
_RlDhcpv6RelayInterfaceListRowStatus_Type = RowStatus
_RlDhcpv6RelayInterfaceListRowStatus_Object = MibTableColumn
rlDhcpv6RelayInterfaceListRowStatus = _RlDhcpv6RelayInterfaceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1, 2),
    _RlDhcpv6RelayInterfaceListRowStatus_Type()
)
rlDhcpv6RelayInterfaceListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceListRowStatus.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalTable_Object = MibTable
rlDhcpv6RelayDestinationsGlobalTable = _RlDhcpv6RelayDestinationsGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2)
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalTable.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalEntry_Object = MibTableRow
rlDhcpv6RelayDestinationsGlobalEntry = _RlDhcpv6RelayDestinationsGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1)
)
rlDhcpv6RelayDestinationsGlobalEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalIpv6AddrType"),
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalIpv6Addr"),
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalOutputInterface"),
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalEntry.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalIpv6AddrType_Type = InetAddressType
_RlDhcpv6RelayDestinationsGlobalIpv6AddrType_Object = MibTableColumn
rlDhcpv6RelayDestinationsGlobalIpv6AddrType = _RlDhcpv6RelayDestinationsGlobalIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 1),
    _RlDhcpv6RelayDestinationsGlobalIpv6AddrType_Type()
)
rlDhcpv6RelayDestinationsGlobalIpv6AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalIpv6AddrType.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalIpv6Addr_Type = InetAddress
_RlDhcpv6RelayDestinationsGlobalIpv6Addr_Object = MibTableColumn
rlDhcpv6RelayDestinationsGlobalIpv6Addr = _RlDhcpv6RelayDestinationsGlobalIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 2),
    _RlDhcpv6RelayDestinationsGlobalIpv6Addr_Type()
)
rlDhcpv6RelayDestinationsGlobalIpv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalIpv6Addr.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalOutputInterface_Type = Unsigned32
_RlDhcpv6RelayDestinationsGlobalOutputInterface_Object = MibTableColumn
rlDhcpv6RelayDestinationsGlobalOutputInterface = _RlDhcpv6RelayDestinationsGlobalOutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 3),
    _RlDhcpv6RelayDestinationsGlobalOutputInterface_Type()
)
rlDhcpv6RelayDestinationsGlobalOutputInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalOutputInterface.setStatus("current")
_RlDhcpv6RelayDestinationsGlobalRowStatus_Type = RowStatus
_RlDhcpv6RelayDestinationsGlobalRowStatus_Object = MibTableColumn
rlDhcpv6RelayDestinationsGlobalRowStatus = _RlDhcpv6RelayDestinationsGlobalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 4),
    _RlDhcpv6RelayDestinationsGlobalRowStatus_Type()
)
rlDhcpv6RelayDestinationsGlobalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6RelayDestinationsGlobalRowStatus.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsTable_Object = MibTable
rlDhcpv6RelayInterfaceDestinationsTable = _RlDhcpv6RelayInterfaceDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3)
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsTable.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsEntry_Object = MibTableRow
rlDhcpv6RelayInterfaceDestinationsEntry = _RlDhcpv6RelayInterfaceDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1)
)
rlDhcpv6RelayInterfaceDestinationsEntry.setIndexNames(
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIfindex"),
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIpv6AddrType"),
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIpv6Addr"),
    (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsOutputInterface"),
)
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsEntry.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsIfindex_Type = Unsigned32
_RlDhcpv6RelayInterfaceDestinationsIfindex_Object = MibTableColumn
rlDhcpv6RelayInterfaceDestinationsIfindex = _RlDhcpv6RelayInterfaceDestinationsIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 1),
    _RlDhcpv6RelayInterfaceDestinationsIfindex_Type()
)
rlDhcpv6RelayInterfaceDestinationsIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsIfindex.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsIpv6AddrType_Type = InetAddressType
_RlDhcpv6RelayInterfaceDestinationsIpv6AddrType_Object = MibTableColumn
rlDhcpv6RelayInterfaceDestinationsIpv6AddrType = _RlDhcpv6RelayInterfaceDestinationsIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 2),
    _RlDhcpv6RelayInterfaceDestinationsIpv6AddrType_Type()
)
rlDhcpv6RelayInterfaceDestinationsIpv6AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsIpv6AddrType.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsIpv6Addr_Type = InetAddress
_RlDhcpv6RelayInterfaceDestinationsIpv6Addr_Object = MibTableColumn
rlDhcpv6RelayInterfaceDestinationsIpv6Addr = _RlDhcpv6RelayInterfaceDestinationsIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 3),
    _RlDhcpv6RelayInterfaceDestinationsIpv6Addr_Type()
)
rlDhcpv6RelayInterfaceDestinationsIpv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsIpv6Addr.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsOutputInterface_Type = Unsigned32
_RlDhcpv6RelayInterfaceDestinationsOutputInterface_Object = MibTableColumn
rlDhcpv6RelayInterfaceDestinationsOutputInterface = _RlDhcpv6RelayInterfaceDestinationsOutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 4),
    _RlDhcpv6RelayInterfaceDestinationsOutputInterface_Type()
)
rlDhcpv6RelayInterfaceDestinationsOutputInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsOutputInterface.setStatus("current")
_RlDhcpv6RelayInterfaceDestinationsRowStatus_Type = RowStatus
_RlDhcpv6RelayInterfaceDestinationsRowStatus_Object = MibTableColumn
rlDhcpv6RelayInterfaceDestinationsRowStatus = _RlDhcpv6RelayInterfaceDestinationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 5),
    _RlDhcpv6RelayInterfaceDestinationsRowStatus_Type()
)
rlDhcpv6RelayInterfaceDestinationsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpv6RelayInterfaceDestinationsRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DHCPv6-RELAY",
    **{"rlDhcpv6RelayInterfaceListTable": rlDhcpv6RelayInterfaceListTable,
       "rlDhcpv6RelayInterfaceListEntry": rlDhcpv6RelayInterfaceListEntry,
       "rlDhcpv6RelayInterfaceListIfIndex": rlDhcpv6RelayInterfaceListIfIndex,
       "rlDhcpv6RelayInterfaceListRowStatus": rlDhcpv6RelayInterfaceListRowStatus,
       "rlDhcpv6RelayDestinationsGlobalTable": rlDhcpv6RelayDestinationsGlobalTable,
       "rlDhcpv6RelayDestinationsGlobalEntry": rlDhcpv6RelayDestinationsGlobalEntry,
       "rlDhcpv6RelayDestinationsGlobalIpv6AddrType": rlDhcpv6RelayDestinationsGlobalIpv6AddrType,
       "rlDhcpv6RelayDestinationsGlobalIpv6Addr": rlDhcpv6RelayDestinationsGlobalIpv6Addr,
       "rlDhcpv6RelayDestinationsGlobalOutputInterface": rlDhcpv6RelayDestinationsGlobalOutputInterface,
       "rlDhcpv6RelayDestinationsGlobalRowStatus": rlDhcpv6RelayDestinationsGlobalRowStatus,
       "rlDhcpv6RelayInterfaceDestinationsTable": rlDhcpv6RelayInterfaceDestinationsTable,
       "rlDhcpv6RelayInterfaceDestinationsEntry": rlDhcpv6RelayInterfaceDestinationsEntry,
       "rlDhcpv6RelayInterfaceDestinationsIfindex": rlDhcpv6RelayInterfaceDestinationsIfindex,
       "rlDhcpv6RelayInterfaceDestinationsIpv6AddrType": rlDhcpv6RelayInterfaceDestinationsIpv6AddrType,
       "rlDhcpv6RelayInterfaceDestinationsIpv6Addr": rlDhcpv6RelayInterfaceDestinationsIpv6Addr,
       "rlDhcpv6RelayInterfaceDestinationsOutputInterface": rlDhcpv6RelayInterfaceDestinationsOutputInterface,
       "rlDhcpv6RelayInterfaceDestinationsRowStatus": rlDhcpv6RelayInterfaceDestinationsRowStatus}
)
