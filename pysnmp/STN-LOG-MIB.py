# SNMP MIB module (STN-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:09 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")


# MODULE-IDENTITY

stnLog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnLogObjects_ObjectIdentity = ObjectIdentity
stnLogObjects = _StnLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1)
)


class _StnLogState_Type(Integer32):
    """Custom type stnLogState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnLogState_Type.__name__ = "Integer32"
_StnLogState_Object = MibScalar
stnLogState = _StnLogState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 1),
    _StnLogState_Type()
)
stnLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogState.setStatus("current")
_StnLogFlushTimer_Type = Integer32
_StnLogFlushTimer_Object = MibScalar
stnLogFlushTimer = _StnLogFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 2),
    _StnLogFlushTimer_Type()
)
stnLogFlushTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFlushTimer.setStatus("current")
_StnLogMaxDisplay_Type = Integer32
_StnLogMaxDisplay_Object = MibScalar
stnLogMaxDisplay = _StnLogMaxDisplay_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 3),
    _StnLogMaxDisplay_Type()
)
stnLogMaxDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogMaxDisplay.setStatus("current")
_StnLogServerTable_Object = MibTable
stnLogServerTable = _StnLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4)
)
if mibBuilder.loadTexts:
    stnLogServerTable.setStatus("current")
_StnLogServerEntry_Object = MibTableRow
stnLogServerEntry = _StnLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1)
)
stnLogServerEntry.setIndexNames(
    (0, "STN-LOG-MIB", "stnLogServerIndex"),
)
if mibBuilder.loadTexts:
    stnLogServerEntry.setStatus("current")
_StnLogServerIndex_Type = Integer32
_StnLogServerIndex_Object = MibTableColumn
stnLogServerIndex = _StnLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1, 1),
    _StnLogServerIndex_Type()
)
stnLogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogServerIndex.setStatus("current")


class _StnLogServerType_Type(Integer32):
    """Custom type stnLogServerType based on Integer32"""
    defaultValue = 1

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
        *(("debug-serial", 5),
          ("flash", 1),
          ("nma", 3),
          ("serial", 4),
          ("syslog", 2))
    )


_StnLogServerType_Type.__name__ = "Integer32"
_StnLogServerType_Object = MibTableColumn
stnLogServerType = _StnLogServerType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1, 2),
    _StnLogServerType_Type()
)
stnLogServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogServerType.setStatus("current")
_StnLogServerIpAddress_Type = IpAddress
_StnLogServerIpAddress_Object = MibTableColumn
stnLogServerIpAddress = _StnLogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1, 3),
    _StnLogServerIpAddress_Type()
)
stnLogServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogServerIpAddress.setStatus("current")
_StnLogServerFacility_Type = DisplayString
_StnLogServerFacility_Object = MibTableColumn
stnLogServerFacility = _StnLogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1, 4),
    _StnLogServerFacility_Type()
)
stnLogServerFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogServerFacility.setStatus("current")
_StnLogServerFileSize_Type = Integer32
_StnLogServerFileSize_Object = MibTableColumn
stnLogServerFileSize = _StnLogServerFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 4, 1, 5),
    _StnLogServerFileSize_Type()
)
stnLogServerFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogServerFileSize.setStatus("current")
_StnLogFilterTable_Object = MibTable
stnLogFilterTable = _StnLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5)
)
if mibBuilder.loadTexts:
    stnLogFilterTable.setStatus("current")
_StnLogFilterEntry_Object = MibTableRow
stnLogFilterEntry = _StnLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1)
)
stnLogFilterEntry.setIndexNames(
    (0, "STN-LOG-MIB", "stnLogFilterEngineId"),
    (0, "STN-LOG-MIB", "stnLogFilterMcId"),
)
if mibBuilder.loadTexts:
    stnLogFilterEntry.setStatus("current")
_StnLogFilterEngineId_Type = Integer32
_StnLogFilterEngineId_Object = MibTableColumn
stnLogFilterEngineId = _StnLogFilterEngineId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 1),
    _StnLogFilterEngineId_Type()
)
stnLogFilterEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterEngineId.setStatus("current")
_StnLogFilterMcId_Type = Integer32
_StnLogFilterMcId_Object = MibTableColumn
stnLogFilterMcId = _StnLogFilterMcId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 2),
    _StnLogFilterMcId_Type()
)
stnLogFilterMcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterMcId.setStatus("current")


class _StnLogFilterPriority_Type(Integer32):
    """Custom type stnLogFilterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_StnLogFilterPriority_Type.__name__ = "Integer32"
_StnLogFilterPriority_Object = MibTableColumn
stnLogFilterPriority = _StnLogFilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 3),
    _StnLogFilterPriority_Type()
)
stnLogFilterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterPriority.setStatus("current")
_StnLogFilterSeverityFatal_Type = TruthValue
_StnLogFilterSeverityFatal_Object = MibTableColumn
stnLogFilterSeverityFatal = _StnLogFilterSeverityFatal_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 4),
    _StnLogFilterSeverityFatal_Type()
)
stnLogFilterSeverityFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityFatal.setStatus("current")
_StnLogFilterSeverityError_Type = TruthValue
_StnLogFilterSeverityError_Object = MibTableColumn
stnLogFilterSeverityError = _StnLogFilterSeverityError_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 5),
    _StnLogFilterSeverityError_Type()
)
stnLogFilterSeverityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityError.setStatus("current")
_StnLogFilterSeverityWarning_Type = TruthValue
_StnLogFilterSeverityWarning_Object = MibTableColumn
stnLogFilterSeverityWarning = _StnLogFilterSeverityWarning_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 6),
    _StnLogFilterSeverityWarning_Type()
)
stnLogFilterSeverityWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityWarning.setStatus("current")
_StnLogFilterSeverityInfo_Type = TruthValue
_StnLogFilterSeverityInfo_Object = MibTableColumn
stnLogFilterSeverityInfo = _StnLogFilterSeverityInfo_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 7),
    _StnLogFilterSeverityInfo_Type()
)
stnLogFilterSeverityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityInfo.setStatus("current")
_StnLogFilterSeverityTrace_Type = TruthValue
_StnLogFilterSeverityTrace_Object = MibTableColumn
stnLogFilterSeverityTrace = _StnLogFilterSeverityTrace_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 8),
    _StnLogFilterSeverityTrace_Type()
)
stnLogFilterSeverityTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityTrace.setStatus("current")
_StnLogFilterSeverityDebug_Type = TruthValue
_StnLogFilterSeverityDebug_Object = MibTableColumn
stnLogFilterSeverityDebug = _StnLogFilterSeverityDebug_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 5, 1, 9),
    _StnLogFilterSeverityDebug_Type()
)
stnLogFilterSeverityDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogFilterSeverityDebug.setStatus("current")
_StnLogEventTable_Object = MibTable
stnLogEventTable = _StnLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6)
)
if mibBuilder.loadTexts:
    stnLogEventTable.setStatus("current")
_StnLogEventEntry_Object = MibTableRow
stnLogEventEntry = _StnLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1)
)
stnLogEventEntry.setIndexNames(
    (0, "STN-LOG-MIB", "stnLogEventIndex"),
)
if mibBuilder.loadTexts:
    stnLogEventEntry.setStatus("current")
_StnLogEventIndex_Type = Integer32
_StnLogEventIndex_Object = MibTableColumn
stnLogEventIndex = _StnLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 1),
    _StnLogEventIndex_Type()
)
stnLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventIndex.setStatus("current")
_StnLogEventEngineId_Type = Integer32
_StnLogEventEngineId_Object = MibTableColumn
stnLogEventEngineId = _StnLogEventEngineId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 2),
    _StnLogEventEngineId_Type()
)
stnLogEventEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventEngineId.setStatus("current")


class _StnLogEventMcName_Type(DisplayString):
    """Custom type stnLogEventMcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_StnLogEventMcName_Type.__name__ = "DisplayString"
_StnLogEventMcName_Object = MibTableColumn
stnLogEventMcName = _StnLogEventMcName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 3),
    _StnLogEventMcName_Type()
)
stnLogEventMcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventMcName.setStatus("current")


class _StnLogEventPriority_Type(Integer32):
    """Custom type stnLogEventPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StnLogEventPriority_Type.__name__ = "Integer32"
_StnLogEventPriority_Object = MibTableColumn
stnLogEventPriority = _StnLogEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 4),
    _StnLogEventPriority_Type()
)
stnLogEventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventPriority.setStatus("current")


class _StnLogEventTimeStamp_Type(DisplayString):
    """Custom type stnLogEventTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_StnLogEventTimeStamp_Type.__name__ = "DisplayString"
_StnLogEventTimeStamp_Object = MibTableColumn
stnLogEventTimeStamp = _StnLogEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 5),
    _StnLogEventTimeStamp_Type()
)
stnLogEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventTimeStamp.setStatus("current")
_StnLogEventMessage_Type = DisplayString
_StnLogEventMessage_Object = MibTableColumn
stnLogEventMessage = _StnLogEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 1, 6, 1, 6),
    _StnLogEventMessage_Type()
)
stnLogEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLogEventMessage.setStatus("current")
_StnLogMibConformance_ObjectIdentity = ObjectIdentity
stnLogMibConformance = _StnLogMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 13, 2)
)

# Managed Objects groups


# Notification objects

stnEventLogServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 24)
)
stnEventLogServerFailure.setObjects(
      *(("STN-LOG-MIB", "stnLogServerIndex"),
        ("STN-LOG-MIB", "stnLogServerType"),
        ("STN-LOG-MIB", "stnLogServerIpAddress"))
)
if mibBuilder.loadTexts:
    stnEventLogServerFailure.setStatus(
        "current"
    )

stnEventLogInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 25)
)
stnEventLogInternalFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnEventLogInternalFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-LOG-MIB",
    **{"stnLog": stnLog,
       "stnLogObjects": stnLogObjects,
       "stnLogState": stnLogState,
       "stnLogFlushTimer": stnLogFlushTimer,
       "stnLogMaxDisplay": stnLogMaxDisplay,
       "stnLogServerTable": stnLogServerTable,
       "stnLogServerEntry": stnLogServerEntry,
       "stnLogServerIndex": stnLogServerIndex,
       "stnLogServerType": stnLogServerType,
       "stnLogServerIpAddress": stnLogServerIpAddress,
       "stnLogServerFacility": stnLogServerFacility,
       "stnLogServerFileSize": stnLogServerFileSize,
       "stnLogFilterTable": stnLogFilterTable,
       "stnLogFilterEntry": stnLogFilterEntry,
       "stnLogFilterEngineId": stnLogFilterEngineId,
       "stnLogFilterMcId": stnLogFilterMcId,
       "stnLogFilterPriority": stnLogFilterPriority,
       "stnLogFilterSeverityFatal": stnLogFilterSeverityFatal,
       "stnLogFilterSeverityError": stnLogFilterSeverityError,
       "stnLogFilterSeverityWarning": stnLogFilterSeverityWarning,
       "stnLogFilterSeverityInfo": stnLogFilterSeverityInfo,
       "stnLogFilterSeverityTrace": stnLogFilterSeverityTrace,
       "stnLogFilterSeverityDebug": stnLogFilterSeverityDebug,
       "stnLogEventTable": stnLogEventTable,
       "stnLogEventEntry": stnLogEventEntry,
       "stnLogEventIndex": stnLogEventIndex,
       "stnLogEventEngineId": stnLogEventEngineId,
       "stnLogEventMcName": stnLogEventMcName,
       "stnLogEventPriority": stnLogEventPriority,
       "stnLogEventTimeStamp": stnLogEventTimeStamp,
       "stnLogEventMessage": stnLogEventMessage,
       "stnLogMibConformance": stnLogMibConformance,
       "stnEventLogServerFailure": stnEventLogServerFailure,
       "stnEventLogInternalFailure": stnEventLogInternalFailure}
)
