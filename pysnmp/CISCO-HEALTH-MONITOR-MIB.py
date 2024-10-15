# SNMP MIB module (CISCO-HEALTH-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HEALTH-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

ciscoHealthMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243)
)
ciscoHealthMonitorMIB.setRevisions(
        ("2003-09-12 12:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HealthLevel(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoHealthMonitorMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoHealthMonitorMIBNotifs = _CiscoHealthMonitorMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 0)
)
_CiscoHealthMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHealthMonitorMIBObjects = _CiscoHealthMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1)
)
_CiscoHealthMonitorTable_Object = MibTable
ciscoHealthMonitorTable = _CiscoHealthMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorTable.setStatus("current")
_CiscoHealthMonitorEntry_Object = MibTableRow
ciscoHealthMonitorEntry = _CiscoHealthMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1)
)
ciscoHealthMonitorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (1, "CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorSubsysName"),
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorEntry.setStatus("current")


class _CiscoHealthMonitorSubsysName_Type(SnmpAdminString):
    """Custom type ciscoHealthMonitorSubsysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CiscoHealthMonitorSubsysName_Type.__name__ = "SnmpAdminString"
_CiscoHealthMonitorSubsysName_Object = MibTableColumn
ciscoHealthMonitorSubsysName = _CiscoHealthMonitorSubsysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 1),
    _CiscoHealthMonitorSubsysName_Type()
)
ciscoHealthMonitorSubsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoHealthMonitorSubsysName.setStatus("current")
_CiscoHealthMonitorHealth_Type = HealthLevel
_CiscoHealthMonitorHealth_Object = MibTableColumn
ciscoHealthMonitorHealth = _CiscoHealthMonitorHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 2),
    _CiscoHealthMonitorHealth_Type()
)
ciscoHealthMonitorHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealth.setStatus("current")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealth.setUnits("0.01 percent")


class _CiscoHealthMonitorHealthNotifyEnable_Type(TruthValue):
    """Custom type ciscoHealthMonitorHealthNotifyEnable based on TruthValue"""


_CiscoHealthMonitorHealthNotifyEnable_Object = MibTableColumn
ciscoHealthMonitorHealthNotifyEnable = _CiscoHealthMonitorHealthNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 3),
    _CiscoHealthMonitorHealthNotifyEnable_Type()
)
ciscoHealthMonitorHealthNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthNotifyEnable.setStatus("current")


class _CiscoHealthMonitorHealthNotifyHighThreshold_Type(HealthLevel):
    """Custom type ciscoHealthMonitorHealthNotifyHighThreshold based on HealthLevel"""
    defaultValue = 10000


_CiscoHealthMonitorHealthNotifyHighThreshold_Object = MibTableColumn
ciscoHealthMonitorHealthNotifyHighThreshold = _CiscoHealthMonitorHealthNotifyHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 4),
    _CiscoHealthMonitorHealthNotifyHighThreshold_Type()
)
ciscoHealthMonitorHealthNotifyHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthNotifyHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthNotifyHighThreshold.setUnits("0.01 percent")


class _CiscoHealthMonitorHealthNotifyLowThreshold_Type(HealthLevel):
    """Custom type ciscoHealthMonitorHealthNotifyLowThreshold based on HealthLevel"""
    defaultValue = 0


_CiscoHealthMonitorHealthNotifyLowThreshold_Object = MibTableColumn
ciscoHealthMonitorHealthNotifyLowThreshold = _CiscoHealthMonitorHealthNotifyLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 5),
    _CiscoHealthMonitorHealthNotifyLowThreshold_Type()
)
ciscoHealthMonitorHealthNotifyLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthNotifyLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthNotifyLowThreshold.setUnits("0.01 percent")
_CiscoHealthMonitorCatastrophicFaults_Type = Counter32
_CiscoHealthMonitorCatastrophicFaults_Object = MibTableColumn
ciscoHealthMonitorCatastrophicFaults = _CiscoHealthMonitorCatastrophicFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 6),
    _CiscoHealthMonitorCatastrophicFaults_Type()
)
ciscoHealthMonitorCatastrophicFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorCatastrophicFaults.setStatus("current")
_CiscoHealthMonitorCriticalFaults_Type = Counter32
_CiscoHealthMonitorCriticalFaults_Object = MibTableColumn
ciscoHealthMonitorCriticalFaults = _CiscoHealthMonitorCriticalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 7),
    _CiscoHealthMonitorCriticalFaults_Type()
)
ciscoHealthMonitorCriticalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorCriticalFaults.setStatus("current")
_CiscoHealthMonitorHighSeverityFaults_Type = Counter32
_CiscoHealthMonitorHighSeverityFaults_Object = MibTableColumn
ciscoHealthMonitorHighSeverityFaults = _CiscoHealthMonitorHighSeverityFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 8),
    _CiscoHealthMonitorHighSeverityFaults_Type()
)
ciscoHealthMonitorHighSeverityFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorHighSeverityFaults.setStatus("current")
_CiscoHealthMonitorMediumSeverityFaults_Type = Counter32
_CiscoHealthMonitorMediumSeverityFaults_Object = MibTableColumn
ciscoHealthMonitorMediumSeverityFaults = _CiscoHealthMonitorMediumSeverityFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 9),
    _CiscoHealthMonitorMediumSeverityFaults_Type()
)
ciscoHealthMonitorMediumSeverityFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorMediumSeverityFaults.setStatus("current")
_CiscoHealthMonitorLowSeverityFaults_Type = Counter32
_CiscoHealthMonitorLowSeverityFaults_Object = MibTableColumn
ciscoHealthMonitorLowSeverityFaults = _CiscoHealthMonitorLowSeverityFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 10),
    _CiscoHealthMonitorLowSeverityFaults_Type()
)
ciscoHealthMonitorLowSeverityFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorLowSeverityFaults.setStatus("current")
_CiscoHealthMonitorPositiveEvents_Type = Counter32
_CiscoHealthMonitorPositiveEvents_Object = MibTableColumn
ciscoHealthMonitorPositiveEvents = _CiscoHealthMonitorPositiveEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 11),
    _CiscoHealthMonitorPositiveEvents_Type()
)
ciscoHealthMonitorPositiveEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonitorPositiveEvents.setStatus("current")
_CiscoHealthMonitorMIBConform_ObjectIdentity = ObjectIdentity
ciscoHealthMonitorMIBConform = _CiscoHealthMonitorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2)
)
_CiscoHealthMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoHealthMonitorMIBCompliances = _CiscoHealthMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1)
)
_CiscoHealthMonitorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoHealthMonitorMIBGroups = _CiscoHealthMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2)
)

# Managed Objects groups

ciscoHealthMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 1)
)
ciscoHealthMonitorGroup.setObjects(
      *(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyEnable"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyHighThreshold"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyLowThreshold"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCatastrophicFaults"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCriticalFaults"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHighSeverityFaults"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorMediumSeverityFaults"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorLowSeverityFaults"),
        ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorPositiveEvents"))
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorGroup.setStatus("current")


# Notification objects

ciscoHealthMonitorHealthLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 0, 1)
)
ciscoHealthMonitorHealthLevel.setObjects(
    ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth")
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorHealthLevel.setStatus(
        "current"
    )


# Notifications groups

ciscoHealthMonitorMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 2)
)
ciscoHealthMonitorMIBNotificationGroup.setObjects(
    ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthLevel")
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoHealthMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHealthMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HEALTH-MONITOR-MIB",
    **{"HealthLevel": HealthLevel,
       "ciscoHealthMonitorMIB": ciscoHealthMonitorMIB,
       "ciscoHealthMonitorMIBNotifs": ciscoHealthMonitorMIBNotifs,
       "ciscoHealthMonitorHealthLevel": ciscoHealthMonitorHealthLevel,
       "ciscoHealthMonitorMIBObjects": ciscoHealthMonitorMIBObjects,
       "ciscoHealthMonitorTable": ciscoHealthMonitorTable,
       "ciscoHealthMonitorEntry": ciscoHealthMonitorEntry,
       "ciscoHealthMonitorSubsysName": ciscoHealthMonitorSubsysName,
       "ciscoHealthMonitorHealth": ciscoHealthMonitorHealth,
       "ciscoHealthMonitorHealthNotifyEnable": ciscoHealthMonitorHealthNotifyEnable,
       "ciscoHealthMonitorHealthNotifyHighThreshold": ciscoHealthMonitorHealthNotifyHighThreshold,
       "ciscoHealthMonitorHealthNotifyLowThreshold": ciscoHealthMonitorHealthNotifyLowThreshold,
       "ciscoHealthMonitorCatastrophicFaults": ciscoHealthMonitorCatastrophicFaults,
       "ciscoHealthMonitorCriticalFaults": ciscoHealthMonitorCriticalFaults,
       "ciscoHealthMonitorHighSeverityFaults": ciscoHealthMonitorHighSeverityFaults,
       "ciscoHealthMonitorMediumSeverityFaults": ciscoHealthMonitorMediumSeverityFaults,
       "ciscoHealthMonitorLowSeverityFaults": ciscoHealthMonitorLowSeverityFaults,
       "ciscoHealthMonitorPositiveEvents": ciscoHealthMonitorPositiveEvents,
       "ciscoHealthMonitorMIBConform": ciscoHealthMonitorMIBConform,
       "ciscoHealthMonitorMIBCompliances": ciscoHealthMonitorMIBCompliances,
       "ciscoHealthMonitorMIBCompliance": ciscoHealthMonitorMIBCompliance,
       "ciscoHealthMonitorMIBGroups": ciscoHealthMonitorMIBGroups,
       "ciscoHealthMonitorGroup": ciscoHealthMonitorGroup,
       "ciscoHealthMonitorMIBNotificationGroup": ciscoHealthMonitorMIBNotificationGroup}
)
