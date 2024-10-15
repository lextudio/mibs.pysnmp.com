# SNMP MIB module (CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:09 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoServiceControlSubscribersMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628)
)
ciscoServiceControlSubscribersMIB.setRevisions(
        ("2007-05-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoServiceControlSubscribersMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoServiceControlSubscribersMIBNotifs = _CiscoServiceControlSubscribersMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 0)
)
_CiscoServiceControlSubscribersMIBObjects_ObjectIdentity = ObjectIdentity
ciscoServiceControlSubscribersMIBObjects = _CiscoServiceControlSubscribersMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1)
)
_CServiceControlSubscribersTable_Object = MibTable
cServiceControlSubscribersTable = _CServiceControlSubscribersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1)
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersTable.setStatus("current")
_CServiceControlSubscribersEntry_Object = MibTableRow
cServiceControlSubscribersEntry = _CServiceControlSubscribersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1)
)
cServiceControlSubscribersEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersIndex"),
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersEntry.setStatus("current")


class _CServiceControlSubscribersIndex_Type(Unsigned32):
    """Custom type cServiceControlSubscribersIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CServiceControlSubscribersIndex_Type.__name__ = "Unsigned32"
_CServiceControlSubscribersIndex_Object = MibTableColumn
cServiceControlSubscribersIndex = _CServiceControlSubscribersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 1),
    _CServiceControlSubscribersIndex_Type()
)
cServiceControlSubscribersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cServiceControlSubscribersIndex.setStatus("current")
_CServiceControlSubscribersName_Type = SnmpAdminString
_CServiceControlSubscribersName_Object = MibTableColumn
cServiceControlSubscribersName = _CServiceControlSubscribersName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 2),
    _CServiceControlSubscribersName_Type()
)
cServiceControlSubscribersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cServiceControlSubscribersName.setStatus("current")


class _CServiceControlSubscriberStorageType_Type(StorageType):
    """Custom type cServiceControlSubscriberStorageType based on StorageType"""


_CServiceControlSubscriberStorageType_Object = MibTableColumn
cServiceControlSubscriberStorageType = _CServiceControlSubscriberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 3),
    _CServiceControlSubscriberStorageType_Type()
)
cServiceControlSubscriberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cServiceControlSubscriberStorageType.setStatus("current")
_CServiceControlSubscribersRowStatus_Type = RowStatus
_CServiceControlSubscribersRowStatus_Object = MibTableColumn
cServiceControlSubscribersRowStatus = _CServiceControlSubscribersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 1, 1, 4),
    _CServiceControlSubscribersRowStatus_Type()
)
cServiceControlSubscribersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cServiceControlSubscribersRowStatus.setStatus("current")
_CServiceControlSubscribersInfoTable_Object = MibTable
cServiceControlSubscribersInfoTable = _CServiceControlSubscribersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2)
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersInfoTable.setStatus("current")
_CServiceControlSubscribersInfoEntry_Object = MibTableRow
cServiceControlSubscribersInfoEntry = _CServiceControlSubscribersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1)
)
cServiceControlSubscribersInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersInfoEntry.setStatus("current")
_CServiceControlSubscribersNumIntroduced_Type = Gauge32
_CServiceControlSubscribersNumIntroduced_Object = MibTableColumn
cServiceControlSubscribersNumIntroduced = _CServiceControlSubscribersNumIntroduced_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 1),
    _CServiceControlSubscribersNumIntroduced_Type()
)
cServiceControlSubscribersNumIntroduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumIntroduced.setStatus("current")
_CServiceControlSubscribersNumFree_Type = Gauge32
_CServiceControlSubscribersNumFree_Object = MibTableColumn
cServiceControlSubscribersNumFree = _CServiceControlSubscribersNumFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 2),
    _CServiceControlSubscribersNumFree_Type()
)
cServiceControlSubscribersNumFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumFree.setStatus("current")
_CServiceControlSubscribersNumIpAddrMappings_Type = Gauge32
_CServiceControlSubscribersNumIpAddrMappings_Object = MibTableColumn
cServiceControlSubscribersNumIpAddrMappings = _CServiceControlSubscribersNumIpAddrMappings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 3),
    _CServiceControlSubscribersNumIpAddrMappings_Type()
)
cServiceControlSubscribersNumIpAddrMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumIpAddrMappings.setStatus("current")
_CServiceControlSubscribersNumIpAddrMappingsFree_Type = Gauge32
_CServiceControlSubscribersNumIpAddrMappingsFree_Object = MibTableColumn
cServiceControlSubscribersNumIpAddrMappingsFree = _CServiceControlSubscribersNumIpAddrMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 4),
    _CServiceControlSubscribersNumIpAddrMappingsFree_Type()
)
cServiceControlSubscribersNumIpAddrMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumIpAddrMappingsFree.setStatus("current")
_CServiceControlSubscribersNumIpRangeMappings_Type = Gauge32
_CServiceControlSubscribersNumIpRangeMappings_Object = MibTableColumn
cServiceControlSubscribersNumIpRangeMappings = _CServiceControlSubscribersNumIpRangeMappings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 5),
    _CServiceControlSubscribersNumIpRangeMappings_Type()
)
cServiceControlSubscribersNumIpRangeMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumIpRangeMappings.setStatus("current")
_CServiceControlSubscribersNumIpRangeMappingsFree_Type = Gauge32
_CServiceControlSubscribersNumIpRangeMappingsFree_Object = MibTableColumn
cServiceControlSubscribersNumIpRangeMappingsFree = _CServiceControlSubscribersNumIpRangeMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 6),
    _CServiceControlSubscribersNumIpRangeMappingsFree_Type()
)
cServiceControlSubscribersNumIpRangeMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumIpRangeMappingsFree.setStatus("current")
_CServiceControlSubscribersNumVlanMappings_Type = Gauge32
_CServiceControlSubscribersNumVlanMappings_Object = MibTableColumn
cServiceControlSubscribersNumVlanMappings = _CServiceControlSubscribersNumVlanMappings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 7),
    _CServiceControlSubscribersNumVlanMappings_Type()
)
cServiceControlSubscribersNumVlanMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumVlanMappings.setStatus("current")
_CServiceControlSubscribersNumVlanMappingsFree_Type = Gauge32
_CServiceControlSubscribersNumVlanMappingsFree_Object = MibTableColumn
cServiceControlSubscribersNumVlanMappingsFree = _CServiceControlSubscribersNumVlanMappingsFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 8),
    _CServiceControlSubscribersNumVlanMappingsFree_Type()
)
cServiceControlSubscribersNumVlanMappingsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumVlanMappingsFree.setStatus("current")
_CServiceControlSubscribersNumActive_Type = Gauge32
_CServiceControlSubscribersNumActive_Object = MibTableColumn
cServiceControlSubscribersNumActive = _CServiceControlSubscribersNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 9),
    _CServiceControlSubscribersNumActive_Type()
)
cServiceControlSubscribersNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumActive.setStatus("current")
_CServiceControlSubscribersNumUpdates_Type = Counter32
_CServiceControlSubscribersNumUpdates_Object = MibTableColumn
cServiceControlSubscribersNumUpdates = _CServiceControlSubscribersNumUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 10),
    _CServiceControlSubscribersNumUpdates_Type()
)
cServiceControlSubscribersNumUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumUpdates.setStatus("current")
_CServiceControlSubscribersNumTpIpRanges_Type = Gauge32
_CServiceControlSubscribersNumTpIpRanges_Object = MibTableColumn
cServiceControlSubscribersNumTpIpRanges = _CServiceControlSubscribersNumTpIpRanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 11),
    _CServiceControlSubscribersNumTpIpRanges_Type()
)
cServiceControlSubscribersNumTpIpRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumTpIpRanges.setStatus("current")
_CServiceControlSubscribersNumTpIpRangesFree_Type = Gauge32
_CServiceControlSubscribersNumTpIpRangesFree_Object = MibTableColumn
cServiceControlSubscribersNumTpIpRangesFree = _CServiceControlSubscribersNumTpIpRangesFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 12),
    _CServiceControlSubscribersNumTpIpRangesFree_Type()
)
cServiceControlSubscribersNumTpIpRangesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumTpIpRangesFree.setStatus("current")
_CServiceControlSubscribersNumAnonymous_Type = Gauge32
_CServiceControlSubscribersNumAnonymous_Object = MibTableColumn
cServiceControlSubscribersNumAnonymous = _CServiceControlSubscribersNumAnonymous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 13),
    _CServiceControlSubscribersNumAnonymous_Type()
)
cServiceControlSubscribersNumAnonymous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumAnonymous.setStatus("current")
_CServiceControlSubscribersNumWithSessions_Type = Gauge32
_CServiceControlSubscribersNumWithSessions_Object = MibTableColumn
cServiceControlSubscribersNumWithSessions = _CServiceControlSubscribersNumWithSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 14),
    _CServiceControlSubscribersNumWithSessions_Type()
)
cServiceControlSubscribersNumWithSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNumWithSessions.setStatus("current")
_CServiceControlSubscriberMappingFailedReason_Type = SnmpAdminString
_CServiceControlSubscriberMappingFailedReason_Object = MibTableColumn
cServiceControlSubscriberMappingFailedReason = _CServiceControlSubscriberMappingFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 15),
    _CServiceControlSubscriberMappingFailedReason_Type()
)
cServiceControlSubscriberMappingFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubscriberMappingFailedReason.setStatus("current")
_CServiceControlSubsribersMaxSupported_Type = Unsigned32
_CServiceControlSubsribersMaxSupported_Object = MibTableColumn
cServiceControlSubsribersMaxSupported = _CServiceControlSubsribersMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 2, 1, 16),
    _CServiceControlSubsribersMaxSupported_Type()
)
cServiceControlSubsribersMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cServiceControlSubsribersMaxSupported.setStatus("current")
_CServiceControlSubscribersNotifsEnable_Type = TruthValue
_CServiceControlSubscribersNotifsEnable_Object = MibScalar
cServiceControlSubscribersNotifsEnable = _CServiceControlSubscribersNotifsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 1, 3),
    _CServiceControlSubscribersNotifsEnable_Type()
)
cServiceControlSubscribersNotifsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cServiceControlSubscribersNotifsEnable.setStatus("current")
_CiscoServiceControlSubscribersMIBConform_ObjectIdentity = ObjectIdentity
ciscoServiceControlSubscribersMIBConform = _CiscoServiceControlSubscribersMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2)
)
_CServiceControlSubscribersCompliances_ObjectIdentity = ObjectIdentity
cServiceControlSubscribersCompliances = _CServiceControlSubscribersCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 1)
)
_CServiceControlSubscribersGroups_ObjectIdentity = ObjectIdentity
cServiceControlSubscribersGroups = _CServiceControlSubscribersGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2)
)

# Managed Objects groups

cServiceControlSubscribersObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 1)
)
cServiceControlSubscribersObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersName"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersRowStatus"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberStorageType"))
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersObjectGroup.setStatus("current")

cServiceControlSubscribersInfoObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 3)
)
cServiceControlSubscribersInfoObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIntroduced"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumFree"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpAddrMappings"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpAddrMappingsFree"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpRangeMappings"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumIpRangeMappingsFree"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumVlanMappings"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumVlanMappingsFree"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumActive"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumUpdates"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumTpIpRanges"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumTpIpRangesFree"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumAnonymous"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNumWithSessions"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMappingFailedReason"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubsribersMaxSupported"))
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersInfoObjectGroup.setStatus("current")

cServiceControlSubscribersNotifsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 4)
)
cServiceControlSubscribersNotifsGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscribersNotifsEnable")
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersNotifsGroup.setStatus("current")


# Notification objects

cServiceControlSubscriberMapping = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 0, 1)
)
cServiceControlSubscriberMapping.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMappingFailedReason"))
)
if mibBuilder.loadTexts:
    cServiceControlSubscriberMapping.setStatus(
        "current"
    )


# Notifications groups

cServiceControlSubscribersNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 2, 2)
)
cServiceControlSubscribersNotificationGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB", "cServiceControlSubscriberMapping")
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cServiceControlSubscribersCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 628, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cServiceControlSubscribersCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROL-SUBSCRIBERS-MIB",
    **{"ciscoServiceControlSubscribersMIB": ciscoServiceControlSubscribersMIB,
       "ciscoServiceControlSubscribersMIBNotifs": ciscoServiceControlSubscribersMIBNotifs,
       "cServiceControlSubscriberMapping": cServiceControlSubscriberMapping,
       "ciscoServiceControlSubscribersMIBObjects": ciscoServiceControlSubscribersMIBObjects,
       "cServiceControlSubscribersTable": cServiceControlSubscribersTable,
       "cServiceControlSubscribersEntry": cServiceControlSubscribersEntry,
       "cServiceControlSubscribersIndex": cServiceControlSubscribersIndex,
       "cServiceControlSubscribersName": cServiceControlSubscribersName,
       "cServiceControlSubscriberStorageType": cServiceControlSubscriberStorageType,
       "cServiceControlSubscribersRowStatus": cServiceControlSubscribersRowStatus,
       "cServiceControlSubscribersInfoTable": cServiceControlSubscribersInfoTable,
       "cServiceControlSubscribersInfoEntry": cServiceControlSubscribersInfoEntry,
       "cServiceControlSubscribersNumIntroduced": cServiceControlSubscribersNumIntroduced,
       "cServiceControlSubscribersNumFree": cServiceControlSubscribersNumFree,
       "cServiceControlSubscribersNumIpAddrMappings": cServiceControlSubscribersNumIpAddrMappings,
       "cServiceControlSubscribersNumIpAddrMappingsFree": cServiceControlSubscribersNumIpAddrMappingsFree,
       "cServiceControlSubscribersNumIpRangeMappings": cServiceControlSubscribersNumIpRangeMappings,
       "cServiceControlSubscribersNumIpRangeMappingsFree": cServiceControlSubscribersNumIpRangeMappingsFree,
       "cServiceControlSubscribersNumVlanMappings": cServiceControlSubscribersNumVlanMappings,
       "cServiceControlSubscribersNumVlanMappingsFree": cServiceControlSubscribersNumVlanMappingsFree,
       "cServiceControlSubscribersNumActive": cServiceControlSubscribersNumActive,
       "cServiceControlSubscribersNumUpdates": cServiceControlSubscribersNumUpdates,
       "cServiceControlSubscribersNumTpIpRanges": cServiceControlSubscribersNumTpIpRanges,
       "cServiceControlSubscribersNumTpIpRangesFree": cServiceControlSubscribersNumTpIpRangesFree,
       "cServiceControlSubscribersNumAnonymous": cServiceControlSubscribersNumAnonymous,
       "cServiceControlSubscribersNumWithSessions": cServiceControlSubscribersNumWithSessions,
       "cServiceControlSubscriberMappingFailedReason": cServiceControlSubscriberMappingFailedReason,
       "cServiceControlSubsribersMaxSupported": cServiceControlSubsribersMaxSupported,
       "cServiceControlSubscribersNotifsEnable": cServiceControlSubscribersNotifsEnable,
       "ciscoServiceControlSubscribersMIBConform": ciscoServiceControlSubscribersMIBConform,
       "cServiceControlSubscribersCompliances": cServiceControlSubscribersCompliances,
       "cServiceControlSubscribersCompliance": cServiceControlSubscribersCompliance,
       "cServiceControlSubscribersGroups": cServiceControlSubscribersGroups,
       "cServiceControlSubscribersObjectGroup": cServiceControlSubscribersObjectGroup,
       "cServiceControlSubscribersNotificationGroup": cServiceControlSubscribersNotificationGroup,
       "cServiceControlSubscribersInfoObjectGroup": cServiceControlSubscribersInfoObjectGroup,
       "cServiceControlSubscribersNotifsGroup": cServiceControlSubscribersNotifsGroup}
)
