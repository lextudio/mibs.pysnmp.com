# SNMP MIB module (BAY-STACK-NES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-NES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:12 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackNesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 34)
)
bayStackNesMib.setRevisions(
        ("2014-08-22 00:00",
         "2009-05-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayStackNesNotifications_ObjectIdentity = ObjectIdentity
bayStackNesNotifications = _BayStackNesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0)
)
_BayStackNesObjects_ObjectIdentity = ObjectIdentity
bayStackNesObjects = _BayStackNesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1)
)
_BsnesScalars_ObjectIdentity = ObjectIdentity
bsnesScalars = _BsnesScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1)
)
_BsnesEnergySaverEnabled_Type = TruthValue
_BsnesEnergySaverEnabled_Object = MibScalar
bsnesEnergySaverEnabled = _BsnesEnergySaverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 1),
    _BsnesEnergySaverEnabled_Type()
)
bsnesEnergySaverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnesEnergySaverEnabled.setStatus("current")
_BsnesPoePowerSavingEnabled_Type = TruthValue
_BsnesPoePowerSavingEnabled_Object = MibScalar
bsnesPoePowerSavingEnabled = _BsnesPoePowerSavingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 2),
    _BsnesPoePowerSavingEnabled_Type()
)
bsnesPoePowerSavingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnesPoePowerSavingEnabled.setStatus("current")
_BsnesEfficiencyModeEnabled_Type = TruthValue
_BsnesEfficiencyModeEnabled_Object = MibScalar
bsnesEfficiencyModeEnabled = _BsnesEfficiencyModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 3),
    _BsnesEfficiencyModeEnabled_Type()
)
bsnesEfficiencyModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnesEfficiencyModeEnabled.setStatus("current")
_BsnesEnergySaverActive_Type = TruthValue
_BsnesEnergySaverActive_Object = MibScalar
bsnesEnergySaverActive = _BsnesEnergySaverActive_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 4),
    _BsnesEnergySaverActive_Type()
)
bsnesEnergySaverActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnesEnergySaverActive.setStatus("current")
_BsnesScheduleTable_Object = MibTable
bsnesScheduleTable = _BsnesScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2)
)
if mibBuilder.loadTexts:
    bsnesScheduleTable.setStatus("current")
_BsnesScheduleEntry_Object = MibTableRow
bsnesScheduleEntry = _BsnesScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1)
)
bsnesScheduleEntry.setIndexNames(
    (0, "BAY-STACK-NES-MIB", "bsnesScheduleDay"),
    (0, "BAY-STACK-NES-MIB", "bsnesScheduleHour"),
    (0, "BAY-STACK-NES-MIB", "bsnesScheduleMinute"),
)
if mibBuilder.loadTexts:
    bsnesScheduleEntry.setStatus("current")


class _BsnesScheduleDay_Type(Integer32):
    """Custom type bsnesScheduleDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_BsnesScheduleDay_Type.__name__ = "Integer32"
_BsnesScheduleDay_Object = MibTableColumn
bsnesScheduleDay = _BsnesScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 1),
    _BsnesScheduleDay_Type()
)
bsnesScheduleDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnesScheduleDay.setStatus("current")


class _BsnesScheduleHour_Type(Integer32):
    """Custom type bsnesScheduleHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_BsnesScheduleHour_Type.__name__ = "Integer32"
_BsnesScheduleHour_Object = MibTableColumn
bsnesScheduleHour = _BsnesScheduleHour_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 2),
    _BsnesScheduleHour_Type()
)
bsnesScheduleHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnesScheduleHour.setStatus("current")


class _BsnesScheduleMinute_Type(Integer32):
    """Custom type bsnesScheduleMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_BsnesScheduleMinute_Type.__name__ = "Integer32"
_BsnesScheduleMinute_Object = MibTableColumn
bsnesScheduleMinute = _BsnesScheduleMinute_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 3),
    _BsnesScheduleMinute_Type()
)
bsnesScheduleMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnesScheduleMinute.setStatus("current")


class _BsnesScheduleAction_Type(Integer32):
    """Custom type bsnesScheduleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_BsnesScheduleAction_Type.__name__ = "Integer32"
_BsnesScheduleAction_Object = MibTableColumn
bsnesScheduleAction = _BsnesScheduleAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 4),
    _BsnesScheduleAction_Type()
)
bsnesScheduleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnesScheduleAction.setStatus("current")
_BsnesScheduleRowStatus_Type = RowStatus
_BsnesScheduleRowStatus_Object = MibTableColumn
bsnesScheduleRowStatus = _BsnesScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 5),
    _BsnesScheduleRowStatus_Type()
)
bsnesScheduleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsnesScheduleRowStatus.setStatus("current")
_BsnesInterfaceTable_Object = MibTable
bsnesInterfaceTable = _BsnesInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3)
)
if mibBuilder.loadTexts:
    bsnesInterfaceTable.setStatus("current")
_BsnesInterfaceEntry_Object = MibTableRow
bsnesInterfaceEntry = _BsnesInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1)
)
bsnesInterfaceEntry.setIndexNames(
    (0, "BAY-STACK-NES-MIB", "bsnesInterfaceIndex"),
)
if mibBuilder.loadTexts:
    bsnesInterfaceEntry.setStatus("current")
_BsnesInterfaceIndex_Type = InterfaceIndex
_BsnesInterfaceIndex_Object = MibTableColumn
bsnesInterfaceIndex = _BsnesInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 1),
    _BsnesInterfaceIndex_Type()
)
bsnesInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnesInterfaceIndex.setStatus("current")
_BsnesInterfaceEnergySaverEnabled_Type = TruthValue
_BsnesInterfaceEnergySaverEnabled_Object = MibTableColumn
bsnesInterfaceEnergySaverEnabled = _BsnesInterfaceEnergySaverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 2),
    _BsnesInterfaceEnergySaverEnabled_Type()
)
bsnesInterfaceEnergySaverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsnesInterfaceEnergySaverEnabled.setStatus("current")


class _BsnesInterfaceEnergySaverPoeStatus_Type(Integer32):
    """Custom type bsnesInterfaceEnergySaverPoeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_BsnesInterfaceEnergySaverPoeStatus_Type.__name__ = "Integer32"
_BsnesInterfaceEnergySaverPoeStatus_Object = MibTableColumn
bsnesInterfaceEnergySaverPoeStatus = _BsnesInterfaceEnergySaverPoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 3),
    _BsnesInterfaceEnergySaverPoeStatus_Type()
)
bsnesInterfaceEnergySaverPoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnesInterfaceEnergySaverPoeStatus.setStatus("current")
_BsnesSavingsTable_Object = MibTable
bsnesSavingsTable = _BsnesSavingsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4)
)
if mibBuilder.loadTexts:
    bsnesSavingsTable.setStatus("current")
_BsnesSavingsEntry_Object = MibTableRow
bsnesSavingsEntry = _BsnesSavingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1)
)
bsnesSavingsEntry.setIndexNames(
    (0, "BAY-STACK-NES-MIB", "bsnesSavingsUnitIndex"),
)
if mibBuilder.loadTexts:
    bsnesSavingsEntry.setStatus("current")


class _BsnesSavingsUnitIndex_Type(Unsigned32):
    """Custom type bsnesSavingsUnitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BsnesSavingsUnitIndex_Type.__name__ = "Unsigned32"
_BsnesSavingsUnitIndex_Object = MibTableColumn
bsnesSavingsUnitIndex = _BsnesSavingsUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 1),
    _BsnesSavingsUnitIndex_Type()
)
bsnesSavingsUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsnesSavingsUnitIndex.setStatus("current")
_BsnesSavingsUnitSavings_Type = Unsigned32
_BsnesSavingsUnitSavings_Object = MibTableColumn
bsnesSavingsUnitSavings = _BsnesSavingsUnitSavings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 2),
    _BsnesSavingsUnitSavings_Type()
)
bsnesSavingsUnitSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnesSavingsUnitSavings.setStatus("current")
_BsnesSavingsPoeSavings_Type = Unsigned32
_BsnesSavingsPoeSavings_Object = MibTableColumn
bsnesSavingsPoeSavings = _BsnesSavingsPoeSavings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 3),
    _BsnesSavingsPoeSavings_Type()
)
bsnesSavingsPoeSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsnesSavingsPoeSavings.setStatus("current")
_BayStackNesNotificationObjects_ObjectIdentity = ObjectIdentity
bayStackNesNotificationObjects = _BayStackNesNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 2)
)

# Managed Objects groups


# Notification objects

bsnesGloballyEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 1)
)
if mibBuilder.loadTexts:
    bsnesGloballyEnabled.setStatus(
        "current"
    )

bsnesGloballyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 2)
)
if mibBuilder.loadTexts:
    bsnesGloballyDisabled.setStatus(
        "current"
    )

bsnesManuallyActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 3)
)
if mibBuilder.loadTexts:
    bsnesManuallyActivated.setStatus(
        "current"
    )

bsnesManuallyDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 4)
)
if mibBuilder.loadTexts:
    bsnesManuallyDeactivated.setStatus(
        "current"
    )

bsnesScheduleNotApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 5)
)
if mibBuilder.loadTexts:
    bsnesScheduleNotApplied.setStatus(
        "current"
    )

bsnesScheduleApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 6)
)
if mibBuilder.loadTexts:
    bsnesScheduleApplied.setStatus(
        "current"
    )

bsnesActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 7)
)
if mibBuilder.loadTexts:
    bsnesActivated.setStatus(
        "current"
    )

bsnesDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 8)
)
if mibBuilder.loadTexts:
    bsnesDeactivated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-NES-MIB",
    **{"bayStackNesMib": bayStackNesMib,
       "bayStackNesNotifications": bayStackNesNotifications,
       "bsnesGloballyEnabled": bsnesGloballyEnabled,
       "bsnesGloballyDisabled": bsnesGloballyDisabled,
       "bsnesManuallyActivated": bsnesManuallyActivated,
       "bsnesManuallyDeactivated": bsnesManuallyDeactivated,
       "bsnesScheduleNotApplied": bsnesScheduleNotApplied,
       "bsnesScheduleApplied": bsnesScheduleApplied,
       "bsnesActivated": bsnesActivated,
       "bsnesDeactivated": bsnesDeactivated,
       "bayStackNesObjects": bayStackNesObjects,
       "bsnesScalars": bsnesScalars,
       "bsnesEnergySaverEnabled": bsnesEnergySaverEnabled,
       "bsnesPoePowerSavingEnabled": bsnesPoePowerSavingEnabled,
       "bsnesEfficiencyModeEnabled": bsnesEfficiencyModeEnabled,
       "bsnesEnergySaverActive": bsnesEnergySaverActive,
       "bsnesScheduleTable": bsnesScheduleTable,
       "bsnesScheduleEntry": bsnesScheduleEntry,
       "bsnesScheduleDay": bsnesScheduleDay,
       "bsnesScheduleHour": bsnesScheduleHour,
       "bsnesScheduleMinute": bsnesScheduleMinute,
       "bsnesScheduleAction": bsnesScheduleAction,
       "bsnesScheduleRowStatus": bsnesScheduleRowStatus,
       "bsnesInterfaceTable": bsnesInterfaceTable,
       "bsnesInterfaceEntry": bsnesInterfaceEntry,
       "bsnesInterfaceIndex": bsnesInterfaceIndex,
       "bsnesInterfaceEnergySaverEnabled": bsnesInterfaceEnergySaverEnabled,
       "bsnesInterfaceEnergySaverPoeStatus": bsnesInterfaceEnergySaverPoeStatus,
       "bsnesSavingsTable": bsnesSavingsTable,
       "bsnesSavingsEntry": bsnesSavingsEntry,
       "bsnesSavingsUnitIndex": bsnesSavingsUnitIndex,
       "bsnesSavingsUnitSavings": bsnesSavingsUnitSavings,
       "bsnesSavingsPoeSavings": bsnesSavingsPoeSavings,
       "bayStackNesNotificationObjects": bayStackNesNotificationObjects}
)
