# SNMP MIB module (AcAlarm) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcAlarm
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:59 2024
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

(AcAlarmEventType,
 AcAlarmProbableCause,
 AcAlarmSeverity) = mibBuilder.importSymbols(
    "AC-FAULT-TC",
    "AcAlarmEventType",
    "AcAlarmProbableCause",
    "AcAlarmSeverity")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

acAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1)
)
acAlarm.setRevisions(
        ("2003-12-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcFault_ObjectIdentity = ObjectIdentity
acFault = _AcFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 11)
)
_AcActiveAlarm_ObjectIdentity = ObjectIdentity
acActiveAlarm = _AcActiveAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1)
)
_AcActiveAlarmTable_Object = MibTable
acActiveAlarmTable = _AcActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acActiveAlarmTable.setStatus("current")
_AcActiveAlarmEntry_Object = MibTableRow
acActiveAlarmEntry = _AcActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1)
)
acActiveAlarmEntry.setIndexNames(
    (0, "AcAlarm", "acActiveAlarmSequenceNumber"),
)
if mibBuilder.loadTexts:
    acActiveAlarmEntry.setStatus("current")
_AcActiveAlarmSequenceNumber_Type = Unsigned32
_AcActiveAlarmSequenceNumber_Object = MibTableColumn
acActiveAlarmSequenceNumber = _AcActiveAlarmSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 1),
    _AcActiveAlarmSequenceNumber_Type()
)
acActiveAlarmSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmSequenceNumber.setStatus("current")
_AcActiveAlarmSysuptime_Type = TimeStamp
_AcActiveAlarmSysuptime_Object = MibTableColumn
acActiveAlarmSysuptime = _AcActiveAlarmSysuptime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 2),
    _AcActiveAlarmSysuptime_Type()
)
acActiveAlarmSysuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmSysuptime.setStatus("current")
_AcActiveAlarmTrapOID_Type = ObjectIdentifier
_AcActiveAlarmTrapOID_Object = MibTableColumn
acActiveAlarmTrapOID = _AcActiveAlarmTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 3),
    _AcActiveAlarmTrapOID_Type()
)
acActiveAlarmTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmTrapOID.setStatus("current")
_AcActiveAlarmDateAndTime_Type = DateAndTime
_AcActiveAlarmDateAndTime_Object = MibTableColumn
acActiveAlarmDateAndTime = _AcActiveAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 4),
    _AcActiveAlarmDateAndTime_Type()
)
acActiveAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmDateAndTime.setStatus("current")
_AcActiveAlarmName_Type = Unsigned32
_AcActiveAlarmName_Object = MibTableColumn
acActiveAlarmName = _AcActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 5),
    _AcActiveAlarmName_Type()
)
acActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmName.setStatus("current")
_AcActiveAlarmTextualDescription_Type = SnmpAdminString
_AcActiveAlarmTextualDescription_Object = MibTableColumn
acActiveAlarmTextualDescription = _AcActiveAlarmTextualDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 6),
    _AcActiveAlarmTextualDescription_Type()
)
acActiveAlarmTextualDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmTextualDescription.setStatus("current")
_AcActiveAlarmSource_Type = SnmpAdminString
_AcActiveAlarmSource_Object = MibTableColumn
acActiveAlarmSource = _AcActiveAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 7),
    _AcActiveAlarmSource_Type()
)
acActiveAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmSource.setStatus("current")
_AcActiveAlarmSeverity_Type = AcAlarmSeverity
_AcActiveAlarmSeverity_Object = MibTableColumn
acActiveAlarmSeverity = _AcActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 8),
    _AcActiveAlarmSeverity_Type()
)
acActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmSeverity.setStatus("current")
_AcActiveAlarmEventType_Type = AcAlarmEventType
_AcActiveAlarmEventType_Object = MibTableColumn
acActiveAlarmEventType = _AcActiveAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 9),
    _AcActiveAlarmEventType_Type()
)
acActiveAlarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmEventType.setStatus("current")
_AcActiveAlarmProbableCause_Type = AcAlarmProbableCause
_AcActiveAlarmProbableCause_Object = MibTableColumn
acActiveAlarmProbableCause = _AcActiveAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 10),
    _AcActiveAlarmProbableCause_Type()
)
acActiveAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmProbableCause.setStatus("current")
_AcActiveAlarmAdditionalInfo1_Type = SnmpAdminString
_AcActiveAlarmAdditionalInfo1_Object = MibTableColumn
acActiveAlarmAdditionalInfo1 = _AcActiveAlarmAdditionalInfo1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 11),
    _AcActiveAlarmAdditionalInfo1_Type()
)
acActiveAlarmAdditionalInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmAdditionalInfo1.setStatus("current")
_AcActiveAlarmAdditionalInfo2_Type = SnmpAdminString
_AcActiveAlarmAdditionalInfo2_Object = MibTableColumn
acActiveAlarmAdditionalInfo2 = _AcActiveAlarmAdditionalInfo2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 12),
    _AcActiveAlarmAdditionalInfo2_Type()
)
acActiveAlarmAdditionalInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmAdditionalInfo2.setStatus("current")
_AcActiveAlarmAdditionalInfo3_Type = SnmpAdminString
_AcActiveAlarmAdditionalInfo3_Object = MibTableColumn
acActiveAlarmAdditionalInfo3 = _AcActiveAlarmAdditionalInfo3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 1, 1, 1, 13),
    _AcActiveAlarmAdditionalInfo3_Type()
)
acActiveAlarmAdditionalInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveAlarmAdditionalInfo3.setStatus("current")
_AcAlarmHistory_ObjectIdentity = ObjectIdentity
acAlarmHistory = _AcAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2)
)
_AcAlarmHistoryTable_Object = MibTable
acAlarmHistoryTable = _AcAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acAlarmHistoryTable.setStatus("current")
_AcAlarmHistoryEntry_Object = MibTableRow
acAlarmHistoryEntry = _AcAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1)
)
acAlarmHistoryEntry.setIndexNames(
    (0, "AcAlarm", "acAlarmHistorySequenceNumber"),
)
if mibBuilder.loadTexts:
    acAlarmHistoryEntry.setStatus("current")
_AcAlarmHistorySequenceNumber_Type = Unsigned32
_AcAlarmHistorySequenceNumber_Object = MibTableColumn
acAlarmHistorySequenceNumber = _AcAlarmHistorySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 1),
    _AcAlarmHistorySequenceNumber_Type()
)
acAlarmHistorySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistorySequenceNumber.setStatus("current")
_AcAlarmHistorySysuptime_Type = TimeStamp
_AcAlarmHistorySysuptime_Object = MibTableColumn
acAlarmHistorySysuptime = _AcAlarmHistorySysuptime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 2),
    _AcAlarmHistorySysuptime_Type()
)
acAlarmHistorySysuptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistorySysuptime.setStatus("current")
_AcAlarmHistoryTrapOID_Type = ObjectIdentifier
_AcAlarmHistoryTrapOID_Object = MibTableColumn
acAlarmHistoryTrapOID = _AcAlarmHistoryTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 3),
    _AcAlarmHistoryTrapOID_Type()
)
acAlarmHistoryTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryTrapOID.setStatus("current")
_AcAlarmHistoryDateAndTime_Type = DateAndTime
_AcAlarmHistoryDateAndTime_Object = MibTableColumn
acAlarmHistoryDateAndTime = _AcAlarmHistoryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 4),
    _AcAlarmHistoryDateAndTime_Type()
)
acAlarmHistoryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryDateAndTime.setStatus("current")
_AcAlarmHistoryName_Type = Unsigned32
_AcAlarmHistoryName_Object = MibTableColumn
acAlarmHistoryName = _AcAlarmHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 5),
    _AcAlarmHistoryName_Type()
)
acAlarmHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryName.setStatus("current")
_AcAlarmHistoryTextualDescription_Type = SnmpAdminString
_AcAlarmHistoryTextualDescription_Object = MibTableColumn
acAlarmHistoryTextualDescription = _AcAlarmHistoryTextualDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 6),
    _AcAlarmHistoryTextualDescription_Type()
)
acAlarmHistoryTextualDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryTextualDescription.setStatus("current")
_AcAlarmHistorySource_Type = SnmpAdminString
_AcAlarmHistorySource_Object = MibTableColumn
acAlarmHistorySource = _AcAlarmHistorySource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 7),
    _AcAlarmHistorySource_Type()
)
acAlarmHistorySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistorySource.setStatus("current")
_AcAlarmHistorySeverity_Type = AcAlarmSeverity
_AcAlarmHistorySeverity_Object = MibTableColumn
acAlarmHistorySeverity = _AcAlarmHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 8),
    _AcAlarmHistorySeverity_Type()
)
acAlarmHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistorySeverity.setStatus("current")
_AcAlarmHistoryEventType_Type = AcAlarmEventType
_AcAlarmHistoryEventType_Object = MibTableColumn
acAlarmHistoryEventType = _AcAlarmHistoryEventType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 9),
    _AcAlarmHistoryEventType_Type()
)
acAlarmHistoryEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryEventType.setStatus("current")
_AcAlarmHistoryProbableCause_Type = AcAlarmProbableCause
_AcAlarmHistoryProbableCause_Object = MibTableColumn
acAlarmHistoryProbableCause = _AcAlarmHistoryProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 10),
    _AcAlarmHistoryProbableCause_Type()
)
acAlarmHistoryProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryProbableCause.setStatus("current")
_AcAlarmHistoryAdditionalInfo1_Type = SnmpAdminString
_AcAlarmHistoryAdditionalInfo1_Object = MibTableColumn
acAlarmHistoryAdditionalInfo1 = _AcAlarmHistoryAdditionalInfo1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 11),
    _AcAlarmHistoryAdditionalInfo1_Type()
)
acAlarmHistoryAdditionalInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryAdditionalInfo1.setStatus("current")
_AcAlarmHistoryAdditionalInfo2_Type = SnmpAdminString
_AcAlarmHistoryAdditionalInfo2_Object = MibTableColumn
acAlarmHistoryAdditionalInfo2 = _AcAlarmHistoryAdditionalInfo2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 12),
    _AcAlarmHistoryAdditionalInfo2_Type()
)
acAlarmHistoryAdditionalInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryAdditionalInfo2.setStatus("current")
_AcAlarmHistoryAdditionalInfo3_Type = SnmpAdminString
_AcAlarmHistoryAdditionalInfo3_Object = MibTableColumn
acAlarmHistoryAdditionalInfo3 = _AcAlarmHistoryAdditionalInfo3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 2, 1, 1, 13),
    _AcAlarmHistoryAdditionalInfo3_Type()
)
acAlarmHistoryAdditionalInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAlarmHistoryAdditionalInfo3.setStatus("current")
_AcAlarmVarbinds_ObjectIdentity = ObjectIdentity
acAlarmVarbinds = _AcAlarmVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3)
)
_AcAlarmVarbindsSequenceNumber_Type = Unsigned32
_AcAlarmVarbindsSequenceNumber_Object = MibScalar
acAlarmVarbindsSequenceNumber = _AcAlarmVarbindsSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 1),
    _AcAlarmVarbindsSequenceNumber_Type()
)
acAlarmVarbindsSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsSequenceNumber.setStatus("current")
_AcAlarmVarbindsDateAndTime_Type = DateAndTime
_AcAlarmVarbindsDateAndTime_Object = MibScalar
acAlarmVarbindsDateAndTime = _AcAlarmVarbindsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 2),
    _AcAlarmVarbindsDateAndTime_Type()
)
acAlarmVarbindsDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsDateAndTime.setStatus("current")
_AcAlarmVarbindsAlarmName_Type = Unsigned32
_AcAlarmVarbindsAlarmName_Object = MibScalar
acAlarmVarbindsAlarmName = _AcAlarmVarbindsAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 3),
    _AcAlarmVarbindsAlarmName_Type()
)
acAlarmVarbindsAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsAlarmName.setStatus("current")
_AcAlarmVarbindsTextualDescription_Type = SnmpAdminString
_AcAlarmVarbindsTextualDescription_Object = MibScalar
acAlarmVarbindsTextualDescription = _AcAlarmVarbindsTextualDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 4),
    _AcAlarmVarbindsTextualDescription_Type()
)
acAlarmVarbindsTextualDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsTextualDescription.setStatus("current")
_AcAlarmVarbindsSource_Type = SnmpAdminString
_AcAlarmVarbindsSource_Object = MibScalar
acAlarmVarbindsSource = _AcAlarmVarbindsSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 5),
    _AcAlarmVarbindsSource_Type()
)
acAlarmVarbindsSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsSource.setStatus("current")
_AcAlarmVarbindsSeverity_Type = AcAlarmSeverity
_AcAlarmVarbindsSeverity_Object = MibScalar
acAlarmVarbindsSeverity = _AcAlarmVarbindsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 6),
    _AcAlarmVarbindsSeverity_Type()
)
acAlarmVarbindsSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsSeverity.setStatus("current")
_AcAlarmVarbindsEventType_Type = AcAlarmEventType
_AcAlarmVarbindsEventType_Object = MibScalar
acAlarmVarbindsEventType = _AcAlarmVarbindsEventType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 7),
    _AcAlarmVarbindsEventType_Type()
)
acAlarmVarbindsEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsEventType.setStatus("current")
_AcAlarmVarbindsProbableCause_Type = AcAlarmProbableCause
_AcAlarmVarbindsProbableCause_Object = MibScalar
acAlarmVarbindsProbableCause = _AcAlarmVarbindsProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 8),
    _AcAlarmVarbindsProbableCause_Type()
)
acAlarmVarbindsProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsProbableCause.setStatus("current")
_AcAlarmVarbindsAdditionalInfo1_Type = SnmpAdminString
_AcAlarmVarbindsAdditionalInfo1_Object = MibScalar
acAlarmVarbindsAdditionalInfo1 = _AcAlarmVarbindsAdditionalInfo1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 9),
    _AcAlarmVarbindsAdditionalInfo1_Type()
)
acAlarmVarbindsAdditionalInfo1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsAdditionalInfo1.setStatus("current")
_AcAlarmVarbindsAdditionalInfo2_Type = SnmpAdminString
_AcAlarmVarbindsAdditionalInfo2_Object = MibScalar
acAlarmVarbindsAdditionalInfo2 = _AcAlarmVarbindsAdditionalInfo2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 10),
    _AcAlarmVarbindsAdditionalInfo2_Type()
)
acAlarmVarbindsAdditionalInfo2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsAdditionalInfo2.setStatus("current")
_AcAlarmVarbindsAdditionalInfo3_Type = SnmpAdminString
_AcAlarmVarbindsAdditionalInfo3_Object = MibScalar
acAlarmVarbindsAdditionalInfo3 = _AcAlarmVarbindsAdditionalInfo3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 11, 1, 3, 11),
    _AcAlarmVarbindsAdditionalInfo3_Type()
)
acAlarmVarbindsAdditionalInfo3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAlarmVarbindsAdditionalInfo3.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcAlarm",
    **{"audioCodes": audioCodes,
       "acFault": acFault,
       "acAlarm": acAlarm,
       "acActiveAlarm": acActiveAlarm,
       "acActiveAlarmTable": acActiveAlarmTable,
       "acActiveAlarmEntry": acActiveAlarmEntry,
       "acActiveAlarmSequenceNumber": acActiveAlarmSequenceNumber,
       "acActiveAlarmSysuptime": acActiveAlarmSysuptime,
       "acActiveAlarmTrapOID": acActiveAlarmTrapOID,
       "acActiveAlarmDateAndTime": acActiveAlarmDateAndTime,
       "acActiveAlarmName": acActiveAlarmName,
       "acActiveAlarmTextualDescription": acActiveAlarmTextualDescription,
       "acActiveAlarmSource": acActiveAlarmSource,
       "acActiveAlarmSeverity": acActiveAlarmSeverity,
       "acActiveAlarmEventType": acActiveAlarmEventType,
       "acActiveAlarmProbableCause": acActiveAlarmProbableCause,
       "acActiveAlarmAdditionalInfo1": acActiveAlarmAdditionalInfo1,
       "acActiveAlarmAdditionalInfo2": acActiveAlarmAdditionalInfo2,
       "acActiveAlarmAdditionalInfo3": acActiveAlarmAdditionalInfo3,
       "acAlarmHistory": acAlarmHistory,
       "acAlarmHistoryTable": acAlarmHistoryTable,
       "acAlarmHistoryEntry": acAlarmHistoryEntry,
       "acAlarmHistorySequenceNumber": acAlarmHistorySequenceNumber,
       "acAlarmHistorySysuptime": acAlarmHistorySysuptime,
       "acAlarmHistoryTrapOID": acAlarmHistoryTrapOID,
       "acAlarmHistoryDateAndTime": acAlarmHistoryDateAndTime,
       "acAlarmHistoryName": acAlarmHistoryName,
       "acAlarmHistoryTextualDescription": acAlarmHistoryTextualDescription,
       "acAlarmHistorySource": acAlarmHistorySource,
       "acAlarmHistorySeverity": acAlarmHistorySeverity,
       "acAlarmHistoryEventType": acAlarmHistoryEventType,
       "acAlarmHistoryProbableCause": acAlarmHistoryProbableCause,
       "acAlarmHistoryAdditionalInfo1": acAlarmHistoryAdditionalInfo1,
       "acAlarmHistoryAdditionalInfo2": acAlarmHistoryAdditionalInfo2,
       "acAlarmHistoryAdditionalInfo3": acAlarmHistoryAdditionalInfo3,
       "acAlarmVarbinds": acAlarmVarbinds,
       "acAlarmVarbindsSequenceNumber": acAlarmVarbindsSequenceNumber,
       "acAlarmVarbindsDateAndTime": acAlarmVarbindsDateAndTime,
       "acAlarmVarbindsAlarmName": acAlarmVarbindsAlarmName,
       "acAlarmVarbindsTextualDescription": acAlarmVarbindsTextualDescription,
       "acAlarmVarbindsSource": acAlarmVarbindsSource,
       "acAlarmVarbindsSeverity": acAlarmVarbindsSeverity,
       "acAlarmVarbindsEventType": acAlarmVarbindsEventType,
       "acAlarmVarbindsProbableCause": acAlarmVarbindsProbableCause,
       "acAlarmVarbindsAdditionalInfo1": acAlarmVarbindsAdditionalInfo1,
       "acAlarmVarbindsAdditionalInfo2": acAlarmVarbindsAdditionalInfo2,
       "acAlarmVarbindsAdditionalInfo3": acAlarmVarbindsAdditionalInfo3}
)
