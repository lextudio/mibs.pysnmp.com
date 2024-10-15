# SNMP MIB module (POSEIDON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POSEIDON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:19 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class OnOff(Integer32):
    """Custom type OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )





class OutputType(Integer32):
    """Custom type OutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 2),
          ("onOff", 0),
          ("rts", 1))
    )





class OutputMode(Integer32):
    """Custom type OutputMode based on Integer32"""
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
        *(("autoAlarm", 1),
          ("autoTriggerEq", 2),
          ("autoTriggerHi", 3),
          ("autoTriggerLo", 4),
          ("manual", 0))
    )





class UnitType(Integer32):
    """Custom type UnitType based on Integer32"""
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
        *(("absoluteHumidity", 10),
          ("celsius", 0),
          ("dewPoint", 9),
          ("fahrenheit", 1),
          ("kelvin", 2),
          ("miliAmper", 5),
          ("noUnit", 6),
          ("percent", 3),
          ("pressure", 11),
          ("pulse", 7),
          ("switch", 8),
          ("universal", 12),
          ("volt", 4))
    )





class InputAlarmSetup(Integer32):
    """Custom type InputAlarmSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeOff", 1),
          ("activeOn", 2),
          ("inactive", 0))
    )





class InputAlarmState(Integer32):
    """Custom type InputAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )





class SensorState(Integer32):
    """Custom type SensorState based on Integer32"""
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
        *(("alarm", 3),
          ("alarmstate", 2),
          ("invalid", 0),
          ("normal", 1))
    )





class SensorID(Integer32):
    """Custom type SensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class IOName(DisplayString):
    """Custom type IOName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )





class SensorName(DisplayString):
    """Custom type SensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )





class SensorValue(Integer32):
    """Custom type SensorValue based on Integer32"""




class SensorString(DisplayString):
    """Custom type SensorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )





class SensorUnitString(DisplayString):
    """Custom type SensorUnitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )





class SensorFlags(Integer32):
    """Custom type SensorFlags based on Integer32"""




class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hwgroup_ObjectIdentity = ObjectIdentity
hwgroup = _Hwgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796)
)
_CharonII_ObjectIdentity = ObjectIdentity
charonII = _CharonII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3)
)
_Poseidon_ObjectIdentity = ObjectIdentity
poseidon = _Poseidon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3)
)
_InpTable_Object = MibTable
inpTable = _InpTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1)
)
if mibBuilder.loadTexts:
    inpTable.setStatus("current")
_InpEntry_Object = MibTableRow
inpEntry = _InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1)
)
inpEntry.setIndexNames(
    (0, "POSEIDON-MIB", "inpIndex"),
)
if mibBuilder.loadTexts:
    inpEntry.setStatus("current")
_InpIndex_Type = PositiveInteger
_InpIndex_Object = MibTableColumn
inpIndex = _InpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 1),
    _InpIndex_Type()
)
inpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inpIndex.setStatus("current")
_InpValue_Type = OnOff
_InpValue_Object = MibTableColumn
inpValue = _InpValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 2),
    _InpValue_Type()
)
inpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpValue.setStatus("current")
_InpName_Type = IOName
_InpName_Object = MibTableColumn
inpName = _InpName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 3),
    _InpName_Type()
)
inpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inpName.setStatus("current")
_InpAlarmSetup_Type = InputAlarmSetup
_InpAlarmSetup_Object = MibTableColumn
inpAlarmSetup = _InpAlarmSetup_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 4),
    _InpAlarmSetup_Type()
)
inpAlarmSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inpAlarmSetup.setStatus("current")
_InpAlarmState_Type = InputAlarmState
_InpAlarmState_Object = MibTableColumn
inpAlarmState = _InpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 5),
    _InpAlarmState_Type()
)
inpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpAlarmState.setStatus("current")
_OutTable_Object = MibTable
outTable = _OutTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2)
)
if mibBuilder.loadTexts:
    outTable.setStatus("current")
_OutEntry_Object = MibTableRow
outEntry = _OutEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1)
)
outEntry.setIndexNames(
    (0, "POSEIDON-MIB", "outIndex"),
)
if mibBuilder.loadTexts:
    outEntry.setStatus("current")
_OutIndex_Type = PositiveInteger
_OutIndex_Object = MibTableColumn
outIndex = _OutIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 1),
    _OutIndex_Type()
)
outIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outIndex.setStatus("current")
_OutValue_Type = OnOff
_OutValue_Object = MibTableColumn
outValue = _OutValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 2),
    _OutValue_Type()
)
outValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outValue.setStatus("current")
_OutName_Type = IOName
_OutName_Object = MibTableColumn
outName = _OutName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 3),
    _OutName_Type()
)
outName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outName.setStatus("current")
_OutType_Type = OutputType
_OutType_Object = MibTableColumn
outType = _OutType_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 4),
    _OutType_Type()
)
outType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outType.setStatus("current")
_OutMode_Type = OutputMode
_OutMode_Object = MibTableColumn
outMode = _OutMode_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 5),
    _OutMode_Type()
)
outMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outMode.setStatus("current")
_SensTable_Object = MibTable
sensTable = _SensTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3)
)
if mibBuilder.loadTexts:
    sensTable.setStatus("current")
_SensEntry_Object = MibTableRow
sensEntry = _SensEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1)
)
sensEntry.setIndexNames(
    (0, "POSEIDON-MIB", "sensIndex"),
)
if mibBuilder.loadTexts:
    sensEntry.setStatus("current")
_SensIndex_Type = PositiveInteger
_SensIndex_Object = MibTableColumn
sensIndex = _SensIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 1),
    _SensIndex_Type()
)
sensIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensIndex.setStatus("current")
_SensName_Type = SensorName
_SensName_Object = MibTableColumn
sensName = _SensName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 2),
    _SensName_Type()
)
sensName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensName.setStatus("current")
_SensState_Type = SensorState
_SensState_Object = MibTableColumn
sensState = _SensState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 4),
    _SensState_Type()
)
sensState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensState.setStatus("current")
_SensString_Type = SensorString
_SensString_Object = MibTableColumn
sensString = _SensString_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 5),
    _SensString_Type()
)
sensString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensString.setStatus("current")
_SensValue_Type = SensorValue
_SensValue_Object = MibTableColumn
sensValue = _SensValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 6),
    _SensValue_Type()
)
sensValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensValue.setStatus("current")
_SensValueRaw_Type = SensorValue
_SensValueRaw_Object = MibTableColumn
sensValueRaw = _SensValueRaw_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 7),
    _SensValueRaw_Type()
)
sensValueRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensValueRaw.setStatus("current")
_SensID_Type = SensorID
_SensID_Object = MibTableColumn
sensID = _SensID_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 8),
    _SensID_Type()
)
sensID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensID.setStatus("current")
_SensUnit_Type = UnitType
_SensUnit_Object = MibTableColumn
sensUnit = _SensUnit_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 9),
    _SensUnit_Type()
)
sensUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensUnit.setStatus("current")
_SensUnitString_Type = SensorUnitString
_SensUnitString_Object = MibTableColumn
sensUnitString = _SensUnitString_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 10),
    _SensUnitString_Type()
)
sensUnitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensUnitString.setStatus("current")
_TsAlarm_ObjectIdentity = ObjectIdentity
tsAlarm = _TsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50)
)
_TsAlarmsPresent_Type = Gauge32
_TsAlarmsPresent_Object = MibScalar
tsAlarmsPresent = _TsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 1),
    _TsAlarmsPresent_Type()
)
tsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAlarmsPresent.setStatus("current")
_TsAlarmTable_Object = MibTable
tsAlarmTable = _TsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2)
)
if mibBuilder.loadTexts:
    tsAlarmTable.setStatus("current")
_TsAlarmEntry_Object = MibTableRow
tsAlarmEntry = _TsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1)
)
tsAlarmEntry.setIndexNames(
    (0, "POSEIDON-MIB", "tsAlarmIdx"),
)
if mibBuilder.loadTexts:
    tsAlarmEntry.setStatus("current")
_TsAlarmIdx_Type = PositiveInteger
_TsAlarmIdx_Object = MibTableColumn
tsAlarmIdx = _TsAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 1),
    _TsAlarmIdx_Type()
)
tsAlarmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsAlarmIdx.setStatus("current")
_TsAlarmId_Type = PositiveInteger
_TsAlarmId_Object = MibTableColumn
tsAlarmId = _TsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 2),
    _TsAlarmId_Type()
)
tsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAlarmId.setStatus("current")


class _TsAlarmDescr_Type(Integer32):
    """Custom type tsAlarmDescr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputStateAlarm", 1),
          ("temperatureOutOfRange", 2))
    )


_TsAlarmDescr_Type.__name__ = "Integer32"
_TsAlarmDescr_Object = MibTableColumn
tsAlarmDescr = _TsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 3),
    _TsAlarmDescr_Type()
)
tsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAlarmDescr.setStatus("current")
_TsAlarmSensName_Type = SensorName
_TsAlarmSensName_Object = MibTableColumn
tsAlarmSensName = _TsAlarmSensName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 4),
    _TsAlarmSensName_Type()
)
tsAlarmSensName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAlarmSensName.setStatus("current")
_TsAlarmTime_Type = TimeStamp
_TsAlarmTime_Object = MibTableColumn
tsAlarmTime = _TsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 5),
    _TsAlarmTime_Type()
)
tsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAlarmTime.setStatus("current")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 70)
)


class _InfoAddressMAC_Type(DisplayString):
    """Custom type infoAddressMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_InfoAddressMAC_Type.__name__ = "DisplayString"
_InfoAddressMAC_Object = MibScalar
infoAddressMAC = _InfoAddressMAC_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 70, 1),
    _InfoAddressMAC_Type()
)
infoAddressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAddressMAC.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99)
)
_SensSetup_ObjectIdentity = ObjectIdentity
sensSetup = _SensSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1)
)
_UnitType_Type = UnitType
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 1),
    _UnitType_Type()
)
unitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitType.setStatus("current")
_SensSetupTable_Object = MibTable
sensSetupTable = _SensSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2)
)
if mibBuilder.loadTexts:
    sensSetupTable.setStatus("current")
_SensSetupEntry_Object = MibTableRow
sensSetupEntry = _SensSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1)
)
sensSetupEntry.setIndexNames(
    (0, "POSEIDON-MIB", "sensSetupIndex"),
)
if mibBuilder.loadTexts:
    sensSetupEntry.setStatus("current")
_SensSetupIndex_Type = PositiveInteger
_SensSetupIndex_Object = MibTableColumn
sensSetupIndex = _SensSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 1),
    _SensSetupIndex_Type()
)
sensSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensSetupIndex.setStatus("current")
_SensSetupName_Type = SensorName
_SensSetupName_Object = MibTableColumn
sensSetupName = _SensSetupName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 2),
    _SensSetupName_Type()
)
sensSetupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensSetupName.setStatus("current")
_SensFlags_Type = SensorFlags
_SensFlags_Object = MibTableColumn
sensFlags = _SensFlags_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 5),
    _SensFlags_Type()
)
sensFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensFlags.setStatus("current")
_SensLimitMin_Type = SensorValue
_SensLimitMin_Object = MibTableColumn
sensLimitMin = _SensLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 6),
    _SensLimitMin_Type()
)
sensLimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensLimitMin.setStatus("current")
_SensLimitMax_Type = SensorValue
_SensLimitMax_Object = MibTableColumn
sensLimitMax = _SensLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 7),
    _SensLimitMax_Type()
)
sensLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensLimitMax.setStatus("current")
_SensHysteresis_Type = SensorValue
_SensHysteresis_Object = MibTableColumn
sensHysteresis = _SensHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 8),
    _SensHysteresis_Type()
)
sensHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensHysteresis.setStatus("current")

# Managed Objects groups


# Notification objects

inpAlarmStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 0, 1)
)
inpAlarmStateChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("POSEIDON-MIB", "infoAddressMAC"),
        ("POSEIDON-MIB", "inpName"),
        ("POSEIDON-MIB", "inpValue"),
        ("POSEIDON-MIB", "inpAlarmState"))
)
if mibBuilder.loadTexts:
    inpAlarmStateChanged.setStatus(
        ""
    )

sensAlarmStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 0, 2)
)
sensAlarmStateChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("POSEIDON-MIB", "infoAddressMAC"),
        ("POSEIDON-MIB", "sensName"),
        ("POSEIDON-MIB", "sensID"),
        ("POSEIDON-MIB", "sensState"),
        ("POSEIDON-MIB", "sensValue"),
        ("POSEIDON-MIB", "sensUnit"))
)
if mibBuilder.loadTexts:
    sensAlarmStateChanged.setStatus(
        ""
    )

tsTrapAlarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 0, 3)
)
tsTrapAlarmStart.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("POSEIDON-MIB", "infoAddressMAC"),
        ("POSEIDON-MIB", "tsAlarmId"),
        ("POSEIDON-MIB", "tsAlarmDescr"))
)
if mibBuilder.loadTexts:
    tsTrapAlarmStart.setStatus(
        ""
    )

tsTrapAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 3, 3, 0, 4)
)
tsTrapAlarmEnd.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("POSEIDON-MIB", "infoAddressMAC"),
        ("POSEIDON-MIB", "tsAlarmId"),
        ("POSEIDON-MIB", "tsAlarmDescr"))
)
if mibBuilder.loadTexts:
    tsTrapAlarmEnd.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POSEIDON-MIB",
    **{"PositiveInteger": PositiveInteger,
       "OnOff": OnOff,
       "OutputType": OutputType,
       "OutputMode": OutputMode,
       "UnitType": UnitType,
       "InputAlarmSetup": InputAlarmSetup,
       "InputAlarmState": InputAlarmState,
       "SensorState": SensorState,
       "SensorID": SensorID,
       "IOName": IOName,
       "SensorName": SensorName,
       "SensorValue": SensorValue,
       "SensorString": SensorString,
       "SensorUnitString": SensorUnitString,
       "SensorFlags": SensorFlags,
       "TimeStamp": TimeStamp,
       "hwgroup": hwgroup,
       "charonII": charonII,
       "poseidon": poseidon,
       "inpAlarmStateChanged": inpAlarmStateChanged,
       "sensAlarmStateChanged": sensAlarmStateChanged,
       "tsTrapAlarmStart": tsTrapAlarmStart,
       "tsTrapAlarmEnd": tsTrapAlarmEnd,
       "inpTable": inpTable,
       "inpEntry": inpEntry,
       "inpIndex": inpIndex,
       "inpValue": inpValue,
       "inpName": inpName,
       "inpAlarmSetup": inpAlarmSetup,
       "inpAlarmState": inpAlarmState,
       "outTable": outTable,
       "outEntry": outEntry,
       "outIndex": outIndex,
       "outValue": outValue,
       "outName": outName,
       "outType": outType,
       "outMode": outMode,
       "sensTable": sensTable,
       "sensEntry": sensEntry,
       "sensIndex": sensIndex,
       "sensName": sensName,
       "sensState": sensState,
       "sensString": sensString,
       "sensValue": sensValue,
       "sensValueRaw": sensValueRaw,
       "sensID": sensID,
       "sensUnit": sensUnit,
       "sensUnitString": sensUnitString,
       "tsAlarm": tsAlarm,
       "tsAlarmsPresent": tsAlarmsPresent,
       "tsAlarmTable": tsAlarmTable,
       "tsAlarmEntry": tsAlarmEntry,
       "tsAlarmIdx": tsAlarmIdx,
       "tsAlarmId": tsAlarmId,
       "tsAlarmDescr": tsAlarmDescr,
       "tsAlarmSensName": tsAlarmSensName,
       "tsAlarmTime": tsAlarmTime,
       "info": info,
       "infoAddressMAC": infoAddressMAC,
       "setup": setup,
       "sensSetup": sensSetup,
       "unitType": unitType,
       "sensSetupTable": sensSetupTable,
       "sensSetupEntry": sensSetupEntry,
       "sensSetupIndex": sensSetupIndex,
       "sensSetupName": sensSetupName,
       "sensFlags": sensFlags,
       "sensLimitMin": sensLimitMin,
       "sensLimitMax": sensLimitMax,
       "sensHysteresis": sensHysteresis}
)
