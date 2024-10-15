# SNMP MIB module (CISCO-FC-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:20 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

ciscoFiberChannelTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999)
)
ciscoFiberChannelTunnelMIB.setRevisions(
        ("2002-03-08 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFCTunnelMIBNotifi_ObjectIdentity = ObjectIdentity
ciscoFCTunnelMIBNotifi = _CiscoFCTunnelMIBNotifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 0)
)
_CiscoFCTunnelMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFCTunnelMIBObjects = _CiscoFCTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1)
)
_CftTcpTunnelObjects_ObjectIdentity = ObjectIdentity
cftTcpTunnelObjects = _CftTcpTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1)
)
_CftMaxTcpTunnels_Type = Unsigned32
_CftMaxTcpTunnels_Object = MibScalar
cftMaxTcpTunnels = _CftMaxTcpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1),
    _CftMaxTcpTunnels_Type()
)
cftMaxTcpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftMaxTcpTunnels.setStatus("current")
_CftTcpTunnelTable_Object = MibTable
cftTcpTunnelTable = _CftTcpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cftTcpTunnelTable.setStatus("current")
_CftTcpTunnelEntry_Object = MibTableRow
cftTcpTunnelEntry = _CftTcpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1)
)
cftTcpTunnelEntry.setIndexNames(
    (0, "CISCO-FC-TUNNEL-MIB", "cftFiberChannelIf"),
    (1, "CISCO-FC-TUNNEL-MIB", "cftTcpTunnelName"),
)
if mibBuilder.loadTexts:
    cftTcpTunnelEntry.setStatus("current")
_CftFiberChannelIf_Type = InterfaceIndex
_CftFiberChannelIf_Object = MibTableColumn
cftFiberChannelIf = _CftFiberChannelIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1),
    _CftFiberChannelIf_Type()
)
cftFiberChannelIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cftFiberChannelIf.setStatus("current")


class _CftTcpTunnelName_Type(SnmpAdminString):
    """Custom type cftTcpTunnelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CftTcpTunnelName_Type.__name__ = "SnmpAdminString"
_CftTcpTunnelName_Object = MibTableColumn
cftTcpTunnelName = _CftTcpTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 2),
    _CftTcpTunnelName_Type()
)
cftTcpTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cftTcpTunnelName.setStatus("current")
_CftTcpTunnelSrcIpType_Type = InetAddressType
_CftTcpTunnelSrcIpType_Object = MibTableColumn
cftTcpTunnelSrcIpType = _CftTcpTunnelSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 3),
    _CftTcpTunnelSrcIpType_Type()
)
cftTcpTunnelSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelSrcIpType.setStatus("current")
_CftTcpTunnelSrcIp_Type = InetAddress
_CftTcpTunnelSrcIp_Object = MibTableColumn
cftTcpTunnelSrcIp = _CftTcpTunnelSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 4),
    _CftTcpTunnelSrcIp_Type()
)
cftTcpTunnelSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelSrcIp.setStatus("current")
_CftTcpTunnelDestIpType_Type = InetAddressType
_CftTcpTunnelDestIpType_Object = MibTableColumn
cftTcpTunnelDestIpType = _CftTcpTunnelDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 5),
    _CftTcpTunnelDestIpType_Type()
)
cftTcpTunnelDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDestIpType.setStatus("current")
_CftTcpTunnelDestIp_Type = InetAddress
_CftTcpTunnelDestIp_Object = MibTableColumn
cftTcpTunnelDestIp = _CftTcpTunnelDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 6),
    _CftTcpTunnelDestIp_Type()
)
cftTcpTunnelDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDestIp.setStatus("current")


class _CftTcpTunnelCmdSrcPort_Type(Unsigned32):
    """Custom type cftTcpTunnelCmdSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_CftTcpTunnelCmdSrcPort_Type.__name__ = "Unsigned32"
_CftTcpTunnelCmdSrcPort_Object = MibTableColumn
cftTcpTunnelCmdSrcPort = _CftTcpTunnelCmdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 7),
    _CftTcpTunnelCmdSrcPort_Type()
)
cftTcpTunnelCmdSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdSrcPort.setStatus("current")


class _CftTcpTunnelCmdDestPort_Type(Unsigned32):
    """Custom type cftTcpTunnelCmdDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_CftTcpTunnelCmdDestPort_Type.__name__ = "Unsigned32"
_CftTcpTunnelCmdDestPort_Object = MibTableColumn
cftTcpTunnelCmdDestPort = _CftTcpTunnelCmdDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 8),
    _CftTcpTunnelCmdDestPort_Type()
)
cftTcpTunnelCmdDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdDestPort.setStatus("current")


class _CftTcpTunnelDataSrcPort_Type(Unsigned32):
    """Custom type cftTcpTunnelDataSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_CftTcpTunnelDataSrcPort_Type.__name__ = "Unsigned32"
_CftTcpTunnelDataSrcPort_Object = MibTableColumn
cftTcpTunnelDataSrcPort = _CftTcpTunnelDataSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 9),
    _CftTcpTunnelDataSrcPort_Type()
)
cftTcpTunnelDataSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDataSrcPort.setStatus("current")


class _CftTcpTunnelDataDestPort_Type(Unsigned32):
    """Custom type cftTcpTunnelDataDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_CftTcpTunnelDataDestPort_Type.__name__ = "Unsigned32"
_CftTcpTunnelDataDestPort_Object = MibTableColumn
cftTcpTunnelDataDestPort = _CftTcpTunnelDataDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 10),
    _CftTcpTunnelDataDestPort_Type()
)
cftTcpTunnelDataDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDataDestPort.setStatus("current")


class _CftTcpTunnelCmdMWS_Type(Integer32):
    """Custom type cftTcpTunnelCmdMWS based on Integer32"""
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
        *(("ws128kbytes", 2),
          ("ws256kbytes", 3),
          ("ws32kbytes", 1),
          ("ws512kbytes", 4))
    )


_CftTcpTunnelCmdMWS_Type.__name__ = "Integer32"
_CftTcpTunnelCmdMWS_Object = MibTableColumn
cftTcpTunnelCmdMWS = _CftTcpTunnelCmdMWS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 11),
    _CftTcpTunnelCmdMWS_Type()
)
cftTcpTunnelCmdMWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdMWS.setStatus("current")


class _CftTcpTunnelDataMWS_Type(Integer32):
    """Custom type cftTcpTunnelDataMWS based on Integer32"""
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
        *(("ws128kbytes", 2),
          ("ws256kbytes", 3),
          ("ws32kbytes", 1),
          ("ws512kbytes", 4))
    )


_CftTcpTunnelDataMWS_Type.__name__ = "Integer32"
_CftTcpTunnelDataMWS_Object = MibTableColumn
cftTcpTunnelDataMWS = _CftTcpTunnelDataMWS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 12),
    _CftTcpTunnelDataMWS_Type()
)
cftTcpTunnelDataMWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDataMWS.setStatus("current")


class _CftTcpTunnelCmdKeepAliveTime_Type(Unsigned32):
    """Custom type cftTcpTunnelCmdKeepAliveTime based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 10800),
    )


_CftTcpTunnelCmdKeepAliveTime_Type.__name__ = "Unsigned32"
_CftTcpTunnelCmdKeepAliveTime_Object = MibTableColumn
cftTcpTunnelCmdKeepAliveTime = _CftTcpTunnelCmdKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 13),
    _CftTcpTunnelCmdKeepAliveTime_Type()
)
cftTcpTunnelCmdKeepAliveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdKeepAliveTime.setUnits("seconds")


class _CftTcpTunnelDataKeepAliveTime_Type(Unsigned32):
    """Custom type cftTcpTunnelDataKeepAliveTime based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 10800),
    )


_CftTcpTunnelDataKeepAliveTime_Type.__name__ = "Unsigned32"
_CftTcpTunnelDataKeepAliveTime_Object = MibTableColumn
cftTcpTunnelDataKeepAliveTime = _CftTcpTunnelDataKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 14),
    _CftTcpTunnelDataKeepAliveTime_Type()
)
cftTcpTunnelDataKeepAliveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDataKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataKeepAliveTime.setUnits("seconds")


class _CftTcpTunnelCmdSelectiveAck_Type(TruthValue):
    """Custom type cftTcpTunnelCmdSelectiveAck based on TruthValue"""


_CftTcpTunnelCmdSelectiveAck_Object = MibTableColumn
cftTcpTunnelCmdSelectiveAck = _CftTcpTunnelCmdSelectiveAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 15),
    _CftTcpTunnelCmdSelectiveAck_Type()
)
cftTcpTunnelCmdSelectiveAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdSelectiveAck.setStatus("current")


class _CftTcpTunnelDataSelectiveAck_Type(TruthValue):
    """Custom type cftTcpTunnelDataSelectiveAck based on TruthValue"""


_CftTcpTunnelDataSelectiveAck_Object = MibTableColumn
cftTcpTunnelDataSelectiveAck = _CftTcpTunnelDataSelectiveAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 16),
    _CftTcpTunnelDataSelectiveAck_Type()
)
cftTcpTunnelDataSelectiveAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelDataSelectiveAck.setStatus("current")


class _CftTcpTunnelCmdConnectStatus_Type(Integer32):
    """Custom type cftTcpTunnelCmdConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2))
    )


_CftTcpTunnelCmdConnectStatus_Type.__name__ = "Integer32"
_CftTcpTunnelCmdConnectStatus_Object = MibTableColumn
cftTcpTunnelCmdConnectStatus = _CftTcpTunnelCmdConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 17),
    _CftTcpTunnelCmdConnectStatus_Type()
)
cftTcpTunnelCmdConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdConnectStatus.setStatus("current")


class _CftTcpTunnelDataConnectStatus_Type(Integer32):
    """Custom type cftTcpTunnelDataConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2))
    )


_CftTcpTunnelDataConnectStatus_Type.__name__ = "Integer32"
_CftTcpTunnelDataConnectStatus_Object = MibTableColumn
cftTcpTunnelDataConnectStatus = _CftTcpTunnelDataConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 18),
    _CftTcpTunnelDataConnectStatus_Type()
)
cftTcpTunnelDataConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataConnectStatus.setStatus("current")


class _CftTcpTunnelOperStatus_Type(Integer32):
    """Custom type cftTcpTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CftTcpTunnelOperStatus_Type.__name__ = "Integer32"
_CftTcpTunnelOperStatus_Object = MibTableColumn
cftTcpTunnelOperStatus = _CftTcpTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 19),
    _CftTcpTunnelOperStatus_Type()
)
cftTcpTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelOperStatus.setStatus("current")
_CftTcpTunnelStatus_Type = RowStatus
_CftTcpTunnelStatus_Object = MibTableColumn
cftTcpTunnelStatus = _CftTcpTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 20),
    _CftTcpTunnelStatus_Type()
)
cftTcpTunnelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cftTcpTunnelStatus.setStatus("current")
_CftTcpTunnelStatsTable_Object = MibTable
cftTcpTunnelStatsTable = _CftTcpTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cftTcpTunnelStatsTable.setStatus("current")
_CftTcpTunnelStatsEntry_Object = MibTableRow
cftTcpTunnelStatsEntry = _CftTcpTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1)
)
cftTcpTunnelStatsEntry.setIndexNames(
    (0, "CISCO-FC-TUNNEL-MIB", "cftFiberChannelIf"),
    (1, "CISCO-FC-TUNNEL-MIB", "cftTcpTunnelName"),
)
if mibBuilder.loadTexts:
    cftTcpTunnelStatsEntry.setStatus("current")
_CftTcpTunnelCmdRxSegmentOctets_Type = Counter64
_CftTcpTunnelCmdRxSegmentOctets_Object = MibTableColumn
cftTcpTunnelCmdRxSegmentOctets = _CftTcpTunnelCmdRxSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1),
    _CftTcpTunnelCmdRxSegmentOctets_Type()
)
cftTcpTunnelCmdRxSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxSegmentOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxSegmentOctets.setUnits("bytes")
_CftTcpTunnelDataRxSegmentOctets_Type = Counter64
_CftTcpTunnelDataRxSegmentOctets_Object = MibTableColumn
cftTcpTunnelDataRxSegmentOctets = _CftTcpTunnelDataRxSegmentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 2),
    _CftTcpTunnelDataRxSegmentOctets_Type()
)
cftTcpTunnelDataRxSegmentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxSegmentOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxSegmentOctets.setUnits("bytes")
_CftTcpTunnelCmdRxPrestufOctets_Type = Counter64
_CftTcpTunnelCmdRxPrestufOctets_Object = MibTableColumn
cftTcpTunnelCmdRxPrestufOctets = _CftTcpTunnelCmdRxPrestufOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 3),
    _CftTcpTunnelCmdRxPrestufOctets_Type()
)
cftTcpTunnelCmdRxPrestufOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxPrestufOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxPrestufOctets.setUnits("bytes")
_CftTcpTunnelDataRxPrestufOctets_Type = Counter64
_CftTcpTunnelDataRxPrestufOctets_Object = MibTableColumn
cftTcpTunnelDataRxPrestufOctets = _CftTcpTunnelDataRxPrestufOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 4),
    _CftTcpTunnelDataRxPrestufOctets_Type()
)
cftTcpTunnelDataRxPrestufOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxPrestufOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxPrestufOctets.setUnits("bytes")
_CftTcpTunnelCmdRxPoststufOctets_Type = Counter64
_CftTcpTunnelCmdRxPoststufOctets_Object = MibTableColumn
cftTcpTunnelCmdRxPoststufOctets = _CftTcpTunnelCmdRxPoststufOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 5),
    _CftTcpTunnelCmdRxPoststufOctets_Type()
)
cftTcpTunnelCmdRxPoststufOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxPoststufOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdRxPoststufOctets.setUnits("bytes")
_CftTcpTunnelDataRxPoststufOctets_Type = Counter64
_CftTcpTunnelDataRxPoststufOctets_Object = MibTableColumn
cftTcpTunnelDataRxPoststufOctets = _CftTcpTunnelDataRxPoststufOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 6),
    _CftTcpTunnelDataRxPoststufOctets_Type()
)
cftTcpTunnelDataRxPoststufOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxPoststufOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataRxPoststufOctets.setUnits("bytes")
_CftTcpTunnelCmdTxOctets_Type = Counter64
_CftTcpTunnelCmdTxOctets_Object = MibTableColumn
cftTcpTunnelCmdTxOctets = _CftTcpTunnelCmdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 7),
    _CftTcpTunnelCmdTxOctets_Type()
)
cftTcpTunnelCmdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxOctets.setUnits("bytes")
_CftTcpTunnelDataTxOctets_Type = Counter64
_CftTcpTunnelDataTxOctets_Object = MibTableColumn
cftTcpTunnelDataTxOctets = _CftTcpTunnelDataTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 8),
    _CftTcpTunnelDataTxOctets_Type()
)
cftTcpTunnelDataTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxOctets.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxOctets.setUnits("bytes")
_CftTcpTunnelCmdTxPkts_Type = Counter32
_CftTcpTunnelCmdTxPkts_Object = MibTableColumn
cftTcpTunnelCmdTxPkts = _CftTcpTunnelCmdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 9),
    _CftTcpTunnelCmdTxPkts_Type()
)
cftTcpTunnelCmdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxPkts.setUnits("packets")
_CftTcpTunnelDataTxPkts_Type = Counter32
_CftTcpTunnelDataTxPkts_Object = MibTableColumn
cftTcpTunnelDataTxPkts = _CftTcpTunnelDataTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 10),
    _CftTcpTunnelDataTxPkts_Type()
)
cftTcpTunnelDataTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxPkts.setUnits("packets")
_CftTcpTunnelCmdTxDrops_Type = Counter32
_CftTcpTunnelCmdTxDrops_Object = MibTableColumn
cftTcpTunnelCmdTxDrops = _CftTcpTunnelCmdTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 11),
    _CftTcpTunnelCmdTxDrops_Type()
)
cftTcpTunnelCmdTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxDrops.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelCmdTxDrops.setUnits("packets")
_CftTcpTunnelDataTxDrops_Type = Counter32
_CftTcpTunnelDataTxDrops_Object = MibTableColumn
cftTcpTunnelDataTxDrops = _CftTcpTunnelDataTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 12),
    _CftTcpTunnelDataTxDrops_Type()
)
cftTcpTunnelDataTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxDrops.setStatus("current")
if mibBuilder.loadTexts:
    cftTcpTunnelDataTxDrops.setUnits("packets")
_CftIfTcpTable_Object = MibTable
cftIfTcpTable = _CftIfTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cftIfTcpTable.setStatus("current")
_CftIfTcpEntry_Object = MibTableRow
cftIfTcpEntry = _CftIfTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1)
)
cftIfTcpEntry.setIndexNames(
    (0, "CISCO-FC-TUNNEL-MIB", "cftIfTcpIndex"),
)
if mibBuilder.loadTexts:
    cftIfTcpEntry.setStatus("current")
_CftIfTcpIndex_Type = InterfaceIndex
_CftIfTcpIndex_Object = MibTableColumn
cftIfTcpIndex = _CftIfTcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1),
    _CftIfTcpIndex_Type()
)
cftIfTcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cftIfTcpIndex.setStatus("current")
_CftIfTcpConnInit_Type = Counter32
_CftIfTcpConnInit_Object = MibTableColumn
cftIfTcpConnInit = _CftIfTcpConnInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 2),
    _CftIfTcpConnInit_Type()
)
cftIfTcpConnInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnInit.setStatus("current")
_CftIfTcpConnAccepted_Type = Counter32
_CftIfTcpConnAccepted_Object = MibTableColumn
cftIfTcpConnAccepted = _CftIfTcpConnAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 3),
    _CftIfTcpConnAccepted_Type()
)
cftIfTcpConnAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnAccepted.setStatus("current")
_CftIfTcpConnEstablished_Type = Counter32
_CftIfTcpConnEstablished_Object = MibTableColumn
cftIfTcpConnEstablished = _CftIfTcpConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 4),
    _CftIfTcpConnEstablished_Type()
)
cftIfTcpConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnEstablished.setStatus("current")
_CftIfTcpConnDrops_Type = Counter32
_CftIfTcpConnDrops_Object = MibTableColumn
cftIfTcpConnDrops = _CftIfTcpConnDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 5),
    _CftIfTcpConnDrops_Type()
)
cftIfTcpConnDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnDrops.setStatus("current")
_CftIfTcpConnClosed_Type = Counter32
_CftIfTcpConnClosed_Object = MibTableColumn
cftIfTcpConnClosed = _CftIfTcpConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 6),
    _CftIfTcpConnClosed_Type()
)
cftIfTcpConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnClosed.setStatus("current")
_CftIfTcpTxPkts_Type = Counter32
_CftIfTcpTxPkts_Object = MibTableColumn
cftIfTcpTxPkts = _CftIfTcpTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 7),
    _CftIfTcpTxPkts_Type()
)
cftIfTcpTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxPkts.setStatus("current")
_CftIfTcpTxDataPkts_Type = Counter32
_CftIfTcpTxDataPkts_Object = MibTableColumn
cftIfTcpTxDataPkts = _CftIfTcpTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 8),
    _CftIfTcpTxDataPkts_Type()
)
cftIfTcpTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxDataPkts.setStatus("current")
_CftIfTcpTxDataOctets_Type = Counter32
_CftIfTcpTxDataOctets_Object = MibTableColumn
cftIfTcpTxDataOctets = _CftIfTcpTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 9),
    _CftIfTcpTxDataOctets_Type()
)
cftIfTcpTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxDataOctets.setStatus("current")
_CftIfTcpRetxDataPkts_Type = Counter32
_CftIfTcpRetxDataPkts_Object = MibTableColumn
cftIfTcpRetxDataPkts = _CftIfTcpRetxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 10),
    _CftIfTcpRetxDataPkts_Type()
)
cftIfTcpRetxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetxDataPkts.setStatus("current")
_CftIfTcpRetxDataOctets_Type = Counter32
_CftIfTcpRetxDataOctets_Object = MibTableColumn
cftIfTcpRetxDataOctets = _CftIfTcpRetxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 11),
    _CftIfTcpRetxDataOctets_Type()
)
cftIfTcpRetxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetxDataOctets.setStatus("current")
_CftIfTcpRxPkts_Type = Counter32
_CftIfTcpRxPkts_Object = MibTableColumn
cftIfTcpRxPkts = _CftIfTcpRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 12),
    _CftIfTcpRxPkts_Type()
)
cftIfTcpRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxPkts.setStatus("current")
_CftIfTcpRxInSequencePkts_Type = Counter32
_CftIfTcpRxInSequencePkts_Object = MibTableColumn
cftIfTcpRxInSequencePkts = _CftIfTcpRxInSequencePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 13),
    _CftIfTcpRxInSequencePkts_Type()
)
cftIfTcpRxInSequencePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxInSequencePkts.setStatus("current")
_CftIfTcpRxInSequenceOctets_Type = Counter32
_CftIfTcpRxInSequenceOctets_Object = MibTableColumn
cftIfTcpRxInSequenceOctets = _CftIfTcpRxInSequenceOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 14),
    _CftIfTcpRxInSequenceOctets_Type()
)
cftIfTcpRxInSequenceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxInSequenceOctets.setStatus("current")
_CftIfTcpRxCcksumErrPkts_Type = Counter32
_CftIfTcpRxCcksumErrPkts_Object = MibTableColumn
cftIfTcpRxCcksumErrPkts = _CftIfTcpRxCcksumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 15),
    _CftIfTcpRxCcksumErrPkts_Type()
)
cftIfTcpRxCcksumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxCcksumErrPkts.setStatus("current")
_CftIfTcpRxBadOffsetPkts_Type = Counter32
_CftIfTcpRxBadOffsetPkts_Object = MibTableColumn
cftIfTcpRxBadOffsetPkts = _CftIfTcpRxBadOffsetPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 16),
    _CftIfTcpRxBadOffsetPkts_Type()
)
cftIfTcpRxBadOffsetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxBadOffsetPkts.setStatus("current")
_CftIfTcpRxOutOfOrderPkts_Type = Counter32
_CftIfTcpRxOutOfOrderPkts_Object = MibTableColumn
cftIfTcpRxOutOfOrderPkts = _CftIfTcpRxOutOfOrderPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 17),
    _CftIfTcpRxOutOfOrderPkts_Type()
)
cftIfTcpRxOutOfOrderPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxOutOfOrderPkts.setStatus("current")
_CftIfTcpRxOutOfOrderOctets_Type = Counter32
_CftIfTcpRxOutOfOrderOctets_Object = MibTableColumn
cftIfTcpRxOutOfOrderOctets = _CftIfTcpRxOutOfOrderOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 18),
    _CftIfTcpRxOutOfOrderOctets_Type()
)
cftIfTcpRxOutOfOrderOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxOutOfOrderOctets.setStatus("current")
_CftIfTcpExtTable_Object = MibTable
cftIfTcpExtTable = _CftIfTcpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cftIfTcpExtTable.setStatus("current")
_CftIfTcpExtEntry_Object = MibTableRow
cftIfTcpExtEntry = _CftIfTcpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1)
)
cftIfTcpExtEntry.setIndexNames(
    (0, "CISCO-FC-TUNNEL-MIB", "cftIfTcpIndex"),
)
if mibBuilder.loadTexts:
    cftIfTcpExtEntry.setStatus("current")
_CftIfTcpEmbryonicConnDrops_Type = Counter32
_CftIfTcpEmbryonicConnDrops_Object = MibTableColumn
cftIfTcpEmbryonicConnDrops = _CftIfTcpEmbryonicConnDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1),
    _CftIfTcpEmbryonicConnDrops_Type()
)
cftIfTcpEmbryonicConnDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpEmbryonicConnDrops.setStatus("current")
_CftIfTcpSegsTryToGetRTT_Type = Counter32
_CftIfTcpSegsTryToGetRTT_Object = MibTableColumn
cftIfTcpSegsTryToGetRTT = _CftIfTcpSegsTryToGetRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 2),
    _CftIfTcpSegsTryToGetRTT_Type()
)
cftIfTcpSegsTryToGetRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpSegsTryToGetRTT.setStatus("current")
_CftIfTcpSegsSucceedToGetRTT_Type = Counter32
_CftIfTcpSegsSucceedToGetRTT_Object = MibTableColumn
cftIfTcpSegsSucceedToGetRTT = _CftIfTcpSegsSucceedToGetRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 3),
    _CftIfTcpSegsSucceedToGetRTT_Type()
)
cftIfTcpSegsSucceedToGetRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpSegsSucceedToGetRTT.setStatus("current")
_CftIfTcpDelayedAcksSent_Type = Counter32
_CftIfTcpDelayedAcksSent_Object = MibTableColumn
cftIfTcpDelayedAcksSent = _CftIfTcpDelayedAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 4),
    _CftIfTcpDelayedAcksSent_Type()
)
cftIfTcpDelayedAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpDelayedAcksSent.setStatus("current")
_CftIfTcpConnDroppedRxTimeout_Type = Counter32
_CftIfTcpConnDroppedRxTimeout_Object = MibTableColumn
cftIfTcpConnDroppedRxTimeout = _CftIfTcpConnDroppedRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 5),
    _CftIfTcpConnDroppedRxTimeout_Type()
)
cftIfTcpConnDroppedRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnDroppedRxTimeout.setStatus("current")
_CftIfTcpRetransmitTimeout_Type = Counter32
_CftIfTcpRetransmitTimeout_Object = MibTableColumn
cftIfTcpRetransmitTimeout = _CftIfTcpRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 6),
    _CftIfTcpRetransmitTimeout_Type()
)
cftIfTcpRetransmitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetransmitTimeout.setStatus("current")
_CftIfTcpPersistTimeout_Type = Counter32
_CftIfTcpPersistTimeout_Object = MibTableColumn
cftIfTcpPersistTimeout = _CftIfTcpPersistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 7),
    _CftIfTcpPersistTimeout_Type()
)
cftIfTcpPersistTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpPersistTimeout.setStatus("current")
_CftIfTcpKeepaliveTimeout_Type = Counter32
_CftIfTcpKeepaliveTimeout_Object = MibTableColumn
cftIfTcpKeepaliveTimeout = _CftIfTcpKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 8),
    _CftIfTcpKeepaliveTimeout_Type()
)
cftIfTcpKeepaliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpKeepaliveTimeout.setStatus("current")
_CftIfTcpKeepaliveProbesSent_Type = Counter32
_CftIfTcpKeepaliveProbesSent_Object = MibTableColumn
cftIfTcpKeepaliveProbesSent = _CftIfTcpKeepaliveProbesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 9),
    _CftIfTcpKeepaliveProbesSent_Type()
)
cftIfTcpKeepaliveProbesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpKeepaliveProbesSent.setStatus("current")
_CftIfTcpConnDroppedInKeepalive_Type = Counter32
_CftIfTcpConnDroppedInKeepalive_Object = MibTableColumn
cftIfTcpConnDroppedInKeepalive = _CftIfTcpConnDroppedInKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 10),
    _CftIfTcpConnDroppedInKeepalive_Type()
)
cftIfTcpConnDroppedInKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnDroppedInKeepalive.setStatus("current")
_CftIfTcpConnDroppedInPersist_Type = Counter32
_CftIfTcpConnDroppedInPersist_Object = MibTableColumn
cftIfTcpConnDroppedInPersist = _CftIfTcpConnDroppedInPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 11),
    _CftIfTcpConnDroppedInPersist_Type()
)
cftIfTcpConnDroppedInPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnDroppedInPersist.setStatus("current")
_CftIfTcpConnDrainedByNoMemory_Type = Counter32
_CftIfTcpConnDrainedByNoMemory_Object = MibTableColumn
cftIfTcpConnDrainedByNoMemory = _CftIfTcpConnDrainedByNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 12),
    _CftIfTcpConnDrainedByNoMemory_Type()
)
cftIfTcpConnDrainedByNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpConnDrainedByNoMemory.setStatus("current")
_CftIfTcpAckOnlyPkts_Type = Counter32
_CftIfTcpAckOnlyPkts_Object = MibTableColumn
cftIfTcpAckOnlyPkts = _CftIfTcpAckOnlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 13),
    _CftIfTcpAckOnlyPkts_Type()
)
cftIfTcpAckOnlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpAckOnlyPkts.setStatus("current")
_CftIfTcpTxWindowProbes_Type = Counter32
_CftIfTcpTxWindowProbes_Object = MibTableColumn
cftIfTcpTxWindowProbes = _CftIfTcpTxWindowProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 14),
    _CftIfTcpTxWindowProbes_Type()
)
cftIfTcpTxWindowProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxWindowProbes.setStatus("current")
_CftIfTcpTxURGPkts_Type = Counter32
_CftIfTcpTxURGPkts_Object = MibTableColumn
cftIfTcpTxURGPkts = _CftIfTcpTxURGPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 15),
    _CftIfTcpTxURGPkts_Type()
)
cftIfTcpTxURGPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxURGPkts.setStatus("current")
_CftIfTcpTxWindowUpdateOnlyPkts_Type = Counter32
_CftIfTcpTxWindowUpdateOnlyPkts_Object = MibTableColumn
cftIfTcpTxWindowUpdateOnlyPkts = _CftIfTcpTxWindowUpdateOnlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 16),
    _CftIfTcpTxWindowUpdateOnlyPkts_Type()
)
cftIfTcpTxWindowUpdateOnlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxWindowUpdateOnlyPkts.setStatus("current")
_CftIfTcpTxControlPkts_Type = Counter32
_CftIfTcpTxControlPkts_Object = MibTableColumn
cftIfTcpTxControlPkts = _CftIfTcpTxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 17),
    _CftIfTcpTxControlPkts_Type()
)
cftIfTcpTxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxControlPkts.setStatus("current")
_CftIfTcpRxDroppedByNoMemory_Type = Counter32
_CftIfTcpRxDroppedByNoMemory_Object = MibTableColumn
cftIfTcpRxDroppedByNoMemory = _CftIfTcpRxDroppedByNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 18),
    _CftIfTcpRxDroppedByNoMemory_Type()
)
cftIfTcpRxDroppedByNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDroppedByNoMemory.setStatus("current")
_CftIfTcpRxTooShort_Type = Counter32
_CftIfTcpRxTooShort_Object = MibTableColumn
cftIfTcpRxTooShort = _CftIfTcpRxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 19),
    _CftIfTcpRxTooShort_Type()
)
cftIfTcpRxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxTooShort.setStatus("current")
_CftIfTcpRxDupOnlyPkts_Type = Counter32
_CftIfTcpRxDupOnlyPkts_Object = MibTableColumn
cftIfTcpRxDupOnlyPkts = _CftIfTcpRxDupOnlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 20),
    _CftIfTcpRxDupOnlyPkts_Type()
)
cftIfTcpRxDupOnlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDupOnlyPkts.setStatus("current")
_CftIfTcpRxDupOnlyOctets_Type = Counter32
_CftIfTcpRxDupOnlyOctets_Object = MibTableColumn
cftIfTcpRxDupOnlyOctets = _CftIfTcpRxDupOnlyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 21),
    _CftIfTcpRxDupOnlyOctets_Type()
)
cftIfTcpRxDupOnlyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDupOnlyOctets.setStatus("current")
_CftIfTcpRxDupDataPkts_Type = Counter32
_CftIfTcpRxDupDataPkts_Object = MibTableColumn
cftIfTcpRxDupDataPkts = _CftIfTcpRxDupDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 22),
    _CftIfTcpRxDupDataPkts_Type()
)
cftIfTcpRxDupDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDupDataPkts.setStatus("current")
_CftIfTcpRxDupOctetsInPartDupPkts_Type = Counter32
_CftIfTcpRxDupOctetsInPartDupPkts_Object = MibTableColumn
cftIfTcpRxDupOctetsInPartDupPkts = _CftIfTcpRxDupOctetsInPartDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 23),
    _CftIfTcpRxDupOctetsInPartDupPkts_Type()
)
cftIfTcpRxDupOctetsInPartDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDupOctetsInPartDupPkts.setStatus("current")
_CftIfTcpRxDataAfterWindowPkts_Type = Counter32
_CftIfTcpRxDataAfterWindowPkts_Object = MibTableColumn
cftIfTcpRxDataAfterWindowPkts = _CftIfTcpRxDataAfterWindowPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 24),
    _CftIfTcpRxDataAfterWindowPkts_Type()
)
cftIfTcpRxDataAfterWindowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDataAfterWindowPkts.setStatus("current")
_CftIfTcpRxDataAfterWindowOctets_Type = Counter32
_CftIfTcpRxDataAfterWindowOctets_Object = MibTableColumn
cftIfTcpRxDataAfterWindowOctets = _CftIfTcpRxDataAfterWindowOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 25),
    _CftIfTcpRxDataAfterWindowOctets_Type()
)
cftIfTcpRxDataAfterWindowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDataAfterWindowOctets.setStatus("current")
_CftIfTcpRxPktsAfterConnClose_Type = Counter32
_CftIfTcpRxPktsAfterConnClose_Object = MibTableColumn
cftIfTcpRxPktsAfterConnClose = _CftIfTcpRxPktsAfterConnClose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 26),
    _CftIfTcpRxPktsAfterConnClose_Type()
)
cftIfTcpRxPktsAfterConnClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxPktsAfterConnClose.setStatus("current")
_CftIfTcpRxWindowProbesPkts_Type = Counter32
_CftIfTcpRxWindowProbesPkts_Object = MibTableColumn
cftIfTcpRxWindowProbesPkts = _CftIfTcpRxWindowProbesPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 27),
    _CftIfTcpRxWindowProbesPkts_Type()
)
cftIfTcpRxWindowProbesPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxWindowProbesPkts.setStatus("current")
_CftIfTcpRxDupAcks_Type = Counter32
_CftIfTcpRxDupAcks_Object = MibTableColumn
cftIfTcpRxDupAcks = _CftIfTcpRxDupAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 28),
    _CftIfTcpRxDupAcks_Type()
)
cftIfTcpRxDupAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxDupAcks.setStatus("current")
_CftIfTcpRxAcksForUnsentData_Type = Counter32
_CftIfTcpRxAcksForUnsentData_Object = MibTableColumn
cftIfTcpRxAcksForUnsentData = _CftIfTcpRxAcksForUnsentData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 29),
    _CftIfTcpRxAcksForUnsentData_Type()
)
cftIfTcpRxAcksForUnsentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxAcksForUnsentData.setStatus("current")
_CftIfTcpRxAcksPkts_Type = Counter32
_CftIfTcpRxAcksPkts_Object = MibTableColumn
cftIfTcpRxAcksPkts = _CftIfTcpRxAcksPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 30),
    _CftIfTcpRxAcksPkts_Type()
)
cftIfTcpRxAcksPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxAcksPkts.setStatus("current")
_CftIfTcpOctetAckedByRxAcks_Type = Counter32
_CftIfTcpOctetAckedByRxAcks_Object = MibTableColumn
cftIfTcpOctetAckedByRxAcks = _CftIfTcpOctetAckedByRxAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 31),
    _CftIfTcpOctetAckedByRxAcks_Type()
)
cftIfTcpOctetAckedByRxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpOctetAckedByRxAcks.setStatus("current")
_CftIfTcpRxWindowUpdatePkts_Type = Counter32
_CftIfTcpRxWindowUpdatePkts_Object = MibTableColumn
cftIfTcpRxWindowUpdatePkts = _CftIfTcpRxWindowUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 32),
    _CftIfTcpRxWindowUpdatePkts_Type()
)
cftIfTcpRxWindowUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRxWindowUpdatePkts.setStatus("current")
_CftIfTcpSegDropByPAWS_Type = Counter32
_CftIfTcpSegDropByPAWS_Object = MibTableColumn
cftIfTcpSegDropByPAWS = _CftIfTcpSegDropByPAWS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 33),
    _CftIfTcpSegDropByPAWS_Type()
)
cftIfTcpSegDropByPAWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpSegDropByPAWS.setStatus("current")
_CftIfTcpTxSackFackDataPkts_Type = Counter32
_CftIfTcpTxSackFackDataPkts_Object = MibTableColumn
cftIfTcpTxSackFackDataPkts = _CftIfTcpTxSackFackDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 34),
    _CftIfTcpTxSackFackDataPkts_Type()
)
cftIfTcpTxSackFackDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxSackFackDataPkts.setStatus("current")
_CftIfTcpTxSackFackDataOctets_Type = Counter32
_CftIfTcpTxSackFackDataOctets_Object = MibTableColumn
cftIfTcpTxSackFackDataOctets = _CftIfTcpTxSackFackDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 35),
    _CftIfTcpTxSackFackDataOctets_Type()
)
cftIfTcpTxSackFackDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpTxSackFackDataOctets.setStatus("current")
_CftIfTcpRetxSackFackDataPkts_Type = Counter32
_CftIfTcpRetxSackFackDataPkts_Object = MibTableColumn
cftIfTcpRetxSackFackDataPkts = _CftIfTcpRetxSackFackDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 36),
    _CftIfTcpRetxSackFackDataPkts_Type()
)
cftIfTcpRetxSackFackDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetxSackFackDataPkts.setStatus("current")
_CftIfTcpRetxSackFackDataOctets_Type = Counter32
_CftIfTcpRetxSackFackDataOctets_Object = MibTableColumn
cftIfTcpRetxSackFackDataOctets = _CftIfTcpRetxSackFackDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 37),
    _CftIfTcpRetxSackFackDataOctets_Type()
)
cftIfTcpRetxSackFackDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetxSackFackDataOctets.setStatus("current")
_CftIfTcpSackFackConnClosed_Type = Counter32
_CftIfTcpSackFackConnClosed_Object = MibTableColumn
cftIfTcpSackFackConnClosed = _CftIfTcpSackFackConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 38),
    _CftIfTcpSackFackConnClosed_Type()
)
cftIfTcpSackFackConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpSackFackConnClosed.setStatus("current")
_CftIfTcpRetxSackFackTimeouts_Type = Counter32
_CftIfTcpRetxSackFackTimeouts_Object = MibTableColumn
cftIfTcpRetxSackFackTimeouts = _CftIfTcpRetxSackFackTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 39),
    _CftIfTcpRetxSackFackTimeouts_Type()
)
cftIfTcpRetxSackFackTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpRetxSackFackTimeouts.setStatus("current")
_CftIfTcpHdrPredictOkForAcks_Type = Counter32
_CftIfTcpHdrPredictOkForAcks_Object = MibTableColumn
cftIfTcpHdrPredictOkForAcks = _CftIfTcpHdrPredictOkForAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 40),
    _CftIfTcpHdrPredictOkForAcks_Type()
)
cftIfTcpHdrPredictOkForAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpHdrPredictOkForAcks.setStatus("current")
_CftIfTcpHdrPredictOkForDataPkts_Type = Counter32
_CftIfTcpHdrPredictOkForDataPkts_Object = MibTableColumn
cftIfTcpHdrPredictOkForDataPkts = _CftIfTcpHdrPredictOkForDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 41),
    _CftIfTcpHdrPredictOkForDataPkts_Type()
)
cftIfTcpHdrPredictOkForDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cftIfTcpHdrPredictOkForDataPkts.setStatus("current")
_CiscoFCTunnelMIBConform_ObjectIdentity = ObjectIdentity
ciscoFCTunnelMIBConform = _CiscoFCTunnelMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2)
)
_CftTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
cftTunnelMIBCompliances = _CftTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1)
)
_CftTunnelMIBGroups_ObjectIdentity = ObjectIdentity
cftTunnelMIBGroups = _CftTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2)
)

# Managed Objects groups

cftTcpTunnelConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)
)
cftTcpTunnelConfigGroup.setObjects(
      *(("CISCO-FC-TUNNEL-MIB", "cftMaxTcpTunnels"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelSrcIpType"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelSrcIp"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDestIpType"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDestIp"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdSrcPort"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdDestPort"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataSrcPort"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataDestPort"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdMWS"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataMWS"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdKeepAliveTime"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataKeepAliveTime"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdSelectiveAck"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataSelectiveAck"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdConnectStatus"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataConnectStatus"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelOperStatus"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelStatus"))
)
if mibBuilder.loadTexts:
    cftTcpTunnelConfigGroup.setStatus("current")

cftTcpTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)
)
cftTcpTunnelStatGroup.setObjects(
      *(("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdRxSegmentOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataRxSegmentOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdRxPrestufOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataRxPrestufOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdRxPoststufOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataRxPoststufOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdTxOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataTxOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdTxPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataTxPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelCmdTxDrops"),
        ("CISCO-FC-TUNNEL-MIB", "cftTcpTunnelDataTxDrops"))
)
if mibBuilder.loadTexts:
    cftTcpTunnelStatGroup.setStatus("current")

cftIfTcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)
)
cftIfTcpGroup.setObjects(
      *(("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnInit"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnAccepted"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnEstablished"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnDrops"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnClosed"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxDataPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxDataOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetxDataPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetxDataOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxInSequencePkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxInSequenceOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxCcksumErrPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxBadOffsetPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxOutOfOrderPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxOutOfOrderOctets"))
)
if mibBuilder.loadTexts:
    cftIfTcpGroup.setStatus("current")

cftIfTcpExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)
)
cftIfTcpExtGroup.setObjects(
      *(("CISCO-FC-TUNNEL-MIB", "cftIfTcpEmbryonicConnDrops"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpSegsTryToGetRTT"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpSegsSucceedToGetRTT"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpDelayedAcksSent"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnDroppedRxTimeout"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetransmitTimeout"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpPersistTimeout"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpKeepaliveTimeout"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpKeepaliveProbesSent"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnDroppedInKeepalive"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnDroppedInPersist"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpConnDrainedByNoMemory"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpAckOnlyPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxWindowProbes"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxURGPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxWindowUpdateOnlyPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxControlPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDroppedByNoMemory"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxTooShort"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDupOnlyPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDupOnlyOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDupDataPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDupOctetsInPartDupPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDataAfterWindowPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDataAfterWindowOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxPktsAfterConnClose"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxWindowProbesPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxDupAcks"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxAcksForUnsentData"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxAcksPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpOctetAckedByRxAcks"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRxWindowUpdatePkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpSegDropByPAWS"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxSackFackDataPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpTxSackFackDataOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetxSackFackDataPkts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetxSackFackDataOctets"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpSackFackConnClosed"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpRetxSackFackTimeouts"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpHdrPredictOkForAcks"),
        ("CISCO-FC-TUNNEL-MIB", "cftIfTcpHdrPredictOkForDataPkts"))
)
if mibBuilder.loadTexts:
    cftIfTcpExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cftTunnelMIBComplianceV01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cftTunnelMIBComplianceV01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-TUNNEL-MIB",
    **{"ciscoFiberChannelTunnelMIB": ciscoFiberChannelTunnelMIB,
       "ciscoFCTunnelMIBNotifi": ciscoFCTunnelMIBNotifi,
       "ciscoFCTunnelMIBObjects": ciscoFCTunnelMIBObjects,
       "cftTcpTunnelObjects": cftTcpTunnelObjects,
       "cftMaxTcpTunnels": cftMaxTcpTunnels,
       "cftTcpTunnelTable": cftTcpTunnelTable,
       "cftTcpTunnelEntry": cftTcpTunnelEntry,
       "cftFiberChannelIf": cftFiberChannelIf,
       "cftTcpTunnelName": cftTcpTunnelName,
       "cftTcpTunnelSrcIpType": cftTcpTunnelSrcIpType,
       "cftTcpTunnelSrcIp": cftTcpTunnelSrcIp,
       "cftTcpTunnelDestIpType": cftTcpTunnelDestIpType,
       "cftTcpTunnelDestIp": cftTcpTunnelDestIp,
       "cftTcpTunnelCmdSrcPort": cftTcpTunnelCmdSrcPort,
       "cftTcpTunnelCmdDestPort": cftTcpTunnelCmdDestPort,
       "cftTcpTunnelDataSrcPort": cftTcpTunnelDataSrcPort,
       "cftTcpTunnelDataDestPort": cftTcpTunnelDataDestPort,
       "cftTcpTunnelCmdMWS": cftTcpTunnelCmdMWS,
       "cftTcpTunnelDataMWS": cftTcpTunnelDataMWS,
       "cftTcpTunnelCmdKeepAliveTime": cftTcpTunnelCmdKeepAliveTime,
       "cftTcpTunnelDataKeepAliveTime": cftTcpTunnelDataKeepAliveTime,
       "cftTcpTunnelCmdSelectiveAck": cftTcpTunnelCmdSelectiveAck,
       "cftTcpTunnelDataSelectiveAck": cftTcpTunnelDataSelectiveAck,
       "cftTcpTunnelCmdConnectStatus": cftTcpTunnelCmdConnectStatus,
       "cftTcpTunnelDataConnectStatus": cftTcpTunnelDataConnectStatus,
       "cftTcpTunnelOperStatus": cftTcpTunnelOperStatus,
       "cftTcpTunnelStatus": cftTcpTunnelStatus,
       "cftTcpTunnelStatsTable": cftTcpTunnelStatsTable,
       "cftTcpTunnelStatsEntry": cftTcpTunnelStatsEntry,
       "cftTcpTunnelCmdRxSegmentOctets": cftTcpTunnelCmdRxSegmentOctets,
       "cftTcpTunnelDataRxSegmentOctets": cftTcpTunnelDataRxSegmentOctets,
       "cftTcpTunnelCmdRxPrestufOctets": cftTcpTunnelCmdRxPrestufOctets,
       "cftTcpTunnelDataRxPrestufOctets": cftTcpTunnelDataRxPrestufOctets,
       "cftTcpTunnelCmdRxPoststufOctets": cftTcpTunnelCmdRxPoststufOctets,
       "cftTcpTunnelDataRxPoststufOctets": cftTcpTunnelDataRxPoststufOctets,
       "cftTcpTunnelCmdTxOctets": cftTcpTunnelCmdTxOctets,
       "cftTcpTunnelDataTxOctets": cftTcpTunnelDataTxOctets,
       "cftTcpTunnelCmdTxPkts": cftTcpTunnelCmdTxPkts,
       "cftTcpTunnelDataTxPkts": cftTcpTunnelDataTxPkts,
       "cftTcpTunnelCmdTxDrops": cftTcpTunnelCmdTxDrops,
       "cftTcpTunnelDataTxDrops": cftTcpTunnelDataTxDrops,
       "cftIfTcpTable": cftIfTcpTable,
       "cftIfTcpEntry": cftIfTcpEntry,
       "cftIfTcpIndex": cftIfTcpIndex,
       "cftIfTcpConnInit": cftIfTcpConnInit,
       "cftIfTcpConnAccepted": cftIfTcpConnAccepted,
       "cftIfTcpConnEstablished": cftIfTcpConnEstablished,
       "cftIfTcpConnDrops": cftIfTcpConnDrops,
       "cftIfTcpConnClosed": cftIfTcpConnClosed,
       "cftIfTcpTxPkts": cftIfTcpTxPkts,
       "cftIfTcpTxDataPkts": cftIfTcpTxDataPkts,
       "cftIfTcpTxDataOctets": cftIfTcpTxDataOctets,
       "cftIfTcpRetxDataPkts": cftIfTcpRetxDataPkts,
       "cftIfTcpRetxDataOctets": cftIfTcpRetxDataOctets,
       "cftIfTcpRxPkts": cftIfTcpRxPkts,
       "cftIfTcpRxInSequencePkts": cftIfTcpRxInSequencePkts,
       "cftIfTcpRxInSequenceOctets": cftIfTcpRxInSequenceOctets,
       "cftIfTcpRxCcksumErrPkts": cftIfTcpRxCcksumErrPkts,
       "cftIfTcpRxBadOffsetPkts": cftIfTcpRxBadOffsetPkts,
       "cftIfTcpRxOutOfOrderPkts": cftIfTcpRxOutOfOrderPkts,
       "cftIfTcpRxOutOfOrderOctets": cftIfTcpRxOutOfOrderOctets,
       "cftIfTcpExtTable": cftIfTcpExtTable,
       "cftIfTcpExtEntry": cftIfTcpExtEntry,
       "cftIfTcpEmbryonicConnDrops": cftIfTcpEmbryonicConnDrops,
       "cftIfTcpSegsTryToGetRTT": cftIfTcpSegsTryToGetRTT,
       "cftIfTcpSegsSucceedToGetRTT": cftIfTcpSegsSucceedToGetRTT,
       "cftIfTcpDelayedAcksSent": cftIfTcpDelayedAcksSent,
       "cftIfTcpConnDroppedRxTimeout": cftIfTcpConnDroppedRxTimeout,
       "cftIfTcpRetransmitTimeout": cftIfTcpRetransmitTimeout,
       "cftIfTcpPersistTimeout": cftIfTcpPersistTimeout,
       "cftIfTcpKeepaliveTimeout": cftIfTcpKeepaliveTimeout,
       "cftIfTcpKeepaliveProbesSent": cftIfTcpKeepaliveProbesSent,
       "cftIfTcpConnDroppedInKeepalive": cftIfTcpConnDroppedInKeepalive,
       "cftIfTcpConnDroppedInPersist": cftIfTcpConnDroppedInPersist,
       "cftIfTcpConnDrainedByNoMemory": cftIfTcpConnDrainedByNoMemory,
       "cftIfTcpAckOnlyPkts": cftIfTcpAckOnlyPkts,
       "cftIfTcpTxWindowProbes": cftIfTcpTxWindowProbes,
       "cftIfTcpTxURGPkts": cftIfTcpTxURGPkts,
       "cftIfTcpTxWindowUpdateOnlyPkts": cftIfTcpTxWindowUpdateOnlyPkts,
       "cftIfTcpTxControlPkts": cftIfTcpTxControlPkts,
       "cftIfTcpRxDroppedByNoMemory": cftIfTcpRxDroppedByNoMemory,
       "cftIfTcpRxTooShort": cftIfTcpRxTooShort,
       "cftIfTcpRxDupOnlyPkts": cftIfTcpRxDupOnlyPkts,
       "cftIfTcpRxDupOnlyOctets": cftIfTcpRxDupOnlyOctets,
       "cftIfTcpRxDupDataPkts": cftIfTcpRxDupDataPkts,
       "cftIfTcpRxDupOctetsInPartDupPkts": cftIfTcpRxDupOctetsInPartDupPkts,
       "cftIfTcpRxDataAfterWindowPkts": cftIfTcpRxDataAfterWindowPkts,
       "cftIfTcpRxDataAfterWindowOctets": cftIfTcpRxDataAfterWindowOctets,
       "cftIfTcpRxPktsAfterConnClose": cftIfTcpRxPktsAfterConnClose,
       "cftIfTcpRxWindowProbesPkts": cftIfTcpRxWindowProbesPkts,
       "cftIfTcpRxDupAcks": cftIfTcpRxDupAcks,
       "cftIfTcpRxAcksForUnsentData": cftIfTcpRxAcksForUnsentData,
       "cftIfTcpRxAcksPkts": cftIfTcpRxAcksPkts,
       "cftIfTcpOctetAckedByRxAcks": cftIfTcpOctetAckedByRxAcks,
       "cftIfTcpRxWindowUpdatePkts": cftIfTcpRxWindowUpdatePkts,
       "cftIfTcpSegDropByPAWS": cftIfTcpSegDropByPAWS,
       "cftIfTcpTxSackFackDataPkts": cftIfTcpTxSackFackDataPkts,
       "cftIfTcpTxSackFackDataOctets": cftIfTcpTxSackFackDataOctets,
       "cftIfTcpRetxSackFackDataPkts": cftIfTcpRetxSackFackDataPkts,
       "cftIfTcpRetxSackFackDataOctets": cftIfTcpRetxSackFackDataOctets,
       "cftIfTcpSackFackConnClosed": cftIfTcpSackFackConnClosed,
       "cftIfTcpRetxSackFackTimeouts": cftIfTcpRetxSackFackTimeouts,
       "cftIfTcpHdrPredictOkForAcks": cftIfTcpHdrPredictOkForAcks,
       "cftIfTcpHdrPredictOkForDataPkts": cftIfTcpHdrPredictOkForDataPkts,
       "ciscoFCTunnelMIBConform": ciscoFCTunnelMIBConform,
       "cftTunnelMIBCompliances": cftTunnelMIBCompliances,
       "cftTunnelMIBComplianceV01": cftTunnelMIBComplianceV01,
       "cftTunnelMIBGroups": cftTunnelMIBGroups,
       "cftTcpTunnelConfigGroup": cftTcpTunnelConfigGroup,
       "cftTcpTunnelStatGroup": cftTcpTunnelStatGroup,
       "cftIfTcpGroup": cftIfTcpGroup,
       "cftIfTcpExtGroup": cftIfTcpExtGroup}
)
