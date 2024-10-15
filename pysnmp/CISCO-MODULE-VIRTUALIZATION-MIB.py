# SNMP MIB module (CISCO-MODULE-VIRTUALIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MODULE-VIRTUALIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:53 2024
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

(CiscoResourceClass,) = mibBuilder.importSymbols(
    "CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB",
    "CiscoResourceClass")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

ciscoModuleVirtualizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472)
)
ciscoModuleVirtualizationMIB.setRevisions(
        ("2006-05-29 00:00",
         "2005-12-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmVirtualizationNotifs_ObjectIdentity = ObjectIdentity
cmVirtualizationNotifs = _CmVirtualizationNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 0)
)
_CmVirtualizationMIBObjects_ObjectIdentity = ObjectIdentity
cmVirtualizationMIBObjects = _CmVirtualizationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1)
)
_CmVirtualContext_ObjectIdentity = ObjectIdentity
cmVirtualContext = _CmVirtualContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1)
)
_CmVirtualContextTable_Object = MibTable
cmVirtualContextTable = _CmVirtualContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmVirtualContextTable.setStatus("current")
_CmVirtualContextEntry_Object = MibTableRow
cmVirtualContextEntry = _CmVirtualContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1)
)
cmVirtualContextEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextName"),
)
if mibBuilder.loadTexts:
    cmVirtualContextEntry.setStatus("current")
_CmVirtContextName_Type = SnmpAdminString
_CmVirtContextName_Object = MibTableColumn
cmVirtContextName = _CmVirtContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 1),
    _CmVirtContextName_Type()
)
cmVirtContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmVirtContextName.setStatus("current")
_CmVirtContextDescr_Type = SnmpAdminString
_CmVirtContextDescr_Object = MibTableColumn
cmVirtContextDescr = _CmVirtContextDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 2),
    _CmVirtContextDescr_Type()
)
cmVirtContextDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextDescr.setStatus("current")
_CmVirtContextURL_Type = CiscoURLString
_CmVirtContextURL_Object = MibTableColumn
cmVirtContextURL = _CmVirtContextURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 3),
    _CmVirtContextURL_Type()
)
cmVirtContextURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextURL.setStatus("current")
_CmVirtContextResourceClass_Type = CiscoResourceClass
_CmVirtContextResourceClass_Object = MibTableColumn
cmVirtContextResourceClass = _CmVirtContextResourceClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 4),
    _CmVirtContextResourceClass_Type()
)
cmVirtContextResourceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextResourceClass.setStatus("current")


class _CmVirtContextStorageType_Type(StorageType):
    """Custom type cmVirtContextStorageType based on StorageType"""


_CmVirtContextStorageType_Object = MibTableColumn
cmVirtContextStorageType = _CmVirtContextStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 5),
    _CmVirtContextStorageType_Type()
)
cmVirtContextStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextStorageType.setStatus("current")
_CmVirtContextRowStatus_Type = RowStatus
_CmVirtContextRowStatus_Object = MibTableColumn
cmVirtContextRowStatus = _CmVirtContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 1, 1, 6),
    _CmVirtContextRowStatus_Type()
)
cmVirtContextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextRowStatus.setStatus("current")
_CmVirtContextIfMapTable_Object = MibTable
cmVirtContextIfMapTable = _CmVirtContextIfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmVirtContextIfMapTable.setStatus("current")
_CmVirtContextIfMapEntry_Object = MibTableRow
cmVirtContextIfMapEntry = _CmVirtContextIfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1)
)
cmVirtContextIfMapEntry.setIndexNames(
    (0, "CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextName"),
    (0, "CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextIfMapType"),
    (0, "CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextIfMapIdLow"),
)
if mibBuilder.loadTexts:
    cmVirtContextIfMapEntry.setStatus("current")
_CmVirtContextIfMapType_Type = IANAifType
_CmVirtContextIfMapType_Object = MibTableColumn
cmVirtContextIfMapType = _CmVirtContextIfMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1, 1),
    _CmVirtContextIfMapType_Type()
)
cmVirtContextIfMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmVirtContextIfMapType.setStatus("current")
_CmVirtContextIfMapIdLow_Type = Unsigned32
_CmVirtContextIfMapIdLow_Object = MibTableColumn
cmVirtContextIfMapIdLow = _CmVirtContextIfMapIdLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1, 2),
    _CmVirtContextIfMapIdLow_Type()
)
cmVirtContextIfMapIdLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmVirtContextIfMapIdLow.setStatus("current")
_CmVirtContextIfMapIdHigh_Type = Unsigned32
_CmVirtContextIfMapIdHigh_Object = MibTableColumn
cmVirtContextIfMapIdHigh = _CmVirtContextIfMapIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1, 3),
    _CmVirtContextIfMapIdHigh_Type()
)
cmVirtContextIfMapIdHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextIfMapIdHigh.setStatus("current")


class _CmVirtContextIfMapStorageType_Type(StorageType):
    """Custom type cmVirtContextIfMapStorageType based on StorageType"""


_CmVirtContextIfMapStorageType_Object = MibTableColumn
cmVirtContextIfMapStorageType = _CmVirtContextIfMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1, 4),
    _CmVirtContextIfMapStorageType_Type()
)
cmVirtContextIfMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextIfMapStorageType.setStatus("current")
_CmVirtContextIfMapRowStatus_Type = RowStatus
_CmVirtContextIfMapRowStatus_Object = MibTableColumn
cmVirtContextIfMapRowStatus = _CmVirtContextIfMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 1, 2, 1, 5),
    _CmVirtContextIfMapRowStatus_Type()
)
cmVirtContextIfMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmVirtContextIfMapRowStatus.setStatus("current")
_CmVirtualContextNotifControl_ObjectIdentity = ObjectIdentity
cmVirtualContextNotifControl = _CmVirtualContextNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 2)
)
_CmVirtContextNotifEnable_Type = TruthValue
_CmVirtContextNotifEnable_Object = MibScalar
cmVirtContextNotifEnable = _CmVirtContextNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 2, 1),
    _CmVirtContextNotifEnable_Type()
)
cmVirtContextNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmVirtContextNotifEnable.setStatus("current")
_CmVirtualContextNotifObjects_ObjectIdentity = ObjectIdentity
cmVirtualContextNotifObjects = _CmVirtualContextNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 3)
)
_CmNotifVirtContextName_Type = SnmpAdminString
_CmNotifVirtContextName_Object = MibScalar
cmNotifVirtContextName = _CmNotifVirtContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 1, 3, 1),
    _CmNotifVirtContextName_Type()
)
cmNotifVirtContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmNotifVirtContextName.setStatus("current")
_CmVirtualizationMIBConformance_ObjectIdentity = ObjectIdentity
cmVirtualizationMIBConformance = _CmVirtualizationMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2)
)
_CmVirtualizationCompliances_ObjectIdentity = ObjectIdentity
cmVirtualizationCompliances = _CmVirtualizationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 1)
)
_CmVirtualizationGroups_ObjectIdentity = ObjectIdentity
cmVirtualizationGroups = _CmVirtualizationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2)
)

# Managed Objects groups

cmVirtContextconfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2, 1)
)
cmVirtContextconfigGroup.setObjects(
      *(("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextDescr"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextURL"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextResourceClass"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextStorageType"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextRowStatus"))
)
if mibBuilder.loadTexts:
    cmVirtContextconfigGroup.setStatus("current")

cmVirtContextIfMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2, 2)
)
cmVirtContextIfMapGroup.setObjects(
      *(("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextIfMapIdHigh"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextIfMapStorageType"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextIfMapRowStatus"))
)
if mibBuilder.loadTexts:
    cmVirtContextIfMapGroup.setStatus("current")

cmVirtContextNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2, 3)
)
cmVirtContextNotifControlGroup.setObjects(
    ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextNotifEnable")
)
if mibBuilder.loadTexts:
    cmVirtContextNotifControlGroup.setStatus("current")

cmVirtContextNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2, 4)
)
cmVirtContextNotifObjectsGroup.setObjects(
    ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmNotifVirtContextName")
)
if mibBuilder.loadTexts:
    cmVirtContextNotifObjectsGroup.setStatus("current")


# Notification objects

cmVirtContextAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 0, 1)
)
cmVirtContextAdded.setObjects(
    ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmNotifVirtContextName")
)
if mibBuilder.loadTexts:
    cmVirtContextAdded.setStatus(
        "current"
    )

cmVirtContextRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 0, 2)
)
cmVirtContextRemoved.setObjects(
    ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmNotifVirtContextName")
)
if mibBuilder.loadTexts:
    cmVirtContextRemoved.setStatus(
        "current"
    )


# Notifications groups

cmVirtContextNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 2, 5)
)
cmVirtContextNotificationGroup.setObjects(
      *(("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextAdded"),
        ("CISCO-MODULE-VIRTUALIZATION-MIB", "cmVirtContextRemoved"))
)
if mibBuilder.loadTexts:
    cmVirtContextNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmVirtualizationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 472, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmVirtualizationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MODULE-VIRTUALIZATION-MIB",
    **{"ciscoModuleVirtualizationMIB": ciscoModuleVirtualizationMIB,
       "cmVirtualizationNotifs": cmVirtualizationNotifs,
       "cmVirtContextAdded": cmVirtContextAdded,
       "cmVirtContextRemoved": cmVirtContextRemoved,
       "cmVirtualizationMIBObjects": cmVirtualizationMIBObjects,
       "cmVirtualContext": cmVirtualContext,
       "cmVirtualContextTable": cmVirtualContextTable,
       "cmVirtualContextEntry": cmVirtualContextEntry,
       "cmVirtContextName": cmVirtContextName,
       "cmVirtContextDescr": cmVirtContextDescr,
       "cmVirtContextURL": cmVirtContextURL,
       "cmVirtContextResourceClass": cmVirtContextResourceClass,
       "cmVirtContextStorageType": cmVirtContextStorageType,
       "cmVirtContextRowStatus": cmVirtContextRowStatus,
       "cmVirtContextIfMapTable": cmVirtContextIfMapTable,
       "cmVirtContextIfMapEntry": cmVirtContextIfMapEntry,
       "cmVirtContextIfMapType": cmVirtContextIfMapType,
       "cmVirtContextIfMapIdLow": cmVirtContextIfMapIdLow,
       "cmVirtContextIfMapIdHigh": cmVirtContextIfMapIdHigh,
       "cmVirtContextIfMapStorageType": cmVirtContextIfMapStorageType,
       "cmVirtContextIfMapRowStatus": cmVirtContextIfMapRowStatus,
       "cmVirtualContextNotifControl": cmVirtualContextNotifControl,
       "cmVirtContextNotifEnable": cmVirtContextNotifEnable,
       "cmVirtualContextNotifObjects": cmVirtualContextNotifObjects,
       "cmNotifVirtContextName": cmNotifVirtContextName,
       "cmVirtualizationMIBConformance": cmVirtualizationMIBConformance,
       "cmVirtualizationCompliances": cmVirtualizationCompliances,
       "cmVirtualizationCompliance": cmVirtualizationCompliance,
       "cmVirtualizationGroups": cmVirtualizationGroups,
       "cmVirtContextconfigGroup": cmVirtContextconfigGroup,
       "cmVirtContextIfMapGroup": cmVirtContextIfMapGroup,
       "cmVirtContextNotifControlGroup": cmVirtContextNotifControlGroup,
       "cmVirtContextNotifObjectsGroup": cmVirtContextNotifObjectsGroup,
       "cmVirtContextNotificationGroup": cmVirtContextNotificationGroup}
)
