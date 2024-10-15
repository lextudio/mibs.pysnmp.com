# SNMP MIB module (MY-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:22 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myMemoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35)
)
myMemoryMIB.setRevisions(
        ("2003-10-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_MyMemoryPoolMIBObjects_ObjectIdentity = ObjectIdentity
myMemoryPoolMIBObjects = _MyMemoryPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1)
)
_MyMemoryPoolUtilizationTable_Object = MibTable
myMemoryPoolUtilizationTable = _MyMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    myMemoryPoolUtilizationTable.setStatus("current")
_MyMemoryPoolUtilizationEntry_Object = MibTableRow
myMemoryPoolUtilizationEntry = _MyMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1)
)
myMemoryPoolUtilizationEntry.setIndexNames(
    (0, "MY-MEMORY-MIB", "myMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    myMemoryPoolUtilizationEntry.setStatus("current")
_MyMemoryPoolIndex_Type = Integer32
_MyMemoryPoolIndex_Object = MibTableColumn
myMemoryPoolIndex = _MyMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 1),
    _MyMemoryPoolIndex_Type()
)
myMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolIndex.setStatus("current")
_MyMemoryPoolName_Type = DisplayString
_MyMemoryPoolName_Object = MibTableColumn
myMemoryPoolName = _MyMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 2),
    _MyMemoryPoolName_Type()
)
myMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolName.setStatus("current")
_MyMemoryPoolCurrentUtilization_Type = Percent
_MyMemoryPoolCurrentUtilization_Object = MibTableColumn
myMemoryPoolCurrentUtilization = _MyMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 3),
    _MyMemoryPoolCurrentUtilization_Type()
)
myMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolCurrentUtilization.setStatus("current")
_MyMemoryPoolLowestUtilization_Type = Percent
_MyMemoryPoolLowestUtilization_Object = MibTableColumn
myMemoryPoolLowestUtilization = _MyMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 4),
    _MyMemoryPoolLowestUtilization_Type()
)
myMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolLowestUtilization.setStatus("current")
_MyMemoryPoolLargestUtilization_Type = Percent
_MyMemoryPoolLargestUtilization_Object = MibTableColumn
myMemoryPoolLargestUtilization = _MyMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 5),
    _MyMemoryPoolLargestUtilization_Type()
)
myMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolLargestUtilization.setStatus("current")
_MyMemoryPoolSize_Type = Integer32
_MyMemoryPoolSize_Object = MibTableColumn
myMemoryPoolSize = _MyMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 6),
    _MyMemoryPoolSize_Type()
)
myMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolSize.setStatus("current")
_MyMemoryPoolUsed_Type = Integer32
_MyMemoryPoolUsed_Object = MibTableColumn
myMemoryPoolUsed = _MyMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 7),
    _MyMemoryPoolUsed_Type()
)
myMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolUsed.setStatus("current")
_MyMemoryPoolFree_Type = Integer32
_MyMemoryPoolFree_Object = MibTableColumn
myMemoryPoolFree = _MyMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 8),
    _MyMemoryPoolFree_Type()
)
myMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myMemoryPoolFree.setStatus("current")
_MyMemoryPoolWarning_Type = Percent
_MyMemoryPoolWarning_Object = MibTableColumn
myMemoryPoolWarning = _MyMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 9),
    _MyMemoryPoolWarning_Type()
)
myMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMemoryPoolWarning.setStatus("current")
_MyMemoryPoolCritical_Type = Percent
_MyMemoryPoolCritical_Object = MibTableColumn
myMemoryPoolCritical = _MyMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 1, 1, 10),
    _MyMemoryPoolCritical_Type()
)
myMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myMemoryPoolCritical.setStatus("current")
_MyNodeMemoryPoolTable_Object = MibTable
myNodeMemoryPoolTable = _MyNodeMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    myNodeMemoryPoolTable.setStatus("current")
_MyNodeMemoryPoolEntry_Object = MibTableRow
myNodeMemoryPoolEntry = _MyNodeMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1)
)
myNodeMemoryPoolEntry.setIndexNames(
    (0, "MY-MEMORY-MIB", "myNodeMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    myNodeMemoryPoolEntry.setStatus("current")
_MyNodeMemoryPoolIndex_Type = Integer32
_MyNodeMemoryPoolIndex_Object = MibTableColumn
myNodeMemoryPoolIndex = _MyNodeMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 1),
    _MyNodeMemoryPoolIndex_Type()
)
myNodeMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolIndex.setStatus("current")
_MyNodeMemoryPoolName_Type = DisplayString
_MyNodeMemoryPoolName_Object = MibTableColumn
myNodeMemoryPoolName = _MyNodeMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 2),
    _MyNodeMemoryPoolName_Type()
)
myNodeMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolName.setStatus("current")
_MyNodeMemoryPoolCurrentUtilization_Type = Percent
_MyNodeMemoryPoolCurrentUtilization_Object = MibTableColumn
myNodeMemoryPoolCurrentUtilization = _MyNodeMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 3),
    _MyNodeMemoryPoolCurrentUtilization_Type()
)
myNodeMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolCurrentUtilization.setStatus("current")
_MyNodeMemoryPoolLowestUtilization_Type = Percent
_MyNodeMemoryPoolLowestUtilization_Object = MibTableColumn
myNodeMemoryPoolLowestUtilization = _MyNodeMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 4),
    _MyNodeMemoryPoolLowestUtilization_Type()
)
myNodeMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolLowestUtilization.setStatus("current")
_MyNodeMemoryPoolLargestUtilization_Type = Percent
_MyNodeMemoryPoolLargestUtilization_Object = MibTableColumn
myNodeMemoryPoolLargestUtilization = _MyNodeMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 5),
    _MyNodeMemoryPoolLargestUtilization_Type()
)
myNodeMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolLargestUtilization.setStatus("current")
_MyNodeMemoryPoolSize_Type = Integer32
_MyNodeMemoryPoolSize_Object = MibTableColumn
myNodeMemoryPoolSize = _MyNodeMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 6),
    _MyNodeMemoryPoolSize_Type()
)
myNodeMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolSize.setStatus("current")
_MyNodeMemoryPoolUsed_Type = Integer32
_MyNodeMemoryPoolUsed_Object = MibTableColumn
myNodeMemoryPoolUsed = _MyNodeMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 7),
    _MyNodeMemoryPoolUsed_Type()
)
myNodeMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolUsed.setStatus("current")
_MyNodeMemoryPoolFree_Type = Integer32
_MyNodeMemoryPoolFree_Object = MibTableColumn
myNodeMemoryPoolFree = _MyNodeMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 8),
    _MyNodeMemoryPoolFree_Type()
)
myNodeMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myNodeMemoryPoolFree.setStatus("current")
_MyNodeMemoryPoolWarning_Type = Percent
_MyNodeMemoryPoolWarning_Object = MibTableColumn
myNodeMemoryPoolWarning = _MyNodeMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 9),
    _MyNodeMemoryPoolWarning_Type()
)
myNodeMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myNodeMemoryPoolWarning.setStatus("current")
_MyNodeMemoryPoolCritical_Type = Percent
_MyNodeMemoryPoolCritical_Object = MibTableColumn
myNodeMemoryPoolCritical = _MyNodeMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 1, 2, 1, 10),
    _MyNodeMemoryPoolCritical_Type()
)
myNodeMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myNodeMemoryPoolCritical.setStatus("current")
_MyMemoryMIBConformance_ObjectIdentity = ObjectIdentity
myMemoryMIBConformance = _MyMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2)
)
_MyMemoryMIBCompliances_ObjectIdentity = ObjectIdentity
myMemoryMIBCompliances = _MyMemoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1)
)
_MyMemoryMIBGroups_ObjectIdentity = ObjectIdentity
myMemoryMIBGroups = _MyMemoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2)
)

# Managed Objects groups

myMemoryPoolUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 1)
)
myMemoryPoolUtilizationMIBGroup.setObjects(
      *(("MY-MEMORY-MIB", "myMemoryPoolIndex"),
        ("MY-MEMORY-MIB", "myMemoryPoolName"),
        ("MY-MEMORY-MIB", "myMemoryPoolCurrentUtilization"),
        ("MY-MEMORY-MIB", "myMemoryPoolLowestUtilization"),
        ("MY-MEMORY-MIB", "myMemoryPoolLargestUtilization"),
        ("MY-MEMORY-MIB", "myMemoryPoolSize"),
        ("MY-MEMORY-MIB", "myMemoryPoolUsed"),
        ("MY-MEMORY-MIB", "myMemoryPoolFree"),
        ("MY-MEMORY-MIB", "myMemoryPoolWarning"),
        ("MY-MEMORY-MIB", "myMemoryPoolCritical"))
)
if mibBuilder.loadTexts:
    myMemoryPoolUtilizationMIBGroup.setStatus("current")

myNodeMemoryPoolMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 2, 2)
)
myNodeMemoryPoolMIBGroup.setObjects(
      *(("MY-MEMORY-MIB", "myNodeMemoryPoolIndex"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolName"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolCurrentUtilization"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolLowestUtilization"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolLargestUtilization"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolSize"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolUsed"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolFree"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolWarning"),
        ("MY-MEMORY-MIB", "myNodeMemoryPoolCritical"))
)
if mibBuilder.loadTexts:
    myNodeMemoryPoolMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myMemoryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 35, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myMemoryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-MEMORY-MIB",
    **{"Percent": Percent,
       "myMemoryMIB": myMemoryMIB,
       "myMemoryPoolMIBObjects": myMemoryPoolMIBObjects,
       "myMemoryPoolUtilizationTable": myMemoryPoolUtilizationTable,
       "myMemoryPoolUtilizationEntry": myMemoryPoolUtilizationEntry,
       "myMemoryPoolIndex": myMemoryPoolIndex,
       "myMemoryPoolName": myMemoryPoolName,
       "myMemoryPoolCurrentUtilization": myMemoryPoolCurrentUtilization,
       "myMemoryPoolLowestUtilization": myMemoryPoolLowestUtilization,
       "myMemoryPoolLargestUtilization": myMemoryPoolLargestUtilization,
       "myMemoryPoolSize": myMemoryPoolSize,
       "myMemoryPoolUsed": myMemoryPoolUsed,
       "myMemoryPoolFree": myMemoryPoolFree,
       "myMemoryPoolWarning": myMemoryPoolWarning,
       "myMemoryPoolCritical": myMemoryPoolCritical,
       "myNodeMemoryPoolTable": myNodeMemoryPoolTable,
       "myNodeMemoryPoolEntry": myNodeMemoryPoolEntry,
       "myNodeMemoryPoolIndex": myNodeMemoryPoolIndex,
       "myNodeMemoryPoolName": myNodeMemoryPoolName,
       "myNodeMemoryPoolCurrentUtilization": myNodeMemoryPoolCurrentUtilization,
       "myNodeMemoryPoolLowestUtilization": myNodeMemoryPoolLowestUtilization,
       "myNodeMemoryPoolLargestUtilization": myNodeMemoryPoolLargestUtilization,
       "myNodeMemoryPoolSize": myNodeMemoryPoolSize,
       "myNodeMemoryPoolUsed": myNodeMemoryPoolUsed,
       "myNodeMemoryPoolFree": myNodeMemoryPoolFree,
       "myNodeMemoryPoolWarning": myNodeMemoryPoolWarning,
       "myNodeMemoryPoolCritical": myNodeMemoryPoolCritical,
       "myMemoryMIBConformance": myMemoryMIBConformance,
       "myMemoryMIBCompliances": myMemoryMIBCompliances,
       "myMemoryMIBCompliance": myMemoryMIBCompliance,
       "myMemoryMIBGroups": myMemoryMIBGroups,
       "myMemoryPoolUtilizationMIBGroup": myMemoryPoolUtilizationMIBGroup,
       "myNodeMemoryPoolMIBGroup": myNodeMemoryPoolMIBGroup}
)
