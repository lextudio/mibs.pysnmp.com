# SNMP MIB module (AVICI-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:42 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysInventoryId,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysInventoryId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aviciMemoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6)
)
aviciMemoryMIB.setRevisions(
        ("0009-07-12 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciMemoryObjects_ObjectIdentity = ObjectIdentity
aviciMemoryObjects = _AviciMemoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1)
)
_AviciPlatformMemoryTable_Object = MibTable
aviciPlatformMemoryTable = _AviciPlatformMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    aviciPlatformMemoryTable.setStatus("current")
_AviciPlatformMemoryEntry_Object = MibTableRow
aviciPlatformMemoryEntry = _AviciPlatformMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1)
)
aviciPlatformMemoryEntry.setIndexNames(
    (0, "AVICI-SYSTEM-MIB", "aviciSysInventoryId"),
)
if mibBuilder.loadTexts:
    aviciPlatformMemoryEntry.setStatus("current")
_AviciPlatformMemoryTotal_Type = Unsigned32
_AviciPlatformMemoryTotal_Object = MibTableColumn
aviciPlatformMemoryTotal = _AviciPlatformMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 1),
    _AviciPlatformMemoryTotal_Type()
)
aviciPlatformMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryTotal.setStatus("current")
_AviciPlatformMemoryUsed_Type = Unsigned32
_AviciPlatformMemoryUsed_Object = MibTableColumn
aviciPlatformMemoryUsed = _AviciPlatformMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 2),
    _AviciPlatformMemoryUsed_Type()
)
aviciPlatformMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryUsed.setStatus("current")
_AviciPlatformMemoryFree_Type = Unsigned32
_AviciPlatformMemoryFree_Object = MibTableColumn
aviciPlatformMemoryFree = _AviciPlatformMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 3),
    _AviciPlatformMemoryFree_Type()
)
aviciPlatformMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryFree.setStatus("current")
_AviciPlatformMemoryFreePages_Type = Unsigned32
_AviciPlatformMemoryFreePages_Object = MibTableColumn
aviciPlatformMemoryFreePages = _AviciPlatformMemoryFreePages_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 4),
    _AviciPlatformMemoryFreePages_Type()
)
aviciPlatformMemoryFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryFreePages.setStatus("current")
_AviciPlatformMemoryPageSize_Type = Unsigned32
_AviciPlatformMemoryPageSize_Object = MibTableColumn
aviciPlatformMemoryPageSize = _AviciPlatformMemoryPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 5),
    _AviciPlatformMemoryPageSize_Type()
)
aviciPlatformMemoryPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryPageSize.setStatus("current")
_AviciPlatformMemoryLargestFree_Type = Unsigned32
_AviciPlatformMemoryLargestFree_Object = MibTableColumn
aviciPlatformMemoryLargestFree = _AviciPlatformMemoryLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 1, 1, 1, 6),
    _AviciPlatformMemoryLargestFree_Type()
)
aviciPlatformMemoryLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciPlatformMemoryLargestFree.setStatus("current")
_AviciMemoryMIBConformance_ObjectIdentity = ObjectIdentity
aviciMemoryMIBConformance = _AviciMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 2)
)
_AviciMemoryMIBCompliances_ObjectIdentity = ObjectIdentity
aviciMemoryMIBCompliances = _AviciMemoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 2, 1)
)
_AviciMemoryMIBGroups_ObjectIdentity = ObjectIdentity
aviciMemoryMIBGroups = _AviciMemoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 2, 2)
)

# Managed Objects groups

aviciMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 2, 2, 1)
)
aviciMemoryGroup.setObjects(
      *(("AVICI-MEMORY-MIB", "aviciPlatformMemoryTotal"),
        ("AVICI-MEMORY-MIB", "aviciPlatformMemoryUsed"),
        ("AVICI-MEMORY-MIB", "aviciPlatformMemoryFree"),
        ("AVICI-MEMORY-MIB", "aviciPlatformMemoryFreePages"),
        ("AVICI-MEMORY-MIB", "aviciPlatformMemoryPageSize"),
        ("AVICI-MEMORY-MIB", "aviciPlatformMemoryLargestFree"))
)
if mibBuilder.loadTexts:
    aviciMemoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviciMemoryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aviciMemoryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-MEMORY-MIB",
    **{"aviciMemoryMIB": aviciMemoryMIB,
       "aviciMemoryObjects": aviciMemoryObjects,
       "aviciPlatformMemoryTable": aviciPlatformMemoryTable,
       "aviciPlatformMemoryEntry": aviciPlatformMemoryEntry,
       "aviciPlatformMemoryTotal": aviciPlatformMemoryTotal,
       "aviciPlatformMemoryUsed": aviciPlatformMemoryUsed,
       "aviciPlatformMemoryFree": aviciPlatformMemoryFree,
       "aviciPlatformMemoryFreePages": aviciPlatformMemoryFreePages,
       "aviciPlatformMemoryPageSize": aviciPlatformMemoryPageSize,
       "aviciPlatformMemoryLargestFree": aviciPlatformMemoryLargestFree,
       "aviciMemoryMIBConformance": aviciMemoryMIBConformance,
       "aviciMemoryMIBCompliances": aviciMemoryMIBCompliances,
       "aviciMemoryMIBCompliance": aviciMemoryMIBCompliance,
       "aviciMemoryMIBGroups": aviciMemoryMIBGroups,
       "aviciMemoryGroup": aviciMemoryGroup}
)
