# SNMP MIB module (XPNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XPNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:46 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanPnni,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPnni")


# MODULE-IDENTITY


# Types definitions



class PnnixAtmAddr(OctetString):
    """Custom type PnnixAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )





class PnnixNodeIndex(Integer32):
    """Custom type PnnixNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class AtmpTrafficDescrParamIndex(Integer32):
    """Custom type AtmpTrafficDescrParamIndex based on Integer32"""




class PnnixNodeId(OctetString):
    """Custom type PnnixNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )





class PnnixPortId(Gauge32):
    """Custom type PnnixPortId based on Gauge32"""




class PnnixAggrToken(Gauge32):
    """Custom type PnnixAggrToken based on Gauge32"""




class PnnixPeerGroupId(OctetString):
    """Custom type PnnixPeerGroupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )





class PnnixLevel(Integer32):
    """Custom type PnnixLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )





class PnnixSvccRccIndex(Integer32):
    """Custom type PnnixSvccRccIndex based on Integer32"""




class AtmAddrPrefix(OctetString):
    """Custom type AtmAddrPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )





class PnnixPrefixLength(Integer32):
    """Custom type PnnixPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )





class PnnixMetricsTag(Integer32):
    """Custom type PnnixMetricsTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class ServiceCategory(Integer32):
    """Custom type ServiceCategory based on Integer32"""
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





class ClpType(Integer32):
    """Custom type ClpType based on Integer32"""
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





class TnsType(Integer32):
    """Custom type TnsType based on Integer32"""
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





class TnsPlan(Integer32):
    """Custom type TnsPlan based on Integer32"""
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





class PnnixVersion(Integer32):
    """Custom type PnnixVersion based on Integer32"""
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





class PnnixHelloState(Integer32):
    """Custom type PnnixHelloState based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PnnixMIB_ObjectIdentity = ObjectIdentity
pnnixMIB = _PnnixMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1)
)
_PnnixMIBObjects_ObjectIdentity = ObjectIdentity
pnnixMIBObjects = _PnnixMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1)
)
_PnnixBaseGroup_ObjectIdentity = ObjectIdentity
pnnixBaseGroup = _PnnixBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1)
)
_PnnixHighestVersion_Type = PnnixVersion
_PnnixHighestVersion_Object = MibScalar
pnnixHighestVersion = _PnnixHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 1),
    _PnnixHighestVersion_Type()
)
pnnixHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixHighestVersion.setStatus("mandatory")
_PnnixLowestVersion_Type = PnnixVersion
_PnnixLowestVersion_Object = MibScalar
pnnixLowestVersion = _PnnixLowestVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 2),
    _PnnixLowestVersion_Type()
)
pnnixLowestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLowestVersion.setStatus("mandatory")
_PnnixDtlCountOriginator_Type = Counter32
_PnnixDtlCountOriginator_Object = MibScalar
pnnixDtlCountOriginator = _PnnixDtlCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 3),
    _PnnixDtlCountOriginator_Type()
)
pnnixDtlCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixDtlCountOriginator.setStatus("mandatory")
_PnnixDtlCountBorder_Type = Counter32
_PnnixDtlCountBorder_Object = MibScalar
pnnixDtlCountBorder = _PnnixDtlCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 4),
    _PnnixDtlCountBorder_Type()
)
pnnixDtlCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixDtlCountBorder.setStatus("mandatory")
_PnnixCrankbackCountOriginator_Type = Counter32
_PnnixCrankbackCountOriginator_Object = MibScalar
pnnixCrankbackCountOriginator = _PnnixCrankbackCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 5),
    _PnnixCrankbackCountOriginator_Type()
)
pnnixCrankbackCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixCrankbackCountOriginator.setStatus("mandatory")
_PnnixCrankbackCountBorder_Type = Counter32
_PnnixCrankbackCountBorder_Object = MibScalar
pnnixCrankbackCountBorder = _PnnixCrankbackCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 6),
    _PnnixCrankbackCountBorder_Type()
)
pnnixCrankbackCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixCrankbackCountBorder.setStatus("mandatory")
_PnnixAltRouteCountOriginator_Type = Counter32
_PnnixAltRouteCountOriginator_Object = MibScalar
pnnixAltRouteCountOriginator = _PnnixAltRouteCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 7),
    _PnnixAltRouteCountOriginator_Type()
)
pnnixAltRouteCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixAltRouteCountOriginator.setStatus("mandatory")
_PnnixAltRouteCountBorder_Type = Counter32
_PnnixAltRouteCountBorder_Object = MibScalar
pnnixAltRouteCountBorder = _PnnixAltRouteCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 8),
    _PnnixAltRouteCountBorder_Type()
)
pnnixAltRouteCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixAltRouteCountBorder.setStatus("mandatory")
_PnnixRouteFailCountOriginator_Type = Counter32
_PnnixRouteFailCountOriginator_Object = MibScalar
pnnixRouteFailCountOriginator = _PnnixRouteFailCountOriginator_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 9),
    _PnnixRouteFailCountOriginator_Type()
)
pnnixRouteFailCountOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteFailCountOriginator.setStatus("mandatory")
_PnnixRouteFailCountBorder_Type = Counter32
_PnnixRouteFailCountBorder_Object = MibScalar
pnnixRouteFailCountBorder = _PnnixRouteFailCountBorder_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 10),
    _PnnixRouteFailCountBorder_Type()
)
pnnixRouteFailCountBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteFailCountBorder.setStatus("mandatory")
_PnnixRouteFailUnreachableOriginator_Type = Counter32
_PnnixRouteFailUnreachableOriginator_Object = MibScalar
pnnixRouteFailUnreachableOriginator = _PnnixRouteFailUnreachableOriginator_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 11),
    _PnnixRouteFailUnreachableOriginator_Type()
)
pnnixRouteFailUnreachableOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteFailUnreachableOriginator.setStatus("mandatory")
_PnnixRouteFailUnreachableBorder_Type = Counter32
_PnnixRouteFailUnreachableBorder_Object = MibScalar
pnnixRouteFailUnreachableBorder = _PnnixRouteFailUnreachableBorder_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 1, 12),
    _PnnixRouteFailUnreachableBorder_Type()
)
pnnixRouteFailUnreachableBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteFailUnreachableBorder.setStatus("mandatory")
_PnnixNodeTable_Object = MibTable
pnnixNodeTable = _PnnixNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pnnixNodeTable.setStatus("mandatory")
_PnnixNodeEntry_Object = MibTableRow
pnnixNodeEntry = _PnnixNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1)
)
pnnixNodeEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
)
if mibBuilder.loadTexts:
    pnnixNodeEntry.setStatus("mandatory")
_PnnixNodeIndex_Type = PnnixNodeIndex
_PnnixNodeIndex_Object = MibTableColumn
pnnixNodeIndex = _PnnixNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 1),
    _PnnixNodeIndex_Type()
)
pnnixNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixNodeIndex.setStatus("mandatory")
_PnnixNodeLevel_Type = PnnixLevel
_PnnixNodeLevel_Object = MibTableColumn
pnnixNodeLevel = _PnnixNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 2),
    _PnnixNodeLevel_Type()
)
pnnixNodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeLevel.setStatus("mandatory")
_PnnixNodeId_Type = PnnixNodeId
_PnnixNodeId_Object = MibTableColumn
pnnixNodeId = _PnnixNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 3),
    _PnnixNodeId_Type()
)
pnnixNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeId.setStatus("mandatory")
_PnnixNodeLowest_Type = TruthValue
_PnnixNodeLowest_Object = MibTableColumn
pnnixNodeLowest = _PnnixNodeLowest_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 4),
    _PnnixNodeLowest_Type()
)
pnnixNodeLowest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeLowest.setStatus("mandatory")


class _PnnixNodeAdminStatus_Type(Integer32):
    """Custom type pnnixNodeAdminStatus based on Integer32"""
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


_PnnixNodeAdminStatus_Type.__name__ = "Integer32"
_PnnixNodeAdminStatus_Object = MibTableColumn
pnnixNodeAdminStatus = _PnnixNodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 5),
    _PnnixNodeAdminStatus_Type()
)
pnnixNodeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeAdminStatus.setStatus("mandatory")


class _PnnixNodeOperStatus_Type(Integer32):
    """Custom type pnnixNodeOperStatus based on Integer32"""
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


_PnnixNodeOperStatus_Type.__name__ = "Integer32"
_PnnixNodeOperStatus_Object = MibTableColumn
pnnixNodeOperStatus = _PnnixNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 6),
    _PnnixNodeOperStatus_Type()
)
pnnixNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodeOperStatus.setStatus("mandatory")
_PnnixNodeDomainName_Type = DisplayString
_PnnixNodeDomainName_Object = MibTableColumn
pnnixNodeDomainName = _PnnixNodeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 7),
    _PnnixNodeDomainName_Type()
)
pnnixNodeDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeDomainName.setStatus("mandatory")
_PnnixNodeAtmAddress_Type = PnnixAtmAddr
_PnnixNodeAtmAddress_Object = MibTableColumn
pnnixNodeAtmAddress = _PnnixNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 8),
    _PnnixNodeAtmAddress_Type()
)
pnnixNodeAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeAtmAddress.setStatus("mandatory")
_PnnixNodePeerGroupId_Type = PnnixPeerGroupId
_PnnixNodePeerGroupId_Object = MibTableColumn
pnnixNodePeerGroupId = _PnnixNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 9),
    _PnnixNodePeerGroupId_Type()
)
pnnixNodePeerGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePeerGroupId.setStatus("mandatory")
_PnnixNodeRestrictedTransit_Type = TruthValue
_PnnixNodeRestrictedTransit_Object = MibTableColumn
pnnixNodeRestrictedTransit = _PnnixNodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 10),
    _PnnixNodeRestrictedTransit_Type()
)
pnnixNodeRestrictedTransit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeRestrictedTransit.setStatus("mandatory")
_PnnixNodeComplexRep_Type = TruthValue
_PnnixNodeComplexRep_Object = MibTableColumn
pnnixNodeComplexRep = _PnnixNodeComplexRep_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 11),
    _PnnixNodeComplexRep_Type()
)
pnnixNodeComplexRep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeComplexRep.setStatus("mandatory")
_PnnixNodeRestrictedBranching_Type = TruthValue
_PnnixNodeRestrictedBranching_Object = MibTableColumn
pnnixNodeRestrictedBranching = _PnnixNodeRestrictedBranching_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 12),
    _PnnixNodeRestrictedBranching_Type()
)
pnnixNodeRestrictedBranching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodeRestrictedBranching.setStatus("mandatory")
_PnnixNodeDatabaseOverload_Type = TruthValue
_PnnixNodeDatabaseOverload_Object = MibTableColumn
pnnixNodeDatabaseOverload = _PnnixNodeDatabaseOverload_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 13),
    _PnnixNodeDatabaseOverload_Type()
)
pnnixNodeDatabaseOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodeDatabaseOverload.setStatus("mandatory")
_PnnixNodePtses_Type = Gauge32
_PnnixNodePtses_Object = MibTableColumn
pnnixNodePtses = _PnnixNodePtses_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 14),
    _PnnixNodePtses_Type()
)
pnnixNodePtses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodePtses.setStatus("mandatory")


class _PnnixNodeRowStatus_Type(Integer32):
    """Custom type pnnixNodeRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixNodeRowStatus_Type.__name__ = "Integer32"
_PnnixNodeRowStatus_Object = MibTableColumn
pnnixNodeRowStatus = _PnnixNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 2, 1, 15),
    _PnnixNodeRowStatus_Type()
)
pnnixNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeRowStatus.setStatus("mandatory")
_PnnixNodePglTable_Object = MibTable
pnnixNodePglTable = _PnnixNodePglTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pnnixNodePglTable.setStatus("mandatory")
_PnnixNodePglEntry_Object = MibTableRow
pnnixNodePglEntry = _PnnixNodePglEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1)
)
pnnixNodePglEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
)
if mibBuilder.loadTexts:
    pnnixNodePglEntry.setStatus("mandatory")


class _PnnixNodePglLeadershipPriority_Type(Integer32):
    """Custom type pnnixNodePglLeadershipPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 205),
    )


_PnnixNodePglLeadershipPriority_Type.__name__ = "Integer32"
_PnnixNodePglLeadershipPriority_Object = MibTableColumn
pnnixNodePglLeadershipPriority = _PnnixNodePglLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 1),
    _PnnixNodePglLeadershipPriority_Type()
)
pnnixNodePglLeadershipPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePglLeadershipPriority.setStatus("mandatory")
_PnnixNodeCfgParentNodeIndex_Type = PnnixNodeIndex
_PnnixNodeCfgParentNodeIndex_Object = MibTableColumn
pnnixNodeCfgParentNodeIndex = _PnnixNodeCfgParentNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 2),
    _PnnixNodeCfgParentNodeIndex_Type()
)
pnnixNodeCfgParentNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeCfgParentNodeIndex.setStatus("mandatory")
_PnnixNodePglInitTime_Type = Integer32
_PnnixNodePglInitTime_Object = MibTableColumn
pnnixNodePglInitTime = _PnnixNodePglInitTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 3),
    _PnnixNodePglInitTime_Type()
)
pnnixNodePglInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePglInitTime.setStatus("mandatory")
_PnnixNodePglOverrideDelay_Type = Integer32
_PnnixNodePglOverrideDelay_Object = MibTableColumn
pnnixNodePglOverrideDelay = _PnnixNodePglOverrideDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 4),
    _PnnixNodePglOverrideDelay_Type()
)
pnnixNodePglOverrideDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePglOverrideDelay.setStatus("mandatory")
_PnnixNodePglReelectTime_Type = Integer32
_PnnixNodePglReelectTime_Object = MibTableColumn
pnnixNodePglReelectTime = _PnnixNodePglReelectTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 5),
    _PnnixNodePglReelectTime_Type()
)
pnnixNodePglReelectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePglReelectTime.setStatus("mandatory")


class _PnnixNodePglState_Type(Integer32):
    """Custom type pnnixNodePglState based on Integer32"""
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


_PnnixNodePglState_Type.__name__ = "Integer32"
_PnnixNodePglState_Object = MibTableColumn
pnnixNodePglState = _PnnixNodePglState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 6),
    _PnnixNodePglState_Type()
)
pnnixNodePglState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodePglState.setStatus("mandatory")
_PnnixNodePreferredPgl_Type = PnnixNodeId
_PnnixNodePreferredPgl_Object = MibTableColumn
pnnixNodePreferredPgl = _PnnixNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 7),
    _PnnixNodePreferredPgl_Type()
)
pnnixNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodePreferredPgl.setStatus("mandatory")
_PnnixNodePeerGroupLeader_Type = PnnixNodeId
_PnnixNodePeerGroupLeader_Object = MibTableColumn
pnnixNodePeerGroupLeader = _PnnixNodePeerGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 8),
    _PnnixNodePeerGroupLeader_Type()
)
pnnixNodePeerGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodePeerGroupLeader.setStatus("mandatory")
_PnnixNodePglTimeStamp_Type = DisplayString
_PnnixNodePglTimeStamp_Object = MibTableColumn
pnnixNodePglTimeStamp = _PnnixNodePglTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 9),
    _PnnixNodePglTimeStamp_Type()
)
pnnixNodePglTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodePglTimeStamp.setStatus("mandatory")
_PnnixNodeActiveParentNodeId_Type = PnnixNodeId
_PnnixNodeActiveParentNodeId_Object = MibTableColumn
pnnixNodeActiveParentNodeId = _PnnixNodeActiveParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 3, 1, 10),
    _PnnixNodeActiveParentNodeId_Type()
)
pnnixNodeActiveParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNodeActiveParentNodeId.setStatus("mandatory")
_PnnixNodeTimerTable_Object = MibTable
pnnixNodeTimerTable = _PnnixNodeTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pnnixNodeTimerTable.setStatus("mandatory")
_PnnixNodeTimerEntry_Object = MibTableRow
pnnixNodeTimerEntry = _PnnixNodeTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1)
)
pnnixNodeTimerEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
)
if mibBuilder.loadTexts:
    pnnixNodeTimerEntry.setStatus("mandatory")
_PnnixNodePtseHolddown_Type = Integer32
_PnnixNodePtseHolddown_Object = MibTableColumn
pnnixNodePtseHolddown = _PnnixNodePtseHolddown_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 1),
    _PnnixNodePtseHolddown_Type()
)
pnnixNodePtseHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePtseHolddown.setStatus("mandatory")
_PnnixNodeHelloHolddown_Type = Integer32
_PnnixNodeHelloHolddown_Object = MibTableColumn
pnnixNodeHelloHolddown = _PnnixNodeHelloHolddown_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 2),
    _PnnixNodeHelloHolddown_Type()
)
pnnixNodeHelloHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeHelloHolddown.setStatus("mandatory")
_PnnixNodeHelloInterval_Type = Integer32
_PnnixNodeHelloInterval_Object = MibTableColumn
pnnixNodeHelloInterval = _PnnixNodeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 3),
    _PnnixNodeHelloInterval_Type()
)
pnnixNodeHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeHelloInterval.setStatus("mandatory")
_PnnixNodeHelloInactivityFactor_Type = Integer32
_PnnixNodeHelloInactivityFactor_Object = MibTableColumn
pnnixNodeHelloInactivityFactor = _PnnixNodeHelloInactivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 4),
    _PnnixNodeHelloInactivityFactor_Type()
)
pnnixNodeHelloInactivityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeHelloInactivityFactor.setStatus("mandatory")
_PnnixNodeHlinkInact_Type = Integer32
_PnnixNodeHlinkInact_Object = MibTableColumn
pnnixNodeHlinkInact = _PnnixNodeHlinkInact_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 5),
    _PnnixNodeHlinkInact_Type()
)
pnnixNodeHlinkInact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeHlinkInact.setStatus("mandatory")
_PnnixNodePtseRefreshInterval_Type = Integer32
_PnnixNodePtseRefreshInterval_Object = MibTableColumn
pnnixNodePtseRefreshInterval = _PnnixNodePtseRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 6),
    _PnnixNodePtseRefreshInterval_Type()
)
pnnixNodePtseRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePtseRefreshInterval.setStatus("mandatory")


class _PnnixNodePtseLifetimeFactor_Type(Integer32):
    """Custom type pnnixNodePtseLifetimeFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 1000),
    )


_PnnixNodePtseLifetimeFactor_Type.__name__ = "Integer32"
_PnnixNodePtseLifetimeFactor_Object = MibTableColumn
pnnixNodePtseLifetimeFactor = _PnnixNodePtseLifetimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 7),
    _PnnixNodePtseLifetimeFactor_Type()
)
pnnixNodePtseLifetimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePtseLifetimeFactor.setStatus("mandatory")
_PnnixNodeRxmtInterval_Type = Integer32
_PnnixNodeRxmtInterval_Object = MibTableColumn
pnnixNodeRxmtInterval = _PnnixNodeRxmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 8),
    _PnnixNodeRxmtInterval_Type()
)
pnnixNodeRxmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeRxmtInterval.setStatus("mandatory")
_PnnixNodePeerDelayedAckInterval_Type = Integer32
_PnnixNodePeerDelayedAckInterval_Object = MibTableColumn
pnnixNodePeerDelayedAckInterval = _PnnixNodePeerDelayedAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 9),
    _PnnixNodePeerDelayedAckInterval_Type()
)
pnnixNodePeerDelayedAckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodePeerDelayedAckInterval.setStatus("mandatory")


class _PnnixNodeAvcrPm_Type(Integer32):
    """Custom type pnnixNodeAvcrPm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnnixNodeAvcrPm_Type.__name__ = "Integer32"
_PnnixNodeAvcrPm_Object = MibTableColumn
pnnixNodeAvcrPm = _PnnixNodeAvcrPm_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 10),
    _PnnixNodeAvcrPm_Type()
)
pnnixNodeAvcrPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeAvcrPm.setStatus("mandatory")


class _PnnixNodeAvcrMt_Type(Integer32):
    """Custom type pnnixNodeAvcrMt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnnixNodeAvcrMt_Type.__name__ = "Integer32"
_PnnixNodeAvcrMt_Object = MibTableColumn
pnnixNodeAvcrMt = _PnnixNodeAvcrMt_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 11),
    _PnnixNodeAvcrMt_Type()
)
pnnixNodeAvcrMt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeAvcrMt.setStatus("mandatory")


class _PnnixNodeCdvPm_Type(Integer32):
    """Custom type pnnixNodeCdvPm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnnixNodeCdvPm_Type.__name__ = "Integer32"
_PnnixNodeCdvPm_Object = MibTableColumn
pnnixNodeCdvPm = _PnnixNodeCdvPm_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 12),
    _PnnixNodeCdvPm_Type()
)
pnnixNodeCdvPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeCdvPm.setStatus("mandatory")


class _PnnixNodeCtdPm_Type(Integer32):
    """Custom type pnnixNodeCtdPm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PnnixNodeCtdPm_Type.__name__ = "Integer32"
_PnnixNodeCtdPm_Object = MibTableColumn
pnnixNodeCtdPm = _PnnixNodeCtdPm_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 4, 1, 13),
    _PnnixNodeCtdPm_Type()
)
pnnixNodeCtdPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeCtdPm.setStatus("mandatory")
_PnnixNodeSvccTable_Object = MibTable
pnnixNodeSvccTable = _PnnixNodeSvccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pnnixNodeSvccTable.setStatus("mandatory")
_PnnixNodeSvccEntry_Object = MibTableRow
pnnixNodeSvccEntry = _PnnixNodeSvccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1)
)
pnnixNodeSvccEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
)
if mibBuilder.loadTexts:
    pnnixNodeSvccEntry.setStatus("mandatory")
_PnnixNodeSvccInitTime_Type = Integer32
_PnnixNodeSvccInitTime_Object = MibTableColumn
pnnixNodeSvccInitTime = _PnnixNodeSvccInitTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1, 1),
    _PnnixNodeSvccInitTime_Type()
)
pnnixNodeSvccInitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeSvccInitTime.setStatus("mandatory")
_PnnixNodeSvccRetryTime_Type = Integer32
_PnnixNodeSvccRetryTime_Object = MibTableColumn
pnnixNodeSvccRetryTime = _PnnixNodeSvccRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1, 2),
    _PnnixNodeSvccRetryTime_Type()
)
pnnixNodeSvccRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeSvccRetryTime.setStatus("mandatory")
_PnnixNodeSvccCallingIntegrityTime_Type = Integer32
_PnnixNodeSvccCallingIntegrityTime_Object = MibTableColumn
pnnixNodeSvccCallingIntegrityTime = _PnnixNodeSvccCallingIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1, 3),
    _PnnixNodeSvccCallingIntegrityTime_Type()
)
pnnixNodeSvccCallingIntegrityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeSvccCallingIntegrityTime.setStatus("mandatory")
_PnnixNodeSvccCalledIntegrityTime_Type = Integer32
_PnnixNodeSvccCalledIntegrityTime_Object = MibTableColumn
pnnixNodeSvccCalledIntegrityTime = _PnnixNodeSvccCalledIntegrityTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1, 4),
    _PnnixNodeSvccCalledIntegrityTime_Type()
)
pnnixNodeSvccCalledIntegrityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeSvccCalledIntegrityTime.setStatus("mandatory")
_PnnixNodeSvccTrafficDescriptorIndex_Type = AtmpTrafficDescrParamIndex
_PnnixNodeSvccTrafficDescriptorIndex_Object = MibTableColumn
pnnixNodeSvccTrafficDescriptorIndex = _PnnixNodeSvccTrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 5, 1, 5),
    _PnnixNodeSvccTrafficDescriptorIndex_Type()
)
pnnixNodeSvccTrafficDescriptorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixNodeSvccTrafficDescriptorIndex.setStatus("mandatory")
_PnnixScopeMappingTable_Object = MibTable
pnnixScopeMappingTable = _PnnixScopeMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pnnixScopeMappingTable.setStatus("mandatory")
_PnnixScopeMappingEntry_Object = MibTableRow
pnnixScopeMappingEntry = _PnnixScopeMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1)
)
pnnixScopeMappingEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
)
if mibBuilder.loadTexts:
    pnnixScopeMappingEntry.setStatus("mandatory")
_PnnixScopeLocalNetwork_Type = PnnixLevel
_PnnixScopeLocalNetwork_Object = MibTableColumn
pnnixScopeLocalNetwork = _PnnixScopeLocalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 1),
    _PnnixScopeLocalNetwork_Type()
)
pnnixScopeLocalNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeLocalNetwork.setStatus("mandatory")
_PnnixScopeLocalNetworkPlusOne_Type = PnnixLevel
_PnnixScopeLocalNetworkPlusOne_Object = MibTableColumn
pnnixScopeLocalNetworkPlusOne = _PnnixScopeLocalNetworkPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 2),
    _PnnixScopeLocalNetworkPlusOne_Type()
)
pnnixScopeLocalNetworkPlusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeLocalNetworkPlusOne.setStatus("mandatory")
_PnnixScopeLocalNetworkPlusTwo_Type = PnnixLevel
_PnnixScopeLocalNetworkPlusTwo_Object = MibTableColumn
pnnixScopeLocalNetworkPlusTwo = _PnnixScopeLocalNetworkPlusTwo_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 3),
    _PnnixScopeLocalNetworkPlusTwo_Type()
)
pnnixScopeLocalNetworkPlusTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeLocalNetworkPlusTwo.setStatus("mandatory")
_PnnixScopeSiteMinusOne_Type = PnnixLevel
_PnnixScopeSiteMinusOne_Object = MibTableColumn
pnnixScopeSiteMinusOne = _PnnixScopeSiteMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 4),
    _PnnixScopeSiteMinusOne_Type()
)
pnnixScopeSiteMinusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeSiteMinusOne.setStatus("mandatory")
_PnnixScopeIntraSite_Type = PnnixLevel
_PnnixScopeIntraSite_Object = MibTableColumn
pnnixScopeIntraSite = _PnnixScopeIntraSite_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 5),
    _PnnixScopeIntraSite_Type()
)
pnnixScopeIntraSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeIntraSite.setStatus("mandatory")
_PnnixScopeSitePlusOne_Type = PnnixLevel
_PnnixScopeSitePlusOne_Object = MibTableColumn
pnnixScopeSitePlusOne = _PnnixScopeSitePlusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 6),
    _PnnixScopeSitePlusOne_Type()
)
pnnixScopeSitePlusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeSitePlusOne.setStatus("mandatory")
_PnnixScopeOrganizationMinusOne_Type = PnnixLevel
_PnnixScopeOrganizationMinusOne_Object = MibTableColumn
pnnixScopeOrganizationMinusOne = _PnnixScopeOrganizationMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 7),
    _PnnixScopeOrganizationMinusOne_Type()
)
pnnixScopeOrganizationMinusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeOrganizationMinusOne.setStatus("mandatory")
_PnnixScopeIntraOrganization_Type = PnnixLevel
_PnnixScopeIntraOrganization_Object = MibTableColumn
pnnixScopeIntraOrganization = _PnnixScopeIntraOrganization_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 8),
    _PnnixScopeIntraOrganization_Type()
)
pnnixScopeIntraOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeIntraOrganization.setStatus("mandatory")
_PnnixScopeOrganizationPlusOne_Type = PnnixLevel
_PnnixScopeOrganizationPlusOne_Object = MibTableColumn
pnnixScopeOrganizationPlusOne = _PnnixScopeOrganizationPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 9),
    _PnnixScopeOrganizationPlusOne_Type()
)
pnnixScopeOrganizationPlusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeOrganizationPlusOne.setStatus("mandatory")
_PnnixScopeCommunityMinusOne_Type = PnnixLevel
_PnnixScopeCommunityMinusOne_Object = MibTableColumn
pnnixScopeCommunityMinusOne = _PnnixScopeCommunityMinusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 10),
    _PnnixScopeCommunityMinusOne_Type()
)
pnnixScopeCommunityMinusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeCommunityMinusOne.setStatus("mandatory")
_PnnixScopeIntraCommunity_Type = PnnixLevel
_PnnixScopeIntraCommunity_Object = MibTableColumn
pnnixScopeIntraCommunity = _PnnixScopeIntraCommunity_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 11),
    _PnnixScopeIntraCommunity_Type()
)
pnnixScopeIntraCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeIntraCommunity.setStatus("mandatory")
_PnnixScopeCommunityPlusOne_Type = PnnixLevel
_PnnixScopeCommunityPlusOne_Object = MibTableColumn
pnnixScopeCommunityPlusOne = _PnnixScopeCommunityPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 12),
    _PnnixScopeCommunityPlusOne_Type()
)
pnnixScopeCommunityPlusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeCommunityPlusOne.setStatus("mandatory")
_PnnixScopeRegional_Type = PnnixLevel
_PnnixScopeRegional_Object = MibTableColumn
pnnixScopeRegional = _PnnixScopeRegional_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 13),
    _PnnixScopeRegional_Type()
)
pnnixScopeRegional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeRegional.setStatus("mandatory")
_PnnixScopeInterRegional_Type = PnnixLevel
_PnnixScopeInterRegional_Object = MibTableColumn
pnnixScopeInterRegional = _PnnixScopeInterRegional_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 14),
    _PnnixScopeInterRegional_Type()
)
pnnixScopeInterRegional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeInterRegional.setStatus("mandatory")
_PnnixScopeGlobal_Type = PnnixLevel
_PnnixScopeGlobal_Object = MibTableColumn
pnnixScopeGlobal = _PnnixScopeGlobal_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 6, 1, 15),
    _PnnixScopeGlobal_Type()
)
pnnixScopeGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixScopeGlobal.setStatus("mandatory")
_PnnixSummaryTable_Object = MibTable
pnnixSummaryTable = _PnnixSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    pnnixSummaryTable.setStatus("mandatory")
_PnnixSummaryEntry_Object = MibTableRow
pnnixSummaryEntry = _PnnixSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1)
)
pnnixSummaryEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixSummaryAddress"),
    (0, "XPNNI-MIB", "pnnixSummaryPrefixLength"),
)
if mibBuilder.loadTexts:
    pnnixSummaryEntry.setStatus("mandatory")
_PnnixSummaryAddress_Type = AtmAddrPrefix
_PnnixSummaryAddress_Object = MibTableColumn
pnnixSummaryAddress = _PnnixSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 1),
    _PnnixSummaryAddress_Type()
)
pnnixSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixSummaryAddress.setStatus("mandatory")
_PnnixSummaryPrefixLength_Type = PnnixPrefixLength
_PnnixSummaryPrefixLength_Object = MibTableColumn
pnnixSummaryPrefixLength = _PnnixSummaryPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 2),
    _PnnixSummaryPrefixLength_Type()
)
pnnixSummaryPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixSummaryPrefixLength.setStatus("mandatory")


class _PnnixSummaryType_Type(Integer32):
    """Custom type pnnixSummaryType based on Integer32"""
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


_PnnixSummaryType_Type.__name__ = "Integer32"
_PnnixSummaryType_Object = MibTableColumn
pnnixSummaryType = _PnnixSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 3),
    _PnnixSummaryType_Type()
)
pnnixSummaryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixSummaryType.setStatus("mandatory")
_PnnixSummarySuppress_Type = TruthValue
_PnnixSummarySuppress_Object = MibTableColumn
pnnixSummarySuppress = _PnnixSummarySuppress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 4),
    _PnnixSummarySuppress_Type()
)
pnnixSummarySuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixSummarySuppress.setStatus("mandatory")


class _PnnixSummaryState_Type(Integer32):
    """Custom type pnnixSummaryState based on Integer32"""
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


_PnnixSummaryState_Type.__name__ = "Integer32"
_PnnixSummaryState_Object = MibTableColumn
pnnixSummaryState = _PnnixSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 5),
    _PnnixSummaryState_Type()
)
pnnixSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSummaryState.setStatus("mandatory")


class _PnnixSummaryRowStatus_Type(Integer32):
    """Custom type pnnixSummaryRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixSummaryRowStatus_Type.__name__ = "Integer32"
_PnnixSummaryRowStatus_Object = MibTableColumn
pnnixSummaryRowStatus = _PnnixSummaryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 7, 1, 6),
    _PnnixSummaryRowStatus_Type()
)
pnnixSummaryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixSummaryRowStatus.setStatus("mandatory")
_PnnixIfTable_Object = MibTable
pnnixIfTable = _PnnixIfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    pnnixIfTable.setStatus("mandatory")
_PnnixIfEntry_Object = MibTableRow
pnnixIfEntry = _PnnixIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1)
)
pnnixIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pnnixIfEntry.setStatus("mandatory")
_PnnixIfNodeIndex_Type = PnnixNodeIndex
_PnnixIfNodeIndex_Object = MibTableColumn
pnnixIfNodeIndex = _PnnixIfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 1),
    _PnnixIfNodeIndex_Type()
)
pnnixIfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfNodeIndex.setStatus("mandatory")
_PnnixIfPortId_Type = PnnixPortId
_PnnixIfPortId_Object = MibTableColumn
pnnixIfPortId = _PnnixIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 2),
    _PnnixIfPortId_Type()
)
pnnixIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIfPortId.setStatus("mandatory")
_PnnixIfAggrToken_Type = PnnixAggrToken
_PnnixIfAggrToken_Object = MibTableColumn
pnnixIfAggrToken = _PnnixIfAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 3),
    _PnnixIfAggrToken_Type()
)
pnnixIfAggrToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAggrToken.setStatus("mandatory")
_PnnixIfVPCapability_Type = TruthValue
_PnnixIfVPCapability_Object = MibTableColumn
pnnixIfVPCapability = _PnnixIfVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 4),
    _PnnixIfVPCapability_Type()
)
pnnixIfVPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfVPCapability.setStatus("mandatory")
_PnnixIfAdmWeightCbr_Type = Gauge32
_PnnixIfAdmWeightCbr_Object = MibTableColumn
pnnixIfAdmWeightCbr = _PnnixIfAdmWeightCbr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 5),
    _PnnixIfAdmWeightCbr_Type()
)
pnnixIfAdmWeightCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAdmWeightCbr.setStatus("mandatory")
_PnnixIfAdmWeightRtVbr_Type = Gauge32
_PnnixIfAdmWeightRtVbr_Object = MibTableColumn
pnnixIfAdmWeightRtVbr = _PnnixIfAdmWeightRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 6),
    _PnnixIfAdmWeightRtVbr_Type()
)
pnnixIfAdmWeightRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAdmWeightRtVbr.setStatus("mandatory")
_PnnixIfAdmWeightNrtVbr_Type = Gauge32
_PnnixIfAdmWeightNrtVbr_Object = MibTableColumn
pnnixIfAdmWeightNrtVbr = _PnnixIfAdmWeightNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 7),
    _PnnixIfAdmWeightNrtVbr_Type()
)
pnnixIfAdmWeightNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAdmWeightNrtVbr.setStatus("mandatory")
_PnnixIfAdmWeightAbr_Type = Gauge32
_PnnixIfAdmWeightAbr_Object = MibTableColumn
pnnixIfAdmWeightAbr = _PnnixIfAdmWeightAbr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 8),
    _PnnixIfAdmWeightAbr_Type()
)
pnnixIfAdmWeightAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAdmWeightAbr.setStatus("mandatory")
_PnnixIfAdmWeightUbr_Type = Gauge32
_PnnixIfAdmWeightUbr_Object = MibTableColumn
pnnixIfAdmWeightUbr = _PnnixIfAdmWeightUbr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 9),
    _PnnixIfAdmWeightUbr_Type()
)
pnnixIfAdmWeightUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfAdmWeightUbr.setStatus("mandatory")
_PnnixIfRccServiceCategory_Type = ServiceCategory
_PnnixIfRccServiceCategory_Object = MibTableColumn
pnnixIfRccServiceCategory = _PnnixIfRccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 10),
    _PnnixIfRccServiceCategory_Type()
)
pnnixIfRccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfRccServiceCategory.setStatus("mandatory")
_PnnixIfRccTrafficDescrIndex_Type = AtmpTrafficDescrParamIndex
_PnnixIfRccTrafficDescrIndex_Object = MibTableColumn
pnnixIfRccTrafficDescrIndex = _PnnixIfRccTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 8, 1, 11),
    _PnnixIfRccTrafficDescrIndex_Type()
)
pnnixIfRccTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixIfRccTrafficDescrIndex.setStatus("mandatory")
_PnnixLinkTable_Object = MibTable
pnnixLinkTable = _PnnixLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    pnnixLinkTable.setStatus("mandatory")
_PnnixLinkEntry_Object = MibTableRow
pnnixLinkEntry = _PnnixLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1)
)
pnnixLinkEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixLinkPortId"),
)
if mibBuilder.loadTexts:
    pnnixLinkEntry.setStatus("mandatory")
_PnnixLinkPortId_Type = Integer32
_PnnixLinkPortId_Object = MibTableColumn
pnnixLinkPortId = _PnnixLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 1),
    _PnnixLinkPortId_Type()
)
pnnixLinkPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixLinkPortId.setStatus("mandatory")


class _PnnixLinkType_Type(Integer32):
    """Custom type pnnixLinkType based on Integer32"""
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


_PnnixLinkType_Type.__name__ = "Integer32"
_PnnixLinkType_Object = MibTableColumn
pnnixLinkType = _PnnixLinkType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 2),
    _PnnixLinkType_Type()
)
pnnixLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkType.setStatus("mandatory")
_PnnixLinkVersion_Type = PnnixVersion
_PnnixLinkVersion_Object = MibTableColumn
pnnixLinkVersion = _PnnixLinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 3),
    _PnnixLinkVersion_Type()
)
pnnixLinkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkVersion.setStatus("mandatory")
_PnnixLinkHelloState_Type = PnnixHelloState
_PnnixLinkHelloState_Object = MibTableColumn
pnnixLinkHelloState = _PnnixLinkHelloState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 4),
    _PnnixLinkHelloState_Type()
)
pnnixLinkHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkHelloState.setStatus("mandatory")
_PnnixLinkRemoteNodeId_Type = PnnixNodeId
_PnnixLinkRemoteNodeId_Object = MibTableColumn
pnnixLinkRemoteNodeId = _PnnixLinkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 5),
    _PnnixLinkRemoteNodeId_Type()
)
pnnixLinkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkRemoteNodeId.setStatus("mandatory")
_PnnixLinkRemotePortId_Type = PnnixPortId
_PnnixLinkRemotePortId_Object = MibTableColumn
pnnixLinkRemotePortId = _PnnixLinkRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 6),
    _PnnixLinkRemotePortId_Type()
)
pnnixLinkRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkRemotePortId.setStatus("mandatory")
_PnnixLinkDerivedAggrToken_Type = PnnixAggrToken
_PnnixLinkDerivedAggrToken_Object = MibTableColumn
pnnixLinkDerivedAggrToken = _PnnixLinkDerivedAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 7),
    _PnnixLinkDerivedAggrToken_Type()
)
pnnixLinkDerivedAggrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkDerivedAggrToken.setStatus("mandatory")
_PnnixLinkUpnodeId_Type = PnnixNodeId
_PnnixLinkUpnodeId_Object = MibTableColumn
pnnixLinkUpnodeId = _PnnixLinkUpnodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 8),
    _PnnixLinkUpnodeId_Type()
)
pnnixLinkUpnodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkUpnodeId.setStatus("mandatory")
_PnnixLinkUpnodeAtmAddress_Type = PnnixAtmAddr
_PnnixLinkUpnodeAtmAddress_Object = MibTableColumn
pnnixLinkUpnodeAtmAddress = _PnnixLinkUpnodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 9),
    _PnnixLinkUpnodeAtmAddress_Type()
)
pnnixLinkUpnodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkUpnodeAtmAddress.setStatus("mandatory")
_PnnixLinkCommonPeerGroupId_Type = PnnixPeerGroupId
_PnnixLinkCommonPeerGroupId_Object = MibTableColumn
pnnixLinkCommonPeerGroupId = _PnnixLinkCommonPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 10),
    _PnnixLinkCommonPeerGroupId_Type()
)
pnnixLinkCommonPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkCommonPeerGroupId.setStatus("mandatory")
_PnnixLinkIfIndex_Type = InterfaceIndex
_PnnixLinkIfIndex_Object = MibTableColumn
pnnixLinkIfIndex = _PnnixLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 11),
    _PnnixLinkIfIndex_Type()
)
pnnixLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkIfIndex.setStatus("mandatory")
_PnnixLinkSvccRccIndex_Type = PnnixSvccRccIndex
_PnnixLinkSvccRccIndex_Object = MibTableColumn
pnnixLinkSvccRccIndex = _PnnixLinkSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 12),
    _PnnixLinkSvccRccIndex_Type()
)
pnnixLinkSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkSvccRccIndex.setStatus("mandatory")
_PnnixLinkRcvHellos_Type = Counter32
_PnnixLinkRcvHellos_Object = MibTableColumn
pnnixLinkRcvHellos = _PnnixLinkRcvHellos_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 13),
    _PnnixLinkRcvHellos_Type()
)
pnnixLinkRcvHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkRcvHellos.setStatus("mandatory")
_PnnixLinkXmtHellos_Type = Counter32
_PnnixLinkXmtHellos_Object = MibTableColumn
pnnixLinkXmtHellos = _PnnixLinkXmtHellos_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 9, 1, 14),
    _PnnixLinkXmtHellos_Type()
)
pnnixLinkXmtHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixLinkXmtHellos.setStatus("mandatory")
_PnnixNbrPeerTable_Object = MibTable
pnnixNbrPeerTable = _PnnixNbrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    pnnixNbrPeerTable.setStatus("mandatory")
_PnnixNbrPeerEntry_Object = MibTableRow
pnnixNbrPeerEntry = _PnnixNbrPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1)
)
pnnixNbrPeerEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixNbrPeerRemoteNodeId"),
)
if mibBuilder.loadTexts:
    pnnixNbrPeerEntry.setStatus("mandatory")
_PnnixNbrPeerRemoteNodeId_Type = PnnixNodeId
_PnnixNbrPeerRemoteNodeId_Object = MibTableColumn
pnnixNbrPeerRemoteNodeId = _PnnixNbrPeerRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 1),
    _PnnixNbrPeerRemoteNodeId_Type()
)
pnnixNbrPeerRemoteNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixNbrPeerRemoteNodeId.setStatus("mandatory")


class _PnnixNbrPeerState_Type(Integer32):
    """Custom type pnnixNbrPeerState based on Integer32"""
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


_PnnixNbrPeerState_Type.__name__ = "Integer32"
_PnnixNbrPeerState_Object = MibTableColumn
pnnixNbrPeerState = _PnnixNbrPeerState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 2),
    _PnnixNbrPeerState_Type()
)
pnnixNbrPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerState.setStatus("mandatory")
_PnnixNbrPeerSvccRccIndex_Type = PnnixSvccRccIndex
_PnnixNbrPeerSvccRccIndex_Object = MibTableColumn
pnnixNbrPeerSvccRccIndex = _PnnixNbrPeerSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 3),
    _PnnixNbrPeerSvccRccIndex_Type()
)
pnnixNbrPeerSvccRccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerSvccRccIndex.setStatus("mandatory")
_PnnixNbrPeerPortCount_Type = Gauge32
_PnnixNbrPeerPortCount_Object = MibTableColumn
pnnixNbrPeerPortCount = _PnnixNbrPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 4),
    _PnnixNbrPeerPortCount_Type()
)
pnnixNbrPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerPortCount.setStatus("mandatory")
_PnnixNbrPeerRcvDbSums_Type = Counter32
_PnnixNbrPeerRcvDbSums_Object = MibTableColumn
pnnixNbrPeerRcvDbSums = _PnnixNbrPeerRcvDbSums_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 5),
    _PnnixNbrPeerRcvDbSums_Type()
)
pnnixNbrPeerRcvDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerRcvDbSums.setStatus("mandatory")
_PnnixNbrPeerXmtDbSums_Type = Counter32
_PnnixNbrPeerXmtDbSums_Object = MibTableColumn
pnnixNbrPeerXmtDbSums = _PnnixNbrPeerXmtDbSums_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 6),
    _PnnixNbrPeerXmtDbSums_Type()
)
pnnixNbrPeerXmtDbSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerXmtDbSums.setStatus("mandatory")
_PnnixNbrPeerRcvPtsps_Type = Counter32
_PnnixNbrPeerRcvPtsps_Object = MibTableColumn
pnnixNbrPeerRcvPtsps = _PnnixNbrPeerRcvPtsps_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 7),
    _PnnixNbrPeerRcvPtsps_Type()
)
pnnixNbrPeerRcvPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerRcvPtsps.setStatus("mandatory")
_PnnixNbrPeerXmtPtsps_Type = Counter32
_PnnixNbrPeerXmtPtsps_Object = MibTableColumn
pnnixNbrPeerXmtPtsps = _PnnixNbrPeerXmtPtsps_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 8),
    _PnnixNbrPeerXmtPtsps_Type()
)
pnnixNbrPeerXmtPtsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerXmtPtsps.setStatus("mandatory")
_PnnixNbrPeerRcvPtseReqs_Type = Counter32
_PnnixNbrPeerRcvPtseReqs_Object = MibTableColumn
pnnixNbrPeerRcvPtseReqs = _PnnixNbrPeerRcvPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 9),
    _PnnixNbrPeerRcvPtseReqs_Type()
)
pnnixNbrPeerRcvPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerRcvPtseReqs.setStatus("mandatory")
_PnnixNbrPeerXmtPtseReqs_Type = Counter32
_PnnixNbrPeerXmtPtseReqs_Object = MibTableColumn
pnnixNbrPeerXmtPtseReqs = _PnnixNbrPeerXmtPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 10),
    _PnnixNbrPeerXmtPtseReqs_Type()
)
pnnixNbrPeerXmtPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerXmtPtseReqs.setStatus("mandatory")
_PnnixNbrPeerRcvPtseAcks_Type = Counter32
_PnnixNbrPeerRcvPtseAcks_Object = MibTableColumn
pnnixNbrPeerRcvPtseAcks = _PnnixNbrPeerRcvPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 11),
    _PnnixNbrPeerRcvPtseAcks_Type()
)
pnnixNbrPeerRcvPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerRcvPtseAcks.setStatus("mandatory")
_PnnixNbrPeerXmtPtseAcks_Type = Counter32
_PnnixNbrPeerXmtPtseAcks_Object = MibTableColumn
pnnixNbrPeerXmtPtseAcks = _PnnixNbrPeerXmtPtseAcks_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 10, 1, 12),
    _PnnixNbrPeerXmtPtseAcks_Type()
)
pnnixNbrPeerXmtPtseAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerXmtPtseAcks.setStatus("mandatory")
_PnnixNbrPeerPortTable_Object = MibTable
pnnixNbrPeerPortTable = _PnnixNbrPeerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pnnixNbrPeerPortTable.setStatus("mandatory")
_PnnixNbrPeerPortEntry_Object = MibTableRow
pnnixNbrPeerPortEntry = _PnnixNbrPeerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 11, 1)
)
pnnixNbrPeerPortEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixNbrPeerRemoteNodeId"),
    (0, "XPNNI-MIB", "pnnixNbrPeerPortId"),
)
if mibBuilder.loadTexts:
    pnnixNbrPeerPortEntry.setStatus("mandatory")
_PnnixNbrPeerPortId_Type = Integer32
_PnnixNbrPeerPortId_Object = MibTableColumn
pnnixNbrPeerPortId = _PnnixNbrPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 11, 1, 1),
    _PnnixNbrPeerPortId_Type()
)
pnnixNbrPeerPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixNbrPeerPortId.setStatus("mandatory")
_PnnixNbrPeerPortFloodStatus_Type = TruthValue
_PnnixNbrPeerPortFloodStatus_Object = MibTableColumn
pnnixNbrPeerPortFloodStatus = _PnnixNbrPeerPortFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 11, 1, 2),
    _PnnixNbrPeerPortFloodStatus_Type()
)
pnnixNbrPeerPortFloodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNbrPeerPortFloodStatus.setStatus("mandatory")
_PnnixSvccRccTable_Object = MibTable
pnnixSvccRccTable = _PnnixSvccRccTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pnnixSvccRccTable.setStatus("mandatory")
_PnnixSvccRccEntry_Object = MibTableRow
pnnixSvccRccEntry = _PnnixSvccRccEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1)
)
pnnixSvccRccEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixSvccRccIndex"),
)
if mibBuilder.loadTexts:
    pnnixSvccRccEntry.setStatus("mandatory")
_PnnixSvccRccIndex_Type = PnnixSvccRccIndex
_PnnixSvccRccIndex_Object = MibTableColumn
pnnixSvccRccIndex = _PnnixSvccRccIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 1),
    _PnnixSvccRccIndex_Type()
)
pnnixSvccRccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixSvccRccIndex.setStatus("mandatory")
_PnnixSvccRccVersion_Type = PnnixVersion
_PnnixSvccRccVersion_Object = MibTableColumn
pnnixSvccRccVersion = _PnnixSvccRccVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 2),
    _PnnixSvccRccVersion_Type()
)
pnnixSvccRccVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccVersion.setStatus("mandatory")
_PnnixSvccRccHelloState_Type = PnnixHelloState
_PnnixSvccRccHelloState_Object = MibTableColumn
pnnixSvccRccHelloState = _PnnixSvccRccHelloState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 3),
    _PnnixSvccRccHelloState_Type()
)
pnnixSvccRccHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccHelloState.setStatus("mandatory")
_PnnixSvccRccRemoteNodeId_Type = PnnixNodeId
_PnnixSvccRccRemoteNodeId_Object = MibTableColumn
pnnixSvccRccRemoteNodeId = _PnnixSvccRccRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 4),
    _PnnixSvccRccRemoteNodeId_Type()
)
pnnixSvccRccRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccRemoteNodeId.setStatus("mandatory")
_PnnixSvccRccRemoteAtmAddress_Type = PnnixAtmAddr
_PnnixSvccRccRemoteAtmAddress_Object = MibTableColumn
pnnixSvccRccRemoteAtmAddress = _PnnixSvccRccRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 5),
    _PnnixSvccRccRemoteAtmAddress_Type()
)
pnnixSvccRccRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccRemoteAtmAddress.setStatus("mandatory")
_PnnixSvccRccRcvHellos_Type = Counter32
_PnnixSvccRccRcvHellos_Object = MibTableColumn
pnnixSvccRccRcvHellos = _PnnixSvccRccRcvHellos_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 6),
    _PnnixSvccRccRcvHellos_Type()
)
pnnixSvccRccRcvHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccRcvHellos.setStatus("mandatory")
_PnnixSvccRccXmtHellos_Type = Counter32
_PnnixSvccRccXmtHellos_Object = MibTableColumn
pnnixSvccRccXmtHellos = _PnnixSvccRccXmtHellos_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 7),
    _PnnixSvccRccXmtHellos_Type()
)
pnnixSvccRccXmtHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccXmtHellos.setStatus("mandatory")
_PnnixSvccRccIfIndex_Type = InterfaceIndex
_PnnixSvccRccIfIndex_Object = MibTableColumn
pnnixSvccRccIfIndex = _PnnixSvccRccIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 8),
    _PnnixSvccRccIfIndex_Type()
)
pnnixSvccRccIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccIfIndex.setStatus("mandatory")


class _PnnixSvccRccVpi_Type(Integer32):
    """Custom type pnnixSvccRccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PnnixSvccRccVpi_Type.__name__ = "Integer32"
_PnnixSvccRccVpi_Object = MibTableColumn
pnnixSvccRccVpi = _PnnixSvccRccVpi_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 9),
    _PnnixSvccRccVpi_Type()
)
pnnixSvccRccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccVpi.setStatus("mandatory")


class _PnnixSvccRccVci_Type(Integer32):
    """Custom type pnnixSvccRccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnnixSvccRccVci_Type.__name__ = "Integer32"
_PnnixSvccRccVci_Object = MibTableColumn
pnnixSvccRccVci = _PnnixSvccRccVci_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 12, 1, 10),
    _PnnixSvccRccVci_Type()
)
pnnixSvccRccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixSvccRccVci.setStatus("mandatory")
_PnnixPtseTable_Object = MibTable
pnnixPtseTable = _PnnixPtseTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    pnnixPtseTable.setStatus("mandatory")
_PnnixPtseEntry_Object = MibTableRow
pnnixPtseEntry = _PnnixPtseEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1)
)
pnnixPtseEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixPtseOriginatingNodeId"),
    (0, "XPNNI-MIB", "pnnixPtseId"),
)
if mibBuilder.loadTexts:
    pnnixPtseEntry.setStatus("mandatory")
_PnnixPtseOriginatingNodeId_Type = PnnixNodeId
_PnnixPtseOriginatingNodeId_Object = MibTableColumn
pnnixPtseOriginatingNodeId = _PnnixPtseOriginatingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 1),
    _PnnixPtseOriginatingNodeId_Type()
)
pnnixPtseOriginatingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixPtseOriginatingNodeId.setStatus("mandatory")
_PnnixPtseId_Type = Integer32
_PnnixPtseId_Object = MibTableColumn
pnnixPtseId = _PnnixPtseId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 2),
    _PnnixPtseId_Type()
)
pnnixPtseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixPtseId.setStatus("mandatory")


class _PnnixPtseType_Type(Integer32):
    """Custom type pnnixPtseType based on Integer32"""
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


_PnnixPtseType_Type.__name__ = "Integer32"
_PnnixPtseType_Object = MibTableColumn
pnnixPtseType = _PnnixPtseType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 3),
    _PnnixPtseType_Type()
)
pnnixPtseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixPtseType.setStatus("mandatory")
_PnnixPtseSequenceNum_Type = Gauge32
_PnnixPtseSequenceNum_Object = MibTableColumn
pnnixPtseSequenceNum = _PnnixPtseSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 4),
    _PnnixPtseSequenceNum_Type()
)
pnnixPtseSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixPtseSequenceNum.setStatus("mandatory")
_PnnixPtseChecksum_Type = Gauge32
_PnnixPtseChecksum_Object = MibTableColumn
pnnixPtseChecksum = _PnnixPtseChecksum_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 5),
    _PnnixPtseChecksum_Type()
)
pnnixPtseChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixPtseChecksum.setStatus("mandatory")
_PnnixPtseLifeTime_Type = Gauge32
_PnnixPtseLifeTime_Object = MibTableColumn
pnnixPtseLifeTime = _PnnixPtseLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 6),
    _PnnixPtseLifeTime_Type()
)
pnnixPtseLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixPtseLifeTime.setStatus("mandatory")


class _PnnixPtseInfo_Type(OctetString):
    """Custom type pnnixPtseInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_PnnixPtseInfo_Type.__name__ = "OctetString"
_PnnixPtseInfo_Object = MibTableColumn
pnnixPtseInfo = _PnnixPtseInfo_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 13, 1, 7),
    _PnnixPtseInfo_Type()
)
pnnixPtseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixPtseInfo.setStatus("mandatory")
_PnnixMapTable_Object = MibTable
pnnixMapTable = _PnnixMapTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    pnnixMapTable.setStatus("mandatory")
_PnnixMapEntry_Object = MibTableRow
pnnixMapEntry = _PnnixMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1)
)
pnnixMapEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixMapOriginatingNodeId"),
    (0, "XPNNI-MIB", "pnnixMapOriginatingPortId"),
    (0, "XPNNI-MIB", "pnnixMapIndex"),
)
if mibBuilder.loadTexts:
    pnnixMapEntry.setStatus("mandatory")
_PnnixMapOriginatingNodeId_Type = PnnixNodeId
_PnnixMapOriginatingNodeId_Object = MibTableColumn
pnnixMapOriginatingNodeId = _PnnixMapOriginatingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 1),
    _PnnixMapOriginatingNodeId_Type()
)
pnnixMapOriginatingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapOriginatingNodeId.setStatus("mandatory")
_PnnixMapOriginatingPortId_Type = Integer32
_PnnixMapOriginatingPortId_Object = MibTableColumn
pnnixMapOriginatingPortId = _PnnixMapOriginatingPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 2),
    _PnnixMapOriginatingPortId_Type()
)
pnnixMapOriginatingPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapOriginatingPortId.setStatus("mandatory")


class _PnnixMapIndex_Type(Integer32):
    """Custom type pnnixMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PnnixMapIndex_Type.__name__ = "Integer32"
_PnnixMapIndex_Object = MibTableColumn
pnnixMapIndex = _PnnixMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 3),
    _PnnixMapIndex_Type()
)
pnnixMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapIndex.setStatus("mandatory")


class _PnnixMapType_Type(Integer32):
    """Custom type pnnixMapType based on Integer32"""
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


_PnnixMapType_Type.__name__ = "Integer32"
_PnnixMapType_Object = MibTableColumn
pnnixMapType = _PnnixMapType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 4),
    _PnnixMapType_Type()
)
pnnixMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapType.setStatus("mandatory")
_PnnixMapPeerGroupId_Type = PnnixPeerGroupId
_PnnixMapPeerGroupId_Object = MibTableColumn
pnnixMapPeerGroupId = _PnnixMapPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 5),
    _PnnixMapPeerGroupId_Type()
)
pnnixMapPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapPeerGroupId.setStatus("mandatory")
_PnnixMapAggrToken_Type = PnnixAggrToken
_PnnixMapAggrToken_Object = MibTableColumn
pnnixMapAggrToken = _PnnixMapAggrToken_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 6),
    _PnnixMapAggrToken_Type()
)
pnnixMapAggrToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapAggrToken.setStatus("mandatory")
_PnnixMapRemoteNodeId_Type = PnnixNodeId
_PnnixMapRemoteNodeId_Object = MibTableColumn
pnnixMapRemoteNodeId = _PnnixMapRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 7),
    _PnnixMapRemoteNodeId_Type()
)
pnnixMapRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapRemoteNodeId.setStatus("mandatory")
_PnnixMapRemotePortId_Type = PnnixPortId
_PnnixMapRemotePortId_Object = MibTableColumn
pnnixMapRemotePortId = _PnnixMapRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 8),
    _PnnixMapRemotePortId_Type()
)
pnnixMapRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapRemotePortId.setStatus("mandatory")
_PnnixMapVPCapability_Type = TruthValue
_PnnixMapVPCapability_Object = MibTableColumn
pnnixMapVPCapability = _PnnixMapVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 9),
    _PnnixMapVPCapability_Type()
)
pnnixMapVPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapVPCapability.setStatus("mandatory")
_PnnixMapPtseId_Type = Gauge32
_PnnixMapPtseId_Object = MibTableColumn
pnnixMapPtseId = _PnnixMapPtseId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 10),
    _PnnixMapPtseId_Type()
)
pnnixMapPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapPtseId.setStatus("mandatory")


class _PnnixMapMetricsTag_Type(PnnixMetricsTag):
    """Custom type pnnixMapMetricsTag based on PnnixMetricsTag"""
    subtypeSpec = PnnixMetricsTag.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnnixMapMetricsTag_Type.__name__ = "PnnixMetricsTag"
_PnnixMapMetricsTag_Object = MibTableColumn
pnnixMapMetricsTag = _PnnixMapMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 14, 1, 11),
    _PnnixMapMetricsTag_Type()
)
pnnixMapMetricsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapMetricsTag.setStatus("mandatory")
_PnnixMapNodeTable_Object = MibTable
pnnixMapNodeTable = _PnnixMapNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    pnnixMapNodeTable.setStatus("mandatory")
_PnnixMapNodeEntry_Object = MibTableRow
pnnixMapNodeEntry = _PnnixMapNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1)
)
pnnixMapNodeEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixMapNodeId"),
)
if mibBuilder.loadTexts:
    pnnixMapNodeEntry.setStatus("mandatory")
_PnnixMapNodeId_Type = PnnixNodeId
_PnnixMapNodeId_Object = MibTableColumn
pnnixMapNodeId = _PnnixMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 1),
    _PnnixMapNodeId_Type()
)
pnnixMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapNodeId.setStatus("mandatory")
_PnnixMapNodePeerGroupId_Type = PnnixPeerGroupId
_PnnixMapNodePeerGroupId_Object = MibTableColumn
pnnixMapNodePeerGroupId = _PnnixMapNodePeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 2),
    _PnnixMapNodePeerGroupId_Type()
)
pnnixMapNodePeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodePeerGroupId.setStatus("mandatory")
_PnnixMapNodeAtmAddress_Type = PnnixAtmAddr
_PnnixMapNodeAtmAddress_Object = MibTableColumn
pnnixMapNodeAtmAddress = _PnnixMapNodeAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 3),
    _PnnixMapNodeAtmAddress_Type()
)
pnnixMapNodeAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeAtmAddress.setStatus("mandatory")
_PnnixMapNodeRestrictedTransit_Type = TruthValue
_PnnixMapNodeRestrictedTransit_Object = MibTableColumn
pnnixMapNodeRestrictedTransit = _PnnixMapNodeRestrictedTransit_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 4),
    _PnnixMapNodeRestrictedTransit_Type()
)
pnnixMapNodeRestrictedTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeRestrictedTransit.setStatus("mandatory")
_PnnixMapNodeComplexRep_Type = TruthValue
_PnnixMapNodeComplexRep_Object = MibTableColumn
pnnixMapNodeComplexRep = _PnnixMapNodeComplexRep_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 5),
    _PnnixMapNodeComplexRep_Type()
)
pnnixMapNodeComplexRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeComplexRep.setStatus("mandatory")
_PnnixMapNodeRestrictedBranching_Type = TruthValue
_PnnixMapNodeRestrictedBranching_Object = MibTableColumn
pnnixMapNodeRestrictedBranching = _PnnixMapNodeRestrictedBranching_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 6),
    _PnnixMapNodeRestrictedBranching_Type()
)
pnnixMapNodeRestrictedBranching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeRestrictedBranching.setStatus("mandatory")
_PnnixMapNodeDatabaseOverload_Type = TruthValue
_PnnixMapNodeDatabaseOverload_Object = MibTableColumn
pnnixMapNodeDatabaseOverload = _PnnixMapNodeDatabaseOverload_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 7),
    _PnnixMapNodeDatabaseOverload_Type()
)
pnnixMapNodeDatabaseOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeDatabaseOverload.setStatus("mandatory")
_PnnixMapNodeIAmLeader_Type = TruthValue
_PnnixMapNodeIAmLeader_Object = MibTableColumn
pnnixMapNodeIAmLeader = _PnnixMapNodeIAmLeader_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 8),
    _PnnixMapNodeIAmLeader_Type()
)
pnnixMapNodeIAmLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeIAmLeader.setStatus("mandatory")


class _PnnixMapNodeLeadershipPriority_Type(Integer32):
    """Custom type pnnixMapNodeLeadershipPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PnnixMapNodeLeadershipPriority_Type.__name__ = "Integer32"
_PnnixMapNodeLeadershipPriority_Object = MibTableColumn
pnnixMapNodeLeadershipPriority = _PnnixMapNodeLeadershipPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 9),
    _PnnixMapNodeLeadershipPriority_Type()
)
pnnixMapNodeLeadershipPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeLeadershipPriority.setStatus("mandatory")
_PnnixMapNodePreferredPgl_Type = PnnixNodeId
_PnnixMapNodePreferredPgl_Object = MibTableColumn
pnnixMapNodePreferredPgl = _PnnixMapNodePreferredPgl_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 10),
    _PnnixMapNodePreferredPgl_Type()
)
pnnixMapNodePreferredPgl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodePreferredPgl.setStatus("mandatory")
_PnnixMapNodeParentNodeId_Type = PnnixNodeId
_PnnixMapNodeParentNodeId_Object = MibTableColumn
pnnixMapNodeParentNodeId = _PnnixMapNodeParentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 11),
    _PnnixMapNodeParentNodeId_Type()
)
pnnixMapNodeParentNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeParentNodeId.setStatus("mandatory")
_PnnixMapNodeParentAtmAddress_Type = PnnixAtmAddr
_PnnixMapNodeParentAtmAddress_Object = MibTableColumn
pnnixMapNodeParentAtmAddress = _PnnixMapNodeParentAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 12),
    _PnnixMapNodeParentAtmAddress_Type()
)
pnnixMapNodeParentAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeParentAtmAddress.setStatus("mandatory")
_PnnixMapNodeParentPeerGroupId_Type = PnnixPeerGroupId
_PnnixMapNodeParentPeerGroupId_Object = MibTableColumn
pnnixMapNodeParentPeerGroupId = _PnnixMapNodeParentPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 13),
    _PnnixMapNodeParentPeerGroupId_Type()
)
pnnixMapNodeParentPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeParentPeerGroupId.setStatus("mandatory")
_PnnixMapNodeParentPglNodeId_Type = PnnixNodeId
_PnnixMapNodeParentPglNodeId_Object = MibTableColumn
pnnixMapNodeParentPglNodeId = _PnnixMapNodeParentPglNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 15, 1, 14),
    _PnnixMapNodeParentPglNodeId_Type()
)
pnnixMapNodeParentPglNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapNodeParentPglNodeId.setStatus("mandatory")
_PnnixMapAddrTable_Object = MibTable
pnnixMapAddrTable = _PnnixMapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    pnnixMapAddrTable.setStatus("mandatory")
_PnnixMapAddrEntry_Object = MibTableRow
pnnixMapAddrEntry = _PnnixMapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1)
)
pnnixMapAddrEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixMapAddrAdvertisingNodeId"),
    (0, "XPNNI-MIB", "pnnixMapAddrAdvertisedPortId"),
    (0, "XPNNI-MIB", "pnnixMapAddrIndex"),
)
if mibBuilder.loadTexts:
    pnnixMapAddrEntry.setStatus("mandatory")
_PnnixMapAddrAdvertisingNodeId_Type = PnnixNodeId
_PnnixMapAddrAdvertisingNodeId_Object = MibTableColumn
pnnixMapAddrAdvertisingNodeId = _PnnixMapAddrAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1, 1),
    _PnnixMapAddrAdvertisingNodeId_Type()
)
pnnixMapAddrAdvertisingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapAddrAdvertisingNodeId.setStatus("mandatory")
_PnnixMapAddrAdvertisedPortId_Type = Integer32
_PnnixMapAddrAdvertisedPortId_Object = MibTableColumn
pnnixMapAddrAdvertisedPortId = _PnnixMapAddrAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1, 2),
    _PnnixMapAddrAdvertisedPortId_Type()
)
pnnixMapAddrAdvertisedPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapAddrAdvertisedPortId.setStatus("mandatory")


class _PnnixMapAddrIndex_Type(Integer32):
    """Custom type pnnixMapAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnnixMapAddrIndex_Type.__name__ = "Integer32"
_PnnixMapAddrIndex_Object = MibTableColumn
pnnixMapAddrIndex = _PnnixMapAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1, 3),
    _PnnixMapAddrIndex_Type()
)
pnnixMapAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapAddrIndex.setStatus("mandatory")
_PnnixMapAddrAddress_Type = AtmAddrPrefix
_PnnixMapAddrAddress_Object = MibTableColumn
pnnixMapAddrAddress = _PnnixMapAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1, 4),
    _PnnixMapAddrAddress_Type()
)
pnnixMapAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapAddrAddress.setStatus("mandatory")
_PnnixMapAddrPrefixLength_Type = PnnixPrefixLength
_PnnixMapAddrPrefixLength_Object = MibTableColumn
pnnixMapAddrPrefixLength = _PnnixMapAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 16, 1, 5),
    _PnnixMapAddrPrefixLength_Type()
)
pnnixMapAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapAddrPrefixLength.setStatus("mandatory")
_PnnixMapTnsTable_Object = MibTable
pnnixMapTnsTable = _PnnixMapTnsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    pnnixMapTnsTable.setStatus("mandatory")
_PnnixMapTnsEntry_Object = MibTableRow
pnnixMapTnsEntry = _PnnixMapTnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1)
)
pnnixMapTnsEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixMapTnsAdvertisingNodeId"),
    (0, "XPNNI-MIB", "pnnixMapTnsAdvertisedPortId"),
    (0, "XPNNI-MIB", "pnnixMapTnsType"),
    (0, "XPNNI-MIB", "pnnixMapTnsPlan"),
    (0, "XPNNI-MIB", "pnnixMapTnsId"),
)
if mibBuilder.loadTexts:
    pnnixMapTnsEntry.setStatus("mandatory")
_PnnixMapTnsAdvertisingNodeId_Type = Integer32
_PnnixMapTnsAdvertisingNodeId_Object = MibTableColumn
pnnixMapTnsAdvertisingNodeId = _PnnixMapTnsAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1, 1),
    _PnnixMapTnsAdvertisingNodeId_Type()
)
pnnixMapTnsAdvertisingNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapTnsAdvertisingNodeId.setStatus("mandatory")
_PnnixMapTnsAdvertisedPortId_Type = Integer32
_PnnixMapTnsAdvertisedPortId_Object = MibTableColumn
pnnixMapTnsAdvertisedPortId = _PnnixMapTnsAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1, 2),
    _PnnixMapTnsAdvertisedPortId_Type()
)
pnnixMapTnsAdvertisedPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapTnsAdvertisedPortId.setStatus("mandatory")
_PnnixMapTnsType_Type = TnsType
_PnnixMapTnsType_Object = MibTableColumn
pnnixMapTnsType = _PnnixMapTnsType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1, 3),
    _PnnixMapTnsType_Type()
)
pnnixMapTnsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapTnsType.setStatus("mandatory")
_PnnixMapTnsPlan_Type = TnsPlan
_PnnixMapTnsPlan_Object = MibTableColumn
pnnixMapTnsPlan = _PnnixMapTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1, 4),
    _PnnixMapTnsPlan_Type()
)
pnnixMapTnsPlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMapTnsPlan.setStatus("mandatory")
_PnnixMapTnsId_Type = DisplayString
_PnnixMapTnsId_Object = MibTableColumn
pnnixMapTnsId = _PnnixMapTnsId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 17, 1, 5),
    _PnnixMapTnsId_Type()
)
pnnixMapTnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixMapTnsId.setStatus("mandatory")
_PnnixMetricsTable_Object = MibTable
pnnixMetricsTable = _PnnixMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    pnnixMetricsTable.setStatus("mandatory")
_PnnixMetricsEntry_Object = MibTableRow
pnnixMetricsEntry = _PnnixMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1)
)
pnnixMetricsEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixMetricsTag"),
    (0, "XPNNI-MIB", "pnnixMetricsDirection"),
    (0, "XPNNI-MIB", "pnnixMetricsIndex"),
)
if mibBuilder.loadTexts:
    pnnixMetricsEntry.setStatus("mandatory")


class _PnnixMetricsTag_Type(PnnixMetricsTag):
    """Custom type pnnixMetricsTag based on PnnixMetricsTag"""
    subtypeSpec = PnnixMetricsTag.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnnixMetricsTag_Type.__name__ = "PnnixMetricsTag"
_PnnixMetricsTag_Object = MibTableColumn
pnnixMetricsTag = _PnnixMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 1),
    _PnnixMetricsTag_Type()
)
pnnixMetricsTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMetricsTag.setStatus("mandatory")


class _PnnixMetricsDirection_Type(Integer32):
    """Custom type pnnixMetricsDirection based on Integer32"""
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


_PnnixMetricsDirection_Type.__name__ = "Integer32"
_PnnixMetricsDirection_Object = MibTableColumn
pnnixMetricsDirection = _PnnixMetricsDirection_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 2),
    _PnnixMetricsDirection_Type()
)
pnnixMetricsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMetricsDirection.setStatus("mandatory")


class _PnnixMetricsIndex_Type(Integer32):
    """Custom type pnnixMetricsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnnixMetricsIndex_Type.__name__ = "Integer32"
_PnnixMetricsIndex_Object = MibTableColumn
pnnixMetricsIndex = _PnnixMetricsIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 3),
    _PnnixMetricsIndex_Type()
)
pnnixMetricsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixMetricsIndex.setStatus("mandatory")


class _PnnixMetricsClasses_Type(Integer32):
    """Custom type pnnixMetricsClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PnnixMetricsClasses_Type.__name__ = "Integer32"
_PnnixMetricsClasses_Object = MibTableColumn
pnnixMetricsClasses = _PnnixMetricsClasses_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 4),
    _PnnixMetricsClasses_Type()
)
pnnixMetricsClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetricsClasses.setStatus("mandatory")
_PnnixMetricsGcacClp_Type = ClpType
_PnnixMetricsGcacClp_Object = MibTableColumn
pnnixMetricsGcacClp = _PnnixMetricsGcacClp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 5),
    _PnnixMetricsGcacClp_Type()
)
pnnixMetricsGcacClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetricsGcacClp.setStatus("mandatory")
_PnnixMetricsAdminWeight_Type = Gauge32
_PnnixMetricsAdminWeight_Object = MibTableColumn
pnnixMetricsAdminWeight = _PnnixMetricsAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 6),
    _PnnixMetricsAdminWeight_Type()
)
pnnixMetricsAdminWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetricsAdminWeight.setStatus("mandatory")
_PnnixMetrics1_Type = Gauge32
_PnnixMetrics1_Object = MibTableColumn
pnnixMetrics1 = _PnnixMetrics1_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 7),
    _PnnixMetrics1_Type()
)
pnnixMetrics1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics1.setStatus("mandatory")
_PnnixMetrics2_Type = Gauge32
_PnnixMetrics2_Object = MibTableColumn
pnnixMetrics2 = _PnnixMetrics2_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 8),
    _PnnixMetrics2_Type()
)
pnnixMetrics2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics2.setStatus("mandatory")
_PnnixMetrics3_Type = Gauge32
_PnnixMetrics3_Object = MibTableColumn
pnnixMetrics3 = _PnnixMetrics3_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 9),
    _PnnixMetrics3_Type()
)
pnnixMetrics3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics3.setStatus("mandatory")
_PnnixMetrics4_Type = Gauge32
_PnnixMetrics4_Object = MibTableColumn
pnnixMetrics4 = _PnnixMetrics4_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 10),
    _PnnixMetrics4_Type()
)
pnnixMetrics4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics4.setStatus("mandatory")
_PnnixMetrics5_Type = Gauge32
_PnnixMetrics5_Object = MibTableColumn
pnnixMetrics5 = _PnnixMetrics5_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 11),
    _PnnixMetrics5_Type()
)
pnnixMetrics5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics5.setStatus("mandatory")
_PnnixMetrics6_Type = Gauge32
_PnnixMetrics6_Object = MibTableColumn
pnnixMetrics6 = _PnnixMetrics6_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 12),
    _PnnixMetrics6_Type()
)
pnnixMetrics6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics6.setStatus("mandatory")
_PnnixMetrics7_Type = Gauge32
_PnnixMetrics7_Object = MibTableColumn
pnnixMetrics7 = _PnnixMetrics7_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 13),
    _PnnixMetrics7_Type()
)
pnnixMetrics7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics7.setStatus("mandatory")
_PnnixMetrics8_Type = Gauge32
_PnnixMetrics8_Object = MibTableColumn
pnnixMetrics8 = _PnnixMetrics8_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 14),
    _PnnixMetrics8_Type()
)
pnnixMetrics8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetrics8.setStatus("mandatory")


class _PnnixMetricsRowStatus_Type(Integer32):
    """Custom type pnnixMetricsRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixMetricsRowStatus_Type.__name__ = "Integer32"
_PnnixMetricsRowStatus_Object = MibTableColumn
pnnixMetricsRowStatus = _PnnixMetricsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 18, 1, 15),
    _PnnixMetricsRowStatus_Type()
)
pnnixMetricsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixMetricsRowStatus.setStatus("mandatory")
_PnnixRoutingGroup_ObjectIdentity = ObjectIdentity
pnnixRoutingGroup = _PnnixRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19)
)
_PnnixRouteBaseGroup_ObjectIdentity = ObjectIdentity
pnnixRouteBaseGroup = _PnnixRouteBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 1)
)
_PnnixRouteNodeNumber_Type = Gauge32
_PnnixRouteNodeNumber_Object = MibScalar
pnnixRouteNodeNumber = _PnnixRouteNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 1, 1),
    _PnnixRouteNodeNumber_Type()
)
pnnixRouteNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteNodeNumber.setStatus("mandatory")
_PnnixRouteAddrNumber_Type = Gauge32
_PnnixRouteAddrNumber_Object = MibScalar
pnnixRouteAddrNumber = _PnnixRouteAddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 1, 2),
    _PnnixRouteAddrNumber_Type()
)
pnnixRouteAddrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteAddrNumber.setStatus("mandatory")
_PnnixRouteNodeTable_Object = MibTable
pnnixRouteNodeTable = _PnnixRouteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    pnnixRouteNodeTable.setStatus("mandatory")
_PnnixRouteNodeEntry_Object = MibTableRow
pnnixRouteNodeEntry = _PnnixRouteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1)
)
pnnixRouteNodeEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixRouteNodeClass"),
    (0, "XPNNI-MIB", "pnnixRouteNodeDestNodeId"),
    (0, "XPNNI-MIB", "pnnixRouteNodeDTL"),
)
if mibBuilder.loadTexts:
    pnnixRouteNodeEntry.setStatus("mandatory")
_PnnixRouteNodeClass_Type = ServiceCategory
_PnnixRouteNodeClass_Object = MibTableColumn
pnnixRouteNodeClass = _PnnixRouteNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 1),
    _PnnixRouteNodeClass_Type()
)
pnnixRouteNodeClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteNodeClass.setStatus("mandatory")
_PnnixRouteNodeDestNodeId_Type = PnnixNodeId
_PnnixRouteNodeDestNodeId_Object = MibTableColumn
pnnixRouteNodeDestNodeId = _PnnixRouteNodeDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 2),
    _PnnixRouteNodeDestNodeId_Type()
)
pnnixRouteNodeDestNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteNodeDestNodeId.setStatus("mandatory")


class _PnnixRouteNodeDTL_Type(Integer32):
    """Custom type pnnixRouteNodeDTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PnnixRouteNodeDTL_Type.__name__ = "Integer32"
_PnnixRouteNodeDTL_Object = MibTableColumn
pnnixRouteNodeDTL = _PnnixRouteNodeDTL_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 3),
    _PnnixRouteNodeDTL_Type()
)
pnnixRouteNodeDTL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteNodeDTL.setStatus("mandatory")
_PnnixRouteNodeDestPortId_Type = PnnixPortId
_PnnixRouteNodeDestPortId_Object = MibTableColumn
pnnixRouteNodeDestPortId = _PnnixRouteNodeDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 4),
    _PnnixRouteNodeDestPortId_Type()
)
pnnixRouteNodeDestPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeDestPortId.setStatus("mandatory")


class _PnnixRouteNodeProto_Type(Integer32):
    """Custom type pnnixRouteNodeProto based on Integer32"""
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


_PnnixRouteNodeProto_Type.__name__ = "Integer32"
_PnnixRouteNodeProto_Object = MibTableColumn
pnnixRouteNodeProto = _PnnixRouteNodeProto_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 5),
    _PnnixRouteNodeProto_Type()
)
pnnixRouteNodeProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteNodeProto.setStatus("mandatory")
_PnnixRouteNodeTimeStamp_Type = DisplayString
_PnnixRouteNodeTimeStamp_Object = MibTableColumn
pnnixRouteNodeTimeStamp = _PnnixRouteNodeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 6),
    _PnnixRouteNodeTimeStamp_Type()
)
pnnixRouteNodeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteNodeTimeStamp.setStatus("mandatory")
_PnnixRouteNodeInfo_Type = ObjectIdentifier
_PnnixRouteNodeInfo_Object = MibTableColumn
pnnixRouteNodeInfo = _PnnixRouteNodeInfo_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 7),
    _PnnixRouteNodeInfo_Type()
)
pnnixRouteNodeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeInfo.setStatus("mandatory")
_PnnixRouteNodeGcacClp_Type = ClpType
_PnnixRouteNodeGcacClp_Object = MibTableColumn
pnnixRouteNodeGcacClp = _PnnixRouteNodeGcacClp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 8),
    _PnnixRouteNodeGcacClp_Type()
)
pnnixRouteNodeGcacClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeGcacClp.setStatus("mandatory")
_PnnixRouteNodeFwdMetricAW_Type = Gauge32
_PnnixRouteNodeFwdMetricAW_Object = MibTableColumn
pnnixRouteNodeFwdMetricAW = _PnnixRouteNodeFwdMetricAW_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 9),
    _PnnixRouteNodeFwdMetricAW_Type()
)
pnnixRouteNodeFwdMetricAW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetricAW.setStatus("mandatory")
_PnnixRouteNodeFwdMetric1_Type = Gauge32
_PnnixRouteNodeFwdMetric1_Object = MibTableColumn
pnnixRouteNodeFwdMetric1 = _PnnixRouteNodeFwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 10),
    _PnnixRouteNodeFwdMetric1_Type()
)
pnnixRouteNodeFwdMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric1.setStatus("mandatory")
_PnnixRouteNodeFwdMetric2_Type = Gauge32
_PnnixRouteNodeFwdMetric2_Object = MibTableColumn
pnnixRouteNodeFwdMetric2 = _PnnixRouteNodeFwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 11),
    _PnnixRouteNodeFwdMetric2_Type()
)
pnnixRouteNodeFwdMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric2.setStatus("mandatory")
_PnnixRouteNodeFwdMetric3_Type = Gauge32
_PnnixRouteNodeFwdMetric3_Object = MibTableColumn
pnnixRouteNodeFwdMetric3 = _PnnixRouteNodeFwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 12),
    _PnnixRouteNodeFwdMetric3_Type()
)
pnnixRouteNodeFwdMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric3.setStatus("mandatory")
_PnnixRouteNodeFwdMetric4_Type = Gauge32
_PnnixRouteNodeFwdMetric4_Object = MibTableColumn
pnnixRouteNodeFwdMetric4 = _PnnixRouteNodeFwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 13),
    _PnnixRouteNodeFwdMetric4_Type()
)
pnnixRouteNodeFwdMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric4.setStatus("mandatory")
_PnnixRouteNodeFwdMetric5_Type = Gauge32
_PnnixRouteNodeFwdMetric5_Object = MibTableColumn
pnnixRouteNodeFwdMetric5 = _PnnixRouteNodeFwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 14),
    _PnnixRouteNodeFwdMetric5_Type()
)
pnnixRouteNodeFwdMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric5.setStatus("mandatory")
_PnnixRouteNodeFwdMetric6_Type = Gauge32
_PnnixRouteNodeFwdMetric6_Object = MibTableColumn
pnnixRouteNodeFwdMetric6 = _PnnixRouteNodeFwdMetric6_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 15),
    _PnnixRouteNodeFwdMetric6_Type()
)
pnnixRouteNodeFwdMetric6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric6.setStatus("mandatory")
_PnnixRouteNodeFwdMetric7_Type = Gauge32
_PnnixRouteNodeFwdMetric7_Object = MibTableColumn
pnnixRouteNodeFwdMetric7 = _PnnixRouteNodeFwdMetric7_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 16),
    _PnnixRouteNodeFwdMetric7_Type()
)
pnnixRouteNodeFwdMetric7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric7.setStatus("mandatory")
_PnnixRouteNodeFwdMetric8_Type = Gauge32
_PnnixRouteNodeFwdMetric8_Object = MibTableColumn
pnnixRouteNodeFwdMetric8 = _PnnixRouteNodeFwdMetric8_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 17),
    _PnnixRouteNodeFwdMetric8_Type()
)
pnnixRouteNodeFwdMetric8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeFwdMetric8.setStatus("mandatory")
_PnnixRouteNodeBwdMetricAW_Type = Gauge32
_PnnixRouteNodeBwdMetricAW_Object = MibTableColumn
pnnixRouteNodeBwdMetricAW = _PnnixRouteNodeBwdMetricAW_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 18),
    _PnnixRouteNodeBwdMetricAW_Type()
)
pnnixRouteNodeBwdMetricAW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetricAW.setStatus("mandatory")
_PnnixRouteNodeBwdMetric1_Type = Gauge32
_PnnixRouteNodeBwdMetric1_Object = MibTableColumn
pnnixRouteNodeBwdMetric1 = _PnnixRouteNodeBwdMetric1_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 19),
    _PnnixRouteNodeBwdMetric1_Type()
)
pnnixRouteNodeBwdMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric1.setStatus("mandatory")
_PnnixRouteNodeBwdMetric2_Type = Gauge32
_PnnixRouteNodeBwdMetric2_Object = MibTableColumn
pnnixRouteNodeBwdMetric2 = _PnnixRouteNodeBwdMetric2_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 20),
    _PnnixRouteNodeBwdMetric2_Type()
)
pnnixRouteNodeBwdMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric2.setStatus("mandatory")
_PnnixRouteNodeBwdMetric3_Type = Gauge32
_PnnixRouteNodeBwdMetric3_Object = MibTableColumn
pnnixRouteNodeBwdMetric3 = _PnnixRouteNodeBwdMetric3_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 21),
    _PnnixRouteNodeBwdMetric3_Type()
)
pnnixRouteNodeBwdMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric3.setStatus("mandatory")
_PnnixRouteNodeBwdMetric4_Type = Gauge32
_PnnixRouteNodeBwdMetric4_Object = MibTableColumn
pnnixRouteNodeBwdMetric4 = _PnnixRouteNodeBwdMetric4_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 22),
    _PnnixRouteNodeBwdMetric4_Type()
)
pnnixRouteNodeBwdMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric4.setStatus("mandatory")
_PnnixRouteNodeBwdMetric5_Type = Gauge32
_PnnixRouteNodeBwdMetric5_Object = MibTableColumn
pnnixRouteNodeBwdMetric5 = _PnnixRouteNodeBwdMetric5_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 23),
    _PnnixRouteNodeBwdMetric5_Type()
)
pnnixRouteNodeBwdMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric5.setStatus("mandatory")
_PnnixRouteNodeBwdMetric6_Type = Gauge32
_PnnixRouteNodeBwdMetric6_Object = MibTableColumn
pnnixRouteNodeBwdMetric6 = _PnnixRouteNodeBwdMetric6_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 24),
    _PnnixRouteNodeBwdMetric6_Type()
)
pnnixRouteNodeBwdMetric6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric6.setStatus("mandatory")
_PnnixRouteNodeBwdMetric7_Type = Gauge32
_PnnixRouteNodeBwdMetric7_Object = MibTableColumn
pnnixRouteNodeBwdMetric7 = _PnnixRouteNodeBwdMetric7_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 25),
    _PnnixRouteNodeBwdMetric7_Type()
)
pnnixRouteNodeBwdMetric7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric7.setStatus("mandatory")
_PnnixRouteNodeBwdMetric8_Type = Gauge32
_PnnixRouteNodeBwdMetric8_Object = MibTableColumn
pnnixRouteNodeBwdMetric8 = _PnnixRouteNodeBwdMetric8_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 26),
    _PnnixRouteNodeBwdMetric8_Type()
)
pnnixRouteNodeBwdMetric8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeBwdMetric8.setStatus("mandatory")
_PnnixRouteNodeVPCapability_Type = TruthValue
_PnnixRouteNodeVPCapability_Object = MibTableColumn
pnnixRouteNodeVPCapability = _PnnixRouteNodeVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 27),
    _PnnixRouteNodeVPCapability_Type()
)
pnnixRouteNodeVPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeVPCapability.setStatus("mandatory")


class _PnnixRouteNodeStatus_Type(Integer32):
    """Custom type pnnixRouteNodeStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixRouteNodeStatus_Type.__name__ = "Integer32"
_PnnixRouteNodeStatus_Object = MibTableColumn
pnnixRouteNodeStatus = _PnnixRouteNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 2, 1, 28),
    _PnnixRouteNodeStatus_Type()
)
pnnixRouteNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteNodeStatus.setStatus("mandatory")
_PnnixDTLTable_Object = MibTable
pnnixDTLTable = _PnnixDTLTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    pnnixDTLTable.setStatus("mandatory")
_PnnixDTLEntry_Object = MibTableRow
pnnixDTLEntry = _PnnixDTLEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1)
)
pnnixDTLEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixDTLIndex"),
    (0, "XPNNI-MIB", "pnnixDTLEntryIndex"),
)
if mibBuilder.loadTexts:
    pnnixDTLEntry.setStatus("mandatory")


class _PnnixDTLIndex_Type(Integer32):
    """Custom type pnnixDTLIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnnixDTLIndex_Type.__name__ = "Integer32"
_PnnixDTLIndex_Object = MibTableColumn
pnnixDTLIndex = _PnnixDTLIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 1),
    _PnnixDTLIndex_Type()
)
pnnixDTLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixDTLIndex.setStatus("mandatory")


class _PnnixDTLEntryIndex_Type(Integer32):
    """Custom type pnnixDTLEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PnnixDTLEntryIndex_Type.__name__ = "Integer32"
_PnnixDTLEntryIndex_Object = MibTableColumn
pnnixDTLEntryIndex = _PnnixDTLEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 2),
    _PnnixDTLEntryIndex_Type()
)
pnnixDTLEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixDTLEntryIndex.setStatus("mandatory")
_PnnixDTLNodeId_Type = PnnixNodeId
_PnnixDTLNodeId_Object = MibTableColumn
pnnixDTLNodeId = _PnnixDTLNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 3),
    _PnnixDTLNodeId_Type()
)
pnnixDTLNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixDTLNodeId.setStatus("mandatory")
_PnnixDTLPortId_Type = PnnixPortId
_PnnixDTLPortId_Object = MibTableColumn
pnnixDTLPortId = _PnnixDTLPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 4),
    _PnnixDTLPortId_Type()
)
pnnixDTLPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixDTLPortId.setStatus("mandatory")


class _PnnixDTLLinkType_Type(Integer32):
    """Custom type pnnixDTLLinkType based on Integer32"""
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


_PnnixDTLLinkType_Type.__name__ = "Integer32"
_PnnixDTLLinkType_Object = MibTableColumn
pnnixDTLLinkType = _PnnixDTLLinkType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 5),
    _PnnixDTLLinkType_Type()
)
pnnixDTLLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixDTLLinkType.setStatus("mandatory")


class _PnnixDTLStatus_Type(Integer32):
    """Custom type pnnixDTLStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixDTLStatus_Type.__name__ = "Integer32"
_PnnixDTLStatus_Object = MibTableColumn
pnnixDTLStatus = _PnnixDTLStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 3, 1, 6),
    _PnnixDTLStatus_Type()
)
pnnixDTLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixDTLStatus.setStatus("mandatory")
_PnnixRouteAddrTable_Object = MibTable
pnnixRouteAddrTable = _PnnixRouteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    pnnixRouteAddrTable.setStatus("mandatory")
_PnnixRouteAddrEntry_Object = MibTableRow
pnnixRouteAddrEntry = _PnnixRouteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1)
)
pnnixRouteAddrEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixRouteAddrAddress"),
    (0, "XPNNI-MIB", "pnnixRouteAddrPrefixLength"),
    (0, "XPNNI-MIB", "pnnixRouteAddrIndex"),
)
if mibBuilder.loadTexts:
    pnnixRouteAddrEntry.setStatus("mandatory")
_PnnixRouteAddrAddress_Type = AtmAddrPrefix
_PnnixRouteAddrAddress_Object = MibTableColumn
pnnixRouteAddrAddress = _PnnixRouteAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 1),
    _PnnixRouteAddrAddress_Type()
)
pnnixRouteAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteAddrAddress.setStatus("mandatory")
_PnnixRouteAddrPrefixLength_Type = PnnixPrefixLength
_PnnixRouteAddrPrefixLength_Object = MibTableColumn
pnnixRouteAddrPrefixLength = _PnnixRouteAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 2),
    _PnnixRouteAddrPrefixLength_Type()
)
pnnixRouteAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteAddrPrefixLength.setStatus("mandatory")


class _PnnixRouteAddrIndex_Type(Integer32):
    """Custom type pnnixRouteAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnnixRouteAddrIndex_Type.__name__ = "Integer32"
_PnnixRouteAddrIndex_Object = MibTableColumn
pnnixRouteAddrIndex = _PnnixRouteAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 3),
    _PnnixRouteAddrIndex_Type()
)
pnnixRouteAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteAddrIndex.setStatus("mandatory")
_PnnixRouteAddrIfIndex_Type = InterfaceIndex
_PnnixRouteAddrIfIndex_Object = MibTableColumn
pnnixRouteAddrIfIndex = _PnnixRouteAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 4),
    _PnnixRouteAddrIfIndex_Type()
)
pnnixRouteAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrIfIndex.setStatus("mandatory")
_PnnixRouteAddrAdvertisingNodeId_Type = PnnixNodeId
_PnnixRouteAddrAdvertisingNodeId_Object = MibTableColumn
pnnixRouteAddrAdvertisingNodeId = _PnnixRouteAddrAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 5),
    _PnnixRouteAddrAdvertisingNodeId_Type()
)
pnnixRouteAddrAdvertisingNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrAdvertisingNodeId.setStatus("mandatory")
_PnnixRouteAddrAdvertisedPortId_Type = PnnixPortId
_PnnixRouteAddrAdvertisedPortId_Object = MibTableColumn
pnnixRouteAddrAdvertisedPortId = _PnnixRouteAddrAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 6),
    _PnnixRouteAddrAdvertisedPortId_Type()
)
pnnixRouteAddrAdvertisedPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrAdvertisedPortId.setStatus("mandatory")


class _PnnixRouteAddrType_Type(Integer32):
    """Custom type pnnixRouteAddrType based on Integer32"""
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


_PnnixRouteAddrType_Type.__name__ = "Integer32"
_PnnixRouteAddrType_Object = MibTableColumn
pnnixRouteAddrType = _PnnixRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 7),
    _PnnixRouteAddrType_Type()
)
pnnixRouteAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrType.setStatus("mandatory")


class _PnnixRouteAddrProto_Type(Integer32):
    """Custom type pnnixRouteAddrProto based on Integer32"""
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


_PnnixRouteAddrProto_Type.__name__ = "Integer32"
_PnnixRouteAddrProto_Object = MibTableColumn
pnnixRouteAddrProto = _PnnixRouteAddrProto_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 8),
    _PnnixRouteAddrProto_Type()
)
pnnixRouteAddrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteAddrProto.setStatus("mandatory")
_PnnixRouteAddrPnniScope_Type = PnnixLevel
_PnnixRouteAddrPnniScope_Object = MibTableColumn
pnnixRouteAddrPnniScope = _PnnixRouteAddrPnniScope_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 9),
    _PnnixRouteAddrPnniScope_Type()
)
pnnixRouteAddrPnniScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrPnniScope.setStatus("mandatory")
_PnnixRouteAddrVPCapability_Type = TruthValue
_PnnixRouteAddrVPCapability_Object = MibTableColumn
pnnixRouteAddrVPCapability = _PnnixRouteAddrVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 10),
    _PnnixRouteAddrVPCapability_Type()
)
pnnixRouteAddrVPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrVPCapability.setStatus("mandatory")
_PnnixRouteAddrMetricsTag_Type = PnnixMetricsTag
_PnnixRouteAddrMetricsTag_Object = MibTableColumn
pnnixRouteAddrMetricsTag = _PnnixRouteAddrMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 11),
    _PnnixRouteAddrMetricsTag_Type()
)
pnnixRouteAddrMetricsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrMetricsTag.setStatus("mandatory")
_PnnixRouteAddrPtseId_Type = Gauge32
_PnnixRouteAddrPtseId_Object = MibTableColumn
pnnixRouteAddrPtseId = _PnnixRouteAddrPtseId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 12),
    _PnnixRouteAddrPtseId_Type()
)
pnnixRouteAddrPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteAddrPtseId.setStatus("mandatory")
_PnnixRouteAddrOriginateAdvertisement_Type = TruthValue
_PnnixRouteAddrOriginateAdvertisement_Object = MibTableColumn
pnnixRouteAddrOriginateAdvertisement = _PnnixRouteAddrOriginateAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 13),
    _PnnixRouteAddrOriginateAdvertisement_Type()
)
pnnixRouteAddrOriginateAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrOriginateAdvertisement.setStatus("mandatory")
_PnnixRouteAddrInfo_Type = ObjectIdentifier
_PnnixRouteAddrInfo_Object = MibTableColumn
pnnixRouteAddrInfo = _PnnixRouteAddrInfo_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 14),
    _PnnixRouteAddrInfo_Type()
)
pnnixRouteAddrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrInfo.setStatus("mandatory")


class _PnnixRouteAddrOperStatus_Type(Integer32):
    """Custom type pnnixRouteAddrOperStatus based on Integer32"""
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


_PnnixRouteAddrOperStatus_Type.__name__ = "Integer32"
_PnnixRouteAddrOperStatus_Object = MibTableColumn
pnnixRouteAddrOperStatus = _PnnixRouteAddrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 15),
    _PnnixRouteAddrOperStatus_Type()
)
pnnixRouteAddrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteAddrOperStatus.setStatus("mandatory")
_PnnixRouteAddrTimeStamp_Type = DisplayString
_PnnixRouteAddrTimeStamp_Object = MibTableColumn
pnnixRouteAddrTimeStamp = _PnnixRouteAddrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 16),
    _PnnixRouteAddrTimeStamp_Type()
)
pnnixRouteAddrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteAddrTimeStamp.setStatus("mandatory")


class _PnnixRouteAddrRowStatus_Type(Integer32):
    """Custom type pnnixRouteAddrRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixRouteAddrRowStatus_Type.__name__ = "Integer32"
_PnnixRouteAddrRowStatus_Object = MibTableColumn
pnnixRouteAddrRowStatus = _PnnixRouteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 4, 1, 17),
    _PnnixRouteAddrRowStatus_Type()
)
pnnixRouteAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteAddrRowStatus.setStatus("mandatory")
_PnnixRouteTnsTable_Object = MibTable
pnnixRouteTnsTable = _PnnixRouteTnsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5)
)
if mibBuilder.loadTexts:
    pnnixRouteTnsTable.setStatus("mandatory")
_PnnixRouteTnsEntry_Object = MibTableRow
pnnixRouteTnsEntry = _PnnixRouteTnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1)
)
pnnixRouteTnsEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixRouteTnsType"),
    (0, "XPNNI-MIB", "pnnixRouteTnsPlan"),
    (0, "XPNNI-MIB", "pnnixRouteTnsId"),
    (0, "XPNNI-MIB", "pnnixRouteTnsIndex"),
)
if mibBuilder.loadTexts:
    pnnixRouteTnsEntry.setStatus("mandatory")
_PnnixRouteTnsType_Type = TnsType
_PnnixRouteTnsType_Object = MibTableColumn
pnnixRouteTnsType = _PnnixRouteTnsType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 1),
    _PnnixRouteTnsType_Type()
)
pnnixRouteTnsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteTnsType.setStatus("mandatory")
_PnnixRouteTnsPlan_Type = TnsPlan
_PnnixRouteTnsPlan_Object = MibTableColumn
pnnixRouteTnsPlan = _PnnixRouteTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 2),
    _PnnixRouteTnsPlan_Type()
)
pnnixRouteTnsPlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteTnsPlan.setStatus("mandatory")
_PnnixRouteTnsId_Type = DisplayString
_PnnixRouteTnsId_Object = MibTableColumn
pnnixRouteTnsId = _PnnixRouteTnsId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 3),
    _PnnixRouteTnsId_Type()
)
pnnixRouteTnsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteTnsId.setStatus("mandatory")


class _PnnixRouteTnsIndex_Type(Integer32):
    """Custom type pnnixRouteTnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PnnixRouteTnsIndex_Type.__name__ = "Integer32"
_PnnixRouteTnsIndex_Object = MibTableColumn
pnnixRouteTnsIndex = _PnnixRouteTnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 4),
    _PnnixRouteTnsIndex_Type()
)
pnnixRouteTnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRouteTnsIndex.setStatus("mandatory")
_PnnixRouteTnsIfIndex_Type = InterfaceIndex
_PnnixRouteTnsIfIndex_Object = MibTableColumn
pnnixRouteTnsIfIndex = _PnnixRouteTnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 5),
    _PnnixRouteTnsIfIndex_Type()
)
pnnixRouteTnsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsIfIndex.setStatus("mandatory")
_PnnixRouteTnsAdvertisingNodeId_Type = PnnixNodeId
_PnnixRouteTnsAdvertisingNodeId_Object = MibTableColumn
pnnixRouteTnsAdvertisingNodeId = _PnnixRouteTnsAdvertisingNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 6),
    _PnnixRouteTnsAdvertisingNodeId_Type()
)
pnnixRouteTnsAdvertisingNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsAdvertisingNodeId.setStatus("mandatory")
_PnnixRouteTnsAdvertisedPortId_Type = PnnixPortId
_PnnixRouteTnsAdvertisedPortId_Object = MibTableColumn
pnnixRouteTnsAdvertisedPortId = _PnnixRouteTnsAdvertisedPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 7),
    _PnnixRouteTnsAdvertisedPortId_Type()
)
pnnixRouteTnsAdvertisedPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsAdvertisedPortId.setStatus("mandatory")


class _PnnixRouteTnsRouteType_Type(Integer32):
    """Custom type pnnixRouteTnsRouteType based on Integer32"""
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


_PnnixRouteTnsRouteType_Type.__name__ = "Integer32"
_PnnixRouteTnsRouteType_Object = MibTableColumn
pnnixRouteTnsRouteType = _PnnixRouteTnsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 8),
    _PnnixRouteTnsRouteType_Type()
)
pnnixRouteTnsRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsRouteType.setStatus("mandatory")


class _PnnixRouteTnsProto_Type(Integer32):
    """Custom type pnnixRouteTnsProto based on Integer32"""
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


_PnnixRouteTnsProto_Type.__name__ = "Integer32"
_PnnixRouteTnsProto_Object = MibTableColumn
pnnixRouteTnsProto = _PnnixRouteTnsProto_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 9),
    _PnnixRouteTnsProto_Type()
)
pnnixRouteTnsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteTnsProto.setStatus("mandatory")
_PnnixRouteTnsPnniScope_Type = PnnixLevel
_PnnixRouteTnsPnniScope_Object = MibTableColumn
pnnixRouteTnsPnniScope = _PnnixRouteTnsPnniScope_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 10),
    _PnnixRouteTnsPnniScope_Type()
)
pnnixRouteTnsPnniScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsPnniScope.setStatus("mandatory")
_PnnixRouteTnsVPCapability_Type = TruthValue
_PnnixRouteTnsVPCapability_Object = MibTableColumn
pnnixRouteTnsVPCapability = _PnnixRouteTnsVPCapability_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 11),
    _PnnixRouteTnsVPCapability_Type()
)
pnnixRouteTnsVPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsVPCapability.setStatus("mandatory")
_PnnixRouteTnsMetricsTag_Type = PnnixMetricsTag
_PnnixRouteTnsMetricsTag_Object = MibTableColumn
pnnixRouteTnsMetricsTag = _PnnixRouteTnsMetricsTag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 12),
    _PnnixRouteTnsMetricsTag_Type()
)
pnnixRouteTnsMetricsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsMetricsTag.setStatus("mandatory")
_PnnixRouteTnsPtseId_Type = Gauge32
_PnnixRouteTnsPtseId_Object = MibTableColumn
pnnixRouteTnsPtseId = _PnnixRouteTnsPtseId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 13),
    _PnnixRouteTnsPtseId_Type()
)
pnnixRouteTnsPtseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteTnsPtseId.setStatus("mandatory")
_PnnixRouteTnsOriginateAdvertisement_Type = TruthValue
_PnnixRouteTnsOriginateAdvertisement_Object = MibTableColumn
pnnixRouteTnsOriginateAdvertisement = _PnnixRouteTnsOriginateAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 14),
    _PnnixRouteTnsOriginateAdvertisement_Type()
)
pnnixRouteTnsOriginateAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsOriginateAdvertisement.setStatus("mandatory")
_PnnixRouteTnsInfo_Type = ObjectIdentifier
_PnnixRouteTnsInfo_Object = MibTableColumn
pnnixRouteTnsInfo = _PnnixRouteTnsInfo_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 15),
    _PnnixRouteTnsInfo_Type()
)
pnnixRouteTnsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsInfo.setStatus("mandatory")


class _PnnixRouteTnsOperStatus_Type(Integer32):
    """Custom type pnnixRouteTnsOperStatus based on Integer32"""
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


_PnnixRouteTnsOperStatus_Type.__name__ = "Integer32"
_PnnixRouteTnsOperStatus_Object = MibTableColumn
pnnixRouteTnsOperStatus = _PnnixRouteTnsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 16),
    _PnnixRouteTnsOperStatus_Type()
)
pnnixRouteTnsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteTnsOperStatus.setStatus("mandatory")
_PnnixRouteTnsTimeStamp_Type = DisplayString
_PnnixRouteTnsTimeStamp_Object = MibTableColumn
pnnixRouteTnsTimeStamp = _PnnixRouteTnsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 17),
    _PnnixRouteTnsTimeStamp_Type()
)
pnnixRouteTnsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRouteTnsTimeStamp.setStatus("mandatory")


class _PnnixRouteTnsRowStatus_Type(Integer32):
    """Custom type pnnixRouteTnsRowStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("notActive", 5))
    )


_PnnixRouteTnsRowStatus_Type.__name__ = "Integer32"
_PnnixRouteTnsRowStatus_Object = MibTableColumn
pnnixRouteTnsRowStatus = _PnnixRouteTnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 1, 19, 5, 1, 18),
    _PnnixRouteTnsRowStatus_Type()
)
pnnixRouteTnsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnnixRouteTnsRowStatus.setStatus("mandatory")
_PnnixMIBConformance_ObjectIdentity = ObjectIdentity
pnnixMIBConformance = _PnnixMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2)
)
_PnnixMIBCompliances_ObjectIdentity = ObjectIdentity
pnnixMIBCompliances = _PnnixMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 1)
)
_PnnixMIBCompliance_ObjectIdentity = ObjectIdentity
pnnixMIBCompliance = _PnnixMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 1, 1)
)
_PnnixMIBGroups_ObjectIdentity = ObjectIdentity
pnnixMIBGroups = _PnnixMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2)
)
_PnnixGeneralMinGroup_ObjectIdentity = ObjectIdentity
pnnixGeneralMinGroup = _PnnixGeneralMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 1)
)
_PnnixGeneralBorderGroup_ObjectIdentity = ObjectIdentity
pnnixGeneralBorderGroup = _PnnixGeneralBorderGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 2)
)
_PnnixNodeMinGroup_ObjectIdentity = ObjectIdentity
pnnixNodeMinGroup = _PnnixNodeMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 3)
)
_PnnixNodePglMinGroup_ObjectIdentity = ObjectIdentity
pnnixNodePglMinGroup = _PnnixNodePglMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 4)
)
_PnnixNodePglLgnGroup_ObjectIdentity = ObjectIdentity
pnnixNodePglLgnGroup = _PnnixNodePglLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 5)
)
_PnnixNodeTimerMinGroup_ObjectIdentity = ObjectIdentity
pnnixNodeTimerMinGroup = _PnnixNodeTimerMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 6)
)
_PnnixNodeTimerLgnGroup_ObjectIdentity = ObjectIdentity
pnnixNodeTimerLgnGroup = _PnnixNodeTimerLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 7)
)
_PnnixNodeSvccLgnGroup_ObjectIdentity = ObjectIdentity
pnnixNodeSvccLgnGroup = _PnnixNodeSvccLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 8)
)
_PnnixScopeMinGroup_ObjectIdentity = ObjectIdentity
pnnixScopeMinGroup = _PnnixScopeMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 9)
)
_PnnixSummaryLgnGroup_ObjectIdentity = ObjectIdentity
pnnixSummaryLgnGroup = _PnnixSummaryLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 10)
)
_PnnixIfMinGroup_ObjectIdentity = ObjectIdentity
pnnixIfMinGroup = _PnnixIfMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 11)
)
_PnnixIfBorderGroup_ObjectIdentity = ObjectIdentity
pnnixIfBorderGroup = _PnnixIfBorderGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 12)
)
_PnnixLinkMinGroup_ObjectIdentity = ObjectIdentity
pnnixLinkMinGroup = _PnnixLinkMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 13)
)
_PnnixLinkBorderOrLgnGroup_ObjectIdentity = ObjectIdentity
pnnixLinkBorderOrLgnGroup = _PnnixLinkBorderOrLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 14)
)
_PnnixLinkLgnGroup_ObjectIdentity = ObjectIdentity
pnnixLinkLgnGroup = _PnnixLinkLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 15)
)
_PnnixNbrPeerMinGroup_ObjectIdentity = ObjectIdentity
pnnixNbrPeerMinGroup = _PnnixNbrPeerMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 16)
)
_PnnixNbrPeerLgnGroup_ObjectIdentity = ObjectIdentity
pnnixNbrPeerLgnGroup = _PnnixNbrPeerLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 17)
)
_PnnixNbrPeerPortMinGroup_ObjectIdentity = ObjectIdentity
pnnixNbrPeerPortMinGroup = _PnnixNbrPeerPortMinGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 18)
)
_PnnixSvccRccLgnGroup_ObjectIdentity = ObjectIdentity
pnnixSvccRccLgnGroup = _PnnixSvccRccLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 19)
)
_PnnixPtseOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixPtseOptionalGroup = _PnnixPtseOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 20)
)
_PnnixMapOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixMapOptionalGroup = _PnnixMapOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 21)
)
_PnnixMapNodeOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixMapNodeOptionalGroup = _PnnixMapNodeOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 22)
)
_PnnixMapAddrOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixMapAddrOptionalGroup = _PnnixMapAddrOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 23)
)
_PnnixMapTnsOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixMapTnsOptionalGroup = _PnnixMapTnsOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 24)
)
_PnnixMetricsOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixMetricsOptionalGroup = _PnnixMetricsOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 25)
)
_PnnixRouteGeneralOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixRouteGeneralOptionalGroup = _PnnixRouteGeneralOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 26)
)
_PnnixRouteNodeOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixRouteNodeOptionalGroup = _PnnixRouteNodeOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 27)
)
_PnnixDTLOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixDTLOptionalGroup = _PnnixDTLOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 28)
)
_PnnixRouteAddrOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixRouteAddrOptionalGroup = _PnnixRouteAddrOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 29)
)
_PnnixRouteTnsOptionalGroup_ObjectIdentity = ObjectIdentity
pnnixRouteTnsOptionalGroup = _PnnixRouteTnsOptionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 2, 2, 30)
)
_PnniIAdjMIBObjects_ObjectIdentity = ObjectIdentity
pnniIAdjMIBObjects = _PnniIAdjMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3)
)
_PnnixIAdjGroup_ObjectIdentity = ObjectIdentity
pnnixIAdjGroup = _PnnixIAdjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1)
)
_PnnixNumIAdj_Type = Counter32
_PnnixNumIAdj_Object = MibScalar
pnnixNumIAdj = _PnnixNumIAdj_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 1),
    _PnnixNumIAdj_Type()
)
pnnixNumIAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixNumIAdj.setStatus("mandatory")
_PnnixIAdjTable_Object = MibTable
pnnixIAdjTable = _PnnixIAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pnnixIAdjTable.setStatus("mandatory")
_PnnixIAdjEntry_Object = MibTableRow
pnnixIAdjEntry = _PnnixIAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1)
)
pnnixIAdjEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixIadjIndex"),
)
if mibBuilder.loadTexts:
    pnnixIAdjEntry.setStatus("mandatory")
_PnnixIadjIndex_Type = Integer32
_PnnixIadjIndex_Object = MibTableColumn
pnnixIadjIndex = _PnnixIadjIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 1),
    _PnnixIadjIndex_Type()
)
pnnixIadjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixIadjIndex.setStatus("mandatory")
_PnnixIAdjAtmAddress_Type = PnnixAtmAddr
_PnnixIAdjAtmAddress_Object = MibTableColumn
pnnixIAdjAtmAddress = _PnnixIAdjAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 2),
    _PnnixIAdjAtmAddress_Type()
)
pnnixIAdjAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjAtmAddress.setStatus("mandatory")
_PnnixIAdjSlot_Type = Integer32
_PnnixIAdjSlot_Object = MibTableColumn
pnnixIAdjSlot = _PnnixIAdjSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 3),
    _PnnixIAdjSlot_Type()
)
pnnixIAdjSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjSlot.setStatus("mandatory")
_PnnixIAdjPort_Type = Integer32
_PnnixIAdjPort_Object = MibTableColumn
pnnixIAdjPort = _PnnixIAdjPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 4),
    _PnnixIAdjPort_Type()
)
pnnixIAdjPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjPort.setStatus("mandatory")
_PnnixIAdjInst_Type = Integer32
_PnnixIAdjInst_Object = MibTableColumn
pnnixIAdjInst = _PnnixIAdjInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 5),
    _PnnixIAdjInst_Type()
)
pnnixIAdjInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjInst.setStatus("mandatory")
_PnnixIAdjCsmPPort_Type = Integer32
_PnnixIAdjCsmPPort_Object = MibTableColumn
pnnixIAdjCsmPPort = _PnnixIAdjCsmPPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 6),
    _PnnixIAdjCsmPPort_Type()
)
pnnixIAdjCsmPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjCsmPPort.setStatus("mandatory")
_PnnixIAdjAdvertised_Type = TruthValue
_PnnixIAdjAdvertised_Object = MibTableColumn
pnnixIAdjAdvertised = _PnnixIAdjAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 7),
    _PnnixIAdjAdvertised_Type()
)
pnnixIAdjAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjAdvertised.setStatus("mandatory")
_PnnixIAdjSummarized_Type = TruthValue
_PnnixIAdjSummarized_Object = MibTableColumn
pnnixIAdjSummarized = _PnnixIAdjSummarized_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 8),
    _PnnixIAdjSummarized_Type()
)
pnnixIAdjSummarized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjSummarized.setStatus("mandatory")
_PnnixIAdjLearned_Type = DisplayString
_PnnixIAdjLearned_Object = MibTableColumn
pnnixIAdjLearned = _PnnixIAdjLearned_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 3, 1, 2, 1, 9),
    _PnnixIAdjLearned_Type()
)
pnnixIAdjLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixIAdjLearned.setStatus("mandatory")
_PnniTestMIBObjects_ObjectIdentity = ObjectIdentity
pnniTestMIBObjects = _PnniTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4)
)
_PnniRtstMIBGroup_ObjectIdentity = ObjectIdentity
pnniRtstMIBGroup = _PnniRtstMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1)
)
_PnnixRtstTable_Object = MibTable
pnnixRtstTable = _PnnixRtstTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    pnnixRtstTable.setStatus("mandatory")
_PnnixRtstEntry_Object = MibTableRow
pnnixRtstEntry = _PnnixRtstEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1)
)
pnnixRtstEntry.setIndexNames(
    (0, "XPNNI-MIB", "pnnixNodeIndex"),
    (0, "XPNNI-MIB", "pnnixRtstClass"),
    (0, "XPNNI-MIB", "pnnixRtstType"),
    (0, "XPNNI-MIB", "pnnixRtstDest"),
)
if mibBuilder.loadTexts:
    pnnixRtstEntry.setStatus("mandatory")


class _PnnixRtstClass_Type(Integer32):
    """Custom type pnnixRtstClass based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("ubr", 1),
          ("vbrNrt", 4),
          ("vbrRt", 3))
    )


_PnnixRtstClass_Type.__name__ = "Integer32"
_PnnixRtstClass_Object = MibTableColumn
pnnixRtstClass = _PnnixRtstClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 1),
    _PnnixRtstClass_Type()
)
pnnixRtstClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRtstClass.setStatus("mandatory")


class _PnnixRtstType_Type(Integer32):
    """Custom type pnnixRtstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmp", 2),
          ("ptpt", 1))
    )


_PnnixRtstType_Type.__name__ = "Integer32"
_PnnixRtstType_Object = MibTableColumn
pnnixRtstType = _PnnixRtstType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 2),
    _PnnixRtstType_Type()
)
pnnixRtstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRtstType.setStatus("mandatory")


class _PnnixRtstDest_Type(OctetString):
    """Custom type pnnixRtstDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PnnixRtstDest_Type.__name__ = "OctetString"
_PnnixRtstDest_Object = MibTableColumn
pnnixRtstDest = _PnnixRtstDest_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 3),
    _PnnixRtstDest_Type()
)
pnnixRtstDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnnixRtstDest.setStatus("mandatory")


class _PnnixRtstError_Type(Integer32):
    """Custom type pnnixRtstError based on Integer32"""
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
        *(("dtlExhaustion", 3),
          ("noRouteToDest", 2),
          ("other", 4),
          ("success", 1))
    )


_PnnixRtstError_Type.__name__ = "Integer32"
_PnnixRtstError_Object = MibTableColumn
pnnixRtstError = _PnnixRtstError_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 4),
    _PnnixRtstError_Type()
)
pnnixRtstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstError.setStatus("mandatory")


class _PnnixRtstFlags_Type(Integer32):
    """Custom type pnnixRtstFlags based on Integer32"""
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
        *(("direct", 2),
          ("directEreach", 4),
          ("dtlAdded", 1),
          ("myself", 3))
    )


_PnnixRtstFlags_Type.__name__ = "Integer32"
_PnnixRtstFlags_Object = MibTableColumn
pnnixRtstFlags = _PnnixRtstFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 5),
    _PnnixRtstFlags_Type()
)
pnnixRtstFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstFlags.setStatus("mandatory")
_PnnixRtstOutboundPort_Type = PnnixPortId
_PnnixRtstOutboundPort_Object = MibTableColumn
pnnixRtstOutboundPort = _PnnixRtstOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 6),
    _PnnixRtstOutboundPort_Type()
)
pnnixRtstOutboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstOutboundPort.setStatus("mandatory")
_PnnixRtstVPI_Type = Integer32
_PnnixRtstVPI_Object = MibTableColumn
pnnixRtstVPI = _PnnixRtstVPI_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 7),
    _PnnixRtstVPI_Type()
)
pnnixRtstVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstVPI.setStatus("mandatory")


class _PnnixRtstE164_Type(OctetString):
    """Custom type pnnixRtstE164 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PnnixRtstE164_Type.__name__ = "OctetString"
_PnnixRtstE164_Object = MibTableColumn
pnnixRtstE164 = _PnnixRtstE164_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 8),
    _PnnixRtstE164_Type()
)
pnnixRtstE164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstE164.setStatus("mandatory")
_PnnixRtstE164len_Type = Integer32
_PnnixRtstE164len_Object = MibTableColumn
pnnixRtstE164len = _PnnixRtstE164len_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 9),
    _PnnixRtstE164len_Type()
)
pnnixRtstE164len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstE164len.setStatus("mandatory")


class _PnnixRtstHopCount_Type(Integer32):
    """Custom type pnnixRtstHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_PnnixRtstHopCount_Type.__name__ = "Integer32"
_PnnixRtstHopCount_Object = MibTableColumn
pnnixRtstHopCount = _PnnixRtstHopCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 10),
    _PnnixRtstHopCount_Type()
)
pnnixRtstHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstHopCount.setStatus("mandatory")


class _PnnixRtstDTL_Type(OctetString):
    """Custom type pnnixRtstDTL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(52, 1500),
    )


_PnnixRtstDTL_Type.__name__ = "OctetString"
_PnnixRtstDTL_Object = MibTableColumn
pnnixRtstDTL = _PnnixRtstDTL_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 11),
    _PnnixRtstDTL_Type()
)
pnnixRtstDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstDTL.setStatus("mandatory")
_PnnixRtstCurPointer_Type = Integer32
_PnnixRtstCurPointer_Object = MibTableColumn
pnnixRtstCurPointer = _PnnixRtstCurPointer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 1, 4, 1, 1, 1, 12),
    _PnnixRtstCurPointer_Type()
)
pnnixRtstCurPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnnixRtstCurPointer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XPNNI-MIB",
    **{"PnnixAtmAddr": PnnixAtmAddr,
       "PnnixNodeIndex": PnnixNodeIndex,
       "InterfaceIndex": InterfaceIndex,
       "TruthValue": TruthValue,
       "AtmpTrafficDescrParamIndex": AtmpTrafficDescrParamIndex,
       "PnnixNodeId": PnnixNodeId,
       "PnnixPortId": PnnixPortId,
       "PnnixAggrToken": PnnixAggrToken,
       "PnnixPeerGroupId": PnnixPeerGroupId,
       "PnnixLevel": PnnixLevel,
       "PnnixSvccRccIndex": PnnixSvccRccIndex,
       "AtmAddrPrefix": AtmAddrPrefix,
       "PnnixPrefixLength": PnnixPrefixLength,
       "PnnixMetricsTag": PnnixMetricsTag,
       "ServiceCategory": ServiceCategory,
       "ClpType": ClpType,
       "TnsType": TnsType,
       "TnsPlan": TnsPlan,
       "PnnixVersion": PnnixVersion,
       "PnnixHelloState": PnnixHelloState,
       "pnnixMIB": pnnixMIB,
       "pnnixMIBObjects": pnnixMIBObjects,
       "pnnixBaseGroup": pnnixBaseGroup,
       "pnnixHighestVersion": pnnixHighestVersion,
       "pnnixLowestVersion": pnnixLowestVersion,
       "pnnixDtlCountOriginator": pnnixDtlCountOriginator,
       "pnnixDtlCountBorder": pnnixDtlCountBorder,
       "pnnixCrankbackCountOriginator": pnnixCrankbackCountOriginator,
       "pnnixCrankbackCountBorder": pnnixCrankbackCountBorder,
       "pnnixAltRouteCountOriginator": pnnixAltRouteCountOriginator,
       "pnnixAltRouteCountBorder": pnnixAltRouteCountBorder,
       "pnnixRouteFailCountOriginator": pnnixRouteFailCountOriginator,
       "pnnixRouteFailCountBorder": pnnixRouteFailCountBorder,
       "pnnixRouteFailUnreachableOriginator": pnnixRouteFailUnreachableOriginator,
       "pnnixRouteFailUnreachableBorder": pnnixRouteFailUnreachableBorder,
       "pnnixNodeTable": pnnixNodeTable,
       "pnnixNodeEntry": pnnixNodeEntry,
       "pnnixNodeIndex": pnnixNodeIndex,
       "pnnixNodeLevel": pnnixNodeLevel,
       "pnnixNodeId": pnnixNodeId,
       "pnnixNodeLowest": pnnixNodeLowest,
       "pnnixNodeAdminStatus": pnnixNodeAdminStatus,
       "pnnixNodeOperStatus": pnnixNodeOperStatus,
       "pnnixNodeDomainName": pnnixNodeDomainName,
       "pnnixNodeAtmAddress": pnnixNodeAtmAddress,
       "pnnixNodePeerGroupId": pnnixNodePeerGroupId,
       "pnnixNodeRestrictedTransit": pnnixNodeRestrictedTransit,
       "pnnixNodeComplexRep": pnnixNodeComplexRep,
       "pnnixNodeRestrictedBranching": pnnixNodeRestrictedBranching,
       "pnnixNodeDatabaseOverload": pnnixNodeDatabaseOverload,
       "pnnixNodePtses": pnnixNodePtses,
       "pnnixNodeRowStatus": pnnixNodeRowStatus,
       "pnnixNodePglTable": pnnixNodePglTable,
       "pnnixNodePglEntry": pnnixNodePglEntry,
       "pnnixNodePglLeadershipPriority": pnnixNodePglLeadershipPriority,
       "pnnixNodeCfgParentNodeIndex": pnnixNodeCfgParentNodeIndex,
       "pnnixNodePglInitTime": pnnixNodePglInitTime,
       "pnnixNodePglOverrideDelay": pnnixNodePglOverrideDelay,
       "pnnixNodePglReelectTime": pnnixNodePglReelectTime,
       "pnnixNodePglState": pnnixNodePglState,
       "pnnixNodePreferredPgl": pnnixNodePreferredPgl,
       "pnnixNodePeerGroupLeader": pnnixNodePeerGroupLeader,
       "pnnixNodePglTimeStamp": pnnixNodePglTimeStamp,
       "pnnixNodeActiveParentNodeId": pnnixNodeActiveParentNodeId,
       "pnnixNodeTimerTable": pnnixNodeTimerTable,
       "pnnixNodeTimerEntry": pnnixNodeTimerEntry,
       "pnnixNodePtseHolddown": pnnixNodePtseHolddown,
       "pnnixNodeHelloHolddown": pnnixNodeHelloHolddown,
       "pnnixNodeHelloInterval": pnnixNodeHelloInterval,
       "pnnixNodeHelloInactivityFactor": pnnixNodeHelloInactivityFactor,
       "pnnixNodeHlinkInact": pnnixNodeHlinkInact,
       "pnnixNodePtseRefreshInterval": pnnixNodePtseRefreshInterval,
       "pnnixNodePtseLifetimeFactor": pnnixNodePtseLifetimeFactor,
       "pnnixNodeRxmtInterval": pnnixNodeRxmtInterval,
       "pnnixNodePeerDelayedAckInterval": pnnixNodePeerDelayedAckInterval,
       "pnnixNodeAvcrPm": pnnixNodeAvcrPm,
       "pnnixNodeAvcrMt": pnnixNodeAvcrMt,
       "pnnixNodeCdvPm": pnnixNodeCdvPm,
       "pnnixNodeCtdPm": pnnixNodeCtdPm,
       "pnnixNodeSvccTable": pnnixNodeSvccTable,
       "pnnixNodeSvccEntry": pnnixNodeSvccEntry,
       "pnnixNodeSvccInitTime": pnnixNodeSvccInitTime,
       "pnnixNodeSvccRetryTime": pnnixNodeSvccRetryTime,
       "pnnixNodeSvccCallingIntegrityTime": pnnixNodeSvccCallingIntegrityTime,
       "pnnixNodeSvccCalledIntegrityTime": pnnixNodeSvccCalledIntegrityTime,
       "pnnixNodeSvccTrafficDescriptorIndex": pnnixNodeSvccTrafficDescriptorIndex,
       "pnnixScopeMappingTable": pnnixScopeMappingTable,
       "pnnixScopeMappingEntry": pnnixScopeMappingEntry,
       "pnnixScopeLocalNetwork": pnnixScopeLocalNetwork,
       "pnnixScopeLocalNetworkPlusOne": pnnixScopeLocalNetworkPlusOne,
       "pnnixScopeLocalNetworkPlusTwo": pnnixScopeLocalNetworkPlusTwo,
       "pnnixScopeSiteMinusOne": pnnixScopeSiteMinusOne,
       "pnnixScopeIntraSite": pnnixScopeIntraSite,
       "pnnixScopeSitePlusOne": pnnixScopeSitePlusOne,
       "pnnixScopeOrganizationMinusOne": pnnixScopeOrganizationMinusOne,
       "pnnixScopeIntraOrganization": pnnixScopeIntraOrganization,
       "pnnixScopeOrganizationPlusOne": pnnixScopeOrganizationPlusOne,
       "pnnixScopeCommunityMinusOne": pnnixScopeCommunityMinusOne,
       "pnnixScopeIntraCommunity": pnnixScopeIntraCommunity,
       "pnnixScopeCommunityPlusOne": pnnixScopeCommunityPlusOne,
       "pnnixScopeRegional": pnnixScopeRegional,
       "pnnixScopeInterRegional": pnnixScopeInterRegional,
       "pnnixScopeGlobal": pnnixScopeGlobal,
       "pnnixSummaryTable": pnnixSummaryTable,
       "pnnixSummaryEntry": pnnixSummaryEntry,
       "pnnixSummaryAddress": pnnixSummaryAddress,
       "pnnixSummaryPrefixLength": pnnixSummaryPrefixLength,
       "pnnixSummaryType": pnnixSummaryType,
       "pnnixSummarySuppress": pnnixSummarySuppress,
       "pnnixSummaryState": pnnixSummaryState,
       "pnnixSummaryRowStatus": pnnixSummaryRowStatus,
       "pnnixIfTable": pnnixIfTable,
       "pnnixIfEntry": pnnixIfEntry,
       "pnnixIfNodeIndex": pnnixIfNodeIndex,
       "pnnixIfPortId": pnnixIfPortId,
       "pnnixIfAggrToken": pnnixIfAggrToken,
       "pnnixIfVPCapability": pnnixIfVPCapability,
       "pnnixIfAdmWeightCbr": pnnixIfAdmWeightCbr,
       "pnnixIfAdmWeightRtVbr": pnnixIfAdmWeightRtVbr,
       "pnnixIfAdmWeightNrtVbr": pnnixIfAdmWeightNrtVbr,
       "pnnixIfAdmWeightAbr": pnnixIfAdmWeightAbr,
       "pnnixIfAdmWeightUbr": pnnixIfAdmWeightUbr,
       "pnnixIfRccServiceCategory": pnnixIfRccServiceCategory,
       "pnnixIfRccTrafficDescrIndex": pnnixIfRccTrafficDescrIndex,
       "pnnixLinkTable": pnnixLinkTable,
       "pnnixLinkEntry": pnnixLinkEntry,
       "pnnixLinkPortId": pnnixLinkPortId,
       "pnnixLinkType": pnnixLinkType,
       "pnnixLinkVersion": pnnixLinkVersion,
       "pnnixLinkHelloState": pnnixLinkHelloState,
       "pnnixLinkRemoteNodeId": pnnixLinkRemoteNodeId,
       "pnnixLinkRemotePortId": pnnixLinkRemotePortId,
       "pnnixLinkDerivedAggrToken": pnnixLinkDerivedAggrToken,
       "pnnixLinkUpnodeId": pnnixLinkUpnodeId,
       "pnnixLinkUpnodeAtmAddress": pnnixLinkUpnodeAtmAddress,
       "pnnixLinkCommonPeerGroupId": pnnixLinkCommonPeerGroupId,
       "pnnixLinkIfIndex": pnnixLinkIfIndex,
       "pnnixLinkSvccRccIndex": pnnixLinkSvccRccIndex,
       "pnnixLinkRcvHellos": pnnixLinkRcvHellos,
       "pnnixLinkXmtHellos": pnnixLinkXmtHellos,
       "pnnixNbrPeerTable": pnnixNbrPeerTable,
       "pnnixNbrPeerEntry": pnnixNbrPeerEntry,
       "pnnixNbrPeerRemoteNodeId": pnnixNbrPeerRemoteNodeId,
       "pnnixNbrPeerState": pnnixNbrPeerState,
       "pnnixNbrPeerSvccRccIndex": pnnixNbrPeerSvccRccIndex,
       "pnnixNbrPeerPortCount": pnnixNbrPeerPortCount,
       "pnnixNbrPeerRcvDbSums": pnnixNbrPeerRcvDbSums,
       "pnnixNbrPeerXmtDbSums": pnnixNbrPeerXmtDbSums,
       "pnnixNbrPeerRcvPtsps": pnnixNbrPeerRcvPtsps,
       "pnnixNbrPeerXmtPtsps": pnnixNbrPeerXmtPtsps,
       "pnnixNbrPeerRcvPtseReqs": pnnixNbrPeerRcvPtseReqs,
       "pnnixNbrPeerXmtPtseReqs": pnnixNbrPeerXmtPtseReqs,
       "pnnixNbrPeerRcvPtseAcks": pnnixNbrPeerRcvPtseAcks,
       "pnnixNbrPeerXmtPtseAcks": pnnixNbrPeerXmtPtseAcks,
       "pnnixNbrPeerPortTable": pnnixNbrPeerPortTable,
       "pnnixNbrPeerPortEntry": pnnixNbrPeerPortEntry,
       "pnnixNbrPeerPortId": pnnixNbrPeerPortId,
       "pnnixNbrPeerPortFloodStatus": pnnixNbrPeerPortFloodStatus,
       "pnnixSvccRccTable": pnnixSvccRccTable,
       "pnnixSvccRccEntry": pnnixSvccRccEntry,
       "pnnixSvccRccIndex": pnnixSvccRccIndex,
       "pnnixSvccRccVersion": pnnixSvccRccVersion,
       "pnnixSvccRccHelloState": pnnixSvccRccHelloState,
       "pnnixSvccRccRemoteNodeId": pnnixSvccRccRemoteNodeId,
       "pnnixSvccRccRemoteAtmAddress": pnnixSvccRccRemoteAtmAddress,
       "pnnixSvccRccRcvHellos": pnnixSvccRccRcvHellos,
       "pnnixSvccRccXmtHellos": pnnixSvccRccXmtHellos,
       "pnnixSvccRccIfIndex": pnnixSvccRccIfIndex,
       "pnnixSvccRccVpi": pnnixSvccRccVpi,
       "pnnixSvccRccVci": pnnixSvccRccVci,
       "pnnixPtseTable": pnnixPtseTable,
       "pnnixPtseEntry": pnnixPtseEntry,
       "pnnixPtseOriginatingNodeId": pnnixPtseOriginatingNodeId,
       "pnnixPtseId": pnnixPtseId,
       "pnnixPtseType": pnnixPtseType,
       "pnnixPtseSequenceNum": pnnixPtseSequenceNum,
       "pnnixPtseChecksum": pnnixPtseChecksum,
       "pnnixPtseLifeTime": pnnixPtseLifeTime,
       "pnnixPtseInfo": pnnixPtseInfo,
       "pnnixMapTable": pnnixMapTable,
       "pnnixMapEntry": pnnixMapEntry,
       "pnnixMapOriginatingNodeId": pnnixMapOriginatingNodeId,
       "pnnixMapOriginatingPortId": pnnixMapOriginatingPortId,
       "pnnixMapIndex": pnnixMapIndex,
       "pnnixMapType": pnnixMapType,
       "pnnixMapPeerGroupId": pnnixMapPeerGroupId,
       "pnnixMapAggrToken": pnnixMapAggrToken,
       "pnnixMapRemoteNodeId": pnnixMapRemoteNodeId,
       "pnnixMapRemotePortId": pnnixMapRemotePortId,
       "pnnixMapVPCapability": pnnixMapVPCapability,
       "pnnixMapPtseId": pnnixMapPtseId,
       "pnnixMapMetricsTag": pnnixMapMetricsTag,
       "pnnixMapNodeTable": pnnixMapNodeTable,
       "pnnixMapNodeEntry": pnnixMapNodeEntry,
       "pnnixMapNodeId": pnnixMapNodeId,
       "pnnixMapNodePeerGroupId": pnnixMapNodePeerGroupId,
       "pnnixMapNodeAtmAddress": pnnixMapNodeAtmAddress,
       "pnnixMapNodeRestrictedTransit": pnnixMapNodeRestrictedTransit,
       "pnnixMapNodeComplexRep": pnnixMapNodeComplexRep,
       "pnnixMapNodeRestrictedBranching": pnnixMapNodeRestrictedBranching,
       "pnnixMapNodeDatabaseOverload": pnnixMapNodeDatabaseOverload,
       "pnnixMapNodeIAmLeader": pnnixMapNodeIAmLeader,
       "pnnixMapNodeLeadershipPriority": pnnixMapNodeLeadershipPriority,
       "pnnixMapNodePreferredPgl": pnnixMapNodePreferredPgl,
       "pnnixMapNodeParentNodeId": pnnixMapNodeParentNodeId,
       "pnnixMapNodeParentAtmAddress": pnnixMapNodeParentAtmAddress,
       "pnnixMapNodeParentPeerGroupId": pnnixMapNodeParentPeerGroupId,
       "pnnixMapNodeParentPglNodeId": pnnixMapNodeParentPglNodeId,
       "pnnixMapAddrTable": pnnixMapAddrTable,
       "pnnixMapAddrEntry": pnnixMapAddrEntry,
       "pnnixMapAddrAdvertisingNodeId": pnnixMapAddrAdvertisingNodeId,
       "pnnixMapAddrAdvertisedPortId": pnnixMapAddrAdvertisedPortId,
       "pnnixMapAddrIndex": pnnixMapAddrIndex,
       "pnnixMapAddrAddress": pnnixMapAddrAddress,
       "pnnixMapAddrPrefixLength": pnnixMapAddrPrefixLength,
       "pnnixMapTnsTable": pnnixMapTnsTable,
       "pnnixMapTnsEntry": pnnixMapTnsEntry,
       "pnnixMapTnsAdvertisingNodeId": pnnixMapTnsAdvertisingNodeId,
       "pnnixMapTnsAdvertisedPortId": pnnixMapTnsAdvertisedPortId,
       "pnnixMapTnsType": pnnixMapTnsType,
       "pnnixMapTnsPlan": pnnixMapTnsPlan,
       "pnnixMapTnsId": pnnixMapTnsId,
       "pnnixMetricsTable": pnnixMetricsTable,
       "pnnixMetricsEntry": pnnixMetricsEntry,
       "pnnixMetricsTag": pnnixMetricsTag,
       "pnnixMetricsDirection": pnnixMetricsDirection,
       "pnnixMetricsIndex": pnnixMetricsIndex,
       "pnnixMetricsClasses": pnnixMetricsClasses,
       "pnnixMetricsGcacClp": pnnixMetricsGcacClp,
       "pnnixMetricsAdminWeight": pnnixMetricsAdminWeight,
       "pnnixMetrics1": pnnixMetrics1,
       "pnnixMetrics2": pnnixMetrics2,
       "pnnixMetrics3": pnnixMetrics3,
       "pnnixMetrics4": pnnixMetrics4,
       "pnnixMetrics5": pnnixMetrics5,
       "pnnixMetrics6": pnnixMetrics6,
       "pnnixMetrics7": pnnixMetrics7,
       "pnnixMetrics8": pnnixMetrics8,
       "pnnixMetricsRowStatus": pnnixMetricsRowStatus,
       "pnnixRoutingGroup": pnnixRoutingGroup,
       "pnnixRouteBaseGroup": pnnixRouteBaseGroup,
       "pnnixRouteNodeNumber": pnnixRouteNodeNumber,
       "pnnixRouteAddrNumber": pnnixRouteAddrNumber,
       "pnnixRouteNodeTable": pnnixRouteNodeTable,
       "pnnixRouteNodeEntry": pnnixRouteNodeEntry,
       "pnnixRouteNodeClass": pnnixRouteNodeClass,
       "pnnixRouteNodeDestNodeId": pnnixRouteNodeDestNodeId,
       "pnnixRouteNodeDTL": pnnixRouteNodeDTL,
       "pnnixRouteNodeDestPortId": pnnixRouteNodeDestPortId,
       "pnnixRouteNodeProto": pnnixRouteNodeProto,
       "pnnixRouteNodeTimeStamp": pnnixRouteNodeTimeStamp,
       "pnnixRouteNodeInfo": pnnixRouteNodeInfo,
       "pnnixRouteNodeGcacClp": pnnixRouteNodeGcacClp,
       "pnnixRouteNodeFwdMetricAW": pnnixRouteNodeFwdMetricAW,
       "pnnixRouteNodeFwdMetric1": pnnixRouteNodeFwdMetric1,
       "pnnixRouteNodeFwdMetric2": pnnixRouteNodeFwdMetric2,
       "pnnixRouteNodeFwdMetric3": pnnixRouteNodeFwdMetric3,
       "pnnixRouteNodeFwdMetric4": pnnixRouteNodeFwdMetric4,
       "pnnixRouteNodeFwdMetric5": pnnixRouteNodeFwdMetric5,
       "pnnixRouteNodeFwdMetric6": pnnixRouteNodeFwdMetric6,
       "pnnixRouteNodeFwdMetric7": pnnixRouteNodeFwdMetric7,
       "pnnixRouteNodeFwdMetric8": pnnixRouteNodeFwdMetric8,
       "pnnixRouteNodeBwdMetricAW": pnnixRouteNodeBwdMetricAW,
       "pnnixRouteNodeBwdMetric1": pnnixRouteNodeBwdMetric1,
       "pnnixRouteNodeBwdMetric2": pnnixRouteNodeBwdMetric2,
       "pnnixRouteNodeBwdMetric3": pnnixRouteNodeBwdMetric3,
       "pnnixRouteNodeBwdMetric4": pnnixRouteNodeBwdMetric4,
       "pnnixRouteNodeBwdMetric5": pnnixRouteNodeBwdMetric5,
       "pnnixRouteNodeBwdMetric6": pnnixRouteNodeBwdMetric6,
       "pnnixRouteNodeBwdMetric7": pnnixRouteNodeBwdMetric7,
       "pnnixRouteNodeBwdMetric8": pnnixRouteNodeBwdMetric8,
       "pnnixRouteNodeVPCapability": pnnixRouteNodeVPCapability,
       "pnnixRouteNodeStatus": pnnixRouteNodeStatus,
       "pnnixDTLTable": pnnixDTLTable,
       "pnnixDTLEntry": pnnixDTLEntry,
       "pnnixDTLIndex": pnnixDTLIndex,
       "pnnixDTLEntryIndex": pnnixDTLEntryIndex,
       "pnnixDTLNodeId": pnnixDTLNodeId,
       "pnnixDTLPortId": pnnixDTLPortId,
       "pnnixDTLLinkType": pnnixDTLLinkType,
       "pnnixDTLStatus": pnnixDTLStatus,
       "pnnixRouteAddrTable": pnnixRouteAddrTable,
       "pnnixRouteAddrEntry": pnnixRouteAddrEntry,
       "pnnixRouteAddrAddress": pnnixRouteAddrAddress,
       "pnnixRouteAddrPrefixLength": pnnixRouteAddrPrefixLength,
       "pnnixRouteAddrIndex": pnnixRouteAddrIndex,
       "pnnixRouteAddrIfIndex": pnnixRouteAddrIfIndex,
       "pnnixRouteAddrAdvertisingNodeId": pnnixRouteAddrAdvertisingNodeId,
       "pnnixRouteAddrAdvertisedPortId": pnnixRouteAddrAdvertisedPortId,
       "pnnixRouteAddrType": pnnixRouteAddrType,
       "pnnixRouteAddrProto": pnnixRouteAddrProto,
       "pnnixRouteAddrPnniScope": pnnixRouteAddrPnniScope,
       "pnnixRouteAddrVPCapability": pnnixRouteAddrVPCapability,
       "pnnixRouteAddrMetricsTag": pnnixRouteAddrMetricsTag,
       "pnnixRouteAddrPtseId": pnnixRouteAddrPtseId,
       "pnnixRouteAddrOriginateAdvertisement": pnnixRouteAddrOriginateAdvertisement,
       "pnnixRouteAddrInfo": pnnixRouteAddrInfo,
       "pnnixRouteAddrOperStatus": pnnixRouteAddrOperStatus,
       "pnnixRouteAddrTimeStamp": pnnixRouteAddrTimeStamp,
       "pnnixRouteAddrRowStatus": pnnixRouteAddrRowStatus,
       "pnnixRouteTnsTable": pnnixRouteTnsTable,
       "pnnixRouteTnsEntry": pnnixRouteTnsEntry,
       "pnnixRouteTnsType": pnnixRouteTnsType,
       "pnnixRouteTnsPlan": pnnixRouteTnsPlan,
       "pnnixRouteTnsId": pnnixRouteTnsId,
       "pnnixRouteTnsIndex": pnnixRouteTnsIndex,
       "pnnixRouteTnsIfIndex": pnnixRouteTnsIfIndex,
       "pnnixRouteTnsAdvertisingNodeId": pnnixRouteTnsAdvertisingNodeId,
       "pnnixRouteTnsAdvertisedPortId": pnnixRouteTnsAdvertisedPortId,
       "pnnixRouteTnsRouteType": pnnixRouteTnsRouteType,
       "pnnixRouteTnsProto": pnnixRouteTnsProto,
       "pnnixRouteTnsPnniScope": pnnixRouteTnsPnniScope,
       "pnnixRouteTnsVPCapability": pnnixRouteTnsVPCapability,
       "pnnixRouteTnsMetricsTag": pnnixRouteTnsMetricsTag,
       "pnnixRouteTnsPtseId": pnnixRouteTnsPtseId,
       "pnnixRouteTnsOriginateAdvertisement": pnnixRouteTnsOriginateAdvertisement,
       "pnnixRouteTnsInfo": pnnixRouteTnsInfo,
       "pnnixRouteTnsOperStatus": pnnixRouteTnsOperStatus,
       "pnnixRouteTnsTimeStamp": pnnixRouteTnsTimeStamp,
       "pnnixRouteTnsRowStatus": pnnixRouteTnsRowStatus,
       "pnnixMIBConformance": pnnixMIBConformance,
       "pnnixMIBCompliances": pnnixMIBCompliances,
       "pnnixMIBCompliance": pnnixMIBCompliance,
       "pnnixMIBGroups": pnnixMIBGroups,
       "pnnixGeneralMinGroup": pnnixGeneralMinGroup,
       "pnnixGeneralBorderGroup": pnnixGeneralBorderGroup,
       "pnnixNodeMinGroup": pnnixNodeMinGroup,
       "pnnixNodePglMinGroup": pnnixNodePglMinGroup,
       "pnnixNodePglLgnGroup": pnnixNodePglLgnGroup,
       "pnnixNodeTimerMinGroup": pnnixNodeTimerMinGroup,
       "pnnixNodeTimerLgnGroup": pnnixNodeTimerLgnGroup,
       "pnnixNodeSvccLgnGroup": pnnixNodeSvccLgnGroup,
       "pnnixScopeMinGroup": pnnixScopeMinGroup,
       "pnnixSummaryLgnGroup": pnnixSummaryLgnGroup,
       "pnnixIfMinGroup": pnnixIfMinGroup,
       "pnnixIfBorderGroup": pnnixIfBorderGroup,
       "pnnixLinkMinGroup": pnnixLinkMinGroup,
       "pnnixLinkBorderOrLgnGroup": pnnixLinkBorderOrLgnGroup,
       "pnnixLinkLgnGroup": pnnixLinkLgnGroup,
       "pnnixNbrPeerMinGroup": pnnixNbrPeerMinGroup,
       "pnnixNbrPeerLgnGroup": pnnixNbrPeerLgnGroup,
       "pnnixNbrPeerPortMinGroup": pnnixNbrPeerPortMinGroup,
       "pnnixSvccRccLgnGroup": pnnixSvccRccLgnGroup,
       "pnnixPtseOptionalGroup": pnnixPtseOptionalGroup,
       "pnnixMapOptionalGroup": pnnixMapOptionalGroup,
       "pnnixMapNodeOptionalGroup": pnnixMapNodeOptionalGroup,
       "pnnixMapAddrOptionalGroup": pnnixMapAddrOptionalGroup,
       "pnnixMapTnsOptionalGroup": pnnixMapTnsOptionalGroup,
       "pnnixMetricsOptionalGroup": pnnixMetricsOptionalGroup,
       "pnnixRouteGeneralOptionalGroup": pnnixRouteGeneralOptionalGroup,
       "pnnixRouteNodeOptionalGroup": pnnixRouteNodeOptionalGroup,
       "pnnixDTLOptionalGroup": pnnixDTLOptionalGroup,
       "pnnixRouteAddrOptionalGroup": pnnixRouteAddrOptionalGroup,
       "pnnixRouteTnsOptionalGroup": pnnixRouteTnsOptionalGroup,
       "pnniIAdjMIBObjects": pnniIAdjMIBObjects,
       "pnnixIAdjGroup": pnnixIAdjGroup,
       "pnnixNumIAdj": pnnixNumIAdj,
       "pnnixIAdjTable": pnnixIAdjTable,
       "pnnixIAdjEntry": pnnixIAdjEntry,
       "pnnixIadjIndex": pnnixIadjIndex,
       "pnnixIAdjAtmAddress": pnnixIAdjAtmAddress,
       "pnnixIAdjSlot": pnnixIAdjSlot,
       "pnnixIAdjPort": pnnixIAdjPort,
       "pnnixIAdjInst": pnnixIAdjInst,
       "pnnixIAdjCsmPPort": pnnixIAdjCsmPPort,
       "pnnixIAdjAdvertised": pnnixIAdjAdvertised,
       "pnnixIAdjSummarized": pnnixIAdjSummarized,
       "pnnixIAdjLearned": pnnixIAdjLearned,
       "pnniTestMIBObjects": pnniTestMIBObjects,
       "pnniRtstMIBGroup": pnniRtstMIBGroup,
       "pnnixRtstTable": pnnixRtstTable,
       "pnnixRtstEntry": pnnixRtstEntry,
       "pnnixRtstClass": pnnixRtstClass,
       "pnnixRtstType": pnnixRtstType,
       "pnnixRtstDest": pnnixRtstDest,
       "pnnixRtstError": pnnixRtstError,
       "pnnixRtstFlags": pnnixRtstFlags,
       "pnnixRtstOutboundPort": pnnixRtstOutboundPort,
       "pnnixRtstVPI": pnnixRtstVPI,
       "pnnixRtstE164": pnnixRtstE164,
       "pnnixRtstE164len": pnnixRtstE164len,
       "pnnixRtstHopCount": pnnixRtstHopCount,
       "pnnixRtstDTL": pnnixRtstDTL,
       "pnnixRtstCurPointer": pnnixRtstCurPointer}
)
