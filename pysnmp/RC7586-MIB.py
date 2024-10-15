# SNMP MIB module (RC7586-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RC7586-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:56 2024
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

rc7586MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2)
)
rc7586MIB.setRevisions(
        ("2009-05-13 00:00",)
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



class FaultStatus7586(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Buc1_ObjectIdentity = ObjectIdentity
buc1 = _Buc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1)
)
_Buc1Configuration_ObjectIdentity = ObjectIdentity
buc1Configuration = _Buc1Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1)
)
_Buc1TxSettings_ObjectIdentity = ObjectIdentity
buc1TxSettings = _Buc1TxSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1)
)


class _Buc1TxOn_Type(Integer32):
    """Custom type buc1TxOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc1TxOn_Type.__name__ = "Integer32"
_Buc1TxOn_Object = MibScalar
buc1TxOn = _Buc1TxOn_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 1),
    _Buc1TxOn_Type()
)
buc1TxOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1TxOn.setStatus("current")


class _Buc1TxDefault_Type(Integer32):
    """Custom type buc1TxDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc1TxDefault_Type.__name__ = "Integer32"
_Buc1TxDefault_Object = MibScalar
buc1TxDefault = _Buc1TxDefault_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 2),
    _Buc1TxDefault_Type()
)
buc1TxDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1TxDefault.setStatus("current")


class _Buc1TxAttenuator_Type(Integer32):
    """Custom type buc1TxAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Buc1TxAttenuator_Type.__name__ = "Integer32"
_Buc1TxAttenuator_Object = MibScalar
buc1TxAttenuator = _Buc1TxAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 1, 3),
    _Buc1TxAttenuator_Type()
)
buc1TxAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1TxAttenuator.setStatus("current")
if mibBuilder.loadTexts:
    buc1TxAttenuator.setUnits("dBm")
_Buc1PktProtocol_ObjectIdentity = ObjectIdentity
buc1PktProtocol = _Buc1PktProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2)
)


class _Buc1Protocol_Type(Integer32):
    """Custom type buc1Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Buc1Protocol_Type.__name__ = "Integer32"
_Buc1Protocol_Object = MibScalar
buc1Protocol = _Buc1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2, 1),
    _Buc1Protocol_Type()
)
buc1Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1Protocol.setStatus("current")
_Buc1Address_Type = Integer32
_Buc1Address_Object = MibScalar
buc1Address = _Buc1Address_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 2, 2),
    _Buc1Address_Type()
)
buc1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1Address.setStatus("current")
_Buc1RCSetting_ObjectIdentity = ObjectIdentity
buc1RCSetting = _Buc1RCSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3)
)


class _Buc1Mode_Type(Integer32):
    """Custom type buc1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Buc1Mode_Type.__name__ = "Integer32"
_Buc1Mode_Object = MibScalar
buc1Mode = _Buc1Mode_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3, 1),
    _Buc1Mode_Type()
)
buc1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1Mode.setStatus("current")
_Buc1OnLine_Type = TruthValue
_Buc1OnLine_Object = MibScalar
buc1OnLine = _Buc1OnLine_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 3, 2),
    _Buc1OnLine_Type()
)
buc1OnLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1OnLine.setStatus("current")
_Buc1Freqs_ObjectIdentity = ObjectIdentity
buc1Freqs = _Buc1Freqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4)
)
_Buc1RFFreq_Type = Integer32
_Buc1RFFreq_Object = MibScalar
buc1RFFreq = _Buc1RFFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 1),
    _Buc1RFFreq_Type()
)
buc1RFFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1RFFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc1RFFreq.setUnits("MHz")
_Buc1IFFreq_Type = Integer32
_Buc1IFFreq_Object = MibScalar
buc1IFFreq = _Buc1IFFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 2),
    _Buc1IFFreq_Type()
)
buc1IFFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1IFFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc1IFFreq.setUnits("MHz")
_Buc1LOFreq_Type = Integer32
_Buc1LOFreq_Object = MibScalar
buc1LOFreq = _Buc1LOFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 4, 3),
    _Buc1LOFreq_Type()
)
buc1LOFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1LOFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc1LOFreq.setUnits("MHz")
_Buc1Misc_ObjectIdentity = ObjectIdentity
buc1Misc = _Buc1Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5)
)
_Buc1SerIf_Type = DisplayString
_Buc1SerIf_Object = MibScalar
buc1SerIf = _Buc1SerIf_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 1),
    _Buc1SerIf_Type()
)
buc1SerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1SerIf.setStatus("current")
_Buc1PwrAlarmThresh_Type = DisplayString
_Buc1PwrAlarmThresh_Object = MibScalar
buc1PwrAlarmThresh = _Buc1PwrAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 2),
    _Buc1PwrAlarmThresh_Type()
)
buc1PwrAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1PwrAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    buc1PwrAlarmThresh.setUnits("dB")
_Buc1BurstPwrThresh_Type = DisplayString
_Buc1BurstPwrThresh_Object = MibScalar
buc1BurstPwrThresh = _Buc1BurstPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 3),
    _Buc1BurstPwrThresh_Type()
)
buc1BurstPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1BurstPwrThresh.setStatus("current")
if mibBuilder.loadTexts:
    buc1BurstPwrThresh.setUnits("dB")
_Buc1RefSource_Type = DisplayString
_Buc1RefSource_Object = MibScalar
buc1RefSource = _Buc1RefSource_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 4),
    _Buc1RefSource_Type()
)
buc1RefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1RefSource.setStatus("current")
_Buc1LEDState_Type = DisplayString
_Buc1LEDState_Object = MibScalar
buc1LEDState = _Buc1LEDState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 1, 5, 5),
    _Buc1LEDState_Type()
)
buc1LEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc1LEDState.setStatus("current")
_Buc1Status_ObjectIdentity = ObjectIdentity
buc1Status = _Buc1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2)
)


class _Buc1PaStatus_Type(Integer32):
    """Custom type buc1PaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc1PaStatus_Type.__name__ = "Integer32"
_Buc1PaStatus_Object = MibScalar
buc1PaStatus = _Buc1PaStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 1),
    _Buc1PaStatus_Type()
)
buc1PaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1PaStatus.setStatus("current")
_Buc1TxPower_Type = DisplayString
_Buc1TxPower_Object = MibScalar
buc1TxPower = _Buc1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 2),
    _Buc1TxPower_Type()
)
buc1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1TxPower.setStatus("current")
if mibBuilder.loadTexts:
    buc1TxPower.setUnits("dB")
_Buc1TxBurstPower_Type = DisplayString
_Buc1TxBurstPower_Object = MibScalar
buc1TxBurstPower = _Buc1TxBurstPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 3),
    _Buc1TxBurstPower_Type()
)
buc1TxBurstPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1TxBurstPower.setStatus("current")
if mibBuilder.loadTexts:
    buc1TxBurstPower.setUnits("dB")
_Buc1Faults_Type = Integer32
_Buc1Faults_Object = MibScalar
buc1Faults = _Buc1Faults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 4),
    _Buc1Faults_Type()
)
buc1Faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Faults.setStatus("current")
_Buc1LatchedFaults_Type = Integer32
_Buc1LatchedFaults_Object = MibScalar
buc1LatchedFaults = _Buc1LatchedFaults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 5),
    _Buc1LatchedFaults_Type()
)
buc1LatchedFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1LatchedFaults.setStatus("current")
_Buc1Temperature_Type = DisplayString
_Buc1Temperature_Object = MibScalar
buc1Temperature = _Buc1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 6),
    _Buc1Temperature_Type()
)
buc1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Temperature.setStatus("current")
_Buc1MinMaxTemperature_Type = DisplayString
_Buc1MinMaxTemperature_Object = MibScalar
buc1MinMaxTemperature = _Buc1MinMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 7),
    _Buc1MinMaxTemperature_Type()
)
buc1MinMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1MinMaxTemperature.setStatus("current")


class _Buc1SystemSetting_Type(Integer32):
    """Custom type buc1SystemSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_Buc1SystemSetting_Type.__name__ = "Integer32"
_Buc1SystemSetting_Object = MibScalar
buc1SystemSetting = _Buc1SystemSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 8),
    _Buc1SystemSetting_Type()
)
buc1SystemSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1SystemSetting.setStatus("current")


class _Buc1SystemPoll_Type(Integer32):
    """Custom type buc1SystemPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Buc1SystemPoll_Type.__name__ = "Integer32"
_Buc1SystemPoll_Object = MibScalar
buc1SystemPoll = _Buc1SystemPoll_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 9),
    _Buc1SystemPoll_Type()
)
buc1SystemPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1SystemPoll.setStatus("current")
_Buc1DeviceType_Type = DisplayString
_Buc1DeviceType_Object = MibScalar
buc1DeviceType = _Buc1DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 10),
    _Buc1DeviceType_Type()
)
buc1DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1DeviceType.setStatus("current")
_Buc1Gateway_Type = DisplayString
_Buc1Gateway_Object = MibScalar
buc1Gateway = _Buc1Gateway_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 11),
    _Buc1Gateway_Type()
)
buc1Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Gateway.setStatus("current")
_Buc1IpAddress_Type = DisplayString
_Buc1IpAddress_Object = MibScalar
buc1IpAddress = _Buc1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 12),
    _Buc1IpAddress_Type()
)
buc1IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1IpAddress.setStatus("current")
_Buc1MACAddress_Type = DisplayString
_Buc1MACAddress_Object = MibScalar
buc1MACAddress = _Buc1MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 13),
    _Buc1MACAddress_Type()
)
buc1MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1MACAddress.setStatus("current")
_Buc1Netmask_Type = DisplayString
_Buc1Netmask_Object = MibScalar
buc1Netmask = _Buc1Netmask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 14),
    _Buc1Netmask_Type()
)
buc1Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Netmask.setStatus("current")
_Buc1RefPower_Type = DisplayString
_Buc1RefPower_Object = MibScalar
buc1RefPower = _Buc1RefPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 15),
    _Buc1RefPower_Type()
)
buc1RefPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1RefPower.setStatus("current")
_Buc1Config_Type = DisplayString
_Buc1Config_Object = MibScalar
buc1Config = _Buc1Config_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 16),
    _Buc1Config_Type()
)
buc1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Config.setStatus("current")
_Buc1BuildStandard_Type = DisplayString
_Buc1BuildStandard_Object = MibScalar
buc1BuildStandard = _Buc1BuildStandard_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 2, 17),
    _Buc1BuildStandard_Type()
)
buc1BuildStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1BuildStandard.setStatus("current")
_Buc1Info_ObjectIdentity = ObjectIdentity
buc1Info = _Buc1Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3)
)
_Buc1IdInfo_Type = DisplayString
_Buc1IdInfo_Object = MibScalar
buc1IdInfo = _Buc1IdInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 1),
    _Buc1IdInfo_Type()
)
buc1IdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1IdInfo.setStatus("current")
_Buc1Limits_Type = DisplayString
_Buc1Limits_Object = MibScalar
buc1Limits = _Buc1Limits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 2),
    _Buc1Limits_Type()
)
buc1Limits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1Limits.setStatus("current")
_Buc1PktProtocolsInfo_Type = DisplayString
_Buc1PktProtocolsInfo_Object = MibScalar
buc1PktProtocolsInfo = _Buc1PktProtocolsInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 1, 3, 3),
    _Buc1PktProtocolsInfo_Type()
)
buc1PktProtocolsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc1PktProtocolsInfo.setStatus("current")
_Buc2_ObjectIdentity = ObjectIdentity
buc2 = _Buc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2)
)
_Buc2Configuration_ObjectIdentity = ObjectIdentity
buc2Configuration = _Buc2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1)
)
_Buc2TxSettings_ObjectIdentity = ObjectIdentity
buc2TxSettings = _Buc2TxSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1)
)


class _Buc2TxOn_Type(Integer32):
    """Custom type buc2TxOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc2TxOn_Type.__name__ = "Integer32"
_Buc2TxOn_Object = MibScalar
buc2TxOn = _Buc2TxOn_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 1),
    _Buc2TxOn_Type()
)
buc2TxOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2TxOn.setStatus("current")


class _Buc2TxDefault_Type(Integer32):
    """Custom type buc2TxDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc2TxDefault_Type.__name__ = "Integer32"
_Buc2TxDefault_Object = MibScalar
buc2TxDefault = _Buc2TxDefault_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 2),
    _Buc2TxDefault_Type()
)
buc2TxDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2TxDefault.setStatus("current")


class _Buc2TxAttenuator_Type(Integer32):
    """Custom type buc2TxAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Buc2TxAttenuator_Type.__name__ = "Integer32"
_Buc2TxAttenuator_Object = MibScalar
buc2TxAttenuator = _Buc2TxAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 1, 3),
    _Buc2TxAttenuator_Type()
)
buc2TxAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2TxAttenuator.setStatus("current")
if mibBuilder.loadTexts:
    buc2TxAttenuator.setUnits("dBm")
_Buc2PktProtocol_ObjectIdentity = ObjectIdentity
buc2PktProtocol = _Buc2PktProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2)
)


class _Buc2Protocol_Type(Integer32):
    """Custom type buc2Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Buc2Protocol_Type.__name__ = "Integer32"
_Buc2Protocol_Object = MibScalar
buc2Protocol = _Buc2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2, 1),
    _Buc2Protocol_Type()
)
buc2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2Protocol.setStatus("current")
_Buc2Address_Type = Integer32
_Buc2Address_Object = MibScalar
buc2Address = _Buc2Address_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 2, 2),
    _Buc2Address_Type()
)
buc2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2Address.setStatus("current")
_Buc2RCSetting_ObjectIdentity = ObjectIdentity
buc2RCSetting = _Buc2RCSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3)
)


class _Buc2Mode_Type(Integer32):
    """Custom type buc2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Buc2Mode_Type.__name__ = "Integer32"
_Buc2Mode_Object = MibScalar
buc2Mode = _Buc2Mode_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3, 1),
    _Buc2Mode_Type()
)
buc2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2Mode.setStatus("current")
_Buc2OnLine_Type = TruthValue
_Buc2OnLine_Object = MibScalar
buc2OnLine = _Buc2OnLine_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 3, 2),
    _Buc2OnLine_Type()
)
buc2OnLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2OnLine.setStatus("current")
_Buc2Freqs_ObjectIdentity = ObjectIdentity
buc2Freqs = _Buc2Freqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4)
)
_Buc2RFFreq_Type = Integer32
_Buc2RFFreq_Object = MibScalar
buc2RFFreq = _Buc2RFFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 1),
    _Buc2RFFreq_Type()
)
buc2RFFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2RFFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc2RFFreq.setUnits("MHz")
_Buc2IFFreq_Type = Integer32
_Buc2IFFreq_Object = MibScalar
buc2IFFreq = _Buc2IFFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 2),
    _Buc2IFFreq_Type()
)
buc2IFFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2IFFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc2IFFreq.setUnits("MHz")
_Buc2LOFreq_Type = Integer32
_Buc2LOFreq_Object = MibScalar
buc2LOFreq = _Buc2LOFreq_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 4, 3),
    _Buc2LOFreq_Type()
)
buc2LOFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2LOFreq.setStatus("current")
if mibBuilder.loadTexts:
    buc2LOFreq.setUnits("MHz")
_Buc2Misc_ObjectIdentity = ObjectIdentity
buc2Misc = _Buc2Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5)
)
_Buc2SerIf_Type = DisplayString
_Buc2SerIf_Object = MibScalar
buc2SerIf = _Buc2SerIf_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 1),
    _Buc2SerIf_Type()
)
buc2SerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2SerIf.setStatus("current")
_Buc2PwrAlarmThresh_Type = DisplayString
_Buc2PwrAlarmThresh_Object = MibScalar
buc2PwrAlarmThresh = _Buc2PwrAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 2),
    _Buc2PwrAlarmThresh_Type()
)
buc2PwrAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2PwrAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    buc2PwrAlarmThresh.setUnits("dB")
_Buc2BurstPwrThresh_Type = DisplayString
_Buc2BurstPwrThresh_Object = MibScalar
buc2BurstPwrThresh = _Buc2BurstPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 3),
    _Buc2BurstPwrThresh_Type()
)
buc2BurstPwrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2BurstPwrThresh.setStatus("current")
if mibBuilder.loadTexts:
    buc2BurstPwrThresh.setUnits("dB")
_Buc2RefSource_Type = DisplayString
_Buc2RefSource_Object = MibScalar
buc2RefSource = _Buc2RefSource_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 4),
    _Buc2RefSource_Type()
)
buc2RefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2RefSource.setStatus("current")
_Buc2LEDState_Type = DisplayString
_Buc2LEDState_Object = MibScalar
buc2LEDState = _Buc2LEDState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 1, 5, 5),
    _Buc2LEDState_Type()
)
buc2LEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buc2LEDState.setStatus("current")
_Buc2Status_ObjectIdentity = ObjectIdentity
buc2Status = _Buc2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2)
)


class _Buc2PaStatus_Type(Integer32):
    """Custom type buc2PaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Buc2PaStatus_Type.__name__ = "Integer32"
_Buc2PaStatus_Object = MibScalar
buc2PaStatus = _Buc2PaStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 1),
    _Buc2PaStatus_Type()
)
buc2PaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2PaStatus.setStatus("current")
_Buc2TxPower_Type = DisplayString
_Buc2TxPower_Object = MibScalar
buc2TxPower = _Buc2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 2),
    _Buc2TxPower_Type()
)
buc2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2TxPower.setStatus("current")
if mibBuilder.loadTexts:
    buc2TxPower.setUnits("dB")
_Buc2TxBurstPower_Type = DisplayString
_Buc2TxBurstPower_Object = MibScalar
buc2TxBurstPower = _Buc2TxBurstPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 3),
    _Buc2TxBurstPower_Type()
)
buc2TxBurstPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2TxBurstPower.setStatus("current")
if mibBuilder.loadTexts:
    buc2TxBurstPower.setUnits("dB")
_Buc2Faults_Type = Integer32
_Buc2Faults_Object = MibScalar
buc2Faults = _Buc2Faults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 4),
    _Buc2Faults_Type()
)
buc2Faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Faults.setStatus("current")
_Buc2LatchedFaults_Type = Integer32
_Buc2LatchedFaults_Object = MibScalar
buc2LatchedFaults = _Buc2LatchedFaults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 5),
    _Buc2LatchedFaults_Type()
)
buc2LatchedFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2LatchedFaults.setStatus("current")
_Buc2Temperature_Type = DisplayString
_Buc2Temperature_Object = MibScalar
buc2Temperature = _Buc2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 6),
    _Buc2Temperature_Type()
)
buc2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Temperature.setStatus("current")
_Buc2MinMaxTemperature_Type = DisplayString
_Buc2MinMaxTemperature_Object = MibScalar
buc2MinMaxTemperature = _Buc2MinMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 7),
    _Buc2MinMaxTemperature_Type()
)
buc2MinMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2MinMaxTemperature.setStatus("current")


class _Buc2SystemSetting_Type(Integer32):
    """Custom type buc2SystemSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_Buc2SystemSetting_Type.__name__ = "Integer32"
_Buc2SystemSetting_Object = MibScalar
buc2SystemSetting = _Buc2SystemSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 8),
    _Buc2SystemSetting_Type()
)
buc2SystemSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2SystemSetting.setStatus("current")


class _Buc2SystemPoll_Type(Integer32):
    """Custom type buc2SystemPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Buc2SystemPoll_Type.__name__ = "Integer32"
_Buc2SystemPoll_Object = MibScalar
buc2SystemPoll = _Buc2SystemPoll_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 9),
    _Buc2SystemPoll_Type()
)
buc2SystemPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2SystemPoll.setStatus("current")
_Buc2DeviceType_Type = DisplayString
_Buc2DeviceType_Object = MibScalar
buc2DeviceType = _Buc2DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 10),
    _Buc2DeviceType_Type()
)
buc2DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2DeviceType.setStatus("current")
_Buc2Gateway_Type = DisplayString
_Buc2Gateway_Object = MibScalar
buc2Gateway = _Buc2Gateway_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 11),
    _Buc2Gateway_Type()
)
buc2Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Gateway.setStatus("current")
_Buc2IpAddress_Type = DisplayString
_Buc2IpAddress_Object = MibScalar
buc2IpAddress = _Buc2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 12),
    _Buc2IpAddress_Type()
)
buc2IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2IpAddress.setStatus("current")
_Buc2MACAddress_Type = DisplayString
_Buc2MACAddress_Object = MibScalar
buc2MACAddress = _Buc2MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 13),
    _Buc2MACAddress_Type()
)
buc2MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2MACAddress.setStatus("current")
_Buc2Netmask_Type = DisplayString
_Buc2Netmask_Object = MibScalar
buc2Netmask = _Buc2Netmask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 14),
    _Buc2Netmask_Type()
)
buc2Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Netmask.setStatus("current")
_Buc2RefPower_Type = DisplayString
_Buc2RefPower_Object = MibScalar
buc2RefPower = _Buc2RefPower_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 15),
    _Buc2RefPower_Type()
)
buc2RefPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2RefPower.setStatus("current")
_Buc2Config_Type = DisplayString
_Buc2Config_Object = MibScalar
buc2Config = _Buc2Config_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 16),
    _Buc2Config_Type()
)
buc2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Config.setStatus("current")
_Buc2BuildStandard_Type = DisplayString
_Buc2BuildStandard_Object = MibScalar
buc2BuildStandard = _Buc2BuildStandard_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 2, 17),
    _Buc2BuildStandard_Type()
)
buc2BuildStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2BuildStandard.setStatus("current")
_Buc2Info_ObjectIdentity = ObjectIdentity
buc2Info = _Buc2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3)
)
_Buc2IdInfo_Type = DisplayString
_Buc2IdInfo_Object = MibScalar
buc2IdInfo = _Buc2IdInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 1),
    _Buc2IdInfo_Type()
)
buc2IdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2IdInfo.setStatus("current")
_Buc2Limits_Type = DisplayString
_Buc2Limits_Object = MibScalar
buc2Limits = _Buc2Limits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 2),
    _Buc2Limits_Type()
)
buc2Limits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2Limits.setStatus("current")
_Buc2PktProtocolsInfo_Type = DisplayString
_Buc2PktProtocolsInfo_Object = MibScalar
buc2PktProtocolsInfo = _Buc2PktProtocolsInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 2, 3, 3),
    _Buc2PktProtocolsInfo_Type()
)
buc2PktProtocolsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buc2PktProtocolsInfo.setStatus("current")
_Ctrl_ObjectIdentity = ObjectIdentity
ctrl = _Ctrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1)
)


class _OperationalMode_Type(Integer32):
    """Custom type operationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OperationalMode_Type.__name__ = "Integer32"
_OperationalMode_Object = MibScalar
operationalMode = _OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 1),
    _OperationalMode_Type()
)
operationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationalMode.setStatus("current")


class _OnlineStream_Type(Integer32):
    """Custom type onlineStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OnlineStream_Type.__name__ = "Integer32"
_OnlineStream_Object = MibScalar
onlineStream = _OnlineStream_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 2),
    _OnlineStream_Type()
)
onlineStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onlineStream.setStatus("current")


class _WaveguideSwitch_Type(Integer32):
    """Custom type waveguideSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WaveguideSwitch_Type.__name__ = "Integer32"
_WaveguideSwitch_Object = MibScalar
waveguideSwitch = _WaveguideSwitch_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 3),
    _WaveguideSwitch_Type()
)
waveguideSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waveguideSwitch.setStatus("current")


class _StartupTime_Type(Integer32):
    """Custom type startupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_StartupTime_Type.__name__ = "Integer32"
_StartupTime_Object = MibScalar
startupTime = _StartupTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 4),
    _StartupTime_Type()
)
startupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startupTime.setStatus("current")
if mibBuilder.loadTexts:
    startupTime.setUnits("s")
_LnbCurrentLimit_Type = DisplayString
_LnbCurrentLimit_Object = MibScalar
lnbCurrentLimit = _LnbCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 5),
    _LnbCurrentLimit_Type()
)
lnbCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnbCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    lnbCurrentLimit.setUnits("mA")


class _LedState_Type(Integer32):
    """Custom type ledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LedState_Type.__name__ = "Integer32"
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 6),
    _LedState_Type()
)
ledState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledState.setStatus("current")


class _RefSource_Type(Integer32):
    """Custom type refSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RefSource_Type.__name__ = "Integer32"
_RefSource_Object = MibScalar
refSource = _RefSource_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 7),
    _RefSource_Type()
)
refSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refSource.setStatus("current")
_RefTrim_Type = DisplayString
_RefTrim_Object = MibScalar
refTrim = _RefTrim_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 8),
    _RefTrim_Type()
)
refTrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refTrim.setStatus("current")
_RefThresh_Type = DisplayString
_RefThresh_Object = MibScalar
refThresh = _RefThresh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 9),
    _RefThresh_Type()
)
refThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refThresh.setStatus("current")
if mibBuilder.loadTexts:
    refThresh.setUnits("dBm")
_RefPwr_Type = DisplayString
_RefPwr_Object = MibScalar
refPwr = _RefPwr_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 10),
    _RefPwr_Type()
)
refPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refPwr.setStatus("current")
if mibBuilder.loadTexts:
    refPwr.setUnits("dBm")
_IpAddr_Type = DisplayString
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 11),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 12),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_Netmask_Type = DisplayString
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 13),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_Gateway_Type = DisplayString
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 1, 14),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2)
)
_LnbCurrent_Type = DisplayString
_LnbCurrent_Object = MibScalar
lnbCurrent = _LnbCurrent_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 1),
    _LnbCurrent_Type()
)
lnbCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnbCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lnbCurrent.setUnits("mA")
_LnbVoltage_Type = DisplayString
_LnbVoltage_Object = MibScalar
lnbVoltage = _LnbVoltage_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 2),
    _LnbVoltage_Type()
)
lnbVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnbVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lnbVoltage.setUnits("V")
_Faults_Type = Integer32
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 2, 3),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 3)
)
_IdInfo_Type = DisplayString
_IdInfo_Object = MibScalar
idInfo = _IdInfo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 2, 2, 3, 3, 1),
    _IdInfo_Type()
)
idInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC7586-MIB",
    **{"ComponentRevision": ComponentRevision,
       "FaultStatus7586": FaultStatus7586,
       "rc7586MIB": rc7586MIB,
       "buc1": buc1,
       "buc1Configuration": buc1Configuration,
       "buc1TxSettings": buc1TxSettings,
       "buc1TxOn": buc1TxOn,
       "buc1TxDefault": buc1TxDefault,
       "buc1TxAttenuator": buc1TxAttenuator,
       "buc1PktProtocol": buc1PktProtocol,
       "buc1Protocol": buc1Protocol,
       "buc1Address": buc1Address,
       "buc1RCSetting": buc1RCSetting,
       "buc1Mode": buc1Mode,
       "buc1OnLine": buc1OnLine,
       "buc1Freqs": buc1Freqs,
       "buc1RFFreq": buc1RFFreq,
       "buc1IFFreq": buc1IFFreq,
       "buc1LOFreq": buc1LOFreq,
       "buc1Misc": buc1Misc,
       "buc1SerIf": buc1SerIf,
       "buc1PwrAlarmThresh": buc1PwrAlarmThresh,
       "buc1BurstPwrThresh": buc1BurstPwrThresh,
       "buc1RefSource": buc1RefSource,
       "buc1LEDState": buc1LEDState,
       "buc1Status": buc1Status,
       "buc1PaStatus": buc1PaStatus,
       "buc1TxPower": buc1TxPower,
       "buc1TxBurstPower": buc1TxBurstPower,
       "buc1Faults": buc1Faults,
       "buc1LatchedFaults": buc1LatchedFaults,
       "buc1Temperature": buc1Temperature,
       "buc1MinMaxTemperature": buc1MinMaxTemperature,
       "buc1SystemSetting": buc1SystemSetting,
       "buc1SystemPoll": buc1SystemPoll,
       "buc1DeviceType": buc1DeviceType,
       "buc1Gateway": buc1Gateway,
       "buc1IpAddress": buc1IpAddress,
       "buc1MACAddress": buc1MACAddress,
       "buc1Netmask": buc1Netmask,
       "buc1RefPower": buc1RefPower,
       "buc1Config": buc1Config,
       "buc1BuildStandard": buc1BuildStandard,
       "buc1Info": buc1Info,
       "buc1IdInfo": buc1IdInfo,
       "buc1Limits": buc1Limits,
       "buc1PktProtocolsInfo": buc1PktProtocolsInfo,
       "buc2": buc2,
       "buc2Configuration": buc2Configuration,
       "buc2TxSettings": buc2TxSettings,
       "buc2TxOn": buc2TxOn,
       "buc2TxDefault": buc2TxDefault,
       "buc2TxAttenuator": buc2TxAttenuator,
       "buc2PktProtocol": buc2PktProtocol,
       "buc2Protocol": buc2Protocol,
       "buc2Address": buc2Address,
       "buc2RCSetting": buc2RCSetting,
       "buc2Mode": buc2Mode,
       "buc2OnLine": buc2OnLine,
       "buc2Freqs": buc2Freqs,
       "buc2RFFreq": buc2RFFreq,
       "buc2IFFreq": buc2IFFreq,
       "buc2LOFreq": buc2LOFreq,
       "buc2Misc": buc2Misc,
       "buc2SerIf": buc2SerIf,
       "buc2PwrAlarmThresh": buc2PwrAlarmThresh,
       "buc2BurstPwrThresh": buc2BurstPwrThresh,
       "buc2RefSource": buc2RefSource,
       "buc2LEDState": buc2LEDState,
       "buc2Status": buc2Status,
       "buc2PaStatus": buc2PaStatus,
       "buc2TxPower": buc2TxPower,
       "buc2TxBurstPower": buc2TxBurstPower,
       "buc2Faults": buc2Faults,
       "buc2LatchedFaults": buc2LatchedFaults,
       "buc2Temperature": buc2Temperature,
       "buc2MinMaxTemperature": buc2MinMaxTemperature,
       "buc2SystemSetting": buc2SystemSetting,
       "buc2SystemPoll": buc2SystemPoll,
       "buc2DeviceType": buc2DeviceType,
       "buc2Gateway": buc2Gateway,
       "buc2IpAddress": buc2IpAddress,
       "buc2MACAddress": buc2MACAddress,
       "buc2Netmask": buc2Netmask,
       "buc2RefPower": buc2RefPower,
       "buc2Config": buc2Config,
       "buc2BuildStandard": buc2BuildStandard,
       "buc2Info": buc2Info,
       "buc2IdInfo": buc2IdInfo,
       "buc2Limits": buc2Limits,
       "buc2PktProtocolsInfo": buc2PktProtocolsInfo,
       "ctrl": ctrl,
       "settings": settings,
       "operationalMode": operationalMode,
       "onlineStream": onlineStream,
       "waveguideSwitch": waveguideSwitch,
       "startupTime": startupTime,
       "lnbCurrentLimit": lnbCurrentLimit,
       "ledState": ledState,
       "refSource": refSource,
       "refTrim": refTrim,
       "refThresh": refThresh,
       "refPwr": refPwr,
       "ipAddr": ipAddr,
       "macAddress": macAddress,
       "netmask": netmask,
       "gateway": gateway,
       "status": status,
       "lnbCurrent": lnbCurrent,
       "lnbVoltage": lnbVoltage,
       "faults": faults,
       "info": info,
       "idInfo": idInfo}
)
