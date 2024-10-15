# SNMP MIB module (HWG-PWR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HWG-PWR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:49 2024
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



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class Txt8(DisplayString):
    """Custom type Txt8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )





class Txt16(DisplayString):
    """Custom type Txt16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorValue(Integer32):
    """Custom type SensorValue based on Integer32"""




class SensorID(Integer32):
    """Custom type SensorID based on Integer32"""




class OpenClose(Integer32):
    """Custom type OpenClose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 0))
    )





class AlarmState(Integer32):
    """Custom type AlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("invalid", 0),
          ("normal", 1))
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
_Hwgpwr_ObjectIdentity = ObjectIdentity
hwgpwr = _Hwgpwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6)
)
_Meters_ObjectIdentity = ObjectIdentity
meters = _Meters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1)
)
_MtNumber_Type = PositiveInteger
_MtNumber_Object = MibScalar
mtNumber = _MtNumber_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 1),
    _MtNumber_Type()
)
mtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtNumber.setStatus("mandatory")
_MtTableMeters_Object = MibTable
mtTableMeters = _MtTableMeters_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2)
)
if mibBuilder.loadTexts:
    mtTableMeters.setStatus("mandatory")
_MtEntry_Object = MibTableRow
mtEntry = _MtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1)
)
mtEntry.setIndexNames(
    (0, "HWG-PWR-MIB", "mtIndex"),
)
if mibBuilder.loadTexts:
    mtEntry.setStatus("mandatory")
_MtIndex_Type = PositiveInteger
_MtIndex_Object = MibTableColumn
mtIndex = _MtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 1),
    _MtIndex_Type()
)
mtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtIndex.setStatus("mandatory")
_MtName_Type = Txt16
_MtName_Object = MibTableColumn
mtName = _MtName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 2),
    _MtName_Type()
)
mtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtName.setStatus("mandatory")
_MtAddr_Type = PositiveInteger
_MtAddr_Object = MibTableColumn
mtAddr = _MtAddr_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 3),
    _MtAddr_Type()
)
mtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtAddr.setStatus("mandatory")
_MtSecAddr_Type = PositiveInteger
_MtSecAddr_Object = MibTableColumn
mtSecAddr = _MtSecAddr_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 4),
    _MtSecAddr_Type()
)
mtSecAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtSecAddr.setStatus("mandatory")
_MtValNumber_Type = PositiveInteger
_MtValNumber_Object = MibTableColumn
mtValNumber = _MtValNumber_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 5),
    _MtValNumber_Type()
)
mtValNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtValNumber.setStatus("mandatory")
_MtvalTableValues_Object = MibTable
mtvalTableValues = _MtvalTableValues_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3)
)
if mibBuilder.loadTexts:
    mtvalTableValues.setStatus("mandatory")
_MtvalEntry_Object = MibTableRow
mtvalEntry = _MtvalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1)
)
mtvalEntry.setIndexNames(
    (0, "HWG-PWR-MIB", "mtvalIndex"),
)
if mibBuilder.loadTexts:
    mtvalEntry.setStatus("mandatory")
_MtvalIndex_Type = PositiveInteger
_MtvalIndex_Object = MibTableColumn
mtvalIndex = _MtvalIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 1),
    _MtvalIndex_Type()
)
mtvalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtvalIndex.setStatus("mandatory")
_MtvalName_Type = Txt16
_MtvalName_Object = MibTableColumn
mtvalName = _MtvalName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 2),
    _MtvalName_Type()
)
mtvalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtvalName.setStatus("mandatory")
_MtvalUnit_Type = Txt8
_MtvalUnit_Object = MibTableColumn
mtvalUnit = _MtvalUnit_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 3),
    _MtvalUnit_Type()
)
mtvalUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtvalUnit.setStatus("mandatory")
_MtvalTarif_Type = PositiveInteger
_MtvalTarif_Object = MibTableColumn
mtvalTarif = _MtvalTarif_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 4),
    _MtvalTarif_Type()
)
mtvalTarif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtvalTarif.setStatus("mandatory")
_MtvalExp_Type = PositiveInteger
_MtvalExp_Object = MibTableColumn
mtvalExp = _MtvalExp_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 5),
    _MtvalExp_Type()
)
mtvalExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtvalExp.setStatus("mandatory")
_MtvalMbusValue_Type = PositiveInteger
_MtvalMbusValue_Object = MibTableColumn
mtvalMbusValue = _MtvalMbusValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 6),
    _MtvalMbusValue_Type()
)
mtvalMbusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtvalMbusValue.setStatus("mandatory")
_MtvalTxtValue_Type = Txt8
_MtvalTxtValue_Object = MibTableColumn
mtvalTxtValue = _MtvalTxtValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 7),
    _MtvalTxtValue_Type()
)
mtvalTxtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtvalTxtValue.setStatus("mandatory")
_MtvalAlarmState_Type = AlarmState
_MtvalAlarmState_Object = MibTableColumn
mtvalAlarmState = _MtvalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 8),
    _MtvalAlarmState_Type()
)
mtvalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtvalAlarmState.setStatus("mandatory")
_MtvalZeroOffset_Type = Integer32
_MtvalZeroOffset_Object = MibTableColumn
mtvalZeroOffset = _MtvalZeroOffset_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 9),
    _MtvalZeroOffset_Type()
)
mtvalZeroOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtvalZeroOffset.setStatus("mandatory")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2)
)
_InpNumber_Type = PositiveInteger
_InpNumber_Object = MibScalar
inpNumber = _InpNumber_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 1),
    _InpNumber_Type()
)
inpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpNumber.setStatus("mandatory")
_InpTable_Object = MibTable
inpTable = _InpTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2)
)
if mibBuilder.loadTexts:
    inpTable.setStatus("mandatory")
_InpEntry_Object = MibTableRow
inpEntry = _InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1)
)
inpEntry.setIndexNames(
    (0, "HWG-PWR-MIB", "inpIndex"),
)
if mibBuilder.loadTexts:
    inpEntry.setStatus("mandatory")
_InpIndex_Type = PositiveInteger
_InpIndex_Object = MibTableColumn
inpIndex = _InpIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 1),
    _InpIndex_Type()
)
inpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpIndex.setStatus("mandatory")
_InpName_Type = Txt16
_InpName_Object = MibTableColumn
inpName = _InpName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 2),
    _InpName_Type()
)
inpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inpName.setStatus("mandatory")
_InpValue_Type = OpenClose
_InpValue_Object = MibTableColumn
inpValue = _InpValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 3),
    _InpValue_Type()
)
inpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpValue.setStatus("mandatory")
_InpValueName_Type = Txt8
_InpValueName_Object = MibTableColumn
inpValueName = _InpValueName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 4),
    _InpValueName_Type()
)
inpValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpValueName.setStatus("mandatory")
_InpAlarmState_Type = AlarmState
_InpAlarmState_Object = MibTableColumn
inpAlarmState = _InpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 5),
    _InpAlarmState_Type()
)
inpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpAlarmState.setStatus("mandatory")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 70)
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
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 70, 1),
    _InfoAddressMAC_Type()
)
infoAddressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAddressMAC.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pwrStateToAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 0, 1)
)
pwrStateToAlarm.setObjects(
      *(("HWG-PWR-MIB", "mtvalIndex"),
        ("HWG-PWR-MIB", "mtvalName"),
        ("HWG-PWR-MIB", "mtvalUnit"),
        ("HWG-PWR-MIB", "mtvalTarif"),
        ("HWG-PWR-MIB", "mtvalExp"),
        ("HWG-PWR-MIB", "mtvalValue"),
        ("HWG-PWR-MIB", "mtvalTxtValue"),
        ("HWG-PWR-MIB", "mtvalAlarmState"))
)
if mibBuilder.loadTexts:
    pwrStateToAlarm.setStatus(
        ""
    )

pwrStateToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 0, 2)
)
pwrStateToNormal.setObjects(
      *(("HWG-PWR-MIB", "mtvalIndex"),
        ("HWG-PWR-MIB", "mtvalName"),
        ("HWG-PWR-MIB", "mtvalUnit"),
        ("HWG-PWR-MIB", "mtvalTarif"),
        ("HWG-PWR-MIB", "mtvalExp"),
        ("HWG-PWR-MIB", "mtvalValue"),
        ("HWG-PWR-MIB", "mtvalTxtValue"),
        ("HWG-PWR-MIB", "mtvalAlarmState"))
)
if mibBuilder.loadTexts:
    pwrStateToNormal.setStatus(
        ""
    )

inContactStateToAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 0, 3)
)
inContactStateToAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("HWG-PWR-MIB", "infoAddressMAC"),
        ("HWG-PWR-MIB", "inpIndex"),
        ("HWG-PWR-MIB", "inpName"),
        ("HWG-PWR-MIB", "inpValue"),
        ("HWG-PWR-MIB", "inpValueName"),
        ("HWG-PWR-MIB", "inpAlarmState"))
)
if mibBuilder.loadTexts:
    inContactStateToAlarm.setStatus(
        ""
    )

inContactStateToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 6, 0, 4)
)
inContactStateToNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("HWG-PWR-MIB", "infoAddressMAC"),
        ("HWG-PWR-MIB", "inpIndex"),
        ("HWG-PWR-MIB", "inpName"),
        ("HWG-PWR-MIB", "inpValue"),
        ("HWG-PWR-MIB", "inpValueName"),
        ("HWG-PWR-MIB", "inpAlarmState"))
)
if mibBuilder.loadTexts:
    inContactStateToNormal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HWG-PWR-MIB",
    **{"PositiveInteger": PositiveInteger,
       "Txt8": Txt8,
       "Txt16": Txt16,
       "SensorValue": SensorValue,
       "SensorID": SensorID,
       "OpenClose": OpenClose,
       "AlarmState": AlarmState,
       "hwgroup": hwgroup,
       "x390": x390,
       "hwgpwr": hwgpwr,
       "pwrStateToAlarm": pwrStateToAlarm,
       "pwrStateToNormal": pwrStateToNormal,
       "inContactStateToAlarm": inContactStateToAlarm,
       "inContactStateToNormal": inContactStateToNormal,
       "meters": meters,
       "mtNumber": mtNumber,
       "mtTableMeters": mtTableMeters,
       "mtEntry": mtEntry,
       "mtIndex": mtIndex,
       "mtName": mtName,
       "mtAddr": mtAddr,
       "mtSecAddr": mtSecAddr,
       "mtValNumber": mtValNumber,
       "mtvalTableValues": mtvalTableValues,
       "mtvalEntry": mtvalEntry,
       "mtvalIndex": mtvalIndex,
       "mtvalName": mtvalName,
       "mtvalUnit": mtvalUnit,
       "mtvalTarif": mtvalTarif,
       "mtvalExp": mtvalExp,
       "mtvalMbusValue": mtvalMbusValue,
       "mtvalTxtValue": mtvalTxtValue,
       "mtvalAlarmState": mtvalAlarmState,
       "mtvalZeroOffset": mtvalZeroOffset,
       "input": input,
       "inpNumber": inpNumber,
       "inpTable": inpTable,
       "inpEntry": inpEntry,
       "inpIndex": inpIndex,
       "inpName": inpName,
       "inpValue": inpValue,
       "inpValueName": inpValueName,
       "inpAlarmState": inpAlarmState,
       "info": info,
       "infoAddressMAC": infoAddressMAC}
)
