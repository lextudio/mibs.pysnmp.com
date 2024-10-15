# SNMP MIB module (NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:37 2024
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

(NoiAcknowledgementState,
 NoiAcknowledgementTime,
 NoiAcknowledgementUserId,
 NoiAdditionalText,
 NoiAlarmId,
 NoiAlarmLogControl,
 NoiAlarmLogCount,
 NoiAlarmTableCount,
 NoiAlarmText,
 NoiEventTime,
 NoiEventType,
 NoiLogFullAction,
 NoiNotificationId,
 NoiNotificationType,
 NoiPerceivedSeverity,
 NoiProbableCause,
 NoiSpecificProblem,
 NoiSystemDistinguishedName) = mibBuilder.importSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION",
    "NoiAcknowledgementState",
    "NoiAcknowledgementTime",
    "NoiAcknowledgementUserId",
    "NoiAdditionalText",
    "NoiAlarmId",
    "NoiAlarmLogControl",
    "NoiAlarmLogCount",
    "NoiAlarmTableCount",
    "NoiAlarmText",
    "NoiEventTime",
    "NoiEventType",
    "NoiLogFullAction",
    "NoiNotificationId",
    "NoiNotificationType",
    "NoiPerceivedSeverity",
    "NoiProbableCause",
    "NoiSpecificProblem",
    "NoiSystemDistinguishedName")

(noiAlarmLog,
 noiAlarmNotification,
 noiAlarmTables,
 noiFMCompliance,
 noiFaultManagementVariable,
 noiOpenInterfaceModule) = mibBuilder.importSymbols(
    "NOKIA-NE3S-REGISTRATION-MIB",
    "noiAlarmLog",
    "noiAlarmNotification",
    "noiAlarmTables",
    "noiFMCompliance",
    "noiFaultManagementVariable",
    "noiOpenInterfaceModule")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

noiSnmpAlarmIrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 2)
)
noiSnmpAlarmIrp.setRevisions(
        ("2002-11-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NoiAlarmIrpVersion_Type(OctetString):
    """Custom type noiAlarmIrpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_NoiAlarmIrpVersion_Type.__name__ = "OctetString"
_NoiAlarmIrpVersion_Object = MibScalar
noiAlarmIrpVersion = _NoiAlarmIrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 2, 1),
    _NoiAlarmIrpVersion_Type()
)
noiAlarmIrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmIrpVersion.setStatus("current")
_NoiAlarmLastSendNotificationId_Type = NoiNotificationId
_NoiAlarmLastSendNotificationId_Object = MibScalar
noiAlarmLastSendNotificationId = _NoiAlarmLastSendNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 2, 2),
    _NoiAlarmLastSendNotificationId_Type()
)
noiAlarmLastSendNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLastSendNotificationId.setStatus("current")
_NoiAlarmTableCount_Type = NoiAlarmTableCount
_NoiAlarmTableCount_Object = MibScalar
noiAlarmTableCount = _NoiAlarmTableCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 1),
    _NoiAlarmTableCount_Type()
)
noiAlarmTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmTableCount.setStatus("current")
_NoiAlarmTable_Object = MibTable
noiAlarmTable = _NoiAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    noiAlarmTable.setStatus("current")
_NoiAlarmEntry_Object = MibTableRow
noiAlarmEntry = _NoiAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1)
)
noiAlarmEntry.setIndexNames(
    (0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
)
if mibBuilder.loadTexts:
    noiAlarmEntry.setStatus("current")
_NoiAlarmId_Type = NoiAlarmId
_NoiAlarmId_Object = MibTableColumn
noiAlarmId = _NoiAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 1),
    _NoiAlarmId_Type()
)
noiAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmId.setStatus("current")
_NoiAlarmSystemDN_Type = NoiSystemDistinguishedName
_NoiAlarmSystemDN_Object = MibTableColumn
noiAlarmSystemDN = _NoiAlarmSystemDN_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 2),
    _NoiAlarmSystemDN_Type()
)
noiAlarmSystemDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmSystemDN.setStatus("current")
_NoiAlarmEventTime_Type = NoiEventTime
_NoiAlarmEventTime_Object = MibTableColumn
noiAlarmEventTime = _NoiAlarmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 3),
    _NoiAlarmEventTime_Type()
)
noiAlarmEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmEventTime.setStatus("current")
_NoiAlarmSpecificProblem_Type = NoiSpecificProblem
_NoiAlarmSpecificProblem_Object = MibTableColumn
noiAlarmSpecificProblem = _NoiAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 4),
    _NoiAlarmSpecificProblem_Type()
)
noiAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmSpecificProblem.setStatus("current")
_NoiAlarmText_Type = NoiAlarmText
_NoiAlarmText_Object = MibTableColumn
noiAlarmText = _NoiAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 5),
    _NoiAlarmText_Type()
)
noiAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmText.setStatus("current")
_NoiAlarmPerceivedSeverity_Type = NoiPerceivedSeverity
_NoiAlarmPerceivedSeverity_Object = MibTableColumn
noiAlarmPerceivedSeverity = _NoiAlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 6),
    _NoiAlarmPerceivedSeverity_Type()
)
noiAlarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmPerceivedSeverity.setStatus("current")
_NoiAlarmAdditionalText_Type = NoiAdditionalText
_NoiAlarmAdditionalText_Object = MibTableColumn
noiAlarmAdditionalText = _NoiAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 7),
    _NoiAlarmAdditionalText_Type()
)
noiAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmAdditionalText.setStatus("current")
_NoiAlarmProbableCause_Type = NoiProbableCause
_NoiAlarmProbableCause_Object = MibTableColumn
noiAlarmProbableCause = _NoiAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 8),
    _NoiAlarmProbableCause_Type()
)
noiAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmProbableCause.setStatus("current")
_NoiAlarmEventType_Type = NoiEventType
_NoiAlarmEventType_Object = MibTableColumn
noiAlarmEventType = _NoiAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 9),
    _NoiAlarmEventType_Type()
)
noiAlarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmEventType.setStatus("current")
_NoiAlarmNotificationId_Type = NoiNotificationId
_NoiAlarmNotificationId_Object = MibTableColumn
noiAlarmNotificationId = _NoiAlarmNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 10),
    _NoiAlarmNotificationId_Type()
)
noiAlarmNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmNotificationId.setStatus("current")
_NoiAlarmAckState_Type = NoiAcknowledgementState
_NoiAlarmAckState_Object = MibTableColumn
noiAlarmAckState = _NoiAlarmAckState_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 11),
    _NoiAlarmAckState_Type()
)
noiAlarmAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiAlarmAckState.setStatus("current")
_NoiAlarmAckTime_Type = NoiAcknowledgementTime
_NoiAlarmAckTime_Object = MibTableColumn
noiAlarmAckTime = _NoiAlarmAckTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 12),
    _NoiAlarmAckTime_Type()
)
noiAlarmAckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiAlarmAckTime.setStatus("current")
_NoiAlarmAckUserId_Type = NoiAcknowledgementUserId
_NoiAlarmAckUserId_Object = MibTableColumn
noiAlarmAckUserId = _NoiAlarmAckUserId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 13),
    _NoiAlarmAckUserId_Type()
)
noiAlarmAckUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiAlarmAckUserId.setStatus("current")


class _NoiAlarmLogFullAction_Type(NoiLogFullAction):
    """Custom type noiAlarmLogFullAction based on NoiLogFullAction"""


_NoiAlarmLogFullAction_Object = MibScalar
noiAlarmLogFullAction = _NoiAlarmLogFullAction_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 1),
    _NoiAlarmLogFullAction_Type()
)
noiAlarmLogFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiAlarmLogFullAction.setStatus("current")


class _NoiAlarmLogControl_Type(NoiAlarmLogControl):
    """Custom type noiAlarmLogControl based on NoiAlarmLogControl"""


_NoiAlarmLogControl_Object = MibScalar
noiAlarmLogControl = _NoiAlarmLogControl_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 2),
    _NoiAlarmLogControl_Type()
)
noiAlarmLogControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiAlarmLogControl.setStatus("current")
_NoiAlarmLogCount_Type = NoiAlarmLogCount
_NoiAlarmLogCount_Object = MibScalar
noiAlarmLogCount = _NoiAlarmLogCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 3),
    _NoiAlarmLogCount_Type()
)
noiAlarmLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogCount.setStatus("current")
_NoiAlarmLogMaxCount_Type = NoiAlarmLogCount
_NoiAlarmLogMaxCount_Object = MibScalar
noiAlarmLogMaxCount = _NoiAlarmLogMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 4),
    _NoiAlarmLogMaxCount_Type()
)
noiAlarmLogMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogMaxCount.setStatus("current")
_NoiAlarmLogTable_Object = MibTable
noiAlarmLogTable = _NoiAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5)
)
if mibBuilder.loadTexts:
    noiAlarmLogTable.setStatus("current")
_NoiAlarmLogEntry_Object = MibTableRow
noiAlarmLogEntry = _NoiAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1)
)
noiAlarmLogEntry.setIndexNames(
    (0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationId"),
)
if mibBuilder.loadTexts:
    noiAlarmLogEntry.setStatus("current")
_NoiAlarmLogEntryNotificationId_Type = NoiNotificationId
_NoiAlarmLogEntryNotificationId_Object = MibTableColumn
noiAlarmLogEntryNotificationId = _NoiAlarmLogEntryNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 1),
    _NoiAlarmLogEntryNotificationId_Type()
)
noiAlarmLogEntryNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryNotificationId.setStatus("current")
_NoiAlarmLogEntryAlarmId_Type = NoiAlarmId
_NoiAlarmLogEntryAlarmId_Object = MibTableColumn
noiAlarmLogEntryAlarmId = _NoiAlarmLogEntryAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 2),
    _NoiAlarmLogEntryAlarmId_Type()
)
noiAlarmLogEntryAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAlarmId.setStatus("current")
_NoiAlarmLogEntrySystemDN_Type = NoiSystemDistinguishedName
_NoiAlarmLogEntrySystemDN_Object = MibTableColumn
noiAlarmLogEntrySystemDN = _NoiAlarmLogEntrySystemDN_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 3),
    _NoiAlarmLogEntrySystemDN_Type()
)
noiAlarmLogEntrySystemDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntrySystemDN.setStatus("current")
_NoiAlarmLogEntryEventTime_Type = NoiEventTime
_NoiAlarmLogEntryEventTime_Object = MibTableColumn
noiAlarmLogEntryEventTime = _NoiAlarmLogEntryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 4),
    _NoiAlarmLogEntryEventTime_Type()
)
noiAlarmLogEntryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryEventTime.setStatus("current")
_NoiAlarmLogEntrySpecificProblem_Type = NoiSpecificProblem
_NoiAlarmLogEntrySpecificProblem_Object = MibTableColumn
noiAlarmLogEntrySpecificProblem = _NoiAlarmLogEntrySpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 5),
    _NoiAlarmLogEntrySpecificProblem_Type()
)
noiAlarmLogEntrySpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntrySpecificProblem.setStatus("current")
_NoiAlarmLogEntryAlarmText_Type = NoiAlarmText
_NoiAlarmLogEntryAlarmText_Object = MibTableColumn
noiAlarmLogEntryAlarmText = _NoiAlarmLogEntryAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 6),
    _NoiAlarmLogEntryAlarmText_Type()
)
noiAlarmLogEntryAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAlarmText.setStatus("current")
_NoiAlarmLogEntryPerceivedSeverity_Type = NoiPerceivedSeverity
_NoiAlarmLogEntryPerceivedSeverity_Object = MibTableColumn
noiAlarmLogEntryPerceivedSeverity = _NoiAlarmLogEntryPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 7),
    _NoiAlarmLogEntryPerceivedSeverity_Type()
)
noiAlarmLogEntryPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryPerceivedSeverity.setStatus("current")
_NoiAlarmLogEntryAdditionalText_Type = NoiAdditionalText
_NoiAlarmLogEntryAdditionalText_Object = MibTableColumn
noiAlarmLogEntryAdditionalText = _NoiAlarmLogEntryAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 8),
    _NoiAlarmLogEntryAdditionalText_Type()
)
noiAlarmLogEntryAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAdditionalText.setStatus("current")
_NoiAlarmLogEntryProbableCause_Type = NoiProbableCause
_NoiAlarmLogEntryProbableCause_Object = MibTableColumn
noiAlarmLogEntryProbableCause = _NoiAlarmLogEntryProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 9),
    _NoiAlarmLogEntryProbableCause_Type()
)
noiAlarmLogEntryProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryProbableCause.setStatus("current")
_NoiAlarmLogEntryEventType_Type = NoiEventType
_NoiAlarmLogEntryEventType_Object = MibTableColumn
noiAlarmLogEntryEventType = _NoiAlarmLogEntryEventType_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 10),
    _NoiAlarmLogEntryEventType_Type()
)
noiAlarmLogEntryEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryEventType.setStatus("current")
_NoiAlarmLogEntryAckState_Type = NoiAcknowledgementState
_NoiAlarmLogEntryAckState_Object = MibTableColumn
noiAlarmLogEntryAckState = _NoiAlarmLogEntryAckState_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 11),
    _NoiAlarmLogEntryAckState_Type()
)
noiAlarmLogEntryAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAckState.setStatus("current")
_NoiAlarmLogEntryAckTime_Type = NoiAcknowledgementTime
_NoiAlarmLogEntryAckTime_Object = MibTableColumn
noiAlarmLogEntryAckTime = _NoiAlarmLogEntryAckTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 12),
    _NoiAlarmLogEntryAckTime_Type()
)
noiAlarmLogEntryAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAckTime.setStatus("current")
_NoiAlarmLogEntryAckUserId_Type = NoiAcknowledgementUserId
_NoiAlarmLogEntryAckUserId_Object = MibTableColumn
noiAlarmLogEntryAckUserId = _NoiAlarmLogEntryAckUserId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 13),
    _NoiAlarmLogEntryAckUserId_Type()
)
noiAlarmLogEntryAckUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryAckUserId.setStatus("current")
_NoiAlarmLogEntryNotificationType_Type = NoiNotificationType
_NoiAlarmLogEntryNotificationType_Object = MibTableColumn
noiAlarmLogEntryNotificationType = _NoiAlarmLogEntryNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 14),
    _NoiAlarmLogEntryNotificationType_Type()
)
noiAlarmLogEntryNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiAlarmLogEntryNotificationType.setStatus("current")

# Managed Objects groups

noiAlarmAdministrationMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 2)
)
noiAlarmAdministrationMandatoryGroup.setObjects(
    ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmIrpVersion")
)
if mibBuilder.loadTexts:
    noiAlarmAdministrationMandatoryGroup.setStatus("current")

noiAlarmTableOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 6)
)
noiAlarmTableOptionalGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmTableCount"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLastSendNotificationId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckState"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckUserId"))
)
if mibBuilder.loadTexts:
    noiAlarmTableOptionalGroup.setStatus("current")

noiAlarmLogOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 9)
)
noiAlarmLogOptionalGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogFullAction"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogControl"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogCount"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogMaxCount"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntrySystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntrySpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckState"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckUserId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationType"))
)
if mibBuilder.loadTexts:
    noiAlarmLogOptionalGroup.setStatus("current")


# Notification objects

noiAlarmNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 1)
)
noiAlarmNew.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
)
if mibBuilder.loadTexts:
    noiAlarmNew.setStatus(
        "current"
    )

noiAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 2)
)
noiAlarmCleared.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
)
if mibBuilder.loadTexts:
    noiAlarmCleared.setStatus(
        "current"
    )

noiAlarmListRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 3)
)
noiAlarmListRebuild.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
)
if mibBuilder.loadTexts:
    noiAlarmListRebuild.setStatus(
        "current"
    )

noiAlarmListRebuildInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 4)
)
noiAlarmListRebuildInitiated.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
)
if mibBuilder.loadTexts:
    noiAlarmListRebuildInitiated.setStatus(
        "current"
    )

noiAlarmChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 5)
)
noiAlarmChanged.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
)
if mibBuilder.loadTexts:
    noiAlarmChanged.setStatus(
        "current"
    )

noiAlarmAckStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 6)
)
noiAlarmAckStateChanged.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckState"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckUserId"))
)
if mibBuilder.loadTexts:
    noiAlarmAckStateChanged.setStatus(
        "current"
    )


# Notifications groups

noiAlarmNotificationMandatoryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 4)
)
noiAlarmNotificationMandatoryGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNew"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmCleared"))
)
if mibBuilder.loadTexts:
    noiAlarmNotificationMandatoryGroup.setStatus(
        "current"
    )

noiAlarmNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 5)
)
noiAlarmNotificationOptionalGroup.setObjects(
    ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmChanged")
)
if mibBuilder.loadTexts:
    noiAlarmNotificationOptionalGroup.setStatus(
        "current"
    )

noiAlarmTableRebuildOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 7)
)
noiAlarmTableRebuildOptionalGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmListRebuild"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmListRebuildInitiated"))
)
if mibBuilder.loadTexts:
    noiAlarmTableRebuildOptionalGroup.setStatus(
        "current"
    )

noiAlarmAcknwledgementOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 8)
)
noiAlarmAcknwledgementOptionalGroup.setObjects(
    ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckStateChanged")
)
if mibBuilder.loadTexts:
    noiAlarmAcknwledgementOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

noiAlarmIRPompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    noiAlarmIRPompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP",
    **{"noiSnmpAlarmIrp": noiSnmpAlarmIrp,
       "noiAlarmIrpVersion": noiAlarmIrpVersion,
       "noiAlarmLastSendNotificationId": noiAlarmLastSendNotificationId,
       "noiAlarmNew": noiAlarmNew,
       "noiAlarmCleared": noiAlarmCleared,
       "noiAlarmListRebuild": noiAlarmListRebuild,
       "noiAlarmListRebuildInitiated": noiAlarmListRebuildInitiated,
       "noiAlarmChanged": noiAlarmChanged,
       "noiAlarmAckStateChanged": noiAlarmAckStateChanged,
       "noiAlarmTableCount": noiAlarmTableCount,
       "noiAlarmTable": noiAlarmTable,
       "noiAlarmEntry": noiAlarmEntry,
       "noiAlarmId": noiAlarmId,
       "noiAlarmSystemDN": noiAlarmSystemDN,
       "noiAlarmEventTime": noiAlarmEventTime,
       "noiAlarmSpecificProblem": noiAlarmSpecificProblem,
       "noiAlarmText": noiAlarmText,
       "noiAlarmPerceivedSeverity": noiAlarmPerceivedSeverity,
       "noiAlarmAdditionalText": noiAlarmAdditionalText,
       "noiAlarmProbableCause": noiAlarmProbableCause,
       "noiAlarmEventType": noiAlarmEventType,
       "noiAlarmNotificationId": noiAlarmNotificationId,
       "noiAlarmAckState": noiAlarmAckState,
       "noiAlarmAckTime": noiAlarmAckTime,
       "noiAlarmAckUserId": noiAlarmAckUserId,
       "noiAlarmLogFullAction": noiAlarmLogFullAction,
       "noiAlarmLogControl": noiAlarmLogControl,
       "noiAlarmLogCount": noiAlarmLogCount,
       "noiAlarmLogMaxCount": noiAlarmLogMaxCount,
       "noiAlarmLogTable": noiAlarmLogTable,
       "noiAlarmLogEntry": noiAlarmLogEntry,
       "noiAlarmLogEntryNotificationId": noiAlarmLogEntryNotificationId,
       "noiAlarmLogEntryAlarmId": noiAlarmLogEntryAlarmId,
       "noiAlarmLogEntrySystemDN": noiAlarmLogEntrySystemDN,
       "noiAlarmLogEntryEventTime": noiAlarmLogEntryEventTime,
       "noiAlarmLogEntrySpecificProblem": noiAlarmLogEntrySpecificProblem,
       "noiAlarmLogEntryAlarmText": noiAlarmLogEntryAlarmText,
       "noiAlarmLogEntryPerceivedSeverity": noiAlarmLogEntryPerceivedSeverity,
       "noiAlarmLogEntryAdditionalText": noiAlarmLogEntryAdditionalText,
       "noiAlarmLogEntryProbableCause": noiAlarmLogEntryProbableCause,
       "noiAlarmLogEntryEventType": noiAlarmLogEntryEventType,
       "noiAlarmLogEntryAckState": noiAlarmLogEntryAckState,
       "noiAlarmLogEntryAckTime": noiAlarmLogEntryAckTime,
       "noiAlarmLogEntryAckUserId": noiAlarmLogEntryAckUserId,
       "noiAlarmLogEntryNotificationType": noiAlarmLogEntryNotificationType,
       "noiAlarmIRPompliance": noiAlarmIRPompliance,
       "noiAlarmAdministrationMandatoryGroup": noiAlarmAdministrationMandatoryGroup,
       "noiAlarmNotificationMandatoryGroup": noiAlarmNotificationMandatoryGroup,
       "noiAlarmNotificationOptionalGroup": noiAlarmNotificationOptionalGroup,
       "noiAlarmTableOptionalGroup": noiAlarmTableOptionalGroup,
       "noiAlarmTableRebuildOptionalGroup": noiAlarmTableRebuildOptionalGroup,
       "noiAlarmAcknwledgementOptionalGroup": noiAlarmAcknwledgementOptionalGroup,
       "noiAlarmLogOptionalGroup": noiAlarmLogOptionalGroup}
)
