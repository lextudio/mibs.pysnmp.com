# SNMP MIB module (CISCO-IETF-MPLS-TE-P2MP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-MPLS-TE-P2MP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:43 2024
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

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsLabel,
 MplsPathIndexOrZero) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel",
    "MplsPathIndexOrZero")

(mplsTunnelEgressLSRId,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelEgressLSRId",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cmplsTeP2mpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142)
)
cmplsTeP2mpStdMIB.setRevisions(
        ("2009-09-30 00:00",
         "2009-09-01 00:00",
         "2009-05-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmplsTeP2mpNotifications_ObjectIdentity = ObjectIdentity
cmplsTeP2mpNotifications = _CmplsTeP2mpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 0)
)
_CmplsTeP2mpScalars_ObjectIdentity = ObjectIdentity
cmplsTeP2mpScalars = _CmplsTeP2mpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 1)
)
_CmplsTeP2mpTunnelConfigured_Type = Unsigned32
_CmplsTeP2mpTunnelConfigured_Object = MibScalar
cmplsTeP2mpTunnelConfigured = _CmplsTeP2mpTunnelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 1, 1),
    _CmplsTeP2mpTunnelConfigured_Type()
)
cmplsTeP2mpTunnelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelConfigured.setStatus("current")
_CmplsTeP2mpTunnelActive_Type = Unsigned32
_CmplsTeP2mpTunnelActive_Object = MibScalar
cmplsTeP2mpTunnelActive = _CmplsTeP2mpTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 1, 2),
    _CmplsTeP2mpTunnelActive_Type()
)
cmplsTeP2mpTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelActive.setStatus("current")
_CmplsTeP2mpTunnelTotalMaxHops_Type = Unsigned32
_CmplsTeP2mpTunnelTotalMaxHops_Object = MibScalar
cmplsTeP2mpTunnelTotalMaxHops = _CmplsTeP2mpTunnelTotalMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 1, 3),
    _CmplsTeP2mpTunnelTotalMaxHops_Type()
)
cmplsTeP2mpTunnelTotalMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelTotalMaxHops.setStatus("current")
_CmplsTeP2mpObjects_ObjectIdentity = ObjectIdentity
cmplsTeP2mpObjects = _CmplsTeP2mpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2)
)
_CmplsTeP2mpTunnelTable_Object = MibTable
cmplsTeP2mpTunnelTable = _CmplsTeP2mpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelTable.setStatus("current")
_CmplsTeP2mpTunnelEntry_Object = MibTableRow
cmplsTeP2mpTunnelEntry = _CmplsTeP2mpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1)
)
cmplsTeP2mpTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelEntry.setStatus("current")


class _CmplsTeP2mpTunnelP2mpIntegrity_Type(TruthValue):
    """Custom type cmplsTeP2mpTunnelP2mpIntegrity based on TruthValue"""


_CmplsTeP2mpTunnelP2mpIntegrity_Object = MibTableColumn
cmplsTeP2mpTunnelP2mpIntegrity = _CmplsTeP2mpTunnelP2mpIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1, 2),
    _CmplsTeP2mpTunnelP2mpIntegrity_Type()
)
cmplsTeP2mpTunnelP2mpIntegrity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelP2mpIntegrity.setStatus("current")


class _CmplsTeP2mpTunnelBranchRole_Type(Integer32):
    """Custom type cmplsTeP2mpTunnelBranchRole based on Integer32"""
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
        *(("branch", 2),
          ("bud", 3),
          ("notBranch", 1))
    )


_CmplsTeP2mpTunnelBranchRole_Type.__name__ = "Integer32"
_CmplsTeP2mpTunnelBranchRole_Object = MibTableColumn
cmplsTeP2mpTunnelBranchRole = _CmplsTeP2mpTunnelBranchRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1, 3),
    _CmplsTeP2mpTunnelBranchRole_Type()
)
cmplsTeP2mpTunnelBranchRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchRole.setStatus("current")
_CmplsTeP2mpTunnelP2mpXcIndex_Type = MplsIndexType
_CmplsTeP2mpTunnelP2mpXcIndex_Object = MibTableColumn
cmplsTeP2mpTunnelP2mpXcIndex = _CmplsTeP2mpTunnelP2mpXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1, 4),
    _CmplsTeP2mpTunnelP2mpXcIndex_Type()
)
cmplsTeP2mpTunnelP2mpXcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelP2mpXcIndex.setStatus("current")
_CmplsTeP2mpTunnelRowStatus_Type = RowStatus
_CmplsTeP2mpTunnelRowStatus_Object = MibTableColumn
cmplsTeP2mpTunnelRowStatus = _CmplsTeP2mpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1, 5),
    _CmplsTeP2mpTunnelRowStatus_Type()
)
cmplsTeP2mpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelRowStatus.setStatus("current")


class _CmplsTeP2mpTunnelStorageType_Type(StorageType):
    """Custom type cmplsTeP2mpTunnelStorageType based on StorageType"""


_CmplsTeP2mpTunnelStorageType_Object = MibTableColumn
cmplsTeP2mpTunnelStorageType = _CmplsTeP2mpTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 1, 1, 6),
    _CmplsTeP2mpTunnelStorageType_Type()
)
cmplsTeP2mpTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelStorageType.setStatus("current")


class _CmplsTeP2mpTunnelSubGroupIDNext_Type(IndexIntegerNextFree):
    """Custom type cmplsTeP2mpTunnelSubGroupIDNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmplsTeP2mpTunnelSubGroupIDNext_Type.__name__ = "IndexIntegerNextFree"
_CmplsTeP2mpTunnelSubGroupIDNext_Object = MibScalar
cmplsTeP2mpTunnelSubGroupIDNext = _CmplsTeP2mpTunnelSubGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 2),
    _CmplsTeP2mpTunnelSubGroupIDNext_Type()
)
cmplsTeP2mpTunnelSubGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelSubGroupIDNext.setStatus("current")
_CmplsTeP2mpTunnelDestTable_Object = MibTable
cmplsTeP2mpTunnelDestTable = _CmplsTeP2mpTunnelDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestTable.setStatus("current")
_CmplsTeP2mpTunnelDestEntry_Object = MibTableRow
cmplsTeP2mpTunnelDestEntry = _CmplsTeP2mpTunnelDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1)
)
cmplsTeP2mpTunnelDestEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSrcSubGroupOriginType"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSrcSubGroupOrigin"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSrcSubGroupID"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSubGroupOriginType"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSubGroupOrigin"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestSubGroupID"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestDestinationType"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestDestination"),
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestEntry.setStatus("current")
_CmplsTeP2mpTunnelDestSrcSubGroupOriginType_Type = InetAddressType
_CmplsTeP2mpTunnelDestSrcSubGroupOriginType_Object = MibTableColumn
cmplsTeP2mpTunnelDestSrcSubGroupOriginType = _CmplsTeP2mpTunnelDestSrcSubGroupOriginType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 1),
    _CmplsTeP2mpTunnelDestSrcSubGroupOriginType_Type()
)
cmplsTeP2mpTunnelDestSrcSubGroupOriginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSrcSubGroupOriginType.setStatus("current")


class _CmplsTeP2mpTunnelDestSrcSubGroupOrigin_Type(InetAddress):
    """Custom type cmplsTeP2mpTunnelDestSrcSubGroupOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmplsTeP2mpTunnelDestSrcSubGroupOrigin_Type.__name__ = "InetAddress"
_CmplsTeP2mpTunnelDestSrcSubGroupOrigin_Object = MibTableColumn
cmplsTeP2mpTunnelDestSrcSubGroupOrigin = _CmplsTeP2mpTunnelDestSrcSubGroupOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 2),
    _CmplsTeP2mpTunnelDestSrcSubGroupOrigin_Type()
)
cmplsTeP2mpTunnelDestSrcSubGroupOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSrcSubGroupOrigin.setStatus("current")


class _CmplsTeP2mpTunnelDestSrcSubGroupID_Type(IndexInteger):
    """Custom type cmplsTeP2mpTunnelDestSrcSubGroupID based on IndexInteger"""
    subtypeSpec = IndexInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmplsTeP2mpTunnelDestSrcSubGroupID_Type.__name__ = "IndexInteger"
_CmplsTeP2mpTunnelDestSrcSubGroupID_Object = MibTableColumn
cmplsTeP2mpTunnelDestSrcSubGroupID = _CmplsTeP2mpTunnelDestSrcSubGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 3),
    _CmplsTeP2mpTunnelDestSrcSubGroupID_Type()
)
cmplsTeP2mpTunnelDestSrcSubGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSrcSubGroupID.setStatus("current")
_CmplsTeP2mpTunnelDestSubGroupOriginType_Type = InetAddressType
_CmplsTeP2mpTunnelDestSubGroupOriginType_Object = MibTableColumn
cmplsTeP2mpTunnelDestSubGroupOriginType = _CmplsTeP2mpTunnelDestSubGroupOriginType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 4),
    _CmplsTeP2mpTunnelDestSubGroupOriginType_Type()
)
cmplsTeP2mpTunnelDestSubGroupOriginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSubGroupOriginType.setStatus("current")


class _CmplsTeP2mpTunnelDestSubGroupOrigin_Type(InetAddress):
    """Custom type cmplsTeP2mpTunnelDestSubGroupOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmplsTeP2mpTunnelDestSubGroupOrigin_Type.__name__ = "InetAddress"
_CmplsTeP2mpTunnelDestSubGroupOrigin_Object = MibTableColumn
cmplsTeP2mpTunnelDestSubGroupOrigin = _CmplsTeP2mpTunnelDestSubGroupOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 5),
    _CmplsTeP2mpTunnelDestSubGroupOrigin_Type()
)
cmplsTeP2mpTunnelDestSubGroupOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSubGroupOrigin.setStatus("current")


class _CmplsTeP2mpTunnelDestSubGroupID_Type(IndexInteger):
    """Custom type cmplsTeP2mpTunnelDestSubGroupID based on IndexInteger"""
    subtypeSpec = IndexInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmplsTeP2mpTunnelDestSubGroupID_Type.__name__ = "IndexInteger"
_CmplsTeP2mpTunnelDestSubGroupID_Object = MibTableColumn
cmplsTeP2mpTunnelDestSubGroupID = _CmplsTeP2mpTunnelDestSubGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 6),
    _CmplsTeP2mpTunnelDestSubGroupID_Type()
)
cmplsTeP2mpTunnelDestSubGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestSubGroupID.setStatus("current")
_CmplsTeP2mpTunnelDestDestinationType_Type = InetAddressType
_CmplsTeP2mpTunnelDestDestinationType_Object = MibTableColumn
cmplsTeP2mpTunnelDestDestinationType = _CmplsTeP2mpTunnelDestDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 7),
    _CmplsTeP2mpTunnelDestDestinationType_Type()
)
cmplsTeP2mpTunnelDestDestinationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestDestinationType.setStatus("current")


class _CmplsTeP2mpTunnelDestDestination_Type(InetAddress):
    """Custom type cmplsTeP2mpTunnelDestDestination based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmplsTeP2mpTunnelDestDestination_Type.__name__ = "InetAddress"
_CmplsTeP2mpTunnelDestDestination_Object = MibTableColumn
cmplsTeP2mpTunnelDestDestination = _CmplsTeP2mpTunnelDestDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 8),
    _CmplsTeP2mpTunnelDestDestination_Type()
)
cmplsTeP2mpTunnelDestDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestDestination.setStatus("current")
_CmplsTeP2mpTunnelDestBranchOutSegment_Type = MplsIndexType
_CmplsTeP2mpTunnelDestBranchOutSegment_Object = MibTableColumn
cmplsTeP2mpTunnelDestBranchOutSegment = _CmplsTeP2mpTunnelDestBranchOutSegment_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 9),
    _CmplsTeP2mpTunnelDestBranchOutSegment_Type()
)
cmplsTeP2mpTunnelDestBranchOutSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestBranchOutSegment.setStatus("current")


class _CmplsTeP2mpTunnelDestHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type cmplsTeP2mpTunnelDestHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_CmplsTeP2mpTunnelDestHopTableIndex_Object = MibTableColumn
cmplsTeP2mpTunnelDestHopTableIndex = _CmplsTeP2mpTunnelDestHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 10),
    _CmplsTeP2mpTunnelDestHopTableIndex_Type()
)
cmplsTeP2mpTunnelDestHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestHopTableIndex.setStatus("current")


class _CmplsTeP2mpTunnelDestPathInUse_Type(MplsPathIndexOrZero):
    """Custom type cmplsTeP2mpTunnelDestPathInUse based on MplsPathIndexOrZero"""
    defaultValue = 0


_CmplsTeP2mpTunnelDestPathInUse_Object = MibTableColumn
cmplsTeP2mpTunnelDestPathInUse = _CmplsTeP2mpTunnelDestPathInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 11),
    _CmplsTeP2mpTunnelDestPathInUse_Type()
)
cmplsTeP2mpTunnelDestPathInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestPathInUse.setStatus("current")
_CmplsTeP2mpTunnelDestCHopTableIndex_Type = MplsPathIndexOrZero
_CmplsTeP2mpTunnelDestCHopTableIndex_Object = MibTableColumn
cmplsTeP2mpTunnelDestCHopTableIndex = _CmplsTeP2mpTunnelDestCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 12),
    _CmplsTeP2mpTunnelDestCHopTableIndex_Type()
)
cmplsTeP2mpTunnelDestCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestCHopTableIndex.setStatus("current")
_CmplsTeP2mpTunnelDestARHopTableIndex_Type = MplsPathIndexOrZero
_CmplsTeP2mpTunnelDestARHopTableIndex_Object = MibTableColumn
cmplsTeP2mpTunnelDestARHopTableIndex = _CmplsTeP2mpTunnelDestARHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 13),
    _CmplsTeP2mpTunnelDestARHopTableIndex_Type()
)
cmplsTeP2mpTunnelDestARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestARHopTableIndex.setStatus("current")
_CmplsTeP2mpTunnelDestTotalUpTime_Type = TimeTicks
_CmplsTeP2mpTunnelDestTotalUpTime_Object = MibTableColumn
cmplsTeP2mpTunnelDestTotalUpTime = _CmplsTeP2mpTunnelDestTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 14),
    _CmplsTeP2mpTunnelDestTotalUpTime_Type()
)
cmplsTeP2mpTunnelDestTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestTotalUpTime.setStatus("current")
_CmplsTeP2mpTunnelDestInstanceUpTime_Type = TimeTicks
_CmplsTeP2mpTunnelDestInstanceUpTime_Object = MibTableColumn
cmplsTeP2mpTunnelDestInstanceUpTime = _CmplsTeP2mpTunnelDestInstanceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 15),
    _CmplsTeP2mpTunnelDestInstanceUpTime_Type()
)
cmplsTeP2mpTunnelDestInstanceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestInstanceUpTime.setStatus("current")
_CmplsTeP2mpTunnelDestPathChanges_Type = Counter32
_CmplsTeP2mpTunnelDestPathChanges_Object = MibTableColumn
cmplsTeP2mpTunnelDestPathChanges = _CmplsTeP2mpTunnelDestPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 16),
    _CmplsTeP2mpTunnelDestPathChanges_Type()
)
cmplsTeP2mpTunnelDestPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestPathChanges.setStatus("current")
_CmplsTeP2mpTunnelDestLastPathChange_Type = TimeTicks
_CmplsTeP2mpTunnelDestLastPathChange_Object = MibTableColumn
cmplsTeP2mpTunnelDestLastPathChange = _CmplsTeP2mpTunnelDestLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 17),
    _CmplsTeP2mpTunnelDestLastPathChange_Type()
)
cmplsTeP2mpTunnelDestLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestLastPathChange.setStatus("current")
_CmplsTeP2mpTunnelDestCreationTime_Type = TimeStamp
_CmplsTeP2mpTunnelDestCreationTime_Object = MibTableColumn
cmplsTeP2mpTunnelDestCreationTime = _CmplsTeP2mpTunnelDestCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 18),
    _CmplsTeP2mpTunnelDestCreationTime_Type()
)
cmplsTeP2mpTunnelDestCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestCreationTime.setStatus("current")
_CmplsTeP2mpTunnelDestStateTransitions_Type = Counter32
_CmplsTeP2mpTunnelDestStateTransitions_Object = MibTableColumn
cmplsTeP2mpTunnelDestStateTransitions = _CmplsTeP2mpTunnelDestStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 19),
    _CmplsTeP2mpTunnelDestStateTransitions_Type()
)
cmplsTeP2mpTunnelDestStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestStateTransitions.setStatus("current")
_CmplsTeP2mpTunnelDestDiscontinuityTime_Type = TimeStamp
_CmplsTeP2mpTunnelDestDiscontinuityTime_Object = MibTableColumn
cmplsTeP2mpTunnelDestDiscontinuityTime = _CmplsTeP2mpTunnelDestDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 20),
    _CmplsTeP2mpTunnelDestDiscontinuityTime_Type()
)
cmplsTeP2mpTunnelDestDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestDiscontinuityTime.setStatus("current")


class _CmplsTeP2mpTunnelDestAdminStatus_Type(Integer32):
    """Custom type cmplsTeP2mpTunnelDestAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CmplsTeP2mpTunnelDestAdminStatus_Type.__name__ = "Integer32"
_CmplsTeP2mpTunnelDestAdminStatus_Object = MibTableColumn
cmplsTeP2mpTunnelDestAdminStatus = _CmplsTeP2mpTunnelDestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 21),
    _CmplsTeP2mpTunnelDestAdminStatus_Type()
)
cmplsTeP2mpTunnelDestAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestAdminStatus.setStatus("current")


class _CmplsTeP2mpTunnelDestOperStatus_Type(Integer32):
    """Custom type cmplsTeP2mpTunnelDestOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("lowerLayerDown", 7),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_CmplsTeP2mpTunnelDestOperStatus_Type.__name__ = "Integer32"
_CmplsTeP2mpTunnelDestOperStatus_Object = MibTableColumn
cmplsTeP2mpTunnelDestOperStatus = _CmplsTeP2mpTunnelDestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 22),
    _CmplsTeP2mpTunnelDestOperStatus_Type()
)
cmplsTeP2mpTunnelDestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestOperStatus.setStatus("current")
_CmplsTeP2mpTunnelDestRowStatus_Type = RowStatus
_CmplsTeP2mpTunnelDestRowStatus_Object = MibTableColumn
cmplsTeP2mpTunnelDestRowStatus = _CmplsTeP2mpTunnelDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 23),
    _CmplsTeP2mpTunnelDestRowStatus_Type()
)
cmplsTeP2mpTunnelDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestRowStatus.setStatus("current")


class _CmplsTeP2mpTunnelDestStorageType_Type(StorageType):
    """Custom type cmplsTeP2mpTunnelDestStorageType based on StorageType"""


_CmplsTeP2mpTunnelDestStorageType_Object = MibTableColumn
cmplsTeP2mpTunnelDestStorageType = _CmplsTeP2mpTunnelDestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 3, 1, 24),
    _CmplsTeP2mpTunnelDestStorageType_Type()
)
cmplsTeP2mpTunnelDestStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestStorageType.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfTable_Object = MibTable
cmplsTeP2mpTunnelBranchPerfTable = _CmplsTeP2mpTunnelBranchPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfTable.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfEntry_Object = MibTableRow
cmplsTeP2mpTunnelBranchPerfEntry = _CmplsTeP2mpTunnelBranchPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1)
)
cmplsTeP2mpTunnelBranchPerfEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
    (0, "CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfBranch"),
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfEntry.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfBranch_Type = MplsIndexType
_CmplsTeP2mpTunnelBranchPerfBranch_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfBranch = _CmplsTeP2mpTunnelBranchPerfBranch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 1),
    _CmplsTeP2mpTunnelBranchPerfBranch_Type()
)
cmplsTeP2mpTunnelBranchPerfBranch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfBranch.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfPackets_Type = Counter32
_CmplsTeP2mpTunnelBranchPerfPackets_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfPackets = _CmplsTeP2mpTunnelBranchPerfPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 2),
    _CmplsTeP2mpTunnelBranchPerfPackets_Type()
)
cmplsTeP2mpTunnelBranchPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfPackets.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfHCPackets_Type = Counter64
_CmplsTeP2mpTunnelBranchPerfHCPackets_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfHCPackets = _CmplsTeP2mpTunnelBranchPerfHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 3),
    _CmplsTeP2mpTunnelBranchPerfHCPackets_Type()
)
cmplsTeP2mpTunnelBranchPerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfHCPackets.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfErrors_Type = Counter32
_CmplsTeP2mpTunnelBranchPerfErrors_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfErrors = _CmplsTeP2mpTunnelBranchPerfErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 4),
    _CmplsTeP2mpTunnelBranchPerfErrors_Type()
)
cmplsTeP2mpTunnelBranchPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfErrors.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfBytes_Type = Counter32
_CmplsTeP2mpTunnelBranchPerfBytes_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfBytes = _CmplsTeP2mpTunnelBranchPerfBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 5),
    _CmplsTeP2mpTunnelBranchPerfBytes_Type()
)
cmplsTeP2mpTunnelBranchPerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfBytes.setStatus("current")
_CmplsTeP2mpTunnelBranchPerfHCBytes_Type = Counter64
_CmplsTeP2mpTunnelBranchPerfHCBytes_Object = MibTableColumn
cmplsTeP2mpTunnelBranchPerfHCBytes = _CmplsTeP2mpTunnelBranchPerfHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 6),
    _CmplsTeP2mpTunnelBranchPerfHCBytes_Type()
)
cmplsTeP2mpTunnelBranchPerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchPerfHCBytes.setStatus("current")
_CmplsTeP2mpTunnelBranchDiscontinuityTime_Type = TimeStamp
_CmplsTeP2mpTunnelBranchDiscontinuityTime_Object = MibTableColumn
cmplsTeP2mpTunnelBranchDiscontinuityTime = _CmplsTeP2mpTunnelBranchDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 7),
    _CmplsTeP2mpTunnelBranchDiscontinuityTime_Type()
)
cmplsTeP2mpTunnelBranchDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchDiscontinuityTime.setStatus("current")
_CmplsTeP2mpTunnelBranchLocalLabel_Type = MplsLabel
_CmplsTeP2mpTunnelBranchLocalLabel_Object = MibTableColumn
cmplsTeP2mpTunnelBranchLocalLabel = _CmplsTeP2mpTunnelBranchLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 8),
    _CmplsTeP2mpTunnelBranchLocalLabel_Type()
)
cmplsTeP2mpTunnelBranchLocalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchLocalLabel.setStatus("current")
_CmplsTeP2mpTunnelBranchOutIfIndex_Type = InterfaceIndexOrZero
_CmplsTeP2mpTunnelBranchOutIfIndex_Object = MibTableColumn
cmplsTeP2mpTunnelBranchOutIfIndex = _CmplsTeP2mpTunnelBranchOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 9),
    _CmplsTeP2mpTunnelBranchOutIfIndex_Type()
)
cmplsTeP2mpTunnelBranchOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchOutIfIndex.setStatus("current")
_CmplsTeP2mpTunnelBranchOutLabel_Type = MplsLabel
_CmplsTeP2mpTunnelBranchOutLabel_Object = MibTableColumn
cmplsTeP2mpTunnelBranchOutLabel = _CmplsTeP2mpTunnelBranchOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 10),
    _CmplsTeP2mpTunnelBranchOutLabel_Type()
)
cmplsTeP2mpTunnelBranchOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchOutLabel.setStatus("current")
_CmplsTeP2mpTunnelBranchSignalArea_Type = OctetString
_CmplsTeP2mpTunnelBranchSignalArea_Object = MibTableColumn
cmplsTeP2mpTunnelBranchSignalArea = _CmplsTeP2mpTunnelBranchSignalArea_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 11),
    _CmplsTeP2mpTunnelBranchSignalArea_Type()
)
cmplsTeP2mpTunnelBranchSignalArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchSignalArea.setStatus("current")
_CmplsTeP2mpTunnelBranchInIfIndex_Type = InterfaceIndexOrZero
_CmplsTeP2mpTunnelBranchInIfIndex_Object = MibTableColumn
cmplsTeP2mpTunnelBranchInIfIndex = _CmplsTeP2mpTunnelBranchInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 4, 1, 12),
    _CmplsTeP2mpTunnelBranchInIfIndex_Type()
)
cmplsTeP2mpTunnelBranchInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelBranchInIfIndex.setStatus("current")


class _CmplsTeP2mpTunnelNotificationEnable_Type(TruthValue):
    """Custom type cmplsTeP2mpTunnelNotificationEnable based on TruthValue"""


_CmplsTeP2mpTunnelNotificationEnable_Object = MibScalar
cmplsTeP2mpTunnelNotificationEnable = _CmplsTeP2mpTunnelNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 2, 5),
    _CmplsTeP2mpTunnelNotificationEnable_Type()
)
cmplsTeP2mpTunnelNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelNotificationEnable.setStatus("current")
_CmplsTeP2mpConformance_ObjectIdentity = ObjectIdentity
cmplsTeP2mpConformance = _CmplsTeP2mpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3)
)
_CmplsTeP2mpGroups_ObjectIdentity = ObjectIdentity
cmplsTeP2mpGroups = _CmplsTeP2mpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1)
)
_CmplsTeP2mpCompliances_ObjectIdentity = ObjectIdentity
cmplsTeP2mpCompliances = _CmplsTeP2mpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2)
)

# Managed Objects groups

cmplsTeP2mpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1, 1)
)
cmplsTeP2mpGeneralGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelConfigured"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelActive"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelTotalMaxHops"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelP2mpIntegrity"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchRole"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelP2mpXcIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelRowStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelStorageType"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelSubGroupIDNext"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestBranchOutSegment"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestHopTableIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestPathInUse"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestCHopTableIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestARHopTableIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestTotalUpTime"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestInstanceUpTime"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestPathChanges"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestLastPathChange"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestCreationTime"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestStateTransitions"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestDiscontinuityTime"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestAdminStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestOperStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestRowStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestStorageType"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfPackets"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfHCPackets"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfErrors"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfBytes"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchPerfHCBytes"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchDiscontinuityTime"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchLocalLabel"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchOutIfIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchOutLabel"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchSignalArea"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchInIfIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelNotificationEnable"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpGeneralGroup.setStatus("current")

cmplsTeP2mpScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1, 3)
)
cmplsTeP2mpScalarGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelConfigured"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelActive"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelTotalMaxHops"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpScalarGroup.setStatus("current")

cmplsTeP2mpGeneralGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1, 4)
)
cmplsTeP2mpGeneralGroupSup1.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchLocalLabel"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchOutIfIndex"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchOutLabel"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchSignalArea"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpGeneralGroupSup1.setStatus("current")

cmplsTeP2mpGeneralGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1, 5)
)
cmplsTeP2mpGeneralGroupSup2.setObjects(
    ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelBranchInIfIndex")
)
if mibBuilder.loadTexts:
    cmplsTeP2mpGeneralGroupSup2.setStatus("current")


# Notification objects

cmplsTeP2mpTunnelDestUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 0, 1)
)
cmplsTeP2mpTunnelDestUp.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestAdminStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestOperStatus"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestUp.setStatus(
        "current"
    )

cmplsTeP2mpTunnelDestDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 0, 2)
)
cmplsTeP2mpTunnelDestDown.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestAdminStatus"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestOperStatus"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpTunnelDestDown.setStatus(
        "current"
    )


# Notifications groups

cmplsTeP2mpNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 1, 2)
)
cmplsTeP2mpNotifGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestUp"),
        ("CISCO-IETF-MPLS-TE-P2MP-STD-MIB", "cmplsTeP2mpTunnelDestDown"))
)
if mibBuilder.loadTexts:
    cmplsTeP2mpNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmplsTeP2mpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleFullCompliance.setStatus(
        "deprecated"
    )

cmplsTeP2mpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleReadOnlyCompliance.setStatus(
        "deprecated"
    )

cmplsTeP2mpModuleFullComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleFullComplianceRev1.setStatus(
        "deprecated"
    )

cmplsTeP2mpModuleReadOnlyComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 4)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleReadOnlyComplianceRev1.setStatus(
        "deprecated"
    )

cmplsTeP2mpModuleFullComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 5)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleFullComplianceRev2.setStatus(
        "current"
    )

cmplsTeP2mpModuleReadOnlyComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 142, 3, 2, 6)
)
if mibBuilder.loadTexts:
    cmplsTeP2mpModuleReadOnlyComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-MPLS-TE-P2MP-STD-MIB",
    **{"cmplsTeP2mpStdMIB": cmplsTeP2mpStdMIB,
       "cmplsTeP2mpNotifications": cmplsTeP2mpNotifications,
       "cmplsTeP2mpTunnelDestUp": cmplsTeP2mpTunnelDestUp,
       "cmplsTeP2mpTunnelDestDown": cmplsTeP2mpTunnelDestDown,
       "cmplsTeP2mpScalars": cmplsTeP2mpScalars,
       "cmplsTeP2mpTunnelConfigured": cmplsTeP2mpTunnelConfigured,
       "cmplsTeP2mpTunnelActive": cmplsTeP2mpTunnelActive,
       "cmplsTeP2mpTunnelTotalMaxHops": cmplsTeP2mpTunnelTotalMaxHops,
       "cmplsTeP2mpObjects": cmplsTeP2mpObjects,
       "cmplsTeP2mpTunnelTable": cmplsTeP2mpTunnelTable,
       "cmplsTeP2mpTunnelEntry": cmplsTeP2mpTunnelEntry,
       "cmplsTeP2mpTunnelP2mpIntegrity": cmplsTeP2mpTunnelP2mpIntegrity,
       "cmplsTeP2mpTunnelBranchRole": cmplsTeP2mpTunnelBranchRole,
       "cmplsTeP2mpTunnelP2mpXcIndex": cmplsTeP2mpTunnelP2mpXcIndex,
       "cmplsTeP2mpTunnelRowStatus": cmplsTeP2mpTunnelRowStatus,
       "cmplsTeP2mpTunnelStorageType": cmplsTeP2mpTunnelStorageType,
       "cmplsTeP2mpTunnelSubGroupIDNext": cmplsTeP2mpTunnelSubGroupIDNext,
       "cmplsTeP2mpTunnelDestTable": cmplsTeP2mpTunnelDestTable,
       "cmplsTeP2mpTunnelDestEntry": cmplsTeP2mpTunnelDestEntry,
       "cmplsTeP2mpTunnelDestSrcSubGroupOriginType": cmplsTeP2mpTunnelDestSrcSubGroupOriginType,
       "cmplsTeP2mpTunnelDestSrcSubGroupOrigin": cmplsTeP2mpTunnelDestSrcSubGroupOrigin,
       "cmplsTeP2mpTunnelDestSrcSubGroupID": cmplsTeP2mpTunnelDestSrcSubGroupID,
       "cmplsTeP2mpTunnelDestSubGroupOriginType": cmplsTeP2mpTunnelDestSubGroupOriginType,
       "cmplsTeP2mpTunnelDestSubGroupOrigin": cmplsTeP2mpTunnelDestSubGroupOrigin,
       "cmplsTeP2mpTunnelDestSubGroupID": cmplsTeP2mpTunnelDestSubGroupID,
       "cmplsTeP2mpTunnelDestDestinationType": cmplsTeP2mpTunnelDestDestinationType,
       "cmplsTeP2mpTunnelDestDestination": cmplsTeP2mpTunnelDestDestination,
       "cmplsTeP2mpTunnelDestBranchOutSegment": cmplsTeP2mpTunnelDestBranchOutSegment,
       "cmplsTeP2mpTunnelDestHopTableIndex": cmplsTeP2mpTunnelDestHopTableIndex,
       "cmplsTeP2mpTunnelDestPathInUse": cmplsTeP2mpTunnelDestPathInUse,
       "cmplsTeP2mpTunnelDestCHopTableIndex": cmplsTeP2mpTunnelDestCHopTableIndex,
       "cmplsTeP2mpTunnelDestARHopTableIndex": cmplsTeP2mpTunnelDestARHopTableIndex,
       "cmplsTeP2mpTunnelDestTotalUpTime": cmplsTeP2mpTunnelDestTotalUpTime,
       "cmplsTeP2mpTunnelDestInstanceUpTime": cmplsTeP2mpTunnelDestInstanceUpTime,
       "cmplsTeP2mpTunnelDestPathChanges": cmplsTeP2mpTunnelDestPathChanges,
       "cmplsTeP2mpTunnelDestLastPathChange": cmplsTeP2mpTunnelDestLastPathChange,
       "cmplsTeP2mpTunnelDestCreationTime": cmplsTeP2mpTunnelDestCreationTime,
       "cmplsTeP2mpTunnelDestStateTransitions": cmplsTeP2mpTunnelDestStateTransitions,
       "cmplsTeP2mpTunnelDestDiscontinuityTime": cmplsTeP2mpTunnelDestDiscontinuityTime,
       "cmplsTeP2mpTunnelDestAdminStatus": cmplsTeP2mpTunnelDestAdminStatus,
       "cmplsTeP2mpTunnelDestOperStatus": cmplsTeP2mpTunnelDestOperStatus,
       "cmplsTeP2mpTunnelDestRowStatus": cmplsTeP2mpTunnelDestRowStatus,
       "cmplsTeP2mpTunnelDestStorageType": cmplsTeP2mpTunnelDestStorageType,
       "cmplsTeP2mpTunnelBranchPerfTable": cmplsTeP2mpTunnelBranchPerfTable,
       "cmplsTeP2mpTunnelBranchPerfEntry": cmplsTeP2mpTunnelBranchPerfEntry,
       "cmplsTeP2mpTunnelBranchPerfBranch": cmplsTeP2mpTunnelBranchPerfBranch,
       "cmplsTeP2mpTunnelBranchPerfPackets": cmplsTeP2mpTunnelBranchPerfPackets,
       "cmplsTeP2mpTunnelBranchPerfHCPackets": cmplsTeP2mpTunnelBranchPerfHCPackets,
       "cmplsTeP2mpTunnelBranchPerfErrors": cmplsTeP2mpTunnelBranchPerfErrors,
       "cmplsTeP2mpTunnelBranchPerfBytes": cmplsTeP2mpTunnelBranchPerfBytes,
       "cmplsTeP2mpTunnelBranchPerfHCBytes": cmplsTeP2mpTunnelBranchPerfHCBytes,
       "cmplsTeP2mpTunnelBranchDiscontinuityTime": cmplsTeP2mpTunnelBranchDiscontinuityTime,
       "cmplsTeP2mpTunnelBranchLocalLabel": cmplsTeP2mpTunnelBranchLocalLabel,
       "cmplsTeP2mpTunnelBranchOutIfIndex": cmplsTeP2mpTunnelBranchOutIfIndex,
       "cmplsTeP2mpTunnelBranchOutLabel": cmplsTeP2mpTunnelBranchOutLabel,
       "cmplsTeP2mpTunnelBranchSignalArea": cmplsTeP2mpTunnelBranchSignalArea,
       "cmplsTeP2mpTunnelBranchInIfIndex": cmplsTeP2mpTunnelBranchInIfIndex,
       "cmplsTeP2mpTunnelNotificationEnable": cmplsTeP2mpTunnelNotificationEnable,
       "cmplsTeP2mpConformance": cmplsTeP2mpConformance,
       "cmplsTeP2mpGroups": cmplsTeP2mpGroups,
       "cmplsTeP2mpGeneralGroup": cmplsTeP2mpGeneralGroup,
       "cmplsTeP2mpNotifGroup": cmplsTeP2mpNotifGroup,
       "cmplsTeP2mpScalarGroup": cmplsTeP2mpScalarGroup,
       "cmplsTeP2mpGeneralGroupSup1": cmplsTeP2mpGeneralGroupSup1,
       "cmplsTeP2mpGeneralGroupSup2": cmplsTeP2mpGeneralGroupSup2,
       "cmplsTeP2mpCompliances": cmplsTeP2mpCompliances,
       "cmplsTeP2mpModuleFullCompliance": cmplsTeP2mpModuleFullCompliance,
       "cmplsTeP2mpModuleReadOnlyCompliance": cmplsTeP2mpModuleReadOnlyCompliance,
       "cmplsTeP2mpModuleFullComplianceRev1": cmplsTeP2mpModuleFullComplianceRev1,
       "cmplsTeP2mpModuleReadOnlyComplianceRev1": cmplsTeP2mpModuleReadOnlyComplianceRev1,
       "cmplsTeP2mpModuleFullComplianceRev2": cmplsTeP2mpModuleFullComplianceRev2,
       "cmplsTeP2mpModuleReadOnlyComplianceRev2": cmplsTeP2mpModuleReadOnlyComplianceRev2}
)
