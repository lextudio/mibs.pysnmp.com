# SNMP MIB module (RADLAN-OSPFV3-LSDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-OSPFV3-LSDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:50 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(AreaID,
 RouterID) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "RouterID")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(RlOspfProcessID,) = mibBuilder.importSymbols(
    "RADLAN-OSPF-MIB",
    "RlOspfProcessID")

(rlOspfv3,) = mibBuilder.importSymbols(
    "RADLAN-OSPFV3-MIB",
    "rlOspfv3")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

rlOspfv3Lsdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 222)
)
rlOspfv3Lsdb.setRevisions(
        ("2011-05-04 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlOspfv3RouterLsaTable_Object = MibTable
rlOspfv3RouterLsaTable = _RlOspfv3RouterLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1)
)
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaTable.setStatus("current")
_RlOspfv3RouterLsaEntry_Object = MibTableRow
rlOspfv3RouterLsaEntry = _RlOspfv3RouterLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1)
)
rlOspfv3RouterLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaRouterId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaEntry.setStatus("current")
_RlOspfv3RouterLsaProcessId_Type = RlOspfProcessID
_RlOspfv3RouterLsaProcessId_Object = MibTableColumn
rlOspfv3RouterLsaProcessId = _RlOspfv3RouterLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 1),
    _RlOspfv3RouterLsaProcessId_Type()
)
rlOspfv3RouterLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaProcessId.setStatus("current")
_RlOspfv3RouterLsaAreaId_Type = AreaID
_RlOspfv3RouterLsaAreaId_Object = MibTableColumn
rlOspfv3RouterLsaAreaId = _RlOspfv3RouterLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 2),
    _RlOspfv3RouterLsaAreaId_Type()
)
rlOspfv3RouterLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaAreaId.setStatus("current")
_RlOspfv3RouterLsaLsid_Type = IpAddress
_RlOspfv3RouterLsaLsid_Object = MibTableColumn
rlOspfv3RouterLsaLsid = _RlOspfv3RouterLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 3),
    _RlOspfv3RouterLsaLsid_Type()
)
rlOspfv3RouterLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaLsid.setStatus("current")
_RlOspfv3RouterLsaRouterId_Type = RouterID
_RlOspfv3RouterLsaRouterId_Object = MibTableColumn
rlOspfv3RouterLsaRouterId = _RlOspfv3RouterLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 4),
    _RlOspfv3RouterLsaRouterId_Type()
)
rlOspfv3RouterLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaRouterId.setStatus("current")


class _RlOspfv3RouterLsaIdx_Type(Unsigned32):
    """Custom type rlOspfv3RouterLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3RouterLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfv3RouterLsaIdx_Object = MibTableColumn
rlOspfv3RouterLsaIdx = _RlOspfv3RouterLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 5),
    _RlOspfv3RouterLsaIdx_Type()
)
rlOspfv3RouterLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaIdx.setStatus("current")


class _RlOspfv3RouterLsaCount_Type(Unsigned32):
    """Custom type rlOspfv3RouterLsaCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3RouterLsaCount_Type.__name__ = "Unsigned32"
_RlOspfv3RouterLsaCount_Object = MibTableColumn
rlOspfv3RouterLsaCount = _RlOspfv3RouterLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 6),
    _RlOspfv3RouterLsaCount_Type()
)
rlOspfv3RouterLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaCount.setStatus("current")
_RlOspfv3RouterLsaSequence_Type = Integer32
_RlOspfv3RouterLsaSequence_Object = MibTableColumn
rlOspfv3RouterLsaSequence = _RlOspfv3RouterLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 7),
    _RlOspfv3RouterLsaSequence_Type()
)
rlOspfv3RouterLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaSequence.setStatus("current")
_RlOspfv3RouterLsaAge_Type = Integer32
_RlOspfv3RouterLsaAge_Object = MibTableColumn
rlOspfv3RouterLsaAge = _RlOspfv3RouterLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 8),
    _RlOspfv3RouterLsaAge_Type()
)
rlOspfv3RouterLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaAge.setStatus("current")
_RlOspfv3RouterLsaChecksum_Type = Integer32
_RlOspfv3RouterLsaChecksum_Object = MibTableColumn
rlOspfv3RouterLsaChecksum = _RlOspfv3RouterLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 9),
    _RlOspfv3RouterLsaChecksum_Type()
)
rlOspfv3RouterLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaChecksum.setStatus("current")
_RlOspfv3RouterLsaLength_Type = Unsigned32
_RlOspfv3RouterLsaLength_Object = MibTableColumn
rlOspfv3RouterLsaLength = _RlOspfv3RouterLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 10),
    _RlOspfv3RouterLsaLength_Type()
)
rlOspfv3RouterLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaLength.setStatus("current")


class _RlOspfv3RouterLsaBitW_Type(Integer32):
    """Custom type rlOspfv3RouterLsaBitW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3RouterLsaBitW_Type.__name__ = "Integer32"
_RlOspfv3RouterLsaBitW_Object = MibTableColumn
rlOspfv3RouterLsaBitW = _RlOspfv3RouterLsaBitW_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 11),
    _RlOspfv3RouterLsaBitW_Type()
)
rlOspfv3RouterLsaBitW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaBitW.setStatus("current")


class _RlOspfv3RouterLsaBitV_Type(Integer32):
    """Custom type rlOspfv3RouterLsaBitV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3RouterLsaBitV_Type.__name__ = "Integer32"
_RlOspfv3RouterLsaBitV_Object = MibTableColumn
rlOspfv3RouterLsaBitV = _RlOspfv3RouterLsaBitV_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 12),
    _RlOspfv3RouterLsaBitV_Type()
)
rlOspfv3RouterLsaBitV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaBitV.setStatus("current")


class _RlOspfv3RouterLsaBitE_Type(Integer32):
    """Custom type rlOspfv3RouterLsaBitE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3RouterLsaBitE_Type.__name__ = "Integer32"
_RlOspfv3RouterLsaBitE_Object = MibTableColumn
rlOspfv3RouterLsaBitE = _RlOspfv3RouterLsaBitE_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 13),
    _RlOspfv3RouterLsaBitE_Type()
)
rlOspfv3RouterLsaBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaBitE.setStatus("current")


class _RlOspfv3RouterLsaBitB_Type(Integer32):
    """Custom type rlOspfv3RouterLsaBitB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3RouterLsaBitB_Type.__name__ = "Integer32"
_RlOspfv3RouterLsaBitB_Object = MibTableColumn
rlOspfv3RouterLsaBitB = _RlOspfv3RouterLsaBitB_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 14),
    _RlOspfv3RouterLsaBitB_Type()
)
rlOspfv3RouterLsaBitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaBitB.setStatus("current")
_RlOspfv3RouterLsaOptions_Type = Unsigned32
_RlOspfv3RouterLsaOptions_Object = MibTableColumn
rlOspfv3RouterLsaOptions = _RlOspfv3RouterLsaOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 15),
    _RlOspfv3RouterLsaOptions_Type()
)
rlOspfv3RouterLsaOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaOptions.setStatus("current")


class _RlOspfv3RouterLsaType_Type(Integer32):
    """Custom type rlOspfv3RouterLsaType based on Integer32"""
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
        *(("pointToPoint", 1),
          ("stubNetwork", 3),
          ("transitNetwork", 2),
          ("virtualLink", 4))
    )


_RlOspfv3RouterLsaType_Type.__name__ = "Integer32"
_RlOspfv3RouterLsaType_Object = MibTableColumn
rlOspfv3RouterLsaType = _RlOspfv3RouterLsaType_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 16),
    _RlOspfv3RouterLsaType_Type()
)
rlOspfv3RouterLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaType.setStatus("current")
_RlOspfv3RouterLsaMetric_Type = Unsigned32
_RlOspfv3RouterLsaMetric_Object = MibTableColumn
rlOspfv3RouterLsaMetric = _RlOspfv3RouterLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 17),
    _RlOspfv3RouterLsaMetric_Type()
)
rlOspfv3RouterLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaMetric.setStatus("current")
_RlOspfv3RouterLsaInterfaceID_Type = Unsigned32
_RlOspfv3RouterLsaInterfaceID_Object = MibTableColumn
rlOspfv3RouterLsaInterfaceID = _RlOspfv3RouterLsaInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 18),
    _RlOspfv3RouterLsaInterfaceID_Type()
)
rlOspfv3RouterLsaInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaInterfaceID.setStatus("current")
_RlOspfv3RouterLsaNeighborInterfaceID_Type = Unsigned32
_RlOspfv3RouterLsaNeighborInterfaceID_Object = MibTableColumn
rlOspfv3RouterLsaNeighborInterfaceID = _RlOspfv3RouterLsaNeighborInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 19),
    _RlOspfv3RouterLsaNeighborInterfaceID_Type()
)
rlOspfv3RouterLsaNeighborInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaNeighborInterfaceID.setStatus("current")
_RlOspfv3RouterLsaNeighborRouterID_Type = RouterID
_RlOspfv3RouterLsaNeighborRouterID_Object = MibTableColumn
rlOspfv3RouterLsaNeighborRouterID = _RlOspfv3RouterLsaNeighborRouterID_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 20),
    _RlOspfv3RouterLsaNeighborRouterID_Type()
)
rlOspfv3RouterLsaNeighborRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3RouterLsaNeighborRouterID.setStatus("current")
_RlOspfv3NetworkLsaTable_Object = MibTable
rlOspfv3NetworkLsaTable = _RlOspfv3NetworkLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2)
)
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaTable.setStatus("current")
_RlOspfv3NetworkLsaEntry_Object = MibTableRow
rlOspfv3NetworkLsaEntry = _RlOspfv3NetworkLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1)
)
rlOspfv3NetworkLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaRouterId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaEntry.setStatus("current")
_RlOspfv3NetworkLsaProcessId_Type = RlOspfProcessID
_RlOspfv3NetworkLsaProcessId_Object = MibTableColumn
rlOspfv3NetworkLsaProcessId = _RlOspfv3NetworkLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 1),
    _RlOspfv3NetworkLsaProcessId_Type()
)
rlOspfv3NetworkLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaProcessId.setStatus("current")
_RlOspfv3NetworkLsaAreaId_Type = AreaID
_RlOspfv3NetworkLsaAreaId_Object = MibTableColumn
rlOspfv3NetworkLsaAreaId = _RlOspfv3NetworkLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 2),
    _RlOspfv3NetworkLsaAreaId_Type()
)
rlOspfv3NetworkLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaAreaId.setStatus("current")
_RlOspfv3NetworkLsaLsid_Type = IpAddress
_RlOspfv3NetworkLsaLsid_Object = MibTableColumn
rlOspfv3NetworkLsaLsid = _RlOspfv3NetworkLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 3),
    _RlOspfv3NetworkLsaLsid_Type()
)
rlOspfv3NetworkLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaLsid.setStatus("current")
_RlOspfv3NetworkLsaRouterId_Type = RouterID
_RlOspfv3NetworkLsaRouterId_Object = MibTableColumn
rlOspfv3NetworkLsaRouterId = _RlOspfv3NetworkLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 4),
    _RlOspfv3NetworkLsaRouterId_Type()
)
rlOspfv3NetworkLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaRouterId.setStatus("current")


class _RlOspfv3NetworkLsaIdx_Type(Unsigned32):
    """Custom type rlOspfv3NetworkLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3NetworkLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfv3NetworkLsaIdx_Object = MibTableColumn
rlOspfv3NetworkLsaIdx = _RlOspfv3NetworkLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 5),
    _RlOspfv3NetworkLsaIdx_Type()
)
rlOspfv3NetworkLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaIdx.setStatus("current")


class _RlOspfv3NetworkLsaCount_Type(Unsigned32):
    """Custom type rlOspfv3NetworkLsaCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3NetworkLsaCount_Type.__name__ = "Unsigned32"
_RlOspfv3NetworkLsaCount_Object = MibTableColumn
rlOspfv3NetworkLsaCount = _RlOspfv3NetworkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 6),
    _RlOspfv3NetworkLsaCount_Type()
)
rlOspfv3NetworkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaCount.setStatus("current")
_RlOspfv3NetworkLsaSequence_Type = Integer32
_RlOspfv3NetworkLsaSequence_Object = MibTableColumn
rlOspfv3NetworkLsaSequence = _RlOspfv3NetworkLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 7),
    _RlOspfv3NetworkLsaSequence_Type()
)
rlOspfv3NetworkLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaSequence.setStatus("current")
_RlOspfv3NetworkLsaAge_Type = Integer32
_RlOspfv3NetworkLsaAge_Object = MibTableColumn
rlOspfv3NetworkLsaAge = _RlOspfv3NetworkLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 8),
    _RlOspfv3NetworkLsaAge_Type()
)
rlOspfv3NetworkLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaAge.setStatus("current")
_RlOspfv3NetworkLsaChecksum_Type = Integer32
_RlOspfv3NetworkLsaChecksum_Object = MibTableColumn
rlOspfv3NetworkLsaChecksum = _RlOspfv3NetworkLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 9),
    _RlOspfv3NetworkLsaChecksum_Type()
)
rlOspfv3NetworkLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaChecksum.setStatus("current")
_RlOspfv3NetworkLsaLength_Type = Unsigned32
_RlOspfv3NetworkLsaLength_Object = MibTableColumn
rlOspfv3NetworkLsaLength = _RlOspfv3NetworkLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 10),
    _RlOspfv3NetworkLsaLength_Type()
)
rlOspfv3NetworkLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaLength.setStatus("current")
_RlOspfv3NetworkLsaOptions_Type = Unsigned32
_RlOspfv3NetworkLsaOptions_Object = MibTableColumn
rlOspfv3NetworkLsaOptions = _RlOspfv3NetworkLsaOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 11),
    _RlOspfv3NetworkLsaOptions_Type()
)
rlOspfv3NetworkLsaOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaOptions.setStatus("current")
_RlOspfv3NetworkLsaAttRouter_Type = RouterID
_RlOspfv3NetworkLsaAttRouter_Object = MibTableColumn
rlOspfv3NetworkLsaAttRouter = _RlOspfv3NetworkLsaAttRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 12),
    _RlOspfv3NetworkLsaAttRouter_Type()
)
rlOspfv3NetworkLsaAttRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3NetworkLsaAttRouter.setStatus("current")
_RlOspfv3InterAreaPrefixLsaTable_Object = MibTable
rlOspfv3InterAreaPrefixLsaTable = _RlOspfv3InterAreaPrefixLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3)
)
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaTable.setStatus("current")
_RlOspfv3InterAreaPrefixLsaEntry_Object = MibTableRow
rlOspfv3InterAreaPrefixLsaEntry = _RlOspfv3InterAreaPrefixLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1)
)
rlOspfv3InterAreaPrefixLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaEntry.setStatus("current")
_RlOspfv3InterAreaPrefixLsaProcessId_Type = RlOspfProcessID
_RlOspfv3InterAreaPrefixLsaProcessId_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaProcessId = _RlOspfv3InterAreaPrefixLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 1),
    _RlOspfv3InterAreaPrefixLsaProcessId_Type()
)
rlOspfv3InterAreaPrefixLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaProcessId.setStatus("current")
_RlOspfv3InterAreaPrefixLsaAreaId_Type = AreaID
_RlOspfv3InterAreaPrefixLsaAreaId_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaAreaId = _RlOspfv3InterAreaPrefixLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 2),
    _RlOspfv3InterAreaPrefixLsaAreaId_Type()
)
rlOspfv3InterAreaPrefixLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaAreaId.setStatus("current")
_RlOspfv3InterAreaPrefixLsaLsid_Type = IpAddress
_RlOspfv3InterAreaPrefixLsaLsid_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaLsid = _RlOspfv3InterAreaPrefixLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 3),
    _RlOspfv3InterAreaPrefixLsaLsid_Type()
)
rlOspfv3InterAreaPrefixLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaLsid.setStatus("current")
_RlOspfv3InterAreaPrefixLsaRouterId_Type = RouterID
_RlOspfv3InterAreaPrefixLsaRouterId_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaRouterId = _RlOspfv3InterAreaPrefixLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 4),
    _RlOspfv3InterAreaPrefixLsaRouterId_Type()
)
rlOspfv3InterAreaPrefixLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaRouterId.setStatus("current")
_RlOspfv3InterAreaPrefixLsaSequence_Type = Integer32
_RlOspfv3InterAreaPrefixLsaSequence_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaSequence = _RlOspfv3InterAreaPrefixLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 5),
    _RlOspfv3InterAreaPrefixLsaSequence_Type()
)
rlOspfv3InterAreaPrefixLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaSequence.setStatus("current")
_RlOspfv3InterAreaPrefixLsaAge_Type = Integer32
_RlOspfv3InterAreaPrefixLsaAge_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaAge = _RlOspfv3InterAreaPrefixLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 6),
    _RlOspfv3InterAreaPrefixLsaAge_Type()
)
rlOspfv3InterAreaPrefixLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaAge.setStatus("current")
_RlOspfv3InterAreaPrefixLsaChecksum_Type = Integer32
_RlOspfv3InterAreaPrefixLsaChecksum_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaChecksum = _RlOspfv3InterAreaPrefixLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 7),
    _RlOspfv3InterAreaPrefixLsaChecksum_Type()
)
rlOspfv3InterAreaPrefixLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaChecksum.setStatus("current")
_RlOspfv3InterAreaPrefixLsaLength_Type = Unsigned32
_RlOspfv3InterAreaPrefixLsaLength_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaLength = _RlOspfv3InterAreaPrefixLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 8),
    _RlOspfv3InterAreaPrefixLsaLength_Type()
)
rlOspfv3InterAreaPrefixLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaLength.setStatus("current")
_RlOspfv3InterAreaPrefixLsaMetric_Type = Unsigned32
_RlOspfv3InterAreaPrefixLsaMetric_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaMetric = _RlOspfv3InterAreaPrefixLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 9),
    _RlOspfv3InterAreaPrefixLsaMetric_Type()
)
rlOspfv3InterAreaPrefixLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaMetric.setStatus("current")
_RlOspfv3InterAreaPrefixLsaPrefixLength_Type = Unsigned32
_RlOspfv3InterAreaPrefixLsaPrefixLength_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaPrefixLength = _RlOspfv3InterAreaPrefixLsaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 10),
    _RlOspfv3InterAreaPrefixLsaPrefixLength_Type()
)
rlOspfv3InterAreaPrefixLsaPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaPrefixLength.setStatus("current")
_RlOspfv3InterAreaPrefixLsaPrefixOptions_Type = Unsigned32
_RlOspfv3InterAreaPrefixLsaPrefixOptions_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaPrefixOptions = _RlOspfv3InterAreaPrefixLsaPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 11),
    _RlOspfv3InterAreaPrefixLsaPrefixOptions_Type()
)
rlOspfv3InterAreaPrefixLsaPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaPrefixOptions.setStatus("current")
_RlOspfv3InterAreaPrefixLsaAddressPrefix_Type = InetAddress
_RlOspfv3InterAreaPrefixLsaAddressPrefix_Object = MibTableColumn
rlOspfv3InterAreaPrefixLsaAddressPrefix = _RlOspfv3InterAreaPrefixLsaAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 12),
    _RlOspfv3InterAreaPrefixLsaAddressPrefix_Type()
)
rlOspfv3InterAreaPrefixLsaAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaPrefixLsaAddressPrefix.setStatus("current")
_RlOspfv3InterAreaRouterLsaTable_Object = MibTable
rlOspfv3InterAreaRouterLsaTable = _RlOspfv3InterAreaRouterLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4)
)
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaTable.setStatus("current")
_RlOspfv3InterAreaRouterLsaEntry_Object = MibTableRow
rlOspfv3InterAreaRouterLsaEntry = _RlOspfv3InterAreaRouterLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1)
)
rlOspfv3InterAreaRouterLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaEntry.setStatus("current")
_RlOspfv3InterAreaRouterLsaProcessId_Type = RlOspfProcessID
_RlOspfv3InterAreaRouterLsaProcessId_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaProcessId = _RlOspfv3InterAreaRouterLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 1),
    _RlOspfv3InterAreaRouterLsaProcessId_Type()
)
rlOspfv3InterAreaRouterLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaProcessId.setStatus("current")
_RlOspfv3InterAreaRouterLsaAreaId_Type = AreaID
_RlOspfv3InterAreaRouterLsaAreaId_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaAreaId = _RlOspfv3InterAreaRouterLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 2),
    _RlOspfv3InterAreaRouterLsaAreaId_Type()
)
rlOspfv3InterAreaRouterLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaAreaId.setStatus("current")
_RlOspfv3InterAreaRouterLsaLsid_Type = IpAddress
_RlOspfv3InterAreaRouterLsaLsid_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaLsid = _RlOspfv3InterAreaRouterLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 3),
    _RlOspfv3InterAreaRouterLsaLsid_Type()
)
rlOspfv3InterAreaRouterLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaLsid.setStatus("current")
_RlOspfv3InterAreaRouterLsaRouterId_Type = RouterID
_RlOspfv3InterAreaRouterLsaRouterId_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaRouterId = _RlOspfv3InterAreaRouterLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 4),
    _RlOspfv3InterAreaRouterLsaRouterId_Type()
)
rlOspfv3InterAreaRouterLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaRouterId.setStatus("current")
_RlOspfv3InterAreaRouterLsaSequence_Type = Integer32
_RlOspfv3InterAreaRouterLsaSequence_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaSequence = _RlOspfv3InterAreaRouterLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 5),
    _RlOspfv3InterAreaRouterLsaSequence_Type()
)
rlOspfv3InterAreaRouterLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaSequence.setStatus("current")
_RlOspfv3InterAreaRouterLsaAge_Type = Integer32
_RlOspfv3InterAreaRouterLsaAge_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaAge = _RlOspfv3InterAreaRouterLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 6),
    _RlOspfv3InterAreaRouterLsaAge_Type()
)
rlOspfv3InterAreaRouterLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaAge.setStatus("current")
_RlOspfv3InterAreaRouterLsaChecksum_Type = Integer32
_RlOspfv3InterAreaRouterLsaChecksum_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaChecksum = _RlOspfv3InterAreaRouterLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 7),
    _RlOspfv3InterAreaRouterLsaChecksum_Type()
)
rlOspfv3InterAreaRouterLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaChecksum.setStatus("current")
_RlOspfv3InterAreaRouterLsaLength_Type = Unsigned32
_RlOspfv3InterAreaRouterLsaLength_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaLength = _RlOspfv3InterAreaRouterLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 8),
    _RlOspfv3InterAreaRouterLsaLength_Type()
)
rlOspfv3InterAreaRouterLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaLength.setStatus("current")
_RlOspfv3InterAreaRouterLsaOptions_Type = Unsigned32
_RlOspfv3InterAreaRouterLsaOptions_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaOptions = _RlOspfv3InterAreaRouterLsaOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 9),
    _RlOspfv3InterAreaRouterLsaOptions_Type()
)
rlOspfv3InterAreaRouterLsaOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaOptions.setStatus("current")
_RlOspfv3InterAreaRouterLsaMetric_Type = Unsigned32
_RlOspfv3InterAreaRouterLsaMetric_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaMetric = _RlOspfv3InterAreaRouterLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 10),
    _RlOspfv3InterAreaRouterLsaMetric_Type()
)
rlOspfv3InterAreaRouterLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaMetric.setStatus("current")
_RlOspfv3InterAreaRouterLsaDestinationRouterId_Type = RouterID
_RlOspfv3InterAreaRouterLsaDestinationRouterId_Object = MibTableColumn
rlOspfv3InterAreaRouterLsaDestinationRouterId = _RlOspfv3InterAreaRouterLsaDestinationRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 11),
    _RlOspfv3InterAreaRouterLsaDestinationRouterId_Type()
)
rlOspfv3InterAreaRouterLsaDestinationRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3InterAreaRouterLsaDestinationRouterId.setStatus("current")
_RlOspfv3AsExternalLsaTable_Object = MibTable
rlOspfv3AsExternalLsaTable = _RlOspfv3AsExternalLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5)
)
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaTable.setStatus("current")
_RlOspfv3AsExternalLsaEntry_Object = MibTableRow
rlOspfv3AsExternalLsaEntry = _RlOspfv3AsExternalLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1)
)
rlOspfv3AsExternalLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaEntry.setStatus("current")
_RlOspfv3AsExternalLsaProcessId_Type = RlOspfProcessID
_RlOspfv3AsExternalLsaProcessId_Object = MibTableColumn
rlOspfv3AsExternalLsaProcessId = _RlOspfv3AsExternalLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 1),
    _RlOspfv3AsExternalLsaProcessId_Type()
)
rlOspfv3AsExternalLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaProcessId.setStatus("current")
_RlOspfv3AsExternalLsaAreaId_Type = AreaID
_RlOspfv3AsExternalLsaAreaId_Object = MibTableColumn
rlOspfv3AsExternalLsaAreaId = _RlOspfv3AsExternalLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 2),
    _RlOspfv3AsExternalLsaAreaId_Type()
)
rlOspfv3AsExternalLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaAreaId.setStatus("current")
_RlOspfv3AsExternalLsaLsid_Type = IpAddress
_RlOspfv3AsExternalLsaLsid_Object = MibTableColumn
rlOspfv3AsExternalLsaLsid = _RlOspfv3AsExternalLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 3),
    _RlOspfv3AsExternalLsaLsid_Type()
)
rlOspfv3AsExternalLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaLsid.setStatus("current")
_RlOspfv3AsExternalLsaRouterId_Type = RouterID
_RlOspfv3AsExternalLsaRouterId_Object = MibTableColumn
rlOspfv3AsExternalLsaRouterId = _RlOspfv3AsExternalLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 4),
    _RlOspfv3AsExternalLsaRouterId_Type()
)
rlOspfv3AsExternalLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaRouterId.setStatus("current")
_RlOspfv3AsExternalLsaSequence_Type = Integer32
_RlOspfv3AsExternalLsaSequence_Object = MibTableColumn
rlOspfv3AsExternalLsaSequence = _RlOspfv3AsExternalLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 5),
    _RlOspfv3AsExternalLsaSequence_Type()
)
rlOspfv3AsExternalLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaSequence.setStatus("current")
_RlOspfv3AsExternalLsaAge_Type = Integer32
_RlOspfv3AsExternalLsaAge_Object = MibTableColumn
rlOspfv3AsExternalLsaAge = _RlOspfv3AsExternalLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 6),
    _RlOspfv3AsExternalLsaAge_Type()
)
rlOspfv3AsExternalLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaAge.setStatus("current")
_RlOspfv3AsExternalLsaChecksum_Type = Integer32
_RlOspfv3AsExternalLsaChecksum_Object = MibTableColumn
rlOspfv3AsExternalLsaChecksum = _RlOspfv3AsExternalLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 7),
    _RlOspfv3AsExternalLsaChecksum_Type()
)
rlOspfv3AsExternalLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaChecksum.setStatus("current")
_RlOspfv3AsExternalLsaLength_Type = Unsigned32
_RlOspfv3AsExternalLsaLength_Object = MibTableColumn
rlOspfv3AsExternalLsaLength = _RlOspfv3AsExternalLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 8),
    _RlOspfv3AsExternalLsaLength_Type()
)
rlOspfv3AsExternalLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaLength.setStatus("current")


class _RlOspfv3AsExternalLsaBitE_Type(Integer32):
    """Custom type rlOspfv3AsExternalLsaBitE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3AsExternalLsaBitE_Type.__name__ = "Integer32"
_RlOspfv3AsExternalLsaBitE_Object = MibTableColumn
rlOspfv3AsExternalLsaBitE = _RlOspfv3AsExternalLsaBitE_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 9),
    _RlOspfv3AsExternalLsaBitE_Type()
)
rlOspfv3AsExternalLsaBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaBitE.setStatus("current")


class _RlOspfv3AsExternalLsaBitF_Type(Integer32):
    """Custom type rlOspfv3AsExternalLsaBitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3AsExternalLsaBitF_Type.__name__ = "Integer32"
_RlOspfv3AsExternalLsaBitF_Object = MibTableColumn
rlOspfv3AsExternalLsaBitF = _RlOspfv3AsExternalLsaBitF_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 10),
    _RlOspfv3AsExternalLsaBitF_Type()
)
rlOspfv3AsExternalLsaBitF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaBitF.setStatus("current")


class _RlOspfv3AsExternalLsaBitT_Type(Integer32):
    """Custom type rlOspfv3AsExternalLsaBitT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfv3AsExternalLsaBitT_Type.__name__ = "Integer32"
_RlOspfv3AsExternalLsaBitT_Object = MibTableColumn
rlOspfv3AsExternalLsaBitT = _RlOspfv3AsExternalLsaBitT_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 11),
    _RlOspfv3AsExternalLsaBitT_Type()
)
rlOspfv3AsExternalLsaBitT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaBitT.setStatus("current")
_RlOspfv3AsExternalLsaMetric_Type = Unsigned32
_RlOspfv3AsExternalLsaMetric_Object = MibTableColumn
rlOspfv3AsExternalLsaMetric = _RlOspfv3AsExternalLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 12),
    _RlOspfv3AsExternalLsaMetric_Type()
)
rlOspfv3AsExternalLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaMetric.setStatus("current")
_RlOspfv3AsExternalLsaReferencedLsType_Type = Unsigned32
_RlOspfv3AsExternalLsaReferencedLsType_Object = MibTableColumn
rlOspfv3AsExternalLsaReferencedLsType = _RlOspfv3AsExternalLsaReferencedLsType_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 13),
    _RlOspfv3AsExternalLsaReferencedLsType_Type()
)
rlOspfv3AsExternalLsaReferencedLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaReferencedLsType.setStatus("current")
_RlOspfv3AsExternalLsaPrefixLength_Type = Unsigned32
_RlOspfv3AsExternalLsaPrefixLength_Object = MibTableColumn
rlOspfv3AsExternalLsaPrefixLength = _RlOspfv3AsExternalLsaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 14),
    _RlOspfv3AsExternalLsaPrefixLength_Type()
)
rlOspfv3AsExternalLsaPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaPrefixLength.setStatus("current")
_RlOspfv3AsExternalLsaPrefixOptions_Type = Unsigned32
_RlOspfv3AsExternalLsaPrefixOptions_Object = MibTableColumn
rlOspfv3AsExternalLsaPrefixOptions = _RlOspfv3AsExternalLsaPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 15),
    _RlOspfv3AsExternalLsaPrefixOptions_Type()
)
rlOspfv3AsExternalLsaPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaPrefixOptions.setStatus("current")
_RlOspfv3AsExternalLsaAddressPrefix_Type = InetAddress
_RlOspfv3AsExternalLsaAddressPrefix_Object = MibTableColumn
rlOspfv3AsExternalLsaAddressPrefix = _RlOspfv3AsExternalLsaAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 16),
    _RlOspfv3AsExternalLsaAddressPrefix_Type()
)
rlOspfv3AsExternalLsaAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaAddressPrefix.setStatus("current")
_RlOspfv3AsExternalLsaForwardingAddress_Type = InetAddress
_RlOspfv3AsExternalLsaForwardingAddress_Object = MibTableColumn
rlOspfv3AsExternalLsaForwardingAddress = _RlOspfv3AsExternalLsaForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 17),
    _RlOspfv3AsExternalLsaForwardingAddress_Type()
)
rlOspfv3AsExternalLsaForwardingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaForwardingAddress.setStatus("current")
_RlOspfv3AsExternalLsaExternalRouteTag_Type = Unsigned32
_RlOspfv3AsExternalLsaExternalRouteTag_Object = MibTableColumn
rlOspfv3AsExternalLsaExternalRouteTag = _RlOspfv3AsExternalLsaExternalRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 18),
    _RlOspfv3AsExternalLsaExternalRouteTag_Type()
)
rlOspfv3AsExternalLsaExternalRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaExternalRouteTag.setStatus("current")
_RlOspfv3AsExternalLsaReferencedLinkStateId_Type = Unsigned32
_RlOspfv3AsExternalLsaReferencedLinkStateId_Object = MibTableColumn
rlOspfv3AsExternalLsaReferencedLinkStateId = _RlOspfv3AsExternalLsaReferencedLinkStateId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 19),
    _RlOspfv3AsExternalLsaReferencedLinkStateId_Type()
)
rlOspfv3AsExternalLsaReferencedLinkStateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3AsExternalLsaReferencedLinkStateId.setStatus("current")
_RlOspfv3LinkLsaTable_Object = MibTable
rlOspfv3LinkLsaTable = _RlOspfv3LinkLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6)
)
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaTable.setStatus("current")
_RlOspfv3LinkLsaEntry_Object = MibTableRow
rlOspfv3LinkLsaEntry = _RlOspfv3LinkLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1)
)
rlOspfv3LinkLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIfIndex"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIfInstId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaRouterId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaEntry.setStatus("current")
_RlOspfv3LinkLsaProcessId_Type = RlOspfProcessID
_RlOspfv3LinkLsaProcessId_Object = MibTableColumn
rlOspfv3LinkLsaProcessId = _RlOspfv3LinkLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 1),
    _RlOspfv3LinkLsaProcessId_Type()
)
rlOspfv3LinkLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaProcessId.setStatus("current")
_RlOspfv3LinkLsaIfIndex_Type = Unsigned32
_RlOspfv3LinkLsaIfIndex_Object = MibTableColumn
rlOspfv3LinkLsaIfIndex = _RlOspfv3LinkLsaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 2),
    _RlOspfv3LinkLsaIfIndex_Type()
)
rlOspfv3LinkLsaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaIfIndex.setStatus("current")


class _RlOspfv3LinkLsaIfInstId_Type(Integer32):
    """Custom type rlOspfv3LinkLsaIfInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlOspfv3LinkLsaIfInstId_Type.__name__ = "Integer32"
_RlOspfv3LinkLsaIfInstId_Object = MibTableColumn
rlOspfv3LinkLsaIfInstId = _RlOspfv3LinkLsaIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 3),
    _RlOspfv3LinkLsaIfInstId_Type()
)
rlOspfv3LinkLsaIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaIfInstId.setStatus("current")
_RlOspfv3LinkLsaLsid_Type = IpAddress
_RlOspfv3LinkLsaLsid_Object = MibTableColumn
rlOspfv3LinkLsaLsid = _RlOspfv3LinkLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 4),
    _RlOspfv3LinkLsaLsid_Type()
)
rlOspfv3LinkLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaLsid.setStatus("current")
_RlOspfv3LinkLsaRouterId_Type = RouterID
_RlOspfv3LinkLsaRouterId_Object = MibTableColumn
rlOspfv3LinkLsaRouterId = _RlOspfv3LinkLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 5),
    _RlOspfv3LinkLsaRouterId_Type()
)
rlOspfv3LinkLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaRouterId.setStatus("current")


class _RlOspfv3LinkLsaIdx_Type(Unsigned32):
    """Custom type rlOspfv3LinkLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3LinkLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfv3LinkLsaIdx_Object = MibTableColumn
rlOspfv3LinkLsaIdx = _RlOspfv3LinkLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 6),
    _RlOspfv3LinkLsaIdx_Type()
)
rlOspfv3LinkLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaIdx.setStatus("current")


class _RlOspfv3LinkLsaCount_Type(Unsigned32):
    """Custom type rlOspfv3LinkLsaCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3LinkLsaCount_Type.__name__ = "Unsigned32"
_RlOspfv3LinkLsaCount_Object = MibTableColumn
rlOspfv3LinkLsaCount = _RlOspfv3LinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 7),
    _RlOspfv3LinkLsaCount_Type()
)
rlOspfv3LinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaCount.setStatus("current")
_RlOspfv3LinkLsaSequence_Type = Integer32
_RlOspfv3LinkLsaSequence_Object = MibTableColumn
rlOspfv3LinkLsaSequence = _RlOspfv3LinkLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 8),
    _RlOspfv3LinkLsaSequence_Type()
)
rlOspfv3LinkLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaSequence.setStatus("current")
_RlOspfv3LinkLsaAge_Type = Integer32
_RlOspfv3LinkLsaAge_Object = MibTableColumn
rlOspfv3LinkLsaAge = _RlOspfv3LinkLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 9),
    _RlOspfv3LinkLsaAge_Type()
)
rlOspfv3LinkLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaAge.setStatus("current")
_RlOspfv3LinkLsaChecksum_Type = Integer32
_RlOspfv3LinkLsaChecksum_Object = MibTableColumn
rlOspfv3LinkLsaChecksum = _RlOspfv3LinkLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 10),
    _RlOspfv3LinkLsaChecksum_Type()
)
rlOspfv3LinkLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaChecksum.setStatus("current")
_RlOspfv3LinkLsaLength_Type = Unsigned32
_RlOspfv3LinkLsaLength_Object = MibTableColumn
rlOspfv3LinkLsaLength = _RlOspfv3LinkLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 11),
    _RlOspfv3LinkLsaLength_Type()
)
rlOspfv3LinkLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaLength.setStatus("current")
_RlOspfv3LinkLsaRtrPri_Type = Unsigned32
_RlOspfv3LinkLsaRtrPri_Object = MibTableColumn
rlOspfv3LinkLsaRtrPri = _RlOspfv3LinkLsaRtrPri_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 12),
    _RlOspfv3LinkLsaRtrPri_Type()
)
rlOspfv3LinkLsaRtrPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaRtrPri.setStatus("current")
_RlOspfv3LinkLsaOptions_Type = Unsigned32
_RlOspfv3LinkLsaOptions_Object = MibTableColumn
rlOspfv3LinkLsaOptions = _RlOspfv3LinkLsaOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 13),
    _RlOspfv3LinkLsaOptions_Type()
)
rlOspfv3LinkLsaOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaOptions.setStatus("current")
_RlOspfv3LinkLsaLinkLocalInterfaceAddress_Type = InetAddress
_RlOspfv3LinkLsaLinkLocalInterfaceAddress_Object = MibTableColumn
rlOspfv3LinkLsaLinkLocalInterfaceAddress = _RlOspfv3LinkLsaLinkLocalInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 14),
    _RlOspfv3LinkLsaLinkLocalInterfaceAddress_Type()
)
rlOspfv3LinkLsaLinkLocalInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaLinkLocalInterfaceAddress.setStatus("current")
_RlOspfv3LinkLsaPrefixLength_Type = Unsigned32
_RlOspfv3LinkLsaPrefixLength_Object = MibTableColumn
rlOspfv3LinkLsaPrefixLength = _RlOspfv3LinkLsaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 15),
    _RlOspfv3LinkLsaPrefixLength_Type()
)
rlOspfv3LinkLsaPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaPrefixLength.setStatus("current")
_RlOspfv3LinkLsaPrefixOptions_Type = Unsigned32
_RlOspfv3LinkLsaPrefixOptions_Object = MibTableColumn
rlOspfv3LinkLsaPrefixOptions = _RlOspfv3LinkLsaPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 16),
    _RlOspfv3LinkLsaPrefixOptions_Type()
)
rlOspfv3LinkLsaPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaPrefixOptions.setStatus("current")
_RlOspfv3LinkLsaAddressPrefix_Type = InetAddress
_RlOspfv3LinkLsaAddressPrefix_Object = MibTableColumn
rlOspfv3LinkLsaAddressPrefix = _RlOspfv3LinkLsaAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 17),
    _RlOspfv3LinkLsaAddressPrefix_Type()
)
rlOspfv3LinkLsaAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3LinkLsaAddressPrefix.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaTable_Object = MibTable
rlOspfv3IntraAreaPrefixLsaTable = _RlOspfv3IntraAreaPrefixLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7)
)
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaTable.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaEntry_Object = MibTableRow
rlOspfv3IntraAreaPrefixLsaEntry = _RlOspfv3IntraAreaPrefixLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1)
)
rlOspfv3IntraAreaPrefixLsaEntry.setIndexNames(
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaProcessId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaAreaId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaLsid"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaRouterId"),
    (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaEntry.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaProcessId_Type = RlOspfProcessID
_RlOspfv3IntraAreaPrefixLsaProcessId_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaProcessId = _RlOspfv3IntraAreaPrefixLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 1),
    _RlOspfv3IntraAreaPrefixLsaProcessId_Type()
)
rlOspfv3IntraAreaPrefixLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaProcessId.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaAreaId_Type = AreaID
_RlOspfv3IntraAreaPrefixLsaAreaId_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaAreaId = _RlOspfv3IntraAreaPrefixLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 2),
    _RlOspfv3IntraAreaPrefixLsaAreaId_Type()
)
rlOspfv3IntraAreaPrefixLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaAreaId.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaLsid_Type = IpAddress
_RlOspfv3IntraAreaPrefixLsaLsid_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaLsid = _RlOspfv3IntraAreaPrefixLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 3),
    _RlOspfv3IntraAreaPrefixLsaLsid_Type()
)
rlOspfv3IntraAreaPrefixLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaLsid.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaRouterId_Type = RouterID
_RlOspfv3IntraAreaPrefixLsaRouterId_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaRouterId = _RlOspfv3IntraAreaPrefixLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 4),
    _RlOspfv3IntraAreaPrefixLsaRouterId_Type()
)
rlOspfv3IntraAreaPrefixLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaRouterId.setStatus("current")


class _RlOspfv3IntraAreaPrefixLsaIdx_Type(Unsigned32):
    """Custom type rlOspfv3IntraAreaPrefixLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3IntraAreaPrefixLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfv3IntraAreaPrefixLsaIdx_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaIdx = _RlOspfv3IntraAreaPrefixLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 5),
    _RlOspfv3IntraAreaPrefixLsaIdx_Type()
)
rlOspfv3IntraAreaPrefixLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaIdx.setStatus("current")


class _RlOspfv3IntraAreaPrefixLsaCount_Type(Unsigned32):
    """Custom type rlOspfv3IntraAreaPrefixLsaCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfv3IntraAreaPrefixLsaCount_Type.__name__ = "Unsigned32"
_RlOspfv3IntraAreaPrefixLsaCount_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaCount = _RlOspfv3IntraAreaPrefixLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 6),
    _RlOspfv3IntraAreaPrefixLsaCount_Type()
)
rlOspfv3IntraAreaPrefixLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaCount.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaSequence_Type = Integer32
_RlOspfv3IntraAreaPrefixLsaSequence_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaSequence = _RlOspfv3IntraAreaPrefixLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 7),
    _RlOspfv3IntraAreaPrefixLsaSequence_Type()
)
rlOspfv3IntraAreaPrefixLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaSequence.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaAge_Type = Integer32
_RlOspfv3IntraAreaPrefixLsaAge_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaAge = _RlOspfv3IntraAreaPrefixLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 8),
    _RlOspfv3IntraAreaPrefixLsaAge_Type()
)
rlOspfv3IntraAreaPrefixLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaAge.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaChecksum_Type = Integer32
_RlOspfv3IntraAreaPrefixLsaChecksum_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaChecksum = _RlOspfv3IntraAreaPrefixLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 9),
    _RlOspfv3IntraAreaPrefixLsaChecksum_Type()
)
rlOspfv3IntraAreaPrefixLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaChecksum.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaLength_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaLength_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaLength = _RlOspfv3IntraAreaPrefixLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 10),
    _RlOspfv3IntraAreaPrefixLsaLength_Type()
)
rlOspfv3IntraAreaPrefixLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaLength.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaNumPrefixes_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaNumPrefixes_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaNumPrefixes = _RlOspfv3IntraAreaPrefixLsaNumPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 11),
    _RlOspfv3IntraAreaPrefixLsaNumPrefixes_Type()
)
rlOspfv3IntraAreaPrefixLsaNumPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaNumPrefixes.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaReferenceLsType_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaReferenceLsType_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaReferenceLsType = _RlOspfv3IntraAreaPrefixLsaReferenceLsType_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 12),
    _RlOspfv3IntraAreaPrefixLsaReferenceLsType_Type()
)
rlOspfv3IntraAreaPrefixLsaReferenceLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaReferenceLsType.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaReferenceLsId_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaReferenceLsId_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaReferenceLsId = _RlOspfv3IntraAreaPrefixLsaReferenceLsId_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 13),
    _RlOspfv3IntraAreaPrefixLsaReferenceLsId_Type()
)
rlOspfv3IntraAreaPrefixLsaReferenceLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaReferenceLsId.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaReferenceAdvRouter_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaReferenceAdvRouter_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter = _RlOspfv3IntraAreaPrefixLsaReferenceAdvRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 14),
    _RlOspfv3IntraAreaPrefixLsaReferenceAdvRouter_Type()
)
rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaMetric_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaMetric_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaMetric = _RlOspfv3IntraAreaPrefixLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 15),
    _RlOspfv3IntraAreaPrefixLsaMetric_Type()
)
rlOspfv3IntraAreaPrefixLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaMetric.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaPrefixLength_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaPrefixLength_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaPrefixLength = _RlOspfv3IntraAreaPrefixLsaPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 16),
    _RlOspfv3IntraAreaPrefixLsaPrefixLength_Type()
)
rlOspfv3IntraAreaPrefixLsaPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaPrefixLength.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaPrefixOptions_Type = Unsigned32
_RlOspfv3IntraAreaPrefixLsaPrefixOptions_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaPrefixOptions = _RlOspfv3IntraAreaPrefixLsaPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 17),
    _RlOspfv3IntraAreaPrefixLsaPrefixOptions_Type()
)
rlOspfv3IntraAreaPrefixLsaPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaPrefixOptions.setStatus("current")
_RlOspfv3IntraAreaPrefixLsaAddressPrefix_Type = InetAddress
_RlOspfv3IntraAreaPrefixLsaAddressPrefix_Object = MibTableColumn
rlOspfv3IntraAreaPrefixLsaAddressPrefix = _RlOspfv3IntraAreaPrefixLsaAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 18),
    _RlOspfv3IntraAreaPrefixLsaAddressPrefix_Type()
)
rlOspfv3IntraAreaPrefixLsaAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfv3IntraAreaPrefixLsaAddressPrefix.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-OSPFV3-LSDB-MIB",
    **{"rlOspfv3Lsdb": rlOspfv3Lsdb,
       "rlOspfv3RouterLsaTable": rlOspfv3RouterLsaTable,
       "rlOspfv3RouterLsaEntry": rlOspfv3RouterLsaEntry,
       "rlOspfv3RouterLsaProcessId": rlOspfv3RouterLsaProcessId,
       "rlOspfv3RouterLsaAreaId": rlOspfv3RouterLsaAreaId,
       "rlOspfv3RouterLsaLsid": rlOspfv3RouterLsaLsid,
       "rlOspfv3RouterLsaRouterId": rlOspfv3RouterLsaRouterId,
       "rlOspfv3RouterLsaIdx": rlOspfv3RouterLsaIdx,
       "rlOspfv3RouterLsaCount": rlOspfv3RouterLsaCount,
       "rlOspfv3RouterLsaSequence": rlOspfv3RouterLsaSequence,
       "rlOspfv3RouterLsaAge": rlOspfv3RouterLsaAge,
       "rlOspfv3RouterLsaChecksum": rlOspfv3RouterLsaChecksum,
       "rlOspfv3RouterLsaLength": rlOspfv3RouterLsaLength,
       "rlOspfv3RouterLsaBitW": rlOspfv3RouterLsaBitW,
       "rlOspfv3RouterLsaBitV": rlOspfv3RouterLsaBitV,
       "rlOspfv3RouterLsaBitE": rlOspfv3RouterLsaBitE,
       "rlOspfv3RouterLsaBitB": rlOspfv3RouterLsaBitB,
       "rlOspfv3RouterLsaOptions": rlOspfv3RouterLsaOptions,
       "rlOspfv3RouterLsaType": rlOspfv3RouterLsaType,
       "rlOspfv3RouterLsaMetric": rlOspfv3RouterLsaMetric,
       "rlOspfv3RouterLsaInterfaceID": rlOspfv3RouterLsaInterfaceID,
       "rlOspfv3RouterLsaNeighborInterfaceID": rlOspfv3RouterLsaNeighborInterfaceID,
       "rlOspfv3RouterLsaNeighborRouterID": rlOspfv3RouterLsaNeighborRouterID,
       "rlOspfv3NetworkLsaTable": rlOspfv3NetworkLsaTable,
       "rlOspfv3NetworkLsaEntry": rlOspfv3NetworkLsaEntry,
       "rlOspfv3NetworkLsaProcessId": rlOspfv3NetworkLsaProcessId,
       "rlOspfv3NetworkLsaAreaId": rlOspfv3NetworkLsaAreaId,
       "rlOspfv3NetworkLsaLsid": rlOspfv3NetworkLsaLsid,
       "rlOspfv3NetworkLsaRouterId": rlOspfv3NetworkLsaRouterId,
       "rlOspfv3NetworkLsaIdx": rlOspfv3NetworkLsaIdx,
       "rlOspfv3NetworkLsaCount": rlOspfv3NetworkLsaCount,
       "rlOspfv3NetworkLsaSequence": rlOspfv3NetworkLsaSequence,
       "rlOspfv3NetworkLsaAge": rlOspfv3NetworkLsaAge,
       "rlOspfv3NetworkLsaChecksum": rlOspfv3NetworkLsaChecksum,
       "rlOspfv3NetworkLsaLength": rlOspfv3NetworkLsaLength,
       "rlOspfv3NetworkLsaOptions": rlOspfv3NetworkLsaOptions,
       "rlOspfv3NetworkLsaAttRouter": rlOspfv3NetworkLsaAttRouter,
       "rlOspfv3InterAreaPrefixLsaTable": rlOspfv3InterAreaPrefixLsaTable,
       "rlOspfv3InterAreaPrefixLsaEntry": rlOspfv3InterAreaPrefixLsaEntry,
       "rlOspfv3InterAreaPrefixLsaProcessId": rlOspfv3InterAreaPrefixLsaProcessId,
       "rlOspfv3InterAreaPrefixLsaAreaId": rlOspfv3InterAreaPrefixLsaAreaId,
       "rlOspfv3InterAreaPrefixLsaLsid": rlOspfv3InterAreaPrefixLsaLsid,
       "rlOspfv3InterAreaPrefixLsaRouterId": rlOspfv3InterAreaPrefixLsaRouterId,
       "rlOspfv3InterAreaPrefixLsaSequence": rlOspfv3InterAreaPrefixLsaSequence,
       "rlOspfv3InterAreaPrefixLsaAge": rlOspfv3InterAreaPrefixLsaAge,
       "rlOspfv3InterAreaPrefixLsaChecksum": rlOspfv3InterAreaPrefixLsaChecksum,
       "rlOspfv3InterAreaPrefixLsaLength": rlOspfv3InterAreaPrefixLsaLength,
       "rlOspfv3InterAreaPrefixLsaMetric": rlOspfv3InterAreaPrefixLsaMetric,
       "rlOspfv3InterAreaPrefixLsaPrefixLength": rlOspfv3InterAreaPrefixLsaPrefixLength,
       "rlOspfv3InterAreaPrefixLsaPrefixOptions": rlOspfv3InterAreaPrefixLsaPrefixOptions,
       "rlOspfv3InterAreaPrefixLsaAddressPrefix": rlOspfv3InterAreaPrefixLsaAddressPrefix,
       "rlOspfv3InterAreaRouterLsaTable": rlOspfv3InterAreaRouterLsaTable,
       "rlOspfv3InterAreaRouterLsaEntry": rlOspfv3InterAreaRouterLsaEntry,
       "rlOspfv3InterAreaRouterLsaProcessId": rlOspfv3InterAreaRouterLsaProcessId,
       "rlOspfv3InterAreaRouterLsaAreaId": rlOspfv3InterAreaRouterLsaAreaId,
       "rlOspfv3InterAreaRouterLsaLsid": rlOspfv3InterAreaRouterLsaLsid,
       "rlOspfv3InterAreaRouterLsaRouterId": rlOspfv3InterAreaRouterLsaRouterId,
       "rlOspfv3InterAreaRouterLsaSequence": rlOspfv3InterAreaRouterLsaSequence,
       "rlOspfv3InterAreaRouterLsaAge": rlOspfv3InterAreaRouterLsaAge,
       "rlOspfv3InterAreaRouterLsaChecksum": rlOspfv3InterAreaRouterLsaChecksum,
       "rlOspfv3InterAreaRouterLsaLength": rlOspfv3InterAreaRouterLsaLength,
       "rlOspfv3InterAreaRouterLsaOptions": rlOspfv3InterAreaRouterLsaOptions,
       "rlOspfv3InterAreaRouterLsaMetric": rlOspfv3InterAreaRouterLsaMetric,
       "rlOspfv3InterAreaRouterLsaDestinationRouterId": rlOspfv3InterAreaRouterLsaDestinationRouterId,
       "rlOspfv3AsExternalLsaTable": rlOspfv3AsExternalLsaTable,
       "rlOspfv3AsExternalLsaEntry": rlOspfv3AsExternalLsaEntry,
       "rlOspfv3AsExternalLsaProcessId": rlOspfv3AsExternalLsaProcessId,
       "rlOspfv3AsExternalLsaAreaId": rlOspfv3AsExternalLsaAreaId,
       "rlOspfv3AsExternalLsaLsid": rlOspfv3AsExternalLsaLsid,
       "rlOspfv3AsExternalLsaRouterId": rlOspfv3AsExternalLsaRouterId,
       "rlOspfv3AsExternalLsaSequence": rlOspfv3AsExternalLsaSequence,
       "rlOspfv3AsExternalLsaAge": rlOspfv3AsExternalLsaAge,
       "rlOspfv3AsExternalLsaChecksum": rlOspfv3AsExternalLsaChecksum,
       "rlOspfv3AsExternalLsaLength": rlOspfv3AsExternalLsaLength,
       "rlOspfv3AsExternalLsaBitE": rlOspfv3AsExternalLsaBitE,
       "rlOspfv3AsExternalLsaBitF": rlOspfv3AsExternalLsaBitF,
       "rlOspfv3AsExternalLsaBitT": rlOspfv3AsExternalLsaBitT,
       "rlOspfv3AsExternalLsaMetric": rlOspfv3AsExternalLsaMetric,
       "rlOspfv3AsExternalLsaReferencedLsType": rlOspfv3AsExternalLsaReferencedLsType,
       "rlOspfv3AsExternalLsaPrefixLength": rlOspfv3AsExternalLsaPrefixLength,
       "rlOspfv3AsExternalLsaPrefixOptions": rlOspfv3AsExternalLsaPrefixOptions,
       "rlOspfv3AsExternalLsaAddressPrefix": rlOspfv3AsExternalLsaAddressPrefix,
       "rlOspfv3AsExternalLsaForwardingAddress": rlOspfv3AsExternalLsaForwardingAddress,
       "rlOspfv3AsExternalLsaExternalRouteTag": rlOspfv3AsExternalLsaExternalRouteTag,
       "rlOspfv3AsExternalLsaReferencedLinkStateId": rlOspfv3AsExternalLsaReferencedLinkStateId,
       "rlOspfv3LinkLsaTable": rlOspfv3LinkLsaTable,
       "rlOspfv3LinkLsaEntry": rlOspfv3LinkLsaEntry,
       "rlOspfv3LinkLsaProcessId": rlOspfv3LinkLsaProcessId,
       "rlOspfv3LinkLsaIfIndex": rlOspfv3LinkLsaIfIndex,
       "rlOspfv3LinkLsaIfInstId": rlOspfv3LinkLsaIfInstId,
       "rlOspfv3LinkLsaLsid": rlOspfv3LinkLsaLsid,
       "rlOspfv3LinkLsaRouterId": rlOspfv3LinkLsaRouterId,
       "rlOspfv3LinkLsaIdx": rlOspfv3LinkLsaIdx,
       "rlOspfv3LinkLsaCount": rlOspfv3LinkLsaCount,
       "rlOspfv3LinkLsaSequence": rlOspfv3LinkLsaSequence,
       "rlOspfv3LinkLsaAge": rlOspfv3LinkLsaAge,
       "rlOspfv3LinkLsaChecksum": rlOspfv3LinkLsaChecksum,
       "rlOspfv3LinkLsaLength": rlOspfv3LinkLsaLength,
       "rlOspfv3LinkLsaRtrPri": rlOspfv3LinkLsaRtrPri,
       "rlOspfv3LinkLsaOptions": rlOspfv3LinkLsaOptions,
       "rlOspfv3LinkLsaLinkLocalInterfaceAddress": rlOspfv3LinkLsaLinkLocalInterfaceAddress,
       "rlOspfv3LinkLsaPrefixLength": rlOspfv3LinkLsaPrefixLength,
       "rlOspfv3LinkLsaPrefixOptions": rlOspfv3LinkLsaPrefixOptions,
       "rlOspfv3LinkLsaAddressPrefix": rlOspfv3LinkLsaAddressPrefix,
       "rlOspfv3IntraAreaPrefixLsaTable": rlOspfv3IntraAreaPrefixLsaTable,
       "rlOspfv3IntraAreaPrefixLsaEntry": rlOspfv3IntraAreaPrefixLsaEntry,
       "rlOspfv3IntraAreaPrefixLsaProcessId": rlOspfv3IntraAreaPrefixLsaProcessId,
       "rlOspfv3IntraAreaPrefixLsaAreaId": rlOspfv3IntraAreaPrefixLsaAreaId,
       "rlOspfv3IntraAreaPrefixLsaLsid": rlOspfv3IntraAreaPrefixLsaLsid,
       "rlOspfv3IntraAreaPrefixLsaRouterId": rlOspfv3IntraAreaPrefixLsaRouterId,
       "rlOspfv3IntraAreaPrefixLsaIdx": rlOspfv3IntraAreaPrefixLsaIdx,
       "rlOspfv3IntraAreaPrefixLsaCount": rlOspfv3IntraAreaPrefixLsaCount,
       "rlOspfv3IntraAreaPrefixLsaSequence": rlOspfv3IntraAreaPrefixLsaSequence,
       "rlOspfv3IntraAreaPrefixLsaAge": rlOspfv3IntraAreaPrefixLsaAge,
       "rlOspfv3IntraAreaPrefixLsaChecksum": rlOspfv3IntraAreaPrefixLsaChecksum,
       "rlOspfv3IntraAreaPrefixLsaLength": rlOspfv3IntraAreaPrefixLsaLength,
       "rlOspfv3IntraAreaPrefixLsaNumPrefixes": rlOspfv3IntraAreaPrefixLsaNumPrefixes,
       "rlOspfv3IntraAreaPrefixLsaReferenceLsType": rlOspfv3IntraAreaPrefixLsaReferenceLsType,
       "rlOspfv3IntraAreaPrefixLsaReferenceLsId": rlOspfv3IntraAreaPrefixLsaReferenceLsId,
       "rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter": rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter,
       "rlOspfv3IntraAreaPrefixLsaMetric": rlOspfv3IntraAreaPrefixLsaMetric,
       "rlOspfv3IntraAreaPrefixLsaPrefixLength": rlOspfv3IntraAreaPrefixLsaPrefixLength,
       "rlOspfv3IntraAreaPrefixLsaPrefixOptions": rlOspfv3IntraAreaPrefixLsaPrefixOptions,
       "rlOspfv3IntraAreaPrefixLsaAddressPrefix": rlOspfv3IntraAreaPrefixLsaAddressPrefix}
)
