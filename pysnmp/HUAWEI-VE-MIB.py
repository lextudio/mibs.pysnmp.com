# SNMP MIB module (HUAWEI-VE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:23 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwVe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVirtualEthernetMibObjects_ObjectIdentity = ObjectIdentity
hwVirtualEthernetMibObjects = _HwVirtualEthernetMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1)
)
_HwVirtualEthernetTable_Object = MibTable
hwVirtualEthernetTable = _HwVirtualEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1)
)
if mibBuilder.loadTexts:
    hwVirtualEthernetTable.setStatus("current")
_HwVirtualEthernetEntry_Object = MibTableRow
hwVirtualEthernetEntry = _HwVirtualEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1)
)
hwVirtualEthernetEntry.setIndexNames(
    (0, "HUAWEI-VE-MIB", "hwVirtualEthernetGroupId"),
)
if mibBuilder.loadTexts:
    hwVirtualEthernetEntry.setStatus("current")
_HwVirtualEthernetGroupId_Type = Integer32
_HwVirtualEthernetGroupId_Object = MibTableColumn
hwVirtualEthernetGroupId = _HwVirtualEthernetGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 1),
    _HwVirtualEthernetGroupId_Type()
)
hwVirtualEthernetGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVirtualEthernetGroupId.setStatus("current")
_HwL2VirtualEthernetName_Type = DisplayString
_HwL2VirtualEthernetName_Object = MibTableColumn
hwL2VirtualEthernetName = _HwL2VirtualEthernetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 11),
    _HwL2VirtualEthernetName_Type()
)
hwL2VirtualEthernetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VirtualEthernetName.setStatus("current")
_HwL3VirtualEthernetName_Type = DisplayString
_HwL3VirtualEthernetName_Object = MibTableColumn
hwL3VirtualEthernetName = _HwL3VirtualEthernetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 12),
    _HwL3VirtualEthernetName_Type()
)
hwL3VirtualEthernetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL3VirtualEthernetName.setStatus("current")
_HwVirtualEthernetGroupRowStatus_Type = RowStatus
_HwVirtualEthernetGroupRowStatus_Object = MibTableColumn
hwVirtualEthernetGroupRowStatus = _HwVirtualEthernetGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 1, 1, 1, 51),
    _HwVirtualEthernetGroupRowStatus_Type()
)
hwVirtualEthernetGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVirtualEthernetGroupRowStatus.setStatus("current")
_HwVirtualEthernetConformance_ObjectIdentity = ObjectIdentity
hwVirtualEthernetConformance = _HwVirtualEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2)
)
_HwVirtualEthernetGroups_ObjectIdentity = ObjectIdentity
hwVirtualEthernetGroups = _HwVirtualEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 1)
)
_HwVirtualEthernetCompliances_ObjectIdentity = ObjectIdentity
hwVirtualEthernetCompliances = _HwVirtualEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 2)
)

# Managed Objects groups

hwVirtualEthernetObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 1, 1)
)
hwVirtualEthernetObjectGroup.setObjects(
      *(("HUAWEI-VE-MIB", "hwL2VirtualEthernetName"),
        ("HUAWEI-VE-MIB", "hwL3VirtualEthernetName"),
        ("HUAWEI-VE-MIB", "hwVirtualEthernetGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwVirtualEthernetObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwVirtualEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 146, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwVirtualEthernetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VE-MIB",
    **{"hwVe": hwVe,
       "hwVirtualEthernetMibObjects": hwVirtualEthernetMibObjects,
       "hwVirtualEthernetTable": hwVirtualEthernetTable,
       "hwVirtualEthernetEntry": hwVirtualEthernetEntry,
       "hwVirtualEthernetGroupId": hwVirtualEthernetGroupId,
       "hwL2VirtualEthernetName": hwL2VirtualEthernetName,
       "hwL3VirtualEthernetName": hwL3VirtualEthernetName,
       "hwVirtualEthernetGroupRowStatus": hwVirtualEthernetGroupRowStatus,
       "hwVirtualEthernetConformance": hwVirtualEthernetConformance,
       "hwVirtualEthernetGroups": hwVirtualEthernetGroups,
       "hwVirtualEthernetObjectGroup": hwVirtualEthernetObjectGroup,
       "hwVirtualEthernetCompliances": hwVirtualEthernetCompliances,
       "hwVirtualEthernetCompliance": hwVirtualEthernetCompliance}
)
