# SNMP MIB module (DLINKSW-IP-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINKSW-IP-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:32 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwIPFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117)
)
dlinkSwIPFilterMIB.setRevisions(
        ("2016-06-08 00:00",
         "2016-06-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIPFilterNotifications_ObjectIdentity = ObjectIdentity
dIPFilterNotifications = _DIPFilterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 0)
)
_DIPFilterObjects_ObjectIdentity = ObjectIdentity
dIPFilterObjects = _DIPFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1)
)
_DRouteMapTable_Object = MibTable
dRouteMapTable = _DRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1)
)
if mibBuilder.loadTexts:
    dRouteMapTable.setStatus("current")
_DRouteMapEntry_Object = MibTableRow
dRouteMapEntry = _DRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1)
)
dRouteMapEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"),
)
if mibBuilder.loadTexts:
    dRouteMapEntry.setStatus("current")


class _DRouteMapName_Type(DisplayString):
    """Custom type dRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DRouteMapName_Type.__name__ = "DisplayString"
_DRouteMapName_Object = MibTableColumn
dRouteMapName = _DRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1, 1),
    _DRouteMapName_Type()
)
dRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dRouteMapName.setStatus("current")
_DRouteMapRowStatus_Type = RowStatus
_DRouteMapRowStatus_Object = MibTableColumn
dRouteMapRowStatus = _DRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1, 99),
    _DRouteMapRowStatus_Type()
)
dRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapRowStatus.setStatus("current")
_DRouteMapSeqTable_Object = MibTable
dRouteMapSeqTable = _DRouteMapSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2)
)
if mibBuilder.loadTexts:
    dRouteMapSeqTable.setStatus("current")
_DRouteMapSeqEntry_Object = MibTableRow
dRouteMapSeqEntry = _DRouteMapSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1)
)
dRouteMapSeqEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapSeqNum"),
)
if mibBuilder.loadTexts:
    dRouteMapSeqEntry.setStatus("current")


class _DRouteMapSeqNum_Type(Unsigned32):
    """Custom type dRouteMapSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DRouteMapSeqNum_Type.__name__ = "Unsigned32"
_DRouteMapSeqNum_Object = MibTableColumn
dRouteMapSeqNum = _DRouteMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 1),
    _DRouteMapSeqNum_Type()
)
dRouteMapSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dRouteMapSeqNum.setStatus("current")


class _DRouteMapSeqMatchAction_Type(Integer32):
    """Custom type dRouteMapSeqMatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DRouteMapSeqMatchAction_Type.__name__ = "Integer32"
_DRouteMapSeqMatchAction_Object = MibTableColumn
dRouteMapSeqMatchAction = _DRouteMapSeqMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 2),
    _DRouteMapSeqMatchAction_Type()
)
dRouteMapSeqMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapSeqMatchAction.setStatus("current")
_DRouteMapSeqRowStatus_Type = RowStatus
_DRouteMapSeqRowStatus_Object = MibTableColumn
dRouteMapSeqRowStatus = _DRouteMapSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 99),
    _DRouteMapSeqRowStatus_Type()
)
dRouteMapSeqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapSeqRowStatus.setStatus("current")
_DRouteMapClauseTable_Object = MibTable
dRouteMapClauseTable = _DRouteMapClauseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3)
)
if mibBuilder.loadTexts:
    dRouteMapClauseTable.setStatus("current")
_DRouteMapClauseEntry_Object = MibTableRow
dRouteMapClauseEntry = _DRouteMapClauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1)
)
dRouteMapClauseEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapSeqNum"),
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapClauseTypeId"),
    (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapClauseSubId"),
)
if mibBuilder.loadTexts:
    dRouteMapClauseEntry.setStatus("current")


class _DRouteMapClauseTypeId_Type(Integer32):
    """Custom type dRouteMapClauseTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              129,
              131,
              136,
              137,
              139,
              140,
              141,
              142,
              143,
              144)
        )
    )
    namedValues = NamedValues(
        *(("macthIpNexthop", 7),
          ("matchAsPath", 4),
          ("matchCommunity", 5),
          ("matchInterface", 10),
          ("matchIpAccessList", 1),
          ("matchIpNexthopPrefixList", 8),
          ("matchIpPrefixList", 2),
          ("matchIpRouteSource", 12),
          ("matchIpv6AccessList", 3),
          ("matchIpv6Nexthop", 13),
          ("matchIpv6NexthopPrefixList", 14),
          ("matchIpv6PrefixList", 15),
          ("matchMetric", 9),
          ("matchRouteType", 11),
          ("setAsPath", 136),
          ("setCommunity", 137),
          ("setDampening", 143),
          ("setIpNexthop", 129),
          ("setIpv6Nexthop", 131),
          ("setLocalPreference", 140),
          ("setMetric", 139),
          ("setMetricType", 144),
          ("setOrigin", 141),
          ("setWeight", 142))
    )


_DRouteMapClauseTypeId_Type.__name__ = "Integer32"
_DRouteMapClauseTypeId_Object = MibTableColumn
dRouteMapClauseTypeId = _DRouteMapClauseTypeId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 1),
    _DRouteMapClauseTypeId_Type()
)
dRouteMapClauseTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dRouteMapClauseTypeId.setStatus("current")


class _DRouteMapClauseSubId_Type(Integer32):
    """Custom type dRouteMapClauseSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DRouteMapClauseSubId_Type.__name__ = "Integer32"
_DRouteMapClauseSubId_Object = MibTableColumn
dRouteMapClauseSubId = _DRouteMapClauseSubId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 2),
    _DRouteMapClauseSubId_Type()
)
dRouteMapClauseSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dRouteMapClauseSubId.setStatus("current")


class _DRouteMapClauseAddOption_Type(Integer32):
    """Custom type dRouteMapClauseAddOption based on Integer32"""
    defaultValue = 0

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
        *(("additive", 2),
          ("communityNone", 3),
          ("exact", 1),
          ("notApplicable", 0))
    )


_DRouteMapClauseAddOption_Type.__name__ = "Integer32"
_DRouteMapClauseAddOption_Object = MibTableColumn
dRouteMapClauseAddOption = _DRouteMapClauseAddOption_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 3),
    _DRouteMapClauseAddOption_Type()
)
dRouteMapClauseAddOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapClauseAddOption.setStatus("current")


class _DRouteMapClauseElementValue_Type(DisplayString):
    """Custom type dRouteMapClauseElementValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DRouteMapClauseElementValue_Type.__name__ = "DisplayString"
_DRouteMapClauseElementValue_Object = MibTableColumn
dRouteMapClauseElementValue = _DRouteMapClauseElementValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 4),
    _DRouteMapClauseElementValue_Type()
)
dRouteMapClauseElementValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapClauseElementValue.setStatus("current")
_DRouteMapClauseRowStatus_Type = RowStatus
_DRouteMapClauseRowStatus_Object = MibTableColumn
dRouteMapClauseRowStatus = _DRouteMapClauseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 99),
    _DRouteMapClauseRowStatus_Type()
)
dRouteMapClauseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRouteMapClauseRowStatus.setStatus("current")
_DAccessListTable_Object = MibTable
dAccessListTable = _DAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4)
)
if mibBuilder.loadTexts:
    dAccessListTable.setStatus("current")
_DAccessListEntry_Object = MibTableRow
dAccessListEntry = _DAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1)
)
dAccessListEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListAddrType"),
)
if mibBuilder.loadTexts:
    dAccessListEntry.setStatus("current")


class _DAccessListName_Type(DisplayString):
    """Custom type dAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DAccessListName_Type.__name__ = "DisplayString"
_DAccessListName_Object = MibTableColumn
dAccessListName = _DAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 1),
    _DAccessListName_Type()
)
dAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAccessListName.setStatus("current")
_DAccessListAddrType_Type = InetAddressType
_DAccessListAddrType_Object = MibTableColumn
dAccessListAddrType = _DAccessListAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 2),
    _DAccessListAddrType_Type()
)
dAccessListAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAccessListAddrType.setStatus("current")
_DAccessListRowStatus_Type = RowStatus
_DAccessListRowStatus_Object = MibTableColumn
dAccessListRowStatus = _DAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 99),
    _DAccessListRowStatus_Type()
)
dAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAccessListRowStatus.setStatus("current")
_DAccessListRuleTable_Object = MibTable
dAccessListRuleTable = _DAccessListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5)
)
if mibBuilder.loadTexts:
    dAccessListRuleTable.setStatus("current")
_DAccessListRuleEntry_Object = MibTableRow
dAccessListRuleEntry = _DAccessListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1)
)
dAccessListRuleEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListAddrType"),
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRuleMatchAction"),
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRuleNetAddr"),
    (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRulePfxLen"),
)
if mibBuilder.loadTexts:
    dAccessListRuleEntry.setStatus("current")


class _DAccessListRuleMatchAction_Type(Integer32):
    """Custom type dAccessListRuleMatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DAccessListRuleMatchAction_Type.__name__ = "Integer32"
_DAccessListRuleMatchAction_Object = MibTableColumn
dAccessListRuleMatchAction = _DAccessListRuleMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 1),
    _DAccessListRuleMatchAction_Type()
)
dAccessListRuleMatchAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAccessListRuleMatchAction.setStatus("current")
_DAccessListRuleNetAddr_Type = InetAddress
_DAccessListRuleNetAddr_Object = MibTableColumn
dAccessListRuleNetAddr = _DAccessListRuleNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 2),
    _DAccessListRuleNetAddr_Type()
)
dAccessListRuleNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAccessListRuleNetAddr.setStatus("current")
_DAccessListRulePfxLen_Type = Integer32
_DAccessListRulePfxLen_Object = MibTableColumn
dAccessListRulePfxLen = _DAccessListRulePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 3),
    _DAccessListRulePfxLen_Type()
)
dAccessListRulePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAccessListRulePfxLen.setStatus("current")
_DAccessListRuleRowStatus_Type = RowStatus
_DAccessListRuleRowStatus_Object = MibTableColumn
dAccessListRuleRowStatus = _DAccessListRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 99),
    _DAccessListRuleRowStatus_Type()
)
dAccessListRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAccessListRuleRowStatus.setStatus("current")
_DPrefixListTable_Object = MibTable
dPrefixListTable = _DPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6)
)
if mibBuilder.loadTexts:
    dPrefixListTable.setStatus("current")
_DPrefixListEntry_Object = MibTableRow
dPrefixListEntry = _DPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1)
)
dPrefixListEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"),
)
if mibBuilder.loadTexts:
    dPrefixListEntry.setStatus("current")


class _DPrefixListName_Type(DisplayString):
    """Custom type dPrefixListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DPrefixListName_Type.__name__ = "DisplayString"
_DPrefixListName_Object = MibTableColumn
dPrefixListName = _DPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 1),
    _DPrefixListName_Type()
)
dPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPrefixListName.setStatus("current")
_DPrefixListAddrType_Type = InetAddressType
_DPrefixListAddrType_Object = MibTableColumn
dPrefixListAddrType = _DPrefixListAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 2),
    _DPrefixListAddrType_Type()
)
dPrefixListAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPrefixListAddrType.setStatus("current")
_DPrefixListRowStatus_Type = RowStatus
_DPrefixListRowStatus_Object = MibTableColumn
dPrefixListRowStatus = _DPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 99),
    _DPrefixListRowStatus_Type()
)
dPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRowStatus.setStatus("current")
_DPrefixListRuleTable_Object = MibTable
dPrefixListRuleTable = _DPrefixListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7)
)
if mibBuilder.loadTexts:
    dPrefixListRuleTable.setStatus("current")
_DPrefixListRuleEntry_Object = MibTableRow
dPrefixListRuleEntry = _DPrefixListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1)
)
dPrefixListRuleEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"),
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListRuleSeqNum"),
)
if mibBuilder.loadTexts:
    dPrefixListRuleEntry.setStatus("current")


class _DPrefixListRuleSeqNum_Type(Unsigned32):
    """Custom type dPrefixListRuleSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_DPrefixListRuleSeqNum_Type.__name__ = "Unsigned32"
_DPrefixListRuleSeqNum_Object = MibTableColumn
dPrefixListRuleSeqNum = _DPrefixListRuleSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 1),
    _DPrefixListRuleSeqNum_Type()
)
dPrefixListRuleSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPrefixListRuleSeqNum.setStatus("current")


class _DPrefixListRuleAction_Type(Integer32):
    """Custom type dPrefixListRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DPrefixListRuleAction_Type.__name__ = "Integer32"
_DPrefixListRuleAction_Object = MibTableColumn
dPrefixListRuleAction = _DPrefixListRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 2),
    _DPrefixListRuleAction_Type()
)
dPrefixListRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRuleAction.setStatus("current")
_DPrefixListRuleNetAddr_Type = InetAddress
_DPrefixListRuleNetAddr_Object = MibTableColumn
dPrefixListRuleNetAddr = _DPrefixListRuleNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 3),
    _DPrefixListRuleNetAddr_Type()
)
dPrefixListRuleNetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRuleNetAddr.setStatus("current")
_DPrefixListRulePrefixLen_Type = InetAddressPrefixLength
_DPrefixListRulePrefixLen_Object = MibTableColumn
dPrefixListRulePrefixLen = _DPrefixListRulePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 4),
    _DPrefixListRulePrefixLen_Type()
)
dPrefixListRulePrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRulePrefixLen.setStatus("current")


class _DPrefixListRuleGeValue_Type(Unsigned32):
    """Custom type dPrefixListRuleGeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_DPrefixListRuleGeValue_Type.__name__ = "Unsigned32"
_DPrefixListRuleGeValue_Object = MibTableColumn
dPrefixListRuleGeValue = _DPrefixListRuleGeValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 5),
    _DPrefixListRuleGeValue_Type()
)
dPrefixListRuleGeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRuleGeValue.setStatus("current")


class _DPrefixListRuleLeValue_Type(Unsigned32):
    """Custom type dPrefixListRuleLeValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_DPrefixListRuleLeValue_Type.__name__ = "Unsigned32"
_DPrefixListRuleLeValue_Object = MibTableColumn
dPrefixListRuleLeValue = _DPrefixListRuleLeValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 6),
    _DPrefixListRuleLeValue_Type()
)
dPrefixListRuleLeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRuleLeValue.setStatus("current")
_DPrefixListRuleHitCount_Type = Unsigned32
_DPrefixListRuleHitCount_Object = MibTableColumn
dPrefixListRuleHitCount = _DPrefixListRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 7),
    _DPrefixListRuleHitCount_Type()
)
dPrefixListRuleHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPrefixListRuleHitCount.setStatus("current")
_DPrefixListRuleRowStatus_Type = RowStatus
_DPrefixListRuleRowStatus_Object = MibTableColumn
dPrefixListRuleRowStatus = _DPrefixListRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 99),
    _DPrefixListRuleRowStatus_Type()
)
dPrefixListRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListRuleRowStatus.setStatus("current")
_DPrefixListDescTable_Object = MibTable
dPrefixListDescTable = _DPrefixListDescTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8)
)
if mibBuilder.loadTexts:
    dPrefixListDescTable.setStatus("current")
_DPrefixListDescEntry_Object = MibTableRow
dPrefixListDescEntry = _DPrefixListDescEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1)
)
dPrefixListDescEntry.setIndexNames(
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"),
    (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"),
)
if mibBuilder.loadTexts:
    dPrefixListDescEntry.setStatus("current")
_DPrefixListDescContent_Type = DisplayString
_DPrefixListDescContent_Object = MibTableColumn
dPrefixListDescContent = _DPrefixListDescContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1, 1),
    _DPrefixListDescContent_Type()
)
dPrefixListDescContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListDescContent.setStatus("current")
_DPrefixListDescRowStatus_Type = RowStatus
_DPrefixListDescRowStatus_Object = MibTableColumn
dPrefixListDescRowStatus = _DPrefixListDescRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1, 99),
    _DPrefixListDescRowStatus_Type()
)
dPrefixListDescRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPrefixListDescRowStatus.setStatus("current")
_DIPFilterConform_ObjectIdentity = ObjectIdentity
dIPFilterConform = _DIPFilterConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2)
)
_DIPFilterMIBGroups_ObjectIdentity = ObjectIdentity
dIPFilterMIBGroups = _DIPFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1)
)
_DIPFilterMIBCompliances_ObjectIdentity = ObjectIdentity
dIPFilterMIBCompliances = _DIPFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 2)
)

# Managed Objects groups

dRouteMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 1)
)
dRouteMapGroup.setObjects(
    ("DLINKSW-IP-FILTER-MIB", "dRouteMapRowStatus")
)
if mibBuilder.loadTexts:
    dRouteMapGroup.setStatus("current")

dRouteMapSeqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 2)
)
dRouteMapSeqGroup.setObjects(
      *(("DLINKSW-IP-FILTER-MIB", "dRouteMapSeqMatchAction"),
        ("DLINKSW-IP-FILTER-MIB", "dRouteMapSeqRowStatus"))
)
if mibBuilder.loadTexts:
    dRouteMapSeqGroup.setStatus("current")

dRouteMapClauseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 3)
)
dRouteMapClauseGroup.setObjects(
      *(("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseAddOption"),
        ("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseElementValue"),
        ("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseRowStatus"))
)
if mibBuilder.loadTexts:
    dRouteMapClauseGroup.setStatus("current")

dAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 4)
)
dAccessListGroup.setObjects(
    ("DLINKSW-IP-FILTER-MIB", "dAccessListRowStatus")
)
if mibBuilder.loadTexts:
    dAccessListGroup.setStatus("current")

dAccessListRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 5)
)
dAccessListRuleGroup.setObjects(
    ("DLINKSW-IP-FILTER-MIB", "dAccessListRuleRowStatus")
)
if mibBuilder.loadTexts:
    dAccessListRuleGroup.setStatus("current")

dPrefixListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 6)
)
dPrefixListGroup.setObjects(
    ("DLINKSW-IP-FILTER-MIB", "dPrefixListRowStatus")
)
if mibBuilder.loadTexts:
    dPrefixListGroup.setStatus("current")

dPrefixListRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 7)
)
dPrefixListRuleGroup.setObjects(
      *(("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleAction"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleNetAddr"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRulePrefixLen"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleGeValue"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleLeValue"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleHitCount"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleRowStatus"))
)
if mibBuilder.loadTexts:
    dPrefixListRuleGroup.setStatus("current")

dPrefixListDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 8)
)
dPrefixListDescGroup.setObjects(
      *(("DLINKSW-IP-FILTER-MIB", "dPrefixListDescContent"),
        ("DLINKSW-IP-FILTER-MIB", "dPrefixListDescRowStatus"))
)
if mibBuilder.loadTexts:
    dPrefixListDescGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIPFilterMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dIPFilterMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IP-FILTER-MIB",
    **{"dlinkSwIPFilterMIB": dlinkSwIPFilterMIB,
       "dIPFilterNotifications": dIPFilterNotifications,
       "dIPFilterObjects": dIPFilterObjects,
       "dRouteMapTable": dRouteMapTable,
       "dRouteMapEntry": dRouteMapEntry,
       "dRouteMapName": dRouteMapName,
       "dRouteMapRowStatus": dRouteMapRowStatus,
       "dRouteMapSeqTable": dRouteMapSeqTable,
       "dRouteMapSeqEntry": dRouteMapSeqEntry,
       "dRouteMapSeqNum": dRouteMapSeqNum,
       "dRouteMapSeqMatchAction": dRouteMapSeqMatchAction,
       "dRouteMapSeqRowStatus": dRouteMapSeqRowStatus,
       "dRouteMapClauseTable": dRouteMapClauseTable,
       "dRouteMapClauseEntry": dRouteMapClauseEntry,
       "dRouteMapClauseTypeId": dRouteMapClauseTypeId,
       "dRouteMapClauseSubId": dRouteMapClauseSubId,
       "dRouteMapClauseAddOption": dRouteMapClauseAddOption,
       "dRouteMapClauseElementValue": dRouteMapClauseElementValue,
       "dRouteMapClauseRowStatus": dRouteMapClauseRowStatus,
       "dAccessListTable": dAccessListTable,
       "dAccessListEntry": dAccessListEntry,
       "dAccessListName": dAccessListName,
       "dAccessListAddrType": dAccessListAddrType,
       "dAccessListRowStatus": dAccessListRowStatus,
       "dAccessListRuleTable": dAccessListRuleTable,
       "dAccessListRuleEntry": dAccessListRuleEntry,
       "dAccessListRuleMatchAction": dAccessListRuleMatchAction,
       "dAccessListRuleNetAddr": dAccessListRuleNetAddr,
       "dAccessListRulePfxLen": dAccessListRulePfxLen,
       "dAccessListRuleRowStatus": dAccessListRuleRowStatus,
       "dPrefixListTable": dPrefixListTable,
       "dPrefixListEntry": dPrefixListEntry,
       "dPrefixListName": dPrefixListName,
       "dPrefixListAddrType": dPrefixListAddrType,
       "dPrefixListRowStatus": dPrefixListRowStatus,
       "dPrefixListRuleTable": dPrefixListRuleTable,
       "dPrefixListRuleEntry": dPrefixListRuleEntry,
       "dPrefixListRuleSeqNum": dPrefixListRuleSeqNum,
       "dPrefixListRuleAction": dPrefixListRuleAction,
       "dPrefixListRuleNetAddr": dPrefixListRuleNetAddr,
       "dPrefixListRulePrefixLen": dPrefixListRulePrefixLen,
       "dPrefixListRuleGeValue": dPrefixListRuleGeValue,
       "dPrefixListRuleLeValue": dPrefixListRuleLeValue,
       "dPrefixListRuleHitCount": dPrefixListRuleHitCount,
       "dPrefixListRuleRowStatus": dPrefixListRuleRowStatus,
       "dPrefixListDescTable": dPrefixListDescTable,
       "dPrefixListDescEntry": dPrefixListDescEntry,
       "dPrefixListDescContent": dPrefixListDescContent,
       "dPrefixListDescRowStatus": dPrefixListDescRowStatus,
       "dIPFilterConform": dIPFilterConform,
       "dIPFilterMIBGroups": dIPFilterMIBGroups,
       "dRouteMapGroup": dRouteMapGroup,
       "dRouteMapSeqGroup": dRouteMapSeqGroup,
       "dRouteMapClauseGroup": dRouteMapClauseGroup,
       "dAccessListGroup": dAccessListGroup,
       "dAccessListRuleGroup": dAccessListRuleGroup,
       "dPrefixListGroup": dPrefixListGroup,
       "dPrefixListRuleGroup": dPrefixListRuleGroup,
       "dPrefixListDescGroup": dPrefixListDescGroup,
       "dIPFilterMIBCompliances": dIPFilterMIBCompliances,
       "dIPFilterMIBFullCompliance": dIPFilterMIBFullCompliance}
)
