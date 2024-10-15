# SNMP MIB module (CISCO-MEMORY-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEMORY-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:27 2024
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
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoMemoryPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48)
)
ciscoMemoryPoolMIB.setRevisions(
        ("2013-09-18 00:00",
         "2001-07-31 00:00",
         "1996-02-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoMemoryPoolTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMemoryPoolObjects_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolObjects = _CiscoMemoryPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1)
)
_CiscoMemoryPoolTable_Object = MibTable
ciscoMemoryPoolTable = _CiscoMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolTable.setStatus("current")
_CiscoMemoryPoolEntry_Object = MibTableRow
ciscoMemoryPoolEntry = _CiscoMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1)
)
ciscoMemoryPoolEntry.setIndexNames(
    (0, "CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolType"),
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolEntry.setStatus("current")
_CiscoMemoryPoolType_Type = CiscoMemoryPoolTypes
_CiscoMemoryPoolType_Object = MibTableColumn
ciscoMemoryPoolType = _CiscoMemoryPoolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 1),
    _CiscoMemoryPoolType_Type()
)
ciscoMemoryPoolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoMemoryPoolType.setStatus("current")
_CiscoMemoryPoolName_Type = DisplayString
_CiscoMemoryPoolName_Object = MibTableColumn
ciscoMemoryPoolName = _CiscoMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 2),
    _CiscoMemoryPoolName_Type()
)
ciscoMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolName.setStatus("current")


class _CiscoMemoryPoolAlternate_Type(Integer32):
    """Custom type ciscoMemoryPoolAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoMemoryPoolAlternate_Type.__name__ = "Integer32"
_CiscoMemoryPoolAlternate_Object = MibTableColumn
ciscoMemoryPoolAlternate = _CiscoMemoryPoolAlternate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 3),
    _CiscoMemoryPoolAlternate_Type()
)
ciscoMemoryPoolAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolAlternate.setStatus("current")
_CiscoMemoryPoolValid_Type = TruthValue
_CiscoMemoryPoolValid_Object = MibTableColumn
ciscoMemoryPoolValid = _CiscoMemoryPoolValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 4),
    _CiscoMemoryPoolValid_Type()
)
ciscoMemoryPoolValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolValid.setStatus("current")
_CiscoMemoryPoolUsed_Type = Gauge32
_CiscoMemoryPoolUsed_Object = MibTableColumn
ciscoMemoryPoolUsed = _CiscoMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 5),
    _CiscoMemoryPoolUsed_Type()
)
ciscoMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolUsed.setStatus("current")
if mibBuilder.loadTexts:
    ciscoMemoryPoolUsed.setUnits("bytes")
_CiscoMemoryPoolFree_Type = Gauge32
_CiscoMemoryPoolFree_Object = MibTableColumn
ciscoMemoryPoolFree = _CiscoMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 6),
    _CiscoMemoryPoolFree_Type()
)
ciscoMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolFree.setStatus("current")
if mibBuilder.loadTexts:
    ciscoMemoryPoolFree.setUnits("bytes")
_CiscoMemoryPoolLargestFree_Type = Gauge32
_CiscoMemoryPoolLargestFree_Object = MibTableColumn
ciscoMemoryPoolLargestFree = _CiscoMemoryPoolLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 7),
    _CiscoMemoryPoolLargestFree_Type()
)
ciscoMemoryPoolLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolLargestFree.setStatus("current")
if mibBuilder.loadTexts:
    ciscoMemoryPoolLargestFree.setUnits("bytes")
_CiscoMemoryPoolLowMemoryNotifThreshold_Type = Percent
_CiscoMemoryPoolLowMemoryNotifThreshold_Object = MibTableColumn
ciscoMemoryPoolLowMemoryNotifThreshold = _CiscoMemoryPoolLowMemoryNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 8),
    _CiscoMemoryPoolLowMemoryNotifThreshold_Type()
)
ciscoMemoryPoolLowMemoryNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoMemoryPoolLowMemoryNotifThreshold.setStatus("current")
_CiscoMemoryPoolUtilizationTable_Object = MibTable
ciscoMemoryPoolUtilizationTable = _CiscoMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilizationTable.setStatus("current")
_CiscoMemoryPoolUtilizationEntry_Object = MibTableRow
ciscoMemoryPoolUtilizationEntry = _CiscoMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilizationEntry.setStatus("current")
_CiscoMemoryPoolUtilization1Min_Type = Percent
_CiscoMemoryPoolUtilization1Min_Object = MibTableColumn
ciscoMemoryPoolUtilization1Min = _CiscoMemoryPoolUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 1),
    _CiscoMemoryPoolUtilization1Min_Type()
)
ciscoMemoryPoolUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilization1Min.setStatus("current")
_CiscoMemoryPoolUtilization5Min_Type = Percent
_CiscoMemoryPoolUtilization5Min_Object = MibTableColumn
ciscoMemoryPoolUtilization5Min = _CiscoMemoryPoolUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 2),
    _CiscoMemoryPoolUtilization5Min_Type()
)
ciscoMemoryPoolUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilization5Min.setStatus("current")
_CiscoMemoryPoolUtilization10Min_Type = Percent
_CiscoMemoryPoolUtilization10Min_Object = MibTableColumn
ciscoMemoryPoolUtilization10Min = _CiscoMemoryPoolUtilization10Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 3),
    _CiscoMemoryPoolUtilization10Min_Type()
)
ciscoMemoryPoolUtilization10Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilization10Min.setStatus("current")
_CiscoMemoryPoolLowMemoryNotifEnable_Type = TruthValue
_CiscoMemoryPoolLowMemoryNotifEnable_Object = MibScalar
ciscoMemoryPoolLowMemoryNotifEnable = _CiscoMemoryPoolLowMemoryNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 3),
    _CiscoMemoryPoolLowMemoryNotifEnable_Type()
)
ciscoMemoryPoolLowMemoryNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoMemoryPoolLowMemoryNotifEnable.setStatus("current")
_CiscoMemoryPoolNotifications_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolNotifications = _CiscoMemoryPoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 2)
)
_CiscoMemoryPoolMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolMIBNotificationPrefix = _CiscoMemoryPoolMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0)
)
_CiscoMemoryPoolConformance_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolConformance = _CiscoMemoryPoolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3)
)
_CiscoMemoryPoolCompliances_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolCompliances = _CiscoMemoryPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1)
)
_CiscoMemoryPoolGroups_ObjectIdentity = ObjectIdentity
ciscoMemoryPoolGroups = _CiscoMemoryPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2)
)
ciscoMemoryPoolEntry.registerAugmentions(
    ("CISCO-MEMORY-POOL-MIB",
     "ciscoMemoryPoolUtilizationEntry")
)
ciscoMemoryPoolUtilizationEntry.setIndexNames(*ciscoMemoryPoolEntry.getIndexNames())

# Managed Objects groups

ciscoMemoryPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 1)
)
ciscoMemoryPoolGroup.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolGroup.setStatus("deprecated")

ciscoMemoryPoolUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 2)
)
ciscoMemoryPoolUtilizationGroup.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization1Min"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization5Min"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization10Min"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolUtilizationGroup.setStatus("current")

ciscoMemoryPoolNotificationCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 4)
)
ciscoMemoryPoolNotificationCtrlGroup.setObjects(
    ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolNotificationCtrlGroup.setStatus("current")

ciscoMemoryPoolGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 5)
)
ciscoMemoryPoolGroupRev1.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifThreshold"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolGroupRev1.setStatus("current")


# Notification objects

ciscoMemoryPoolLowMemoryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 1)
)
ciscoMemoryPoolLowMemoryNotif.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolLowMemoryNotif.setStatus(
        "current"
    )

ciscoMemoryPoolLowMemoryRecoveryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 2)
)
ciscoMemoryPoolLowMemoryRecoveryNotif.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolLowMemoryRecoveryNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoMemoryPoolNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 3)
)
ciscoMemoryPoolNotificationGroup.setObjects(
      *(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotif"),
        ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryRecoveryNotif"))
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoMemoryPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolCompliance.setStatus(
        "deprecated"
    )

ciscoMemoryPoolComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolComplianceRev1.setStatus(
        "deprecated"
    )

ciscoMemoryPoolComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoMemoryPoolComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEMORY-POOL-MIB",
    **{"CiscoMemoryPoolTypes": CiscoMemoryPoolTypes,
       "ciscoMemoryPoolMIB": ciscoMemoryPoolMIB,
       "ciscoMemoryPoolObjects": ciscoMemoryPoolObjects,
       "ciscoMemoryPoolTable": ciscoMemoryPoolTable,
       "ciscoMemoryPoolEntry": ciscoMemoryPoolEntry,
       "ciscoMemoryPoolType": ciscoMemoryPoolType,
       "ciscoMemoryPoolName": ciscoMemoryPoolName,
       "ciscoMemoryPoolAlternate": ciscoMemoryPoolAlternate,
       "ciscoMemoryPoolValid": ciscoMemoryPoolValid,
       "ciscoMemoryPoolUsed": ciscoMemoryPoolUsed,
       "ciscoMemoryPoolFree": ciscoMemoryPoolFree,
       "ciscoMemoryPoolLargestFree": ciscoMemoryPoolLargestFree,
       "ciscoMemoryPoolLowMemoryNotifThreshold": ciscoMemoryPoolLowMemoryNotifThreshold,
       "ciscoMemoryPoolUtilizationTable": ciscoMemoryPoolUtilizationTable,
       "ciscoMemoryPoolUtilizationEntry": ciscoMemoryPoolUtilizationEntry,
       "ciscoMemoryPoolUtilization1Min": ciscoMemoryPoolUtilization1Min,
       "ciscoMemoryPoolUtilization5Min": ciscoMemoryPoolUtilization5Min,
       "ciscoMemoryPoolUtilization10Min": ciscoMemoryPoolUtilization10Min,
       "ciscoMemoryPoolLowMemoryNotifEnable": ciscoMemoryPoolLowMemoryNotifEnable,
       "ciscoMemoryPoolNotifications": ciscoMemoryPoolNotifications,
       "ciscoMemoryPoolMIBNotificationPrefix": ciscoMemoryPoolMIBNotificationPrefix,
       "ciscoMemoryPoolLowMemoryNotif": ciscoMemoryPoolLowMemoryNotif,
       "ciscoMemoryPoolLowMemoryRecoveryNotif": ciscoMemoryPoolLowMemoryRecoveryNotif,
       "ciscoMemoryPoolConformance": ciscoMemoryPoolConformance,
       "ciscoMemoryPoolCompliances": ciscoMemoryPoolCompliances,
       "ciscoMemoryPoolCompliance": ciscoMemoryPoolCompliance,
       "ciscoMemoryPoolComplianceRev1": ciscoMemoryPoolComplianceRev1,
       "ciscoMemoryPoolComplianceRev2": ciscoMemoryPoolComplianceRev2,
       "ciscoMemoryPoolGroups": ciscoMemoryPoolGroups,
       "ciscoMemoryPoolGroup": ciscoMemoryPoolGroup,
       "ciscoMemoryPoolUtilizationGroup": ciscoMemoryPoolUtilizationGroup,
       "ciscoMemoryPoolNotificationGroup": ciscoMemoryPoolNotificationGroup,
       "ciscoMemoryPoolNotificationCtrlGroup": ciscoMemoryPoolNotificationCtrlGroup,
       "ciscoMemoryPoolGroupRev1": ciscoMemoryPoolGroupRev1}
)
