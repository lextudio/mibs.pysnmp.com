# SNMP MIB module (GBNDeviceSwitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNDeviceSwitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:45 2024
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

(gbnDevice,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnDevice")

(PortList,
 VlanIndex,
 dot1qStaticMulticastEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qStaticMulticastEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnDeviceSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1)
)
gbnDeviceSwitch.setRevisions(
        ("1900-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GbnDeviceSwitchMirror_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchMirror = _GbnDeviceSwitchMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 1)
)


class _MirroringPort_Type(Integer32):
    """Custom type mirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_MirroringPort_Type.__name__ = "Integer32"
_MirroringPort_Object = MibScalar
mirroringPort = _MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 1, 1),
    _MirroringPort_Type()
)
mirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroringPort.setStatus("current")
_MirroredEgrPort_Type = PortList
_MirroredEgrPort_Object = MibScalar
mirroredEgrPort = _MirroredEgrPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 1, 2),
    _MirroredEgrPort_Type()
)
mirroredEgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroredEgrPort.setStatus("current")
_MirroredIgrPort_Type = PortList
_MirroredIgrPort_Object = MibScalar
mirroredIgrPort = _MirroredIgrPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 1, 3),
    _MirroredIgrPort_Type()
)
mirroredIgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroredIgrPort.setStatus("current")
_GbnDeviceSwitchPort_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchPort = _GbnDeviceSwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 2)
)
_PortTypeTable_Object = MibTable
portTypeTable = _PortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTypeTable.setStatus("current")
_PortTypeEntry_Object = MibTableRow
portTypeEntry = _PortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 2, 1, 1)
)
portTypeEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    portTypeEntry.setStatus("current")


class _PortNumber_Type(Integer32):
    """Custom type portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_PortNumber_Type.__name__ = "Integer32"
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 2, 1, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("MM_2SC_1310_2", 10),
          ("MM_2SC_850_2", 11),
          ("SM_1SC_1310_20", 13),
          ("SM_1SC_1550_20", 12),
          ("SM_2SC_1310_25", 9),
          ("blank", 1),
          ("double1000FX", 6),
          ("double100FX", 4),
          ("fE", 2),
          ("fE1000", 7),
          ("single1000FX", 5),
          ("single100FX", 3))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 2, 1, 1, 2),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_GbnDeviceSwitchAggregation_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchAggregation = _GbnDeviceSwitchAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3)
)
_AggTable_Object = MibTable
aggTable = _AggTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aggTable.setStatus("obsolete")
_AggEntry_Object = MibTableRow
aggEntry = _AggEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1)
)
aggEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "aggUnit"),
    (0, "GBNDeviceSwitch-MIB", "aggPort"),
)
if mibBuilder.loadTexts:
    aggEntry.setStatus("obsolete")
_AggUnit_Type = Integer32
_AggUnit_Object = MibTableColumn
aggUnit = _AggUnit_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1, 1),
    _AggUnit_Type()
)
aggUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggUnit.setStatus("obsolete")
_AggPort_Type = Integer32
_AggPort_Object = MibTableColumn
aggPort = _AggPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1, 2),
    _AggPort_Type()
)
aggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPort.setStatus("obsolete")
_AggPortListPorts_Type = PortList
_AggPortListPorts_Object = MibTableColumn
aggPortListPorts = _AggPortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1, 3),
    _AggPortListPorts_Type()
)
aggPortListPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggPortListPorts.setStatus("obsolete")


class _AggRule_Type(Integer32):
    """Custom type aggRule based on Integer32"""
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
        *(("destIP", 5),
          ("destMAC", 2),
          ("srcIP", 4),
          ("srcMAC", 1),
          ("srcXORDestIP", 6),
          ("srcXORDestMAC", 3))
    )


_AggRule_Type.__name__ = "Integer32"
_AggRule_Object = MibTableColumn
aggRule = _AggRule_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1, 4),
    _AggRule_Type()
)
aggRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggRule.setStatus("obsolete")
_AggRowstatus_Type = TruthValue
_AggRowstatus_Object = MibTableColumn
aggRowstatus = _AggRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 3, 1, 1, 5),
    _AggRowstatus_Type()
)
aggRowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggRowstatus.setStatus("obsolete")
_GbnDeviceSwitchL3_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchL3 = _GbnDeviceSwitchL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4)
)
_L3Table_Object = MibTable
l3Table = _L3Table_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    l3Table.setStatus("current")
_L3Entry_Object = MibTableRow
l3Entry = _L3Entry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1)
)
l3Entry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "l3IpAddress"),
)
if mibBuilder.loadTexts:
    l3Entry.setStatus("current")
_L3IpAddress_Type = IpAddress
_L3IpAddress_Object = MibTableColumn
l3IpAddress = _L3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 1),
    _L3IpAddress_Type()
)
l3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3IpAddress.setStatus("current")
_L3NextHopMacAddress_Type = MacAddress
_L3NextHopMacAddress_Object = MibTableColumn
l3NextHopMacAddress = _L3NextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 2),
    _L3NextHopMacAddress_Type()
)
l3NextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NextHopMacAddress.setStatus("current")
_L3Vlan_Type = VlanIndex
_L3Vlan_Object = MibTableColumn
l3Vlan = _L3Vlan_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 3),
    _L3Vlan_Type()
)
l3Vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3Vlan.setStatus("current")
_L3Port_Type = Integer32
_L3Port_Object = MibTableColumn
l3Port = _L3Port_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 4),
    _L3Port_Type()
)
l3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3Port.setStatus("current")
_L3CreateTime_Type = DateAndTime
_L3CreateTime_Object = MibTableColumn
l3CreateTime = _L3CreateTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 5),
    _L3CreateTime_Type()
)
l3CreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3CreateTime.setStatus("current")
_L3UpdateTime_Type = DateAndTime
_L3UpdateTime_Object = MibTableColumn
l3UpdateTime = _L3UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 4, 1, 1, 6),
    _L3UpdateTime_Type()
)
l3UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3UpdateTime.setStatus("current")
_GbnDeviceSwitchLoopTest_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchLoopTest = _GbnDeviceSwitchLoopTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 5)
)


class _LoopTestPortno_Type(DisplayString):
    """Custom type loopTestPortno based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_LoopTestPortno_Type.__name__ = "DisplayString"
_LoopTestPortno_Object = MibScalar
loopTestPortno = _LoopTestPortno_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 5, 1),
    _LoopTestPortno_Type()
)
loopTestPortno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopTestPortno.setStatus("current")


class _LoopTestType_Type(Integer32):
    """Custom type loopTestType based on Integer32"""
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
        *(("local", 2),
          ("noop", 1),
          ("other", 4),
          ("remote", 3))
    )


_LoopTestType_Type.__name__ = "Integer32"
_LoopTestType_Object = MibScalar
loopTestType = _LoopTestType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 5, 2),
    _LoopTestType_Type()
)
loopTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopTestType.setStatus("current")


class _LoopTestSuccess_Type(DisplayString):
    """Custom type loopTestSuccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_LoopTestSuccess_Type.__name__ = "DisplayString"
_LoopTestSuccess_Object = MibScalar
loopTestSuccess = _LoopTestSuccess_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 5, 3),
    _LoopTestSuccess_Type()
)
loopTestSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopTestSuccess.setStatus("current")
_GbnDeviceSwitchSRM_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchSRM = _GbnDeviceSwitchSRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 6)
)


class _SrmHardwareEnable_Type(Integer32):
    """Custom type srmHardwareEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SrmHardwareEnable_Type.__name__ = "Integer32"
_SrmHardwareEnable_Object = MibScalar
srmHardwareEnable = _SrmHardwareEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 6, 1),
    _SrmHardwareEnable_Type()
)
srmHardwareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmHardwareEnable.setStatus("current")


class _SrmHardwareDEFCPU_Type(Integer32):
    """Custom type srmHardwareDEFCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SrmHardwareDEFCPU_Type.__name__ = "Integer32"
_SrmHardwareDEFCPU_Object = MibScalar
srmHardwareDEFCPU = _SrmHardwareDEFCPU_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 6, 2),
    _SrmHardwareDEFCPU_Type()
)
srmHardwareDEFCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srmHardwareDEFCPU.setStatus("current")
_GbnDeviceSwitchFlowAlarm_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchFlowAlarm = _GbnDeviceSwitchFlowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7)
)
_PortFlowAlarmTable_Object = MibTable
portFlowAlarmTable = _PortFlowAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    portFlowAlarmTable.setStatus("current")
_PortFlowAlarmEntry_Object = MibTableRow
portFlowAlarmEntry = _PortFlowAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1)
)
portFlowAlarmEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "portFlowAlarmPort"),
)
if mibBuilder.loadTexts:
    portFlowAlarmEntry.setStatus("current")


class _PortFlowAlarmPort_Type(Integer32):
    """Custom type portFlowAlarmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_PortFlowAlarmPort_Type.__name__ = "Integer32"
_PortFlowAlarmPort_Object = MibTableColumn
portFlowAlarmPort = _PortFlowAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1, 1),
    _PortFlowAlarmPort_Type()
)
portFlowAlarmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portFlowAlarmPort.setStatus("current")
_PortFlowAlarmEnable_Type = TruthValue
_PortFlowAlarmEnable_Object = MibTableColumn
portFlowAlarmEnable = _PortFlowAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1, 2),
    _PortFlowAlarmEnable_Type()
)
portFlowAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowAlarmEnable.setStatus("current")
_PortFlowAlarmExceedStatus_Type = TruthValue
_PortFlowAlarmExceedStatus_Object = MibTableColumn
portFlowAlarmExceedStatus = _PortFlowAlarmExceedStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1, 3),
    _PortFlowAlarmExceedStatus_Type()
)
portFlowAlarmExceedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowAlarmExceedStatus.setStatus("current")
_PortFlowAlarmExceedThreshold_Type = Integer32
_PortFlowAlarmExceedThreshold_Object = MibTableColumn
portFlowAlarmExceedThreshold = _PortFlowAlarmExceedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1, 4),
    _PortFlowAlarmExceedThreshold_Type()
)
portFlowAlarmExceedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowAlarmExceedThreshold.setStatus("current")
_PortFlowAlarmNormalThreshold_Type = Integer32
_PortFlowAlarmNormalThreshold_Object = MibTableColumn
portFlowAlarmNormalThreshold = _PortFlowAlarmNormalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 1, 1, 5),
    _PortFlowAlarmNormalThreshold_Type()
)
portFlowAlarmNormalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowAlarmNormalThreshold.setStatus("current")
_PortFlowAlarmGlobalEnable_Type = TruthValue
_PortFlowAlarmGlobalEnable_Object = MibScalar
portFlowAlarmGlobalEnable = _PortFlowAlarmGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 2),
    _PortFlowAlarmGlobalEnable_Type()
)
portFlowAlarmGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowAlarmGlobalEnable.setStatus("current")
_PortFlowAlarmTrap_ObjectIdentity = ObjectIdentity
portFlowAlarmTrap = _PortFlowAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 5)
)
_GbnDeviceSwitchQueneScheduer_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchQueneScheduer = _GbnDeviceSwitchQueneScheduer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8)
)
_QosQueueSchedulerGroup_ObjectIdentity = ObjectIdentity
qosQueueSchedulerGroup = _QosQueueSchedulerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1)
)


class _QosWrrQueue1Weight_Type(Integer32):
    """Custom type qosWrrQueue1Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue1Weight_Type.__name__ = "Integer32"
_QosWrrQueue1Weight_Object = MibScalar
qosWrrQueue1Weight = _QosWrrQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 1),
    _QosWrrQueue1Weight_Type()
)
qosWrrQueue1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue1Weight.setStatus("current")


class _QosWrrQueue2Weight_Type(Integer32):
    """Custom type qosWrrQueue2Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue2Weight_Type.__name__ = "Integer32"
_QosWrrQueue2Weight_Object = MibScalar
qosWrrQueue2Weight = _QosWrrQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 2),
    _QosWrrQueue2Weight_Type()
)
qosWrrQueue2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue2Weight.setStatus("current")


class _QosWrrQueue3Weight_Type(Integer32):
    """Custom type qosWrrQueue3Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue3Weight_Type.__name__ = "Integer32"
_QosWrrQueue3Weight_Object = MibScalar
qosWrrQueue3Weight = _QosWrrQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 3),
    _QosWrrQueue3Weight_Type()
)
qosWrrQueue3Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue3Weight.setStatus("current")


class _QosWrrQueue4Weight_Type(Integer32):
    """Custom type qosWrrQueue4Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue4Weight_Type.__name__ = "Integer32"
_QosWrrQueue4Weight_Object = MibScalar
qosWrrQueue4Weight = _QosWrrQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 4),
    _QosWrrQueue4Weight_Type()
)
qosWrrQueue4Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue4Weight.setStatus("current")


class _QosWrrMaxDelayValue_Type(Integer32):
    """Custom type qosWrrMaxDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosWrrMaxDelayValue_Type.__name__ = "Integer32"
_QosWrrMaxDelayValue_Object = MibScalar
qosWrrMaxDelayValue = _QosWrrMaxDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 5),
    _QosWrrMaxDelayValue_Type()
)
qosWrrMaxDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrMaxDelayValue.setStatus("current")


class _QosQueueSchedulerMode_Type(Integer32):
    """Custom type qosQueueSchedulerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("wrr", 2))
    )


_QosQueueSchedulerMode_Type.__name__ = "Integer32"
_QosQueueSchedulerMode_Object = MibScalar
qosQueueSchedulerMode = _QosQueueSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 6),
    _QosQueueSchedulerMode_Type()
)
qosQueueSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueSchedulerMode.setStatus("current")


class _QosWrrQueue5Weight_Type(Integer32):
    """Custom type qosWrrQueue5Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue5Weight_Type.__name__ = "Integer32"
_QosWrrQueue5Weight_Object = MibScalar
qosWrrQueue5Weight = _QosWrrQueue5Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 7),
    _QosWrrQueue5Weight_Type()
)
qosWrrQueue5Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue5Weight.setStatus("current")


class _QosWrrQueue6Weight_Type(Integer32):
    """Custom type qosWrrQueue6Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue6Weight_Type.__name__ = "Integer32"
_QosWrrQueue6Weight_Object = MibScalar
qosWrrQueue6Weight = _QosWrrQueue6Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 8),
    _QosWrrQueue6Weight_Type()
)
qosWrrQueue6Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue6Weight.setStatus("current")


class _QosWrrQueue7Weight_Type(Integer32):
    """Custom type qosWrrQueue7Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue7Weight_Type.__name__ = "Integer32"
_QosWrrQueue7Weight_Object = MibScalar
qosWrrQueue7Weight = _QosWrrQueue7Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 9),
    _QosWrrQueue7Weight_Type()
)
qosWrrQueue7Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue7Weight.setStatus("current")


class _QosWrrQueue8Weight_Type(Integer32):
    """Custom type qosWrrQueue8Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosWrrQueue8Weight_Type.__name__ = "Integer32"
_QosWrrQueue8Weight_Object = MibScalar
qosWrrQueue8Weight = _QosWrrQueue8Weight_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 1, 10),
    _QosWrrQueue8Weight_Type()
)
qosWrrQueue8Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue8Weight.setStatus("current")
_QosPriorityRemapGroup_ObjectIdentity = ObjectIdentity
qosPriorityRemapGroup = _QosPriorityRemapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2)
)


class _QosPriority0Remap_Type(Integer32):
    """Custom type qosPriority0Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority0Remap_Type.__name__ = "Integer32"
_QosPriority0Remap_Object = MibScalar
qosPriority0Remap = _QosPriority0Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 1),
    _QosPriority0Remap_Type()
)
qosPriority0Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority0Remap.setStatus("current")


class _QosPriority1Remap_Type(Integer32):
    """Custom type qosPriority1Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority1Remap_Type.__name__ = "Integer32"
_QosPriority1Remap_Object = MibScalar
qosPriority1Remap = _QosPriority1Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 2),
    _QosPriority1Remap_Type()
)
qosPriority1Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority1Remap.setStatus("current")


class _QosPriority2Remap_Type(Integer32):
    """Custom type qosPriority2Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority2Remap_Type.__name__ = "Integer32"
_QosPriority2Remap_Object = MibScalar
qosPriority2Remap = _QosPriority2Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 3),
    _QosPriority2Remap_Type()
)
qosPriority2Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority2Remap.setStatus("current")


class _QosPriority3Remap_Type(Integer32):
    """Custom type qosPriority3Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority3Remap_Type.__name__ = "Integer32"
_QosPriority3Remap_Object = MibScalar
qosPriority3Remap = _QosPriority3Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 4),
    _QosPriority3Remap_Type()
)
qosPriority3Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority3Remap.setStatus("current")


class _QosPriority4Remap_Type(Integer32):
    """Custom type qosPriority4Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority4Remap_Type.__name__ = "Integer32"
_QosPriority4Remap_Object = MibScalar
qosPriority4Remap = _QosPriority4Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 5),
    _QosPriority4Remap_Type()
)
qosPriority4Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority4Remap.setStatus("current")


class _QosPriority5Remap_Type(Integer32):
    """Custom type qosPriority5Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority5Remap_Type.__name__ = "Integer32"
_QosPriority5Remap_Object = MibScalar
qosPriority5Remap = _QosPriority5Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 6),
    _QosPriority5Remap_Type()
)
qosPriority5Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority5Remap.setStatus("current")


class _QosPriority6Remap_Type(Integer32):
    """Custom type qosPriority6Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority6Remap_Type.__name__ = "Integer32"
_QosPriority6Remap_Object = MibScalar
qosPriority6Remap = _QosPriority6Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 7),
    _QosPriority6Remap_Type()
)
qosPriority6Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority6Remap.setStatus("current")


class _QosPriority7Remap_Type(Integer32):
    """Custom type qosPriority7Remap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosPriority7Remap_Type.__name__ = "Integer32"
_QosPriority7Remap_Object = MibScalar
qosPriority7Remap = _QosPriority7Remap_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 8),
    _QosPriority7Remap_Type()
)
qosPriority7Remap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriority7Remap.setStatus("current")


class _QosPriorityRemapStatus_Type(Integer32):
    """Custom type qosPriorityRemapStatus based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_QosPriorityRemapStatus_Type.__name__ = "Integer32"
_QosPriorityRemapStatus_Object = MibScalar
qosPriorityRemapStatus = _QosPriorityRemapStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 8, 2, 9),
    _QosPriorityRemapStatus_Type()
)
qosPriorityRemapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityRemapStatus.setStatus("current")
_GbnDeviceSwitchLineRate_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchLineRate = _GbnDeviceSwitchLineRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 9)
)
_QosLineRateTable_Object = MibTable
qosLineRateTable = _QosLineRateTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    qosLineRateTable.setStatus("current")
_QosLineRateEntry_Object = MibTableRow
qosLineRateEntry = _QosLineRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 9, 1, 1)
)
qosLineRateEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "qosLineRateInterface"),
)
if mibBuilder.loadTexts:
    qosLineRateEntry.setStatus("current")


class _QosLineRateInterface_Type(Integer32):
    """Custom type qosLineRateInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_QosLineRateInterface_Type.__name__ = "Integer32"
_QosLineRateInterface_Object = MibTableColumn
qosLineRateInterface = _QosLineRateInterface_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 9, 1, 1, 1),
    _QosLineRateInterface_Type()
)
qosLineRateInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLineRateInterface.setStatus("current")


class _QosLineRateTargetRate_Type(Integer32):
    """Custom type qosLineRateTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosLineRateTargetRate_Type.__name__ = "Integer32"
_QosLineRateTargetRate_Object = MibTableColumn
qosLineRateTargetRate = _QosLineRateTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 9, 1, 1, 2),
    _QosLineRateTargetRate_Type()
)
qosLineRateTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosLineRateTargetRate.setStatus("current")
_GbnDeviceSwitchPortIsolation_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchPortIsolation = _GbnDeviceSwitchPortIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 10)
)
_PortIsolationGroup_ObjectIdentity = ObjectIdentity
portIsolationGroup = _PortIsolationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 10, 1)
)
_PortIsolationDownLinkPorts_Type = PortList
_PortIsolationDownLinkPorts_Object = MibScalar
portIsolationDownLinkPorts = _PortIsolationDownLinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 10, 1, 1),
    _PortIsolationDownLinkPorts_Type()
)
portIsolationDownLinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIsolationDownLinkPorts.setStatus("current")
_GbnDeviceSwitchStormControl_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchStormControl = _GbnDeviceSwitchStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11)
)
_StormControlTable_Object = MibTable
stormControlTable = _StormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    stormControlTable.setStatus("current")
_StormControlEntry_Object = MibTableRow
stormControlEntry = _StormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1, 1)
)
stormControlEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "stormControlInterface"),
    (0, "GBNDeviceSwitch-MIB", "stormControlType"),
)
if mibBuilder.loadTexts:
    stormControlEntry.setStatus("current")


class _StormControlInterface_Type(Integer32):
    """Custom type stormControlInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_StormControlInterface_Type.__name__ = "Integer32"
_StormControlInterface_Object = MibTableColumn
stormControlInterface = _StormControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1, 1, 1),
    _StormControlInterface_Type()
)
stormControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormControlInterface.setStatus("current")
_StormControlType_Type = Integer32
_StormControlType_Object = MibTableColumn
stormControlType = _StormControlType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1, 1, 2),
    _StormControlType_Type()
)
stormControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormControlType.setStatus("current")


class _StormControlTargetRate_Type(Integer32):
    """Custom type stormControlTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_StormControlTargetRate_Type.__name__ = "Integer32"
_StormControlTargetRate_Object = MibTableColumn
stormControlTargetRate = _StormControlTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1, 1, 3),
    _StormControlTargetRate_Type()
)
stormControlTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormControlTargetRate.setStatus("current")
_StormControlRowStatus_Type = RowStatus
_StormControlRowStatus_Object = MibTableColumn
stormControlRowStatus = _StormControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 11, 1, 1, 4),
    _StormControlRowStatus_Type()
)
stormControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormControlRowStatus.setStatus("current")
_GbnDeviceSwitchBandWidth_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchBandWidth = _GbnDeviceSwitchBandWidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12)
)
_BandwidthcontrolTable_Object = MibTable
bandwidthcontrolTable = _BandwidthcontrolTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    bandwidthcontrolTable.setStatus("current")
_BandwidthcontrolEntry_Object = MibTableRow
bandwidthcontrolEntry = _BandwidthcontrolEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12, 1, 1)
)
bandwidthcontrolEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "controlPort"),
)
if mibBuilder.loadTexts:
    bandwidthcontrolEntry.setStatus("current")


class _ControlPort_Type(Integer32):
    """Custom type controlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_ControlPort_Type.__name__ = "Integer32"
_ControlPort_Object = MibTableColumn
controlPort = _ControlPort_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12, 1, 1, 1),
    _ControlPort_Type()
)
controlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlPort.setStatus("current")


class _PortEgressBandwidthcontrol_Type(Integer32):
    """Custom type portEgressBandwidthcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_PortEgressBandwidthcontrol_Type.__name__ = "Integer32"
_PortEgressBandwidthcontrol_Object = MibTableColumn
portEgressBandwidthcontrol = _PortEgressBandwidthcontrol_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12, 1, 1, 2),
    _PortEgressBandwidthcontrol_Type()
)
portEgressBandwidthcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgressBandwidthcontrol.setStatus("current")


class _PortIngressBandwidthcontrol_Type(Integer32):
    """Custom type portIngressBandwidthcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_PortIngressBandwidthcontrol_Type.__name__ = "Integer32"
_PortIngressBandwidthcontrol_Object = MibTableColumn
portIngressBandwidthcontrol = _PortIngressBandwidthcontrol_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 12, 1, 1, 3),
    _PortIngressBandwidthcontrol_Type()
)
portIngressBandwidthcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIngressBandwidthcontrol.setStatus("current")
_GbnDeviceSwitchNewStormControl_ObjectIdentity = ObjectIdentity
gbnDeviceSwitchNewStormControl = _GbnDeviceSwitchNewStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13)
)


class _NewStormControlType_Type(Integer32):
    """Custom type newStormControlType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("broadcast_dlf", 5),
          ("broadcast_ipmulticast", 3),
          ("broadcast_ipmulticast_dlf", 7),
          ("dlf", 4),
          ("ipmulticast", 2),
          ("ipmulticast_dlf", 6),
          ("none", 0))
    )


_NewStormControlType_Type.__name__ = "Integer32"
_NewStormControlType_Object = MibScalar
newStormControlType = _NewStormControlType_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 1),
    _NewStormControlType_Type()
)
newStormControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newStormControlType.setStatus("current")


class _NewStormControlTargetRate_Type(Integer32):
    """Custom type newStormControlTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              12,
              25,
              50)
        )
    )
    namedValues = NamedValues(
        *(("rate_one_eighth", 12),
          ("rate_one_fourth", 25),
          ("rate_one_half", 50),
          ("rate_one_sixteenth", 6))
    )


_NewStormControlTargetRate_Type.__name__ = "Integer32"
_NewStormControlTargetRate_Object = MibScalar
newStormControlTargetRate = _NewStormControlTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 2),
    _NewStormControlTargetRate_Type()
)
newStormControlTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newStormControlTargetRate.setStatus("current")
_NewStormControlTable_Object = MibTable
newStormControlTable = _NewStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 3)
)
if mibBuilder.loadTexts:
    newStormControlTable.setStatus("current")
_NewStormControlEntry_Object = MibTableRow
newStormControlEntry = _NewStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 3, 1)
)
newStormControlEntry.setIndexNames(
    (0, "GBNDeviceSwitch-MIB", "newStormControlInterface"),
)
if mibBuilder.loadTexts:
    newStormControlEntry.setStatus("current")


class _NewStormControlInterface_Type(Integer32):
    """Custom type newStormControlInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_NewStormControlInterface_Type.__name__ = "Integer32"
_NewStormControlInterface_Object = MibTableColumn
newStormControlInterface = _NewStormControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 3, 1, 1),
    _NewStormControlInterface_Type()
)
newStormControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newStormControlInterface.setStatus("current")


class _NewStormControlStatus_Type(Integer32):
    """Custom type newStormControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NewStormControlStatus_Type.__name__ = "Integer32"
_NewStormControlStatus_Object = MibTableColumn
newStormControlStatus = _NewStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 13, 3, 1, 2),
    _NewStormControlStatus_Type()
)
newStormControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newStormControlStatus.setStatus("current")

# Managed Objects groups


# Notification objects

portFlowAlarmExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 5, 1)
)
portFlowAlarmExceedTrap.setObjects(
    ("GBNDeviceSwitch-MIB", "portFlowAlarmPort")
)
if mibBuilder.loadTexts:
    portFlowAlarmExceedTrap.setStatus(
        "current"
    )

portFlowAlarmNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 2, 1, 7, 5, 2)
)
portFlowAlarmNormalTrap.setObjects(
    ("GBNDeviceSwitch-MIB", "portFlowAlarmPort")
)
if mibBuilder.loadTexts:
    portFlowAlarmNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNDeviceSwitch-MIB",
    **{"gbnDeviceSwitch": gbnDeviceSwitch,
       "gbnDeviceSwitchMirror": gbnDeviceSwitchMirror,
       "mirroringPort": mirroringPort,
       "mirroredEgrPort": mirroredEgrPort,
       "mirroredIgrPort": mirroredIgrPort,
       "gbnDeviceSwitchPort": gbnDeviceSwitchPort,
       "portTypeTable": portTypeTable,
       "portTypeEntry": portTypeEntry,
       "portNumber": portNumber,
       "portType": portType,
       "gbnDeviceSwitchAggregation": gbnDeviceSwitchAggregation,
       "aggTable": aggTable,
       "aggEntry": aggEntry,
       "aggUnit": aggUnit,
       "aggPort": aggPort,
       "aggPortListPorts": aggPortListPorts,
       "aggRule": aggRule,
       "aggRowstatus": aggRowstatus,
       "gbnDeviceSwitchL3": gbnDeviceSwitchL3,
       "l3Table": l3Table,
       "l3Entry": l3Entry,
       "l3IpAddress": l3IpAddress,
       "l3NextHopMacAddress": l3NextHopMacAddress,
       "l3Vlan": l3Vlan,
       "l3Port": l3Port,
       "l3CreateTime": l3CreateTime,
       "l3UpdateTime": l3UpdateTime,
       "gbnDeviceSwitchLoopTest": gbnDeviceSwitchLoopTest,
       "loopTestPortno": loopTestPortno,
       "loopTestType": loopTestType,
       "loopTestSuccess": loopTestSuccess,
       "gbnDeviceSwitchSRM": gbnDeviceSwitchSRM,
       "srmHardwareEnable": srmHardwareEnable,
       "srmHardwareDEFCPU": srmHardwareDEFCPU,
       "gbnDeviceSwitchFlowAlarm": gbnDeviceSwitchFlowAlarm,
       "portFlowAlarmTable": portFlowAlarmTable,
       "portFlowAlarmEntry": portFlowAlarmEntry,
       "portFlowAlarmPort": portFlowAlarmPort,
       "portFlowAlarmEnable": portFlowAlarmEnable,
       "portFlowAlarmExceedStatus": portFlowAlarmExceedStatus,
       "portFlowAlarmExceedThreshold": portFlowAlarmExceedThreshold,
       "portFlowAlarmNormalThreshold": portFlowAlarmNormalThreshold,
       "portFlowAlarmGlobalEnable": portFlowAlarmGlobalEnable,
       "portFlowAlarmTrap": portFlowAlarmTrap,
       "portFlowAlarmExceedTrap": portFlowAlarmExceedTrap,
       "portFlowAlarmNormalTrap": portFlowAlarmNormalTrap,
       "gbnDeviceSwitchQueneScheduer": gbnDeviceSwitchQueneScheduer,
       "qosQueueSchedulerGroup": qosQueueSchedulerGroup,
       "qosWrrQueue1Weight": qosWrrQueue1Weight,
       "qosWrrQueue2Weight": qosWrrQueue2Weight,
       "qosWrrQueue3Weight": qosWrrQueue3Weight,
       "qosWrrQueue4Weight": qosWrrQueue4Weight,
       "qosWrrMaxDelayValue": qosWrrMaxDelayValue,
       "qosQueueSchedulerMode": qosQueueSchedulerMode,
       "qosWrrQueue5Weight": qosWrrQueue5Weight,
       "qosWrrQueue6Weight": qosWrrQueue6Weight,
       "qosWrrQueue7Weight": qosWrrQueue7Weight,
       "qosWrrQueue8Weight": qosWrrQueue8Weight,
       "qosPriorityRemapGroup": qosPriorityRemapGroup,
       "qosPriority0Remap": qosPriority0Remap,
       "qosPriority1Remap": qosPriority1Remap,
       "qosPriority2Remap": qosPriority2Remap,
       "qosPriority3Remap": qosPriority3Remap,
       "qosPriority4Remap": qosPriority4Remap,
       "qosPriority5Remap": qosPriority5Remap,
       "qosPriority6Remap": qosPriority6Remap,
       "qosPriority7Remap": qosPriority7Remap,
       "qosPriorityRemapStatus": qosPriorityRemapStatus,
       "gbnDeviceSwitchLineRate": gbnDeviceSwitchLineRate,
       "qosLineRateTable": qosLineRateTable,
       "qosLineRateEntry": qosLineRateEntry,
       "qosLineRateInterface": qosLineRateInterface,
       "qosLineRateTargetRate": qosLineRateTargetRate,
       "gbnDeviceSwitchPortIsolation": gbnDeviceSwitchPortIsolation,
       "portIsolationGroup": portIsolationGroup,
       "portIsolationDownLinkPorts": portIsolationDownLinkPorts,
       "gbnDeviceSwitchStormControl": gbnDeviceSwitchStormControl,
       "stormControlTable": stormControlTable,
       "stormControlEntry": stormControlEntry,
       "stormControlInterface": stormControlInterface,
       "stormControlType": stormControlType,
       "stormControlTargetRate": stormControlTargetRate,
       "stormControlRowStatus": stormControlRowStatus,
       "gbnDeviceSwitchBandWidth": gbnDeviceSwitchBandWidth,
       "bandwidthcontrolTable": bandwidthcontrolTable,
       "bandwidthcontrolEntry": bandwidthcontrolEntry,
       "controlPort": controlPort,
       "portEgressBandwidthcontrol": portEgressBandwidthcontrol,
       "portIngressBandwidthcontrol": portIngressBandwidthcontrol,
       "gbnDeviceSwitchNewStormControl": gbnDeviceSwitchNewStormControl,
       "newStormControlType": newStormControlType,
       "newStormControlTargetRate": newStormControlTargetRate,
       "newStormControlTable": newStormControlTable,
       "newStormControlEntry": newStormControlEntry,
       "newStormControlInterface": newStormControlInterface,
       "newStormControlStatus": newStormControlStatus}
)
