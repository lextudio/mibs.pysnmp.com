# SNMP MIB module (NLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:32 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swNlbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwNlbMgmt_ObjectIdentity = ObjectIdentity
swNlbMgmt = _SwNlbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3)
)
_SwNlbUnicastFdbTable_Object = MibTable
swNlbUnicastFdbTable = _SwNlbUnicastFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 1)
)
if mibBuilder.loadTexts:
    swNlbUnicastFdbTable.setStatus("current")
_SwNlbUnicastFdbEntry_Object = MibTableRow
swNlbUnicastFdbEntry = _SwNlbUnicastFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 1, 1)
)
swNlbUnicastFdbEntry.setIndexNames(
    (0, "NLB-MIB", "swNlbUnicastFdbMacAddress"),
)
if mibBuilder.loadTexts:
    swNlbUnicastFdbEntry.setStatus("current")
_SwNlbUnicastFdbMacAddress_Type = MacAddress
_SwNlbUnicastFdbMacAddress_Object = MibTableColumn
swNlbUnicastFdbMacAddress = _SwNlbUnicastFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 1, 1, 1),
    _SwNlbUnicastFdbMacAddress_Type()
)
swNlbUnicastFdbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swNlbUnicastFdbMacAddress.setStatus("current")
_SwNlbUnicastFdbEgressPorts_Type = PortList
_SwNlbUnicastFdbEgressPorts_Object = MibTableColumn
swNlbUnicastFdbEgressPorts = _SwNlbUnicastFdbEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 1, 1, 2),
    _SwNlbUnicastFdbEgressPorts_Type()
)
swNlbUnicastFdbEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swNlbUnicastFdbEgressPorts.setStatus("current")
_SwNlbUnicastFdbRowStatus_Type = RowStatus
_SwNlbUnicastFdbRowStatus_Object = MibTableColumn
swNlbUnicastFdbRowStatus = _SwNlbUnicastFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 1, 1, 3),
    _SwNlbUnicastFdbRowStatus_Type()
)
swNlbUnicastFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swNlbUnicastFdbRowStatus.setStatus("current")
_SwNlbMulticastFdbTable_Object = MibTable
swNlbMulticastFdbTable = _SwNlbMulticastFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2)
)
if mibBuilder.loadTexts:
    swNlbMulticastFdbTable.setStatus("current")
_SwNlbMulticastFdbEntry_Object = MibTableRow
swNlbMulticastFdbEntry = _SwNlbMulticastFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2, 1)
)
swNlbMulticastFdbEntry.setIndexNames(
    (0, "NLB-MIB", "swNlbMulticastFdbVlanIndex"),
    (0, "NLB-MIB", "swNlbMulticastFdbMacAddress"),
)
if mibBuilder.loadTexts:
    swNlbMulticastFdbEntry.setStatus("current")
_SwNlbMulticastFdbVlanIndex_Type = VlanIndex
_SwNlbMulticastFdbVlanIndex_Object = MibTableColumn
swNlbMulticastFdbVlanIndex = _SwNlbMulticastFdbVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2, 1, 1),
    _SwNlbMulticastFdbVlanIndex_Type()
)
swNlbMulticastFdbVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swNlbMulticastFdbVlanIndex.setStatus("current")
_SwNlbMulticastFdbMacAddress_Type = MacAddress
_SwNlbMulticastFdbMacAddress_Object = MibTableColumn
swNlbMulticastFdbMacAddress = _SwNlbMulticastFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2, 1, 2),
    _SwNlbMulticastFdbMacAddress_Type()
)
swNlbMulticastFdbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swNlbMulticastFdbMacAddress.setStatus("current")
_SwNlbMulticastFdbEgressPorts_Type = PortList
_SwNlbMulticastFdbEgressPorts_Object = MibTableColumn
swNlbMulticastFdbEgressPorts = _SwNlbMulticastFdbEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2, 1, 3),
    _SwNlbMulticastFdbEgressPorts_Type()
)
swNlbMulticastFdbEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swNlbMulticastFdbEgressPorts.setStatus("current")
_SwNlbMulticastFdbRowStatus_Type = RowStatus
_SwNlbMulticastFdbRowStatus_Object = MibTableColumn
swNlbMulticastFdbRowStatus = _SwNlbMulticastFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 77, 3, 2, 1, 4),
    _SwNlbMulticastFdbRowStatus_Type()
)
swNlbMulticastFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swNlbMulticastFdbRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NLB-MIB",
    **{"swNlbMIB": swNlbMIB,
       "swNlbMgmt": swNlbMgmt,
       "swNlbUnicastFdbTable": swNlbUnicastFdbTable,
       "swNlbUnicastFdbEntry": swNlbUnicastFdbEntry,
       "swNlbUnicastFdbMacAddress": swNlbUnicastFdbMacAddress,
       "swNlbUnicastFdbEgressPorts": swNlbUnicastFdbEgressPorts,
       "swNlbUnicastFdbRowStatus": swNlbUnicastFdbRowStatus,
       "swNlbMulticastFdbTable": swNlbMulticastFdbTable,
       "swNlbMulticastFdbEntry": swNlbMulticastFdbEntry,
       "swNlbMulticastFdbVlanIndex": swNlbMulticastFdbVlanIndex,
       "swNlbMulticastFdbMacAddress": swNlbMulticastFdbMacAddress,
       "swNlbMulticastFdbEgressPorts": swNlbMulticastFdbEgressPorts,
       "swNlbMulticastFdbRowStatus": swNlbMulticastFdbRowStatus}
)
