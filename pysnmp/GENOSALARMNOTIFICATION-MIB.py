# SNMP MIB module (GENOSALARMNOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENOSALARMNOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:33 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alarmHandoff = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1)
)


# Types definitions



class AlarmId(Counter32):
    """Custom type AlarmId based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alcatel_ObjectIdentity = ObjectIdentity
alcatel = _Alcatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637)
)
_Nmu_ObjectIdentity = ObjectIdentity
nmu = _Nmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65)
)
_Genos_ObjectIdentity = ObjectIdentity
genos = _Genos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1)
)
_AlarmHandoffObjects_ObjectIdentity = ObjectIdentity
alarmHandoffObjects = _AlarmHandoffObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1)
)
_UnsolicitedEventsEnabled_Type = TruthValue
_UnsolicitedEventsEnabled_Object = MibScalar
unsolicitedEventsEnabled = _UnsolicitedEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 1),
    _UnsolicitedEventsEnabled_Type()
)
unsolicitedEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unsolicitedEventsEnabled.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "GENOSALARMNOTIFICATION-MIB", "currentAlarmId"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_CurrentAlarmId_Type = AlarmId
_CurrentAlarmId_Object = MibTableColumn
currentAlarmId = _CurrentAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 1),
    _CurrentAlarmId_Type()
)
currentAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmId.setStatus("current")
_FriendlyName_Type = DisplayString
_FriendlyName_Object = MibTableColumn
friendlyName = _FriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 2),
    _FriendlyName_Type()
)
friendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friendlyName.setStatus("current")
_EventTime_Type = DisplayString
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 3),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventType_Type = DisplayString
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 4),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_ProbableCause_Type = DisplayString
_ProbableCause_Object = MibTableColumn
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 5),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCause.setStatus("current")
_PerceivedSeverity_Type = DisplayString
_PerceivedSeverity_Object = MibTableColumn
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 6),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("current")
_AdditionalText_Type = DisplayString
_AdditionalText_Object = MibTableColumn
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 7),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")
_SpecificProblems_Type = DisplayString
_SpecificProblems_Object = MibTableColumn
specificProblems = _SpecificProblems_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 8),
    _SpecificProblems_Type()
)
specificProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificProblems.setStatus("current")
_AcknowledgementStatus_Type = DisplayString
_AcknowledgementStatus_Object = MibTableColumn
acknowledgementStatus = _AcknowledgementStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 9),
    _AcknowledgementStatus_Type()
)
acknowledgementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acknowledgementStatus.setStatus("current")
_ReserveStatus_Type = DisplayString
_ReserveStatus_Object = MibTableColumn
reserveStatus = _ReserveStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 10),
    _ReserveStatus_Type()
)
reserveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reserveStatus.setStatus("current")
_AdditionalInformation_Type = DisplayString
_AdditionalInformation_Object = MibTableColumn
additionalInformation = _AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 11),
    _AdditionalInformation_Type()
)
additionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalInformation.setStatus("current")
_NeLocationName_Type = DisplayString
_NeLocationName_Object = MibTableColumn
neLocationName = _NeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 12),
    _NeLocationName_Type()
)
neLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLocationName.setStatus("current")
_ManagedobjectInstance_Type = DisplayString
_ManagedobjectInstance_Object = MibTableColumn
managedobjectInstance = _ManagedobjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 13),
    _ManagedobjectInstance_Type()
)
managedobjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedobjectInstance.setStatus("current")
_AcknowledgementUserName_Type = DisplayString
_AcknowledgementUserName_Object = MibTableColumn
acknowledgementUserName = _AcknowledgementUserName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 14),
    _AcknowledgementUserName_Type()
)
acknowledgementUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acknowledgementUserName.setStatus("current")
_AsIdentity_Type = DisplayString
_AsIdentity_Object = MibTableColumn
asIdentity = _AsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 1, 2, 1, 15),
    _AsIdentity_Type()
)
asIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asIdentity.setStatus("current")
_AlarmHandoffTraps_ObjectIdentity = ObjectIdentity
alarmHandoffTraps = _AlarmHandoffTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2)
)
_AlarmHandoffAck_ObjectIdentity = ObjectIdentity
alarmHandoffAck = _AlarmHandoffAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 3)
)
_ListAlarmIds_Type = DisplayString
_ListAlarmIds_Object = MibScalar
listAlarmIds = _ListAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 3, 1),
    _ListAlarmIds_Type()
)
listAlarmIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listAlarmIds.setStatus("current")
_OperatorName_Type = DisplayString
_OperatorName_Object = MibScalar
operatorName = _OperatorName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 3, 2),
    _OperatorName_Type()
)
operatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatorName.setStatus("current")
_AckasIdentityFilter_Type = DisplayString
_AckasIdentityFilter_Object = MibScalar
ackasIdentityFilter = _AckasIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 3, 3),
    _AckasIdentityFilter_Type()
)
ackasIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ackasIdentityFilter.setStatus("current")
_AlarmHandoffFilter_ObjectIdentity = ObjectIdentity
alarmHandoffFilter = _AlarmHandoffFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4)
)
_FriendlyNameFilter_Type = DisplayString
_FriendlyNameFilter_Object = MibScalar
friendlyNameFilter = _FriendlyNameFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 1),
    _FriendlyNameFilter_Type()
)
friendlyNameFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friendlyNameFilter.setStatus("current")
_EventTimeFilter_Type = DisplayString
_EventTimeFilter_Object = MibScalar
eventTimeFilter = _EventTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 2),
    _EventTimeFilter_Type()
)
eventTimeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTimeFilter.setStatus("current")
_EventTypeFilter_Type = DisplayString
_EventTypeFilter_Object = MibScalar
eventTypeFilter = _EventTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 3),
    _EventTypeFilter_Type()
)
eventTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTypeFilter.setStatus("current")
_ProbableCauseFilter_Type = DisplayString
_ProbableCauseFilter_Object = MibScalar
probableCauseFilter = _ProbableCauseFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 4),
    _ProbableCauseFilter_Type()
)
probableCauseFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probableCauseFilter.setStatus("current")
_PerceivedSeverityFilter_Type = DisplayString
_PerceivedSeverityFilter_Object = MibScalar
perceivedSeverityFilter = _PerceivedSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 5),
    _PerceivedSeverityFilter_Type()
)
perceivedSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perceivedSeverityFilter.setStatus("current")
_SpecificProblemsFilter_Type = DisplayString
_SpecificProblemsFilter_Object = MibScalar
specificProblemsFilter = _SpecificProblemsFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 6),
    _SpecificProblemsFilter_Type()
)
specificProblemsFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificProblemsFilter.setStatus("current")
_NelocationNameFilter_Type = DisplayString
_NelocationNameFilter_Object = MibScalar
nelocationNameFilter = _NelocationNameFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 7),
    _NelocationNameFilter_Type()
)
nelocationNameFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nelocationNameFilter.setStatus("current")
_AdditionalInformationFilter_Type = DisplayString
_AdditionalInformationFilter_Object = MibScalar
additionalInformationFilter = _AdditionalInformationFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 8),
    _AdditionalInformationFilter_Type()
)
additionalInformationFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    additionalInformationFilter.setStatus("current")
_ManagedobjectInstanceFilter_Type = DisplayString
_ManagedobjectInstanceFilter_Object = MibScalar
managedobjectInstanceFilter = _ManagedobjectInstanceFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 9),
    _ManagedobjectInstanceFilter_Type()
)
managedobjectInstanceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managedobjectInstanceFilter.setStatus("current")
_AsIdentityFilter_Type = DisplayString
_AsIdentityFilter_Object = MibScalar
asIdentityFilter = _AsIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 4, 10),
    _AsIdentityFilter_Type()
)
asIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIdentityFilter.setStatus("current")
_AlarmHandoffPurge_ObjectIdentity = ObjectIdentity
alarmHandoffPurge = _AlarmHandoffPurge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 5)
)
_PurgelistAlarmIds_Type = DisplayString
_PurgelistAlarmIds_Object = MibScalar
purgelistAlarmIds = _PurgelistAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 5, 1),
    _PurgelistAlarmIds_Type()
)
purgelistAlarmIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    purgelistAlarmIds.setStatus("current")
_PurgeoperatorName_Type = DisplayString
_PurgeoperatorName_Object = MibScalar
purgeoperatorName = _PurgeoperatorName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 5, 2),
    _PurgeoperatorName_Type()
)
purgeoperatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    purgeoperatorName.setStatus("current")
_PurgeasIdentityFilter_Type = DisplayString
_PurgeasIdentityFilter_Object = MibScalar
purgeasIdentityFilter = _PurgeasIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 5, 3),
    _PurgeasIdentityFilter_Type()
)
purgeasIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    purgeasIdentityFilter.setStatus("current")
_AlarmHandoffReserve_ObjectIdentity = ObjectIdentity
alarmHandoffReserve = _AlarmHandoffReserve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 6)
)
_ReservelistAlarmIds_Type = DisplayString
_ReservelistAlarmIds_Object = MibScalar
reservelistAlarmIds = _ReservelistAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 6, 1),
    _ReservelistAlarmIds_Type()
)
reservelistAlarmIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reservelistAlarmIds.setStatus("current")
_ReserveoperatorName_Type = DisplayString
_ReserveoperatorName_Object = MibScalar
reserveoperatorName = _ReserveoperatorName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 6, 2),
    _ReserveoperatorName_Type()
)
reserveoperatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reserveoperatorName.setStatus("current")
_ReserveasIdentityFilter_Type = DisplayString
_ReserveasIdentityFilter_Object = MibScalar
reserveasIdentityFilter = _ReserveasIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 6, 3),
    _ReserveasIdentityFilter_Type()
)
reserveasIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reserveasIdentityFilter.setStatus("current")
_AlarmHandoffUnreserve_ObjectIdentity = ObjectIdentity
alarmHandoffUnreserve = _AlarmHandoffUnreserve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 7)
)
_UnreservelistAlarmIds_Type = DisplayString
_UnreservelistAlarmIds_Object = MibScalar
unreservelistAlarmIds = _UnreservelistAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 7, 1),
    _UnreservelistAlarmIds_Type()
)
unreservelistAlarmIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unreservelistAlarmIds.setStatus("current")
_UnreserveoperatorName_Type = DisplayString
_UnreserveoperatorName_Object = MibScalar
unreserveoperatorName = _UnreserveoperatorName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 7, 2),
    _UnreserveoperatorName_Type()
)
unreserveoperatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unreserveoperatorName.setStatus("current")
_UnreserveasIdentityFilter_Type = DisplayString
_UnreserveasIdentityFilter_Object = MibScalar
unreserveasIdentityFilter = _UnreserveasIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 7, 3),
    _UnreserveasIdentityFilter_Type()
)
unreserveasIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unreserveasIdentityFilter.setStatus("current")
_AlarmHandoffasConnectionStatus_ObjectIdentity = ObjectIdentity
alarmHandoffasConnectionStatus = _AlarmHandoffasConnectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 8)
)
_Asconnectionstatus_Type = DisplayString
_Asconnectionstatus_Object = MibScalar
asconnectionstatus = _Asconnectionstatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 8, 1),
    _Asconnectionstatus_Type()
)
asconnectionstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asconnectionstatus.setStatus("current")
_AsId_Type = DisplayString
_AsId_Object = MibScalar
asId = _AsId_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 8, 2),
    _AsId_Type()
)
asId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asId.setStatus("current")
_AlarmHandoffUnAck_ObjectIdentity = ObjectIdentity
alarmHandoffUnAck = _AlarmHandoffUnAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 9)
)
_UnacklistAlarmIds_Type = DisplayString
_UnacklistAlarmIds_Object = MibScalar
unacklistAlarmIds = _UnacklistAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 9, 1),
    _UnacklistAlarmIds_Type()
)
unacklistAlarmIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unacklistAlarmIds.setStatus("current")
_UnackoperatorName_Type = DisplayString
_UnackoperatorName_Object = MibScalar
unackoperatorName = _UnackoperatorName_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 9, 2),
    _UnackoperatorName_Type()
)
unackoperatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unackoperatorName.setStatus("current")
_UnackasIdentityFilter_Type = DisplayString
_UnackasIdentityFilter_Object = MibScalar
unackasIdentityFilter = _UnackasIdentityFilter_Object(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 9, 3),
    _UnackasIdentityFilter_Type()
)
unackasIdentityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unackasIdentityFilter.setStatus("current")

# Managed Objects groups


# Notification objects

alarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 1)
)
alarmRaise.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "currentAlarmId"),
        ("GENOSALARMNOTIFICATION-MIB", "friendlyName"),
        ("GENOSALARMNOTIFICATION-MIB", "eventTime"),
        ("GENOSALARMNOTIFICATION-MIB", "eventType"),
        ("GENOSALARMNOTIFICATION-MIB", "probableCause"),
        ("GENOSALARMNOTIFICATION-MIB", "perceivedSeverity"),
        ("GENOSALARMNOTIFICATION-MIB", "additionalText"),
        ("GENOSALARMNOTIFICATION-MIB", "specificProblems"),
        ("GENOSALARMNOTIFICATION-MIB", "acknowledgementStatus"),
        ("GENOSALARMNOTIFICATION-MIB", "reserveStatus"),
        ("GENOSALARMNOTIFICATION-MIB", "additionalInformation"),
        ("GENOSALARMNOTIFICATION-MIB", "neLocationName"),
        ("GENOSALARMNOTIFICATION-MIB", "managedobjectInstance"),
        ("GENOSALARMNOTIFICATION-MIB", "acknowledgementUserName"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmRaise.setStatus(
        "current"
    )

alarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 2)
)
alarmClear.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "currentAlarmId"),
        ("GENOSALARMNOTIFICATION-MIB", "eventTime"),
        ("GENOSALARMNOTIFICATION-MIB", "friendlyName"),
        ("GENOSALARMNOTIFICATION-MIB", "probableCause"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmClear.setStatus(
        "current"
    )

alarmAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 3)
)
alarmAck.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "listAlarmIds"),
        ("GENOSALARMNOTIFICATION-MIB", "operatorName"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmAck.setStatus(
        "current"
    )

alarmPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 4)
)
alarmPurge.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "purgelistAlarmIds"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmPurge.setStatus(
        "current"
    )

alarmReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 5)
)
alarmReserve.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "reservelistAlarmIds"),
        ("GENOSALARMNOTIFICATION-MIB", "reserveoperatorName"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmReserve.setStatus(
        "current"
    )

alarmUnreserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 6)
)
alarmUnreserve.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "unreservelistAlarmIds"),
        ("GENOSALARMNOTIFICATION-MIB", "unreserveoperatorName"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmUnreserve.setStatus(
        "current"
    )

asConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 7)
)
asConnectionStatus.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "asconnectionstatus"),
        ("GENOSALARMNOTIFICATION-MIB", "asId"))
)
if mibBuilder.loadTexts:
    asConnectionStatus.setStatus(
        "current"
    )

alarmUnAck = NotificationType(
    (1, 3, 6, 1, 4, 1, 637, 65, 1, 1, 2, 8)
)
alarmUnAck.setObjects(
      *(("GENOSALARMNOTIFICATION-MIB", "unacklistAlarmIds"),
        ("GENOSALARMNOTIFICATION-MIB", "unackoperatorName"),
        ("GENOSALARMNOTIFICATION-MIB", "asIdentity"))
)
if mibBuilder.loadTexts:
    alarmUnAck.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENOSALARMNOTIFICATION-MIB",
    **{"AlarmId": AlarmId,
       "alcatel": alcatel,
       "nmu": nmu,
       "genos": genos,
       "alarmHandoff": alarmHandoff,
       "alarmHandoffObjects": alarmHandoffObjects,
       "unsolicitedEventsEnabled": unsolicitedEventsEnabled,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "currentAlarmId": currentAlarmId,
       "friendlyName": friendlyName,
       "eventTime": eventTime,
       "eventType": eventType,
       "probableCause": probableCause,
       "perceivedSeverity": perceivedSeverity,
       "additionalText": additionalText,
       "specificProblems": specificProblems,
       "acknowledgementStatus": acknowledgementStatus,
       "reserveStatus": reserveStatus,
       "additionalInformation": additionalInformation,
       "neLocationName": neLocationName,
       "managedobjectInstance": managedobjectInstance,
       "acknowledgementUserName": acknowledgementUserName,
       "asIdentity": asIdentity,
       "alarmHandoffTraps": alarmHandoffTraps,
       "alarmRaise": alarmRaise,
       "alarmClear": alarmClear,
       "alarmAck": alarmAck,
       "alarmPurge": alarmPurge,
       "alarmReserve": alarmReserve,
       "alarmUnreserve": alarmUnreserve,
       "asConnectionStatus": asConnectionStatus,
       "alarmUnAck": alarmUnAck,
       "alarmHandoffAck": alarmHandoffAck,
       "listAlarmIds": listAlarmIds,
       "operatorName": operatorName,
       "ackasIdentityFilter": ackasIdentityFilter,
       "alarmHandoffFilter": alarmHandoffFilter,
       "friendlyNameFilter": friendlyNameFilter,
       "eventTimeFilter": eventTimeFilter,
       "eventTypeFilter": eventTypeFilter,
       "probableCauseFilter": probableCauseFilter,
       "perceivedSeverityFilter": perceivedSeverityFilter,
       "specificProblemsFilter": specificProblemsFilter,
       "nelocationNameFilter": nelocationNameFilter,
       "additionalInformationFilter": additionalInformationFilter,
       "managedobjectInstanceFilter": managedobjectInstanceFilter,
       "asIdentityFilter": asIdentityFilter,
       "alarmHandoffPurge": alarmHandoffPurge,
       "purgelistAlarmIds": purgelistAlarmIds,
       "purgeoperatorName": purgeoperatorName,
       "purgeasIdentityFilter": purgeasIdentityFilter,
       "alarmHandoffReserve": alarmHandoffReserve,
       "reservelistAlarmIds": reservelistAlarmIds,
       "reserveoperatorName": reserveoperatorName,
       "reserveasIdentityFilter": reserveasIdentityFilter,
       "alarmHandoffUnreserve": alarmHandoffUnreserve,
       "unreservelistAlarmIds": unreservelistAlarmIds,
       "unreserveoperatorName": unreserveoperatorName,
       "unreserveasIdentityFilter": unreserveasIdentityFilter,
       "alarmHandoffasConnectionStatus": alarmHandoffasConnectionStatus,
       "asconnectionstatus": asconnectionstatus,
       "asId": asId,
       "alarmHandoffUnAck": alarmHandoffUnAck,
       "unacklistAlarmIds": unacklistAlarmIds,
       "unackoperatorName": unackoperatorName,
       "unackasIdentityFilter": unackasIdentityFilter}
)
