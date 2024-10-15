# SNMP MIB module (CISCO-LWAPP-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:16 2024
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

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792)
)
ciscoLwappDhcpMIB.setRevisions(
        ("2012-01-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDhcpMIBNotif_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBNotif = _CiscoLwappDhcpMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 0)
)
_CiscoLwappDhcpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBObjects = _CiscoLwappDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1)
)
_CiscoLwappDhcpGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpGlobalConfig = _CiscoLwappDhcpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1)
)


class _CLDhcpClearAllStats_Type(TruthValue):
    """Custom type cLDhcpClearAllStats based on TruthValue"""


_CLDhcpClearAllStats_Object = MibScalar
cLDhcpClearAllStats = _CLDhcpClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1, 1),
    _CLDhcpClearAllStats_Type()
)
cLDhcpClearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpClearAllStats.setStatus("current")


class _CLDhcpOpt82RemoteIdFormat_Type(Integer32):
    """Custom type cLDhcpOpt82RemoteIdFormat based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("apEthMac", 3),
          ("apEthMacSsid", 10),
          ("apGroupName", 5),
          ("apLocation", 7),
          ("apMac", 1),
          ("apMacSsid", 2),
          ("apMacVlanId", 8),
          ("apNameSsid", 4),
          ("apNameVlanId", 9),
          ("flexGroupName", 6))
    )


_CLDhcpOpt82RemoteIdFormat_Type.__name__ = "Integer32"
_CLDhcpOpt82RemoteIdFormat_Object = MibScalar
cLDhcpOpt82RemoteIdFormat = _CLDhcpOpt82RemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1, 2),
    _CLDhcpOpt82RemoteIdFormat_Type()
)
cLDhcpOpt82RemoteIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpOpt82RemoteIdFormat.setStatus("current")
_CLDhcpClearAllDiscontinuityTime_Type = TimeStamp
_CLDhcpClearAllDiscontinuityTime_Object = MibScalar
cLDhcpClearAllDiscontinuityTime = _CLDhcpClearAllDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1, 3),
    _CLDhcpClearAllDiscontinuityTime_Type()
)
cLDhcpClearAllDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpClearAllDiscontinuityTime.setStatus("current")
_CLDhcpTimeout_Type = Unsigned32
_CLDhcpTimeout_Object = MibScalar
cLDhcpTimeout = _CLDhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1, 4),
    _CLDhcpTimeout_Type()
)
cLDhcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpTimeout.setUnits("seconds")


class _CLDhcpOpt37RemoteIdFormat_Type(Integer32):
    """Custom type cLDhcpOpt37RemoteIdFormat based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("apEthMac", 3),
          ("apEthMacSsid", 10),
          ("apGroupName", 5),
          ("apLocation", 7),
          ("apMac", 1),
          ("apMacSsid", 2),
          ("apMacVlanId", 8),
          ("apNameSsid", 4),
          ("apNameVlanId", 9),
          ("flexGroupName", 6))
    )


_CLDhcpOpt37RemoteIdFormat_Type.__name__ = "Integer32"
_CLDhcpOpt37RemoteIdFormat_Object = MibScalar
cLDhcpOpt37RemoteIdFormat = _CLDhcpOpt37RemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 1, 5),
    _CLDhcpOpt37RemoteIdFormat_Type()
)
cLDhcpOpt37RemoteIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpOpt37RemoteIdFormat.setStatus("current")
_CiscoLwappDhcpStatsConfig_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpStatsConfig = _CiscoLwappDhcpStatsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2)
)
_CLDhcpStatsConfigTable_Object = MibTable
cLDhcpStatsConfigTable = _CLDhcpStatsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLDhcpStatsConfigTable.setStatus("current")
_CLDhcpStatsConfigEntry_Object = MibTableRow
cLDhcpStatsConfigEntry = _CLDhcpStatsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1, 1)
)
cLDhcpStatsConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-DHCP-MIB", "cLDhcpServerInetAddressType"),
    (0, "CISCO-LWAPP-DHCP-MIB", "cLDhcpServerInetAddress"),
)
if mibBuilder.loadTexts:
    cLDhcpStatsConfigEntry.setStatus("current")
_CLDhcpServerInetAddressType_Type = InetAddressType
_CLDhcpServerInetAddressType_Object = MibTableColumn
cLDhcpServerInetAddressType = _CLDhcpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1, 1, 1),
    _CLDhcpServerInetAddressType_Type()
)
cLDhcpServerInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLDhcpServerInetAddressType.setStatus("current")
_CLDhcpServerInetAddress_Type = InetAddress
_CLDhcpServerInetAddress_Object = MibTableColumn
cLDhcpServerInetAddress = _CLDhcpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1, 1, 2),
    _CLDhcpServerInetAddress_Type()
)
cLDhcpServerInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLDhcpServerInetAddress.setStatus("current")
_CLDhcpClearStats_Type = TruthValue
_CLDhcpClearStats_Object = MibTableColumn
cLDhcpClearStats = _CLDhcpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1, 1, 3),
    _CLDhcpClearStats_Type()
)
cLDhcpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpClearStats.setStatus("current")
_CLDhcpClearDiscontinuityTime_Type = TimeStamp
_CLDhcpClearDiscontinuityTime_Object = MibTableColumn
cLDhcpClearDiscontinuityTime = _CLDhcpClearDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 2, 1, 1, 4),
    _CLDhcpClearDiscontinuityTime_Type()
)
cLDhcpClearDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpClearDiscontinuityTime.setStatus("current")
_CiscoLwappDhcpStats_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpStats = _CiscoLwappDhcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3)
)
_CLDhcpStatsShowTable_Object = MibTable
cLDhcpStatsShowTable = _CLDhcpStatsShowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLDhcpStatsShowTable.setStatus("current")
_CLDhcpStatsShowEntry_Object = MibTableRow
cLDhcpStatsShowEntry = _CLDhcpStatsShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1)
)
cLDhcpStatsShowEntry.setIndexNames(
    (0, "CISCO-LWAPP-DHCP-MIB", "cLDhcpServerInetAddressType"),
    (0, "CISCO-LWAPP-DHCP-MIB", "cLDhcpServerInetAddress"),
)
if mibBuilder.loadTexts:
    cLDhcpStatsShowEntry.setStatus("current")
_CLDhcpProxy_Type = TruthValue
_CLDhcpProxy_Object = MibTableColumn
cLDhcpProxy = _CLDhcpProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 1),
    _CLDhcpProxy_Type()
)
cLDhcpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLDhcpProxy.setStatus("current")
_CLDhcpDiscoverPackets_Type = Counter32
_CLDhcpDiscoverPackets_Object = MibTableColumn
cLDhcpDiscoverPackets = _CLDhcpDiscoverPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 2),
    _CLDhcpDiscoverPackets_Type()
)
cLDhcpDiscoverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpDiscoverPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpDiscoverPackets.setUnits("packets")
_CLDhcpRequestPackets_Type = Counter32
_CLDhcpRequestPackets_Object = MibTableColumn
cLDhcpRequestPackets = _CLDhcpRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 3),
    _CLDhcpRequestPackets_Type()
)
cLDhcpRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpRequestPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpRequestPackets.setUnits("packets")
_CLDhcpDeclinePackets_Type = Counter32
_CLDhcpDeclinePackets_Object = MibTableColumn
cLDhcpDeclinePackets = _CLDhcpDeclinePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 4),
    _CLDhcpDeclinePackets_Type()
)
cLDhcpDeclinePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpDeclinePackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpDeclinePackets.setUnits("packets")
_CLDhcpInformPackets_Type = Counter32
_CLDhcpInformPackets_Object = MibTableColumn
cLDhcpInformPackets = _CLDhcpInformPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 5),
    _CLDhcpInformPackets_Type()
)
cLDhcpInformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpInformPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpInformPackets.setUnits("packets")
_CLDhcpReleasePackets_Type = Counter32
_CLDhcpReleasePackets_Object = MibTableColumn
cLDhcpReleasePackets = _CLDhcpReleasePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 6),
    _CLDhcpReleasePackets_Type()
)
cLDhcpReleasePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpReleasePackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpReleasePackets.setUnits("packets")
_CLDhcpReplyPackets_Type = Counter32
_CLDhcpReplyPackets_Object = MibTableColumn
cLDhcpReplyPackets = _CLDhcpReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 7),
    _CLDhcpReplyPackets_Type()
)
cLDhcpReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpReplyPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpReplyPackets.setUnits("packets")
_CLDhcpOfferPackets_Type = Counter32
_CLDhcpOfferPackets_Object = MibTableColumn
cLDhcpOfferPackets = _CLDhcpOfferPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 8),
    _CLDhcpOfferPackets_Type()
)
cLDhcpOfferPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpOfferPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpOfferPackets.setUnits("packets")
_CLDhcpAckPackets_Type = Counter32
_CLDhcpAckPackets_Object = MibTableColumn
cLDhcpAckPackets = _CLDhcpAckPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 9),
    _CLDhcpAckPackets_Type()
)
cLDhcpAckPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpAckPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpAckPackets.setUnits("packets")
_CLDhcpNakPackets_Type = Counter32
_CLDhcpNakPackets_Object = MibTableColumn
cLDhcpNakPackets = _CLDhcpNakPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 10),
    _CLDhcpNakPackets_Type()
)
cLDhcpNakPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpNakPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpNakPackets.setUnits("packets")
_CLDhcpTxFailures_Type = Counter32
_CLDhcpTxFailures_Object = MibTableColumn
cLDhcpTxFailures = _CLDhcpTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 11),
    _CLDhcpTxFailures_Type()
)
cLDhcpTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpTxFailures.setStatus("current")
_CLDhcpLastResponseTime_Type = TimeStamp
_CLDhcpLastResponseTime_Object = MibTableColumn
cLDhcpLastResponseTime = _CLDhcpLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 12),
    _CLDhcpLastResponseTime_Type()
)
cLDhcpLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpLastResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpLastResponseTime.setUnits("seconds")
_CLDhcpLastRequestTime_Type = TimeStamp
_CLDhcpLastRequestTime_Object = MibTableColumn
cLDhcpLastRequestTime = _CLDhcpLastRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 13),
    _CLDhcpLastRequestTime_Type()
)
cLDhcpLastRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpLastRequestTime.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpLastRequestTime.setUnits("seconds")
_CLDhcpRxDiscoverPackets_Type = Counter32
_CLDhcpRxDiscoverPackets_Object = MibTableColumn
cLDhcpRxDiscoverPackets = _CLDhcpRxDiscoverPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 3, 1, 1, 14),
    _CLDhcpRxDiscoverPackets_Type()
)
cLDhcpRxDiscoverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpRxDiscoverPackets.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpRxDiscoverPackets.setUnits("packets")
_CiscoLwappDhcpScopeStats_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpScopeStats = _CiscoLwappDhcpScopeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4)
)
_CLDhcpScopeStatsTable_Object = MibTable
cLDhcpScopeStatsTable = _CLDhcpScopeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLDhcpScopeStatsTable.setStatus("current")
_CLDhcpScopeStatsEntry_Object = MibTableRow
cLDhcpScopeStatsEntry = _CLDhcpScopeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1)
)
cLDhcpScopeStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DHCP-MIB", "cLDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    cLDhcpScopeStatsEntry.setStatus("current")
_CLDhcpScopeIndex_Type = Unsigned32
_CLDhcpScopeIndex_Object = MibTableColumn
cLDhcpScopeIndex = _CLDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 1),
    _CLDhcpScopeIndex_Type()
)
cLDhcpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLDhcpScopeIndex.setStatus("current")
_CLDhcpScopeAddressPoolUsage_Type = Unsigned32
_CLDhcpScopeAddressPoolUsage_Object = MibTableColumn
cLDhcpScopeAddressPoolUsage = _CLDhcpScopeAddressPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 2),
    _CLDhcpScopeAddressPoolUsage_Type()
)
cLDhcpScopeAddressPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeAddressPoolUsage.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeAddressPoolUsage.setUnits("Percent")
_CLDhcpScopeName_Type = DisplayString
_CLDhcpScopeName_Object = MibTableColumn
cLDhcpScopeName = _CLDhcpScopeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 3),
    _CLDhcpScopeName_Type()
)
cLDhcpScopeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeName.setStatus("current")
_CLDhcpScopeAllocatedIP_Type = Counter32
_CLDhcpScopeAllocatedIP_Object = MibTableColumn
cLDhcpScopeAllocatedIP = _CLDhcpScopeAllocatedIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 4),
    _CLDhcpScopeAllocatedIP_Type()
)
cLDhcpScopeAllocatedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeAllocatedIP.setStatus("current")
_CLDhcpScopeAvailableIP_Type = Counter32
_CLDhcpScopeAvailableIP_Object = MibTableColumn
cLDhcpScopeAvailableIP = _CLDhcpScopeAvailableIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 5),
    _CLDhcpScopeAvailableIP_Type()
)
cLDhcpScopeAvailableIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeAvailableIP.setStatus("current")
_CLDhcpScopeDiscoverPkts_Type = Counter32
_CLDhcpScopeDiscoverPkts_Object = MibTableColumn
cLDhcpScopeDiscoverPkts = _CLDhcpScopeDiscoverPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 6),
    _CLDhcpScopeDiscoverPkts_Type()
)
cLDhcpScopeDiscoverPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeDiscoverPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeDiscoverPkts.setUnits("packets")
_CLDhcpScopeAckPkts_Type = Counter32
_CLDhcpScopeAckPkts_Object = MibTableColumn
cLDhcpScopeAckPkts = _CLDhcpScopeAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 7),
    _CLDhcpScopeAckPkts_Type()
)
cLDhcpScopeAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeAckPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeAckPkts.setUnits("packets")
_CLDhcpScopeOfferPkts_Type = Counter32
_CLDhcpScopeOfferPkts_Object = MibTableColumn
cLDhcpScopeOfferPkts = _CLDhcpScopeOfferPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 8),
    _CLDhcpScopeOfferPkts_Type()
)
cLDhcpScopeOfferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeOfferPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeOfferPkts.setUnits("packets")
_CLDhcpScopeTotalAckPkts_Type = Counter32
_CLDhcpScopeTotalAckPkts_Object = MibTableColumn
cLDhcpScopeTotalAckPkts = _CLDhcpScopeTotalAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 9),
    _CLDhcpScopeTotalAckPkts_Type()
)
cLDhcpScopeTotalAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeTotalAckPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeTotalAckPkts.setUnits("packets")
_CLDhcpScopeRequestPkts_Type = Counter32
_CLDhcpScopeRequestPkts_Object = MibTableColumn
cLDhcpScopeRequestPkts = _CLDhcpScopeRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 10),
    _CLDhcpScopeRequestPkts_Type()
)
cLDhcpScopeRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeRequestPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeRequestPkts.setUnits("packets")
_CLDhcpScopeRequestGoodPkts_Type = Counter32
_CLDhcpScopeRequestGoodPkts_Object = MibTableColumn
cLDhcpScopeRequestGoodPkts = _CLDhcpScopeRequestGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 4, 1, 1, 11),
    _CLDhcpScopeRequestGoodPkts_Type()
)
cLDhcpScopeRequestGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpScopeRequestGoodPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLDhcpScopeRequestGoodPkts.setUnits("packets")
_CiscoLwappDhcpMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBNotifObjects = _CiscoLwappDhcpMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 5)
)
_CLDhcpTrapSet_Type = TruthValue
_CLDhcpTrapSet_Object = MibScalar
cLDhcpTrapSet = _CLDhcpTrapSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 1, 5, 1),
    _CLDhcpTrapSet_Type()
)
cLDhcpTrapSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLDhcpTrapSet.setStatus("current")
_CiscoLwappDhcpMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBConform = _CiscoLwappDhcpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 2)
)
_CiscoLwappDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBCompliances = _CiscoLwappDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 2, 1)
)
_CiscoLwappDhcpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDhcpMIBGroups = _CiscoLwappDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 2, 2)
)

# Managed Objects groups

ciscoLwappDhcpMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 2, 2, 1)
)
ciscoLwappDhcpMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-DHCP-MIB", "cLDhcpClearAllStats"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpOpt82RemoteIdFormat"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpClearAllDiscontinuityTime"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpTimeout"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpOpt37RemoteIdFormat"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpClearStats"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpClearDiscontinuityTime"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpProxy"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpDiscoverPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpRequestPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpDeclinePackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpInformPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpReleasePackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpReplyPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpOfferPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpAckPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpNakPackets"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpTxFailures"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpLastResponseTime"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpLastRequestTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappDhcpMIBConfigGroup.setStatus("current")


# Notification objects

ciscoLwappDhcpScopeAddressExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 0, 1)
)
ciscoLwappDhcpScopeAddressExhaust.setObjects(
      *(("CISCO-LWAPP-DHCP-MIB", "cLDhcpScopeName"),
        ("CISCO-LWAPP-DHCP-MIB", "cLDhcpTrapSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappDhcpScopeAddressExhaust.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappDhcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 792, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDhcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DHCP-MIB",
    **{"ciscoLwappDhcpMIB": ciscoLwappDhcpMIB,
       "ciscoLwappDhcpMIBNotif": ciscoLwappDhcpMIBNotif,
       "ciscoLwappDhcpScopeAddressExhaust": ciscoLwappDhcpScopeAddressExhaust,
       "ciscoLwappDhcpMIBObjects": ciscoLwappDhcpMIBObjects,
       "ciscoLwappDhcpGlobalConfig": ciscoLwappDhcpGlobalConfig,
       "cLDhcpClearAllStats": cLDhcpClearAllStats,
       "cLDhcpOpt82RemoteIdFormat": cLDhcpOpt82RemoteIdFormat,
       "cLDhcpClearAllDiscontinuityTime": cLDhcpClearAllDiscontinuityTime,
       "cLDhcpTimeout": cLDhcpTimeout,
       "cLDhcpOpt37RemoteIdFormat": cLDhcpOpt37RemoteIdFormat,
       "ciscoLwappDhcpStatsConfig": ciscoLwappDhcpStatsConfig,
       "cLDhcpStatsConfigTable": cLDhcpStatsConfigTable,
       "cLDhcpStatsConfigEntry": cLDhcpStatsConfigEntry,
       "cLDhcpServerInetAddressType": cLDhcpServerInetAddressType,
       "cLDhcpServerInetAddress": cLDhcpServerInetAddress,
       "cLDhcpClearStats": cLDhcpClearStats,
       "cLDhcpClearDiscontinuityTime": cLDhcpClearDiscontinuityTime,
       "ciscoLwappDhcpStats": ciscoLwappDhcpStats,
       "cLDhcpStatsShowTable": cLDhcpStatsShowTable,
       "cLDhcpStatsShowEntry": cLDhcpStatsShowEntry,
       "cLDhcpProxy": cLDhcpProxy,
       "cLDhcpDiscoverPackets": cLDhcpDiscoverPackets,
       "cLDhcpRequestPackets": cLDhcpRequestPackets,
       "cLDhcpDeclinePackets": cLDhcpDeclinePackets,
       "cLDhcpInformPackets": cLDhcpInformPackets,
       "cLDhcpReleasePackets": cLDhcpReleasePackets,
       "cLDhcpReplyPackets": cLDhcpReplyPackets,
       "cLDhcpOfferPackets": cLDhcpOfferPackets,
       "cLDhcpAckPackets": cLDhcpAckPackets,
       "cLDhcpNakPackets": cLDhcpNakPackets,
       "cLDhcpTxFailures": cLDhcpTxFailures,
       "cLDhcpLastResponseTime": cLDhcpLastResponseTime,
       "cLDhcpLastRequestTime": cLDhcpLastRequestTime,
       "cLDhcpRxDiscoverPackets": cLDhcpRxDiscoverPackets,
       "ciscoLwappDhcpScopeStats": ciscoLwappDhcpScopeStats,
       "cLDhcpScopeStatsTable": cLDhcpScopeStatsTable,
       "cLDhcpScopeStatsEntry": cLDhcpScopeStatsEntry,
       "cLDhcpScopeIndex": cLDhcpScopeIndex,
       "cLDhcpScopeAddressPoolUsage": cLDhcpScopeAddressPoolUsage,
       "cLDhcpScopeName": cLDhcpScopeName,
       "cLDhcpScopeAllocatedIP": cLDhcpScopeAllocatedIP,
       "cLDhcpScopeAvailableIP": cLDhcpScopeAvailableIP,
       "cLDhcpScopeDiscoverPkts": cLDhcpScopeDiscoverPkts,
       "cLDhcpScopeAckPkts": cLDhcpScopeAckPkts,
       "cLDhcpScopeOfferPkts": cLDhcpScopeOfferPkts,
       "cLDhcpScopeTotalAckPkts": cLDhcpScopeTotalAckPkts,
       "cLDhcpScopeRequestPkts": cLDhcpScopeRequestPkts,
       "cLDhcpScopeRequestGoodPkts": cLDhcpScopeRequestGoodPkts,
       "ciscoLwappDhcpMIBNotifObjects": ciscoLwappDhcpMIBNotifObjects,
       "cLDhcpTrapSet": cLDhcpTrapSet,
       "ciscoLwappDhcpMIBConform": ciscoLwappDhcpMIBConform,
       "ciscoLwappDhcpMIBCompliances": ciscoLwappDhcpMIBCompliances,
       "ciscoLwappDhcpMIBCompliance": ciscoLwappDhcpMIBCompliance,
       "ciscoLwappDhcpMIBGroups": ciscoLwappDhcpMIBGroups,
       "ciscoLwappDhcpMIBConfigGroup": ciscoLwappDhcpMIBConfigGroup}
)
