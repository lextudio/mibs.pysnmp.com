# SNMP MIB module (ORACLE-ENTERPRISE-MANAGER-4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORACLE-ENTERPRISE-MANAGER-4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:36 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraEM4_ObjectIdentity = ObjectIdentity
oraEM4 = _OraEM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 15)
)
_OraEM4Objects_ObjectIdentity = ObjectIdentity
oraEM4Objects = _OraEM4Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 15, 1)
)
_OraEM4AlertTable_Object = MibTable
oraEM4AlertTable = _OraEM4AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1)
)
if mibBuilder.loadTexts:
    oraEM4AlertTable.setStatus("mandatory")
_OraEM4AlertEntry_Object = MibTableRow
oraEM4AlertEntry = _OraEM4AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1)
)
oraEM4AlertEntry.setIndexNames(
    (0, "ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertIndex"),
)
if mibBuilder.loadTexts:
    oraEM4AlertEntry.setStatus("mandatory")
_OraEM4AlertIndex_Type = Integer32
_OraEM4AlertIndex_Object = MibTableColumn
oraEM4AlertIndex = _OraEM4AlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 1),
    _OraEM4AlertIndex_Type()
)
oraEM4AlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertIndex.setStatus("mandatory")
_OraEM4AlertTargetName_Type = DisplayString
_OraEM4AlertTargetName_Object = MibTableColumn
oraEM4AlertTargetName = _OraEM4AlertTargetName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 2),
    _OraEM4AlertTargetName_Type()
)
oraEM4AlertTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertTargetName.setStatus("mandatory")
_OraEM4AlertTargetType_Type = DisplayString
_OraEM4AlertTargetType_Object = MibTableColumn
oraEM4AlertTargetType = _OraEM4AlertTargetType_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 3),
    _OraEM4AlertTargetType_Type()
)
oraEM4AlertTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertTargetType.setStatus("mandatory")
_OraEM4AlertHostName_Type = DisplayString
_OraEM4AlertHostName_Object = MibTableColumn
oraEM4AlertHostName = _OraEM4AlertHostName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 4),
    _OraEM4AlertHostName_Type()
)
oraEM4AlertHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertHostName.setStatus("mandatory")
_OraEM4AlertMetricName_Type = DisplayString
_OraEM4AlertMetricName_Object = MibTableColumn
oraEM4AlertMetricName = _OraEM4AlertMetricName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 5),
    _OraEM4AlertMetricName_Type()
)
oraEM4AlertMetricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertMetricName.setStatus("mandatory")
_OraEM4AlertKeyName_Type = DisplayString
_OraEM4AlertKeyName_Object = MibTableColumn
oraEM4AlertKeyName = _OraEM4AlertKeyName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 6),
    _OraEM4AlertKeyName_Type()
)
oraEM4AlertKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertKeyName.setStatus("mandatory")
_OraEM4AlertKeyValue_Type = DisplayString
_OraEM4AlertKeyValue_Object = MibTableColumn
oraEM4AlertKeyValue = _OraEM4AlertKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 7),
    _OraEM4AlertKeyValue_Type()
)
oraEM4AlertKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertKeyValue.setStatus("mandatory")
_OraEM4AlertTimeStamp_Type = DisplayString
_OraEM4AlertTimeStamp_Object = MibTableColumn
oraEM4AlertTimeStamp = _OraEM4AlertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 8),
    _OraEM4AlertTimeStamp_Type()
)
oraEM4AlertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertTimeStamp.setStatus("mandatory")
_OraEM4AlertSeverity_Type = DisplayString
_OraEM4AlertSeverity_Object = MibTableColumn
oraEM4AlertSeverity = _OraEM4AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 9),
    _OraEM4AlertSeverity_Type()
)
oraEM4AlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertSeverity.setStatus("mandatory")
_OraEM4AlertMessage_Type = DisplayString
_OraEM4AlertMessage_Object = MibTableColumn
oraEM4AlertMessage = _OraEM4AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 10),
    _OraEM4AlertMessage_Type()
)
oraEM4AlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertMessage.setStatus("mandatory")
_OraEM4AlertRuleName_Type = DisplayString
_OraEM4AlertRuleName_Object = MibTableColumn
oraEM4AlertRuleName = _OraEM4AlertRuleName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 11),
    _OraEM4AlertRuleName_Type()
)
oraEM4AlertRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertRuleName.setStatus("mandatory")
_OraEM4AlertRuleOwner_Type = DisplayString
_OraEM4AlertRuleOwner_Object = MibTableColumn
oraEM4AlertRuleOwner = _OraEM4AlertRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 12),
    _OraEM4AlertRuleOwner_Type()
)
oraEM4AlertRuleOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertRuleOwner.setStatus("mandatory")
_OraEM4AlertMetricValue_Type = DisplayString
_OraEM4AlertMetricValue_Object = MibTableColumn
oraEM4AlertMetricValue = _OraEM4AlertMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 13),
    _OraEM4AlertMetricValue_Type()
)
oraEM4AlertMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertMetricValue.setStatus("mandatory")
_OraEM4AlertContext_Type = DisplayString
_OraEM4AlertContext_Object = MibTableColumn
oraEM4AlertContext = _OraEM4AlertContext_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 1, 1, 14),
    _OraEM4AlertContext_Type()
)
oraEM4AlertContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4AlertContext.setStatus("mandatory")
_OraEM4JobAlertTable_Object = MibTable
oraEM4JobAlertTable = _OraEM4JobAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2)
)
if mibBuilder.loadTexts:
    oraEM4JobAlertTable.setStatus("mandatory")
_OraEM4JobAlertEntry_Object = MibTableRow
oraEM4JobAlertEntry = _OraEM4JobAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1)
)
oraEM4JobAlertEntry.setIndexNames(
    (0, "ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertIndex"),
)
if mibBuilder.loadTexts:
    oraEM4JobAlertEntry.setStatus("mandatory")
_OraEM4JobAlertIndex_Type = Integer32
_OraEM4JobAlertIndex_Object = MibTableColumn
oraEM4JobAlertIndex = _OraEM4JobAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 1),
    _OraEM4JobAlertIndex_Type()
)
oraEM4JobAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertIndex.setStatus("mandatory")
_OraEM4JobAlertJobName_Type = DisplayString
_OraEM4JobAlertJobName_Object = MibTableColumn
oraEM4JobAlertJobName = _OraEM4JobAlertJobName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 2),
    _OraEM4JobAlertJobName_Type()
)
oraEM4JobAlertJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertJobName.setStatus("mandatory")
_OraEM4JobAlertJobOwner_Type = DisplayString
_OraEM4JobAlertJobOwner_Object = MibTableColumn
oraEM4JobAlertJobOwner = _OraEM4JobAlertJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 3),
    _OraEM4JobAlertJobOwner_Type()
)
oraEM4JobAlertJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertJobOwner.setStatus("mandatory")
_OraEM4JobAlertJobType_Type = DisplayString
_OraEM4JobAlertJobType_Object = MibTableColumn
oraEM4JobAlertJobType = _OraEM4JobAlertJobType_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 4),
    _OraEM4JobAlertJobType_Type()
)
oraEM4JobAlertJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertJobType.setStatus("mandatory")
_OraEM4JobAlertJobStatus_Type = DisplayString
_OraEM4JobAlertJobStatus_Object = MibTableColumn
oraEM4JobAlertJobStatus = _OraEM4JobAlertJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 5),
    _OraEM4JobAlertJobStatus_Type()
)
oraEM4JobAlertJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertJobStatus.setStatus("mandatory")
_OraEM4JobAlertTargets_Type = DisplayString
_OraEM4JobAlertTargets_Object = MibTableColumn
oraEM4JobAlertTargets = _OraEM4JobAlertTargets_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 6),
    _OraEM4JobAlertTargets_Type()
)
oraEM4JobAlertTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertTargets.setStatus("mandatory")
_OraEM4JobAlertTimeStamp_Type = DisplayString
_OraEM4JobAlertTimeStamp_Object = MibTableColumn
oraEM4JobAlertTimeStamp = _OraEM4JobAlertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 7),
    _OraEM4JobAlertTimeStamp_Type()
)
oraEM4JobAlertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertTimeStamp.setStatus("mandatory")
_OraEM4JobAlertRuleName_Type = DisplayString
_OraEM4JobAlertRuleName_Object = MibTableColumn
oraEM4JobAlertRuleName = _OraEM4JobAlertRuleName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 8),
    _OraEM4JobAlertRuleName_Type()
)
oraEM4JobAlertRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertRuleName.setStatus("mandatory")
_OraEM4JobAlertRuleOwner_Type = DisplayString
_OraEM4JobAlertRuleOwner_Object = MibTableColumn
oraEM4JobAlertRuleOwner = _OraEM4JobAlertRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 9),
    _OraEM4JobAlertRuleOwner_Type()
)
oraEM4JobAlertRuleOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertRuleOwner.setStatus("mandatory")
_OraEM4JobAlertMetricName_Type = DisplayString
_OraEM4JobAlertMetricName_Object = MibTableColumn
oraEM4JobAlertMetricName = _OraEM4JobAlertMetricName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 10),
    _OraEM4JobAlertMetricName_Type()
)
oraEM4JobAlertMetricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertMetricName.setStatus("mandatory")
_OraEM4JobAlertMetricValue_Type = DisplayString
_OraEM4JobAlertMetricValue_Object = MibTableColumn
oraEM4JobAlertMetricValue = _OraEM4JobAlertMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 11),
    _OraEM4JobAlertMetricValue_Type()
)
oraEM4JobAlertMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertMetricValue.setStatus("mandatory")
_OraEM4JobAlertContext_Type = DisplayString
_OraEM4JobAlertContext_Object = MibTableColumn
oraEM4JobAlertContext = _OraEM4JobAlertContext_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 12),
    _OraEM4JobAlertContext_Type()
)
oraEM4JobAlertContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertContext.setStatus("mandatory")
_OraEM4JobAlertKeyName_Type = DisplayString
_OraEM4JobAlertKeyName_Object = MibTableColumn
oraEM4JobAlertKeyName = _OraEM4JobAlertKeyName_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 13),
    _OraEM4JobAlertKeyName_Type()
)
oraEM4JobAlertKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertKeyName.setStatus("mandatory")
_OraEM4JobAlertKeyValue_Type = DisplayString
_OraEM4JobAlertKeyValue_Object = MibTableColumn
oraEM4JobAlertKeyValue = _OraEM4JobAlertKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 14),
    _OraEM4JobAlertKeyValue_Type()
)
oraEM4JobAlertKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertKeyValue.setStatus("mandatory")
_OraEM4JobAlertSeverity_Type = DisplayString
_OraEM4JobAlertSeverity_Object = MibTableColumn
oraEM4JobAlertSeverity = _OraEM4JobAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 111, 15, 1, 2, 1, 15),
    _OraEM4JobAlertSeverity_Type()
)
oraEM4JobAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraEM4JobAlertSeverity.setStatus("mandatory")
_OraEM4Traps_ObjectIdentity = ObjectIdentity
oraEM4Traps = _OraEM4Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 15, 2)
)

# Managed Objects groups


# Notification objects

oraEM4Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 15, 2, 0, 1)
)
oraEM4Alert.setObjects(
      *(("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertTargetName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertTargetType"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertHostName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertMetricName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertKeyName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertKeyValue"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertTimeStamp"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertSeverity"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertMessage"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertRuleName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertRuleOwner"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertMetricValue"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4AlertContext"))
)
if mibBuilder.loadTexts:
    oraEM4Alert.setStatus(
        ""
    )

oraEM4JobAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 15, 2, 0, 2)
)
oraEM4JobAlert.setObjects(
      *(("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertJobName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertJobOwner"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertJobType"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertJobStatus"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertTargets"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertTimeStamp"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertRuleName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertRuleOwner"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertMetricName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertMetricValue"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertContext"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertKeyName"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertKeyValue"),
        ("ORACLE-ENTERPRISE-MANAGER-4-MIB", "oraEM4JobAlertSeverity"))
)
if mibBuilder.loadTexts:
    oraEM4JobAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORACLE-ENTERPRISE-MANAGER-4-MIB",
    **{"oracle": oracle,
       "oraEM4": oraEM4,
       "oraEM4Objects": oraEM4Objects,
       "oraEM4AlertTable": oraEM4AlertTable,
       "oraEM4AlertEntry": oraEM4AlertEntry,
       "oraEM4AlertIndex": oraEM4AlertIndex,
       "oraEM4AlertTargetName": oraEM4AlertTargetName,
       "oraEM4AlertTargetType": oraEM4AlertTargetType,
       "oraEM4AlertHostName": oraEM4AlertHostName,
       "oraEM4AlertMetricName": oraEM4AlertMetricName,
       "oraEM4AlertKeyName": oraEM4AlertKeyName,
       "oraEM4AlertKeyValue": oraEM4AlertKeyValue,
       "oraEM4AlertTimeStamp": oraEM4AlertTimeStamp,
       "oraEM4AlertSeverity": oraEM4AlertSeverity,
       "oraEM4AlertMessage": oraEM4AlertMessage,
       "oraEM4AlertRuleName": oraEM4AlertRuleName,
       "oraEM4AlertRuleOwner": oraEM4AlertRuleOwner,
       "oraEM4AlertMetricValue": oraEM4AlertMetricValue,
       "oraEM4AlertContext": oraEM4AlertContext,
       "oraEM4JobAlertTable": oraEM4JobAlertTable,
       "oraEM4JobAlertEntry": oraEM4JobAlertEntry,
       "oraEM4JobAlertIndex": oraEM4JobAlertIndex,
       "oraEM4JobAlertJobName": oraEM4JobAlertJobName,
       "oraEM4JobAlertJobOwner": oraEM4JobAlertJobOwner,
       "oraEM4JobAlertJobType": oraEM4JobAlertJobType,
       "oraEM4JobAlertJobStatus": oraEM4JobAlertJobStatus,
       "oraEM4JobAlertTargets": oraEM4JobAlertTargets,
       "oraEM4JobAlertTimeStamp": oraEM4JobAlertTimeStamp,
       "oraEM4JobAlertRuleName": oraEM4JobAlertRuleName,
       "oraEM4JobAlertRuleOwner": oraEM4JobAlertRuleOwner,
       "oraEM4JobAlertMetricName": oraEM4JobAlertMetricName,
       "oraEM4JobAlertMetricValue": oraEM4JobAlertMetricValue,
       "oraEM4JobAlertContext": oraEM4JobAlertContext,
       "oraEM4JobAlertKeyName": oraEM4JobAlertKeyName,
       "oraEM4JobAlertKeyValue": oraEM4JobAlertKeyValue,
       "oraEM4JobAlertSeverity": oraEM4JobAlertSeverity,
       "oraEM4Traps": oraEM4Traps,
       "oraEM4Alert": oraEM4Alert,
       "oraEM4JobAlert": oraEM4JobAlert}
)
