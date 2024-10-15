# SNMP MIB module (HIK-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIK-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:26 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39165)
)
_Devicemib_ObjectIdentity = ObjectIdentity
devicemib = _Devicemib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39165, 1)
)


class _DeviceType_Type(OctetString):
    """Custom type deviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceType_Type.__name__ = "OctetString"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 1),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")


class _HardwVersion_Type(OctetString):
    """Custom type hardwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HardwVersion_Type.__name__ = "OctetString"
_HardwVersion_Object = MibScalar
hardwVersion = _HardwVersion_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 2),
    _HardwVersion_Type()
)
hardwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwVersion.setStatus("current")


class _SoftwVersion_Type(OctetString):
    """Custom type softwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwVersion_Type.__name__ = "OctetString"
_SoftwVersion_Object = MibScalar
softwVersion = _SoftwVersion_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 3),
    _SoftwVersion_Type()
)
softwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwVersion.setStatus("current")


class _MacAddr_Type(OctetString):
    """Custom type macAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MacAddr_Type.__name__ = "OctetString"
_MacAddr_Object = MibScalar
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 4),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")


class _DeviceID_Type(OctetString):
    """Custom type deviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceID_Type.__name__ = "OctetString"
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 5),
    _DeviceID_Type()
)
deviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceID.setStatus("current")


class _Manufacturer_Type(OctetString):
    """Custom type manufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Manufacturer_Type.__name__ = "OctetString"
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 6),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")


class _CpuPercent_Type(OctetString):
    """Custom type cpuPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpuPercent_Type.__name__ = "OctetString"
_CpuPercent_Object = MibScalar
cpuPercent = _CpuPercent_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 7),
    _CpuPercent_Type()
)
cpuPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPercent.setStatus("current")


class _DiskSize_Type(OctetString):
    """Custom type diskSize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskSize_Type.__name__ = "OctetString"
_DiskSize_Object = MibScalar
diskSize = _DiskSize_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 8),
    _DiskSize_Type()
)
diskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSize.setStatus("current")


class _DiskPercent_Type(OctetString):
    """Custom type diskPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskPercent_Type.__name__ = "OctetString"
_DiskPercent_Object = MibScalar
diskPercent = _DiskPercent_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 9),
    _DiskPercent_Type()
)
diskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPercent.setStatus("current")


class _MemSize_Type(OctetString):
    """Custom type memSize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemSize_Type.__name__ = "OctetString"
_MemSize_Object = MibScalar
memSize = _MemSize_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 10),
    _MemSize_Type()
)
memSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSize.setStatus("current")


class _MemUsed_Type(OctetString):
    """Custom type memUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemUsed_Type.__name__ = "OctetString"
_MemUsed_Object = MibScalar
memUsed = _MemUsed_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 11),
    _MemUsed_Type()
)
memUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsed.setStatus("current")
_RestartDev_Type = Integer32
_RestartDev_Object = MibScalar
restartDev = _RestartDev_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 12),
    _RestartDev_Type()
)
restartDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDev.setStatus("current")
_DynIpAddr_Type = IpAddress
_DynIpAddr_Object = MibScalar
dynIpAddr = _DynIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 13),
    _DynIpAddr_Type()
)
dynIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynIpAddr.setStatus("current")
_DynNetMask_Type = IpAddress
_DynNetMask_Object = MibScalar
dynNetMask = _DynNetMask_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 14),
    _DynNetMask_Type()
)
dynNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynNetMask.setStatus("current")
_DynGateway_Type = IpAddress
_DynGateway_Object = MibScalar
dynGateway = _DynGateway_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 15),
    _DynGateway_Type()
)
dynGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynGateway.setStatus("current")
_StaticIpAddr_Type = IpAddress
_StaticIpAddr_Object = MibScalar
staticIpAddr = _StaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 16),
    _StaticIpAddr_Type()
)
staticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpAddr.setStatus("current")
_StaticNetMask_Type = IpAddress
_StaticNetMask_Object = MibScalar
staticNetMask = _StaticNetMask_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 17),
    _StaticNetMask_Type()
)
staticNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticNetMask.setStatus("current")
_StaticGateway_Type = IpAddress
_StaticGateway_Object = MibScalar
staticGateway = _StaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 18),
    _StaticGateway_Type()
)
staticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticGateway.setStatus("current")


class _SysTime_Type(OctetString):
    """Custom type sysTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysTime_Type.__name__ = "OctetString"
_SysTime_Object = MibScalar
sysTime = _SysTime_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 19),
    _SysTime_Type()
)
sysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTime.setStatus("current")
_VideoInChanNum_Type = Integer32
_VideoInChanNum_Object = MibScalar
videoInChanNum = _VideoInChanNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 20),
    _VideoInChanNum_Type()
)
videoInChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoInChanNum.setStatus("current")


class _VideoEncode_Type(OctetString):
    """Custom type videoEncode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VideoEncode_Type.__name__ = "OctetString"
_VideoEncode_Object = MibScalar
videoEncode = _VideoEncode_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 21),
    _VideoEncode_Type()
)
videoEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoEncode.setStatus("current")


class _VideoNetTrans_Type(OctetString):
    """Custom type videoNetTrans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VideoNetTrans_Type.__name__ = "OctetString"
_VideoNetTrans_Object = MibScalar
videoNetTrans = _VideoNetTrans_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 22),
    _VideoNetTrans_Type()
)
videoNetTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoNetTrans.setStatus("current")
_AudioAbility_Type = Integer32
_AudioAbility_Object = MibScalar
audioAbility = _AudioAbility_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 23),
    _AudioAbility_Type()
)
audioAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioAbility.setStatus("current")
_AudioInNum_Type = Integer32
_AudioInNum_Object = MibScalar
audioInNum = _AudioInNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 24),
    _AudioInNum_Type()
)
audioInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioInNum.setStatus("current")
_VideoOutNum_Type = Integer32
_VideoOutNum_Object = MibScalar
videoOutNum = _VideoOutNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 25),
    _VideoOutNum_Type()
)
videoOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoOutNum.setStatus("current")
_ClarityChanNum_Type = Integer32
_ClarityChanNum_Object = MibScalar
clarityChanNum = _ClarityChanNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 26),
    _ClarityChanNum_Type()
)
clarityChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clarityChanNum.setStatus("current")
_LocalStorage_Type = Integer32
_LocalStorage_Object = MibScalar
localStorage = _LocalStorage_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 27),
    _LocalStorage_Type()
)
localStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localStorage.setStatus("current")
_RtspPlayBack_Type = Integer32
_RtspPlayBack_Object = MibScalar
rtspPlayBack = _RtspPlayBack_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 28),
    _RtspPlayBack_Type()
)
rtspPlayBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspPlayBack.setStatus("current")


class _NetAccessType_Type(OctetString):
    """Custom type netAccessType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetAccessType_Type.__name__ = "OctetString"
_NetAccessType_Object = MibScalar
netAccessType = _NetAccessType_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 29),
    _NetAccessType_Type()
)
netAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAccessType.setStatus("current")
_AlarmInChanNum_Type = Integer32
_AlarmInChanNum_Object = MibScalar
alarmInChanNum = _AlarmInChanNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 30),
    _AlarmInChanNum_Type()
)
alarmInChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInChanNum.setStatus("current")
_AlarmOutChanNum_Type = Integer32
_AlarmOutChanNum_Object = MibScalar
alarmOutChanNum = _AlarmOutChanNum_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 31),
    _AlarmOutChanNum_Type()
)
alarmOutChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOutChanNum.setStatus("current")
_ManageServAddr_Type = IpAddress
_ManageServAddr_Object = MibScalar
manageServAddr = _ManageServAddr_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 32),
    _ManageServAddr_Type()
)
manageServAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manageServAddr.setStatus("current")


class _NtpServIpAddr_Type(OctetString):
    """Custom type ntpServIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtpServIpAddr_Type.__name__ = "OctetString"
_NtpServIpAddr_Object = MibScalar
ntpServIpAddr = _NtpServIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 33),
    _NtpServIpAddr_Type()
)
ntpServIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServIpAddr.setStatus("current")
_ManagePort_Type = Integer32
_ManagePort_Object = MibScalar
managePort = _ManagePort_Object(
    (1, 3, 6, 1, 4, 1, 39165, 1, 34),
    _ManagePort_Type()
)
managePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managePort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIK-DEVICE-MIB",
    **{"test": test,
       "devicemib": devicemib,
       "deviceType": deviceType,
       "hardwVersion": hardwVersion,
       "softwVersion": softwVersion,
       "macAddr": macAddr,
       "deviceID": deviceID,
       "manufacturer": manufacturer,
       "cpuPercent": cpuPercent,
       "diskSize": diskSize,
       "diskPercent": diskPercent,
       "memSize": memSize,
       "memUsed": memUsed,
       "restartDev": restartDev,
       "dynIpAddr": dynIpAddr,
       "dynNetMask": dynNetMask,
       "dynGateway": dynGateway,
       "staticIpAddr": staticIpAddr,
       "staticNetMask": staticNetMask,
       "staticGateway": staticGateway,
       "sysTime": sysTime,
       "videoInChanNum": videoInChanNum,
       "videoEncode": videoEncode,
       "videoNetTrans": videoNetTrans,
       "audioAbility": audioAbility,
       "audioInNum": audioInNum,
       "videoOutNum": videoOutNum,
       "clarityChanNum": clarityChanNum,
       "localStorage": localStorage,
       "rtspPlayBack": rtspPlayBack,
       "netAccessType": netAccessType,
       "alarmInChanNum": alarmInChanNum,
       "alarmOutChanNum": alarmOutChanNum,
       "manageServAddr": manageServAddr,
       "ntpServIpAddr": ntpServIpAddr,
       "managePort": managePort}
)
