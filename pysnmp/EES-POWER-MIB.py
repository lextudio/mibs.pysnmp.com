# SNMP MIB module (EES-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EES-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:36 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

powerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 10),
          ("major", 6),
          ("minor", 5),
          ("normal", 2),
          ("observation", 3),
          ("restricted", 8),
          ("testing", 9),
          ("unknown", 1),
          ("unmanaged", 7),
          ("warning", 4))
    )



class StatusChange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Ees_ObjectIdentity = ObjectIdentity
ees = _Ees_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentControllerFirmwareVersion_Type = DisplayString
_IdentControllerFirmwareVersion_Object = MibScalar
identControllerFirmwareVersion = _IdentControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 3),
    _IdentControllerFirmwareVersion_Type()
)
identControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identControllerFirmwareVersion.setStatus("current")
_IdentName_Type = DisplayString
_IdentName_Object = MibScalar
identName = _IdentName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 4),
    _IdentName_Type()
)
identName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identName.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_SystemVoltage_Type = Integer32
_SystemVoltage_Object = MibScalar
systemVoltage = _SystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 2),
    _SystemVoltage_Type()
)
systemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoltage.setStatus("current")
_SystemCurrent_Type = Integer32
_SystemCurrent_Object = MibScalar
systemCurrent = _SystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 3),
    _SystemCurrent_Type()
)
systemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrent.setStatus("current")
_SystemUsedCapacity_Type = Integer32
_SystemUsedCapacity_Object = MibScalar
systemUsedCapacity = _SystemUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 4),
    _SystemUsedCapacity_Type()
)
systemUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedCapacity.setStatus("current")
_PsBattery_ObjectIdentity = ObjectIdentity
psBattery = _PsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5)
)
_PsBatteryVoltage_Type = Integer32
_PsBatteryVoltage_Object = MibScalar
psBatteryVoltage = _PsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 1),
    _PsBatteryVoltage_Type()
)
psBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryVoltage.setStatus("current")
_PsBatteryCurrent_Type = Integer32
_PsBatteryCurrent_Object = MibScalar
psBatteryCurrent = _PsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 2),
    _PsBatteryCurrent_Type()
)
psBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCurrent.setStatus("current")
_PsInput_ObjectIdentity = ObjectIdentity
psInput = _PsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6)
)
_PsInputLineAVoltage_Type = Integer32
_PsInputLineAVoltage_Object = MibScalar
psInputLineAVoltage = _PsInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 1),
    _PsInputLineAVoltage_Type()
)
psInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineAVoltage.setStatus("current")
_PsInputLineBVoltage_Type = Integer32
_PsInputLineBVoltage_Object = MibScalar
psInputLineBVoltage = _PsInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 2),
    _PsInputLineBVoltage_Type()
)
psInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineBVoltage.setStatus("current")
_PsInputLineCVoltage_Type = Integer32
_PsInputLineCVoltage_Object = MibScalar
psInputLineCVoltage = _PsInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 3),
    _PsInputLineCVoltage_Type()
)
psInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineCVoltage.setStatus("current")
_PsTemperature_ObjectIdentity = ObjectIdentity
psTemperature = _PsTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7)
)
_PsTemperature1_Type = Integer32
_PsTemperature1_Object = MibScalar
psTemperature1 = _PsTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 1),
    _PsTemperature1_Type()
)
psTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature1.setStatus("current")
_PsTemperature2_Type = Integer32
_PsTemperature2_Object = MibScalar
psTemperature2 = _PsTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 2),
    _PsTemperature2_Type()
)
psTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature2.setStatus("current")


class _PsStatusCommunication_Type(Integer32):
    """Custom type psStatusCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interrupt", 3),
          ("normal", 2),
          ("unknown", 1))
    )


_PsStatusCommunication_Type.__name__ = "Integer32"
_PsStatusCommunication_Object = MibScalar
psStatusCommunication = _PsStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 8),
    _PsStatusCommunication_Type()
)
psStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusCommunication.setStatus("current")


class _PsStatusBatteryMode_Type(Integer32):
    """Custom type psStatusBatteryMode based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ACFail", 8),
          ("ACFailTesting", 7),
          ("AutoBC", 10),
          ("BCForTest", 4),
          ("CyclicBC", 11),
          ("FloatCharging", 2),
          ("ManualBC", 9),
          ("ManualTesting", 5),
          ("MasterBC", 12),
          ("MasterBT", 13),
          ("PlanTesting", 6),
          ("ShortTest", 3),
          ("unknown", 1))
    )


_PsStatusBatteryMode_Type.__name__ = "Integer32"
_PsStatusBatteryMode_Object = MibScalar
psStatusBatteryMode = _PsStatusBatteryMode_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 9),
    _PsStatusBatteryMode_Type()
)
psStatusBatteryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusBatteryMode.setStatus("current")
_PsSMNumber_ObjectIdentity = ObjectIdentity
psSMNumber = _PsSMNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10)
)
_PsSMACNumber_Type = Integer32
_PsSMACNumber_Object = MibScalar
psSMACNumber = _PsSMACNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 1),
    _PsSMACNumber_Type()
)
psSMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMACNumber.setStatus("current")
_PsSMBATNumber_Type = Integer32
_PsSMBATNumber_Object = MibScalar
psSMBATNumber = _PsSMBATNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 2),
    _PsSMBATNumber_Type()
)
psSMBATNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMBATNumber.setStatus("current")
_PsSMIONumber_Type = Integer32
_PsSMIONumber_Object = MibScalar
psSMIONumber = _PsSMIONumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 3),
    _PsSMIONumber_Type()
)
psSMIONumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMIONumber.setStatus("current")
_AlarmLastTrapNo_Type = Counter32
_AlarmLastTrapNo_Object = MibScalar
alarmLastTrapNo = _AlarmLastTrapNo_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 3),
    _AlarmLastTrapNo_Type()
)
alarmLastTrapNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLastTrapNo.setStatus("current")
_AlarmTrapTable_Object = MibTable
alarmTrapTable = _AlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alarmTrapTable.setStatus("current")
_AlarmTrapEntry_Object = MibTableRow
alarmTrapEntry = _AlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1)
)
alarmTrapEntry.setIndexNames(
    (0, "EES-POWER-MIB", "alarmTrapNo"),
)
if mibBuilder.loadTexts:
    alarmTrapEntry.setStatus("current")
_AlarmTrapNo_Type = Counter32
_AlarmTrapNo_Object = MibTableColumn
alarmTrapNo = _AlarmTrapNo_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 1),
    _AlarmTrapNo_Type()
)
alarmTrapNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrapNo.setStatus("current")
_AlarmTime_Type = DateAndTime
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmType_Type = Integer32
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 6),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_PowerEvents_ObjectIdentity = ObjectIdentity
powerEvents = _PowerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5)
)

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 1)
)
alarmTrap.setObjects(
      *(("EES-POWER-MIB", "alarmTrapNo"),
        ("EES-POWER-MIB", "alarmTime"),
        ("EES-POWER-MIB", "alarmStatusChange"),
        ("EES-POWER-MIB", "alarmSeverity"),
        ("EES-POWER-MIB", "alarmDescription"),
        ("EES-POWER-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EES-POWER-MIB",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "ees": ees,
       "global": _pysmi_global,
       "powerMIB": powerMIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identControllerFirmwareVersion": identControllerFirmwareVersion,
       "identName": identName,
       "system": system,
       "systemStatus": systemStatus,
       "systemVoltage": systemVoltage,
       "systemCurrent": systemCurrent,
       "systemUsedCapacity": systemUsedCapacity,
       "psBattery": psBattery,
       "psBatteryVoltage": psBatteryVoltage,
       "psBatteryCurrent": psBatteryCurrent,
       "psInput": psInput,
       "psInputLineAVoltage": psInputLineAVoltage,
       "psInputLineBVoltage": psInputLineBVoltage,
       "psInputLineCVoltage": psInputLineCVoltage,
       "psTemperature": psTemperature,
       "psTemperature1": psTemperature1,
       "psTemperature2": psTemperature2,
       "psStatusCommunication": psStatusCommunication,
       "psStatusBatteryMode": psStatusBatteryMode,
       "psSMNumber": psSMNumber,
       "psSMACNumber": psSMACNumber,
       "psSMBATNumber": psSMBATNumber,
       "psSMIONumber": psSMIONumber,
       "alarmLastTrapNo": alarmLastTrapNo,
       "alarmTrapTable": alarmTrapTable,
       "alarmTrapEntry": alarmTrapEntry,
       "alarmTrapNo": alarmTrapNo,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmType": alarmType,
       "powerEvents": powerEvents,
       "alarmTrap": alarmTrap}
)
