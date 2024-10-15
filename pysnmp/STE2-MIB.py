# SNMP MIB module (STE2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STE2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:58 2024
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


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2),
          ("kelvin", 3),
          ("none", 0),
          ("percent", 4))
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





class IOName(DisplayString):
    """Custom type IOName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorState(Integer32):
    """Custom type SensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alarmhi", 5),
          ("alarmlo", 4),
          ("invalid", 0),
          ("normal", 1),
          ("outofrangehi", 3),
          ("outofrangelo", 2))
    )





class SensorSN(DisplayString):
    """Custom type SensorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorName(DisplayString):
    """Custom type SensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorValue(Integer32):
    """Custom type SensorValue based on Integer32"""




class SensorID(Integer32):
    """Custom type SensorID based on Integer32"""




class SensorString(DisplayString):
    """Custom type SensorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hwgroup_ObjectIdentity = ObjectIdentity
hwgroup = _Hwgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796)
)
_X390_ObjectIdentity = ObjectIdentity
x390 = _X390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4)
)
_Ste2_ObjectIdentity = ObjectIdentity
ste2 = _Ste2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9)
)
_InpTable_Object = MibTable
inpTable = _InpTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1)
)
if mibBuilder.loadTexts:
    inpTable.setStatus("mandatory")
_InpEntry_Object = MibTableRow
inpEntry = _InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1)
)
inpEntry.setIndexNames(
    (0, "STE2-MIB", "inpIndex"),
)
if mibBuilder.loadTexts:
    inpEntry.setStatus("mandatory")
_InpIndex_Type = PositiveInteger
_InpIndex_Object = MibTableColumn
inpIndex = _InpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 1),
    _InpIndex_Type()
)
inpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inpIndex.setStatus("mandatory")
_InpValue_Type = OnOff
_InpValue_Object = MibTableColumn
inpValue = _InpValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 2),
    _InpValue_Type()
)
inpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpValue.setStatus("mandatory")
_InpName_Type = IOName
_InpName_Object = MibTableColumn
inpName = _InpName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 3),
    _InpName_Type()
)
inpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpName.setStatus("mandatory")
_InpAlarmState_Type = InputAlarmState
_InpAlarmState_Object = MibTableColumn
inpAlarmState = _InpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 4),
    _InpAlarmState_Type()
)
inpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpAlarmState.setStatus("mandatory")
_SensTable_Object = MibTable
sensTable = _SensTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3)
)
if mibBuilder.loadTexts:
    sensTable.setStatus("mandatory")
_SensEntry_Object = MibTableRow
sensEntry = _SensEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1)
)
sensEntry.setIndexNames(
    (0, "STE2-MIB", "sensIndex"),
)
if mibBuilder.loadTexts:
    sensEntry.setStatus("mandatory")
_SensIndex_Type = PositiveInteger
_SensIndex_Object = MibTableColumn
sensIndex = _SensIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 1),
    _SensIndex_Type()
)
sensIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensIndex.setStatus("mandatory")
_SensName_Type = SensorName
_SensName_Object = MibTableColumn
sensName = _SensName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 2),
    _SensName_Type()
)
sensName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensName.setStatus("mandatory")
_SensState_Type = SensorState
_SensState_Object = MibTableColumn
sensState = _SensState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 3),
    _SensState_Type()
)
sensState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensState.setStatus("mandatory")
_SensString_Type = SensorString
_SensString_Object = MibTableColumn
sensString = _SensString_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 4),
    _SensString_Type()
)
sensString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensString.setStatus("mandatory")
_SensValue_Type = SensorValue
_SensValue_Object = MibTableColumn
sensValue = _SensValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 5),
    _SensValue_Type()
)
sensValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensValue.setStatus("mandatory")
_SensSN_Type = SensorSN
_SensSN_Object = MibTableColumn
sensSN = _SensSN_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 6),
    _SensSN_Type()
)
sensSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensSN.setStatus("mandatory")
_SensUnit_Type = UnitType
_SensUnit_Object = MibTableColumn
sensUnit = _SensUnit_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 7),
    _SensUnit_Type()
)
sensUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensUnit.setStatus("mandatory")
_SensID_Type = UnitType
_SensID_Object = MibTableColumn
sensID = _SensID_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 8),
    _SensID_Type()
)
sensID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensID.setStatus("mandatory")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 70)
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
    (1, 3, 6, 1, 4, 1, 21796, 4, 9, 70, 1),
    _InfoAddressMAC_Type()
)
infoAddressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAddressMAC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STE2-MIB",
    **{"PositiveInteger": PositiveInteger,
       "UnitType": UnitType,
       "OnOff": OnOff,
       "InputAlarmState": InputAlarmState,
       "IOName": IOName,
       "SensorState": SensorState,
       "SensorSN": SensorSN,
       "SensorName": SensorName,
       "SensorValue": SensorValue,
       "SensorID": SensorID,
       "SensorString": SensorString,
       "hwgroup": hwgroup,
       "x390": x390,
       "ste2": ste2,
       "inpTable": inpTable,
       "inpEntry": inpEntry,
       "inpIndex": inpIndex,
       "inpValue": inpValue,
       "inpName": inpName,
       "inpAlarmState": inpAlarmState,
       "sensTable": sensTable,
       "sensEntry": sensEntry,
       "sensIndex": sensIndex,
       "sensName": sensName,
       "sensState": sensState,
       "sensString": sensString,
       "sensValue": sensValue,
       "sensSN": sensSN,
       "sensUnit": sensUnit,
       "sensID": sensID,
       "info": info,
       "infoAddressMAC": infoAddressMAC}
)
