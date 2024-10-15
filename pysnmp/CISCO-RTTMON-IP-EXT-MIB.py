# SNMP MIB module (CISCO-RTTMON-IP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-IP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:49 2024
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

(rttMonCtrlAdminEntry,
 rttMonEchoAdminEntry,
 rttMonEchoPathAdminEntry,
 rttMonHistoryCollectionEntry,
 rttMonLpdGrpStatsEntry,
 rttMonStatsCollectEntry) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminEntry",
    "rttMonEchoAdminEntry",
    "rttMonEchoPathAdminEntry",
    "rttMonHistoryCollectionEntry",
    "rttMonLpdGrpStatsEntry",
    "rttMonStatsCollectEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IPv6FlowLabelOrAny,) = mibBuilder.importSymbols(
    "IPV6-FLOW-LABEL-MIB",
    "IPv6FlowLabelOrAny")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoRttMonIPExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572)
)
ciscoRttMonIPExtMIB.setRevisions(
        ("2006-08-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrttMonIPExtObjects_ObjectIdentity = ObjectIdentity
crttMonIPExtObjects = _CrttMonIPExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1)
)
_CrttMonIPEchoAdminTable_Object = MibTable
crttMonIPEchoAdminTable = _CrttMonIPEchoAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTable.setStatus("current")
_CrttMonIPEchoAdminEntry_Object = MibTableRow
crttMonIPEchoAdminEntry = _CrttMonIPEchoAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoAdminEntry.setStatus("current")


class _CrttMonIPEchoAdminTargetAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminTargetAddrType based on InetAddressType"""


_CrttMonIPEchoAdminTargetAddrType_Object = MibTableColumn
crttMonIPEchoAdminTargetAddrType = _CrttMonIPEchoAdminTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 1),
    _CrttMonIPEchoAdminTargetAddrType_Type()
)
crttMonIPEchoAdminTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTargetAddrType.setStatus("current")
_CrttMonIPEchoAdminTargetAddress_Type = InetAddress
_CrttMonIPEchoAdminTargetAddress_Object = MibTableColumn
crttMonIPEchoAdminTargetAddress = _CrttMonIPEchoAdminTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 2),
    _CrttMonIPEchoAdminTargetAddress_Type()
)
crttMonIPEchoAdminTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminTargetAddress.setStatus("current")


class _CrttMonIPEchoAdminSourceAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminSourceAddrType based on InetAddressType"""


_CrttMonIPEchoAdminSourceAddrType_Object = MibTableColumn
crttMonIPEchoAdminSourceAddrType = _CrttMonIPEchoAdminSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 3),
    _CrttMonIPEchoAdminSourceAddrType_Type()
)
crttMonIPEchoAdminSourceAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminSourceAddrType.setStatus("current")
_CrttMonIPEchoAdminSourceAddress_Type = InetAddress
_CrttMonIPEchoAdminSourceAddress_Object = MibTableColumn
crttMonIPEchoAdminSourceAddress = _CrttMonIPEchoAdminSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 4),
    _CrttMonIPEchoAdminSourceAddress_Type()
)
crttMonIPEchoAdminSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminSourceAddress.setStatus("current")


class _CrttMonIPEchoAdminNameServerAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminNameServerAddrType based on InetAddressType"""


_CrttMonIPEchoAdminNameServerAddrType_Object = MibTableColumn
crttMonIPEchoAdminNameServerAddrType = _CrttMonIPEchoAdminNameServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 5),
    _CrttMonIPEchoAdminNameServerAddrType_Type()
)
crttMonIPEchoAdminNameServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminNameServerAddrType.setStatus("current")
_CrttMonIPEchoAdminNameServerAddress_Type = InetAddress
_CrttMonIPEchoAdminNameServerAddress_Object = MibTableColumn
crttMonIPEchoAdminNameServerAddress = _CrttMonIPEchoAdminNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 6),
    _CrttMonIPEchoAdminNameServerAddress_Type()
)
crttMonIPEchoAdminNameServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminNameServerAddress.setStatus("current")


class _CrttMonIPEchoAdminLSPSelAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoAdminLSPSelAddrType based on InetAddressType"""


_CrttMonIPEchoAdminLSPSelAddrType_Object = MibTableColumn
crttMonIPEchoAdminLSPSelAddrType = _CrttMonIPEchoAdminLSPSelAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 7),
    _CrttMonIPEchoAdminLSPSelAddrType_Type()
)
crttMonIPEchoAdminLSPSelAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminLSPSelAddrType.setStatus("current")
_CrttMonIPEchoAdminLSPSelAddress_Type = InetAddress
_CrttMonIPEchoAdminLSPSelAddress_Object = MibTableColumn
crttMonIPEchoAdminLSPSelAddress = _CrttMonIPEchoAdminLSPSelAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 8),
    _CrttMonIPEchoAdminLSPSelAddress_Type()
)
crttMonIPEchoAdminLSPSelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminLSPSelAddress.setStatus("current")


class _CrttMonIPEchoAdminDscp_Type(DscpOrAny):
    """Custom type crttMonIPEchoAdminDscp based on DscpOrAny"""
    defaultValue = -1


_CrttMonIPEchoAdminDscp_Object = MibTableColumn
crttMonIPEchoAdminDscp = _CrttMonIPEchoAdminDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 9),
    _CrttMonIPEchoAdminDscp_Type()
)
crttMonIPEchoAdminDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminDscp.setStatus("current")
_CrttMonIPEchoAdminFlowLabel_Type = IPv6FlowLabelOrAny
_CrttMonIPEchoAdminFlowLabel_Object = MibTableColumn
crttMonIPEchoAdminFlowLabel = _CrttMonIPEchoAdminFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 1, 1, 10),
    _CrttMonIPEchoAdminFlowLabel_Type()
)
crttMonIPEchoAdminFlowLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoAdminFlowLabel.setStatus("current")
_CrttMonIPLatestRttOperTable_Object = MibTable
crttMonIPLatestRttOperTable = _CrttMonIPLatestRttOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2)
)
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperTable.setStatus("current")
_CrttMonIPLatestRttOperEntry_Object = MibTableRow
crttMonIPLatestRttOperEntry = _CrttMonIPLatestRttOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1)
)
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperEntry.setStatus("current")


class _CrttMonIPLatestRttOperAddressType_Type(InetAddressType):
    """Custom type crttMonIPLatestRttOperAddressType based on InetAddressType"""


_CrttMonIPLatestRttOperAddressType_Object = MibTableColumn
crttMonIPLatestRttOperAddressType = _CrttMonIPLatestRttOperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 1),
    _CrttMonIPLatestRttOperAddressType_Type()
)
crttMonIPLatestRttOperAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperAddressType.setStatus("current")
_CrttMonIPLatestRttOperAddress_Type = InetAddress
_CrttMonIPLatestRttOperAddress_Object = MibTableColumn
crttMonIPLatestRttOperAddress = _CrttMonIPLatestRttOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 2, 1, 2),
    _CrttMonIPLatestRttOperAddress_Type()
)
crttMonIPLatestRttOperAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crttMonIPLatestRttOperAddress.setStatus("current")
_CrttMonIPEchoPathAdminTable_Object = MibTable
crttMonIPEchoPathAdminTable = _CrttMonIPEchoPathAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3)
)
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminTable.setStatus("current")
_CrttMonIPEchoPathAdminEntry_Object = MibTableRow
crttMonIPEchoPathAdminEntry = _CrttMonIPEchoPathAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1)
)
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminEntry.setStatus("current")


class _CrttMonIPEchoPathAdminHopAddrType_Type(InetAddressType):
    """Custom type crttMonIPEchoPathAdminHopAddrType based on InetAddressType"""


_CrttMonIPEchoPathAdminHopAddrType_Object = MibTableColumn
crttMonIPEchoPathAdminHopAddrType = _CrttMonIPEchoPathAdminHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 1),
    _CrttMonIPEchoPathAdminHopAddrType_Type()
)
crttMonIPEchoPathAdminHopAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminHopAddrType.setStatus("current")
_CrttMonIPEchoPathAdminHopAddress_Type = InetAddress
_CrttMonIPEchoPathAdminHopAddress_Object = MibTableColumn
crttMonIPEchoPathAdminHopAddress = _CrttMonIPEchoPathAdminHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 3, 1, 2),
    _CrttMonIPEchoPathAdminHopAddress_Type()
)
crttMonIPEchoPathAdminHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crttMonIPEchoPathAdminHopAddress.setStatus("current")
_CrttMonIPStatsCollectTable_Object = MibTable
crttMonIPStatsCollectTable = _CrttMonIPStatsCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4)
)
if mibBuilder.loadTexts:
    crttMonIPStatsCollectTable.setStatus("current")
_CrttMonIPStatsCollectEntry_Object = MibTableRow
crttMonIPStatsCollectEntry = _CrttMonIPStatsCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1)
)
if mibBuilder.loadTexts:
    crttMonIPStatsCollectEntry.setStatus("current")


class _CrttMonIPStatsCollectAddressType_Type(InetAddressType):
    """Custom type crttMonIPStatsCollectAddressType based on InetAddressType"""


_CrttMonIPStatsCollectAddressType_Object = MibTableColumn
crttMonIPStatsCollectAddressType = _CrttMonIPStatsCollectAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 1),
    _CrttMonIPStatsCollectAddressType_Type()
)
crttMonIPStatsCollectAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPStatsCollectAddressType.setStatus("current")
_CrttMonIPStatsCollectAddress_Type = InetAddress
_CrttMonIPStatsCollectAddress_Object = MibTableColumn
crttMonIPStatsCollectAddress = _CrttMonIPStatsCollectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 4, 1, 2),
    _CrttMonIPStatsCollectAddress_Type()
)
crttMonIPStatsCollectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPStatsCollectAddress.setStatus("current")
_CrttMonIPLpdGrpStatsTable_Object = MibTable
crttMonIPLpdGrpStatsTable = _CrttMonIPLpdGrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5)
)
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTable.setStatus("current")
_CrttMonIPLpdGrpStatsEntry_Object = MibTableRow
crttMonIPLpdGrpStatsEntry = _CrttMonIPLpdGrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1)
)
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsEntry.setStatus("current")


class _CrttMonIPLpdGrpStatsTargetPEAddrType_Type(InetAddressType):
    """Custom type crttMonIPLpdGrpStatsTargetPEAddrType based on InetAddressType"""


_CrttMonIPLpdGrpStatsTargetPEAddrType_Object = MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddrType = _CrttMonIPLpdGrpStatsTargetPEAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 1),
    _CrttMonIPLpdGrpStatsTargetPEAddrType_Type()
)
crttMonIPLpdGrpStatsTargetPEAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTargetPEAddrType.setStatus("current")
_CrttMonIPLpdGrpStatsTargetPEAddr_Type = InetAddress
_CrttMonIPLpdGrpStatsTargetPEAddr_Object = MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddr = _CrttMonIPLpdGrpStatsTargetPEAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 5, 1, 2),
    _CrttMonIPLpdGrpStatsTargetPEAddr_Type()
)
crttMonIPLpdGrpStatsTargetPEAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPLpdGrpStatsTargetPEAddr.setStatus("current")
_CrttMonIPHistoryCollectionTable_Object = MibTable
crttMonIPHistoryCollectionTable = _CrttMonIPHistoryCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6)
)
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionTable.setStatus("current")
_CrttMonIPHistoryCollectionEntry_Object = MibTableRow
crttMonIPHistoryCollectionEntry = _CrttMonIPHistoryCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1)
)
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionEntry.setStatus("current")


class _CrttMonIPHistoryCollectionAddrType_Type(InetAddressType):
    """Custom type crttMonIPHistoryCollectionAddrType based on InetAddressType"""


_CrttMonIPHistoryCollectionAddrType_Object = MibTableColumn
crttMonIPHistoryCollectionAddrType = _CrttMonIPHistoryCollectionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 1),
    _CrttMonIPHistoryCollectionAddrType_Type()
)
crttMonIPHistoryCollectionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionAddrType.setStatus("current")
_CrttMonIPHistoryCollectionAddress_Type = InetAddress
_CrttMonIPHistoryCollectionAddress_Object = MibTableColumn
crttMonIPHistoryCollectionAddress = _CrttMonIPHistoryCollectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 1, 6, 1, 2),
    _CrttMonIPHistoryCollectionAddress_Type()
)
crttMonIPHistoryCollectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crttMonIPHistoryCollectionAddress.setStatus("current")
_CiscoRttMonIPExtMibConformance_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibConformance = _CiscoRttMonIPExtMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2)
)
_CiscoRttMonIPExtMibCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibCompliances = _CiscoRttMonIPExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1)
)
_CiscoRttMonIPExtMibGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonIPExtMibGroups = _CiscoRttMonIPExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2)
)
rttMonEchoAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPEchoAdminEntry")
)
crttMonIPEchoAdminEntry.setIndexNames(*rttMonEchoAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPLatestRttOperEntry")
)
crttMonIPLatestRttOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonEchoPathAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPEchoPathAdminEntry")
)
crttMonIPEchoPathAdminEntry.setIndexNames(*rttMonEchoPathAdminEntry.getIndexNames())
rttMonStatsCollectEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPStatsCollectEntry")
)
crttMonIPStatsCollectEntry.setIndexNames(*rttMonStatsCollectEntry.getIndexNames())
rttMonLpdGrpStatsEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPLpdGrpStatsEntry")
)
crttMonIPLpdGrpStatsEntry.setIndexNames(*rttMonLpdGrpStatsEntry.getIndexNames())
rttMonHistoryCollectionEntry.registerAugmentions(
    ("CISCO-RTTMON-IP-EXT-MIB",
     "crttMonIPHistoryCollectionEntry")
)
crttMonIPHistoryCollectionEntry.setIndexNames(*rttMonHistoryCollectionEntry.getIndexNames())

# Managed Objects groups

ciscoIPExtCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 2, 1)
)
ciscoIPExtCtrlGroupRev1.setObjects(
      *(("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminTargetAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminSourceAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminNameServerAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminLSPSelAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminDscp"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoAdminFlowLabel"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddressType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLatestRttOperAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPEchoPathAdminHopAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddressType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPStatsCollectAddress"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPLpdGrpStatsTargetPEAddr"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddrType"),
        ("CISCO-RTTMON-IP-EXT-MIB", "crttMonIPHistoryCollectionAddress"))
)
if mibBuilder.loadTexts:
    ciscoIPExtCtrlGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRttMonIPExtMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 572, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRttMonIPExtMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-IP-EXT-MIB",
    **{"ciscoRttMonIPExtMIB": ciscoRttMonIPExtMIB,
       "crttMonIPExtObjects": crttMonIPExtObjects,
       "crttMonIPEchoAdminTable": crttMonIPEchoAdminTable,
       "crttMonIPEchoAdminEntry": crttMonIPEchoAdminEntry,
       "crttMonIPEchoAdminTargetAddrType": crttMonIPEchoAdminTargetAddrType,
       "crttMonIPEchoAdminTargetAddress": crttMonIPEchoAdminTargetAddress,
       "crttMonIPEchoAdminSourceAddrType": crttMonIPEchoAdminSourceAddrType,
       "crttMonIPEchoAdminSourceAddress": crttMonIPEchoAdminSourceAddress,
       "crttMonIPEchoAdminNameServerAddrType": crttMonIPEchoAdminNameServerAddrType,
       "crttMonIPEchoAdminNameServerAddress": crttMonIPEchoAdminNameServerAddress,
       "crttMonIPEchoAdminLSPSelAddrType": crttMonIPEchoAdminLSPSelAddrType,
       "crttMonIPEchoAdminLSPSelAddress": crttMonIPEchoAdminLSPSelAddress,
       "crttMonIPEchoAdminDscp": crttMonIPEchoAdminDscp,
       "crttMonIPEchoAdminFlowLabel": crttMonIPEchoAdminFlowLabel,
       "crttMonIPLatestRttOperTable": crttMonIPLatestRttOperTable,
       "crttMonIPLatestRttOperEntry": crttMonIPLatestRttOperEntry,
       "crttMonIPLatestRttOperAddressType": crttMonIPLatestRttOperAddressType,
       "crttMonIPLatestRttOperAddress": crttMonIPLatestRttOperAddress,
       "crttMonIPEchoPathAdminTable": crttMonIPEchoPathAdminTable,
       "crttMonIPEchoPathAdminEntry": crttMonIPEchoPathAdminEntry,
       "crttMonIPEchoPathAdminHopAddrType": crttMonIPEchoPathAdminHopAddrType,
       "crttMonIPEchoPathAdminHopAddress": crttMonIPEchoPathAdminHopAddress,
       "crttMonIPStatsCollectTable": crttMonIPStatsCollectTable,
       "crttMonIPStatsCollectEntry": crttMonIPStatsCollectEntry,
       "crttMonIPStatsCollectAddressType": crttMonIPStatsCollectAddressType,
       "crttMonIPStatsCollectAddress": crttMonIPStatsCollectAddress,
       "crttMonIPLpdGrpStatsTable": crttMonIPLpdGrpStatsTable,
       "crttMonIPLpdGrpStatsEntry": crttMonIPLpdGrpStatsEntry,
       "crttMonIPLpdGrpStatsTargetPEAddrType": crttMonIPLpdGrpStatsTargetPEAddrType,
       "crttMonIPLpdGrpStatsTargetPEAddr": crttMonIPLpdGrpStatsTargetPEAddr,
       "crttMonIPHistoryCollectionTable": crttMonIPHistoryCollectionTable,
       "crttMonIPHistoryCollectionEntry": crttMonIPHistoryCollectionEntry,
       "crttMonIPHistoryCollectionAddrType": crttMonIPHistoryCollectionAddrType,
       "crttMonIPHistoryCollectionAddress": crttMonIPHistoryCollectionAddress,
       "ciscoRttMonIPExtMibConformance": ciscoRttMonIPExtMibConformance,
       "ciscoRttMonIPExtMibCompliances": ciscoRttMonIPExtMibCompliances,
       "ciscoRttMonIPExtMibComplianceRev1": ciscoRttMonIPExtMibComplianceRev1,
       "ciscoRttMonIPExtMibGroups": ciscoRttMonIPExtMibGroups,
       "ciscoIPExtCtrlGroupRev1": ciscoIPExtCtrlGroupRev1}
)
