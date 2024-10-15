# SNMP MIB module (STN-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:01 2024
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

(stnNotification,
 stnSystems) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification",
    "stnSystems")

(StnBatteryStatus,
 StnEngineAdminStatus,
 StnEngineOperStatus,
 StnFlashStatus,
 StnHardwareModuleType,
 StnHardwareSubModuleType,
 StnLedStatus,
 StnModuleAdminStatus,
 StnModuleOperStatus,
 StnPowerStatus,
 StnResourceStatus) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "StnBatteryStatus",
    "StnEngineAdminStatus",
    "StnEngineOperStatus",
    "StnFlashStatus",
    "StnHardwareModuleType",
    "StnHardwareSubModuleType",
    "StnLedStatus",
    "StnModuleAdminStatus",
    "StnModuleOperStatus",
    "StnPowerStatus",
    "StnResourceStatus")


# MODULE-IDENTITY

stnChassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnChassisObjects_ObjectIdentity = ObjectIdentity
stnChassisObjects = _StnChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1)
)
_StnChassisVars_ObjectIdentity = ObjectIdentity
stnChassisVars = _StnChassisVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 1)
)


class _StnChassisSysType_Type(Integer32):
    """Custom type stnChassisSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stn5000", 2))
    )


_StnChassisSysType_Type.__name__ = "Integer32"
_StnChassisSysType_Object = MibScalar
stnChassisSysType = _StnChassisSysType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 1, 1),
    _StnChassisSysType_Type()
)
stnChassisSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnChassisSysType.setStatus("current")
_StnChassisSysDescr_Type = DisplayString
_StnChassisSysDescr_Object = MibScalar
stnChassisSysDescr = _StnChassisSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 1, 2),
    _StnChassisSysDescr_Type()
)
stnChassisSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnChassisSysDescr.setStatus("current")
_StnChassisId_Type = DisplayString
_StnChassisId_Object = MibScalar
stnChassisId = _StnChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 1, 3),
    _StnChassisId_Type()
)
stnChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnChassisId.setStatus("current")
_StnModules_ObjectIdentity = ObjectIdentity
stnModules = _StnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2)
)
_StnSlotTable_Object = MibTable
stnSlotTable = _StnSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnSlotTable.setStatus("current")
_StnSlotEntry_Object = MibTableRow
stnSlotEntry = _StnSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1)
)
stnSlotEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnSlotIndex"),
)
if mibBuilder.loadTexts:
    stnSlotEntry.setStatus("current")
_StnSlotIndex_Type = Integer32
_StnSlotIndex_Object = MibTableColumn
stnSlotIndex = _StnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 1),
    _StnSlotIndex_Type()
)
stnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSlotIndex.setStatus("current")
_StnModuleType_Type = StnHardwareModuleType
_StnModuleType_Object = MibTableColumn
stnModuleType = _StnModuleType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 2),
    _StnModuleType_Type()
)
stnModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModuleType.setStatus("current")
_StnModulePeer_Type = Integer32
_StnModulePeer_Object = MibTableColumn
stnModulePeer = _StnModulePeer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 3),
    _StnModulePeer_Type()
)
stnModulePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModulePeer.setStatus("current")
_StnModuleAdminStatus_Type = StnModuleAdminStatus
_StnModuleAdminStatus_Object = MibTableColumn
stnModuleAdminStatus = _StnModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 4),
    _StnModuleAdminStatus_Type()
)
stnModuleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModuleAdminStatus.setStatus("current")
_StnModuleOperStatus_Type = StnModuleOperStatus
_StnModuleOperStatus_Object = MibTableColumn
stnModuleOperStatus = _StnModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 5),
    _StnModuleOperStatus_Type()
)
stnModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModuleOperStatus.setStatus("current")
_StnModuleDescr_Type = DisplayString
_StnModuleDescr_Object = MibTableColumn
stnModuleDescr = _StnModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 6),
    _StnModuleDescr_Type()
)
stnModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModuleDescr.setStatus("current")
_StnModuleLed_Type = StnLedStatus
_StnModuleLed_Object = MibTableColumn
stnModuleLed = _StnModuleLed_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 7),
    _StnModuleLed_Type()
)
stnModuleLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnModuleLed.setStatus("current")
_StnSubModules_Type = Integer32
_StnSubModules_Object = MibTableColumn
stnSubModules = _StnSubModules_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 1, 1, 8),
    _StnSubModules_Type()
)
stnSubModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModules.setStatus("current")
_StnSubModuleTable_Object = MibTable
stnSubModuleTable = _StnSubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    stnSubModuleTable.setStatus("current")
_StnSubModuleEntry_Object = MibTableRow
stnSubModuleEntry = _StnSubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1)
)
stnSubModuleEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnSubModuleSlot"),
    (0, "STN-CHASSIS-MIB", "stnSubModuleIndex"),
)
if mibBuilder.loadTexts:
    stnSubModuleEntry.setStatus("current")
_StnSubModuleSlot_Type = Integer32
_StnSubModuleSlot_Object = MibTableColumn
stnSubModuleSlot = _StnSubModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 1),
    _StnSubModuleSlot_Type()
)
stnSubModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleSlot.setStatus("current")
_StnSubModuleIndex_Type = Integer32
_StnSubModuleIndex_Object = MibTableColumn
stnSubModuleIndex = _StnSubModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 2),
    _StnSubModuleIndex_Type()
)
stnSubModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleIndex.setStatus("current")
_StnSubModuleType_Type = StnHardwareSubModuleType
_StnSubModuleType_Object = MibTableColumn
stnSubModuleType = _StnSubModuleType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 3),
    _StnSubModuleType_Type()
)
stnSubModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleType.setStatus("current")
_StnSubModulePeer_Type = Integer32
_StnSubModulePeer_Object = MibTableColumn
stnSubModulePeer = _StnSubModulePeer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 4),
    _StnSubModulePeer_Type()
)
stnSubModulePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModulePeer.setStatus("current")
_StnSubModuleAdminStatus_Type = StnModuleAdminStatus
_StnSubModuleAdminStatus_Object = MibTableColumn
stnSubModuleAdminStatus = _StnSubModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 5),
    _StnSubModuleAdminStatus_Type()
)
stnSubModuleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleAdminStatus.setStatus("current")
_StnSubModuleOperStatus_Type = StnModuleOperStatus
_StnSubModuleOperStatus_Object = MibTableColumn
stnSubModuleOperStatus = _StnSubModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 6),
    _StnSubModuleOperStatus_Type()
)
stnSubModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleOperStatus.setStatus("current")
_StnSubModuleDescr_Type = DisplayString
_StnSubModuleDescr_Object = MibTableColumn
stnSubModuleDescr = _StnSubModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 2, 1, 7),
    _StnSubModuleDescr_Type()
)
stnSubModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSubModuleDescr.setStatus("current")
_StnEngineTable_Object = MibTable
stnEngineTable = _StnEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    stnEngineTable.setStatus("current")
_StnEngineEntry_Object = MibTableRow
stnEngineEntry = _StnEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1)
)
stnEngineEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnEngineIndex"),
)
if mibBuilder.loadTexts:
    stnEngineEntry.setStatus("current")
_StnEngineIndex_Type = Integer32
_StnEngineIndex_Object = MibTableColumn
stnEngineIndex = _StnEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 1),
    _StnEngineIndex_Type()
)
stnEngineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineIndex.setStatus("current")
_StnEngineSlot_Type = Integer32
_StnEngineSlot_Object = MibTableColumn
stnEngineSlot = _StnEngineSlot_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 2),
    _StnEngineSlot_Type()
)
stnEngineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineSlot.setStatus("current")
_StnEngineCpu_Type = Integer32
_StnEngineCpu_Object = MibTableColumn
stnEngineCpu = _StnEngineCpu_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 3),
    _StnEngineCpu_Type()
)
stnEngineCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineCpu.setStatus("current")


class _StnEngineType_Type(Integer32):
    """Custom type stnEngineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ecf", 4),
          ("ecf2", 5),
          ("rpe", 3),
          ("swc", 2),
          ("unknown", 1))
    )


_StnEngineType_Type.__name__ = "Integer32"
_StnEngineType_Object = MibTableColumn
stnEngineType = _StnEngineType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 4),
    _StnEngineType_Type()
)
stnEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineType.setStatus("current")
_StnEnginePeer_Type = Integer32
_StnEnginePeer_Object = MibTableColumn
stnEnginePeer = _StnEnginePeer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 5),
    _StnEnginePeer_Type()
)
stnEnginePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEnginePeer.setStatus("current")
_StnEngineAdminStatus_Type = StnEngineAdminStatus
_StnEngineAdminStatus_Object = MibTableColumn
stnEngineAdminStatus = _StnEngineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 6),
    _StnEngineAdminStatus_Type()
)
stnEngineAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineAdminStatus.setStatus("current")
_StnEngineOperStatus_Type = StnEngineOperStatus
_StnEngineOperStatus_Object = MibTableColumn
stnEngineOperStatus = _StnEngineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 7),
    _StnEngineOperStatus_Type()
)
stnEngineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineOperStatus.setStatus("current")
_StnEngineDescr_Type = DisplayString
_StnEngineDescr_Object = MibTableColumn
stnEngineDescr = _StnEngineDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 2, 3, 1, 8),
    _StnEngineDescr_Type()
)
stnEngineDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnEngineDescr.setStatus("current")
_StnLeds_ObjectIdentity = ObjectIdentity
stnLeds = _StnLeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3)
)
_StnLedFanTray_Type = StnLedStatus
_StnLedFanTray_Object = MibScalar
stnLedFanTray = _StnLedFanTray_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 1),
    _StnLedFanTray_Type()
)
stnLedFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLedFanTray.setStatus("current")
_StnLedPowerA_Type = StnLedStatus
_StnLedPowerA_Object = MibScalar
stnLedPowerA = _StnLedPowerA_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 2),
    _StnLedPowerA_Type()
)
stnLedPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLedPowerA.setStatus("current")
_StnLedPowerB_Type = StnLedStatus
_StnLedPowerB_Object = MibScalar
stnLedPowerB = _StnLedPowerB_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 3),
    _StnLedPowerB_Type()
)
stnLedPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLedPowerB.setStatus("current")
_StnLedAlarm_Type = StnLedStatus
_StnLedAlarm_Object = MibScalar
stnLedAlarm = _StnLedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 4),
    _StnLedAlarm_Type()
)
stnLedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnLedAlarm.setStatus("current")
_StnFanTrayLedTable_Object = MibTable
stnFanTrayLedTable = _StnFanTrayLedTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    stnFanTrayLedTable.setStatus("current")
_StnFanTrayLedEntry_Object = MibTableRow
stnFanTrayLedEntry = _StnFanTrayLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 5, 1)
)
stnFanTrayLedEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnFanTrayLedIndex"),
)
if mibBuilder.loadTexts:
    stnFanTrayLedEntry.setStatus("current")
_StnFanTrayLedIndex_Type = Integer32
_StnFanTrayLedIndex_Object = MibTableColumn
stnFanTrayLedIndex = _StnFanTrayLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 5, 1, 1),
    _StnFanTrayLedIndex_Type()
)
stnFanTrayLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnFanTrayLedIndex.setStatus("current")
_StnFanTrayLedSlotIndex_Type = Integer32
_StnFanTrayLedSlotIndex_Object = MibTableColumn
stnFanTrayLedSlotIndex = _StnFanTrayLedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 5, 1, 2),
    _StnFanTrayLedSlotIndex_Type()
)
stnFanTrayLedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnFanTrayLedSlotIndex.setStatus("current")
_StnFanTrayLedStatus_Type = StnLedStatus
_StnFanTrayLedStatus_Object = MibTableColumn
stnFanTrayLedStatus = _StnFanTrayLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 5, 1, 3),
    _StnFanTrayLedStatus_Type()
)
stnFanTrayLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnFanTrayLedStatus.setStatus("current")
_StnPortLedTable_Object = MibTable
stnPortLedTable = _StnPortLedTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    stnPortLedTable.setStatus("current")
_StnPortLedEntry_Object = MibTableRow
stnPortLedEntry = _StnPortLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1)
)
stnPortLedEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnPortLedSlotIndex"),
    (0, "STN-CHASSIS-MIB", "stnPortLedPortIndex"),
    (0, "STN-CHASSIS-MIB", "stnPortLedIndex"),
)
if mibBuilder.loadTexts:
    stnPortLedEntry.setStatus("current")
_StnPortLedSlotIndex_Type = Integer32
_StnPortLedSlotIndex_Object = MibTableColumn
stnPortLedSlotIndex = _StnPortLedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1, 1),
    _StnPortLedSlotIndex_Type()
)
stnPortLedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPortLedSlotIndex.setStatus("current")
_StnPortLedPortIndex_Type = Integer32
_StnPortLedPortIndex_Object = MibTableColumn
stnPortLedPortIndex = _StnPortLedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1, 2),
    _StnPortLedPortIndex_Type()
)
stnPortLedPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPortLedPortIndex.setStatus("current")
_StnPortLedIndex_Type = Integer32
_StnPortLedIndex_Object = MibTableColumn
stnPortLedIndex = _StnPortLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1, 3),
    _StnPortLedIndex_Type()
)
stnPortLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPortLedIndex.setStatus("current")
_StnPortLedStatus_Type = StnLedStatus
_StnPortLedStatus_Object = MibTableColumn
stnPortLedStatus = _StnPortLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1, 4),
    _StnPortLedStatus_Type()
)
stnPortLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPortLedStatus.setStatus("current")
_StnPortLedDescr_Type = DisplayString
_StnPortLedDescr_Object = MibTableColumn
stnPortLedDescr = _StnPortLedDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 3, 6, 1, 5),
    _StnPortLedDescr_Type()
)
stnPortLedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPortLedDescr.setStatus("current")
_StnPower_ObjectIdentity = ObjectIdentity
stnPower = _StnPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4)
)
_StnPowerTable_Object = MibTable
stnPowerTable = _StnPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    stnPowerTable.setStatus("current")
_StnPowerEntry_Object = MibTableRow
stnPowerEntry = _StnPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 1, 1)
)
stnPowerEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnPowerIndex"),
)
if mibBuilder.loadTexts:
    stnPowerEntry.setStatus("current")
_StnPowerIndex_Type = Integer32
_StnPowerIndex_Object = MibTableColumn
stnPowerIndex = _StnPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 1, 1, 1),
    _StnPowerIndex_Type()
)
stnPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPowerIndex.setStatus("current")
_StnPowerStatus_Type = StnPowerStatus
_StnPowerStatus_Object = MibTableColumn
stnPowerStatus = _StnPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 1, 1, 2),
    _StnPowerStatus_Type()
)
stnPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPowerStatus.setStatus("current")
_StnPowerDescr_Type = DisplayString
_StnPowerDescr_Object = MibTableColumn
stnPowerDescr = _StnPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 1, 1, 3),
    _StnPowerDescr_Type()
)
stnPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPowerDescr.setStatus("current")
_StnBatteryTable_Object = MibTable
stnBatteryTable = _StnBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    stnBatteryTable.setStatus("current")
_StnBatteryEntry_Object = MibTableRow
stnBatteryEntry = _StnBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2, 1)
)
stnBatteryEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnBatterySlotIndex"),
)
if mibBuilder.loadTexts:
    stnBatteryEntry.setStatus("current")
_StnBatterySlotIndex_Type = Integer32
_StnBatterySlotIndex_Object = MibTableColumn
stnBatterySlotIndex = _StnBatterySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2, 1, 1),
    _StnBatterySlotIndex_Type()
)
stnBatterySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBatterySlotIndex.setStatus("current")
_StnBatteryType_Type = Integer32
_StnBatteryType_Object = MibTableColumn
stnBatteryType = _StnBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2, 1, 2),
    _StnBatteryType_Type()
)
stnBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBatteryType.setStatus("current")
_StnBatteryStatus_Type = StnBatteryStatus
_StnBatteryStatus_Object = MibTableColumn
stnBatteryStatus = _StnBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2, 1, 3),
    _StnBatteryStatus_Type()
)
stnBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBatteryStatus.setStatus("current")
_StnBatteryDescr_Type = DisplayString
_StnBatteryDescr_Object = MibTableColumn
stnBatteryDescr = _StnBatteryDescr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 4, 2, 1, 4),
    _StnBatteryDescr_Type()
)
stnBatteryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBatteryDescr.setStatus("current")
_StnResource_ObjectIdentity = ObjectIdentity
stnResource = _StnResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5)
)
_StnCpuUtilizationTable_Object = MibTable
stnCpuUtilizationTable = _StnCpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    stnCpuUtilizationTable.setStatus("current")
_StnCpuUtilizationEntry_Object = MibTableRow
stnCpuUtilizationEntry = _StnCpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1)
)
stnCpuUtilizationEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnCpuUtilizationIndex"),
)
if mibBuilder.loadTexts:
    stnCpuUtilizationEntry.setStatus("current")
_StnCpuUtilizationIndex_Type = Integer32
_StnCpuUtilizationIndex_Object = MibTableColumn
stnCpuUtilizationIndex = _StnCpuUtilizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1, 1),
    _StnCpuUtilizationIndex_Type()
)
stnCpuUtilizationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuUtilizationIndex.setStatus("current")
_StnCpuUtilizationCurrent_Type = Integer32
_StnCpuUtilizationCurrent_Object = MibTableColumn
stnCpuUtilizationCurrent = _StnCpuUtilizationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1, 2),
    _StnCpuUtilizationCurrent_Type()
)
stnCpuUtilizationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuUtilizationCurrent.setStatus("current")
_StnCpuUtilization5Min_Type = Integer32
_StnCpuUtilization5Min_Object = MibTableColumn
stnCpuUtilization5Min = _StnCpuUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1, 3),
    _StnCpuUtilization5Min_Type()
)
stnCpuUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuUtilization5Min.setStatus("current")
_StnCpuUtilization15Min_Type = Integer32
_StnCpuUtilization15Min_Object = MibTableColumn
stnCpuUtilization15Min = _StnCpuUtilization15Min_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1, 4),
    _StnCpuUtilization15Min_Type()
)
stnCpuUtilization15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuUtilization15Min.setStatus("current")
_StnCpuUtilization30Min_Type = Integer32
_StnCpuUtilization30Min_Object = MibTableColumn
stnCpuUtilization30Min = _StnCpuUtilization30Min_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 1, 1, 5),
    _StnCpuUtilization30Min_Type()
)
stnCpuUtilization30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuUtilization30Min.setStatus("current")
_StnCpuIpTable_Object = MibTable
stnCpuIpTable = _StnCpuIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    stnCpuIpTable.setStatus("current")
_StnCpuIpEntry_Object = MibTableRow
stnCpuIpEntry = _StnCpuIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1)
)
stnCpuIpEntry.setIndexNames(
    (0, "STN-CHASSIS-MIB", "stnCpuIpIndex"),
)
if mibBuilder.loadTexts:
    stnCpuIpEntry.setStatus("current")
_StnCpuIpIndex_Type = Integer32
_StnCpuIpIndex_Object = MibTableColumn
stnCpuIpIndex = _StnCpuIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 1),
    _StnCpuIpIndex_Type()
)
stnCpuIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpIndex.setStatus("current")
_StnCpuIpRouteLimit_Type = Integer32
_StnCpuIpRouteLimit_Object = MibTableColumn
stnCpuIpRouteLimit = _StnCpuIpRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 2),
    _StnCpuIpRouteLimit_Type()
)
stnCpuIpRouteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpRouteLimit.setStatus("current")
_StnCpuIpRoutesInUse_Type = Integer32
_StnCpuIpRoutesInUse_Object = MibTableColumn
stnCpuIpRoutesInUse = _StnCpuIpRoutesInUse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 3),
    _StnCpuIpRoutesInUse_Type()
)
stnCpuIpRoutesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpRoutesInUse.setStatus("current")
_StnCpuIpRoutesBooked_Type = Integer32
_StnCpuIpRoutesBooked_Object = MibTableColumn
stnCpuIpRoutesBooked = _StnCpuIpRoutesBooked_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 4),
    _StnCpuIpRoutesBooked_Type()
)
stnCpuIpRoutesBooked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpRoutesBooked.setStatus("current")
_StnCpuIpFwdProcesses_Type = Integer32
_StnCpuIpFwdProcesses_Object = MibTableColumn
stnCpuIpFwdProcesses = _StnCpuIpFwdProcesses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 5),
    _StnCpuIpFwdProcesses_Type()
)
stnCpuIpFwdProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpFwdProcesses.setStatus("current")
_StnCpuIpRoutingProcesses_Type = Integer32
_StnCpuIpRoutingProcesses_Object = MibTableColumn
stnCpuIpRoutingProcesses = _StnCpuIpRoutingProcesses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 5, 2, 1, 6),
    _StnCpuIpRoutingProcesses_Type()
)
stnCpuIpRoutingProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnCpuIpRoutingProcesses.setStatus("current")
_StnChassisTrapVars_ObjectIdentity = ObjectIdentity
stnChassisTrapVars = _StnChassisTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 100)
)
_StnNotificationCfgChangeTime_Type = TimeTicks
_StnNotificationCfgChangeTime_Object = MibScalar
stnNotificationCfgChangeTime = _StnNotificationCfgChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 100, 1),
    _StnNotificationCfgChangeTime_Type()
)
stnNotificationCfgChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationCfgChangeTime.setStatus("current")
_StnNotificationFlashStatus_Type = StnFlashStatus
_StnNotificationFlashStatus_Object = MibScalar
stnNotificationFlashStatus = _StnNotificationFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 100, 2),
    _StnNotificationFlashStatus_Type()
)
stnNotificationFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationFlashStatus.setStatus("current")
_StnNotificationModuleTemperature_Type = Integer32
_StnNotificationModuleTemperature_Object = MibScalar
stnNotificationModuleTemperature = _StnNotificationModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 100, 3),
    _StnNotificationModuleTemperature_Type()
)
stnNotificationModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationModuleTemperature.setStatus("current")
_StnNotificationResourceStatus_Type = StnResourceStatus
_StnNotificationResourceStatus_Object = MibScalar
stnNotificationResourceStatus = _StnNotificationResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 1, 100, 4),
    _StnNotificationResourceStatus_Type()
)
stnNotificationResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNotificationResourceStatus.setStatus("current")
_StnChassisMibConformance_ObjectIdentity = ObjectIdentity
stnChassisMibConformance = _StnChassisMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 2)
)
_StnChassisMibCompliances_ObjectIdentity = ObjectIdentity
stnChassisMibCompliances = _StnChassisMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 2, 1)
)
_StnChassisMibGroups_ObjectIdentity = ObjectIdentity
stnChassisMibGroups = _StnChassisMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 2, 2)
)

# Managed Objects groups

stnChassisMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 2, 2, 1)
)
stnChassisMibGroup.setObjects(
      *(("STN-CHASSIS-MIB", "stnChassisSysType"),
        ("STN-CHASSIS-MIB", "stnChassisSysDescr"),
        ("STN-CHASSIS-MIB", "stnChassisId"),
        ("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnModulePeer"),
        ("STN-CHASSIS-MIB", "stnModuleAdminStatus"),
        ("STN-CHASSIS-MIB", "stnModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnModuleDescr"),
        ("STN-CHASSIS-MIB", "stnModuleLed"),
        ("STN-CHASSIS-MIB", "stnSubModules"),
        ("STN-CHASSIS-MIB", "stnSubModuleSlot"),
        ("STN-CHASSIS-MIB", "stnSubModuleIndex"),
        ("STN-CHASSIS-MIB", "stnSubModuleType"),
        ("STN-CHASSIS-MIB", "stnSubModulePeer"),
        ("STN-CHASSIS-MIB", "stnSubModuleAdminStatus"),
        ("STN-CHASSIS-MIB", "stnSubModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnSubModuleDescr"),
        ("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-CHASSIS-MIB", "stnEngineType"),
        ("STN-CHASSIS-MIB", "stnEnginePeer"),
        ("STN-CHASSIS-MIB", "stnEngineAdminStatus"),
        ("STN-CHASSIS-MIB", "stnEngineOperStatus"),
        ("STN-CHASSIS-MIB", "stnEngineDescr"),
        ("STN-CHASSIS-MIB", "stnLedFanTray"),
        ("STN-CHASSIS-MIB", "stnLedPowerA"),
        ("STN-CHASSIS-MIB", "stnLedPowerB"),
        ("STN-CHASSIS-MIB", "stnLedAlarm"),
        ("STN-CHASSIS-MIB", "stnFanTrayLedIndex"),
        ("STN-CHASSIS-MIB", "stnFanTrayLedSlotIndex"),
        ("STN-CHASSIS-MIB", "stnFanTrayLedStatus"),
        ("STN-CHASSIS-MIB", "stnPortLedSlotIndex"),
        ("STN-CHASSIS-MIB", "stnPortLedPortIndex"),
        ("STN-CHASSIS-MIB", "stnPortLedIndex"),
        ("STN-CHASSIS-MIB", "stnPortLedStatus"),
        ("STN-CHASSIS-MIB", "stnPortLedDescr"),
        ("STN-CHASSIS-MIB", "stnPowerIndex"),
        ("STN-CHASSIS-MIB", "stnPowerStatus"),
        ("STN-CHASSIS-MIB", "stnPowerDescr"),
        ("STN-CHASSIS-MIB", "stnBatterySlotIndex"),
        ("STN-CHASSIS-MIB", "stnBatteryType"),
        ("STN-CHASSIS-MIB", "stnBatteryStatus"),
        ("STN-CHASSIS-MIB", "stnBatteryDescr"))
)
if mibBuilder.loadTexts:
    stnChassisMibGroup.setStatus("current")


# Notification objects

stnRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 1)
)
stnRedundant.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnModuleOperStatus"))
)
if mibBuilder.loadTexts:
    stnRedundant.setStatus(
        "current"
    )

stnNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 2)
)
stnNotRedundant.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnModuleOperStatus"))
)
if mibBuilder.loadTexts:
    stnNotRedundant.setStatus(
        "current"
    )

stnModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 3)
)
stnModuleUp.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnModuleDescr"),
        ("STN-CHASSIS-MIB", "stnSubModules"))
)
if mibBuilder.loadTexts:
    stnModuleUp.setStatus(
        "current"
    )

stnModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 4)
)
stnModuleDown.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnModuleDescr"),
        ("STN-CHASSIS-MIB", "stnSubModules"))
)
if mibBuilder.loadTexts:
    stnModuleDown.setStatus(
        "current"
    )

stnSubModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 5)
)
stnSubModuleUp.setObjects(
      *(("STN-CHASSIS-MIB", "stnSubModuleSlot"),
        ("STN-CHASSIS-MIB", "stnSubModuleIndex"),
        ("STN-CHASSIS-MIB", "stnSubModuleType"),
        ("STN-CHASSIS-MIB", "stnSubModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnSubModuleDescr"))
)
if mibBuilder.loadTexts:
    stnSubModuleUp.setStatus(
        "current"
    )

stnSubModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 6)
)
stnSubModuleDown.setObjects(
      *(("STN-CHASSIS-MIB", "stnSubModuleSlot"),
        ("STN-CHASSIS-MIB", "stnSubModuleIndex"),
        ("STN-CHASSIS-MIB", "stnSubModuleType"),
        ("STN-CHASSIS-MIB", "stnSubModuleOperStatus"),
        ("STN-CHASSIS-MIB", "stnSubModuleDescr"))
)
if mibBuilder.loadTexts:
    stnSubModuleDown.setStatus(
        "current"
    )

stnEngineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 7)
)
stnEngineUp.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-CHASSIS-MIB", "stnEngineType"),
        ("STN-CHASSIS-MIB", "stnEngineOperStatus"))
)
if mibBuilder.loadTexts:
    stnEngineUp.setStatus(
        "current"
    )

stnEngineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 8)
)
stnEngineDown.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-CHASSIS-MIB", "stnEngineType"),
        ("STN-CHASSIS-MIB", "stnEngineOperStatus"))
)
if mibBuilder.loadTexts:
    stnEngineDown.setStatus(
        "current"
    )

stnBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 9)
)
stnBatteryLow.setObjects(
      *(("STN-CHASSIS-MIB", "stnBatterySlotIndex"),
        ("STN-CHASSIS-MIB", "stnBatteryType"),
        ("STN-CHASSIS-MIB", "stnBatteryStatus"))
)
if mibBuilder.loadTexts:
    stnBatteryLow.setStatus(
        "current"
    )

stnFlashFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 10)
)
stnFlashFailure.setObjects(
    ("STN-CHASSIS-MIB", "stnNotificationFlashStatus")
)
if mibBuilder.loadTexts:
    stnFlashFailure.setStatus(
        "current"
    )

stnResourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 11)
)
stnResourceFailure.setObjects(
    ("STN-CHASSIS-MIB", "stnNotificationResourceStatus")
)
if mibBuilder.loadTexts:
    stnResourceFailure.setStatus(
        "current"
    )

stnFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 12)
)
stnFailover.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"))
)
if mibBuilder.loadTexts:
    stnFailover.setStatus(
        "current"
    )

stnCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 19)
)
stnCfgChange.setObjects(
    ("STN-CHASSIS-MIB", "stnNotificationCfgChangeTime")
)
if mibBuilder.loadTexts:
    stnCfgChange.setStatus(
        "current"
    )

stnPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 55)
)
stnPowerFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnPowerIndex"),
        ("STN-CHASSIS-MIB", "stnPowerStatus"))
)
if mibBuilder.loadTexts:
    stnPowerFailure.setStatus(
        "current"
    )

stnTemperatureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 56)
)
stnTemperatureFailure.setObjects(
      *(("STN-CHASSIS-MIB", "stnSlotIndex"),
        ("STN-CHASSIS-MIB", "stnModuleType"),
        ("STN-CHASSIS-MIB", "stnSubModuleType"),
        ("STN-CHASSIS-MIB", "stnNotificationModuleTemperature"))
)
if mibBuilder.loadTexts:
    stnTemperatureFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

stnChassisMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3551, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    stnChassisMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-CHASSIS-MIB",
    **{"stnChassis": stnChassis,
       "stnChassisObjects": stnChassisObjects,
       "stnChassisVars": stnChassisVars,
       "stnChassisSysType": stnChassisSysType,
       "stnChassisSysDescr": stnChassisSysDescr,
       "stnChassisId": stnChassisId,
       "stnModules": stnModules,
       "stnSlotTable": stnSlotTable,
       "stnSlotEntry": stnSlotEntry,
       "stnSlotIndex": stnSlotIndex,
       "stnModuleType": stnModuleType,
       "stnModulePeer": stnModulePeer,
       "stnModuleAdminStatus": stnModuleAdminStatus,
       "stnModuleOperStatus": stnModuleOperStatus,
       "stnModuleDescr": stnModuleDescr,
       "stnModuleLed": stnModuleLed,
       "stnSubModules": stnSubModules,
       "stnSubModuleTable": stnSubModuleTable,
       "stnSubModuleEntry": stnSubModuleEntry,
       "stnSubModuleSlot": stnSubModuleSlot,
       "stnSubModuleIndex": stnSubModuleIndex,
       "stnSubModuleType": stnSubModuleType,
       "stnSubModulePeer": stnSubModulePeer,
       "stnSubModuleAdminStatus": stnSubModuleAdminStatus,
       "stnSubModuleOperStatus": stnSubModuleOperStatus,
       "stnSubModuleDescr": stnSubModuleDescr,
       "stnEngineTable": stnEngineTable,
       "stnEngineEntry": stnEngineEntry,
       "stnEngineIndex": stnEngineIndex,
       "stnEngineSlot": stnEngineSlot,
       "stnEngineCpu": stnEngineCpu,
       "stnEngineType": stnEngineType,
       "stnEnginePeer": stnEnginePeer,
       "stnEngineAdminStatus": stnEngineAdminStatus,
       "stnEngineOperStatus": stnEngineOperStatus,
       "stnEngineDescr": stnEngineDescr,
       "stnLeds": stnLeds,
       "stnLedFanTray": stnLedFanTray,
       "stnLedPowerA": stnLedPowerA,
       "stnLedPowerB": stnLedPowerB,
       "stnLedAlarm": stnLedAlarm,
       "stnFanTrayLedTable": stnFanTrayLedTable,
       "stnFanTrayLedEntry": stnFanTrayLedEntry,
       "stnFanTrayLedIndex": stnFanTrayLedIndex,
       "stnFanTrayLedSlotIndex": stnFanTrayLedSlotIndex,
       "stnFanTrayLedStatus": stnFanTrayLedStatus,
       "stnPortLedTable": stnPortLedTable,
       "stnPortLedEntry": stnPortLedEntry,
       "stnPortLedSlotIndex": stnPortLedSlotIndex,
       "stnPortLedPortIndex": stnPortLedPortIndex,
       "stnPortLedIndex": stnPortLedIndex,
       "stnPortLedStatus": stnPortLedStatus,
       "stnPortLedDescr": stnPortLedDescr,
       "stnPower": stnPower,
       "stnPowerTable": stnPowerTable,
       "stnPowerEntry": stnPowerEntry,
       "stnPowerIndex": stnPowerIndex,
       "stnPowerStatus": stnPowerStatus,
       "stnPowerDescr": stnPowerDescr,
       "stnBatteryTable": stnBatteryTable,
       "stnBatteryEntry": stnBatteryEntry,
       "stnBatterySlotIndex": stnBatterySlotIndex,
       "stnBatteryType": stnBatteryType,
       "stnBatteryStatus": stnBatteryStatus,
       "stnBatteryDescr": stnBatteryDescr,
       "stnResource": stnResource,
       "stnCpuUtilizationTable": stnCpuUtilizationTable,
       "stnCpuUtilizationEntry": stnCpuUtilizationEntry,
       "stnCpuUtilizationIndex": stnCpuUtilizationIndex,
       "stnCpuUtilizationCurrent": stnCpuUtilizationCurrent,
       "stnCpuUtilization5Min": stnCpuUtilization5Min,
       "stnCpuUtilization15Min": stnCpuUtilization15Min,
       "stnCpuUtilization30Min": stnCpuUtilization30Min,
       "stnCpuIpTable": stnCpuIpTable,
       "stnCpuIpEntry": stnCpuIpEntry,
       "stnCpuIpIndex": stnCpuIpIndex,
       "stnCpuIpRouteLimit": stnCpuIpRouteLimit,
       "stnCpuIpRoutesInUse": stnCpuIpRoutesInUse,
       "stnCpuIpRoutesBooked": stnCpuIpRoutesBooked,
       "stnCpuIpFwdProcesses": stnCpuIpFwdProcesses,
       "stnCpuIpRoutingProcesses": stnCpuIpRoutingProcesses,
       "stnChassisTrapVars": stnChassisTrapVars,
       "stnNotificationCfgChangeTime": stnNotificationCfgChangeTime,
       "stnNotificationFlashStatus": stnNotificationFlashStatus,
       "stnNotificationModuleTemperature": stnNotificationModuleTemperature,
       "stnNotificationResourceStatus": stnNotificationResourceStatus,
       "stnChassisMibConformance": stnChassisMibConformance,
       "stnChassisMibCompliances": stnChassisMibCompliances,
       "stnChassisMibComplianceRev1": stnChassisMibComplianceRev1,
       "stnChassisMibGroups": stnChassisMibGroups,
       "stnChassisMibGroup": stnChassisMibGroup,
       "stnRedundant": stnRedundant,
       "stnNotRedundant": stnNotRedundant,
       "stnModuleUp": stnModuleUp,
       "stnModuleDown": stnModuleDown,
       "stnSubModuleUp": stnSubModuleUp,
       "stnSubModuleDown": stnSubModuleDown,
       "stnEngineUp": stnEngineUp,
       "stnEngineDown": stnEngineDown,
       "stnBatteryLow": stnBatteryLow,
       "stnFlashFailure": stnFlashFailure,
       "stnResourceFailure": stnResourceFailure,
       "stnFailover": stnFailover,
       "stnCfgChange": stnCfgChange,
       "stnPowerFailure": stnPowerFailure,
       "stnTemperatureFailure": stnTemperatureFailure}
)
