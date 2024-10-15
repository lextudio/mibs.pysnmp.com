# SNMP MIB module (RBUC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBUC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:40 2024
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

(satcomMibs,) = mibBuilder.importSymbols(
    "CODAN-SMI",
    "satcomMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rbucMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1)
)
rbucMIB.setRevisions(
        ("2009-02-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ComponentRevision(DisplayString, TextualConvention):
    status = "current"
    displayHint = "vxx.yy"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class FaultStatus(Bits, TextualConvention):
    status = "current"


class TxStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1)
)
_TxSettings_ObjectIdentity = ObjectIdentity
txSettings = _TxSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1)
)
_TxOn_Type = Integer32
_TxOn_Object = MibScalar
txOn = _TxOn_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 1),
    _TxOn_Type()
)
txOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txOn.setStatus("current")
_TxDefault_Type = TruthValue
_TxDefault_Object = MibScalar
txDefault = _TxDefault_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 2),
    _TxDefault_Type()
)
txDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txDefault.setStatus("current")


class _TxAttenuator_Type(Integer32):
    """Custom type txAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TxAttenuator_Type.__name__ = "Integer32"
_TxAttenuator_Object = MibScalar
txAttenuator = _TxAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 1, 3),
    _TxAttenuator_Type()
)
txAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txAttenuator.setStatus("current")
if mibBuilder.loadTexts:
    txAttenuator.setUnits("dBm")
_PktProtocol_ObjectIdentity = ObjectIdentity
pktProtocol = _PktProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2)
)


class _Protocol_Type(Integer32):
    """Custom type protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Protocol_Type.__name__ = "Integer32"
_Protocol_Object = MibScalar
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2, 1),
    _Protocol_Type()
)
protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocol.setStatus("current")
_Address_Type = Integer32
_Address_Object = MibScalar
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 2, 2),
    _Address_Type()
)
address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    address.setStatus("current")
_RcSetting_ObjectIdentity = ObjectIdentity
rcSetting = _RcSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3)
)


class _Mode_Type(Integer32):
    """Custom type mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Mode_Type.__name__ = "Integer32"
_Mode_Object = MibScalar
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3, 1),
    _Mode_Type()
)
mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mode.setStatus("current")
_OnLine_Type = TruthValue
_OnLine_Object = MibScalar
onLine = _OnLine_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 3, 2),
    _OnLine_Type()
)
onLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onLine.setStatus("current")
_Freqs_ObjectIdentity = ObjectIdentity
freqs = _Freqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4)
)
_RfFreq_Type = Integer32
_RfFreq_Object = MibScalar
rfFreq = _RfFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 1),
    _RfFreq_Type()
)
rfFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFreq.setStatus("current")
if mibBuilder.loadTexts:
    rfFreq.setUnits("MHz")
_IfFreq_Type = Integer32
_IfFreq_Object = MibScalar
ifFreq = _IfFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 2),
    _IfFreq_Type()
)
ifFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifFreq.setStatus("current")
if mibBuilder.loadTexts:
    ifFreq.setUnits("MHz")
_LoFreq_Type = Integer32
_LoFreq_Object = MibScalar
loFreq = _LoFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 4, 3),
    _LoFreq_Type()
)
loFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loFreq.setStatus("current")
if mibBuilder.loadTexts:
    loFreq.setUnits("MHz")
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5)
)
_SerIf_Type = DisplayString
_SerIf_Object = MibScalar
serIf = _SerIf_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 1),
    _SerIf_Type()
)
serIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serIf.setStatus("current")
_SerEcho_Type = TruthValue
_SerEcho_Object = MibScalar
serEcho = _SerEcho_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 2),
    _SerEcho_Type()
)
serEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serEcho.setStatus("current")
_PwrAlarmThresh_Type = DisplayString
_PwrAlarmThresh_Object = MibScalar
pwrAlarmThresh = _PwrAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 3),
    _PwrAlarmThresh_Type()
)
pwrAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwrAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    pwrAlarmThresh.setUnits("dB")
_BurstPwrThresh_Type = DisplayString
_BurstPwrThresh_Object = MibScalar
burstPwrThresh = _BurstPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 4),
    _BurstPwrThresh_Type()
)
burstPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    burstPwrThresh.setStatus("current")
if mibBuilder.loadTexts:
    burstPwrThresh.setUnits("dB")
_RefSource_Type = TruthValue
_RefSource_Object = MibScalar
refSource = _RefSource_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 5),
    _RefSource_Type()
)
refSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refSource.setStatus("current")
_LedState_Type = TruthValue
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 1, 5, 6),
    _LedState_Type()
)
ledState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2)
)


class _PaStatus_Type(Integer32):
    """Custom type paStatus based on Integer32"""
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


_PaStatus_Type.__name__ = "Integer32"
_PaStatus_Object = MibScalar
paStatus = _PaStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 1),
    _PaStatus_Type()
)
paStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paStatus.setStatus("current")
_TxPower_Type = DisplayString
_TxPower_Object = MibScalar
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 2),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("current")
if mibBuilder.loadTexts:
    txPower.setUnits("dB")
_TxBurstPower_Type = DisplayString
_TxBurstPower_Object = MibScalar
txBurstPower = _TxBurstPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 3),
    _TxBurstPower_Type()
)
txBurstPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBurstPower.setStatus("current")
if mibBuilder.loadTexts:
    txBurstPower.setUnits("dB")
_Faults_Type = Integer32
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 4),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")
_LatchedFaults_Type = Integer32
_LatchedFaults_Object = MibScalar
latchedFaults = _LatchedFaults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 5),
    _LatchedFaults_Type()
)
latchedFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latchedFaults.setStatus("current")
_Temperature_Type = DisplayString
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 6),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_MinMaxTemperature_Type = DisplayString
_MinMaxTemperature_Object = MibScalar
minMaxTemperature = _MinMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 7),
    _MinMaxTemperature_Type()
)
minMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minMaxTemperature.setStatus("current")


class _SystemSetting_Type(Integer32):
    """Custom type systemSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_SystemSetting_Type.__name__ = "Integer32"
_SystemSetting_Object = MibScalar
systemSetting = _SystemSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 8),
    _SystemSetting_Type()
)
systemSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSetting.setStatus("current")


class _SystemPoll_Type(Integer32):
    """Custom type systemPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SystemPoll_Type.__name__ = "Integer32"
_SystemPoll_Object = MibScalar
systemPoll = _SystemPoll_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 9),
    _SystemPoll_Type()
)
systemPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPoll.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 10),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_Gateway_Type = DisplayString
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 11),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_IpAddr_Type = DisplayString
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 12),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 13),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_Netmask_Type = DisplayString
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 14),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_RefPower_Type = DisplayString
_RefPower_Object = MibScalar
refPower = _RefPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 15),
    _RefPower_Type()
)
refPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refPower.setStatus("current")
_BucConfiguration_Type = DisplayString
_BucConfiguration_Object = MibScalar
bucConfiguration = _BucConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 16),
    _BucConfiguration_Type()
)
bucConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bucConfiguration.setStatus("current")
_BuildStandard_Type = DisplayString
_BuildStandard_Object = MibScalar
buildStandard = _BuildStandard_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 2, 17),
    _BuildStandard_Type()
)
buildStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildStandard.setStatus("current")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 3)
)
_IdInfo_Type = DisplayString
_IdInfo_Object = MibScalar
idInfo = _IdInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 1),
    _IdInfo_Type()
)
idInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idInfo.setStatus("current")
_Limits_Type = DisplayString
_Limits_Object = MibScalar
limits = _Limits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 2),
    _Limits_Type()
)
limits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limits.setStatus("current")
_PktProtocolsInfo_Type = DisplayString
_PktProtocolsInfo_Object = MibScalar
pktProtocolsInfo = _PktProtocolsInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 1, 3, 3),
    _PktProtocolsInfo_Type()
)
pktProtocolsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktProtocolsInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBUC-MIB",
    **{"ComponentRevision": ComponentRevision,
       "FaultStatus": FaultStatus,
       "TxStatus": TxStatus,
       "rbucMIB": rbucMIB,
       "configuration": configuration,
       "txSettings": txSettings,
       "txOn": txOn,
       "txDefault": txDefault,
       "txAttenuator": txAttenuator,
       "pktProtocol": pktProtocol,
       "protocol": protocol,
       "address": address,
       "rcSetting": rcSetting,
       "mode": mode,
       "onLine": onLine,
       "freqs": freqs,
       "rfFreq": rfFreq,
       "ifFreq": ifFreq,
       "loFreq": loFreq,
       "misc": misc,
       "serIf": serIf,
       "serEcho": serEcho,
       "pwrAlarmThresh": pwrAlarmThresh,
       "burstPwrThresh": burstPwrThresh,
       "refSource": refSource,
       "ledState": ledState,
       "status": status,
       "paStatus": paStatus,
       "txPower": txPower,
       "txBurstPower": txBurstPower,
       "faults": faults,
       "latchedFaults": latchedFaults,
       "temperature": temperature,
       "minMaxTemperature": minMaxTemperature,
       "systemSetting": systemSetting,
       "systemPoll": systemPoll,
       "deviceType": deviceType,
       "gateway": gateway,
       "ipAddr": ipAddr,
       "macAddress": macAddress,
       "netmask": netmask,
       "refPower": refPower,
       "bucConfiguration": bucConfiguration,
       "buildStandard": buildStandard,
       "info": info,
       "idInfo": idInfo,
       "limits": limits,
       "pktProtocolsInfo": pktProtocolsInfo}
)
