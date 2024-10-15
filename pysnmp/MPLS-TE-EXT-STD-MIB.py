# SNMP MIB module (MPLS-TE-EXT-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-TE-EXT-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:25 2024
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

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexIntegerNextFree")

(MplsCcId,
 MplsGlobalId,
 MplsIccId,
 MplsNodeId) = mibBuilder.importSymbols(
    "MPLS-TC-EXT-STD-MIB",
    "MplsCcId",
    "MplsGlobalId",
    "MplsIccId",
    "MplsNodeId")

(MplsExtendedTunnelId,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex",
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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mplsTeExtStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 20)
)
mplsTeExtStdMIB.setRevisions(
        ("2015-02-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsTeExtObjects_ObjectIdentity = ObjectIdentity
mplsTeExtObjects = _MplsTeExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0)
)


class _MplsTunnelExtNodeConfigLocalIdNext_Type(IndexIntegerNextFree):
    """Custom type mplsTunnelExtNodeConfigLocalIdNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MplsTunnelExtNodeConfigLocalIdNext_Type.__name__ = "IndexIntegerNextFree"
_MplsTunnelExtNodeConfigLocalIdNext_Object = MibScalar
mplsTunnelExtNodeConfigLocalIdNext = _MplsTunnelExtNodeConfigLocalIdNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 1),
    _MplsTunnelExtNodeConfigLocalIdNext_Type()
)
mplsTunnelExtNodeConfigLocalIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigLocalIdNext.setStatus("current")
_MplsTunnelExtNodeConfigTable_Object = MibTable
mplsTunnelExtNodeConfigTable = _MplsTunnelExtNodeConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2)
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigTable.setStatus("current")
_MplsTunnelExtNodeConfigEntry_Object = MibTableRow
mplsTunnelExtNodeConfigEntry = _MplsTunnelExtNodeConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1)
)
mplsTunnelExtNodeConfigEntry.setIndexNames(
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalId"),
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigEntry.setStatus("current")
_MplsTunnelExtNodeConfigLocalId_Type = MplsExtendedTunnelId
_MplsTunnelExtNodeConfigLocalId_Object = MibTableColumn
mplsTunnelExtNodeConfigLocalId = _MplsTunnelExtNodeConfigLocalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 1),
    _MplsTunnelExtNodeConfigLocalId_Type()
)
mplsTunnelExtNodeConfigLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigLocalId.setStatus("current")
_MplsTunnelExtNodeConfigGlobalId_Type = MplsGlobalId
_MplsTunnelExtNodeConfigGlobalId_Object = MibTableColumn
mplsTunnelExtNodeConfigGlobalId = _MplsTunnelExtNodeConfigGlobalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 2),
    _MplsTunnelExtNodeConfigGlobalId_Type()
)
mplsTunnelExtNodeConfigGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigGlobalId.setStatus("current")
_MplsTunnelExtNodeConfigCcId_Type = MplsCcId
_MplsTunnelExtNodeConfigCcId_Object = MibTableColumn
mplsTunnelExtNodeConfigCcId = _MplsTunnelExtNodeConfigCcId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 3),
    _MplsTunnelExtNodeConfigCcId_Type()
)
mplsTunnelExtNodeConfigCcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigCcId.setStatus("current")
_MplsTunnelExtNodeConfigIccId_Type = MplsIccId
_MplsTunnelExtNodeConfigIccId_Object = MibTableColumn
mplsTunnelExtNodeConfigIccId = _MplsTunnelExtNodeConfigIccId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 4),
    _MplsTunnelExtNodeConfigIccId_Type()
)
mplsTunnelExtNodeConfigIccId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigIccId.setStatus("current")
_MplsTunnelExtNodeConfigNodeId_Type = MplsNodeId
_MplsTunnelExtNodeConfigNodeId_Object = MibTableColumn
mplsTunnelExtNodeConfigNodeId = _MplsTunnelExtNodeConfigNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 5),
    _MplsTunnelExtNodeConfigNodeId_Type()
)
mplsTunnelExtNodeConfigNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigNodeId.setStatus("current")


class _MplsTunnelExtNodeConfigIccValid_Type(TruthValue):
    """Custom type mplsTunnelExtNodeConfigIccValid based on TruthValue"""


_MplsTunnelExtNodeConfigIccValid_Object = MibTableColumn
mplsTunnelExtNodeConfigIccValid = _MplsTunnelExtNodeConfigIccValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 6),
    _MplsTunnelExtNodeConfigIccValid_Type()
)
mplsTunnelExtNodeConfigIccValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigIccValid.setStatus("current")


class _MplsTunnelExtNodeConfigStorageType_Type(StorageType):
    """Custom type mplsTunnelExtNodeConfigStorageType based on StorageType"""


_MplsTunnelExtNodeConfigStorageType_Object = MibTableColumn
mplsTunnelExtNodeConfigStorageType = _MplsTunnelExtNodeConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 7),
    _MplsTunnelExtNodeConfigStorageType_Type()
)
mplsTunnelExtNodeConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigStorageType.setStatus("current")
_MplsTunnelExtNodeConfigRowStatus_Type = RowStatus
_MplsTunnelExtNodeConfigRowStatus_Object = MibTableColumn
mplsTunnelExtNodeConfigRowStatus = _MplsTunnelExtNodeConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 2, 1, 8),
    _MplsTunnelExtNodeConfigRowStatus_Type()
)
mplsTunnelExtNodeConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeConfigRowStatus.setStatus("current")
_MplsTunnelExtNodeIpMapTable_Object = MibTable
mplsTunnelExtNodeIpMapTable = _MplsTunnelExtNodeIpMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3)
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIpMapTable.setStatus("current")
_MplsTunnelExtNodeIpMapEntry_Object = MibTableRow
mplsTunnelExtNodeIpMapEntry = _MplsTunnelExtNodeIpMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1)
)
mplsTunnelExtNodeIpMapEntry.setIndexNames(
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapGlobalId"),
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapNodeId"),
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIpMapEntry.setStatus("current")
_MplsTunnelExtNodeIpMapGlobalId_Type = MplsGlobalId
_MplsTunnelExtNodeIpMapGlobalId_Object = MibTableColumn
mplsTunnelExtNodeIpMapGlobalId = _MplsTunnelExtNodeIpMapGlobalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 1),
    _MplsTunnelExtNodeIpMapGlobalId_Type()
)
mplsTunnelExtNodeIpMapGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIpMapGlobalId.setStatus("current")
_MplsTunnelExtNodeIpMapNodeId_Type = MplsNodeId
_MplsTunnelExtNodeIpMapNodeId_Object = MibTableColumn
mplsTunnelExtNodeIpMapNodeId = _MplsTunnelExtNodeIpMapNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 2),
    _MplsTunnelExtNodeIpMapNodeId_Type()
)
mplsTunnelExtNodeIpMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIpMapNodeId.setStatus("current")
_MplsTunnelExtNodeIpMapLocalId_Type = MplsExtendedTunnelId
_MplsTunnelExtNodeIpMapLocalId_Object = MibTableColumn
mplsTunnelExtNodeIpMapLocalId = _MplsTunnelExtNodeIpMapLocalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 3, 1, 3),
    _MplsTunnelExtNodeIpMapLocalId_Type()
)
mplsTunnelExtNodeIpMapLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIpMapLocalId.setStatus("current")
_MplsTunnelExtNodeIccMapTable_Object = MibTable
mplsTunnelExtNodeIccMapTable = _MplsTunnelExtNodeIccMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4)
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapTable.setStatus("current")
_MplsTunnelExtNodeIccMapEntry_Object = MibTableRow
mplsTunnelExtNodeIccMapEntry = _MplsTunnelExtNodeIccMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1)
)
mplsTunnelExtNodeIccMapEntry.setIndexNames(
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapCcId"),
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapIccId"),
    (0, "MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapNodeId"),
)
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapEntry.setStatus("current")
_MplsTunnelExtNodeIccMapCcId_Type = MplsCcId
_MplsTunnelExtNodeIccMapCcId_Object = MibTableColumn
mplsTunnelExtNodeIccMapCcId = _MplsTunnelExtNodeIccMapCcId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 1),
    _MplsTunnelExtNodeIccMapCcId_Type()
)
mplsTunnelExtNodeIccMapCcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapCcId.setStatus("current")
_MplsTunnelExtNodeIccMapIccId_Type = MplsIccId
_MplsTunnelExtNodeIccMapIccId_Object = MibTableColumn
mplsTunnelExtNodeIccMapIccId = _MplsTunnelExtNodeIccMapIccId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 2),
    _MplsTunnelExtNodeIccMapIccId_Type()
)
mplsTunnelExtNodeIccMapIccId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapIccId.setStatus("current")
_MplsTunnelExtNodeIccMapNodeId_Type = MplsNodeId
_MplsTunnelExtNodeIccMapNodeId_Object = MibTableColumn
mplsTunnelExtNodeIccMapNodeId = _MplsTunnelExtNodeIccMapNodeId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 3),
    _MplsTunnelExtNodeIccMapNodeId_Type()
)
mplsTunnelExtNodeIccMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapNodeId.setStatus("current")
_MplsTunnelExtNodeIccMapLocalId_Type = MplsExtendedTunnelId
_MplsTunnelExtNodeIccMapLocalId_Object = MibTableColumn
mplsTunnelExtNodeIccMapLocalId = _MplsTunnelExtNodeIccMapLocalId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 4, 1, 4),
    _MplsTunnelExtNodeIccMapLocalId_Type()
)
mplsTunnelExtNodeIccMapLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelExtNodeIccMapLocalId.setStatus("current")
_MplsTunnelExtTable_Object = MibTable
mplsTunnelExtTable = _MplsTunnelExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5)
)
if mibBuilder.loadTexts:
    mplsTunnelExtTable.setStatus("current")
_MplsTunnelExtEntry_Object = MibTableRow
mplsTunnelExtEntry = _MplsTunnelExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1)
)
mplsTunnelExtEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsTunnelExtEntry.setStatus("current")
_MplsTunnelExtOppositeDirPtr_Type = RowPointer
_MplsTunnelExtOppositeDirPtr_Object = MibTableColumn
mplsTunnelExtOppositeDirPtr = _MplsTunnelExtOppositeDirPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 1),
    _MplsTunnelExtOppositeDirPtr_Type()
)
mplsTunnelExtOppositeDirPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtOppositeDirPtr.setStatus("current")


class _MplsTunnelExtOppositeDirTnlValid_Type(TruthValue):
    """Custom type mplsTunnelExtOppositeDirTnlValid based on TruthValue"""


_MplsTunnelExtOppositeDirTnlValid_Object = MibTableColumn
mplsTunnelExtOppositeDirTnlValid = _MplsTunnelExtOppositeDirTnlValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 2),
    _MplsTunnelExtOppositeDirTnlValid_Type()
)
mplsTunnelExtOppositeDirTnlValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtOppositeDirTnlValid.setStatus("current")
_MplsTunnelExtDestTnlIndex_Type = MplsTunnelIndex
_MplsTunnelExtDestTnlIndex_Object = MibTableColumn
mplsTunnelExtDestTnlIndex = _MplsTunnelExtDestTnlIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 3),
    _MplsTunnelExtDestTnlIndex_Type()
)
mplsTunnelExtDestTnlIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtDestTnlIndex.setStatus("current")
_MplsTunnelExtDestTnlLspIndex_Type = MplsTunnelInstanceIndex
_MplsTunnelExtDestTnlLspIndex_Object = MibTableColumn
mplsTunnelExtDestTnlLspIndex = _MplsTunnelExtDestTnlLspIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 4),
    _MplsTunnelExtDestTnlLspIndex_Type()
)
mplsTunnelExtDestTnlLspIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtDestTnlLspIndex.setStatus("current")


class _MplsTunnelExtDestTnlValid_Type(TruthValue):
    """Custom type mplsTunnelExtDestTnlValid based on TruthValue"""


_MplsTunnelExtDestTnlValid_Object = MibTableColumn
mplsTunnelExtDestTnlValid = _MplsTunnelExtDestTnlValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 5),
    _MplsTunnelExtDestTnlValid_Type()
)
mplsTunnelExtDestTnlValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtDestTnlValid.setStatus("current")


class _MplsTunnelExtIngressLSRLocalIdValid_Type(TruthValue):
    """Custom type mplsTunnelExtIngressLSRLocalIdValid based on TruthValue"""


_MplsTunnelExtIngressLSRLocalIdValid_Object = MibTableColumn
mplsTunnelExtIngressLSRLocalIdValid = _MplsTunnelExtIngressLSRLocalIdValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 6),
    _MplsTunnelExtIngressLSRLocalIdValid_Type()
)
mplsTunnelExtIngressLSRLocalIdValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtIngressLSRLocalIdValid.setStatus("current")


class _MplsTunnelExtEgressLSRLocalIdValid_Type(TruthValue):
    """Custom type mplsTunnelExtEgressLSRLocalIdValid based on TruthValue"""


_MplsTunnelExtEgressLSRLocalIdValid_Object = MibTableColumn
mplsTunnelExtEgressLSRLocalIdValid = _MplsTunnelExtEgressLSRLocalIdValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 0, 5, 1, 7),
    _MplsTunnelExtEgressLSRLocalIdValid_Type()
)
mplsTunnelExtEgressLSRLocalIdValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtEgressLSRLocalIdValid.setStatus("current")
_MplsTeExtConformance_ObjectIdentity = ObjectIdentity
mplsTeExtConformance = _MplsTeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1)
)
_MplsTeExtCompliances_ObjectIdentity = ObjectIdentity
mplsTeExtCompliances = _MplsTeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1)
)
_MplsTeExtGroups_ObjectIdentity = ObjectIdentity
mplsTeExtGroups = _MplsTeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2)
)

# Managed Objects groups

mplsTunnelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 1)
)
mplsTunnelExtGroup.setObjects(
      *(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtOppositeDirPtr"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtOppositeDirTnlValid"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlIndex"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlLspIndex"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtDestTnlValid"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtIngressLSRLocalIdValid"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtEgressLSRLocalIdValid"))
)
if mibBuilder.loadTexts:
    mplsTunnelExtGroup.setStatus("current")

mplsTunnelExtIpOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 2)
)
mplsTunnelExtIpOperatorGroup.setObjects(
      *(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalIdNext"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigGlobalId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigNodeId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIpMapLocalId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigStorageType"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigRowStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelExtIpOperatorGroup.setStatus("current")

mplsTunnelExtIccOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 2, 3)
)
mplsTunnelExtIccOperatorGroup.setObjects(
      *(("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigLocalIdNext"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigCcId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigIccId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigNodeId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigIccValid"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeIccMapLocalId"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigStorageType"),
        ("MPLS-TE-EXT-STD-MIB", "mplsTunnelExtNodeConfigRowStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelExtIccOperatorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsTeExtModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mplsTeExtModuleFullCompliance.setStatus(
        "current"
    )

mplsTeExtModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mplsTeExtModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-TE-EXT-STD-MIB",
    **{"mplsTeExtStdMIB": mplsTeExtStdMIB,
       "mplsTeExtObjects": mplsTeExtObjects,
       "mplsTunnelExtNodeConfigLocalIdNext": mplsTunnelExtNodeConfigLocalIdNext,
       "mplsTunnelExtNodeConfigTable": mplsTunnelExtNodeConfigTable,
       "mplsTunnelExtNodeConfigEntry": mplsTunnelExtNodeConfigEntry,
       "mplsTunnelExtNodeConfigLocalId": mplsTunnelExtNodeConfigLocalId,
       "mplsTunnelExtNodeConfigGlobalId": mplsTunnelExtNodeConfigGlobalId,
       "mplsTunnelExtNodeConfigCcId": mplsTunnelExtNodeConfigCcId,
       "mplsTunnelExtNodeConfigIccId": mplsTunnelExtNodeConfigIccId,
       "mplsTunnelExtNodeConfigNodeId": mplsTunnelExtNodeConfigNodeId,
       "mplsTunnelExtNodeConfigIccValid": mplsTunnelExtNodeConfigIccValid,
       "mplsTunnelExtNodeConfigStorageType": mplsTunnelExtNodeConfigStorageType,
       "mplsTunnelExtNodeConfigRowStatus": mplsTunnelExtNodeConfigRowStatus,
       "mplsTunnelExtNodeIpMapTable": mplsTunnelExtNodeIpMapTable,
       "mplsTunnelExtNodeIpMapEntry": mplsTunnelExtNodeIpMapEntry,
       "mplsTunnelExtNodeIpMapGlobalId": mplsTunnelExtNodeIpMapGlobalId,
       "mplsTunnelExtNodeIpMapNodeId": mplsTunnelExtNodeIpMapNodeId,
       "mplsTunnelExtNodeIpMapLocalId": mplsTunnelExtNodeIpMapLocalId,
       "mplsTunnelExtNodeIccMapTable": mplsTunnelExtNodeIccMapTable,
       "mplsTunnelExtNodeIccMapEntry": mplsTunnelExtNodeIccMapEntry,
       "mplsTunnelExtNodeIccMapCcId": mplsTunnelExtNodeIccMapCcId,
       "mplsTunnelExtNodeIccMapIccId": mplsTunnelExtNodeIccMapIccId,
       "mplsTunnelExtNodeIccMapNodeId": mplsTunnelExtNodeIccMapNodeId,
       "mplsTunnelExtNodeIccMapLocalId": mplsTunnelExtNodeIccMapLocalId,
       "mplsTunnelExtTable": mplsTunnelExtTable,
       "mplsTunnelExtEntry": mplsTunnelExtEntry,
       "mplsTunnelExtOppositeDirPtr": mplsTunnelExtOppositeDirPtr,
       "mplsTunnelExtOppositeDirTnlValid": mplsTunnelExtOppositeDirTnlValid,
       "mplsTunnelExtDestTnlIndex": mplsTunnelExtDestTnlIndex,
       "mplsTunnelExtDestTnlLspIndex": mplsTunnelExtDestTnlLspIndex,
       "mplsTunnelExtDestTnlValid": mplsTunnelExtDestTnlValid,
       "mplsTunnelExtIngressLSRLocalIdValid": mplsTunnelExtIngressLSRLocalIdValid,
       "mplsTunnelExtEgressLSRLocalIdValid": mplsTunnelExtEgressLSRLocalIdValid,
       "mplsTeExtConformance": mplsTeExtConformance,
       "mplsTeExtCompliances": mplsTeExtCompliances,
       "mplsTeExtModuleFullCompliance": mplsTeExtModuleFullCompliance,
       "mplsTeExtModuleReadOnlyCompliance": mplsTeExtModuleReadOnlyCompliance,
       "mplsTeExtGroups": mplsTeExtGroups,
       "mplsTunnelExtGroup": mplsTunnelExtGroup,
       "mplsTunnelExtIpOperatorGroup": mplsTunnelExtIpOperatorGroup,
       "mplsTunnelExtIccOperatorGroup": mplsTunnelExtIccOperatorGroup}
)
