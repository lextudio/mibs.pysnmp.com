# SNMP MIB module (FD-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:27 2024
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

(DeviceOperation,
 DeviceStatus,
 DeviceType,
 LedStatus,
 epon) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "DeviceOperation",
    "DeviceStatus",
    "DeviceType",
    "LedStatus",
    "epon")

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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

systemInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysBaseInfo_ObjectIdentity = ObjectIdentity
sysBaseInfo = _SysBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1)
)
_SysModel_Type = DeviceType
_SysModel_Object = MibScalar
sysModel = _SysModel_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 1),
    _SysModel_Type()
)
sysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModel.setStatus("current")
_SysDesc_Type = DisplayString
_SysDesc_Object = MibScalar
sysDesc = _SysDesc_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 2),
    _SysDesc_Type()
)
sysDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDesc.setStatus("current")
_SysLocation_Type = DisplayString
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 3),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_SysContact_Type = DisplayString
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")
_SysMajAlarmLed_Type = LedStatus
_SysMajAlarmLed_Object = MibScalar
sysMajAlarmLed = _SysMajAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 5),
    _SysMajAlarmLed_Type()
)
sysMajAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMajAlarmLed.setStatus("current")
_SysCriAlarmLed_Type = LedStatus
_SysCriAlarmLed_Object = MibScalar
sysCriAlarmLed = _SysCriAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 6),
    _SysCriAlarmLed_Type()
)
sysCriAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCriAlarmLed.setStatus("current")
_SysAlarmDesc_Type = DisplayString
_SysAlarmDesc_Object = MibScalar
sysAlarmDesc = _SysAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 1, 7),
    _SysAlarmDesc_Type()
)
sysAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmDesc.setStatus("current")
_SysConfig_ObjectIdentity = ObjectIdentity
sysConfig = _SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2)
)


class _ConsolePortSpd_Type(Integer32):
    """Custom type consolePortSpd based on Integer32"""
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
        *(("bps115200", 7),
          ("bps19200", 4),
          ("bps2400", 1),
          ("bps38400", 5),
          ("bps4800", 2),
          ("bps57600", 6),
          ("bps9600", 3))
    )


_ConsolePortSpd_Type.__name__ = "Integer32"
_ConsolePortSpd_Object = MibScalar
consolePortSpd = _ConsolePortSpd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 1),
    _ConsolePortSpd_Type()
)
consolePortSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolePortSpd.setStatus("current")
_ManageIpAddr_Type = IpAddress
_ManageIpAddr_Object = MibScalar
manageIpAddr = _ManageIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 2),
    _ManageIpAddr_Type()
)
manageIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageIpAddr.setStatus("current")
_ManageNetMask_Type = IpAddress
_ManageNetMask_Object = MibScalar
manageNetMask = _ManageNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 3),
    _ManageNetMask_Type()
)
manageNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageNetMask.setStatus("current")
_ManageGateway_Type = IpAddress
_ManageGateway_Object = MibScalar
manageGateway = _ManageGateway_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 4),
    _ManageGateway_Type()
)
manageGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageGateway.setStatus("current")
_SnmpReadCommunity_Type = DisplayString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 5),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")
_SnmpRWCommunity_Type = DisplayString
_SnmpRWCommunity_Object = MibScalar
snmpRWCommunity = _SnmpRWCommunity_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 6),
    _SnmpRWCommunity_Type()
)
snmpRWCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRWCommunity.setStatus("current")
_TrapDstIpAddr1_Type = IpAddress
_TrapDstIpAddr1_Object = MibScalar
trapDstIpAddr1 = _TrapDstIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 8),
    _TrapDstIpAddr1_Type()
)
trapDstIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDstIpAddr1.setStatus("current")
_TrapDstIpAddr2_Type = IpAddress
_TrapDstIpAddr2_Object = MibScalar
trapDstIpAddr2 = _TrapDstIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 9),
    _TrapDstIpAddr2_Type()
)
trapDstIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDstIpAddr2.setStatus("current")
_TrapDstIpAddr3_Type = IpAddress
_TrapDstIpAddr3_Object = MibScalar
trapDstIpAddr3 = _TrapDstIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 10),
    _TrapDstIpAddr3_Type()
)
trapDstIpAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDstIpAddr3.setStatus("current")
_TrapDstIpAddr4_Type = IpAddress
_TrapDstIpAddr4_Object = MibScalar
trapDstIpAddr4 = _TrapDstIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 11),
    _TrapDstIpAddr4_Type()
)
trapDstIpAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDstIpAddr4.setStatus("current")
_SysOperate_Type = DeviceOperation
_SysOperate_Object = MibScalar
sysOperate = _SysOperate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 2, 12),
    _SysOperate_Type()
)
sysOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOperate.setStatus("current")
_ChassisInfo_ObjectIdentity = ObjectIdentity
chassisInfo = _ChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3)
)
_ChassisType_Type = DeviceType
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("current")


class _ChassisFactorySerial_Type(OctetString):
    """Custom type chassisFactorySerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ChassisFactorySerial_Type.__name__ = "OctetString"
_ChassisFactorySerial_Object = MibScalar
chassisFactorySerial = _ChassisFactorySerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 2),
    _ChassisFactorySerial_Type()
)
chassisFactorySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFactorySerial.setStatus("current")
_ChassisRevision_Type = DisplayString
_ChassisRevision_Object = MibScalar
chassisRevision = _ChassisRevision_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 3),
    _ChassisRevision_Type()
)
chassisRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisRevision.setStatus("current")
_ChassisTemperature_Type = Unsigned32
_ChassisTemperature_Object = MibScalar
chassisTemperature = _ChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 4),
    _ChassisTemperature_Type()
)
chassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperature.setStatus("current")
_PowerStatusBit_Type = Unsigned32
_PowerStatusBit_Object = MibScalar
powerStatusBit = _PowerStatusBit_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 5),
    _PowerStatusBit_Type()
)
powerStatusBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatusBit.setStatus("current")
_FanStatusBit_Type = Unsigned32
_FanStatusBit_Object = MibScalar
fanStatusBit = _FanStatusBit_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 3, 6),
    _FanStatusBit_Type()
)
fanStatusBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatusBit.setStatus("current")
_CardModule_ObjectIdentity = ObjectIdentity
cardModule = _CardModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5)
)
_MainCard_ObjectIdentity = ObjectIdentity
mainCard = _MainCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1)
)
_MainCardType_Type = DeviceType
_MainCardType_Object = MibScalar
mainCardType = _MainCardType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 1),
    _MainCardType_Type()
)
mainCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardType.setStatus("current")


class _MainCardFactorySerial_Type(OctetString):
    """Custom type mainCardFactorySerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MainCardFactorySerial_Type.__name__ = "OctetString"
_MainCardFactorySerial_Object = MibScalar
mainCardFactorySerial = _MainCardFactorySerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 2),
    _MainCardFactorySerial_Type()
)
mainCardFactorySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardFactorySerial.setStatus("current")
_MainCardHWRevision_Type = DisplayString
_MainCardHWRevision_Object = MibScalar
mainCardHWRevision = _MainCardHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 3),
    _MainCardHWRevision_Type()
)
mainCardHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardHWRevision.setStatus("current")
_MainCardSWVersion_Type = DisplayString
_MainCardSWVersion_Object = MibScalar
mainCardSWVersion = _MainCardSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 4),
    _MainCardSWVersion_Type()
)
mainCardSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardSWVersion.setStatus("current")
_MainCardRunningStatus_Type = DeviceStatus
_MainCardRunningStatus_Object = MibScalar
mainCardRunningStatus = _MainCardRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 5),
    _MainCardRunningStatus_Type()
)
mainCardRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardRunningStatus.setStatus("current")
_MainCardRunningTime_Type = TimeTicks
_MainCardRunningTime_Object = MibScalar
mainCardRunningTime = _MainCardRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 6),
    _MainCardRunningTime_Type()
)
mainCardRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardRunningTime.setStatus("current")
_MainCardOperate_Type = DeviceOperation
_MainCardOperate_Object = MibScalar
mainCardOperate = _MainCardOperate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 1, 7),
    _MainCardOperate_Type()
)
mainCardOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainCardOperate.setStatus("current")
_PonCard_ObjectIdentity = ObjectIdentity
ponCard = _PonCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2)
)
_PonCardTable_Object = MibTable
ponCardTable = _PonCardTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ponCardTable.setStatus("current")
_PonCardEntry_Object = MibTableRow
ponCardEntry = _PonCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1)
)
ponCardEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
)
if mibBuilder.loadTexts:
    ponCardEntry.setStatus("current")


class _PonCardSlotId_Type(Integer32):
    """Custom type ponCardSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PonCardSlotId_Type.__name__ = "Integer32"
_PonCardSlotId_Object = MibTableColumn
ponCardSlotId = _PonCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 1),
    _PonCardSlotId_Type()
)
ponCardSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponCardSlotId.setStatus("current")
_PonCardType_Type = DeviceType
_PonCardType_Object = MibTableColumn
ponCardType = _PonCardType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 2),
    _PonCardType_Type()
)
ponCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardType.setStatus("current")


class _PonCardFactorySerial_Type(OctetString):
    """Custom type ponCardFactorySerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PonCardFactorySerial_Type.__name__ = "OctetString"
_PonCardFactorySerial_Object = MibTableColumn
ponCardFactorySerial = _PonCardFactorySerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 3),
    _PonCardFactorySerial_Type()
)
ponCardFactorySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardFactorySerial.setStatus("current")
_PonCardHwRev_Type = DisplayString
_PonCardHwRev_Object = MibTableColumn
ponCardHwRev = _PonCardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 4),
    _PonCardHwRev_Type()
)
ponCardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardHwRev.setStatus("current")
_PonCardFwVer_Type = DisplayString
_PonCardFwVer_Object = MibTableColumn
ponCardFwVer = _PonCardFwVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 5),
    _PonCardFwVer_Type()
)
ponCardFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardFwVer.setStatus("current")
_PonCardRunningStatus_Type = DeviceStatus
_PonCardRunningStatus_Object = MibTableColumn
ponCardRunningStatus = _PonCardRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 7),
    _PonCardRunningStatus_Type()
)
ponCardRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardRunningStatus.setStatus("current")
_PonCardRuningTime_Type = TimeTicks
_PonCardRuningTime_Object = MibTableColumn
ponCardRuningTime = _PonCardRuningTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 8),
    _PonCardRuningTime_Type()
)
ponCardRuningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardRuningTime.setStatus("current")
_PonCardOperate_Type = DeviceOperation
_PonCardOperate_Object = MibTableColumn
ponCardOperate = _PonCardOperate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 9),
    _PonCardOperate_Type()
)
ponCardOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponCardOperate.setStatus("current")


class _PonCardUpgradeStat_Type(Integer32):
    """Custom type ponCardUpgradeStat based on Integer32"""
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
        *(("booting", 1),
          ("normalRun", 2),
          ("rcvFileErr", 5),
          ("rcvFileIng", 3),
          ("rcvFileOk", 4),
          ("upgradeErr", 8),
          ("upgradeOk", 7),
          ("upgradeOlt", 9),
          ("upgradeOnu", 10),
          ("upgrading", 6))
    )


_PonCardUpgradeStat_Type.__name__ = "Integer32"
_PonCardUpgradeStat_Object = MibTableColumn
ponCardUpgradeStat = _PonCardUpgradeStat_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 5, 2, 1, 1, 10),
    _PonCardUpgradeStat_Type()
)
ponCardUpgradeStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponCardUpgradeStat.setStatus("current")
_OnuAuth_ObjectIdentity = ObjectIdentity
onuAuth = _OnuAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6)
)


class _AuthMethod_Type(Integer32):
    """Custom type authMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackList", 1),
          ("none", 3),
          ("whiteList", 2))
    )


_AuthMethod_Type.__name__ = "Integer32"
_AuthMethod_Object = MibScalar
authMethod = _AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 1),
    _AuthMethod_Type()
)
authMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMethod.setStatus("current")


class _NonAuthOper_Type(Integer32):
    """Custom type nonAuthOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("clearNonAuthMacList", 2)
    )


_NonAuthOper_Type.__name__ = "Integer32"
_NonAuthOper_Object = MibScalar
nonAuthOper = _NonAuthOper_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 2),
    _NonAuthOper_Type()
)
nonAuthOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonAuthOper.setStatus("current")
_OnuAuthMacCfgTable_Object = MibTable
onuAuthMacCfgTable = _OnuAuthMacCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    onuAuthMacCfgTable.setStatus("current")
_OnuAuthMacCfgEntry_Object = MibTableRow
onuAuthMacCfgEntry = _OnuAuthMacCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1)
)
onuAuthMacCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "authMacEntryId"),
)
if mibBuilder.loadTexts:
    onuAuthMacCfgEntry.setStatus("current")
_AuthMacEntryId_Type = Unsigned32
_AuthMacEntryId_Object = MibTableColumn
authMacEntryId = _AuthMacEntryId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1, 1),
    _AuthMacEntryId_Type()
)
authMacEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authMacEntryId.setStatus("current")
_BeginMacAddr_Type = MacAddress
_BeginMacAddr_Object = MibTableColumn
beginMacAddr = _BeginMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1, 2),
    _BeginMacAddr_Type()
)
beginMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    beginMacAddr.setStatus("current")
_EndMacAddr_Type = MacAddress
_EndMacAddr_Object = MibTableColumn
endMacAddr = _EndMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1, 3),
    _EndMacAddr_Type()
)
endMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    endMacAddr.setStatus("current")


class _MacAttr_Type(Integer32):
    """Custom type macAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackMac", 1),
          ("obsolete", 3),
          ("whiteMac", 2))
    )


_MacAttr_Type.__name__ = "Integer32"
_MacAttr_Object = MibTableColumn
macAttr = _MacAttr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1, 4),
    _MacAttr_Type()
)
macAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAttr.setStatus("current")
_OnuAuthMacRowStatus_Type = RowStatus
_OnuAuthMacRowStatus_Object = MibTableColumn
onuAuthMacRowStatus = _OnuAuthMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 3, 1, 5),
    _OnuAuthMacRowStatus_Type()
)
onuAuthMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthMacRowStatus.setStatus("current")
_NonAuthOnuListTable_Object = MibTable
nonAuthOnuListTable = _NonAuthOnuListTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    nonAuthOnuListTable.setStatus("current")
_NonAuthOnuListEntry_Object = MibTableRow
nonAuthOnuListEntry = _NonAuthOnuListEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 4, 1)
)
nonAuthOnuListEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "nonAuthOnuMacIndex"),
)
if mibBuilder.loadTexts:
    nonAuthOnuListEntry.setStatus("current")
_NonAuthOnuMacIndex_Type = Unsigned32
_NonAuthOnuMacIndex_Object = MibTableColumn
nonAuthOnuMacIndex = _NonAuthOnuMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 4, 1, 1),
    _NonAuthOnuMacIndex_Type()
)
nonAuthOnuMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nonAuthOnuMacIndex.setStatus("current")
_NonAuthOnuMac_Type = MacAddress
_NonAuthOnuMac_Object = MibTableColumn
nonAuthOnuMac = _NonAuthOnuMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 4, 1, 2),
    _NonAuthOnuMac_Type()
)
nonAuthOnuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nonAuthOnuMac.setStatus("current")
_NonAuthOnuTries_Type = Unsigned32
_NonAuthOnuTries_Object = MibTableColumn
nonAuthOnuTries = _NonAuthOnuTries_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 6, 4, 1, 3),
    _NonAuthOnuTries_Type()
)
nonAuthOnuTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nonAuthOnuTries.setStatus("current")
_UserManage_ObjectIdentity = ObjectIdentity
userManage = _UserManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7)
)
_UserManageTable_Object = MibTable
userManageTable = _UserManageTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    userManageTable.setStatus("current")
_UserManageEntry_Object = MibTableRow
userManageEntry = _UserManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1)
)
userManageEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "userId"),
)
if mibBuilder.loadTexts:
    userManageEntry.setStatus("current")


class _UserId_Type(Integer32):
    """Custom type userId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UserId_Type.__name__ = "Integer32"
_UserId_Object = MibTableColumn
userId = _UserId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 1),
    _UserId_Type()
)
userId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userId.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserPassword_Type(OctetString):
    """Custom type userPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserPassword_Type.__name__ = "OctetString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 3),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_UserPermission_Type = Unsigned32
_UserPermission_Object = MibTableColumn
userPermission = _UserPermission_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 4),
    _UserPermission_Type()
)
userPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPermission.setStatus("current")
_UserAccessDeviceMap_Type = Unsigned32
_UserAccessDeviceMap_Object = MibTableColumn
userAccessDeviceMap = _UserAccessDeviceMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 5),
    _UserAccessDeviceMap_Type()
)
userAccessDeviceMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAccessDeviceMap.setStatus("current")


class _LoginTimeout_Type(Unsigned32):
    """Custom type loginTimeout based on Unsigned32"""
    defaultValue = 300


_LoginTimeout_Object = MibTableColumn
loginTimeout = _LoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 6),
    _LoginTimeout_Type()
)
loginTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginTimeout.setStatus("current")
_UserEntryRowStatus_Type = RowStatus
_UserEntryRowStatus_Object = MibTableColumn
userEntryRowStatus = _UserEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 7, 1, 1, 7),
    _UserEntryRowStatus_Type()
)
userEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userEntryRowStatus.setStatus("current")
_Upgrade_ObjectIdentity = ObjectIdentity
upgrade = _Upgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8)
)


class _FtpServerIp_Type(DisplayString):
    """Custom type ftpServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FtpServerIp_Type.__name__ = "DisplayString"
_FtpServerIp_Object = MibScalar
ftpServerIp = _FtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 1),
    _FtpServerIp_Type()
)
ftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerIp.setStatus("current")


class _FtpServerUserName_Type(DisplayString):
    """Custom type ftpServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FtpServerUserName_Type.__name__ = "DisplayString"
_FtpServerUserName_Object = MibScalar
ftpServerUserName = _FtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 2),
    _FtpServerUserName_Type()
)
ftpServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerUserName.setStatus("current")


class _FtpServerUserPasswd_Type(DisplayString):
    """Custom type ftpServerUserPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FtpServerUserPasswd_Type.__name__ = "DisplayString"
_FtpServerUserPasswd_Object = MibScalar
ftpServerUserPasswd = _FtpServerUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 3),
    _FtpServerUserPasswd_Type()
)
ftpServerUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpServerUserPasswd.setStatus("current")


class _FtpOperFileName_Type(DisplayString):
    """Custom type ftpOperFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FtpOperFileName_Type.__name__ = "DisplayString"
_FtpOperFileName_Object = MibScalar
ftpOperFileName = _FtpOperFileName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 4),
    _FtpOperFileName_Type()
)
ftpOperFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpOperFileName.setStatus("current")


class _FtpOperTarget_Type(Integer32):
    """Custom type ftpOperTarget based on Integer32"""
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
        *(("ctrlCardImage", 1),
          ("oltApp", 3),
          ("oltBoot", 5),
          ("oltPers", 4),
          ("onuApp", 6),
          ("onuBoot", 8),
          ("onuPers", 7),
          ("otherSpecifiedFile", 9),
          ("ponCardImage", 2))
    )


_FtpOperTarget_Type.__name__ = "Integer32"
_FtpOperTarget_Object = MibScalar
ftpOperTarget = _FtpOperTarget_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 6),
    _FtpOperTarget_Type()
)
ftpOperTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpOperTarget.setStatus("current")


class _DwLoadFileCrcCheck_Type(Integer32):
    """Custom type dwLoadFileCrcCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkCrc", 1),
          ("dontCheckCrc", 2))
    )


_DwLoadFileCrcCheck_Type.__name__ = "Integer32"
_DwLoadFileCrcCheck_Object = MibScalar
dwLoadFileCrcCheck = _DwLoadFileCrcCheck_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 7),
    _DwLoadFileCrcCheck_Type()
)
dwLoadFileCrcCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwLoadFileCrcCheck.setStatus("current")
_DwLoadFileCrcValue_Type = Unsigned32
_DwLoadFileCrcValue_Object = MibScalar
dwLoadFileCrcValue = _DwLoadFileCrcValue_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 8),
    _DwLoadFileCrcValue_Type()
)
dwLoadFileCrcValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwLoadFileCrcValue.setStatus("current")


class _OperDeviceMap_Type(OctetString):
    """Custom type operDeviceMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_OperDeviceMap_Type.__name__ = "OctetString"
_OperDeviceMap_Object = MibScalar
operDeviceMap = _OperDeviceMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 9),
    _OperDeviceMap_Type()
)
operDeviceMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operDeviceMap.setStatus("current")


class _UpgradeStatus_Type(Integer32):
    """Custom type upgradeStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("initFtpErr", 2),
          ("paraErr", 1),
          ("transmitErr", 4),
          ("transmitOk", 5),
          ("transmitting", 3),
          ("upgradeErr", 7),
          ("upgradeOk", 8),
          ("upgrading", 6),
          ("uploadErr", 10),
          ("uploadOk", 11),
          ("uploading", 9))
    )


_UpgradeStatus_Type.__name__ = "Integer32"
_UpgradeStatus_Object = MibScalar
upgradeStatus = _UpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 10),
    _UpgradeStatus_Type()
)
upgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeStatus.setStatus("current")


class _UpgradeOperation_Type(Integer32):
    """Custom type upgradeOperation based on Integer32"""
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
        *(("downloadFile", 1),
          ("reboot", 3),
          ("upgrade", 2),
          ("uploadFile", 4))
    )


_UpgradeOperation_Type.__name__ = "Integer32"
_UpgradeOperation_Object = MibScalar
upgradeOperation = _UpgradeOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 11),
    _UpgradeOperation_Type()
)
upgradeOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeOperation.setStatus("current")
_FtpProgress_Type = Integer32
_FtpProgress_Object = MibScalar
ftpProgress = _FtpProgress_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 8, 12),
    _FtpProgress_Type()
)
ftpProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpProgress.setStatus("current")
if mibBuilder.loadTexts:
    ftpProgress.setUnits("percent")
_FdSysConformance_ObjectIdentity = ObjectIdentity
fdSysConformance = _FdSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13)
)
_FdSystemGroups_ObjectIdentity = ObjectIdentity
fdSystemGroups = _FdSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1)
)
_FdSystemCompliances_ObjectIdentity = ObjectIdentity
fdSystemCompliances = _FdSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 2)
)

# Managed Objects groups

sysBaseManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 1)
)
sysBaseManageGroup.setObjects(
      *(("FD-SYSTEM-MIB", "sysModel"),
        ("FD-SYSTEM-MIB", "sysDesc"),
        ("FD-SYSTEM-MIB", "sysLocation"),
        ("FD-SYSTEM-MIB", "sysContact"),
        ("FD-SYSTEM-MIB", "sysMajAlarmLed"),
        ("FD-SYSTEM-MIB", "sysCriAlarmLed"),
        ("FD-SYSTEM-MIB", "sysAlarmDesc"),
        ("FD-SYSTEM-MIB", "consolePortSpd"),
        ("FD-SYSTEM-MIB", "manageIpAddr"),
        ("FD-SYSTEM-MIB", "manageNetMask"),
        ("FD-SYSTEM-MIB", "manageGateway"),
        ("FD-SYSTEM-MIB", "snmpReadCommunity"),
        ("FD-SYSTEM-MIB", "snmpRWCommunity"),
        ("FD-SYSTEM-MIB", "trapDstIpAddr1"),
        ("FD-SYSTEM-MIB", "trapDstIpAddr2"),
        ("FD-SYSTEM-MIB", "trapDstIpAddr3"),
        ("FD-SYSTEM-MIB", "trapDstIpAddr4"),
        ("FD-SYSTEM-MIB", "sysOperate"))
)
if mibBuilder.loadTexts:
    sysBaseManageGroup.setStatus("current")

chassisInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 2)
)
chassisInfoGroup.setObjects(
      *(("FD-SYSTEM-MIB", "chassisType"),
        ("FD-SYSTEM-MIB", "chassisFactorySerial"),
        ("FD-SYSTEM-MIB", "chassisRevision"),
        ("FD-SYSTEM-MIB", "chassisTemperature"),
        ("FD-SYSTEM-MIB", "powerStatusBit"),
        ("FD-SYSTEM-MIB", "fanStatusBit"))
)
if mibBuilder.loadTexts:
    chassisInfoGroup.setStatus("current")

cardModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 3)
)
cardModuleGroup.setObjects(
      *(("FD-SYSTEM-MIB", "mainCardType"),
        ("FD-SYSTEM-MIB", "mainCardFactorySerial"),
        ("FD-SYSTEM-MIB", "mainCardHWRevision"),
        ("FD-SYSTEM-MIB", "mainCardSWVersion"),
        ("FD-SYSTEM-MIB", "mainCardRunningStatus"),
        ("FD-SYSTEM-MIB", "mainCardRunningTime"),
        ("FD-SYSTEM-MIB", "mainCardOperate"),
        ("FD-SYSTEM-MIB", "ponCardType"),
        ("FD-SYSTEM-MIB", "ponCardFactorySerial"),
        ("FD-SYSTEM-MIB", "ponCardHwRev"),
        ("FD-SYSTEM-MIB", "ponCardFwVer"),
        ("FD-SYSTEM-MIB", "ponCardRunningStatus"),
        ("FD-SYSTEM-MIB", "ponCardRuningTime"),
        ("FD-SYSTEM-MIB", "ponCardOperate"),
        ("FD-SYSTEM-MIB", "ponCardUpgradeStat"))
)
if mibBuilder.loadTexts:
    cardModuleGroup.setStatus("current")

onuAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 4)
)
onuAuthGroup.setObjects(
      *(("FD-SYSTEM-MIB", "authMethod"),
        ("FD-SYSTEM-MIB", "nonAuthOper"),
        ("FD-SYSTEM-MIB", "beginMacAddr"),
        ("FD-SYSTEM-MIB", "endMacAddr"),
        ("FD-SYSTEM-MIB", "macAttr"),
        ("FD-SYSTEM-MIB", "onuAuthMacRowStatus"),
        ("FD-SYSTEM-MIB", "nonAuthOnuMac"),
        ("FD-SYSTEM-MIB", "nonAuthOnuTries"))
)
if mibBuilder.loadTexts:
    onuAuthGroup.setStatus("current")

userManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 5)
)
userManageGroup.setObjects(
      *(("FD-SYSTEM-MIB", "userName"),
        ("FD-SYSTEM-MIB", "userPassword"),
        ("FD-SYSTEM-MIB", "userPermission"),
        ("FD-SYSTEM-MIB", "userAccessDeviceMap"),
        ("FD-SYSTEM-MIB", "loginTimeout"),
        ("FD-SYSTEM-MIB", "userEntryRowStatus"))
)
if mibBuilder.loadTexts:
    userManageGroup.setStatus("current")

systemUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 1, 6)
)
systemUpgradeGroup.setObjects(
      *(("FD-SYSTEM-MIB", "ftpServerIp"),
        ("FD-SYSTEM-MIB", "ftpServerUserName"),
        ("FD-SYSTEM-MIB", "ftpServerUserPasswd"),
        ("FD-SYSTEM-MIB", "ftpOperFileName"),
        ("FD-SYSTEM-MIB", "dwLoadFileCrcCheck"),
        ("FD-SYSTEM-MIB", "dwLoadFileCrcValue"),
        ("FD-SYSTEM-MIB", "operDeviceMap"),
        ("FD-SYSTEM-MIB", "upgradeStatus"),
        ("FD-SYSTEM-MIB", "ftpProgress"),
        ("FD-SYSTEM-MIB", "upgradeOperation"),
        ("FD-SYSTEM-MIB", "ftpOperTarget"))
)
if mibBuilder.loadTexts:
    systemUpgradeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fdSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    fdSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-SYSTEM-MIB",
    **{"systemInfo": systemInfo,
       "sysBaseInfo": sysBaseInfo,
       "sysModel": sysModel,
       "sysDesc": sysDesc,
       "sysLocation": sysLocation,
       "sysContact": sysContact,
       "sysMajAlarmLed": sysMajAlarmLed,
       "sysCriAlarmLed": sysCriAlarmLed,
       "sysAlarmDesc": sysAlarmDesc,
       "sysConfig": sysConfig,
       "consolePortSpd": consolePortSpd,
       "manageIpAddr": manageIpAddr,
       "manageNetMask": manageNetMask,
       "manageGateway": manageGateway,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpRWCommunity": snmpRWCommunity,
       "trapDstIpAddr1": trapDstIpAddr1,
       "trapDstIpAddr2": trapDstIpAddr2,
       "trapDstIpAddr3": trapDstIpAddr3,
       "trapDstIpAddr4": trapDstIpAddr4,
       "sysOperate": sysOperate,
       "chassisInfo": chassisInfo,
       "chassisType": chassisType,
       "chassisFactorySerial": chassisFactorySerial,
       "chassisRevision": chassisRevision,
       "chassisTemperature": chassisTemperature,
       "powerStatusBit": powerStatusBit,
       "fanStatusBit": fanStatusBit,
       "cardModule": cardModule,
       "mainCard": mainCard,
       "mainCardType": mainCardType,
       "mainCardFactorySerial": mainCardFactorySerial,
       "mainCardHWRevision": mainCardHWRevision,
       "mainCardSWVersion": mainCardSWVersion,
       "mainCardRunningStatus": mainCardRunningStatus,
       "mainCardRunningTime": mainCardRunningTime,
       "mainCardOperate": mainCardOperate,
       "ponCard": ponCard,
       "ponCardTable": ponCardTable,
       "ponCardEntry": ponCardEntry,
       "ponCardSlotId": ponCardSlotId,
       "ponCardType": ponCardType,
       "ponCardFactorySerial": ponCardFactorySerial,
       "ponCardHwRev": ponCardHwRev,
       "ponCardFwVer": ponCardFwVer,
       "ponCardRunningStatus": ponCardRunningStatus,
       "ponCardRuningTime": ponCardRuningTime,
       "ponCardOperate": ponCardOperate,
       "ponCardUpgradeStat": ponCardUpgradeStat,
       "onuAuth": onuAuth,
       "authMethod": authMethod,
       "nonAuthOper": nonAuthOper,
       "onuAuthMacCfgTable": onuAuthMacCfgTable,
       "onuAuthMacCfgEntry": onuAuthMacCfgEntry,
       "authMacEntryId": authMacEntryId,
       "beginMacAddr": beginMacAddr,
       "endMacAddr": endMacAddr,
       "macAttr": macAttr,
       "onuAuthMacRowStatus": onuAuthMacRowStatus,
       "nonAuthOnuListTable": nonAuthOnuListTable,
       "nonAuthOnuListEntry": nonAuthOnuListEntry,
       "nonAuthOnuMacIndex": nonAuthOnuMacIndex,
       "nonAuthOnuMac": nonAuthOnuMac,
       "nonAuthOnuTries": nonAuthOnuTries,
       "userManage": userManage,
       "userManageTable": userManageTable,
       "userManageEntry": userManageEntry,
       "userId": userId,
       "userName": userName,
       "userPassword": userPassword,
       "userPermission": userPermission,
       "userAccessDeviceMap": userAccessDeviceMap,
       "loginTimeout": loginTimeout,
       "userEntryRowStatus": userEntryRowStatus,
       "upgrade": upgrade,
       "ftpServerIp": ftpServerIp,
       "ftpServerUserName": ftpServerUserName,
       "ftpServerUserPasswd": ftpServerUserPasswd,
       "ftpOperFileName": ftpOperFileName,
       "ftpOperTarget": ftpOperTarget,
       "dwLoadFileCrcCheck": dwLoadFileCrcCheck,
       "dwLoadFileCrcValue": dwLoadFileCrcValue,
       "operDeviceMap": operDeviceMap,
       "upgradeStatus": upgradeStatus,
       "upgradeOperation": upgradeOperation,
       "ftpProgress": ftpProgress,
       "fdSysConformance": fdSysConformance,
       "fdSystemGroups": fdSystemGroups,
       "sysBaseManageGroup": sysBaseManageGroup,
       "chassisInfoGroup": chassisInfoGroup,
       "cardModuleGroup": cardModuleGroup,
       "onuAuthGroup": onuAuthGroup,
       "userManageGroup": userManageGroup,
       "systemUpgradeGroup": systemUpgradeGroup,
       "fdSystemCompliances": fdSystemCompliances,
       "fdSystemCompliance": fdSystemCompliance}
)
