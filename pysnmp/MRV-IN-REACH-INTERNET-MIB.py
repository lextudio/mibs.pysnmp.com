# SNMP MIB module (MRV-IN-REACH-INTERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-INTERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAdEntAddr,
 ipNetToMediaNetAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr",
    "ipNetToMediaNetAddress")

(AddressType,
 DateTime,
 TypedAddress,
 mrvInReachProductDivision) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "AddressType",
    "DateTime",
    "TypedAddress",
    "mrvInReachProductDivision")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XInternetDep_ObjectIdentity = ObjectIdentity
xInternetDep = _XInternetDep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 4)
)
_XInternet_ObjectIdentity = ObjectIdentity
xInternet = _XInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10)
)
_XIp_ObjectIdentity = ObjectIdentity
xIp = _XIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 1)
)
_IpGatewayAddress1_Type = IpAddress
_IpGatewayAddress1_Object = MibScalar
ipGatewayAddress1 = _IpGatewayAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 1),
    _IpGatewayAddress1_Type()
)
ipGatewayAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress1.setStatus("mandatory")
_IpGatewayAddress2_Type = IpAddress
_IpGatewayAddress2_Object = MibScalar
ipGatewayAddress2 = _IpGatewayAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 2),
    _IpGatewayAddress2_Type()
)
ipGatewayAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress2.setStatus("mandatory")


class _IpAutoSubnetMask_Type(Integer32):
    """Custom type ipAutoSubnetMask based on Integer32"""
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


_IpAutoSubnetMask_Type.__name__ = "Integer32"
_IpAutoSubnetMask_Object = MibScalar
ipAutoSubnetMask = _IpAutoSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 3),
    _IpAutoSubnetMask_Type()
)
ipAutoSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAutoSubnetMask.setStatus("deprecated")


class _IpReassembly_Type(Integer32):
    """Custom type ipReassembly based on Integer32"""
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


_IpReassembly_Type.__name__ = "Integer32"
_IpReassembly_Object = MibScalar
ipReassembly = _IpReassembly_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 4),
    _IpReassembly_Type()
)
ipReassembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipReassembly.setStatus("mandatory")
_IpFragmentsQueuedHigh_Type = Gauge32
_IpFragmentsQueuedHigh_Object = MibScalar
ipFragmentsQueuedHigh = _IpFragmentsQueuedHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 5),
    _IpFragmentsQueuedHigh_Type()
)
ipFragmentsQueuedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentsQueuedHigh.setStatus("mandatory")
_IpFragmentsQueuedCurrent_Type = Gauge32
_IpFragmentsQueuedCurrent_Object = MibScalar
ipFragmentsQueuedCurrent = _IpFragmentsQueuedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 6),
    _IpFragmentsQueuedCurrent_Type()
)
ipFragmentsQueuedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragmentsQueuedCurrent.setStatus("mandatory")
_IpGenAdExtTable_Object = MibTable
ipGenAdExtTable = _IpGenAdExtTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 7)
)
if mibBuilder.loadTexts:
    ipGenAdExtTable.setStatus("mandatory")
_IpGenAdExtEntry_Object = MibTableRow
ipGenAdExtEntry = _IpGenAdExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 7, 1)
)
ipGenAdExtEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    ipGenAdExtEntry.setStatus("mandatory")


class _IpGenAdEntExtType_Type(Integer32):
    """Custom type ipGenAdEntExtType based on Integer32"""
    defaultValue = 1

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
        *(("ppp", 4),
          ("primary", 1),
          ("rotary", 2),
          ("slip", 3))
    )


_IpGenAdEntExtType_Type.__name__ = "Integer32"
_IpGenAdEntExtType_Object = MibTableColumn
ipGenAdEntExtType = _IpGenAdEntExtType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 7, 1, 1),
    _IpGenAdEntExtType_Type()
)
ipGenAdEntExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGenAdEntExtType.setStatus("mandatory")


class _IpGenAdEntExtBroadcast_Type(IpAddress):
    """Custom type ipGenAdEntExtBroadcast based on IpAddress"""
    defaultHexValue = "ffffffff"


_IpGenAdEntExtBroadcast_Object = MibTableColumn
ipGenAdEntExtBroadcast = _IpGenAdEntExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 7, 1, 2),
    _IpGenAdEntExtBroadcast_Type()
)
ipGenAdEntExtBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGenAdEntExtBroadcast.setStatus("mandatory")


class _IpARPTimeout_Type(Integer32):
    """Custom type ipARPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpARPTimeout_Type.__name__ = "Integer32"
_IpARPTimeout_Object = MibScalar
ipARPTimeout = _IpARPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 8),
    _IpARPTimeout_Type()
)
ipARPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipARPTimeout.setStatus("mandatory")


class _IpGatewayPingInterval_Type(Integer32):
    """Custom type ipGatewayPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_IpGatewayPingInterval_Type.__name__ = "Integer32"
_IpGatewayPingInterval_Object = MibScalar
ipGatewayPingInterval = _IpGatewayPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 9),
    _IpGatewayPingInterval_Type()
)
ipGatewayPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayPingInterval.setStatus("mandatory")


class _IpConfigureBootp_Type(Integer32):
    """Custom type ipConfigureBootp based on Integer32"""
    defaultValue = 2

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


_IpConfigureBootp_Type.__name__ = "Integer32"
_IpConfigureBootp_Object = MibScalar
ipConfigureBootp = _IpConfigureBootp_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 11),
    _IpConfigureBootp_Type()
)
ipConfigureBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigureBootp.setStatus("mandatory")
_XTcp_ObjectIdentity = ObjectIdentity
xTcp = _XTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 2)
)
_TcpPortTable_Object = MibTable
tcpPortTable = _TcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1)
)
if mibBuilder.loadTexts:
    tcpPortTable.setStatus("mandatory")
_TcpPortEntry_Object = MibTableRow
tcpPortEntry = _TcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1)
)
tcpPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tcpPortIndex"),
)
if mibBuilder.loadTexts:
    tcpPortEntry.setStatus("mandatory")
_TcpPortIndex_Type = Integer32
_TcpPortIndex_Object = MibTableColumn
tcpPortIndex = _TcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 1),
    _TcpPortIndex_Type()
)
tcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpPortIndex.setStatus("mandatory")


class _TcpPortConnectByAddress_Type(Integer32):
    """Custom type tcpPortConnectByAddress based on Integer32"""
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


_TcpPortConnectByAddress_Type.__name__ = "Integer32"
_TcpPortConnectByAddress_Object = MibTableColumn
tcpPortConnectByAddress = _TcpPortConnectByAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 2),
    _TcpPortConnectByAddress_Type()
)
tcpPortConnectByAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortConnectByAddress.setStatus("mandatory")


class _TcpPortWindowSize_Type(Integer32):
    """Custom type tcpPortWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 8192),
    )


_TcpPortWindowSize_Type.__name__ = "Integer32"
_TcpPortWindowSize_Object = MibTableColumn
tcpPortWindowSize = _TcpPortWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 3),
    _TcpPortWindowSize_Type()
)
tcpPortWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortWindowSize.setStatus("mandatory")


class _TcpPortKeepAliveLimit_Type(Integer32):
    """Custom type tcpPortKeepAliveLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TcpPortKeepAliveLimit_Type.__name__ = "Integer32"
_TcpPortKeepAliveLimit_Object = MibTableColumn
tcpPortKeepAliveLimit = _TcpPortKeepAliveLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 4),
    _TcpPortKeepAliveLimit_Type()
)
tcpPortKeepAliveLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortKeepAliveLimit.setStatus("mandatory")


class _TcpResequencing_Type(Integer32):
    """Custom type tcpResequencing based on Integer32"""
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


_TcpResequencing_Type.__name__ = "Integer32"
_TcpResequencing_Object = MibScalar
tcpResequencing = _TcpResequencing_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 2),
    _TcpResequencing_Type()
)
tcpResequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpResequencing.setStatus("mandatory")
_TcpQueuedSegs_Type = Gauge32
_TcpQueuedSegs_Object = MibScalar
tcpQueuedSegs = _TcpQueuedSegs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 3),
    _TcpQueuedSegs_Type()
)
tcpQueuedSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpQueuedSegs.setStatus("mandatory")
_TcpDiscardSegs_Type = Counter32
_TcpDiscardSegs_Object = MibScalar
tcpDiscardSegs = _TcpDiscardSegs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 4),
    _TcpDiscardSegs_Type()
)
tcpDiscardSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpDiscardSegs.setStatus("mandatory")


class _TcpConnectTimer_Type(Integer32):
    """Custom type tcpConnectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_TcpConnectTimer_Type.__name__ = "Integer32"
_TcpConnectTimer_Object = MibScalar
tcpConnectTimer = _TcpConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 5),
    _TcpConnectTimer_Type()
)
tcpConnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpConnectTimer.setStatus("mandatory")


class _TcpLocalPortBase_Type(Integer32):
    """Custom type tcpLocalPortBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TcpLocalPortBase_Type.__name__ = "Integer32"
_TcpLocalPortBase_Object = MibScalar
tcpLocalPortBase = _TcpLocalPortBase_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 6),
    _TcpLocalPortBase_Type()
)
tcpLocalPortBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpLocalPortBase.setStatus("mandatory")


class _TcpLocalPortIncrement_Type(Integer32):
    """Custom type tcpLocalPortIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TcpLocalPortIncrement_Type.__name__ = "Integer32"
_TcpLocalPortIncrement_Object = MibScalar
tcpLocalPortIncrement = _TcpLocalPortIncrement_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 7),
    _TcpLocalPortIncrement_Type()
)
tcpLocalPortIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpLocalPortIncrement.setStatus("mandatory")


class _TcpRoutingTblSz_Type(Integer32):
    """Custom type tcpRoutingTblSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 512),
    )


_TcpRoutingTblSz_Type.__name__ = "Integer32"
_TcpRoutingTblSz_Object = MibScalar
tcpRoutingTblSz = _TcpRoutingTblSz_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 8),
    _TcpRoutingTblSz_Type()
)
tcpRoutingTblSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRoutingTblSz.setStatus("mandatory")


class _TcpDataSendDelay_Type(Integer32):
    """Custom type tcpDataSendDelay based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_TcpDataSendDelay_Type.__name__ = "Integer32"
_TcpDataSendDelay_Object = MibScalar
tcpDataSendDelay = _TcpDataSendDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 9),
    _TcpDataSendDelay_Type()
)
tcpDataSendDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpDataSendDelay.setStatus("mandatory")


class _TcpAckDelay_Type(Integer32):
    """Custom type tcpAckDelay based on Integer32"""
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


_TcpAckDelay_Type.__name__ = "Integer32"
_TcpAckDelay_Object = MibScalar
tcpAckDelay = _TcpAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 10),
    _TcpAckDelay_Type()
)
tcpAckDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpAckDelay.setStatus("mandatory")


class _TcpRetransmitMin_Type(Integer32):
    """Custom type tcpRetransmitMin based on Integer32"""
    defaultValue = 640

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_TcpRetransmitMin_Type.__name__ = "Integer32"
_TcpRetransmitMin_Object = MibScalar
tcpRetransmitMin = _TcpRetransmitMin_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 11),
    _TcpRetransmitMin_Type()
)
tcpRetransmitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpRetransmitMin.setStatus("mandatory")
_XSnmpAgent_ObjectIdentity = ObjectIdentity
xSnmpAgent = _XSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 3)
)


class _SnmpAgentGetCommunity_Type(DisplayString):
    """Custom type snmpAgentGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentGetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentGetCommunity_Object = MibScalar
snmpAgentGetCommunity = _SnmpAgentGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 1),
    _SnmpAgentGetCommunity_Type()
)
snmpAgentGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentGetCommunity.setStatus("mandatory")


class _SnmpAgentSetCommunity_Type(DisplayString):
    """Custom type snmpAgentSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentSetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentSetCommunity_Object = MibScalar
snmpAgentSetCommunity = _SnmpAgentSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 2),
    _SnmpAgentSetCommunity_Type()
)
snmpAgentSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentSetCommunity.setStatus("mandatory")


class _SnmpAgentTrapCommunity_Type(DisplayString):
    """Custom type snmpAgentTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentTrapCommunity_Type.__name__ = "DisplayString"
_SnmpAgentTrapCommunity_Object = MibScalar
snmpAgentTrapCommunity = _SnmpAgentTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 3),
    _SnmpAgentTrapCommunity_Type()
)
snmpAgentTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentTrapCommunity.setStatus("mandatory")
_SnmpAgentGetClientNumber_Type = Integer32
_SnmpAgentGetClientNumber_Object = MibScalar
snmpAgentGetClientNumber = _SnmpAgentGetClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 4),
    _SnmpAgentGetClientNumber_Type()
)
snmpAgentGetClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentGetClientNumber.setStatus("mandatory")
_SnmpAgentSetClientNumber_Type = Integer32
_SnmpAgentSetClientNumber_Object = MibScalar
snmpAgentSetClientNumber = _SnmpAgentSetClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 5),
    _SnmpAgentSetClientNumber_Type()
)
snmpAgentSetClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentSetClientNumber.setStatus("mandatory")
_SnmpAgentTrapClientNumber_Type = Integer32
_SnmpAgentTrapClientNumber_Object = MibScalar
snmpAgentTrapClientNumber = _SnmpAgentTrapClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 6),
    _SnmpAgentTrapClientNumber_Type()
)
snmpAgentTrapClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientNumber.setStatus("mandatory")
_GetClientTable_Object = MibTable
getClientTable = _GetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7)
)
if mibBuilder.loadTexts:
    getClientTable.setStatus("mandatory")
_GetClientEntry_Object = MibTableRow
getClientEntry = _GetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1)
)
getClientEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "getClientIndex"),
)
if mibBuilder.loadTexts:
    getClientEntry.setStatus("mandatory")
_GetClientIndex_Type = Integer32
_GetClientIndex_Object = MibTableColumn
getClientIndex = _GetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 1),
    _GetClientIndex_Type()
)
getClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getClientIndex.setStatus("mandatory")


class _GetClientEntryStatus_Type(Integer32):
    """Custom type getClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_GetClientEntryStatus_Type.__name__ = "Integer32"
_GetClientEntryStatus_Object = MibTableColumn
getClientEntryStatus = _GetClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 2),
    _GetClientEntryStatus_Type()
)
getClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientEntryStatus.setStatus("mandatory")


class _GetClientAddressType_Type(AddressType):
    """Custom type getClientAddressType based on AddressType"""


_GetClientAddressType_Object = MibTableColumn
getClientAddressType = _GetClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 3),
    _GetClientAddressType_Type()
)
getClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientAddressType.setStatus("mandatory")
_GetClientAddress_Type = OctetString
_GetClientAddress_Object = MibTableColumn
getClientAddress = _GetClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 4),
    _GetClientAddress_Type()
)
getClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientAddress.setStatus("mandatory")
_SetClientTable_Object = MibTable
setClientTable = _SetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8)
)
if mibBuilder.loadTexts:
    setClientTable.setStatus("mandatory")
_SetClientEntry_Object = MibTableRow
setClientEntry = _SetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1)
)
setClientEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "setClientIndex"),
)
if mibBuilder.loadTexts:
    setClientEntry.setStatus("mandatory")
_SetClientIndex_Type = Integer32
_SetClientIndex_Object = MibTableColumn
setClientIndex = _SetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 1),
    _SetClientIndex_Type()
)
setClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setClientIndex.setStatus("mandatory")


class _SetClientEntryStatus_Type(Integer32):
    """Custom type setClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_SetClientEntryStatus_Type.__name__ = "Integer32"
_SetClientEntryStatus_Object = MibTableColumn
setClientEntryStatus = _SetClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 2),
    _SetClientEntryStatus_Type()
)
setClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientEntryStatus.setStatus("mandatory")


class _SetClientAddressType_Type(AddressType):
    """Custom type setClientAddressType based on AddressType"""


_SetClientAddressType_Object = MibTableColumn
setClientAddressType = _SetClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 3),
    _SetClientAddressType_Type()
)
setClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientAddressType.setStatus("mandatory")
_SetClientAddress_Type = OctetString
_SetClientAddress_Object = MibTableColumn
setClientAddress = _SetClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 4),
    _SetClientAddress_Type()
)
setClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientAddress.setStatus("mandatory")
_TrapClientTable_Object = MibTable
trapClientTable = _TrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9)
)
if mibBuilder.loadTexts:
    trapClientTable.setStatus("mandatory")
_TrapClientEntry_Object = MibTableRow
trapClientEntry = _TrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1)
)
trapClientEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "trapClientIndex"),
)
if mibBuilder.loadTexts:
    trapClientEntry.setStatus("mandatory")
_TrapClientIndex_Type = Integer32
_TrapClientIndex_Object = MibTableColumn
trapClientIndex = _TrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 1),
    _TrapClientIndex_Type()
)
trapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientIndex.setStatus("mandatory")


class _TrapClientEntryStatus_Type(Integer32):
    """Custom type trapClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_TrapClientEntryStatus_Type.__name__ = "Integer32"
_TrapClientEntryStatus_Object = MibTableColumn
trapClientEntryStatus = _TrapClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 2),
    _TrapClientEntryStatus_Type()
)
trapClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientEntryStatus.setStatus("mandatory")


class _TrapClientAddressType_Type(AddressType):
    """Custom type trapClientAddressType based on AddressType"""


_TrapClientAddressType_Object = MibTableColumn
trapClientAddressType = _TrapClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 3),
    _TrapClientAddressType_Type()
)
trapClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientAddressType.setStatus("mandatory")
_TrapClientAddress_Type = OctetString
_TrapClientAddress_Object = MibTableColumn
trapClientAddress = _TrapClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 4),
    _TrapClientAddress_Type()
)
trapClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientAddress.setStatus("mandatory")
_SnmpAgentAuthFailureAddress_Type = TypedAddress
_SnmpAgentAuthFailureAddress_Object = MibScalar
snmpAgentAuthFailureAddress = _SnmpAgentAuthFailureAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 10),
    _SnmpAgentAuthFailureAddress_Type()
)
snmpAgentAuthFailureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentAuthFailureAddress.setStatus("mandatory")


class _SnmpAgentCommunityAuthenticationAlways_Type(Integer32):
    """Custom type snmpAgentCommunityAuthenticationAlways based on Integer32"""
    defaultValue = 2

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


_SnmpAgentCommunityAuthenticationAlways_Type.__name__ = "Integer32"
_SnmpAgentCommunityAuthenticationAlways_Object = MibScalar
snmpAgentCommunityAuthenticationAlways = _SnmpAgentCommunityAuthenticationAlways_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 14),
    _SnmpAgentCommunityAuthenticationAlways_Type()
)
snmpAgentCommunityAuthenticationAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentCommunityAuthenticationAlways.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost1_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost1 based on Integer32"""
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


_SnmpAgentTrapClientPingHost1_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost1_Object = MibScalar
snmpAgentTrapClientPingHost1 = _SnmpAgentTrapClientPingHost1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 15),
    _SnmpAgentTrapClientPingHost1_Type()
)
snmpAgentTrapClientPingHost1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost1.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost2_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost2 based on Integer32"""
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


_SnmpAgentTrapClientPingHost2_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost2_Object = MibScalar
snmpAgentTrapClientPingHost2 = _SnmpAgentTrapClientPingHost2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 16),
    _SnmpAgentTrapClientPingHost2_Type()
)
snmpAgentTrapClientPingHost2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost2.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost1PollInterval_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost1PollInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAgentTrapClientPingHost1PollInterval_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost1PollInterval_Object = MibScalar
snmpAgentTrapClientPingHost1PollInterval = _SnmpAgentTrapClientPingHost1PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 17),
    _SnmpAgentTrapClientPingHost1PollInterval_Type()
)
snmpAgentTrapClientPingHost1PollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost1PollInterval.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost2PollInterval_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost2PollInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAgentTrapClientPingHost2PollInterval_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost2PollInterval_Object = MibScalar
snmpAgentTrapClientPingHost2PollInterval = _SnmpAgentTrapClientPingHost2PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 18),
    _SnmpAgentTrapClientPingHost2PollInterval_Type()
)
snmpAgentTrapClientPingHost2PollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost2PollInterval.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost1PollRetries_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost1PollRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnmpAgentTrapClientPingHost1PollRetries_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost1PollRetries_Object = MibScalar
snmpAgentTrapClientPingHost1PollRetries = _SnmpAgentTrapClientPingHost1PollRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 19),
    _SnmpAgentTrapClientPingHost1PollRetries_Type()
)
snmpAgentTrapClientPingHost1PollRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost1PollRetries.setStatus("mandatory")


class _SnmpAgentTrapClientPingHost2PollRetries_Type(Integer32):
    """Custom type snmpAgentTrapClientPingHost2PollRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnmpAgentTrapClientPingHost2PollRetries_Type.__name__ = "Integer32"
_SnmpAgentTrapClientPingHost2PollRetries_Object = MibScalar
snmpAgentTrapClientPingHost2PollRetries = _SnmpAgentTrapClientPingHost2PollRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 20),
    _SnmpAgentTrapClientPingHost2PollRetries_Type()
)
snmpAgentTrapClientPingHost2PollRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientPingHost2PollRetries.setStatus("mandatory")


class _SnmpAgentTrapClientQuerySourceHost1_Type(Integer32):
    """Custom type snmpAgentTrapClientQuerySourceHost1 based on Integer32"""
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


_SnmpAgentTrapClientQuerySourceHost1_Type.__name__ = "Integer32"
_SnmpAgentTrapClientQuerySourceHost1_Object = MibScalar
snmpAgentTrapClientQuerySourceHost1 = _SnmpAgentTrapClientQuerySourceHost1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 21),
    _SnmpAgentTrapClientQuerySourceHost1_Type()
)
snmpAgentTrapClientQuerySourceHost1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientQuerySourceHost1.setStatus("mandatory")


class _SnmpAgentTrapClientQuerySourceHost2_Type(Integer32):
    """Custom type snmpAgentTrapClientQuerySourceHost2 based on Integer32"""
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


_SnmpAgentTrapClientQuerySourceHost2_Type.__name__ = "Integer32"
_SnmpAgentTrapClientQuerySourceHost2_Object = MibScalar
snmpAgentTrapClientQuerySourceHost2 = _SnmpAgentTrapClientQuerySourceHost2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 22),
    _SnmpAgentTrapClientQuerySourceHost2_Type()
)
snmpAgentTrapClientQuerySourceHost2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientQuerySourceHost2.setStatus("mandatory")


class _SnmpAgentTrapClientQuerySourceHost1Timeout_Type(Integer32):
    """Custom type snmpAgentTrapClientQuerySourceHost1Timeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAgentTrapClientQuerySourceHost1Timeout_Type.__name__ = "Integer32"
_SnmpAgentTrapClientQuerySourceHost1Timeout_Object = MibScalar
snmpAgentTrapClientQuerySourceHost1Timeout = _SnmpAgentTrapClientQuerySourceHost1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 23),
    _SnmpAgentTrapClientQuerySourceHost1Timeout_Type()
)
snmpAgentTrapClientQuerySourceHost1Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientQuerySourceHost1Timeout.setStatus("mandatory")


class _SnmpAgentTrapClientQuerySourceHost2Timeout_Type(Integer32):
    """Custom type snmpAgentTrapClientQuerySourceHost2Timeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAgentTrapClientQuerySourceHost2Timeout_Type.__name__ = "Integer32"
_SnmpAgentTrapClientQuerySourceHost2Timeout_Object = MibScalar
snmpAgentTrapClientQuerySourceHost2Timeout = _SnmpAgentTrapClientQuerySourceHost2Timeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 24),
    _SnmpAgentTrapClientQuerySourceHost2Timeout_Type()
)
snmpAgentTrapClientQuerySourceHost2Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientQuerySourceHost2Timeout.setStatus("mandatory")
_XDomainResolver_ObjectIdentity = ObjectIdentity
xDomainResolver = _XDomainResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 4)
)


class _DomainResolverSuffix_Type(DisplayString):
    """Custom type domainResolverSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_DomainResolverSuffix_Type.__name__ = "DisplayString"
_DomainResolverSuffix_Object = MibScalar
domainResolverSuffix = _DomainResolverSuffix_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 1),
    _DomainResolverSuffix_Type()
)
domainResolverSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverSuffix.setStatus("mandatory")
_DomainResolverAddress1_Type = IpAddress
_DomainResolverAddress1_Object = MibScalar
domainResolverAddress1 = _DomainResolverAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 2),
    _DomainResolverAddress1_Type()
)
domainResolverAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverAddress1.setStatus("mandatory")
_DomainResolverAddress2_Type = IpAddress
_DomainResolverAddress2_Object = MibScalar
domainResolverAddress2 = _DomainResolverAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 3),
    _DomainResolverAddress2_Type()
)
domainResolverAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverAddress2.setStatus("mandatory")


class _DomainResolverTtl_Type(Integer32):
    """Custom type domainResolverTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_DomainResolverTtl_Type.__name__ = "Integer32"
_DomainResolverTtl_Object = MibScalar
domainResolverTtl = _DomainResolverTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 4),
    _DomainResolverTtl_Type()
)
domainResolverTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverTtl.setStatus("mandatory")
_DomainResolverNameNumber_Type = Integer32
_DomainResolverNameNumber_Object = MibScalar
domainResolverNameNumber = _DomainResolverNameNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 5),
    _DomainResolverNameNumber_Type()
)
domainResolverNameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainResolverNameNumber.setStatus("mandatory")
_NameTable_Object = MibTable
nameTable = _NameTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6)
)
if mibBuilder.loadTexts:
    nameTable.setStatus("mandatory")
_NameEntry_Object = MibTableRow
nameEntry = _NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1)
)
nameEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "nameName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "nameAddress"),
)
if mibBuilder.loadTexts:
    nameEntry.setStatus("mandatory")


class _NameName_Type(DisplayString):
    """Custom type nameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NameName_Type.__name__ = "DisplayString"
_NameName_Object = MibTableColumn
nameName = _NameName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 1),
    _NameName_Type()
)
nameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameName.setStatus("mandatory")
_NameAddress_Type = IpAddress
_NameAddress_Object = MibTableColumn
nameAddress = _NameAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 2),
    _NameAddress_Type()
)
nameAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameAddress.setStatus("mandatory")


class _NameStatus_Type(Integer32):
    """Custom type nameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NameStatus_Type.__name__ = "Integer32"
_NameStatus_Object = MibTableColumn
nameStatus = _NameStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 3),
    _NameStatus_Type()
)
nameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameStatus.setStatus("mandatory")


class _NameSource_Type(Integer32):
    """Custom type nameSource based on Integer32"""
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
        *(("manager", 1),
          ("primary", 2),
          ("rwho", 4),
          ("secondary", 3))
    )


_NameSource_Type.__name__ = "Integer32"
_NameSource_Object = MibTableColumn
nameSource = _NameSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 4),
    _NameSource_Type()
)
nameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameSource.setStatus("mandatory")
_NameTtl_Type = Integer32
_NameTtl_Object = MibTableColumn
nameTtl = _NameTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 5),
    _NameTtl_Type()
)
nameTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameTtl.setStatus("mandatory")
_DomainResolverPpp_ObjectIdentity = ObjectIdentity
domainResolverPpp = _DomainResolverPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 7)
)
_DomainResolverPppPrimaryServer_Type = IpAddress
_DomainResolverPppPrimaryServer_Object = MibScalar
domainResolverPppPrimaryServer = _DomainResolverPppPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 7, 1),
    _DomainResolverPppPrimaryServer_Type()
)
domainResolverPppPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverPppPrimaryServer.setStatus("mandatory")
_DomainResolverPppSecondaryServer_Type = IpAddress
_DomainResolverPppSecondaryServer_Object = MibScalar
domainResolverPppSecondaryServer = _DomainResolverPppSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 7, 2),
    _DomainResolverPppSecondaryServer_Type()
)
domainResolverPppSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverPppSecondaryServer.setStatus("mandatory")
_XSlip_ObjectIdentity = ObjectIdentity
xSlip = _XSlip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 5)
)
_SlipTable_Object = MibTable
slipTable = _SlipTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1)
)
if mibBuilder.loadTexts:
    slipTable.setStatus("mandatory")
_SlipEntry_Object = MibTableRow
slipEntry = _SlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1)
)
slipEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "slipIndex"),
)
if mibBuilder.loadTexts:
    slipEntry.setStatus("mandatory")
_SlipIndex_Type = Integer32
_SlipIndex_Object = MibTableColumn
slipIndex = _SlipIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 1),
    _SlipIndex_Type()
)
slipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipIndex.setStatus("mandatory")


class _SlipState_Type(Integer32):
    """Custom type slipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 3),
          ("off", 1),
          ("on", 2))
    )


_SlipState_Type.__name__ = "Integer32"
_SlipState_Object = MibTableColumn
slipState = _SlipState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 2),
    _SlipState_Type()
)
slipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipState.setStatus("mandatory")
_SlipLocalAddress_Type = IpAddress
_SlipLocalAddress_Object = MibTableColumn
slipLocalAddress = _SlipLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 3),
    _SlipLocalAddress_Type()
)
slipLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipLocalAddress.setStatus("mandatory")
_SlipRemoteAddress_Type = IpAddress
_SlipRemoteAddress_Object = MibTableColumn
slipRemoteAddress = _SlipRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 4),
    _SlipRemoteAddress_Type()
)
slipRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipRemoteAddress.setStatus("mandatory")
_SlipMask_Type = IpAddress
_SlipMask_Object = MibTableColumn
slipMask = _SlipMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 5),
    _SlipMask_Type()
)
slipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipMask.setStatus("mandatory")
_SlipPortPacketsReceived_Type = Counter32
_SlipPortPacketsReceived_Object = MibTableColumn
slipPortPacketsReceived = _SlipPortPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 6),
    _SlipPortPacketsReceived_Type()
)
slipPortPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsReceived.setStatus("mandatory")
_SlipPortPacketsSent_Type = Counter32
_SlipPortPacketsSent_Object = MibTableColumn
slipPortPacketsSent = _SlipPortPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 7),
    _SlipPortPacketsSent_Type()
)
slipPortPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsSent.setStatus("mandatory")
_SlipPortPacketsDiscarded_Type = Counter32
_SlipPortPacketsDiscarded_Object = MibTableColumn
slipPortPacketsDiscarded = _SlipPortPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 8),
    _SlipPortPacketsDiscarded_Type()
)
slipPortPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsDiscarded.setStatus("mandatory")
_SlipPortPacketLengthErrors_Type = Counter32
_SlipPortPacketLengthErrors_Object = MibTableColumn
slipPortPacketLengthErrors = _SlipPortPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 9),
    _SlipPortPacketLengthErrors_Type()
)
slipPortPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketLengthErrors.setStatus("mandatory")
_SlipPortPacketChecksumErrors_Type = Counter32
_SlipPortPacketChecksumErrors_Object = MibTableColumn
slipPortPacketChecksumErrors = _SlipPortPacketChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 10),
    _SlipPortPacketChecksumErrors_Type()
)
slipPortPacketChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketChecksumErrors.setStatus("mandatory")
_SlipNetworkPacketsReceived_Type = Counter32
_SlipNetworkPacketsReceived_Object = MibTableColumn
slipNetworkPacketsReceived = _SlipNetworkPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 11),
    _SlipNetworkPacketsReceived_Type()
)
slipNetworkPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsReceived.setStatus("mandatory")
_SlipNetworkPacketsSent_Type = Counter32
_SlipNetworkPacketsSent_Object = MibTableColumn
slipNetworkPacketsSent = _SlipNetworkPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 12),
    _SlipNetworkPacketsSent_Type()
)
slipNetworkPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsSent.setStatus("mandatory")
_SlipNetworkPacketsDiscarded_Type = Counter32
_SlipNetworkPacketsDiscarded_Object = MibTableColumn
slipNetworkPacketsDiscarded = _SlipNetworkPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 13),
    _SlipNetworkPacketsDiscarded_Type()
)
slipNetworkPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsDiscarded.setStatus("mandatory")
_XTelnet_ObjectIdentity = ObjectIdentity
xTelnet = _XTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 6)
)
_TelnetPortTable_Object = MibTable
telnetPortTable = _TelnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1)
)
if mibBuilder.loadTexts:
    telnetPortTable.setStatus("mandatory")
_TelnetPortEntry_Object = MibTableRow
telnetPortEntry = _TelnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1)
)
telnetPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "telnetPortIndex"),
)
if mibBuilder.loadTexts:
    telnetPortEntry.setStatus("mandatory")
_TelnetPortIndex_Type = Integer32
_TelnetPortIndex_Object = MibTableColumn
telnetPortIndex = _TelnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 1),
    _TelnetPortIndex_Type()
)
telnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortIndex.setStatus("mandatory")


class _TelnetPortIncomingTcpPort_Type(Integer32):
    """Custom type telnetPortIncomingTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TelnetPortIncomingTcpPort_Type.__name__ = "Integer32"
_TelnetPortIncomingTcpPort_Object = MibTableColumn
telnetPortIncomingTcpPort = _TelnetPortIncomingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 2),
    _TelnetPortIncomingTcpPort_Type()
)
telnetPortIncomingTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortIncomingTcpPort.setStatus("mandatory")
_TelnetPortOutgoingTcpPort_Type = Integer32
_TelnetPortOutgoingTcpPort_Object = MibTableColumn
telnetPortOutgoingTcpPort = _TelnetPortOutgoingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 3),
    _TelnetPortOutgoingTcpPort_Type()
)
telnetPortOutgoingTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortOutgoingTcpPort.setStatus("mandatory")


class _TelnetPortNewlineTranslation_Type(Integer32):
    """Custom type telnetPortNewlineTranslation based on Integer32"""
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
        *(("cr", 2),
          ("crLf", 4),
          ("crNull", 3),
          ("lfToCrLf", 6),
          ("none", 1),
          ("std", 5))
    )


_TelnetPortNewlineTranslation_Type.__name__ = "Integer32"
_TelnetPortNewlineTranslation_Object = MibTableColumn
telnetPortNewlineTranslation = _TelnetPortNewlineTranslation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 4),
    _TelnetPortNewlineTranslation_Type()
)
telnetPortNewlineTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNewlineTranslation.setStatus("mandatory")


class _TelnetPortTerminalType_Type(DisplayString):
    """Custom type telnetPortTerminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_TelnetPortTerminalType_Type.__name__ = "DisplayString"
_TelnetPortTerminalType_Object = MibTableColumn
telnetPortTerminalType = _TelnetPortTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 5),
    _TelnetPortTerminalType_Type()
)
telnetPortTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortTerminalType.setStatus("mandatory")


class _TelnetPortEorReflection_Type(Integer32):
    """Custom type telnetPortEorReflection based on Integer32"""
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


_TelnetPortEorReflection_Type.__name__ = "Integer32"
_TelnetPortEorReflection_Object = MibTableColumn
telnetPortEorReflection = _TelnetPortEorReflection_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 6),
    _TelnetPortEorReflection_Type()
)
telnetPortEorReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortEorReflection.setStatus("mandatory")


class _TelnetPortBinaryMode_Type(Integer32):
    """Custom type telnetPortBinaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("disabled", 3),
          ("flowControl", 1))
    )


_TelnetPortBinaryMode_Type.__name__ = "Integer32"
_TelnetPortBinaryMode_Object = MibTableColumn
telnetPortBinaryMode = _TelnetPortBinaryMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 7),
    _TelnetPortBinaryMode_Type()
)
telnetPortBinaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortBinaryMode.setStatus("mandatory")


class _TelnetPortSendLocation_Type(Integer32):
    """Custom type telnetPortSendLocation based on Integer32"""
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


_TelnetPortSendLocation_Type.__name__ = "Integer32"
_TelnetPortSendLocation_Object = MibTableColumn
telnetPortSendLocation = _TelnetPortSendLocation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 8),
    _TelnetPortSendLocation_Type()
)
telnetPortSendLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortSendLocation.setStatus("mandatory")


class _TelnetPortClientLocation_Type(DisplayString):
    """Custom type telnetPortClientLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TelnetPortClientLocation_Type.__name__ = "DisplayString"
_TelnetPortClientLocation_Object = MibTableColumn
telnetPortClientLocation = _TelnetPortClientLocation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 9),
    _TelnetPortClientLocation_Type()
)
telnetPortClientLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortClientLocation.setStatus("mandatory")


class _TelnetPortPassiveSendLocation_Type(Integer32):
    """Custom type telnetPortPassiveSendLocation based on Integer32"""
    defaultValue = 2

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


_TelnetPortPassiveSendLocation_Type.__name__ = "Integer32"
_TelnetPortPassiveSendLocation_Object = MibTableColumn
telnetPortPassiveSendLocation = _TelnetPortPassiveSendLocation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 10),
    _TelnetPortPassiveSendLocation_Type()
)
telnetPortPassiveSendLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortPassiveSendLocation.setStatus("mandatory")
_TelnetSerialPortTable_Object = MibTable
telnetSerialPortTable = _TelnetSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2)
)
if mibBuilder.loadTexts:
    telnetSerialPortTable.setStatus("mandatory")
_TelnetSerialPortEntry_Object = MibTableRow
telnetSerialPortEntry = _TelnetSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1)
)
telnetSerialPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "telnetSerialPortIndex"),
)
if mibBuilder.loadTexts:
    telnetSerialPortEntry.setStatus("mandatory")
_TelnetSerialPortIndex_Type = Integer32
_TelnetSerialPortIndex_Object = MibTableColumn
telnetSerialPortIndex = _TelnetSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 1),
    _TelnetSerialPortIndex_Type()
)
telnetSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSerialPortIndex.setStatus("mandatory")


class _TelnetSerialPortOptionDisplay_Type(Integer32):
    """Custom type telnetSerialPortOptionDisplay based on Integer32"""
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


_TelnetSerialPortOptionDisplay_Type.__name__ = "Integer32"
_TelnetSerialPortOptionDisplay_Object = MibTableColumn
telnetSerialPortOptionDisplay = _TelnetSerialPortOptionDisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 2),
    _TelnetSerialPortOptionDisplay_Type()
)
telnetSerialPortOptionDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortOptionDisplay.setStatus("mandatory")


class _TelnetSerialPortCsiEscape_Type(Integer32):
    """Custom type telnetSerialPortCsiEscape based on Integer32"""
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


_TelnetSerialPortCsiEscape_Type.__name__ = "Integer32"
_TelnetSerialPortCsiEscape_Object = MibTableColumn
telnetSerialPortCsiEscape = _TelnetSerialPortCsiEscape_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 3),
    _TelnetSerialPortCsiEscape_Type()
)
telnetSerialPortCsiEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortCsiEscape.setStatus("mandatory")


class _TelnetSerialPortEchoMode_Type(Integer32):
    """Custom type telnetSerialPortEchoMode based on Integer32"""
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
        *(("character", 5),
          ("disabled", 3),
          ("line", 6),
          ("local", 1),
          ("noecho", 7),
          ("passive", 4),
          ("remote", 2))
    )


_TelnetSerialPortEchoMode_Type.__name__ = "Integer32"
_TelnetSerialPortEchoMode_Object = MibTableColumn
telnetSerialPortEchoMode = _TelnetSerialPortEchoMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 4),
    _TelnetSerialPortEchoMode_Type()
)
telnetSerialPortEchoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEchoMode.setStatus("mandatory")


class _TelnetSerialPortNewlineMode_Type(Integer32):
    """Custom type telnetSerialPortNewlineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crLf", 2),
          ("crNull", 1),
          ("verbatim", 3))
    )


_TelnetSerialPortNewlineMode_Type.__name__ = "Integer32"
_TelnetSerialPortNewlineMode_Object = MibTableColumn
telnetSerialPortNewlineMode = _TelnetSerialPortNewlineMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 5),
    _TelnetSerialPortNewlineMode_Type()
)
telnetSerialPortNewlineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortNewlineMode.setStatus("mandatory")


class _TelnetSerialPortTransmitMode_Type(Integer32):
    """Custom type telnetSerialPortTransmitMode based on Integer32"""
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
        *(("buffered", 2),
          ("controlchar", 4),
          ("immediate", 1),
          ("timed", 3))
    )


_TelnetSerialPortTransmitMode_Type.__name__ = "Integer32"
_TelnetSerialPortTransmitMode_Object = MibTableColumn
telnetSerialPortTransmitMode = _TelnetSerialPortTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 6),
    _TelnetSerialPortTransmitMode_Type()
)
telnetSerialPortTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortTransmitMode.setStatus("mandatory")


class _TelnetSerialPortTransmitCharacterTimes_Type(Integer32):
    """Custom type telnetSerialPortTransmitCharacterTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortTransmitCharacterTimes_Type.__name__ = "Integer32"
_TelnetSerialPortTransmitCharacterTimes_Object = MibTableColumn
telnetSerialPortTransmitCharacterTimes = _TelnetSerialPortTransmitCharacterTimes_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 7),
    _TelnetSerialPortTransmitCharacterTimes_Type()
)
telnetSerialPortTransmitCharacterTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortTransmitCharacterTimes.setStatus("mandatory")


class _TelnetSerialPortAbortOutputCharacter_Type(Integer32):
    """Custom type telnetSerialPortAbortOutputCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortAbortOutputCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortAbortOutputCharacter_Object = MibTableColumn
telnetSerialPortAbortOutputCharacter = _TelnetSerialPortAbortOutputCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 8),
    _TelnetSerialPortAbortOutputCharacter_Type()
)
telnetSerialPortAbortOutputCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortAbortOutputCharacter.setStatus("mandatory")


class _TelnetSerialPortAttentionCharacter_Type(Integer32):
    """Custom type telnetSerialPortAttentionCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortAttentionCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortAttentionCharacter_Object = MibTableColumn
telnetSerialPortAttentionCharacter = _TelnetSerialPortAttentionCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 9),
    _TelnetSerialPortAttentionCharacter_Type()
)
telnetSerialPortAttentionCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortAttentionCharacter.setStatus("mandatory")


class _TelnetSerialPortEraseKeyCharacter_Type(Integer32):
    """Custom type telnetSerialPortEraseKeyCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortEraseKeyCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortEraseKeyCharacter_Object = MibTableColumn
telnetSerialPortEraseKeyCharacter = _TelnetSerialPortEraseKeyCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 10),
    _TelnetSerialPortEraseKeyCharacter_Type()
)
telnetSerialPortEraseKeyCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEraseKeyCharacter.setStatus("mandatory")


class _TelnetSerialPortEraseLineCharacter_Type(Integer32):
    """Custom type telnetSerialPortEraseLineCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortEraseLineCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortEraseLineCharacter_Object = MibTableColumn
telnetSerialPortEraseLineCharacter = _TelnetSerialPortEraseLineCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 11),
    _TelnetSerialPortEraseLineCharacter_Type()
)
telnetSerialPortEraseLineCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEraseLineCharacter.setStatus("mandatory")


class _TelnetSerialPortInterruptCharacter_Type(Integer32):
    """Custom type telnetSerialPortInterruptCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortInterruptCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortInterruptCharacter_Object = MibTableColumn
telnetSerialPortInterruptCharacter = _TelnetSerialPortInterruptCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 12),
    _TelnetSerialPortInterruptCharacter_Type()
)
telnetSerialPortInterruptCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortInterruptCharacter.setStatus("mandatory")


class _TelnetSerialPortQueryCharacter_Type(Integer32):
    """Custom type telnetSerialPortQueryCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortQueryCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortQueryCharacter_Object = MibTableColumn
telnetSerialPortQueryCharacter = _TelnetSerialPortQueryCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 13),
    _TelnetSerialPortQueryCharacter_Type()
)
telnetSerialPortQueryCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortQueryCharacter.setStatus("mandatory")


class _TelnetSerialPortSynchronizeCharacter_Type(Integer32):
    """Custom type telnetSerialPortSynchronizeCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortSynchronizeCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortSynchronizeCharacter_Object = MibTableColumn
telnetSerialPortSynchronizeCharacter = _TelnetSerialPortSynchronizeCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 14),
    _TelnetSerialPortSynchronizeCharacter_Type()
)
telnetSerialPortSynchronizeCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortSynchronizeCharacter.setStatus("mandatory")


class _TelnetSerialPortUrgentBreak_Type(Integer32):
    """Custom type telnetSerialPortUrgentBreak based on Integer32"""
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


_TelnetSerialPortUrgentBreak_Type.__name__ = "Integer32"
_TelnetSerialPortUrgentBreak_Object = MibTableColumn
telnetSerialPortUrgentBreak = _TelnetSerialPortUrgentBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 15),
    _TelnetSerialPortUrgentBreak_Type()
)
telnetSerialPortUrgentBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortUrgentBreak.setStatus("mandatory")


class _TelnetSerialPortRs491_Type(Integer32):
    """Custom type telnetSerialPortRs491 based on Integer32"""
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


_TelnetSerialPortRs491_Type.__name__ = "Integer32"
_TelnetSerialPortRs491_Object = MibTableColumn
telnetSerialPortRs491 = _TelnetSerialPortRs491_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 16),
    _TelnetSerialPortRs491_Type()
)
telnetSerialPortRs491.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortRs491.setStatus("mandatory")


class _TelnetSerialPortTransmitBufferedTime_Type(Integer32):
    """Custom type telnetSerialPortTransmitBufferedTime based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1500),
    )


_TelnetSerialPortTransmitBufferedTime_Type.__name__ = "Integer32"
_TelnetSerialPortTransmitBufferedTime_Object = MibTableColumn
telnetSerialPortTransmitBufferedTime = _TelnetSerialPortTransmitBufferedTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 17),
    _TelnetSerialPortTransmitBufferedTime_Type()
)
telnetSerialPortTransmitBufferedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortTransmitBufferedTime.setStatus("mandatory")


class _TelnetSerialPortInterpretInterruptAsBreak_Type(Integer32):
    """Custom type telnetSerialPortInterpretInterruptAsBreak based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortInterpretInterruptAsBreak_Type.__name__ = "Integer32"
_TelnetSerialPortInterpretInterruptAsBreak_Object = MibTableColumn
telnetSerialPortInterpretInterruptAsBreak = _TelnetSerialPortInterpretInterruptAsBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 18),
    _TelnetSerialPortInterpretInterruptAsBreak_Type()
)
telnetSerialPortInterpretInterruptAsBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortInterpretInterruptAsBreak.setStatus("mandatory")


class _TelnetSerialPortPass8d_Type(Integer32):
    """Custom type telnetSerialPortPass8d based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortPass8d_Type.__name__ = "Integer32"
_TelnetSerialPortPass8d_Object = MibTableColumn
telnetSerialPortPass8d = _TelnetSerialPortPass8d_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 19),
    _TelnetSerialPortPass8d_Type()
)
telnetSerialPortPass8d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortPass8d.setStatus("mandatory")


class _TelnetSerialPortComControlClient_Type(Integer32):
    """Custom type telnetSerialPortComControlClient based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortComControlClient_Type.__name__ = "Integer32"
_TelnetSerialPortComControlClient_Object = MibTableColumn
telnetSerialPortComControlClient = _TelnetSerialPortComControlClient_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 20),
    _TelnetSerialPortComControlClient_Type()
)
telnetSerialPortComControlClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortComControlClient.setStatus("mandatory")


class _TelnetSerialPortComControlServer_Type(Integer32):
    """Custom type telnetSerialPortComControlServer based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortComControlServer_Type.__name__ = "Integer32"
_TelnetSerialPortComControlServer_Object = MibTableColumn
telnetSerialPortComControlServer = _TelnetSerialPortComControlServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 21),
    _TelnetSerialPortComControlServer_Type()
)
telnetSerialPortComControlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortComControlServer.setStatus("mandatory")


class _TelnetSerialPortComControlServerRaisesDtr_Type(Integer32):
    """Custom type telnetSerialPortComControlServerRaisesDtr based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortComControlServerRaisesDtr_Type.__name__ = "Integer32"
_TelnetSerialPortComControlServerRaisesDtr_Object = MibTableColumn
telnetSerialPortComControlServerRaisesDtr = _TelnetSerialPortComControlServerRaisesDtr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 22),
    _TelnetSerialPortComControlServerRaisesDtr_Type()
)
telnetSerialPortComControlServerRaisesDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortComControlServerRaisesDtr.setStatus("mandatory")


class _TelnetSerialPortComControlClientTogglesDtr_Type(Integer32):
    """Custom type telnetSerialPortComControlClientTogglesDtr based on Integer32"""
    defaultValue = 2

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


_TelnetSerialPortComControlClientTogglesDtr_Type.__name__ = "Integer32"
_TelnetSerialPortComControlClientTogglesDtr_Object = MibTableColumn
telnetSerialPortComControlClientTogglesDtr = _TelnetSerialPortComControlClientTogglesDtr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 23),
    _TelnetSerialPortComControlClientTogglesDtr_Type()
)
telnetSerialPortComControlClientTogglesDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortComControlClientTogglesDtr.setStatus("mandatory")
_XTn3270_ObjectIdentity = ObjectIdentity
xTn3270 = _XTn3270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 7)
)
_Tn3270DeviceNumber_Type = Integer32
_Tn3270DeviceNumber_Object = MibScalar
tn3270DeviceNumber = _Tn3270DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 1),
    _Tn3270DeviceNumber_Type()
)
tn3270DeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceNumber.setStatus("mandatory")
_Tn3270LanguageNumber_Type = Integer32
_Tn3270LanguageNumber_Object = MibScalar
tn3270LanguageNumber = _Tn3270LanguageNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 2),
    _Tn3270LanguageNumber_Type()
)
tn3270LanguageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270LanguageNumber.setStatus("mandatory")


class _Tn3270PortKeymapStatus_Type(Integer32):
    """Custom type tn3270PortKeymapStatus based on Integer32"""
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


_Tn3270PortKeymapStatus_Type.__name__ = "Integer32"
_Tn3270PortKeymapStatus_Object = MibScalar
tn3270PortKeymapStatus = _Tn3270PortKeymapStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 3),
    _Tn3270PortKeymapStatus_Type()
)
tn3270PortKeymapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortKeymapStatus.setStatus("mandatory")
_Tn3270DeviceTable_Object = MibTable
tn3270DeviceTable = _Tn3270DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4)
)
if mibBuilder.loadTexts:
    tn3270DeviceTable.setStatus("mandatory")
_Tn3270DeviceEntry_Object = MibTableRow
tn3270DeviceEntry = _Tn3270DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1)
)
tn3270DeviceEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270DeviceName"),
)
if mibBuilder.loadTexts:
    tn3270DeviceEntry.setStatus("mandatory")


class _Tn3270DeviceName_Type(DisplayString):
    """Custom type tn3270DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270DeviceName_Type.__name__ = "DisplayString"
_Tn3270DeviceName_Object = MibTableColumn
tn3270DeviceName = _Tn3270DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 1),
    _Tn3270DeviceName_Type()
)
tn3270DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceName.setStatus("mandatory")


class _Tn3270DeviceStatus_Type(Integer32):
    """Custom type tn3270DeviceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270DeviceStatus_Type.__name__ = "Integer32"
_Tn3270DeviceStatus_Object = MibTableColumn
tn3270DeviceStatus = _Tn3270DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 2),
    _Tn3270DeviceStatus_Type()
)
tn3270DeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270DeviceStatus.setStatus("mandatory")


class _Tn3270DeviceType_Type(DisplayString):
    """Custom type tn3270DeviceType based on DisplayString"""
    defaultValue = OctetString("VT100")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Tn3270DeviceType_Type.__name__ = "DisplayString"
_Tn3270DeviceType_Object = MibTableColumn
tn3270DeviceType = _Tn3270DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 3),
    _Tn3270DeviceType_Type()
)
tn3270DeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270DeviceType.setStatus("mandatory")


class _Tn3270Device3278Model_Type(Integer32):
    """Custom type tn3270Device3278Model based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("model2", 1),
          ("model5", 2))
    )


_Tn3270Device3278Model_Type.__name__ = "Integer32"
_Tn3270Device3278Model_Object = MibTableColumn
tn3270Device3278Model = _Tn3270Device3278Model_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 4),
    _Tn3270Device3278Model_Type()
)
tn3270Device3278Model.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270Device3278Model.setStatus("mandatory")


class _Tn3270DeviceKeyNumber_Type(Integer32):
    """Custom type tn3270DeviceKeyNumber based on Integer32"""
    defaultValue = 70


_Tn3270DeviceKeyNumber_Object = MibTableColumn
tn3270DeviceKeyNumber = _Tn3270DeviceKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 5),
    _Tn3270DeviceKeyNumber_Type()
)
tn3270DeviceKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceKeyNumber.setStatus("mandatory")


class _Tn3270DeviceScreenNumber_Type(Integer32):
    """Custom type tn3270DeviceScreenNumber based on Integer32"""
    defaultValue = 24


_Tn3270DeviceScreenNumber_Object = MibTableColumn
tn3270DeviceScreenNumber = _Tn3270DeviceScreenNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 6),
    _Tn3270DeviceScreenNumber_Type()
)
tn3270DeviceScreenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceScreenNumber.setStatus("mandatory")
_Tn3270KeyTable_Object = MibTable
tn3270KeyTable = _Tn3270KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5)
)
if mibBuilder.loadTexts:
    tn3270KeyTable.setStatus("mandatory")
_Tn3270KeyEntry_Object = MibTableRow
tn3270KeyEntry = _Tn3270KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1)
)
tn3270KeyEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270KeyDeviceName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270KeyName"),
)
if mibBuilder.loadTexts:
    tn3270KeyEntry.setStatus("mandatory")


class _Tn3270KeyDeviceName_Type(DisplayString):
    """Custom type tn3270KeyDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270KeyDeviceName_Type.__name__ = "DisplayString"
_Tn3270KeyDeviceName_Object = MibTableColumn
tn3270KeyDeviceName = _Tn3270KeyDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 1),
    _Tn3270KeyDeviceName_Type()
)
tn3270KeyDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270KeyDeviceName.setStatus("mandatory")


class _Tn3270KeyName_Type(Integer32):
    """Custom type tn3270KeyName based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("backtab", 3),
          ("centsign", 15),
          ("clear", 68),
          ("cursordown", 7),
          ("cursorleft", 5),
          ("cursorright", 6),
          ("cursorsel", 69),
          ("cursorup", 4),
          ("delete", 9),
          ("duplicate", 16),
          ("enter", 67),
          ("eraseeof", 10),
          ("eraseinput", 11),
          ("fastleft", 21),
          ("fastright", 22),
          ("fieldmark", 17),
          ("flushinput", 13),
          ("home", 8),
          ("insert", 12),
          ("newline", 1),
          ("pa1", 63),
          ("pa2", 64),
          ("pa3", 65),
          ("pf1", 39),
          ("pf10", 48),
          ("pf11", 49),
          ("pf12", 50),
          ("pf13", 51),
          ("pf14", 52),
          ("pf15", 53),
          ("pf16", 54),
          ("pf17", 55),
          ("pf18", 56),
          ("pf19", 57),
          ("pf2", 40),
          ("pf20", 58),
          ("pf21", 59),
          ("pf22", 60),
          ("pf23", 61),
          ("pf24", 62),
          ("pf3", 41),
          ("pf4", 42),
          ("pf5", 43),
          ("pf6", 44),
          ("pf7", 45),
          ("pf8", 46),
          ("pf9", 47),
          ("print", 24),
          ("refresh", 14),
          ("reset", 20),
          ("scroll", 18),
          ("showkeys", 23),
          ("status", 19),
          ("sysreq", 66),
          ("tab", 2),
          ("test", 70))
    )


_Tn3270KeyName_Type.__name__ = "Integer32"
_Tn3270KeyName_Object = MibTableColumn
tn3270KeyName = _Tn3270KeyName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 2),
    _Tn3270KeyName_Type()
)
tn3270KeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270KeyName.setStatus("mandatory")


class _Tn3270KeyStatus_Type(Integer32):
    """Custom type tn3270KeyStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270KeyStatus_Type.__name__ = "Integer32"
_Tn3270KeyStatus_Object = MibTableColumn
tn3270KeyStatus = _Tn3270KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 3),
    _Tn3270KeyStatus_Type()
)
tn3270KeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyStatus.setStatus("deprecated")


class _Tn3270KeyCharacterSequence_Type(OctetString):
    """Custom type tn3270KeyCharacterSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Tn3270KeyCharacterSequence_Type.__name__ = "OctetString"
_Tn3270KeyCharacterSequence_Object = MibTableColumn
tn3270KeyCharacterSequence = _Tn3270KeyCharacterSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 4),
    _Tn3270KeyCharacterSequence_Type()
)
tn3270KeyCharacterSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyCharacterSequence.setStatus("mandatory")


class _Tn3270KeyDescription_Type(DisplayString):
    """Custom type tn3270KeyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Tn3270KeyDescription_Type.__name__ = "DisplayString"
_Tn3270KeyDescription_Object = MibTableColumn
tn3270KeyDescription = _Tn3270KeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 5),
    _Tn3270KeyDescription_Type()
)
tn3270KeyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyDescription.setStatus("mandatory")
_Tn3270ScreenTable_Object = MibTable
tn3270ScreenTable = _Tn3270ScreenTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6)
)
if mibBuilder.loadTexts:
    tn3270ScreenTable.setStatus("mandatory")
_Tn3270ScreenEntry_Object = MibTableRow
tn3270ScreenEntry = _Tn3270ScreenEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1)
)
tn3270ScreenEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270ScreenDeviceName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270ScreenActionName"),
)
if mibBuilder.loadTexts:
    tn3270ScreenEntry.setStatus("mandatory")


class _Tn3270ScreenDeviceName_Type(DisplayString):
    """Custom type tn3270ScreenDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270ScreenDeviceName_Type.__name__ = "DisplayString"
_Tn3270ScreenDeviceName_Object = MibTableColumn
tn3270ScreenDeviceName = _Tn3270ScreenDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 1),
    _Tn3270ScreenDeviceName_Type()
)
tn3270ScreenDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270ScreenDeviceName.setStatus("mandatory")


class _Tn3270ScreenActionName_Type(Integer32):
    """Custom type tn3270ScreenActionName based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("base", 32),
          ("beep", 6),
          ("blinkoff", 11),
          ("blinkon", 10),
          ("boldoff", 9),
          ("boldon", 8),
          ("charset", 7),
          ("clearscr", 2),
          ("col132", 4),
          ("col80", 5),
          ("colorBlue", 16),
          ("colorGreen", 19),
          ("colorPink", 18),
          ("colorRed", 17),
          ("colorTurquoise", 20),
          ("colorWhite", 22),
          ("colorYellow", 21),
          ("eraseeol", 1),
          ("movecursor", 3),
          ("reset1", 28),
          ("reset2", 29),
          ("reset3", 30),
          ("reset4", 31),
          ("reverseoff", 15),
          ("reverseon", 14),
          ("sgr", 33),
          ("status1", 26),
          ("status2", 27),
          ("underscoreoff", 13),
          ("underscoreon", 12))
    )


_Tn3270ScreenActionName_Type.__name__ = "Integer32"
_Tn3270ScreenActionName_Object = MibTableColumn
tn3270ScreenActionName = _Tn3270ScreenActionName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 2),
    _Tn3270ScreenActionName_Type()
)
tn3270ScreenActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270ScreenActionName.setStatus("mandatory")


class _Tn3270ScreenStatus_Type(Integer32):
    """Custom type tn3270ScreenStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270ScreenStatus_Type.__name__ = "Integer32"
_Tn3270ScreenStatus_Object = MibTableColumn
tn3270ScreenStatus = _Tn3270ScreenStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 3),
    _Tn3270ScreenStatus_Type()
)
tn3270ScreenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270ScreenStatus.setStatus("deprecated")


class _Tn3270ScreenCharacterSequence_Type(OctetString):
    """Custom type tn3270ScreenCharacterSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Tn3270ScreenCharacterSequence_Type.__name__ = "OctetString"
_Tn3270ScreenCharacterSequence_Object = MibTableColumn
tn3270ScreenCharacterSequence = _Tn3270ScreenCharacterSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 4),
    _Tn3270ScreenCharacterSequence_Type()
)
tn3270ScreenCharacterSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270ScreenCharacterSequence.setStatus("mandatory")
_Tn3270LanguageTable_Object = MibTable
tn3270LanguageTable = _Tn3270LanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7)
)
if mibBuilder.loadTexts:
    tn3270LanguageTable.setStatus("mandatory")
_Tn3270LanguageEntry_Object = MibTableRow
tn3270LanguageEntry = _Tn3270LanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1)
)
tn3270LanguageEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270LanguageName"),
)
if mibBuilder.loadTexts:
    tn3270LanguageEntry.setStatus("mandatory")


class _Tn3270LanguageName_Type(DisplayString):
    """Custom type tn3270LanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270LanguageName_Type.__name__ = "DisplayString"
_Tn3270LanguageName_Object = MibTableColumn
tn3270LanguageName = _Tn3270LanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1, 1),
    _Tn3270LanguageName_Type()
)
tn3270LanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270LanguageName.setStatus("mandatory")


class _Tn3270LanguageStatus_Type(Integer32):
    """Custom type tn3270LanguageStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270LanguageStatus_Type.__name__ = "Integer32"
_Tn3270LanguageStatus_Object = MibTableColumn
tn3270LanguageStatus = _Tn3270LanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1, 2),
    _Tn3270LanguageStatus_Type()
)
tn3270LanguageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270LanguageStatus.setStatus("mandatory")
_EToALanguageTable_Object = MibTable
eToALanguageTable = _EToALanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8)
)
if mibBuilder.loadTexts:
    eToALanguageTable.setStatus("mandatory")
_EToALanguageEntry_Object = MibTableRow
eToALanguageEntry = _EToALanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1)
)
eToALanguageEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "eToALanguageName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "eToAOffset"),
)
if mibBuilder.loadTexts:
    eToALanguageEntry.setStatus("mandatory")


class _EToALanguageName_Type(DisplayString):
    """Custom type eToALanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EToALanguageName_Type.__name__ = "DisplayString"
_EToALanguageName_Object = MibTableColumn
eToALanguageName = _EToALanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 1),
    _EToALanguageName_Type()
)
eToALanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eToALanguageName.setStatus("mandatory")


class _EToAOffset_Type(Integer32):
    """Custom type eToAOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 256),
    )


_EToAOffset_Type.__name__ = "Integer32"
_EToAOffset_Object = MibTableColumn
eToAOffset = _EToAOffset_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 2),
    _EToAOffset_Type()
)
eToAOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eToAOffset.setStatus("mandatory")


class _EToAValue_Type(Integer32):
    """Custom type eToAValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_EToAValue_Type.__name__ = "Integer32"
_EToAValue_Object = MibTableColumn
eToAValue = _EToAValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 3),
    _EToAValue_Type()
)
eToAValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eToAValue.setStatus("mandatory")
_AToELanguageTable_Object = MibTable
aToELanguageTable = _AToELanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9)
)
if mibBuilder.loadTexts:
    aToELanguageTable.setStatus("mandatory")
_AToELanguageEntry_Object = MibTableRow
aToELanguageEntry = _AToELanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1)
)
aToELanguageEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "aToELanguageName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "aToEOffset"),
)
if mibBuilder.loadTexts:
    aToELanguageEntry.setStatus("mandatory")


class _AToELanguageName_Type(DisplayString):
    """Custom type aToELanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AToELanguageName_Type.__name__ = "DisplayString"
_AToELanguageName_Object = MibTableColumn
aToELanguageName = _AToELanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 1),
    _AToELanguageName_Type()
)
aToELanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aToELanguageName.setStatus("mandatory")


class _AToEOffset_Type(Integer32):
    """Custom type aToEOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 256),
    )


_AToEOffset_Type.__name__ = "Integer32"
_AToEOffset_Object = MibTableColumn
aToEOffset = _AToEOffset_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 2),
    _AToEOffset_Type()
)
aToEOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aToEOffset.setStatus("mandatory")


class _AToEValue_Type(Integer32):
    """Custom type aToEValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AToEValue_Type.__name__ = "Integer32"
_AToEValue_Object = MibTableColumn
aToEValue = _AToEValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 3),
    _AToEValue_Type()
)
aToEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aToEValue.setStatus("mandatory")
_Tn3270PortTable_Object = MibTable
tn3270PortTable = _Tn3270PortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10)
)
if mibBuilder.loadTexts:
    tn3270PortTable.setStatus("mandatory")
_Tn3270PortEntry_Object = MibTableRow
tn3270PortEntry = _Tn3270PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1)
)
tn3270PortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "tn3270PortIndex"),
)
if mibBuilder.loadTexts:
    tn3270PortEntry.setStatus("mandatory")
_Tn3270PortIndex_Type = Integer32
_Tn3270PortIndex_Object = MibTableColumn
tn3270PortIndex = _Tn3270PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 1),
    _Tn3270PortIndex_Type()
)
tn3270PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270PortIndex.setStatus("mandatory")


class _Tn3270PortDeviceName_Type(DisplayString):
    """Custom type tn3270PortDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Tn3270PortDeviceName_Type.__name__ = "DisplayString"
_Tn3270PortDeviceName_Object = MibTableColumn
tn3270PortDeviceName = _Tn3270PortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 2),
    _Tn3270PortDeviceName_Type()
)
tn3270PortDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortDeviceName.setStatus("mandatory")


class _Tn3270PortLanguageName_Type(DisplayString):
    """Custom type tn3270PortLanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Tn3270PortLanguageName_Type.__name__ = "DisplayString"
_Tn3270PortLanguageName_Object = MibTableColumn
tn3270PortLanguageName = _Tn3270PortLanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 3),
    _Tn3270PortLanguageName_Type()
)
tn3270PortLanguageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortLanguageName.setStatus("mandatory")


class _Tn3270PortExtendedAttributes_Type(Integer32):
    """Custom type tn3270PortExtendedAttributes based on Integer32"""
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


_Tn3270PortExtendedAttributes_Type.__name__ = "Integer32"
_Tn3270PortExtendedAttributes_Object = MibTableColumn
tn3270PortExtendedAttributes = _Tn3270PortExtendedAttributes_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 4),
    _Tn3270PortExtendedAttributes_Type()
)
tn3270PortExtendedAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortExtendedAttributes.setStatus("mandatory")


class _Tn3270PortEorNegotiation_Type(Integer32):
    """Custom type tn3270PortEorNegotiation based on Integer32"""
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


_Tn3270PortEorNegotiation_Type.__name__ = "Integer32"
_Tn3270PortEorNegotiation_Object = MibTableColumn
tn3270PortEorNegotiation = _Tn3270PortEorNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 5),
    _Tn3270PortEorNegotiation_Type()
)
tn3270PortEorNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortEorNegotiation.setStatus("mandatory")


class _Tn3270PortErrorLock_Type(Integer32):
    """Custom type tn3270PortErrorLock based on Integer32"""
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


_Tn3270PortErrorLock_Type.__name__ = "Integer32"
_Tn3270PortErrorLock_Object = MibTableColumn
tn3270PortErrorLock = _Tn3270PortErrorLock_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 6),
    _Tn3270PortErrorLock_Type()
)
tn3270PortErrorLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortErrorLock.setStatus("mandatory")
_Tn3270PortPrinterPort_Type = Integer32
_Tn3270PortPrinterPort_Object = MibTableColumn
tn3270PortPrinterPort = _Tn3270PortPrinterPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 7),
    _Tn3270PortPrinterPort_Type()
)
tn3270PortPrinterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortPrinterPort.setStatus("mandatory")


class _Tn3270PortOutgoingTcpPort_Type(Integer32):
    """Custom type tn3270PortOutgoingTcpPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Tn3270PortOutgoingTcpPort_Type.__name__ = "Integer32"
_Tn3270PortOutgoingTcpPort_Object = MibTableColumn
tn3270PortOutgoingTcpPort = _Tn3270PortOutgoingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 8),
    _Tn3270PortOutgoingTcpPort_Type()
)
tn3270PortOutgoingTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortOutgoingTcpPort.setStatus("mandatory")


class _Tn3270PortSpaceInsert_Type(Integer32):
    """Custom type tn3270PortSpaceInsert based on Integer32"""
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


_Tn3270PortSpaceInsert_Type.__name__ = "Integer32"
_Tn3270PortSpaceInsert_Object = MibTableColumn
tn3270PortSpaceInsert = _Tn3270PortSpaceInsert_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 9),
    _Tn3270PortSpaceInsert_Type()
)
tn3270PortSpaceInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortSpaceInsert.setStatus("mandatory")


class _Tn3270PortTypeAhead_Type(Integer32):
    """Custom type tn3270PortTypeAhead based on Integer32"""
    defaultValue = 2

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


_Tn3270PortTypeAhead_Type.__name__ = "Integer32"
_Tn3270PortTypeAhead_Object = MibTableColumn
tn3270PortTypeAhead = _Tn3270PortTypeAhead_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 10),
    _Tn3270PortTypeAhead_Type()
)
tn3270PortTypeAhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortTypeAhead.setStatus("mandatory")


class _Tn3270PrefixKeyMap_Type(Integer32):
    """Custom type tn3270PrefixKeyMap based on Integer32"""
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


_Tn3270PrefixKeyMap_Type.__name__ = "Integer32"
_Tn3270PrefixKeyMap_Object = MibTableColumn
tn3270PrefixKeyMap = _Tn3270PrefixKeyMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 11),
    _Tn3270PrefixKeyMap_Type()
)
tn3270PrefixKeyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PrefixKeyMap.setStatus("mandatory")


class _Tn3270PortScanner_Type(Integer32):
    """Custom type tn3270PortScanner based on Integer32"""
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


_Tn3270PortScanner_Type.__name__ = "Integer32"
_Tn3270PortScanner_Object = MibTableColumn
tn3270PortScanner = _Tn3270PortScanner_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 12),
    _Tn3270PortScanner_Type()
)
tn3270PortScanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortScanner.setStatus("mandatory")
_XKerberos_ObjectIdentity = ObjectIdentity
xKerberos = _XKerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 8)
)


class _KerbStatus_Type(Integer32):
    """Custom type kerbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("none", 1))
    )


_KerbStatus_Type.__name__ = "Integer32"
_KerbStatus_Object = MibScalar
kerbStatus = _KerbStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 1),
    _KerbStatus_Type()
)
kerbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbStatus.setStatus("mandatory")


class _KerbRealm_Type(DisplayString):
    """Custom type kerbRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_KerbRealm_Type.__name__ = "DisplayString"
_KerbRealm_Object = MibScalar
kerbRealm = _KerbRealm_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 2),
    _KerbRealm_Type()
)
kerbRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbRealm.setStatus("mandatory")


class _KerbQueryLimit_Type(Integer32):
    """Custom type kerbQueryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_KerbQueryLimit_Type.__name__ = "Integer32"
_KerbQueryLimit_Object = MibScalar
kerbQueryLimit = _KerbQueryLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 3),
    _KerbQueryLimit_Type()
)
kerbQueryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbQueryLimit.setStatus("mandatory")


class _KerbMasterName_Type(DisplayString):
    """Custom type kerbMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbMasterName_Type.__name__ = "DisplayString"
_KerbMasterName_Object = MibScalar
kerbMasterName = _KerbMasterName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 4),
    _KerbMasterName_Type()
)
kerbMasterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbMasterName.setStatus("mandatory")


class _KerbServerName1_Type(DisplayString):
    """Custom type kerbServerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbServerName1_Type.__name__ = "DisplayString"
_KerbServerName1_Object = MibScalar
kerbServerName1 = _KerbServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 5),
    _KerbServerName1_Type()
)
kerbServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbServerName1.setStatus("mandatory")


class _KerbServerName2_Type(DisplayString):
    """Custom type kerbServerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbServerName2_Type.__name__ = "DisplayString"
_KerbServerName2_Object = MibScalar
kerbServerName2 = _KerbServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 6),
    _KerbServerName2_Type()
)
kerbServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbServerName2.setStatus("mandatory")
_KerbInsecureLogins_Type = Counter32
_KerbInsecureLogins_Object = MibScalar
kerbInsecureLogins = _KerbInsecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 7),
    _KerbInsecureLogins_Type()
)
kerbInsecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbInsecureLogins.setStatus("mandatory")
_KerbSecureLogins_Type = Counter32
_KerbSecureLogins_Object = MibScalar
kerbSecureLogins = _KerbSecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 8),
    _KerbSecureLogins_Type()
)
kerbSecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbSecureLogins.setStatus("mandatory")
_KerbSecureLoginsFailed_Type = Counter32
_KerbSecureLoginsFailed_Object = MibScalar
kerbSecureLoginsFailed = _KerbSecureLoginsFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 9),
    _KerbSecureLoginsFailed_Type()
)
kerbSecureLoginsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbSecureLoginsFailed.setStatus("mandatory")
_KerbPasswordChangeFailed_Type = Counter32
_KerbPasswordChangeFailed_Object = MibScalar
kerbPasswordChangeFailed = _KerbPasswordChangeFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 10),
    _KerbPasswordChangeFailed_Type()
)
kerbPasswordChangeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbPasswordChangeFailed.setStatus("mandatory")
_KerbError_Type = Integer32
_KerbError_Object = MibScalar
kerbError = _KerbError_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 11),
    _KerbError_Type()
)
kerbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbError.setStatus("mandatory")
_KerbErrorTime_Type = DateTime
_KerbErrorTime_Object = MibScalar
kerbErrorTime = _KerbErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 12),
    _KerbErrorTime_Type()
)
kerbErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbErrorTime.setStatus("mandatory")
_KerbMasterAccess_Type = Counter32
_KerbMasterAccess_Object = MibScalar
kerbMasterAccess = _KerbMasterAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 13),
    _KerbMasterAccess_Type()
)
kerbMasterAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbMasterAccess.setStatus("mandatory")
_KerbMasterAccessFailed_Type = Counter32
_KerbMasterAccessFailed_Object = MibScalar
kerbMasterAccessFailed = _KerbMasterAccessFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 14),
    _KerbMasterAccessFailed_Type()
)
kerbMasterAccessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbMasterAccessFailed.setStatus("mandatory")
_KerbServerAccess1_Type = Counter32
_KerbServerAccess1_Object = MibScalar
kerbServerAccess1 = _KerbServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 15),
    _KerbServerAccess1_Type()
)
kerbServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccess1.setStatus("mandatory")
_KerbServerAccessFailed1_Type = Counter32
_KerbServerAccessFailed1_Object = MibScalar
kerbServerAccessFailed1 = _KerbServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 16),
    _KerbServerAccessFailed1_Type()
)
kerbServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccessFailed1.setStatus("mandatory")
_KerbServerAccess2_Type = Counter32
_KerbServerAccess2_Object = MibScalar
kerbServerAccess2 = _KerbServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 17),
    _KerbServerAccess2_Type()
)
kerbServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccess2.setStatus("mandatory")
_KerbServerAccessFailed2_Type = Counter32
_KerbServerAccessFailed2_Object = MibScalar
kerbServerAccessFailed2 = _KerbServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 18),
    _KerbServerAccessFailed2_Type()
)
kerbServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccessFailed2.setStatus("mandatory")
_KerbPortTable_Object = MibTable
kerbPortTable = _KerbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19)
)
if mibBuilder.loadTexts:
    kerbPortTable.setStatus("mandatory")
_KerbPortEntry_Object = MibTableRow
kerbPortEntry = _KerbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1)
)
kerbPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "kerbPortIndex"),
)
if mibBuilder.loadTexts:
    kerbPortEntry.setStatus("mandatory")
_KerbPortIndex_Type = Integer32
_KerbPortIndex_Object = MibTableColumn
kerbPortIndex = _KerbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1, 1),
    _KerbPortIndex_Type()
)
kerbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbPortIndex.setStatus("mandatory")


class _KerbPortStatus_Type(Integer32):
    """Custom type kerbPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("none", 1))
    )


_KerbPortStatus_Type.__name__ = "Integer32"
_KerbPortStatus_Object = MibTableColumn
kerbPortStatus = _KerbPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1, 2),
    _KerbPortStatus_Type()
)
kerbPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbPortStatus.setStatus("mandatory")


class _KerbServerPort_Type(Integer32):
    """Custom type kerbServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(88,
              750)
        )
    )
    namedValues = NamedValues(
        *(("experimentalPort", 750),
          ("standardPort", 88))
    )


_KerbServerPort_Type.__name__ = "Integer32"
_KerbServerPort_Object = MibScalar
kerbServerPort = _KerbServerPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 20),
    _KerbServerPort_Type()
)
kerbServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbServerPort.setStatus("mandatory")
_XPortSecurity_ObjectIdentity = ObjectIdentity
xPortSecurity = _XPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 9)
)
_PsEntryNumber_Type = Integer32
_PsEntryNumber_Object = MibScalar
psEntryNumber = _PsEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 1),
    _PsEntryNumber_Type()
)
psEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryNumber.setStatus("mandatory")
_PsEntryNumberLimit_Type = Integer32
_PsEntryNumberLimit_Object = MibScalar
psEntryNumberLimit = _PsEntryNumberLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 2),
    _PsEntryNumberLimit_Type()
)
psEntryNumberLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryNumberLimit.setStatus("mandatory")
_PsEntryInvalidIndex_Type = Integer32
_PsEntryInvalidIndex_Object = MibScalar
psEntryInvalidIndex = _PsEntryInvalidIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 3),
    _PsEntryInvalidIndex_Type()
)
psEntryInvalidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryInvalidIndex.setStatus("mandatory")
_PsPortTable_Object = MibTable
psPortTable = _PsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4)
)
if mibBuilder.loadTexts:
    psPortTable.setStatus("mandatory")
_PsPortEntry_Object = MibTableRow
psPortEntry = _PsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1)
)
psPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "psPortIndex"),
)
if mibBuilder.loadTexts:
    psPortEntry.setStatus("mandatory")
_PsPortIndex_Type = Integer32
_PsPortIndex_Object = MibTableColumn
psPortIndex = _PsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 1),
    _PsPortIndex_Type()
)
psPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPortIndex.setStatus("mandatory")


class _PsPortDefaultInboundAccess_Type(Integer32):
    """Custom type psPortDefaultInboundAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsPortDefaultInboundAccess_Type.__name__ = "Integer32"
_PsPortDefaultInboundAccess_Object = MibTableColumn
psPortDefaultInboundAccess = _PsPortDefaultInboundAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 2),
    _PsPortDefaultInboundAccess_Type()
)
psPortDefaultInboundAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPortDefaultInboundAccess.setStatus("mandatory")


class _PsPortDefaultOutboundAccess_Type(Integer32):
    """Custom type psPortDefaultOutboundAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsPortDefaultOutboundAccess_Type.__name__ = "Integer32"
_PsPortDefaultOutboundAccess_Object = MibTableColumn
psPortDefaultOutboundAccess = _PsPortDefaultOutboundAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 3),
    _PsPortDefaultOutboundAccess_Type()
)
psPortDefaultOutboundAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPortDefaultOutboundAccess.setStatus("mandatory")


class _PsClrInternetSecurity_Type(Integer32):
    """Custom type psClrInternetSecurity based on Integer32"""
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


_PsClrInternetSecurity_Type.__name__ = "Integer32"
_PsClrInternetSecurity_Object = MibTableColumn
psClrInternetSecurity = _PsClrInternetSecurity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 4),
    _PsClrInternetSecurity_Type()
)
psClrInternetSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psClrInternetSecurity.setStatus("mandatory")
_PsTable_Object = MibTable
psTable = _PsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5)
)
if mibBuilder.loadTexts:
    psTable.setStatus("mandatory")
_PsEntry_Object = MibTableRow
psEntry = _PsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1)
)
psEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "psEntryIndex"),
)
if mibBuilder.loadTexts:
    psEntry.setStatus("mandatory")
_PsEntryIndex_Type = Integer32
_PsEntryIndex_Object = MibTableColumn
psEntryIndex = _PsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 1),
    _PsEntryIndex_Type()
)
psEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryIndex.setStatus("mandatory")


class _PsEntryStatus_Type(Integer32):
    """Custom type psEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PsEntryStatus_Type.__name__ = "Integer32"
_PsEntryStatus_Object = MibTableColumn
psEntryStatus = _PsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 2),
    _PsEntryStatus_Type()
)
psEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryStatus.setStatus("mandatory")
_PsEntryAddress_Type = IpAddress
_PsEntryAddress_Object = MibTableColumn
psEntryAddress = _PsEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 3),
    _PsEntryAddress_Type()
)
psEntryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryAddress.setStatus("mandatory")
_PsEntryMask_Type = IpAddress
_PsEntryMask_Object = MibTableColumn
psEntryMask = _PsEntryMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 4),
    _PsEntryMask_Type()
)
psEntryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryMask.setStatus("mandatory")


class _PsEntryAccess_Type(Integer32):
    """Custom type psEntryAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsEntryAccess_Type.__name__ = "Integer32"
_PsEntryAccess_Object = MibTableColumn
psEntryAccess = _PsEntryAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 5),
    _PsEntryAccess_Type()
)
psEntryAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryAccess.setStatus("mandatory")


class _PsEntryDirection_Type(Integer32):
    """Custom type psEntryDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_PsEntryDirection_Type.__name__ = "Integer32"
_PsEntryDirection_Object = MibTableColumn
psEntryDirection = _PsEntryDirection_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 6),
    _PsEntryDirection_Type()
)
psEntryDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryDirection.setStatus("mandatory")
_PsEntryPortMap_Type = OctetString
_PsEntryPortMap_Object = MibTableColumn
psEntryPortMap = _PsEntryPortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 7),
    _PsEntryPortMap_Type()
)
psEntryPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryPortMap.setStatus("mandatory")
_XXremote_ObjectIdentity = ObjectIdentity
xXremote = _XXremote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 10)
)


class _XremoteServerName1_Type(DisplayString):
    """Custom type xremoteServerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremoteServerName1_Type.__name__ = "DisplayString"
_XremoteServerName1_Object = MibScalar
xremoteServerName1 = _XremoteServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 1),
    _XremoteServerName1_Type()
)
xremoteServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremoteServerName1.setStatus("mandatory")


class _XremoteServerName2_Type(DisplayString):
    """Custom type xremoteServerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremoteServerName2_Type.__name__ = "DisplayString"
_XremoteServerName2_Object = MibScalar
xremoteServerName2 = _XremoteServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 2),
    _XremoteServerName2_Type()
)
xremoteServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremoteServerName2.setStatus("mandatory")
_XremoteServerAccess1_Type = Counter32
_XremoteServerAccess1_Object = MibScalar
xremoteServerAccess1 = _XremoteServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 3),
    _XremoteServerAccess1_Type()
)
xremoteServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccess1.setStatus("mandatory")
_XremoteServerAccessFailed1_Type = Counter32
_XremoteServerAccessFailed1_Object = MibScalar
xremoteServerAccessFailed1 = _XremoteServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 4),
    _XremoteServerAccessFailed1_Type()
)
xremoteServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccessFailed1.setStatus("mandatory")
_XremoteServerAccess2_Type = Counter32
_XremoteServerAccess2_Object = MibScalar
xremoteServerAccess2 = _XremoteServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 5),
    _XremoteServerAccess2_Type()
)
xremoteServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccess2.setStatus("mandatory")
_XremoteServerAccessFailed2_Type = Counter32
_XremoteServerAccessFailed2_Object = MibScalar
xremoteServerAccessFailed2 = _XremoteServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 6),
    _XremoteServerAccessFailed2_Type()
)
xremoteServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccessFailed2.setStatus("mandatory")
_XremoteSessions_Type = Gauge32
_XremoteSessions_Object = MibScalar
xremoteSessions = _XremoteSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 7),
    _XremoteSessions_Type()
)
xremoteSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteSessions.setStatus("mandatory")
_XremotePortTable_Object = MibTable
xremotePortTable = _XremotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8)
)
if mibBuilder.loadTexts:
    xremotePortTable.setStatus("mandatory")
_XremotePortEntry_Object = MibTableRow
xremotePortEntry = _XremotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1)
)
xremotePortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "xremotePortIndex"),
)
if mibBuilder.loadTexts:
    xremotePortEntry.setStatus("mandatory")
_XremotePortIndex_Type = Integer32
_XremotePortIndex_Object = MibTableColumn
xremotePortIndex = _XremotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 1),
    _XremotePortIndex_Type()
)
xremotePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremotePortIndex.setStatus("mandatory")


class _XremotePortXremote_Type(Integer32):
    """Custom type xremotePortXremote based on Integer32"""
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


_XremotePortXremote_Type.__name__ = "Integer32"
_XremotePortXremote_Object = MibTableColumn
xremotePortXremote = _XremotePortXremote_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 2),
    _XremotePortXremote_Type()
)
xremotePortXremote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXremote.setStatus("mandatory")


class _XremotePortXdmQuery_Type(Integer32):
    """Custom type xremotePortXdmQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("indirect", 3),
          ("specific", 1))
    )


_XremotePortXdmQuery_Type.__name__ = "Integer32"
_XremotePortXdmQuery_Object = MibTableColumn
xremotePortXdmQuery = _XremotePortXdmQuery_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 3),
    _XremotePortXdmQuery_Type()
)
xremotePortXdmQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXdmQuery.setStatus("mandatory")


class _XremotePortXdmHost_Type(DisplayString):
    """Custom type xremotePortXdmHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremotePortXdmHost_Type.__name__ = "DisplayString"
_XremotePortXdmHost_Object = MibTableColumn
xremotePortXdmHost = _XremotePortXdmHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 4),
    _XremotePortXdmHost_Type()
)
xremotePortXdmHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXdmHost.setStatus("mandatory")
_XremoteServerClients_Type = Gauge32
_XremoteServerClients_Object = MibScalar
xremoteServerClients = _XremoteServerClients_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 9),
    _XremoteServerClients_Type()
)
xremoteServerClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerClients.setStatus("mandatory")
_XRotary_ObjectIdentity = ObjectIdentity
xRotary = _XRotary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 11)
)
_RotaryNumber_Type = Integer32
_RotaryNumber_Object = MibScalar
rotaryNumber = _RotaryNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 1),
    _RotaryNumber_Type()
)
rotaryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotaryNumber.setStatus("mandatory")
_RotaryTable_Object = MibTable
rotaryTable = _RotaryTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2)
)
if mibBuilder.loadTexts:
    rotaryTable.setStatus("mandatory")
_RotaryEntry_Object = MibTableRow
rotaryEntry = _RotaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1)
)
rotaryEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "rotaryAddress"),
)
if mibBuilder.loadTexts:
    rotaryEntry.setStatus("mandatory")
_RotaryAddress_Type = IpAddress
_RotaryAddress_Object = MibTableColumn
rotaryAddress = _RotaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 1),
    _RotaryAddress_Type()
)
rotaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotaryAddress.setStatus("mandatory")


class _RotaryStatus_Type(Integer32):
    """Custom type rotaryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RotaryStatus_Type.__name__ = "Integer32"
_RotaryStatus_Object = MibTableColumn
rotaryStatus = _RotaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 2),
    _RotaryStatus_Type()
)
rotaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rotaryStatus.setStatus("mandatory")
_RotaryPortMap_Type = OctetString
_RotaryPortMap_Object = MibTableColumn
rotaryPortMap = _RotaryPortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 3),
    _RotaryPortMap_Type()
)
rotaryPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rotaryPortMap.setStatus("mandatory")
_XEgp_ObjectIdentity = ObjectIdentity
xEgp = _XEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 12)
)


class _EgpRouting_Type(Integer32):
    """Custom type egpRouting based on Integer32"""
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


_EgpRouting_Type.__name__ = "Integer32"
_EgpRouting_Object = MibScalar
egpRouting = _EgpRouting_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 1),
    _EgpRouting_Type()
)
egpRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egpRouting.setStatus("mandatory")


class _EgpStatus_Type(Integer32):
    """Custom type egpStatus based on Integer32"""
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
        *(("active", 1),
          ("noAS", 6),
          ("noEgpRouting", 4),
          ("noIpRouting", 3),
          ("noMemory", 2),
          ("noNeighbors", 5))
    )


_EgpStatus_Type.__name__ = "Integer32"
_EgpStatus_Object = MibScalar
egpStatus = _EgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 2),
    _EgpStatus_Type()
)
egpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpStatus.setStatus("mandatory")
_EgpNbrTable_Object = MibTable
egpNbrTable = _EgpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 3)
)
if mibBuilder.loadTexts:
    egpNbrTable.setStatus("mandatory")
_EgpNbrEntry_Object = MibTableRow
egpNbrEntry = _EgpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 3, 1)
)
egpNbrEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "egpNbrAddr"),
)
if mibBuilder.loadTexts:
    egpNbrEntry.setStatus("mandatory")
_EgpNbrAddr_Type = IpAddress
_EgpNbrAddr_Object = MibTableColumn
egpNbrAddr = _EgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 3, 1, 1),
    _EgpNbrAddr_Type()
)
egpNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpNbrAddr.setStatus("mandatory")


class _EgpNbrIntervalDead_Type(Integer32):
    """Custom type egpNbrIntervalDead based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EgpNbrIntervalDead_Type.__name__ = "Integer32"
_EgpNbrIntervalDead_Object = MibTableColumn
egpNbrIntervalDead = _EgpNbrIntervalDead_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 3, 1, 2),
    _EgpNbrIntervalDead_Type()
)
egpNbrIntervalDead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egpNbrIntervalDead.setStatus("mandatory")


class _EgpNbrStatus_Type(Integer32):
    """Custom type egpNbrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_EgpNbrStatus_Type.__name__ = "Integer32"
_EgpNbrStatus_Object = MibTableColumn
egpNbrStatus = _EgpNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 12, 3, 1, 3),
    _EgpNbrStatus_Type()
)
egpNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egpNbrStatus.setStatus("mandatory")
_XOspf_ObjectIdentity = ObjectIdentity
xOspf = _XOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 13)
)


class _OspfAutoConfigure_Type(Integer32):
    """Custom type ospfAutoConfigure based on Integer32"""
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


_OspfAutoConfigure_Type.__name__ = "Integer32"
_OspfAutoConfigure_Object = MibScalar
ospfAutoConfigure = _OspfAutoConfigure_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 1),
    _OspfAutoConfigure_Type()
)
ospfAutoConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAutoConfigure.setStatus("mandatory")


class _OspfStatus_Type(Integer32):
    """Custom type ospfStatus based on Integer32"""
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
        *(("active", 1),
          ("noAreas", 5),
          ("noBackBone", 10),
          ("noBackBoneAndInterface", 9),
          ("noBackBoneAndVirtualInterfaces", 8),
          ("noInterfaces", 6),
          ("noIpRouting", 3),
          ("noMemory", 2),
          ("noOspfRouting", 4),
          ("noRtrId", 7))
    )


_OspfStatus_Type.__name__ = "Integer32"
_OspfStatus_Object = MibScalar
ospfStatus = _OspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 2),
    _OspfStatus_Type()
)
ospfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatus.setStatus("mandatory")
_OspfIfMtrcTable_Object = MibTable
ospfIfMtrcTable = _OspfIfMtrcTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3)
)
if mibBuilder.loadTexts:
    ospfIfMtrcTable.setStatus("mandatory")
_OspfIfMtrcEntry_Object = MibTableRow
ospfIfMtrcEntry = _OspfIfMtrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3, 1)
)
ospfIfMtrcEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfIfMtrcIpAddress"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfIfMtrcAddressLessIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfIfMtrcTos"),
)
if mibBuilder.loadTexts:
    ospfIfMtrcEntry.setStatus("mandatory")
_OspfIfMtrcIpAddress_Type = IpAddress
_OspfIfMtrcIpAddress_Object = MibTableColumn
ospfIfMtrcIpAddress = _OspfIfMtrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3, 1, 1),
    _OspfIfMtrcIpAddress_Type()
)
ospfIfMtrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMtrcIpAddress.setStatus("mandatory")
_OspfIfMtrcAddressLessIf_Type = Integer32
_OspfIfMtrcAddressLessIf_Object = MibTableColumn
ospfIfMtrcAddressLessIf = _OspfIfMtrcAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3, 1, 2),
    _OspfIfMtrcAddressLessIf_Type()
)
ospfIfMtrcAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMtrcAddressLessIf.setStatus("mandatory")


class _OspfIfMtrcTos_Type(Integer32):
    """Custom type ospfIfMtrcTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OspfIfMtrcTos_Type.__name__ = "Integer32"
_OspfIfMtrcTos_Object = MibTableColumn
ospfIfMtrcTos = _OspfIfMtrcTos_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3, 1, 3),
    _OspfIfMtrcTos_Type()
)
ospfIfMtrcTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMtrcTos.setStatus("mandatory")


class _OspfIfMtrcCostActual_Type(Integer32):
    """Custom type ospfIfMtrcCostActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfIfMtrcCostActual_Type.__name__ = "Integer32"
_OspfIfMtrcCostActual_Object = MibTableColumn
ospfIfMtrcCostActual = _OspfIfMtrcCostActual_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 3, 1, 4),
    _OspfIfMtrcCostActual_Type()
)
ospfIfMtrcCostActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMtrcCostActual.setStatus("mandatory")
_OspfXIfTable_Object = MibTable
ospfXIfTable = _OspfXIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4)
)
if mibBuilder.loadTexts:
    ospfXIfTable.setStatus("mandatory")
_OspfXIfEntry_Object = MibTableRow
ospfXIfEntry = _OspfXIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4, 1)
)
ospfXIfEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfXIfIpAddress"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfXIfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfXIfEntry.setStatus("mandatory")
_OspfXIfIpAddress_Type = IpAddress
_OspfXIfIpAddress_Object = MibTableColumn
ospfXIfIpAddress = _OspfXIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4, 1, 1),
    _OspfXIfIpAddress_Type()
)
ospfXIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXIfIpAddress.setStatus("mandatory")
_OspfXIfAddressLessIf_Type = Integer32
_OspfXIfAddressLessIf_Object = MibTableColumn
ospfXIfAddressLessIf = _OspfXIfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4, 1, 2),
    _OspfXIfAddressLessIf_Type()
)
ospfXIfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXIfAddressLessIf.setStatus("mandatory")


class _OspfXIfTypeActual_Type(Integer32):
    """Custom type ospfXIfTypeActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nonbroadcast", 2),
          ("pointToPoint", 3))
    )


_OspfXIfTypeActual_Type.__name__ = "Integer32"
_OspfXIfTypeActual_Object = MibTableColumn
ospfXIfTypeActual = _OspfXIfTypeActual_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4, 1, 3),
    _OspfXIfTypeActual_Type()
)
ospfXIfTypeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXIfTypeActual.setStatus("mandatory")


class _OspfXIfStatus_Type(Integer32):
    """Custom type ospfXIfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_OspfXIfStatus_Type.__name__ = "Integer32"
_OspfXIfStatus_Object = MibTableColumn
ospfXIfStatus = _OspfXIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 4, 1, 4),
    _OspfXIfStatus_Type()
)
ospfXIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfXIfStatus.setStatus("mandatory")
_OspfXAreaTable_Object = MibTable
ospfXAreaTable = _OspfXAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 5)
)
if mibBuilder.loadTexts:
    ospfXAreaTable.setStatus("mandatory")
_OspfXAreaEntry_Object = MibTableRow
ospfXAreaEntry = _OspfXAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 5, 1)
)
ospfXAreaEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ospfXAreaId"),
)
if mibBuilder.loadTexts:
    ospfXAreaEntry.setStatus("mandatory")
_OspfXAreaId_Type = IpAddress
_OspfXAreaId_Object = MibTableColumn
ospfXAreaId = _OspfXAreaId_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 5, 1, 1),
    _OspfXAreaId_Type()
)
ospfXAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXAreaId.setStatus("mandatory")


class _OspfXAreaStatus_Type(Integer32):
    """Custom type ospfXAreaStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_OspfXAreaStatus_Type.__name__ = "Integer32"
_OspfXAreaStatus_Object = MibTableColumn
ospfXAreaStatus = _OspfXAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 13, 5, 1, 2),
    _OspfXAreaStatus_Type()
)
ospfXAreaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfXAreaStatus.setStatus("mandatory")
_XRouterIp_ObjectIdentity = ObjectIdentity
xRouterIp = _XRouterIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 14)
)
_IpAdExtTable_Object = MibTable
ipAdExtTable = _IpAdExtTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 1)
)
if mibBuilder.loadTexts:
    ipAdExtTable.setStatus("mandatory")
_IpAdExtEntry_Object = MibTableRow
ipAdExtEntry = _IpAdExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 1, 1)
)
ipAdExtEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipAdEntExtAddress"),
)
if mibBuilder.loadTexts:
    ipAdExtEntry.setStatus("mandatory")
_IpAdEntExtAddress_Type = IpAddress
_IpAdEntExtAddress_Object = MibTableColumn
ipAdEntExtAddress = _IpAdEntExtAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 1, 1, 1),
    _IpAdEntExtAddress_Type()
)
ipAdEntExtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntExtAddress.setStatus("mandatory")


class _IpAdEntExtProxyArp_Type(Integer32):
    """Custom type ipAdEntExtProxyArp based on Integer32"""
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


_IpAdEntExtProxyArp_Type.__name__ = "Integer32"
_IpAdEntExtProxyArp_Object = MibTableColumn
ipAdEntExtProxyArp = _IpAdEntExtProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 1, 1, 2),
    _IpAdEntExtProxyArp_Type()
)
ipAdEntExtProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAdEntExtProxyArp.setStatus("mandatory")


class _IpAdEntExtRip_Type(Integer32):
    """Custom type ipAdEntExtRip based on Integer32"""
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


_IpAdEntExtRip_Type.__name__ = "Integer32"
_IpAdEntExtRip_Object = MibTableColumn
ipAdEntExtRip = _IpAdEntExtRip_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 1, 1, 3),
    _IpAdEntExtRip_Type()
)
ipAdEntExtRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntExtRip.setStatus("deprecated")
_IpRouterIfTable_Object = MibTable
ipRouterIfTable = _IpRouterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2)
)
if mibBuilder.loadTexts:
    ipRouterIfTable.setStatus("mandatory")
_IpRouterIfEntry_Object = MibTableRow
ipRouterIfEntry = _IpRouterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1)
)
ipRouterIfEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipRouterIfIndex"),
)
if mibBuilder.loadTexts:
    ipRouterIfEntry.setStatus("mandatory")
_IpRouterIfIndex_Type = Integer32
_IpRouterIfIndex_Object = MibTableColumn
ipRouterIfIndex = _IpRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 1),
    _IpRouterIfIndex_Type()
)
ipRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfIndex.setStatus("mandatory")


class _IpRouterIfProtocolPriority_Type(Integer32):
    """Custom type ipRouterIfProtocolPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_IpRouterIfProtocolPriority_Type.__name__ = "Integer32"
_IpRouterIfProtocolPriority_Object = MibTableColumn
ipRouterIfProtocolPriority = _IpRouterIfProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 2),
    _IpRouterIfProtocolPriority_Type()
)
ipRouterIfProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouterIfProtocolPriority.setStatus("mandatory")


class _IpRouterIfMTU_Type(Integer32):
    """Custom type ipRouterIfMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 65535),
    )


_IpRouterIfMTU_Type.__name__ = "Integer32"
_IpRouterIfMTU_Object = MibTableColumn
ipRouterIfMTU = _IpRouterIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 3),
    _IpRouterIfMTU_Type()
)
ipRouterIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouterIfMTU.setStatus("mandatory")


class _IpRouterIfRDP_Type(Integer32):
    """Custom type ipRouterIfRDP based on Integer32"""
    defaultValue = 2

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


_IpRouterIfRDP_Type.__name__ = "Integer32"
_IpRouterIfRDP_Object = MibTableColumn
ipRouterIfRDP = _IpRouterIfRDP_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 4),
    _IpRouterIfRDP_Type()
)
ipRouterIfRDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouterIfRDP.setStatus("mandatory")
_IpRouterIfArpPacketsIn_Type = Counter32
_IpRouterIfArpPacketsIn_Object = MibTableColumn
ipRouterIfArpPacketsIn = _IpRouterIfArpPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 5),
    _IpRouterIfArpPacketsIn_Type()
)
ipRouterIfArpPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfArpPacketsIn.setStatus("mandatory")
_IpRouterIfArpPacketsOut_Type = Counter32
_IpRouterIfArpPacketsOut_Object = MibTableColumn
ipRouterIfArpPacketsOut = _IpRouterIfArpPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 6),
    _IpRouterIfArpPacketsOut_Type()
)
ipRouterIfArpPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfArpPacketsOut.setStatus("mandatory")
_IpRouterIfPacketsIn_Type = Counter32
_IpRouterIfPacketsIn_Object = MibTableColumn
ipRouterIfPacketsIn = _IpRouterIfPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 7),
    _IpRouterIfPacketsIn_Type()
)
ipRouterIfPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfPacketsIn.setStatus("mandatory")
_IpRouterIfPacketsOut_Type = Counter32
_IpRouterIfPacketsOut_Object = MibTableColumn
ipRouterIfPacketsOut = _IpRouterIfPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 8),
    _IpRouterIfPacketsOut_Type()
)
ipRouterIfPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfPacketsOut.setStatus("mandatory")
_IpRouterIfForwardsIn_Type = Counter32
_IpRouterIfForwardsIn_Object = MibTableColumn
ipRouterIfForwardsIn = _IpRouterIfForwardsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 9),
    _IpRouterIfForwardsIn_Type()
)
ipRouterIfForwardsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfForwardsIn.setStatus("mandatory")
_IpRouterIfForwardsOut_Type = Counter32
_IpRouterIfForwardsOut_Object = MibTableColumn
ipRouterIfForwardsOut = _IpRouterIfForwardsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 2, 1, 10),
    _IpRouterIfForwardsOut_Type()
)
ipRouterIfForwardsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouterIfForwardsOut.setStatus("mandatory")
_XIpTraffic_ObjectIdentity = ObjectIdentity
xIpTraffic = _XIpTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3)
)


class _IpTrafficSort_Type(Integer32):
    """Custom type ipTrafficSort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_IpTrafficSort_Type.__name__ = "Integer32"
_IpTrafficSort_Object = MibScalar
ipTrafficSort = _IpTrafficSort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 1),
    _IpTrafficSort_Type()
)
ipTrafficSort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTrafficSort.setStatus("mandatory")
_IpTrafficTable_Object = MibTable
ipTrafficTable = _IpTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2)
)
if mibBuilder.loadTexts:
    ipTrafficTable.setStatus("mandatory")
_IpTrafficEntry_Object = MibTableRow
ipTrafficEntry = _IpTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1)
)
ipTrafficEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipTrafficIndex"),
)
if mibBuilder.loadTexts:
    ipTrafficEntry.setStatus("mandatory")
_IpTrafficIndex_Type = Integer32
_IpTrafficIndex_Object = MibTableColumn
ipTrafficIndex = _IpTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 1),
    _IpTrafficIndex_Type()
)
ipTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficIndex.setStatus("mandatory")
_IpTrafficPercent_Type = Integer32
_IpTrafficPercent_Object = MibTableColumn
ipTrafficPercent = _IpTrafficPercent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 2),
    _IpTrafficPercent_Type()
)
ipTrafficPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficPercent.setStatus("mandatory")
_IpTrafficDstAddr_Type = IpAddress
_IpTrafficDstAddr_Object = MibTableColumn
ipTrafficDstAddr = _IpTrafficDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 3),
    _IpTrafficDstAddr_Type()
)
ipTrafficDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficDstAddr.setStatus("mandatory")
_IpTrafficSrcAddr_Type = IpAddress
_IpTrafficSrcAddr_Object = MibTableColumn
ipTrafficSrcAddr = _IpTrafficSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 4),
    _IpTrafficSrcAddr_Type()
)
ipTrafficSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficSrcAddr.setStatus("mandatory")


class _IpTrafficProtocol_Type(Integer32):
    """Custom type ipTrafficProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpTrafficProtocol_Type.__name__ = "Integer32"
_IpTrafficProtocol_Object = MibTableColumn
ipTrafficProtocol = _IpTrafficProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 5),
    _IpTrafficProtocol_Type()
)
ipTrafficProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficProtocol.setStatus("mandatory")


class _IpTrafficDstPort_Type(Integer32):
    """Custom type ipTrafficDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTrafficDstPort_Type.__name__ = "Integer32"
_IpTrafficDstPort_Object = MibTableColumn
ipTrafficDstPort = _IpTrafficDstPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 6),
    _IpTrafficDstPort_Type()
)
ipTrafficDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficDstPort.setStatus("mandatory")


class _IpTrafficSrcPort_Type(Integer32):
    """Custom type ipTrafficSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpTrafficSrcPort_Type.__name__ = "Integer32"
_IpTrafficSrcPort_Object = MibTableColumn
ipTrafficSrcPort = _IpTrafficSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 7),
    _IpTrafficSrcPort_Type()
)
ipTrafficSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficSrcPort.setStatus("mandatory")
_IpTrafficIf_Type = Integer32
_IpTrafficIf_Object = MibTableColumn
ipTrafficIf = _IpTrafficIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 2, 1, 8),
    _IpTrafficIf_Type()
)
ipTrafficIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTrafficIf.setStatus("mandatory")


class _IpTrafficMonitoring_Type(Integer32):
    """Custom type ipTrafficMonitoring based on Integer32"""
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


_IpTrafficMonitoring_Type.__name__ = "Integer32"
_IpTrafficMonitoring_Object = MibScalar
ipTrafficMonitoring = _IpTrafficMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 3, 3),
    _IpTrafficMonitoring_Type()
)
ipTrafficMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTrafficMonitoring.setStatus("mandatory")
_XIpNetToMediaTable_Object = MibTable
xIpNetToMediaTable = _XIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 4)
)
if mibBuilder.loadTexts:
    xIpNetToMediaTable.setStatus("mandatory")
_XIpNetToMediaEntry_Object = MibTableRow
xIpNetToMediaEntry = _XIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 4, 1)
)
xIpNetToMediaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    xIpNetToMediaEntry.setStatus("mandatory")
_XIpNetToMediaCircuit_Type = Integer32
_XIpNetToMediaCircuit_Object = MibTableColumn
xIpNetToMediaCircuit = _XIpNetToMediaCircuit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 4, 1, 1),
    _XIpNetToMediaCircuit_Type()
)
xIpNetToMediaCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIpNetToMediaCircuit.setStatus("mandatory")


class _XIpNetToMediaReverseArp_Type(Integer32):
    """Custom type xIpNetToMediaReverseArp based on Integer32"""
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


_XIpNetToMediaReverseArp_Type.__name__ = "Integer32"
_XIpNetToMediaReverseArp_Object = MibTableColumn
xIpNetToMediaReverseArp = _XIpNetToMediaReverseArp_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 14, 4, 1, 2),
    _XIpNetToMediaReverseArp_Type()
)
xIpNetToMediaReverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xIpNetToMediaReverseArp.setStatus("mandatory")
_XRouterUdp_ObjectIdentity = ObjectIdentity
xRouterUdp = _XRouterUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 15)
)
_UdpBcstServerTable_Object = MibTable
udpBcstServerTable = _UdpBcstServerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 1)
)
if mibBuilder.loadTexts:
    udpBcstServerTable.setStatus("mandatory")
_UdpBcstServerEntry_Object = MibTableRow
udpBcstServerEntry = _UdpBcstServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 1, 1)
)
udpBcstServerEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "udpBcstServerAddress"),
)
if mibBuilder.loadTexts:
    udpBcstServerEntry.setStatus("mandatory")
_UdpBcstServerAddress_Type = IpAddress
_UdpBcstServerAddress_Object = MibTableColumn
udpBcstServerAddress = _UdpBcstServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 1, 1, 1),
    _UdpBcstServerAddress_Type()
)
udpBcstServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBcstServerAddress.setStatus("mandatory")


class _UdpBcstServerStatus_Type(Integer32):
    """Custom type udpBcstServerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_UdpBcstServerStatus_Type.__name__ = "Integer32"
_UdpBcstServerStatus_Object = MibTableColumn
udpBcstServerStatus = _UdpBcstServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 1, 1, 2),
    _UdpBcstServerStatus_Type()
)
udpBcstServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpBcstServerStatus.setStatus("mandatory")
_UdpBcstPortTable_Object = MibTable
udpBcstPortTable = _UdpBcstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 2)
)
if mibBuilder.loadTexts:
    udpBcstPortTable.setStatus("mandatory")
_UdpBcstPortEntry_Object = MibTableRow
udpBcstPortEntry = _UdpBcstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 2, 1)
)
udpBcstPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "udpBcstPort"),
)
if mibBuilder.loadTexts:
    udpBcstPortEntry.setStatus("mandatory")
_UdpBcstPort_Type = Integer32
_UdpBcstPort_Object = MibTableColumn
udpBcstPort = _UdpBcstPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 2, 1, 1),
    _UdpBcstPort_Type()
)
udpBcstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpBcstPort.setStatus("mandatory")


class _UdpBcstPortStatus_Type(Integer32):
    """Custom type udpBcstPortStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_UdpBcstPortStatus_Type.__name__ = "Integer32"
_UdpBcstPortStatus_Object = MibTableColumn
udpBcstPortStatus = _UdpBcstPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 2, 1, 2),
    _UdpBcstPortStatus_Type()
)
udpBcstPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpBcstPortStatus.setStatus("mandatory")


class _UdpBcstRouting_Type(Integer32):
    """Custom type udpBcstRouting based on Integer32"""
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


_UdpBcstRouting_Type.__name__ = "Integer32"
_UdpBcstRouting_Object = MibScalar
udpBcstRouting = _UdpBcstRouting_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 15, 3),
    _UdpBcstRouting_Type()
)
udpBcstRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpBcstRouting.setStatus("mandatory")
_XRouterPolicy_ObjectIdentity = ObjectIdentity
xRouterPolicy = _XRouterPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 16)
)
_XImport_ObjectIdentity = ObjectIdentity
xImport = _XImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1)
)
_ImpEgpRuleTable_Object = MibTable
impEgpRuleTable = _ImpEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1)
)
if mibBuilder.loadTexts:
    impEgpRuleTable.setStatus("mandatory")
_ImpEgpRuleEntry_Object = MibTableRow
impEgpRuleEntry = _ImpEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1)
)
impEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "impEgpRuleAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "impEgpRuleNetwork"),
)
if mibBuilder.loadTexts:
    impEgpRuleEntry.setStatus("mandatory")


class _ImpEgpRuleAs_Type(Integer32):
    """Custom type impEgpRuleAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ImpEgpRuleAs_Type.__name__ = "Integer32"
_ImpEgpRuleAs_Object = MibTableColumn
impEgpRuleAs = _ImpEgpRuleAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 1),
    _ImpEgpRuleAs_Type()
)
impEgpRuleAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impEgpRuleAs.setStatus("mandatory")
_ImpEgpRuleNetwork_Type = IpAddress
_ImpEgpRuleNetwork_Object = MibTableColumn
impEgpRuleNetwork = _ImpEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 2),
    _ImpEgpRuleNetwork_Type()
)
impEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impEgpRuleNetwork.setStatus("mandatory")


class _ImpEgpRuleAction_Type(Integer32):
    """Custom type impEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_ImpEgpRuleAction_Type.__name__ = "Integer32"
_ImpEgpRuleAction_Object = MibTableColumn
impEgpRuleAction = _ImpEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 3),
    _ImpEgpRuleAction_Type()
)
impEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRuleAction.setStatus("mandatory")


class _ImpEgpRulePreference_Type(Integer32):
    """Custom type impEgpRulePreference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ImpEgpRulePreference_Type.__name__ = "Integer32"
_ImpEgpRulePreference_Object = MibTableColumn
impEgpRulePreference = _ImpEgpRulePreference_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 4),
    _ImpEgpRulePreference_Type()
)
impEgpRulePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRulePreference.setStatus("mandatory")


class _ImpEgpRuleType_Type(Integer32):
    """Custom type impEgpRuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImpEgpRuleType_Type.__name__ = "Integer32"
_ImpEgpRuleType_Object = MibTableColumn
impEgpRuleType = _ImpEgpRuleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 5),
    _ImpEgpRuleType_Type()
)
impEgpRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRuleType.setStatus("mandatory")


class _ImpEgpRuleMetricAction_Type(Integer32):
    """Custom type impEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ImpEgpRuleMetricAction_Type.__name__ = "Integer32"
_ImpEgpRuleMetricAction_Object = MibTableColumn
impEgpRuleMetricAction = _ImpEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 6),
    _ImpEgpRuleMetricAction_Type()
)
impEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRuleMetricAction.setStatus("mandatory")


class _ImpEgpRuleMetric_Type(Integer32):
    """Custom type impEgpRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ImpEgpRuleMetric_Type.__name__ = "Integer32"
_ImpEgpRuleMetric_Object = MibTableColumn
impEgpRuleMetric = _ImpEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 7),
    _ImpEgpRuleMetric_Type()
)
impEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRuleMetric.setStatus("mandatory")


class _ImpEgpRuleStatus_Type(Integer32):
    """Custom type impEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ImpEgpRuleStatus_Type.__name__ = "Integer32"
_ImpEgpRuleStatus_Object = MibTableColumn
impEgpRuleStatus = _ImpEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 1, 1, 8),
    _ImpEgpRuleStatus_Type()
)
impEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impEgpRuleStatus.setStatus("mandatory")
_ImpOspfRuleTable_Object = MibTable
impOspfRuleTable = _ImpOspfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 2)
)
if mibBuilder.loadTexts:
    impOspfRuleTable.setStatus("mandatory")
_ImpOspfRuleEntry_Object = MibTableRow
impOspfRuleEntry = _ImpOspfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 2, 1)
)
impOspfRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "impOspfRuleNetwork"),
)
if mibBuilder.loadTexts:
    impOspfRuleEntry.setStatus("mandatory")
_ImpOspfRuleNetwork_Type = IpAddress
_ImpOspfRuleNetwork_Object = MibTableColumn
impOspfRuleNetwork = _ImpOspfRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 2, 1, 1),
    _ImpOspfRuleNetwork_Type()
)
impOspfRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impOspfRuleNetwork.setStatus("mandatory")


class _ImpOspfRulePreference_Type(Integer32):
    """Custom type impOspfRulePreference based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ImpOspfRulePreference_Type.__name__ = "Integer32"
_ImpOspfRulePreference_Object = MibTableColumn
impOspfRulePreference = _ImpOspfRulePreference_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 2, 1, 2),
    _ImpOspfRulePreference_Type()
)
impOspfRulePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impOspfRulePreference.setStatus("mandatory")


class _ImpOspfRuleStatus_Type(Integer32):
    """Custom type impOspfRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ImpOspfRuleStatus_Type.__name__ = "Integer32"
_ImpOspfRuleStatus_Object = MibTableColumn
impOspfRuleStatus = _ImpOspfRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 2, 1, 3),
    _ImpOspfRuleStatus_Type()
)
impOspfRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impOspfRuleStatus.setStatus("mandatory")
_ImpRipRuleTable_Object = MibTable
impRipRuleTable = _ImpRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3)
)
if mibBuilder.loadTexts:
    impRipRuleTable.setStatus("mandatory")
_ImpRipRuleEntry_Object = MibTableRow
impRipRuleEntry = _ImpRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1)
)
impRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "impRipRuleFromIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "impRipRuleNetwork"),
)
if mibBuilder.loadTexts:
    impRipRuleEntry.setStatus("mandatory")
_ImpRipRuleFromIf_Type = IpAddress
_ImpRipRuleFromIf_Object = MibTableColumn
impRipRuleFromIf = _ImpRipRuleFromIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 1),
    _ImpRipRuleFromIf_Type()
)
impRipRuleFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impRipRuleFromIf.setStatus("mandatory")
_ImpRipRuleNetwork_Type = IpAddress
_ImpRipRuleNetwork_Object = MibTableColumn
impRipRuleNetwork = _ImpRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 2),
    _ImpRipRuleNetwork_Type()
)
impRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impRipRuleNetwork.setStatus("mandatory")


class _ImpRipRuleAction_Type(Integer32):
    """Custom type impRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_ImpRipRuleAction_Type.__name__ = "Integer32"
_ImpRipRuleAction_Object = MibTableColumn
impRipRuleAction = _ImpRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 3),
    _ImpRipRuleAction_Type()
)
impRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRuleAction.setStatus("mandatory")


class _ImpRipRulePreference_Type(Integer32):
    """Custom type impRipRulePreference based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImpRipRulePreference_Type.__name__ = "Integer32"
_ImpRipRulePreference_Object = MibTableColumn
impRipRulePreference = _ImpRipRulePreference_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 4),
    _ImpRipRulePreference_Type()
)
impRipRulePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRulePreference.setStatus("mandatory")


class _ImpRipRuleType_Type(Integer32):
    """Custom type impRipRuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImpRipRuleType_Type.__name__ = "Integer32"
_ImpRipRuleType_Object = MibTableColumn
impRipRuleType = _ImpRipRuleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 5),
    _ImpRipRuleType_Type()
)
impRipRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRuleType.setStatus("mandatory")


class _ImpRipRuleMetricAction_Type(Integer32):
    """Custom type impRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ImpRipRuleMetricAction_Type.__name__ = "Integer32"
_ImpRipRuleMetricAction_Object = MibTableColumn
impRipRuleMetricAction = _ImpRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 6),
    _ImpRipRuleMetricAction_Type()
)
impRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRuleMetricAction.setStatus("mandatory")


class _ImpRipRuleMetric_Type(Integer32):
    """Custom type impRipRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ImpRipRuleMetric_Type.__name__ = "Integer32"
_ImpRipRuleMetric_Object = MibTableColumn
impRipRuleMetric = _ImpRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 7),
    _ImpRipRuleMetric_Type()
)
impRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRuleMetric.setStatus("mandatory")


class _ImpRipRuleStatus_Type(Integer32):
    """Custom type impRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ImpRipRuleStatus_Type.__name__ = "Integer32"
_ImpRipRuleStatus_Object = MibTableColumn
impRipRuleStatus = _ImpRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 3, 1, 8),
    _ImpRipRuleStatus_Type()
)
impRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impRipRuleStatus.setStatus("mandatory")
_ImpIsisRuleTable_Object = MibTable
impIsisRuleTable = _ImpIsisRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4)
)
if mibBuilder.loadTexts:
    impIsisRuleTable.setStatus("mandatory")
_ImpIsisRuleEntry_Object = MibTableRow
impIsisRuleEntry = _ImpIsisRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1)
)
impIsisRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "impIsisRuleNetwork"),
)
if mibBuilder.loadTexts:
    impIsisRuleEntry.setStatus("mandatory")
_ImpIsisRuleNetwork_Type = IpAddress
_ImpIsisRuleNetwork_Object = MibTableColumn
impIsisRuleNetwork = _ImpIsisRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 1),
    _ImpIsisRuleNetwork_Type()
)
impIsisRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impIsisRuleNetwork.setStatus("mandatory")


class _ImpIsisRuleAction_Type(Integer32):
    """Custom type impIsisRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_ImpIsisRuleAction_Type.__name__ = "Integer32"
_ImpIsisRuleAction_Object = MibTableColumn
impIsisRuleAction = _ImpIsisRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 2),
    _ImpIsisRuleAction_Type()
)
impIsisRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRuleAction.setStatus("mandatory")


class _ImpIsisRulePreference_Type(Integer32):
    """Custom type impIsisRulePreference based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImpIsisRulePreference_Type.__name__ = "Integer32"
_ImpIsisRulePreference_Object = MibTableColumn
impIsisRulePreference = _ImpIsisRulePreference_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 3),
    _ImpIsisRulePreference_Type()
)
impIsisRulePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRulePreference.setStatus("mandatory")


class _ImpIsisRuleType_Type(Integer32):
    """Custom type impIsisRuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImpIsisRuleType_Type.__name__ = "Integer32"
_ImpIsisRuleType_Object = MibTableColumn
impIsisRuleType = _ImpIsisRuleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 4),
    _ImpIsisRuleType_Type()
)
impIsisRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRuleType.setStatus("mandatory")


class _ImpIsisRuleMetricAction_Type(Integer32):
    """Custom type impIsisRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ImpIsisRuleMetricAction_Type.__name__ = "Integer32"
_ImpIsisRuleMetricAction_Object = MibTableColumn
impIsisRuleMetricAction = _ImpIsisRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 5),
    _ImpIsisRuleMetricAction_Type()
)
impIsisRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRuleMetricAction.setStatus("mandatory")


class _ImpIsisRuleMetric_Type(Integer32):
    """Custom type impIsisRuleMetric based on Integer32"""
    defaultValue = 0


_ImpIsisRuleMetric_Object = MibTableColumn
impIsisRuleMetric = _ImpIsisRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 6),
    _ImpIsisRuleMetric_Type()
)
impIsisRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRuleMetric.setStatus("mandatory")


class _ImpIsisRuleStatus_Type(Integer32):
    """Custom type impIsisRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ImpIsisRuleStatus_Type.__name__ = "Integer32"
_ImpIsisRuleStatus_Object = MibTableColumn
impIsisRuleStatus = _ImpIsisRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 1, 4, 1, 7),
    _ImpIsisRuleStatus_Type()
)
impIsisRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    impIsisRuleStatus.setStatus("mandatory")
_XExport_ObjectIdentity = ObjectIdentity
xExport = _XExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2)
)
_ExpEgpToEgpRuleTable_Object = MibTable
expEgpToEgpRuleTable = _ExpEgpToEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1)
)
if mibBuilder.loadTexts:
    expEgpToEgpRuleTable.setStatus("mandatory")
_ExpEgpToEgpRuleEntry_Object = MibTableRow
expEgpToEgpRuleEntry = _ExpEgpToEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1)
)
expEgpToEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToEgpRuleToAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToEgpRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToEgpRuleFromAs"),
)
if mibBuilder.loadTexts:
    expEgpToEgpRuleEntry.setStatus("mandatory")


class _ExpEgpToEgpRuleToAs_Type(Integer32):
    """Custom type expEgpToEgpRuleToAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpEgpToEgpRuleToAs_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleToAs_Object = MibTableColumn
expEgpToEgpRuleToAs = _ExpEgpToEgpRuleToAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 1),
    _ExpEgpToEgpRuleToAs_Type()
)
expEgpToEgpRuleToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToEgpRuleToAs.setStatus("mandatory")
_ExpEgpToEgpRuleNetwork_Type = IpAddress
_ExpEgpToEgpRuleNetwork_Object = MibTableColumn
expEgpToEgpRuleNetwork = _ExpEgpToEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 2),
    _ExpEgpToEgpRuleNetwork_Type()
)
expEgpToEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToEgpRuleNetwork.setStatus("mandatory")


class _ExpEgpToEgpRuleFromAs_Type(Integer32):
    """Custom type expEgpToEgpRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpEgpToEgpRuleFromAs_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleFromAs_Object = MibTableColumn
expEgpToEgpRuleFromAs = _ExpEgpToEgpRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 3),
    _ExpEgpToEgpRuleFromAs_Type()
)
expEgpToEgpRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToEgpRuleFromAs.setStatus("mandatory")


class _ExpEgpToEgpRuleAction_Type(Integer32):
    """Custom type expEgpToEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpEgpToEgpRuleAction_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleAction_Object = MibTableColumn
expEgpToEgpRuleAction = _ExpEgpToEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 4),
    _ExpEgpToEgpRuleAction_Type()
)
expEgpToEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToEgpRuleAction.setStatus("mandatory")


class _ExpEgpToEgpRuleMetricAction_Type(Integer32):
    """Custom type expEgpToEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToEgpRuleMetricAction_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleMetricAction_Object = MibTableColumn
expEgpToEgpRuleMetricAction = _ExpEgpToEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 5),
    _ExpEgpToEgpRuleMetricAction_Type()
)
expEgpToEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToEgpRuleMetricAction.setStatus("mandatory")


class _ExpEgpToEgpRuleMetric_Type(Integer32):
    """Custom type expEgpToEgpRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpEgpToEgpRuleMetric_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleMetric_Object = MibTableColumn
expEgpToEgpRuleMetric = _ExpEgpToEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 6),
    _ExpEgpToEgpRuleMetric_Type()
)
expEgpToEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToEgpRuleMetric.setStatus("mandatory")


class _ExpEgpToEgpRuleStatus_Type(Integer32):
    """Custom type expEgpToEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpEgpToEgpRuleStatus_Type.__name__ = "Integer32"
_ExpEgpToEgpRuleStatus_Object = MibTableColumn
expEgpToEgpRuleStatus = _ExpEgpToEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 1, 1, 7),
    _ExpEgpToEgpRuleStatus_Type()
)
expEgpToEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToEgpRuleStatus.setStatus("mandatory")
_ExpOspfToEgpRuleTable_Object = MibTable
expOspfToEgpRuleTable = _ExpOspfToEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2)
)
if mibBuilder.loadTexts:
    expOspfToEgpRuleTable.setStatus("mandatory")
_ExpOspfToEgpRuleEntry_Object = MibTableRow
expOspfToEgpRuleEntry = _ExpOspfToEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1)
)
expOspfToEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToEgpRuleToAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToEgpRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToEgpRuleFromAs"),
)
if mibBuilder.loadTexts:
    expOspfToEgpRuleEntry.setStatus("mandatory")


class _ExpOspfToEgpRuleToAs_Type(Integer32):
    """Custom type expOspfToEgpRuleToAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpOspfToEgpRuleToAs_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleToAs_Object = MibTableColumn
expOspfToEgpRuleToAs = _ExpOspfToEgpRuleToAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 1),
    _ExpOspfToEgpRuleToAs_Type()
)
expOspfToEgpRuleToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToEgpRuleToAs.setStatus("mandatory")
_ExpOspfToEgpRuleNetwork_Type = IpAddress
_ExpOspfToEgpRuleNetwork_Object = MibTableColumn
expOspfToEgpRuleNetwork = _ExpOspfToEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 2),
    _ExpOspfToEgpRuleNetwork_Type()
)
expOspfToEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToEgpRuleNetwork.setStatus("mandatory")


class _ExpOspfToEgpRuleFromAs_Type(Integer32):
    """Custom type expOspfToEgpRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpOspfToEgpRuleFromAs_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleFromAs_Object = MibTableColumn
expOspfToEgpRuleFromAs = _ExpOspfToEgpRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 3),
    _ExpOspfToEgpRuleFromAs_Type()
)
expOspfToEgpRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToEgpRuleFromAs.setStatus("mandatory")


class _ExpOspfToEgpRuleAction_Type(Integer32):
    """Custom type expOspfToEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpOspfToEgpRuleAction_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleAction_Object = MibTableColumn
expOspfToEgpRuleAction = _ExpOspfToEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 4),
    _ExpOspfToEgpRuleAction_Type()
)
expOspfToEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToEgpRuleAction.setStatus("mandatory")


class _ExpOspfToEgpRuleMetricAction_Type(Integer32):
    """Custom type expOspfToEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToEgpRuleMetricAction_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleMetricAction_Object = MibTableColumn
expOspfToEgpRuleMetricAction = _ExpOspfToEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 5),
    _ExpOspfToEgpRuleMetricAction_Type()
)
expOspfToEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToEgpRuleMetricAction.setStatus("mandatory")


class _ExpOspfToEgpRuleMetric_Type(Integer32):
    """Custom type expOspfToEgpRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpOspfToEgpRuleMetric_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleMetric_Object = MibTableColumn
expOspfToEgpRuleMetric = _ExpOspfToEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 6),
    _ExpOspfToEgpRuleMetric_Type()
)
expOspfToEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToEgpRuleMetric.setStatus("mandatory")


class _ExpOspfToEgpRuleStatus_Type(Integer32):
    """Custom type expOspfToEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpOspfToEgpRuleStatus_Type.__name__ = "Integer32"
_ExpOspfToEgpRuleStatus_Object = MibTableColumn
expOspfToEgpRuleStatus = _ExpOspfToEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 2, 1, 7),
    _ExpOspfToEgpRuleStatus_Type()
)
expOspfToEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToEgpRuleStatus.setStatus("mandatory")
_ExpStaticToEgpRuleTable_Object = MibTable
expStaticToEgpRuleTable = _ExpStaticToEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3)
)
if mibBuilder.loadTexts:
    expStaticToEgpRuleTable.setStatus("mandatory")
_ExpStaticToEgpRuleEntry_Object = MibTableRow
expStaticToEgpRuleEntry = _ExpStaticToEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1)
)
expStaticToEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expStaticToEgpRuleToAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expStaticToEgpRuleNetwork"),
)
if mibBuilder.loadTexts:
    expStaticToEgpRuleEntry.setStatus("mandatory")


class _ExpStaticToEgpRuleToAs_Type(Integer32):
    """Custom type expStaticToEgpRuleToAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpStaticToEgpRuleToAs_Type.__name__ = "Integer32"
_ExpStaticToEgpRuleToAs_Object = MibTableColumn
expStaticToEgpRuleToAs = _ExpStaticToEgpRuleToAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 1),
    _ExpStaticToEgpRuleToAs_Type()
)
expStaticToEgpRuleToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expStaticToEgpRuleToAs.setStatus("mandatory")
_ExpStaticToEgpRuleNetwork_Type = IpAddress
_ExpStaticToEgpRuleNetwork_Object = MibTableColumn
expStaticToEgpRuleNetwork = _ExpStaticToEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 2),
    _ExpStaticToEgpRuleNetwork_Type()
)
expStaticToEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expStaticToEgpRuleNetwork.setStatus("mandatory")


class _ExpStaticToEgpRuleAction_Type(Integer32):
    """Custom type expStaticToEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpStaticToEgpRuleAction_Type.__name__ = "Integer32"
_ExpStaticToEgpRuleAction_Object = MibTableColumn
expStaticToEgpRuleAction = _ExpStaticToEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 3),
    _ExpStaticToEgpRuleAction_Type()
)
expStaticToEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToEgpRuleAction.setStatus("mandatory")


class _ExpStaticToEgpRuleMetricAction_Type(Integer32):
    """Custom type expStaticToEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToEgpRuleMetricAction_Type.__name__ = "Integer32"
_ExpStaticToEgpRuleMetricAction_Object = MibTableColumn
expStaticToEgpRuleMetricAction = _ExpStaticToEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 4),
    _ExpStaticToEgpRuleMetricAction_Type()
)
expStaticToEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToEgpRuleMetricAction.setStatus("mandatory")


class _ExpStaticToEgpRuleMetric_Type(Integer32):
    """Custom type expStaticToEgpRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpStaticToEgpRuleMetric_Type.__name__ = "Integer32"
_ExpStaticToEgpRuleMetric_Object = MibTableColumn
expStaticToEgpRuleMetric = _ExpStaticToEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 5),
    _ExpStaticToEgpRuleMetric_Type()
)
expStaticToEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToEgpRuleMetric.setStatus("mandatory")


class _ExpStaticToEgpRuleStatus_Type(Integer32):
    """Custom type expStaticToEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpStaticToEgpRuleStatus_Type.__name__ = "Integer32"
_ExpStaticToEgpRuleStatus_Object = MibTableColumn
expStaticToEgpRuleStatus = _ExpStaticToEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 3, 1, 6),
    _ExpStaticToEgpRuleStatus_Type()
)
expStaticToEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToEgpRuleStatus.setStatus("mandatory")
_ExpEgpToOspfRuleTable_Object = MibTable
expEgpToOspfRuleTable = _ExpEgpToOspfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4)
)
if mibBuilder.loadTexts:
    expEgpToOspfRuleTable.setStatus("mandatory")
_ExpEgpToOspfRuleEntry_Object = MibTableRow
expEgpToOspfRuleEntry = _ExpEgpToOspfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4, 1)
)
expEgpToOspfRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToOspfRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToOspfRuleFromAs"),
)
if mibBuilder.loadTexts:
    expEgpToOspfRuleEntry.setStatus("mandatory")
_ExpEgpToOspfRuleNetwork_Type = IpAddress
_ExpEgpToOspfRuleNetwork_Object = MibTableColumn
expEgpToOspfRuleNetwork = _ExpEgpToOspfRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4, 1, 1),
    _ExpEgpToOspfRuleNetwork_Type()
)
expEgpToOspfRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToOspfRuleNetwork.setStatus("mandatory")


class _ExpEgpToOspfRuleFromAs_Type(Integer32):
    """Custom type expEgpToOspfRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpEgpToOspfRuleFromAs_Type.__name__ = "Integer32"
_ExpEgpToOspfRuleFromAs_Object = MibTableColumn
expEgpToOspfRuleFromAs = _ExpEgpToOspfRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4, 1, 2),
    _ExpEgpToOspfRuleFromAs_Type()
)
expEgpToOspfRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToOspfRuleFromAs.setStatus("mandatory")


class _ExpEgpToOspfRuleAction_Type(Integer32):
    """Custom type expEgpToOspfRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpEgpToOspfRuleAction_Type.__name__ = "Integer32"
_ExpEgpToOspfRuleAction_Object = MibTableColumn
expEgpToOspfRuleAction = _ExpEgpToOspfRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4, 1, 3),
    _ExpEgpToOspfRuleAction_Type()
)
expEgpToOspfRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToOspfRuleAction.setStatus("mandatory")


class _ExpEgpToOspfRuleStatus_Type(Integer32):
    """Custom type expEgpToOspfRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpEgpToOspfRuleStatus_Type.__name__ = "Integer32"
_ExpEgpToOspfRuleStatus_Object = MibTableColumn
expEgpToOspfRuleStatus = _ExpEgpToOspfRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 4, 1, 4),
    _ExpEgpToOspfRuleStatus_Type()
)
expEgpToOspfRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToOspfRuleStatus.setStatus("mandatory")
_ExpRipToEgpRuleTable_Object = MibTable
expRipToEgpRuleTable = _ExpRipToEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5)
)
if mibBuilder.loadTexts:
    expRipToEgpRuleTable.setStatus("mandatory")
_ExpRipToEgpRuleEntry_Object = MibTableRow
expRipToEgpRuleEntry = _ExpRipToEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1)
)
expRipToEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToEgpRuleToAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToEgpRuleNetwork"),
)
if mibBuilder.loadTexts:
    expRipToEgpRuleEntry.setStatus("mandatory")


class _ExpRipToEgpRuleToAs_Type(Integer32):
    """Custom type expRipToEgpRuleToAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpRipToEgpRuleToAs_Type.__name__ = "Integer32"
_ExpRipToEgpRuleToAs_Object = MibTableColumn
expRipToEgpRuleToAs = _ExpRipToEgpRuleToAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 1),
    _ExpRipToEgpRuleToAs_Type()
)
expRipToEgpRuleToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToEgpRuleToAs.setStatus("mandatory")
_ExpRipToEgpRuleNetwork_Type = IpAddress
_ExpRipToEgpRuleNetwork_Object = MibTableColumn
expRipToEgpRuleNetwork = _ExpRipToEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 2),
    _ExpRipToEgpRuleNetwork_Type()
)
expRipToEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToEgpRuleNetwork.setStatus("mandatory")


class _ExpRipToEgpRuleAction_Type(Integer32):
    """Custom type expRipToEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpRipToEgpRuleAction_Type.__name__ = "Integer32"
_ExpRipToEgpRuleAction_Object = MibTableColumn
expRipToEgpRuleAction = _ExpRipToEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 3),
    _ExpRipToEgpRuleAction_Type()
)
expRipToEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToEgpRuleAction.setStatus("mandatory")


class _ExpRipToEgpRuleMetricAction_Type(Integer32):
    """Custom type expRipToEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToEgpRuleMetricAction_Type.__name__ = "Integer32"
_ExpRipToEgpRuleMetricAction_Object = MibTableColumn
expRipToEgpRuleMetricAction = _ExpRipToEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 4),
    _ExpRipToEgpRuleMetricAction_Type()
)
expRipToEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToEgpRuleMetricAction.setStatus("mandatory")


class _ExpRipToEgpRuleMetric_Type(Integer32):
    """Custom type expRipToEgpRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpRipToEgpRuleMetric_Type.__name__ = "Integer32"
_ExpRipToEgpRuleMetric_Object = MibTableColumn
expRipToEgpRuleMetric = _ExpRipToEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 5),
    _ExpRipToEgpRuleMetric_Type()
)
expRipToEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToEgpRuleMetric.setStatus("mandatory")


class _ExpRipToEgpRuleStatus_Type(Integer32):
    """Custom type expRipToEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpRipToEgpRuleStatus_Type.__name__ = "Integer32"
_ExpRipToEgpRuleStatus_Object = MibTableColumn
expRipToEgpRuleStatus = _ExpRipToEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 5, 1, 6),
    _ExpRipToEgpRuleStatus_Type()
)
expRipToEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToEgpRuleStatus.setStatus("mandatory")
_ExpRipToOspfRuleTable_Object = MibTable
expRipToOspfRuleTable = _ExpRipToOspfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 6)
)
if mibBuilder.loadTexts:
    expRipToOspfRuleTable.setStatus("mandatory")
_ExpRipToOspfRuleEntry_Object = MibTableRow
expRipToOspfRuleEntry = _ExpRipToOspfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 6, 1)
)
expRipToOspfRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToOspfRuleNetwork"),
)
if mibBuilder.loadTexts:
    expRipToOspfRuleEntry.setStatus("mandatory")
_ExpRipToOspfRuleNetwork_Type = IpAddress
_ExpRipToOspfRuleNetwork_Object = MibTableColumn
expRipToOspfRuleNetwork = _ExpRipToOspfRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 6, 1, 1),
    _ExpRipToOspfRuleNetwork_Type()
)
expRipToOspfRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToOspfRuleNetwork.setStatus("mandatory")


class _ExpRipToOspfRuleAction_Type(Integer32):
    """Custom type expRipToOspfRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpRipToOspfRuleAction_Type.__name__ = "Integer32"
_ExpRipToOspfRuleAction_Object = MibTableColumn
expRipToOspfRuleAction = _ExpRipToOspfRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 6, 1, 2),
    _ExpRipToOspfRuleAction_Type()
)
expRipToOspfRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToOspfRuleAction.setStatus("mandatory")


class _ExpRipToOspfRuleStatus_Type(Integer32):
    """Custom type expRipToOspfRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpRipToOspfRuleStatus_Type.__name__ = "Integer32"
_ExpRipToOspfRuleStatus_Object = MibTableColumn
expRipToOspfRuleStatus = _ExpRipToOspfRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 6, 1, 3),
    _ExpRipToOspfRuleStatus_Type()
)
expRipToOspfRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToOspfRuleStatus.setStatus("mandatory")
_ExpEgpToRipRuleTable_Object = MibTable
expEgpToRipRuleTable = _ExpEgpToRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7)
)
if mibBuilder.loadTexts:
    expEgpToRipRuleTable.setStatus("mandatory")
_ExpEgpToRipRuleEntry_Object = MibTableRow
expEgpToRipRuleEntry = _ExpEgpToRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1)
)
expEgpToRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToRipRuleToIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToRipRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToRipRuleFromAs"),
)
if mibBuilder.loadTexts:
    expEgpToRipRuleEntry.setStatus("mandatory")
_ExpEgpToRipRuleToIf_Type = IpAddress
_ExpEgpToRipRuleToIf_Object = MibTableColumn
expEgpToRipRuleToIf = _ExpEgpToRipRuleToIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 1),
    _ExpEgpToRipRuleToIf_Type()
)
expEgpToRipRuleToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToRipRuleToIf.setStatus("mandatory")
_ExpEgpToRipRuleNetwork_Type = IpAddress
_ExpEgpToRipRuleNetwork_Object = MibTableColumn
expEgpToRipRuleNetwork = _ExpEgpToRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 2),
    _ExpEgpToRipRuleNetwork_Type()
)
expEgpToRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToRipRuleNetwork.setStatus("mandatory")


class _ExpEgpToRipRuleFromAs_Type(Integer32):
    """Custom type expEgpToRipRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpEgpToRipRuleFromAs_Type.__name__ = "Integer32"
_ExpEgpToRipRuleFromAs_Object = MibTableColumn
expEgpToRipRuleFromAs = _ExpEgpToRipRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 3),
    _ExpEgpToRipRuleFromAs_Type()
)
expEgpToRipRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToRipRuleFromAs.setStatus("mandatory")


class _ExpEgpToRipRuleAction_Type(Integer32):
    """Custom type expEgpToRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpEgpToRipRuleAction_Type.__name__ = "Integer32"
_ExpEgpToRipRuleAction_Object = MibTableColumn
expEgpToRipRuleAction = _ExpEgpToRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 4),
    _ExpEgpToRipRuleAction_Type()
)
expEgpToRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToRipRuleAction.setStatus("mandatory")


class _ExpEgpToRipRuleMetricAction_Type(Integer32):
    """Custom type expEgpToRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToRipRuleMetricAction_Type.__name__ = "Integer32"
_ExpEgpToRipRuleMetricAction_Object = MibTableColumn
expEgpToRipRuleMetricAction = _ExpEgpToRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 5),
    _ExpEgpToRipRuleMetricAction_Type()
)
expEgpToRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToRipRuleMetricAction.setStatus("mandatory")


class _ExpEgpToRipRuleMetric_Type(Integer32):
    """Custom type expEgpToRipRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpEgpToRipRuleMetric_Type.__name__ = "Integer32"
_ExpEgpToRipRuleMetric_Object = MibTableColumn
expEgpToRipRuleMetric = _ExpEgpToRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 6),
    _ExpEgpToRipRuleMetric_Type()
)
expEgpToRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToRipRuleMetric.setStatus("mandatory")


class _ExpEgpToRipRuleStatus_Type(Integer32):
    """Custom type expEgpToRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpEgpToRipRuleStatus_Type.__name__ = "Integer32"
_ExpEgpToRipRuleStatus_Object = MibTableColumn
expEgpToRipRuleStatus = _ExpEgpToRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 7, 1, 7),
    _ExpEgpToRipRuleStatus_Type()
)
expEgpToRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToRipRuleStatus.setStatus("mandatory")
_ExpOspfToRipRuleTable_Object = MibTable
expOspfToRipRuleTable = _ExpOspfToRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8)
)
if mibBuilder.loadTexts:
    expOspfToRipRuleTable.setStatus("mandatory")
_ExpOspfToRipRuleEntry_Object = MibTableRow
expOspfToRipRuleEntry = _ExpOspfToRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1)
)
expOspfToRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToRipRuleToIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToRipRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToRipRuleFromAs"),
)
if mibBuilder.loadTexts:
    expOspfToRipRuleEntry.setStatus("mandatory")
_ExpOspfToRipRuleToIf_Type = IpAddress
_ExpOspfToRipRuleToIf_Object = MibTableColumn
expOspfToRipRuleToIf = _ExpOspfToRipRuleToIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 1),
    _ExpOspfToRipRuleToIf_Type()
)
expOspfToRipRuleToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToRipRuleToIf.setStatus("mandatory")
_ExpOspfToRipRuleNetwork_Type = IpAddress
_ExpOspfToRipRuleNetwork_Object = MibTableColumn
expOspfToRipRuleNetwork = _ExpOspfToRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 2),
    _ExpOspfToRipRuleNetwork_Type()
)
expOspfToRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToRipRuleNetwork.setStatus("mandatory")


class _ExpOspfToRipRuleFromAs_Type(Integer32):
    """Custom type expOspfToRipRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpOspfToRipRuleFromAs_Type.__name__ = "Integer32"
_ExpOspfToRipRuleFromAs_Object = MibTableColumn
expOspfToRipRuleFromAs = _ExpOspfToRipRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 3),
    _ExpOspfToRipRuleFromAs_Type()
)
expOspfToRipRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToRipRuleFromAs.setStatus("mandatory")


class _ExpOspfToRipRuleAction_Type(Integer32):
    """Custom type expOspfToRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpOspfToRipRuleAction_Type.__name__ = "Integer32"
_ExpOspfToRipRuleAction_Object = MibTableColumn
expOspfToRipRuleAction = _ExpOspfToRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 4),
    _ExpOspfToRipRuleAction_Type()
)
expOspfToRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToRipRuleAction.setStatus("mandatory")


class _ExpOspfToRipRuleMetricAction_Type(Integer32):
    """Custom type expOspfToRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToRipRuleMetricAction_Type.__name__ = "Integer32"
_ExpOspfToRipRuleMetricAction_Object = MibTableColumn
expOspfToRipRuleMetricAction = _ExpOspfToRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 5),
    _ExpOspfToRipRuleMetricAction_Type()
)
expOspfToRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToRipRuleMetricAction.setStatus("mandatory")


class _ExpOspfToRipRuleMetric_Type(Integer32):
    """Custom type expOspfToRipRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpOspfToRipRuleMetric_Type.__name__ = "Integer32"
_ExpOspfToRipRuleMetric_Object = MibTableColumn
expOspfToRipRuleMetric = _ExpOspfToRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 6),
    _ExpOspfToRipRuleMetric_Type()
)
expOspfToRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToRipRuleMetric.setStatus("mandatory")


class _ExpOspfToRipRuleStatus_Type(Integer32):
    """Custom type expOspfToRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpOspfToRipRuleStatus_Type.__name__ = "Integer32"
_ExpOspfToRipRuleStatus_Object = MibTableColumn
expOspfToRipRuleStatus = _ExpOspfToRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 8, 1, 7),
    _ExpOspfToRipRuleStatus_Type()
)
expOspfToRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToRipRuleStatus.setStatus("mandatory")
_ExpRipToRipRuleTable_Object = MibTable
expRipToRipRuleTable = _ExpRipToRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9)
)
if mibBuilder.loadTexts:
    expRipToRipRuleTable.setStatus("mandatory")
_ExpRipToRipRuleEntry_Object = MibTableRow
expRipToRipRuleEntry = _ExpRipToRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1)
)
expRipToRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToRipRuleToIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToRipRuleNetwork"),
)
if mibBuilder.loadTexts:
    expRipToRipRuleEntry.setStatus("mandatory")
_ExpRipToRipRuleToIf_Type = IpAddress
_ExpRipToRipRuleToIf_Object = MibTableColumn
expRipToRipRuleToIf = _ExpRipToRipRuleToIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 1),
    _ExpRipToRipRuleToIf_Type()
)
expRipToRipRuleToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToRipRuleToIf.setStatus("mandatory")
_ExpRipToRipRuleNetwork_Type = IpAddress
_ExpRipToRipRuleNetwork_Object = MibTableColumn
expRipToRipRuleNetwork = _ExpRipToRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 2),
    _ExpRipToRipRuleNetwork_Type()
)
expRipToRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToRipRuleNetwork.setStatus("mandatory")


class _ExpRipToRipRuleAction_Type(Integer32):
    """Custom type expRipToRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpRipToRipRuleAction_Type.__name__ = "Integer32"
_ExpRipToRipRuleAction_Object = MibTableColumn
expRipToRipRuleAction = _ExpRipToRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 3),
    _ExpRipToRipRuleAction_Type()
)
expRipToRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToRipRuleAction.setStatus("mandatory")


class _ExpRipToRipRuleMetricAction_Type(Integer32):
    """Custom type expRipToRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToRipRuleMetricAction_Type.__name__ = "Integer32"
_ExpRipToRipRuleMetricAction_Object = MibTableColumn
expRipToRipRuleMetricAction = _ExpRipToRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 4),
    _ExpRipToRipRuleMetricAction_Type()
)
expRipToRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToRipRuleMetricAction.setStatus("mandatory")


class _ExpRipToRipRuleMetric_Type(Integer32):
    """Custom type expRipToRipRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpRipToRipRuleMetric_Type.__name__ = "Integer32"
_ExpRipToRipRuleMetric_Object = MibTableColumn
expRipToRipRuleMetric = _ExpRipToRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 5),
    _ExpRipToRipRuleMetric_Type()
)
expRipToRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToRipRuleMetric.setStatus("mandatory")


class _ExpRipToRipRuleStatus_Type(Integer32):
    """Custom type expRipToRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpRipToRipRuleStatus_Type.__name__ = "Integer32"
_ExpRipToRipRuleStatus_Object = MibTableColumn
expRipToRipRuleStatus = _ExpRipToRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 9, 1, 6),
    _ExpRipToRipRuleStatus_Type()
)
expRipToRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToRipRuleStatus.setStatus("mandatory")
_ExpStaticToRipRuleTable_Object = MibTable
expStaticToRipRuleTable = _ExpStaticToRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10)
)
if mibBuilder.loadTexts:
    expStaticToRipRuleTable.setStatus("mandatory")
_ExpStaticToRipRuleEntry_Object = MibTableRow
expStaticToRipRuleEntry = _ExpStaticToRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1)
)
expStaticToRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expStaticToRipRuleToIf"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expStaticToRipRuleNetwork"),
)
if mibBuilder.loadTexts:
    expStaticToRipRuleEntry.setStatus("mandatory")
_ExpStaticToRipRuleToIf_Type = IpAddress
_ExpStaticToRipRuleToIf_Object = MibTableColumn
expStaticToRipRuleToIf = _ExpStaticToRipRuleToIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 1),
    _ExpStaticToRipRuleToIf_Type()
)
expStaticToRipRuleToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expStaticToRipRuleToIf.setStatus("mandatory")
_ExpStaticToRipRuleNetwork_Type = IpAddress
_ExpStaticToRipRuleNetwork_Object = MibTableColumn
expStaticToRipRuleNetwork = _ExpStaticToRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 2),
    _ExpStaticToRipRuleNetwork_Type()
)
expStaticToRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expStaticToRipRuleNetwork.setStatus("mandatory")


class _ExpStaticToRipRuleAction_Type(Integer32):
    """Custom type expStaticToRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpStaticToRipRuleAction_Type.__name__ = "Integer32"
_ExpStaticToRipRuleAction_Object = MibTableColumn
expStaticToRipRuleAction = _ExpStaticToRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 3),
    _ExpStaticToRipRuleAction_Type()
)
expStaticToRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToRipRuleAction.setStatus("mandatory")


class _ExpStaticToRipRuleMetricAction_Type(Integer32):
    """Custom type expStaticToRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToRipRuleMetricAction_Type.__name__ = "Integer32"
_ExpStaticToRipRuleMetricAction_Object = MibTableColumn
expStaticToRipRuleMetricAction = _ExpStaticToRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 4),
    _ExpStaticToRipRuleMetricAction_Type()
)
expStaticToRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToRipRuleMetricAction.setStatus("mandatory")


class _ExpStaticToRipRuleMetric_Type(Integer32):
    """Custom type expStaticToRipRuleMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ExpStaticToRipRuleMetric_Type.__name__ = "Integer32"
_ExpStaticToRipRuleMetric_Object = MibTableColumn
expStaticToRipRuleMetric = _ExpStaticToRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 5),
    _ExpStaticToRipRuleMetric_Type()
)
expStaticToRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToRipRuleMetric.setStatus("mandatory")


class _ExpStaticToRipRuleStatus_Type(Integer32):
    """Custom type expStaticToRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpStaticToRipRuleStatus_Type.__name__ = "Integer32"
_ExpStaticToRipRuleStatus_Object = MibTableColumn
expStaticToRipRuleStatus = _ExpStaticToRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 10, 1, 6),
    _ExpStaticToRipRuleStatus_Type()
)
expStaticToRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToRipRuleStatus.setStatus("mandatory")
_ExpIsisToEgpRuleTable_Object = MibTable
expIsisToEgpRuleTable = _ExpIsisToEgpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11)
)
if mibBuilder.loadTexts:
    expIsisToEgpRuleTable.setStatus("mandatory")
_ExpIsisToEgpRuleEntry_Object = MibTableRow
expIsisToEgpRuleEntry = _ExpIsisToEgpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1)
)
expIsisToEgpRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expIsisToEgpRuleToAs"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expIsisToEgpRuleNetwork"),
)
if mibBuilder.loadTexts:
    expIsisToEgpRuleEntry.setStatus("mandatory")


class _ExpIsisToEgpRuleToAs_Type(Integer32):
    """Custom type expIsisToEgpRuleToAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpIsisToEgpRuleToAs_Type.__name__ = "Integer32"
_ExpIsisToEgpRuleToAs_Object = MibTableColumn
expIsisToEgpRuleToAs = _ExpIsisToEgpRuleToAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 1),
    _ExpIsisToEgpRuleToAs_Type()
)
expIsisToEgpRuleToAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expIsisToEgpRuleToAs.setStatus("mandatory")
_ExpIsisToEgpRuleNetwork_Type = IpAddress
_ExpIsisToEgpRuleNetwork_Object = MibTableColumn
expIsisToEgpRuleNetwork = _ExpIsisToEgpRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 2),
    _ExpIsisToEgpRuleNetwork_Type()
)
expIsisToEgpRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expIsisToEgpRuleNetwork.setStatus("mandatory")


class _ExpIsisToEgpRuleAction_Type(Integer32):
    """Custom type expIsisToEgpRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpIsisToEgpRuleAction_Type.__name__ = "Integer32"
_ExpIsisToEgpRuleAction_Object = MibTableColumn
expIsisToEgpRuleAction = _ExpIsisToEgpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 3),
    _ExpIsisToEgpRuleAction_Type()
)
expIsisToEgpRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToEgpRuleAction.setStatus("mandatory")


class _ExpIsisToEgpRuleMetricAction_Type(Integer32):
    """Custom type expIsisToEgpRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpIsisToEgpRuleMetricAction_Type.__name__ = "Integer32"
_ExpIsisToEgpRuleMetricAction_Object = MibTableColumn
expIsisToEgpRuleMetricAction = _ExpIsisToEgpRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 4),
    _ExpIsisToEgpRuleMetricAction_Type()
)
expIsisToEgpRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToEgpRuleMetricAction.setStatus("mandatory")


class _ExpIsisToEgpRuleMetric_Type(Integer32):
    """Custom type expIsisToEgpRuleMetric based on Integer32"""
    defaultValue = 0


_ExpIsisToEgpRuleMetric_Object = MibTableColumn
expIsisToEgpRuleMetric = _ExpIsisToEgpRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 5),
    _ExpIsisToEgpRuleMetric_Type()
)
expIsisToEgpRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToEgpRuleMetric.setStatus("mandatory")


class _ExpIsisToEgpRuleStatus_Type(Integer32):
    """Custom type expIsisToEgpRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpIsisToEgpRuleStatus_Type.__name__ = "Integer32"
_ExpIsisToEgpRuleStatus_Object = MibTableColumn
expIsisToEgpRuleStatus = _ExpIsisToEgpRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 11, 1, 6),
    _ExpIsisToEgpRuleStatus_Type()
)
expIsisToEgpRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToEgpRuleStatus.setStatus("mandatory")
_ExpIsisToOspfRuleTable_Object = MibTable
expIsisToOspfRuleTable = _ExpIsisToOspfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 12)
)
if mibBuilder.loadTexts:
    expIsisToOspfRuleTable.setStatus("mandatory")
_ExpIsisToOspfRuleEntry_Object = MibTableRow
expIsisToOspfRuleEntry = _ExpIsisToOspfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 12, 1)
)
expIsisToOspfRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expIsisToOspfRuleNetwork"),
)
if mibBuilder.loadTexts:
    expIsisToOspfRuleEntry.setStatus("mandatory")
_ExpIsisToOspfRuleNetwork_Type = IpAddress
_ExpIsisToOspfRuleNetwork_Object = MibTableColumn
expIsisToOspfRuleNetwork = _ExpIsisToOspfRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 12, 1, 1),
    _ExpIsisToOspfRuleNetwork_Type()
)
expIsisToOspfRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expIsisToOspfRuleNetwork.setStatus("mandatory")


class _ExpIsisToOspfRuleAction_Type(Integer32):
    """Custom type expIsisToOspfRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpIsisToOspfRuleAction_Type.__name__ = "Integer32"
_ExpIsisToOspfRuleAction_Object = MibTableColumn
expIsisToOspfRuleAction = _ExpIsisToOspfRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 12, 1, 2),
    _ExpIsisToOspfRuleAction_Type()
)
expIsisToOspfRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToOspfRuleAction.setStatus("mandatory")


class _ExpIsisToOspfRuleStatus_Type(Integer32):
    """Custom type expIsisToOspfRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpIsisToOspfRuleStatus_Type.__name__ = "Integer32"
_ExpIsisToOspfRuleStatus_Object = MibTableColumn
expIsisToOspfRuleStatus = _ExpIsisToOspfRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 12, 1, 3),
    _ExpIsisToOspfRuleStatus_Type()
)
expIsisToOspfRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToOspfRuleStatus.setStatus("mandatory")
_ExpIsisToRipRuleTable_Object = MibTable
expIsisToRipRuleTable = _ExpIsisToRipRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13)
)
if mibBuilder.loadTexts:
    expIsisToRipRuleTable.setStatus("mandatory")
_ExpIsisToRipRuleEntry_Object = MibTableRow
expIsisToRipRuleEntry = _ExpIsisToRipRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1)
)
expIsisToRipRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expIsisToRipRuleNetwork"),
)
if mibBuilder.loadTexts:
    expIsisToRipRuleEntry.setStatus("mandatory")
_ExpIsisToRipRuleToIf_Type = IpAddress
_ExpIsisToRipRuleToIf_Object = MibTableColumn
expIsisToRipRuleToIf = _ExpIsisToRipRuleToIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 1),
    _ExpIsisToRipRuleToIf_Type()
)
expIsisToRipRuleToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expIsisToRipRuleToIf.setStatus("mandatory")
_ExpIsisToRipRuleNetwork_Type = IpAddress
_ExpIsisToRipRuleNetwork_Object = MibTableColumn
expIsisToRipRuleNetwork = _ExpIsisToRipRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 2),
    _ExpIsisToRipRuleNetwork_Type()
)
expIsisToRipRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expIsisToRipRuleNetwork.setStatus("mandatory")


class _ExpIsisToRipRuleAction_Type(Integer32):
    """Custom type expIsisToRipRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpIsisToRipRuleAction_Type.__name__ = "Integer32"
_ExpIsisToRipRuleAction_Object = MibTableColumn
expIsisToRipRuleAction = _ExpIsisToRipRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 3),
    _ExpIsisToRipRuleAction_Type()
)
expIsisToRipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToRipRuleAction.setStatus("mandatory")


class _ExpIsisToRipRuleMetricAction_Type(Integer32):
    """Custom type expIsisToRipRuleMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpIsisToRipRuleMetricAction_Type.__name__ = "Integer32"
_ExpIsisToRipRuleMetricAction_Object = MibTableColumn
expIsisToRipRuleMetricAction = _ExpIsisToRipRuleMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 4),
    _ExpIsisToRipRuleMetricAction_Type()
)
expIsisToRipRuleMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToRipRuleMetricAction.setStatus("mandatory")


class _ExpIsisToRipRuleMetric_Type(Integer32):
    """Custom type expIsisToRipRuleMetric based on Integer32"""
    defaultValue = 0


_ExpIsisToRipRuleMetric_Object = MibTableColumn
expIsisToRipRuleMetric = _ExpIsisToRipRuleMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 5),
    _ExpIsisToRipRuleMetric_Type()
)
expIsisToRipRuleMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToRipRuleMetric.setStatus("mandatory")


class _ExpIsisToRipRuleStatus_Type(Integer32):
    """Custom type expIsisToRipRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpIsisToRipRuleStatus_Type.__name__ = "Integer32"
_ExpIsisToRipRuleStatus_Object = MibTableColumn
expIsisToRipRuleStatus = _ExpIsisToRipRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 13, 1, 6),
    _ExpIsisToRipRuleStatus_Type()
)
expIsisToRipRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expIsisToRipRuleStatus.setStatus("mandatory")
_ExpEgpToIsisRuleTable_Object = MibTable
expEgpToIsisRuleTable = _ExpEgpToIsisRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14)
)
if mibBuilder.loadTexts:
    expEgpToIsisRuleTable.setStatus("mandatory")
_ExpEgpToIsisRuleEntry_Object = MibTableRow
expEgpToIsisRuleEntry = _ExpEgpToIsisRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1)
)
expEgpToIsisRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToIsisRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expEgpToIsisRuleFromAs"),
)
if mibBuilder.loadTexts:
    expEgpToIsisRuleEntry.setStatus("mandatory")
_ExpEgpToIsisRuleNetwork_Type = IpAddress
_ExpEgpToIsisRuleNetwork_Object = MibTableColumn
expEgpToIsisRuleNetwork = _ExpEgpToIsisRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 1),
    _ExpEgpToIsisRuleNetwork_Type()
)
expEgpToIsisRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToIsisRuleNetwork.setStatus("mandatory")


class _ExpEgpToIsisRuleFromAs_Type(Integer32):
    """Custom type expEgpToIsisRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpEgpToIsisRuleFromAs_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleFromAs_Object = MibTableColumn
expEgpToIsisRuleFromAs = _ExpEgpToIsisRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 2),
    _ExpEgpToIsisRuleFromAs_Type()
)
expEgpToIsisRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expEgpToIsisRuleFromAs.setStatus("mandatory")


class _ExpEgpToIsisRuleAction_Type(Integer32):
    """Custom type expEgpToIsisRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpEgpToIsisRuleAction_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleAction_Object = MibTableColumn
expEgpToIsisRuleAction = _ExpEgpToIsisRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 3),
    _ExpEgpToIsisRuleAction_Type()
)
expEgpToIsisRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleAction.setStatus("mandatory")


class _ExpEgpToIsisRuleMetricType_Type(Integer32):
    """Custom type expEgpToIsisRuleMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ExpEgpToIsisRuleMetricType_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleMetricType_Object = MibTableColumn
expEgpToIsisRuleMetricType = _ExpEgpToIsisRuleMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 4),
    _ExpEgpToIsisRuleMetricType_Type()
)
expEgpToIsisRuleMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleMetricType.setStatus("mandatory")


class _ExpEgpToIsisRuleDefaultMetricAction_Type(Integer32):
    """Custom type expEgpToIsisRuleDefaultMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToIsisRuleDefaultMetricAction_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleDefaultMetricAction_Object = MibTableColumn
expEgpToIsisRuleDefaultMetricAction = _ExpEgpToIsisRuleDefaultMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 5),
    _ExpEgpToIsisRuleDefaultMetricAction_Type()
)
expEgpToIsisRuleDefaultMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleDefaultMetricAction.setStatus("mandatory")


class _ExpEgpToIsisRuleDefaultMetric_Type(Integer32):
    """Custom type expEgpToIsisRuleDefaultMetric based on Integer32"""
    defaultValue = 1


_ExpEgpToIsisRuleDefaultMetric_Object = MibTableColumn
expEgpToIsisRuleDefaultMetric = _ExpEgpToIsisRuleDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 6),
    _ExpEgpToIsisRuleDefaultMetric_Type()
)
expEgpToIsisRuleDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleDefaultMetric.setStatus("mandatory")


class _ExpEgpToIsisRuleDelayMetricAction_Type(Integer32):
    """Custom type expEgpToIsisRuleDelayMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToIsisRuleDelayMetricAction_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleDelayMetricAction_Object = MibTableColumn
expEgpToIsisRuleDelayMetricAction = _ExpEgpToIsisRuleDelayMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 7),
    _ExpEgpToIsisRuleDelayMetricAction_Type()
)
expEgpToIsisRuleDelayMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleDelayMetricAction.setStatus("mandatory")


class _ExpEgpToIsisRuleDelayMetric_Type(Integer32):
    """Custom type expEgpToIsisRuleDelayMetric based on Integer32"""
    defaultValue = 0


_ExpEgpToIsisRuleDelayMetric_Object = MibTableColumn
expEgpToIsisRuleDelayMetric = _ExpEgpToIsisRuleDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 8),
    _ExpEgpToIsisRuleDelayMetric_Type()
)
expEgpToIsisRuleDelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleDelayMetric.setStatus("mandatory")


class _ExpEgpToIsisRuleErrorMetricAction_Type(Integer32):
    """Custom type expEgpToIsisRuleErrorMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToIsisRuleErrorMetricAction_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleErrorMetricAction_Object = MibTableColumn
expEgpToIsisRuleErrorMetricAction = _ExpEgpToIsisRuleErrorMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 9),
    _ExpEgpToIsisRuleErrorMetricAction_Type()
)
expEgpToIsisRuleErrorMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleErrorMetricAction.setStatus("mandatory")


class _ExpEgpToIsisRuleErrorMetric_Type(Integer32):
    """Custom type expEgpToIsisRuleErrorMetric based on Integer32"""
    defaultValue = 0


_ExpEgpToIsisRuleErrorMetric_Object = MibTableColumn
expEgpToIsisRuleErrorMetric = _ExpEgpToIsisRuleErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 10),
    _ExpEgpToIsisRuleErrorMetric_Type()
)
expEgpToIsisRuleErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleErrorMetric.setStatus("mandatory")


class _ExpEgpToIsisRuleExpenseMetricAction_Type(Integer32):
    """Custom type expEgpToIsisRuleExpenseMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpEgpToIsisRuleExpenseMetricAction_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleExpenseMetricAction_Object = MibTableColumn
expEgpToIsisRuleExpenseMetricAction = _ExpEgpToIsisRuleExpenseMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 11),
    _ExpEgpToIsisRuleExpenseMetricAction_Type()
)
expEgpToIsisRuleExpenseMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleExpenseMetricAction.setStatus("mandatory")


class _ExpEgpToIsisRuleExpenseMetric_Type(Integer32):
    """Custom type expEgpToIsisRuleExpenseMetric based on Integer32"""
    defaultValue = 0


_ExpEgpToIsisRuleExpenseMetric_Object = MibTableColumn
expEgpToIsisRuleExpenseMetric = _ExpEgpToIsisRuleExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 12),
    _ExpEgpToIsisRuleExpenseMetric_Type()
)
expEgpToIsisRuleExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleExpenseMetric.setStatus("mandatory")


class _ExpEgpToIsisRuleStatus_Type(Integer32):
    """Custom type expEgpToIsisRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpEgpToIsisRuleStatus_Type.__name__ = "Integer32"
_ExpEgpToIsisRuleStatus_Object = MibTableColumn
expEgpToIsisRuleStatus = _ExpEgpToIsisRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 14, 1, 13),
    _ExpEgpToIsisRuleStatus_Type()
)
expEgpToIsisRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expEgpToIsisRuleStatus.setStatus("mandatory")
_ExpOspfToIsisRuleTable_Object = MibTable
expOspfToIsisRuleTable = _ExpOspfToIsisRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15)
)
if mibBuilder.loadTexts:
    expOspfToIsisRuleTable.setStatus("mandatory")
_ExpOspfToIsisRuleEntry_Object = MibTableRow
expOspfToIsisRuleEntry = _ExpOspfToIsisRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1)
)
expOspfToIsisRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToIsisRuleNetwork"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "expOspfToIsisRuleFromAs"),
)
if mibBuilder.loadTexts:
    expOspfToIsisRuleEntry.setStatus("mandatory")
_ExpOspfToIsisRuleNetwork_Type = IpAddress
_ExpOspfToIsisRuleNetwork_Object = MibTableColumn
expOspfToIsisRuleNetwork = _ExpOspfToIsisRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 1),
    _ExpOspfToIsisRuleNetwork_Type()
)
expOspfToIsisRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToIsisRuleNetwork.setStatus("mandatory")


class _ExpOspfToIsisRuleFromAs_Type(Integer32):
    """Custom type expOspfToIsisRuleFromAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpOspfToIsisRuleFromAs_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleFromAs_Object = MibTableColumn
expOspfToIsisRuleFromAs = _ExpOspfToIsisRuleFromAs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 2),
    _ExpOspfToIsisRuleFromAs_Type()
)
expOspfToIsisRuleFromAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expOspfToIsisRuleFromAs.setStatus("mandatory")


class _ExpOspfToIsisRuleAction_Type(Integer32):
    """Custom type expOspfToIsisRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpOspfToIsisRuleAction_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleAction_Object = MibTableColumn
expOspfToIsisRuleAction = _ExpOspfToIsisRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 3),
    _ExpOspfToIsisRuleAction_Type()
)
expOspfToIsisRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleAction.setStatus("mandatory")


class _ExpOspfToIsisRuleMetricType_Type(Integer32):
    """Custom type expOspfToIsisRuleMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ExpOspfToIsisRuleMetricType_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleMetricType_Object = MibTableColumn
expOspfToIsisRuleMetricType = _ExpOspfToIsisRuleMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 4),
    _ExpOspfToIsisRuleMetricType_Type()
)
expOspfToIsisRuleMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleMetricType.setStatus("mandatory")


class _ExpOspfToIsisRuleDefaultMetricAction_Type(Integer32):
    """Custom type expOspfToIsisRuleDefaultMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToIsisRuleDefaultMetricAction_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleDefaultMetricAction_Object = MibTableColumn
expOspfToIsisRuleDefaultMetricAction = _ExpOspfToIsisRuleDefaultMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 5),
    _ExpOspfToIsisRuleDefaultMetricAction_Type()
)
expOspfToIsisRuleDefaultMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleDefaultMetricAction.setStatus("mandatory")


class _ExpOspfToIsisRuleDefaultMetric_Type(Integer32):
    """Custom type expOspfToIsisRuleDefaultMetric based on Integer32"""
    defaultValue = 1


_ExpOspfToIsisRuleDefaultMetric_Object = MibTableColumn
expOspfToIsisRuleDefaultMetric = _ExpOspfToIsisRuleDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 6),
    _ExpOspfToIsisRuleDefaultMetric_Type()
)
expOspfToIsisRuleDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleDefaultMetric.setStatus("mandatory")


class _ExpOspfToIsisRuleDelayMetricAction_Type(Integer32):
    """Custom type expOspfToIsisRuleDelayMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToIsisRuleDelayMetricAction_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleDelayMetricAction_Object = MibTableColumn
expOspfToIsisRuleDelayMetricAction = _ExpOspfToIsisRuleDelayMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 7),
    _ExpOspfToIsisRuleDelayMetricAction_Type()
)
expOspfToIsisRuleDelayMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleDelayMetricAction.setStatus("mandatory")


class _ExpOspfToIsisRuleDelayMetric_Type(Integer32):
    """Custom type expOspfToIsisRuleDelayMetric based on Integer32"""
    defaultValue = 0


_ExpOspfToIsisRuleDelayMetric_Object = MibTableColumn
expOspfToIsisRuleDelayMetric = _ExpOspfToIsisRuleDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 8),
    _ExpOspfToIsisRuleDelayMetric_Type()
)
expOspfToIsisRuleDelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleDelayMetric.setStatus("mandatory")


class _ExpOspfToIsisRuleErrorMetricAction_Type(Integer32):
    """Custom type expOspfToIsisRuleErrorMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToIsisRuleErrorMetricAction_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleErrorMetricAction_Object = MibTableColumn
expOspfToIsisRuleErrorMetricAction = _ExpOspfToIsisRuleErrorMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 9),
    _ExpOspfToIsisRuleErrorMetricAction_Type()
)
expOspfToIsisRuleErrorMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleErrorMetricAction.setStatus("mandatory")


class _ExpOspfToIsisRuleErrorMetric_Type(Integer32):
    """Custom type expOspfToIsisRuleErrorMetric based on Integer32"""
    defaultValue = 0


_ExpOspfToIsisRuleErrorMetric_Object = MibTableColumn
expOspfToIsisRuleErrorMetric = _ExpOspfToIsisRuleErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 10),
    _ExpOspfToIsisRuleErrorMetric_Type()
)
expOspfToIsisRuleErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleErrorMetric.setStatus("mandatory")


class _ExpOspfToIsisRuleExpenseMetricAction_Type(Integer32):
    """Custom type expOspfToIsisRuleExpenseMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpOspfToIsisRuleExpenseMetricAction_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleExpenseMetricAction_Object = MibTableColumn
expOspfToIsisRuleExpenseMetricAction = _ExpOspfToIsisRuleExpenseMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 11),
    _ExpOspfToIsisRuleExpenseMetricAction_Type()
)
expOspfToIsisRuleExpenseMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleExpenseMetricAction.setStatus("mandatory")


class _ExpOspfToIsisRuleExpenseMetric_Type(Integer32):
    """Custom type expOspfToIsisRuleExpenseMetric based on Integer32"""
    defaultValue = 0


_ExpOspfToIsisRuleExpenseMetric_Object = MibTableColumn
expOspfToIsisRuleExpenseMetric = _ExpOspfToIsisRuleExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 12),
    _ExpOspfToIsisRuleExpenseMetric_Type()
)
expOspfToIsisRuleExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleExpenseMetric.setStatus("mandatory")


class _ExpOspfToIsisRuleStatus_Type(Integer32):
    """Custom type expOspfToIsisRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpOspfToIsisRuleStatus_Type.__name__ = "Integer32"
_ExpOspfToIsisRuleStatus_Object = MibTableColumn
expOspfToIsisRuleStatus = _ExpOspfToIsisRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 15, 1, 13),
    _ExpOspfToIsisRuleStatus_Type()
)
expOspfToIsisRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expOspfToIsisRuleStatus.setStatus("mandatory")
_ExpRipToIsisRuleTable_Object = MibTable
expRipToIsisRuleTable = _ExpRipToIsisRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16)
)
if mibBuilder.loadTexts:
    expRipToIsisRuleTable.setStatus("mandatory")
_ExpRipToIsisRuleEntry_Object = MibTableRow
expRipToIsisRuleEntry = _ExpRipToIsisRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1)
)
expRipToIsisRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expRipToIsisRuleNetwork"),
)
if mibBuilder.loadTexts:
    expRipToIsisRuleEntry.setStatus("mandatory")
_ExpRipToIsisRuleNetwork_Type = IpAddress
_ExpRipToIsisRuleNetwork_Object = MibTableColumn
expRipToIsisRuleNetwork = _ExpRipToIsisRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 1),
    _ExpRipToIsisRuleNetwork_Type()
)
expRipToIsisRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expRipToIsisRuleNetwork.setStatus("mandatory")


class _ExpRipToIsisRuleAction_Type(Integer32):
    """Custom type expRipToIsisRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpRipToIsisRuleAction_Type.__name__ = "Integer32"
_ExpRipToIsisRuleAction_Object = MibTableColumn
expRipToIsisRuleAction = _ExpRipToIsisRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 2),
    _ExpRipToIsisRuleAction_Type()
)
expRipToIsisRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleAction.setStatus("mandatory")


class _ExpRipToIsisRuleMetricType_Type(Integer32):
    """Custom type expRipToIsisRuleMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ExpRipToIsisRuleMetricType_Type.__name__ = "Integer32"
_ExpRipToIsisRuleMetricType_Object = MibTableColumn
expRipToIsisRuleMetricType = _ExpRipToIsisRuleMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 3),
    _ExpRipToIsisRuleMetricType_Type()
)
expRipToIsisRuleMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleMetricType.setStatus("mandatory")


class _ExpRipToIsisRuleDefaultMetricAction_Type(Integer32):
    """Custom type expRipToIsisRuleDefaultMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToIsisRuleDefaultMetricAction_Type.__name__ = "Integer32"
_ExpRipToIsisRuleDefaultMetricAction_Object = MibTableColumn
expRipToIsisRuleDefaultMetricAction = _ExpRipToIsisRuleDefaultMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 4),
    _ExpRipToIsisRuleDefaultMetricAction_Type()
)
expRipToIsisRuleDefaultMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleDefaultMetricAction.setStatus("mandatory")


class _ExpRipToIsisRuleDefaultMetric_Type(Integer32):
    """Custom type expRipToIsisRuleDefaultMetric based on Integer32"""
    defaultValue = 1


_ExpRipToIsisRuleDefaultMetric_Object = MibTableColumn
expRipToIsisRuleDefaultMetric = _ExpRipToIsisRuleDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 5),
    _ExpRipToIsisRuleDefaultMetric_Type()
)
expRipToIsisRuleDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleDefaultMetric.setStatus("mandatory")


class _ExpRipToIsisRuleDelayMetricAction_Type(Integer32):
    """Custom type expRipToIsisRuleDelayMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToIsisRuleDelayMetricAction_Type.__name__ = "Integer32"
_ExpRipToIsisRuleDelayMetricAction_Object = MibTableColumn
expRipToIsisRuleDelayMetricAction = _ExpRipToIsisRuleDelayMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 6),
    _ExpRipToIsisRuleDelayMetricAction_Type()
)
expRipToIsisRuleDelayMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleDelayMetricAction.setStatus("mandatory")


class _ExpRipToIsisRuleDelayMetric_Type(Integer32):
    """Custom type expRipToIsisRuleDelayMetric based on Integer32"""
    defaultValue = 0


_ExpRipToIsisRuleDelayMetric_Object = MibTableColumn
expRipToIsisRuleDelayMetric = _ExpRipToIsisRuleDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 7),
    _ExpRipToIsisRuleDelayMetric_Type()
)
expRipToIsisRuleDelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleDelayMetric.setStatus("mandatory")


class _ExpRipToIsisRuleErrorMetricAction_Type(Integer32):
    """Custom type expRipToIsisRuleErrorMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToIsisRuleErrorMetricAction_Type.__name__ = "Integer32"
_ExpRipToIsisRuleErrorMetricAction_Object = MibTableColumn
expRipToIsisRuleErrorMetricAction = _ExpRipToIsisRuleErrorMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 8),
    _ExpRipToIsisRuleErrorMetricAction_Type()
)
expRipToIsisRuleErrorMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleErrorMetricAction.setStatus("mandatory")


class _ExpRipToIsisRuleErrorMetric_Type(Integer32):
    """Custom type expRipToIsisRuleErrorMetric based on Integer32"""
    defaultValue = 0


_ExpRipToIsisRuleErrorMetric_Object = MibTableColumn
expRipToIsisRuleErrorMetric = _ExpRipToIsisRuleErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 9),
    _ExpRipToIsisRuleErrorMetric_Type()
)
expRipToIsisRuleErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleErrorMetric.setStatus("mandatory")


class _ExpRipToIsisRuleExpenseMetricAction_Type(Integer32):
    """Custom type expRipToIsisRuleExpenseMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpRipToIsisRuleExpenseMetricAction_Type.__name__ = "Integer32"
_ExpRipToIsisRuleExpenseMetricAction_Object = MibTableColumn
expRipToIsisRuleExpenseMetricAction = _ExpRipToIsisRuleExpenseMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 10),
    _ExpRipToIsisRuleExpenseMetricAction_Type()
)
expRipToIsisRuleExpenseMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleExpenseMetricAction.setStatus("mandatory")


class _ExpRipToIsisRuleExpenseMetric_Type(Integer32):
    """Custom type expRipToIsisRuleExpenseMetric based on Integer32"""
    defaultValue = 0


_ExpRipToIsisRuleExpenseMetric_Object = MibTableColumn
expRipToIsisRuleExpenseMetric = _ExpRipToIsisRuleExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 11),
    _ExpRipToIsisRuleExpenseMetric_Type()
)
expRipToIsisRuleExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleExpenseMetric.setStatus("mandatory")


class _ExpRipToIsisRuleStatus_Type(Integer32):
    """Custom type expRipToIsisRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpRipToIsisRuleStatus_Type.__name__ = "Integer32"
_ExpRipToIsisRuleStatus_Object = MibTableColumn
expRipToIsisRuleStatus = _ExpRipToIsisRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 16, 1, 12),
    _ExpRipToIsisRuleStatus_Type()
)
expRipToIsisRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expRipToIsisRuleStatus.setStatus("mandatory")
_ExpStaticToIsisRuleTable_Object = MibTable
expStaticToIsisRuleTable = _ExpStaticToIsisRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17)
)
if mibBuilder.loadTexts:
    expStaticToIsisRuleTable.setStatus("mandatory")
_ExpStaticToIsisRuleEntry_Object = MibTableRow
expStaticToIsisRuleEntry = _ExpStaticToIsisRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1)
)
expStaticToIsisRuleEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "expStaticToIsisRuleNetwork"),
)
if mibBuilder.loadTexts:
    expStaticToIsisRuleEntry.setStatus("mandatory")
_ExpStaticToIsisRuleNetwork_Type = IpAddress
_ExpStaticToIsisRuleNetwork_Object = MibTableColumn
expStaticToIsisRuleNetwork = _ExpStaticToIsisRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 1),
    _ExpStaticToIsisRuleNetwork_Type()
)
expStaticToIsisRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expStaticToIsisRuleNetwork.setStatus("mandatory")


class _ExpStaticToIsisRuleAction_Type(Integer32):
    """Custom type expStaticToIsisRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ExpStaticToIsisRuleAction_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleAction_Object = MibTableColumn
expStaticToIsisRuleAction = _ExpStaticToIsisRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 2),
    _ExpStaticToIsisRuleAction_Type()
)
expStaticToIsisRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleAction.setStatus("mandatory")


class _ExpStaticToIsisRuleMetricType_Type(Integer32):
    """Custom type expStaticToIsisRuleMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_ExpStaticToIsisRuleMetricType_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleMetricType_Object = MibTableColumn
expStaticToIsisRuleMetricType = _ExpStaticToIsisRuleMetricType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 3),
    _ExpStaticToIsisRuleMetricType_Type()
)
expStaticToIsisRuleMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleMetricType.setStatus("mandatory")


class _ExpStaticToIsisRuleDefaultMetricAction_Type(Integer32):
    """Custom type expStaticToIsisRuleDefaultMetricAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToIsisRuleDefaultMetricAction_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleDefaultMetricAction_Object = MibTableColumn
expStaticToIsisRuleDefaultMetricAction = _ExpStaticToIsisRuleDefaultMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 4),
    _ExpStaticToIsisRuleDefaultMetricAction_Type()
)
expStaticToIsisRuleDefaultMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleDefaultMetricAction.setStatus("mandatory")


class _ExpStaticToIsisRuleDefaultMetric_Type(Integer32):
    """Custom type expStaticToIsisRuleDefaultMetric based on Integer32"""
    defaultValue = 1


_ExpStaticToIsisRuleDefaultMetric_Object = MibTableColumn
expStaticToIsisRuleDefaultMetric = _ExpStaticToIsisRuleDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 5),
    _ExpStaticToIsisRuleDefaultMetric_Type()
)
expStaticToIsisRuleDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleDefaultMetric.setStatus("mandatory")


class _ExpStaticToIsisRuleDelayMetricAction_Type(Integer32):
    """Custom type expStaticToIsisRuleDelayMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToIsisRuleDelayMetricAction_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleDelayMetricAction_Object = MibTableColumn
expStaticToIsisRuleDelayMetricAction = _ExpStaticToIsisRuleDelayMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 6),
    _ExpStaticToIsisRuleDelayMetricAction_Type()
)
expStaticToIsisRuleDelayMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleDelayMetricAction.setStatus("mandatory")


class _ExpStaticToIsisRuleDelayMetric_Type(Integer32):
    """Custom type expStaticToIsisRuleDelayMetric based on Integer32"""
    defaultValue = 0


_ExpStaticToIsisRuleDelayMetric_Object = MibTableColumn
expStaticToIsisRuleDelayMetric = _ExpStaticToIsisRuleDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 7),
    _ExpStaticToIsisRuleDelayMetric_Type()
)
expStaticToIsisRuleDelayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleDelayMetric.setStatus("mandatory")


class _ExpStaticToIsisRuleErrorMetricAction_Type(Integer32):
    """Custom type expStaticToIsisRuleErrorMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToIsisRuleErrorMetricAction_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleErrorMetricAction_Object = MibTableColumn
expStaticToIsisRuleErrorMetricAction = _ExpStaticToIsisRuleErrorMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 8),
    _ExpStaticToIsisRuleErrorMetricAction_Type()
)
expStaticToIsisRuleErrorMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleErrorMetricAction.setStatus("mandatory")


class _ExpStaticToIsisRuleErrorMetric_Type(Integer32):
    """Custom type expStaticToIsisRuleErrorMetric based on Integer32"""
    defaultValue = 0


_ExpStaticToIsisRuleErrorMetric_Object = MibTableColumn
expStaticToIsisRuleErrorMetric = _ExpStaticToIsisRuleErrorMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 9),
    _ExpStaticToIsisRuleErrorMetric_Type()
)
expStaticToIsisRuleErrorMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleErrorMetric.setStatus("mandatory")


class _ExpStaticToIsisRuleExpenseMetricAction_Type(Integer32):
    """Custom type expStaticToIsisRuleExpenseMetricAction based on Integer32"""
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
        *(("decrement", 3),
          ("increment", 2),
          ("replace", 1))
    )


_ExpStaticToIsisRuleExpenseMetricAction_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleExpenseMetricAction_Object = MibTableColumn
expStaticToIsisRuleExpenseMetricAction = _ExpStaticToIsisRuleExpenseMetricAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 10),
    _ExpStaticToIsisRuleExpenseMetricAction_Type()
)
expStaticToIsisRuleExpenseMetricAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleExpenseMetricAction.setStatus("mandatory")


class _ExpStaticToIsisRuleExpenseMetric_Type(Integer32):
    """Custom type expStaticToIsisRuleExpenseMetric based on Integer32"""
    defaultValue = 0


_ExpStaticToIsisRuleExpenseMetric_Object = MibTableColumn
expStaticToIsisRuleExpenseMetric = _ExpStaticToIsisRuleExpenseMetric_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 11),
    _ExpStaticToIsisRuleExpenseMetric_Type()
)
expStaticToIsisRuleExpenseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleExpenseMetric.setStatus("mandatory")


class _ExpStaticToIsisRuleStatus_Type(Integer32):
    """Custom type expStaticToIsisRuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ExpStaticToIsisRuleStatus_Type.__name__ = "Integer32"
_ExpStaticToIsisRuleStatus_Object = MibTableColumn
expStaticToIsisRuleStatus = _ExpStaticToIsisRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 2, 17, 1, 12),
    _ExpStaticToIsisRuleStatus_Type()
)
expStaticToIsisRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expStaticToIsisRuleStatus.setStatus("mandatory")
_XFilter_ObjectIdentity = ObjectIdentity
xFilter = _XFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3)
)
_IpIfFilterTable_Object = MibTable
ipIfFilterTable = _IpIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1)
)
if mibBuilder.loadTexts:
    ipIfFilterTable.setStatus("deprecated")
_IpIfFilterEntry_Object = MibTableRow
ipIfFilterEntry = _IpIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1)
)
ipIfFilterEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterIndex"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterProtocol"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterDstPort"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterSrcPort"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterDstAddr"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterDstMask"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterSrcAddr"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilterSrcMask"),
)
if mibBuilder.loadTexts:
    ipIfFilterEntry.setStatus("deprecated")
_IpIfFilterIndex_Type = Integer32
_IpIfFilterIndex_Object = MibTableColumn
ipIfFilterIndex = _IpIfFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 1),
    _IpIfFilterIndex_Type()
)
ipIfFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterIndex.setStatus("deprecated")
_IpIfFilterDstAddr_Type = IpAddress
_IpIfFilterDstAddr_Object = MibTableColumn
ipIfFilterDstAddr = _IpIfFilterDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 2),
    _IpIfFilterDstAddr_Type()
)
ipIfFilterDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterDstAddr.setStatus("deprecated")
_IpIfFilterDstMask_Type = IpAddress
_IpIfFilterDstMask_Object = MibTableColumn
ipIfFilterDstMask = _IpIfFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 3),
    _IpIfFilterDstMask_Type()
)
ipIfFilterDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterDstMask.setStatus("deprecated")
_IpIfFilterSrcAddr_Type = IpAddress
_IpIfFilterSrcAddr_Object = MibTableColumn
ipIfFilterSrcAddr = _IpIfFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 4),
    _IpIfFilterSrcAddr_Type()
)
ipIfFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterSrcAddr.setStatus("deprecated")
_IpIfFilterSrcMask_Type = IpAddress
_IpIfFilterSrcMask_Object = MibTableColumn
ipIfFilterSrcMask = _IpIfFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 5),
    _IpIfFilterSrcMask_Type()
)
ipIfFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterSrcMask.setStatus("deprecated")


class _IpIfFilterProtocol_Type(Integer32):
    """Custom type ipIfFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpIfFilterProtocol_Type.__name__ = "Integer32"
_IpIfFilterProtocol_Object = MibTableColumn
ipIfFilterProtocol = _IpIfFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 6),
    _IpIfFilterProtocol_Type()
)
ipIfFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterProtocol.setStatus("deprecated")


class _IpIfFilterDstPort_Type(Integer32):
    """Custom type ipIfFilterDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpIfFilterDstPort_Type.__name__ = "Integer32"
_IpIfFilterDstPort_Object = MibTableColumn
ipIfFilterDstPort = _IpIfFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 7),
    _IpIfFilterDstPort_Type()
)
ipIfFilterDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterDstPort.setStatus("deprecated")


class _IpIfFilterSrcPort_Type(Integer32):
    """Custom type ipIfFilterSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpIfFilterSrcPort_Type.__name__ = "Integer32"
_IpIfFilterSrcPort_Object = MibTableColumn
ipIfFilterSrcPort = _IpIfFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 8),
    _IpIfFilterSrcPort_Type()
)
ipIfFilterSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilterSrcPort.setStatus("deprecated")


class _IpIfFilterAction_Type(Integer32):
    """Custom type ipIfFilterAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_IpIfFilterAction_Type.__name__ = "Integer32"
_IpIfFilterAction_Object = MibTableColumn
ipIfFilterAction = _IpIfFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 9),
    _IpIfFilterAction_Type()
)
ipIfFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFilterAction.setStatus("deprecated")


class _IpIfFilterStatus_Type(Integer32):
    """Custom type ipIfFilterStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpIfFilterStatus_Type.__name__ = "Integer32"
_IpIfFilterStatus_Object = MibTableColumn
ipIfFilterStatus = _IpIfFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 1, 1, 10),
    _IpIfFilterStatus_Type()
)
ipIfFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFilterStatus.setStatus("deprecated")


class _IpFilterState_Type(Integer32):
    """Custom type ipFilterState based on Integer32"""
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


_IpFilterState_Type.__name__ = "Integer32"
_IpFilterState_Object = MibScalar
ipFilterState = _IpFilterState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 2),
    _IpFilterState_Type()
)
ipFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterState.setStatus("mandatory")
_IpIfFilter2Table_Object = MibTable
ipIfFilter2Table = _IpIfFilter2Table_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3)
)
if mibBuilder.loadTexts:
    ipIfFilter2Table.setStatus("mandatory")
_IpIfFilter2Entry_Object = MibTableRow
ipIfFilter2Entry = _IpIfFilter2Entry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1)
)
ipIfFilter2Entry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2Index"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2Protocol"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2DstPortStart"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2DstPortEnd"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2TcpSyn"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2SrcPortStart"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2SrcPortEnd"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2DstMask"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2DstAddr"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2SrcMask"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "ipIfFilter2SrcAddr"),
)
if mibBuilder.loadTexts:
    ipIfFilter2Entry.setStatus("mandatory")
_IpIfFilter2Index_Type = Integer32
_IpIfFilter2Index_Object = MibTableColumn
ipIfFilter2Index = _IpIfFilter2Index_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 1),
    _IpIfFilter2Index_Type()
)
ipIfFilter2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2Index.setStatus("mandatory")
_IpIfFilter2DstAddr_Type = IpAddress
_IpIfFilter2DstAddr_Object = MibTableColumn
ipIfFilter2DstAddr = _IpIfFilter2DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 2),
    _IpIfFilter2DstAddr_Type()
)
ipIfFilter2DstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2DstAddr.setStatus("mandatory")
_IpIfFilter2DstMask_Type = IpAddress
_IpIfFilter2DstMask_Object = MibTableColumn
ipIfFilter2DstMask = _IpIfFilter2DstMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 3),
    _IpIfFilter2DstMask_Type()
)
ipIfFilter2DstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2DstMask.setStatus("mandatory")
_IpIfFilter2SrcAddr_Type = IpAddress
_IpIfFilter2SrcAddr_Object = MibTableColumn
ipIfFilter2SrcAddr = _IpIfFilter2SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 4),
    _IpIfFilter2SrcAddr_Type()
)
ipIfFilter2SrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2SrcAddr.setStatus("mandatory")
_IpIfFilter2SrcMask_Type = IpAddress
_IpIfFilter2SrcMask_Object = MibTableColumn
ipIfFilter2SrcMask = _IpIfFilter2SrcMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 5),
    _IpIfFilter2SrcMask_Type()
)
ipIfFilter2SrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2SrcMask.setStatus("mandatory")


class _IpIfFilter2Protocol_Type(Integer32):
    """Custom type ipIfFilter2Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpIfFilter2Protocol_Type.__name__ = "Integer32"
_IpIfFilter2Protocol_Object = MibTableColumn
ipIfFilter2Protocol = _IpIfFilter2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 6),
    _IpIfFilter2Protocol_Type()
)
ipIfFilter2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2Protocol.setStatus("mandatory")


class _IpIfFilter2DstPortStart_Type(Integer32):
    """Custom type ipIfFilter2DstPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpIfFilter2DstPortStart_Type.__name__ = "Integer32"
_IpIfFilter2DstPortStart_Object = MibTableColumn
ipIfFilter2DstPortStart = _IpIfFilter2DstPortStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 7),
    _IpIfFilter2DstPortStart_Type()
)
ipIfFilter2DstPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2DstPortStart.setStatus("mandatory")


class _IpIfFilter2SrcPortStart_Type(Integer32):
    """Custom type ipIfFilter2SrcPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpIfFilter2SrcPortStart_Type.__name__ = "Integer32"
_IpIfFilter2SrcPortStart_Object = MibTableColumn
ipIfFilter2SrcPortStart = _IpIfFilter2SrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 8),
    _IpIfFilter2SrcPortStart_Type()
)
ipIfFilter2SrcPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2SrcPortStart.setStatus("mandatory")


class _IpIfFilter2Action_Type(Integer32):
    """Custom type ipIfFilter2Action based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_IpIfFilter2Action_Type.__name__ = "Integer32"
_IpIfFilter2Action_Object = MibTableColumn
ipIfFilter2Action = _IpIfFilter2Action_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 9),
    _IpIfFilter2Action_Type()
)
ipIfFilter2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFilter2Action.setStatus("mandatory")


class _IpIfFilter2Status_Type(Integer32):
    """Custom type ipIfFilter2Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpIfFilter2Status_Type.__name__ = "Integer32"
_IpIfFilter2Status_Object = MibTableColumn
ipIfFilter2Status = _IpIfFilter2Status_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 10),
    _IpIfFilter2Status_Type()
)
ipIfFilter2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFilter2Status.setStatus("mandatory")


class _IpIfFilter2DstPortEnd_Type(Integer32):
    """Custom type ipIfFilter2DstPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpIfFilter2DstPortEnd_Type.__name__ = "Integer32"
_IpIfFilter2DstPortEnd_Object = MibTableColumn
ipIfFilter2DstPortEnd = _IpIfFilter2DstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 11),
    _IpIfFilter2DstPortEnd_Type()
)
ipIfFilter2DstPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2DstPortEnd.setStatus("mandatory")


class _IpIfFilter2SrcPortEnd_Type(Integer32):
    """Custom type ipIfFilter2SrcPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpIfFilter2SrcPortEnd_Type.__name__ = "Integer32"
_IpIfFilter2SrcPortEnd_Object = MibTableColumn
ipIfFilter2SrcPortEnd = _IpIfFilter2SrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 12),
    _IpIfFilter2SrcPortEnd_Type()
)
ipIfFilter2SrcPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2SrcPortEnd.setStatus("mandatory")


class _IpIfFilter2TcpSyn_Type(Integer32):
    """Custom type ipIfFilter2TcpSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("off", 1),
          ("on", 2))
    )


_IpIfFilter2TcpSyn_Type.__name__ = "Integer32"
_IpIfFilter2TcpSyn_Object = MibTableColumn
ipIfFilter2TcpSyn = _IpIfFilter2TcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 13),
    _IpIfFilter2TcpSyn_Type()
)
ipIfFilter2TcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfFilter2TcpSyn.setStatus("mandatory")


class _IpIfFilter2ProtocolPriority_Type(Integer32):
    """Custom type ipIfFilter2ProtocolPriority based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              256)
        )
    )
    namedValues = NamedValues(
        *(("high", 5),
          ("low", 1),
          ("medium", 3),
          ("none", 256))
    )


_IpIfFilter2ProtocolPriority_Type.__name__ = "Integer32"
_IpIfFilter2ProtocolPriority_Object = MibTableColumn
ipIfFilter2ProtocolPriority = _IpIfFilter2ProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 16, 3, 3, 1, 14),
    _IpIfFilter2ProtocolPriority_Type()
)
ipIfFilter2ProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfFilter2ProtocolPriority.setStatus("mandatory")
_XRip_ObjectIdentity = ObjectIdentity
xRip = _XRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 18)
)


class _RipState_Type(Integer32):
    """Custom type ripState based on Integer32"""
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


_RipState_Type.__name__ = "Integer32"
_RipState_Object = MibScalar
ripState = _RipState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 1),
    _RipState_Type()
)
ripState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripState.setStatus("mandatory")


class _RipStatus_Type(Integer32):
    """Custom type ripStatus based on Integer32"""
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
        *(("active", 1),
          ("ipDisabled", 3),
          ("noMemory", 5),
          ("noNetworksEnabled", 4),
          ("ripDisabled", 2))
    )


_RipStatus_Type.__name__ = "Integer32"
_RipStatus_Object = MibScalar
ripStatus = _RipStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 2),
    _RipStatus_Type()
)
ripStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatus.setStatus("mandatory")
_RipNetTable_Object = MibTable
ripNetTable = _RipNetTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3)
)
if mibBuilder.loadTexts:
    ripNetTable.setStatus("mandatory")
_RipNetEntry_Object = MibTableRow
ripNetEntry = _RipNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1)
)
ripNetEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "ripNetNet"),
)
if mibBuilder.loadTexts:
    ripNetEntry.setStatus("mandatory")
_RipNetNet_Type = IpAddress
_RipNetNet_Object = MibTableColumn
ripNetNet = _RipNetNet_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1, 1),
    _RipNetNet_Type()
)
ripNetNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNetNet.setStatus("mandatory")


class _RipNetState_Type(Integer32):
    """Custom type ripNetState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("full", 3),
          ("routerDiscovery", 2))
    )


_RipNetState_Type.__name__ = "Integer32"
_RipNetState_Object = MibTableColumn
ripNetState = _RipNetState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1, 2),
    _RipNetState_Type()
)
ripNetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNetState.setStatus("mandatory")
_RipNetRipsIn_Type = Counter32
_RipNetRipsIn_Object = MibTableColumn
ripNetRipsIn = _RipNetRipsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1, 3),
    _RipNetRipsIn_Type()
)
ripNetRipsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNetRipsIn.setStatus("mandatory")
_RipNetRipsOut_Type = Counter32
_RipNetRipsOut_Object = MibTableColumn
ripNetRipsOut = _RipNetRipsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1, 4),
    _RipNetRipsOut_Type()
)
ripNetRipsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNetRipsOut.setStatus("mandatory")


class _RipNetAlgorithm_Type(Integer32):
    """Custom type ripNetAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poisonedReverse", 1),
          ("splitHorizon", 2))
    )


_RipNetAlgorithm_Type.__name__ = "Integer32"
_RipNetAlgorithm_Object = MibTableColumn
ripNetAlgorithm = _RipNetAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 18, 3, 1, 5),
    _RipNetAlgorithm_Type()
)
ripNetAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNetAlgorithm.setStatus("mandatory")
_Xlpd_ObjectIdentity = ObjectIdentity
xlpd = _Xlpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 19)
)
_LpdQueueTable_Object = MibTable
lpdQueueTable = _LpdQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1)
)
if mibBuilder.loadTexts:
    lpdQueueTable.setStatus("mandatory")
_LpdQueueEntry_Object = MibTableRow
lpdQueueEntry = _LpdQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1)
)
lpdQueueEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "lpdQueueName"),
)
if mibBuilder.loadTexts:
    lpdQueueEntry.setStatus("mandatory")


class _LpdQueueStatus_Type(Integer32):
    """Custom type lpdQueueStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LpdQueueStatus_Type.__name__ = "Integer32"
_LpdQueueStatus_Object = MibTableColumn
lpdQueueStatus = _LpdQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 1),
    _LpdQueueStatus_Type()
)
lpdQueueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueueStatus.setStatus("mandatory")


class _LpdQueueName_Type(DisplayString):
    """Custom type lpdQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LpdQueueName_Type.__name__ = "DisplayString"
_LpdQueueName_Object = MibTableColumn
lpdQueueName = _LpdQueueName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 2),
    _LpdQueueName_Type()
)
lpdQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdQueueName.setStatus("mandatory")


class _LpdQueuePorts_Type(OctetString):
    """Custom type lpdQueuePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_LpdQueuePorts_Type.__name__ = "OctetString"
_LpdQueuePorts_Object = MibTableColumn
lpdQueuePorts = _LpdQueuePorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 3),
    _LpdQueuePorts_Type()
)
lpdQueuePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueuePorts.setStatus("mandatory")


class _LpdQueueEnabled_Type(Integer32):
    """Custom type lpdQueueEnabled based on Integer32"""
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


_LpdQueueEnabled_Type.__name__ = "Integer32"
_LpdQueueEnabled_Object = MibTableColumn
lpdQueueEnabled = _LpdQueueEnabled_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 4),
    _LpdQueueEnabled_Type()
)
lpdQueueEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueueEnabled.setStatus("mandatory")


class _LpdQueueLfConversion_Type(Integer32):
    """Custom type lpdQueueLfConversion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lf", 1),
          ("lfcr", 2))
    )


_LpdQueueLfConversion_Type.__name__ = "Integer32"
_LpdQueueLfConversion_Object = MibTableColumn
lpdQueueLfConversion = _LpdQueueLfConversion_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 5),
    _LpdQueueLfConversion_Type()
)
lpdQueueLfConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueueLfConversion.setStatus("mandatory")
_LpdQueueTotalJobs_Type = Gauge32
_LpdQueueTotalJobs_Object = MibTableColumn
lpdQueueTotalJobs = _LpdQueueTotalJobs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 6),
    _LpdQueueTotalJobs_Type()
)
lpdQueueTotalJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdQueueTotalJobs.setStatus("mandatory")
_LpdQueueActiveJobs_Type = Gauge32
_LpdQueueActiveJobs_Object = MibTableColumn
lpdQueueActiveJobs = _LpdQueueActiveJobs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 7),
    _LpdQueueActiveJobs_Type()
)
lpdQueueActiveJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdQueueActiveJobs.setStatus("mandatory")
_LpdQueueWaitingJobs_Type = Gauge32
_LpdQueueWaitingJobs_Object = MibTableColumn
lpdQueueWaitingJobs = _LpdQueueWaitingJobs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 8),
    _LpdQueueWaitingJobs_Type()
)
lpdQueueWaitingJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdQueueWaitingJobs.setStatus("mandatory")
_LpdQueueProcessedJobs_Type = Counter32
_LpdQueueProcessedJobs_Object = MibTableColumn
lpdQueueProcessedJobs = _LpdQueueProcessedJobs_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 9),
    _LpdQueueProcessedJobs_Type()
)
lpdQueueProcessedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdQueueProcessedJobs.setStatus("mandatory")


class _LpdQueueFormFeed_Type(Integer32):
    """Custom type lpdQueueFormFeed based on Integer32"""
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
        *(("formfeedafter", 1),
          ("formfeedbefore", 2),
          ("formfeednone", 3))
    )


_LpdQueueFormFeed_Type.__name__ = "Integer32"
_LpdQueueFormFeed_Object = MibTableColumn
lpdQueueFormFeed = _LpdQueueFormFeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 10),
    _LpdQueueFormFeed_Type()
)
lpdQueueFormFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueueFormFeed.setStatus("mandatory")


class _LpdQueueBypass_Type(Integer32):
    """Custom type lpdQueueBypass based on Integer32"""
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


_LpdQueueBypass_Type.__name__ = "Integer32"
_LpdQueueBypass_Object = MibTableColumn
lpdQueueBypass = _LpdQueueBypass_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 1, 1, 11),
    _LpdQueueBypass_Type()
)
lpdQueueBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdQueueBypass.setStatus("mandatory")
_LpdJobTable_Object = MibTable
lpdJobTable = _LpdJobTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2)
)
if mibBuilder.loadTexts:
    lpdJobTable.setStatus("mandatory")
_LpdJobEntry_Object = MibTableRow
lpdJobEntry = _LpdJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1)
)
lpdJobEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "lpdQueueName"),
    (0, "MRV-IN-REACH-INTERNET-MIB", "lpdJobNumber"),
)
if mibBuilder.loadTexts:
    lpdJobEntry.setStatus("mandatory")


class _LpdJobStatus_Type(Integer32):
    """Custom type lpdJobStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LpdJobStatus_Type.__name__ = "Integer32"
_LpdJobStatus_Object = MibTableColumn
lpdJobStatus = _LpdJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 1),
    _LpdJobStatus_Type()
)
lpdJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpdJobStatus.setStatus("mandatory")


class _LpdJobNumber_Type(Integer32):
    """Custom type lpdJobNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_LpdJobNumber_Type.__name__ = "Integer32"
_LpdJobNumber_Object = MibTableColumn
lpdJobNumber = _LpdJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 2),
    _LpdJobNumber_Type()
)
lpdJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobNumber.setStatus("mandatory")


class _LpdJobAssignedPort_Type(Integer32):
    """Custom type lpdJobAssignedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_LpdJobAssignedPort_Type.__name__ = "Integer32"
_LpdJobAssignedPort_Object = MibTableColumn
lpdJobAssignedPort = _LpdJobAssignedPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 3),
    _LpdJobAssignedPort_Type()
)
lpdJobAssignedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobAssignedPort.setStatus("mandatory")


class _LpdJobFileSize_Type(Integer32):
    """Custom type lpdJobFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpdJobFileSize_Type.__name__ = "Integer32"
_LpdJobFileSize_Object = MibTableColumn
lpdJobFileSize = _LpdJobFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 4),
    _LpdJobFileSize_Type()
)
lpdJobFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobFileSize.setStatus("mandatory")


class _LpdJobHostName_Type(DisplayString):
    """Custom type lpdJobHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_LpdJobHostName_Type.__name__ = "DisplayString"
_LpdJobHostName_Object = MibTableColumn
lpdJobHostName = _LpdJobHostName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 5),
    _LpdJobHostName_Type()
)
lpdJobHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobHostName.setStatus("mandatory")


class _LpdJobFileName_Type(DisplayString):
    """Custom type lpdJobFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_LpdJobFileName_Type.__name__ = "DisplayString"
_LpdJobFileName_Object = MibTableColumn
lpdJobFileName = _LpdJobFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 6),
    _LpdJobFileName_Type()
)
lpdJobFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobFileName.setStatus("mandatory")


class _LpdJobState_Type(Integer32):
    """Custom type lpdJobState based on Integer32"""
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
        *(("aborted", 6),
          ("assigned", 3),
          ("completed", 7),
          ("error", 8),
          ("flushing", 9),
          ("initialized", 1),
          ("printingControl", 5),
          ("printingData", 4),
          ("waiting", 2))
    )


_LpdJobState_Type.__name__ = "Integer32"
_LpdJobState_Object = MibTableColumn
lpdJobState = _LpdJobState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 19, 2, 1, 7),
    _LpdJobState_Type()
)
lpdJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpdJobState.setStatus("mandatory")
_XSecurID_ObjectIdentity = ObjectIdentity
xSecurID = _XSecurID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 20)
)


class _SecurIDServerName0_Type(DisplayString):
    """Custom type securIDServerName0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SecurIDServerName0_Type.__name__ = "DisplayString"
_SecurIDServerName0_Object = MibScalar
securIDServerName0 = _SecurIDServerName0_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 1),
    _SecurIDServerName0_Type()
)
securIDServerName0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDServerName0.setStatus("mandatory")


class _SecurIDServerName1_Type(DisplayString):
    """Custom type securIDServerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SecurIDServerName1_Type.__name__ = "DisplayString"
_SecurIDServerName1_Object = MibScalar
securIDServerName1 = _SecurIDServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 2),
    _SecurIDServerName1_Type()
)
securIDServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDServerName1.setStatus("mandatory")


class _SecurIDServerName2_Type(DisplayString):
    """Custom type securIDServerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SecurIDServerName2_Type.__name__ = "DisplayString"
_SecurIDServerName2_Object = MibScalar
securIDServerName2 = _SecurIDServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 3),
    _SecurIDServerName2_Type()
)
securIDServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDServerName2.setStatus("mandatory")


class _SecurIDServerName3_Type(DisplayString):
    """Custom type securIDServerName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SecurIDServerName3_Type.__name__ = "DisplayString"
_SecurIDServerName3_Object = MibScalar
securIDServerName3 = _SecurIDServerName3_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 4),
    _SecurIDServerName3_Type()
)
securIDServerName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDServerName3.setStatus("mandatory")


class _SecurIDServerName4_Type(DisplayString):
    """Custom type securIDServerName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SecurIDServerName4_Type.__name__ = "DisplayString"
_SecurIDServerName4_Object = MibScalar
securIDServerName4 = _SecurIDServerName4_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 5),
    _SecurIDServerName4_Type()
)
securIDServerName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDServerName4.setStatus("mandatory")


class _SecurIDMaxRetries_Type(Integer32):
    """Custom type securIDMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SecurIDMaxRetries_Type.__name__ = "Integer32"
_SecurIDMaxRetries_Object = MibScalar
securIDMaxRetries = _SecurIDMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 6),
    _SecurIDMaxRetries_Type()
)
securIDMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDMaxRetries.setStatus("mandatory")


class _SecurIDBaseTimeout_Type(Integer32):
    """Custom type securIDBaseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SecurIDBaseTimeout_Type.__name__ = "Integer32"
_SecurIDBaseTimeout_Object = MibScalar
securIDBaseTimeout = _SecurIDBaseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 7),
    _SecurIDBaseTimeout_Type()
)
securIDBaseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDBaseTimeout.setStatus("mandatory")


class _SecurIDPort_Type(Integer32):
    """Custom type securIDPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SecurIDPort_Type.__name__ = "Integer32"
_SecurIDPort_Object = MibScalar
securIDPort = _SecurIDPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 8),
    _SecurIDPort_Type()
)
securIDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDPort.setStatus("mandatory")


class _SecurIDQueryLimit_Type(Integer32):
    """Custom type securIDQueryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SecurIDQueryLimit_Type.__name__ = "Integer32"
_SecurIDQueryLimit_Object = MibScalar
securIDQueryLimit = _SecurIDQueryLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 9),
    _SecurIDQueryLimit_Type()
)
securIDQueryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDQueryLimit.setStatus("mandatory")


class _SecurIDEncryptionMode_Type(Integer32):
    """Custom type securIDEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("sdiBlockCipher", 1))
    )


_SecurIDEncryptionMode_Type.__name__ = "Integer32"
_SecurIDEncryptionMode_Object = MibScalar
securIDEncryptionMode = _SecurIDEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 10),
    _SecurIDEncryptionMode_Type()
)
securIDEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDEncryptionMode.setStatus("mandatory")
_SecurIDInsecureLogins_Type = Counter32
_SecurIDInsecureLogins_Object = MibScalar
securIDInsecureLogins = _SecurIDInsecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 11),
    _SecurIDInsecureLogins_Type()
)
securIDInsecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDInsecureLogins.setStatus("mandatory")
_SecurIDSecureLogins_Type = Counter32
_SecurIDSecureLogins_Object = MibScalar
securIDSecureLogins = _SecurIDSecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 12),
    _SecurIDSecureLogins_Type()
)
securIDSecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDSecureLogins.setStatus("mandatory")
_SecurIDSecureLoginsFailed_Type = Counter32
_SecurIDSecureLoginsFailed_Object = MibScalar
securIDSecureLoginsFailed = _SecurIDSecureLoginsFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 13),
    _SecurIDSecureLoginsFailed_Type()
)
securIDSecureLoginsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDSecureLoginsFailed.setStatus("mandatory")
_SecurIDServerAccess0_Type = Counter32
_SecurIDServerAccess0_Object = MibScalar
securIDServerAccess0 = _SecurIDServerAccess0_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 14),
    _SecurIDServerAccess0_Type()
)
securIDServerAccess0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccess0.setStatus("mandatory")
_SecurIDServerAccessFailed0_Type = Counter32
_SecurIDServerAccessFailed0_Object = MibScalar
securIDServerAccessFailed0 = _SecurIDServerAccessFailed0_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 15),
    _SecurIDServerAccessFailed0_Type()
)
securIDServerAccessFailed0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccessFailed0.setStatus("mandatory")
_SecurIDServerAccess1_Type = Counter32
_SecurIDServerAccess1_Object = MibScalar
securIDServerAccess1 = _SecurIDServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 16),
    _SecurIDServerAccess1_Type()
)
securIDServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccess1.setStatus("mandatory")
_SecurIDServerAccessFailed1_Type = Counter32
_SecurIDServerAccessFailed1_Object = MibScalar
securIDServerAccessFailed1 = _SecurIDServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 17),
    _SecurIDServerAccessFailed1_Type()
)
securIDServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccessFailed1.setStatus("mandatory")
_SecurIDServerAccess2_Type = Counter32
_SecurIDServerAccess2_Object = MibScalar
securIDServerAccess2 = _SecurIDServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 18),
    _SecurIDServerAccess2_Type()
)
securIDServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccess2.setStatus("mandatory")
_SecurIDServerAccessFailed2_Type = Counter32
_SecurIDServerAccessFailed2_Object = MibScalar
securIDServerAccessFailed2 = _SecurIDServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 19),
    _SecurIDServerAccessFailed2_Type()
)
securIDServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccessFailed2.setStatus("mandatory")
_SecurIDServerAccess3_Type = Counter32
_SecurIDServerAccess3_Object = MibScalar
securIDServerAccess3 = _SecurIDServerAccess3_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 20),
    _SecurIDServerAccess3_Type()
)
securIDServerAccess3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccess3.setStatus("mandatory")
_SecurIDServerAccessFailed3_Type = Counter32
_SecurIDServerAccessFailed3_Object = MibScalar
securIDServerAccessFailed3 = _SecurIDServerAccessFailed3_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 21),
    _SecurIDServerAccessFailed3_Type()
)
securIDServerAccessFailed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccessFailed3.setStatus("mandatory")
_SecurIDServerAccess4_Type = Counter32
_SecurIDServerAccess4_Object = MibScalar
securIDServerAccess4 = _SecurIDServerAccess4_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 22),
    _SecurIDServerAccess4_Type()
)
securIDServerAccess4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccess4.setStatus("mandatory")
_SecurIDServerAccessFailed4_Type = Counter32
_SecurIDServerAccessFailed4_Object = MibScalar
securIDServerAccessFailed4 = _SecurIDServerAccessFailed4_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 23),
    _SecurIDServerAccessFailed4_Type()
)
securIDServerAccessFailed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDServerAccessFailed4.setStatus("mandatory")


class _SecurIDErrorPortIndex_Type(Integer32):
    """Custom type securIDErrorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SecurIDErrorPortIndex_Type.__name__ = "Integer32"
_SecurIDErrorPortIndex_Object = MibScalar
securIDErrorPortIndex = _SecurIDErrorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 24),
    _SecurIDErrorPortIndex_Type()
)
securIDErrorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDErrorPortIndex.setStatus("mandatory")


class _SecurIDError_Type(Integer32):
    """Custom type securIDError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SecurIDError_Type.__name__ = "Integer32"
_SecurIDError_Object = MibScalar
securIDError = _SecurIDError_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 25),
    _SecurIDError_Type()
)
securIDError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDError.setStatus("mandatory")


class _SecurIDErrorUsername_Type(DisplayString):
    """Custom type securIDErrorUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SecurIDErrorUsername_Type.__name__ = "DisplayString"
_SecurIDErrorUsername_Object = MibScalar
securIDErrorUsername = _SecurIDErrorUsername_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 26),
    _SecurIDErrorUsername_Type()
)
securIDErrorUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDErrorUsername.setStatus("mandatory")
_SecurIDPortTable_Object = MibTable
securIDPortTable = _SecurIDPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 27)
)
if mibBuilder.loadTexts:
    securIDPortTable.setStatus("mandatory")
_SecurIDPortEntry_Object = MibTableRow
securIDPortEntry = _SecurIDPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 27, 1)
)
securIDPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "securIDPortIndex"),
)
if mibBuilder.loadTexts:
    securIDPortEntry.setStatus("mandatory")
_SecurIDPortIndex_Type = Integer32
_SecurIDPortIndex_Object = MibTableColumn
securIDPortIndex = _SecurIDPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 27, 1, 1),
    _SecurIDPortIndex_Type()
)
securIDPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securIDPortIndex.setStatus("mandatory")


class _SecurIDPortStatus_Type(Integer32):
    """Custom type securIDPortStatus based on Integer32"""
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


_SecurIDPortStatus_Type.__name__ = "Integer32"
_SecurIDPortStatus_Object = MibTableColumn
securIDPortStatus = _SecurIDPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 20, 27, 1, 2),
    _SecurIDPortStatus_Type()
)
securIDPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securIDPortStatus.setStatus("mandatory")
_XSsh_ObjectIdentity = ObjectIdentity
xSsh = _XSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 23)
)
_SshPortTable_Object = MibTable
sshPortTable = _SshPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1)
)
if mibBuilder.loadTexts:
    sshPortTable.setStatus("mandatory")
_SshPortEntry_Object = MibTableRow
sshPortEntry = _SshPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1)
)
sshPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-INTERNET-MIB", "sshPortIndex"),
)
if mibBuilder.loadTexts:
    sshPortEntry.setStatus("mandatory")
_SshPortIndex_Type = Integer32
_SshPortIndex_Object = MibTableColumn
sshPortIndex = _SshPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 1),
    _SshPortIndex_Type()
)
sshPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshPortIndex.setStatus("mandatory")


class _SshPortIncomingTcpPort_Type(Integer32):
    """Custom type sshPortIncomingTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SshPortIncomingTcpPort_Type.__name__ = "Integer32"
_SshPortIncomingTcpPort_Object = MibTableColumn
sshPortIncomingTcpPort = _SshPortIncomingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 2),
    _SshPortIncomingTcpPort_Type()
)
sshPortIncomingTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortIncomingTcpPort.setStatus("mandatory")


class _SshPortNewlineFiltering_Type(Integer32):
    """Custom type sshPortNewlineFiltering based on Integer32"""
    defaultValue = 1

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
        *(("crLfToCr", 4),
          ("crLfToCrNull", 5),
          ("crNullToCr", 6),
          ("crNullToCrLf", 7),
          ("crToCrLf", 2),
          ("crToCrNull", 3),
          ("none", 1))
    )


_SshPortNewlineFiltering_Type.__name__ = "Integer32"
_SshPortNewlineFiltering_Object = MibTableColumn
sshPortNewlineFiltering = _SshPortNewlineFiltering_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 3),
    _SshPortNewlineFiltering_Type()
)
sshPortNewlineFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortNewlineFiltering.setStatus("mandatory")


class _SshPortNewline_Type(Integer32):
    """Custom type sshPortNewline based on Integer32"""
    defaultValue = 1

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
        *(("crLfToCr", 4),
          ("crLfToCrNull", 5),
          ("crNullToCr", 6),
          ("crNullToCrLf", 7),
          ("crToCrLf", 2),
          ("crToCrNull", 3),
          ("none", 1))
    )


_SshPortNewline_Type.__name__ = "Integer32"
_SshPortNewline_Object = MibTableColumn
sshPortNewline = _SshPortNewline_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 4),
    _SshPortNewline_Type()
)
sshPortNewline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortNewline.setStatus("mandatory")


class _SshPortTransmitBufferedTime_Type(Integer32):
    """Custom type sshPortTransmitBufferedTime based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1500),
    )


_SshPortTransmitBufferedTime_Type.__name__ = "Integer32"
_SshPortTransmitBufferedTime_Object = MibTableColumn
sshPortTransmitBufferedTime = _SshPortTransmitBufferedTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 5),
    _SshPortTransmitBufferedTime_Type()
)
sshPortTransmitBufferedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortTransmitBufferedTime.setStatus("mandatory")


class _SshPortRemoteProtocol_Type(Integer32):
    """Custom type sshPortRemoteProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ssh", 1),
          ("telnet", 2))
    )


_SshPortRemoteProtocol_Type.__name__ = "Integer32"
_SshPortRemoteProtocol_Object = MibTableColumn
sshPortRemoteProtocol = _SshPortRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 6),
    _SshPortRemoteProtocol_Type()
)
sshPortRemoteProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortRemoteProtocol.setStatus("mandatory")


class _SshPortBreakSequence_Type(OctetString):
    """Custom type sshPortBreakSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SshPortBreakSequence_Type.__name__ = "OctetString"
_SshPortBreakSequence_Object = MibTableColumn
sshPortBreakSequence = _SshPortBreakSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 1, 1, 7),
    _SshPortBreakSequence_Type()
)
sshPortBreakSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPortBreakSequence.setStatus("mandatory")


class _SshCipherMask_Type(OctetString):
    """Custom type sshCipherMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SshCipherMask_Type.__name__ = "OctetString"
_SshCipherMask_Object = MibScalar
sshCipherMask = _SshCipherMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 2),
    _SshCipherMask_Type()
)
sshCipherMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshCipherMask.setStatus("mandatory")


class _SshAuthenticationTimeout_Type(Integer32):
    """Custom type sshAuthenticationTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SshAuthenticationTimeout_Type.__name__ = "Integer32"
_SshAuthenticationTimeout_Object = MibScalar
sshAuthenticationTimeout = _SshAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 3),
    _SshAuthenticationTimeout_Type()
)
sshAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthenticationTimeout.setStatus("mandatory")


class _SshHostKeyLength_Type(Integer32):
    """Custom type sshHostKeyLength based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_SshHostKeyLength_Type.__name__ = "Integer32"
_SshHostKeyLength_Object = MibScalar
sshHostKeyLength = _SshHostKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 4),
    _SshHostKeyLength_Type()
)
sshHostKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyLength.setStatus("mandatory")


class _SshHostKeyGenerate_Type(Integer32):
    """Custom type sshHostKeyGenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generate", 2),
          ("ready", 1),
          ("update", 3))
    )


_SshHostKeyGenerate_Type.__name__ = "Integer32"
_SshHostKeyGenerate_Object = MibScalar
sshHostKeyGenerate = _SshHostKeyGenerate_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 5),
    _SshHostKeyGenerate_Type()
)
sshHostKeyGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyGenerate.setStatus("mandatory")


class _SshServerKeyLength_Type(Integer32):
    """Custom type sshServerKeyLength based on Integer32"""
    defaultValue = 768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_SshServerKeyLength_Type.__name__ = "Integer32"
_SshServerKeyLength_Object = MibScalar
sshServerKeyLength = _SshServerKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 6),
    _SshServerKeyLength_Type()
)
sshServerKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerKeyLength.setStatus("mandatory")


class _SshServerKeyTtl_Type(Integer32):
    """Custom type sshServerKeyTtl based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_SshServerKeyTtl_Type.__name__ = "Integer32"
_SshServerKeyTtl_Object = MibScalar
sshServerKeyTtl = _SshServerKeyTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 7),
    _SshServerKeyTtl_Type()
)
sshServerKeyTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerKeyTtl.setStatus("mandatory")


class _SshServerMaxBufferSize_Type(Integer32):
    """Custom type sshServerMaxBufferSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 262144),
    )


_SshServerMaxBufferSize_Type.__name__ = "Integer32"
_SshServerMaxBufferSize_Object = MibScalar
sshServerMaxBufferSize = _SshServerMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 23, 8),
    _SshServerMaxBufferSize_Type()
)
sshServerMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerMaxBufferSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-INTERNET-MIB",
    **{"xInternetDep": xInternetDep,
       "xInternet": xInternet,
       "xIp": xIp,
       "ipGatewayAddress1": ipGatewayAddress1,
       "ipGatewayAddress2": ipGatewayAddress2,
       "ipAutoSubnetMask": ipAutoSubnetMask,
       "ipReassembly": ipReassembly,
       "ipFragmentsQueuedHigh": ipFragmentsQueuedHigh,
       "ipFragmentsQueuedCurrent": ipFragmentsQueuedCurrent,
       "ipGenAdExtTable": ipGenAdExtTable,
       "ipGenAdExtEntry": ipGenAdExtEntry,
       "ipGenAdEntExtType": ipGenAdEntExtType,
       "ipGenAdEntExtBroadcast": ipGenAdEntExtBroadcast,
       "ipARPTimeout": ipARPTimeout,
       "ipGatewayPingInterval": ipGatewayPingInterval,
       "ipConfigureBootp": ipConfigureBootp,
       "xTcp": xTcp,
       "tcpPortTable": tcpPortTable,
       "tcpPortEntry": tcpPortEntry,
       "tcpPortIndex": tcpPortIndex,
       "tcpPortConnectByAddress": tcpPortConnectByAddress,
       "tcpPortWindowSize": tcpPortWindowSize,
       "tcpPortKeepAliveLimit": tcpPortKeepAliveLimit,
       "tcpResequencing": tcpResequencing,
       "tcpQueuedSegs": tcpQueuedSegs,
       "tcpDiscardSegs": tcpDiscardSegs,
       "tcpConnectTimer": tcpConnectTimer,
       "tcpLocalPortBase": tcpLocalPortBase,
       "tcpLocalPortIncrement": tcpLocalPortIncrement,
       "tcpRoutingTblSz": tcpRoutingTblSz,
       "tcpDataSendDelay": tcpDataSendDelay,
       "tcpAckDelay": tcpAckDelay,
       "tcpRetransmitMin": tcpRetransmitMin,
       "xSnmpAgent": xSnmpAgent,
       "snmpAgentGetCommunity": snmpAgentGetCommunity,
       "snmpAgentSetCommunity": snmpAgentSetCommunity,
       "snmpAgentTrapCommunity": snmpAgentTrapCommunity,
       "snmpAgentGetClientNumber": snmpAgentGetClientNumber,
       "snmpAgentSetClientNumber": snmpAgentSetClientNumber,
       "snmpAgentTrapClientNumber": snmpAgentTrapClientNumber,
       "getClientTable": getClientTable,
       "getClientEntry": getClientEntry,
       "getClientIndex": getClientIndex,
       "getClientEntryStatus": getClientEntryStatus,
       "getClientAddressType": getClientAddressType,
       "getClientAddress": getClientAddress,
       "setClientTable": setClientTable,
       "setClientEntry": setClientEntry,
       "setClientIndex": setClientIndex,
       "setClientEntryStatus": setClientEntryStatus,
       "setClientAddressType": setClientAddressType,
       "setClientAddress": setClientAddress,
       "trapClientTable": trapClientTable,
       "trapClientEntry": trapClientEntry,
       "trapClientIndex": trapClientIndex,
       "trapClientEntryStatus": trapClientEntryStatus,
       "trapClientAddressType": trapClientAddressType,
       "trapClientAddress": trapClientAddress,
       "snmpAgentAuthFailureAddress": snmpAgentAuthFailureAddress,
       "snmpAgentCommunityAuthenticationAlways": snmpAgentCommunityAuthenticationAlways,
       "snmpAgentTrapClientPingHost1": snmpAgentTrapClientPingHost1,
       "snmpAgentTrapClientPingHost2": snmpAgentTrapClientPingHost2,
       "snmpAgentTrapClientPingHost1PollInterval": snmpAgentTrapClientPingHost1PollInterval,
       "snmpAgentTrapClientPingHost2PollInterval": snmpAgentTrapClientPingHost2PollInterval,
       "snmpAgentTrapClientPingHost1PollRetries": snmpAgentTrapClientPingHost1PollRetries,
       "snmpAgentTrapClientPingHost2PollRetries": snmpAgentTrapClientPingHost2PollRetries,
       "snmpAgentTrapClientQuerySourceHost1": snmpAgentTrapClientQuerySourceHost1,
       "snmpAgentTrapClientQuerySourceHost2": snmpAgentTrapClientQuerySourceHost2,
       "snmpAgentTrapClientQuerySourceHost1Timeout": snmpAgentTrapClientQuerySourceHost1Timeout,
       "snmpAgentTrapClientQuerySourceHost2Timeout": snmpAgentTrapClientQuerySourceHost2Timeout,
       "xDomainResolver": xDomainResolver,
       "domainResolverSuffix": domainResolverSuffix,
       "domainResolverAddress1": domainResolverAddress1,
       "domainResolverAddress2": domainResolverAddress2,
       "domainResolverTtl": domainResolverTtl,
       "domainResolverNameNumber": domainResolverNameNumber,
       "nameTable": nameTable,
       "nameEntry": nameEntry,
       "nameName": nameName,
       "nameAddress": nameAddress,
       "nameStatus": nameStatus,
       "nameSource": nameSource,
       "nameTtl": nameTtl,
       "domainResolverPpp": domainResolverPpp,
       "domainResolverPppPrimaryServer": domainResolverPppPrimaryServer,
       "domainResolverPppSecondaryServer": domainResolverPppSecondaryServer,
       "xSlip": xSlip,
       "slipTable": slipTable,
       "slipEntry": slipEntry,
       "slipIndex": slipIndex,
       "slipState": slipState,
       "slipLocalAddress": slipLocalAddress,
       "slipRemoteAddress": slipRemoteAddress,
       "slipMask": slipMask,
       "slipPortPacketsReceived": slipPortPacketsReceived,
       "slipPortPacketsSent": slipPortPacketsSent,
       "slipPortPacketsDiscarded": slipPortPacketsDiscarded,
       "slipPortPacketLengthErrors": slipPortPacketLengthErrors,
       "slipPortPacketChecksumErrors": slipPortPacketChecksumErrors,
       "slipNetworkPacketsReceived": slipNetworkPacketsReceived,
       "slipNetworkPacketsSent": slipNetworkPacketsSent,
       "slipNetworkPacketsDiscarded": slipNetworkPacketsDiscarded,
       "xTelnet": xTelnet,
       "telnetPortTable": telnetPortTable,
       "telnetPortEntry": telnetPortEntry,
       "telnetPortIndex": telnetPortIndex,
       "telnetPortIncomingTcpPort": telnetPortIncomingTcpPort,
       "telnetPortOutgoingTcpPort": telnetPortOutgoingTcpPort,
       "telnetPortNewlineTranslation": telnetPortNewlineTranslation,
       "telnetPortTerminalType": telnetPortTerminalType,
       "telnetPortEorReflection": telnetPortEorReflection,
       "telnetPortBinaryMode": telnetPortBinaryMode,
       "telnetPortSendLocation": telnetPortSendLocation,
       "telnetPortClientLocation": telnetPortClientLocation,
       "telnetPortPassiveSendLocation": telnetPortPassiveSendLocation,
       "telnetSerialPortTable": telnetSerialPortTable,
       "telnetSerialPortEntry": telnetSerialPortEntry,
       "telnetSerialPortIndex": telnetSerialPortIndex,
       "telnetSerialPortOptionDisplay": telnetSerialPortOptionDisplay,
       "telnetSerialPortCsiEscape": telnetSerialPortCsiEscape,
       "telnetSerialPortEchoMode": telnetSerialPortEchoMode,
       "telnetSerialPortNewlineMode": telnetSerialPortNewlineMode,
       "telnetSerialPortTransmitMode": telnetSerialPortTransmitMode,
       "telnetSerialPortTransmitCharacterTimes": telnetSerialPortTransmitCharacterTimes,
       "telnetSerialPortAbortOutputCharacter": telnetSerialPortAbortOutputCharacter,
       "telnetSerialPortAttentionCharacter": telnetSerialPortAttentionCharacter,
       "telnetSerialPortEraseKeyCharacter": telnetSerialPortEraseKeyCharacter,
       "telnetSerialPortEraseLineCharacter": telnetSerialPortEraseLineCharacter,
       "telnetSerialPortInterruptCharacter": telnetSerialPortInterruptCharacter,
       "telnetSerialPortQueryCharacter": telnetSerialPortQueryCharacter,
       "telnetSerialPortSynchronizeCharacter": telnetSerialPortSynchronizeCharacter,
       "telnetSerialPortUrgentBreak": telnetSerialPortUrgentBreak,
       "telnetSerialPortRs491": telnetSerialPortRs491,
       "telnetSerialPortTransmitBufferedTime": telnetSerialPortTransmitBufferedTime,
       "telnetSerialPortInterpretInterruptAsBreak": telnetSerialPortInterpretInterruptAsBreak,
       "telnetSerialPortPass8d": telnetSerialPortPass8d,
       "telnetSerialPortComControlClient": telnetSerialPortComControlClient,
       "telnetSerialPortComControlServer": telnetSerialPortComControlServer,
       "telnetSerialPortComControlServerRaisesDtr": telnetSerialPortComControlServerRaisesDtr,
       "telnetSerialPortComControlClientTogglesDtr": telnetSerialPortComControlClientTogglesDtr,
       "xTn3270": xTn3270,
       "tn3270DeviceNumber": tn3270DeviceNumber,
       "tn3270LanguageNumber": tn3270LanguageNumber,
       "tn3270PortKeymapStatus": tn3270PortKeymapStatus,
       "tn3270DeviceTable": tn3270DeviceTable,
       "tn3270DeviceEntry": tn3270DeviceEntry,
       "tn3270DeviceName": tn3270DeviceName,
       "tn3270DeviceStatus": tn3270DeviceStatus,
       "tn3270DeviceType": tn3270DeviceType,
       "tn3270Device3278Model": tn3270Device3278Model,
       "tn3270DeviceKeyNumber": tn3270DeviceKeyNumber,
       "tn3270DeviceScreenNumber": tn3270DeviceScreenNumber,
       "tn3270KeyTable": tn3270KeyTable,
       "tn3270KeyEntry": tn3270KeyEntry,
       "tn3270KeyDeviceName": tn3270KeyDeviceName,
       "tn3270KeyName": tn3270KeyName,
       "tn3270KeyStatus": tn3270KeyStatus,
       "tn3270KeyCharacterSequence": tn3270KeyCharacterSequence,
       "tn3270KeyDescription": tn3270KeyDescription,
       "tn3270ScreenTable": tn3270ScreenTable,
       "tn3270ScreenEntry": tn3270ScreenEntry,
       "tn3270ScreenDeviceName": tn3270ScreenDeviceName,
       "tn3270ScreenActionName": tn3270ScreenActionName,
       "tn3270ScreenStatus": tn3270ScreenStatus,
       "tn3270ScreenCharacterSequence": tn3270ScreenCharacterSequence,
       "tn3270LanguageTable": tn3270LanguageTable,
       "tn3270LanguageEntry": tn3270LanguageEntry,
       "tn3270LanguageName": tn3270LanguageName,
       "tn3270LanguageStatus": tn3270LanguageStatus,
       "eToALanguageTable": eToALanguageTable,
       "eToALanguageEntry": eToALanguageEntry,
       "eToALanguageName": eToALanguageName,
       "eToAOffset": eToAOffset,
       "eToAValue": eToAValue,
       "aToELanguageTable": aToELanguageTable,
       "aToELanguageEntry": aToELanguageEntry,
       "aToELanguageName": aToELanguageName,
       "aToEOffset": aToEOffset,
       "aToEValue": aToEValue,
       "tn3270PortTable": tn3270PortTable,
       "tn3270PortEntry": tn3270PortEntry,
       "tn3270PortIndex": tn3270PortIndex,
       "tn3270PortDeviceName": tn3270PortDeviceName,
       "tn3270PortLanguageName": tn3270PortLanguageName,
       "tn3270PortExtendedAttributes": tn3270PortExtendedAttributes,
       "tn3270PortEorNegotiation": tn3270PortEorNegotiation,
       "tn3270PortErrorLock": tn3270PortErrorLock,
       "tn3270PortPrinterPort": tn3270PortPrinterPort,
       "tn3270PortOutgoingTcpPort": tn3270PortOutgoingTcpPort,
       "tn3270PortSpaceInsert": tn3270PortSpaceInsert,
       "tn3270PortTypeAhead": tn3270PortTypeAhead,
       "tn3270PrefixKeyMap": tn3270PrefixKeyMap,
       "tn3270PortScanner": tn3270PortScanner,
       "xKerberos": xKerberos,
       "kerbStatus": kerbStatus,
       "kerbRealm": kerbRealm,
       "kerbQueryLimit": kerbQueryLimit,
       "kerbMasterName": kerbMasterName,
       "kerbServerName1": kerbServerName1,
       "kerbServerName2": kerbServerName2,
       "kerbInsecureLogins": kerbInsecureLogins,
       "kerbSecureLogins": kerbSecureLogins,
       "kerbSecureLoginsFailed": kerbSecureLoginsFailed,
       "kerbPasswordChangeFailed": kerbPasswordChangeFailed,
       "kerbError": kerbError,
       "kerbErrorTime": kerbErrorTime,
       "kerbMasterAccess": kerbMasterAccess,
       "kerbMasterAccessFailed": kerbMasterAccessFailed,
       "kerbServerAccess1": kerbServerAccess1,
       "kerbServerAccessFailed1": kerbServerAccessFailed1,
       "kerbServerAccess2": kerbServerAccess2,
       "kerbServerAccessFailed2": kerbServerAccessFailed2,
       "kerbPortTable": kerbPortTable,
       "kerbPortEntry": kerbPortEntry,
       "kerbPortIndex": kerbPortIndex,
       "kerbPortStatus": kerbPortStatus,
       "kerbServerPort": kerbServerPort,
       "xPortSecurity": xPortSecurity,
       "psEntryNumber": psEntryNumber,
       "psEntryNumberLimit": psEntryNumberLimit,
       "psEntryInvalidIndex": psEntryInvalidIndex,
       "psPortTable": psPortTable,
       "psPortEntry": psPortEntry,
       "psPortIndex": psPortIndex,
       "psPortDefaultInboundAccess": psPortDefaultInboundAccess,
       "psPortDefaultOutboundAccess": psPortDefaultOutboundAccess,
       "psClrInternetSecurity": psClrInternetSecurity,
       "psTable": psTable,
       "psEntry": psEntry,
       "psEntryIndex": psEntryIndex,
       "psEntryStatus": psEntryStatus,
       "psEntryAddress": psEntryAddress,
       "psEntryMask": psEntryMask,
       "psEntryAccess": psEntryAccess,
       "psEntryDirection": psEntryDirection,
       "psEntryPortMap": psEntryPortMap,
       "xXremote": xXremote,
       "xremoteServerName1": xremoteServerName1,
       "xremoteServerName2": xremoteServerName2,
       "xremoteServerAccess1": xremoteServerAccess1,
       "xremoteServerAccessFailed1": xremoteServerAccessFailed1,
       "xremoteServerAccess2": xremoteServerAccess2,
       "xremoteServerAccessFailed2": xremoteServerAccessFailed2,
       "xremoteSessions": xremoteSessions,
       "xremotePortTable": xremotePortTable,
       "xremotePortEntry": xremotePortEntry,
       "xremotePortIndex": xremotePortIndex,
       "xremotePortXremote": xremotePortXremote,
       "xremotePortXdmQuery": xremotePortXdmQuery,
       "xremotePortXdmHost": xremotePortXdmHost,
       "xremoteServerClients": xremoteServerClients,
       "xRotary": xRotary,
       "rotaryNumber": rotaryNumber,
       "rotaryTable": rotaryTable,
       "rotaryEntry": rotaryEntry,
       "rotaryAddress": rotaryAddress,
       "rotaryStatus": rotaryStatus,
       "rotaryPortMap": rotaryPortMap,
       "xEgp": xEgp,
       "egpRouting": egpRouting,
       "egpStatus": egpStatus,
       "egpNbrTable": egpNbrTable,
       "egpNbrEntry": egpNbrEntry,
       "egpNbrAddr": egpNbrAddr,
       "egpNbrIntervalDead": egpNbrIntervalDead,
       "egpNbrStatus": egpNbrStatus,
       "xOspf": xOspf,
       "ospfAutoConfigure": ospfAutoConfigure,
       "ospfStatus": ospfStatus,
       "ospfIfMtrcTable": ospfIfMtrcTable,
       "ospfIfMtrcEntry": ospfIfMtrcEntry,
       "ospfIfMtrcIpAddress": ospfIfMtrcIpAddress,
       "ospfIfMtrcAddressLessIf": ospfIfMtrcAddressLessIf,
       "ospfIfMtrcTos": ospfIfMtrcTos,
       "ospfIfMtrcCostActual": ospfIfMtrcCostActual,
       "ospfXIfTable": ospfXIfTable,
       "ospfXIfEntry": ospfXIfEntry,
       "ospfXIfIpAddress": ospfXIfIpAddress,
       "ospfXIfAddressLessIf": ospfXIfAddressLessIf,
       "ospfXIfTypeActual": ospfXIfTypeActual,
       "ospfXIfStatus": ospfXIfStatus,
       "ospfXAreaTable": ospfXAreaTable,
       "ospfXAreaEntry": ospfXAreaEntry,
       "ospfXAreaId": ospfXAreaId,
       "ospfXAreaStatus": ospfXAreaStatus,
       "xRouterIp": xRouterIp,
       "ipAdExtTable": ipAdExtTable,
       "ipAdExtEntry": ipAdExtEntry,
       "ipAdEntExtAddress": ipAdEntExtAddress,
       "ipAdEntExtProxyArp": ipAdEntExtProxyArp,
       "ipAdEntExtRip": ipAdEntExtRip,
       "ipRouterIfTable": ipRouterIfTable,
       "ipRouterIfEntry": ipRouterIfEntry,
       "ipRouterIfIndex": ipRouterIfIndex,
       "ipRouterIfProtocolPriority": ipRouterIfProtocolPriority,
       "ipRouterIfMTU": ipRouterIfMTU,
       "ipRouterIfRDP": ipRouterIfRDP,
       "ipRouterIfArpPacketsIn": ipRouterIfArpPacketsIn,
       "ipRouterIfArpPacketsOut": ipRouterIfArpPacketsOut,
       "ipRouterIfPacketsIn": ipRouterIfPacketsIn,
       "ipRouterIfPacketsOut": ipRouterIfPacketsOut,
       "ipRouterIfForwardsIn": ipRouterIfForwardsIn,
       "ipRouterIfForwardsOut": ipRouterIfForwardsOut,
       "xIpTraffic": xIpTraffic,
       "ipTrafficSort": ipTrafficSort,
       "ipTrafficTable": ipTrafficTable,
       "ipTrafficEntry": ipTrafficEntry,
       "ipTrafficIndex": ipTrafficIndex,
       "ipTrafficPercent": ipTrafficPercent,
       "ipTrafficDstAddr": ipTrafficDstAddr,
       "ipTrafficSrcAddr": ipTrafficSrcAddr,
       "ipTrafficProtocol": ipTrafficProtocol,
       "ipTrafficDstPort": ipTrafficDstPort,
       "ipTrafficSrcPort": ipTrafficSrcPort,
       "ipTrafficIf": ipTrafficIf,
       "ipTrafficMonitoring": ipTrafficMonitoring,
       "xIpNetToMediaTable": xIpNetToMediaTable,
       "xIpNetToMediaEntry": xIpNetToMediaEntry,
       "xIpNetToMediaCircuit": xIpNetToMediaCircuit,
       "xIpNetToMediaReverseArp": xIpNetToMediaReverseArp,
       "xRouterUdp": xRouterUdp,
       "udpBcstServerTable": udpBcstServerTable,
       "udpBcstServerEntry": udpBcstServerEntry,
       "udpBcstServerAddress": udpBcstServerAddress,
       "udpBcstServerStatus": udpBcstServerStatus,
       "udpBcstPortTable": udpBcstPortTable,
       "udpBcstPortEntry": udpBcstPortEntry,
       "udpBcstPort": udpBcstPort,
       "udpBcstPortStatus": udpBcstPortStatus,
       "udpBcstRouting": udpBcstRouting,
       "xRouterPolicy": xRouterPolicy,
       "xImport": xImport,
       "impEgpRuleTable": impEgpRuleTable,
       "impEgpRuleEntry": impEgpRuleEntry,
       "impEgpRuleAs": impEgpRuleAs,
       "impEgpRuleNetwork": impEgpRuleNetwork,
       "impEgpRuleAction": impEgpRuleAction,
       "impEgpRulePreference": impEgpRulePreference,
       "impEgpRuleType": impEgpRuleType,
       "impEgpRuleMetricAction": impEgpRuleMetricAction,
       "impEgpRuleMetric": impEgpRuleMetric,
       "impEgpRuleStatus": impEgpRuleStatus,
       "impOspfRuleTable": impOspfRuleTable,
       "impOspfRuleEntry": impOspfRuleEntry,
       "impOspfRuleNetwork": impOspfRuleNetwork,
       "impOspfRulePreference": impOspfRulePreference,
       "impOspfRuleStatus": impOspfRuleStatus,
       "impRipRuleTable": impRipRuleTable,
       "impRipRuleEntry": impRipRuleEntry,
       "impRipRuleFromIf": impRipRuleFromIf,
       "impRipRuleNetwork": impRipRuleNetwork,
       "impRipRuleAction": impRipRuleAction,
       "impRipRulePreference": impRipRulePreference,
       "impRipRuleType": impRipRuleType,
       "impRipRuleMetricAction": impRipRuleMetricAction,
       "impRipRuleMetric": impRipRuleMetric,
       "impRipRuleStatus": impRipRuleStatus,
       "impIsisRuleTable": impIsisRuleTable,
       "impIsisRuleEntry": impIsisRuleEntry,
       "impIsisRuleNetwork": impIsisRuleNetwork,
       "impIsisRuleAction": impIsisRuleAction,
       "impIsisRulePreference": impIsisRulePreference,
       "impIsisRuleType": impIsisRuleType,
       "impIsisRuleMetricAction": impIsisRuleMetricAction,
       "impIsisRuleMetric": impIsisRuleMetric,
       "impIsisRuleStatus": impIsisRuleStatus,
       "xExport": xExport,
       "expEgpToEgpRuleTable": expEgpToEgpRuleTable,
       "expEgpToEgpRuleEntry": expEgpToEgpRuleEntry,
       "expEgpToEgpRuleToAs": expEgpToEgpRuleToAs,
       "expEgpToEgpRuleNetwork": expEgpToEgpRuleNetwork,
       "expEgpToEgpRuleFromAs": expEgpToEgpRuleFromAs,
       "expEgpToEgpRuleAction": expEgpToEgpRuleAction,
       "expEgpToEgpRuleMetricAction": expEgpToEgpRuleMetricAction,
       "expEgpToEgpRuleMetric": expEgpToEgpRuleMetric,
       "expEgpToEgpRuleStatus": expEgpToEgpRuleStatus,
       "expOspfToEgpRuleTable": expOspfToEgpRuleTable,
       "expOspfToEgpRuleEntry": expOspfToEgpRuleEntry,
       "expOspfToEgpRuleToAs": expOspfToEgpRuleToAs,
       "expOspfToEgpRuleNetwork": expOspfToEgpRuleNetwork,
       "expOspfToEgpRuleFromAs": expOspfToEgpRuleFromAs,
       "expOspfToEgpRuleAction": expOspfToEgpRuleAction,
       "expOspfToEgpRuleMetricAction": expOspfToEgpRuleMetricAction,
       "expOspfToEgpRuleMetric": expOspfToEgpRuleMetric,
       "expOspfToEgpRuleStatus": expOspfToEgpRuleStatus,
       "expStaticToEgpRuleTable": expStaticToEgpRuleTable,
       "expStaticToEgpRuleEntry": expStaticToEgpRuleEntry,
       "expStaticToEgpRuleToAs": expStaticToEgpRuleToAs,
       "expStaticToEgpRuleNetwork": expStaticToEgpRuleNetwork,
       "expStaticToEgpRuleAction": expStaticToEgpRuleAction,
       "expStaticToEgpRuleMetricAction": expStaticToEgpRuleMetricAction,
       "expStaticToEgpRuleMetric": expStaticToEgpRuleMetric,
       "expStaticToEgpRuleStatus": expStaticToEgpRuleStatus,
       "expEgpToOspfRuleTable": expEgpToOspfRuleTable,
       "expEgpToOspfRuleEntry": expEgpToOspfRuleEntry,
       "expEgpToOspfRuleNetwork": expEgpToOspfRuleNetwork,
       "expEgpToOspfRuleFromAs": expEgpToOspfRuleFromAs,
       "expEgpToOspfRuleAction": expEgpToOspfRuleAction,
       "expEgpToOspfRuleStatus": expEgpToOspfRuleStatus,
       "expRipToEgpRuleTable": expRipToEgpRuleTable,
       "expRipToEgpRuleEntry": expRipToEgpRuleEntry,
       "expRipToEgpRuleToAs": expRipToEgpRuleToAs,
       "expRipToEgpRuleNetwork": expRipToEgpRuleNetwork,
       "expRipToEgpRuleAction": expRipToEgpRuleAction,
       "expRipToEgpRuleMetricAction": expRipToEgpRuleMetricAction,
       "expRipToEgpRuleMetric": expRipToEgpRuleMetric,
       "expRipToEgpRuleStatus": expRipToEgpRuleStatus,
       "expRipToOspfRuleTable": expRipToOspfRuleTable,
       "expRipToOspfRuleEntry": expRipToOspfRuleEntry,
       "expRipToOspfRuleNetwork": expRipToOspfRuleNetwork,
       "expRipToOspfRuleAction": expRipToOspfRuleAction,
       "expRipToOspfRuleStatus": expRipToOspfRuleStatus,
       "expEgpToRipRuleTable": expEgpToRipRuleTable,
       "expEgpToRipRuleEntry": expEgpToRipRuleEntry,
       "expEgpToRipRuleToIf": expEgpToRipRuleToIf,
       "expEgpToRipRuleNetwork": expEgpToRipRuleNetwork,
       "expEgpToRipRuleFromAs": expEgpToRipRuleFromAs,
       "expEgpToRipRuleAction": expEgpToRipRuleAction,
       "expEgpToRipRuleMetricAction": expEgpToRipRuleMetricAction,
       "expEgpToRipRuleMetric": expEgpToRipRuleMetric,
       "expEgpToRipRuleStatus": expEgpToRipRuleStatus,
       "expOspfToRipRuleTable": expOspfToRipRuleTable,
       "expOspfToRipRuleEntry": expOspfToRipRuleEntry,
       "expOspfToRipRuleToIf": expOspfToRipRuleToIf,
       "expOspfToRipRuleNetwork": expOspfToRipRuleNetwork,
       "expOspfToRipRuleFromAs": expOspfToRipRuleFromAs,
       "expOspfToRipRuleAction": expOspfToRipRuleAction,
       "expOspfToRipRuleMetricAction": expOspfToRipRuleMetricAction,
       "expOspfToRipRuleMetric": expOspfToRipRuleMetric,
       "expOspfToRipRuleStatus": expOspfToRipRuleStatus,
       "expRipToRipRuleTable": expRipToRipRuleTable,
       "expRipToRipRuleEntry": expRipToRipRuleEntry,
       "expRipToRipRuleToIf": expRipToRipRuleToIf,
       "expRipToRipRuleNetwork": expRipToRipRuleNetwork,
       "expRipToRipRuleAction": expRipToRipRuleAction,
       "expRipToRipRuleMetricAction": expRipToRipRuleMetricAction,
       "expRipToRipRuleMetric": expRipToRipRuleMetric,
       "expRipToRipRuleStatus": expRipToRipRuleStatus,
       "expStaticToRipRuleTable": expStaticToRipRuleTable,
       "expStaticToRipRuleEntry": expStaticToRipRuleEntry,
       "expStaticToRipRuleToIf": expStaticToRipRuleToIf,
       "expStaticToRipRuleNetwork": expStaticToRipRuleNetwork,
       "expStaticToRipRuleAction": expStaticToRipRuleAction,
       "expStaticToRipRuleMetricAction": expStaticToRipRuleMetricAction,
       "expStaticToRipRuleMetric": expStaticToRipRuleMetric,
       "expStaticToRipRuleStatus": expStaticToRipRuleStatus,
       "expIsisToEgpRuleTable": expIsisToEgpRuleTable,
       "expIsisToEgpRuleEntry": expIsisToEgpRuleEntry,
       "expIsisToEgpRuleToAs": expIsisToEgpRuleToAs,
       "expIsisToEgpRuleNetwork": expIsisToEgpRuleNetwork,
       "expIsisToEgpRuleAction": expIsisToEgpRuleAction,
       "expIsisToEgpRuleMetricAction": expIsisToEgpRuleMetricAction,
       "expIsisToEgpRuleMetric": expIsisToEgpRuleMetric,
       "expIsisToEgpRuleStatus": expIsisToEgpRuleStatus,
       "expIsisToOspfRuleTable": expIsisToOspfRuleTable,
       "expIsisToOspfRuleEntry": expIsisToOspfRuleEntry,
       "expIsisToOspfRuleNetwork": expIsisToOspfRuleNetwork,
       "expIsisToOspfRuleAction": expIsisToOspfRuleAction,
       "expIsisToOspfRuleStatus": expIsisToOspfRuleStatus,
       "expIsisToRipRuleTable": expIsisToRipRuleTable,
       "expIsisToRipRuleEntry": expIsisToRipRuleEntry,
       "expIsisToRipRuleToIf": expIsisToRipRuleToIf,
       "expIsisToRipRuleNetwork": expIsisToRipRuleNetwork,
       "expIsisToRipRuleAction": expIsisToRipRuleAction,
       "expIsisToRipRuleMetricAction": expIsisToRipRuleMetricAction,
       "expIsisToRipRuleMetric": expIsisToRipRuleMetric,
       "expIsisToRipRuleStatus": expIsisToRipRuleStatus,
       "expEgpToIsisRuleTable": expEgpToIsisRuleTable,
       "expEgpToIsisRuleEntry": expEgpToIsisRuleEntry,
       "expEgpToIsisRuleNetwork": expEgpToIsisRuleNetwork,
       "expEgpToIsisRuleFromAs": expEgpToIsisRuleFromAs,
       "expEgpToIsisRuleAction": expEgpToIsisRuleAction,
       "expEgpToIsisRuleMetricType": expEgpToIsisRuleMetricType,
       "expEgpToIsisRuleDefaultMetricAction": expEgpToIsisRuleDefaultMetricAction,
       "expEgpToIsisRuleDefaultMetric": expEgpToIsisRuleDefaultMetric,
       "expEgpToIsisRuleDelayMetricAction": expEgpToIsisRuleDelayMetricAction,
       "expEgpToIsisRuleDelayMetric": expEgpToIsisRuleDelayMetric,
       "expEgpToIsisRuleErrorMetricAction": expEgpToIsisRuleErrorMetricAction,
       "expEgpToIsisRuleErrorMetric": expEgpToIsisRuleErrorMetric,
       "expEgpToIsisRuleExpenseMetricAction": expEgpToIsisRuleExpenseMetricAction,
       "expEgpToIsisRuleExpenseMetric": expEgpToIsisRuleExpenseMetric,
       "expEgpToIsisRuleStatus": expEgpToIsisRuleStatus,
       "expOspfToIsisRuleTable": expOspfToIsisRuleTable,
       "expOspfToIsisRuleEntry": expOspfToIsisRuleEntry,
       "expOspfToIsisRuleNetwork": expOspfToIsisRuleNetwork,
       "expOspfToIsisRuleFromAs": expOspfToIsisRuleFromAs,
       "expOspfToIsisRuleAction": expOspfToIsisRuleAction,
       "expOspfToIsisRuleMetricType": expOspfToIsisRuleMetricType,
       "expOspfToIsisRuleDefaultMetricAction": expOspfToIsisRuleDefaultMetricAction,
       "expOspfToIsisRuleDefaultMetric": expOspfToIsisRuleDefaultMetric,
       "expOspfToIsisRuleDelayMetricAction": expOspfToIsisRuleDelayMetricAction,
       "expOspfToIsisRuleDelayMetric": expOspfToIsisRuleDelayMetric,
       "expOspfToIsisRuleErrorMetricAction": expOspfToIsisRuleErrorMetricAction,
       "expOspfToIsisRuleErrorMetric": expOspfToIsisRuleErrorMetric,
       "expOspfToIsisRuleExpenseMetricAction": expOspfToIsisRuleExpenseMetricAction,
       "expOspfToIsisRuleExpenseMetric": expOspfToIsisRuleExpenseMetric,
       "expOspfToIsisRuleStatus": expOspfToIsisRuleStatus,
       "expRipToIsisRuleTable": expRipToIsisRuleTable,
       "expRipToIsisRuleEntry": expRipToIsisRuleEntry,
       "expRipToIsisRuleNetwork": expRipToIsisRuleNetwork,
       "expRipToIsisRuleAction": expRipToIsisRuleAction,
       "expRipToIsisRuleMetricType": expRipToIsisRuleMetricType,
       "expRipToIsisRuleDefaultMetricAction": expRipToIsisRuleDefaultMetricAction,
       "expRipToIsisRuleDefaultMetric": expRipToIsisRuleDefaultMetric,
       "expRipToIsisRuleDelayMetricAction": expRipToIsisRuleDelayMetricAction,
       "expRipToIsisRuleDelayMetric": expRipToIsisRuleDelayMetric,
       "expRipToIsisRuleErrorMetricAction": expRipToIsisRuleErrorMetricAction,
       "expRipToIsisRuleErrorMetric": expRipToIsisRuleErrorMetric,
       "expRipToIsisRuleExpenseMetricAction": expRipToIsisRuleExpenseMetricAction,
       "expRipToIsisRuleExpenseMetric": expRipToIsisRuleExpenseMetric,
       "expRipToIsisRuleStatus": expRipToIsisRuleStatus,
       "expStaticToIsisRuleTable": expStaticToIsisRuleTable,
       "expStaticToIsisRuleEntry": expStaticToIsisRuleEntry,
       "expStaticToIsisRuleNetwork": expStaticToIsisRuleNetwork,
       "expStaticToIsisRuleAction": expStaticToIsisRuleAction,
       "expStaticToIsisRuleMetricType": expStaticToIsisRuleMetricType,
       "expStaticToIsisRuleDefaultMetricAction": expStaticToIsisRuleDefaultMetricAction,
       "expStaticToIsisRuleDefaultMetric": expStaticToIsisRuleDefaultMetric,
       "expStaticToIsisRuleDelayMetricAction": expStaticToIsisRuleDelayMetricAction,
       "expStaticToIsisRuleDelayMetric": expStaticToIsisRuleDelayMetric,
       "expStaticToIsisRuleErrorMetricAction": expStaticToIsisRuleErrorMetricAction,
       "expStaticToIsisRuleErrorMetric": expStaticToIsisRuleErrorMetric,
       "expStaticToIsisRuleExpenseMetricAction": expStaticToIsisRuleExpenseMetricAction,
       "expStaticToIsisRuleExpenseMetric": expStaticToIsisRuleExpenseMetric,
       "expStaticToIsisRuleStatus": expStaticToIsisRuleStatus,
       "xFilter": xFilter,
       "ipIfFilterTable": ipIfFilterTable,
       "ipIfFilterEntry": ipIfFilterEntry,
       "ipIfFilterIndex": ipIfFilterIndex,
       "ipIfFilterDstAddr": ipIfFilterDstAddr,
       "ipIfFilterDstMask": ipIfFilterDstMask,
       "ipIfFilterSrcAddr": ipIfFilterSrcAddr,
       "ipIfFilterSrcMask": ipIfFilterSrcMask,
       "ipIfFilterProtocol": ipIfFilterProtocol,
       "ipIfFilterDstPort": ipIfFilterDstPort,
       "ipIfFilterSrcPort": ipIfFilterSrcPort,
       "ipIfFilterAction": ipIfFilterAction,
       "ipIfFilterStatus": ipIfFilterStatus,
       "ipFilterState": ipFilterState,
       "ipIfFilter2Table": ipIfFilter2Table,
       "ipIfFilter2Entry": ipIfFilter2Entry,
       "ipIfFilter2Index": ipIfFilter2Index,
       "ipIfFilter2DstAddr": ipIfFilter2DstAddr,
       "ipIfFilter2DstMask": ipIfFilter2DstMask,
       "ipIfFilter2SrcAddr": ipIfFilter2SrcAddr,
       "ipIfFilter2SrcMask": ipIfFilter2SrcMask,
       "ipIfFilter2Protocol": ipIfFilter2Protocol,
       "ipIfFilter2DstPortStart": ipIfFilter2DstPortStart,
       "ipIfFilter2SrcPortStart": ipIfFilter2SrcPortStart,
       "ipIfFilter2Action": ipIfFilter2Action,
       "ipIfFilter2Status": ipIfFilter2Status,
       "ipIfFilter2DstPortEnd": ipIfFilter2DstPortEnd,
       "ipIfFilter2SrcPortEnd": ipIfFilter2SrcPortEnd,
       "ipIfFilter2TcpSyn": ipIfFilter2TcpSyn,
       "ipIfFilter2ProtocolPriority": ipIfFilter2ProtocolPriority,
       "xRip": xRip,
       "ripState": ripState,
       "ripStatus": ripStatus,
       "ripNetTable": ripNetTable,
       "ripNetEntry": ripNetEntry,
       "ripNetNet": ripNetNet,
       "ripNetState": ripNetState,
       "ripNetRipsIn": ripNetRipsIn,
       "ripNetRipsOut": ripNetRipsOut,
       "ripNetAlgorithm": ripNetAlgorithm,
       "xlpd": xlpd,
       "lpdQueueTable": lpdQueueTable,
       "lpdQueueEntry": lpdQueueEntry,
       "lpdQueueStatus": lpdQueueStatus,
       "lpdQueueName": lpdQueueName,
       "lpdQueuePorts": lpdQueuePorts,
       "lpdQueueEnabled": lpdQueueEnabled,
       "lpdQueueLfConversion": lpdQueueLfConversion,
       "lpdQueueTotalJobs": lpdQueueTotalJobs,
       "lpdQueueActiveJobs": lpdQueueActiveJobs,
       "lpdQueueWaitingJobs": lpdQueueWaitingJobs,
       "lpdQueueProcessedJobs": lpdQueueProcessedJobs,
       "lpdQueueFormFeed": lpdQueueFormFeed,
       "lpdQueueBypass": lpdQueueBypass,
       "lpdJobTable": lpdJobTable,
       "lpdJobEntry": lpdJobEntry,
       "lpdJobStatus": lpdJobStatus,
       "lpdJobNumber": lpdJobNumber,
       "lpdJobAssignedPort": lpdJobAssignedPort,
       "lpdJobFileSize": lpdJobFileSize,
       "lpdJobHostName": lpdJobHostName,
       "lpdJobFileName": lpdJobFileName,
       "lpdJobState": lpdJobState,
       "xSecurID": xSecurID,
       "securIDServerName0": securIDServerName0,
       "securIDServerName1": securIDServerName1,
       "securIDServerName2": securIDServerName2,
       "securIDServerName3": securIDServerName3,
       "securIDServerName4": securIDServerName4,
       "securIDMaxRetries": securIDMaxRetries,
       "securIDBaseTimeout": securIDBaseTimeout,
       "securIDPort": securIDPort,
       "securIDQueryLimit": securIDQueryLimit,
       "securIDEncryptionMode": securIDEncryptionMode,
       "securIDInsecureLogins": securIDInsecureLogins,
       "securIDSecureLogins": securIDSecureLogins,
       "securIDSecureLoginsFailed": securIDSecureLoginsFailed,
       "securIDServerAccess0": securIDServerAccess0,
       "securIDServerAccessFailed0": securIDServerAccessFailed0,
       "securIDServerAccess1": securIDServerAccess1,
       "securIDServerAccessFailed1": securIDServerAccessFailed1,
       "securIDServerAccess2": securIDServerAccess2,
       "securIDServerAccessFailed2": securIDServerAccessFailed2,
       "securIDServerAccess3": securIDServerAccess3,
       "securIDServerAccessFailed3": securIDServerAccessFailed3,
       "securIDServerAccess4": securIDServerAccess4,
       "securIDServerAccessFailed4": securIDServerAccessFailed4,
       "securIDErrorPortIndex": securIDErrorPortIndex,
       "securIDError": securIDError,
       "securIDErrorUsername": securIDErrorUsername,
       "securIDPortTable": securIDPortTable,
       "securIDPortEntry": securIDPortEntry,
       "securIDPortIndex": securIDPortIndex,
       "securIDPortStatus": securIDPortStatus,
       "xSsh": xSsh,
       "sshPortTable": sshPortTable,
       "sshPortEntry": sshPortEntry,
       "sshPortIndex": sshPortIndex,
       "sshPortIncomingTcpPort": sshPortIncomingTcpPort,
       "sshPortNewlineFiltering": sshPortNewlineFiltering,
       "sshPortNewline": sshPortNewline,
       "sshPortTransmitBufferedTime": sshPortTransmitBufferedTime,
       "sshPortRemoteProtocol": sshPortRemoteProtocol,
       "sshPortBreakSequence": sshPortBreakSequence,
       "sshCipherMask": sshCipherMask,
       "sshAuthenticationTimeout": sshAuthenticationTimeout,
       "sshHostKeyLength": sshHostKeyLength,
       "sshHostKeyGenerate": sshHostKeyGenerate,
       "sshServerKeyLength": sshServerKeyLength,
       "sshServerKeyTtl": sshServerKeyTtl,
       "sshServerMaxBufferSize": sshServerMaxBufferSize}
)
