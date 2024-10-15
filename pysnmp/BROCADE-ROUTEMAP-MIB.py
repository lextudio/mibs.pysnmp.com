# SNMP MIB module (BROCADE-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-ROUTEMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:32 2024
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

(AclNumber,
 Action) = mibBuilder.importSymbols(
    "FOUNDRY-SN-IP-ACL-MIB",
    "AclNumber",
    "Action")

(FdryVlanIdOrNoneTC,
 brcdRouteMap) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "FdryVlanIdOrNoneTC",
    "brcdRouteMap")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

brcdRouteMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1)
)
brcdRouteMapMIB.setRevisions(
        ("2011-11-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdRouteMapConfig_ObjectIdentity = ObjectIdentity
brcdRouteMapConfig = _BrcdRouteMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1)
)
_BrcdRouteMapTable_Object = MibTable
brcdRouteMapTable = _BrcdRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    brcdRouteMapTable.setStatus("current")
_BrcdRouteMapEntry_Object = MibTableRow
brcdRouteMapEntry = _BrcdRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1)
)
brcdRouteMapEntry.setIndexNames(
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapName"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapSequence"),
)
if mibBuilder.loadTexts:
    brcdRouteMapEntry.setStatus("current")
_BrcdRouteMapName_Type = DisplayString
_BrcdRouteMapName_Object = MibTableColumn
brcdRouteMapName = _BrcdRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1, 1),
    _BrcdRouteMapName_Type()
)
brcdRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapName.setStatus("current")
_BrcdRouteMapSequence_Type = Unsigned32
_BrcdRouteMapSequence_Object = MibTableColumn
brcdRouteMapSequence = _BrcdRouteMapSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1, 2),
    _BrcdRouteMapSequence_Type()
)
brcdRouteMapSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapSequence.setStatus("current")
_BrcdRouteMapAction_Type = Action
_BrcdRouteMapAction_Object = MibTableColumn
brcdRouteMapAction = _BrcdRouteMapAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1, 3),
    _BrcdRouteMapAction_Type()
)
brcdRouteMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapAction.setStatus("current")
_BrcdRouteMapRuleName_Type = DisplayString
_BrcdRouteMapRuleName_Object = MibTableColumn
brcdRouteMapRuleName = _BrcdRouteMapRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1, 4),
    _BrcdRouteMapRuleName_Type()
)
brcdRouteMapRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapRuleName.setStatus("current")
_BrcdRouteMapRowStatus_Type = RowStatus
_BrcdRouteMapRowStatus_Object = MibTableColumn
brcdRouteMapRowStatus = _BrcdRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 1, 1, 5),
    _BrcdRouteMapRowStatus_Type()
)
brcdRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapRowStatus.setStatus("current")
_BrcdRouteMapMatchTable_Object = MibTable
brcdRouteMapMatchTable = _BrcdRouteMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brcdRouteMapMatchTable.setStatus("current")
_BrcdRouteMapMatchEntry_Object = MibTableRow
brcdRouteMapMatchEntry = _BrcdRouteMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1)
)
brcdRouteMapMatchEntry.setIndexNames(
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapName"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapSequence"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapMatchSequence"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapMatchType"),
)
if mibBuilder.loadTexts:
    brcdRouteMapMatchEntry.setStatus("current")
_BrcdRouteMapMatchSequence_Type = Integer32
_BrcdRouteMapMatchSequence_Object = MibTableColumn
brcdRouteMapMatchSequence = _BrcdRouteMapMatchSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1, 1),
    _BrcdRouteMapMatchSequence_Type()
)
brcdRouteMapMatchSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapMatchSequence.setStatus("current")


class _BrcdRouteMapMatchType_Type(Integer32):
    """Custom type brcdRouteMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("matchAsPath", 1),
          ("matchBgpCommunityName", 2),
          ("matchBgpCommunityNameExact", 3),
          ("matchBgpExtCommunityNumber", 4),
          ("matchInterfaces", 5),
          ("matchIpv4AddressAclNames", 6),
          ("matchIpv4AddressAclNumbers", 7),
          ("matchIpv4AddressPrefixList", 8),
          ("matchIpv4NextHopAclNames", 9),
          ("matchIpv4NextHopAclNumbers", 10),
          ("matchIpv4NextHopPrefixList", 11),
          ("matchIpv4RouteSourceAclNames", 12),
          ("matchIpv4RouteSourceAclNumbers", 13),
          ("matchIpv4RouteSourcePrefixList", 14),
          ("matchIpv6AddressAclNames", 15),
          ("matchIpv6AddressPrefixList", 16),
          ("matchIpv6NextHopPrefixList", 17),
          ("matchIpv6RouteSourcePrefixList", 18),
          ("matchMetric", 19),
          ("matchRouteType", 21),
          ("matchRoutingProtocol", 20),
          ("matchTags", 22),
          ("matchUndefined", 0))
    )


_BrcdRouteMapMatchType_Type.__name__ = "Integer32"
_BrcdRouteMapMatchType_Object = MibTableColumn
brcdRouteMapMatchType = _BrcdRouteMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1, 2),
    _BrcdRouteMapMatchType_Type()
)
brcdRouteMapMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapMatchType.setStatus("current")
_BrcdRouteMapMatchValue_Type = DisplayString
_BrcdRouteMapMatchValue_Object = MibTableColumn
brcdRouteMapMatchValue = _BrcdRouteMapMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1, 3),
    _BrcdRouteMapMatchValue_Type()
)
brcdRouteMapMatchValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapMatchValue.setStatus("current")
_BrcdRouteMapMatchCliString_Type = DisplayString
_BrcdRouteMapMatchCliString_Object = MibTableColumn
brcdRouteMapMatchCliString = _BrcdRouteMapMatchCliString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1, 4),
    _BrcdRouteMapMatchCliString_Type()
)
brcdRouteMapMatchCliString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRouteMapMatchCliString.setStatus("current")
_BrcdRouteMapMatchRowStatus_Type = RowStatus
_BrcdRouteMapMatchRowStatus_Object = MibTableColumn
brcdRouteMapMatchRowStatus = _BrcdRouteMapMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 2, 1, 5),
    _BrcdRouteMapMatchRowStatus_Type()
)
brcdRouteMapMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapMatchRowStatus.setStatus("current")
_BrcdRouteMapSetTable_Object = MibTable
brcdRouteMapSetTable = _BrcdRouteMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3)
)
if mibBuilder.loadTexts:
    brcdRouteMapSetTable.setStatus("current")
_BrcdRouteMapSetEntry_Object = MibTableRow
brcdRouteMapSetEntry = _BrcdRouteMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1)
)
brcdRouteMapSetEntry.setIndexNames(
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapName"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapSequence"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapSetSequence"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapSetType"),
)
if mibBuilder.loadTexts:
    brcdRouteMapSetEntry.setStatus("current")
_BrcdRouteMapSetSequence_Type = Integer32
_BrcdRouteMapSetSequence_Object = MibTableColumn
brcdRouteMapSetSequence = _BrcdRouteMapSetSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1, 1),
    _BrcdRouteMapSetSequence_Type()
)
brcdRouteMapSetSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapSetSequence.setStatus("current")


class _BrcdRouteMapSetType_Type(Integer32):
    """Custom type brcdRouteMapSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("setAsPath", 1),
          ("setAutomaticTag", 2),
          ("setBgpOrigin", 26),
          ("setCommunityFlag", 5),
          ("setCommunityNumber", 4),
          ("setDampening", 6),
          ("setDeleteCommunityList", 3),
          ("setDistance", 7),
          ("setExtCommunityRT", 8),
          ("setExtCommunityRTAdditive", 9),
          ("setExtCommunitySOO", 10),
          ("setIsisLevel", 17),
          ("setLocalPreference", 18),
          ("setMetric", 20),
          ("setMetricType", 19),
          ("setNextHopFloodVlan", 21),
          ("setNextHopFloodVlanOutgoingDa", 23),
          ("setNextHopFloodVlanPreserveVlan", 22),
          ("setNextHopIpPeerAddr", 16),
          ("setNextHopIpTunnel", 24),
          ("setNextHopIpv4Addr", 12),
          ("setNextHopIpv4AddrWithPreserveVlan", 13),
          ("setNextHopIpv6Addr", 14),
          ("setNextHopIpv6AddrWithPreserveVlan", 15),
          ("setNextHopLsp", 25),
          ("setOutputInterfaces", 11),
          ("setTag", 27),
          ("setUnDefinedType", 0),
          ("setWeight", 28))
    )


_BrcdRouteMapSetType_Type.__name__ = "Integer32"
_BrcdRouteMapSetType_Object = MibTableColumn
brcdRouteMapSetType = _BrcdRouteMapSetType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1, 2),
    _BrcdRouteMapSetType_Type()
)
brcdRouteMapSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapSetType.setStatus("current")
_BrcdRouteMapSetValue_Type = DisplayString
_BrcdRouteMapSetValue_Object = MibTableColumn
brcdRouteMapSetValue = _BrcdRouteMapSetValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1, 3),
    _BrcdRouteMapSetValue_Type()
)
brcdRouteMapSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapSetValue.setStatus("current")
_BrcdRouteMapSetCliString_Type = DisplayString
_BrcdRouteMapSetCliString_Object = MibTableColumn
brcdRouteMapSetCliString = _BrcdRouteMapSetCliString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1, 4),
    _BrcdRouteMapSetCliString_Type()
)
brcdRouteMapSetCliString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRouteMapSetCliString.setStatus("current")
_BrcdRouteMapSetRowStatus_Type = RowStatus
_BrcdRouteMapSetRowStatus_Object = MibTableColumn
brcdRouteMapSetRowStatus = _BrcdRouteMapSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 3, 1, 5),
    _BrcdRouteMapSetRowStatus_Type()
)
brcdRouteMapSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapSetRowStatus.setStatus("current")
_BrcdRouteMapBindTable_Object = MibTable
brcdRouteMapBindTable = _BrcdRouteMapBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4)
)
if mibBuilder.loadTexts:
    brcdRouteMapBindTable.setStatus("current")
_BrcdRouteMapBindEntry_Object = MibTableRow
brcdRouteMapBindEntry = _BrcdRouteMapBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4, 1)
)
brcdRouteMapBindEntry.setIndexNames(
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapBindIfIndex"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRouteMapBindIpType"),
)
if mibBuilder.loadTexts:
    brcdRouteMapBindEntry.setStatus("current")
_BrcdRouteMapBindIfIndex_Type = InterfaceIndex
_BrcdRouteMapBindIfIndex_Object = MibTableColumn
brcdRouteMapBindIfIndex = _BrcdRouteMapBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4, 1, 1),
    _BrcdRouteMapBindIfIndex_Type()
)
brcdRouteMapBindIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapBindIfIndex.setStatus("current")
_BrcdRouteMapBindIpType_Type = InetAddressType
_BrcdRouteMapBindIpType_Object = MibTableColumn
brcdRouteMapBindIpType = _BrcdRouteMapBindIpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4, 1, 2),
    _BrcdRouteMapBindIpType_Type()
)
brcdRouteMapBindIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRouteMapBindIpType.setStatus("current")
_BrcdRouteMapBindMapName_Type = DisplayString
_BrcdRouteMapBindMapName_Object = MibTableColumn
brcdRouteMapBindMapName = _BrcdRouteMapBindMapName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4, 1, 3),
    _BrcdRouteMapBindMapName_Type()
)
brcdRouteMapBindMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapBindMapName.setStatus("current")
_BrcdRouteMapBindRowStatus_Type = RowStatus
_BrcdRouteMapBindRowStatus_Object = MibTableColumn
brcdRouteMapBindRowStatus = _BrcdRouteMapBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 1, 4, 1, 4),
    _BrcdRouteMapBindRowStatus_Type()
)
brcdRouteMapBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdRouteMapBindRowStatus.setStatus("current")
_BrcdRouteMapShow_ObjectIdentity = ObjectIdentity
brcdRouteMapShow = _BrcdRouteMapShow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2)
)
_BrcdRMapRuleDisplayTable_Object = MibTable
brcdRMapRuleDisplayTable = _BrcdRMapRuleDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayTable.setStatus("current")
_BrcdRMapRuleDisplayEntry_Object = MibTableRow
brcdRMapRuleDisplayEntry = _BrcdRMapRuleDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1)
)
brcdRMapRuleDisplayEntry.setIndexNames(
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRMapRuleDisplayRuleName"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRMapRuleDisplayRouteMapName"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRMapRuleDisplaySequence"),
    (0, "BROCADE-ROUTEMAP-MIB", "brcdRMapRuleDisplayIpType"),
)
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayEntry.setStatus("current")
_BrcdRMapRuleDisplayRuleName_Type = DisplayString
_BrcdRMapRuleDisplayRuleName_Object = MibTableColumn
brcdRMapRuleDisplayRuleName = _BrcdRMapRuleDisplayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 1),
    _BrcdRMapRuleDisplayRuleName_Type()
)
brcdRMapRuleDisplayRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayRuleName.setStatus("current")
_BrcdRMapRuleDisplayRouteMapName_Type = DisplayString
_BrcdRMapRuleDisplayRouteMapName_Object = MibTableColumn
brcdRMapRuleDisplayRouteMapName = _BrcdRMapRuleDisplayRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 2),
    _BrcdRMapRuleDisplayRouteMapName_Type()
)
brcdRMapRuleDisplayRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayRouteMapName.setStatus("current")
_BrcdRMapRuleDisplaySequence_Type = Unsigned32
_BrcdRMapRuleDisplaySequence_Object = MibTableColumn
brcdRMapRuleDisplaySequence = _BrcdRMapRuleDisplaySequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 3),
    _BrcdRMapRuleDisplaySequence_Type()
)
brcdRMapRuleDisplaySequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplaySequence.setStatus("current")
_BrcdRMapRuleDisplayIpType_Type = InetAddressType
_BrcdRMapRuleDisplayIpType_Object = MibTableColumn
brcdRMapRuleDisplayIpType = _BrcdRMapRuleDisplayIpType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 4),
    _BrcdRMapRuleDisplayIpType_Type()
)
brcdRMapRuleDisplayIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayIpType.setStatus("current")
_BrcdRMapRuleDisplayInputInterfaceList_Type = DisplayString
_BrcdRMapRuleDisplayInputInterfaceList_Object = MibTableColumn
brcdRMapRuleDisplayInputInterfaceList = _BrcdRMapRuleDisplayInputInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 5),
    _BrcdRMapRuleDisplayInputInterfaceList_Type()
)
brcdRMapRuleDisplayInputInterfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayInputInterfaceList.setStatus("current")
_BrcdRMapRuleDisplayAclMatchFilter_Type = DisplayString
_BrcdRMapRuleDisplayAclMatchFilter_Object = MibTableColumn
brcdRMapRuleDisplayAclMatchFilter = _BrcdRMapRuleDisplayAclMatchFilter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 6),
    _BrcdRMapRuleDisplayAclMatchFilter_Type()
)
brcdRMapRuleDisplayAclMatchFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayAclMatchFilter.setStatus("current")
_BrcdRMapRuleDisplayOutputVlan_Type = DisplayString
_BrcdRMapRuleDisplayOutputVlan_Object = MibTableColumn
brcdRMapRuleDisplayOutputVlan = _BrcdRMapRuleDisplayOutputVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 7),
    _BrcdRMapRuleDisplayOutputVlan_Type()
)
brcdRMapRuleDisplayOutputVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayOutputVlan.setStatus("current")
_BrcdRMapRuleDisplayOutputPort_Type = DisplayString
_BrcdRMapRuleDisplayOutputPort_Object = MibTableColumn
brcdRMapRuleDisplayOutputPort = _BrcdRMapRuleDisplayOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 8),
    _BrcdRMapRuleDisplayOutputPort_Type()
)
brcdRMapRuleDisplayOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayOutputPort.setStatus("current")
_BrcdRMapRuleDisplayOutputIPAddress_Type = DisplayString
_BrcdRMapRuleDisplayOutputIPAddress_Object = MibTableColumn
brcdRMapRuleDisplayOutputIPAddress = _BrcdRMapRuleDisplayOutputIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39, 1, 2, 1, 1, 9),
    _BrcdRMapRuleDisplayOutputIPAddress_Type()
)
brcdRMapRuleDisplayOutputIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdRMapRuleDisplayOutputIPAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-ROUTEMAP-MIB",
    **{"brcdRouteMapMIB": brcdRouteMapMIB,
       "brcdRouteMapConfig": brcdRouteMapConfig,
       "brcdRouteMapTable": brcdRouteMapTable,
       "brcdRouteMapEntry": brcdRouteMapEntry,
       "brcdRouteMapName": brcdRouteMapName,
       "brcdRouteMapSequence": brcdRouteMapSequence,
       "brcdRouteMapAction": brcdRouteMapAction,
       "brcdRouteMapRuleName": brcdRouteMapRuleName,
       "brcdRouteMapRowStatus": brcdRouteMapRowStatus,
       "brcdRouteMapMatchTable": brcdRouteMapMatchTable,
       "brcdRouteMapMatchEntry": brcdRouteMapMatchEntry,
       "brcdRouteMapMatchSequence": brcdRouteMapMatchSequence,
       "brcdRouteMapMatchType": brcdRouteMapMatchType,
       "brcdRouteMapMatchValue": brcdRouteMapMatchValue,
       "brcdRouteMapMatchCliString": brcdRouteMapMatchCliString,
       "brcdRouteMapMatchRowStatus": brcdRouteMapMatchRowStatus,
       "brcdRouteMapSetTable": brcdRouteMapSetTable,
       "brcdRouteMapSetEntry": brcdRouteMapSetEntry,
       "brcdRouteMapSetSequence": brcdRouteMapSetSequence,
       "brcdRouteMapSetType": brcdRouteMapSetType,
       "brcdRouteMapSetValue": brcdRouteMapSetValue,
       "brcdRouteMapSetCliString": brcdRouteMapSetCliString,
       "brcdRouteMapSetRowStatus": brcdRouteMapSetRowStatus,
       "brcdRouteMapBindTable": brcdRouteMapBindTable,
       "brcdRouteMapBindEntry": brcdRouteMapBindEntry,
       "brcdRouteMapBindIfIndex": brcdRouteMapBindIfIndex,
       "brcdRouteMapBindIpType": brcdRouteMapBindIpType,
       "brcdRouteMapBindMapName": brcdRouteMapBindMapName,
       "brcdRouteMapBindRowStatus": brcdRouteMapBindRowStatus,
       "brcdRouteMapShow": brcdRouteMapShow,
       "brcdRMapRuleDisplayTable": brcdRMapRuleDisplayTable,
       "brcdRMapRuleDisplayEntry": brcdRMapRuleDisplayEntry,
       "brcdRMapRuleDisplayRuleName": brcdRMapRuleDisplayRuleName,
       "brcdRMapRuleDisplayRouteMapName": brcdRMapRuleDisplayRouteMapName,
       "brcdRMapRuleDisplaySequence": brcdRMapRuleDisplaySequence,
       "brcdRMapRuleDisplayIpType": brcdRMapRuleDisplayIpType,
       "brcdRMapRuleDisplayInputInterfaceList": brcdRMapRuleDisplayInputInterfaceList,
       "brcdRMapRuleDisplayAclMatchFilter": brcdRMapRuleDisplayAclMatchFilter,
       "brcdRMapRuleDisplayOutputVlan": brcdRMapRuleDisplayOutputVlan,
       "brcdRMapRuleDisplayOutputPort": brcdRMapRuleDisplayOutputPort,
       "brcdRMapRuleDisplayOutputIPAddress": brcdRMapRuleDisplayOutputIPAddress}
)
