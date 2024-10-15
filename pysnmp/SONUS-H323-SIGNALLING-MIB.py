# SNMP MIB module (SONUS-H323-SIGNALLING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-H323-SIGNALLING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:58 2024
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

(PerfCurrentCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount")

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

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(SonusAdminState,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusServiceState")


# MODULE-IDENTITY

sonusH323SignallingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusH323SignallingMIBObjects_ObjectIdentity = ObjectIdentity
sonusH323SignallingMIBObjects = _SonusH323SignallingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1)
)
_SonusH323SigTimerObjects_ObjectIdentity = ObjectIdentity
sonusH323SigTimerObjects = _SonusH323SigTimerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1)
)


class _SonusH323SigSrvTimerT301_Type(Integer32):
    """Custom type sonusH323SigSrvTimerT301 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusH323SigSrvTimerT301_Type.__name__ = "Integer32"
_SonusH323SigSrvTimerT301_Object = MibScalar
sonusH323SigSrvTimerT301 = _SonusH323SigSrvTimerT301_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1, 1),
    _SonusH323SigSrvTimerT301_Type()
)
sonusH323SigSrvTimerT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SigSrvTimerT301.setStatus("current")


class _SonusH323SigSrvTimerT303_Type(Integer32):
    """Custom type sonusH323SigSrvTimerT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusH323SigSrvTimerT303_Type.__name__ = "Integer32"
_SonusH323SigSrvTimerT303_Object = MibScalar
sonusH323SigSrvTimerT303 = _SonusH323SigSrvTimerT303_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1, 2),
    _SonusH323SigSrvTimerT303_Type()
)
sonusH323SigSrvTimerT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SigSrvTimerT303.setStatus("current")


class _SonusH323SigSrvTimerT310_Type(Integer32):
    """Custom type sonusH323SigSrvTimerT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusH323SigSrvTimerT310_Type.__name__ = "Integer32"
_SonusH323SigSrvTimerT310_Object = MibScalar
sonusH323SigSrvTimerT310 = _SonusH323SigSrvTimerT310_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1, 3),
    _SonusH323SigSrvTimerT310_Type()
)
sonusH323SigSrvTimerT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SigSrvTimerT310.setStatus("current")


class _SonusH323SigTimerEstablish_Type(Integer32):
    """Custom type sonusH323SigTimerEstablish based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusH323SigTimerEstablish_Type.__name__ = "Integer32"
_SonusH323SigTimerEstablish_Object = MibScalar
sonusH323SigTimerEstablish = _SonusH323SigTimerEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1, 4),
    _SonusH323SigTimerEstablish_Type()
)
sonusH323SigTimerEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SigTimerEstablish.setStatus("current")


class _SonusH323SigTimerTcpConnect_Type(Integer32):
    """Custom type sonusH323SigTimerTcpConnect based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusH323SigTimerTcpConnect_Type.__name__ = "Integer32"
_SonusH323SigTimerTcpConnect_Object = MibScalar
sonusH323SigTimerTcpConnect = _SonusH323SigTimerTcpConnect_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 1, 5),
    _SonusH323SigTimerTcpConnect_Type()
)
sonusH323SigTimerTcpConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SigTimerTcpConnect.setStatus("current")
_SonusH323H225PortObjects_ObjectIdentity = ObjectIdentity
sonusH323H225PortObjects = _SonusH323H225PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 2)
)


class _SonusH323H225PortIpAddress_Type(IpAddress):
    """Custom type sonusH323H225PortIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SonusH323H225PortIpAddress_Object = MibScalar
sonusH323H225PortIpAddress = _SonusH323H225PortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 2, 1),
    _SonusH323H225PortIpAddress_Type()
)
sonusH323H225PortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H225PortIpAddress.setStatus("current")


class _SonusH323H225PortNum_Type(Integer32):
    """Custom type sonusH323H225PortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusH323H225PortNum_Type.__name__ = "Integer32"
_SonusH323H225PortNum_Object = MibScalar
sonusH323H225PortNum = _SonusH323H225PortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 2, 2),
    _SonusH323H225PortNum_Type()
)
sonusH323H225PortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H225PortNum.setStatus("current")


class _SonusH323H225PortShelfId_Type(Integer32):
    """Custom type sonusH323H225PortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_SonusH323H225PortShelfId_Type.__name__ = "Integer32"
_SonusH323H225PortShelfId_Object = MibScalar
sonusH323H225PortShelfId = _SonusH323H225PortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 2, 3),
    _SonusH323H225PortShelfId_Type()
)
sonusH323H225PortShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H225PortShelfId.setStatus("current")


class _SonusH323H225PortSlotNum_Type(Integer32):
    """Custom type sonusH323H225PortSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusH323H225PortSlotNum_Type.__name__ = "Integer32"
_SonusH323H225PortSlotNum_Object = MibScalar
sonusH323H225PortSlotNum = _SonusH323H225PortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 2, 4),
    _SonusH323H225PortSlotNum_Type()
)
sonusH323H225PortSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H225PortSlotNum.setStatus("current")
_SonusH323H245PortObjects_ObjectIdentity = ObjectIdentity
sonusH323H245PortObjects = _SonusH323H245PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 3)
)


class _SonusH323H245PortIpAddress_Type(IpAddress):
    """Custom type sonusH323H245PortIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SonusH323H245PortIpAddress_Object = MibScalar
sonusH323H245PortIpAddress = _SonusH323H245PortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 3, 1),
    _SonusH323H245PortIpAddress_Type()
)
sonusH323H245PortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H245PortIpAddress.setStatus("current")


class _SonusH323H245PortShelfId_Type(Integer32):
    """Custom type sonusH323H245PortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_SonusH323H245PortShelfId_Type.__name__ = "Integer32"
_SonusH323H245PortShelfId_Object = MibScalar
sonusH323H245PortShelfId = _SonusH323H245PortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 3, 2),
    _SonusH323H245PortShelfId_Type()
)
sonusH323H245PortShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H245PortShelfId.setStatus("current")


class _SonusH323H245PortSlotNum_Type(Integer32):
    """Custom type sonusH323H245PortSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusH323H245PortSlotNum_Type.__name__ = "Integer32"
_SonusH323H245PortSlotNum_Object = MibScalar
sonusH323H245PortSlotNum = _SonusH323H245PortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 3, 3),
    _SonusH323H245PortSlotNum_Type()
)
sonusH323H245PortSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323H245PortSlotNum.setStatus("current")
_SonusH323SigControlObjects_ObjectIdentity = ObjectIdentity
sonusH323SigControlObjects = _SonusH323SigControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 4)
)


class _SonusH323SignalingControlMode_Type(SonusServiceState):
    """Custom type sonusH323SignalingControlMode based on SonusServiceState"""


_SonusH323SignalingControlMode_Object = MibScalar
sonusH323SignalingControlMode = _SonusH323SignalingControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 4, 1),
    _SonusH323SignalingControlMode_Type()
)
sonusH323SignalingControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SignalingControlMode.setStatus("current")


class _SonusH323SignalingControlState_Type(SonusAdminState):
    """Custom type sonusH323SignalingControlState based on SonusAdminState"""


_SonusH323SignalingControlState_Object = MibScalar
sonusH323SignalingControlState = _SonusH323SignalingControlState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 4, 2),
    _SonusH323SignalingControlState_Type()
)
sonusH323SignalingControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SignalingControlState.setStatus("current")


class _SonusH323SignalingControlAction_Type(Integer32):
    """Custom type sonusH323SignalingControlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dryup", 3),
          ("force", 2),
          ("none", 1))
    )


_SonusH323SignalingControlAction_Type.__name__ = "Integer32"
_SonusH323SignalingControlAction_Object = MibScalar
sonusH323SignalingControlAction = _SonusH323SignalingControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 4, 3),
    _SonusH323SignalingControlAction_Type()
)
sonusH323SignalingControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SignalingControlAction.setStatus("current")


class _SonusH323SignalingControlDryupTimeout_Type(Integer32):
    """Custom type sonusH323SignalingControlDryupTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusH323SignalingControlDryupTimeout_Type.__name__ = "Integer32"
_SonusH323SignalingControlDryupTimeout_Object = MibScalar
sonusH323SignalingControlDryupTimeout = _SonusH323SignalingControlDryupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 4, 4),
    _SonusH323SignalingControlDryupTimeout_Type()
)
sonusH323SignalingControlDryupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusH323SignalingControlDryupTimeout.setStatus("current")
_SonusH323FeObjects_ObjectIdentity = ObjectIdentity
sonusH323FeObjects = _SonusH323FeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5)
)
_SonusH323FeCurrentStatTable_Object = MibTable
sonusH323FeCurrentStatTable = _SonusH323FeCurrentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatTable.setStatus("current")
_SonusH323FeCurrentStatEntry_Object = MibTableRow
sonusH323FeCurrentStatEntry = _SonusH323FeCurrentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1)
)
sonusH323FeCurrentStatEntry.setIndexNames(
    (0, "SONUS-H323-SIGNALLING-MIB", "sonusH323FeCurrentStatIndex"),
)
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatEntry.setStatus("current")


class _SonusH323FeCurrentStatIndex_Type(Integer32):
    """Custom type sonusH323FeCurrentStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusH323FeCurrentStatIndex_Type.__name__ = "Integer32"
_SonusH323FeCurrentStatIndex_Object = MibTableColumn
sonusH323FeCurrentStatIndex = _SonusH323FeCurrentStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 1),
    _SonusH323FeCurrentStatIndex_Type()
)
sonusH323FeCurrentStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatIndex.setStatus("current")


class _SonusH323FeCurrentStatStatus_Type(Integer32):
    """Custom type sonusH323FeCurrentStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("dryup", 3),
          ("unavailable", 2))
    )


_SonusH323FeCurrentStatStatus_Type.__name__ = "Integer32"
_SonusH323FeCurrentStatStatus_Object = MibTableColumn
sonusH323FeCurrentStatStatus = _SonusH323FeCurrentStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 2),
    _SonusH323FeCurrentStatStatus_Type()
)
sonusH323FeCurrentStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatStatus.setStatus("current")
_SonusH323FeCurrentStatInCallsCompl_Type = PerfCurrentCount
_SonusH323FeCurrentStatInCallsCompl_Object = MibTableColumn
sonusH323FeCurrentStatInCallsCompl = _SonusH323FeCurrentStatInCallsCompl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 3),
    _SonusH323FeCurrentStatInCallsCompl_Type()
)
sonusH323FeCurrentStatInCallsCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatInCallsCompl.setStatus("current")
_SonusH323FeCurrentStatEgCallsCompl_Type = PerfCurrentCount
_SonusH323FeCurrentStatEgCallsCompl_Object = MibTableColumn
sonusH323FeCurrentStatEgCallsCompl = _SonusH323FeCurrentStatEgCallsCompl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 4),
    _SonusH323FeCurrentStatEgCallsCompl_Type()
)
sonusH323FeCurrentStatEgCallsCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatEgCallsCompl.setStatus("current")
_SonusH323FeCurrentStatInCallsAttemped_Type = PerfCurrentCount
_SonusH323FeCurrentStatInCallsAttemped_Object = MibTableColumn
sonusH323FeCurrentStatInCallsAttemped = _SonusH323FeCurrentStatInCallsAttemped_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 5),
    _SonusH323FeCurrentStatInCallsAttemped_Type()
)
sonusH323FeCurrentStatInCallsAttemped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatInCallsAttemped.setStatus("current")
_SonusH323FeCurrentStatEgCallsAttemped_Type = PerfCurrentCount
_SonusH323FeCurrentStatEgCallsAttemped_Object = MibTableColumn
sonusH323FeCurrentStatEgCallsAttemped = _SonusH323FeCurrentStatEgCallsAttemped_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 6),
    _SonusH323FeCurrentStatEgCallsAttemped_Type()
)
sonusH323FeCurrentStatEgCallsAttemped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatEgCallsAttemped.setStatus("current")
_SonusH323FeCurrentStatH225MsgNoSent_Type = PerfCurrentCount
_SonusH323FeCurrentStatH225MsgNoSent_Object = MibTableColumn
sonusH323FeCurrentStatH225MsgNoSent = _SonusH323FeCurrentStatH225MsgNoSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 7),
    _SonusH323FeCurrentStatH225MsgNoSent_Type()
)
sonusH323FeCurrentStatH225MsgNoSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH225MsgNoSent.setStatus("current")
_SonusH323FeCurrentStatH225MsgBytesSent_Type = PerfCurrentCount
_SonusH323FeCurrentStatH225MsgBytesSent_Object = MibTableColumn
sonusH323FeCurrentStatH225MsgBytesSent = _SonusH323FeCurrentStatH225MsgBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 8),
    _SonusH323FeCurrentStatH225MsgBytesSent_Type()
)
sonusH323FeCurrentStatH225MsgBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH225MsgBytesSent.setStatus("current")
_SonusH323FeCurrentStatH225MsgNoRcv_Type = PerfCurrentCount
_SonusH323FeCurrentStatH225MsgNoRcv_Object = MibTableColumn
sonusH323FeCurrentStatH225MsgNoRcv = _SonusH323FeCurrentStatH225MsgNoRcv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 9),
    _SonusH323FeCurrentStatH225MsgNoRcv_Type()
)
sonusH323FeCurrentStatH225MsgNoRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH225MsgNoRcv.setStatus("current")
_SonusH323FeCurrentStatH225MsgBytesRcv_Type = PerfCurrentCount
_SonusH323FeCurrentStatH225MsgBytesRcv_Object = MibTableColumn
sonusH323FeCurrentStatH225MsgBytesRcv = _SonusH323FeCurrentStatH225MsgBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 10),
    _SonusH323FeCurrentStatH225MsgBytesRcv_Type()
)
sonusH323FeCurrentStatH225MsgBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH225MsgBytesRcv.setStatus("current")
_SonusH323FeCurrentStatH245MsgNoSent_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245MsgNoSent_Object = MibTableColumn
sonusH323FeCurrentStatH245MsgNoSent = _SonusH323FeCurrentStatH245MsgNoSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 11),
    _SonusH323FeCurrentStatH245MsgNoSent_Type()
)
sonusH323FeCurrentStatH245MsgNoSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245MsgNoSent.setStatus("current")
_SonusH323FeCurrentStatH245MsgBytesSent_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245MsgBytesSent_Object = MibTableColumn
sonusH323FeCurrentStatH245MsgBytesSent = _SonusH323FeCurrentStatH245MsgBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 12),
    _SonusH323FeCurrentStatH245MsgBytesSent_Type()
)
sonusH323FeCurrentStatH245MsgBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245MsgBytesSent.setStatus("current")
_SonusH323FeCurrentStatH245MsgNoRcv_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245MsgNoRcv_Object = MibTableColumn
sonusH323FeCurrentStatH245MsgNoRcv = _SonusH323FeCurrentStatH245MsgNoRcv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 13),
    _SonusH323FeCurrentStatH245MsgNoRcv_Type()
)
sonusH323FeCurrentStatH245MsgNoRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245MsgNoRcv.setStatus("current")
_SonusH323FeCurrentStatH245MsgBytesRcv_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245MsgBytesRcv_Object = MibTableColumn
sonusH323FeCurrentStatH245MsgBytesRcv = _SonusH323FeCurrentStatH245MsgBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 14),
    _SonusH323FeCurrentStatH245MsgBytesRcv_Type()
)
sonusH323FeCurrentStatH245MsgBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245MsgBytesRcv.setStatus("current")
_SonusH323FeCurrentStatActiveCalls_Type = PerfCurrentCount
_SonusH323FeCurrentStatActiveCalls_Object = MibTableColumn
sonusH323FeCurrentStatActiveCalls = _SonusH323FeCurrentStatActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 15),
    _SonusH323FeCurrentStatActiveCalls_Type()
)
sonusH323FeCurrentStatActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatActiveCalls.setStatus("current")
_SonusH323FeCurrentStatH225TcpPortsOpened_Type = PerfCurrentCount
_SonusH323FeCurrentStatH225TcpPortsOpened_Object = MibTableColumn
sonusH323FeCurrentStatH225TcpPortsOpened = _SonusH323FeCurrentStatH225TcpPortsOpened_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 16),
    _SonusH323FeCurrentStatH225TcpPortsOpened_Type()
)
sonusH323FeCurrentStatH225TcpPortsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH225TcpPortsOpened.setStatus("current")
_SonusH323FeCurrentStatH245TcpPortsOpened_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245TcpPortsOpened_Object = MibTableColumn
sonusH323FeCurrentStatH245TcpPortsOpened = _SonusH323FeCurrentStatH245TcpPortsOpened_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 17),
    _SonusH323FeCurrentStatH245TcpPortsOpened_Type()
)
sonusH323FeCurrentStatH245TcpPortsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245TcpPortsOpened.setStatus("current")
_SonusH323FeCurrentStatH245TcpPortsAllocated_Type = PerfCurrentCount
_SonusH323FeCurrentStatH245TcpPortsAllocated_Object = MibTableColumn
sonusH323FeCurrentStatH245TcpPortsAllocated = _SonusH323FeCurrentStatH245TcpPortsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 6, 1, 5, 1, 1, 18),
    _SonusH323FeCurrentStatH245TcpPortsAllocated_Type()
)
sonusH323FeCurrentStatH245TcpPortsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusH323FeCurrentStatH245TcpPortsAllocated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-H323-SIGNALLING-MIB",
    **{"sonusH323SignallingMIB": sonusH323SignallingMIB,
       "sonusH323SignallingMIBObjects": sonusH323SignallingMIBObjects,
       "sonusH323SigTimerObjects": sonusH323SigTimerObjects,
       "sonusH323SigSrvTimerT301": sonusH323SigSrvTimerT301,
       "sonusH323SigSrvTimerT303": sonusH323SigSrvTimerT303,
       "sonusH323SigSrvTimerT310": sonusH323SigSrvTimerT310,
       "sonusH323SigTimerEstablish": sonusH323SigTimerEstablish,
       "sonusH323SigTimerTcpConnect": sonusH323SigTimerTcpConnect,
       "sonusH323H225PortObjects": sonusH323H225PortObjects,
       "sonusH323H225PortIpAddress": sonusH323H225PortIpAddress,
       "sonusH323H225PortNum": sonusH323H225PortNum,
       "sonusH323H225PortShelfId": sonusH323H225PortShelfId,
       "sonusH323H225PortSlotNum": sonusH323H225PortSlotNum,
       "sonusH323H245PortObjects": sonusH323H245PortObjects,
       "sonusH323H245PortIpAddress": sonusH323H245PortIpAddress,
       "sonusH323H245PortShelfId": sonusH323H245PortShelfId,
       "sonusH323H245PortSlotNum": sonusH323H245PortSlotNum,
       "sonusH323SigControlObjects": sonusH323SigControlObjects,
       "sonusH323SignalingControlMode": sonusH323SignalingControlMode,
       "sonusH323SignalingControlState": sonusH323SignalingControlState,
       "sonusH323SignalingControlAction": sonusH323SignalingControlAction,
       "sonusH323SignalingControlDryupTimeout": sonusH323SignalingControlDryupTimeout,
       "sonusH323FeObjects": sonusH323FeObjects,
       "sonusH323FeCurrentStatTable": sonusH323FeCurrentStatTable,
       "sonusH323FeCurrentStatEntry": sonusH323FeCurrentStatEntry,
       "sonusH323FeCurrentStatIndex": sonusH323FeCurrentStatIndex,
       "sonusH323FeCurrentStatStatus": sonusH323FeCurrentStatStatus,
       "sonusH323FeCurrentStatInCallsCompl": sonusH323FeCurrentStatInCallsCompl,
       "sonusH323FeCurrentStatEgCallsCompl": sonusH323FeCurrentStatEgCallsCompl,
       "sonusH323FeCurrentStatInCallsAttemped": sonusH323FeCurrentStatInCallsAttemped,
       "sonusH323FeCurrentStatEgCallsAttemped": sonusH323FeCurrentStatEgCallsAttemped,
       "sonusH323FeCurrentStatH225MsgNoSent": sonusH323FeCurrentStatH225MsgNoSent,
       "sonusH323FeCurrentStatH225MsgBytesSent": sonusH323FeCurrentStatH225MsgBytesSent,
       "sonusH323FeCurrentStatH225MsgNoRcv": sonusH323FeCurrentStatH225MsgNoRcv,
       "sonusH323FeCurrentStatH225MsgBytesRcv": sonusH323FeCurrentStatH225MsgBytesRcv,
       "sonusH323FeCurrentStatH245MsgNoSent": sonusH323FeCurrentStatH245MsgNoSent,
       "sonusH323FeCurrentStatH245MsgBytesSent": sonusH323FeCurrentStatH245MsgBytesSent,
       "sonusH323FeCurrentStatH245MsgNoRcv": sonusH323FeCurrentStatH245MsgNoRcv,
       "sonusH323FeCurrentStatH245MsgBytesRcv": sonusH323FeCurrentStatH245MsgBytesRcv,
       "sonusH323FeCurrentStatActiveCalls": sonusH323FeCurrentStatActiveCalls,
       "sonusH323FeCurrentStatH225TcpPortsOpened": sonusH323FeCurrentStatH225TcpPortsOpened,
       "sonusH323FeCurrentStatH245TcpPortsOpened": sonusH323FeCurrentStatH245TcpPortsOpened,
       "sonusH323FeCurrentStatH245TcpPortsAllocated": sonusH323FeCurrentStatH245TcpPortsAllocated}
)
