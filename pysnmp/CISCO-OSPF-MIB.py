# SNMP MIB module (CISCO-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:29 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(AreaID,
 HelloRange,
 Metric,
 PositiveInteger,
 RouterID,
 UpToMaxAge,
 ospfAreaEntry,
 ospfIfEntry,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "RouterID",
    "UpToMaxAge",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfVirtIfEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cospf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99)
)
cospf.setRevisions(
        ("2003-07-18 00:00",
         "2003-01-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CospfGeneralGroup_ObjectIdentity = ObjectIdentity
cospfGeneralGroup = _CospfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1)
)
_CospfRFC1583Compatibility_Type = TruthValue
_CospfRFC1583Compatibility_Object = MibScalar
cospfRFC1583Compatibility = _CospfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1, 1),
    _CospfRFC1583Compatibility_Type()
)
cospfRFC1583Compatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfRFC1583Compatibility.setStatus("current")
_CospfOpaqueLsaSupport_Type = TruthValue
_CospfOpaqueLsaSupport_Object = MibScalar
cospfOpaqueLsaSupport = _CospfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1, 2),
    _CospfOpaqueLsaSupport_Type()
)
cospfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfOpaqueLsaSupport.setStatus("current")
_CospfTrafficEngineeringSupport_Type = TruthValue
_CospfTrafficEngineeringSupport_Object = MibScalar
cospfTrafficEngineeringSupport = _CospfTrafficEngineeringSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1, 3),
    _CospfTrafficEngineeringSupport_Type()
)
cospfTrafficEngineeringSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfTrafficEngineeringSupport.setStatus("current")
_CospfOpaqueASLsaCount_Type = Gauge32
_CospfOpaqueASLsaCount_Object = MibScalar
cospfOpaqueASLsaCount = _CospfOpaqueASLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1, 4),
    _CospfOpaqueASLsaCount_Type()
)
cospfOpaqueASLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfOpaqueASLsaCount.setStatus("current")


class _CospfOpaqueASLsaCksumSum_Type(Unsigned32):
    """Custom type cospfOpaqueASLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfOpaqueASLsaCksumSum_Type.__name__ = "Unsigned32"
_CospfOpaqueASLsaCksumSum_Object = MibScalar
cospfOpaqueASLsaCksumSum = _CospfOpaqueASLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 1, 5),
    _CospfOpaqueASLsaCksumSum_Type()
)
cospfOpaqueASLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfOpaqueASLsaCksumSum.setStatus("current")
_CospfAreaTable_Object = MibTable
cospfAreaTable = _CospfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2)
)
if mibBuilder.loadTexts:
    cospfAreaTable.setStatus("current")
_CospfAreaEntry_Object = MibTableRow
cospfAreaEntry = _CospfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1)
)
if mibBuilder.loadTexts:
    cospfAreaEntry.setStatus("current")
_CospfOpaqueAreaLsaCount_Type = Gauge32
_CospfOpaqueAreaLsaCount_Object = MibTableColumn
cospfOpaqueAreaLsaCount = _CospfOpaqueAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1, 1),
    _CospfOpaqueAreaLsaCount_Type()
)
cospfOpaqueAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfOpaqueAreaLsaCount.setStatus("current")


class _CospfOpaqueAreaLsaCksumSum_Type(Unsigned32):
    """Custom type cospfOpaqueAreaLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfOpaqueAreaLsaCksumSum_Type.__name__ = "Unsigned32"
_CospfOpaqueAreaLsaCksumSum_Object = MibTableColumn
cospfOpaqueAreaLsaCksumSum = _CospfOpaqueAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1, 2),
    _CospfOpaqueAreaLsaCksumSum_Type()
)
cospfOpaqueAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfOpaqueAreaLsaCksumSum.setStatus("current")


class _CospfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type cospfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_CospfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_CospfAreaNssaTranslatorRole_Object = MibTableColumn
cospfAreaNssaTranslatorRole = _CospfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1, 3),
    _CospfAreaNssaTranslatorRole_Type()
)
cospfAreaNssaTranslatorRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfAreaNssaTranslatorRole.setStatus("current")


class _CospfAreaNssaTranslatorState_Type(Integer32):
    """Custom type cospfAreaNssaTranslatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("elected", 2),
          ("enabled", 1))
    )


_CospfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_CospfAreaNssaTranslatorState_Object = MibTableColumn
cospfAreaNssaTranslatorState = _CospfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1, 4),
    _CospfAreaNssaTranslatorState_Type()
)
cospfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfAreaNssaTranslatorState.setStatus("current")
_CospfAreaNssaTranslatorEvents_Type = Counter32
_CospfAreaNssaTranslatorEvents_Object = MibTableColumn
cospfAreaNssaTranslatorEvents = _CospfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 2, 1, 5),
    _CospfAreaNssaTranslatorEvents_Type()
)
cospfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfAreaNssaTranslatorEvents.setStatus("current")
_CospfLsdbTable_Object = MibTable
cospfLsdbTable = _CospfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3)
)
if mibBuilder.loadTexts:
    cospfLsdbTable.setStatus("current")
_CospfLsdbEntry_Object = MibTableRow
cospfLsdbEntry = _CospfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1)
)
cospfLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "CISCO-OSPF-MIB", "cospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    cospfLsdbEntry.setStatus("current")


class _CospfLsdbType_Type(Integer32):
    """Custom type cospfLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("areaOpaqueLink", 10),
          ("asOpaqueLink", 11))
    )


_CospfLsdbType_Type.__name__ = "Integer32"
_CospfLsdbType_Object = MibTableColumn
cospfLsdbType = _CospfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1, 1),
    _CospfLsdbType_Type()
)
cospfLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLsdbType.setStatus("current")


class _CospfLsdbSequence_Type(Integer32):
    """Custom type cospfLsdbSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 147483647),
    )


_CospfLsdbSequence_Type.__name__ = "Integer32"
_CospfLsdbSequence_Object = MibTableColumn
cospfLsdbSequence = _CospfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1, 2),
    _CospfLsdbSequence_Type()
)
cospfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLsdbSequence.setStatus("current")


class _CospfLsdbAge_Type(Integer32):
    """Custom type cospfLsdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CospfLsdbAge_Type.__name__ = "Integer32"
_CospfLsdbAge_Object = MibTableColumn
cospfLsdbAge = _CospfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1, 3),
    _CospfLsdbAge_Type()
)
cospfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLsdbAge.setStatus("current")


class _CospfLsdbChecksum_Type(Integer32):
    """Custom type cospfLsdbChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CospfLsdbChecksum_Type.__name__ = "Integer32"
_CospfLsdbChecksum_Object = MibTableColumn
cospfLsdbChecksum = _CospfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1, 4),
    _CospfLsdbChecksum_Type()
)
cospfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLsdbChecksum.setStatus("current")


class _CospfLsdbAdvertisement_Type(OctetString):
    """Custom type cospfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_CospfLsdbAdvertisement_Type.__name__ = "OctetString"
_CospfLsdbAdvertisement_Object = MibTableColumn
cospfLsdbAdvertisement = _CospfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 3, 1, 5),
    _CospfLsdbAdvertisement_Type()
)
cospfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLsdbAdvertisement.setStatus("current")
_CospfIfTable_Object = MibTable
cospfIfTable = _CospfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 4)
)
if mibBuilder.loadTexts:
    cospfIfTable.setStatus("current")
_CospfIfEntry_Object = MibTableRow
cospfIfEntry = _CospfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 4, 1)
)
if mibBuilder.loadTexts:
    cospfIfEntry.setStatus("current")
_CospfIfLsaCount_Type = Gauge32
_CospfIfLsaCount_Object = MibTableColumn
cospfIfLsaCount = _CospfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 4, 1, 1),
    _CospfIfLsaCount_Type()
)
cospfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfIfLsaCount.setStatus("current")


class _CospfIfLsaCksumSum_Type(Unsigned32):
    """Custom type cospfIfLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfIfLsaCksumSum_Type.__name__ = "Unsigned32"
_CospfIfLsaCksumSum_Object = MibTableColumn
cospfIfLsaCksumSum = _CospfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 4, 1, 2),
    _CospfIfLsaCksumSum_Type()
)
cospfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfIfLsaCksumSum.setStatus("current")
_CospfVirtIfTable_Object = MibTable
cospfVirtIfTable = _CospfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 5)
)
if mibBuilder.loadTexts:
    cospfVirtIfTable.setStatus("current")
_CospfVirtIfEntry_Object = MibTableRow
cospfVirtIfEntry = _CospfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 5, 1)
)
if mibBuilder.loadTexts:
    cospfVirtIfEntry.setStatus("current")
_CospfVirtIfLsaCount_Type = Gauge32
_CospfVirtIfLsaCount_Object = MibTableColumn
cospfVirtIfLsaCount = _CospfVirtIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 5, 1, 1),
    _CospfVirtIfLsaCount_Type()
)
cospfVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtIfLsaCount.setStatus("current")


class _CospfVirtIfLsaCksumSum_Type(Unsigned32):
    """Custom type cospfVirtIfLsaCksumSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfVirtIfLsaCksumSum_Type.__name__ = "Unsigned32"
_CospfVirtIfLsaCksumSum_Object = MibTableColumn
cospfVirtIfLsaCksumSum = _CospfVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 5, 1, 2),
    _CospfVirtIfLsaCksumSum_Type()
)
cospfVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtIfLsaCksumSum.setStatus("current")
_CospfShamLinkTable_Object = MibTable
cospfShamLinkTable = _CospfShamLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6)
)
if mibBuilder.loadTexts:
    cospfShamLinkTable.setStatus("deprecated")
_CospfShamLinkEntry_Object = MibTableRow
cospfShamLinkEntry = _CospfShamLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1)
)
cospfShamLinkEntry.setIndexNames(
    (0, "CISCO-OSPF-MIB", "cospfShamLinkAreaId"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinkLocalIpAddress"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinkNeighborId"),
)
if mibBuilder.loadTexts:
    cospfShamLinkEntry.setStatus("deprecated")
_CospfShamLinkAreaId_Type = AreaID
_CospfShamLinkAreaId_Object = MibTableColumn
cospfShamLinkAreaId = _CospfShamLinkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 1),
    _CospfShamLinkAreaId_Type()
)
cospfShamLinkAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkAreaId.setStatus("deprecated")
_CospfShamLinkLocalIpAddress_Type = IpAddress
_CospfShamLinkLocalIpAddress_Object = MibTableColumn
cospfShamLinkLocalIpAddress = _CospfShamLinkLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 2),
    _CospfShamLinkLocalIpAddress_Type()
)
cospfShamLinkLocalIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkLocalIpAddress.setStatus("deprecated")
_CospfShamLinkNeighborId_Type = RouterID
_CospfShamLinkNeighborId_Object = MibTableColumn
cospfShamLinkNeighborId = _CospfShamLinkNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 3),
    _CospfShamLinkNeighborId_Type()
)
cospfShamLinkNeighborId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkNeighborId.setStatus("deprecated")


class _CospfShamLinkRetransInterval_Type(UpToMaxAge):
    """Custom type cospfShamLinkRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_CospfShamLinkRetransInterval_Object = MibTableColumn
cospfShamLinkRetransInterval = _CospfShamLinkRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 4),
    _CospfShamLinkRetransInterval_Type()
)
cospfShamLinkRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkRetransInterval.setStatus("deprecated")


class _CospfShamLinkHelloInterval_Type(HelloRange):
    """Custom type cospfShamLinkHelloInterval based on HelloRange"""
    defaultValue = 10


_CospfShamLinkHelloInterval_Object = MibTableColumn
cospfShamLinkHelloInterval = _CospfShamLinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 5),
    _CospfShamLinkHelloInterval_Type()
)
cospfShamLinkHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkHelloInterval.setStatus("deprecated")


class _CospfShamLinkRtrDeadInterval_Type(PositiveInteger):
    """Custom type cospfShamLinkRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_CospfShamLinkRtrDeadInterval_Object = MibTableColumn
cospfShamLinkRtrDeadInterval = _CospfShamLinkRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 6),
    _CospfShamLinkRtrDeadInterval_Type()
)
cospfShamLinkRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkRtrDeadInterval.setStatus("deprecated")


class _CospfShamLinkState_Type(Integer32):
    """Custom type cospfShamLinkState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_CospfShamLinkState_Type.__name__ = "Integer32"
_CospfShamLinkState_Object = MibTableColumn
cospfShamLinkState = _CospfShamLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 7),
    _CospfShamLinkState_Type()
)
cospfShamLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkState.setStatus("deprecated")
_CospfShamLinkEvents_Type = Counter32
_CospfShamLinkEvents_Object = MibTableColumn
cospfShamLinkEvents = _CospfShamLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 8),
    _CospfShamLinkEvents_Type()
)
cospfShamLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkEvents.setStatus("deprecated")
_CospfShamLinkMetric_Type = Metric
_CospfShamLinkMetric_Object = MibTableColumn
cospfShamLinkMetric = _CospfShamLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 6, 1, 9),
    _CospfShamLinkMetric_Type()
)
cospfShamLinkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkMetric.setStatus("deprecated")
_CospfLocalLsdbTable_Object = MibTable
cospfLocalLsdbTable = _CospfLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7)
)
if mibBuilder.loadTexts:
    cospfLocalLsdbTable.setStatus("current")
_CospfLocalLsdbEntry_Object = MibTableRow
cospfLocalLsdbEntry = _CospfLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1)
)
cospfLocalLsdbEntry.setIndexNames(
    (0, "CISCO-OSPF-MIB", "cospfLocalLsdbIpAddress"),
    (0, "CISCO-OSPF-MIB", "cospfLocalLsdbAddressLessIf"),
    (0, "CISCO-OSPF-MIB", "cospfLocalLsdbType"),
    (0, "CISCO-OSPF-MIB", "cospfLocalLsdbLsid"),
    (0, "CISCO-OSPF-MIB", "cospfLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    cospfLocalLsdbEntry.setStatus("current")
_CospfLocalLsdbIpAddress_Type = IpAddress
_CospfLocalLsdbIpAddress_Object = MibTableColumn
cospfLocalLsdbIpAddress = _CospfLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 1),
    _CospfLocalLsdbIpAddress_Type()
)
cospfLocalLsdbIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLocalLsdbIpAddress.setStatus("current")
_CospfLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_CospfLocalLsdbAddressLessIf_Object = MibTableColumn
cospfLocalLsdbAddressLessIf = _CospfLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 2),
    _CospfLocalLsdbAddressLessIf_Type()
)
cospfLocalLsdbAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLocalLsdbAddressLessIf.setStatus("current")


class _CospfLocalLsdbType_Type(Integer32):
    """Custom type cospfLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_CospfLocalLsdbType_Type.__name__ = "Integer32"
_CospfLocalLsdbType_Object = MibTableColumn
cospfLocalLsdbType = _CospfLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 3),
    _CospfLocalLsdbType_Type()
)
cospfLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLocalLsdbType.setStatus("current")
_CospfLocalLsdbLsid_Type = IpAddress
_CospfLocalLsdbLsid_Object = MibTableColumn
cospfLocalLsdbLsid = _CospfLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 4),
    _CospfLocalLsdbLsid_Type()
)
cospfLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLocalLsdbLsid.setStatus("current")
_CospfLocalLsdbRouterId_Type = RouterID
_CospfLocalLsdbRouterId_Object = MibTableColumn
cospfLocalLsdbRouterId = _CospfLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 5),
    _CospfLocalLsdbRouterId_Type()
)
cospfLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfLocalLsdbRouterId.setStatus("current")


class _CospfLocalLsdbSequence_Type(Integer32):
    """Custom type cospfLocalLsdbSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CospfLocalLsdbSequence_Type.__name__ = "Integer32"
_CospfLocalLsdbSequence_Object = MibTableColumn
cospfLocalLsdbSequence = _CospfLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 6),
    _CospfLocalLsdbSequence_Type()
)
cospfLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLocalLsdbSequence.setStatus("current")


class _CospfLocalLsdbAge_Type(Integer32):
    """Custom type cospfLocalLsdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CospfLocalLsdbAge_Type.__name__ = "Integer32"
_CospfLocalLsdbAge_Object = MibTableColumn
cospfLocalLsdbAge = _CospfLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 7),
    _CospfLocalLsdbAge_Type()
)
cospfLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLocalLsdbAge.setStatus("current")


class _CospfLocalLsdbChecksum_Type(Unsigned32):
    """Custom type cospfLocalLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfLocalLsdbChecksum_Type.__name__ = "Unsigned32"
_CospfLocalLsdbChecksum_Object = MibTableColumn
cospfLocalLsdbChecksum = _CospfLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 8),
    _CospfLocalLsdbChecksum_Type()
)
cospfLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLocalLsdbChecksum.setStatus("current")


class _CospfLocalLsdbAdvertisement_Type(OctetString):
    """Custom type cospfLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_CospfLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_CospfLocalLsdbAdvertisement_Object = MibTableColumn
cospfLocalLsdbAdvertisement = _CospfLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 7, 1, 9),
    _CospfLocalLsdbAdvertisement_Type()
)
cospfLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfLocalLsdbAdvertisement.setStatus("current")
_CospfVirtLocalLsdbTable_Object = MibTable
cospfVirtLocalLsdbTable = _CospfVirtLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8)
)
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbTable.setStatus("current")
_CospfVirtLocalLsdbEntry_Object = MibTableRow
cospfVirtLocalLsdbEntry = _CospfVirtLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1)
)
cospfVirtLocalLsdbEntry.setIndexNames(
    (0, "CISCO-OSPF-MIB", "cospfVirtLocalLsdbTransitArea"),
    (0, "CISCO-OSPF-MIB", "cospfVirtLocalLsdbNeighbor"),
    (0, "CISCO-OSPF-MIB", "cospfVirtLocalLsdbType"),
    (0, "CISCO-OSPF-MIB", "cospfVirtLocalLsdbLsid"),
    (0, "CISCO-OSPF-MIB", "cospfVirtLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbEntry.setStatus("current")
_CospfVirtLocalLsdbTransitArea_Type = AreaID
_CospfVirtLocalLsdbTransitArea_Object = MibTableColumn
cospfVirtLocalLsdbTransitArea = _CospfVirtLocalLsdbTransitArea_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 1),
    _CospfVirtLocalLsdbTransitArea_Type()
)
cospfVirtLocalLsdbTransitArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbTransitArea.setStatus("current")
_CospfVirtLocalLsdbNeighbor_Type = RouterID
_CospfVirtLocalLsdbNeighbor_Object = MibTableColumn
cospfVirtLocalLsdbNeighbor = _CospfVirtLocalLsdbNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 2),
    _CospfVirtLocalLsdbNeighbor_Type()
)
cospfVirtLocalLsdbNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbNeighbor.setStatus("current")


class _CospfVirtLocalLsdbType_Type(Integer32):
    """Custom type cospfVirtLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_CospfVirtLocalLsdbType_Type.__name__ = "Integer32"
_CospfVirtLocalLsdbType_Object = MibTableColumn
cospfVirtLocalLsdbType = _CospfVirtLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 3),
    _CospfVirtLocalLsdbType_Type()
)
cospfVirtLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbType.setStatus("current")
_CospfVirtLocalLsdbLsid_Type = IpAddress
_CospfVirtLocalLsdbLsid_Object = MibTableColumn
cospfVirtLocalLsdbLsid = _CospfVirtLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 4),
    _CospfVirtLocalLsdbLsid_Type()
)
cospfVirtLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbLsid.setStatus("current")
_CospfVirtLocalLsdbRouterId_Type = RouterID
_CospfVirtLocalLsdbRouterId_Object = MibTableColumn
cospfVirtLocalLsdbRouterId = _CospfVirtLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 5),
    _CospfVirtLocalLsdbRouterId_Type()
)
cospfVirtLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbRouterId.setStatus("current")


class _CospfVirtLocalLsdbSequence_Type(Integer32):
    """Custom type cospfVirtLocalLsdbSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CospfVirtLocalLsdbSequence_Type.__name__ = "Integer32"
_CospfVirtLocalLsdbSequence_Object = MibTableColumn
cospfVirtLocalLsdbSequence = _CospfVirtLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 6),
    _CospfVirtLocalLsdbSequence_Type()
)
cospfVirtLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbSequence.setStatus("current")


class _CospfVirtLocalLsdbAge_Type(Integer32):
    """Custom type cospfVirtLocalLsdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CospfVirtLocalLsdbAge_Type.__name__ = "Integer32"
_CospfVirtLocalLsdbAge_Object = MibTableColumn
cospfVirtLocalLsdbAge = _CospfVirtLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 7),
    _CospfVirtLocalLsdbAge_Type()
)
cospfVirtLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbAge.setStatus("current")


class _CospfVirtLocalLsdbChecksum_Type(Unsigned32):
    """Custom type cospfVirtLocalLsdbChecksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CospfVirtLocalLsdbChecksum_Type.__name__ = "Unsigned32"
_CospfVirtLocalLsdbChecksum_Object = MibTableColumn
cospfVirtLocalLsdbChecksum = _CospfVirtLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 8),
    _CospfVirtLocalLsdbChecksum_Type()
)
cospfVirtLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbChecksum.setStatus("current")


class _CospfVirtLocalLsdbAdvertisement_Type(OctetString):
    """Custom type cospfVirtLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_CospfVirtLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_CospfVirtLocalLsdbAdvertisement_Object = MibTableColumn
cospfVirtLocalLsdbAdvertisement = _CospfVirtLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 8, 1, 9),
    _CospfVirtLocalLsdbAdvertisement_Type()
)
cospfVirtLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbAdvertisement.setStatus("current")
_CospfConformance_ObjectIdentity = ObjectIdentity
cospfConformance = _CospfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9)
)
_CospfGroups_ObjectIdentity = ObjectIdentity
cospfGroups = _CospfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1)
)
_CospfCompliances_ObjectIdentity = ObjectIdentity
cospfCompliances = _CospfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 2)
)
_CospfShamLinkNbrTable_Object = MibTable
cospfShamLinkNbrTable = _CospfShamLinkNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10)
)
if mibBuilder.loadTexts:
    cospfShamLinkNbrTable.setStatus("current")
_CospfShamLinkNbrEntry_Object = MibTableRow
cospfShamLinkNbrEntry = _CospfShamLinkNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1)
)
cospfShamLinkNbrEntry.setIndexNames(
    (0, "CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinkNbrArea"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddrType"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddr"),
)
if mibBuilder.loadTexts:
    cospfShamLinkNbrEntry.setStatus("current")
_CospfShamLinkNbrArea_Type = AreaID
_CospfShamLinkNbrArea_Object = MibTableColumn
cospfShamLinkNbrArea = _CospfShamLinkNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 1),
    _CospfShamLinkNbrArea_Type()
)
cospfShamLinkNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkNbrArea.setStatus("current")
_CospfShamLinkNbrIpAddrType_Type = InetAddressType
_CospfShamLinkNbrIpAddrType_Object = MibTableColumn
cospfShamLinkNbrIpAddrType = _CospfShamLinkNbrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 2),
    _CospfShamLinkNbrIpAddrType_Type()
)
cospfShamLinkNbrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkNbrIpAddrType.setStatus("current")
_CospfShamLinkNbrIpAddr_Type = InetAddress
_CospfShamLinkNbrIpAddr_Object = MibTableColumn
cospfShamLinkNbrIpAddr = _CospfShamLinkNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 3),
    _CospfShamLinkNbrIpAddr_Type()
)
cospfShamLinkNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinkNbrIpAddr.setStatus("current")
_CospfShamLinkNbrRtrId_Type = RouterID
_CospfShamLinkNbrRtrId_Object = MibTableColumn
cospfShamLinkNbrRtrId = _CospfShamLinkNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 4),
    _CospfShamLinkNbrRtrId_Type()
)
cospfShamLinkNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrRtrId.setStatus("current")


class _CospfShamLinkNbrOptions_Type(Integer32):
    """Custom type cospfShamLinkNbrOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CospfShamLinkNbrOptions_Type.__name__ = "Integer32"
_CospfShamLinkNbrOptions_Object = MibTableColumn
cospfShamLinkNbrOptions = _CospfShamLinkNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 5),
    _CospfShamLinkNbrOptions_Type()
)
cospfShamLinkNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrOptions.setStatus("current")


class _CospfShamLinkNbrState_Type(Integer32):
    """Custom type cospfShamLinkNbrState based on Integer32"""
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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_CospfShamLinkNbrState_Type.__name__ = "Integer32"
_CospfShamLinkNbrState_Object = MibTableColumn
cospfShamLinkNbrState = _CospfShamLinkNbrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 6),
    _CospfShamLinkNbrState_Type()
)
cospfShamLinkNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrState.setStatus("current")
_CospfShamLinkNbrEvents_Type = Counter32
_CospfShamLinkNbrEvents_Object = MibTableColumn
cospfShamLinkNbrEvents = _CospfShamLinkNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 7),
    _CospfShamLinkNbrEvents_Type()
)
cospfShamLinkNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrEvents.setStatus("current")
_CospfShamLinkNbrLsRetransQLen_Type = Gauge32
_CospfShamLinkNbrLsRetransQLen_Object = MibTableColumn
cospfShamLinkNbrLsRetransQLen = _CospfShamLinkNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 8),
    _CospfShamLinkNbrLsRetransQLen_Type()
)
cospfShamLinkNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrLsRetransQLen.setStatus("current")
_CospfShamLinkNbrHelloSuppressed_Type = TruthValue
_CospfShamLinkNbrHelloSuppressed_Object = MibTableColumn
cospfShamLinkNbrHelloSuppressed = _CospfShamLinkNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 10, 1, 9),
    _CospfShamLinkNbrHelloSuppressed_Type()
)
cospfShamLinkNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinkNbrHelloSuppressed.setStatus("current")
_CospfShamLinksTable_Object = MibTable
cospfShamLinksTable = _CospfShamLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11)
)
if mibBuilder.loadTexts:
    cospfShamLinksTable.setStatus("current")
_CospfShamLinksEntry_Object = MibTableRow
cospfShamLinksEntry = _CospfShamLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1)
)
cospfShamLinksEntry.setIndexNames(
    (0, "CISCO-OSPF-MIB", "cospfShamLinksAreaId"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"),
    (0, "CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    cospfShamLinksEntry.setStatus("current")
_CospfShamLinksAreaId_Type = AreaID
_CospfShamLinksAreaId_Object = MibTableColumn
cospfShamLinksAreaId = _CospfShamLinksAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 1),
    _CospfShamLinksAreaId_Type()
)
cospfShamLinksAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinksAreaId.setStatus("current")
_CospfShamLinksLocalIpAddrType_Type = InetAddressType
_CospfShamLinksLocalIpAddrType_Object = MibTableColumn
cospfShamLinksLocalIpAddrType = _CospfShamLinksLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 2),
    _CospfShamLinksLocalIpAddrType_Type()
)
cospfShamLinksLocalIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinksLocalIpAddrType.setStatus("current")
_CospfShamLinksLocalIpAddr_Type = InetAddress
_CospfShamLinksLocalIpAddr_Object = MibTableColumn
cospfShamLinksLocalIpAddr = _CospfShamLinksLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 3),
    _CospfShamLinksLocalIpAddr_Type()
)
cospfShamLinksLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinksLocalIpAddr.setStatus("current")
_CospfShamLinksRemoteIpAddrType_Type = InetAddressType
_CospfShamLinksRemoteIpAddrType_Object = MibTableColumn
cospfShamLinksRemoteIpAddrType = _CospfShamLinksRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 4),
    _CospfShamLinksRemoteIpAddrType_Type()
)
cospfShamLinksRemoteIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinksRemoteIpAddrType.setStatus("current")
_CospfShamLinksRemoteIpAddr_Type = InetAddress
_CospfShamLinksRemoteIpAddr_Object = MibTableColumn
cospfShamLinksRemoteIpAddr = _CospfShamLinksRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 5),
    _CospfShamLinksRemoteIpAddr_Type()
)
cospfShamLinksRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cospfShamLinksRemoteIpAddr.setStatus("current")


class _CospfShamLinksRetransInterval_Type(UpToMaxAge):
    """Custom type cospfShamLinksRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_CospfShamLinksRetransInterval_Object = MibTableColumn
cospfShamLinksRetransInterval = _CospfShamLinksRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 6),
    _CospfShamLinksRetransInterval_Type()
)
cospfShamLinksRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksRetransInterval.setStatus("current")


class _CospfShamLinksHelloInterval_Type(HelloRange):
    """Custom type cospfShamLinksHelloInterval based on HelloRange"""
    defaultValue = 10


_CospfShamLinksHelloInterval_Object = MibTableColumn
cospfShamLinksHelloInterval = _CospfShamLinksHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 7),
    _CospfShamLinksHelloInterval_Type()
)
cospfShamLinksHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksHelloInterval.setStatus("current")


class _CospfShamLinksRtrDeadInterval_Type(PositiveInteger):
    """Custom type cospfShamLinksRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_CospfShamLinksRtrDeadInterval_Object = MibTableColumn
cospfShamLinksRtrDeadInterval = _CospfShamLinksRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 8),
    _CospfShamLinksRtrDeadInterval_Type()
)
cospfShamLinksRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksRtrDeadInterval.setStatus("current")


class _CospfShamLinksState_Type(Integer32):
    """Custom type cospfShamLinksState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_CospfShamLinksState_Type.__name__ = "Integer32"
_CospfShamLinksState_Object = MibTableColumn
cospfShamLinksState = _CospfShamLinksState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 9),
    _CospfShamLinksState_Type()
)
cospfShamLinksState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksState.setStatus("current")
_CospfShamLinksEvents_Type = Counter32
_CospfShamLinksEvents_Object = MibTableColumn
cospfShamLinksEvents = _CospfShamLinksEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 10),
    _CospfShamLinksEvents_Type()
)
cospfShamLinksEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksEvents.setStatus("current")
_CospfShamLinksMetric_Type = Metric
_CospfShamLinksMetric_Object = MibTableColumn
cospfShamLinksMetric = _CospfShamLinksMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 11, 1, 11),
    _CospfShamLinksMetric_Type()
)
cospfShamLinksMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cospfShamLinksMetric.setStatus("current")
ospfAreaEntry.registerAugmentions(
    ("CISCO-OSPF-MIB",
     "cospfAreaEntry")
)
cospfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("CISCO-OSPF-MIB",
     "cospfIfEntry")
)
cospfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("CISCO-OSPF-MIB",
     "cospfVirtIfEntry")
)
cospfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups

cospfLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 1)
)
cospfLsdbGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfLsdbSequence"),
        ("CISCO-OSPF-MIB", "cospfLsdbAge"),
        ("CISCO-OSPF-MIB", "cospfLsdbChecksum"),
        ("CISCO-OSPF-MIB", "cospfLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    cospfLsdbGroup.setStatus("current")

cospfLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 2)
)
cospfLocalLsdbGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfLocalLsdbSequence"),
        ("CISCO-OSPF-MIB", "cospfLocalLsdbAge"),
        ("CISCO-OSPF-MIB", "cospfLocalLsdbChecksum"),
        ("CISCO-OSPF-MIB", "cospfLocalLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    cospfLocalLsdbGroup.setStatus("current")

cospfVirtLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 3)
)
cospfVirtLocalLsdbGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfVirtLocalLsdbSequence"),
        ("CISCO-OSPF-MIB", "cospfVirtLocalLsdbAge"),
        ("CISCO-OSPF-MIB", "cospfVirtLocalLsdbChecksum"),
        ("CISCO-OSPF-MIB", "cospfVirtLocalLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    cospfVirtLocalLsdbGroup.setStatus("current")

cospfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 4)
)
cospfBasicGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfRFC1583Compatibility"),
        ("CISCO-OSPF-MIB", "cospfOpaqueLsaSupport"),
        ("CISCO-OSPF-MIB", "cospfTrafficEngineeringSupport"),
        ("CISCO-OSPF-MIB", "cospfOpaqueASLsaCount"),
        ("CISCO-OSPF-MIB", "cospfOpaqueASLsaCksumSum"))
)
if mibBuilder.loadTexts:
    cospfBasicGroup.setStatus("current")

cospfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 5)
)
cospfAreaGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfOpaqueAreaLsaCount"),
        ("CISCO-OSPF-MIB", "cospfOpaqueAreaLsaCksumSum"),
        ("CISCO-OSPF-MIB", "cospfAreaNssaTranslatorRole"),
        ("CISCO-OSPF-MIB", "cospfAreaNssaTranslatorState"),
        ("CISCO-OSPF-MIB", "cospfAreaNssaTranslatorEvents"))
)
if mibBuilder.loadTexts:
    cospfAreaGroup.setStatus("current")

cospfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 6)
)
cospfIfGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfIfLsaCount"),
        ("CISCO-OSPF-MIB", "cospfIfLsaCksumSum"))
)
if mibBuilder.loadTexts:
    cospfIfGroup.setStatus("current")

cospfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 7)
)
cospfVirtIfGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfVirtIfLsaCount"),
        ("CISCO-OSPF-MIB", "cospfVirtIfLsaCksumSum"))
)
if mibBuilder.loadTexts:
    cospfVirtIfGroup.setStatus("current")

cospfShamLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 8)
)
cospfShamLinkGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfShamLinkRetransInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinkHelloInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinkRtrDeadInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinkState"),
        ("CISCO-OSPF-MIB", "cospfShamLinkEvents"),
        ("CISCO-OSPF-MIB", "cospfShamLinkMetric"))
)
if mibBuilder.loadTexts:
    cospfShamLinkGroup.setStatus("deprecated")

cospfShamLinkNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 9)
)
cospfShamLinkNbrGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfShamLinkNbrRtrId"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrOptions"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrState"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrEvents"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrLsRetransQLen"),
        ("CISCO-OSPF-MIB", "cospfShamLinkNbrHelloSuppressed"))
)
if mibBuilder.loadTexts:
    cospfShamLinkNbrGroup.setStatus("current")

cospfShamLinksGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 1, 10)
)
cospfShamLinksGroup.setObjects(
      *(("CISCO-OSPF-MIB", "cospfShamLinksRetransInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinksHelloInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinksRtrDeadInterval"),
        ("CISCO-OSPF-MIB", "cospfShamLinksState"),
        ("CISCO-OSPF-MIB", "cospfShamLinksEvents"),
        ("CISCO-OSPF-MIB", "cospfShamLinksMetric"))
)
if mibBuilder.loadTexts:
    cospfShamLinksGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cospfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 2, 1)
)
if mibBuilder.loadTexts:
    cospfCompliance.setStatus(
        "deprecated"
    )

cospfComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 99, 9, 2, 2)
)
if mibBuilder.loadTexts:
    cospfComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OSPF-MIB",
    **{"cospf": cospf,
       "cospfGeneralGroup": cospfGeneralGroup,
       "cospfRFC1583Compatibility": cospfRFC1583Compatibility,
       "cospfOpaqueLsaSupport": cospfOpaqueLsaSupport,
       "cospfTrafficEngineeringSupport": cospfTrafficEngineeringSupport,
       "cospfOpaqueASLsaCount": cospfOpaqueASLsaCount,
       "cospfOpaqueASLsaCksumSum": cospfOpaqueASLsaCksumSum,
       "cospfAreaTable": cospfAreaTable,
       "cospfAreaEntry": cospfAreaEntry,
       "cospfOpaqueAreaLsaCount": cospfOpaqueAreaLsaCount,
       "cospfOpaqueAreaLsaCksumSum": cospfOpaqueAreaLsaCksumSum,
       "cospfAreaNssaTranslatorRole": cospfAreaNssaTranslatorRole,
       "cospfAreaNssaTranslatorState": cospfAreaNssaTranslatorState,
       "cospfAreaNssaTranslatorEvents": cospfAreaNssaTranslatorEvents,
       "cospfLsdbTable": cospfLsdbTable,
       "cospfLsdbEntry": cospfLsdbEntry,
       "cospfLsdbType": cospfLsdbType,
       "cospfLsdbSequence": cospfLsdbSequence,
       "cospfLsdbAge": cospfLsdbAge,
       "cospfLsdbChecksum": cospfLsdbChecksum,
       "cospfLsdbAdvertisement": cospfLsdbAdvertisement,
       "cospfIfTable": cospfIfTable,
       "cospfIfEntry": cospfIfEntry,
       "cospfIfLsaCount": cospfIfLsaCount,
       "cospfIfLsaCksumSum": cospfIfLsaCksumSum,
       "cospfVirtIfTable": cospfVirtIfTable,
       "cospfVirtIfEntry": cospfVirtIfEntry,
       "cospfVirtIfLsaCount": cospfVirtIfLsaCount,
       "cospfVirtIfLsaCksumSum": cospfVirtIfLsaCksumSum,
       "cospfShamLinkTable": cospfShamLinkTable,
       "cospfShamLinkEntry": cospfShamLinkEntry,
       "cospfShamLinkAreaId": cospfShamLinkAreaId,
       "cospfShamLinkLocalIpAddress": cospfShamLinkLocalIpAddress,
       "cospfShamLinkNeighborId": cospfShamLinkNeighborId,
       "cospfShamLinkRetransInterval": cospfShamLinkRetransInterval,
       "cospfShamLinkHelloInterval": cospfShamLinkHelloInterval,
       "cospfShamLinkRtrDeadInterval": cospfShamLinkRtrDeadInterval,
       "cospfShamLinkState": cospfShamLinkState,
       "cospfShamLinkEvents": cospfShamLinkEvents,
       "cospfShamLinkMetric": cospfShamLinkMetric,
       "cospfLocalLsdbTable": cospfLocalLsdbTable,
       "cospfLocalLsdbEntry": cospfLocalLsdbEntry,
       "cospfLocalLsdbIpAddress": cospfLocalLsdbIpAddress,
       "cospfLocalLsdbAddressLessIf": cospfLocalLsdbAddressLessIf,
       "cospfLocalLsdbType": cospfLocalLsdbType,
       "cospfLocalLsdbLsid": cospfLocalLsdbLsid,
       "cospfLocalLsdbRouterId": cospfLocalLsdbRouterId,
       "cospfLocalLsdbSequence": cospfLocalLsdbSequence,
       "cospfLocalLsdbAge": cospfLocalLsdbAge,
       "cospfLocalLsdbChecksum": cospfLocalLsdbChecksum,
       "cospfLocalLsdbAdvertisement": cospfLocalLsdbAdvertisement,
       "cospfVirtLocalLsdbTable": cospfVirtLocalLsdbTable,
       "cospfVirtLocalLsdbEntry": cospfVirtLocalLsdbEntry,
       "cospfVirtLocalLsdbTransitArea": cospfVirtLocalLsdbTransitArea,
       "cospfVirtLocalLsdbNeighbor": cospfVirtLocalLsdbNeighbor,
       "cospfVirtLocalLsdbType": cospfVirtLocalLsdbType,
       "cospfVirtLocalLsdbLsid": cospfVirtLocalLsdbLsid,
       "cospfVirtLocalLsdbRouterId": cospfVirtLocalLsdbRouterId,
       "cospfVirtLocalLsdbSequence": cospfVirtLocalLsdbSequence,
       "cospfVirtLocalLsdbAge": cospfVirtLocalLsdbAge,
       "cospfVirtLocalLsdbChecksum": cospfVirtLocalLsdbChecksum,
       "cospfVirtLocalLsdbAdvertisement": cospfVirtLocalLsdbAdvertisement,
       "cospfConformance": cospfConformance,
       "cospfGroups": cospfGroups,
       "cospfLsdbGroup": cospfLsdbGroup,
       "cospfLocalLsdbGroup": cospfLocalLsdbGroup,
       "cospfVirtLocalLsdbGroup": cospfVirtLocalLsdbGroup,
       "cospfBasicGroup": cospfBasicGroup,
       "cospfAreaGroup": cospfAreaGroup,
       "cospfIfGroup": cospfIfGroup,
       "cospfVirtIfGroup": cospfVirtIfGroup,
       "cospfShamLinkGroup": cospfShamLinkGroup,
       "cospfShamLinkNbrGroup": cospfShamLinkNbrGroup,
       "cospfShamLinksGroup": cospfShamLinksGroup,
       "cospfCompliances": cospfCompliances,
       "cospfCompliance": cospfCompliance,
       "cospfComplianceRev1": cospfComplianceRev1,
       "cospfShamLinkNbrTable": cospfShamLinkNbrTable,
       "cospfShamLinkNbrEntry": cospfShamLinkNbrEntry,
       "cospfShamLinkNbrArea": cospfShamLinkNbrArea,
       "cospfShamLinkNbrIpAddrType": cospfShamLinkNbrIpAddrType,
       "cospfShamLinkNbrIpAddr": cospfShamLinkNbrIpAddr,
       "cospfShamLinkNbrRtrId": cospfShamLinkNbrRtrId,
       "cospfShamLinkNbrOptions": cospfShamLinkNbrOptions,
       "cospfShamLinkNbrState": cospfShamLinkNbrState,
       "cospfShamLinkNbrEvents": cospfShamLinkNbrEvents,
       "cospfShamLinkNbrLsRetransQLen": cospfShamLinkNbrLsRetransQLen,
       "cospfShamLinkNbrHelloSuppressed": cospfShamLinkNbrHelloSuppressed,
       "cospfShamLinksTable": cospfShamLinksTable,
       "cospfShamLinksEntry": cospfShamLinksEntry,
       "cospfShamLinksAreaId": cospfShamLinksAreaId,
       "cospfShamLinksLocalIpAddrType": cospfShamLinksLocalIpAddrType,
       "cospfShamLinksLocalIpAddr": cospfShamLinksLocalIpAddr,
       "cospfShamLinksRemoteIpAddrType": cospfShamLinksRemoteIpAddrType,
       "cospfShamLinksRemoteIpAddr": cospfShamLinksRemoteIpAddr,
       "cospfShamLinksRetransInterval": cospfShamLinksRetransInterval,
       "cospfShamLinksHelloInterval": cospfShamLinksHelloInterval,
       "cospfShamLinksRtrDeadInterval": cospfShamLinksRtrDeadInterval,
       "cospfShamLinksState": cospfShamLinksState,
       "cospfShamLinksEvents": cospfShamLinksEvents,
       "cospfShamLinksMetric": cospfShamLinksMetric}
)
