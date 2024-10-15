# SNMP MIB module (CHECKPOINT-GAIA-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHECKPOINT-GAIA-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:38 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

chkpntTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 0)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Checkpoint_ObjectIdentity = ObjectIdentity
checkpoint = _Checkpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1)
)
_Svn_ObjectIdentity = ObjectIdentity
svn = _Svn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6)
)
_SvnPerf_ObjectIdentity = ObjectIdentity
svnPerf = _SvnPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7)
)
_RaidInfo_ObjectIdentity = ObjectIdentity
raidInfo = _RaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6)
)
_RaidVolumeTable_ObjectIdentity = ObjectIdentity
raidVolumeTable = _RaidVolumeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1)
)
_RaidVolumeEntry_ObjectIdentity = ObjectIdentity
raidVolumeEntry = _RaidVolumeEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1)
)
_RaidVolumeState_Type = DisplayString
_RaidVolumeState_Object = MibScalar
raidVolumeState = _RaidVolumeState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1, 6),
    _RaidVolumeState_Type()
)
raidVolumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeState.setStatus("mandatory")
_RaidVolumeFlags_Type = DisplayString
_RaidVolumeFlags_Object = MibScalar
raidVolumeFlags = _RaidVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1, 7),
    _RaidVolumeFlags_Type()
)
raidVolumeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeFlags.setStatus("mandatory")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8)
)
_TempertureSensorTable_ObjectIdentity = ObjectIdentity
tempertureSensorTable = _TempertureSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1)
)
_TempertureSensorEntry_ObjectIdentity = ObjectIdentity
tempertureSensorEntry = _TempertureSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1)
)
_TempertureSensorName_Type = DisplayString
_TempertureSensorName_Object = MibScalar
tempertureSensorName = _TempertureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 2),
    _TempertureSensorName_Type()
)
tempertureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorName.setStatus("mandatory")
_TempertureSensorValue_Type = DisplayString
_TempertureSensorValue_Object = MibScalar
tempertureSensorValue = _TempertureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 3),
    _TempertureSensorValue_Type()
)
tempertureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorValue.setStatus("mandatory")
_FanSpeedSensorTable_ObjectIdentity = ObjectIdentity
fanSpeedSensorTable = _FanSpeedSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2)
)
_FanSpeedSensorEntry_ObjectIdentity = ObjectIdentity
fanSpeedSensorEntry = _FanSpeedSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1)
)
_FanSpeedSensorName_Type = DisplayString
_FanSpeedSensorName_Object = MibScalar
fanSpeedSensorName = _FanSpeedSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 2),
    _FanSpeedSensorName_Type()
)
fanSpeedSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorName.setStatus("mandatory")
_FanSpeedSensorValue_Type = DisplayString
_FanSpeedSensorValue_Object = MibScalar
fanSpeedSensorValue = _FanSpeedSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 3),
    _FanSpeedSensorValue_Type()
)
fanSpeedSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorValue.setStatus("mandatory")
_VoltageSensorTable_ObjectIdentity = ObjectIdentity
voltageSensorTable = _VoltageSensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3)
)
_VoltageSensorEntry_ObjectIdentity = ObjectIdentity
voltageSensorEntry = _VoltageSensorEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1)
)
_VoltageSensorName_Type = DisplayString
_VoltageSensorName_Object = MibScalar
voltageSensorName = _VoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 2),
    _VoltageSensorName_Type()
)
voltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorName.setStatus("mandatory")
_VoltageSensorValue_Type = DisplayString
_VoltageSensorValue_Object = MibScalar
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 3),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("mandatory")
_PowerSupplyInfo_ObjectIdentity = ObjectIdentity
powerSupplyInfo = _PowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9)
)
_PowerSupplyTable_ObjectIdentity = ObjectIdentity
powerSupplyTable = _PowerSupplyTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1)
)
_PowerSupplyEntry_ObjectIdentity = ObjectIdentity
powerSupplyEntry = _PowerSupplyEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1)
)
_PowerSupplySensorName_Type = DisplayString
_PowerSupplySensorName_Object = MibScalar
powerSupplySensorName = _PowerSupplySensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 2),
    _PowerSupplySensorName_Type()
)
powerSupplySensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySensorName.setStatus("mandatory")
_PowerSupplySensorValue_Type = DisplayString
_PowerSupplySensorValue_Object = MibScalar
powerSupplySensorValue = _PowerSupplySensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 3),
    _PowerSupplySensorValue_Type()
)
powerSupplySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySensorValue.setStatus("mandatory")
_ChkpntTrap_ObjectIdentity = ObjectIdentity
chkpntTrap = _ChkpntTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000)
)
_ChkpntTrapInfo_ObjectIdentity = ObjectIdentity
chkpntTrapInfo = _ChkpntTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0)
)
_ChkpntTrapOID_Type = DisplayString
_ChkpntTrapOID_Object = MibScalar
chkpntTrapOID = _ChkpntTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 10),
    _ChkpntTrapOID_Type()
)
chkpntTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapOID.setStatus("optional")
_ChkpntTrapMsgText_Type = DisplayString
_ChkpntTrapMsgText_Object = MibScalar
chkpntTrapMsgText = _ChkpntTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 0, 12),
    _ChkpntTrapMsgText_Type()
)
chkpntTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapMsgText.setStatus("mandatory")
_ChkpntTrapDisk_ObjectIdentity = ObjectIdentity
chkpntTrapDisk = _ChkpntTrapDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2)
)
_ChkpntTrapRAID_ObjectIdentity = ObjectIdentity
chkpntTrapRAID = _ChkpntTrapRAID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2, 1)
)
_ChkpntTrapHWSensor_ObjectIdentity = ObjectIdentity
chkpntTrapHWSensor = _ChkpntTrapHWSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5)
)
_ChkpntTrapTempertureSensor_ObjectIdentity = ObjectIdentity
chkpntTrapTempertureSensor = _ChkpntTrapTempertureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 1)
)
_ChkpntTrapFanSpeedSensor_ObjectIdentity = ObjectIdentity
chkpntTrapFanSpeedSensor = _ChkpntTrapFanSpeedSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 2)
)
_ChkpntTrapVoltageSensor_ObjectIdentity = ObjectIdentity
chkpntTrapVoltageSensor = _ChkpntTrapVoltageSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 3)
)
_ChkpntTrapPowerSupplySensor_ObjectIdentity = ObjectIdentity
chkpntTrapPowerSupplySensor = _ChkpntTrapPowerSupplySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 4)
)
_ChkpntTrapConfiguration_ObjectIdentity = ObjectIdentity
chkpntTrapConfiguration = _ChkpntTrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10)
)
_ChkpntTrapSystemConfiguration_ObjectIdentity = ObjectIdentity
chkpntTrapSystemConfiguration = _ChkpntTrapSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1)
)

# Managed Objects groups


# Notification objects

chkpntRAIDVolumeStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 2, 1, 1)
)
chkpntRAIDVolumeStateTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "raidVolumeState"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "raidVolumeFlags"))
)
if mibBuilder.loadTexts:
    chkpntRAIDVolumeStateTrap.setStatus(
        "current"
    )

chkpntTempertureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 1, 1)
)
chkpntTempertureTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "tempertureSensorName"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "tempertureSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntTempertureTrap.setStatus(
        "current"
    )

chkpntFanSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 2, 1)
)
chkpntFanSpeedTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "fanSpeedSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntFanSpeedTrap.setStatus(
        "current"
    )

chkpntVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 3, 1)
)
chkpntVoltageTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "voltageSensorName"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "voltageSensorValue"))
)
if mibBuilder.loadTexts:
    chkpntVoltageTrap.setStatus(
        "current"
    )

chkpntPowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 5, 4, 1)
)
chkpntPowerSupplyTrap.setObjects(
      *(("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "powerSupplySensorName"),
        ("CHECKPOINT-GAIA-TRAP-MIB", "powerSupplySensorValue"))
)
if mibBuilder.loadTexts:
    chkpntPowerSupplyTrap.setStatus(
        "current"
    )

chkpntSystemConfigurationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1, 1)
)
chkpntSystemConfigurationChangeTrap.setObjects(
    ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText")
)
if mibBuilder.loadTexts:
    chkpntSystemConfigurationChangeTrap.setStatus(
        "current"
    )

chkpntSystemConfigurationSaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3000, 10, 1, 2)
)
chkpntSystemConfigurationSaveTrap.setObjects(
    ("CHECKPOINT-GAIA-TRAP-MIB", "chkpntTrapMsgText")
)
if mibBuilder.loadTexts:
    chkpntSystemConfigurationSaveTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECKPOINT-GAIA-TRAP-MIB",
    **{"DisplayString": DisplayString,
       "checkpoint": checkpoint,
       "products": products,
       "svn": svn,
       "svnPerf": svnPerf,
       "raidInfo": raidInfo,
       "raidVolumeTable": raidVolumeTable,
       "raidVolumeEntry": raidVolumeEntry,
       "raidVolumeState": raidVolumeState,
       "raidVolumeFlags": raidVolumeFlags,
       "sensorInfo": sensorInfo,
       "tempertureSensorTable": tempertureSensorTable,
       "tempertureSensorEntry": tempertureSensorEntry,
       "tempertureSensorName": tempertureSensorName,
       "tempertureSensorValue": tempertureSensorValue,
       "fanSpeedSensorTable": fanSpeedSensorTable,
       "fanSpeedSensorEntry": fanSpeedSensorEntry,
       "fanSpeedSensorName": fanSpeedSensorName,
       "fanSpeedSensorValue": fanSpeedSensorValue,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorName": voltageSensorName,
       "voltageSensorValue": voltageSensorValue,
       "powerSupplyInfo": powerSupplyInfo,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplySensorName": powerSupplySensorName,
       "powerSupplySensorValue": powerSupplySensorValue,
       "chkpntTrap": chkpntTrap,
       "chkpntTrapInfo": chkpntTrapInfo,
       "chkpntTrapMibModule": chkpntTrapMibModule,
       "chkpntTrapOID": chkpntTrapOID,
       "chkpntTrapMsgText": chkpntTrapMsgText,
       "chkpntTrapDisk": chkpntTrapDisk,
       "chkpntTrapRAID": chkpntTrapRAID,
       "chkpntRAIDVolumeStateTrap": chkpntRAIDVolumeStateTrap,
       "chkpntTrapHWSensor": chkpntTrapHWSensor,
       "chkpntTrapTempertureSensor": chkpntTrapTempertureSensor,
       "chkpntTempertureTrap": chkpntTempertureTrap,
       "chkpntTrapFanSpeedSensor": chkpntTrapFanSpeedSensor,
       "chkpntFanSpeedTrap": chkpntFanSpeedTrap,
       "chkpntTrapVoltageSensor": chkpntTrapVoltageSensor,
       "chkpntVoltageTrap": chkpntVoltageTrap,
       "chkpntTrapPowerSupplySensor": chkpntTrapPowerSupplySensor,
       "chkpntPowerSupplyTrap": chkpntPowerSupplyTrap,
       "chkpntTrapConfiguration": chkpntTrapConfiguration,
       "chkpntTrapSystemConfiguration": chkpntTrapSystemConfiguration,
       "chkpntSystemConfigurationChangeTrap": chkpntSystemConfigurationChangeTrap,
       "chkpntSystemConfigurationSaveTrap": chkpntSystemConfigurationSaveTrap}
)
