# SNMP MIB module (SALIX-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:36 2024
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

(atmfM4CellProtoHistIndex,
 atmfM4EquipHolderEntry,
 atmfM4PlugInUnitAvailStatus,
 atmfM4PlugInUnitEntry,
 atmfM4TcAdaptorEntry,
 atmfM4TrapAlarmSeverity) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4CellProtoHistIndex",
    "atmfM4EquipHolderEntry",
    "atmfM4PlugInUnitAvailStatus",
    "atmfM4PlugInUnitEntry",
    "atmfM4TcAdaptorEntry",
    "atmfM4TrapAlarmSeverity")

(TruthValue,) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "TruthValue")

(PhysicalIndex,
 entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalIndex,
 entPhysicalParentRelPos) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalIndex",
    "entPhysicalParentRelPos")

(InterfaceIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifOperStatus")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

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

salixSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixSystemMIBObjects_ObjectIdentity = ObjectIdentity
salixSystemMIBObjects = _SalixSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1)
)
_SalixSysLastLogErrorNumber_Type = Unsigned32
_SalixSysLastLogErrorNumber_Object = MibScalar
salixSysLastLogErrorNumber = _SalixSysLastLogErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 1),
    _SalixSysLastLogErrorNumber_Type()
)
salixSysLastLogErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysLastLogErrorNumber.setStatus("current")


class _SalixSysLastLogErrorMessage_Type(DisplayString):
    """Custom type salixSysLastLogErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SalixSysLastLogErrorMessage_Type.__name__ = "DisplayString"
_SalixSysLastLogErrorMessage_Object = MibScalar
salixSysLastLogErrorMessage = _SalixSysLastLogErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 2),
    _SalixSysLastLogErrorMessage_Type()
)
salixSysLastLogErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysLastLogErrorMessage.setStatus("current")
_SalixSysLastLogErrorOid_Type = ObjectIdentifier
_SalixSysLastLogErrorOid_Object = MibScalar
salixSysLastLogErrorOid = _SalixSysLastLogErrorOid_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 3),
    _SalixSysLastLogErrorOid_Type()
)
salixSysLastLogErrorOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysLastLogErrorOid.setStatus("current")
_SalixSysTemperature_Type = Integer32
_SalixSysTemperature_Object = MibScalar
salixSysTemperature = _SalixSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 4),
    _SalixSysTemperature_Type()
)
salixSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysTemperature.setStatus("deprecated")
_SalixSystemSync_ObjectIdentity = ObjectIdentity
salixSystemSync = _SalixSystemSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5)
)


class _SalixSysSyncTimingMode_Type(Integer32):
    """Custom type salixSysSyncTimingMode based on Integer32"""
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
        *(("external", 3),
          ("internal", 1),
          ("line", 2))
    )


_SalixSysSyncTimingMode_Type.__name__ = "Integer32"
_SalixSysSyncTimingMode_Object = MibScalar
salixSysSyncTimingMode = _SalixSysSyncTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 1),
    _SalixSysSyncTimingMode_Type()
)
salixSysSyncTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncTimingMode.setStatus("current")
_SalixSysSyncPrimaryRef_Type = InterfaceIndex
_SalixSysSyncPrimaryRef_Object = MibScalar
salixSysSyncPrimaryRef = _SalixSysSyncPrimaryRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 2),
    _SalixSysSyncPrimaryRef_Type()
)
salixSysSyncPrimaryRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncPrimaryRef.setStatus("current")
_SalixSysSyncSecondaryRef_Type = InterfaceIndex
_SalixSysSyncSecondaryRef_Object = MibScalar
salixSysSyncSecondaryRef = _SalixSysSyncSecondaryRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 3),
    _SalixSysSyncSecondaryRef_Type()
)
salixSysSyncSecondaryRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncSecondaryRef.setStatus("current")


class _SalixSysSyncRevertiveSwitch_Type(TruthValue):
    """Custom type salixSysSyncRevertiveSwitch based on TruthValue"""


_SalixSysSyncRevertiveSwitch_Object = MibScalar
salixSysSyncRevertiveSwitch = _SalixSysSyncRevertiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 4),
    _SalixSysSyncRevertiveSwitch_Type()
)
salixSysSyncRevertiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncRevertiveSwitch.setStatus("current")


class _SalixSysSyncClockMode_Type(Integer32):
    """Custom type salixSysSyncClockMode based on Integer32"""
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
        *(("fastStart", 4),
          ("freeRun", 1),
          ("holdover", 3),
          ("normal", 2))
    )


_SalixSysSyncClockMode_Type.__name__ = "Integer32"
_SalixSysSyncClockMode_Object = MibScalar
salixSysSyncClockMode = _SalixSysSyncClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 5),
    _SalixSysSyncClockMode_Type()
)
salixSysSyncClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncClockMode.setStatus("current")


class _SalixSysSyncConfiguredActiveRef_Type(Integer32):
    """Custom type salixSysSyncConfiguredActiveRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SalixSysSyncConfiguredActiveRef_Type.__name__ = "Integer32"
_SalixSysSyncConfiguredActiveRef_Object = MibScalar
salixSysSyncConfiguredActiveRef = _SalixSysSyncConfiguredActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 6),
    _SalixSysSyncConfiguredActiveRef_Type()
)
salixSysSyncConfiguredActiveRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncConfiguredActiveRef.setStatus("current")


class _SalixSysSyncAutoRefSwitch_Type(TruthValue):
    """Custom type salixSysSyncAutoRefSwitch based on TruthValue"""


_SalixSysSyncAutoRefSwitch_Object = MibScalar
salixSysSyncAutoRefSwitch = _SalixSysSyncAutoRefSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 7),
    _SalixSysSyncAutoRefSwitch_Type()
)
salixSysSyncAutoRefSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncAutoRefSwitch.setStatus("current")


class _SalixSysSyncFreeRunAlarm_Type(TruthValue):
    """Custom type salixSysSyncFreeRunAlarm based on TruthValue"""


_SalixSysSyncFreeRunAlarm_Object = MibScalar
salixSysSyncFreeRunAlarm = _SalixSysSyncFreeRunAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 8),
    _SalixSysSyncFreeRunAlarm_Type()
)
salixSysSyncFreeRunAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncFreeRunAlarm.setStatus("current")
_SalixSysSyncWorking_Type = PhysicalIndex
_SalixSysSyncWorking_Object = MibScalar
salixSysSyncWorking = _SalixSysSyncWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 9),
    _SalixSysSyncWorking_Type()
)
salixSysSyncWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysSyncWorking.setStatus("current")
_SalixSysSyncProtect_Type = PhysicalIndex
_SalixSysSyncProtect_Object = MibScalar
salixSysSyncProtect = _SalixSysSyncProtect_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 10),
    _SalixSysSyncProtect_Type()
)
salixSysSyncProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncProtect.setStatus("current")


class _SalixSysSyncPrimaryRefState_Type(Integer32):
    """Custom type salixSysSyncPrimaryRefState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequencyOffsetError", 3),
          ("lossOfSignalError", 2),
          ("unknown", 0),
          ("valid", 1))
    )


_SalixSysSyncPrimaryRefState_Type.__name__ = "Integer32"
_SalixSysSyncPrimaryRefState_Object = MibScalar
salixSysSyncPrimaryRefState = _SalixSysSyncPrimaryRefState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 11),
    _SalixSysSyncPrimaryRefState_Type()
)
salixSysSyncPrimaryRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncPrimaryRefState.setStatus("current")


class _SalixSysSyncSecondaryRefState_Type(Integer32):
    """Custom type salixSysSyncSecondaryRefState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequencyOffsetError", 3),
          ("lossOfSignalError", 2),
          ("unknown", 0),
          ("valid", 1))
    )


_SalixSysSyncSecondaryRefState_Type.__name__ = "Integer32"
_SalixSysSyncSecondaryRefState_Object = MibScalar
salixSysSyncSecondaryRefState = _SalixSysSyncSecondaryRefState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 12),
    _SalixSysSyncSecondaryRefState_Type()
)
salixSysSyncSecondaryRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncSecondaryRefState.setStatus("current")


class _SalixSysSyncCurrentActiveRef_Type(Integer32):
    """Custom type salixSysSyncCurrentActiveRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SalixSysSyncCurrentActiveRef_Type.__name__ = "Integer32"
_SalixSysSyncCurrentActiveRef_Object = MibScalar
salixSysSyncCurrentActiveRef = _SalixSysSyncCurrentActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 13),
    _SalixSysSyncCurrentActiveRef_Type()
)
salixSysSyncCurrentActiveRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncCurrentActiveRef.setStatus("current")


class _SalixSysSyncForcedState_Type(Integer32):
    """Custom type salixSysSyncForcedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoReferenceSwitchInhbit", 2),
          ("none", 0),
          ("revertiveSwitchInhibit", 1))
    )


_SalixSysSyncForcedState_Type.__name__ = "Integer32"
_SalixSysSyncForcedState_Object = MibScalar
salixSysSyncForcedState = _SalixSysSyncForcedState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 5, 14),
    _SalixSysSyncForcedState_Type()
)
salixSysSyncForcedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysSyncForcedState.setStatus("current")
_SalixSystemHsf_ObjectIdentity = ObjectIdentity
salixSystemHsf = _SalixSystemHsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 6)
)
_SalixSysHsfWorking_Type = PhysicalIndex
_SalixSysHsfWorking_Object = MibScalar
salixSysHsfWorking = _SalixSysHsfWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 6, 1),
    _SalixSysHsfWorking_Type()
)
salixSysHsfWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysHsfWorking.setStatus("current")
_SalixSysHsfProtect_Type = PhysicalIndex
_SalixSysHsfProtect_Object = MibScalar
salixSysHsfProtect = _SalixSysHsfProtect_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 6, 2),
    _SalixSysHsfProtect_Type()
)
salixSysHsfProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysHsfProtect.setStatus("current")
_SalixSystemRsc_ObjectIdentity = ObjectIdentity
salixSystemRsc = _SalixSystemRsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 7)
)
_SalixSysRscWorking_Type = PhysicalIndex
_SalixSysRscWorking_Object = MibScalar
salixSysRscWorking = _SalixSysRscWorking_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 7, 1),
    _SalixSysRscWorking_Type()
)
salixSysRscWorking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysRscWorking.setStatus("current")
_SalixSysRscProtect_Type = PhysicalIndex
_SalixSysRscProtect_Object = MibScalar
salixSysRscProtect = _SalixSysRscProtect_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 7, 2),
    _SalixSysRscProtect_Type()
)
salixSysRscProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSysRscProtect.setStatus("current")


class _SalixSysLoginMessage_Type(OctetString):
    """Custom type salixSysLoginMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 768),
    )


_SalixSysLoginMessage_Type.__name__ = "OctetString"
_SalixSysLoginMessage_Object = MibScalar
salixSysLoginMessage = _SalixSysLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 1, 8),
    _SalixSysLoginMessage_Type()
)
salixSysLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixSysLoginMessage.setStatus("current")
_SalixSystemMIBTraps_ObjectIdentity = ObjectIdentity
salixSystemMIBTraps = _SalixSystemMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2)
)
_SalixSystemMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixSystemMIBTrapPrefix = _SalixSystemMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0)
)
_SalixSystemMIBCompliance_ObjectIdentity = ObjectIdentity
salixSystemMIBCompliance = _SalixSystemMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 3)
)
_SalixSystemGroups_ObjectIdentity = ObjectIdentity
salixSystemGroups = _SalixSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 3, 1)
)
_SalixSystemCompliances_ObjectIdentity = ObjectIdentity
salixSystemCompliances = _SalixSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 3, 2)
)

# Managed Objects groups

salixSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 3, 1, 1)
)
salixSystemGroup.setObjects(
      *(("SALIX-SYSTEM-MIB", "salixSysLastLogErrorNumber"),
        ("SALIX-SYSTEM-MIB", "salixSysLastLogErrorMessage"),
        ("SALIX-SYSTEM-MIB", "salixSysLastLogErrorOid"))
)
if mibBuilder.loadTexts:
    salixSystemGroup.setStatus("current")


# Notification objects

salixSysSyncRefLineAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0, 1)
)
salixSysSyncRefLineAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("IF-MIB", "ifOperStatus"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixSysSyncRefLineAlarm.setStatus(
        "current"
    )

salixSysSyncInvalidRefLineAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0, 2)
)
salixSysSyncInvalidRefLineAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncPrimaryRef"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncSecondaryRef"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixSysSyncInvalidRefLineAlarm.setStatus(
        "current"
    )

salixSysSyncClockModeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0, 3)
)
salixSysSyncClockModeAlarm.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitAvailStatus"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncClockMode"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncWorking"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixSysSyncClockModeAlarm.setStatus(
        "current"
    )

salixSysSyncClockModeStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0, 4)
)
salixSysSyncClockModeStateChange.setObjects(
      *(("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitAvailStatus"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncClockMode"),
        ("SALIX-SYSTEM-MIB", "salixSysSyncWorking"))
)
if mibBuilder.loadTexts:
    salixSysSyncClockModeStateChange.setStatus(
        "current"
    )

salixSysFileSystemUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 2, 0, 5)
)
salixSysFileSystemUnavailable.setObjects(
    ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity")
)
if mibBuilder.loadTexts:
    salixSysFileSystemUnavailable.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

salixSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-SYSTEM-MIB",
    **{"salixSystemMIB": salixSystemMIB,
       "salixSystemMIBObjects": salixSystemMIBObjects,
       "salixSysLastLogErrorNumber": salixSysLastLogErrorNumber,
       "salixSysLastLogErrorMessage": salixSysLastLogErrorMessage,
       "salixSysLastLogErrorOid": salixSysLastLogErrorOid,
       "salixSysTemperature": salixSysTemperature,
       "salixSystemSync": salixSystemSync,
       "salixSysSyncTimingMode": salixSysSyncTimingMode,
       "salixSysSyncPrimaryRef": salixSysSyncPrimaryRef,
       "salixSysSyncSecondaryRef": salixSysSyncSecondaryRef,
       "salixSysSyncRevertiveSwitch": salixSysSyncRevertiveSwitch,
       "salixSysSyncClockMode": salixSysSyncClockMode,
       "salixSysSyncConfiguredActiveRef": salixSysSyncConfiguredActiveRef,
       "salixSysSyncAutoRefSwitch": salixSysSyncAutoRefSwitch,
       "salixSysSyncFreeRunAlarm": salixSysSyncFreeRunAlarm,
       "salixSysSyncWorking": salixSysSyncWorking,
       "salixSysSyncProtect": salixSysSyncProtect,
       "salixSysSyncPrimaryRefState": salixSysSyncPrimaryRefState,
       "salixSysSyncSecondaryRefState": salixSysSyncSecondaryRefState,
       "salixSysSyncCurrentActiveRef": salixSysSyncCurrentActiveRef,
       "salixSysSyncForcedState": salixSysSyncForcedState,
       "salixSystemHsf": salixSystemHsf,
       "salixSysHsfWorking": salixSysHsfWorking,
       "salixSysHsfProtect": salixSysHsfProtect,
       "salixSystemRsc": salixSystemRsc,
       "salixSysRscWorking": salixSysRscWorking,
       "salixSysRscProtect": salixSysRscProtect,
       "salixSysLoginMessage": salixSysLoginMessage,
       "salixSystemMIBTraps": salixSystemMIBTraps,
       "salixSystemMIBTrapPrefix": salixSystemMIBTrapPrefix,
       "salixSysSyncRefLineAlarm": salixSysSyncRefLineAlarm,
       "salixSysSyncInvalidRefLineAlarm": salixSysSyncInvalidRefLineAlarm,
       "salixSysSyncClockModeAlarm": salixSysSyncClockModeAlarm,
       "salixSysSyncClockModeStateChange": salixSysSyncClockModeStateChange,
       "salixSysFileSystemUnavailable": salixSysFileSystemUnavailable,
       "salixSystemMIBCompliance": salixSystemMIBCompliance,
       "salixSystemGroups": salixSystemGroups,
       "salixSystemGroup": salixSystemGroup,
       "salixSystemCompliances": salixSystemCompliances,
       "salixSystemCompliance": salixSystemCompliance}
)
