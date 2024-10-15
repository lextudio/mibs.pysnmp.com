# SNMP MIB module (WLSX-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-MOBILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:08 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaActiveState,
 ArubaAuthenticationMethods,
 ArubaEnableValue,
 ArubaEncryptionMethods,
 ArubaFrameType,
 ArubaPhyType,
 ArubaRogueApType) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaActiveState",
    "ArubaAuthenticationMethods",
    "ArubaEnableValue",
    "ArubaEncryptionMethods",
    "ArubaFrameType",
    "ArubaPhyType",
    "ArubaRogueApType")

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
 snmpModules) = mibBuilder.importSymbols(
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
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9)
)
wlsxMobilityMIB.setRevisions(
        ("1908-04-16 02:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxMobilityConfigGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityConfigGroup = _WlsxMobilityConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1)
)
_WlsxMobilityDomainTable_Object = MibTable
wlsxMobilityDomainTable = _WlsxMobilityDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxMobilityDomainTable.setStatus("current")
_WlsxMobilityDomainEntry_Object = MibTableRow
wlsxMobilityDomainEntry = _WlsxMobilityDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1)
)
wlsxMobilityDomainEntry.setIndexNames(
    (0, "WLSX-MOBILITY-MIB", "mobilityDomainName"),
)
if mibBuilder.loadTexts:
    wlsxMobilityDomainEntry.setStatus("current")
_MobilityDomainName_Type = DisplayString
_MobilityDomainName_Object = MibTableColumn
mobilityDomainName = _MobilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 1),
    _MobilityDomainName_Type()
)
mobilityDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mobilityDomainName.setStatus("current")
_MobilityDomainIsExclusive_Type = ArubaEnableValue
_MobilityDomainIsExclusive_Object = MibTableColumn
mobilityDomainIsExclusive = _MobilityDomainIsExclusive_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 2),
    _MobilityDomainIsExclusive_Type()
)
mobilityDomainIsExclusive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityDomainIsExclusive.setStatus("deprecated")
_MobilityDomainStatus_Type = RowStatus
_MobilityDomainStatus_Object = MibTableColumn
mobilityDomainStatus = _MobilityDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 3),
    _MobilityDomainStatus_Type()
)
mobilityDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mobilityDomainStatus.setStatus("current")
_WlsxMobilityHomeAgentTable_Object = MibTable
wlsxMobilityHomeAgentTable = _WlsxMobilityHomeAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxMobilityHomeAgentTable.setStatus("current")
_WlsxMobilityHomeAgentEntry_Object = MibTableRow
wlsxMobilityHomeAgentEntry = _WlsxMobilityHomeAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1)
)
wlsxMobilityHomeAgentEntry.setIndexNames(
    (0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentSubnet"),
    (0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentMask"),
    (0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentIp"),
)
if mibBuilder.loadTexts:
    wlsxMobilityHomeAgentEntry.setStatus("current")
_MobilityHomeAgentSubnet_Type = IpAddress
_MobilityHomeAgentSubnet_Object = MibTableColumn
mobilityHomeAgentSubnet = _MobilityHomeAgentSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 1),
    _MobilityHomeAgentSubnet_Type()
)
mobilityHomeAgentSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHomeAgentSubnet.setStatus("current")
_MobilityHomeAgentMask_Type = IpAddress
_MobilityHomeAgentMask_Object = MibTableColumn
mobilityHomeAgentMask = _MobilityHomeAgentMask_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 2),
    _MobilityHomeAgentMask_Type()
)
mobilityHomeAgentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHomeAgentMask.setStatus("current")
_MobilityHomeAgentIp_Type = IpAddress
_MobilityHomeAgentIp_Object = MibTableColumn
mobilityHomeAgentIp = _MobilityHomeAgentIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 3),
    _MobilityHomeAgentIp_Type()
)
mobilityHomeAgentIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mobilityHomeAgentIp.setStatus("current")
_MobilityHomeAgentVlan_Type = Integer32
_MobilityHomeAgentVlan_Object = MibTableColumn
mobilityHomeAgentVlan = _MobilityHomeAgentVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 4),
    _MobilityHomeAgentVlan_Type()
)
mobilityHomeAgentVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHomeAgentVlan.setStatus("current")
_WlsxMobilityHostTable_Object = MibTable
wlsxMobilityHostTable = _WlsxMobilityHostTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxMobilityHostTable.setStatus("current")
_WlsxMobilityHostEntry_Object = MibTableRow
wlsxMobilityHostEntry = _WlsxMobilityHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1)
)
wlsxMobilityHostEntry.setIndexNames(
    (0, "WLSX-MOBILITY-MIB", "mobilityHostMac"),
)
if mibBuilder.loadTexts:
    wlsxMobilityHostEntry.setStatus("current")
_MobilityHostMac_Type = MacAddress
_MobilityHostMac_Object = MibTableColumn
mobilityHostMac = _MobilityHostMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 1),
    _MobilityHostMac_Type()
)
mobilityHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mobilityHostMac.setStatus("current")
_MobilityHostIp_Type = IpAddress
_MobilityHostIp_Object = MibTableColumn
mobilityHostIp = _MobilityHostIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 2),
    _MobilityHostIp_Type()
)
mobilityHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostIp.setStatus("current")
_MobilityHostStatus_Type = DisplayString
_MobilityHostStatus_Object = MibTableColumn
mobilityHostStatus = _MobilityHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 3),
    _MobilityHostStatus_Type()
)
mobilityHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostStatus.setStatus("current")
_MobilityHostServiceTime_Type = Integer32
_MobilityHostServiceTime_Object = MibTableColumn
mobilityHostServiceTime = _MobilityHostServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 4),
    _MobilityHostServiceTime_Type()
)
mobilityHostServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostServiceTime.setStatus("current")
_MobilityHostHomeVlan_Type = Integer32
_MobilityHostHomeVlan_Object = MibTableColumn
mobilityHostHomeVlan = _MobilityHostHomeVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 5),
    _MobilityHostHomeVlan_Type()
)
mobilityHostHomeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostHomeVlan.setStatus("current")
_MobilityHostHomeNetwork_Type = IpAddress
_MobilityHostHomeNetwork_Object = MibTableColumn
mobilityHostHomeNetwork = _MobilityHostHomeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 6),
    _MobilityHostHomeNetwork_Type()
)
mobilityHostHomeNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostHomeNetwork.setStatus("current")
_MobilityHostHomeMask_Type = IpAddress
_MobilityHostHomeMask_Object = MibTableColumn
mobilityHostHomeMask = _MobilityHostHomeMask_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 7),
    _MobilityHostHomeMask_Type()
)
mobilityHostHomeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostHomeMask.setStatus("current")
_MobilityHostDhcpInfo_Type = DisplayString
_MobilityHostDhcpInfo_Object = MibTableColumn
mobilityHostDhcpInfo = _MobilityHostDhcpInfo_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 8),
    _MobilityHostDhcpInfo_Type()
)
mobilityHostDhcpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHostDhcpInfo.setStatus("current")
_WlsxMobilityProxyStatsGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityProxyStatsGroup = _WlsxMobilityProxyStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2)
)
_MobilityProxyPktRx_Type = Counter32
_MobilityProxyPktRx_Object = MibScalar
mobilityProxyPktRx = _MobilityProxyPktRx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 1),
    _MobilityProxyPktRx_Type()
)
mobilityProxyPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyPktRx.setStatus("current")
_MobilityProxyPktHandled_Type = Counter32
_MobilityProxyPktHandled_Object = MibScalar
mobilityProxyPktHandled = _MobilityProxyPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 2),
    _MobilityProxyPktHandled_Type()
)
mobilityProxyPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyPktHandled.setStatus("current")
_MobilityProxyPktFwd_Type = Counter32
_MobilityProxyPktFwd_Object = MibScalar
mobilityProxyPktFwd = _MobilityProxyPktFwd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 3),
    _MobilityProxyPktFwd_Type()
)
mobilityProxyPktFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyPktFwd.setStatus("current")
_MobilityProxyPktDrop_Type = Counter32
_MobilityProxyPktDrop_Object = MibScalar
mobilityProxyPktDrop = _MobilityProxyPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 4),
    _MobilityProxyPktDrop_Type()
)
mobilityProxyPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyPktDrop.setStatus("current")
_MobilityProxyBusy_Type = Counter32
_MobilityProxyBusy_Object = MibScalar
mobilityProxyBusy = _MobilityProxyBusy_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 5),
    _MobilityProxyBusy_Type()
)
mobilityProxyBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyBusy.setStatus("current")
_MobilityProxyNoMobility_Type = Counter32
_MobilityProxyNoMobility_Object = MibScalar
mobilityProxyNoMobility = _MobilityProxyNoMobility_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 6),
    _MobilityProxyNoMobility_Type()
)
mobilityProxyNoMobility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyNoMobility.setStatus("current")
_MobilityProxyClientIPChg_Type = Counter32
_MobilityProxyClientIPChg_Object = MibScalar
mobilityProxyClientIPChg = _MobilityProxyClientIPChg_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 7),
    _MobilityProxyClientIPChg_Type()
)
mobilityProxyClientIPChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyClientIPChg.setStatus("current")
_MobilityProxyClientEssidChg_Type = Counter32
_MobilityProxyClientEssidChg_Object = MibScalar
mobilityProxyClientEssidChg = _MobilityProxyClientEssidChg_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 8),
    _MobilityProxyClientEssidChg_Type()
)
mobilityProxyClientEssidChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyClientEssidChg.setStatus("current")
_WlsxMobilityProxyDHCPStatsGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityProxyDHCPStatsGroup = _WlsxMobilityProxyDHCPStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3)
)
_MobilityProxyDhcpBootpRx_Type = Counter32
_MobilityProxyDhcpBootpRx_Object = MibScalar
mobilityProxyDhcpBootpRx = _MobilityProxyDhcpBootpRx_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 1),
    _MobilityProxyDhcpBootpRx_Type()
)
mobilityProxyDhcpBootpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDhcpBootpRx.setStatus("current")
_MobilityProxyDhcpPktProc_Type = Counter32
_MobilityProxyDhcpPktProc_Object = MibScalar
mobilityProxyDhcpPktProc = _MobilityProxyDhcpPktProc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 2),
    _MobilityProxyDhcpPktProc_Type()
)
mobilityProxyDhcpPktProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDhcpPktProc.setStatus("current")
_MobilityProxyDhcpPktFwd_Type = Counter32
_MobilityProxyDhcpPktFwd_Object = MibScalar
mobilityProxyDhcpPktFwd = _MobilityProxyDhcpPktFwd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 3),
    _MobilityProxyDhcpPktFwd_Type()
)
mobilityProxyDhcpPktFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDhcpPktFwd.setStatus("current")
_MobilityProxyDhcpPktDrop_Type = Counter32
_MobilityProxyDhcpPktDrop_Object = MibScalar
mobilityProxyDhcpPktDrop = _MobilityProxyDhcpPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 4),
    _MobilityProxyDhcpPktDrop_Type()
)
mobilityProxyDhcpPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDhcpPktDrop.setStatus("current")
_MobilityProxyDHCPNak_Type = Counter32
_MobilityProxyDHCPNak_Object = MibScalar
mobilityProxyDHCPNak = _MobilityProxyDHCPNak_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 5),
    _MobilityProxyDHCPNak_Type()
)
mobilityProxyDHCPNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDHCPNak.setStatus("current")
_MobilityProxyBadDHCPPkt_Type = Counter32
_MobilityProxyBadDHCPPkt_Object = MibScalar
mobilityProxyBadDHCPPkt = _MobilityProxyBadDHCPPkt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 6),
    _MobilityProxyBadDHCPPkt_Type()
)
mobilityProxyBadDHCPPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyBadDHCPPkt.setStatus("current")
_MobilityProxyNotDHCP_Type = Counter32
_MobilityProxyNotDHCP_Object = MibScalar
mobilityProxyNotDHCP = _MobilityProxyNotDHCP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 7),
    _MobilityProxyNotDHCP_Type()
)
mobilityProxyNotDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyNotDHCP.setStatus("current")
_MobilityProxyDHCPNoHomeVlan_Type = Counter32
_MobilityProxyDHCPNoHomeVlan_Object = MibScalar
mobilityProxyDHCPNoHomeVlan = _MobilityProxyDHCPNoHomeVlan_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 8),
    _MobilityProxyDHCPNoHomeVlan_Type()
)
mobilityProxyDHCPNoHomeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDHCPNoHomeVlan.setStatus("current")
_MobilityProxyDHCPUnexpFrame_Type = Counter32
_MobilityProxyDHCPUnexpFrame_Object = MibScalar
mobilityProxyDHCPUnexpFrame = _MobilityProxyDHCPUnexpFrame_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 9),
    _MobilityProxyDHCPUnexpFrame_Type()
)
mobilityProxyDHCPUnexpFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDHCPUnexpFrame.setStatus("current")
_MobilityProxyDHCPUnexpRemote_Type = Counter32
_MobilityProxyDHCPUnexpRemote_Object = MibScalar
mobilityProxyDHCPUnexpRemote = _MobilityProxyDHCPUnexpRemote_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 10),
    _MobilityProxyDHCPUnexpRemote_Type()
)
mobilityProxyDHCPUnexpRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityProxyDHCPUnexpRemote.setStatus("current")
_WlsxMobilityHAStatsGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityHAStatsGroup = _WlsxMobilityHAStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4)
)
_MobilityHARxRRQ_Type = Counter32
_MobilityHARxRRQ_Object = MibScalar
mobilityHARxRRQ = _MobilityHARxRRQ_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 1),
    _MobilityHARxRRQ_Type()
)
mobilityHARxRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARxRRQ.setStatus("current")
_MobilityHASentRRP_Type = Counter32
_MobilityHASentRRP_Object = MibScalar
mobilityHASentRRP = _MobilityHASentRRP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 2),
    _MobilityHASentRRP_Type()
)
mobilityHASentRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHASentRRP.setStatus("current")
_MobilityHARRQAccept_Type = Counter32
_MobilityHARRQAccept_Object = MibScalar
mobilityHARRQAccept = _MobilityHARRQAccept_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 3),
    _MobilityHARRQAccept_Type()
)
mobilityHARRQAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARRQAccept.setStatus("current")
_MobilityHARRQDenied_Type = Counter32
_MobilityHARRQDenied_Object = MibScalar
mobilityHARRQDenied = _MobilityHARRQDenied_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 4),
    _MobilityHARRQDenied_Type()
)
mobilityHARRQDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARRQDenied.setStatus("current")
_MobilityHARRQIgnore_Type = Counter32
_MobilityHARRQIgnore_Object = MibScalar
mobilityHARRQIgnore = _MobilityHARRQIgnore_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 5),
    _MobilityHARRQIgnore_Type()
)
mobilityHARRQIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARRQIgnore.setStatus("current")
_MobilityHARRQAdminDeny_Type = Counter32
_MobilityHARRQAdminDeny_Object = MibScalar
mobilityHARRQAdminDeny = _MobilityHARRQAdminDeny_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 6),
    _MobilityHARRQAdminDeny_Type()
)
mobilityHARRQAdminDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARRQAdminDeny.setStatus("current")
_MobilityHARRQNoResource_Type = Counter32
_MobilityHARRQNoResource_Object = MibScalar
mobilityHARRQNoResource = _MobilityHARRQNoResource_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 7),
    _MobilityHARRQNoResource_Type()
)
mobilityHARRQNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHARRQNoResource.setStatus("current")
_MobilityHAMNauthFail_Type = Counter32
_MobilityHAMNauthFail_Object = MibScalar
mobilityHAMNauthFail = _MobilityHAMNauthFail_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 8),
    _MobilityHAMNauthFail_Type()
)
mobilityHAMNauthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHAMNauthFail.setStatus("current")
_MobilityHAFAauthFail_Type = Counter32
_MobilityHAFAauthFail_Object = MibScalar
mobilityHAFAauthFail = _MobilityHAFAauthFail_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 9),
    _MobilityHAFAauthFail_Type()
)
mobilityHAFAauthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHAFAauthFail.setStatus("current")
_MobilityHABadID_Type = Counter32
_MobilityHABadID_Object = MibScalar
mobilityHABadID = _MobilityHABadID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 10),
    _MobilityHABadID_Type()
)
mobilityHABadID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHABadID.setStatus("current")
_MobilityHAMalform_Type = Counter32
_MobilityHAMalform_Object = MibScalar
mobilityHAMalform = _MobilityHAMalform_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 11),
    _MobilityHAMalform_Type()
)
mobilityHAMalform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHAMalform.setStatus("current")
_MobilityHATooManyBnd_Type = Counter32
_MobilityHATooManyBnd_Object = MibScalar
mobilityHATooManyBnd = _MobilityHATooManyBnd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 12),
    _MobilityHATooManyBnd_Type()
)
mobilityHATooManyBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHATooManyBnd.setStatus("current")
_MobilityHABndExpire_Type = Counter32
_MobilityHABndExpire_Object = MibScalar
mobilityHABndExpire = _MobilityHABndExpire_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 13),
    _MobilityHABndExpire_Type()
)
mobilityHABndExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityHABndExpire.setStatus("current")
_WlsxMobilityFAStatsGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityFAStatsGroup = _WlsxMobilityFAStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5)
)
_MobilityFASentRRQ_Type = Counter32
_MobilityFASentRRQ_Object = MibScalar
mobilityFASentRRQ = _MobilityFASentRRQ_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 1),
    _MobilityFASentRRQ_Type()
)
mobilityFASentRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFASentRRQ.setStatus("current")
_MobilityFARcvRRP_Type = Counter32
_MobilityFARcvRRP_Object = MibScalar
mobilityFARcvRRP = _MobilityFARcvRRP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 2),
    _MobilityFARcvRRP_Type()
)
mobilityFARcvRRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFARcvRRP.setStatus("current")
_MobilityFARRQAccept_Type = Counter32
_MobilityFARRQAccept_Object = MibScalar
mobilityFARRQAccept = _MobilityFARRQAccept_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 3),
    _MobilityFARRQAccept_Type()
)
mobilityFARRQAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFARRQAccept.setStatus("current")
_MobilityFARRQReject_Type = Counter32
_MobilityFARRQReject_Object = MibScalar
mobilityFARRQReject = _MobilityFARRQReject_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 4),
    _MobilityFARRQReject_Type()
)
mobilityFARRQReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFARRQReject.setStatus("current")
_MobilityMNHAauthFAIL_Type = Counter32
_MobilityMNHAauthFAIL_Object = MibScalar
mobilityMNHAauthFAIL = _MobilityMNHAauthFAIL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 5),
    _MobilityMNHAauthFAIL_Type()
)
mobilityMNHAauthFAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityMNHAauthFAIL.setStatus("current")
_MobilityFAHAauthFAIL_Type = Counter32
_MobilityFAHAauthFAIL_Object = MibScalar
mobilityFAHAauthFAIL = _MobilityFAHAauthFAIL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 6),
    _MobilityFAHAauthFAIL_Type()
)
mobilityFAHAauthFAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFAHAauthFAIL.setStatus("current")
_MobilityFABadID_Type = Counter32
_MobilityFABadID_Object = MibScalar
mobilityFABadID = _MobilityFABadID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 7),
    _MobilityFABadID_Type()
)
mobilityFABadID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFABadID.setStatus("current")
_MobilityFAMalform_Type = Counter32
_MobilityFAMalform_Object = MibScalar
mobilityFAMalform = _MobilityFAMalform_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 8),
    _MobilityFAMalform_Type()
)
mobilityFAMalform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityFAMalform.setStatus("current")
_WlsxMobilityHAFARevocationStatsGroup_ObjectIdentity = ObjectIdentity
wlsxMobilityHAFARevocationStatsGroup = _WlsxMobilityHAFARevocationStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6)
)
_MobilitySentRRVRQ_Type = Counter32
_MobilitySentRRVRQ_Object = MibScalar
mobilitySentRRVRQ = _MobilitySentRRVRQ_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 1),
    _MobilitySentRRVRQ_Type()
)
mobilitySentRRVRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilitySentRRVRQ.setStatus("current")
_MobilityRcvRRVAck_Type = Counter32
_MobilityRcvRRVAck_Object = MibScalar
mobilityRcvRRVAck = _MobilityRcvRRVAck_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 2),
    _MobilityRcvRRVAck_Type()
)
mobilityRcvRRVAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityRcvRRVAck.setStatus("current")
_MobilityRcvRRV_Type = Counter32
_MobilityRcvRRV_Object = MibScalar
mobilityRcvRRV = _MobilityRcvRRV_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 3),
    _MobilityRcvRRV_Type()
)
mobilityRcvRRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityRcvRRV.setStatus("current")
_MobilitySentRRVAck_Type = Counter32
_MobilitySentRRVAck_Object = MibScalar
mobilitySentRRVAck = _MobilitySentRRVAck_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 4),
    _MobilitySentRRVAck_Type()
)
mobilitySentRRVAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilitySentRRVAck.setStatus("current")
_MobilityRRVRQIgnore_Type = Counter32
_MobilityRRVRQIgnore_Object = MibScalar
mobilityRRVRQIgnore = _MobilityRRVRQIgnore_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 5),
    _MobilityRRVRQIgnore_Type()
)
mobilityRRVRQIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityRRVRQIgnore.setStatus("current")
_MobilityRRVAckIgnore_Type = Counter32
_MobilityRRVAckIgnore_Object = MibScalar
mobilityRRVAckIgnore = _MobilityRRVAckIgnore_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 6),
    _MobilityRRVAckIgnore_Type()
)
mobilityRRVAckIgnore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mobilityRRVAckIgnore.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-MOBILITY-MIB",
    **{"wlsxMobilityMIB": wlsxMobilityMIB,
       "wlsxMobilityConfigGroup": wlsxMobilityConfigGroup,
       "wlsxMobilityDomainTable": wlsxMobilityDomainTable,
       "wlsxMobilityDomainEntry": wlsxMobilityDomainEntry,
       "mobilityDomainName": mobilityDomainName,
       "mobilityDomainIsExclusive": mobilityDomainIsExclusive,
       "mobilityDomainStatus": mobilityDomainStatus,
       "wlsxMobilityHomeAgentTable": wlsxMobilityHomeAgentTable,
       "wlsxMobilityHomeAgentEntry": wlsxMobilityHomeAgentEntry,
       "mobilityHomeAgentSubnet": mobilityHomeAgentSubnet,
       "mobilityHomeAgentMask": mobilityHomeAgentMask,
       "mobilityHomeAgentIp": mobilityHomeAgentIp,
       "mobilityHomeAgentVlan": mobilityHomeAgentVlan,
       "wlsxMobilityHostTable": wlsxMobilityHostTable,
       "wlsxMobilityHostEntry": wlsxMobilityHostEntry,
       "mobilityHostMac": mobilityHostMac,
       "mobilityHostIp": mobilityHostIp,
       "mobilityHostStatus": mobilityHostStatus,
       "mobilityHostServiceTime": mobilityHostServiceTime,
       "mobilityHostHomeVlan": mobilityHostHomeVlan,
       "mobilityHostHomeNetwork": mobilityHostHomeNetwork,
       "mobilityHostHomeMask": mobilityHostHomeMask,
       "mobilityHostDhcpInfo": mobilityHostDhcpInfo,
       "wlsxMobilityProxyStatsGroup": wlsxMobilityProxyStatsGroup,
       "mobilityProxyPktRx": mobilityProxyPktRx,
       "mobilityProxyPktHandled": mobilityProxyPktHandled,
       "mobilityProxyPktFwd": mobilityProxyPktFwd,
       "mobilityProxyPktDrop": mobilityProxyPktDrop,
       "mobilityProxyBusy": mobilityProxyBusy,
       "mobilityProxyNoMobility": mobilityProxyNoMobility,
       "mobilityProxyClientIPChg": mobilityProxyClientIPChg,
       "mobilityProxyClientEssidChg": mobilityProxyClientEssidChg,
       "wlsxMobilityProxyDHCPStatsGroup": wlsxMobilityProxyDHCPStatsGroup,
       "mobilityProxyDhcpBootpRx": mobilityProxyDhcpBootpRx,
       "mobilityProxyDhcpPktProc": mobilityProxyDhcpPktProc,
       "mobilityProxyDhcpPktFwd": mobilityProxyDhcpPktFwd,
       "mobilityProxyDhcpPktDrop": mobilityProxyDhcpPktDrop,
       "mobilityProxyDHCPNak": mobilityProxyDHCPNak,
       "mobilityProxyBadDHCPPkt": mobilityProxyBadDHCPPkt,
       "mobilityProxyNotDHCP": mobilityProxyNotDHCP,
       "mobilityProxyDHCPNoHomeVlan": mobilityProxyDHCPNoHomeVlan,
       "mobilityProxyDHCPUnexpFrame": mobilityProxyDHCPUnexpFrame,
       "mobilityProxyDHCPUnexpRemote": mobilityProxyDHCPUnexpRemote,
       "wlsxMobilityHAStatsGroup": wlsxMobilityHAStatsGroup,
       "mobilityHARxRRQ": mobilityHARxRRQ,
       "mobilityHASentRRP": mobilityHASentRRP,
       "mobilityHARRQAccept": mobilityHARRQAccept,
       "mobilityHARRQDenied": mobilityHARRQDenied,
       "mobilityHARRQIgnore": mobilityHARRQIgnore,
       "mobilityHARRQAdminDeny": mobilityHARRQAdminDeny,
       "mobilityHARRQNoResource": mobilityHARRQNoResource,
       "mobilityHAMNauthFail": mobilityHAMNauthFail,
       "mobilityHAFAauthFail": mobilityHAFAauthFail,
       "mobilityHABadID": mobilityHABadID,
       "mobilityHAMalform": mobilityHAMalform,
       "mobilityHATooManyBnd": mobilityHATooManyBnd,
       "mobilityHABndExpire": mobilityHABndExpire,
       "wlsxMobilityFAStatsGroup": wlsxMobilityFAStatsGroup,
       "mobilityFASentRRQ": mobilityFASentRRQ,
       "mobilityFARcvRRP": mobilityFARcvRRP,
       "mobilityFARRQAccept": mobilityFARRQAccept,
       "mobilityFARRQReject": mobilityFARRQReject,
       "mobilityMNHAauthFAIL": mobilityMNHAauthFAIL,
       "mobilityFAHAauthFAIL": mobilityFAHAauthFAIL,
       "mobilityFABadID": mobilityFABadID,
       "mobilityFAMalform": mobilityFAMalform,
       "wlsxMobilityHAFARevocationStatsGroup": wlsxMobilityHAFARevocationStatsGroup,
       "mobilitySentRRVRQ": mobilitySentRRVRQ,
       "mobilityRcvRRVAck": mobilityRcvRRVAck,
       "mobilityRcvRRV": mobilityRcvRRV,
       "mobilitySentRRVAck": mobilitySentRRVAck,
       "mobilityRRVRQIgnore": mobilityRRVRQIgnore,
       "mobilityRRVAckIgnore": mobilityRRVAckIgnore}
)
