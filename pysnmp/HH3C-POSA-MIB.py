# SNMP MIB module (HH3C-POSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-POSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:30 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cPosa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92)
)
hh3cPosa.setRevisions(
        ("2014-05-29 00:00",
         "2008-03-12 09:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cAppServiceType(Integer32, TextualConvention):
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



class Hh3cAppMode(Integer32, TextualConvention):
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



class Hh3cPeerState(Integer32, TextualConvention):
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 8),
          ("down", 2),
          ("error", 9),
          ("kept", 4),
          ("linked", 6),
          ("linking", 5),
          ("multilink", 7),
          ("notset", 1),
          ("up", 3))
    )



class Hh3cTerminalAccessType(Integer32, TextualConvention):
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



class Hh3cTpduChangeStrategy(Integer32, TextualConvention):
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

_Hh3cPosaControl_ObjectIdentity = ObjectIdentity
hh3cPosaControl = _Hh3cPosaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1)
)


class _Hh3cPosaServerEnable_Type(Integer32):
    """Custom type hh3cPosaServerEnable based on Integer32"""
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


_Hh3cPosaServerEnable_Type.__name__ = "Integer32"
_Hh3cPosaServerEnable_Object = MibScalar
hh3cPosaServerEnable = _Hh3cPosaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 1),
    _Hh3cPosaServerEnable_Type()
)
hh3cPosaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaServerEnable.setStatus("current")


class _Hh3cPosaFcmAnswerTimeout_Type(Integer32):
    """Custom type hh3cPosaFcmAnswerTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_Hh3cPosaFcmAnswerTimeout_Type.__name__ = "Integer32"
_Hh3cPosaFcmAnswerTimeout_Object = MibScalar
hh3cPosaFcmAnswerTimeout = _Hh3cPosaFcmAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 2),
    _Hh3cPosaFcmAnswerTimeout_Type()
)
hh3cPosaFcmAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmAnswerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmAnswerTimeout.setUnits("milliseconds")


class _Hh3cPosaFcmTradeTimeout_Type(Integer32):
    """Custom type hh3cPosaFcmTradeTimeout based on Integer32"""
    defaultValue = 12000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 12000000),
    )


_Hh3cPosaFcmTradeTimeout_Type.__name__ = "Integer32"
_Hh3cPosaFcmTradeTimeout_Object = MibScalar
hh3cPosaFcmTradeTimeout = _Hh3cPosaFcmTradeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 3),
    _Hh3cPosaFcmTradeTimeout_Type()
)
hh3cPosaFcmTradeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmTradeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmTradeTimeout.setUnits("milliseconds")


class _Hh3cPosaFcmIdleTimeout_Type(Integer32):
    """Custom type hh3cPosaFcmIdleTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12000),
    )


_Hh3cPosaFcmIdleTimeout_Type.__name__ = "Integer32"
_Hh3cPosaFcmIdleTimeout_Object = MibScalar
hh3cPosaFcmIdleTimeout = _Hh3cPosaFcmIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 4),
    _Hh3cPosaFcmIdleTimeout_Type()
)
hh3cPosaFcmIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmIdleTimeout.setUnits("seconds")


class _Hh3cPosaSrvStateChangeTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaSrvStateChangeTrapEnable based on TruthValue"""


_Hh3cPosaSrvStateChangeTrapEnable_Object = MibScalar
hh3cPosaSrvStateChangeTrapEnable = _Hh3cPosaSrvStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 5),
    _Hh3cPosaSrvStateChangeTrapEnable_Type()
)
hh3cPosaSrvStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaSrvStateChangeTrapEnable.setStatus("current")


class _Hh3cPosaAppStateChangeTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaAppStateChangeTrapEnable based on TruthValue"""


_Hh3cPosaAppStateChangeTrapEnable_Object = MibScalar
hh3cPosaAppStateChangeTrapEnable = _Hh3cPosaAppStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 6),
    _Hh3cPosaAppStateChangeTrapEnable_Type()
)
hh3cPosaAppStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaAppStateChangeTrapEnable.setStatus("current")


class _Hh3cPosaTerminalHangUpTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaTerminalHangUpTrapEnable based on TruthValue"""


_Hh3cPosaTerminalHangUpTrapEnable_Object = MibScalar
hh3cPosaTerminalHangUpTrapEnable = _Hh3cPosaTerminalHangUpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 7),
    _Hh3cPosaTerminalHangUpTrapEnable_Type()
)
hh3cPosaTerminalHangUpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTerminalHangUpTrapEnable.setStatus("current")


class _Hh3cPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaFcmLnkNegoFailTrapEnable based on TruthValue"""


_Hh3cPosaFcmLnkNegoFailTrapEnable_Object = MibScalar
hh3cPosaFcmLnkNegoFailTrapEnable = _Hh3cPosaFcmLnkNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 8),
    _Hh3cPosaFcmLnkNegoFailTrapEnable_Type()
)
hh3cPosaFcmLnkNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmLnkNegoFailTrapEnable.setStatus("current")


class _Hh3cPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaFcmPhyNegoFailTrapEnable based on TruthValue"""


_Hh3cPosaFcmPhyNegoFailTrapEnable_Object = MibScalar
hh3cPosaFcmPhyNegoFailTrapEnable = _Hh3cPosaFcmPhyNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 9),
    _Hh3cPosaFcmPhyNegoFailTrapEnable_Type()
)
hh3cPosaFcmPhyNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmPhyNegoFailTrapEnable.setStatus("current")
_Hh3cPosaTcpConnectionNumber_Type = Integer32
_Hh3cPosaTcpConnectionNumber_Object = MibScalar
hh3cPosaTcpConnectionNumber = _Hh3cPosaTcpConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 10),
    _Hh3cPosaTcpConnectionNumber_Type()
)
hh3cPosaTcpConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpConnectionNumber.setStatus("current")
_Hh3cPosaFcmConnectionNumber_Type = Integer32
_Hh3cPosaFcmConnectionNumber_Object = MibScalar
hh3cPosaFcmConnectionNumber = _Hh3cPosaFcmConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 11),
    _Hh3cPosaFcmConnectionNumber_Type()
)
hh3cPosaFcmConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaFcmConnectionNumber.setStatus("current")


class _Hh3cPosaTcpConnectionThreshold_Type(Integer32):
    """Custom type hh3cPosaTcpConnectionThreshold based on Integer32"""
    defaultValue = 4096


_Hh3cPosaTcpConnectionThreshold_Object = MibScalar
hh3cPosaTcpConnectionThreshold = _Hh3cPosaTcpConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 12),
    _Hh3cPosaTcpConnectionThreshold_Type()
)
hh3cPosaTcpConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTcpConnectionThreshold.setStatus("current")


class _Hh3cPosaFcmConnectionThreshold_Type(Integer32):
    """Custom type hh3cPosaFcmConnectionThreshold based on Integer32"""
    defaultValue = 255


_Hh3cPosaFcmConnectionThreshold_Object = MibScalar
hh3cPosaFcmConnectionThreshold = _Hh3cPosaFcmConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 13),
    _Hh3cPosaFcmConnectionThreshold_Type()
)
hh3cPosaFcmConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmConnectionThreshold.setStatus("current")


class _Hh3cPosaTcpConnectionTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaTcpConnectionTrapEnable based on TruthValue"""


_Hh3cPosaTcpConnectionTrapEnable_Object = MibScalar
hh3cPosaTcpConnectionTrapEnable = _Hh3cPosaTcpConnectionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 14),
    _Hh3cPosaTcpConnectionTrapEnable_Type()
)
hh3cPosaTcpConnectionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTcpConnectionTrapEnable.setStatus("current")


class _Hh3cPosaFcmConnectionTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaFcmConnectionTrapEnable based on TruthValue"""


_Hh3cPosaFcmConnectionTrapEnable_Object = MibScalar
hh3cPosaFcmConnectionTrapEnable = _Hh3cPosaFcmConnectionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 15),
    _Hh3cPosaFcmConnectionTrapEnable_Type()
)
hh3cPosaFcmConnectionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmConnectionTrapEnable.setStatus("current")


class _Hh3cPosaTcpTradeLimit_Type(Integer32):
    """Custom type hh3cPosaTcpTradeLimit based on Integer32"""
    defaultValue = 0


_Hh3cPosaTcpTradeLimit_Object = MibScalar
hh3cPosaTcpTradeLimit = _Hh3cPosaTcpTradeLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 16),
    _Hh3cPosaTcpTradeLimit_Type()
)
hh3cPosaTcpTradeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTcpTradeLimit.setStatus("current")


class _Hh3cPosaTcpTradeTrapEnable_Type(TruthValue):
    """Custom type hh3cPosaTcpTradeTrapEnable based on TruthValue"""


_Hh3cPosaTcpTradeTrapEnable_Object = MibScalar
hh3cPosaTcpTradeTrapEnable = _Hh3cPosaTcpTradeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 17),
    _Hh3cPosaTcpTradeTrapEnable_Type()
)
hh3cPosaTcpTradeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTcpTradeTrapEnable.setStatus("current")


class _Hh3cPosaTcpTradeTimeout_Type(Integer32):
    """Custom type hh3cPosaTcpTradeTimeout based on Integer32"""
    defaultValue = 240


_Hh3cPosaTcpTradeTimeout_Object = MibScalar
hh3cPosaTcpTradeTimeout = _Hh3cPosaTcpTradeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 1, 18),
    _Hh3cPosaTcpTradeTimeout_Type()
)
hh3cPosaTcpTradeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaTcpTradeTimeout.setStatus("current")
_Hh3cPosaTables_ObjectIdentity = ObjectIdentity
hh3cPosaTables = _Hh3cPosaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2)
)
_Hh3cPosaAppTable_Object = MibTable
hh3cPosaAppTable = _Hh3cPosaAppTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPosaAppTable.setStatus("current")
_Hh3cPosaAppEntry_Object = MibTableRow
hh3cPosaAppEntry = _Hh3cPosaAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1)
)
hh3cPosaAppEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaAppID"),
)
if mibBuilder.loadTexts:
    hh3cPosaAppEntry.setStatus("current")


class _Hh3cPosaAppID_Type(Integer32):
    """Custom type hh3cPosaAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cPosaAppID_Type.__name__ = "Integer32"
_Hh3cPosaAppID_Object = MibTableColumn
hh3cPosaAppID = _Hh3cPosaAppID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 1),
    _Hh3cPosaAppID_Type()
)
hh3cPosaAppID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPosaAppID.setStatus("current")


class _Hh3cPosaAppServiceType_Type(Hh3cAppServiceType):
    """Custom type hh3cPosaAppServiceType based on Hh3cAppServiceType"""


_Hh3cPosaAppServiceType_Object = MibTableColumn
hh3cPosaAppServiceType = _Hh3cPosaAppServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 2),
    _Hh3cPosaAppServiceType_Type()
)
hh3cPosaAppServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppServiceType.setStatus("current")
_Hh3cPosaAppIfIndex_Type = Integer32
_Hh3cPosaAppIfIndex_Object = MibTableColumn
hh3cPosaAppIfIndex = _Hh3cPosaAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 3),
    _Hh3cPosaAppIfIndex_Type()
)
hh3cPosaAppIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppIfIndex.setStatus("current")


class _Hh3cPosaAppMode_Type(Hh3cAppMode):
    """Custom type hh3cPosaAppMode based on Hh3cAppMode"""


_Hh3cPosaAppMode_Object = MibTableColumn
hh3cPosaAppMode = _Hh3cPosaAppMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 4),
    _Hh3cPosaAppMode_Type()
)
hh3cPosaAppMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppMode.setStatus("current")
_Hh3cPosaAppHostIPType_Type = InetAddressType
_Hh3cPosaAppHostIPType_Object = MibTableColumn
hh3cPosaAppHostIPType = _Hh3cPosaAppHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 5),
    _Hh3cPosaAppHostIPType_Type()
)
hh3cPosaAppHostIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppHostIPType.setStatus("current")
_Hh3cPosaAppHostIP_Type = InetAddress
_Hh3cPosaAppHostIP_Object = MibTableColumn
hh3cPosaAppHostIP = _Hh3cPosaAppHostIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 6),
    _Hh3cPosaAppHostIP_Type()
)
hh3cPosaAppHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppHostIP.setStatus("current")


class _Hh3cPosaAppHostPort_Type(Integer32):
    """Custom type hh3cPosaAppHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPosaAppHostPort_Type.__name__ = "Integer32"
_Hh3cPosaAppHostPort_Object = MibTableColumn
hh3cPosaAppHostPort = _Hh3cPosaAppHostPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 7),
    _Hh3cPosaAppHostPort_Type()
)
hh3cPosaAppHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppHostPort.setStatus("current")
_Hh3cPosaAppRouterIPType_Type = InetAddressType
_Hh3cPosaAppRouterIPType_Object = MibTableColumn
hh3cPosaAppRouterIPType = _Hh3cPosaAppRouterIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 8),
    _Hh3cPosaAppRouterIPType_Type()
)
hh3cPosaAppRouterIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppRouterIPType.setStatus("current")
_Hh3cPosaAppRouterIP_Type = InetAddress
_Hh3cPosaAppRouterIP_Object = MibTableColumn
hh3cPosaAppRouterIP = _Hh3cPosaAppRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 9),
    _Hh3cPosaAppRouterIP_Type()
)
hh3cPosaAppRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppRouterIP.setStatus("current")


class _Hh3cPosaAppKeepAliveInterval_Type(Integer32):
    """Custom type hh3cPosaAppKeepAliveInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_Hh3cPosaAppKeepAliveInterval_Type.__name__ = "Integer32"
_Hh3cPosaAppKeepAliveInterval_Object = MibTableColumn
hh3cPosaAppKeepAliveInterval = _Hh3cPosaAppKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 10),
    _Hh3cPosaAppKeepAliveInterval_Type()
)
hh3cPosaAppKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaAppKeepAliveInterval.setUnits("seconds")


class _Hh3cPosaAppKeepAliveCount_Type(Integer32):
    """Custom type hh3cPosaAppKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_Hh3cPosaAppKeepAliveCount_Type.__name__ = "Integer32"
_Hh3cPosaAppKeepAliveCount_Object = MibTableColumn
hh3cPosaAppKeepAliveCount = _Hh3cPosaAppKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 11),
    _Hh3cPosaAppKeepAliveCount_Type()
)
hh3cPosaAppKeepAliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppKeepAliveCount.setStatus("current")


class _Hh3cPosaAppConnectTimeout_Type(Integer32):
    """Custom type hh3cPosaAppConnectTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cPosaAppConnectTimeout_Type.__name__ = "Integer32"
_Hh3cPosaAppConnectTimeout_Object = MibTableColumn
hh3cPosaAppConnectTimeout = _Hh3cPosaAppConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 12),
    _Hh3cPosaAppConnectTimeout_Type()
)
hh3cPosaAppConnectTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppConnectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaAppConnectTimeout.setUnits("seconds")
_Hh3cPosaAppState_Type = Hh3cPeerState
_Hh3cPosaAppState_Object = MibTableColumn
hh3cPosaAppState = _Hh3cPosaAppState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 13),
    _Hh3cPosaAppState_Type()
)
hh3cPosaAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppState.setStatus("current")
_Hh3cPosaAppRowStatus_Type = RowStatus
_Hh3cPosaAppRowStatus_Object = MibTableColumn
hh3cPosaAppRowStatus = _Hh3cPosaAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 14),
    _Hh3cPosaAppRowStatus_Type()
)
hh3cPosaAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppRowStatus.setStatus("current")


class _Hh3cPosaAppName_Type(OctetString):
    """Custom type hh3cPosaAppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cPosaAppName_Type.__name__ = "OctetString"
_Hh3cPosaAppName_Object = MibTableColumn
hh3cPosaAppName = _Hh3cPosaAppName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 15),
    _Hh3cPosaAppName_Type()
)
hh3cPosaAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppName.setStatus("current")


class _Hh3cPosaCallerIDTransEnable_Type(TruthValue):
    """Custom type hh3cPosaCallerIDTransEnable based on TruthValue"""


_Hh3cPosaCallerIDTransEnable_Object = MibTableColumn
hh3cPosaCallerIDTransEnable = _Hh3cPosaCallerIDTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 16),
    _Hh3cPosaCallerIDTransEnable_Type()
)
hh3cPosaCallerIDTransEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaCallerIDTransEnable.setStatus("current")


class _Hh3cPosaTpduChangeStrategy_Type(Hh3cTpduChangeStrategy):
    """Custom type hh3cPosaTpduChangeStrategy based on Hh3cTpduChangeStrategy"""


_Hh3cPosaTpduChangeStrategy_Object = MibTableColumn
hh3cPosaTpduChangeStrategy = _Hh3cPosaTpduChangeStrategy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 17),
    _Hh3cPosaTpduChangeStrategy_Type()
)
hh3cPosaTpduChangeStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTpduChangeStrategy.setStatus("current")


class _Hh3cPosaBackupAppID_Type(Integer32):
    """Custom type hh3cPosaBackupAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hh3cPosaBackupAppID_Type.__name__ = "Integer32"
_Hh3cPosaBackupAppID_Object = MibTableColumn
hh3cPosaBackupAppID = _Hh3cPosaBackupAppID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 18),
    _Hh3cPosaBackupAppID_Type()
)
hh3cPosaBackupAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaBackupAppID.setStatus("current")


class _Hh3cPosaQuietTimeOut_Type(Integer32):
    """Custom type hh3cPosaQuietTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_Hh3cPosaQuietTimeOut_Type.__name__ = "Integer32"
_Hh3cPosaQuietTimeOut_Object = MibTableColumn
hh3cPosaQuietTimeOut = _Hh3cPosaQuietTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 19),
    _Hh3cPosaQuietTimeOut_Type()
)
hh3cPosaQuietTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaQuietTimeOut.setStatus("current")


class _Hh3cPosaAppHello_Type(TruthValue):
    """Custom type hh3cPosaAppHello based on TruthValue"""


_Hh3cPosaAppHello_Object = MibTableColumn
hh3cPosaAppHello = _Hh3cPosaAppHello_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 20),
    _Hh3cPosaAppHello_Type()
)
hh3cPosaAppHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppHello.setStatus("current")


class _Hh3cPosaAppHelloInterval_Type(Integer32):
    """Custom type hh3cPosaAppHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Hh3cPosaAppHelloInterval_Type.__name__ = "Integer32"
_Hh3cPosaAppHelloInterval_Object = MibTableColumn
hh3cPosaAppHelloInterval = _Hh3cPosaAppHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 21),
    _Hh3cPosaAppHelloInterval_Type()
)
hh3cPosaAppHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppHelloInterval.setStatus("current")


class _Hh3cPosaAppRouterPort_Type(Integer32):
    """Custom type hh3cPosaAppRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4999),
    )


_Hh3cPosaAppRouterPort_Type.__name__ = "Integer32"
_Hh3cPosaAppRouterPort_Object = MibTableColumn
hh3cPosaAppRouterPort = _Hh3cPosaAppRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 1, 1, 22),
    _Hh3cPosaAppRouterPort_Type()
)
hh3cPosaAppRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaAppRouterPort.setStatus("current")
_Hh3cPosaTerminalTable_Object = MibTable
hh3cPosaTerminalTable = _Hh3cPosaTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cPosaTerminalTable.setStatus("current")
_Hh3cPosaTerminalEntry_Object = MibTableRow
hh3cPosaTerminalEntry = _Hh3cPosaTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1)
)
hh3cPosaTerminalEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaTerminalID"),
)
if mibBuilder.loadTexts:
    hh3cPosaTerminalEntry.setStatus("current")


class _Hh3cPosaTerminalID_Type(Integer32):
    """Custom type hh3cPosaTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cPosaTerminalID_Type.__name__ = "Integer32"
_Hh3cPosaTerminalID_Object = MibTableColumn
hh3cPosaTerminalID = _Hh3cPosaTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 1),
    _Hh3cPosaTerminalID_Type()
)
hh3cPosaTerminalID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPosaTerminalID.setStatus("current")


class _Hh3cPosaTerminalAccessType_Type(Hh3cTerminalAccessType):
    """Custom type hh3cPosaTerminalAccessType based on Hh3cTerminalAccessType"""


_Hh3cPosaTerminalAccessType_Object = MibTableColumn
hh3cPosaTerminalAccessType = _Hh3cPosaTerminalAccessType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 2),
    _Hh3cPosaTerminalAccessType_Type()
)
hh3cPosaTerminalAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalAccessType.setStatus("current")
_Hh3cPosaTerminalIfIndex_Type = Integer32
_Hh3cPosaTerminalIfIndex_Object = MibTableColumn
hh3cPosaTerminalIfIndex = _Hh3cPosaTerminalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 3),
    _Hh3cPosaTerminalIfIndex_Type()
)
hh3cPosaTerminalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalIfIndex.setStatus("current")


class _Hh3cPosaTerminalTransAppID_Type(Integer32):
    """Custom type hh3cPosaTerminalTransAppID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hh3cPosaTerminalTransAppID_Type.__name__ = "Integer32"
_Hh3cPosaTerminalTransAppID_Object = MibTableColumn
hh3cPosaTerminalTransAppID = _Hh3cPosaTerminalTransAppID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 4),
    _Hh3cPosaTerminalTransAppID_Type()
)
hh3cPosaTerminalTransAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalTransAppID.setStatus("current")


class _Hh3cPosaTerminalListenPort_Type(Integer32):
    """Custom type hh3cPosaTerminalListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPosaTerminalListenPort_Type.__name__ = "Integer32"
_Hh3cPosaTerminalListenPort_Object = MibTableColumn
hh3cPosaTerminalListenPort = _Hh3cPosaTerminalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 5),
    _Hh3cPosaTerminalListenPort_Type()
)
hh3cPosaTerminalListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalListenPort.setStatus("current")
_Hh3cPosaTerminalState_Type = Hh3cPeerState
_Hh3cPosaTerminalState_Object = MibTableColumn
hh3cPosaTerminalState = _Hh3cPosaTerminalState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 6),
    _Hh3cPosaTerminalState_Type()
)
hh3cPosaTerminalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalState.setStatus("current")
_Hh3cPosaTerminalRowStatus_Type = RowStatus
_Hh3cPosaTerminalRowStatus_Object = MibTableColumn
hh3cPosaTerminalRowStatus = _Hh3cPosaTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 7),
    _Hh3cPosaTerminalRowStatus_Type()
)
hh3cPosaTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalRowStatus.setStatus("current")


class _Hh3cPosaTerminalName_Type(OctetString):
    """Custom type hh3cPosaTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cPosaTerminalName_Type.__name__ = "OctetString"
_Hh3cPosaTerminalName_Object = MibTableColumn
hh3cPosaTerminalName = _Hh3cPosaTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 8),
    _Hh3cPosaTerminalName_Type()
)
hh3cPosaTerminalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTerminalName.setStatus("current")
_Hh3cPosaTerminalCfgIfIndex_Type = Integer32
_Hh3cPosaTerminalCfgIfIndex_Object = MibTableColumn
hh3cPosaTerminalCfgIfIndex = _Hh3cPosaTerminalCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 2, 1, 9),
    _Hh3cPosaTerminalCfgIfIndex_Type()
)
hh3cPosaTerminalCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalCfgIfIndex.setStatus("current")
_Hh3cPosaMapTable_Object = MibTable
hh3cPosaMapTable = _Hh3cPosaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cPosaMapTable.setStatus("current")
_Hh3cPosaMapEntry_Object = MibTableRow
hh3cPosaMapEntry = _Hh3cPosaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1)
)
hh3cPosaMapEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaMapSrcCode"),
    (0, "HH3C-POSA-MIB", "hh3cPosaMapDestCode"),
)
if mibBuilder.loadTexts:
    hh3cPosaMapEntry.setStatus("current")


class _Hh3cPosaMapDestCode_Type(OctetString):
    """Custom type hh3cPosaMapDestCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_Hh3cPosaMapDestCode_Type.__name__ = "OctetString"
_Hh3cPosaMapDestCode_Object = MibTableColumn
hh3cPosaMapDestCode = _Hh3cPosaMapDestCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 1),
    _Hh3cPosaMapDestCode_Type()
)
hh3cPosaMapDestCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPosaMapDestCode.setStatus("current")


class _Hh3cPosaMapAppID_Type(Integer32):
    """Custom type hh3cPosaMapAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cPosaMapAppID_Type.__name__ = "Integer32"
_Hh3cPosaMapAppID_Object = MibTableColumn
hh3cPosaMapAppID = _Hh3cPosaMapAppID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 2),
    _Hh3cPosaMapAppID_Type()
)
hh3cPosaMapAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaMapAppID.setStatus("current")
_Hh3cPosaMapRowStatus_Type = RowStatus
_Hh3cPosaMapRowStatus_Object = MibTableColumn
hh3cPosaMapRowStatus = _Hh3cPosaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 3),
    _Hh3cPosaMapRowStatus_Type()
)
hh3cPosaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaMapRowStatus.setStatus("current")


class _Hh3cPosaMapSrcCode_Type(OctetString):
    """Custom type hh3cPosaMapSrcCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_Hh3cPosaMapSrcCode_Type.__name__ = "OctetString"
_Hh3cPosaMapSrcCode_Object = MibTableColumn
hh3cPosaMapSrcCode = _Hh3cPosaMapSrcCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 3, 1, 4),
    _Hh3cPosaMapSrcCode_Type()
)
hh3cPosaMapSrcCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPosaMapSrcCode.setStatus("current")
_Hh3cPosaFcmStatTable_Object = MibTable
hh3cPosaFcmStatTable = _Hh3cPosaFcmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cPosaFcmStatTable.setStatus("current")
_Hh3cPosaFcmStatEntry_Object = MibTableRow
hh3cPosaFcmStatEntry = _Hh3cPosaFcmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1)
)
hh3cPosaFcmStatEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaFcmStatIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cPosaFcmStatEntry.setStatus("current")


class _Hh3cPosaFcmStatIfIndex_Type(Integer32):
    """Custom type hh3cPosaFcmStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPosaFcmStatIfIndex_Type.__name__ = "Integer32"
_Hh3cPosaFcmStatIfIndex_Object = MibTableColumn
hh3cPosaFcmStatIfIndex = _Hh3cPosaFcmStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 1),
    _Hh3cPosaFcmStatIfIndex_Type()
)
hh3cPosaFcmStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatIfIndex.setStatus("current")
_Hh3cPosaFcmStatTimeoutCnts_Type = Counter32
_Hh3cPosaFcmStatTimeoutCnts_Object = MibTableColumn
hh3cPosaFcmStatTimeoutCnts = _Hh3cPosaFcmStatTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 2),
    _Hh3cPosaFcmStatTimeoutCnts_Type()
)
hh3cPosaFcmStatTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatTimeoutCnts.setStatus("current")
_Hh3cPosaFcmStatConnectFailCnts_Type = Counter32
_Hh3cPosaFcmStatConnectFailCnts_Object = MibTableColumn
hh3cPosaFcmStatConnectFailCnts = _Hh3cPosaFcmStatConnectFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 3),
    _Hh3cPosaFcmStatConnectFailCnts_Type()
)
hh3cPosaFcmStatConnectFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatConnectFailCnts.setStatus("current")
_Hh3cPosaFcmStatTransCnts_Type = Gauge32
_Hh3cPosaFcmStatTransCnts_Object = MibTableColumn
hh3cPosaFcmStatTransCnts = _Hh3cPosaFcmStatTransCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 4),
    _Hh3cPosaFcmStatTransCnts_Type()
)
hh3cPosaFcmStatTransCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatTransCnts.setStatus("current")
_Hh3cPosaFcmStatTransSuccessCnts_Type = Gauge32
_Hh3cPosaFcmStatTransSuccessCnts_Object = MibTableColumn
hh3cPosaFcmStatTransSuccessCnts = _Hh3cPosaFcmStatTransSuccessCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 5),
    _Hh3cPosaFcmStatTransSuccessCnts_Type()
)
hh3cPosaFcmStatTransSuccessCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatTransSuccessCnts.setStatus("current")


class _Hh3cPosaFcmStatTransCntsClear_Type(TruthValue):
    """Custom type hh3cPosaFcmStatTransCntsClear based on TruthValue"""


_Hh3cPosaFcmStatTransCntsClear_Object = MibTableColumn
hh3cPosaFcmStatTransCntsClear = _Hh3cPosaFcmStatTransCntsClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 4, 1, 6),
    _Hh3cPosaFcmStatTransCntsClear_Type()
)
hh3cPosaFcmStatTransCntsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmStatTransCntsClear.setStatus("current")
_Hh3cPosaAppStatTable_Object = MibTable
hh3cPosaAppStatTable = _Hh3cPosaAppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cPosaAppStatTable.setStatus("current")
_Hh3cPosaAppStatEntry_Object = MibTableRow
hh3cPosaAppStatEntry = _Hh3cPosaAppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1)
)
hh3cPosaAppStatEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaAppID"),
)
if mibBuilder.loadTexts:
    hh3cPosaAppStatEntry.setStatus("current")
_Hh3cPosaAppRecvPkts_Type = Counter32
_Hh3cPosaAppRecvPkts_Object = MibTableColumn
hh3cPosaAppRecvPkts = _Hh3cPosaAppRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 1),
    _Hh3cPosaAppRecvPkts_Type()
)
hh3cPosaAppRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppRecvPkts.setStatus("current")
_Hh3cPosaAppSendPkts_Type = Counter32
_Hh3cPosaAppSendPkts_Object = MibTableColumn
hh3cPosaAppSendPkts = _Hh3cPosaAppSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 2),
    _Hh3cPosaAppSendPkts_Type()
)
hh3cPosaAppSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppSendPkts.setStatus("current")
_Hh3cPosaAppErrPkts_Type = Counter32
_Hh3cPosaAppErrPkts_Object = MibTableColumn
hh3cPosaAppErrPkts = _Hh3cPosaAppErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 3),
    _Hh3cPosaAppErrPkts_Type()
)
hh3cPosaAppErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppErrPkts.setStatus("current")
_Hh3cPosaAppDistributeErrCnts_Type = Counter32
_Hh3cPosaAppDistributeErrCnts_Object = MibTableColumn
hh3cPosaAppDistributeErrCnts = _Hh3cPosaAppDistributeErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 4),
    _Hh3cPosaAppDistributeErrCnts_Type()
)
hh3cPosaAppDistributeErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppDistributeErrCnts.setStatus("current")
_Hh3cPosaAppInDiscardedPkts_Type = Counter32
_Hh3cPosaAppInDiscardedPkts_Object = MibTableColumn
hh3cPosaAppInDiscardedPkts = _Hh3cPosaAppInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 5),
    _Hh3cPosaAppInDiscardedPkts_Type()
)
hh3cPosaAppInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppInDiscardedPkts.setStatus("current")
_Hh3cPosaAppOutDiscardedPkts_Type = Counter32
_Hh3cPosaAppOutDiscardedPkts_Object = MibTableColumn
hh3cPosaAppOutDiscardedPkts = _Hh3cPosaAppOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 5, 1, 6),
    _Hh3cPosaAppOutDiscardedPkts_Type()
)
hh3cPosaAppOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaAppOutDiscardedPkts.setStatus("current")
_Hh3cPosaTerminalStatTable_Object = MibTable
hh3cPosaTerminalStatTable = _Hh3cPosaTerminalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cPosaTerminalStatTable.setStatus("current")
_Hh3cPosaTerminalStatEntry_Object = MibTableRow
hh3cPosaTerminalStatEntry = _Hh3cPosaTerminalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1)
)
hh3cPosaTerminalStatEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaTerminalID"),
)
if mibBuilder.loadTexts:
    hh3cPosaTerminalStatEntry.setStatus("current")
_Hh3cPosaTerminalRecvPkts_Type = Counter32
_Hh3cPosaTerminalRecvPkts_Object = MibTableColumn
hh3cPosaTerminalRecvPkts = _Hh3cPosaTerminalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 1),
    _Hh3cPosaTerminalRecvPkts_Type()
)
hh3cPosaTerminalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalRecvPkts.setStatus("current")
_Hh3cPosaTerminalSendPkts_Type = Counter32
_Hh3cPosaTerminalSendPkts_Object = MibTableColumn
hh3cPosaTerminalSendPkts = _Hh3cPosaTerminalSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 2),
    _Hh3cPosaTerminalSendPkts_Type()
)
hh3cPosaTerminalSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalSendPkts.setStatus("current")
_Hh3cPosaTerminalErrPkts_Type = Counter32
_Hh3cPosaTerminalErrPkts_Object = MibTableColumn
hh3cPosaTerminalErrPkts = _Hh3cPosaTerminalErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 3),
    _Hh3cPosaTerminalErrPkts_Type()
)
hh3cPosaTerminalErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalErrPkts.setStatus("current")
_Hh3cPosaTerminalMapErrCnts_Type = Counter32
_Hh3cPosaTerminalMapErrCnts_Object = MibTableColumn
hh3cPosaTerminalMapErrCnts = _Hh3cPosaTerminalMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 4),
    _Hh3cPosaTerminalMapErrCnts_Type()
)
hh3cPosaTerminalMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalMapErrCnts.setStatus("current")
_Hh3cPosaTerminalInDiscardedPkts_Type = Counter32
_Hh3cPosaTerminalInDiscardedPkts_Object = MibTableColumn
hh3cPosaTerminalInDiscardedPkts = _Hh3cPosaTerminalInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 5),
    _Hh3cPosaTerminalInDiscardedPkts_Type()
)
hh3cPosaTerminalInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalInDiscardedPkts.setStatus("current")
_Hh3cPosaTerminalOutDiscardedPkts_Type = Counter32
_Hh3cPosaTerminalOutDiscardedPkts_Object = MibTableColumn
hh3cPosaTerminalOutDiscardedPkts = _Hh3cPosaTerminalOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 6, 1, 6),
    _Hh3cPosaTerminalOutDiscardedPkts_Type()
)
hh3cPosaTerminalOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTerminalOutDiscardedPkts.setStatus("current")
_Hh3cPosaBatchTerminalTable_Object = MibTable
hh3cPosaBatchTerminalTable = _Hh3cPosaBatchTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cPosaBatchTerminalTable.setStatus("current")
_Hh3cPosaBatchTerminalEntry_Object = MibTableRow
hh3cPosaBatchTerminalEntry = _Hh3cPosaBatchTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1)
)
hh3cPosaBatchTerminalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cPosaBatchTerminalEntry.setStatus("current")


class _Hh3cPosaBatchTerminalFirstID_Type(Integer32):
    """Custom type hh3cPosaBatchTerminalFirstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cPosaBatchTerminalFirstID_Type.__name__ = "Integer32"
_Hh3cPosaBatchTerminalFirstID_Object = MibTableColumn
hh3cPosaBatchTerminalFirstID = _Hh3cPosaBatchTerminalFirstID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1, 1),
    _Hh3cPosaBatchTerminalFirstID_Type()
)
hh3cPosaBatchTerminalFirstID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaBatchTerminalFirstID.setStatus("current")
_Hh3cPosaBatchTerminalRowStatus_Type = RowStatus
_Hh3cPosaBatchTerminalRowStatus_Object = MibTableColumn
hh3cPosaBatchTerminalRowStatus = _Hh3cPosaBatchTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 7, 1, 2),
    _Hh3cPosaBatchTerminalRowStatus_Type()
)
hh3cPosaBatchTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaBatchTerminalRowStatus.setStatus("current")
_Hh3cPosaTcpTermStatTable_Object = MibTable
hh3cPosaTcpTermStatTable = _Hh3cPosaTcpTermStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatTable.setStatus("current")
_Hh3cPosaTcpTermStatEntry_Object = MibTableRow
hh3cPosaTcpTermStatEntry = _Hh3cPosaTcpTermStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1)
)
hh3cPosaTcpTermStatEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaTcpTermStatIndex"),
)
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatEntry.setStatus("current")


class _Hh3cPosaTcpTermStatIndex_Type(Integer32):
    """Custom type hh3cPosaTcpTermStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cPosaTcpTermStatIndex_Type.__name__ = "Integer32"
_Hh3cPosaTcpTermStatIndex_Object = MibTableColumn
hh3cPosaTcpTermStatIndex = _Hh3cPosaTcpTermStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 1),
    _Hh3cPosaTcpTermStatIndex_Type()
)
hh3cPosaTcpTermStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatIndex.setStatus("current")
_Hh3cPosaTcpTermStatIPType_Type = InetAddressType
_Hh3cPosaTcpTermStatIPType_Object = MibTableColumn
hh3cPosaTcpTermStatIPType = _Hh3cPosaTcpTermStatIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 2),
    _Hh3cPosaTcpTermStatIPType_Type()
)
hh3cPosaTcpTermStatIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatIPType.setStatus("current")
_Hh3cPosaTcpTermStatIP_Type = InetAddress
_Hh3cPosaTcpTermStatIP_Object = MibTableColumn
hh3cPosaTcpTermStatIP = _Hh3cPosaTcpTermStatIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 3),
    _Hh3cPosaTcpTermStatIP_Type()
)
hh3cPosaTcpTermStatIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatIP.setStatus("current")
_Hh3cPosaTcpTermStatIPMask_Type = InetAddress
_Hh3cPosaTcpTermStatIPMask_Object = MibTableColumn
hh3cPosaTcpTermStatIPMask = _Hh3cPosaTcpTermStatIPMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 4),
    _Hh3cPosaTcpTermStatIPMask_Type()
)
hh3cPosaTcpTermStatIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatIPMask.setStatus("current")
_Hh3cPosaTcpTermRecvPkts_Type = Counter64
_Hh3cPosaTcpTermRecvPkts_Object = MibTableColumn
hh3cPosaTcpTermRecvPkts = _Hh3cPosaTcpTermRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 5),
    _Hh3cPosaTcpTermRecvPkts_Type()
)
hh3cPosaTcpTermRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermRecvPkts.setStatus("current")
_Hh3cPosaTcpTermSendPkts_Type = Counter64
_Hh3cPosaTcpTermSendPkts_Object = MibTableColumn
hh3cPosaTcpTermSendPkts = _Hh3cPosaTcpTermSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 6),
    _Hh3cPosaTcpTermSendPkts_Type()
)
hh3cPosaTcpTermSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermSendPkts.setStatus("current")
_Hh3cPosaTcpTermErrPkts_Type = Counter64
_Hh3cPosaTcpTermErrPkts_Object = MibTableColumn
hh3cPosaTcpTermErrPkts = _Hh3cPosaTcpTermErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 7),
    _Hh3cPosaTcpTermErrPkts_Type()
)
hh3cPosaTcpTermErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermErrPkts.setStatus("current")
_Hh3cPosaTcpTermMapErrCnts_Type = Counter64
_Hh3cPosaTcpTermMapErrCnts_Object = MibTableColumn
hh3cPosaTcpTermMapErrCnts = _Hh3cPosaTcpTermMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 8),
    _Hh3cPosaTcpTermMapErrCnts_Type()
)
hh3cPosaTcpTermMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermMapErrCnts.setStatus("current")
_Hh3cPosaTcpTermInDiscardedPkts_Type = Counter64
_Hh3cPosaTcpTermInDiscardedPkts_Object = MibTableColumn
hh3cPosaTcpTermInDiscardedPkts = _Hh3cPosaTcpTermInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 9),
    _Hh3cPosaTcpTermInDiscardedPkts_Type()
)
hh3cPosaTcpTermInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermInDiscardedPkts.setStatus("current")
_Hh3cPosaTcpTermOutDiscardedPkts_Type = Counter64
_Hh3cPosaTcpTermOutDiscardedPkts_Object = MibTableColumn
hh3cPosaTcpTermOutDiscardedPkts = _Hh3cPosaTcpTermOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 10),
    _Hh3cPosaTcpTermOutDiscardedPkts_Type()
)
hh3cPosaTcpTermOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermOutDiscardedPkts.setStatus("current")
_Hh3cPosaTcpTermStatRowStatus_Type = RowStatus
_Hh3cPosaTcpTermStatRowStatus_Object = MibTableColumn
hh3cPosaTcpTermStatRowStatus = _Hh3cPosaTcpTermStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 8, 1, 11),
    _Hh3cPosaTcpTermStatRowStatus_Type()
)
hh3cPosaTcpTermStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaTcpTermStatRowStatus.setStatus("current")
_Hh3cPosaFcmConfTable_Object = MibTable
hh3cPosaFcmConfTable = _Hh3cPosaFcmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cPosaFcmConfTable.setStatus("current")
_Hh3cPosaFcmConfEntry_Object = MibTableRow
hh3cPosaFcmConfEntry = _Hh3cPosaFcmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1)
)
hh3cPosaFcmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cPosaFcmConfEntry.setStatus("current")


class _Hh3cPosaFcmNegoHookOff_Type(Integer32):
    """Custom type hh3cPosaFcmNegoHookOff based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 6000),
    )


_Hh3cPosaFcmNegoHookOff_Type.__name__ = "Integer32"
_Hh3cPosaFcmNegoHookOff_Object = MibTableColumn
hh3cPosaFcmNegoHookOff = _Hh3cPosaFcmNegoHookOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 1),
    _Hh3cPosaFcmNegoHookOff_Type()
)
hh3cPosaFcmNegoHookOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoHookOff.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoHookOff.setUnits("milliseconds")


class _Hh3cPosaFcmNegoSilence_Type(Integer32):
    """Custom type hh3cPosaFcmNegoSilence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_Hh3cPosaFcmNegoSilence_Type.__name__ = "Integer32"
_Hh3cPosaFcmNegoSilence_Object = MibTableColumn
hh3cPosaFcmNegoSilence = _Hh3cPosaFcmNegoSilence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 2),
    _Hh3cPosaFcmNegoSilence_Type()
)
hh3cPosaFcmNegoSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoSilence.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoSilence.setUnits("milliseconds")


class _Hh3cPosaFcmNegoScrmbBinary1_Type(Integer32):
    """Custom type hh3cPosaFcmNegoScrmbBinary1 based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_Hh3cPosaFcmNegoScrmbBinary1_Type.__name__ = "Integer32"
_Hh3cPosaFcmNegoScrmbBinary1_Object = MibTableColumn
hh3cPosaFcmNegoScrmbBinary1 = _Hh3cPosaFcmNegoScrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 3),
    _Hh3cPosaFcmNegoScrmbBinary1_Type()
)
hh3cPosaFcmNegoScrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoScrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoScrmbBinary1.setUnits("milliseconds")


class _Hh3cPosaFcmNegoUnscrmbBinary1_Type(Integer32):
    """Custom type hh3cPosaFcmNegoUnscrmbBinary1 based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1500),
    )


_Hh3cPosaFcmNegoUnscrmbBinary1_Type.__name__ = "Integer32"
_Hh3cPosaFcmNegoUnscrmbBinary1_Object = MibTableColumn
hh3cPosaFcmNegoUnscrmbBinary1 = _Hh3cPosaFcmNegoUnscrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 4),
    _Hh3cPosaFcmNegoUnscrmbBinary1_Type()
)
hh3cPosaFcmNegoUnscrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoUnscrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmNegoUnscrmbBinary1.setUnits("milliseconds")


class _Hh3cPosaFcmThresholdRlsdOff_Type(Integer32):
    """Custom type hh3cPosaFcmThresholdRlsdOff based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_Hh3cPosaFcmThresholdRlsdOff_Type.__name__ = "Integer32"
_Hh3cPosaFcmThresholdRlsdOff_Object = MibTableColumn
hh3cPosaFcmThresholdRlsdOff = _Hh3cPosaFcmThresholdRlsdOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 5),
    _Hh3cPosaFcmThresholdRlsdOff_Type()
)
hh3cPosaFcmThresholdRlsdOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdRlsdOff.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdRlsdOff.setUnits("-dBm")


class _Hh3cPosaFcmThresholdRlsdOn_Type(Integer32):
    """Custom type hh3cPosaFcmThresholdRlsdOn based on Integer32"""
    defaultValue = 43

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_Hh3cPosaFcmThresholdRlsdOn_Type.__name__ = "Integer32"
_Hh3cPosaFcmThresholdRlsdOn_Object = MibTableColumn
hh3cPosaFcmThresholdRlsdOn = _Hh3cPosaFcmThresholdRlsdOn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 6),
    _Hh3cPosaFcmThresholdRlsdOn_Type()
)
hh3cPosaFcmThresholdRlsdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdRlsdOn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdRlsdOn.setUnits("-dBm")


class _Hh3cPosaFcmThresholdTxPower_Type(Integer32):
    """Custom type hh3cPosaFcmThresholdTxPower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_Hh3cPosaFcmThresholdTxPower_Type.__name__ = "Integer32"
_Hh3cPosaFcmThresholdTxPower_Object = MibTableColumn
hh3cPosaFcmThresholdTxPower = _Hh3cPosaFcmThresholdTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 7),
    _Hh3cPosaFcmThresholdTxPower_Type()
)
hh3cPosaFcmThresholdTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdTxPower.setUnits("-dBm")


class _Hh3cPosaFcmThresholdAnswerTone_Type(Integer32):
    """Custom type hh3cPosaFcmThresholdAnswerTone based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_Hh3cPosaFcmThresholdAnswerTone_Type.__name__ = "Integer32"
_Hh3cPosaFcmThresholdAnswerTone_Object = MibTableColumn
hh3cPosaFcmThresholdAnswerTone = _Hh3cPosaFcmThresholdAnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 9, 1, 8),
    _Hh3cPosaFcmThresholdAnswerTone_Type()
)
hh3cPosaFcmThresholdAnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdAnswerTone.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPosaFcmThresholdAnswerTone.setUnits("-dBm")
_Hh3cPosaCallerStatTable_Object = MibTable
hh3cPosaCallerStatTable = _Hh3cPosaCallerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cPosaCallerStatTable.setStatus("current")
_Hh3cPosaCallerStatEntry_Object = MibTableRow
hh3cPosaCallerStatEntry = _Hh3cPosaCallerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1)
)
hh3cPosaCallerStatEntry.setIndexNames(
    (0, "HH3C-POSA-MIB", "hh3cPosaCallerStatCallerID"),
)
if mibBuilder.loadTexts:
    hh3cPosaCallerStatEntry.setStatus("current")


class _Hh3cPosaCallerStatCallerID_Type(OctetString):
    """Custom type hh3cPosaCallerStatCallerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cPosaCallerStatCallerID_Type.__name__ = "OctetString"
_Hh3cPosaCallerStatCallerID_Object = MibTableColumn
hh3cPosaCallerStatCallerID = _Hh3cPosaCallerStatCallerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 1),
    _Hh3cPosaCallerStatCallerID_Type()
)
hh3cPosaCallerStatCallerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPosaCallerStatCallerID.setStatus("current")
_Hh3cPosaCallerRecvPkts_Type = Counter64
_Hh3cPosaCallerRecvPkts_Object = MibTableColumn
hh3cPosaCallerRecvPkts = _Hh3cPosaCallerRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 2),
    _Hh3cPosaCallerRecvPkts_Type()
)
hh3cPosaCallerRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerRecvPkts.setStatus("current")
_Hh3cPosaCallerSendPkts_Type = Counter64
_Hh3cPosaCallerSendPkts_Object = MibTableColumn
hh3cPosaCallerSendPkts = _Hh3cPosaCallerSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 3),
    _Hh3cPosaCallerSendPkts_Type()
)
hh3cPosaCallerSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerSendPkts.setStatus("current")
_Hh3cPosaCallerErrPkts_Type = Counter64
_Hh3cPosaCallerErrPkts_Object = MibTableColumn
hh3cPosaCallerErrPkts = _Hh3cPosaCallerErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 4),
    _Hh3cPosaCallerErrPkts_Type()
)
hh3cPosaCallerErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerErrPkts.setStatus("current")
_Hh3cPosaCallerMapErrCnts_Type = Counter64
_Hh3cPosaCallerMapErrCnts_Object = MibTableColumn
hh3cPosaCallerMapErrCnts = _Hh3cPosaCallerMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 5),
    _Hh3cPosaCallerMapErrCnts_Type()
)
hh3cPosaCallerMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerMapErrCnts.setStatus("current")
_Hh3cPosaCallerInDiscardedPkts_Type = Counter64
_Hh3cPosaCallerInDiscardedPkts_Object = MibTableColumn
hh3cPosaCallerInDiscardedPkts = _Hh3cPosaCallerInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 6),
    _Hh3cPosaCallerInDiscardedPkts_Type()
)
hh3cPosaCallerInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerInDiscardedPkts.setStatus("current")
_Hh3cPosaCallerOutDiscardedPkts_Type = Counter64
_Hh3cPosaCallerOutDiscardedPkts_Object = MibTableColumn
hh3cPosaCallerOutDiscardedPkts = _Hh3cPosaCallerOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 7),
    _Hh3cPosaCallerOutDiscardedPkts_Type()
)
hh3cPosaCallerOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPosaCallerOutDiscardedPkts.setStatus("current")
_Hh3cPosaCallerStatRowStatus_Type = RowStatus
_Hh3cPosaCallerStatRowStatus_Object = MibTableColumn
hh3cPosaCallerStatRowStatus = _Hh3cPosaCallerStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 2, 10, 1, 8),
    _Hh3cPosaCallerStatRowStatus_Type()
)
hh3cPosaCallerStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPosaCallerStatRowStatus.setStatus("current")
_Hh3cPosaTrap_ObjectIdentity = ObjectIdentity
hh3cPosaTrap = _Hh3cPosaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3)
)
_Hh3cPosaTrapPrex_ObjectIdentity = ObjectIdentity
hh3cPosaTrapPrex = _Hh3cPosaTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0)
)
_Hh3cPosaTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPosaTrapObjects = _Hh3cPosaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 1)
)


class _Hh3cPosaAppStateChangeObject_Type(Integer32):
    """Custom type hh3cPosaAppStateChangeObject based on Integer32"""
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


_Hh3cPosaAppStateChangeObject_Type.__name__ = "Integer32"
_Hh3cPosaAppStateChangeObject_Object = MibScalar
hh3cPosaAppStateChangeObject = _Hh3cPosaAppStateChangeObject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 1, 1),
    _Hh3cPosaAppStateChangeObject_Type()
)
hh3cPosaAppStateChangeObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPosaAppStateChangeObject.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPosaServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 1)
)
hh3cPosaServerStatusChange.setObjects(
    ("HH3C-POSA-MIB", "hh3cPosaServerEnable")
)
if mibBuilder.loadTexts:
    hh3cPosaServerStatusChange.setStatus(
        "current"
    )

hh3cPosaAppStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 2)
)
hh3cPosaAppStateChange.setObjects(
      *(("HH3C-POSA-MIB", "hh3cPosaAppID"),
        ("HH3C-POSA-MIB", "hh3cPosaAppStateChangeObject"))
)
if mibBuilder.loadTexts:
    hh3cPosaAppStateChange.setStatus(
        "current"
    )

hh3cPosaTerminalHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 3)
)
hh3cPosaTerminalHangUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosaTerminalHangUp.setStatus(
        "current"
    )

hh3cPosaFcmLinkNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 4)
)
hh3cPosaFcmLinkNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosaFcmLinkNegoFailed.setStatus(
        "current"
    )

hh3cPosaFcmPhyNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 5)
)
hh3cPosaFcmPhyNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cPosaFcmPhyNegoFailed.setStatus(
        "current"
    )

hh3cPosaTcpConnectionExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 6)
)
hh3cPosaTcpConnectionExceed.setObjects(
    ("HH3C-POSA-MIB", "hh3cPosaTcpConnectionThreshold")
)
if mibBuilder.loadTexts:
    hh3cPosaTcpConnectionExceed.setStatus(
        "current"
    )

hh3cPosaFcmConnectionExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 7)
)
hh3cPosaFcmConnectionExceed.setObjects(
    ("HH3C-POSA-MIB", "hh3cPosaFcmConnectionThreshold")
)
if mibBuilder.loadTexts:
    hh3cPosaFcmConnectionExceed.setStatus(
        "current"
    )

hh3cPosaTcpTradeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92, 3, 0, 8)
)
hh3cPosaTcpTradeExceed.setObjects(
      *(("HH3C-POSA-MIB", "hh3cPosaTcpTradeLimit"),
        ("HH3C-POSA-MIB", "hh3cPosaTerminalID"))
)
if mibBuilder.loadTexts:
    hh3cPosaTcpTradeExceed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-POSA-MIB",
    **{"Hh3cAppServiceType": Hh3cAppServiceType,
       "Hh3cAppMode": Hh3cAppMode,
       "Hh3cPeerState": Hh3cPeerState,
       "Hh3cTerminalAccessType": Hh3cTerminalAccessType,
       "Hh3cTpduChangeStrategy": Hh3cTpduChangeStrategy,
       "hh3cPosa": hh3cPosa,
       "hh3cPosaControl": hh3cPosaControl,
       "hh3cPosaServerEnable": hh3cPosaServerEnable,
       "hh3cPosaFcmAnswerTimeout": hh3cPosaFcmAnswerTimeout,
       "hh3cPosaFcmTradeTimeout": hh3cPosaFcmTradeTimeout,
       "hh3cPosaFcmIdleTimeout": hh3cPosaFcmIdleTimeout,
       "hh3cPosaSrvStateChangeTrapEnable": hh3cPosaSrvStateChangeTrapEnable,
       "hh3cPosaAppStateChangeTrapEnable": hh3cPosaAppStateChangeTrapEnable,
       "hh3cPosaTerminalHangUpTrapEnable": hh3cPosaTerminalHangUpTrapEnable,
       "hh3cPosaFcmLnkNegoFailTrapEnable": hh3cPosaFcmLnkNegoFailTrapEnable,
       "hh3cPosaFcmPhyNegoFailTrapEnable": hh3cPosaFcmPhyNegoFailTrapEnable,
       "hh3cPosaTcpConnectionNumber": hh3cPosaTcpConnectionNumber,
       "hh3cPosaFcmConnectionNumber": hh3cPosaFcmConnectionNumber,
       "hh3cPosaTcpConnectionThreshold": hh3cPosaTcpConnectionThreshold,
       "hh3cPosaFcmConnectionThreshold": hh3cPosaFcmConnectionThreshold,
       "hh3cPosaTcpConnectionTrapEnable": hh3cPosaTcpConnectionTrapEnable,
       "hh3cPosaFcmConnectionTrapEnable": hh3cPosaFcmConnectionTrapEnable,
       "hh3cPosaTcpTradeLimit": hh3cPosaTcpTradeLimit,
       "hh3cPosaTcpTradeTrapEnable": hh3cPosaTcpTradeTrapEnable,
       "hh3cPosaTcpTradeTimeout": hh3cPosaTcpTradeTimeout,
       "hh3cPosaTables": hh3cPosaTables,
       "hh3cPosaAppTable": hh3cPosaAppTable,
       "hh3cPosaAppEntry": hh3cPosaAppEntry,
       "hh3cPosaAppID": hh3cPosaAppID,
       "hh3cPosaAppServiceType": hh3cPosaAppServiceType,
       "hh3cPosaAppIfIndex": hh3cPosaAppIfIndex,
       "hh3cPosaAppMode": hh3cPosaAppMode,
       "hh3cPosaAppHostIPType": hh3cPosaAppHostIPType,
       "hh3cPosaAppHostIP": hh3cPosaAppHostIP,
       "hh3cPosaAppHostPort": hh3cPosaAppHostPort,
       "hh3cPosaAppRouterIPType": hh3cPosaAppRouterIPType,
       "hh3cPosaAppRouterIP": hh3cPosaAppRouterIP,
       "hh3cPosaAppKeepAliveInterval": hh3cPosaAppKeepAliveInterval,
       "hh3cPosaAppKeepAliveCount": hh3cPosaAppKeepAliveCount,
       "hh3cPosaAppConnectTimeout": hh3cPosaAppConnectTimeout,
       "hh3cPosaAppState": hh3cPosaAppState,
       "hh3cPosaAppRowStatus": hh3cPosaAppRowStatus,
       "hh3cPosaAppName": hh3cPosaAppName,
       "hh3cPosaCallerIDTransEnable": hh3cPosaCallerIDTransEnable,
       "hh3cPosaTpduChangeStrategy": hh3cPosaTpduChangeStrategy,
       "hh3cPosaBackupAppID": hh3cPosaBackupAppID,
       "hh3cPosaQuietTimeOut": hh3cPosaQuietTimeOut,
       "hh3cPosaAppHello": hh3cPosaAppHello,
       "hh3cPosaAppHelloInterval": hh3cPosaAppHelloInterval,
       "hh3cPosaAppRouterPort": hh3cPosaAppRouterPort,
       "hh3cPosaTerminalTable": hh3cPosaTerminalTable,
       "hh3cPosaTerminalEntry": hh3cPosaTerminalEntry,
       "hh3cPosaTerminalID": hh3cPosaTerminalID,
       "hh3cPosaTerminalAccessType": hh3cPosaTerminalAccessType,
       "hh3cPosaTerminalIfIndex": hh3cPosaTerminalIfIndex,
       "hh3cPosaTerminalTransAppID": hh3cPosaTerminalTransAppID,
       "hh3cPosaTerminalListenPort": hh3cPosaTerminalListenPort,
       "hh3cPosaTerminalState": hh3cPosaTerminalState,
       "hh3cPosaTerminalRowStatus": hh3cPosaTerminalRowStatus,
       "hh3cPosaTerminalName": hh3cPosaTerminalName,
       "hh3cPosaTerminalCfgIfIndex": hh3cPosaTerminalCfgIfIndex,
       "hh3cPosaMapTable": hh3cPosaMapTable,
       "hh3cPosaMapEntry": hh3cPosaMapEntry,
       "hh3cPosaMapDestCode": hh3cPosaMapDestCode,
       "hh3cPosaMapAppID": hh3cPosaMapAppID,
       "hh3cPosaMapRowStatus": hh3cPosaMapRowStatus,
       "hh3cPosaMapSrcCode": hh3cPosaMapSrcCode,
       "hh3cPosaFcmStatTable": hh3cPosaFcmStatTable,
       "hh3cPosaFcmStatEntry": hh3cPosaFcmStatEntry,
       "hh3cPosaFcmStatIfIndex": hh3cPosaFcmStatIfIndex,
       "hh3cPosaFcmStatTimeoutCnts": hh3cPosaFcmStatTimeoutCnts,
       "hh3cPosaFcmStatConnectFailCnts": hh3cPosaFcmStatConnectFailCnts,
       "hh3cPosaFcmStatTransCnts": hh3cPosaFcmStatTransCnts,
       "hh3cPosaFcmStatTransSuccessCnts": hh3cPosaFcmStatTransSuccessCnts,
       "hh3cPosaFcmStatTransCntsClear": hh3cPosaFcmStatTransCntsClear,
       "hh3cPosaAppStatTable": hh3cPosaAppStatTable,
       "hh3cPosaAppStatEntry": hh3cPosaAppStatEntry,
       "hh3cPosaAppRecvPkts": hh3cPosaAppRecvPkts,
       "hh3cPosaAppSendPkts": hh3cPosaAppSendPkts,
       "hh3cPosaAppErrPkts": hh3cPosaAppErrPkts,
       "hh3cPosaAppDistributeErrCnts": hh3cPosaAppDistributeErrCnts,
       "hh3cPosaAppInDiscardedPkts": hh3cPosaAppInDiscardedPkts,
       "hh3cPosaAppOutDiscardedPkts": hh3cPosaAppOutDiscardedPkts,
       "hh3cPosaTerminalStatTable": hh3cPosaTerminalStatTable,
       "hh3cPosaTerminalStatEntry": hh3cPosaTerminalStatEntry,
       "hh3cPosaTerminalRecvPkts": hh3cPosaTerminalRecvPkts,
       "hh3cPosaTerminalSendPkts": hh3cPosaTerminalSendPkts,
       "hh3cPosaTerminalErrPkts": hh3cPosaTerminalErrPkts,
       "hh3cPosaTerminalMapErrCnts": hh3cPosaTerminalMapErrCnts,
       "hh3cPosaTerminalInDiscardedPkts": hh3cPosaTerminalInDiscardedPkts,
       "hh3cPosaTerminalOutDiscardedPkts": hh3cPosaTerminalOutDiscardedPkts,
       "hh3cPosaBatchTerminalTable": hh3cPosaBatchTerminalTable,
       "hh3cPosaBatchTerminalEntry": hh3cPosaBatchTerminalEntry,
       "hh3cPosaBatchTerminalFirstID": hh3cPosaBatchTerminalFirstID,
       "hh3cPosaBatchTerminalRowStatus": hh3cPosaBatchTerminalRowStatus,
       "hh3cPosaTcpTermStatTable": hh3cPosaTcpTermStatTable,
       "hh3cPosaTcpTermStatEntry": hh3cPosaTcpTermStatEntry,
       "hh3cPosaTcpTermStatIndex": hh3cPosaTcpTermStatIndex,
       "hh3cPosaTcpTermStatIPType": hh3cPosaTcpTermStatIPType,
       "hh3cPosaTcpTermStatIP": hh3cPosaTcpTermStatIP,
       "hh3cPosaTcpTermStatIPMask": hh3cPosaTcpTermStatIPMask,
       "hh3cPosaTcpTermRecvPkts": hh3cPosaTcpTermRecvPkts,
       "hh3cPosaTcpTermSendPkts": hh3cPosaTcpTermSendPkts,
       "hh3cPosaTcpTermErrPkts": hh3cPosaTcpTermErrPkts,
       "hh3cPosaTcpTermMapErrCnts": hh3cPosaTcpTermMapErrCnts,
       "hh3cPosaTcpTermInDiscardedPkts": hh3cPosaTcpTermInDiscardedPkts,
       "hh3cPosaTcpTermOutDiscardedPkts": hh3cPosaTcpTermOutDiscardedPkts,
       "hh3cPosaTcpTermStatRowStatus": hh3cPosaTcpTermStatRowStatus,
       "hh3cPosaFcmConfTable": hh3cPosaFcmConfTable,
       "hh3cPosaFcmConfEntry": hh3cPosaFcmConfEntry,
       "hh3cPosaFcmNegoHookOff": hh3cPosaFcmNegoHookOff,
       "hh3cPosaFcmNegoSilence": hh3cPosaFcmNegoSilence,
       "hh3cPosaFcmNegoScrmbBinary1": hh3cPosaFcmNegoScrmbBinary1,
       "hh3cPosaFcmNegoUnscrmbBinary1": hh3cPosaFcmNegoUnscrmbBinary1,
       "hh3cPosaFcmThresholdRlsdOff": hh3cPosaFcmThresholdRlsdOff,
       "hh3cPosaFcmThresholdRlsdOn": hh3cPosaFcmThresholdRlsdOn,
       "hh3cPosaFcmThresholdTxPower": hh3cPosaFcmThresholdTxPower,
       "hh3cPosaFcmThresholdAnswerTone": hh3cPosaFcmThresholdAnswerTone,
       "hh3cPosaCallerStatTable": hh3cPosaCallerStatTable,
       "hh3cPosaCallerStatEntry": hh3cPosaCallerStatEntry,
       "hh3cPosaCallerStatCallerID": hh3cPosaCallerStatCallerID,
       "hh3cPosaCallerRecvPkts": hh3cPosaCallerRecvPkts,
       "hh3cPosaCallerSendPkts": hh3cPosaCallerSendPkts,
       "hh3cPosaCallerErrPkts": hh3cPosaCallerErrPkts,
       "hh3cPosaCallerMapErrCnts": hh3cPosaCallerMapErrCnts,
       "hh3cPosaCallerInDiscardedPkts": hh3cPosaCallerInDiscardedPkts,
       "hh3cPosaCallerOutDiscardedPkts": hh3cPosaCallerOutDiscardedPkts,
       "hh3cPosaCallerStatRowStatus": hh3cPosaCallerStatRowStatus,
       "hh3cPosaTrap": hh3cPosaTrap,
       "hh3cPosaTrapPrex": hh3cPosaTrapPrex,
       "hh3cPosaServerStatusChange": hh3cPosaServerStatusChange,
       "hh3cPosaAppStateChange": hh3cPosaAppStateChange,
       "hh3cPosaTerminalHangUp": hh3cPosaTerminalHangUp,
       "hh3cPosaFcmLinkNegoFailed": hh3cPosaFcmLinkNegoFailed,
       "hh3cPosaFcmPhyNegoFailed": hh3cPosaFcmPhyNegoFailed,
       "hh3cPosaTcpConnectionExceed": hh3cPosaTcpConnectionExceed,
       "hh3cPosaFcmConnectionExceed": hh3cPosaFcmConnectionExceed,
       "hh3cPosaTcpTradeExceed": hh3cPosaTcpTradeExceed,
       "hh3cPosaTrapObjects": hh3cPosaTrapObjects,
       "hh3cPosaAppStateChangeObject": hh3cPosaAppStateChangeObject}
)
