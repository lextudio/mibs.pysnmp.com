# SNMP MIB module (SUN-CLUSTER-EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-CLUSTER-EVENTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:30 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

sunClusterEventsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2)
)
sunClusterEventsMIB.setRevisions(
        ("1902-11-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScEventTableCount(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 32767),
    )



class ScEventIndex(Integer32, TextualConvention):
    status = "current"


class ScClusterId(DisplayString, TextualConvention):
    status = "current"


class ScClusterName(DisplayString, TextualConvention):
    status = "current"


class ScNodeName(DisplayString, TextualConvention):
    status = "current"


class ScEventVersion(Integer32, TextualConvention):
    status = "current"


class ScEventClassName(DisplayString, TextualConvention):
    status = "current"


class ScEventSubclassName(DisplayString, TextualConvention):
    status = "current"


class ScEventSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clEventSevCritical", 3),
          ("clEventSevError", 2),
          ("clEventSevFatal", 4),
          ("clEventSevInfo", 0),
          ("clEventSevWarning", 1))
    )



class ScEventInitiator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clEventInitAgent", 3),
          ("clEventInitOperator", 2),
          ("clEventInitSystem", 1),
          ("clEventInitUnknown", 0))
    )



class ScEventPublisher(DisplayString, TextualConvention):
    status = "current"


class ScEventPid(Counter64, TextualConvention):
    status = "current"


class ScTimeStamp(Counter64, TextualConvention):
    status = "current"


class ScEventData(DisplayString, TextualConvention):
    status = "current"


class ScEventAttributeName(DisplayString, TextualConvention):
    status = "current"


class ScEventAttributeValue(DisplayString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Suncluster_ObjectIdentity = ObjectIdentity
suncluster = _Suncluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80)
)
_ScEventsMIBObjects_ObjectIdentity = ObjectIdentity
scEventsMIBObjects = _ScEventsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1)
)
_EscEventTableCount_Type = ScEventTableCount
_EscEventTableCount_Object = MibScalar
escEventTableCount = _EscEventTableCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 1),
    _EscEventTableCount_Type()
)
escEventTableCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    escEventTableCount.setStatus("current")
_EscEventsTable_Object = MibTable
escEventsTable = _EscEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2)
)
if mibBuilder.loadTexts:
    escEventsTable.setStatus("current")
_EscEventsEntry_Object = MibTableRow
escEventsEntry = _EscEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1)
)
escEventsEntry.setIndexNames(
    (0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    escEventsEntry.setStatus("current")
_EventIndex_Type = ScEventIndex
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
_EventClusterId_Type = ScClusterId
_EventClusterId_Object = MibTableColumn
eventClusterId = _EventClusterId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 2),
    _EventClusterId_Type()
)
eventClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClusterId.setStatus("current")
_EventClusterName_Type = ScClusterName
_EventClusterName_Object = MibTableColumn
eventClusterName = _EventClusterName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 3),
    _EventClusterName_Type()
)
eventClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClusterName.setStatus("current")
_EventNodeName_Type = ScNodeName
_EventNodeName_Object = MibTableColumn
eventNodeName = _EventNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 4),
    _EventNodeName_Type()
)
eventNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNodeName.setStatus("current")
_EventVersion_Type = ScEventVersion
_EventVersion_Object = MibTableColumn
eventVersion = _EventVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 5),
    _EventVersion_Type()
)
eventVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventVersion.setStatus("current")
_EventClassName_Type = ScEventClassName
_EventClassName_Object = MibTableColumn
eventClassName = _EventClassName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 6),
    _EventClassName_Type()
)
eventClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClassName.setStatus("current")
_EventSubclassName_Type = ScEventSubclassName
_EventSubclassName_Object = MibTableColumn
eventSubclassName = _EventSubclassName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 7),
    _EventSubclassName_Type()
)
eventSubclassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSubclassName.setStatus("current")
_EventSeverity_Type = ScEventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 8),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventInitiator_Type = ScEventInitiator
_EventInitiator_Object = MibTableColumn
eventInitiator = _EventInitiator_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 9),
    _EventInitiator_Type()
)
eventInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInitiator.setStatus("current")
_EventPublisher_Type = ScEventPublisher
_EventPublisher_Object = MibTableColumn
eventPublisher = _EventPublisher_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 10),
    _EventPublisher_Type()
)
eventPublisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventPublisher.setStatus("current")
_EventSeqNo_Type = Counter64
_EventSeqNo_Object = MibTableColumn
eventSeqNo = _EventSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 11),
    _EventSeqNo_Type()
)
eventSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNo.setStatus("current")
_EventPid_Type = ScEventPid
_EventPid_Object = MibTableColumn
eventPid = _EventPid_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 12),
    _EventPid_Type()
)
eventPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventPid.setStatus("current")
_EventTimeStamp_Type = ScTimeStamp
_EventTimeStamp_Object = MibTableColumn
eventTimeStamp = _EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 13),
    _EventTimeStamp_Type()
)
eventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTimeStamp.setStatus("current")
_EventData_Type = ScEventData
_EventData_Object = MibTableColumn
eventData = _EventData_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 14),
    _EventData_Type()
)
eventData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventData.setStatus("current")
_EscEventsAttributesTable_Object = MibTable
escEventsAttributesTable = _EscEventsAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3)
)
if mibBuilder.loadTexts:
    escEventsAttributesTable.setStatus("current")
_EscEventsAttributesEntry_Object = MibTableRow
escEventsAttributesEntry = _EscEventsAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1)
)
escEventsAttributesEntry.setIndexNames(
    (0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"),
    (0, "SUN-CLUSTER-EVENTS-MIB", "attributeName"),
)
if mibBuilder.loadTexts:
    escEventsAttributesEntry.setStatus("current")
_AttributeName_Type = ScEventAttributeName
_AttributeName_Object = MibTableColumn
attributeName = _AttributeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 1),
    _AttributeName_Type()
)
attributeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attributeName.setStatus("current")
_AttributeValue_Type = ScEventAttributeValue
_AttributeValue_Object = MibTableColumn
attributeValue = _AttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 2),
    _AttributeValue_Type()
)
attributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attributeValue.setStatus("current")
_ScEventsMIBNotifications_ObjectIdentity = ObjectIdentity
scEventsMIBNotifications = _ScEventsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2)
)

# Managed Objects groups


# Notification objects

escNewEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2, 1)
)
escNewEvents.setObjects(
      *(("SUN-CLUSTER-EVENTS-MIB", "eventIndex"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventClusterId"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventClusterName"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventNodeName"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventVersion"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventClassName"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventSubclassName"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventSeverity"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventInitiator"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventPublisher"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventSeqNo"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventPid"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventTimeStamp"),
        ("SUN-CLUSTER-EVENTS-MIB", "eventData"))
)
if mibBuilder.loadTexts:
    escNewEvents.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-CLUSTER-EVENTS-MIB",
    **{"ScEventTableCount": ScEventTableCount,
       "ScEventIndex": ScEventIndex,
       "ScClusterId": ScClusterId,
       "ScClusterName": ScClusterName,
       "ScNodeName": ScNodeName,
       "ScEventVersion": ScEventVersion,
       "ScEventClassName": ScEventClassName,
       "ScEventSubclassName": ScEventSubclassName,
       "ScEventSeverity": ScEventSeverity,
       "ScEventInitiator": ScEventInitiator,
       "ScEventPublisher": ScEventPublisher,
       "ScEventPid": ScEventPid,
       "ScTimeStamp": ScTimeStamp,
       "ScEventData": ScEventData,
       "ScEventAttributeName": ScEventAttributeName,
       "ScEventAttributeValue": ScEventAttributeValue,
       "sun": sun,
       "prod": prod,
       "suncluster": suncluster,
       "sunClusterEventsMIB": sunClusterEventsMIB,
       "scEventsMIBObjects": scEventsMIBObjects,
       "escEventTableCount": escEventTableCount,
       "escEventsTable": escEventsTable,
       "escEventsEntry": escEventsEntry,
       "eventIndex": eventIndex,
       "eventClusterId": eventClusterId,
       "eventClusterName": eventClusterName,
       "eventNodeName": eventNodeName,
       "eventVersion": eventVersion,
       "eventClassName": eventClassName,
       "eventSubclassName": eventSubclassName,
       "eventSeverity": eventSeverity,
       "eventInitiator": eventInitiator,
       "eventPublisher": eventPublisher,
       "eventSeqNo": eventSeqNo,
       "eventPid": eventPid,
       "eventTimeStamp": eventTimeStamp,
       "eventData": eventData,
       "escEventsAttributesTable": escEventsAttributesTable,
       "escEventsAttributesEntry": escEventsAttributesEntry,
       "attributeName": attributeName,
       "attributeValue": attributeValue,
       "scEventsMIBNotifications": scEventsMIBNotifications,
       "escNewEvents": escNewEvents}
)
