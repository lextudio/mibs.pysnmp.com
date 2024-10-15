# SNMP MIB module (SAVEPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAVEPOWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:45 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpicfSavepowerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56)
)
hpicfSavepowerMIB.setRevisions(
        ("2010-08-12 00:00",
         "2008-10-17 14:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SavepowerBlockIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class SavepowerControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 2),
          ("powerOn", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfSavepowerScalars_ObjectIdentity = ObjectIdentity
hpicfSavepowerScalars = _HpicfSavepowerScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1)
)
_HpicfSavepowerMaxBlocks_Type = Unsigned32
_HpicfSavepowerMaxBlocks_Object = MibScalar
hpicfSavepowerMaxBlocks = _HpicfSavepowerMaxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 1),
    _HpicfSavepowerMaxBlocks_Type()
)
hpicfSavepowerMaxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerMaxBlocks.setStatus("current")


class _HpicfSavepowerEnabledPorts_Type(Unsigned32):
    """Custom type hpicfSavepowerEnabledPorts based on Unsigned32"""
    defaultValue = 0


_HpicfSavepowerEnabledPorts_Object = MibScalar
hpicfSavepowerEnabledPorts = _HpicfSavepowerEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 2),
    _HpicfSavepowerEnabledPorts_Type()
)
hpicfSavepowerEnabledPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerEnabledPorts.setStatus("current")
_HpicfSavepowerLEDScalars_ObjectIdentity = ObjectIdentity
hpicfSavepowerLEDScalars = _HpicfSavepowerLEDScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3)
)
_HpicfSavePowerLEDOffAlarmStartTime_Type = DateAndTime
_HpicfSavePowerLEDOffAlarmStartTime_Object = MibScalar
hpicfSavePowerLEDOffAlarmStartTime = _HpicfSavePowerLEDOffAlarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 1),
    _HpicfSavePowerLEDOffAlarmStartTime_Type()
)
hpicfSavePowerLEDOffAlarmStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavePowerLEDOffAlarmStartTime.setStatus("current")
_HpicfSavePowerLEDOffAlarmDuration_Type = Unsigned32
_HpicfSavePowerLEDOffAlarmDuration_Object = MibScalar
hpicfSavePowerLEDOffAlarmDuration = _HpicfSavePowerLEDOffAlarmDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 2),
    _HpicfSavePowerLEDOffAlarmDuration_Type()
)
hpicfSavePowerLEDOffAlarmDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavePowerLEDOffAlarmDuration.setStatus("current")
_HpicfSavePowerLEDOffAlarmRecur_Type = TruthValue
_HpicfSavePowerLEDOffAlarmRecur_Object = MibScalar
hpicfSavePowerLEDOffAlarmRecur = _HpicfSavePowerLEDOffAlarmRecur_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 1, 3, 3),
    _HpicfSavePowerLEDOffAlarmRecur_Type()
)
hpicfSavePowerLEDOffAlarmRecur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavePowerLEDOffAlarmRecur.setStatus("current")
_HpicfEntitySavepower_ObjectIdentity = ObjectIdentity
hpicfEntitySavepower = _HpicfEntitySavepower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2)
)
_HpicfSavepowerTable_Object = MibTable
hpicfSavepowerTable = _HpicfSavepowerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSavepowerTable.setStatus("current")
_HpicfSavepowerEntry_Object = MibTableRow
hpicfSavepowerEntry = _HpicfSavepowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1)
)
hpicfSavepowerEntry.setIndexNames(
    (0, "SAVEPOWER-MIB", "hpicfSavepowerBlockID"),
)
if mibBuilder.loadTexts:
    hpicfSavepowerEntry.setStatus("current")
_HpicfSavepowerBlockID_Type = SavepowerBlockIndex
_HpicfSavepowerBlockID_Object = MibTableColumn
hpicfSavepowerBlockID = _HpicfSavepowerBlockID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 1),
    _HpicfSavepowerBlockID_Type()
)
hpicfSavepowerBlockID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSavepowerBlockID.setStatus("current")
_HpicfSavepowerControl_Type = SavepowerControl
_HpicfSavepowerControl_Object = MibTableColumn
hpicfSavepowerControl = _HpicfSavepowerControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 2),
    _HpicfSavepowerControl_Type()
)
hpicfSavepowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavepowerControl.setStatus("current")
_HpicfSavepowerBlockPorts_Type = DisplayString
_HpicfSavepowerBlockPorts_Object = MibTableColumn
hpicfSavepowerBlockPorts = _HpicfSavepowerBlockPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 1, 1, 3),
    _HpicfSavepowerBlockPorts_Type()
)
hpicfSavepowerBlockPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerBlockPorts.setStatus("current")
_HpicfSavepowerGreenFeaturesTable_Object = MibTable
hpicfSavepowerGreenFeaturesTable = _HpicfSavepowerGreenFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfSavepowerGreenFeaturesTable.setStatus("current")
_HpicfSavepowerGreenFeaturesEntry_Object = MibTableRow
hpicfSavepowerGreenFeaturesEntry = _HpicfSavepowerGreenFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1)
)
hpicfSavepowerGreenFeaturesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfSavepowerGreenFeaturesEntry.setStatus("current")
_HpicfSavepowerEntityPowerAdminStatus_Type = TruthValue
_HpicfSavepowerEntityPowerAdminStatus_Object = MibTableColumn
hpicfSavepowerEntityPowerAdminStatus = _HpicfSavepowerEntityPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 1),
    _HpicfSavepowerEntityPowerAdminStatus_Type()
)
hpicfSavepowerEntityPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavepowerEntityPowerAdminStatus.setStatus("current")
_HpicfSavepowerEntityPowerOperStatus_Type = SavepowerControl
_HpicfSavepowerEntityPowerOperStatus_Object = MibTableColumn
hpicfSavepowerEntityPowerOperStatus = _HpicfSavepowerEntityPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 2),
    _HpicfSavepowerEntityPowerOperStatus_Type()
)
hpicfSavepowerEntityPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerEntityPowerOperStatus.setStatus("current")
_HpicfSavepowerEntityLEDAdminStatus_Type = TruthValue
_HpicfSavepowerEntityLEDAdminStatus_Object = MibTableColumn
hpicfSavepowerEntityLEDAdminStatus = _HpicfSavepowerEntityLEDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 3),
    _HpicfSavepowerEntityLEDAdminStatus_Type()
)
hpicfSavepowerEntityLEDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavepowerEntityLEDAdminStatus.setStatus("current")
_HpicfSavepowerEntityLEDOperStatus_Type = SavepowerControl
_HpicfSavepowerEntityLEDOperStatus_Object = MibTableColumn
hpicfSavepowerEntityLEDOperStatus = _HpicfSavepowerEntityLEDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 2, 1, 4),
    _HpicfSavepowerEntityLEDOperStatus_Type()
)
hpicfSavepowerEntityLEDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerEntityLEDOperStatus.setStatus("current")
_HpicfSavepowerPHYTable_Object = MibTable
hpicfSavepowerPHYTable = _HpicfSavepowerPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfSavepowerPHYTable.setStatus("current")
_HpicfSavepowerPHYEntry_Object = MibTableRow
hpicfSavepowerPHYEntry = _HpicfSavepowerPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1)
)
hpicfSavepowerPHYEntry.setIndexNames(
    (0, "SAVEPOWER-MIB", "hpicfSavepowerSlotNum"),
    (0, "SAVEPOWER-MIB", "hpicfSavepowerPortNum"),
)
if mibBuilder.loadTexts:
    hpicfSavepowerPHYEntry.setStatus("current")
_HpicfSavepowerSlotNum_Type = Unsigned32
_HpicfSavepowerSlotNum_Object = MibTableColumn
hpicfSavepowerSlotNum = _HpicfSavepowerSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 1),
    _HpicfSavepowerSlotNum_Type()
)
hpicfSavepowerSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSavepowerSlotNum.setStatus("current")
_HpicfSavepowerPortNum_Type = Unsigned32
_HpicfSavepowerPortNum_Object = MibTableColumn
hpicfSavepowerPortNum = _HpicfSavepowerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 2),
    _HpicfSavepowerPortNum_Type()
)
hpicfSavepowerPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSavepowerPortNum.setStatus("current")
_HpicfSavepowerPHYAdminStatus_Type = TruthValue
_HpicfSavepowerPHYAdminStatus_Object = MibTableColumn
hpicfSavepowerPHYAdminStatus = _HpicfSavepowerPHYAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 3),
    _HpicfSavepowerPHYAdminStatus_Type()
)
hpicfSavepowerPHYAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavepowerPHYAdminStatus.setStatus("current")
_HpicfSavepowerPHYOperStatus_Type = SavepowerControl
_HpicfSavepowerPHYOperStatus_Object = MibTableColumn
hpicfSavepowerPHYOperStatus = _HpicfSavepowerPHYOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 3, 1, 4),
    _HpicfSavepowerPHYOperStatus_Type()
)
hpicfSavepowerPHYOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerPHYOperStatus.setStatus("current")
_HpicfSavepowerEntPHYTable_Object = MibTable
hpicfSavepowerEntPHYTable = _HpicfSavepowerEntPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfSavepowerEntPHYTable.setStatus("current")
_HpicfSavepowerEntPHYEntry_Object = MibTableRow
hpicfSavepowerEntPHYEntry = _HpicfSavepowerEntPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1)
)
hpicfSavepowerEntPHYEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfSavepowerEntPHYEntry.setStatus("current")
_HpicfSavepowerEntPHYAdminStatus_Type = TruthValue
_HpicfSavepowerEntPHYAdminStatus_Object = MibTableColumn
hpicfSavepowerEntPHYAdminStatus = _HpicfSavepowerEntPHYAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1, 1),
    _HpicfSavepowerEntPHYAdminStatus_Type()
)
hpicfSavepowerEntPHYAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSavepowerEntPHYAdminStatus.setStatus("current")
_HpicfSavepowerEntPHYOperStatus_Type = SavepowerControl
_HpicfSavepowerEntPHYOperStatus_Object = MibTableColumn
hpicfSavepowerEntPHYOperStatus = _HpicfSavepowerEntPHYOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 2, 4, 1, 2),
    _HpicfSavepowerEntPHYOperStatus_Type()
)
hpicfSavepowerEntPHYOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSavepowerEntPHYOperStatus.setStatus("current")
_HpicfSavepowerConformance_ObjectIdentity = ObjectIdentity
hpicfSavepowerConformance = _HpicfSavepowerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3)
)
_HpicfSavepowerCompliance_ObjectIdentity = ObjectIdentity
hpicfSavepowerCompliance = _HpicfSavepowerCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 1)
)
_HpicfSavepowerGroups_ObjectIdentity = ObjectIdentity
hpicfSavepowerGroups = _HpicfSavepowerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2)
)
_HpicfPHYConformance_ObjectIdentity = ObjectIdentity
hpicfPHYConformance = _HpicfPHYConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4)
)
_HpicfPHYCompliance_ObjectIdentity = ObjectIdentity
hpicfPHYCompliance = _HpicfPHYCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 1)
)
_HpicfPHYGroups_ObjectIdentity = ObjectIdentity
hpicfPHYGroups = _HpicfPHYGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 2)
)

# Managed Objects groups

hpicfSavepowerScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 1)
)
hpicfSavepowerScalarsGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavepowerMaxBlocks"),
        ("SAVEPOWER-MIB", "hpicfSavepowerEnabledPorts"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerScalarsGroup.setStatus("current")

hpicfSavepowerLEDScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 2)
)
hpicfSavepowerLEDScalarsGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmStartTime"),
        ("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmDuration"),
        ("SAVEPOWER-MIB", "hpicfSavePowerLEDOffAlarmRecur"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerLEDScalarsGroup.setStatus("current")

hpicfSavepowerGreenFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 3)
)
hpicfSavepowerGreenFeaturesGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavepowerEntityPowerAdminStatus"),
        ("SAVEPOWER-MIB", "hpicfSavepowerEntityPowerOperStatus"),
        ("SAVEPOWER-MIB", "hpicfSavepowerEntityLEDAdminStatus"),
        ("SAVEPOWER-MIB", "hpicfSavepowerEntityLEDOperStatus"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerGreenFeaturesGroup.setStatus("current")

hpicfSavepowerPHYGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 4)
)
hpicfSavepowerPHYGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavepowerPHYAdminStatus"),
        ("SAVEPOWER-MIB", "hpicfSavepowerPHYOperStatus"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerPHYGroup.setStatus("current")

hpicfSavepowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 2, 5)
)
hpicfSavepowerGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavepowerControl"),
        ("SAVEPOWER-MIB", "hpicfSavepowerBlockPorts"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerGroup.setStatus("current")

hpicfSavepowerEntPHYGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 2, 1)
)
hpicfSavepowerEntPHYGroup.setObjects(
      *(("SAVEPOWER-MIB", "hpicfSavepowerEntPHYAdminStatus"),
        ("SAVEPOWER-MIB", "hpicfSavepowerEntPHYOperStatus"))
)
if mibBuilder.loadTexts:
    hpicfSavepowerEntPHYGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSavepowerComplianceInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSavepowerComplianceInfo.setStatus(
        "current"
    )

hpicfPHYComplianceInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPHYComplianceInfo.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAVEPOWER-MIB",
    **{"SavepowerBlockIndex": SavepowerBlockIndex,
       "SavepowerControl": SavepowerControl,
       "hpicfSavepowerMIB": hpicfSavepowerMIB,
       "hpicfSavepowerScalars": hpicfSavepowerScalars,
       "hpicfSavepowerMaxBlocks": hpicfSavepowerMaxBlocks,
       "hpicfSavepowerEnabledPorts": hpicfSavepowerEnabledPorts,
       "hpicfSavepowerLEDScalars": hpicfSavepowerLEDScalars,
       "hpicfSavePowerLEDOffAlarmStartTime": hpicfSavePowerLEDOffAlarmStartTime,
       "hpicfSavePowerLEDOffAlarmDuration": hpicfSavePowerLEDOffAlarmDuration,
       "hpicfSavePowerLEDOffAlarmRecur": hpicfSavePowerLEDOffAlarmRecur,
       "hpicfEntitySavepower": hpicfEntitySavepower,
       "hpicfSavepowerTable": hpicfSavepowerTable,
       "hpicfSavepowerEntry": hpicfSavepowerEntry,
       "hpicfSavepowerBlockID": hpicfSavepowerBlockID,
       "hpicfSavepowerControl": hpicfSavepowerControl,
       "hpicfSavepowerBlockPorts": hpicfSavepowerBlockPorts,
       "hpicfSavepowerGreenFeaturesTable": hpicfSavepowerGreenFeaturesTable,
       "hpicfSavepowerGreenFeaturesEntry": hpicfSavepowerGreenFeaturesEntry,
       "hpicfSavepowerEntityPowerAdminStatus": hpicfSavepowerEntityPowerAdminStatus,
       "hpicfSavepowerEntityPowerOperStatus": hpicfSavepowerEntityPowerOperStatus,
       "hpicfSavepowerEntityLEDAdminStatus": hpicfSavepowerEntityLEDAdminStatus,
       "hpicfSavepowerEntityLEDOperStatus": hpicfSavepowerEntityLEDOperStatus,
       "hpicfSavepowerPHYTable": hpicfSavepowerPHYTable,
       "hpicfSavepowerPHYEntry": hpicfSavepowerPHYEntry,
       "hpicfSavepowerSlotNum": hpicfSavepowerSlotNum,
       "hpicfSavepowerPortNum": hpicfSavepowerPortNum,
       "hpicfSavepowerPHYAdminStatus": hpicfSavepowerPHYAdminStatus,
       "hpicfSavepowerPHYOperStatus": hpicfSavepowerPHYOperStatus,
       "hpicfSavepowerEntPHYTable": hpicfSavepowerEntPHYTable,
       "hpicfSavepowerEntPHYEntry": hpicfSavepowerEntPHYEntry,
       "hpicfSavepowerEntPHYAdminStatus": hpicfSavepowerEntPHYAdminStatus,
       "hpicfSavepowerEntPHYOperStatus": hpicfSavepowerEntPHYOperStatus,
       "hpicfSavepowerConformance": hpicfSavepowerConformance,
       "hpicfSavepowerCompliance": hpicfSavepowerCompliance,
       "hpicfSavepowerComplianceInfo": hpicfSavepowerComplianceInfo,
       "hpicfSavepowerGroups": hpicfSavepowerGroups,
       "hpicfSavepowerScalarsGroup": hpicfSavepowerScalarsGroup,
       "hpicfSavepowerLEDScalarsGroup": hpicfSavepowerLEDScalarsGroup,
       "hpicfSavepowerGreenFeaturesGroup": hpicfSavepowerGreenFeaturesGroup,
       "hpicfSavepowerPHYGroup": hpicfSavepowerPHYGroup,
       "hpicfSavepowerGroup": hpicfSavepowerGroup,
       "hpicfPHYConformance": hpicfPHYConformance,
       "hpicfPHYCompliance": hpicfPHYCompliance,
       "hpicfPHYComplianceInfo": hpicfPHYComplianceInfo,
       "hpicfPHYGroups": hpicfPHYGroups,
       "hpicfSavepowerEntPHYGroup": hpicfSavepowerEntPHYGroup}
)
