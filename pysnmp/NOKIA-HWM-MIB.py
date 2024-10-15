# SNMP MIB module (NOKIA-HWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-HWM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:39 2024
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

(ntcCommonModules,
 ntcHWMibs,
 ntcHWReqs) = mibBuilder.importSymbols(
    "NOKIA-COMMON-MIB-OID-REGISTRATION-MIB",
    "ntcCommonModules",
    "ntcHWMibs",
    "ntcHWReqs")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ntcHWModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 1)
)
ntcHWModule.setRevisions(
        ("1998-08-24 00:00",
         "1998-09-03 00:00",
         "1998-09-24 00:00",
         "1998-10-04 00:00",
         "1999-01-08 00:00",
         "1999-08-05 00:00",
         "1999-10-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcHWObjs_ObjectIdentity = ObjectIdentity
ntcHWObjs = _NtcHWObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1)
)
_NtcHWUnitTable_Object = MibTable
ntcHWUnitTable = _NtcHWUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntcHWUnitTable.setStatus("current")
_NtcHWUnitEntry_Object = MibTableRow
ntcHWUnitEntry = _NtcHWUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1)
)
ntcHWUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ntcHWUnitEntry.setStatus("current")


class _NtcHWAdminState_Type(Integer32):
    """Custom type ntcHWAdminState based on Integer32"""
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
        *(("inService", 1),
          ("inTest", 3),
          ("missing", 4),
          ("outOfService", 2))
    )


_NtcHWAdminState_Type.__name__ = "Integer32"
_NtcHWAdminState_Object = MibTableColumn
ntcHWAdminState = _NtcHWAdminState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 1),
    _NtcHWAdminState_Type()
)
ntcHWAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcHWAdminState.setStatus("current")


class _NtcHWOperState_Type(Integer32):
    """Custom type ntcHWOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_NtcHWOperState_Type.__name__ = "Integer32"
_NtcHWOperState_Object = MibTableColumn
ntcHWOperState = _NtcHWOperState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 2),
    _NtcHWOperState_Type()
)
ntcHWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWOperState.setStatus("current")


class _NtcHWAvailabilityStatus_Type(Integer32):
    """Custom type ntcHWAvailabilityStatus based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("applicationShutdown", 3),
          ("applicationStarting", 2),
          ("dormant", 10),
          ("inCharge", 1),
          ("platformStarting", 4),
          ("resetting", 5),
          ("separated", 6),
          ("standby", 9),
          ("testing", 8),
          ("unavailable", 11),
          ("unconfigured", 7))
    )


_NtcHWAvailabilityStatus_Type.__name__ = "Integer32"
_NtcHWAvailabilityStatus_Object = MibTableColumn
ntcHWAvailabilityStatus = _NtcHWAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 3),
    _NtcHWAvailabilityStatus_Type()
)
ntcHWAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWAvailabilityStatus.setStatus("current")


class _NtcHWRestart_Type(Integer32):
    """Custom type ntcHWRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detach", 3),
          ("hotRestart", 2),
          ("reset", 1))
    )


_NtcHWRestart_Type.__name__ = "Integer32"
_NtcHWRestart_Object = MibTableColumn
ntcHWRestart = _NtcHWRestart_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 4),
    _NtcHWRestart_Type()
)
ntcHWRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcHWRestart.setStatus("current")


class _NtcHWLedState_Type(Integer32):
    """Custom type ntcHWLedState based on Integer32"""
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
        *(("black", 3),
          ("green", 4),
          ("red", 1),
          ("yellow", 2))
    )


_NtcHWLedState_Type.__name__ = "Integer32"
_NtcHWLedState_Object = MibTableColumn
ntcHWLedState = _NtcHWLedState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 5),
    _NtcHWLedState_Type()
)
ntcHWLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWLedState.setStatus("current")
_NtcHWSerialNumber_Type = DisplayString
_NtcHWSerialNumber_Object = MibTableColumn
ntcHWSerialNumber = _NtcHWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 6),
    _NtcHWSerialNumber_Type()
)
ntcHWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWSerialNumber.setStatus("current")
_NtcHWProductionDate_Type = DisplayString
_NtcHWProductionDate_Object = MibTableColumn
ntcHWProductionDate = _NtcHWProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 7),
    _NtcHWProductionDate_Type()
)
ntcHWProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWProductionDate.setStatus("current")
_NtcHWUnitEntryChanged_Type = TimeStamp
_NtcHWUnitEntryChanged_Object = MibTableColumn
ntcHWUnitEntryChanged = _NtcHWUnitEntryChanged_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 8),
    _NtcHWUnitEntryChanged_Type()
)
ntcHWUnitEntryChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWUnitEntryChanged.setStatus("current")
_NtcHWSlotTable_Object = MibTable
ntcHWSlotTable = _NtcHWSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ntcHWSlotTable.setStatus("current")
_NtcHWSlotEntry_Object = MibTableRow
ntcHWSlotEntry = _NtcHWSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2, 1)
)
ntcHWSlotEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ntcHWSlotEntry.setStatus("current")
_NtcHWDesiredUnitType_Type = AutonomousType
_NtcHWDesiredUnitType_Object = MibTableColumn
ntcHWDesiredUnitType = _NtcHWDesiredUnitType_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2, 1, 2),
    _NtcHWDesiredUnitType_Type()
)
ntcHWDesiredUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcHWDesiredUnitType.setStatus("current")
_NtcHWLastChangedTime_Type = TimeStamp
_NtcHWLastChangedTime_Object = MibScalar
ntcHWLastChangedTime = _NtcHWLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 3),
    _NtcHWLastChangedTime_Type()
)
ntcHWLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcHWLastChangedTime.setStatus("current")
_NtcHWLoadInventoryContainer_Type = Integer32
_NtcHWLoadInventoryContainer_Object = MibScalar
ntcHWLoadInventoryContainer = _NtcHWLoadInventoryContainer_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 4),
    _NtcHWLoadInventoryContainer_Type()
)
ntcHWLoadInventoryContainer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcHWLoadInventoryContainer.setStatus("current")
_NtcHWEvents_ObjectIdentity = ObjectIdentity
ntcHWEvents = _NtcHWEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 2, 0)
)
_NtcHWGroups_ObjectIdentity = ObjectIdentity
ntcHWGroups = _NtcHWGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 1)
)
_NtcHWCompliances_ObjectIdentity = ObjectIdentity
ntcHWCompliances = _NtcHWCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 2)
)

# Managed Objects groups

ntcHWUnits = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 1, 1)
)
ntcHWUnits.setObjects(
      *(("NOKIA-HWM-MIB", "ntcHWAdminState"),
        ("NOKIA-HWM-MIB", "ntcHWOperState"),
        ("NOKIA-HWM-MIB", "ntcHWAvailabilityStatus"),
        ("NOKIA-HWM-MIB", "ntcHWRestart"),
        ("NOKIA-HWM-MIB", "ntcHWLedState"),
        ("NOKIA-HWM-MIB", "ntcHWSerialNumber"),
        ("NOKIA-HWM-MIB", "ntcHWProductionDate"),
        ("NOKIA-HWM-MIB", "ntcHWUnitEntryChanged"))
)
if mibBuilder.loadTexts:
    ntcHWUnits.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcHWCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntcHWCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-HWM-MIB",
    **{"ntcHWModule": ntcHWModule,
       "ntcHWObjs": ntcHWObjs,
       "ntcHWUnitTable": ntcHWUnitTable,
       "ntcHWUnitEntry": ntcHWUnitEntry,
       "ntcHWAdminState": ntcHWAdminState,
       "ntcHWOperState": ntcHWOperState,
       "ntcHWAvailabilityStatus": ntcHWAvailabilityStatus,
       "ntcHWRestart": ntcHWRestart,
       "ntcHWLedState": ntcHWLedState,
       "ntcHWSerialNumber": ntcHWSerialNumber,
       "ntcHWProductionDate": ntcHWProductionDate,
       "ntcHWUnitEntryChanged": ntcHWUnitEntryChanged,
       "ntcHWSlotTable": ntcHWSlotTable,
       "ntcHWSlotEntry": ntcHWSlotEntry,
       "ntcHWDesiredUnitType": ntcHWDesiredUnitType,
       "ntcHWLastChangedTime": ntcHWLastChangedTime,
       "ntcHWLoadInventoryContainer": ntcHWLoadInventoryContainer,
       "ntcHWEvents": ntcHWEvents,
       "ntcHWGroups": ntcHWGroups,
       "ntcHWUnits": ntcHWUnits,
       "ntcHWCompliances": ntcHWCompliances,
       "ntcHWCompliance": ntcHWCompliance}
)
