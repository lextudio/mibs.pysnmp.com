# SNMP MIB module (CISCO-IETF-DOT11-QOS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-DOT11-QOS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:31 2024
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

(Cid11QosTrafficCategory,
 cid11TrafficCategory,
 cid11TrafficPriority) = mibBuilder.importSymbols(
    "CISCO-IETF-DOT11-QOS-MIB",
    "Cid11QosTrafficCategory",
    "cid11TrafficCategory",
    "cid11TrafficPriority")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(cwvlWlanVlanEntry,) = mibBuilder.importSymbols(
    "CISCO-WLAN-VLAN-MIB",
    "cwvlWlanVlanEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoIetfDot11QosExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90)
)
ciscoIetfDot11QosExtMIB.setRevisions(
        ("2002-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIetfDot11QosExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosExtMIBNotifs = _CiscoIetfDot11QosExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 0)
)
_CiscoIetfDot11QosExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosExtMIBObjects = _CiscoIetfDot11QosExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1)
)
_Cid11QosExtConfig_ObjectIdentity = ObjectIdentity
cid11QosExtConfig = _Cid11QosExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1)
)
_Cid11QosExtConfigTable_Object = MibTable
cid11QosExtConfigTable = _Cid11QosExtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cid11QosExtConfigTable.setStatus("current")
_Cid11QosExtConfigEntry_Object = MibTableRow
cid11QosExtConfigEntry = _Cid11QosExtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 1, 1)
)
cid11QosExtConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficCategory"),
)
if mibBuilder.loadTexts:
    cid11QosExtConfigEntry.setStatus("current")


class _Cid11QosExtBackoffOffset_Type(Unsigned32):
    """Custom type cid11QosExtBackoffOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Cid11QosExtBackoffOffset_Type.__name__ = "Unsigned32"
_Cid11QosExtBackoffOffset_Object = MibTableColumn
cid11QosExtBackoffOffset = _Cid11QosExtBackoffOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 1, 1, 1),
    _Cid11QosExtBackoffOffset_Type()
)
cid11QosExtBackoffOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11QosExtBackoffOffset.setStatus("current")


class _Cid11QosExtMaxRetry_Type(Unsigned32):
    """Custom type cid11QosExtMaxRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cid11QosExtMaxRetry_Type.__name__ = "Unsigned32"
_Cid11QosExtMaxRetry_Object = MibTableColumn
cid11QosExtMaxRetry = _Cid11QosExtMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 1, 1, 2),
    _Cid11QosExtMaxRetry_Type()
)
cid11QosExtMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11QosExtMaxRetry.setStatus("current")
_Cid11QosExtIfConfigTable_Object = MibTable
cid11QosExtIfConfigTable = _Cid11QosExtIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cid11QosExtIfConfigTable.setStatus("current")
_Cid11QosExtIfConfigEntry_Object = MibTableRow
cid11QosExtIfConfigEntry = _Cid11QosExtIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 2, 1)
)
cid11QosExtIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cid11QosExtIfConfigEntry.setStatus("current")
_Cid11QosExtOptionEnabled_Type = TruthValue
_Cid11QosExtOptionEnabled_Object = MibTableColumn
cid11QosExtOptionEnabled = _Cid11QosExtOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 2, 1, 1),
    _Cid11QosExtOptionEnabled_Type()
)
cid11QosExtOptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosExtOptionEnabled.setStatus("current")
_Cid11QosExtVlanTable_Object = MibTable
cid11QosExtVlanTable = _Cid11QosExtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cid11QosExtVlanTable.setStatus("current")
_Cid11QosExtVlanEntry_Object = MibTableRow
cid11QosExtVlanEntry = _Cid11QosExtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cid11QosExtVlanEntry.setStatus("current")


class _Cid11QosExtVlanClassOfService_Type(Cid11QosTrafficCategory):
    """Custom type cid11QosExtVlanClassOfService based on Cid11QosTrafficCategory"""


_Cid11QosExtVlanClassOfService_Object = MibTableColumn
cid11QosExtVlanClassOfService = _Cid11QosExtVlanClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 1, 3, 1, 1),
    _Cid11QosExtVlanClassOfService_Type()
)
cid11QosExtVlanClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cid11QosExtVlanClassOfService.setStatus("current")
_Cid11QosExtQueue_ObjectIdentity = ObjectIdentity
cid11QosExtQueue = _Cid11QosExtQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 2)
)
_Cid11QosExtQueueTable_Object = MibTable
cid11QosExtQueueTable = _Cid11QosExtQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cid11QosExtQueueTable.setStatus("current")
_Cid11QosExtQueueEntry_Object = MibTableRow
cid11QosExtQueueEntry = _Cid11QosExtQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 2, 1, 1)
)
cid11QosExtQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficCategory"),
)
if mibBuilder.loadTexts:
    cid11QosExtQueueEntry.setStatus("current")


class _Cid11QosExtQueueQuota_Type(Unsigned32):
    """Custom type cid11QosExtQueueQuota based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Cid11QosExtQueueQuota_Type.__name__ = "Unsigned32"
_Cid11QosExtQueueQuota_Object = MibTableColumn
cid11QosExtQueueQuota = _Cid11QosExtQueueQuota_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 2, 1, 1, 1),
    _Cid11QosExtQueueQuota_Type()
)
cid11QosExtQueueQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid11QosExtQueueQuota.setStatus("current")
_Cid11QosExtNotifControl_ObjectIdentity = ObjectIdentity
cid11QosExtNotifControl = _Cid11QosExtNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 3)
)


class _Cid11QosExtNotifEnabled_Type(TruthValue):
    """Custom type cid11QosExtNotifEnabled based on TruthValue"""


_Cid11QosExtNotifEnabled_Object = MibScalar
cid11QosExtNotifEnabled = _Cid11QosExtNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 1, 3, 1),
    _Cid11QosExtNotifEnabled_Type()
)
cid11QosExtNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cid11QosExtNotifEnabled.setStatus("current")
_CiscoIetfDot11QosExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoIetfDot11QosExtMIBConform = _CiscoIetfDot11QosExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2)
)
_CiscoIetfD11QosExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIetfD11QosExtMIBCompliances = _CiscoIetfD11QosExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 1)
)
_CiscoIetfD11QosExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIetfD11QosExtMIBGroups = _CiscoIetfD11QosExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 2)
)
cwvlWlanVlanEntry.registerAugmentions(
    ("CISCO-IETF-DOT11-QOS-EXT-MIB",
     "cid11QosExtVlanEntry")
)
cid11QosExtVlanEntry.setIndexNames(*cwvlWlanVlanEntry.getIndexNames())

# Managed Objects groups

ciscoIetfD11QosExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 2, 1)
)
ciscoIetfD11QosExtConfigGroup.setObjects(
      *(("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtBackoffOffset"),
        ("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtMaxRetry"),
        ("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtOptionEnabled"),
        ("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtVlanClassOfService"))
)
if mibBuilder.loadTexts:
    ciscoIetfD11QosExtConfigGroup.setStatus("current")

ciscoIetfD11QosExtQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 2, 2)
)
ciscoIetfD11QosExtQueueGroup.setObjects(
    ("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtQueueQuota")
)
if mibBuilder.loadTexts:
    ciscoIetfD11QosExtQueueGroup.setStatus("current")

ciscoIetfD11QosExtNotifConGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 2, 3)
)
ciscoIetfD11QosExtNotifConGroup.setObjects(
    ("CISCO-IETF-DOT11-QOS-EXT-MIB", "cid11QosExtNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoIetfD11QosExtNotifConGroup.setStatus("current")


# Notification objects

ciscoIetfDot11QosExtChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 0, 1)
)
ciscoIetfDot11QosExtChangeNotif.setObjects(
    ("CISCO-IETF-DOT11-QOS-MIB", "cid11TrafficPriority")
)
if mibBuilder.loadTexts:
    ciscoIetfDot11QosExtChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoIetfD11QosExtNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 2, 4)
)
ciscoIetfD11QosExtNotifGroup.setObjects(
    ("CISCO-IETF-DOT11-QOS-EXT-MIB", "ciscoIetfDot11QosExtChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoIetfD11QosExtNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIetfD11QosExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 90, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIetfD11QosExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-DOT11-QOS-EXT-MIB",
    **{"ciscoIetfDot11QosExtMIB": ciscoIetfDot11QosExtMIB,
       "ciscoIetfDot11QosExtMIBNotifs": ciscoIetfDot11QosExtMIBNotifs,
       "ciscoIetfDot11QosExtChangeNotif": ciscoIetfDot11QosExtChangeNotif,
       "ciscoIetfDot11QosExtMIBObjects": ciscoIetfDot11QosExtMIBObjects,
       "cid11QosExtConfig": cid11QosExtConfig,
       "cid11QosExtConfigTable": cid11QosExtConfigTable,
       "cid11QosExtConfigEntry": cid11QosExtConfigEntry,
       "cid11QosExtBackoffOffset": cid11QosExtBackoffOffset,
       "cid11QosExtMaxRetry": cid11QosExtMaxRetry,
       "cid11QosExtIfConfigTable": cid11QosExtIfConfigTable,
       "cid11QosExtIfConfigEntry": cid11QosExtIfConfigEntry,
       "cid11QosExtOptionEnabled": cid11QosExtOptionEnabled,
       "cid11QosExtVlanTable": cid11QosExtVlanTable,
       "cid11QosExtVlanEntry": cid11QosExtVlanEntry,
       "cid11QosExtVlanClassOfService": cid11QosExtVlanClassOfService,
       "cid11QosExtQueue": cid11QosExtQueue,
       "cid11QosExtQueueTable": cid11QosExtQueueTable,
       "cid11QosExtQueueEntry": cid11QosExtQueueEntry,
       "cid11QosExtQueueQuota": cid11QosExtQueueQuota,
       "cid11QosExtNotifControl": cid11QosExtNotifControl,
       "cid11QosExtNotifEnabled": cid11QosExtNotifEnabled,
       "ciscoIetfDot11QosExtMIBConform": ciscoIetfDot11QosExtMIBConform,
       "ciscoIetfD11QosExtMIBCompliances": ciscoIetfD11QosExtMIBCompliances,
       "ciscoIetfD11QosExtMIBCompliance": ciscoIetfD11QosExtMIBCompliance,
       "ciscoIetfD11QosExtMIBGroups": ciscoIetfD11QosExtMIBGroups,
       "ciscoIetfD11QosExtConfigGroup": ciscoIetfD11QosExtConfigGroup,
       "ciscoIetfD11QosExtQueueGroup": ciscoIetfD11QosExtQueueGroup,
       "ciscoIetfD11QosExtNotifConGroup": ciscoIetfD11QosExtNotifConGroup,
       "ciscoIetfD11QosExtNotifGroup": ciscoIetfD11QosExtNotifGroup}
)
