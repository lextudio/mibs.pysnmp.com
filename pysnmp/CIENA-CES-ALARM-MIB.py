# SNMP MIB module (CIENA-CES-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:54 2024
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
 alarmClearDateAndTime,
 alarmClearIndex,
 alarmListName,
 alarmModelIndex,
 alarmModelState) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmActiveDateAndTime",
    "alarmActiveIndex",
    "alarmClearDateAndTime",
    "alarmClearIndex",
    "alarmListName",
    "alarmModelIndex",
    "alarmModelState")

(cienaCesConfig,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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


# MODULE-IDENTITY

cienaCesAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24)
)
cienaCesAlarmMIB.setRevisions(
        ("2016-11-07 00:00",
         "2016-02-22 00:00",
         "2015-09-16 00:00",
         "2015-05-13 00:00",
         "2012-03-14 01:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesAlarmMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBObjects = _CienaCesAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1)
)
_CienaCesAlarmGlobal_ObjectIdentity = ObjectIdentity
cienaCesAlarmGlobal = _CienaCesAlarmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 1)
)
_CienaCesAlarmCutOff_Type = TruthValue
_CienaCesAlarmCutOff_Object = MibScalar
cienaCesAlarmCutOff = _CienaCesAlarmCutOff_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 1, 1),
    _CienaCesAlarmCutOff_Type()
)
cienaCesAlarmCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesAlarmCutOff.setStatus("current")
_CienaCesAlarm_ObjectIdentity = ObjectIdentity
cienaCesAlarm = _CienaCesAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2)
)
_CienaCesAlarmTable_Object = MibTable
cienaCesAlarmTable = _CienaCesAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesAlarmTable.setStatus("current")
_CienaCesAlarmEntry_Object = MibTableRow
cienaCesAlarmEntry = _CienaCesAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1)
)
cienaCesAlarmEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmModelIndex"),
    (0, "ALARM-MIB", "alarmModelState"),
)
if mibBuilder.loadTexts:
    cienaCesAlarmEntry.setStatus("current")
_CienaCesAlarmDescription_Type = DisplayString
_CienaCesAlarmDescription_Object = MibTableColumn
cienaCesAlarmDescription = _CienaCesAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 1),
    _CienaCesAlarmDescription_Type()
)
cienaCesAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmDescription.setStatus("current")


class _CienaCesAlarmThreshold_Type(Integer32):
    """Custom type cienaCesAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesAlarmThreshold_Type.__name__ = "Integer32"
_CienaCesAlarmThreshold_Object = MibTableColumn
cienaCesAlarmThreshold = _CienaCesAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 2),
    _CienaCesAlarmThreshold_Type()
)
cienaCesAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmThreshold.setStatus("current")


class _CienaCesAlarmLeak_Type(Integer32):
    """Custom type cienaCesAlarmLeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesAlarmLeak_Type.__name__ = "Integer32"
_CienaCesAlarmLeak_Object = MibTableColumn
cienaCesAlarmLeak = _CienaCesAlarmLeak_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 3),
    _CienaCesAlarmLeak_Type()
)
cienaCesAlarmLeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLeak.setStatus("current")
_CienaCesAlarmGPO_Type = TruthValue
_CienaCesAlarmGPO_Object = MibTableColumn
cienaCesAlarmGPO = _CienaCesAlarmGPO_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 4),
    _CienaCesAlarmGPO_Type()
)
cienaCesAlarmGPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmGPO.setStatus("current")
_CienaCesAlarmEvery_Type = Integer32
_CienaCesAlarmEvery_Object = MibTableColumn
cienaCesAlarmEvery = _CienaCesAlarmEvery_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 5),
    _CienaCesAlarmEvery_Type()
)
cienaCesAlarmEvery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmEvery.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesAlarmEvery.setUnits("seconds")
_CienaCesAlarmToMinor_Type = Integer32
_CienaCesAlarmToMinor_Object = MibTableColumn
cienaCesAlarmToMinor = _CienaCesAlarmToMinor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 6),
    _CienaCesAlarmToMinor_Type()
)
cienaCesAlarmToMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmToMinor.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesAlarmToMinor.setUnits("seconds")
_CienaCesAlarmToMajor_Type = Integer32
_CienaCesAlarmToMajor_Object = MibTableColumn
cienaCesAlarmToMajor = _CienaCesAlarmToMajor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 7),
    _CienaCesAlarmToMajor_Type()
)
cienaCesAlarmToMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmToMajor.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesAlarmToMajor.setUnits("seconds")
_CienaCesAlarmToCritical_Type = Integer32
_CienaCesAlarmToCritical_Object = MibTableColumn
cienaCesAlarmToCritical = _CienaCesAlarmToCritical_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 8),
    _CienaCesAlarmToCritical_Type()
)
cienaCesAlarmToCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmToCritical.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesAlarmToCritical.setUnits("seconds")
_CienaCesAlarmSense_Type = TruthValue
_CienaCesAlarmSense_Object = MibTableColumn
cienaCesAlarmSense = _CienaCesAlarmSense_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 9),
    _CienaCesAlarmSense_Type()
)
cienaCesAlarmSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmSense.setStatus("current")
_CienaCesAlarmTrigger_Type = TruthValue
_CienaCesAlarmTrigger_Object = MibTableColumn
cienaCesAlarmTrigger = _CienaCesAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 1, 1, 10),
    _CienaCesAlarmTrigger_Type()
)
cienaCesAlarmTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmTrigger.setStatus("current")
_CienaCesAlarmSeverityTable_Object = MibTable
cienaCesAlarmSeverityTable = _CienaCesAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesAlarmSeverityTable.setStatus("current")
_CienaCesAlarmSeverityEntry_Object = MibTableRow
cienaCesAlarmSeverityEntry = _CienaCesAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 2, 1)
)
cienaCesAlarmSeverityEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmModelIndex"),
)
if mibBuilder.loadTexts:
    cienaCesAlarmSeverityEntry.setStatus("current")
_CienaCesAlarmSeverity_Type = ItuPerceivedSeverity
_CienaCesAlarmSeverity_Object = MibTableColumn
cienaCesAlarmSeverity = _CienaCesAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 2, 2, 1, 1),
    _CienaCesAlarmSeverity_Type()
)
cienaCesAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmSeverity.setStatus("current")
_CienaCesAlarmActive_ObjectIdentity = ObjectIdentity
cienaCesAlarmActive = _CienaCesAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3)
)
_CienaCesAlarmActiveTable_Object = MibTable
cienaCesAlarmActiveTable = _CienaCesAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesAlarmActiveTable.setStatus("current")
_CienaCesAlarmActiveEntry_Object = MibTableRow
cienaCesAlarmActiveEntry = _CienaCesAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1)
)
cienaCesAlarmActiveEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmActiveIndex"),
    (0, "ALARM-MIB", "alarmActiveDateAndTime"),
)
if mibBuilder.loadTexts:
    cienaCesAlarmActiveEntry.setStatus("current")
_CienaCesAlarmActiveSeverity_Type = ItuPerceivedSeverity
_CienaCesAlarmActiveSeverity_Object = MibTableColumn
cienaCesAlarmActiveSeverity = _CienaCesAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 1),
    _CienaCesAlarmActiveSeverity_Type()
)
cienaCesAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveSeverity.setStatus("current")
_CienaCesAlarmActiveInvokeId_Type = Integer32
_CienaCesAlarmActiveInvokeId_Object = MibTableColumn
cienaCesAlarmActiveInvokeId = _CienaCesAlarmActiveInvokeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 2),
    _CienaCesAlarmActiveInvokeId_Type()
)
cienaCesAlarmActiveInvokeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveInvokeId.setStatus("current")


class _CienaCesAlarmActiveManagedObjectClass_Type(Integer32):
    """Custom type cienaCesAlarmActiveManagedObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 2),
          ("port", 4),
          ("slot", 3),
          ("unknown", 1))
    )


_CienaCesAlarmActiveManagedObjectClass_Type.__name__ = "Integer32"
_CienaCesAlarmActiveManagedObjectClass_Object = MibTableColumn
cienaCesAlarmActiveManagedObjectClass = _CienaCesAlarmActiveManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 3),
    _CienaCesAlarmActiveManagedObjectClass_Type()
)
cienaCesAlarmActiveManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveManagedObjectClass.setStatus("current")


class _CienaCesAlarmActiveManagedObjectInterpret_Type(OctetString):
    """Custom type cienaCesAlarmActiveManagedObjectInterpret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CienaCesAlarmActiveManagedObjectInterpret_Type.__name__ = "OctetString"
_CienaCesAlarmActiveManagedObjectInterpret_Object = MibTableColumn
cienaCesAlarmActiveManagedObjectInterpret = _CienaCesAlarmActiveManagedObjectInterpret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 4),
    _CienaCesAlarmActiveManagedObjectInterpret_Type()
)
cienaCesAlarmActiveManagedObjectInterpret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveManagedObjectInterpret.setStatus("current")


class _CienaCesAlarmActiveManagedObjectInstance_Type(OctetString):
    """Custom type cienaCesAlarmActiveManagedObjectInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CienaCesAlarmActiveManagedObjectInstance_Type.__name__ = "OctetString"
_CienaCesAlarmActiveManagedObjectInstance_Object = MibTableColumn
cienaCesAlarmActiveManagedObjectInstance = _CienaCesAlarmActiveManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 5),
    _CienaCesAlarmActiveManagedObjectInstance_Type()
)
cienaCesAlarmActiveManagedObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveManagedObjectInstance.setStatus("current")
_CienaCesAlarmActiveAck_Type = TruthValue
_CienaCesAlarmActiveAck_Object = MibTableColumn
cienaCesAlarmActiveAck = _CienaCesAlarmActiveAck_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 6),
    _CienaCesAlarmActiveAck_Type()
)
cienaCesAlarmActiveAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveAck.setStatus("current")
_CienaCesAlarmActiveDescription_Type = DisplayString
_CienaCesAlarmActiveDescription_Object = MibTableColumn
cienaCesAlarmActiveDescription = _CienaCesAlarmActiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 7),
    _CienaCesAlarmActiveDescription_Type()
)
cienaCesAlarmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveDescription.setStatus("current")
_CienaCesAlarmActiveTimeStamp_Type = DisplayString
_CienaCesAlarmActiveTimeStamp_Object = MibTableColumn
cienaCesAlarmActiveTimeStamp = _CienaCesAlarmActiveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 3, 1, 1, 8),
    _CienaCesAlarmActiveTimeStamp_Type()
)
cienaCesAlarmActiveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmActiveTimeStamp.setStatus("current")
_CienaCesAlarmClear_ObjectIdentity = ObjectIdentity
cienaCesAlarmClear = _CienaCesAlarmClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4)
)
_CienaCesAlarmClearTable_Object = MibTable
cienaCesAlarmClearTable = _CienaCesAlarmClearTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesAlarmClearTable.setStatus("current")
_CienaCesAlarmClearEntry_Object = MibTableRow
cienaCesAlarmClearEntry = _CienaCesAlarmClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4, 1, 1)
)
cienaCesAlarmClearEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmClearIndex"),
    (0, "ALARM-MIB", "alarmClearDateAndTime"),
)
if mibBuilder.loadTexts:
    cienaCesAlarmClearEntry.setStatus("current")


class _CienaCesAlarmClearManagedObjectClass_Type(Integer32):
    """Custom type cienaCesAlarmClearManagedObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 2),
          ("port", 4),
          ("slot", 3),
          ("unknown", 1))
    )


_CienaCesAlarmClearManagedObjectClass_Type.__name__ = "Integer32"
_CienaCesAlarmClearManagedObjectClass_Object = MibTableColumn
cienaCesAlarmClearManagedObjectClass = _CienaCesAlarmClearManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4, 1, 1, 3),
    _CienaCesAlarmClearManagedObjectClass_Type()
)
cienaCesAlarmClearManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmClearManagedObjectClass.setStatus("current")


class _CienaCesAlarmClearManagedObjectInterpret_Type(OctetString):
    """Custom type cienaCesAlarmClearManagedObjectInterpret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CienaCesAlarmClearManagedObjectInterpret_Type.__name__ = "OctetString"
_CienaCesAlarmClearManagedObjectInterpret_Object = MibTableColumn
cienaCesAlarmClearManagedObjectInterpret = _CienaCesAlarmClearManagedObjectInterpret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4, 1, 1, 4),
    _CienaCesAlarmClearManagedObjectInterpret_Type()
)
cienaCesAlarmClearManagedObjectInterpret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmClearManagedObjectInterpret.setStatus("current")


class _CienaCesAlarmClearManagedObjectInstance_Type(OctetString):
    """Custom type cienaCesAlarmClearManagedObjectInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CienaCesAlarmClearManagedObjectInstance_Type.__name__ = "OctetString"
_CienaCesAlarmClearManagedObjectInstance_Object = MibTableColumn
cienaCesAlarmClearManagedObjectInstance = _CienaCesAlarmClearManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 4, 1, 1, 5),
    _CienaCesAlarmClearManagedObjectInstance_Type()
)
cienaCesAlarmClearManagedObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmClearManagedObjectInstance.setStatus("current")
_CienaCesAlarmLog_ObjectIdentity = ObjectIdentity
cienaCesAlarmLog = _CienaCesAlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5)
)
_CienaCesAlarmLogTable_Object = MibTable
cienaCesAlarmLogTable = _CienaCesAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cienaCesAlarmLogTable.setStatus("current")
_CienaCesAlarmLogEntry_Object = MibTableRow
cienaCesAlarmLogEntry = _CienaCesAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1)
)
cienaCesAlarmLogEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "CIENA-CES-ALARM-MIB", "cienaCesAlarmLogIndex"),
)
if mibBuilder.loadTexts:
    cienaCesAlarmLogEntry.setStatus("current")


class _CienaCesAlarmLogIndex_Type(Unsigned32):
    """Custom type cienaCesAlarmLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesAlarmLogIndex_Type.__name__ = "Unsigned32"
_CienaCesAlarmLogIndex_Object = MibTableColumn
cienaCesAlarmLogIndex = _CienaCesAlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 1),
    _CienaCesAlarmLogIndex_Type()
)
cienaCesAlarmLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAlarmLogIndex.setStatus("current")
_CienaCesAlarmLogSeverity_Type = ItuPerceivedSeverity
_CienaCesAlarmLogSeverity_Object = MibTableColumn
cienaCesAlarmLogSeverity = _CienaCesAlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 2),
    _CienaCesAlarmLogSeverity_Type()
)
cienaCesAlarmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogSeverity.setStatus("current")


class _CienaCesAlarmLogManagedObjectClass_Type(Integer32):
    """Custom type cienaCesAlarmLogManagedObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 2),
          ("port", 4),
          ("slot", 3),
          ("unknown", 1))
    )


_CienaCesAlarmLogManagedObjectClass_Type.__name__ = "Integer32"
_CienaCesAlarmLogManagedObjectClass_Object = MibTableColumn
cienaCesAlarmLogManagedObjectClass = _CienaCesAlarmLogManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 3),
    _CienaCesAlarmLogManagedObjectClass_Type()
)
cienaCesAlarmLogManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogManagedObjectClass.setStatus("current")


class _CienaCesAlarmLogManagedObjectInterpret_Type(OctetString):
    """Custom type cienaCesAlarmLogManagedObjectInterpret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CienaCesAlarmLogManagedObjectInterpret_Type.__name__ = "OctetString"
_CienaCesAlarmLogManagedObjectInterpret_Object = MibTableColumn
cienaCesAlarmLogManagedObjectInterpret = _CienaCesAlarmLogManagedObjectInterpret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 4),
    _CienaCesAlarmLogManagedObjectInterpret_Type()
)
cienaCesAlarmLogManagedObjectInterpret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogManagedObjectInterpret.setStatus("current")


class _CienaCesAlarmLogManagedObjectInstance_Type(OctetString):
    """Custom type cienaCesAlarmLogManagedObjectInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CienaCesAlarmLogManagedObjectInstance_Type.__name__ = "OctetString"
_CienaCesAlarmLogManagedObjectInstance_Object = MibTableColumn
cienaCesAlarmLogManagedObjectInstance = _CienaCesAlarmLogManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 5),
    _CienaCesAlarmLogManagedObjectInstance_Type()
)
cienaCesAlarmLogManagedObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogManagedObjectInstance.setStatus("current")


class _CienaCesAlarmLogModelIndex_Type(Unsigned32):
    """Custom type cienaCesAlarmLogModelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesAlarmLogModelIndex_Type.__name__ = "Unsigned32"
_CienaCesAlarmLogModelIndex_Object = MibTableColumn
cienaCesAlarmLogModelIndex = _CienaCesAlarmLogModelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 6),
    _CienaCesAlarmLogModelIndex_Type()
)
cienaCesAlarmLogModelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogModelIndex.setStatus("current")
_CienaCesAlarmLogTimeStamp_Type = DisplayString
_CienaCesAlarmLogTimeStamp_Object = MibTableColumn
cienaCesAlarmLogTimeStamp = _CienaCesAlarmLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 1, 5, 1, 1, 7),
    _CienaCesAlarmLogTimeStamp_Type()
)
cienaCesAlarmLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAlarmLogTimeStamp.setStatus("current")
_CienaCesAlarmMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBNotificationPrefix = _CienaCesAlarmMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 2)
)
_CienaCesAlarmMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBNotifications = _CienaCesAlarmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 2, 0)
)
_CienaCesAlarmMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBConformance = _CienaCesAlarmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 3)
)
_CienaCesAlarmMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBCompliances = _CienaCesAlarmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 3, 1)
)
_CienaCesAlarmMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesAlarmMIBGroups = _CienaCesAlarmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 24, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-ALARM-MIB",
    **{"cienaCesAlarmMIB": cienaCesAlarmMIB,
       "cienaCesAlarmMIBObjects": cienaCesAlarmMIBObjects,
       "cienaCesAlarmGlobal": cienaCesAlarmGlobal,
       "cienaCesAlarmCutOff": cienaCesAlarmCutOff,
       "cienaCesAlarm": cienaCesAlarm,
       "cienaCesAlarmTable": cienaCesAlarmTable,
       "cienaCesAlarmEntry": cienaCesAlarmEntry,
       "cienaCesAlarmDescription": cienaCesAlarmDescription,
       "cienaCesAlarmThreshold": cienaCesAlarmThreshold,
       "cienaCesAlarmLeak": cienaCesAlarmLeak,
       "cienaCesAlarmGPO": cienaCesAlarmGPO,
       "cienaCesAlarmEvery": cienaCesAlarmEvery,
       "cienaCesAlarmToMinor": cienaCesAlarmToMinor,
       "cienaCesAlarmToMajor": cienaCesAlarmToMajor,
       "cienaCesAlarmToCritical": cienaCesAlarmToCritical,
       "cienaCesAlarmSense": cienaCesAlarmSense,
       "cienaCesAlarmTrigger": cienaCesAlarmTrigger,
       "cienaCesAlarmSeverityTable": cienaCesAlarmSeverityTable,
       "cienaCesAlarmSeverityEntry": cienaCesAlarmSeverityEntry,
       "cienaCesAlarmSeverity": cienaCesAlarmSeverity,
       "cienaCesAlarmActive": cienaCesAlarmActive,
       "cienaCesAlarmActiveTable": cienaCesAlarmActiveTable,
       "cienaCesAlarmActiveEntry": cienaCesAlarmActiveEntry,
       "cienaCesAlarmActiveSeverity": cienaCesAlarmActiveSeverity,
       "cienaCesAlarmActiveInvokeId": cienaCesAlarmActiveInvokeId,
       "cienaCesAlarmActiveManagedObjectClass": cienaCesAlarmActiveManagedObjectClass,
       "cienaCesAlarmActiveManagedObjectInterpret": cienaCesAlarmActiveManagedObjectInterpret,
       "cienaCesAlarmActiveManagedObjectInstance": cienaCesAlarmActiveManagedObjectInstance,
       "cienaCesAlarmActiveAck": cienaCesAlarmActiveAck,
       "cienaCesAlarmActiveDescription": cienaCesAlarmActiveDescription,
       "cienaCesAlarmActiveTimeStamp": cienaCesAlarmActiveTimeStamp,
       "cienaCesAlarmClear": cienaCesAlarmClear,
       "cienaCesAlarmClearTable": cienaCesAlarmClearTable,
       "cienaCesAlarmClearEntry": cienaCesAlarmClearEntry,
       "cienaCesAlarmClearManagedObjectClass": cienaCesAlarmClearManagedObjectClass,
       "cienaCesAlarmClearManagedObjectInterpret": cienaCesAlarmClearManagedObjectInterpret,
       "cienaCesAlarmClearManagedObjectInstance": cienaCesAlarmClearManagedObjectInstance,
       "cienaCesAlarmLog": cienaCesAlarmLog,
       "cienaCesAlarmLogTable": cienaCesAlarmLogTable,
       "cienaCesAlarmLogEntry": cienaCesAlarmLogEntry,
       "cienaCesAlarmLogIndex": cienaCesAlarmLogIndex,
       "cienaCesAlarmLogSeverity": cienaCesAlarmLogSeverity,
       "cienaCesAlarmLogManagedObjectClass": cienaCesAlarmLogManagedObjectClass,
       "cienaCesAlarmLogManagedObjectInterpret": cienaCesAlarmLogManagedObjectInterpret,
       "cienaCesAlarmLogManagedObjectInstance": cienaCesAlarmLogManagedObjectInstance,
       "cienaCesAlarmLogModelIndex": cienaCesAlarmLogModelIndex,
       "cienaCesAlarmLogTimeStamp": cienaCesAlarmLogTimeStamp,
       "cienaCesAlarmMIBNotificationPrefix": cienaCesAlarmMIBNotificationPrefix,
       "cienaCesAlarmMIBNotifications": cienaCesAlarmMIBNotifications,
       "cienaCesAlarmMIBConformance": cienaCesAlarmMIBConformance,
       "cienaCesAlarmMIBCompliances": cienaCesAlarmMIBCompliances,
       "cienaCesAlarmMIBGroups": cienaCesAlarmMIBGroups}
)
