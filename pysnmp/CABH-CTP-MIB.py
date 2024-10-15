# SNMP MIB module (CABH-CTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-CTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:00 2024
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cabhCtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhCtpObjects_ObjectIdentity = ObjectIdentity
cabhCtpObjects = _CabhCtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1)
)
_CabhCtpBase_ObjectIdentity = ObjectIdentity
cabhCtpBase = _CabhCtpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 1)
)
_CabhCtpSetToFactory_Type = TruthValue
_CabhCtpSetToFactory_Object = MibScalar
cabhCtpSetToFactory = _CabhCtpSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 1, 1),
    _CabhCtpSetToFactory_Type()
)
cabhCtpSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpSetToFactory.setStatus("current")
_CabhCtpConnSpeed_ObjectIdentity = ObjectIdentity
cabhCtpConnSpeed = _CabhCtpConnSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2)
)


class _CabhCtpConnSrcIpType_Type(InetAddressType):
    """Custom type cabhCtpConnSrcIpType based on InetAddressType"""


_CabhCtpConnSrcIpType_Object = MibScalar
cabhCtpConnSrcIpType = _CabhCtpConnSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 1),
    _CabhCtpConnSrcIpType_Type()
)
cabhCtpConnSrcIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnSrcIpType.setStatus("current")


class _CabhCtpConnSrcIp_Type(InetAddress):
    """Custom type cabhCtpConnSrcIp based on InetAddress"""
    defaultHexValue = "c0a80001"


_CabhCtpConnSrcIp_Object = MibScalar
cabhCtpConnSrcIp = _CabhCtpConnSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 2),
    _CabhCtpConnSrcIp_Type()
)
cabhCtpConnSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnSrcIp.setStatus("current")


class _CabhCtpConnDestIpType_Type(InetAddressType):
    """Custom type cabhCtpConnDestIpType based on InetAddressType"""


_CabhCtpConnDestIpType_Object = MibScalar
cabhCtpConnDestIpType = _CabhCtpConnDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 3),
    _CabhCtpConnDestIpType_Type()
)
cabhCtpConnDestIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnDestIpType.setStatus("current")
_CabhCtpConnDestIp_Type = InetAddress
_CabhCtpConnDestIp_Object = MibScalar
cabhCtpConnDestIp = _CabhCtpConnDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 4),
    _CabhCtpConnDestIp_Type()
)
cabhCtpConnDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnDestIp.setStatus("current")


class _CabhCtpConnProto_Type(Integer32):
    """Custom type cabhCtpConnProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )


_CabhCtpConnProto_Type.__name__ = "Integer32"
_CabhCtpConnProto_Object = MibScalar
cabhCtpConnProto = _CabhCtpConnProto_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 5),
    _CabhCtpConnProto_Type()
)
cabhCtpConnProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnProto.setStatus("current")


class _CabhCtpConnNumPkts_Type(Integer32):
    """Custom type cabhCtpConnNumPkts based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhCtpConnNumPkts_Type.__name__ = "Integer32"
_CabhCtpConnNumPkts_Object = MibScalar
cabhCtpConnNumPkts = _CabhCtpConnNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 6),
    _CabhCtpConnNumPkts_Type()
)
cabhCtpConnNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnNumPkts.setStatus("current")


class _CabhCtpConnPktSize_Type(Integer32):
    """Custom type cabhCtpConnPktSize based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_CabhCtpConnPktSize_Type.__name__ = "Integer32"
_CabhCtpConnPktSize_Object = MibScalar
cabhCtpConnPktSize = _CabhCtpConnPktSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 7),
    _CabhCtpConnPktSize_Type()
)
cabhCtpConnPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnPktSize.setStatus("current")


class _CabhCtpConnTimeOut_Type(Integer32):
    """Custom type cabhCtpConnTimeOut based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpConnTimeOut_Type.__name__ = "Integer32"
_CabhCtpConnTimeOut_Object = MibScalar
cabhCtpConnTimeOut = _CabhCtpConnTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 8),
    _CabhCtpConnTimeOut_Type()
)
cabhCtpConnTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpConnTimeOut.setUnits("milliseconds")


class _CabhCtpConnControl_Type(Integer32):
    """Custom type cabhCtpConnControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("start", 1))
    )


_CabhCtpConnControl_Type.__name__ = "Integer32"
_CabhCtpConnControl_Object = MibScalar
cabhCtpConnControl = _CabhCtpConnControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 9),
    _CabhCtpConnControl_Type()
)
cabhCtpConnControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpConnControl.setStatus("current")


class _CabhCtpConnStatus_Type(Integer32):
    """Custom type cabhCtpConnStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("complete", 3),
          ("notRun", 1),
          ("running", 2),
          ("timedOut", 5))
    )


_CabhCtpConnStatus_Type.__name__ = "Integer32"
_CabhCtpConnStatus_Object = MibScalar
cabhCtpConnStatus = _CabhCtpConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 10),
    _CabhCtpConnStatus_Type()
)
cabhCtpConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpConnStatus.setStatus("current")


class _CabhCtpConnPktsSent_Type(Integer32):
    """Custom type cabhCtpConnPktsSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhCtpConnPktsSent_Type.__name__ = "Integer32"
_CabhCtpConnPktsSent_Object = MibScalar
cabhCtpConnPktsSent = _CabhCtpConnPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 11),
    _CabhCtpConnPktsSent_Type()
)
cabhCtpConnPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpConnPktsSent.setStatus("current")


class _CabhCtpConnPktsRecv_Type(Integer32):
    """Custom type cabhCtpConnPktsRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhCtpConnPktsRecv_Type.__name__ = "Integer32"
_CabhCtpConnPktsRecv_Object = MibScalar
cabhCtpConnPktsRecv = _CabhCtpConnPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 12),
    _CabhCtpConnPktsRecv_Type()
)
cabhCtpConnPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpConnPktsRecv.setStatus("current")


class _CabhCtpConnRTT_Type(Integer32):
    """Custom type cabhCtpConnRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpConnRTT_Type.__name__ = "Integer32"
_CabhCtpConnRTT_Object = MibScalar
cabhCtpConnRTT = _CabhCtpConnRTT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 13),
    _CabhCtpConnRTT_Type()
)
cabhCtpConnRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpConnRTT.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpConnRTT.setUnits("millisec")


class _CabhCtpConnThroughput_Type(Integer32):
    """Custom type cabhCtpConnThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CabhCtpConnThroughput_Type.__name__ = "Integer32"
_CabhCtpConnThroughput_Object = MibScalar
cabhCtpConnThroughput = _CabhCtpConnThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 2, 14),
    _CabhCtpConnThroughput_Type()
)
cabhCtpConnThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpConnThroughput.setStatus("current")
_CabhCtpPing_ObjectIdentity = ObjectIdentity
cabhCtpPing = _CabhCtpPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3)
)


class _CabhCtpPingSrcIpType_Type(InetAddressType):
    """Custom type cabhCtpPingSrcIpType based on InetAddressType"""


_CabhCtpPingSrcIpType_Object = MibScalar
cabhCtpPingSrcIpType = _CabhCtpPingSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 1),
    _CabhCtpPingSrcIpType_Type()
)
cabhCtpPingSrcIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingSrcIpType.setStatus("current")


class _CabhCtpPingSrcIp_Type(InetAddress):
    """Custom type cabhCtpPingSrcIp based on InetAddress"""
    defaultHexValue = "c0a80001"


_CabhCtpPingSrcIp_Object = MibScalar
cabhCtpPingSrcIp = _CabhCtpPingSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 2),
    _CabhCtpPingSrcIp_Type()
)
cabhCtpPingSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingSrcIp.setStatus("current")


class _CabhCtpPingDestIpType_Type(InetAddressType):
    """Custom type cabhCtpPingDestIpType based on InetAddressType"""


_CabhCtpPingDestIpType_Object = MibScalar
cabhCtpPingDestIpType = _CabhCtpPingDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 3),
    _CabhCtpPingDestIpType_Type()
)
cabhCtpPingDestIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingDestIpType.setStatus("current")
_CabhCtpPingDestIp_Type = InetAddress
_CabhCtpPingDestIp_Object = MibScalar
cabhCtpPingDestIp = _CabhCtpPingDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 4),
    _CabhCtpPingDestIp_Type()
)
cabhCtpPingDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingDestIp.setStatus("current")


class _CabhCtpPingNumPkts_Type(Integer32):
    """Custom type cabhCtpPingNumPkts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CabhCtpPingNumPkts_Type.__name__ = "Integer32"
_CabhCtpPingNumPkts_Object = MibScalar
cabhCtpPingNumPkts = _CabhCtpPingNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 5),
    _CabhCtpPingNumPkts_Type()
)
cabhCtpPingNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingNumPkts.setStatus("current")


class _CabhCtpPingPktSize_Type(Integer32):
    """Custom type cabhCtpPingPktSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_CabhCtpPingPktSize_Type.__name__ = "Integer32"
_CabhCtpPingPktSize_Object = MibScalar
cabhCtpPingPktSize = _CabhCtpPingPktSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 6),
    _CabhCtpPingPktSize_Type()
)
cabhCtpPingPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingPktSize.setStatus("current")


class _CabhCtpPingTimeBetween_Type(Integer32):
    """Custom type cabhCtpPingTimeBetween based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpPingTimeBetween_Type.__name__ = "Integer32"
_CabhCtpPingTimeBetween_Object = MibScalar
cabhCtpPingTimeBetween = _CabhCtpPingTimeBetween_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 7),
    _CabhCtpPingTimeBetween_Type()
)
cabhCtpPingTimeBetween.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingTimeBetween.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpPingTimeBetween.setUnits("milliseconds")


class _CabhCtpPingTimeOut_Type(Integer32):
    """Custom type cabhCtpPingTimeOut based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_CabhCtpPingTimeOut_Type.__name__ = "Integer32"
_CabhCtpPingTimeOut_Object = MibScalar
cabhCtpPingTimeOut = _CabhCtpPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 8),
    _CabhCtpPingTimeOut_Type()
)
cabhCtpPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpPingTimeOut.setUnits("milliseconds")


class _CabhCtpPingControl_Type(Integer32):
    """Custom type cabhCtpPingControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("start", 1))
    )


_CabhCtpPingControl_Type.__name__ = "Integer32"
_CabhCtpPingControl_Object = MibScalar
cabhCtpPingControl = _CabhCtpPingControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 9),
    _CabhCtpPingControl_Type()
)
cabhCtpPingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhCtpPingControl.setStatus("current")


class _CabhCtpPingStatus_Type(Integer32):
    """Custom type cabhCtpPingStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("complete", 3),
          ("notRun", 1),
          ("running", 2),
          ("timedOut", 5))
    )


_CabhCtpPingStatus_Type.__name__ = "Integer32"
_CabhCtpPingStatus_Object = MibScalar
cabhCtpPingStatus = _CabhCtpPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 10),
    _CabhCtpPingStatus_Type()
)
cabhCtpPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingStatus.setStatus("current")


class _CabhCtpPingNumSent_Type(Integer32):
    """Custom type cabhCtpPingNumSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CabhCtpPingNumSent_Type.__name__ = "Integer32"
_CabhCtpPingNumSent_Object = MibScalar
cabhCtpPingNumSent = _CabhCtpPingNumSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 11),
    _CabhCtpPingNumSent_Type()
)
cabhCtpPingNumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingNumSent.setStatus("current")


class _CabhCtpPingNumRecv_Type(Integer32):
    """Custom type cabhCtpPingNumRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhCtpPingNumRecv_Type.__name__ = "Integer32"
_CabhCtpPingNumRecv_Object = MibScalar
cabhCtpPingNumRecv = _CabhCtpPingNumRecv_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 12),
    _CabhCtpPingNumRecv_Type()
)
cabhCtpPingNumRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingNumRecv.setStatus("current")


class _CabhCtpPingAvgRTT_Type(Integer32):
    """Custom type cabhCtpPingAvgRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpPingAvgRTT_Type.__name__ = "Integer32"
_CabhCtpPingAvgRTT_Object = MibScalar
cabhCtpPingAvgRTT = _CabhCtpPingAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 13),
    _CabhCtpPingAvgRTT_Type()
)
cabhCtpPingAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpPingAvgRTT.setUnits("millisec")


class _CabhCtpPingMaxRTT_Type(Integer32):
    """Custom type cabhCtpPingMaxRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpPingMaxRTT_Type.__name__ = "Integer32"
_CabhCtpPingMaxRTT_Object = MibScalar
cabhCtpPingMaxRTT = _CabhCtpPingMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 14),
    _CabhCtpPingMaxRTT_Type()
)
cabhCtpPingMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpPingMaxRTT.setUnits("millisec")


class _CabhCtpPingMinRTT_Type(Integer32):
    """Custom type cabhCtpPingMinRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CabhCtpPingMinRTT_Type.__name__ = "Integer32"
_CabhCtpPingMinRTT_Object = MibScalar
cabhCtpPingMinRTT = _CabhCtpPingMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 15),
    _CabhCtpPingMinRTT_Type()
)
cabhCtpPingMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    cabhCtpPingMinRTT.setUnits("millisec")


class _CabhCtpPingNumIcmpError_Type(Integer32):
    """Custom type cabhCtpPingNumIcmpError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhCtpPingNumIcmpError_Type.__name__ = "Integer32"
_CabhCtpPingNumIcmpError_Object = MibScalar
cabhCtpPingNumIcmpError = _CabhCtpPingNumIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 16),
    _CabhCtpPingNumIcmpError_Type()
)
cabhCtpPingNumIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingNumIcmpError.setStatus("current")


class _CabhCtpPingIcmpError_Type(Integer32):
    """Custom type cabhCtpPingIcmpError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhCtpPingIcmpError_Type.__name__ = "Integer32"
_CabhCtpPingIcmpError_Object = MibScalar
cabhCtpPingIcmpError = _CabhCtpPingIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 1, 3, 17),
    _CabhCtpPingIcmpError_Type()
)
cabhCtpPingIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhCtpPingIcmpError.setStatus("current")
_CabhCtpNotification_ObjectIdentity = ObjectIdentity
cabhCtpNotification = _CabhCtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 2, 0)
)
_CabhCtpConformance_ObjectIdentity = ObjectIdentity
cabhCtpConformance = _CabhCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3)
)
_CabhCtpCompliances_ObjectIdentity = ObjectIdentity
cabhCtpCompliances = _CabhCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 1)
)
_CabhCtpGroups_ObjectIdentity = ObjectIdentity
cabhCtpGroups = _CabhCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 2)
)

# Managed Objects groups

cabhCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 2, 1)
)
cabhCtpGroup.setObjects(
      *(("CABH-CTP-MIB", "cabhCtpSetToFactory"),
        ("CABH-CTP-MIB", "cabhCtpConnSrcIpType"),
        ("CABH-CTP-MIB", "cabhCtpConnSrcIp"),
        ("CABH-CTP-MIB", "cabhCtpConnDestIpType"),
        ("CABH-CTP-MIB", "cabhCtpConnDestIp"),
        ("CABH-CTP-MIB", "cabhCtpConnProto"),
        ("CABH-CTP-MIB", "cabhCtpConnNumPkts"),
        ("CABH-CTP-MIB", "cabhCtpConnPktSize"),
        ("CABH-CTP-MIB", "cabhCtpConnTimeOut"),
        ("CABH-CTP-MIB", "cabhCtpConnControl"),
        ("CABH-CTP-MIB", "cabhCtpConnStatus"),
        ("CABH-CTP-MIB", "cabhCtpConnPktsSent"),
        ("CABH-CTP-MIB", "cabhCtpConnPktsRecv"),
        ("CABH-CTP-MIB", "cabhCtpConnRTT"),
        ("CABH-CTP-MIB", "cabhCtpConnThroughput"),
        ("CABH-CTP-MIB", "cabhCtpPingSrcIpType"),
        ("CABH-CTP-MIB", "cabhCtpPingSrcIp"),
        ("CABH-CTP-MIB", "cabhCtpPingDestIpType"),
        ("CABH-CTP-MIB", "cabhCtpPingDestIp"),
        ("CABH-CTP-MIB", "cabhCtpPingNumPkts"),
        ("CABH-CTP-MIB", "cabhCtpPingPktSize"),
        ("CABH-CTP-MIB", "cabhCtpPingTimeBetween"),
        ("CABH-CTP-MIB", "cabhCtpPingTimeOut"),
        ("CABH-CTP-MIB", "cabhCtpPingControl"),
        ("CABH-CTP-MIB", "cabhCtpPingStatus"),
        ("CABH-CTP-MIB", "cabhCtpPingNumSent"),
        ("CABH-CTP-MIB", "cabhCtpPingNumRecv"),
        ("CABH-CTP-MIB", "cabhCtpPingAvgRTT"),
        ("CABH-CTP-MIB", "cabhCtpPingMinRTT"),
        ("CABH-CTP-MIB", "cabhCtpPingMaxRTT"),
        ("CABH-CTP-MIB", "cabhCtpPingNumIcmpError"),
        ("CABH-CTP-MIB", "cabhCtpPingIcmpError"))
)
if mibBuilder.loadTexts:
    cabhCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhCtpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cabhCtpBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-CTP-MIB",
    **{"cabhCtpMib": cabhCtpMib,
       "cabhCtpObjects": cabhCtpObjects,
       "cabhCtpBase": cabhCtpBase,
       "cabhCtpSetToFactory": cabhCtpSetToFactory,
       "cabhCtpConnSpeed": cabhCtpConnSpeed,
       "cabhCtpConnSrcIpType": cabhCtpConnSrcIpType,
       "cabhCtpConnSrcIp": cabhCtpConnSrcIp,
       "cabhCtpConnDestIpType": cabhCtpConnDestIpType,
       "cabhCtpConnDestIp": cabhCtpConnDestIp,
       "cabhCtpConnProto": cabhCtpConnProto,
       "cabhCtpConnNumPkts": cabhCtpConnNumPkts,
       "cabhCtpConnPktSize": cabhCtpConnPktSize,
       "cabhCtpConnTimeOut": cabhCtpConnTimeOut,
       "cabhCtpConnControl": cabhCtpConnControl,
       "cabhCtpConnStatus": cabhCtpConnStatus,
       "cabhCtpConnPktsSent": cabhCtpConnPktsSent,
       "cabhCtpConnPktsRecv": cabhCtpConnPktsRecv,
       "cabhCtpConnRTT": cabhCtpConnRTT,
       "cabhCtpConnThroughput": cabhCtpConnThroughput,
       "cabhCtpPing": cabhCtpPing,
       "cabhCtpPingSrcIpType": cabhCtpPingSrcIpType,
       "cabhCtpPingSrcIp": cabhCtpPingSrcIp,
       "cabhCtpPingDestIpType": cabhCtpPingDestIpType,
       "cabhCtpPingDestIp": cabhCtpPingDestIp,
       "cabhCtpPingNumPkts": cabhCtpPingNumPkts,
       "cabhCtpPingPktSize": cabhCtpPingPktSize,
       "cabhCtpPingTimeBetween": cabhCtpPingTimeBetween,
       "cabhCtpPingTimeOut": cabhCtpPingTimeOut,
       "cabhCtpPingControl": cabhCtpPingControl,
       "cabhCtpPingStatus": cabhCtpPingStatus,
       "cabhCtpPingNumSent": cabhCtpPingNumSent,
       "cabhCtpPingNumRecv": cabhCtpPingNumRecv,
       "cabhCtpPingAvgRTT": cabhCtpPingAvgRTT,
       "cabhCtpPingMaxRTT": cabhCtpPingMaxRTT,
       "cabhCtpPingMinRTT": cabhCtpPingMinRTT,
       "cabhCtpPingNumIcmpError": cabhCtpPingNumIcmpError,
       "cabhCtpPingIcmpError": cabhCtpPingIcmpError,
       "cabhCtpNotification": cabhCtpNotification,
       "cabhCtpConformance": cabhCtpConformance,
       "cabhCtpCompliances": cabhCtpCompliances,
       "cabhCtpBasicCompliance": cabhCtpBasicCompliance,
       "cabhCtpGroups": cabhCtpGroups,
       "cabhCtpGroup": cabhCtpGroup}
)
