# SNMP MIB module (HP-ICF-VIRTUAL-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-VIRTUAL-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:28 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(tunnelIfAddressType,
 tunnelIfEntry,
 tunnelIfLocalInetAddress,
 tunnelIfRemoteInetAddress) = mibBuilder.importSymbols(
    "TUNNEL-MIB",
    "tunnelIfAddressType",
    "tunnelIfEntry",
    "tunnelIfLocalInetAddress",
    "tunnelIfRemoteInetAddress")


# MODULE-IDENTITY

hpicfVirtualNetwork = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107)
)
hpicfVirtualNetwork.setRevisions(
        ("2014-03-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfVirtualNetworkNotifications_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkNotifications = _HpicfVirtualNetworkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 0)
)
_HpicfVirtualNetworkObjects_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkObjects = _HpicfVirtualNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1)
)
_HpicfVirtualNetworkScalars_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkScalars = _HpicfVirtualNetworkScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1)
)
_HpicfMaxVirtualNetworks_Type = Unsigned32
_HpicfMaxVirtualNetworks_Object = MibScalar
hpicfMaxVirtualNetworks = _HpicfMaxVirtualNetworks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1, 1),
    _HpicfMaxVirtualNetworks_Type()
)
hpicfMaxVirtualNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMaxVirtualNetworks.setStatus("current")
_HpicfTotalVirtualNetworks_Type = Unsigned32
_HpicfTotalVirtualNetworks_Object = MibScalar
hpicfTotalVirtualNetworks = _HpicfTotalVirtualNetworks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 1, 2),
    _HpicfTotalVirtualNetworks_Type()
)
hpicfTotalVirtualNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTotalVirtualNetworks.setStatus("current")
_HpicfVirtualNetworkTable_Object = MibTable
hpicfVirtualNetworkTable = _HpicfVirtualNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkTable.setStatus("current")
_HpicfVirtualNetworkEntry_Object = MibTableRow
hpicfVirtualNetworkEntry = _HpicfVirtualNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1)
)
hpicfVirtualNetworkEntry.setIndexNames(
    (0, "HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkID"),
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkEntry.setStatus("current")


class _HpicfVirtualNetworkID_Type(Integer32):
    """Custom type hpicfVirtualNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HpicfVirtualNetworkID_Type.__name__ = "Integer32"
_HpicfVirtualNetworkID_Object = MibTableColumn
hpicfVirtualNetworkID = _HpicfVirtualNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 1),
    _HpicfVirtualNetworkID_Type()
)
hpicfVirtualNetworkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVirtualNetworkID.setStatus("current")
_HpicfVirtualNetworkName_Type = SnmpAdminString
_HpicfVirtualNetworkName_Object = MibTableColumn
hpicfVirtualNetworkName = _HpicfVirtualNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 2),
    _HpicfVirtualNetworkName_Type()
)
hpicfVirtualNetworkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVirtualNetworkName.setStatus("current")
_HpicfVirtualNetworkVLANID_Type = VlanIndex
_HpicfVirtualNetworkVLANID_Object = MibTableColumn
hpicfVirtualNetworkVLANID = _HpicfVirtualNetworkVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 3),
    _HpicfVirtualNetworkVLANID_Type()
)
hpicfVirtualNetworkVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVirtualNetworkVLANID.setStatus("current")
_HpicfVirtualNetworkRowStatus_Type = RowStatus
_HpicfVirtualNetworkRowStatus_Object = MibTableColumn
hpicfVirtualNetworkRowStatus = _HpicfVirtualNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 2, 1, 4),
    _HpicfVirtualNetworkRowStatus_Type()
)
hpicfVirtualNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVirtualNetworkRowStatus.setStatus("current")
_HpicfVirtualNetworkNotifyScalars_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkNotifyScalars = _HpicfVirtualNetworkNotifyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3)
)
_HpicfMTUDropRouterAddrType_Type = InetAddressType
_HpicfMTUDropRouterAddrType_Object = MibScalar
hpicfMTUDropRouterAddrType = _HpicfMTUDropRouterAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 1),
    _HpicfMTUDropRouterAddrType_Type()
)
hpicfMTUDropRouterAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropRouterAddrType.setStatus("current")
_HpicfMTUDropRouterAddr_Type = InetAddress
_HpicfMTUDropRouterAddr_Object = MibScalar
hpicfMTUDropRouterAddr = _HpicfMTUDropRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 2),
    _HpicfMTUDropRouterAddr_Type()
)
hpicfMTUDropRouterAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropRouterAddr.setStatus("current")
_HpicfMTUDropRouterMTU_Type = Integer32
_HpicfMTUDropRouterMTU_Object = MibScalar
hpicfMTUDropRouterMTU = _HpicfMTUDropRouterMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 3),
    _HpicfMTUDropRouterMTU_Type()
)
hpicfMTUDropRouterMTU.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropRouterMTU.setStatus("current")
_HpicfMTUDropVTEPSrcAddrType_Type = InetAddressType
_HpicfMTUDropVTEPSrcAddrType_Object = MibScalar
hpicfMTUDropVTEPSrcAddrType = _HpicfMTUDropVTEPSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 4),
    _HpicfMTUDropVTEPSrcAddrType_Type()
)
hpicfMTUDropVTEPSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropVTEPSrcAddrType.setStatus("current")
_HpicfMTUDropVTEPSource_Type = InetAddress
_HpicfMTUDropVTEPSource_Object = MibScalar
hpicfMTUDropVTEPSource = _HpicfMTUDropVTEPSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 5),
    _HpicfMTUDropVTEPSource_Type()
)
hpicfMTUDropVTEPSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropVTEPSource.setStatus("current")
_HpicfMTUDropVTEPDstAddrType_Type = InetAddressType
_HpicfMTUDropVTEPDstAddrType_Object = MibScalar
hpicfMTUDropVTEPDstAddrType = _HpicfMTUDropVTEPDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 6),
    _HpicfMTUDropVTEPDstAddrType_Type()
)
hpicfMTUDropVTEPDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropVTEPDstAddrType.setStatus("current")
_HpicfMTUDropVTEPDest_Type = InetAddress
_HpicfMTUDropVTEPDest_Object = MibScalar
hpicfMTUDropVTEPDest = _HpicfMTUDropVTEPDest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 7),
    _HpicfMTUDropVTEPDest_Type()
)
hpicfMTUDropVTEPDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropVTEPDest.setStatus("current")
_HpicfMTUDropInIfIndex_Type = InterfaceIndex
_HpicfMTUDropInIfIndex_Object = MibScalar
hpicfMTUDropInIfIndex = _HpicfMTUDropInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 8),
    _HpicfMTUDropInIfIndex_Type()
)
hpicfMTUDropInIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfMTUDropInIfIndex.setStatus("current")


class _HpicfMTUDropNotifyEnable_Type(Integer32):
    """Custom type hpicfMTUDropNotifyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfMTUDropNotifyEnable_Type.__name__ = "Integer32"
_HpicfMTUDropNotifyEnable_Object = MibScalar
hpicfMTUDropNotifyEnable = _HpicfMTUDropNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 1, 3, 9),
    _HpicfMTUDropNotifyEnable_Type()
)
hpicfMTUDropNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMTUDropNotifyEnable.setStatus("current")
_HpicfTunnelObjects_ObjectIdentity = ObjectIdentity
hpicfTunnelObjects = _HpicfTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2)
)
_HpicfVXLANTunnelObjects_ObjectIdentity = ObjectIdentity
hpicfVXLANTunnelObjects = _HpicfVXLANTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1)
)
_HpicfVXLANTunnelConfigObjects_ObjectIdentity = ObjectIdentity
hpicfVXLANTunnelConfigObjects = _HpicfVXLANTunnelConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1)
)
_HpicfVXLANTunnelIfTable_Object = MibTable
hpicfVXLANTunnelIfTable = _HpicfVXLANTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfTable.setStatus("current")
_HpicfVXLANTunnelIfEntry_Object = MibTableRow
hpicfVXLANTunnelIfEntry = _HpicfVXLANTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfEntry.setStatus("current")


class _HpicfVXLANTunnelIfDownReason_Type(Integer32):
    """Custom type hpicfVXLANTunnelIfDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ifAdminDown", 1),
          ("none", 0),
          ("resourceUnavailable", 3),
          ("tepNotReachable", 2))
    )


_HpicfVXLANTunnelIfDownReason_Type.__name__ = "Integer32"
_HpicfVXLANTunnelIfDownReason_Object = MibTableColumn
hpicfVXLANTunnelIfDownReason = _HpicfVXLANTunnelIfDownReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 1),
    _HpicfVXLANTunnelIfDownReason_Type()
)
hpicfVXLANTunnelIfDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfDownReason.setStatus("current")
_HpicfVXLANTunnelIfNextHopIpType_Type = InetAddressType
_HpicfVXLANTunnelIfNextHopIpType_Object = MibTableColumn
hpicfVXLANTunnelIfNextHopIpType = _HpicfVXLANTunnelIfNextHopIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 2),
    _HpicfVXLANTunnelIfNextHopIpType_Type()
)
hpicfVXLANTunnelIfNextHopIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfNextHopIpType.setStatus("current")
_HpicfVXLANTunnelIfNextHopIp_Type = InetAddress
_HpicfVXLANTunnelIfNextHopIp_Object = MibTableColumn
hpicfVXLANTunnelIfNextHopIp = _HpicfVXLANTunnelIfNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 3),
    _HpicfVXLANTunnelIfNextHopIp_Type()
)
hpicfVXLANTunnelIfNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfNextHopIp.setStatus("current")
_HpicfVXLANTunnelIfNextHopInterface_Type = DisplayString
_HpicfVXLANTunnelIfNextHopInterface_Object = MibTableColumn
hpicfVXLANTunnelIfNextHopInterface = _HpicfVXLANTunnelIfNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 4),
    _HpicfVXLANTunnelIfNextHopInterface_Type()
)
hpicfVXLANTunnelIfNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfNextHopInterface.setStatus("current")
_HpicfVXLANTunnelIfNextHopPortName_Type = DisplayString
_HpicfVXLANTunnelIfNextHopPortName_Object = MibTableColumn
hpicfVXLANTunnelIfNextHopPortName = _HpicfVXLANTunnelIfNextHopPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 5),
    _HpicfVXLANTunnelIfNextHopPortName_Type()
)
hpicfVXLANTunnelIfNextHopPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelIfNextHopPortName.setStatus("current")
_HpicfVXLANTunnelStatsRxPackets_Type = Counter64
_HpicfVXLANTunnelStatsRxPackets_Object = MibTableColumn
hpicfVXLANTunnelStatsRxPackets = _HpicfVXLANTunnelStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 6),
    _HpicfVXLANTunnelStatsRxPackets_Type()
)
hpicfVXLANTunnelStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelStatsRxPackets.setStatus("current")
_HpicfVXLANTunnelStatsTxPackets_Type = Counter32
_HpicfVXLANTunnelStatsTxPackets_Object = MibTableColumn
hpicfVXLANTunnelStatsTxPackets = _HpicfVXLANTunnelStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 7),
    _HpicfVXLANTunnelStatsTxPackets_Type()
)
hpicfVXLANTunnelStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelStatsTxPackets.setStatus("current")
_HpicfVXLANTunnelStatsClear_Type = TruthValue
_HpicfVXLANTunnelStatsClear_Object = MibTableColumn
hpicfVXLANTunnelStatsClear = _HpicfVXLANTunnelStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 1, 1, 1, 9),
    _HpicfVXLANTunnelStatsClear_Type()
)
hpicfVXLANTunnelStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelStatsClear.setStatus("current")
_HpicfVXLANTunnelScalars_ObjectIdentity = ObjectIdentity
hpicfVXLANTunnelScalars = _HpicfVXLANTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2)
)
_HpicfMaxVXLANTunnels_Type = Unsigned32
_HpicfMaxVXLANTunnels_Object = MibScalar
hpicfMaxVXLANTunnels = _HpicfMaxVXLANTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 1),
    _HpicfMaxVXLANTunnels_Type()
)
hpicfMaxVXLANTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMaxVXLANTunnels.setStatus("current")
_HpicfTotalVXLANTunnels_Type = Unsigned32
_HpicfTotalVXLANTunnels_Object = MibScalar
hpicfTotalVXLANTunnels = _HpicfTotalVXLANTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 2),
    _HpicfTotalVXLANTunnels_Type()
)
hpicfTotalVXLANTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTotalVXLANTunnels.setStatus("current")
_HpicfVXLANTunnelStatsTxMTUViolation_Type = Counter32
_HpicfVXLANTunnelStatsTxMTUViolation_Object = MibScalar
hpicfVXLANTunnelStatsTxMTUViolation = _HpicfVXLANTunnelStatsTxMTUViolation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 3),
    _HpicfVXLANTunnelStatsTxMTUViolation_Type()
)
hpicfVXLANTunnelStatsTxMTUViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelStatsTxMTUViolation.setStatus("current")
_HpicfVXLANTunnelGlobalStatsDropCount_Type = Counter64
_HpicfVXLANTunnelGlobalStatsDropCount_Object = MibScalar
hpicfVXLANTunnelGlobalStatsDropCount = _HpicfVXLANTunnelGlobalStatsDropCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 4),
    _HpicfVXLANTunnelGlobalStatsDropCount_Type()
)
hpicfVXLANTunnelGlobalStatsDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelGlobalStatsDropCount.setStatus("current")
_HpicfVXLANTunnelGlobalStatsClear_Type = TruthValue
_HpicfVXLANTunnelGlobalStatsClear_Object = MibScalar
hpicfVXLANTunnelGlobalStatsClear = _HpicfVXLANTunnelGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 5),
    _HpicfVXLANTunnelGlobalStatsClear_Type()
)
hpicfVXLANTunnelGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelGlobalStatsClear.setStatus("current")


class _HpicfVXLANTunnelEnable_Type(TruthValue):
    """Custom type hpicfVXLANTunnelEnable based on TruthValue"""


_HpicfVXLANTunnelEnable_Object = MibScalar
hpicfVXLANTunnelEnable = _HpicfVXLANTunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 6),
    _HpicfVXLANTunnelEnable_Type()
)
hpicfVXLANTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelEnable.setStatus("current")


class _HpicfVXLANTunnelUDPPort_Type(Integer32):
    """Custom type hpicfVXLANTunnelUDPPort based on Integer32"""
    defaultValue = 4789

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfVXLANTunnelUDPPort_Type.__name__ = "Integer32"
_HpicfVXLANTunnelUDPPort_Object = MibScalar
hpicfVXLANTunnelUDPPort = _HpicfVXLANTunnelUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 2, 1, 2, 7),
    _HpicfVXLANTunnelUDPPort_Type()
)
hpicfVXLANTunnelUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVXLANTunnelUDPPort.setStatus("current")
_HpicfVirtualNetworkConformance_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkConformance = _HpicfVirtualNetworkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3)
)
_HpicfVirtualNetworkCompliances_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkCompliances = _HpicfVirtualNetworkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 1)
)
_HpicfVirtualNetworkGroups_ObjectIdentity = ObjectIdentity
hpicfVirtualNetworkGroups = _HpicfVirtualNetworkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2)
)
tunnelIfEntry.registerAugmentions(
    ("HP-ICF-VIRTUAL-NETWORK-MIB",
     "hpicfVXLANTunnelIfEntry")
)
hpicfVXLANTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())

# Managed Objects groups

hpicfVirtualNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 1)
)
hpicfVirtualNetworkGroup.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkName"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkVLANID"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkGroup.setStatus("current")

hpicfVirtualNetworkScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 2)
)
hpicfVirtualNetworkScalarGroup.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMaxVirtualNetworks"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfTotalVirtualNetworks"))
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkScalarGroup.setStatus("current")

hpicfVXLANTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 3)
)
hpicfVXLANTunnelStatsGroup.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfDownReason"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopIpType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopIp"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopInterface"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelIfNextHopPortName"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsRxPackets"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsTxPackets"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsClear"))
)
if mibBuilder.loadTexts:
    hpicfVXLANTunnelStatsGroup.setStatus("current")

hpicfVXLANTunnelScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 4)
)
hpicfVXLANTunnelScalarGroup.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMaxVXLANTunnels"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfTotalVXLANTunnels"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelStatsTxMTUViolation"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelGlobalStatsDropCount"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelGlobalStatsClear"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelEnable"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVXLANTunnelUDPPort"))
)
if mibBuilder.loadTexts:
    hpicfVXLANTunnelScalarGroup.setStatus("current")

hpicfVirtualNetworkNotifyScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 5)
)
hpicfVirtualNetworkNotifyScalarsGroup.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddr"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterMTU"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSrcAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSource"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDstAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDest"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropInIfIndex"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkNotifyScalarsGroup.setStatus("current")


# Notification objects

hpicfVirtualNetworkIcmpErrorRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 0, 1)
)
hpicfVirtualNetworkIcmpErrorRcvd.setObjects(
      *(("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterAddr"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropRouterMTU"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSrcAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPSource"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDstAddrType"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropVTEPDest"),
        ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfMTUDropInIfIndex"),
        ("TUNNEL-MIB", "tunnelIfAddressType"),
        ("TUNNEL-MIB", "tunnelIfLocalInetAddress"),
        ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"))
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkIcmpErrorRcvd.setStatus(
        "current"
    )


# Notifications groups

hpicfVirtualNetworkNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 2, 6)
)
hpicfVirtualNetworkNotificationsGroup.setObjects(
    ("HP-ICF-VIRTUAL-NETWORK-MIB", "hpicfVirtualNetworkIcmpErrorRcvd")
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfVirtualNetworkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVirtualNetworkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-VIRTUAL-NETWORK-MIB",
    **{"hpicfVirtualNetwork": hpicfVirtualNetwork,
       "hpicfVirtualNetworkNotifications": hpicfVirtualNetworkNotifications,
       "hpicfVirtualNetworkIcmpErrorRcvd": hpicfVirtualNetworkIcmpErrorRcvd,
       "hpicfVirtualNetworkObjects": hpicfVirtualNetworkObjects,
       "hpicfVirtualNetworkScalars": hpicfVirtualNetworkScalars,
       "hpicfMaxVirtualNetworks": hpicfMaxVirtualNetworks,
       "hpicfTotalVirtualNetworks": hpicfTotalVirtualNetworks,
       "hpicfVirtualNetworkTable": hpicfVirtualNetworkTable,
       "hpicfVirtualNetworkEntry": hpicfVirtualNetworkEntry,
       "hpicfVirtualNetworkID": hpicfVirtualNetworkID,
       "hpicfVirtualNetworkName": hpicfVirtualNetworkName,
       "hpicfVirtualNetworkVLANID": hpicfVirtualNetworkVLANID,
       "hpicfVirtualNetworkRowStatus": hpicfVirtualNetworkRowStatus,
       "hpicfVirtualNetworkNotifyScalars": hpicfVirtualNetworkNotifyScalars,
       "hpicfMTUDropRouterAddrType": hpicfMTUDropRouterAddrType,
       "hpicfMTUDropRouterAddr": hpicfMTUDropRouterAddr,
       "hpicfMTUDropRouterMTU": hpicfMTUDropRouterMTU,
       "hpicfMTUDropVTEPSrcAddrType": hpicfMTUDropVTEPSrcAddrType,
       "hpicfMTUDropVTEPSource": hpicfMTUDropVTEPSource,
       "hpicfMTUDropVTEPDstAddrType": hpicfMTUDropVTEPDstAddrType,
       "hpicfMTUDropVTEPDest": hpicfMTUDropVTEPDest,
       "hpicfMTUDropInIfIndex": hpicfMTUDropInIfIndex,
       "hpicfMTUDropNotifyEnable": hpicfMTUDropNotifyEnable,
       "hpicfTunnelObjects": hpicfTunnelObjects,
       "hpicfVXLANTunnelObjects": hpicfVXLANTunnelObjects,
       "hpicfVXLANTunnelConfigObjects": hpicfVXLANTunnelConfigObjects,
       "hpicfVXLANTunnelIfTable": hpicfVXLANTunnelIfTable,
       "hpicfVXLANTunnelIfEntry": hpicfVXLANTunnelIfEntry,
       "hpicfVXLANTunnelIfDownReason": hpicfVXLANTunnelIfDownReason,
       "hpicfVXLANTunnelIfNextHopIpType": hpicfVXLANTunnelIfNextHopIpType,
       "hpicfVXLANTunnelIfNextHopIp": hpicfVXLANTunnelIfNextHopIp,
       "hpicfVXLANTunnelIfNextHopInterface": hpicfVXLANTunnelIfNextHopInterface,
       "hpicfVXLANTunnelIfNextHopPortName": hpicfVXLANTunnelIfNextHopPortName,
       "hpicfVXLANTunnelStatsRxPackets": hpicfVXLANTunnelStatsRxPackets,
       "hpicfVXLANTunnelStatsTxPackets": hpicfVXLANTunnelStatsTxPackets,
       "hpicfVXLANTunnelStatsClear": hpicfVXLANTunnelStatsClear,
       "hpicfVXLANTunnelScalars": hpicfVXLANTunnelScalars,
       "hpicfMaxVXLANTunnels": hpicfMaxVXLANTunnels,
       "hpicfTotalVXLANTunnels": hpicfTotalVXLANTunnels,
       "hpicfVXLANTunnelStatsTxMTUViolation": hpicfVXLANTunnelStatsTxMTUViolation,
       "hpicfVXLANTunnelGlobalStatsDropCount": hpicfVXLANTunnelGlobalStatsDropCount,
       "hpicfVXLANTunnelGlobalStatsClear": hpicfVXLANTunnelGlobalStatsClear,
       "hpicfVXLANTunnelEnable": hpicfVXLANTunnelEnable,
       "hpicfVXLANTunnelUDPPort": hpicfVXLANTunnelUDPPort,
       "hpicfVirtualNetworkConformance": hpicfVirtualNetworkConformance,
       "hpicfVirtualNetworkCompliances": hpicfVirtualNetworkCompliances,
       "hpicfVirtualNetworkCompliance": hpicfVirtualNetworkCompliance,
       "hpicfVirtualNetworkGroups": hpicfVirtualNetworkGroups,
       "hpicfVirtualNetworkGroup": hpicfVirtualNetworkGroup,
       "hpicfVirtualNetworkScalarGroup": hpicfVirtualNetworkScalarGroup,
       "hpicfVXLANTunnelStatsGroup": hpicfVXLANTunnelStatsGroup,
       "hpicfVXLANTunnelScalarGroup": hpicfVXLANTunnelScalarGroup,
       "hpicfVirtualNetworkNotifyScalarsGroup": hpicfVirtualNetworkNotifyScalarsGroup,
       "hpicfVirtualNetworkNotificationsGroup": hpicfVirtualNetworkNotificationsGroup}
)
