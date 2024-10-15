# SNMP MIB module (ALCATEL-IND1-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:40 2024
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

(routingIND1Ospf,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ospf")

(ospfAreaAggregateEntry,
 ospfAreaEntry,
 ospfAreaId,
 ospfExtLsdbEntry,
 ospfIfEntry,
 ospfNbrEntry,
 ospfVirtIfEntry,
 ospfVirtNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAreaAggregateEntry",
    "ospfAreaEntry",
    "ospfAreaId",
    "ospfExtLsdbEntry",
    "ospfIfEntry",
    "ospfNbrEntry",
    "ospfVirtIfEntry",
    "ospfVirtNbrEntry")

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


# MODULE-IDENTITY

alcatelIND1OSPFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1)
)
alcatelIND1OSPFMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaAuthenticationEncryptKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OSPFMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBObjects = _AlcatelIND1OSPFMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBObjects.setStatus("current")
_AlaProtocolOspf_ObjectIdentity = ObjectIdentity
alaProtocolOspf = _AlaProtocolOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1)
)


class _AlaOspfRedistAdminStatus_Type(Integer32):
    """Custom type alaOspfRedistAdminStatus based on Integer32"""
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


_AlaOspfRedistAdminStatus_Type.__name__ = "Integer32"
_AlaOspfRedistAdminStatus_Object = MibScalar
alaOspfRedistAdminStatus = _AlaOspfRedistAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 1),
    _AlaOspfRedistAdminStatus_Type()
)
alaOspfRedistAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistAdminStatus.setStatus("deprecated")


class _AlaOspfRedistRouteTag_Type(Integer32):
    """Custom type alaOspfRedistRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRedistRouteTag_Type.__name__ = "Integer32"
_AlaOspfRedistRouteTag_Object = MibScalar
alaOspfRedistRouteTag = _AlaOspfRedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 2),
    _AlaOspfRedistRouteTag_Type()
)
alaOspfRedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteTag.setStatus("current")


class _AlaOspfTimerSpfDelay_Type(Integer32):
    """Custom type alaOspfTimerSpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfTimerSpfDelay_Type.__name__ = "Integer32"
_AlaOspfTimerSpfDelay_Object = MibScalar
alaOspfTimerSpfDelay = _AlaOspfTimerSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 3),
    _AlaOspfTimerSpfDelay_Type()
)
alaOspfTimerSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfTimerSpfDelay.setStatus("current")


class _AlaOspfTimerSpfHold_Type(Integer32):
    """Custom type alaOspfTimerSpfHold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfTimerSpfHold_Type.__name__ = "Integer32"
_AlaOspfTimerSpfHold_Object = MibScalar
alaOspfTimerSpfHold = _AlaOspfTimerSpfHold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 4),
    _AlaOspfTimerSpfHold_Type()
)
alaOspfTimerSpfHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfTimerSpfHold.setStatus("current")
_AlaOspfRouteNumber_Type = Counter32
_AlaOspfRouteNumber_Object = MibScalar
alaOspfRouteNumber = _AlaOspfRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 7),
    _AlaOspfRouteNumber_Type()
)
alaOspfRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteNumber.setStatus("current")


class _AlaOspfMTUCheck_Type(Integer32):
    """Custom type alaOspfMTUCheck based on Integer32"""
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


_AlaOspfMTUCheck_Type.__name__ = "Integer32"
_AlaOspfMTUCheck_Object = MibScalar
alaOspfMTUCheck = _AlaOspfMTUCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 8),
    _AlaOspfMTUCheck_Type()
)
alaOspfMTUCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfMTUCheck.setStatus("current")


class _AlaOspfAsBdrRtr_Type(Integer32):
    """Custom type alaOspfAsBdrRtr based on Integer32"""
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


_AlaOspfAsBdrRtr_Type.__name__ = "Integer32"
_AlaOspfAsBdrRtr_Object = MibScalar
alaOspfAsBdrRtr = _AlaOspfAsBdrRtr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 9),
    _AlaOspfAsBdrRtr_Type()
)
alaOspfAsBdrRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfAsBdrRtr.setStatus("deprecated")
_AlaOspfRedistProtoTable_Object = MibTable
alaOspfRedistProtoTable = _AlaOspfRedistProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaOspfRedistProtoTable.setStatus("deprecated")
_AlaOspfRedistProtoEntry_Object = MibTableRow
alaOspfRedistProtoEntry = _AlaOspfRedistProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1)
)
alaOspfRedistProtoEntry.setIndexNames(
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoId"),
)
if mibBuilder.loadTexts:
    alaOspfRedistProtoEntry.setStatus("deprecated")


class _AlaOspfRedistProtoId_Type(Integer32):
    """Custom type alaOspfRedistProtoId based on Integer32"""
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
              38,
              70,
              102,
              134,
              166,
              198,
              230)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("directHost", 4),
          ("isis", 7),
          ("local", 2),
          ("ospf", 6),
          ("ospf2", 38),
          ("ospf3", 70),
          ("ospf4", 102),
          ("ospf5", 134),
          ("ospf6", 166),
          ("ospf7", 198),
          ("ospf8", 230),
          ("other", 1),
          ("rip", 5),
          ("static", 3))
    )


_AlaOspfRedistProtoId_Type.__name__ = "Integer32"
_AlaOspfRedistProtoId_Object = MibTableColumn
alaOspfRedistProtoId = _AlaOspfRedistProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 1),
    _AlaOspfRedistProtoId_Type()
)
alaOspfRedistProtoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRedistProtoId.setStatus("deprecated")


class _AlaOspfRedistProtoSubnets_Type(Integer32):
    """Custom type alaOspfRedistProtoSubnets based on Integer32"""
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


_AlaOspfRedistProtoSubnets_Type.__name__ = "Integer32"
_AlaOspfRedistProtoSubnets_Object = MibTableColumn
alaOspfRedistProtoSubnets = _AlaOspfRedistProtoSubnets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 2),
    _AlaOspfRedistProtoSubnets_Type()
)
alaOspfRedistProtoSubnets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistProtoSubnets.setStatus("deprecated")


class _AlaOspfRedistProtoMetricType_Type(Integer32):
    """Custom type alaOspfRedistProtoMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_AlaOspfRedistProtoMetricType_Type.__name__ = "Integer32"
_AlaOspfRedistProtoMetricType_Object = MibTableColumn
alaOspfRedistProtoMetricType = _AlaOspfRedistProtoMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 3),
    _AlaOspfRedistProtoMetricType_Type()
)
alaOspfRedistProtoMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistProtoMetricType.setStatus("deprecated")


class _AlaOspfRedistProtoMetric_Type(Integer32):
    """Custom type alaOspfRedistProtoMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRedistProtoMetric_Type.__name__ = "Integer32"
_AlaOspfRedistProtoMetric_Object = MibTableColumn
alaOspfRedistProtoMetric = _AlaOspfRedistProtoMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 4),
    _AlaOspfRedistProtoMetric_Type()
)
alaOspfRedistProtoMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistProtoMetric.setStatus("deprecated")


class _AlaOspfRedistProtoStatus_Type(RowStatus):
    """Custom type alaOspfRedistProtoStatus based on RowStatus"""


_AlaOspfRedistProtoStatus_Object = MibTableColumn
alaOspfRedistProtoStatus = _AlaOspfRedistProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 5),
    _AlaOspfRedistProtoStatus_Type()
)
alaOspfRedistProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistProtoStatus.setStatus("deprecated")
_AlaOspfRedistProtoRouteTag_Type = Counter32
_AlaOspfRedistProtoRouteTag_Object = MibTableColumn
alaOspfRedistProtoRouteTag = _AlaOspfRedistProtoRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 10, 1, 6),
    _AlaOspfRedistProtoRouteTag_Type()
)
alaOspfRedistProtoRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRedistProtoRouteTag.setStatus("deprecated")
_AlaOspfRouteTable_Object = MibTable
alaOspfRouteTable = _AlaOspfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaOspfRouteTable.setStatus("current")
_AlaOspfRouteEntry_Object = MibTableRow
alaOspfRouteEntry = _AlaOspfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1)
)
alaOspfRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRouteDest"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRouteMask"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRouteTos"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaOspfRouteEntry.setStatus("current")


class _AlaOspfRouteDest_Type(IpAddress):
    """Custom type alaOspfRouteDest based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteDest_Object = MibTableColumn
alaOspfRouteDest = _AlaOspfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 1),
    _AlaOspfRouteDest_Type()
)
alaOspfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteDest.setStatus("current")


class _AlaOspfRouteMask_Type(IpAddress):
    """Custom type alaOspfRouteMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteMask_Object = MibTableColumn
alaOspfRouteMask = _AlaOspfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 2),
    _AlaOspfRouteMask_Type()
)
alaOspfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMask.setStatus("current")


class _AlaOspfRouteTos_Type(Integer32):
    """Custom type alaOspfRouteTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRouteTos_Type.__name__ = "Integer32"
_AlaOspfRouteTos_Object = MibTableColumn
alaOspfRouteTos = _AlaOspfRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 3),
    _AlaOspfRouteTos_Type()
)
alaOspfRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteTos.setStatus("current")


class _AlaOspfRouteNextHop_Type(IpAddress):
    """Custom type alaOspfRouteNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRouteNextHop_Object = MibTableColumn
alaOspfRouteNextHop = _AlaOspfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 4),
    _AlaOspfRouteNextHop_Type()
)
alaOspfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteNextHop.setStatus("current")


class _AlaOspfRouteIfIndex_Type(Integer32):
    """Custom type alaOspfRouteIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AlaOspfRouteIfIndex_Type.__name__ = "Integer32"
_AlaOspfRouteIfIndex_Object = MibTableColumn
alaOspfRouteIfIndex = _AlaOspfRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 5),
    _AlaOspfRouteIfIndex_Type()
)
alaOspfRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteIfIndex.setStatus("current")


class _AlaOspfRouteType_Type(Integer32):
    """Custom type alaOspfRouteType based on Integer32"""
    defaultValue = 1

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
        *(("externalType1", 3),
          ("externalType2", 4),
          ("interArea", 2),
          ("intraArea", 1),
          ("nssaExternalType1", 5),
          ("nssaExternalType2", 6))
    )


_AlaOspfRouteType_Type.__name__ = "Integer32"
_AlaOspfRouteType_Object = MibTableColumn
alaOspfRouteType = _AlaOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 6),
    _AlaOspfRouteType_Type()
)
alaOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteType.setStatus("current")


class _AlaOspfRouteAge_Type(TimeTicks):
    """Custom type alaOspfRouteAge based on TimeTicks"""
    defaultValue = 0


_AlaOspfRouteAge_Object = MibTableColumn
alaOspfRouteAge = _AlaOspfRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 7),
    _AlaOspfRouteAge_Type()
)
alaOspfRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteAge.setStatus("current")


class _AlaOspfRouteTag_Type(Integer32):
    """Custom type alaOspfRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRouteTag_Type.__name__ = "Integer32"
_AlaOspfRouteTag_Object = MibTableColumn
alaOspfRouteTag = _AlaOspfRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 8),
    _AlaOspfRouteTag_Type()
)
alaOspfRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteTag.setStatus("current")


class _AlaOspfRouteMetric1_Type(Integer32):
    """Custom type alaOspfRouteMetric1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRouteMetric1_Type.__name__ = "Integer32"
_AlaOspfRouteMetric1_Object = MibTableColumn
alaOspfRouteMetric1 = _AlaOspfRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 9),
    _AlaOspfRouteMetric1_Type()
)
alaOspfRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMetric1.setStatus("current")


class _AlaOspfRouteMetric2_Type(Integer32):
    """Custom type alaOspfRouteMetric2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRouteMetric2_Type.__name__ = "Integer32"
_AlaOspfRouteMetric2_Object = MibTableColumn
alaOspfRouteMetric2 = _AlaOspfRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 10),
    _AlaOspfRouteMetric2_Type()
)
alaOspfRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteMetric2.setStatus("current")


class _AlaOspfRouteStatus_Type(RowStatus):
    """Custom type alaOspfRouteStatus based on RowStatus"""


_AlaOspfRouteStatus_Object = MibTableColumn
alaOspfRouteStatus = _AlaOspfRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 12, 1, 11),
    _AlaOspfRouteStatus_Type()
)
alaOspfRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRouteStatus.setStatus("current")
_AlaOspfBdrRouterTable_Object = MibTable
alaOspfBdrRouterTable = _AlaOspfBdrRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterTable.setStatus("current")
_AlaOspfBdrRouterEntry_Object = MibTableRow
alaOspfBdrRouterEntry = _AlaOspfBdrRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1)
)
alaOspfBdrRouterEntry.setIndexNames(
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterAreaId"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterId"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterTos"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterNextHop"),
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterEntry.setStatus("current")


class _AlaOspfBdrRouterAreaId_Type(IpAddress):
    """Custom type alaOspfBdrRouterAreaId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterAreaId_Object = MibTableColumn
alaOspfBdrRouterAreaId = _AlaOspfBdrRouterAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 1),
    _AlaOspfBdrRouterAreaId_Type()
)
alaOspfBdrRouterAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterAreaId.setStatus("current")


class _AlaOspfBdrRouterId_Type(IpAddress):
    """Custom type alaOspfBdrRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterId_Object = MibTableColumn
alaOspfBdrRouterId = _AlaOspfBdrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 2),
    _AlaOspfBdrRouterId_Type()
)
alaOspfBdrRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterId.setStatus("current")


class _AlaOspfBdrRouterTos_Type(Integer32):
    """Custom type alaOspfBdrRouterTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfBdrRouterTos_Type.__name__ = "Integer32"
_AlaOspfBdrRouterTos_Object = MibTableColumn
alaOspfBdrRouterTos = _AlaOspfBdrRouterTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 3),
    _AlaOspfBdrRouterTos_Type()
)
alaOspfBdrRouterTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterTos.setStatus("current")


class _AlaOspfBdrRouterNextHop_Type(IpAddress):
    """Custom type alaOspfBdrRouterNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfBdrRouterNextHop_Object = MibTableColumn
alaOspfBdrRouterNextHop = _AlaOspfBdrRouterNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 4),
    _AlaOspfBdrRouterNextHop_Type()
)
alaOspfBdrRouterNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterNextHop.setStatus("current")


class _AlaOspfBdrRouterIfIndex_Type(Integer32):
    """Custom type alaOspfBdrRouterIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfBdrRouterIfIndex_Type.__name__ = "Integer32"
_AlaOspfBdrRouterIfIndex_Object = MibTableColumn
alaOspfBdrRouterIfIndex = _AlaOspfBdrRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 5),
    _AlaOspfBdrRouterIfIndex_Type()
)
alaOspfBdrRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterIfIndex.setStatus("current")


class _AlaOspfBdrRouterType_Type(Integer32):
    """Custom type alaOspfBdrRouterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("abrAsbr", 3),
          ("asbr", 2))
    )


_AlaOspfBdrRouterType_Type.__name__ = "Integer32"
_AlaOspfBdrRouterType_Object = MibTableColumn
alaOspfBdrRouterType = _AlaOspfBdrRouterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 6),
    _AlaOspfBdrRouterType_Type()
)
alaOspfBdrRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterType.setStatus("current")


class _AlaOspfBdrRouterAge_Type(TimeTicks):
    """Custom type alaOspfBdrRouterAge based on TimeTicks"""
    defaultValue = 0


_AlaOspfBdrRouterAge_Object = MibTableColumn
alaOspfBdrRouterAge = _AlaOspfBdrRouterAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 7),
    _AlaOspfBdrRouterAge_Type()
)
alaOspfBdrRouterAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterAge.setStatus("current")


class _AlaOspfBdrRouterMetric_Type(Integer32):
    """Custom type alaOspfBdrRouterMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfBdrRouterMetric_Type.__name__ = "Integer32"
_AlaOspfBdrRouterMetric_Object = MibTableColumn
alaOspfBdrRouterMetric = _AlaOspfBdrRouterMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 8),
    _AlaOspfBdrRouterMetric_Type()
)
alaOspfBdrRouterMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterMetric.setStatus("current")


class _AlaOspfBdrRouterStatus_Type(RowStatus):
    """Custom type alaOspfBdrRouterStatus based on RowStatus"""


_AlaOspfBdrRouterStatus_Object = MibTableColumn
alaOspfBdrRouterStatus = _AlaOspfBdrRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 13, 1, 9),
    _AlaOspfBdrRouterStatus_Type()
)
alaOspfBdrRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfBdrRouterStatus.setStatus("current")
_AlaOspfRedistRouteTable_Object = MibTable
alaOspfRedistRouteTable = _AlaOspfRedistRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaOspfRedistRouteTable.setStatus("deprecated")
_AlaOspfRedistRouteEntry_Object = MibTableRow
alaOspfRedistRouteEntry = _AlaOspfRedistRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1)
)
alaOspfRedistRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteProto"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteDest"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteMask"),
)
if mibBuilder.loadTexts:
    alaOspfRedistRouteEntry.setStatus("deprecated")


class _AlaOspfRedistRouteProto_Type(Integer32):
    """Custom type alaOspfRedistRouteProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("directHost", 4),
          ("isis", 7),
          ("local", 2),
          ("other", 1),
          ("rip", 5),
          ("static", 3))
    )


_AlaOspfRedistRouteProto_Type.__name__ = "Integer32"
_AlaOspfRedistRouteProto_Object = MibTableColumn
alaOspfRedistRouteProto = _AlaOspfRedistRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 1),
    _AlaOspfRedistRouteProto_Type()
)
alaOspfRedistRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteProto.setStatus("deprecated")


class _AlaOspfRedistRouteDest_Type(IpAddress):
    """Custom type alaOspfRedistRouteDest based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRedistRouteDest_Object = MibTableColumn
alaOspfRedistRouteDest = _AlaOspfRedistRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 2),
    _AlaOspfRedistRouteDest_Type()
)
alaOspfRedistRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRedistRouteDest.setStatus("deprecated")


class _AlaOspfRedistRouteMask_Type(IpAddress):
    """Custom type alaOspfRedistRouteMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfRedistRouteMask_Object = MibTableColumn
alaOspfRedistRouteMask = _AlaOspfRedistRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 3),
    _AlaOspfRedistRouteMask_Type()
)
alaOspfRedistRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRedistRouteMask.setStatus("deprecated")


class _AlaOspfRedistRouteMetric_Type(Integer32):
    """Custom type alaOspfRedistRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfRedistRouteMetric_Type.__name__ = "Integer32"
_AlaOspfRedistRouteMetric_Object = MibTableColumn
alaOspfRedistRouteMetric = _AlaOspfRedistRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 4),
    _AlaOspfRedistRouteMetric_Type()
)
alaOspfRedistRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteMetric.setStatus("deprecated")


class _AlaOspfRedistRouteControl_Type(Integer32):
    """Custom type alaOspfRedistRouteControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("redistributeAllSubnets", 1),
          ("redistributeAsAggregate", 2),
          ("redistributeExactMatch", 3))
    )


_AlaOspfRedistRouteControl_Type.__name__ = "Integer32"
_AlaOspfRedistRouteControl_Object = MibTableColumn
alaOspfRedistRouteControl = _AlaOspfRedistRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 5),
    _AlaOspfRedistRouteControl_Type()
)
alaOspfRedistRouteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteControl.setStatus("deprecated")


class _AlaOspfRedistRouteTagMatch_Type(Integer32):
    """Custom type alaOspfRedistRouteTagMatch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfRedistRouteTagMatch_Type.__name__ = "Integer32"
_AlaOspfRedistRouteTagMatch_Object = MibTableColumn
alaOspfRedistRouteTagMatch = _AlaOspfRedistRouteTagMatch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 6),
    _AlaOspfRedistRouteTagMatch_Type()
)
alaOspfRedistRouteTagMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteTagMatch.setStatus("deprecated")


class _AlaOspfRedistRouteEffect_Type(Integer32):
    """Custom type alaOspfRedistRouteEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotRedistribute", 2),
          ("redistribute", 1))
    )


_AlaOspfRedistRouteEffect_Type.__name__ = "Integer32"
_AlaOspfRedistRouteEffect_Object = MibTableColumn
alaOspfRedistRouteEffect = _AlaOspfRedistRouteEffect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 7),
    _AlaOspfRedistRouteEffect_Type()
)
alaOspfRedistRouteEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteEffect.setStatus("deprecated")


class _AlaOspfRedistRouteStatus_Type(RowStatus):
    """Custom type alaOspfRedistRouteStatus based on RowStatus"""


_AlaOspfRedistRouteStatus_Object = MibTableColumn
alaOspfRedistRouteStatus = _AlaOspfRedistRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 14, 1, 8),
    _AlaOspfRedistRouteStatus_Type()
)
alaOspfRedistRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRedistRouteStatus.setStatus("deprecated")
_AlaOspfIfMd5Table_Object = MibTable
alaOspfIfMd5Table = _AlaOspfIfMd5Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Table.setStatus("current")
_AlaOspfIfMd5Entry_Object = MibTableRow
alaOspfIfMd5Entry = _AlaOspfIfMd5Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1)
)
alaOspfIfMd5Entry.setIndexNames(
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5IpAddress"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyId"),
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Entry.setStatus("current")


class _AlaOspfIfMd5IpAddress_Type(IpAddress):
    """Custom type alaOspfIfMd5IpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaOspfIfMd5IpAddress_Object = MibTableColumn
alaOspfIfMd5IpAddress = _AlaOspfIfMd5IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 1),
    _AlaOspfIfMd5IpAddress_Type()
)
alaOspfIfMd5IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMd5IpAddress.setStatus("current")


class _AlaOspfIfMd5KeyId_Type(Integer32):
    """Custom type alaOspfIfMd5KeyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaOspfIfMd5KeyId_Type.__name__ = "Integer32"
_AlaOspfIfMd5KeyId_Object = MibTableColumn
alaOspfIfMd5KeyId = _AlaOspfIfMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 2),
    _AlaOspfIfMd5KeyId_Type()
)
alaOspfIfMd5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyId.setStatus("current")


class _AlaOspfIfMd5Key_Type(OctetString):
    """Custom type alaOspfIfMd5Key based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlaOspfIfMd5Key_Type.__name__ = "OctetString"
_AlaOspfIfMd5Key_Object = MibTableColumn
alaOspfIfMd5Key = _AlaOspfIfMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 3),
    _AlaOspfIfMd5Key_Type()
)
alaOspfIfMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5Key.setStatus("current")


class _AlaOspfIfMd5KeyStartAccept_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStartAccept based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStartAccept_Object = MibTableColumn
alaOspfIfMd5KeyStartAccept = _AlaOspfIfMd5KeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 4),
    _AlaOspfIfMd5KeyStartAccept_Type()
)
alaOspfIfMd5KeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStartAccept.setStatus("current")


class _AlaOspfIfMd5KeyStopAccept_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStopAccept based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStopAccept_Object = MibTableColumn
alaOspfIfMd5KeyStopAccept = _AlaOspfIfMd5KeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 5),
    _AlaOspfIfMd5KeyStopAccept_Type()
)
alaOspfIfMd5KeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStopAccept.setStatus("current")


class _AlaOspfIfMd5KeyStartGenerate_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStartGenerate based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStartGenerate_Object = MibTableColumn
alaOspfIfMd5KeyStartGenerate = _AlaOspfIfMd5KeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 6),
    _AlaOspfIfMd5KeyStartGenerate_Type()
)
alaOspfIfMd5KeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStartGenerate.setStatus("current")


class _AlaOspfIfMd5KeyStopGenerate_Type(TimeTicks):
    """Custom type alaOspfIfMd5KeyStopGenerate based on TimeTicks"""
    defaultValue = 0


_AlaOspfIfMd5KeyStopGenerate_Object = MibTableColumn
alaOspfIfMd5KeyStopGenerate = _AlaOspfIfMd5KeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 7),
    _AlaOspfIfMd5KeyStopGenerate_Type()
)
alaOspfIfMd5KeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5KeyStopGenerate.setStatus("current")


class _AlaOspfIfMd5RowStatus_Type(RowStatus):
    """Custom type alaOspfIfMd5RowStatus based on RowStatus"""


_AlaOspfIfMd5RowStatus_Object = MibTableColumn
alaOspfIfMd5RowStatus = _AlaOspfIfMd5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 8),
    _AlaOspfIfMd5RowStatus_Type()
)
alaOspfIfMd5RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5RowStatus.setStatus("current")


class _AlaOspfIfMd5EncryptKey_Type(AlaAuthenticationEncryptKey):
    """Custom type alaOspfIfMd5EncryptKey based on AlaAuthenticationEncryptKey"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaOspfIfMd5EncryptKey_Object = MibTableColumn
alaOspfIfMd5EncryptKey = _AlaOspfIfMd5EncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 16, 1, 9),
    _AlaOspfIfMd5EncryptKey_Type()
)
alaOspfIfMd5EncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfIfMd5EncryptKey.setStatus("current")
_AlaOspfIfAugTable_Object = MibTable
alaOspfIfAugTable = _AlaOspfIfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaOspfIfAugTable.setStatus("current")
_AlaOspfIfAugEntry_Object = MibTableRow
alaOspfIfAugEntry = _AlaOspfIfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    alaOspfIfAugEntry.setStatus("current")
_AlaOspfIfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaOspfIfEncryptKey_Object = MibTableColumn
alaOspfIfEncryptKey = _AlaOspfIfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 1),
    _AlaOspfIfEncryptKey_Type()
)
alaOspfIfEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfEncryptKey.setStatus("current")
_AlaOspfIfIpMask_Type = IpAddress
_AlaOspfIfIpMask_Object = MibTableColumn
alaOspfIfIpMask = _AlaOspfIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 2),
    _AlaOspfIfIpMask_Type()
)
alaOspfIfIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfIpMask.setStatus("current")


class _AlaOspfIfVlanId_Type(Integer32):
    """Custom type alaOspfIfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_AlaOspfIfVlanId_Type.__name__ = "Integer32"
_AlaOspfIfVlanId_Object = MibTableColumn
alaOspfIfVlanId = _AlaOspfIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 3),
    _AlaOspfIfVlanId_Type()
)
alaOspfIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfVlanId.setStatus("current")
_AlaOspfIfDrRouterid_Type = IpAddress
_AlaOspfIfDrRouterid_Object = MibTableColumn
alaOspfIfDrRouterid = _AlaOspfIfDrRouterid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 4),
    _AlaOspfIfDrRouterid_Type()
)
alaOspfIfDrRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfDrRouterid.setStatus("current")
_AlaOspfIfBdrRouterid_Type = IpAddress
_AlaOspfIfBdrRouterid_Object = MibTableColumn
alaOspfIfBdrRouterid = _AlaOspfIfBdrRouterid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 5),
    _AlaOspfIfBdrRouterid_Type()
)
alaOspfIfBdrRouterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfBdrRouterid.setStatus("current")
_AlaOspfIfMTU_Type = Counter32
_AlaOspfIfMTU_Object = MibTableColumn
alaOspfIfMTU = _AlaOspfIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 6),
    _AlaOspfIfMTU_Type()
)
alaOspfIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfMTU.setStatus("current")
_AlaOspfIfInitNbrs_Type = Counter32
_AlaOspfIfInitNbrs_Object = MibTableColumn
alaOspfIfInitNbrs = _AlaOspfIfInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 7),
    _AlaOspfIfInitNbrs_Type()
)
alaOspfIfInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfInitNbrs.setStatus("current")
_AlaOspfIfExchNbrs_Type = Counter32
_AlaOspfIfExchNbrs_Object = MibTableColumn
alaOspfIfExchNbrs = _AlaOspfIfExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 8),
    _AlaOspfIfExchNbrs_Type()
)
alaOspfIfExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfExchNbrs.setStatus("current")
_AlaOspfIfFullNbrs_Type = Counter32
_AlaOspfIfFullNbrs_Object = MibTableColumn
alaOspfIfFullNbrs = _AlaOspfIfFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 9),
    _AlaOspfIfFullNbrs_Type()
)
alaOspfIfFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfFullNbrs.setStatus("current")


class _AlaOspfIfLinkType_Type(Integer32):
    """Custom type alaOspfIfLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("broadcast", 1)
    )


_AlaOspfIfLinkType_Type.__name__ = "Integer32"
_AlaOspfIfLinkType_Object = MibTableColumn
alaOspfIfLinkType = _AlaOspfIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 10),
    _AlaOspfIfLinkType_Type()
)
alaOspfIfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfLinkType.setStatus("current")


class _AlaOspfIfOperStatus_Type(Integer32):
    """Custom type alaOspfIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AlaOspfIfOperStatus_Type.__name__ = "Integer32"
_AlaOspfIfOperStatus_Object = MibTableColumn
alaOspfIfOperStatus = _AlaOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 11),
    _AlaOspfIfOperStatus_Type()
)
alaOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfOperStatus.setStatus("current")
_AlaOspfIfIntfName_Type = DisplayString
_AlaOspfIfIntfName_Object = MibTableColumn
alaOspfIfIntfName = _AlaOspfIfIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 12),
    _AlaOspfIfIntfName_Type()
)
alaOspfIfIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfIntfName.setStatus("current")
_AlaOspfIf2WayNbrs_Type = Counter32
_AlaOspfIf2WayNbrs_Object = MibTableColumn
alaOspfIf2WayNbrs = _AlaOspfIf2WayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 13),
    _AlaOspfIf2WayNbrs_Type()
)
alaOspfIf2WayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIf2WayNbrs.setStatus("current")


class _AlaOspfIfBfdStatus_Type(Integer32):
    """Custom type alaOspfIfBfdStatus based on Integer32"""
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


_AlaOspfIfBfdStatus_Type.__name__ = "Integer32"
_AlaOspfIfBfdStatus_Object = MibTableColumn
alaOspfIfBfdStatus = _AlaOspfIfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 14),
    _AlaOspfIfBfdStatus_Type()
)
alaOspfIfBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfBfdStatus.setStatus("current")


class _AlaOspfIfBfdDrsOnly_Type(Integer32):
    """Custom type alaOspfIfBfdDrsOnly based on Integer32"""
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


_AlaOspfIfBfdDrsOnly_Type.__name__ = "Integer32"
_AlaOspfIfBfdDrsOnly_Object = MibTableColumn
alaOspfIfBfdDrsOnly = _AlaOspfIfBfdDrsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 17, 1, 15),
    _AlaOspfIfBfdDrsOnly_Type()
)
alaOspfIfBfdDrsOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfIfBfdDrsOnly.setStatus("current")
_AlaOspfVirtIfAugTable_Object = MibTable
alaOspfVirtIfAugTable = _AlaOspfVirtIfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaOspfVirtIfAugTable.setStatus("current")
_AlaOspfVirtIfAugEntry_Object = MibTableRow
alaOspfVirtIfAugEntry = _AlaOspfVirtIfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    alaOspfVirtIfAugEntry.setStatus("current")
_AlaOspfVirtIfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaOspfVirtIfEncryptKey_Object = MibTableColumn
alaOspfVirtIfEncryptKey = _AlaOspfVirtIfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1, 1),
    _AlaOspfVirtIfEncryptKey_Type()
)
alaOspfVirtIfEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOspfVirtIfEncryptKey.setStatus("current")


class _AlaOspfVirtIfOperStatus_Type(Integer32):
    """Custom type alaOspfVirtIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AlaOspfVirtIfOperStatus_Type.__name__ = "Integer32"
_AlaOspfVirtIfOperStatus_Object = MibTableColumn
alaOspfVirtIfOperStatus = _AlaOspfVirtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 18, 1, 2),
    _AlaOspfVirtIfOperStatus_Type()
)
alaOspfVirtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtIfOperStatus.setStatus("current")


class _AlaOspfRestartHelperSupport_Type(Integer32):
    """Custom type alaOspfRestartHelperSupport based on Integer32"""
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


_AlaOspfRestartHelperSupport_Type.__name__ = "Integer32"
_AlaOspfRestartHelperSupport_Object = MibScalar
alaOspfRestartHelperSupport = _AlaOspfRestartHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 19),
    _AlaOspfRestartHelperSupport_Type()
)
alaOspfRestartHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartHelperSupport.setStatus("current")


class _AlaOspfRestartHelperStrictLSAChecking_Type(Integer32):
    """Custom type alaOspfRestartHelperStrictLSAChecking based on Integer32"""
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


_AlaOspfRestartHelperStrictLSAChecking_Type.__name__ = "Integer32"
_AlaOspfRestartHelperStrictLSAChecking_Object = MibScalar
alaOspfRestartHelperStrictLSAChecking = _AlaOspfRestartHelperStrictLSAChecking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 20),
    _AlaOspfRestartHelperStrictLSAChecking_Type()
)
alaOspfRestartHelperStrictLSAChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartHelperStrictLSAChecking.setStatus("current")


class _AlaOspfRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 1),
          ("notHelping", 2))
    )


_AlaOspfRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfRestartHelperStatus_Object = MibScalar
alaOspfRestartHelperStatus = _AlaOspfRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 21),
    _AlaOspfRestartHelperStatus_Type()
)
alaOspfRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartHelperStatus.setStatus("current")
_AlaOspfRFC1583Compatibility_Type = TruthValue
_AlaOspfRFC1583Compatibility_Object = MibScalar
alaOspfRFC1583Compatibility = _AlaOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 22),
    _AlaOspfRFC1583Compatibility_Type()
)
alaOspfRFC1583Compatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRFC1583Compatibility.setStatus("current")
_AlaOspfOpaqueLsaSupport_Type = TruthValue
_AlaOspfOpaqueLsaSupport_Object = MibScalar
alaOspfOpaqueLsaSupport = _AlaOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 23),
    _AlaOspfOpaqueLsaSupport_Type()
)
alaOspfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfOpaqueLsaSupport.setStatus("current")
_AlaOspfTrafficEngineeringSupport_Type = TruthValue
_AlaOspfTrafficEngineeringSupport_Object = MibScalar
alaOspfTrafficEngineeringSupport = _AlaOspfTrafficEngineeringSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 24),
    _AlaOspfTrafficEngineeringSupport_Type()
)
alaOspfTrafficEngineeringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTrafficEngineeringSupport.setStatus("current")
_AlaOspfReferenceBandwidth_Type = Unsigned32
_AlaOspfReferenceBandwidth_Object = MibScalar
alaOspfReferenceBandwidth = _AlaOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 25),
    _AlaOspfReferenceBandwidth_Type()
)
alaOspfReferenceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfReferenceBandwidth.setStatus("current")


class _AlaOspfRestartSupport_Type(Integer32):
    """Custom type alaOspfRestartSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedAndUnplanned", 3),
          ("plannedOnly", 2))
    )


_AlaOspfRestartSupport_Type.__name__ = "Integer32"
_AlaOspfRestartSupport_Object = MibScalar
alaOspfRestartSupport = _AlaOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 26),
    _AlaOspfRestartSupport_Type()
)
alaOspfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartSupport.setStatus("current")


class _AlaOspfRestartInterval_Type(Integer32):
    """Custom type alaOspfRestartInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_AlaOspfRestartInterval_Type.__name__ = "Integer32"
_AlaOspfRestartInterval_Object = MibScalar
alaOspfRestartInterval = _AlaOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 27),
    _AlaOspfRestartInterval_Type()
)
alaOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaOspfRestartInterval.setUnits("seconds")


class _AlaOspfRestartStatus_Type(Integer32):
    """Custom type alaOspfRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_AlaOspfRestartStatus_Type.__name__ = "Integer32"
_AlaOspfRestartStatus_Object = MibScalar
alaOspfRestartStatus = _AlaOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 28),
    _AlaOspfRestartStatus_Type()
)
alaOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartStatus.setStatus("current")
_AlaOspfRestartAge_Type = Unsigned32
_AlaOspfRestartAge_Object = MibScalar
alaOspfRestartAge = _AlaOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 29),
    _AlaOspfRestartAge_Type()
)
alaOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    alaOspfRestartAge.setUnits("seconds")


class _AlaOspfRestartExitReason_Type(Integer32):
    """Custom type alaOspfRestartExitReason based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfRestartExitReason_Type.__name__ = "Integer32"
_AlaOspfRestartExitReason_Object = MibScalar
alaOspfRestartExitReason = _AlaOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 30),
    _AlaOspfRestartExitReason_Type()
)
alaOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfRestartExitReason.setStatus("current")
_AlaOspfNbrAugTable_Object = MibTable
alaOspfNbrAugTable = _AlaOspfNbrAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31)
)
if mibBuilder.loadTexts:
    alaOspfNbrAugTable.setStatus("current")
_AlaOspfNbrAugEntry_Object = MibTableRow
alaOspfNbrAugEntry = _AlaOspfNbrAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    alaOspfNbrAugEntry.setStatus("current")


class _AlaOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 2),
          ("notHelping", 1))
    )


_AlaOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfNbrRestartHelperStatus_Object = MibTableColumn
alaOspfNbrRestartHelperStatus = _AlaOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 1),
    _AlaOspfNbrRestartHelperStatus_Type()
)
alaOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperStatus.setStatus("current")
_AlaOspfNbrRestartHelperAge_Type = Unsigned32
_AlaOspfNbrRestartHelperAge_Object = MibTableColumn
alaOspfNbrRestartHelperAge = _AlaOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 2),
    _AlaOspfNbrRestartHelperAge_Type()
)
alaOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperAge.setUnits("seconds")


class _AlaOspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type alaOspfNbrRestartHelperExitReason based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AlaOspfNbrRestartHelperExitReason_Object = MibTableColumn
alaOspfNbrRestartHelperExitReason = _AlaOspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 3),
    _AlaOspfNbrRestartHelperExitReason_Type()
)
alaOspfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrRestartHelperExitReason.setStatus("current")
_AlaOspfNbrAreaId_Type = IpAddress
_AlaOspfNbrAreaId_Object = MibTableColumn
alaOspfNbrAreaId = _AlaOspfNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 4),
    _AlaOspfNbrAreaId_Type()
)
alaOspfNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrAreaId.setStatus("current")
_AlaOspfNbrDrAddress_Type = IpAddress
_AlaOspfNbrDrAddress_Object = MibTableColumn
alaOspfNbrDrAddress = _AlaOspfNbrDrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 5),
    _AlaOspfNbrDrAddress_Type()
)
alaOspfNbrDrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrDrAddress.setStatus("current")
_AlaOspfNbrBdrAddress_Type = IpAddress
_AlaOspfNbrBdrAddress_Object = MibTableColumn
alaOspfNbrBdrAddress = _AlaOspfNbrBdrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 6),
    _AlaOspfNbrBdrAddress_Type()
)
alaOspfNbrBdrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrBdrAddress.setStatus("current")


class _AlaOspfNbrType_Type(Integer32):
    """Custom type alaOspfNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AlaOspfNbrType_Type.__name__ = "Integer32"
_AlaOspfNbrType_Object = MibTableColumn
alaOspfNbrType = _AlaOspfNbrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 7),
    _AlaOspfNbrType_Type()
)
alaOspfNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrType.setStatus("current")


class _AlaOspfNbrMode_Type(Integer32):
    """Custom type alaOspfNbrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1),
          ("slaveHold", 3))
    )


_AlaOspfNbrMode_Type.__name__ = "Integer32"
_AlaOspfNbrMode_Object = MibTableColumn
alaOspfNbrMode = _AlaOspfNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 8),
    _AlaOspfNbrMode_Type()
)
alaOspfNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrMode.setStatus("current")
_AlaOspfNbrMd5SeqNo_Type = Counter32
_AlaOspfNbrMd5SeqNo_Object = MibTableColumn
alaOspfNbrMd5SeqNo = _AlaOspfNbrMd5SeqNo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 9),
    _AlaOspfNbrMd5SeqNo_Type()
)
alaOspfNbrMd5SeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrMd5SeqNo.setStatus("current")
_AlaOspfNbrLastHello_Type = Counter32
_AlaOspfNbrLastHello_Object = MibTableColumn
alaOspfNbrLastHello = _AlaOspfNbrLastHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 10),
    _AlaOspfNbrLastHello_Type()
)
alaOspfNbrLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrLastHello.setStatus("current")
_AlaOspfNbrPendingLSreq_Type = Counter32
_AlaOspfNbrPendingLSreq_Object = MibTableColumn
alaOspfNbrPendingLSreq = _AlaOspfNbrPendingLSreq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 11),
    _AlaOspfNbrPendingLSreq_Type()
)
alaOspfNbrPendingLSreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSreq.setStatus("current")
_AlaOspfNbrPendingLSack_Type = Counter32
_AlaOspfNbrPendingLSack_Object = MibTableColumn
alaOspfNbrPendingLSack = _AlaOspfNbrPendingLSack_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 12),
    _AlaOspfNbrPendingLSack_Type()
)
alaOspfNbrPendingLSack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSack.setStatus("current")
_AlaOspfNbrPendingLSupd_Type = Counter32
_AlaOspfNbrPendingLSupd_Object = MibTableColumn
alaOspfNbrPendingLSupd = _AlaOspfNbrPendingLSupd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 31, 1, 13),
    _AlaOspfNbrPendingLSupd_Type()
)
alaOspfNbrPendingLSupd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfNbrPendingLSupd.setStatus("current")
_AlaOspfVirtNbrAugTable_Object = MibTable
alaOspfVirtNbrAugTable = _AlaOspfVirtNbrAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32)
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugTable.setStatus("current")
_AlaOspfVirtNbrAugEntry_Object = MibTableRow
alaOspfVirtNbrAugEntry = _AlaOspfVirtNbrAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugEntry.setStatus("current")


class _AlaOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type alaOspfVirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 2),
          ("notHelping", 1))
    )


_AlaOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_AlaOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
alaOspfVirtNbrRestartHelperStatus = _AlaOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 1),
    _AlaOspfVirtNbrRestartHelperStatus_Type()
)
alaOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperStatus.setStatus("current")
_AlaOspfVirtNbrRestartHelperAge_Type = Unsigned32
_AlaOspfVirtNbrRestartHelperAge_Object = MibTableColumn
alaOspfVirtNbrRestartHelperAge = _AlaOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 2),
    _AlaOspfVirtNbrRestartHelperAge_Type()
)
alaOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _AlaOspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type alaOspfVirtNbrRestartHelperExitReason based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AlaOspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AlaOspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
alaOspfVirtNbrRestartHelperExitReason = _AlaOspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 3),
    _AlaOspfVirtNbrRestartHelperExitReason_Type()
)
alaOspfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrRestartHelperExitReason.setStatus("current")
_AlaOspfVirtNbrDrAddr_Type = IpAddress
_AlaOspfVirtNbrDrAddr_Object = MibTableColumn
alaOspfVirtNbrDrAddr = _AlaOspfVirtNbrDrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 4),
    _AlaOspfVirtNbrDrAddr_Type()
)
alaOspfVirtNbrDrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrDrAddr.setStatus("current")
_AlaOspfVirtNbrBdrAddr_Type = IpAddress
_AlaOspfVirtNbrBdrAddr_Object = MibTableColumn
alaOspfVirtNbrBdrAddr = _AlaOspfVirtNbrBdrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 5),
    _AlaOspfVirtNbrBdrAddr_Type()
)
alaOspfVirtNbrBdrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrBdrAddr.setStatus("current")


class _AlaOspfVirtNbrMode_Type(Integer32):
    """Custom type alaOspfVirtNbrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1),
          ("slaveHold", 3))
    )


_AlaOspfVirtNbrMode_Type.__name__ = "Integer32"
_AlaOspfVirtNbrMode_Object = MibTableColumn
alaOspfVirtNbrMode = _AlaOspfVirtNbrMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 6),
    _AlaOspfVirtNbrMode_Type()
)
alaOspfVirtNbrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrMode.setStatus("current")
_AlaOspfVirtNbrMd5SeqNo_Type = Counter32
_AlaOspfVirtNbrMd5SeqNo_Object = MibTableColumn
alaOspfVirtNbrMd5SeqNo = _AlaOspfVirtNbrMd5SeqNo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 7),
    _AlaOspfVirtNbrMd5SeqNo_Type()
)
alaOspfVirtNbrMd5SeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrMd5SeqNo.setStatus("current")
_AlaOspfVirtNbrLastHello_Type = Counter32
_AlaOspfVirtNbrLastHello_Object = MibTableColumn
alaOspfVirtNbrLastHello = _AlaOspfVirtNbrLastHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 8),
    _AlaOspfVirtNbrLastHello_Type()
)
alaOspfVirtNbrLastHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrLastHello.setStatus("current")
_AlaOspfVirtNbrPendingLSreq_Type = Counter32
_AlaOspfVirtNbrPendingLSreq_Object = MibTableColumn
alaOspfVirtNbrPendingLSreq = _AlaOspfVirtNbrPendingLSreq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 9),
    _AlaOspfVirtNbrPendingLSreq_Type()
)
alaOspfVirtNbrPendingLSreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSreq.setStatus("current")
_AlaOspfVirtNbrPendingLSack_Type = Counter32
_AlaOspfVirtNbrPendingLSack_Object = MibTableColumn
alaOspfVirtNbrPendingLSack = _AlaOspfVirtNbrPendingLSack_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 10),
    _AlaOspfVirtNbrPendingLSack_Type()
)
alaOspfVirtNbrPendingLSack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSack.setStatus("current")
_AlaOspfVirtNbrPendingLSupd_Type = Counter32
_AlaOspfVirtNbrPendingLSupd_Object = MibTableColumn
alaOspfVirtNbrPendingLSupd = _AlaOspfVirtNbrPendingLSupd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 32, 1, 11),
    _AlaOspfVirtNbrPendingLSupd_Type()
)
alaOspfVirtNbrPendingLSupd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfVirtNbrPendingLSupd.setStatus("current")


class _AlaOspfRestartInitiate_Type(Integer32):
    """Custom type alaOspfRestartInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2))
    )


_AlaOspfRestartInitiate_Type.__name__ = "Integer32"
_AlaOspfRestartInitiate_Object = MibScalar
alaOspfRestartInitiate = _AlaOspfRestartInitiate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 33),
    _AlaOspfRestartInitiate_Type()
)
alaOspfRestartInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfRestartInitiate.setStatus("current")
_AlaOspfAreaAugTable_Object = MibTable
alaOspfAreaAugTable = _AlaOspfAreaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35)
)
if mibBuilder.loadTexts:
    alaOspfAreaAugTable.setStatus("current")
_AlaOspfAreaAugEntry_Object = MibTableRow
alaOspfAreaAugEntry = _AlaOspfAreaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    alaOspfAreaAugEntry.setStatus("current")


class _AlaOspfAreaOperStatus_Type(Integer32):
    """Custom type alaOspfAreaOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("inactive", 1),
          ("up", 2))
    )


_AlaOspfAreaOperStatus_Type.__name__ = "Integer32"
_AlaOspfAreaOperStatus_Object = MibTableColumn
alaOspfAreaOperStatus = _AlaOspfAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 1),
    _AlaOspfAreaOperStatus_Type()
)
alaOspfAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaOperStatus.setStatus("current")
_AlaOspfAreaLastSpfRun_Type = Counter32
_AlaOspfAreaLastSpfRun_Object = MibTableColumn
alaOspfAreaLastSpfRun = _AlaOspfAreaLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 2),
    _AlaOspfAreaLastSpfRun_Type()
)
alaOspfAreaLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaLastSpfRun.setStatus("current")
_AlaOspfAreaActiveVlinks_Type = Counter32
_AlaOspfAreaActiveVlinks_Object = MibTableColumn
alaOspfAreaActiveVlinks = _AlaOspfAreaActiveVlinks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 3),
    _AlaOspfAreaActiveVlinks_Type()
)
alaOspfAreaActiveVlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaActiveVlinks.setStatus("current")
_AlaOspfAreaIncrSpfRuns_Type = Counter32
_AlaOspfAreaIncrSpfRuns_Object = MibTableColumn
alaOspfAreaIncrSpfRuns = _AlaOspfAreaIncrSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 4),
    _AlaOspfAreaIncrSpfRuns_Type()
)
alaOspfAreaIncrSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaIncrSpfRuns.setStatus("current")
_AlaOspfAreaInitNbrs_Type = Counter32
_AlaOspfAreaInitNbrs_Object = MibTableColumn
alaOspfAreaInitNbrs = _AlaOspfAreaInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 5),
    _AlaOspfAreaInitNbrs_Type()
)
alaOspfAreaInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaInitNbrs.setStatus("current")
_AlaOspfAreaExchNbrs_Type = Counter32
_AlaOspfAreaExchNbrs_Object = MibTableColumn
alaOspfAreaExchNbrs = _AlaOspfAreaExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 6),
    _AlaOspfAreaExchNbrs_Type()
)
alaOspfAreaExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaExchNbrs.setStatus("current")
_AlaOspfAreaFullNbrs_Type = Counter32
_AlaOspfAreaFullNbrs_Object = MibTableColumn
alaOspfAreaFullNbrs = _AlaOspfAreaFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 7),
    _AlaOspfAreaFullNbrs_Type()
)
alaOspfAreaFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaFullNbrs.setStatus("current")
_AlaOspfAreaNumIntfs_Type = Counter32
_AlaOspfAreaNumIntfs_Object = MibTableColumn
alaOspfAreaNumIntfs = _AlaOspfAreaNumIntfs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 8),
    _AlaOspfAreaNumIntfs_Type()
)
alaOspfAreaNumIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNumIntfs.setStatus("current")


class _AlaOspfAreaAttachedIntfs_Type(OctetString):
    """Custom type alaOspfAreaAttachedIntfs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2200),
    )


_AlaOspfAreaAttachedIntfs_Type.__name__ = "OctetString"
_AlaOspfAreaAttachedIntfs_Object = MibTableColumn
alaOspfAreaAttachedIntfs = _AlaOspfAreaAttachedIntfs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 9),
    _AlaOspfAreaAttachedIntfs_Type()
)
alaOspfAreaAttachedIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaAttachedIntfs.setStatus("current")
_AlaOspfArea2WayNbrs_Type = Counter32
_AlaOspfArea2WayNbrs_Object = MibTableColumn
alaOspfArea2WayNbrs = _AlaOspfArea2WayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 10),
    _AlaOspfArea2WayNbrs_Type()
)
alaOspfArea2WayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfArea2WayNbrs.setStatus("current")


class _AlaOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("candidate", 1),
          ("none", 3))
    )


_AlaOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorRole_Object = MibTableColumn
alaOspfAreaNssaTranslatorRole = _AlaOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 11),
    _AlaOspfAreaNssaTranslatorRole_Type()
)
alaOspfAreaNssaTranslatorRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorRole.setStatus("current")


class _AlaOspfAreaNssaTranslatorStabilityInterval_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorStabilityInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaOspfAreaNssaTranslatorStabilityInterval_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
alaOspfAreaNssaTranslatorStabilityInterval = _AlaOspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 12),
    _AlaOspfAreaNssaTranslatorStabilityInterval_Type()
)
alaOspfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorStabilityInterval.setStatus("current")


class _AlaOspfAreaNssaImportSetPbit_Type(Integer32):
    """Custom type alaOspfAreaNssaImportSetPbit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNotPropagate", 2),
          ("none", 3),
          ("propagate", 1))
    )


_AlaOspfAreaNssaImportSetPbit_Type.__name__ = "Integer32"
_AlaOspfAreaNssaImportSetPbit_Object = MibTableColumn
alaOspfAreaNssaImportSetPbit = _AlaOspfAreaNssaImportSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 13),
    _AlaOspfAreaNssaImportSetPbit_Type()
)
alaOspfAreaNssaImportSetPbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaImportSetPbit.setStatus("current")


class _AlaOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type alaOspfAreaNssaTranslatorState based on Integer32"""
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
        *(("disabled", 1),
          ("elected", 3),
          ("enabled", 2),
          ("none", 4))
    )


_AlaOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_AlaOspfAreaNssaTranslatorState_Object = MibTableColumn
alaOspfAreaNssaTranslatorState = _AlaOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 14),
    _AlaOspfAreaNssaTranslatorState_Type()
)
alaOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaTranslatorState.setStatus("current")
_AlaOspfAreaNssaElectedTranslatorRouterId_Type = IpAddress
_AlaOspfAreaNssaElectedTranslatorRouterId_Object = MibTableColumn
alaOspfAreaNssaElectedTranslatorRouterId = _AlaOspfAreaNssaElectedTranslatorRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 35, 1, 15),
    _AlaOspfAreaNssaElectedTranslatorRouterId_Type()
)
alaOspfAreaNssaElectedTranslatorRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAreaNssaElectedTranslatorRouterId.setStatus("current")
_AlaOspfExtLsdbAugTable_Object = MibTable
alaOspfExtLsdbAugTable = _AlaOspfExtLsdbAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36)
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugTable.setStatus("current")
_AlaOspfExtLsdbAugEntry_Object = MibTableRow
alaOspfExtLsdbAugEntry = _AlaOspfExtLsdbAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugEntry.setStatus("current")


class _AlaOspfExtLsdbProto_Type(Integer32):
    """Custom type alaOspfExtLsdbProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 7),
          ("direct", 3),
          ("isis", 6),
          ("local", 1),
          ("ospf", 5),
          ("rip", 4),
          ("static", 2))
    )


_AlaOspfExtLsdbProto_Type.__name__ = "Integer32"
_AlaOspfExtLsdbProto_Object = MibTableColumn
alaOspfExtLsdbProto = _AlaOspfExtLsdbProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 1),
    _AlaOspfExtLsdbProto_Type()
)
alaOspfExtLsdbProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbProto.setStatus("current")
_AlaOspfExtLsdbRouteTag_Type = Counter32
_AlaOspfExtLsdbRouteTag_Object = MibTableColumn
alaOspfExtLsdbRouteTag = _AlaOspfExtLsdbRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 2),
    _AlaOspfExtLsdbRouteTag_Type()
)
alaOspfExtLsdbRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbRouteTag.setStatus("current")
_AlaOspfExtLsdbFwdAddr_Type = IpAddress
_AlaOspfExtLsdbFwdAddr_Object = MibTableColumn
alaOspfExtLsdbFwdAddr = _AlaOspfExtLsdbFwdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 3),
    _AlaOspfExtLsdbFwdAddr_Type()
)
alaOspfExtLsdbFwdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbFwdAddr.setStatus("current")


class _AlaOspfExtLsdbMetricType_Type(Integer32):
    """Custom type alaOspfExtLsdbMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_AlaOspfExtLsdbMetricType_Type.__name__ = "Integer32"
_AlaOspfExtLsdbMetricType_Object = MibTableColumn
alaOspfExtLsdbMetricType = _AlaOspfExtLsdbMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 4),
    _AlaOspfExtLsdbMetricType_Type()
)
alaOspfExtLsdbMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMetricType.setStatus("current")
_AlaOspfExtLsdbMetric_Type = Integer32
_AlaOspfExtLsdbMetric_Object = MibTableColumn
alaOspfExtLsdbMetric = _AlaOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 5),
    _AlaOspfExtLsdbMetric_Type()
)
alaOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMetric.setStatus("current")
_AlaOspfExtLsdbLength_Type = Integer32
_AlaOspfExtLsdbLength_Object = MibTableColumn
alaOspfExtLsdbLength = _AlaOspfExtLsdbLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 6),
    _AlaOspfExtLsdbLength_Type()
)
alaOspfExtLsdbLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbLength.setStatus("current")
_AlaOspfExtLsdbMask_Type = IpAddress
_AlaOspfExtLsdbMask_Object = MibTableColumn
alaOspfExtLsdbMask = _AlaOspfExtLsdbMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 36, 1, 7),
    _AlaOspfExtLsdbMask_Type()
)
alaOspfExtLsdbMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfExtLsdbMask.setStatus("current")
_AlaOspfAreaInterfaceTable_Object = MibTable
alaOspfAreaInterfaceTable = _AlaOspfAreaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 37)
)
if mibBuilder.loadTexts:
    alaOspfAreaInterfaceTable.setStatus("obsolete")
_AlaOspfAreaInterfaceEntry_Object = MibTableRow
alaOspfAreaInterfaceEntry = _AlaOspfAreaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 37, 1)
)
alaOspfAreaInterfaceEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaId"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfIfIpAddress"),
    (0, "ALCATEL-IND1-OSPF-MIB", "alaOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    alaOspfAreaInterfaceEntry.setStatus("obsolete")
_AlaOspfIfIpAddress_Type = IpAddress
_AlaOspfIfIpAddress_Object = MibTableColumn
alaOspfIfIpAddress = _AlaOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 37, 1, 1),
    _AlaOspfIfIpAddress_Type()
)
alaOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfIfIpAddress.setStatus("obsolete")


class _AlaOspfAddressLessIf_Type(Integer32):
    """Custom type alaOspfAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaOspfAddressLessIf_Type.__name__ = "Integer32"
_AlaOspfAddressLessIf_Object = MibTableColumn
alaOspfAddressLessIf = _AlaOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 37, 1, 2),
    _AlaOspfAddressLessIf_Type()
)
alaOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfAddressLessIf.setStatus("obsolete")
_AlaOspfAreaAggregateAugTable_Object = MibTable
alaOspfAreaAggregateAugTable = _AlaOspfAreaAggregateAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38)
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugTable.setStatus("current")
_AlaOspfAreaAggregateAugEntry_Object = MibTableRow
alaOspfAreaAggregateAugEntry = _AlaOspfAreaAggregateAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38, 1)
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugEntry.setStatus("current")


class _AlaOspfAreaAggregateMetric_Type(Integer32):
    """Custom type alaOspfAreaAggregateMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspfAreaAggregateMetric_Type.__name__ = "Integer32"
_AlaOspfAreaAggregateMetric_Object = MibTableColumn
alaOspfAreaAggregateMetric = _AlaOspfAreaAggregateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 38, 1, 1),
    _AlaOspfAreaAggregateMetric_Type()
)
alaOspfAreaAggregateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfAreaAggregateMetric.setStatus("current")


class _AlaOspfDefaultOriginate_Type(Integer32):
    """Custom type alaOspfDefaultOriginate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("none", 1),
          ("only", 2))
    )


_AlaOspfDefaultOriginate_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginate_Object = MibScalar
alaOspfDefaultOriginate = _AlaOspfDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 39),
    _AlaOspfDefaultOriginate_Type()
)
alaOspfDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginate.setStatus("current")


class _AlaOspfDefaultOriginateMetricType_Type(Integer32):
    """Custom type alaOspfDefaultOriginateMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_AlaOspfDefaultOriginateMetricType_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginateMetricType_Object = MibScalar
alaOspfDefaultOriginateMetricType = _AlaOspfDefaultOriginateMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 40),
    _AlaOspfDefaultOriginateMetricType_Type()
)
alaOspfDefaultOriginateMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginateMetricType.setStatus("current")


class _AlaOspfDefaultOriginateMetric_Type(Integer32):
    """Custom type alaOspfDefaultOriginateMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOspfDefaultOriginateMetric_Type.__name__ = "Integer32"
_AlaOspfDefaultOriginateMetric_Object = MibScalar
alaOspfDefaultOriginateMetric = _AlaOspfDefaultOriginateMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 41),
    _AlaOspfDefaultOriginateMetric_Type()
)
alaOspfDefaultOriginateMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDefaultOriginateMetric.setStatus("current")


class _AlaOspfBfdStatus_Type(Integer32):
    """Custom type alaOspfBfdStatus based on Integer32"""
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


_AlaOspfBfdStatus_Type.__name__ = "Integer32"
_AlaOspfBfdStatus_Object = MibScalar
alaOspfBfdStatus = _AlaOspfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 42),
    _AlaOspfBfdStatus_Type()
)
alaOspfBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfBfdStatus.setStatus("current")


class _AlaOspfBfdAllInterfaceStatus_Type(Integer32):
    """Custom type alaOspfBfdAllInterfaceStatus based on Integer32"""
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


_AlaOspfBfdAllInterfaceStatus_Type.__name__ = "Integer32"
_AlaOspfBfdAllInterfaceStatus_Object = MibScalar
alaOspfBfdAllInterfaceStatus = _AlaOspfBfdAllInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 1, 43),
    _AlaOspfBfdAllInterfaceStatus_Type()
)
alaOspfBfdAllInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfBfdAllInterfaceStatus.setStatus("current")
_AlaOspfDebugConfig_ObjectIdentity = ObjectIdentity
alaOspfDebugConfig = _AlaOspfDebugConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2)
)


class _AlaOspfDebugLevel_Type(Integer32):
    """Custom type alaOspfDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaOspfDebugLevel_Type.__name__ = "Integer32"
_AlaOspfDebugLevel_Object = MibScalar
alaOspfDebugLevel = _AlaOspfDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 1),
    _AlaOspfDebugLevel_Type()
)
alaOspfDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugLevel.setStatus("deprecated")


class _AlaOspfDebugError_Type(Integer32):
    """Custom type alaOspfDebugError based on Integer32"""
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


_AlaOspfDebugError_Type.__name__ = "Integer32"
_AlaOspfDebugError_Object = MibScalar
alaOspfDebugError = _AlaOspfDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 2),
    _AlaOspfDebugError_Type()
)
alaOspfDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugError.setStatus("deprecated")


class _AlaOspfDebugWarning_Type(Integer32):
    """Custom type alaOspfDebugWarning based on Integer32"""
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


_AlaOspfDebugWarning_Type.__name__ = "Integer32"
_AlaOspfDebugWarning_Object = MibScalar
alaOspfDebugWarning = _AlaOspfDebugWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 3),
    _AlaOspfDebugWarning_Type()
)
alaOspfDebugWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugWarning.setStatus("deprecated")


class _AlaOspfDebugState_Type(Integer32):
    """Custom type alaOspfDebugState based on Integer32"""
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


_AlaOspfDebugState_Type.__name__ = "Integer32"
_AlaOspfDebugState_Object = MibScalar
alaOspfDebugState = _AlaOspfDebugState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 4),
    _AlaOspfDebugState_Type()
)
alaOspfDebugState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugState.setStatus("deprecated")


class _AlaOspfDebugRecv_Type(Integer32):
    """Custom type alaOspfDebugRecv based on Integer32"""
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


_AlaOspfDebugRecv_Type.__name__ = "Integer32"
_AlaOspfDebugRecv_Object = MibScalar
alaOspfDebugRecv = _AlaOspfDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 5),
    _AlaOspfDebugRecv_Type()
)
alaOspfDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugRecv.setStatus("deprecated")


class _AlaOspfDebugSend_Type(Integer32):
    """Custom type alaOspfDebugSend based on Integer32"""
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


_AlaOspfDebugSend_Type.__name__ = "Integer32"
_AlaOspfDebugSend_Object = MibScalar
alaOspfDebugSend = _AlaOspfDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 6),
    _AlaOspfDebugSend_Type()
)
alaOspfDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugSend.setStatus("deprecated")


class _AlaOspfDebugFlood_Type(Integer32):
    """Custom type alaOspfDebugFlood based on Integer32"""
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


_AlaOspfDebugFlood_Type.__name__ = "Integer32"
_AlaOspfDebugFlood_Object = MibScalar
alaOspfDebugFlood = _AlaOspfDebugFlood_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 7),
    _AlaOspfDebugFlood_Type()
)
alaOspfDebugFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugFlood.setStatus("deprecated")


class _AlaOspfDebugSPF_Type(Integer32):
    """Custom type alaOspfDebugSPF based on Integer32"""
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


_AlaOspfDebugSPF_Type.__name__ = "Integer32"
_AlaOspfDebugSPF_Object = MibScalar
alaOspfDebugSPF = _AlaOspfDebugSPF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 8),
    _AlaOspfDebugSPF_Type()
)
alaOspfDebugSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugSPF.setStatus("deprecated")


class _AlaOspfDebugLsdb_Type(Integer32):
    """Custom type alaOspfDebugLsdb based on Integer32"""
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


_AlaOspfDebugLsdb_Type.__name__ = "Integer32"
_AlaOspfDebugLsdb_Object = MibScalar
alaOspfDebugLsdb = _AlaOspfDebugLsdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 9),
    _AlaOspfDebugLsdb_Type()
)
alaOspfDebugLsdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugLsdb.setStatus("deprecated")


class _AlaOspfDebugRdb_Type(Integer32):
    """Custom type alaOspfDebugRdb based on Integer32"""
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


_AlaOspfDebugRdb_Type.__name__ = "Integer32"
_AlaOspfDebugRdb_Object = MibScalar
alaOspfDebugRdb = _AlaOspfDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 10),
    _AlaOspfDebugRdb_Type()
)
alaOspfDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugRdb.setStatus("deprecated")


class _AlaOspfDebugAge_Type(Integer32):
    """Custom type alaOspfDebugAge based on Integer32"""
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


_AlaOspfDebugAge_Type.__name__ = "Integer32"
_AlaOspfDebugAge_Object = MibScalar
alaOspfDebugAge = _AlaOspfDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 11),
    _AlaOspfDebugAge_Type()
)
alaOspfDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugAge.setStatus("deprecated")


class _AlaOspfDebugVlink_Type(Integer32):
    """Custom type alaOspfDebugVlink based on Integer32"""
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


_AlaOspfDebugVlink_Type.__name__ = "Integer32"
_AlaOspfDebugVlink_Object = MibScalar
alaOspfDebugVlink = _AlaOspfDebugVlink_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 12),
    _AlaOspfDebugVlink_Type()
)
alaOspfDebugVlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugVlink.setStatus("deprecated")


class _AlaOspfDebugRedist_Type(Integer32):
    """Custom type alaOspfDebugRedist based on Integer32"""
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


_AlaOspfDebugRedist_Type.__name__ = "Integer32"
_AlaOspfDebugRedist_Object = MibScalar
alaOspfDebugRedist = _AlaOspfDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 13),
    _AlaOspfDebugRedist_Type()
)
alaOspfDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugRedist.setStatus("deprecated")


class _AlaOspfDebugSummary_Type(Integer32):
    """Custom type alaOspfDebugSummary based on Integer32"""
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


_AlaOspfDebugSummary_Type.__name__ = "Integer32"
_AlaOspfDebugSummary_Object = MibScalar
alaOspfDebugSummary = _AlaOspfDebugSummary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 14),
    _AlaOspfDebugSummary_Type()
)
alaOspfDebugSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugSummary.setStatus("deprecated")


class _AlaOspfDebugDbexch_Type(Integer32):
    """Custom type alaOspfDebugDbexch based on Integer32"""
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


_AlaOspfDebugDbexch_Type.__name__ = "Integer32"
_AlaOspfDebugDbexch_Object = MibScalar
alaOspfDebugDbexch = _AlaOspfDebugDbexch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 15),
    _AlaOspfDebugDbexch_Type()
)
alaOspfDebugDbexch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugDbexch.setStatus("deprecated")


class _AlaOspfDebugHello_Type(Integer32):
    """Custom type alaOspfDebugHello based on Integer32"""
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


_AlaOspfDebugHello_Type.__name__ = "Integer32"
_AlaOspfDebugHello_Object = MibScalar
alaOspfDebugHello = _AlaOspfDebugHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 16),
    _AlaOspfDebugHello_Type()
)
alaOspfDebugHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugHello.setStatus("deprecated")


class _AlaOspfDebugAuth_Type(Integer32):
    """Custom type alaOspfDebugAuth based on Integer32"""
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


_AlaOspfDebugAuth_Type.__name__ = "Integer32"
_AlaOspfDebugAuth_Object = MibScalar
alaOspfDebugAuth = _AlaOspfDebugAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 17),
    _AlaOspfDebugAuth_Type()
)
alaOspfDebugAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugAuth.setStatus("deprecated")


class _AlaOspfDebugArea_Type(Integer32):
    """Custom type alaOspfDebugArea based on Integer32"""
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


_AlaOspfDebugArea_Type.__name__ = "Integer32"
_AlaOspfDebugArea_Object = MibScalar
alaOspfDebugArea = _AlaOspfDebugArea_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 18),
    _AlaOspfDebugArea_Type()
)
alaOspfDebugArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugArea.setStatus("deprecated")


class _AlaOspfDebugIntf_Type(Integer32):
    """Custom type alaOspfDebugIntf based on Integer32"""
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


_AlaOspfDebugIntf_Type.__name__ = "Integer32"
_AlaOspfDebugIntf_Object = MibScalar
alaOspfDebugIntf = _AlaOspfDebugIntf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 19),
    _AlaOspfDebugIntf_Type()
)
alaOspfDebugIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugIntf.setStatus("deprecated")


class _AlaOspfDebugMip_Type(Integer32):
    """Custom type alaOspfDebugMip based on Integer32"""
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


_AlaOspfDebugMip_Type.__name__ = "Integer32"
_AlaOspfDebugMip_Object = MibScalar
alaOspfDebugMip = _AlaOspfDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 20),
    _AlaOspfDebugMip_Type()
)
alaOspfDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugMip.setStatus("deprecated")


class _AlaOspfDebugInfo_Type(Integer32):
    """Custom type alaOspfDebugInfo based on Integer32"""
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


_AlaOspfDebugInfo_Type.__name__ = "Integer32"
_AlaOspfDebugInfo_Object = MibScalar
alaOspfDebugInfo = _AlaOspfDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 21),
    _AlaOspfDebugInfo_Type()
)
alaOspfDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugInfo.setStatus("deprecated")


class _AlaOspfDebugSetup_Type(Integer32):
    """Custom type alaOspfDebugSetup based on Integer32"""
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


_AlaOspfDebugSetup_Type.__name__ = "Integer32"
_AlaOspfDebugSetup_Object = MibScalar
alaOspfDebugSetup = _AlaOspfDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 22),
    _AlaOspfDebugSetup_Type()
)
alaOspfDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugSetup.setStatus("deprecated")


class _AlaOspfDebugTime_Type(Integer32):
    """Custom type alaOspfDebugTime based on Integer32"""
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


_AlaOspfDebugTime_Type.__name__ = "Integer32"
_AlaOspfDebugTime_Object = MibScalar
alaOspfDebugTime = _AlaOspfDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 23),
    _AlaOspfDebugTime_Type()
)
alaOspfDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugTime.setStatus("deprecated")


class _AlaOspfDebugTm_Type(Integer32):
    """Custom type alaOspfDebugTm based on Integer32"""
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


_AlaOspfDebugTm_Type.__name__ = "Integer32"
_AlaOspfDebugTm_Object = MibScalar
alaOspfDebugTm = _AlaOspfDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 24),
    _AlaOspfDebugTm_Type()
)
alaOspfDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugTm.setStatus("deprecated")


class _AlaOspfDebugAll_Type(Integer32):
    """Custom type alaOspfDebugAll based on Integer32"""
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


_AlaOspfDebugAll_Type.__name__ = "Integer32"
_AlaOspfDebugAll_Object = MibScalar
alaOspfDebugAll = _AlaOspfDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 25),
    _AlaOspfDebugAll_Type()
)
alaOspfDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugAll.setStatus("deprecated")


class _AlaOspfDebugRestart_Type(Integer32):
    """Custom type alaOspfDebugRestart based on Integer32"""
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


_AlaOspfDebugRestart_Type.__name__ = "Integer32"
_AlaOspfDebugRestart_Object = MibScalar
alaOspfDebugRestart = _AlaOspfDebugRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 26),
    _AlaOspfDebugRestart_Type()
)
alaOspfDebugRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugRestart.setStatus("deprecated")


class _AlaOspfDebugHelper_Type(Integer32):
    """Custom type alaOspfDebugHelper based on Integer32"""
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


_AlaOspfDebugHelper_Type.__name__ = "Integer32"
_AlaOspfDebugHelper_Object = MibScalar
alaOspfDebugHelper = _AlaOspfDebugHelper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 2, 27),
    _AlaOspfDebugHelper_Type()
)
alaOspfDebugHelper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspfDebugHelper.setStatus("deprecated")
_AlaOspfGeneralTable_ObjectIdentity = ObjectIdentity
alaOspfGeneralTable = _AlaOspfGeneralTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3)
)
_AlaOspfTotalSpfRuns_Type = Counter32
_AlaOspfTotalSpfRuns_Object = MibScalar
alaOspfTotalSpfRuns = _AlaOspfTotalSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 1),
    _AlaOspfTotalSpfRuns_Type()
)
alaOspfTotalSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalSpfRuns.setStatus("current")
_AlaOspfTotalIncrSpfRuns_Type = Counter32
_AlaOspfTotalIncrSpfRuns_Object = MibScalar
alaOspfTotalIncrSpfRuns = _AlaOspfTotalIncrSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 2),
    _AlaOspfTotalIncrSpfRuns_Type()
)
alaOspfTotalIncrSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalIncrSpfRuns.setStatus("current")
_AlaOspfTotalInitNbrs_Type = Counter32
_AlaOspfTotalInitNbrs_Object = MibScalar
alaOspfTotalInitNbrs = _AlaOspfTotalInitNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 3),
    _AlaOspfTotalInitNbrs_Type()
)
alaOspfTotalInitNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalInitNbrs.setStatus("current")
_AlaOspfTotalExchNbrs_Type = Counter32
_AlaOspfTotalExchNbrs_Object = MibScalar
alaOspfTotalExchNbrs = _AlaOspfTotalExchNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 4),
    _AlaOspfTotalExchNbrs_Type()
)
alaOspfTotalExchNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalExchNbrs.setStatus("current")
_AlaOspfTotalFullNbrs_Type = Counter32
_AlaOspfTotalFullNbrs_Object = MibScalar
alaOspfTotalFullNbrs = _AlaOspfTotalFullNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 5),
    _AlaOspfTotalFullNbrs_Type()
)
alaOspfTotalFullNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalFullNbrs.setStatus("current")
_AlaOspfTotalAreas_Type = Counter32
_AlaOspfTotalAreas_Object = MibScalar
alaOspfTotalAreas = _AlaOspfTotalAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 6),
    _AlaOspfTotalAreas_Type()
)
alaOspfTotalAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalAreas.setStatus("current")
_AlaOspfTotalActiveAreas_Type = Counter32
_AlaOspfTotalActiveAreas_Object = MibScalar
alaOspfTotalActiveAreas = _AlaOspfTotalActiveAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 7),
    _AlaOspfTotalActiveAreas_Type()
)
alaOspfTotalActiveAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalActiveAreas.setStatus("current")
_AlaOspfTotalTransitAreas_Type = Counter32
_AlaOspfTotalTransitAreas_Object = MibScalar
alaOspfTotalTransitAreas = _AlaOspfTotalTransitAreas_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 8),
    _AlaOspfTotalTransitAreas_Type()
)
alaOspfTotalTransitAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalTransitAreas.setStatus("current")
_AlaOspfTotalNSSA_Type = Counter32
_AlaOspfTotalNSSA_Object = MibScalar
alaOspfTotalNSSA = _AlaOspfTotalNSSA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 9),
    _AlaOspfTotalNSSA_Type()
)
alaOspfTotalNSSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotalNSSA.setStatus("current")
_AlaOspfTotal2wayNbrs_Type = Counter32
_AlaOspfTotal2wayNbrs_Object = MibScalar
alaOspfTotal2wayNbrs = _AlaOspfTotal2wayNbrs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 1, 3, 10),
    _AlaOspfTotal2wayNbrs_Type()
)
alaOspfTotal2wayNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOspfTotal2wayNbrs.setStatus("current")
_AlcatelIND1OSPFMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBConformance = _AlcatelIND1OSPFMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBConformance.setStatus("current")
_AlcatelIND1OSPFMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBGroups = _AlcatelIND1OSPFMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBGroups.setStatus("current")
_AlcatelIND1OSPFMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OSPFMIBCompliances = _AlcatelIND1OSPFMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBCompliances.setStatus("current")
ospfIfEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfIfAugEntry")
)
alaOspfIfAugEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfVirtIfAugEntry")
)
alaOspfVirtIfAugEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfNbrAugEntry")
)
alaOspfNbrAugEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfVirtNbrAugEntry")
)
alaOspfVirtNbrAugEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfAreaEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfAreaAugEntry")
)
alaOspfAreaAugEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfExtLsdbEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfExtLsdbAugEntry")
)
alaOspfExtLsdbAugEntry.setIndexNames(*ospfExtLsdbEntry.getIndexNames())
ospfAreaAggregateEntry.registerAugmentions(
    ("ALCATEL-IND1-OSPF-MIB",
     "alaOspfAreaAggregateAugEntry")
)
alaOspfAreaAggregateAugEntry.setIndexNames(*ospfAreaAggregateEntry.getIndexNames())

# Managed Objects groups

alaOspfMiscellaneousGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 1)
)
alaOspfMiscellaneousGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistAdminStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteTag"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTimerSpfDelay"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTimerSpfHold"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteNumber"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfMTUCheck"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBfdStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBfdAllInterfaceStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAsBdrRtr"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDefaultOriginate"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDefaultOriginateMetric"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDefaultOriginateMetricType"))
)
if mibBuilder.loadTexts:
    alaOspfMiscellaneousGroup.setStatus("current")

alaOspfRedistProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 2)
)
alaOspfRedistProtoGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoSubnets"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoMetricType"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoMetric"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoStatus"))
)
if mibBuilder.loadTexts:
    alaOspfRedistProtoGroup.setStatus("deprecated")

alaOspfDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 3)
)
alaOspfDebugGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugLevel"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugError"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugWarning"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugState"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugRecv"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugSend"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugFlood"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugSPF"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugLsdb"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugRdb"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugVlink"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugRedist"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugSummary"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugDbexch"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugHello"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugAuth"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugArea"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugIntf"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugMip"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugInfo"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugSetup"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugTime"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugTm"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugAll"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugHelper"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfDebugRestart"))
)
if mibBuilder.loadTexts:
    alaOspfDebugGroup.setStatus("current")

alaOspfRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 4)
)
alaOspfRouteGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteDest"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteMask"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteTos"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteNextHop"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteIfIndex"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteType"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteTag"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteMetric1"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteMetric2"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRouteStatus"))
)
if mibBuilder.loadTexts:
    alaOspfRouteGroup.setStatus("current")

alaOspfBdrRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 5)
)
alaOspfBdrRouterGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterAreaId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterTos"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterNextHop"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterIfIndex"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterType"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterMetric"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfBdrRouterStatus"))
)
if mibBuilder.loadTexts:
    alaOspfBdrRouterGroup.setStatus("current")

alaOspfRedistRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 6)
)
alaOspfRedistRouteGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteProto"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteDest"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteMask"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteMetric"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteControl"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteTagMatch"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteEffect"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistRouteStatus"))
)
if mibBuilder.loadTexts:
    alaOspfRedistRouteGroup.setStatus("deprecated")

alaOspfAreaInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 7)
)
alaOspfAreaInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfAddressLessIf"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfIpAddress"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfArea2WayNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaActiveVlinks"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaAttachedIntfs"))
)
if mibBuilder.loadTexts:
    alaOspfAreaInterfaceGroup.setStatus("current")

alaOspfIfMd5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 8)
)
alaOspfIfMd5Group.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5IpAddress"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5Key"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyStartAccept"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyStopAccept"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyStartGenerate"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5KeyStopGenerate"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5RowStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMd5EncryptKey"))
)
if mibBuilder.loadTexts:
    alaOspfIfMd5Group.setStatus("current")

alaOspfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 9)
)
alaOspfGeneralGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalSpfRuns"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalIncrSpfRuns"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalInitNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalExchNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalFullNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalAreas"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalActiveAreas"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalTransitAreas"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotalNSSA"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTotal2wayNbrs"))
)
if mibBuilder.loadTexts:
    alaOspfGeneralGroup.setStatus("current")

alaOspfAreaAggregateAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 10)
)
alaOspfAreaAggregateAugGroup.setObjects(
    ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaAggregateMetric")
)
if mibBuilder.loadTexts:
    alaOspfAreaAggregateAugGroup.setStatus("current")

alaOspfAreaAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 11)
)
alaOspfAreaAugGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaExchNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaFullNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaIncrSpfRuns"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaInitNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaLastSpfRun"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNssaElectedTranslatorRouterId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNssaImportSetPbit"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNssaTranslatorRole"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNssaTranslatorStabilityInterval"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNssaTranslatorState"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaNumIntfs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfAreaOperStatus"))
)
if mibBuilder.loadTexts:
    alaOspfAreaAugGroup.setStatus("current")

alaOspfExtLsdbAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 12)
)
alaOspfExtLsdbAugGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbFwdAddr"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbLength"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbMask"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbMetric"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbMetricType"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbProto"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfExtLsdbRouteTag"))
)
if mibBuilder.loadTexts:
    alaOspfExtLsdbAugGroup.setStatus("current")

alaOspfIfAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 13)
)
alaOspfIfAugGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfIf2WayNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfBdrRouterid"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfFullNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfBfdDrsOnly"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfBfdStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfDrRouterid"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfEncryptKey"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfExchNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfInitNbrs"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfIntfName"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfIpMask"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfLinkType"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfMTU"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfOperStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfIfVlanId"))
)
if mibBuilder.loadTexts:
    alaOspfIfAugGroup.setStatus("current")

alaOspfNbrAugEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 14)
)
alaOspfNbrAugEntryGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrAreaId"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrBdrAddress"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrDrAddress"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrLastHello"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrMd5SeqNo"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrMode"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrPendingLSack"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrPendingLSreq"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrPendingLSupd"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrRestartHelperAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrRestartHelperExitReason"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrRestartHelperStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfNbrType"))
)
if mibBuilder.loadTexts:
    alaOspfNbrAugEntryGroup.setStatus("current")

alaProtocolOspfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 15)
)
alaProtocolOspfGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfOpaqueLsaSupport"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRFC1583Compatibility"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRedistProtoRouteTag"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfReferenceBandwidth"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartExitReason"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartHelperStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartHelperStrictLSAChecking"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartHelperSupport"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartInitiate"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartInterval"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfRestartSupport"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfTrafficEngineeringSupport"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtIfEncryptKey"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtIfOperStatus"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrBdrAddr"))
)
if mibBuilder.loadTexts:
    alaProtocolOspfGroup.setStatus("current")

alaOspfVirtNbrAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 1, 16)
)
alaOspfVirtNbrAugGroup.setObjects(
      *(("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrDrAddr"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrLastHello"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrMd5SeqNo"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrMode"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrPendingLSack"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrPendingLSreq"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrPendingLSupd"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrRestartHelperAge"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrRestartHelperExitReason"),
        ("ALCATEL-IND1-OSPF-MIB", "alaOspfVirtNbrRestartHelperStatus"))
)
if mibBuilder.loadTexts:
    alaOspfVirtNbrAugGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1OSPFMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPFMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-OSPF-MIB",
    **{"AlaAuthenticationEncryptKey": AlaAuthenticationEncryptKey,
       "alcatelIND1OSPFMIB": alcatelIND1OSPFMIB,
       "alcatelIND1OSPFMIBObjects": alcatelIND1OSPFMIBObjects,
       "alaProtocolOspf": alaProtocolOspf,
       "alaOspfRedistAdminStatus": alaOspfRedistAdminStatus,
       "alaOspfRedistRouteTag": alaOspfRedistRouteTag,
       "alaOspfTimerSpfDelay": alaOspfTimerSpfDelay,
       "alaOspfTimerSpfHold": alaOspfTimerSpfHold,
       "alaOspfRouteNumber": alaOspfRouteNumber,
       "alaOspfMTUCheck": alaOspfMTUCheck,
       "alaOspfAsBdrRtr": alaOspfAsBdrRtr,
       "alaOspfRedistProtoTable": alaOspfRedistProtoTable,
       "alaOspfRedistProtoEntry": alaOspfRedistProtoEntry,
       "alaOspfRedistProtoId": alaOspfRedistProtoId,
       "alaOspfRedistProtoSubnets": alaOspfRedistProtoSubnets,
       "alaOspfRedistProtoMetricType": alaOspfRedistProtoMetricType,
       "alaOspfRedistProtoMetric": alaOspfRedistProtoMetric,
       "alaOspfRedistProtoStatus": alaOspfRedistProtoStatus,
       "alaOspfRedistProtoRouteTag": alaOspfRedistProtoRouteTag,
       "alaOspfRouteTable": alaOspfRouteTable,
       "alaOspfRouteEntry": alaOspfRouteEntry,
       "alaOspfRouteDest": alaOspfRouteDest,
       "alaOspfRouteMask": alaOspfRouteMask,
       "alaOspfRouteTos": alaOspfRouteTos,
       "alaOspfRouteNextHop": alaOspfRouteNextHop,
       "alaOspfRouteIfIndex": alaOspfRouteIfIndex,
       "alaOspfRouteType": alaOspfRouteType,
       "alaOspfRouteAge": alaOspfRouteAge,
       "alaOspfRouteTag": alaOspfRouteTag,
       "alaOspfRouteMetric1": alaOspfRouteMetric1,
       "alaOspfRouteMetric2": alaOspfRouteMetric2,
       "alaOspfRouteStatus": alaOspfRouteStatus,
       "alaOspfBdrRouterTable": alaOspfBdrRouterTable,
       "alaOspfBdrRouterEntry": alaOspfBdrRouterEntry,
       "alaOspfBdrRouterAreaId": alaOspfBdrRouterAreaId,
       "alaOspfBdrRouterId": alaOspfBdrRouterId,
       "alaOspfBdrRouterTos": alaOspfBdrRouterTos,
       "alaOspfBdrRouterNextHop": alaOspfBdrRouterNextHop,
       "alaOspfBdrRouterIfIndex": alaOspfBdrRouterIfIndex,
       "alaOspfBdrRouterType": alaOspfBdrRouterType,
       "alaOspfBdrRouterAge": alaOspfBdrRouterAge,
       "alaOspfBdrRouterMetric": alaOspfBdrRouterMetric,
       "alaOspfBdrRouterStatus": alaOspfBdrRouterStatus,
       "alaOspfRedistRouteTable": alaOspfRedistRouteTable,
       "alaOspfRedistRouteEntry": alaOspfRedistRouteEntry,
       "alaOspfRedistRouteProto": alaOspfRedistRouteProto,
       "alaOspfRedistRouteDest": alaOspfRedistRouteDest,
       "alaOspfRedistRouteMask": alaOspfRedistRouteMask,
       "alaOspfRedistRouteMetric": alaOspfRedistRouteMetric,
       "alaOspfRedistRouteControl": alaOspfRedistRouteControl,
       "alaOspfRedistRouteTagMatch": alaOspfRedistRouteTagMatch,
       "alaOspfRedistRouteEffect": alaOspfRedistRouteEffect,
       "alaOspfRedistRouteStatus": alaOspfRedistRouteStatus,
       "alaOspfIfMd5Table": alaOspfIfMd5Table,
       "alaOspfIfMd5Entry": alaOspfIfMd5Entry,
       "alaOspfIfMd5IpAddress": alaOspfIfMd5IpAddress,
       "alaOspfIfMd5KeyId": alaOspfIfMd5KeyId,
       "alaOspfIfMd5Key": alaOspfIfMd5Key,
       "alaOspfIfMd5KeyStartAccept": alaOspfIfMd5KeyStartAccept,
       "alaOspfIfMd5KeyStopAccept": alaOspfIfMd5KeyStopAccept,
       "alaOspfIfMd5KeyStartGenerate": alaOspfIfMd5KeyStartGenerate,
       "alaOspfIfMd5KeyStopGenerate": alaOspfIfMd5KeyStopGenerate,
       "alaOspfIfMd5RowStatus": alaOspfIfMd5RowStatus,
       "alaOspfIfMd5EncryptKey": alaOspfIfMd5EncryptKey,
       "alaOspfIfAugTable": alaOspfIfAugTable,
       "alaOspfIfAugEntry": alaOspfIfAugEntry,
       "alaOspfIfEncryptKey": alaOspfIfEncryptKey,
       "alaOspfIfIpMask": alaOspfIfIpMask,
       "alaOspfIfVlanId": alaOspfIfVlanId,
       "alaOspfIfDrRouterid": alaOspfIfDrRouterid,
       "alaOspfIfBdrRouterid": alaOspfIfBdrRouterid,
       "alaOspfIfMTU": alaOspfIfMTU,
       "alaOspfIfInitNbrs": alaOspfIfInitNbrs,
       "alaOspfIfExchNbrs": alaOspfIfExchNbrs,
       "alaOspfIfFullNbrs": alaOspfIfFullNbrs,
       "alaOspfIfLinkType": alaOspfIfLinkType,
       "alaOspfIfOperStatus": alaOspfIfOperStatus,
       "alaOspfIfIntfName": alaOspfIfIntfName,
       "alaOspfIf2WayNbrs": alaOspfIf2WayNbrs,
       "alaOspfIfBfdStatus": alaOspfIfBfdStatus,
       "alaOspfIfBfdDrsOnly": alaOspfIfBfdDrsOnly,
       "alaOspfVirtIfAugTable": alaOspfVirtIfAugTable,
       "alaOspfVirtIfAugEntry": alaOspfVirtIfAugEntry,
       "alaOspfVirtIfEncryptKey": alaOspfVirtIfEncryptKey,
       "alaOspfVirtIfOperStatus": alaOspfVirtIfOperStatus,
       "alaOspfRestartHelperSupport": alaOspfRestartHelperSupport,
       "alaOspfRestartHelperStrictLSAChecking": alaOspfRestartHelperStrictLSAChecking,
       "alaOspfRestartHelperStatus": alaOspfRestartHelperStatus,
       "alaOspfRFC1583Compatibility": alaOspfRFC1583Compatibility,
       "alaOspfOpaqueLsaSupport": alaOspfOpaqueLsaSupport,
       "alaOspfTrafficEngineeringSupport": alaOspfTrafficEngineeringSupport,
       "alaOspfReferenceBandwidth": alaOspfReferenceBandwidth,
       "alaOspfRestartSupport": alaOspfRestartSupport,
       "alaOspfRestartInterval": alaOspfRestartInterval,
       "alaOspfRestartStatus": alaOspfRestartStatus,
       "alaOspfRestartAge": alaOspfRestartAge,
       "alaOspfRestartExitReason": alaOspfRestartExitReason,
       "alaOspfNbrAugTable": alaOspfNbrAugTable,
       "alaOspfNbrAugEntry": alaOspfNbrAugEntry,
       "alaOspfNbrRestartHelperStatus": alaOspfNbrRestartHelperStatus,
       "alaOspfNbrRestartHelperAge": alaOspfNbrRestartHelperAge,
       "alaOspfNbrRestartHelperExitReason": alaOspfNbrRestartHelperExitReason,
       "alaOspfNbrAreaId": alaOspfNbrAreaId,
       "alaOspfNbrDrAddress": alaOspfNbrDrAddress,
       "alaOspfNbrBdrAddress": alaOspfNbrBdrAddress,
       "alaOspfNbrType": alaOspfNbrType,
       "alaOspfNbrMode": alaOspfNbrMode,
       "alaOspfNbrMd5SeqNo": alaOspfNbrMd5SeqNo,
       "alaOspfNbrLastHello": alaOspfNbrLastHello,
       "alaOspfNbrPendingLSreq": alaOspfNbrPendingLSreq,
       "alaOspfNbrPendingLSack": alaOspfNbrPendingLSack,
       "alaOspfNbrPendingLSupd": alaOspfNbrPendingLSupd,
       "alaOspfVirtNbrAugTable": alaOspfVirtNbrAugTable,
       "alaOspfVirtNbrAugEntry": alaOspfVirtNbrAugEntry,
       "alaOspfVirtNbrRestartHelperStatus": alaOspfVirtNbrRestartHelperStatus,
       "alaOspfVirtNbrRestartHelperAge": alaOspfVirtNbrRestartHelperAge,
       "alaOspfVirtNbrRestartHelperExitReason": alaOspfVirtNbrRestartHelperExitReason,
       "alaOspfVirtNbrDrAddr": alaOspfVirtNbrDrAddr,
       "alaOspfVirtNbrBdrAddr": alaOspfVirtNbrBdrAddr,
       "alaOspfVirtNbrMode": alaOspfVirtNbrMode,
       "alaOspfVirtNbrMd5SeqNo": alaOspfVirtNbrMd5SeqNo,
       "alaOspfVirtNbrLastHello": alaOspfVirtNbrLastHello,
       "alaOspfVirtNbrPendingLSreq": alaOspfVirtNbrPendingLSreq,
       "alaOspfVirtNbrPendingLSack": alaOspfVirtNbrPendingLSack,
       "alaOspfVirtNbrPendingLSupd": alaOspfVirtNbrPendingLSupd,
       "alaOspfRestartInitiate": alaOspfRestartInitiate,
       "alaOspfAreaAugTable": alaOspfAreaAugTable,
       "alaOspfAreaAugEntry": alaOspfAreaAugEntry,
       "alaOspfAreaOperStatus": alaOspfAreaOperStatus,
       "alaOspfAreaLastSpfRun": alaOspfAreaLastSpfRun,
       "alaOspfAreaActiveVlinks": alaOspfAreaActiveVlinks,
       "alaOspfAreaIncrSpfRuns": alaOspfAreaIncrSpfRuns,
       "alaOspfAreaInitNbrs": alaOspfAreaInitNbrs,
       "alaOspfAreaExchNbrs": alaOspfAreaExchNbrs,
       "alaOspfAreaFullNbrs": alaOspfAreaFullNbrs,
       "alaOspfAreaNumIntfs": alaOspfAreaNumIntfs,
       "alaOspfAreaAttachedIntfs": alaOspfAreaAttachedIntfs,
       "alaOspfArea2WayNbrs": alaOspfArea2WayNbrs,
       "alaOspfAreaNssaTranslatorRole": alaOspfAreaNssaTranslatorRole,
       "alaOspfAreaNssaTranslatorStabilityInterval": alaOspfAreaNssaTranslatorStabilityInterval,
       "alaOspfAreaNssaImportSetPbit": alaOspfAreaNssaImportSetPbit,
       "alaOspfAreaNssaTranslatorState": alaOspfAreaNssaTranslatorState,
       "alaOspfAreaNssaElectedTranslatorRouterId": alaOspfAreaNssaElectedTranslatorRouterId,
       "alaOspfExtLsdbAugTable": alaOspfExtLsdbAugTable,
       "alaOspfExtLsdbAugEntry": alaOspfExtLsdbAugEntry,
       "alaOspfExtLsdbProto": alaOspfExtLsdbProto,
       "alaOspfExtLsdbRouteTag": alaOspfExtLsdbRouteTag,
       "alaOspfExtLsdbFwdAddr": alaOspfExtLsdbFwdAddr,
       "alaOspfExtLsdbMetricType": alaOspfExtLsdbMetricType,
       "alaOspfExtLsdbMetric": alaOspfExtLsdbMetric,
       "alaOspfExtLsdbLength": alaOspfExtLsdbLength,
       "alaOspfExtLsdbMask": alaOspfExtLsdbMask,
       "alaOspfAreaInterfaceTable": alaOspfAreaInterfaceTable,
       "alaOspfAreaInterfaceEntry": alaOspfAreaInterfaceEntry,
       "alaOspfIfIpAddress": alaOspfIfIpAddress,
       "alaOspfAddressLessIf": alaOspfAddressLessIf,
       "alaOspfAreaAggregateAugTable": alaOspfAreaAggregateAugTable,
       "alaOspfAreaAggregateAugEntry": alaOspfAreaAggregateAugEntry,
       "alaOspfAreaAggregateMetric": alaOspfAreaAggregateMetric,
       "alaOspfDefaultOriginate": alaOspfDefaultOriginate,
       "alaOspfDefaultOriginateMetricType": alaOspfDefaultOriginateMetricType,
       "alaOspfDefaultOriginateMetric": alaOspfDefaultOriginateMetric,
       "alaOspfBfdStatus": alaOspfBfdStatus,
       "alaOspfBfdAllInterfaceStatus": alaOspfBfdAllInterfaceStatus,
       "alaOspfDebugConfig": alaOspfDebugConfig,
       "alaOspfDebugLevel": alaOspfDebugLevel,
       "alaOspfDebugError": alaOspfDebugError,
       "alaOspfDebugWarning": alaOspfDebugWarning,
       "alaOspfDebugState": alaOspfDebugState,
       "alaOspfDebugRecv": alaOspfDebugRecv,
       "alaOspfDebugSend": alaOspfDebugSend,
       "alaOspfDebugFlood": alaOspfDebugFlood,
       "alaOspfDebugSPF": alaOspfDebugSPF,
       "alaOspfDebugLsdb": alaOspfDebugLsdb,
       "alaOspfDebugRdb": alaOspfDebugRdb,
       "alaOspfDebugAge": alaOspfDebugAge,
       "alaOspfDebugVlink": alaOspfDebugVlink,
       "alaOspfDebugRedist": alaOspfDebugRedist,
       "alaOspfDebugSummary": alaOspfDebugSummary,
       "alaOspfDebugDbexch": alaOspfDebugDbexch,
       "alaOspfDebugHello": alaOspfDebugHello,
       "alaOspfDebugAuth": alaOspfDebugAuth,
       "alaOspfDebugArea": alaOspfDebugArea,
       "alaOspfDebugIntf": alaOspfDebugIntf,
       "alaOspfDebugMip": alaOspfDebugMip,
       "alaOspfDebugInfo": alaOspfDebugInfo,
       "alaOspfDebugSetup": alaOspfDebugSetup,
       "alaOspfDebugTime": alaOspfDebugTime,
       "alaOspfDebugTm": alaOspfDebugTm,
       "alaOspfDebugAll": alaOspfDebugAll,
       "alaOspfDebugRestart": alaOspfDebugRestart,
       "alaOspfDebugHelper": alaOspfDebugHelper,
       "alaOspfGeneralTable": alaOspfGeneralTable,
       "alaOspfTotalSpfRuns": alaOspfTotalSpfRuns,
       "alaOspfTotalIncrSpfRuns": alaOspfTotalIncrSpfRuns,
       "alaOspfTotalInitNbrs": alaOspfTotalInitNbrs,
       "alaOspfTotalExchNbrs": alaOspfTotalExchNbrs,
       "alaOspfTotalFullNbrs": alaOspfTotalFullNbrs,
       "alaOspfTotalAreas": alaOspfTotalAreas,
       "alaOspfTotalActiveAreas": alaOspfTotalActiveAreas,
       "alaOspfTotalTransitAreas": alaOspfTotalTransitAreas,
       "alaOspfTotalNSSA": alaOspfTotalNSSA,
       "alaOspfTotal2wayNbrs": alaOspfTotal2wayNbrs,
       "alcatelIND1OSPFMIBConformance": alcatelIND1OSPFMIBConformance,
       "alcatelIND1OSPFMIBGroups": alcatelIND1OSPFMIBGroups,
       "alaOspfMiscellaneousGroup": alaOspfMiscellaneousGroup,
       "alaOspfRedistProtoGroup": alaOspfRedistProtoGroup,
       "alaOspfDebugGroup": alaOspfDebugGroup,
       "alaOspfRouteGroup": alaOspfRouteGroup,
       "alaOspfBdrRouterGroup": alaOspfBdrRouterGroup,
       "alaOspfRedistRouteGroup": alaOspfRedistRouteGroup,
       "alaOspfAreaInterfaceGroup": alaOspfAreaInterfaceGroup,
       "alaOspfIfMd5Group": alaOspfIfMd5Group,
       "alaOspfGeneralGroup": alaOspfGeneralGroup,
       "alaOspfAreaAggregateAugGroup": alaOspfAreaAggregateAugGroup,
       "alaOspfAreaAugGroup": alaOspfAreaAugGroup,
       "alaOspfExtLsdbAugGroup": alaOspfExtLsdbAugGroup,
       "alaOspfIfAugGroup": alaOspfIfAugGroup,
       "alaOspfNbrAugEntryGroup": alaOspfNbrAugEntryGroup,
       "alaProtocolOspfGroup": alaProtocolOspfGroup,
       "alaOspfVirtNbrAugGroup": alaOspfVirtNbrAugGroup,
       "alcatelIND1OSPFMIBCompliances": alcatelIND1OSPFMIBCompliances,
       "alcatelIND1OSPFMIBCompliance": alcatelIND1OSPFMIBCompliance}
)
