# SNMP MIB module (CISCO-MODULE-AUTO-SHUTDOWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:51 2024
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

(entPhysicalIndex,
 entPhysicalModelName,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalModelName",
    "entPhysicalName")

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

ciscoModuleAutoShutdownMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386)
)
ciscoModuleAutoShutdownMIB.setRevisions(
        ("2008-03-12 00:00",
         "2003-12-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoModuleAutoShutSysAction(Integer32, TextualConvention):
    status = "current"
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
        *(("other", 1),
          ("powerCycle", 3),
          ("powerDown", 4),
          ("reset", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CmasMIBNotifs_ObjectIdentity = ObjectIdentity
cmasMIBNotifs = _CmasMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 0)
)
_CmasMIBObjects_ObjectIdentity = ObjectIdentity
cmasMIBObjects = _CmasMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1)
)
_CmasGlobal_ObjectIdentity = ObjectIdentity
cmasGlobal = _CmasGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1)
)
_CmasFrequency_Type = Unsigned32
_CmasFrequency_Object = MibScalar
cmasFrequency = _CmasFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 1),
    _CmasFrequency_Type()
)
cmasFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmasFrequency.setStatus("current")
_CmasPeriod_Type = Unsigned32
_CmasPeriod_Object = MibScalar
cmasPeriod = _CmasPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 2),
    _CmasPeriod_Type()
)
cmasPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmasPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cmasPeriod.setUnits("minutes")
_CmasNotifObjects_ObjectIdentity = ObjectIdentity
cmasNotifObjects = _CmasNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2)
)


class _CmasMIBEnableNotification_Type(TruthValue):
    """Custom type cmasMIBEnableNotification based on TruthValue"""


_CmasMIBEnableNotification_Object = MibScalar
cmasMIBEnableNotification = _CmasMIBEnableNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 1),
    _CmasMIBEnableNotification_Type()
)
cmasMIBEnableNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmasMIBEnableNotification.setStatus("current")


class _CmasModuleSysActionNotifEnable_Type(TruthValue):
    """Custom type cmasModuleSysActionNotifEnable based on TruthValue"""


_CmasModuleSysActionNotifEnable_Object = MibScalar
cmasModuleSysActionNotifEnable = _CmasModuleSysActionNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 2),
    _CmasModuleSysActionNotifEnable_Type()
)
cmasModuleSysActionNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmasModuleSysActionNotifEnable.setStatus("current")
_CmasModule_ObjectIdentity = ObjectIdentity
cmasModule = _CmasModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3)
)
_CmasModuleTable_Object = MibTable
cmasModuleTable = _CmasModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmasModuleTable.setStatus("current")
_CmasModuleEntry_Object = MibTableRow
cmasModuleEntry = _CmasModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1)
)
cmasModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmasModuleEntry.setStatus("current")
_CmasModuleEnable_Type = TruthValue
_CmasModuleEnable_Object = MibTableColumn
cmasModuleEnable = _CmasModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 1),
    _CmasModuleEnable_Type()
)
cmasModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmasModuleEnable.setStatus("current")
_CmasModuleNumResets_Type = Gauge32
_CmasModuleNumResets_Object = MibTableColumn
cmasModuleNumResets = _CmasModuleNumResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 2),
    _CmasModuleNumResets_Type()
)
cmasModuleNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmasModuleNumResets.setStatus("current")
_CmasModuleLastResetReason_Type = SnmpAdminString
_CmasModuleLastResetReason_Object = MibTableColumn
cmasModuleLastResetReason = _CmasModuleLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 3),
    _CmasModuleLastResetReason_Type()
)
cmasModuleLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmasModuleLastResetReason.setStatus("current")
_CmasModuleLastResetTime_Type = DateAndTime
_CmasModuleLastResetTime_Object = MibTableColumn
cmasModuleLastResetTime = _CmasModuleLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 4),
    _CmasModuleLastResetTime_Type()
)
cmasModuleLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmasModuleLastResetTime.setStatus("current")
_CmasModuleSysActionObjects_ObjectIdentity = ObjectIdentity
cmasModuleSysActionObjects = _CmasModuleSysActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4)
)
_CmasModuleSysAction_Type = CiscoModuleAutoShutSysAction
_CmasModuleSysAction_Object = MibScalar
cmasModuleSysAction = _CmasModuleSysAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 1),
    _CmasModuleSysAction_Type()
)
cmasModuleSysAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmasModuleSysAction.setStatus("current")
_CmasModuleSysActionReason_Type = SnmpAdminString
_CmasModuleSysActionReason_Object = MibScalar
cmasModuleSysActionReason = _CmasModuleSysActionReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 2),
    _CmasModuleSysActionReason_Type()
)
cmasModuleSysActionReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmasModuleSysActionReason.setStatus("current")
_CmasMIBConformance_ObjectIdentity = ObjectIdentity
cmasMIBConformance = _CmasMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2)
)
_CmasMIBCompliances_ObjectIdentity = ObjectIdentity
cmasMIBCompliances = _CmasMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1)
)
_CmasMIBGroups_ObjectIdentity = ObjectIdentity
cmasMIBGroups = _CmasMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2)
)

# Managed Objects groups

cmasModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 1)
)
cmasModuleGroup.setObjects(
      *(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasFrequency"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasPeriod"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleEnable"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetTime"))
)
if mibBuilder.loadTexts:
    cmasModuleGroup.setStatus("current")

cmasNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 2)
)
cmasNotificationEnableGroup.setObjects(
    ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasMIBEnableNotification")
)
if mibBuilder.loadTexts:
    cmasNotificationEnableGroup.setStatus("current")

cmasModuleSysActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 4)
)
cmasModuleSysActionGroup.setObjects(
      *(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotifEnable"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
)
if mibBuilder.loadTexts:
    cmasModuleSysActionGroup.setStatus("current")


# Notification objects

cmasModuleAutoShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 1)
)
cmasModuleAutoShutdown.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalModelName"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"))
)
if mibBuilder.loadTexts:
    cmasModuleAutoShutdown.setStatus(
        "current"
    )

cmasModuleSysActionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 2)
)
cmasModuleSysActionNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalModelName"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"),
        ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
)
if mibBuilder.loadTexts:
    cmasModuleSysActionNotif.setStatus(
        "current"
    )


# Notifications groups

cmasNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 3)
)
cmasNotificationsGroup.setObjects(
    ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleAutoShutdown")
)
if mibBuilder.loadTexts:
    cmasNotificationsGroup.setStatus(
        "current"
    )

cmasNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 5)
)
cmasNotificationsGroup2.setObjects(
    ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotif")
)
if mibBuilder.loadTexts:
    cmasNotificationsGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmasMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmasMIBCompliance.setStatus(
        "deprecated"
    )

cmasMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmasMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MODULE-AUTO-SHUTDOWN-MIB",
    **{"CiscoModuleAutoShutSysAction": CiscoModuleAutoShutSysAction,
       "ciscoModuleAutoShutdownMIB": ciscoModuleAutoShutdownMIB,
       "cmasMIBNotifs": cmasMIBNotifs,
       "cmasModuleAutoShutdown": cmasModuleAutoShutdown,
       "cmasModuleSysActionNotif": cmasModuleSysActionNotif,
       "cmasMIBObjects": cmasMIBObjects,
       "cmasGlobal": cmasGlobal,
       "cmasFrequency": cmasFrequency,
       "cmasPeriod": cmasPeriod,
       "cmasNotifObjects": cmasNotifObjects,
       "cmasMIBEnableNotification": cmasMIBEnableNotification,
       "cmasModuleSysActionNotifEnable": cmasModuleSysActionNotifEnable,
       "cmasModule": cmasModule,
       "cmasModuleTable": cmasModuleTable,
       "cmasModuleEntry": cmasModuleEntry,
       "cmasModuleEnable": cmasModuleEnable,
       "cmasModuleNumResets": cmasModuleNumResets,
       "cmasModuleLastResetReason": cmasModuleLastResetReason,
       "cmasModuleLastResetTime": cmasModuleLastResetTime,
       "cmasModuleSysActionObjects": cmasModuleSysActionObjects,
       "cmasModuleSysAction": cmasModuleSysAction,
       "cmasModuleSysActionReason": cmasModuleSysActionReason,
       "cmasMIBConformance": cmasMIBConformance,
       "cmasMIBCompliances": cmasMIBCompliances,
       "cmasMIBCompliance": cmasMIBCompliance,
       "cmasMIBCompliance2": cmasMIBCompliance2,
       "cmasMIBGroups": cmasMIBGroups,
       "cmasModuleGroup": cmasModuleGroup,
       "cmasNotificationEnableGroup": cmasNotificationEnableGroup,
       "cmasNotificationsGroup": cmasNotificationsGroup,
       "cmasModuleSysActionGroup": cmasModuleSysActionGroup,
       "cmasNotificationsGroup2": cmasNotificationsGroup2}
)
