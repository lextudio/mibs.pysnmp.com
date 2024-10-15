# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:49 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(jnxMobileGatewaySgw,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewaySgw")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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

jnxMbgSgwGtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2)
)
jnxMbgSgwGtpMib.setRevisions(
        ("2011-09-21 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSgwGtpNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSgwGtpNotifications = _JnxMbgSgwGtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 0)
)
_JnxMbgSgwGtpObjects_ObjectIdentity = ObjectIdentity
jnxMbgSgwGtpObjects = _JnxMbgSgwGtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1)
)
_JnxMbgSgwGtpCPerPeerStatsTable_Object = MibTable
jnxMbgSgwGtpCPerPeerStatsTable = _JnxMbgSgwGtpCPerPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpCPerPeerStatsTable.setStatus("current")
_JnxMbgSgwGtpPerPeerStatsEntry_Object = MibTableRow
jnxMbgSgwGtpPerPeerStatsEntry = _JnxMbgSgwGtpPerPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1)
)
jnxMbgSgwGtpPerPeerStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwPPGtpRmtAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwPPGtpLclAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwPPGtpRtgInst"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPerPeerStatsEntry.setStatus("current")
_JnxMbgSgwPPGtpRmtAddr_Type = IpAddress
_JnxMbgSgwPPGtpRmtAddr_Object = MibTableColumn
jnxMbgSgwPPGtpRmtAddr = _JnxMbgSgwPPGtpRmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 1),
    _JnxMbgSgwPPGtpRmtAddr_Type()
)
jnxMbgSgwPPGtpRmtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpRmtAddr.setStatus("current")
_JnxMbgSgwPPGtpLclAddr_Type = IpAddress
_JnxMbgSgwPPGtpLclAddr_Object = MibTableColumn
jnxMbgSgwPPGtpLclAddr = _JnxMbgSgwPPGtpLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 2),
    _JnxMbgSgwPPGtpLclAddr_Type()
)
jnxMbgSgwPPGtpLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpLclAddr.setStatus("current")
_JnxMbgSgwPPGtpRtgInst_Type = Unsigned32
_JnxMbgSgwPPGtpRtgInst_Object = MibTableColumn
jnxMbgSgwPPGtpRtgInst = _JnxMbgSgwPPGtpRtgInst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 3),
    _JnxMbgSgwPPGtpRtgInst_Type()
)
jnxMbgSgwPPGtpRtgInst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpRtgInst.setStatus("current")
_JnxMbgSgwPPRxPacketsDropped_Type = Counter64
_JnxMbgSgwPPRxPacketsDropped_Object = MibTableColumn
jnxMbgSgwPPRxPacketsDropped = _JnxMbgSgwPPRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 4),
    _JnxMbgSgwPPRxPacketsDropped_Type()
)
jnxMbgSgwPPRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPRxPacketsDropped.setStatus("current")
_JnxMbgSgwPPPacketAllocFail_Type = Counter64
_JnxMbgSgwPPPacketAllocFail_Object = MibTableColumn
jnxMbgSgwPPPacketAllocFail = _JnxMbgSgwPPPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 5),
    _JnxMbgSgwPPPacketAllocFail_Type()
)
jnxMbgSgwPPPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPPacketAllocFail.setStatus("current")
_JnxMbgSgwPPPacketSendFail_Type = Counter64
_JnxMbgSgwPPPacketSendFail_Object = MibTableColumn
jnxMbgSgwPPPacketSendFail = _JnxMbgSgwPPPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 6),
    _JnxMbgSgwPPPacketSendFail_Type()
)
jnxMbgSgwPPPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPPacketSendFail.setStatus("current")
_JnxMbgSgwPPIPVerErrRx_Type = Counter64
_JnxMbgSgwPPIPVerErrRx_Object = MibTableColumn
jnxMbgSgwPPIPVerErrRx = _JnxMbgSgwPPIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 7),
    _JnxMbgSgwPPIPVerErrRx_Type()
)
jnxMbgSgwPPIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPIPVerErrRx.setStatus("current")
_JnxMbgSgwPPIPProtoErrRx_Type = Counter64
_JnxMbgSgwPPIPProtoErrRx_Object = MibTableColumn
jnxMbgSgwPPIPProtoErrRx = _JnxMbgSgwPPIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 8),
    _JnxMbgSgwPPIPProtoErrRx_Type()
)
jnxMbgSgwPPIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPIPProtoErrRx.setStatus("current")
_JnxMbgSgwPPGTPPortErrRx_Type = Counter64
_JnxMbgSgwPPGTPPortErrRx_Object = MibTableColumn
jnxMbgSgwPPGTPPortErrRx = _JnxMbgSgwPPGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 9),
    _JnxMbgSgwPPGTPPortErrRx_Type()
)
jnxMbgSgwPPGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGTPPortErrRx.setStatus("current")
_JnxMbgSgwPPGTPUnknVerRx_Type = Counter64
_JnxMbgSgwPPGTPUnknVerRx_Object = MibTableColumn
jnxMbgSgwPPGTPUnknVerRx = _JnxMbgSgwPPGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 10),
    _JnxMbgSgwPPGTPUnknVerRx_Type()
)
jnxMbgSgwPPGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGTPUnknVerRx.setStatus("current")
_JnxMbgSgwPPPcktLenErrRx_Type = Counter64
_JnxMbgSgwPPPcktLenErrRx_Object = MibTableColumn
jnxMbgSgwPPPcktLenErrRx = _JnxMbgSgwPPPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 11),
    _JnxMbgSgwPPPcktLenErrRx_Type()
)
jnxMbgSgwPPPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPPcktLenErrRx.setStatus("current")
_JnxMbgSgwPPUnknMsgRx_Type = Counter64
_JnxMbgSgwPPUnknMsgRx_Object = MibTableColumn
jnxMbgSgwPPUnknMsgRx = _JnxMbgSgwPPUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 12),
    _JnxMbgSgwPPUnknMsgRx_Type()
)
jnxMbgSgwPPUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUnknMsgRx.setStatus("current")
_JnxMbgSgwPPProtocolErrRx_Type = Counter64
_JnxMbgSgwPPProtocolErrRx_Object = MibTableColumn
jnxMbgSgwPPProtocolErrRx = _JnxMbgSgwPPProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 13),
    _JnxMbgSgwPPProtocolErrRx_Type()
)
jnxMbgSgwPPProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPProtocolErrRx.setStatus("current")
_JnxMbgSgwPPUnSupportedMsgRx_Type = Counter64
_JnxMbgSgwPPUnSupportedMsgRx_Object = MibTableColumn
jnxMbgSgwPPUnSupportedMsgRx = _JnxMbgSgwPPUnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 14),
    _JnxMbgSgwPPUnSupportedMsgRx_Type()
)
jnxMbgSgwPPUnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUnSupportedMsgRx.setStatus("current")
_JnxMbgSgwPPT3RespTmrExpRx_Type = Counter64
_JnxMbgSgwPPT3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwPPT3RespTmrExpRx = _JnxMbgSgwPPT3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 15),
    _JnxMbgSgwPPT3RespTmrExpRx_Type()
)
jnxMbgSgwPPT3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPT3RespTmrExpRx.setStatus("current")
_JnxMbgSgwPPV2NumMsgRx_Type = Counter64
_JnxMbgSgwPPV2NumMsgRx_Object = MibTableColumn
jnxMbgSgwPPV2NumMsgRx = _JnxMbgSgwPPV2NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 16),
    _JnxMbgSgwPPV2NumMsgRx_Type()
)
jnxMbgSgwPPV2NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2NumMsgRx.setStatus("current")
_JnxMbgSgwPPV2NumMsgTx_Type = Counter64
_JnxMbgSgwPPV2NumMsgTx_Object = MibTableColumn
jnxMbgSgwPPV2NumMsgTx = _JnxMbgSgwPPV2NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 17),
    _JnxMbgSgwPPV2NumMsgTx_Type()
)
jnxMbgSgwPPV2NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2NumMsgTx.setStatus("current")
_JnxMbgSgwPPV2NumBytesRx_Type = Counter64
_JnxMbgSgwPPV2NumBytesRx_Object = MibTableColumn
jnxMbgSgwPPV2NumBytesRx = _JnxMbgSgwPPV2NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 18),
    _JnxMbgSgwPPV2NumBytesRx_Type()
)
jnxMbgSgwPPV2NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2NumBytesRx.setStatus("current")
_JnxMbgSgwPPV2NumBytesTx_Type = Counter64
_JnxMbgSgwPPV2NumBytesTx_Object = MibTableColumn
jnxMbgSgwPPV2NumBytesTx = _JnxMbgSgwPPV2NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 19),
    _JnxMbgSgwPPV2NumBytesTx_Type()
)
jnxMbgSgwPPV2NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2NumBytesTx.setStatus("current")
_JnxMbgSgwPPV2EchoReqRx_Type = Counter64
_JnxMbgSgwPPV2EchoReqRx_Object = MibTableColumn
jnxMbgSgwPPV2EchoReqRx = _JnxMbgSgwPPV2EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 20),
    _JnxMbgSgwPPV2EchoReqRx_Type()
)
jnxMbgSgwPPV2EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2EchoReqRx.setStatus("current")
_JnxMbgSgwPPV2EchoReqTx_Type = Counter64
_JnxMbgSgwPPV2EchoReqTx_Object = MibTableColumn
jnxMbgSgwPPV2EchoReqTx = _JnxMbgSgwPPV2EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 21),
    _JnxMbgSgwPPV2EchoReqTx_Type()
)
jnxMbgSgwPPV2EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2EchoReqTx.setStatus("current")
_JnxMbgSgwPPV2EchoRespRx_Type = Counter64
_JnxMbgSgwPPV2EchoRespRx_Object = MibTableColumn
jnxMbgSgwPPV2EchoRespRx = _JnxMbgSgwPPV2EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 22),
    _JnxMbgSgwPPV2EchoRespRx_Type()
)
jnxMbgSgwPPV2EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2EchoRespRx.setStatus("current")
_JnxMbgSgwPPV2EchoRespTx_Type = Counter64
_JnxMbgSgwPPV2EchoRespTx_Object = MibTableColumn
jnxMbgSgwPPV2EchoRespTx = _JnxMbgSgwPPV2EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 23),
    _JnxMbgSgwPPV2EchoRespTx_Type()
)
jnxMbgSgwPPV2EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2EchoRespTx.setStatus("current")
_JnxMbgSgwPPV2VerNotSupRx_Type = Counter64
_JnxMbgSgwPPV2VerNotSupRx_Object = MibTableColumn
jnxMbgSgwPPV2VerNotSupRx = _JnxMbgSgwPPV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 24),
    _JnxMbgSgwPPV2VerNotSupRx_Type()
)
jnxMbgSgwPPV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2VerNotSupRx.setStatus("current")
_JnxMbgSgwPPV2VerNotSupTx_Type = Counter64
_JnxMbgSgwPPV2VerNotSupTx_Object = MibTableColumn
jnxMbgSgwPPV2VerNotSupTx = _JnxMbgSgwPPV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 25),
    _JnxMbgSgwPPV2VerNotSupTx_Type()
)
jnxMbgSgwPPV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPV2VerNotSupTx.setStatus("current")
_JnxMbgSgwPPCreateSessReqRx_Type = Counter64
_JnxMbgSgwPPCreateSessReqRx_Object = MibTableColumn
jnxMbgSgwPPCreateSessReqRx = _JnxMbgSgwPPCreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 26),
    _JnxMbgSgwPPCreateSessReqRx_Type()
)
jnxMbgSgwPPCreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCreateSessReqRx.setStatus("current")
_JnxMbgSgwPPCreateSessReqTx_Type = Counter64
_JnxMbgSgwPPCreateSessReqTx_Object = MibTableColumn
jnxMbgSgwPPCreateSessReqTx = _JnxMbgSgwPPCreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 27),
    _JnxMbgSgwPPCreateSessReqTx_Type()
)
jnxMbgSgwPPCreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCreateSessReqTx.setStatus("current")
_JnxMbgSgwPPCreateSessRspRx_Type = Counter64
_JnxMbgSgwPPCreateSessRspRx_Object = MibTableColumn
jnxMbgSgwPPCreateSessRspRx = _JnxMbgSgwPPCreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 28),
    _JnxMbgSgwPPCreateSessRspRx_Type()
)
jnxMbgSgwPPCreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCreateSessRspRx.setStatus("current")
_JnxMbgSgwPPCreateSessRspTx_Type = Counter64
_JnxMbgSgwPPCreateSessRspTx_Object = MibTableColumn
jnxMbgSgwPPCreateSessRspTx = _JnxMbgSgwPPCreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 29),
    _JnxMbgSgwPPCreateSessRspTx_Type()
)
jnxMbgSgwPPCreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCreateSessRspTx.setStatus("current")
_JnxMbgSgwPPModBrReqRx_Type = Counter64
_JnxMbgSgwPPModBrReqRx_Object = MibTableColumn
jnxMbgSgwPPModBrReqRx = _JnxMbgSgwPPModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 30),
    _JnxMbgSgwPPModBrReqRx_Type()
)
jnxMbgSgwPPModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrReqRx.setStatus("current")
_JnxMbgSgwPPModBrReqTx_Type = Counter64
_JnxMbgSgwPPModBrReqTx_Object = MibTableColumn
jnxMbgSgwPPModBrReqTx = _JnxMbgSgwPPModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 31),
    _JnxMbgSgwPPModBrReqTx_Type()
)
jnxMbgSgwPPModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrReqTx.setStatus("current")
_JnxMbgSgwPPModBrRspRx_Type = Counter64
_JnxMbgSgwPPModBrRspRx_Object = MibTableColumn
jnxMbgSgwPPModBrRspRx = _JnxMbgSgwPPModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 32),
    _JnxMbgSgwPPModBrRspRx_Type()
)
jnxMbgSgwPPModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrRspRx.setStatus("current")
_JnxMbgSgwPPModBrRspTx_Type = Counter64
_JnxMbgSgwPPModBrRspTx_Object = MibTableColumn
jnxMbgSgwPPModBrRspTx = _JnxMbgSgwPPModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 33),
    _JnxMbgSgwPPModBrRspTx_Type()
)
jnxMbgSgwPPModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrRspTx.setStatus("current")
_JnxMbgSgwPPDelSessReqRx_Type = Counter64
_JnxMbgSgwPPDelSessReqRx_Object = MibTableColumn
jnxMbgSgwPPDelSessReqRx = _JnxMbgSgwPPDelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 34),
    _JnxMbgSgwPPDelSessReqRx_Type()
)
jnxMbgSgwPPDelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelSessReqRx.setStatus("current")
_JnxMbgSgwPPDelSessReqTx_Type = Counter64
_JnxMbgSgwPPDelSessReqTx_Object = MibTableColumn
jnxMbgSgwPPDelSessReqTx = _JnxMbgSgwPPDelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 35),
    _JnxMbgSgwPPDelSessReqTx_Type()
)
jnxMbgSgwPPDelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelSessReqTx.setStatus("current")
_JnxMbgSgwPPDelSessRspRx_Type = Counter64
_JnxMbgSgwPPDelSessRspRx_Object = MibTableColumn
jnxMbgSgwPPDelSessRspRx = _JnxMbgSgwPPDelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 36),
    _JnxMbgSgwPPDelSessRspRx_Type()
)
jnxMbgSgwPPDelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelSessRspRx.setStatus("current")
_JnxMbgSgwPPDelSessRspTx_Type = Counter64
_JnxMbgSgwPPDelSessRspTx_Object = MibTableColumn
jnxMbgSgwPPDelSessRspTx = _JnxMbgSgwPPDelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 37),
    _JnxMbgSgwPPDelSessRspTx_Type()
)
jnxMbgSgwPPDelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelSessRspTx.setStatus("current")
_JnxMbgSgwPPCrtBrReqRx_Type = Counter64
_JnxMbgSgwPPCrtBrReqRx_Object = MibTableColumn
jnxMbgSgwPPCrtBrReqRx = _JnxMbgSgwPPCrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 38),
    _JnxMbgSgwPPCrtBrReqRx_Type()
)
jnxMbgSgwPPCrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrtBrReqRx.setStatus("current")
_JnxMbgSgwPPCrtBrReqTx_Type = Counter64
_JnxMbgSgwPPCrtBrReqTx_Object = MibTableColumn
jnxMbgSgwPPCrtBrReqTx = _JnxMbgSgwPPCrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 39),
    _JnxMbgSgwPPCrtBrReqTx_Type()
)
jnxMbgSgwPPCrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrtBrReqTx.setStatus("current")
_JnxMbgSgwPPCrtBrRspRx_Type = Counter64
_JnxMbgSgwPPCrtBrRspRx_Object = MibTableColumn
jnxMbgSgwPPCrtBrRspRx = _JnxMbgSgwPPCrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 40),
    _JnxMbgSgwPPCrtBrRspRx_Type()
)
jnxMbgSgwPPCrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrtBrRspRx.setStatus("current")
_JnxMbgSgwPPCrtBrRspTx_Type = Counter64
_JnxMbgSgwPPCrtBrRspTx_Object = MibTableColumn
jnxMbgSgwPPCrtBrRspTx = _JnxMbgSgwPPCrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 41),
    _JnxMbgSgwPPCrtBrRspTx_Type()
)
jnxMbgSgwPPCrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrtBrRspTx.setStatus("current")
_JnxMbgSgwPPUpdBrReqRx_Type = Counter64
_JnxMbgSgwPPUpdBrReqRx_Object = MibTableColumn
jnxMbgSgwPPUpdBrReqRx = _JnxMbgSgwPPUpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 42),
    _JnxMbgSgwPPUpdBrReqRx_Type()
)
jnxMbgSgwPPUpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdBrReqRx.setStatus("current")
_JnxMbgSgwPPUpdBrReqTx_Type = Counter64
_JnxMbgSgwPPUpdBrReqTx_Object = MibTableColumn
jnxMbgSgwPPUpdBrReqTx = _JnxMbgSgwPPUpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 43),
    _JnxMbgSgwPPUpdBrReqTx_Type()
)
jnxMbgSgwPPUpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdBrReqTx.setStatus("current")
_JnxMbgSgwPPUpdBrRspRx_Type = Counter64
_JnxMbgSgwPPUpdBrRspRx_Object = MibTableColumn
jnxMbgSgwPPUpdBrRspRx = _JnxMbgSgwPPUpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 44),
    _JnxMbgSgwPPUpdBrRspRx_Type()
)
jnxMbgSgwPPUpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdBrRspRx.setStatus("current")
_JnxMbgSgwPPUpdBrRspTx_Type = Counter64
_JnxMbgSgwPPUpdBrRspTx_Object = MibTableColumn
jnxMbgSgwPPUpdBrRspTx = _JnxMbgSgwPPUpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 45),
    _JnxMbgSgwPPUpdBrRspTx_Type()
)
jnxMbgSgwPPUpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdBrRspTx.setStatus("current")
_JnxMbgSgwPPDelBrReqRx_Type = Counter64
_JnxMbgSgwPPDelBrReqRx_Object = MibTableColumn
jnxMbgSgwPPDelBrReqRx = _JnxMbgSgwPPDelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 46),
    _JnxMbgSgwPPDelBrReqRx_Type()
)
jnxMbgSgwPPDelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrReqRx.setStatus("current")
_JnxMbgSgwPPDelBrReqTx_Type = Counter64
_JnxMbgSgwPPDelBrReqTx_Object = MibTableColumn
jnxMbgSgwPPDelBrReqTx = _JnxMbgSgwPPDelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 47),
    _JnxMbgSgwPPDelBrReqTx_Type()
)
jnxMbgSgwPPDelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrReqTx.setStatus("current")
_JnxMbgSgwPPDelBrRspRx_Type = Counter64
_JnxMbgSgwPPDelBrRspRx_Object = MibTableColumn
jnxMbgSgwPPDelBrRspRx = _JnxMbgSgwPPDelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 48),
    _JnxMbgSgwPPDelBrRspRx_Type()
)
jnxMbgSgwPPDelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrRspRx.setStatus("current")
_JnxMbgSgwPPDelBrRspTx_Type = Counter64
_JnxMbgSgwPPDelBrRspTx_Object = MibTableColumn
jnxMbgSgwPPDelBrRspTx = _JnxMbgSgwPPDelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 49),
    _JnxMbgSgwPPDelBrRspTx_Type()
)
jnxMbgSgwPPDelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrRspTx.setStatus("current")
_JnxMbgSgwPPDelConnSetReqRx_Type = Counter64
_JnxMbgSgwPPDelConnSetReqRx_Object = MibTableColumn
jnxMbgSgwPPDelConnSetReqRx = _JnxMbgSgwPPDelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 50),
    _JnxMbgSgwPPDelConnSetReqRx_Type()
)
jnxMbgSgwPPDelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelConnSetReqRx.setStatus("current")
_JnxMbgSgwPPDelConnSetReqTx_Type = Counter64
_JnxMbgSgwPPDelConnSetReqTx_Object = MibTableColumn
jnxMbgSgwPPDelConnSetReqTx = _JnxMbgSgwPPDelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 51),
    _JnxMbgSgwPPDelConnSetReqTx_Type()
)
jnxMbgSgwPPDelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelConnSetReqTx.setStatus("current")
_JnxMbgSgwPPDelConnSetRspRx_Type = Counter64
_JnxMbgSgwPPDelConnSetRspRx_Object = MibTableColumn
jnxMbgSgwPPDelConnSetRspRx = _JnxMbgSgwPPDelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 52),
    _JnxMbgSgwPPDelConnSetRspRx_Type()
)
jnxMbgSgwPPDelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelConnSetRspRx.setStatus("current")
_JnxMbgSgwPPDelConnSetRspTx_Type = Counter64
_JnxMbgSgwPPDelConnSetRspTx_Object = MibTableColumn
jnxMbgSgwPPDelConnSetRspTx = _JnxMbgSgwPPDelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 53),
    _JnxMbgSgwPPDelConnSetRspTx_Type()
)
jnxMbgSgwPPDelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelConnSetRspTx.setStatus("current")
_JnxMbgSgwPPUpdConnSetReqRx_Type = Counter64
_JnxMbgSgwPPUpdConnSetReqRx_Object = MibTableColumn
jnxMbgSgwPPUpdConnSetReqRx = _JnxMbgSgwPPUpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 54),
    _JnxMbgSgwPPUpdConnSetReqRx_Type()
)
jnxMbgSgwPPUpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdConnSetReqRx.setStatus("current")
_JnxMbgSgwPPUpdConnSetReqTx_Type = Counter64
_JnxMbgSgwPPUpdConnSetReqTx_Object = MibTableColumn
jnxMbgSgwPPUpdConnSetReqTx = _JnxMbgSgwPPUpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 55),
    _JnxMbgSgwPPUpdConnSetReqTx_Type()
)
jnxMbgSgwPPUpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdConnSetReqTx.setStatus("current")
_JnxMbgSgwPPUpdConnSetRspRx_Type = Counter64
_JnxMbgSgwPPUpdConnSetRspRx_Object = MibTableColumn
jnxMbgSgwPPUpdConnSetRspRx = _JnxMbgSgwPPUpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 56),
    _JnxMbgSgwPPUpdConnSetRspRx_Type()
)
jnxMbgSgwPPUpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdConnSetRspRx.setStatus("current")
_JnxMbgSgwPPUpdConnSetRspTx_Type = Counter64
_JnxMbgSgwPPUpdConnSetRspTx_Object = MibTableColumn
jnxMbgSgwPPUpdConnSetRspTx = _JnxMbgSgwPPUpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 57),
    _JnxMbgSgwPPUpdConnSetRspTx_Type()
)
jnxMbgSgwPPUpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPUpdConnSetRspTx.setStatus("current")
_JnxMbgSgwPPModBrCmdRx_Type = Counter64
_JnxMbgSgwPPModBrCmdRx_Object = MibTableColumn
jnxMbgSgwPPModBrCmdRx = _JnxMbgSgwPPModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 58),
    _JnxMbgSgwPPModBrCmdRx_Type()
)
jnxMbgSgwPPModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrCmdRx.setStatus("current")
_JnxMbgSgwPPModBrCmdTx_Type = Counter64
_JnxMbgSgwPPModBrCmdTx_Object = MibTableColumn
jnxMbgSgwPPModBrCmdTx = _JnxMbgSgwPPModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 59),
    _JnxMbgSgwPPModBrCmdTx_Type()
)
jnxMbgSgwPPModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrCmdTx.setStatus("current")
_JnxMbgSgwPPModBrFlrIndRx_Type = Counter64
_JnxMbgSgwPPModBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwPPModBrFlrIndRx = _JnxMbgSgwPPModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 60),
    _JnxMbgSgwPPModBrFlrIndRx_Type()
)
jnxMbgSgwPPModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrFlrIndRx.setStatus("current")
_JnxMbgSgwPPModBrFlrIndTx_Type = Counter64
_JnxMbgSgwPPModBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwPPModBrFlrIndTx = _JnxMbgSgwPPModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 61),
    _JnxMbgSgwPPModBrFlrIndTx_Type()
)
jnxMbgSgwPPModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPModBrFlrIndTx.setStatus("current")
_JnxMbgSgwPPDelBrCmdRx_Type = Counter64
_JnxMbgSgwPPDelBrCmdRx_Object = MibTableColumn
jnxMbgSgwPPDelBrCmdRx = _JnxMbgSgwPPDelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 62),
    _JnxMbgSgwPPDelBrCmdRx_Type()
)
jnxMbgSgwPPDelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrCmdRx.setStatus("current")
_JnxMbgSgwPPDelBrCmdTx_Type = Counter64
_JnxMbgSgwPPDelBrCmdTx_Object = MibTableColumn
jnxMbgSgwPPDelBrCmdTx = _JnxMbgSgwPPDelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 63),
    _JnxMbgSgwPPDelBrCmdTx_Type()
)
jnxMbgSgwPPDelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrCmdTx.setStatus("current")
_JnxMbgSgwPPDelBrFlrIndRx_Type = Counter64
_JnxMbgSgwPPDelBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwPPDelBrFlrIndRx = _JnxMbgSgwPPDelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 64),
    _JnxMbgSgwPPDelBrFlrIndRx_Type()
)
jnxMbgSgwPPDelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrFlrIndRx.setStatus("current")
_JnxMbgSgwPPDelBrFlrIndTx_Type = Counter64
_JnxMbgSgwPPDelBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwPPDelBrFlrIndTx = _JnxMbgSgwPPDelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 65),
    _JnxMbgSgwPPDelBrFlrIndTx_Type()
)
jnxMbgSgwPPDelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelBrFlrIndTx.setStatus("current")
_JnxMbgSgwPPBrResCmdRx_Type = Counter64
_JnxMbgSgwPPBrResCmdRx_Object = MibTableColumn
jnxMbgSgwPPBrResCmdRx = _JnxMbgSgwPPBrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 66),
    _JnxMbgSgwPPBrResCmdRx_Type()
)
jnxMbgSgwPPBrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPBrResCmdRx.setStatus("current")
_JnxMbgSgwPPBrResCmdTx_Type = Counter64
_JnxMbgSgwPPBrResCmdTx_Object = MibTableColumn
jnxMbgSgwPPBrResCmdTx = _JnxMbgSgwPPBrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 67),
    _JnxMbgSgwPPBrResCmdTx_Type()
)
jnxMbgSgwPPBrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPBrResCmdTx.setStatus("current")
_JnxMbgSgwPPBrResFlrIndRx_Type = Counter64
_JnxMbgSgwPPBrResFlrIndRx_Object = MibTableColumn
jnxMbgSgwPPBrResFlrIndRx = _JnxMbgSgwPPBrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 68),
    _JnxMbgSgwPPBrResFlrIndRx_Type()
)
jnxMbgSgwPPBrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPBrResFlrIndRx.setStatus("current")
_JnxMbgSgwPPBrResFlrIndTx_Type = Counter64
_JnxMbgSgwPPBrResFlrIndTx_Object = MibTableColumn
jnxMbgSgwPPBrResFlrIndTx = _JnxMbgSgwPPBrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 69),
    _JnxMbgSgwPPBrResFlrIndTx_Type()
)
jnxMbgSgwPPBrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPBrResFlrIndTx.setStatus("current")
_JnxMbgSgwPPRelAcsBrReqRx_Type = Counter64
_JnxMbgSgwPPRelAcsBrReqRx_Object = MibTableColumn
jnxMbgSgwPPRelAcsBrReqRx = _JnxMbgSgwPPRelAcsBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 70),
    _JnxMbgSgwPPRelAcsBrReqRx_Type()
)
jnxMbgSgwPPRelAcsBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPRelAcsBrReqRx.setStatus("current")
_JnxMbgSgwPPRelAcsBrReqTx_Type = Counter64
_JnxMbgSgwPPRelAcsBrReqTx_Object = MibTableColumn
jnxMbgSgwPPRelAcsBrReqTx = _JnxMbgSgwPPRelAcsBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 71),
    _JnxMbgSgwPPRelAcsBrReqTx_Type()
)
jnxMbgSgwPPRelAcsBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPRelAcsBrReqTx.setStatus("current")
_JnxMbgSgwPPRelAcsBrRespRx_Type = Counter64
_JnxMbgSgwPPRelAcsBrRespRx_Object = MibTableColumn
jnxMbgSgwPPRelAcsBrRespRx = _JnxMbgSgwPPRelAcsBrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 72),
    _JnxMbgSgwPPRelAcsBrRespRx_Type()
)
jnxMbgSgwPPRelAcsBrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPRelAcsBrRespRx.setStatus("current")
_JnxMbgSgwPPRelAcsBrRespTx_Type = Counter64
_JnxMbgSgwPPRelAcsBrRespTx_Object = MibTableColumn
jnxMbgSgwPPRelAcsBrRespTx = _JnxMbgSgwPPRelAcsBrRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 73),
    _JnxMbgSgwPPRelAcsBrRespTx_Type()
)
jnxMbgSgwPPRelAcsBrRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPRelAcsBrRespTx.setStatus("current")
_JnxMbgSgwPPCrIndTunReqRx_Type = Counter64
_JnxMbgSgwPPCrIndTunReqRx_Object = MibTableColumn
jnxMbgSgwPPCrIndTunReqRx = _JnxMbgSgwPPCrIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 74),
    _JnxMbgSgwPPCrIndTunReqRx_Type()
)
jnxMbgSgwPPCrIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrIndTunReqRx.setStatus("current")
_JnxMbgSgwPPCrIndTunReqTx_Type = Counter64
_JnxMbgSgwPPCrIndTunReqTx_Object = MibTableColumn
jnxMbgSgwPPCrIndTunReqTx = _JnxMbgSgwPPCrIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 75),
    _JnxMbgSgwPPCrIndTunReqTx_Type()
)
jnxMbgSgwPPCrIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrIndTunReqTx.setStatus("current")
_JnxMbgSgwPPCrIndTunRespRx_Type = Counter64
_JnxMbgSgwPPCrIndTunRespRx_Object = MibTableColumn
jnxMbgSgwPPCrIndTunRespRx = _JnxMbgSgwPPCrIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 76),
    _JnxMbgSgwPPCrIndTunRespRx_Type()
)
jnxMbgSgwPPCrIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrIndTunRespRx.setStatus("current")
_JnxMbgSgwPPCrIndTunRespTx_Type = Counter64
_JnxMbgSgwPPCrIndTunRespTx_Object = MibTableColumn
jnxMbgSgwPPCrIndTunRespTx = _JnxMbgSgwPPCrIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 77),
    _JnxMbgSgwPPCrIndTunRespTx_Type()
)
jnxMbgSgwPPCrIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPCrIndTunRespTx.setStatus("current")
_JnxMbgSgwPPDelIndTunReqRx_Type = Counter64
_JnxMbgSgwPPDelIndTunReqRx_Object = MibTableColumn
jnxMbgSgwPPDelIndTunReqRx = _JnxMbgSgwPPDelIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 78),
    _JnxMbgSgwPPDelIndTunReqRx_Type()
)
jnxMbgSgwPPDelIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelIndTunReqRx.setStatus("current")
_JnxMbgSgwPPDelIndTunReqTx_Type = Counter64
_JnxMbgSgwPPDelIndTunReqTx_Object = MibTableColumn
jnxMbgSgwPPDelIndTunReqTx = _JnxMbgSgwPPDelIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 79),
    _JnxMbgSgwPPDelIndTunReqTx_Type()
)
jnxMbgSgwPPDelIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelIndTunReqTx.setStatus("current")
_JnxMbgSgwPPDelIndTunRespRx_Type = Counter64
_JnxMbgSgwPPDelIndTunRespRx_Object = MibTableColumn
jnxMbgSgwPPDelIndTunRespRx = _JnxMbgSgwPPDelIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 80),
    _JnxMbgSgwPPDelIndTunRespRx_Type()
)
jnxMbgSgwPPDelIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelIndTunRespRx.setStatus("current")
_JnxMbgSgwPPDelIndTunRespTx_Type = Counter64
_JnxMbgSgwPPDelIndTunRespTx_Object = MibTableColumn
jnxMbgSgwPPDelIndTunRespTx = _JnxMbgSgwPPDelIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 81),
    _JnxMbgSgwPPDelIndTunRespTx_Type()
)
jnxMbgSgwPPDelIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDelIndTunRespTx.setStatus("current")
_JnxMbgSgwPPDlDataNotifRx_Type = Counter64
_JnxMbgSgwPPDlDataNotifRx_Object = MibTableColumn
jnxMbgSgwPPDlDataNotifRx = _JnxMbgSgwPPDlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 82),
    _JnxMbgSgwPPDlDataNotifRx_Type()
)
jnxMbgSgwPPDlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataNotifRx.setStatus("current")
_JnxMbgSgwPPDlDataNotifTx_Type = Counter64
_JnxMbgSgwPPDlDataNotifTx_Object = MibTableColumn
jnxMbgSgwPPDlDataNotifTx = _JnxMbgSgwPPDlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 83),
    _JnxMbgSgwPPDlDataNotifTx_Type()
)
jnxMbgSgwPPDlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataNotifTx.setStatus("current")
_JnxMbgSgwPPDlDataAckRx_Type = Counter64
_JnxMbgSgwPPDlDataAckRx_Object = MibTableColumn
jnxMbgSgwPPDlDataAckRx = _JnxMbgSgwPPDlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 84),
    _JnxMbgSgwPPDlDataAckRx_Type()
)
jnxMbgSgwPPDlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataAckRx.setStatus("current")
_JnxMbgSgwPPDlDataAckTx_Type = Counter64
_JnxMbgSgwPPDlDataAckTx_Object = MibTableColumn
jnxMbgSgwPPDlDataAckTx = _JnxMbgSgwPPDlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 85),
    _JnxMbgSgwPPDlDataAckTx_Type()
)
jnxMbgSgwPPDlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataAckTx.setStatus("current")
_JnxMbgSgwPPDlDataNotiFlrIndRx_Type = Counter64
_JnxMbgSgwPPDlDataNotiFlrIndRx_Object = MibTableColumn
jnxMbgSgwPPDlDataNotiFlrIndRx = _JnxMbgSgwPPDlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 86),
    _JnxMbgSgwPPDlDataNotiFlrIndRx_Type()
)
jnxMbgSgwPPDlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataNotiFlrIndRx.setStatus("current")
_JnxMbgSgwPPDlDataNotiFlrIndTx_Type = Counter64
_JnxMbgSgwPPDlDataNotiFlrIndTx_Object = MibTableColumn
jnxMbgSgwPPDlDataNotiFlrIndTx = _JnxMbgSgwPPDlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 87),
    _JnxMbgSgwPPDlDataNotiFlrIndTx_Type()
)
jnxMbgSgwPPDlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPDlDataNotiFlrIndTx.setStatus("current")
_JnxMbgSgwPPStopPagingIndRx_Type = Counter64
_JnxMbgSgwPPStopPagingIndRx_Object = MibTableColumn
jnxMbgSgwPPStopPagingIndRx = _JnxMbgSgwPPStopPagingIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 88),
    _JnxMbgSgwPPStopPagingIndRx_Type()
)
jnxMbgSgwPPStopPagingIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPStopPagingIndRx.setStatus("current")
_JnxMbgSgwPPStopPagingIndTx_Type = Counter64
_JnxMbgSgwPPStopPagingIndTx_Object = MibTableColumn
jnxMbgSgwPPStopPagingIndTx = _JnxMbgSgwPPStopPagingIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 89),
    _JnxMbgSgwPPStopPagingIndTx_Type()
)
jnxMbgSgwPPStopPagingIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPStopPagingIndTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPageRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPageRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPageRx = _JnxMbgSgwPPGtpV2ICsPageRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 90),
    _JnxMbgSgwPPGtpV2ICsPageRx_Type()
)
jnxMbgSgwPPGtpV2ICsPageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPageRx.setStatus("obsolete")
_JnxMbgSgwPPGtpV2ICsPageTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPageTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPageTx = _JnxMbgSgwPPGtpV2ICsPageTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 91),
    _JnxMbgSgwPPGtpV2ICsPageTx_Type()
)
jnxMbgSgwPPGtpV2ICsPageTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPageTx.setStatus("obsolete")
_JnxMbgSgwPPGtpV2ICsReqAcceptRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsReqAcceptRx = _JnxMbgSgwPPGtpV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 92),
    _JnxMbgSgwPPGtpV2ICsReqAcceptRx_Type()
)
jnxMbgSgwPPGtpV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsReqAcceptRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsReqAcceptTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsReqAcceptTx = _JnxMbgSgwPPGtpV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 93),
    _JnxMbgSgwPPGtpV2ICsReqAcceptTx_Type()
)
jnxMbgSgwPPGtpV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsReqAcceptTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAcceptPartRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAcceptPartRx = _JnxMbgSgwPPGtpV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 94),
    _JnxMbgSgwPPGtpV2ICsAcceptPartRx_Type()
)
jnxMbgSgwPPGtpV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAcceptPartRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAcceptPartTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAcceptPartTx = _JnxMbgSgwPPGtpV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 95),
    _JnxMbgSgwPPGtpV2ICsAcceptPartTx_Type()
)
jnxMbgSgwPPGtpV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAcceptPartTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNewPTNPrefRx = _JnxMbgSgwPPGtpV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 96),
    _JnxMbgSgwPPGtpV2ICsNewPTNPrefRx_Type()
)
jnxMbgSgwPPGtpV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNewPTNPrefTx = _JnxMbgSgwPPGtpV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 97),
    _JnxMbgSgwPPGtpV2ICsNewPTNPrefTx_Type()
)
jnxMbgSgwPPGtpV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNPTSIAdbrRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNPTSIAdbrRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNPTSIAdbrRx = _JnxMbgSgwPPGtpV2ICsNPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 98),
    _JnxMbgSgwPPGtpV2ICsNPTSIAdbrRx_Type()
)
jnxMbgSgwPPGtpV2ICsNPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNPTSIAdbrRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNPTSIAdbrTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNPTSIAdbrTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNPTSIAdbrTx = _JnxMbgSgwPPGtpV2ICsNPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 99),
    _JnxMbgSgwPPGtpV2ICsNPTSIAdbrTx_Type()
)
jnxMbgSgwPPGtpV2ICsNPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNPTSIAdbrTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCtxNotFndRx = _JnxMbgSgwPPGtpV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 100),
    _JnxMbgSgwPPGtpV2ICsCtxNotFndRx_Type()
)
jnxMbgSgwPPGtpV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCtxNotFndTx = _JnxMbgSgwPPGtpV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 101),
    _JnxMbgSgwPPGtpV2ICsCtxNotFndTx_Type()
)
jnxMbgSgwPPGtpV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvMsgFmtRx = _JnxMbgSgwPPGtpV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 102),
    _JnxMbgSgwPPGtpV2ICsInvMsgFmtRx_Type()
)
jnxMbgSgwPPGtpV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvMsgFmtTx = _JnxMbgSgwPPGtpV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 103),
    _JnxMbgSgwPPGtpV2ICsInvMsgFmtTx_Type()
)
jnxMbgSgwPPGtpV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsVerNotSuppRx = _JnxMbgSgwPPGtpV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 104),
    _JnxMbgSgwPPGtpV2ICsVerNotSuppRx_Type()
)
jnxMbgSgwPPGtpV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsVerNotSuppTx = _JnxMbgSgwPPGtpV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 105),
    _JnxMbgSgwPPGtpV2ICsVerNotSuppTx_Type()
)
jnxMbgSgwPPGtpV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvLenRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvLenRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvLenRx = _JnxMbgSgwPPGtpV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 106),
    _JnxMbgSgwPPGtpV2ICsInvLenRx_Type()
)
jnxMbgSgwPPGtpV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvLenRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvLenTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvLenTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvLenTx = _JnxMbgSgwPPGtpV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 107),
    _JnxMbgSgwPPGtpV2ICsInvLenTx_Type()
)
jnxMbgSgwPPGtpV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvLenTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsServNotSupRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsServNotSupRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsServNotSupRx = _JnxMbgSgwPPGtpV2ICsServNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 108),
    _JnxMbgSgwPPGtpV2ICsServNotSupRx_Type()
)
jnxMbgSgwPPGtpV2ICsServNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsServNotSupRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsServNotSupTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsServNotSupTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsServNotSupTx = _JnxMbgSgwPPGtpV2ICsServNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 109),
    _JnxMbgSgwPPGtpV2ICsServNotSupTx_Type()
)
jnxMbgSgwPPGtpV2ICsServNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsServNotSupTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsManIEIncorRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsManIEIncorRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsManIEIncorRx = _JnxMbgSgwPPGtpV2ICsManIEIncorRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 110),
    _JnxMbgSgwPPGtpV2ICsManIEIncorRx_Type()
)
jnxMbgSgwPPGtpV2ICsManIEIncorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsManIEIncorRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsManIEIncorTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsManIEIncorTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsManIEIncorTx = _JnxMbgSgwPPGtpV2ICsManIEIncorTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 111),
    _JnxMbgSgwPPGtpV2ICsManIEIncorTx_Type()
)
jnxMbgSgwPPGtpV2ICsManIEIncorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsManIEIncorTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsManIEMissRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsManIEMissRx = _JnxMbgSgwPPGtpV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 112),
    _JnxMbgSgwPPGtpV2ICsManIEMissRx_Type()
)
jnxMbgSgwPPGtpV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsManIEMissRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsManIEMissTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsManIEMissTx = _JnxMbgSgwPPGtpV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 113),
    _JnxMbgSgwPPGtpV2ICsManIEMissTx_Type()
)
jnxMbgSgwPPGtpV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsManIEMissTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsOptIEIncorRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsOptIEIncorRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsOptIEIncorRx = _JnxMbgSgwPPGtpV2ICsOptIEIncorRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 114),
    _JnxMbgSgwPPGtpV2ICsOptIEIncorRx_Type()
)
jnxMbgSgwPPGtpV2ICsOptIEIncorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsOptIEIncorRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsOptIEIncorTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsOptIEIncorTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsOptIEIncorTx = _JnxMbgSgwPPGtpV2ICsOptIEIncorTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 115),
    _JnxMbgSgwPPGtpV2ICsOptIEIncorTx_Type()
)
jnxMbgSgwPPGtpV2ICsOptIEIncorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsOptIEIncorTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSysFailRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSysFailRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSysFailRx = _JnxMbgSgwPPGtpV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 116),
    _JnxMbgSgwPPGtpV2ICsSysFailRx_Type()
)
jnxMbgSgwPPGtpV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSysFailRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSysFailTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSysFailTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSysFailTx = _JnxMbgSgwPPGtpV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 117),
    _JnxMbgSgwPPGtpV2ICsSysFailTx_Type()
)
jnxMbgSgwPPGtpV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSysFailTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNoResRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNoResRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNoResRx = _JnxMbgSgwPPGtpV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 118),
    _JnxMbgSgwPPGtpV2ICsNoResRx_Type()
)
jnxMbgSgwPPGtpV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNoResRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNoResTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNoResTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNoResTx = _JnxMbgSgwPPGtpV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 119),
    _JnxMbgSgwPPGtpV2ICsNoResTx_Type()
)
jnxMbgSgwPPGtpV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNoResTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsTFTSMANTErRx = _JnxMbgSgwPPGtpV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 120),
    _JnxMbgSgwPPGtpV2ICsTFTSMANTErRx_Type()
)
jnxMbgSgwPPGtpV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsTFTSMANTErTx = _JnxMbgSgwPPGtpV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 121),
    _JnxMbgSgwPPGtpV2ICsTFTSMANTErTx_Type()
)
jnxMbgSgwPPGtpV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsTFTSysErrRx = _JnxMbgSgwPPGtpV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 122),
    _JnxMbgSgwPPGtpV2ICsTFTSysErrRx_Type()
)
jnxMbgSgwPPGtpV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsTFTSysErrTx = _JnxMbgSgwPPGtpV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 123),
    _JnxMbgSgwPPGtpV2ICsTFTSysErrTx_Type()
)
jnxMbgSgwPPGtpV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPkFltManErRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPkFltManErRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPkFltManErRx = _JnxMbgSgwPPGtpV2ICsPkFltManErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 124),
    _JnxMbgSgwPPGtpV2ICsPkFltManErRx_Type()
)
jnxMbgSgwPPGtpV2ICsPkFltManErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPkFltManErRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPkFltManErTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPkFltManErTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPkFltManErTx = _JnxMbgSgwPPGtpV2ICsPkFltManErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 125),
    _JnxMbgSgwPPGtpV2ICsPkFltManErTx_Type()
)
jnxMbgSgwPPGtpV2ICsPkFltManErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPkFltManErTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPkFltSynErRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPkFltSynErRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPkFltSynErRx = _JnxMbgSgwPPGtpV2ICsPkFltSynErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 126),
    _JnxMbgSgwPPGtpV2ICsPkFltSynErRx_Type()
)
jnxMbgSgwPPGtpV2ICsPkFltSynErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPkFltSynErRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPkFltSynErTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPkFltSynErTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPkFltSynErTx = _JnxMbgSgwPPGtpV2ICsPkFltSynErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 127),
    _JnxMbgSgwPPGtpV2ICsPkFltSynErTx_Type()
)
jnxMbgSgwPPGtpV2ICsPkFltSynErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPkFltSynErTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsMisUnknAPNRx = _JnxMbgSgwPPGtpV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 128),
    _JnxMbgSgwPPGtpV2ICsMisUnknAPNRx_Type()
)
jnxMbgSgwPPGtpV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsMisUnknAPNTx = _JnxMbgSgwPPGtpV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 129),
    _JnxMbgSgwPPGtpV2ICsMisUnknAPNTx_Type()
)
jnxMbgSgwPPGtpV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnexpRptIERx = _JnxMbgSgwPPGtpV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 130),
    _JnxMbgSgwPPGtpV2ICsUnexpRptIERx_Type()
)
jnxMbgSgwPPGtpV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnexpRptIETx = _JnxMbgSgwPPGtpV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 131),
    _JnxMbgSgwPPGtpV2ICsUnexpRptIETx_Type()
)
jnxMbgSgwPPGtpV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsGREKeyNtFdRx = _JnxMbgSgwPPGtpV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 132),
    _JnxMbgSgwPPGtpV2ICsGREKeyNtFdRx_Type()
)
jnxMbgSgwPPGtpV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsGREKeyNtFdTx = _JnxMbgSgwPPGtpV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 133),
    _JnxMbgSgwPPGtpV2ICsGREKeyNtFdTx_Type()
)
jnxMbgSgwPPGtpV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRelocFailRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRelocFailRx = _JnxMbgSgwPPGtpV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 134),
    _JnxMbgSgwPPGtpV2ICsRelocFailRx_Type()
)
jnxMbgSgwPPGtpV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRelocFailRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRelocFailTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRelocFailTx = _JnxMbgSgwPPGtpV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 135),
    _JnxMbgSgwPPGtpV2ICsRelocFailTx_Type()
)
jnxMbgSgwPPGtpV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRelocFailTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsDenINRatRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsDenINRatRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsDenINRatRx = _JnxMbgSgwPPGtpV2ICsDenINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 136),
    _JnxMbgSgwPPGtpV2ICsDenINRatRx_Type()
)
jnxMbgSgwPPGtpV2ICsDenINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsDenINRatRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsDenINRatTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsDenINRatTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsDenINRatTx = _JnxMbgSgwPPGtpV2ICsDenINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 137),
    _JnxMbgSgwPPGtpV2ICsDenINRatTx_Type()
)
jnxMbgSgwPPGtpV2ICsDenINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsDenINRatTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPTNotSuppRx = _JnxMbgSgwPPGtpV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 138),
    _JnxMbgSgwPPGtpV2ICsPTNotSuppRx_Type()
)
jnxMbgSgwPPGtpV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPTNotSuppTx = _JnxMbgSgwPPGtpV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 139),
    _JnxMbgSgwPPGtpV2ICsPTNotSuppTx_Type()
)
jnxMbgSgwPPGtpV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAllDynAdOcRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAllDynAdOcRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAllDynAdOcRx = _JnxMbgSgwPPGtpV2ICsAllDynAdOcRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 140),
    _JnxMbgSgwPPGtpV2ICsAllDynAdOcRx_Type()
)
jnxMbgSgwPPGtpV2ICsAllDynAdOcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAllDynAdOcRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAllDynAdOcTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAllDynAdOcTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAllDynAdOcTx = _JnxMbgSgwPPGtpV2ICsAllDynAdOcTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 141),
    _JnxMbgSgwPPGtpV2ICsAllDynAdOcTx_Type()
)
jnxMbgSgwPPGtpV2ICsAllDynAdOcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAllDynAdOcTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNOTFTUECTXRx = _JnxMbgSgwPPGtpV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 142),
    _JnxMbgSgwPPGtpV2ICsNOTFTUECTXRx_Type()
)
jnxMbgSgwPPGtpV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNOTFTUECTXTx = _JnxMbgSgwPPGtpV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 143),
    _JnxMbgSgwPPGtpV2ICsNOTFTUECTXTx_Type()
)
jnxMbgSgwPPGtpV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsProtoNtSupRx = _JnxMbgSgwPPGtpV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 144),
    _JnxMbgSgwPPGtpV2ICsProtoNtSupRx_Type()
)
jnxMbgSgwPPGtpV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsProtoNtSupTx = _JnxMbgSgwPPGtpV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 145),
    _JnxMbgSgwPPGtpV2ICsProtoNtSupTx_Type()
)
jnxMbgSgwPPGtpV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUENotRespRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUENotRespRx = _JnxMbgSgwPPGtpV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 146),
    _JnxMbgSgwPPGtpV2ICsUENotRespRx_Type()
)
jnxMbgSgwPPGtpV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUENotRespRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUENotRespTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUENotRespTx = _JnxMbgSgwPPGtpV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 147),
    _JnxMbgSgwPPGtpV2ICsUENotRespTx_Type()
)
jnxMbgSgwPPGtpV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUENotRespTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUERefusesRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUERefusesRx = _JnxMbgSgwPPGtpV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 148),
    _JnxMbgSgwPPGtpV2ICsUERefusesRx_Type()
)
jnxMbgSgwPPGtpV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUERefusesRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUERefusesTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUERefusesTx = _JnxMbgSgwPPGtpV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 149),
    _JnxMbgSgwPPGtpV2ICsUERefusesTx_Type()
)
jnxMbgSgwPPGtpV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUERefusesTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsServDeniedRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsServDeniedRx = _JnxMbgSgwPPGtpV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 150),
    _JnxMbgSgwPPGtpV2ICsServDeniedRx_Type()
)
jnxMbgSgwPPGtpV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsServDeniedRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsServDeniedTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsServDeniedTx = _JnxMbgSgwPPGtpV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 151),
    _JnxMbgSgwPPGtpV2ICsServDeniedTx_Type()
)
jnxMbgSgwPPGtpV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsServDeniedTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnabPageUERx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnabPageUERx = _JnxMbgSgwPPGtpV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 152),
    _JnxMbgSgwPPGtpV2ICsUnabPageUERx_Type()
)
jnxMbgSgwPPGtpV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnabPageUERx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnabPageUETx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnabPageUETx = _JnxMbgSgwPPGtpV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 153),
    _JnxMbgSgwPPGtpV2ICsUnabPageUETx_Type()
)
jnxMbgSgwPPGtpV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnabPageUETx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNoMemRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNoMemRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNoMemRx = _JnxMbgSgwPPGtpV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 154),
    _JnxMbgSgwPPGtpV2ICsNoMemRx_Type()
)
jnxMbgSgwPPGtpV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNoMemRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsNoMemTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsNoMemTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsNoMemTx = _JnxMbgSgwPPGtpV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 155),
    _JnxMbgSgwPPGtpV2ICsNoMemTx_Type()
)
jnxMbgSgwPPGtpV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsNoMemTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUserAUTHFlRx = _JnxMbgSgwPPGtpV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 156),
    _JnxMbgSgwPPGtpV2ICsUserAUTHFlRx_Type()
)
jnxMbgSgwPPGtpV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUserAUTHFlTx = _JnxMbgSgwPPGtpV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 157),
    _JnxMbgSgwPPGtpV2ICsUserAUTHFlTx_Type()
)
jnxMbgSgwPPGtpV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAPNAcsDenRx = _JnxMbgSgwPPGtpV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 158),
    _JnxMbgSgwPPGtpV2ICsAPNAcsDenRx_Type()
)
jnxMbgSgwPPGtpV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAPNAcsDenTx = _JnxMbgSgwPPGtpV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 159),
    _JnxMbgSgwPPGtpV2ICsAPNAcsDenTx_Type()
)
jnxMbgSgwPPGtpV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsReqRejRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsReqRejRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsReqRejRx = _JnxMbgSgwPPGtpV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 160),
    _JnxMbgSgwPPGtpV2ICsReqRejRx_Type()
)
jnxMbgSgwPPGtpV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsReqRejRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsReqRejTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsReqRejTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsReqRejTx = _JnxMbgSgwPPGtpV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 161),
    _JnxMbgSgwPPGtpV2ICsReqRejTx_Type()
)
jnxMbgSgwPPGtpV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsReqRejTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPTMSISigMMRx = _JnxMbgSgwPPGtpV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 162),
    _JnxMbgSgwPPGtpV2ICsPTMSISigMMRx_Type()
)
jnxMbgSgwPPGtpV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsPTMSISigMMTx = _JnxMbgSgwPPGtpV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 163),
    _JnxMbgSgwPPGtpV2ICsPTMSISigMMTx_Type()
)
jnxMbgSgwPPGtpV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsIMSINotKnRx = _JnxMbgSgwPPGtpV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 164),
    _JnxMbgSgwPPGtpV2ICsIMSINotKnRx_Type()
)
jnxMbgSgwPPGtpV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsIMSINotKnTx = _JnxMbgSgwPPGtpV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 165),
    _JnxMbgSgwPPGtpV2ICsIMSINotKnTx_Type()
)
jnxMbgSgwPPGtpV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCondIEMsRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCondIEMsRx = _JnxMbgSgwPPGtpV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 166),
    _JnxMbgSgwPPGtpV2ICsCondIEMsRx_Type()
)
jnxMbgSgwPPGtpV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCondIEMsRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCondIEMsTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCondIEMsTx = _JnxMbgSgwPPGtpV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 167),
    _JnxMbgSgwPPGtpV2ICsCondIEMsTx_Type()
)
jnxMbgSgwPPGtpV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCondIEMsTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAPNResTIncRx = _JnxMbgSgwPPGtpV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 168),
    _JnxMbgSgwPPGtpV2ICsAPNResTIncRx_Type()
)
jnxMbgSgwPPGtpV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsAPNResTIncTx = _JnxMbgSgwPPGtpV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 169),
    _JnxMbgSgwPPGtpV2ICsAPNResTIncTx_Type()
)
jnxMbgSgwPPGtpV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnknownRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnknownRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnknownRx = _JnxMbgSgwPPGtpV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 170),
    _JnxMbgSgwPPGtpV2ICsUnknownRx_Type()
)
jnxMbgSgwPPGtpV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnknownRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnknownTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnknownTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnknownTx = _JnxMbgSgwPPGtpV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 171),
    _JnxMbgSgwPPGtpV2ICsUnknownTx_Type()
)
jnxMbgSgwPPGtpV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnknownTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsLclDetRx = _JnxMbgSgwPPGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 172),
    _JnxMbgSgwPPGtpV2ICsLclDetRx_Type()
)
jnxMbgSgwPPGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsLclDetTx = _JnxMbgSgwPPGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 173),
    _JnxMbgSgwPPGtpV2ICsLclDetTx_Type()
)
jnxMbgSgwPPGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCmpDetRx = _JnxMbgSgwPPGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 174),
    _JnxMbgSgwPPGtpV2ICsCmpDetRx_Type()
)
jnxMbgSgwPPGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsCmpDetTx = _JnxMbgSgwPPGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 175),
    _JnxMbgSgwPPGtpV2ICsCmpDetTx_Type()
)
jnxMbgSgwPPGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRATChgRx = _JnxMbgSgwPPGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 176),
    _JnxMbgSgwPPGtpV2ICsRATChgRx_Type()
)
jnxMbgSgwPPGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRATChgTx = _JnxMbgSgwPPGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 177),
    _JnxMbgSgwPPGtpV2ICsRATChgTx_Type()
)
jnxMbgSgwPPGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsISRDeactRx = _JnxMbgSgwPPGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 178),
    _JnxMbgSgwPPGtpV2ICsISRDeactRx_Type()
)
jnxMbgSgwPPGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsISRDeactTx = _JnxMbgSgwPPGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 179),
    _JnxMbgSgwPPGtpV2ICsISRDeactTx_Type()
)
jnxMbgSgwPPGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsEIFRNCEnRx = _JnxMbgSgwPPGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 180),
    _JnxMbgSgwPPGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgSgwPPGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsEIFRNCEnTx = _JnxMbgSgwPPGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 181),
    _JnxMbgSgwPPGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgSgwPPGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSemErTADRx = _JnxMbgSgwPPGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 182),
    _JnxMbgSgwPPGtpV2ICsSemErTADRx_Type()
)
jnxMbgSgwPPGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSemErTADTx = _JnxMbgSgwPPGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 183),
    _JnxMbgSgwPPGtpV2ICsSemErTADTx_Type()
)
jnxMbgSgwPPGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSynErTADRx = _JnxMbgSgwPPGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 184),
    _JnxMbgSgwPPGtpV2ICsSynErTADRx_Type()
)
jnxMbgSgwPPGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsSynErTADTx = _JnxMbgSgwPPGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 185),
    _JnxMbgSgwPPGtpV2ICsSynErTADTx_Type()
)
jnxMbgSgwPPGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRMValRcvRx = _JnxMbgSgwPPGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 186),
    _JnxMbgSgwPPGtpV2ICsRMValRcvRx_Type()
)
jnxMbgSgwPPGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRMValRcvTx = _JnxMbgSgwPPGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 187),
    _JnxMbgSgwPPGtpV2ICsRMValRcvTx_Type()
)
jnxMbgSgwPPGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRPrNtRspRx = _JnxMbgSgwPPGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 188),
    _JnxMbgSgwPPGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgSgwPPGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsRPrNtRspTx = _JnxMbgSgwPPGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 189),
    _JnxMbgSgwPPGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgSgwPPGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsColNWReqRx = _JnxMbgSgwPPGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 190),
    _JnxMbgSgwPPGtpV2ICsColNWReqRx_Type()
)
jnxMbgSgwPPGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsColNWReqTx = _JnxMbgSgwPPGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 191),
    _JnxMbgSgwPPGtpV2ICsColNWReqTx_Type()
)
jnxMbgSgwPPGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnPgUESusRx = _JnxMbgSgwPPGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 192),
    _JnxMbgSgwPPGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgSgwPPGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsUnPgUESusTx = _JnxMbgSgwPPGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 193),
    _JnxMbgSgwPPGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgSgwPPGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvTotLenRx = _JnxMbgSgwPPGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 194),
    _JnxMbgSgwPPGtpV2ICsInvTotLenRx_Type()
)
jnxMbgSgwPPGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvTotLenTx = _JnxMbgSgwPPGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 195),
    _JnxMbgSgwPPGtpV2ICsInvTotLenTx_Type()
)
jnxMbgSgwPPGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsDtForNtSupRx = _JnxMbgSgwPPGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 196),
    _JnxMbgSgwPPGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgSgwPPGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsDtForNtSupTx = _JnxMbgSgwPPGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 197),
    _JnxMbgSgwPPGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgSgwPPGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInReFRePrRx = _JnxMbgSgwPPGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 198),
    _JnxMbgSgwPPGtpV2ICsInReFRePrRx_Type()
)
jnxMbgSgwPPGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInReFRePrTx = _JnxMbgSgwPPGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 199),
    _JnxMbgSgwPPGtpV2ICsInReFRePrTx_Type()
)
jnxMbgSgwPPGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvPrRx = _JnxMbgSgwPPGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 200),
    _JnxMbgSgwPPGtpV2ICsInvPrRx_Type()
)
jnxMbgSgwPPGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgSgwPPGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgSgwPPGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgSgwPPGtpV2ICsInvPrTx = _JnxMbgSgwPPGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 201),
    _JnxMbgSgwPPGtpV2ICsInvPrTx_Type()
)
jnxMbgSgwPPGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgSgwPPGtpV1ProtocolErrRx_Type = Counter64
_JnxMbgSgwPPGtpV1ProtocolErrRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1ProtocolErrRx = _JnxMbgSgwPPGtpV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 202),
    _JnxMbgSgwPPGtpV1ProtocolErrRx_Type()
)
jnxMbgSgwPPGtpV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1ProtocolErrRx.setStatus("current")
_JnxMbgSgwPPGtpV1UnSupMsgRx_Type = Counter64
_JnxMbgSgwPPGtpV1UnSupMsgRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1UnSupMsgRx = _JnxMbgSgwPPGtpV1UnSupMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 203),
    _JnxMbgSgwPPGtpV1UnSupMsgRx_Type()
)
jnxMbgSgwPPGtpV1UnSupMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1UnSupMsgRx.setStatus("current")
_JnxMbgSgwPPGtpV1T3RespTmrExpRx_Type = Counter64
_JnxMbgSgwPPGtpV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1T3RespTmrExpRx = _JnxMbgSgwPPGtpV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 204),
    _JnxMbgSgwPPGtpV1T3RespTmrExpRx_Type()
)
jnxMbgSgwPPGtpV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1T3RespTmrExpRx.setStatus("current")
_JnxMbgSgwPPGtpV1EndMarkerRx_Type = Counter64
_JnxMbgSgwPPGtpV1EndMarkerRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EndMarkerRx = _JnxMbgSgwPPGtpV1EndMarkerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 205),
    _JnxMbgSgwPPGtpV1EndMarkerRx_Type()
)
jnxMbgSgwPPGtpV1EndMarkerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EndMarkerRx.setStatus("current")
_JnxMbgSgwPPGtpV1EndMarkerTx_Type = Counter64
_JnxMbgSgwPPGtpV1EndMarkerTx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EndMarkerTx = _JnxMbgSgwPPGtpV1EndMarkerTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 206),
    _JnxMbgSgwPPGtpV1EndMarkerTx_Type()
)
jnxMbgSgwPPGtpV1EndMarkerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EndMarkerTx.setStatus("current")
_JnxMbgSgwPPGtpV1EchoReqRx_Type = Counter64
_JnxMbgSgwPPGtpV1EchoReqRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EchoReqRx = _JnxMbgSgwPPGtpV1EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 207),
    _JnxMbgSgwPPGtpV1EchoReqRx_Type()
)
jnxMbgSgwPPGtpV1EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EchoReqRx.setStatus("current")
_JnxMbgSgwPPGtpV1EchoReqTx_Type = Counter64
_JnxMbgSgwPPGtpV1EchoReqTx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EchoReqTx = _JnxMbgSgwPPGtpV1EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 208),
    _JnxMbgSgwPPGtpV1EchoReqTx_Type()
)
jnxMbgSgwPPGtpV1EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EchoReqTx.setStatus("current")
_JnxMbgSgwPPGtpV1EchoRespRx_Type = Counter64
_JnxMbgSgwPPGtpV1EchoRespRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EchoRespRx = _JnxMbgSgwPPGtpV1EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 209),
    _JnxMbgSgwPPGtpV1EchoRespRx_Type()
)
jnxMbgSgwPPGtpV1EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EchoRespRx.setStatus("current")
_JnxMbgSgwPPGtpV1EchoRespTx_Type = Counter64
_JnxMbgSgwPPGtpV1EchoRespTx_Object = MibTableColumn
jnxMbgSgwPPGtpV1EchoRespTx = _JnxMbgSgwPPGtpV1EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 210),
    _JnxMbgSgwPPGtpV1EchoRespTx_Type()
)
jnxMbgSgwPPGtpV1EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1EchoRespTx.setStatus("current")
_JnxMbgSgwPPGtpV1ErrIndRx_Type = Counter64
_JnxMbgSgwPPGtpV1ErrIndRx_Object = MibTableColumn
jnxMbgSgwPPGtpV1ErrIndRx = _JnxMbgSgwPPGtpV1ErrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 211),
    _JnxMbgSgwPPGtpV1ErrIndRx_Type()
)
jnxMbgSgwPPGtpV1ErrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1ErrIndRx.setStatus("current")
_JnxMbgSgwPPGtpV1ErrIndTx_Type = Counter64
_JnxMbgSgwPPGtpV1ErrIndTx_Object = MibTableColumn
jnxMbgSgwPPGtpV1ErrIndTx = _JnxMbgSgwPPGtpV1ErrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 212),
    _JnxMbgSgwPPGtpV1ErrIndTx_Type()
)
jnxMbgSgwPPGtpV1ErrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPGtpV1ErrIndTx.setStatus("current")
_JnxMbgSgwPPSuspNotifRx_Type = Counter64
_JnxMbgSgwPPSuspNotifRx_Object = MibTableColumn
jnxMbgSgwPPSuspNotifRx = _JnxMbgSgwPPSuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 213),
    _JnxMbgSgwPPSuspNotifRx_Type()
)
jnxMbgSgwPPSuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPSuspNotifRx.setStatus("current")
_JnxMbgSgwPPSuspNotifTx_Type = Counter64
_JnxMbgSgwPPSuspNotifTx_Object = MibTableColumn
jnxMbgSgwPPSuspNotifTx = _JnxMbgSgwPPSuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 214),
    _JnxMbgSgwPPSuspNotifTx_Type()
)
jnxMbgSgwPPSuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPSuspNotifTx.setStatus("current")
_JnxMbgSgwPPSuspAckRx_Type = Counter64
_JnxMbgSgwPPSuspAckRx_Object = MibTableColumn
jnxMbgSgwPPSuspAckRx = _JnxMbgSgwPPSuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 215),
    _JnxMbgSgwPPSuspAckRx_Type()
)
jnxMbgSgwPPSuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPSuspAckRx.setStatus("current")
_JnxMbgSgwPPSuspAckTx_Type = Counter64
_JnxMbgSgwPPSuspAckTx_Object = MibTableColumn
jnxMbgSgwPPSuspAckTx = _JnxMbgSgwPPSuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 216),
    _JnxMbgSgwPPSuspAckTx_Type()
)
jnxMbgSgwPPSuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPSuspAckTx.setStatus("current")
_JnxMbgSgwPPResumeNotifRx_Type = Counter64
_JnxMbgSgwPPResumeNotifRx_Object = MibTableColumn
jnxMbgSgwPPResumeNotifRx = _JnxMbgSgwPPResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 217),
    _JnxMbgSgwPPResumeNotifRx_Type()
)
jnxMbgSgwPPResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPResumeNotifRx.setStatus("current")
_JnxMbgSgwPPResumeNotifTx_Type = Counter64
_JnxMbgSgwPPResumeNotifTx_Object = MibTableColumn
jnxMbgSgwPPResumeNotifTx = _JnxMbgSgwPPResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 218),
    _JnxMbgSgwPPResumeNotifTx_Type()
)
jnxMbgSgwPPResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPResumeNotifTx.setStatus("current")
_JnxMbgSgwPPResumeAckRx_Type = Counter64
_JnxMbgSgwPPResumeAckRx_Object = MibTableColumn
jnxMbgSgwPPResumeAckRx = _JnxMbgSgwPPResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 219),
    _JnxMbgSgwPPResumeAckRx_Type()
)
jnxMbgSgwPPResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPResumeAckRx.setStatus("current")
_JnxMbgSgwPPResumeAckTx_Type = Counter64
_JnxMbgSgwPPResumeAckTx_Object = MibTableColumn
jnxMbgSgwPPResumeAckTx = _JnxMbgSgwPPResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 220),
    _JnxMbgSgwPPResumeAckTx_Type()
)
jnxMbgSgwPPResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPResumeAckTx.setStatus("current")
_JnxMbgSgwPPPiggybackMsgRx_Type = Counter64
_JnxMbgSgwPPPiggybackMsgRx_Object = MibTableColumn
jnxMbgSgwPPPiggybackMsgRx = _JnxMbgSgwPPPiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 221),
    _JnxMbgSgwPPPiggybackMsgRx_Type()
)
jnxMbgSgwPPPiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPPiggybackMsgRx.setStatus("current")
_JnxMbgSgwPPPiggybackMsgTx_Type = Counter64
_JnxMbgSgwPPPiggybackMsgTx_Object = MibTableColumn
jnxMbgSgwPPPiggybackMsgTx = _JnxMbgSgwPPPiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 1, 1, 222),
    _JnxMbgSgwPPPiggybackMsgTx_Type()
)
jnxMbgSgwPPPiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPPPiggybackMsgTx.setStatus("current")
_JnxMbgSgwGtpCGlbStatsTable_Object = MibTable
jnxMbgSgwGtpCGlbStatsTable = _JnxMbgSgwGtpCGlbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpCGlbStatsTable.setStatus("current")
_JnxMbgSgwGtpGlbStatsEntry_Object = MibTableRow
jnxMbgSgwGtpGlbStatsEntry = _JnxMbgSgwGtpGlbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1)
)
jnxMbgSgwGtpGlbStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpGlbStatsEntry.setStatus("current")
_JnxMbgSgwRxPacketsDropped_Type = Counter64
_JnxMbgSgwRxPacketsDropped_Object = MibTableColumn
jnxMbgSgwRxPacketsDropped = _JnxMbgSgwRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 1),
    _JnxMbgSgwRxPacketsDropped_Type()
)
jnxMbgSgwRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwRxPacketsDropped.setStatus("current")
_JnxMbgSgwPacketAllocFail_Type = Counter64
_JnxMbgSgwPacketAllocFail_Object = MibTableColumn
jnxMbgSgwPacketAllocFail = _JnxMbgSgwPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 2),
    _JnxMbgSgwPacketAllocFail_Type()
)
jnxMbgSgwPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPacketAllocFail.setStatus("current")
_JnxMbgSgwPacketSendFail_Type = Counter64
_JnxMbgSgwPacketSendFail_Object = MibTableColumn
jnxMbgSgwPacketSendFail = _JnxMbgSgwPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 3),
    _JnxMbgSgwPacketSendFail_Type()
)
jnxMbgSgwPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPacketSendFail.setStatus("current")
_JnxMbgSgwIPVerErrRx_Type = Counter64
_JnxMbgSgwIPVerErrRx_Object = MibTableColumn
jnxMbgSgwIPVerErrRx = _JnxMbgSgwIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 4),
    _JnxMbgSgwIPVerErrRx_Type()
)
jnxMbgSgwIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIPVerErrRx.setStatus("current")
_JnxMbgSgwIPProtoErrRx_Type = Counter64
_JnxMbgSgwIPProtoErrRx_Object = MibTableColumn
jnxMbgSgwIPProtoErrRx = _JnxMbgSgwIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 5),
    _JnxMbgSgwIPProtoErrRx_Type()
)
jnxMbgSgwIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIPProtoErrRx.setStatus("current")
_JnxMbgSgwGTPPortErrRx_Type = Counter64
_JnxMbgSgwGTPPortErrRx_Object = MibTableColumn
jnxMbgSgwGTPPortErrRx = _JnxMbgSgwGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 6),
    _JnxMbgSgwGTPPortErrRx_Type()
)
jnxMbgSgwGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGTPPortErrRx.setStatus("current")
_JnxMbgSgwGTPUnknVerRx_Type = Counter64
_JnxMbgSgwGTPUnknVerRx_Object = MibTableColumn
jnxMbgSgwGTPUnknVerRx = _JnxMbgSgwGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 7),
    _JnxMbgSgwGTPUnknVerRx_Type()
)
jnxMbgSgwGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGTPUnknVerRx.setStatus("current")
_JnxMbgSgwPcktLenErrRx_Type = Counter64
_JnxMbgSgwPcktLenErrRx_Object = MibTableColumn
jnxMbgSgwPcktLenErrRx = _JnxMbgSgwPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 8),
    _JnxMbgSgwPcktLenErrRx_Type()
)
jnxMbgSgwPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPcktLenErrRx.setStatus("current")
_JnxMbgSgwUnknMsgRx_Type = Counter64
_JnxMbgSgwUnknMsgRx_Object = MibTableColumn
jnxMbgSgwUnknMsgRx = _JnxMbgSgwUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 9),
    _JnxMbgSgwUnknMsgRx_Type()
)
jnxMbgSgwUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUnknMsgRx.setStatus("current")
_JnxMbgSgwProtocolErrRx_Type = Counter64
_JnxMbgSgwProtocolErrRx_Object = MibTableColumn
jnxMbgSgwProtocolErrRx = _JnxMbgSgwProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 10),
    _JnxMbgSgwProtocolErrRx_Type()
)
jnxMbgSgwProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwProtocolErrRx.setStatus("current")
_JnxMbgSgwUnSupportedMsgRx_Type = Counter64
_JnxMbgSgwUnSupportedMsgRx_Object = MibTableColumn
jnxMbgSgwUnSupportedMsgRx = _JnxMbgSgwUnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 11),
    _JnxMbgSgwUnSupportedMsgRx_Type()
)
jnxMbgSgwUnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUnSupportedMsgRx.setStatus("current")
_JnxMbgSgwT3RespTmrExpRx_Type = Counter64
_JnxMbgSgwT3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwT3RespTmrExpRx = _JnxMbgSgwT3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 12),
    _JnxMbgSgwT3RespTmrExpRx_Type()
)
jnxMbgSgwT3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwT3RespTmrExpRx.setStatus("current")
_JnxMbgSgwV2NumMsgRx_Type = Counter64
_JnxMbgSgwV2NumMsgRx_Object = MibTableColumn
jnxMbgSgwV2NumMsgRx = _JnxMbgSgwV2NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 13),
    _JnxMbgSgwV2NumMsgRx_Type()
)
jnxMbgSgwV2NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2NumMsgRx.setStatus("current")
_JnxMbgSgwV2NumMsgTx_Type = Counter64
_JnxMbgSgwV2NumMsgTx_Object = MibTableColumn
jnxMbgSgwV2NumMsgTx = _JnxMbgSgwV2NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 14),
    _JnxMbgSgwV2NumMsgTx_Type()
)
jnxMbgSgwV2NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2NumMsgTx.setStatus("current")
_JnxMbgSgwV2NumBytesRx_Type = Counter64
_JnxMbgSgwV2NumBytesRx_Object = MibTableColumn
jnxMbgSgwV2NumBytesRx = _JnxMbgSgwV2NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 15),
    _JnxMbgSgwV2NumBytesRx_Type()
)
jnxMbgSgwV2NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2NumBytesRx.setStatus("current")
_JnxMbgSgwV2NumBytesTx_Type = Counter64
_JnxMbgSgwV2NumBytesTx_Object = MibTableColumn
jnxMbgSgwV2NumBytesTx = _JnxMbgSgwV2NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 16),
    _JnxMbgSgwV2NumBytesTx_Type()
)
jnxMbgSgwV2NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2NumBytesTx.setStatus("current")
_JnxMbgSgwV2EchoReqRx_Type = Counter64
_JnxMbgSgwV2EchoReqRx_Object = MibTableColumn
jnxMbgSgwV2EchoReqRx = _JnxMbgSgwV2EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 19),
    _JnxMbgSgwV2EchoReqRx_Type()
)
jnxMbgSgwV2EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2EchoReqRx.setStatus("current")
_JnxMbgSgwV2EchoReqTx_Type = Counter64
_JnxMbgSgwV2EchoReqTx_Object = MibTableColumn
jnxMbgSgwV2EchoReqTx = _JnxMbgSgwV2EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 20),
    _JnxMbgSgwV2EchoReqTx_Type()
)
jnxMbgSgwV2EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2EchoReqTx.setStatus("current")
_JnxMbgSgwV2EchoRespRx_Type = Counter64
_JnxMbgSgwV2EchoRespRx_Object = MibTableColumn
jnxMbgSgwV2EchoRespRx = _JnxMbgSgwV2EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 21),
    _JnxMbgSgwV2EchoRespRx_Type()
)
jnxMbgSgwV2EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2EchoRespRx.setStatus("current")
_JnxMbgSgwV2EchoRespTx_Type = Counter64
_JnxMbgSgwV2EchoRespTx_Object = MibTableColumn
jnxMbgSgwV2EchoRespTx = _JnxMbgSgwV2EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 22),
    _JnxMbgSgwV2EchoRespTx_Type()
)
jnxMbgSgwV2EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2EchoRespTx.setStatus("current")
_JnxMbgSgwV2VerNotSupRx_Type = Counter64
_JnxMbgSgwV2VerNotSupRx_Object = MibTableColumn
jnxMbgSgwV2VerNotSupRx = _JnxMbgSgwV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 23),
    _JnxMbgSgwV2VerNotSupRx_Type()
)
jnxMbgSgwV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2VerNotSupRx.setStatus("current")
_JnxMbgSgwV2VerNotSupTx_Type = Counter64
_JnxMbgSgwV2VerNotSupTx_Object = MibTableColumn
jnxMbgSgwV2VerNotSupTx = _JnxMbgSgwV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 24),
    _JnxMbgSgwV2VerNotSupTx_Type()
)
jnxMbgSgwV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwV2VerNotSupTx.setStatus("current")
_JnxMbgSgwCreateSessReqRx_Type = Counter64
_JnxMbgSgwCreateSessReqRx_Object = MibTableColumn
jnxMbgSgwCreateSessReqRx = _JnxMbgSgwCreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 25),
    _JnxMbgSgwCreateSessReqRx_Type()
)
jnxMbgSgwCreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCreateSessReqRx.setStatus("current")
_JnxMbgSgwCreateSessReqTx_Type = Counter64
_JnxMbgSgwCreateSessReqTx_Object = MibTableColumn
jnxMbgSgwCreateSessReqTx = _JnxMbgSgwCreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 26),
    _JnxMbgSgwCreateSessReqTx_Type()
)
jnxMbgSgwCreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCreateSessReqTx.setStatus("current")
_JnxMbgSgwCreateSessRspRx_Type = Counter64
_JnxMbgSgwCreateSessRspRx_Object = MibTableColumn
jnxMbgSgwCreateSessRspRx = _JnxMbgSgwCreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 27),
    _JnxMbgSgwCreateSessRspRx_Type()
)
jnxMbgSgwCreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCreateSessRspRx.setStatus("current")
_JnxMbgSgwCreateSessRspTx_Type = Counter64
_JnxMbgSgwCreateSessRspTx_Object = MibTableColumn
jnxMbgSgwCreateSessRspTx = _JnxMbgSgwCreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 28),
    _JnxMbgSgwCreateSessRspTx_Type()
)
jnxMbgSgwCreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCreateSessRspTx.setStatus("current")
_JnxMbgSgwModBrReqRx_Type = Counter64
_JnxMbgSgwModBrReqRx_Object = MibTableColumn
jnxMbgSgwModBrReqRx = _JnxMbgSgwModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 29),
    _JnxMbgSgwModBrReqRx_Type()
)
jnxMbgSgwModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrReqRx.setStatus("current")
_JnxMbgSgwModBrReqTx_Type = Counter64
_JnxMbgSgwModBrReqTx_Object = MibTableColumn
jnxMbgSgwModBrReqTx = _JnxMbgSgwModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 30),
    _JnxMbgSgwModBrReqTx_Type()
)
jnxMbgSgwModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrReqTx.setStatus("current")
_JnxMbgSgwModBrRspRx_Type = Counter64
_JnxMbgSgwModBrRspRx_Object = MibTableColumn
jnxMbgSgwModBrRspRx = _JnxMbgSgwModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 31),
    _JnxMbgSgwModBrRspRx_Type()
)
jnxMbgSgwModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrRspRx.setStatus("current")
_JnxMbgSgwModBrRspTx_Type = Counter64
_JnxMbgSgwModBrRspTx_Object = MibTableColumn
jnxMbgSgwModBrRspTx = _JnxMbgSgwModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 32),
    _JnxMbgSgwModBrRspTx_Type()
)
jnxMbgSgwModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrRspTx.setStatus("current")
_JnxMbgSgwDelSessReqRx_Type = Counter64
_JnxMbgSgwDelSessReqRx_Object = MibTableColumn
jnxMbgSgwDelSessReqRx = _JnxMbgSgwDelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 33),
    _JnxMbgSgwDelSessReqRx_Type()
)
jnxMbgSgwDelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelSessReqRx.setStatus("current")
_JnxMbgSgwDelSessReqTx_Type = Counter64
_JnxMbgSgwDelSessReqTx_Object = MibTableColumn
jnxMbgSgwDelSessReqTx = _JnxMbgSgwDelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 34),
    _JnxMbgSgwDelSessReqTx_Type()
)
jnxMbgSgwDelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelSessReqTx.setStatus("current")
_JnxMbgSgwDelSessRspRx_Type = Counter64
_JnxMbgSgwDelSessRspRx_Object = MibTableColumn
jnxMbgSgwDelSessRspRx = _JnxMbgSgwDelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 35),
    _JnxMbgSgwDelSessRspRx_Type()
)
jnxMbgSgwDelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelSessRspRx.setStatus("current")
_JnxMbgSgwDelSessRspTx_Type = Counter64
_JnxMbgSgwDelSessRspTx_Object = MibTableColumn
jnxMbgSgwDelSessRspTx = _JnxMbgSgwDelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 36),
    _JnxMbgSgwDelSessRspTx_Type()
)
jnxMbgSgwDelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelSessRspTx.setStatus("current")
_JnxMbgSgwCrtBrReqRx_Type = Counter64
_JnxMbgSgwCrtBrReqRx_Object = MibTableColumn
jnxMbgSgwCrtBrReqRx = _JnxMbgSgwCrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 37),
    _JnxMbgSgwCrtBrReqRx_Type()
)
jnxMbgSgwCrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrtBrReqRx.setStatus("current")
_JnxMbgSgwCrtBrReqTx_Type = Counter64
_JnxMbgSgwCrtBrReqTx_Object = MibTableColumn
jnxMbgSgwCrtBrReqTx = _JnxMbgSgwCrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 38),
    _JnxMbgSgwCrtBrReqTx_Type()
)
jnxMbgSgwCrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrtBrReqTx.setStatus("current")
_JnxMbgSgwCrtBrRspRx_Type = Counter64
_JnxMbgSgwCrtBrRspRx_Object = MibTableColumn
jnxMbgSgwCrtBrRspRx = _JnxMbgSgwCrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 39),
    _JnxMbgSgwCrtBrRspRx_Type()
)
jnxMbgSgwCrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrtBrRspRx.setStatus("current")
_JnxMbgSgwCrtBrRspTx_Type = Counter64
_JnxMbgSgwCrtBrRspTx_Object = MibTableColumn
jnxMbgSgwCrtBrRspTx = _JnxMbgSgwCrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 40),
    _JnxMbgSgwCrtBrRspTx_Type()
)
jnxMbgSgwCrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrtBrRspTx.setStatus("current")
_JnxMbgSgwUpdBrReqRx_Type = Counter64
_JnxMbgSgwUpdBrReqRx_Object = MibTableColumn
jnxMbgSgwUpdBrReqRx = _JnxMbgSgwUpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 41),
    _JnxMbgSgwUpdBrReqRx_Type()
)
jnxMbgSgwUpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdBrReqRx.setStatus("current")
_JnxMbgSgwUpdBrReqTx_Type = Counter64
_JnxMbgSgwUpdBrReqTx_Object = MibTableColumn
jnxMbgSgwUpdBrReqTx = _JnxMbgSgwUpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 42),
    _JnxMbgSgwUpdBrReqTx_Type()
)
jnxMbgSgwUpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdBrReqTx.setStatus("current")
_JnxMbgSgwUpdBrRspRx_Type = Counter64
_JnxMbgSgwUpdBrRspRx_Object = MibTableColumn
jnxMbgSgwUpdBrRspRx = _JnxMbgSgwUpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 43),
    _JnxMbgSgwUpdBrRspRx_Type()
)
jnxMbgSgwUpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdBrRspRx.setStatus("current")
_JnxMbgSgwUpdBrRspTx_Type = Counter64
_JnxMbgSgwUpdBrRspTx_Object = MibTableColumn
jnxMbgSgwUpdBrRspTx = _JnxMbgSgwUpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 44),
    _JnxMbgSgwUpdBrRspTx_Type()
)
jnxMbgSgwUpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdBrRspTx.setStatus("current")
_JnxMbgSgwDelBrReqRx_Type = Counter64
_JnxMbgSgwDelBrReqRx_Object = MibTableColumn
jnxMbgSgwDelBrReqRx = _JnxMbgSgwDelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 45),
    _JnxMbgSgwDelBrReqRx_Type()
)
jnxMbgSgwDelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrReqRx.setStatus("current")
_JnxMbgSgwDelBrReqTx_Type = Counter64
_JnxMbgSgwDelBrReqTx_Object = MibTableColumn
jnxMbgSgwDelBrReqTx = _JnxMbgSgwDelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 46),
    _JnxMbgSgwDelBrReqTx_Type()
)
jnxMbgSgwDelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrReqTx.setStatus("current")
_JnxMbgSgwDelBrRspRx_Type = Counter64
_JnxMbgSgwDelBrRspRx_Object = MibTableColumn
jnxMbgSgwDelBrRspRx = _JnxMbgSgwDelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 47),
    _JnxMbgSgwDelBrRspRx_Type()
)
jnxMbgSgwDelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrRspRx.setStatus("current")
_JnxMbgSgwDelBrRspTx_Type = Counter64
_JnxMbgSgwDelBrRspTx_Object = MibTableColumn
jnxMbgSgwDelBrRspTx = _JnxMbgSgwDelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 48),
    _JnxMbgSgwDelBrRspTx_Type()
)
jnxMbgSgwDelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrRspTx.setStatus("current")
_JnxMbgSgwDelConnSetReqRx_Type = Counter64
_JnxMbgSgwDelConnSetReqRx_Object = MibTableColumn
jnxMbgSgwDelConnSetReqRx = _JnxMbgSgwDelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 49),
    _JnxMbgSgwDelConnSetReqRx_Type()
)
jnxMbgSgwDelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelConnSetReqRx.setStatus("current")
_JnxMbgSgwDelConnSetReqTx_Type = Counter64
_JnxMbgSgwDelConnSetReqTx_Object = MibTableColumn
jnxMbgSgwDelConnSetReqTx = _JnxMbgSgwDelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 50),
    _JnxMbgSgwDelConnSetReqTx_Type()
)
jnxMbgSgwDelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelConnSetReqTx.setStatus("current")
_JnxMbgSgwDelConnSetRspRx_Type = Counter64
_JnxMbgSgwDelConnSetRspRx_Object = MibTableColumn
jnxMbgSgwDelConnSetRspRx = _JnxMbgSgwDelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 51),
    _JnxMbgSgwDelConnSetRspRx_Type()
)
jnxMbgSgwDelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelConnSetRspRx.setStatus("current")
_JnxMbgSgwDelConnSetRspTx_Type = Counter64
_JnxMbgSgwDelConnSetRspTx_Object = MibTableColumn
jnxMbgSgwDelConnSetRspTx = _JnxMbgSgwDelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 52),
    _JnxMbgSgwDelConnSetRspTx_Type()
)
jnxMbgSgwDelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelConnSetRspTx.setStatus("current")
_JnxMbgSgwUpdConnSetReqRx_Type = Counter64
_JnxMbgSgwUpdConnSetReqRx_Object = MibTableColumn
jnxMbgSgwUpdConnSetReqRx = _JnxMbgSgwUpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 53),
    _JnxMbgSgwUpdConnSetReqRx_Type()
)
jnxMbgSgwUpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdConnSetReqRx.setStatus("current")
_JnxMbgSgwUpdConnSetReqTx_Type = Counter64
_JnxMbgSgwUpdConnSetReqTx_Object = MibTableColumn
jnxMbgSgwUpdConnSetReqTx = _JnxMbgSgwUpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 54),
    _JnxMbgSgwUpdConnSetReqTx_Type()
)
jnxMbgSgwUpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdConnSetReqTx.setStatus("current")
_JnxMbgSgwUpdConnSetRspRx_Type = Counter64
_JnxMbgSgwUpdConnSetRspRx_Object = MibTableColumn
jnxMbgSgwUpdConnSetRspRx = _JnxMbgSgwUpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 55),
    _JnxMbgSgwUpdConnSetRspRx_Type()
)
jnxMbgSgwUpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdConnSetRspRx.setStatus("current")
_JnxMbgSgwUpdConnSetRspTx_Type = Counter64
_JnxMbgSgwUpdConnSetRspTx_Object = MibTableColumn
jnxMbgSgwUpdConnSetRspTx = _JnxMbgSgwUpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 56),
    _JnxMbgSgwUpdConnSetRspTx_Type()
)
jnxMbgSgwUpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwUpdConnSetRspTx.setStatus("current")
_JnxMbgSgwModBrCmdRx_Type = Counter64
_JnxMbgSgwModBrCmdRx_Object = MibTableColumn
jnxMbgSgwModBrCmdRx = _JnxMbgSgwModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 57),
    _JnxMbgSgwModBrCmdRx_Type()
)
jnxMbgSgwModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrCmdRx.setStatus("current")
_JnxMbgSgwModBrCmdTx_Type = Counter64
_JnxMbgSgwModBrCmdTx_Object = MibTableColumn
jnxMbgSgwModBrCmdTx = _JnxMbgSgwModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 58),
    _JnxMbgSgwModBrCmdTx_Type()
)
jnxMbgSgwModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrCmdTx.setStatus("current")
_JnxMbgSgwModBrFlrIndRx_Type = Counter64
_JnxMbgSgwModBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwModBrFlrIndRx = _JnxMbgSgwModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 59),
    _JnxMbgSgwModBrFlrIndRx_Type()
)
jnxMbgSgwModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrFlrIndRx.setStatus("current")
_JnxMbgSgwModBrFlrIndTx_Type = Counter64
_JnxMbgSgwModBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwModBrFlrIndTx = _JnxMbgSgwModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 60),
    _JnxMbgSgwModBrFlrIndTx_Type()
)
jnxMbgSgwModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwModBrFlrIndTx.setStatus("current")
_JnxMbgSgwDelBrCmdRx_Type = Counter64
_JnxMbgSgwDelBrCmdRx_Object = MibTableColumn
jnxMbgSgwDelBrCmdRx = _JnxMbgSgwDelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 61),
    _JnxMbgSgwDelBrCmdRx_Type()
)
jnxMbgSgwDelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrCmdRx.setStatus("current")
_JnxMbgSgwDelBrCmdTx_Type = Counter64
_JnxMbgSgwDelBrCmdTx_Object = MibTableColumn
jnxMbgSgwDelBrCmdTx = _JnxMbgSgwDelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 62),
    _JnxMbgSgwDelBrCmdTx_Type()
)
jnxMbgSgwDelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrCmdTx.setStatus("current")
_JnxMbgSgwDelBrFlrIndRx_Type = Counter64
_JnxMbgSgwDelBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwDelBrFlrIndRx = _JnxMbgSgwDelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 63),
    _JnxMbgSgwDelBrFlrIndRx_Type()
)
jnxMbgSgwDelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrFlrIndRx.setStatus("current")
_JnxMbgSgwDelBrFlrIndTx_Type = Counter64
_JnxMbgSgwDelBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwDelBrFlrIndTx = _JnxMbgSgwDelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 64),
    _JnxMbgSgwDelBrFlrIndTx_Type()
)
jnxMbgSgwDelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelBrFlrIndTx.setStatus("current")
_JnxMbgSgwBrResCmdRx_Type = Counter64
_JnxMbgSgwBrResCmdRx_Object = MibTableColumn
jnxMbgSgwBrResCmdRx = _JnxMbgSgwBrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 65),
    _JnxMbgSgwBrResCmdRx_Type()
)
jnxMbgSgwBrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwBrResCmdRx.setStatus("current")
_JnxMbgSgwBrResCmdTx_Type = Counter64
_JnxMbgSgwBrResCmdTx_Object = MibTableColumn
jnxMbgSgwBrResCmdTx = _JnxMbgSgwBrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 66),
    _JnxMbgSgwBrResCmdTx_Type()
)
jnxMbgSgwBrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwBrResCmdTx.setStatus("current")
_JnxMbgSgwBrResFlrIndRx_Type = Counter64
_JnxMbgSgwBrResFlrIndRx_Object = MibTableColumn
jnxMbgSgwBrResFlrIndRx = _JnxMbgSgwBrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 67),
    _JnxMbgSgwBrResFlrIndRx_Type()
)
jnxMbgSgwBrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwBrResFlrIndRx.setStatus("current")
_JnxMbgSgwBrResFlrIndTx_Type = Counter64
_JnxMbgSgwBrResFlrIndTx_Object = MibTableColumn
jnxMbgSgwBrResFlrIndTx = _JnxMbgSgwBrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 68),
    _JnxMbgSgwBrResFlrIndTx_Type()
)
jnxMbgSgwBrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwBrResFlrIndTx.setStatus("current")
_JnxMbgSgwRelAcsBrReqRx_Type = Counter64
_JnxMbgSgwRelAcsBrReqRx_Object = MibTableColumn
jnxMbgSgwRelAcsBrReqRx = _JnxMbgSgwRelAcsBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 69),
    _JnxMbgSgwRelAcsBrReqRx_Type()
)
jnxMbgSgwRelAcsBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwRelAcsBrReqRx.setStatus("current")
_JnxMbgSgwRelAcsBrReqTx_Type = Counter64
_JnxMbgSgwRelAcsBrReqTx_Object = MibTableColumn
jnxMbgSgwRelAcsBrReqTx = _JnxMbgSgwRelAcsBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 70),
    _JnxMbgSgwRelAcsBrReqTx_Type()
)
jnxMbgSgwRelAcsBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwRelAcsBrReqTx.setStatus("current")
_JnxMbgSgwRelAcsBrRespRx_Type = Counter64
_JnxMbgSgwRelAcsBrRespRx_Object = MibTableColumn
jnxMbgSgwRelAcsBrRespRx = _JnxMbgSgwRelAcsBrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 71),
    _JnxMbgSgwRelAcsBrRespRx_Type()
)
jnxMbgSgwRelAcsBrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwRelAcsBrRespRx.setStatus("current")
_JnxMbgSgwRelAcsBrRespTx_Type = Counter64
_JnxMbgSgwRelAcsBrRespTx_Object = MibTableColumn
jnxMbgSgwRelAcsBrRespTx = _JnxMbgSgwRelAcsBrRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 72),
    _JnxMbgSgwRelAcsBrRespTx_Type()
)
jnxMbgSgwRelAcsBrRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwRelAcsBrRespTx.setStatus("current")
_JnxMbgSgwCrIndTunReqRx_Type = Counter64
_JnxMbgSgwCrIndTunReqRx_Object = MibTableColumn
jnxMbgSgwCrIndTunReqRx = _JnxMbgSgwCrIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 73),
    _JnxMbgSgwCrIndTunReqRx_Type()
)
jnxMbgSgwCrIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrIndTunReqRx.setStatus("current")
_JnxMbgSgwCrIndTunReqTx_Type = Counter64
_JnxMbgSgwCrIndTunReqTx_Object = MibTableColumn
jnxMbgSgwCrIndTunReqTx = _JnxMbgSgwCrIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 74),
    _JnxMbgSgwCrIndTunReqTx_Type()
)
jnxMbgSgwCrIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrIndTunReqTx.setStatus("current")
_JnxMbgSgwCrIndTunRespRx_Type = Counter64
_JnxMbgSgwCrIndTunRespRx_Object = MibTableColumn
jnxMbgSgwCrIndTunRespRx = _JnxMbgSgwCrIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 75),
    _JnxMbgSgwCrIndTunRespRx_Type()
)
jnxMbgSgwCrIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrIndTunRespRx.setStatus("current")
_JnxMbgSgwCrIndTunRespTx_Type = Counter64
_JnxMbgSgwCrIndTunRespTx_Object = MibTableColumn
jnxMbgSgwCrIndTunRespTx = _JnxMbgSgwCrIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 76),
    _JnxMbgSgwCrIndTunRespTx_Type()
)
jnxMbgSgwCrIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCrIndTunRespTx.setStatus("current")
_JnxMbgSgwDelIndTunReqRx_Type = Counter64
_JnxMbgSgwDelIndTunReqRx_Object = MibTableColumn
jnxMbgSgwDelIndTunReqRx = _JnxMbgSgwDelIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 77),
    _JnxMbgSgwDelIndTunReqRx_Type()
)
jnxMbgSgwDelIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelIndTunReqRx.setStatus("current")
_JnxMbgSgwDelIndTunReqTx_Type = Counter64
_JnxMbgSgwDelIndTunReqTx_Object = MibTableColumn
jnxMbgSgwDelIndTunReqTx = _JnxMbgSgwDelIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 78),
    _JnxMbgSgwDelIndTunReqTx_Type()
)
jnxMbgSgwDelIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelIndTunReqTx.setStatus("current")
_JnxMbgSgwDelIndTunRespRx_Type = Counter64
_JnxMbgSgwDelIndTunRespRx_Object = MibTableColumn
jnxMbgSgwDelIndTunRespRx = _JnxMbgSgwDelIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 79),
    _JnxMbgSgwDelIndTunRespRx_Type()
)
jnxMbgSgwDelIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelIndTunRespRx.setStatus("current")
_JnxMbgSgwDelIndTunRespTx_Type = Counter64
_JnxMbgSgwDelIndTunRespTx_Object = MibTableColumn
jnxMbgSgwDelIndTunRespTx = _JnxMbgSgwDelIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 80),
    _JnxMbgSgwDelIndTunRespTx_Type()
)
jnxMbgSgwDelIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDelIndTunRespTx.setStatus("current")
_JnxMbgSgwDlDataNotifRx_Type = Counter64
_JnxMbgSgwDlDataNotifRx_Object = MibTableColumn
jnxMbgSgwDlDataNotifRx = _JnxMbgSgwDlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 81),
    _JnxMbgSgwDlDataNotifRx_Type()
)
jnxMbgSgwDlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataNotifRx.setStatus("current")
_JnxMbgSgwDlDataNotifTx_Type = Counter64
_JnxMbgSgwDlDataNotifTx_Object = MibTableColumn
jnxMbgSgwDlDataNotifTx = _JnxMbgSgwDlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 82),
    _JnxMbgSgwDlDataNotifTx_Type()
)
jnxMbgSgwDlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataNotifTx.setStatus("current")
_JnxMbgSgwDlDataAckRx_Type = Counter64
_JnxMbgSgwDlDataAckRx_Object = MibTableColumn
jnxMbgSgwDlDataAckRx = _JnxMbgSgwDlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 83),
    _JnxMbgSgwDlDataAckRx_Type()
)
jnxMbgSgwDlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataAckRx.setStatus("current")
_JnxMbgSgwDlDataAckTx_Type = Counter64
_JnxMbgSgwDlDataAckTx_Object = MibTableColumn
jnxMbgSgwDlDataAckTx = _JnxMbgSgwDlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 84),
    _JnxMbgSgwDlDataAckTx_Type()
)
jnxMbgSgwDlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataAckTx.setStatus("current")
_JnxMbgSgwDlDataNotiFlrIndRx_Type = Counter64
_JnxMbgSgwDlDataNotiFlrIndRx_Object = MibTableColumn
jnxMbgSgwDlDataNotiFlrIndRx = _JnxMbgSgwDlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 85),
    _JnxMbgSgwDlDataNotiFlrIndRx_Type()
)
jnxMbgSgwDlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataNotiFlrIndRx.setStatus("current")
_JnxMbgSgwDlDataNotiFlrIndTx_Type = Counter64
_JnxMbgSgwDlDataNotiFlrIndTx_Object = MibTableColumn
jnxMbgSgwDlDataNotiFlrIndTx = _JnxMbgSgwDlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 86),
    _JnxMbgSgwDlDataNotiFlrIndTx_Type()
)
jnxMbgSgwDlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDlDataNotiFlrIndTx.setStatus("current")
_JnxMbgSgwStopPagingIndRx_Type = Counter64
_JnxMbgSgwStopPagingIndRx_Object = MibTableColumn
jnxMbgSgwStopPagingIndRx = _JnxMbgSgwStopPagingIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 87),
    _JnxMbgSgwStopPagingIndRx_Type()
)
jnxMbgSgwStopPagingIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwStopPagingIndRx.setStatus("current")
_JnxMbgSgwStopPagingIndTx_Type = Counter64
_JnxMbgSgwStopPagingIndTx_Object = MibTableColumn
jnxMbgSgwStopPagingIndTx = _JnxMbgSgwStopPagingIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 88),
    _JnxMbgSgwStopPagingIndTx_Type()
)
jnxMbgSgwStopPagingIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwStopPagingIndTx.setStatus("current")
_JnxMbgSgwGtpV2ICsPageRx_Type = Counter64
_JnxMbgSgwGtpV2ICsPageRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPageRx = _JnxMbgSgwGtpV2ICsPageRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 89),
    _JnxMbgSgwGtpV2ICsPageRx_Type()
)
jnxMbgSgwGtpV2ICsPageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPageRx.setStatus("obsolete")
_JnxMbgSgwGtpV2ICsPageTx_Type = Counter64
_JnxMbgSgwGtpV2ICsPageTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPageTx = _JnxMbgSgwGtpV2ICsPageTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 90),
    _JnxMbgSgwGtpV2ICsPageTx_Type()
)
jnxMbgSgwGtpV2ICsPageTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPageTx.setStatus("obsolete")
_JnxMbgSgwGtpV2ICsReqAcceptRx_Type = Counter64
_JnxMbgSgwGtpV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsReqAcceptRx = _JnxMbgSgwGtpV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 91),
    _JnxMbgSgwGtpV2ICsReqAcceptRx_Type()
)
jnxMbgSgwGtpV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsReqAcceptRx.setStatus("current")
_JnxMbgSgwGtpV2ICsReqAcceptTx_Type = Counter64
_JnxMbgSgwGtpV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsReqAcceptTx = _JnxMbgSgwGtpV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 92),
    _JnxMbgSgwGtpV2ICsReqAcceptTx_Type()
)
jnxMbgSgwGtpV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsReqAcceptTx.setStatus("current")
_JnxMbgSgwGtpV2ICsAcceptPartRx_Type = Counter64
_JnxMbgSgwGtpV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAcceptPartRx = _JnxMbgSgwGtpV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 93),
    _JnxMbgSgwGtpV2ICsAcceptPartRx_Type()
)
jnxMbgSgwGtpV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAcceptPartRx.setStatus("current")
_JnxMbgSgwGtpV2ICsAcceptPartTx_Type = Counter64
_JnxMbgSgwGtpV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAcceptPartTx = _JnxMbgSgwGtpV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 94),
    _JnxMbgSgwGtpV2ICsAcceptPartTx_Type()
)
jnxMbgSgwGtpV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAcceptPartTx.setStatus("current")
_JnxMbgSgwGtpV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgSgwGtpV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNewPTNPrefRx = _JnxMbgSgwGtpV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 95),
    _JnxMbgSgwGtpV2ICsNewPTNPrefRx_Type()
)
jnxMbgSgwGtpV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgSgwGtpV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgSgwGtpV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNewPTNPrefTx = _JnxMbgSgwGtpV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 96),
    _JnxMbgSgwGtpV2ICsNewPTNPrefTx_Type()
)
jnxMbgSgwGtpV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgSgwGtpV2ICsNewPTSIAdbrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsNewPTSIAdbrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNewPTSIAdbrRx = _JnxMbgSgwGtpV2ICsNewPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 97),
    _JnxMbgSgwGtpV2ICsNewPTSIAdbrRx_Type()
)
jnxMbgSgwGtpV2ICsNewPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNewPTSIAdbrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsNewPTSIAdbrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsNewPTSIAdbrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNewPTSIAdbrTx = _JnxMbgSgwGtpV2ICsNewPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 98),
    _JnxMbgSgwGtpV2ICsNewPTSIAdbrTx_Type()
)
jnxMbgSgwGtpV2ICsNewPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNewPTSIAdbrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgSgwGtpV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCtxNotFndRx = _JnxMbgSgwGtpV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 99),
    _JnxMbgSgwGtpV2ICsCtxNotFndRx_Type()
)
jnxMbgSgwGtpV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgSgwGtpV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgSgwGtpV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCtxNotFndTx = _JnxMbgSgwGtpV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 100),
    _JnxMbgSgwGtpV2ICsCtxNotFndTx_Type()
)
jnxMbgSgwGtpV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvMsgFmtRx = _JnxMbgSgwGtpV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 101),
    _JnxMbgSgwGtpV2ICsInvMsgFmtRx_Type()
)
jnxMbgSgwGtpV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvMsgFmtTx = _JnxMbgSgwGtpV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 102),
    _JnxMbgSgwGtpV2ICsInvMsgFmtTx_Type()
)
jnxMbgSgwGtpV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgSgwGtpV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgSgwGtpV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsVerNotSuppRx = _JnxMbgSgwGtpV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 103),
    _JnxMbgSgwGtpV2ICsVerNotSuppRx_Type()
)
jnxMbgSgwGtpV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgSgwGtpV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgSgwGtpV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsVerNotSuppTx = _JnxMbgSgwGtpV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 104),
    _JnxMbgSgwGtpV2ICsVerNotSuppTx_Type()
)
jnxMbgSgwGtpV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvLenRx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvLenRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvLenRx = _JnxMbgSgwGtpV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 105),
    _JnxMbgSgwGtpV2ICsInvLenRx_Type()
)
jnxMbgSgwGtpV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvLenRx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvLenTx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvLenTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvLenTx = _JnxMbgSgwGtpV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 106),
    _JnxMbgSgwGtpV2ICsInvLenTx_Type()
)
jnxMbgSgwGtpV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvLenTx.setStatus("current")
_JnxMbgSgwGtpV2ICsServNotSuppRx_Type = Counter64
_JnxMbgSgwGtpV2ICsServNotSuppRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsServNotSuppRx = _JnxMbgSgwGtpV2ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 107),
    _JnxMbgSgwGtpV2ICsServNotSuppRx_Type()
)
jnxMbgSgwGtpV2ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsServNotSuppRx.setStatus("current")
_JnxMbgSgwGtpV2ICsServNotSuppTx_Type = Counter64
_JnxMbgSgwGtpV2ICsServNotSuppTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsServNotSuppTx = _JnxMbgSgwGtpV2ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 108),
    _JnxMbgSgwGtpV2ICsServNotSuppTx_Type()
)
jnxMbgSgwGtpV2ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsServNotSuppTx.setStatus("current")
_JnxMbgSgwGtpV2ICsManIEIncorrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsManIEIncorrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsManIEIncorrRx = _JnxMbgSgwGtpV2ICsManIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 109),
    _JnxMbgSgwGtpV2ICsManIEIncorrRx_Type()
)
jnxMbgSgwGtpV2ICsManIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsManIEIncorrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsManIEIncorrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsManIEIncorrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsManIEIncorrTx = _JnxMbgSgwGtpV2ICsManIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 110),
    _JnxMbgSgwGtpV2ICsManIEIncorrTx_Type()
)
jnxMbgSgwGtpV2ICsManIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsManIEIncorrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsManIEMissRx_Type = Counter64
_JnxMbgSgwGtpV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsManIEMissRx = _JnxMbgSgwGtpV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 111),
    _JnxMbgSgwGtpV2ICsManIEMissRx_Type()
)
jnxMbgSgwGtpV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsManIEMissRx.setStatus("current")
_JnxMbgSgwGtpV2ICsManIEMissTx_Type = Counter64
_JnxMbgSgwGtpV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsManIEMissTx = _JnxMbgSgwGtpV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 112),
    _JnxMbgSgwGtpV2ICsManIEMissTx_Type()
)
jnxMbgSgwGtpV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsManIEMissTx.setStatus("current")
_JnxMbgSgwGtpV2ICsOptIEIncorrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsOptIEIncorrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsOptIEIncorrRx = _JnxMbgSgwGtpV2ICsOptIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 113),
    _JnxMbgSgwGtpV2ICsOptIEIncorrRx_Type()
)
jnxMbgSgwGtpV2ICsOptIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsOptIEIncorrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsOptIEIncorrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsOptIEIncorrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsOptIEIncorrTx = _JnxMbgSgwGtpV2ICsOptIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 114),
    _JnxMbgSgwGtpV2ICsOptIEIncorrTx_Type()
)
jnxMbgSgwGtpV2ICsOptIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsOptIEIncorrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsSysFailRx_Type = Counter64
_JnxMbgSgwGtpV2ICsSysFailRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSysFailRx = _JnxMbgSgwGtpV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 115),
    _JnxMbgSgwGtpV2ICsSysFailRx_Type()
)
jnxMbgSgwGtpV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSysFailRx.setStatus("current")
_JnxMbgSgwGtpV2ICsSysFailTx_Type = Counter64
_JnxMbgSgwGtpV2ICsSysFailTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSysFailTx = _JnxMbgSgwGtpV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 116),
    _JnxMbgSgwGtpV2ICsSysFailTx_Type()
)
jnxMbgSgwGtpV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSysFailTx.setStatus("current")
_JnxMbgSgwGtpV2ICsNoResRx_Type = Counter64
_JnxMbgSgwGtpV2ICsNoResRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNoResRx = _JnxMbgSgwGtpV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 117),
    _JnxMbgSgwGtpV2ICsNoResRx_Type()
)
jnxMbgSgwGtpV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNoResRx.setStatus("current")
_JnxMbgSgwGtpV2ICsNoResTx_Type = Counter64
_JnxMbgSgwGtpV2ICsNoResTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNoResTx = _JnxMbgSgwGtpV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 118),
    _JnxMbgSgwGtpV2ICsNoResTx_Type()
)
jnxMbgSgwGtpV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNoResTx.setStatus("current")
_JnxMbgSgwGtpV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgSgwGtpV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsTFTSMANTErRx = _JnxMbgSgwGtpV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 119),
    _JnxMbgSgwGtpV2ICsTFTSMANTErRx_Type()
)
jnxMbgSgwGtpV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgSgwGtpV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgSgwGtpV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsTFTSMANTErTx = _JnxMbgSgwGtpV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 120),
    _JnxMbgSgwGtpV2ICsTFTSMANTErTx_Type()
)
jnxMbgSgwGtpV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgSgwGtpV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsTFTSysErrRx = _JnxMbgSgwGtpV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 121),
    _JnxMbgSgwGtpV2ICsTFTSysErrRx_Type()
)
jnxMbgSgwGtpV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsTFTSysErrTx = _JnxMbgSgwGtpV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 122),
    _JnxMbgSgwGtpV2ICsTFTSysErrTx_Type()
)
jnxMbgSgwGtpV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsPkFltManErrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsPkFltManErrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPkFltManErrRx = _JnxMbgSgwGtpV2ICsPkFltManErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 123),
    _JnxMbgSgwGtpV2ICsPkFltManErrRx_Type()
)
jnxMbgSgwGtpV2ICsPkFltManErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPkFltManErrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsPkFltManErrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsPkFltManErrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPkFltManErrTx = _JnxMbgSgwGtpV2ICsPkFltManErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 124),
    _JnxMbgSgwGtpV2ICsPkFltManErrTx_Type()
)
jnxMbgSgwGtpV2ICsPkFltManErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPkFltManErrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsPkFltSynErrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsPkFltSynErrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPkFltSynErrRx = _JnxMbgSgwGtpV2ICsPkFltSynErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 125),
    _JnxMbgSgwGtpV2ICsPkFltSynErrRx_Type()
)
jnxMbgSgwGtpV2ICsPkFltSynErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPkFltSynErrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsPkFltSynErrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsPkFltSynErrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPkFltSynErrTx = _JnxMbgSgwGtpV2ICsPkFltSynErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 126),
    _JnxMbgSgwGtpV2ICsPkFltSynErrTx_Type()
)
jnxMbgSgwGtpV2ICsPkFltSynErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPkFltSynErrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgSgwGtpV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsMisUnknAPNRx = _JnxMbgSgwGtpV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 127),
    _JnxMbgSgwGtpV2ICsMisUnknAPNRx_Type()
)
jnxMbgSgwGtpV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgSgwGtpV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgSgwGtpV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsMisUnknAPNTx = _JnxMbgSgwGtpV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 128),
    _JnxMbgSgwGtpV2ICsMisUnknAPNTx_Type()
)
jnxMbgSgwGtpV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnexpRptIERx = _JnxMbgSgwGtpV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 129),
    _JnxMbgSgwGtpV2ICsUnexpRptIERx_Type()
)
jnxMbgSgwGtpV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnexpRptIETx = _JnxMbgSgwGtpV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 130),
    _JnxMbgSgwGtpV2ICsUnexpRptIETx_Type()
)
jnxMbgSgwGtpV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgSgwGtpV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgSgwGtpV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsGREKeyNtFdRx = _JnxMbgSgwGtpV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 131),
    _JnxMbgSgwGtpV2ICsGREKeyNtFdRx_Type()
)
jnxMbgSgwGtpV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgSgwGtpV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgSgwGtpV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsGREKeyNtFdTx = _JnxMbgSgwGtpV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 132),
    _JnxMbgSgwGtpV2ICsGREKeyNtFdTx_Type()
)
jnxMbgSgwGtpV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgSgwGtpV2ICsRelocFailRx_Type = Counter64
_JnxMbgSgwGtpV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRelocFailRx = _JnxMbgSgwGtpV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 133),
    _JnxMbgSgwGtpV2ICsRelocFailRx_Type()
)
jnxMbgSgwGtpV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRelocFailRx.setStatus("current")
_JnxMbgSgwGtpV2ICsRelocFailTx_Type = Counter64
_JnxMbgSgwGtpV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRelocFailTx = _JnxMbgSgwGtpV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 134),
    _JnxMbgSgwGtpV2ICsRelocFailTx_Type()
)
jnxMbgSgwGtpV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRelocFailTx.setStatus("current")
_JnxMbgSgwGtpV2ICsDeniedINRatRx_Type = Counter64
_JnxMbgSgwGtpV2ICsDeniedINRatRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsDeniedINRatRx = _JnxMbgSgwGtpV2ICsDeniedINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 135),
    _JnxMbgSgwGtpV2ICsDeniedINRatRx_Type()
)
jnxMbgSgwGtpV2ICsDeniedINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsDeniedINRatRx.setStatus("current")
_JnxMbgSgwGtpV2ICsDeniedINRatTx_Type = Counter64
_JnxMbgSgwGtpV2ICsDeniedINRatTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsDeniedINRatTx = _JnxMbgSgwGtpV2ICsDeniedINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 136),
    _JnxMbgSgwGtpV2ICsDeniedINRatTx_Type()
)
jnxMbgSgwGtpV2ICsDeniedINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsDeniedINRatTx.setStatus("current")
_JnxMbgSgwGtpV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgSgwGtpV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPTNotSuppRx = _JnxMbgSgwGtpV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 137),
    _JnxMbgSgwGtpV2ICsPTNotSuppRx_Type()
)
jnxMbgSgwGtpV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgSgwGtpV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgSgwGtpV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPTNotSuppTx = _JnxMbgSgwGtpV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 138),
    _JnxMbgSgwGtpV2ICsPTNotSuppTx_Type()
)
jnxMbgSgwGtpV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgSgwGtpV2ICsAllDynAdOccRx_Type = Counter64
_JnxMbgSgwGtpV2ICsAllDynAdOccRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAllDynAdOccRx = _JnxMbgSgwGtpV2ICsAllDynAdOccRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 139),
    _JnxMbgSgwGtpV2ICsAllDynAdOccRx_Type()
)
jnxMbgSgwGtpV2ICsAllDynAdOccRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAllDynAdOccRx.setStatus("current")
_JnxMbgSgwGtpV2ICsAllDynAdOccTx_Type = Counter64
_JnxMbgSgwGtpV2ICsAllDynAdOccTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAllDynAdOccTx = _JnxMbgSgwGtpV2ICsAllDynAdOccTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 140),
    _JnxMbgSgwGtpV2ICsAllDynAdOccTx_Type()
)
jnxMbgSgwGtpV2ICsAllDynAdOccTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAllDynAdOccTx.setStatus("current")
_JnxMbgSgwGtpV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgSgwGtpV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNOTFTUECTXRx = _JnxMbgSgwGtpV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 141),
    _JnxMbgSgwGtpV2ICsNOTFTUECTXRx_Type()
)
jnxMbgSgwGtpV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgSgwGtpV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgSgwGtpV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNOTFTUECTXTx = _JnxMbgSgwGtpV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 142),
    _JnxMbgSgwGtpV2ICsNOTFTUECTXTx_Type()
)
jnxMbgSgwGtpV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgSgwGtpV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgSgwGtpV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsProtoNtSupRx = _JnxMbgSgwGtpV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 143),
    _JnxMbgSgwGtpV2ICsProtoNtSupRx_Type()
)
jnxMbgSgwGtpV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgSgwGtpV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgSgwGtpV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsProtoNtSupTx = _JnxMbgSgwGtpV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 144),
    _JnxMbgSgwGtpV2ICsProtoNtSupTx_Type()
)
jnxMbgSgwGtpV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUENotRespRx_Type = Counter64
_JnxMbgSgwGtpV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUENotRespRx = _JnxMbgSgwGtpV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 145),
    _JnxMbgSgwGtpV2ICsUENotRespRx_Type()
)
jnxMbgSgwGtpV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUENotRespRx.setStatus("current")
_JnxMbgSgwGtpV2ICsUENotRespTx_Type = Counter64
_JnxMbgSgwGtpV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUENotRespTx = _JnxMbgSgwGtpV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 146),
    _JnxMbgSgwGtpV2ICsUENotRespTx_Type()
)
jnxMbgSgwGtpV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUENotRespTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUERefusesRx_Type = Counter64
_JnxMbgSgwGtpV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUERefusesRx = _JnxMbgSgwGtpV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 147),
    _JnxMbgSgwGtpV2ICsUERefusesRx_Type()
)
jnxMbgSgwGtpV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUERefusesRx.setStatus("current")
_JnxMbgSgwGtpV2ICsUERefusesTx_Type = Counter64
_JnxMbgSgwGtpV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUERefusesTx = _JnxMbgSgwGtpV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 148),
    _JnxMbgSgwGtpV2ICsUERefusesTx_Type()
)
jnxMbgSgwGtpV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUERefusesTx.setStatus("current")
_JnxMbgSgwGtpV2ICsServDeniedRx_Type = Counter64
_JnxMbgSgwGtpV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsServDeniedRx = _JnxMbgSgwGtpV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 149),
    _JnxMbgSgwGtpV2ICsServDeniedRx_Type()
)
jnxMbgSgwGtpV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsServDeniedRx.setStatus("current")
_JnxMbgSgwGtpV2ICsServDeniedTx_Type = Counter64
_JnxMbgSgwGtpV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsServDeniedTx = _JnxMbgSgwGtpV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 150),
    _JnxMbgSgwGtpV2ICsServDeniedTx_Type()
)
jnxMbgSgwGtpV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsServDeniedTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnabPageUERx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnabPageUERx = _JnxMbgSgwGtpV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 151),
    _JnxMbgSgwGtpV2ICsUnabPageUERx_Type()
)
jnxMbgSgwGtpV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnabPageUERx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnabPageUETx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnabPageUETx = _JnxMbgSgwGtpV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 152),
    _JnxMbgSgwGtpV2ICsUnabPageUETx_Type()
)
jnxMbgSgwGtpV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnabPageUETx.setStatus("current")
_JnxMbgSgwGtpV2ICsNoMemRx_Type = Counter64
_JnxMbgSgwGtpV2ICsNoMemRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNoMemRx = _JnxMbgSgwGtpV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 153),
    _JnxMbgSgwGtpV2ICsNoMemRx_Type()
)
jnxMbgSgwGtpV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNoMemRx.setStatus("current")
_JnxMbgSgwGtpV2ICsNoMemTx_Type = Counter64
_JnxMbgSgwGtpV2ICsNoMemTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsNoMemTx = _JnxMbgSgwGtpV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 154),
    _JnxMbgSgwGtpV2ICsNoMemTx_Type()
)
jnxMbgSgwGtpV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsNoMemTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgSgwGtpV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUserAUTHFlRx = _JnxMbgSgwGtpV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 155),
    _JnxMbgSgwGtpV2ICsUserAUTHFlRx_Type()
)
jnxMbgSgwGtpV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgSgwGtpV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgSgwGtpV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUserAUTHFlTx = _JnxMbgSgwGtpV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 156),
    _JnxMbgSgwGtpV2ICsUserAUTHFlTx_Type()
)
jnxMbgSgwGtpV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgSgwGtpV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgSgwGtpV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAPNAcsDenRx = _JnxMbgSgwGtpV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 157),
    _JnxMbgSgwGtpV2ICsAPNAcsDenRx_Type()
)
jnxMbgSgwGtpV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgSgwGtpV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgSgwGtpV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAPNAcsDenTx = _JnxMbgSgwGtpV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 158),
    _JnxMbgSgwGtpV2ICsAPNAcsDenTx_Type()
)
jnxMbgSgwGtpV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgSgwGtpV2ICsReqRejRx_Type = Counter64
_JnxMbgSgwGtpV2ICsReqRejRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsReqRejRx = _JnxMbgSgwGtpV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 159),
    _JnxMbgSgwGtpV2ICsReqRejRx_Type()
)
jnxMbgSgwGtpV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsReqRejRx.setStatus("current")
_JnxMbgSgwGtpV2ICsReqRejTx_Type = Counter64
_JnxMbgSgwGtpV2ICsReqRejTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsReqRejTx = _JnxMbgSgwGtpV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 160),
    _JnxMbgSgwGtpV2ICsReqRejTx_Type()
)
jnxMbgSgwGtpV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsReqRejTx.setStatus("current")
_JnxMbgSgwGtpV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgSgwGtpV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPTMSISigMMRx = _JnxMbgSgwGtpV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 161),
    _JnxMbgSgwGtpV2ICsPTMSISigMMRx_Type()
)
jnxMbgSgwGtpV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgSgwGtpV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgSgwGtpV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsPTMSISigMMTx = _JnxMbgSgwGtpV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 162),
    _JnxMbgSgwGtpV2ICsPTMSISigMMTx_Type()
)
jnxMbgSgwGtpV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgSgwGtpV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgSgwGtpV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsIMSINotKnRx = _JnxMbgSgwGtpV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 163),
    _JnxMbgSgwGtpV2ICsIMSINotKnRx_Type()
)
jnxMbgSgwGtpV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgSgwGtpV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgSgwGtpV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsIMSINotKnTx = _JnxMbgSgwGtpV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 164),
    _JnxMbgSgwGtpV2ICsIMSINotKnTx_Type()
)
jnxMbgSgwGtpV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgSgwGtpV2ICsCondIEMsRx_Type = Counter64
_JnxMbgSgwGtpV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCondIEMsRx = _JnxMbgSgwGtpV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 165),
    _JnxMbgSgwGtpV2ICsCondIEMsRx_Type()
)
jnxMbgSgwGtpV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCondIEMsRx.setStatus("current")
_JnxMbgSgwGtpV2ICsCondIEMsTx_Type = Counter64
_JnxMbgSgwGtpV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCondIEMsTx = _JnxMbgSgwGtpV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 166),
    _JnxMbgSgwGtpV2ICsCondIEMsTx_Type()
)
jnxMbgSgwGtpV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCondIEMsTx.setStatus("current")
_JnxMbgSgwGtpV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgSgwGtpV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAPNResTIncRx = _JnxMbgSgwGtpV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 167),
    _JnxMbgSgwGtpV2ICsAPNResTIncRx_Type()
)
jnxMbgSgwGtpV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgSgwGtpV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgSgwGtpV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsAPNResTIncTx = _JnxMbgSgwGtpV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 168),
    _JnxMbgSgwGtpV2ICsAPNResTIncTx_Type()
)
jnxMbgSgwGtpV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnknownRx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnknownRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnknownRx = _JnxMbgSgwGtpV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 169),
    _JnxMbgSgwGtpV2ICsUnknownRx_Type()
)
jnxMbgSgwGtpV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnknownRx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnknownTx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnknownTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnknownTx = _JnxMbgSgwGtpV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 170),
    _JnxMbgSgwGtpV2ICsUnknownTx_Type()
)
jnxMbgSgwGtpV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnknownTx.setStatus("current")
_JnxMbgSgwGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgSgwGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsLclDetRx = _JnxMbgSgwGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 171),
    _JnxMbgSgwGtpV2ICsLclDetRx_Type()
)
jnxMbgSgwGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgSgwGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgSgwGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsLclDetTx = _JnxMbgSgwGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 172),
    _JnxMbgSgwGtpV2ICsLclDetTx_Type()
)
jnxMbgSgwGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgSgwGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgSgwGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCmpDetRx = _JnxMbgSgwGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 173),
    _JnxMbgSgwGtpV2ICsCmpDetRx_Type()
)
jnxMbgSgwGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgSgwGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgSgwGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsCmpDetTx = _JnxMbgSgwGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 174),
    _JnxMbgSgwGtpV2ICsCmpDetTx_Type()
)
jnxMbgSgwGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgSgwGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgSgwGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRATChgRx = _JnxMbgSgwGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 175),
    _JnxMbgSgwGtpV2ICsRATChgRx_Type()
)
jnxMbgSgwGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgSgwGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgSgwGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRATChgTx = _JnxMbgSgwGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 176),
    _JnxMbgSgwGtpV2ICsRATChgTx_Type()
)
jnxMbgSgwGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgSgwGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgSgwGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsISRDeactRx = _JnxMbgSgwGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 177),
    _JnxMbgSgwGtpV2ICsISRDeactRx_Type()
)
jnxMbgSgwGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgSgwGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgSgwGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsISRDeactTx = _JnxMbgSgwGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 178),
    _JnxMbgSgwGtpV2ICsISRDeactTx_Type()
)
jnxMbgSgwGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgSgwGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgSgwGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsEIFRNCEnRx = _JnxMbgSgwGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 179),
    _JnxMbgSgwGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgSgwGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgSgwGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgSgwGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsEIFRNCEnTx = _JnxMbgSgwGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 180),
    _JnxMbgSgwGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgSgwGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgSgwGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgSgwGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSemErTADRx = _JnxMbgSgwGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 181),
    _JnxMbgSgwGtpV2ICsSemErTADRx_Type()
)
jnxMbgSgwGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgSgwGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgSgwGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSemErTADTx = _JnxMbgSgwGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 182),
    _JnxMbgSgwGtpV2ICsSemErTADTx_Type()
)
jnxMbgSgwGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgSgwGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgSgwGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSynErTADRx = _JnxMbgSgwGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 183),
    _JnxMbgSgwGtpV2ICsSynErTADRx_Type()
)
jnxMbgSgwGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgSgwGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgSgwGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsSynErTADTx = _JnxMbgSgwGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 184),
    _JnxMbgSgwGtpV2ICsSynErTADTx_Type()
)
jnxMbgSgwGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgSgwGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgSgwGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRMValRcvRx = _JnxMbgSgwGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 185),
    _JnxMbgSgwGtpV2ICsRMValRcvRx_Type()
)
jnxMbgSgwGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgSgwGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgSgwGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRMValRcvTx = _JnxMbgSgwGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 186),
    _JnxMbgSgwGtpV2ICsRMValRcvTx_Type()
)
jnxMbgSgwGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgSgwGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgSgwGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRPrNtRspRx = _JnxMbgSgwGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 187),
    _JnxMbgSgwGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgSgwGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgSgwGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgSgwGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsRPrNtRspTx = _JnxMbgSgwGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 188),
    _JnxMbgSgwGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgSgwGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgSgwGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgSgwGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsColNWReqRx = _JnxMbgSgwGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 189),
    _JnxMbgSgwGtpV2ICsColNWReqRx_Type()
)
jnxMbgSgwGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgSgwGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgSgwGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsColNWReqTx = _JnxMbgSgwGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 190),
    _JnxMbgSgwGtpV2ICsColNWReqTx_Type()
)
jnxMbgSgwGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnPgUESusRx = _JnxMbgSgwGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 191),
    _JnxMbgSgwGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgSgwGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgSgwGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgSgwGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsUnPgUESusTx = _JnxMbgSgwGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 192),
    _JnxMbgSgwGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgSgwGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvTotLenRx = _JnxMbgSgwGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 193),
    _JnxMbgSgwGtpV2ICsInvTotLenRx_Type()
)
jnxMbgSgwGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvTotLenTx = _JnxMbgSgwGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 194),
    _JnxMbgSgwGtpV2ICsInvTotLenTx_Type()
)
jnxMbgSgwGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgSgwGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgSgwGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsDtForNtSupRx = _JnxMbgSgwGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 195),
    _JnxMbgSgwGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgSgwGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgSgwGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgSgwGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsDtForNtSupTx = _JnxMbgSgwGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 196),
    _JnxMbgSgwGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgSgwGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgSgwGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInReFRePrRx = _JnxMbgSgwGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 197),
    _JnxMbgSgwGtpV2ICsInReFRePrRx_Type()
)
jnxMbgSgwGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInReFRePrTx = _JnxMbgSgwGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 198),
    _JnxMbgSgwGtpV2ICsInReFRePrTx_Type()
)
jnxMbgSgwGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvPrRx = _JnxMbgSgwGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 199),
    _JnxMbgSgwGtpV2ICsInvPrRx_Type()
)
jnxMbgSgwGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgSgwGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgSgwGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgSgwGtpV2ICsInvPrTx = _JnxMbgSgwGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 200),
    _JnxMbgSgwGtpV2ICsInvPrTx_Type()
)
jnxMbgSgwGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgSgwGtpV1ProtocolErrRx_Type = Counter64
_JnxMbgSgwGtpV1ProtocolErrRx_Object = MibTableColumn
jnxMbgSgwGtpV1ProtocolErrRx = _JnxMbgSgwGtpV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 201),
    _JnxMbgSgwGtpV1ProtocolErrRx_Type()
)
jnxMbgSgwGtpV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1ProtocolErrRx.setStatus("current")
_JnxMbgSgwGtpV1UnSupMsgRx_Type = Counter64
_JnxMbgSgwGtpV1UnSupMsgRx_Object = MibTableColumn
jnxMbgSgwGtpV1UnSupMsgRx = _JnxMbgSgwGtpV1UnSupMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 202),
    _JnxMbgSgwGtpV1UnSupMsgRx_Type()
)
jnxMbgSgwGtpV1UnSupMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1UnSupMsgRx.setStatus("current")
_JnxMbgSgwGtpV1T3RespTmrExpRx_Type = Counter64
_JnxMbgSgwGtpV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwGtpV1T3RespTmrExpRx = _JnxMbgSgwGtpV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 203),
    _JnxMbgSgwGtpV1T3RespTmrExpRx_Type()
)
jnxMbgSgwGtpV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1T3RespTmrExpRx.setStatus("current")
_JnxMbgSgwGtpV1EndMarkerRx_Type = Counter64
_JnxMbgSgwGtpV1EndMarkerRx_Object = MibTableColumn
jnxMbgSgwGtpV1EndMarkerRx = _JnxMbgSgwGtpV1EndMarkerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 204),
    _JnxMbgSgwGtpV1EndMarkerRx_Type()
)
jnxMbgSgwGtpV1EndMarkerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EndMarkerRx.setStatus("current")
_JnxMbgSgwGtpV1EndMarkerTx_Type = Counter64
_JnxMbgSgwGtpV1EndMarkerTx_Object = MibTableColumn
jnxMbgSgwGtpV1EndMarkerTx = _JnxMbgSgwGtpV1EndMarkerTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 205),
    _JnxMbgSgwGtpV1EndMarkerTx_Type()
)
jnxMbgSgwGtpV1EndMarkerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EndMarkerTx.setStatus("current")
_JnxMbgSgwGtpV1EchoReqRx_Type = Counter64
_JnxMbgSgwGtpV1EchoReqRx_Object = MibTableColumn
jnxMbgSgwGtpV1EchoReqRx = _JnxMbgSgwGtpV1EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 206),
    _JnxMbgSgwGtpV1EchoReqRx_Type()
)
jnxMbgSgwGtpV1EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EchoReqRx.setStatus("current")
_JnxMbgSgwGtpV1EchoReqTx_Type = Counter64
_JnxMbgSgwGtpV1EchoReqTx_Object = MibTableColumn
jnxMbgSgwGtpV1EchoReqTx = _JnxMbgSgwGtpV1EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 207),
    _JnxMbgSgwGtpV1EchoReqTx_Type()
)
jnxMbgSgwGtpV1EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EchoReqTx.setStatus("current")
_JnxMbgSgwGtpV1EchoRespRx_Type = Counter64
_JnxMbgSgwGtpV1EchoRespRx_Object = MibTableColumn
jnxMbgSgwGtpV1EchoRespRx = _JnxMbgSgwGtpV1EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 208),
    _JnxMbgSgwGtpV1EchoRespRx_Type()
)
jnxMbgSgwGtpV1EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EchoRespRx.setStatus("current")
_JnxMbgSgwGtpV1EchoRespTx_Type = Counter64
_JnxMbgSgwGtpV1EchoRespTx_Object = MibTableColumn
jnxMbgSgwGtpV1EchoRespTx = _JnxMbgSgwGtpV1EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 209),
    _JnxMbgSgwGtpV1EchoRespTx_Type()
)
jnxMbgSgwGtpV1EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1EchoRespTx.setStatus("current")
_JnxMbgSgwGtpV1ErrIndRx_Type = Counter64
_JnxMbgSgwGtpV1ErrIndRx_Object = MibTableColumn
jnxMbgSgwGtpV1ErrIndRx = _JnxMbgSgwGtpV1ErrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 210),
    _JnxMbgSgwGtpV1ErrIndRx_Type()
)
jnxMbgSgwGtpV1ErrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1ErrIndRx.setStatus("current")
_JnxMbgSgwGtpV1ErrIndTx_Type = Counter64
_JnxMbgSgwGtpV1ErrIndTx_Object = MibTableColumn
jnxMbgSgwGtpV1ErrIndTx = _JnxMbgSgwGtpV1ErrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 211),
    _JnxMbgSgwGtpV1ErrIndTx_Type()
)
jnxMbgSgwGtpV1ErrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpV1ErrIndTx.setStatus("current")
_JnxMbgSgwSuspNotifRx_Type = Counter64
_JnxMbgSgwSuspNotifRx_Object = MibTableColumn
jnxMbgSgwSuspNotifRx = _JnxMbgSgwSuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 212),
    _JnxMbgSgwSuspNotifRx_Type()
)
jnxMbgSgwSuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspNotifRx.setStatus("current")
_JnxMbgSgwSuspNotifTx_Type = Counter64
_JnxMbgSgwSuspNotifTx_Object = MibTableColumn
jnxMbgSgwSuspNotifTx = _JnxMbgSgwSuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 213),
    _JnxMbgSgwSuspNotifTx_Type()
)
jnxMbgSgwSuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspNotifTx.setStatus("current")
_JnxMbgSgwSuspAckRx_Type = Counter64
_JnxMbgSgwSuspAckRx_Object = MibTableColumn
jnxMbgSgwSuspAckRx = _JnxMbgSgwSuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 214),
    _JnxMbgSgwSuspAckRx_Type()
)
jnxMbgSgwSuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspAckRx.setStatus("current")
_JnxMbgSgwSuspAckTx_Type = Counter64
_JnxMbgSgwSuspAckTx_Object = MibTableColumn
jnxMbgSgwSuspAckTx = _JnxMbgSgwSuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 215),
    _JnxMbgSgwSuspAckTx_Type()
)
jnxMbgSgwSuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspAckTx.setStatus("current")
_JnxMbgSgwResumeNotifRx_Type = Counter64
_JnxMbgSgwResumeNotifRx_Object = MibTableColumn
jnxMbgSgwResumeNotifRx = _JnxMbgSgwResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 216),
    _JnxMbgSgwResumeNotifRx_Type()
)
jnxMbgSgwResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwResumeNotifRx.setStatus("current")
_JnxMbgSgwResumeNotifTx_Type = Counter64
_JnxMbgSgwResumeNotifTx_Object = MibTableColumn
jnxMbgSgwResumeNotifTx = _JnxMbgSgwResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 217),
    _JnxMbgSgwResumeNotifTx_Type()
)
jnxMbgSgwResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwResumeNotifTx.setStatus("current")
_JnxMbgSgwResumeAckRx_Type = Counter64
_JnxMbgSgwResumeAckRx_Object = MibTableColumn
jnxMbgSgwResumeAckRx = _JnxMbgSgwResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 218),
    _JnxMbgSgwResumeAckRx_Type()
)
jnxMbgSgwResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwResumeAckRx.setStatus("current")
_JnxMbgSgwResumeAckTx_Type = Counter64
_JnxMbgSgwResumeAckTx_Object = MibTableColumn
jnxMbgSgwResumeAckTx = _JnxMbgSgwResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 219),
    _JnxMbgSgwResumeAckTx_Type()
)
jnxMbgSgwResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwResumeAckTx.setStatus("current")
_JnxMbgSgwS11PiggybackMsgRx_Type = Counter64
_JnxMbgSgwS11PiggybackMsgRx_Object = MibTableColumn
jnxMbgSgwS11PiggybackMsgRx = _JnxMbgSgwS11PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 220),
    _JnxMbgSgwS11PiggybackMsgRx_Type()
)
jnxMbgSgwS11PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS11PiggybackMsgRx.setStatus("current")
_JnxMbgSgwS11PiggybackMsgTx_Type = Counter64
_JnxMbgSgwS11PiggybackMsgTx_Object = MibTableColumn
jnxMbgSgwS11PiggybackMsgTx = _JnxMbgSgwS11PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 221),
    _JnxMbgSgwS11PiggybackMsgTx_Type()
)
jnxMbgSgwS11PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS11PiggybackMsgTx.setStatus("current")
_JnxMbgSgwS4PiggybackMsgRx_Type = Counter64
_JnxMbgSgwS4PiggybackMsgRx_Object = MibTableColumn
jnxMbgSgwS4PiggybackMsgRx = _JnxMbgSgwS4PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 222),
    _JnxMbgSgwS4PiggybackMsgRx_Type()
)
jnxMbgSgwS4PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS4PiggybackMsgRx.setStatus("current")
_JnxMbgSgwS4PiggybackMsgTx_Type = Counter64
_JnxMbgSgwS4PiggybackMsgTx_Object = MibTableColumn
jnxMbgSgwS4PiggybackMsgTx = _JnxMbgSgwS4PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 223),
    _JnxMbgSgwS4PiggybackMsgTx_Type()
)
jnxMbgSgwS4PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS4PiggybackMsgTx.setStatus("current")
_JnxMbgSgwS5PiggybackMsgRx_Type = Counter64
_JnxMbgSgwS5PiggybackMsgRx_Object = MibTableColumn
jnxMbgSgwS5PiggybackMsgRx = _JnxMbgSgwS5PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 224),
    _JnxMbgSgwS5PiggybackMsgRx_Type()
)
jnxMbgSgwS5PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS5PiggybackMsgRx.setStatus("current")
_JnxMbgSgwS5PiggybackMsgTx_Type = Counter64
_JnxMbgSgwS5PiggybackMsgTx_Object = MibTableColumn
jnxMbgSgwS5PiggybackMsgTx = _JnxMbgSgwS5PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 2, 1, 225),
    _JnxMbgSgwS5PiggybackMsgTx_Type()
)
jnxMbgSgwS5PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS5PiggybackMsgTx.setStatus("current")
_JnxMbgSgwGtpNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSgwGtpNotificationVars = _JnxMbgSgwGtpNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3)
)
_JnxMbgSgwGtpPeerName_Type = DisplayString
_JnxMbgSgwGtpPeerName_Object = MibScalar
jnxMbgSgwGtpPeerName = _JnxMbgSgwGtpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3, 1),
    _JnxMbgSgwGtpPeerName_Type()
)
jnxMbgSgwGtpPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPeerName.setStatus("current")
_JnxMbgSgwGtpAlarmStatCounter_Type = Unsigned32
_JnxMbgSgwGtpAlarmStatCounter_Object = MibScalar
jnxMbgSgwGtpAlarmStatCounter = _JnxMbgSgwGtpAlarmStatCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3, 2),
    _JnxMbgSgwGtpAlarmStatCounter_Type()
)
jnxMbgSgwGtpAlarmStatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpAlarmStatCounter.setStatus("current")
_JnxMbgSgwGtpInterfaceType_Type = DisplayString
_JnxMbgSgwGtpInterfaceType_Object = MibScalar
jnxMbgSgwGtpInterfaceType = _JnxMbgSgwGtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3, 3),
    _JnxMbgSgwGtpInterfaceType_Type()
)
jnxMbgSgwGtpInterfaceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpInterfaceType.setStatus("current")
_JnxMbgSgwGtpGwName_Type = DisplayString
_JnxMbgSgwGtpGwName_Object = MibScalar
jnxMbgSgwGtpGwName = _JnxMbgSgwGtpGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3, 4),
    _JnxMbgSgwGtpGwName_Type()
)
jnxMbgSgwGtpGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpGwName.setStatus("current")
_JnxMbgSgwGtpGwIndex_Type = Unsigned32
_JnxMbgSgwGtpGwIndex_Object = MibScalar
jnxMbgSgwGtpGwIndex = _JnxMbgSgwGtpGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 3, 5),
    _JnxMbgSgwGtpGwIndex_Type()
)
jnxMbgSgwGtpGwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpGwIndex.setStatus("current")
_JnxMbgSgwGtpIfStatsTable_Object = MibTable
jnxMbgSgwGtpIfStatsTable = _JnxMbgSgwGtpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpIfStatsTable.setStatus("current")
_JnxMbgSgwGtpIfStatsEntry_Object = MibTableRow
jnxMbgSgwGtpIfStatsEntry = _JnxMbgSgwGtpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1)
)
jnxMbgSgwGtpIfStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwIfIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpIfStatsEntry.setStatus("current")
_JnxMbgSgwIfIndex_Type = Unsigned32
_JnxMbgSgwIfIndex_Object = MibTableColumn
jnxMbgSgwIfIndex = _JnxMbgSgwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 1),
    _JnxMbgSgwIfIndex_Type()
)
jnxMbgSgwIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSgwIfIndex.setStatus("current")
_JnxMbgSgwIfType_Type = DisplayString
_JnxMbgSgwIfType_Object = MibTableColumn
jnxMbgSgwIfType = _JnxMbgSgwIfType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 2),
    _JnxMbgSgwIfType_Type()
)
jnxMbgSgwIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfType.setStatus("current")
_JnxMbgSgwIfRxPacketsDropped_Type = Counter64
_JnxMbgSgwIfRxPacketsDropped_Object = MibTableColumn
jnxMbgSgwIfRxPacketsDropped = _JnxMbgSgwIfRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 3),
    _JnxMbgSgwIfRxPacketsDropped_Type()
)
jnxMbgSgwIfRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfRxPacketsDropped.setStatus("current")
_JnxMbgSgwIfPacketAllocFail_Type = Counter64
_JnxMbgSgwIfPacketAllocFail_Object = MibTableColumn
jnxMbgSgwIfPacketAllocFail = _JnxMbgSgwIfPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 4),
    _JnxMbgSgwIfPacketAllocFail_Type()
)
jnxMbgSgwIfPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfPacketAllocFail.setStatus("current")
_JnxMbgSgwIfPacketSendFail_Type = Counter64
_JnxMbgSgwIfPacketSendFail_Object = MibTableColumn
jnxMbgSgwIfPacketSendFail = _JnxMbgSgwIfPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 5),
    _JnxMbgSgwIfPacketSendFail_Type()
)
jnxMbgSgwIfPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfPacketSendFail.setStatus("current")
_JnxMbgSgwIfIPVerErrRx_Type = Counter64
_JnxMbgSgwIfIPVerErrRx_Object = MibTableColumn
jnxMbgSgwIfIPVerErrRx = _JnxMbgSgwIfIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 6),
    _JnxMbgSgwIfIPVerErrRx_Type()
)
jnxMbgSgwIfIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfIPVerErrRx.setStatus("current")
_JnxMbgSgwIfIPProtoErrRx_Type = Counter64
_JnxMbgSgwIfIPProtoErrRx_Object = MibTableColumn
jnxMbgSgwIfIPProtoErrRx = _JnxMbgSgwIfIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 7),
    _JnxMbgSgwIfIPProtoErrRx_Type()
)
jnxMbgSgwIfIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfIPProtoErrRx.setStatus("current")
_JnxMbgSgwIfGTPPortErrRx_Type = Counter64
_JnxMbgSgwIfGTPPortErrRx_Object = MibTableColumn
jnxMbgSgwIfGTPPortErrRx = _JnxMbgSgwIfGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 8),
    _JnxMbgSgwIfGTPPortErrRx_Type()
)
jnxMbgSgwIfGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGTPPortErrRx.setStatus("current")
_JnxMbgSgwIfGTPUnknVerRx_Type = Counter64
_JnxMbgSgwIfGTPUnknVerRx_Object = MibTableColumn
jnxMbgSgwIfGTPUnknVerRx = _JnxMbgSgwIfGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 9),
    _JnxMbgSgwIfGTPUnknVerRx_Type()
)
jnxMbgSgwIfGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGTPUnknVerRx.setStatus("current")
_JnxMbgSgwIfPcktLenErrRx_Type = Counter64
_JnxMbgSgwIfPcktLenErrRx_Object = MibTableColumn
jnxMbgSgwIfPcktLenErrRx = _JnxMbgSgwIfPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 10),
    _JnxMbgSgwIfPcktLenErrRx_Type()
)
jnxMbgSgwIfPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfPcktLenErrRx.setStatus("current")
_JnxMbgSgwIfUnknMsgRx_Type = Counter64
_JnxMbgSgwIfUnknMsgRx_Object = MibTableColumn
jnxMbgSgwIfUnknMsgRx = _JnxMbgSgwIfUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 11),
    _JnxMbgSgwIfUnknMsgRx_Type()
)
jnxMbgSgwIfUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUnknMsgRx.setStatus("current")
_JnxMbgSgwIfProtocolErrRx_Type = Counter64
_JnxMbgSgwIfProtocolErrRx_Object = MibTableColumn
jnxMbgSgwIfProtocolErrRx = _JnxMbgSgwIfProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 12),
    _JnxMbgSgwIfProtocolErrRx_Type()
)
jnxMbgSgwIfProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfProtocolErrRx.setStatus("current")
_JnxMbgSgwIfUnSupportedMsgRx_Type = Counter64
_JnxMbgSgwIfUnSupportedMsgRx_Object = MibTableColumn
jnxMbgSgwIfUnSupportedMsgRx = _JnxMbgSgwIfUnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 13),
    _JnxMbgSgwIfUnSupportedMsgRx_Type()
)
jnxMbgSgwIfUnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUnSupportedMsgRx.setStatus("current")
_JnxMbgSgwIfT3RespTmrExpRx_Type = Counter64
_JnxMbgSgwIfT3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwIfT3RespTmrExpRx = _JnxMbgSgwIfT3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 14),
    _JnxMbgSgwIfT3RespTmrExpRx_Type()
)
jnxMbgSgwIfT3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfT3RespTmrExpRx.setStatus("current")
_JnxMbgSgwIfV2NumMsgRx_Type = Counter64
_JnxMbgSgwIfV2NumMsgRx_Object = MibTableColumn
jnxMbgSgwIfV2NumMsgRx = _JnxMbgSgwIfV2NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 15),
    _JnxMbgSgwIfV2NumMsgRx_Type()
)
jnxMbgSgwIfV2NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2NumMsgRx.setStatus("current")
_JnxMbgSgwIfV2NumMsgTx_Type = Counter64
_JnxMbgSgwIfV2NumMsgTx_Object = MibTableColumn
jnxMbgSgwIfV2NumMsgTx = _JnxMbgSgwIfV2NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 16),
    _JnxMbgSgwIfV2NumMsgTx_Type()
)
jnxMbgSgwIfV2NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2NumMsgTx.setStatus("current")
_JnxMbgSgwIfV2NumBytesRx_Type = Counter64
_JnxMbgSgwIfV2NumBytesRx_Object = MibTableColumn
jnxMbgSgwIfV2NumBytesRx = _JnxMbgSgwIfV2NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 17),
    _JnxMbgSgwIfV2NumBytesRx_Type()
)
jnxMbgSgwIfV2NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2NumBytesRx.setStatus("current")
_JnxMbgSgwIfV2NumBytesTx_Type = Counter64
_JnxMbgSgwIfV2NumBytesTx_Object = MibTableColumn
jnxMbgSgwIfV2NumBytesTx = _JnxMbgSgwIfV2NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 18),
    _JnxMbgSgwIfV2NumBytesTx_Type()
)
jnxMbgSgwIfV2NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2NumBytesTx.setStatus("current")
_JnxMbgSgwIfV2EchoReqRx_Type = Counter64
_JnxMbgSgwIfV2EchoReqRx_Object = MibTableColumn
jnxMbgSgwIfV2EchoReqRx = _JnxMbgSgwIfV2EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 19),
    _JnxMbgSgwIfV2EchoReqRx_Type()
)
jnxMbgSgwIfV2EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2EchoReqRx.setStatus("current")
_JnxMbgSgwIfV2EchoReqTx_Type = Counter64
_JnxMbgSgwIfV2EchoReqTx_Object = MibTableColumn
jnxMbgSgwIfV2EchoReqTx = _JnxMbgSgwIfV2EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 20),
    _JnxMbgSgwIfV2EchoReqTx_Type()
)
jnxMbgSgwIfV2EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2EchoReqTx.setStatus("current")
_JnxMbgSgwIfV2EchoRespRx_Type = Counter64
_JnxMbgSgwIfV2EchoRespRx_Object = MibTableColumn
jnxMbgSgwIfV2EchoRespRx = _JnxMbgSgwIfV2EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 21),
    _JnxMbgSgwIfV2EchoRespRx_Type()
)
jnxMbgSgwIfV2EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2EchoRespRx.setStatus("current")
_JnxMbgSgwIfV2EchoRespTx_Type = Counter64
_JnxMbgSgwIfV2EchoRespTx_Object = MibTableColumn
jnxMbgSgwIfV2EchoRespTx = _JnxMbgSgwIfV2EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 22),
    _JnxMbgSgwIfV2EchoRespTx_Type()
)
jnxMbgSgwIfV2EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2EchoRespTx.setStatus("current")
_JnxMbgSgwIfV2VerNotSupRx_Type = Counter64
_JnxMbgSgwIfV2VerNotSupRx_Object = MibTableColumn
jnxMbgSgwIfV2VerNotSupRx = _JnxMbgSgwIfV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 23),
    _JnxMbgSgwIfV2VerNotSupRx_Type()
)
jnxMbgSgwIfV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2VerNotSupRx.setStatus("current")
_JnxMbgSgwIfV2VerNotSupTx_Type = Counter64
_JnxMbgSgwIfV2VerNotSupTx_Object = MibTableColumn
jnxMbgSgwIfV2VerNotSupTx = _JnxMbgSgwIfV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 24),
    _JnxMbgSgwIfV2VerNotSupTx_Type()
)
jnxMbgSgwIfV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfV2VerNotSupTx.setStatus("current")
_JnxMbgSgwIfCreateSessReqRx_Type = Counter64
_JnxMbgSgwIfCreateSessReqRx_Object = MibTableColumn
jnxMbgSgwIfCreateSessReqRx = _JnxMbgSgwIfCreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 25),
    _JnxMbgSgwIfCreateSessReqRx_Type()
)
jnxMbgSgwIfCreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCreateSessReqRx.setStatus("current")
_JnxMbgSgwIfCreateSessReqTx_Type = Counter64
_JnxMbgSgwIfCreateSessReqTx_Object = MibTableColumn
jnxMbgSgwIfCreateSessReqTx = _JnxMbgSgwIfCreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 26),
    _JnxMbgSgwIfCreateSessReqTx_Type()
)
jnxMbgSgwIfCreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCreateSessReqTx.setStatus("current")
_JnxMbgSgwIfCreateSessRspRx_Type = Counter64
_JnxMbgSgwIfCreateSessRspRx_Object = MibTableColumn
jnxMbgSgwIfCreateSessRspRx = _JnxMbgSgwIfCreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 27),
    _JnxMbgSgwIfCreateSessRspRx_Type()
)
jnxMbgSgwIfCreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCreateSessRspRx.setStatus("current")
_JnxMbgSgwIfCreateSessRspTx_Type = Counter64
_JnxMbgSgwIfCreateSessRspTx_Object = MibTableColumn
jnxMbgSgwIfCreateSessRspTx = _JnxMbgSgwIfCreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 28),
    _JnxMbgSgwIfCreateSessRspTx_Type()
)
jnxMbgSgwIfCreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCreateSessRspTx.setStatus("current")
_JnxMbgSgwIfModBrReqRx_Type = Counter64
_JnxMbgSgwIfModBrReqRx_Object = MibTableColumn
jnxMbgSgwIfModBrReqRx = _JnxMbgSgwIfModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 29),
    _JnxMbgSgwIfModBrReqRx_Type()
)
jnxMbgSgwIfModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrReqRx.setStatus("current")
_JnxMbgSgwIfModBrReqTx_Type = Counter64
_JnxMbgSgwIfModBrReqTx_Object = MibTableColumn
jnxMbgSgwIfModBrReqTx = _JnxMbgSgwIfModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 30),
    _JnxMbgSgwIfModBrReqTx_Type()
)
jnxMbgSgwIfModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrReqTx.setStatus("current")
_JnxMbgSgwIfModBrRspRx_Type = Counter64
_JnxMbgSgwIfModBrRspRx_Object = MibTableColumn
jnxMbgSgwIfModBrRspRx = _JnxMbgSgwIfModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 31),
    _JnxMbgSgwIfModBrRspRx_Type()
)
jnxMbgSgwIfModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrRspRx.setStatus("current")
_JnxMbgSgwIfModBrRspTx_Type = Counter64
_JnxMbgSgwIfModBrRspTx_Object = MibTableColumn
jnxMbgSgwIfModBrRspTx = _JnxMbgSgwIfModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 32),
    _JnxMbgSgwIfModBrRspTx_Type()
)
jnxMbgSgwIfModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrRspTx.setStatus("current")
_JnxMbgSgwIfDelSessReqRx_Type = Counter64
_JnxMbgSgwIfDelSessReqRx_Object = MibTableColumn
jnxMbgSgwIfDelSessReqRx = _JnxMbgSgwIfDelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 33),
    _JnxMbgSgwIfDelSessReqRx_Type()
)
jnxMbgSgwIfDelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelSessReqRx.setStatus("current")
_JnxMbgSgwIfDelSessReqTx_Type = Counter64
_JnxMbgSgwIfDelSessReqTx_Object = MibTableColumn
jnxMbgSgwIfDelSessReqTx = _JnxMbgSgwIfDelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 34),
    _JnxMbgSgwIfDelSessReqTx_Type()
)
jnxMbgSgwIfDelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelSessReqTx.setStatus("current")
_JnxMbgSgwIfDelSessRspRx_Type = Counter64
_JnxMbgSgwIfDelSessRspRx_Object = MibTableColumn
jnxMbgSgwIfDelSessRspRx = _JnxMbgSgwIfDelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 35),
    _JnxMbgSgwIfDelSessRspRx_Type()
)
jnxMbgSgwIfDelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelSessRspRx.setStatus("current")
_JnxMbgSgwIfDelSessRspTx_Type = Counter64
_JnxMbgSgwIfDelSessRspTx_Object = MibTableColumn
jnxMbgSgwIfDelSessRspTx = _JnxMbgSgwIfDelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 36),
    _JnxMbgSgwIfDelSessRspTx_Type()
)
jnxMbgSgwIfDelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelSessRspTx.setStatus("current")
_JnxMbgSgwIfCrtBrReqRx_Type = Counter64
_JnxMbgSgwIfCrtBrReqRx_Object = MibTableColumn
jnxMbgSgwIfCrtBrReqRx = _JnxMbgSgwIfCrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 37),
    _JnxMbgSgwIfCrtBrReqRx_Type()
)
jnxMbgSgwIfCrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrtBrReqRx.setStatus("current")
_JnxMbgSgwIfCrtBrReqTx_Type = Counter64
_JnxMbgSgwIfCrtBrReqTx_Object = MibTableColumn
jnxMbgSgwIfCrtBrReqTx = _JnxMbgSgwIfCrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 38),
    _JnxMbgSgwIfCrtBrReqTx_Type()
)
jnxMbgSgwIfCrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrtBrReqTx.setStatus("current")
_JnxMbgSgwIfCrtBrRspRx_Type = Counter64
_JnxMbgSgwIfCrtBrRspRx_Object = MibTableColumn
jnxMbgSgwIfCrtBrRspRx = _JnxMbgSgwIfCrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 39),
    _JnxMbgSgwIfCrtBrRspRx_Type()
)
jnxMbgSgwIfCrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrtBrRspRx.setStatus("current")
_JnxMbgSgwIfCrtBrRspTx_Type = Counter64
_JnxMbgSgwIfCrtBrRspTx_Object = MibTableColumn
jnxMbgSgwIfCrtBrRspTx = _JnxMbgSgwIfCrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 40),
    _JnxMbgSgwIfCrtBrRspTx_Type()
)
jnxMbgSgwIfCrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrtBrRspTx.setStatus("current")
_JnxMbgSgwIfUpdBrReqRx_Type = Counter64
_JnxMbgSgwIfUpdBrReqRx_Object = MibTableColumn
jnxMbgSgwIfUpdBrReqRx = _JnxMbgSgwIfUpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 41),
    _JnxMbgSgwIfUpdBrReqRx_Type()
)
jnxMbgSgwIfUpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdBrReqRx.setStatus("current")
_JnxMbgSgwIfUpdBrReqTx_Type = Counter64
_JnxMbgSgwIfUpdBrReqTx_Object = MibTableColumn
jnxMbgSgwIfUpdBrReqTx = _JnxMbgSgwIfUpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 42),
    _JnxMbgSgwIfUpdBrReqTx_Type()
)
jnxMbgSgwIfUpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdBrReqTx.setStatus("current")
_JnxMbgSgwIfUpdBrRspRx_Type = Counter64
_JnxMbgSgwIfUpdBrRspRx_Object = MibTableColumn
jnxMbgSgwIfUpdBrRspRx = _JnxMbgSgwIfUpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 43),
    _JnxMbgSgwIfUpdBrRspRx_Type()
)
jnxMbgSgwIfUpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdBrRspRx.setStatus("current")
_JnxMbgSgwIfUpdBrRspTx_Type = Counter64
_JnxMbgSgwIfUpdBrRspTx_Object = MibTableColumn
jnxMbgSgwIfUpdBrRspTx = _JnxMbgSgwIfUpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 44),
    _JnxMbgSgwIfUpdBrRspTx_Type()
)
jnxMbgSgwIfUpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdBrRspTx.setStatus("current")
_JnxMbgSgwIfDelBrReqRx_Type = Counter64
_JnxMbgSgwIfDelBrReqRx_Object = MibTableColumn
jnxMbgSgwIfDelBrReqRx = _JnxMbgSgwIfDelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 45),
    _JnxMbgSgwIfDelBrReqRx_Type()
)
jnxMbgSgwIfDelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrReqRx.setStatus("current")
_JnxMbgSgwIfDelBrReqTx_Type = Counter64
_JnxMbgSgwIfDelBrReqTx_Object = MibTableColumn
jnxMbgSgwIfDelBrReqTx = _JnxMbgSgwIfDelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 46),
    _JnxMbgSgwIfDelBrReqTx_Type()
)
jnxMbgSgwIfDelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrReqTx.setStatus("current")
_JnxMbgSgwIfDelBrRspRx_Type = Counter64
_JnxMbgSgwIfDelBrRspRx_Object = MibTableColumn
jnxMbgSgwIfDelBrRspRx = _JnxMbgSgwIfDelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 47),
    _JnxMbgSgwIfDelBrRspRx_Type()
)
jnxMbgSgwIfDelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrRspRx.setStatus("current")
_JnxMbgSgwIfDelBrRspTx_Type = Counter64
_JnxMbgSgwIfDelBrRspTx_Object = MibTableColumn
jnxMbgSgwIfDelBrRspTx = _JnxMbgSgwIfDelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 48),
    _JnxMbgSgwIfDelBrRspTx_Type()
)
jnxMbgSgwIfDelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrRspTx.setStatus("current")
_JnxMbgSgwIfDelConnSetReqRx_Type = Counter64
_JnxMbgSgwIfDelConnSetReqRx_Object = MibTableColumn
jnxMbgSgwIfDelConnSetReqRx = _JnxMbgSgwIfDelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 49),
    _JnxMbgSgwIfDelConnSetReqRx_Type()
)
jnxMbgSgwIfDelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelConnSetReqRx.setStatus("current")
_JnxMbgSgwIfDelConnSetReqTx_Type = Counter64
_JnxMbgSgwIfDelConnSetReqTx_Object = MibTableColumn
jnxMbgSgwIfDelConnSetReqTx = _JnxMbgSgwIfDelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 50),
    _JnxMbgSgwIfDelConnSetReqTx_Type()
)
jnxMbgSgwIfDelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelConnSetReqTx.setStatus("current")
_JnxMbgSgwIfDelConnSetRspRx_Type = Counter64
_JnxMbgSgwIfDelConnSetRspRx_Object = MibTableColumn
jnxMbgSgwIfDelConnSetRspRx = _JnxMbgSgwIfDelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 51),
    _JnxMbgSgwIfDelConnSetRspRx_Type()
)
jnxMbgSgwIfDelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelConnSetRspRx.setStatus("current")
_JnxMbgSgwIfDelConnSetRspTx_Type = Counter64
_JnxMbgSgwIfDelConnSetRspTx_Object = MibTableColumn
jnxMbgSgwIfDelConnSetRspTx = _JnxMbgSgwIfDelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 52),
    _JnxMbgSgwIfDelConnSetRspTx_Type()
)
jnxMbgSgwIfDelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelConnSetRspTx.setStatus("current")
_JnxMbgSgwIfUpdConnSetReqRx_Type = Counter64
_JnxMbgSgwIfUpdConnSetReqRx_Object = MibTableColumn
jnxMbgSgwIfUpdConnSetReqRx = _JnxMbgSgwIfUpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 53),
    _JnxMbgSgwIfUpdConnSetReqRx_Type()
)
jnxMbgSgwIfUpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdConnSetReqRx.setStatus("current")
_JnxMbgSgwIfUpdConnSetReqTx_Type = Counter64
_JnxMbgSgwIfUpdConnSetReqTx_Object = MibTableColumn
jnxMbgSgwIfUpdConnSetReqTx = _JnxMbgSgwIfUpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 54),
    _JnxMbgSgwIfUpdConnSetReqTx_Type()
)
jnxMbgSgwIfUpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdConnSetReqTx.setStatus("current")
_JnxMbgSgwIfUpdConnSetRspRx_Type = Counter64
_JnxMbgSgwIfUpdConnSetRspRx_Object = MibTableColumn
jnxMbgSgwIfUpdConnSetRspRx = _JnxMbgSgwIfUpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 55),
    _JnxMbgSgwIfUpdConnSetRspRx_Type()
)
jnxMbgSgwIfUpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdConnSetRspRx.setStatus("current")
_JnxMbgSgwIfUpdConnSetRspTx_Type = Counter64
_JnxMbgSgwIfUpdConnSetRspTx_Object = MibTableColumn
jnxMbgSgwIfUpdConnSetRspTx = _JnxMbgSgwIfUpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 56),
    _JnxMbgSgwIfUpdConnSetRspTx_Type()
)
jnxMbgSgwIfUpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfUpdConnSetRspTx.setStatus("current")
_JnxMbgSgwIfModBrCmdRx_Type = Counter64
_JnxMbgSgwIfModBrCmdRx_Object = MibTableColumn
jnxMbgSgwIfModBrCmdRx = _JnxMbgSgwIfModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 57),
    _JnxMbgSgwIfModBrCmdRx_Type()
)
jnxMbgSgwIfModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrCmdRx.setStatus("current")
_JnxMbgSgwIfModBrCmdTx_Type = Counter64
_JnxMbgSgwIfModBrCmdTx_Object = MibTableColumn
jnxMbgSgwIfModBrCmdTx = _JnxMbgSgwIfModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 58),
    _JnxMbgSgwIfModBrCmdTx_Type()
)
jnxMbgSgwIfModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrCmdTx.setStatus("current")
_JnxMbgSgwIfModBrFlrIndRx_Type = Counter64
_JnxMbgSgwIfModBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwIfModBrFlrIndRx = _JnxMbgSgwIfModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 59),
    _JnxMbgSgwIfModBrFlrIndRx_Type()
)
jnxMbgSgwIfModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrFlrIndRx.setStatus("current")
_JnxMbgSgwIfModBrFlrIndTx_Type = Counter64
_JnxMbgSgwIfModBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwIfModBrFlrIndTx = _JnxMbgSgwIfModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 60),
    _JnxMbgSgwIfModBrFlrIndTx_Type()
)
jnxMbgSgwIfModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfModBrFlrIndTx.setStatus("current")
_JnxMbgSgwIfDelBrCmdRx_Type = Counter64
_JnxMbgSgwIfDelBrCmdRx_Object = MibTableColumn
jnxMbgSgwIfDelBrCmdRx = _JnxMbgSgwIfDelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 61),
    _JnxMbgSgwIfDelBrCmdRx_Type()
)
jnxMbgSgwIfDelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrCmdRx.setStatus("current")
_JnxMbgSgwIfDelBrCmdTx_Type = Counter64
_JnxMbgSgwIfDelBrCmdTx_Object = MibTableColumn
jnxMbgSgwIfDelBrCmdTx = _JnxMbgSgwIfDelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 62),
    _JnxMbgSgwIfDelBrCmdTx_Type()
)
jnxMbgSgwIfDelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrCmdTx.setStatus("current")
_JnxMbgSgwIfDelBrFlrIndRx_Type = Counter64
_JnxMbgSgwIfDelBrFlrIndRx_Object = MibTableColumn
jnxMbgSgwIfDelBrFlrIndRx = _JnxMbgSgwIfDelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 63),
    _JnxMbgSgwIfDelBrFlrIndRx_Type()
)
jnxMbgSgwIfDelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrFlrIndRx.setStatus("current")
_JnxMbgSgwIfDelBrFlrIndTx_Type = Counter64
_JnxMbgSgwIfDelBrFlrIndTx_Object = MibTableColumn
jnxMbgSgwIfDelBrFlrIndTx = _JnxMbgSgwIfDelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 64),
    _JnxMbgSgwIfDelBrFlrIndTx_Type()
)
jnxMbgSgwIfDelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelBrFlrIndTx.setStatus("current")
_JnxMbgSgwIfBrResCmdRx_Type = Counter64
_JnxMbgSgwIfBrResCmdRx_Object = MibTableColumn
jnxMbgSgwIfBrResCmdRx = _JnxMbgSgwIfBrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 65),
    _JnxMbgSgwIfBrResCmdRx_Type()
)
jnxMbgSgwIfBrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfBrResCmdRx.setStatus("current")
_JnxMbgSgwIfBrResCmdTx_Type = Counter64
_JnxMbgSgwIfBrResCmdTx_Object = MibTableColumn
jnxMbgSgwIfBrResCmdTx = _JnxMbgSgwIfBrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 66),
    _JnxMbgSgwIfBrResCmdTx_Type()
)
jnxMbgSgwIfBrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfBrResCmdTx.setStatus("current")
_JnxMbgSgwIfBrResFlrIndRx_Type = Counter64
_JnxMbgSgwIfBrResFlrIndRx_Object = MibTableColumn
jnxMbgSgwIfBrResFlrIndRx = _JnxMbgSgwIfBrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 67),
    _JnxMbgSgwIfBrResFlrIndRx_Type()
)
jnxMbgSgwIfBrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfBrResFlrIndRx.setStatus("current")
_JnxMbgSgwIfBrResFlrIndTx_Type = Counter64
_JnxMbgSgwIfBrResFlrIndTx_Object = MibTableColumn
jnxMbgSgwIfBrResFlrIndTx = _JnxMbgSgwIfBrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 68),
    _JnxMbgSgwIfBrResFlrIndTx_Type()
)
jnxMbgSgwIfBrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfBrResFlrIndTx.setStatus("current")
_JnxMbgSgwIfRelAcsBrReqRx_Type = Counter64
_JnxMbgSgwIfRelAcsBrReqRx_Object = MibTableColumn
jnxMbgSgwIfRelAcsBrReqRx = _JnxMbgSgwIfRelAcsBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 69),
    _JnxMbgSgwIfRelAcsBrReqRx_Type()
)
jnxMbgSgwIfRelAcsBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfRelAcsBrReqRx.setStatus("current")
_JnxMbgSgwIfRelAcsBrReqTx_Type = Counter64
_JnxMbgSgwIfRelAcsBrReqTx_Object = MibTableColumn
jnxMbgSgwIfRelAcsBrReqTx = _JnxMbgSgwIfRelAcsBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 70),
    _JnxMbgSgwIfRelAcsBrReqTx_Type()
)
jnxMbgSgwIfRelAcsBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfRelAcsBrReqTx.setStatus("current")
_JnxMbgSgwIfRelAcsBrRespRx_Type = Counter64
_JnxMbgSgwIfRelAcsBrRespRx_Object = MibTableColumn
jnxMbgSgwIfRelAcsBrRespRx = _JnxMbgSgwIfRelAcsBrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 71),
    _JnxMbgSgwIfRelAcsBrRespRx_Type()
)
jnxMbgSgwIfRelAcsBrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfRelAcsBrRespRx.setStatus("current")
_JnxMbgSgwIfRelAcsBrRespTx_Type = Counter64
_JnxMbgSgwIfRelAcsBrRespTx_Object = MibTableColumn
jnxMbgSgwIfRelAcsBrRespTx = _JnxMbgSgwIfRelAcsBrRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 72),
    _JnxMbgSgwIfRelAcsBrRespTx_Type()
)
jnxMbgSgwIfRelAcsBrRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfRelAcsBrRespTx.setStatus("current")
_JnxMbgSgwIfCrIndTunReqRx_Type = Counter64
_JnxMbgSgwIfCrIndTunReqRx_Object = MibTableColumn
jnxMbgSgwIfCrIndTunReqRx = _JnxMbgSgwIfCrIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 73),
    _JnxMbgSgwIfCrIndTunReqRx_Type()
)
jnxMbgSgwIfCrIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrIndTunReqRx.setStatus("current")
_JnxMbgSgwIfCrIndTunReqTx_Type = Counter64
_JnxMbgSgwIfCrIndTunReqTx_Object = MibTableColumn
jnxMbgSgwIfCrIndTunReqTx = _JnxMbgSgwIfCrIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 74),
    _JnxMbgSgwIfCrIndTunReqTx_Type()
)
jnxMbgSgwIfCrIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrIndTunReqTx.setStatus("current")
_JnxMbgSgwIfCrIndTunRespRx_Type = Counter64
_JnxMbgSgwIfCrIndTunRespRx_Object = MibTableColumn
jnxMbgSgwIfCrIndTunRespRx = _JnxMbgSgwIfCrIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 75),
    _JnxMbgSgwIfCrIndTunRespRx_Type()
)
jnxMbgSgwIfCrIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrIndTunRespRx.setStatus("current")
_JnxMbgSgwIfCrIndTunRespTx_Type = Counter64
_JnxMbgSgwIfCrIndTunRespTx_Object = MibTableColumn
jnxMbgSgwIfCrIndTunRespTx = _JnxMbgSgwIfCrIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 76),
    _JnxMbgSgwIfCrIndTunRespTx_Type()
)
jnxMbgSgwIfCrIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfCrIndTunRespTx.setStatus("current")
_JnxMbgSgwIfDelIndTunReqRx_Type = Counter64
_JnxMbgSgwIfDelIndTunReqRx_Object = MibTableColumn
jnxMbgSgwIfDelIndTunReqRx = _JnxMbgSgwIfDelIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 77),
    _JnxMbgSgwIfDelIndTunReqRx_Type()
)
jnxMbgSgwIfDelIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelIndTunReqRx.setStatus("current")
_JnxMbgSgwIfDelIndTunReqTx_Type = Counter64
_JnxMbgSgwIfDelIndTunReqTx_Object = MibTableColumn
jnxMbgSgwIfDelIndTunReqTx = _JnxMbgSgwIfDelIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 78),
    _JnxMbgSgwIfDelIndTunReqTx_Type()
)
jnxMbgSgwIfDelIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelIndTunReqTx.setStatus("current")
_JnxMbgSgwIfDelIndTunRespRx_Type = Counter64
_JnxMbgSgwIfDelIndTunRespRx_Object = MibTableColumn
jnxMbgSgwIfDelIndTunRespRx = _JnxMbgSgwIfDelIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 79),
    _JnxMbgSgwIfDelIndTunRespRx_Type()
)
jnxMbgSgwIfDelIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelIndTunRespRx.setStatus("current")
_JnxMbgSgwIfDelIndTunRespTx_Type = Counter64
_JnxMbgSgwIfDelIndTunRespTx_Object = MibTableColumn
jnxMbgSgwIfDelIndTunRespTx = _JnxMbgSgwIfDelIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 80),
    _JnxMbgSgwIfDelIndTunRespTx_Type()
)
jnxMbgSgwIfDelIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDelIndTunRespTx.setStatus("current")
_JnxMbgSgwIfDlDataNotifRx_Type = Counter64
_JnxMbgSgwIfDlDataNotifRx_Object = MibTableColumn
jnxMbgSgwIfDlDataNotifRx = _JnxMbgSgwIfDlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 81),
    _JnxMbgSgwIfDlDataNotifRx_Type()
)
jnxMbgSgwIfDlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataNotifRx.setStatus("current")
_JnxMbgSgwIfDlDataNotifTx_Type = Counter64
_JnxMbgSgwIfDlDataNotifTx_Object = MibTableColumn
jnxMbgSgwIfDlDataNotifTx = _JnxMbgSgwIfDlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 82),
    _JnxMbgSgwIfDlDataNotifTx_Type()
)
jnxMbgSgwIfDlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataNotifTx.setStatus("current")
_JnxMbgSgwIfDlDataAckRx_Type = Counter64
_JnxMbgSgwIfDlDataAckRx_Object = MibTableColumn
jnxMbgSgwIfDlDataAckRx = _JnxMbgSgwIfDlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 83),
    _JnxMbgSgwIfDlDataAckRx_Type()
)
jnxMbgSgwIfDlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataAckRx.setStatus("current")
_JnxMbgSgwIfDlDataAckTx_Type = Counter64
_JnxMbgSgwIfDlDataAckTx_Object = MibTableColumn
jnxMbgSgwIfDlDataAckTx = _JnxMbgSgwIfDlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 84),
    _JnxMbgSgwIfDlDataAckTx_Type()
)
jnxMbgSgwIfDlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataAckTx.setStatus("current")
_JnxMbgSgwIfDlDataNotiFlrIndRx_Type = Counter64
_JnxMbgSgwIfDlDataNotiFlrIndRx_Object = MibTableColumn
jnxMbgSgwIfDlDataNotiFlrIndRx = _JnxMbgSgwIfDlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 85),
    _JnxMbgSgwIfDlDataNotiFlrIndRx_Type()
)
jnxMbgSgwIfDlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataNotiFlrIndRx.setStatus("current")
_JnxMbgSgwIfDlDataNotiFlrIndTx_Type = Counter64
_JnxMbgSgwIfDlDataNotiFlrIndTx_Object = MibTableColumn
jnxMbgSgwIfDlDataNotiFlrIndTx = _JnxMbgSgwIfDlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 86),
    _JnxMbgSgwIfDlDataNotiFlrIndTx_Type()
)
jnxMbgSgwIfDlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfDlDataNotiFlrIndTx.setStatus("current")
_JnxMbgSgwIfStopPagingIndRx_Type = Counter64
_JnxMbgSgwIfStopPagingIndRx_Object = MibTableColumn
jnxMbgSgwIfStopPagingIndRx = _JnxMbgSgwIfStopPagingIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 87),
    _JnxMbgSgwIfStopPagingIndRx_Type()
)
jnxMbgSgwIfStopPagingIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfStopPagingIndRx.setStatus("current")
_JnxMbgSgwIfStopPagingIndTx_Type = Counter64
_JnxMbgSgwIfStopPagingIndTx_Object = MibTableColumn
jnxMbgSgwIfStopPagingIndTx = _JnxMbgSgwIfStopPagingIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 88),
    _JnxMbgSgwIfStopPagingIndTx_Type()
)
jnxMbgSgwIfStopPagingIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfStopPagingIndTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsReqAcceptRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsReqAcceptRx = _JnxMbgSgwIfGtpV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 89),
    _JnxMbgSgwIfGtpV2ICsReqAcceptRx_Type()
)
jnxMbgSgwIfGtpV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsReqAcceptRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsReqAcceptTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsReqAcceptTx = _JnxMbgSgwIfGtpV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 90),
    _JnxMbgSgwIfGtpV2ICsReqAcceptTx_Type()
)
jnxMbgSgwIfGtpV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsReqAcceptTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAcceptPartRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAcceptPartRx = _JnxMbgSgwIfGtpV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 91),
    _JnxMbgSgwIfGtpV2ICsAcceptPartRx_Type()
)
jnxMbgSgwIfGtpV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAcceptPartRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAcceptPartTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAcceptPartTx = _JnxMbgSgwIfGtpV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 92),
    _JnxMbgSgwIfGtpV2ICsAcceptPartTx_Type()
)
jnxMbgSgwIfGtpV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAcceptPartTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNewPTNPrefRx = _JnxMbgSgwIfGtpV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 93),
    _JnxMbgSgwIfGtpV2ICsNewPTNPrefRx_Type()
)
jnxMbgSgwIfGtpV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNewPTNPrefTx = _JnxMbgSgwIfGtpV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 94),
    _JnxMbgSgwIfGtpV2ICsNewPTNPrefTx_Type()
)
jnxMbgSgwIfGtpV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNPTSIAdbrRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNPTSIAdbrRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNPTSIAdbrRx = _JnxMbgSgwIfGtpV2ICsNPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 95),
    _JnxMbgSgwIfGtpV2ICsNPTSIAdbrRx_Type()
)
jnxMbgSgwIfGtpV2ICsNPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNPTSIAdbrRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNPTSIAdbrTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNPTSIAdbrTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNPTSIAdbrTx = _JnxMbgSgwIfGtpV2ICsNPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 96),
    _JnxMbgSgwIfGtpV2ICsNPTSIAdbrTx_Type()
)
jnxMbgSgwIfGtpV2ICsNPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNPTSIAdbrTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCtxNotFndRx = _JnxMbgSgwIfGtpV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 97),
    _JnxMbgSgwIfGtpV2ICsCtxNotFndRx_Type()
)
jnxMbgSgwIfGtpV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCtxNotFndTx = _JnxMbgSgwIfGtpV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 98),
    _JnxMbgSgwIfGtpV2ICsCtxNotFndTx_Type()
)
jnxMbgSgwIfGtpV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvMsgFmtRx = _JnxMbgSgwIfGtpV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 99),
    _JnxMbgSgwIfGtpV2ICsInvMsgFmtRx_Type()
)
jnxMbgSgwIfGtpV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvMsgFmtTx = _JnxMbgSgwIfGtpV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 100),
    _JnxMbgSgwIfGtpV2ICsInvMsgFmtTx_Type()
)
jnxMbgSgwIfGtpV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsVerNotSuppRx = _JnxMbgSgwIfGtpV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 101),
    _JnxMbgSgwIfGtpV2ICsVerNotSuppRx_Type()
)
jnxMbgSgwIfGtpV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsVerNotSuppTx = _JnxMbgSgwIfGtpV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 102),
    _JnxMbgSgwIfGtpV2ICsVerNotSuppTx_Type()
)
jnxMbgSgwIfGtpV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvLenRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvLenRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvLenRx = _JnxMbgSgwIfGtpV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 103),
    _JnxMbgSgwIfGtpV2ICsInvLenRx_Type()
)
jnxMbgSgwIfGtpV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvLenRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvLenTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvLenTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvLenTx = _JnxMbgSgwIfGtpV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 104),
    _JnxMbgSgwIfGtpV2ICsInvLenTx_Type()
)
jnxMbgSgwIfGtpV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvLenTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSrvNotSuppRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSrvNotSuppRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSrvNotSuppRx = _JnxMbgSgwIfGtpV2ICsSrvNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 105),
    _JnxMbgSgwIfGtpV2ICsSrvNotSuppRx_Type()
)
jnxMbgSgwIfGtpV2ICsSrvNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSrvNotSuppRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSrvNotSuppTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSrvNotSuppTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSrvNotSuppTx = _JnxMbgSgwIfGtpV2ICsSrvNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 106),
    _JnxMbgSgwIfGtpV2ICsSrvNotSuppTx_Type()
)
jnxMbgSgwIfGtpV2ICsSrvNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSrvNotSuppTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsManIEIncorRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsManIEIncorRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsManIEIncorRx = _JnxMbgSgwIfGtpV2ICsManIEIncorRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 107),
    _JnxMbgSgwIfGtpV2ICsManIEIncorRx_Type()
)
jnxMbgSgwIfGtpV2ICsManIEIncorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsManIEIncorRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsManIEIncorTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsManIEIncorTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsManIEIncorTx = _JnxMbgSgwIfGtpV2ICsManIEIncorTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 108),
    _JnxMbgSgwIfGtpV2ICsManIEIncorTx_Type()
)
jnxMbgSgwIfGtpV2ICsManIEIncorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsManIEIncorTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsManIEMissRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsManIEMissRx = _JnxMbgSgwIfGtpV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 109),
    _JnxMbgSgwIfGtpV2ICsManIEMissRx_Type()
)
jnxMbgSgwIfGtpV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsManIEMissRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsManIEMissTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsManIEMissTx = _JnxMbgSgwIfGtpV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 110),
    _JnxMbgSgwIfGtpV2ICsManIEMissTx_Type()
)
jnxMbgSgwIfGtpV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsManIEMissTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsOptIEIncorRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsOptIEIncorRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsOptIEIncorRx = _JnxMbgSgwIfGtpV2ICsOptIEIncorRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 111),
    _JnxMbgSgwIfGtpV2ICsOptIEIncorRx_Type()
)
jnxMbgSgwIfGtpV2ICsOptIEIncorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsOptIEIncorRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsOptIEIncorTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsOptIEIncorTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsOptIEIncorTx = _JnxMbgSgwIfGtpV2ICsOptIEIncorTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 112),
    _JnxMbgSgwIfGtpV2ICsOptIEIncorTx_Type()
)
jnxMbgSgwIfGtpV2ICsOptIEIncorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsOptIEIncorTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSysFailRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSysFailRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSysFailRx = _JnxMbgSgwIfGtpV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 113),
    _JnxMbgSgwIfGtpV2ICsSysFailRx_Type()
)
jnxMbgSgwIfGtpV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSysFailRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSysFailTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSysFailTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSysFailTx = _JnxMbgSgwIfGtpV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 114),
    _JnxMbgSgwIfGtpV2ICsSysFailTx_Type()
)
jnxMbgSgwIfGtpV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSysFailTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNoResRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNoResRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNoResRx = _JnxMbgSgwIfGtpV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 115),
    _JnxMbgSgwIfGtpV2ICsNoResRx_Type()
)
jnxMbgSgwIfGtpV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNoResRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNoResTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNoResTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNoResTx = _JnxMbgSgwIfGtpV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 116),
    _JnxMbgSgwIfGtpV2ICsNoResTx_Type()
)
jnxMbgSgwIfGtpV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNoResTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsTFTSMANTErRx = _JnxMbgSgwIfGtpV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 117),
    _JnxMbgSgwIfGtpV2ICsTFTSMANTErRx_Type()
)
jnxMbgSgwIfGtpV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsTFTSMANTErTx = _JnxMbgSgwIfGtpV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 118),
    _JnxMbgSgwIfGtpV2ICsTFTSMANTErTx_Type()
)
jnxMbgSgwIfGtpV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsTFTSysErrRx = _JnxMbgSgwIfGtpV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 119),
    _JnxMbgSgwIfGtpV2ICsTFTSysErrRx_Type()
)
jnxMbgSgwIfGtpV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsTFTSysErrTx = _JnxMbgSgwIfGtpV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 120),
    _JnxMbgSgwIfGtpV2ICsTFTSysErrTx_Type()
)
jnxMbgSgwIfGtpV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPkFltManErRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPkFltManErRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPkFltManErRx = _JnxMbgSgwIfGtpV2ICsPkFltManErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 121),
    _JnxMbgSgwIfGtpV2ICsPkFltManErRx_Type()
)
jnxMbgSgwIfGtpV2ICsPkFltManErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPkFltManErRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPkFltManErTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPkFltManErTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPkFltManErTx = _JnxMbgSgwIfGtpV2ICsPkFltManErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 122),
    _JnxMbgSgwIfGtpV2ICsPkFltManErTx_Type()
)
jnxMbgSgwIfGtpV2ICsPkFltManErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPkFltManErTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPkFltSynErRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPkFltSynErRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPkFltSynErRx = _JnxMbgSgwIfGtpV2ICsPkFltSynErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 123),
    _JnxMbgSgwIfGtpV2ICsPkFltSynErRx_Type()
)
jnxMbgSgwIfGtpV2ICsPkFltSynErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPkFltSynErRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPkFltSynErTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPkFltSynErTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPkFltSynErTx = _JnxMbgSgwIfGtpV2ICsPkFltSynErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 124),
    _JnxMbgSgwIfGtpV2ICsPkFltSynErTx_Type()
)
jnxMbgSgwIfGtpV2ICsPkFltSynErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPkFltSynErTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsMisUnknAPNRx = _JnxMbgSgwIfGtpV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 125),
    _JnxMbgSgwIfGtpV2ICsMisUnknAPNRx_Type()
)
jnxMbgSgwIfGtpV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsMisUnknAPNTx = _JnxMbgSgwIfGtpV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 126),
    _JnxMbgSgwIfGtpV2ICsMisUnknAPNTx_Type()
)
jnxMbgSgwIfGtpV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnexpRptIERx = _JnxMbgSgwIfGtpV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 127),
    _JnxMbgSgwIfGtpV2ICsUnexpRptIERx_Type()
)
jnxMbgSgwIfGtpV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnexpRptIETx = _JnxMbgSgwIfGtpV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 128),
    _JnxMbgSgwIfGtpV2ICsUnexpRptIETx_Type()
)
jnxMbgSgwIfGtpV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsGREKeyNtFdRx = _JnxMbgSgwIfGtpV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 129),
    _JnxMbgSgwIfGtpV2ICsGREKeyNtFdRx_Type()
)
jnxMbgSgwIfGtpV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsGREKeyNtFdTx = _JnxMbgSgwIfGtpV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 130),
    _JnxMbgSgwIfGtpV2ICsGREKeyNtFdTx_Type()
)
jnxMbgSgwIfGtpV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRelocFailRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRelocFailRx = _JnxMbgSgwIfGtpV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 131),
    _JnxMbgSgwIfGtpV2ICsRelocFailRx_Type()
)
jnxMbgSgwIfGtpV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRelocFailRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRelocFailTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRelocFailTx = _JnxMbgSgwIfGtpV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 132),
    _JnxMbgSgwIfGtpV2ICsRelocFailTx_Type()
)
jnxMbgSgwIfGtpV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRelocFailTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsDenINRatRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsDenINRatRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsDenINRatRx = _JnxMbgSgwIfGtpV2ICsDenINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 133),
    _JnxMbgSgwIfGtpV2ICsDenINRatRx_Type()
)
jnxMbgSgwIfGtpV2ICsDenINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsDenINRatRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsDenINRatTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsDenINRatTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsDenINRatTx = _JnxMbgSgwIfGtpV2ICsDenINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 134),
    _JnxMbgSgwIfGtpV2ICsDenINRatTx_Type()
)
jnxMbgSgwIfGtpV2ICsDenINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsDenINRatTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPTNotSuppRx = _JnxMbgSgwIfGtpV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 135),
    _JnxMbgSgwIfGtpV2ICsPTNotSuppRx_Type()
)
jnxMbgSgwIfGtpV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPTNotSuppTx = _JnxMbgSgwIfGtpV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 136),
    _JnxMbgSgwIfGtpV2ICsPTNotSuppTx_Type()
)
jnxMbgSgwIfGtpV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAlDynAdOccRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAlDynAdOccRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAlDynAdOccRx = _JnxMbgSgwIfGtpV2ICsAlDynAdOccRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 137),
    _JnxMbgSgwIfGtpV2ICsAlDynAdOccRx_Type()
)
jnxMbgSgwIfGtpV2ICsAlDynAdOccRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAlDynAdOccRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAlDynAdOccTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAlDynAdOccTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAlDynAdOccTx = _JnxMbgSgwIfGtpV2ICsAlDynAdOccTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 138),
    _JnxMbgSgwIfGtpV2ICsAlDynAdOccTx_Type()
)
jnxMbgSgwIfGtpV2ICsAlDynAdOccTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAlDynAdOccTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNOTFTUECTXRx = _JnxMbgSgwIfGtpV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 139),
    _JnxMbgSgwIfGtpV2ICsNOTFTUECTXRx_Type()
)
jnxMbgSgwIfGtpV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNOTFTUECTXTx = _JnxMbgSgwIfGtpV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 140),
    _JnxMbgSgwIfGtpV2ICsNOTFTUECTXTx_Type()
)
jnxMbgSgwIfGtpV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsProtoNtSupRx = _JnxMbgSgwIfGtpV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 141),
    _JnxMbgSgwIfGtpV2ICsProtoNtSupRx_Type()
)
jnxMbgSgwIfGtpV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsProtoNtSupTx = _JnxMbgSgwIfGtpV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 142),
    _JnxMbgSgwIfGtpV2ICsProtoNtSupTx_Type()
)
jnxMbgSgwIfGtpV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUENotRespRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUENotRespRx = _JnxMbgSgwIfGtpV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 143),
    _JnxMbgSgwIfGtpV2ICsUENotRespRx_Type()
)
jnxMbgSgwIfGtpV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUENotRespRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUENotRespTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUENotRespTx = _JnxMbgSgwIfGtpV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 144),
    _JnxMbgSgwIfGtpV2ICsUENotRespTx_Type()
)
jnxMbgSgwIfGtpV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUENotRespTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUERefusesRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUERefusesRx = _JnxMbgSgwIfGtpV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 145),
    _JnxMbgSgwIfGtpV2ICsUERefusesRx_Type()
)
jnxMbgSgwIfGtpV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUERefusesRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUERefusesTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUERefusesTx = _JnxMbgSgwIfGtpV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 146),
    _JnxMbgSgwIfGtpV2ICsUERefusesTx_Type()
)
jnxMbgSgwIfGtpV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUERefusesTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsServDeniedRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsServDeniedRx = _JnxMbgSgwIfGtpV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 147),
    _JnxMbgSgwIfGtpV2ICsServDeniedRx_Type()
)
jnxMbgSgwIfGtpV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsServDeniedRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsServDeniedTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsServDeniedTx = _JnxMbgSgwIfGtpV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 148),
    _JnxMbgSgwIfGtpV2ICsServDeniedTx_Type()
)
jnxMbgSgwIfGtpV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsServDeniedTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnabPageUERx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnabPageUERx = _JnxMbgSgwIfGtpV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 149),
    _JnxMbgSgwIfGtpV2ICsUnabPageUERx_Type()
)
jnxMbgSgwIfGtpV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnabPageUERx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnabPageUETx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnabPageUETx = _JnxMbgSgwIfGtpV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 150),
    _JnxMbgSgwIfGtpV2ICsUnabPageUETx_Type()
)
jnxMbgSgwIfGtpV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnabPageUETx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNoMemRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNoMemRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNoMemRx = _JnxMbgSgwIfGtpV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 151),
    _JnxMbgSgwIfGtpV2ICsNoMemRx_Type()
)
jnxMbgSgwIfGtpV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNoMemRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsNoMemTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsNoMemTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsNoMemTx = _JnxMbgSgwIfGtpV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 152),
    _JnxMbgSgwIfGtpV2ICsNoMemTx_Type()
)
jnxMbgSgwIfGtpV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsNoMemTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUserAUTHFlRx = _JnxMbgSgwIfGtpV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 153),
    _JnxMbgSgwIfGtpV2ICsUserAUTHFlRx_Type()
)
jnxMbgSgwIfGtpV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUserAUTHFlTx = _JnxMbgSgwIfGtpV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 154),
    _JnxMbgSgwIfGtpV2ICsUserAUTHFlTx_Type()
)
jnxMbgSgwIfGtpV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAPNAcsDenRx = _JnxMbgSgwIfGtpV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 155),
    _JnxMbgSgwIfGtpV2ICsAPNAcsDenRx_Type()
)
jnxMbgSgwIfGtpV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAPNAcsDenTx = _JnxMbgSgwIfGtpV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 156),
    _JnxMbgSgwIfGtpV2ICsAPNAcsDenTx_Type()
)
jnxMbgSgwIfGtpV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsReqRejRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsReqRejRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsReqRejRx = _JnxMbgSgwIfGtpV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 157),
    _JnxMbgSgwIfGtpV2ICsReqRejRx_Type()
)
jnxMbgSgwIfGtpV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsReqRejRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsReqRejTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsReqRejTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsReqRejTx = _JnxMbgSgwIfGtpV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 158),
    _JnxMbgSgwIfGtpV2ICsReqRejTx_Type()
)
jnxMbgSgwIfGtpV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsReqRejTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPTMSISigMMRx = _JnxMbgSgwIfGtpV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 159),
    _JnxMbgSgwIfGtpV2ICsPTMSISigMMRx_Type()
)
jnxMbgSgwIfGtpV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsPTMSISigMMTx = _JnxMbgSgwIfGtpV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 160),
    _JnxMbgSgwIfGtpV2ICsPTMSISigMMTx_Type()
)
jnxMbgSgwIfGtpV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsIMSINotKnRx = _JnxMbgSgwIfGtpV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 161),
    _JnxMbgSgwIfGtpV2ICsIMSINotKnRx_Type()
)
jnxMbgSgwIfGtpV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsIMSINotKnTx = _JnxMbgSgwIfGtpV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 162),
    _JnxMbgSgwIfGtpV2ICsIMSINotKnTx_Type()
)
jnxMbgSgwIfGtpV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCondIEMsRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCondIEMsRx = _JnxMbgSgwIfGtpV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 163),
    _JnxMbgSgwIfGtpV2ICsCondIEMsRx_Type()
)
jnxMbgSgwIfGtpV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCondIEMsRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCondIEMsTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCondIEMsTx = _JnxMbgSgwIfGtpV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 164),
    _JnxMbgSgwIfGtpV2ICsCondIEMsTx_Type()
)
jnxMbgSgwIfGtpV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCondIEMsTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAPNResTIncRx = _JnxMbgSgwIfGtpV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 165),
    _JnxMbgSgwIfGtpV2ICsAPNResTIncRx_Type()
)
jnxMbgSgwIfGtpV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsAPNResTIncTx = _JnxMbgSgwIfGtpV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 166),
    _JnxMbgSgwIfGtpV2ICsAPNResTIncTx_Type()
)
jnxMbgSgwIfGtpV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnknownRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnknownRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnknownRx = _JnxMbgSgwIfGtpV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 167),
    _JnxMbgSgwIfGtpV2ICsUnknownRx_Type()
)
jnxMbgSgwIfGtpV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnknownRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnknownTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnknownTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnknownTx = _JnxMbgSgwIfGtpV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 168),
    _JnxMbgSgwIfGtpV2ICsUnknownTx_Type()
)
jnxMbgSgwIfGtpV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnknownTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsLclDetRx = _JnxMbgSgwIfGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 169),
    _JnxMbgSgwIfGtpV2ICsLclDetRx_Type()
)
jnxMbgSgwIfGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsLclDetTx = _JnxMbgSgwIfGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 170),
    _JnxMbgSgwIfGtpV2ICsLclDetTx_Type()
)
jnxMbgSgwIfGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCmpDetRx = _JnxMbgSgwIfGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 171),
    _JnxMbgSgwIfGtpV2ICsCmpDetRx_Type()
)
jnxMbgSgwIfGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsCmpDetTx = _JnxMbgSgwIfGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 172),
    _JnxMbgSgwIfGtpV2ICsCmpDetTx_Type()
)
jnxMbgSgwIfGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRATChgRx = _JnxMbgSgwIfGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 173),
    _JnxMbgSgwIfGtpV2ICsRATChgRx_Type()
)
jnxMbgSgwIfGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRATChgTx = _JnxMbgSgwIfGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 174),
    _JnxMbgSgwIfGtpV2ICsRATChgTx_Type()
)
jnxMbgSgwIfGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsISRDeactRx = _JnxMbgSgwIfGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 175),
    _JnxMbgSgwIfGtpV2ICsISRDeactRx_Type()
)
jnxMbgSgwIfGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsISRDeactTx = _JnxMbgSgwIfGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 176),
    _JnxMbgSgwIfGtpV2ICsISRDeactTx_Type()
)
jnxMbgSgwIfGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsEIFRNCEnRx = _JnxMbgSgwIfGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 177),
    _JnxMbgSgwIfGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgSgwIfGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsEIFRNCEnTx = _JnxMbgSgwIfGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 178),
    _JnxMbgSgwIfGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgSgwIfGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSemErTADRx = _JnxMbgSgwIfGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 179),
    _JnxMbgSgwIfGtpV2ICsSemErTADRx_Type()
)
jnxMbgSgwIfGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSemErTADTx = _JnxMbgSgwIfGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 180),
    _JnxMbgSgwIfGtpV2ICsSemErTADTx_Type()
)
jnxMbgSgwIfGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSynErTADRx = _JnxMbgSgwIfGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 181),
    _JnxMbgSgwIfGtpV2ICsSynErTADRx_Type()
)
jnxMbgSgwIfGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsSynErTADTx = _JnxMbgSgwIfGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 182),
    _JnxMbgSgwIfGtpV2ICsSynErTADTx_Type()
)
jnxMbgSgwIfGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRMValRcvRx = _JnxMbgSgwIfGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 183),
    _JnxMbgSgwIfGtpV2ICsRMValRcvRx_Type()
)
jnxMbgSgwIfGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRMValRcvTx = _JnxMbgSgwIfGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 184),
    _JnxMbgSgwIfGtpV2ICsRMValRcvTx_Type()
)
jnxMbgSgwIfGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRPrNtRspRx = _JnxMbgSgwIfGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 185),
    _JnxMbgSgwIfGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgSgwIfGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsRPrNtRspTx = _JnxMbgSgwIfGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 186),
    _JnxMbgSgwIfGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgSgwIfGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsColNWReqRx = _JnxMbgSgwIfGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 187),
    _JnxMbgSgwIfGtpV2ICsColNWReqRx_Type()
)
jnxMbgSgwIfGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsColNWReqTx = _JnxMbgSgwIfGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 188),
    _JnxMbgSgwIfGtpV2ICsColNWReqTx_Type()
)
jnxMbgSgwIfGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnPgUESusRx = _JnxMbgSgwIfGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 189),
    _JnxMbgSgwIfGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgSgwIfGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsUnPgUESusTx = _JnxMbgSgwIfGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 190),
    _JnxMbgSgwIfGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgSgwIfGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvTotLenRx = _JnxMbgSgwIfGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 191),
    _JnxMbgSgwIfGtpV2ICsInvTotLenRx_Type()
)
jnxMbgSgwIfGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvTotLenTx = _JnxMbgSgwIfGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 192),
    _JnxMbgSgwIfGtpV2ICsInvTotLenTx_Type()
)
jnxMbgSgwIfGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsDtForNtSupRx = _JnxMbgSgwIfGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 193),
    _JnxMbgSgwIfGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgSgwIfGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsDtForNtSupTx = _JnxMbgSgwIfGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 194),
    _JnxMbgSgwIfGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgSgwIfGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInReFRePrRx = _JnxMbgSgwIfGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 195),
    _JnxMbgSgwIfGtpV2ICsInReFRePrRx_Type()
)
jnxMbgSgwIfGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInReFRePrTx = _JnxMbgSgwIfGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 196),
    _JnxMbgSgwIfGtpV2ICsInReFRePrTx_Type()
)
jnxMbgSgwIfGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvPrRx = _JnxMbgSgwIfGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 197),
    _JnxMbgSgwIfGtpV2ICsInvPrRx_Type()
)
jnxMbgSgwIfGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgSgwIfGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgSgwIfGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgSgwIfGtpV2ICsInvPrTx = _JnxMbgSgwIfGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 198),
    _JnxMbgSgwIfGtpV2ICsInvPrTx_Type()
)
jnxMbgSgwIfGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgSgwIfGtpV1ProtocolErrRx_Type = Counter64
_JnxMbgSgwIfGtpV1ProtocolErrRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1ProtocolErrRx = _JnxMbgSgwIfGtpV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 199),
    _JnxMbgSgwIfGtpV1ProtocolErrRx_Type()
)
jnxMbgSgwIfGtpV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1ProtocolErrRx.setStatus("current")
_JnxMbgSgwIfGtpV1UnSupMsgRx_Type = Counter64
_JnxMbgSgwIfGtpV1UnSupMsgRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1UnSupMsgRx = _JnxMbgSgwIfGtpV1UnSupMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 200),
    _JnxMbgSgwIfGtpV1UnSupMsgRx_Type()
)
jnxMbgSgwIfGtpV1UnSupMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1UnSupMsgRx.setStatus("current")
_JnxMbgSgwIfGtpV1T3RespTmrExpRx_Type = Counter64
_JnxMbgSgwIfGtpV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1T3RespTmrExpRx = _JnxMbgSgwIfGtpV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 201),
    _JnxMbgSgwIfGtpV1T3RespTmrExpRx_Type()
)
jnxMbgSgwIfGtpV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1T3RespTmrExpRx.setStatus("current")
_JnxMbgSgwIfGtpV1EndMarkerRx_Type = Counter64
_JnxMbgSgwIfGtpV1EndMarkerRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EndMarkerRx = _JnxMbgSgwIfGtpV1EndMarkerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 202),
    _JnxMbgSgwIfGtpV1EndMarkerRx_Type()
)
jnxMbgSgwIfGtpV1EndMarkerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EndMarkerRx.setStatus("current")
_JnxMbgSgwIfGtpV1EndMarkerTx_Type = Counter64
_JnxMbgSgwIfGtpV1EndMarkerTx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EndMarkerTx = _JnxMbgSgwIfGtpV1EndMarkerTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 203),
    _JnxMbgSgwIfGtpV1EndMarkerTx_Type()
)
jnxMbgSgwIfGtpV1EndMarkerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EndMarkerTx.setStatus("current")
_JnxMbgSgwIfGtpV1EchoReqRx_Type = Counter64
_JnxMbgSgwIfGtpV1EchoReqRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EchoReqRx = _JnxMbgSgwIfGtpV1EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 204),
    _JnxMbgSgwIfGtpV1EchoReqRx_Type()
)
jnxMbgSgwIfGtpV1EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EchoReqRx.setStatus("current")
_JnxMbgSgwIfGtpV1EchoReqTx_Type = Counter64
_JnxMbgSgwIfGtpV1EchoReqTx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EchoReqTx = _JnxMbgSgwIfGtpV1EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 205),
    _JnxMbgSgwIfGtpV1EchoReqTx_Type()
)
jnxMbgSgwIfGtpV1EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EchoReqTx.setStatus("current")
_JnxMbgSgwIfGtpV1EchoRespRx_Type = Counter64
_JnxMbgSgwIfGtpV1EchoRespRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EchoRespRx = _JnxMbgSgwIfGtpV1EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 206),
    _JnxMbgSgwIfGtpV1EchoRespRx_Type()
)
jnxMbgSgwIfGtpV1EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EchoRespRx.setStatus("current")
_JnxMbgSgwIfGtpV1EchoRespTx_Type = Counter64
_JnxMbgSgwIfGtpV1EchoRespTx_Object = MibTableColumn
jnxMbgSgwIfGtpV1EchoRespTx = _JnxMbgSgwIfGtpV1EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 207),
    _JnxMbgSgwIfGtpV1EchoRespTx_Type()
)
jnxMbgSgwIfGtpV1EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1EchoRespTx.setStatus("current")
_JnxMbgSgwIfGtpV1ErrIndRx_Type = Counter64
_JnxMbgSgwIfGtpV1ErrIndRx_Object = MibTableColumn
jnxMbgSgwIfGtpV1ErrIndRx = _JnxMbgSgwIfGtpV1ErrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 208),
    _JnxMbgSgwIfGtpV1ErrIndRx_Type()
)
jnxMbgSgwIfGtpV1ErrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1ErrIndRx.setStatus("current")
_JnxMbgSgwIfGtpV1ErrIndTx_Type = Counter64
_JnxMbgSgwIfGtpV1ErrIndTx_Object = MibTableColumn
jnxMbgSgwIfGtpV1ErrIndTx = _JnxMbgSgwIfGtpV1ErrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 209),
    _JnxMbgSgwIfGtpV1ErrIndTx_Type()
)
jnxMbgSgwIfGtpV1ErrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfGtpV1ErrIndTx.setStatus("current")
_JnxMbgSgwIfSuspNotifRx_Type = Counter64
_JnxMbgSgwIfSuspNotifRx_Object = MibTableColumn
jnxMbgSgwIfSuspNotifRx = _JnxMbgSgwIfSuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 210),
    _JnxMbgSgwIfSuspNotifRx_Type()
)
jnxMbgSgwIfSuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfSuspNotifRx.setStatus("current")
_JnxMbgSgwIfSuspNotifTx_Type = Counter64
_JnxMbgSgwIfSuspNotifTx_Object = MibTableColumn
jnxMbgSgwIfSuspNotifTx = _JnxMbgSgwIfSuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 211),
    _JnxMbgSgwIfSuspNotifTx_Type()
)
jnxMbgSgwIfSuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfSuspNotifTx.setStatus("current")
_JnxMbgSgwIfSuspAckRx_Type = Counter64
_JnxMbgSgwIfSuspAckRx_Object = MibTableColumn
jnxMbgSgwIfSuspAckRx = _JnxMbgSgwIfSuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 212),
    _JnxMbgSgwIfSuspAckRx_Type()
)
jnxMbgSgwIfSuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfSuspAckRx.setStatus("current")
_JnxMbgSgwIfSuspAckTx_Type = Counter64
_JnxMbgSgwIfSuspAckTx_Object = MibTableColumn
jnxMbgSgwIfSuspAckTx = _JnxMbgSgwIfSuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 213),
    _JnxMbgSgwIfSuspAckTx_Type()
)
jnxMbgSgwIfSuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfSuspAckTx.setStatus("current")
_JnxMbgSgwIfResumeNotifRx_Type = Counter64
_JnxMbgSgwIfResumeNotifRx_Object = MibTableColumn
jnxMbgSgwIfResumeNotifRx = _JnxMbgSgwIfResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 214),
    _JnxMbgSgwIfResumeNotifRx_Type()
)
jnxMbgSgwIfResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfResumeNotifRx.setStatus("current")
_JnxMbgSgwIfResumeNotifTx_Type = Counter64
_JnxMbgSgwIfResumeNotifTx_Object = MibTableColumn
jnxMbgSgwIfResumeNotifTx = _JnxMbgSgwIfResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 215),
    _JnxMbgSgwIfResumeNotifTx_Type()
)
jnxMbgSgwIfResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfResumeNotifTx.setStatus("current")
_JnxMbgSgwIfResumeAckRx_Type = Counter64
_JnxMbgSgwIfResumeAckRx_Object = MibTableColumn
jnxMbgSgwIfResumeAckRx = _JnxMbgSgwIfResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 216),
    _JnxMbgSgwIfResumeAckRx_Type()
)
jnxMbgSgwIfResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfResumeAckRx.setStatus("current")
_JnxMbgSgwIfResumeAckTx_Type = Counter64
_JnxMbgSgwIfResumeAckTx_Object = MibTableColumn
jnxMbgSgwIfResumeAckTx = _JnxMbgSgwIfResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 217),
    _JnxMbgSgwIfResumeAckTx_Type()
)
jnxMbgSgwIfResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfResumeAckTx.setStatus("current")
_JnxMbgSgwIfPiggybackMsgRx_Type = Counter64
_JnxMbgSgwIfPiggybackMsgRx_Object = MibTableColumn
jnxMbgSgwIfPiggybackMsgRx = _JnxMbgSgwIfPiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 218),
    _JnxMbgSgwIfPiggybackMsgRx_Type()
)
jnxMbgSgwIfPiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfPiggybackMsgRx.setStatus("current")
_JnxMbgSgwIfPiggybackMsgTx_Type = Counter64
_JnxMbgSgwIfPiggybackMsgTx_Object = MibTableColumn
jnxMbgSgwIfPiggybackMsgTx = _JnxMbgSgwIfPiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 1, 4, 1, 219),
    _JnxMbgSgwIfPiggybackMsgTx_Type()
)
jnxMbgSgwIfPiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIfPiggybackMsgTx.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgSgwGtpPeerGwUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 0, 1)
)
jnxMbgSgwGtpPeerGwUpNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpPeerName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPeerGwUpNotif.setStatus(
        "current"
    )

jnxMbgSgwGtpPeerGwDnNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 0, 2)
)
jnxMbgSgwGtpPeerGwDnNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpPeerName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPeerGwDnNotif.setStatus(
        "current"
    )

jnxMbgSgwGtpPrDnTPerPrAlrmActv = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 0, 3)
)
jnxMbgSgwGtpPrDnTPerPrAlrmActv.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpPeerName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpAlarmStatCounter"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPrDnTPerPrAlrmActv.setStatus(
        "current"
    )

jnxMbgSgwGtpPrDnTPerPrAlrmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 2, 0, 4)
)
jnxMbgSgwGtpPrDnTPerPrAlrmClr.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpPeerName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB", "jnxMbgSgwGtpAlarmStatCounter"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwGtpPrDnTPerPrAlrmClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-SGW-GTP-MIB",
    **{"jnxMbgSgwGtpMib": jnxMbgSgwGtpMib,
       "jnxMbgSgwGtpNotifications": jnxMbgSgwGtpNotifications,
       "jnxMbgSgwGtpPeerGwUpNotif": jnxMbgSgwGtpPeerGwUpNotif,
       "jnxMbgSgwGtpPeerGwDnNotif": jnxMbgSgwGtpPeerGwDnNotif,
       "jnxMbgSgwGtpPrDnTPerPrAlrmActv": jnxMbgSgwGtpPrDnTPerPrAlrmActv,
       "jnxMbgSgwGtpPrDnTPerPrAlrmClr": jnxMbgSgwGtpPrDnTPerPrAlrmClr,
       "jnxMbgSgwGtpObjects": jnxMbgSgwGtpObjects,
       "jnxMbgSgwGtpCPerPeerStatsTable": jnxMbgSgwGtpCPerPeerStatsTable,
       "jnxMbgSgwGtpPerPeerStatsEntry": jnxMbgSgwGtpPerPeerStatsEntry,
       "jnxMbgSgwPPGtpRmtAddr": jnxMbgSgwPPGtpRmtAddr,
       "jnxMbgSgwPPGtpLclAddr": jnxMbgSgwPPGtpLclAddr,
       "jnxMbgSgwPPGtpRtgInst": jnxMbgSgwPPGtpRtgInst,
       "jnxMbgSgwPPRxPacketsDropped": jnxMbgSgwPPRxPacketsDropped,
       "jnxMbgSgwPPPacketAllocFail": jnxMbgSgwPPPacketAllocFail,
       "jnxMbgSgwPPPacketSendFail": jnxMbgSgwPPPacketSendFail,
       "jnxMbgSgwPPIPVerErrRx": jnxMbgSgwPPIPVerErrRx,
       "jnxMbgSgwPPIPProtoErrRx": jnxMbgSgwPPIPProtoErrRx,
       "jnxMbgSgwPPGTPPortErrRx": jnxMbgSgwPPGTPPortErrRx,
       "jnxMbgSgwPPGTPUnknVerRx": jnxMbgSgwPPGTPUnknVerRx,
       "jnxMbgSgwPPPcktLenErrRx": jnxMbgSgwPPPcktLenErrRx,
       "jnxMbgSgwPPUnknMsgRx": jnxMbgSgwPPUnknMsgRx,
       "jnxMbgSgwPPProtocolErrRx": jnxMbgSgwPPProtocolErrRx,
       "jnxMbgSgwPPUnSupportedMsgRx": jnxMbgSgwPPUnSupportedMsgRx,
       "jnxMbgSgwPPT3RespTmrExpRx": jnxMbgSgwPPT3RespTmrExpRx,
       "jnxMbgSgwPPV2NumMsgRx": jnxMbgSgwPPV2NumMsgRx,
       "jnxMbgSgwPPV2NumMsgTx": jnxMbgSgwPPV2NumMsgTx,
       "jnxMbgSgwPPV2NumBytesRx": jnxMbgSgwPPV2NumBytesRx,
       "jnxMbgSgwPPV2NumBytesTx": jnxMbgSgwPPV2NumBytesTx,
       "jnxMbgSgwPPV2EchoReqRx": jnxMbgSgwPPV2EchoReqRx,
       "jnxMbgSgwPPV2EchoReqTx": jnxMbgSgwPPV2EchoReqTx,
       "jnxMbgSgwPPV2EchoRespRx": jnxMbgSgwPPV2EchoRespRx,
       "jnxMbgSgwPPV2EchoRespTx": jnxMbgSgwPPV2EchoRespTx,
       "jnxMbgSgwPPV2VerNotSupRx": jnxMbgSgwPPV2VerNotSupRx,
       "jnxMbgSgwPPV2VerNotSupTx": jnxMbgSgwPPV2VerNotSupTx,
       "jnxMbgSgwPPCreateSessReqRx": jnxMbgSgwPPCreateSessReqRx,
       "jnxMbgSgwPPCreateSessReqTx": jnxMbgSgwPPCreateSessReqTx,
       "jnxMbgSgwPPCreateSessRspRx": jnxMbgSgwPPCreateSessRspRx,
       "jnxMbgSgwPPCreateSessRspTx": jnxMbgSgwPPCreateSessRspTx,
       "jnxMbgSgwPPModBrReqRx": jnxMbgSgwPPModBrReqRx,
       "jnxMbgSgwPPModBrReqTx": jnxMbgSgwPPModBrReqTx,
       "jnxMbgSgwPPModBrRspRx": jnxMbgSgwPPModBrRspRx,
       "jnxMbgSgwPPModBrRspTx": jnxMbgSgwPPModBrRspTx,
       "jnxMbgSgwPPDelSessReqRx": jnxMbgSgwPPDelSessReqRx,
       "jnxMbgSgwPPDelSessReqTx": jnxMbgSgwPPDelSessReqTx,
       "jnxMbgSgwPPDelSessRspRx": jnxMbgSgwPPDelSessRspRx,
       "jnxMbgSgwPPDelSessRspTx": jnxMbgSgwPPDelSessRspTx,
       "jnxMbgSgwPPCrtBrReqRx": jnxMbgSgwPPCrtBrReqRx,
       "jnxMbgSgwPPCrtBrReqTx": jnxMbgSgwPPCrtBrReqTx,
       "jnxMbgSgwPPCrtBrRspRx": jnxMbgSgwPPCrtBrRspRx,
       "jnxMbgSgwPPCrtBrRspTx": jnxMbgSgwPPCrtBrRspTx,
       "jnxMbgSgwPPUpdBrReqRx": jnxMbgSgwPPUpdBrReqRx,
       "jnxMbgSgwPPUpdBrReqTx": jnxMbgSgwPPUpdBrReqTx,
       "jnxMbgSgwPPUpdBrRspRx": jnxMbgSgwPPUpdBrRspRx,
       "jnxMbgSgwPPUpdBrRspTx": jnxMbgSgwPPUpdBrRspTx,
       "jnxMbgSgwPPDelBrReqRx": jnxMbgSgwPPDelBrReqRx,
       "jnxMbgSgwPPDelBrReqTx": jnxMbgSgwPPDelBrReqTx,
       "jnxMbgSgwPPDelBrRspRx": jnxMbgSgwPPDelBrRspRx,
       "jnxMbgSgwPPDelBrRspTx": jnxMbgSgwPPDelBrRspTx,
       "jnxMbgSgwPPDelConnSetReqRx": jnxMbgSgwPPDelConnSetReqRx,
       "jnxMbgSgwPPDelConnSetReqTx": jnxMbgSgwPPDelConnSetReqTx,
       "jnxMbgSgwPPDelConnSetRspRx": jnxMbgSgwPPDelConnSetRspRx,
       "jnxMbgSgwPPDelConnSetRspTx": jnxMbgSgwPPDelConnSetRspTx,
       "jnxMbgSgwPPUpdConnSetReqRx": jnxMbgSgwPPUpdConnSetReqRx,
       "jnxMbgSgwPPUpdConnSetReqTx": jnxMbgSgwPPUpdConnSetReqTx,
       "jnxMbgSgwPPUpdConnSetRspRx": jnxMbgSgwPPUpdConnSetRspRx,
       "jnxMbgSgwPPUpdConnSetRspTx": jnxMbgSgwPPUpdConnSetRspTx,
       "jnxMbgSgwPPModBrCmdRx": jnxMbgSgwPPModBrCmdRx,
       "jnxMbgSgwPPModBrCmdTx": jnxMbgSgwPPModBrCmdTx,
       "jnxMbgSgwPPModBrFlrIndRx": jnxMbgSgwPPModBrFlrIndRx,
       "jnxMbgSgwPPModBrFlrIndTx": jnxMbgSgwPPModBrFlrIndTx,
       "jnxMbgSgwPPDelBrCmdRx": jnxMbgSgwPPDelBrCmdRx,
       "jnxMbgSgwPPDelBrCmdTx": jnxMbgSgwPPDelBrCmdTx,
       "jnxMbgSgwPPDelBrFlrIndRx": jnxMbgSgwPPDelBrFlrIndRx,
       "jnxMbgSgwPPDelBrFlrIndTx": jnxMbgSgwPPDelBrFlrIndTx,
       "jnxMbgSgwPPBrResCmdRx": jnxMbgSgwPPBrResCmdRx,
       "jnxMbgSgwPPBrResCmdTx": jnxMbgSgwPPBrResCmdTx,
       "jnxMbgSgwPPBrResFlrIndRx": jnxMbgSgwPPBrResFlrIndRx,
       "jnxMbgSgwPPBrResFlrIndTx": jnxMbgSgwPPBrResFlrIndTx,
       "jnxMbgSgwPPRelAcsBrReqRx": jnxMbgSgwPPRelAcsBrReqRx,
       "jnxMbgSgwPPRelAcsBrReqTx": jnxMbgSgwPPRelAcsBrReqTx,
       "jnxMbgSgwPPRelAcsBrRespRx": jnxMbgSgwPPRelAcsBrRespRx,
       "jnxMbgSgwPPRelAcsBrRespTx": jnxMbgSgwPPRelAcsBrRespTx,
       "jnxMbgSgwPPCrIndTunReqRx": jnxMbgSgwPPCrIndTunReqRx,
       "jnxMbgSgwPPCrIndTunReqTx": jnxMbgSgwPPCrIndTunReqTx,
       "jnxMbgSgwPPCrIndTunRespRx": jnxMbgSgwPPCrIndTunRespRx,
       "jnxMbgSgwPPCrIndTunRespTx": jnxMbgSgwPPCrIndTunRespTx,
       "jnxMbgSgwPPDelIndTunReqRx": jnxMbgSgwPPDelIndTunReqRx,
       "jnxMbgSgwPPDelIndTunReqTx": jnxMbgSgwPPDelIndTunReqTx,
       "jnxMbgSgwPPDelIndTunRespRx": jnxMbgSgwPPDelIndTunRespRx,
       "jnxMbgSgwPPDelIndTunRespTx": jnxMbgSgwPPDelIndTunRespTx,
       "jnxMbgSgwPPDlDataNotifRx": jnxMbgSgwPPDlDataNotifRx,
       "jnxMbgSgwPPDlDataNotifTx": jnxMbgSgwPPDlDataNotifTx,
       "jnxMbgSgwPPDlDataAckRx": jnxMbgSgwPPDlDataAckRx,
       "jnxMbgSgwPPDlDataAckTx": jnxMbgSgwPPDlDataAckTx,
       "jnxMbgSgwPPDlDataNotiFlrIndRx": jnxMbgSgwPPDlDataNotiFlrIndRx,
       "jnxMbgSgwPPDlDataNotiFlrIndTx": jnxMbgSgwPPDlDataNotiFlrIndTx,
       "jnxMbgSgwPPStopPagingIndRx": jnxMbgSgwPPStopPagingIndRx,
       "jnxMbgSgwPPStopPagingIndTx": jnxMbgSgwPPStopPagingIndTx,
       "jnxMbgSgwPPGtpV2ICsPageRx": jnxMbgSgwPPGtpV2ICsPageRx,
       "jnxMbgSgwPPGtpV2ICsPageTx": jnxMbgSgwPPGtpV2ICsPageTx,
       "jnxMbgSgwPPGtpV2ICsReqAcceptRx": jnxMbgSgwPPGtpV2ICsReqAcceptRx,
       "jnxMbgSgwPPGtpV2ICsReqAcceptTx": jnxMbgSgwPPGtpV2ICsReqAcceptTx,
       "jnxMbgSgwPPGtpV2ICsAcceptPartRx": jnxMbgSgwPPGtpV2ICsAcceptPartRx,
       "jnxMbgSgwPPGtpV2ICsAcceptPartTx": jnxMbgSgwPPGtpV2ICsAcceptPartTx,
       "jnxMbgSgwPPGtpV2ICsNewPTNPrefRx": jnxMbgSgwPPGtpV2ICsNewPTNPrefRx,
       "jnxMbgSgwPPGtpV2ICsNewPTNPrefTx": jnxMbgSgwPPGtpV2ICsNewPTNPrefTx,
       "jnxMbgSgwPPGtpV2ICsNPTSIAdbrRx": jnxMbgSgwPPGtpV2ICsNPTSIAdbrRx,
       "jnxMbgSgwPPGtpV2ICsNPTSIAdbrTx": jnxMbgSgwPPGtpV2ICsNPTSIAdbrTx,
       "jnxMbgSgwPPGtpV2ICsCtxNotFndRx": jnxMbgSgwPPGtpV2ICsCtxNotFndRx,
       "jnxMbgSgwPPGtpV2ICsCtxNotFndTx": jnxMbgSgwPPGtpV2ICsCtxNotFndTx,
       "jnxMbgSgwPPGtpV2ICsInvMsgFmtRx": jnxMbgSgwPPGtpV2ICsInvMsgFmtRx,
       "jnxMbgSgwPPGtpV2ICsInvMsgFmtTx": jnxMbgSgwPPGtpV2ICsInvMsgFmtTx,
       "jnxMbgSgwPPGtpV2ICsVerNotSuppRx": jnxMbgSgwPPGtpV2ICsVerNotSuppRx,
       "jnxMbgSgwPPGtpV2ICsVerNotSuppTx": jnxMbgSgwPPGtpV2ICsVerNotSuppTx,
       "jnxMbgSgwPPGtpV2ICsInvLenRx": jnxMbgSgwPPGtpV2ICsInvLenRx,
       "jnxMbgSgwPPGtpV2ICsInvLenTx": jnxMbgSgwPPGtpV2ICsInvLenTx,
       "jnxMbgSgwPPGtpV2ICsServNotSupRx": jnxMbgSgwPPGtpV2ICsServNotSupRx,
       "jnxMbgSgwPPGtpV2ICsServNotSupTx": jnxMbgSgwPPGtpV2ICsServNotSupTx,
       "jnxMbgSgwPPGtpV2ICsManIEIncorRx": jnxMbgSgwPPGtpV2ICsManIEIncorRx,
       "jnxMbgSgwPPGtpV2ICsManIEIncorTx": jnxMbgSgwPPGtpV2ICsManIEIncorTx,
       "jnxMbgSgwPPGtpV2ICsManIEMissRx": jnxMbgSgwPPGtpV2ICsManIEMissRx,
       "jnxMbgSgwPPGtpV2ICsManIEMissTx": jnxMbgSgwPPGtpV2ICsManIEMissTx,
       "jnxMbgSgwPPGtpV2ICsOptIEIncorRx": jnxMbgSgwPPGtpV2ICsOptIEIncorRx,
       "jnxMbgSgwPPGtpV2ICsOptIEIncorTx": jnxMbgSgwPPGtpV2ICsOptIEIncorTx,
       "jnxMbgSgwPPGtpV2ICsSysFailRx": jnxMbgSgwPPGtpV2ICsSysFailRx,
       "jnxMbgSgwPPGtpV2ICsSysFailTx": jnxMbgSgwPPGtpV2ICsSysFailTx,
       "jnxMbgSgwPPGtpV2ICsNoResRx": jnxMbgSgwPPGtpV2ICsNoResRx,
       "jnxMbgSgwPPGtpV2ICsNoResTx": jnxMbgSgwPPGtpV2ICsNoResTx,
       "jnxMbgSgwPPGtpV2ICsTFTSMANTErRx": jnxMbgSgwPPGtpV2ICsTFTSMANTErRx,
       "jnxMbgSgwPPGtpV2ICsTFTSMANTErTx": jnxMbgSgwPPGtpV2ICsTFTSMANTErTx,
       "jnxMbgSgwPPGtpV2ICsTFTSysErrRx": jnxMbgSgwPPGtpV2ICsTFTSysErrRx,
       "jnxMbgSgwPPGtpV2ICsTFTSysErrTx": jnxMbgSgwPPGtpV2ICsTFTSysErrTx,
       "jnxMbgSgwPPGtpV2ICsPkFltManErRx": jnxMbgSgwPPGtpV2ICsPkFltManErRx,
       "jnxMbgSgwPPGtpV2ICsPkFltManErTx": jnxMbgSgwPPGtpV2ICsPkFltManErTx,
       "jnxMbgSgwPPGtpV2ICsPkFltSynErRx": jnxMbgSgwPPGtpV2ICsPkFltSynErRx,
       "jnxMbgSgwPPGtpV2ICsPkFltSynErTx": jnxMbgSgwPPGtpV2ICsPkFltSynErTx,
       "jnxMbgSgwPPGtpV2ICsMisUnknAPNRx": jnxMbgSgwPPGtpV2ICsMisUnknAPNRx,
       "jnxMbgSgwPPGtpV2ICsMisUnknAPNTx": jnxMbgSgwPPGtpV2ICsMisUnknAPNTx,
       "jnxMbgSgwPPGtpV2ICsUnexpRptIERx": jnxMbgSgwPPGtpV2ICsUnexpRptIERx,
       "jnxMbgSgwPPGtpV2ICsUnexpRptIETx": jnxMbgSgwPPGtpV2ICsUnexpRptIETx,
       "jnxMbgSgwPPGtpV2ICsGREKeyNtFdRx": jnxMbgSgwPPGtpV2ICsGREKeyNtFdRx,
       "jnxMbgSgwPPGtpV2ICsGREKeyNtFdTx": jnxMbgSgwPPGtpV2ICsGREKeyNtFdTx,
       "jnxMbgSgwPPGtpV2ICsRelocFailRx": jnxMbgSgwPPGtpV2ICsRelocFailRx,
       "jnxMbgSgwPPGtpV2ICsRelocFailTx": jnxMbgSgwPPGtpV2ICsRelocFailTx,
       "jnxMbgSgwPPGtpV2ICsDenINRatRx": jnxMbgSgwPPGtpV2ICsDenINRatRx,
       "jnxMbgSgwPPGtpV2ICsDenINRatTx": jnxMbgSgwPPGtpV2ICsDenINRatTx,
       "jnxMbgSgwPPGtpV2ICsPTNotSuppRx": jnxMbgSgwPPGtpV2ICsPTNotSuppRx,
       "jnxMbgSgwPPGtpV2ICsPTNotSuppTx": jnxMbgSgwPPGtpV2ICsPTNotSuppTx,
       "jnxMbgSgwPPGtpV2ICsAllDynAdOcRx": jnxMbgSgwPPGtpV2ICsAllDynAdOcRx,
       "jnxMbgSgwPPGtpV2ICsAllDynAdOcTx": jnxMbgSgwPPGtpV2ICsAllDynAdOcTx,
       "jnxMbgSgwPPGtpV2ICsNOTFTUECTXRx": jnxMbgSgwPPGtpV2ICsNOTFTUECTXRx,
       "jnxMbgSgwPPGtpV2ICsNOTFTUECTXTx": jnxMbgSgwPPGtpV2ICsNOTFTUECTXTx,
       "jnxMbgSgwPPGtpV2ICsProtoNtSupRx": jnxMbgSgwPPGtpV2ICsProtoNtSupRx,
       "jnxMbgSgwPPGtpV2ICsProtoNtSupTx": jnxMbgSgwPPGtpV2ICsProtoNtSupTx,
       "jnxMbgSgwPPGtpV2ICsUENotRespRx": jnxMbgSgwPPGtpV2ICsUENotRespRx,
       "jnxMbgSgwPPGtpV2ICsUENotRespTx": jnxMbgSgwPPGtpV2ICsUENotRespTx,
       "jnxMbgSgwPPGtpV2ICsUERefusesRx": jnxMbgSgwPPGtpV2ICsUERefusesRx,
       "jnxMbgSgwPPGtpV2ICsUERefusesTx": jnxMbgSgwPPGtpV2ICsUERefusesTx,
       "jnxMbgSgwPPGtpV2ICsServDeniedRx": jnxMbgSgwPPGtpV2ICsServDeniedRx,
       "jnxMbgSgwPPGtpV2ICsServDeniedTx": jnxMbgSgwPPGtpV2ICsServDeniedTx,
       "jnxMbgSgwPPGtpV2ICsUnabPageUERx": jnxMbgSgwPPGtpV2ICsUnabPageUERx,
       "jnxMbgSgwPPGtpV2ICsUnabPageUETx": jnxMbgSgwPPGtpV2ICsUnabPageUETx,
       "jnxMbgSgwPPGtpV2ICsNoMemRx": jnxMbgSgwPPGtpV2ICsNoMemRx,
       "jnxMbgSgwPPGtpV2ICsNoMemTx": jnxMbgSgwPPGtpV2ICsNoMemTx,
       "jnxMbgSgwPPGtpV2ICsUserAUTHFlRx": jnxMbgSgwPPGtpV2ICsUserAUTHFlRx,
       "jnxMbgSgwPPGtpV2ICsUserAUTHFlTx": jnxMbgSgwPPGtpV2ICsUserAUTHFlTx,
       "jnxMbgSgwPPGtpV2ICsAPNAcsDenRx": jnxMbgSgwPPGtpV2ICsAPNAcsDenRx,
       "jnxMbgSgwPPGtpV2ICsAPNAcsDenTx": jnxMbgSgwPPGtpV2ICsAPNAcsDenTx,
       "jnxMbgSgwPPGtpV2ICsReqRejRx": jnxMbgSgwPPGtpV2ICsReqRejRx,
       "jnxMbgSgwPPGtpV2ICsReqRejTx": jnxMbgSgwPPGtpV2ICsReqRejTx,
       "jnxMbgSgwPPGtpV2ICsPTMSISigMMRx": jnxMbgSgwPPGtpV2ICsPTMSISigMMRx,
       "jnxMbgSgwPPGtpV2ICsPTMSISigMMTx": jnxMbgSgwPPGtpV2ICsPTMSISigMMTx,
       "jnxMbgSgwPPGtpV2ICsIMSINotKnRx": jnxMbgSgwPPGtpV2ICsIMSINotKnRx,
       "jnxMbgSgwPPGtpV2ICsIMSINotKnTx": jnxMbgSgwPPGtpV2ICsIMSINotKnTx,
       "jnxMbgSgwPPGtpV2ICsCondIEMsRx": jnxMbgSgwPPGtpV2ICsCondIEMsRx,
       "jnxMbgSgwPPGtpV2ICsCondIEMsTx": jnxMbgSgwPPGtpV2ICsCondIEMsTx,
       "jnxMbgSgwPPGtpV2ICsAPNResTIncRx": jnxMbgSgwPPGtpV2ICsAPNResTIncRx,
       "jnxMbgSgwPPGtpV2ICsAPNResTIncTx": jnxMbgSgwPPGtpV2ICsAPNResTIncTx,
       "jnxMbgSgwPPGtpV2ICsUnknownRx": jnxMbgSgwPPGtpV2ICsUnknownRx,
       "jnxMbgSgwPPGtpV2ICsUnknownTx": jnxMbgSgwPPGtpV2ICsUnknownTx,
       "jnxMbgSgwPPGtpV2ICsLclDetRx": jnxMbgSgwPPGtpV2ICsLclDetRx,
       "jnxMbgSgwPPGtpV2ICsLclDetTx": jnxMbgSgwPPGtpV2ICsLclDetTx,
       "jnxMbgSgwPPGtpV2ICsCmpDetRx": jnxMbgSgwPPGtpV2ICsCmpDetRx,
       "jnxMbgSgwPPGtpV2ICsCmpDetTx": jnxMbgSgwPPGtpV2ICsCmpDetTx,
       "jnxMbgSgwPPGtpV2ICsRATChgRx": jnxMbgSgwPPGtpV2ICsRATChgRx,
       "jnxMbgSgwPPGtpV2ICsRATChgTx": jnxMbgSgwPPGtpV2ICsRATChgTx,
       "jnxMbgSgwPPGtpV2ICsISRDeactRx": jnxMbgSgwPPGtpV2ICsISRDeactRx,
       "jnxMbgSgwPPGtpV2ICsISRDeactTx": jnxMbgSgwPPGtpV2ICsISRDeactTx,
       "jnxMbgSgwPPGtpV2ICsEIFRNCEnRx": jnxMbgSgwPPGtpV2ICsEIFRNCEnRx,
       "jnxMbgSgwPPGtpV2ICsEIFRNCEnTx": jnxMbgSgwPPGtpV2ICsEIFRNCEnTx,
       "jnxMbgSgwPPGtpV2ICsSemErTADRx": jnxMbgSgwPPGtpV2ICsSemErTADRx,
       "jnxMbgSgwPPGtpV2ICsSemErTADTx": jnxMbgSgwPPGtpV2ICsSemErTADTx,
       "jnxMbgSgwPPGtpV2ICsSynErTADRx": jnxMbgSgwPPGtpV2ICsSynErTADRx,
       "jnxMbgSgwPPGtpV2ICsSynErTADTx": jnxMbgSgwPPGtpV2ICsSynErTADTx,
       "jnxMbgSgwPPGtpV2ICsRMValRcvRx": jnxMbgSgwPPGtpV2ICsRMValRcvRx,
       "jnxMbgSgwPPGtpV2ICsRMValRcvTx": jnxMbgSgwPPGtpV2ICsRMValRcvTx,
       "jnxMbgSgwPPGtpV2ICsRPrNtRspRx": jnxMbgSgwPPGtpV2ICsRPrNtRspRx,
       "jnxMbgSgwPPGtpV2ICsRPrNtRspTx": jnxMbgSgwPPGtpV2ICsRPrNtRspTx,
       "jnxMbgSgwPPGtpV2ICsColNWReqRx": jnxMbgSgwPPGtpV2ICsColNWReqRx,
       "jnxMbgSgwPPGtpV2ICsColNWReqTx": jnxMbgSgwPPGtpV2ICsColNWReqTx,
       "jnxMbgSgwPPGtpV2ICsUnPgUESusRx": jnxMbgSgwPPGtpV2ICsUnPgUESusRx,
       "jnxMbgSgwPPGtpV2ICsUnPgUESusTx": jnxMbgSgwPPGtpV2ICsUnPgUESusTx,
       "jnxMbgSgwPPGtpV2ICsInvTotLenRx": jnxMbgSgwPPGtpV2ICsInvTotLenRx,
       "jnxMbgSgwPPGtpV2ICsInvTotLenTx": jnxMbgSgwPPGtpV2ICsInvTotLenTx,
       "jnxMbgSgwPPGtpV2ICsDtForNtSupRx": jnxMbgSgwPPGtpV2ICsDtForNtSupRx,
       "jnxMbgSgwPPGtpV2ICsDtForNtSupTx": jnxMbgSgwPPGtpV2ICsDtForNtSupTx,
       "jnxMbgSgwPPGtpV2ICsInReFRePrRx": jnxMbgSgwPPGtpV2ICsInReFRePrRx,
       "jnxMbgSgwPPGtpV2ICsInReFRePrTx": jnxMbgSgwPPGtpV2ICsInReFRePrTx,
       "jnxMbgSgwPPGtpV2ICsInvPrRx": jnxMbgSgwPPGtpV2ICsInvPrRx,
       "jnxMbgSgwPPGtpV2ICsInvPrTx": jnxMbgSgwPPGtpV2ICsInvPrTx,
       "jnxMbgSgwPPGtpV1ProtocolErrRx": jnxMbgSgwPPGtpV1ProtocolErrRx,
       "jnxMbgSgwPPGtpV1UnSupMsgRx": jnxMbgSgwPPGtpV1UnSupMsgRx,
       "jnxMbgSgwPPGtpV1T3RespTmrExpRx": jnxMbgSgwPPGtpV1T3RespTmrExpRx,
       "jnxMbgSgwPPGtpV1EndMarkerRx": jnxMbgSgwPPGtpV1EndMarkerRx,
       "jnxMbgSgwPPGtpV1EndMarkerTx": jnxMbgSgwPPGtpV1EndMarkerTx,
       "jnxMbgSgwPPGtpV1EchoReqRx": jnxMbgSgwPPGtpV1EchoReqRx,
       "jnxMbgSgwPPGtpV1EchoReqTx": jnxMbgSgwPPGtpV1EchoReqTx,
       "jnxMbgSgwPPGtpV1EchoRespRx": jnxMbgSgwPPGtpV1EchoRespRx,
       "jnxMbgSgwPPGtpV1EchoRespTx": jnxMbgSgwPPGtpV1EchoRespTx,
       "jnxMbgSgwPPGtpV1ErrIndRx": jnxMbgSgwPPGtpV1ErrIndRx,
       "jnxMbgSgwPPGtpV1ErrIndTx": jnxMbgSgwPPGtpV1ErrIndTx,
       "jnxMbgSgwPPSuspNotifRx": jnxMbgSgwPPSuspNotifRx,
       "jnxMbgSgwPPSuspNotifTx": jnxMbgSgwPPSuspNotifTx,
       "jnxMbgSgwPPSuspAckRx": jnxMbgSgwPPSuspAckRx,
       "jnxMbgSgwPPSuspAckTx": jnxMbgSgwPPSuspAckTx,
       "jnxMbgSgwPPResumeNotifRx": jnxMbgSgwPPResumeNotifRx,
       "jnxMbgSgwPPResumeNotifTx": jnxMbgSgwPPResumeNotifTx,
       "jnxMbgSgwPPResumeAckRx": jnxMbgSgwPPResumeAckRx,
       "jnxMbgSgwPPResumeAckTx": jnxMbgSgwPPResumeAckTx,
       "jnxMbgSgwPPPiggybackMsgRx": jnxMbgSgwPPPiggybackMsgRx,
       "jnxMbgSgwPPPiggybackMsgTx": jnxMbgSgwPPPiggybackMsgTx,
       "jnxMbgSgwGtpCGlbStatsTable": jnxMbgSgwGtpCGlbStatsTable,
       "jnxMbgSgwGtpGlbStatsEntry": jnxMbgSgwGtpGlbStatsEntry,
       "jnxMbgSgwRxPacketsDropped": jnxMbgSgwRxPacketsDropped,
       "jnxMbgSgwPacketAllocFail": jnxMbgSgwPacketAllocFail,
       "jnxMbgSgwPacketSendFail": jnxMbgSgwPacketSendFail,
       "jnxMbgSgwIPVerErrRx": jnxMbgSgwIPVerErrRx,
       "jnxMbgSgwIPProtoErrRx": jnxMbgSgwIPProtoErrRx,
       "jnxMbgSgwGTPPortErrRx": jnxMbgSgwGTPPortErrRx,
       "jnxMbgSgwGTPUnknVerRx": jnxMbgSgwGTPUnknVerRx,
       "jnxMbgSgwPcktLenErrRx": jnxMbgSgwPcktLenErrRx,
       "jnxMbgSgwUnknMsgRx": jnxMbgSgwUnknMsgRx,
       "jnxMbgSgwProtocolErrRx": jnxMbgSgwProtocolErrRx,
       "jnxMbgSgwUnSupportedMsgRx": jnxMbgSgwUnSupportedMsgRx,
       "jnxMbgSgwT3RespTmrExpRx": jnxMbgSgwT3RespTmrExpRx,
       "jnxMbgSgwV2NumMsgRx": jnxMbgSgwV2NumMsgRx,
       "jnxMbgSgwV2NumMsgTx": jnxMbgSgwV2NumMsgTx,
       "jnxMbgSgwV2NumBytesRx": jnxMbgSgwV2NumBytesRx,
       "jnxMbgSgwV2NumBytesTx": jnxMbgSgwV2NumBytesTx,
       "jnxMbgSgwV2EchoReqRx": jnxMbgSgwV2EchoReqRx,
       "jnxMbgSgwV2EchoReqTx": jnxMbgSgwV2EchoReqTx,
       "jnxMbgSgwV2EchoRespRx": jnxMbgSgwV2EchoRespRx,
       "jnxMbgSgwV2EchoRespTx": jnxMbgSgwV2EchoRespTx,
       "jnxMbgSgwV2VerNotSupRx": jnxMbgSgwV2VerNotSupRx,
       "jnxMbgSgwV2VerNotSupTx": jnxMbgSgwV2VerNotSupTx,
       "jnxMbgSgwCreateSessReqRx": jnxMbgSgwCreateSessReqRx,
       "jnxMbgSgwCreateSessReqTx": jnxMbgSgwCreateSessReqTx,
       "jnxMbgSgwCreateSessRspRx": jnxMbgSgwCreateSessRspRx,
       "jnxMbgSgwCreateSessRspTx": jnxMbgSgwCreateSessRspTx,
       "jnxMbgSgwModBrReqRx": jnxMbgSgwModBrReqRx,
       "jnxMbgSgwModBrReqTx": jnxMbgSgwModBrReqTx,
       "jnxMbgSgwModBrRspRx": jnxMbgSgwModBrRspRx,
       "jnxMbgSgwModBrRspTx": jnxMbgSgwModBrRspTx,
       "jnxMbgSgwDelSessReqRx": jnxMbgSgwDelSessReqRx,
       "jnxMbgSgwDelSessReqTx": jnxMbgSgwDelSessReqTx,
       "jnxMbgSgwDelSessRspRx": jnxMbgSgwDelSessRspRx,
       "jnxMbgSgwDelSessRspTx": jnxMbgSgwDelSessRspTx,
       "jnxMbgSgwCrtBrReqRx": jnxMbgSgwCrtBrReqRx,
       "jnxMbgSgwCrtBrReqTx": jnxMbgSgwCrtBrReqTx,
       "jnxMbgSgwCrtBrRspRx": jnxMbgSgwCrtBrRspRx,
       "jnxMbgSgwCrtBrRspTx": jnxMbgSgwCrtBrRspTx,
       "jnxMbgSgwUpdBrReqRx": jnxMbgSgwUpdBrReqRx,
       "jnxMbgSgwUpdBrReqTx": jnxMbgSgwUpdBrReqTx,
       "jnxMbgSgwUpdBrRspRx": jnxMbgSgwUpdBrRspRx,
       "jnxMbgSgwUpdBrRspTx": jnxMbgSgwUpdBrRspTx,
       "jnxMbgSgwDelBrReqRx": jnxMbgSgwDelBrReqRx,
       "jnxMbgSgwDelBrReqTx": jnxMbgSgwDelBrReqTx,
       "jnxMbgSgwDelBrRspRx": jnxMbgSgwDelBrRspRx,
       "jnxMbgSgwDelBrRspTx": jnxMbgSgwDelBrRspTx,
       "jnxMbgSgwDelConnSetReqRx": jnxMbgSgwDelConnSetReqRx,
       "jnxMbgSgwDelConnSetReqTx": jnxMbgSgwDelConnSetReqTx,
       "jnxMbgSgwDelConnSetRspRx": jnxMbgSgwDelConnSetRspRx,
       "jnxMbgSgwDelConnSetRspTx": jnxMbgSgwDelConnSetRspTx,
       "jnxMbgSgwUpdConnSetReqRx": jnxMbgSgwUpdConnSetReqRx,
       "jnxMbgSgwUpdConnSetReqTx": jnxMbgSgwUpdConnSetReqTx,
       "jnxMbgSgwUpdConnSetRspRx": jnxMbgSgwUpdConnSetRspRx,
       "jnxMbgSgwUpdConnSetRspTx": jnxMbgSgwUpdConnSetRspTx,
       "jnxMbgSgwModBrCmdRx": jnxMbgSgwModBrCmdRx,
       "jnxMbgSgwModBrCmdTx": jnxMbgSgwModBrCmdTx,
       "jnxMbgSgwModBrFlrIndRx": jnxMbgSgwModBrFlrIndRx,
       "jnxMbgSgwModBrFlrIndTx": jnxMbgSgwModBrFlrIndTx,
       "jnxMbgSgwDelBrCmdRx": jnxMbgSgwDelBrCmdRx,
       "jnxMbgSgwDelBrCmdTx": jnxMbgSgwDelBrCmdTx,
       "jnxMbgSgwDelBrFlrIndRx": jnxMbgSgwDelBrFlrIndRx,
       "jnxMbgSgwDelBrFlrIndTx": jnxMbgSgwDelBrFlrIndTx,
       "jnxMbgSgwBrResCmdRx": jnxMbgSgwBrResCmdRx,
       "jnxMbgSgwBrResCmdTx": jnxMbgSgwBrResCmdTx,
       "jnxMbgSgwBrResFlrIndRx": jnxMbgSgwBrResFlrIndRx,
       "jnxMbgSgwBrResFlrIndTx": jnxMbgSgwBrResFlrIndTx,
       "jnxMbgSgwRelAcsBrReqRx": jnxMbgSgwRelAcsBrReqRx,
       "jnxMbgSgwRelAcsBrReqTx": jnxMbgSgwRelAcsBrReqTx,
       "jnxMbgSgwRelAcsBrRespRx": jnxMbgSgwRelAcsBrRespRx,
       "jnxMbgSgwRelAcsBrRespTx": jnxMbgSgwRelAcsBrRespTx,
       "jnxMbgSgwCrIndTunReqRx": jnxMbgSgwCrIndTunReqRx,
       "jnxMbgSgwCrIndTunReqTx": jnxMbgSgwCrIndTunReqTx,
       "jnxMbgSgwCrIndTunRespRx": jnxMbgSgwCrIndTunRespRx,
       "jnxMbgSgwCrIndTunRespTx": jnxMbgSgwCrIndTunRespTx,
       "jnxMbgSgwDelIndTunReqRx": jnxMbgSgwDelIndTunReqRx,
       "jnxMbgSgwDelIndTunReqTx": jnxMbgSgwDelIndTunReqTx,
       "jnxMbgSgwDelIndTunRespRx": jnxMbgSgwDelIndTunRespRx,
       "jnxMbgSgwDelIndTunRespTx": jnxMbgSgwDelIndTunRespTx,
       "jnxMbgSgwDlDataNotifRx": jnxMbgSgwDlDataNotifRx,
       "jnxMbgSgwDlDataNotifTx": jnxMbgSgwDlDataNotifTx,
       "jnxMbgSgwDlDataAckRx": jnxMbgSgwDlDataAckRx,
       "jnxMbgSgwDlDataAckTx": jnxMbgSgwDlDataAckTx,
       "jnxMbgSgwDlDataNotiFlrIndRx": jnxMbgSgwDlDataNotiFlrIndRx,
       "jnxMbgSgwDlDataNotiFlrIndTx": jnxMbgSgwDlDataNotiFlrIndTx,
       "jnxMbgSgwStopPagingIndRx": jnxMbgSgwStopPagingIndRx,
       "jnxMbgSgwStopPagingIndTx": jnxMbgSgwStopPagingIndTx,
       "jnxMbgSgwGtpV2ICsPageRx": jnxMbgSgwGtpV2ICsPageRx,
       "jnxMbgSgwGtpV2ICsPageTx": jnxMbgSgwGtpV2ICsPageTx,
       "jnxMbgSgwGtpV2ICsReqAcceptRx": jnxMbgSgwGtpV2ICsReqAcceptRx,
       "jnxMbgSgwGtpV2ICsReqAcceptTx": jnxMbgSgwGtpV2ICsReqAcceptTx,
       "jnxMbgSgwGtpV2ICsAcceptPartRx": jnxMbgSgwGtpV2ICsAcceptPartRx,
       "jnxMbgSgwGtpV2ICsAcceptPartTx": jnxMbgSgwGtpV2ICsAcceptPartTx,
       "jnxMbgSgwGtpV2ICsNewPTNPrefRx": jnxMbgSgwGtpV2ICsNewPTNPrefRx,
       "jnxMbgSgwGtpV2ICsNewPTNPrefTx": jnxMbgSgwGtpV2ICsNewPTNPrefTx,
       "jnxMbgSgwGtpV2ICsNewPTSIAdbrRx": jnxMbgSgwGtpV2ICsNewPTSIAdbrRx,
       "jnxMbgSgwGtpV2ICsNewPTSIAdbrTx": jnxMbgSgwGtpV2ICsNewPTSIAdbrTx,
       "jnxMbgSgwGtpV2ICsCtxNotFndRx": jnxMbgSgwGtpV2ICsCtxNotFndRx,
       "jnxMbgSgwGtpV2ICsCtxNotFndTx": jnxMbgSgwGtpV2ICsCtxNotFndTx,
       "jnxMbgSgwGtpV2ICsInvMsgFmtRx": jnxMbgSgwGtpV2ICsInvMsgFmtRx,
       "jnxMbgSgwGtpV2ICsInvMsgFmtTx": jnxMbgSgwGtpV2ICsInvMsgFmtTx,
       "jnxMbgSgwGtpV2ICsVerNotSuppRx": jnxMbgSgwGtpV2ICsVerNotSuppRx,
       "jnxMbgSgwGtpV2ICsVerNotSuppTx": jnxMbgSgwGtpV2ICsVerNotSuppTx,
       "jnxMbgSgwGtpV2ICsInvLenRx": jnxMbgSgwGtpV2ICsInvLenRx,
       "jnxMbgSgwGtpV2ICsInvLenTx": jnxMbgSgwGtpV2ICsInvLenTx,
       "jnxMbgSgwGtpV2ICsServNotSuppRx": jnxMbgSgwGtpV2ICsServNotSuppRx,
       "jnxMbgSgwGtpV2ICsServNotSuppTx": jnxMbgSgwGtpV2ICsServNotSuppTx,
       "jnxMbgSgwGtpV2ICsManIEIncorrRx": jnxMbgSgwGtpV2ICsManIEIncorrRx,
       "jnxMbgSgwGtpV2ICsManIEIncorrTx": jnxMbgSgwGtpV2ICsManIEIncorrTx,
       "jnxMbgSgwGtpV2ICsManIEMissRx": jnxMbgSgwGtpV2ICsManIEMissRx,
       "jnxMbgSgwGtpV2ICsManIEMissTx": jnxMbgSgwGtpV2ICsManIEMissTx,
       "jnxMbgSgwGtpV2ICsOptIEIncorrRx": jnxMbgSgwGtpV2ICsOptIEIncorrRx,
       "jnxMbgSgwGtpV2ICsOptIEIncorrTx": jnxMbgSgwGtpV2ICsOptIEIncorrTx,
       "jnxMbgSgwGtpV2ICsSysFailRx": jnxMbgSgwGtpV2ICsSysFailRx,
       "jnxMbgSgwGtpV2ICsSysFailTx": jnxMbgSgwGtpV2ICsSysFailTx,
       "jnxMbgSgwGtpV2ICsNoResRx": jnxMbgSgwGtpV2ICsNoResRx,
       "jnxMbgSgwGtpV2ICsNoResTx": jnxMbgSgwGtpV2ICsNoResTx,
       "jnxMbgSgwGtpV2ICsTFTSMANTErRx": jnxMbgSgwGtpV2ICsTFTSMANTErRx,
       "jnxMbgSgwGtpV2ICsTFTSMANTErTx": jnxMbgSgwGtpV2ICsTFTSMANTErTx,
       "jnxMbgSgwGtpV2ICsTFTSysErrRx": jnxMbgSgwGtpV2ICsTFTSysErrRx,
       "jnxMbgSgwGtpV2ICsTFTSysErrTx": jnxMbgSgwGtpV2ICsTFTSysErrTx,
       "jnxMbgSgwGtpV2ICsPkFltManErrRx": jnxMbgSgwGtpV2ICsPkFltManErrRx,
       "jnxMbgSgwGtpV2ICsPkFltManErrTx": jnxMbgSgwGtpV2ICsPkFltManErrTx,
       "jnxMbgSgwGtpV2ICsPkFltSynErrRx": jnxMbgSgwGtpV2ICsPkFltSynErrRx,
       "jnxMbgSgwGtpV2ICsPkFltSynErrTx": jnxMbgSgwGtpV2ICsPkFltSynErrTx,
       "jnxMbgSgwGtpV2ICsMisUnknAPNRx": jnxMbgSgwGtpV2ICsMisUnknAPNRx,
       "jnxMbgSgwGtpV2ICsMisUnknAPNTx": jnxMbgSgwGtpV2ICsMisUnknAPNTx,
       "jnxMbgSgwGtpV2ICsUnexpRptIERx": jnxMbgSgwGtpV2ICsUnexpRptIERx,
       "jnxMbgSgwGtpV2ICsUnexpRptIETx": jnxMbgSgwGtpV2ICsUnexpRptIETx,
       "jnxMbgSgwGtpV2ICsGREKeyNtFdRx": jnxMbgSgwGtpV2ICsGREKeyNtFdRx,
       "jnxMbgSgwGtpV2ICsGREKeyNtFdTx": jnxMbgSgwGtpV2ICsGREKeyNtFdTx,
       "jnxMbgSgwGtpV2ICsRelocFailRx": jnxMbgSgwGtpV2ICsRelocFailRx,
       "jnxMbgSgwGtpV2ICsRelocFailTx": jnxMbgSgwGtpV2ICsRelocFailTx,
       "jnxMbgSgwGtpV2ICsDeniedINRatRx": jnxMbgSgwGtpV2ICsDeniedINRatRx,
       "jnxMbgSgwGtpV2ICsDeniedINRatTx": jnxMbgSgwGtpV2ICsDeniedINRatTx,
       "jnxMbgSgwGtpV2ICsPTNotSuppRx": jnxMbgSgwGtpV2ICsPTNotSuppRx,
       "jnxMbgSgwGtpV2ICsPTNotSuppTx": jnxMbgSgwGtpV2ICsPTNotSuppTx,
       "jnxMbgSgwGtpV2ICsAllDynAdOccRx": jnxMbgSgwGtpV2ICsAllDynAdOccRx,
       "jnxMbgSgwGtpV2ICsAllDynAdOccTx": jnxMbgSgwGtpV2ICsAllDynAdOccTx,
       "jnxMbgSgwGtpV2ICsNOTFTUECTXRx": jnxMbgSgwGtpV2ICsNOTFTUECTXRx,
       "jnxMbgSgwGtpV2ICsNOTFTUECTXTx": jnxMbgSgwGtpV2ICsNOTFTUECTXTx,
       "jnxMbgSgwGtpV2ICsProtoNtSupRx": jnxMbgSgwGtpV2ICsProtoNtSupRx,
       "jnxMbgSgwGtpV2ICsProtoNtSupTx": jnxMbgSgwGtpV2ICsProtoNtSupTx,
       "jnxMbgSgwGtpV2ICsUENotRespRx": jnxMbgSgwGtpV2ICsUENotRespRx,
       "jnxMbgSgwGtpV2ICsUENotRespTx": jnxMbgSgwGtpV2ICsUENotRespTx,
       "jnxMbgSgwGtpV2ICsUERefusesRx": jnxMbgSgwGtpV2ICsUERefusesRx,
       "jnxMbgSgwGtpV2ICsUERefusesTx": jnxMbgSgwGtpV2ICsUERefusesTx,
       "jnxMbgSgwGtpV2ICsServDeniedRx": jnxMbgSgwGtpV2ICsServDeniedRx,
       "jnxMbgSgwGtpV2ICsServDeniedTx": jnxMbgSgwGtpV2ICsServDeniedTx,
       "jnxMbgSgwGtpV2ICsUnabPageUERx": jnxMbgSgwGtpV2ICsUnabPageUERx,
       "jnxMbgSgwGtpV2ICsUnabPageUETx": jnxMbgSgwGtpV2ICsUnabPageUETx,
       "jnxMbgSgwGtpV2ICsNoMemRx": jnxMbgSgwGtpV2ICsNoMemRx,
       "jnxMbgSgwGtpV2ICsNoMemTx": jnxMbgSgwGtpV2ICsNoMemTx,
       "jnxMbgSgwGtpV2ICsUserAUTHFlRx": jnxMbgSgwGtpV2ICsUserAUTHFlRx,
       "jnxMbgSgwGtpV2ICsUserAUTHFlTx": jnxMbgSgwGtpV2ICsUserAUTHFlTx,
       "jnxMbgSgwGtpV2ICsAPNAcsDenRx": jnxMbgSgwGtpV2ICsAPNAcsDenRx,
       "jnxMbgSgwGtpV2ICsAPNAcsDenTx": jnxMbgSgwGtpV2ICsAPNAcsDenTx,
       "jnxMbgSgwGtpV2ICsReqRejRx": jnxMbgSgwGtpV2ICsReqRejRx,
       "jnxMbgSgwGtpV2ICsReqRejTx": jnxMbgSgwGtpV2ICsReqRejTx,
       "jnxMbgSgwGtpV2ICsPTMSISigMMRx": jnxMbgSgwGtpV2ICsPTMSISigMMRx,
       "jnxMbgSgwGtpV2ICsPTMSISigMMTx": jnxMbgSgwGtpV2ICsPTMSISigMMTx,
       "jnxMbgSgwGtpV2ICsIMSINotKnRx": jnxMbgSgwGtpV2ICsIMSINotKnRx,
       "jnxMbgSgwGtpV2ICsIMSINotKnTx": jnxMbgSgwGtpV2ICsIMSINotKnTx,
       "jnxMbgSgwGtpV2ICsCondIEMsRx": jnxMbgSgwGtpV2ICsCondIEMsRx,
       "jnxMbgSgwGtpV2ICsCondIEMsTx": jnxMbgSgwGtpV2ICsCondIEMsTx,
       "jnxMbgSgwGtpV2ICsAPNResTIncRx": jnxMbgSgwGtpV2ICsAPNResTIncRx,
       "jnxMbgSgwGtpV2ICsAPNResTIncTx": jnxMbgSgwGtpV2ICsAPNResTIncTx,
       "jnxMbgSgwGtpV2ICsUnknownRx": jnxMbgSgwGtpV2ICsUnknownRx,
       "jnxMbgSgwGtpV2ICsUnknownTx": jnxMbgSgwGtpV2ICsUnknownTx,
       "jnxMbgSgwGtpV2ICsLclDetRx": jnxMbgSgwGtpV2ICsLclDetRx,
       "jnxMbgSgwGtpV2ICsLclDetTx": jnxMbgSgwGtpV2ICsLclDetTx,
       "jnxMbgSgwGtpV2ICsCmpDetRx": jnxMbgSgwGtpV2ICsCmpDetRx,
       "jnxMbgSgwGtpV2ICsCmpDetTx": jnxMbgSgwGtpV2ICsCmpDetTx,
       "jnxMbgSgwGtpV2ICsRATChgRx": jnxMbgSgwGtpV2ICsRATChgRx,
       "jnxMbgSgwGtpV2ICsRATChgTx": jnxMbgSgwGtpV2ICsRATChgTx,
       "jnxMbgSgwGtpV2ICsISRDeactRx": jnxMbgSgwGtpV2ICsISRDeactRx,
       "jnxMbgSgwGtpV2ICsISRDeactTx": jnxMbgSgwGtpV2ICsISRDeactTx,
       "jnxMbgSgwGtpV2ICsEIFRNCEnRx": jnxMbgSgwGtpV2ICsEIFRNCEnRx,
       "jnxMbgSgwGtpV2ICsEIFRNCEnTx": jnxMbgSgwGtpV2ICsEIFRNCEnTx,
       "jnxMbgSgwGtpV2ICsSemErTADRx": jnxMbgSgwGtpV2ICsSemErTADRx,
       "jnxMbgSgwGtpV2ICsSemErTADTx": jnxMbgSgwGtpV2ICsSemErTADTx,
       "jnxMbgSgwGtpV2ICsSynErTADRx": jnxMbgSgwGtpV2ICsSynErTADRx,
       "jnxMbgSgwGtpV2ICsSynErTADTx": jnxMbgSgwGtpV2ICsSynErTADTx,
       "jnxMbgSgwGtpV2ICsRMValRcvRx": jnxMbgSgwGtpV2ICsRMValRcvRx,
       "jnxMbgSgwGtpV2ICsRMValRcvTx": jnxMbgSgwGtpV2ICsRMValRcvTx,
       "jnxMbgSgwGtpV2ICsRPrNtRspRx": jnxMbgSgwGtpV2ICsRPrNtRspRx,
       "jnxMbgSgwGtpV2ICsRPrNtRspTx": jnxMbgSgwGtpV2ICsRPrNtRspTx,
       "jnxMbgSgwGtpV2ICsColNWReqRx": jnxMbgSgwGtpV2ICsColNWReqRx,
       "jnxMbgSgwGtpV2ICsColNWReqTx": jnxMbgSgwGtpV2ICsColNWReqTx,
       "jnxMbgSgwGtpV2ICsUnPgUESusRx": jnxMbgSgwGtpV2ICsUnPgUESusRx,
       "jnxMbgSgwGtpV2ICsUnPgUESusTx": jnxMbgSgwGtpV2ICsUnPgUESusTx,
       "jnxMbgSgwGtpV2ICsInvTotLenRx": jnxMbgSgwGtpV2ICsInvTotLenRx,
       "jnxMbgSgwGtpV2ICsInvTotLenTx": jnxMbgSgwGtpV2ICsInvTotLenTx,
       "jnxMbgSgwGtpV2ICsDtForNtSupRx": jnxMbgSgwGtpV2ICsDtForNtSupRx,
       "jnxMbgSgwGtpV2ICsDtForNtSupTx": jnxMbgSgwGtpV2ICsDtForNtSupTx,
       "jnxMbgSgwGtpV2ICsInReFRePrRx": jnxMbgSgwGtpV2ICsInReFRePrRx,
       "jnxMbgSgwGtpV2ICsInReFRePrTx": jnxMbgSgwGtpV2ICsInReFRePrTx,
       "jnxMbgSgwGtpV2ICsInvPrRx": jnxMbgSgwGtpV2ICsInvPrRx,
       "jnxMbgSgwGtpV2ICsInvPrTx": jnxMbgSgwGtpV2ICsInvPrTx,
       "jnxMbgSgwGtpV1ProtocolErrRx": jnxMbgSgwGtpV1ProtocolErrRx,
       "jnxMbgSgwGtpV1UnSupMsgRx": jnxMbgSgwGtpV1UnSupMsgRx,
       "jnxMbgSgwGtpV1T3RespTmrExpRx": jnxMbgSgwGtpV1T3RespTmrExpRx,
       "jnxMbgSgwGtpV1EndMarkerRx": jnxMbgSgwGtpV1EndMarkerRx,
       "jnxMbgSgwGtpV1EndMarkerTx": jnxMbgSgwGtpV1EndMarkerTx,
       "jnxMbgSgwGtpV1EchoReqRx": jnxMbgSgwGtpV1EchoReqRx,
       "jnxMbgSgwGtpV1EchoReqTx": jnxMbgSgwGtpV1EchoReqTx,
       "jnxMbgSgwGtpV1EchoRespRx": jnxMbgSgwGtpV1EchoRespRx,
       "jnxMbgSgwGtpV1EchoRespTx": jnxMbgSgwGtpV1EchoRespTx,
       "jnxMbgSgwGtpV1ErrIndRx": jnxMbgSgwGtpV1ErrIndRx,
       "jnxMbgSgwGtpV1ErrIndTx": jnxMbgSgwGtpV1ErrIndTx,
       "jnxMbgSgwSuspNotifRx": jnxMbgSgwSuspNotifRx,
       "jnxMbgSgwSuspNotifTx": jnxMbgSgwSuspNotifTx,
       "jnxMbgSgwSuspAckRx": jnxMbgSgwSuspAckRx,
       "jnxMbgSgwSuspAckTx": jnxMbgSgwSuspAckTx,
       "jnxMbgSgwResumeNotifRx": jnxMbgSgwResumeNotifRx,
       "jnxMbgSgwResumeNotifTx": jnxMbgSgwResumeNotifTx,
       "jnxMbgSgwResumeAckRx": jnxMbgSgwResumeAckRx,
       "jnxMbgSgwResumeAckTx": jnxMbgSgwResumeAckTx,
       "jnxMbgSgwS11PiggybackMsgRx": jnxMbgSgwS11PiggybackMsgRx,
       "jnxMbgSgwS11PiggybackMsgTx": jnxMbgSgwS11PiggybackMsgTx,
       "jnxMbgSgwS4PiggybackMsgRx": jnxMbgSgwS4PiggybackMsgRx,
       "jnxMbgSgwS4PiggybackMsgTx": jnxMbgSgwS4PiggybackMsgTx,
       "jnxMbgSgwS5PiggybackMsgRx": jnxMbgSgwS5PiggybackMsgRx,
       "jnxMbgSgwS5PiggybackMsgTx": jnxMbgSgwS5PiggybackMsgTx,
       "jnxMbgSgwGtpNotificationVars": jnxMbgSgwGtpNotificationVars,
       "jnxMbgSgwGtpPeerName": jnxMbgSgwGtpPeerName,
       "jnxMbgSgwGtpAlarmStatCounter": jnxMbgSgwGtpAlarmStatCounter,
       "jnxMbgSgwGtpInterfaceType": jnxMbgSgwGtpInterfaceType,
       "jnxMbgSgwGtpGwName": jnxMbgSgwGtpGwName,
       "jnxMbgSgwGtpGwIndex": jnxMbgSgwGtpGwIndex,
       "jnxMbgSgwGtpIfStatsTable": jnxMbgSgwGtpIfStatsTable,
       "jnxMbgSgwGtpIfStatsEntry": jnxMbgSgwGtpIfStatsEntry,
       "jnxMbgSgwIfIndex": jnxMbgSgwIfIndex,
       "jnxMbgSgwIfType": jnxMbgSgwIfType,
       "jnxMbgSgwIfRxPacketsDropped": jnxMbgSgwIfRxPacketsDropped,
       "jnxMbgSgwIfPacketAllocFail": jnxMbgSgwIfPacketAllocFail,
       "jnxMbgSgwIfPacketSendFail": jnxMbgSgwIfPacketSendFail,
       "jnxMbgSgwIfIPVerErrRx": jnxMbgSgwIfIPVerErrRx,
       "jnxMbgSgwIfIPProtoErrRx": jnxMbgSgwIfIPProtoErrRx,
       "jnxMbgSgwIfGTPPortErrRx": jnxMbgSgwIfGTPPortErrRx,
       "jnxMbgSgwIfGTPUnknVerRx": jnxMbgSgwIfGTPUnknVerRx,
       "jnxMbgSgwIfPcktLenErrRx": jnxMbgSgwIfPcktLenErrRx,
       "jnxMbgSgwIfUnknMsgRx": jnxMbgSgwIfUnknMsgRx,
       "jnxMbgSgwIfProtocolErrRx": jnxMbgSgwIfProtocolErrRx,
       "jnxMbgSgwIfUnSupportedMsgRx": jnxMbgSgwIfUnSupportedMsgRx,
       "jnxMbgSgwIfT3RespTmrExpRx": jnxMbgSgwIfT3RespTmrExpRx,
       "jnxMbgSgwIfV2NumMsgRx": jnxMbgSgwIfV2NumMsgRx,
       "jnxMbgSgwIfV2NumMsgTx": jnxMbgSgwIfV2NumMsgTx,
       "jnxMbgSgwIfV2NumBytesRx": jnxMbgSgwIfV2NumBytesRx,
       "jnxMbgSgwIfV2NumBytesTx": jnxMbgSgwIfV2NumBytesTx,
       "jnxMbgSgwIfV2EchoReqRx": jnxMbgSgwIfV2EchoReqRx,
       "jnxMbgSgwIfV2EchoReqTx": jnxMbgSgwIfV2EchoReqTx,
       "jnxMbgSgwIfV2EchoRespRx": jnxMbgSgwIfV2EchoRespRx,
       "jnxMbgSgwIfV2EchoRespTx": jnxMbgSgwIfV2EchoRespTx,
       "jnxMbgSgwIfV2VerNotSupRx": jnxMbgSgwIfV2VerNotSupRx,
       "jnxMbgSgwIfV2VerNotSupTx": jnxMbgSgwIfV2VerNotSupTx,
       "jnxMbgSgwIfCreateSessReqRx": jnxMbgSgwIfCreateSessReqRx,
       "jnxMbgSgwIfCreateSessReqTx": jnxMbgSgwIfCreateSessReqTx,
       "jnxMbgSgwIfCreateSessRspRx": jnxMbgSgwIfCreateSessRspRx,
       "jnxMbgSgwIfCreateSessRspTx": jnxMbgSgwIfCreateSessRspTx,
       "jnxMbgSgwIfModBrReqRx": jnxMbgSgwIfModBrReqRx,
       "jnxMbgSgwIfModBrReqTx": jnxMbgSgwIfModBrReqTx,
       "jnxMbgSgwIfModBrRspRx": jnxMbgSgwIfModBrRspRx,
       "jnxMbgSgwIfModBrRspTx": jnxMbgSgwIfModBrRspTx,
       "jnxMbgSgwIfDelSessReqRx": jnxMbgSgwIfDelSessReqRx,
       "jnxMbgSgwIfDelSessReqTx": jnxMbgSgwIfDelSessReqTx,
       "jnxMbgSgwIfDelSessRspRx": jnxMbgSgwIfDelSessRspRx,
       "jnxMbgSgwIfDelSessRspTx": jnxMbgSgwIfDelSessRspTx,
       "jnxMbgSgwIfCrtBrReqRx": jnxMbgSgwIfCrtBrReqRx,
       "jnxMbgSgwIfCrtBrReqTx": jnxMbgSgwIfCrtBrReqTx,
       "jnxMbgSgwIfCrtBrRspRx": jnxMbgSgwIfCrtBrRspRx,
       "jnxMbgSgwIfCrtBrRspTx": jnxMbgSgwIfCrtBrRspTx,
       "jnxMbgSgwIfUpdBrReqRx": jnxMbgSgwIfUpdBrReqRx,
       "jnxMbgSgwIfUpdBrReqTx": jnxMbgSgwIfUpdBrReqTx,
       "jnxMbgSgwIfUpdBrRspRx": jnxMbgSgwIfUpdBrRspRx,
       "jnxMbgSgwIfUpdBrRspTx": jnxMbgSgwIfUpdBrRspTx,
       "jnxMbgSgwIfDelBrReqRx": jnxMbgSgwIfDelBrReqRx,
       "jnxMbgSgwIfDelBrReqTx": jnxMbgSgwIfDelBrReqTx,
       "jnxMbgSgwIfDelBrRspRx": jnxMbgSgwIfDelBrRspRx,
       "jnxMbgSgwIfDelBrRspTx": jnxMbgSgwIfDelBrRspTx,
       "jnxMbgSgwIfDelConnSetReqRx": jnxMbgSgwIfDelConnSetReqRx,
       "jnxMbgSgwIfDelConnSetReqTx": jnxMbgSgwIfDelConnSetReqTx,
       "jnxMbgSgwIfDelConnSetRspRx": jnxMbgSgwIfDelConnSetRspRx,
       "jnxMbgSgwIfDelConnSetRspTx": jnxMbgSgwIfDelConnSetRspTx,
       "jnxMbgSgwIfUpdConnSetReqRx": jnxMbgSgwIfUpdConnSetReqRx,
       "jnxMbgSgwIfUpdConnSetReqTx": jnxMbgSgwIfUpdConnSetReqTx,
       "jnxMbgSgwIfUpdConnSetRspRx": jnxMbgSgwIfUpdConnSetRspRx,
       "jnxMbgSgwIfUpdConnSetRspTx": jnxMbgSgwIfUpdConnSetRspTx,
       "jnxMbgSgwIfModBrCmdRx": jnxMbgSgwIfModBrCmdRx,
       "jnxMbgSgwIfModBrCmdTx": jnxMbgSgwIfModBrCmdTx,
       "jnxMbgSgwIfModBrFlrIndRx": jnxMbgSgwIfModBrFlrIndRx,
       "jnxMbgSgwIfModBrFlrIndTx": jnxMbgSgwIfModBrFlrIndTx,
       "jnxMbgSgwIfDelBrCmdRx": jnxMbgSgwIfDelBrCmdRx,
       "jnxMbgSgwIfDelBrCmdTx": jnxMbgSgwIfDelBrCmdTx,
       "jnxMbgSgwIfDelBrFlrIndRx": jnxMbgSgwIfDelBrFlrIndRx,
       "jnxMbgSgwIfDelBrFlrIndTx": jnxMbgSgwIfDelBrFlrIndTx,
       "jnxMbgSgwIfBrResCmdRx": jnxMbgSgwIfBrResCmdRx,
       "jnxMbgSgwIfBrResCmdTx": jnxMbgSgwIfBrResCmdTx,
       "jnxMbgSgwIfBrResFlrIndRx": jnxMbgSgwIfBrResFlrIndRx,
       "jnxMbgSgwIfBrResFlrIndTx": jnxMbgSgwIfBrResFlrIndTx,
       "jnxMbgSgwIfRelAcsBrReqRx": jnxMbgSgwIfRelAcsBrReqRx,
       "jnxMbgSgwIfRelAcsBrReqTx": jnxMbgSgwIfRelAcsBrReqTx,
       "jnxMbgSgwIfRelAcsBrRespRx": jnxMbgSgwIfRelAcsBrRespRx,
       "jnxMbgSgwIfRelAcsBrRespTx": jnxMbgSgwIfRelAcsBrRespTx,
       "jnxMbgSgwIfCrIndTunReqRx": jnxMbgSgwIfCrIndTunReqRx,
       "jnxMbgSgwIfCrIndTunReqTx": jnxMbgSgwIfCrIndTunReqTx,
       "jnxMbgSgwIfCrIndTunRespRx": jnxMbgSgwIfCrIndTunRespRx,
       "jnxMbgSgwIfCrIndTunRespTx": jnxMbgSgwIfCrIndTunRespTx,
       "jnxMbgSgwIfDelIndTunReqRx": jnxMbgSgwIfDelIndTunReqRx,
       "jnxMbgSgwIfDelIndTunReqTx": jnxMbgSgwIfDelIndTunReqTx,
       "jnxMbgSgwIfDelIndTunRespRx": jnxMbgSgwIfDelIndTunRespRx,
       "jnxMbgSgwIfDelIndTunRespTx": jnxMbgSgwIfDelIndTunRespTx,
       "jnxMbgSgwIfDlDataNotifRx": jnxMbgSgwIfDlDataNotifRx,
       "jnxMbgSgwIfDlDataNotifTx": jnxMbgSgwIfDlDataNotifTx,
       "jnxMbgSgwIfDlDataAckRx": jnxMbgSgwIfDlDataAckRx,
       "jnxMbgSgwIfDlDataAckTx": jnxMbgSgwIfDlDataAckTx,
       "jnxMbgSgwIfDlDataNotiFlrIndRx": jnxMbgSgwIfDlDataNotiFlrIndRx,
       "jnxMbgSgwIfDlDataNotiFlrIndTx": jnxMbgSgwIfDlDataNotiFlrIndTx,
       "jnxMbgSgwIfStopPagingIndRx": jnxMbgSgwIfStopPagingIndRx,
       "jnxMbgSgwIfStopPagingIndTx": jnxMbgSgwIfStopPagingIndTx,
       "jnxMbgSgwIfGtpV2ICsReqAcceptRx": jnxMbgSgwIfGtpV2ICsReqAcceptRx,
       "jnxMbgSgwIfGtpV2ICsReqAcceptTx": jnxMbgSgwIfGtpV2ICsReqAcceptTx,
       "jnxMbgSgwIfGtpV2ICsAcceptPartRx": jnxMbgSgwIfGtpV2ICsAcceptPartRx,
       "jnxMbgSgwIfGtpV2ICsAcceptPartTx": jnxMbgSgwIfGtpV2ICsAcceptPartTx,
       "jnxMbgSgwIfGtpV2ICsNewPTNPrefRx": jnxMbgSgwIfGtpV2ICsNewPTNPrefRx,
       "jnxMbgSgwIfGtpV2ICsNewPTNPrefTx": jnxMbgSgwIfGtpV2ICsNewPTNPrefTx,
       "jnxMbgSgwIfGtpV2ICsNPTSIAdbrRx": jnxMbgSgwIfGtpV2ICsNPTSIAdbrRx,
       "jnxMbgSgwIfGtpV2ICsNPTSIAdbrTx": jnxMbgSgwIfGtpV2ICsNPTSIAdbrTx,
       "jnxMbgSgwIfGtpV2ICsCtxNotFndRx": jnxMbgSgwIfGtpV2ICsCtxNotFndRx,
       "jnxMbgSgwIfGtpV2ICsCtxNotFndTx": jnxMbgSgwIfGtpV2ICsCtxNotFndTx,
       "jnxMbgSgwIfGtpV2ICsInvMsgFmtRx": jnxMbgSgwIfGtpV2ICsInvMsgFmtRx,
       "jnxMbgSgwIfGtpV2ICsInvMsgFmtTx": jnxMbgSgwIfGtpV2ICsInvMsgFmtTx,
       "jnxMbgSgwIfGtpV2ICsVerNotSuppRx": jnxMbgSgwIfGtpV2ICsVerNotSuppRx,
       "jnxMbgSgwIfGtpV2ICsVerNotSuppTx": jnxMbgSgwIfGtpV2ICsVerNotSuppTx,
       "jnxMbgSgwIfGtpV2ICsInvLenRx": jnxMbgSgwIfGtpV2ICsInvLenRx,
       "jnxMbgSgwIfGtpV2ICsInvLenTx": jnxMbgSgwIfGtpV2ICsInvLenTx,
       "jnxMbgSgwIfGtpV2ICsSrvNotSuppRx": jnxMbgSgwIfGtpV2ICsSrvNotSuppRx,
       "jnxMbgSgwIfGtpV2ICsSrvNotSuppTx": jnxMbgSgwIfGtpV2ICsSrvNotSuppTx,
       "jnxMbgSgwIfGtpV2ICsManIEIncorRx": jnxMbgSgwIfGtpV2ICsManIEIncorRx,
       "jnxMbgSgwIfGtpV2ICsManIEIncorTx": jnxMbgSgwIfGtpV2ICsManIEIncorTx,
       "jnxMbgSgwIfGtpV2ICsManIEMissRx": jnxMbgSgwIfGtpV2ICsManIEMissRx,
       "jnxMbgSgwIfGtpV2ICsManIEMissTx": jnxMbgSgwIfGtpV2ICsManIEMissTx,
       "jnxMbgSgwIfGtpV2ICsOptIEIncorRx": jnxMbgSgwIfGtpV2ICsOptIEIncorRx,
       "jnxMbgSgwIfGtpV2ICsOptIEIncorTx": jnxMbgSgwIfGtpV2ICsOptIEIncorTx,
       "jnxMbgSgwIfGtpV2ICsSysFailRx": jnxMbgSgwIfGtpV2ICsSysFailRx,
       "jnxMbgSgwIfGtpV2ICsSysFailTx": jnxMbgSgwIfGtpV2ICsSysFailTx,
       "jnxMbgSgwIfGtpV2ICsNoResRx": jnxMbgSgwIfGtpV2ICsNoResRx,
       "jnxMbgSgwIfGtpV2ICsNoResTx": jnxMbgSgwIfGtpV2ICsNoResTx,
       "jnxMbgSgwIfGtpV2ICsTFTSMANTErRx": jnxMbgSgwIfGtpV2ICsTFTSMANTErRx,
       "jnxMbgSgwIfGtpV2ICsTFTSMANTErTx": jnxMbgSgwIfGtpV2ICsTFTSMANTErTx,
       "jnxMbgSgwIfGtpV2ICsTFTSysErrRx": jnxMbgSgwIfGtpV2ICsTFTSysErrRx,
       "jnxMbgSgwIfGtpV2ICsTFTSysErrTx": jnxMbgSgwIfGtpV2ICsTFTSysErrTx,
       "jnxMbgSgwIfGtpV2ICsPkFltManErRx": jnxMbgSgwIfGtpV2ICsPkFltManErRx,
       "jnxMbgSgwIfGtpV2ICsPkFltManErTx": jnxMbgSgwIfGtpV2ICsPkFltManErTx,
       "jnxMbgSgwIfGtpV2ICsPkFltSynErRx": jnxMbgSgwIfGtpV2ICsPkFltSynErRx,
       "jnxMbgSgwIfGtpV2ICsPkFltSynErTx": jnxMbgSgwIfGtpV2ICsPkFltSynErTx,
       "jnxMbgSgwIfGtpV2ICsMisUnknAPNRx": jnxMbgSgwIfGtpV2ICsMisUnknAPNRx,
       "jnxMbgSgwIfGtpV2ICsMisUnknAPNTx": jnxMbgSgwIfGtpV2ICsMisUnknAPNTx,
       "jnxMbgSgwIfGtpV2ICsUnexpRptIERx": jnxMbgSgwIfGtpV2ICsUnexpRptIERx,
       "jnxMbgSgwIfGtpV2ICsUnexpRptIETx": jnxMbgSgwIfGtpV2ICsUnexpRptIETx,
       "jnxMbgSgwIfGtpV2ICsGREKeyNtFdRx": jnxMbgSgwIfGtpV2ICsGREKeyNtFdRx,
       "jnxMbgSgwIfGtpV2ICsGREKeyNtFdTx": jnxMbgSgwIfGtpV2ICsGREKeyNtFdTx,
       "jnxMbgSgwIfGtpV2ICsRelocFailRx": jnxMbgSgwIfGtpV2ICsRelocFailRx,
       "jnxMbgSgwIfGtpV2ICsRelocFailTx": jnxMbgSgwIfGtpV2ICsRelocFailTx,
       "jnxMbgSgwIfGtpV2ICsDenINRatRx": jnxMbgSgwIfGtpV2ICsDenINRatRx,
       "jnxMbgSgwIfGtpV2ICsDenINRatTx": jnxMbgSgwIfGtpV2ICsDenINRatTx,
       "jnxMbgSgwIfGtpV2ICsPTNotSuppRx": jnxMbgSgwIfGtpV2ICsPTNotSuppRx,
       "jnxMbgSgwIfGtpV2ICsPTNotSuppTx": jnxMbgSgwIfGtpV2ICsPTNotSuppTx,
       "jnxMbgSgwIfGtpV2ICsAlDynAdOccRx": jnxMbgSgwIfGtpV2ICsAlDynAdOccRx,
       "jnxMbgSgwIfGtpV2ICsAlDynAdOccTx": jnxMbgSgwIfGtpV2ICsAlDynAdOccTx,
       "jnxMbgSgwIfGtpV2ICsNOTFTUECTXRx": jnxMbgSgwIfGtpV2ICsNOTFTUECTXRx,
       "jnxMbgSgwIfGtpV2ICsNOTFTUECTXTx": jnxMbgSgwIfGtpV2ICsNOTFTUECTXTx,
       "jnxMbgSgwIfGtpV2ICsProtoNtSupRx": jnxMbgSgwIfGtpV2ICsProtoNtSupRx,
       "jnxMbgSgwIfGtpV2ICsProtoNtSupTx": jnxMbgSgwIfGtpV2ICsProtoNtSupTx,
       "jnxMbgSgwIfGtpV2ICsUENotRespRx": jnxMbgSgwIfGtpV2ICsUENotRespRx,
       "jnxMbgSgwIfGtpV2ICsUENotRespTx": jnxMbgSgwIfGtpV2ICsUENotRespTx,
       "jnxMbgSgwIfGtpV2ICsUERefusesRx": jnxMbgSgwIfGtpV2ICsUERefusesRx,
       "jnxMbgSgwIfGtpV2ICsUERefusesTx": jnxMbgSgwIfGtpV2ICsUERefusesTx,
       "jnxMbgSgwIfGtpV2ICsServDeniedRx": jnxMbgSgwIfGtpV2ICsServDeniedRx,
       "jnxMbgSgwIfGtpV2ICsServDeniedTx": jnxMbgSgwIfGtpV2ICsServDeniedTx,
       "jnxMbgSgwIfGtpV2ICsUnabPageUERx": jnxMbgSgwIfGtpV2ICsUnabPageUERx,
       "jnxMbgSgwIfGtpV2ICsUnabPageUETx": jnxMbgSgwIfGtpV2ICsUnabPageUETx,
       "jnxMbgSgwIfGtpV2ICsNoMemRx": jnxMbgSgwIfGtpV2ICsNoMemRx,
       "jnxMbgSgwIfGtpV2ICsNoMemTx": jnxMbgSgwIfGtpV2ICsNoMemTx,
       "jnxMbgSgwIfGtpV2ICsUserAUTHFlRx": jnxMbgSgwIfGtpV2ICsUserAUTHFlRx,
       "jnxMbgSgwIfGtpV2ICsUserAUTHFlTx": jnxMbgSgwIfGtpV2ICsUserAUTHFlTx,
       "jnxMbgSgwIfGtpV2ICsAPNAcsDenRx": jnxMbgSgwIfGtpV2ICsAPNAcsDenRx,
       "jnxMbgSgwIfGtpV2ICsAPNAcsDenTx": jnxMbgSgwIfGtpV2ICsAPNAcsDenTx,
       "jnxMbgSgwIfGtpV2ICsReqRejRx": jnxMbgSgwIfGtpV2ICsReqRejRx,
       "jnxMbgSgwIfGtpV2ICsReqRejTx": jnxMbgSgwIfGtpV2ICsReqRejTx,
       "jnxMbgSgwIfGtpV2ICsPTMSISigMMRx": jnxMbgSgwIfGtpV2ICsPTMSISigMMRx,
       "jnxMbgSgwIfGtpV2ICsPTMSISigMMTx": jnxMbgSgwIfGtpV2ICsPTMSISigMMTx,
       "jnxMbgSgwIfGtpV2ICsIMSINotKnRx": jnxMbgSgwIfGtpV2ICsIMSINotKnRx,
       "jnxMbgSgwIfGtpV2ICsIMSINotKnTx": jnxMbgSgwIfGtpV2ICsIMSINotKnTx,
       "jnxMbgSgwIfGtpV2ICsCondIEMsRx": jnxMbgSgwIfGtpV2ICsCondIEMsRx,
       "jnxMbgSgwIfGtpV2ICsCondIEMsTx": jnxMbgSgwIfGtpV2ICsCondIEMsTx,
       "jnxMbgSgwIfGtpV2ICsAPNResTIncRx": jnxMbgSgwIfGtpV2ICsAPNResTIncRx,
       "jnxMbgSgwIfGtpV2ICsAPNResTIncTx": jnxMbgSgwIfGtpV2ICsAPNResTIncTx,
       "jnxMbgSgwIfGtpV2ICsUnknownRx": jnxMbgSgwIfGtpV2ICsUnknownRx,
       "jnxMbgSgwIfGtpV2ICsUnknownTx": jnxMbgSgwIfGtpV2ICsUnknownTx,
       "jnxMbgSgwIfGtpV2ICsLclDetRx": jnxMbgSgwIfGtpV2ICsLclDetRx,
       "jnxMbgSgwIfGtpV2ICsLclDetTx": jnxMbgSgwIfGtpV2ICsLclDetTx,
       "jnxMbgSgwIfGtpV2ICsCmpDetRx": jnxMbgSgwIfGtpV2ICsCmpDetRx,
       "jnxMbgSgwIfGtpV2ICsCmpDetTx": jnxMbgSgwIfGtpV2ICsCmpDetTx,
       "jnxMbgSgwIfGtpV2ICsRATChgRx": jnxMbgSgwIfGtpV2ICsRATChgRx,
       "jnxMbgSgwIfGtpV2ICsRATChgTx": jnxMbgSgwIfGtpV2ICsRATChgTx,
       "jnxMbgSgwIfGtpV2ICsISRDeactRx": jnxMbgSgwIfGtpV2ICsISRDeactRx,
       "jnxMbgSgwIfGtpV2ICsISRDeactTx": jnxMbgSgwIfGtpV2ICsISRDeactTx,
       "jnxMbgSgwIfGtpV2ICsEIFRNCEnRx": jnxMbgSgwIfGtpV2ICsEIFRNCEnRx,
       "jnxMbgSgwIfGtpV2ICsEIFRNCEnTx": jnxMbgSgwIfGtpV2ICsEIFRNCEnTx,
       "jnxMbgSgwIfGtpV2ICsSemErTADRx": jnxMbgSgwIfGtpV2ICsSemErTADRx,
       "jnxMbgSgwIfGtpV2ICsSemErTADTx": jnxMbgSgwIfGtpV2ICsSemErTADTx,
       "jnxMbgSgwIfGtpV2ICsSynErTADRx": jnxMbgSgwIfGtpV2ICsSynErTADRx,
       "jnxMbgSgwIfGtpV2ICsSynErTADTx": jnxMbgSgwIfGtpV2ICsSynErTADTx,
       "jnxMbgSgwIfGtpV2ICsRMValRcvRx": jnxMbgSgwIfGtpV2ICsRMValRcvRx,
       "jnxMbgSgwIfGtpV2ICsRMValRcvTx": jnxMbgSgwIfGtpV2ICsRMValRcvTx,
       "jnxMbgSgwIfGtpV2ICsRPrNtRspRx": jnxMbgSgwIfGtpV2ICsRPrNtRspRx,
       "jnxMbgSgwIfGtpV2ICsRPrNtRspTx": jnxMbgSgwIfGtpV2ICsRPrNtRspTx,
       "jnxMbgSgwIfGtpV2ICsColNWReqRx": jnxMbgSgwIfGtpV2ICsColNWReqRx,
       "jnxMbgSgwIfGtpV2ICsColNWReqTx": jnxMbgSgwIfGtpV2ICsColNWReqTx,
       "jnxMbgSgwIfGtpV2ICsUnPgUESusRx": jnxMbgSgwIfGtpV2ICsUnPgUESusRx,
       "jnxMbgSgwIfGtpV2ICsUnPgUESusTx": jnxMbgSgwIfGtpV2ICsUnPgUESusTx,
       "jnxMbgSgwIfGtpV2ICsInvTotLenRx": jnxMbgSgwIfGtpV2ICsInvTotLenRx,
       "jnxMbgSgwIfGtpV2ICsInvTotLenTx": jnxMbgSgwIfGtpV2ICsInvTotLenTx,
       "jnxMbgSgwIfGtpV2ICsDtForNtSupRx": jnxMbgSgwIfGtpV2ICsDtForNtSupRx,
       "jnxMbgSgwIfGtpV2ICsDtForNtSupTx": jnxMbgSgwIfGtpV2ICsDtForNtSupTx,
       "jnxMbgSgwIfGtpV2ICsInReFRePrRx": jnxMbgSgwIfGtpV2ICsInReFRePrRx,
       "jnxMbgSgwIfGtpV2ICsInReFRePrTx": jnxMbgSgwIfGtpV2ICsInReFRePrTx,
       "jnxMbgSgwIfGtpV2ICsInvPrRx": jnxMbgSgwIfGtpV2ICsInvPrRx,
       "jnxMbgSgwIfGtpV2ICsInvPrTx": jnxMbgSgwIfGtpV2ICsInvPrTx,
       "jnxMbgSgwIfGtpV1ProtocolErrRx": jnxMbgSgwIfGtpV1ProtocolErrRx,
       "jnxMbgSgwIfGtpV1UnSupMsgRx": jnxMbgSgwIfGtpV1UnSupMsgRx,
       "jnxMbgSgwIfGtpV1T3RespTmrExpRx": jnxMbgSgwIfGtpV1T3RespTmrExpRx,
       "jnxMbgSgwIfGtpV1EndMarkerRx": jnxMbgSgwIfGtpV1EndMarkerRx,
       "jnxMbgSgwIfGtpV1EndMarkerTx": jnxMbgSgwIfGtpV1EndMarkerTx,
       "jnxMbgSgwIfGtpV1EchoReqRx": jnxMbgSgwIfGtpV1EchoReqRx,
       "jnxMbgSgwIfGtpV1EchoReqTx": jnxMbgSgwIfGtpV1EchoReqTx,
       "jnxMbgSgwIfGtpV1EchoRespRx": jnxMbgSgwIfGtpV1EchoRespRx,
       "jnxMbgSgwIfGtpV1EchoRespTx": jnxMbgSgwIfGtpV1EchoRespTx,
       "jnxMbgSgwIfGtpV1ErrIndRx": jnxMbgSgwIfGtpV1ErrIndRx,
       "jnxMbgSgwIfGtpV1ErrIndTx": jnxMbgSgwIfGtpV1ErrIndTx,
       "jnxMbgSgwIfSuspNotifRx": jnxMbgSgwIfSuspNotifRx,
       "jnxMbgSgwIfSuspNotifTx": jnxMbgSgwIfSuspNotifTx,
       "jnxMbgSgwIfSuspAckRx": jnxMbgSgwIfSuspAckRx,
       "jnxMbgSgwIfSuspAckTx": jnxMbgSgwIfSuspAckTx,
       "jnxMbgSgwIfResumeNotifRx": jnxMbgSgwIfResumeNotifRx,
       "jnxMbgSgwIfResumeNotifTx": jnxMbgSgwIfResumeNotifTx,
       "jnxMbgSgwIfResumeAckRx": jnxMbgSgwIfResumeAckRx,
       "jnxMbgSgwIfResumeAckTx": jnxMbgSgwIfResumeAckTx,
       "jnxMbgSgwIfPiggybackMsgRx": jnxMbgSgwIfPiggybackMsgRx,
       "jnxMbgSgwIfPiggybackMsgTx": jnxMbgSgwIfPiggybackMsgTx}
)
