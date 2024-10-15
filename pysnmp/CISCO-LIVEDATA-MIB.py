# SNMP MIB module (CISCO-LIVEDATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LIVEDATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:05 2024
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

ciscoLivedataMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814)
)
ciscoLivedataMIB.setRevisions(
        ("2013-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CldIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CldSeverity(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLivedataMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLivedataMIBNotifs = _CiscoLivedataMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 0)
)
_CiscoLivedataMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLivedataMIBObjects = _CiscoLivedataMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1)
)
_CldGeneral_ObjectIdentity = ObjectIdentity
cldGeneral = _CldGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1)
)
_CldServerName_Type = SnmpAdminString
_CldServerName_Object = MibScalar
cldServerName = _CldServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 1),
    _CldServerName_Type()
)
cldServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldServerName.setStatus("current")
_CldDescription_Type = SnmpAdminString
_CldDescription_Object = MibScalar
cldDescription = _CldDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 2),
    _CldDescription_Type()
)
cldDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDescription.setStatus("current")
_CldVersion_Type = SnmpAdminString
_CldVersion_Object = MibScalar
cldVersion = _CldVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 3),
    _CldVersion_Type()
)
cldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldVersion.setStatus("current")
_CldStartTime_Type = DateAndTime
_CldStartTime_Object = MibScalar
cldStartTime = _CldStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 4),
    _CldStartTime_Type()
)
cldStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldStartTime.setStatus("current")
_CldTimeZoneName_Type = SnmpAdminString
_CldTimeZoneName_Object = MibScalar
cldTimeZoneName = _CldTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 5),
    _CldTimeZoneName_Type()
)
cldTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldTimeZoneName.setStatus("current")
_CldTimeZoneOffset_Type = Integer32
_CldTimeZoneOffset_Object = MibScalar
cldTimeZoneOffset = _CldTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 6),
    _CldTimeZoneOffset_Type()
)
cldTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldTimeZoneOffset.setStatus("current")
if mibBuilder.loadTexts:
    cldTimeZoneOffset.setUnits("minutes")


class _CldEventNotifEnable_Type(TruthValue):
    """Custom type cldEventNotifEnable based on TruthValue"""


_CldEventNotifEnable_Object = MibScalar
cldEventNotifEnable = _CldEventNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 1, 7),
    _CldEventNotifEnable_Type()
)
cldEventNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldEventNotifEnable.setStatus("current")
_CldCluster_ObjectIdentity = ObjectIdentity
cldCluster = _CldCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 2)
)
_CldClusterID_Type = SnmpAdminString
_CldClusterID_Object = MibScalar
cldClusterID = _CldClusterID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 2, 1),
    _CldClusterID_Type()
)
cldClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldClusterID.setStatus("current")


class _CldClusterStatus_Type(Integer32):
    """Custom type cldClusterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("isolatedActive", 3),
          ("isolatedStandby", 4),
          ("outOfService", 6),
          ("pairedActive", 1),
          ("pairedStandby", 2),
          ("testing", 5))
    )


_CldClusterStatus_Type.__name__ = "Integer32"
_CldClusterStatus_Object = MibScalar
cldClusterStatus = _CldClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 2, 2),
    _CldClusterStatus_Type()
)
cldClusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldClusterStatus.setStatus("current")
_CldClusterAddress_Type = SnmpAdminString
_CldClusterAddress_Object = MibScalar
cldClusterAddress = _CldClusterAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 2, 3),
    _CldClusterAddress_Type()
)
cldClusterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldClusterAddress.setStatus("current")
_CldServices_ObjectIdentity = ObjectIdentity
cldServices = _CldServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3)
)
_CldServiceTable_Object = MibTable
cldServiceTable = _CldServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cldServiceTable.setStatus("current")
_CldServiceEntry_Object = MibTableRow
cldServiceEntry = _CldServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1, 1)
)
cldServiceEntry.setIndexNames(
    (0, "CISCO-LIVEDATA-MIB", "cldServiceIndex"),
)
if mibBuilder.loadTexts:
    cldServiceEntry.setStatus("current")
_CldServiceIndex_Type = CldIndex
_CldServiceIndex_Object = MibTableColumn
cldServiceIndex = _CldServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1, 1, 1),
    _CldServiceIndex_Type()
)
cldServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldServiceIndex.setStatus("current")
_CldServiceName_Type = SnmpAdminString
_CldServiceName_Object = MibTableColumn
cldServiceName = _CldServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1, 1, 2),
    _CldServiceName_Type()
)
cldServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldServiceName.setStatus("current")


class _CldServiceState_Type(Integer32):
    """Custom type cldServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("disabled", 2),
          ("started", 4),
          ("starting", 3),
          ("stopped", 7),
          ("stopping", 6),
          ("unknown", 1))
    )


_CldServiceState_Type.__name__ = "Integer32"
_CldServiceState_Object = MibTableColumn
cldServiceState = _CldServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1, 1, 3),
    _CldServiceState_Type()
)
cldServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldServiceState.setStatus("current")
_CldServiceUpTime_Type = DateAndTime
_CldServiceUpTime_Object = MibTableColumn
cldServiceUpTime = _CldServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 3, 1, 1, 4),
    _CldServiceUpTime_Type()
)
cldServiceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldServiceUpTime.setStatus("current")
_CldReportingConnections_ObjectIdentity = ObjectIdentity
cldReportingConnections = _CldReportingConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4)
)
_CldReportingConnectionTable_Object = MibTable
cldReportingConnectionTable = _CldReportingConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cldReportingConnectionTable.setStatus("current")
_CldReportingConnectionEntry_Object = MibTableRow
cldReportingConnectionEntry = _CldReportingConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1)
)
cldReportingConnectionEntry.setIndexNames(
    (0, "CISCO-LIVEDATA-MIB", "cldRptConnIndex"),
)
if mibBuilder.loadTexts:
    cldReportingConnectionEntry.setStatus("current")
_CldRptConnIndex_Type = CldIndex
_CldRptConnIndex_Object = MibTableColumn
cldRptConnIndex = _CldRptConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 1),
    _CldRptConnIndex_Type()
)
cldRptConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldRptConnIndex.setStatus("current")
_CldRptConnServerID_Type = SnmpAdminString
_CldRptConnServerID_Object = MibTableColumn
cldRptConnServerID = _CldRptConnServerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 2),
    _CldRptConnServerID_Type()
)
cldRptConnServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnServerID.setStatus("current")
_CldRptConnServerAddress_Type = SnmpAdminString
_CldRptConnServerAddress_Object = MibTableColumn
cldRptConnServerAddress = _CldRptConnServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 3),
    _CldRptConnServerAddress_Type()
)
cldRptConnServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnServerAddress.setStatus("current")


class _CldRptConnState_Type(Integer32):
    """Custom type cldRptConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_CldRptConnState_Type.__name__ = "Integer32"
_CldRptConnState_Object = MibTableColumn
cldRptConnState = _CldRptConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 4),
    _CldRptConnState_Type()
)
cldRptConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnState.setStatus("current")
_CldRptConnStateTime_Type = DateAndTime
_CldRptConnStateTime_Object = MibTableColumn
cldRptConnStateTime = _CldRptConnStateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 5),
    _CldRptConnStateTime_Type()
)
cldRptConnStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnStateTime.setStatus("current")
_CldRptConnEventRate_Type = Gauge32
_CldRptConnEventRate_Object = MibTableColumn
cldRptConnEventRate = _CldRptConnEventRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 6),
    _CldRptConnEventRate_Type()
)
cldRptConnEventRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnEventRate.setStatus("current")
if mibBuilder.loadTexts:
    cldRptConnEventRate.setUnits("events")
_CldRptConnHeartbeatRTT_Type = Gauge32
_CldRptConnHeartbeatRTT_Object = MibTableColumn
cldRptConnHeartbeatRTT = _CldRptConnHeartbeatRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 7),
    _CldRptConnHeartbeatRTT_Type()
)
cldRptConnHeartbeatRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnHeartbeatRTT.setStatus("current")
if mibBuilder.loadTexts:
    cldRptConnHeartbeatRTT.setUnits("milliseconds")
_CldRptConnSocketConnects_Type = Counter32
_CldRptConnSocketConnects_Object = MibTableColumn
cldRptConnSocketConnects = _CldRptConnSocketConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 8),
    _CldRptConnSocketConnects_Type()
)
cldRptConnSocketConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnSocketConnects.setStatus("current")
_CldRptConnSocketDisconnects_Type = Counter32
_CldRptConnSocketDisconnects_Object = MibTableColumn
cldRptConnSocketDisconnects = _CldRptConnSocketDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 9),
    _CldRptConnSocketDisconnects_Type()
)
cldRptConnSocketDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnSocketDisconnects.setStatus("current")
_CldRptConnMessagesDiscarded_Type = Counter32
_CldRptConnMessagesDiscarded_Object = MibTableColumn
cldRptConnMessagesDiscarded = _CldRptConnMessagesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 10),
    _CldRptConnMessagesDiscarded_Type()
)
cldRptConnMessagesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnMessagesDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    cldRptConnMessagesDiscarded.setUnits("messages")
_CldRptConnDSCP_Type = Integer32
_CldRptConnDSCP_Object = MibTableColumn
cldRptConnDSCP = _CldRptConnDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 4, 1, 1, 11),
    _CldRptConnDSCP_Type()
)
cldRptConnDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRptConnDSCP.setStatus("current")
_CldEvents_ObjectIdentity = ObjectIdentity
cldEvents = _CldEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5)
)
_CldEventTable_Object = MibTable
cldEventTable = _CldEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cldEventTable.setStatus("current")
_CldEventEntry_Object = MibTableRow
cldEventEntry = _CldEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1)
)
cldEventEntry.setIndexNames(
    (0, "CISCO-LIVEDATA-MIB", "cldEventIndex"),
)
if mibBuilder.loadTexts:
    cldEventEntry.setStatus("current")
_CldEventIndex_Type = CldIndex
_CldEventIndex_Object = MibTableColumn
cldEventIndex = _CldEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 1),
    _CldEventIndex_Type()
)
cldEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldEventIndex.setStatus("current")
_CldEventID_Type = Unsigned32
_CldEventID_Object = MibTableColumn
cldEventID = _CldEventID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 2),
    _CldEventID_Type()
)
cldEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventID.setStatus("current")
_CldEventAppName_Type = SnmpAdminString
_CldEventAppName_Object = MibTableColumn
cldEventAppName = _CldEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 3),
    _CldEventAppName_Type()
)
cldEventAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventAppName.setStatus("current")
_CldEventName_Type = SnmpAdminString
_CldEventName_Object = MibTableColumn
cldEventName = _CldEventName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 4),
    _CldEventName_Type()
)
cldEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventName.setStatus("current")


class _CldEventState_Type(Integer32):
    """Custom type cldEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("raise", 1))
    )


_CldEventState_Type.__name__ = "Integer32"
_CldEventState_Object = MibTableColumn
cldEventState = _CldEventState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 5),
    _CldEventState_Type()
)
cldEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventState.setStatus("current")
_CldEventSeverity_Type = CldSeverity
_CldEventSeverity_Object = MibTableColumn
cldEventSeverity = _CldEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 6),
    _CldEventSeverity_Type()
)
cldEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventSeverity.setStatus("current")
_CldEventTimestamp_Type = DateAndTime
_CldEventTimestamp_Object = MibTableColumn
cldEventTimestamp = _CldEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 7),
    _CldEventTimestamp_Type()
)
cldEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventTimestamp.setStatus("current")
_CldEventText_Type = SnmpAdminString
_CldEventText_Object = MibTableColumn
cldEventText = _CldEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 1, 5, 1, 1, 8),
    _CldEventText_Type()
)
cldEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldEventText.setStatus("current")
_CiscoLivedataMIBConform_ObjectIdentity = ObjectIdentity
ciscoLivedataMIBConform = _CiscoLivedataMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2)
)
_CiscoLivedataMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLivedataMIBCompliances = _CiscoLivedataMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 1)
)
_CiscoLivedataMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLivedataMIBGroups = _CiscoLivedataMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2)
)

# Managed Objects groups

cldGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 1)
)
cldGeneralGroup.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldServerName"),
        ("CISCO-LIVEDATA-MIB", "cldDescription"),
        ("CISCO-LIVEDATA-MIB", "cldVersion"),
        ("CISCO-LIVEDATA-MIB", "cldStartTime"),
        ("CISCO-LIVEDATA-MIB", "cldTimeZoneName"),
        ("CISCO-LIVEDATA-MIB", "cldTimeZoneOffset"),
        ("CISCO-LIVEDATA-MIB", "cldEventNotifEnable"))
)
if mibBuilder.loadTexts:
    cldGeneralGroup.setStatus("current")

cldClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 2)
)
cldClusterGroup.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldClusterID"),
        ("CISCO-LIVEDATA-MIB", "cldClusterStatus"),
        ("CISCO-LIVEDATA-MIB", "cldClusterAddress"))
)
if mibBuilder.loadTexts:
    cldClusterGroup.setStatus("current")

cldServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 3)
)
cldServicesGroup.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldServiceName"),
        ("CISCO-LIVEDATA-MIB", "cldServiceState"),
        ("CISCO-LIVEDATA-MIB", "cldServiceUpTime"))
)
if mibBuilder.loadTexts:
    cldServicesGroup.setStatus("current")

cldRptConnectionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 4)
)
cldRptConnectionsGroup.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldRptConnServerID"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnServerAddress"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnState"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnStateTime"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnEventRate"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnHeartbeatRTT"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnSocketConnects"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnSocketDisconnects"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnMessagesDiscarded"),
        ("CISCO-LIVEDATA-MIB", "cldRptConnDSCP"))
)
if mibBuilder.loadTexts:
    cldRptConnectionsGroup.setStatus("current")

cldEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 5)
)
cldEventsGroup.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldEventID"),
        ("CISCO-LIVEDATA-MIB", "cldEventAppName"),
        ("CISCO-LIVEDATA-MIB", "cldEventName"),
        ("CISCO-LIVEDATA-MIB", "cldEventState"),
        ("CISCO-LIVEDATA-MIB", "cldEventSeverity"),
        ("CISCO-LIVEDATA-MIB", "cldEventTimestamp"),
        ("CISCO-LIVEDATA-MIB", "cldEventText"))
)
if mibBuilder.loadTexts:
    cldEventsGroup.setStatus("current")


# Notification objects

cldEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 0, 1)
)
cldEventNotif.setObjects(
      *(("CISCO-LIVEDATA-MIB", "cldEventID"),
        ("CISCO-LIVEDATA-MIB", "cldServerName"),
        ("CISCO-LIVEDATA-MIB", "cldEventAppName"),
        ("CISCO-LIVEDATA-MIB", "cldEventName"),
        ("CISCO-LIVEDATA-MIB", "cldEventState"),
        ("CISCO-LIVEDATA-MIB", "cldEventSeverity"),
        ("CISCO-LIVEDATA-MIB", "cldEventTimestamp"),
        ("CISCO-LIVEDATA-MIB", "cldEventText"))
)
if mibBuilder.loadTexts:
    cldEventNotif.setStatus(
        "current"
    )


# Notifications groups

cldMIBEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 2, 6)
)
cldMIBEventGroup.setObjects(
    ("CISCO-LIVEDATA-MIB", "cldEventNotif")
)
if mibBuilder.loadTexts:
    cldMIBEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLivedataMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 814, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLivedataMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LIVEDATA-MIB",
    **{"CldIndex": CldIndex,
       "CldSeverity": CldSeverity,
       "ciscoLivedataMIB": ciscoLivedataMIB,
       "ciscoLivedataMIBNotifs": ciscoLivedataMIBNotifs,
       "cldEventNotif": cldEventNotif,
       "ciscoLivedataMIBObjects": ciscoLivedataMIBObjects,
       "cldGeneral": cldGeneral,
       "cldServerName": cldServerName,
       "cldDescription": cldDescription,
       "cldVersion": cldVersion,
       "cldStartTime": cldStartTime,
       "cldTimeZoneName": cldTimeZoneName,
       "cldTimeZoneOffset": cldTimeZoneOffset,
       "cldEventNotifEnable": cldEventNotifEnable,
       "cldCluster": cldCluster,
       "cldClusterID": cldClusterID,
       "cldClusterStatus": cldClusterStatus,
       "cldClusterAddress": cldClusterAddress,
       "cldServices": cldServices,
       "cldServiceTable": cldServiceTable,
       "cldServiceEntry": cldServiceEntry,
       "cldServiceIndex": cldServiceIndex,
       "cldServiceName": cldServiceName,
       "cldServiceState": cldServiceState,
       "cldServiceUpTime": cldServiceUpTime,
       "cldReportingConnections": cldReportingConnections,
       "cldReportingConnectionTable": cldReportingConnectionTable,
       "cldReportingConnectionEntry": cldReportingConnectionEntry,
       "cldRptConnIndex": cldRptConnIndex,
       "cldRptConnServerID": cldRptConnServerID,
       "cldRptConnServerAddress": cldRptConnServerAddress,
       "cldRptConnState": cldRptConnState,
       "cldRptConnStateTime": cldRptConnStateTime,
       "cldRptConnEventRate": cldRptConnEventRate,
       "cldRptConnHeartbeatRTT": cldRptConnHeartbeatRTT,
       "cldRptConnSocketConnects": cldRptConnSocketConnects,
       "cldRptConnSocketDisconnects": cldRptConnSocketDisconnects,
       "cldRptConnMessagesDiscarded": cldRptConnMessagesDiscarded,
       "cldRptConnDSCP": cldRptConnDSCP,
       "cldEvents": cldEvents,
       "cldEventTable": cldEventTable,
       "cldEventEntry": cldEventEntry,
       "cldEventIndex": cldEventIndex,
       "cldEventID": cldEventID,
       "cldEventAppName": cldEventAppName,
       "cldEventName": cldEventName,
       "cldEventState": cldEventState,
       "cldEventSeverity": cldEventSeverity,
       "cldEventTimestamp": cldEventTimestamp,
       "cldEventText": cldEventText,
       "ciscoLivedataMIBConform": ciscoLivedataMIBConform,
       "ciscoLivedataMIBCompliances": ciscoLivedataMIBCompliances,
       "ciscoLivedataMIBCompliance": ciscoLivedataMIBCompliance,
       "ciscoLivedataMIBGroups": ciscoLivedataMIBGroups,
       "cldGeneralGroup": cldGeneralGroup,
       "cldClusterGroup": cldClusterGroup,
       "cldServicesGroup": cldServicesGroup,
       "cldRptConnectionsGroup": cldRptConnectionsGroup,
       "cldEventsGroup": cldEventsGroup,
       "cldMIBEventGroup": cldMIBEventGroup}
)
