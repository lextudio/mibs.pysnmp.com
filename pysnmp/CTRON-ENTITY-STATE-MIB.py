# SNMP MIB module (CTRON-ENTITY-STATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:47 2024
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

(EntityAdminState,
 EntityAlarmStatus,
 EntityOperState,
 EntityStandbyStatus,
 EntityUsageState) = mibBuilder.importSymbols(
    "CTRON-ENTITY-STATE-TC-MIB",
    "EntityAdminState",
    "EntityAlarmStatus",
    "EntityOperState",
    "EntityStandbyStatus",
    "EntityUsageState")

(ctEntityStateMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctEntityStateMib")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ctEntityStateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1)
)
ctEntityStateMIB.setRevisions(
        ("2005-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtEntStateNotifications_ObjectIdentity = ObjectIdentity
ctEntStateNotifications = _CtEntStateNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0)
)
_CtEntStateObjects_ObjectIdentity = ObjectIdentity
ctEntStateObjects = _CtEntStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1)
)
_CtEntStateTable_Object = MibTable
ctEntStateTable = _CtEntStateTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctEntStateTable.setStatus("current")
_CtEntStateEntry_Object = MibTableRow
ctEntStateEntry = _CtEntStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1)
)
ctEntStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ctEntStateEntry.setStatus("current")
_CtEntStateLastChanged_Type = DateAndTime
_CtEntStateLastChanged_Object = MibTableColumn
ctEntStateLastChanged = _CtEntStateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 1),
    _CtEntStateLastChanged_Type()
)
ctEntStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEntStateLastChanged.setStatus("current")
_CtEntStateAdmin_Type = EntityAdminState
_CtEntStateAdmin_Object = MibTableColumn
ctEntStateAdmin = _CtEntStateAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 2),
    _CtEntStateAdmin_Type()
)
ctEntStateAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEntStateAdmin.setStatus("current")
_CtEntStateOper_Type = EntityOperState
_CtEntStateOper_Object = MibTableColumn
ctEntStateOper = _CtEntStateOper_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 3),
    _CtEntStateOper_Type()
)
ctEntStateOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEntStateOper.setStatus("current")
_CtEntStateUsage_Type = EntityUsageState
_CtEntStateUsage_Object = MibTableColumn
ctEntStateUsage = _CtEntStateUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 4),
    _CtEntStateUsage_Type()
)
ctEntStateUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEntStateUsage.setStatus("current")
_CtEntStateAlarm_Type = EntityAlarmStatus
_CtEntStateAlarm_Object = MibTableColumn
ctEntStateAlarm = _CtEntStateAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 5),
    _CtEntStateAlarm_Type()
)
ctEntStateAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEntStateAlarm.setStatus("current")
_CtEntStateStandby_Type = EntityStandbyStatus
_CtEntStateStandby_Object = MibTableColumn
ctEntStateStandby = _CtEntStateStandby_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 6),
    _CtEntStateStandby_Type()
)
ctEntStateStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctEntStateStandby.setStatus("current")
_CtEntStateConformance_ObjectIdentity = ObjectIdentity
ctEntStateConformance = _CtEntStateConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2)
)
_CtEntStateCompliances_ObjectIdentity = ObjectIdentity
ctEntStateCompliances = _CtEntStateCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1)
)
_CtEntStateGroups_ObjectIdentity = ObjectIdentity
ctEntStateGroups = _CtEntStateGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2)
)

# Managed Objects groups

ctEntStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 1)
)
ctEntStateGroup.setObjects(
      *(("CTRON-ENTITY-STATE-MIB", "ctEntStateLastChanged"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateOper"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateUsage"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateStandby"))
)
if mibBuilder.loadTexts:
    ctEntStateGroup.setStatus("current")


# Notification objects

ctEntStateOperEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 1)
)
ctEntStateOperEnabled.setObjects(
      *(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
)
if mibBuilder.loadTexts:
    ctEntStateOperEnabled.setStatus(
        "current"
    )

ctEntStateOperDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 2)
)
ctEntStateOperDisabled.setObjects(
      *(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
)
if mibBuilder.loadTexts:
    ctEntStateOperDisabled.setStatus(
        "current"
    )


# Notifications groups

ctEntStateNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 2)
)
ctEntStateNotificationsGroup.setObjects(
      *(("CTRON-ENTITY-STATE-MIB", "ctEntStateOperEnabled"),
        ("CTRON-ENTITY-STATE-MIB", "ctEntStateOperDisabled"))
)
if mibBuilder.loadTexts:
    ctEntStateNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ctEntStateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctEntStateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ENTITY-STATE-MIB",
    **{"ctEntityStateMIB": ctEntityStateMIB,
       "ctEntStateNotifications": ctEntStateNotifications,
       "ctEntStateOperEnabled": ctEntStateOperEnabled,
       "ctEntStateOperDisabled": ctEntStateOperDisabled,
       "ctEntStateObjects": ctEntStateObjects,
       "ctEntStateTable": ctEntStateTable,
       "ctEntStateEntry": ctEntStateEntry,
       "ctEntStateLastChanged": ctEntStateLastChanged,
       "ctEntStateAdmin": ctEntStateAdmin,
       "ctEntStateOper": ctEntStateOper,
       "ctEntStateUsage": ctEntStateUsage,
       "ctEntStateAlarm": ctEntStateAlarm,
       "ctEntStateStandby": ctEntStateStandby,
       "ctEntStateConformance": ctEntStateConformance,
       "ctEntStateCompliances": ctEntStateCompliances,
       "ctEntStateCompliance": ctEntStateCompliance,
       "ctEntStateGroups": ctEntStateGroups,
       "ctEntStateGroup": ctEntStateGroup,
       "ctEntStateNotificationsGroup": ctEntStateNotificationsGroup}
)
