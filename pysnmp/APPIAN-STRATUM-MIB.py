# SNMP MIB module (APPIAN-STRATUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-STRATUM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:44 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcNodeId,
 AcOpStatus,
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcNodeId",
    "AcOpStatus",
    "acOsap")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acStratum = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9)
)
acStratum.setRevisions(
        ("1900-08-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcStratumTraps_ObjectIdentity = ObjectIdentity
acStratumTraps = _AcStratumTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0)
)
_AcStratumTable_Object = MibTable
acStratumTable = _AcStratumTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1)
)
if mibBuilder.loadTexts:
    acStratumTable.setStatus("current")
_AcStratumEntry_Object = MibTableRow
acStratumEntry = _AcStratumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1)
)
acStratumEntry.setIndexNames(
    (0, "APPIAN-STRATUM-MIB", "acStratumNodeId"),
)
if mibBuilder.loadTexts:
    acStratumEntry.setStatus("current")
_AcStratumNodeId_Type = AcNodeId
_AcStratumNodeId_Object = MibTableColumn
acStratumNodeId = _AcStratumNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 1),
    _AcStratumNodeId_Type()
)
acStratumNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acStratumNodeId.setStatus("current")


class _AcStratumClockSource_Type(Integer32):
    """Custom type acStratumClockSource based on Integer32"""
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
        *(("bits", 2),
          ("internal", 1),
          ("line", 3))
    )


_AcStratumClockSource_Type.__name__ = "Integer32"
_AcStratumClockSource_Object = MibTableColumn
acStratumClockSource = _AcStratumClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 2),
    _AcStratumClockSource_Type()
)
acStratumClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumClockSource.setStatus("current")
_AcStratumOpStatusModuleA_Type = AcOpStatus
_AcStratumOpStatusModuleA_Object = MibTableColumn
acStratumOpStatusModuleA = _AcStratumOpStatusModuleA_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 3),
    _AcStratumOpStatusModuleA_Type()
)
acStratumOpStatusModuleA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumOpStatusModuleA.setStatus("current")
_AcStratumOpStatusModuleB_Type = AcOpStatus
_AcStratumOpStatusModuleB_Object = MibTableColumn
acStratumOpStatusModuleB = _AcStratumOpStatusModuleB_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 4),
    _AcStratumOpStatusModuleB_Type()
)
acStratumOpStatusModuleB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumOpStatusModuleB.setStatus("current")


class _AcStratumAlarmStatusModuleA_Type(Integer32):
    """Custom type acStratumAlarmStatusModuleA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcStratumAlarmStatusModuleA_Type.__name__ = "Integer32"
_AcStratumAlarmStatusModuleA_Object = MibTableColumn
acStratumAlarmStatusModuleA = _AcStratumAlarmStatusModuleA_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 5),
    _AcStratumAlarmStatusModuleA_Type()
)
acStratumAlarmStatusModuleA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumAlarmStatusModuleA.setStatus("current")


class _AcStratumAlarmStatusModuleB_Type(Integer32):
    """Custom type acStratumAlarmStatusModuleB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcStratumAlarmStatusModuleB_Type.__name__ = "Integer32"
_AcStratumAlarmStatusModuleB_Object = MibTableColumn
acStratumAlarmStatusModuleB = _AcStratumAlarmStatusModuleB_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 6),
    _AcStratumAlarmStatusModuleB_Type()
)
acStratumAlarmStatusModuleB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumAlarmStatusModuleB.setStatus("current")


class _AcStratumCurrentClockSourceModuleA_Type(Integer32):
    """Custom type acStratumCurrentClockSourceModuleA based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits-a", 2),
          ("bits-b", 3),
          ("holdover", 8),
          ("internal", 9),
          ("line-slot1-port1", 4),
          ("line-slot1-port2", 5),
          ("line-slot2-port1", 6),
          ("line-slot2-port2", 7),
          ("none", 1),
          ("unknown", 0))
    )


_AcStratumCurrentClockSourceModuleA_Type.__name__ = "Integer32"
_AcStratumCurrentClockSourceModuleA_Object = MibTableColumn
acStratumCurrentClockSourceModuleA = _AcStratumCurrentClockSourceModuleA_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 7),
    _AcStratumCurrentClockSourceModuleA_Type()
)
acStratumCurrentClockSourceModuleA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumCurrentClockSourceModuleA.setStatus("current")


class _AcStratumCurrentClockSourceModuleB_Type(Integer32):
    """Custom type acStratumCurrentClockSourceModuleB based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits-a", 2),
          ("bits-b", 3),
          ("holdover", 8),
          ("internal", 9),
          ("line-slot1-port1", 4),
          ("line-slot1-port2", 5),
          ("line-slot2-port1", 6),
          ("line-slot2-port2", 7),
          ("none", 1),
          ("unknown", 0))
    )


_AcStratumCurrentClockSourceModuleB_Type.__name__ = "Integer32"
_AcStratumCurrentClockSourceModuleB_Object = MibTableColumn
acStratumCurrentClockSourceModuleB = _AcStratumCurrentClockSourceModuleB_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 8),
    _AcStratumCurrentClockSourceModuleB_Type()
)
acStratumCurrentClockSourceModuleB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumCurrentClockSourceModuleB.setStatus("current")


class _AcStratumLockoutReference_Type(Integer32):
    """Custom type acStratumLockoutReference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcStratumLockoutReference_Type.__name__ = "Integer32"
_AcStratumLockoutReference_Object = MibTableColumn
acStratumLockoutReference = _AcStratumLockoutReference_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 9),
    _AcStratumLockoutReference_Type()
)
acStratumLockoutReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumLockoutReference.setStatus("current")


class _AcStratumManualSwitch_Type(Integer32):
    """Custom type acStratumManualSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bits-a", 1),
          ("bits-b", 2),
          ("line-slot1", 3),
          ("line-slot2", 4),
          ("none", 0))
    )


_AcStratumManualSwitch_Type.__name__ = "Integer32"
_AcStratumManualSwitch_Object = MibTableColumn
acStratumManualSwitch = _AcStratumManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 10),
    _AcStratumManualSwitch_Type()
)
acStratumManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumManualSwitch.setStatus("current")


class _AcStratumForcedSwitch_Type(Integer32):
    """Custom type acStratumForcedSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bits-a", 1),
          ("bits-b", 2),
          ("line-slot1", 3),
          ("line-slot2", 4),
          ("none", 0))
    )


_AcStratumForcedSwitch_Type.__name__ = "Integer32"
_AcStratumForcedSwitch_Object = MibTableColumn
acStratumForcedSwitch = _AcStratumForcedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 11),
    _AcStratumForcedSwitch_Type()
)
acStratumForcedSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumForcedSwitch.setStatus("current")


class _AcStratumRevertiveRefSwitchEnabled_Type(TruthValue):
    """Custom type acStratumRevertiveRefSwitchEnabled based on TruthValue"""


_AcStratumRevertiveRefSwitchEnabled_Object = MibTableColumn
acStratumRevertiveRefSwitchEnabled = _AcStratumRevertiveRefSwitchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 12),
    _AcStratumRevertiveRefSwitchEnabled_Type()
)
acStratumRevertiveRefSwitchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumRevertiveRefSwitchEnabled.setStatus("current")


class _AcStratumClearAlarms_Type(TruthValue):
    """Custom type acStratumClearAlarms based on TruthValue"""


_AcStratumClearAlarms_Object = MibTableColumn
acStratumClearAlarms = _AcStratumClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 13),
    _AcStratumClearAlarms_Type()
)
acStratumClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumClearAlarms.setStatus("current")


class _AcStratumLineTimingPortSlot1_Type(Integer32):
    """Custom type acStratumLineTimingPortSlot1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcStratumLineTimingPortSlot1_Type.__name__ = "Integer32"
_AcStratumLineTimingPortSlot1_Object = MibTableColumn
acStratumLineTimingPortSlot1 = _AcStratumLineTimingPortSlot1_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 14),
    _AcStratumLineTimingPortSlot1_Type()
)
acStratumLineTimingPortSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumLineTimingPortSlot1.setStatus("current")


class _AcStratumLineTimingPortSlot2_Type(Integer32):
    """Custom type acStratumLineTimingPortSlot2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcStratumLineTimingPortSlot2_Type.__name__ = "Integer32"
_AcStratumLineTimingPortSlot2_Object = MibTableColumn
acStratumLineTimingPortSlot2 = _AcStratumLineTimingPortSlot2_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 15),
    _AcStratumLineTimingPortSlot2_Type()
)
acStratumLineTimingPortSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumLineTimingPortSlot2.setStatus("current")


class _AcStratumBITSFramingType_Type(Integer32):
    """Custom type acStratumBITSFramingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esf", 1))
    )


_AcStratumBITSFramingType_Type.__name__ = "Integer32"
_AcStratumBITSFramingType_Object = MibTableColumn
acStratumBITSFramingType = _AcStratumBITSFramingType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 16),
    _AcStratumBITSFramingType_Type()
)
acStratumBITSFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStratumBITSFramingType.setStatus("current")


class _AcStratumCurrentClockSourceSystem_Type(Integer32):
    """Custom type acStratumCurrentClockSourceSystem based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bits-a", 1),
          ("bits-b", 2),
          ("holdover-clock-a", 7),
          ("holdover-clock-b", 8),
          ("internal-clock-a", 9),
          ("internal-clock-b", 10),
          ("internal-sonet-slot1", 11),
          ("internal-sonet-slot2", 12),
          ("line-slot1-port1", 3),
          ("line-slot1-port2", 4),
          ("line-slot2-port1", 5),
          ("line-slot2-port2", 6),
          ("unknown", 0))
    )


_AcStratumCurrentClockSourceSystem_Type.__name__ = "Integer32"
_AcStratumCurrentClockSourceSystem_Object = MibTableColumn
acStratumCurrentClockSourceSystem = _AcStratumCurrentClockSourceSystem_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 1, 1, 17),
    _AcStratumCurrentClockSourceSystem_Type()
)
acStratumCurrentClockSourceSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStratumCurrentClockSourceSystem.setStatus("current")

# Managed Objects groups


# Notification objects

acStratumFailedModuleATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 1)
)
acStratumFailedModuleATrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumFailedModuleATrap.setStatus(
        "current"
    )

acStratumFailedModuleBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 2)
)
acStratumFailedModuleBTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumFailedModuleBTrap.setStatus(
        "current"
    )

acStratumClockFailureModuleATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 3)
)
acStratumClockFailureModuleATrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"),
        ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleA"))
)
if mibBuilder.loadTexts:
    acStratumClockFailureModuleATrap.setStatus(
        "current"
    )

acStratumClockFailureModuleBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 4)
)
acStratumClockFailureModuleBTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"),
        ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleB"))
)
if mibBuilder.loadTexts:
    acStratumClockFailureModuleBTrap.setStatus(
        "current"
    )

acStratumRemovalModuleATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 5)
)
acStratumRemovalModuleATrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumRemovalModuleATrap.setStatus(
        "current"
    )

acStratumRemovalModuleBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 6)
)
acStratumRemovalModuleBTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumRemovalModuleBTrap.setStatus(
        "current"
    )

acStratumInsertedModuleATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 7)
)
acStratumInsertedModuleATrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumInsertedModuleATrap.setStatus(
        "current"
    )

acStratumInsertedModuleBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 8)
)
acStratumInsertedModuleBTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"))
)
if mibBuilder.loadTexts:
    acStratumInsertedModuleBTrap.setStatus(
        "current"
    )

acStratumClockModuleAOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 9)
)
acStratumClockModuleAOk.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"),
        ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleA"))
)
if mibBuilder.loadTexts:
    acStratumClockModuleAOk.setStatus(
        "current"
    )

acStratumClockModuleBOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 10)
)
acStratumClockModuleBOk.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"),
        ("APPIAN-STRATUM-MIB", "acStratumAlarmStatusModuleB"))
)
if mibBuilder.loadTexts:
    acStratumClockModuleBOk.setStatus(
        "current"
    )

acStratumSystemClockSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 9, 0, 11)
)
acStratumSystemClockSourceChange.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-STRATUM-MIB", "acStratumNodeId"),
        ("APPIAN-STRATUM-MIB", "acStratumCurrentClockSourceSystem"))
)
if mibBuilder.loadTexts:
    acStratumSystemClockSourceChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-STRATUM-MIB",
    **{"acStratum": acStratum,
       "acStratumTraps": acStratumTraps,
       "acStratumFailedModuleATrap": acStratumFailedModuleATrap,
       "acStratumFailedModuleBTrap": acStratumFailedModuleBTrap,
       "acStratumClockFailureModuleATrap": acStratumClockFailureModuleATrap,
       "acStratumClockFailureModuleBTrap": acStratumClockFailureModuleBTrap,
       "acStratumRemovalModuleATrap": acStratumRemovalModuleATrap,
       "acStratumRemovalModuleBTrap": acStratumRemovalModuleBTrap,
       "acStratumInsertedModuleATrap": acStratumInsertedModuleATrap,
       "acStratumInsertedModuleBTrap": acStratumInsertedModuleBTrap,
       "acStratumClockModuleAOk": acStratumClockModuleAOk,
       "acStratumClockModuleBOk": acStratumClockModuleBOk,
       "acStratumSystemClockSourceChange": acStratumSystemClockSourceChange,
       "acStratumTable": acStratumTable,
       "acStratumEntry": acStratumEntry,
       "acStratumNodeId": acStratumNodeId,
       "acStratumClockSource": acStratumClockSource,
       "acStratumOpStatusModuleA": acStratumOpStatusModuleA,
       "acStratumOpStatusModuleB": acStratumOpStatusModuleB,
       "acStratumAlarmStatusModuleA": acStratumAlarmStatusModuleA,
       "acStratumAlarmStatusModuleB": acStratumAlarmStatusModuleB,
       "acStratumCurrentClockSourceModuleA": acStratumCurrentClockSourceModuleA,
       "acStratumCurrentClockSourceModuleB": acStratumCurrentClockSourceModuleB,
       "acStratumLockoutReference": acStratumLockoutReference,
       "acStratumManualSwitch": acStratumManualSwitch,
       "acStratumForcedSwitch": acStratumForcedSwitch,
       "acStratumRevertiveRefSwitchEnabled": acStratumRevertiveRefSwitchEnabled,
       "acStratumClearAlarms": acStratumClearAlarms,
       "acStratumLineTimingPortSlot1": acStratumLineTimingPortSlot1,
       "acStratumLineTimingPortSlot2": acStratumLineTimingPortSlot2,
       "acStratumBITSFramingType": acStratumBITSFramingType,
       "acStratumCurrentClockSourceSystem": acStratumCurrentClockSourceSystem}
)
