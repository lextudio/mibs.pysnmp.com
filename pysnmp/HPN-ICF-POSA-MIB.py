# SNMP MIB module (HPN-ICF-POSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-POSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:29 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfPosa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92)
)
hpnicfPosa.setRevisions(
        ("2014-05-29 00:00",
         "2008-03-12 09:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfAppServiceType(Integer32, TextualConvention):
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



class HpnicfAppMode(Integer32, TextualConvention):
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



class HpnicfPeerState(Integer32, TextualConvention):
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



class HpnicfTerminalAccessType(Integer32, TextualConvention):
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



class HpnicfTpduChangeStrategy(Integer32, TextualConvention):
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

_HpnicfPosaControl_ObjectIdentity = ObjectIdentity
hpnicfPosaControl = _HpnicfPosaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1)
)


class _HpnicfPosaServerEnable_Type(Integer32):
    """Custom type hpnicfPosaServerEnable based on Integer32"""
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


_HpnicfPosaServerEnable_Type.__name__ = "Integer32"
_HpnicfPosaServerEnable_Object = MibScalar
hpnicfPosaServerEnable = _HpnicfPosaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 1),
    _HpnicfPosaServerEnable_Type()
)
hpnicfPosaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaServerEnable.setStatus("current")


class _HpnicfPosaFcmAnswerTimeout_Type(Integer32):
    """Custom type hpnicfPosaFcmAnswerTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_HpnicfPosaFcmAnswerTimeout_Type.__name__ = "Integer32"
_HpnicfPosaFcmAnswerTimeout_Object = MibScalar
hpnicfPosaFcmAnswerTimeout = _HpnicfPosaFcmAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 2),
    _HpnicfPosaFcmAnswerTimeout_Type()
)
hpnicfPosaFcmAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmAnswerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmAnswerTimeout.setUnits("milliseconds")


class _HpnicfPosaFcmTradeTimeout_Type(Integer32):
    """Custom type hpnicfPosaFcmTradeTimeout based on Integer32"""
    defaultValue = 12000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 12000000),
    )


_HpnicfPosaFcmTradeTimeout_Type.__name__ = "Integer32"
_HpnicfPosaFcmTradeTimeout_Object = MibScalar
hpnicfPosaFcmTradeTimeout = _HpnicfPosaFcmTradeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 3),
    _HpnicfPosaFcmTradeTimeout_Type()
)
hpnicfPosaFcmTradeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmTradeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmTradeTimeout.setUnits("milliseconds")


class _HpnicfPosaFcmIdleTimeout_Type(Integer32):
    """Custom type hpnicfPosaFcmIdleTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12000),
    )


_HpnicfPosaFcmIdleTimeout_Type.__name__ = "Integer32"
_HpnicfPosaFcmIdleTimeout_Object = MibScalar
hpnicfPosaFcmIdleTimeout = _HpnicfPosaFcmIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 4),
    _HpnicfPosaFcmIdleTimeout_Type()
)
hpnicfPosaFcmIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmIdleTimeout.setUnits("seconds")


class _HpnicfPosaSrvStateChangeTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaSrvStateChangeTrapEnable based on TruthValue"""


_HpnicfPosaSrvStateChangeTrapEnable_Object = MibScalar
hpnicfPosaSrvStateChangeTrapEnable = _HpnicfPosaSrvStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 5),
    _HpnicfPosaSrvStateChangeTrapEnable_Type()
)
hpnicfPosaSrvStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaSrvStateChangeTrapEnable.setStatus("current")


class _HpnicfPosaAppStateChangeTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaAppStateChangeTrapEnable based on TruthValue"""


_HpnicfPosaAppStateChangeTrapEnable_Object = MibScalar
hpnicfPosaAppStateChangeTrapEnable = _HpnicfPosaAppStateChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 6),
    _HpnicfPosaAppStateChangeTrapEnable_Type()
)
hpnicfPosaAppStateChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaAppStateChangeTrapEnable.setStatus("current")


class _HpnicfPosaTerminalHangUpTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaTerminalHangUpTrapEnable based on TruthValue"""


_HpnicfPosaTerminalHangUpTrapEnable_Object = MibScalar
hpnicfPosaTerminalHangUpTrapEnable = _HpnicfPosaTerminalHangUpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 7),
    _HpnicfPosaTerminalHangUpTrapEnable_Type()
)
hpnicfPosaTerminalHangUpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalHangUpTrapEnable.setStatus("current")


class _HpnicfPosaFcmLnkNegoFailTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaFcmLnkNegoFailTrapEnable based on TruthValue"""


_HpnicfPosaFcmLnkNegoFailTrapEnable_Object = MibScalar
hpnicfPosaFcmLnkNegoFailTrapEnable = _HpnicfPosaFcmLnkNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 8),
    _HpnicfPosaFcmLnkNegoFailTrapEnable_Type()
)
hpnicfPosaFcmLnkNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmLnkNegoFailTrapEnable.setStatus("current")


class _HpnicfPosaFcmPhyNegoFailTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaFcmPhyNegoFailTrapEnable based on TruthValue"""


_HpnicfPosaFcmPhyNegoFailTrapEnable_Object = MibScalar
hpnicfPosaFcmPhyNegoFailTrapEnable = _HpnicfPosaFcmPhyNegoFailTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 9),
    _HpnicfPosaFcmPhyNegoFailTrapEnable_Type()
)
hpnicfPosaFcmPhyNegoFailTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmPhyNegoFailTrapEnable.setStatus("current")
_HpnicfPosaTcpConnectionNumber_Type = Integer32
_HpnicfPosaTcpConnectionNumber_Object = MibScalar
hpnicfPosaTcpConnectionNumber = _HpnicfPosaTcpConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 10),
    _HpnicfPosaTcpConnectionNumber_Type()
)
hpnicfPosaTcpConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpConnectionNumber.setStatus("current")
_HpnicfPosaFcmConnectionNumber_Type = Integer32
_HpnicfPosaFcmConnectionNumber_Object = MibScalar
hpnicfPosaFcmConnectionNumber = _HpnicfPosaFcmConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 11),
    _HpnicfPosaFcmConnectionNumber_Type()
)
hpnicfPosaFcmConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaFcmConnectionNumber.setStatus("current")


class _HpnicfPosaTcpConnectionThreshold_Type(Integer32):
    """Custom type hpnicfPosaTcpConnectionThreshold based on Integer32"""
    defaultValue = 4096


_HpnicfPosaTcpConnectionThreshold_Object = MibScalar
hpnicfPosaTcpConnectionThreshold = _HpnicfPosaTcpConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 12),
    _HpnicfPosaTcpConnectionThreshold_Type()
)
hpnicfPosaTcpConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTcpConnectionThreshold.setStatus("current")


class _HpnicfPosaFcmConnectionThreshold_Type(Integer32):
    """Custom type hpnicfPosaFcmConnectionThreshold based on Integer32"""
    defaultValue = 255


_HpnicfPosaFcmConnectionThreshold_Object = MibScalar
hpnicfPosaFcmConnectionThreshold = _HpnicfPosaFcmConnectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 13),
    _HpnicfPosaFcmConnectionThreshold_Type()
)
hpnicfPosaFcmConnectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmConnectionThreshold.setStatus("current")


class _HpnicfPosaTcpConnectionTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaTcpConnectionTrapEnable based on TruthValue"""


_HpnicfPosaTcpConnectionTrapEnable_Object = MibScalar
hpnicfPosaTcpConnectionTrapEnable = _HpnicfPosaTcpConnectionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 14),
    _HpnicfPosaTcpConnectionTrapEnable_Type()
)
hpnicfPosaTcpConnectionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTcpConnectionTrapEnable.setStatus("current")


class _HpnicfPosaFcmConnectionTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaFcmConnectionTrapEnable based on TruthValue"""


_HpnicfPosaFcmConnectionTrapEnable_Object = MibScalar
hpnicfPosaFcmConnectionTrapEnable = _HpnicfPosaFcmConnectionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 15),
    _HpnicfPosaFcmConnectionTrapEnable_Type()
)
hpnicfPosaFcmConnectionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmConnectionTrapEnable.setStatus("current")


class _HpnicfPosaTcpTradeLimit_Type(Integer32):
    """Custom type hpnicfPosaTcpTradeLimit based on Integer32"""
    defaultValue = 0


_HpnicfPosaTcpTradeLimit_Object = MibScalar
hpnicfPosaTcpTradeLimit = _HpnicfPosaTcpTradeLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 16),
    _HpnicfPosaTcpTradeLimit_Type()
)
hpnicfPosaTcpTradeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTradeLimit.setStatus("current")


class _HpnicfPosaTcpTradeTrapEnable_Type(TruthValue):
    """Custom type hpnicfPosaTcpTradeTrapEnable based on TruthValue"""


_HpnicfPosaTcpTradeTrapEnable_Object = MibScalar
hpnicfPosaTcpTradeTrapEnable = _HpnicfPosaTcpTradeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 17),
    _HpnicfPosaTcpTradeTrapEnable_Type()
)
hpnicfPosaTcpTradeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTradeTrapEnable.setStatus("current")


class _HpnicfPosaTcpTradeTimeout_Type(Integer32):
    """Custom type hpnicfPosaTcpTradeTimeout based on Integer32"""
    defaultValue = 240


_HpnicfPosaTcpTradeTimeout_Object = MibScalar
hpnicfPosaTcpTradeTimeout = _HpnicfPosaTcpTradeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 1, 18),
    _HpnicfPosaTcpTradeTimeout_Type()
)
hpnicfPosaTcpTradeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTradeTimeout.setStatus("current")
_HpnicfPosaTables_ObjectIdentity = ObjectIdentity
hpnicfPosaTables = _HpnicfPosaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2)
)
_HpnicfPosaAppTable_Object = MibTable
hpnicfPosaAppTable = _HpnicfPosaAppTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfPosaAppTable.setStatus("current")
_HpnicfPosaAppEntry_Object = MibTableRow
hpnicfPosaAppEntry = _HpnicfPosaAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1)
)
hpnicfPosaAppEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaAppID"),
)
if mibBuilder.loadTexts:
    hpnicfPosaAppEntry.setStatus("current")


class _HpnicfPosaAppID_Type(Integer32):
    """Custom type hpnicfPosaAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfPosaAppID_Type.__name__ = "Integer32"
_HpnicfPosaAppID_Object = MibTableColumn
hpnicfPosaAppID = _HpnicfPosaAppID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 1),
    _HpnicfPosaAppID_Type()
)
hpnicfPosaAppID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPosaAppID.setStatus("current")


class _HpnicfPosaAppServiceType_Type(HpnicfAppServiceType):
    """Custom type hpnicfPosaAppServiceType based on HpnicfAppServiceType"""


_HpnicfPosaAppServiceType_Object = MibTableColumn
hpnicfPosaAppServiceType = _HpnicfPosaAppServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 2),
    _HpnicfPosaAppServiceType_Type()
)
hpnicfPosaAppServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppServiceType.setStatus("current")
_HpnicfPosaAppIfIndex_Type = Integer32
_HpnicfPosaAppIfIndex_Object = MibTableColumn
hpnicfPosaAppIfIndex = _HpnicfPosaAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 3),
    _HpnicfPosaAppIfIndex_Type()
)
hpnicfPosaAppIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppIfIndex.setStatus("current")


class _HpnicfPosaAppMode_Type(HpnicfAppMode):
    """Custom type hpnicfPosaAppMode based on HpnicfAppMode"""


_HpnicfPosaAppMode_Object = MibTableColumn
hpnicfPosaAppMode = _HpnicfPosaAppMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 4),
    _HpnicfPosaAppMode_Type()
)
hpnicfPosaAppMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppMode.setStatus("current")
_HpnicfPosaAppHostIPType_Type = InetAddressType
_HpnicfPosaAppHostIPType_Object = MibTableColumn
hpnicfPosaAppHostIPType = _HpnicfPosaAppHostIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 5),
    _HpnicfPosaAppHostIPType_Type()
)
hpnicfPosaAppHostIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppHostIPType.setStatus("current")
_HpnicfPosaAppHostIP_Type = InetAddress
_HpnicfPosaAppHostIP_Object = MibTableColumn
hpnicfPosaAppHostIP = _HpnicfPosaAppHostIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 6),
    _HpnicfPosaAppHostIP_Type()
)
hpnicfPosaAppHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppHostIP.setStatus("current")


class _HpnicfPosaAppHostPort_Type(Integer32):
    """Custom type hpnicfPosaAppHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPosaAppHostPort_Type.__name__ = "Integer32"
_HpnicfPosaAppHostPort_Object = MibTableColumn
hpnicfPosaAppHostPort = _HpnicfPosaAppHostPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 7),
    _HpnicfPosaAppHostPort_Type()
)
hpnicfPosaAppHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppHostPort.setStatus("current")
_HpnicfPosaAppRouterIPType_Type = InetAddressType
_HpnicfPosaAppRouterIPType_Object = MibTableColumn
hpnicfPosaAppRouterIPType = _HpnicfPosaAppRouterIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 8),
    _HpnicfPosaAppRouterIPType_Type()
)
hpnicfPosaAppRouterIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppRouterIPType.setStatus("current")
_HpnicfPosaAppRouterIP_Type = InetAddress
_HpnicfPosaAppRouterIP_Object = MibTableColumn
hpnicfPosaAppRouterIP = _HpnicfPosaAppRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 9),
    _HpnicfPosaAppRouterIP_Type()
)
hpnicfPosaAppRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppRouterIP.setStatus("current")


class _HpnicfPosaAppKeepAliveInterval_Type(Integer32):
    """Custom type hpnicfPosaAppKeepAliveInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_HpnicfPosaAppKeepAliveInterval_Type.__name__ = "Integer32"
_HpnicfPosaAppKeepAliveInterval_Object = MibTableColumn
hpnicfPosaAppKeepAliveInterval = _HpnicfPosaAppKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 10),
    _HpnicfPosaAppKeepAliveInterval_Type()
)
hpnicfPosaAppKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaAppKeepAliveInterval.setUnits("seconds")


class _HpnicfPosaAppKeepAliveCount_Type(Integer32):
    """Custom type hpnicfPosaAppKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_HpnicfPosaAppKeepAliveCount_Type.__name__ = "Integer32"
_HpnicfPosaAppKeepAliveCount_Object = MibTableColumn
hpnicfPosaAppKeepAliveCount = _HpnicfPosaAppKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 11),
    _HpnicfPosaAppKeepAliveCount_Type()
)
hpnicfPosaAppKeepAliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppKeepAliveCount.setStatus("current")


class _HpnicfPosaAppConnectTimeout_Type(Integer32):
    """Custom type hpnicfPosaAppConnectTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfPosaAppConnectTimeout_Type.__name__ = "Integer32"
_HpnicfPosaAppConnectTimeout_Object = MibTableColumn
hpnicfPosaAppConnectTimeout = _HpnicfPosaAppConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 12),
    _HpnicfPosaAppConnectTimeout_Type()
)
hpnicfPosaAppConnectTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppConnectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaAppConnectTimeout.setUnits("seconds")
_HpnicfPosaAppState_Type = HpnicfPeerState
_HpnicfPosaAppState_Object = MibTableColumn
hpnicfPosaAppState = _HpnicfPosaAppState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 13),
    _HpnicfPosaAppState_Type()
)
hpnicfPosaAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppState.setStatus("current")
_HpnicfPosaAppRowStatus_Type = RowStatus
_HpnicfPosaAppRowStatus_Object = MibTableColumn
hpnicfPosaAppRowStatus = _HpnicfPosaAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 14),
    _HpnicfPosaAppRowStatus_Type()
)
hpnicfPosaAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppRowStatus.setStatus("current")


class _HpnicfPosaAppName_Type(OctetString):
    """Custom type hpnicfPosaAppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfPosaAppName_Type.__name__ = "OctetString"
_HpnicfPosaAppName_Object = MibTableColumn
hpnicfPosaAppName = _HpnicfPosaAppName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 15),
    _HpnicfPosaAppName_Type()
)
hpnicfPosaAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppName.setStatus("current")


class _HpnicfPosaCallerIDTransEnable_Type(TruthValue):
    """Custom type hpnicfPosaCallerIDTransEnable based on TruthValue"""


_HpnicfPosaCallerIDTransEnable_Object = MibTableColumn
hpnicfPosaCallerIDTransEnable = _HpnicfPosaCallerIDTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 16),
    _HpnicfPosaCallerIDTransEnable_Type()
)
hpnicfPosaCallerIDTransEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaCallerIDTransEnable.setStatus("current")


class _HpnicfPosaTpduChangeStrategy_Type(HpnicfTpduChangeStrategy):
    """Custom type hpnicfPosaTpduChangeStrategy based on HpnicfTpduChangeStrategy"""


_HpnicfPosaTpduChangeStrategy_Object = MibTableColumn
hpnicfPosaTpduChangeStrategy = _HpnicfPosaTpduChangeStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 17),
    _HpnicfPosaTpduChangeStrategy_Type()
)
hpnicfPosaTpduChangeStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTpduChangeStrategy.setStatus("current")


class _HpnicfPosaBackupAppID_Type(Integer32):
    """Custom type hpnicfPosaBackupAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HpnicfPosaBackupAppID_Type.__name__ = "Integer32"
_HpnicfPosaBackupAppID_Object = MibTableColumn
hpnicfPosaBackupAppID = _HpnicfPosaBackupAppID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 18),
    _HpnicfPosaBackupAppID_Type()
)
hpnicfPosaBackupAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaBackupAppID.setStatus("current")


class _HpnicfPosaQuietTimeOut_Type(Integer32):
    """Custom type hpnicfPosaQuietTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_HpnicfPosaQuietTimeOut_Type.__name__ = "Integer32"
_HpnicfPosaQuietTimeOut_Object = MibTableColumn
hpnicfPosaQuietTimeOut = _HpnicfPosaQuietTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 19),
    _HpnicfPosaQuietTimeOut_Type()
)
hpnicfPosaQuietTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaQuietTimeOut.setStatus("current")


class _HpnicfPosaAppHello_Type(TruthValue):
    """Custom type hpnicfPosaAppHello based on TruthValue"""


_HpnicfPosaAppHello_Object = MibTableColumn
hpnicfPosaAppHello = _HpnicfPosaAppHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 20),
    _HpnicfPosaAppHello_Type()
)
hpnicfPosaAppHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppHello.setStatus("current")


class _HpnicfPosaAppHelloInterval_Type(Integer32):
    """Custom type hpnicfPosaAppHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HpnicfPosaAppHelloInterval_Type.__name__ = "Integer32"
_HpnicfPosaAppHelloInterval_Object = MibTableColumn
hpnicfPosaAppHelloInterval = _HpnicfPosaAppHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 21),
    _HpnicfPosaAppHelloInterval_Type()
)
hpnicfPosaAppHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppHelloInterval.setStatus("current")


class _HpnicfPosaAppRouterPort_Type(Integer32):
    """Custom type hpnicfPosaAppRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4999),
    )


_HpnicfPosaAppRouterPort_Type.__name__ = "Integer32"
_HpnicfPosaAppRouterPort_Object = MibTableColumn
hpnicfPosaAppRouterPort = _HpnicfPosaAppRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 1, 1, 22),
    _HpnicfPosaAppRouterPort_Type()
)
hpnicfPosaAppRouterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaAppRouterPort.setStatus("current")
_HpnicfPosaTerminalTable_Object = MibTable
hpnicfPosaTerminalTable = _HpnicfPosaTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfPosaTerminalTable.setStatus("current")
_HpnicfPosaTerminalEntry_Object = MibTableRow
hpnicfPosaTerminalEntry = _HpnicfPosaTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1)
)
hpnicfPosaTerminalEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaTerminalID"),
)
if mibBuilder.loadTexts:
    hpnicfPosaTerminalEntry.setStatus("current")


class _HpnicfPosaTerminalID_Type(Integer32):
    """Custom type hpnicfPosaTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfPosaTerminalID_Type.__name__ = "Integer32"
_HpnicfPosaTerminalID_Object = MibTableColumn
hpnicfPosaTerminalID = _HpnicfPosaTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 1),
    _HpnicfPosaTerminalID_Type()
)
hpnicfPosaTerminalID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalID.setStatus("current")


class _HpnicfPosaTerminalAccessType_Type(HpnicfTerminalAccessType):
    """Custom type hpnicfPosaTerminalAccessType based on HpnicfTerminalAccessType"""


_HpnicfPosaTerminalAccessType_Object = MibTableColumn
hpnicfPosaTerminalAccessType = _HpnicfPosaTerminalAccessType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 2),
    _HpnicfPosaTerminalAccessType_Type()
)
hpnicfPosaTerminalAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalAccessType.setStatus("current")
_HpnicfPosaTerminalIfIndex_Type = Integer32
_HpnicfPosaTerminalIfIndex_Object = MibTableColumn
hpnicfPosaTerminalIfIndex = _HpnicfPosaTerminalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 3),
    _HpnicfPosaTerminalIfIndex_Type()
)
hpnicfPosaTerminalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalIfIndex.setStatus("current")


class _HpnicfPosaTerminalTransAppID_Type(Integer32):
    """Custom type hpnicfPosaTerminalTransAppID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HpnicfPosaTerminalTransAppID_Type.__name__ = "Integer32"
_HpnicfPosaTerminalTransAppID_Object = MibTableColumn
hpnicfPosaTerminalTransAppID = _HpnicfPosaTerminalTransAppID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 4),
    _HpnicfPosaTerminalTransAppID_Type()
)
hpnicfPosaTerminalTransAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalTransAppID.setStatus("current")


class _HpnicfPosaTerminalListenPort_Type(Integer32):
    """Custom type hpnicfPosaTerminalListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPosaTerminalListenPort_Type.__name__ = "Integer32"
_HpnicfPosaTerminalListenPort_Object = MibTableColumn
hpnicfPosaTerminalListenPort = _HpnicfPosaTerminalListenPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 5),
    _HpnicfPosaTerminalListenPort_Type()
)
hpnicfPosaTerminalListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalListenPort.setStatus("current")
_HpnicfPosaTerminalState_Type = HpnicfPeerState
_HpnicfPosaTerminalState_Object = MibTableColumn
hpnicfPosaTerminalState = _HpnicfPosaTerminalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 6),
    _HpnicfPosaTerminalState_Type()
)
hpnicfPosaTerminalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalState.setStatus("current")
_HpnicfPosaTerminalRowStatus_Type = RowStatus
_HpnicfPosaTerminalRowStatus_Object = MibTableColumn
hpnicfPosaTerminalRowStatus = _HpnicfPosaTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 7),
    _HpnicfPosaTerminalRowStatus_Type()
)
hpnicfPosaTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalRowStatus.setStatus("current")


class _HpnicfPosaTerminalName_Type(OctetString):
    """Custom type hpnicfPosaTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfPosaTerminalName_Type.__name__ = "OctetString"
_HpnicfPosaTerminalName_Object = MibTableColumn
hpnicfPosaTerminalName = _HpnicfPosaTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 8),
    _HpnicfPosaTerminalName_Type()
)
hpnicfPosaTerminalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalName.setStatus("current")
_HpnicfPosaTerminalCfgIfIndex_Type = Integer32
_HpnicfPosaTerminalCfgIfIndex_Object = MibTableColumn
hpnicfPosaTerminalCfgIfIndex = _HpnicfPosaTerminalCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 2, 1, 9),
    _HpnicfPosaTerminalCfgIfIndex_Type()
)
hpnicfPosaTerminalCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalCfgIfIndex.setStatus("current")
_HpnicfPosaMapTable_Object = MibTable
hpnicfPosaMapTable = _HpnicfPosaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfPosaMapTable.setStatus("current")
_HpnicfPosaMapEntry_Object = MibTableRow
hpnicfPosaMapEntry = _HpnicfPosaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3, 1)
)
hpnicfPosaMapEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaMapSrcCode"),
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaMapDestCode"),
)
if mibBuilder.loadTexts:
    hpnicfPosaMapEntry.setStatus("current")


class _HpnicfPosaMapDestCode_Type(OctetString):
    """Custom type hpnicfPosaMapDestCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_HpnicfPosaMapDestCode_Type.__name__ = "OctetString"
_HpnicfPosaMapDestCode_Object = MibTableColumn
hpnicfPosaMapDestCode = _HpnicfPosaMapDestCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3, 1, 1),
    _HpnicfPosaMapDestCode_Type()
)
hpnicfPosaMapDestCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPosaMapDestCode.setStatus("current")


class _HpnicfPosaMapAppID_Type(Integer32):
    """Custom type hpnicfPosaMapAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfPosaMapAppID_Type.__name__ = "Integer32"
_HpnicfPosaMapAppID_Object = MibTableColumn
hpnicfPosaMapAppID = _HpnicfPosaMapAppID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3, 1, 2),
    _HpnicfPosaMapAppID_Type()
)
hpnicfPosaMapAppID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaMapAppID.setStatus("current")
_HpnicfPosaMapRowStatus_Type = RowStatus
_HpnicfPosaMapRowStatus_Object = MibTableColumn
hpnicfPosaMapRowStatus = _HpnicfPosaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3, 1, 3),
    _HpnicfPosaMapRowStatus_Type()
)
hpnicfPosaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaMapRowStatus.setStatus("current")


class _HpnicfPosaMapSrcCode_Type(OctetString):
    """Custom type hpnicfPosaMapSrcCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 7),
    )


_HpnicfPosaMapSrcCode_Type.__name__ = "OctetString"
_HpnicfPosaMapSrcCode_Object = MibTableColumn
hpnicfPosaMapSrcCode = _HpnicfPosaMapSrcCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 3, 1, 4),
    _HpnicfPosaMapSrcCode_Type()
)
hpnicfPosaMapSrcCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPosaMapSrcCode.setStatus("current")
_HpnicfPosaFcmStatTable_Object = MibTable
hpnicfPosaFcmStatTable = _HpnicfPosaFcmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatTable.setStatus("current")
_HpnicfPosaFcmStatEntry_Object = MibTableRow
hpnicfPosaFcmStatEntry = _HpnicfPosaFcmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1)
)
hpnicfPosaFcmStatEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaFcmStatIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatEntry.setStatus("current")


class _HpnicfPosaFcmStatIfIndex_Type(Integer32):
    """Custom type hpnicfPosaFcmStatIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPosaFcmStatIfIndex_Type.__name__ = "Integer32"
_HpnicfPosaFcmStatIfIndex_Object = MibTableColumn
hpnicfPosaFcmStatIfIndex = _HpnicfPosaFcmStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 1),
    _HpnicfPosaFcmStatIfIndex_Type()
)
hpnicfPosaFcmStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatIfIndex.setStatus("current")
_HpnicfPosaFcmStatTimeoutCnts_Type = Counter32
_HpnicfPosaFcmStatTimeoutCnts_Object = MibTableColumn
hpnicfPosaFcmStatTimeoutCnts = _HpnicfPosaFcmStatTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 2),
    _HpnicfPosaFcmStatTimeoutCnts_Type()
)
hpnicfPosaFcmStatTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatTimeoutCnts.setStatus("current")
_HpnicfPosaFcmStatConnectFailCnts_Type = Counter32
_HpnicfPosaFcmStatConnectFailCnts_Object = MibTableColumn
hpnicfPosaFcmStatConnectFailCnts = _HpnicfPosaFcmStatConnectFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 3),
    _HpnicfPosaFcmStatConnectFailCnts_Type()
)
hpnicfPosaFcmStatConnectFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatConnectFailCnts.setStatus("current")
_HpnicfPosaFcmStatTransCnts_Type = Gauge32
_HpnicfPosaFcmStatTransCnts_Object = MibTableColumn
hpnicfPosaFcmStatTransCnts = _HpnicfPosaFcmStatTransCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 4),
    _HpnicfPosaFcmStatTransCnts_Type()
)
hpnicfPosaFcmStatTransCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatTransCnts.setStatus("current")
_HpnicfPosaFcmStatTransSuccessCnts_Type = Gauge32
_HpnicfPosaFcmStatTransSuccessCnts_Object = MibTableColumn
hpnicfPosaFcmStatTransSuccessCnts = _HpnicfPosaFcmStatTransSuccessCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 5),
    _HpnicfPosaFcmStatTransSuccessCnts_Type()
)
hpnicfPosaFcmStatTransSuccessCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatTransSuccessCnts.setStatus("current")


class _HpnicfPosaFcmStatTransCntsClear_Type(TruthValue):
    """Custom type hpnicfPosaFcmStatTransCntsClear based on TruthValue"""


_HpnicfPosaFcmStatTransCntsClear_Object = MibTableColumn
hpnicfPosaFcmStatTransCntsClear = _HpnicfPosaFcmStatTransCntsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 4, 1, 6),
    _HpnicfPosaFcmStatTransCntsClear_Type()
)
hpnicfPosaFcmStatTransCntsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmStatTransCntsClear.setStatus("current")
_HpnicfPosaAppStatTable_Object = MibTable
hpnicfPosaAppStatTable = _HpnicfPosaAppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfPosaAppStatTable.setStatus("current")
_HpnicfPosaAppStatEntry_Object = MibTableRow
hpnicfPosaAppStatEntry = _HpnicfPosaAppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1)
)
hpnicfPosaAppStatEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaAppID"),
)
if mibBuilder.loadTexts:
    hpnicfPosaAppStatEntry.setStatus("current")
_HpnicfPosaAppRecvPkts_Type = Counter32
_HpnicfPosaAppRecvPkts_Object = MibTableColumn
hpnicfPosaAppRecvPkts = _HpnicfPosaAppRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 1),
    _HpnicfPosaAppRecvPkts_Type()
)
hpnicfPosaAppRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppRecvPkts.setStatus("current")
_HpnicfPosaAppSendPkts_Type = Counter32
_HpnicfPosaAppSendPkts_Object = MibTableColumn
hpnicfPosaAppSendPkts = _HpnicfPosaAppSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 2),
    _HpnicfPosaAppSendPkts_Type()
)
hpnicfPosaAppSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppSendPkts.setStatus("current")
_HpnicfPosaAppErrPkts_Type = Counter32
_HpnicfPosaAppErrPkts_Object = MibTableColumn
hpnicfPosaAppErrPkts = _HpnicfPosaAppErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 3),
    _HpnicfPosaAppErrPkts_Type()
)
hpnicfPosaAppErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppErrPkts.setStatus("current")
_HpnicfPosaAppDistributeErrCnts_Type = Counter32
_HpnicfPosaAppDistributeErrCnts_Object = MibTableColumn
hpnicfPosaAppDistributeErrCnts = _HpnicfPosaAppDistributeErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 4),
    _HpnicfPosaAppDistributeErrCnts_Type()
)
hpnicfPosaAppDistributeErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppDistributeErrCnts.setStatus("current")
_HpnicfPosaAppInDiscardedPkts_Type = Counter32
_HpnicfPosaAppInDiscardedPkts_Object = MibTableColumn
hpnicfPosaAppInDiscardedPkts = _HpnicfPosaAppInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 5),
    _HpnicfPosaAppInDiscardedPkts_Type()
)
hpnicfPosaAppInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppInDiscardedPkts.setStatus("current")
_HpnicfPosaAppOutDiscardedPkts_Type = Counter32
_HpnicfPosaAppOutDiscardedPkts_Object = MibTableColumn
hpnicfPosaAppOutDiscardedPkts = _HpnicfPosaAppOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 5, 1, 6),
    _HpnicfPosaAppOutDiscardedPkts_Type()
)
hpnicfPosaAppOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaAppOutDiscardedPkts.setStatus("current")
_HpnicfPosaTerminalStatTable_Object = MibTable
hpnicfPosaTerminalStatTable = _HpnicfPosaTerminalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfPosaTerminalStatTable.setStatus("current")
_HpnicfPosaTerminalStatEntry_Object = MibTableRow
hpnicfPosaTerminalStatEntry = _HpnicfPosaTerminalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1)
)
hpnicfPosaTerminalStatEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaTerminalID"),
)
if mibBuilder.loadTexts:
    hpnicfPosaTerminalStatEntry.setStatus("current")
_HpnicfPosaTerminalRecvPkts_Type = Counter32
_HpnicfPosaTerminalRecvPkts_Object = MibTableColumn
hpnicfPosaTerminalRecvPkts = _HpnicfPosaTerminalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 1),
    _HpnicfPosaTerminalRecvPkts_Type()
)
hpnicfPosaTerminalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalRecvPkts.setStatus("current")
_HpnicfPosaTerminalSendPkts_Type = Counter32
_HpnicfPosaTerminalSendPkts_Object = MibTableColumn
hpnicfPosaTerminalSendPkts = _HpnicfPosaTerminalSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 2),
    _HpnicfPosaTerminalSendPkts_Type()
)
hpnicfPosaTerminalSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalSendPkts.setStatus("current")
_HpnicfPosaTerminalErrPkts_Type = Counter32
_HpnicfPosaTerminalErrPkts_Object = MibTableColumn
hpnicfPosaTerminalErrPkts = _HpnicfPosaTerminalErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 3),
    _HpnicfPosaTerminalErrPkts_Type()
)
hpnicfPosaTerminalErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalErrPkts.setStatus("current")
_HpnicfPosaTerminalMapErrCnts_Type = Counter32
_HpnicfPosaTerminalMapErrCnts_Object = MibTableColumn
hpnicfPosaTerminalMapErrCnts = _HpnicfPosaTerminalMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 4),
    _HpnicfPosaTerminalMapErrCnts_Type()
)
hpnicfPosaTerminalMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalMapErrCnts.setStatus("current")
_HpnicfPosaTerminalInDiscardedPkts_Type = Counter32
_HpnicfPosaTerminalInDiscardedPkts_Object = MibTableColumn
hpnicfPosaTerminalInDiscardedPkts = _HpnicfPosaTerminalInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 5),
    _HpnicfPosaTerminalInDiscardedPkts_Type()
)
hpnicfPosaTerminalInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalInDiscardedPkts.setStatus("current")
_HpnicfPosaTerminalOutDiscardedPkts_Type = Counter32
_HpnicfPosaTerminalOutDiscardedPkts_Object = MibTableColumn
hpnicfPosaTerminalOutDiscardedPkts = _HpnicfPosaTerminalOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 6, 1, 6),
    _HpnicfPosaTerminalOutDiscardedPkts_Type()
)
hpnicfPosaTerminalOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTerminalOutDiscardedPkts.setStatus("current")
_HpnicfPosaBatchTerminalTable_Object = MibTable
hpnicfPosaBatchTerminalTable = _HpnicfPosaBatchTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfPosaBatchTerminalTable.setStatus("current")
_HpnicfPosaBatchTerminalEntry_Object = MibTableRow
hpnicfPosaBatchTerminalEntry = _HpnicfPosaBatchTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 7, 1)
)
hpnicfPosaBatchTerminalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPosaBatchTerminalEntry.setStatus("current")


class _HpnicfPosaBatchTerminalFirstID_Type(Integer32):
    """Custom type hpnicfPosaBatchTerminalFirstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfPosaBatchTerminalFirstID_Type.__name__ = "Integer32"
_HpnicfPosaBatchTerminalFirstID_Object = MibTableColumn
hpnicfPosaBatchTerminalFirstID = _HpnicfPosaBatchTerminalFirstID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 7, 1, 1),
    _HpnicfPosaBatchTerminalFirstID_Type()
)
hpnicfPosaBatchTerminalFirstID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaBatchTerminalFirstID.setStatus("current")
_HpnicfPosaBatchTerminalRowStatus_Type = RowStatus
_HpnicfPosaBatchTerminalRowStatus_Object = MibTableColumn
hpnicfPosaBatchTerminalRowStatus = _HpnicfPosaBatchTerminalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 7, 1, 2),
    _HpnicfPosaBatchTerminalRowStatus_Type()
)
hpnicfPosaBatchTerminalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaBatchTerminalRowStatus.setStatus("current")
_HpnicfPosaTcpTermStatTable_Object = MibTable
hpnicfPosaTcpTermStatTable = _HpnicfPosaTcpTermStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatTable.setStatus("current")
_HpnicfPosaTcpTermStatEntry_Object = MibTableRow
hpnicfPosaTcpTermStatEntry = _HpnicfPosaTcpTermStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1)
)
hpnicfPosaTcpTermStatEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaTcpTermStatIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatEntry.setStatus("current")


class _HpnicfPosaTcpTermStatIndex_Type(Integer32):
    """Custom type hpnicfPosaTcpTermStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfPosaTcpTermStatIndex_Type.__name__ = "Integer32"
_HpnicfPosaTcpTermStatIndex_Object = MibTableColumn
hpnicfPosaTcpTermStatIndex = _HpnicfPosaTcpTermStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 1),
    _HpnicfPosaTcpTermStatIndex_Type()
)
hpnicfPosaTcpTermStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatIndex.setStatus("current")
_HpnicfPosaTcpTermStatIPType_Type = InetAddressType
_HpnicfPosaTcpTermStatIPType_Object = MibTableColumn
hpnicfPosaTcpTermStatIPType = _HpnicfPosaTcpTermStatIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 2),
    _HpnicfPosaTcpTermStatIPType_Type()
)
hpnicfPosaTcpTermStatIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatIPType.setStatus("current")
_HpnicfPosaTcpTermStatIP_Type = InetAddress
_HpnicfPosaTcpTermStatIP_Object = MibTableColumn
hpnicfPosaTcpTermStatIP = _HpnicfPosaTcpTermStatIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 3),
    _HpnicfPosaTcpTermStatIP_Type()
)
hpnicfPosaTcpTermStatIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatIP.setStatus("current")
_HpnicfPosaTcpTermStatIPMask_Type = InetAddress
_HpnicfPosaTcpTermStatIPMask_Object = MibTableColumn
hpnicfPosaTcpTermStatIPMask = _HpnicfPosaTcpTermStatIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 4),
    _HpnicfPosaTcpTermStatIPMask_Type()
)
hpnicfPosaTcpTermStatIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatIPMask.setStatus("current")
_HpnicfPosaTcpTermRecvPkts_Type = Counter64
_HpnicfPosaTcpTermRecvPkts_Object = MibTableColumn
hpnicfPosaTcpTermRecvPkts = _HpnicfPosaTcpTermRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 5),
    _HpnicfPosaTcpTermRecvPkts_Type()
)
hpnicfPosaTcpTermRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermRecvPkts.setStatus("current")
_HpnicfPosaTcpTermSendPkts_Type = Counter64
_HpnicfPosaTcpTermSendPkts_Object = MibTableColumn
hpnicfPosaTcpTermSendPkts = _HpnicfPosaTcpTermSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 6),
    _HpnicfPosaTcpTermSendPkts_Type()
)
hpnicfPosaTcpTermSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermSendPkts.setStatus("current")
_HpnicfPosaTcpTermErrPkts_Type = Counter64
_HpnicfPosaTcpTermErrPkts_Object = MibTableColumn
hpnicfPosaTcpTermErrPkts = _HpnicfPosaTcpTermErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 7),
    _HpnicfPosaTcpTermErrPkts_Type()
)
hpnicfPosaTcpTermErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermErrPkts.setStatus("current")
_HpnicfPosaTcpTermMapErrCnts_Type = Counter64
_HpnicfPosaTcpTermMapErrCnts_Object = MibTableColumn
hpnicfPosaTcpTermMapErrCnts = _HpnicfPosaTcpTermMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 8),
    _HpnicfPosaTcpTermMapErrCnts_Type()
)
hpnicfPosaTcpTermMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermMapErrCnts.setStatus("current")
_HpnicfPosaTcpTermInDiscardedPkts_Type = Counter64
_HpnicfPosaTcpTermInDiscardedPkts_Object = MibTableColumn
hpnicfPosaTcpTermInDiscardedPkts = _HpnicfPosaTcpTermInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 9),
    _HpnicfPosaTcpTermInDiscardedPkts_Type()
)
hpnicfPosaTcpTermInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermInDiscardedPkts.setStatus("current")
_HpnicfPosaTcpTermOutDiscardedPkts_Type = Counter64
_HpnicfPosaTcpTermOutDiscardedPkts_Object = MibTableColumn
hpnicfPosaTcpTermOutDiscardedPkts = _HpnicfPosaTcpTermOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 10),
    _HpnicfPosaTcpTermOutDiscardedPkts_Type()
)
hpnicfPosaTcpTermOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermOutDiscardedPkts.setStatus("current")
_HpnicfPosaTcpTermStatRowStatus_Type = RowStatus
_HpnicfPosaTcpTermStatRowStatus_Object = MibTableColumn
hpnicfPosaTcpTermStatRowStatus = _HpnicfPosaTcpTermStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 8, 1, 11),
    _HpnicfPosaTcpTermStatRowStatus_Type()
)
hpnicfPosaTcpTermStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaTcpTermStatRowStatus.setStatus("current")
_HpnicfPosaFcmConfTable_Object = MibTable
hpnicfPosaFcmConfTable = _HpnicfPosaFcmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmConfTable.setStatus("current")
_HpnicfPosaFcmConfEntry_Object = MibTableRow
hpnicfPosaFcmConfEntry = _HpnicfPosaFcmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1)
)
hpnicfPosaFcmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmConfEntry.setStatus("current")


class _HpnicfPosaFcmNegoHookOff_Type(Integer32):
    """Custom type hpnicfPosaFcmNegoHookOff based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 6000),
    )


_HpnicfPosaFcmNegoHookOff_Type.__name__ = "Integer32"
_HpnicfPosaFcmNegoHookOff_Object = MibTableColumn
hpnicfPosaFcmNegoHookOff = _HpnicfPosaFcmNegoHookOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 1),
    _HpnicfPosaFcmNegoHookOff_Type()
)
hpnicfPosaFcmNegoHookOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoHookOff.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoHookOff.setUnits("milliseconds")


class _HpnicfPosaFcmNegoSilence_Type(Integer32):
    """Custom type hpnicfPosaFcmNegoSilence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_HpnicfPosaFcmNegoSilence_Type.__name__ = "Integer32"
_HpnicfPosaFcmNegoSilence_Object = MibTableColumn
hpnicfPosaFcmNegoSilence = _HpnicfPosaFcmNegoSilence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 2),
    _HpnicfPosaFcmNegoSilence_Type()
)
hpnicfPosaFcmNegoSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoSilence.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoSilence.setUnits("milliseconds")


class _HpnicfPosaFcmNegoScrmbBinary1_Type(Integer32):
    """Custom type hpnicfPosaFcmNegoScrmbBinary1 based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_HpnicfPosaFcmNegoScrmbBinary1_Type.__name__ = "Integer32"
_HpnicfPosaFcmNegoScrmbBinary1_Object = MibTableColumn
hpnicfPosaFcmNegoScrmbBinary1 = _HpnicfPosaFcmNegoScrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 3),
    _HpnicfPosaFcmNegoScrmbBinary1_Type()
)
hpnicfPosaFcmNegoScrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoScrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoScrmbBinary1.setUnits("milliseconds")


class _HpnicfPosaFcmNegoUnscrmbBinary1_Type(Integer32):
    """Custom type hpnicfPosaFcmNegoUnscrmbBinary1 based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1500),
    )


_HpnicfPosaFcmNegoUnscrmbBinary1_Type.__name__ = "Integer32"
_HpnicfPosaFcmNegoUnscrmbBinary1_Object = MibTableColumn
hpnicfPosaFcmNegoUnscrmbBinary1 = _HpnicfPosaFcmNegoUnscrmbBinary1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 4),
    _HpnicfPosaFcmNegoUnscrmbBinary1_Type()
)
hpnicfPosaFcmNegoUnscrmbBinary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoUnscrmbBinary1.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmNegoUnscrmbBinary1.setUnits("milliseconds")


class _HpnicfPosaFcmThresholdRlsdOff_Type(Integer32):
    """Custom type hpnicfPosaFcmThresholdRlsdOff based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_HpnicfPosaFcmThresholdRlsdOff_Type.__name__ = "Integer32"
_HpnicfPosaFcmThresholdRlsdOff_Object = MibTableColumn
hpnicfPosaFcmThresholdRlsdOff = _HpnicfPosaFcmThresholdRlsdOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 5),
    _HpnicfPosaFcmThresholdRlsdOff_Type()
)
hpnicfPosaFcmThresholdRlsdOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdRlsdOff.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdRlsdOff.setUnits("-dBm")


class _HpnicfPosaFcmThresholdRlsdOn_Type(Integer32):
    """Custom type hpnicfPosaFcmThresholdRlsdOn based on Integer32"""
    defaultValue = 43

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 75),
    )


_HpnicfPosaFcmThresholdRlsdOn_Type.__name__ = "Integer32"
_HpnicfPosaFcmThresholdRlsdOn_Object = MibTableColumn
hpnicfPosaFcmThresholdRlsdOn = _HpnicfPosaFcmThresholdRlsdOn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 6),
    _HpnicfPosaFcmThresholdRlsdOn_Type()
)
hpnicfPosaFcmThresholdRlsdOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdRlsdOn.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdRlsdOn.setUnits("-dBm")


class _HpnicfPosaFcmThresholdTxPower_Type(Integer32):
    """Custom type hpnicfPosaFcmThresholdTxPower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_HpnicfPosaFcmThresholdTxPower_Type.__name__ = "Integer32"
_HpnicfPosaFcmThresholdTxPower_Object = MibTableColumn
hpnicfPosaFcmThresholdTxPower = _HpnicfPosaFcmThresholdTxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 7),
    _HpnicfPosaFcmThresholdTxPower_Type()
)
hpnicfPosaFcmThresholdTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdTxPower.setUnits("-dBm")


class _HpnicfPosaFcmThresholdAnswerTone_Type(Integer32):
    """Custom type hpnicfPosaFcmThresholdAnswerTone based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_HpnicfPosaFcmThresholdAnswerTone_Type.__name__ = "Integer32"
_HpnicfPosaFcmThresholdAnswerTone_Object = MibTableColumn
hpnicfPosaFcmThresholdAnswerTone = _HpnicfPosaFcmThresholdAnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 9, 1, 8),
    _HpnicfPosaFcmThresholdAnswerTone_Type()
)
hpnicfPosaFcmThresholdAnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdAnswerTone.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPosaFcmThresholdAnswerTone.setUnits("-dBm")
_HpnicfPosaCallerStatTable_Object = MibTable
hpnicfPosaCallerStatTable = _HpnicfPosaCallerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfPosaCallerStatTable.setStatus("current")
_HpnicfPosaCallerStatEntry_Object = MibTableRow
hpnicfPosaCallerStatEntry = _HpnicfPosaCallerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1)
)
hpnicfPosaCallerStatEntry.setIndexNames(
    (0, "HPN-ICF-POSA-MIB", "hpnicfPosaCallerStatCallerID"),
)
if mibBuilder.loadTexts:
    hpnicfPosaCallerStatEntry.setStatus("current")


class _HpnicfPosaCallerStatCallerID_Type(OctetString):
    """Custom type hpnicfPosaCallerStatCallerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfPosaCallerStatCallerID_Type.__name__ = "OctetString"
_HpnicfPosaCallerStatCallerID_Object = MibTableColumn
hpnicfPosaCallerStatCallerID = _HpnicfPosaCallerStatCallerID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 1),
    _HpnicfPosaCallerStatCallerID_Type()
)
hpnicfPosaCallerStatCallerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPosaCallerStatCallerID.setStatus("current")
_HpnicfPosaCallerRecvPkts_Type = Counter64
_HpnicfPosaCallerRecvPkts_Object = MibTableColumn
hpnicfPosaCallerRecvPkts = _HpnicfPosaCallerRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 2),
    _HpnicfPosaCallerRecvPkts_Type()
)
hpnicfPosaCallerRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerRecvPkts.setStatus("current")
_HpnicfPosaCallerSendPkts_Type = Counter64
_HpnicfPosaCallerSendPkts_Object = MibTableColumn
hpnicfPosaCallerSendPkts = _HpnicfPosaCallerSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 3),
    _HpnicfPosaCallerSendPkts_Type()
)
hpnicfPosaCallerSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerSendPkts.setStatus("current")
_HpnicfPosaCallerErrPkts_Type = Counter64
_HpnicfPosaCallerErrPkts_Object = MibTableColumn
hpnicfPosaCallerErrPkts = _HpnicfPosaCallerErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 4),
    _HpnicfPosaCallerErrPkts_Type()
)
hpnicfPosaCallerErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerErrPkts.setStatus("current")
_HpnicfPosaCallerMapErrCnts_Type = Counter64
_HpnicfPosaCallerMapErrCnts_Object = MibTableColumn
hpnicfPosaCallerMapErrCnts = _HpnicfPosaCallerMapErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 5),
    _HpnicfPosaCallerMapErrCnts_Type()
)
hpnicfPosaCallerMapErrCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerMapErrCnts.setStatus("current")
_HpnicfPosaCallerInDiscardedPkts_Type = Counter64
_HpnicfPosaCallerInDiscardedPkts_Object = MibTableColumn
hpnicfPosaCallerInDiscardedPkts = _HpnicfPosaCallerInDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 6),
    _HpnicfPosaCallerInDiscardedPkts_Type()
)
hpnicfPosaCallerInDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerInDiscardedPkts.setStatus("current")
_HpnicfPosaCallerOutDiscardedPkts_Type = Counter64
_HpnicfPosaCallerOutDiscardedPkts_Object = MibTableColumn
hpnicfPosaCallerOutDiscardedPkts = _HpnicfPosaCallerOutDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 7),
    _HpnicfPosaCallerOutDiscardedPkts_Type()
)
hpnicfPosaCallerOutDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPosaCallerOutDiscardedPkts.setStatus("current")
_HpnicfPosaCallerStatRowStatus_Type = RowStatus
_HpnicfPosaCallerStatRowStatus_Object = MibTableColumn
hpnicfPosaCallerStatRowStatus = _HpnicfPosaCallerStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 2, 10, 1, 8),
    _HpnicfPosaCallerStatRowStatus_Type()
)
hpnicfPosaCallerStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPosaCallerStatRowStatus.setStatus("current")
_HpnicfPosaTrap_ObjectIdentity = ObjectIdentity
hpnicfPosaTrap = _HpnicfPosaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3)
)
_HpnicfPosaTrapPrex_ObjectIdentity = ObjectIdentity
hpnicfPosaTrapPrex = _HpnicfPosaTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0)
)
_HpnicfPosaTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfPosaTrapObjects = _HpnicfPosaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 1)
)


class _HpnicfPosaAppStateChangeObject_Type(Integer32):
    """Custom type hpnicfPosaAppStateChangeObject based on Integer32"""
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


_HpnicfPosaAppStateChangeObject_Type.__name__ = "Integer32"
_HpnicfPosaAppStateChangeObject_Object = MibScalar
hpnicfPosaAppStateChangeObject = _HpnicfPosaAppStateChangeObject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 1, 1),
    _HpnicfPosaAppStateChangeObject_Type()
)
hpnicfPosaAppStateChangeObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPosaAppStateChangeObject.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfPosaServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 1)
)
hpnicfPosaServerStatusChange.setObjects(
    ("HPN-ICF-POSA-MIB", "hpnicfPosaServerEnable")
)
if mibBuilder.loadTexts:
    hpnicfPosaServerStatusChange.setStatus(
        "current"
    )

hpnicfPosaAppStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 2)
)
hpnicfPosaAppStateChange.setObjects(
      *(("HPN-ICF-POSA-MIB", "hpnicfPosaAppID"),
        ("HPN-ICF-POSA-MIB", "hpnicfPosaAppStateChangeObject"))
)
if mibBuilder.loadTexts:
    hpnicfPosaAppStateChange.setStatus(
        "current"
    )

hpnicfPosaTerminalHangUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 3)
)
hpnicfPosaTerminalHangUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosaTerminalHangUp.setStatus(
        "current"
    )

hpnicfPosaFcmLinkNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 4)
)
hpnicfPosaFcmLinkNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmLinkNegoFailed.setStatus(
        "current"
    )

hpnicfPosaFcmPhyNegoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 5)
)
hpnicfPosaFcmPhyNegoFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmPhyNegoFailed.setStatus(
        "current"
    )

hpnicfPosaTcpConnectionExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 6)
)
hpnicfPosaTcpConnectionExceed.setObjects(
    ("HPN-ICF-POSA-MIB", "hpnicfPosaTcpConnectionThreshold")
)
if mibBuilder.loadTexts:
    hpnicfPosaTcpConnectionExceed.setStatus(
        "current"
    )

hpnicfPosaFcmConnectionExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 7)
)
hpnicfPosaFcmConnectionExceed.setObjects(
    ("HPN-ICF-POSA-MIB", "hpnicfPosaFcmConnectionThreshold")
)
if mibBuilder.loadTexts:
    hpnicfPosaFcmConnectionExceed.setStatus(
        "current"
    )

hpnicfPosaTcpTradeExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92, 3, 0, 8)
)
hpnicfPosaTcpTradeExceed.setObjects(
      *(("HPN-ICF-POSA-MIB", "hpnicfPosaTcpTradeLimit"),
        ("HPN-ICF-POSA-MIB", "hpnicfPosaTerminalID"))
)
if mibBuilder.loadTexts:
    hpnicfPosaTcpTradeExceed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-POSA-MIB",
    **{"HpnicfAppServiceType": HpnicfAppServiceType,
       "HpnicfAppMode": HpnicfAppMode,
       "HpnicfPeerState": HpnicfPeerState,
       "HpnicfTerminalAccessType": HpnicfTerminalAccessType,
       "HpnicfTpduChangeStrategy": HpnicfTpduChangeStrategy,
       "hpnicfPosa": hpnicfPosa,
       "hpnicfPosaControl": hpnicfPosaControl,
       "hpnicfPosaServerEnable": hpnicfPosaServerEnable,
       "hpnicfPosaFcmAnswerTimeout": hpnicfPosaFcmAnswerTimeout,
       "hpnicfPosaFcmTradeTimeout": hpnicfPosaFcmTradeTimeout,
       "hpnicfPosaFcmIdleTimeout": hpnicfPosaFcmIdleTimeout,
       "hpnicfPosaSrvStateChangeTrapEnable": hpnicfPosaSrvStateChangeTrapEnable,
       "hpnicfPosaAppStateChangeTrapEnable": hpnicfPosaAppStateChangeTrapEnable,
       "hpnicfPosaTerminalHangUpTrapEnable": hpnicfPosaTerminalHangUpTrapEnable,
       "hpnicfPosaFcmLnkNegoFailTrapEnable": hpnicfPosaFcmLnkNegoFailTrapEnable,
       "hpnicfPosaFcmPhyNegoFailTrapEnable": hpnicfPosaFcmPhyNegoFailTrapEnable,
       "hpnicfPosaTcpConnectionNumber": hpnicfPosaTcpConnectionNumber,
       "hpnicfPosaFcmConnectionNumber": hpnicfPosaFcmConnectionNumber,
       "hpnicfPosaTcpConnectionThreshold": hpnicfPosaTcpConnectionThreshold,
       "hpnicfPosaFcmConnectionThreshold": hpnicfPosaFcmConnectionThreshold,
       "hpnicfPosaTcpConnectionTrapEnable": hpnicfPosaTcpConnectionTrapEnable,
       "hpnicfPosaFcmConnectionTrapEnable": hpnicfPosaFcmConnectionTrapEnable,
       "hpnicfPosaTcpTradeLimit": hpnicfPosaTcpTradeLimit,
       "hpnicfPosaTcpTradeTrapEnable": hpnicfPosaTcpTradeTrapEnable,
       "hpnicfPosaTcpTradeTimeout": hpnicfPosaTcpTradeTimeout,
       "hpnicfPosaTables": hpnicfPosaTables,
       "hpnicfPosaAppTable": hpnicfPosaAppTable,
       "hpnicfPosaAppEntry": hpnicfPosaAppEntry,
       "hpnicfPosaAppID": hpnicfPosaAppID,
       "hpnicfPosaAppServiceType": hpnicfPosaAppServiceType,
       "hpnicfPosaAppIfIndex": hpnicfPosaAppIfIndex,
       "hpnicfPosaAppMode": hpnicfPosaAppMode,
       "hpnicfPosaAppHostIPType": hpnicfPosaAppHostIPType,
       "hpnicfPosaAppHostIP": hpnicfPosaAppHostIP,
       "hpnicfPosaAppHostPort": hpnicfPosaAppHostPort,
       "hpnicfPosaAppRouterIPType": hpnicfPosaAppRouterIPType,
       "hpnicfPosaAppRouterIP": hpnicfPosaAppRouterIP,
       "hpnicfPosaAppKeepAliveInterval": hpnicfPosaAppKeepAliveInterval,
       "hpnicfPosaAppKeepAliveCount": hpnicfPosaAppKeepAliveCount,
       "hpnicfPosaAppConnectTimeout": hpnicfPosaAppConnectTimeout,
       "hpnicfPosaAppState": hpnicfPosaAppState,
       "hpnicfPosaAppRowStatus": hpnicfPosaAppRowStatus,
       "hpnicfPosaAppName": hpnicfPosaAppName,
       "hpnicfPosaCallerIDTransEnable": hpnicfPosaCallerIDTransEnable,
       "hpnicfPosaTpduChangeStrategy": hpnicfPosaTpduChangeStrategy,
       "hpnicfPosaBackupAppID": hpnicfPosaBackupAppID,
       "hpnicfPosaQuietTimeOut": hpnicfPosaQuietTimeOut,
       "hpnicfPosaAppHello": hpnicfPosaAppHello,
       "hpnicfPosaAppHelloInterval": hpnicfPosaAppHelloInterval,
       "hpnicfPosaAppRouterPort": hpnicfPosaAppRouterPort,
       "hpnicfPosaTerminalTable": hpnicfPosaTerminalTable,
       "hpnicfPosaTerminalEntry": hpnicfPosaTerminalEntry,
       "hpnicfPosaTerminalID": hpnicfPosaTerminalID,
       "hpnicfPosaTerminalAccessType": hpnicfPosaTerminalAccessType,
       "hpnicfPosaTerminalIfIndex": hpnicfPosaTerminalIfIndex,
       "hpnicfPosaTerminalTransAppID": hpnicfPosaTerminalTransAppID,
       "hpnicfPosaTerminalListenPort": hpnicfPosaTerminalListenPort,
       "hpnicfPosaTerminalState": hpnicfPosaTerminalState,
       "hpnicfPosaTerminalRowStatus": hpnicfPosaTerminalRowStatus,
       "hpnicfPosaTerminalName": hpnicfPosaTerminalName,
       "hpnicfPosaTerminalCfgIfIndex": hpnicfPosaTerminalCfgIfIndex,
       "hpnicfPosaMapTable": hpnicfPosaMapTable,
       "hpnicfPosaMapEntry": hpnicfPosaMapEntry,
       "hpnicfPosaMapDestCode": hpnicfPosaMapDestCode,
       "hpnicfPosaMapAppID": hpnicfPosaMapAppID,
       "hpnicfPosaMapRowStatus": hpnicfPosaMapRowStatus,
       "hpnicfPosaMapSrcCode": hpnicfPosaMapSrcCode,
       "hpnicfPosaFcmStatTable": hpnicfPosaFcmStatTable,
       "hpnicfPosaFcmStatEntry": hpnicfPosaFcmStatEntry,
       "hpnicfPosaFcmStatIfIndex": hpnicfPosaFcmStatIfIndex,
       "hpnicfPosaFcmStatTimeoutCnts": hpnicfPosaFcmStatTimeoutCnts,
       "hpnicfPosaFcmStatConnectFailCnts": hpnicfPosaFcmStatConnectFailCnts,
       "hpnicfPosaFcmStatTransCnts": hpnicfPosaFcmStatTransCnts,
       "hpnicfPosaFcmStatTransSuccessCnts": hpnicfPosaFcmStatTransSuccessCnts,
       "hpnicfPosaFcmStatTransCntsClear": hpnicfPosaFcmStatTransCntsClear,
       "hpnicfPosaAppStatTable": hpnicfPosaAppStatTable,
       "hpnicfPosaAppStatEntry": hpnicfPosaAppStatEntry,
       "hpnicfPosaAppRecvPkts": hpnicfPosaAppRecvPkts,
       "hpnicfPosaAppSendPkts": hpnicfPosaAppSendPkts,
       "hpnicfPosaAppErrPkts": hpnicfPosaAppErrPkts,
       "hpnicfPosaAppDistributeErrCnts": hpnicfPosaAppDistributeErrCnts,
       "hpnicfPosaAppInDiscardedPkts": hpnicfPosaAppInDiscardedPkts,
       "hpnicfPosaAppOutDiscardedPkts": hpnicfPosaAppOutDiscardedPkts,
       "hpnicfPosaTerminalStatTable": hpnicfPosaTerminalStatTable,
       "hpnicfPosaTerminalStatEntry": hpnicfPosaTerminalStatEntry,
       "hpnicfPosaTerminalRecvPkts": hpnicfPosaTerminalRecvPkts,
       "hpnicfPosaTerminalSendPkts": hpnicfPosaTerminalSendPkts,
       "hpnicfPosaTerminalErrPkts": hpnicfPosaTerminalErrPkts,
       "hpnicfPosaTerminalMapErrCnts": hpnicfPosaTerminalMapErrCnts,
       "hpnicfPosaTerminalInDiscardedPkts": hpnicfPosaTerminalInDiscardedPkts,
       "hpnicfPosaTerminalOutDiscardedPkts": hpnicfPosaTerminalOutDiscardedPkts,
       "hpnicfPosaBatchTerminalTable": hpnicfPosaBatchTerminalTable,
       "hpnicfPosaBatchTerminalEntry": hpnicfPosaBatchTerminalEntry,
       "hpnicfPosaBatchTerminalFirstID": hpnicfPosaBatchTerminalFirstID,
       "hpnicfPosaBatchTerminalRowStatus": hpnicfPosaBatchTerminalRowStatus,
       "hpnicfPosaTcpTermStatTable": hpnicfPosaTcpTermStatTable,
       "hpnicfPosaTcpTermStatEntry": hpnicfPosaTcpTermStatEntry,
       "hpnicfPosaTcpTermStatIndex": hpnicfPosaTcpTermStatIndex,
       "hpnicfPosaTcpTermStatIPType": hpnicfPosaTcpTermStatIPType,
       "hpnicfPosaTcpTermStatIP": hpnicfPosaTcpTermStatIP,
       "hpnicfPosaTcpTermStatIPMask": hpnicfPosaTcpTermStatIPMask,
       "hpnicfPosaTcpTermRecvPkts": hpnicfPosaTcpTermRecvPkts,
       "hpnicfPosaTcpTermSendPkts": hpnicfPosaTcpTermSendPkts,
       "hpnicfPosaTcpTermErrPkts": hpnicfPosaTcpTermErrPkts,
       "hpnicfPosaTcpTermMapErrCnts": hpnicfPosaTcpTermMapErrCnts,
       "hpnicfPosaTcpTermInDiscardedPkts": hpnicfPosaTcpTermInDiscardedPkts,
       "hpnicfPosaTcpTermOutDiscardedPkts": hpnicfPosaTcpTermOutDiscardedPkts,
       "hpnicfPosaTcpTermStatRowStatus": hpnicfPosaTcpTermStatRowStatus,
       "hpnicfPosaFcmConfTable": hpnicfPosaFcmConfTable,
       "hpnicfPosaFcmConfEntry": hpnicfPosaFcmConfEntry,
       "hpnicfPosaFcmNegoHookOff": hpnicfPosaFcmNegoHookOff,
       "hpnicfPosaFcmNegoSilence": hpnicfPosaFcmNegoSilence,
       "hpnicfPosaFcmNegoScrmbBinary1": hpnicfPosaFcmNegoScrmbBinary1,
       "hpnicfPosaFcmNegoUnscrmbBinary1": hpnicfPosaFcmNegoUnscrmbBinary1,
       "hpnicfPosaFcmThresholdRlsdOff": hpnicfPosaFcmThresholdRlsdOff,
       "hpnicfPosaFcmThresholdRlsdOn": hpnicfPosaFcmThresholdRlsdOn,
       "hpnicfPosaFcmThresholdTxPower": hpnicfPosaFcmThresholdTxPower,
       "hpnicfPosaFcmThresholdAnswerTone": hpnicfPosaFcmThresholdAnswerTone,
       "hpnicfPosaCallerStatTable": hpnicfPosaCallerStatTable,
       "hpnicfPosaCallerStatEntry": hpnicfPosaCallerStatEntry,
       "hpnicfPosaCallerStatCallerID": hpnicfPosaCallerStatCallerID,
       "hpnicfPosaCallerRecvPkts": hpnicfPosaCallerRecvPkts,
       "hpnicfPosaCallerSendPkts": hpnicfPosaCallerSendPkts,
       "hpnicfPosaCallerErrPkts": hpnicfPosaCallerErrPkts,
       "hpnicfPosaCallerMapErrCnts": hpnicfPosaCallerMapErrCnts,
       "hpnicfPosaCallerInDiscardedPkts": hpnicfPosaCallerInDiscardedPkts,
       "hpnicfPosaCallerOutDiscardedPkts": hpnicfPosaCallerOutDiscardedPkts,
       "hpnicfPosaCallerStatRowStatus": hpnicfPosaCallerStatRowStatus,
       "hpnicfPosaTrap": hpnicfPosaTrap,
       "hpnicfPosaTrapPrex": hpnicfPosaTrapPrex,
       "hpnicfPosaServerStatusChange": hpnicfPosaServerStatusChange,
       "hpnicfPosaAppStateChange": hpnicfPosaAppStateChange,
       "hpnicfPosaTerminalHangUp": hpnicfPosaTerminalHangUp,
       "hpnicfPosaFcmLinkNegoFailed": hpnicfPosaFcmLinkNegoFailed,
       "hpnicfPosaFcmPhyNegoFailed": hpnicfPosaFcmPhyNegoFailed,
       "hpnicfPosaTcpConnectionExceed": hpnicfPosaTcpConnectionExceed,
       "hpnicfPosaFcmConnectionExceed": hpnicfPosaFcmConnectionExceed,
       "hpnicfPosaTcpTradeExceed": hpnicfPosaTcpTradeExceed,
       "hpnicfPosaTrapObjects": hpnicfPosaTrapObjects,
       "hpnicfPosaAppStateChangeObject": hpnicfPosaAppStateChangeObject}
)
