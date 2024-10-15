# SNMP MIB module (ITU-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITU-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:26 2024
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

(alarmActiveDateAndTime,
 alarmActiveIndex,
 alarmListName,
 alarmModelIndex) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmActiveDateAndTime",
    "alarmActiveIndex",
    "alarmListName",
    "alarmModelIndex")

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,
 ItuTrendIndication) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity",
    "ItuTrendIndication")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

ituAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 121)
)
ituAlarmMIB.setRevisions(
        ("2004-09-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ItuAlarmObjects_ObjectIdentity = ObjectIdentity
ituAlarmObjects = _ItuAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 1)
)
_ItuAlarmModel_ObjectIdentity = ObjectIdentity
ituAlarmModel = _ItuAlarmModel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 1, 1)
)
_ItuAlarmTable_Object = MibTable
ituAlarmTable = _ItuAlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ituAlarmTable.setStatus("current")
_ItuAlarmEntry_Object = MibTableRow
ituAlarmEntry = _ItuAlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1)
)
ituAlarmEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmModelIndex"),
    (0, "ITU-ALARM-MIB", "ituAlarmPerceivedSeverity"),
)
if mibBuilder.loadTexts:
    ituAlarmEntry.setStatus("current")
_ItuAlarmPerceivedSeverity_Type = ItuPerceivedSeverity
_ItuAlarmPerceivedSeverity_Object = MibTableColumn
ituAlarmPerceivedSeverity = _ItuAlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 1),
    _ItuAlarmPerceivedSeverity_Type()
)
ituAlarmPerceivedSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ituAlarmPerceivedSeverity.setStatus("current")
_ItuAlarmEventType_Type = IANAItuEventType
_ItuAlarmEventType_Object = MibTableColumn
ituAlarmEventType = _ItuAlarmEventType_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 2),
    _ItuAlarmEventType_Type()
)
ituAlarmEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ituAlarmEventType.setStatus("current")
_ItuAlarmProbableCause_Type = IANAItuProbableCause
_ItuAlarmProbableCause_Object = MibTableColumn
ituAlarmProbableCause = _ItuAlarmProbableCause_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 3),
    _ItuAlarmProbableCause_Type()
)
ituAlarmProbableCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ituAlarmProbableCause.setStatus("current")
_ItuAlarmAdditionalText_Type = SnmpAdminString
_ItuAlarmAdditionalText_Object = MibTableColumn
ituAlarmAdditionalText = _ItuAlarmAdditionalText_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 4),
    _ItuAlarmAdditionalText_Type()
)
ituAlarmAdditionalText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ituAlarmAdditionalText.setStatus("current")
_ItuAlarmGenericModel_Type = RowPointer
_ItuAlarmGenericModel_Object = MibTableColumn
ituAlarmGenericModel = _ItuAlarmGenericModel_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 1, 1, 1, 5),
    _ItuAlarmGenericModel_Type()
)
ituAlarmGenericModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ituAlarmGenericModel.setStatus("current")
_ItuAlarmActive_ObjectIdentity = ObjectIdentity
ituAlarmActive = _ItuAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 1, 2)
)
_ItuAlarmActiveTable_Object = MibTable
ituAlarmActiveTable = _ItuAlarmActiveTable_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ituAlarmActiveTable.setStatus("current")
_ItuAlarmActiveEntry_Object = MibTableRow
ituAlarmActiveEntry = _ItuAlarmActiveEntry_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1)
)
ituAlarmActiveEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmActiveDateAndTime"),
    (0, "ALARM-MIB", "alarmActiveIndex"),
)
if mibBuilder.loadTexts:
    ituAlarmActiveEntry.setStatus("current")
_ItuAlarmActiveTrendIndication_Type = ItuTrendIndication
_ItuAlarmActiveTrendIndication_Object = MibTableColumn
ituAlarmActiveTrendIndication = _ItuAlarmActiveTrendIndication_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 1),
    _ItuAlarmActiveTrendIndication_Type()
)
ituAlarmActiveTrendIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveTrendIndication.setStatus("current")
_ItuAlarmActiveDetector_Type = AutonomousType
_ItuAlarmActiveDetector_Object = MibTableColumn
ituAlarmActiveDetector = _ItuAlarmActiveDetector_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 2),
    _ItuAlarmActiveDetector_Type()
)
ituAlarmActiveDetector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveDetector.setStatus("current")
_ItuAlarmActiveServiceProvider_Type = AutonomousType
_ItuAlarmActiveServiceProvider_Object = MibTableColumn
ituAlarmActiveServiceProvider = _ItuAlarmActiveServiceProvider_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 3),
    _ItuAlarmActiveServiceProvider_Type()
)
ituAlarmActiveServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveServiceProvider.setStatus("current")
_ItuAlarmActiveServiceUser_Type = AutonomousType
_ItuAlarmActiveServiceUser_Object = MibTableColumn
ituAlarmActiveServiceUser = _ItuAlarmActiveServiceUser_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 1, 1, 4),
    _ItuAlarmActiveServiceUser_Type()
)
ituAlarmActiveServiceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveServiceUser.setStatus("current")
_ItuAlarmActiveStatsTable_Object = MibTable
ituAlarmActiveStatsTable = _ItuAlarmActiveStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ituAlarmActiveStatsTable.setStatus("current")
_ItuAlarmActiveStatsEntry_Object = MibTableRow
ituAlarmActiveStatsEntry = _ItuAlarmActiveStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1)
)
ituAlarmActiveStatsEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
)
if mibBuilder.loadTexts:
    ituAlarmActiveStatsEntry.setStatus("current")
_ItuAlarmActiveStatsIndeterminateCurrent_Type = Gauge32
_ItuAlarmActiveStatsIndeterminateCurrent_Object = MibTableColumn
ituAlarmActiveStatsIndeterminateCurrent = _ItuAlarmActiveStatsIndeterminateCurrent_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 1),
    _ItuAlarmActiveStatsIndeterminateCurrent_Type()
)
ituAlarmActiveStatsIndeterminateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsIndeterminateCurrent.setStatus("current")
_ItuAlarmActiveStatsCriticalCurrent_Type = Gauge32
_ItuAlarmActiveStatsCriticalCurrent_Object = MibTableColumn
ituAlarmActiveStatsCriticalCurrent = _ItuAlarmActiveStatsCriticalCurrent_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 2),
    _ItuAlarmActiveStatsCriticalCurrent_Type()
)
ituAlarmActiveStatsCriticalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsCriticalCurrent.setStatus("current")
_ItuAlarmActiveStatsMajorCurrent_Type = Gauge32
_ItuAlarmActiveStatsMajorCurrent_Object = MibTableColumn
ituAlarmActiveStatsMajorCurrent = _ItuAlarmActiveStatsMajorCurrent_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 3),
    _ItuAlarmActiveStatsMajorCurrent_Type()
)
ituAlarmActiveStatsMajorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsMajorCurrent.setStatus("current")
_ItuAlarmActiveStatsMinorCurrent_Type = Gauge32
_ItuAlarmActiveStatsMinorCurrent_Object = MibTableColumn
ituAlarmActiveStatsMinorCurrent = _ItuAlarmActiveStatsMinorCurrent_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 4),
    _ItuAlarmActiveStatsMinorCurrent_Type()
)
ituAlarmActiveStatsMinorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsMinorCurrent.setStatus("current")
_ItuAlarmActiveStatsWarningCurrent_Type = Gauge32
_ItuAlarmActiveStatsWarningCurrent_Object = MibTableColumn
ituAlarmActiveStatsWarningCurrent = _ItuAlarmActiveStatsWarningCurrent_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 5),
    _ItuAlarmActiveStatsWarningCurrent_Type()
)
ituAlarmActiveStatsWarningCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsWarningCurrent.setStatus("current")
_ItuAlarmActiveStatsIndeterminates_Type = ZeroBasedCounter32
_ItuAlarmActiveStatsIndeterminates_Object = MibTableColumn
ituAlarmActiveStatsIndeterminates = _ItuAlarmActiveStatsIndeterminates_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 6),
    _ItuAlarmActiveStatsIndeterminates_Type()
)
ituAlarmActiveStatsIndeterminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsIndeterminates.setStatus("current")
_ItuAlarmActiveStatsCriticals_Type = ZeroBasedCounter32
_ItuAlarmActiveStatsCriticals_Object = MibTableColumn
ituAlarmActiveStatsCriticals = _ItuAlarmActiveStatsCriticals_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 7),
    _ItuAlarmActiveStatsCriticals_Type()
)
ituAlarmActiveStatsCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsCriticals.setStatus("current")
_ItuAlarmActiveStatsMajors_Type = ZeroBasedCounter32
_ItuAlarmActiveStatsMajors_Object = MibTableColumn
ituAlarmActiveStatsMajors = _ItuAlarmActiveStatsMajors_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 8),
    _ItuAlarmActiveStatsMajors_Type()
)
ituAlarmActiveStatsMajors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsMajors.setStatus("current")
_ItuAlarmActiveStatsMinors_Type = ZeroBasedCounter32
_ItuAlarmActiveStatsMinors_Object = MibTableColumn
ituAlarmActiveStatsMinors = _ItuAlarmActiveStatsMinors_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 9),
    _ItuAlarmActiveStatsMinors_Type()
)
ituAlarmActiveStatsMinors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsMinors.setStatus("current")
_ItuAlarmActiveStatsWarnings_Type = ZeroBasedCounter32
_ItuAlarmActiveStatsWarnings_Object = MibTableColumn
ituAlarmActiveStatsWarnings = _ItuAlarmActiveStatsWarnings_Object(
    (1, 3, 6, 1, 2, 1, 121, 1, 2, 2, 1, 10),
    _ItuAlarmActiveStatsWarnings_Type()
)
ituAlarmActiveStatsWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ituAlarmActiveStatsWarnings.setStatus("current")
_ItuAlarmConformance_ObjectIdentity = ObjectIdentity
ituAlarmConformance = _ItuAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 2)
)
_ItuAlarmCompliances_ObjectIdentity = ObjectIdentity
ituAlarmCompliances = _ItuAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 2, 1)
)
_ItuAlarmGroups_ObjectIdentity = ObjectIdentity
ituAlarmGroups = _ItuAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 121, 2, 2)
)

# Managed Objects groups

ituAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 121, 2, 2, 1)
)
ituAlarmGroup.setObjects(
      *(("ITU-ALARM-MIB", "ituAlarmEventType"),
        ("ITU-ALARM-MIB", "ituAlarmProbableCause"),
        ("ITU-ALARM-MIB", "ituAlarmGenericModel"))
)
if mibBuilder.loadTexts:
    ituAlarmGroup.setStatus("current")

ituAlarmServiceUserGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 121, 2, 2, 2)
)
ituAlarmServiceUserGroup.setObjects(
      *(("ITU-ALARM-MIB", "ituAlarmAdditionalText"),
        ("ITU-ALARM-MIB", "ituAlarmActiveTrendIndication"))
)
if mibBuilder.loadTexts:
    ituAlarmServiceUserGroup.setStatus("current")

ituAlarmSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 121, 2, 2, 3)
)
ituAlarmSecurityGroup.setObjects(
      *(("ITU-ALARM-MIB", "ituAlarmActiveDetector"),
        ("ITU-ALARM-MIB", "ituAlarmActiveServiceProvider"),
        ("ITU-ALARM-MIB", "ituAlarmActiveServiceUser"))
)
if mibBuilder.loadTexts:
    ituAlarmSecurityGroup.setStatus("current")

ituAlarmStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 121, 2, 2, 4)
)
ituAlarmStatisticsGroup.setObjects(
      *(("ITU-ALARM-MIB", "ituAlarmActiveStatsIndeterminateCurrent"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsCriticalCurrent"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsMajorCurrent"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsMinorCurrent"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsWarningCurrent"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsIndeterminates"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsCriticals"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsMajors"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsMinors"),
        ("ITU-ALARM-MIB", "ituAlarmActiveStatsWarnings"))
)
if mibBuilder.loadTexts:
    ituAlarmStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ituAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 121, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ituAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITU-ALARM-MIB",
    **{"ituAlarmMIB": ituAlarmMIB,
       "ituAlarmObjects": ituAlarmObjects,
       "ituAlarmModel": ituAlarmModel,
       "ituAlarmTable": ituAlarmTable,
       "ituAlarmEntry": ituAlarmEntry,
       "ituAlarmPerceivedSeverity": ituAlarmPerceivedSeverity,
       "ituAlarmEventType": ituAlarmEventType,
       "ituAlarmProbableCause": ituAlarmProbableCause,
       "ituAlarmAdditionalText": ituAlarmAdditionalText,
       "ituAlarmGenericModel": ituAlarmGenericModel,
       "ituAlarmActive": ituAlarmActive,
       "ituAlarmActiveTable": ituAlarmActiveTable,
       "ituAlarmActiveEntry": ituAlarmActiveEntry,
       "ituAlarmActiveTrendIndication": ituAlarmActiveTrendIndication,
       "ituAlarmActiveDetector": ituAlarmActiveDetector,
       "ituAlarmActiveServiceProvider": ituAlarmActiveServiceProvider,
       "ituAlarmActiveServiceUser": ituAlarmActiveServiceUser,
       "ituAlarmActiveStatsTable": ituAlarmActiveStatsTable,
       "ituAlarmActiveStatsEntry": ituAlarmActiveStatsEntry,
       "ituAlarmActiveStatsIndeterminateCurrent": ituAlarmActiveStatsIndeterminateCurrent,
       "ituAlarmActiveStatsCriticalCurrent": ituAlarmActiveStatsCriticalCurrent,
       "ituAlarmActiveStatsMajorCurrent": ituAlarmActiveStatsMajorCurrent,
       "ituAlarmActiveStatsMinorCurrent": ituAlarmActiveStatsMinorCurrent,
       "ituAlarmActiveStatsWarningCurrent": ituAlarmActiveStatsWarningCurrent,
       "ituAlarmActiveStatsIndeterminates": ituAlarmActiveStatsIndeterminates,
       "ituAlarmActiveStatsCriticals": ituAlarmActiveStatsCriticals,
       "ituAlarmActiveStatsMajors": ituAlarmActiveStatsMajors,
       "ituAlarmActiveStatsMinors": ituAlarmActiveStatsMinors,
       "ituAlarmActiveStatsWarnings": ituAlarmActiveStatsWarnings,
       "ituAlarmConformance": ituAlarmConformance,
       "ituAlarmCompliances": ituAlarmCompliances,
       "ituAlarmCompliance": ituAlarmCompliance,
       "ituAlarmGroups": ituAlarmGroups,
       "ituAlarmGroup": ituAlarmGroup,
       "ituAlarmServiceUserGroup": ituAlarmServiceUserGroup,
       "ituAlarmSecurityGroup": ituAlarmSecurityGroup,
       "ituAlarmStatisticsGroup": ituAlarmStatisticsGroup}
)
