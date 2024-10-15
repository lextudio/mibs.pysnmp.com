# SNMP MIB module (OGTRAPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OGTRAPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:55 2024
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

_Opengear_ObjectIdentity = ObjectIdentity
opengear = _Opengear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049)
)
_OgLegacyMgmt_ObjectIdentity = ObjectIdentity
ogLegacyMgmt = _OgLegacyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2)
)
_OgNotification_ObjectIdentity = ObjectIdentity
ogNotification = _OgNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 0)
)
_OgAlarmMib_ObjectIdentity = ObjectIdentity
ogAlarmMib = _OgAlarmMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101)
)
_OgAlarmMibObjects_ObjectIdentity = ObjectIdentity
ogAlarmMibObjects = _OgAlarmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1)
)
_OgAlarm_ObjectIdentity = ObjectIdentity
ogAlarm = _OgAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1)
)
_OgAlarmTable_ObjectIdentity = ObjectIdentity
ogAlarmTable = _OgAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1)
)
_OgAlarmEntry_ObjectIdentity = ObjectIdentity
ogAlarmEntry = _OgAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1)
)
_OgAlarmIndex_Type = Integer32
_OgAlarmIndex_Object = MibScalar
ogAlarmIndex = _OgAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 1),
    _OgAlarmIndex_Type()
)
ogAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmIndex.setStatus("mandatory")
_OgAlarmEventId_Type = Integer32
_OgAlarmEventId_Object = MibScalar
ogAlarmEventId = _OgAlarmEventId_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 2),
    _OgAlarmEventId_Type()
)
ogAlarmEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmEventId.setStatus("mandatory")
_OgAlarmName_Type = OctetString
_OgAlarmName_Object = MibScalar
ogAlarmName = _OgAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 3),
    _OgAlarmName_Type()
)
ogAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmName.setStatus("mandatory")


class _OgAlarmCheck_Type(Integer32):
    """Custom type ogAlarmCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OgAlarmCheck_Type.__name__ = "Integer32"
_OgAlarmCheck_Object = MibScalar
ogAlarmCheck = _OgAlarmCheck_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 4),
    _OgAlarmCheck_Type()
)
ogAlarmCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmCheck.setStatus("mandatory")


class _OgAlarmInstance_Type(Integer32):
    """Custom type ogAlarmInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OgAlarmInstance_Type.__name__ = "Integer32"
_OgAlarmInstance_Object = MibScalar
ogAlarmInstance = _OgAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 5),
    _OgAlarmInstance_Type()
)
ogAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmInstance.setStatus("mandatory")


class _OgAlarmTime_Type(OctetString):
    """Custom type ogAlarmTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )


_OgAlarmTime_Type.__name__ = "OctetString"
_OgAlarmTime_Object = MibScalar
ogAlarmTime = _OgAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 6),
    _OgAlarmTime_Type()
)
ogAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmTime.setStatus("mandatory")


class _OgAlarmType_Type(Integer32):
    """Custom type ogAlarmType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              255,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("cellApnChanged", 79),
          ("cellDataUsage", 75),
          ("cellMessageReceived", 76),
          ("cellNetworkChanged", 81),
          ("cellSignalHigh", 78),
          ("cellSignalLow", 77),
          ("cellTowerChanged", 80),
          ("customCheckFailure", 255),
          ("dialPoolHealth", 89),
          ("dioSignalClosed", 18),
          ("dioSignalOpened", 17),
          ("envHumidityHigh", 16),
          ("envHumidityLow", 15),
          ("envTemperatureHigh", 14),
          ("envTemperatureLow", 13),
          ("hostPingDown", 7),
          ("hostPingUp", 8),
          ("hostServiceDown", 9),
          ("hostServiceUp", 10),
          ("hostUserSession", 11),
          ("netInterfaceDown", 19),
          ("netInterfaceStarting", 20),
          ("netInterfaceStopping", 22),
          ("netInterfaceUp", 21),
          ("powerSupplyInputVoltageHigh", 24),
          ("powerSupplyInputVoltageLow", 23),
          ("powerSupplyOutputCurrentHigh", 26),
          ("powerSupplyOutputCurrentLow", 25),
          ("powerSupplyTemperatureHigh", 28),
          ("powerSupplyTemperatureLow", 27),
          ("rpcInputCurrentHigh", 66),
          ("rpcInputCurrentLow", 65),
          ("rpcInputFrequencyHigh", 62),
          ("rpcInputFrequencyLow", 61),
          ("rpcInputVoltageHigh", 64),
          ("rpcInputVoltageLow", 63),
          ("rpcOutletCurrentHigh", 71),
          ("rpcOutletCurrentLow", 72),
          ("rpcOutletFrequencyHigh", 67),
          ("rpcOutletFrequencyLow", 68),
          ("rpcOutletStateOff", 73),
          ("rpcOutletStateOn", 74),
          ("rpcOutletVoltageHigh", 69),
          ("rpcOutletVoltageLow", 70),
          ("serialPatternRx", 5),
          ("serialPatternTx", 4),
          ("serialSignalCts", 1),
          ("serialSignalDcd", 2),
          ("serialSignalDsr", 3),
          ("serialUserSession", 6),
          ("unknown", 65535),
          ("upsBatteryChargeHigh", 36),
          ("upsBatteryChargeLow", 35),
          ("upsBatteryCurrentHigh", 40),
          ("upsBatteryCurrentLow", 39),
          ("upsBatteryTemperatureHigh", 42),
          ("upsBatteryTemperatureLow", 41),
          ("upsBatteryVoltageHigh", 38),
          ("upsBatteryVoltageLow", 37),
          ("upsHumidityHigh", 31),
          ("upsHumidityLow", 32),
          ("upsInputCurrentHigh", 48),
          ("upsInputCurrentLow", 47),
          ("upsInputFrequencyHigh", 44),
          ("upsInputFrequencyLow", 43),
          ("upsInputVoltageHigh", 46),
          ("upsInputVoltageLow", 45),
          ("upsLowBattery", 34),
          ("upsOnBattery", 33),
          ("upsOutputCurrentHigh", 54),
          ("upsOutputCurrentLow", 53),
          ("upsOutputFrequencyHigh", 50),
          ("upsOutputFrequencyLow", 49),
          ("upsOutputLoadHigh", 56),
          ("upsOutputLoadLow", 55),
          ("upsOutputPowerHigh", 58),
          ("upsOutputPowerLow", 57),
          ("upsOutputTruePowerHigh", 60),
          ("upsOutputTruePowerLow", 59),
          ("upsOutputVoltageHigh", 52),
          ("upsOutputVoltageLow", 51),
          ("upsTemperatureHigh", 29),
          ("upsTemperatureLow", 30),
          ("webUserSession", 12),
          ("wirelessApAssociation", 86),
          ("wirelessApAuthenticationFailure", 88),
          ("wirelessApDisassociation", 87),
          ("wirelessClientConnected", 82),
          ("wirelessClientDisconnected", 83),
          ("wirelessClientSignalHigh", 85),
          ("wirelessClientSignalLow", 84))
    )


_OgAlarmType_Type.__name__ = "Integer32"
_OgAlarmType_Object = MibScalar
ogAlarmType = _OgAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 7),
    _OgAlarmType_Type()
)
ogAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmType.setStatus("mandatory")
_OgAlarmSummary_Type = OctetString
_OgAlarmSummary_Object = MibScalar
ogAlarmSummary = _OgAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 8),
    _OgAlarmSummary_Type()
)
ogAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmSummary.setStatus("mandatory")
_OgAlarmDevice_Type = OctetString
_OgAlarmDevice_Object = MibScalar
ogAlarmDevice = _OgAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 9),
    _OgAlarmDevice_Type()
)
ogAlarmDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmDevice.setStatus("mandatory")
_OgAlarmUser_Type = OctetString
_OgAlarmUser_Object = MibScalar
ogAlarmUser = _OgAlarmUser_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 10),
    _OgAlarmUser_Type()
)
ogAlarmUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmUser.setStatus("mandatory")
_OgAlarmTriggerValue_Type = Integer32
_OgAlarmTriggerValue_Object = MibScalar
ogAlarmTriggerValue = _OgAlarmTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 11),
    _OgAlarmTriggerValue_Type()
)
ogAlarmTriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmTriggerValue.setStatus("mandatory")
_OgAlarmCurrentValue_Type = Integer32
_OgAlarmCurrentValue_Object = MibScalar
ogAlarmCurrentValue = _OgAlarmCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 12),
    _OgAlarmCurrentValue_Type()
)
ogAlarmCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmCurrentValue.setStatus("mandatory")
_OgAlarmPreviousValue_Type = Integer32
_OgAlarmPreviousValue_Object = MibScalar
ogAlarmPreviousValue = _OgAlarmPreviousValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 13),
    _OgAlarmPreviousValue_Type()
)
ogAlarmPreviousValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmPreviousValue.setStatus("mandatory")


class _OgAlarmState_Type(Integer32):
    """Custom type ogAlarmState based on Integer32"""
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
        *(("disabled", 5),
          ("normal", 1),
          ("resolving", 3),
          ("triggered", 2),
          ("unresolvable", 6),
          ("waiting", 4))
    )


_OgAlarmState_Type.__name__ = "Integer32"
_OgAlarmState_Object = MibScalar
ogAlarmState = _OgAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 14),
    _OgAlarmState_Type()
)
ogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogAlarmState.setStatus("mandatory")
_OgSerialSignalMib_ObjectIdentity = ObjectIdentity
ogSerialSignalMib = _OgSerialSignalMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 102)
)
_OgSerialSignalMibObjects_ObjectIdentity = ObjectIdentity
ogSerialSignalMibObjects = _OgSerialSignalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 102, 1)
)
_OgSerialSignalAlarm_ObjectIdentity = ObjectIdentity
ogSerialSignalAlarm = _OgSerialSignalAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1)
)
_OgSerialSignalAlarmTable_ObjectIdentity = ObjectIdentity
ogSerialSignalAlarmTable = _OgSerialSignalAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1, 1)
)
_OgSerialSignalAlarmEntry_ObjectIdentity = ObjectIdentity
ogSerialSignalAlarmEntry = _OgSerialSignalAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1, 1, 1)
)
_OgSerialPatternMib_ObjectIdentity = ObjectIdentity
ogSerialPatternMib = _OgSerialPatternMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 103)
)
_OgSerialPatternMibObjects_ObjectIdentity = ObjectIdentity
ogSerialPatternMibObjects = _OgSerialPatternMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 103, 1)
)
_OgSerialPatternAlarm_ObjectIdentity = ObjectIdentity
ogSerialPatternAlarm = _OgSerialPatternAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1)
)
_OgSerialPatternAlarmTable_ObjectIdentity = ObjectIdentity
ogSerialPatternAlarmTable = _OgSerialPatternAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1, 1)
)
_OgSerialPatternAlarmEntry_ObjectIdentity = ObjectIdentity
ogSerialPatternAlarmEntry = _OgSerialPatternAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1, 1, 1)
)
_OgSerialUserMib_ObjectIdentity = ObjectIdentity
ogSerialUserMib = _OgSerialUserMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 104)
)
_OgSerialUserMibObjects_ObjectIdentity = ObjectIdentity
ogSerialUserMibObjects = _OgSerialUserMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 104, 1)
)
_OgSerialUserAlarm_ObjectIdentity = ObjectIdentity
ogSerialUserAlarm = _OgSerialUserAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1)
)
_OgSerialUserAlarmTable_ObjectIdentity = ObjectIdentity
ogSerialUserAlarmTable = _OgSerialUserAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1, 1)
)
_OgSerialUserAlarmEntry_ObjectIdentity = ObjectIdentity
ogSerialUserAlarmEntry = _OgSerialUserAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1, 1, 1)
)
_OgHostMib_ObjectIdentity = ObjectIdentity
ogHostMib = _OgHostMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 105)
)
_OgHostMibObjects_ObjectIdentity = ObjectIdentity
ogHostMibObjects = _OgHostMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 105, 1)
)
_OgHostEvent_ObjectIdentity = ObjectIdentity
ogHostEvent = _OgHostEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1)
)
_OgHostEventTable_ObjectIdentity = ObjectIdentity
ogHostEventTable = _OgHostEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1, 1)
)
_OgHostEventEntry_ObjectIdentity = ObjectIdentity
ogHostEventEntry = _OgHostEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1, 1, 1)
)
_OgWebMib_ObjectIdentity = ObjectIdentity
ogWebMib = _OgWebMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 106)
)
_OgWebMibObjects_ObjectIdentity = ObjectIdentity
ogWebMibObjects = _OgWebMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 106, 1)
)
_OgWebEvent_ObjectIdentity = ObjectIdentity
ogWebEvent = _OgWebEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1)
)
_OgWebEventTable_ObjectIdentity = ObjectIdentity
ogWebEventTable = _OgWebEventTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1, 1)
)
_OgWebEventEntry_ObjectIdentity = ObjectIdentity
ogWebEventEntry = _OgWebEventEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1, 1, 1)
)
_OgEmdMib_ObjectIdentity = ObjectIdentity
ogEmdMib = _OgEmdMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 107)
)
_OgEmdMibObjects_ObjectIdentity = ObjectIdentity
ogEmdMibObjects = _OgEmdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 107, 1)
)
_OgEmdAlarm_ObjectIdentity = ObjectIdentity
ogEmdAlarm = _OgEmdAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1)
)
_OgEmdAlarmTable_ObjectIdentity = ObjectIdentity
ogEmdAlarmTable = _OgEmdAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1, 1)
)
_OgEmdAlarmEntry_ObjectIdentity = ObjectIdentity
ogEmdAlarmEntry = _OgEmdAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1, 1, 1)
)
_OgPowerSupplyMib_ObjectIdentity = ObjectIdentity
ogPowerSupplyMib = _OgPowerSupplyMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 108)
)
_OgPowerSupplyMibObjects_ObjectIdentity = ObjectIdentity
ogPowerSupplyMibObjects = _OgPowerSupplyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 108, 1)
)
_OgPowerSupplyAlarm_ObjectIdentity = ObjectIdentity
ogPowerSupplyAlarm = _OgPowerSupplyAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1)
)
_OgPowerSupplyAlarmTable_ObjectIdentity = ObjectIdentity
ogPowerSupplyAlarmTable = _OgPowerSupplyAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1, 1)
)
_OgPowerSupplyAlarmEntry_ObjectIdentity = ObjectIdentity
ogPowerSupplyAlarmEntry = _OgPowerSupplyAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1, 1, 1)
)
_OgUpsMib_ObjectIdentity = ObjectIdentity
ogUpsMib = _OgUpsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 109)
)
_OgUpsMibObjects_ObjectIdentity = ObjectIdentity
ogUpsMibObjects = _OgUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 109, 1)
)
_OgUpsAlarm_ObjectIdentity = ObjectIdentity
ogUpsAlarm = _OgUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1)
)
_OgUpsAlarmTable_ObjectIdentity = ObjectIdentity
ogUpsAlarmTable = _OgUpsAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1, 1)
)
_OgUpsAlarmEntry_ObjectIdentity = ObjectIdentity
ogUpsAlarmEntry = _OgUpsAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1, 1, 1)
)
_OgRpcMib_ObjectIdentity = ObjectIdentity
ogRpcMib = _OgRpcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 110)
)
_OgRpcMibObjects_ObjectIdentity = ObjectIdentity
ogRpcMibObjects = _OgRpcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 110, 1)
)
_OgRpcAlarm_ObjectIdentity = ObjectIdentity
ogRpcAlarm = _OgRpcAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1)
)
_OgRpcAlarmTable_ObjectIdentity = ObjectIdentity
ogRpcAlarmTable = _OgRpcAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1, 1)
)
_OgRpcAlarmEntry_ObjectIdentity = ObjectIdentity
ogRpcAlarmEntry = _OgRpcAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1, 1, 1)
)
_OgNetMib_ObjectIdentity = ObjectIdentity
ogNetMib = _OgNetMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 111)
)
_OgNetMibObjects_ObjectIdentity = ObjectIdentity
ogNetMibObjects = _OgNetMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 111, 1)
)
_OgNetAlarm_ObjectIdentity = ObjectIdentity
ogNetAlarm = _OgNetAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1)
)
_OgNetAlarmTable_ObjectIdentity = ObjectIdentity
ogNetAlarmTable = _OgNetAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1, 1)
)
_OgNetAlarmEntry_ObjectIdentity = ObjectIdentity
ogNetAlarmEntry = _OgNetAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1, 1, 1)
)
_OgCellMib_ObjectIdentity = ObjectIdentity
ogCellMib = _OgCellMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 112)
)
_OgCellMibObjects_ObjectIdentity = ObjectIdentity
ogCellMibObjects = _OgCellMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 112, 1)
)
_OgCellAlarm_ObjectIdentity = ObjectIdentity
ogCellAlarm = _OgCellAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1)
)
_OgCellAlarmTable_ObjectIdentity = ObjectIdentity
ogCellAlarmTable = _OgCellAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1, 1)
)
_OgCellAlarmEntry_ObjectIdentity = ObjectIdentity
ogCellAlarmEntry = _OgCellAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1, 1, 1)
)
_OgWifiMib_ObjectIdentity = ObjectIdentity
ogWifiMib = _OgWifiMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 113)
)
_OgWifiMibObjects_ObjectIdentity = ObjectIdentity
ogWifiMibObjects = _OgWifiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 113, 1)
)
_OgWifiAlarm_ObjectIdentity = ObjectIdentity
ogWifiAlarm = _OgWifiAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1)
)
_OgWifiAlarmTable_ObjectIdentity = ObjectIdentity
ogWifiAlarmTable = _OgWifiAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1, 1)
)
_OgWifiAlarmEntry_ObjectIdentity = ObjectIdentity
ogWifiAlarmEntry = _OgWifiAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1, 1, 1)
)
_OgDialPoolMib_ObjectIdentity = ObjectIdentity
ogDialPoolMib = _OgDialPoolMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 114)
)
_OgDialPoolMibObjects_ObjectIdentity = ObjectIdentity
ogDialPoolMibObjects = _OgDialPoolMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 114, 1)
)
_OgDialPoolAlarm_ObjectIdentity = ObjectIdentity
ogDialPoolAlarm = _OgDialPoolAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1)
)
_OgDialPoolAlarmTable_ObjectIdentity = ObjectIdentity
ogDialPoolAlarmTable = _OgDialPoolAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1, 1)
)
_OgDialPoolAlarmEntry_ObjectIdentity = ObjectIdentity
ogDialPoolAlarmEntry = _OgDialPoolAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1, 1, 1)
)
_OgCustomMib_ObjectIdentity = ObjectIdentity
ogCustomMib = _OgCustomMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 115)
)
_OgCustomMibObjects_ObjectIdentity = ObjectIdentity
ogCustomMibObjects = _OgCustomMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 115, 1)
)
_OgCustomAlarm_ObjectIdentity = ObjectIdentity
ogCustomAlarm = _OgCustomAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1)
)
_OgCustomAlarmTable_ObjectIdentity = ObjectIdentity
ogCustomAlarmTable = _OgCustomAlarmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1, 1)
)
_OgCustomAlarmEntry_ObjectIdentity = ObjectIdentity
ogCustomAlarmEntry = _OgCustomAlarmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1, 1, 1)
)

# Managed Objects groups


# Notification objects

ogSerialSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 1)
)
ogSerialSignalNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialSignalNotification.setStatus(
        ""
    )

ogSerialPatternNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 2)
)
ogSerialPatternNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialPatternNotification.setStatus(
        ""
    )

ogSerialUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 3)
)
ogSerialUserNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogSerialUserNotification.setStatus(
        ""
    )

ogHostPingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 4)
)
ogHostPingNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostPingNotification.setStatus(
        ""
    )

ogHostServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 5)
)
ogHostServiceNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostServiceNotification.setStatus(
        ""
    )

ogHostUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 6)
)
ogHostUserNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogHostUserNotification.setStatus(
        ""
    )

ogWebUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 7)
)
ogWebUserNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWebUserNotification.setStatus(
        ""
    )

ogEmdTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 8)
)
ogEmdTemperatureNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdTemperatureNotification.setStatus(
        ""
    )

ogEmdHumidityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 9)
)
ogEmdHumidityNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdHumidityNotification.setStatus(
        ""
    )

ogEmdDioNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 10)
)
ogEmdDioNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogEmdDioNotification.setStatus(
        ""
    )

ogPowerSupplyInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 11)
)
ogPowerSupplyInputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyInputNotification.setStatus(
        ""
    )

ogPowerSupplyOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 12)
)
ogPowerSupplyOutputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyOutputNotification.setStatus(
        ""
    )

ogPowerSupplyTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 13)
)
ogPowerSupplyTempNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogPowerSupplyTempNotification.setStatus(
        ""
    )

ogUpsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 14)
)
ogUpsNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsNotification.setStatus(
        ""
    )

ogUpsBatteryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 15)
)
ogUpsBatteryNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsBatteryNotification.setStatus(
        ""
    )

ogUpsInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 16)
)
ogUpsInputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsInputNotification.setStatus(
        ""
    )

ogUpsOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 17)
)
ogUpsOutputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogUpsOutputNotification.setStatus(
        ""
    )

ogRpcInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 18)
)
ogRpcInputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcInputNotification.setStatus(
        ""
    )

ogRpcOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 19)
)
ogRpcOutputNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcOutputNotification.setStatus(
        ""
    )

ogRpcOutletNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 20)
)
ogRpcOutletNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogRpcOutletNotification.setStatus(
        ""
    )

ogNetInterfaceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 21)
)
ogNetInterfaceNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogNetInterfaceNotification.setStatus(
        ""
    )

ogCellDataNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 22)
)
ogCellDataNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellDataNotification.setStatus(
        ""
    )

ogCellMessageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 23)
)
ogCellMessageNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellMessageNotification.setStatus(
        ""
    )

ogCellSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 24)
)
ogCellSignalNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellSignalNotification.setStatus(
        ""
    )

ogCellApnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 25)
)
ogCellApnNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellApnNotification.setStatus(
        ""
    )

ogCellTowerNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 26)
)
ogCellTowerNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellTowerNotification.setStatus(
        ""
    )

ogCellNetworkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 27)
)
ogCellNetworkNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCellNetworkNotification.setStatus(
        ""
    )

ogWifiClientConnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 28)
)
ogWifiClientConnectNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiClientConnectNotification.setStatus(
        ""
    )

ogWifiClientSignalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 29)
)
ogWifiClientSignalNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiClientSignalNotification.setStatus(
        ""
    )

ogWifiApAssociationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 30)
)
ogWifiApAssociationNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiApAssociationNotification.setStatus(
        ""
    )

ogWifiApAuthNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 31)
)
ogWifiApAuthNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogWifiApAuthNotification.setStatus(
        ""
    )

ogDialPoolHealthNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 32)
)
ogDialPoolHealthNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogDialPoolHealthNotification.setStatus(
        ""
    )

ogCustomNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 0, 33)
)
ogCustomNotification.setObjects(
      *(("OGTRAPv2-MIB", "ogAlarmEventId"),
        ("OGTRAPv2-MIB", "ogAlarmName"),
        ("OGTRAPv2-MIB", "ogAlarmCheck"),
        ("OGTRAPv2-MIB", "ogAlarmInstance"),
        ("OGTRAPv2-MIB", "ogAlarmTime"),
        ("OGTRAPv2-MIB", "ogAlarmType"),
        ("OGTRAPv2-MIB", "ogAlarmSummary"),
        ("OGTRAPv2-MIB", "ogAlarmDevice"),
        ("OGTRAPv2-MIB", "ogAlarmUser"),
        ("OGTRAPv2-MIB", "ogAlarmTriggerValue"),
        ("OGTRAPv2-MIB", "ogAlarmCurrentValue"),
        ("OGTRAPv2-MIB", "ogAlarmPreviousValue"),
        ("OGTRAPv2-MIB", "ogAlarmState"))
)
if mibBuilder.loadTexts:
    ogCustomNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OGTRAPv2-MIB",
    **{"opengear": opengear,
       "ogSerialSignalNotification": ogSerialSignalNotification,
       "ogSerialPatternNotification": ogSerialPatternNotification,
       "ogSerialUserNotification": ogSerialUserNotification,
       "ogHostPingNotification": ogHostPingNotification,
       "ogHostServiceNotification": ogHostServiceNotification,
       "ogHostUserNotification": ogHostUserNotification,
       "ogWebUserNotification": ogWebUserNotification,
       "ogEmdTemperatureNotification": ogEmdTemperatureNotification,
       "ogEmdHumidityNotification": ogEmdHumidityNotification,
       "ogEmdDioNotification": ogEmdDioNotification,
       "ogPowerSupplyInputNotification": ogPowerSupplyInputNotification,
       "ogPowerSupplyOutputNotification": ogPowerSupplyOutputNotification,
       "ogPowerSupplyTempNotification": ogPowerSupplyTempNotification,
       "ogUpsNotification": ogUpsNotification,
       "ogUpsBatteryNotification": ogUpsBatteryNotification,
       "ogUpsInputNotification": ogUpsInputNotification,
       "ogUpsOutputNotification": ogUpsOutputNotification,
       "ogRpcInputNotification": ogRpcInputNotification,
       "ogRpcOutputNotification": ogRpcOutputNotification,
       "ogRpcOutletNotification": ogRpcOutletNotification,
       "ogNetInterfaceNotification": ogNetInterfaceNotification,
       "ogCellDataNotification": ogCellDataNotification,
       "ogCellMessageNotification": ogCellMessageNotification,
       "ogCellSignalNotification": ogCellSignalNotification,
       "ogCellApnNotification": ogCellApnNotification,
       "ogCellTowerNotification": ogCellTowerNotification,
       "ogCellNetworkNotification": ogCellNetworkNotification,
       "ogWifiClientConnectNotification": ogWifiClientConnectNotification,
       "ogWifiClientSignalNotification": ogWifiClientSignalNotification,
       "ogWifiApAssociationNotification": ogWifiApAssociationNotification,
       "ogWifiApAuthNotification": ogWifiApAuthNotification,
       "ogDialPoolHealthNotification": ogDialPoolHealthNotification,
       "ogCustomNotification": ogCustomNotification,
       "ogLegacyMgmt": ogLegacyMgmt,
       "ogNotification": ogNotification,
       "ogAlarmMib": ogAlarmMib,
       "ogAlarmMibObjects": ogAlarmMibObjects,
       "ogAlarm": ogAlarm,
       "ogAlarmTable": ogAlarmTable,
       "ogAlarmEntry": ogAlarmEntry,
       "ogAlarmIndex": ogAlarmIndex,
       "ogAlarmEventId": ogAlarmEventId,
       "ogAlarmName": ogAlarmName,
       "ogAlarmCheck": ogAlarmCheck,
       "ogAlarmInstance": ogAlarmInstance,
       "ogAlarmTime": ogAlarmTime,
       "ogAlarmType": ogAlarmType,
       "ogAlarmSummary": ogAlarmSummary,
       "ogAlarmDevice": ogAlarmDevice,
       "ogAlarmUser": ogAlarmUser,
       "ogAlarmTriggerValue": ogAlarmTriggerValue,
       "ogAlarmCurrentValue": ogAlarmCurrentValue,
       "ogAlarmPreviousValue": ogAlarmPreviousValue,
       "ogAlarmState": ogAlarmState,
       "ogSerialSignalMib": ogSerialSignalMib,
       "ogSerialSignalMibObjects": ogSerialSignalMibObjects,
       "ogSerialSignalAlarm": ogSerialSignalAlarm,
       "ogSerialSignalAlarmTable": ogSerialSignalAlarmTable,
       "ogSerialSignalAlarmEntry": ogSerialSignalAlarmEntry,
       "ogSerialPatternMib": ogSerialPatternMib,
       "ogSerialPatternMibObjects": ogSerialPatternMibObjects,
       "ogSerialPatternAlarm": ogSerialPatternAlarm,
       "ogSerialPatternAlarmTable": ogSerialPatternAlarmTable,
       "ogSerialPatternAlarmEntry": ogSerialPatternAlarmEntry,
       "ogSerialUserMib": ogSerialUserMib,
       "ogSerialUserMibObjects": ogSerialUserMibObjects,
       "ogSerialUserAlarm": ogSerialUserAlarm,
       "ogSerialUserAlarmTable": ogSerialUserAlarmTable,
       "ogSerialUserAlarmEntry": ogSerialUserAlarmEntry,
       "ogHostMib": ogHostMib,
       "ogHostMibObjects": ogHostMibObjects,
       "ogHostEvent": ogHostEvent,
       "ogHostEventTable": ogHostEventTable,
       "ogHostEventEntry": ogHostEventEntry,
       "ogWebMib": ogWebMib,
       "ogWebMibObjects": ogWebMibObjects,
       "ogWebEvent": ogWebEvent,
       "ogWebEventTable": ogWebEventTable,
       "ogWebEventEntry": ogWebEventEntry,
       "ogEmdMib": ogEmdMib,
       "ogEmdMibObjects": ogEmdMibObjects,
       "ogEmdAlarm": ogEmdAlarm,
       "ogEmdAlarmTable": ogEmdAlarmTable,
       "ogEmdAlarmEntry": ogEmdAlarmEntry,
       "ogPowerSupplyMib": ogPowerSupplyMib,
       "ogPowerSupplyMibObjects": ogPowerSupplyMibObjects,
       "ogPowerSupplyAlarm": ogPowerSupplyAlarm,
       "ogPowerSupplyAlarmTable": ogPowerSupplyAlarmTable,
       "ogPowerSupplyAlarmEntry": ogPowerSupplyAlarmEntry,
       "ogUpsMib": ogUpsMib,
       "ogUpsMibObjects": ogUpsMibObjects,
       "ogUpsAlarm": ogUpsAlarm,
       "ogUpsAlarmTable": ogUpsAlarmTable,
       "ogUpsAlarmEntry": ogUpsAlarmEntry,
       "ogRpcMib": ogRpcMib,
       "ogRpcMibObjects": ogRpcMibObjects,
       "ogRpcAlarm": ogRpcAlarm,
       "ogRpcAlarmTable": ogRpcAlarmTable,
       "ogRpcAlarmEntry": ogRpcAlarmEntry,
       "ogNetMib": ogNetMib,
       "ogNetMibObjects": ogNetMibObjects,
       "ogNetAlarm": ogNetAlarm,
       "ogNetAlarmTable": ogNetAlarmTable,
       "ogNetAlarmEntry": ogNetAlarmEntry,
       "ogCellMib": ogCellMib,
       "ogCellMibObjects": ogCellMibObjects,
       "ogCellAlarm": ogCellAlarm,
       "ogCellAlarmTable": ogCellAlarmTable,
       "ogCellAlarmEntry": ogCellAlarmEntry,
       "ogWifiMib": ogWifiMib,
       "ogWifiMibObjects": ogWifiMibObjects,
       "ogWifiAlarm": ogWifiAlarm,
       "ogWifiAlarmTable": ogWifiAlarmTable,
       "ogWifiAlarmEntry": ogWifiAlarmEntry,
       "ogDialPoolMib": ogDialPoolMib,
       "ogDialPoolMibObjects": ogDialPoolMibObjects,
       "ogDialPoolAlarm": ogDialPoolAlarm,
       "ogDialPoolAlarmTable": ogDialPoolAlarmTable,
       "ogDialPoolAlarmEntry": ogDialPoolAlarmEntry,
       "ogCustomMib": ogCustomMib,
       "ogCustomMibObjects": ogCustomMibObjects,
       "ogCustomAlarm": ogCustomAlarm,
       "ogCustomAlarmTable": ogCustomAlarmTable,
       "ogCustomAlarmEntry": ogCustomAlarmEntry}
)
