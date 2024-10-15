# SNMP MIB module (H3C-POSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-POSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:08 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cPosa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92)
)
h3cPosa.setRevisions(
        ("2008-03-12 09:33",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cAppServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flow", 2),
          ("tcp", 1))
    )



class H3cAppMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("temporary", 2))
    )



class H3cPeerState(Integer32, TextualConvention):
    status = "current"
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
        *(("down", 2),
          ("kept", 4),
          ("linked", 6),
          ("linking", 5),
          ("multilink", 7),
          ("notset", 1),
          ("up", 3))
    )



class H3cTerminalAccessType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fcm", 1),
          ("flow", 2),
          ("tcp", 3))
    )



class H3cTpduChangeStrategy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changeTpduDest", 2),
          ("changeTpduSrc", 1))
    )



# MIB Managed Objects in the order of their OIDs

_H3cPosaControl_ObjectIdentity = ObjectIdentity
h3cPosaControl = _H3cPosaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1)
)


class _H3cPosaServerEnable_Type(Integer32):
    """Custom type h3cPosaServerEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_H3cPosaServerEnable_Type.__name__ = "Integer32"
_H3cPosaServerEnable_Object = MibScalar
h3cPosaServerEnable = _H3cPosaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 1),
    _H3cPosaServerEnable_Type()
)
h3cPosaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaServerEnable.setStatus("current")


class _H3cPosaFcmAnswerTimeout_Type(Integer32):
    """Custom type h3cPosaFcmAnswerTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_H3cPosaFcmAnswerTimeout_Type.__name__ = "Integer32"
_H3cPosaFcmAnswerTimeout_Object = MibScalar
h3cPosaFcmAnswerTimeout = _H3cPosaFcmAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 2),
    _H3cPosaFcmAnswerTimeout_Type()
)
h3cPosaFcmAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmAnswerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmAnswerTimeout.setUnits("milliseconds")


class _H3cPosaFcmTradeTimeout_Type(Integer32):
    """Custom type h3cPosaFcmTradeTimeout based on Integer32"""
    defaultValue = 12000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 12000000),
    )


_H3cPosaFcmTradeTimeout_Type.__name__ = "Integer32"
_H3cPosaFcmTradeTimeout_Object = MibScalar
h3cPosaFcmTradeTimeout = _H3cPosaFcmTradeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 3),
    _H3cPosaFcmTradeTimeout_Type()
)
h3cPosaFcmTradeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmTradeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmTradeTimeout.setUnits("milliseconds")


class _H3cPosaFcmIdleTimeout_Type(Integer32):
    """Custom type h3cPosaFcmIdleTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12000),
    )


_H3cPosaFcmIdleTimeout_Type.__name__ = "Integer32"
_H3cPosaFcmIdleTimeout_Object = MibScalar
h3cPosaFcmIdleTimeout = _H3cPosaFcmIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 4),
    _H3cPosaFcmIdleTimeout_Type()
)
h3cPosaFcmIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmIdleTimeout.setUnits("seconds")


class _H3cPosaSrvStateChangeTrapEnable_Type(TruthValue):
    """Custom type h3cPosaSrvStateChangeTrapEnable based on TruthValue"""


_H3cPosaSrvStateChangeTrapEnable_Object = MibScalar
h3cPosaSrvStateChangeTrapEnable = _H3cPosaSrvStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 5),
    _H3cPosaSrvStateChangeTrapEnable_Type()
)
h3cPosaSrvStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaSrvStateChangeTrapEnable.setStatus("current")


class _H3cPosaAppStateChangeTrapEnable_Type(TruthValue):
    """Custom type h3cPosaAppStateChangeTrapEnable based on TruthValue"""


_H3cPosaAppStateChangeTrapEnable_Object = MibScalar
h3cPosaAppStateChangeTrapEnable = _H3cPosaAppStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 6),
    _H3cPosaAppStateChangeTrapEnable_Type()
)
h3cPosaAppStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaAppStateChangeTrapEnable.setStatus("current")


class _H3cPosaTerminalHangUpTrapEnable_Type(TruthValue):
    """Custom type h3cPosaTerminalHangUpTrapEnable based on TruthValue"""


_H3cPosaTerminalHangUpTrapEnable_Object = MibScalar
h3cPosaTerminalHangUpTrapEnable = _H3cPosaTerminalHangUpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 7),
    _H3cPosaTerminalHangUpTrapEnable_Type()
)
h3cPosaTerminalHangUpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaTerminalHangUpTrapEnable.setStatus("current")


class _H3cPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):
    """Custom type h3cPosaFcmLnkNegoFailTrapEnable based on TruthValue"""


_H3cPosaFcmLnkNegoFailTrapEnable_Object = MibScalar
h3cPosaFcmLnkNegoFailTrapEnable = _H3cPosaFcmLnkNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 8),
    _H3cPosaFcmLnkNegoFailTrapEnable_Type()
)
h3cPosaFcmLnkNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmLnkNegoFailTrapEnable.setStatus("current")


class _H3cPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):
    """Custom type h3cPosaFcmPhyNegoFailTrapEnable based on TruthValue"""


_H3cPosaFcmPhyNegoFailTrapEnable_Object = MibScalar
h3cPosaFcmPhyNegoFailTrapEnable = _H3cPosaFcmPhyNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 1, 9),
    _H3cPosaFcmPhyNegoFailTrapEnable_Type()
)
h3cPosaFcmPhyNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmPhyNegoFailTrapEnable.setStatus("current")
_H3cPosaTables_ObjectIdentity = ObjectIdentity
h3cPosaTables = _H3cPosaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2)
)
_H3cPosaAppTable_Object = MibTable
h3cPosaAppTable = _H3cPosaAppTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPosaAppTable.setStatus("current")
_H3cPosaAppEntry_Object = MibTableRow
h3cPosaAppEntry = _H3cPosaAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1)
)
h3cPosaAppEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaAppID"),
)
if mibBuilder.loadTexts:
    h3cPosaAppEntry.setStatus("current")


class _H3cPosaAppID_Type(Integer32):
    """Custom type h3cPosaAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_H3cPosaAppID_Type.__name__ = "Integer32"
_H3cPosaAppID_Object = MibTableColumn
h3cPosaAppID = _H3cPosaAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 1),
    _H3cPosaAppID_Type()
)
h3cPosaAppID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPosaAppID.setStatus("current")


class _H3cPosaAppServiceType_Type(H3cAppServiceType):
    """Custom type h3cPosaAppServiceType based on H3cAppServiceType"""


_H3cPosaAppServiceType_Object = MibTableColumn
h3cPosaAppServiceType = _H3cPosaAppServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 2),
    _H3cPosaAppServiceType_Type()
)
h3cPosaAppServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppServiceType.setStatus("current")
_H3cPosaAppIfIndex_Type = Integer32
_H3cPosaAppIfIndex_Object = MibTableColumn
h3cPosaAppIfIndex = _H3cPosaAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 3),
    _H3cPosaAppIfIndex_Type()
)
h3cPosaAppIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppIfIndex.setStatus("current")


class _H3cPosaAppMode_Type(H3cAppMode):
    """Custom type h3cPosaAppMode based on H3cAppMode"""


_H3cPosaAppMode_Object = MibTableColumn
h3cPosaAppMode = _H3cPosaAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 4),
    _H3cPosaAppMode_Type()
)
h3cPosaAppMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppMode.setStatus("current")
_H3cPosaAppHostIPType_Type = InetAddressType
_H3cPosaAppHostIPType_Object = MibTableColumn
h3cPosaAppHostIPType = _H3cPosaAppHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 5),
    _H3cPosaAppHostIPType_Type()
)
h3cPosaAppHostIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppHostIPType.setStatus("current")
_H3cPosaAppHostIP_Type = InetAddress
_H3cPosaAppHostIP_Object = MibTableColumn
h3cPosaAppHostIP = _H3cPosaAppHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 6),
    _H3cPosaAppHostIP_Type()
)
h3cPosaAppHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppHostIP.setStatus("current")


class _H3cPosaAppHostPort_Type(Integer32):
    """Custom type h3cPosaAppHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cPosaAppHostPort_Type.__name__ = "Integer32"
_H3cPosaAppHostPort_Object = MibTableColumn
h3cPosaAppHostPort = _H3cPosaAppHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 7),
    _H3cPosaAppHostPort_Type()
)
h3cPosaAppHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppHostPort.setStatus("current")
_H3cPosaAppRouterIPType_Type = InetAddressType
_H3cPosaAppRouterIPType_Object = MibTableColumn
h3cPosaAppRouterIPType = _H3cPosaAppRouterIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 8),
    _H3cPosaAppRouterIPType_Type()
)
h3cPosaAppRouterIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppRouterIPType.setStatus("current")
_H3cPosaAppRouterIP_Type = InetAddress
_H3cPosaAppRouterIP_Object = MibTableColumn
h3cPosaAppRouterIP = _H3cPosaAppRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 9),
    _H3cPosaAppRouterIP_Type()
)
h3cPosaAppRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppRouterIP.setStatus("current")


class _H3cPosaAppKeepAliveInterval_Type(Integer32):
    """Custom type h3cPosaAppKeepAliveInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_H3cPosaAppKeepAliveInterval_Type.__name__ = "Integer32"
_H3cPosaAppKeepAliveInterval_Object = MibTableColumn
h3cPosaAppKeepAliveInterval = _H3cPosaAppKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 10),
    _H3cPosaAppKeepAliveInterval_Type()
)
h3cPosaAppKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaAppKeepAliveInterval.setUnits("seconds")


class _H3cPosaAppKeepAliveCount_Type(Integer32):
    """Custom type h3cPosaAppKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_H3cPosaAppKeepAliveCount_Type.__name__ = "Integer32"
_H3cPosaAppKeepAliveCount_Object = MibTableColumn
h3cPosaAppKeepAliveCount = _H3cPosaAppKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 11),
    _H3cPosaAppKeepAliveCount_Type()
)
h3cPosaAppKeepAliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppKeepAliveCount.setStatus("current")


class _H3cPosaAppConnectTimeout_Type(Integer32):
    """Custom type h3cPosaAppConnectTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_H3cPosaAppConnectTimeout_Type.__name__ = "Integer32"
_H3cPosaAppConnectTimeout_Object = MibTableColumn
h3cPosaAppConnectTimeout = _H3cPosaAppConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 12),
    _H3cPosaAppConnectTimeout_Type()
)
h3cPosaAppConnectTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppConnectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaAppConnectTimeout.setUnits("seconds")
_H3cPosaAppState_Type = H3cPeerState
_H3cPosaAppState_Object = MibTableColumn
h3cPosaAppState = _H3cPosaAppState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 13),
    _H3cPosaAppState_Type()
)
h3cPosaAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppState.setStatus("current")
_H3cPosaAppRowStatus_Type = RowStatus
_H3cPosaAppRowStatus_Object = MibTableColumn
h3cPosaAppRowStatus = _H3cPosaAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 14),
    _H3cPosaAppRowStatus_Type()
)
h3cPosaAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppRowStatus.setStatus("current")


class _H3cPosaAppName_Type(OctetString):
    """Custom type h3cPosaAppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cPosaAppName_Type.__name__ = "OctetString"
_H3cPosaAppName_Object = MibTableColumn
h3cPosaAppName = _H3cPosaAppName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 15),
    _H3cPosaAppName_Type()
)
h3cPosaAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaAppName.setStatus("current")


class _H3cPosaCallerIDTransEnable_Type(TruthValue):
    """Custom type h3cPosaCallerIDTransEnable based on TruthValue"""


_H3cPosaCallerIDTransEnable_Object = MibTableColumn
h3cPosaCallerIDTransEnable = _H3cPosaCallerIDTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 16),
    _H3cPosaCallerIDTransEnable_Type()
)
h3cPosaCallerIDTransEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaCallerIDTransEnable.setStatus("current")


class _H3cPosaTpduChangeStrategy_Type(H3cTpduChangeStrategy):
    """Custom type h3cPosaTpduChangeStrategy based on H3cTpduChangeStrategy"""


_H3cPosaTpduChangeStrategy_Object = MibTableColumn
h3cPosaTpduChangeStrategy = _H3cPosaTpduChangeStrategy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 1, 1, 17),
    _H3cPosaTpduChangeStrategy_Type()
)
h3cPosaTpduChangeStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTpduChangeStrategy.setStatus("current")
_H3cPosaTerminalTable_Object = MibTable
h3cPosaTerminalTable = _H3cPosaTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2)
)
if mibBuilder.loadTexts:
    h3cPosaTerminalTable.setStatus("current")
_H3cPosaTerminalEntry_Object = MibTableRow
h3cPosaTerminalEntry = _H3cPosaTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1)
)
h3cPosaTerminalEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaTerminalID"),
)
if mibBuilder.loadTexts:
    h3cPosaTerminalEntry.setStatus("current")


class _H3cPosaTerminalID_Type(Integer32):
    """Custom type h3cPosaTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cPosaTerminalID_Type.__name__ = "Integer32"
_H3cPosaTerminalID_Object = MibTableColumn
h3cPosaTerminalID = _H3cPosaTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 1),
    _H3cPosaTerminalID_Type()
)
h3cPosaTerminalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaTerminalID.setStatus("current")


class _H3cPosaTerminalAccessType_Type(H3cTerminalAccessType):
    """Custom type h3cPosaTerminalAccessType based on H3cTerminalAccessType"""


_H3cPosaTerminalAccessType_Object = MibTableColumn
h3cPosaTerminalAccessType = _H3cPosaTerminalAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 2),
    _H3cPosaTerminalAccessType_Type()
)
h3cPosaTerminalAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalAccessType.setStatus("current")
_H3cPosaTerminalIfIndex_Type = Integer32
_H3cPosaTerminalIfIndex_Object = MibTableColumn
h3cPosaTerminalIfIndex = _H3cPosaTerminalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 3),
    _H3cPosaTerminalIfIndex_Type()
)
h3cPosaTerminalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalIfIndex.setStatus("current")


class _H3cPosaTerminalTransAppID_Type(Integer32):
    """Custom type h3cPosaTerminalTransAppID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_H3cPosaTerminalTransAppID_Type.__name__ = "Integer32"
_H3cPosaTerminalTransAppID_Object = MibTableColumn
h3cPosaTerminalTransAppID = _H3cPosaTerminalTransAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 4),
    _H3cPosaTerminalTransAppID_Type()
)
h3cPosaTerminalTransAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalTransAppID.setStatus("current")


class _H3cPosaTerminalListenPort_Type(Integer32):
    """Custom type h3cPosaTerminalListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cPosaTerminalListenPort_Type.__name__ = "Integer32"
_H3cPosaTerminalListenPort_Object = MibTableColumn
h3cPosaTerminalListenPort = _H3cPosaTerminalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 5),
    _H3cPosaTerminalListenPort_Type()
)
h3cPosaTerminalListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalListenPort.setStatus("current")
_H3cPosaTerminalState_Type = H3cPeerState
_H3cPosaTerminalState_Object = MibTableColumn
h3cPosaTerminalState = _H3cPosaTerminalState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 6),
    _H3cPosaTerminalState_Type()
)
h3cPosaTerminalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalState.setStatus("current")
_H3cPosaTerminalRowStatus_Type = RowStatus
_H3cPosaTerminalRowStatus_Object = MibTableColumn
h3cPosaTerminalRowStatus = _H3cPosaTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 7),
    _H3cPosaTerminalRowStatus_Type()
)
h3cPosaTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalRowStatus.setStatus("current")


class _H3cPosaTerminalName_Type(OctetString):
    """Custom type h3cPosaTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cPosaTerminalName_Type.__name__ = "OctetString"
_H3cPosaTerminalName_Object = MibTableColumn
h3cPosaTerminalName = _H3cPosaTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 8),
    _H3cPosaTerminalName_Type()
)
h3cPosaTerminalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTerminalName.setStatus("current")
_H3cPosaTerminalCfgIfIndex_Type = Integer32
_H3cPosaTerminalCfgIfIndex_Object = MibTableColumn
h3cPosaTerminalCfgIfIndex = _H3cPosaTerminalCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 2, 1, 9),
    _H3cPosaTerminalCfgIfIndex_Type()
)
h3cPosaTerminalCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalCfgIfIndex.setStatus("current")
_H3cPosaMapTable_Object = MibTable
h3cPosaMapTable = _H3cPosaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3)
)
if mibBuilder.loadTexts:
    h3cPosaMapTable.setStatus("current")
_H3cPosaMapEntry_Object = MibTableRow
h3cPosaMapEntry = _H3cPosaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3, 1)
)
h3cPosaMapEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaMapSrcCode"),
    (0, "H3C-POSA-MIB", "h3cPosaMapDestCode"),
)
if mibBuilder.loadTexts:
    h3cPosaMapEntry.setStatus("current")


class _H3cPosaMapDestCode_Type(OctetString):
    """Custom type h3cPosaMapDestCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_H3cPosaMapDestCode_Type.__name__ = "OctetString"
_H3cPosaMapDestCode_Object = MibTableColumn
h3cPosaMapDestCode = _H3cPosaMapDestCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3, 1, 1),
    _H3cPosaMapDestCode_Type()
)
h3cPosaMapDestCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaMapDestCode.setStatus("current")


class _H3cPosaMapAppID_Type(Integer32):
    """Custom type h3cPosaMapAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_H3cPosaMapAppID_Type.__name__ = "Integer32"
_H3cPosaMapAppID_Object = MibTableColumn
h3cPosaMapAppID = _H3cPosaMapAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3, 1, 2),
    _H3cPosaMapAppID_Type()
)
h3cPosaMapAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaMapAppID.setStatus("current")
_H3cPosaMapRowStatus_Type = RowStatus
_H3cPosaMapRowStatus_Object = MibTableColumn
h3cPosaMapRowStatus = _H3cPosaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3, 1, 3),
    _H3cPosaMapRowStatus_Type()
)
h3cPosaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaMapRowStatus.setStatus("current")


class _H3cPosaMapSrcCode_Type(OctetString):
    """Custom type h3cPosaMapSrcCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_H3cPosaMapSrcCode_Type.__name__ = "OctetString"
_H3cPosaMapSrcCode_Object = MibTableColumn
h3cPosaMapSrcCode = _H3cPosaMapSrcCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 3, 1, 4),
    _H3cPosaMapSrcCode_Type()
)
h3cPosaMapSrcCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaMapSrcCode.setStatus("current")
_H3cPosaFcmStatTable_Object = MibTable
h3cPosaFcmStatTable = _H3cPosaFcmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 4)
)
if mibBuilder.loadTexts:
    h3cPosaFcmStatTable.setStatus("current")
_H3cPosaFcmStatEntry_Object = MibTableRow
h3cPosaFcmStatEntry = _H3cPosaFcmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 4, 1)
)
h3cPosaFcmStatEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaFcmStatIfIndex"),
)
if mibBuilder.loadTexts:
    h3cPosaFcmStatEntry.setStatus("current")


class _H3cPosaFcmStatIfIndex_Type(Integer32):
    """Custom type h3cPosaFcmStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPosaFcmStatIfIndex_Type.__name__ = "Integer32"
_H3cPosaFcmStatIfIndex_Object = MibTableColumn
h3cPosaFcmStatIfIndex = _H3cPosaFcmStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 4, 1, 1),
    _H3cPosaFcmStatIfIndex_Type()
)
h3cPosaFcmStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaFcmStatIfIndex.setStatus("current")
_H3cPosaFcmStatTimeoutCnts_Type = Counter32
_H3cPosaFcmStatTimeoutCnts_Object = MibTableColumn
h3cPosaFcmStatTimeoutCnts = _H3cPosaFcmStatTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 4, 1, 2),
    _H3cPosaFcmStatTimeoutCnts_Type()
)
h3cPosaFcmStatTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaFcmStatTimeoutCnts.setStatus("current")
_H3cPosaFcmStatConnectFailCnts_Type = Counter32
_H3cPosaFcmStatConnectFailCnts_Object = MibTableColumn
h3cPosaFcmStatConnectFailCnts = _H3cPosaFcmStatConnectFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 4, 1, 3),
    _H3cPosaFcmStatConnectFailCnts_Type()
)
h3cPosaFcmStatConnectFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaFcmStatConnectFailCnts.setStatus("current")
_H3cPosaAppStatTable_Object = MibTable
h3cPosaAppStatTable = _H3cPosaAppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5)
)
if mibBuilder.loadTexts:
    h3cPosaAppStatTable.setStatus("current")
_H3cPosaAppStatEntry_Object = MibTableRow
h3cPosaAppStatEntry = _H3cPosaAppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1)
)
h3cPosaAppStatEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaAppID"),
)
if mibBuilder.loadTexts:
    h3cPosaAppStatEntry.setStatus("current")
_H3cPosaAppRecvPkts_Type = Counter32
_H3cPosaAppRecvPkts_Object = MibTableColumn
h3cPosaAppRecvPkts = _H3cPosaAppRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 1),
    _H3cPosaAppRecvPkts_Type()
)
h3cPosaAppRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppRecvPkts.setStatus("current")
_H3cPosaAppSendPkts_Type = Counter32
_H3cPosaAppSendPkts_Object = MibTableColumn
h3cPosaAppSendPkts = _H3cPosaAppSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 2),
    _H3cPosaAppSendPkts_Type()
)
h3cPosaAppSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppSendPkts.setStatus("current")
_H3cPosaAppErrPkts_Type = Counter32
_H3cPosaAppErrPkts_Object = MibTableColumn
h3cPosaAppErrPkts = _H3cPosaAppErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 3),
    _H3cPosaAppErrPkts_Type()
)
h3cPosaAppErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppErrPkts.setStatus("current")
_H3cPosaAppDistributeErrCnts_Type = Counter32
_H3cPosaAppDistributeErrCnts_Object = MibTableColumn
h3cPosaAppDistributeErrCnts = _H3cPosaAppDistributeErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 4),
    _H3cPosaAppDistributeErrCnts_Type()
)
h3cPosaAppDistributeErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppDistributeErrCnts.setStatus("current")
_H3cPosaAppInDiscardedPkts_Type = Counter32
_H3cPosaAppInDiscardedPkts_Object = MibTableColumn
h3cPosaAppInDiscardedPkts = _H3cPosaAppInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 5),
    _H3cPosaAppInDiscardedPkts_Type()
)
h3cPosaAppInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppInDiscardedPkts.setStatus("current")
_H3cPosaAppOutDiscardedPkts_Type = Counter32
_H3cPosaAppOutDiscardedPkts_Object = MibTableColumn
h3cPosaAppOutDiscardedPkts = _H3cPosaAppOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 5, 1, 6),
    _H3cPosaAppOutDiscardedPkts_Type()
)
h3cPosaAppOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaAppOutDiscardedPkts.setStatus("current")
_H3cPosaTerminalStatTable_Object = MibTable
h3cPosaTerminalStatTable = _H3cPosaTerminalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6)
)
if mibBuilder.loadTexts:
    h3cPosaTerminalStatTable.setStatus("current")
_H3cPosaTerminalStatEntry_Object = MibTableRow
h3cPosaTerminalStatEntry = _H3cPosaTerminalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1)
)
h3cPosaTerminalStatEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaTerminalID"),
)
if mibBuilder.loadTexts:
    h3cPosaTerminalStatEntry.setStatus("current")
_H3cPosaTerminalRecvPkts_Type = Counter32
_H3cPosaTerminalRecvPkts_Object = MibTableColumn
h3cPosaTerminalRecvPkts = _H3cPosaTerminalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 1),
    _H3cPosaTerminalRecvPkts_Type()
)
h3cPosaTerminalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalRecvPkts.setStatus("current")
_H3cPosaTerminalSendPkts_Type = Counter32
_H3cPosaTerminalSendPkts_Object = MibTableColumn
h3cPosaTerminalSendPkts = _H3cPosaTerminalSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 2),
    _H3cPosaTerminalSendPkts_Type()
)
h3cPosaTerminalSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalSendPkts.setStatus("current")
_H3cPosaTerminalErrPkts_Type = Counter32
_H3cPosaTerminalErrPkts_Object = MibTableColumn
h3cPosaTerminalErrPkts = _H3cPosaTerminalErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 3),
    _H3cPosaTerminalErrPkts_Type()
)
h3cPosaTerminalErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalErrPkts.setStatus("current")
_H3cPosaTerminalMapErrCnts_Type = Counter32
_H3cPosaTerminalMapErrCnts_Object = MibTableColumn
h3cPosaTerminalMapErrCnts = _H3cPosaTerminalMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 4),
    _H3cPosaTerminalMapErrCnts_Type()
)
h3cPosaTerminalMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalMapErrCnts.setStatus("current")
_H3cPosaTerminalInDiscardedPkts_Type = Counter32
_H3cPosaTerminalInDiscardedPkts_Object = MibTableColumn
h3cPosaTerminalInDiscardedPkts = _H3cPosaTerminalInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 5),
    _H3cPosaTerminalInDiscardedPkts_Type()
)
h3cPosaTerminalInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalInDiscardedPkts.setStatus("current")
_H3cPosaTerminalOutDiscardedPkts_Type = Counter32
_H3cPosaTerminalOutDiscardedPkts_Object = MibTableColumn
h3cPosaTerminalOutDiscardedPkts = _H3cPosaTerminalOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 6, 1, 6),
    _H3cPosaTerminalOutDiscardedPkts_Type()
)
h3cPosaTerminalOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTerminalOutDiscardedPkts.setStatus("current")
_H3cPosaBatchTerminalTable_Object = MibTable
h3cPosaBatchTerminalTable = _H3cPosaBatchTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 7)
)
if mibBuilder.loadTexts:
    h3cPosaBatchTerminalTable.setStatus("current")
_H3cPosaBatchTerminalEntry_Object = MibTableRow
h3cPosaBatchTerminalEntry = _H3cPosaBatchTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 7, 1)
)
h3cPosaBatchTerminalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cPosaBatchTerminalEntry.setStatus("current")


class _H3cPosaBatchTerminalFirstID_Type(Integer32):
    """Custom type h3cPosaBatchTerminalFirstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cPosaBatchTerminalFirstID_Type.__name__ = "Integer32"
_H3cPosaBatchTerminalFirstID_Object = MibTableColumn
h3cPosaBatchTerminalFirstID = _H3cPosaBatchTerminalFirstID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 7, 1, 1),
    _H3cPosaBatchTerminalFirstID_Type()
)
h3cPosaBatchTerminalFirstID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaBatchTerminalFirstID.setStatus("current")
_H3cPosaBatchTerminalRowStatus_Type = RowStatus
_H3cPosaBatchTerminalRowStatus_Object = MibTableColumn
h3cPosaBatchTerminalRowStatus = _H3cPosaBatchTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 7, 1, 2),
    _H3cPosaBatchTerminalRowStatus_Type()
)
h3cPosaBatchTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaBatchTerminalRowStatus.setStatus("current")
_H3cPosaTcpTermStatTable_Object = MibTable
h3cPosaTcpTermStatTable = _H3cPosaTcpTermStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8)
)
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatTable.setStatus("current")
_H3cPosaTcpTermStatEntry_Object = MibTableRow
h3cPosaTcpTermStatEntry = _H3cPosaTcpTermStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1)
)
h3cPosaTcpTermStatEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaTcpTermStatIndex"),
)
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatEntry.setStatus("current")


class _H3cPosaTcpTermStatIndex_Type(Integer32):
    """Custom type h3cPosaTcpTermStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cPosaTcpTermStatIndex_Type.__name__ = "Integer32"
_H3cPosaTcpTermStatIndex_Object = MibTableColumn
h3cPosaTcpTermStatIndex = _H3cPosaTcpTermStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 1),
    _H3cPosaTcpTermStatIndex_Type()
)
h3cPosaTcpTermStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatIndex.setStatus("current")
_H3cPosaTcpTermStatIPType_Type = InetAddressType
_H3cPosaTcpTermStatIPType_Object = MibTableColumn
h3cPosaTcpTermStatIPType = _H3cPosaTcpTermStatIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 2),
    _H3cPosaTcpTermStatIPType_Type()
)
h3cPosaTcpTermStatIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatIPType.setStatus("current")
_H3cPosaTcpTermStatIP_Type = InetAddress
_H3cPosaTcpTermStatIP_Object = MibTableColumn
h3cPosaTcpTermStatIP = _H3cPosaTcpTermStatIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 3),
    _H3cPosaTcpTermStatIP_Type()
)
h3cPosaTcpTermStatIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatIP.setStatus("current")
_H3cPosaTcpTermStatIPMask_Type = InetAddress
_H3cPosaTcpTermStatIPMask_Object = MibTableColumn
h3cPosaTcpTermStatIPMask = _H3cPosaTcpTermStatIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 4),
    _H3cPosaTcpTermStatIPMask_Type()
)
h3cPosaTcpTermStatIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatIPMask.setStatus("current")
_H3cPosaTcpTermRecvPkts_Type = Counter64
_H3cPosaTcpTermRecvPkts_Object = MibTableColumn
h3cPosaTcpTermRecvPkts = _H3cPosaTcpTermRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 5),
    _H3cPosaTcpTermRecvPkts_Type()
)
h3cPosaTcpTermRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermRecvPkts.setStatus("current")
_H3cPosaTcpTermSendPkts_Type = Counter64
_H3cPosaTcpTermSendPkts_Object = MibTableColumn
h3cPosaTcpTermSendPkts = _H3cPosaTcpTermSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 6),
    _H3cPosaTcpTermSendPkts_Type()
)
h3cPosaTcpTermSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermSendPkts.setStatus("current")
_H3cPosaTcpTermErrPkts_Type = Counter64
_H3cPosaTcpTermErrPkts_Object = MibTableColumn
h3cPosaTcpTermErrPkts = _H3cPosaTcpTermErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 7),
    _H3cPosaTcpTermErrPkts_Type()
)
h3cPosaTcpTermErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermErrPkts.setStatus("current")
_H3cPosaTcpTermMapErrCnts_Type = Counter64
_H3cPosaTcpTermMapErrCnts_Object = MibTableColumn
h3cPosaTcpTermMapErrCnts = _H3cPosaTcpTermMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 8),
    _H3cPosaTcpTermMapErrCnts_Type()
)
h3cPosaTcpTermMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermMapErrCnts.setStatus("current")
_H3cPosaTcpTermInDiscardedPkts_Type = Counter64
_H3cPosaTcpTermInDiscardedPkts_Object = MibTableColumn
h3cPosaTcpTermInDiscardedPkts = _H3cPosaTcpTermInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 9),
    _H3cPosaTcpTermInDiscardedPkts_Type()
)
h3cPosaTcpTermInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermInDiscardedPkts.setStatus("current")
_H3cPosaTcpTermOutDiscardedPkts_Type = Counter64
_H3cPosaTcpTermOutDiscardedPkts_Object = MibTableColumn
h3cPosaTcpTermOutDiscardedPkts = _H3cPosaTcpTermOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 10),
    _H3cPosaTcpTermOutDiscardedPkts_Type()
)
h3cPosaTcpTermOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaTcpTermOutDiscardedPkts.setStatus("current")
_H3cPosaTcpTermStatRowStatus_Type = RowStatus
_H3cPosaTcpTermStatRowStatus_Object = MibTableColumn
h3cPosaTcpTermStatRowStatus = _H3cPosaTcpTermStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 8, 1, 11),
    _H3cPosaTcpTermStatRowStatus_Type()
)
h3cPosaTcpTermStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaTcpTermStatRowStatus.setStatus("current")
_H3cPosaFcmConfTable_Object = MibTable
h3cPosaFcmConfTable = _H3cPosaFcmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9)
)
if mibBuilder.loadTexts:
    h3cPosaFcmConfTable.setStatus("current")
_H3cPosaFcmConfEntry_Object = MibTableRow
h3cPosaFcmConfEntry = _H3cPosaFcmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1)
)
h3cPosaFcmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cPosaFcmConfEntry.setStatus("current")


class _H3cPosaFcmNegoHookOff_Type(Integer32):
    """Custom type h3cPosaFcmNegoHookOff based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 6000),
    )


_H3cPosaFcmNegoHookOff_Type.__name__ = "Integer32"
_H3cPosaFcmNegoHookOff_Object = MibTableColumn
h3cPosaFcmNegoHookOff = _H3cPosaFcmNegoHookOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 1),
    _H3cPosaFcmNegoHookOff_Type()
)
h3cPosaFcmNegoHookOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoHookOff.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoHookOff.setUnits("milliseconds")


class _H3cPosaFcmNegoSilence_Type(Integer32):
    """Custom type h3cPosaFcmNegoSilence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_H3cPosaFcmNegoSilence_Type.__name__ = "Integer32"
_H3cPosaFcmNegoSilence_Object = MibTableColumn
h3cPosaFcmNegoSilence = _H3cPosaFcmNegoSilence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 2),
    _H3cPosaFcmNegoSilence_Type()
)
h3cPosaFcmNegoSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoSilence.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoSilence.setUnits("milliseconds")


class _H3cPosaFcmNegoScrmbBinary1_Type(Integer32):
    """Custom type h3cPosaFcmNegoScrmbBinary1 based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_H3cPosaFcmNegoScrmbBinary1_Type.__name__ = "Integer32"
_H3cPosaFcmNegoScrmbBinary1_Object = MibTableColumn
h3cPosaFcmNegoScrmbBinary1 = _H3cPosaFcmNegoScrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 3),
    _H3cPosaFcmNegoScrmbBinary1_Type()
)
h3cPosaFcmNegoScrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoScrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoScrmbBinary1.setUnits("milliseconds")


class _H3cPosaFcmNegoUnscrmbBinary1_Type(Integer32):
    """Custom type h3cPosaFcmNegoUnscrmbBinary1 based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1500),
    )


_H3cPosaFcmNegoUnscrmbBinary1_Type.__name__ = "Integer32"
_H3cPosaFcmNegoUnscrmbBinary1_Object = MibTableColumn
h3cPosaFcmNegoUnscrmbBinary1 = _H3cPosaFcmNegoUnscrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 4),
    _H3cPosaFcmNegoUnscrmbBinary1_Type()
)
h3cPosaFcmNegoUnscrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoUnscrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmNegoUnscrmbBinary1.setUnits("milliseconds")


class _H3cPosaFcmThresholdRlsdOff_Type(Integer32):
    """Custom type h3cPosaFcmThresholdRlsdOff based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_H3cPosaFcmThresholdRlsdOff_Type.__name__ = "Integer32"
_H3cPosaFcmThresholdRlsdOff_Object = MibTableColumn
h3cPosaFcmThresholdRlsdOff = _H3cPosaFcmThresholdRlsdOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 5),
    _H3cPosaFcmThresholdRlsdOff_Type()
)
h3cPosaFcmThresholdRlsdOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdRlsdOff.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdRlsdOff.setUnits("-dBm")


class _H3cPosaFcmThresholdRlsdOn_Type(Integer32):
    """Custom type h3cPosaFcmThresholdRlsdOn based on Integer32"""
    defaultValue = 43

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_H3cPosaFcmThresholdRlsdOn_Type.__name__ = "Integer32"
_H3cPosaFcmThresholdRlsdOn_Object = MibTableColumn
h3cPosaFcmThresholdRlsdOn = _H3cPosaFcmThresholdRlsdOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 6),
    _H3cPosaFcmThresholdRlsdOn_Type()
)
h3cPosaFcmThresholdRlsdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdRlsdOn.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdRlsdOn.setUnits("-dBm")


class _H3cPosaFcmThresholdTxPower_Type(Integer32):
    """Custom type h3cPosaFcmThresholdTxPower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_H3cPosaFcmThresholdTxPower_Type.__name__ = "Integer32"
_H3cPosaFcmThresholdTxPower_Object = MibTableColumn
h3cPosaFcmThresholdTxPower = _H3cPosaFcmThresholdTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 7),
    _H3cPosaFcmThresholdTxPower_Type()
)
h3cPosaFcmThresholdTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdTxPower.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdTxPower.setUnits("-dBm")


class _H3cPosaFcmThresholdAnswerTone_Type(Integer32):
    """Custom type h3cPosaFcmThresholdAnswerTone based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_H3cPosaFcmThresholdAnswerTone_Type.__name__ = "Integer32"
_H3cPosaFcmThresholdAnswerTone_Object = MibTableColumn
h3cPosaFcmThresholdAnswerTone = _H3cPosaFcmThresholdAnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 9, 1, 8),
    _H3cPosaFcmThresholdAnswerTone_Type()
)
h3cPosaFcmThresholdAnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdAnswerTone.setStatus("current")
if mibBuilder.loadTexts:
    h3cPosaFcmThresholdAnswerTone.setUnits("-dBm")
_H3cPosaCallerStatTable_Object = MibTable
h3cPosaCallerStatTable = _H3cPosaCallerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10)
)
if mibBuilder.loadTexts:
    h3cPosaCallerStatTable.setStatus("current")
_H3cPosaCallerStatEntry_Object = MibTableRow
h3cPosaCallerStatEntry = _H3cPosaCallerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1)
)
h3cPosaCallerStatEntry.setIndexNames(
    (0, "H3C-POSA-MIB", "h3cPosaCallerStatCallerID"),
)
if mibBuilder.loadTexts:
    h3cPosaCallerStatEntry.setStatus("current")


class _H3cPosaCallerStatCallerID_Type(OctetString):
    """Custom type h3cPosaCallerStatCallerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cPosaCallerStatCallerID_Type.__name__ = "OctetString"
_H3cPosaCallerStatCallerID_Object = MibTableColumn
h3cPosaCallerStatCallerID = _H3cPosaCallerStatCallerID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 1),
    _H3cPosaCallerStatCallerID_Type()
)
h3cPosaCallerStatCallerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPosaCallerStatCallerID.setStatus("current")
_H3cPosaCallerRecvPkts_Type = Counter64
_H3cPosaCallerRecvPkts_Object = MibTableColumn
h3cPosaCallerRecvPkts = _H3cPosaCallerRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 2),
    _H3cPosaCallerRecvPkts_Type()
)
h3cPosaCallerRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerRecvPkts.setStatus("current")
_H3cPosaCallerSendPkts_Type = Counter64
_H3cPosaCallerSendPkts_Object = MibTableColumn
h3cPosaCallerSendPkts = _H3cPosaCallerSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 3),
    _H3cPosaCallerSendPkts_Type()
)
h3cPosaCallerSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerSendPkts.setStatus("current")
_H3cPosaCallerErrPkts_Type = Counter64
_H3cPosaCallerErrPkts_Object = MibTableColumn
h3cPosaCallerErrPkts = _H3cPosaCallerErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 4),
    _H3cPosaCallerErrPkts_Type()
)
h3cPosaCallerErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerErrPkts.setStatus("current")
_H3cPosaCallerMapErrCnts_Type = Counter64
_H3cPosaCallerMapErrCnts_Object = MibTableColumn
h3cPosaCallerMapErrCnts = _H3cPosaCallerMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 5),
    _H3cPosaCallerMapErrCnts_Type()
)
h3cPosaCallerMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerMapErrCnts.setStatus("current")
_H3cPosaCallerInDiscardedPkts_Type = Counter64
_H3cPosaCallerInDiscardedPkts_Object = MibTableColumn
h3cPosaCallerInDiscardedPkts = _H3cPosaCallerInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 6),
    _H3cPosaCallerInDiscardedPkts_Type()
)
h3cPosaCallerInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerInDiscardedPkts.setStatus("current")
_H3cPosaCallerOutDiscardedPkts_Type = Counter64
_H3cPosaCallerOutDiscardedPkts_Object = MibTableColumn
h3cPosaCallerOutDiscardedPkts = _H3cPosaCallerOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 7),
    _H3cPosaCallerOutDiscardedPkts_Type()
)
h3cPosaCallerOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPosaCallerOutDiscardedPkts.setStatus("current")
_H3cPosaCallerStatRowStatus_Type = RowStatus
_H3cPosaCallerStatRowStatus_Object = MibTableColumn
h3cPosaCallerStatRowStatus = _H3cPosaCallerStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 2, 10, 1, 8),
    _H3cPosaCallerStatRowStatus_Type()
)
h3cPosaCallerStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPosaCallerStatRowStatus.setStatus("current")
_H3cPosaTrap_ObjectIdentity = ObjectIdentity
h3cPosaTrap = _H3cPosaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3)
)
_H3cPosaTrapPrex_ObjectIdentity = ObjectIdentity
h3cPosaTrapPrex = _H3cPosaTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0)
)
_H3cPosaTrapObjects_ObjectIdentity = ObjectIdentity
h3cPosaTrapObjects = _H3cPosaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 1)
)


class _H3cPosaAppStateChangeObject_Type(Integer32):
    """Custom type h3cPosaAppStateChangeObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_H3cPosaAppStateChangeObject_Type.__name__ = "Integer32"
_H3cPosaAppStateChangeObject_Object = MibScalar
h3cPosaAppStateChangeObject = _H3cPosaAppStateChangeObject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 1, 1),
    _H3cPosaAppStateChangeObject_Type()
)
h3cPosaAppStateChangeObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPosaAppStateChangeObject.setStatus("current")

# Managed Objects groups


# Notification objects

h3cPosaServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0, 1)
)
h3cPosaServerStatusChange.setObjects(
    ("H3C-POSA-MIB", "h3cPosaServerEnable")
)
if mibBuilder.loadTexts:
    h3cPosaServerStatusChange.setStatus(
        "current"
    )

h3cPosaAppStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0, 2)
)
h3cPosaAppStateChange.setObjects(
      *(("H3C-POSA-MIB", "h3cPosaAppID"),
        ("H3C-POSA-MIB", "h3cPosaAppStateChangeObject"))
)
if mibBuilder.loadTexts:
    h3cPosaAppStateChange.setStatus(
        "current"
    )

h3cPosaTerminalHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0, 3)
)
h3cPosaTerminalHangUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosaTerminalHangUp.setStatus(
        "current"
    )

h3cPosaFcmLinkNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0, 4)
)
h3cPosaFcmLinkNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosaFcmLinkNegoFailed.setStatus(
        "current"
    )

h3cPosaFcmPhyNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 92, 3, 0, 5)
)
h3cPosaFcmPhyNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cPosaFcmPhyNegoFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-POSA-MIB",
    **{"H3cAppServiceType": H3cAppServiceType,
       "H3cAppMode": H3cAppMode,
       "H3cPeerState": H3cPeerState,
       "H3cTerminalAccessType": H3cTerminalAccessType,
       "H3cTpduChangeStrategy": H3cTpduChangeStrategy,
       "h3cPosa": h3cPosa,
       "h3cPosaControl": h3cPosaControl,
       "h3cPosaServerEnable": h3cPosaServerEnable,
       "h3cPosaFcmAnswerTimeout": h3cPosaFcmAnswerTimeout,
       "h3cPosaFcmTradeTimeout": h3cPosaFcmTradeTimeout,
       "h3cPosaFcmIdleTimeout": h3cPosaFcmIdleTimeout,
       "h3cPosaSrvStateChangeTrapEnable": h3cPosaSrvStateChangeTrapEnable,
       "h3cPosaAppStateChangeTrapEnable": h3cPosaAppStateChangeTrapEnable,
       "h3cPosaTerminalHangUpTrapEnable": h3cPosaTerminalHangUpTrapEnable,
       "h3cPosaFcmLnkNegoFailTrapEnable": h3cPosaFcmLnkNegoFailTrapEnable,
       "h3cPosaFcmPhyNegoFailTrapEnable": h3cPosaFcmPhyNegoFailTrapEnable,
       "h3cPosaTables": h3cPosaTables,
       "h3cPosaAppTable": h3cPosaAppTable,
       "h3cPosaAppEntry": h3cPosaAppEntry,
       "h3cPosaAppID": h3cPosaAppID,
       "h3cPosaAppServiceType": h3cPosaAppServiceType,
       "h3cPosaAppIfIndex": h3cPosaAppIfIndex,
       "h3cPosaAppMode": h3cPosaAppMode,
       "h3cPosaAppHostIPType": h3cPosaAppHostIPType,
       "h3cPosaAppHostIP": h3cPosaAppHostIP,
       "h3cPosaAppHostPort": h3cPosaAppHostPort,
       "h3cPosaAppRouterIPType": h3cPosaAppRouterIPType,
       "h3cPosaAppRouterIP": h3cPosaAppRouterIP,
       "h3cPosaAppKeepAliveInterval": h3cPosaAppKeepAliveInterval,
       "h3cPosaAppKeepAliveCount": h3cPosaAppKeepAliveCount,
       "h3cPosaAppConnectTimeout": h3cPosaAppConnectTimeout,
       "h3cPosaAppState": h3cPosaAppState,
       "h3cPosaAppRowStatus": h3cPosaAppRowStatus,
       "h3cPosaAppName": h3cPosaAppName,
       "h3cPosaCallerIDTransEnable": h3cPosaCallerIDTransEnable,
       "h3cPosaTpduChangeStrategy": h3cPosaTpduChangeStrategy,
       "h3cPosaTerminalTable": h3cPosaTerminalTable,
       "h3cPosaTerminalEntry": h3cPosaTerminalEntry,
       "h3cPosaTerminalID": h3cPosaTerminalID,
       "h3cPosaTerminalAccessType": h3cPosaTerminalAccessType,
       "h3cPosaTerminalIfIndex": h3cPosaTerminalIfIndex,
       "h3cPosaTerminalTransAppID": h3cPosaTerminalTransAppID,
       "h3cPosaTerminalListenPort": h3cPosaTerminalListenPort,
       "h3cPosaTerminalState": h3cPosaTerminalState,
       "h3cPosaTerminalRowStatus": h3cPosaTerminalRowStatus,
       "h3cPosaTerminalName": h3cPosaTerminalName,
       "h3cPosaTerminalCfgIfIndex": h3cPosaTerminalCfgIfIndex,
       "h3cPosaMapTable": h3cPosaMapTable,
       "h3cPosaMapEntry": h3cPosaMapEntry,
       "h3cPosaMapDestCode": h3cPosaMapDestCode,
       "h3cPosaMapAppID": h3cPosaMapAppID,
       "h3cPosaMapRowStatus": h3cPosaMapRowStatus,
       "h3cPosaMapSrcCode": h3cPosaMapSrcCode,
       "h3cPosaFcmStatTable": h3cPosaFcmStatTable,
       "h3cPosaFcmStatEntry": h3cPosaFcmStatEntry,
       "h3cPosaFcmStatIfIndex": h3cPosaFcmStatIfIndex,
       "h3cPosaFcmStatTimeoutCnts": h3cPosaFcmStatTimeoutCnts,
       "h3cPosaFcmStatConnectFailCnts": h3cPosaFcmStatConnectFailCnts,
       "h3cPosaAppStatTable": h3cPosaAppStatTable,
       "h3cPosaAppStatEntry": h3cPosaAppStatEntry,
       "h3cPosaAppRecvPkts": h3cPosaAppRecvPkts,
       "h3cPosaAppSendPkts": h3cPosaAppSendPkts,
       "h3cPosaAppErrPkts": h3cPosaAppErrPkts,
       "h3cPosaAppDistributeErrCnts": h3cPosaAppDistributeErrCnts,
       "h3cPosaAppInDiscardedPkts": h3cPosaAppInDiscardedPkts,
       "h3cPosaAppOutDiscardedPkts": h3cPosaAppOutDiscardedPkts,
       "h3cPosaTerminalStatTable": h3cPosaTerminalStatTable,
       "h3cPosaTerminalStatEntry": h3cPosaTerminalStatEntry,
       "h3cPosaTerminalRecvPkts": h3cPosaTerminalRecvPkts,
       "h3cPosaTerminalSendPkts": h3cPosaTerminalSendPkts,
       "h3cPosaTerminalErrPkts": h3cPosaTerminalErrPkts,
       "h3cPosaTerminalMapErrCnts": h3cPosaTerminalMapErrCnts,
       "h3cPosaTerminalInDiscardedPkts": h3cPosaTerminalInDiscardedPkts,
       "h3cPosaTerminalOutDiscardedPkts": h3cPosaTerminalOutDiscardedPkts,
       "h3cPosaBatchTerminalTable": h3cPosaBatchTerminalTable,
       "h3cPosaBatchTerminalEntry": h3cPosaBatchTerminalEntry,
       "h3cPosaBatchTerminalFirstID": h3cPosaBatchTerminalFirstID,
       "h3cPosaBatchTerminalRowStatus": h3cPosaBatchTerminalRowStatus,
       "h3cPosaTcpTermStatTable": h3cPosaTcpTermStatTable,
       "h3cPosaTcpTermStatEntry": h3cPosaTcpTermStatEntry,
       "h3cPosaTcpTermStatIndex": h3cPosaTcpTermStatIndex,
       "h3cPosaTcpTermStatIPType": h3cPosaTcpTermStatIPType,
       "h3cPosaTcpTermStatIP": h3cPosaTcpTermStatIP,
       "h3cPosaTcpTermStatIPMask": h3cPosaTcpTermStatIPMask,
       "h3cPosaTcpTermRecvPkts": h3cPosaTcpTermRecvPkts,
       "h3cPosaTcpTermSendPkts": h3cPosaTcpTermSendPkts,
       "h3cPosaTcpTermErrPkts": h3cPosaTcpTermErrPkts,
       "h3cPosaTcpTermMapErrCnts": h3cPosaTcpTermMapErrCnts,
       "h3cPosaTcpTermInDiscardedPkts": h3cPosaTcpTermInDiscardedPkts,
       "h3cPosaTcpTermOutDiscardedPkts": h3cPosaTcpTermOutDiscardedPkts,
       "h3cPosaTcpTermStatRowStatus": h3cPosaTcpTermStatRowStatus,
       "h3cPosaFcmConfTable": h3cPosaFcmConfTable,
       "h3cPosaFcmConfEntry": h3cPosaFcmConfEntry,
       "h3cPosaFcmNegoHookOff": h3cPosaFcmNegoHookOff,
       "h3cPosaFcmNegoSilence": h3cPosaFcmNegoSilence,
       "h3cPosaFcmNegoScrmbBinary1": h3cPosaFcmNegoScrmbBinary1,
       "h3cPosaFcmNegoUnscrmbBinary1": h3cPosaFcmNegoUnscrmbBinary1,
       "h3cPosaFcmThresholdRlsdOff": h3cPosaFcmThresholdRlsdOff,
       "h3cPosaFcmThresholdRlsdOn": h3cPosaFcmThresholdRlsdOn,
       "h3cPosaFcmThresholdTxPower": h3cPosaFcmThresholdTxPower,
       "h3cPosaFcmThresholdAnswerTone": h3cPosaFcmThresholdAnswerTone,
       "h3cPosaCallerStatTable": h3cPosaCallerStatTable,
       "h3cPosaCallerStatEntry": h3cPosaCallerStatEntry,
       "h3cPosaCallerStatCallerID": h3cPosaCallerStatCallerID,
       "h3cPosaCallerRecvPkts": h3cPosaCallerRecvPkts,
       "h3cPosaCallerSendPkts": h3cPosaCallerSendPkts,
       "h3cPosaCallerErrPkts": h3cPosaCallerErrPkts,
       "h3cPosaCallerMapErrCnts": h3cPosaCallerMapErrCnts,
       "h3cPosaCallerInDiscardedPkts": h3cPosaCallerInDiscardedPkts,
       "h3cPosaCallerOutDiscardedPkts": h3cPosaCallerOutDiscardedPkts,
       "h3cPosaCallerStatRowStatus": h3cPosaCallerStatRowStatus,
       "h3cPosaTrap": h3cPosaTrap,
       "h3cPosaTrapPrex": h3cPosaTrapPrex,
       "h3cPosaServerStatusChange": h3cPosaServerStatusChange,
       "h3cPosaAppStateChange": h3cPosaAppStateChange,
       "h3cPosaTerminalHangUp": h3cPosaTerminalHangUp,
       "h3cPosaFcmLinkNegoFailed": h3cPosaFcmLinkNegoFailed,
       "h3cPosaFcmPhyNegoFailed": h3cPosaFcmPhyNegoFailed,
       "h3cPosaTrapObjects": h3cPosaTrapObjects,
       "h3cPosaAppStateChangeObject": h3cPosaAppStateChangeObject}
)
