# SNMP MIB module (PDN-ENTITY-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ENTITY-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:37 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(pdnEntityRedundancy,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnEntityRedundancy")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdnEntRedunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1)
)
pdnEntRedunMIB.setRevisions(
        ("2003-07-25 13:00",
         "2003-05-22 10:00",
         "2003-05-04 17:00",
         "2003-03-03 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnRedunStates(Integer32, TextualConvention):
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
        *(("activeAlarmState", 2),
          ("activeState", 1),
          ("standbyAlarmState", 4),
          ("standbyState", 3))
    )



class PdnRedunCmd(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedswitch", 3),
          ("noCmd", 1),
          ("switch", 2))
    )



class PdnRedunAlarmStatus(Bits, TextualConvention):
    status = "current"


class PdnRedunGeneralAlarmStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PdnEntityRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
pdnEntityRedundancyMIBObjects = _PdnEntityRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1)
)


class _PdnEntityRedundancySelection_Type(Integer32):
    """Custom type pdnEntityRedundancySelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PdnEntityRedundancySelection_Type.__name__ = "Integer32"
_PdnEntityRedundancySelection_Object = MibScalar
pdnEntityRedundancySelection = _PdnEntityRedundancySelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 1),
    _PdnEntityRedundancySelection_Type()
)
pdnEntityRedundancySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnEntityRedundancySelection.setStatus("current")


class _PdnYCableSelection_Type(Integer32):
    """Custom type pdnYCableSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PdnYCableSelection_Type.__name__ = "Integer32"
_PdnYCableSelection_Object = MibScalar
pdnYCableSelection = _PdnYCableSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 2),
    _PdnYCableSelection_Type()
)
pdnYCableSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnYCableSelection.setStatus("current")
_PdnRedunGeneralAlarmStatus_Type = PdnRedunGeneralAlarmStatus
_PdnRedunGeneralAlarmStatus_Object = MibScalar
pdnRedunGeneralAlarmStatus = _PdnRedunGeneralAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 3),
    _PdnRedunGeneralAlarmStatus_Type()
)
pdnRedunGeneralAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnRedunGeneralAlarmStatus.setStatus("current")
_PdnRedunCmdTable_Object = MibTable
pdnRedunCmdTable = _PdnRedunCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdnRedunCmdTable.setStatus("current")
_PdnRedunCmdEntry_Object = MibTableRow
pdnRedunCmdEntry = _PdnRedunCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1)
)
pdnRedunCmdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    pdnRedunCmdEntry.setStatus("current")
_PdnRedunCommand_Type = PdnRedunCmd
_PdnRedunCommand_Object = MibTableColumn
pdnRedunCommand = _PdnRedunCommand_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1, 1),
    _PdnRedunCommand_Type()
)
pdnRedunCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnRedunCommand.setStatus("current")
_PdnRedunStatusTable_Object = MibTable
pdnRedunStatusTable = _PdnRedunStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pdnRedunStatusTable.setStatus("current")
_PdnRedunStatusEntry_Object = MibTableRow
pdnRedunStatusEntry = _PdnRedunStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1)
)
pdnRedunStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    pdnRedunStatusEntry.setStatus("current")
_PdnRedunEntityState_Type = PdnRedunStates
_PdnRedunEntityState_Object = MibTableColumn
pdnRedunEntityState = _PdnRedunEntityState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 1),
    _PdnRedunEntityState_Type()
)
pdnRedunEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnRedunEntityState.setStatus("current")
_PdnRedunAlarmStatus_Type = PdnRedunAlarmStatus
_PdnRedunAlarmStatus_Object = MibTableColumn
pdnRedunAlarmStatus = _PdnRedunAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 2),
    _PdnRedunAlarmStatus_Type()
)
pdnRedunAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnRedunAlarmStatus.setStatus("current")
_PdnRedunNotificationEnable_Type = PdnRedunAlarmStatus
_PdnRedunNotificationEnable_Object = MibTableColumn
pdnRedunNotificationEnable = _PdnRedunNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 3),
    _PdnRedunNotificationEnable_Type()
)
pdnRedunNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnRedunNotificationEnable.setStatus("current")
_PdnRedunGeneralNotificationEnable_Type = PdnRedunGeneralAlarmStatus
_PdnRedunGeneralNotificationEnable_Object = MibScalar
pdnRedunGeneralNotificationEnable = _PdnRedunGeneralNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 6),
    _PdnRedunGeneralNotificationEnable_Type()
)
pdnRedunGeneralNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnRedunGeneralNotificationEnable.setStatus("current")
_PdnEntityRedundancyNotifications_ObjectIdentity = ObjectIdentity
pdnEntityRedundancyNotifications = _PdnEntityRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2)
)
_PdnRedunNotificationsPrefix_ObjectIdentity = ObjectIdentity
pdnRedunNotificationsPrefix = _PdnRedunNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0)
)
_PdnEntityRedundancyConformance_ObjectIdentity = ObjectIdentity
pdnEntityRedundancyConformance = _PdnEntityRedundancyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3)
)
_PdnEntityRedundancyCompliances_ObjectIdentity = ObjectIdentity
pdnEntityRedundancyCompliances = _PdnEntityRedundancyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1)
)
_PdnEntityRedundancyGroups_ObjectIdentity = ObjectIdentity
pdnEntityRedundancyGroups = _PdnEntityRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2)
)

# Managed Objects groups

pdnRedundancyGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 1)
)
pdnRedundancyGeneralGroup.setObjects(
      *(("PDN-ENTITY-REDUNDANCY-MIB", "pdnEntityRedundancySelection"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnYCableSelection"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralNotificationEnable"))
)
if mibBuilder.loadTexts:
    pdnRedundancyGeneralGroup.setStatus("current")

pdnEntityRedundancyOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 2)
)
pdnEntityRedundancyOptGroup.setObjects(
      *(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunCommand"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunNotificationEnable"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEntityState"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
)
if mibBuilder.loadTexts:
    pdnEntityRedundancyOptGroup.setStatus("current")


# Notification objects

pdnRedunEventNoActiveModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 1)
)
pdnRedunEventNoActiveModule.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventNoActiveModule.setStatus(
        "current"
    )

pdnRedunEventHwIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 2)
)
pdnRedunEventHwIncompatible.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventHwIncompatible.setStatus(
        "current"
    )

pdnRedunEventStandbyAlarmOrReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 3)
)
pdnRedunEventStandbyAlarmOrReset.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventStandbyAlarmOrReset.setStatus(
        "current"
    )

pdnRedunEventFwIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 4)
)
pdnRedunEventFwIncompatible.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventFwIncompatible.setStatus(
        "current"
    )

pdnRedunEventCfgIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 5)
)
pdnRedunEventCfgIncompatible.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventCfgIncompatible.setStatus(
        "current"
    )

pdnRedunEventLinkDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 6)
)
pdnRedunEventLinkDefect.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventLinkDefect.setStatus(
        "current"
    )

pdnRedunEventHwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 7)
)
pdnRedunEventHwFailure.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventHwFailure.setStatus(
        "current"
    )

pdnRedunEventHwMissingHwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 8)
)
pdnRedunEventHwMissingHwFailure.setObjects(
    ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus")
)
if mibBuilder.loadTexts:
    pdnRedunEventHwMissingHwFailure.setStatus(
        "current"
    )


# Notifications groups

pdnEntityRedundancyEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 3)
)
pdnEntityRedundancyEventGroup.setObjects(
      *(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventNoActiveModule"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwIncompatible"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventStandbyAlarmOrReset"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventFwIncompatible"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventCfgIncompatible"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventLinkDefect"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwFailure"),
        ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwMissingHwFailure"))
)
if mibBuilder.loadTexts:
    pdnEntityRedundancyEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnEntityRedundancyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnEntityRedundancyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ENTITY-REDUNDANCY-MIB",
    **{"PdnRedunStates": PdnRedunStates,
       "PdnRedunCmd": PdnRedunCmd,
       "PdnRedunAlarmStatus": PdnRedunAlarmStatus,
       "PdnRedunGeneralAlarmStatus": PdnRedunGeneralAlarmStatus,
       "pdnEntRedunMIB": pdnEntRedunMIB,
       "pdnEntityRedundancyMIBObjects": pdnEntityRedundancyMIBObjects,
       "pdnEntityRedundancySelection": pdnEntityRedundancySelection,
       "pdnYCableSelection": pdnYCableSelection,
       "pdnRedunGeneralAlarmStatus": pdnRedunGeneralAlarmStatus,
       "pdnRedunCmdTable": pdnRedunCmdTable,
       "pdnRedunCmdEntry": pdnRedunCmdEntry,
       "pdnRedunCommand": pdnRedunCommand,
       "pdnRedunStatusTable": pdnRedunStatusTable,
       "pdnRedunStatusEntry": pdnRedunStatusEntry,
       "pdnRedunEntityState": pdnRedunEntityState,
       "pdnRedunAlarmStatus": pdnRedunAlarmStatus,
       "pdnRedunNotificationEnable": pdnRedunNotificationEnable,
       "pdnRedunGeneralNotificationEnable": pdnRedunGeneralNotificationEnable,
       "pdnEntityRedundancyNotifications": pdnEntityRedundancyNotifications,
       "pdnRedunNotificationsPrefix": pdnRedunNotificationsPrefix,
       "pdnRedunEventNoActiveModule": pdnRedunEventNoActiveModule,
       "pdnRedunEventHwIncompatible": pdnRedunEventHwIncompatible,
       "pdnRedunEventStandbyAlarmOrReset": pdnRedunEventStandbyAlarmOrReset,
       "pdnRedunEventFwIncompatible": pdnRedunEventFwIncompatible,
       "pdnRedunEventCfgIncompatible": pdnRedunEventCfgIncompatible,
       "pdnRedunEventLinkDefect": pdnRedunEventLinkDefect,
       "pdnRedunEventHwFailure": pdnRedunEventHwFailure,
       "pdnRedunEventHwMissingHwFailure": pdnRedunEventHwMissingHwFailure,
       "pdnEntityRedundancyConformance": pdnEntityRedundancyConformance,
       "pdnEntityRedundancyCompliances": pdnEntityRedundancyCompliances,
       "pdnEntityRedundancyCompliance": pdnEntityRedundancyCompliance,
       "pdnEntityRedundancyGroups": pdnEntityRedundancyGroups,
       "pdnRedundancyGeneralGroup": pdnRedundancyGeneralGroup,
       "pdnEntityRedundancyOptGroup": pdnEntityRedundancyOptGroup,
       "pdnEntityRedundancyEventGroup": pdnEntityRedundancyEventGroup}
)
