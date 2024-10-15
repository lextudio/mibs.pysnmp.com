# SNMP MIB module (ALCATEL-IND1-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-ROUTEMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:56 2024
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

(routingIND1Iprm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Iprm")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

alcatelIND1RouteMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3)
)
alcatelIND1RouteMapMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaRouteMapType(Integer32, TextualConvention):
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
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136)
        )
    )
    namedValues = NamedValues(
        *(("matchIpAccesList", 1),
          ("matchIpAddress", 2),
          ("matchIpNextHopAccessList", 3),
          ("matchIpNextHopAddress", 4),
          ("matchIpv4Interface", 10),
          ("matchIpv6AccessList", 5),
          ("matchIpv6Address", 6),
          ("matchIpv6Interface", 11),
          ("matchIpv6NextHopAddress", 8),
          ("matchIpv6nExtHopAccessList", 7),
          ("matchMetric", 12),
          ("matchRouteType", 13),
          ("matchTag", 9),
          ("setCommunity", 132),
          ("setIpNexthop", 135),
          ("setIpv6Nexthop", 136),
          ("setLevel", 134),
          ("setLocalPreference", 133),
          ("setMetric", 129),
          ("setMetricType", 130),
          ("setTag", 131))
    )



class AlaRouteMapAction(Integer32, TextualConvention):
    status = "current"
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



class AlaRouteMapRedistControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 3),
          ("allSubnets", 1),
          ("noSubnets", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RouteMapMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RouteMapMIBObjects = _AlcatelIND1RouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1)
)
_AlaRouteMapConfig_ObjectIdentity = ObjectIdentity
alaRouteMapConfig = _AlaRouteMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1)
)
_AlaRouteMapRedistProtoTable_Object = MibTable
alaRouteMapRedistProtoTable = _AlaRouteMapRedistProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaRouteMapRedistProtoTable.setStatus("current")
_AlaRouteMapRedistProtoEntry_Object = MibTableRow
alaRouteMapRedistProtoEntry = _AlaRouteMapRedistProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1)
)
alaRouteMapRedistProtoEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapRedistSrcProtoId"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapRedistDestProtoId"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapRedistRouteMapIndex"),
)
if mibBuilder.loadTexts:
    alaRouteMapRedistProtoEntry.setStatus("current")


class _AlaRouteMapRedistSrcProtoId_Type(Integer32):
    """Custom type alaRouteMapRedistSrcProtoId based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 6),
          ("bgp6", 9),
          ("isis", 10),
          ("isis6", 11),
          ("local", 2),
          ("ospf", 5),
          ("ospfv3", 8),
          ("other", 1),
          ("rip", 4),
          ("ripng", 7),
          ("static", 3))
    )


_AlaRouteMapRedistSrcProtoId_Type.__name__ = "Integer32"
_AlaRouteMapRedistSrcProtoId_Object = MibTableColumn
alaRouteMapRedistSrcProtoId = _AlaRouteMapRedistSrcProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 1),
    _AlaRouteMapRedistSrcProtoId_Type()
)
alaRouteMapRedistSrcProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapRedistSrcProtoId.setStatus("current")


class _AlaRouteMapRedistDestProtoId_Type(Integer32):
    """Custom type alaRouteMapRedistDestProtoId based on Integer32"""
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
        *(("bgp", 3),
          ("bgp6", 6),
          ("isis", 7),
          ("isis6", 8),
          ("ospf", 2),
          ("ospfv3", 5),
          ("rip", 1),
          ("ripng", 4))
    )


_AlaRouteMapRedistDestProtoId_Type.__name__ = "Integer32"
_AlaRouteMapRedistDestProtoId_Object = MibTableColumn
alaRouteMapRedistDestProtoId = _AlaRouteMapRedistDestProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 2),
    _AlaRouteMapRedistDestProtoId_Type()
)
alaRouteMapRedistDestProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapRedistDestProtoId.setStatus("current")
_AlaRouteMapRedistRouteMapIndex_Type = Unsigned32
_AlaRouteMapRedistRouteMapIndex_Object = MibTableColumn
alaRouteMapRedistRouteMapIndex = _AlaRouteMapRedistRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 3),
    _AlaRouteMapRedistRouteMapIndex_Type()
)
alaRouteMapRedistRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapRedistRouteMapIndex.setStatus("current")


class _AlaRouteMapRedistStatus_Type(Integer32):
    """Custom type alaRouteMapRedistStatus based on Integer32"""
    defaultValue = 1

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


_AlaRouteMapRedistStatus_Type.__name__ = "Integer32"
_AlaRouteMapRedistStatus_Object = MibTableColumn
alaRouteMapRedistStatus = _AlaRouteMapRedistStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 4),
    _AlaRouteMapRedistStatus_Type()
)
alaRouteMapRedistStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapRedistStatus.setStatus("current")
_AlaRouteMapRedistAddressType_Type = InetAddressType
_AlaRouteMapRedistAddressType_Object = MibTableColumn
alaRouteMapRedistAddressType = _AlaRouteMapRedistAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 5),
    _AlaRouteMapRedistAddressType_Type()
)
alaRouteMapRedistAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRouteMapRedistAddressType.setStatus("current")
_AlaRouteMapRedistRowStatus_Type = RowStatus
_AlaRouteMapRedistRowStatus_Object = MibTableColumn
alaRouteMapRedistRowStatus = _AlaRouteMapRedistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 1, 1, 6),
    _AlaRouteMapRedistRowStatus_Type()
)
alaRouteMapRedistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapRedistRowStatus.setStatus("current")
_AlaRouteMapAccessListNameTable_Object = MibTable
alaRouteMapAccessListNameTable = _AlaRouteMapAccessListNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaRouteMapAccessListNameTable.setStatus("current")
_AlaRouteMapAccessListNameEntry_Object = MibTableRow
alaRouteMapAccessListNameEntry = _AlaRouteMapAccessListNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2, 1)
)
alaRouteMapAccessListNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListName"),
)
if mibBuilder.loadTexts:
    alaRouteMapAccessListNameEntry.setStatus("current")


class _AlaRouteMapAccessListName_Type(DisplayString):
    """Custom type alaRouteMapAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlaRouteMapAccessListName_Type.__name__ = "DisplayString"
_AlaRouteMapAccessListName_Object = MibTableColumn
alaRouteMapAccessListName = _AlaRouteMapAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2, 1, 1),
    _AlaRouteMapAccessListName_Type()
)
alaRouteMapAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapAccessListName.setStatus("current")
_AlaRouteMapAccessListNameIndex_Type = Unsigned32
_AlaRouteMapAccessListNameIndex_Object = MibTableColumn
alaRouteMapAccessListNameIndex = _AlaRouteMapAccessListNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2, 1, 2),
    _AlaRouteMapAccessListNameIndex_Type()
)
alaRouteMapAccessListNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRouteMapAccessListNameIndex.setStatus("current")
_AlaRouteMapAccessListNameAddressType_Type = InetAddressType
_AlaRouteMapAccessListNameAddressType_Object = MibTableColumn
alaRouteMapAccessListNameAddressType = _AlaRouteMapAccessListNameAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2, 1, 3),
    _AlaRouteMapAccessListNameAddressType_Type()
)
alaRouteMapAccessListNameAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapAccessListNameAddressType.setStatus("current")
_AlaRouteMapAccessListNameRowStatus_Type = RowStatus
_AlaRouteMapAccessListNameRowStatus_Object = MibTableColumn
alaRouteMapAccessListNameRowStatus = _AlaRouteMapAccessListNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 2, 1, 4),
    _AlaRouteMapAccessListNameRowStatus_Type()
)
alaRouteMapAccessListNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapAccessListNameRowStatus.setStatus("current")
_AlaRouteMapAccessListTable_Object = MibTable
alaRouteMapAccessListTable = _AlaRouteMapAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaRouteMapAccessListTable.setStatus("current")
_AlaRouteMapAccessListEntry_Object = MibTableRow
alaRouteMapAccessListEntry = _AlaRouteMapAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1)
)
alaRouteMapAccessListEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListIndex"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListAddressType"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListAddress"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListPrefixLength"),
)
if mibBuilder.loadTexts:
    alaRouteMapAccessListEntry.setStatus("current")


class _AlaRouteMapAccessListIndex_Type(Unsigned32):
    """Custom type alaRouteMapAccessListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaRouteMapAccessListIndex_Type.__name__ = "Unsigned32"
_AlaRouteMapAccessListIndex_Object = MibTableColumn
alaRouteMapAccessListIndex = _AlaRouteMapAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 1),
    _AlaRouteMapAccessListIndex_Type()
)
alaRouteMapAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapAccessListIndex.setStatus("current")
_AlaRouteMapAccessListAddressType_Type = InetAddressType
_AlaRouteMapAccessListAddressType_Object = MibTableColumn
alaRouteMapAccessListAddressType = _AlaRouteMapAccessListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 2),
    _AlaRouteMapAccessListAddressType_Type()
)
alaRouteMapAccessListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapAccessListAddressType.setStatus("current")
_AlaRouteMapAccessListAddress_Type = InetAddress
_AlaRouteMapAccessListAddress_Object = MibTableColumn
alaRouteMapAccessListAddress = _AlaRouteMapAccessListAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 3),
    _AlaRouteMapAccessListAddress_Type()
)
alaRouteMapAccessListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapAccessListAddress.setStatus("current")


class _AlaRouteMapAccessListPrefixLength_Type(Unsigned32):
    """Custom type alaRouteMapAccessListPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaRouteMapAccessListPrefixLength_Type.__name__ = "Unsigned32"
_AlaRouteMapAccessListPrefixLength_Object = MibTableColumn
alaRouteMapAccessListPrefixLength = _AlaRouteMapAccessListPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 4),
    _AlaRouteMapAccessListPrefixLength_Type()
)
alaRouteMapAccessListPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapAccessListPrefixLength.setStatus("current")
_AlaRouteMapAccessListRedistControl_Type = AlaRouteMapRedistControl
_AlaRouteMapAccessListRedistControl_Object = MibTableColumn
alaRouteMapAccessListRedistControl = _AlaRouteMapAccessListRedistControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 5),
    _AlaRouteMapAccessListRedistControl_Type()
)
alaRouteMapAccessListRedistControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapAccessListRedistControl.setStatus("current")
_AlaRouteMapAccessListAction_Type = AlaRouteMapAction
_AlaRouteMapAccessListAction_Object = MibTableColumn
alaRouteMapAccessListAction = _AlaRouteMapAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 6),
    _AlaRouteMapAccessListAction_Type()
)
alaRouteMapAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapAccessListAction.setStatus("current")
_AlaRouteMapAccessListRowStatus_Type = RowStatus
_AlaRouteMapAccessListRowStatus_Object = MibTableColumn
alaRouteMapAccessListRowStatus = _AlaRouteMapAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 3, 1, 7),
    _AlaRouteMapAccessListRowStatus_Type()
)
alaRouteMapAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapAccessListRowStatus.setStatus("current")
_AlaRouteMapNameTable_Object = MibTable
alaRouteMapNameTable = _AlaRouteMapNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaRouteMapNameTable.setStatus("current")
_AlaRouteMapNameEntry_Object = MibTableRow
alaRouteMapNameEntry = _AlaRouteMapNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 4, 1)
)
alaRouteMapNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapName"),
)
if mibBuilder.loadTexts:
    alaRouteMapNameEntry.setStatus("current")


class _AlaRouteMapName_Type(DisplayString):
    """Custom type alaRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlaRouteMapName_Type.__name__ = "DisplayString"
_AlaRouteMapName_Object = MibTableColumn
alaRouteMapName = _AlaRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 4, 1, 1),
    _AlaRouteMapName_Type()
)
alaRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapName.setStatus("current")
_AlaRouteMapNameIndex_Type = Unsigned32
_AlaRouteMapNameIndex_Object = MibTableColumn
alaRouteMapNameIndex = _AlaRouteMapNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 4, 1, 2),
    _AlaRouteMapNameIndex_Type()
)
alaRouteMapNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRouteMapNameIndex.setStatus("current")
_AlaRouteMapNameRowStatus_Type = RowStatus
_AlaRouteMapNameRowStatus_Object = MibTableColumn
alaRouteMapNameRowStatus = _AlaRouteMapNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 4, 1, 3),
    _AlaRouteMapNameRowStatus_Type()
)
alaRouteMapNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapNameRowStatus.setStatus("current")
_AlaRouteMapSequenceTable_Object = MibTable
alaRouteMapSequenceTable = _AlaRouteMapSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaRouteMapSequenceTable.setStatus("current")
_AlaRouteMapSequenceEntry_Object = MibTableRow
alaRouteMapSequenceEntry = _AlaRouteMapSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5, 1)
)
alaRouteMapSequenceEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapSequenceIndex"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapSequenceNumber"),
)
if mibBuilder.loadTexts:
    alaRouteMapSequenceEntry.setStatus("current")
_AlaRouteMapSequenceIndex_Type = Unsigned32
_AlaRouteMapSequenceIndex_Object = MibTableColumn
alaRouteMapSequenceIndex = _AlaRouteMapSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5, 1, 1),
    _AlaRouteMapSequenceIndex_Type()
)
alaRouteMapSequenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapSequenceIndex.setStatus("current")


class _AlaRouteMapSequenceNumber_Type(Unsigned32):
    """Custom type alaRouteMapSequenceNumber based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaRouteMapSequenceNumber_Type.__name__ = "Unsigned32"
_AlaRouteMapSequenceNumber_Object = MibTableColumn
alaRouteMapSequenceNumber = _AlaRouteMapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5, 1, 2),
    _AlaRouteMapSequenceNumber_Type()
)
alaRouteMapSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapSequenceNumber.setStatus("current")
_AlaRouteMapSequenceAction_Type = AlaRouteMapAction
_AlaRouteMapSequenceAction_Object = MibTableColumn
alaRouteMapSequenceAction = _AlaRouteMapSequenceAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5, 1, 3),
    _AlaRouteMapSequenceAction_Type()
)
alaRouteMapSequenceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapSequenceAction.setStatus("current")
_AlaRouteMapSequenceRowStatus_Type = RowStatus
_AlaRouteMapSequenceRowStatus_Object = MibTableColumn
alaRouteMapSequenceRowStatus = _AlaRouteMapSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 5, 1, 4),
    _AlaRouteMapSequenceRowStatus_Type()
)
alaRouteMapSequenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapSequenceRowStatus.setStatus("current")
_AlaRouteMapTable_Object = MibTable
alaRouteMapTable = _AlaRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaRouteMapTable.setStatus("current")
_AlaRouteMapEntry_Object = MibTableRow
alaRouteMapEntry = _AlaRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1)
)
alaRouteMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapIndex"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapSequence"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapType"),
    (0, "ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapValue"),
)
if mibBuilder.loadTexts:
    alaRouteMapEntry.setStatus("current")
_AlaRouteMapIndex_Type = Unsigned32
_AlaRouteMapIndex_Object = MibTableColumn
alaRouteMapIndex = _AlaRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1, 1),
    _AlaRouteMapIndex_Type()
)
alaRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapIndex.setStatus("current")


class _AlaRouteMapSequence_Type(Unsigned32):
    """Custom type alaRouteMapSequence based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlaRouteMapSequence_Type.__name__ = "Unsigned32"
_AlaRouteMapSequence_Object = MibTableColumn
alaRouteMapSequence = _AlaRouteMapSequence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1, 2),
    _AlaRouteMapSequence_Type()
)
alaRouteMapSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapSequence.setStatus("current")
_AlaRouteMapType_Type = AlaRouteMapType
_AlaRouteMapType_Object = MibTableColumn
alaRouteMapType = _AlaRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1, 3),
    _AlaRouteMapType_Type()
)
alaRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapType.setStatus("current")


class _AlaRouteMapValue_Type(DisplayString):
    """Custom type alaRouteMapValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaRouteMapValue_Type.__name__ = "DisplayString"
_AlaRouteMapValue_Object = MibTableColumn
alaRouteMapValue = _AlaRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1, 4),
    _AlaRouteMapValue_Type()
)
alaRouteMapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRouteMapValue.setStatus("current")
_AlaRouteMapRowStatus_Type = RowStatus
_AlaRouteMapRowStatus_Object = MibTableColumn
alaRouteMapRowStatus = _AlaRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 1, 1, 6, 1, 5),
    _AlaRouteMapRowStatus_Type()
)
alaRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRouteMapRowStatus.setStatus("current")
_AlcatelIND1RouteMapMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RouteMapMIBConformance = _AlcatelIND1RouteMapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 2)
)
_AlcatelIND1RouteMapMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RouteMapMIBCompliances = _AlcatelIND1RouteMapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 2, 1)
)
_AlcatelIND1RouteMapMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RouteMapMIBGroups = _AlcatelIND1RouteMapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 2, 2)
)

# Managed Objects groups

alaRouteMapConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 2, 2, 1)
)
alaRouteMapConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListNameIndex"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListNameAddressType"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListNameRowStatus"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListRedistControl"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListAction"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapAccessListRowStatus"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapNameIndex"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapNameRowStatus"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapSequenceAction"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapSequenceRowStatus"),
        ("ALCATEL-IND1-ROUTEMAP-MIB", "alaRouteMapRowStatus"))
)
if mibBuilder.loadTexts:
    alaRouteMapConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaRouteMapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaRouteMapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-ROUTEMAP-MIB",
    **{"AlaRouteMapType": AlaRouteMapType,
       "AlaRouteMapAction": AlaRouteMapAction,
       "AlaRouteMapRedistControl": AlaRouteMapRedistControl,
       "alcatelIND1RouteMapMIB": alcatelIND1RouteMapMIB,
       "alcatelIND1RouteMapMIBObjects": alcatelIND1RouteMapMIBObjects,
       "alaRouteMapConfig": alaRouteMapConfig,
       "alaRouteMapRedistProtoTable": alaRouteMapRedistProtoTable,
       "alaRouteMapRedistProtoEntry": alaRouteMapRedistProtoEntry,
       "alaRouteMapRedistSrcProtoId": alaRouteMapRedistSrcProtoId,
       "alaRouteMapRedistDestProtoId": alaRouteMapRedistDestProtoId,
       "alaRouteMapRedistRouteMapIndex": alaRouteMapRedistRouteMapIndex,
       "alaRouteMapRedistStatus": alaRouteMapRedistStatus,
       "alaRouteMapRedistAddressType": alaRouteMapRedistAddressType,
       "alaRouteMapRedistRowStatus": alaRouteMapRedistRowStatus,
       "alaRouteMapAccessListNameTable": alaRouteMapAccessListNameTable,
       "alaRouteMapAccessListNameEntry": alaRouteMapAccessListNameEntry,
       "alaRouteMapAccessListName": alaRouteMapAccessListName,
       "alaRouteMapAccessListNameIndex": alaRouteMapAccessListNameIndex,
       "alaRouteMapAccessListNameAddressType": alaRouteMapAccessListNameAddressType,
       "alaRouteMapAccessListNameRowStatus": alaRouteMapAccessListNameRowStatus,
       "alaRouteMapAccessListTable": alaRouteMapAccessListTable,
       "alaRouteMapAccessListEntry": alaRouteMapAccessListEntry,
       "alaRouteMapAccessListIndex": alaRouteMapAccessListIndex,
       "alaRouteMapAccessListAddressType": alaRouteMapAccessListAddressType,
       "alaRouteMapAccessListAddress": alaRouteMapAccessListAddress,
       "alaRouteMapAccessListPrefixLength": alaRouteMapAccessListPrefixLength,
       "alaRouteMapAccessListRedistControl": alaRouteMapAccessListRedistControl,
       "alaRouteMapAccessListAction": alaRouteMapAccessListAction,
       "alaRouteMapAccessListRowStatus": alaRouteMapAccessListRowStatus,
       "alaRouteMapNameTable": alaRouteMapNameTable,
       "alaRouteMapNameEntry": alaRouteMapNameEntry,
       "alaRouteMapName": alaRouteMapName,
       "alaRouteMapNameIndex": alaRouteMapNameIndex,
       "alaRouteMapNameRowStatus": alaRouteMapNameRowStatus,
       "alaRouteMapSequenceTable": alaRouteMapSequenceTable,
       "alaRouteMapSequenceEntry": alaRouteMapSequenceEntry,
       "alaRouteMapSequenceIndex": alaRouteMapSequenceIndex,
       "alaRouteMapSequenceNumber": alaRouteMapSequenceNumber,
       "alaRouteMapSequenceAction": alaRouteMapSequenceAction,
       "alaRouteMapSequenceRowStatus": alaRouteMapSequenceRowStatus,
       "alaRouteMapTable": alaRouteMapTable,
       "alaRouteMapEntry": alaRouteMapEntry,
       "alaRouteMapIndex": alaRouteMapIndex,
       "alaRouteMapSequence": alaRouteMapSequence,
       "alaRouteMapType": alaRouteMapType,
       "alaRouteMapValue": alaRouteMapValue,
       "alaRouteMapRowStatus": alaRouteMapRowStatus,
       "alcatelIND1RouteMapMIBConformance": alcatelIND1RouteMapMIBConformance,
       "alcatelIND1RouteMapMIBCompliances": alcatelIND1RouteMapMIBCompliances,
       "alaRouteMapCompliance": alaRouteMapCompliance,
       "alcatelIND1RouteMapMIBGroups": alcatelIND1RouteMapMIBGroups,
       "alaRouteMapConfigMIBGroup": alaRouteMapConfigMIBGroup}
)
