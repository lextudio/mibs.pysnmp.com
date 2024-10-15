# SNMP MIB module (PNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:04 2024
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

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmTrafficDescrParamIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 enterprises,
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "zeroDotZero")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pnniMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1)
)
pnniMIB.setRevisions(
        ("2002-04-24 00:00",
         "1997-03-01 00:00",
         "1996-02-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PnniAtmAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )



class PnniNodeIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PnniNodeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )



class PnniPortId(Unsigned32, TextualConvention):
    status = "current"


class PnniAggrToken(Unsigned32, TextualConvention):
    status = "current"


class PnniPeerGroupId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )



class PnniLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )



class PnniSvccRccIndex(Integer32, TextualConvention):
    status = "current"


class AtmAddrPrefix(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )



class PnniPrefixLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )



class PnniMetricsTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ServiceCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )



class ClpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clpEqual0", 1),
          ("clpEqual0Or1", 2))
    )



class TnsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("nationalNetworkIdentification", 2),
          ("other", 8))
    )



class TnsPlan(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("carrierIdentificationCode", 1),
          ("other", 16))
    )



class PnniVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version1point0", 2))
    )



class PnniHelloState(Integer32, TextualConvention):
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
        *(("attempt", 3),
          ("commonOutside", 8),
          ("down", 2),
          ("notApplicable", 1),
          ("oneWayInside", 4),
          ("oneWayOutside", 6),
          ("twoWayInside", 5),
          ("twoWayOutside", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfPnni_ObjectIdentity = ObjectIdentity
atmfPnni = _AtmfPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4)
)
_PnniMIBObjects_ObjectIdentity = ObjectIdentity
pnniMIBObjects = _PnniMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1)
)
_PnniBaseGroup_ObjectIdentity = ObjectIdentity
pnniBaseGroup = _PnniBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1)
)
_PnniHighestVersion_Type = PnniVersion
_PnniHighestVersion_Object = MibScalar
pnniHighestVersion = _PnniHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 1),
    _PnniHighestVersion_Type()
)
pnniHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniHighestVersion.setStatus("current")
_PnniLowestVersion_Type = PnniVersion
_PnniLowestVersion_Object = MibScalar
pnniLowestVersion = _PnniLowestVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 2),
    _PnniLowestVersion_Type()
)
pnniLowestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLowestVersion.setStatus("current")
_PnniDtlCountOriginator_Type = Counter32
_PnniDtlCountOriginator_Object = MibScalar
pnniDtlCountOriginator = _PnniDtlCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 3),
    _PnniDtlCountOriginator_Type()
)
pnniDtlCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDtlCountOriginator.setStatus("current")
_PnniDtlCountBorder_Type = Counter32
_PnniDtlCountBorder_Object = MibScalar
pnniDtlCountBorder = _PnniDtlCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 4),
    _PnniDtlCountBorder_Type()
)
pnniDtlCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDtlCountBorder.setStatus("current")
_PnniCrankbackCountOriginator_Type = Counter32
_PnniCrankbackCountOriginator_Object = MibScalar
pnniCrankbackCountOriginator = _PnniCrankbackCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 5),
    _PnniCrankbackCountOriginator_Type()
)
pnniCrankbackCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniCrankbackCountOriginator.setStatus("current")
_PnniCrankbackCountBorder_Type = Counter32
_PnniCrankbackCountBorder_Object = MibScalar
pnniCrankbackCountBorder = _PnniCrankbackCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 6),
    _PnniCrankbackCountBorder_Type()
)
pnniCrankbackCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniCrankbackCountBorder.setStatus("current")
_PnniAltRouteCountOriginator_Type = Counter32
_PnniAltRouteCountOriginator_Object = MibScalar
pnniAltRouteCountOriginator = _PnniAltRouteCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 7),
    _PnniAltRouteCountOriginator_Type()
)
pnniAltRouteCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniAltRouteCountOriginator.setStatus("current")
_PnniAltRouteCountBorder_Type = Counter32
_PnniAltRouteCountBorder_Object = MibScalar
pnniAltRouteCountBorder = _PnniAltRouteCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 8),
    _PnniAltRouteCountBorder_Type()
)
pnniAltRouteCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniAltRouteCountBorder.setStatus("current")
_PnniRouteFailCountOriginator_Type = Counter32
_PnniRouteFailCountOriginator_Object = MibScalar
pnniRouteFailCountOriginator = _PnniRouteFailCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 9),
    _PnniRouteFailCountOriginator_Type()
)
pnniRouteFailCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteFailCountOriginator.setStatus("current")
_PnniRouteFailCountBorder_Type = Counter32
_PnniRouteFailCountBorder_Object = MibScalar
pnniRouteFailCountBorder = _PnniRouteFailCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 10),
    _PnniRouteFailCountBorder_Type()
)
pnniRouteFailCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteFailCountBorder.setStatus("current")
_PnniRouteFailUnreachableOriginator_Type = Counter32
_PnniRouteFailUnreachableOriginator_Object = MibScalar
pnniRouteFailUnreachableOriginator = _PnniRouteFailUnreachableOriginator_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 11),
    _PnniRouteFailUnreachableOriginator_Type()
)
pnniRouteFailUnreachableOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteFailUnreachableOriginator.setStatus("current")
_PnniRouteFailUnreachableBorder_Type = Counter32
_PnniRouteFailUnreachableBorder_Object = MibScalar
pnniRouteFailUnreachableBorder = _PnniRouteFailUnreachableBorder_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 1, 12),
    _PnniRouteFailUnreachableBorder_Type()
)
pnniRouteFailUnreachableBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteFailUnreachableBorder.setStatus("current")
_PnniNodeTable_Object = MibTable
pnniNodeTable = _PnniNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pnniNodeTable.setStatus("current")
_PnniNodeEntry_Object = MibTableRow
pnniNodeEntry = _PnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1)
)
pnniNodeEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
)
if mibBuilder.loadTexts:
    pnniNodeEntry.setStatus("current")
_PnniNodeIndex_Type = PnniNodeIndex
_PnniNodeIndex_Object = MibTableColumn
pnniNodeIndex = _PnniNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 1),
    _PnniNodeIndex_Type()
)
pnniNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniNodeIndex.setStatus("current")


class _PnniNodeLevel_Type(PnniLevel):
    """Custom type pnniNodeLevel based on PnniLevel"""
    defaultValue = 96


_PnniNodeLevel_Object = MibTableColumn
pnniNodeLevel = _PnniNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 2),
    _PnniNodeLevel_Type()
)
pnniNodeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeLevel.setStatus("current")
_PnniNodeId_Type = PnniNodeId
_PnniNodeId_Object = MibTableColumn
pnniNodeId = _PnniNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 3),
    _PnniNodeId_Type()
)
pnniNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeId.setStatus("current")


class _PnniNodeLowest_Type(TruthValue):
    """Custom type pnniNodeLowest based on TruthValue"""


_PnniNodeLowest_Object = MibTableColumn
pnniNodeLowest = _PnniNodeLowest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 4),
    _PnniNodeLowest_Type()
)
pnniNodeLowest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeLowest.setStatus("current")


class _PnniNodeAdminStatus_Type(Integer32):
    """Custom type pnniNodeAdminStatus based on Integer32"""
    defaultValue = 1

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


_PnniNodeAdminStatus_Type.__name__ = "Integer32"
_PnniNodeAdminStatus_Object = MibTableColumn
pnniNodeAdminStatus = _PnniNodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 5),
    _PnniNodeAdminStatus_Type()
)
pnniNodeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeAdminStatus.setStatus("current")


class _PnniNodeOperStatus_Type(Integer32):
    """Custom type pnniNodeOperStatus based on Integer32"""
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


_PnniNodeOperStatus_Type.__name__ = "Integer32"
_PnniNodeOperStatus_Object = MibTableColumn
pnniNodeOperStatus = _PnniNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 6),
    _PnniNodeOperStatus_Type()
)
pnniNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeOperStatus.setStatus("current")
_PnniNodeDomainName_Type = DisplayString
_PnniNodeDomainName_Object = MibTableColumn
pnniNodeDomainName = _PnniNodeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 7),
    _PnniNodeDomainName_Type()
)
pnniNodeDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeDomainName.setStatus("current")
_PnniNodeAtmAddress_Type = PnniAtmAddr
_PnniNodeAtmAddress_Object = MibTableColumn
pnniNodeAtmAddress = _PnniNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 8),
    _PnniNodeAtmAddress_Type()
)
pnniNodeAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeAtmAddress.setStatus("current")
_PnniNodePeerGroupId_Type = PnniPeerGroupId
_PnniNodePeerGroupId_Object = MibTableColumn
pnniNodePeerGroupId = _PnniNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 9),
    _PnniNodePeerGroupId_Type()
)
pnniNodePeerGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePeerGroupId.setStatus("current")


class _PnniNodeRestrictedTransit_Type(TruthValue):
    """Custom type pnniNodeRestrictedTransit based on TruthValue"""


_PnniNodeRestrictedTransit_Object = MibTableColumn
pnniNodeRestrictedTransit = _PnniNodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 10),
    _PnniNodeRestrictedTransit_Type()
)
pnniNodeRestrictedTransit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeRestrictedTransit.setStatus("current")
_PnniNodeComplexRep_Type = TruthValue
_PnniNodeComplexRep_Object = MibTableColumn
pnniNodeComplexRep = _PnniNodeComplexRep_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 11),
    _PnniNodeComplexRep_Type()
)
pnniNodeComplexRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeComplexRep.setStatus("current")
_PnniNodeRestrictedBranching_Type = TruthValue
_PnniNodeRestrictedBranching_Object = MibTableColumn
pnniNodeRestrictedBranching = _PnniNodeRestrictedBranching_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 12),
    _PnniNodeRestrictedBranching_Type()
)
pnniNodeRestrictedBranching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeRestrictedBranching.setStatus("current")
_PnniNodeDatabaseOverload_Type = TruthValue
_PnniNodeDatabaseOverload_Object = MibTableColumn
pnniNodeDatabaseOverload = _PnniNodeDatabaseOverload_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 13),
    _PnniNodeDatabaseOverload_Type()
)
pnniNodeDatabaseOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeDatabaseOverload.setStatus("current")
_PnniNodePtses_Type = Gauge32
_PnniNodePtses_Object = MibTableColumn
pnniNodePtses = _PnniNodePtses_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 14),
    _PnniNodePtses_Type()
)
pnniNodePtses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePtses.setStatus("current")
_PnniNodeRowStatus_Type = RowStatus
_PnniNodeRowStatus_Object = MibTableColumn
pnniNodeRowStatus = _PnniNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 2, 1, 15),
    _PnniNodeRowStatus_Type()
)
pnniNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeRowStatus.setStatus("current")
_PnniNodePglTable_Object = MibTable
pnniNodePglTable = _PnniNodePglTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pnniNodePglTable.setStatus("current")
_PnniNodePglEntry_Object = MibTableRow
pnniNodePglEntry = _PnniNodePglEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pnniNodePglEntry.setStatus("current")


class _PnniNodePglLeadershipPriority_Type(Integer32):
    """Custom type pnniNodePglLeadershipPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 205),
    )


_PnniNodePglLeadershipPriority_Type.__name__ = "Integer32"
_PnniNodePglLeadershipPriority_Object = MibTableColumn
pnniNodePglLeadershipPriority = _PnniNodePglLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 1),
    _PnniNodePglLeadershipPriority_Type()
)
pnniNodePglLeadershipPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePglLeadershipPriority.setStatus("current")


class _PnniNodeCfgParentNodeIndex_Type(PnniNodeIndex):
    """Custom type pnniNodeCfgParentNodeIndex based on PnniNodeIndex"""
    defaultValue = 0


_PnniNodeCfgParentNodeIndex_Object = MibTableColumn
pnniNodeCfgParentNodeIndex = _PnniNodeCfgParentNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 2),
    _PnniNodeCfgParentNodeIndex_Type()
)
pnniNodeCfgParentNodeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeCfgParentNodeIndex.setStatus("current")


class _PnniNodePglInitTime_Type(Integer32):
    """Custom type pnniNodePglInitTime based on Integer32"""
    defaultValue = 15


_PnniNodePglInitTime_Object = MibTableColumn
pnniNodePglInitTime = _PnniNodePglInitTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 3),
    _PnniNodePglInitTime_Type()
)
pnniNodePglInitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePglInitTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePglInitTime.setUnits("seconds")


class _PnniNodePglOverrideDelay_Type(Integer32):
    """Custom type pnniNodePglOverrideDelay based on Integer32"""
    defaultValue = 30


_PnniNodePglOverrideDelay_Object = MibTableColumn
pnniNodePglOverrideDelay = _PnniNodePglOverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 4),
    _PnniNodePglOverrideDelay_Type()
)
pnniNodePglOverrideDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePglOverrideDelay.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePglOverrideDelay.setUnits("seconds")


class _PnniNodePglReelectTime_Type(Integer32):
    """Custom type pnniNodePglReelectTime based on Integer32"""
    defaultValue = 15


_PnniNodePglReelectTime_Object = MibTableColumn
pnniNodePglReelectTime = _PnniNodePglReelectTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 5),
    _PnniNodePglReelectTime_Type()
)
pnniNodePglReelectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePglReelectTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePglReelectTime.setUnits("seconds")


class _PnniNodePglState_Type(Integer32):
    """Custom type pnniNodePglState based on Integer32"""
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
        *(("awaitReElection", 10),
          ("awaitUnanimity", 6),
          ("awaiting", 2),
          ("awaitingFull", 3),
          ("calculating", 5),
          ("hungElection", 9),
          ("initialDelay", 4),
          ("operNotPgl", 8),
          ("operPgl", 7),
          ("starting", 1))
    )


_PnniNodePglState_Type.__name__ = "Integer32"
_PnniNodePglState_Object = MibTableColumn
pnniNodePglState = _PnniNodePglState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 6),
    _PnniNodePglState_Type()
)
pnniNodePglState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePglState.setStatus("current")
_PnniNodePreferredPgl_Type = PnniNodeId
_PnniNodePreferredPgl_Object = MibTableColumn
pnniNodePreferredPgl = _PnniNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 7),
    _PnniNodePreferredPgl_Type()
)
pnniNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePreferredPgl.setStatus("current")
_PnniNodePeerGroupLeader_Type = PnniNodeId
_PnniNodePeerGroupLeader_Object = MibTableColumn
pnniNodePeerGroupLeader = _PnniNodePeerGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 8),
    _PnniNodePeerGroupLeader_Type()
)
pnniNodePeerGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePeerGroupLeader.setStatus("current")
_PnniNodePglTimeStamp_Type = TimeStamp
_PnniNodePglTimeStamp_Object = MibTableColumn
pnniNodePglTimeStamp = _PnniNodePglTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 9),
    _PnniNodePglTimeStamp_Type()
)
pnniNodePglTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodePglTimeStamp.setStatus("current")
_PnniNodeActiveParentNodeId_Type = PnniNodeId
_PnniNodeActiveParentNodeId_Object = MibTableColumn
pnniNodeActiveParentNodeId = _PnniNodeActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 3, 1, 10),
    _PnniNodeActiveParentNodeId_Type()
)
pnniNodeActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNodeActiveParentNodeId.setStatus("current")
_PnniNodeTimerTable_Object = MibTable
pnniNodeTimerTable = _PnniNodeTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pnniNodeTimerTable.setStatus("current")
_PnniNodeTimerEntry_Object = MibTableRow
pnniNodeTimerEntry = _PnniNodeTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pnniNodeTimerEntry.setStatus("current")


class _PnniNodePtseHolddown_Type(Integer32):
    """Custom type pnniNodePtseHolddown based on Integer32"""
    defaultValue = 10


_PnniNodePtseHolddown_Object = MibTableColumn
pnniNodePtseHolddown = _PnniNodePtseHolddown_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 1),
    _PnniNodePtseHolddown_Type()
)
pnniNodePtseHolddown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePtseHolddown.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePtseHolddown.setUnits("100 milliseconds")


class _PnniNodeHelloHolddown_Type(Integer32):
    """Custom type pnniNodeHelloHolddown based on Integer32"""
    defaultValue = 10


_PnniNodeHelloHolddown_Object = MibTableColumn
pnniNodeHelloHolddown = _PnniNodeHelloHolddown_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 2),
    _PnniNodeHelloHolddown_Type()
)
pnniNodeHelloHolddown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeHelloHolddown.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeHelloHolddown.setUnits("100 milliseconds")


class _PnniNodeHelloInterval_Type(Integer32):
    """Custom type pnniNodeHelloInterval based on Integer32"""
    defaultValue = 15


_PnniNodeHelloInterval_Object = MibTableColumn
pnniNodeHelloInterval = _PnniNodeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 3),
    _PnniNodeHelloInterval_Type()
)
pnniNodeHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeHelloInterval.setUnits("seconds")


class _PnniNodeHelloInactivityFactor_Type(Integer32):
    """Custom type pnniNodeHelloInactivityFactor based on Integer32"""
    defaultValue = 5


_PnniNodeHelloInactivityFactor_Object = MibTableColumn
pnniNodeHelloInactivityFactor = _PnniNodeHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 4),
    _PnniNodeHelloInactivityFactor_Type()
)
pnniNodeHelloInactivityFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeHelloInactivityFactor.setStatus("current")


class _PnniNodeHlinkInact_Type(Integer32):
    """Custom type pnniNodeHlinkInact based on Integer32"""
    defaultValue = 120


_PnniNodeHlinkInact_Object = MibTableColumn
pnniNodeHlinkInact = _PnniNodeHlinkInact_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 5),
    _PnniNodeHlinkInact_Type()
)
pnniNodeHlinkInact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeHlinkInact.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeHlinkInact.setUnits("seconds")


class _PnniNodePtseRefreshInterval_Type(Integer32):
    """Custom type pnniNodePtseRefreshInterval based on Integer32"""
    defaultValue = 1800


_PnniNodePtseRefreshInterval_Object = MibTableColumn
pnniNodePtseRefreshInterval = _PnniNodePtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 6),
    _PnniNodePtseRefreshInterval_Type()
)
pnniNodePtseRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePtseRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePtseRefreshInterval.setUnits("seconds")


class _PnniNodePtseLifetimeFactor_Type(Integer32):
    """Custom type pnniNodePtseLifetimeFactor based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1000),
    )


_PnniNodePtseLifetimeFactor_Type.__name__ = "Integer32"
_PnniNodePtseLifetimeFactor_Object = MibTableColumn
pnniNodePtseLifetimeFactor = _PnniNodePtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 7),
    _PnniNodePtseLifetimeFactor_Type()
)
pnniNodePtseLifetimeFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePtseLifetimeFactor.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePtseLifetimeFactor.setUnits("percent")


class _PnniNodeRxmtInterval_Type(Integer32):
    """Custom type pnniNodeRxmtInterval based on Integer32"""
    defaultValue = 5


_PnniNodeRxmtInterval_Object = MibTableColumn
pnniNodeRxmtInterval = _PnniNodeRxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 8),
    _PnniNodeRxmtInterval_Type()
)
pnniNodeRxmtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeRxmtInterval.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeRxmtInterval.setUnits("seconds")


class _PnniNodePeerDelayedAckInterval_Type(Integer32):
    """Custom type pnniNodePeerDelayedAckInterval based on Integer32"""
    defaultValue = 10


_PnniNodePeerDelayedAckInterval_Object = MibTableColumn
pnniNodePeerDelayedAckInterval = _PnniNodePeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 9),
    _PnniNodePeerDelayedAckInterval_Type()
)
pnniNodePeerDelayedAckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodePeerDelayedAckInterval.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodePeerDelayedAckInterval.setUnits("100 milliseconds")


class _PnniNodeAvcrPm_Type(Integer32):
    """Custom type pnniNodeAvcrPm based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnniNodeAvcrPm_Type.__name__ = "Integer32"
_PnniNodeAvcrPm_Object = MibTableColumn
pnniNodeAvcrPm = _PnniNodeAvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 10),
    _PnniNodeAvcrPm_Type()
)
pnniNodeAvcrPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeAvcrPm.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeAvcrPm.setUnits("percent")


class _PnniNodeAvcrMt_Type(Integer32):
    """Custom type pnniNodeAvcrMt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnniNodeAvcrMt_Type.__name__ = "Integer32"
_PnniNodeAvcrMt_Object = MibTableColumn
pnniNodeAvcrMt = _PnniNodeAvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 11),
    _PnniNodeAvcrMt_Type()
)
pnniNodeAvcrMt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeAvcrMt.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeAvcrMt.setUnits("percent")


class _PnniNodeCdvPm_Type(Integer32):
    """Custom type pnniNodeCdvPm based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnniNodeCdvPm_Type.__name__ = "Integer32"
_PnniNodeCdvPm_Object = MibTableColumn
pnniNodeCdvPm = _PnniNodeCdvPm_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 12),
    _PnniNodeCdvPm_Type()
)
pnniNodeCdvPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeCdvPm.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeCdvPm.setUnits("percent")


class _PnniNodeCtdPm_Type(Integer32):
    """Custom type pnniNodeCtdPm based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnniNodeCtdPm_Type.__name__ = "Integer32"
_PnniNodeCtdPm_Object = MibTableColumn
pnniNodeCtdPm = _PnniNodeCtdPm_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 4, 1, 13),
    _PnniNodeCtdPm_Type()
)
pnniNodeCtdPm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeCtdPm.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeCtdPm.setUnits("percent")
_PnniNodeSvccTable_Object = MibTable
pnniNodeSvccTable = _PnniNodeSvccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pnniNodeSvccTable.setStatus("current")
_PnniNodeSvccEntry_Object = MibTableRow
pnniNodeSvccEntry = _PnniNodeSvccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pnniNodeSvccEntry.setStatus("current")


class _PnniNodeSvccInitTime_Type(Integer32):
    """Custom type pnniNodeSvccInitTime based on Integer32"""
    defaultValue = 4


_PnniNodeSvccInitTime_Object = MibTableColumn
pnniNodeSvccInitTime = _PnniNodeSvccInitTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1, 1),
    _PnniNodeSvccInitTime_Type()
)
pnniNodeSvccInitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeSvccInitTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeSvccInitTime.setUnits("seconds")


class _PnniNodeSvccRetryTime_Type(Integer32):
    """Custom type pnniNodeSvccRetryTime based on Integer32"""
    defaultValue = 30


_PnniNodeSvccRetryTime_Object = MibTableColumn
pnniNodeSvccRetryTime = _PnniNodeSvccRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1, 2),
    _PnniNodeSvccRetryTime_Type()
)
pnniNodeSvccRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeSvccRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeSvccRetryTime.setUnits("seconds")


class _PnniNodeSvccCallingIntegrityTime_Type(Integer32):
    """Custom type pnniNodeSvccCallingIntegrityTime based on Integer32"""
    defaultValue = 35


_PnniNodeSvccCallingIntegrityTime_Object = MibTableColumn
pnniNodeSvccCallingIntegrityTime = _PnniNodeSvccCallingIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1, 3),
    _PnniNodeSvccCallingIntegrityTime_Type()
)
pnniNodeSvccCallingIntegrityTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeSvccCallingIntegrityTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeSvccCallingIntegrityTime.setUnits("seconds")


class _PnniNodeSvccCalledIntegrityTime_Type(Integer32):
    """Custom type pnniNodeSvccCalledIntegrityTime based on Integer32"""
    defaultValue = 50


_PnniNodeSvccCalledIntegrityTime_Object = MibTableColumn
pnniNodeSvccCalledIntegrityTime = _PnniNodeSvccCalledIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1, 4),
    _PnniNodeSvccCalledIntegrityTime_Type()
)
pnniNodeSvccCalledIntegrityTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeSvccCalledIntegrityTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniNodeSvccCalledIntegrityTime.setUnits("seconds")
_PnniNodeSvccTrafficDescriptorIndex_Type = AtmTrafficDescrParamIndex
_PnniNodeSvccTrafficDescriptorIndex_Object = MibTableColumn
pnniNodeSvccTrafficDescriptorIndex = _PnniNodeSvccTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 5, 1, 5),
    _PnniNodeSvccTrafficDescriptorIndex_Type()
)
pnniNodeSvccTrafficDescriptorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniNodeSvccTrafficDescriptorIndex.setStatus("current")
_PnniScopeMappingTable_Object = MibTable
pnniScopeMappingTable = _PnniScopeMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pnniScopeMappingTable.setStatus("current")
_PnniScopeMappingEntry_Object = MibTableRow
pnniScopeMappingEntry = _PnniScopeMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pnniScopeMappingEntry.setStatus("current")


class _PnniScopeLocalNetwork_Type(PnniLevel):
    """Custom type pnniScopeLocalNetwork based on PnniLevel"""
    defaultValue = 96


_PnniScopeLocalNetwork_Object = MibTableColumn
pnniScopeLocalNetwork = _PnniScopeLocalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 1),
    _PnniScopeLocalNetwork_Type()
)
pnniScopeLocalNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeLocalNetwork.setStatus("current")


class _PnniScopeLocalNetworkPlusOne_Type(PnniLevel):
    """Custom type pnniScopeLocalNetworkPlusOne based on PnniLevel"""
    defaultValue = 96


_PnniScopeLocalNetworkPlusOne_Object = MibTableColumn
pnniScopeLocalNetworkPlusOne = _PnniScopeLocalNetworkPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 2),
    _PnniScopeLocalNetworkPlusOne_Type()
)
pnniScopeLocalNetworkPlusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeLocalNetworkPlusOne.setStatus("current")


class _PnniScopeLocalNetworkPlusTwo_Type(PnniLevel):
    """Custom type pnniScopeLocalNetworkPlusTwo based on PnniLevel"""
    defaultValue = 96


_PnniScopeLocalNetworkPlusTwo_Object = MibTableColumn
pnniScopeLocalNetworkPlusTwo = _PnniScopeLocalNetworkPlusTwo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 3),
    _PnniScopeLocalNetworkPlusTwo_Type()
)
pnniScopeLocalNetworkPlusTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeLocalNetworkPlusTwo.setStatus("current")


class _PnniScopeSiteMinusOne_Type(PnniLevel):
    """Custom type pnniScopeSiteMinusOne based on PnniLevel"""
    defaultValue = 80


_PnniScopeSiteMinusOne_Object = MibTableColumn
pnniScopeSiteMinusOne = _PnniScopeSiteMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 4),
    _PnniScopeSiteMinusOne_Type()
)
pnniScopeSiteMinusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeSiteMinusOne.setStatus("current")


class _PnniScopeIntraSite_Type(PnniLevel):
    """Custom type pnniScopeIntraSite based on PnniLevel"""
    defaultValue = 80


_PnniScopeIntraSite_Object = MibTableColumn
pnniScopeIntraSite = _PnniScopeIntraSite_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 5),
    _PnniScopeIntraSite_Type()
)
pnniScopeIntraSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeIntraSite.setStatus("current")


class _PnniScopeSitePlusOne_Type(PnniLevel):
    """Custom type pnniScopeSitePlusOne based on PnniLevel"""
    defaultValue = 72


_PnniScopeSitePlusOne_Object = MibTableColumn
pnniScopeSitePlusOne = _PnniScopeSitePlusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 6),
    _PnniScopeSitePlusOne_Type()
)
pnniScopeSitePlusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeSitePlusOne.setStatus("current")


class _PnniScopeOrganizationMinusOne_Type(PnniLevel):
    """Custom type pnniScopeOrganizationMinusOne based on PnniLevel"""
    defaultValue = 72


_PnniScopeOrganizationMinusOne_Object = MibTableColumn
pnniScopeOrganizationMinusOne = _PnniScopeOrganizationMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 7),
    _PnniScopeOrganizationMinusOne_Type()
)
pnniScopeOrganizationMinusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeOrganizationMinusOne.setStatus("current")


class _PnniScopeIntraOrganization_Type(PnniLevel):
    """Custom type pnniScopeIntraOrganization based on PnniLevel"""
    defaultValue = 64


_PnniScopeIntraOrganization_Object = MibTableColumn
pnniScopeIntraOrganization = _PnniScopeIntraOrganization_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 8),
    _PnniScopeIntraOrganization_Type()
)
pnniScopeIntraOrganization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeIntraOrganization.setStatus("current")


class _PnniScopeOrganizationPlusOne_Type(PnniLevel):
    """Custom type pnniScopeOrganizationPlusOne based on PnniLevel"""
    defaultValue = 64


_PnniScopeOrganizationPlusOne_Object = MibTableColumn
pnniScopeOrganizationPlusOne = _PnniScopeOrganizationPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 9),
    _PnniScopeOrganizationPlusOne_Type()
)
pnniScopeOrganizationPlusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeOrganizationPlusOne.setStatus("current")


class _PnniScopeCommunityMinusOne_Type(PnniLevel):
    """Custom type pnniScopeCommunityMinusOne based on PnniLevel"""
    defaultValue = 64


_PnniScopeCommunityMinusOne_Object = MibTableColumn
pnniScopeCommunityMinusOne = _PnniScopeCommunityMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 10),
    _PnniScopeCommunityMinusOne_Type()
)
pnniScopeCommunityMinusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeCommunityMinusOne.setStatus("current")


class _PnniScopeIntraCommunity_Type(PnniLevel):
    """Custom type pnniScopeIntraCommunity based on PnniLevel"""
    defaultValue = 48


_PnniScopeIntraCommunity_Object = MibTableColumn
pnniScopeIntraCommunity = _PnniScopeIntraCommunity_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 11),
    _PnniScopeIntraCommunity_Type()
)
pnniScopeIntraCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeIntraCommunity.setStatus("current")


class _PnniScopeCommunityPlusOne_Type(PnniLevel):
    """Custom type pnniScopeCommunityPlusOne based on PnniLevel"""
    defaultValue = 48


_PnniScopeCommunityPlusOne_Object = MibTableColumn
pnniScopeCommunityPlusOne = _PnniScopeCommunityPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 12),
    _PnniScopeCommunityPlusOne_Type()
)
pnniScopeCommunityPlusOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeCommunityPlusOne.setStatus("current")


class _PnniScopeRegional_Type(PnniLevel):
    """Custom type pnniScopeRegional based on PnniLevel"""
    defaultValue = 32


_PnniScopeRegional_Object = MibTableColumn
pnniScopeRegional = _PnniScopeRegional_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 13),
    _PnniScopeRegional_Type()
)
pnniScopeRegional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeRegional.setStatus("current")


class _PnniScopeInterRegional_Type(PnniLevel):
    """Custom type pnniScopeInterRegional based on PnniLevel"""
    defaultValue = 32


_PnniScopeInterRegional_Object = MibTableColumn
pnniScopeInterRegional = _PnniScopeInterRegional_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 14),
    _PnniScopeInterRegional_Type()
)
pnniScopeInterRegional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeInterRegional.setStatus("current")


class _PnniScopeGlobal_Type(PnniLevel):
    """Custom type pnniScopeGlobal based on PnniLevel"""
    defaultValue = 0


_PnniScopeGlobal_Object = MibTableColumn
pnniScopeGlobal = _PnniScopeGlobal_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 6, 1, 15),
    _PnniScopeGlobal_Type()
)
pnniScopeGlobal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniScopeGlobal.setStatus("current")
_PnniSummaryTable_Object = MibTable
pnniSummaryTable = _PnniSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    pnniSummaryTable.setStatus("deprecated")
_PnniSummaryEntry_Object = MibTableRow
pnniSummaryEntry = _PnniSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1)
)
pnniSummaryEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniSummaryAddress"),
    (0, "PNNI-MIB", "pnniSummaryPrefixLength"),
)
if mibBuilder.loadTexts:
    pnniSummaryEntry.setStatus("deprecated")
_PnniSummaryAddress_Type = AtmAddrPrefix
_PnniSummaryAddress_Object = MibTableColumn
pnniSummaryAddress = _PnniSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 1),
    _PnniSummaryAddress_Type()
)
pnniSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSummaryAddress.setStatus("deprecated")
_PnniSummaryPrefixLength_Type = PnniPrefixLength
_PnniSummaryPrefixLength_Object = MibTableColumn
pnniSummaryPrefixLength = _PnniSummaryPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 2),
    _PnniSummaryPrefixLength_Type()
)
pnniSummaryPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSummaryPrefixLength.setStatus("deprecated")


class _PnniSummaryType_Type(Integer32):
    """Custom type pnniSummaryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 2),
          ("internal", 1))
    )


_PnniSummaryType_Type.__name__ = "Integer32"
_PnniSummaryType_Object = MibTableColumn
pnniSummaryType = _PnniSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 3),
    _PnniSummaryType_Type()
)
pnniSummaryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSummaryType.setStatus("deprecated")


class _PnniSummarySuppress_Type(TruthValue):
    """Custom type pnniSummarySuppress based on TruthValue"""


_PnniSummarySuppress_Object = MibTableColumn
pnniSummarySuppress = _PnniSummarySuppress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 4),
    _PnniSummarySuppress_Type()
)
pnniSummarySuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSummarySuppress.setStatus("deprecated")


class _PnniSummaryState_Type(Integer32):
    """Custom type pnniSummaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 1),
          ("inactive", 3),
          ("suppressing", 2))
    )


_PnniSummaryState_Type.__name__ = "Integer32"
_PnniSummaryState_Object = MibTableColumn
pnniSummaryState = _PnniSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 5),
    _PnniSummaryState_Type()
)
pnniSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSummaryState.setStatus("deprecated")
_PnniSummaryRowStatus_Type = RowStatus
_PnniSummaryRowStatus_Object = MibTableColumn
pnniSummaryRowStatus = _PnniSummaryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 7, 1, 6),
    _PnniSummaryRowStatus_Type()
)
pnniSummaryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSummaryRowStatus.setStatus("deprecated")
_PnniIfTable_Object = MibTable
pnniIfTable = _PnniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    pnniIfTable.setStatus("current")
_PnniIfEntry_Object = MibTableRow
pnniIfEntry = _PnniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1)
)
pnniIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pnniIfEntry.setStatus("current")


class _PnniIfNodeIndex_Type(PnniNodeIndex):
    """Custom type pnniIfNodeIndex based on PnniNodeIndex"""
    defaultValue = 1

    subtypeSpec = PnniNodeIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniIfNodeIndex_Type.__name__ = "PnniNodeIndex"
_PnniIfNodeIndex_Object = MibTableColumn
pnniIfNodeIndex = _PnniIfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 1),
    _PnniIfNodeIndex_Type()
)
pnniIfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfNodeIndex.setStatus("current")
_PnniIfPortId_Type = PnniPortId
_PnniIfPortId_Object = MibTableColumn
pnniIfPortId = _PnniIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 2),
    _PnniIfPortId_Type()
)
pnniIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniIfPortId.setStatus("current")


class _PnniIfAggrToken_Type(PnniAggrToken):
    """Custom type pnniIfAggrToken based on PnniAggrToken"""
    defaultValue = 0


_PnniIfAggrToken_Object = MibTableColumn
pnniIfAggrToken = _PnniIfAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 3),
    _PnniIfAggrToken_Type()
)
pnniIfAggrToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAggrToken.setStatus("current")
_PnniIfVPCapability_Type = TruthValue
_PnniIfVPCapability_Object = MibTableColumn
pnniIfVPCapability = _PnniIfVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 4),
    _PnniIfVPCapability_Type()
)
pnniIfVPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfVPCapability.setStatus("current")


class _PnniIfAdmWeightCbr_Type(Unsigned32):
    """Custom type pnniIfAdmWeightCbr based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniIfAdmWeightCbr_Type.__name__ = "Unsigned32"
_PnniIfAdmWeightCbr_Object = MibTableColumn
pnniIfAdmWeightCbr = _PnniIfAdmWeightCbr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 5),
    _PnniIfAdmWeightCbr_Type()
)
pnniIfAdmWeightCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAdmWeightCbr.setStatus("current")


class _PnniIfAdmWeightRtVbr_Type(Unsigned32):
    """Custom type pnniIfAdmWeightRtVbr based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniIfAdmWeightRtVbr_Type.__name__ = "Unsigned32"
_PnniIfAdmWeightRtVbr_Object = MibTableColumn
pnniIfAdmWeightRtVbr = _PnniIfAdmWeightRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 6),
    _PnniIfAdmWeightRtVbr_Type()
)
pnniIfAdmWeightRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAdmWeightRtVbr.setStatus("current")


class _PnniIfAdmWeightNrtVbr_Type(Unsigned32):
    """Custom type pnniIfAdmWeightNrtVbr based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniIfAdmWeightNrtVbr_Type.__name__ = "Unsigned32"
_PnniIfAdmWeightNrtVbr_Object = MibTableColumn
pnniIfAdmWeightNrtVbr = _PnniIfAdmWeightNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 7),
    _PnniIfAdmWeightNrtVbr_Type()
)
pnniIfAdmWeightNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAdmWeightNrtVbr.setStatus("current")


class _PnniIfAdmWeightAbr_Type(Unsigned32):
    """Custom type pnniIfAdmWeightAbr based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniIfAdmWeightAbr_Type.__name__ = "Unsigned32"
_PnniIfAdmWeightAbr_Object = MibTableColumn
pnniIfAdmWeightAbr = _PnniIfAdmWeightAbr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 8),
    _PnniIfAdmWeightAbr_Type()
)
pnniIfAdmWeightAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAdmWeightAbr.setStatus("current")


class _PnniIfAdmWeightUbr_Type(Unsigned32):
    """Custom type pnniIfAdmWeightUbr based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniIfAdmWeightUbr_Type.__name__ = "Unsigned32"
_PnniIfAdmWeightUbr_Object = MibTableColumn
pnniIfAdmWeightUbr = _PnniIfAdmWeightUbr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 9),
    _PnniIfAdmWeightUbr_Type()
)
pnniIfAdmWeightUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfAdmWeightUbr.setStatus("current")
_PnniIfRccServiceCategory_Type = ServiceCategory
_PnniIfRccServiceCategory_Object = MibTableColumn
pnniIfRccServiceCategory = _PnniIfRccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 10),
    _PnniIfRccServiceCategory_Type()
)
pnniIfRccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfRccServiceCategory.setStatus("current")
_PnniIfRccTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_PnniIfRccTrafficDescrIndex_Object = MibTableColumn
pnniIfRccTrafficDescrIndex = _PnniIfRccTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 8, 1, 11),
    _PnniIfRccTrafficDescrIndex_Type()
)
pnniIfRccTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfRccTrafficDescrIndex.setStatus("current")
_PnniLinkTable_Object = MibTable
pnniLinkTable = _PnniLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    pnniLinkTable.setStatus("current")
_PnniLinkEntry_Object = MibTableRow
pnniLinkEntry = _PnniLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1)
)
pnniLinkEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniLinkPortId"),
)
if mibBuilder.loadTexts:
    pnniLinkEntry.setStatus("current")
_PnniLinkPortId_Type = PnniPortId
_PnniLinkPortId_Object = MibTableColumn
pnniLinkPortId = _PnniLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 1),
    _PnniLinkPortId_Type()
)
pnniLinkPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniLinkPortId.setStatus("current")


class _PnniLinkType_Type(Integer32):
    """Custom type pnniLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("horizontalLinkToFromLgn", 3),
          ("lowestLevelHorizontalLink", 2),
          ("lowestLevelOutsideLink", 4),
          ("outsideLinkAndUplink", 6),
          ("unknown", 1),
          ("uplink", 5))
    )


_PnniLinkType_Type.__name__ = "Integer32"
_PnniLinkType_Object = MibTableColumn
pnniLinkType = _PnniLinkType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 2),
    _PnniLinkType_Type()
)
pnniLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkType.setStatus("current")
_PnniLinkVersion_Type = PnniVersion
_PnniLinkVersion_Object = MibTableColumn
pnniLinkVersion = _PnniLinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 3),
    _PnniLinkVersion_Type()
)
pnniLinkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkVersion.setStatus("current")
_PnniLinkHelloState_Type = PnniHelloState
_PnniLinkHelloState_Object = MibTableColumn
pnniLinkHelloState = _PnniLinkHelloState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 4),
    _PnniLinkHelloState_Type()
)
pnniLinkHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkHelloState.setStatus("current")
_PnniLinkRemoteNodeId_Type = PnniNodeId
_PnniLinkRemoteNodeId_Object = MibTableColumn
pnniLinkRemoteNodeId = _PnniLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 5),
    _PnniLinkRemoteNodeId_Type()
)
pnniLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkRemoteNodeId.setStatus("current")
_PnniLinkRemotePortId_Type = PnniPortId
_PnniLinkRemotePortId_Object = MibTableColumn
pnniLinkRemotePortId = _PnniLinkRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 6),
    _PnniLinkRemotePortId_Type()
)
pnniLinkRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkRemotePortId.setStatus("current")
_PnniLinkDerivedAggrToken_Type = PnniAggrToken
_PnniLinkDerivedAggrToken_Object = MibTableColumn
pnniLinkDerivedAggrToken = _PnniLinkDerivedAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 7),
    _PnniLinkDerivedAggrToken_Type()
)
pnniLinkDerivedAggrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkDerivedAggrToken.setStatus("current")
_PnniLinkUpnodeId_Type = PnniNodeId
_PnniLinkUpnodeId_Object = MibTableColumn
pnniLinkUpnodeId = _PnniLinkUpnodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 8),
    _PnniLinkUpnodeId_Type()
)
pnniLinkUpnodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkUpnodeId.setStatus("current")
_PnniLinkUpnodeAtmAddress_Type = PnniAtmAddr
_PnniLinkUpnodeAtmAddress_Object = MibTableColumn
pnniLinkUpnodeAtmAddress = _PnniLinkUpnodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 9),
    _PnniLinkUpnodeAtmAddress_Type()
)
pnniLinkUpnodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkUpnodeAtmAddress.setStatus("current")
_PnniLinkCommonPeerGroupId_Type = PnniPeerGroupId
_PnniLinkCommonPeerGroupId_Object = MibTableColumn
pnniLinkCommonPeerGroupId = _PnniLinkCommonPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 10),
    _PnniLinkCommonPeerGroupId_Type()
)
pnniLinkCommonPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkCommonPeerGroupId.setStatus("current")
_PnniLinkIfIndex_Type = InterfaceIndex
_PnniLinkIfIndex_Object = MibTableColumn
pnniLinkIfIndex = _PnniLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 11),
    _PnniLinkIfIndex_Type()
)
pnniLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkIfIndex.setStatus("current")
_PnniLinkSvccRccIndex_Type = PnniSvccRccIndex
_PnniLinkSvccRccIndex_Object = MibTableColumn
pnniLinkSvccRccIndex = _PnniLinkSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 12),
    _PnniLinkSvccRccIndex_Type()
)
pnniLinkSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkSvccRccIndex.setStatus("current")
_PnniLinkRcvHellos_Type = Counter32
_PnniLinkRcvHellos_Object = MibTableColumn
pnniLinkRcvHellos = _PnniLinkRcvHellos_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 13),
    _PnniLinkRcvHellos_Type()
)
pnniLinkRcvHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkRcvHellos.setStatus("current")
_PnniLinkXmtHellos_Type = Counter32
_PnniLinkXmtHellos_Object = MibTableColumn
pnniLinkXmtHellos = _PnniLinkXmtHellos_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 9, 1, 14),
    _PnniLinkXmtHellos_Type()
)
pnniLinkXmtHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniLinkXmtHellos.setStatus("current")
_PnniNbrPeerTable_Object = MibTable
pnniNbrPeerTable = _PnniNbrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    pnniNbrPeerTable.setStatus("current")
_PnniNbrPeerEntry_Object = MibTableRow
pnniNbrPeerEntry = _PnniNbrPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1)
)
pnniNbrPeerEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniNbrPeerRemoteNodeId"),
)
if mibBuilder.loadTexts:
    pnniNbrPeerEntry.setStatus("current")
_PnniNbrPeerRemoteNodeId_Type = PnniNodeId
_PnniNbrPeerRemoteNodeId_Object = MibTableColumn
pnniNbrPeerRemoteNodeId = _PnniNbrPeerRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 1),
    _PnniNbrPeerRemoteNodeId_Type()
)
pnniNbrPeerRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniNbrPeerRemoteNodeId.setStatus("current")


class _PnniNbrPeerState_Type(Integer32):
    """Custom type pnniNbrPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("exchanging", 3),
          ("full", 5),
          ("loading", 4),
          ("negotiating", 2),
          ("npdown", 1))
    )


_PnniNbrPeerState_Type.__name__ = "Integer32"
_PnniNbrPeerState_Object = MibTableColumn
pnniNbrPeerState = _PnniNbrPeerState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 2),
    _PnniNbrPeerState_Type()
)
pnniNbrPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerState.setStatus("current")
_PnniNbrPeerSvccRccIndex_Type = PnniSvccRccIndex
_PnniNbrPeerSvccRccIndex_Object = MibTableColumn
pnniNbrPeerSvccRccIndex = _PnniNbrPeerSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 3),
    _PnniNbrPeerSvccRccIndex_Type()
)
pnniNbrPeerSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerSvccRccIndex.setStatus("current")
_PnniNbrPeerPortCount_Type = Gauge32
_PnniNbrPeerPortCount_Object = MibTableColumn
pnniNbrPeerPortCount = _PnniNbrPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 4),
    _PnniNbrPeerPortCount_Type()
)
pnniNbrPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerPortCount.setStatus("current")
_PnniNbrPeerRcvDbSums_Type = Counter32
_PnniNbrPeerRcvDbSums_Object = MibTableColumn
pnniNbrPeerRcvDbSums = _PnniNbrPeerRcvDbSums_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 5),
    _PnniNbrPeerRcvDbSums_Type()
)
pnniNbrPeerRcvDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerRcvDbSums.setStatus("current")
_PnniNbrPeerXmtDbSums_Type = Counter32
_PnniNbrPeerXmtDbSums_Object = MibTableColumn
pnniNbrPeerXmtDbSums = _PnniNbrPeerXmtDbSums_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 6),
    _PnniNbrPeerXmtDbSums_Type()
)
pnniNbrPeerXmtDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerXmtDbSums.setStatus("current")
_PnniNbrPeerRcvPtsps_Type = Counter32
_PnniNbrPeerRcvPtsps_Object = MibTableColumn
pnniNbrPeerRcvPtsps = _PnniNbrPeerRcvPtsps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 7),
    _PnniNbrPeerRcvPtsps_Type()
)
pnniNbrPeerRcvPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerRcvPtsps.setStatus("current")
_PnniNbrPeerXmtPtsps_Type = Counter32
_PnniNbrPeerXmtPtsps_Object = MibTableColumn
pnniNbrPeerXmtPtsps = _PnniNbrPeerXmtPtsps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 8),
    _PnniNbrPeerXmtPtsps_Type()
)
pnniNbrPeerXmtPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerXmtPtsps.setStatus("current")
_PnniNbrPeerRcvPtseReqs_Type = Counter32
_PnniNbrPeerRcvPtseReqs_Object = MibTableColumn
pnniNbrPeerRcvPtseReqs = _PnniNbrPeerRcvPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 9),
    _PnniNbrPeerRcvPtseReqs_Type()
)
pnniNbrPeerRcvPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerRcvPtseReqs.setStatus("current")
_PnniNbrPeerXmtPtseReqs_Type = Counter32
_PnniNbrPeerXmtPtseReqs_Object = MibTableColumn
pnniNbrPeerXmtPtseReqs = _PnniNbrPeerXmtPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 10),
    _PnniNbrPeerXmtPtseReqs_Type()
)
pnniNbrPeerXmtPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerXmtPtseReqs.setStatus("current")
_PnniNbrPeerRcvPtseAcks_Type = Counter32
_PnniNbrPeerRcvPtseAcks_Object = MibTableColumn
pnniNbrPeerRcvPtseAcks = _PnniNbrPeerRcvPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 11),
    _PnniNbrPeerRcvPtseAcks_Type()
)
pnniNbrPeerRcvPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerRcvPtseAcks.setStatus("current")
_PnniNbrPeerXmtPtseAcks_Type = Counter32
_PnniNbrPeerXmtPtseAcks_Object = MibTableColumn
pnniNbrPeerXmtPtseAcks = _PnniNbrPeerXmtPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 10, 1, 12),
    _PnniNbrPeerXmtPtseAcks_Type()
)
pnniNbrPeerXmtPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerXmtPtseAcks.setStatus("current")
_PnniNbrPeerPortTable_Object = MibTable
pnniNbrPeerPortTable = _PnniNbrPeerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pnniNbrPeerPortTable.setStatus("current")
_PnniNbrPeerPortEntry_Object = MibTableRow
pnniNbrPeerPortEntry = _PnniNbrPeerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 11, 1)
)
pnniNbrPeerPortEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniNbrPeerRemoteNodeId"),
    (0, "PNNI-MIB", "pnniNbrPeerPortId"),
)
if mibBuilder.loadTexts:
    pnniNbrPeerPortEntry.setStatus("current")
_PnniNbrPeerPortId_Type = PnniPortId
_PnniNbrPeerPortId_Object = MibTableColumn
pnniNbrPeerPortId = _PnniNbrPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 11, 1, 1),
    _PnniNbrPeerPortId_Type()
)
pnniNbrPeerPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniNbrPeerPortId.setStatus("current")
_PnniNbrPeerPortFloodStatus_Type = TruthValue
_PnniNbrPeerPortFloodStatus_Object = MibTableColumn
pnniNbrPeerPortFloodStatus = _PnniNbrPeerPortFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 11, 1, 2),
    _PnniNbrPeerPortFloodStatus_Type()
)
pnniNbrPeerPortFloodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniNbrPeerPortFloodStatus.setStatus("current")
_PnniSvccRccTable_Object = MibTable
pnniSvccRccTable = _PnniSvccRccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pnniSvccRccTable.setStatus("current")
_PnniSvccRccEntry_Object = MibTableRow
pnniSvccRccEntry = _PnniSvccRccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1)
)
pnniSvccRccEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniSvccRccIndex"),
)
if mibBuilder.loadTexts:
    pnniSvccRccEntry.setStatus("current")
_PnniSvccRccIndex_Type = PnniSvccRccIndex
_PnniSvccRccIndex_Object = MibTableColumn
pnniSvccRccIndex = _PnniSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 1),
    _PnniSvccRccIndex_Type()
)
pnniSvccRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSvccRccIndex.setStatus("current")
_PnniSvccRccVersion_Type = PnniVersion
_PnniSvccRccVersion_Object = MibTableColumn
pnniSvccRccVersion = _PnniSvccRccVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 2),
    _PnniSvccRccVersion_Type()
)
pnniSvccRccVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccVersion.setStatus("current")
_PnniSvccRccHelloState_Type = PnniHelloState
_PnniSvccRccHelloState_Object = MibTableColumn
pnniSvccRccHelloState = _PnniSvccRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 3),
    _PnniSvccRccHelloState_Type()
)
pnniSvccRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccHelloState.setStatus("current")
_PnniSvccRccRemoteNodeId_Type = PnniNodeId
_PnniSvccRccRemoteNodeId_Object = MibTableColumn
pnniSvccRccRemoteNodeId = _PnniSvccRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 4),
    _PnniSvccRccRemoteNodeId_Type()
)
pnniSvccRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccRemoteNodeId.setStatus("current")
_PnniSvccRccRemoteAtmAddress_Type = PnniAtmAddr
_PnniSvccRccRemoteAtmAddress_Object = MibTableColumn
pnniSvccRccRemoteAtmAddress = _PnniSvccRccRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 5),
    _PnniSvccRccRemoteAtmAddress_Type()
)
pnniSvccRccRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccRemoteAtmAddress.setStatus("current")
_PnniSvccRccRcvHellos_Type = Counter32
_PnniSvccRccRcvHellos_Object = MibTableColumn
pnniSvccRccRcvHellos = _PnniSvccRccRcvHellos_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 6),
    _PnniSvccRccRcvHellos_Type()
)
pnniSvccRccRcvHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccRcvHellos.setStatus("current")
_PnniSvccRccXmtHellos_Type = Counter32
_PnniSvccRccXmtHellos_Object = MibTableColumn
pnniSvccRccXmtHellos = _PnniSvccRccXmtHellos_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 7),
    _PnniSvccRccXmtHellos_Type()
)
pnniSvccRccXmtHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccXmtHellos.setStatus("current")
_PnniSvccRccIfIndex_Type = InterfaceIndex
_PnniSvccRccIfIndex_Object = MibTableColumn
pnniSvccRccIfIndex = _PnniSvccRccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 8),
    _PnniSvccRccIfIndex_Type()
)
pnniSvccRccIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccIfIndex.setStatus("current")


class _PnniSvccRccVpi_Type(Integer32):
    """Custom type pnniSvccRccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PnniSvccRccVpi_Type.__name__ = "Integer32"
_PnniSvccRccVpi_Object = MibTableColumn
pnniSvccRccVpi = _PnniSvccRccVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 9),
    _PnniSvccRccVpi_Type()
)
pnniSvccRccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccVpi.setStatus("current")


class _PnniSvccRccVci_Type(Integer32):
    """Custom type pnniSvccRccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnniSvccRccVci_Type.__name__ = "Integer32"
_PnniSvccRccVci_Object = MibTableColumn
pnniSvccRccVci = _PnniSvccRccVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 12, 1, 10),
    _PnniSvccRccVci_Type()
)
pnniSvccRccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSvccRccVci.setStatus("current")
_PnniPtseTable_Object = MibTable
pnniPtseTable = _PnniPtseTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    pnniPtseTable.setStatus("current")
_PnniPtseEntry_Object = MibTableRow
pnniPtseEntry = _PnniPtseEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1)
)
pnniPtseEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniPtseOriginatingNodeId"),
    (0, "PNNI-MIB", "pnniPtseId"),
)
if mibBuilder.loadTexts:
    pnniPtseEntry.setStatus("current")
_PnniPtseOriginatingNodeId_Type = PnniNodeId
_PnniPtseOriginatingNodeId_Object = MibTableColumn
pnniPtseOriginatingNodeId = _PnniPtseOriginatingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 1),
    _PnniPtseOriginatingNodeId_Type()
)
pnniPtseOriginatingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPtseOriginatingNodeId.setStatus("current")
_PnniPtseId_Type = Unsigned32
_PnniPtseId_Object = MibTableColumn
pnniPtseId = _PnniPtseId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 2),
    _PnniPtseId_Type()
)
pnniPtseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniPtseId.setStatus("current")


class _PnniPtseType_Type(Integer32):
    """Custom type pnniPtseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              96,
              97,
              224,
              256,
              288,
              289)
        )
    )
    namedValues = NamedValues(
        *(("exteriorReachableAddresses", 256),
          ("horizontalLinks", 288),
          ("internalReachableAddresses", 224),
          ("nodalInformation", 97),
          ("nodalStateParameters", 96),
          ("other", 1),
          ("uplinks", 289))
    )


_PnniPtseType_Type.__name__ = "Integer32"
_PnniPtseType_Object = MibTableColumn
pnniPtseType = _PnniPtseType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 3),
    _PnniPtseType_Type()
)
pnniPtseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPtseType.setStatus("current")
_PnniPtseSequenceNum_Type = Unsigned32
_PnniPtseSequenceNum_Object = MibTableColumn
pnniPtseSequenceNum = _PnniPtseSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 4),
    _PnniPtseSequenceNum_Type()
)
pnniPtseSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPtseSequenceNum.setStatus("current")


class _PnniPtseChecksum_Type(Unsigned32):
    """Custom type pnniPtseChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnniPtseChecksum_Type.__name__ = "Unsigned32"
_PnniPtseChecksum_Object = MibTableColumn
pnniPtseChecksum = _PnniPtseChecksum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 5),
    _PnniPtseChecksum_Type()
)
pnniPtseChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPtseChecksum.setStatus("current")


class _PnniPtseLifeTime_Type(Unsigned32):
    """Custom type pnniPtseLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnniPtseLifeTime_Type.__name__ = "Unsigned32"
_PnniPtseLifeTime_Object = MibTableColumn
pnniPtseLifeTime = _PnniPtseLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 6),
    _PnniPtseLifeTime_Type()
)
pnniPtseLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPtseLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    pnniPtseLifeTime.setUnits("seconds")


class _PnniPtseInfo_Type(OctetString):
    """Custom type pnniPtseInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_PnniPtseInfo_Type.__name__ = "OctetString"
_PnniPtseInfo_Object = MibTableColumn
pnniPtseInfo = _PnniPtseInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 13, 1, 7),
    _PnniPtseInfo_Type()
)
pnniPtseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniPtseInfo.setStatus("current")
_PnniMapTable_Object = MibTable
pnniMapTable = _PnniMapTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    pnniMapTable.setStatus("current")
_PnniMapEntry_Object = MibTableRow
pnniMapEntry = _PnniMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1)
)
pnniMapEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapOriginatingNodeId"),
    (0, "PNNI-MIB", "pnniMapOriginatingPortId"),
    (0, "PNNI-MIB", "pnniMapIndex"),
)
if mibBuilder.loadTexts:
    pnniMapEntry.setStatus("current")
_PnniMapOriginatingNodeId_Type = PnniNodeId
_PnniMapOriginatingNodeId_Object = MibTableColumn
pnniMapOriginatingNodeId = _PnniMapOriginatingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 1),
    _PnniMapOriginatingNodeId_Type()
)
pnniMapOriginatingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapOriginatingNodeId.setStatus("current")
_PnniMapOriginatingPortId_Type = PnniPortId
_PnniMapOriginatingPortId_Object = MibTableColumn
pnniMapOriginatingPortId = _PnniMapOriginatingPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 2),
    _PnniMapOriginatingPortId_Type()
)
pnniMapOriginatingPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapOriginatingPortId.setStatus("current")


class _PnniMapIndex_Type(Integer32):
    """Custom type pnniMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnniMapIndex_Type.__name__ = "Integer32"
_PnniMapIndex_Object = MibTableColumn
pnniMapIndex = _PnniMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 3),
    _PnniMapIndex_Type()
)
pnniMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapIndex.setStatus("current")


class _PnniMapType_Type(Integer32):
    """Custom type pnniMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("horizontalLink", 1),
          ("node", 3),
          ("uplink", 2))
    )


_PnniMapType_Type.__name__ = "Integer32"
_PnniMapType_Object = MibTableColumn
pnniMapType = _PnniMapType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 4),
    _PnniMapType_Type()
)
pnniMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapType.setStatus("current")
_PnniMapPeerGroupId_Type = PnniPeerGroupId
_PnniMapPeerGroupId_Object = MibTableColumn
pnniMapPeerGroupId = _PnniMapPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 5),
    _PnniMapPeerGroupId_Type()
)
pnniMapPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapPeerGroupId.setStatus("current")
_PnniMapAggrToken_Type = PnniAggrToken
_PnniMapAggrToken_Object = MibTableColumn
pnniMapAggrToken = _PnniMapAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 6),
    _PnniMapAggrToken_Type()
)
pnniMapAggrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAggrToken.setStatus("current")
_PnniMapRemoteNodeId_Type = PnniNodeId
_PnniMapRemoteNodeId_Object = MibTableColumn
pnniMapRemoteNodeId = _PnniMapRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 7),
    _PnniMapRemoteNodeId_Type()
)
pnniMapRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRemoteNodeId.setStatus("current")
_PnniMapRemotePortId_Type = PnniPortId
_PnniMapRemotePortId_Object = MibTableColumn
pnniMapRemotePortId = _PnniMapRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 8),
    _PnniMapRemotePortId_Type()
)
pnniMapRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapRemotePortId.setStatus("current")
_PnniMapVPCapability_Type = TruthValue
_PnniMapVPCapability_Object = MibTableColumn
pnniMapVPCapability = _PnniMapVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 9),
    _PnniMapVPCapability_Type()
)
pnniMapVPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapVPCapability.setStatus("current")
_PnniMapPtseId_Type = Unsigned32
_PnniMapPtseId_Object = MibTableColumn
pnniMapPtseId = _PnniMapPtseId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 10),
    _PnniMapPtseId_Type()
)
pnniMapPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapPtseId.setStatus("current")
_PnniMapMetricsTag_Type = PnniMetricsTag
_PnniMapMetricsTag_Object = MibTableColumn
pnniMapMetricsTag = _PnniMapMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 14, 1, 11),
    _PnniMapMetricsTag_Type()
)
pnniMapMetricsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapMetricsTag.setStatus("current")
_PnniMapNodeTable_Object = MibTable
pnniMapNodeTable = _PnniMapNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    pnniMapNodeTable.setStatus("current")
_PnniMapNodeEntry_Object = MibTableRow
pnniMapNodeEntry = _PnniMapNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1)
)
pnniMapNodeEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapNodeId"),
)
if mibBuilder.loadTexts:
    pnniMapNodeEntry.setStatus("current")
_PnniMapNodeId_Type = PnniNodeId
_PnniMapNodeId_Object = MibTableColumn
pnniMapNodeId = _PnniMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 1),
    _PnniMapNodeId_Type()
)
pnniMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapNodeId.setStatus("current")
_PnniMapNodePeerGroupId_Type = PnniPeerGroupId
_PnniMapNodePeerGroupId_Object = MibTableColumn
pnniMapNodePeerGroupId = _PnniMapNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 2),
    _PnniMapNodePeerGroupId_Type()
)
pnniMapNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodePeerGroupId.setStatus("current")
_PnniMapNodeAtmAddress_Type = PnniAtmAddr
_PnniMapNodeAtmAddress_Object = MibTableColumn
pnniMapNodeAtmAddress = _PnniMapNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 3),
    _PnniMapNodeAtmAddress_Type()
)
pnniMapNodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeAtmAddress.setStatus("current")
_PnniMapNodeRestrictedTransit_Type = TruthValue
_PnniMapNodeRestrictedTransit_Object = MibTableColumn
pnniMapNodeRestrictedTransit = _PnniMapNodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 4),
    _PnniMapNodeRestrictedTransit_Type()
)
pnniMapNodeRestrictedTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeRestrictedTransit.setStatus("current")
_PnniMapNodeComplexRep_Type = TruthValue
_PnniMapNodeComplexRep_Object = MibTableColumn
pnniMapNodeComplexRep = _PnniMapNodeComplexRep_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 5),
    _PnniMapNodeComplexRep_Type()
)
pnniMapNodeComplexRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeComplexRep.setStatus("current")
_PnniMapNodeRestrictedBranching_Type = TruthValue
_PnniMapNodeRestrictedBranching_Object = MibTableColumn
pnniMapNodeRestrictedBranching = _PnniMapNodeRestrictedBranching_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 6),
    _PnniMapNodeRestrictedBranching_Type()
)
pnniMapNodeRestrictedBranching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeRestrictedBranching.setStatus("current")
_PnniMapNodeDatabaseOverload_Type = TruthValue
_PnniMapNodeDatabaseOverload_Object = MibTableColumn
pnniMapNodeDatabaseOverload = _PnniMapNodeDatabaseOverload_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 7),
    _PnniMapNodeDatabaseOverload_Type()
)
pnniMapNodeDatabaseOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeDatabaseOverload.setStatus("current")
_PnniMapNodeIAmLeader_Type = TruthValue
_PnniMapNodeIAmLeader_Object = MibTableColumn
pnniMapNodeIAmLeader = _PnniMapNodeIAmLeader_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 8),
    _PnniMapNodeIAmLeader_Type()
)
pnniMapNodeIAmLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeIAmLeader.setStatus("current")


class _PnniMapNodeLeadershipPriority_Type(Integer32):
    """Custom type pnniMapNodeLeadershipPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PnniMapNodeLeadershipPriority_Type.__name__ = "Integer32"
_PnniMapNodeLeadershipPriority_Object = MibTableColumn
pnniMapNodeLeadershipPriority = _PnniMapNodeLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 9),
    _PnniMapNodeLeadershipPriority_Type()
)
pnniMapNodeLeadershipPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeLeadershipPriority.setStatus("current")
_PnniMapNodePreferredPgl_Type = PnniNodeId
_PnniMapNodePreferredPgl_Object = MibTableColumn
pnniMapNodePreferredPgl = _PnniMapNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 10),
    _PnniMapNodePreferredPgl_Type()
)
pnniMapNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodePreferredPgl.setStatus("current")
_PnniMapNodeParentNodeId_Type = PnniNodeId
_PnniMapNodeParentNodeId_Object = MibTableColumn
pnniMapNodeParentNodeId = _PnniMapNodeParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 11),
    _PnniMapNodeParentNodeId_Type()
)
pnniMapNodeParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeParentNodeId.setStatus("current")
_PnniMapNodeParentAtmAddress_Type = PnniAtmAddr
_PnniMapNodeParentAtmAddress_Object = MibTableColumn
pnniMapNodeParentAtmAddress = _PnniMapNodeParentAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 12),
    _PnniMapNodeParentAtmAddress_Type()
)
pnniMapNodeParentAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeParentAtmAddress.setStatus("current")
_PnniMapNodeParentPeerGroupId_Type = PnniPeerGroupId
_PnniMapNodeParentPeerGroupId_Object = MibTableColumn
pnniMapNodeParentPeerGroupId = _PnniMapNodeParentPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 13),
    _PnniMapNodeParentPeerGroupId_Type()
)
pnniMapNodeParentPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeParentPeerGroupId.setStatus("current")
_PnniMapNodeParentPglNodeId_Type = PnniNodeId
_PnniMapNodeParentPglNodeId_Object = MibTableColumn
pnniMapNodeParentPglNodeId = _PnniMapNodeParentPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 15, 1, 14),
    _PnniMapNodeParentPglNodeId_Type()
)
pnniMapNodeParentPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapNodeParentPglNodeId.setStatus("current")
_PnniMapAddrTable_Object = MibTable
pnniMapAddrTable = _PnniMapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    pnniMapAddrTable.setStatus("current")
_PnniMapAddrEntry_Object = MibTableRow
pnniMapAddrEntry = _PnniMapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1)
)
pnniMapAddrEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapAddrAdvertisingNodeId"),
    (0, "PNNI-MIB", "pnniMapAddrAdvertisedPortId"),
    (0, "PNNI-MIB", "pnniMapAddrIndex"),
)
if mibBuilder.loadTexts:
    pnniMapAddrEntry.setStatus("current")
_PnniMapAddrAdvertisingNodeId_Type = PnniNodeId
_PnniMapAddrAdvertisingNodeId_Object = MibTableColumn
pnniMapAddrAdvertisingNodeId = _PnniMapAddrAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1, 1),
    _PnniMapAddrAdvertisingNodeId_Type()
)
pnniMapAddrAdvertisingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapAddrAdvertisingNodeId.setStatus("current")
_PnniMapAddrAdvertisedPortId_Type = PnniPortId
_PnniMapAddrAdvertisedPortId_Object = MibTableColumn
pnniMapAddrAdvertisedPortId = _PnniMapAddrAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1, 2),
    _PnniMapAddrAdvertisedPortId_Type()
)
pnniMapAddrAdvertisedPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapAddrAdvertisedPortId.setStatus("current")


class _PnniMapAddrIndex_Type(Integer32):
    """Custom type pnniMapAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniMapAddrIndex_Type.__name__ = "Integer32"
_PnniMapAddrIndex_Object = MibTableColumn
pnniMapAddrIndex = _PnniMapAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1, 3),
    _PnniMapAddrIndex_Type()
)
pnniMapAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapAddrIndex.setStatus("current")
_PnniMapAddrAddress_Type = AtmAddrPrefix
_PnniMapAddrAddress_Object = MibTableColumn
pnniMapAddrAddress = _PnniMapAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1, 4),
    _PnniMapAddrAddress_Type()
)
pnniMapAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrAddress.setStatus("current")
_PnniMapAddrPrefixLength_Type = PnniPrefixLength
_PnniMapAddrPrefixLength_Object = MibTableColumn
pnniMapAddrPrefixLength = _PnniMapAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 16, 1, 5),
    _PnniMapAddrPrefixLength_Type()
)
pnniMapAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapAddrPrefixLength.setStatus("current")
_PnniMapTnsTable_Object = MibTable
pnniMapTnsTable = _PnniMapTnsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    pnniMapTnsTable.setStatus("current")
_PnniMapTnsEntry_Object = MibTableRow
pnniMapTnsEntry = _PnniMapTnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1)
)
pnniMapTnsEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMapTnsAdvertisingNodeId"),
    (0, "PNNI-MIB", "pnniMapTnsAdvertisedPortId"),
    (0, "PNNI-MIB", "pnniMapTnsType"),
    (0, "PNNI-MIB", "pnniMapTnsPlan"),
    (0, "PNNI-MIB", "pnniMapTnsId"),
)
if mibBuilder.loadTexts:
    pnniMapTnsEntry.setStatus("current")
_PnniMapTnsAdvertisingNodeId_Type = PnniNodeId
_PnniMapTnsAdvertisingNodeId_Object = MibTableColumn
pnniMapTnsAdvertisingNodeId = _PnniMapTnsAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1, 1),
    _PnniMapTnsAdvertisingNodeId_Type()
)
pnniMapTnsAdvertisingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapTnsAdvertisingNodeId.setStatus("current")
_PnniMapTnsAdvertisedPortId_Type = PnniPortId
_PnniMapTnsAdvertisedPortId_Object = MibTableColumn
pnniMapTnsAdvertisedPortId = _PnniMapTnsAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1, 2),
    _PnniMapTnsAdvertisedPortId_Type()
)
pnniMapTnsAdvertisedPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapTnsAdvertisedPortId.setStatus("current")
_PnniMapTnsType_Type = TnsType
_PnniMapTnsType_Object = MibTableColumn
pnniMapTnsType = _PnniMapTnsType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1, 3),
    _PnniMapTnsType_Type()
)
pnniMapTnsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapTnsType.setStatus("current")
_PnniMapTnsPlan_Type = TnsPlan
_PnniMapTnsPlan_Object = MibTableColumn
pnniMapTnsPlan = _PnniMapTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1, 4),
    _PnniMapTnsPlan_Type()
)
pnniMapTnsPlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMapTnsPlan.setStatus("current")
_PnniMapTnsId_Type = DisplayString
_PnniMapTnsId_Object = MibTableColumn
pnniMapTnsId = _PnniMapTnsId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 17, 1, 5),
    _PnniMapTnsId_Type()
)
pnniMapTnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMapTnsId.setStatus("current")
_PnniMetricsTable_Object = MibTable
pnniMetricsTable = _PnniMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    pnniMetricsTable.setStatus("current")
_PnniMetricsEntry_Object = MibTableRow
pnniMetricsEntry = _PnniMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1)
)
pnniMetricsEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniMetricsTag"),
    (0, "PNNI-MIB", "pnniMetricsDirection"),
    (0, "PNNI-MIB", "pnniMetricsIndex"),
)
if mibBuilder.loadTexts:
    pnniMetricsEntry.setStatus("current")


class _PnniMetricsTag_Type(PnniMetricsTag):
    """Custom type pnniMetricsTag based on PnniMetricsTag"""
    subtypeSpec = PnniMetricsTag.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniMetricsTag_Type.__name__ = "PnniMetricsTag"
_PnniMetricsTag_Object = MibTableColumn
pnniMetricsTag = _PnniMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 1),
    _PnniMetricsTag_Type()
)
pnniMetricsTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMetricsTag.setStatus("current")


class _PnniMetricsDirection_Type(Integer32):
    """Custom type pnniMetricsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_PnniMetricsDirection_Type.__name__ = "Integer32"
_PnniMetricsDirection_Object = MibTableColumn
pnniMetricsDirection = _PnniMetricsDirection_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 2),
    _PnniMetricsDirection_Type()
)
pnniMetricsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMetricsDirection.setStatus("current")


class _PnniMetricsIndex_Type(Integer32):
    """Custom type pnniMetricsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniMetricsIndex_Type.__name__ = "Integer32"
_PnniMetricsIndex_Object = MibTableColumn
pnniMetricsIndex = _PnniMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 3),
    _PnniMetricsIndex_Type()
)
pnniMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniMetricsIndex.setStatus("current")


class _PnniMetricsClasses_Type(Integer32):
    """Custom type pnniMetricsClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PnniMetricsClasses_Type.__name__ = "Integer32"
_PnniMetricsClasses_Object = MibTableColumn
pnniMetricsClasses = _PnniMetricsClasses_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 4),
    _PnniMetricsClasses_Type()
)
pnniMetricsClasses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetricsClasses.setStatus("current")
_PnniMetricsGcacClp_Type = ClpType
_PnniMetricsGcacClp_Object = MibTableColumn
pnniMetricsGcacClp = _PnniMetricsGcacClp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 5),
    _PnniMetricsGcacClp_Type()
)
pnniMetricsGcacClp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetricsGcacClp.setStatus("current")


class _PnniMetricsAdminWeight_Type(Unsigned32):
    """Custom type pnniMetricsAdminWeight based on Unsigned32"""
    defaultValue = 5040

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PnniMetricsAdminWeight_Type.__name__ = "Unsigned32"
_PnniMetricsAdminWeight_Object = MibTableColumn
pnniMetricsAdminWeight = _PnniMetricsAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 6),
    _PnniMetricsAdminWeight_Type()
)
pnniMetricsAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetricsAdminWeight.setStatus("current")


class _PnniMetrics1_Type(Unsigned32):
    """Custom type pnniMetrics1 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics1_Object = MibTableColumn
pnniMetrics1 = _PnniMetrics1_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 7),
    _PnniMetrics1_Type()
)
pnniMetrics1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics1.setStatus("current")


class _PnniMetrics2_Type(Unsigned32):
    """Custom type pnniMetrics2 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics2_Object = MibTableColumn
pnniMetrics2 = _PnniMetrics2_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 8),
    _PnniMetrics2_Type()
)
pnniMetrics2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics2.setStatus("current")


class _PnniMetrics3_Type(Unsigned32):
    """Custom type pnniMetrics3 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics3_Object = MibTableColumn
pnniMetrics3 = _PnniMetrics3_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 9),
    _PnniMetrics3_Type()
)
pnniMetrics3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics3.setStatus("current")


class _PnniMetrics4_Type(Unsigned32):
    """Custom type pnniMetrics4 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics4_Object = MibTableColumn
pnniMetrics4 = _PnniMetrics4_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 10),
    _PnniMetrics4_Type()
)
pnniMetrics4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics4.setStatus("current")


class _PnniMetrics5_Type(Unsigned32):
    """Custom type pnniMetrics5 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics5_Object = MibTableColumn
pnniMetrics5 = _PnniMetrics5_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 11),
    _PnniMetrics5_Type()
)
pnniMetrics5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics5.setStatus("current")


class _PnniMetrics6_Type(Unsigned32):
    """Custom type pnniMetrics6 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics6_Object = MibTableColumn
pnniMetrics6 = _PnniMetrics6_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 12),
    _PnniMetrics6_Type()
)
pnniMetrics6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics6.setStatus("current")


class _PnniMetrics7_Type(Unsigned32):
    """Custom type pnniMetrics7 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics7_Object = MibTableColumn
pnniMetrics7 = _PnniMetrics7_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 13),
    _PnniMetrics7_Type()
)
pnniMetrics7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics7.setStatus("current")


class _PnniMetrics8_Type(Unsigned32):
    """Custom type pnniMetrics8 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniMetrics8_Object = MibTableColumn
pnniMetrics8 = _PnniMetrics8_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 14),
    _PnniMetrics8_Type()
)
pnniMetrics8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetrics8.setStatus("current")
_PnniMetricsRowStatus_Type = RowStatus
_PnniMetricsRowStatus_Object = MibTableColumn
pnniMetricsRowStatus = _PnniMetricsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 18, 1, 15),
    _PnniMetricsRowStatus_Type()
)
pnniMetricsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniMetricsRowStatus.setStatus("current")
_PnniRoutingGroup_ObjectIdentity = ObjectIdentity
pnniRoutingGroup = _PnniRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19)
)
_PnniRouteBaseGroup_ObjectIdentity = ObjectIdentity
pnniRouteBaseGroup = _PnniRouteBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 1)
)
_PnniRouteNodeNumber_Type = Gauge32
_PnniRouteNodeNumber_Object = MibScalar
pnniRouteNodeNumber = _PnniRouteNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 1, 1),
    _PnniRouteNodeNumber_Type()
)
pnniRouteNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeNumber.setStatus("current")
_PnniRouteAddrNumber_Type = Gauge32
_PnniRouteAddrNumber_Object = MibScalar
pnniRouteAddrNumber = _PnniRouteAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 1, 2),
    _PnniRouteAddrNumber_Type()
)
pnniRouteAddrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrNumber.setStatus("current")
_PnniRouteNodeTable_Object = MibTable
pnniRouteNodeTable = _PnniRouteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    pnniRouteNodeTable.setStatus("current")
_PnniRouteNodeEntry_Object = MibTableRow
pnniRouteNodeEntry = _PnniRouteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1)
)
pnniRouteNodeEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniRouteNodeClass"),
    (0, "PNNI-MIB", "pnniRouteNodeDestNodeId"),
    (0, "PNNI-MIB", "pnniRouteNodeDTL"),
)
if mibBuilder.loadTexts:
    pnniRouteNodeEntry.setStatus("current")
_PnniRouteNodeClass_Type = ServiceCategory
_PnniRouteNodeClass_Object = MibTableColumn
pnniRouteNodeClass = _PnniRouteNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 1),
    _PnniRouteNodeClass_Type()
)
pnniRouteNodeClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteNodeClass.setStatus("current")
_PnniRouteNodeDestNodeId_Type = PnniNodeId
_PnniRouteNodeDestNodeId_Object = MibTableColumn
pnniRouteNodeDestNodeId = _PnniRouteNodeDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 2),
    _PnniRouteNodeDestNodeId_Type()
)
pnniRouteNodeDestNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteNodeDestNodeId.setStatus("current")


class _PnniRouteNodeDTL_Type(Integer32):
    """Custom type pnniRouteNodeDTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniRouteNodeDTL_Type.__name__ = "Integer32"
_PnniRouteNodeDTL_Object = MibTableColumn
pnniRouteNodeDTL = _PnniRouteNodeDTL_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 3),
    _PnniRouteNodeDTL_Type()
)
pnniRouteNodeDTL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteNodeDTL.setStatus("current")


class _PnniRouteNodeDestPortId_Type(PnniPortId):
    """Custom type pnniRouteNodeDestPortId based on PnniPortId"""
    defaultValue = 0


_PnniRouteNodeDestPortId_Object = MibTableColumn
pnniRouteNodeDestPortId = _PnniRouteNodeDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 4),
    _PnniRouteNodeDestPortId_Type()
)
pnniRouteNodeDestPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeDestPortId.setStatus("current")


class _PnniRouteNodeProto_Type(Integer32):
    """Custom type pnniRouteNodeProto based on Integer32"""
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
        *(("local", 2),
          ("mgmt", 3),
          ("other", 1),
          ("pnni", 4))
    )


_PnniRouteNodeProto_Type.__name__ = "Integer32"
_PnniRouteNodeProto_Object = MibTableColumn
pnniRouteNodeProto = _PnniRouteNodeProto_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 5),
    _PnniRouteNodeProto_Type()
)
pnniRouteNodeProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeProto.setStatus("current")
_PnniRouteNodeTimeStamp_Type = TimeStamp
_PnniRouteNodeTimeStamp_Object = MibTableColumn
pnniRouteNodeTimeStamp = _PnniRouteNodeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 6),
    _PnniRouteNodeTimeStamp_Type()
)
pnniRouteNodeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteNodeTimeStamp.setStatus("current")


class _PnniRouteNodeInfo_Type(ObjectIdentifier):
    """Custom type pnniRouteNodeInfo based on ObjectIdentifier"""
    defaultValue = (0, 0)


_PnniRouteNodeInfo_Object = MibTableColumn
pnniRouteNodeInfo = _PnniRouteNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 7),
    _PnniRouteNodeInfo_Type()
)
pnniRouteNodeInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeInfo.setStatus("current")
_PnniRouteNodeGcacClp_Type = ClpType
_PnniRouteNodeGcacClp_Object = MibTableColumn
pnniRouteNodeGcacClp = _PnniRouteNodeGcacClp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 8),
    _PnniRouteNodeGcacClp_Type()
)
pnniRouteNodeGcacClp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeGcacClp.setStatus("current")


class _PnniRouteNodeFwdMetricAW_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetricAW based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetricAW_Object = MibTableColumn
pnniRouteNodeFwdMetricAW = _PnniRouteNodeFwdMetricAW_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 9),
    _PnniRouteNodeFwdMetricAW_Type()
)
pnniRouteNodeFwdMetricAW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetricAW.setStatus("current")


class _PnniRouteNodeFwdMetric1_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric1 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric1_Object = MibTableColumn
pnniRouteNodeFwdMetric1 = _PnniRouteNodeFwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 10),
    _PnniRouteNodeFwdMetric1_Type()
)
pnniRouteNodeFwdMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric1.setStatus("current")


class _PnniRouteNodeFwdMetric2_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric2 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric2_Object = MibTableColumn
pnniRouteNodeFwdMetric2 = _PnniRouteNodeFwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 11),
    _PnniRouteNodeFwdMetric2_Type()
)
pnniRouteNodeFwdMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric2.setStatus("current")


class _PnniRouteNodeFwdMetric3_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric3 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric3_Object = MibTableColumn
pnniRouteNodeFwdMetric3 = _PnniRouteNodeFwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 12),
    _PnniRouteNodeFwdMetric3_Type()
)
pnniRouteNodeFwdMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric3.setStatus("current")


class _PnniRouteNodeFwdMetric4_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric4 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric4_Object = MibTableColumn
pnniRouteNodeFwdMetric4 = _PnniRouteNodeFwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 13),
    _PnniRouteNodeFwdMetric4_Type()
)
pnniRouteNodeFwdMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric4.setStatus("current")


class _PnniRouteNodeFwdMetric5_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric5 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric5_Object = MibTableColumn
pnniRouteNodeFwdMetric5 = _PnniRouteNodeFwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 14),
    _PnniRouteNodeFwdMetric5_Type()
)
pnniRouteNodeFwdMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric5.setStatus("current")


class _PnniRouteNodeFwdMetric6_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric6 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric6_Object = MibTableColumn
pnniRouteNodeFwdMetric6 = _PnniRouteNodeFwdMetric6_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 15),
    _PnniRouteNodeFwdMetric6_Type()
)
pnniRouteNodeFwdMetric6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric6.setStatus("current")


class _PnniRouteNodeFwdMetric7_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric7 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric7_Object = MibTableColumn
pnniRouteNodeFwdMetric7 = _PnniRouteNodeFwdMetric7_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 16),
    _PnniRouteNodeFwdMetric7_Type()
)
pnniRouteNodeFwdMetric7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric7.setStatus("current")


class _PnniRouteNodeFwdMetric8_Type(Unsigned32):
    """Custom type pnniRouteNodeFwdMetric8 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeFwdMetric8_Object = MibTableColumn
pnniRouteNodeFwdMetric8 = _PnniRouteNodeFwdMetric8_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 17),
    _PnniRouteNodeFwdMetric8_Type()
)
pnniRouteNodeFwdMetric8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeFwdMetric8.setStatus("current")


class _PnniRouteNodeBwdMetricAW_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetricAW based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetricAW_Object = MibTableColumn
pnniRouteNodeBwdMetricAW = _PnniRouteNodeBwdMetricAW_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 18),
    _PnniRouteNodeBwdMetricAW_Type()
)
pnniRouteNodeBwdMetricAW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetricAW.setStatus("current")


class _PnniRouteNodeBwdMetric1_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric1 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric1_Object = MibTableColumn
pnniRouteNodeBwdMetric1 = _PnniRouteNodeBwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 19),
    _PnniRouteNodeBwdMetric1_Type()
)
pnniRouteNodeBwdMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric1.setStatus("current")


class _PnniRouteNodeBwdMetric2_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric2 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric2_Object = MibTableColumn
pnniRouteNodeBwdMetric2 = _PnniRouteNodeBwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 20),
    _PnniRouteNodeBwdMetric2_Type()
)
pnniRouteNodeBwdMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric2.setStatus("current")


class _PnniRouteNodeBwdMetric3_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric3 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric3_Object = MibTableColumn
pnniRouteNodeBwdMetric3 = _PnniRouteNodeBwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 21),
    _PnniRouteNodeBwdMetric3_Type()
)
pnniRouteNodeBwdMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric3.setStatus("current")


class _PnniRouteNodeBwdMetric4_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric4 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric4_Object = MibTableColumn
pnniRouteNodeBwdMetric4 = _PnniRouteNodeBwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 22),
    _PnniRouteNodeBwdMetric4_Type()
)
pnniRouteNodeBwdMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric4.setStatus("current")


class _PnniRouteNodeBwdMetric5_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric5 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric5_Object = MibTableColumn
pnniRouteNodeBwdMetric5 = _PnniRouteNodeBwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 23),
    _PnniRouteNodeBwdMetric5_Type()
)
pnniRouteNodeBwdMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric5.setStatus("current")


class _PnniRouteNodeBwdMetric6_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric6 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric6_Object = MibTableColumn
pnniRouteNodeBwdMetric6 = _PnniRouteNodeBwdMetric6_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 24),
    _PnniRouteNodeBwdMetric6_Type()
)
pnniRouteNodeBwdMetric6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric6.setStatus("current")


class _PnniRouteNodeBwdMetric7_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric7 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric7_Object = MibTableColumn
pnniRouteNodeBwdMetric7 = _PnniRouteNodeBwdMetric7_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 25),
    _PnniRouteNodeBwdMetric7_Type()
)
pnniRouteNodeBwdMetric7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric7.setStatus("current")


class _PnniRouteNodeBwdMetric8_Type(Unsigned32):
    """Custom type pnniRouteNodeBwdMetric8 based on Unsigned32"""
    defaultHexValue = 4294967295


_PnniRouteNodeBwdMetric8_Object = MibTableColumn
pnniRouteNodeBwdMetric8 = _PnniRouteNodeBwdMetric8_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 26),
    _PnniRouteNodeBwdMetric8_Type()
)
pnniRouteNodeBwdMetric8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeBwdMetric8.setStatus("current")
_PnniRouteNodeVPCapability_Type = TruthValue
_PnniRouteNodeVPCapability_Object = MibTableColumn
pnniRouteNodeVPCapability = _PnniRouteNodeVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 27),
    _PnniRouteNodeVPCapability_Type()
)
pnniRouteNodeVPCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeVPCapability.setStatus("current")
_PnniRouteNodeStatus_Type = RowStatus
_PnniRouteNodeStatus_Object = MibTableColumn
pnniRouteNodeStatus = _PnniRouteNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 2, 1, 28),
    _PnniRouteNodeStatus_Type()
)
pnniRouteNodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteNodeStatus.setStatus("current")
_PnniDTLTable_Object = MibTable
pnniDTLTable = _PnniDTLTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    pnniDTLTable.setStatus("current")
_PnniDTLEntry_Object = MibTableRow
pnniDTLEntry = _PnniDTLEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1)
)
pnniDTLEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniDTLIndex"),
    (0, "PNNI-MIB", "pnniDTLEntryIndex"),
)
if mibBuilder.loadTexts:
    pnniDTLEntry.setStatus("current")


class _PnniDTLIndex_Type(Integer32):
    """Custom type pnniDTLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnniDTLIndex_Type.__name__ = "Integer32"
_PnniDTLIndex_Object = MibTableColumn
pnniDTLIndex = _PnniDTLIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 1),
    _PnniDTLIndex_Type()
)
pnniDTLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniDTLIndex.setStatus("current")


class _PnniDTLEntryIndex_Type(Integer32):
    """Custom type pnniDTLEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PnniDTLEntryIndex_Type.__name__ = "Integer32"
_PnniDTLEntryIndex_Object = MibTableColumn
pnniDTLEntryIndex = _PnniDTLEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 2),
    _PnniDTLEntryIndex_Type()
)
pnniDTLEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniDTLEntryIndex.setStatus("current")
_PnniDTLNodeId_Type = PnniNodeId
_PnniDTLNodeId_Object = MibTableColumn
pnniDTLNodeId = _PnniDTLNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 3),
    _PnniDTLNodeId_Type()
)
pnniDTLNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDTLNodeId.setStatus("current")
_PnniDTLPortId_Type = PnniPortId
_PnniDTLPortId_Object = MibTableColumn
pnniDTLPortId = _PnniDTLPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 4),
    _PnniDTLPortId_Type()
)
pnniDTLPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDTLPortId.setStatus("current")


class _PnniDTLLinkType_Type(Integer32):
    """Custom type pnniDTLLinkType based on Integer32"""
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
        *(("horizontal", 2),
          ("invalid", 1),
          ("last", 4),
          ("uplink", 3))
    )


_PnniDTLLinkType_Type.__name__ = "Integer32"
_PnniDTLLinkType_Object = MibTableColumn
pnniDTLLinkType = _PnniDTLLinkType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 5),
    _PnniDTLLinkType_Type()
)
pnniDTLLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDTLLinkType.setStatus("current")
_PnniDTLStatus_Type = RowStatus
_PnniDTLStatus_Object = MibTableColumn
pnniDTLStatus = _PnniDTLStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 3, 1, 6),
    _PnniDTLStatus_Type()
)
pnniDTLStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniDTLStatus.setStatus("current")
_PnniRouteAddrTable_Object = MibTable
pnniRouteAddrTable = _PnniRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    pnniRouteAddrTable.setStatus("current")
_PnniRouteAddrEntry_Object = MibTableRow
pnniRouteAddrEntry = _PnniRouteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1)
)
pnniRouteAddrEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniRouteAddrAddress"),
    (0, "PNNI-MIB", "pnniRouteAddrPrefixLength"),
    (0, "PNNI-MIB", "pnniRouteAddrIndex"),
)
if mibBuilder.loadTexts:
    pnniRouteAddrEntry.setStatus("current")
_PnniRouteAddrAddress_Type = AtmAddrPrefix
_PnniRouteAddrAddress_Object = MibTableColumn
pnniRouteAddrAddress = _PnniRouteAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 1),
    _PnniRouteAddrAddress_Type()
)
pnniRouteAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteAddrAddress.setStatus("current")
_PnniRouteAddrPrefixLength_Type = PnniPrefixLength
_PnniRouteAddrPrefixLength_Object = MibTableColumn
pnniRouteAddrPrefixLength = _PnniRouteAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 2),
    _PnniRouteAddrPrefixLength_Type()
)
pnniRouteAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteAddrPrefixLength.setStatus("current")


class _PnniRouteAddrIndex_Type(Integer32):
    """Custom type pnniRouteAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniRouteAddrIndex_Type.__name__ = "Integer32"
_PnniRouteAddrIndex_Object = MibTableColumn
pnniRouteAddrIndex = _PnniRouteAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 3),
    _PnniRouteAddrIndex_Type()
)
pnniRouteAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteAddrIndex.setStatus("current")
_PnniRouteAddrIfIndex_Type = InterfaceIndex
_PnniRouteAddrIfIndex_Object = MibTableColumn
pnniRouteAddrIfIndex = _PnniRouteAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 4),
    _PnniRouteAddrIfIndex_Type()
)
pnniRouteAddrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrIfIndex.setStatus("current")
_PnniRouteAddrAdvertisingNodeId_Type = PnniNodeId
_PnniRouteAddrAdvertisingNodeId_Object = MibTableColumn
pnniRouteAddrAdvertisingNodeId = _PnniRouteAddrAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 5),
    _PnniRouteAddrAdvertisingNodeId_Type()
)
pnniRouteAddrAdvertisingNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrAdvertisingNodeId.setStatus("current")


class _PnniRouteAddrAdvertisedPortId_Type(PnniPortId):
    """Custom type pnniRouteAddrAdvertisedPortId based on PnniPortId"""
    defaultValue = 0


_PnniRouteAddrAdvertisedPortId_Object = MibTableColumn
pnniRouteAddrAdvertisedPortId = _PnniRouteAddrAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 6),
    _PnniRouteAddrAdvertisedPortId_Type()
)
pnniRouteAddrAdvertisedPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrAdvertisedPortId.setStatus("current")


class _PnniRouteAddrType_Type(Integer32):
    """Custom type pnniRouteAddrType based on Integer32"""
    defaultValue = 4

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
        *(("exterior", 4),
          ("internal", 3),
          ("other", 1),
          ("reject", 2))
    )


_PnniRouteAddrType_Type.__name__ = "Integer32"
_PnniRouteAddrType_Object = MibTableColumn
pnniRouteAddrType = _PnniRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 7),
    _PnniRouteAddrType_Type()
)
pnniRouteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrType.setStatus("current")


class _PnniRouteAddrProto_Type(Integer32):
    """Custom type pnniRouteAddrProto based on Integer32"""
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
        *(("local", 2),
          ("mgmt", 3),
          ("other", 1),
          ("pnni", 4))
    )


_PnniRouteAddrProto_Type.__name__ = "Integer32"
_PnniRouteAddrProto_Object = MibTableColumn
pnniRouteAddrProto = _PnniRouteAddrProto_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 8),
    _PnniRouteAddrProto_Type()
)
pnniRouteAddrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrProto.setStatus("current")
_PnniRouteAddrPnniScope_Type = PnniLevel
_PnniRouteAddrPnniScope_Object = MibTableColumn
pnniRouteAddrPnniScope = _PnniRouteAddrPnniScope_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 9),
    _PnniRouteAddrPnniScope_Type()
)
pnniRouteAddrPnniScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrPnniScope.setStatus("current")
_PnniRouteAddrVPCapability_Type = TruthValue
_PnniRouteAddrVPCapability_Object = MibTableColumn
pnniRouteAddrVPCapability = _PnniRouteAddrVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 10),
    _PnniRouteAddrVPCapability_Type()
)
pnniRouteAddrVPCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrVPCapability.setStatus("current")


class _PnniRouteAddrMetricsTag_Type(PnniMetricsTag):
    """Custom type pnniRouteAddrMetricsTag based on PnniMetricsTag"""
    defaultValue = 0


_PnniRouteAddrMetricsTag_Object = MibTableColumn
pnniRouteAddrMetricsTag = _PnniRouteAddrMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 11),
    _PnniRouteAddrMetricsTag_Type()
)
pnniRouteAddrMetricsTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrMetricsTag.setStatus("current")
_PnniRouteAddrPtseId_Type = Unsigned32
_PnniRouteAddrPtseId_Object = MibTableColumn
pnniRouteAddrPtseId = _PnniRouteAddrPtseId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 12),
    _PnniRouteAddrPtseId_Type()
)
pnniRouteAddrPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrPtseId.setStatus("current")


class _PnniRouteAddrOriginateAdvertisement_Type(TruthValue):
    """Custom type pnniRouteAddrOriginateAdvertisement based on TruthValue"""


_PnniRouteAddrOriginateAdvertisement_Object = MibTableColumn
pnniRouteAddrOriginateAdvertisement = _PnniRouteAddrOriginateAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 13),
    _PnniRouteAddrOriginateAdvertisement_Type()
)
pnniRouteAddrOriginateAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrOriginateAdvertisement.setStatus("current")


class _PnniRouteAddrInfo_Type(ObjectIdentifier):
    """Custom type pnniRouteAddrInfo based on ObjectIdentifier"""
    defaultValue = (0, 0)


_PnniRouteAddrInfo_Object = MibTableColumn
pnniRouteAddrInfo = _PnniRouteAddrInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 14),
    _PnniRouteAddrInfo_Type()
)
pnniRouteAddrInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrInfo.setStatus("current")


class _PnniRouteAddrOperStatus_Type(Integer32):
    """Custom type pnniRouteAddrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("advertised", 3),
          ("inactive", 1))
    )


_PnniRouteAddrOperStatus_Type.__name__ = "Integer32"
_PnniRouteAddrOperStatus_Object = MibTableColumn
pnniRouteAddrOperStatus = _PnniRouteAddrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 15),
    _PnniRouteAddrOperStatus_Type()
)
pnniRouteAddrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrOperStatus.setStatus("current")
_PnniRouteAddrTimeStamp_Type = TimeStamp
_PnniRouteAddrTimeStamp_Object = MibTableColumn
pnniRouteAddrTimeStamp = _PnniRouteAddrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 16),
    _PnniRouteAddrTimeStamp_Type()
)
pnniRouteAddrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteAddrTimeStamp.setStatus("current")
_PnniRouteAddrRowStatus_Type = RowStatus
_PnniRouteAddrRowStatus_Object = MibTableColumn
pnniRouteAddrRowStatus = _PnniRouteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 4, 1, 17),
    _PnniRouteAddrRowStatus_Type()
)
pnniRouteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteAddrRowStatus.setStatus("current")
_PnniRouteTnsTable_Object = MibTable
pnniRouteTnsTable = _PnniRouteTnsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5)
)
if mibBuilder.loadTexts:
    pnniRouteTnsTable.setStatus("current")
_PnniRouteTnsEntry_Object = MibTableRow
pnniRouteTnsEntry = _PnniRouteTnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1)
)
pnniRouteTnsEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniRouteTnsType"),
    (0, "PNNI-MIB", "pnniRouteTnsPlan"),
    (0, "PNNI-MIB", "pnniRouteTnsId"),
    (0, "PNNI-MIB", "pnniRouteTnsIndex"),
)
if mibBuilder.loadTexts:
    pnniRouteTnsEntry.setStatus("current")
_PnniRouteTnsType_Type = TnsType
_PnniRouteTnsType_Object = MibTableColumn
pnniRouteTnsType = _PnniRouteTnsType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 1),
    _PnniRouteTnsType_Type()
)
pnniRouteTnsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteTnsType.setStatus("current")
_PnniRouteTnsPlan_Type = TnsPlan
_PnniRouteTnsPlan_Object = MibTableColumn
pnniRouteTnsPlan = _PnniRouteTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 2),
    _PnniRouteTnsPlan_Type()
)
pnniRouteTnsPlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteTnsPlan.setStatus("current")
_PnniRouteTnsId_Type = DisplayString
_PnniRouteTnsId_Object = MibTableColumn
pnniRouteTnsId = _PnniRouteTnsId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 3),
    _PnniRouteTnsId_Type()
)
pnniRouteTnsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteTnsId.setStatus("current")


class _PnniRouteTnsIndex_Type(Integer32):
    """Custom type pnniRouteTnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnniRouteTnsIndex_Type.__name__ = "Integer32"
_PnniRouteTnsIndex_Object = MibTableColumn
pnniRouteTnsIndex = _PnniRouteTnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 4),
    _PnniRouteTnsIndex_Type()
)
pnniRouteTnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniRouteTnsIndex.setStatus("current")
_PnniRouteTnsIfIndex_Type = InterfaceIndex
_PnniRouteTnsIfIndex_Object = MibTableColumn
pnniRouteTnsIfIndex = _PnniRouteTnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 5),
    _PnniRouteTnsIfIndex_Type()
)
pnniRouteTnsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsIfIndex.setStatus("current")
_PnniRouteTnsAdvertisingNodeId_Type = PnniNodeId
_PnniRouteTnsAdvertisingNodeId_Object = MibTableColumn
pnniRouteTnsAdvertisingNodeId = _PnniRouteTnsAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 6),
    _PnniRouteTnsAdvertisingNodeId_Type()
)
pnniRouteTnsAdvertisingNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsAdvertisingNodeId.setStatus("current")


class _PnniRouteTnsAdvertisedPortId_Type(PnniPortId):
    """Custom type pnniRouteTnsAdvertisedPortId based on PnniPortId"""
    defaultValue = 0


_PnniRouteTnsAdvertisedPortId_Object = MibTableColumn
pnniRouteTnsAdvertisedPortId = _PnniRouteTnsAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 7),
    _PnniRouteTnsAdvertisedPortId_Type()
)
pnniRouteTnsAdvertisedPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsAdvertisedPortId.setStatus("current")


class _PnniRouteTnsRouteType_Type(Integer32):
    """Custom type pnniRouteTnsRouteType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 4),
          ("other", 1))
    )


_PnniRouteTnsRouteType_Type.__name__ = "Integer32"
_PnniRouteTnsRouteType_Object = MibTableColumn
pnniRouteTnsRouteType = _PnniRouteTnsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 8),
    _PnniRouteTnsRouteType_Type()
)
pnniRouteTnsRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsRouteType.setStatus("current")


class _PnniRouteTnsProto_Type(Integer32):
    """Custom type pnniRouteTnsProto based on Integer32"""
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
        *(("local", 2),
          ("mgmt", 3),
          ("other", 1),
          ("pnni", 4))
    )


_PnniRouteTnsProto_Type.__name__ = "Integer32"
_PnniRouteTnsProto_Object = MibTableColumn
pnniRouteTnsProto = _PnniRouteTnsProto_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 9),
    _PnniRouteTnsProto_Type()
)
pnniRouteTnsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsProto.setStatus("current")
_PnniRouteTnsPnniScope_Type = PnniLevel
_PnniRouteTnsPnniScope_Object = MibTableColumn
pnniRouteTnsPnniScope = _PnniRouteTnsPnniScope_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 10),
    _PnniRouteTnsPnniScope_Type()
)
pnniRouteTnsPnniScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsPnniScope.setStatus("current")
_PnniRouteTnsVPCapability_Type = TruthValue
_PnniRouteTnsVPCapability_Object = MibTableColumn
pnniRouteTnsVPCapability = _PnniRouteTnsVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 11),
    _PnniRouteTnsVPCapability_Type()
)
pnniRouteTnsVPCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsVPCapability.setStatus("current")


class _PnniRouteTnsMetricsTag_Type(PnniMetricsTag):
    """Custom type pnniRouteTnsMetricsTag based on PnniMetricsTag"""
    defaultValue = 0


_PnniRouteTnsMetricsTag_Object = MibTableColumn
pnniRouteTnsMetricsTag = _PnniRouteTnsMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 12),
    _PnniRouteTnsMetricsTag_Type()
)
pnniRouteTnsMetricsTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsMetricsTag.setStatus("current")
_PnniRouteTnsPtseId_Type = Unsigned32
_PnniRouteTnsPtseId_Object = MibTableColumn
pnniRouteTnsPtseId = _PnniRouteTnsPtseId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 13),
    _PnniRouteTnsPtseId_Type()
)
pnniRouteTnsPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsPtseId.setStatus("current")


class _PnniRouteTnsOriginateAdvertisement_Type(TruthValue):
    """Custom type pnniRouteTnsOriginateAdvertisement based on TruthValue"""


_PnniRouteTnsOriginateAdvertisement_Object = MibTableColumn
pnniRouteTnsOriginateAdvertisement = _PnniRouteTnsOriginateAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 14),
    _PnniRouteTnsOriginateAdvertisement_Type()
)
pnniRouteTnsOriginateAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsOriginateAdvertisement.setStatus("current")


class _PnniRouteTnsInfo_Type(ObjectIdentifier):
    """Custom type pnniRouteTnsInfo based on ObjectIdentifier"""
    defaultValue = (0, 0)


_PnniRouteTnsInfo_Object = MibTableColumn
pnniRouteTnsInfo = _PnniRouteTnsInfo_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 15),
    _PnniRouteTnsInfo_Type()
)
pnniRouteTnsInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsInfo.setStatus("current")


class _PnniRouteTnsOperStatus_Type(Integer32):
    """Custom type pnniRouteTnsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("advertised", 3),
          ("inactive", 1))
    )


_PnniRouteTnsOperStatus_Type.__name__ = "Integer32"
_PnniRouteTnsOperStatus_Object = MibTableColumn
pnniRouteTnsOperStatus = _PnniRouteTnsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 16),
    _PnniRouteTnsOperStatus_Type()
)
pnniRouteTnsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsOperStatus.setStatus("current")
_PnniRouteTnsTimeStamp_Type = TimeStamp
_PnniRouteTnsTimeStamp_Object = MibTableColumn
pnniRouteTnsTimeStamp = _PnniRouteTnsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 17),
    _PnniRouteTnsTimeStamp_Type()
)
pnniRouteTnsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniRouteTnsTimeStamp.setStatus("current")
_PnniRouteTnsRowStatus_Type = RowStatus
_PnniRouteTnsRowStatus_Object = MibTableColumn
pnniRouteTnsRowStatus = _PnniRouteTnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 19, 5, 1, 18),
    _PnniRouteTnsRowStatus_Type()
)
pnniRouteTnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniRouteTnsRowStatus.setStatus("current")
_PnniSummaryAddressTable_Object = MibTable
pnniSummaryAddressTable = _PnniSummaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    pnniSummaryAddressTable.setStatus("current")
_PnniSummaryAddressEntry_Object = MibTableRow
pnniSummaryAddressEntry = _PnniSummaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1)
)
pnniSummaryAddressEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniSummaryAddressType"),
    (0, "PNNI-MIB", "pnniSummaryAddressAddress"),
    (0, "PNNI-MIB", "pnniSummaryAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    pnniSummaryAddressEntry.setStatus("current")


class _PnniSummaryAddressType_Type(Integer32):
    """Custom type pnniSummaryAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 2),
          ("internal", 1))
    )


_PnniSummaryAddressType_Type.__name__ = "Integer32"
_PnniSummaryAddressType_Object = MibTableColumn
pnniSummaryAddressType = _PnniSummaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 1),
    _PnniSummaryAddressType_Type()
)
pnniSummaryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSummaryAddressType.setStatus("current")
_PnniSummaryAddressAddress_Type = AtmAddrPrefix
_PnniSummaryAddressAddress_Object = MibTableColumn
pnniSummaryAddressAddress = _PnniSummaryAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 2),
    _PnniSummaryAddressAddress_Type()
)
pnniSummaryAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSummaryAddressAddress.setStatus("current")
_PnniSummaryAddressPrefixLength_Type = PnniPrefixLength
_PnniSummaryAddressPrefixLength_Object = MibTableColumn
pnniSummaryAddressPrefixLength = _PnniSummaryAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 3),
    _PnniSummaryAddressPrefixLength_Type()
)
pnniSummaryAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniSummaryAddressPrefixLength.setStatus("current")


class _PnniSummaryAddressSuppress_Type(TruthValue):
    """Custom type pnniSummaryAddressSuppress based on TruthValue"""


_PnniSummaryAddressSuppress_Object = MibTableColumn
pnniSummaryAddressSuppress = _PnniSummaryAddressSuppress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 4),
    _PnniSummaryAddressSuppress_Type()
)
pnniSummaryAddressSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSummaryAddressSuppress.setStatus("current")


class _PnniSummaryAddressState_Type(Integer32):
    """Custom type pnniSummaryAddressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 1),
          ("inactive", 3),
          ("suppressing", 2))
    )


_PnniSummaryAddressState_Type.__name__ = "Integer32"
_PnniSummaryAddressState_Object = MibTableColumn
pnniSummaryAddressState = _PnniSummaryAddressState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 5),
    _PnniSummaryAddressState_Type()
)
pnniSummaryAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniSummaryAddressState.setStatus("current")
_PnniSummaryAddressRowStatus_Type = RowStatus
_PnniSummaryAddressRowStatus_Object = MibTableColumn
pnniSummaryAddressRowStatus = _PnniSummaryAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 1, 20, 1, 6),
    _PnniSummaryAddressRowStatus_Type()
)
pnniSummaryAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pnniSummaryAddressRowStatus.setStatus("current")
_PnniMIBConformance_ObjectIdentity = ObjectIdentity
pnniMIBConformance = _PnniMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2)
)
_PnniMIBCompliances_ObjectIdentity = ObjectIdentity
pnniMIBCompliances = _PnniMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 1)
)
_PnniMIBGroups_ObjectIdentity = ObjectIdentity
pnniMIBGroups = _PnniMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2)
)
pnniNodeEntry.registerAugmentions(
    ("PNNI-MIB",
     "pnniNodePglEntry")
)
pnniNodePglEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniNodeEntry.registerAugmentions(
    ("PNNI-MIB",
     "pnniNodeTimerEntry")
)
pnniNodeTimerEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniNodeEntry.registerAugmentions(
    ("PNNI-MIB",
     "pnniNodeSvccEntry")
)
pnniNodeSvccEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniNodeEntry.registerAugmentions(
    ("PNNI-MIB",
     "pnniScopeMappingEntry")
)
pnniScopeMappingEntry.setIndexNames(*pnniNodeEntry.getIndexNames())

# Managed Objects groups

pnniGeneralMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 1)
)
pnniGeneralMinGroup.setObjects(
      *(("PNNI-MIB", "pnniHighestVersion"),
        ("PNNI-MIB", "pnniLowestVersion"),
        ("PNNI-MIB", "pnniDtlCountOriginator"),
        ("PNNI-MIB", "pnniCrankbackCountOriginator"),
        ("PNNI-MIB", "pnniAltRouteCountOriginator"),
        ("PNNI-MIB", "pnniRouteFailCountOriginator"),
        ("PNNI-MIB", "pnniRouteFailUnreachableOriginator"))
)
if mibBuilder.loadTexts:
    pnniGeneralMinGroup.setStatus("current")

pnniGeneralBorderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 2)
)
pnniGeneralBorderGroup.setObjects(
      *(("PNNI-MIB", "pnniDtlCountBorder"),
        ("PNNI-MIB", "pnniCrankbackCountBorder"),
        ("PNNI-MIB", "pnniAltRouteCountBorder"),
        ("PNNI-MIB", "pnniRouteFailCountBorder"),
        ("PNNI-MIB", "pnniRouteFailUnreachableBorder"))
)
if mibBuilder.loadTexts:
    pnniGeneralBorderGroup.setStatus("current")

pnniNodeMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 3)
)
pnniNodeMinGroup.setObjects(
      *(("PNNI-MIB", "pnniNodeLevel"),
        ("PNNI-MIB", "pnniNodeId"),
        ("PNNI-MIB", "pnniNodeLowest"),
        ("PNNI-MIB", "pnniNodeAdminStatus"),
        ("PNNI-MIB", "pnniNodeOperStatus"),
        ("PNNI-MIB", "pnniNodeDomainName"),
        ("PNNI-MIB", "pnniNodeAtmAddress"),
        ("PNNI-MIB", "pnniNodePeerGroupId"),
        ("PNNI-MIB", "pnniNodeRestrictedTransit"),
        ("PNNI-MIB", "pnniNodeComplexRep"),
        ("PNNI-MIB", "pnniNodeRestrictedBranching"),
        ("PNNI-MIB", "pnniNodeDatabaseOverload"),
        ("PNNI-MIB", "pnniNodePtses"),
        ("PNNI-MIB", "pnniNodeRowStatus"))
)
if mibBuilder.loadTexts:
    pnniNodeMinGroup.setStatus("current")

pnniNodePglMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 4)
)
pnniNodePglMinGroup.setObjects(
      *(("PNNI-MIB", "pnniNodePglLeadershipPriority"),
        ("PNNI-MIB", "pnniNodePglInitTime"),
        ("PNNI-MIB", "pnniNodePglReelectTime"),
        ("PNNI-MIB", "pnniNodePglState"),
        ("PNNI-MIB", "pnniNodePreferredPgl"),
        ("PNNI-MIB", "pnniNodePeerGroupLeader"),
        ("PNNI-MIB", "pnniNodePglTimeStamp"),
        ("PNNI-MIB", "pnniNodeActiveParentNodeId"))
)
if mibBuilder.loadTexts:
    pnniNodePglMinGroup.setStatus("current")

pnniNodePglLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 5)
)
pnniNodePglLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniNodeCfgParentNodeIndex"),
        ("PNNI-MIB", "pnniNodePglOverrideDelay"))
)
if mibBuilder.loadTexts:
    pnniNodePglLgnGroup.setStatus("current")

pnniNodeTimerMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 6)
)
pnniNodeTimerMinGroup.setObjects(
      *(("PNNI-MIB", "pnniNodePtseHolddown"),
        ("PNNI-MIB", "pnniNodeHelloHolddown"),
        ("PNNI-MIB", "pnniNodeHelloInterval"),
        ("PNNI-MIB", "pnniNodeHelloInactivityFactor"),
        ("PNNI-MIB", "pnniNodePtseRefreshInterval"),
        ("PNNI-MIB", "pnniNodePtseLifetimeFactor"),
        ("PNNI-MIB", "pnniNodeRxmtInterval"),
        ("PNNI-MIB", "pnniNodePeerDelayedAckInterval"),
        ("PNNI-MIB", "pnniNodeAvcrPm"),
        ("PNNI-MIB", "pnniNodeAvcrMt"),
        ("PNNI-MIB", "pnniNodeCdvPm"),
        ("PNNI-MIB", "pnniNodeCtdPm"))
)
if mibBuilder.loadTexts:
    pnniNodeTimerMinGroup.setStatus("current")

pnniNodeTimerLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 7)
)
pnniNodeTimerLgnGroup.setObjects(
    ("PNNI-MIB", "pnniNodeHlinkInact")
)
if mibBuilder.loadTexts:
    pnniNodeTimerLgnGroup.setStatus("current")

pnniNodeSvccLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 8)
)
pnniNodeSvccLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniNodeSvccInitTime"),
        ("PNNI-MIB", "pnniNodeSvccRetryTime"),
        ("PNNI-MIB", "pnniNodeSvccCallingIntegrityTime"),
        ("PNNI-MIB", "pnniNodeSvccCalledIntegrityTime"),
        ("PNNI-MIB", "pnniNodeSvccTrafficDescriptorIndex"))
)
if mibBuilder.loadTexts:
    pnniNodeSvccLgnGroup.setStatus("current")

pnniScopeMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 9)
)
pnniScopeMinGroup.setObjects(
      *(("PNNI-MIB", "pnniScopeLocalNetwork"),
        ("PNNI-MIB", "pnniScopeLocalNetworkPlusOne"),
        ("PNNI-MIB", "pnniScopeLocalNetworkPlusTwo"),
        ("PNNI-MIB", "pnniScopeSiteMinusOne"),
        ("PNNI-MIB", "pnniScopeIntraSite"),
        ("PNNI-MIB", "pnniScopeSitePlusOne"),
        ("PNNI-MIB", "pnniScopeOrganizationMinusOne"),
        ("PNNI-MIB", "pnniScopeIntraOrganization"),
        ("PNNI-MIB", "pnniScopeOrganizationPlusOne"),
        ("PNNI-MIB", "pnniScopeCommunityMinusOne"),
        ("PNNI-MIB", "pnniScopeIntraCommunity"),
        ("PNNI-MIB", "pnniScopeCommunityPlusOne"),
        ("PNNI-MIB", "pnniScopeRegional"),
        ("PNNI-MIB", "pnniScopeInterRegional"),
        ("PNNI-MIB", "pnniScopeGlobal"))
)
if mibBuilder.loadTexts:
    pnniScopeMinGroup.setStatus("current")

pnniSummaryLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 10)
)
pnniSummaryLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniSummaryType"),
        ("PNNI-MIB", "pnniSummarySuppress"),
        ("PNNI-MIB", "pnniSummaryState"),
        ("PNNI-MIB", "pnniSummaryRowStatus"))
)
if mibBuilder.loadTexts:
    pnniSummaryLgnGroup.setStatus("deprecated")

pnniIfMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 11)
)
pnniIfMinGroup.setObjects(
      *(("PNNI-MIB", "pnniIfNodeIndex"),
        ("PNNI-MIB", "pnniIfPortId"),
        ("PNNI-MIB", "pnniIfVPCapability"),
        ("PNNI-MIB", "pnniIfAdmWeightCbr"),
        ("PNNI-MIB", "pnniIfAdmWeightRtVbr"),
        ("PNNI-MIB", "pnniIfAdmWeightNrtVbr"),
        ("PNNI-MIB", "pnniIfAdmWeightAbr"),
        ("PNNI-MIB", "pnniIfAdmWeightUbr"),
        ("PNNI-MIB", "pnniIfRccServiceCategory"),
        ("PNNI-MIB", "pnniIfRccTrafficDescrIndex"))
)
if mibBuilder.loadTexts:
    pnniIfMinGroup.setStatus("current")

pnniIfBorderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 12)
)
pnniIfBorderGroup.setObjects(
    ("PNNI-MIB", "pnniIfAggrToken")
)
if mibBuilder.loadTexts:
    pnniIfBorderGroup.setStatus("current")

pnniLinkMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 13)
)
pnniLinkMinGroup.setObjects(
      *(("PNNI-MIB", "pnniLinkType"),
        ("PNNI-MIB", "pnniLinkVersion"),
        ("PNNI-MIB", "pnniLinkHelloState"),
        ("PNNI-MIB", "pnniLinkRemoteNodeId"),
        ("PNNI-MIB", "pnniLinkRemotePortId"),
        ("PNNI-MIB", "pnniLinkIfIndex"),
        ("PNNI-MIB", "pnniLinkRcvHellos"),
        ("PNNI-MIB", "pnniLinkXmtHellos"))
)
if mibBuilder.loadTexts:
    pnniLinkMinGroup.setStatus("current")

pnniLinkBorderOrLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 14)
)
pnniLinkBorderOrLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniLinkDerivedAggrToken"),
        ("PNNI-MIB", "pnniLinkUpnodeId"),
        ("PNNI-MIB", "pnniLinkUpnodeAtmAddress"),
        ("PNNI-MIB", "pnniLinkCommonPeerGroupId"))
)
if mibBuilder.loadTexts:
    pnniLinkBorderOrLgnGroup.setStatus("current")

pnniLinkLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 15)
)
pnniLinkLgnGroup.setObjects(
    ("PNNI-MIB", "pnniLinkSvccRccIndex")
)
if mibBuilder.loadTexts:
    pnniLinkLgnGroup.setStatus("current")

pnniNbrPeerMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 16)
)
pnniNbrPeerMinGroup.setObjects(
      *(("PNNI-MIB", "pnniNbrPeerState"),
        ("PNNI-MIB", "pnniNbrPeerPortCount"),
        ("PNNI-MIB", "pnniNbrPeerRcvDbSums"),
        ("PNNI-MIB", "pnniNbrPeerXmtDbSums"),
        ("PNNI-MIB", "pnniNbrPeerRcvPtsps"),
        ("PNNI-MIB", "pnniNbrPeerXmtPtsps"),
        ("PNNI-MIB", "pnniNbrPeerRcvPtseReqs"),
        ("PNNI-MIB", "pnniNbrPeerXmtPtseReqs"),
        ("PNNI-MIB", "pnniNbrPeerRcvPtseAcks"),
        ("PNNI-MIB", "pnniNbrPeerXmtPtseAcks"))
)
if mibBuilder.loadTexts:
    pnniNbrPeerMinGroup.setStatus("current")

pnniNbrPeerLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 17)
)
pnniNbrPeerLgnGroup.setObjects(
    ("PNNI-MIB", "pnniNbrPeerSvccRccIndex")
)
if mibBuilder.loadTexts:
    pnniNbrPeerLgnGroup.setStatus("current")

pnniNbrPeerPortMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 18)
)
pnniNbrPeerPortMinGroup.setObjects(
    ("PNNI-MIB", "pnniNbrPeerPortFloodStatus")
)
if mibBuilder.loadTexts:
    pnniNbrPeerPortMinGroup.setStatus("current")

pnniSvccRccLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 19)
)
pnniSvccRccLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniSvccRccVersion"),
        ("PNNI-MIB", "pnniSvccRccHelloState"),
        ("PNNI-MIB", "pnniSvccRccRemoteNodeId"),
        ("PNNI-MIB", "pnniSvccRccRemoteAtmAddress"),
        ("PNNI-MIB", "pnniSvccRccRcvHellos"),
        ("PNNI-MIB", "pnniSvccRccXmtHellos"),
        ("PNNI-MIB", "pnniSvccRccIfIndex"),
        ("PNNI-MIB", "pnniSvccRccVpi"),
        ("PNNI-MIB", "pnniSvccRccVci"))
)
if mibBuilder.loadTexts:
    pnniSvccRccLgnGroup.setStatus("current")

pnniPtseOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 20)
)
pnniPtseOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniPtseType"),
        ("PNNI-MIB", "pnniPtseSequenceNum"),
        ("PNNI-MIB", "pnniPtseChecksum"),
        ("PNNI-MIB", "pnniPtseLifeTime"),
        ("PNNI-MIB", "pnniPtseInfo"))
)
if mibBuilder.loadTexts:
    pnniPtseOptionalGroup.setStatus("current")

pnniMapOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 21)
)
pnniMapOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniMapType"),
        ("PNNI-MIB", "pnniMapPeerGroupId"),
        ("PNNI-MIB", "pnniMapAggrToken"),
        ("PNNI-MIB", "pnniMapRemoteNodeId"),
        ("PNNI-MIB", "pnniMapRemotePortId"),
        ("PNNI-MIB", "pnniMapVPCapability"),
        ("PNNI-MIB", "pnniMapPtseId"),
        ("PNNI-MIB", "pnniMapMetricsTag"))
)
if mibBuilder.loadTexts:
    pnniMapOptionalGroup.setStatus("current")

pnniMapNodeOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 22)
)
pnniMapNodeOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniMapNodePeerGroupId"),
        ("PNNI-MIB", "pnniMapNodeAtmAddress"),
        ("PNNI-MIB", "pnniMapNodeRestrictedTransit"),
        ("PNNI-MIB", "pnniMapNodeComplexRep"),
        ("PNNI-MIB", "pnniMapNodeRestrictedBranching"),
        ("PNNI-MIB", "pnniMapNodeDatabaseOverload"),
        ("PNNI-MIB", "pnniMapNodeIAmLeader"),
        ("PNNI-MIB", "pnniMapNodeLeadershipPriority"),
        ("PNNI-MIB", "pnniMapNodePreferredPgl"),
        ("PNNI-MIB", "pnniMapNodeParentNodeId"),
        ("PNNI-MIB", "pnniMapNodeParentAtmAddress"),
        ("PNNI-MIB", "pnniMapNodeParentPeerGroupId"),
        ("PNNI-MIB", "pnniMapNodeParentPglNodeId"))
)
if mibBuilder.loadTexts:
    pnniMapNodeOptionalGroup.setStatus("current")

pnniMapAddrOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 23)
)
pnniMapAddrOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniMapAddrAddress"),
        ("PNNI-MIB", "pnniMapAddrPrefixLength"))
)
if mibBuilder.loadTexts:
    pnniMapAddrOptionalGroup.setStatus("current")

pnniMapTnsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 24)
)
pnniMapTnsOptionalGroup.setObjects(
    ("PNNI-MIB", "pnniMapTnsId")
)
if mibBuilder.loadTexts:
    pnniMapTnsOptionalGroup.setStatus("current")

pnniMetricsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 25)
)
pnniMetricsOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniMetricsClasses"),
        ("PNNI-MIB", "pnniMetricsGcacClp"),
        ("PNNI-MIB", "pnniMetricsAdminWeight"),
        ("PNNI-MIB", "pnniMetrics1"),
        ("PNNI-MIB", "pnniMetrics2"),
        ("PNNI-MIB", "pnniMetrics3"),
        ("PNNI-MIB", "pnniMetrics4"),
        ("PNNI-MIB", "pnniMetrics5"),
        ("PNNI-MIB", "pnniMetrics6"),
        ("PNNI-MIB", "pnniMetrics7"),
        ("PNNI-MIB", "pnniMetrics8"),
        ("PNNI-MIB", "pnniMetricsRowStatus"))
)
if mibBuilder.loadTexts:
    pnniMetricsOptionalGroup.setStatus("current")

pnniRouteGeneralOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 26)
)
pnniRouteGeneralOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniRouteNodeNumber"),
        ("PNNI-MIB", "pnniRouteAddrNumber"))
)
if mibBuilder.loadTexts:
    pnniRouteGeneralOptionalGroup.setStatus("current")

pnniRouteNodeOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 27)
)
pnniRouteNodeOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniRouteNodeDestPortId"),
        ("PNNI-MIB", "pnniRouteNodeProto"),
        ("PNNI-MIB", "pnniRouteNodeTimeStamp"),
        ("PNNI-MIB", "pnniRouteNodeInfo"),
        ("PNNI-MIB", "pnniRouteNodeGcacClp"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetricAW"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric1"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric2"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric3"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric4"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric5"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric6"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric7"),
        ("PNNI-MIB", "pnniRouteNodeFwdMetric8"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetricAW"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric1"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric2"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric3"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric4"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric5"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric6"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric7"),
        ("PNNI-MIB", "pnniRouteNodeBwdMetric8"),
        ("PNNI-MIB", "pnniRouteNodeVPCapability"),
        ("PNNI-MIB", "pnniRouteNodeStatus"))
)
if mibBuilder.loadTexts:
    pnniRouteNodeOptionalGroup.setStatus("current")

pnniDTLOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 28)
)
pnniDTLOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniDTLNodeId"),
        ("PNNI-MIB", "pnniDTLPortId"),
        ("PNNI-MIB", "pnniDTLLinkType"),
        ("PNNI-MIB", "pnniDTLStatus"))
)
if mibBuilder.loadTexts:
    pnniDTLOptionalGroup.setStatus("current")

pnniRouteAddrOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 29)
)
pnniRouteAddrOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniRouteAddrIfIndex"),
        ("PNNI-MIB", "pnniRouteAddrAdvertisingNodeId"),
        ("PNNI-MIB", "pnniRouteAddrAdvertisedPortId"),
        ("PNNI-MIB", "pnniRouteAddrType"),
        ("PNNI-MIB", "pnniRouteAddrProto"),
        ("PNNI-MIB", "pnniRouteAddrPnniScope"),
        ("PNNI-MIB", "pnniRouteAddrVPCapability"),
        ("PNNI-MIB", "pnniRouteAddrMetricsTag"),
        ("PNNI-MIB", "pnniRouteAddrPtseId"),
        ("PNNI-MIB", "pnniRouteAddrOriginateAdvertisement"),
        ("PNNI-MIB", "pnniRouteAddrInfo"),
        ("PNNI-MIB", "pnniRouteAddrOperStatus"),
        ("PNNI-MIB", "pnniRouteAddrTimeStamp"),
        ("PNNI-MIB", "pnniRouteAddrRowStatus"))
)
if mibBuilder.loadTexts:
    pnniRouteAddrOptionalGroup.setStatus("current")

pnniRouteTnsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 30)
)
pnniRouteTnsOptionalGroup.setObjects(
      *(("PNNI-MIB", "pnniRouteTnsIfIndex"),
        ("PNNI-MIB", "pnniRouteTnsAdvertisingNodeId"),
        ("PNNI-MIB", "pnniRouteTnsAdvertisedPortId"),
        ("PNNI-MIB", "pnniRouteTnsRouteType"),
        ("PNNI-MIB", "pnniRouteTnsProto"),
        ("PNNI-MIB", "pnniRouteTnsPnniScope"),
        ("PNNI-MIB", "pnniRouteTnsVPCapability"),
        ("PNNI-MIB", "pnniRouteTnsMetricsTag"),
        ("PNNI-MIB", "pnniRouteTnsPtseId"),
        ("PNNI-MIB", "pnniRouteTnsOriginateAdvertisement"),
        ("PNNI-MIB", "pnniRouteTnsInfo"),
        ("PNNI-MIB", "pnniRouteTnsOperStatus"),
        ("PNNI-MIB", "pnniRouteTnsTimeStamp"),
        ("PNNI-MIB", "pnniRouteTnsRowStatus"))
)
if mibBuilder.loadTexts:
    pnniRouteTnsOptionalGroup.setStatus("current")

pnniSummaryAddressLgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 2, 31)
)
pnniSummaryAddressLgnGroup.setObjects(
      *(("PNNI-MIB", "pnniSummaryAddressSuppress"),
        ("PNNI-MIB", "pnniSummaryAddressState"),
        ("PNNI-MIB", "pnniSummaryAddressRowStatus"))
)
if mibBuilder.loadTexts:
    pnniSummaryAddressLgnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pnniMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pnniMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PNNI-MIB",
    **{"PnniAtmAddr": PnniAtmAddr,
       "PnniNodeIndex": PnniNodeIndex,
       "PnniNodeId": PnniNodeId,
       "PnniPortId": PnniPortId,
       "PnniAggrToken": PnniAggrToken,
       "PnniPeerGroupId": PnniPeerGroupId,
       "PnniLevel": PnniLevel,
       "PnniSvccRccIndex": PnniSvccRccIndex,
       "AtmAddrPrefix": AtmAddrPrefix,
       "PnniPrefixLength": PnniPrefixLength,
       "PnniMetricsTag": PnniMetricsTag,
       "ServiceCategory": ServiceCategory,
       "ClpType": ClpType,
       "TnsType": TnsType,
       "TnsPlan": TnsPlan,
       "PnniVersion": PnniVersion,
       "PnniHelloState": PnniHelloState,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfPnni": atmfPnni,
       "pnniMIB": pnniMIB,
       "pnniMIBObjects": pnniMIBObjects,
       "pnniBaseGroup": pnniBaseGroup,
       "pnniHighestVersion": pnniHighestVersion,
       "pnniLowestVersion": pnniLowestVersion,
       "pnniDtlCountOriginator": pnniDtlCountOriginator,
       "pnniDtlCountBorder": pnniDtlCountBorder,
       "pnniCrankbackCountOriginator": pnniCrankbackCountOriginator,
       "pnniCrankbackCountBorder": pnniCrankbackCountBorder,
       "pnniAltRouteCountOriginator": pnniAltRouteCountOriginator,
       "pnniAltRouteCountBorder": pnniAltRouteCountBorder,
       "pnniRouteFailCountOriginator": pnniRouteFailCountOriginator,
       "pnniRouteFailCountBorder": pnniRouteFailCountBorder,
       "pnniRouteFailUnreachableOriginator": pnniRouteFailUnreachableOriginator,
       "pnniRouteFailUnreachableBorder": pnniRouteFailUnreachableBorder,
       "pnniNodeTable": pnniNodeTable,
       "pnniNodeEntry": pnniNodeEntry,
       "pnniNodeIndex": pnniNodeIndex,
       "pnniNodeLevel": pnniNodeLevel,
       "pnniNodeId": pnniNodeId,
       "pnniNodeLowest": pnniNodeLowest,
       "pnniNodeAdminStatus": pnniNodeAdminStatus,
       "pnniNodeOperStatus": pnniNodeOperStatus,
       "pnniNodeDomainName": pnniNodeDomainName,
       "pnniNodeAtmAddress": pnniNodeAtmAddress,
       "pnniNodePeerGroupId": pnniNodePeerGroupId,
       "pnniNodeRestrictedTransit": pnniNodeRestrictedTransit,
       "pnniNodeComplexRep": pnniNodeComplexRep,
       "pnniNodeRestrictedBranching": pnniNodeRestrictedBranching,
       "pnniNodeDatabaseOverload": pnniNodeDatabaseOverload,
       "pnniNodePtses": pnniNodePtses,
       "pnniNodeRowStatus": pnniNodeRowStatus,
       "pnniNodePglTable": pnniNodePglTable,
       "pnniNodePglEntry": pnniNodePglEntry,
       "pnniNodePglLeadershipPriority": pnniNodePglLeadershipPriority,
       "pnniNodeCfgParentNodeIndex": pnniNodeCfgParentNodeIndex,
       "pnniNodePglInitTime": pnniNodePglInitTime,
       "pnniNodePglOverrideDelay": pnniNodePglOverrideDelay,
       "pnniNodePglReelectTime": pnniNodePglReelectTime,
       "pnniNodePglState": pnniNodePglState,
       "pnniNodePreferredPgl": pnniNodePreferredPgl,
       "pnniNodePeerGroupLeader": pnniNodePeerGroupLeader,
       "pnniNodePglTimeStamp": pnniNodePglTimeStamp,
       "pnniNodeActiveParentNodeId": pnniNodeActiveParentNodeId,
       "pnniNodeTimerTable": pnniNodeTimerTable,
       "pnniNodeTimerEntry": pnniNodeTimerEntry,
       "pnniNodePtseHolddown": pnniNodePtseHolddown,
       "pnniNodeHelloHolddown": pnniNodeHelloHolddown,
       "pnniNodeHelloInterval": pnniNodeHelloInterval,
       "pnniNodeHelloInactivityFactor": pnniNodeHelloInactivityFactor,
       "pnniNodeHlinkInact": pnniNodeHlinkInact,
       "pnniNodePtseRefreshInterval": pnniNodePtseRefreshInterval,
       "pnniNodePtseLifetimeFactor": pnniNodePtseLifetimeFactor,
       "pnniNodeRxmtInterval": pnniNodeRxmtInterval,
       "pnniNodePeerDelayedAckInterval": pnniNodePeerDelayedAckInterval,
       "pnniNodeAvcrPm": pnniNodeAvcrPm,
       "pnniNodeAvcrMt": pnniNodeAvcrMt,
       "pnniNodeCdvPm": pnniNodeCdvPm,
       "pnniNodeCtdPm": pnniNodeCtdPm,
       "pnniNodeSvccTable": pnniNodeSvccTable,
       "pnniNodeSvccEntry": pnniNodeSvccEntry,
       "pnniNodeSvccInitTime": pnniNodeSvccInitTime,
       "pnniNodeSvccRetryTime": pnniNodeSvccRetryTime,
       "pnniNodeSvccCallingIntegrityTime": pnniNodeSvccCallingIntegrityTime,
       "pnniNodeSvccCalledIntegrityTime": pnniNodeSvccCalledIntegrityTime,
       "pnniNodeSvccTrafficDescriptorIndex": pnniNodeSvccTrafficDescriptorIndex,
       "pnniScopeMappingTable": pnniScopeMappingTable,
       "pnniScopeMappingEntry": pnniScopeMappingEntry,
       "pnniScopeLocalNetwork": pnniScopeLocalNetwork,
       "pnniScopeLocalNetworkPlusOne": pnniScopeLocalNetworkPlusOne,
       "pnniScopeLocalNetworkPlusTwo": pnniScopeLocalNetworkPlusTwo,
       "pnniScopeSiteMinusOne": pnniScopeSiteMinusOne,
       "pnniScopeIntraSite": pnniScopeIntraSite,
       "pnniScopeSitePlusOne": pnniScopeSitePlusOne,
       "pnniScopeOrganizationMinusOne": pnniScopeOrganizationMinusOne,
       "pnniScopeIntraOrganization": pnniScopeIntraOrganization,
       "pnniScopeOrganizationPlusOne": pnniScopeOrganizationPlusOne,
       "pnniScopeCommunityMinusOne": pnniScopeCommunityMinusOne,
       "pnniScopeIntraCommunity": pnniScopeIntraCommunity,
       "pnniScopeCommunityPlusOne": pnniScopeCommunityPlusOne,
       "pnniScopeRegional": pnniScopeRegional,
       "pnniScopeInterRegional": pnniScopeInterRegional,
       "pnniScopeGlobal": pnniScopeGlobal,
       "pnniSummaryTable": pnniSummaryTable,
       "pnniSummaryEntry": pnniSummaryEntry,
       "pnniSummaryAddress": pnniSummaryAddress,
       "pnniSummaryPrefixLength": pnniSummaryPrefixLength,
       "pnniSummaryType": pnniSummaryType,
       "pnniSummarySuppress": pnniSummarySuppress,
       "pnniSummaryState": pnniSummaryState,
       "pnniSummaryRowStatus": pnniSummaryRowStatus,
       "pnniIfTable": pnniIfTable,
       "pnniIfEntry": pnniIfEntry,
       "pnniIfNodeIndex": pnniIfNodeIndex,
       "pnniIfPortId": pnniIfPortId,
       "pnniIfAggrToken": pnniIfAggrToken,
       "pnniIfVPCapability": pnniIfVPCapability,
       "pnniIfAdmWeightCbr": pnniIfAdmWeightCbr,
       "pnniIfAdmWeightRtVbr": pnniIfAdmWeightRtVbr,
       "pnniIfAdmWeightNrtVbr": pnniIfAdmWeightNrtVbr,
       "pnniIfAdmWeightAbr": pnniIfAdmWeightAbr,
       "pnniIfAdmWeightUbr": pnniIfAdmWeightUbr,
       "pnniIfRccServiceCategory": pnniIfRccServiceCategory,
       "pnniIfRccTrafficDescrIndex": pnniIfRccTrafficDescrIndex,
       "pnniLinkTable": pnniLinkTable,
       "pnniLinkEntry": pnniLinkEntry,
       "pnniLinkPortId": pnniLinkPortId,
       "pnniLinkType": pnniLinkType,
       "pnniLinkVersion": pnniLinkVersion,
       "pnniLinkHelloState": pnniLinkHelloState,
       "pnniLinkRemoteNodeId": pnniLinkRemoteNodeId,
       "pnniLinkRemotePortId": pnniLinkRemotePortId,
       "pnniLinkDerivedAggrToken": pnniLinkDerivedAggrToken,
       "pnniLinkUpnodeId": pnniLinkUpnodeId,
       "pnniLinkUpnodeAtmAddress": pnniLinkUpnodeAtmAddress,
       "pnniLinkCommonPeerGroupId": pnniLinkCommonPeerGroupId,
       "pnniLinkIfIndex": pnniLinkIfIndex,
       "pnniLinkSvccRccIndex": pnniLinkSvccRccIndex,
       "pnniLinkRcvHellos": pnniLinkRcvHellos,
       "pnniLinkXmtHellos": pnniLinkXmtHellos,
       "pnniNbrPeerTable": pnniNbrPeerTable,
       "pnniNbrPeerEntry": pnniNbrPeerEntry,
       "pnniNbrPeerRemoteNodeId": pnniNbrPeerRemoteNodeId,
       "pnniNbrPeerState": pnniNbrPeerState,
       "pnniNbrPeerSvccRccIndex": pnniNbrPeerSvccRccIndex,
       "pnniNbrPeerPortCount": pnniNbrPeerPortCount,
       "pnniNbrPeerRcvDbSums": pnniNbrPeerRcvDbSums,
       "pnniNbrPeerXmtDbSums": pnniNbrPeerXmtDbSums,
       "pnniNbrPeerRcvPtsps": pnniNbrPeerRcvPtsps,
       "pnniNbrPeerXmtPtsps": pnniNbrPeerXmtPtsps,
       "pnniNbrPeerRcvPtseReqs": pnniNbrPeerRcvPtseReqs,
       "pnniNbrPeerXmtPtseReqs": pnniNbrPeerXmtPtseReqs,
       "pnniNbrPeerRcvPtseAcks": pnniNbrPeerRcvPtseAcks,
       "pnniNbrPeerXmtPtseAcks": pnniNbrPeerXmtPtseAcks,
       "pnniNbrPeerPortTable": pnniNbrPeerPortTable,
       "pnniNbrPeerPortEntry": pnniNbrPeerPortEntry,
       "pnniNbrPeerPortId": pnniNbrPeerPortId,
       "pnniNbrPeerPortFloodStatus": pnniNbrPeerPortFloodStatus,
       "pnniSvccRccTable": pnniSvccRccTable,
       "pnniSvccRccEntry": pnniSvccRccEntry,
       "pnniSvccRccIndex": pnniSvccRccIndex,
       "pnniSvccRccVersion": pnniSvccRccVersion,
       "pnniSvccRccHelloState": pnniSvccRccHelloState,
       "pnniSvccRccRemoteNodeId": pnniSvccRccRemoteNodeId,
       "pnniSvccRccRemoteAtmAddress": pnniSvccRccRemoteAtmAddress,
       "pnniSvccRccRcvHellos": pnniSvccRccRcvHellos,
       "pnniSvccRccXmtHellos": pnniSvccRccXmtHellos,
       "pnniSvccRccIfIndex": pnniSvccRccIfIndex,
       "pnniSvccRccVpi": pnniSvccRccVpi,
       "pnniSvccRccVci": pnniSvccRccVci,
       "pnniPtseTable": pnniPtseTable,
       "pnniPtseEntry": pnniPtseEntry,
       "pnniPtseOriginatingNodeId": pnniPtseOriginatingNodeId,
       "pnniPtseId": pnniPtseId,
       "pnniPtseType": pnniPtseType,
       "pnniPtseSequenceNum": pnniPtseSequenceNum,
       "pnniPtseChecksum": pnniPtseChecksum,
       "pnniPtseLifeTime": pnniPtseLifeTime,
       "pnniPtseInfo": pnniPtseInfo,
       "pnniMapTable": pnniMapTable,
       "pnniMapEntry": pnniMapEntry,
       "pnniMapOriginatingNodeId": pnniMapOriginatingNodeId,
       "pnniMapOriginatingPortId": pnniMapOriginatingPortId,
       "pnniMapIndex": pnniMapIndex,
       "pnniMapType": pnniMapType,
       "pnniMapPeerGroupId": pnniMapPeerGroupId,
       "pnniMapAggrToken": pnniMapAggrToken,
       "pnniMapRemoteNodeId": pnniMapRemoteNodeId,
       "pnniMapRemotePortId": pnniMapRemotePortId,
       "pnniMapVPCapability": pnniMapVPCapability,
       "pnniMapPtseId": pnniMapPtseId,
       "pnniMapMetricsTag": pnniMapMetricsTag,
       "pnniMapNodeTable": pnniMapNodeTable,
       "pnniMapNodeEntry": pnniMapNodeEntry,
       "pnniMapNodeId": pnniMapNodeId,
       "pnniMapNodePeerGroupId": pnniMapNodePeerGroupId,
       "pnniMapNodeAtmAddress": pnniMapNodeAtmAddress,
       "pnniMapNodeRestrictedTransit": pnniMapNodeRestrictedTransit,
       "pnniMapNodeComplexRep": pnniMapNodeComplexRep,
       "pnniMapNodeRestrictedBranching": pnniMapNodeRestrictedBranching,
       "pnniMapNodeDatabaseOverload": pnniMapNodeDatabaseOverload,
       "pnniMapNodeIAmLeader": pnniMapNodeIAmLeader,
       "pnniMapNodeLeadershipPriority": pnniMapNodeLeadershipPriority,
       "pnniMapNodePreferredPgl": pnniMapNodePreferredPgl,
       "pnniMapNodeParentNodeId": pnniMapNodeParentNodeId,
       "pnniMapNodeParentAtmAddress": pnniMapNodeParentAtmAddress,
       "pnniMapNodeParentPeerGroupId": pnniMapNodeParentPeerGroupId,
       "pnniMapNodeParentPglNodeId": pnniMapNodeParentPglNodeId,
       "pnniMapAddrTable": pnniMapAddrTable,
       "pnniMapAddrEntry": pnniMapAddrEntry,
       "pnniMapAddrAdvertisingNodeId": pnniMapAddrAdvertisingNodeId,
       "pnniMapAddrAdvertisedPortId": pnniMapAddrAdvertisedPortId,
       "pnniMapAddrIndex": pnniMapAddrIndex,
       "pnniMapAddrAddress": pnniMapAddrAddress,
       "pnniMapAddrPrefixLength": pnniMapAddrPrefixLength,
       "pnniMapTnsTable": pnniMapTnsTable,
       "pnniMapTnsEntry": pnniMapTnsEntry,
       "pnniMapTnsAdvertisingNodeId": pnniMapTnsAdvertisingNodeId,
       "pnniMapTnsAdvertisedPortId": pnniMapTnsAdvertisedPortId,
       "pnniMapTnsType": pnniMapTnsType,
       "pnniMapTnsPlan": pnniMapTnsPlan,
       "pnniMapTnsId": pnniMapTnsId,
       "pnniMetricsTable": pnniMetricsTable,
       "pnniMetricsEntry": pnniMetricsEntry,
       "pnniMetricsTag": pnniMetricsTag,
       "pnniMetricsDirection": pnniMetricsDirection,
       "pnniMetricsIndex": pnniMetricsIndex,
       "pnniMetricsClasses": pnniMetricsClasses,
       "pnniMetricsGcacClp": pnniMetricsGcacClp,
       "pnniMetricsAdminWeight": pnniMetricsAdminWeight,
       "pnniMetrics1": pnniMetrics1,
       "pnniMetrics2": pnniMetrics2,
       "pnniMetrics3": pnniMetrics3,
       "pnniMetrics4": pnniMetrics4,
       "pnniMetrics5": pnniMetrics5,
       "pnniMetrics6": pnniMetrics6,
       "pnniMetrics7": pnniMetrics7,
       "pnniMetrics8": pnniMetrics8,
       "pnniMetricsRowStatus": pnniMetricsRowStatus,
       "pnniRoutingGroup": pnniRoutingGroup,
       "pnniRouteBaseGroup": pnniRouteBaseGroup,
       "pnniRouteNodeNumber": pnniRouteNodeNumber,
       "pnniRouteAddrNumber": pnniRouteAddrNumber,
       "pnniRouteNodeTable": pnniRouteNodeTable,
       "pnniRouteNodeEntry": pnniRouteNodeEntry,
       "pnniRouteNodeClass": pnniRouteNodeClass,
       "pnniRouteNodeDestNodeId": pnniRouteNodeDestNodeId,
       "pnniRouteNodeDTL": pnniRouteNodeDTL,
       "pnniRouteNodeDestPortId": pnniRouteNodeDestPortId,
       "pnniRouteNodeProto": pnniRouteNodeProto,
       "pnniRouteNodeTimeStamp": pnniRouteNodeTimeStamp,
       "pnniRouteNodeInfo": pnniRouteNodeInfo,
       "pnniRouteNodeGcacClp": pnniRouteNodeGcacClp,
       "pnniRouteNodeFwdMetricAW": pnniRouteNodeFwdMetricAW,
       "pnniRouteNodeFwdMetric1": pnniRouteNodeFwdMetric1,
       "pnniRouteNodeFwdMetric2": pnniRouteNodeFwdMetric2,
       "pnniRouteNodeFwdMetric3": pnniRouteNodeFwdMetric3,
       "pnniRouteNodeFwdMetric4": pnniRouteNodeFwdMetric4,
       "pnniRouteNodeFwdMetric5": pnniRouteNodeFwdMetric5,
       "pnniRouteNodeFwdMetric6": pnniRouteNodeFwdMetric6,
       "pnniRouteNodeFwdMetric7": pnniRouteNodeFwdMetric7,
       "pnniRouteNodeFwdMetric8": pnniRouteNodeFwdMetric8,
       "pnniRouteNodeBwdMetricAW": pnniRouteNodeBwdMetricAW,
       "pnniRouteNodeBwdMetric1": pnniRouteNodeBwdMetric1,
       "pnniRouteNodeBwdMetric2": pnniRouteNodeBwdMetric2,
       "pnniRouteNodeBwdMetric3": pnniRouteNodeBwdMetric3,
       "pnniRouteNodeBwdMetric4": pnniRouteNodeBwdMetric4,
       "pnniRouteNodeBwdMetric5": pnniRouteNodeBwdMetric5,
       "pnniRouteNodeBwdMetric6": pnniRouteNodeBwdMetric6,
       "pnniRouteNodeBwdMetric7": pnniRouteNodeBwdMetric7,
       "pnniRouteNodeBwdMetric8": pnniRouteNodeBwdMetric8,
       "pnniRouteNodeVPCapability": pnniRouteNodeVPCapability,
       "pnniRouteNodeStatus": pnniRouteNodeStatus,
       "pnniDTLTable": pnniDTLTable,
       "pnniDTLEntry": pnniDTLEntry,
       "pnniDTLIndex": pnniDTLIndex,
       "pnniDTLEntryIndex": pnniDTLEntryIndex,
       "pnniDTLNodeId": pnniDTLNodeId,
       "pnniDTLPortId": pnniDTLPortId,
       "pnniDTLLinkType": pnniDTLLinkType,
       "pnniDTLStatus": pnniDTLStatus,
       "pnniRouteAddrTable": pnniRouteAddrTable,
       "pnniRouteAddrEntry": pnniRouteAddrEntry,
       "pnniRouteAddrAddress": pnniRouteAddrAddress,
       "pnniRouteAddrPrefixLength": pnniRouteAddrPrefixLength,
       "pnniRouteAddrIndex": pnniRouteAddrIndex,
       "pnniRouteAddrIfIndex": pnniRouteAddrIfIndex,
       "pnniRouteAddrAdvertisingNodeId": pnniRouteAddrAdvertisingNodeId,
       "pnniRouteAddrAdvertisedPortId": pnniRouteAddrAdvertisedPortId,
       "pnniRouteAddrType": pnniRouteAddrType,
       "pnniRouteAddrProto": pnniRouteAddrProto,
       "pnniRouteAddrPnniScope": pnniRouteAddrPnniScope,
       "pnniRouteAddrVPCapability": pnniRouteAddrVPCapability,
       "pnniRouteAddrMetricsTag": pnniRouteAddrMetricsTag,
       "pnniRouteAddrPtseId": pnniRouteAddrPtseId,
       "pnniRouteAddrOriginateAdvertisement": pnniRouteAddrOriginateAdvertisement,
       "pnniRouteAddrInfo": pnniRouteAddrInfo,
       "pnniRouteAddrOperStatus": pnniRouteAddrOperStatus,
       "pnniRouteAddrTimeStamp": pnniRouteAddrTimeStamp,
       "pnniRouteAddrRowStatus": pnniRouteAddrRowStatus,
       "pnniRouteTnsTable": pnniRouteTnsTable,
       "pnniRouteTnsEntry": pnniRouteTnsEntry,
       "pnniRouteTnsType": pnniRouteTnsType,
       "pnniRouteTnsPlan": pnniRouteTnsPlan,
       "pnniRouteTnsId": pnniRouteTnsId,
       "pnniRouteTnsIndex": pnniRouteTnsIndex,
       "pnniRouteTnsIfIndex": pnniRouteTnsIfIndex,
       "pnniRouteTnsAdvertisingNodeId": pnniRouteTnsAdvertisingNodeId,
       "pnniRouteTnsAdvertisedPortId": pnniRouteTnsAdvertisedPortId,
       "pnniRouteTnsRouteType": pnniRouteTnsRouteType,
       "pnniRouteTnsProto": pnniRouteTnsProto,
       "pnniRouteTnsPnniScope": pnniRouteTnsPnniScope,
       "pnniRouteTnsVPCapability": pnniRouteTnsVPCapability,
       "pnniRouteTnsMetricsTag": pnniRouteTnsMetricsTag,
       "pnniRouteTnsPtseId": pnniRouteTnsPtseId,
       "pnniRouteTnsOriginateAdvertisement": pnniRouteTnsOriginateAdvertisement,
       "pnniRouteTnsInfo": pnniRouteTnsInfo,
       "pnniRouteTnsOperStatus": pnniRouteTnsOperStatus,
       "pnniRouteTnsTimeStamp": pnniRouteTnsTimeStamp,
       "pnniRouteTnsRowStatus": pnniRouteTnsRowStatus,
       "pnniSummaryAddressTable": pnniSummaryAddressTable,
       "pnniSummaryAddressEntry": pnniSummaryAddressEntry,
       "pnniSummaryAddressType": pnniSummaryAddressType,
       "pnniSummaryAddressAddress": pnniSummaryAddressAddress,
       "pnniSummaryAddressPrefixLength": pnniSummaryAddressPrefixLength,
       "pnniSummaryAddressSuppress": pnniSummaryAddressSuppress,
       "pnniSummaryAddressState": pnniSummaryAddressState,
       "pnniSummaryAddressRowStatus": pnniSummaryAddressRowStatus,
       "pnniMIBConformance": pnniMIBConformance,
       "pnniMIBCompliances": pnniMIBCompliances,
       "pnniMIBCompliance": pnniMIBCompliance,
       "pnniMIBGroups": pnniMIBGroups,
       "pnniGeneralMinGroup": pnniGeneralMinGroup,
       "pnniGeneralBorderGroup": pnniGeneralBorderGroup,
       "pnniNodeMinGroup": pnniNodeMinGroup,
       "pnniNodePglMinGroup": pnniNodePglMinGroup,
       "pnniNodePglLgnGroup": pnniNodePglLgnGroup,
       "pnniNodeTimerMinGroup": pnniNodeTimerMinGroup,
       "pnniNodeTimerLgnGroup": pnniNodeTimerLgnGroup,
       "pnniNodeSvccLgnGroup": pnniNodeSvccLgnGroup,
       "pnniScopeMinGroup": pnniScopeMinGroup,
       "pnniSummaryLgnGroup": pnniSummaryLgnGroup,
       "pnniIfMinGroup": pnniIfMinGroup,
       "pnniIfBorderGroup": pnniIfBorderGroup,
       "pnniLinkMinGroup": pnniLinkMinGroup,
       "pnniLinkBorderOrLgnGroup": pnniLinkBorderOrLgnGroup,
       "pnniLinkLgnGroup": pnniLinkLgnGroup,
       "pnniNbrPeerMinGroup": pnniNbrPeerMinGroup,
       "pnniNbrPeerLgnGroup": pnniNbrPeerLgnGroup,
       "pnniNbrPeerPortMinGroup": pnniNbrPeerPortMinGroup,
       "pnniSvccRccLgnGroup": pnniSvccRccLgnGroup,
       "pnniPtseOptionalGroup": pnniPtseOptionalGroup,
       "pnniMapOptionalGroup": pnniMapOptionalGroup,
       "pnniMapNodeOptionalGroup": pnniMapNodeOptionalGroup,
       "pnniMapAddrOptionalGroup": pnniMapAddrOptionalGroup,
       "pnniMapTnsOptionalGroup": pnniMapTnsOptionalGroup,
       "pnniMetricsOptionalGroup": pnniMetricsOptionalGroup,
       "pnniRouteGeneralOptionalGroup": pnniRouteGeneralOptionalGroup,
       "pnniRouteNodeOptionalGroup": pnniRouteNodeOptionalGroup,
       "pnniDTLOptionalGroup": pnniDTLOptionalGroup,
       "pnniRouteAddrOptionalGroup": pnniRouteAddrOptionalGroup,
       "pnniRouteTnsOptionalGroup": pnniRouteTnsOptionalGroup,
       "pnniSummaryAddressLgnGroup": pnniSummaryAddressLgnGroup}
)
