# SNMP MIB module (HYTERA-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HYTERA-REPEATER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:51 2024
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HyteraRepeaterMIB_ObjectIdentity = ObjectIdentity
hyteraRepeaterMIB = _HyteraRepeaterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2)
)
_RptRealTimeInfo_ObjectIdentity = ObjectIdentity
rptRealTimeInfo = _RptRealTimeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1)
)
_RptAlarmInfo_ObjectIdentity = ObjectIdentity
rptAlarmInfo = _RptAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1)
)


class _RptVoltageAlarm_Type(Integer32):
    """Custom type rptVoltageAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RptVoltageAlarm_Type.__name__ = "Integer32"
_RptVoltageAlarm_Object = MibScalar
rptVoltageAlarm = _RptVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 1),
    _RptVoltageAlarm_Type()
)
rptVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptVoltageAlarm.setStatus("mandatory")


class _RptTemperatureAlarm_Type(Integer32):
    """Custom type rptTemperatureAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RptTemperatureAlarm_Type.__name__ = "Integer32"
_RptTemperatureAlarm_Object = MibScalar
rptTemperatureAlarm = _RptTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 2),
    _RptTemperatureAlarm_Type()
)
rptTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptTemperatureAlarm.setStatus("mandatory")


class _RptFanAlarm_Type(Integer32):
    """Custom type rptFanAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptFanAlarm_Type.__name__ = "Integer32"
_RptFanAlarm_Object = MibScalar
rptFanAlarm = _RptFanAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 3),
    _RptFanAlarm_Type()
)
rptFanAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptFanAlarm.setStatus("optional")


class _RptForwardAlarm_Type(Integer32):
    """Custom type rptForwardAlarm based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_RptForwardAlarm_Type.__name__ = "Integer32"
_RptForwardAlarm_Object = MibScalar
rptForwardAlarm = _RptForwardAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 4),
    _RptForwardAlarm_Type()
)
rptForwardAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptForwardAlarm.setStatus("optional")


class _RptReflectedAlarm_Type(Integer32):
    """Custom type rptReflectedAlarm based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_RptReflectedAlarm_Type.__name__ = "Integer32"
_RptReflectedAlarm_Object = MibScalar
rptReflectedAlarm = _RptReflectedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 5),
    _RptReflectedAlarm_Type()
)
rptReflectedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptReflectedAlarm.setStatus("optional")


class _RptVswrAlarm_Type(Integer32):
    """Custom type rptVswrAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptVswrAlarm_Type.__name__ = "Integer32"
_RptVswrAlarm_Object = MibScalar
rptVswrAlarm = _RptVswrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 6),
    _RptVswrAlarm_Type()
)
rptVswrAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptVswrAlarm.setStatus("mandatory")


class _RptTxPllAlarm_Type(Integer32):
    """Custom type rptTxPllAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptTxPllAlarm_Type.__name__ = "Integer32"
_RptTxPllAlarm_Object = MibScalar
rptTxPllAlarm = _RptTxPllAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 7),
    _RptTxPllAlarm_Type()
)
rptTxPllAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptTxPllAlarm.setStatus("mandatory")


class _RptRxPllAlarm_Type(Integer32):
    """Custom type rptRxPllAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptRxPllAlarm_Type.__name__ = "Integer32"
_RptRxPllAlarm_Object = MibScalar
rptRxPllAlarm = _RptRxPllAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 8),
    _RptRxPllAlarm_Type()
)
rptRxPllAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptRxPllAlarm.setStatus("mandatory")


class _RptBatteryVoltageAlarm_Type(Integer32):
    """Custom type rptBatteryVoltageAlarm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RptBatteryVoltageAlarm_Type.__name__ = "Integer32"
_RptBatteryVoltageAlarm_Object = MibScalar
rptBatteryVoltageAlarm = _RptBatteryVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 1, 9),
    _RptBatteryVoltageAlarm_Type()
)
rptBatteryVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptBatteryVoltageAlarm.setStatus("mandatory")
_RptDataInfo_ObjectIdentity = ObjectIdentity
rptDataInfo = _RptDataInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2)
)


class _RptVoltage_Type(OctetString):
    """Custom type rptVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptVoltage_Type.__name__ = "OctetString"
_RptVoltage_Object = MibScalar
rptVoltage = _RptVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 1),
    _RptVoltage_Type()
)
rptVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptVoltage.setStatus("mandatory")


class _RptPaTemprature_Type(OctetString):
    """Custom type rptPaTemprature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptPaTemprature_Type.__name__ = "OctetString"
_RptPaTemprature_Object = MibScalar
rptPaTemprature = _RptPaTemprature_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 2),
    _RptPaTemprature_Type()
)
rptPaTemprature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptPaTemprature.setStatus("mandatory")
_RptFanSpeed_Type = Integer32
_RptFanSpeed_Object = MibScalar
rptFanSpeed = _RptFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 3),
    _RptFanSpeed_Type()
)
rptFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptFanSpeed.setStatus("optional")


class _RptVswr_Type(OctetString):
    """Custom type rptVswr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptVswr_Type.__name__ = "OctetString"
_RptVswr_Object = MibScalar
rptVswr = _RptVswr_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 4),
    _RptVswr_Type()
)
rptVswr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptVswr.setStatus("mandatory")


class _RptTxFwdPower_Type(OctetString):
    """Custom type rptTxFwdPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptTxFwdPower_Type.__name__ = "OctetString"
_RptTxFwdPower_Object = MibScalar
rptTxFwdPower = _RptTxFwdPower_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 5),
    _RptTxFwdPower_Type()
)
rptTxFwdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptTxFwdPower.setStatus("mandatory")


class _RptTxRefPower_Type(OctetString):
    """Custom type rptTxRefPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptTxRefPower_Type.__name__ = "OctetString"
_RptTxRefPower_Object = MibScalar
rptTxRefPower = _RptTxRefPower_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 6),
    _RptTxRefPower_Type()
)
rptTxRefPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptTxRefPower.setStatus("mandatory")


class _RptDataInfoBak1_Type(OctetString):
    """Custom type rptDataInfoBak1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptDataInfoBak1_Type.__name__ = "OctetString"
_RptDataInfoBak1_Object = MibScalar
rptDataInfoBak1 = _RptDataInfoBak1_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 7),
    _RptDataInfoBak1_Type()
)
rptDataInfoBak1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptDataInfoBak1.setStatus("optional")


class _RptDataInfoBak2_Type(OctetString):
    """Custom type rptDataInfoBak2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptDataInfoBak2_Type.__name__ = "OctetString"
_RptDataInfoBak2_Object = MibScalar
rptDataInfoBak2 = _RptDataInfoBak2_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 8),
    _RptDataInfoBak2_Type()
)
rptDataInfoBak2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptDataInfoBak2.setStatus("optional")


class _RptSlot1Rssi_Type(Integer32):
    """Custom type rptSlot1Rssi based on Integer32"""
    defaultValue = -200


_RptSlot1Rssi_Object = MibScalar
rptSlot1Rssi = _RptSlot1Rssi_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 9),
    _RptSlot1Rssi_Type()
)
rptSlot1Rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptSlot1Rssi.setStatus("mandatory")


class _RptSlot2Rssi_Type(Integer32):
    """Custom type rptSlot2Rssi based on Integer32"""
    defaultValue = -200


_RptSlot2Rssi_Object = MibScalar
rptSlot2Rssi = _RptSlot2Rssi_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 10),
    _RptSlot2Rssi_Type()
)
rptSlot2Rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptSlot2Rssi.setStatus("mandatory")
_RptSupplyPowerType_Type = Integer32
_RptSupplyPowerType_Object = MibScalar
rptSupplyPowerType = _RptSupplyPowerType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 11),
    _RptSupplyPowerType_Type()
)
rptSupplyPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptSupplyPowerType.setStatus("mandatory")
_RptBatteryConnect_Type = Integer32
_RptBatteryConnect_Object = MibScalar
rptBatteryConnect = _RptBatteryConnect_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 12),
    _RptBatteryConnect_Type()
)
rptBatteryConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptBatteryConnect.setStatus("mandatory")


class _RptBatteryVoltage_Type(OctetString):
    """Custom type rptBatteryVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RptBatteryVoltage_Type.__name__ = "OctetString"
_RptBatteryVoltage_Object = MibScalar
rptBatteryVoltage = _RptBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 1, 2, 13),
    _RptBatteryVoltage_Type()
)
rptBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptBatteryVoltage.setStatus("optional")
_RptControl_ObjectIdentity = ObjectIdentity
rptControl = _RptControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2)
)


class _RptRestart_Type(Integer32):
    """Custom type rptRestart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptRestart_Type.__name__ = "Integer32"
_RptRestart_Object = MibScalar
rptRestart = _RptRestart_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 1),
    _RptRestart_Type()
)
rptRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptRestart.setStatus("mandatory")


class _RptChannelNumber_Type(Integer32):
    """Custom type rptChannelNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RptChannelNumber_Type.__name__ = "Integer32"
_RptChannelNumber_Object = MibScalar
rptChannelNumber = _RptChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 2),
    _RptChannelNumber_Type()
)
rptChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptChannelNumber.setStatus("mandatory")


class _RptChannelType_Type(Integer32):
    """Custom type rptChannelType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RptChannelType_Type.__name__ = "Integer32"
_RptChannelType_Object = MibScalar
rptChannelType = _RptChannelType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 3),
    _RptChannelType_Type()
)
rptChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptChannelType.setStatus("mandatory")


class _RptControlObjBak1_Type(Integer32):
    """Custom type rptControlObjBak1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptControlObjBak1_Type.__name__ = "Integer32"
_RptControlObjBak1_Object = MibScalar
rptControlObjBak1 = _RptControlObjBak1_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 4),
    _RptControlObjBak1_Type()
)
rptControlObjBak1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptControlObjBak1.setStatus("optional")


class _RptTxPowerLevel_Type(Integer32):
    """Custom type rptTxPowerLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
    )


_RptTxPowerLevel_Type.__name__ = "Integer32"
_RptTxPowerLevel_Object = MibScalar
rptTxPowerLevel = _RptTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 5),
    _RptTxPowerLevel_Type()
)
rptTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptTxPowerLevel.setStatus("mandatory")


class _RptKnockdown_Type(Integer32):
    """Custom type rptKnockdown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptKnockdown_Type.__name__ = "Integer32"
_RptKnockdown_Object = MibScalar
rptKnockdown = _RptKnockdown_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 6),
    _RptKnockdown_Type()
)
rptKnockdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptKnockdown.setStatus("mandatory")


class _RptRadioState_Type(Integer32):
    """Custom type rptRadioState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptRadioState_Type.__name__ = "Integer32"
_RptRadioState_Object = MibScalar
rptRadioState = _RptRadioState_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 7),
    _RptRadioState_Type()
)
rptRadioState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptRadioState.setStatus("mandatory")
_RptSnmpTrapIp_Type = IpAddress
_RptSnmpTrapIp_Object = MibScalar
rptSnmpTrapIp = _RptSnmpTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 8),
    _RptSnmpTrapIp_Type()
)
rptSnmpTrapIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptSnmpTrapIp.setStatus("mandatory")


class _RptSnmpTrapPort_Type(Integer32):
    """Custom type rptSnmpTrapPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(162, 162),
    )


_RptSnmpTrapPort_Type.__name__ = "Integer32"
_RptSnmpTrapPort_Object = MibScalar
rptSnmpTrapPort = _RptSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 9),
    _RptSnmpTrapPort_Type()
)
rptSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptSnmpTrapPort.setStatus("mandatory")
_RptchannelParaTable_Object = MibTable
rptchannelParaTable = _RptchannelParaTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rptchannelParaTable.setStatus("mandatory")
_ChannelParaEntry_Object = MibTableRow
channelParaEntry = _ChannelParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1)
)
channelParaEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "channelParaIndex"),
)
if mibBuilder.loadTexts:
    channelParaEntry.setStatus("mandatory")
_ChannelParaIndex_Type = Integer32
_ChannelParaIndex_Object = MibTableColumn
channelParaIndex = _ChannelParaIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 1),
    _ChannelParaIndex_Type()
)
channelParaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelParaIndex.setStatus("mandatory")


class _ActChannelAlias_Type(OctetString):
    """Custom type actChannelAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ActChannelAlias_Type.__name__ = "OctetString"
_ActChannelAlias_Object = MibTableColumn
actChannelAlias = _ActChannelAlias_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 2),
    _ActChannelAlias_Type()
)
actChannelAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actChannelAlias.setStatus("mandatory")
_ActChannelType_Type = Integer32
_ActChannelType_Object = MibTableColumn
actChannelType = _ActChannelType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 3),
    _ActChannelType_Type()
)
actChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actChannelType.setStatus("mandatory")
_ActTxPower_Type = Integer32
_ActTxPower_Object = MibTableColumn
actTxPower = _ActTxPower_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 4),
    _ActTxPower_Type()
)
actTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actTxPower.setStatus("mandatory")
_ActChannelNo_Type = Integer32
_ActChannelNo_Object = MibTableColumn
actChannelNo = _ActChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 5),
    _ActChannelNo_Type()
)
actChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actChannelNo.setStatus("mandatory")
_ActChannelSubNo_Type = Integer32
_ActChannelSubNo_Object = MibTableColumn
actChannelSubNo = _ActChannelSubNo_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 10, 1, 6),
    _ActChannelSubNo_Type()
)
actChannelSubNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actChannelSubNo.setStatus("mandatory")


class _RptForbid_Type(Integer32):
    """Custom type rptForbid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RptForbid_Type.__name__ = "Integer32"
_RptForbid_Object = MibScalar
rptForbid = _RptForbid_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 2, 11),
    _RptForbid_Type()
)
rptForbid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptForbid.setStatus("mandatory")
_RptLog_ObjectIdentity = ObjectIdentity
rptLog = _RptLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1, 1)
)
logEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")


class _AlarmName_Type(Integer32):
    """Custom type alarmName based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
        ValueRangeConstraint(65535, 65535),
    )


_AlarmName_Type.__name__ = "Integer32"
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1, 1, 2),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("mandatory")


class _AlarmStatus_Type(Integer32):
    """Custom type alarmStatus based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(65535, 65535),
    )


_AlarmStatus_Type.__name__ = "Integer32"
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1, 1, 3),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")


class _LogTime_Type(Integer32):
    """Custom type logTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 134217728),
    )


_LogTime_Type.__name__ = "Integer32"
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 1, 1, 4),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")


class _ClearLog_Type(Integer32):
    """Custom type clearLog based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ClearLog_Type.__name__ = "Integer32"
_ClearLog_Object = MibScalar
clearLog = _ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 2),
    _ClearLog_Type()
)
clearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearLog.setStatus("mandatory")


class _RecordCount_Type(Integer32):
    """Custom type recordCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RecordCount_Type.__name__ = "Integer32"
_RecordCount_Object = MibScalar
recordCount = _RecordCount_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 3),
    _RecordCount_Type()
)
recordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordCount.setStatus("mandatory")


class _LatestRecordPosition_Type(Integer32):
    """Custom type latestRecordPosition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LatestRecordPosition_Type.__name__ = "Integer32"
_LatestRecordPosition_Object = MibScalar
latestRecordPosition = _LatestRecordPosition_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 3, 4),
    _LatestRecordPosition_Type()
)
latestRecordPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latestRecordPosition.setStatus("mandatory")
_RptSystemInfo_ObjectIdentity = ObjectIdentity
rptSystemInfo = _RptSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4)
)


class _RptModelName_Type(OctetString):
    """Custom type rptModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RptModelName_Type.__name__ = "OctetString"
_RptModelName_Object = MibScalar
rptModelName = _RptModelName_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 1),
    _RptModelName_Type()
)
rptModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptModelName.setStatus("mandatory")


class _RptModelNo_Type(OctetString):
    """Custom type rptModelNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RptModelNo_Type.__name__ = "OctetString"
_RptModelNo_Object = MibScalar
rptModelNo = _RptModelNo_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 2),
    _RptModelNo_Type()
)
rptModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptModelNo.setStatus("mandatory")


class _RptFirmwareVersion_Type(OctetString):
    """Custom type rptFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RptFirmwareVersion_Type.__name__ = "OctetString"
_RptFirmwareVersion_Object = MibScalar
rptFirmwareVersion = _RptFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 3),
    _RptFirmwareVersion_Type()
)
rptFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptFirmwareVersion.setStatus("mandatory")


class _RptRcdbVersion_Type(OctetString):
    """Custom type rptRcdbVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RptRcdbVersion_Type.__name__ = "OctetString"
_RptRcdbVersion_Object = MibScalar
rptRcdbVersion = _RptRcdbVersion_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 4),
    _RptRcdbVersion_Type()
)
rptRcdbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptRcdbVersion.setStatus("mandatory")


class _RptSerialNo_Type(OctetString):
    """Custom type rptSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RptSerialNo_Type.__name__ = "OctetString"
_RptSerialNo_Object = MibScalar
rptSerialNo = _RptSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 5),
    _RptSerialNo_Type()
)
rptSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptSerialNo.setStatus("mandatory")


class _RptRadioAlias_Type(OctetString):
    """Custom type rptRadioAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RptRadioAlias_Type.__name__ = "OctetString"
_RptRadioAlias_Object = MibScalar
rptRadioAlias = _RptRadioAlias_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 6),
    _RptRadioAlias_Type()
)
rptRadioAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptRadioAlias.setStatus("mandatory")
_RptRadioID_Type = Integer32
_RptRadioID_Object = MibScalar
rptRadioID = _RptRadioID_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 7),
    _RptRadioID_Type()
)
rptRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptRadioID.setStatus("mandatory")


class _RptCurChannelType_Type(Integer32):
    """Custom type rptCurChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RptCurChannelType_Type.__name__ = "Integer32"
_RptCurChannelType_Object = MibScalar
rptCurChannelType = _RptCurChannelType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 8),
    _RptCurChannelType_Type()
)
rptCurChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptCurChannelType.setStatus("mandatory")


class _RptChannelName_Type(OctetString):
    """Custom type rptChannelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RptChannelName_Type.__name__ = "OctetString"
_RptChannelName_Object = MibScalar
rptChannelName = _RptChannelName_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 9),
    _RptChannelName_Type()
)
rptChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptChannelName.setStatus("mandatory")


class _RptCurTxFreq_Type(Integer32):
    """Custom type rptCurTxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_RptCurTxFreq_Type.__name__ = "Integer32"
_RptCurTxFreq_Object = MibScalar
rptCurTxFreq = _RptCurTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 10),
    _RptCurTxFreq_Type()
)
rptCurTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptCurTxFreq.setStatus("mandatory")


class _RptCurRxFreq_Type(Integer32):
    """Custom type rptCurRxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_RptCurRxFreq_Type.__name__ = "Integer32"
_RptCurRxFreq_Object = MibScalar
rptCurRxFreq = _RptCurRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 11),
    _RptCurRxFreq_Type()
)
rptCurRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptCurRxFreq.setStatus("mandatory")
_RptWorkState_Type = Integer32
_RptWorkState_Object = MibScalar
rptWorkState = _RptWorkState_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 12),
    _RptWorkState_Type()
)
rptWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptWorkState.setStatus("mandatory")


class _RptCurZoneAlias_Type(OctetString):
    """Custom type rptCurZoneAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_RptCurZoneAlias_Type.__name__ = "OctetString"
_RptCurZoneAlias_Object = MibScalar
rptCurZoneAlias = _RptCurZoneAlias_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 4, 13),
    _RptCurZoneAlias_Type()
)
rptCurZoneAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptCurZoneAlias.setStatus("mandatory")
_RptConfiguration_ObjectIdentity = ObjectIdentity
rptConfiguration = _RptConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5)
)
_RptBasicSetting_ObjectIdentity = ObjectIdentity
rptBasicSetting = _RptBasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1)
)
_PowerOn_ObjectIdentity = ObjectIdentity
powerOn = _PowerOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 1)
)


class _DesignatedPowerOnChn_Type(Integer32):
    """Custom type designatedPowerOnChn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DesignatedPowerOnChn_Type.__name__ = "Integer32"
_DesignatedPowerOnChn_Object = MibScalar
designatedPowerOnChn = _DesignatedPowerOnChn_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 1, 1),
    _DesignatedPowerOnChn_Type()
)
designatedPowerOnChn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    designatedPowerOnChn.setStatus("mandatory")


class _PowerOnChannelNo_Type(Integer32):
    """Custom type powerOnChannelNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(65535, 65535),
    )


_PowerOnChannelNo_Type.__name__ = "Integer32"
_PowerOnChannelNo_Object = MibScalar
powerOnChannelNo = _PowerOnChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 1, 2),
    _PowerOnChannelNo_Type()
)
powerOnChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerOnChannelNo.setStatus("mandatory")
_Microphone_ObjectIdentity = ObjectIdentity
microphone = _Microphone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 2)
)


class _InternalMicGain_Type(Integer32):
    """Custom type internalMicGain based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 36),
    )


_InternalMicGain_Type.__name__ = "Integer32"
_InternalMicGain_Object = MibScalar
internalMicGain = _InternalMicGain_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 2, 1),
    _InternalMicGain_Type()
)
internalMicGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMicGain.setStatus("mandatory")


class _ExternalMicGain_Type(Integer32):
    """Custom type externalMicGain based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 36),
    )


_ExternalMicGain_Type.__name__ = "Integer32"
_ExternalMicGain_Object = MibScalar
externalMicGain = _ExternalMicGain_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 2, 2),
    _ExternalMicGain_Type()
)
externalMicGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalMicGain.setStatus("mandatory")
_MultiCTCCDCTable_Object = MibTable
multiCTCCDCTable = _MultiCTCCDCTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    multiCTCCDCTable.setStatus("mandatory")
_MultiCTCCDCEntry_Object = MibTableRow
multiCTCCDCEntry = _MultiCTCCDCEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1)
)
multiCTCCDCEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "ctcssIndex"),
)
if mibBuilder.loadTexts:
    multiCTCCDCEntry.setStatus("mandatory")


class _CtcssIndex_Type(Integer32):
    """Custom type ctcssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CtcssIndex_Type.__name__ = "Integer32"
_CtcssIndex_Object = MibTableColumn
ctcssIndex = _CtcssIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1, 1),
    _CtcssIndex_Type()
)
ctcssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcssIndex.setStatus("mandatory")


class _TxCtcssFrequency_Type(Integer32):
    """Custom type txCtcssFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(670, 2541),
    )


_TxCtcssFrequency_Type.__name__ = "Integer32"
_TxCtcssFrequency_Object = MibTableColumn
txCtcssFrequency = _TxCtcssFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1, 2),
    _TxCtcssFrequency_Type()
)
txCtcssFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txCtcssFrequency.setStatus("mandatory")


class _TxCtcssType_Type(Integer32):
    """Custom type txCtcssType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TxCtcssType_Type.__name__ = "Integer32"
_TxCtcssType_Object = MibTableColumn
txCtcssType = _TxCtcssType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1, 3),
    _TxCtcssType_Type()
)
txCtcssType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txCtcssType.setStatus("mandatory")


class _RxCtcssFrequency_Type(Integer32):
    """Custom type rxCtcssFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(670, 2541),
    )


_RxCtcssFrequency_Type.__name__ = "Integer32"
_RxCtcssFrequency_Object = MibTableColumn
rxCtcssFrequency = _RxCtcssFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1, 4),
    _RxCtcssFrequency_Type()
)
rxCtcssFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxCtcssFrequency.setStatus("mandatory")


class _RxCtcssType_Type(Integer32):
    """Custom type rxCtcssType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RxCtcssType_Type.__name__ = "Integer32"
_RxCtcssType_Object = MibTableColumn
rxCtcssType = _RxCtcssType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 3, 1, 5),
    _RxCtcssType_Type()
)
rxCtcssType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxCtcssType.setStatus("mandatory")
_AudioPriority_ObjectIdentity = ObjectIdentity
audioPriority = _AudioPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 4)
)


class _PathPriority_Type(Integer32):
    """Custom type pathPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PathPriority_Type.__name__ = "Integer32"
_PathPriority_Object = MibScalar
pathPriority = _PathPriority_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 4, 1),
    _PathPriority_Type()
)
pathPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathPriority.setStatus("mandatory")


class _PttPriority_Type(Integer32):
    """Custom type pttPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PttPriority_Type.__name__ = "Integer32"
_PttPriority_Object = MibScalar
pttPriority = _PttPriority_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 4, 2),
    _PttPriority_Type()
)
pttPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pttPriority.setStatus("mandatory")


class _JitterBufferLenth_Type(Integer32):
    """Custom type jitterBufferLenth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_JitterBufferLenth_Type.__name__ = "Integer32"
_JitterBufferLenth_Object = MibScalar
jitterBufferLenth = _JitterBufferLenth_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 5),
    _JitterBufferLenth_Type()
)
jitterBufferLenth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jitterBufferLenth.setStatus("mandatory")


class _AnalogCallHangTime_Type(Integer32):
    """Custom type analogCallHangTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_AnalogCallHangTime_Type.__name__ = "Integer32"
_AnalogCallHangTime_Object = MibScalar
analogCallHangTime = _AnalogCallHangTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 6),
    _AnalogCallHangTime_Type()
)
analogCallHangTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogCallHangTime.setStatus("mandatory")


class _RepeatRequestPriority_Type(Integer32):
    """Custom type repeatRequestPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RepeatRequestPriority_Type.__name__ = "Integer32"
_RepeatRequestPriority_Object = MibScalar
repeatRequestPriority = _RepeatRequestPriority_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 1, 7),
    _RepeatRequestPriority_Type()
)
repeatRequestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeatRequestPriority.setStatus("mandatory")
_RptDigitalChannelSetting_ObjectIdentity = ObjectIdentity
rptDigitalChannelSetting = _RptDigitalChannelSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2)
)
_DigitalChnTable_Object = MibTable
digitalChnTable = _DigitalChnTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    digitalChnTable.setStatus("mandatory")
_DigitalChnEntry_Object = MibTableRow
digitalChnEntry = _DigitalChnEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1)
)
digitalChnEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "digitalChnIndex"),
)
if mibBuilder.loadTexts:
    digitalChnEntry.setStatus("mandatory")


class _DigitalChnIndex_Type(Integer32):
    """Custom type digitalChnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DigitalChnIndex_Type.__name__ = "Integer32"
_DigitalChnIndex_Object = MibTableColumn
digitalChnIndex = _DigitalChnIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 1),
    _DigitalChnIndex_Type()
)
digitalChnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalChnIndex.setStatus("mandatory")


class _DigitalColorCode_Type(Integer32):
    """Custom type digitalColorCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DigitalColorCode_Type.__name__ = "Integer32"
_DigitalColorCode_Object = MibTableColumn
digitalColorCode = _DigitalColorCode_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 2),
    _DigitalColorCode_Type()
)
digitalColorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalColorCode.setStatus("mandatory")


class _DigitalIpMultisiteConnect_Type(Integer32):
    """Custom type digitalIpMultisiteConnect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_DigitalIpMultisiteConnect_Type.__name__ = "Integer32"
_DigitalIpMultisiteConnect_Object = MibTableColumn
digitalIpMultisiteConnect = _DigitalIpMultisiteConnect_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 3),
    _DigitalIpMultisiteConnect_Type()
)
digitalIpMultisiteConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalIpMultisiteConnect.setStatus("mandatory")


class _DigitalReceiveFrequency_Type(Integer32):
    """Custom type digitalReceiveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_DigitalReceiveFrequency_Type.__name__ = "Integer32"
_DigitalReceiveFrequency_Object = MibTableColumn
digitalReceiveFrequency = _DigitalReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 4),
    _DigitalReceiveFrequency_Type()
)
digitalReceiveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalReceiveFrequency.setStatus("mandatory")


class _DigitalTransmitFrequency_Type(Integer32):
    """Custom type digitalTransmitFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_DigitalTransmitFrequency_Type.__name__ = "Integer32"
_DigitalTransmitFrequency_Object = MibTableColumn
digitalTransmitFrequency = _DigitalTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 5),
    _DigitalTransmitFrequency_Type()
)
digitalTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalTransmitFrequency.setStatus("mandatory")


class _DigitalTxContactName_Type(Integer32):
    """Custom type digitalTxContactName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_DigitalTxContactName_Type.__name__ = "Integer32"
_DigitalTxContactName_Object = MibTableColumn
digitalTxContactName = _DigitalTxContactName_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 2, 1, 1, 6),
    _DigitalTxContactName_Type()
)
digitalTxContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalTxContactName.setStatus("mandatory")
_RptAnalogChannelSetting_ObjectIdentity = ObjectIdentity
rptAnalogChannelSetting = _RptAnalogChannelSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3)
)
_AnalogChnTable_Object = MibTable
analogChnTable = _AnalogChnTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    analogChnTable.setStatus("mandatory")
_AnalogChnEntry_Object = MibTableRow
analogChnEntry = _AnalogChnEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1)
)
analogChnEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "analogChnIndex"),
)
if mibBuilder.loadTexts:
    analogChnEntry.setStatus("mandatory")


class _AnalogChnIndex_Type(Integer32):
    """Custom type analogChnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AnalogChnIndex_Type.__name__ = "Integer32"
_AnalogChnIndex_Object = MibTableColumn
analogChnIndex = _AnalogChnIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 1),
    _AnalogChnIndex_Type()
)
analogChnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogChnIndex.setStatus("mandatory")


class _AnalogCarrierSquelchLevel_Type(Integer32):
    """Custom type analogCarrierSquelchLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AnalogCarrierSquelchLevel_Type.__name__ = "Integer32"
_AnalogCarrierSquelchLevel_Object = MibTableColumn
analogCarrierSquelchLevel = _AnalogCarrierSquelchLevel_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 2),
    _AnalogCarrierSquelchLevel_Type()
)
analogCarrierSquelchLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogCarrierSquelchLevel.setStatus("mandatory")


class _AnalogMultiCtcCdc_Type(Integer32):
    """Custom type analogMultiCtcCdc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogMultiCtcCdc_Type.__name__ = "Integer32"
_AnalogMultiCtcCdc_Object = MibTableColumn
analogMultiCtcCdc = _AnalogMultiCtcCdc_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 3),
    _AnalogMultiCtcCdc_Type()
)
analogMultiCtcCdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogMultiCtcCdc.setStatus("mandatory")


class _AnalogPreEmp_Type(Integer32):
    """Custom type analogPreEmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogPreEmp_Type.__name__ = "Integer32"
_AnalogPreEmp_Object = MibTableColumn
analogPreEmp = _AnalogPreEmp_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 4),
    _AnalogPreEmp_Type()
)
analogPreEmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogPreEmp.setStatus("mandatory")


class _AnalogScrambler_Type(Integer32):
    """Custom type analogScrambler based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogScrambler_Type.__name__ = "Integer32"
_AnalogScrambler_Object = MibTableColumn
analogScrambler = _AnalogScrambler_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 5),
    _AnalogScrambler_Type()
)
analogScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogScrambler.setStatus("mandatory")


class _AnalogFlatAudio_Type(Integer32):
    """Custom type analogFlatAudio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AnalogFlatAudio_Type.__name__ = "Integer32"
_AnalogFlatAudio_Object = MibTableColumn
analogFlatAudio = _AnalogFlatAudio_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 6),
    _AnalogFlatAudio_Type()
)
analogFlatAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogFlatAudio.setStatus("mandatory")


class _AnalogReceiveFrequency_Type(Integer32):
    """Custom type analogReceiveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_AnalogReceiveFrequency_Type.__name__ = "Integer32"
_AnalogReceiveFrequency_Object = MibTableColumn
analogReceiveFrequency = _AnalogReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 7),
    _AnalogReceiveFrequency_Type()
)
analogReceiveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogReceiveFrequency.setStatus("mandatory")


class _AnalogRxCtcCdcType_Type(Integer32):
    """Custom type analogRxCtcCdcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AnalogRxCtcCdcType_Type.__name__ = "Integer32"
_AnalogRxCtcCdcType_Object = MibTableColumn
analogRxCtcCdcType = _AnalogRxCtcCdcType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 8),
    _AnalogRxCtcCdcType_Type()
)
analogRxCtcCdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogRxCtcCdcType.setStatus("mandatory")


class _AnalogRxCtcss_Type(Integer32):
    """Custom type analogRxCtcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(670, 2541),
        ValueRangeConstraint(65535, 65535),
    )


_AnalogRxCtcss_Type.__name__ = "Integer32"
_AnalogRxCtcss_Object = MibTableColumn
analogRxCtcss = _AnalogRxCtcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 9),
    _AnalogRxCtcss_Type()
)
analogRxCtcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogRxCtcss.setStatus("mandatory")


class _AnalogRxCdcss_Type(Integer32):
    """Custom type analogRxCdcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(65535, 65535),
    )


_AnalogRxCdcss_Type.__name__ = "Integer32"
_AnalogRxCdcss_Object = MibTableColumn
analogRxCdcss = _AnalogRxCdcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 10),
    _AnalogRxCdcss_Type()
)
analogRxCdcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogRxCdcss.setStatus("mandatory")


class _AnalogTransmitFrequency_Type(Integer32):
    """Custom type analogTransmitFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_AnalogTransmitFrequency_Type.__name__ = "Integer32"
_AnalogTransmitFrequency_Object = MibTableColumn
analogTransmitFrequency = _AnalogTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 11),
    _AnalogTransmitFrequency_Type()
)
analogTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogTransmitFrequency.setStatus("mandatory")


class _AnalogTxCtcCdcType_Type(Integer32):
    """Custom type analogTxCtcCdcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AnalogTxCtcCdcType_Type.__name__ = "Integer32"
_AnalogTxCtcCdcType_Object = MibTableColumn
analogTxCtcCdcType = _AnalogTxCtcCdcType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 12),
    _AnalogTxCtcCdcType_Type()
)
analogTxCtcCdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogTxCtcCdcType.setStatus("mandatory")


class _AnalogTxCtcss_Type(Integer32):
    """Custom type analogTxCtcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(670, 2541),
        ValueRangeConstraint(65535, 65535),
    )


_AnalogTxCtcss_Type.__name__ = "Integer32"
_AnalogTxCtcss_Object = MibTableColumn
analogTxCtcss = _AnalogTxCtcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 13),
    _AnalogTxCtcss_Type()
)
analogTxCtcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogTxCtcss.setStatus("mandatory")


class _AnalogTxCdcss_Type(Integer32):
    """Custom type analogTxCdcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(65535, 65535),
    )


_AnalogTxCdcss_Type.__name__ = "Integer32"
_AnalogTxCdcss_Object = MibTableColumn
analogTxCdcss = _AnalogTxCdcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 3, 1, 1, 14),
    _AnalogTxCdcss_Type()
)
analogTxCdcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogTxCdcss.setStatus("mandatory")
_RptMixedChannelSetting_ObjectIdentity = ObjectIdentity
rptMixedChannelSetting = _RptMixedChannelSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4)
)
_MixedChnTable_Object = MibTable
mixedChnTable = _MixedChnTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mixedChnTable.setStatus("mandatory")
_MixedChnEntry_Object = MibTableRow
mixedChnEntry = _MixedChnEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1)
)
mixedChnEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "analogChnIndex"),
)
if mibBuilder.loadTexts:
    mixedChnEntry.setStatus("mandatory")


class _MixedChnIndex_Type(Integer32):
    """Custom type mixedChnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MixedChnIndex_Type.__name__ = "Integer32"
_MixedChnIndex_Object = MibTableColumn
mixedChnIndex = _MixedChnIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 1),
    _MixedChnIndex_Type()
)
mixedChnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mixedChnIndex.setStatus("mandatory")


class _MixedCarrierSquelchLevel_Type(Integer32):
    """Custom type mixedCarrierSquelchLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MixedCarrierSquelchLevel_Type.__name__ = "Integer32"
_MixedCarrierSquelchLevel_Object = MibTableColumn
mixedCarrierSquelchLevel = _MixedCarrierSquelchLevel_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 2),
    _MixedCarrierSquelchLevel_Type()
)
mixedCarrierSquelchLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedCarrierSquelchLevel.setStatus("mandatory")


class _MixedTxContactName_Type(Integer32):
    """Custom type mixedTxContactName based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_MixedTxContactName_Type.__name__ = "Integer32"
_MixedTxContactName_Object = MibTableColumn
mixedTxContactName = _MixedTxContactName_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 3),
    _MixedTxContactName_Type()
)
mixedTxContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTxContactName.setStatus("mandatory")


class _MixedIpMultisiteConnect_Type(Integer32):
    """Custom type mixedIpMultisiteConnect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MixedIpMultisiteConnect_Type.__name__ = "Integer32"
_MixedIpMultisiteConnect_Object = MibTableColumn
mixedIpMultisiteConnect = _MixedIpMultisiteConnect_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 4),
    _MixedIpMultisiteConnect_Type()
)
mixedIpMultisiteConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedIpMultisiteConnect.setStatus("mandatory")


class _MixedColorCode_Type(Integer32):
    """Custom type mixedColorCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MixedColorCode_Type.__name__ = "Integer32"
_MixedColorCode_Object = MibTableColumn
mixedColorCode = _MixedColorCode_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 5),
    _MixedColorCode_Type()
)
mixedColorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedColorCode.setStatus("mandatory")


class _MixedTxChannelType_Type(Integer32):
    """Custom type mixedTxChannelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MixedTxChannelType_Type.__name__ = "Integer32"
_MixedTxChannelType_Object = MibTableColumn
mixedTxChannelType = _MixedTxChannelType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 6),
    _MixedTxChannelType_Type()
)
mixedTxChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTxChannelType.setStatus("mandatory")


class _MixedPreEmp_Type(Integer32):
    """Custom type mixedPreEmp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MixedPreEmp_Type.__name__ = "Integer32"
_MixedPreEmp_Object = MibTableColumn
mixedPreEmp = _MixedPreEmp_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 7),
    _MixedPreEmp_Type()
)
mixedPreEmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedPreEmp.setStatus("mandatory")


class _MixedScrambler_Type(Integer32):
    """Custom type mixedScrambler based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MixedScrambler_Type.__name__ = "Integer32"
_MixedScrambler_Object = MibTableColumn
mixedScrambler = _MixedScrambler_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 8),
    _MixedScrambler_Type()
)
mixedScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedScrambler.setStatus("mandatory")


class _MixedFlatAudio_Type(Integer32):
    """Custom type mixedFlatAudio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MixedFlatAudio_Type.__name__ = "Integer32"
_MixedFlatAudio_Object = MibTableColumn
mixedFlatAudio = _MixedFlatAudio_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 9),
    _MixedFlatAudio_Type()
)
mixedFlatAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedFlatAudio.setStatus("mandatory")


class _MixedMultiCtcCdc_Type(Integer32):
    """Custom type mixedMultiCtcCdc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MixedMultiCtcCdc_Type.__name__ = "Integer32"
_MixedMultiCtcCdc_Object = MibTableColumn
mixedMultiCtcCdc = _MixedMultiCtcCdc_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 10),
    _MixedMultiCtcCdc_Type()
)
mixedMultiCtcCdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedMultiCtcCdc.setStatus("mandatory")


class _MixedReceiveFrequency_Type(Integer32):
    """Custom type mixedReceiveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_MixedReceiveFrequency_Type.__name__ = "Integer32"
_MixedReceiveFrequency_Object = MibTableColumn
mixedReceiveFrequency = _MixedReceiveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 11),
    _MixedReceiveFrequency_Type()
)
mixedReceiveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedReceiveFrequency.setStatus("mandatory")


class _MixedRxCtcCdcType_Type(Integer32):
    """Custom type mixedRxCtcCdcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MixedRxCtcCdcType_Type.__name__ = "Integer32"
_MixedRxCtcCdcType_Object = MibTableColumn
mixedRxCtcCdcType = _MixedRxCtcCdcType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 12),
    _MixedRxCtcCdcType_Type()
)
mixedRxCtcCdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedRxCtcCdcType.setStatus("mandatory")


class _MixedRxCtcss_Type(Integer32):
    """Custom type mixedRxCtcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(670, 2541),
        ValueRangeConstraint(65535, 65535),
    )


_MixedRxCtcss_Type.__name__ = "Integer32"
_MixedRxCtcss_Object = MibTableColumn
mixedRxCtcss = _MixedRxCtcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 13),
    _MixedRxCtcss_Type()
)
mixedRxCtcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedRxCtcss.setStatus("mandatory")


class _MixedRxCdcss_Type(Integer32):
    """Custom type mixedRxCdcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(65535, 65535),
    )


_MixedRxCdcss_Type.__name__ = "Integer32"
_MixedRxCdcss_Object = MibTableColumn
mixedRxCdcss = _MixedRxCdcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 14),
    _MixedRxCdcss_Type()
)
mixedRxCdcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedRxCdcss.setStatus("mandatory")


class _MixedTransmitFrequency_Type(Integer32):
    """Custom type mixedTransmitFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000000, 550000000),
    )


_MixedTransmitFrequency_Type.__name__ = "Integer32"
_MixedTransmitFrequency_Object = MibTableColumn
mixedTransmitFrequency = _MixedTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 15),
    _MixedTransmitFrequency_Type()
)
mixedTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTransmitFrequency.setStatus("mandatory")


class _MixedTxCtcCdcType_Type(Integer32):
    """Custom type mixedTxCtcCdcType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MixedTxCtcCdcType_Type.__name__ = "Integer32"
_MixedTxCtcCdcType_Object = MibTableColumn
mixedTxCtcCdcType = _MixedTxCtcCdcType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 16),
    _MixedTxCtcCdcType_Type()
)
mixedTxCtcCdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTxCtcCdcType.setStatus("mandatory")


class _MixedTxCtcss_Type(Integer32):
    """Custom type mixedTxCtcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(670, 2541),
        ValueRangeConstraint(65535, 65535),
    )


_MixedTxCtcss_Type.__name__ = "Integer32"
_MixedTxCtcss_Object = MibTableColumn
mixedTxCtcss = _MixedTxCtcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 17),
    _MixedTxCtcss_Type()
)
mixedTxCtcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTxCtcss.setStatus("mandatory")


class _MixedTxCdcss_Type(Integer32):
    """Custom type mixedTxCdcss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 492),
        ValueRangeConstraint(65535, 65535),
    )


_MixedTxCdcss_Type.__name__ = "Integer32"
_MixedTxCdcss_Object = MibTableColumn
mixedTxCdcss = _MixedTxCdcss_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 4, 1, 1, 18),
    _MixedTxCdcss_Type()
)
mixedTxCdcss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mixedTxCdcss.setStatus("mandatory")
_RptServiceSetting_ObjectIdentity = ObjectIdentity
rptServiceSetting = _RptServiceSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5)
)


class _GroupCallHangTime_Type(Integer32):
    """Custom type groupCallHangTime based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_GroupCallHangTime_Type.__name__ = "Integer32"
_GroupCallHangTime_Object = MibScalar
groupCallHangTime = _GroupCallHangTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 1),
    _GroupCallHangTime_Type()
)
groupCallHangTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCallHangTime.setStatus("mandatory")


class _PrivateCallHangTime_Type(Integer32):
    """Custom type privateCallHangTime based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PrivateCallHangTime_Type.__name__ = "Integer32"
_PrivateCallHangTime_Object = MibScalar
privateCallHangTime = _PrivateCallHangTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 2),
    _PrivateCallHangTime_Type()
)
privateCallHangTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateCallHangTime.setStatus("mandatory")


class _EmergencyCallHangTime_Type(Integer32):
    """Custom type emergencyCallHangTime based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_EmergencyCallHangTime_Type.__name__ = "Integer32"
_EmergencyCallHangTime_Object = MibScalar
emergencyCallHangTime = _EmergencyCallHangTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 3),
    _EmergencyCallHangTime_Type()
)
emergencyCallHangTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emergencyCallHangTime.setStatus("mandatory")


class _Sit_Type(Integer32):
    """Custom type sit based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 120),
    )


_Sit_Type.__name__ = "Integer32"
_Sit_Object = MibScalar
sit = _Sit_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 4),
    _Sit_Type()
)
sit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sit.setStatus("mandatory")


class _TxPreambleDuration_Type(Integer32):
    """Custom type txPreambleDuration based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 144),
    )


_TxPreambleDuration_Type.__name__ = "Integer32"
_TxPreambleDuration_Object = MibScalar
txPreambleDuration = _TxPreambleDuration_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 5),
    _TxPreambleDuration_Type()
)
txPreambleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txPreambleDuration.setStatus("mandatory")


class _BeaconTxMode_Type(Integer32):
    """Custom type beaconTxMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BeaconTxMode_Type.__name__ = "Integer32"
_BeaconTxMode_Object = MibScalar
beaconTxMode = _BeaconTxMode_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 6),
    _BeaconTxMode_Type()
)
beaconTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconTxMode.setStatus("mandatory")


class _BeaconDuration_Type(Integer32):
    """Custom type beaconDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 150),
    )


_BeaconDuration_Type.__name__ = "Integer32"
_BeaconDuration_Object = MibScalar
beaconDuration = _BeaconDuration_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 7),
    _BeaconDuration_Type()
)
beaconDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconDuration.setStatus("mandatory")


class _BeaconInterval_Type(Integer32):
    """Custom type beaconInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_BeaconInterval_Type.__name__ = "Integer32"
_BeaconInterval_Object = MibScalar
beaconInterval = _BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 8),
    _BeaconInterval_Type()
)
beaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    beaconInterval.setStatus("mandatory")


class _MultisiteAccessManagement_Type(Integer32):
    """Custom type multisiteAccessManagement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MultisiteAccessManagement_Type.__name__ = "Integer32"
_MultisiteAccessManagement_Object = MibScalar
multisiteAccessManagement = _MultisiteAccessManagement_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 9),
    _MultisiteAccessManagement_Type()
)
multisiteAccessManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multisiteAccessManagement.setStatus("mandatory")


class _AccessManagement_Type(Integer32):
    """Custom type accessManagement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccessManagement_Type.__name__ = "Integer32"
_AccessManagement_Object = MibScalar
accessManagement = _AccessManagement_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 10),
    _AccessManagement_Type()
)
accessManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessManagement.setStatus("mandatory")
_MultisiteAccessManageTable_Object = MibTable
multisiteAccessManageTable = _MultisiteAccessManageTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11)
)
if mibBuilder.loadTexts:
    multisiteAccessManageTable.setStatus("mandatory")
_MultisiteAccessManageEntry_Object = MibTableRow
multisiteAccessManageEntry = _MultisiteAccessManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11, 1)
)
multisiteAccessManageEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "mutisiteAccessManageIndex"),
)
if mibBuilder.loadTexts:
    multisiteAccessManageEntry.setStatus("mandatory")


class _MultisiteAccessManageIndex_Type(Integer32):
    """Custom type multisiteAccessManageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MultisiteAccessManageIndex_Type.__name__ = "Integer32"
_MultisiteAccessManageIndex_Object = MibTableColumn
multisiteAccessManageIndex = _MultisiteAccessManageIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11, 1, 1),
    _MultisiteAccessManageIndex_Type()
)
multisiteAccessManageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multisiteAccessManageIndex.setStatus("mandatory")


class _MultisiteStartId_Type(Integer32):
    """Custom type multisiteStartId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16776415),
    )


_MultisiteStartId_Type.__name__ = "Integer32"
_MultisiteStartId_Object = MibTableColumn
multisiteStartId = _MultisiteStartId_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11, 1, 2),
    _MultisiteStartId_Type()
)
multisiteStartId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multisiteStartId.setStatus("mandatory")


class _MultisiteIdLength_Type(Integer32):
    """Custom type multisiteIdLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(65535, 65535),
    )


_MultisiteIdLength_Type.__name__ = "Integer32"
_MultisiteIdLength_Object = MibTableColumn
multisiteIdLength = _MultisiteIdLength_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11, 1, 3),
    _MultisiteIdLength_Type()
)
multisiteIdLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multisiteIdLength.setStatus("mandatory")


class _MultisiteAccessCallType_Type(Integer32):
    """Custom type multisiteAccessCallType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(65535, 65535),
    )


_MultisiteAccessCallType_Type.__name__ = "Integer32"
_MultisiteAccessCallType_Object = MibTableColumn
multisiteAccessCallType = _MultisiteAccessCallType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 11, 1, 4),
    _MultisiteAccessCallType_Type()
)
multisiteAccessCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multisiteAccessCallType.setStatus("mandatory")
_ContactTable_Object = MibTable
contactTable = _ContactTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12)
)
if mibBuilder.loadTexts:
    contactTable.setStatus("mandatory")
_ContactEntry_Object = MibTableRow
contactEntry = _ContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12, 1)
)
contactEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "contactIndex"),
)
if mibBuilder.loadTexts:
    contactEntry.setStatus("mandatory")


class _ContactIndex_Type(Integer32):
    """Custom type contactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_ContactIndex_Type.__name__ = "Integer32"
_ContactIndex_Object = MibTableColumn
contactIndex = _ContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12, 1, 1),
    _ContactIndex_Type()
)
contactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactIndex.setStatus("mandatory")


class _CallAlias_Type(OctetString):
    """Custom type callAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CallAlias_Type.__name__ = "OctetString"
_CallAlias_Object = MibTableColumn
callAlias = _CallAlias_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12, 1, 2),
    _CallAlias_Type()
)
callAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAlias.setStatus("mandatory")


class _ContactCallType_Type(Integer32):
    """Custom type contactCallType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(65535, 65535),
    )


_ContactCallType_Type.__name__ = "Integer32"
_ContactCallType_Object = MibTableColumn
contactCallType = _ContactCallType_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12, 1, 3),
    _ContactCallType_Type()
)
contactCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactCallType.setStatus("mandatory")


class _CallId_Type(Integer32):
    """Custom type callId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16776415),
        ValueRangeConstraint(16777215, 16777215),
    )


_CallId_Type.__name__ = "Integer32"
_CallId_Object = MibTableColumn
callId = _CallId_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 12, 1, 4),
    _CallId_Type()
)
callId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callId.setStatus("mandatory")
_AccessManageTable_Object = MibTable
accessManageTable = _AccessManageTable_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 13)
)
if mibBuilder.loadTexts:
    accessManageTable.setStatus("mandatory")
_AccessManageEntry_Object = MibTableRow
accessManageEntry = _AccessManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 13, 1)
)
accessManageEntry.setIndexNames(
    (0, "HYTERA-REPEATER-MIB", "accessManageIndex"),
)
if mibBuilder.loadTexts:
    accessManageEntry.setStatus("mandatory")


class _AccessManageIndex_Type(Integer32):
    """Custom type accessManageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccessManageIndex_Type.__name__ = "Integer32"
_AccessManageIndex_Object = MibTableColumn
accessManageIndex = _AccessManageIndex_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 13, 1, 1),
    _AccessManageIndex_Type()
)
accessManageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessManageIndex.setStatus("mandatory")


class _StartId_Type(Integer32):
    """Custom type startId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16776415),
    )


_StartId_Type.__name__ = "Integer32"
_StartId_Object = MibTableColumn
startId = _StartId_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 13, 1, 2),
    _StartId_Type()
)
startId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startId.setStatus("mandatory")


class _IdLength_Type(Integer32):
    """Custom type idLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
        ValueRangeConstraint(65535, 65535),
    )


_IdLength_Type.__name__ = "Integer32"
_IdLength_Object = MibTableColumn
idLength = _IdLength_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 13, 1, 3),
    _IdLength_Type()
)
idLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idLength.setStatus("mandatory")


class _RepeatTOTTime_Type(Integer32):
    """Custom type repeatTOTTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 120),
    )


_RepeatTOTTime_Type.__name__ = "Integer32"
_RepeatTOTTime_Object = MibScalar
repeatTOTTime = _RepeatTOTTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 14),
    _RepeatTOTTime_Type()
)
repeatTOTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeatTOTTime.setStatus("mandatory")


class _RerepeatTOTTime_Type(Integer32):
    """Custom type rerepeatTOTTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RerepeatTOTTime_Type.__name__ = "Integer32"
_RerepeatTOTTime_Object = MibScalar
rerepeatTOTTime = _RerepeatTOTTime_Object(
    (1, 3, 6, 1, 4, 1, 40297, 1, 2, 5, 5, 15),
    _RerepeatTOTTime_Type()
)
rerepeatTOTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rerepeatTOTTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HYTERA-REPEATER-MIB",
    **{"hyteraRepeaterMIB": hyteraRepeaterMIB,
       "product": product,
       "repeater": repeater,
       "rptRealTimeInfo": rptRealTimeInfo,
       "rptAlarmInfo": rptAlarmInfo,
       "rptVoltageAlarm": rptVoltageAlarm,
       "rptTemperatureAlarm": rptTemperatureAlarm,
       "rptFanAlarm": rptFanAlarm,
       "rptForwardAlarm": rptForwardAlarm,
       "rptReflectedAlarm": rptReflectedAlarm,
       "rptVswrAlarm": rptVswrAlarm,
       "rptTxPllAlarm": rptTxPllAlarm,
       "rptRxPllAlarm": rptRxPllAlarm,
       "rptBatteryVoltageAlarm": rptBatteryVoltageAlarm,
       "rptDataInfo": rptDataInfo,
       "rptVoltage": rptVoltage,
       "rptPaTemprature": rptPaTemprature,
       "rptFanSpeed": rptFanSpeed,
       "rptVswr": rptVswr,
       "rptTxFwdPower": rptTxFwdPower,
       "rptTxRefPower": rptTxRefPower,
       "rptDataInfoBak1": rptDataInfoBak1,
       "rptDataInfoBak2": rptDataInfoBak2,
       "rptSlot1Rssi": rptSlot1Rssi,
       "rptSlot2Rssi": rptSlot2Rssi,
       "rptSupplyPowerType": rptSupplyPowerType,
       "rptBatteryConnect": rptBatteryConnect,
       "rptBatteryVoltage": rptBatteryVoltage,
       "rptControl": rptControl,
       "rptRestart": rptRestart,
       "rptChannelNumber": rptChannelNumber,
       "rptChannelType": rptChannelType,
       "rptControlObjBak1": rptControlObjBak1,
       "rptTxPowerLevel": rptTxPowerLevel,
       "rptKnockdown": rptKnockdown,
       "rptRadioState": rptRadioState,
       "rptSnmpTrapIp": rptSnmpTrapIp,
       "rptSnmpTrapPort": rptSnmpTrapPort,
       "rptchannelParaTable": rptchannelParaTable,
       "channelParaEntry": channelParaEntry,
       "channelParaIndex": channelParaIndex,
       "actChannelAlias": actChannelAlias,
       "actChannelType": actChannelType,
       "actTxPower": actTxPower,
       "actChannelNo": actChannelNo,
       "actChannelSubNo": actChannelSubNo,
       "rptForbid": rptForbid,
       "rptLog": rptLog,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "alarmName": alarmName,
       "alarmStatus": alarmStatus,
       "logTime": logTime,
       "clearLog": clearLog,
       "recordCount": recordCount,
       "latestRecordPosition": latestRecordPosition,
       "rptSystemInfo": rptSystemInfo,
       "rptModelName": rptModelName,
       "rptModelNo": rptModelNo,
       "rptFirmwareVersion": rptFirmwareVersion,
       "rptRcdbVersion": rptRcdbVersion,
       "rptSerialNo": rptSerialNo,
       "rptRadioAlias": rptRadioAlias,
       "rptRadioID": rptRadioID,
       "rptCurChannelType": rptCurChannelType,
       "rptChannelName": rptChannelName,
       "rptCurTxFreq": rptCurTxFreq,
       "rptCurRxFreq": rptCurRxFreq,
       "rptWorkState": rptWorkState,
       "rptCurZoneAlias": rptCurZoneAlias,
       "rptConfiguration": rptConfiguration,
       "rptBasicSetting": rptBasicSetting,
       "powerOn": powerOn,
       "designatedPowerOnChn": designatedPowerOnChn,
       "powerOnChannelNo": powerOnChannelNo,
       "microphone": microphone,
       "internalMicGain": internalMicGain,
       "externalMicGain": externalMicGain,
       "multiCTCCDCTable": multiCTCCDCTable,
       "multiCTCCDCEntry": multiCTCCDCEntry,
       "ctcssIndex": ctcssIndex,
       "txCtcssFrequency": txCtcssFrequency,
       "txCtcssType": txCtcssType,
       "rxCtcssFrequency": rxCtcssFrequency,
       "rxCtcssType": rxCtcssType,
       "audioPriority": audioPriority,
       "pathPriority": pathPriority,
       "pttPriority": pttPriority,
       "jitterBufferLenth": jitterBufferLenth,
       "analogCallHangTime": analogCallHangTime,
       "repeatRequestPriority": repeatRequestPriority,
       "rptDigitalChannelSetting": rptDigitalChannelSetting,
       "digitalChnTable": digitalChnTable,
       "digitalChnEntry": digitalChnEntry,
       "digitalChnIndex": digitalChnIndex,
       "digitalColorCode": digitalColorCode,
       "digitalIpMultisiteConnect": digitalIpMultisiteConnect,
       "digitalReceiveFrequency": digitalReceiveFrequency,
       "digitalTransmitFrequency": digitalTransmitFrequency,
       "digitalTxContactName": digitalTxContactName,
       "rptAnalogChannelSetting": rptAnalogChannelSetting,
       "analogChnTable": analogChnTable,
       "analogChnEntry": analogChnEntry,
       "analogChnIndex": analogChnIndex,
       "analogCarrierSquelchLevel": analogCarrierSquelchLevel,
       "analogMultiCtcCdc": analogMultiCtcCdc,
       "analogPreEmp": analogPreEmp,
       "analogScrambler": analogScrambler,
       "analogFlatAudio": analogFlatAudio,
       "analogReceiveFrequency": analogReceiveFrequency,
       "analogRxCtcCdcType": analogRxCtcCdcType,
       "analogRxCtcss": analogRxCtcss,
       "analogRxCdcss": analogRxCdcss,
       "analogTransmitFrequency": analogTransmitFrequency,
       "analogTxCtcCdcType": analogTxCtcCdcType,
       "analogTxCtcss": analogTxCtcss,
       "analogTxCdcss": analogTxCdcss,
       "rptMixedChannelSetting": rptMixedChannelSetting,
       "mixedChnTable": mixedChnTable,
       "mixedChnEntry": mixedChnEntry,
       "mixedChnIndex": mixedChnIndex,
       "mixedCarrierSquelchLevel": mixedCarrierSquelchLevel,
       "mixedTxContactName": mixedTxContactName,
       "mixedIpMultisiteConnect": mixedIpMultisiteConnect,
       "mixedColorCode": mixedColorCode,
       "mixedTxChannelType": mixedTxChannelType,
       "mixedPreEmp": mixedPreEmp,
       "mixedScrambler": mixedScrambler,
       "mixedFlatAudio": mixedFlatAudio,
       "mixedMultiCtcCdc": mixedMultiCtcCdc,
       "mixedReceiveFrequency": mixedReceiveFrequency,
       "mixedRxCtcCdcType": mixedRxCtcCdcType,
       "mixedRxCtcss": mixedRxCtcss,
       "mixedRxCdcss": mixedRxCdcss,
       "mixedTransmitFrequency": mixedTransmitFrequency,
       "mixedTxCtcCdcType": mixedTxCtcCdcType,
       "mixedTxCtcss": mixedTxCtcss,
       "mixedTxCdcss": mixedTxCdcss,
       "rptServiceSetting": rptServiceSetting,
       "groupCallHangTime": groupCallHangTime,
       "privateCallHangTime": privateCallHangTime,
       "emergencyCallHangTime": emergencyCallHangTime,
       "sit": sit,
       "txPreambleDuration": txPreambleDuration,
       "beaconTxMode": beaconTxMode,
       "beaconDuration": beaconDuration,
       "beaconInterval": beaconInterval,
       "multisiteAccessManagement": multisiteAccessManagement,
       "accessManagement": accessManagement,
       "multisiteAccessManageTable": multisiteAccessManageTable,
       "multisiteAccessManageEntry": multisiteAccessManageEntry,
       "multisiteAccessManageIndex": multisiteAccessManageIndex,
       "multisiteStartId": multisiteStartId,
       "multisiteIdLength": multisiteIdLength,
       "multisiteAccessCallType": multisiteAccessCallType,
       "contactTable": contactTable,
       "contactEntry": contactEntry,
       "contactIndex": contactIndex,
       "callAlias": callAlias,
       "contactCallType": contactCallType,
       "callId": callId,
       "accessManageTable": accessManageTable,
       "accessManageEntry": accessManageEntry,
       "accessManageIndex": accessManageIndex,
       "startId": startId,
       "idLength": idLength,
       "repeatTOTTime": repeatTOTTime,
       "rerepeatTOTTime": rerepeatTOTTime}
)
