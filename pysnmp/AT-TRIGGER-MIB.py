# SNMP MIB module (AT-TRIGGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-TRIGGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:35 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

trigger = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53)
)
trigger.setRevisions(
        ("2010-09-07 00:00",
         "2010-06-15 00:15",
         "2007-11-28 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TriggerTraps_ObjectIdentity = ObjectIdentity
triggerTraps = _TriggerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0)
)
_TriggerLastTriggerActivated_Type = Integer32
_TriggerLastTriggerActivated_Object = MibScalar
triggerLastTriggerActivated = _TriggerLastTriggerActivated_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 1),
    _TriggerLastTriggerActivated_Type()
)
triggerLastTriggerActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerLastTriggerActivated.setStatus("current")
_TriggerConfigInfoTable_Object = MibTable
triggerConfigInfoTable = _TriggerConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9)
)
if mibBuilder.loadTexts:
    triggerConfigInfoTable.setStatus("current")
_TriggerConfigInfoEntry_Object = MibTableRow
triggerConfigInfoEntry = _TriggerConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1)
)
triggerConfigInfoEntry.setIndexNames(
    (0, "AT-TRIGGER-MIB", "triggerNumber"),
)
if mibBuilder.loadTexts:
    triggerConfigInfoEntry.setStatus("current")


class _TriggerNumber_Type(Unsigned32):
    """Custom type triggerNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_TriggerNumber_Type.__name__ = "Unsigned32"
_TriggerNumber_Object = MibTableColumn
triggerNumber = _TriggerNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 1),
    _TriggerNumber_Type()
)
triggerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumber.setStatus("current")
_TriggerName_Type = DisplayString
_TriggerName_Object = MibTableColumn
triggerName = _TriggerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 2),
    _TriggerName_Type()
)
triggerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerName.setStatus("current")
_TriggerTypeDetail_Type = DisplayString
_TriggerTypeDetail_Object = MibTableColumn
triggerTypeDetail = _TriggerTypeDetail_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 3),
    _TriggerTypeDetail_Type()
)
triggerTypeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerTypeDetail.setStatus("current")
_TriggerActiveDaysOrDate_Type = DisplayString
_TriggerActiveDaysOrDate_Object = MibTableColumn
triggerActiveDaysOrDate = _TriggerActiveDaysOrDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 4),
    _TriggerActiveDaysOrDate_Type()
)
triggerActiveDaysOrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerActiveDaysOrDate.setStatus("current")
_TriggerActivateAfter_Type = DisplayString
_TriggerActivateAfter_Object = MibTableColumn
triggerActivateAfter = _TriggerActivateAfter_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 5),
    _TriggerActivateAfter_Type()
)
triggerActivateAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerActivateAfter.setStatus("current")
_TriggerActivateBefore_Type = DisplayString
_TriggerActivateBefore_Object = MibTableColumn
triggerActivateBefore = _TriggerActivateBefore_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 6),
    _TriggerActivateBefore_Type()
)
triggerActivateBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerActivateBefore.setStatus("current")
_TriggerActiveStatus_Type = TruthValue
_TriggerActiveStatus_Object = MibTableColumn
triggerActiveStatus = _TriggerActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 7),
    _TriggerActiveStatus_Type()
)
triggerActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerActiveStatus.setStatus("current")
_TriggerTestMode_Type = TruthValue
_TriggerTestMode_Object = MibTableColumn
triggerTestMode = _TriggerTestMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 8),
    _TriggerTestMode_Type()
)
triggerTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerTestMode.setStatus("current")
_TriggerSnmpTrap_Type = TruthValue
_TriggerSnmpTrap_Object = MibTableColumn
triggerSnmpTrap = _TriggerSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 9),
    _TriggerSnmpTrap_Type()
)
triggerSnmpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerSnmpTrap.setStatus("current")
_TriggerRepeatTimes_Type = DisplayString
_TriggerRepeatTimes_Object = MibTableColumn
triggerRepeatTimes = _TriggerRepeatTimes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 10),
    _TriggerRepeatTimes_Type()
)
triggerRepeatTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerRepeatTimes.setStatus("current")
_TriggerLasttimeModified_Type = DisplayString
_TriggerLasttimeModified_Object = MibTableColumn
triggerLasttimeModified = _TriggerLasttimeModified_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 11),
    _TriggerLasttimeModified_Type()
)
triggerLasttimeModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerLasttimeModified.setStatus("current")
_TriggerNumberOfActivation_Type = Counter32
_TriggerNumberOfActivation_Object = MibTableColumn
triggerNumberOfActivation = _TriggerNumberOfActivation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 12),
    _TriggerNumberOfActivation_Type()
)
triggerNumberOfActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumberOfActivation.setStatus("current")
_TriggerLasttimeActivation_Type = DisplayString
_TriggerLasttimeActivation_Object = MibTableColumn
triggerLasttimeActivation = _TriggerLasttimeActivation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 13),
    _TriggerLasttimeActivation_Type()
)
triggerLasttimeActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerLasttimeActivation.setStatus("current")


class _TriggerNumberOfScripts_Type(Unsigned32):
    """Custom type triggerNumberOfScripts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TriggerNumberOfScripts_Type.__name__ = "Unsigned32"
_TriggerNumberOfScripts_Object = MibTableColumn
triggerNumberOfScripts = _TriggerNumberOfScripts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 14),
    _TriggerNumberOfScripts_Type()
)
triggerNumberOfScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumberOfScripts.setStatus("current")
_TriggerScript1_Type = DisplayString
_TriggerScript1_Object = MibTableColumn
triggerScript1 = _TriggerScript1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 15),
    _TriggerScript1_Type()
)
triggerScript1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerScript1.setStatus("current")
_TriggerScript2_Type = DisplayString
_TriggerScript2_Object = MibTableColumn
triggerScript2 = _TriggerScript2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 16),
    _TriggerScript2_Type()
)
triggerScript2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerScript2.setStatus("current")
_TriggerScript3_Type = DisplayString
_TriggerScript3_Object = MibTableColumn
triggerScript3 = _TriggerScript3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 17),
    _TriggerScript3_Type()
)
triggerScript3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerScript3.setStatus("current")
_TriggerScript4_Type = DisplayString
_TriggerScript4_Object = MibTableColumn
triggerScript4 = _TriggerScript4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 18),
    _TriggerScript4_Type()
)
triggerScript4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerScript4.setStatus("current")
_TriggerScript5_Type = DisplayString
_TriggerScript5_Object = MibTableColumn
triggerScript5 = _TriggerScript5_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 19),
    _TriggerScript5_Type()
)
triggerScript5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerScript5.setStatus("current")
_TriggerCounters_ObjectIdentity = ObjectIdentity
triggerCounters = _TriggerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10)
)
_TriggerNumOfActivation_Type = Counter32
_TriggerNumOfActivation_Object = MibScalar
triggerNumOfActivation = _TriggerNumOfActivation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 1),
    _TriggerNumOfActivation_Type()
)
triggerNumOfActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfActivation.setStatus("current")
_TriggerNumOfActivationToday_Type = Counter32
_TriggerNumOfActivationToday_Object = MibScalar
triggerNumOfActivationToday = _TriggerNumOfActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 2),
    _TriggerNumOfActivationToday_Type()
)
triggerNumOfActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfActivationToday.setStatus("current")
_TriggerNumOfPerodicActivationToday_Type = Counter32
_TriggerNumOfPerodicActivationToday_Object = MibScalar
triggerNumOfPerodicActivationToday = _TriggerNumOfPerodicActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 3),
    _TriggerNumOfPerodicActivationToday_Type()
)
triggerNumOfPerodicActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfPerodicActivationToday.setStatus("current")
_TriggerNumOfInterfaceActivationToday_Type = Counter32
_TriggerNumOfInterfaceActivationToday_Object = MibScalar
triggerNumOfInterfaceActivationToday = _TriggerNumOfInterfaceActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 4),
    _TriggerNumOfInterfaceActivationToday_Type()
)
triggerNumOfInterfaceActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfInterfaceActivationToday.setStatus("current")
_TriggerNumOfResourceActivationToday_Type = Counter32
_TriggerNumOfResourceActivationToday_Object = MibScalar
triggerNumOfResourceActivationToday = _TriggerNumOfResourceActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 5),
    _TriggerNumOfResourceActivationToday_Type()
)
triggerNumOfResourceActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfResourceActivationToday.setStatus("current")
_TriggerNumOfRebootActivationToday_Type = Counter32
_TriggerNumOfRebootActivationToday_Object = MibScalar
triggerNumOfRebootActivationToday = _TriggerNumOfRebootActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 6),
    _TriggerNumOfRebootActivationToday_Type()
)
triggerNumOfRebootActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfRebootActivationToday.setStatus("current")
_TriggerNumOfPingPollActivationToday_Type = Counter32
_TriggerNumOfPingPollActivationToday_Object = MibScalar
triggerNumOfPingPollActivationToday = _TriggerNumOfPingPollActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 7),
    _TriggerNumOfPingPollActivationToday_Type()
)
triggerNumOfPingPollActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfPingPollActivationToday.setStatus("current")
_TriggerNumOfStackMasterFailActivationToday_Type = Counter32
_TriggerNumOfStackMasterFailActivationToday_Object = MibScalar
triggerNumOfStackMasterFailActivationToday = _TriggerNumOfStackMasterFailActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 8),
    _TriggerNumOfStackMasterFailActivationToday_Type()
)
triggerNumOfStackMasterFailActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfStackMasterFailActivationToday.setStatus("current")
_TriggerNumOfStackMemberActivationToday_Type = Counter32
_TriggerNumOfStackMemberActivationToday_Object = MibScalar
triggerNumOfStackMemberActivationToday = _TriggerNumOfStackMemberActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 9),
    _TriggerNumOfStackMemberActivationToday_Type()
)
triggerNumOfStackMemberActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfStackMemberActivationToday.setStatus("current")
_TriggerNumOfStackXemStkActivationToday_Type = Counter32
_TriggerNumOfStackXemStkActivationToday_Object = MibScalar
triggerNumOfStackXemStkActivationToday = _TriggerNumOfStackXemStkActivationToday_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 10),
    _TriggerNumOfStackXemStkActivationToday_Type()
)
triggerNumOfStackXemStkActivationToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerNumOfStackXemStkActivationToday.setStatus("current")

# Managed Objects groups


# Notification objects

triggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0, 1)
)
triggerTrap.setObjects(
    ("AT-TRIGGER-MIB", "triggerLastTriggerActivated")
)
if mibBuilder.loadTexts:
    triggerTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-TRIGGER-MIB",
    **{"trigger": trigger,
       "triggerTraps": triggerTraps,
       "triggerTrap": triggerTrap,
       "triggerLastTriggerActivated": triggerLastTriggerActivated,
       "triggerConfigInfoTable": triggerConfigInfoTable,
       "triggerConfigInfoEntry": triggerConfigInfoEntry,
       "triggerNumber": triggerNumber,
       "triggerName": triggerName,
       "triggerTypeDetail": triggerTypeDetail,
       "triggerActiveDaysOrDate": triggerActiveDaysOrDate,
       "triggerActivateAfter": triggerActivateAfter,
       "triggerActivateBefore": triggerActivateBefore,
       "triggerActiveStatus": triggerActiveStatus,
       "triggerTestMode": triggerTestMode,
       "triggerSnmpTrap": triggerSnmpTrap,
       "triggerRepeatTimes": triggerRepeatTimes,
       "triggerLasttimeModified": triggerLasttimeModified,
       "triggerNumberOfActivation": triggerNumberOfActivation,
       "triggerLasttimeActivation": triggerLasttimeActivation,
       "triggerNumberOfScripts": triggerNumberOfScripts,
       "triggerScript1": triggerScript1,
       "triggerScript2": triggerScript2,
       "triggerScript3": triggerScript3,
       "triggerScript4": triggerScript4,
       "triggerScript5": triggerScript5,
       "triggerCounters": triggerCounters,
       "triggerNumOfActivation": triggerNumOfActivation,
       "triggerNumOfActivationToday": triggerNumOfActivationToday,
       "triggerNumOfPerodicActivationToday": triggerNumOfPerodicActivationToday,
       "triggerNumOfInterfaceActivationToday": triggerNumOfInterfaceActivationToday,
       "triggerNumOfResourceActivationToday": triggerNumOfResourceActivationToday,
       "triggerNumOfRebootActivationToday": triggerNumOfRebootActivationToday,
       "triggerNumOfPingPollActivationToday": triggerNumOfPingPollActivationToday,
       "triggerNumOfStackMasterFailActivationToday": triggerNumOfStackMasterFailActivationToday,
       "triggerNumOfStackMemberActivationToday": triggerNumOfStackMemberActivationToday,
       "triggerNumOfStackXemStkActivationToday": triggerNumOfStackXemStkActivationToday}
)
