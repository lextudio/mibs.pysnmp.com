# SNMP MIB module (ZXR10-OPTICAL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-OPTICAL-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:02 2024
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

(zxr10,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10")


# MODULE-IDENTITY

zxr10OpticalAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126)
)
zxr10OpticalAlarmMIB.setRevisions(
        ("2008-04-18 00:00",)
)


# Types definitions



class OptStatType(Integer32):
    """Custom type OptStatType based on Integer32"""
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
        *(("sfpNotSupportDom", 2),
          ("sfpOffline", 1),
          ("sfpOnlineAndHaveData", 3),
          ("sfpOnlineButNoData", 4))
    )




# TEXTUAL-CONVENTIONS



class Zxr10optAlarmType(Integer32, TextualConvention):
    status = "current"
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
        *(("alarmCurrent", 2),
          ("alarmRxPower", 4),
          ("alarmTemperature", 0),
          ("alarmTxPower", 3),
          ("alarmVoltage", 1))
    )



class Zxr10optAlarmOverType(Integer32, TextualConvention):
    status = "current"
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
        *(("highAlarm", 1),
          ("highWarning", 2),
          ("lowAlarm", 4),
          ("lowWarning", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Zxr10Notifications_ObjectIdentity = ObjectIdentity
zxr10Notifications = _Zxr10Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 0)
)
_Zxr10MIBObjects_ObjectIdentity = ObjectIdentity
zxr10MIBObjects = _Zxr10MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1)
)
_Zxr10optAlarmTable_Object = MibTable
zxr10optAlarmTable = _Zxr10optAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10optAlarmTable.setStatus("current")
_Zxr10optAlarmEntry_Object = MibTableRow
zxr10optAlarmEntry = _Zxr10optAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1)
)
zxr10optAlarmEntry.setIndexNames(
    (0, "ZXR10-OPTICAL-ALARM-MIB", "zxr10optAlarmIndex"),
)
if mibBuilder.loadTexts:
    zxr10optAlarmEntry.setStatus("current")
_Zxr10optAlarmIndex_Type = Unsigned32
_Zxr10optAlarmIndex_Object = MibTableColumn
zxr10optAlarmIndex = _Zxr10optAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 1),
    _Zxr10optAlarmIndex_Type()
)
zxr10optAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optAlarmIndex.setStatus("current")
_Zxr10optIfIndex_Type = Unsigned32
_Zxr10optIfIndex_Object = MibTableColumn
zxr10optIfIndex = _Zxr10optIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 2),
    _Zxr10optIfIndex_Type()
)
zxr10optIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optIfIndex.setStatus("current")
_Zxr10optIfName_Type = DisplayString
_Zxr10optIfName_Object = MibTableColumn
zxr10optIfName = _Zxr10optIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 3),
    _Zxr10optIfName_Type()
)
zxr10optIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optIfName.setStatus("current")
_Zxr10optAlarmType_Type = Zxr10optAlarmType
_Zxr10optAlarmType_Object = MibTableColumn
zxr10optAlarmType = _Zxr10optAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 4),
    _Zxr10optAlarmType_Type()
)
zxr10optAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optAlarmType.setStatus("current")
_Zxr10optAlarmOverType_Type = Zxr10optAlarmOverType
_Zxr10optAlarmOverType_Object = MibTableColumn
zxr10optAlarmOverType = _Zxr10optAlarmOverType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 5),
    _Zxr10optAlarmOverType_Type()
)
zxr10optAlarmOverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optAlarmOverType.setStatus("current")
_Zxr10optAlarmOverCurValue_Type = DisplayString
_Zxr10optAlarmOverCurValue_Object = MibTableColumn
zxr10optAlarmOverCurValue = _Zxr10optAlarmOverCurValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 6),
    _Zxr10optAlarmOverCurValue_Type()
)
zxr10optAlarmOverCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optAlarmOverCurValue.setStatus("current")
_Zxr10optHighAlarmValue_Type = DisplayString
_Zxr10optHighAlarmValue_Object = MibTableColumn
zxr10optHighAlarmValue = _Zxr10optHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 7),
    _Zxr10optHighAlarmValue_Type()
)
zxr10optHighAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optHighAlarmValue.setStatus("current")
_Zxr10optHighWarnValue_Type = DisplayString
_Zxr10optHighWarnValue_Object = MibTableColumn
zxr10optHighWarnValue = _Zxr10optHighWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 8),
    _Zxr10optHighWarnValue_Type()
)
zxr10optHighWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optHighWarnValue.setStatus("current")
_Zxr10optLowWarnValue_Type = DisplayString
_Zxr10optLowWarnValue_Object = MibTableColumn
zxr10optLowWarnValue = _Zxr10optLowWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 9),
    _Zxr10optLowWarnValue_Type()
)
zxr10optLowWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optLowWarnValue.setStatus("current")
_Zxr10optLowAlarmValue_Type = DisplayString
_Zxr10optLowAlarmValue_Object = MibTableColumn
zxr10optLowAlarmValue = _Zxr10optLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 1, 1, 10),
    _Zxr10optLowAlarmValue_Type()
)
zxr10optLowAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10optLowAlarmValue.setStatus("current")
_Zxr10opticalTable_Object = MibTable
zxr10opticalTable = _Zxr10opticalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10opticalTable.setStatus("current")
_Zxr10opticalEntry_Object = MibTableRow
zxr10opticalEntry = _Zxr10opticalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1)
)
zxr10opticalEntry.setIndexNames(
    (0, "ZXR10-OPTICAL-ALARM-MIB", "zxr10opticalIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10opticalEntry.setStatus("current")
_Zxr10opticalIfIndex_Type = Unsigned32
_Zxr10opticalIfIndex_Object = MibTableColumn
zxr10opticalIfIndex = _Zxr10opticalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 1),
    _Zxr10opticalIfIndex_Type()
)
zxr10opticalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalIfIndex.setStatus("current")
_Zxr10opticalState_Type = OptStatType
_Zxr10opticalState_Object = MibTableColumn
zxr10opticalState = _Zxr10opticalState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 2),
    _Zxr10opticalState_Type()
)
zxr10opticalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalState.setStatus("current")
_Zxr10opticalTxPower_Type = DisplayString
_Zxr10opticalTxPower_Object = MibTableColumn
zxr10opticalTxPower = _Zxr10opticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 3),
    _Zxr10opticalTxPower_Type()
)
zxr10opticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalTxPower.setStatus("current")
_Zxr10opticalRxPower_Type = DisplayString
_Zxr10opticalRxPower_Object = MibTableColumn
zxr10opticalRxPower = _Zxr10opticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 4),
    _Zxr10opticalRxPower_Type()
)
zxr10opticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalRxPower.setStatus("current")
_Zxr10opticalTxCurrent_Type = DisplayString
_Zxr10opticalTxCurrent_Object = MibTableColumn
zxr10opticalTxCurrent = _Zxr10opticalTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 5),
    _Zxr10opticalTxCurrent_Type()
)
zxr10opticalTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalTxCurrent.setStatus("current")
_Zxr10opticalVoltage_Type = DisplayString
_Zxr10opticalVoltage_Object = MibTableColumn
zxr10opticalVoltage = _Zxr10opticalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 6),
    _Zxr10opticalVoltage_Type()
)
zxr10opticalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalVoltage.setStatus("current")
_Zxr10opticalTemperature_Type = DisplayString
_Zxr10opticalTemperature_Object = MibTableColumn
zxr10opticalTemperature = _Zxr10opticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 1, 2, 1, 7),
    _Zxr10opticalTemperature_Type()
)
zxr10opticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10opticalTemperature.setStatus("current")

# Managed Objects groups


# Notification objects

zxr10optAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 126, 0, 1)
)
zxr10optAlarmTrap.setObjects(
      *(("ZXR10-OPTICAL-ALARM-MIB", "zxr10optAlarmIndex"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optIfIndex"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optIfName"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optAlarmType"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optAlarmOverType"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optAlarmOverCurValue"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optHighAlarmValue"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optHighWarnValue"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optLowWarnValue"),
        ("ZXR10-OPTICAL-ALARM-MIB", "zxr10optLowAlarmValue"))
)
if mibBuilder.loadTexts:
    zxr10optAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-OPTICAL-ALARM-MIB",
    **{"Zxr10optAlarmType": Zxr10optAlarmType,
       "Zxr10optAlarmOverType": Zxr10optAlarmOverType,
       "OptStatType": OptStatType,
       "zxr10OpticalAlarmMIB": zxr10OpticalAlarmMIB,
       "zxr10Notifications": zxr10Notifications,
       "zxr10optAlarmTrap": zxr10optAlarmTrap,
       "zxr10MIBObjects": zxr10MIBObjects,
       "zxr10optAlarmTable": zxr10optAlarmTable,
       "zxr10optAlarmEntry": zxr10optAlarmEntry,
       "zxr10optAlarmIndex": zxr10optAlarmIndex,
       "zxr10optIfIndex": zxr10optIfIndex,
       "zxr10optIfName": zxr10optIfName,
       "zxr10optAlarmType": zxr10optAlarmType,
       "zxr10optAlarmOverType": zxr10optAlarmOverType,
       "zxr10optAlarmOverCurValue": zxr10optAlarmOverCurValue,
       "zxr10optHighAlarmValue": zxr10optHighAlarmValue,
       "zxr10optHighWarnValue": zxr10optHighWarnValue,
       "zxr10optLowWarnValue": zxr10optLowWarnValue,
       "zxr10optLowAlarmValue": zxr10optLowAlarmValue,
       "zxr10opticalTable": zxr10opticalTable,
       "zxr10opticalEntry": zxr10opticalEntry,
       "zxr10opticalIfIndex": zxr10opticalIfIndex,
       "zxr10opticalState": zxr10opticalState,
       "zxr10opticalTxPower": zxr10opticalTxPower,
       "zxr10opticalRxPower": zxr10opticalRxPower,
       "zxr10opticalTxCurrent": zxr10opticalTxCurrent,
       "zxr10opticalVoltage": zxr10opticalVoltage,
       "zxr10opticalTemperature": zxr10opticalTemperature}
)
