# SNMP MIB module (ZHONE-GEN-ALARM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-ALARM
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:30 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneModules,
 zhoneSystem) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneSystem")

(ZhoneAlarmSeverity,
 ZhoneAlarmTypeId) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAlarmSeverity",
    "ZhoneAlarmTypeId")


# MODULE-IDENTITY

genAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 79)
)
genAlarm.setRevisions(
        ("2004-02-18 14:30",
         "2004-01-12 13:37")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneAlarmActiveVariableValue(Integer32, TextualConvention):
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("opaque", 9),
          ("timeTicks", 3),
          ("unsigned32", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneAlarm_ObjectIdentity = ObjectIdentity
zhoneAlarm = _ZhoneAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18)
)
if mibBuilder.loadTexts:
    zhoneAlarm.setStatus("current")
_ZhoneAlarmStats_ObjectIdentity = ObjectIdentity
zhoneAlarmStats = _ZhoneAlarmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1)
)
_ZhoneAlarmActiveOverflowCnt_Type = Counter32
_ZhoneAlarmActiveOverflowCnt_Object = MibScalar
zhoneAlarmActiveOverflowCnt = _ZhoneAlarmActiveOverflowCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 1),
    _ZhoneAlarmActiveOverflowCnt_Type()
)
zhoneAlarmActiveOverflowCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveOverflowCnt.setStatus("current")
_ZhoneAlarmActiveStatsCurrentCnt_Type = Counter32
_ZhoneAlarmActiveStatsCurrentCnt_Object = MibScalar
zhoneAlarmActiveStatsCurrentCnt = _ZhoneAlarmActiveStatsCurrentCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 2),
    _ZhoneAlarmActiveStatsCurrentCnt_Type()
)
zhoneAlarmActiveStatsCurrentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveStatsCurrentCnt.setStatus("current")
_ZhoneAlarmActiveStatsTotalCnt_Type = Counter32
_ZhoneAlarmActiveStatsTotalCnt_Object = MibScalar
zhoneAlarmActiveStatsTotalCnt = _ZhoneAlarmActiveStatsTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 3),
    _ZhoneAlarmActiveStatsTotalCnt_Type()
)
zhoneAlarmActiveStatsTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveStatsTotalCnt.setStatus("current")
_ZhoneAlarmClearStatsTotalCnt_Type = Counter32
_ZhoneAlarmClearStatsTotalCnt_Object = MibScalar
zhoneAlarmClearStatsTotalCnt = _ZhoneAlarmClearStatsTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 4),
    _ZhoneAlarmClearStatsTotalCnt_Type()
)
zhoneAlarmClearStatsTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmClearStatsTotalCnt.setStatus("current")
_ZhoneAlarmLastRaised_Type = TimeTicks
_ZhoneAlarmLastRaised_Object = MibScalar
zhoneAlarmLastRaised = _ZhoneAlarmLastRaised_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 5),
    _ZhoneAlarmLastRaised_Type()
)
zhoneAlarmLastRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmLastRaised.setStatus("current")
_ZhoneAlarmLastCleared_Type = TimeTicks
_ZhoneAlarmLastCleared_Object = MibScalar
zhoneAlarmLastCleared = _ZhoneAlarmLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 6),
    _ZhoneAlarmLastCleared_Type()
)
zhoneAlarmLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmLastCleared.setStatus("current")
_ZhoneAlarmModelTable_Object = MibTable
zhoneAlarmModelTable = _ZhoneAlarmModelTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2)
)
if mibBuilder.loadTexts:
    zhoneAlarmModelTable.setStatus("current")
_ZhoneAlarmModelEntry_Object = MibTableRow
zhoneAlarmModelEntry = _ZhoneAlarmModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1)
)
zhoneAlarmModelEntry.setIndexNames(
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmModelAlarmId"),
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmModelNotificationId"),
)
if mibBuilder.loadTexts:
    zhoneAlarmModelEntry.setStatus("current")
_ZhoneAlarmModelAlarmId_Type = ZhoneAlarmTypeId
_ZhoneAlarmModelAlarmId_Object = MibTableColumn
zhoneAlarmModelAlarmId = _ZhoneAlarmModelAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 1),
    _ZhoneAlarmModelAlarmId_Type()
)
zhoneAlarmModelAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAlarmModelAlarmId.setStatus("current")
_ZhoneAlarmModelNotificationId_Type = ObjectIdentifier
_ZhoneAlarmModelNotificationId_Object = MibTableColumn
zhoneAlarmModelNotificationId = _ZhoneAlarmModelNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 2),
    _ZhoneAlarmModelNotificationId_Type()
)
zhoneAlarmModelNotificationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAlarmModelNotificationId.setStatus("current")
_ZhoneAlarmModelVariableId_Type = Integer32
_ZhoneAlarmModelVariableId_Object = MibTableColumn
zhoneAlarmModelVariableId = _ZhoneAlarmModelVariableId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 3),
    _ZhoneAlarmModelVariableId_Type()
)
zhoneAlarmModelVariableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmModelVariableId.setStatus("current")
_ZhoneAlarmModelDescription_Type = OctetString
_ZhoneAlarmModelDescription_Object = MibTableColumn
zhoneAlarmModelDescription = _ZhoneAlarmModelDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 4),
    _ZhoneAlarmModelDescription_Type()
)
zhoneAlarmModelDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmModelDescription.setStatus("current")
_ZhoneAlarmActiveTable_Object = MibTable
zhoneAlarmActiveTable = _ZhoneAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3)
)
if mibBuilder.loadTexts:
    zhoneAlarmActiveTable.setStatus("current")
_ZhoneAlarmActiveEntry_Object = MibTableRow
zhoneAlarmActiveEntry = _ZhoneAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1)
)
zhoneAlarmActiveEntry.setIndexNames(
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveId"),
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveResourceId"),
)
if mibBuilder.loadTexts:
    zhoneAlarmActiveEntry.setStatus("current")
_ZhoneAlarmActiveId_Type = ZhoneAlarmTypeId
_ZhoneAlarmActiveId_Object = MibTableColumn
zhoneAlarmActiveId = _ZhoneAlarmActiveId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 1),
    _ZhoneAlarmActiveId_Type()
)
zhoneAlarmActiveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAlarmActiveId.setStatus("current")
_ZhoneAlarmActiveResourceId_Type = ObjectIdentifier
_ZhoneAlarmActiveResourceId_Object = MibTableColumn
zhoneAlarmActiveResourceId = _ZhoneAlarmActiveResourceId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 2),
    _ZhoneAlarmActiveResourceId_Type()
)
zhoneAlarmActiveResourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAlarmActiveResourceId.setStatus("current")


class _ZhoneAlarmActiveVariables_Type(Unsigned32):
    """Custom type zhoneAlarmActiveVariables based on Unsigned32"""
    defaultValue = 0


_ZhoneAlarmActiveVariables_Object = MibTableColumn
zhoneAlarmActiveVariables = _ZhoneAlarmActiveVariables_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 3),
    _ZhoneAlarmActiveVariables_Type()
)
zhoneAlarmActiveVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariables.setStatus("current")
_ZhoneAlarmActiveNotificationId_Type = ObjectIdentifier
_ZhoneAlarmActiveNotificationId_Object = MibTableColumn
zhoneAlarmActiveNotificationId = _ZhoneAlarmActiveNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 4),
    _ZhoneAlarmActiveNotificationId_Type()
)
zhoneAlarmActiveNotificationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveNotificationId.setStatus("current")
_ZhoneAlarmActiveSeverity_Type = ZhoneAlarmSeverity
_ZhoneAlarmActiveSeverity_Object = MibTableColumn
zhoneAlarmActiveSeverity = _ZhoneAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 5),
    _ZhoneAlarmActiveSeverity_Type()
)
zhoneAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveSeverity.setStatus("current")
_ZhoneAlarmActiveVariableTable_Object = MibTable
zhoneAlarmActiveVariableTable = _ZhoneAlarmActiveVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4)
)
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableTable.setStatus("current")
_ZhoneAlarmActiveVariableEntry_Object = MibTableRow
zhoneAlarmActiveVariableEntry = _ZhoneAlarmActiveVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1)
)
zhoneAlarmActiveVariableEntry.setIndexNames(
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveId"),
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveResourceId"),
    (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableId"),
)
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableEntry.setStatus("current")


class _ZhoneAlarmActiveVariableId_Type(Integer32):
    """Custom type zhoneAlarmActiveVariableId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneAlarmActiveVariableId_Type.__name__ = "Integer32"
_ZhoneAlarmActiveVariableId_Object = MibTableColumn
zhoneAlarmActiveVariableId = _ZhoneAlarmActiveVariableId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 1),
    _ZhoneAlarmActiveVariableId_Type()
)
zhoneAlarmActiveVariableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableId.setStatus("current")
_ZhoneAlarmActiveVariableValueType_Type = ZhoneAlarmActiveVariableValue
_ZhoneAlarmActiveVariableValueType_Object = MibTableColumn
zhoneAlarmActiveVariableValueType = _ZhoneAlarmActiveVariableValueType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 2),
    _ZhoneAlarmActiveVariableValueType_Type()
)
zhoneAlarmActiveVariableValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableValueType.setStatus("current")
_ZhoneAlarmActiveVariableCounter32Val_Type = Counter32
_ZhoneAlarmActiveVariableCounter32Val_Object = MibTableColumn
zhoneAlarmActiveVariableCounter32Val = _ZhoneAlarmActiveVariableCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 3),
    _ZhoneAlarmActiveVariableCounter32Val_Type()
)
zhoneAlarmActiveVariableCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableCounter32Val.setStatus("current")
_ZhoneAlarmActiveVariableUnsigned32Val_Type = Unsigned32
_ZhoneAlarmActiveVariableUnsigned32Val_Object = MibTableColumn
zhoneAlarmActiveVariableUnsigned32Val = _ZhoneAlarmActiveVariableUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 4),
    _ZhoneAlarmActiveVariableUnsigned32Val_Type()
)
zhoneAlarmActiveVariableUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableUnsigned32Val.setStatus("current")
_ZhoneAlarmActiveVariableTimeTicksVal_Type = TimeTicks
_ZhoneAlarmActiveVariableTimeTicksVal_Object = MibTableColumn
zhoneAlarmActiveVariableTimeTicksVal = _ZhoneAlarmActiveVariableTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 5),
    _ZhoneAlarmActiveVariableTimeTicksVal_Type()
)
zhoneAlarmActiveVariableTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableTimeTicksVal.setStatus("current")
_ZhoneAlarmActiveVariableInteger32Val_Type = Integer32
_ZhoneAlarmActiveVariableInteger32Val_Object = MibTableColumn
zhoneAlarmActiveVariableInteger32Val = _ZhoneAlarmActiveVariableInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 6),
    _ZhoneAlarmActiveVariableInteger32Val_Type()
)
zhoneAlarmActiveVariableInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableInteger32Val.setStatus("current")


class _ZhoneAlarmActiveVariableOctetStringVal_Type(OctetString):
    """Custom type zhoneAlarmActiveVariableOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ZhoneAlarmActiveVariableOctetStringVal_Type.__name__ = "OctetString"
_ZhoneAlarmActiveVariableOctetStringVal_Object = MibTableColumn
zhoneAlarmActiveVariableOctetStringVal = _ZhoneAlarmActiveVariableOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 7),
    _ZhoneAlarmActiveVariableOctetStringVal_Type()
)
zhoneAlarmActiveVariableOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableOctetStringVal.setStatus("current")
_ZhoneAlarmActiveVariableIpAddressVal_Type = IpAddress
_ZhoneAlarmActiveVariableIpAddressVal_Object = MibTableColumn
zhoneAlarmActiveVariableIpAddressVal = _ZhoneAlarmActiveVariableIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 8),
    _ZhoneAlarmActiveVariableIpAddressVal_Type()
)
zhoneAlarmActiveVariableIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableIpAddressVal.setStatus("current")
_ZhoneAlarmActiveVariableOidVal_Type = ObjectIdentifier
_ZhoneAlarmActiveVariableOidVal_Object = MibTableColumn
zhoneAlarmActiveVariableOidVal = _ZhoneAlarmActiveVariableOidVal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 9),
    _ZhoneAlarmActiveVariableOidVal_Type()
)
zhoneAlarmActiveVariableOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableOidVal.setStatus("current")
_ZhoneAlarmActiveVariableCounter64Val_Type = Counter64
_ZhoneAlarmActiveVariableCounter64Val_Object = MibTableColumn
zhoneAlarmActiveVariableCounter64Val = _ZhoneAlarmActiveVariableCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 10),
    _ZhoneAlarmActiveVariableCounter64Val_Type()
)
zhoneAlarmActiveVariableCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableCounter64Val.setStatus("current")
_ZhoneAlarmActiveVariableOpaqueVal_Type = Opaque
_ZhoneAlarmActiveVariableOpaqueVal_Object = MibTableColumn
zhoneAlarmActiveVariableOpaqueVal = _ZhoneAlarmActiveVariableOpaqueVal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 11),
    _ZhoneAlarmActiveVariableOpaqueVal_Type()
)
zhoneAlarmActiveVariableOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableOpaqueVal.setStatus("current")
_ZhoneAlarmActiveVariableResourceId_Type = ObjectIdentifier
_ZhoneAlarmActiveVariableResourceId_Object = MibTableColumn
zhoneAlarmActiveVariableResourceId = _ZhoneAlarmActiveVariableResourceId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 12),
    _ZhoneAlarmActiveVariableResourceId_Type()
)
zhoneAlarmActiveVariableResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneAlarmActiveVariableResourceId.setStatus("current")

# Managed Objects groups

zhoneAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 5)
)
zhoneAlarmGroup.setObjects(
      *(("ZHONE-GEN-ALARM", "zhoneAlarmActiveOverflowCnt"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveStatsCurrentCnt"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveStatsTotalCnt"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmClearStatsTotalCnt"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmLastRaised"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmLastCleared"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariables"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveNotificationId"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableValueType"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableCounter32Val"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableUnsigned32Val"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableTimeTicksVal"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableInteger32Val"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOctetStringVal"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableIpAddressVal"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOidVal"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableCounter64Val"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmModelVariableId"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableResourceId"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOpaqueVal"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmModelDescription"),
        ("ZHONE-GEN-ALARM", "zhoneAlarmActiveSeverity"))
)
if mibBuilder.loadTexts:
    zhoneAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-ALARM",
    **{"ZhoneAlarmActiveVariableValue": ZhoneAlarmActiveVariableValue,
       "zhoneAlarm": zhoneAlarm,
       "zhoneAlarmStats": zhoneAlarmStats,
       "zhoneAlarmActiveOverflowCnt": zhoneAlarmActiveOverflowCnt,
       "zhoneAlarmActiveStatsCurrentCnt": zhoneAlarmActiveStatsCurrentCnt,
       "zhoneAlarmActiveStatsTotalCnt": zhoneAlarmActiveStatsTotalCnt,
       "zhoneAlarmClearStatsTotalCnt": zhoneAlarmClearStatsTotalCnt,
       "zhoneAlarmLastRaised": zhoneAlarmLastRaised,
       "zhoneAlarmLastCleared": zhoneAlarmLastCleared,
       "zhoneAlarmModelTable": zhoneAlarmModelTable,
       "zhoneAlarmModelEntry": zhoneAlarmModelEntry,
       "zhoneAlarmModelAlarmId": zhoneAlarmModelAlarmId,
       "zhoneAlarmModelNotificationId": zhoneAlarmModelNotificationId,
       "zhoneAlarmModelVariableId": zhoneAlarmModelVariableId,
       "zhoneAlarmModelDescription": zhoneAlarmModelDescription,
       "zhoneAlarmActiveTable": zhoneAlarmActiveTable,
       "zhoneAlarmActiveEntry": zhoneAlarmActiveEntry,
       "zhoneAlarmActiveId": zhoneAlarmActiveId,
       "zhoneAlarmActiveResourceId": zhoneAlarmActiveResourceId,
       "zhoneAlarmActiveVariables": zhoneAlarmActiveVariables,
       "zhoneAlarmActiveNotificationId": zhoneAlarmActiveNotificationId,
       "zhoneAlarmActiveSeverity": zhoneAlarmActiveSeverity,
       "zhoneAlarmActiveVariableTable": zhoneAlarmActiveVariableTable,
       "zhoneAlarmActiveVariableEntry": zhoneAlarmActiveVariableEntry,
       "zhoneAlarmActiveVariableId": zhoneAlarmActiveVariableId,
       "zhoneAlarmActiveVariableValueType": zhoneAlarmActiveVariableValueType,
       "zhoneAlarmActiveVariableCounter32Val": zhoneAlarmActiveVariableCounter32Val,
       "zhoneAlarmActiveVariableUnsigned32Val": zhoneAlarmActiveVariableUnsigned32Val,
       "zhoneAlarmActiveVariableTimeTicksVal": zhoneAlarmActiveVariableTimeTicksVal,
       "zhoneAlarmActiveVariableInteger32Val": zhoneAlarmActiveVariableInteger32Val,
       "zhoneAlarmActiveVariableOctetStringVal": zhoneAlarmActiveVariableOctetStringVal,
       "zhoneAlarmActiveVariableIpAddressVal": zhoneAlarmActiveVariableIpAddressVal,
       "zhoneAlarmActiveVariableOidVal": zhoneAlarmActiveVariableOidVal,
       "zhoneAlarmActiveVariableCounter64Val": zhoneAlarmActiveVariableCounter64Val,
       "zhoneAlarmActiveVariableOpaqueVal": zhoneAlarmActiveVariableOpaqueVal,
       "zhoneAlarmActiveVariableResourceId": zhoneAlarmActiveVariableResourceId,
       "zhoneAlarmGroup": zhoneAlarmGroup,
       "genAlarm": genAlarm}
)
