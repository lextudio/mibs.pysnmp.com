# SNMP MIB module (TIMETRA-ROUTE-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-ROUTE-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:09 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(IpAddressPrefixLength,
 TFCNameOrEmpty,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPriority,
 TPriorityOrUndefined,
 TmnxBGPFamilyType,
 TmnxBgpAutonomousSystem,
 TmnxBgpLocalPreference,
 TmnxBgpPreference,
 TmnxEnabledDisabled,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TFCNameOrEmpty",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPriority",
    "TPriorityOrUndefined",
    "TmnxBGPFamilyType",
    "TmnxBgpAutonomousSystem",
    "TmnxBgpLocalPreference",
    "TmnxBgpPreference",
    "TmnxEnabledDisabled",
    "TmnxServId")


# MODULE-IDENTITY

timetraRoutePolicyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 17)
)
timetraRoutePolicyMIBModule.setRevisions(
        ("1912-02-28 12:00",
         "1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-01-01 00:00",
         "1906-03-23 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "2003-01-20 00:00",
         "2001-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TASPathName(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TCommunityName(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TCommunityMember(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 72),
    )



class TCommunityExpression(DisplayString, TextualConvention):
    status = "current"


class TDampingName(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TPrefixListName(TNamedItemOrEmpty, TextualConvention):
    status = "current"


class TPolicyStatementName(TNamedItem, TextualConvention):
    status = "current"


class TRegularExpression(DisplayString, TextualConvention):
    status = "current"


class TPolicyStatementEntryID(Unsigned32, TextualConvention):
    status = "current"


class TRoutePolicyProtocol(Integer32, TextualConvention):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 8),
          ("bgp", 4),
          ("bgpVpn", 9),
          ("direct", 2),
          ("igmp", 10),
          ("ipsec", 23),
          ("isis", 5),
          ("ldp", 13),
          ("managed", 16),
          ("mld", 15),
          ("mobileHost", 19),
          ("msdp", 17),
          ("nat", 21),
          ("none", 1),
          ("ospf", 6),
          ("ospf3", 12),
          ("periodic", 22),
          ("pim", 11),
          ("rip", 7),
          ("static", 3),
          ("subscriber", 14),
          ("tms", 20),
          ("vpnLeak", 18))
    )



class TOspfRouteType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )



class TIsisLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )



class TPolicyEntryAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("continue", 3),
          ("nextPolicy", 4),
          ("none", 0),
          ("reject", 2))
    )



class TPolicyEntryEdit(Integer32, TextualConvention):
    status = "current"
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
        *(("add", 2),
          ("none", 1),
          ("remove", 3),
          ("replace", 4))
    )



class TPolicyEntryCriteriaOrigin(Integer32, TextualConvention):
    status = "current"
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
        *(("aaa", 6),
          ("any", 5),
          ("dhcp", 7),
          ("egp", 3),
          ("igp", 2),
          ("incomplete", 4),
          ("ludb", 8),
          ("none", 1))
    )



class TPolicyActionTag(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TPolicyEntryCriteriaState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipsecMaster", 6),
          ("ipsecMasterNoPeer", 7),
          ("ipsecNonMaster", 8),
          ("none", 1),
          ("srrpMaster", 2),
          ("srrpNonMaster", 3))
    )



class TPolicyActionMetricSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igpCost", 1),
          ("metricVal", 2))
    )



class TPolicyEntryAigpMetricEdit(Integer32, TextualConvention):
    status = "current"
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
        *(("add", 2),
          ("none", 1),
          ("replace", 3),
          ("useIgp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxRoutePolicyConformance_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyConformance = _TmnxRoutePolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17)
)
_TmnxRoutePolicyCompliances_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyCompliances = _TmnxRoutePolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1)
)
_TmnxRoutePolicyGroups_ObjectIdentity = ObjectIdentity
tmnxRoutePolicyGroups = _TmnxRoutePolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2)
)
_TRoutePolicyObjects_ObjectIdentity = ObjectIdentity
tRoutePolicyObjects = _TRoutePolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17)
)
_TRPOperObjects_ObjectIdentity = ObjectIdentity
tRPOperObjects = _TRPOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1)
)
_TRPOperValueObjects_ObjectIdentity = ObjectIdentity
tRPOperValueObjects = _TRPOperValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1)
)
_TRPOperASPathTableLastChanged_Type = TimeStamp
_TRPOperASPathTableLastChanged_Object = MibScalar
tRPOperASPathTableLastChanged = _TRPOperASPathTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 1),
    _TRPOperASPathTableLastChanged_Type()
)
tRPOperASPathTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathTableLastChanged.setStatus("obsolete")
_TRPOperASPathTable_Object = MibTable
tRPOperASPathTable = _TRPOperASPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tRPOperASPathTable.setStatus("current")
_TRPOperASPathEntry_Object = MibTableRow
tRPOperASPathEntry = _TRPOperASPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1)
)
tRPOperASPathEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathName"),
)
if mibBuilder.loadTexts:
    tRPOperASPathEntry.setStatus("current")


class _TRPOperASPathName_Type(TASPathName):
    """Custom type tRPOperASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperASPathName_Type.__name__ = "TASPathName"
_TRPOperASPathName_Object = MibTableColumn
tRPOperASPathName = _TRPOperASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 1),
    _TRPOperASPathName_Type()
)
tRPOperASPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathName.setStatus("current")
_TRPOperASPathRowStatus_Type = RowStatus
_TRPOperASPathRowStatus_Object = MibTableColumn
tRPOperASPathRowStatus = _TRPOperASPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 2),
    _TRPOperASPathRowStatus_Type()
)
tRPOperASPathRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathRowStatus.setStatus("current")
_TRPOperASPathRegEx_Type = TRegularExpression
_TRPOperASPathRegEx_Object = MibTableColumn
tRPOperASPathRegEx = _TRPOperASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 3),
    _TRPOperASPathRegEx_Type()
)
tRPOperASPathRegEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathRegEx.setStatus("current")
_TRPOperASPathEntryLastChanged_Type = TimeStamp
_TRPOperASPathEntryLastChanged_Object = MibTableColumn
tRPOperASPathEntryLastChanged = _TRPOperASPathEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 2, 1, 4),
    _TRPOperASPathEntryLastChanged_Type()
)
tRPOperASPathEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathEntryLastChanged.setStatus("obsolete")
_TRPOperCommunityTableLastChanged_Type = TimeStamp
_TRPOperCommunityTableLastChanged_Object = MibScalar
tRPOperCommunityTableLastChanged = _TRPOperCommunityTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 3),
    _TRPOperCommunityTableLastChanged_Type()
)
tRPOperCommunityTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityTableLastChanged.setStatus("obsolete")
_TRPOperCommunityTable_Object = MibTable
tRPOperCommunityTable = _TRPOperCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tRPOperCommunityTable.setStatus("current")
_TRPOperCommunityEntry_Object = MibTableRow
tRPOperCommunityEntry = _TRPOperCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1)
)
tRPOperCommunityEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityMember"),
)
if mibBuilder.loadTexts:
    tRPOperCommunityEntry.setStatus("current")


class _TRPOperCommunityName_Type(TCommunityName):
    """Custom type tRPOperCommunityName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperCommunityName_Type.__name__ = "TCommunityName"
_TRPOperCommunityName_Object = MibTableColumn
tRPOperCommunityName = _TRPOperCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 1),
    _TRPOperCommunityName_Type()
)
tRPOperCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityName.setStatus("current")
_TRPOperCommunityMember_Type = TCommunityMember
_TRPOperCommunityMember_Object = MibTableColumn
tRPOperCommunityMember = _TRPOperCommunityMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 2),
    _TRPOperCommunityMember_Type()
)
tRPOperCommunityMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityMember.setStatus("current")
_TRPOperCommunityRowStatus_Type = RowStatus
_TRPOperCommunityRowStatus_Object = MibTableColumn
tRPOperCommunityRowStatus = _TRPOperCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 3),
    _TRPOperCommunityRowStatus_Type()
)
tRPOperCommunityRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityRowStatus.setStatus("current")
_TRPOperCommunityEntryLastChanged_Type = TimeStamp
_TRPOperCommunityEntryLastChanged_Object = MibTableColumn
tRPOperCommunityEntryLastChanged = _TRPOperCommunityEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 4, 1, 4),
    _TRPOperCommunityEntryLastChanged_Type()
)
tRPOperCommunityEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityEntryLastChanged.setStatus("obsolete")
_TRPOperDampingTableLastChanged_Type = TimeStamp
_TRPOperDampingTableLastChanged_Object = MibScalar
tRPOperDampingTableLastChanged = _TRPOperDampingTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 5),
    _TRPOperDampingTableLastChanged_Type()
)
tRPOperDampingTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingTableLastChanged.setStatus("obsolete")
_TRPOperDampingTable_Object = MibTable
tRPOperDampingTable = _TRPOperDampingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tRPOperDampingTable.setStatus("current")
_TRPOperDampingEntry_Object = MibTableRow
tRPOperDampingEntry = _TRPOperDampingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1)
)
tRPOperDampingEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingName"),
)
if mibBuilder.loadTexts:
    tRPOperDampingEntry.setStatus("current")


class _TRPOperDampingName_Type(TDampingName):
    """Custom type tRPOperDampingName based on TDampingName"""
    subtypeSpec = TDampingName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperDampingName_Type.__name__ = "TDampingName"
_TRPOperDampingName_Object = MibTableColumn
tRPOperDampingName = _TRPOperDampingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 1),
    _TRPOperDampingName_Type()
)
tRPOperDampingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperDampingName.setStatus("current")
_TRPOperDampingRowStatus_Type = RowStatus
_TRPOperDampingRowStatus_Object = MibTableColumn
tRPOperDampingRowStatus = _TRPOperDampingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 2),
    _TRPOperDampingRowStatus_Type()
)
tRPOperDampingRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingRowStatus.setStatus("current")


class _TRPOperDampingHalfLife_Type(Unsigned32):
    """Custom type tRPOperDampingHalfLife based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_TRPOperDampingHalfLife_Type.__name__ = "Unsigned32"
_TRPOperDampingHalfLife_Object = MibTableColumn
tRPOperDampingHalfLife = _TRPOperDampingHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 3),
    _TRPOperDampingHalfLife_Type()
)
tRPOperDampingHalfLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingHalfLife.setStatus("current")
if mibBuilder.loadTexts:
    tRPOperDampingHalfLife.setUnits("minutes")


class _TRPOperDampingMaxSuppress_Type(Unsigned32):
    """Custom type tRPOperDampingMaxSuppress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TRPOperDampingMaxSuppress_Type.__name__ = "Unsigned32"
_TRPOperDampingMaxSuppress_Object = MibTableColumn
tRPOperDampingMaxSuppress = _TRPOperDampingMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 4),
    _TRPOperDampingMaxSuppress_Type()
)
tRPOperDampingMaxSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingMaxSuppress.setStatus("current")
if mibBuilder.loadTexts:
    tRPOperDampingMaxSuppress.setUnits("minutes")


class _TRPOperDampingReuse_Type(Unsigned32):
    """Custom type tRPOperDampingReuse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPOperDampingReuse_Type.__name__ = "Unsigned32"
_TRPOperDampingReuse_Object = MibTableColumn
tRPOperDampingReuse = _TRPOperDampingReuse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 5),
    _TRPOperDampingReuse_Type()
)
tRPOperDampingReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingReuse.setStatus("current")


class _TRPOperDampingSuppress_Type(Unsigned32):
    """Custom type tRPOperDampingSuppress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPOperDampingSuppress_Type.__name__ = "Unsigned32"
_TRPOperDampingSuppress_Object = MibTableColumn
tRPOperDampingSuppress = _TRPOperDampingSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 6),
    _TRPOperDampingSuppress_Type()
)
tRPOperDampingSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingSuppress.setStatus("current")
_TRPOperDampingEntryLastChanged_Type = TimeStamp
_TRPOperDampingEntryLastChanged_Object = MibTableColumn
tRPOperDampingEntryLastChanged = _TRPOperDampingEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 6, 1, 7),
    _TRPOperDampingEntryLastChanged_Type()
)
tRPOperDampingEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperDampingEntryLastChanged.setStatus("obsolete")
_TRPOperPrefixListTableLastChanged_Type = TimeStamp
_TRPOperPrefixListTableLastChanged_Object = MibScalar
tRPOperPrefixListTableLastChanged = _TRPOperPrefixListTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 7),
    _TRPOperPrefixListTableLastChanged_Type()
)
tRPOperPrefixListTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListTableLastChanged.setStatus("obsolete")
_TRPOperPrefixListTable_Object = MibTable
tRPOperPrefixListTable = _TRPOperPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tRPOperPrefixListTable.setStatus("current")
_TRPOperPrefixListEntry_Object = MibTableRow
tRPOperPrefixListEntry = _TRPOperPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1)
)
tRPOperPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListIpPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListMask"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPOperPrefixListEntry.setStatus("current")


class _TRPOperPrefixListName_Type(TPrefixListName):
    """Custom type tRPOperPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperPrefixListName_Type.__name__ = "TPrefixListName"
_TRPOperPrefixListName_Object = MibTableColumn
tRPOperPrefixListName = _TRPOperPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 1),
    _TRPOperPrefixListName_Type()
)
tRPOperPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListName.setStatus("current")
_TRPOperPrefixListIpPrefix_Type = IpAddress
_TRPOperPrefixListIpPrefix_Object = MibTableColumn
tRPOperPrefixListIpPrefix = _TRPOperPrefixListIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 2),
    _TRPOperPrefixListIpPrefix_Type()
)
tRPOperPrefixListIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListIpPrefix.setStatus("current")
_TRPOperPrefixListMask_Type = IpAddressPrefixLength
_TRPOperPrefixListMask_Object = MibTableColumn
tRPOperPrefixListMask = _TRPOperPrefixListMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 3),
    _TRPOperPrefixListMask_Type()
)
tRPOperPrefixListMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListMask.setStatus("current")
_TRPOperPrefixListRowStatus_Type = RowStatus
_TRPOperPrefixListRowStatus_Object = MibTableColumn
tRPOperPrefixListRowStatus = _TRPOperPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 4),
    _TRPOperPrefixListRowStatus_Type()
)
tRPOperPrefixListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListRowStatus.setStatus("current")


class _TRPOperPrefixListType_Type(Integer32):
    """Custom type tRPOperPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("range", 4),
          ("through", 3))
    )


_TRPOperPrefixListType_Type.__name__ = "Integer32"
_TRPOperPrefixListType_Object = MibTableColumn
tRPOperPrefixListType = _TRPOperPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 5),
    _TRPOperPrefixListType_Type()
)
tRPOperPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPrefixListType.setStatus("current")
_TRPOperPrefixListThroughLength_Type = IpAddressPrefixLength
_TRPOperPrefixListThroughLength_Object = MibTableColumn
tRPOperPrefixListThroughLength = _TRPOperPrefixListThroughLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 6),
    _TRPOperPrefixListThroughLength_Type()
)
tRPOperPrefixListThroughLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListThroughLength.setStatus("current")
_TRPOperPrefixListEntryLastChanged_Type = TimeStamp
_TRPOperPrefixListEntryLastChanged_Object = MibTableColumn
tRPOperPrefixListEntryLastChanged = _TRPOperPrefixListEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 7),
    _TRPOperPrefixListEntryLastChanged_Type()
)
tRPOperPrefixListEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListEntryLastChanged.setStatus("obsolete")
_TRPOperPrefixListBeginLength_Type = IpAddressPrefixLength
_TRPOperPrefixListBeginLength_Object = MibTableColumn
tRPOperPrefixListBeginLength = _TRPOperPrefixListBeginLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 8, 1, 8),
    _TRPOperPrefixListBeginLength_Type()
)
tRPOperPrefixListBeginLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPrefixListBeginLength.setStatus("current")
_TRPOperPolicyStatementTableLastChanged_Type = TimeStamp
_TRPOperPolicyStatementTableLastChanged_Object = MibScalar
tRPOperPolicyStatementTableLastChanged = _TRPOperPolicyStatementTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 9),
    _TRPOperPolicyStatementTableLastChanged_Type()
)
tRPOperPolicyStatementTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementTableLastChanged.setStatus("obsolete")
_TRPOperPolicyStatementTable_Object = MibTable
tRPOperPolicyStatementTable = _TRPOperPolicyStatementTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tRPOperPolicyStatementTable.setStatus("current")
_TRPOperPolicyStatementEntry_Object = MibTableRow
tRPOperPolicyStatementEntry = _TRPOperPolicyStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1)
)
tRPOperPolicyStatementEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPOperPolicyStatementEntry.setStatus("current")
_TRPOperPolicyStatementName_Type = TPolicyStatementName
_TRPOperPolicyStatementName_Object = MibTableColumn
tRPOperPolicyStatementName = _TRPOperPolicyStatementName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 1),
    _TRPOperPolicyStatementName_Type()
)
tRPOperPolicyStatementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementName.setStatus("current")
_TRPOperPolicyStatementRowStatus_Type = RowStatus
_TRPOperPolicyStatementRowStatus_Object = MibTableColumn
tRPOperPolicyStatementRowStatus = _TRPOperPolicyStatementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 2),
    _TRPOperPolicyStatementRowStatus_Type()
)
tRPOperPolicyStatementRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementRowStatus.setStatus("current")
_TRPOperPolicyStatementDescription_Type = TItemDescription
_TRPOperPolicyStatementDescription_Object = MibTableColumn
tRPOperPolicyStatementDescription = _TRPOperPolicyStatementDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 3),
    _TRPOperPolicyStatementDescription_Type()
)
tRPOperPolicyStatementDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementDescription.setStatus("current")
_TRPOperPolicyStatementDefaultAction_Type = TPolicyEntryAction
_TRPOperPolicyStatementDefaultAction_Object = MibTableColumn
tRPOperPolicyStatementDefaultAction = _TRPOperPolicyStatementDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 4),
    _TRPOperPolicyStatementDefaultAction_Type()
)
tRPOperPolicyStatementDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementDefaultAction.setStatus("current")
_TRPOperPolicyStatementEntryLastChanged_Type = TimeStamp
_TRPOperPolicyStatementEntryLastChanged_Object = MibTableColumn
tRPOperPolicyStatementEntryLastChanged = _TRPOperPolicyStatementEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 10, 1, 5),
    _TRPOperPolicyStatementEntryLastChanged_Type()
)
tRPOperPolicyStatementEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPolicyStatementEntryLastChanged.setStatus("obsolete")
_TRPOperPSDefaultActionParamsTableLastChanged_Type = TimeStamp
_TRPOperPSDefaultActionParamsTableLastChanged_Object = MibScalar
tRPOperPSDefaultActionParamsTableLastChanged = _TRPOperPSDefaultActionParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 11),
    _TRPOperPSDefaultActionParamsTableLastChanged_Type()
)
tRPOperPSDefaultActionParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSDefaultActionParamsTable_Object = MibTable
tRPOperPSDefaultActionParamsTable = _TRPOperPSDefaultActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsTable.setStatus("current")
_TRPOperPSDefaultActionParamsEntry_Object = MibTableRow
tRPOperPSDefaultActionParamsEntry = _TRPOperPSDefaultActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1)
)
tRPOperPSDefaultActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsEntry.setStatus("current")
_TRPOperPSDefaultActionASPath_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionASPath_Object = MibTableColumn
tRPOperPSDefaultActionASPath = _TRPOperPSDefaultActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 1),
    _TRPOperPSDefaultActionASPath_Type()
)
tRPOperPSDefaultActionASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPath.setStatus("current")
_TRPOperPSDefaultActionASPathName_Type = TASPathName
_TRPOperPSDefaultActionASPathName_Object = MibTableColumn
tRPOperPSDefaultActionASPathName = _TRPOperPSDefaultActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 2),
    _TRPOperPSDefaultActionASPathName_Type()
)
tRPOperPSDefaultActionASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathName.setStatus("current")
_TRPOperPSDefaultActionASPathPrependAS_Type = TmnxBgpAutonomousSystem
_TRPOperPSDefaultActionASPathPrependAS_Object = MibTableColumn
tRPOperPSDefaultActionASPathPrependAS = _TRPOperPSDefaultActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 3),
    _TRPOperPSDefaultActionASPathPrependAS_Type()
)
tRPOperPSDefaultActionASPathPrependAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPrependAS.setStatus("obsolete")


class _TRPOperPSDefaultActionASPathPrependCount_Type(Integer32):
    """Custom type tRPOperPSDefaultActionASPathPrependCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPOperPSDefaultActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPOperPSDefaultActionASPathPrependCount_Object = MibTableColumn
tRPOperPSDefaultActionASPathPrependCount = _TRPOperPSDefaultActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 4),
    _TRPOperPSDefaultActionASPathPrependCount_Type()
)
tRPOperPSDefaultActionASPathPrependCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPrependCount.setStatus("current")
_TRPOperPSDefaultActionCommunity1_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionCommunity1_Object = MibTableColumn
tRPOperPSDefaultActionCommunity1 = _TRPOperPSDefaultActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 5),
    _TRPOperPSDefaultActionCommunity1_Type()
)
tRPOperPSDefaultActionCommunity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunity1.setStatus("current")
_TRPOperPSDefaultActionCommunityName1_Type = TCommunityName
_TRPOperPSDefaultActionCommunityName1_Object = MibTableColumn
tRPOperPSDefaultActionCommunityName1 = _TRPOperPSDefaultActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 6),
    _TRPOperPSDefaultActionCommunityName1_Type()
)
tRPOperPSDefaultActionCommunityName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunityName1.setStatus("current")
_TRPOperPSDefaultActionCommunity2_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionCommunity2_Object = MibTableColumn
tRPOperPSDefaultActionCommunity2 = _TRPOperPSDefaultActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 7),
    _TRPOperPSDefaultActionCommunity2_Type()
)
tRPOperPSDefaultActionCommunity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunity2.setStatus("current")
_TRPOperPSDefaultActionCommunityName2_Type = TCommunityName
_TRPOperPSDefaultActionCommunityName2_Object = MibTableColumn
tRPOperPSDefaultActionCommunityName2 = _TRPOperPSDefaultActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 8),
    _TRPOperPSDefaultActionCommunityName2_Type()
)
tRPOperPSDefaultActionCommunityName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionCommunityName2.setStatus("current")
_TRPOperPSDefaultActionOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSDefaultActionOrigin_Object = MibTableColumn
tRPOperPSDefaultActionOrigin = _TRPOperPSDefaultActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 9),
    _TRPOperPSDefaultActionOrigin_Type()
)
tRPOperPSDefaultActionOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionOrigin.setStatus("current")
_TRPOperPSDefaultActionLocalPreferenceSet_Type = TruthValue
_TRPOperPSDefaultActionLocalPreferenceSet_Object = MibTableColumn
tRPOperPSDefaultActionLocalPreferenceSet = _TRPOperPSDefaultActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 10),
    _TRPOperPSDefaultActionLocalPreferenceSet_Type()
)
tRPOperPSDefaultActionLocalPreferenceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionLocalPreferenceSet.setStatus("current")
_TRPOperPSDefaultActionLocalPreference_Type = TmnxBgpLocalPreference
_TRPOperPSDefaultActionLocalPreference_Object = MibTableColumn
tRPOperPSDefaultActionLocalPreference = _TRPOperPSDefaultActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 11),
    _TRPOperPSDefaultActionLocalPreference_Type()
)
tRPOperPSDefaultActionLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionLocalPreference.setStatus("current")
_TRPOperPSDefaultActionMetric_Type = TPolicyEntryEdit
_TRPOperPSDefaultActionMetric_Object = MibTableColumn
tRPOperPSDefaultActionMetric = _TRPOperPSDefaultActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 12),
    _TRPOperPSDefaultActionMetric_Type()
)
tRPOperPSDefaultActionMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionMetric.setStatus("current")
_TRPOperPSDefaultActionMetricValue_Type = Unsigned32
_TRPOperPSDefaultActionMetricValue_Object = MibTableColumn
tRPOperPSDefaultActionMetricValue = _TRPOperPSDefaultActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 13),
    _TRPOperPSDefaultActionMetricValue_Type()
)
tRPOperPSDefaultActionMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionMetricValue.setStatus("current")
_TRPOperPSDefaultActionPreference_Type = TmnxBgpPreference
_TRPOperPSDefaultActionPreference_Object = MibTableColumn
tRPOperPSDefaultActionPreference = _TRPOperPSDefaultActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 15),
    _TRPOperPSDefaultActionPreference_Type()
)
tRPOperPSDefaultActionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionPreference.setStatus("current")
_TRPOperPSDefaultActionDamping_Type = TDampingName
_TRPOperPSDefaultActionDamping_Object = MibTableColumn
tRPOperPSDefaultActionDamping = _TRPOperPSDefaultActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 16),
    _TRPOperPSDefaultActionDamping_Type()
)
tRPOperPSDefaultActionDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionDamping.setStatus("current")
_TRPOperPSDefaultActionNextHopSelf_Type = TruthValue
_TRPOperPSDefaultActionNextHopSelf_Object = MibTableColumn
tRPOperPSDefaultActionNextHopSelf = _TRPOperPSDefaultActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 17),
    _TRPOperPSDefaultActionNextHopSelf_Type()
)
tRPOperPSDefaultActionNextHopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionNextHopSelf.setStatus("current")
_TRPOperPSDefaultActionNextHop_Type = IpAddress
_TRPOperPSDefaultActionNextHop_Object = MibTableColumn
tRPOperPSDefaultActionNextHop = _TRPOperPSDefaultActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 18),
    _TRPOperPSDefaultActionNextHop_Type()
)
tRPOperPSDefaultActionNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionNextHop.setStatus("current")
_TRPOperPSDefaultActionTag_Type = TPolicyActionTag
_TRPOperPSDefaultActionTag_Object = MibTableColumn
tRPOperPSDefaultActionTag = _TRPOperPSDefaultActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 19),
    _TRPOperPSDefaultActionTag_Type()
)
tRPOperPSDefaultActionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionTag.setStatus("current")
_TRPOperPSDefaultActionOspfType_Type = TOspfRouteType
_TRPOperPSDefaultActionOspfType_Object = MibTableColumn
tRPOperPSDefaultActionOspfType = _TRPOperPSDefaultActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 20),
    _TRPOperPSDefaultActionOspfType_Type()
)
tRPOperPSDefaultActionOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionOspfType.setStatus("current")
_TRPOperPSDefaultActionParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSDefaultActionParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSDefaultActionParamsEntryLastChanged = _TRPOperPSDefaultActionParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 21),
    _TRPOperPSDefaultActionParamsEntryLastChanged_Type()
)
tRPOperPSDefaultActionParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSDefActInetNextHopType_Type = InetAddressType
_TRPOperPSDefActInetNextHopType_Object = MibTableColumn
tRPOperPSDefActInetNextHopType = _TRPOperPSDefActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 22),
    _TRPOperPSDefActInetNextHopType_Type()
)
tRPOperPSDefActInetNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActInetNextHopType.setStatus("current")
_TRPOperPSDefActInetNextHop_Type = InetAddress
_TRPOperPSDefActInetNextHop_Object = MibTableColumn
tRPOperPSDefActInetNextHop = _TRPOperPSDefActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 23),
    _TRPOperPSDefActInetNextHop_Type()
)
tRPOperPSDefActInetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActInetNextHop.setStatus("current")
_TRPOperPSDefaultActionASPathPend_Type = InetAutonomousSystemNumber
_TRPOperPSDefaultActionASPathPend_Object = MibTableColumn
tRPOperPSDefaultActionASPathPend = _TRPOperPSDefaultActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 24),
    _TRPOperPSDefaultActionASPathPend_Type()
)
tRPOperPSDefaultActionASPathPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefaultActionASPathPend.setStatus("current")
_TRPOperPSDefActMcRedirSvcId_Type = TmnxServId
_TRPOperPSDefActMcRedirSvcId_Object = MibTableColumn
tRPOperPSDefActMcRedirSvcId = _TRPOperPSDefActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 30),
    _TRPOperPSDefActMcRedirSvcId_Type()
)
tRPOperPSDefActMcRedirSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActMcRedirSvcId.setStatus("current")
_TRPOperPSDefActMcRedirIfIndex_Type = InterfaceIndexOrZero
_TRPOperPSDefActMcRedirIfIndex_Object = MibTableColumn
tRPOperPSDefActMcRedirIfIndex = _TRPOperPSDefActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 31),
    _TRPOperPSDefActMcRedirIfIndex_Type()
)
tRPOperPSDefActMcRedirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActMcRedirIfIndex.setStatus("current")
_TRPOperPSDefActionMetricSource_Type = TPolicyActionMetricSource
_TRPOperPSDefActionMetricSource_Object = MibTableColumn
tRPOperPSDefActionMetricSource = _TRPOperPSDefActionMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 32),
    _TRPOperPSDefActionMetricSource_Type()
)
tRPOperPSDefActionMetricSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionMetricSource.setStatus("current")
_TRPOperPSDefActionAigpMetric_Type = TPolicyEntryAigpMetricEdit
_TRPOperPSDefActionAigpMetric_Object = MibTableColumn
tRPOperPSDefActionAigpMetric = _TRPOperPSDefActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 33),
    _TRPOperPSDefActionAigpMetric_Type()
)
tRPOperPSDefActionAigpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActionAigpMetric.setStatus("current")
_TRPOperPSDefActnAigpMetricVal_Type = Unsigned32
_TRPOperPSDefActnAigpMetricVal_Object = MibTableColumn
tRPOperPSDefActnAigpMetricVal = _TRPOperPSDefActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 12, 1, 34),
    _TRPOperPSDefActnAigpMetricVal_Type()
)
tRPOperPSDefActnAigpMetricVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSDefActnAigpMetricVal.setStatus("current")
_TRPOperPSParamsTableLastChanged_Type = TimeStamp
_TRPOperPSParamsTableLastChanged_Object = MibScalar
tRPOperPSParamsTableLastChanged = _TRPOperPSParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 13),
    _TRPOperPSParamsTableLastChanged_Type()
)
tRPOperPSParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSParamsTable_Object = MibTable
tRPOperPSParamsTable = _TRPOperPSParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tRPOperPSParamsTable.setStatus("current")
_TRPOperPSParamsEntry_Object = MibTableRow
tRPOperPSParamsEntry = _TRPOperPSParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1)
)
tRPOperPSParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSParamsEntry.setStatus("current")
_TRPOperPSNameEntryIndex_Type = TPolicyStatementEntryID
_TRPOperPSNameEntryIndex_Object = MibTableColumn
tRPOperPSNameEntryIndex = _TRPOperPSNameEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 1),
    _TRPOperPSNameEntryIndex_Type()
)
tRPOperPSNameEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSNameEntryIndex.setStatus("current")
_TRPOperPSParamsRowStatus_Type = RowStatus
_TRPOperPSParamsRowStatus_Object = MibTableColumn
tRPOperPSParamsRowStatus = _TRPOperPSParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 2),
    _TRPOperPSParamsRowStatus_Type()
)
tRPOperPSParamsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsRowStatus.setStatus("current")
_TRPOperPSParamsDescription_Type = TItemDescription
_TRPOperPSParamsDescription_Object = MibTableColumn
tRPOperPSParamsDescription = _TRPOperPSParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 3),
    _TRPOperPSParamsDescription_Type()
)
tRPOperPSParamsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsDescription.setStatus("current")
_TRPOperPSParamsAction_Type = TPolicyEntryAction
_TRPOperPSParamsAction_Object = MibTableColumn
tRPOperPSParamsAction = _TRPOperPSParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 4),
    _TRPOperPSParamsAction_Type()
)
tRPOperPSParamsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsAction.setStatus("current")
_TRPOperPSParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSParamsEntryLastChanged = _TRPOperPSParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 14, 1, 5),
    _TRPOperPSParamsEntryLastChanged_Type()
)
tRPOperPSParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSAcceptActionParamsTableLastChanged_Type = TimeStamp
_TRPOperPSAcceptActionParamsTableLastChanged_Object = MibScalar
tRPOperPSAcceptActionParamsTableLastChanged = _TRPOperPSAcceptActionParamsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 15),
    _TRPOperPSAcceptActionParamsTableLastChanged_Type()
)
tRPOperPSAcceptActionParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsTableLastChanged.setStatus("obsolete")
_TRPOperPSAcceptActionParamsTable_Object = MibTable
tRPOperPSAcceptActionParamsTable = _TRPOperPSAcceptActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16)
)
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsTable.setStatus("current")
_TRPOperPSAcceptActionParamsEntry_Object = MibTableRow
tRPOperPSAcceptActionParamsEntry = _TRPOperPSAcceptActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1)
)
tRPOperPSAcceptActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsEntry.setStatus("current")
_TRPOperPSAcceptActionASPath_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionASPath_Object = MibTableColumn
tRPOperPSAcceptActionASPath = _TRPOperPSAcceptActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 1),
    _TRPOperPSAcceptActionASPath_Type()
)
tRPOperPSAcceptActionASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPath.setStatus("current")
_TRPOperPSAcceptActionASPathName_Type = TASPathName
_TRPOperPSAcceptActionASPathName_Object = MibTableColumn
tRPOperPSAcceptActionASPathName = _TRPOperPSAcceptActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 2),
    _TRPOperPSAcceptActionASPathName_Type()
)
tRPOperPSAcceptActionASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathName.setStatus("current")
_TRPOperPSAcceptActionASPathPrependAS_Type = TmnxBgpAutonomousSystem
_TRPOperPSAcceptActionASPathPrependAS_Object = MibTableColumn
tRPOperPSAcceptActionASPathPrependAS = _TRPOperPSAcceptActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 3),
    _TRPOperPSAcceptActionASPathPrependAS_Type()
)
tRPOperPSAcceptActionASPathPrependAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPrependAS.setStatus("obsolete")


class _TRPOperPSAcceptActionASPathPrependCount_Type(Integer32):
    """Custom type tRPOperPSAcceptActionASPathPrependCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPOperPSAcceptActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPOperPSAcceptActionASPathPrependCount_Object = MibTableColumn
tRPOperPSAcceptActionASPathPrependCount = _TRPOperPSAcceptActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 4),
    _TRPOperPSAcceptActionASPathPrependCount_Type()
)
tRPOperPSAcceptActionASPathPrependCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPrependCount.setStatus("current")
_TRPOperPSAcceptActionCommunity1_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionCommunity1_Object = MibTableColumn
tRPOperPSAcceptActionCommunity1 = _TRPOperPSAcceptActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 5),
    _TRPOperPSAcceptActionCommunity1_Type()
)
tRPOperPSAcceptActionCommunity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunity1.setStatus("current")
_TRPOperPSAcceptActionCommunityName1_Type = TCommunityName
_TRPOperPSAcceptActionCommunityName1_Object = MibTableColumn
tRPOperPSAcceptActionCommunityName1 = _TRPOperPSAcceptActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 6),
    _TRPOperPSAcceptActionCommunityName1_Type()
)
tRPOperPSAcceptActionCommunityName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunityName1.setStatus("current")
_TRPOperPSAcceptActionCommunity2_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionCommunity2_Object = MibTableColumn
tRPOperPSAcceptActionCommunity2 = _TRPOperPSAcceptActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 7),
    _TRPOperPSAcceptActionCommunity2_Type()
)
tRPOperPSAcceptActionCommunity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunity2.setStatus("current")
_TRPOperPSAcceptActionCommunityName2_Type = TCommunityName
_TRPOperPSAcceptActionCommunityName2_Object = MibTableColumn
tRPOperPSAcceptActionCommunityName2 = _TRPOperPSAcceptActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 8),
    _TRPOperPSAcceptActionCommunityName2_Type()
)
tRPOperPSAcceptActionCommunityName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionCommunityName2.setStatus("current")
_TRPOperPSAcceptActionOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSAcceptActionOrigin_Object = MibTableColumn
tRPOperPSAcceptActionOrigin = _TRPOperPSAcceptActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 9),
    _TRPOperPSAcceptActionOrigin_Type()
)
tRPOperPSAcceptActionOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionOrigin.setStatus("current")
_TRPOperPSAcceptActionLocalPreferenceSet_Type = TruthValue
_TRPOperPSAcceptActionLocalPreferenceSet_Object = MibTableColumn
tRPOperPSAcceptActionLocalPreferenceSet = _TRPOperPSAcceptActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 10),
    _TRPOperPSAcceptActionLocalPreferenceSet_Type()
)
tRPOperPSAcceptActionLocalPreferenceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionLocalPreferenceSet.setStatus("current")
_TRPOperPSAcceptActionLocalPreference_Type = TmnxBgpLocalPreference
_TRPOperPSAcceptActionLocalPreference_Object = MibTableColumn
tRPOperPSAcceptActionLocalPreference = _TRPOperPSAcceptActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 11),
    _TRPOperPSAcceptActionLocalPreference_Type()
)
tRPOperPSAcceptActionLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionLocalPreference.setStatus("current")
_TRPOperPSAcceptActionMetric_Type = TPolicyEntryEdit
_TRPOperPSAcceptActionMetric_Object = MibTableColumn
tRPOperPSAcceptActionMetric = _TRPOperPSAcceptActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 12),
    _TRPOperPSAcceptActionMetric_Type()
)
tRPOperPSAcceptActionMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionMetric.setStatus("current")
_TRPOperPSAcceptActionMetricValue_Type = Unsigned32
_TRPOperPSAcceptActionMetricValue_Object = MibTableColumn
tRPOperPSAcceptActionMetricValue = _TRPOperPSAcceptActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 13),
    _TRPOperPSAcceptActionMetricValue_Type()
)
tRPOperPSAcceptActionMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionMetricValue.setStatus("current")
_TRPOperPSAcceptActionPreference_Type = TmnxBgpPreference
_TRPOperPSAcceptActionPreference_Object = MibTableColumn
tRPOperPSAcceptActionPreference = _TRPOperPSAcceptActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 15),
    _TRPOperPSAcceptActionPreference_Type()
)
tRPOperPSAcceptActionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionPreference.setStatus("current")
_TRPOperPSAcceptActionDamping_Type = TDampingName
_TRPOperPSAcceptActionDamping_Object = MibTableColumn
tRPOperPSAcceptActionDamping = _TRPOperPSAcceptActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 16),
    _TRPOperPSAcceptActionDamping_Type()
)
tRPOperPSAcceptActionDamping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionDamping.setStatus("current")
_TRPOperPSAcceptActionNextHopSelf_Type = TruthValue
_TRPOperPSAcceptActionNextHopSelf_Object = MibTableColumn
tRPOperPSAcceptActionNextHopSelf = _TRPOperPSAcceptActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 17),
    _TRPOperPSAcceptActionNextHopSelf_Type()
)
tRPOperPSAcceptActionNextHopSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionNextHopSelf.setStatus("current")
_TRPOperPSAcceptActionNextHop_Type = IpAddress
_TRPOperPSAcceptActionNextHop_Object = MibTableColumn
tRPOperPSAcceptActionNextHop = _TRPOperPSAcceptActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 18),
    _TRPOperPSAcceptActionNextHop_Type()
)
tRPOperPSAcceptActionNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionNextHop.setStatus("current")
_TRPOperPSAcceptActionTag_Type = TPolicyActionTag
_TRPOperPSAcceptActionTag_Object = MibTableColumn
tRPOperPSAcceptActionTag = _TRPOperPSAcceptActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 19),
    _TRPOperPSAcceptActionTag_Type()
)
tRPOperPSAcceptActionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionTag.setStatus("current")
_TRPOperPSAcceptActionOspfType_Type = TOspfRouteType
_TRPOperPSAcceptActionOspfType_Object = MibTableColumn
tRPOperPSAcceptActionOspfType = _TRPOperPSAcceptActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 20),
    _TRPOperPSAcceptActionOspfType_Type()
)
tRPOperPSAcceptActionOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionOspfType.setStatus("current")
_TRPOperPSAcceptActionParamsEntryLastChanged_Type = TimeStamp
_TRPOperPSAcceptActionParamsEntryLastChanged_Object = MibTableColumn
tRPOperPSAcceptActionParamsEntryLastChanged = _TRPOperPSAcceptActionParamsEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 21),
    _TRPOperPSAcceptActionParamsEntryLastChanged_Type()
)
tRPOperPSAcceptActionParamsEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionParamsEntryLastChanged.setStatus("obsolete")
_TRPOperPSAcptActInetNextHopType_Type = InetAddressType
_TRPOperPSAcptActInetNextHopType_Object = MibTableColumn
tRPOperPSAcptActInetNextHopType = _TRPOperPSAcptActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 22),
    _TRPOperPSAcptActInetNextHopType_Type()
)
tRPOperPSAcptActInetNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActInetNextHopType.setStatus("current")
_TRPOperPSAcptActInetNextHop_Type = InetAddress
_TRPOperPSAcptActInetNextHop_Object = MibTableColumn
tRPOperPSAcptActInetNextHop = _TRPOperPSAcptActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 23),
    _TRPOperPSAcptActInetNextHop_Type()
)
tRPOperPSAcptActInetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActInetNextHop.setStatus("current")
_TRPOperPSAcceptActionASPathPend_Type = InetAutonomousSystemNumber
_TRPOperPSAcceptActionASPathPend_Object = MibTableColumn
tRPOperPSAcceptActionASPathPend = _TRPOperPSAcceptActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 24),
    _TRPOperPSAcceptActionASPathPend_Type()
)
tRPOperPSAcceptActionASPathPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcceptActionASPathPend.setStatus("current")


class _TRPOperPSAcptActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPOperPSAcptActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPOperPSAcptActMcRedirSvcId_Object = MibTableColumn
tRPOperPSAcptActMcRedirSvcId = _TRPOperPSAcptActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 30),
    _TRPOperPSAcptActMcRedirSvcId_Type()
)
tRPOperPSAcptActMcRedirSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActMcRedirSvcId.setStatus("current")


class _TRPOperPSAcptActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPOperPSAcptActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPOperPSAcptActMcRedirIfIndex_Object = MibTableColumn
tRPOperPSAcptActMcRedirIfIndex = _TRPOperPSAcptActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 31),
    _TRPOperPSAcptActMcRedirIfIndex_Type()
)
tRPOperPSAcptActMcRedirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActMcRedirIfIndex.setStatus("current")


class _TRPOperPSAcptActnMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPOperPSAcptActnMetricSource based on TPolicyActionMetricSource"""


_TRPOperPSAcptActnMetricSource_Object = MibTableColumn
tRPOperPSAcptActnMetricSource = _TRPOperPSAcptActnMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 32),
    _TRPOperPSAcptActnMetricSource_Type()
)
tRPOperPSAcptActnMetricSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnMetricSource.setStatus("current")
_TRPOperPSAcptActionAigpMetric_Type = TPolicyEntryAigpMetricEdit
_TRPOperPSAcptActionAigpMetric_Object = MibTableColumn
tRPOperPSAcptActionAigpMetric = _TRPOperPSAcptActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 33),
    _TRPOperPSAcptActionAigpMetric_Type()
)
tRPOperPSAcptActionAigpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActionAigpMetric.setStatus("current")
_TRPOperPSAcptActnAigpMetricVal_Type = Unsigned32
_TRPOperPSAcptActnAigpMetricVal_Object = MibTableColumn
tRPOperPSAcptActnAigpMetricVal = _TRPOperPSAcptActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 16, 1, 34),
    _TRPOperPSAcptActnAigpMetricVal_Type()
)
tRPOperPSAcptActnAigpMetricVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSAcptActnAigpMetricVal.setStatus("current")
_TRPOperPSToCriteriaTableLastChanged_Type = TimeStamp
_TRPOperPSToCriteriaTableLastChanged_Object = MibScalar
tRPOperPSToCriteriaTableLastChanged = _TRPOperPSToCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 17),
    _TRPOperPSToCriteriaTableLastChanged_Type()
)
tRPOperPSToCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaTableLastChanged.setStatus("obsolete")
_TRPOperPSToCriteriaTable_Object = MibTable
tRPOperPSToCriteriaTable = _TRPOperPSToCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18)
)
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaTable.setStatus("current")
_TRPOperPSToCriteriaEntry_Object = MibTableRow
tRPOperPSToCriteriaEntry = _TRPOperPSToCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1)
)
tRPOperPSToCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaEntry.setStatus("current")
_TRPOperPSToCriteriaIndex_Type = TPolicyStatementEntryID
_TRPOperPSToCriteriaIndex_Object = MibTableColumn
tRPOperPSToCriteriaIndex = _TRPOperPSToCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 1),
    _TRPOperPSToCriteriaIndex_Type()
)
tRPOperPSToCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaIndex.setStatus("current")
_TRPOperPSToCriteriaRowStatus_Type = RowStatus
_TRPOperPSToCriteriaRowStatus_Object = MibTableColumn
tRPOperPSToCriteriaRowStatus = _TRPOperPSToCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 2),
    _TRPOperPSToCriteriaRowStatus_Type()
)
tRPOperPSToCriteriaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaRowStatus.setStatus("current")
_TRPOperPSToCriteriaProtocol_Type = TRoutePolicyProtocol
_TRPOperPSToCriteriaProtocol_Object = MibTableColumn
tRPOperPSToCriteriaProtocol = _TRPOperPSToCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 3),
    _TRPOperPSToCriteriaProtocol_Type()
)
tRPOperPSToCriteriaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaProtocol.setStatus("current")
_TRPOperPSToCriteriaNeighborIpAddr_Type = IpAddress
_TRPOperPSToCriteriaNeighborIpAddr_Object = MibTableColumn
tRPOperPSToCriteriaNeighborIpAddr = _TRPOperPSToCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 4),
    _TRPOperPSToCriteriaNeighborIpAddr_Type()
)
tRPOperPSToCriteriaNeighborIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaNeighborIpAddr.setStatus("current")
_TRPOperPSToCriteriaNeighborPrefixList_Type = TPrefixListName
_TRPOperPSToCriteriaNeighborPrefixList_Object = MibTableColumn
tRPOperPSToCriteriaNeighborPrefixList = _TRPOperPSToCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 5),
    _TRPOperPSToCriteriaNeighborPrefixList_Type()
)
tRPOperPSToCriteriaNeighborPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaNeighborPrefixList.setStatus("current")
_TRPOperPSToCriteriaEntryLastChanged_Type = TimeStamp
_TRPOperPSToCriteriaEntryLastChanged_Object = MibTableColumn
tRPOperPSToCriteriaEntryLastChanged = _TRPOperPSToCriteriaEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 6),
    _TRPOperPSToCriteriaEntryLastChanged_Type()
)
tRPOperPSToCriteriaEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaEntryLastChanged.setStatus("obsolete")
_TRPOperPSToCriteriaIsisLevel_Type = TIsisLevel
_TRPOperPSToCriteriaIsisLevel_Object = MibTableColumn
tRPOperPSToCriteriaIsisLevel = _TRPOperPSToCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 7),
    _TRPOperPSToCriteriaIsisLevel_Type()
)
tRPOperPSToCriteriaIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaIsisLevel.setStatus("current")
_TRPOperPSToCriteriaPrefixList1_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList1_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList1 = _TRPOperPSToCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 8),
    _TRPOperPSToCriteriaPrefixList1_Type()
)
tRPOperPSToCriteriaPrefixList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList1.setStatus("current")
_TRPOperPSToCriteriaPrefixList2_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList2_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList2 = _TRPOperPSToCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 9),
    _TRPOperPSToCriteriaPrefixList2_Type()
)
tRPOperPSToCriteriaPrefixList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList2.setStatus("current")
_TRPOperPSToCriteriaPrefixList3_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList3_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList3 = _TRPOperPSToCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 10),
    _TRPOperPSToCriteriaPrefixList3_Type()
)
tRPOperPSToCriteriaPrefixList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList3.setStatus("current")
_TRPOperPSToCriteriaPrefixList4_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList4_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList4 = _TRPOperPSToCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 11),
    _TRPOperPSToCriteriaPrefixList4_Type()
)
tRPOperPSToCriteriaPrefixList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList4.setStatus("current")
_TRPOperPSToCriteriaPrefixList5_Type = TPrefixListName
_TRPOperPSToCriteriaPrefixList5_Object = MibTableColumn
tRPOperPSToCriteriaPrefixList5 = _TRPOperPSToCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 12),
    _TRPOperPSToCriteriaPrefixList5_Type()
)
tRPOperPSToCriteriaPrefixList5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaPrefixList5.setStatus("current")
_TRPOperPSToCritNbrInetAddrType_Type = InetAddressType
_TRPOperPSToCritNbrInetAddrType_Object = MibTableColumn
tRPOperPSToCritNbrInetAddrType = _TRPOperPSToCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 13),
    _TRPOperPSToCritNbrInetAddrType_Type()
)
tRPOperPSToCritNbrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCritNbrInetAddrType.setStatus("current")
_TRPOperPSToCritNbrInetAddr_Type = InetAddress
_TRPOperPSToCritNbrInetAddr_Object = MibTableColumn
tRPOperPSToCritNbrInetAddr = _TRPOperPSToCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 14),
    _TRPOperPSToCritNbrInetAddr_Type()
)
tRPOperPSToCritNbrInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCritNbrInetAddr.setStatus("current")


class _TRPOperPSToCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPOperPSToCriteriaInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPOperPSToCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPOperPSToCriteriaInstanceId_Object = MibTableColumn
tRPOperPSToCriteriaInstanceId = _TRPOperPSToCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 18, 1, 15),
    _TRPOperPSToCriteriaInstanceId_Type()
)
tRPOperPSToCriteriaInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSToCriteriaInstanceId.setStatus("current")
_TRPOperPSFromCriteriaTableLastChanged_Type = TimeStamp
_TRPOperPSFromCriteriaTableLastChanged_Object = MibScalar
tRPOperPSFromCriteriaTableLastChanged = _TRPOperPSFromCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 19),
    _TRPOperPSFromCriteriaTableLastChanged_Type()
)
tRPOperPSFromCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTableLastChanged.setStatus("obsolete")
_TRPOperPSFromCriteriaTable_Object = MibTable
tRPOperPSFromCriteriaTable = _TRPOperPSFromCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20)
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTable.setStatus("current")
_TRPOperPSFromCriteriaEntry_Object = MibTableRow
tRPOperPSFromCriteriaEntry = _TRPOperPSFromCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1)
)
tRPOperPSFromCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaEntry.setStatus("current")
_TRPOperPSFromCriteriaIndex_Type = TPolicyStatementEntryID
_TRPOperPSFromCriteriaIndex_Object = MibTableColumn
tRPOperPSFromCriteriaIndex = _TRPOperPSFromCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 1),
    _TRPOperPSFromCriteriaIndex_Type()
)
tRPOperPSFromCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIndex.setStatus("current")
_TRPOperPSFromCriteriaRowStatus_Type = RowStatus
_TRPOperPSFromCriteriaRowStatus_Object = MibTableColumn
tRPOperPSFromCriteriaRowStatus = _TRPOperPSFromCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 2),
    _TRPOperPSFromCriteriaRowStatus_Type()
)
tRPOperPSFromCriteriaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaRowStatus.setStatus("current")
_TRPOperPSFromCriteriaProtocol_Type = TRoutePolicyProtocol
_TRPOperPSFromCriteriaProtocol_Object = MibTableColumn
tRPOperPSFromCriteriaProtocol = _TRPOperPSFromCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 3),
    _TRPOperPSFromCriteriaProtocol_Type()
)
tRPOperPSFromCriteriaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaProtocol.setStatus("current")
_TRPOperPSFromCriteriaNeighborIpAddr_Type = IpAddress
_TRPOperPSFromCriteriaNeighborIpAddr_Object = MibTableColumn
tRPOperPSFromCriteriaNeighborIpAddr = _TRPOperPSFromCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 4),
    _TRPOperPSFromCriteriaNeighborIpAddr_Type()
)
tRPOperPSFromCriteriaNeighborIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaNeighborIpAddr.setStatus("current")
_TRPOperPSFromCriteriaNeighborPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaNeighborPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaNeighborPrefixList = _TRPOperPSFromCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 5),
    _TRPOperPSFromCriteriaNeighborPrefixList_Type()
)
tRPOperPSFromCriteriaNeighborPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaNeighborPrefixList.setStatus("current")
_TRPOperPSFromCriteriaPrefixList1_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList1_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList1 = _TRPOperPSFromCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 6),
    _TRPOperPSFromCriteriaPrefixList1_Type()
)
tRPOperPSFromCriteriaPrefixList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList1.setStatus("current")
_TRPOperPSFromCriteriaPrefixList2_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList2_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList2 = _TRPOperPSFromCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 7),
    _TRPOperPSFromCriteriaPrefixList2_Type()
)
tRPOperPSFromCriteriaPrefixList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList2.setStatus("current")
_TRPOperPSFromCriteriaPrefixList3_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList3_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList3 = _TRPOperPSFromCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 8),
    _TRPOperPSFromCriteriaPrefixList3_Type()
)
tRPOperPSFromCriteriaPrefixList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList3.setStatus("current")
_TRPOperPSFromCriteriaPrefixList4_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList4_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList4 = _TRPOperPSFromCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 9),
    _TRPOperPSFromCriteriaPrefixList4_Type()
)
tRPOperPSFromCriteriaPrefixList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList4.setStatus("current")
_TRPOperPSFromCriteriaPrefixList5_Type = TPrefixListName
_TRPOperPSFromCriteriaPrefixList5_Object = MibTableColumn
tRPOperPSFromCriteriaPrefixList5 = _TRPOperPSFromCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 10),
    _TRPOperPSFromCriteriaPrefixList5_Type()
)
tRPOperPSFromCriteriaPrefixList5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaPrefixList5.setStatus("current")
_TRPOperPSFromCriteriaASPath_Type = TASPathName
_TRPOperPSFromCriteriaASPath_Object = MibTableColumn
tRPOperPSFromCriteriaASPath = _TRPOperPSFromCriteriaASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 11),
    _TRPOperPSFromCriteriaASPath_Type()
)
tRPOperPSFromCriteriaASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaASPath.setStatus("current")
_TRPOperPSFromCriteriaCommunity_Type = TCommunityName
_TRPOperPSFromCriteriaCommunity_Object = MibTableColumn
tRPOperPSFromCriteriaCommunity = _TRPOperPSFromCriteriaCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 12),
    _TRPOperPSFromCriteriaCommunity_Type()
)
tRPOperPSFromCriteriaCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaCommunity.setStatus("current")
_TRPOperPSFromCriteriaOrigin_Type = TPolicyEntryCriteriaOrigin
_TRPOperPSFromCriteriaOrigin_Object = MibTableColumn
tRPOperPSFromCriteriaOrigin = _TRPOperPSFromCriteriaOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 13),
    _TRPOperPSFromCriteriaOrigin_Type()
)
tRPOperPSFromCriteriaOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaOrigin.setStatus("current")
_TRPOperPSFromCriteriaOspfRouteType_Type = TOspfRouteType
_TRPOperPSFromCriteriaOspfRouteType_Object = MibTableColumn
tRPOperPSFromCriteriaOspfRouteType = _TRPOperPSFromCriteriaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 14),
    _TRPOperPSFromCriteriaOspfRouteType_Type()
)
tRPOperPSFromCriteriaOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaOspfRouteType.setStatus("current")
_TRPOperPSFromCriteriaEntryLastChanged_Type = TimeStamp
_TRPOperPSFromCriteriaEntryLastChanged_Object = MibTableColumn
tRPOperPSFromCriteriaEntryLastChanged = _TRPOperPSFromCriteriaEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 15),
    _TRPOperPSFromCriteriaEntryLastChanged_Type()
)
tRPOperPSFromCriteriaEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaEntryLastChanged.setStatus("obsolete")
_TRPOperPSFromCriteriaArea_Type = IpAddress
_TRPOperPSFromCriteriaArea_Object = MibTableColumn
tRPOperPSFromCriteriaArea = _TRPOperPSFromCriteriaArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 16),
    _TRPOperPSFromCriteriaArea_Type()
)
tRPOperPSFromCriteriaArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaArea.setStatus("current")
_TRPOperPSFromCriteriaAreaConfigured_Type = TruthValue
_TRPOperPSFromCriteriaAreaConfigured_Object = MibTableColumn
tRPOperPSFromCriteriaAreaConfigured = _TRPOperPSFromCriteriaAreaConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 17),
    _TRPOperPSFromCriteriaAreaConfigured_Type()
)
tRPOperPSFromCriteriaAreaConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaAreaConfigured.setStatus("current")
_TRPOperPSFromCriteriaIsisLevel_Type = TIsisLevel
_TRPOperPSFromCriteriaIsisLevel_Object = MibTableColumn
tRPOperPSFromCriteriaIsisLevel = _TRPOperPSFromCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 18),
    _TRPOperPSFromCriteriaIsisLevel_Type()
)
tRPOperPSFromCriteriaIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIsisLevel.setStatus("current")
_TRPOperPSFromCriteriaIsisExternal_Type = TruthValue
_TRPOperPSFromCriteriaIsisExternal_Object = MibTableColumn
tRPOperPSFromCriteriaIsisExternal = _TRPOperPSFromCriteriaIsisExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 19),
    _TRPOperPSFromCriteriaIsisExternal_Type()
)
tRPOperPSFromCriteriaIsisExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIsisExternal.setStatus("current")
_TRPOperPSFromCriteriaIgmpHostPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaIgmpHostPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaIgmpHostPrefixList = _TRPOperPSFromCriteriaIgmpHostPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 20),
    _TRPOperPSFromCriteriaIgmpHostPrefixList_Type()
)
tRPOperPSFromCriteriaIgmpHostPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaIgmpHostPrefixList.setStatus("current")
_TRPOperPSFromCriteriaGrpAddrPrefixList_Type = TPrefixListName
_TRPOperPSFromCriteriaGrpAddrPrefixList_Object = MibTableColumn
tRPOperPSFromCriteriaGrpAddrPrefixList = _TRPOperPSFromCriteriaGrpAddrPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 21),
    _TRPOperPSFromCriteriaGrpAddrPrefixList_Type()
)
tRPOperPSFromCriteriaGrpAddrPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaGrpAddrPrefixList.setStatus("current")
_TRPOperPSFromCriteriaSrcAddr_Type = IpAddress
_TRPOperPSFromCriteriaSrcAddr_Object = MibTableColumn
tRPOperPSFromCriteriaSrcAddr = _TRPOperPSFromCriteriaSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 22),
    _TRPOperPSFromCriteriaSrcAddr_Type()
)
tRPOperPSFromCriteriaSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaSrcAddr.setStatus("current")
_TRPOperPSFromCriteriaInterface_Type = TNamedItemOrEmpty
_TRPOperPSFromCriteriaInterface_Object = MibTableColumn
tRPOperPSFromCriteriaInterface = _TRPOperPSFromCriteriaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 23),
    _TRPOperPSFromCriteriaInterface_Type()
)
tRPOperPSFromCriteriaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaInterface.setStatus("current")
_TRPOperPSFromCriteriaTag_Type = TPolicyActionTag
_TRPOperPSFromCriteriaTag_Object = MibTableColumn
tRPOperPSFromCriteriaTag = _TRPOperPSFromCriteriaTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 24),
    _TRPOperPSFromCriteriaTag_Type()
)
tRPOperPSFromCriteriaTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaTag.setStatus("current")
_TRPOperPSFromCritNbrInetAddrType_Type = InetAddressType
_TRPOperPSFromCritNbrInetAddrType_Object = MibTableColumn
tRPOperPSFromCritNbrInetAddrType = _TRPOperPSFromCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 25),
    _TRPOperPSFromCritNbrInetAddrType_Type()
)
tRPOperPSFromCritNbrInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritNbrInetAddrType.setStatus("current")
_TRPOperPSFromCritNbrInetAddr_Type = InetAddress
_TRPOperPSFromCritNbrInetAddr_Object = MibTableColumn
tRPOperPSFromCritNbrInetAddr = _TRPOperPSFromCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 26),
    _TRPOperPSFromCritNbrInetAddr_Type()
)
tRPOperPSFromCritNbrInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritNbrInetAddr.setStatus("current")
_TRPOperPSFromCritSrcInetAddrType_Type = InetAddressType
_TRPOperPSFromCritSrcInetAddrType_Object = MibTableColumn
tRPOperPSFromCritSrcInetAddrType = _TRPOperPSFromCritSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 27),
    _TRPOperPSFromCritSrcInetAddrType_Type()
)
tRPOperPSFromCritSrcInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritSrcInetAddrType.setStatus("current")
_TRPOperPSFromCritSrcInetAddr_Type = InetAddress
_TRPOperPSFromCritSrcInetAddr_Object = MibTableColumn
tRPOperPSFromCritSrcInetAddr = _TRPOperPSFromCritSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 28),
    _TRPOperPSFromCritSrcInetAddr_Type()
)
tRPOperPSFromCritSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritSrcInetAddr.setStatus("current")
_TRPOperPSFromCriteriaFamily_Type = TmnxBGPFamilyType
_TRPOperPSFromCriteriaFamily_Object = MibTableColumn
tRPOperPSFromCriteriaFamily = _TRPOperPSFromCriteriaFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 29),
    _TRPOperPSFromCriteriaFamily_Type()
)
tRPOperPSFromCriteriaFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaFamily.setStatus("current")


class _TRPOperPSFromCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPOperPSFromCriteriaInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPOperPSFromCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPOperPSFromCriteriaInstanceId_Object = MibTableColumn
tRPOperPSFromCriteriaInstanceId = _TRPOperPSFromCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 30),
    _TRPOperPSFromCriteriaInstanceId_Type()
)
tRPOperPSFromCriteriaInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaInstanceId.setStatus("current")
_TRPOperPSFromCriteriaMatchTag_Type = TmnxEnabledDisabled
_TRPOperPSFromCriteriaMatchTag_Object = MibTableColumn
tRPOperPSFromCriteriaMatchTag = _TRPOperPSFromCriteriaMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 31),
    _TRPOperPSFromCriteriaMatchTag_Type()
)
tRPOperPSFromCriteriaMatchTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaMatchTag.setStatus("current")
_TRPOperPSFromCriteriaState_Type = TPolicyEntryCriteriaState
_TRPOperPSFromCriteriaState_Object = MibTableColumn
tRPOperPSFromCriteriaState = _TRPOperPSFromCriteriaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 32),
    _TRPOperPSFromCriteriaState_Type()
)
tRPOperPSFromCriteriaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCriteriaState.setStatus("current")
_TRPOperPSFromCritASPathGroup_Type = TNamedItemOrEmpty
_TRPOperPSFromCritASPathGroup_Object = MibTableColumn
tRPOperPSFromCritASPathGroup = _TRPOperPSFromCritASPathGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 20, 1, 33),
    _TRPOperPSFromCritASPathGroup_Type()
)
tRPOperPSFromCritASPathGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperPSFromCritASPathGroup.setStatus("current")
_TRPOperInetPrefixListTblLastChg_Type = TimeStamp
_TRPOperInetPrefixListTblLastChg_Object = MibScalar
tRPOperInetPrefixListTblLastChg = _TRPOperInetPrefixListTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 21),
    _TRPOperInetPrefixListTblLastChg_Type()
)
tRPOperInetPrefixListTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListTblLastChg.setStatus("obsolete")
_TRPOperInetPrefixListTable_Object = MibTable
tRPOperInetPrefixListTable = _TRPOperInetPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22)
)
if mibBuilder.loadTexts:
    tRPOperInetPrefixListTable.setStatus("current")
_TRPOperInetPrefixListEntry_Object = MibTableRow
tRPOperInetPrefixListEntry = _TRPOperInetPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1)
)
tRPOperInetPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefixType"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListPrefixLen"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPOperInetPrefixListEntry.setStatus("current")


class _TRPOperInetPrefixListName_Type(TPrefixListName):
    """Custom type tRPOperInetPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperInetPrefixListName_Type.__name__ = "TPrefixListName"
_TRPOperInetPrefixListName_Object = MibTableColumn
tRPOperInetPrefixListName = _TRPOperInetPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 1),
    _TRPOperInetPrefixListName_Type()
)
tRPOperInetPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListName.setStatus("current")
_TRPOperInetPrefixListPrefixType_Type = InetAddressType
_TRPOperInetPrefixListPrefixType_Object = MibTableColumn
tRPOperInetPrefixListPrefixType = _TRPOperInetPrefixListPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 2),
    _TRPOperInetPrefixListPrefixType_Type()
)
tRPOperInetPrefixListPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefixType.setStatus("current")
_TRPOperInetPrefixListPrefix_Type = InetAddress
_TRPOperInetPrefixListPrefix_Object = MibTableColumn
tRPOperInetPrefixListPrefix = _TRPOperInetPrefixListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 3),
    _TRPOperInetPrefixListPrefix_Type()
)
tRPOperInetPrefixListPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefix.setStatus("current")
_TRPOperInetPrefixListPrefixLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListPrefixLen_Object = MibTableColumn
tRPOperInetPrefixListPrefixLen = _TRPOperInetPrefixListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 4),
    _TRPOperInetPrefixListPrefixLen_Type()
)
tRPOperInetPrefixListPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListPrefixLen.setStatus("current")


class _TRPOperInetPrefixListType_Type(Integer32):
    """Custom type tRPOperInetPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("range", 4),
          ("through", 3))
    )


_TRPOperInetPrefixListType_Type.__name__ = "Integer32"
_TRPOperInetPrefixListType_Object = MibTableColumn
tRPOperInetPrefixListType = _TRPOperInetPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 5),
    _TRPOperInetPrefixListType_Type()
)
tRPOperInetPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListType.setStatus("current")
_TRPOperInetPrefixListRowStatus_Type = RowStatus
_TRPOperInetPrefixListRowStatus_Object = MibTableColumn
tRPOperInetPrefixListRowStatus = _TRPOperInetPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 6),
    _TRPOperInetPrefixListRowStatus_Type()
)
tRPOperInetPrefixListRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListRowStatus.setStatus("current")
_TRPOperInetPrefixListThroughLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListThroughLen_Object = MibTableColumn
tRPOperInetPrefixListThroughLen = _TRPOperInetPrefixListThroughLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 7),
    _TRPOperInetPrefixListThroughLen_Type()
)
tRPOperInetPrefixListThroughLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListThroughLen.setStatus("current")
_TRPOperInetPrefixListLastChg_Type = TimeStamp
_TRPOperInetPrefixListLastChg_Object = MibTableColumn
tRPOperInetPrefixListLastChg = _TRPOperInetPrefixListLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 8),
    _TRPOperInetPrefixListLastChg_Type()
)
tRPOperInetPrefixListLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListLastChg.setStatus("obsolete")
_TRPOperInetPrefixListBeginLen_Type = InetAddressPrefixLength
_TRPOperInetPrefixListBeginLen_Object = MibTableColumn
tRPOperInetPrefixListBeginLen = _TRPOperInetPrefixListBeginLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 22, 1, 9),
    _TRPOperInetPrefixListBeginLen_Type()
)
tRPOperInetPrefixListBeginLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperInetPrefixListBeginLen.setStatus("current")
_TRPOperCommunityExprTable_Object = MibTable
tRPOperCommunityExprTable = _TRPOperCommunityExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25)
)
if mibBuilder.loadTexts:
    tRPOperCommunityExprTable.setStatus("current")
_TRPOperCommunityExprEntry_Object = MibTableRow
tRPOperCommunityExprEntry = _TRPOperCommunityExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1)
)
tRPOperCommunityExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprName"),
)
if mibBuilder.loadTexts:
    tRPOperCommunityExprEntry.setStatus("current")


class _TRPOperCommunityExprName_Type(TCommunityName):
    """Custom type tRPOperCommunityExprName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperCommunityExprName_Type.__name__ = "TCommunityName"
_TRPOperCommunityExprName_Object = MibTableColumn
tRPOperCommunityExprName = _TRPOperCommunityExprName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 1),
    _TRPOperCommunityExprName_Type()
)
tRPOperCommunityExprName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperCommunityExprName.setStatus("current")
_TRPOperCommunityExprRowStatus_Type = RowStatus
_TRPOperCommunityExprRowStatus_Object = MibTableColumn
tRPOperCommunityExprRowStatus = _TRPOperCommunityExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 2),
    _TRPOperCommunityExprRowStatus_Type()
)
tRPOperCommunityExprRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprRowStatus.setStatus("current")
_TRPOperCommunityExprString1_Type = TCommunityExpression
_TRPOperCommunityExprString1_Object = MibTableColumn
tRPOperCommunityExprString1 = _TRPOperCommunityExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 3),
    _TRPOperCommunityExprString1_Type()
)
tRPOperCommunityExprString1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString1.setStatus("current")
_TRPOperCommunityExprString2_Type = TCommunityExpression
_TRPOperCommunityExprString2_Object = MibTableColumn
tRPOperCommunityExprString2 = _TRPOperCommunityExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 4),
    _TRPOperCommunityExprString2_Type()
)
tRPOperCommunityExprString2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString2.setStatus("current")
_TRPOperCommunityExprString3_Type = TCommunityExpression
_TRPOperCommunityExprString3_Object = MibTableColumn
tRPOperCommunityExprString3 = _TRPOperCommunityExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 5),
    _TRPOperCommunityExprString3_Type()
)
tRPOperCommunityExprString3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString3.setStatus("current")
_TRPOperCommunityExprString4_Type = TCommunityExpression
_TRPOperCommunityExprString4_Object = MibTableColumn
tRPOperCommunityExprString4 = _TRPOperCommunityExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 25, 1, 6),
    _TRPOperCommunityExprString4_Type()
)
tRPOperCommunityExprString4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperCommunityExprString4.setStatus("current")
_TRPOperASPathGroupTable_Object = MibTable
tRPOperASPathGroupTable = _TRPOperASPathGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26)
)
if mibBuilder.loadTexts:
    tRPOperASPathGroupTable.setStatus("current")
_TRPOperASPathGroupEntry_Object = MibTableRow
tRPOperASPathGroupEntry = _TRPOperASPathGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1)
)
tRPOperASPathGroupEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPOperASPathGroupEntry.setStatus("current")
_TRPOperASPathGroupName_Type = TNamedItem
_TRPOperASPathGroupName_Object = MibTableColumn
tRPOperASPathGroupName = _TRPOperASPathGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 1),
    _TRPOperASPathGroupName_Type()
)
tRPOperASPathGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathGroupName.setStatus("current")


class _TRPOperASPathGroupEntryIndex_Type(Unsigned32):
    """Custom type tRPOperASPathGroupEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TRPOperASPathGroupEntryIndex_Type.__name__ = "Unsigned32"
_TRPOperASPathGroupEntryIndex_Object = MibTableColumn
tRPOperASPathGroupEntryIndex = _TRPOperASPathGroupEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 2),
    _TRPOperASPathGroupEntryIndex_Type()
)
tRPOperASPathGroupEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPOperASPathGroupEntryIndex.setStatus("current")
_TRPOperASPathGroupRowStatus_Type = RowStatus
_TRPOperASPathGroupRowStatus_Object = MibTableColumn
tRPOperASPathGroupRowStatus = _TRPOperASPathGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 3),
    _TRPOperASPathGroupRowStatus_Type()
)
tRPOperASPathGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathGroupRowStatus.setStatus("current")


class _TRPOperASPathGroupASPathName_Type(TASPathName):
    """Custom type tRPOperASPathGroupASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPOperASPathGroupASPathName_Type.__name__ = "TASPathName"
_TRPOperASPathGroupASPathName_Object = MibTableColumn
tRPOperASPathGroupASPathName = _TRPOperASPathGroupASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 1, 1, 26, 1, 4),
    _TRPOperASPathGroupASPathName_Type()
)
tRPOperASPathGroupASPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPOperASPathGroupASPathName.setStatus("current")
_TRPAdminObjects_ObjectIdentity = ObjectIdentity
tRPAdminObjects = _TRPAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2)
)
_TRPAdminControlObjects_ObjectIdentity = ObjectIdentity
tRPAdminControlObjects = _TRPAdminControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1)
)


class _TRPAdminOwner_Type(DisplayString):
    """Custom type tRPAdminOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TRPAdminOwner_Type.__name__ = "DisplayString"
_TRPAdminOwner_Object = MibScalar
tRPAdminOwner = _TRPAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 1),
    _TRPAdminOwner_Type()
)
tRPAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminOwner.setStatus("current")


class _TRPAdminControlApply_Type(Integer32):
    """Custom type tRPAdminControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commit", 3),
          ("initialize", 2),
          ("none", 1))
    )


_TRPAdminControlApply_Type.__name__ = "Integer32"
_TRPAdminControlApply_Object = MibScalar
tRPAdminControlApply = _TRPAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 2),
    _TRPAdminControlApply_Type()
)
tRPAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminControlApply.setStatus("current")
_TRPAdminLastSetTimer_Type = TimeInterval
_TRPAdminLastSetTimer_Object = MibScalar
tRPAdminLastSetTimer = _TRPAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 3),
    _TRPAdminLastSetTimer_Type()
)
tRPAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimer.setUnits("centiseconds")


class _TRPAdminLastSetTimeout_Type(TimeInterval):
    """Custom type tRPAdminLastSetTimeout based on TimeInterval"""
    defaultValue = 180000


_TRPAdminLastSetTimeout_Object = MibScalar
tRPAdminLastSetTimeout = _TRPAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 1, 4),
    _TRPAdminLastSetTimeout_Type()
)
tRPAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminLastSetTimeout.setUnits("centiseconds")
_TRPAdminValueObjects_ObjectIdentity = ObjectIdentity
tRPAdminValueObjects = _TRPAdminValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2)
)
_TRPAdminASPathTable_Object = MibTable
tRPAdminASPathTable = _TRPAdminASPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tRPAdminASPathTable.setStatus("current")
_TRPAdminASPathEntry_Object = MibTableRow
tRPAdminASPathEntry = _TRPAdminASPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1)
)
tRPAdminASPathEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathName"),
)
if mibBuilder.loadTexts:
    tRPAdminASPathEntry.setStatus("current")


class _TRPAdminASPathName_Type(TASPathName):
    """Custom type tRPAdminASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminASPathName_Type.__name__ = "TASPathName"
_TRPAdminASPathName_Object = MibTableColumn
tRPAdminASPathName = _TRPAdminASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 1),
    _TRPAdminASPathName_Type()
)
tRPAdminASPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathName.setStatus("current")
_TRPAdminASPathRowStatus_Type = RowStatus
_TRPAdminASPathRowStatus_Object = MibTableColumn
tRPAdminASPathRowStatus = _TRPAdminASPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 2),
    _TRPAdminASPathRowStatus_Type()
)
tRPAdminASPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathRowStatus.setStatus("current")
_TRPAdminASPathRegEx_Type = TRegularExpression
_TRPAdminASPathRegEx_Object = MibTableColumn
tRPAdminASPathRegEx = _TRPAdminASPathRegEx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 1, 1, 3),
    _TRPAdminASPathRegEx_Type()
)
tRPAdminASPathRegEx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathRegEx.setStatus("current")
_TRPAdminCommunityTable_Object = MibTable
tRPAdminCommunityTable = _TRPAdminCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tRPAdminCommunityTable.setStatus("current")
_TRPAdminCommunityEntry_Object = MibTableRow
tRPAdminCommunityEntry = _TRPAdminCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1)
)
tRPAdminCommunityEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityMember"),
)
if mibBuilder.loadTexts:
    tRPAdminCommunityEntry.setStatus("current")


class _TRPAdminCommunityName_Type(TCommunityName):
    """Custom type tRPAdminCommunityName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminCommunityName_Type.__name__ = "TCommunityName"
_TRPAdminCommunityName_Object = MibTableColumn
tRPAdminCommunityName = _TRPAdminCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 1),
    _TRPAdminCommunityName_Type()
)
tRPAdminCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityName.setStatus("current")
_TRPAdminCommunityMember_Type = TCommunityMember
_TRPAdminCommunityMember_Object = MibTableColumn
tRPAdminCommunityMember = _TRPAdminCommunityMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 2),
    _TRPAdminCommunityMember_Type()
)
tRPAdminCommunityMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityMember.setStatus("current")
_TRPAdminCommunityRowStatus_Type = RowStatus
_TRPAdminCommunityRowStatus_Object = MibTableColumn
tRPAdminCommunityRowStatus = _TRPAdminCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 2, 1, 3),
    _TRPAdminCommunityRowStatus_Type()
)
tRPAdminCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityRowStatus.setStatus("current")
_TRPAdminDampingTable_Object = MibTable
tRPAdminDampingTable = _TRPAdminDampingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tRPAdminDampingTable.setStatus("current")
_TRPAdminDampingEntry_Object = MibTableRow
tRPAdminDampingEntry = _TRPAdminDampingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1)
)
tRPAdminDampingEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingName"),
)
if mibBuilder.loadTexts:
    tRPAdminDampingEntry.setStatus("current")


class _TRPAdminDampingName_Type(TDampingName):
    """Custom type tRPAdminDampingName based on TDampingName"""
    subtypeSpec = TDampingName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminDampingName_Type.__name__ = "TDampingName"
_TRPAdminDampingName_Object = MibTableColumn
tRPAdminDampingName = _TRPAdminDampingName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 1),
    _TRPAdminDampingName_Type()
)
tRPAdminDampingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminDampingName.setStatus("current")
_TRPAdminDampingRowStatus_Type = RowStatus
_TRPAdminDampingRowStatus_Object = MibTableColumn
tRPAdminDampingRowStatus = _TRPAdminDampingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 2),
    _TRPAdminDampingRowStatus_Type()
)
tRPAdminDampingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingRowStatus.setStatus("current")


class _TRPAdminDampingHalfLife_Type(Unsigned32):
    """Custom type tRPAdminDampingHalfLife based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_TRPAdminDampingHalfLife_Type.__name__ = "Unsigned32"
_TRPAdminDampingHalfLife_Object = MibTableColumn
tRPAdminDampingHalfLife = _TRPAdminDampingHalfLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 3),
    _TRPAdminDampingHalfLife_Type()
)
tRPAdminDampingHalfLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingHalfLife.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminDampingHalfLife.setUnits("minutes")


class _TRPAdminDampingMaxSuppress_Type(Unsigned32):
    """Custom type tRPAdminDampingMaxSuppress based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TRPAdminDampingMaxSuppress_Type.__name__ = "Unsigned32"
_TRPAdminDampingMaxSuppress_Object = MibTableColumn
tRPAdminDampingMaxSuppress = _TRPAdminDampingMaxSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 4),
    _TRPAdminDampingMaxSuppress_Type()
)
tRPAdminDampingMaxSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingMaxSuppress.setStatus("current")
if mibBuilder.loadTexts:
    tRPAdminDampingMaxSuppress.setUnits("minutes")


class _TRPAdminDampingReuse_Type(Unsigned32):
    """Custom type tRPAdminDampingReuse based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPAdminDampingReuse_Type.__name__ = "Unsigned32"
_TRPAdminDampingReuse_Object = MibTableColumn
tRPAdminDampingReuse = _TRPAdminDampingReuse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 5),
    _TRPAdminDampingReuse_Type()
)
tRPAdminDampingReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingReuse.setStatus("current")


class _TRPAdminDampingSuppress_Type(Unsigned32):
    """Custom type tRPAdminDampingSuppress based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_TRPAdminDampingSuppress_Type.__name__ = "Unsigned32"
_TRPAdminDampingSuppress_Object = MibTableColumn
tRPAdminDampingSuppress = _TRPAdminDampingSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 3, 1, 6),
    _TRPAdminDampingSuppress_Type()
)
tRPAdminDampingSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminDampingSuppress.setStatus("current")
_TRPAdminPrefixListTable_Object = MibTable
tRPAdminPrefixListTable = _TRPAdminPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tRPAdminPrefixListTable.setStatus("current")
_TRPAdminPrefixListEntry_Object = MibTableRow
tRPAdminPrefixListEntry = _TRPAdminPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1)
)
tRPAdminPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListIpPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListMask"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPAdminPrefixListEntry.setStatus("current")


class _TRPAdminPrefixListName_Type(TPrefixListName):
    """Custom type tRPAdminPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminPrefixListName_Type.__name__ = "TPrefixListName"
_TRPAdminPrefixListName_Object = MibTableColumn
tRPAdminPrefixListName = _TRPAdminPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 1),
    _TRPAdminPrefixListName_Type()
)
tRPAdminPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListName.setStatus("current")
_TRPAdminPrefixListIpPrefix_Type = IpAddress
_TRPAdminPrefixListIpPrefix_Object = MibTableColumn
tRPAdminPrefixListIpPrefix = _TRPAdminPrefixListIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 2),
    _TRPAdminPrefixListIpPrefix_Type()
)
tRPAdminPrefixListIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListIpPrefix.setStatus("current")
_TRPAdminPrefixListMask_Type = IpAddressPrefixLength
_TRPAdminPrefixListMask_Object = MibTableColumn
tRPAdminPrefixListMask = _TRPAdminPrefixListMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 3),
    _TRPAdminPrefixListMask_Type()
)
tRPAdminPrefixListMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListMask.setStatus("current")
_TRPAdminPrefixListRowStatus_Type = RowStatus
_TRPAdminPrefixListRowStatus_Object = MibTableColumn
tRPAdminPrefixListRowStatus = _TRPAdminPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 4),
    _TRPAdminPrefixListRowStatus_Type()
)
tRPAdminPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListRowStatus.setStatus("current")


class _TRPAdminPrefixListType_Type(Integer32):
    """Custom type tRPAdminPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("range", 4),
          ("through", 3))
    )


_TRPAdminPrefixListType_Type.__name__ = "Integer32"
_TRPAdminPrefixListType_Object = MibTableColumn
tRPAdminPrefixListType = _TRPAdminPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 5),
    _TRPAdminPrefixListType_Type()
)
tRPAdminPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPrefixListType.setStatus("current")


class _TRPAdminPrefixListThroughLength_Type(IpAddressPrefixLength):
    """Custom type tRPAdminPrefixListThroughLength based on IpAddressPrefixLength"""
    defaultValue = 0


_TRPAdminPrefixListThroughLength_Object = MibTableColumn
tRPAdminPrefixListThroughLength = _TRPAdminPrefixListThroughLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 6),
    _TRPAdminPrefixListThroughLength_Type()
)
tRPAdminPrefixListThroughLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListThroughLength.setStatus("current")


class _TRPAdminPrefixListBeginLength_Type(IpAddressPrefixLength):
    """Custom type tRPAdminPrefixListBeginLength based on IpAddressPrefixLength"""
    defaultValue = 0


_TRPAdminPrefixListBeginLength_Object = MibTableColumn
tRPAdminPrefixListBeginLength = _TRPAdminPrefixListBeginLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 4, 1, 8),
    _TRPAdminPrefixListBeginLength_Type()
)
tRPAdminPrefixListBeginLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPrefixListBeginLength.setStatus("current")
_TRPAdminPolicyStatementTable_Object = MibTable
tRPAdminPolicyStatementTable = _TRPAdminPolicyStatementTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementTable.setStatus("current")
_TRPAdminPolicyStatementEntry_Object = MibTableRow
tRPAdminPolicyStatementEntry = _TRPAdminPolicyStatementEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1)
)
tRPAdminPolicyStatementEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementEntry.setStatus("current")
_TRPAdminPolicyStatementName_Type = TPolicyStatementName
_TRPAdminPolicyStatementName_Object = MibTableColumn
tRPAdminPolicyStatementName = _TRPAdminPolicyStatementName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 1),
    _TRPAdminPolicyStatementName_Type()
)
tRPAdminPolicyStatementName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementName.setStatus("current")
_TRPAdminPolicyStatementRowStatus_Type = RowStatus
_TRPAdminPolicyStatementRowStatus_Object = MibTableColumn
tRPAdminPolicyStatementRowStatus = _TRPAdminPolicyStatementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 2),
    _TRPAdminPolicyStatementRowStatus_Type()
)
tRPAdminPolicyStatementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementRowStatus.setStatus("current")


class _TRPAdminPolicyStatementDescription_Type(TItemDescription):
    """Custom type tRPAdminPolicyStatementDescription based on TItemDescription"""
    defaultHexValue = ""


_TRPAdminPolicyStatementDescription_Object = MibTableColumn
tRPAdminPolicyStatementDescription = _TRPAdminPolicyStatementDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 3),
    _TRPAdminPolicyStatementDescription_Type()
)
tRPAdminPolicyStatementDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementDescription.setStatus("current")


class _TRPAdminPolicyStatementDefaultAction_Type(TPolicyEntryAction):
    """Custom type tRPAdminPolicyStatementDefaultAction based on TPolicyEntryAction"""


_TRPAdminPolicyStatementDefaultAction_Object = MibTableColumn
tRPAdminPolicyStatementDefaultAction = _TRPAdminPolicyStatementDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 5, 1, 4),
    _TRPAdminPolicyStatementDefaultAction_Type()
)
tRPAdminPolicyStatementDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPolicyStatementDefaultAction.setStatus("current")
_TRPAdminPSDefaultActionParamsTable_Object = MibTable
tRPAdminPSDefaultActionParamsTable = _TRPAdminPSDefaultActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionParamsTable.setStatus("current")
_TRPAdminPSDefaultActionParamsEntry_Object = MibTableRow
tRPAdminPSDefaultActionParamsEntry = _TRPAdminPSDefaultActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1)
)
tRPAdminPSDefaultActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
)
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionParamsEntry.setStatus("current")


class _TRPAdminPSDefaultActionASPath_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionASPath based on TPolicyEntryEdit"""


_TRPAdminPSDefaultActionASPath_Object = MibTableColumn
tRPAdminPSDefaultActionASPath = _TRPAdminPSDefaultActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 1),
    _TRPAdminPSDefaultActionASPath_Type()
)
tRPAdminPSDefaultActionASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPath.setStatus("current")


class _TRPAdminPSDefaultActionASPathName_Type(TASPathName):
    """Custom type tRPAdminPSDefaultActionASPathName based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionASPathName_Object = MibTableColumn
tRPAdminPSDefaultActionASPathName = _TRPAdminPSDefaultActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 2),
    _TRPAdminPSDefaultActionASPathName_Type()
)
tRPAdminPSDefaultActionASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathName.setStatus("current")


class _TRPAdminPSDefaultActionASPathPrependAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tRPAdminPSDefaultActionASPathPrependAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TRPAdminPSDefaultActionASPathPrependAS_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPrependAS = _TRPAdminPSDefaultActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 3),
    _TRPAdminPSDefaultActionASPathPrependAS_Type()
)
tRPAdminPSDefaultActionASPathPrependAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPrependAS.setStatus("obsolete")


class _TRPAdminPSDefaultActionASPathPrependCount_Type(Integer32):
    """Custom type tRPAdminPSDefaultActionASPathPrependCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPAdminPSDefaultActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPAdminPSDefaultActionASPathPrependCount_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPrependCount = _TRPAdminPSDefaultActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 4),
    _TRPAdminPSDefaultActionASPathPrependCount_Type()
)
tRPAdminPSDefaultActionASPathPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPrependCount.setStatus("current")


class _TRPAdminPSDefaultActionCommunity1_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionCommunity1 based on TPolicyEntryEdit"""


_TRPAdminPSDefaultActionCommunity1_Object = MibTableColumn
tRPAdminPSDefaultActionCommunity1 = _TRPAdminPSDefaultActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 5),
    _TRPAdminPSDefaultActionCommunity1_Type()
)
tRPAdminPSDefaultActionCommunity1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunity1.setStatus("current")


class _TRPAdminPSDefaultActionCommunityName1_Type(TCommunityName):
    """Custom type tRPAdminPSDefaultActionCommunityName1 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionCommunityName1_Object = MibTableColumn
tRPAdminPSDefaultActionCommunityName1 = _TRPAdminPSDefaultActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 6),
    _TRPAdminPSDefaultActionCommunityName1_Type()
)
tRPAdminPSDefaultActionCommunityName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunityName1.setStatus("current")


class _TRPAdminPSDefaultActionCommunity2_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionCommunity2 based on TPolicyEntryEdit"""


_TRPAdminPSDefaultActionCommunity2_Object = MibTableColumn
tRPAdminPSDefaultActionCommunity2 = _TRPAdminPSDefaultActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 7),
    _TRPAdminPSDefaultActionCommunity2_Type()
)
tRPAdminPSDefaultActionCommunity2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunity2.setStatus("current")


class _TRPAdminPSDefaultActionCommunityName2_Type(TCommunityName):
    """Custom type tRPAdminPSDefaultActionCommunityName2 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionCommunityName2_Object = MibTableColumn
tRPAdminPSDefaultActionCommunityName2 = _TRPAdminPSDefaultActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 8),
    _TRPAdminPSDefaultActionCommunityName2_Type()
)
tRPAdminPSDefaultActionCommunityName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionCommunityName2.setStatus("current")


class _TRPAdminPSDefaultActionOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSDefaultActionOrigin based on TPolicyEntryCriteriaOrigin"""


_TRPAdminPSDefaultActionOrigin_Object = MibTableColumn
tRPAdminPSDefaultActionOrigin = _TRPAdminPSDefaultActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 9),
    _TRPAdminPSDefaultActionOrigin_Type()
)
tRPAdminPSDefaultActionOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionOrigin.setStatus("current")


class _TRPAdminPSDefaultActionLocalPreferenceSet_Type(TruthValue):
    """Custom type tRPAdminPSDefaultActionLocalPreferenceSet based on TruthValue"""


_TRPAdminPSDefaultActionLocalPreferenceSet_Object = MibTableColumn
tRPAdminPSDefaultActionLocalPreferenceSet = _TRPAdminPSDefaultActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 10),
    _TRPAdminPSDefaultActionLocalPreferenceSet_Type()
)
tRPAdminPSDefaultActionLocalPreferenceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionLocalPreferenceSet.setStatus("current")


class _TRPAdminPSDefaultActionLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tRPAdminPSDefaultActionLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 0


_TRPAdminPSDefaultActionLocalPreference_Object = MibTableColumn
tRPAdminPSDefaultActionLocalPreference = _TRPAdminPSDefaultActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 11),
    _TRPAdminPSDefaultActionLocalPreference_Type()
)
tRPAdminPSDefaultActionLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionLocalPreference.setStatus("current")


class _TRPAdminPSDefaultActionMetric_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSDefaultActionMetric based on TPolicyEntryEdit"""


_TRPAdminPSDefaultActionMetric_Object = MibTableColumn
tRPAdminPSDefaultActionMetric = _TRPAdminPSDefaultActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 12),
    _TRPAdminPSDefaultActionMetric_Type()
)
tRPAdminPSDefaultActionMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionMetric.setStatus("current")


class _TRPAdminPSDefaultActionMetricValue_Type(Unsigned32):
    """Custom type tRPAdminPSDefaultActionMetricValue based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSDefaultActionMetricValue_Object = MibTableColumn
tRPAdminPSDefaultActionMetricValue = _TRPAdminPSDefaultActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 13),
    _TRPAdminPSDefaultActionMetricValue_Type()
)
tRPAdminPSDefaultActionMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionMetricValue.setStatus("current")


class _TRPAdminPSDefaultActionPreference_Type(TmnxBgpPreference):
    """Custom type tRPAdminPSDefaultActionPreference based on TmnxBgpPreference"""
    defaultValue = 0


_TRPAdminPSDefaultActionPreference_Object = MibTableColumn
tRPAdminPSDefaultActionPreference = _TRPAdminPSDefaultActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 15),
    _TRPAdminPSDefaultActionPreference_Type()
)
tRPAdminPSDefaultActionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionPreference.setStatus("current")


class _TRPAdminPSDefaultActionDamping_Type(TDampingName):
    """Custom type tRPAdminPSDefaultActionDamping based on TDampingName"""
    defaultHexValue = ""


_TRPAdminPSDefaultActionDamping_Object = MibTableColumn
tRPAdminPSDefaultActionDamping = _TRPAdminPSDefaultActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 16),
    _TRPAdminPSDefaultActionDamping_Type()
)
tRPAdminPSDefaultActionDamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionDamping.setStatus("current")


class _TRPAdminPSDefaultActionNextHopSelf_Type(TruthValue):
    """Custom type tRPAdminPSDefaultActionNextHopSelf based on TruthValue"""


_TRPAdminPSDefaultActionNextHopSelf_Object = MibTableColumn
tRPAdminPSDefaultActionNextHopSelf = _TRPAdminPSDefaultActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 17),
    _TRPAdminPSDefaultActionNextHopSelf_Type()
)
tRPAdminPSDefaultActionNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionNextHopSelf.setStatus("current")


class _TRPAdminPSDefaultActionNextHop_Type(IpAddress):
    """Custom type tRPAdminPSDefaultActionNextHop based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TRPAdminPSDefaultActionNextHop_Object = MibTableColumn
tRPAdminPSDefaultActionNextHop = _TRPAdminPSDefaultActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 18),
    _TRPAdminPSDefaultActionNextHop_Type()
)
tRPAdminPSDefaultActionNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionNextHop.setStatus("current")


class _TRPAdminPSDefaultActionTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSDefaultActionTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSDefaultActionTag_Object = MibTableColumn
tRPAdminPSDefaultActionTag = _TRPAdminPSDefaultActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 19),
    _TRPAdminPSDefaultActionTag_Type()
)
tRPAdminPSDefaultActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionTag.setStatus("current")


class _TRPAdminPSDefaultActionOspfType_Type(TOspfRouteType):
    """Custom type tRPAdminPSDefaultActionOspfType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSDefaultActionOspfType_Object = MibTableColumn
tRPAdminPSDefaultActionOspfType = _TRPAdminPSDefaultActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 20),
    _TRPAdminPSDefaultActionOspfType_Type()
)
tRPAdminPSDefaultActionOspfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionOspfType.setStatus("current")
_TRPAdminPSDefActInetNextHopType_Type = InetAddressType
_TRPAdminPSDefActInetNextHopType_Object = MibTableColumn
tRPAdminPSDefActInetNextHopType = _TRPAdminPSDefActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 21),
    _TRPAdminPSDefActInetNextHopType_Type()
)
tRPAdminPSDefActInetNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActInetNextHopType.setStatus("current")
_TRPAdminPSDefActInetNextHop_Type = InetAddress
_TRPAdminPSDefActInetNextHop_Object = MibTableColumn
tRPAdminPSDefActInetNextHop = _TRPAdminPSDefActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 22),
    _TRPAdminPSDefActInetNextHop_Type()
)
tRPAdminPSDefActInetNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActInetNextHop.setStatus("current")


class _TRPAdminPSDefaultActionASPathPnd_Type(InetAutonomousSystemNumber):
    """Custom type tRPAdminPSDefaultActionASPathPnd based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TRPAdminPSDefaultActionASPathPnd_Object = MibTableColumn
tRPAdminPSDefaultActionASPathPnd = _TRPAdminPSDefaultActionASPathPnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 23),
    _TRPAdminPSDefaultActionASPathPnd_Type()
)
tRPAdminPSDefaultActionASPathPnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefaultActionASPathPnd.setStatus("current")


class _TRPAdminPSDefActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPAdminPSDefActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPAdminPSDefActMcRedirSvcId_Object = MibTableColumn
tRPAdminPSDefActMcRedirSvcId = _TRPAdminPSDefActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 30),
    _TRPAdminPSDefActMcRedirSvcId_Type()
)
tRPAdminPSDefActMcRedirSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActMcRedirSvcId.setStatus("current")


class _TRPAdminPSDefActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPAdminPSDefActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPAdminPSDefActMcRedirIfIndex_Object = MibTableColumn
tRPAdminPSDefActMcRedirIfIndex = _TRPAdminPSDefActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 31),
    _TRPAdminPSDefActMcRedirIfIndex_Type()
)
tRPAdminPSDefActMcRedirIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActMcRedirIfIndex.setStatus("current")


class _TRPAdminPSDefActionMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPAdminPSDefActionMetricSource based on TPolicyActionMetricSource"""


_TRPAdminPSDefActionMetricSource_Object = MibTableColumn
tRPAdminPSDefActionMetricSource = _TRPAdminPSDefActionMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 32),
    _TRPAdminPSDefActionMetricSource_Type()
)
tRPAdminPSDefActionMetricSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionMetricSource.setStatus("current")


class _TRPAdminPSDefActionAigpMetric_Type(TPolicyEntryAigpMetricEdit):
    """Custom type tRPAdminPSDefActionAigpMetric based on TPolicyEntryAigpMetricEdit"""


_TRPAdminPSDefActionAigpMetric_Object = MibTableColumn
tRPAdminPSDefActionAigpMetric = _TRPAdminPSDefActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 33),
    _TRPAdminPSDefActionAigpMetric_Type()
)
tRPAdminPSDefActionAigpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActionAigpMetric.setStatus("current")


class _TRPAdminPSDefActnAigpMetricVal_Type(Unsigned32):
    """Custom type tRPAdminPSDefActnAigpMetricVal based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSDefActnAigpMetricVal_Object = MibTableColumn
tRPAdminPSDefActnAigpMetricVal = _TRPAdminPSDefActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 6, 1, 34),
    _TRPAdminPSDefActnAigpMetricVal_Type()
)
tRPAdminPSDefActnAigpMetricVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSDefActnAigpMetricVal.setStatus("current")
_TRPAdminPSParamsTable_Object = MibTable
tRPAdminPSParamsTable = _TRPAdminPSParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tRPAdminPSParamsTable.setStatus("current")
_TRPAdminPSParamsEntry_Object = MibTableRow
tRPAdminPSParamsEntry = _TRPAdminPSParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1)
)
tRPAdminPSParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSParamsEntry.setStatus("current")
_TRPAdminPSNameEntryIndex_Type = TPolicyStatementEntryID
_TRPAdminPSNameEntryIndex_Object = MibTableColumn
tRPAdminPSNameEntryIndex = _TRPAdminPSNameEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 1),
    _TRPAdminPSNameEntryIndex_Type()
)
tRPAdminPSNameEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSNameEntryIndex.setStatus("current")
_TRPAdminPSParamsRowStatus_Type = RowStatus
_TRPAdminPSParamsRowStatus_Object = MibTableColumn
tRPAdminPSParamsRowStatus = _TRPAdminPSParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 2),
    _TRPAdminPSParamsRowStatus_Type()
)
tRPAdminPSParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsRowStatus.setStatus("current")


class _TRPAdminPSParamsDescription_Type(TItemDescription):
    """Custom type tRPAdminPSParamsDescription based on TItemDescription"""
    defaultHexValue = ""


_TRPAdminPSParamsDescription_Object = MibTableColumn
tRPAdminPSParamsDescription = _TRPAdminPSParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 3),
    _TRPAdminPSParamsDescription_Type()
)
tRPAdminPSParamsDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsDescription.setStatus("current")
_TRPAdminPSParamsAction_Type = TPolicyEntryAction
_TRPAdminPSParamsAction_Object = MibTableColumn
tRPAdminPSParamsAction = _TRPAdminPSParamsAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 7, 1, 4),
    _TRPAdminPSParamsAction_Type()
)
tRPAdminPSParamsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSParamsAction.setStatus("current")
_TRPAdminPSAcceptActionParamsTable_Object = MibTable
tRPAdminPSAcceptActionParamsTable = _TRPAdminPSAcceptActionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionParamsTable.setStatus("current")
_TRPAdminPSAcceptActionParamsEntry_Object = MibTableRow
tRPAdminPSAcceptActionParamsEntry = _TRPAdminPSAcceptActionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1)
)
tRPAdminPSAcceptActionParamsEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSNameEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionParamsEntry.setStatus("current")


class _TRPAdminPSAcceptActionASPath_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionASPath based on TPolicyEntryEdit"""


_TRPAdminPSAcceptActionASPath_Object = MibTableColumn
tRPAdminPSAcceptActionASPath = _TRPAdminPSAcceptActionASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 1),
    _TRPAdminPSAcceptActionASPath_Type()
)
tRPAdminPSAcceptActionASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPath.setStatus("current")


class _TRPAdminPSAcceptActionASPathName_Type(TASPathName):
    """Custom type tRPAdminPSAcceptActionASPathName based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionASPathName_Object = MibTableColumn
tRPAdminPSAcceptActionASPathName = _TRPAdminPSAcceptActionASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 2),
    _TRPAdminPSAcceptActionASPathName_Type()
)
tRPAdminPSAcceptActionASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathName.setStatus("current")


class _TRPAdminPSAcceptActionASPathPrependAS_Type(TmnxBgpAutonomousSystem):
    """Custom type tRPAdminPSAcceptActionASPathPrependAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_TRPAdminPSAcceptActionASPathPrependAS_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPrependAS = _TRPAdminPSAcceptActionASPathPrependAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 3),
    _TRPAdminPSAcceptActionASPathPrependAS_Type()
)
tRPAdminPSAcceptActionASPathPrependAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPrependAS.setStatus("obsolete")


class _TRPAdminPSAcceptActionASPathPrependCount_Type(Integer32):
    """Custom type tRPAdminPSAcceptActionASPathPrependCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TRPAdminPSAcceptActionASPathPrependCount_Type.__name__ = "Integer32"
_TRPAdminPSAcceptActionASPathPrependCount_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPrependCount = _TRPAdminPSAcceptActionASPathPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 4),
    _TRPAdminPSAcceptActionASPathPrependCount_Type()
)
tRPAdminPSAcceptActionASPathPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPrependCount.setStatus("current")


class _TRPAdminPSAcceptActionCommunity1_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionCommunity1 based on TPolicyEntryEdit"""


_TRPAdminPSAcceptActionCommunity1_Object = MibTableColumn
tRPAdminPSAcceptActionCommunity1 = _TRPAdminPSAcceptActionCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 5),
    _TRPAdminPSAcceptActionCommunity1_Type()
)
tRPAdminPSAcceptActionCommunity1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunity1.setStatus("current")


class _TRPAdminPSAcceptActionCommunityName1_Type(TCommunityName):
    """Custom type tRPAdminPSAcceptActionCommunityName1 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionCommunityName1_Object = MibTableColumn
tRPAdminPSAcceptActionCommunityName1 = _TRPAdminPSAcceptActionCommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 6),
    _TRPAdminPSAcceptActionCommunityName1_Type()
)
tRPAdminPSAcceptActionCommunityName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunityName1.setStatus("current")


class _TRPAdminPSAcceptActionCommunity2_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionCommunity2 based on TPolicyEntryEdit"""


_TRPAdminPSAcceptActionCommunity2_Object = MibTableColumn
tRPAdminPSAcceptActionCommunity2 = _TRPAdminPSAcceptActionCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 7),
    _TRPAdminPSAcceptActionCommunity2_Type()
)
tRPAdminPSAcceptActionCommunity2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunity2.setStatus("current")


class _TRPAdminPSAcceptActionCommunityName2_Type(TCommunityName):
    """Custom type tRPAdminPSAcceptActionCommunityName2 based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionCommunityName2_Object = MibTableColumn
tRPAdminPSAcceptActionCommunityName2 = _TRPAdminPSAcceptActionCommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 8),
    _TRPAdminPSAcceptActionCommunityName2_Type()
)
tRPAdminPSAcceptActionCommunityName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionCommunityName2.setStatus("current")


class _TRPAdminPSAcceptActionOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSAcceptActionOrigin based on TPolicyEntryCriteriaOrigin"""


_TRPAdminPSAcceptActionOrigin_Object = MibTableColumn
tRPAdminPSAcceptActionOrigin = _TRPAdminPSAcceptActionOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 9),
    _TRPAdminPSAcceptActionOrigin_Type()
)
tRPAdminPSAcceptActionOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionOrigin.setStatus("current")


class _TRPAdminPSAcceptActionLocalPreferenceSet_Type(TruthValue):
    """Custom type tRPAdminPSAcceptActionLocalPreferenceSet based on TruthValue"""


_TRPAdminPSAcceptActionLocalPreferenceSet_Object = MibTableColumn
tRPAdminPSAcceptActionLocalPreferenceSet = _TRPAdminPSAcceptActionLocalPreferenceSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 10),
    _TRPAdminPSAcceptActionLocalPreferenceSet_Type()
)
tRPAdminPSAcceptActionLocalPreferenceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionLocalPreferenceSet.setStatus("current")


class _TRPAdminPSAcceptActionLocalPreference_Type(TmnxBgpLocalPreference):
    """Custom type tRPAdminPSAcceptActionLocalPreference based on TmnxBgpLocalPreference"""
    defaultValue = 0


_TRPAdminPSAcceptActionLocalPreference_Object = MibTableColumn
tRPAdminPSAcceptActionLocalPreference = _TRPAdminPSAcceptActionLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 11),
    _TRPAdminPSAcceptActionLocalPreference_Type()
)
tRPAdminPSAcceptActionLocalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionLocalPreference.setStatus("current")


class _TRPAdminPSAcceptActionMetric_Type(TPolicyEntryEdit):
    """Custom type tRPAdminPSAcceptActionMetric based on TPolicyEntryEdit"""


_TRPAdminPSAcceptActionMetric_Object = MibTableColumn
tRPAdminPSAcceptActionMetric = _TRPAdminPSAcceptActionMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 12),
    _TRPAdminPSAcceptActionMetric_Type()
)
tRPAdminPSAcceptActionMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionMetric.setStatus("current")


class _TRPAdminPSAcceptActionMetricValue_Type(Unsigned32):
    """Custom type tRPAdminPSAcceptActionMetricValue based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSAcceptActionMetricValue_Object = MibTableColumn
tRPAdminPSAcceptActionMetricValue = _TRPAdminPSAcceptActionMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 13),
    _TRPAdminPSAcceptActionMetricValue_Type()
)
tRPAdminPSAcceptActionMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionMetricValue.setStatus("current")


class _TRPAdminPSAcceptActionPreference_Type(TmnxBgpPreference):
    """Custom type tRPAdminPSAcceptActionPreference based on TmnxBgpPreference"""
    defaultValue = 0


_TRPAdminPSAcceptActionPreference_Object = MibTableColumn
tRPAdminPSAcceptActionPreference = _TRPAdminPSAcceptActionPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 15),
    _TRPAdminPSAcceptActionPreference_Type()
)
tRPAdminPSAcceptActionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionPreference.setStatus("current")


class _TRPAdminPSAcceptActionDamping_Type(TDampingName):
    """Custom type tRPAdminPSAcceptActionDamping based on TDampingName"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionDamping_Object = MibTableColumn
tRPAdminPSAcceptActionDamping = _TRPAdminPSAcceptActionDamping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 16),
    _TRPAdminPSAcceptActionDamping_Type()
)
tRPAdminPSAcceptActionDamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionDamping.setStatus("current")


class _TRPAdminPSAcceptActionNextHopSelf_Type(TruthValue):
    """Custom type tRPAdminPSAcceptActionNextHopSelf based on TruthValue"""


_TRPAdminPSAcceptActionNextHopSelf_Object = MibTableColumn
tRPAdminPSAcceptActionNextHopSelf = _TRPAdminPSAcceptActionNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 17),
    _TRPAdminPSAcceptActionNextHopSelf_Type()
)
tRPAdminPSAcceptActionNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionNextHopSelf.setStatus("current")


class _TRPAdminPSAcceptActionNextHop_Type(IpAddress):
    """Custom type tRPAdminPSAcceptActionNextHop based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TRPAdminPSAcceptActionNextHop_Object = MibTableColumn
tRPAdminPSAcceptActionNextHop = _TRPAdminPSAcceptActionNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 18),
    _TRPAdminPSAcceptActionNextHop_Type()
)
tRPAdminPSAcceptActionNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionNextHop.setStatus("current")


class _TRPAdminPSAcceptActionTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSAcceptActionTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSAcceptActionTag_Object = MibTableColumn
tRPAdminPSAcceptActionTag = _TRPAdminPSAcceptActionTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 19),
    _TRPAdminPSAcceptActionTag_Type()
)
tRPAdminPSAcceptActionTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionTag.setStatus("current")


class _TRPAdminPSAcceptActionOspfType_Type(TOspfRouteType):
    """Custom type tRPAdminPSAcceptActionOspfType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSAcceptActionOspfType_Object = MibTableColumn
tRPAdminPSAcceptActionOspfType = _TRPAdminPSAcceptActionOspfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 20),
    _TRPAdminPSAcceptActionOspfType_Type()
)
tRPAdminPSAcceptActionOspfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionOspfType.setStatus("current")
_TRPAdminPSAcptActInetNextHopType_Type = InetAddressType
_TRPAdminPSAcptActInetNextHopType_Object = MibTableColumn
tRPAdminPSAcptActInetNextHopType = _TRPAdminPSAcptActInetNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 21),
    _TRPAdminPSAcptActInetNextHopType_Type()
)
tRPAdminPSAcptActInetNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActInetNextHopType.setStatus("current")
_TRPAdminPSAcptActInetNextHop_Type = InetAddress
_TRPAdminPSAcptActInetNextHop_Object = MibTableColumn
tRPAdminPSAcptActInetNextHop = _TRPAdminPSAcptActInetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 22),
    _TRPAdminPSAcptActInetNextHop_Type()
)
tRPAdminPSAcptActInetNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActInetNextHop.setStatus("current")


class _TRPAdminPSAcceptActionASPathPend_Type(InetAutonomousSystemNumber):
    """Custom type tRPAdminPSAcceptActionASPathPend based on InetAutonomousSystemNumber"""
    defaultValue = 0


_TRPAdminPSAcceptActionASPathPend_Object = MibTableColumn
tRPAdminPSAcceptActionASPathPend = _TRPAdminPSAcceptActionASPathPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 23),
    _TRPAdminPSAcceptActionASPathPend_Type()
)
tRPAdminPSAcceptActionASPathPend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionASPathPend.setStatus("current")


class _TRPAdminPSAcceptActionFC_Type(TNamedItemOrEmpty):
    """Custom type tRPAdminPSAcceptActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TRPAdminPSAcceptActionFC_Object = MibTableColumn
tRPAdminPSAcceptActionFC = _TRPAdminPSAcceptActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 24),
    _TRPAdminPSAcceptActionFC_Type()
)
tRPAdminPSAcceptActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionFC.setStatus("current")


class _TRPAdminPSAcceptActionFCPriority_Type(TPriorityOrUndefined):
    """Custom type tRPAdminPSAcceptActionFCPriority based on TPriorityOrUndefined"""


_TRPAdminPSAcceptActionFCPriority_Object = MibTableColumn
tRPAdminPSAcceptActionFCPriority = _TRPAdminPSAcceptActionFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 25),
    _TRPAdminPSAcceptActionFCPriority_Type()
)
tRPAdminPSAcceptActionFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcceptActionFCPriority.setStatus("current")


class _TRPAdminPSAcptActMcRedirSvcId_Type(TmnxServId):
    """Custom type tRPAdminPSAcptActMcRedirSvcId based on TmnxServId"""
    defaultValue = 0


_TRPAdminPSAcptActMcRedirSvcId_Object = MibTableColumn
tRPAdminPSAcptActMcRedirSvcId = _TRPAdminPSAcptActMcRedirSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 30),
    _TRPAdminPSAcptActMcRedirSvcId_Type()
)
tRPAdminPSAcptActMcRedirSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActMcRedirSvcId.setStatus("current")


class _TRPAdminPSAcptActMcRedirIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tRPAdminPSAcptActMcRedirIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TRPAdminPSAcptActMcRedirIfIndex_Object = MibTableColumn
tRPAdminPSAcptActMcRedirIfIndex = _TRPAdminPSAcptActMcRedirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 31),
    _TRPAdminPSAcptActMcRedirIfIndex_Type()
)
tRPAdminPSAcptActMcRedirIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActMcRedirIfIndex.setStatus("current")


class _TRPAdminPSAcptActnMetricSource_Type(TPolicyActionMetricSource):
    """Custom type tRPAdminPSAcptActnMetricSource based on TPolicyActionMetricSource"""


_TRPAdminPSAcptActnMetricSource_Object = MibTableColumn
tRPAdminPSAcptActnMetricSource = _TRPAdminPSAcptActnMetricSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 32),
    _TRPAdminPSAcptActnMetricSource_Type()
)
tRPAdminPSAcptActnMetricSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnMetricSource.setStatus("current")


class _TRPAdminPSAcptActionAigpMetric_Type(TPolicyEntryAigpMetricEdit):
    """Custom type tRPAdminPSAcptActionAigpMetric based on TPolicyEntryAigpMetricEdit"""


_TRPAdminPSAcptActionAigpMetric_Object = MibTableColumn
tRPAdminPSAcptActionAigpMetric = _TRPAdminPSAcptActionAigpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 33),
    _TRPAdminPSAcptActionAigpMetric_Type()
)
tRPAdminPSAcptActionAigpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActionAigpMetric.setStatus("current")


class _TRPAdminPSAcptActnAigpMetricVal_Type(Unsigned32):
    """Custom type tRPAdminPSAcptActnAigpMetricVal based on Unsigned32"""
    defaultValue = 0


_TRPAdminPSAcptActnAigpMetricVal_Object = MibTableColumn
tRPAdminPSAcptActnAigpMetricVal = _TRPAdminPSAcptActnAigpMetricVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 8, 1, 34),
    _TRPAdminPSAcptActnAigpMetricVal_Type()
)
tRPAdminPSAcptActnAigpMetricVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSAcptActnAigpMetricVal.setStatus("current")
_TRPAdminPSToCriteriaTable_Object = MibTable
tRPAdminPSToCriteriaTable = _TRPAdminPSToCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaTable.setStatus("current")
_TRPAdminPSToCriteriaEntry_Object = MibTableRow
tRPAdminPSToCriteriaEntry = _TRPAdminPSToCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1)
)
tRPAdminPSToCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaEntry.setStatus("current")
_TRPAdminPSToCriteriaIndex_Type = TPolicyStatementEntryID
_TRPAdminPSToCriteriaIndex_Object = MibTableColumn
tRPAdminPSToCriteriaIndex = _TRPAdminPSToCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 1),
    _TRPAdminPSToCriteriaIndex_Type()
)
tRPAdminPSToCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaIndex.setStatus("current")
_TRPAdminPSToCriteriaRowStatus_Type = RowStatus
_TRPAdminPSToCriteriaRowStatus_Object = MibTableColumn
tRPAdminPSToCriteriaRowStatus = _TRPAdminPSToCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 2),
    _TRPAdminPSToCriteriaRowStatus_Type()
)
tRPAdminPSToCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaRowStatus.setStatus("current")


class _TRPAdminPSToCriteriaProtocol_Type(TRoutePolicyProtocol):
    """Custom type tRPAdminPSToCriteriaProtocol based on TRoutePolicyProtocol"""


_TRPAdminPSToCriteriaProtocol_Object = MibTableColumn
tRPAdminPSToCriteriaProtocol = _TRPAdminPSToCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 3),
    _TRPAdminPSToCriteriaProtocol_Type()
)
tRPAdminPSToCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaProtocol.setStatus("current")


class _TRPAdminPSToCriteriaNeighborIpAddr_Type(IpAddress):
    """Custom type tRPAdminPSToCriteriaNeighborIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TRPAdminPSToCriteriaNeighborIpAddr_Object = MibTableColumn
tRPAdminPSToCriteriaNeighborIpAddr = _TRPAdminPSToCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 4),
    _TRPAdminPSToCriteriaNeighborIpAddr_Type()
)
tRPAdminPSToCriteriaNeighborIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaNeighborIpAddr.setStatus("current")


class _TRPAdminPSToCriteriaNeighborPrefixList_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaNeighborPrefixList based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaNeighborPrefixList_Object = MibTableColumn
tRPAdminPSToCriteriaNeighborPrefixList = _TRPAdminPSToCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 5),
    _TRPAdminPSToCriteriaNeighborPrefixList_Type()
)
tRPAdminPSToCriteriaNeighborPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaNeighborPrefixList.setStatus("current")


class _TRPAdminPSToCriteriaIsisLevel_Type(TIsisLevel):
    """Custom type tRPAdminPSToCriteriaIsisLevel based on TIsisLevel"""
    defaultValue = 0


_TRPAdminPSToCriteriaIsisLevel_Object = MibTableColumn
tRPAdminPSToCriteriaIsisLevel = _TRPAdminPSToCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 7),
    _TRPAdminPSToCriteriaIsisLevel_Type()
)
tRPAdminPSToCriteriaIsisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaIsisLevel.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList1_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList1 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList1_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList1 = _TRPAdminPSToCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 8),
    _TRPAdminPSToCriteriaPrefixList1_Type()
)
tRPAdminPSToCriteriaPrefixList1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList1.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList2_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList2 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList2_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList2 = _TRPAdminPSToCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 9),
    _TRPAdminPSToCriteriaPrefixList2_Type()
)
tRPAdminPSToCriteriaPrefixList2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList2.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList3_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList3 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList3_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList3 = _TRPAdminPSToCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 10),
    _TRPAdminPSToCriteriaPrefixList3_Type()
)
tRPAdminPSToCriteriaPrefixList3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList3.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList4_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList4 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList4_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList4 = _TRPAdminPSToCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 11),
    _TRPAdminPSToCriteriaPrefixList4_Type()
)
tRPAdminPSToCriteriaPrefixList4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList4.setStatus("current")


class _TRPAdminPSToCriteriaPrefixList5_Type(TPrefixListName):
    """Custom type tRPAdminPSToCriteriaPrefixList5 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSToCriteriaPrefixList5_Object = MibTableColumn
tRPAdminPSToCriteriaPrefixList5 = _TRPAdminPSToCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 12),
    _TRPAdminPSToCriteriaPrefixList5_Type()
)
tRPAdminPSToCriteriaPrefixList5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaPrefixList5.setStatus("current")
_TRPAdminPSToCritNbrInetAddrType_Type = InetAddressType
_TRPAdminPSToCritNbrInetAddrType_Object = MibTableColumn
tRPAdminPSToCritNbrInetAddrType = _TRPAdminPSToCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 13),
    _TRPAdminPSToCritNbrInetAddrType_Type()
)
tRPAdminPSToCritNbrInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCritNbrInetAddrType.setStatus("current")
_TRPAdminPSToCritNbrInetAddr_Type = InetAddress
_TRPAdminPSToCritNbrInetAddr_Object = MibTableColumn
tRPAdminPSToCritNbrInetAddr = _TRPAdminPSToCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 14),
    _TRPAdminPSToCritNbrInetAddr_Type()
)
tRPAdminPSToCritNbrInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCritNbrInetAddr.setStatus("current")


class _TRPAdminPSToCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPAdminPSToCriteriaInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPAdminPSToCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPAdminPSToCriteriaInstanceId_Object = MibTableColumn
tRPAdminPSToCriteriaInstanceId = _TRPAdminPSToCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 9, 1, 15),
    _TRPAdminPSToCriteriaInstanceId_Type()
)
tRPAdminPSToCriteriaInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSToCriteriaInstanceId.setStatus("current")
_TRPAdminPSFromCriteriaTable_Object = MibTable
tRPAdminPSFromCriteriaTable = _TRPAdminPSFromCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10)
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaTable.setStatus("current")
_TRPAdminPSFromCriteriaEntry_Object = MibTableRow
tRPAdminPSFromCriteriaEntry = _TRPAdminPSFromCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1)
)
tRPAdminPSFromCriteriaEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaEntry.setStatus("current")
_TRPAdminPSFromCriteriaIndex_Type = TPolicyStatementEntryID
_TRPAdminPSFromCriteriaIndex_Object = MibTableColumn
tRPAdminPSFromCriteriaIndex = _TRPAdminPSFromCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 1),
    _TRPAdminPSFromCriteriaIndex_Type()
)
tRPAdminPSFromCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIndex.setStatus("current")
_TRPAdminPSFromCriteriaRowStatus_Type = RowStatus
_TRPAdminPSFromCriteriaRowStatus_Object = MibTableColumn
tRPAdminPSFromCriteriaRowStatus = _TRPAdminPSFromCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 2),
    _TRPAdminPSFromCriteriaRowStatus_Type()
)
tRPAdminPSFromCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaRowStatus.setStatus("current")


class _TRPAdminPSFromCriteriaProtocol_Type(TRoutePolicyProtocol):
    """Custom type tRPAdminPSFromCriteriaProtocol based on TRoutePolicyProtocol"""


_TRPAdminPSFromCriteriaProtocol_Object = MibTableColumn
tRPAdminPSFromCriteriaProtocol = _TRPAdminPSFromCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 3),
    _TRPAdminPSFromCriteriaProtocol_Type()
)
tRPAdminPSFromCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaProtocol.setStatus("current")


class _TRPAdminPSFromCriteriaNeighborIpAddr_Type(IpAddress):
    """Custom type tRPAdminPSFromCriteriaNeighborIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TRPAdminPSFromCriteriaNeighborIpAddr_Object = MibTableColumn
tRPAdminPSFromCriteriaNeighborIpAddr = _TRPAdminPSFromCriteriaNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 4),
    _TRPAdminPSFromCriteriaNeighborIpAddr_Type()
)
tRPAdminPSFromCriteriaNeighborIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaNeighborIpAddr.setStatus("current")


class _TRPAdminPSFromCriteriaNeighborPrefixList_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaNeighborPrefixList based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaNeighborPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaNeighborPrefixList = _TRPAdminPSFromCriteriaNeighborPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 5),
    _TRPAdminPSFromCriteriaNeighborPrefixList_Type()
)
tRPAdminPSFromCriteriaNeighborPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaNeighborPrefixList.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList1_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList1 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList1_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList1 = _TRPAdminPSFromCriteriaPrefixList1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 6),
    _TRPAdminPSFromCriteriaPrefixList1_Type()
)
tRPAdminPSFromCriteriaPrefixList1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList1.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList2_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList2 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList2_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList2 = _TRPAdminPSFromCriteriaPrefixList2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 7),
    _TRPAdminPSFromCriteriaPrefixList2_Type()
)
tRPAdminPSFromCriteriaPrefixList2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList2.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList3_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList3 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList3_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList3 = _TRPAdminPSFromCriteriaPrefixList3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 8),
    _TRPAdminPSFromCriteriaPrefixList3_Type()
)
tRPAdminPSFromCriteriaPrefixList3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList3.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList4_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList4 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList4_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList4 = _TRPAdminPSFromCriteriaPrefixList4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 9),
    _TRPAdminPSFromCriteriaPrefixList4_Type()
)
tRPAdminPSFromCriteriaPrefixList4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList4.setStatus("current")


class _TRPAdminPSFromCriteriaPrefixList5_Type(TPrefixListName):
    """Custom type tRPAdminPSFromCriteriaPrefixList5 based on TPrefixListName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaPrefixList5_Object = MibTableColumn
tRPAdminPSFromCriteriaPrefixList5 = _TRPAdminPSFromCriteriaPrefixList5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 10),
    _TRPAdminPSFromCriteriaPrefixList5_Type()
)
tRPAdminPSFromCriteriaPrefixList5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaPrefixList5.setStatus("current")


class _TRPAdminPSFromCriteriaASPath_Type(TASPathName):
    """Custom type tRPAdminPSFromCriteriaASPath based on TASPathName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaASPath_Object = MibTableColumn
tRPAdminPSFromCriteriaASPath = _TRPAdminPSFromCriteriaASPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 11),
    _TRPAdminPSFromCriteriaASPath_Type()
)
tRPAdminPSFromCriteriaASPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaASPath.setStatus("current")


class _TRPAdminPSFromCriteriaCommunity_Type(TCommunityName):
    """Custom type tRPAdminPSFromCriteriaCommunity based on TCommunityName"""
    defaultHexValue = ""


_TRPAdminPSFromCriteriaCommunity_Object = MibTableColumn
tRPAdminPSFromCriteriaCommunity = _TRPAdminPSFromCriteriaCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 12),
    _TRPAdminPSFromCriteriaCommunity_Type()
)
tRPAdminPSFromCriteriaCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaCommunity.setStatus("current")


class _TRPAdminPSFromCriteriaOrigin_Type(TPolicyEntryCriteriaOrigin):
    """Custom type tRPAdminPSFromCriteriaOrigin based on TPolicyEntryCriteriaOrigin"""


_TRPAdminPSFromCriteriaOrigin_Object = MibTableColumn
tRPAdminPSFromCriteriaOrigin = _TRPAdminPSFromCriteriaOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 13),
    _TRPAdminPSFromCriteriaOrigin_Type()
)
tRPAdminPSFromCriteriaOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaOrigin.setStatus("current")


class _TRPAdminPSFromCriteriaOspfRouteType_Type(TOspfRouteType):
    """Custom type tRPAdminPSFromCriteriaOspfRouteType based on TOspfRouteType"""
    defaultValue = 0


_TRPAdminPSFromCriteriaOspfRouteType_Object = MibTableColumn
tRPAdminPSFromCriteriaOspfRouteType = _TRPAdminPSFromCriteriaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 14),
    _TRPAdminPSFromCriteriaOspfRouteType_Type()
)
tRPAdminPSFromCriteriaOspfRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaOspfRouteType.setStatus("current")
_TRPAdminPSFromCriteriaArea_Type = IpAddress
_TRPAdminPSFromCriteriaArea_Object = MibTableColumn
tRPAdminPSFromCriteriaArea = _TRPAdminPSFromCriteriaArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 16),
    _TRPAdminPSFromCriteriaArea_Type()
)
tRPAdminPSFromCriteriaArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaArea.setStatus("current")
_TRPAdminPSFromCriteriaAreaConfigured_Type = TruthValue
_TRPAdminPSFromCriteriaAreaConfigured_Object = MibTableColumn
tRPAdminPSFromCriteriaAreaConfigured = _TRPAdminPSFromCriteriaAreaConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 17),
    _TRPAdminPSFromCriteriaAreaConfigured_Type()
)
tRPAdminPSFromCriteriaAreaConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaAreaConfigured.setStatus("current")


class _TRPAdminPSFromCriteriaIsisLevel_Type(TIsisLevel):
    """Custom type tRPAdminPSFromCriteriaIsisLevel based on TIsisLevel"""
    defaultValue = 0


_TRPAdminPSFromCriteriaIsisLevel_Object = MibTableColumn
tRPAdminPSFromCriteriaIsisLevel = _TRPAdminPSFromCriteriaIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 18),
    _TRPAdminPSFromCriteriaIsisLevel_Type()
)
tRPAdminPSFromCriteriaIsisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIsisLevel.setStatus("current")


class _TRPAdminPSFromCriteriaIsisExternal_Type(TruthValue):
    """Custom type tRPAdminPSFromCriteriaIsisExternal based on TruthValue"""


_TRPAdminPSFromCriteriaIsisExternal_Object = MibTableColumn
tRPAdminPSFromCriteriaIsisExternal = _TRPAdminPSFromCriteriaIsisExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 19),
    _TRPAdminPSFromCriteriaIsisExternal_Type()
)
tRPAdminPSFromCriteriaIsisExternal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIsisExternal.setStatus("current")
_TRPAdminPSFromCriteriaIgmpHostPrefixList_Type = TPrefixListName
_TRPAdminPSFromCriteriaIgmpHostPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaIgmpHostPrefixList = _TRPAdminPSFromCriteriaIgmpHostPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 20),
    _TRPAdminPSFromCriteriaIgmpHostPrefixList_Type()
)
tRPAdminPSFromCriteriaIgmpHostPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaIgmpHostPrefixList.setStatus("current")
_TRPAdminPSFromCriteriaGrpAddrPrefixList_Type = TPrefixListName
_TRPAdminPSFromCriteriaGrpAddrPrefixList_Object = MibTableColumn
tRPAdminPSFromCriteriaGrpAddrPrefixList = _TRPAdminPSFromCriteriaGrpAddrPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 21),
    _TRPAdminPSFromCriteriaGrpAddrPrefixList_Type()
)
tRPAdminPSFromCriteriaGrpAddrPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaGrpAddrPrefixList.setStatus("current")
_TRPAdminPSFromCriteriaSrcAddr_Type = IpAddress
_TRPAdminPSFromCriteriaSrcAddr_Object = MibTableColumn
tRPAdminPSFromCriteriaSrcAddr = _TRPAdminPSFromCriteriaSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 22),
    _TRPAdminPSFromCriteriaSrcAddr_Type()
)
tRPAdminPSFromCriteriaSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaSrcAddr.setStatus("current")
_TRPAdminPSFromCriteriaInterface_Type = TNamedItemOrEmpty
_TRPAdminPSFromCriteriaInterface_Object = MibTableColumn
tRPAdminPSFromCriteriaInterface = _TRPAdminPSFromCriteriaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 23),
    _TRPAdminPSFromCriteriaInterface_Type()
)
tRPAdminPSFromCriteriaInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaInterface.setStatus("current")


class _TRPAdminPSFromCriteriaTag_Type(TPolicyActionTag):
    """Custom type tRPAdminPSFromCriteriaTag based on TPolicyActionTag"""
    defaultValue = 0


_TRPAdminPSFromCriteriaTag_Object = MibTableColumn
tRPAdminPSFromCriteriaTag = _TRPAdminPSFromCriteriaTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 24),
    _TRPAdminPSFromCriteriaTag_Type()
)
tRPAdminPSFromCriteriaTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaTag.setStatus("current")
_TRPAdminPSFromCritNbrInetAddrType_Type = InetAddressType
_TRPAdminPSFromCritNbrInetAddrType_Object = MibTableColumn
tRPAdminPSFromCritNbrInetAddrType = _TRPAdminPSFromCritNbrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 25),
    _TRPAdminPSFromCritNbrInetAddrType_Type()
)
tRPAdminPSFromCritNbrInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritNbrInetAddrType.setStatus("current")
_TRPAdminPSFromCritNbrInetAddr_Type = InetAddress
_TRPAdminPSFromCritNbrInetAddr_Object = MibTableColumn
tRPAdminPSFromCritNbrInetAddr = _TRPAdminPSFromCritNbrInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 26),
    _TRPAdminPSFromCritNbrInetAddr_Type()
)
tRPAdminPSFromCritNbrInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritNbrInetAddr.setStatus("current")
_TRPAdminPSFromCritSrcInetAddrType_Type = InetAddressType
_TRPAdminPSFromCritSrcInetAddrType_Object = MibTableColumn
tRPAdminPSFromCritSrcInetAddrType = _TRPAdminPSFromCritSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 27),
    _TRPAdminPSFromCritSrcInetAddrType_Type()
)
tRPAdminPSFromCritSrcInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritSrcInetAddrType.setStatus("current")


class _TRPAdminPSFromCritSrcInetAddr_Type(InetAddress):
    """Custom type tRPAdminPSFromCritSrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TRPAdminPSFromCritSrcInetAddr_Type.__name__ = "InetAddress"
_TRPAdminPSFromCritSrcInetAddr_Object = MibTableColumn
tRPAdminPSFromCritSrcInetAddr = _TRPAdminPSFromCritSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 28),
    _TRPAdminPSFromCritSrcInetAddr_Type()
)
tRPAdminPSFromCritSrcInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritSrcInetAddr.setStatus("current")


class _TRPAdminPSFromCriteriaFamily_Type(TmnxBGPFamilyType):
    """Custom type tRPAdminPSFromCriteriaFamily based on TmnxBGPFamilyType"""
    defaultBinValue = "0"


_TRPAdminPSFromCriteriaFamily_Object = MibTableColumn
tRPAdminPSFromCriteriaFamily = _TRPAdminPSFromCriteriaFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 29),
    _TRPAdminPSFromCriteriaFamily_Type()
)
tRPAdminPSFromCriteriaFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaFamily.setStatus("current")


class _TRPAdminPSFromCriteriaInstanceId_Type(Unsigned32):
    """Custom type tRPAdminPSFromCriteriaInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TRPAdminPSFromCriteriaInstanceId_Type.__name__ = "Unsigned32"
_TRPAdminPSFromCriteriaInstanceId_Object = MibTableColumn
tRPAdminPSFromCriteriaInstanceId = _TRPAdminPSFromCriteriaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 30),
    _TRPAdminPSFromCriteriaInstanceId_Type()
)
tRPAdminPSFromCriteriaInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaInstanceId.setStatus("current")


class _TRPAdminPSFromCriteriaMatchTag_Type(TmnxEnabledDisabled):
    """Custom type tRPAdminPSFromCriteriaMatchTag based on TmnxEnabledDisabled"""


_TRPAdminPSFromCriteriaMatchTag_Object = MibTableColumn
tRPAdminPSFromCriteriaMatchTag = _TRPAdminPSFromCriteriaMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 31),
    _TRPAdminPSFromCriteriaMatchTag_Type()
)
tRPAdminPSFromCriteriaMatchTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaMatchTag.setStatus("current")


class _TRPAdminPSFromCriteriaState_Type(TPolicyEntryCriteriaState):
    """Custom type tRPAdminPSFromCriteriaState based on TPolicyEntryCriteriaState"""


_TRPAdminPSFromCriteriaState_Object = MibTableColumn
tRPAdminPSFromCriteriaState = _TRPAdminPSFromCriteriaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 32),
    _TRPAdminPSFromCriteriaState_Type()
)
tRPAdminPSFromCriteriaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCriteriaState.setStatus("current")
_TRPAdminPSFromCritASPathGroup_Type = TNamedItemOrEmpty
_TRPAdminPSFromCritASPathGroup_Object = MibTableColumn
tRPAdminPSFromCritASPathGroup = _TRPAdminPSFromCritASPathGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 10, 1, 33),
    _TRPAdminPSFromCritASPathGroup_Type()
)
tRPAdminPSFromCritASPathGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminPSFromCritASPathGroup.setStatus("current")
_TRPAdminInetPrefixListTable_Object = MibTable
tRPAdminInetPrefixListTable = _TRPAdminInetPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11)
)
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListTable.setStatus("current")
_TRPAdminInetPrefixListEntry_Object = MibTableRow
tRPAdminInetPrefixListEntry = _TRPAdminInetPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1)
)
tRPAdminInetPrefixListEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefixType"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefix"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListPrefixLen"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListType"),
)
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListEntry.setStatus("current")


class _TRPAdminInetPrefixListName_Type(TPrefixListName):
    """Custom type tRPAdminInetPrefixListName based on TPrefixListName"""
    subtypeSpec = TPrefixListName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminInetPrefixListName_Type.__name__ = "TPrefixListName"
_TRPAdminInetPrefixListName_Object = MibTableColumn
tRPAdminInetPrefixListName = _TRPAdminInetPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 1),
    _TRPAdminInetPrefixListName_Type()
)
tRPAdminInetPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListName.setStatus("current")
_TRPAdminInetPrefixListPrefixType_Type = InetAddressType
_TRPAdminInetPrefixListPrefixType_Object = MibTableColumn
tRPAdminInetPrefixListPrefixType = _TRPAdminInetPrefixListPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 2),
    _TRPAdminInetPrefixListPrefixType_Type()
)
tRPAdminInetPrefixListPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefixType.setStatus("current")
_TRPAdminInetPrefixListPrefix_Type = InetAddress
_TRPAdminInetPrefixListPrefix_Object = MibTableColumn
tRPAdminInetPrefixListPrefix = _TRPAdminInetPrefixListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 3),
    _TRPAdminInetPrefixListPrefix_Type()
)
tRPAdminInetPrefixListPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefix.setStatus("current")
_TRPAdminInetPrefixListPrefixLen_Type = InetAddressPrefixLength
_TRPAdminInetPrefixListPrefixLen_Object = MibTableColumn
tRPAdminInetPrefixListPrefixLen = _TRPAdminInetPrefixListPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 4),
    _TRPAdminInetPrefixListPrefixLen_Type()
)
tRPAdminInetPrefixListPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListPrefixLen.setStatus("current")


class _TRPAdminInetPrefixListType_Type(Integer32):
    """Custom type tRPAdminInetPrefixListType based on Integer32"""
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
        *(("exact", 1),
          ("longer", 2),
          ("range", 4),
          ("through", 3))
    )


_TRPAdminInetPrefixListType_Type.__name__ = "Integer32"
_TRPAdminInetPrefixListType_Object = MibTableColumn
tRPAdminInetPrefixListType = _TRPAdminInetPrefixListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 5),
    _TRPAdminInetPrefixListType_Type()
)
tRPAdminInetPrefixListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListType.setStatus("current")
_TRPAdminInetPrefixListRowStatus_Type = RowStatus
_TRPAdminInetPrefixListRowStatus_Object = MibTableColumn
tRPAdminInetPrefixListRowStatus = _TRPAdminInetPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 6),
    _TRPAdminInetPrefixListRowStatus_Type()
)
tRPAdminInetPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListRowStatus.setStatus("current")


class _TRPAdminInetPrefixListThroughLen_Type(InetAddressPrefixLength):
    """Custom type tRPAdminInetPrefixListThroughLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TRPAdminInetPrefixListThroughLen_Object = MibTableColumn
tRPAdminInetPrefixListThroughLen = _TRPAdminInetPrefixListThroughLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 7),
    _TRPAdminInetPrefixListThroughLen_Type()
)
tRPAdminInetPrefixListThroughLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListThroughLen.setStatus("current")


class _TRPAdminInetPrefixListBeginLen_Type(InetAddressPrefixLength):
    """Custom type tRPAdminInetPrefixListBeginLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TRPAdminInetPrefixListBeginLen_Object = MibTableColumn
tRPAdminInetPrefixListBeginLen = _TRPAdminInetPrefixListBeginLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 11, 1, 8),
    _TRPAdminInetPrefixListBeginLen_Type()
)
tRPAdminInetPrefixListBeginLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminInetPrefixListBeginLen.setStatus("current")
_TRPAdminCommunityExprTable_Object = MibTable
tRPAdminCommunityExprTable = _TRPAdminCommunityExprTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12)
)
if mibBuilder.loadTexts:
    tRPAdminCommunityExprTable.setStatus("current")
_TRPAdminCommunityExprEntry_Object = MibTableRow
tRPAdminCommunityExprEntry = _TRPAdminCommunityExprEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1)
)
tRPAdminCommunityExprEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprName"),
)
if mibBuilder.loadTexts:
    tRPAdminCommunityExprEntry.setStatus("current")


class _TRPAdminCommunityExprName_Type(TCommunityName):
    """Custom type tRPAdminCommunityExprName based on TCommunityName"""
    subtypeSpec = TCommunityName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminCommunityExprName_Type.__name__ = "TCommunityName"
_TRPAdminCommunityExprName_Object = MibTableColumn
tRPAdminCommunityExprName = _TRPAdminCommunityExprName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 1),
    _TRPAdminCommunityExprName_Type()
)
tRPAdminCommunityExprName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprName.setStatus("current")
_TRPAdminCommunityExprRowStatus_Type = RowStatus
_TRPAdminCommunityExprRowStatus_Object = MibTableColumn
tRPAdminCommunityExprRowStatus = _TRPAdminCommunityExprRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 2),
    _TRPAdminCommunityExprRowStatus_Type()
)
tRPAdminCommunityExprRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprRowStatus.setStatus("current")
_TRPAdminCommunityExprString1_Type = TCommunityExpression
_TRPAdminCommunityExprString1_Object = MibTableColumn
tRPAdminCommunityExprString1 = _TRPAdminCommunityExprString1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 3),
    _TRPAdminCommunityExprString1_Type()
)
tRPAdminCommunityExprString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString1.setStatus("current")
_TRPAdminCommunityExprString2_Type = TCommunityExpression
_TRPAdminCommunityExprString2_Object = MibTableColumn
tRPAdminCommunityExprString2 = _TRPAdminCommunityExprString2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 4),
    _TRPAdminCommunityExprString2_Type()
)
tRPAdminCommunityExprString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString2.setStatus("current")
_TRPAdminCommunityExprString3_Type = TCommunityExpression
_TRPAdminCommunityExprString3_Object = MibTableColumn
tRPAdminCommunityExprString3 = _TRPAdminCommunityExprString3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 5),
    _TRPAdminCommunityExprString3_Type()
)
tRPAdminCommunityExprString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString3.setStatus("current")
_TRPAdminCommunityExprString4_Type = TCommunityExpression
_TRPAdminCommunityExprString4_Object = MibTableColumn
tRPAdminCommunityExprString4 = _TRPAdminCommunityExprString4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 12, 1, 6),
    _TRPAdminCommunityExprString4_Type()
)
tRPAdminCommunityExprString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminCommunityExprString4.setStatus("current")
_TRPAdminASPathGroupTable_Object = MibTable
tRPAdminASPathGroupTable = _TRPAdminASPathGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13)
)
if mibBuilder.loadTexts:
    tRPAdminASPathGroupTable.setStatus("current")
_TRPAdminASPathGroupEntry_Object = MibTableRow
tRPAdminASPathGroupEntry = _TRPAdminASPathGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1)
)
tRPAdminASPathGroupEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupName"),
    (0, "TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupEntryIndex"),
)
if mibBuilder.loadTexts:
    tRPAdminASPathGroupEntry.setStatus("current")
_TRPAdminASPathGroupName_Type = TNamedItem
_TRPAdminASPathGroupName_Object = MibTableColumn
tRPAdminASPathGroupName = _TRPAdminASPathGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 1),
    _TRPAdminASPathGroupName_Type()
)
tRPAdminASPathGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupName.setStatus("current")


class _TRPAdminASPathGroupEntryIndex_Type(Unsigned32):
    """Custom type tRPAdminASPathGroupEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TRPAdminASPathGroupEntryIndex_Type.__name__ = "Unsigned32"
_TRPAdminASPathGroupEntryIndex_Object = MibTableColumn
tRPAdminASPathGroupEntryIndex = _TRPAdminASPathGroupEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 2),
    _TRPAdminASPathGroupEntryIndex_Type()
)
tRPAdminASPathGroupEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupEntryIndex.setStatus("current")
_TRPAdminASPathGroupRowStatus_Type = RowStatus
_TRPAdminASPathGroupRowStatus_Object = MibTableColumn
tRPAdminASPathGroupRowStatus = _TRPAdminASPathGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 3),
    _TRPAdminASPathGroupRowStatus_Type()
)
tRPAdminASPathGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupRowStatus.setStatus("current")


class _TRPAdminASPathGroupASPathName_Type(TASPathName):
    """Custom type tRPAdminASPathGroupASPathName based on TASPathName"""
    subtypeSpec = TASPathName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TRPAdminASPathGroupASPathName_Type.__name__ = "TASPathName"
_TRPAdminASPathGroupASPathName_Object = MibTableColumn
tRPAdminASPathGroupASPathName = _TRPAdminASPathGroupASPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 17, 2, 2, 13, 1, 4),
    _TRPAdminASPathGroupASPathName_Type()
)
tRPAdminASPathGroupASPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tRPAdminASPathGroupASPathName.setStatus("current")
_TRoutePolicyNotifyPrefix_ObjectIdentity = ObjectIdentity
tRoutePolicyNotifyPrefix = _TRoutePolicyNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 17)
)
_TRoutePolicyNotifications_ObjectIdentity = ObjectIdentity
tRoutePolicyNotifications = _TRoutePolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 17, 0)
)

# Managed Objects groups

tmnxRPAdminControlObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 1)
)
tmnxRPAdminControlObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminOwner"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminControlApply"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminLastSetTimer"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminLastSetTimeout"))
)
if mibBuilder.loadTexts:
    tmnxRPAdminControlObjectsGroup.setStatus("current")

tmnxRPASPathObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 2)
)
tmnxRPASPathObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRegEx"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathObjectsGroup.setStatus("obsolete")

tmnxRPCommunityObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 3)
)
tmnxRPCommunityObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRPCommunityObjectsGroup.setStatus("obsolete")

tmnxRPDampingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 4)
)
tmnxRPDampingObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingSuppress"))
)
if mibBuilder.loadTexts:
    tmnxRPDampingObjectsGroup.setStatus("obsolete")

tmnxRPPrefixListObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 5)
)
tmnxRPPrefixListObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListBeginLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListBeginLength"))
)
if mibBuilder.loadTexts:
    tmnxRPPrefixListObjectsGroup.setStatus("obsolete")

tmnxRPPolicyObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 9)
)
tmnxRPPolicyObjectsV4v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV4v0Group.setStatus("obsolete")

tmnxRPPolicyEntryObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 10)
)
tmnxRPPolicyEntryObjectsV4v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV4v0Group.setStatus("obsolete")

tmnxRPInetPrefixListObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 11)
)
tmnxRPInetPrefixListObjectsGroup.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListTblLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListBeginLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListBeginLen"))
)
if mibBuilder.loadTexts:
    tmnxRPInetPrefixListObjectsGroup.setStatus("obsolete")

tmnxRPPolicyEntryObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 12)
)
tmnxRPPolicyEntryObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV5v0Group.setStatus("obsolete")

tmnxRPPolicyObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 13)
)
tmnxRPPolicyObsoleteV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionParamsEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTableLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaEntryLastChanged"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListTblLastChg"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListLastChg"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObsoleteV5v0Group.setStatus("current")

tmnxRPASPathObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 14)
)
tmnxRPASPathObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathRegEx"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathRegEx"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathObjectsV5v0Group.setStatus("current")

tmnxRPCommunityObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 15)
)
tmnxRPCommunityObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxRPCommunityObjectsV5v0Group.setStatus("current")

tmnxRPDampingObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 16)
)
tmnxRPDampingObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperDampingSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingHalfLife"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingMaxSuppress"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingReuse"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminDampingSuppress"))
)
if mibBuilder.loadTexts:
    tmnxRPDampingObjectsV5v0Group.setStatus("current")

tmnxRPPrefixListObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 17)
)
tmnxRPPrefixListObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPrefixListBeginLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListThroughLength"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPrefixListBeginLength"))
)
if mibBuilder.loadTexts:
    tmnxRPPrefixListObjectsV5v0Group.setStatus("current")

tmnxRPPolicyObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 18)
)
tmnxRPPolicyObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV5v0Group.setStatus("obsolete")

tmnxRPInetPrefixListObjectsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 19)
)
tmnxRPInetPrefixListObjectsV5v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperInetPrefixListBeginLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListThroughLen"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminInetPrefixListBeginLen"))
)
if mibBuilder.loadTexts:
    tmnxRPInetPrefixListObjectsV5v0Group.setStatus("current")

tmnxRPPolicyObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 20)
)
tmnxRPPolicyObjectsV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPolicyStatementDefaultAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPnd"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPend"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV7v0Group.setStatus("current")

tmnxRPPolicyEntryObjectsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 21)
)
tmnxRPPolicyEntryObjectsV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaMatchTag"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV7v0Group.setStatus("obsolete")

tmnxRPPolicyObsoleteV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 22)
)
tmnxRPPolicyObsoleteV7v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefaultActionASPathPrependAS"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependAS"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObsoleteV7v0Group.setStatus("current")

tmnxRPPolicyObjectsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 25)
)
tmnxRPPolicyObjectsV8v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActMcRedirIfIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActMcRedirIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV8v0Group.setStatus("current")

tmnxRPQPPBV9v0R4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 26)
)
tmnxRPQPPBV9v0R4Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionFC"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionFCPriority"))
)
if mibBuilder.loadTexts:
    tmnxRPQPPBV9v0R4Group.setStatus("current")

tmnxRPPolicyEntryObjectsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 27)
)
tmnxRPPolicyEntryObjectsV9v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsDescription"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSParamsAction"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPrependCount"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunity2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionCommunityName2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreferenceSet"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionLocalPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionMetricValue"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionPreference"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionDamping"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHopSelf"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionOspfType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHopType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActInetNextHop"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSToCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaProtocol"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborIpAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaNeighborPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaPrefixList5"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaASPath"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaCommunity"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOrigin"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaOspfRouteType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaArea"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaAreaConfigured"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisLevel"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIsisExternal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaIgmpHostPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaGrpAddrPrefixList"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaSrcAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInterface"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritNbrInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddrType"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritSrcInetAddr"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaFamily"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaInstanceId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcceptActionASPathPend"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaMatchTag"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCriteriaState"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCriteriaState"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyEntryObjectsV9v0Group.setStatus("current")

tmnxRPPolicyObjectsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 30)
)
tmnxRPPolicyObjectsV9v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActMcRedirIfIndex"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActMcRedirSvcId"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActMcRedirIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV9v0Group.setStatus("current")

tmnxRPPolicyObjectsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 31)
)
tmnxRPPolicyObjectsV10v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionMetricSource"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSAcptActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSAcptActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprString4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperCommunityExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString1"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString2"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString3"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprString4"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminCommunityExprRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSDefActnAigpMetricVal"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActionAigpMetric"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSDefActnAigpMetricVal"))
)
if mibBuilder.loadTexts:
    tmnxRPPolicyObjectsV10v0Group.setStatus("current")

tmnxRPASPathGroupV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 2, 32)
)
tmnxRPASPathGroupV10v0Group.setObjects(
      *(("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperASPathGroupASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupRowStatus"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminASPathGroupASPathName"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPOperPSFromCritASPathGroup"),
        ("TIMETRA-ROUTE-POLICY-MIB", "tRPAdminPSFromCritASPathGroup"))
)
if mibBuilder.loadTexts:
    tmnxRPASPathGroupV10v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxRoutePolicy7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxRoutePolicy7750V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxRoutePolicy7750V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxRtPolicy7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxRtPolicy7450V10v0Compliance.setStatus(
        "current"
    )

tmnxRtPolicy7750V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 17, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxRtPolicy7750V10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ROUTE-POLICY-MIB",
    **{"TASPathName": TASPathName,
       "TCommunityName": TCommunityName,
       "TCommunityMember": TCommunityMember,
       "TCommunityExpression": TCommunityExpression,
       "TDampingName": TDampingName,
       "TPrefixListName": TPrefixListName,
       "TPolicyStatementName": TPolicyStatementName,
       "TRegularExpression": TRegularExpression,
       "TPolicyStatementEntryID": TPolicyStatementEntryID,
       "TRoutePolicyProtocol": TRoutePolicyProtocol,
       "TOspfRouteType": TOspfRouteType,
       "TIsisLevel": TIsisLevel,
       "TPolicyEntryAction": TPolicyEntryAction,
       "TPolicyEntryEdit": TPolicyEntryEdit,
       "TPolicyEntryCriteriaOrigin": TPolicyEntryCriteriaOrigin,
       "TPolicyActionTag": TPolicyActionTag,
       "TPolicyEntryCriteriaState": TPolicyEntryCriteriaState,
       "TPolicyActionMetricSource": TPolicyActionMetricSource,
       "TPolicyEntryAigpMetricEdit": TPolicyEntryAigpMetricEdit,
       "timetraRoutePolicyMIBModule": timetraRoutePolicyMIBModule,
       "tmnxRoutePolicyConformance": tmnxRoutePolicyConformance,
       "tmnxRoutePolicyCompliances": tmnxRoutePolicyCompliances,
       "tmnxRoutePolicy7450V4v0Compliance": tmnxRoutePolicy7450V4v0Compliance,
       "tmnxRoutePolicy7750V4v0Compliance": tmnxRoutePolicy7750V4v0Compliance,
       "tmnxRoutePolicy7450V5v0Compliance": tmnxRoutePolicy7450V5v0Compliance,
       "tmnxRoutePolicy7750V5v0Compliance": tmnxRoutePolicy7750V5v0Compliance,
       "tmnxRoutePolicy7450V7v0Compliance": tmnxRoutePolicy7450V7v0Compliance,
       "tmnxRoutePolicy7750V7v0Compliance": tmnxRoutePolicy7750V7v0Compliance,
       "tmnxRoutePolicy7450V8v0Compliance": tmnxRoutePolicy7450V8v0Compliance,
       "tmnxRoutePolicy7750V8v0Compliance": tmnxRoutePolicy7750V8v0Compliance,
       "tmnxRoutePolicy7450V9v0Compliance": tmnxRoutePolicy7450V9v0Compliance,
       "tmnxRoutePolicy7750V9v0Compliance": tmnxRoutePolicy7750V9v0Compliance,
       "tmnxRtPolicy7450V10v0Compliance": tmnxRtPolicy7450V10v0Compliance,
       "tmnxRtPolicy7750V10v0Compliance": tmnxRtPolicy7750V10v0Compliance,
       "tmnxRoutePolicyGroups": tmnxRoutePolicyGroups,
       "tmnxRPAdminControlObjectsGroup": tmnxRPAdminControlObjectsGroup,
       "tmnxRPASPathObjectsGroup": tmnxRPASPathObjectsGroup,
       "tmnxRPCommunityObjectsGroup": tmnxRPCommunityObjectsGroup,
       "tmnxRPDampingObjectsGroup": tmnxRPDampingObjectsGroup,
       "tmnxRPPrefixListObjectsGroup": tmnxRPPrefixListObjectsGroup,
       "tmnxRPPolicyObjectsV4v0Group": tmnxRPPolicyObjectsV4v0Group,
       "tmnxRPPolicyEntryObjectsV4v0Group": tmnxRPPolicyEntryObjectsV4v0Group,
       "tmnxRPInetPrefixListObjectsGroup": tmnxRPInetPrefixListObjectsGroup,
       "tmnxRPPolicyEntryObjectsV5v0Group": tmnxRPPolicyEntryObjectsV5v0Group,
       "tmnxRPPolicyObsoleteV5v0Group": tmnxRPPolicyObsoleteV5v0Group,
       "tmnxRPASPathObjectsV5v0Group": tmnxRPASPathObjectsV5v0Group,
       "tmnxRPCommunityObjectsV5v0Group": tmnxRPCommunityObjectsV5v0Group,
       "tmnxRPDampingObjectsV5v0Group": tmnxRPDampingObjectsV5v0Group,
       "tmnxRPPrefixListObjectsV5v0Group": tmnxRPPrefixListObjectsV5v0Group,
       "tmnxRPPolicyObjectsV5v0Group": tmnxRPPolicyObjectsV5v0Group,
       "tmnxRPInetPrefixListObjectsV5v0Group": tmnxRPInetPrefixListObjectsV5v0Group,
       "tmnxRPPolicyObjectsV7v0Group": tmnxRPPolicyObjectsV7v0Group,
       "tmnxRPPolicyEntryObjectsV7v0Group": tmnxRPPolicyEntryObjectsV7v0Group,
       "tmnxRPPolicyObsoleteV7v0Group": tmnxRPPolicyObsoleteV7v0Group,
       "tmnxRPPolicyObjectsV8v0Group": tmnxRPPolicyObjectsV8v0Group,
       "tmnxRPQPPBV9v0R4Group": tmnxRPQPPBV9v0R4Group,
       "tmnxRPPolicyEntryObjectsV9v0Group": tmnxRPPolicyEntryObjectsV9v0Group,
       "tmnxRPPolicyObjectsV9v0Group": tmnxRPPolicyObjectsV9v0Group,
       "tmnxRPPolicyObjectsV10v0Group": tmnxRPPolicyObjectsV10v0Group,
       "tmnxRPASPathGroupV10v0Group": tmnxRPASPathGroupV10v0Group,
       "tRoutePolicyObjects": tRoutePolicyObjects,
       "tRPOperObjects": tRPOperObjects,
       "tRPOperValueObjects": tRPOperValueObjects,
       "tRPOperASPathTableLastChanged": tRPOperASPathTableLastChanged,
       "tRPOperASPathTable": tRPOperASPathTable,
       "tRPOperASPathEntry": tRPOperASPathEntry,
       "tRPOperASPathName": tRPOperASPathName,
       "tRPOperASPathRowStatus": tRPOperASPathRowStatus,
       "tRPOperASPathRegEx": tRPOperASPathRegEx,
       "tRPOperASPathEntryLastChanged": tRPOperASPathEntryLastChanged,
       "tRPOperCommunityTableLastChanged": tRPOperCommunityTableLastChanged,
       "tRPOperCommunityTable": tRPOperCommunityTable,
       "tRPOperCommunityEntry": tRPOperCommunityEntry,
       "tRPOperCommunityName": tRPOperCommunityName,
       "tRPOperCommunityMember": tRPOperCommunityMember,
       "tRPOperCommunityRowStatus": tRPOperCommunityRowStatus,
       "tRPOperCommunityEntryLastChanged": tRPOperCommunityEntryLastChanged,
       "tRPOperDampingTableLastChanged": tRPOperDampingTableLastChanged,
       "tRPOperDampingTable": tRPOperDampingTable,
       "tRPOperDampingEntry": tRPOperDampingEntry,
       "tRPOperDampingName": tRPOperDampingName,
       "tRPOperDampingRowStatus": tRPOperDampingRowStatus,
       "tRPOperDampingHalfLife": tRPOperDampingHalfLife,
       "tRPOperDampingMaxSuppress": tRPOperDampingMaxSuppress,
       "tRPOperDampingReuse": tRPOperDampingReuse,
       "tRPOperDampingSuppress": tRPOperDampingSuppress,
       "tRPOperDampingEntryLastChanged": tRPOperDampingEntryLastChanged,
       "tRPOperPrefixListTableLastChanged": tRPOperPrefixListTableLastChanged,
       "tRPOperPrefixListTable": tRPOperPrefixListTable,
       "tRPOperPrefixListEntry": tRPOperPrefixListEntry,
       "tRPOperPrefixListName": tRPOperPrefixListName,
       "tRPOperPrefixListIpPrefix": tRPOperPrefixListIpPrefix,
       "tRPOperPrefixListMask": tRPOperPrefixListMask,
       "tRPOperPrefixListRowStatus": tRPOperPrefixListRowStatus,
       "tRPOperPrefixListType": tRPOperPrefixListType,
       "tRPOperPrefixListThroughLength": tRPOperPrefixListThroughLength,
       "tRPOperPrefixListEntryLastChanged": tRPOperPrefixListEntryLastChanged,
       "tRPOperPrefixListBeginLength": tRPOperPrefixListBeginLength,
       "tRPOperPolicyStatementTableLastChanged": tRPOperPolicyStatementTableLastChanged,
       "tRPOperPolicyStatementTable": tRPOperPolicyStatementTable,
       "tRPOperPolicyStatementEntry": tRPOperPolicyStatementEntry,
       "tRPOperPolicyStatementName": tRPOperPolicyStatementName,
       "tRPOperPolicyStatementRowStatus": tRPOperPolicyStatementRowStatus,
       "tRPOperPolicyStatementDescription": tRPOperPolicyStatementDescription,
       "tRPOperPolicyStatementDefaultAction": tRPOperPolicyStatementDefaultAction,
       "tRPOperPolicyStatementEntryLastChanged": tRPOperPolicyStatementEntryLastChanged,
       "tRPOperPSDefaultActionParamsTableLastChanged": tRPOperPSDefaultActionParamsTableLastChanged,
       "tRPOperPSDefaultActionParamsTable": tRPOperPSDefaultActionParamsTable,
       "tRPOperPSDefaultActionParamsEntry": tRPOperPSDefaultActionParamsEntry,
       "tRPOperPSDefaultActionASPath": tRPOperPSDefaultActionASPath,
       "tRPOperPSDefaultActionASPathName": tRPOperPSDefaultActionASPathName,
       "tRPOperPSDefaultActionASPathPrependAS": tRPOperPSDefaultActionASPathPrependAS,
       "tRPOperPSDefaultActionASPathPrependCount": tRPOperPSDefaultActionASPathPrependCount,
       "tRPOperPSDefaultActionCommunity1": tRPOperPSDefaultActionCommunity1,
       "tRPOperPSDefaultActionCommunityName1": tRPOperPSDefaultActionCommunityName1,
       "tRPOperPSDefaultActionCommunity2": tRPOperPSDefaultActionCommunity2,
       "tRPOperPSDefaultActionCommunityName2": tRPOperPSDefaultActionCommunityName2,
       "tRPOperPSDefaultActionOrigin": tRPOperPSDefaultActionOrigin,
       "tRPOperPSDefaultActionLocalPreferenceSet": tRPOperPSDefaultActionLocalPreferenceSet,
       "tRPOperPSDefaultActionLocalPreference": tRPOperPSDefaultActionLocalPreference,
       "tRPOperPSDefaultActionMetric": tRPOperPSDefaultActionMetric,
       "tRPOperPSDefaultActionMetricValue": tRPOperPSDefaultActionMetricValue,
       "tRPOperPSDefaultActionPreference": tRPOperPSDefaultActionPreference,
       "tRPOperPSDefaultActionDamping": tRPOperPSDefaultActionDamping,
       "tRPOperPSDefaultActionNextHopSelf": tRPOperPSDefaultActionNextHopSelf,
       "tRPOperPSDefaultActionNextHop": tRPOperPSDefaultActionNextHop,
       "tRPOperPSDefaultActionTag": tRPOperPSDefaultActionTag,
       "tRPOperPSDefaultActionOspfType": tRPOperPSDefaultActionOspfType,
       "tRPOperPSDefaultActionParamsEntryLastChanged": tRPOperPSDefaultActionParamsEntryLastChanged,
       "tRPOperPSDefActInetNextHopType": tRPOperPSDefActInetNextHopType,
       "tRPOperPSDefActInetNextHop": tRPOperPSDefActInetNextHop,
       "tRPOperPSDefaultActionASPathPend": tRPOperPSDefaultActionASPathPend,
       "tRPOperPSDefActMcRedirSvcId": tRPOperPSDefActMcRedirSvcId,
       "tRPOperPSDefActMcRedirIfIndex": tRPOperPSDefActMcRedirIfIndex,
       "tRPOperPSDefActionMetricSource": tRPOperPSDefActionMetricSource,
       "tRPOperPSDefActionAigpMetric": tRPOperPSDefActionAigpMetric,
       "tRPOperPSDefActnAigpMetricVal": tRPOperPSDefActnAigpMetricVal,
       "tRPOperPSParamsTableLastChanged": tRPOperPSParamsTableLastChanged,
       "tRPOperPSParamsTable": tRPOperPSParamsTable,
       "tRPOperPSParamsEntry": tRPOperPSParamsEntry,
       "tRPOperPSNameEntryIndex": tRPOperPSNameEntryIndex,
       "tRPOperPSParamsRowStatus": tRPOperPSParamsRowStatus,
       "tRPOperPSParamsDescription": tRPOperPSParamsDescription,
       "tRPOperPSParamsAction": tRPOperPSParamsAction,
       "tRPOperPSParamsEntryLastChanged": tRPOperPSParamsEntryLastChanged,
       "tRPOperPSAcceptActionParamsTableLastChanged": tRPOperPSAcceptActionParamsTableLastChanged,
       "tRPOperPSAcceptActionParamsTable": tRPOperPSAcceptActionParamsTable,
       "tRPOperPSAcceptActionParamsEntry": tRPOperPSAcceptActionParamsEntry,
       "tRPOperPSAcceptActionASPath": tRPOperPSAcceptActionASPath,
       "tRPOperPSAcceptActionASPathName": tRPOperPSAcceptActionASPathName,
       "tRPOperPSAcceptActionASPathPrependAS": tRPOperPSAcceptActionASPathPrependAS,
       "tRPOperPSAcceptActionASPathPrependCount": tRPOperPSAcceptActionASPathPrependCount,
       "tRPOperPSAcceptActionCommunity1": tRPOperPSAcceptActionCommunity1,
       "tRPOperPSAcceptActionCommunityName1": tRPOperPSAcceptActionCommunityName1,
       "tRPOperPSAcceptActionCommunity2": tRPOperPSAcceptActionCommunity2,
       "tRPOperPSAcceptActionCommunityName2": tRPOperPSAcceptActionCommunityName2,
       "tRPOperPSAcceptActionOrigin": tRPOperPSAcceptActionOrigin,
       "tRPOperPSAcceptActionLocalPreferenceSet": tRPOperPSAcceptActionLocalPreferenceSet,
       "tRPOperPSAcceptActionLocalPreference": tRPOperPSAcceptActionLocalPreference,
       "tRPOperPSAcceptActionMetric": tRPOperPSAcceptActionMetric,
       "tRPOperPSAcceptActionMetricValue": tRPOperPSAcceptActionMetricValue,
       "tRPOperPSAcceptActionPreference": tRPOperPSAcceptActionPreference,
       "tRPOperPSAcceptActionDamping": tRPOperPSAcceptActionDamping,
       "tRPOperPSAcceptActionNextHopSelf": tRPOperPSAcceptActionNextHopSelf,
       "tRPOperPSAcceptActionNextHop": tRPOperPSAcceptActionNextHop,
       "tRPOperPSAcceptActionTag": tRPOperPSAcceptActionTag,
       "tRPOperPSAcceptActionOspfType": tRPOperPSAcceptActionOspfType,
       "tRPOperPSAcceptActionParamsEntryLastChanged": tRPOperPSAcceptActionParamsEntryLastChanged,
       "tRPOperPSAcptActInetNextHopType": tRPOperPSAcptActInetNextHopType,
       "tRPOperPSAcptActInetNextHop": tRPOperPSAcptActInetNextHop,
       "tRPOperPSAcceptActionASPathPend": tRPOperPSAcceptActionASPathPend,
       "tRPOperPSAcptActMcRedirSvcId": tRPOperPSAcptActMcRedirSvcId,
       "tRPOperPSAcptActMcRedirIfIndex": tRPOperPSAcptActMcRedirIfIndex,
       "tRPOperPSAcptActnMetricSource": tRPOperPSAcptActnMetricSource,
       "tRPOperPSAcptActionAigpMetric": tRPOperPSAcptActionAigpMetric,
       "tRPOperPSAcptActnAigpMetricVal": tRPOperPSAcptActnAigpMetricVal,
       "tRPOperPSToCriteriaTableLastChanged": tRPOperPSToCriteriaTableLastChanged,
       "tRPOperPSToCriteriaTable": tRPOperPSToCriteriaTable,
       "tRPOperPSToCriteriaEntry": tRPOperPSToCriteriaEntry,
       "tRPOperPSToCriteriaIndex": tRPOperPSToCriteriaIndex,
       "tRPOperPSToCriteriaRowStatus": tRPOperPSToCriteriaRowStatus,
       "tRPOperPSToCriteriaProtocol": tRPOperPSToCriteriaProtocol,
       "tRPOperPSToCriteriaNeighborIpAddr": tRPOperPSToCriteriaNeighborIpAddr,
       "tRPOperPSToCriteriaNeighborPrefixList": tRPOperPSToCriteriaNeighborPrefixList,
       "tRPOperPSToCriteriaEntryLastChanged": tRPOperPSToCriteriaEntryLastChanged,
       "tRPOperPSToCriteriaIsisLevel": tRPOperPSToCriteriaIsisLevel,
       "tRPOperPSToCriteriaPrefixList1": tRPOperPSToCriteriaPrefixList1,
       "tRPOperPSToCriteriaPrefixList2": tRPOperPSToCriteriaPrefixList2,
       "tRPOperPSToCriteriaPrefixList3": tRPOperPSToCriteriaPrefixList3,
       "tRPOperPSToCriteriaPrefixList4": tRPOperPSToCriteriaPrefixList4,
       "tRPOperPSToCriteriaPrefixList5": tRPOperPSToCriteriaPrefixList5,
       "tRPOperPSToCritNbrInetAddrType": tRPOperPSToCritNbrInetAddrType,
       "tRPOperPSToCritNbrInetAddr": tRPOperPSToCritNbrInetAddr,
       "tRPOperPSToCriteriaInstanceId": tRPOperPSToCriteriaInstanceId,
       "tRPOperPSFromCriteriaTableLastChanged": tRPOperPSFromCriteriaTableLastChanged,
       "tRPOperPSFromCriteriaTable": tRPOperPSFromCriteriaTable,
       "tRPOperPSFromCriteriaEntry": tRPOperPSFromCriteriaEntry,
       "tRPOperPSFromCriteriaIndex": tRPOperPSFromCriteriaIndex,
       "tRPOperPSFromCriteriaRowStatus": tRPOperPSFromCriteriaRowStatus,
       "tRPOperPSFromCriteriaProtocol": tRPOperPSFromCriteriaProtocol,
       "tRPOperPSFromCriteriaNeighborIpAddr": tRPOperPSFromCriteriaNeighborIpAddr,
       "tRPOperPSFromCriteriaNeighborPrefixList": tRPOperPSFromCriteriaNeighborPrefixList,
       "tRPOperPSFromCriteriaPrefixList1": tRPOperPSFromCriteriaPrefixList1,
       "tRPOperPSFromCriteriaPrefixList2": tRPOperPSFromCriteriaPrefixList2,
       "tRPOperPSFromCriteriaPrefixList3": tRPOperPSFromCriteriaPrefixList3,
       "tRPOperPSFromCriteriaPrefixList4": tRPOperPSFromCriteriaPrefixList4,
       "tRPOperPSFromCriteriaPrefixList5": tRPOperPSFromCriteriaPrefixList5,
       "tRPOperPSFromCriteriaASPath": tRPOperPSFromCriteriaASPath,
       "tRPOperPSFromCriteriaCommunity": tRPOperPSFromCriteriaCommunity,
       "tRPOperPSFromCriteriaOrigin": tRPOperPSFromCriteriaOrigin,
       "tRPOperPSFromCriteriaOspfRouteType": tRPOperPSFromCriteriaOspfRouteType,
       "tRPOperPSFromCriteriaEntryLastChanged": tRPOperPSFromCriteriaEntryLastChanged,
       "tRPOperPSFromCriteriaArea": tRPOperPSFromCriteriaArea,
       "tRPOperPSFromCriteriaAreaConfigured": tRPOperPSFromCriteriaAreaConfigured,
       "tRPOperPSFromCriteriaIsisLevel": tRPOperPSFromCriteriaIsisLevel,
       "tRPOperPSFromCriteriaIsisExternal": tRPOperPSFromCriteriaIsisExternal,
       "tRPOperPSFromCriteriaIgmpHostPrefixList": tRPOperPSFromCriteriaIgmpHostPrefixList,
       "tRPOperPSFromCriteriaGrpAddrPrefixList": tRPOperPSFromCriteriaGrpAddrPrefixList,
       "tRPOperPSFromCriteriaSrcAddr": tRPOperPSFromCriteriaSrcAddr,
       "tRPOperPSFromCriteriaInterface": tRPOperPSFromCriteriaInterface,
       "tRPOperPSFromCriteriaTag": tRPOperPSFromCriteriaTag,
       "tRPOperPSFromCritNbrInetAddrType": tRPOperPSFromCritNbrInetAddrType,
       "tRPOperPSFromCritNbrInetAddr": tRPOperPSFromCritNbrInetAddr,
       "tRPOperPSFromCritSrcInetAddrType": tRPOperPSFromCritSrcInetAddrType,
       "tRPOperPSFromCritSrcInetAddr": tRPOperPSFromCritSrcInetAddr,
       "tRPOperPSFromCriteriaFamily": tRPOperPSFromCriteriaFamily,
       "tRPOperPSFromCriteriaInstanceId": tRPOperPSFromCriteriaInstanceId,
       "tRPOperPSFromCriteriaMatchTag": tRPOperPSFromCriteriaMatchTag,
       "tRPOperPSFromCriteriaState": tRPOperPSFromCriteriaState,
       "tRPOperPSFromCritASPathGroup": tRPOperPSFromCritASPathGroup,
       "tRPOperInetPrefixListTblLastChg": tRPOperInetPrefixListTblLastChg,
       "tRPOperInetPrefixListTable": tRPOperInetPrefixListTable,
       "tRPOperInetPrefixListEntry": tRPOperInetPrefixListEntry,
       "tRPOperInetPrefixListName": tRPOperInetPrefixListName,
       "tRPOperInetPrefixListPrefixType": tRPOperInetPrefixListPrefixType,
       "tRPOperInetPrefixListPrefix": tRPOperInetPrefixListPrefix,
       "tRPOperInetPrefixListPrefixLen": tRPOperInetPrefixListPrefixLen,
       "tRPOperInetPrefixListType": tRPOperInetPrefixListType,
       "tRPOperInetPrefixListRowStatus": tRPOperInetPrefixListRowStatus,
       "tRPOperInetPrefixListThroughLen": tRPOperInetPrefixListThroughLen,
       "tRPOperInetPrefixListLastChg": tRPOperInetPrefixListLastChg,
       "tRPOperInetPrefixListBeginLen": tRPOperInetPrefixListBeginLen,
       "tRPOperCommunityExprTable": tRPOperCommunityExprTable,
       "tRPOperCommunityExprEntry": tRPOperCommunityExprEntry,
       "tRPOperCommunityExprName": tRPOperCommunityExprName,
       "tRPOperCommunityExprRowStatus": tRPOperCommunityExprRowStatus,
       "tRPOperCommunityExprString1": tRPOperCommunityExprString1,
       "tRPOperCommunityExprString2": tRPOperCommunityExprString2,
       "tRPOperCommunityExprString3": tRPOperCommunityExprString3,
       "tRPOperCommunityExprString4": tRPOperCommunityExprString4,
       "tRPOperASPathGroupTable": tRPOperASPathGroupTable,
       "tRPOperASPathGroupEntry": tRPOperASPathGroupEntry,
       "tRPOperASPathGroupName": tRPOperASPathGroupName,
       "tRPOperASPathGroupEntryIndex": tRPOperASPathGroupEntryIndex,
       "tRPOperASPathGroupRowStatus": tRPOperASPathGroupRowStatus,
       "tRPOperASPathGroupASPathName": tRPOperASPathGroupASPathName,
       "tRPAdminObjects": tRPAdminObjects,
       "tRPAdminControlObjects": tRPAdminControlObjects,
       "tRPAdminOwner": tRPAdminOwner,
       "tRPAdminControlApply": tRPAdminControlApply,
       "tRPAdminLastSetTimer": tRPAdminLastSetTimer,
       "tRPAdminLastSetTimeout": tRPAdminLastSetTimeout,
       "tRPAdminValueObjects": tRPAdminValueObjects,
       "tRPAdminASPathTable": tRPAdminASPathTable,
       "tRPAdminASPathEntry": tRPAdminASPathEntry,
       "tRPAdminASPathName": tRPAdminASPathName,
       "tRPAdminASPathRowStatus": tRPAdminASPathRowStatus,
       "tRPAdminASPathRegEx": tRPAdminASPathRegEx,
       "tRPAdminCommunityTable": tRPAdminCommunityTable,
       "tRPAdminCommunityEntry": tRPAdminCommunityEntry,
       "tRPAdminCommunityName": tRPAdminCommunityName,
       "tRPAdminCommunityMember": tRPAdminCommunityMember,
       "tRPAdminCommunityRowStatus": tRPAdminCommunityRowStatus,
       "tRPAdminDampingTable": tRPAdminDampingTable,
       "tRPAdminDampingEntry": tRPAdminDampingEntry,
       "tRPAdminDampingName": tRPAdminDampingName,
       "tRPAdminDampingRowStatus": tRPAdminDampingRowStatus,
       "tRPAdminDampingHalfLife": tRPAdminDampingHalfLife,
       "tRPAdminDampingMaxSuppress": tRPAdminDampingMaxSuppress,
       "tRPAdminDampingReuse": tRPAdminDampingReuse,
       "tRPAdminDampingSuppress": tRPAdminDampingSuppress,
       "tRPAdminPrefixListTable": tRPAdminPrefixListTable,
       "tRPAdminPrefixListEntry": tRPAdminPrefixListEntry,
       "tRPAdminPrefixListName": tRPAdminPrefixListName,
       "tRPAdminPrefixListIpPrefix": tRPAdminPrefixListIpPrefix,
       "tRPAdminPrefixListMask": tRPAdminPrefixListMask,
       "tRPAdminPrefixListRowStatus": tRPAdminPrefixListRowStatus,
       "tRPAdminPrefixListType": tRPAdminPrefixListType,
       "tRPAdminPrefixListThroughLength": tRPAdminPrefixListThroughLength,
       "tRPAdminPrefixListBeginLength": tRPAdminPrefixListBeginLength,
       "tRPAdminPolicyStatementTable": tRPAdminPolicyStatementTable,
       "tRPAdminPolicyStatementEntry": tRPAdminPolicyStatementEntry,
       "tRPAdminPolicyStatementName": tRPAdminPolicyStatementName,
       "tRPAdminPolicyStatementRowStatus": tRPAdminPolicyStatementRowStatus,
       "tRPAdminPolicyStatementDescription": tRPAdminPolicyStatementDescription,
       "tRPAdminPolicyStatementDefaultAction": tRPAdminPolicyStatementDefaultAction,
       "tRPAdminPSDefaultActionParamsTable": tRPAdminPSDefaultActionParamsTable,
       "tRPAdminPSDefaultActionParamsEntry": tRPAdminPSDefaultActionParamsEntry,
       "tRPAdminPSDefaultActionASPath": tRPAdminPSDefaultActionASPath,
       "tRPAdminPSDefaultActionASPathName": tRPAdminPSDefaultActionASPathName,
       "tRPAdminPSDefaultActionASPathPrependAS": tRPAdminPSDefaultActionASPathPrependAS,
       "tRPAdminPSDefaultActionASPathPrependCount": tRPAdminPSDefaultActionASPathPrependCount,
       "tRPAdminPSDefaultActionCommunity1": tRPAdminPSDefaultActionCommunity1,
       "tRPAdminPSDefaultActionCommunityName1": tRPAdminPSDefaultActionCommunityName1,
       "tRPAdminPSDefaultActionCommunity2": tRPAdminPSDefaultActionCommunity2,
       "tRPAdminPSDefaultActionCommunityName2": tRPAdminPSDefaultActionCommunityName2,
       "tRPAdminPSDefaultActionOrigin": tRPAdminPSDefaultActionOrigin,
       "tRPAdminPSDefaultActionLocalPreferenceSet": tRPAdminPSDefaultActionLocalPreferenceSet,
       "tRPAdminPSDefaultActionLocalPreference": tRPAdminPSDefaultActionLocalPreference,
       "tRPAdminPSDefaultActionMetric": tRPAdminPSDefaultActionMetric,
       "tRPAdminPSDefaultActionMetricValue": tRPAdminPSDefaultActionMetricValue,
       "tRPAdminPSDefaultActionPreference": tRPAdminPSDefaultActionPreference,
       "tRPAdminPSDefaultActionDamping": tRPAdminPSDefaultActionDamping,
       "tRPAdminPSDefaultActionNextHopSelf": tRPAdminPSDefaultActionNextHopSelf,
       "tRPAdminPSDefaultActionNextHop": tRPAdminPSDefaultActionNextHop,
       "tRPAdminPSDefaultActionTag": tRPAdminPSDefaultActionTag,
       "tRPAdminPSDefaultActionOspfType": tRPAdminPSDefaultActionOspfType,
       "tRPAdminPSDefActInetNextHopType": tRPAdminPSDefActInetNextHopType,
       "tRPAdminPSDefActInetNextHop": tRPAdminPSDefActInetNextHop,
       "tRPAdminPSDefaultActionASPathPnd": tRPAdminPSDefaultActionASPathPnd,
       "tRPAdminPSDefActMcRedirSvcId": tRPAdminPSDefActMcRedirSvcId,
       "tRPAdminPSDefActMcRedirIfIndex": tRPAdminPSDefActMcRedirIfIndex,
       "tRPAdminPSDefActionMetricSource": tRPAdminPSDefActionMetricSource,
       "tRPAdminPSDefActionAigpMetric": tRPAdminPSDefActionAigpMetric,
       "tRPAdminPSDefActnAigpMetricVal": tRPAdminPSDefActnAigpMetricVal,
       "tRPAdminPSParamsTable": tRPAdminPSParamsTable,
       "tRPAdminPSParamsEntry": tRPAdminPSParamsEntry,
       "tRPAdminPSNameEntryIndex": tRPAdminPSNameEntryIndex,
       "tRPAdminPSParamsRowStatus": tRPAdminPSParamsRowStatus,
       "tRPAdminPSParamsDescription": tRPAdminPSParamsDescription,
       "tRPAdminPSParamsAction": tRPAdminPSParamsAction,
       "tRPAdminPSAcceptActionParamsTable": tRPAdminPSAcceptActionParamsTable,
       "tRPAdminPSAcceptActionParamsEntry": tRPAdminPSAcceptActionParamsEntry,
       "tRPAdminPSAcceptActionASPath": tRPAdminPSAcceptActionASPath,
       "tRPAdminPSAcceptActionASPathName": tRPAdminPSAcceptActionASPathName,
       "tRPAdminPSAcceptActionASPathPrependAS": tRPAdminPSAcceptActionASPathPrependAS,
       "tRPAdminPSAcceptActionASPathPrependCount": tRPAdminPSAcceptActionASPathPrependCount,
       "tRPAdminPSAcceptActionCommunity1": tRPAdminPSAcceptActionCommunity1,
       "tRPAdminPSAcceptActionCommunityName1": tRPAdminPSAcceptActionCommunityName1,
       "tRPAdminPSAcceptActionCommunity2": tRPAdminPSAcceptActionCommunity2,
       "tRPAdminPSAcceptActionCommunityName2": tRPAdminPSAcceptActionCommunityName2,
       "tRPAdminPSAcceptActionOrigin": tRPAdminPSAcceptActionOrigin,
       "tRPAdminPSAcceptActionLocalPreferenceSet": tRPAdminPSAcceptActionLocalPreferenceSet,
       "tRPAdminPSAcceptActionLocalPreference": tRPAdminPSAcceptActionLocalPreference,
       "tRPAdminPSAcceptActionMetric": tRPAdminPSAcceptActionMetric,
       "tRPAdminPSAcceptActionMetricValue": tRPAdminPSAcceptActionMetricValue,
       "tRPAdminPSAcceptActionPreference": tRPAdminPSAcceptActionPreference,
       "tRPAdminPSAcceptActionDamping": tRPAdminPSAcceptActionDamping,
       "tRPAdminPSAcceptActionNextHopSelf": tRPAdminPSAcceptActionNextHopSelf,
       "tRPAdminPSAcceptActionNextHop": tRPAdminPSAcceptActionNextHop,
       "tRPAdminPSAcceptActionTag": tRPAdminPSAcceptActionTag,
       "tRPAdminPSAcceptActionOspfType": tRPAdminPSAcceptActionOspfType,
       "tRPAdminPSAcptActInetNextHopType": tRPAdminPSAcptActInetNextHopType,
       "tRPAdminPSAcptActInetNextHop": tRPAdminPSAcptActInetNextHop,
       "tRPAdminPSAcceptActionASPathPend": tRPAdminPSAcceptActionASPathPend,
       "tRPAdminPSAcceptActionFC": tRPAdminPSAcceptActionFC,
       "tRPAdminPSAcceptActionFCPriority": tRPAdminPSAcceptActionFCPriority,
       "tRPAdminPSAcptActMcRedirSvcId": tRPAdminPSAcptActMcRedirSvcId,
       "tRPAdminPSAcptActMcRedirIfIndex": tRPAdminPSAcptActMcRedirIfIndex,
       "tRPAdminPSAcptActnMetricSource": tRPAdminPSAcptActnMetricSource,
       "tRPAdminPSAcptActionAigpMetric": tRPAdminPSAcptActionAigpMetric,
       "tRPAdminPSAcptActnAigpMetricVal": tRPAdminPSAcptActnAigpMetricVal,
       "tRPAdminPSToCriteriaTable": tRPAdminPSToCriteriaTable,
       "tRPAdminPSToCriteriaEntry": tRPAdminPSToCriteriaEntry,
       "tRPAdminPSToCriteriaIndex": tRPAdminPSToCriteriaIndex,
       "tRPAdminPSToCriteriaRowStatus": tRPAdminPSToCriteriaRowStatus,
       "tRPAdminPSToCriteriaProtocol": tRPAdminPSToCriteriaProtocol,
       "tRPAdminPSToCriteriaNeighborIpAddr": tRPAdminPSToCriteriaNeighborIpAddr,
       "tRPAdminPSToCriteriaNeighborPrefixList": tRPAdminPSToCriteriaNeighborPrefixList,
       "tRPAdminPSToCriteriaIsisLevel": tRPAdminPSToCriteriaIsisLevel,
       "tRPAdminPSToCriteriaPrefixList1": tRPAdminPSToCriteriaPrefixList1,
       "tRPAdminPSToCriteriaPrefixList2": tRPAdminPSToCriteriaPrefixList2,
       "tRPAdminPSToCriteriaPrefixList3": tRPAdminPSToCriteriaPrefixList3,
       "tRPAdminPSToCriteriaPrefixList4": tRPAdminPSToCriteriaPrefixList4,
       "tRPAdminPSToCriteriaPrefixList5": tRPAdminPSToCriteriaPrefixList5,
       "tRPAdminPSToCritNbrInetAddrType": tRPAdminPSToCritNbrInetAddrType,
       "tRPAdminPSToCritNbrInetAddr": tRPAdminPSToCritNbrInetAddr,
       "tRPAdminPSToCriteriaInstanceId": tRPAdminPSToCriteriaInstanceId,
       "tRPAdminPSFromCriteriaTable": tRPAdminPSFromCriteriaTable,
       "tRPAdminPSFromCriteriaEntry": tRPAdminPSFromCriteriaEntry,
       "tRPAdminPSFromCriteriaIndex": tRPAdminPSFromCriteriaIndex,
       "tRPAdminPSFromCriteriaRowStatus": tRPAdminPSFromCriteriaRowStatus,
       "tRPAdminPSFromCriteriaProtocol": tRPAdminPSFromCriteriaProtocol,
       "tRPAdminPSFromCriteriaNeighborIpAddr": tRPAdminPSFromCriteriaNeighborIpAddr,
       "tRPAdminPSFromCriteriaNeighborPrefixList": tRPAdminPSFromCriteriaNeighborPrefixList,
       "tRPAdminPSFromCriteriaPrefixList1": tRPAdminPSFromCriteriaPrefixList1,
       "tRPAdminPSFromCriteriaPrefixList2": tRPAdminPSFromCriteriaPrefixList2,
       "tRPAdminPSFromCriteriaPrefixList3": tRPAdminPSFromCriteriaPrefixList3,
       "tRPAdminPSFromCriteriaPrefixList4": tRPAdminPSFromCriteriaPrefixList4,
       "tRPAdminPSFromCriteriaPrefixList5": tRPAdminPSFromCriteriaPrefixList5,
       "tRPAdminPSFromCriteriaASPath": tRPAdminPSFromCriteriaASPath,
       "tRPAdminPSFromCriteriaCommunity": tRPAdminPSFromCriteriaCommunity,
       "tRPAdminPSFromCriteriaOrigin": tRPAdminPSFromCriteriaOrigin,
       "tRPAdminPSFromCriteriaOspfRouteType": tRPAdminPSFromCriteriaOspfRouteType,
       "tRPAdminPSFromCriteriaArea": tRPAdminPSFromCriteriaArea,
       "tRPAdminPSFromCriteriaAreaConfigured": tRPAdminPSFromCriteriaAreaConfigured,
       "tRPAdminPSFromCriteriaIsisLevel": tRPAdminPSFromCriteriaIsisLevel,
       "tRPAdminPSFromCriteriaIsisExternal": tRPAdminPSFromCriteriaIsisExternal,
       "tRPAdminPSFromCriteriaIgmpHostPrefixList": tRPAdminPSFromCriteriaIgmpHostPrefixList,
       "tRPAdminPSFromCriteriaGrpAddrPrefixList": tRPAdminPSFromCriteriaGrpAddrPrefixList,
       "tRPAdminPSFromCriteriaSrcAddr": tRPAdminPSFromCriteriaSrcAddr,
       "tRPAdminPSFromCriteriaInterface": tRPAdminPSFromCriteriaInterface,
       "tRPAdminPSFromCriteriaTag": tRPAdminPSFromCriteriaTag,
       "tRPAdminPSFromCritNbrInetAddrType": tRPAdminPSFromCritNbrInetAddrType,
       "tRPAdminPSFromCritNbrInetAddr": tRPAdminPSFromCritNbrInetAddr,
       "tRPAdminPSFromCritSrcInetAddrType": tRPAdminPSFromCritSrcInetAddrType,
       "tRPAdminPSFromCritSrcInetAddr": tRPAdminPSFromCritSrcInetAddr,
       "tRPAdminPSFromCriteriaFamily": tRPAdminPSFromCriteriaFamily,
       "tRPAdminPSFromCriteriaInstanceId": tRPAdminPSFromCriteriaInstanceId,
       "tRPAdminPSFromCriteriaMatchTag": tRPAdminPSFromCriteriaMatchTag,
       "tRPAdminPSFromCriteriaState": tRPAdminPSFromCriteriaState,
       "tRPAdminPSFromCritASPathGroup": tRPAdminPSFromCritASPathGroup,
       "tRPAdminInetPrefixListTable": tRPAdminInetPrefixListTable,
       "tRPAdminInetPrefixListEntry": tRPAdminInetPrefixListEntry,
       "tRPAdminInetPrefixListName": tRPAdminInetPrefixListName,
       "tRPAdminInetPrefixListPrefixType": tRPAdminInetPrefixListPrefixType,
       "tRPAdminInetPrefixListPrefix": tRPAdminInetPrefixListPrefix,
       "tRPAdminInetPrefixListPrefixLen": tRPAdminInetPrefixListPrefixLen,
       "tRPAdminInetPrefixListType": tRPAdminInetPrefixListType,
       "tRPAdminInetPrefixListRowStatus": tRPAdminInetPrefixListRowStatus,
       "tRPAdminInetPrefixListThroughLen": tRPAdminInetPrefixListThroughLen,
       "tRPAdminInetPrefixListBeginLen": tRPAdminInetPrefixListBeginLen,
       "tRPAdminCommunityExprTable": tRPAdminCommunityExprTable,
       "tRPAdminCommunityExprEntry": tRPAdminCommunityExprEntry,
       "tRPAdminCommunityExprName": tRPAdminCommunityExprName,
       "tRPAdminCommunityExprRowStatus": tRPAdminCommunityExprRowStatus,
       "tRPAdminCommunityExprString1": tRPAdminCommunityExprString1,
       "tRPAdminCommunityExprString2": tRPAdminCommunityExprString2,
       "tRPAdminCommunityExprString3": tRPAdminCommunityExprString3,
       "tRPAdminCommunityExprString4": tRPAdminCommunityExprString4,
       "tRPAdminASPathGroupTable": tRPAdminASPathGroupTable,
       "tRPAdminASPathGroupEntry": tRPAdminASPathGroupEntry,
       "tRPAdminASPathGroupName": tRPAdminASPathGroupName,
       "tRPAdminASPathGroupEntryIndex": tRPAdminASPathGroupEntryIndex,
       "tRPAdminASPathGroupRowStatus": tRPAdminASPathGroupRowStatus,
       "tRPAdminASPathGroupASPathName": tRPAdminASPathGroupASPathName,
       "tRoutePolicyNotifyPrefix": tRoutePolicyNotifyPrefix,
       "tRoutePolicyNotifications": tRoutePolicyNotifications}
)
