# SNMP MIB module (ERICSSON-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERICSSON-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:33 2024
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

(ResourceId,) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "ResourceId")

(EriProbableCause,) = mibBuilder.importSymbols(
    "ERICSSON-ALARM-PC-MIB",
    "EriProbableCause")

(EriAdditionalText,
 EriAlarmIndex,
 EriAlarmSequenceNumber,
 EriAlarmSpecificProblem,
 EriAlarmType,
 EriLargeAdditionalText) = mibBuilder.importSymbols(
    "ERICSSON-ALARM-TC-MIB",
    "EriAdditionalText",
    "EriAlarmIndex",
    "EriAlarmSequenceNumber",
    "EriAlarmSpecificProblem",
    "EriAlarmType",
    "EriLargeAdditionalText")

(EriMO,) = mibBuilder.importSymbols(
    "ERICSSON-TC-MIB",
    "EriMO")

(ericssonModules,) = mibBuilder.importSymbols(
    "ERICSSON-TOP-MIB",
    "ericssonModules")

(IANAItuEventType,) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpNotifyGroup,) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyGroup")

(snmpTargetBasicGroup,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetBasicGroup")

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

ericssonAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4)
)
ericssonAlarmMIB.setRevisions(
        ("2008-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EriAlarmObjects_ObjectIdentity = ObjectIdentity
eriAlarmObjects = _EriAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1)
)
_EriAlarmSummary_ObjectIdentity = ObjectIdentity
eriAlarmSummary = _EriAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1)
)
_EriAlarmSumIndeterminate_Type = Gauge32
_EriAlarmSumIndeterminate_Object = MibScalar
eriAlarmSumIndeterminate = _EriAlarmSumIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1, 1),
    _EriAlarmSumIndeterminate_Type()
)
eriAlarmSumIndeterminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmSumIndeterminate.setStatus("current")
_EriAlarmSumCritical_Type = Gauge32
_EriAlarmSumCritical_Object = MibScalar
eriAlarmSumCritical = _EriAlarmSumCritical_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1, 2),
    _EriAlarmSumCritical_Type()
)
eriAlarmSumCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmSumCritical.setStatus("current")
_EriAlarmSumMajor_Type = Gauge32
_EriAlarmSumMajor_Object = MibScalar
eriAlarmSumMajor = _EriAlarmSumMajor_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1, 3),
    _EriAlarmSumMajor_Type()
)
eriAlarmSumMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmSumMajor.setStatus("current")
_EriAlarmSumMinor_Type = Gauge32
_EriAlarmSumMinor_Object = MibScalar
eriAlarmSumMinor = _EriAlarmSumMinor_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1, 4),
    _EriAlarmSumMinor_Type()
)
eriAlarmSumMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmSumMinor.setStatus("current")
_EriAlarmSumWarning_Type = Gauge32
_EriAlarmSumWarning_Object = MibScalar
eriAlarmSumWarning = _EriAlarmSumWarning_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 1, 5),
    _EriAlarmSumWarning_Type()
)
eriAlarmSumWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmSumWarning.setStatus("current")
_EriAlarmNotifObjects_ObjectIdentity = ObjectIdentity
eriAlarmNotifObjects = _EriAlarmNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 2)
)
_EriAlarmNObjAdditionalText_Type = EriAdditionalText
_EriAlarmNObjAdditionalText_Object = MibScalar
eriAlarmNObjAdditionalText = _EriAlarmNObjAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 2, 1),
    _EriAlarmNObjAdditionalText_Type()
)
eriAlarmNObjAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriAlarmNObjAdditionalText.setStatus("current")
_EriAlarmNObjMoreAdditionalText_Type = TruthValue
_EriAlarmNObjMoreAdditionalText_Object = MibScalar
eriAlarmNObjMoreAdditionalText = _EriAlarmNObjMoreAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 2, 2),
    _EriAlarmNObjMoreAdditionalText_Type()
)
eriAlarmNObjMoreAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriAlarmNObjMoreAdditionalText.setStatus("current")
_EriAlarmNObjResourceId_Type = TruthValue
_EriAlarmNObjResourceId_Object = MibScalar
eriAlarmNObjResourceId = _EriAlarmNObjResourceId_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 2, 3),
    _EriAlarmNObjResourceId_Type()
)
eriAlarmNObjResourceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eriAlarmNObjResourceId.setStatus("current")
_EriAlarmActiveAlarms_ObjectIdentity = ObjectIdentity
eriAlarmActiveAlarms = _EriAlarmActiveAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3)
)
_EriAlarmActiveNumber_Type = Unsigned32
_EriAlarmActiveNumber_Object = MibScalar
eriAlarmActiveNumber = _EriAlarmActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 1),
    _EriAlarmActiveNumber_Type()
)
eriAlarmActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveNumber.setStatus("current")
_EriAlarmActiveLastChanged_Type = DateAndTime
_EriAlarmActiveLastChanged_Object = MibScalar
eriAlarmActiveLastChanged = _EriAlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 2),
    _EriAlarmActiveLastChanged_Type()
)
eriAlarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveLastChanged.setStatus("current")
_EriAlarmActiveLastSequenceNo_Type = EriAlarmSequenceNumber
_EriAlarmActiveLastSequenceNo_Object = MibScalar
eriAlarmActiveLastSequenceNo = _EriAlarmActiveLastSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 3),
    _EriAlarmActiveLastSequenceNo_Type()
)
eriAlarmActiveLastSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveLastSequenceNo.setStatus("current")
_EriAlarmActiveTableURL_Type = SnmpAdminString
_EriAlarmActiveTableURL_Object = MibScalar
eriAlarmActiveTableURL = _EriAlarmActiveTableURL_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 4),
    _EriAlarmActiveTableURL_Type()
)
eriAlarmActiveTableURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveTableURL.setStatus("current")
_EriAlarmActiveAlarmTable_Object = MibTable
eriAlarmActiveAlarmTable = _EriAlarmActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    eriAlarmActiveAlarmTable.setStatus("current")
_EriAlarmActiveAlarmEntry_Object = MibTableRow
eriAlarmActiveAlarmEntry = _EriAlarmActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1)
)
eriAlarmActiveAlarmEntry.setIndexNames(
    (0, "ERICSSON-ALARM-MIB", "eriAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    eriAlarmActiveAlarmEntry.setStatus("current")
_EriAlarmActiveIndex_Type = EriAlarmIndex
_EriAlarmActiveIndex_Object = MibTableColumn
eriAlarmActiveIndex = _EriAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 1),
    _EriAlarmActiveIndex_Type()
)
eriAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriAlarmActiveIndex.setStatus("current")
_EriAlarmActiveMajorType_Type = EriAlarmType
_EriAlarmActiveMajorType_Object = MibTableColumn
eriAlarmActiveMajorType = _EriAlarmActiveMajorType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 2),
    _EriAlarmActiveMajorType_Type()
)
eriAlarmActiveMajorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveMajorType.setStatus("current")
_EriAlarmActiveMinorType_Type = EriAlarmType
_EriAlarmActiveMinorType_Object = MibTableColumn
eriAlarmActiveMinorType = _EriAlarmActiveMinorType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 3),
    _EriAlarmActiveMinorType_Type()
)
eriAlarmActiveMinorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveMinorType.setStatus("current")
_EriAlarmActiveSpecificProblem_Type = EriAlarmSpecificProblem
_EriAlarmActiveSpecificProblem_Object = MibTableColumn
eriAlarmActiveSpecificProblem = _EriAlarmActiveSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 4),
    _EriAlarmActiveSpecificProblem_Type()
)
eriAlarmActiveSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveSpecificProblem.setStatus("current")
_EriAlarmActiveManagedObject_Type = EriMO
_EriAlarmActiveManagedObject_Object = MibTableColumn
eriAlarmActiveManagedObject = _EriAlarmActiveManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 5),
    _EriAlarmActiveManagedObject_Type()
)
eriAlarmActiveManagedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveManagedObject.setStatus("current")
_EriAlarmActiveEventType_Type = IANAItuEventType
_EriAlarmActiveEventType_Object = MibTableColumn
eriAlarmActiveEventType = _EriAlarmActiveEventType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 6),
    _EriAlarmActiveEventType_Type()
)
eriAlarmActiveEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveEventType.setStatus("current")
_EriAlarmActiveEventTime_Type = DateAndTime
_EriAlarmActiveEventTime_Object = MibTableColumn
eriAlarmActiveEventTime = _EriAlarmActiveEventTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 7),
    _EriAlarmActiveEventTime_Type()
)
eriAlarmActiveEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveEventTime.setStatus("current")
_EriAlarmActiveOriginalEventTime_Type = DateAndTime
_EriAlarmActiveOriginalEventTime_Object = MibTableColumn
eriAlarmActiveOriginalEventTime = _EriAlarmActiveOriginalEventTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 8),
    _EriAlarmActiveOriginalEventTime_Type()
)
eriAlarmActiveOriginalEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveOriginalEventTime.setStatus("current")
_EriAlarmActiveProbableCause_Type = EriProbableCause
_EriAlarmActiveProbableCause_Object = MibTableColumn
eriAlarmActiveProbableCause = _EriAlarmActiveProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 9),
    _EriAlarmActiveProbableCause_Type()
)
eriAlarmActiveProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveProbableCause.setStatus("current")
_EriAlarmActiveSeverity_Type = ItuPerceivedSeverity
_EriAlarmActiveSeverity_Object = MibTableColumn
eriAlarmActiveSeverity = _EriAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 10),
    _EriAlarmActiveSeverity_Type()
)
eriAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveSeverity.setStatus("current")
_EriAlarmActiveOriginalSeverity_Type = ItuPerceivedSeverity
_EriAlarmActiveOriginalSeverity_Object = MibTableColumn
eriAlarmActiveOriginalSeverity = _EriAlarmActiveOriginalSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 11),
    _EriAlarmActiveOriginalSeverity_Type()
)
eriAlarmActiveOriginalSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveOriginalSeverity.setStatus("current")
_EriAlarmActiveAdditionalText_Type = EriLargeAdditionalText
_EriAlarmActiveAdditionalText_Object = MibTableColumn
eriAlarmActiveAdditionalText = _EriAlarmActiveAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 12),
    _EriAlarmActiveAdditionalText_Type()
)
eriAlarmActiveAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveAdditionalText.setStatus("current")
_EriAlarmActiveOrigAdditionalText_Type = EriLargeAdditionalText
_EriAlarmActiveOrigAdditionalText_Object = MibTableColumn
eriAlarmActiveOrigAdditionalText = _EriAlarmActiveOrigAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 13),
    _EriAlarmActiveOrigAdditionalText_Type()
)
eriAlarmActiveOrigAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveOrigAdditionalText.setStatus("current")
_EriAlarmActiveResourceId_Type = ResourceId
_EriAlarmActiveResourceId_Object = MibTableColumn
eriAlarmActiveResourceId = _EriAlarmActiveResourceId_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 3, 5, 1, 14),
    _EriAlarmActiveResourceId_Type()
)
eriAlarmActiveResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmActiveResourceId.setStatus("current")
_EriAlarmAlerts_ObjectIdentity = ObjectIdentity
eriAlarmAlerts = _EriAlarmAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4)
)
_EriAlarmAlertNumber_Type = Unsigned32
_EriAlarmAlertNumber_Object = MibScalar
eriAlarmAlertNumber = _EriAlarmAlertNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 1),
    _EriAlarmAlertNumber_Type()
)
eriAlarmAlertNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertNumber.setStatus("current")
_EriAlarmAlertLastChanged_Type = DateAndTime
_EriAlarmAlertLastChanged_Object = MibScalar
eriAlarmAlertLastChanged = _EriAlarmAlertLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 2),
    _EriAlarmAlertLastChanged_Type()
)
eriAlarmAlertLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertLastChanged.setStatus("current")
_EriAlarmAlertLastSequenceNo_Type = EriAlarmSequenceNumber
_EriAlarmAlertLastSequenceNo_Object = MibScalar
eriAlarmAlertLastSequenceNo = _EriAlarmAlertLastSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 3),
    _EriAlarmAlertLastSequenceNo_Type()
)
eriAlarmAlertLastSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertLastSequenceNo.setStatus("current")
_EriAlarmAlertTableURL_Type = SnmpAdminString
_EriAlarmAlertTableURL_Object = MibScalar
eriAlarmAlertTableURL = _EriAlarmAlertTableURL_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 4),
    _EriAlarmAlertTableURL_Type()
)
eriAlarmAlertTableURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertTableURL.setStatus("current")
_EriAlarmAlertTable_Object = MibTable
eriAlarmAlertTable = _EriAlarmAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5)
)
if mibBuilder.loadTexts:
    eriAlarmAlertTable.setStatus("current")
_EriAlarmAlertEntry_Object = MibTableRow
eriAlarmAlertEntry = _EriAlarmAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1)
)
eriAlarmAlertEntry.setIndexNames(
    (0, "ERICSSON-ALARM-MIB", "eriAlarmAlertIndex"),
)
if mibBuilder.loadTexts:
    eriAlarmAlertEntry.setStatus("current")
_EriAlarmAlertIndex_Type = EriAlarmIndex
_EriAlarmAlertIndex_Object = MibTableColumn
eriAlarmAlertIndex = _EriAlarmAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 1),
    _EriAlarmAlertIndex_Type()
)
eriAlarmAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eriAlarmAlertIndex.setStatus("current")
_EriAlarmAlertMajorType_Type = EriAlarmType
_EriAlarmAlertMajorType_Object = MibTableColumn
eriAlarmAlertMajorType = _EriAlarmAlertMajorType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 2),
    _EriAlarmAlertMajorType_Type()
)
eriAlarmAlertMajorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertMajorType.setStatus("current")
_EriAlarmAlertMinorType_Type = EriAlarmType
_EriAlarmAlertMinorType_Object = MibTableColumn
eriAlarmAlertMinorType = _EriAlarmAlertMinorType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 3),
    _EriAlarmAlertMinorType_Type()
)
eriAlarmAlertMinorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertMinorType.setStatus("current")
_EriAlarmAlertSpecificProblem_Type = EriAlarmSpecificProblem
_EriAlarmAlertSpecificProblem_Object = MibTableColumn
eriAlarmAlertSpecificProblem = _EriAlarmAlertSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 4),
    _EriAlarmAlertSpecificProblem_Type()
)
eriAlarmAlertSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertSpecificProblem.setStatus("current")
_EriAlarmAlertManagedObject_Type = EriMO
_EriAlarmAlertManagedObject_Object = MibTableColumn
eriAlarmAlertManagedObject = _EriAlarmAlertManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 5),
    _EriAlarmAlertManagedObject_Type()
)
eriAlarmAlertManagedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertManagedObject.setStatus("current")
_EriAlarmAlertEventType_Type = IANAItuEventType
_EriAlarmAlertEventType_Object = MibTableColumn
eriAlarmAlertEventType = _EriAlarmAlertEventType_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 6),
    _EriAlarmAlertEventType_Type()
)
eriAlarmAlertEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertEventType.setStatus("current")
_EriAlarmAlertEventTime_Type = DateAndTime
_EriAlarmAlertEventTime_Object = MibTableColumn
eriAlarmAlertEventTime = _EriAlarmAlertEventTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 7),
    _EriAlarmAlertEventTime_Type()
)
eriAlarmAlertEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertEventTime.setStatus("current")
_EriAlarmAlertProbableCause_Type = EriProbableCause
_EriAlarmAlertProbableCause_Object = MibTableColumn
eriAlarmAlertProbableCause = _EriAlarmAlertProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 8),
    _EriAlarmAlertProbableCause_Type()
)
eriAlarmAlertProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertProbableCause.setStatus("current")
_EriAlarmAlertSeverity_Type = ItuPerceivedSeverity
_EriAlarmAlertSeverity_Object = MibTableColumn
eriAlarmAlertSeverity = _EriAlarmAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 9),
    _EriAlarmAlertSeverity_Type()
)
eriAlarmAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertSeverity.setStatus("current")
_EriAlarmAlertAdditionalText_Type = EriLargeAdditionalText
_EriAlarmAlertAdditionalText_Object = MibTableColumn
eriAlarmAlertAdditionalText = _EriAlarmAlertAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 10),
    _EriAlarmAlertAdditionalText_Type()
)
eriAlarmAlertAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertAdditionalText.setStatus("current")
_EriAlarmAlertResourceId_Type = ResourceId
_EriAlarmAlertResourceId_Object = MibTableColumn
eriAlarmAlertResourceId = _EriAlarmAlertResourceId_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 4, 5, 1, 11),
    _EriAlarmAlertResourceId_Type()
)
eriAlarmAlertResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eriAlarmAlertResourceId.setStatus("current")
_EriAlarmHeartBeat_ObjectIdentity = ObjectIdentity
eriAlarmHeartBeat = _EriAlarmHeartBeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 5)
)
_EriAlarmHbInterval_Type = Unsigned32
_EriAlarmHbInterval_Object = MibScalar
eriAlarmHbInterval = _EriAlarmHbInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 1, 5, 1),
    _EriAlarmHbInterval_Type()
)
eriAlarmHbInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eriAlarmHbInterval.setStatus("current")
_EriAlarmNotifications_ObjectIdentity = ObjectIdentity
eriAlarmNotifications = _EriAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2)
)
_EriAlarmNotifsPrefix_ObjectIdentity = ObjectIdentity
eriAlarmNotifsPrefix = _EriAlarmNotifsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0)
)
_EriAlarmConformance_ObjectIdentity = ObjectIdentity
eriAlarmConformance = _EriAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4)
)
_EriAlarmCompliances_ObjectIdentity = ObjectIdentity
eriAlarmCompliances = _EriAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 1)
)
_EriAlarmGroups_ObjectIdentity = ObjectIdentity
eriAlarmGroups = _EriAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2)
)

# Managed Objects groups

eriAlarmSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 1)
)
eriAlarmSummaryGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmSumIndeterminate"),
        ("ERICSSON-ALARM-MIB", "eriAlarmSumCritical"),
        ("ERICSSON-ALARM-MIB", "eriAlarmSumMajor"),
        ("ERICSSON-ALARM-MIB", "eriAlarmSumMinor"),
        ("ERICSSON-ALARM-MIB", "eriAlarmSumWarning"))
)
if mibBuilder.loadTexts:
    eriAlarmSummaryGroup.setStatus("current")

eriAlarmActiveAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 2)
)
eriAlarmActiveAlarmsGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveNumber"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastChanged"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveTableURL"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSeverity"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmActiveAlarmsGroup.setStatus("current")

eriAlarmAlertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 3)
)
eriAlarmAlertsGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertNumber"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastChanged"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertTableURL"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSeverity"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertAdditionalText"))
)
if mibBuilder.loadTexts:
    eriAlarmAlertsGroup.setStatus("current")

eriAlarmHeartBeatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 4)
)
eriAlarmHeartBeatGroup.setObjects(
    ("ERICSSON-ALARM-MIB", "eriAlarmHbInterval")
)
if mibBuilder.loadTexts:
    eriAlarmHeartBeatGroup.setStatus("current")

eriAlarmSNMPResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 5)
)
eriAlarmSNMPResourceGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveResourceId"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmSNMPResourceGroup.setStatus("current")

eriAlarmChangeAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 6)
)
eriAlarmChangeAlarmGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveOriginalEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveOriginalSeverity"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveOrigAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"))
)
if mibBuilder.loadTexts:
    eriAlarmChangeAlarmGroup.setStatus("current")


# Notification objects

eriAlarmIndeterminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 1)
)
eriAlarmIndeterminate.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmIndeterminate.setStatus(
        "current"
    )

eriAlarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 2)
)
eriAlarmWarning.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmWarning.setStatus(
        "current"
    )

eriAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 3)
)
eriAlarmMinor.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmMinor.setStatus(
        "current"
    )

eriAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 4)
)
eriAlarmMajor.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmMajor.setStatus(
        "current"
    )

eriAlarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 5)
)
eriAlarmCritical.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmCritical.setStatus(
        "current"
    )

eriAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 7)
)
eriAlarmCleared.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmCleared.setStatus(
        "current"
    )

eriAlarmAppendInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 8)
)
eriAlarmAppendInfo.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmAppendInfo.setStatus(
        "current"
    )

eriAlarmIndAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 10)
)
eriAlarmIndAlert.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmIndAlert.setStatus(
        "current"
    )

eriAlarmWarnAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 11)
)
eriAlarmWarnAlert.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmWarnAlert.setStatus(
        "current"
    )

eriAlarmMinorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 12)
)
eriAlarmMinorAlert.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmMinorAlert.setStatus(
        "current"
    )

eriAlarmMajorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 13)
)
eriAlarmMajorAlert.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmMajorAlert.setStatus(
        "current"
    )

eriAlarmCriticalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 14)
)
eriAlarmCriticalAlert.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertSpecificProblem"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertEventTime"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertProbableCause"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjMoreAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmCriticalAlert.setStatus(
        "current"
    )

eriAlarmAppendAlertInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 15)
)
eriAlarmAppendAlertInfo.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAlertManagedObject"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMajorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertMinorType"),
        ("ERICSSON-ALARM-MIB", "eriAlarmNObjAdditionalText"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertResourceId"))
)
if mibBuilder.loadTexts:
    eriAlarmAppendAlertInfo.setStatus(
        "current"
    )

eriAlarmHeartBeatNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 20)
)
eriAlarmHeartBeatNotif.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmActiveLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastSequenceNo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmActiveLastChanged"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlertLastChanged"))
)
if mibBuilder.loadTexts:
    eriAlarmHeartBeatNotif.setStatus(
        "current"
    )

eriAlarmAlarmListRebuilt = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 2, 0, 30)
)
eriAlarmAlarmListRebuilt.setObjects(
    ("ERICSSON-ALARM-MIB", "eriAlarmActiveTableURL")
)
if mibBuilder.loadTexts:
    eriAlarmAlarmListRebuilt.setStatus(
        "current"
    )


# Notifications groups

eriAlarmSimpleAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 10)
)
eriAlarmSimpleAlarmGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmIndeterminate"),
        ("ERICSSON-ALARM-MIB", "eriAlarmWarning"),
        ("ERICSSON-ALARM-MIB", "eriAlarmMinor"),
        ("ERICSSON-ALARM-MIB", "eriAlarmMajor"),
        ("ERICSSON-ALARM-MIB", "eriAlarmCritical"),
        ("ERICSSON-ALARM-MIB", "eriAlarmCleared"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAlarmListRebuilt"))
)
if mibBuilder.loadTexts:
    eriAlarmSimpleAlarmGroup.setStatus(
        "current"
    )

eriAlarmAddAddInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 12)
)
eriAlarmAddAddInfoGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmAppendInfo"),
        ("ERICSSON-ALARM-MIB", "eriAlarmAppendAlertInfo"))
)
if mibBuilder.loadTexts:
    eriAlarmAddAddInfoGroup.setStatus(
        "current"
    )

eriAlarmAlertNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 13)
)
eriAlarmAlertNotifGroup.setObjects(
      *(("ERICSSON-ALARM-MIB", "eriAlarmIndAlert"),
        ("ERICSSON-ALARM-MIB", "eriAlarmWarnAlert"),
        ("ERICSSON-ALARM-MIB", "eriAlarmMinorAlert"),
        ("ERICSSON-ALARM-MIB", "eriAlarmMajorAlert"),
        ("ERICSSON-ALARM-MIB", "eriAlarmCriticalAlert"))
)
if mibBuilder.loadTexts:
    eriAlarmAlertNotifGroup.setStatus(
        "current"
    )

eriAlarmHeartBeatNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 2, 14)
)
eriAlarmHeartBeatNotifGroup.setObjects(
    ("ERICSSON-ALARM-MIB", "eriAlarmHeartBeatNotif")
)
if mibBuilder.loadTexts:
    eriAlarmHeartBeatNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eriAlarmBasicAlarmsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 183, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    eriAlarmBasicAlarmsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ALARM-MIB",
    **{"ericssonAlarmMIB": ericssonAlarmMIB,
       "eriAlarmObjects": eriAlarmObjects,
       "eriAlarmSummary": eriAlarmSummary,
       "eriAlarmSumIndeterminate": eriAlarmSumIndeterminate,
       "eriAlarmSumCritical": eriAlarmSumCritical,
       "eriAlarmSumMajor": eriAlarmSumMajor,
       "eriAlarmSumMinor": eriAlarmSumMinor,
       "eriAlarmSumWarning": eriAlarmSumWarning,
       "eriAlarmNotifObjects": eriAlarmNotifObjects,
       "eriAlarmNObjAdditionalText": eriAlarmNObjAdditionalText,
       "eriAlarmNObjMoreAdditionalText": eriAlarmNObjMoreAdditionalText,
       "eriAlarmNObjResourceId": eriAlarmNObjResourceId,
       "eriAlarmActiveAlarms": eriAlarmActiveAlarms,
       "eriAlarmActiveNumber": eriAlarmActiveNumber,
       "eriAlarmActiveLastChanged": eriAlarmActiveLastChanged,
       "eriAlarmActiveLastSequenceNo": eriAlarmActiveLastSequenceNo,
       "eriAlarmActiveTableURL": eriAlarmActiveTableURL,
       "eriAlarmActiveAlarmTable": eriAlarmActiveAlarmTable,
       "eriAlarmActiveAlarmEntry": eriAlarmActiveAlarmEntry,
       "eriAlarmActiveIndex": eriAlarmActiveIndex,
       "eriAlarmActiveMajorType": eriAlarmActiveMajorType,
       "eriAlarmActiveMinorType": eriAlarmActiveMinorType,
       "eriAlarmActiveSpecificProblem": eriAlarmActiveSpecificProblem,
       "eriAlarmActiveManagedObject": eriAlarmActiveManagedObject,
       "eriAlarmActiveEventType": eriAlarmActiveEventType,
       "eriAlarmActiveEventTime": eriAlarmActiveEventTime,
       "eriAlarmActiveOriginalEventTime": eriAlarmActiveOriginalEventTime,
       "eriAlarmActiveProbableCause": eriAlarmActiveProbableCause,
       "eriAlarmActiveSeverity": eriAlarmActiveSeverity,
       "eriAlarmActiveOriginalSeverity": eriAlarmActiveOriginalSeverity,
       "eriAlarmActiveAdditionalText": eriAlarmActiveAdditionalText,
       "eriAlarmActiveOrigAdditionalText": eriAlarmActiveOrigAdditionalText,
       "eriAlarmActiveResourceId": eriAlarmActiveResourceId,
       "eriAlarmAlerts": eriAlarmAlerts,
       "eriAlarmAlertNumber": eriAlarmAlertNumber,
       "eriAlarmAlertLastChanged": eriAlarmAlertLastChanged,
       "eriAlarmAlertLastSequenceNo": eriAlarmAlertLastSequenceNo,
       "eriAlarmAlertTableURL": eriAlarmAlertTableURL,
       "eriAlarmAlertTable": eriAlarmAlertTable,
       "eriAlarmAlertEntry": eriAlarmAlertEntry,
       "eriAlarmAlertIndex": eriAlarmAlertIndex,
       "eriAlarmAlertMajorType": eriAlarmAlertMajorType,
       "eriAlarmAlertMinorType": eriAlarmAlertMinorType,
       "eriAlarmAlertSpecificProblem": eriAlarmAlertSpecificProblem,
       "eriAlarmAlertManagedObject": eriAlarmAlertManagedObject,
       "eriAlarmAlertEventType": eriAlarmAlertEventType,
       "eriAlarmAlertEventTime": eriAlarmAlertEventTime,
       "eriAlarmAlertProbableCause": eriAlarmAlertProbableCause,
       "eriAlarmAlertSeverity": eriAlarmAlertSeverity,
       "eriAlarmAlertAdditionalText": eriAlarmAlertAdditionalText,
       "eriAlarmAlertResourceId": eriAlarmAlertResourceId,
       "eriAlarmHeartBeat": eriAlarmHeartBeat,
       "eriAlarmHbInterval": eriAlarmHbInterval,
       "eriAlarmNotifications": eriAlarmNotifications,
       "eriAlarmNotifsPrefix": eriAlarmNotifsPrefix,
       "eriAlarmIndeterminate": eriAlarmIndeterminate,
       "eriAlarmWarning": eriAlarmWarning,
       "eriAlarmMinor": eriAlarmMinor,
       "eriAlarmMajor": eriAlarmMajor,
       "eriAlarmCritical": eriAlarmCritical,
       "eriAlarmCleared": eriAlarmCleared,
       "eriAlarmAppendInfo": eriAlarmAppendInfo,
       "eriAlarmIndAlert": eriAlarmIndAlert,
       "eriAlarmWarnAlert": eriAlarmWarnAlert,
       "eriAlarmMinorAlert": eriAlarmMinorAlert,
       "eriAlarmMajorAlert": eriAlarmMajorAlert,
       "eriAlarmCriticalAlert": eriAlarmCriticalAlert,
       "eriAlarmAppendAlertInfo": eriAlarmAppendAlertInfo,
       "eriAlarmHeartBeatNotif": eriAlarmHeartBeatNotif,
       "eriAlarmAlarmListRebuilt": eriAlarmAlarmListRebuilt,
       "eriAlarmConformance": eriAlarmConformance,
       "eriAlarmCompliances": eriAlarmCompliances,
       "eriAlarmBasicAlarmsCompliance": eriAlarmBasicAlarmsCompliance,
       "eriAlarmGroups": eriAlarmGroups,
       "eriAlarmSummaryGroup": eriAlarmSummaryGroup,
       "eriAlarmActiveAlarmsGroup": eriAlarmActiveAlarmsGroup,
       "eriAlarmAlertsGroup": eriAlarmAlertsGroup,
       "eriAlarmHeartBeatGroup": eriAlarmHeartBeatGroup,
       "eriAlarmSNMPResourceGroup": eriAlarmSNMPResourceGroup,
       "eriAlarmChangeAlarmGroup": eriAlarmChangeAlarmGroup,
       "eriAlarmSimpleAlarmGroup": eriAlarmSimpleAlarmGroup,
       "eriAlarmAddAddInfoGroup": eriAlarmAddAddInfoGroup,
       "eriAlarmAlertNotifGroup": eriAlarmAlertNotifGroup,
       "eriAlarmHeartBeatNotifGroup": eriAlarmHeartBeatNotifGroup}
)
