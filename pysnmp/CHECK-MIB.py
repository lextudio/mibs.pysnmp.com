# SNMP MIB module (CHECK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHECK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:37 2024
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
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

checkMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 7777)
)
checkMIB.setRevisions(
        ("2003-12-19 13:13",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RuleValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"


class SeverityConfigured(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )



class SeverityReturned(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CheckObjects_ObjectIdentity = ObjectIdentity
checkObjects = _CheckObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 1)
)
_CheckCapabilities_ObjectIdentity = ObjectIdentity
checkCapabilities = _CheckCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 1, 1)
)
_CheckCapabMinCheckInterval_Type = TimeTicks
_CheckCapabMinCheckInterval_Object = MibScalar
checkCapabMinCheckInterval = _CheckCapabMinCheckInterval_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 1, 1),
    _CheckCapabMinCheckInterval_Type()
)
checkCapabMinCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkCapabMinCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    checkCapabMinCheckInterval.setUnits("centi-seconds")
_CheckCapabMaxResults_Type = Unsigned32
_CheckCapabMaxResults_Object = MibScalar
checkCapabMaxResults = _CheckCapabMaxResults_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 1, 2),
    _CheckCapabMaxResults_Type()
)
checkCapabMaxResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkCapabMaxResults.setStatus("current")
_CheckCapabMaxRules_Type = Unsigned32
_CheckCapabMaxRules_Object = MibScalar
checkCapabMaxRules = _CheckCapabMaxRules_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 1, 3),
    _CheckCapabMaxRules_Type()
)
checkCapabMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkCapabMaxRules.setStatus("current")
_CheckControl_ObjectIdentity = ObjectIdentity
checkControl = _CheckControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 1, 2)
)


class _CheckCtrlAdminStatus_Type(Integer32):
    """Custom type checkCtrlAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("silent", 2),
          ("up", 1))
    )


_CheckCtrlAdminStatus_Type.__name__ = "Integer32"
_CheckCtrlAdminStatus_Object = MibScalar
checkCtrlAdminStatus = _CheckCtrlAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 2, 1),
    _CheckCtrlAdminStatus_Type()
)
checkCtrlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checkCtrlAdminStatus.setStatus("current")


class _CheckCtrlOperStatus_Type(Integer32):
    """Custom type checkCtrlOperStatus based on Integer32"""
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
        *(("down", 3),
          ("flushing", 4),
          ("silent", 2),
          ("up", 1))
    )


_CheckCtrlOperStatus_Type.__name__ = "Integer32"
_CheckCtrlOperStatus_Object = MibScalar
checkCtrlOperStatus = _CheckCtrlOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 2, 2),
    _CheckCtrlOperStatus_Type()
)
checkCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkCtrlOperStatus.setStatus("current")
_CheckResultTable_Object = MibTable
checkResultTable = _CheckResultTable_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3)
)
if mibBuilder.loadTexts:
    checkResultTable.setStatus("current")
_CheckResultEntry_Object = MibTableRow
checkResultEntry = _CheckResultEntry_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1)
)
checkResultEntry.setIndexNames(
    (0, "CHECK-MIB", "checkResultName"),
)
if mibBuilder.loadTexts:
    checkResultEntry.setStatus("current")


class _CheckResultName_Type(SnmpAdminString):
    """Custom type checkResultName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CheckResultName_Type.__name__ = "SnmpAdminString"
_CheckResultName_Object = MibTableColumn
checkResultName = _CheckResultName_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 1),
    _CheckResultName_Type()
)
checkResultName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    checkResultName.setStatus("current")
_CheckResultSeverity_Type = SeverityReturned
_CheckResultSeverity_Object = MibTableColumn
checkResultSeverity = _CheckResultSeverity_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 2),
    _CheckResultSeverity_Type()
)
checkResultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkResultSeverity.setStatus("current")
_CheckResultSize_Type = Unsigned32
_CheckResultSize_Object = MibTableColumn
checkResultSize = _CheckResultSize_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 3),
    _CheckResultSize_Type()
)
checkResultSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkResultSize.setStatus("current")
_CheckResultTime_Type = TimeStamp
_CheckResultTime_Object = MibTableColumn
checkResultTime = _CheckResultTime_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 4),
    _CheckResultTime_Type()
)
checkResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkResultTime.setStatus("current")


class _CheckResultInterval_Type(TimeInterval):
    """Custom type checkResultInterval based on TimeInterval"""
    defaultValue = 0


_CheckResultInterval_Object = MibTableColumn
checkResultInterval = _CheckResultInterval_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 5),
    _CheckResultInterval_Type()
)
checkResultInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkResultInterval.setStatus("current")
if mibBuilder.loadTexts:
    checkResultInterval.setUnits("centi-seconds")


class _CheckResultSeverityThreshold_Type(SeverityConfigured):
    """Custom type checkResultSeverityThreshold based on SeverityConfigured"""
    defaultValue = 0


_CheckResultSeverityThreshold_Object = MibTableColumn
checkResultSeverityThreshold = _CheckResultSeverityThreshold_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 6),
    _CheckResultSeverityThreshold_Type()
)
checkResultSeverityThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkResultSeverityThreshold.setStatus("current")


class _CheckResultStorageType_Type(StorageType):
    """Custom type checkResultStorageType based on StorageType"""


_CheckResultStorageType_Object = MibTableColumn
checkResultStorageType = _CheckResultStorageType_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 7),
    _CheckResultStorageType_Type()
)
checkResultStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkResultStorageType.setStatus("current")
_CheckResultRowStatus_Type = RowStatus
_CheckResultRowStatus_Object = MibTableColumn
checkResultRowStatus = _CheckResultRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 3, 1, 8),
    _CheckResultRowStatus_Type()
)
checkResultRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkResultRowStatus.setStatus("current")
_CheckRuleTable_Object = MibTable
checkRuleTable = _CheckRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4)
)
if mibBuilder.loadTexts:
    checkRuleTable.setStatus("current")
_CheckRuleEntry_Object = MibTableRow
checkRuleEntry = _CheckRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1)
)
checkRuleEntry.setIndexNames(
    (0, "CHECK-MIB", "checkResultName"),
    (0, "CHECK-MIB", "checkRuleName"),
)
if mibBuilder.loadTexts:
    checkRuleEntry.setStatus("current")


class _CheckRuleName_Type(SnmpAdminString):
    """Custom type checkRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CheckRuleName_Type.__name__ = "SnmpAdminString"
_CheckRuleName_Object = MibTableColumn
checkRuleName = _CheckRuleName_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 2),
    _CheckRuleName_Type()
)
checkRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    checkRuleName.setStatus("current")


class _CheckRuleOid_Type(ObjectIdentifier):
    """Custom type checkRuleOid based on ObjectIdentifier"""
    defaultValue = (0, 0)


_CheckRuleOid_Object = MibTableColumn
checkRuleOid = _CheckRuleOid_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 3),
    _CheckRuleOid_Type()
)
checkRuleOid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkRuleOid.setStatus("current")
_CheckRuleValue_Type = RuleValue
_CheckRuleValue_Object = MibTableColumn
checkRuleValue = _CheckRuleValue_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 4),
    _CheckRuleValue_Type()
)
checkRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkRuleValue.setStatus("current")


class _CheckRuleOperation_Type(Integer32):
    """Custom type checkRuleOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delta", 7),
          ("equal", 2),
          ("greater", 5),
          ("greaterOrEqual", 6),
          ("less", 3),
          ("lessOrEqual", 4),
          ("noOperation", 0),
          ("unequal", 1))
    )


_CheckRuleOperation_Type.__name__ = "Integer32"
_CheckRuleOperation_Object = MibTableColumn
checkRuleOperation = _CheckRuleOperation_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 5),
    _CheckRuleOperation_Type()
)
checkRuleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checkRuleOperation.setStatus("current")


class _CheckRuleSeverity_Type(SeverityConfigured):
    """Custom type checkRuleSeverity based on SeverityConfigured"""
    defaultValue = 1


_CheckRuleSeverity_Object = MibTableColumn
checkRuleSeverity = _CheckRuleSeverity_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 6),
    _CheckRuleSeverity_Type()
)
checkRuleSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkRuleSeverity.setStatus("current")
_CheckRuleRowStatus_Type = RowStatus
_CheckRuleRowStatus_Object = MibTableColumn
checkRuleRowStatus = _CheckRuleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 4, 1, 7),
    _CheckRuleRowStatus_Type()
)
checkRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    checkRuleRowStatus.setStatus("current")
_CheckFailureTable_Object = MibTable
checkFailureTable = _CheckFailureTable_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 5)
)
if mibBuilder.loadTexts:
    checkFailureTable.setStatus("current")
_CheckFailureEntry_Object = MibTableRow
checkFailureEntry = _CheckFailureEntry_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 5, 1)
)
checkFailureEntry.setIndexNames(
    (0, "CHECK-MIB", "checkResultName"),
    (0, "CHECK-MIB", "checkFailureSeverity"),
    (0, "CHECK-MIB", "checkRuleName"),
)
if mibBuilder.loadTexts:
    checkFailureEntry.setStatus("current")
_CheckFailureSeverity_Type = SeverityReturned
_CheckFailureSeverity_Object = MibTableColumn
checkFailureSeverity = _CheckFailureSeverity_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 5, 1, 1),
    _CheckFailureSeverity_Type()
)
checkFailureSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    checkFailureSeverity.setStatus("current")
_CheckFailureOid_Type = ObjectIdentifier
_CheckFailureOid_Object = MibTableColumn
checkFailureOid = _CheckFailureOid_Object(
    (1, 3, 6, 1, 2, 1, 7777, 1, 5, 1, 2),
    _CheckFailureOid_Type()
)
checkFailureOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkFailureOid.setStatus("current")
_CheckNotifications_ObjectIdentity = ObjectIdentity
checkNotifications = _CheckNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 2)
)
_CheckEvent_ObjectIdentity = ObjectIdentity
checkEvent = _CheckEvent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 2, 0)
)
_CheckConformance_ObjectIdentity = ObjectIdentity
checkConformance = _CheckConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 3)
)
_CheckCompliances_ObjectIdentity = ObjectIdentity
checkCompliances = _CheckCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 3, 1)
)
_CheckGroups_ObjectIdentity = ObjectIdentity
checkGroups = _CheckGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2)
)

# Managed Objects groups

checkCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 1)
)
checkCapabilitiesGroup.setObjects(
      *(("CHECK-MIB", "checkCapabMinCheckInterval"),
        ("CHECK-MIB", "checkCapabMaxResults"),
        ("CHECK-MIB", "checkCapabMaxRules"))
)
if mibBuilder.loadTexts:
    checkCapabilitiesGroup.setStatus("current")

checkControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 2)
)
checkControlGroup.setObjects(
      *(("CHECK-MIB", "checkCtrlAdminStatus"),
        ("CHECK-MIB", "checkCtrlOperStatus"))
)
if mibBuilder.loadTexts:
    checkControlGroup.setStatus("current")

checkResultGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 3)
)
checkResultGroup.setObjects(
      *(("CHECK-MIB", "checkResultSeverity"),
        ("CHECK-MIB", "checkResultSize"),
        ("CHECK-MIB", "checkResultTime"),
        ("CHECK-MIB", "checkResultInterval"),
        ("CHECK-MIB", "checkResultSeverityThreshold"),
        ("CHECK-MIB", "checkResultStorageType"),
        ("CHECK-MIB", "checkResultRowStatus"))
)
if mibBuilder.loadTexts:
    checkResultGroup.setStatus("current")

checkRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 4)
)
checkRuleGroup.setObjects(
      *(("CHECK-MIB", "checkRuleOid"),
        ("CHECK-MIB", "checkRuleValue"),
        ("CHECK-MIB", "checkRuleOperation"),
        ("CHECK-MIB", "checkRuleSeverity"),
        ("CHECK-MIB", "checkRuleRowStatus"))
)
if mibBuilder.loadTexts:
    checkRuleGroup.setStatus("current")

checkFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 5)
)
checkFailureGroup.setObjects(
    ("CHECK-MIB", "checkFailureOid")
)
if mibBuilder.loadTexts:
    checkFailureGroup.setStatus("current")

checkNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 7777, 3, 2, 6)
)
checkNotificationsGroup.setObjects(
    ("CHECK-MIB", "checkFailed")
)
if mibBuilder.loadTexts:
    checkNotificationsGroup.setStatus("current")


# Notification objects

checkFailed = NotificationType(
    (1, 3, 6, 1, 2, 1, 7777, 2, 0, 1)
)
checkFailed.setObjects(
    ("CHECK-MIB", "checkResultSeverity")
)
if mibBuilder.loadTexts:
    checkFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

checkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 7777, 3, 1, 1)
)
if mibBuilder.loadTexts:
    checkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECK-MIB",
    **{"RuleValue": RuleValue,
       "SeverityConfigured": SeverityConfigured,
       "SeverityReturned": SeverityReturned,
       "checkMIB": checkMIB,
       "checkObjects": checkObjects,
       "checkCapabilities": checkCapabilities,
       "checkCapabMinCheckInterval": checkCapabMinCheckInterval,
       "checkCapabMaxResults": checkCapabMaxResults,
       "checkCapabMaxRules": checkCapabMaxRules,
       "checkControl": checkControl,
       "checkCtrlAdminStatus": checkCtrlAdminStatus,
       "checkCtrlOperStatus": checkCtrlOperStatus,
       "checkResultTable": checkResultTable,
       "checkResultEntry": checkResultEntry,
       "checkResultName": checkResultName,
       "checkResultSeverity": checkResultSeverity,
       "checkResultSize": checkResultSize,
       "checkResultTime": checkResultTime,
       "checkResultInterval": checkResultInterval,
       "checkResultSeverityThreshold": checkResultSeverityThreshold,
       "checkResultStorageType": checkResultStorageType,
       "checkResultRowStatus": checkResultRowStatus,
       "checkRuleTable": checkRuleTable,
       "checkRuleEntry": checkRuleEntry,
       "checkRuleName": checkRuleName,
       "checkRuleOid": checkRuleOid,
       "checkRuleValue": checkRuleValue,
       "checkRuleOperation": checkRuleOperation,
       "checkRuleSeverity": checkRuleSeverity,
       "checkRuleRowStatus": checkRuleRowStatus,
       "checkFailureTable": checkFailureTable,
       "checkFailureEntry": checkFailureEntry,
       "checkFailureSeverity": checkFailureSeverity,
       "checkFailureOid": checkFailureOid,
       "checkNotifications": checkNotifications,
       "checkEvent": checkEvent,
       "checkFailed": checkFailed,
       "checkConformance": checkConformance,
       "checkCompliances": checkCompliances,
       "checkCompliance": checkCompliance,
       "checkGroups": checkGroups,
       "checkCapabilitiesGroup": checkCapabilitiesGroup,
       "checkControlGroup": checkControlGroup,
       "checkResultGroup": checkResultGroup,
       "checkRuleGroup": checkRuleGroup,
       "checkFailureGroup": checkFailureGroup,
       "checkNotificationsGroup": checkNotificationsGroup}
)
