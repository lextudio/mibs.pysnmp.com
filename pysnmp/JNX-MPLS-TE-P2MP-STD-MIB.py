# SNMP MIB module (JNX-MPLS-TE-P2MP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-MPLS-TE-P2MP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:41 2024
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

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxP2mpExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxP2mpExperiment")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsPathIndexOrZero,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsPathIndexOrZero",
    "mplsStdMIB")

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

jnxMplsTeP2mpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1)
)
jnxMplsTeP2mpStdMIB.setRevisions(
        ("2009-04-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMplsTeP2mpNotifications_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpNotifications = _JnxMplsTeP2mpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 0)
)
_JnxMplsTeP2mpScalars_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpScalars = _JnxMplsTeP2mpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 1)
)
_JnxMplsTeP2mpTunnelConfigured_Type = Unsigned32
_JnxMplsTeP2mpTunnelConfigured_Object = MibScalar
jnxMplsTeP2mpTunnelConfigured = _JnxMplsTeP2mpTunnelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 1, 1),
    _JnxMplsTeP2mpTunnelConfigured_Type()
)
jnxMplsTeP2mpTunnelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelConfigured.setStatus("current")
_JnxMplsTeP2mpTunnelActive_Type = Unsigned32
_JnxMplsTeP2mpTunnelActive_Object = MibScalar
jnxMplsTeP2mpTunnelActive = _JnxMplsTeP2mpTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 1, 2),
    _JnxMplsTeP2mpTunnelActive_Type()
)
jnxMplsTeP2mpTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelActive.setStatus("current")
_JnxMplsTeP2mpTunnelTotalMaxHops_Type = Unsigned32
_JnxMplsTeP2mpTunnelTotalMaxHops_Object = MibScalar
jnxMplsTeP2mpTunnelTotalMaxHops = _JnxMplsTeP2mpTunnelTotalMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 1, 3),
    _JnxMplsTeP2mpTunnelTotalMaxHops_Type()
)
jnxMplsTeP2mpTunnelTotalMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelTotalMaxHops.setStatus("current")
_JnxMplsTeP2mpObjects_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpObjects = _JnxMplsTeP2mpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2)
)
_JnxMplsTeP2mpTunnelTable_Object = MibTable
jnxMplsTeP2mpTunnelTable = _JnxMplsTeP2mpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelTable.setStatus("current")
_JnxMplsTeP2mpTunnelEntry_Object = MibTableRow
jnxMplsTeP2mpTunnelEntry = _JnxMplsTeP2mpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1)
)
jnxMplsTeP2mpTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelEntry.setStatus("current")


class _JnxMplsTeP2mpTunnelP2mpIntegrity_Type(TruthValue):
    """Custom type jnxMplsTeP2mpTunnelP2mpIntegrity based on TruthValue"""


_JnxMplsTeP2mpTunnelP2mpIntegrity_Object = MibTableColumn
jnxMplsTeP2mpTunnelP2mpIntegrity = _JnxMplsTeP2mpTunnelP2mpIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1, 2),
    _JnxMplsTeP2mpTunnelP2mpIntegrity_Type()
)
jnxMplsTeP2mpTunnelP2mpIntegrity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelP2mpIntegrity.setStatus("current")


class _JnxMplsTeP2mpTunnelBranchRole_Type(Integer32):
    """Custom type jnxMplsTeP2mpTunnelBranchRole based on Integer32"""
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


_JnxMplsTeP2mpTunnelBranchRole_Type.__name__ = "Integer32"
_JnxMplsTeP2mpTunnelBranchRole_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchRole = _JnxMplsTeP2mpTunnelBranchRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1, 3),
    _JnxMplsTeP2mpTunnelBranchRole_Type()
)
jnxMplsTeP2mpTunnelBranchRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchRole.setStatus("current")
_JnxMplsTeP2mpTunnelP2mpXcIndex_Type = MplsIndexType
_JnxMplsTeP2mpTunnelP2mpXcIndex_Object = MibTableColumn
jnxMplsTeP2mpTunnelP2mpXcIndex = _JnxMplsTeP2mpTunnelP2mpXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1, 4),
    _JnxMplsTeP2mpTunnelP2mpXcIndex_Type()
)
jnxMplsTeP2mpTunnelP2mpXcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelP2mpXcIndex.setStatus("current")
_JnxMplsTeP2mpTunnelRowStatus_Type = RowStatus
_JnxMplsTeP2mpTunnelRowStatus_Object = MibTableColumn
jnxMplsTeP2mpTunnelRowStatus = _JnxMplsTeP2mpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1, 5),
    _JnxMplsTeP2mpTunnelRowStatus_Type()
)
jnxMplsTeP2mpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelRowStatus.setStatus("current")


class _JnxMplsTeP2mpTunnelStorageType_Type(StorageType):
    """Custom type jnxMplsTeP2mpTunnelStorageType based on StorageType"""


_JnxMplsTeP2mpTunnelStorageType_Object = MibTableColumn
jnxMplsTeP2mpTunnelStorageType = _JnxMplsTeP2mpTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 1, 1, 6),
    _JnxMplsTeP2mpTunnelStorageType_Type()
)
jnxMplsTeP2mpTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelStorageType.setStatus("current")


class _JnxMplsTeP2mpTunnelSubGroupIDNext_Type(IndexIntegerNextFree):
    """Custom type jnxMplsTeP2mpTunnelSubGroupIDNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxMplsTeP2mpTunnelSubGroupIDNext_Type.__name__ = "IndexIntegerNextFree"
_JnxMplsTeP2mpTunnelSubGroupIDNext_Object = MibScalar
jnxMplsTeP2mpTunnelSubGroupIDNext = _JnxMplsTeP2mpTunnelSubGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 2),
    _JnxMplsTeP2mpTunnelSubGroupIDNext_Type()
)
jnxMplsTeP2mpTunnelSubGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelSubGroupIDNext.setStatus("current")
_JnxMplsTeP2mpTunnelDestTable_Object = MibTable
jnxMplsTeP2mpTunnelDestTable = _JnxMplsTeP2mpTunnelDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestTable.setStatus("current")
_JnxMplsTeP2mpTunnelDestEntry_Object = MibTableRow
jnxMplsTeP2mpTunnelDestEntry = _JnxMplsTeP2mpTunnelDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1)
)
jnxMplsTeP2mpTunnelDestEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSrcSubGroupID"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSubGroupOriginType"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSubGroupOrigin"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestSubGroupID"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestDestinationType"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestDestination"),
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestEntry.setStatus("current")
_JnxMplsTeP2mpTunnelDestSrcSubGroupOriginType_Type = InetAddressType
_JnxMplsTeP2mpTunnelDestSrcSubGroupOriginType_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType = _JnxMplsTeP2mpTunnelDestSrcSubGroupOriginType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 1),
    _JnxMplsTeP2mpTunnelDestSrcSubGroupOriginType_Type()
)
jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType.setStatus("current")


class _JnxMplsTeP2mpTunnelDestSrcSubGroupOrigin_Type(InetAddress):
    """Custom type jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_JnxMplsTeP2mpTunnelDestSrcSubGroupOrigin_Type.__name__ = "InetAddress"
_JnxMplsTeP2mpTunnelDestSrcSubGroupOrigin_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin = _JnxMplsTeP2mpTunnelDestSrcSubGroupOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 2),
    _JnxMplsTeP2mpTunnelDestSrcSubGroupOrigin_Type()
)
jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin.setStatus("current")


class _JnxMplsTeP2mpTunnelDestSrcSubGroupID_Type(IndexInteger):
    """Custom type jnxMplsTeP2mpTunnelDestSrcSubGroupID based on IndexInteger"""
    subtypeSpec = IndexInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxMplsTeP2mpTunnelDestSrcSubGroupID_Type.__name__ = "IndexInteger"
_JnxMplsTeP2mpTunnelDestSrcSubGroupID_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSrcSubGroupID = _JnxMplsTeP2mpTunnelDestSrcSubGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 3),
    _JnxMplsTeP2mpTunnelDestSrcSubGroupID_Type()
)
jnxMplsTeP2mpTunnelDestSrcSubGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSrcSubGroupID.setStatus("current")
_JnxMplsTeP2mpTunnelDestSubGroupOriginType_Type = InetAddressType
_JnxMplsTeP2mpTunnelDestSubGroupOriginType_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSubGroupOriginType = _JnxMplsTeP2mpTunnelDestSubGroupOriginType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 4),
    _JnxMplsTeP2mpTunnelDestSubGroupOriginType_Type()
)
jnxMplsTeP2mpTunnelDestSubGroupOriginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSubGroupOriginType.setStatus("current")


class _JnxMplsTeP2mpTunnelDestSubGroupOrigin_Type(InetAddress):
    """Custom type jnxMplsTeP2mpTunnelDestSubGroupOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_JnxMplsTeP2mpTunnelDestSubGroupOrigin_Type.__name__ = "InetAddress"
_JnxMplsTeP2mpTunnelDestSubGroupOrigin_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSubGroupOrigin = _JnxMplsTeP2mpTunnelDestSubGroupOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 5),
    _JnxMplsTeP2mpTunnelDestSubGroupOrigin_Type()
)
jnxMplsTeP2mpTunnelDestSubGroupOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSubGroupOrigin.setStatus("current")


class _JnxMplsTeP2mpTunnelDestSubGroupID_Type(IndexInteger):
    """Custom type jnxMplsTeP2mpTunnelDestSubGroupID based on IndexInteger"""
    subtypeSpec = IndexInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMplsTeP2mpTunnelDestSubGroupID_Type.__name__ = "IndexInteger"
_JnxMplsTeP2mpTunnelDestSubGroupID_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestSubGroupID = _JnxMplsTeP2mpTunnelDestSubGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 6),
    _JnxMplsTeP2mpTunnelDestSubGroupID_Type()
)
jnxMplsTeP2mpTunnelDestSubGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestSubGroupID.setStatus("current")
_JnxMplsTeP2mpTunnelDestDestinationType_Type = InetAddressType
_JnxMplsTeP2mpTunnelDestDestinationType_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestDestinationType = _JnxMplsTeP2mpTunnelDestDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 7),
    _JnxMplsTeP2mpTunnelDestDestinationType_Type()
)
jnxMplsTeP2mpTunnelDestDestinationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestDestinationType.setStatus("current")


class _JnxMplsTeP2mpTunnelDestDestination_Type(InetAddress):
    """Custom type jnxMplsTeP2mpTunnelDestDestination based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_JnxMplsTeP2mpTunnelDestDestination_Type.__name__ = "InetAddress"
_JnxMplsTeP2mpTunnelDestDestination_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestDestination = _JnxMplsTeP2mpTunnelDestDestination_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 8),
    _JnxMplsTeP2mpTunnelDestDestination_Type()
)
jnxMplsTeP2mpTunnelDestDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestDestination.setStatus("current")
_JnxMplsTeP2mpTunnelDestBranchOutSegment_Type = MplsIndexType
_JnxMplsTeP2mpTunnelDestBranchOutSegment_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestBranchOutSegment = _JnxMplsTeP2mpTunnelDestBranchOutSegment_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 9),
    _JnxMplsTeP2mpTunnelDestBranchOutSegment_Type()
)
jnxMplsTeP2mpTunnelDestBranchOutSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestBranchOutSegment.setStatus("current")


class _JnxMplsTeP2mpTunnelDestHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type jnxMplsTeP2mpTunnelDestHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_JnxMplsTeP2mpTunnelDestHopTableIndex_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestHopTableIndex = _JnxMplsTeP2mpTunnelDestHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 10),
    _JnxMplsTeP2mpTunnelDestHopTableIndex_Type()
)
jnxMplsTeP2mpTunnelDestHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestHopTableIndex.setStatus("current")


class _JnxMplsTeP2mpTunnelDestPathInUse_Type(MplsPathIndexOrZero):
    """Custom type jnxMplsTeP2mpTunnelDestPathInUse based on MplsPathIndexOrZero"""
    defaultValue = 0


_JnxMplsTeP2mpTunnelDestPathInUse_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestPathInUse = _JnxMplsTeP2mpTunnelDestPathInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 11),
    _JnxMplsTeP2mpTunnelDestPathInUse_Type()
)
jnxMplsTeP2mpTunnelDestPathInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestPathInUse.setStatus("current")
_JnxMplsTeP2mpTunnelDestCHopTableIndex_Type = MplsPathIndexOrZero
_JnxMplsTeP2mpTunnelDestCHopTableIndex_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestCHopTableIndex = _JnxMplsTeP2mpTunnelDestCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 12),
    _JnxMplsTeP2mpTunnelDestCHopTableIndex_Type()
)
jnxMplsTeP2mpTunnelDestCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestCHopTableIndex.setStatus("current")
_JnxMplsTeP2mpTunnelDestARHopTableIndex_Type = MplsPathIndexOrZero
_JnxMplsTeP2mpTunnelDestARHopTableIndex_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestARHopTableIndex = _JnxMplsTeP2mpTunnelDestARHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 13),
    _JnxMplsTeP2mpTunnelDestARHopTableIndex_Type()
)
jnxMplsTeP2mpTunnelDestARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestARHopTableIndex.setStatus("current")
_JnxMplsTeP2mpTunnelDestTotalUpTime_Type = TimeTicks
_JnxMplsTeP2mpTunnelDestTotalUpTime_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestTotalUpTime = _JnxMplsTeP2mpTunnelDestTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 14),
    _JnxMplsTeP2mpTunnelDestTotalUpTime_Type()
)
jnxMplsTeP2mpTunnelDestTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestTotalUpTime.setStatus("current")
_JnxMplsTeP2mpTunnelDestInstanceUpTime_Type = TimeTicks
_JnxMplsTeP2mpTunnelDestInstanceUpTime_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestInstanceUpTime = _JnxMplsTeP2mpTunnelDestInstanceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 15),
    _JnxMplsTeP2mpTunnelDestInstanceUpTime_Type()
)
jnxMplsTeP2mpTunnelDestInstanceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestInstanceUpTime.setStatus("current")
_JnxMplsTeP2mpTunnelDestPathChanges_Type = Counter32
_JnxMplsTeP2mpTunnelDestPathChanges_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestPathChanges = _JnxMplsTeP2mpTunnelDestPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 16),
    _JnxMplsTeP2mpTunnelDestPathChanges_Type()
)
jnxMplsTeP2mpTunnelDestPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestPathChanges.setStatus("current")
_JnxMplsTeP2mpTunnelDestLastPathChange_Type = TimeTicks
_JnxMplsTeP2mpTunnelDestLastPathChange_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestLastPathChange = _JnxMplsTeP2mpTunnelDestLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 17),
    _JnxMplsTeP2mpTunnelDestLastPathChange_Type()
)
jnxMplsTeP2mpTunnelDestLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestLastPathChange.setStatus("current")
_JnxMplsTeP2mpTunnelDestCreationTime_Type = TimeStamp
_JnxMplsTeP2mpTunnelDestCreationTime_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestCreationTime = _JnxMplsTeP2mpTunnelDestCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 18),
    _JnxMplsTeP2mpTunnelDestCreationTime_Type()
)
jnxMplsTeP2mpTunnelDestCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestCreationTime.setStatus("current")
_JnxMplsTeP2mpTunnelDestStateTransitions_Type = Counter32
_JnxMplsTeP2mpTunnelDestStateTransitions_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestStateTransitions = _JnxMplsTeP2mpTunnelDestStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 19),
    _JnxMplsTeP2mpTunnelDestStateTransitions_Type()
)
jnxMplsTeP2mpTunnelDestStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestStateTransitions.setStatus("current")
_JnxMplsTeP2mpTunnelDestDiscontinuityTime_Type = TimeStamp
_JnxMplsTeP2mpTunnelDestDiscontinuityTime_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestDiscontinuityTime = _JnxMplsTeP2mpTunnelDestDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 20),
    _JnxMplsTeP2mpTunnelDestDiscontinuityTime_Type()
)
jnxMplsTeP2mpTunnelDestDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestDiscontinuityTime.setStatus("current")


class _JnxMplsTeP2mpTunnelDestAdminStatus_Type(Integer32):
    """Custom type jnxMplsTeP2mpTunnelDestAdminStatus based on Integer32"""
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


_JnxMplsTeP2mpTunnelDestAdminStatus_Type.__name__ = "Integer32"
_JnxMplsTeP2mpTunnelDestAdminStatus_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestAdminStatus = _JnxMplsTeP2mpTunnelDestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 21),
    _JnxMplsTeP2mpTunnelDestAdminStatus_Type()
)
jnxMplsTeP2mpTunnelDestAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestAdminStatus.setStatus("current")


class _JnxMplsTeP2mpTunnelDestOperStatus_Type(Integer32):
    """Custom type jnxMplsTeP2mpTunnelDestOperStatus based on Integer32"""
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


_JnxMplsTeP2mpTunnelDestOperStatus_Type.__name__ = "Integer32"
_JnxMplsTeP2mpTunnelDestOperStatus_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestOperStatus = _JnxMplsTeP2mpTunnelDestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 22),
    _JnxMplsTeP2mpTunnelDestOperStatus_Type()
)
jnxMplsTeP2mpTunnelDestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestOperStatus.setStatus("current")
_JnxMplsTeP2mpTunnelDestRowStatus_Type = RowStatus
_JnxMplsTeP2mpTunnelDestRowStatus_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestRowStatus = _JnxMplsTeP2mpTunnelDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 23),
    _JnxMplsTeP2mpTunnelDestRowStatus_Type()
)
jnxMplsTeP2mpTunnelDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestRowStatus.setStatus("current")


class _JnxMplsTeP2mpTunnelDestStorageType_Type(StorageType):
    """Custom type jnxMplsTeP2mpTunnelDestStorageType based on StorageType"""


_JnxMplsTeP2mpTunnelDestStorageType_Object = MibTableColumn
jnxMplsTeP2mpTunnelDestStorageType = _JnxMplsTeP2mpTunnelDestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 3, 1, 24),
    _JnxMplsTeP2mpTunnelDestStorageType_Type()
)
jnxMplsTeP2mpTunnelDestStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestStorageType.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfTable_Object = MibTable
jnxMplsTeP2mpTunnelBranchPerfTable = _JnxMplsTeP2mpTunnelBranchPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfTable.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfEntry_Object = MibTableRow
jnxMplsTeP2mpTunnelBranchPerfEntry = _JnxMplsTeP2mpTunnelBranchPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1)
)
jnxMplsTeP2mpTunnelBranchPerfEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
    (0, "JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfBranch"),
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfEntry.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfBranch_Type = MplsIndexType
_JnxMplsTeP2mpTunnelBranchPerfBranch_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfBranch = _JnxMplsTeP2mpTunnelBranchPerfBranch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 1),
    _JnxMplsTeP2mpTunnelBranchPerfBranch_Type()
)
jnxMplsTeP2mpTunnelBranchPerfBranch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfBranch.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfPackets_Type = Counter32
_JnxMplsTeP2mpTunnelBranchPerfPackets_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfPackets = _JnxMplsTeP2mpTunnelBranchPerfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 2),
    _JnxMplsTeP2mpTunnelBranchPerfPackets_Type()
)
jnxMplsTeP2mpTunnelBranchPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfPackets.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfHCPackets_Type = Counter64
_JnxMplsTeP2mpTunnelBranchPerfHCPackets_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfHCPackets = _JnxMplsTeP2mpTunnelBranchPerfHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 3),
    _JnxMplsTeP2mpTunnelBranchPerfHCPackets_Type()
)
jnxMplsTeP2mpTunnelBranchPerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfHCPackets.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfErrors_Type = Counter32
_JnxMplsTeP2mpTunnelBranchPerfErrors_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfErrors = _JnxMplsTeP2mpTunnelBranchPerfErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 4),
    _JnxMplsTeP2mpTunnelBranchPerfErrors_Type()
)
jnxMplsTeP2mpTunnelBranchPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfErrors.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfBytes_Type = Counter32
_JnxMplsTeP2mpTunnelBranchPerfBytes_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfBytes = _JnxMplsTeP2mpTunnelBranchPerfBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 5),
    _JnxMplsTeP2mpTunnelBranchPerfBytes_Type()
)
jnxMplsTeP2mpTunnelBranchPerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfBytes.setStatus("current")
_JnxMplsTeP2mpTunnelBranchPerfHCBytes_Type = Counter64
_JnxMplsTeP2mpTunnelBranchPerfHCBytes_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchPerfHCBytes = _JnxMplsTeP2mpTunnelBranchPerfHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 6),
    _JnxMplsTeP2mpTunnelBranchPerfHCBytes_Type()
)
jnxMplsTeP2mpTunnelBranchPerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchPerfHCBytes.setStatus("current")
_JnxMplsTeP2mpTunnelBranchDiscontinuityTime_Type = TimeStamp
_JnxMplsTeP2mpTunnelBranchDiscontinuityTime_Object = MibTableColumn
jnxMplsTeP2mpTunnelBranchDiscontinuityTime = _JnxMplsTeP2mpTunnelBranchDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 4, 1, 7),
    _JnxMplsTeP2mpTunnelBranchDiscontinuityTime_Type()
)
jnxMplsTeP2mpTunnelBranchDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelBranchDiscontinuityTime.setStatus("current")


class _JnxMplsTeP2mpTunnelNotificationEnable_Type(TruthValue):
    """Custom type jnxMplsTeP2mpTunnelNotificationEnable based on TruthValue"""


_JnxMplsTeP2mpTunnelNotificationEnable_Object = MibScalar
jnxMplsTeP2mpTunnelNotificationEnable = _JnxMplsTeP2mpTunnelNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 2, 5),
    _JnxMplsTeP2mpTunnelNotificationEnable_Type()
)
jnxMplsTeP2mpTunnelNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelNotificationEnable.setStatus("current")
_JnxMplsTeP2mpConformance_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpConformance = _JnxMplsTeP2mpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3)
)
_JnxMplsTeP2mpGroups_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpGroups = _JnxMplsTeP2mpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 1)
)
_JnxMplsTeP2mpCompliances_ObjectIdentity = ObjectIdentity
jnxMplsTeP2mpCompliances = _JnxMplsTeP2mpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 2)
)

# Managed Objects groups

jnxMplsTeP2mpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 1, 1)
)
jnxMplsTeP2mpGeneralGroup.setObjects(
      *(("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelConfigured"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelActive"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelTotalMaxHops"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelP2mpIntegrity"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchRole"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelP2mpXcIndex"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelRowStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelStorageType"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelSubGroupIDNext"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestBranchOutSegment"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestHopTableIndex"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestPathInUse"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestCHopTableIndex"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestARHopTableIndex"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestTotalUpTime"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestInstanceUpTime"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestPathChanges"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestLastPathChange"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestCreationTime"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestStateTransitions"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestDiscontinuityTime"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestAdminStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestOperStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestRowStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestStorageType"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfPackets"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfHCPackets"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfErrors"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfBytes"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchPerfHCBytes"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelBranchDiscontinuityTime"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelNotificationEnable"))
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpGeneralGroup.setStatus("current")

jnxMplsTeP2mpScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 1, 3)
)
jnxMplsTeP2mpScalarGroup.setObjects(
      *(("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelConfigured"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelActive"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelTotalMaxHops"))
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpScalarGroup.setStatus("current")


# Notification objects

jnxMplsTeP2mpTunnelDestUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 0, 1)
)
jnxMplsTeP2mpTunnelDestUp.setObjects(
      *(("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestAdminStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestOperStatus"))
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestUp.setStatus(
        "current"
    )

jnxMplsTeP2mpTunnelDestDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 0, 2)
)
jnxMplsTeP2mpTunnelDestDown.setObjects(
      *(("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestAdminStatus"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestOperStatus"))
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpTunnelDestDown.setStatus(
        "current"
    )


# Notifications groups

jnxMplsTeP2mpNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 1, 2)
)
jnxMplsTeP2mpNotifGroup.setObjects(
      *(("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestUp"),
        ("JNX-MPLS-TE-P2MP-STD-MIB", "jnxMplsTeP2mpTunnelDestDown"))
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jnxMplsTeP2mpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpModuleFullCompliance.setStatus(
        "current"
    )

jnxMplsTeP2mpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 5, 7, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    jnxMplsTeP2mpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-MPLS-TE-P2MP-STD-MIB",
    **{"jnxMplsTeP2mpStdMIB": jnxMplsTeP2mpStdMIB,
       "jnxMplsTeP2mpNotifications": jnxMplsTeP2mpNotifications,
       "jnxMplsTeP2mpTunnelDestUp": jnxMplsTeP2mpTunnelDestUp,
       "jnxMplsTeP2mpTunnelDestDown": jnxMplsTeP2mpTunnelDestDown,
       "jnxMplsTeP2mpScalars": jnxMplsTeP2mpScalars,
       "jnxMplsTeP2mpTunnelConfigured": jnxMplsTeP2mpTunnelConfigured,
       "jnxMplsTeP2mpTunnelActive": jnxMplsTeP2mpTunnelActive,
       "jnxMplsTeP2mpTunnelTotalMaxHops": jnxMplsTeP2mpTunnelTotalMaxHops,
       "jnxMplsTeP2mpObjects": jnxMplsTeP2mpObjects,
       "jnxMplsTeP2mpTunnelTable": jnxMplsTeP2mpTunnelTable,
       "jnxMplsTeP2mpTunnelEntry": jnxMplsTeP2mpTunnelEntry,
       "jnxMplsTeP2mpTunnelP2mpIntegrity": jnxMplsTeP2mpTunnelP2mpIntegrity,
       "jnxMplsTeP2mpTunnelBranchRole": jnxMplsTeP2mpTunnelBranchRole,
       "jnxMplsTeP2mpTunnelP2mpXcIndex": jnxMplsTeP2mpTunnelP2mpXcIndex,
       "jnxMplsTeP2mpTunnelRowStatus": jnxMplsTeP2mpTunnelRowStatus,
       "jnxMplsTeP2mpTunnelStorageType": jnxMplsTeP2mpTunnelStorageType,
       "jnxMplsTeP2mpTunnelSubGroupIDNext": jnxMplsTeP2mpTunnelSubGroupIDNext,
       "jnxMplsTeP2mpTunnelDestTable": jnxMplsTeP2mpTunnelDestTable,
       "jnxMplsTeP2mpTunnelDestEntry": jnxMplsTeP2mpTunnelDestEntry,
       "jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType": jnxMplsTeP2mpTunnelDestSrcSubGroupOriginType,
       "jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin": jnxMplsTeP2mpTunnelDestSrcSubGroupOrigin,
       "jnxMplsTeP2mpTunnelDestSrcSubGroupID": jnxMplsTeP2mpTunnelDestSrcSubGroupID,
       "jnxMplsTeP2mpTunnelDestSubGroupOriginType": jnxMplsTeP2mpTunnelDestSubGroupOriginType,
       "jnxMplsTeP2mpTunnelDestSubGroupOrigin": jnxMplsTeP2mpTunnelDestSubGroupOrigin,
       "jnxMplsTeP2mpTunnelDestSubGroupID": jnxMplsTeP2mpTunnelDestSubGroupID,
       "jnxMplsTeP2mpTunnelDestDestinationType": jnxMplsTeP2mpTunnelDestDestinationType,
       "jnxMplsTeP2mpTunnelDestDestination": jnxMplsTeP2mpTunnelDestDestination,
       "jnxMplsTeP2mpTunnelDestBranchOutSegment": jnxMplsTeP2mpTunnelDestBranchOutSegment,
       "jnxMplsTeP2mpTunnelDestHopTableIndex": jnxMplsTeP2mpTunnelDestHopTableIndex,
       "jnxMplsTeP2mpTunnelDestPathInUse": jnxMplsTeP2mpTunnelDestPathInUse,
       "jnxMplsTeP2mpTunnelDestCHopTableIndex": jnxMplsTeP2mpTunnelDestCHopTableIndex,
       "jnxMplsTeP2mpTunnelDestARHopTableIndex": jnxMplsTeP2mpTunnelDestARHopTableIndex,
       "jnxMplsTeP2mpTunnelDestTotalUpTime": jnxMplsTeP2mpTunnelDestTotalUpTime,
       "jnxMplsTeP2mpTunnelDestInstanceUpTime": jnxMplsTeP2mpTunnelDestInstanceUpTime,
       "jnxMplsTeP2mpTunnelDestPathChanges": jnxMplsTeP2mpTunnelDestPathChanges,
       "jnxMplsTeP2mpTunnelDestLastPathChange": jnxMplsTeP2mpTunnelDestLastPathChange,
       "jnxMplsTeP2mpTunnelDestCreationTime": jnxMplsTeP2mpTunnelDestCreationTime,
       "jnxMplsTeP2mpTunnelDestStateTransitions": jnxMplsTeP2mpTunnelDestStateTransitions,
       "jnxMplsTeP2mpTunnelDestDiscontinuityTime": jnxMplsTeP2mpTunnelDestDiscontinuityTime,
       "jnxMplsTeP2mpTunnelDestAdminStatus": jnxMplsTeP2mpTunnelDestAdminStatus,
       "jnxMplsTeP2mpTunnelDestOperStatus": jnxMplsTeP2mpTunnelDestOperStatus,
       "jnxMplsTeP2mpTunnelDestRowStatus": jnxMplsTeP2mpTunnelDestRowStatus,
       "jnxMplsTeP2mpTunnelDestStorageType": jnxMplsTeP2mpTunnelDestStorageType,
       "jnxMplsTeP2mpTunnelBranchPerfTable": jnxMplsTeP2mpTunnelBranchPerfTable,
       "jnxMplsTeP2mpTunnelBranchPerfEntry": jnxMplsTeP2mpTunnelBranchPerfEntry,
       "jnxMplsTeP2mpTunnelBranchPerfBranch": jnxMplsTeP2mpTunnelBranchPerfBranch,
       "jnxMplsTeP2mpTunnelBranchPerfPackets": jnxMplsTeP2mpTunnelBranchPerfPackets,
       "jnxMplsTeP2mpTunnelBranchPerfHCPackets": jnxMplsTeP2mpTunnelBranchPerfHCPackets,
       "jnxMplsTeP2mpTunnelBranchPerfErrors": jnxMplsTeP2mpTunnelBranchPerfErrors,
       "jnxMplsTeP2mpTunnelBranchPerfBytes": jnxMplsTeP2mpTunnelBranchPerfBytes,
       "jnxMplsTeP2mpTunnelBranchPerfHCBytes": jnxMplsTeP2mpTunnelBranchPerfHCBytes,
       "jnxMplsTeP2mpTunnelBranchDiscontinuityTime": jnxMplsTeP2mpTunnelBranchDiscontinuityTime,
       "jnxMplsTeP2mpTunnelNotificationEnable": jnxMplsTeP2mpTunnelNotificationEnable,
       "jnxMplsTeP2mpConformance": jnxMplsTeP2mpConformance,
       "jnxMplsTeP2mpGroups": jnxMplsTeP2mpGroups,
       "jnxMplsTeP2mpGeneralGroup": jnxMplsTeP2mpGeneralGroup,
       "jnxMplsTeP2mpNotifGroup": jnxMplsTeP2mpNotifGroup,
       "jnxMplsTeP2mpScalarGroup": jnxMplsTeP2mpScalarGroup,
       "jnxMplsTeP2mpCompliances": jnxMplsTeP2mpCompliances,
       "jnxMplsTeP2mpModuleFullCompliance": jnxMplsTeP2mpModuleFullCompliance,
       "jnxMplsTeP2mpModuleReadOnlyCompliance": jnxMplsTeP2mpModuleReadOnlyCompliance}
)
