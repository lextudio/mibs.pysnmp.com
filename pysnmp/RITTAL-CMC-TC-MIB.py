# SNMP MIB module (RITTAL-CMC-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RITTAL-CMC-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:40 2024
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

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rittal_ObjectIdentity = ObjectIdentity
rittal = _Rittal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606)
)
_CmcTc_ObjectIdentity = ObjectIdentity
cmcTc = _CmcTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4)
)
_CmcTcMibRev_ObjectIdentity = ObjectIdentity
cmcTcMibRev = _CmcTcMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 1)
)


class _CmcTcMibMajRev_Type(Integer32):
    """Custom type cmcTcMibMajRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcTcMibMajRev_Type.__name__ = "Integer32"
_CmcTcMibMajRev_Object = MibScalar
cmcTcMibMajRev = _CmcTcMibMajRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 1, 1),
    _CmcTcMibMajRev_Type()
)
cmcTcMibMajRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcMibMajRev.setStatus("mandatory")


class _CmcTcMibMinRev_Type(Integer32):
    """Custom type cmcTcMibMinRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmcTcMibMinRev_Type.__name__ = "Integer32"
_CmcTcMibMinRev_Object = MibScalar
cmcTcMibMinRev = _CmcTcMibMinRev_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 1, 2),
    _CmcTcMibMinRev_Type()
)
cmcTcMibMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcMibMinRev.setStatus("mandatory")


class _CmcTcMibCondition_Type(Integer32):
    """Custom type cmcTcMibCondition based on Integer32"""
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
        *(("configChanged", 5),
          ("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CmcTcMibCondition_Type.__name__ = "Integer32"
_CmcTcMibCondition_Object = MibScalar
cmcTcMibCondition = _CmcTcMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 1, 3),
    _CmcTcMibCondition_Type()
)
cmcTcMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcMibCondition.setStatus("mandatory")
_CmcTcStatus_ObjectIdentity = ObjectIdentity
cmcTcStatus = _CmcTcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2)
)


class _CmcTcStatusDeviceCMC_Type(Integer32):
    """Custom type cmcTcStatusDeviceCMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_CmcTcStatusDeviceCMC_Type.__name__ = "Integer32"
_CmcTcStatusDeviceCMC_Object = MibScalar
cmcTcStatusDeviceCMC = _CmcTcStatusDeviceCMC_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 1),
    _CmcTcStatusDeviceCMC_Type()
)
cmcTcStatusDeviceCMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcStatusDeviceCMC.setStatus("mandatory")
_CmcTcUnitsConnected_Type = Integer32
_CmcTcUnitsConnected_Object = MibScalar
cmcTcUnitsConnected = _CmcTcUnitsConnected_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 2),
    _CmcTcUnitsConnected_Type()
)
cmcTcUnitsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnitsConnected.setStatus("mandatory")
_CmcTcStatusSensorUnit1_ObjectIdentity = ObjectIdentity
cmcTcStatusSensorUnit1 = _CmcTcStatusSensorUnit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3)
)


class _CmcTcUnit1TypeOfDevice_Type(Integer32):
    """Custom type cmcTcUnit1TypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitAccess", 3),
          ("unitClimate", 4),
          ("unitFCS", 5),
          ("unitIO", 2),
          ("unitRTT", 6))
    )


_CmcTcUnit1TypeOfDevice_Type.__name__ = "Integer32"
_CmcTcUnit1TypeOfDevice_Object = MibScalar
cmcTcUnit1TypeOfDevice = _CmcTcUnit1TypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 1),
    _CmcTcUnit1TypeOfDevice_Type()
)
cmcTcUnit1TypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1TypeOfDevice.setStatus("mandatory")


class _CmcTcUnit1Text_Type(DisplayString):
    """Custom type cmcTcUnit1Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcTcUnit1Text_Type.__name__ = "DisplayString"
_CmcTcUnit1Text_Object = MibScalar
cmcTcUnit1Text = _CmcTcUnit1Text_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 2),
    _CmcTcUnit1Text_Type()
)
cmcTcUnit1Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcUnit1Text.setStatus("mandatory")
_CmcTcUnit1Serial_Type = Integer32
_CmcTcUnit1Serial_Object = MibScalar
cmcTcUnit1Serial = _CmcTcUnit1Serial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 3),
    _CmcTcUnit1Serial_Type()
)
cmcTcUnit1Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1Serial.setStatus("mandatory")


class _CmcTcUnit1Status_Type(Integer32):
    """Custom type cmcTcUnit1Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("quit", 4),
          ("timeout", 5))
    )


_CmcTcUnit1Status_Type.__name__ = "Integer32"
_CmcTcUnit1Status_Object = MibScalar
cmcTcUnit1Status = _CmcTcUnit1Status_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 4),
    _CmcTcUnit1Status_Type()
)
cmcTcUnit1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1Status.setStatus("mandatory")
_CmcTcStatusUnit1Sensors_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit1Sensors = _CmcTcStatusUnit1Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5)
)
_CmcTcUnit1NumberOfSensors_Type = Integer32
_CmcTcUnit1NumberOfSensors_Object = MibScalar
cmcTcUnit1NumberOfSensors = _CmcTcUnit1NumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 1),
    _CmcTcUnit1NumberOfSensors_Type()
)
cmcTcUnit1NumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1NumberOfSensors.setStatus("mandatory")
_CmcTcUnit1SensorTable_Object = MibTable
cmcTcUnit1SensorTable = _CmcTcUnit1SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit1SensorTable.setStatus("mandatory")
_CmcTcUnit1SensorEntry_Object = MibTableRow
cmcTcUnit1SensorEntry = _CmcTcUnit1SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1)
)
cmcTcUnit1SensorEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit1SensorIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit1SensorEntry.setStatus("mandatory")


class _Unit1SensorIndex_Type(Integer32):
    """Custom type unit1SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit1SensorIndex_Type.__name__ = "Integer32"
_Unit1SensorIndex_Object = MibTableColumn
unit1SensorIndex = _Unit1SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 1),
    _Unit1SensorIndex_Type()
)
unit1SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorIndex.setStatus("mandatory")


class _Unit1SensorType_Type(Integer32):
    """Custom type unit1SensorType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("airFlow", 8),
          ("alarmRTT", 25),
          ("current4to20", 11),
          ("dutyPWM", 21),
          ("failure", 2),
          ("fanOK", 19),
          ("fanStatus", 22),
          ("filterRTT", 26),
          ("humidity", 12),
          ("leakage", 23),
          ("lock", 15),
          ("motion", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("readerKeypad", 20),
          ("smoke", 7),
          ("temperature", 10),
          ("type6", 9),
          ("unlock", 16),
          ("userNC", 14),
          ("userNO", 13),
          ("vibration", 5),
          ("voltOK", 17),
          ("voltage", 18),
          ("warningRTT", 24))
    )


_Unit1SensorType_Type.__name__ = "Integer32"
_Unit1SensorType_Object = MibTableColumn
unit1SensorType = _Unit1SensorType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 2),
    _Unit1SensorType_Type()
)
unit1SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorType.setStatus("mandatory")


class _Unit1SensorText_Type(DisplayString):
    """Custom type unit1SensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit1SensorText_Type.__name__ = "DisplayString"
_Unit1SensorText_Object = MibTableColumn
unit1SensorText = _Unit1SensorText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 3),
    _Unit1SensorText_Type()
)
unit1SensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1SensorText.setStatus("mandatory")


class _Unit1SensorStatus_Type(Integer32):
    """Custom type unit1SensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_Unit1SensorStatus_Type.__name__ = "Integer32"
_Unit1SensorStatus_Object = MibTableColumn
unit1SensorStatus = _Unit1SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 4),
    _Unit1SensorStatus_Type()
)
unit1SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorStatus.setStatus("mandatory")
_Unit1SensorValue_Type = Integer32
_Unit1SensorValue_Object = MibTableColumn
unit1SensorValue = _Unit1SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 5),
    _Unit1SensorValue_Type()
)
unit1SensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1SensorValue.setStatus("mandatory")
_Unit1SensorSetHigh_Type = Integer32
_Unit1SensorSetHigh_Object = MibTableColumn
unit1SensorSetHigh = _Unit1SensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 6),
    _Unit1SensorSetHigh_Type()
)
unit1SensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1SensorSetHigh.setStatus("mandatory")
_Unit1SensorSetLow_Type = Integer32
_Unit1SensorSetLow_Object = MibTableColumn
unit1SensorSetLow = _Unit1SensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 7),
    _Unit1SensorSetLow_Type()
)
unit1SensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1SensorSetLow.setStatus("mandatory")
_Unit1SensorSetWarn_Type = Integer32
_Unit1SensorSetWarn_Object = MibTableColumn
unit1SensorSetWarn = _Unit1SensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 5, 2, 1, 8),
    _Unit1SensorSetWarn_Type()
)
unit1SensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1SensorSetWarn.setStatus("mandatory")
_CmcTcStatusUnit1Outputs_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit1Outputs = _CmcTcStatusUnit1Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6)
)
_CmcTcUnit1NumberOfOutputs_Type = Integer32
_CmcTcUnit1NumberOfOutputs_Object = MibScalar
cmcTcUnit1NumberOfOutputs = _CmcTcUnit1NumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 1),
    _CmcTcUnit1NumberOfOutputs_Type()
)
cmcTcUnit1NumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1NumberOfOutputs.setStatus("mandatory")
_CmcTcUnit1OutputTable_Object = MibTable
cmcTcUnit1OutputTable = _CmcTcUnit1OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit1OutputTable.setStatus("mandatory")
_CmcTcUnit1OutputEntry_Object = MibTableRow
cmcTcUnit1OutputEntry = _CmcTcUnit1OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1)
)
cmcTcUnit1OutputEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit1OutputIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit1OutputEntry.setStatus("mandatory")


class _Unit1OutputIndex_Type(Integer32):
    """Custom type unit1OutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit1OutputIndex_Type.__name__ = "Integer32"
_Unit1OutputIndex_Object = MibTableColumn
unit1OutputIndex = _Unit1OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 1),
    _Unit1OutputIndex_Type()
)
unit1OutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutputIndex.setStatus("mandatory")


class _Unit1OutputType_Type(Integer32):
    """Custom type unit1OutputType based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doorLock", 4),
          ("doorLockFRi", 13),
          ("doorLockMaster", 12),
          ("failure", 2),
          ("fan", 7),
          ("fanSpeedContr", 8),
          ("notAvail", 1),
          ("overflow", 3),
          ("powerOut", 11),
          ("roomLock", 10),
          ("setpoint", 14),
          ("setpointTimax", 15),
          ("univLock1", 5),
          ("univLock2", 6),
          ("universalOut", 9))
    )


_Unit1OutputType_Type.__name__ = "Integer32"
_Unit1OutputType_Object = MibTableColumn
unit1OutputType = _Unit1OutputType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 2),
    _Unit1OutputType_Type()
)
unit1OutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1OutputType.setStatus("mandatory")


class _Unit1OutputText_Type(DisplayString):
    """Custom type unit1OutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit1OutputText_Type.__name__ = "DisplayString"
_Unit1OutputText_Object = MibTableColumn
unit1OutputText = _Unit1OutputText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 3),
    _Unit1OutputText_Type()
)
unit1OutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputText.setStatus("mandatory")


class _Unit1OutputStatus_Type(Integer32):
    """Custom type unit1OutputStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_Unit1OutputStatus_Type.__name__ = "Integer32"
_Unit1OutputStatus_Object = MibTableColumn
unit1OutputStatus = _Unit1OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 4),
    _Unit1OutputStatus_Type()
)
unit1OutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputStatus.setStatus("mandatory")
_Unit1OutputValue_Type = Integer32
_Unit1OutputValue_Object = MibTableColumn
unit1OutputValue = _Unit1OutputValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 5),
    _Unit1OutputValue_Type()
)
unit1OutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputValue.setStatus("mandatory")


class _Unit1OutputSet_Type(Integer32):
    """Custom type unit1OutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_Unit1OutputSet_Type.__name__ = "Integer32"
_Unit1OutputSet_Object = MibTableColumn
unit1OutputSet = _Unit1OutputSet_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 6),
    _Unit1OutputSet_Type()
)
unit1OutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputSet.setStatus("mandatory")


class _Unit1OutputConfig_Type(Integer32):
    """Custom type unit1OutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_Unit1OutputConfig_Type.__name__ = "Integer32"
_Unit1OutputConfig_Object = MibTableColumn
unit1OutputConfig = _Unit1OutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 7),
    _Unit1OutputConfig_Type()
)
unit1OutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputConfig.setStatus("mandatory")
_Unit1OutputDelay_Type = Integer32
_Unit1OutputDelay_Object = MibTableColumn
unit1OutputDelay = _Unit1OutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 8),
    _Unit1OutputDelay_Type()
)
unit1OutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputDelay.setStatus("mandatory")


class _Unit1OutputTimeoutAction_Type(Integer32):
    """Custom type unit1OutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_Unit1OutputTimeoutAction_Type.__name__ = "Integer32"
_Unit1OutputTimeoutAction_Object = MibTableColumn
unit1OutputTimeoutAction = _Unit1OutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 6, 2, 1, 9),
    _Unit1OutputTimeoutAction_Type()
)
unit1OutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1OutputTimeoutAction.setStatus("mandatory")
_CmcTcStatusUnit1Msg_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit1Msg = _CmcTcStatusUnit1Msg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7)
)
_CmcTcUnit1NumberOfMsgs_Type = Integer32
_CmcTcUnit1NumberOfMsgs_Object = MibScalar
cmcTcUnit1NumberOfMsgs = _CmcTcUnit1NumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 1),
    _CmcTcUnit1NumberOfMsgs_Type()
)
cmcTcUnit1NumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit1NumberOfMsgs.setStatus("mandatory")
_CmcTcUnit1MsgTable_Object = MibTable
cmcTcUnit1MsgTable = _CmcTcUnit1MsgTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit1MsgTable.setStatus("mandatory")
_CmcTcUnit1MsgEntry_Object = MibTableRow
cmcTcUnit1MsgEntry = _CmcTcUnit1MsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1)
)
cmcTcUnit1MsgEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit1MsgIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit1MsgEntry.setStatus("mandatory")


class _Unit1MsgIndex_Type(Integer32):
    """Custom type unit1MsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit1MsgIndex_Type.__name__ = "Integer32"
_Unit1MsgIndex_Object = MibTableColumn
unit1MsgIndex = _Unit1MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 1),
    _Unit1MsgIndex_Type()
)
unit1MsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1MsgIndex.setStatus("mandatory")


class _Unit1MsgText_Type(DisplayString):
    """Custom type unit1MsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit1MsgText_Type.__name__ = "DisplayString"
_Unit1MsgText_Object = MibTableColumn
unit1MsgText = _Unit1MsgText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 2),
    _Unit1MsgText_Type()
)
unit1MsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgText.setStatus("mandatory")


class _Unit1MsgStatus_Type(Integer32):
    """Custom type unit1MsgStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("closed", 12),
          ("configChanged", 2),
          ("error", 3),
          ("locked", 13),
          ("noAccess", 19),
          ("notAvail", 1),
          ("ok", 4),
          ("open", 11),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("unlReaderKeypad", 15),
          ("unlRemote", 14),
          ("unlSNMP", 16),
          ("unlTimer", 18),
          ("unlWEB", 17),
          ("warning", 6))
    )


_Unit1MsgStatus_Type.__name__ = "Integer32"
_Unit1MsgStatus_Object = MibTableColumn
unit1MsgStatus = _Unit1MsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 3),
    _Unit1MsgStatus_Type()
)
unit1MsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit1MsgStatus.setStatus("mandatory")


class _Unit1MsgRelay_Type(Integer32):
    """Custom type unit1MsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgRelay_Type.__name__ = "Integer32"
_Unit1MsgRelay_Object = MibTableColumn
unit1MsgRelay = _Unit1MsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 4),
    _Unit1MsgRelay_Type()
)
unit1MsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgRelay.setStatus("mandatory")


class _Unit1MsgBeeper_Type(Integer32):
    """Custom type unit1MsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgBeeper_Type.__name__ = "Integer32"
_Unit1MsgBeeper_Object = MibTableColumn
unit1MsgBeeper = _Unit1MsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 5),
    _Unit1MsgBeeper_Type()
)
unit1MsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgBeeper.setStatus("mandatory")


class _Unit1MsgTrap1_Type(Integer32):
    """Custom type unit1MsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgTrap1_Type.__name__ = "Integer32"
_Unit1MsgTrap1_Object = MibTableColumn
unit1MsgTrap1 = _Unit1MsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 6),
    _Unit1MsgTrap1_Type()
)
unit1MsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgTrap1.setStatus("mandatory")


class _Unit1MsgTrap2_Type(Integer32):
    """Custom type unit1MsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgTrap2_Type.__name__ = "Integer32"
_Unit1MsgTrap2_Object = MibTableColumn
unit1MsgTrap2 = _Unit1MsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 7),
    _Unit1MsgTrap2_Type()
)
unit1MsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgTrap2.setStatus("mandatory")


class _Unit1MsgTrap3_Type(Integer32):
    """Custom type unit1MsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgTrap3_Type.__name__ = "Integer32"
_Unit1MsgTrap3_Object = MibTableColumn
unit1MsgTrap3 = _Unit1MsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 8),
    _Unit1MsgTrap3_Type()
)
unit1MsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgTrap3.setStatus("mandatory")


class _Unit1MsgTrap4_Type(Integer32):
    """Custom type unit1MsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit1MsgTrap4_Type.__name__ = "Integer32"
_Unit1MsgTrap4_Object = MibTableColumn
unit1MsgTrap4 = _Unit1MsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 9),
    _Unit1MsgTrap4_Type()
)
unit1MsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgTrap4.setStatus("mandatory")


class _Unit1MsgQuit_Type(Integer32):
    """Custom type unit1MsgQuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Unit1MsgQuit_Type.__name__ = "Integer32"
_Unit1MsgQuit_Object = MibTableColumn
unit1MsgQuit = _Unit1MsgQuit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 3, 7, 2, 1, 10),
    _Unit1MsgQuit_Type()
)
unit1MsgQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit1MsgQuit.setStatus("mandatory")
_CmcTcStatusSensorUnit2_ObjectIdentity = ObjectIdentity
cmcTcStatusSensorUnit2 = _CmcTcStatusSensorUnit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4)
)


class _CmcTcUnit2TypeOfDevice_Type(Integer32):
    """Custom type cmcTcUnit2TypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitAccess", 3),
          ("unitClimate", 4),
          ("unitFCS", 5),
          ("unitIO", 2),
          ("unitRTT", 6))
    )


_CmcTcUnit2TypeOfDevice_Type.__name__ = "Integer32"
_CmcTcUnit2TypeOfDevice_Object = MibScalar
cmcTcUnit2TypeOfDevice = _CmcTcUnit2TypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 1),
    _CmcTcUnit2TypeOfDevice_Type()
)
cmcTcUnit2TypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2TypeOfDevice.setStatus("mandatory")


class _CmcTcUnit2Text_Type(DisplayString):
    """Custom type cmcTcUnit2Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcTcUnit2Text_Type.__name__ = "DisplayString"
_CmcTcUnit2Text_Object = MibScalar
cmcTcUnit2Text = _CmcTcUnit2Text_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 2),
    _CmcTcUnit2Text_Type()
)
cmcTcUnit2Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcUnit2Text.setStatus("mandatory")
_CmcTcUnit2Serial_Type = Integer32
_CmcTcUnit2Serial_Object = MibScalar
cmcTcUnit2Serial = _CmcTcUnit2Serial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 3),
    _CmcTcUnit2Serial_Type()
)
cmcTcUnit2Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2Serial.setStatus("mandatory")


class _CmcTcUnit2Status_Type(Integer32):
    """Custom type cmcTcUnit2Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("quit", 4),
          ("timeout", 5))
    )


_CmcTcUnit2Status_Type.__name__ = "Integer32"
_CmcTcUnit2Status_Object = MibScalar
cmcTcUnit2Status = _CmcTcUnit2Status_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 4),
    _CmcTcUnit2Status_Type()
)
cmcTcUnit2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2Status.setStatus("mandatory")
_CmcTcStatusUnit2Sensors_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit2Sensors = _CmcTcStatusUnit2Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5)
)
_CmcTcUnit2NumberOfSensors_Type = Integer32
_CmcTcUnit2NumberOfSensors_Object = MibScalar
cmcTcUnit2NumberOfSensors = _CmcTcUnit2NumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 1),
    _CmcTcUnit2NumberOfSensors_Type()
)
cmcTcUnit2NumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2NumberOfSensors.setStatus("mandatory")
_CmcTcUnit2SensorTable_Object = MibTable
cmcTcUnit2SensorTable = _CmcTcUnit2SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit2SensorTable.setStatus("mandatory")
_CmcTcUnit2SensorEntry_Object = MibTableRow
cmcTcUnit2SensorEntry = _CmcTcUnit2SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1)
)
cmcTcUnit2SensorEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit2SensorIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit2SensorEntry.setStatus("mandatory")


class _Unit2SensorIndex_Type(Integer32):
    """Custom type unit2SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit2SensorIndex_Type.__name__ = "Integer32"
_Unit2SensorIndex_Object = MibTableColumn
unit2SensorIndex = _Unit2SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 1),
    _Unit2SensorIndex_Type()
)
unit2SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorIndex.setStatus("mandatory")


class _Unit2SensorType_Type(Integer32):
    """Custom type unit2SensorType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("airFlow", 8),
          ("alarmRTT", 25),
          ("current4to20", 11),
          ("dutyPWM", 21),
          ("failure", 2),
          ("fanOK", 19),
          ("fanStatus", 22),
          ("filterRTT", 26),
          ("humidity", 12),
          ("leakage", 23),
          ("lock", 15),
          ("motion", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("readerKeypad", 20),
          ("smoke", 7),
          ("temperature", 10),
          ("type6", 9),
          ("unlock", 16),
          ("userNC", 14),
          ("userNO", 13),
          ("vibration", 5),
          ("voltOK", 17),
          ("voltage", 18),
          ("warningRTT", 24))
    )


_Unit2SensorType_Type.__name__ = "Integer32"
_Unit2SensorType_Object = MibTableColumn
unit2SensorType = _Unit2SensorType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 2),
    _Unit2SensorType_Type()
)
unit2SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorType.setStatus("mandatory")


class _Unit2SensorText_Type(DisplayString):
    """Custom type unit2SensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit2SensorText_Type.__name__ = "DisplayString"
_Unit2SensorText_Object = MibTableColumn
unit2SensorText = _Unit2SensorText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 3),
    _Unit2SensorText_Type()
)
unit2SensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2SensorText.setStatus("mandatory")


class _Unit2SensorStatus_Type(Integer32):
    """Custom type unit2SensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_Unit2SensorStatus_Type.__name__ = "Integer32"
_Unit2SensorStatus_Object = MibTableColumn
unit2SensorStatus = _Unit2SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 4),
    _Unit2SensorStatus_Type()
)
unit2SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorStatus.setStatus("mandatory")
_Unit2SensorValue_Type = Integer32
_Unit2SensorValue_Object = MibTableColumn
unit2SensorValue = _Unit2SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 5),
    _Unit2SensorValue_Type()
)
unit2SensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2SensorValue.setStatus("mandatory")
_Unit2SensorSetHigh_Type = Integer32
_Unit2SensorSetHigh_Object = MibTableColumn
unit2SensorSetHigh = _Unit2SensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 6),
    _Unit2SensorSetHigh_Type()
)
unit2SensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2SensorSetHigh.setStatus("mandatory")
_Unit2SensorSetLow_Type = Integer32
_Unit2SensorSetLow_Object = MibTableColumn
unit2SensorSetLow = _Unit2SensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 7),
    _Unit2SensorSetLow_Type()
)
unit2SensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2SensorSetLow.setStatus("mandatory")
_Unit2SensorSetWarn_Type = Integer32
_Unit2SensorSetWarn_Object = MibTableColumn
unit2SensorSetWarn = _Unit2SensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 5, 2, 1, 8),
    _Unit2SensorSetWarn_Type()
)
unit2SensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2SensorSetWarn.setStatus("mandatory")
_CmcTcStatusUnit2Outputs_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit2Outputs = _CmcTcStatusUnit2Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6)
)
_CmcTcUnit2NumberOfOutputs_Type = Integer32
_CmcTcUnit2NumberOfOutputs_Object = MibScalar
cmcTcUnit2NumberOfOutputs = _CmcTcUnit2NumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 1),
    _CmcTcUnit2NumberOfOutputs_Type()
)
cmcTcUnit2NumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2NumberOfOutputs.setStatus("mandatory")
_CmcTcUnit2OutputTable_Object = MibTable
cmcTcUnit2OutputTable = _CmcTcUnit2OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit2OutputTable.setStatus("mandatory")
_CmcTcUnit2OutputEntry_Object = MibTableRow
cmcTcUnit2OutputEntry = _CmcTcUnit2OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1)
)
cmcTcUnit2OutputEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit2OutputIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit2OutputEntry.setStatus("mandatory")


class _Unit2OutputIndex_Type(Integer32):
    """Custom type unit2OutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit2OutputIndex_Type.__name__ = "Integer32"
_Unit2OutputIndex_Object = MibTableColumn
unit2OutputIndex = _Unit2OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 1),
    _Unit2OutputIndex_Type()
)
unit2OutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutputIndex.setStatus("mandatory")


class _Unit2OutputType_Type(Integer32):
    """Custom type unit2OutputType based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doorLock", 4),
          ("doorLockFRi", 13),
          ("doorLockMaster", 12),
          ("failure", 2),
          ("fan", 7),
          ("fanSpeedContr", 8),
          ("notAvail", 1),
          ("overflow", 3),
          ("powerOut", 11),
          ("roomLock", 10),
          ("setpoint", 14),
          ("setpointTimax", 15),
          ("univLock1", 5),
          ("univLock2", 6),
          ("universalOut", 9))
    )


_Unit2OutputType_Type.__name__ = "Integer32"
_Unit2OutputType_Object = MibTableColumn
unit2OutputType = _Unit2OutputType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 2),
    _Unit2OutputType_Type()
)
unit2OutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2OutputType.setStatus("mandatory")


class _Unit2OutputText_Type(DisplayString):
    """Custom type unit2OutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit2OutputText_Type.__name__ = "DisplayString"
_Unit2OutputText_Object = MibTableColumn
unit2OutputText = _Unit2OutputText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 3),
    _Unit2OutputText_Type()
)
unit2OutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputText.setStatus("mandatory")


class _Unit2OutputStatus_Type(Integer32):
    """Custom type unit2OutputStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_Unit2OutputStatus_Type.__name__ = "Integer32"
_Unit2OutputStatus_Object = MibTableColumn
unit2OutputStatus = _Unit2OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 4),
    _Unit2OutputStatus_Type()
)
unit2OutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputStatus.setStatus("mandatory")
_Unit2OutputValue_Type = Integer32
_Unit2OutputValue_Object = MibTableColumn
unit2OutputValue = _Unit2OutputValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 5),
    _Unit2OutputValue_Type()
)
unit2OutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputValue.setStatus("mandatory")


class _Unit2OutputSet_Type(Integer32):
    """Custom type unit2OutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_Unit2OutputSet_Type.__name__ = "Integer32"
_Unit2OutputSet_Object = MibTableColumn
unit2OutputSet = _Unit2OutputSet_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 6),
    _Unit2OutputSet_Type()
)
unit2OutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputSet.setStatus("mandatory")


class _Unit2OutputConfig_Type(Integer32):
    """Custom type unit2OutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_Unit2OutputConfig_Type.__name__ = "Integer32"
_Unit2OutputConfig_Object = MibTableColumn
unit2OutputConfig = _Unit2OutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 7),
    _Unit2OutputConfig_Type()
)
unit2OutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputConfig.setStatus("mandatory")
_Unit2OutputDelay_Type = Integer32
_Unit2OutputDelay_Object = MibTableColumn
unit2OutputDelay = _Unit2OutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 8),
    _Unit2OutputDelay_Type()
)
unit2OutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputDelay.setStatus("mandatory")


class _Unit2OutputTimeoutAction_Type(Integer32):
    """Custom type unit2OutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_Unit2OutputTimeoutAction_Type.__name__ = "Integer32"
_Unit2OutputTimeoutAction_Object = MibTableColumn
unit2OutputTimeoutAction = _Unit2OutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 6, 2, 1, 9),
    _Unit2OutputTimeoutAction_Type()
)
unit2OutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2OutputTimeoutAction.setStatus("mandatory")
_CmcTcStatusUnit2Msg_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit2Msg = _CmcTcStatusUnit2Msg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7)
)
_CmcTcUnit2NumberOfMsgs_Type = Integer32
_CmcTcUnit2NumberOfMsgs_Object = MibScalar
cmcTcUnit2NumberOfMsgs = _CmcTcUnit2NumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 1),
    _CmcTcUnit2NumberOfMsgs_Type()
)
cmcTcUnit2NumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit2NumberOfMsgs.setStatus("mandatory")
_CmcTcUnit2MsgTable_Object = MibTable
cmcTcUnit2MsgTable = _CmcTcUnit2MsgTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit2MsgTable.setStatus("mandatory")
_CmcTcUnit2MsgEntry_Object = MibTableRow
cmcTcUnit2MsgEntry = _CmcTcUnit2MsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1)
)
cmcTcUnit2MsgEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit2MsgIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit2MsgEntry.setStatus("mandatory")


class _Unit2MsgIndex_Type(Integer32):
    """Custom type unit2MsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit2MsgIndex_Type.__name__ = "Integer32"
_Unit2MsgIndex_Object = MibTableColumn
unit2MsgIndex = _Unit2MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 1),
    _Unit2MsgIndex_Type()
)
unit2MsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2MsgIndex.setStatus("mandatory")


class _Unit2MsgText_Type(DisplayString):
    """Custom type unit2MsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit2MsgText_Type.__name__ = "DisplayString"
_Unit2MsgText_Object = MibTableColumn
unit2MsgText = _Unit2MsgText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 2),
    _Unit2MsgText_Type()
)
unit2MsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgText.setStatus("mandatory")


class _Unit2MsgStatus_Type(Integer32):
    """Custom type unit2MsgStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("closed", 12),
          ("configChanged", 2),
          ("error", 3),
          ("locked", 13),
          ("noAccess", 19),
          ("notAvail", 1),
          ("ok", 4),
          ("open", 11),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("unlReaderKeypad", 15),
          ("unlRemote", 14),
          ("unlSNMP", 16),
          ("unlTimer", 18),
          ("unlWEB", 17),
          ("warning", 6))
    )


_Unit2MsgStatus_Type.__name__ = "Integer32"
_Unit2MsgStatus_Object = MibTableColumn
unit2MsgStatus = _Unit2MsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 3),
    _Unit2MsgStatus_Type()
)
unit2MsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit2MsgStatus.setStatus("mandatory")


class _Unit2MsgRelay_Type(Integer32):
    """Custom type unit2MsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgRelay_Type.__name__ = "Integer32"
_Unit2MsgRelay_Object = MibTableColumn
unit2MsgRelay = _Unit2MsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 4),
    _Unit2MsgRelay_Type()
)
unit2MsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgRelay.setStatus("mandatory")


class _Unit2MsgBeeper_Type(Integer32):
    """Custom type unit2MsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgBeeper_Type.__name__ = "Integer32"
_Unit2MsgBeeper_Object = MibTableColumn
unit2MsgBeeper = _Unit2MsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 5),
    _Unit2MsgBeeper_Type()
)
unit2MsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgBeeper.setStatus("mandatory")


class _Unit2MsgTrap1_Type(Integer32):
    """Custom type unit2MsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgTrap1_Type.__name__ = "Integer32"
_Unit2MsgTrap1_Object = MibTableColumn
unit2MsgTrap1 = _Unit2MsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 6),
    _Unit2MsgTrap1_Type()
)
unit2MsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgTrap1.setStatus("mandatory")


class _Unit2MsgTrap2_Type(Integer32):
    """Custom type unit2MsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgTrap2_Type.__name__ = "Integer32"
_Unit2MsgTrap2_Object = MibTableColumn
unit2MsgTrap2 = _Unit2MsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 7),
    _Unit2MsgTrap2_Type()
)
unit2MsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgTrap2.setStatus("mandatory")


class _Unit2MsgTrap3_Type(Integer32):
    """Custom type unit2MsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgTrap3_Type.__name__ = "Integer32"
_Unit2MsgTrap3_Object = MibTableColumn
unit2MsgTrap3 = _Unit2MsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 8),
    _Unit2MsgTrap3_Type()
)
unit2MsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgTrap3.setStatus("mandatory")


class _Unit2MsgTrap4_Type(Integer32):
    """Custom type unit2MsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit2MsgTrap4_Type.__name__ = "Integer32"
_Unit2MsgTrap4_Object = MibTableColumn
unit2MsgTrap4 = _Unit2MsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 9),
    _Unit2MsgTrap4_Type()
)
unit2MsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgTrap4.setStatus("mandatory")


class _Unit2MsgQuit_Type(Integer32):
    """Custom type unit2MsgQuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Unit2MsgQuit_Type.__name__ = "Integer32"
_Unit2MsgQuit_Object = MibTableColumn
unit2MsgQuit = _Unit2MsgQuit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 4, 7, 2, 1, 10),
    _Unit2MsgQuit_Type()
)
unit2MsgQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit2MsgQuit.setStatus("mandatory")
_CmcTcStatusSensorUnit3_ObjectIdentity = ObjectIdentity
cmcTcStatusSensorUnit3 = _CmcTcStatusSensorUnit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5)
)


class _CmcTcUnit3TypeOfDevice_Type(Integer32):
    """Custom type cmcTcUnit3TypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitAccess", 3),
          ("unitClimate", 4),
          ("unitFCS", 5),
          ("unitIO", 2),
          ("unitRTT", 6))
    )


_CmcTcUnit3TypeOfDevice_Type.__name__ = "Integer32"
_CmcTcUnit3TypeOfDevice_Object = MibScalar
cmcTcUnit3TypeOfDevice = _CmcTcUnit3TypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 1),
    _CmcTcUnit3TypeOfDevice_Type()
)
cmcTcUnit3TypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3TypeOfDevice.setStatus("mandatory")


class _CmcTcUnit3Text_Type(DisplayString):
    """Custom type cmcTcUnit3Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcTcUnit3Text_Type.__name__ = "DisplayString"
_CmcTcUnit3Text_Object = MibScalar
cmcTcUnit3Text = _CmcTcUnit3Text_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 2),
    _CmcTcUnit3Text_Type()
)
cmcTcUnit3Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcUnit3Text.setStatus("mandatory")
_CmcTcUnit3Serial_Type = Integer32
_CmcTcUnit3Serial_Object = MibScalar
cmcTcUnit3Serial = _CmcTcUnit3Serial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 3),
    _CmcTcUnit3Serial_Type()
)
cmcTcUnit3Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3Serial.setStatus("mandatory")


class _CmcTcUnit3Status_Type(Integer32):
    """Custom type cmcTcUnit3Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("quit", 4),
          ("timeout", 5))
    )


_CmcTcUnit3Status_Type.__name__ = "Integer32"
_CmcTcUnit3Status_Object = MibScalar
cmcTcUnit3Status = _CmcTcUnit3Status_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 4),
    _CmcTcUnit3Status_Type()
)
cmcTcUnit3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3Status.setStatus("mandatory")
_CmcTcStatusUnit3Sensors_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit3Sensors = _CmcTcStatusUnit3Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5)
)
_CmcTcUnit3NumberOfSensors_Type = Integer32
_CmcTcUnit3NumberOfSensors_Object = MibScalar
cmcTcUnit3NumberOfSensors = _CmcTcUnit3NumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 1),
    _CmcTcUnit3NumberOfSensors_Type()
)
cmcTcUnit3NumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3NumberOfSensors.setStatus("mandatory")
_CmcTcUnit3SensorTable_Object = MibTable
cmcTcUnit3SensorTable = _CmcTcUnit3SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit3SensorTable.setStatus("mandatory")
_CmcTcUnit3SensorEntry_Object = MibTableRow
cmcTcUnit3SensorEntry = _CmcTcUnit3SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1)
)
cmcTcUnit3SensorEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit3SensorIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit3SensorEntry.setStatus("mandatory")


class _Unit3SensorIndex_Type(Integer32):
    """Custom type unit3SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit3SensorIndex_Type.__name__ = "Integer32"
_Unit3SensorIndex_Object = MibTableColumn
unit3SensorIndex = _Unit3SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 1),
    _Unit3SensorIndex_Type()
)
unit3SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorIndex.setStatus("mandatory")


class _Unit3SensorType_Type(Integer32):
    """Custom type unit3SensorType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("airFlow", 8),
          ("alarmRTT", 25),
          ("current4to20", 11),
          ("dutyPWM", 21),
          ("failure", 2),
          ("fanOK", 19),
          ("fanStatus", 22),
          ("filterRTT", 26),
          ("humidity", 12),
          ("leakage", 23),
          ("lock", 15),
          ("motion", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("readerKeypad", 20),
          ("smoke", 7),
          ("temperature", 10),
          ("type6", 9),
          ("unlock", 16),
          ("userNC", 14),
          ("userNO", 13),
          ("vibration", 5),
          ("voltOK", 17),
          ("voltage", 18),
          ("warningRTT", 24))
    )


_Unit3SensorType_Type.__name__ = "Integer32"
_Unit3SensorType_Object = MibTableColumn
unit3SensorType = _Unit3SensorType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 2),
    _Unit3SensorType_Type()
)
unit3SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorType.setStatus("mandatory")


class _Unit3SensorText_Type(DisplayString):
    """Custom type unit3SensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit3SensorText_Type.__name__ = "DisplayString"
_Unit3SensorText_Object = MibTableColumn
unit3SensorText = _Unit3SensorText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 3),
    _Unit3SensorText_Type()
)
unit3SensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3SensorText.setStatus("mandatory")


class _Unit3SensorStatus_Type(Integer32):
    """Custom type unit3SensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_Unit3SensorStatus_Type.__name__ = "Integer32"
_Unit3SensorStatus_Object = MibTableColumn
unit3SensorStatus = _Unit3SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 4),
    _Unit3SensorStatus_Type()
)
unit3SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorStatus.setStatus("mandatory")
_Unit3SensorValue_Type = Integer32
_Unit3SensorValue_Object = MibTableColumn
unit3SensorValue = _Unit3SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 5),
    _Unit3SensorValue_Type()
)
unit3SensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3SensorValue.setStatus("mandatory")
_Unit3SensorSetHigh_Type = Integer32
_Unit3SensorSetHigh_Object = MibTableColumn
unit3SensorSetHigh = _Unit3SensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 6),
    _Unit3SensorSetHigh_Type()
)
unit3SensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3SensorSetHigh.setStatus("mandatory")
_Unit3SensorSetLow_Type = Integer32
_Unit3SensorSetLow_Object = MibTableColumn
unit3SensorSetLow = _Unit3SensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 7),
    _Unit3SensorSetLow_Type()
)
unit3SensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3SensorSetLow.setStatus("mandatory")
_Unit3SensorSetWarn_Type = Integer32
_Unit3SensorSetWarn_Object = MibTableColumn
unit3SensorSetWarn = _Unit3SensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 5, 2, 1, 8),
    _Unit3SensorSetWarn_Type()
)
unit3SensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3SensorSetWarn.setStatus("mandatory")
_CmcTcStatusUnit3Outputs_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit3Outputs = _CmcTcStatusUnit3Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6)
)
_CmcTcUnit3NumberOfOutputs_Type = Integer32
_CmcTcUnit3NumberOfOutputs_Object = MibScalar
cmcTcUnit3NumberOfOutputs = _CmcTcUnit3NumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 1),
    _CmcTcUnit3NumberOfOutputs_Type()
)
cmcTcUnit3NumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3NumberOfOutputs.setStatus("mandatory")
_CmcTcUnit3OutputTable_Object = MibTable
cmcTcUnit3OutputTable = _CmcTcUnit3OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit3OutputTable.setStatus("mandatory")
_CmcTcUnit3OutputEntry_Object = MibTableRow
cmcTcUnit3OutputEntry = _CmcTcUnit3OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1)
)
cmcTcUnit3OutputEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit3OutputIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit3OutputEntry.setStatus("mandatory")


class _Unit3OutputIndex_Type(Integer32):
    """Custom type unit3OutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit3OutputIndex_Type.__name__ = "Integer32"
_Unit3OutputIndex_Object = MibTableColumn
unit3OutputIndex = _Unit3OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 1),
    _Unit3OutputIndex_Type()
)
unit3OutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutputIndex.setStatus("mandatory")


class _Unit3OutputType_Type(Integer32):
    """Custom type unit3OutputType based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doorLock", 4),
          ("doorLockFRi", 13),
          ("doorLockMaster", 12),
          ("failure", 2),
          ("fan", 7),
          ("fanSpeedContr", 8),
          ("notAvail", 1),
          ("overflow", 3),
          ("powerOut", 11),
          ("roomLock", 10),
          ("setpoint", 14),
          ("setpointTimax", 15),
          ("univLock1", 5),
          ("univLock2", 6),
          ("universalOut", 9))
    )


_Unit3OutputType_Type.__name__ = "Integer32"
_Unit3OutputType_Object = MibTableColumn
unit3OutputType = _Unit3OutputType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 2),
    _Unit3OutputType_Type()
)
unit3OutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3OutputType.setStatus("mandatory")


class _Unit3OutputText_Type(DisplayString):
    """Custom type unit3OutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit3OutputText_Type.__name__ = "DisplayString"
_Unit3OutputText_Object = MibTableColumn
unit3OutputText = _Unit3OutputText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 3),
    _Unit3OutputText_Type()
)
unit3OutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputText.setStatus("mandatory")


class _Unit3OutputStatus_Type(Integer32):
    """Custom type unit3OutputStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_Unit3OutputStatus_Type.__name__ = "Integer32"
_Unit3OutputStatus_Object = MibTableColumn
unit3OutputStatus = _Unit3OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 4),
    _Unit3OutputStatus_Type()
)
unit3OutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputStatus.setStatus("mandatory")
_Unit3OutputValue_Type = Integer32
_Unit3OutputValue_Object = MibTableColumn
unit3OutputValue = _Unit3OutputValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 5),
    _Unit3OutputValue_Type()
)
unit3OutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputValue.setStatus("mandatory")


class _Unit3OutputSet_Type(Integer32):
    """Custom type unit3OutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_Unit3OutputSet_Type.__name__ = "Integer32"
_Unit3OutputSet_Object = MibTableColumn
unit3OutputSet = _Unit3OutputSet_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 6),
    _Unit3OutputSet_Type()
)
unit3OutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputSet.setStatus("mandatory")


class _Unit3OutputConfig_Type(Integer32):
    """Custom type unit3OutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_Unit3OutputConfig_Type.__name__ = "Integer32"
_Unit3OutputConfig_Object = MibTableColumn
unit3OutputConfig = _Unit3OutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 7),
    _Unit3OutputConfig_Type()
)
unit3OutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputConfig.setStatus("mandatory")
_Unit3OutputDelay_Type = Integer32
_Unit3OutputDelay_Object = MibTableColumn
unit3OutputDelay = _Unit3OutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 8),
    _Unit3OutputDelay_Type()
)
unit3OutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputDelay.setStatus("mandatory")


class _Unit3OutputTimeoutAction_Type(Integer32):
    """Custom type unit3OutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_Unit3OutputTimeoutAction_Type.__name__ = "Integer32"
_Unit3OutputTimeoutAction_Object = MibTableColumn
unit3OutputTimeoutAction = _Unit3OutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 6, 2, 1, 9),
    _Unit3OutputTimeoutAction_Type()
)
unit3OutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3OutputTimeoutAction.setStatus("mandatory")
_CmcTcStatusUnit3Msg_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit3Msg = _CmcTcStatusUnit3Msg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7)
)
_CmcTcUnit3NumberOfMsgs_Type = Integer32
_CmcTcUnit3NumberOfMsgs_Object = MibScalar
cmcTcUnit3NumberOfMsgs = _CmcTcUnit3NumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 1),
    _CmcTcUnit3NumberOfMsgs_Type()
)
cmcTcUnit3NumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit3NumberOfMsgs.setStatus("mandatory")
_CmcTcUnit3MsgTable_Object = MibTable
cmcTcUnit3MsgTable = _CmcTcUnit3MsgTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit3MsgTable.setStatus("mandatory")
_CmcTcUnit3MsgEntry_Object = MibTableRow
cmcTcUnit3MsgEntry = _CmcTcUnit3MsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1)
)
cmcTcUnit3MsgEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit3MsgIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit3MsgEntry.setStatus("mandatory")


class _Unit3MsgIndex_Type(Integer32):
    """Custom type unit3MsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit3MsgIndex_Type.__name__ = "Integer32"
_Unit3MsgIndex_Object = MibTableColumn
unit3MsgIndex = _Unit3MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 1),
    _Unit3MsgIndex_Type()
)
unit3MsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3MsgIndex.setStatus("mandatory")


class _Unit3MsgText_Type(DisplayString):
    """Custom type unit3MsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit3MsgText_Type.__name__ = "DisplayString"
_Unit3MsgText_Object = MibTableColumn
unit3MsgText = _Unit3MsgText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 2),
    _Unit3MsgText_Type()
)
unit3MsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgText.setStatus("mandatory")


class _Unit3MsgStatus_Type(Integer32):
    """Custom type unit3MsgStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("closed", 12),
          ("configChanged", 2),
          ("error", 3),
          ("locked", 13),
          ("noAccess", 19),
          ("notAvail", 1),
          ("ok", 4),
          ("open", 11),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("unlReaderKeypad", 15),
          ("unlRemote", 14),
          ("unlSNMP", 16),
          ("unlTimer", 18),
          ("unlWEB", 17),
          ("warning", 6))
    )


_Unit3MsgStatus_Type.__name__ = "Integer32"
_Unit3MsgStatus_Object = MibTableColumn
unit3MsgStatus = _Unit3MsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 3),
    _Unit3MsgStatus_Type()
)
unit3MsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit3MsgStatus.setStatus("mandatory")


class _Unit3MsgRelay_Type(Integer32):
    """Custom type unit3MsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgRelay_Type.__name__ = "Integer32"
_Unit3MsgRelay_Object = MibTableColumn
unit3MsgRelay = _Unit3MsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 4),
    _Unit3MsgRelay_Type()
)
unit3MsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgRelay.setStatus("mandatory")


class _Unit3MsgBeeper_Type(Integer32):
    """Custom type unit3MsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgBeeper_Type.__name__ = "Integer32"
_Unit3MsgBeeper_Object = MibTableColumn
unit3MsgBeeper = _Unit3MsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 5),
    _Unit3MsgBeeper_Type()
)
unit3MsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgBeeper.setStatus("mandatory")


class _Unit3MsgTrap1_Type(Integer32):
    """Custom type unit3MsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgTrap1_Type.__name__ = "Integer32"
_Unit3MsgTrap1_Object = MibTableColumn
unit3MsgTrap1 = _Unit3MsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 6),
    _Unit3MsgTrap1_Type()
)
unit3MsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgTrap1.setStatus("mandatory")


class _Unit3MsgTrap2_Type(Integer32):
    """Custom type unit3MsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgTrap2_Type.__name__ = "Integer32"
_Unit3MsgTrap2_Object = MibTableColumn
unit3MsgTrap2 = _Unit3MsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 7),
    _Unit3MsgTrap2_Type()
)
unit3MsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgTrap2.setStatus("mandatory")


class _Unit3MsgTrap3_Type(Integer32):
    """Custom type unit3MsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgTrap3_Type.__name__ = "Integer32"
_Unit3MsgTrap3_Object = MibTableColumn
unit3MsgTrap3 = _Unit3MsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 8),
    _Unit3MsgTrap3_Type()
)
unit3MsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgTrap3.setStatus("mandatory")


class _Unit3MsgTrap4_Type(Integer32):
    """Custom type unit3MsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit3MsgTrap4_Type.__name__ = "Integer32"
_Unit3MsgTrap4_Object = MibTableColumn
unit3MsgTrap4 = _Unit3MsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 9),
    _Unit3MsgTrap4_Type()
)
unit3MsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgTrap4.setStatus("mandatory")


class _Unit3MsgQuit_Type(Integer32):
    """Custom type unit3MsgQuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Unit3MsgQuit_Type.__name__ = "Integer32"
_Unit3MsgQuit_Object = MibTableColumn
unit3MsgQuit = _Unit3MsgQuit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 5, 7, 2, 1, 10),
    _Unit3MsgQuit_Type()
)
unit3MsgQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit3MsgQuit.setStatus("mandatory")
_CmcTcStatusSensorUnit4_ObjectIdentity = ObjectIdentity
cmcTcStatusSensorUnit4 = _CmcTcStatusSensorUnit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6)
)


class _CmcTcUnit4TypeOfDevice_Type(Integer32):
    """Custom type cmcTcUnit4TypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitAccess", 3),
          ("unitClimate", 4),
          ("unitFCS", 5),
          ("unitIO", 2),
          ("unitRTT", 6))
    )


_CmcTcUnit4TypeOfDevice_Type.__name__ = "Integer32"
_CmcTcUnit4TypeOfDevice_Object = MibScalar
cmcTcUnit4TypeOfDevice = _CmcTcUnit4TypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 1),
    _CmcTcUnit4TypeOfDevice_Type()
)
cmcTcUnit4TypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4TypeOfDevice.setStatus("mandatory")


class _CmcTcUnit4Text_Type(DisplayString):
    """Custom type cmcTcUnit4Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcTcUnit4Text_Type.__name__ = "DisplayString"
_CmcTcUnit4Text_Object = MibScalar
cmcTcUnit4Text = _CmcTcUnit4Text_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 2),
    _CmcTcUnit4Text_Type()
)
cmcTcUnit4Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcUnit4Text.setStatus("mandatory")
_CmcTcUnit4Serial_Type = Integer32
_CmcTcUnit4Serial_Object = MibScalar
cmcTcUnit4Serial = _CmcTcUnit4Serial_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 3),
    _CmcTcUnit4Serial_Type()
)
cmcTcUnit4Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4Serial.setStatus("mandatory")


class _CmcTcUnit4Status_Type(Integer32):
    """Custom type cmcTcUnit4Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("quit", 4),
          ("timeout", 5))
    )


_CmcTcUnit4Status_Type.__name__ = "Integer32"
_CmcTcUnit4Status_Object = MibScalar
cmcTcUnit4Status = _CmcTcUnit4Status_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 4),
    _CmcTcUnit4Status_Type()
)
cmcTcUnit4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4Status.setStatus("mandatory")
_CmcTcStatusUnit4Sensors_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit4Sensors = _CmcTcStatusUnit4Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5)
)
_CmcTcUnit4NumberOfSensors_Type = Integer32
_CmcTcUnit4NumberOfSensors_Object = MibScalar
cmcTcUnit4NumberOfSensors = _CmcTcUnit4NumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 1),
    _CmcTcUnit4NumberOfSensors_Type()
)
cmcTcUnit4NumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4NumberOfSensors.setStatus("mandatory")
_CmcTcUnit4SensorTable_Object = MibTable
cmcTcUnit4SensorTable = _CmcTcUnit4SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit4SensorTable.setStatus("mandatory")
_CmcTcUnit4SensorEntry_Object = MibTableRow
cmcTcUnit4SensorEntry = _CmcTcUnit4SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1)
)
cmcTcUnit4SensorEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit4SensorIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit4SensorEntry.setStatus("mandatory")


class _Unit4SensorIndex_Type(Integer32):
    """Custom type unit4SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit4SensorIndex_Type.__name__ = "Integer32"
_Unit4SensorIndex_Object = MibTableColumn
unit4SensorIndex = _Unit4SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 1),
    _Unit4SensorIndex_Type()
)
unit4SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorIndex.setStatus("mandatory")


class _Unit4SensorType_Type(Integer32):
    """Custom type unit4SensorType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("airFlow", 8),
          ("alarmRTT", 25),
          ("current4to20", 11),
          ("dutyPWM", 21),
          ("failure", 2),
          ("fanOK", 19),
          ("fanStatus", 22),
          ("filterRTT", 26),
          ("humidity", 12),
          ("leakage", 23),
          ("lock", 15),
          ("motion", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("readerKeypad", 20),
          ("smoke", 7),
          ("temperature", 10),
          ("type6", 9),
          ("unlock", 16),
          ("userNC", 14),
          ("userNO", 13),
          ("vibration", 5),
          ("voltOK", 17),
          ("voltage", 18),
          ("warningRTT", 24))
    )


_Unit4SensorType_Type.__name__ = "Integer32"
_Unit4SensorType_Object = MibTableColumn
unit4SensorType = _Unit4SensorType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 2),
    _Unit4SensorType_Type()
)
unit4SensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorType.setStatus("mandatory")


class _Unit4SensorText_Type(DisplayString):
    """Custom type unit4SensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit4SensorText_Type.__name__ = "DisplayString"
_Unit4SensorText_Object = MibTableColumn
unit4SensorText = _Unit4SensorText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 3),
    _Unit4SensorText_Type()
)
unit4SensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4SensorText.setStatus("mandatory")


class _Unit4SensorStatus_Type(Integer32):
    """Custom type unit4SensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_Unit4SensorStatus_Type.__name__ = "Integer32"
_Unit4SensorStatus_Object = MibTableColumn
unit4SensorStatus = _Unit4SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 4),
    _Unit4SensorStatus_Type()
)
unit4SensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorStatus.setStatus("mandatory")
_Unit4SensorValue_Type = Integer32
_Unit4SensorValue_Object = MibTableColumn
unit4SensorValue = _Unit4SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 5),
    _Unit4SensorValue_Type()
)
unit4SensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4SensorValue.setStatus("mandatory")
_Unit4SensorSetHigh_Type = Integer32
_Unit4SensorSetHigh_Object = MibTableColumn
unit4SensorSetHigh = _Unit4SensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 6),
    _Unit4SensorSetHigh_Type()
)
unit4SensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4SensorSetHigh.setStatus("mandatory")
_Unit4SensorSetLow_Type = Integer32
_Unit4SensorSetLow_Object = MibTableColumn
unit4SensorSetLow = _Unit4SensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 7),
    _Unit4SensorSetLow_Type()
)
unit4SensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4SensorSetLow.setStatus("mandatory")
_Unit4SensorSetWarn_Type = Integer32
_Unit4SensorSetWarn_Object = MibTableColumn
unit4SensorSetWarn = _Unit4SensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 5, 2, 1, 8),
    _Unit4SensorSetWarn_Type()
)
unit4SensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4SensorSetWarn.setStatus("mandatory")
_CmcTcStatusUnit4Outputs_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit4Outputs = _CmcTcStatusUnit4Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6)
)
_CmcTcUnit4NumberOfOutputs_Type = Integer32
_CmcTcUnit4NumberOfOutputs_Object = MibScalar
cmcTcUnit4NumberOfOutputs = _CmcTcUnit4NumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 1),
    _CmcTcUnit4NumberOfOutputs_Type()
)
cmcTcUnit4NumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4NumberOfOutputs.setStatus("mandatory")
_CmcTcUnit4OutputTable_Object = MibTable
cmcTcUnit4OutputTable = _CmcTcUnit4OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit4OutputTable.setStatus("mandatory")
_CmcTcUnit4OutputEntry_Object = MibTableRow
cmcTcUnit4OutputEntry = _CmcTcUnit4OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1)
)
cmcTcUnit4OutputEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit4OutputIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit4OutputEntry.setStatus("mandatory")


class _Unit4OutputIndex_Type(Integer32):
    """Custom type unit4OutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit4OutputIndex_Type.__name__ = "Integer32"
_Unit4OutputIndex_Object = MibTableColumn
unit4OutputIndex = _Unit4OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 1),
    _Unit4OutputIndex_Type()
)
unit4OutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutputIndex.setStatus("mandatory")


class _Unit4OutputType_Type(Integer32):
    """Custom type unit4OutputType based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doorLock", 4),
          ("doorLockFRi", 13),
          ("doorLockMaster", 12),
          ("failure", 2),
          ("fan", 7),
          ("fanSpeedContr", 8),
          ("notAvail", 1),
          ("overflow", 3),
          ("powerOut", 11),
          ("roomLock", 10),
          ("setpoint", 14),
          ("setpointTimax", 15),
          ("univLock1", 5),
          ("univLock2", 6),
          ("universalOut", 9))
    )


_Unit4OutputType_Type.__name__ = "Integer32"
_Unit4OutputType_Object = MibTableColumn
unit4OutputType = _Unit4OutputType_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 2),
    _Unit4OutputType_Type()
)
unit4OutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4OutputType.setStatus("mandatory")


class _Unit4OutputText_Type(DisplayString):
    """Custom type unit4OutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit4OutputText_Type.__name__ = "DisplayString"
_Unit4OutputText_Object = MibTableColumn
unit4OutputText = _Unit4OutputText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 3),
    _Unit4OutputText_Type()
)
unit4OutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputText.setStatus("mandatory")


class _Unit4OutputStatus_Type(Integer32):
    """Custom type unit4OutputStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_Unit4OutputStatus_Type.__name__ = "Integer32"
_Unit4OutputStatus_Object = MibTableColumn
unit4OutputStatus = _Unit4OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 4),
    _Unit4OutputStatus_Type()
)
unit4OutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputStatus.setStatus("mandatory")
_Unit4OutputValue_Type = Integer32
_Unit4OutputValue_Object = MibTableColumn
unit4OutputValue = _Unit4OutputValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 5),
    _Unit4OutputValue_Type()
)
unit4OutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputValue.setStatus("mandatory")


class _Unit4OutputSet_Type(Integer32):
    """Custom type unit4OutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_Unit4OutputSet_Type.__name__ = "Integer32"
_Unit4OutputSet_Object = MibTableColumn
unit4OutputSet = _Unit4OutputSet_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 6),
    _Unit4OutputSet_Type()
)
unit4OutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputSet.setStatus("mandatory")


class _Unit4OutputConfig_Type(Integer32):
    """Custom type unit4OutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_Unit4OutputConfig_Type.__name__ = "Integer32"
_Unit4OutputConfig_Object = MibTableColumn
unit4OutputConfig = _Unit4OutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 7),
    _Unit4OutputConfig_Type()
)
unit4OutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputConfig.setStatus("mandatory")
_Unit4OutputDelay_Type = Integer32
_Unit4OutputDelay_Object = MibTableColumn
unit4OutputDelay = _Unit4OutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 8),
    _Unit4OutputDelay_Type()
)
unit4OutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputDelay.setStatus("mandatory")


class _Unit4OutputTimeoutAction_Type(Integer32):
    """Custom type unit4OutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_Unit4OutputTimeoutAction_Type.__name__ = "Integer32"
_Unit4OutputTimeoutAction_Object = MibTableColumn
unit4OutputTimeoutAction = _Unit4OutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 6, 2, 1, 9),
    _Unit4OutputTimeoutAction_Type()
)
unit4OutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4OutputTimeoutAction.setStatus("mandatory")
_CmcTcStatusUnit4Msg_ObjectIdentity = ObjectIdentity
cmcTcStatusUnit4Msg = _CmcTcStatusUnit4Msg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7)
)
_CmcTcUnit4NumberOfMsgs_Type = Integer32
_CmcTcUnit4NumberOfMsgs_Object = MibScalar
cmcTcUnit4NumberOfMsgs = _CmcTcUnit4NumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 1),
    _CmcTcUnit4NumberOfMsgs_Type()
)
cmcTcUnit4NumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcUnit4NumberOfMsgs.setStatus("mandatory")
_CmcTcUnit4MsgTable_Object = MibTable
cmcTcUnit4MsgTable = _CmcTcUnit4MsgTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2)
)
if mibBuilder.loadTexts:
    cmcTcUnit4MsgTable.setStatus("mandatory")
_CmcTcUnit4MsgEntry_Object = MibTableRow
cmcTcUnit4MsgEntry = _CmcTcUnit4MsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1)
)
cmcTcUnit4MsgEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "unit4MsgIndex"),
)
if mibBuilder.loadTexts:
    cmcTcUnit4MsgEntry.setStatus("mandatory")


class _Unit4MsgIndex_Type(Integer32):
    """Custom type unit4MsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Unit4MsgIndex_Type.__name__ = "Integer32"
_Unit4MsgIndex_Object = MibTableColumn
unit4MsgIndex = _Unit4MsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 1),
    _Unit4MsgIndex_Type()
)
unit4MsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4MsgIndex.setStatus("mandatory")


class _Unit4MsgText_Type(DisplayString):
    """Custom type unit4MsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Unit4MsgText_Type.__name__ = "DisplayString"
_Unit4MsgText_Object = MibTableColumn
unit4MsgText = _Unit4MsgText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 2),
    _Unit4MsgText_Type()
)
unit4MsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgText.setStatus("mandatory")


class _Unit4MsgStatus_Type(Integer32):
    """Custom type unit4MsgStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("closed", 12),
          ("configChanged", 2),
          ("error", 3),
          ("locked", 13),
          ("noAccess", 19),
          ("notAvail", 1),
          ("ok", 4),
          ("open", 11),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("unlReaderKeypad", 15),
          ("unlRemote", 14),
          ("unlSNMP", 16),
          ("unlTimer", 18),
          ("unlWEB", 17),
          ("warning", 6))
    )


_Unit4MsgStatus_Type.__name__ = "Integer32"
_Unit4MsgStatus_Object = MibTableColumn
unit4MsgStatus = _Unit4MsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 3),
    _Unit4MsgStatus_Type()
)
unit4MsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit4MsgStatus.setStatus("mandatory")


class _Unit4MsgRelay_Type(Integer32):
    """Custom type unit4MsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgRelay_Type.__name__ = "Integer32"
_Unit4MsgRelay_Object = MibTableColumn
unit4MsgRelay = _Unit4MsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 4),
    _Unit4MsgRelay_Type()
)
unit4MsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgRelay.setStatus("mandatory")


class _Unit4MsgBeeper_Type(Integer32):
    """Custom type unit4MsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgBeeper_Type.__name__ = "Integer32"
_Unit4MsgBeeper_Object = MibTableColumn
unit4MsgBeeper = _Unit4MsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 5),
    _Unit4MsgBeeper_Type()
)
unit4MsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgBeeper.setStatus("mandatory")


class _Unit4MsgTrap1_Type(Integer32):
    """Custom type unit4MsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgTrap1_Type.__name__ = "Integer32"
_Unit4MsgTrap1_Object = MibTableColumn
unit4MsgTrap1 = _Unit4MsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 6),
    _Unit4MsgTrap1_Type()
)
unit4MsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgTrap1.setStatus("mandatory")


class _Unit4MsgTrap2_Type(Integer32):
    """Custom type unit4MsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgTrap2_Type.__name__ = "Integer32"
_Unit4MsgTrap2_Object = MibTableColumn
unit4MsgTrap2 = _Unit4MsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 7),
    _Unit4MsgTrap2_Type()
)
unit4MsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgTrap2.setStatus("mandatory")


class _Unit4MsgTrap3_Type(Integer32):
    """Custom type unit4MsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgTrap3_Type.__name__ = "Integer32"
_Unit4MsgTrap3_Object = MibTableColumn
unit4MsgTrap3 = _Unit4MsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 8),
    _Unit4MsgTrap3_Type()
)
unit4MsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgTrap3.setStatus("mandatory")


class _Unit4MsgTrap4_Type(Integer32):
    """Custom type unit4MsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Unit4MsgTrap4_Type.__name__ = "Integer32"
_Unit4MsgTrap4_Object = MibTableColumn
unit4MsgTrap4 = _Unit4MsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 9),
    _Unit4MsgTrap4_Type()
)
unit4MsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgTrap4.setStatus("mandatory")


class _Unit4MsgQuit_Type(Integer32):
    """Custom type unit4MsgQuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_Unit4MsgQuit_Type.__name__ = "Integer32"
_Unit4MsgQuit_Object = MibTableColumn
unit4MsgQuit = _Unit4MsgQuit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 6, 7, 2, 1, 10),
    _Unit4MsgQuit_Type()
)
unit4MsgQuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unit4MsgQuit.setStatus("mandatory")
_CmcTcStatusExtUnit_ObjectIdentity = ObjectIdentity
cmcTcStatusExtUnit = _CmcTcStatusExtUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7)
)


class _CmcTcValuesRelay_Type(Integer32):
    """Custom type cmcTcValuesRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesRelay_Type.__name__ = "Integer32"
_CmcTcValuesRelay_Object = MibScalar
cmcTcValuesRelay = _CmcTcValuesRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 1),
    _CmcTcValuesRelay_Type()
)
cmcTcValuesRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesRelay.setStatus("mandatory")


class _CmcTcValuesBeeper_Type(Integer32):
    """Custom type cmcTcValuesBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesBeeper_Type.__name__ = "Integer32"
_CmcTcValuesBeeper_Object = MibScalar
cmcTcValuesBeeper = _CmcTcValuesBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 2),
    _CmcTcValuesBeeper_Type()
)
cmcTcValuesBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesBeeper.setStatus("mandatory")


class _CmcTcValuesTrap1_Type(Integer32):
    """Custom type cmcTcValuesTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesTrap1_Type.__name__ = "Integer32"
_CmcTcValuesTrap1_Object = MibScalar
cmcTcValuesTrap1 = _CmcTcValuesTrap1_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 3),
    _CmcTcValuesTrap1_Type()
)
cmcTcValuesTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesTrap1.setStatus("mandatory")


class _CmcTcValuesTrap2_Type(Integer32):
    """Custom type cmcTcValuesTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesTrap2_Type.__name__ = "Integer32"
_CmcTcValuesTrap2_Object = MibScalar
cmcTcValuesTrap2 = _CmcTcValuesTrap2_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 4),
    _CmcTcValuesTrap2_Type()
)
cmcTcValuesTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesTrap2.setStatus("mandatory")


class _CmcTcValuesTrap3_Type(Integer32):
    """Custom type cmcTcValuesTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesTrap3_Type.__name__ = "Integer32"
_CmcTcValuesTrap3_Object = MibScalar
cmcTcValuesTrap3 = _CmcTcValuesTrap3_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 5),
    _CmcTcValuesTrap3_Type()
)
cmcTcValuesTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesTrap3.setStatus("mandatory")


class _CmcTcValuesTrap4_Type(Integer32):
    """Custom type cmcTcValuesTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmcTcValuesTrap4_Type.__name__ = "Integer32"
_CmcTcValuesTrap4_Object = MibScalar
cmcTcValuesTrap4 = _CmcTcValuesTrap4_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 6),
    _CmcTcValuesTrap4_Type()
)
cmcTcValuesTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcValuesTrap4.setStatus("mandatory")
_CmcTcNumberOfValues_Type = Integer32
_CmcTcNumberOfValues_Object = MibScalar
cmcTcNumberOfValues = _CmcTcNumberOfValues_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 7),
    _CmcTcNumberOfValues_Type()
)
cmcTcNumberOfValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcNumberOfValues.setStatus("mandatory")
_CmcTcValuesTable_Object = MibTable
cmcTcValuesTable = _CmcTcValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8)
)
if mibBuilder.loadTexts:
    cmcTcValuesTable.setStatus("mandatory")
_CmcTcValuesEntry_Object = MibTableRow
cmcTcValuesEntry = _CmcTcValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1)
)
cmcTcValuesEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "valuesIndex"),
)
if mibBuilder.loadTexts:
    cmcTcValuesEntry.setStatus("mandatory")


class _ValuesIndex_Type(Integer32):
    """Custom type valuesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ValuesIndex_Type.__name__ = "Integer32"
_ValuesIndex_Object = MibTableColumn
valuesIndex = _ValuesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 1),
    _ValuesIndex_Type()
)
valuesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valuesIndex.setStatus("mandatory")


class _ValuesText_Type(DisplayString):
    """Custom type valuesText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ValuesText_Type.__name__ = "DisplayString"
_ValuesText_Object = MibTableColumn
valuesText = _ValuesText_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 2),
    _ValuesText_Type()
)
valuesText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuesText.setStatus("mandatory")


class _ValuesStatus_Type(Integer32):
    """Custom type valuesStatus based on Integer32"""
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
        *(("changed", 3),
          ("error", 7),
          ("lost", 2),
          ("notAvail", 1),
          ("ok", 4),
          ("tooHigh", 6),
          ("tooLow", 5))
    )


_ValuesStatus_Type.__name__ = "Integer32"
_ValuesStatus_Object = MibTableColumn
valuesStatus = _ValuesStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 3),
    _ValuesStatus_Type()
)
valuesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valuesStatus.setStatus("mandatory")
_ValuesValue_Type = Integer32
_ValuesValue_Object = MibTableColumn
valuesValue = _ValuesValue_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 4),
    _ValuesValue_Type()
)
valuesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valuesValue.setStatus("mandatory")
_ValuesSetHigh_Type = Integer32
_ValuesSetHigh_Object = MibTableColumn
valuesSetHigh = _ValuesSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 5),
    _ValuesSetHigh_Type()
)
valuesSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuesSetHigh.setStatus("mandatory")
_ValuesSetLow_Type = Integer32
_ValuesSetLow_Object = MibTableColumn
valuesSetLow = _ValuesSetLow_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 2, 7, 8, 1, 6),
    _ValuesSetLow_Type()
)
valuesSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valuesSetLow.setStatus("mandatory")
_CmcTcSetup_ObjectIdentity = ObjectIdentity
cmcTcSetup = _CmcTcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3)
)
_CmcTcSetupGeneral_ObjectIdentity = ObjectIdentity
cmcTcSetupGeneral = _CmcTcSetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1)
)


class _CmcTcSetTempUnit_Type(Integer32):
    """Custom type cmcTcSetTempUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_CmcTcSetTempUnit_Type.__name__ = "Integer32"
_CmcTcSetTempUnit_Object = MibScalar
cmcTcSetTempUnit = _CmcTcSetTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 1),
    _CmcTcSetTempUnit_Type()
)
cmcTcSetTempUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcSetTempUnit.setStatus("mandatory")


class _CmcTcSetBeeper_Type(Integer32):
    """Custom type cmcTcSetBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmcTcSetBeeper_Type.__name__ = "Integer32"
_CmcTcSetBeeper_Object = MibScalar
cmcTcSetBeeper = _CmcTcSetBeeper_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 2),
    _CmcTcSetBeeper_Type()
)
cmcTcSetBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcSetBeeper.setStatus("mandatory")


class _CmcTcQuitRelay_Type(Integer32):
    """Custom type cmcTcQuitRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcTcQuitRelay_Type.__name__ = "Integer32"
_CmcTcQuitRelay_Object = MibScalar
cmcTcQuitRelay = _CmcTcQuitRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 3),
    _CmcTcQuitRelay_Type()
)
cmcTcQuitRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcQuitRelay.setStatus("mandatory")


class _CmcTcLogicRelay_Type(Integer32):
    """Custom type cmcTcLogicRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closeAtAlarm", 1),
          ("off", 3),
          ("openAtAlarm", 2))
    )


_CmcTcLogicRelay_Type.__name__ = "Integer32"
_CmcTcLogicRelay_Object = MibScalar
cmcTcLogicRelay = _CmcTcLogicRelay_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 4),
    _CmcTcLogicRelay_Type()
)
cmcTcLogicRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcLogicRelay.setStatus("mandatory")


class _CmcTcWebAccess_Type(Integer32):
    """Custom type cmcTcWebAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullAccess", 2),
          ("off", 3),
          ("viewOnly", 1))
    )


_CmcTcWebAccess_Type.__name__ = "Integer32"
_CmcTcWebAccess_Object = MibScalar
cmcTcWebAccess = _CmcTcWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 5),
    _CmcTcWebAccess_Type()
)
cmcTcWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcWebAccess.setStatus("mandatory")


class _CmcTcSetupDate_Type(DisplayString):
    """Custom type cmcTcSetupDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CmcTcSetupDate_Type.__name__ = "DisplayString"
_CmcTcSetupDate_Object = MibScalar
cmcTcSetupDate = _CmcTcSetupDate_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 6),
    _CmcTcSetupDate_Type()
)
cmcTcSetupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcSetupDate.setStatus("mandatory")


class _CmcTcSetupTime_Type(DisplayString):
    """Custom type cmcTcSetupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmcTcSetupTime_Type.__name__ = "DisplayString"
_CmcTcSetupTime_Object = MibScalar
cmcTcSetupTime = _CmcTcSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 7),
    _CmcTcSetupTime_Type()
)
cmcTcSetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcSetupTime.setStatus("mandatory")
_CmcTcTimerTable1_ObjectIdentity = ObjectIdentity
cmcTcTimerTable1 = _CmcTcTimerTable1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8)
)
_CmcTcTimerNumber_Type = Integer32
_CmcTcTimerNumber_Object = MibScalar
cmcTcTimerNumber = _CmcTcTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 1),
    _CmcTcTimerNumber_Type()
)
cmcTcTimerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcTimerNumber.setStatus("mandatory")
_CmcTcTimerTable_Object = MibTable
cmcTcTimerTable = _CmcTcTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cmcTcTimerTable.setStatus("mandatory")
_CmcTcTimerEntry_Object = MibTableRow
cmcTcTimerEntry = _CmcTcTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1)
)
cmcTcTimerEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "cmcTcTimerIndex"),
)
if mibBuilder.loadTexts:
    cmcTcTimerEntry.setStatus("mandatory")


class _CmcTcTimerIndex_Type(Integer32):
    """Custom type cmcTcTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmcTcTimerIndex_Type.__name__ = "Integer32"
_CmcTcTimerIndex_Object = MibTableColumn
cmcTcTimerIndex = _CmcTcTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 1),
    _CmcTcTimerIndex_Type()
)
cmcTcTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcTimerIndex.setStatus("mandatory")


class _CmcTcTimerStatus_Type(Integer32):
    """Custom type cmcTcTimerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTime", 3),
          ("switchedOff", 1),
          ("switchedOn", 2))
    )


_CmcTcTimerStatus_Type.__name__ = "Integer32"
_CmcTcTimerStatus_Object = MibTableColumn
cmcTcTimerStatus = _CmcTcTimerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 2),
    _CmcTcTimerStatus_Type()
)
cmcTcTimerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcTimerStatus.setStatus("mandatory")


class _CmcTcTimerDayOfWeek_Type(Integer32):
    """Custom type cmcTcTimerDayOfWeek based on Integer32"""
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
        *(("fri", 6),
          ("mon", 2),
          ("mon-fri", 9),
          ("mon-sun", 10),
          ("sat", 7),
          ("sat-sun", 8),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_CmcTcTimerDayOfWeek_Type.__name__ = "Integer32"
_CmcTcTimerDayOfWeek_Object = MibTableColumn
cmcTcTimerDayOfWeek = _CmcTcTimerDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 3),
    _CmcTcTimerDayOfWeek_Type()
)
cmcTcTimerDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcTimerDayOfWeek.setStatus("mandatory")


class _CmcTcTimeOn_Type(DisplayString):
    """Custom type cmcTcTimeOn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CmcTcTimeOn_Type.__name__ = "DisplayString"
_CmcTcTimeOn_Object = MibTableColumn
cmcTcTimeOn = _CmcTcTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 4),
    _CmcTcTimeOn_Type()
)
cmcTcTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcTimeOn.setStatus("mandatory")


class _CmcTcTimeOff_Type(DisplayString):
    """Custom type cmcTcTimeOff based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CmcTcTimeOff_Type.__name__ = "DisplayString"
_CmcTcTimeOff_Object = MibTableColumn
cmcTcTimeOff = _CmcTcTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 5),
    _CmcTcTimeOff_Type()
)
cmcTcTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcTimeOff.setStatus("mandatory")


class _CmcTcTimeControl_Type(Integer32):
    """Custom type cmcTcTimeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CmcTcTimeControl_Type.__name__ = "Integer32"
_CmcTcTimeControl_Object = MibTableColumn
cmcTcTimeControl = _CmcTcTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 6),
    _CmcTcTimeControl_Type()
)
cmcTcTimeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcTimeControl.setStatus("mandatory")


class _CmcTcTimerFunction_Type(Integer32):
    """Custom type cmcTcTimerFunction based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("disKeypad1-1", 1),
          ("disKeypad1-2", 3),
          ("disKeypad1-3", 5),
          ("disKeypad1-4", 7),
          ("disKeypad2-1", 2),
          ("disKeypad2-2", 4),
          ("disKeypad2-3", 6),
          ("disKeypad2-4", 8),
          ("disTrapRec1", 17),
          ("disTrapRec2", 18),
          ("disTrapRec3", 19),
          ("disTrapRec4", 20),
          ("unlDoor1-1", 9),
          ("unlDoor1-2", 11),
          ("unlDoor1-3", 13),
          ("unlDoor1-4", 15),
          ("unlDoor2-1", 10),
          ("unlDoor2-2", 12),
          ("unlDoor2-3", 14),
          ("unlDoor2-5", 16))
    )


_CmcTcTimerFunction_Type.__name__ = "Integer32"
_CmcTcTimerFunction_Object = MibTableColumn
cmcTcTimerFunction = _CmcTcTimerFunction_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 3, 1, 8, 2, 1, 7),
    _CmcTcTimerFunction_Type()
)
cmcTcTimerFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcTimerFunction.setStatus("mandatory")
_CmcTcTrapControl_ObjectIdentity = ObjectIdentity
cmcTcTrapControl = _CmcTcTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4)
)
_CmcTcTraps_ObjectIdentity = ObjectIdentity
cmcTcTraps = _CmcTcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7)
)
_CmcTcTraptableNumber_Type = Integer32
_CmcTcTraptableNumber_Object = MibScalar
cmcTcTraptableNumber = _CmcTcTraptableNumber_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 1),
    _CmcTcTraptableNumber_Type()
)
cmcTcTraptableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmcTcTraptableNumber.setStatus("mandatory")
_CmcTcTrapTableTable_Object = MibTable
cmcTcTrapTableTable = _CmcTcTrapTableTable_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 2)
)
if mibBuilder.loadTexts:
    cmcTcTrapTableTable.setStatus("mandatory")
_CmcTcTrapTableEntry_Object = MibTableRow
cmcTcTrapTableEntry = _CmcTcTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 2, 1)
)
cmcTcTrapTableEntry.setIndexNames(
    (0, "RITTAL-CMC-TC-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    cmcTcTrapTableEntry.setStatus("mandatory")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 2, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 2, 1, 2),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")


class _TrapIPaddress_Type(DisplayString):
    """Custom type trapIPaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TrapIPaddress_Type.__name__ = "DisplayString"
_TrapIPaddress_Object = MibTableColumn
trapIPaddress = _TrapIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 4, 7, 2, 1, 3),
    _TrapIPaddress_Type()
)
trapIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPaddress.setStatus("mandatory")
_CmcTcControl_ObjectIdentity = ObjectIdentity
cmcTcControl = _CmcTcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 4, 5)
)


class _CmcTcQuitUnit_Type(Integer32):
    """Custom type cmcTcQuitUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noQuit", 1),
          ("quit", 2))
    )


_CmcTcQuitUnit_Type.__name__ = "Integer32"
_CmcTcQuitUnit_Object = MibScalar
cmcTcQuitUnit = _CmcTcQuitUnit_Object(
    (1, 3, 6, 1, 4, 1, 2606, 4, 5, 1),
    _CmcTcQuitUnit_Type()
)
cmcTcQuitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmcTcQuitUnit.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmSensorUnit1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 1)
)
alarmSensorUnit1.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "unit1MsgIndex"),
        ("RITTAL-CMC-TC-MIB", "unit1MsgText"),
        ("RITTAL-CMC-TC-MIB", "unit1MsgStatus"),
        ("RITTAL-CMC-TC-MIB", "unit1SensorValue"))
)
if mibBuilder.loadTexts:
    alarmSensorUnit1.setStatus(
        ""
    )

alarmSensorUnit2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 2)
)
alarmSensorUnit2.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "unit2MsgIndex"),
        ("RITTAL-CMC-TC-MIB", "unit2MsgText"),
        ("RITTAL-CMC-TC-MIB", "unit2MsgStatus"),
        ("RITTAL-CMC-TC-MIB", "unit2SensorValue"))
)
if mibBuilder.loadTexts:
    alarmSensorUnit2.setStatus(
        ""
    )

alarmSensorUnit3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 3)
)
alarmSensorUnit3.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "unit3MsgIndex"),
        ("RITTAL-CMC-TC-MIB", "unit3MsgText"),
        ("RITTAL-CMC-TC-MIB", "unit3MsgStatus"),
        ("RITTAL-CMC-TC-MIB", "unit3SensorValue"))
)
if mibBuilder.loadTexts:
    alarmSensorUnit3.setStatus(
        ""
    )

alarmSensorUnit4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 4)
)
alarmSensorUnit4.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "unit4MsgIndex"),
        ("RITTAL-CMC-TC-MIB", "unit4MsgText"),
        ("RITTAL-CMC-TC-MIB", "unit4MsgStatus"),
        ("RITTAL-CMC-TC-MIB", "unit4SensorValue"))
)
if mibBuilder.loadTexts:
    alarmSensorUnit4.setStatus(
        ""
    )

alarmUnit1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 5)
)
alarmUnit1.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit1Text"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit1Status"))
)
if mibBuilder.loadTexts:
    alarmUnit1.setStatus(
        ""
    )

alarmUnit2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 6)
)
alarmUnit2.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit2Text"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit2Status"))
)
if mibBuilder.loadTexts:
    alarmUnit2.setStatus(
        ""
    )

alarmUnit3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 7)
)
alarmUnit3.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit3Text"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit3Status"))
)
if mibBuilder.loadTexts:
    alarmUnit3.setStatus(
        ""
    )

alarmUnit4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 8)
)
alarmUnit4.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit4Text"),
        ("RITTAL-CMC-TC-MIB", "cmcTcUnit4Status"))
)
if mibBuilder.loadTexts:
    alarmUnit4.setStatus(
        ""
    )

alarmValues = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 9)
)
alarmValues.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("RITTAL-CMC-TC-MIB", "valuesIndex"),
        ("RITTAL-CMC-TC-MIB", "valuesText"),
        ("RITTAL-CMC-TC-MIB", "valuesStatus"))
)
if mibBuilder.loadTexts:
    alarmValues.setStatus(
        ""
    )

configChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2606, 4, 0, 10)
)
configChanged.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    configChanged.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RITTAL-CMC-TC-MIB",
    **{"rittal": rittal,
       "cmcTc": cmcTc,
       "alarmSensorUnit1": alarmSensorUnit1,
       "alarmSensorUnit2": alarmSensorUnit2,
       "alarmSensorUnit3": alarmSensorUnit3,
       "alarmSensorUnit4": alarmSensorUnit4,
       "alarmUnit1": alarmUnit1,
       "alarmUnit2": alarmUnit2,
       "alarmUnit3": alarmUnit3,
       "alarmUnit4": alarmUnit4,
       "alarmValues": alarmValues,
       "configChanged": configChanged,
       "cmcTcMibRev": cmcTcMibRev,
       "cmcTcMibMajRev": cmcTcMibMajRev,
       "cmcTcMibMinRev": cmcTcMibMinRev,
       "cmcTcMibCondition": cmcTcMibCondition,
       "cmcTcStatus": cmcTcStatus,
       "cmcTcStatusDeviceCMC": cmcTcStatusDeviceCMC,
       "cmcTcUnitsConnected": cmcTcUnitsConnected,
       "cmcTcStatusSensorUnit1": cmcTcStatusSensorUnit1,
       "cmcTcUnit1TypeOfDevice": cmcTcUnit1TypeOfDevice,
       "cmcTcUnit1Text": cmcTcUnit1Text,
       "cmcTcUnit1Serial": cmcTcUnit1Serial,
       "cmcTcUnit1Status": cmcTcUnit1Status,
       "cmcTcStatusUnit1Sensors": cmcTcStatusUnit1Sensors,
       "cmcTcUnit1NumberOfSensors": cmcTcUnit1NumberOfSensors,
       "cmcTcUnit1SensorTable": cmcTcUnit1SensorTable,
       "cmcTcUnit1SensorEntry": cmcTcUnit1SensorEntry,
       "unit1SensorIndex": unit1SensorIndex,
       "unit1SensorType": unit1SensorType,
       "unit1SensorText": unit1SensorText,
       "unit1SensorStatus": unit1SensorStatus,
       "unit1SensorValue": unit1SensorValue,
       "unit1SensorSetHigh": unit1SensorSetHigh,
       "unit1SensorSetLow": unit1SensorSetLow,
       "unit1SensorSetWarn": unit1SensorSetWarn,
       "cmcTcStatusUnit1Outputs": cmcTcStatusUnit1Outputs,
       "cmcTcUnit1NumberOfOutputs": cmcTcUnit1NumberOfOutputs,
       "cmcTcUnit1OutputTable": cmcTcUnit1OutputTable,
       "cmcTcUnit1OutputEntry": cmcTcUnit1OutputEntry,
       "unit1OutputIndex": unit1OutputIndex,
       "unit1OutputType": unit1OutputType,
       "unit1OutputText": unit1OutputText,
       "unit1OutputStatus": unit1OutputStatus,
       "unit1OutputValue": unit1OutputValue,
       "unit1OutputSet": unit1OutputSet,
       "unit1OutputConfig": unit1OutputConfig,
       "unit1OutputDelay": unit1OutputDelay,
       "unit1OutputTimeoutAction": unit1OutputTimeoutAction,
       "cmcTcStatusUnit1Msg": cmcTcStatusUnit1Msg,
       "cmcTcUnit1NumberOfMsgs": cmcTcUnit1NumberOfMsgs,
       "cmcTcUnit1MsgTable": cmcTcUnit1MsgTable,
       "cmcTcUnit1MsgEntry": cmcTcUnit1MsgEntry,
       "unit1MsgIndex": unit1MsgIndex,
       "unit1MsgText": unit1MsgText,
       "unit1MsgStatus": unit1MsgStatus,
       "unit1MsgRelay": unit1MsgRelay,
       "unit1MsgBeeper": unit1MsgBeeper,
       "unit1MsgTrap1": unit1MsgTrap1,
       "unit1MsgTrap2": unit1MsgTrap2,
       "unit1MsgTrap3": unit1MsgTrap3,
       "unit1MsgTrap4": unit1MsgTrap4,
       "unit1MsgQuit": unit1MsgQuit,
       "cmcTcStatusSensorUnit2": cmcTcStatusSensorUnit2,
       "cmcTcUnit2TypeOfDevice": cmcTcUnit2TypeOfDevice,
       "cmcTcUnit2Text": cmcTcUnit2Text,
       "cmcTcUnit2Serial": cmcTcUnit2Serial,
       "cmcTcUnit2Status": cmcTcUnit2Status,
       "cmcTcStatusUnit2Sensors": cmcTcStatusUnit2Sensors,
       "cmcTcUnit2NumberOfSensors": cmcTcUnit2NumberOfSensors,
       "cmcTcUnit2SensorTable": cmcTcUnit2SensorTable,
       "cmcTcUnit2SensorEntry": cmcTcUnit2SensorEntry,
       "unit2SensorIndex": unit2SensorIndex,
       "unit2SensorType": unit2SensorType,
       "unit2SensorText": unit2SensorText,
       "unit2SensorStatus": unit2SensorStatus,
       "unit2SensorValue": unit2SensorValue,
       "unit2SensorSetHigh": unit2SensorSetHigh,
       "unit2SensorSetLow": unit2SensorSetLow,
       "unit2SensorSetWarn": unit2SensorSetWarn,
       "cmcTcStatusUnit2Outputs": cmcTcStatusUnit2Outputs,
       "cmcTcUnit2NumberOfOutputs": cmcTcUnit2NumberOfOutputs,
       "cmcTcUnit2OutputTable": cmcTcUnit2OutputTable,
       "cmcTcUnit2OutputEntry": cmcTcUnit2OutputEntry,
       "unit2OutputIndex": unit2OutputIndex,
       "unit2OutputType": unit2OutputType,
       "unit2OutputText": unit2OutputText,
       "unit2OutputStatus": unit2OutputStatus,
       "unit2OutputValue": unit2OutputValue,
       "unit2OutputSet": unit2OutputSet,
       "unit2OutputConfig": unit2OutputConfig,
       "unit2OutputDelay": unit2OutputDelay,
       "unit2OutputTimeoutAction": unit2OutputTimeoutAction,
       "cmcTcStatusUnit2Msg": cmcTcStatusUnit2Msg,
       "cmcTcUnit2NumberOfMsgs": cmcTcUnit2NumberOfMsgs,
       "cmcTcUnit2MsgTable": cmcTcUnit2MsgTable,
       "cmcTcUnit2MsgEntry": cmcTcUnit2MsgEntry,
       "unit2MsgIndex": unit2MsgIndex,
       "unit2MsgText": unit2MsgText,
       "unit2MsgStatus": unit2MsgStatus,
       "unit2MsgRelay": unit2MsgRelay,
       "unit2MsgBeeper": unit2MsgBeeper,
       "unit2MsgTrap1": unit2MsgTrap1,
       "unit2MsgTrap2": unit2MsgTrap2,
       "unit2MsgTrap3": unit2MsgTrap3,
       "unit2MsgTrap4": unit2MsgTrap4,
       "unit2MsgQuit": unit2MsgQuit,
       "cmcTcStatusSensorUnit3": cmcTcStatusSensorUnit3,
       "cmcTcUnit3TypeOfDevice": cmcTcUnit3TypeOfDevice,
       "cmcTcUnit3Text": cmcTcUnit3Text,
       "cmcTcUnit3Serial": cmcTcUnit3Serial,
       "cmcTcUnit3Status": cmcTcUnit3Status,
       "cmcTcStatusUnit3Sensors": cmcTcStatusUnit3Sensors,
       "cmcTcUnit3NumberOfSensors": cmcTcUnit3NumberOfSensors,
       "cmcTcUnit3SensorTable": cmcTcUnit3SensorTable,
       "cmcTcUnit3SensorEntry": cmcTcUnit3SensorEntry,
       "unit3SensorIndex": unit3SensorIndex,
       "unit3SensorType": unit3SensorType,
       "unit3SensorText": unit3SensorText,
       "unit3SensorStatus": unit3SensorStatus,
       "unit3SensorValue": unit3SensorValue,
       "unit3SensorSetHigh": unit3SensorSetHigh,
       "unit3SensorSetLow": unit3SensorSetLow,
       "unit3SensorSetWarn": unit3SensorSetWarn,
       "cmcTcStatusUnit3Outputs": cmcTcStatusUnit3Outputs,
       "cmcTcUnit3NumberOfOutputs": cmcTcUnit3NumberOfOutputs,
       "cmcTcUnit3OutputTable": cmcTcUnit3OutputTable,
       "cmcTcUnit3OutputEntry": cmcTcUnit3OutputEntry,
       "unit3OutputIndex": unit3OutputIndex,
       "unit3OutputType": unit3OutputType,
       "unit3OutputText": unit3OutputText,
       "unit3OutputStatus": unit3OutputStatus,
       "unit3OutputValue": unit3OutputValue,
       "unit3OutputSet": unit3OutputSet,
       "unit3OutputConfig": unit3OutputConfig,
       "unit3OutputDelay": unit3OutputDelay,
       "unit3OutputTimeoutAction": unit3OutputTimeoutAction,
       "cmcTcStatusUnit3Msg": cmcTcStatusUnit3Msg,
       "cmcTcUnit3NumberOfMsgs": cmcTcUnit3NumberOfMsgs,
       "cmcTcUnit3MsgTable": cmcTcUnit3MsgTable,
       "cmcTcUnit3MsgEntry": cmcTcUnit3MsgEntry,
       "unit3MsgIndex": unit3MsgIndex,
       "unit3MsgText": unit3MsgText,
       "unit3MsgStatus": unit3MsgStatus,
       "unit3MsgRelay": unit3MsgRelay,
       "unit3MsgBeeper": unit3MsgBeeper,
       "unit3MsgTrap1": unit3MsgTrap1,
       "unit3MsgTrap2": unit3MsgTrap2,
       "unit3MsgTrap3": unit3MsgTrap3,
       "unit3MsgTrap4": unit3MsgTrap4,
       "unit3MsgQuit": unit3MsgQuit,
       "cmcTcStatusSensorUnit4": cmcTcStatusSensorUnit4,
       "cmcTcUnit4TypeOfDevice": cmcTcUnit4TypeOfDevice,
       "cmcTcUnit4Text": cmcTcUnit4Text,
       "cmcTcUnit4Serial": cmcTcUnit4Serial,
       "cmcTcUnit4Status": cmcTcUnit4Status,
       "cmcTcStatusUnit4Sensors": cmcTcStatusUnit4Sensors,
       "cmcTcUnit4NumberOfSensors": cmcTcUnit4NumberOfSensors,
       "cmcTcUnit4SensorTable": cmcTcUnit4SensorTable,
       "cmcTcUnit4SensorEntry": cmcTcUnit4SensorEntry,
       "unit4SensorIndex": unit4SensorIndex,
       "unit4SensorType": unit4SensorType,
       "unit4SensorText": unit4SensorText,
       "unit4SensorStatus": unit4SensorStatus,
       "unit4SensorValue": unit4SensorValue,
       "unit4SensorSetHigh": unit4SensorSetHigh,
       "unit4SensorSetLow": unit4SensorSetLow,
       "unit4SensorSetWarn": unit4SensorSetWarn,
       "cmcTcStatusUnit4Outputs": cmcTcStatusUnit4Outputs,
       "cmcTcUnit4NumberOfOutputs": cmcTcUnit4NumberOfOutputs,
       "cmcTcUnit4OutputTable": cmcTcUnit4OutputTable,
       "cmcTcUnit4OutputEntry": cmcTcUnit4OutputEntry,
       "unit4OutputIndex": unit4OutputIndex,
       "unit4OutputType": unit4OutputType,
       "unit4OutputText": unit4OutputText,
       "unit4OutputStatus": unit4OutputStatus,
       "unit4OutputValue": unit4OutputValue,
       "unit4OutputSet": unit4OutputSet,
       "unit4OutputConfig": unit4OutputConfig,
       "unit4OutputDelay": unit4OutputDelay,
       "unit4OutputTimeoutAction": unit4OutputTimeoutAction,
       "cmcTcStatusUnit4Msg": cmcTcStatusUnit4Msg,
       "cmcTcUnit4NumberOfMsgs": cmcTcUnit4NumberOfMsgs,
       "cmcTcUnit4MsgTable": cmcTcUnit4MsgTable,
       "cmcTcUnit4MsgEntry": cmcTcUnit4MsgEntry,
       "unit4MsgIndex": unit4MsgIndex,
       "unit4MsgText": unit4MsgText,
       "unit4MsgStatus": unit4MsgStatus,
       "unit4MsgRelay": unit4MsgRelay,
       "unit4MsgBeeper": unit4MsgBeeper,
       "unit4MsgTrap1": unit4MsgTrap1,
       "unit4MsgTrap2": unit4MsgTrap2,
       "unit4MsgTrap3": unit4MsgTrap3,
       "unit4MsgTrap4": unit4MsgTrap4,
       "unit4MsgQuit": unit4MsgQuit,
       "cmcTcStatusExtUnit": cmcTcStatusExtUnit,
       "cmcTcValuesRelay": cmcTcValuesRelay,
       "cmcTcValuesBeeper": cmcTcValuesBeeper,
       "cmcTcValuesTrap1": cmcTcValuesTrap1,
       "cmcTcValuesTrap2": cmcTcValuesTrap2,
       "cmcTcValuesTrap3": cmcTcValuesTrap3,
       "cmcTcValuesTrap4": cmcTcValuesTrap4,
       "cmcTcNumberOfValues": cmcTcNumberOfValues,
       "cmcTcValuesTable": cmcTcValuesTable,
       "cmcTcValuesEntry": cmcTcValuesEntry,
       "valuesIndex": valuesIndex,
       "valuesText": valuesText,
       "valuesStatus": valuesStatus,
       "valuesValue": valuesValue,
       "valuesSetHigh": valuesSetHigh,
       "valuesSetLow": valuesSetLow,
       "cmcTcSetup": cmcTcSetup,
       "cmcTcSetupGeneral": cmcTcSetupGeneral,
       "cmcTcSetTempUnit": cmcTcSetTempUnit,
       "cmcTcSetBeeper": cmcTcSetBeeper,
       "cmcTcQuitRelay": cmcTcQuitRelay,
       "cmcTcLogicRelay": cmcTcLogicRelay,
       "cmcTcWebAccess": cmcTcWebAccess,
       "cmcTcSetupDate": cmcTcSetupDate,
       "cmcTcSetupTime": cmcTcSetupTime,
       "cmcTcTimerTable1": cmcTcTimerTable1,
       "cmcTcTimerNumber": cmcTcTimerNumber,
       "cmcTcTimerTable": cmcTcTimerTable,
       "cmcTcTimerEntry": cmcTcTimerEntry,
       "cmcTcTimerIndex": cmcTcTimerIndex,
       "cmcTcTimerStatus": cmcTcTimerStatus,
       "cmcTcTimerDayOfWeek": cmcTcTimerDayOfWeek,
       "cmcTcTimeOn": cmcTcTimeOn,
       "cmcTcTimeOff": cmcTcTimeOff,
       "cmcTcTimeControl": cmcTcTimeControl,
       "cmcTcTimerFunction": cmcTcTimerFunction,
       "cmcTcTrapControl": cmcTcTrapControl,
       "cmcTcTraps": cmcTcTraps,
       "cmcTcTraptableNumber": cmcTcTraptableNumber,
       "cmcTcTrapTableTable": cmcTcTrapTableTable,
       "cmcTcTrapTableEntry": cmcTcTrapTableEntry,
       "trapIndex": trapIndex,
       "trapStatus": trapStatus,
       "trapIPaddress": trapIPaddress,
       "cmcTcControl": cmcTcControl,
       "cmcTcQuitUnit": cmcTcQuitUnit}
)
