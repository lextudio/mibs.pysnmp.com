# SNMP MIB module (CISCO-IETF-MPLS-TE-EXT-STD-03-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-MPLS-TE-EXT-STD-03-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:42 2024
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

(CMplsGlobalId,
 CMplsIccId,
 CMplsLocalId,
 CMplsNodeId) = mibBuilder.importSymbols(
    "CISCO-MPLS-TC-EXT-STD-MIB",
    "CMplsGlobalId",
    "CMplsIccId",
    "CMplsLocalId",
    "CMplsNodeId")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
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
    "iso",
    "zeroDotZero")

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

cmplsTeExtStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146)
)
cmplsTeExtStdMIB.setRevisions(
        ("2012-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmplsTeExtNotifications_ObjectIdentity = ObjectIdentity
cmplsTeExtNotifications = _CmplsTeExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 0)
)
_CmplsTeExtObjects_ObjectIdentity = ObjectIdentity
cmplsTeExtObjects = _CmplsTeExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1)
)
_CmplsNodeConfigTable_Object = MibTable
cmplsNodeConfigTable = _CmplsNodeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1)
)
if mibBuilder.loadTexts:
    cmplsNodeConfigTable.setStatus("current")
_CmplsNodeConfigEntry_Object = MibTableRow
cmplsNodeConfigEntry = _CmplsNodeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1)
)
cmplsNodeConfigEntry.setIndexNames(
    (0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigLocalId"),
)
if mibBuilder.loadTexts:
    cmplsNodeConfigEntry.setStatus("current")
_CmplsNodeConfigLocalId_Type = CMplsLocalId
_CmplsNodeConfigLocalId_Object = MibTableColumn
cmplsNodeConfigLocalId = _CmplsNodeConfigLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 1),
    _CmplsNodeConfigLocalId_Type()
)
cmplsNodeConfigLocalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsNodeConfigLocalId.setStatus("current")
_CmplsNodeConfigGlobalId_Type = CMplsGlobalId
_CmplsNodeConfigGlobalId_Object = MibTableColumn
cmplsNodeConfigGlobalId = _CmplsNodeConfigGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 2),
    _CmplsNodeConfigGlobalId_Type()
)
cmplsNodeConfigGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeConfigGlobalId.setStatus("current")
_CmplsNodeConfigNodeId_Type = CMplsNodeId
_CmplsNodeConfigNodeId_Object = MibTableColumn
cmplsNodeConfigNodeId = _CmplsNodeConfigNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 3),
    _CmplsNodeConfigNodeId_Type()
)
cmplsNodeConfigNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeConfigNodeId.setStatus("current")
_CmplsNodeConfigIccId_Type = CMplsIccId
_CmplsNodeConfigIccId_Object = MibTableColumn
cmplsNodeConfigIccId = _CmplsNodeConfigIccId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 4),
    _CmplsNodeConfigIccId_Type()
)
cmplsNodeConfigIccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeConfigIccId.setStatus("current")
_CmplsNodeConfigRowStatus_Type = RowStatus
_CmplsNodeConfigRowStatus_Object = MibTableColumn
cmplsNodeConfigRowStatus = _CmplsNodeConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 5),
    _CmplsNodeConfigRowStatus_Type()
)
cmplsNodeConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeConfigRowStatus.setStatus("current")


class _CmplsNodeConfigStorageType_Type(StorageType):
    """Custom type cmplsNodeConfigStorageType based on StorageType"""


_CmplsNodeConfigStorageType_Object = MibTableColumn
cmplsNodeConfigStorageType = _CmplsNodeConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 1, 1, 6),
    _CmplsNodeConfigStorageType_Type()
)
cmplsNodeConfigStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsNodeConfigStorageType.setStatus("current")
_CmplsNodeIpMapTable_Object = MibTable
cmplsNodeIpMapTable = _CmplsNodeIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2)
)
if mibBuilder.loadTexts:
    cmplsNodeIpMapTable.setStatus("current")
_CmplsNodeIpMapEntry_Object = MibTableRow
cmplsNodeIpMapEntry = _CmplsNodeIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1)
)
cmplsNodeIpMapEntry.setIndexNames(
    (0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapGlobalId"),
    (0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapNodeId"),
)
if mibBuilder.loadTexts:
    cmplsNodeIpMapEntry.setStatus("current")
_CmplsNodeIpMapGlobalId_Type = CMplsGlobalId
_CmplsNodeIpMapGlobalId_Object = MibTableColumn
cmplsNodeIpMapGlobalId = _CmplsNodeIpMapGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 1),
    _CmplsNodeIpMapGlobalId_Type()
)
cmplsNodeIpMapGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsNodeIpMapGlobalId.setStatus("current")
_CmplsNodeIpMapNodeId_Type = CMplsNodeId
_CmplsNodeIpMapNodeId_Object = MibTableColumn
cmplsNodeIpMapNodeId = _CmplsNodeIpMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 2),
    _CmplsNodeIpMapNodeId_Type()
)
cmplsNodeIpMapNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsNodeIpMapNodeId.setStatus("current")
_CmplsNodeIpMapLocalId_Type = CMplsLocalId
_CmplsNodeIpMapLocalId_Object = MibTableColumn
cmplsNodeIpMapLocalId = _CmplsNodeIpMapLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 2, 1, 3),
    _CmplsNodeIpMapLocalId_Type()
)
cmplsNodeIpMapLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsNodeIpMapLocalId.setStatus("current")
_CmplsNodeIccMapTable_Object = MibTable
cmplsNodeIccMapTable = _CmplsNodeIccMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3)
)
if mibBuilder.loadTexts:
    cmplsNodeIccMapTable.setStatus("current")
_CmplsNodeIccMapEntry_Object = MibTableRow
cmplsNodeIccMapEntry = _CmplsNodeIccMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1)
)
cmplsNodeIccMapEntry.setIndexNames(
    (0, "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIccMapIccId"),
)
if mibBuilder.loadTexts:
    cmplsNodeIccMapEntry.setStatus("current")
_CmplsNodeIccMapIccId_Type = CMplsIccId
_CmplsNodeIccMapIccId_Object = MibTableColumn
cmplsNodeIccMapIccId = _CmplsNodeIccMapIccId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1, 1),
    _CmplsNodeIccMapIccId_Type()
)
cmplsNodeIccMapIccId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsNodeIccMapIccId.setStatus("current")
_CmplsNodeIccMapLocalId_Type = CMplsLocalId
_CmplsNodeIccMapLocalId_Object = MibTableColumn
cmplsNodeIccMapLocalId = _CmplsNodeIccMapLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 3, 1, 2),
    _CmplsNodeIccMapLocalId_Type()
)
cmplsNodeIccMapLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsNodeIccMapLocalId.setStatus("current")
_CmplsTunnelExtTable_Object = MibTable
cmplsTunnelExtTable = _CmplsTunnelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4)
)
if mibBuilder.loadTexts:
    cmplsTunnelExtTable.setStatus("current")
_CmplsTunnelExtEntry_Object = MibTableRow
cmplsTunnelExtEntry = _CmplsTunnelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1)
)
cmplsTunnelExtEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTunnelExtEntry.setStatus("current")


class _CmplsTunnelOppositeDirPtr_Type(RowPointer):
    """Custom type cmplsTunnelOppositeDirPtr based on RowPointer"""
    defaultValue = (0, 0)


_CmplsTunnelOppositeDirPtr_Object = MibTableColumn
cmplsTunnelOppositeDirPtr = _CmplsTunnelOppositeDirPtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 1),
    _CmplsTunnelOppositeDirPtr_Type()
)
cmplsTunnelOppositeDirPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTunnelOppositeDirPtr.setStatus("current")


class _CmplsTunnelExtOppositeDirTnlValid_Type(TruthValue):
    """Custom type cmplsTunnelExtOppositeDirTnlValid based on TruthValue"""


_CmplsTunnelExtOppositeDirTnlValid_Object = MibTableColumn
cmplsTunnelExtOppositeDirTnlValid = _CmplsTunnelExtOppositeDirTnlValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 2),
    _CmplsTunnelExtOppositeDirTnlValid_Type()
)
cmplsTunnelExtOppositeDirTnlValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTunnelExtOppositeDirTnlValid.setStatus("current")
_CmplsTunnelExtDestTnlIndex_Type = MplsTunnelIndex
_CmplsTunnelExtDestTnlIndex_Object = MibTableColumn
cmplsTunnelExtDestTnlIndex = _CmplsTunnelExtDestTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 3),
    _CmplsTunnelExtDestTnlIndex_Type()
)
cmplsTunnelExtDestTnlIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTunnelExtDestTnlIndex.setStatus("current")
_CmplsTunnelExtDestTnlLspIndex_Type = MplsTunnelInstanceIndex
_CmplsTunnelExtDestTnlLspIndex_Object = MibTableColumn
cmplsTunnelExtDestTnlLspIndex = _CmplsTunnelExtDestTnlLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 4),
    _CmplsTunnelExtDestTnlLspIndex_Type()
)
cmplsTunnelExtDestTnlLspIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTunnelExtDestTnlLspIndex.setStatus("current")


class _CmplsTunnelExtDestTnlValid_Type(TruthValue):
    """Custom type cmplsTunnelExtDestTnlValid based on TruthValue"""


_CmplsTunnelExtDestTnlValid_Object = MibTableColumn
cmplsTunnelExtDestTnlValid = _CmplsTunnelExtDestTnlValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 4, 1, 5),
    _CmplsTunnelExtDestTnlValid_Type()
)
cmplsTunnelExtDestTnlValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsTunnelExtDestTnlValid.setStatus("current")
_CmplsTunnelReversePerfTable_Object = MibTable
cmplsTunnelReversePerfTable = _CmplsTunnelReversePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5)
)
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfTable.setStatus("current")
_CmplsTunnelReversePerfEntry_Object = MibTableRow
cmplsTunnelReversePerfEntry = _CmplsTunnelReversePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1)
)
cmplsTunnelReversePerfEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfEntry.setStatus("current")
_CmplsTunnelReversePerfPackets_Type = Counter32
_CmplsTunnelReversePerfPackets_Object = MibTableColumn
cmplsTunnelReversePerfPackets = _CmplsTunnelReversePerfPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 1),
    _CmplsTunnelReversePerfPackets_Type()
)
cmplsTunnelReversePerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfPackets.setStatus("current")
_CmplsTunnelReversePerfHCPackets_Type = Counter64
_CmplsTunnelReversePerfHCPackets_Object = MibTableColumn
cmplsTunnelReversePerfHCPackets = _CmplsTunnelReversePerfHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 2),
    _CmplsTunnelReversePerfHCPackets_Type()
)
cmplsTunnelReversePerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfHCPackets.setStatus("current")
_CmplsTunnelReversePerfErrors_Type = Counter32
_CmplsTunnelReversePerfErrors_Object = MibTableColumn
cmplsTunnelReversePerfErrors = _CmplsTunnelReversePerfErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 3),
    _CmplsTunnelReversePerfErrors_Type()
)
cmplsTunnelReversePerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfErrors.setStatus("current")
_CmplsTunnelReversePerfBytes_Type = Counter32
_CmplsTunnelReversePerfBytes_Object = MibTableColumn
cmplsTunnelReversePerfBytes = _CmplsTunnelReversePerfBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 4),
    _CmplsTunnelReversePerfBytes_Type()
)
cmplsTunnelReversePerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfBytes.setStatus("current")
_CmplsTunnelReversePerfHCBytes_Type = Counter64
_CmplsTunnelReversePerfHCBytes_Object = MibTableColumn
cmplsTunnelReversePerfHCBytes = _CmplsTunnelReversePerfHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 1, 5, 1, 5),
    _CmplsTunnelReversePerfHCBytes_Type()
)
cmplsTunnelReversePerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelReversePerfHCBytes.setStatus("current")
_CmplsTeExtConformance_ObjectIdentity = ObjectIdentity
cmplsTeExtConformance = _CmplsTeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2)
)
_CmplsTeExtGroups_ObjectIdentity = ObjectIdentity
cmplsTeExtGroups = _CmplsTeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1)
)
_CmplsTeExtCompliances_ObjectIdentity = ObjectIdentity
cmplsTeExtCompliances = _CmplsTeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2)
)

# Managed Objects groups

cmplsTunnelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 1)
)
cmplsTunnelExtGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelOppositeDirPtr"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtOppositeDirTnlValid"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlIndex"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlLspIndex"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelExtDestTnlValid"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfPackets"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfHCPackets"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfErrors"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfBytes"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsTunnelReversePerfHCBytes"))
)
if mibBuilder.loadTexts:
    cmplsTunnelExtGroup.setStatus("current")

cmplsTunnelExtIpOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 2)
)
cmplsTunnelExtIpOperatorGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigGlobalId"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigNodeId"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigRowStatus"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigStorageType"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIpMapLocalId"))
)
if mibBuilder.loadTexts:
    cmplsTunnelExtIpOperatorGroup.setStatus("current")

cmplsTunnelExtIccOperatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 1, 3)
)
cmplsTunnelExtIccOperatorGroup.setObjects(
      *(("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigIccId"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigRowStatus"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeConfigStorageType"),
        ("CISCO-IETF-MPLS-TE-EXT-STD-03-MIB", "cmplsNodeIccMapLocalId"))
)
if mibBuilder.loadTexts:
    cmplsTunnelExtIccOperatorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmplsTeExtModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmplsTeExtModuleFullCompliance.setStatus(
        "current"
    )

cmplsTeExtModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 146, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cmplsTeExtModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB",
    **{"cmplsTeExtStdMIB": cmplsTeExtStdMIB,
       "cmplsTeExtNotifications": cmplsTeExtNotifications,
       "cmplsTeExtObjects": cmplsTeExtObjects,
       "cmplsNodeConfigTable": cmplsNodeConfigTable,
       "cmplsNodeConfigEntry": cmplsNodeConfigEntry,
       "cmplsNodeConfigLocalId": cmplsNodeConfigLocalId,
       "cmplsNodeConfigGlobalId": cmplsNodeConfigGlobalId,
       "cmplsNodeConfigNodeId": cmplsNodeConfigNodeId,
       "cmplsNodeConfigIccId": cmplsNodeConfigIccId,
       "cmplsNodeConfigRowStatus": cmplsNodeConfigRowStatus,
       "cmplsNodeConfigStorageType": cmplsNodeConfigStorageType,
       "cmplsNodeIpMapTable": cmplsNodeIpMapTable,
       "cmplsNodeIpMapEntry": cmplsNodeIpMapEntry,
       "cmplsNodeIpMapGlobalId": cmplsNodeIpMapGlobalId,
       "cmplsNodeIpMapNodeId": cmplsNodeIpMapNodeId,
       "cmplsNodeIpMapLocalId": cmplsNodeIpMapLocalId,
       "cmplsNodeIccMapTable": cmplsNodeIccMapTable,
       "cmplsNodeIccMapEntry": cmplsNodeIccMapEntry,
       "cmplsNodeIccMapIccId": cmplsNodeIccMapIccId,
       "cmplsNodeIccMapLocalId": cmplsNodeIccMapLocalId,
       "cmplsTunnelExtTable": cmplsTunnelExtTable,
       "cmplsTunnelExtEntry": cmplsTunnelExtEntry,
       "cmplsTunnelOppositeDirPtr": cmplsTunnelOppositeDirPtr,
       "cmplsTunnelExtOppositeDirTnlValid": cmplsTunnelExtOppositeDirTnlValid,
       "cmplsTunnelExtDestTnlIndex": cmplsTunnelExtDestTnlIndex,
       "cmplsTunnelExtDestTnlLspIndex": cmplsTunnelExtDestTnlLspIndex,
       "cmplsTunnelExtDestTnlValid": cmplsTunnelExtDestTnlValid,
       "cmplsTunnelReversePerfTable": cmplsTunnelReversePerfTable,
       "cmplsTunnelReversePerfEntry": cmplsTunnelReversePerfEntry,
       "cmplsTunnelReversePerfPackets": cmplsTunnelReversePerfPackets,
       "cmplsTunnelReversePerfHCPackets": cmplsTunnelReversePerfHCPackets,
       "cmplsTunnelReversePerfErrors": cmplsTunnelReversePerfErrors,
       "cmplsTunnelReversePerfBytes": cmplsTunnelReversePerfBytes,
       "cmplsTunnelReversePerfHCBytes": cmplsTunnelReversePerfHCBytes,
       "cmplsTeExtConformance": cmplsTeExtConformance,
       "cmplsTeExtGroups": cmplsTeExtGroups,
       "cmplsTunnelExtGroup": cmplsTunnelExtGroup,
       "cmplsTunnelExtIpOperatorGroup": cmplsTunnelExtIpOperatorGroup,
       "cmplsTunnelExtIccOperatorGroup": cmplsTunnelExtIccOperatorGroup,
       "cmplsTeExtCompliances": cmplsTeExtCompliances,
       "cmplsTeExtModuleFullCompliance": cmplsTeExtModuleFullCompliance,
       "cmplsTeExtModuleReadOnlyCompliance": cmplsTeExtModuleReadOnlyCompliance}
)
