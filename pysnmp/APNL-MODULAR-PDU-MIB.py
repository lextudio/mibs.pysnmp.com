# SNMP MIB module (APNL-MODULAR-PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APNL-MODULAR-PDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:25 2024
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

apNederland = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29640)
)
apNederland.setRevisions(
        ("2013-01-24 13:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApnlDirectory_ObjectIdentity = ObjectIdentity
apnlDirectory = _ApnlDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 1)
)
_ApnlMib_ObjectIdentity = ObjectIdentity
apnlMib = _ApnlMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 2)
)
_ApnlTmp_ObjectIdentity = ObjectIdentity
apnlTmp = _ApnlTmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 3)
)
_ApnlModules_ObjectIdentity = ObjectIdentity
apnlModules = _ApnlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 4)
)
_Cm_ObjectIdentity = ObjectIdentity
cm = _Cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 4, 1)
)
_CmTraps_ObjectIdentity = ObjectIdentity
cmTraps = _CmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 4, 2)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3)
)


class _PduType_Type(Integer32):
    """Custom type pduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pduGateway1", 1),
          ("pduGateway2", 2),
          ("pduModular", 0))
    )


_PduType_Type.__name__ = "Integer32"
_PduType_Object = MibScalar
pduType = _PduType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 1),
    _PduType_Type()
)
pduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduType.setStatus("current")
_PduProductIdentifier_Type = Integer32
_PduProductIdentifier_Object = MibScalar
pduProductIdentifier = _PduProductIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 2),
    _PduProductIdentifier_Type()
)
pduProductIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduProductIdentifier.setStatus("current")


class _PduSerialNumber_Type(DisplayString):
    """Custom type pduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PduSerialNumber_Type.__name__ = "DisplayString"
_PduSerialNumber_Object = MibScalar
pduSerialNumber = _PduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 3),
    _PduSerialNumber_Type()
)
pduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSerialNumber.setStatus("current")


class _PduStatus_Type(Integer32):
    """Custom type pduStatus based on Integer32"""
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
        *(("pduAlarm", 2),
          ("pduBusy", 0),
          ("pduError", 3),
          ("pduReady1", 1))
    )


_PduStatus_Type.__name__ = "Integer32"
_PduStatus_Object = MibScalar
pduStatus = _PduStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 4),
    _PduStatus_Type()
)
pduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatus.setStatus("current")
_PduPower_Type = Unsigned32
_PduPower_Object = MibScalar
pduPower = _PduPower_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 5),
    _PduPower_Type()
)
pduPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPower.setStatus("current")
if mibBuilder.loadTexts:
    pduPower.setUnits("kiloWattHours")
_PduPowerL1_Type = Unsigned32
_PduPowerL1_Object = MibScalar
pduPowerL1 = _PduPowerL1_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 6),
    _PduPowerL1_Type()
)
pduPowerL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerL1.setStatus("current")
if mibBuilder.loadTexts:
    pduPowerL1.setUnits("kiloWattHours")
_PduPowerL2_Type = Unsigned32
_PduPowerL2_Object = MibScalar
pduPowerL2 = _PduPowerL2_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 7),
    _PduPowerL2_Type()
)
pduPowerL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerL2.setStatus("current")
if mibBuilder.loadTexts:
    pduPowerL2.setUnits("kiloWattHours")
_PduPowerL3_Type = Unsigned32
_PduPowerL3_Object = MibScalar
pduPowerL3 = _PduPowerL3_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 8),
    _PduPowerL3_Type()
)
pduPowerL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPowerL3.setStatus("current")
if mibBuilder.loadTexts:
    pduPowerL3.setUnits("kiloWattHours")
_PduKvar_Type = Unsigned32
_PduKvar_Object = MibScalar
pduKvar = _PduKvar_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 9),
    _PduKvar_Type()
)
pduKvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduKvar.setStatus("current")
if mibBuilder.loadTexts:
    pduKvar.setUnits("KiloWattHours")
_PduKvarL1_Type = Unsigned32
_PduKvarL1_Object = MibScalar
pduKvarL1 = _PduKvarL1_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 10),
    _PduKvarL1_Type()
)
pduKvarL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduKvarL1.setStatus("current")
if mibBuilder.loadTexts:
    pduKvarL1.setUnits("KiloWattHours")
_PduKvarL2_Type = Unsigned32
_PduKvarL2_Object = MibScalar
pduKvarL2 = _PduKvarL2_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 11),
    _PduKvarL2_Type()
)
pduKvarL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduKvarL2.setStatus("current")
if mibBuilder.loadTexts:
    pduKvarL2.setUnits("KiloWattHours")
_PduKvarL3_Type = Unsigned32
_PduKvarL3_Object = MibScalar
pduKvarL3 = _PduKvarL3_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 12),
    _PduKvarL3_Type()
)
pduKvarL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduKvarL3.setStatus("current")
if mibBuilder.loadTexts:
    pduKvarL3.setUnits("KiloWattHours")
_PdulAcurrent_Type = Unsigned32
_PdulAcurrent_Object = MibScalar
pdulAcurrent = _PdulAcurrent_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 13),
    _PdulAcurrent_Type()
)
pdulAcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdulAcurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdulAcurrent.setUnits("DeciAmpers")
_PduAcurrentL1_Type = Unsigned32
_PduAcurrentL1_Object = MibScalar
pduAcurrentL1 = _PduAcurrentL1_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 14),
    _PduAcurrentL1_Type()
)
pduAcurrentL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduAcurrentL1.setStatus("current")
if mibBuilder.loadTexts:
    pduAcurrentL1.setUnits("DeciAmpers")
_PduAcurrentL2_Type = Unsigned32
_PduAcurrentL2_Object = MibScalar
pduAcurrentL2 = _PduAcurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 15),
    _PduAcurrentL2_Type()
)
pduAcurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduAcurrentL2.setStatus("current")
if mibBuilder.loadTexts:
    pduAcurrentL2.setUnits("DeciAmpers")
_PduAcurrentL3_Type = Unsigned32
_PduAcurrentL3_Object = MibScalar
pduAcurrentL3 = _PduAcurrentL3_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 16),
    _PduAcurrentL3_Type()
)
pduAcurrentL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduAcurrentL3.setStatus("current")
if mibBuilder.loadTexts:
    pduAcurrentL3.setUnits("DeciAmpers")
_PduCurIpAddress_Type = IpAddress
_PduCurIpAddress_Object = MibScalar
pduCurIpAddress = _PduCurIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 17),
    _PduCurIpAddress_Type()
)
pduCurIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCurIpAddress.setStatus("current")
if mibBuilder.loadTexts:
    pduCurIpAddress.setUnits("IPv4 Addr")
_PduCurSubNetMask_Type = IpAddress
_PduCurSubNetMask_Object = MibScalar
pduCurSubNetMask = _PduCurSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 18),
    _PduCurSubNetMask_Type()
)
pduCurSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCurSubNetMask.setStatus("current")
if mibBuilder.loadTexts:
    pduCurSubNetMask.setUnits("IPv4 Addr")
_PduCurDefGwAddress_Type = IpAddress
_PduCurDefGwAddress_Object = MibScalar
pduCurDefGwAddress = _PduCurDefGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 19),
    _PduCurDefGwAddress_Type()
)
pduCurDefGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCurDefGwAddress.setStatus("current")
if mibBuilder.loadTexts:
    pduCurDefGwAddress.setUnits("IPv4 Addr")
_PduNumberOfNodes_Type = Integer32
_PduNumberOfNodes_Object = MibScalar
pduNumberOfNodes = _PduNumberOfNodes_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 20),
    _PduNumberOfNodes_Type()
)
pduNumberOfNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumberOfNodes.setStatus("current")
_PduNumberOfSensors_Type = Integer32
_PduNumberOfSensors_Object = MibScalar
pduNumberOfSensors = _PduNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 21),
    _PduNumberOfSensors_Type()
)
pduNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumberOfSensors.setStatus("current")


class _PduSoftwareVersion_Type(DisplayString):
    """Custom type pduSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_PduSoftwareVersion_Type.__name__ = "DisplayString"
_PduSoftwareVersion_Object = MibScalar
pduSoftwareVersion = _PduSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 22),
    _PduSoftwareVersion_Type()
)
pduSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSoftwareVersion.setStatus("current")


class _PduFirmwareVersion_Type(DisplayString):
    """Custom type pduFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_PduFirmwareVersion_Type.__name__ = "DisplayString"
_PduFirmwareVersion_Object = MibScalar
pduFirmwareVersion = _PduFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 23),
    _PduFirmwareVersion_Type()
)
pduFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFirmwareVersion.setStatus("current")


class _PduBusProtocol_Type(Integer32):
    """Custom type pduBusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apbus", 0),
          ("modbus", 1))
    )


_PduBusProtocol_Type.__name__ = "Integer32"
_PduBusProtocol_Object = MibScalar
pduBusProtocol = _PduBusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 24),
    _PduBusProtocol_Type()
)
pduBusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBusProtocol.setStatus("current")


class _PduAdminCommand_Type(Integer32):
    """Custom type pduAdminCommand based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("readDataFromBusPdu", 7),
          ("rebootPdu", 1),
          ("rediscover", 2),
          ("resetConfig", 4),
          ("resetNetworkSetting", 6),
          ("resetSNMPv3Config", 5),
          ("updateSofware", 3),
          ("writeDataToBusPdu", 8))
    )


_PduAdminCommand_Type.__name__ = "Integer32"
_PduAdminCommand_Object = MibScalar
pduAdminCommand = _PduAdminCommand_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 25),
    _PduAdminCommand_Type()
)
pduAdminCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAdminCommand.setStatus("current")
_PduStartupIpAddress_Type = IpAddress
_PduStartupIpAddress_Object = MibScalar
pduStartupIpAddress = _PduStartupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 26),
    _PduStartupIpAddress_Type()
)
pduStartupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStartupIpAddress.setStatus("current")
if mibBuilder.loadTexts:
    pduStartupIpAddress.setUnits("IPv4 Addr")
_PduStartupSubNetMask_Type = IpAddress
_PduStartupSubNetMask_Object = MibScalar
pduStartupSubNetMask = _PduStartupSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 27),
    _PduStartupSubNetMask_Type()
)
pduStartupSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStartupSubNetMask.setStatus("current")
if mibBuilder.loadTexts:
    pduStartupSubNetMask.setUnits("IPv4 Addr")
_PduStartupDefGwAddress_Type = IpAddress
_PduStartupDefGwAddress_Object = MibScalar
pduStartupDefGwAddress = _PduStartupDefGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 28),
    _PduStartupDefGwAddress_Type()
)
pduStartupDefGwAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStartupDefGwAddress.setStatus("current")
if mibBuilder.loadTexts:
    pduStartupDefGwAddress.setUnits("IPv4 Addr")
_PduRealTimeClock_Type = DateAndTime
_PduRealTimeClock_Object = MibScalar
pduRealTimeClock = _PduRealTimeClock_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 29),
    _PduRealTimeClock_Type()
)
pduRealTimeClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduRealTimeClock.setStatus("current")


class _PduEnableFeatures_Type(Bits):
    """Custom type pduEnableFeatures based on Bits"""
    namedValues = NamedValues(
        *(("displaySwitchEnabled", 3),
          ("globalSwitchEnabled", 2),
          ("globalUsbEnabled", 1),
          ("globalWebEnabled", 0),
          ("webSwitchEnabled", 4))
    )

_PduEnableFeatures_Type.__name__ = "Bits"
_PduEnableFeatures_Object = MibScalar
pduEnableFeatures = _PduEnableFeatures_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 30),
    _PduEnableFeatures_Type()
)
pduEnableFeatures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnableFeatures.setStatus("current")
_PduBusAddress_Type = Integer32
_PduBusAddress_Object = MibScalar
pduBusAddress = _PduBusAddress_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 31),
    _PduBusAddress_Type()
)
pduBusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBusAddress.setStatus("current")


class _PduName_Type(DisplayString):
    """Custom type pduName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PduName_Type.__name__ = "DisplayString"
_PduName_Object = MibScalar
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 32),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("current")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1)
)
nodeEntry.setIndexNames(
    (0, "APNL-MODULAR-PDU-MIB", "nodeIndex"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("current")


class _NodeIndex_Type(Unsigned32):
    """Custom type nodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NodeIndex_Type.__name__ = "Unsigned32"
_NodeIndex_Object = MibTableColumn
nodeIndex = _NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 1),
    _NodeIndex_Type()
)
nodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeIndex.setStatus("current")


class _NodeType_Type(Integer32):
    """Custom type nodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("typePowerMeter", 4),
          ("typePowerMeterSwitch", 5),
          ("typePresModChar", 1),
          ("typePresModGraph", 3),
          ("typePresModMono", 2),
          ("typeSwitch", 6),
          ("typeUnknown", 0))
    )


_NodeType_Type.__name__ = "Integer32"
_NodeType_Object = MibTableColumn
nodeType = _NodeType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 2),
    _NodeType_Type()
)
nodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeType.setStatus("current")
_NodeOutlet_Type = Unsigned32
_NodeOutlet_Object = MibTableColumn
nodeOutlet = _NodeOutlet_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 3),
    _NodeOutlet_Type()
)
nodeOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOutlet.setStatus("current")


class _NodeAlarmStatus_Type(Bits):
    """Custom type nodeAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("switchOff", 5),
          ("switchOn", 4),
          ("trapCurrHi", 0),
          ("trapCurrLo", 1),
          ("trapVoltHi", 2),
          ("trapVoltLo", 3))
    )

_NodeAlarmStatus_Type.__name__ = "Bits"
_NodeAlarmStatus_Object = MibTableColumn
nodeAlarmStatus = _NodeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 4),
    _NodeAlarmStatus_Type()
)
nodeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeAlarmStatus.setStatus("current")
_NodePower_Type = Unsigned32
_NodePower_Object = MibTableColumn
nodePower = _NodePower_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 5),
    _NodePower_Type()
)
nodePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePower.setStatus("current")
if mibBuilder.loadTexts:
    nodePower.setUnits("kiloWattHours")
_NodeAcurrent_Type = Unsigned32
_NodeAcurrent_Object = MibTableColumn
nodeAcurrent = _NodeAcurrent_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 6),
    _NodeAcurrent_Type()
)
nodeAcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeAcurrent.setStatus("current")
if mibBuilder.loadTexts:
    nodeAcurrent.setUnits("DeciAmpers")
_NodePeakCurrent_Type = Unsigned32
_NodePeakCurrent_Object = MibTableColumn
nodePeakCurrent = _NodePeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 7),
    _NodePeakCurrent_Type()
)
nodePeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePeakCurrent.setStatus("current")
if mibBuilder.loadTexts:
    nodePeakCurrent.setUnits("DeciAmpers")
_NodeVoltage_Type = Unsigned32
_NodeVoltage_Object = MibTableColumn
nodeVoltage = _NodeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 8),
    _NodeVoltage_Type()
)
nodeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    nodeVoltage.setUnits("Volts")
_NodeMinVoltage_Type = Unsigned32
_NodeMinVoltage_Object = MibTableColumn
nodeMinVoltage = _NodeMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 9),
    _NodeMinVoltage_Type()
)
nodeMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMinVoltage.setStatus("current")
if mibBuilder.loadTexts:
    nodeMinVoltage.setUnits("Volts")
_NodeKvar_Type = Unsigned32
_NodeKvar_Object = MibTableColumn
nodeKvar = _NodeKvar_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 10),
    _NodeKvar_Type()
)
nodeKvar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeKvar.setStatus("current")
if mibBuilder.loadTexts:
    nodeKvar.setUnits("KiloWattHours")
_NodeFrequency_Type = Unsigned32
_NodeFrequency_Object = MibTableColumn
nodeFrequency = _NodeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 11),
    _NodeFrequency_Type()
)
nodeFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFrequency.setStatus("current")
if mibBuilder.loadTexts:
    nodeFrequency.setUnits("Hertz")
_NodePowerFactor_Type = Unsigned32
_NodePowerFactor_Object = MibTableColumn
nodePowerFactor = _NodePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 12),
    _NodePowerFactor_Type()
)
nodePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    nodePowerFactor.setUnits("Percent")


class _NodeSwitchOperStatus_Type(Integer32):
    """Custom type nodeSwitchOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_NodeSwitchOperStatus_Type.__name__ = "Integer32"
_NodeSwitchOperStatus_Object = MibTableColumn
nodeSwitchOperStatus = _NodeSwitchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 13),
    _NodeSwitchOperStatus_Type()
)
nodeSwitchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSwitchOperStatus.setStatus("current")


class _NodeSwitchAdminStatus_Type(Integer32):
    """Custom type nodeSwitchAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_NodeSwitchAdminStatus_Type.__name__ = "Integer32"
_NodeSwitchAdminStatus_Object = MibTableColumn
nodeSwitchAdminStatus = _NodeSwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 14),
    _NodeSwitchAdminStatus_Type()
)
nodeSwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSwitchAdminStatus.setStatus("current")
_NodeCurrHiThresh_Type = Unsigned32
_NodeCurrHiThresh_Object = MibTableColumn
nodeCurrHiThresh = _NodeCurrHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 15),
    _NodeCurrHiThresh_Type()
)
nodeCurrHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeCurrHiThresh.setStatus("current")
if mibBuilder.loadTexts:
    nodeCurrHiThresh.setUnits("DeciAmpers")
_NodeCurrLoThresh_Type = Unsigned32
_NodeCurrLoThresh_Object = MibTableColumn
nodeCurrLoThresh = _NodeCurrLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 16),
    _NodeCurrLoThresh_Type()
)
nodeCurrLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeCurrLoThresh.setStatus("current")
if mibBuilder.loadTexts:
    nodeCurrLoThresh.setUnits("DeciAmpers")
_NodeVoltHiThresh_Type = Unsigned32
_NodeVoltHiThresh_Object = MibTableColumn
nodeVoltHiThresh = _NodeVoltHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 17),
    _NodeVoltHiThresh_Type()
)
nodeVoltHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeVoltHiThresh.setStatus("current")
if mibBuilder.loadTexts:
    nodeVoltHiThresh.setUnits("Volts")
_NodeVoltLoThresh_Type = Unsigned32
_NodeVoltLoThresh_Object = MibTableColumn
nodeVoltLoThresh = _NodeVoltLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 18),
    _NodeVoltLoThresh_Type()
)
nodeVoltLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeVoltLoThresh.setStatus("current")
if mibBuilder.loadTexts:
    nodeVoltLoThresh.setUnits("Volts")


class _NodeAlarmSelector_Type(Bits):
    """Custom type nodeAlarmSelector based on Bits"""
    namedValues = NamedValues(
        *(("switchOff", 5),
          ("switchOn", 4),
          ("trapCurrHi", 0),
          ("trapCurrLo", 1),
          ("trapVoltHi", 2),
          ("trapVoltLo", 3))
    )

_NodeAlarmSelector_Type.__name__ = "Bits"
_NodeAlarmSelector_Object = MibTableColumn
nodeAlarmSelector = _NodeAlarmSelector_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 19),
    _NodeAlarmSelector_Type()
)
nodeAlarmSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeAlarmSelector.setStatus("current")


class _NodeName_Type(DisplayString):
    """Custom type nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_NodeName_Type.__name__ = "DisplayString"
_NodeName_Object = MibTableColumn
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 20),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")


class _NodePhase_Type(Integer32):
    """Custom type nodePhase based on Integer32"""
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
        *(("phaseL1", 1),
          ("phaseL2", 2),
          ("phaseL3", 3),
          ("phaseUnknown", 0))
    )


_NodePhase_Type.__name__ = "Integer32"
_NodePhase_Object = MibTableColumn
nodePhase = _NodePhase_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 33, 1, 21),
    _NodePhase_Type()
)
nodePhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodePhase.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1)
)
sensorEntry.setIndexNames(
    (0, "APNL-MODULAR-PDU-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorIndex_Type(Unsigned32):
    """Custom type sensorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SensorIndex_Type.__name__ = "Unsigned32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")


class _SensorType_Type(Integer32):
    """Custom type sensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("co1", 4),
          ("doorStatus", 6),
          ("humidity", 2),
          ("other", 0),
          ("smoke", 3),
          ("temperature", 1),
          ("vibration", 5))
    )


_SensorType_Type.__name__ = "Integer32"
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 2),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")


class _SensorAlarmStatus_Type(Bits):
    """Custom type sensorAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("beeperHi", 4),
          ("beeperLo", 5),
          ("switchOff", 3),
          ("switchOn", 2),
          ("trapHi", 0),
          ("trapLo", 1))
    )

_SensorAlarmStatus_Type.__name__ = "Bits"
_SensorAlarmStatus_Object = MibTableColumn
sensorAlarmStatus = _SensorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 3),
    _SensorAlarmStatus_Type()
)
sensorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorAlarmStatus.setStatus("current")
_SensorValue_Type = Integer32
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 4),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
if mibBuilder.loadTexts:
    sensorValue.setUnits("by type")


class _SensorSwitchOperStatus_Type(Integer32):
    """Custom type sensorSwitchOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_SensorSwitchOperStatus_Type.__name__ = "Integer32"
_SensorSwitchOperStatus_Object = MibTableColumn
sensorSwitchOperStatus = _SensorSwitchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 5),
    _SensorSwitchOperStatus_Type()
)
sensorSwitchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSwitchOperStatus.setStatus("current")


class _SensorSwitchAdminStatus_Type(Integer32):
    """Custom type sensorSwitchAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_SensorSwitchAdminStatus_Type.__name__ = "Integer32"
_SensorSwitchAdminStatus_Object = MibTableColumn
sensorSwitchAdminStatus = _SensorSwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 6),
    _SensorSwitchAdminStatus_Type()
)
sensorSwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorSwitchAdminStatus.setStatus("current")
_SensorHiThresh_Type = Integer32
_SensorHiThresh_Object = MibTableColumn
sensorHiThresh = _SensorHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 7),
    _SensorHiThresh_Type()
)
sensorHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorHiThresh.setStatus("current")
if mibBuilder.loadTexts:
    sensorHiThresh.setUnits("by type")
_SensorLoThresh_Type = Integer32
_SensorLoThresh_Object = MibTableColumn
sensorLoThresh = _SensorLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 8),
    _SensorLoThresh_Type()
)
sensorLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorLoThresh.setStatus("current")
if mibBuilder.loadTexts:
    sensorLoThresh.setUnits("by type")


class _SensorAlarmSelector_Type(Bits):
    """Custom type sensorAlarmSelector based on Bits"""
    namedValues = NamedValues(
        *(("beeperHi", 4),
          ("beeperLo", 5),
          ("switchOff", 3),
          ("switchOn", 2),
          ("trapHi", 0),
          ("trapLo", 1))
    )

_SensorAlarmSelector_Type.__name__ = "Bits"
_SensorAlarmSelector_Object = MibTableColumn
sensorAlarmSelector = _SensorAlarmSelector_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 9),
    _SensorAlarmSelector_Type()
)
sensorAlarmSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmSelector.setStatus("current")


class _SensorName_Type(DisplayString):
    """Custom type sensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SensorName_Type.__name__ = "DisplayString"
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 3, 34, 1, 10),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4)
)


class _TrapType_Type(Integer32):
    """Custom type trapType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("blackBoxColdTrap", 11),
          ("currentHiAlarm", 2),
          ("currentLoAlarm", 3),
          ("humidityHiAlarm", 6),
          ("humidityLoAlarm", 7),
          ("powerHiAlarm", 10),
          ("switchOffAlarm", 9),
          ("switchOnAlarm", 8),
          ("tempHiAlarm", 4),
          ("tempLoAlarm", 5),
          ("voltageHiAlarm", 0),
          ("voltageLoAlarm", 1))
    )


_TrapType_Type.__name__ = "Integer32"
_TrapType_Object = MibScalar
trapType = _TrapType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 1),
    _TrapType_Type()
)
trapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapType.setStatus("current")


class _PduTableType_Type(Integer32):
    """Custom type pduTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pduNodeTable", 0),
          ("pduSensorTable", 1))
    )


_PduTableType_Type.__name__ = "Integer32"
_PduTableType_Object = MibScalar
pduTableType = _PduTableType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 2),
    _PduTableType_Type()
)
pduTableType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduTableType.setStatus("current")
_TrapTableIndex_Type = Integer32
_TrapTableIndex_Object = MibScalar
trapTableIndex = _TrapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 3),
    _TrapTableIndex_Type()
)
trapTableIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTableIndex.setStatus("current")


class _TrapThreshHoldType_Type(Integer32):
    """Custom type trapThreshHoldType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapThresholdHi", 1),
          ("trapThresholdLo", 2),
          ("trapThresholdOther", 0))
    )


_TrapThreshHoldType_Type.__name__ = "Integer32"
_TrapThreshHoldType_Object = MibScalar
trapThreshHoldType = _TrapThreshHoldType_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 4),
    _TrapThreshHoldType_Type()
)
trapThreshHoldType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapThreshHoldType.setStatus("current")
_TrapThreshHold_Type = Integer32
_TrapThreshHold_Object = MibScalar
trapThreshHold = _TrapThreshHold_Object(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 5),
    _TrapThreshHold_Type()
)
trapThreshHold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapThreshHold.setStatus("current")
_ApnlTest_ObjectIdentity = ObjectIdentity
apnlTest = _ApnlTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 5)
)
_ApnlDemo_ObjectIdentity = ObjectIdentity
apnlDemo = _ApnlDemo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 6)
)
_ApnlMIBConformance_ObjectIdentity = ObjectIdentity
apnlMIBConformance = _ApnlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29640, 7)
)

# Managed Objects groups


# Notification objects

pduVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 6)
)
pduVoltageAlarm.setObjects(
      *(("APNL-MODULAR-PDU-MIB", "trapType"),
        ("APNL-MODULAR-PDU-MIB", "trapTableIndex"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHoldType"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHold"))
)
if mibBuilder.loadTexts:
    pduVoltageAlarm.setStatus(
        "current"
    )

pduCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 7)
)
pduCurrentAlarm.setObjects(
      *(("APNL-MODULAR-PDU-MIB", "trapType"),
        ("APNL-MODULAR-PDU-MIB", "trapTableIndex"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHoldType"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHold"))
)
if mibBuilder.loadTexts:
    pduCurrentAlarm.setStatus(
        "current"
    )

pduPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 8)
)
pduPowerAlarm.setObjects(
      *(("APNL-MODULAR-PDU-MIB", "trapType"),
        ("APNL-MODULAR-PDU-MIB", "trapTableIndex"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHoldType"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHold"))
)
if mibBuilder.loadTexts:
    pduPowerAlarm.setStatus(
        "current"
    )

sensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 9)
)
sensorAlarm.setObjects(
      *(("APNL-MODULAR-PDU-MIB", "trapType"),
        ("APNL-MODULAR-PDU-MIB", "trapTableIndex"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHoldType"),
        ("APNL-MODULAR-PDU-MIB", "trapThreshHold"))
)
if mibBuilder.loadTexts:
    sensorAlarm.setStatus(
        "current"
    )

pduSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 29640, 4, 4, 10)
)
pduSwitchAlarm.setObjects(
      *(("APNL-MODULAR-PDU-MIB", "trapType"),
        ("APNL-MODULAR-PDU-MIB", "trapTableIndex"))
)
if mibBuilder.loadTexts:
    pduSwitchAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APNL-MODULAR-PDU-MIB",
    **{"apNederland": apNederland,
       "apnlDirectory": apnlDirectory,
       "apnlMib": apnlMib,
       "apnlTmp": apnlTmp,
       "apnlModules": apnlModules,
       "cm": cm,
       "cmTraps": cmTraps,
       "pdu": pdu,
       "pduType": pduType,
       "pduProductIdentifier": pduProductIdentifier,
       "pduSerialNumber": pduSerialNumber,
       "pduStatus": pduStatus,
       "pduPower": pduPower,
       "pduPowerL1": pduPowerL1,
       "pduPowerL2": pduPowerL2,
       "pduPowerL3": pduPowerL3,
       "pduKvar": pduKvar,
       "pduKvarL1": pduKvarL1,
       "pduKvarL2": pduKvarL2,
       "pduKvarL3": pduKvarL3,
       "pdulAcurrent": pdulAcurrent,
       "pduAcurrentL1": pduAcurrentL1,
       "pduAcurrentL2": pduAcurrentL2,
       "pduAcurrentL3": pduAcurrentL3,
       "pduCurIpAddress": pduCurIpAddress,
       "pduCurSubNetMask": pduCurSubNetMask,
       "pduCurDefGwAddress": pduCurDefGwAddress,
       "pduNumberOfNodes": pduNumberOfNodes,
       "pduNumberOfSensors": pduNumberOfSensors,
       "pduSoftwareVersion": pduSoftwareVersion,
       "pduFirmwareVersion": pduFirmwareVersion,
       "pduBusProtocol": pduBusProtocol,
       "pduAdminCommand": pduAdminCommand,
       "pduStartupIpAddress": pduStartupIpAddress,
       "pduStartupSubNetMask": pduStartupSubNetMask,
       "pduStartupDefGwAddress": pduStartupDefGwAddress,
       "pduRealTimeClock": pduRealTimeClock,
       "pduEnableFeatures": pduEnableFeatures,
       "pduBusAddress": pduBusAddress,
       "pduName": pduName,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeIndex": nodeIndex,
       "nodeType": nodeType,
       "nodeOutlet": nodeOutlet,
       "nodeAlarmStatus": nodeAlarmStatus,
       "nodePower": nodePower,
       "nodeAcurrent": nodeAcurrent,
       "nodePeakCurrent": nodePeakCurrent,
       "nodeVoltage": nodeVoltage,
       "nodeMinVoltage": nodeMinVoltage,
       "nodeKvar": nodeKvar,
       "nodeFrequency": nodeFrequency,
       "nodePowerFactor": nodePowerFactor,
       "nodeSwitchOperStatus": nodeSwitchOperStatus,
       "nodeSwitchAdminStatus": nodeSwitchAdminStatus,
       "nodeCurrHiThresh": nodeCurrHiThresh,
       "nodeCurrLoThresh": nodeCurrLoThresh,
       "nodeVoltHiThresh": nodeVoltHiThresh,
       "nodeVoltLoThresh": nodeVoltLoThresh,
       "nodeAlarmSelector": nodeAlarmSelector,
       "nodeName": nodeName,
       "nodePhase": nodePhase,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorType": sensorType,
       "sensorAlarmStatus": sensorAlarmStatus,
       "sensorValue": sensorValue,
       "sensorSwitchOperStatus": sensorSwitchOperStatus,
       "sensorSwitchAdminStatus": sensorSwitchAdminStatus,
       "sensorHiThresh": sensorHiThresh,
       "sensorLoThresh": sensorLoThresh,
       "sensorAlarmSelector": sensorAlarmSelector,
       "sensorName": sensorName,
       "pduTraps": pduTraps,
       "trapType": trapType,
       "pduTableType": pduTableType,
       "trapTableIndex": trapTableIndex,
       "trapThreshHoldType": trapThreshHoldType,
       "trapThreshHold": trapThreshHold,
       "pduVoltageAlarm": pduVoltageAlarm,
       "pduCurrentAlarm": pduCurrentAlarm,
       "pduPowerAlarm": pduPowerAlarm,
       "sensorAlarm": sensorAlarm,
       "pduSwitchAlarm": pduSwitchAlarm,
       "apnlTest": apnlTest,
       "apnlDemo": apnlDemo,
       "apnlMIBConformance": apnlMIBConformance}
)
