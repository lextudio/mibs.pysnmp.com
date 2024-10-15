# SNMP MIB module (HP-ICF-UFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-UFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:22 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpicfUfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74)
)
hpicfUfdMIB.setRevisions(
        ("2012-04-30 00:00",
         "2011-05-12 00:00",
         "2010-02-06 15:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpUfdTrackEntityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ufd", 1)
    )



class HpUfdTrackLinksSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacpKey", 2),
          ("none", 0),
          ("portMap", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfUfdNotifications_ObjectIdentity = ObjectIdentity
hpicfUfdNotifications = _HpicfUfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0)
)
_HpicfUfdNotificationPrefix_ObjectIdentity = ObjectIdentity
hpicfUfdNotificationPrefix = _HpicfUfdNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0)
)
_HpicfUfdConfigObjects_ObjectIdentity = ObjectIdentity
hpicfUfdConfigObjects = _HpicfUfdConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1)
)
_HpicfUfdScalars_ObjectIdentity = ObjectIdentity
hpicfUfdScalars = _HpicfUfdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1)
)


class _HpicfUfdAdminStatus_Type(Integer32):
    """Custom type hpicfUfdAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfUfdAdminStatus_Type.__name__ = "Integer32"
_HpicfUfdAdminStatus_Object = MibScalar
hpicfUfdAdminStatus = _HpicfUfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 1),
    _HpicfUfdAdminStatus_Type()
)
hpicfUfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdAdminStatus.setStatus("current")


class _HpicfUfdNotifyTrackId_Type(Integer32):
    """Custom type hpicfUfdNotifyTrackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HpicfUfdNotifyTrackId_Type.__name__ = "Integer32"
_HpicfUfdNotifyTrackId_Object = MibScalar
hpicfUfdNotifyTrackId = _HpicfUfdNotifyTrackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 2),
    _HpicfUfdNotifyTrackId_Type()
)
hpicfUfdNotifyTrackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfUfdNotifyTrackId.setStatus("current")
_HpicfUfdTrackEntities_ObjectIdentity = ObjectIdentity
hpicfUfdTrackEntities = _HpicfUfdTrackEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2)
)
_HpicfUfdTrackTable_Object = MibTable
hpicfUfdTrackTable = _HpicfUfdTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUfdTrackTable.setStatus("current")
_HpicfUfdTrackEntry_Object = MibTableRow
hpicfUfdTrackEntry = _HpicfUfdTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1)
)
hpicfUfdTrackEntry.setIndexNames(
    (0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"),
)
if mibBuilder.loadTexts:
    hpicfUfdTrackEntry.setStatus("current")


class _HpicfUfdTrackId_Type(Integer32):
    """Custom type hpicfUfdTrackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HpicfUfdTrackId_Type.__name__ = "Integer32"
_HpicfUfdTrackId_Object = MibTableColumn
hpicfUfdTrackId = _HpicfUfdTrackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 1),
    _HpicfUfdTrackId_Type()
)
hpicfUfdTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUfdTrackId.setStatus("current")
_HpicfUfdTrackEntityType_Type = HpUfdTrackEntityType
_HpicfUfdTrackEntityType_Object = MibTableColumn
hpicfUfdTrackEntityType = _HpicfUfdTrackEntityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 2),
    _HpicfUfdTrackEntityType_Type()
)
hpicfUfdTrackEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdTrackEntityType.setStatus("current")


class _HpicfUfdLinksToMonitor_Type(OctetString):
    """Custom type hpicfUfdLinksToMonitor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HpicfUfdLinksToMonitor_Type.__name__ = "OctetString"
_HpicfUfdLinksToMonitor_Object = MibTableColumn
hpicfUfdLinksToMonitor = _HpicfUfdLinksToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 3),
    _HpicfUfdLinksToMonitor_Type()
)
hpicfUfdLinksToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdLinksToMonitor.setStatus("current")


class _HpicfUfdLinksToTransition_Type(OctetString):
    """Custom type hpicfUfdLinksToTransition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_HpicfUfdLinksToTransition_Type.__name__ = "OctetString"
_HpicfUfdLinksToTransition_Object = MibTableColumn
hpicfUfdLinksToTransition = _HpicfUfdLinksToTransition_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 4),
    _HpicfUfdLinksToTransition_Type()
)
hpicfUfdLinksToTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdLinksToTransition.setStatus("current")


class _HpicfUfdLinksToMonitorState_Type(Integer32):
    """Custom type hpicfUfdLinksToMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HpicfUfdLinksToMonitorState_Type.__name__ = "Integer32"
_HpicfUfdLinksToMonitorState_Object = MibTableColumn
hpicfUfdLinksToMonitorState = _HpicfUfdLinksToMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 5),
    _HpicfUfdLinksToMonitorState_Type()
)
hpicfUfdLinksToMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUfdLinksToMonitorState.setStatus("current")


class _HpicfUfdLinksToTransitionState_Type(Integer32):
    """Custom type hpicfUfdLinksToTransitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDisabled", 2),
          ("up", 1))
    )


_HpicfUfdLinksToTransitionState_Type.__name__ = "Integer32"
_HpicfUfdLinksToTransitionState_Object = MibTableColumn
hpicfUfdLinksToTransitionState = _HpicfUfdLinksToTransitionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 6),
    _HpicfUfdLinksToTransitionState_Type()
)
hpicfUfdLinksToTransitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUfdLinksToTransitionState.setStatus("current")


class _HpicfUfdTrackEntityState_Type(Integer32):
    """Custom type hpicfUfdTrackEntityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("none", 0),
          ("ok", 1))
    )


_HpicfUfdTrackEntityState_Type.__name__ = "Integer32"
_HpicfUfdTrackEntityState_Object = MibTableColumn
hpicfUfdTrackEntityState = _HpicfUfdTrackEntityState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 7),
    _HpicfUfdTrackEntityState_Type()
)
hpicfUfdTrackEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUfdTrackEntityState.setStatus("current")
_HpicfUfdTrackEntityRowStatus_Type = RowStatus
_HpicfUfdTrackEntityRowStatus_Object = MibTableColumn
hpicfUfdTrackEntityRowStatus = _HpicfUfdTrackEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 8),
    _HpicfUfdTrackEntityRowStatus_Type()
)
hpicfUfdTrackEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUfdTrackEntityRowStatus.setStatus("current")
_HpicfUfdLinksToMonitorType_Type = HpUfdTrackLinksSubtype
_HpicfUfdLinksToMonitorType_Object = MibTableColumn
hpicfUfdLinksToMonitorType = _HpicfUfdLinksToMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 9),
    _HpicfUfdLinksToMonitorType_Type()
)
hpicfUfdLinksToMonitorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdLinksToMonitorType.setStatus("current")
_HpicfUfdLinksToTransitionType_Type = HpUfdTrackLinksSubtype
_HpicfUfdLinksToTransitionType_Object = MibTableColumn
hpicfUfdLinksToTransitionType = _HpicfUfdLinksToTransitionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 10),
    _HpicfUfdLinksToTransitionType_Type()
)
hpicfUfdLinksToTransitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUfdLinksToTransitionType.setStatus("current")
_HpicfUfdTrackedLinkTable_Object = MibTable
hpicfUfdTrackedLinkTable = _HpicfUfdTrackedLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfUfdTrackedLinkTable.setStatus("current")
_HpicfUfdTrackedLinkEntry_Object = MibTableRow
hpicfUfdTrackedLinkEntry = _HpicfUfdTrackedLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1)
)
hpicfUfdTrackedLinkEntry.setIndexNames(
    (0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"),
    (0, "HP-ICF-UFD-MIB", "hpicfUfdIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfUfdTrackedLinkEntry.setStatus("current")
_HpicfUfdIfIndex_Type = InterfaceIndex
_HpicfUfdIfIndex_Object = MibTableColumn
hpicfUfdIfIndex = _HpicfUfdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 1),
    _HpicfUfdIfIndex_Type()
)
hpicfUfdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUfdIfIndex.setStatus("current")


class _HpicfUfdLinkRole_Type(Integer32):
    """Custom type hpicfUfdLinkRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("uplink", 1))
    )


_HpicfUfdLinkRole_Type.__name__ = "Integer32"
_HpicfUfdLinkRole_Object = MibTableColumn
hpicfUfdLinkRole = _HpicfUfdLinkRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 2),
    _HpicfUfdLinkRole_Type()
)
hpicfUfdLinkRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUfdLinkRole.setStatus("current")
_HpicfUfdConformance_ObjectIdentity = ObjectIdentity
hpicfUfdConformance = _HpicfUfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3)
)
_HpicfUfdCompliances_ObjectIdentity = ObjectIdentity
hpicfUfdCompliances = _HpicfUfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1)
)
_HpicfUfdGroups_ObjectIdentity = ObjectIdentity
hpicfUfdGroups = _HpicfUfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2)
)

# Managed Objects groups

hpicfUfdBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 1)
)
hpicfUfdBaseGroup.setObjects(
      *(("HP-ICF-UFD-MIB", "hpicfUfdAdminStatus"),
        ("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"))
)
if mibBuilder.loadTexts:
    hpicfUfdBaseGroup.setStatus("current")

hpicfUfdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 2)
)
hpicfUfdConfigGroup.setObjects(
      *(("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityType"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitor"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorState"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionState"),
        ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityState"),
        ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityRowStatus"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorType"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionType"))
)
if mibBuilder.loadTexts:
    hpicfUfdConfigGroup.setStatus("current")

hpicfUfdConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 4)
)
hpicfUfdConfigGroup1.setObjects(
    ("HP-ICF-UFD-MIB", "hpicfUfdLinkRole")
)
if mibBuilder.loadTexts:
    hpicfUfdConfigGroup1.setStatus("current")


# Notification objects

hpicfUfdLtDAutoDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 3)
)
hpicfUfdLtDAutoDisabled.setObjects(
      *(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
)
if mibBuilder.loadTexts:
    hpicfUfdLtDAutoDisabled.setStatus(
        "current"
    )

hpicfUfdLtDAutoEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 4)
)
hpicfUfdLtDAutoEnabled.setObjects(
      *(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
)
if mibBuilder.loadTexts:
    hpicfUfdLtDAutoEnabled.setStatus(
        "current"
    )


# Notifications groups

hpicfUfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 3)
)
hpicfUfdNotificationGroup.setObjects(
      *(("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoDisabled"),
        ("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoEnabled"))
)
if mibBuilder.loadTexts:
    hpicfUfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfUfdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfUfdCompliance.setStatus(
        "deprecated"
    )

hpicfUfdCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfUfdCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-UFD-MIB",
    **{"HpUfdTrackEntityType": HpUfdTrackEntityType,
       "HpUfdTrackLinksSubtype": HpUfdTrackLinksSubtype,
       "hpicfUfdMIB": hpicfUfdMIB,
       "hpicfUfdNotifications": hpicfUfdNotifications,
       "hpicfUfdNotificationPrefix": hpicfUfdNotificationPrefix,
       "hpicfUfdLtDAutoDisabled": hpicfUfdLtDAutoDisabled,
       "hpicfUfdLtDAutoEnabled": hpicfUfdLtDAutoEnabled,
       "hpicfUfdConfigObjects": hpicfUfdConfigObjects,
       "hpicfUfdScalars": hpicfUfdScalars,
       "hpicfUfdAdminStatus": hpicfUfdAdminStatus,
       "hpicfUfdNotifyTrackId": hpicfUfdNotifyTrackId,
       "hpicfUfdTrackEntities": hpicfUfdTrackEntities,
       "hpicfUfdTrackTable": hpicfUfdTrackTable,
       "hpicfUfdTrackEntry": hpicfUfdTrackEntry,
       "hpicfUfdTrackId": hpicfUfdTrackId,
       "hpicfUfdTrackEntityType": hpicfUfdTrackEntityType,
       "hpicfUfdLinksToMonitor": hpicfUfdLinksToMonitor,
       "hpicfUfdLinksToTransition": hpicfUfdLinksToTransition,
       "hpicfUfdLinksToMonitorState": hpicfUfdLinksToMonitorState,
       "hpicfUfdLinksToTransitionState": hpicfUfdLinksToTransitionState,
       "hpicfUfdTrackEntityState": hpicfUfdTrackEntityState,
       "hpicfUfdTrackEntityRowStatus": hpicfUfdTrackEntityRowStatus,
       "hpicfUfdLinksToMonitorType": hpicfUfdLinksToMonitorType,
       "hpicfUfdLinksToTransitionType": hpicfUfdLinksToTransitionType,
       "hpicfUfdTrackedLinkTable": hpicfUfdTrackedLinkTable,
       "hpicfUfdTrackedLinkEntry": hpicfUfdTrackedLinkEntry,
       "hpicfUfdIfIndex": hpicfUfdIfIndex,
       "hpicfUfdLinkRole": hpicfUfdLinkRole,
       "hpicfUfdConformance": hpicfUfdConformance,
       "hpicfUfdCompliances": hpicfUfdCompliances,
       "hpicfUfdCompliance": hpicfUfdCompliance,
       "hpicfUfdCompliance1": hpicfUfdCompliance1,
       "hpicfUfdGroups": hpicfUfdGroups,
       "hpicfUfdBaseGroup": hpicfUfdBaseGroup,
       "hpicfUfdConfigGroup": hpicfUfdConfigGroup,
       "hpicfUfdNotificationGroup": hpicfUfdNotificationGroup,
       "hpicfUfdConfigGroup1": hpicfUfdConfigGroup1}
)
