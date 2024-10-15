# SNMP MIB module (CISCO-DOCS-REMOTE-QUERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOCS-REMOTE-QUERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:44 2024
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

(cdxCmCpeMacAddress,) = mibBuilder.importSymbols(
    "CISCO-DOCS-EXT-MIB",
    "cdxCmCpeMacAddress")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDocsRemoteQueryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59)
)
ciscoDocsRemoteQueryMIB.setRevisions(
        ("2004-08-06 00:00",
         "2000-12-21 00:00",
         "2000-03-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDocsRemQueryMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDocsRemQueryMIBObjects = _CiscoDocsRemQueryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1)
)
_CdrqPoller_ObjectIdentity = ObjectIdentity
cdrqPoller = _CdrqPoller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1)
)
_CdrqCmtsCmPollerEnable_Type = TruthValue
_CdrqCmtsCmPollerEnable_Object = MibScalar
cdrqCmtsCmPollerEnable = _CdrqCmtsCmPollerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 1),
    _CdrqCmtsCmPollerEnable_Type()
)
cdrqCmtsCmPollerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerEnable.setStatus("current")


class _CdrqCmtsCmPollerInterval_Type(TimeInterval):
    """Custom type cdrqCmtsCmPollerInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8640000),
    )


_CdrqCmtsCmPollerInterval_Type.__name__ = "TimeInterval"
_CdrqCmtsCmPollerInterval_Object = MibScalar
cdrqCmtsCmPollerInterval = _CdrqCmtsCmPollerInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 2),
    _CdrqCmtsCmPollerInterval_Type()
)
cdrqCmtsCmPollerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerInterval.setStatus("current")
_CdrqCmtsCmPollerCommunity_Type = OctetString
_CdrqCmtsCmPollerCommunity_Object = MibScalar
cdrqCmtsCmPollerCommunity = _CdrqCmtsCmPollerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 3),
    _CdrqCmtsCmPollerCommunity_Type()
)
cdrqCmtsCmPollerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerCommunity.setStatus("current")
_CdrqCmtsCmPollerContextEngineID_Type = SnmpEngineID
_CdrqCmtsCmPollerContextEngineID_Object = MibScalar
cdrqCmtsCmPollerContextEngineID = _CdrqCmtsCmPollerContextEngineID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 4),
    _CdrqCmtsCmPollerContextEngineID_Type()
)
cdrqCmtsCmPollerContextEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerContextEngineID.setStatus("current")


class _CdrqCmtsCmPollerContextName_Type(SnmpAdminString):
    """Custom type cdrqCmtsCmPollerContextName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdrqCmtsCmPollerContextName_Type.__name__ = "SnmpAdminString"
_CdrqCmtsCmPollerContextName_Object = MibScalar
cdrqCmtsCmPollerContextName = _CdrqCmtsCmPollerContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 5),
    _CdrqCmtsCmPollerContextName_Type()
)
cdrqCmtsCmPollerContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerContextName.setStatus("current")
_CdrqCmtsCmPollerStartTime_Type = TimeStamp
_CdrqCmtsCmPollerStartTime_Object = MibScalar
cdrqCmtsCmPollerStartTime = _CdrqCmtsCmPollerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 6),
    _CdrqCmtsCmPollerStartTime_Type()
)
cdrqCmtsCmPollerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerStartTime.setStatus("current")
_CdrqCmtsCmPollerStopTime_Type = TimeStamp
_CdrqCmtsCmPollerStopTime_Object = MibScalar
cdrqCmtsCmPollerStopTime = _CdrqCmtsCmPollerStopTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 1, 7),
    _CdrqCmtsCmPollerStopTime_Type()
)
cdrqCmtsCmPollerStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollerStopTime.setStatus("current")
_CdrqCM_ObjectIdentity = ObjectIdentity
cdrqCM = _CdrqCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2)
)
_CdrqCmtsCmStatusTable_Object = MibTable
cdrqCmtsCmStatusTable = _CdrqCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdrqCmtsCmStatusTable.setStatus("current")
_CdrqCmtsCmStatusEntry_Object = MibTableRow
cdrqCmtsCmStatusEntry = _CdrqCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1)
)
cdrqCmtsCmStatusEntry.setIndexNames(
    (0, "CISCO-DOCS-EXT-MIB", "cdxCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    cdrqCmtsCmStatusEntry.setStatus("current")
_CdrqCmtsCmDownChannelPower_Type = TenthdBmV
_CdrqCmtsCmDownChannelPower_Object = MibTableColumn
cdrqCmtsCmDownChannelPower = _CdrqCmtsCmDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 1),
    _CdrqCmtsCmDownChannelPower_Type()
)
cdrqCmtsCmDownChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cdrqCmtsCmDownChannelPower.setUnits("dBmV")
_CdrqCmtsCmStatusTxPower_Type = TenthdBmV
_CdrqCmtsCmStatusTxPower_Object = MibTableColumn
cdrqCmtsCmStatusTxPower = _CdrqCmtsCmStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 2),
    _CdrqCmtsCmStatusTxPower_Type()
)
cdrqCmtsCmStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmStatusTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cdrqCmtsCmStatusTxPower.setUnits("dBmV")
_CdrqCmtsCmUpChnlTxTimingOffset_Type = Unsigned32
_CdrqCmtsCmUpChnlTxTimingOffset_Object = MibTableColumn
cdrqCmtsCmUpChnlTxTimingOffset = _CdrqCmtsCmUpChnlTxTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 3),
    _CdrqCmtsCmUpChnlTxTimingOffset_Type()
)
cdrqCmtsCmUpChnlTxTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmUpChnlTxTimingOffset.setStatus("current")
_CdrqCmtsCmSigQSignalNoise_Type = TenthdB
_CdrqCmtsCmSigQSignalNoise_Object = MibTableColumn
cdrqCmtsCmSigQSignalNoise = _CdrqCmtsCmSigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 4),
    _CdrqCmtsCmSigQSignalNoise_Type()
)
cdrqCmtsCmSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmSigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    cdrqCmtsCmSigQSignalNoise.setUnits("dB")


class _CdrqCmtsCmSigQMicroreflections_Type(Integer32):
    """Custom type cdrqCmtsCmSigQMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdrqCmtsCmSigQMicroreflections_Type.__name__ = "Integer32"
_CdrqCmtsCmSigQMicroreflections_Object = MibTableColumn
cdrqCmtsCmSigQMicroreflections = _CdrqCmtsCmSigQMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 5),
    _CdrqCmtsCmSigQMicroreflections_Type()
)
cdrqCmtsCmSigQMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmSigQMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    cdrqCmtsCmSigQMicroreflections.setUnits("dBc")
_CdrqCmtsCmPollTime_Type = TimeStamp
_CdrqCmtsCmPollTime_Object = MibTableColumn
cdrqCmtsCmPollTime = _CdrqCmtsCmPollTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 1, 2, 1, 1, 6),
    _CdrqCmtsCmPollTime_Type()
)
cdrqCmtsCmPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrqCmtsCmPollTime.setStatus("current")
_CiscoDocsRQNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoDocsRQNotificationsPrefix = _CiscoDocsRQNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 2)
)
_CiscoDocsRQNotifications_ObjectIdentity = ObjectIdentity
ciscoDocsRQNotifications = _CiscoDocsRQNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 2, 0)
)
_CiscoDocsRemoteQueryConformance_ObjectIdentity = ObjectIdentity
ciscoDocsRemoteQueryConformance = _CiscoDocsRemoteQueryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3)
)
_CdrqDocsRemoteQueryCompliances_ObjectIdentity = ObjectIdentity
cdrqDocsRemoteQueryCompliances = _CdrqDocsRemoteQueryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 1)
)
_CdrqDocsRemoteQueryGroups_ObjectIdentity = ObjectIdentity
cdrqDocsRemoteQueryGroups = _CdrqDocsRemoteQueryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 2)
)

# Managed Objects groups

cdrqPollerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 2, 1)
)
cdrqPollerGroup.setObjects(
      *(("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerInterval"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerCommunity"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerContextEngineID"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerContextName"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerEnable"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerStartTime"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerStopTime"))
)
if mibBuilder.loadTexts:
    cdrqPollerGroup.setStatus("current")

cdrqCMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 2, 2)
)
cdrqCMGroup.setObjects(
      *(("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmDownChannelPower"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmStatusTxPower"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmUpChnlTxTimingOffset"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmSigQSignalNoise"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmSigQMicroreflections"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollTime"))
)
if mibBuilder.loadTexts:
    cdrqCMGroup.setStatus("current")


# Notification objects

cdrqCmtsCmRQDoneNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 2, 0, 1)
)
cdrqCmtsCmRQDoneNotification.setObjects(
      *(("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerStartTime"),
        ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmPollerStopTime"))
)
if mibBuilder.loadTexts:
    cdrqCmtsCmRQDoneNotification.setStatus(
        "current"
    )


# Notifications groups

cdrqNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 2, 3)
)
cdrqNotificationGroup.setObjects(
    ("CISCO-DOCS-REMOTE-QUERY-MIB", "cdrqCmtsCmRQDoneNotification")
)
if mibBuilder.loadTexts:
    cdrqNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdrqDocsRemoteQueryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 59, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdrqDocsRemoteQueryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOCS-REMOTE-QUERY-MIB",
    **{"ciscoDocsRemoteQueryMIB": ciscoDocsRemoteQueryMIB,
       "ciscoDocsRemQueryMIBObjects": ciscoDocsRemQueryMIBObjects,
       "cdrqPoller": cdrqPoller,
       "cdrqCmtsCmPollerEnable": cdrqCmtsCmPollerEnable,
       "cdrqCmtsCmPollerInterval": cdrqCmtsCmPollerInterval,
       "cdrqCmtsCmPollerCommunity": cdrqCmtsCmPollerCommunity,
       "cdrqCmtsCmPollerContextEngineID": cdrqCmtsCmPollerContextEngineID,
       "cdrqCmtsCmPollerContextName": cdrqCmtsCmPollerContextName,
       "cdrqCmtsCmPollerStartTime": cdrqCmtsCmPollerStartTime,
       "cdrqCmtsCmPollerStopTime": cdrqCmtsCmPollerStopTime,
       "cdrqCM": cdrqCM,
       "cdrqCmtsCmStatusTable": cdrqCmtsCmStatusTable,
       "cdrqCmtsCmStatusEntry": cdrqCmtsCmStatusEntry,
       "cdrqCmtsCmDownChannelPower": cdrqCmtsCmDownChannelPower,
       "cdrqCmtsCmStatusTxPower": cdrqCmtsCmStatusTxPower,
       "cdrqCmtsCmUpChnlTxTimingOffset": cdrqCmtsCmUpChnlTxTimingOffset,
       "cdrqCmtsCmSigQSignalNoise": cdrqCmtsCmSigQSignalNoise,
       "cdrqCmtsCmSigQMicroreflections": cdrqCmtsCmSigQMicroreflections,
       "cdrqCmtsCmPollTime": cdrqCmtsCmPollTime,
       "ciscoDocsRQNotificationsPrefix": ciscoDocsRQNotificationsPrefix,
       "ciscoDocsRQNotifications": ciscoDocsRQNotifications,
       "cdrqCmtsCmRQDoneNotification": cdrqCmtsCmRQDoneNotification,
       "ciscoDocsRemoteQueryConformance": ciscoDocsRemoteQueryConformance,
       "cdrqDocsRemoteQueryCompliances": cdrqDocsRemoteQueryCompliances,
       "cdrqDocsRemoteQueryCompliance": cdrqDocsRemoteQueryCompliance,
       "cdrqDocsRemoteQueryGroups": cdrqDocsRemoteQueryGroups,
       "cdrqPollerGroup": cdrqPollerGroup,
       "cdrqCMGroup": cdrqCMGroup,
       "cdrqNotificationGroup": cdrqNotificationGroup}
)
