# SNMP MIB module (JNX-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:39 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(jnxL2tpMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxL2tpMibRoot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxL2tp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1)
)
jnxL2tp.setRevisions(
        ("2007-01-11 00:00",
         "2012-06-08 00:00",
         "2013-09-19 00:00",
         "2013-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxL2tpObjects_ObjectIdentity = ObjectIdentity
jnxL2tpObjects = _JnxL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1)
)
_JnxL2tpScalar_ObjectIdentity = ObjectIdentity
jnxL2tpScalar = _JnxL2tpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1)
)
_JnxL2tpStats_ObjectIdentity = ObjectIdentity
jnxL2tpStats = _JnxL2tpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1)
)
_JnxL2tpStatsTotalTunnels_Type = Gauge32
_JnxL2tpStatsTotalTunnels_Object = MibScalar
jnxL2tpStatsTotalTunnels = _JnxL2tpStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 1),
    _JnxL2tpStatsTotalTunnels_Type()
)
jnxL2tpStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsTotalTunnels.setStatus("current")
_JnxL2tpStatsTotalSessions_Type = Gauge32
_JnxL2tpStatsTotalSessions_Object = MibScalar
jnxL2tpStatsTotalSessions = _JnxL2tpStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 2),
    _JnxL2tpStatsTotalSessions_Type()
)
jnxL2tpStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsTotalSessions.setStatus("current")
_JnxL2tpStatsControlRxOctets_Type = Gauge32
_JnxL2tpStatsControlRxOctets_Object = MibScalar
jnxL2tpStatsControlRxOctets = _JnxL2tpStatsControlRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 3),
    _JnxL2tpStatsControlRxOctets_Type()
)
jnxL2tpStatsControlRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsControlRxOctets.setStatus("current")
_JnxL2tpStatsControlRxPkts_Type = Gauge32
_JnxL2tpStatsControlRxPkts_Object = MibScalar
jnxL2tpStatsControlRxPkts = _JnxL2tpStatsControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 4),
    _JnxL2tpStatsControlRxPkts_Type()
)
jnxL2tpStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsControlRxPkts.setStatus("current")
_JnxL2tpStatsControlTxOctets_Type = Gauge32
_JnxL2tpStatsControlTxOctets_Object = MibScalar
jnxL2tpStatsControlTxOctets = _JnxL2tpStatsControlTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 5),
    _JnxL2tpStatsControlTxOctets_Type()
)
jnxL2tpStatsControlTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsControlTxOctets.setStatus("current")
_JnxL2tpStatsControlTxPkts_Type = Gauge32
_JnxL2tpStatsControlTxPkts_Object = MibScalar
jnxL2tpStatsControlTxPkts = _JnxL2tpStatsControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 6),
    _JnxL2tpStatsControlTxPkts_Type()
)
jnxL2tpStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsControlTxPkts.setStatus("current")
_JnxL2tpStatsPayloadRxOctets_Type = Gauge32
_JnxL2tpStatsPayloadRxOctets_Object = MibScalar
jnxL2tpStatsPayloadRxOctets = _JnxL2tpStatsPayloadRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 7),
    _JnxL2tpStatsPayloadRxOctets_Type()
)
jnxL2tpStatsPayloadRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsPayloadRxOctets.setStatus("deprecated")
_JnxL2tpStatsPayloadRxPkts_Type = CounterBasedGauge64
_JnxL2tpStatsPayloadRxPkts_Object = MibScalar
jnxL2tpStatsPayloadRxPkts = _JnxL2tpStatsPayloadRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 8),
    _JnxL2tpStatsPayloadRxPkts_Type()
)
jnxL2tpStatsPayloadRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsPayloadRxPkts.setStatus("current")
_JnxL2tpStatsPayloadTxOctets_Type = CounterBasedGauge64
_JnxL2tpStatsPayloadTxOctets_Object = MibScalar
jnxL2tpStatsPayloadTxOctets = _JnxL2tpStatsPayloadTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 9),
    _JnxL2tpStatsPayloadTxOctets_Type()
)
jnxL2tpStatsPayloadTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsPayloadTxOctets.setStatus("current")
_JnxL2tpStatsPayloadTxPkts_Type = CounterBasedGauge64
_JnxL2tpStatsPayloadTxPkts_Object = MibScalar
jnxL2tpStatsPayloadTxPkts = _JnxL2tpStatsPayloadTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 10),
    _JnxL2tpStatsPayloadTxPkts_Type()
)
jnxL2tpStatsPayloadTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsPayloadTxPkts.setStatus("current")
_JnxL2tpStatsErrorTxPkts_Type = CounterBasedGauge64
_JnxL2tpStatsErrorTxPkts_Object = MibScalar
jnxL2tpStatsErrorTxPkts = _JnxL2tpStatsErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 11),
    _JnxL2tpStatsErrorTxPkts_Type()
)
jnxL2tpStatsErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsErrorTxPkts.setStatus("current")
_JnxL2tpStatsErrorRxPkts_Type = CounterBasedGauge64
_JnxL2tpStatsErrorRxPkts_Object = MibScalar
jnxL2tpStatsErrorRxPkts = _JnxL2tpStatsErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 12),
    _JnxL2tpStatsErrorRxPkts_Type()
)
jnxL2tpStatsErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsErrorRxPkts.setStatus("current")
_JnxL2tpStatsPayloadRxOctets64_Type = CounterBasedGauge64
_JnxL2tpStatsPayloadRxOctets64_Object = MibScalar
jnxL2tpStatsPayloadRxOctets64 = _JnxL2tpStatsPayloadRxOctets64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 1, 1, 13),
    _JnxL2tpStatsPayloadRxOctets64_Type()
)
jnxL2tpStatsPayloadRxOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpStatsPayloadRxOctets64.setStatus("current")
_JnxL2tpTunnelGroupStatsTable_Object = MibTable
jnxL2tpTunnelGroupStatsTable = _JnxL2tpTunnelGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsTable.setStatus("current")
_JnxL2tpTunnelGroupStatsEntry_Object = MibTableRow
jnxL2tpTunnelGroupStatsEntry = _JnxL2tpTunnelGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1)
)
jnxL2tpTunnelGroupStatsEntry.setIndexNames(
    (1, "JNX-L2TP-MIB", "jnxL2tpTunnelGroupStatsTnlGrpName"),
)
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsEntry.setStatus("current")


class _JnxL2tpTunnelGroupStatsTnlGrpName_Type(OctetString):
    """Custom type jnxL2tpTunnelGroupStatsTnlGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JnxL2tpTunnelGroupStatsTnlGrpName_Type.__name__ = "OctetString"
_JnxL2tpTunnelGroupStatsTnlGrpName_Object = MibTableColumn
jnxL2tpTunnelGroupStatsTnlGrpName = _JnxL2tpTunnelGroupStatsTnlGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 1),
    _JnxL2tpTunnelGroupStatsTnlGrpName_Type()
)
jnxL2tpTunnelGroupStatsTnlGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsTnlGrpName.setStatus("current")
_JnxL2tpTunnelGroupStatsGatewayAddrType_Type = InetAddressType
_JnxL2tpTunnelGroupStatsGatewayAddrType_Object = MibTableColumn
jnxL2tpTunnelGroupStatsGatewayAddrType = _JnxL2tpTunnelGroupStatsGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 2),
    _JnxL2tpTunnelGroupStatsGatewayAddrType_Type()
)
jnxL2tpTunnelGroupStatsGatewayAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsGatewayAddrType.setStatus("current")
_JnxL2tpTunnelGroupStatsGatewayAddr_Type = InetAddress
_JnxL2tpTunnelGroupStatsGatewayAddr_Object = MibTableColumn
jnxL2tpTunnelGroupStatsGatewayAddr = _JnxL2tpTunnelGroupStatsGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 3),
    _JnxL2tpTunnelGroupStatsGatewayAddr_Type()
)
jnxL2tpTunnelGroupStatsGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsGatewayAddr.setStatus("current")
_JnxL2tpTunnelGroupStatsSvcIntfName_Type = SnmpAdminString
_JnxL2tpTunnelGroupStatsSvcIntfName_Object = MibTableColumn
jnxL2tpTunnelGroupStatsSvcIntfName = _JnxL2tpTunnelGroupStatsSvcIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 4),
    _JnxL2tpTunnelGroupStatsSvcIntfName_Type()
)
jnxL2tpTunnelGroupStatsSvcIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsSvcIntfName.setStatus("current")
_JnxL2tpTunnelGroupStatsTotalTunnels_Type = Gauge32
_JnxL2tpTunnelGroupStatsTotalTunnels_Object = MibTableColumn
jnxL2tpTunnelGroupStatsTotalTunnels = _JnxL2tpTunnelGroupStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 5),
    _JnxL2tpTunnelGroupStatsTotalTunnels_Type()
)
jnxL2tpTunnelGroupStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsTotalTunnels.setStatus("current")
_JnxL2tpTunnelGroupStatsTotalSessions_Type = Gauge32
_JnxL2tpTunnelGroupStatsTotalSessions_Object = MibTableColumn
jnxL2tpTunnelGroupStatsTotalSessions = _JnxL2tpTunnelGroupStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 2, 1, 6),
    _JnxL2tpTunnelGroupStatsTotalSessions_Type()
)
jnxL2tpTunnelGroupStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelGroupStatsTotalSessions.setStatus("current")
_JnxL2tpTunnelStatsTable_Object = MibTable
jnxL2tpTunnelStatsTable = _JnxL2tpTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsTable.setStatus("current")
_JnxL2tpTunnelStatsEntry_Object = MibTableRow
jnxL2tpTunnelStatsEntry = _JnxL2tpTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1)
)
jnxL2tpTunnelStatsEntry.setIndexNames(
    (0, "JNX-L2TP-MIB", "jnxL2tpTunnelStatsLocalTID"),
)
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsEntry.setStatus("current")


class _JnxL2tpTunnelStatsLocalTID_Type(Integer32):
    """Custom type jnxL2tpTunnelStatsLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpTunnelStatsLocalTID_Type.__name__ = "Integer32"
_JnxL2tpTunnelStatsLocalTID_Object = MibTableColumn
jnxL2tpTunnelStatsLocalTID = _JnxL2tpTunnelStatsLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 1),
    _JnxL2tpTunnelStatsLocalTID_Type()
)
jnxL2tpTunnelStatsLocalTID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsLocalTID.setStatus("current")
_JnxL2tpTunnelStatsServiceInterface_Type = SnmpAdminString
_JnxL2tpTunnelStatsServiceInterface_Object = MibTableColumn
jnxL2tpTunnelStatsServiceInterface = _JnxL2tpTunnelStatsServiceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 2),
    _JnxL2tpTunnelStatsServiceInterface_Type()
)
jnxL2tpTunnelStatsServiceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsServiceInterface.setStatus("current")
_JnxL2tpTunnelStatsTunnelGroup_Type = SnmpAdminString
_JnxL2tpTunnelStatsTunnelGroup_Object = MibTableColumn
jnxL2tpTunnelStatsTunnelGroup = _JnxL2tpTunnelStatsTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 3),
    _JnxL2tpTunnelStatsTunnelGroup_Type()
)
jnxL2tpTunnelStatsTunnelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsTunnelGroup.setStatus("current")


class _JnxL2tpTunnelStatsRemoteTID_Type(Integer32):
    """Custom type jnxL2tpTunnelStatsRemoteTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpTunnelStatsRemoteTID_Type.__name__ = "Integer32"
_JnxL2tpTunnelStatsRemoteTID_Object = MibTableColumn
jnxL2tpTunnelStatsRemoteTID = _JnxL2tpTunnelStatsRemoteTID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 4),
    _JnxL2tpTunnelStatsRemoteTID_Type()
)
jnxL2tpTunnelStatsRemoteTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsRemoteTID.setStatus("current")
_JnxL2tpTunnelStatsRemoteIpAddrType_Type = InetAddressType
_JnxL2tpTunnelStatsRemoteIpAddrType_Object = MibTableColumn
jnxL2tpTunnelStatsRemoteIpAddrType = _JnxL2tpTunnelStatsRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 5),
    _JnxL2tpTunnelStatsRemoteIpAddrType_Type()
)
jnxL2tpTunnelStatsRemoteIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsRemoteIpAddrType.setStatus("current")
_JnxL2tpTunnelStatsRemoteIpAddress_Type = InetAddress
_JnxL2tpTunnelStatsRemoteIpAddress_Object = MibTableColumn
jnxL2tpTunnelStatsRemoteIpAddress = _JnxL2tpTunnelStatsRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 6),
    _JnxL2tpTunnelStatsRemoteIpAddress_Type()
)
jnxL2tpTunnelStatsRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsRemoteIpAddress.setStatus("current")
_JnxL2tpTunnelStatsRemoteUdpPort_Type = InetPortNumber
_JnxL2tpTunnelStatsRemoteUdpPort_Object = MibTableColumn
jnxL2tpTunnelStatsRemoteUdpPort = _JnxL2tpTunnelStatsRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 7),
    _JnxL2tpTunnelStatsRemoteUdpPort_Type()
)
jnxL2tpTunnelStatsRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsRemoteUdpPort.setStatus("current")
_JnxL2tpTunnelStatsActiveSessions_Type = Gauge32
_JnxL2tpTunnelStatsActiveSessions_Object = MibTableColumn
jnxL2tpTunnelStatsActiveSessions = _JnxL2tpTunnelStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 8),
    _JnxL2tpTunnelStatsActiveSessions_Type()
)
jnxL2tpTunnelStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsActiveSessions.setStatus("current")


class _JnxL2tpTunnelStatsState_Type(Integer32):
    """Custom type jnxL2tpTunnelStatsState based on Integer32"""
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
        *(("cc-responder-accept-new", 1),
          ("cc-responder-idle", 3),
          ("cc-responder-reject-new", 2),
          ("cc-responder-wait-ctl-conn", 4),
          ("cleanup", 5),
          ("closed", 6),
          ("destroyed", 7),
          ("established", 8),
          ("terminate", 9),
          ("unknown", 10))
    )


_JnxL2tpTunnelStatsState_Type.__name__ = "Integer32"
_JnxL2tpTunnelStatsState_Object = MibTableColumn
jnxL2tpTunnelStatsState = _JnxL2tpTunnelStatsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 9),
    _JnxL2tpTunnelStatsState_Type()
)
jnxL2tpTunnelStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsState.setStatus("current")
_JnxL2tpTunnelStatsLocalIpAddrType_Type = InetAddressType
_JnxL2tpTunnelStatsLocalIpAddrType_Object = MibTableColumn
jnxL2tpTunnelStatsLocalIpAddrType = _JnxL2tpTunnelStatsLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 10),
    _JnxL2tpTunnelStatsLocalIpAddrType_Type()
)
jnxL2tpTunnelStatsLocalIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsLocalIpAddrType.setStatus("current")
_JnxL2tpTunnelStatsLocalIpAddress_Type = InetAddress
_JnxL2tpTunnelStatsLocalIpAddress_Object = MibTableColumn
jnxL2tpTunnelStatsLocalIpAddress = _JnxL2tpTunnelStatsLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 11),
    _JnxL2tpTunnelStatsLocalIpAddress_Type()
)
jnxL2tpTunnelStatsLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsLocalIpAddress.setStatus("current")
_JnxL2tpTunnelStatsLocalUdpPort_Type = InetPortNumber
_JnxL2tpTunnelStatsLocalUdpPort_Object = MibTableColumn
jnxL2tpTunnelStatsLocalUdpPort = _JnxL2tpTunnelStatsLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 12),
    _JnxL2tpTunnelStatsLocalUdpPort_Type()
)
jnxL2tpTunnelStatsLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsLocalUdpPort.setStatus("current")
_JnxL2tpTunnelStatsLocalHostName_Type = SnmpAdminString
_JnxL2tpTunnelStatsLocalHostName_Object = MibTableColumn
jnxL2tpTunnelStatsLocalHostName = _JnxL2tpTunnelStatsLocalHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 13),
    _JnxL2tpTunnelStatsLocalHostName_Type()
)
jnxL2tpTunnelStatsLocalHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsLocalHostName.setStatus("current")
_JnxL2tpTunnelStatsRemoteHostName_Type = SnmpAdminString
_JnxL2tpTunnelStatsRemoteHostName_Object = MibTableColumn
jnxL2tpTunnelStatsRemoteHostName = _JnxL2tpTunnelStatsRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 14),
    _JnxL2tpTunnelStatsRemoteHostName_Type()
)
jnxL2tpTunnelStatsRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsRemoteHostName.setStatus("current")
_JnxL2tpTunnelMaxSessions_Type = Integer32
_JnxL2tpTunnelMaxSessions_Object = MibTableColumn
jnxL2tpTunnelMaxSessions = _JnxL2tpTunnelMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 15),
    _JnxL2tpTunnelMaxSessions_Type()
)
jnxL2tpTunnelMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelMaxSessions.setStatus("current")


class _JnxL2tpTunnelStatsWindowSize_Type(Integer32):
    """Custom type jnxL2tpTunnelStatsWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpTunnelStatsWindowSize_Type.__name__ = "Integer32"
_JnxL2tpTunnelStatsWindowSize_Object = MibTableColumn
jnxL2tpTunnelStatsWindowSize = _JnxL2tpTunnelStatsWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 16),
    _JnxL2tpTunnelStatsWindowSize_Type()
)
jnxL2tpTunnelStatsWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsWindowSize.setStatus("current")


class _JnxL2tpTunnelStatsHelloInterval_Type(Integer32):
    """Custom type jnxL2tpTunnelStatsHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpTunnelStatsHelloInterval_Type.__name__ = "Integer32"
_JnxL2tpTunnelStatsHelloInterval_Object = MibTableColumn
jnxL2tpTunnelStatsHelloInterval = _JnxL2tpTunnelStatsHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 17),
    _JnxL2tpTunnelStatsHelloInterval_Type()
)
jnxL2tpTunnelStatsHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsHelloInterval.setStatus("current")
_JnxL2tpTunnelStatsCreationTime_Type = DateAndTime
_JnxL2tpTunnelStatsCreationTime_Object = MibTableColumn
jnxL2tpTunnelStatsCreationTime = _JnxL2tpTunnelStatsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 18),
    _JnxL2tpTunnelStatsCreationTime_Type()
)
jnxL2tpTunnelStatsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsCreationTime.setStatus("current")
_JnxL2tpTunnelStatsUpTime_Type = TimeTicks
_JnxL2tpTunnelStatsUpTime_Object = MibTableColumn
jnxL2tpTunnelStatsUpTime = _JnxL2tpTunnelStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 19),
    _JnxL2tpTunnelStatsUpTime_Type()
)
jnxL2tpTunnelStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsUpTime.setStatus("current")
_JnxL2tpTunnelStatsIdleTime_Type = TimeTicks
_JnxL2tpTunnelStatsIdleTime_Object = MibTableColumn
jnxL2tpTunnelStatsIdleTime = _JnxL2tpTunnelStatsIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 20),
    _JnxL2tpTunnelStatsIdleTime_Type()
)
jnxL2tpTunnelStatsIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsIdleTime.setStatus("current")
_JnxL2tpTunnelStatsCollectionStart_Type = DateAndTime
_JnxL2tpTunnelStatsCollectionStart_Object = MibTableColumn
jnxL2tpTunnelStatsCollectionStart = _JnxL2tpTunnelStatsCollectionStart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 21),
    _JnxL2tpTunnelStatsCollectionStart_Type()
)
jnxL2tpTunnelStatsCollectionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsCollectionStart.setStatus("current")
_JnxL2tpTunnelStatsControlTxPkts_Type = Counter32
_JnxL2tpTunnelStatsControlTxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsControlTxPkts = _JnxL2tpTunnelStatsControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 22),
    _JnxL2tpTunnelStatsControlTxPkts_Type()
)
jnxL2tpTunnelStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlTxPkts.setStatus("current")
_JnxL2tpTunnelStatsControlTxBytes_Type = Counter64
_JnxL2tpTunnelStatsControlTxBytes_Object = MibTableColumn
jnxL2tpTunnelStatsControlTxBytes = _JnxL2tpTunnelStatsControlTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 23),
    _JnxL2tpTunnelStatsControlTxBytes_Type()
)
jnxL2tpTunnelStatsControlTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlTxBytes.setStatus("deprecated")
_JnxL2tpTunnelStatsControlRxPkts_Type = Counter32
_JnxL2tpTunnelStatsControlRxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsControlRxPkts = _JnxL2tpTunnelStatsControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 24),
    _JnxL2tpTunnelStatsControlRxPkts_Type()
)
jnxL2tpTunnelStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlRxPkts.setStatus("current")
_JnxL2tpTunnelStatsControlRxBytes_Type = Counter64
_JnxL2tpTunnelStatsControlRxBytes_Object = MibTableColumn
jnxL2tpTunnelStatsControlRxBytes = _JnxL2tpTunnelStatsControlRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 25),
    _JnxL2tpTunnelStatsControlRxBytes_Type()
)
jnxL2tpTunnelStatsControlRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlRxBytes.setStatus("deprecated")
_JnxL2tpTunnelStatsDataTxPkts_Type = Counter32
_JnxL2tpTunnelStatsDataTxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsDataTxPkts = _JnxL2tpTunnelStatsDataTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 26),
    _JnxL2tpTunnelStatsDataTxPkts_Type()
)
jnxL2tpTunnelStatsDataTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataTxPkts.setStatus("deprecated")
_JnxL2tpTunnelStatsDataTxBytes_Type = Counter64
_JnxL2tpTunnelStatsDataTxBytes_Object = MibTableColumn
jnxL2tpTunnelStatsDataTxBytes = _JnxL2tpTunnelStatsDataTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 27),
    _JnxL2tpTunnelStatsDataTxBytes_Type()
)
jnxL2tpTunnelStatsDataTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataTxBytes.setStatus("current")
_JnxL2tpTunnelStatsDataRxPkts_Type = Counter32
_JnxL2tpTunnelStatsDataRxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsDataRxPkts = _JnxL2tpTunnelStatsDataRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 28),
    _JnxL2tpTunnelStatsDataRxPkts_Type()
)
jnxL2tpTunnelStatsDataRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataRxPkts.setStatus("deprecated")
_JnxL2tpTunnelStatsDataRxBytes_Type = Counter64
_JnxL2tpTunnelStatsDataRxBytes_Object = MibTableColumn
jnxL2tpTunnelStatsDataRxBytes = _JnxL2tpTunnelStatsDataRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 29),
    _JnxL2tpTunnelStatsDataRxBytes_Type()
)
jnxL2tpTunnelStatsDataRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataRxBytes.setStatus("current")
_JnxL2tpTunnelStatsErrorTxPkts_Type = Counter32
_JnxL2tpTunnelStatsErrorTxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsErrorTxPkts = _JnxL2tpTunnelStatsErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 30),
    _JnxL2tpTunnelStatsErrorTxPkts_Type()
)
jnxL2tpTunnelStatsErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsErrorTxPkts.setStatus("current")
_JnxL2tpTunnelStatsErrorRxPkts_Type = Counter32
_JnxL2tpTunnelStatsErrorRxPkts_Object = MibTableColumn
jnxL2tpTunnelStatsErrorRxPkts = _JnxL2tpTunnelStatsErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 31),
    _JnxL2tpTunnelStatsErrorRxPkts_Type()
)
jnxL2tpTunnelStatsErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsErrorRxPkts.setStatus("current")
_JnxL2tpTunnelStatsControlTxBytes32_Type = Counter32
_JnxL2tpTunnelStatsControlTxBytes32_Object = MibTableColumn
jnxL2tpTunnelStatsControlTxBytes32 = _JnxL2tpTunnelStatsControlTxBytes32_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 32),
    _JnxL2tpTunnelStatsControlTxBytes32_Type()
)
jnxL2tpTunnelStatsControlTxBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlTxBytes32.setStatus("current")
_JnxL2tpTunnelStatsControlRxBytes32_Type = Counter32
_JnxL2tpTunnelStatsControlRxBytes32_Object = MibTableColumn
jnxL2tpTunnelStatsControlRxBytes32 = _JnxL2tpTunnelStatsControlRxBytes32_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 33),
    _JnxL2tpTunnelStatsControlRxBytes32_Type()
)
jnxL2tpTunnelStatsControlRxBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsControlRxBytes32.setStatus("current")
_JnxL2tpTunnelStatsDataTxPkts64_Type = Counter64
_JnxL2tpTunnelStatsDataTxPkts64_Object = MibTableColumn
jnxL2tpTunnelStatsDataTxPkts64 = _JnxL2tpTunnelStatsDataTxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 34),
    _JnxL2tpTunnelStatsDataTxPkts64_Type()
)
jnxL2tpTunnelStatsDataTxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataTxPkts64.setStatus("current")
_JnxL2tpTunnelStatsDataRxPkts64_Type = Counter64
_JnxL2tpTunnelStatsDataRxPkts64_Object = MibTableColumn
jnxL2tpTunnelStatsDataRxPkts64 = _JnxL2tpTunnelStatsDataRxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 3, 1, 35),
    _JnxL2tpTunnelStatsDataRxPkts64_Type()
)
jnxL2tpTunnelStatsDataRxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpTunnelStatsDataRxPkts64.setStatus("current")
_JnxL2tpSessionStatsTable_Object = MibTable
jnxL2tpSessionStatsTable = _JnxL2tpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsTable.setStatus("current")
_JnxL2tpSessionStatsEntry_Object = MibTableRow
jnxL2tpSessionStatsEntry = _JnxL2tpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1)
)
jnxL2tpSessionStatsEntry.setIndexNames(
    (0, "JNX-L2TP-MIB", "jnxL2tpSessionStatsLocalTID"),
    (0, "JNX-L2TP-MIB", "jnxL2tpSessionStatsLocalSID"),
)
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsEntry.setStatus("current")


class _JnxL2tpSessionStatsLocalTID_Type(Integer32):
    """Custom type jnxL2tpSessionStatsLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsLocalTID_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsLocalTID_Object = MibTableColumn
jnxL2tpSessionStatsLocalTID = _JnxL2tpSessionStatsLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 1),
    _JnxL2tpSessionStatsLocalTID_Type()
)
jnxL2tpSessionStatsLocalTID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalTID.setStatus("current")


class _JnxL2tpSessionStatsLocalSID_Type(Integer32):
    """Custom type jnxL2tpSessionStatsLocalSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsLocalSID_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsLocalSID_Object = MibTableColumn
jnxL2tpSessionStatsLocalSID = _JnxL2tpSessionStatsLocalSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 2),
    _JnxL2tpSessionStatsLocalSID_Type()
)
jnxL2tpSessionStatsLocalSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalSID.setStatus("current")
_JnxL2tpSessionStatsServiceInterface_Type = SnmpAdminString
_JnxL2tpSessionStatsServiceInterface_Object = MibTableColumn
jnxL2tpSessionStatsServiceInterface = _JnxL2tpSessionStatsServiceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 3),
    _JnxL2tpSessionStatsServiceInterface_Type()
)
jnxL2tpSessionStatsServiceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsServiceInterface.setStatus("current")
_JnxL2tpSessionStatsTunnelGroup_Type = SnmpAdminString
_JnxL2tpSessionStatsTunnelGroup_Object = MibTableColumn
jnxL2tpSessionStatsTunnelGroup = _JnxL2tpSessionStatsTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 4),
    _JnxL2tpSessionStatsTunnelGroup_Type()
)
jnxL2tpSessionStatsTunnelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsTunnelGroup.setStatus("current")


class _JnxL2tpSessionStatsRemoteSID_Type(Integer32):
    """Custom type jnxL2tpSessionStatsRemoteSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsRemoteSID_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsRemoteSID_Object = MibTableColumn
jnxL2tpSessionStatsRemoteSID = _JnxL2tpSessionStatsRemoteSID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 5),
    _JnxL2tpSessionStatsRemoteSID_Type()
)
jnxL2tpSessionStatsRemoteSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRemoteSID.setStatus("current")


class _JnxL2tpSessionStatsInterfaceUnit_Type(Integer32):
    """Custom type jnxL2tpSessionStatsInterfaceUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsInterfaceUnit_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsInterfaceUnit_Object = MibTableColumn
jnxL2tpSessionStatsInterfaceUnit = _JnxL2tpSessionStatsInterfaceUnit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 6),
    _JnxL2tpSessionStatsInterfaceUnit_Type()
)
jnxL2tpSessionStatsInterfaceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsInterfaceUnit.setStatus("current")


class _JnxL2tpSessionStatsEncapType_Type(Integer32):
    """Custom type jnxL2tpSessionStatsEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multilink-ppp", 2),
          ("ppp", 1),
          ("unknown", 3))
    )


_JnxL2tpSessionStatsEncapType_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsEncapType_Object = MibTableColumn
jnxL2tpSessionStatsEncapType = _JnxL2tpSessionStatsEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 7),
    _JnxL2tpSessionStatsEncapType_Type()
)
jnxL2tpSessionStatsEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsEncapType.setStatus("current")


class _JnxL2tpSessionStatsBundleID_Type(Integer32):
    """Custom type jnxL2tpSessionStatsBundleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_JnxL2tpSessionStatsBundleID_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsBundleID_Object = MibTableColumn
jnxL2tpSessionStatsBundleID = _JnxL2tpSessionStatsBundleID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 8),
    _JnxL2tpSessionStatsBundleID_Type()
)
jnxL2tpSessionStatsBundleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsBundleID.setStatus("current")


class _JnxL2tpSessionStatsState_Type(Integer32):
    """Custom type jnxL2tpSessionStatsState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleanup", 4),
          ("closed", 2),
          ("destroyed", 3),
          ("established", 1),
          ("lns-ic-accept-new", 5),
          ("lns-ic-idle", 6),
          ("lns-ic-reject-new", 7),
          ("lns-ic-wait-connect", 8))
    )


_JnxL2tpSessionStatsState_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsState_Object = MibTableColumn
jnxL2tpSessionStatsState = _JnxL2tpSessionStatsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 9),
    _JnxL2tpSessionStatsState_Type()
)
jnxL2tpSessionStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsState.setStatus("current")
_JnxL2tpSessionStatsUserName_Type = SnmpAdminString
_JnxL2tpSessionStatsUserName_Object = MibTableColumn
jnxL2tpSessionStatsUserName = _JnxL2tpSessionStatsUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 10),
    _JnxL2tpSessionStatsUserName_Type()
)
jnxL2tpSessionStatsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsUserName.setStatus("current")


class _JnxL2tpSessionStatsMode_Type(Integer32):
    """Custom type jnxL2tpSessionStatsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicate", 2),
          ("shared", 1),
          ("unknown", 3))
    )


_JnxL2tpSessionStatsMode_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsMode_Object = MibTableColumn
jnxL2tpSessionStatsMode = _JnxL2tpSessionStatsMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 11),
    _JnxL2tpSessionStatsMode_Type()
)
jnxL2tpSessionStatsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsMode.setStatus("current")
_JnxL2tpSessionStatsLocalAddrType_Type = InetAddressType
_JnxL2tpSessionStatsLocalAddrType_Object = MibTableColumn
jnxL2tpSessionStatsLocalAddrType = _JnxL2tpSessionStatsLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 12),
    _JnxL2tpSessionStatsLocalAddrType_Type()
)
jnxL2tpSessionStatsLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalAddrType.setStatus("current")
_JnxL2tpSessionStatsLocalAddress_Type = InetAddress
_JnxL2tpSessionStatsLocalAddress_Object = MibTableColumn
jnxL2tpSessionStatsLocalAddress = _JnxL2tpSessionStatsLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 13),
    _JnxL2tpSessionStatsLocalAddress_Type()
)
jnxL2tpSessionStatsLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalAddress.setStatus("current")
_JnxL2tpSessionStatsLocalUdpPort_Type = InetPortNumber
_JnxL2tpSessionStatsLocalUdpPort_Object = MibTableColumn
jnxL2tpSessionStatsLocalUdpPort = _JnxL2tpSessionStatsLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 14),
    _JnxL2tpSessionStatsLocalUdpPort_Type()
)
jnxL2tpSessionStatsLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalUdpPort.setStatus("current")
_JnxL2tpSessionStatsRemoteAddrType_Type = InetAddressType
_JnxL2tpSessionStatsRemoteAddrType_Object = MibTableColumn
jnxL2tpSessionStatsRemoteAddrType = _JnxL2tpSessionStatsRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 15),
    _JnxL2tpSessionStatsRemoteAddrType_Type()
)
jnxL2tpSessionStatsRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRemoteAddrType.setStatus("current")
_JnxL2tpSessionStatsRemoteAddress_Type = InetAddress
_JnxL2tpSessionStatsRemoteAddress_Object = MibTableColumn
jnxL2tpSessionStatsRemoteAddress = _JnxL2tpSessionStatsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 16),
    _JnxL2tpSessionStatsRemoteAddress_Type()
)
jnxL2tpSessionStatsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRemoteAddress.setStatus("current")
_JnxL2tpSessionStatsRemoteUdpPort_Type = InetPortNumber
_JnxL2tpSessionStatsRemoteUdpPort_Object = MibTableColumn
jnxL2tpSessionStatsRemoteUdpPort = _JnxL2tpSessionStatsRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 17),
    _JnxL2tpSessionStatsRemoteUdpPort_Type()
)
jnxL2tpSessionStatsRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRemoteUdpPort.setStatus("current")
_JnxL2tpSessionStatsLocalHostName_Type = SnmpAdminString
_JnxL2tpSessionStatsLocalHostName_Object = MibTableColumn
jnxL2tpSessionStatsLocalHostName = _JnxL2tpSessionStatsLocalHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 18),
    _JnxL2tpSessionStatsLocalHostName_Type()
)
jnxL2tpSessionStatsLocalHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLocalHostName.setStatus("current")
_JnxL2tpSessionStatsRemoteHostName_Type = SnmpAdminString
_JnxL2tpSessionStatsRemoteHostName_Object = MibTableColumn
jnxL2tpSessionStatsRemoteHostName = _JnxL2tpSessionStatsRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 19),
    _JnxL2tpSessionStatsRemoteHostName_Type()
)
jnxL2tpSessionStatsRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRemoteHostName.setStatus("current")
_JnxL2tpSessionAssignedIpAddrType_Type = InetAddressType
_JnxL2tpSessionAssignedIpAddrType_Object = MibTableColumn
jnxL2tpSessionAssignedIpAddrType = _JnxL2tpSessionAssignedIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 20),
    _JnxL2tpSessionAssignedIpAddrType_Type()
)
jnxL2tpSessionAssignedIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionAssignedIpAddrType.setStatus("current")
_JnxL2tpSessionAssignedIpAddress_Type = InetAddress
_JnxL2tpSessionAssignedIpAddress_Object = MibTableColumn
jnxL2tpSessionAssignedIpAddress = _JnxL2tpSessionAssignedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 21),
    _JnxL2tpSessionAssignedIpAddress_Type()
)
jnxL2tpSessionAssignedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionAssignedIpAddress.setStatus("current")


class _JnxL2tpSessionLocalMRU_Type(Integer32):
    """Custom type jnxL2tpSessionLocalMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxL2tpSessionLocalMRU_Type.__name__ = "Integer32"
_JnxL2tpSessionLocalMRU_Object = MibTableColumn
jnxL2tpSessionLocalMRU = _JnxL2tpSessionLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 22),
    _JnxL2tpSessionLocalMRU_Type()
)
jnxL2tpSessionLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionLocalMRU.setStatus("current")


class _JnxL2tpSessionRemoteMRU_Type(Integer32):
    """Custom type jnxL2tpSessionRemoteMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxL2tpSessionRemoteMRU_Type.__name__ = "Integer32"
_JnxL2tpSessionRemoteMRU_Object = MibTableColumn
jnxL2tpSessionRemoteMRU = _JnxL2tpSessionRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 23),
    _JnxL2tpSessionRemoteMRU_Type()
)
jnxL2tpSessionRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionRemoteMRU.setStatus("current")
_JnxL2tpSessionStatsTxSpeed_Type = Unsigned32
_JnxL2tpSessionStatsTxSpeed_Object = MibTableColumn
jnxL2tpSessionStatsTxSpeed = _JnxL2tpSessionStatsTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 24),
    _JnxL2tpSessionStatsTxSpeed_Type()
)
jnxL2tpSessionStatsTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsTxSpeed.setUnits("bits per second")
_JnxL2tpSessionStatsRxSpeed_Type = Unsigned32
_JnxL2tpSessionStatsRxSpeed_Object = MibTableColumn
jnxL2tpSessionStatsRxSpeed = _JnxL2tpSessionStatsRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 25),
    _JnxL2tpSessionStatsRxSpeed_Type()
)
jnxL2tpSessionStatsRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsRxSpeed.setUnits("bits per second")


class _JnxL2tpSessionStatsCallBearerType_Type(Integer32):
    """Custom type jnxL2tpSessionStatsCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("digital", 2),
          ("none", 1))
    )


_JnxL2tpSessionStatsCallBearerType_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsCallBearerType_Object = MibTableColumn
jnxL2tpSessionStatsCallBearerType = _JnxL2tpSessionStatsCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 26),
    _JnxL2tpSessionStatsCallBearerType_Type()
)
jnxL2tpSessionStatsCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCallBearerType.setStatus("current")


class _JnxL2tpSessionStatsFramingType_Type(Integer32):
    """Custom type jnxL2tpSessionStatsFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 3),
          ("none", 1),
          ("sync", 2))
    )


_JnxL2tpSessionStatsFramingType_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsFramingType_Object = MibTableColumn
jnxL2tpSessionStatsFramingType = _JnxL2tpSessionStatsFramingType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 27),
    _JnxL2tpSessionStatsFramingType_Type()
)
jnxL2tpSessionStatsFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsFramingType.setStatus("current")


class _JnxL2tpSessionStatsLCPRenegotiation_Type(Integer32):
    """Custom type jnxL2tpSessionStatsLCPRenegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_JnxL2tpSessionStatsLCPRenegotiation_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsLCPRenegotiation_Object = MibTableColumn
jnxL2tpSessionStatsLCPRenegotiation = _JnxL2tpSessionStatsLCPRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 28),
    _JnxL2tpSessionStatsLCPRenegotiation_Type()
)
jnxL2tpSessionStatsLCPRenegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsLCPRenegotiation.setStatus("current")


class _JnxL2tpSessionStatsAuthMethod_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAuthMethod based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 8),
          ("pppChap", 3),
          ("pppEap", 5),
          ("pppMsChapV1", 6),
          ("pppMsChapV2", 7),
          ("pppPap", 4),
          ("text", 2))
    )


_JnxL2tpSessionStatsAuthMethod_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAuthMethod_Object = MibTableColumn
jnxL2tpSessionStatsAuthMethod = _JnxL2tpSessionStatsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 29),
    _JnxL2tpSessionStatsAuthMethod_Type()
)
jnxL2tpSessionStatsAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAuthMethod.setStatus("current")
_JnxL2tpSessionStatsNasIpAddrType_Type = InetAddressType
_JnxL2tpSessionStatsNasIpAddrType_Object = MibTableColumn
jnxL2tpSessionStatsNasIpAddrType = _JnxL2tpSessionStatsNasIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 30),
    _JnxL2tpSessionStatsNasIpAddrType_Type()
)
jnxL2tpSessionStatsNasIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsNasIpAddrType.setStatus("current")
_JnxL2tpSessionStatsNasIpAddress_Type = InetAddress
_JnxL2tpSessionStatsNasIpAddress_Object = MibTableColumn
jnxL2tpSessionStatsNasIpAddress = _JnxL2tpSessionStatsNasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 31),
    _JnxL2tpSessionStatsNasIpAddress_Type()
)
jnxL2tpSessionStatsNasIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsNasIpAddress.setStatus("current")
_JnxL2tpSessionStatsNasIpPort_Type = InetPortNumber
_JnxL2tpSessionStatsNasIpPort_Object = MibTableColumn
jnxL2tpSessionStatsNasIpPort = _JnxL2tpSessionStatsNasIpPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 32),
    _JnxL2tpSessionStatsNasIpPort_Type()
)
jnxL2tpSessionStatsNasIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsNasIpPort.setStatus("current")


class _JnxL2tpSessionStatsFramedProtocol_Type(Integer32):
    """Custom type jnxL2tpSessionStatsFramedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("arap", 3),
          ("gandalf", 4),
          ("none", 100),
          ("ppp", 1),
          ("slip", 2),
          ("x75-sync", 6),
          ("xylogicsIPX-SLIP", 5))
    )


_JnxL2tpSessionStatsFramedProtocol_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsFramedProtocol_Object = MibTableColumn
jnxL2tpSessionStatsFramedProtocol = _JnxL2tpSessionStatsFramedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 33),
    _JnxL2tpSessionStatsFramedProtocol_Type()
)
jnxL2tpSessionStatsFramedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsFramedProtocol.setStatus("current")
_JnxL2tpSessionStatsFramedIpAddrType_Type = InetAddressType
_JnxL2tpSessionStatsFramedIpAddrType_Object = MibTableColumn
jnxL2tpSessionStatsFramedIpAddrType = _JnxL2tpSessionStatsFramedIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 34),
    _JnxL2tpSessionStatsFramedIpAddrType_Type()
)
jnxL2tpSessionStatsFramedIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsFramedIpAddrType.setStatus("current")
_JnxL2tpSessionStatsFramedIpAddress_Type = InetAddress
_JnxL2tpSessionStatsFramedIpAddress_Object = MibTableColumn
jnxL2tpSessionStatsFramedIpAddress = _JnxL2tpSessionStatsFramedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 35),
    _JnxL2tpSessionStatsFramedIpAddress_Type()
)
jnxL2tpSessionStatsFramedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsFramedIpAddress.setStatus("current")
_JnxL2tpSessionStatsCallingStationID_Type = SnmpAdminString
_JnxL2tpSessionStatsCallingStationID_Object = MibTableColumn
jnxL2tpSessionStatsCallingStationID = _JnxL2tpSessionStatsCallingStationID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 36),
    _JnxL2tpSessionStatsCallingStationID_Type()
)
jnxL2tpSessionStatsCallingStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCallingStationID.setStatus("current")
_JnxL2tpSessionStatsCalledStationID_Type = SnmpAdminString
_JnxL2tpSessionStatsCalledStationID_Object = MibTableColumn
jnxL2tpSessionStatsCalledStationID = _JnxL2tpSessionStatsCalledStationID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 37),
    _JnxL2tpSessionStatsCalledStationID_Type()
)
jnxL2tpSessionStatsCalledStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCalledStationID.setStatus("current")


class _JnxL2tpSessionStatsAcctDelayTime_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAcctDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_JnxL2tpSessionStatsAcctDelayTime_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAcctDelayTime_Object = MibTableColumn
jnxL2tpSessionStatsAcctDelayTime = _JnxL2tpSessionStatsAcctDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 38),
    _JnxL2tpSessionStatsAcctDelayTime_Type()
)
jnxL2tpSessionStatsAcctDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctDelayTime.setStatus("current")
_JnxL2tpSessionStatsAcctSessionID_Type = SnmpAdminString
_JnxL2tpSessionStatsAcctSessionID_Object = MibTableColumn
jnxL2tpSessionStatsAcctSessionID = _JnxL2tpSessionStatsAcctSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 39),
    _JnxL2tpSessionStatsAcctSessionID_Type()
)
jnxL2tpSessionStatsAcctSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctSessionID.setStatus("current")


class _JnxL2tpSessionStatsAcctMethod_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAcctMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1))
    )


_JnxL2tpSessionStatsAcctMethod_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAcctMethod_Object = MibTableColumn
jnxL2tpSessionStatsAcctMethod = _JnxL2tpSessionStatsAcctMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 40),
    _JnxL2tpSessionStatsAcctMethod_Type()
)
jnxL2tpSessionStatsAcctMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctMethod.setStatus("current")
_JnxL2tpSessionStatsAcctSessionTime_Type = Gauge32
_JnxL2tpSessionStatsAcctSessionTime_Object = MibTableColumn
jnxL2tpSessionStatsAcctSessionTime = _JnxL2tpSessionStatsAcctSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 41),
    _JnxL2tpSessionStatsAcctSessionTime_Type()
)
jnxL2tpSessionStatsAcctSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctSessionTime.setStatus("current")


class _JnxL2tpSessionStatsAcctNasPortType_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAcctNasPortType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("adsl-cap", 13),
          ("adsl-dmt", 14),
          ("async", 1),
          ("cable", 18),
          ("ethernet", 16),
          ("g-3-fax", 11),
          ("hdlc-clear-channel", 8),
          ("idsl", 15),
          ("isdn-asunc-v-120", 4),
          ("isdn-async-v-110", 5),
          ("isdn-sync", 3),
          ("piafs", 7),
          ("sdsl", 12),
          ("sync", 2),
          ("virtual", 6),
          ("wireless-ieee-802-1", 20),
          ("wireless-other", 19),
          ("x-25", 9),
          ("x-75", 10),
          ("xdsl", 17))
    )


_JnxL2tpSessionStatsAcctNasPortType_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAcctNasPortType_Object = MibTableColumn
jnxL2tpSessionStatsAcctNasPortType = _JnxL2tpSessionStatsAcctNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 42),
    _JnxL2tpSessionStatsAcctNasPortType_Type()
)
jnxL2tpSessionStatsAcctNasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctNasPortType.setStatus("current")


class _JnxL2tpSessionStatsAcctTnlClientEndPoint_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAcctTnlClientEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsAcctTnlClientEndPoint_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAcctTnlClientEndPoint_Object = MibTableColumn
jnxL2tpSessionStatsAcctTnlClientEndPoint = _JnxL2tpSessionStatsAcctTnlClientEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 43),
    _JnxL2tpSessionStatsAcctTnlClientEndPoint_Type()
)
jnxL2tpSessionStatsAcctTnlClientEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctTnlClientEndPoint.setStatus("current")


class _JnxL2tpSessionStatsAcctTnlServerEndPoint_Type(Integer32):
    """Custom type jnxL2tpSessionStatsAcctTnlServerEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxL2tpSessionStatsAcctTnlServerEndPoint_Type.__name__ = "Integer32"
_JnxL2tpSessionStatsAcctTnlServerEndPoint_Object = MibTableColumn
jnxL2tpSessionStatsAcctTnlServerEndPoint = _JnxL2tpSessionStatsAcctTnlServerEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 44),
    _JnxL2tpSessionStatsAcctTnlServerEndPoint_Type()
)
jnxL2tpSessionStatsAcctTnlServerEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctTnlServerEndPoint.setStatus("current")
_JnxL2tpSessionStatsAcctTnlClientAuthID_Type = SnmpAdminString
_JnxL2tpSessionStatsAcctTnlClientAuthID_Object = MibTableColumn
jnxL2tpSessionStatsAcctTnlClientAuthID = _JnxL2tpSessionStatsAcctTnlClientAuthID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 45),
    _JnxL2tpSessionStatsAcctTnlClientAuthID_Type()
)
jnxL2tpSessionStatsAcctTnlClientAuthID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctTnlClientAuthID.setStatus("current")
_JnxL2tpSessionStatsAcctTnlServerAuthID_Type = SnmpAdminString
_JnxL2tpSessionStatsAcctTnlServerAuthID_Object = MibTableColumn
jnxL2tpSessionStatsAcctTnlServerAuthID = _JnxL2tpSessionStatsAcctTnlServerAuthID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 46),
    _JnxL2tpSessionStatsAcctTnlServerAuthID_Type()
)
jnxL2tpSessionStatsAcctTnlServerAuthID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsAcctTnlServerAuthID.setStatus("current")
_JnxL2tpSessionStatsUserProfileName_Type = SnmpAdminString
_JnxL2tpSessionStatsUserProfileName_Object = MibTableColumn
jnxL2tpSessionStatsUserProfileName = _JnxL2tpSessionStatsUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 47),
    _JnxL2tpSessionStatsUserProfileName_Type()
)
jnxL2tpSessionStatsUserProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsUserProfileName.setStatus("current")
_JnxL2tpSessionStatsInterfaceID_Type = SnmpAdminString
_JnxL2tpSessionStatsInterfaceID_Object = MibTableColumn
jnxL2tpSessionStatsInterfaceID = _JnxL2tpSessionStatsInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 48),
    _JnxL2tpSessionStatsInterfaceID_Type()
)
jnxL2tpSessionStatsInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsInterfaceID.setStatus("current")
_JnxL2tpSessionStatsCallSerialNumber_Type = Unsigned32
_JnxL2tpSessionStatsCallSerialNumber_Object = MibTableColumn
jnxL2tpSessionStatsCallSerialNumber = _JnxL2tpSessionStatsCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 49),
    _JnxL2tpSessionStatsCallSerialNumber_Type()
)
jnxL2tpSessionStatsCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCallSerialNumber.setStatus("current")
_JnxL2tpSessionStatsCreationTime_Type = DateAndTime
_JnxL2tpSessionStatsCreationTime_Object = MibTableColumn
jnxL2tpSessionStatsCreationTime = _JnxL2tpSessionStatsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 50),
    _JnxL2tpSessionStatsCreationTime_Type()
)
jnxL2tpSessionStatsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCreationTime.setStatus("current")
_JnxL2tpSessionStatsUpTime_Type = TimeTicks
_JnxL2tpSessionStatsUpTime_Object = MibTableColumn
jnxL2tpSessionStatsUpTime = _JnxL2tpSessionStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 51),
    _JnxL2tpSessionStatsUpTime_Type()
)
jnxL2tpSessionStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsUpTime.setStatus("current")
_JnxL2tpSessionStatsIdleTime_Type = TimeTicks
_JnxL2tpSessionStatsIdleTime_Object = MibTableColumn
jnxL2tpSessionStatsIdleTime = _JnxL2tpSessionStatsIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 52),
    _JnxL2tpSessionStatsIdleTime_Type()
)
jnxL2tpSessionStatsIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsIdleTime.setStatus("current")
_JnxL2tpSessionStatsCollectionStart_Type = DateAndTime
_JnxL2tpSessionStatsCollectionStart_Object = MibTableColumn
jnxL2tpSessionStatsCollectionStart = _JnxL2tpSessionStatsCollectionStart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 53),
    _JnxL2tpSessionStatsCollectionStart_Type()
)
jnxL2tpSessionStatsCollectionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsCollectionStart.setStatus("current")
_JnxL2tpSessionStatsControlTxPkts_Type = Counter32
_JnxL2tpSessionStatsControlTxPkts_Object = MibTableColumn
jnxL2tpSessionStatsControlTxPkts = _JnxL2tpSessionStatsControlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 54),
    _JnxL2tpSessionStatsControlTxPkts_Type()
)
jnxL2tpSessionStatsControlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlTxPkts.setStatus("current")
_JnxL2tpSessionStatsControlTxBytes_Type = Counter64
_JnxL2tpSessionStatsControlTxBytes_Object = MibTableColumn
jnxL2tpSessionStatsControlTxBytes = _JnxL2tpSessionStatsControlTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 55),
    _JnxL2tpSessionStatsControlTxBytes_Type()
)
jnxL2tpSessionStatsControlTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlTxBytes.setStatus("deprecated")
_JnxL2tpSessionStatsControlRxPkts_Type = Counter32
_JnxL2tpSessionStatsControlRxPkts_Object = MibTableColumn
jnxL2tpSessionStatsControlRxPkts = _JnxL2tpSessionStatsControlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 56),
    _JnxL2tpSessionStatsControlRxPkts_Type()
)
jnxL2tpSessionStatsControlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlRxPkts.setStatus("current")
_JnxL2tpSessionStatsControlRxBytes_Type = Counter64
_JnxL2tpSessionStatsControlRxBytes_Object = MibTableColumn
jnxL2tpSessionStatsControlRxBytes = _JnxL2tpSessionStatsControlRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 57),
    _JnxL2tpSessionStatsControlRxBytes_Type()
)
jnxL2tpSessionStatsControlRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlRxBytes.setStatus("deprecated")
_JnxL2tpSessionStatsDataTxPkts_Type = Counter32
_JnxL2tpSessionStatsDataTxPkts_Object = MibTableColumn
jnxL2tpSessionStatsDataTxPkts = _JnxL2tpSessionStatsDataTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 58),
    _JnxL2tpSessionStatsDataTxPkts_Type()
)
jnxL2tpSessionStatsDataTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataTxPkts.setStatus("deprecated")
_JnxL2tpSessionStatsDataTxBytes_Type = Counter64
_JnxL2tpSessionStatsDataTxBytes_Object = MibTableColumn
jnxL2tpSessionStatsDataTxBytes = _JnxL2tpSessionStatsDataTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 59),
    _JnxL2tpSessionStatsDataTxBytes_Type()
)
jnxL2tpSessionStatsDataTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataTxBytes.setStatus("current")
_JnxL2tpSessionStatsDataRxPkts_Type = Counter32
_JnxL2tpSessionStatsDataRxPkts_Object = MibTableColumn
jnxL2tpSessionStatsDataRxPkts = _JnxL2tpSessionStatsDataRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 60),
    _JnxL2tpSessionStatsDataRxPkts_Type()
)
jnxL2tpSessionStatsDataRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataRxPkts.setStatus("deprecated")
_JnxL2tpSessionStatsDataRxBytes_Type = Counter64
_JnxL2tpSessionStatsDataRxBytes_Object = MibTableColumn
jnxL2tpSessionStatsDataRxBytes = _JnxL2tpSessionStatsDataRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 61),
    _JnxL2tpSessionStatsDataRxBytes_Type()
)
jnxL2tpSessionStatsDataRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataRxBytes.setStatus("current")
_JnxL2tpSessionStatsErrorTxPkts_Type = Counter32
_JnxL2tpSessionStatsErrorTxPkts_Object = MibTableColumn
jnxL2tpSessionStatsErrorTxPkts = _JnxL2tpSessionStatsErrorTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 62),
    _JnxL2tpSessionStatsErrorTxPkts_Type()
)
jnxL2tpSessionStatsErrorTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsErrorTxPkts.setStatus("current")
_JnxL2tpSessionStatsErrorRxPkts_Type = Counter32
_JnxL2tpSessionStatsErrorRxPkts_Object = MibTableColumn
jnxL2tpSessionStatsErrorRxPkts = _JnxL2tpSessionStatsErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 63),
    _JnxL2tpSessionStatsErrorRxPkts_Type()
)
jnxL2tpSessionStatsErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsErrorRxPkts.setStatus("current")
_JnxL2tpSessionStatsControlTxBytes32_Type = Counter32
_JnxL2tpSessionStatsControlTxBytes32_Object = MibTableColumn
jnxL2tpSessionStatsControlTxBytes32 = _JnxL2tpSessionStatsControlTxBytes32_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 64),
    _JnxL2tpSessionStatsControlTxBytes32_Type()
)
jnxL2tpSessionStatsControlTxBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlTxBytes32.setStatus("current")
_JnxL2tpSessionStatsControlRxBytes32_Type = Counter32
_JnxL2tpSessionStatsControlRxBytes32_Object = MibTableColumn
jnxL2tpSessionStatsControlRxBytes32 = _JnxL2tpSessionStatsControlRxBytes32_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 65),
    _JnxL2tpSessionStatsControlRxBytes32_Type()
)
jnxL2tpSessionStatsControlRxBytes32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsControlRxBytes32.setStatus("current")
_JnxL2tpSessionStatsDataTxPkts64_Type = Counter64
_JnxL2tpSessionStatsDataTxPkts64_Object = MibTableColumn
jnxL2tpSessionStatsDataTxPkts64 = _JnxL2tpSessionStatsDataTxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 66),
    _JnxL2tpSessionStatsDataTxPkts64_Type()
)
jnxL2tpSessionStatsDataTxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataTxPkts64.setStatus("current")
_JnxL2tpSessionStatsDataRxPkts64_Type = Counter64
_JnxL2tpSessionStatsDataRxPkts64_Object = MibTableColumn
jnxL2tpSessionStatsDataRxPkts64 = _JnxL2tpSessionStatsDataRxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 4, 1, 67),
    _JnxL2tpSessionStatsDataRxPkts64_Type()
)
jnxL2tpSessionStatsDataRxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpSessionStatsDataRxPkts64.setStatus("current")
_JnxL2tpMlpppBundleStatsTable_Object = MibTable
jnxL2tpMlpppBundleStatsTable = _JnxL2tpMlpppBundleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsTable.setStatus("current")
_JnxL2tpMlpppBundleStatsEntry_Object = MibTableRow
jnxL2tpMlpppBundleStatsEntry = _JnxL2tpMlpppBundleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1)
)
jnxL2tpMlpppBundleStatsEntry.setIndexNames(
    (0, "JNX-L2TP-MIB", "jnxL2tpMlpppBundleStatsBundleID"),
)
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsEntry.setStatus("current")


class _JnxL2tpMlpppBundleStatsBundleID_Type(Integer32):
    """Custom type jnxL2tpMlpppBundleStatsBundleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_JnxL2tpMlpppBundleStatsBundleID_Type.__name__ = "Integer32"
_JnxL2tpMlpppBundleStatsBundleID_Object = MibTableColumn
jnxL2tpMlpppBundleStatsBundleID = _JnxL2tpMlpppBundleStatsBundleID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1, 1),
    _JnxL2tpMlpppBundleStatsBundleID_Type()
)
jnxL2tpMlpppBundleStatsBundleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsBundleID.setStatus("current")


class _JnxL2tpMlpppBundleStatsNumLinks_Type(Integer32):
    """Custom type jnxL2tpMlpppBundleStatsNumLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_JnxL2tpMlpppBundleStatsNumLinks_Type.__name__ = "Integer32"
_JnxL2tpMlpppBundleStatsNumLinks_Object = MibTableColumn
jnxL2tpMlpppBundleStatsNumLinks = _JnxL2tpMlpppBundleStatsNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1, 2),
    _JnxL2tpMlpppBundleStatsNumLinks_Type()
)
jnxL2tpMlpppBundleStatsNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsNumLinks.setStatus("current")
_JnxL2tpMlpppBundleStatsEndpoint_Type = SnmpAdminString
_JnxL2tpMlpppBundleStatsEndpoint_Object = MibTableColumn
jnxL2tpMlpppBundleStatsEndpoint = _JnxL2tpMlpppBundleStatsEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1, 3),
    _JnxL2tpMlpppBundleStatsEndpoint_Type()
)
jnxL2tpMlpppBundleStatsEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsEndpoint.setStatus("current")


class _JnxL2tpMlpppBundleStatsInputMrru_Type(Integer32):
    """Custom type jnxL2tpMlpppBundleStatsInputMrru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4500),
    )


_JnxL2tpMlpppBundleStatsInputMrru_Type.__name__ = "Integer32"
_JnxL2tpMlpppBundleStatsInputMrru_Object = MibTableColumn
jnxL2tpMlpppBundleStatsInputMrru = _JnxL2tpMlpppBundleStatsInputMrru_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1, 4),
    _JnxL2tpMlpppBundleStatsInputMrru_Type()
)
jnxL2tpMlpppBundleStatsInputMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsInputMrru.setStatus("current")


class _JnxL2tpMlpppBundleStatsOutputMrru_Type(Integer32):
    """Custom type jnxL2tpMlpppBundleStatsOutputMrru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4500),
    )


_JnxL2tpMlpppBundleStatsOutputMrru_Type.__name__ = "Integer32"
_JnxL2tpMlpppBundleStatsOutputMrru_Object = MibTableColumn
jnxL2tpMlpppBundleStatsOutputMrru = _JnxL2tpMlpppBundleStatsOutputMrru_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 49, 1, 1, 5, 1, 5),
    _JnxL2tpMlpppBundleStatsOutputMrru_Type()
)
jnxL2tpMlpppBundleStatsOutputMrru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2tpMlpppBundleStatsOutputMrru.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-L2TP-MIB",
    **{"jnxL2tp": jnxL2tp,
       "jnxL2tpObjects": jnxL2tpObjects,
       "jnxL2tpScalar": jnxL2tpScalar,
       "jnxL2tpStats": jnxL2tpStats,
       "jnxL2tpStatsTotalTunnels": jnxL2tpStatsTotalTunnels,
       "jnxL2tpStatsTotalSessions": jnxL2tpStatsTotalSessions,
       "jnxL2tpStatsControlRxOctets": jnxL2tpStatsControlRxOctets,
       "jnxL2tpStatsControlRxPkts": jnxL2tpStatsControlRxPkts,
       "jnxL2tpStatsControlTxOctets": jnxL2tpStatsControlTxOctets,
       "jnxL2tpStatsControlTxPkts": jnxL2tpStatsControlTxPkts,
       "jnxL2tpStatsPayloadRxOctets": jnxL2tpStatsPayloadRxOctets,
       "jnxL2tpStatsPayloadRxPkts": jnxL2tpStatsPayloadRxPkts,
       "jnxL2tpStatsPayloadTxOctets": jnxL2tpStatsPayloadTxOctets,
       "jnxL2tpStatsPayloadTxPkts": jnxL2tpStatsPayloadTxPkts,
       "jnxL2tpStatsErrorTxPkts": jnxL2tpStatsErrorTxPkts,
       "jnxL2tpStatsErrorRxPkts": jnxL2tpStatsErrorRxPkts,
       "jnxL2tpStatsPayloadRxOctets64": jnxL2tpStatsPayloadRxOctets64,
       "jnxL2tpTunnelGroupStatsTable": jnxL2tpTunnelGroupStatsTable,
       "jnxL2tpTunnelGroupStatsEntry": jnxL2tpTunnelGroupStatsEntry,
       "jnxL2tpTunnelGroupStatsTnlGrpName": jnxL2tpTunnelGroupStatsTnlGrpName,
       "jnxL2tpTunnelGroupStatsGatewayAddrType": jnxL2tpTunnelGroupStatsGatewayAddrType,
       "jnxL2tpTunnelGroupStatsGatewayAddr": jnxL2tpTunnelGroupStatsGatewayAddr,
       "jnxL2tpTunnelGroupStatsSvcIntfName": jnxL2tpTunnelGroupStatsSvcIntfName,
       "jnxL2tpTunnelGroupStatsTotalTunnels": jnxL2tpTunnelGroupStatsTotalTunnels,
       "jnxL2tpTunnelGroupStatsTotalSessions": jnxL2tpTunnelGroupStatsTotalSessions,
       "jnxL2tpTunnelStatsTable": jnxL2tpTunnelStatsTable,
       "jnxL2tpTunnelStatsEntry": jnxL2tpTunnelStatsEntry,
       "jnxL2tpTunnelStatsLocalTID": jnxL2tpTunnelStatsLocalTID,
       "jnxL2tpTunnelStatsServiceInterface": jnxL2tpTunnelStatsServiceInterface,
       "jnxL2tpTunnelStatsTunnelGroup": jnxL2tpTunnelStatsTunnelGroup,
       "jnxL2tpTunnelStatsRemoteTID": jnxL2tpTunnelStatsRemoteTID,
       "jnxL2tpTunnelStatsRemoteIpAddrType": jnxL2tpTunnelStatsRemoteIpAddrType,
       "jnxL2tpTunnelStatsRemoteIpAddress": jnxL2tpTunnelStatsRemoteIpAddress,
       "jnxL2tpTunnelStatsRemoteUdpPort": jnxL2tpTunnelStatsRemoteUdpPort,
       "jnxL2tpTunnelStatsActiveSessions": jnxL2tpTunnelStatsActiveSessions,
       "jnxL2tpTunnelStatsState": jnxL2tpTunnelStatsState,
       "jnxL2tpTunnelStatsLocalIpAddrType": jnxL2tpTunnelStatsLocalIpAddrType,
       "jnxL2tpTunnelStatsLocalIpAddress": jnxL2tpTunnelStatsLocalIpAddress,
       "jnxL2tpTunnelStatsLocalUdpPort": jnxL2tpTunnelStatsLocalUdpPort,
       "jnxL2tpTunnelStatsLocalHostName": jnxL2tpTunnelStatsLocalHostName,
       "jnxL2tpTunnelStatsRemoteHostName": jnxL2tpTunnelStatsRemoteHostName,
       "jnxL2tpTunnelMaxSessions": jnxL2tpTunnelMaxSessions,
       "jnxL2tpTunnelStatsWindowSize": jnxL2tpTunnelStatsWindowSize,
       "jnxL2tpTunnelStatsHelloInterval": jnxL2tpTunnelStatsHelloInterval,
       "jnxL2tpTunnelStatsCreationTime": jnxL2tpTunnelStatsCreationTime,
       "jnxL2tpTunnelStatsUpTime": jnxL2tpTunnelStatsUpTime,
       "jnxL2tpTunnelStatsIdleTime": jnxL2tpTunnelStatsIdleTime,
       "jnxL2tpTunnelStatsCollectionStart": jnxL2tpTunnelStatsCollectionStart,
       "jnxL2tpTunnelStatsControlTxPkts": jnxL2tpTunnelStatsControlTxPkts,
       "jnxL2tpTunnelStatsControlTxBytes": jnxL2tpTunnelStatsControlTxBytes,
       "jnxL2tpTunnelStatsControlRxPkts": jnxL2tpTunnelStatsControlRxPkts,
       "jnxL2tpTunnelStatsControlRxBytes": jnxL2tpTunnelStatsControlRxBytes,
       "jnxL2tpTunnelStatsDataTxPkts": jnxL2tpTunnelStatsDataTxPkts,
       "jnxL2tpTunnelStatsDataTxBytes": jnxL2tpTunnelStatsDataTxBytes,
       "jnxL2tpTunnelStatsDataRxPkts": jnxL2tpTunnelStatsDataRxPkts,
       "jnxL2tpTunnelStatsDataRxBytes": jnxL2tpTunnelStatsDataRxBytes,
       "jnxL2tpTunnelStatsErrorTxPkts": jnxL2tpTunnelStatsErrorTxPkts,
       "jnxL2tpTunnelStatsErrorRxPkts": jnxL2tpTunnelStatsErrorRxPkts,
       "jnxL2tpTunnelStatsControlTxBytes32": jnxL2tpTunnelStatsControlTxBytes32,
       "jnxL2tpTunnelStatsControlRxBytes32": jnxL2tpTunnelStatsControlRxBytes32,
       "jnxL2tpTunnelStatsDataTxPkts64": jnxL2tpTunnelStatsDataTxPkts64,
       "jnxL2tpTunnelStatsDataRxPkts64": jnxL2tpTunnelStatsDataRxPkts64,
       "jnxL2tpSessionStatsTable": jnxL2tpSessionStatsTable,
       "jnxL2tpSessionStatsEntry": jnxL2tpSessionStatsEntry,
       "jnxL2tpSessionStatsLocalTID": jnxL2tpSessionStatsLocalTID,
       "jnxL2tpSessionStatsLocalSID": jnxL2tpSessionStatsLocalSID,
       "jnxL2tpSessionStatsServiceInterface": jnxL2tpSessionStatsServiceInterface,
       "jnxL2tpSessionStatsTunnelGroup": jnxL2tpSessionStatsTunnelGroup,
       "jnxL2tpSessionStatsRemoteSID": jnxL2tpSessionStatsRemoteSID,
       "jnxL2tpSessionStatsInterfaceUnit": jnxL2tpSessionStatsInterfaceUnit,
       "jnxL2tpSessionStatsEncapType": jnxL2tpSessionStatsEncapType,
       "jnxL2tpSessionStatsBundleID": jnxL2tpSessionStatsBundleID,
       "jnxL2tpSessionStatsState": jnxL2tpSessionStatsState,
       "jnxL2tpSessionStatsUserName": jnxL2tpSessionStatsUserName,
       "jnxL2tpSessionStatsMode": jnxL2tpSessionStatsMode,
       "jnxL2tpSessionStatsLocalAddrType": jnxL2tpSessionStatsLocalAddrType,
       "jnxL2tpSessionStatsLocalAddress": jnxL2tpSessionStatsLocalAddress,
       "jnxL2tpSessionStatsLocalUdpPort": jnxL2tpSessionStatsLocalUdpPort,
       "jnxL2tpSessionStatsRemoteAddrType": jnxL2tpSessionStatsRemoteAddrType,
       "jnxL2tpSessionStatsRemoteAddress": jnxL2tpSessionStatsRemoteAddress,
       "jnxL2tpSessionStatsRemoteUdpPort": jnxL2tpSessionStatsRemoteUdpPort,
       "jnxL2tpSessionStatsLocalHostName": jnxL2tpSessionStatsLocalHostName,
       "jnxL2tpSessionStatsRemoteHostName": jnxL2tpSessionStatsRemoteHostName,
       "jnxL2tpSessionAssignedIpAddrType": jnxL2tpSessionAssignedIpAddrType,
       "jnxL2tpSessionAssignedIpAddress": jnxL2tpSessionAssignedIpAddress,
       "jnxL2tpSessionLocalMRU": jnxL2tpSessionLocalMRU,
       "jnxL2tpSessionRemoteMRU": jnxL2tpSessionRemoteMRU,
       "jnxL2tpSessionStatsTxSpeed": jnxL2tpSessionStatsTxSpeed,
       "jnxL2tpSessionStatsRxSpeed": jnxL2tpSessionStatsRxSpeed,
       "jnxL2tpSessionStatsCallBearerType": jnxL2tpSessionStatsCallBearerType,
       "jnxL2tpSessionStatsFramingType": jnxL2tpSessionStatsFramingType,
       "jnxL2tpSessionStatsLCPRenegotiation": jnxL2tpSessionStatsLCPRenegotiation,
       "jnxL2tpSessionStatsAuthMethod": jnxL2tpSessionStatsAuthMethod,
       "jnxL2tpSessionStatsNasIpAddrType": jnxL2tpSessionStatsNasIpAddrType,
       "jnxL2tpSessionStatsNasIpAddress": jnxL2tpSessionStatsNasIpAddress,
       "jnxL2tpSessionStatsNasIpPort": jnxL2tpSessionStatsNasIpPort,
       "jnxL2tpSessionStatsFramedProtocol": jnxL2tpSessionStatsFramedProtocol,
       "jnxL2tpSessionStatsFramedIpAddrType": jnxL2tpSessionStatsFramedIpAddrType,
       "jnxL2tpSessionStatsFramedIpAddress": jnxL2tpSessionStatsFramedIpAddress,
       "jnxL2tpSessionStatsCallingStationID": jnxL2tpSessionStatsCallingStationID,
       "jnxL2tpSessionStatsCalledStationID": jnxL2tpSessionStatsCalledStationID,
       "jnxL2tpSessionStatsAcctDelayTime": jnxL2tpSessionStatsAcctDelayTime,
       "jnxL2tpSessionStatsAcctSessionID": jnxL2tpSessionStatsAcctSessionID,
       "jnxL2tpSessionStatsAcctMethod": jnxL2tpSessionStatsAcctMethod,
       "jnxL2tpSessionStatsAcctSessionTime": jnxL2tpSessionStatsAcctSessionTime,
       "jnxL2tpSessionStatsAcctNasPortType": jnxL2tpSessionStatsAcctNasPortType,
       "jnxL2tpSessionStatsAcctTnlClientEndPoint": jnxL2tpSessionStatsAcctTnlClientEndPoint,
       "jnxL2tpSessionStatsAcctTnlServerEndPoint": jnxL2tpSessionStatsAcctTnlServerEndPoint,
       "jnxL2tpSessionStatsAcctTnlClientAuthID": jnxL2tpSessionStatsAcctTnlClientAuthID,
       "jnxL2tpSessionStatsAcctTnlServerAuthID": jnxL2tpSessionStatsAcctTnlServerAuthID,
       "jnxL2tpSessionStatsUserProfileName": jnxL2tpSessionStatsUserProfileName,
       "jnxL2tpSessionStatsInterfaceID": jnxL2tpSessionStatsInterfaceID,
       "jnxL2tpSessionStatsCallSerialNumber": jnxL2tpSessionStatsCallSerialNumber,
       "jnxL2tpSessionStatsCreationTime": jnxL2tpSessionStatsCreationTime,
       "jnxL2tpSessionStatsUpTime": jnxL2tpSessionStatsUpTime,
       "jnxL2tpSessionStatsIdleTime": jnxL2tpSessionStatsIdleTime,
       "jnxL2tpSessionStatsCollectionStart": jnxL2tpSessionStatsCollectionStart,
       "jnxL2tpSessionStatsControlTxPkts": jnxL2tpSessionStatsControlTxPkts,
       "jnxL2tpSessionStatsControlTxBytes": jnxL2tpSessionStatsControlTxBytes,
       "jnxL2tpSessionStatsControlRxPkts": jnxL2tpSessionStatsControlRxPkts,
       "jnxL2tpSessionStatsControlRxBytes": jnxL2tpSessionStatsControlRxBytes,
       "jnxL2tpSessionStatsDataTxPkts": jnxL2tpSessionStatsDataTxPkts,
       "jnxL2tpSessionStatsDataTxBytes": jnxL2tpSessionStatsDataTxBytes,
       "jnxL2tpSessionStatsDataRxPkts": jnxL2tpSessionStatsDataRxPkts,
       "jnxL2tpSessionStatsDataRxBytes": jnxL2tpSessionStatsDataRxBytes,
       "jnxL2tpSessionStatsErrorTxPkts": jnxL2tpSessionStatsErrorTxPkts,
       "jnxL2tpSessionStatsErrorRxPkts": jnxL2tpSessionStatsErrorRxPkts,
       "jnxL2tpSessionStatsControlTxBytes32": jnxL2tpSessionStatsControlTxBytes32,
       "jnxL2tpSessionStatsControlRxBytes32": jnxL2tpSessionStatsControlRxBytes32,
       "jnxL2tpSessionStatsDataTxPkts64": jnxL2tpSessionStatsDataTxPkts64,
       "jnxL2tpSessionStatsDataRxPkts64": jnxL2tpSessionStatsDataRxPkts64,
       "jnxL2tpMlpppBundleStatsTable": jnxL2tpMlpppBundleStatsTable,
       "jnxL2tpMlpppBundleStatsEntry": jnxL2tpMlpppBundleStatsEntry,
       "jnxL2tpMlpppBundleStatsBundleID": jnxL2tpMlpppBundleStatsBundleID,
       "jnxL2tpMlpppBundleStatsNumLinks": jnxL2tpMlpppBundleStatsNumLinks,
       "jnxL2tpMlpppBundleStatsEndpoint": jnxL2tpMlpppBundleStatsEndpoint,
       "jnxL2tpMlpppBundleStatsInputMrru": jnxL2tpMlpppBundleStatsInputMrru,
       "jnxL2tpMlpppBundleStatsOutputMrru": jnxL2tpMlpppBundleStatsOutputMrru}
)
