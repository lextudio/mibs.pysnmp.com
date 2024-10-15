# SNMP MIB module (CISCO-FLEX-LINKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLEX-LINKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:38 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFlexLinksMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471)
)
ciscoFlexLinksMIB.setRevisions(
        ("2010-02-04 00:00",
         "2005-04-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFlexLinksMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFlexLinksMIBNotifs = _CiscoFlexLinksMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 0)
)
_CiscoFlexLinksMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFlexLinksMIBObjects = _CiscoFlexLinksMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1)
)
_CflConfig_ObjectIdentity = ObjectIdentity
cflConfig = _CflConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1)
)
_CflIfConfigTable_Object = MibTable
cflIfConfigTable = _CflIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cflIfConfigTable.setStatus("current")
_CflIfConfigEntry_Object = MibTableRow
cflIfConfigEntry = _CflIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1)
)
cflIfConfigEntry.setIndexNames(
    (0, "CISCO-FLEX-LINKS-MIB", "cflIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    cflIfConfigEntry.setStatus("current")
_CflIfConfigPrimary_Type = InterfaceIndex
_CflIfConfigPrimary_Object = MibTableColumn
cflIfConfigPrimary = _CflIfConfigPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 1),
    _CflIfConfigPrimary_Type()
)
cflIfConfigPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cflIfConfigPrimary.setStatus("current")
_CflIfConfigBackUp_Type = InterfaceIndexOrZero
_CflIfConfigBackUp_Object = MibTableColumn
cflIfConfigBackUp = _CflIfConfigBackUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 2),
    _CflIfConfigBackUp_Type()
)
cflIfConfigBackUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cflIfConfigBackUp.setStatus("current")


class _CflIfConfigStorageType_Type(StorageType):
    """Custom type cflIfConfigStorageType based on StorageType"""


_CflIfConfigStorageType_Object = MibTableColumn
cflIfConfigStorageType = _CflIfConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 3),
    _CflIfConfigStorageType_Type()
)
cflIfConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cflIfConfigStorageType.setStatus("current")
_CflIfConfigStatus_Type = RowStatus
_CflIfConfigStatus_Object = MibTableColumn
cflIfConfigStatus = _CflIfConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 1, 1, 4),
    _CflIfConfigStatus_Type()
)
cflIfConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cflIfConfigStatus.setStatus("current")
_CflEnableStatusChangeNotif_Type = TruthValue
_CflEnableStatusChangeNotif_Object = MibScalar
cflEnableStatusChangeNotif = _CflEnableStatusChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 2),
    _CflEnableStatusChangeNotif_Type()
)
cflEnableStatusChangeNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflEnableStatusChangeNotif.setStatus("current")
_CflIfConfigExtTable_Object = MibTable
cflIfConfigExtTable = _CflIfConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cflIfConfigExtTable.setStatus("current")
_CflIfConfigExtEntry_Object = MibTableRow
cflIfConfigExtEntry = _CflIfConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1)
)
cflIfConfigExtEntry.setIndexNames(
    (0, "CISCO-FLEX-LINKS-MIB", "cflIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    cflIfConfigExtEntry.setStatus("current")
_CflIfConfigMmuPrimaryVlan_Type = VlanIdOrNone
_CflIfConfigMmuPrimaryVlan_Object = MibTableColumn
cflIfConfigMmuPrimaryVlan = _CflIfConfigMmuPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 1),
    _CflIfConfigMmuPrimaryVlan_Type()
)
cflIfConfigMmuPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflIfConfigMmuPrimaryVlan.setStatus("current")


class _CflIfConfigPreemptionMode_Type(Integer32):
    """Custom type cflIfConfigPreemptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 3),
          ("forced", 2),
          ("off", 1))
    )


_CflIfConfigPreemptionMode_Type.__name__ = "Integer32"
_CflIfConfigPreemptionMode_Object = MibTableColumn
cflIfConfigPreemptionMode = _CflIfConfigPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 2),
    _CflIfConfigPreemptionMode_Type()
)
cflIfConfigPreemptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflIfConfigPreemptionMode.setStatus("current")
_CflIfConfigPreemptionDelay_Type = Unsigned32
_CflIfConfigPreemptionDelay_Object = MibTableColumn
cflIfConfigPreemptionDelay = _CflIfConfigPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 3),
    _CflIfConfigPreemptionDelay_Type()
)
cflIfConfigPreemptionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflIfConfigPreemptionDelay.setStatus("current")
if mibBuilder.loadTexts:
    cflIfConfigPreemptionDelay.setUnits("seconds")
_CflIfConfigPrefer2kVlan_Type = Cisco2KVlanList
_CflIfConfigPrefer2kVlan_Object = MibTableColumn
cflIfConfigPrefer2kVlan = _CflIfConfigPrefer2kVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 4),
    _CflIfConfigPrefer2kVlan_Type()
)
cflIfConfigPrefer2kVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflIfConfigPrefer2kVlan.setStatus("current")
_CflIfConfigPrefer4kVlan_Type = Cisco2KVlanList
_CflIfConfigPrefer4kVlan_Object = MibTableColumn
cflIfConfigPrefer4kVlan = _CflIfConfigPrefer4kVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 1, 3, 1, 5),
    _CflIfConfigPrefer4kVlan_Type()
)
cflIfConfigPrefer4kVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cflIfConfigPrefer4kVlan.setStatus("current")
_CflStatus_ObjectIdentity = ObjectIdentity
cflStatus = _CflStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2)
)
_CflIfStatusTable_Object = MibTable
cflIfStatusTable = _CflIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cflIfStatusTable.setStatus("current")
_CflIfStatusEntry_Object = MibTableRow
cflIfStatusEntry = _CflIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1)
)
cflIfStatusEntry.setIndexNames(
    (0, "CISCO-FLEX-LINKS-MIB", "cflIfIndex"),
)
if mibBuilder.loadTexts:
    cflIfStatusEntry.setStatus("current")
_CflIfIndex_Type = InterfaceIndex
_CflIfIndex_Object = MibTableColumn
cflIfIndex = _CflIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1, 1),
    _CflIfIndex_Type()
)
cflIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cflIfIndex.setStatus("current")


class _CflIfStatus_Type(Integer32):
    """Custom type cflIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("down", 3),
          ("forwarding", 1),
          ("unknown", 6),
          ("vlbAll", 7),
          ("vlbConfig", 8),
          ("vlbPreempt", 9),
          ("waitingForPeerStrate", 5),
          ("waitingToSync", 4))
    )


_CflIfStatus_Type.__name__ = "Integer32"
_CflIfStatus_Object = MibTableColumn
cflIfStatus = _CflIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 1, 2, 1, 1, 2),
    _CflIfStatus_Type()
)
cflIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cflIfStatus.setStatus("current")
_CiscoFlexLinksMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFlexLinksMIBConformance = _CiscoFlexLinksMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2)
)
_CiscoFlexLinksMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFlexLinksMIBCompliances = _CiscoFlexLinksMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1)
)
_CiscoFlexLinksMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFlexLinksMIBGroups = _CiscoFlexLinksMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2)
)

# Managed Objects groups

ciscoFlexLinksIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 1)
)
ciscoFlexLinksIfConfigGroup.setObjects(
      *(("CISCO-FLEX-LINKS-MIB", "cflIfConfigBackUp"),
        ("CISCO-FLEX-LINKS-MIB", "cflIfConfigStorageType"),
        ("CISCO-FLEX-LINKS-MIB", "cflIfConfigStatus"))
)
if mibBuilder.loadTexts:
    ciscoFlexLinksIfConfigGroup.setStatus("current")

ciscoFlexLinksIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 2)
)
ciscoFlexLinksIfStatusGroup.setObjects(
    ("CISCO-FLEX-LINKS-MIB", "cflIfStatus")
)
if mibBuilder.loadTexts:
    ciscoFlexLinksIfStatusGroup.setStatus("current")

ciscoFlexLinksEnableNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 3)
)
ciscoFlexLinksEnableNotifGroup.setObjects(
    ("CISCO-FLEX-LINKS-MIB", "cflEnableStatusChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoFlexLinksEnableNotifGroup.setStatus("current")

ciscoFlexLinksMmuPrimaryVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 5)
)
ciscoFlexLinksMmuPrimaryVlanGroup.setObjects(
    ("CISCO-FLEX-LINKS-MIB", "cflIfConfigMmuPrimaryVlan")
)
if mibBuilder.loadTexts:
    ciscoFlexLinksMmuPrimaryVlanGroup.setStatus("current")

ciscoFlexLinksPreemptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 6)
)
ciscoFlexLinksPreemptionGroup.setObjects(
      *(("CISCO-FLEX-LINKS-MIB", "cflIfConfigPreemptionMode"),
        ("CISCO-FLEX-LINKS-MIB", "cflIfConfigPreemptionDelay"))
)
if mibBuilder.loadTexts:
    ciscoFlexLinksPreemptionGroup.setStatus("current")

ciscoFlexLinksPreferVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 7)
)
ciscoFlexLinksPreferVlanGroup.setObjects(
      *(("CISCO-FLEX-LINKS-MIB", "cflIfConfigPrefer2kVlan"),
        ("CISCO-FLEX-LINKS-MIB", "cflIfConfigPrefer4kVlan"))
)
if mibBuilder.loadTexts:
    ciscoFlexLinksPreferVlanGroup.setStatus("current")


# Notification objects

cflIfStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 0, 1)
)
cflIfStatusChangeNotif.setObjects(
    ("CISCO-FLEX-LINKS-MIB", "cflIfStatus")
)
if mibBuilder.loadTexts:
    cflIfStatusChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoFlexLinksNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 2, 4)
)
ciscoFlexLinksNotifGroup.setObjects(
    ("CISCO-FLEX-LINKS-MIB", "cflIfStatusChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoFlexLinksNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFlexLinksMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFlexLinksMIBCompliance.setStatus(
        "deprecated"
    )

ciscoFlexLinksMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 471, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFlexLinksMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLEX-LINKS-MIB",
    **{"ciscoFlexLinksMIB": ciscoFlexLinksMIB,
       "ciscoFlexLinksMIBNotifs": ciscoFlexLinksMIBNotifs,
       "cflIfStatusChangeNotif": cflIfStatusChangeNotif,
       "ciscoFlexLinksMIBObjects": ciscoFlexLinksMIBObjects,
       "cflConfig": cflConfig,
       "cflIfConfigTable": cflIfConfigTable,
       "cflIfConfigEntry": cflIfConfigEntry,
       "cflIfConfigPrimary": cflIfConfigPrimary,
       "cflIfConfigBackUp": cflIfConfigBackUp,
       "cflIfConfigStorageType": cflIfConfigStorageType,
       "cflIfConfigStatus": cflIfConfigStatus,
       "cflEnableStatusChangeNotif": cflEnableStatusChangeNotif,
       "cflIfConfigExtTable": cflIfConfigExtTable,
       "cflIfConfigExtEntry": cflIfConfigExtEntry,
       "cflIfConfigMmuPrimaryVlan": cflIfConfigMmuPrimaryVlan,
       "cflIfConfigPreemptionMode": cflIfConfigPreemptionMode,
       "cflIfConfigPreemptionDelay": cflIfConfigPreemptionDelay,
       "cflIfConfigPrefer2kVlan": cflIfConfigPrefer2kVlan,
       "cflIfConfigPrefer4kVlan": cflIfConfigPrefer4kVlan,
       "cflStatus": cflStatus,
       "cflIfStatusTable": cflIfStatusTable,
       "cflIfStatusEntry": cflIfStatusEntry,
       "cflIfIndex": cflIfIndex,
       "cflIfStatus": cflIfStatus,
       "ciscoFlexLinksMIBConformance": ciscoFlexLinksMIBConformance,
       "ciscoFlexLinksMIBCompliances": ciscoFlexLinksMIBCompliances,
       "ciscoFlexLinksMIBCompliance": ciscoFlexLinksMIBCompliance,
       "ciscoFlexLinksMIBCompliance2": ciscoFlexLinksMIBCompliance2,
       "ciscoFlexLinksMIBGroups": ciscoFlexLinksMIBGroups,
       "ciscoFlexLinksIfConfigGroup": ciscoFlexLinksIfConfigGroup,
       "ciscoFlexLinksIfStatusGroup": ciscoFlexLinksIfStatusGroup,
       "ciscoFlexLinksEnableNotifGroup": ciscoFlexLinksEnableNotifGroup,
       "ciscoFlexLinksNotifGroup": ciscoFlexLinksNotifGroup,
       "ciscoFlexLinksMmuPrimaryVlanGroup": ciscoFlexLinksMmuPrimaryVlanGroup,
       "ciscoFlexLinksPreemptionGroup": ciscoFlexLinksPreemptionGroup,
       "ciscoFlexLinksPreferVlanGroup": ciscoFlexLinksPreferVlanGroup}
)
