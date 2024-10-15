# SNMP MIB module (CISCO-OUTAGE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OUTAGE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:34 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoOutageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280)
)
ciscoOutageMIB.setRevisions(
        ("2005-08-22 00:00",
         "2002-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OutageMonObjectType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("logicalEntity", 5),
          ("physicalEntity", 2),
          ("remoteObject", 4),
          ("swProcess", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOutageMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOutageMIBObjects = _CiscoOutageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1)
)
_COutageBasicInfo_ObjectIdentity = ObjectIdentity
cOutageBasicInfo = _COutageBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1)
)
_COutageApplVersion_Type = SnmpAdminString
_COutageApplVersion_Object = MibScalar
cOutageApplVersion = _COutageApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 1),
    _COutageApplVersion_Type()
)
cOutageApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageApplVersion.setStatus("current")
_COutageNotificationsSent_Type = Counter32
_COutageNotificationsSent_Object = MibScalar
cOutageNotificationsSent = _COutageNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 2),
    _COutageNotificationsSent_Type()
)
cOutageNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageNotificationsSent.setStatus("current")
if mibBuilder.loadTexts:
    cOutageNotificationsSent.setUnits("notifications")


class _COutageNotificationsEnabled_Type(TruthValue):
    """Custom type cOutageNotificationsEnabled based on TruthValue"""


_COutageNotificationsEnabled_Object = MibScalar
cOutageNotificationsEnabled = _COutageNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 3),
    _COutageNotificationsEnabled_Type()
)
cOutageNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOutageNotificationsEnabled.setStatus("current")


class _COutageNotificationFilterEnabled_Type(TruthValue):
    """Custom type cOutageNotificationFilterEnabled based on TruthValue"""


_COutageNotificationFilterEnabled_Object = MibScalar
cOutageNotificationFilterEnabled = _COutageNotificationFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 4),
    _COutageNotificationFilterEnabled_Type()
)
cOutageNotificationFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOutageNotificationFilterEnabled.setStatus("current")
_COutageFilteredEvents_Type = Counter32
_COutageFilteredEvents_Object = MibScalar
cOutageFilteredEvents = _COutageFilteredEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 1, 5),
    _COutageFilteredEvents_Type()
)
cOutageFilteredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageFilteredEvents.setStatus("current")
_COutageHistory_ObjectIdentity = ObjectIdentity
cOutageHistory = _COutageHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2)
)


class _COutageHistTableSize_Type(Unsigned32):
    """Custom type cOutageHistTableSize based on Unsigned32"""
    defaultValue = 100


_COutageHistTableSize_Object = MibScalar
cOutageHistTableSize = _COutageHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 1),
    _COutageHistTableSize_Type()
)
cOutageHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOutageHistTableSize.setStatus("current")
if mibBuilder.loadTexts:
    cOutageHistTableSize.setUnits("entries")
_COutageHistMsgsFlushed_Type = Counter32
_COutageHistMsgsFlushed_Object = MibScalar
cOutageHistMsgsFlushed = _COutageHistMsgsFlushed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 2),
    _COutageHistMsgsFlushed_Type()
)
cOutageHistMsgsFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageHistMsgsFlushed.setStatus("current")
if mibBuilder.loadTexts:
    cOutageHistMsgsFlushed.setUnits("messages")
_COutageHistoryTable_Object = MibTable
cOutageHistoryTable = _COutageHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cOutageHistoryTable.setStatus("current")
_COutageHistoryEntry_Object = MibTableRow
cOutageHistoryEntry = _COutageHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1)
)
cOutageHistoryEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageEventIndex"),
)
if mibBuilder.loadTexts:
    cOutageHistoryEntry.setStatus("current")
_COutageEventIndex_Type = Unsigned32
_COutageEventIndex_Object = MibTableColumn
cOutageEventIndex = _COutageEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 1),
    _COutageEventIndex_Type()
)
cOutageEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageEventIndex.setStatus("current")
_COutageEventObjectType_Type = OutageMonObjectType
_COutageEventObjectType_Object = MibTableColumn
cOutageEventObjectType = _COutageEventObjectType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 2),
    _COutageEventObjectType_Type()
)
cOutageEventObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventObjectType.setStatus("current")
_COutageEventMonObjectIndex_Type = Unsigned32
_COutageEventMonObjectIndex_Object = MibTableColumn
cOutageEventMonObjectIndex = _COutageEventMonObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 3),
    _COutageEventMonObjectIndex_Type()
)
cOutageEventMonObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventMonObjectIndex.setStatus("current")
_COutageEventTypeIndex_Type = Unsigned32
_COutageEventTypeIndex_Object = MibTableColumn
cOutageEventTypeIndex = _COutageEventTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 4),
    _COutageEventTypeIndex_Type()
)
cOutageEventTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventTypeIndex.setStatus("current")
_COutageEventTime_Type = DateAndTime
_COutageEventTime_Object = MibTableColumn
cOutageEventTime = _COutageEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 5),
    _COutageEventTime_Type()
)
cOutageEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventTime.setStatus("current")
_COutageEventInterval_Type = Unsigned32
_COutageEventInterval_Object = MibTableColumn
cOutageEventInterval = _COutageEventInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 2, 3, 1, 6),
    _COutageEventInterval_Type()
)
cOutageEventInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventInterval.setStatus("current")
_COutageDescription_ObjectIdentity = ObjectIdentity
cOutageDescription = _COutageDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3)
)
_COutageEventTypeMapTable_Object = MibTable
cOutageEventTypeMapTable = _COutageEventTypeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cOutageEventTypeMapTable.setStatus("current")
_COutageEventTypeMapEntry_Object = MibTableRow
cOutageEventTypeMapEntry = _COutageEventTypeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1)
)
cOutageEventTypeMapEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeMapIndex"),
)
if mibBuilder.loadTexts:
    cOutageEventTypeMapEntry.setStatus("current")
_COutageEventTypeMapIndex_Type = Unsigned32
_COutageEventTypeMapIndex_Object = MibTableColumn
cOutageEventTypeMapIndex = _COutageEventTypeMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 1),
    _COutageEventTypeMapIndex_Type()
)
cOutageEventTypeMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageEventTypeMapIndex.setStatus("current")


class _COutageEventTypeName_Type(SnmpAdminString):
    """Custom type cOutageEventTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_COutageEventTypeName_Type.__name__ = "SnmpAdminString"
_COutageEventTypeName_Object = MibTableColumn
cOutageEventTypeName = _COutageEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 2),
    _COutageEventTypeName_Type()
)
cOutageEventTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventTypeName.setStatus("current")
_COutageEventTypeDescrText_Type = SnmpAdminString
_COutageEventTypeDescrText_Object = MibTableColumn
cOutageEventTypeDescrText = _COutageEventTypeDescrText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 3, 1, 1, 3),
    _COutageEventTypeDescrText_Type()
)
cOutageEventTypeDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageEventTypeDescrText.setStatus("current")
_COutageMonObject_ObjectIdentity = ObjectIdentity
cOutageMonObject = _COutageMonObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4)
)
_COutageObjectTable_Object = MibTable
cOutageObjectTable = _COutageObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cOutageObjectTable.setStatus("current")
_COutageObjectEntry_Object = MibTableRow
cOutageObjectEntry = _COutageObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1)
)
cOutageObjectEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageObjectType"),
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageMonitoredObjectIndex"),
)
if mibBuilder.loadTexts:
    cOutageObjectEntry.setStatus("current")
_COutageObjectType_Type = OutageMonObjectType
_COutageObjectType_Object = MibTableColumn
cOutageObjectType = _COutageObjectType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 1),
    _COutageObjectType_Type()
)
cOutageObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageObjectType.setStatus("current")
_COutageMonitoredObjectIndex_Type = Unsigned32
_COutageMonitoredObjectIndex_Object = MibTableColumn
cOutageMonitoredObjectIndex = _COutageMonitoredObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 2),
    _COutageMonitoredObjectIndex_Type()
)
cOutageMonitoredObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageMonitoredObjectIndex.setStatus("current")


class _COutageCurrentStatus_Type(Integer32):
    """Custom type cOutageCurrentStatus based on Integer32"""
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


_COutageCurrentStatus_Type.__name__ = "Integer32"
_COutageCurrentStatus_Object = MibTableColumn
cOutageCurrentStatus = _COutageCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 3),
    _COutageCurrentStatus_Type()
)
cOutageCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageCurrentStatus.setStatus("current")
_COutageAOTSinceMeasureStarted_Type = Unsigned32
_COutageAOTSinceMeasureStarted_Object = MibTableColumn
cOutageAOTSinceMeasureStarted = _COutageAOTSinceMeasureStarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 4),
    _COutageAOTSinceMeasureStarted_Type()
)
cOutageAOTSinceMeasureStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageAOTSinceMeasureStarted.setStatus("current")
_COutageNAFSinceMeasureStarted_Type = Unsigned32
_COutageNAFSinceMeasureStarted_Object = MibTableColumn
cOutageNAFSinceMeasureStarted = _COutageNAFSinceMeasureStarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 5),
    _COutageNAFSinceMeasureStarted_Type()
)
cOutageNAFSinceMeasureStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageNAFSinceMeasureStarted.setStatus("current")
_COutageRecordingStartTime_Type = DateAndTime
_COutageRecordingStartTime_Object = MibTableColumn
cOutageRecordingStartTime = _COutageRecordingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 4, 1, 1, 6),
    _COutageRecordingStartTime_Type()
)
cOutageRecordingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageRecordingStartTime.setStatus("current")
_COutageCpmMapping_ObjectIdentity = ObjectIdentity
cOutageCpmMapping = _COutageCpmMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5)
)
_COutageCpmMapTable_Object = MibTable
cOutageCpmMapTable = _COutageCpmMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cOutageCpmMapTable.setStatus("current")
_COutageCpmMapEntry_Object = MibTableRow
cOutageCpmMapEntry = _COutageCpmMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1)
)
cOutageCpmMapEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmMapIndex"),
)
if mibBuilder.loadTexts:
    cOutageCpmMapEntry.setStatus("current")
_COutageCpmMapIndex_Type = Unsigned32
_COutageCpmMapIndex_Object = MibTableColumn
cOutageCpmMapIndex = _COutageCpmMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 1),
    _COutageCpmMapIndex_Type()
)
cOutageCpmMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageCpmMapIndex.setStatus("current")
_COutageCpmCPUTotalIndex_Type = Unsigned32
_COutageCpmCPUTotalIndex_Object = MibTableColumn
cOutageCpmCPUTotalIndex = _COutageCpmCPUTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 2),
    _COutageCpmCPUTotalIndex_Type()
)
cOutageCpmCPUTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageCpmCPUTotalIndex.setStatus("current")
_COutageCpmProcessPID_Type = Unsigned32
_COutageCpmProcessPID_Object = MibTableColumn
cOutageCpmProcessPID = _COutageCpmProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 5, 1, 1, 3),
    _COutageCpmProcessPID_Type()
)
cOutageCpmProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageCpmProcessPID.setStatus("current")
_COutageRmtMapping_ObjectIdentity = ObjectIdentity
cOutageRmtMapping = _COutageRmtMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6)
)
_COutageRemoteObjMapTable_Object = MibTable
cOutageRemoteObjMapTable = _COutageRemoteObjMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cOutageRemoteObjMapTable.setStatus("current")
_COutageRemoteObjMapEntry_Object = MibTableRow
cOutageRemoteObjMapEntry = _COutageRemoteObjMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1)
)
cOutageRemoteObjMapEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjMapIndex"),
)
if mibBuilder.loadTexts:
    cOutageRemoteObjMapEntry.setStatus("current")
_COutageRemoteObjMapIndex_Type = Unsigned32
_COutageRemoteObjMapIndex_Object = MibTableColumn
cOutageRemoteObjMapIndex = _COutageRemoteObjMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 1),
    _COutageRemoteObjMapIndex_Type()
)
cOutageRemoteObjMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageRemoteObjMapIndex.setStatus("current")
_COutageRemoteObjIDType_Type = InetAddressType
_COutageRemoteObjIDType_Object = MibTableColumn
cOutageRemoteObjIDType = _COutageRemoteObjIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 2),
    _COutageRemoteObjIDType_Type()
)
cOutageRemoteObjIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageRemoteObjIDType.setStatus("current")
_COutageRemoteObjID_Type = InetAddress
_COutageRemoteObjID_Object = MibTableColumn
cOutageRemoteObjID = _COutageRemoteObjID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 3),
    _COutageRemoteObjID_Type()
)
cOutageRemoteObjID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageRemoteObjID.setStatus("current")
_COutageRemoteObjDescrText_Type = SnmpAdminString
_COutageRemoteObjDescrText_Object = MibTableColumn
cOutageRemoteObjDescrText = _COutageRemoteObjDescrText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 6, 1, 1, 4),
    _COutageRemoteObjDescrText_Type()
)
cOutageRemoteObjDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageRemoteObjDescrText.setStatus("current")
_COutageLntMapping_ObjectIdentity = ObjectIdentity
cOutageLntMapping = _COutageLntMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7)
)
_COutageLogicalObjMapTable_Object = MibTable
cOutageLogicalObjMapTable = _COutageLogicalObjMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cOutageLogicalObjMapTable.setStatus("current")
_COutageLogicalObjMapEntry_Object = MibTableRow
cOutageLogicalObjMapEntry = _COutageLogicalObjMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1)
)
cOutageLogicalObjMapEntry.setIndexNames(
    (0, "CISCO-OUTAGE-MONITOR-MIB", "cOutageLogicalObjMapIndex"),
)
if mibBuilder.loadTexts:
    cOutageLogicalObjMapEntry.setStatus("current")
_COutageLogicalObjMapIndex_Type = Unsigned32
_COutageLogicalObjMapIndex_Object = MibTableColumn
cOutageLogicalObjMapIndex = _COutageLogicalObjMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1, 1),
    _COutageLogicalObjMapIndex_Type()
)
cOutageLogicalObjMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOutageLogicalObjMapIndex.setStatus("current")
_COutageLogicalObjDescrText_Type = SnmpAdminString
_COutageLogicalObjDescrText_Object = MibTableColumn
cOutageLogicalObjDescrText = _COutageLogicalObjDescrText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 1, 7, 1, 1, 2),
    _COutageLogicalObjDescrText_Type()
)
cOutageLogicalObjDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOutageLogicalObjDescrText.setStatus("current")
_CiscoOutageMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoOutageMIBNotificationPrefix = _CiscoOutageMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 2)
)
_CiscoOutageMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoOutageMIBNotifications = _CiscoOutageMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 2, 0)
)
_CiscoOutageMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOutageMIBConformance = _CiscoOutageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3)
)
_CiscoOutageMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOutageMIBCompliances = _CiscoOutageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1)
)
_CiscoOutageMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOutageMIBGroups = _CiscoOutageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2)
)

# Managed Objects groups

ciscoOutageBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 1)
)
ciscoOutageBasicGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageApplVersion"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationsSent"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationsEnabled"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNotificationFilterEnabled"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageFilteredEvents"))
)
if mibBuilder.loadTexts:
    ciscoOutageBasicGroup.setStatus("current")

ciscoEventHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 2)
)
ciscoEventHistoryGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageHistTableSize"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageHistMsgsFlushed"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventObjectType"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventMonObjectIndex"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeIndex"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTime"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventInterval"))
)
if mibBuilder.loadTexts:
    ciscoEventHistoryGroup.setStatus("current")

ciscoEventDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 3)
)
ciscoEventDescrGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeName"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeDescrText"))
)
if mibBuilder.loadTexts:
    ciscoEventDescrGroup.setStatus("current")

ciscoObjectOutageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 4)
)
ciscoObjectOutageGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCurrentStatus"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageAOTSinceMeasureStarted"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNAFSinceMeasureStarted"))
)
if mibBuilder.loadTexts:
    ciscoObjectOutageGroup.setStatus("deprecated")

ciscoCpmMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 5)
)
ciscoCpmMappingGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmCPUTotalIndex"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageCpmProcessPID"))
)
if mibBuilder.loadTexts:
    ciscoCpmMappingGroup.setStatus("current")

ciscoRmtMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 6)
)
ciscoRmtMappingGroup.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjIDType"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjID"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRemoteObjDescrText"))
)
if mibBuilder.loadTexts:
    ciscoRmtMappingGroup.setStatus("current")

ciscoObjectOutageGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 8)
)
ciscoObjectOutageGroupRev.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageCurrentStatus"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageRecordingStartTime"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageAOTSinceMeasureStarted"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageNAFSinceMeasureStarted"))
)
if mibBuilder.loadTexts:
    ciscoObjectOutageGroupRev.setStatus("current")

ciscoLntMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 9)
)
ciscoLntMappingGroup.setObjects(
    ("CISCO-OUTAGE-MONITOR-MIB", "cOutageLogicalObjDescrText")
)
if mibBuilder.loadTexts:
    ciscoLntMappingGroup.setStatus("current")


# Notification objects

ciscoOutageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 2, 0, 1)
)
ciscoOutageEvent.setObjects(
      *(("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventObjectType"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventMonObjectIndex"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTypeIndex"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventTime"),
        ("CISCO-OUTAGE-MONITOR-MIB", "cOutageEventInterval"))
)
if mibBuilder.loadTexts:
    ciscoOutageEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoOutageNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 2, 7)
)
ciscoOutageNotificationsGroup.setObjects(
    ("CISCO-OUTAGE-MONITOR-MIB", "ciscoOutageEvent")
)
if mibBuilder.loadTexts:
    ciscoOutageNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOutageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOutageMIBCompliance.setStatus(
        "deprecated"
    )

ciscoOutageMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 280, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoOutageMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OUTAGE-MONITOR-MIB",
    **{"OutageMonObjectType": OutageMonObjectType,
       "ciscoOutageMIB": ciscoOutageMIB,
       "ciscoOutageMIBObjects": ciscoOutageMIBObjects,
       "cOutageBasicInfo": cOutageBasicInfo,
       "cOutageApplVersion": cOutageApplVersion,
       "cOutageNotificationsSent": cOutageNotificationsSent,
       "cOutageNotificationsEnabled": cOutageNotificationsEnabled,
       "cOutageNotificationFilterEnabled": cOutageNotificationFilterEnabled,
       "cOutageFilteredEvents": cOutageFilteredEvents,
       "cOutageHistory": cOutageHistory,
       "cOutageHistTableSize": cOutageHistTableSize,
       "cOutageHistMsgsFlushed": cOutageHistMsgsFlushed,
       "cOutageHistoryTable": cOutageHistoryTable,
       "cOutageHistoryEntry": cOutageHistoryEntry,
       "cOutageEventIndex": cOutageEventIndex,
       "cOutageEventObjectType": cOutageEventObjectType,
       "cOutageEventMonObjectIndex": cOutageEventMonObjectIndex,
       "cOutageEventTypeIndex": cOutageEventTypeIndex,
       "cOutageEventTime": cOutageEventTime,
       "cOutageEventInterval": cOutageEventInterval,
       "cOutageDescription": cOutageDescription,
       "cOutageEventTypeMapTable": cOutageEventTypeMapTable,
       "cOutageEventTypeMapEntry": cOutageEventTypeMapEntry,
       "cOutageEventTypeMapIndex": cOutageEventTypeMapIndex,
       "cOutageEventTypeName": cOutageEventTypeName,
       "cOutageEventTypeDescrText": cOutageEventTypeDescrText,
       "cOutageMonObject": cOutageMonObject,
       "cOutageObjectTable": cOutageObjectTable,
       "cOutageObjectEntry": cOutageObjectEntry,
       "cOutageObjectType": cOutageObjectType,
       "cOutageMonitoredObjectIndex": cOutageMonitoredObjectIndex,
       "cOutageCurrentStatus": cOutageCurrentStatus,
       "cOutageAOTSinceMeasureStarted": cOutageAOTSinceMeasureStarted,
       "cOutageNAFSinceMeasureStarted": cOutageNAFSinceMeasureStarted,
       "cOutageRecordingStartTime": cOutageRecordingStartTime,
       "cOutageCpmMapping": cOutageCpmMapping,
       "cOutageCpmMapTable": cOutageCpmMapTable,
       "cOutageCpmMapEntry": cOutageCpmMapEntry,
       "cOutageCpmMapIndex": cOutageCpmMapIndex,
       "cOutageCpmCPUTotalIndex": cOutageCpmCPUTotalIndex,
       "cOutageCpmProcessPID": cOutageCpmProcessPID,
       "cOutageRmtMapping": cOutageRmtMapping,
       "cOutageRemoteObjMapTable": cOutageRemoteObjMapTable,
       "cOutageRemoteObjMapEntry": cOutageRemoteObjMapEntry,
       "cOutageRemoteObjMapIndex": cOutageRemoteObjMapIndex,
       "cOutageRemoteObjIDType": cOutageRemoteObjIDType,
       "cOutageRemoteObjID": cOutageRemoteObjID,
       "cOutageRemoteObjDescrText": cOutageRemoteObjDescrText,
       "cOutageLntMapping": cOutageLntMapping,
       "cOutageLogicalObjMapTable": cOutageLogicalObjMapTable,
       "cOutageLogicalObjMapEntry": cOutageLogicalObjMapEntry,
       "cOutageLogicalObjMapIndex": cOutageLogicalObjMapIndex,
       "cOutageLogicalObjDescrText": cOutageLogicalObjDescrText,
       "ciscoOutageMIBNotificationPrefix": ciscoOutageMIBNotificationPrefix,
       "ciscoOutageMIBNotifications": ciscoOutageMIBNotifications,
       "ciscoOutageEvent": ciscoOutageEvent,
       "ciscoOutageMIBConformance": ciscoOutageMIBConformance,
       "ciscoOutageMIBCompliances": ciscoOutageMIBCompliances,
       "ciscoOutageMIBCompliance": ciscoOutageMIBCompliance,
       "ciscoOutageMIBComplianceRev1": ciscoOutageMIBComplianceRev1,
       "ciscoOutageMIBGroups": ciscoOutageMIBGroups,
       "ciscoOutageBasicGroup": ciscoOutageBasicGroup,
       "ciscoEventHistoryGroup": ciscoEventHistoryGroup,
       "ciscoEventDescrGroup": ciscoEventDescrGroup,
       "ciscoObjectOutageGroup": ciscoObjectOutageGroup,
       "ciscoCpmMappingGroup": ciscoCpmMappingGroup,
       "ciscoRmtMappingGroup": ciscoRmtMappingGroup,
       "ciscoOutageNotificationsGroup": ciscoOutageNotificationsGroup,
       "ciscoObjectOutageGroupRev": ciscoObjectOutageGroupRev,
       "ciscoLntMappingGroup": ciscoLntMappingGroup}
)
