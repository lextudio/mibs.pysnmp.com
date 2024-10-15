# SNMP MIB module (BDCOM-MEMORY-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-MEMORY-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:35 2024
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

(Percent,) = mibBuilder.importSymbols(
    "BDCOM-QOS-PIB-MIB",
    "Percent")

(bdMgmt,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bdcomMemoryPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48)
)
bdcomMemoryPoolMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BDCOMMemoryPoolTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_BdcomMemoryPoolObjects_ObjectIdentity = ObjectIdentity
bdcomMemoryPoolObjects = _BdcomMemoryPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1)
)
_BdcomMemoryPoolTable_Object = MibTable
bdcomMemoryPoolTable = _BdcomMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1)
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolTable.setStatus("current")
_BdcomMemoryPoolEntry_Object = MibTableRow
bdcomMemoryPoolEntry = _BdcomMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1)
)
bdcomMemoryPoolEntry.setIndexNames(
    (0, "BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolType"),
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolEntry.setStatus("current")
_BdcomMemoryPoolType_Type = BDCOMMemoryPoolTypes
_BdcomMemoryPoolType_Object = MibTableColumn
bdcomMemoryPoolType = _BdcomMemoryPoolType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 1),
    _BdcomMemoryPoolType_Type()
)
bdcomMemoryPoolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdcomMemoryPoolType.setStatus("current")
_BdcomMemoryPoolName_Type = DisplayString
_BdcomMemoryPoolName_Object = MibTableColumn
bdcomMemoryPoolName = _BdcomMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 2),
    _BdcomMemoryPoolName_Type()
)
bdcomMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolName.setStatus("current")


class _BdcomMemoryPoolAlternate_Type(Integer32):
    """Custom type bdcomMemoryPoolAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BdcomMemoryPoolAlternate_Type.__name__ = "Integer32"
_BdcomMemoryPoolAlternate_Object = MibTableColumn
bdcomMemoryPoolAlternate = _BdcomMemoryPoolAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 3),
    _BdcomMemoryPoolAlternate_Type()
)
bdcomMemoryPoolAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolAlternate.setStatus("current")
_BdcomMemoryPoolValid_Type = TruthValue
_BdcomMemoryPoolValid_Object = MibTableColumn
bdcomMemoryPoolValid = _BdcomMemoryPoolValid_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 4),
    _BdcomMemoryPoolValid_Type()
)
bdcomMemoryPoolValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolValid.setStatus("current")
_BdcomMemoryPoolUsed_Type = Gauge32
_BdcomMemoryPoolUsed_Object = MibTableColumn
bdcomMemoryPoolUsed = _BdcomMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 5),
    _BdcomMemoryPoolUsed_Type()
)
bdcomMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolUsed.setStatus("current")
if mibBuilder.loadTexts:
    bdcomMemoryPoolUsed.setUnits("bytes")
_BdcomMemoryPoolFree_Type = Gauge32
_BdcomMemoryPoolFree_Object = MibTableColumn
bdcomMemoryPoolFree = _BdcomMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 6),
    _BdcomMemoryPoolFree_Type()
)
bdcomMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolFree.setStatus("current")
if mibBuilder.loadTexts:
    bdcomMemoryPoolFree.setUnits("bytes")
_BdcomMemoryPoolLargestFree_Type = Gauge32
_BdcomMemoryPoolLargestFree_Object = MibTableColumn
bdcomMemoryPoolLargestFree = _BdcomMemoryPoolLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 7),
    _BdcomMemoryPoolLargestFree_Type()
)
bdcomMemoryPoolLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolLargestFree.setStatus("current")
if mibBuilder.loadTexts:
    bdcomMemoryPoolLargestFree.setUnits("bytes")
_BdcomMemoryPoolUtilizationTable_Object = MibTable
bdcomMemoryPoolUtilizationTable = _BdcomMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2)
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilizationTable.setStatus("current")
_BdcomMemoryPoolUtilizationEntry_Object = MibTableRow
bdcomMemoryPoolUtilizationEntry = _BdcomMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilizationEntry.setStatus("current")
_BdcomMemoryPoolUtilization1Min_Type = Percent
_BdcomMemoryPoolUtilization1Min_Object = MibTableColumn
bdcomMemoryPoolUtilization1Min = _BdcomMemoryPoolUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 1),
    _BdcomMemoryPoolUtilization1Min_Type()
)
bdcomMemoryPoolUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilization1Min.setStatus("current")
_BdcomMemoryPoolUtilization5Min_Type = Percent
_BdcomMemoryPoolUtilization5Min_Object = MibTableColumn
bdcomMemoryPoolUtilization5Min = _BdcomMemoryPoolUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 2),
    _BdcomMemoryPoolUtilization5Min_Type()
)
bdcomMemoryPoolUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilization5Min.setStatus("current")
_BdcomMemoryPoolUtilization10Min_Type = Percent
_BdcomMemoryPoolUtilization10Min_Object = MibTableColumn
bdcomMemoryPoolUtilization10Min = _BdcomMemoryPoolUtilization10Min_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 3),
    _BdcomMemoryPoolUtilization10Min_Type()
)
bdcomMemoryPoolUtilization10Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilization10Min.setStatus("current")
_BdcomMemoryPoolNotifications_ObjectIdentity = ObjectIdentity
bdcomMemoryPoolNotifications = _BdcomMemoryPoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 2)
)
_BdcomMemoryPoolConformance_ObjectIdentity = ObjectIdentity
bdcomMemoryPoolConformance = _BdcomMemoryPoolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3)
)
_BdcomMemoryPoolCompliances_ObjectIdentity = ObjectIdentity
bdcomMemoryPoolCompliances = _BdcomMemoryPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1)
)
_BdcomMemoryPoolGroups_ObjectIdentity = ObjectIdentity
bdcomMemoryPoolGroups = _BdcomMemoryPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2)
)
bdcomMemoryPoolEntry.registerAugmentions(
    ("BDCOM-MEMORY-POOL-MIB",
     "bdcomMemoryPoolUtilizationEntry")
)
bdcomMemoryPoolUtilizationEntry.setIndexNames(*bdcomMemoryPoolEntry.getIndexNames())

# Managed Objects groups

bdcomMemoryPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2, 1)
)
bdcomMemoryPoolGroup.setObjects(
      *(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolName"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolAlternate"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolValid"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUsed"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolFree"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolLargestFree"))
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolGroup.setStatus("current")

bdcomMemoryPoolUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2, 2)
)
bdcomMemoryPoolUtilizationGroup.setObjects(
      *(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization1Min"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization5Min"),
        ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization10Min"))
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolUtilizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bdcomMemoryPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolCompliance.setStatus(
        "deprecated"
    )

bdcomMemoryPoolComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1, 2)
)
if mibBuilder.loadTexts:
    bdcomMemoryPoolComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-MEMORY-POOL-MIB",
    **{"BDCOMMemoryPoolTypes": BDCOMMemoryPoolTypes,
       "bdcomMemoryPoolMIB": bdcomMemoryPoolMIB,
       "bdcomMemoryPoolObjects": bdcomMemoryPoolObjects,
       "bdcomMemoryPoolTable": bdcomMemoryPoolTable,
       "bdcomMemoryPoolEntry": bdcomMemoryPoolEntry,
       "bdcomMemoryPoolType": bdcomMemoryPoolType,
       "bdcomMemoryPoolName": bdcomMemoryPoolName,
       "bdcomMemoryPoolAlternate": bdcomMemoryPoolAlternate,
       "bdcomMemoryPoolValid": bdcomMemoryPoolValid,
       "bdcomMemoryPoolUsed": bdcomMemoryPoolUsed,
       "bdcomMemoryPoolFree": bdcomMemoryPoolFree,
       "bdcomMemoryPoolLargestFree": bdcomMemoryPoolLargestFree,
       "bdcomMemoryPoolUtilizationTable": bdcomMemoryPoolUtilizationTable,
       "bdcomMemoryPoolUtilizationEntry": bdcomMemoryPoolUtilizationEntry,
       "bdcomMemoryPoolUtilization1Min": bdcomMemoryPoolUtilization1Min,
       "bdcomMemoryPoolUtilization5Min": bdcomMemoryPoolUtilization5Min,
       "bdcomMemoryPoolUtilization10Min": bdcomMemoryPoolUtilization10Min,
       "bdcomMemoryPoolNotifications": bdcomMemoryPoolNotifications,
       "bdcomMemoryPoolConformance": bdcomMemoryPoolConformance,
       "bdcomMemoryPoolCompliances": bdcomMemoryPoolCompliances,
       "bdcomMemoryPoolCompliance": bdcomMemoryPoolCompliance,
       "bdcomMemoryPoolComplianceRev1": bdcomMemoryPoolComplianceRev1,
       "bdcomMemoryPoolGroups": bdcomMemoryPoolGroups,
       "bdcomMemoryPoolGroup": bdcomMemoryPoolGroup,
       "bdcomMemoryPoolUtilizationGroup": bdcomMemoryPoolUtilizationGroup}
)
