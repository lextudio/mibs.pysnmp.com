# SNMP MIB module (RADLAN-OSPF-LSDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-OSPF-LSDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:47 2024
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

(AreaID,
 RouterID) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "RouterID")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(RlOspfProcessID,
 rlOspf,
 rlOspfIfEntry,
 rlOspfVirtIfEntry) = mibBuilder.importSymbols(
    "RADLAN-OSPF-MIB",
    "RlOspfProcessID",
    "rlOspf",
    "rlOspfIfEntry",
    "rlOspfVirtIfEntry")

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

rlOspfLsdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 221)
)
rlOspfLsdb.setRevisions(
        ("2011-05-04 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlOspfRouterLsaTable_Object = MibTable
rlOspfRouterLsaTable = _RlOspfRouterLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1)
)
if mibBuilder.loadTexts:
    rlOspfRouterLsaTable.setStatus("current")
_RlOspfRouterLsaEntry_Object = MibTableRow
rlOspfRouterLsaEntry = _RlOspfRouterLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1)
)
rlOspfRouterLsaEntry.setIndexNames(
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaProcessId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaAreaId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaLsid"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaRouterId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfRouterLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfRouterLsaEntry.setStatus("current")
_RlOspfRouterLsaProcessId_Type = RlOspfProcessID
_RlOspfRouterLsaProcessId_Object = MibTableColumn
rlOspfRouterLsaProcessId = _RlOspfRouterLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 1),
    _RlOspfRouterLsaProcessId_Type()
)
rlOspfRouterLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaProcessId.setStatus("current")
_RlOspfRouterLsaAreaId_Type = AreaID
_RlOspfRouterLsaAreaId_Object = MibTableColumn
rlOspfRouterLsaAreaId = _RlOspfRouterLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 2),
    _RlOspfRouterLsaAreaId_Type()
)
rlOspfRouterLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaAreaId.setStatus("current")
_RlOspfRouterLsaLsid_Type = IpAddress
_RlOspfRouterLsaLsid_Object = MibTableColumn
rlOspfRouterLsaLsid = _RlOspfRouterLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 3),
    _RlOspfRouterLsaLsid_Type()
)
rlOspfRouterLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaLsid.setStatus("current")
_RlOspfRouterLsaRouterId_Type = RouterID
_RlOspfRouterLsaRouterId_Object = MibTableColumn
rlOspfRouterLsaRouterId = _RlOspfRouterLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 4),
    _RlOspfRouterLsaRouterId_Type()
)
rlOspfRouterLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaRouterId.setStatus("current")


class _RlOspfRouterLsaIdx_Type(Unsigned32):
    """Custom type rlOspfRouterLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfRouterLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfRouterLsaIdx_Object = MibTableColumn
rlOspfRouterLsaIdx = _RlOspfRouterLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 5),
    _RlOspfRouterLsaIdx_Type()
)
rlOspfRouterLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaIdx.setStatus("current")
_RlOspfRouterLsaSequence_Type = Integer32
_RlOspfRouterLsaSequence_Object = MibTableColumn
rlOspfRouterLsaSequence = _RlOspfRouterLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 6),
    _RlOspfRouterLsaSequence_Type()
)
rlOspfRouterLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaSequence.setStatus("current")
_RlOspfRouterLsaAge_Type = Integer32
_RlOspfRouterLsaAge_Object = MibTableColumn
rlOspfRouterLsaAge = _RlOspfRouterLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 7),
    _RlOspfRouterLsaAge_Type()
)
rlOspfRouterLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaAge.setStatus("current")
_RlOspfRouterLsaChecksum_Type = Integer32
_RlOspfRouterLsaChecksum_Object = MibTableColumn
rlOspfRouterLsaChecksum = _RlOspfRouterLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 8),
    _RlOspfRouterLsaChecksum_Type()
)
rlOspfRouterLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaChecksum.setStatus("current")
_RlOspfRouterLsaLength_Type = Unsigned32
_RlOspfRouterLsaLength_Object = MibTableColumn
rlOspfRouterLsaLength = _RlOspfRouterLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 9),
    _RlOspfRouterLsaLength_Type()
)
rlOspfRouterLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaLength.setStatus("current")


class _RlOspfRouterLsaBitV_Type(Integer32):
    """Custom type rlOspfRouterLsaBitV based on Integer32"""
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


_RlOspfRouterLsaBitV_Type.__name__ = "Integer32"
_RlOspfRouterLsaBitV_Object = MibTableColumn
rlOspfRouterLsaBitV = _RlOspfRouterLsaBitV_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 10),
    _RlOspfRouterLsaBitV_Type()
)
rlOspfRouterLsaBitV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaBitV.setStatus("current")


class _RlOspfRouterLsaBitE_Type(Integer32):
    """Custom type rlOspfRouterLsaBitE based on Integer32"""
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


_RlOspfRouterLsaBitE_Type.__name__ = "Integer32"
_RlOspfRouterLsaBitE_Object = MibTableColumn
rlOspfRouterLsaBitE = _RlOspfRouterLsaBitE_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 11),
    _RlOspfRouterLsaBitE_Type()
)
rlOspfRouterLsaBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaBitE.setStatus("current")


class _RlOspfRouterLsaBitB_Type(Integer32):
    """Custom type rlOspfRouterLsaBitB based on Integer32"""
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


_RlOspfRouterLsaBitB_Type.__name__ = "Integer32"
_RlOspfRouterLsaBitB_Object = MibTableColumn
rlOspfRouterLsaBitB = _RlOspfRouterLsaBitB_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 12),
    _RlOspfRouterLsaBitB_Type()
)
rlOspfRouterLsaBitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaBitB.setStatus("current")
_RlOspfRouterLsaLinks_Type = Unsigned32
_RlOspfRouterLsaLinks_Object = MibTableColumn
rlOspfRouterLsaLinks = _RlOspfRouterLsaLinks_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 13),
    _RlOspfRouterLsaLinks_Type()
)
rlOspfRouterLsaLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaLinks.setStatus("current")
_RlOspfRouterLsaLinkID_Type = IpAddress
_RlOspfRouterLsaLinkID_Object = MibTableColumn
rlOspfRouterLsaLinkID = _RlOspfRouterLsaLinkID_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 14),
    _RlOspfRouterLsaLinkID_Type()
)
rlOspfRouterLsaLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaLinkID.setStatus("current")
_RlOspfRouterLsaLinkData_Type = IpAddress
_RlOspfRouterLsaLinkData_Object = MibTableColumn
rlOspfRouterLsaLinkData = _RlOspfRouterLsaLinkData_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 15),
    _RlOspfRouterLsaLinkData_Type()
)
rlOspfRouterLsaLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaLinkData.setStatus("current")


class _RlOspfRouterLsaType_Type(Integer32):
    """Custom type rlOspfRouterLsaType based on Integer32"""
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


_RlOspfRouterLsaType_Type.__name__ = "Integer32"
_RlOspfRouterLsaType_Object = MibTableColumn
rlOspfRouterLsaType = _RlOspfRouterLsaType_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 16),
    _RlOspfRouterLsaType_Type()
)
rlOspfRouterLsaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaType.setStatus("current")
_RlOspfRouterLsaMetric_Type = Unsigned32
_RlOspfRouterLsaMetric_Object = MibTableColumn
rlOspfRouterLsaMetric = _RlOspfRouterLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 1, 1, 17),
    _RlOspfRouterLsaMetric_Type()
)
rlOspfRouterLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterLsaMetric.setStatus("current")
_RlOspfNetworkLsaTable_Object = MibTable
rlOspfNetworkLsaTable = _RlOspfNetworkLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2)
)
if mibBuilder.loadTexts:
    rlOspfNetworkLsaTable.setStatus("current")
_RlOspfNetworkLsaEntry_Object = MibTableRow
rlOspfNetworkLsaEntry = _RlOspfNetworkLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1)
)
rlOspfNetworkLsaEntry.setIndexNames(
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaProcessId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaAreaId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaLsid"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaRouterId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfNetworkLsaIdx"),
)
if mibBuilder.loadTexts:
    rlOspfNetworkLsaEntry.setStatus("current")
_RlOspfNetworkLsaProcessId_Type = RlOspfProcessID
_RlOspfNetworkLsaProcessId_Object = MibTableColumn
rlOspfNetworkLsaProcessId = _RlOspfNetworkLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 1),
    _RlOspfNetworkLsaProcessId_Type()
)
rlOspfNetworkLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaProcessId.setStatus("current")
_RlOspfNetworkLsaAreaId_Type = AreaID
_RlOspfNetworkLsaAreaId_Object = MibTableColumn
rlOspfNetworkLsaAreaId = _RlOspfNetworkLsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 2),
    _RlOspfNetworkLsaAreaId_Type()
)
rlOspfNetworkLsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaAreaId.setStatus("current")
_RlOspfNetworkLsaLsid_Type = IpAddress
_RlOspfNetworkLsaLsid_Object = MibTableColumn
rlOspfNetworkLsaLsid = _RlOspfNetworkLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 3),
    _RlOspfNetworkLsaLsid_Type()
)
rlOspfNetworkLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaLsid.setStatus("current")
_RlOspfNetworkLsaRouterId_Type = RouterID
_RlOspfNetworkLsaRouterId_Object = MibTableColumn
rlOspfNetworkLsaRouterId = _RlOspfNetworkLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 4),
    _RlOspfNetworkLsaRouterId_Type()
)
rlOspfNetworkLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaRouterId.setStatus("current")


class _RlOspfNetworkLsaIdx_Type(Unsigned32):
    """Custom type rlOspfNetworkLsaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfNetworkLsaIdx_Type.__name__ = "Unsigned32"
_RlOspfNetworkLsaIdx_Object = MibTableColumn
rlOspfNetworkLsaIdx = _RlOspfNetworkLsaIdx_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 5),
    _RlOspfNetworkLsaIdx_Type()
)
rlOspfNetworkLsaIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaIdx.setStatus("current")
_RlOspfNetworkLsaSequence_Type = Integer32
_RlOspfNetworkLsaSequence_Object = MibTableColumn
rlOspfNetworkLsaSequence = _RlOspfNetworkLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 6),
    _RlOspfNetworkLsaSequence_Type()
)
rlOspfNetworkLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaSequence.setStatus("current")
_RlOspfNetworkLsaAge_Type = Integer32
_RlOspfNetworkLsaAge_Object = MibTableColumn
rlOspfNetworkLsaAge = _RlOspfNetworkLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 7),
    _RlOspfNetworkLsaAge_Type()
)
rlOspfNetworkLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaAge.setStatus("current")
_RlOspfNetworkLsaChecksum_Type = Integer32
_RlOspfNetworkLsaChecksum_Object = MibTableColumn
rlOspfNetworkLsaChecksum = _RlOspfNetworkLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 8),
    _RlOspfNetworkLsaChecksum_Type()
)
rlOspfNetworkLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaChecksum.setStatus("current")
_RlOspfNetworkLsaLength_Type = Unsigned32
_RlOspfNetworkLsaLength_Object = MibTableColumn
rlOspfNetworkLsaLength = _RlOspfNetworkLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 9),
    _RlOspfNetworkLsaLength_Type()
)
rlOspfNetworkLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaLength.setStatus("current")
_RlOspfNetworkLsaMask_Type = IpAddress
_RlOspfNetworkLsaMask_Object = MibTableColumn
rlOspfNetworkLsaMask = _RlOspfNetworkLsaMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 10),
    _RlOspfNetworkLsaMask_Type()
)
rlOspfNetworkLsaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaMask.setStatus("current")
_RlOspfNetworkLsaAttRouter_Type = IpAddress
_RlOspfNetworkLsaAttRouter_Object = MibTableColumn
rlOspfNetworkLsaAttRouter = _RlOspfNetworkLsaAttRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 2, 1, 11),
    _RlOspfNetworkLsaAttRouter_Type()
)
rlOspfNetworkLsaAttRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetworkLsaAttRouter.setStatus("current")
_RlOspfSummaryType3LsaTable_Object = MibTable
rlOspfSummaryType3LsaTable = _RlOspfSummaryType3LsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3)
)
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaTable.setStatus("current")
_RlOspfSummaryType3LsaEntry_Object = MibTableRow
rlOspfSummaryType3LsaEntry = _RlOspfSummaryType3LsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1)
)
rlOspfSummaryType3LsaEntry.setIndexNames(
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaProcessId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaAreaId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaLsid"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType3LsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaEntry.setStatus("current")
_RlOspfSummaryType3LsaProcessId_Type = RlOspfProcessID
_RlOspfSummaryType3LsaProcessId_Object = MibTableColumn
rlOspfSummaryType3LsaProcessId = _RlOspfSummaryType3LsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 1),
    _RlOspfSummaryType3LsaProcessId_Type()
)
rlOspfSummaryType3LsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaProcessId.setStatus("current")
_RlOspfSummaryType3LsaAreaId_Type = AreaID
_RlOspfSummaryType3LsaAreaId_Object = MibTableColumn
rlOspfSummaryType3LsaAreaId = _RlOspfSummaryType3LsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 2),
    _RlOspfSummaryType3LsaAreaId_Type()
)
rlOspfSummaryType3LsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaAreaId.setStatus("current")
_RlOspfSummaryType3LsaLsid_Type = IpAddress
_RlOspfSummaryType3LsaLsid_Object = MibTableColumn
rlOspfSummaryType3LsaLsid = _RlOspfSummaryType3LsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 3),
    _RlOspfSummaryType3LsaLsid_Type()
)
rlOspfSummaryType3LsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaLsid.setStatus("current")
_RlOspfSummaryType3LsaRouterId_Type = RouterID
_RlOspfSummaryType3LsaRouterId_Object = MibTableColumn
rlOspfSummaryType3LsaRouterId = _RlOspfSummaryType3LsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 4),
    _RlOspfSummaryType3LsaRouterId_Type()
)
rlOspfSummaryType3LsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaRouterId.setStatus("current")
_RlOspfSummaryType3LsaSequence_Type = Integer32
_RlOspfSummaryType3LsaSequence_Object = MibTableColumn
rlOspfSummaryType3LsaSequence = _RlOspfSummaryType3LsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 5),
    _RlOspfSummaryType3LsaSequence_Type()
)
rlOspfSummaryType3LsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaSequence.setStatus("current")
_RlOspfSummaryType3LsaAge_Type = Integer32
_RlOspfSummaryType3LsaAge_Object = MibTableColumn
rlOspfSummaryType3LsaAge = _RlOspfSummaryType3LsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 6),
    _RlOspfSummaryType3LsaAge_Type()
)
rlOspfSummaryType3LsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaAge.setStatus("current")
_RlOspfSummaryType3LsaChecksum_Type = Integer32
_RlOspfSummaryType3LsaChecksum_Object = MibTableColumn
rlOspfSummaryType3LsaChecksum = _RlOspfSummaryType3LsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 7),
    _RlOspfSummaryType3LsaChecksum_Type()
)
rlOspfSummaryType3LsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaChecksum.setStatus("current")
_RlOspfSummaryType3LsaLength_Type = Unsigned32
_RlOspfSummaryType3LsaLength_Object = MibTableColumn
rlOspfSummaryType3LsaLength = _RlOspfSummaryType3LsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 8),
    _RlOspfSummaryType3LsaLength_Type()
)
rlOspfSummaryType3LsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaLength.setStatus("current")
_RlOspfSummaryType3LsaMask_Type = IpAddress
_RlOspfSummaryType3LsaMask_Object = MibTableColumn
rlOspfSummaryType3LsaMask = _RlOspfSummaryType3LsaMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 9),
    _RlOspfSummaryType3LsaMask_Type()
)
rlOspfSummaryType3LsaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaMask.setStatus("current")
_RlOspfSummaryType3LsaMetric_Type = Unsigned32
_RlOspfSummaryType3LsaMetric_Object = MibTableColumn
rlOspfSummaryType3LsaMetric = _RlOspfSummaryType3LsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 3, 1, 10),
    _RlOspfSummaryType3LsaMetric_Type()
)
rlOspfSummaryType3LsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType3LsaMetric.setStatus("current")
_RlOspfSummaryType4LsaTable_Object = MibTable
rlOspfSummaryType4LsaTable = _RlOspfSummaryType4LsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4)
)
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaTable.setStatus("current")
_RlOspfSummaryType4LsaEntry_Object = MibTableRow
rlOspfSummaryType4LsaEntry = _RlOspfSummaryType4LsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1)
)
rlOspfSummaryType4LsaEntry.setIndexNames(
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaProcessId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaAreaId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaLsid"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfSummaryType4LsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaEntry.setStatus("current")
_RlOspfSummaryType4LsaProcessId_Type = RlOspfProcessID
_RlOspfSummaryType4LsaProcessId_Object = MibTableColumn
rlOspfSummaryType4LsaProcessId = _RlOspfSummaryType4LsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 1),
    _RlOspfSummaryType4LsaProcessId_Type()
)
rlOspfSummaryType4LsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaProcessId.setStatus("current")
_RlOspfSummaryType4LsaAreaId_Type = AreaID
_RlOspfSummaryType4LsaAreaId_Object = MibTableColumn
rlOspfSummaryType4LsaAreaId = _RlOspfSummaryType4LsaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 2),
    _RlOspfSummaryType4LsaAreaId_Type()
)
rlOspfSummaryType4LsaAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaAreaId.setStatus("current")
_RlOspfSummaryType4LsaLsid_Type = IpAddress
_RlOspfSummaryType4LsaLsid_Object = MibTableColumn
rlOspfSummaryType4LsaLsid = _RlOspfSummaryType4LsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 3),
    _RlOspfSummaryType4LsaLsid_Type()
)
rlOspfSummaryType4LsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaLsid.setStatus("current")
_RlOspfSummaryType4LsaRouterId_Type = RouterID
_RlOspfSummaryType4LsaRouterId_Object = MibTableColumn
rlOspfSummaryType4LsaRouterId = _RlOspfSummaryType4LsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 4),
    _RlOspfSummaryType4LsaRouterId_Type()
)
rlOspfSummaryType4LsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaRouterId.setStatus("current")
_RlOspfSummaryType4LsaSequence_Type = Integer32
_RlOspfSummaryType4LsaSequence_Object = MibTableColumn
rlOspfSummaryType4LsaSequence = _RlOspfSummaryType4LsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 5),
    _RlOspfSummaryType4LsaSequence_Type()
)
rlOspfSummaryType4LsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaSequence.setStatus("current")
_RlOspfSummaryType4LsaAge_Type = Integer32
_RlOspfSummaryType4LsaAge_Object = MibTableColumn
rlOspfSummaryType4LsaAge = _RlOspfSummaryType4LsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 6),
    _RlOspfSummaryType4LsaAge_Type()
)
rlOspfSummaryType4LsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaAge.setStatus("current")
_RlOspfSummaryType4LsaChecksum_Type = Integer32
_RlOspfSummaryType4LsaChecksum_Object = MibTableColumn
rlOspfSummaryType4LsaChecksum = _RlOspfSummaryType4LsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 7),
    _RlOspfSummaryType4LsaChecksum_Type()
)
rlOspfSummaryType4LsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaChecksum.setStatus("current")
_RlOspfSummaryType4LsaLength_Type = Unsigned32
_RlOspfSummaryType4LsaLength_Object = MibTableColumn
rlOspfSummaryType4LsaLength = _RlOspfSummaryType4LsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 8),
    _RlOspfSummaryType4LsaLength_Type()
)
rlOspfSummaryType4LsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaLength.setStatus("current")
_RlOspfSummaryType4LsaMetric_Type = Unsigned32
_RlOspfSummaryType4LsaMetric_Object = MibTableColumn
rlOspfSummaryType4LsaMetric = _RlOspfSummaryType4LsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 4, 1, 9),
    _RlOspfSummaryType4LsaMetric_Type()
)
rlOspfSummaryType4LsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSummaryType4LsaMetric.setStatus("current")
_RlOspfExternalLsaTable_Object = MibTable
rlOspfExternalLsaTable = _RlOspfExternalLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5)
)
if mibBuilder.loadTexts:
    rlOspfExternalLsaTable.setStatus("current")
_RlOspfExternalLsaEntry_Object = MibTableRow
rlOspfExternalLsaEntry = _RlOspfExternalLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1)
)
rlOspfExternalLsaEntry.setIndexNames(
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaProcessId"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaLsid"),
    (0, "RADLAN-OSPF-LSDB-MIB", "rlOspfExternalLsaRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfExternalLsaEntry.setStatus("current")
_RlOspfExternalLsaProcessId_Type = RlOspfProcessID
_RlOspfExternalLsaProcessId_Object = MibTableColumn
rlOspfExternalLsaProcessId = _RlOspfExternalLsaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 1),
    _RlOspfExternalLsaProcessId_Type()
)
rlOspfExternalLsaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaProcessId.setStatus("current")
_RlOspfExternalLsaLsid_Type = IpAddress
_RlOspfExternalLsaLsid_Object = MibTableColumn
rlOspfExternalLsaLsid = _RlOspfExternalLsaLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 2),
    _RlOspfExternalLsaLsid_Type()
)
rlOspfExternalLsaLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaLsid.setStatus("current")
_RlOspfExternalLsaRouterId_Type = RouterID
_RlOspfExternalLsaRouterId_Object = MibTableColumn
rlOspfExternalLsaRouterId = _RlOspfExternalLsaRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 3),
    _RlOspfExternalLsaRouterId_Type()
)
rlOspfExternalLsaRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaRouterId.setStatus("current")
_RlOspfExternalLsaSequence_Type = Integer32
_RlOspfExternalLsaSequence_Object = MibTableColumn
rlOspfExternalLsaSequence = _RlOspfExternalLsaSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 4),
    _RlOspfExternalLsaSequence_Type()
)
rlOspfExternalLsaSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaSequence.setStatus("current")
_RlOspfExternalLsaAge_Type = Integer32
_RlOspfExternalLsaAge_Object = MibTableColumn
rlOspfExternalLsaAge = _RlOspfExternalLsaAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 5),
    _RlOspfExternalLsaAge_Type()
)
rlOspfExternalLsaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaAge.setStatus("current")
_RlOspfExternalLsaChecksum_Type = Integer32
_RlOspfExternalLsaChecksum_Object = MibTableColumn
rlOspfExternalLsaChecksum = _RlOspfExternalLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 6),
    _RlOspfExternalLsaChecksum_Type()
)
rlOspfExternalLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaChecksum.setStatus("current")
_RlOspfExternalLsaLength_Type = Unsigned32
_RlOspfExternalLsaLength_Object = MibTableColumn
rlOspfExternalLsaLength = _RlOspfExternalLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 7),
    _RlOspfExternalLsaLength_Type()
)
rlOspfExternalLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaLength.setStatus("current")
_RlOspfExternalLsaMask_Type = IpAddress
_RlOspfExternalLsaMask_Object = MibTableColumn
rlOspfExternalLsaMask = _RlOspfExternalLsaMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 8),
    _RlOspfExternalLsaMask_Type()
)
rlOspfExternalLsaMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaMask.setStatus("current")
_RlOspfExternalLsaFrwAddress_Type = IpAddress
_RlOspfExternalLsaFrwAddress_Object = MibTableColumn
rlOspfExternalLsaFrwAddress = _RlOspfExternalLsaFrwAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 9),
    _RlOspfExternalLsaFrwAddress_Type()
)
rlOspfExternalLsaFrwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaFrwAddress.setStatus("current")


class _RlOspfExternalLsaBitE_Type(Integer32):
    """Custom type rlOspfExternalLsaBitE based on Integer32"""
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


_RlOspfExternalLsaBitE_Type.__name__ = "Integer32"
_RlOspfExternalLsaBitE_Object = MibTableColumn
rlOspfExternalLsaBitE = _RlOspfExternalLsaBitE_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 10),
    _RlOspfExternalLsaBitE_Type()
)
rlOspfExternalLsaBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaBitE.setStatus("current")
_RlOspfExternalLsaMetric_Type = Unsigned32
_RlOspfExternalLsaMetric_Object = MibTableColumn
rlOspfExternalLsaMetric = _RlOspfExternalLsaMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 11),
    _RlOspfExternalLsaMetric_Type()
)
rlOspfExternalLsaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaMetric.setStatus("current")
_RlOspfExternalLsaTag_Type = Unsigned32
_RlOspfExternalLsaTag_Object = MibTableColumn
rlOspfExternalLsaTag = _RlOspfExternalLsaTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 221, 5, 1, 12),
    _RlOspfExternalLsaTag_Type()
)
rlOspfExternalLsaTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternalLsaTag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-OSPF-LSDB-MIB",
    **{"rlOspfLsdb": rlOspfLsdb,
       "rlOspfRouterLsaTable": rlOspfRouterLsaTable,
       "rlOspfRouterLsaEntry": rlOspfRouterLsaEntry,
       "rlOspfRouterLsaProcessId": rlOspfRouterLsaProcessId,
       "rlOspfRouterLsaAreaId": rlOspfRouterLsaAreaId,
       "rlOspfRouterLsaLsid": rlOspfRouterLsaLsid,
       "rlOspfRouterLsaRouterId": rlOspfRouterLsaRouterId,
       "rlOspfRouterLsaIdx": rlOspfRouterLsaIdx,
       "rlOspfRouterLsaSequence": rlOspfRouterLsaSequence,
       "rlOspfRouterLsaAge": rlOspfRouterLsaAge,
       "rlOspfRouterLsaChecksum": rlOspfRouterLsaChecksum,
       "rlOspfRouterLsaLength": rlOspfRouterLsaLength,
       "rlOspfRouterLsaBitV": rlOspfRouterLsaBitV,
       "rlOspfRouterLsaBitE": rlOspfRouterLsaBitE,
       "rlOspfRouterLsaBitB": rlOspfRouterLsaBitB,
       "rlOspfRouterLsaLinks": rlOspfRouterLsaLinks,
       "rlOspfRouterLsaLinkID": rlOspfRouterLsaLinkID,
       "rlOspfRouterLsaLinkData": rlOspfRouterLsaLinkData,
       "rlOspfRouterLsaType": rlOspfRouterLsaType,
       "rlOspfRouterLsaMetric": rlOspfRouterLsaMetric,
       "rlOspfNetworkLsaTable": rlOspfNetworkLsaTable,
       "rlOspfNetworkLsaEntry": rlOspfNetworkLsaEntry,
       "rlOspfNetworkLsaProcessId": rlOspfNetworkLsaProcessId,
       "rlOspfNetworkLsaAreaId": rlOspfNetworkLsaAreaId,
       "rlOspfNetworkLsaLsid": rlOspfNetworkLsaLsid,
       "rlOspfNetworkLsaRouterId": rlOspfNetworkLsaRouterId,
       "rlOspfNetworkLsaIdx": rlOspfNetworkLsaIdx,
       "rlOspfNetworkLsaSequence": rlOspfNetworkLsaSequence,
       "rlOspfNetworkLsaAge": rlOspfNetworkLsaAge,
       "rlOspfNetworkLsaChecksum": rlOspfNetworkLsaChecksum,
       "rlOspfNetworkLsaLength": rlOspfNetworkLsaLength,
       "rlOspfNetworkLsaMask": rlOspfNetworkLsaMask,
       "rlOspfNetworkLsaAttRouter": rlOspfNetworkLsaAttRouter,
       "rlOspfSummaryType3LsaTable": rlOspfSummaryType3LsaTable,
       "rlOspfSummaryType3LsaEntry": rlOspfSummaryType3LsaEntry,
       "rlOspfSummaryType3LsaProcessId": rlOspfSummaryType3LsaProcessId,
       "rlOspfSummaryType3LsaAreaId": rlOspfSummaryType3LsaAreaId,
       "rlOspfSummaryType3LsaLsid": rlOspfSummaryType3LsaLsid,
       "rlOspfSummaryType3LsaRouterId": rlOspfSummaryType3LsaRouterId,
       "rlOspfSummaryType3LsaSequence": rlOspfSummaryType3LsaSequence,
       "rlOspfSummaryType3LsaAge": rlOspfSummaryType3LsaAge,
       "rlOspfSummaryType3LsaChecksum": rlOspfSummaryType3LsaChecksum,
       "rlOspfSummaryType3LsaLength": rlOspfSummaryType3LsaLength,
       "rlOspfSummaryType3LsaMask": rlOspfSummaryType3LsaMask,
       "rlOspfSummaryType3LsaMetric": rlOspfSummaryType3LsaMetric,
       "rlOspfSummaryType4LsaTable": rlOspfSummaryType4LsaTable,
       "rlOspfSummaryType4LsaEntry": rlOspfSummaryType4LsaEntry,
       "rlOspfSummaryType4LsaProcessId": rlOspfSummaryType4LsaProcessId,
       "rlOspfSummaryType4LsaAreaId": rlOspfSummaryType4LsaAreaId,
       "rlOspfSummaryType4LsaLsid": rlOspfSummaryType4LsaLsid,
       "rlOspfSummaryType4LsaRouterId": rlOspfSummaryType4LsaRouterId,
       "rlOspfSummaryType4LsaSequence": rlOspfSummaryType4LsaSequence,
       "rlOspfSummaryType4LsaAge": rlOspfSummaryType4LsaAge,
       "rlOspfSummaryType4LsaChecksum": rlOspfSummaryType4LsaChecksum,
       "rlOspfSummaryType4LsaLength": rlOspfSummaryType4LsaLength,
       "rlOspfSummaryType4LsaMetric": rlOspfSummaryType4LsaMetric,
       "rlOspfExternalLsaTable": rlOspfExternalLsaTable,
       "rlOspfExternalLsaEntry": rlOspfExternalLsaEntry,
       "rlOspfExternalLsaProcessId": rlOspfExternalLsaProcessId,
       "rlOspfExternalLsaLsid": rlOspfExternalLsaLsid,
       "rlOspfExternalLsaRouterId": rlOspfExternalLsaRouterId,
       "rlOspfExternalLsaSequence": rlOspfExternalLsaSequence,
       "rlOspfExternalLsaAge": rlOspfExternalLsaAge,
       "rlOspfExternalLsaChecksum": rlOspfExternalLsaChecksum,
       "rlOspfExternalLsaLength": rlOspfExternalLsaLength,
       "rlOspfExternalLsaMask": rlOspfExternalLsaMask,
       "rlOspfExternalLsaFrwAddress": rlOspfExternalLsaFrwAddress,
       "rlOspfExternalLsaBitE": rlOspfExternalLsaBitE,
       "rlOspfExternalLsaMetric": rlOspfExternalLsaMetric,
       "rlOspfExternalLsaTag": rlOspfExternalLsaTag}
)
