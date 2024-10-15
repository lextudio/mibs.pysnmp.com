# SNMP MIB module (DLINK-3100-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:12 2024
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

(diffServClassifierEntry,) = mibBuilder.importSymbols(
    "DIFF-SERV-MIB",
    "diffServClassifierEntry")

(Percents,
 VlanPriority,
 rnd) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "Percents",
    "VlanPriority",
    "rnd")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59)
)
rlPolicy.setRevisions(
        ("2005-03-14 00:00",
         "2005-02-07 00:00",
         "2005-01-27 00:00",
         "2003-10-07 00:00",
         "2003-09-22 00:00",
         "2005-04-14 00:00",
         "2005-04-17 00:00",
         "2006-04-08 00:00",
         "2006-05-20 00:00",
         "2006-06-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 2),
          ("vlan", 1))
    )



class StatisticsCntrNumOfBitsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("uint32", 32),
          ("uint48", 48),
          ("uint64", 64))
    )



class StatisticsDPType(Integer32, TextualConvention):
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
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )



class StatisticsClearActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("action", 2),
          ("noaction", 1))
    )



class StatisticsCntrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statisticsCntrTypeDeny", 2),
          ("statisticsCntrTypeSetDSCP", 1))
    )



class RlPolicyGroupType(Integer32, TextualConvention):
    status = "current"
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
        *(("bridged", 1),
          ("notUsed", 4),
          ("routedIp", 2),
          ("routedIpx", 3))
    )



class RlPolicyClassifierDiffservIfType(Integer32, TextualConvention):
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
        *(("allBoundaryPorts", 2),
          ("allInteriorPorts", 3),
          ("normal", 1))
    )



class RlPolicyTrustTypes(Integer32, TextualConvention):
    status = "current"
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
        *(("cos", 1),
          ("cos-dscp", 5),
          ("dscp", 2),
          ("none", 4),
          ("tcp-udp", 3))
    )



class RlPolicyQosMode(Integer32, TextualConvention):
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
        *(("advanced", 2),
          ("basic", 1),
          ("service", 3))
    )



class L4ProtType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )



class RlPolicyTimeBasedAclWeekPeriodicList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RlPolicyMibVersion_Type = Integer32
_RlPolicyMibVersion_Object = MibScalar
rlPolicyMibVersion = _RlPolicyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 1),
    _RlPolicyMibVersion_Type()
)
rlPolicyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMibVersion.setStatus("current")
_RlPolicyClassifier_ObjectIdentity = ObjectIdentity
rlPolicyClassifier = _RlPolicyClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2)
)
_RlPolicyClassifierPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyClassifierPlatDependParams = _RlPolicyClassifierPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1)
)


class _RlPolicyFlowClassificationOffsetsGroupScheme_Type(Integer32):
    """Custom type rlPolicyFlowClassificationOffsetsGroupScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOffsetsPermitted", 1),
          ("singleFlowClassificationOffsetGroupsForIpIpxBridge", 2))
    )


_RlPolicyFlowClassificationOffsetsGroupScheme_Type.__name__ = "Integer32"
_RlPolicyFlowClassificationOffsetsGroupScheme_Object = MibScalar
rlPolicyFlowClassificationOffsetsGroupScheme = _RlPolicyFlowClassificationOffsetsGroupScheme_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 1),
    _RlPolicyFlowClassificationOffsetsGroupScheme_Type()
)
rlPolicyFlowClassificationOffsetsGroupScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupScheme.setStatus("current")
_RlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup_Type = Integer32
_RlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup_Object = MibScalar
rlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup = _RlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 2),
    _RlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup_Type()
)
rlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup.setStatus("current")
_RlPolicyFlowClassificationOffsetGroupMaximumOffset_Type = Integer32
_RlPolicyFlowClassificationOffsetGroupMaximumOffset_Object = MibScalar
rlPolicyFlowClassificationOffsetGroupMaximumOffset = _RlPolicyFlowClassificationOffsetGroupMaximumOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 3),
    _RlPolicyFlowClassificationOffsetGroupMaximumOffset_Type()
)
rlPolicyFlowClassificationOffsetGroupMaximumOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetGroupMaximumOffset.setStatus("current")
_RlPolicyNumberOfOffsetsPerOmpcGroup_Type = Integer32
_RlPolicyNumberOfOffsetsPerOmpcGroup_Object = MibScalar
rlPolicyNumberOfOffsetsPerOmpcGroup = _RlPolicyNumberOfOffsetsPerOmpcGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 4),
    _RlPolicyNumberOfOffsetsPerOmpcGroup_Type()
)
rlPolicyNumberOfOffsetsPerOmpcGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyNumberOfOffsetsPerOmpcGroup.setStatus("current")
_RlPolicyOmpcMaximumOffset_Type = Integer32
_RlPolicyOmpcMaximumOffset_Object = MibScalar
rlPolicyOmpcMaximumOffset = _RlPolicyOmpcMaximumOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 5),
    _RlPolicyOmpcMaximumOffset_Type()
)
rlPolicyOmpcMaximumOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOmpcMaximumOffset.setStatus("current")


class _RlPolicyOMPCPermittedOperators_Type(OctetString):
    """Custom type rlPolicyOMPCPermittedOperators based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyOMPCPermittedOperators_Type.__name__ = "OctetString"
_RlPolicyOMPCPermittedOperators_Object = MibScalar
rlPolicyOMPCPermittedOperators = _RlPolicyOMPCPermittedOperators_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 6),
    _RlPolicyOMPCPermittedOperators_Type()
)
rlPolicyOMPCPermittedOperators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOMPCPermittedOperators.setStatus("current")
_RlPolicyMaxOMPCLengthForBiggerSmallerOperation_Type = Integer32
_RlPolicyMaxOMPCLengthForBiggerSmallerOperation_Object = MibScalar
rlPolicyMaxOMPCLengthForBiggerSmallerOperation = _RlPolicyMaxOMPCLengthForBiggerSmallerOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 7),
    _RlPolicyMaxOMPCLengthForBiggerSmallerOperation_Type()
)
rlPolicyMaxOMPCLengthForBiggerSmallerOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMaxOMPCLengthForBiggerSmallerOperation.setStatus("current")


class _RlPolicyClassifierAdditionalCriteriaSupported_Type(OctetString):
    """Custom type rlPolicyClassifierAdditionalCriteriaSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyClassifierAdditionalCriteriaSupported_Type.__name__ = "OctetString"
_RlPolicyClassifierAdditionalCriteriaSupported_Object = MibScalar
rlPolicyClassifierAdditionalCriteriaSupported = _RlPolicyClassifierAdditionalCriteriaSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 8),
    _RlPolicyClassifierAdditionalCriteriaSupported_Type()
)
rlPolicyClassifierAdditionalCriteriaSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierAdditionalCriteriaSupported.setStatus("current")
_RlPolicyClassifierAdditionalCriteriaUsedInOffsetCount_Type = TruthValue
_RlPolicyClassifierAdditionalCriteriaUsedInOffsetCount_Object = MibScalar
rlPolicyClassifierAdditionalCriteriaUsedInOffsetCount = _RlPolicyClassifierAdditionalCriteriaUsedInOffsetCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 9),
    _RlPolicyClassifierAdditionalCriteriaUsedInOffsetCount_Type()
)
rlPolicyClassifierAdditionalCriteriaUsedInOffsetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierAdditionalCriteriaUsedInOffsetCount.setStatus("current")


class _RlPolicyClassifierPermittedOffsetTypes_Type(OctetString):
    """Custom type rlPolicyClassifierPermittedOffsetTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyClassifierPermittedOffsetTypes_Type.__name__ = "OctetString"
_RlPolicyClassifierPermittedOffsetTypes_Object = MibScalar
rlPolicyClassifierPermittedOffsetTypes = _RlPolicyClassifierPermittedOffsetTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 10),
    _RlPolicyClassifierPermittedOffsetTypes_Type()
)
rlPolicyClassifierPermittedOffsetTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierPermittedOffsetTypes.setStatus("current")


class _RlPolicyClassifierOMPCActions_Type(OctetString):
    """Custom type rlPolicyClassifierOMPCActions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyClassifierOMPCActions_Type.__name__ = "OctetString"
_RlPolicyClassifierOMPCActions_Object = MibScalar
rlPolicyClassifierOMPCActions = _RlPolicyClassifierOMPCActions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 1, 11),
    _RlPolicyClassifierOMPCActions_Type()
)
rlPolicyClassifierOMPCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierOMPCActions.setStatus("current")
_RlPolicyFlowClassificationOffsetsTable_Object = MibTable
rlPolicyFlowClassificationOffsetsTable = _RlPolicyFlowClassificationOffsetsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2)
)
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsTable.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupEntry_Object = MibTableRow
rlPolicyFlowClassificationOffsetsGroupEntry = _RlPolicyFlowClassificationOffsetsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1)
)
rlPolicyFlowClassificationOffsetsGroupEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyFlowClassificationOffsetsGroupType"),
)
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupEntry.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupType_Type = RlPolicyGroupType
_RlPolicyFlowClassificationOffsetsGroupType_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupType = _RlPolicyFlowClassificationOffsetsGroupType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 1),
    _RlPolicyFlowClassificationOffsetsGroupType_Type()
)
rlPolicyFlowClassificationOffsetsGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupType.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupOffset_Type = ObjectIdentifier
_RlPolicyFlowClassificationOffsetsGroupOffset_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupOffset = _RlPolicyFlowClassificationOffsetsGroupOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 2),
    _RlPolicyFlowClassificationOffsetsGroupOffset_Type()
)
rlPolicyFlowClassificationOffsetsGroupOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupOffset.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupOffsetType_Type = ObjectIdentifier
_RlPolicyFlowClassificationOffsetsGroupOffsetType_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupOffsetType = _RlPolicyFlowClassificationOffsetsGroupOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 3),
    _RlPolicyFlowClassificationOffsetsGroupOffsetType_Type()
)
rlPolicyFlowClassificationOffsetsGroupOffsetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupOffsetType.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupMask_Type = OctetString
_RlPolicyFlowClassificationOffsetsGroupMask_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupMask = _RlPolicyFlowClassificationOffsetsGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 4),
    _RlPolicyFlowClassificationOffsetsGroupMask_Type()
)
rlPolicyFlowClassificationOffsetsGroupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupMask.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupUseInputInterface_Type = TruthValue
_RlPolicyFlowClassificationOffsetsGroupUseInputInterface_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseInputInterface = _RlPolicyFlowClassificationOffsetsGroupUseInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 5),
    _RlPolicyFlowClassificationOffsetsGroupUseInputInterface_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseInputInterface.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupUseOutputInterface_Type = TruthValue
_RlPolicyFlowClassificationOffsetsGroupUseOutputInterface_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseOutputInterface = _RlPolicyFlowClassificationOffsetsGroupUseOutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 6),
    _RlPolicyFlowClassificationOffsetsGroupUseOutputInterface_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseOutputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseOutputInterface.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupUseVlanId_Type = TruthValue
_RlPolicyFlowClassificationOffsetsGroupUseVlanId_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseVlanId = _RlPolicyFlowClassificationOffsetsGroupUseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 7),
    _RlPolicyFlowClassificationOffsetsGroupUseVlanId_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseVlanId.setStatus("current")
_RlPolicyFlowClassificationOffsetsGroupStatus_Type = RowStatus
_RlPolicyFlowClassificationOffsetsGroupStatus_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupStatus = _RlPolicyFlowClassificationOffsetsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 8),
    _RlPolicyFlowClassificationOffsetsGroupStatus_Type()
)
rlPolicyFlowClassificationOffsetsGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupStatus.setStatus("current")


class _RlPolicyFlowClassificationOffsetsGroupUseVPTId_Type(TruthValue):
    """Custom type rlPolicyFlowClassificationOffsetsGroupUseVPTId based on TruthValue"""


_RlPolicyFlowClassificationOffsetsGroupUseVPTId_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseVPTId = _RlPolicyFlowClassificationOffsetsGroupUseVPTId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 9),
    _RlPolicyFlowClassificationOffsetsGroupUseVPTId_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseVPTId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseVPTId.setStatus("current")


class _RlPolicyFlowClassificationOffsetsGroupUseEtherTypeId_Type(TruthValue):
    """Custom type rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId based on TruthValue"""


_RlPolicyFlowClassificationOffsetsGroupUseEtherTypeId_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId = _RlPolicyFlowClassificationOffsetsGroupUseEtherTypeId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 10),
    _RlPolicyFlowClassificationOffsetsGroupUseEtherTypeId_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId.setStatus("current")


class _RlPolicyFlowClassificationOffsetsGroupUseInnerVlanId_Type(TruthValue):
    """Custom type rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId based on TruthValue"""


_RlPolicyFlowClassificationOffsetsGroupUseInnerVlanId_Object = MibTableColumn
rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId = _RlPolicyFlowClassificationOffsetsGroupUseInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 2, 1, 11),
    _RlPolicyFlowClassificationOffsetsGroupUseInnerVlanId_Type()
)
rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId.setStatus("current")
_RlPolicyOMPCTable_Object = MibTable
rlPolicyOMPCTable = _RlPolicyOMPCTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3)
)
if mibBuilder.loadTexts:
    rlPolicyOMPCTable.setStatus("current")
_RlPolicyOMPCEntry_Object = MibTableRow
rlPolicyOMPCEntry = _RlPolicyOMPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1)
)
rlPolicyOMPCEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyOMPCGroupType"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyOMPCIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyOMPCEntry.setStatus("current")
_RlPolicyOMPCGroupType_Type = RlPolicyGroupType
_RlPolicyOMPCGroupType_Object = MibTableColumn
rlPolicyOMPCGroupType = _RlPolicyOMPCGroupType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 1),
    _RlPolicyOMPCGroupType_Type()
)
rlPolicyOMPCGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOMPCGroupType.setStatus("current")


class _RlPolicyOMPCIndex_Type(Integer32):
    """Custom type rlPolicyOMPCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicyOMPCIndex_Type.__name__ = "Integer32"
_RlPolicyOMPCIndex_Object = MibTableColumn
rlPolicyOMPCIndex = _RlPolicyOMPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 2),
    _RlPolicyOMPCIndex_Type()
)
rlPolicyOMPCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOMPCIndex.setStatus("current")
_RlPolicyOMPCOffset_Type = Integer32
_RlPolicyOMPCOffset_Object = MibTableColumn
rlPolicyOMPCOffset = _RlPolicyOMPCOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 3),
    _RlPolicyOMPCOffset_Type()
)
rlPolicyOMPCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCOffset.setStatus("current")


class _RlPolicyOMPCOffsetType_Type(Integer32):
    """Custom type rlPolicyOMPCOffsetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2),
          ("l3-ipv6", 3))
    )


_RlPolicyOMPCOffsetType_Type.__name__ = "Integer32"
_RlPolicyOMPCOffsetType_Object = MibTableColumn
rlPolicyOMPCOffsetType = _RlPolicyOMPCOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 4),
    _RlPolicyOMPCOffsetType_Type()
)
rlPolicyOMPCOffsetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCOffsetType.setStatus("current")
_RlPolicyOMPCMask_Type = OctetString
_RlPolicyOMPCMask_Object = MibTableColumn
rlPolicyOMPCMask = _RlPolicyOMPCMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 5),
    _RlPolicyOMPCMask_Type()
)
rlPolicyOMPCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCMask.setStatus("current")
_RlPolicyOMPCPattern_Type = OctetString
_RlPolicyOMPCPattern_Object = MibTableColumn
rlPolicyOMPCPattern = _RlPolicyOMPCPattern_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 6),
    _RlPolicyOMPCPattern_Type()
)
rlPolicyOMPCPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCPattern.setStatus("current")


class _RlPolicyOMPCCondition_Type(Integer32):
    """Custom type rlPolicyOMPCCondition based on Integer32"""
    defaultValue = 1

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
        *(("bigger", 3),
          ("equal", 1),
          ("notEqual", 2),
          ("smaller", 4))
    )


_RlPolicyOMPCCondition_Type.__name__ = "Integer32"
_RlPolicyOMPCCondition_Object = MibTableColumn
rlPolicyOMPCCondition = _RlPolicyOMPCCondition_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 7),
    _RlPolicyOMPCCondition_Type()
)
rlPolicyOMPCCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCCondition.setStatus("current")


class _RlPolicyOMPCDescription_Type(DisplayString):
    """Custom type rlPolicyOMPCDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPolicyOMPCDescription_Type.__name__ = "DisplayString"
_RlPolicyOMPCDescription_Object = MibTableColumn
rlPolicyOMPCDescription = _RlPolicyOMPCDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 8),
    _RlPolicyOMPCDescription_Type()
)
rlPolicyOMPCDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCDescription.setStatus("current")
_RlPolicyOMPCStatus_Type = RowStatus
_RlPolicyOMPCStatus_Object = MibTableColumn
rlPolicyOMPCStatus = _RlPolicyOMPCStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 3, 1, 9),
    _RlPolicyOMPCStatus_Type()
)
rlPolicyOMPCStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOMPCStatus.setStatus("current")
_RlPolicyClassifierTable_Object = MibTable
rlPolicyClassifierTable = _RlPolicyClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4)
)
if mibBuilder.loadTexts:
    rlPolicyClassifierTable.setStatus("current")
_RlPolicyClassifierEntry_Object = MibTableRow
rlPolicyClassifierEntry = _RlPolicyClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1)
)
rlPolicyClassifierEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyClassifierType"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyClassifierIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyClassifierEntry.setStatus("current")
_RlPolicyClassifierType_Type = RlPolicyGroupType
_RlPolicyClassifierType_Object = MibTableColumn
rlPolicyClassifierType = _RlPolicyClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 1),
    _RlPolicyClassifierType_Type()
)
rlPolicyClassifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierType.setStatus("current")


class _RlPolicyClassifierIndex_Type(Integer32):
    """Custom type rlPolicyClassifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicyClassifierIndex_Type.__name__ = "Integer32"
_RlPolicyClassifierIndex_Object = MibTableColumn
rlPolicyClassifierIndex = _RlPolicyClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 2),
    _RlPolicyClassifierIndex_Type()
)
rlPolicyClassifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierIndex.setStatus("current")
_RlPolicyClassifierOmpcList_Type = ObjectIdentifier
_RlPolicyClassifierOmpcList_Object = MibTableColumn
rlPolicyClassifierOmpcList = _RlPolicyClassifierOmpcList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 3),
    _RlPolicyClassifierOmpcList_Type()
)
rlPolicyClassifierOmpcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierOmpcList.setStatus("current")


class _RlPolicyClassifierInIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlPolicyClassifierInIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlPolicyClassifierInIfIndex_Object = MibTableColumn
rlPolicyClassifierInIfIndex = _RlPolicyClassifierInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 4),
    _RlPolicyClassifierInIfIndex_Type()
)
rlPolicyClassifierInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierInIfIndex.setStatus("current")


class _RlPolicyClassifierOutIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlPolicyClassifierOutIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlPolicyClassifierOutIfIndex_Object = MibTableColumn
rlPolicyClassifierOutIfIndex = _RlPolicyClassifierOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 5),
    _RlPolicyClassifierOutIfIndex_Type()
)
rlPolicyClassifierOutIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierOutIfIndex.setStatus("current")


class _RlPolicyClassifierVID_Type(Integer32):
    """Custom type rlPolicyClassifierVID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlPolicyClassifierVID_Type.__name__ = "Integer32"
_RlPolicyClassifierVID_Object = MibTableColumn
rlPolicyClassifierVID = _RlPolicyClassifierVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 6),
    _RlPolicyClassifierVID_Type()
)
rlPolicyClassifierVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierVID.setStatus("current")


class _RlPolicyClassifierDiffservInIfType_Type(RlPolicyClassifierDiffservIfType):
    """Custom type rlPolicyClassifierDiffservInIfType based on RlPolicyClassifierDiffservIfType"""


_RlPolicyClassifierDiffservInIfType_Object = MibTableColumn
rlPolicyClassifierDiffservInIfType = _RlPolicyClassifierDiffservInIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 7),
    _RlPolicyClassifierDiffservInIfType_Type()
)
rlPolicyClassifierDiffservInIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierDiffservInIfType.setStatus("current")


class _RlPolicyClassifierDiffservOutIfType_Type(RlPolicyClassifierDiffservIfType):
    """Custom type rlPolicyClassifierDiffservOutIfType based on RlPolicyClassifierDiffservIfType"""


_RlPolicyClassifierDiffservOutIfType_Object = MibTableColumn
rlPolicyClassifierDiffservOutIfType = _RlPolicyClassifierDiffservOutIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 8),
    _RlPolicyClassifierDiffservOutIfType_Type()
)
rlPolicyClassifierDiffservOutIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierDiffservOutIfType.setStatus("current")
_RlPolicyClassifierStatus_Type = RowStatus
_RlPolicyClassifierStatus_Object = MibTableColumn
rlPolicyClassifierStatus = _RlPolicyClassifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 9),
    _RlPolicyClassifierStatus_Type()
)
rlPolicyClassifierStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierStatus.setStatus("current")
_RlPolicyClassifierInIfIndexList_Type = PortList
_RlPolicyClassifierInIfIndexList_Object = MibTableColumn
rlPolicyClassifierInIfIndexList = _RlPolicyClassifierInIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 10),
    _RlPolicyClassifierInIfIndexList_Type()
)
rlPolicyClassifierInIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierInIfIndexList.setStatus("current")
_RlPolicyClassifierOutIfIndexList_Type = PortList
_RlPolicyClassifierOutIfIndexList_Object = MibTableColumn
rlPolicyClassifierOutIfIndexList = _RlPolicyClassifierOutIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 11),
    _RlPolicyClassifierOutIfIndexList_Type()
)
rlPolicyClassifierOutIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierOutIfIndexList.setStatus("current")


class _RlPolicyClassifierVPTID_Type(Integer32):
    """Custom type rlPolicyClassifierVPTID based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RlPolicyClassifierVPTID_Type.__name__ = "Integer32"
_RlPolicyClassifierVPTID_Object = MibTableColumn
rlPolicyClassifierVPTID = _RlPolicyClassifierVPTID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 12),
    _RlPolicyClassifierVPTID_Type()
)
rlPolicyClassifierVPTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierVPTID.setStatus("current")


class _RlPolicyClassifierVPTIDMask_Type(Integer32):
    """Custom type rlPolicyClassifierVPTIDMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyClassifierVPTIDMask_Type.__name__ = "Integer32"
_RlPolicyClassifierVPTIDMask_Object = MibTableColumn
rlPolicyClassifierVPTIDMask = _RlPolicyClassifierVPTIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 13),
    _RlPolicyClassifierVPTIDMask_Type()
)
rlPolicyClassifierVPTIDMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierVPTIDMask.setStatus("current")


class _RlPolicyClassifierEtherTypeID_Type(Integer32):
    """Custom type rlPolicyClassifierEtherTypeID based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1499, 65536),
    )


_RlPolicyClassifierEtherTypeID_Type.__name__ = "Integer32"
_RlPolicyClassifierEtherTypeID_Object = MibTableColumn
rlPolicyClassifierEtherTypeID = _RlPolicyClassifierEtherTypeID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 14),
    _RlPolicyClassifierEtherTypeID_Type()
)
rlPolicyClassifierEtherTypeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierEtherTypeID.setStatus("current")


class _RlPolicyClassifierInnerVID_Type(Integer32):
    """Custom type rlPolicyClassifierInnerVID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlPolicyClassifierInnerVID_Type.__name__ = "Integer32"
_RlPolicyClassifierInnerVID_Object = MibTableColumn
rlPolicyClassifierInnerVID = _RlPolicyClassifierInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 2, 4, 1, 15),
    _RlPolicyClassifierInnerVID_Type()
)
rlPolicyClassifierInnerVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClassifierInnerVID.setStatus("current")
_RlPolicyRules_ObjectIdentity = ObjectIdentity
rlPolicyRules = _RlPolicyRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3)
)
_RlPolicyRulesPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyRulesPlatDependParams = _RlPolicyRulesPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 1)
)
_RlPolicyDroppedPacketCountSupported_Type = TruthValue
_RlPolicyDroppedPacketCountSupported_Object = MibScalar
rlPolicyDroppedPacketCountSupported = _RlPolicyDroppedPacketCountSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 1, 1),
    _RlPolicyDroppedPacketCountSupported_Type()
)
rlPolicyDroppedPacketCountSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDroppedPacketCountSupported.setStatus("current")


class _RlPolicyFilterActionOptions_Type(OctetString):
    """Custom type rlPolicyFilterActionOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyFilterActionOptions_Type.__name__ = "OctetString"
_RlPolicyFilterActionOptions_Object = MibScalar
rlPolicyFilterActionOptions = _RlPolicyFilterActionOptions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 1, 2),
    _RlPolicyFilterActionOptions_Type()
)
rlPolicyFilterActionOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyFilterActionOptions.setStatus("current")
_RlPolicyIngressMeteringSupported_Type = TruthValue
_RlPolicyIngressMeteringSupported_Object = MibScalar
rlPolicyIngressMeteringSupported = _RlPolicyIngressMeteringSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 1, 3),
    _RlPolicyIngressMeteringSupported_Type()
)
rlPolicyIngressMeteringSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyIngressMeteringSupported.setStatus("current")
_RlPolicyEgressMeteringSupported_Type = TruthValue
_RlPolicyEgressMeteringSupported_Object = MibScalar
rlPolicyEgressMeteringSupported = _RlPolicyEgressMeteringSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 1, 4),
    _RlPolicyEgressMeteringSupported_Type()
)
rlPolicyEgressMeteringSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyEgressMeteringSupported.setStatus("current")
_RlPolicyRulesTable_Object = MibTable
rlPolicyRulesTable = _RlPolicyRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2)
)
if mibBuilder.loadTexts:
    rlPolicyRulesTable.setStatus("current")
_RlPolicyRulesEntry_Object = MibTableRow
rlPolicyRulesEntry = _RlPolicyRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1)
)
rlPolicyRulesEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyRulesTableType"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyRulesInterfaceDirection"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyRulesIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyRulesEntry.setStatus("current")
_RlPolicyRulesTableType_Type = RlPolicyGroupType
_RlPolicyRulesTableType_Object = MibTableColumn
rlPolicyRulesTableType = _RlPolicyRulesTableType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 1),
    _RlPolicyRulesTableType_Type()
)
rlPolicyRulesTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRulesTableType.setStatus("current")


class _RlPolicyRulesInterfaceDirection_Type(Integer32):
    """Custom type rlPolicyRulesInterfaceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("none", 3),
          ("outbound", 2))
    )


_RlPolicyRulesInterfaceDirection_Type.__name__ = "Integer32"
_RlPolicyRulesInterfaceDirection_Object = MibTableColumn
rlPolicyRulesInterfaceDirection = _RlPolicyRulesInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 2),
    _RlPolicyRulesInterfaceDirection_Type()
)
rlPolicyRulesInterfaceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRulesInterfaceDirection.setStatus("current")


class _RlPolicyRulesIndex_Type(Integer32):
    """Custom type rlPolicyRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicyRulesIndex_Type.__name__ = "Integer32"
_RlPolicyRulesIndex_Object = MibTableColumn
rlPolicyRulesIndex = _RlPolicyRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 3),
    _RlPolicyRulesIndex_Type()
)
rlPolicyRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRulesIndex.setStatus("current")
_RlPolicyRulesClassifierPointer_Type = Integer32
_RlPolicyRulesClassifierPointer_Object = MibTableColumn
rlPolicyRulesClassifierPointer = _RlPolicyRulesClassifierPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 4),
    _RlPolicyRulesClassifierPointer_Type()
)
rlPolicyRulesClassifierPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesClassifierPointer.setStatus("current")


class _RlPolicyRulesFilteringAction_Type(Integer32):
    """Custom type rlPolicyRulesFilteringAction based on Integer32"""
    defaultValue = 4

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
        *(("block", 1),
          ("blockAndDisablePort", 5),
          ("blockAndTrap", 2),
          ("blockTrapAndDisablePort", 6),
          ("permit", 4),
          ("permitAndTrap", 3))
    )


_RlPolicyRulesFilteringAction_Type.__name__ = "Integer32"
_RlPolicyRulesFilteringAction_Object = MibTableColumn
rlPolicyRulesFilteringAction = _RlPolicyRulesFilteringAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 5),
    _RlPolicyRulesFilteringAction_Type()
)
rlPolicyRulesFilteringAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesFilteringAction.setStatus("current")
_RlPolicyRulesDroppedPackets_Type = Counter32
_RlPolicyRulesDroppedPackets_Object = MibTableColumn
rlPolicyRulesDroppedPackets = _RlPolicyRulesDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 6),
    _RlPolicyRulesDroppedPackets_Type()
)
rlPolicyRulesDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRulesDroppedPackets.setStatus("current")
_RlPolicyRulesFurtherRefPointer_Type = Integer32
_RlPolicyRulesFurtherRefPointer_Object = MibTableColumn
rlPolicyRulesFurtherRefPointer = _RlPolicyRulesFurtherRefPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 7),
    _RlPolicyRulesFurtherRefPointer_Type()
)
rlPolicyRulesFurtherRefPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesFurtherRefPointer.setStatus("current")


class _RlPolicyRulesDescription_Type(DisplayString):
    """Custom type rlPolicyRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPolicyRulesDescription_Type.__name__ = "DisplayString"
_RlPolicyRulesDescription_Object = MibTableColumn
rlPolicyRulesDescription = _RlPolicyRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 8),
    _RlPolicyRulesDescription_Type()
)
rlPolicyRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesDescription.setStatus("current")
_RlPolicyRulesStatus_Type = RowStatus
_RlPolicyRulesStatus_Object = MibTableColumn
rlPolicyRulesStatus = _RlPolicyRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 9),
    _RlPolicyRulesStatus_Type()
)
rlPolicyRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesStatus.setStatus("current")


class _RlPolicyRulesCounterEnable_Type(TruthValue):
    """Custom type rlPolicyRulesCounterEnable based on TruthValue"""


_RlPolicyRulesCounterEnable_Object = MibTableColumn
rlPolicyRulesCounterEnable = _RlPolicyRulesCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 10),
    _RlPolicyRulesCounterEnable_Type()
)
rlPolicyRulesCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesCounterEnable.setStatus("current")
_RlPolicyRulesCounter_Type = Counter32
_RlPolicyRulesCounter_Object = MibTableColumn
rlPolicyRulesCounter = _RlPolicyRulesCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 11),
    _RlPolicyRulesCounter_Type()
)
rlPolicyRulesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRulesCounter.setStatus("current")
_RlPolicyRulesActionPointer_Type = Integer32
_RlPolicyRulesActionPointer_Object = MibTableColumn
rlPolicyRulesActionPointer = _RlPolicyRulesActionPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 12),
    _RlPolicyRulesActionPointer_Type()
)
rlPolicyRulesActionPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesActionPointer.setStatus("current")


class _RlPolicyRulesTimeRange1_Type(Integer32):
    """Custom type rlPolicyRulesTimeRange1 based on Integer32"""
    defaultValue = 0


_RlPolicyRulesTimeRange1_Object = MibTableColumn
rlPolicyRulesTimeRange1 = _RlPolicyRulesTimeRange1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 13),
    _RlPolicyRulesTimeRange1_Type()
)
rlPolicyRulesTimeRange1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesTimeRange1.setStatus("current")


class _RlPolicyRulesTimeRange2_Type(Integer32):
    """Custom type rlPolicyRulesTimeRange2 based on Integer32"""
    defaultValue = 0


_RlPolicyRulesTimeRange2_Object = MibTableColumn
rlPolicyRulesTimeRange2 = _RlPolicyRulesTimeRange2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 2, 1, 14),
    _RlPolicyRulesTimeRange2_Type()
)
rlPolicyRulesTimeRange2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesTimeRange2.setStatus("current")


class _RlPolicyRulesDownloadMarker_Type(Integer32):
    """Custom type rlPolicyRulesDownloadMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("finish", 2),
          ("start", 1))
    )


_RlPolicyRulesDownloadMarker_Type.__name__ = "Integer32"
_RlPolicyRulesDownloadMarker_Object = MibScalar
rlPolicyRulesDownloadMarker = _RlPolicyRulesDownloadMarker_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 3, 3),
    _RlPolicyRulesDownloadMarker_Type()
)
rlPolicyRulesDownloadMarker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRulesDownloadMarker.setStatus("current")
_RlPolicyMeterClass_ObjectIdentity = ObjectIdentity
rlPolicyMeterClass = _RlPolicyMeterClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4)
)
_RlPolicyMeterPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyMeterPlatDependParams = _RlPolicyMeterPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 1)
)
_RlPolicyMeterDepth_Type = Integer32
_RlPolicyMeterDepth_Object = MibScalar
rlPolicyMeterDepth = _RlPolicyMeterDepth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 1, 1),
    _RlPolicyMeterDepth_Type()
)
rlPolicyMeterDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMeterDepth.setStatus("current")
_RlPolicyMeterClassTable_Object = MibTable
rlPolicyMeterClassTable = _RlPolicyMeterClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2)
)
if mibBuilder.loadTexts:
    rlPolicyMeterClassTable.setStatus("current")
_RlPolicyMeteringClassEntry_Object = MibTableRow
rlPolicyMeteringClassEntry = _RlPolicyMeteringClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1)
)
rlPolicyMeteringClassEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyMeteringClassIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyMeteringClassEntry.setStatus("current")


class _RlPolicyMeteringClassIndex_Type(Integer32):
    """Custom type rlPolicyMeteringClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicyMeteringClassIndex_Type.__name__ = "Integer32"
_RlPolicyMeteringClassIndex_Object = MibTableColumn
rlPolicyMeteringClassIndex = _RlPolicyMeteringClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 1),
    _RlPolicyMeteringClassIndex_Type()
)
rlPolicyMeteringClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassIndex.setStatus("current")


class _RlPolicyMeteringClassAlwaysConform_Type(TruthValue):
    """Custom type rlPolicyMeteringClassAlwaysConform based on TruthValue"""


_RlPolicyMeteringClassAlwaysConform_Object = MibTableColumn
rlPolicyMeteringClassAlwaysConform = _RlPolicyMeteringClassAlwaysConform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 2),
    _RlPolicyMeteringClassAlwaysConform_Type()
)
rlPolicyMeteringClassAlwaysConform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassAlwaysConform.setStatus("current")


class _RlPolicyMeteringClassAggregateMeterRate_Type(Integer32):
    """Custom type rlPolicyMeteringClassAggregateMeterRate based on Integer32"""
    defaultValue = 0


_RlPolicyMeteringClassAggregateMeterRate_Object = MibTableColumn
rlPolicyMeteringClassAggregateMeterRate = _RlPolicyMeteringClassAggregateMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 3),
    _RlPolicyMeteringClassAggregateMeterRate_Type()
)
rlPolicyMeteringClassAggregateMeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassAggregateMeterRate.setStatus("current")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassAggregateMeterRate.setUnits("kbps")


class _RlPolicyMeteringClassAggregateMeterBurstSize_Type(Integer32):
    """Custom type rlPolicyMeteringClassAggregateMeterBurstSize based on Integer32"""
    defaultValue = 0


_RlPolicyMeteringClassAggregateMeterBurstSize_Object = MibTableColumn
rlPolicyMeteringClassAggregateMeterBurstSize = _RlPolicyMeteringClassAggregateMeterBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 4),
    _RlPolicyMeteringClassAggregateMeterBurstSize_Type()
)
rlPolicyMeteringClassAggregateMeterBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassAggregateMeterBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassAggregateMeterBurstSize.setUnits("bytes")


class _RlPolicyMeteringClassPerSessionMeteringRate_Type(Integer32):
    """Custom type rlPolicyMeteringClassPerSessionMeteringRate based on Integer32"""
    defaultValue = 0


_RlPolicyMeteringClassPerSessionMeteringRate_Object = MibTableColumn
rlPolicyMeteringClassPerSessionMeteringRate = _RlPolicyMeteringClassPerSessionMeteringRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 5),
    _RlPolicyMeteringClassPerSessionMeteringRate_Type()
)
rlPolicyMeteringClassPerSessionMeteringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassPerSessionMeteringRate.setStatus("current")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassPerSessionMeteringRate.setUnits("kbps")


class _RlPolicyMeteringClassMaxSessionLimit_Type(Integer32):
    """Custom type rlPolicyMeteringClassMaxSessionLimit based on Integer32"""
    defaultValue = 0


_RlPolicyMeteringClassMaxSessionLimit_Object = MibTableColumn
rlPolicyMeteringClassMaxSessionLimit = _RlPolicyMeteringClassMaxSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 6),
    _RlPolicyMeteringClassMaxSessionLimit_Type()
)
rlPolicyMeteringClassMaxSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassMaxSessionLimit.setStatus("current")
_RlPolicyMeteringClassActionPointer_Type = Integer32
_RlPolicyMeteringClassActionPointer_Object = MibTableColumn
rlPolicyMeteringClassActionPointer = _RlPolicyMeteringClassActionPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 7),
    _RlPolicyMeteringClassActionPointer_Type()
)
rlPolicyMeteringClassActionPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassActionPointer.setStatus("current")


class _RlPolicyMeteringClassFailMeterPointer_Type(Integer32):
    """Custom type rlPolicyMeteringClassFailMeterPointer based on Integer32"""
    defaultValue = 0


_RlPolicyMeteringClassFailMeterPointer_Object = MibTableColumn
rlPolicyMeteringClassFailMeterPointer = _RlPolicyMeteringClassFailMeterPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 8),
    _RlPolicyMeteringClassFailMeterPointer_Type()
)
rlPolicyMeteringClassFailMeterPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassFailMeterPointer.setStatus("current")
_RlPolicyMeteringClassStatus_Type = RowStatus
_RlPolicyMeteringClassStatus_Object = MibTableColumn
rlPolicyMeteringClassStatus = _RlPolicyMeteringClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 9),
    _RlPolicyMeteringClassStatus_Type()
)
rlPolicyMeteringClassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassStatus.setStatus("current")


class _RlPolicyMeteringCounterEnable_Type(TruthValue):
    """Custom type rlPolicyMeteringCounterEnable based on TruthValue"""


_RlPolicyMeteringCounterEnable_Object = MibTableColumn
rlPolicyMeteringCounterEnable = _RlPolicyMeteringCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 10),
    _RlPolicyMeteringCounterEnable_Type()
)
rlPolicyMeteringCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMeteringCounterEnable.setStatus("current")
_RlPolicyMeteringClassInProfileCounter_Type = Counter32
_RlPolicyMeteringClassInProfileCounter_Object = MibTableColumn
rlPolicyMeteringClassInProfileCounter = _RlPolicyMeteringClassInProfileCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 11),
    _RlPolicyMeteringClassInProfileCounter_Type()
)
rlPolicyMeteringClassInProfileCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassInProfileCounter.setStatus("current")
_RlPolicyMeteringClassOutProfileCounter_Type = Counter32
_RlPolicyMeteringClassOutProfileCounter_Object = MibTableColumn
rlPolicyMeteringClassOutProfileCounter = _RlPolicyMeteringClassOutProfileCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 4, 2, 1, 12),
    _RlPolicyMeteringClassOutProfileCounter_Type()
)
rlPolicyMeteringClassOutProfileCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyMeteringClassOutProfileCounter.setStatus("current")
_RlPolicyAction_ObjectIdentity = ObjectIdentity
rlPolicyAction = _RlPolicyAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5)
)
_RlPolicyActionPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyActionPlatDependParams = _RlPolicyActionPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1)
)


class _RlPolicyActionMREDSupported_Type(Integer32):
    """Custom type rlPolicyActionMREDSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlPolicyActionMREDSupported_Type.__name__ = "Integer32"
_RlPolicyActionMREDSupported_Object = MibScalar
rlPolicyActionMREDSupported = _RlPolicyActionMREDSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 1),
    _RlPolicyActionMREDSupported_Type()
)
rlPolicyActionMREDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionMREDSupported.setStatus("current")
_RlPolicyActionDroppedPacketCountSupported_Type = TruthValue
_RlPolicyActionDroppedPacketCountSupported_Object = MibScalar
rlPolicyActionDroppedPacketCountSupported = _RlPolicyActionDroppedPacketCountSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 2),
    _RlPolicyActionDroppedPacketCountSupported_Type()
)
rlPolicyActionDroppedPacketCountSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionDroppedPacketCountSupported.setStatus("current")
_RlPolicyActionDroppedDropPrecedenceSupported_Type = TruthValue
_RlPolicyActionDroppedDropPrecedenceSupported_Object = MibScalar
rlPolicyActionDroppedDropPrecedenceSupported = _RlPolicyActionDroppedDropPrecedenceSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 3),
    _RlPolicyActionDroppedDropPrecedenceSupported_Type()
)
rlPolicyActionDroppedDropPrecedenceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionDroppedDropPrecedenceSupported.setStatus("current")


class _RlPolicyActionInProfileDropPrecedence_Type(OctetString):
    """Custom type rlPolicyActionInProfileDropPrecedence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyActionInProfileDropPrecedence_Type.__name__ = "OctetString"
_RlPolicyActionInProfileDropPrecedence_Object = MibScalar
rlPolicyActionInProfileDropPrecedence = _RlPolicyActionInProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 4),
    _RlPolicyActionInProfileDropPrecedence_Type()
)
rlPolicyActionInProfileDropPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionInProfileDropPrecedence.setStatus("current")


class _RlPolicyActionOutProfileDropPrecedence_Type(OctetString):
    """Custom type rlPolicyActionOutProfileDropPrecedence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicyActionOutProfileDropPrecedence_Type.__name__ = "OctetString"
_RlPolicyActionOutProfileDropPrecedence_Object = MibScalar
rlPolicyActionOutProfileDropPrecedence = _RlPolicyActionOutProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 5),
    _RlPolicyActionOutProfileDropPrecedence_Type()
)
rlPolicyActionOutProfileDropPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionOutProfileDropPrecedence.setStatus("current")
_RlPolicyActionDscpSupport_Type = TruthValue
_RlPolicyActionDscpSupport_Object = MibScalar
rlPolicyActionDscpSupport = _RlPolicyActionDscpSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 6),
    _RlPolicyActionDscpSupport_Type()
)
rlPolicyActionDscpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionDscpSupport.setStatus("current")


class _RlPolicyActionDsQueueManagmentSupported_Type(Integer32):
    """Custom type rlPolicyActionDsQueueManagmentSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlPolicyActionDsQueueManagmentSupported_Type.__name__ = "Integer32"
_RlPolicyActionDsQueueManagmentSupported_Object = MibScalar
rlPolicyActionDsQueueManagmentSupported = _RlPolicyActionDsQueueManagmentSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 1, 7),
    _RlPolicyActionDsQueueManagmentSupported_Type()
)
rlPolicyActionDsQueueManagmentSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionDsQueueManagmentSupported.setStatus("current")
_RlPolicyActionTable_Object = MibTable
rlPolicyActionTable = _RlPolicyActionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2)
)
if mibBuilder.loadTexts:
    rlPolicyActionTable.setStatus("current")
_RlPolicyActionEntry_Object = MibTableRow
rlPolicyActionEntry = _RlPolicyActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1)
)
rlPolicyActionEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyActionIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyActionEntry.setStatus("current")


class _RlPolicyActionIndex_Type(Integer32):
    """Custom type rlPolicyActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicyActionIndex_Type.__name__ = "Integer32"
_RlPolicyActionIndex_Object = MibTableColumn
rlPolicyActionIndex = _RlPolicyActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 1),
    _RlPolicyActionIndex_Type()
)
rlPolicyActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionIndex.setStatus("current")


class _RlPolicyActionNewDscp_Type(Integer32):
    """Custom type rlPolicyActionNewDscp based on Integer32"""
    defaultValue = 0


_RlPolicyActionNewDscp_Object = MibTableColumn
rlPolicyActionNewDscp = _RlPolicyActionNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 2),
    _RlPolicyActionNewDscp_Type()
)
rlPolicyActionNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNewDscp.setStatus("current")


class _RlPolicyActionChangeDscp_Type(TruthValue):
    """Custom type rlPolicyActionChangeDscp based on TruthValue"""


_RlPolicyActionChangeDscp_Object = MibTableColumn
rlPolicyActionChangeDscp = _RlPolicyActionChangeDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 3),
    _RlPolicyActionChangeDscp_Type()
)
rlPolicyActionChangeDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeDscp.setStatus("current")


class _RlPolicyActionMinThreshold_Type(Integer32):
    """Custom type rlPolicyActionMinThreshold based on Integer32"""
    defaultValue = 0


_RlPolicyActionMinThreshold_Object = MibTableColumn
rlPolicyActionMinThreshold = _RlPolicyActionMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 4),
    _RlPolicyActionMinThreshold_Type()
)
rlPolicyActionMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionMinThreshold.setStatus("current")


class _RlPolicyActionMaxThreshold_Type(Integer32):
    """Custom type rlPolicyActionMaxThreshold based on Integer32"""
    defaultValue = 0


_RlPolicyActionMaxThreshold_Object = MibTableColumn
rlPolicyActionMaxThreshold = _RlPolicyActionMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 5),
    _RlPolicyActionMaxThreshold_Type()
)
rlPolicyActionMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionMaxThreshold.setStatus("current")


class _RlPolicyActionDropPolicy_Type(Integer32):
    """Custom type rlPolicyActionDropPolicy based on Integer32"""
    defaultValue = 1

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
        *(("alwaysDrop", 2),
          ("other", 1),
          ("randomDrop", 4),
          ("tailDrop", 3))
    )


_RlPolicyActionDropPolicy_Type.__name__ = "Integer32"
_RlPolicyActionDropPolicy_Object = MibTableColumn
rlPolicyActionDropPolicy = _RlPolicyActionDropPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 6),
    _RlPolicyActionDropPolicy_Type()
)
rlPolicyActionDropPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionDropPolicy.setStatus("current")
_RlPolicyActionDroppedPackets_Type = Counter32
_RlPolicyActionDroppedPackets_Object = MibTableColumn
rlPolicyActionDroppedPackets = _RlPolicyActionDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 7),
    _RlPolicyActionDroppedPackets_Type()
)
rlPolicyActionDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyActionDroppedPackets.setStatus("current")


class _RlPolicyActionNonDsInProfileDropPrecedence_Type(Integer32):
    """Custom type rlPolicyActionNonDsInProfileDropPrecedence based on Integer32"""
    defaultValue = 1

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
        *(("drop", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlPolicyActionNonDsInProfileDropPrecedence_Type.__name__ = "Integer32"
_RlPolicyActionNonDsInProfileDropPrecedence_Object = MibTableColumn
rlPolicyActionNonDsInProfileDropPrecedence = _RlPolicyActionNonDsInProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 8),
    _RlPolicyActionNonDsInProfileDropPrecedence_Type()
)
rlPolicyActionNonDsInProfileDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNonDsInProfileDropPrecedence.setStatus("current")


class _RlPolicyActionNonDsOutProfileDropPrecedence_Type(Integer32):
    """Custom type rlPolicyActionNonDsOutProfileDropPrecedence based on Integer32"""
    defaultValue = 1

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
        *(("drop", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlPolicyActionNonDsOutProfileDropPrecedence_Type.__name__ = "Integer32"
_RlPolicyActionNonDsOutProfileDropPrecedence_Object = MibTableColumn
rlPolicyActionNonDsOutProfileDropPrecedence = _RlPolicyActionNonDsOutProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 9),
    _RlPolicyActionNonDsOutProfileDropPrecedence_Type()
)
rlPolicyActionNonDsOutProfileDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNonDsOutProfileDropPrecedence.setStatus("current")


class _RlPolicyActionChangeVpt_Type(TruthValue):
    """Custom type rlPolicyActionChangeVpt based on TruthValue"""


_RlPolicyActionChangeVpt_Object = MibTableColumn
rlPolicyActionChangeVpt = _RlPolicyActionChangeVpt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 10),
    _RlPolicyActionChangeVpt_Type()
)
rlPolicyActionChangeVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeVpt.setStatus("current")


class _RlPolicyActionNewVpt_Type(Integer32):
    """Custom type rlPolicyActionNewVpt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyActionNewVpt_Type.__name__ = "Integer32"
_RlPolicyActionNewVpt_Object = MibTableColumn
rlPolicyActionNewVpt = _RlPolicyActionNewVpt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 11),
    _RlPolicyActionNewVpt_Type()
)
rlPolicyActionNewVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNewVpt.setStatus("current")
_RlPolicyActionServiceClassPointer_Type = Integer32
_RlPolicyActionServiceClassPointer_Object = MibTableColumn
rlPolicyActionServiceClassPointer = _RlPolicyActionServiceClassPointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 12),
    _RlPolicyActionServiceClassPointer_Type()
)
rlPolicyActionServiceClassPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionServiceClassPointer.setStatus("current")
_RlPolicyActionStatus_Type = RowStatus
_RlPolicyActionStatus_Object = MibTableColumn
rlPolicyActionStatus = _RlPolicyActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 13),
    _RlPolicyActionStatus_Type()
)
rlPolicyActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionStatus.setStatus("current")


class _RlPolicyActionChangeDscpNonConform_Type(TruthValue):
    """Custom type rlPolicyActionChangeDscpNonConform based on TruthValue"""


_RlPolicyActionChangeDscpNonConform_Object = MibTableColumn
rlPolicyActionChangeDscpNonConform = _RlPolicyActionChangeDscpNonConform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 14),
    _RlPolicyActionChangeDscpNonConform_Type()
)
rlPolicyActionChangeDscpNonConform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeDscpNonConform.setStatus("current")


class _RlPolicyActionChangeNewDscpNonConform_Type(Integer32):
    """Custom type rlPolicyActionChangeNewDscpNonConform based on Integer32"""
    defaultValue = 0


_RlPolicyActionChangeNewDscpNonConform_Object = MibTableColumn
rlPolicyActionChangeNewDscpNonConform = _RlPolicyActionChangeNewDscpNonConform_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 15),
    _RlPolicyActionChangeNewDscpNonConform_Type()
)
rlPolicyActionChangeNewDscpNonConform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeNewDscpNonConform.setStatus("current")


class _RlPolicyActionAdvancedTrustMode_Type(RlPolicyTrustTypes):
    """Custom type rlPolicyActionAdvancedTrustMode based on RlPolicyTrustTypes"""


_RlPolicyActionAdvancedTrustMode_Object = MibTableColumn
rlPolicyActionAdvancedTrustMode = _RlPolicyActionAdvancedTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 16),
    _RlPolicyActionAdvancedTrustMode_Type()
)
rlPolicyActionAdvancedTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionAdvancedTrustMode.setStatus("current")


class _RlPolicyActionNewIpPrecedence_Type(Integer32):
    """Custom type rlPolicyActionNewIpPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyActionNewIpPrecedence_Type.__name__ = "Integer32"
_RlPolicyActionNewIpPrecedence_Object = MibTableColumn
rlPolicyActionNewIpPrecedence = _RlPolicyActionNewIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 17),
    _RlPolicyActionNewIpPrecedence_Type()
)
rlPolicyActionNewIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNewIpPrecedence.setStatus("current")


class _RlPolicyActionChangeIpPrecedence_Type(TruthValue):
    """Custom type rlPolicyActionChangeIpPrecedence based on TruthValue"""


_RlPolicyActionChangeIpPrecedence_Object = MibTableColumn
rlPolicyActionChangeIpPrecedence = _RlPolicyActionChangeIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 18),
    _RlPolicyActionChangeIpPrecedence_Type()
)
rlPolicyActionChangeIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeIpPrecedence.setStatus("current")


class _RlPolicyActionReDirect_Type(Integer32):
    """Custom type rlPolicyActionReDirect based on Integer32"""
    defaultValue = 0


_RlPolicyActionReDirect_Object = MibTableColumn
rlPolicyActionReDirect = _RlPolicyActionReDirect_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 19),
    _RlPolicyActionReDirect_Type()
)
rlPolicyActionReDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionReDirect.setStatus("current")


class _RlPolicyActionCopyPort_Type(Integer32):
    """Custom type rlPolicyActionCopyPort based on Integer32"""
    defaultValue = 0


_RlPolicyActionCopyPort_Object = MibTableColumn
rlPolicyActionCopyPort = _RlPolicyActionCopyPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 20),
    _RlPolicyActionCopyPort_Type()
)
rlPolicyActionCopyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionCopyPort.setStatus("current")


class _RlPolicyActionChangeVid_Type(TruthValue):
    """Custom type rlPolicyActionChangeVid based on TruthValue"""


_RlPolicyActionChangeVid_Object = MibTableColumn
rlPolicyActionChangeVid = _RlPolicyActionChangeVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 21),
    _RlPolicyActionChangeVid_Type()
)
rlPolicyActionChangeVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionChangeVid.setStatus("current")


class _RlPolicyActionNewVid_Type(Integer32):
    """Custom type rlPolicyActionNewVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlPolicyActionNewVid_Type.__name__ = "Integer32"
_RlPolicyActionNewVid_Object = MibTableColumn
rlPolicyActionNewVid = _RlPolicyActionNewVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 5, 2, 1, 22),
    _RlPolicyActionNewVid_Type()
)
rlPolicyActionNewVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActionNewVid.setStatus("current")
_RlPolicyServiceClass_ObjectIdentity = ObjectIdentity
rlPolicyServiceClass = _RlPolicyServiceClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6)
)
_RlPolicyServiceClassPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyServiceClassPlatDependParams = _RlPolicyServiceClassPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 1)
)
_RlPolicyNumberOfServiceClassesSupported_Type = Integer32
_RlPolicyNumberOfServiceClassesSupported_Object = MibScalar
rlPolicyNumberOfServiceClassesSupported = _RlPolicyNumberOfServiceClassesSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 1, 1),
    _RlPolicyNumberOfServiceClassesSupported_Type()
)
rlPolicyNumberOfServiceClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyNumberOfServiceClassesSupported.setStatus("current")


class _RlPolicyBoundedPriorityQueueSupport_Type(Integer32):
    """Custom type rlPolicyBoundedPriorityQueueSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlPolicyBoundedPriorityQueueSupport_Type.__name__ = "Integer32"
_RlPolicyBoundedPriorityQueueSupport_Object = MibScalar
rlPolicyBoundedPriorityQueueSupport = _RlPolicyBoundedPriorityQueueSupport_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 1, 2),
    _RlPolicyBoundedPriorityQueueSupport_Type()
)
rlPolicyBoundedPriorityQueueSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyBoundedPriorityQueueSupport.setStatus("current")
_RlPolicyDefaultServiceClass_Type = Integer32
_RlPolicyDefaultServiceClass_Object = MibScalar
rlPolicyDefaultServiceClass = _RlPolicyDefaultServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 2),
    _RlPolicyDefaultServiceClass_Type()
)
rlPolicyDefaultServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultServiceClass.setStatus("current")


class _RlPolicyActiveServiceClassTable_Type(Integer32):
    """Custom type rlPolicyActiveServiceClassTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_RlPolicyActiveServiceClassTable_Type.__name__ = "Integer32"
_RlPolicyActiveServiceClassTable_Object = MibScalar
rlPolicyActiveServiceClassTable = _RlPolicyActiveServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 3),
    _RlPolicyActiveServiceClassTable_Type()
)
rlPolicyActiveServiceClassTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyActiveServiceClassTable.setStatus("current")
_RlPolicyServiceClassTentativeTable_Object = MibTable
rlPolicyServiceClassTentativeTable = _RlPolicyServiceClassTentativeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4)
)
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeTable.setStatus("current")
_RlPolicyServiceClassTentativeEntry_Object = MibTableRow
rlPolicyServiceClassTentativeEntry = _RlPolicyServiceClassTentativeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1)
)
rlPolicyServiceClassTentativeEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyServiceClassTentativeIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeEntry.setStatus("current")
_RlPolicyServiceClassTentativeIndex_Type = Integer32
_RlPolicyServiceClassTentativeIndex_Object = MibTableColumn
rlPolicyServiceClassTentativeIndex = _RlPolicyServiceClassTentativeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 1),
    _RlPolicyServiceClassTentativeIndex_Type()
)
rlPolicyServiceClassTentativeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeIndex.setStatus("current")


class _RlPolicyServiceClassTentativeName_Type(DisplayString):
    """Custom type rlPolicyServiceClassTentativeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPolicyServiceClassTentativeName_Type.__name__ = "DisplayString"
_RlPolicyServiceClassTentativeName_Object = MibTableColumn
rlPolicyServiceClassTentativeName = _RlPolicyServiceClassTentativeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 2),
    _RlPolicyServiceClassTentativeName_Type()
)
rlPolicyServiceClassTentativeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeName.setStatus("current")


class _RlPolicyServiceClassTentativePhbType_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativePhbType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assuredForwarding", 2),
          ("bestEffort", 3),
          ("expeditedForwarding", 1))
    )


_RlPolicyServiceClassTentativePhbType_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativePhbType_Object = MibTableColumn
rlPolicyServiceClassTentativePhbType = _RlPolicyServiceClassTentativePhbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 3),
    _RlPolicyServiceClassTentativePhbType_Type()
)
rlPolicyServiceClassTentativePhbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativePhbType.setStatus("current")
_RlPolicyServiceClassTentativeMinRate_Type = Integer32
_RlPolicyServiceClassTentativeMinRate_Object = MibTableColumn
rlPolicyServiceClassTentativeMinRate = _RlPolicyServiceClassTentativeMinRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 4),
    _RlPolicyServiceClassTentativeMinRate_Type()
)
rlPolicyServiceClassTentativeMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeMinRate.setStatus("current")
_RlPolicyServiceClassTentativeMaxRate_Type = Integer32
_RlPolicyServiceClassTentativeMaxRate_Object = MibTableColumn
rlPolicyServiceClassTentativeMaxRate = _RlPolicyServiceClassTentativeMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 5),
    _RlPolicyServiceClassTentativeMaxRate_Type()
)
rlPolicyServiceClassTentativeMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeMaxRate.setStatus("current")
_RlPolicyServiceClassTentativePriority_Type = Integer32
_RlPolicyServiceClassTentativePriority_Object = MibTableColumn
rlPolicyServiceClassTentativePriority = _RlPolicyServiceClassTentativePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 6),
    _RlPolicyServiceClassTentativePriority_Type()
)
rlPolicyServiceClassTentativePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativePriority.setStatus("current")


class _RlPolicyServiceClassTentative8021DPri_Type(Integer32):
    """Custom type rlPolicyServiceClassTentative8021DPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyServiceClassTentative8021DPri_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentative8021DPri_Object = MibTableColumn
rlPolicyServiceClassTentative8021DPri = _RlPolicyServiceClassTentative8021DPri_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 7),
    _RlPolicyServiceClassTentative8021DPri_Type()
)
rlPolicyServiceClassTentative8021DPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentative8021DPri.setStatus("current")
_RlPolicyServiceClassTentativeStatus_Type = RowStatus
_RlPolicyServiceClassTentativeStatus_Object = MibTableColumn
rlPolicyServiceClassTentativeStatus = _RlPolicyServiceClassTentativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 8),
    _RlPolicyServiceClassTentativeStatus_Type()
)
rlPolicyServiceClassTentativeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeStatus.setStatus("current")


class _RlPolicyServiceClassTentativeTdThersholdDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeTdThersholdDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeTdThersholdDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeTdThersholdDp0_Object = MibTableColumn
rlPolicyServiceClassTentativeTdThersholdDp0 = _RlPolicyServiceClassTentativeTdThersholdDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 9),
    _RlPolicyServiceClassTentativeTdThersholdDp0_Type()
)
rlPolicyServiceClassTentativeTdThersholdDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeTdThersholdDp0.setStatus("current")


class _RlPolicyServiceClassTentativeTdThersholdDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeTdThersholdDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeTdThersholdDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeTdThersholdDp1_Object = MibTableColumn
rlPolicyServiceClassTentativeTdThersholdDp1 = _RlPolicyServiceClassTentativeTdThersholdDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 10),
    _RlPolicyServiceClassTentativeTdThersholdDp1_Type()
)
rlPolicyServiceClassTentativeTdThersholdDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeTdThersholdDp1.setStatus("current")


class _RlPolicyServiceClassTentativeTdThersholdDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeTdThersholdDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeTdThersholdDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeTdThersholdDp2_Object = MibTableColumn
rlPolicyServiceClassTentativeTdThersholdDp2 = _RlPolicyServiceClassTentativeTdThersholdDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 11),
    _RlPolicyServiceClassTentativeTdThersholdDp2_Type()
)
rlPolicyServiceClassTentativeTdThersholdDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeTdThersholdDp2.setStatus("current")


class _RlPolicyServiceClassTentativeRedMinDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMinDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMinDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMinDp0_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMinDp0 = _RlPolicyServiceClassTentativeRedMinDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 12),
    _RlPolicyServiceClassTentativeRedMinDp0_Type()
)
rlPolicyServiceClassTentativeRedMinDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMinDp0.setStatus("current")


class _RlPolicyServiceClassTentativeRedMaxDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMaxDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMaxDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMaxDp0_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMaxDp0 = _RlPolicyServiceClassTentativeRedMaxDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 13),
    _RlPolicyServiceClassTentativeRedMaxDp0_Type()
)
rlPolicyServiceClassTentativeRedMaxDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMaxDp0.setStatus("current")
_RlPolicyServiceClassTentativeRedProbDp0_Type = Integer32
_RlPolicyServiceClassTentativeRedProbDp0_Object = MibTableColumn
rlPolicyServiceClassTentativeRedProbDp0 = _RlPolicyServiceClassTentativeRedProbDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 14),
    _RlPolicyServiceClassTentativeRedProbDp0_Type()
)
rlPolicyServiceClassTentativeRedProbDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedProbDp0.setStatus("current")


class _RlPolicyServiceClassTentativeRedMinDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMinDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMinDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMinDp1_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMinDp1 = _RlPolicyServiceClassTentativeRedMinDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 15),
    _RlPolicyServiceClassTentativeRedMinDp1_Type()
)
rlPolicyServiceClassTentativeRedMinDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMinDp1.setStatus("current")


class _RlPolicyServiceClassTentativeRedMaxDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMaxDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMaxDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMaxDp1_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMaxDp1 = _RlPolicyServiceClassTentativeRedMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 16),
    _RlPolicyServiceClassTentativeRedMaxDp1_Type()
)
rlPolicyServiceClassTentativeRedMaxDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMaxDp1.setStatus("current")
_RlPolicyServiceClassTentativeRedProbDp1_Type = Integer32
_RlPolicyServiceClassTentativeRedProbDp1_Object = MibTableColumn
rlPolicyServiceClassTentativeRedProbDp1 = _RlPolicyServiceClassTentativeRedProbDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 17),
    _RlPolicyServiceClassTentativeRedProbDp1_Type()
)
rlPolicyServiceClassTentativeRedProbDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedProbDp1.setStatus("current")


class _RlPolicyServiceClassTentativeRedMinDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMinDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMinDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMinDp2_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMinDp2 = _RlPolicyServiceClassTentativeRedMinDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 18),
    _RlPolicyServiceClassTentativeRedMinDp2_Type()
)
rlPolicyServiceClassTentativeRedMinDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMinDp2.setStatus("current")


class _RlPolicyServiceClassTentativeRedMaxDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassTentativeRedMaxDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassTentativeRedMaxDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassTentativeRedMaxDp2_Object = MibTableColumn
rlPolicyServiceClassTentativeRedMaxDp2 = _RlPolicyServiceClassTentativeRedMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 19),
    _RlPolicyServiceClassTentativeRedMaxDp2_Type()
)
rlPolicyServiceClassTentativeRedMaxDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedMaxDp2.setStatus("current")
_RlPolicyServiceClassTentativeRedProbDp2_Type = Integer32
_RlPolicyServiceClassTentativeRedProbDp2_Object = MibTableColumn
rlPolicyServiceClassTentativeRedProbDp2 = _RlPolicyServiceClassTentativeRedProbDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 20),
    _RlPolicyServiceClassTentativeRedProbDp2_Type()
)
rlPolicyServiceClassTentativeRedProbDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedProbDp2.setStatus("current")
_RlPolicyServiceClassTentativeRedQweight_Type = Integer32
_RlPolicyServiceClassTentativeRedQweight_Object = MibTableColumn
rlPolicyServiceClassTentativeRedQweight = _RlPolicyServiceClassTentativeRedQweight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 21),
    _RlPolicyServiceClassTentativeRedQweight_Type()
)
rlPolicyServiceClassTentativeRedQweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeRedQweight.setStatus("current")
_RlPolicyServiceClassTentativeShaperStatus_Type = TruthValue
_RlPolicyServiceClassTentativeShaperStatus_Object = MibTableColumn
rlPolicyServiceClassTentativeShaperStatus = _RlPolicyServiceClassTentativeShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 22),
    _RlPolicyServiceClassTentativeShaperStatus_Type()
)
rlPolicyServiceClassTentativeShaperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeShaperStatus.setStatus("current")
_RlPolicyServiceClassTentativeCirQueueShaper_Type = Integer32
_RlPolicyServiceClassTentativeCirQueueShaper_Object = MibTableColumn
rlPolicyServiceClassTentativeCirQueueShaper = _RlPolicyServiceClassTentativeCirQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 23),
    _RlPolicyServiceClassTentativeCirQueueShaper_Type()
)
rlPolicyServiceClassTentativeCirQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeCirQueueShaper.setStatus("current")
_RlPolicyServiceClassTentativeCbsQueueShaper_Type = Integer32
_RlPolicyServiceClassTentativeCbsQueueShaper_Object = MibTableColumn
rlPolicyServiceClassTentativeCbsQueueShaper = _RlPolicyServiceClassTentativeCbsQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 4, 1, 24),
    _RlPolicyServiceClassTentativeCbsQueueShaper_Type()
)
rlPolicyServiceClassTentativeCbsQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassTentativeCbsQueueShaper.setStatus("current")
_RlPolicyServiceClassActiveTable_Object = MibTable
rlPolicyServiceClassActiveTable = _RlPolicyServiceClassActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5)
)
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveTable.setStatus("current")
_RlPolicyServiceClassActiveEntry_Object = MibTableRow
rlPolicyServiceClassActiveEntry = _RlPolicyServiceClassActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1)
)
rlPolicyServiceClassActiveEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyServiceClassActiveIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveEntry.setStatus("current")
_RlPolicyServiceClassActiveIndex_Type = Integer32
_RlPolicyServiceClassActiveIndex_Object = MibTableColumn
rlPolicyServiceClassActiveIndex = _RlPolicyServiceClassActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 1),
    _RlPolicyServiceClassActiveIndex_Type()
)
rlPolicyServiceClassActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveIndex.setStatus("current")


class _RlPolicyServiceClassActiveName_Type(DisplayString):
    """Custom type rlPolicyServiceClassActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPolicyServiceClassActiveName_Type.__name__ = "DisplayString"
_RlPolicyServiceClassActiveName_Object = MibTableColumn
rlPolicyServiceClassActiveName = _RlPolicyServiceClassActiveName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 2),
    _RlPolicyServiceClassActiveName_Type()
)
rlPolicyServiceClassActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveName.setStatus("current")


class _RlPolicyServiceClassActivePhbType_Type(Integer32):
    """Custom type rlPolicyServiceClassActivePhbType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assuredForwarding", 2),
          ("bestEffort", 3),
          ("expeditedForwarding", 1))
    )


_RlPolicyServiceClassActivePhbType_Type.__name__ = "Integer32"
_RlPolicyServiceClassActivePhbType_Object = MibTableColumn
rlPolicyServiceClassActivePhbType = _RlPolicyServiceClassActivePhbType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 3),
    _RlPolicyServiceClassActivePhbType_Type()
)
rlPolicyServiceClassActivePhbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActivePhbType.setStatus("current")
_RlPolicyServiceClassActiveMinRate_Type = Integer32
_RlPolicyServiceClassActiveMinRate_Object = MibTableColumn
rlPolicyServiceClassActiveMinRate = _RlPolicyServiceClassActiveMinRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 4),
    _RlPolicyServiceClassActiveMinRate_Type()
)
rlPolicyServiceClassActiveMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveMinRate.setStatus("current")
_RlPolicyServiceClassActiveMaxRate_Type = Integer32
_RlPolicyServiceClassActiveMaxRate_Object = MibTableColumn
rlPolicyServiceClassActiveMaxRate = _RlPolicyServiceClassActiveMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 5),
    _RlPolicyServiceClassActiveMaxRate_Type()
)
rlPolicyServiceClassActiveMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveMaxRate.setStatus("current")
_RlPolicyServiceClassActivePriority_Type = Integer32
_RlPolicyServiceClassActivePriority_Object = MibTableColumn
rlPolicyServiceClassActivePriority = _RlPolicyServiceClassActivePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 6),
    _RlPolicyServiceClassActivePriority_Type()
)
rlPolicyServiceClassActivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActivePriority.setStatus("current")


class _RlPolicyServiceClassActive8021DPri_Type(Integer32):
    """Custom type rlPolicyServiceClassActive8021DPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyServiceClassActive8021DPri_Type.__name__ = "Integer32"
_RlPolicyServiceClassActive8021DPri_Object = MibTableColumn
rlPolicyServiceClassActive8021DPri = _RlPolicyServiceClassActive8021DPri_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 7),
    _RlPolicyServiceClassActive8021DPri_Type()
)
rlPolicyServiceClassActive8021DPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActive8021DPri.setStatus("current")


class _RlPolicyServiceClassActiveTdThersholdDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveTdThersholdDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveTdThersholdDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveTdThersholdDp0_Object = MibTableColumn
rlPolicyServiceClassActiveTdThersholdDp0 = _RlPolicyServiceClassActiveTdThersholdDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 8),
    _RlPolicyServiceClassActiveTdThersholdDp0_Type()
)
rlPolicyServiceClassActiveTdThersholdDp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveTdThersholdDp0.setStatus("current")


class _RlPolicyServiceClassActiveTdThersholdDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveTdThersholdDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveTdThersholdDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveTdThersholdDp1_Object = MibTableColumn
rlPolicyServiceClassActiveTdThersholdDp1 = _RlPolicyServiceClassActiveTdThersholdDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 9),
    _RlPolicyServiceClassActiveTdThersholdDp1_Type()
)
rlPolicyServiceClassActiveTdThersholdDp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveTdThersholdDp1.setStatus("current")


class _RlPolicyServiceClassActiveTdThersholdDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveTdThersholdDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveTdThersholdDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveTdThersholdDp2_Object = MibTableColumn
rlPolicyServiceClassActiveTdThersholdDp2 = _RlPolicyServiceClassActiveTdThersholdDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 10),
    _RlPolicyServiceClassActiveTdThersholdDp2_Type()
)
rlPolicyServiceClassActiveTdThersholdDp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveTdThersholdDp2.setStatus("current")


class _RlPolicyServiceClassActiveRedMinDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMinDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMinDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMinDp0_Object = MibTableColumn
rlPolicyServiceClassActiveRedMinDp0 = _RlPolicyServiceClassActiveRedMinDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 11),
    _RlPolicyServiceClassActiveRedMinDp0_Type()
)
rlPolicyServiceClassActiveRedMinDp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMinDp0.setStatus("current")


class _RlPolicyServiceClassActiveRedMaxDp0_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMaxDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMaxDp0_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMaxDp0_Object = MibTableColumn
rlPolicyServiceClassActiveRedMaxDp0 = _RlPolicyServiceClassActiveRedMaxDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 12),
    _RlPolicyServiceClassActiveRedMaxDp0_Type()
)
rlPolicyServiceClassActiveRedMaxDp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMaxDp0.setStatus("current")
_RlPolicyServiceClassActiveRedProbDp0_Type = Integer32
_RlPolicyServiceClassActiveRedProbDp0_Object = MibTableColumn
rlPolicyServiceClassActiveRedProbDp0 = _RlPolicyServiceClassActiveRedProbDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 13),
    _RlPolicyServiceClassActiveRedProbDp0_Type()
)
rlPolicyServiceClassActiveRedProbDp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedProbDp0.setStatus("current")


class _RlPolicyServiceClassActiveRedMinDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMinDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMinDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMinDp1_Object = MibTableColumn
rlPolicyServiceClassActiveRedMinDp1 = _RlPolicyServiceClassActiveRedMinDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 14),
    _RlPolicyServiceClassActiveRedMinDp1_Type()
)
rlPolicyServiceClassActiveRedMinDp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMinDp1.setStatus("current")


class _RlPolicyServiceClassActiveRedMaxDp1_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMaxDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMaxDp1_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMaxDp1_Object = MibTableColumn
rlPolicyServiceClassActiveRedMaxDp1 = _RlPolicyServiceClassActiveRedMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 15),
    _RlPolicyServiceClassActiveRedMaxDp1_Type()
)
rlPolicyServiceClassActiveRedMaxDp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMaxDp1.setStatus("current")
_RlPolicyServiceClassActiveRedProbDp1_Type = Integer32
_RlPolicyServiceClassActiveRedProbDp1_Object = MibTableColumn
rlPolicyServiceClassActiveRedProbDp1 = _RlPolicyServiceClassActiveRedProbDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 16),
    _RlPolicyServiceClassActiveRedProbDp1_Type()
)
rlPolicyServiceClassActiveRedProbDp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedProbDp1.setStatus("current")


class _RlPolicyServiceClassActiveRedMinDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMinDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMinDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMinDp2_Object = MibTableColumn
rlPolicyServiceClassActiveRedMinDp2 = _RlPolicyServiceClassActiveRedMinDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 17),
    _RlPolicyServiceClassActiveRedMinDp2_Type()
)
rlPolicyServiceClassActiveRedMinDp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMinDp2.setStatus("current")


class _RlPolicyServiceClassActiveRedMaxDp2_Type(Integer32):
    """Custom type rlPolicyServiceClassActiveRedMaxDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyServiceClassActiveRedMaxDp2_Type.__name__ = "Integer32"
_RlPolicyServiceClassActiveRedMaxDp2_Object = MibTableColumn
rlPolicyServiceClassActiveRedMaxDp2 = _RlPolicyServiceClassActiveRedMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 18),
    _RlPolicyServiceClassActiveRedMaxDp2_Type()
)
rlPolicyServiceClassActiveRedMaxDp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedMaxDp2.setStatus("current")
_RlPolicyServiceClassActiveRedProbDp2_Type = Integer32
_RlPolicyServiceClassActiveRedProbDp2_Object = MibTableColumn
rlPolicyServiceClassActiveRedProbDp2 = _RlPolicyServiceClassActiveRedProbDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 19),
    _RlPolicyServiceClassActiveRedProbDp2_Type()
)
rlPolicyServiceClassActiveRedProbDp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedProbDp2.setStatus("current")
_RlPolicyServiceClassActiveRedQweight_Type = Integer32
_RlPolicyServiceClassActiveRedQweight_Object = MibTableColumn
rlPolicyServiceClassActiveRedQweight = _RlPolicyServiceClassActiveRedQweight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 20),
    _RlPolicyServiceClassActiveRedQweight_Type()
)
rlPolicyServiceClassActiveRedQweight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveRedQweight.setStatus("current")
_RlPolicyServiceClassActiveShaperStatus_Type = TruthValue
_RlPolicyServiceClassActiveShaperStatus_Object = MibTableColumn
rlPolicyServiceClassActiveShaperStatus = _RlPolicyServiceClassActiveShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 21),
    _RlPolicyServiceClassActiveShaperStatus_Type()
)
rlPolicyServiceClassActiveShaperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveShaperStatus.setStatus("current")
_RlPolicyServiceClassActiveCirQueueShaper_Type = Integer32
_RlPolicyServiceClassActiveCirQueueShaper_Object = MibTableColumn
rlPolicyServiceClassActiveCirQueueShaper = _RlPolicyServiceClassActiveCirQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 22),
    _RlPolicyServiceClassActiveCirQueueShaper_Type()
)
rlPolicyServiceClassActiveCirQueueShaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveCirQueueShaper.setStatus("current")
_RlPolicyServiceClassActiveCbsQueueShaper_Type = Integer32
_RlPolicyServiceClassActiveCbsQueueShaper_Object = MibTableColumn
rlPolicyServiceClassActiveCbsQueueShaper = _RlPolicyServiceClassActiveCbsQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 5, 1, 23),
    _RlPolicyServiceClassActiveCbsQueueShaper_Type()
)
rlPolicyServiceClassActiveCbsQueueShaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyServiceClassActiveCbsQueueShaper.setStatus("current")
_RlPolicyPortConfigurationTable_Object = MibTable
rlPolicyPortConfigurationTable = _RlPolicyPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6)
)
if mibBuilder.loadTexts:
    rlPolicyPortConfigurationTable.setStatus("current")
_RlPolicyPortCfgEntry_Object = MibTableRow
rlPolicyPortCfgEntry = _RlPolicyPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1)
)
rlPolicyPortCfgEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyPortCfgEntry.setStatus("current")
_RlPolicyPortCfgIfIndex_Type = InterfaceIndex
_RlPolicyPortCfgIfIndex_Object = MibTableColumn
rlPolicyPortCfgIfIndex = _RlPolicyPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 1),
    _RlPolicyPortCfgIfIndex_Type()
)
rlPolicyPortCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyPortCfgIfIndex.setStatus("current")
_RlPolicyPortCfgMinimalBandwidth_Type = ObjectIdentifier
_RlPolicyPortCfgMinimalBandwidth_Object = MibTableColumn
rlPolicyPortCfgMinimalBandwidth = _RlPolicyPortCfgMinimalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 2),
    _RlPolicyPortCfgMinimalBandwidth_Type()
)
rlPolicyPortCfgMinimalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgMinimalBandwidth.setStatus("current")
_RlPolicyPortCfgMaximalBandwidth_Type = ObjectIdentifier
_RlPolicyPortCfgMaximalBandwidth_Object = MibTableColumn
rlPolicyPortCfgMaximalBandwidth = _RlPolicyPortCfgMaximalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 3),
    _RlPolicyPortCfgMaximalBandwidth_Type()
)
rlPolicyPortCfgMaximalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgMaximalBandwidth.setStatus("current")
_RlPolicyPortCfgStatus_Type = RowStatus
_RlPolicyPortCfgStatus_Object = MibTableColumn
rlPolicyPortCfgStatus = _RlPolicyPortCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 4),
    _RlPolicyPortCfgStatus_Type()
)
rlPolicyPortCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgStatus.setStatus("current")
_RlpolicyDropProfilePointer_Type = Integer32
_RlpolicyDropProfilePointer_Object = MibTableColumn
rlpolicyDropProfilePointer = _RlpolicyDropProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 5),
    _RlpolicyDropProfilePointer_Type()
)
rlpolicyDropProfilePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlpolicyDropProfilePointer.setStatus("current")
_RlPolicyPortCfgQueueShaperStatus_Type = ObjectIdentifier
_RlPolicyPortCfgQueueShaperStatus_Object = MibTableColumn
rlPolicyPortCfgQueueShaperStatus = _RlPolicyPortCfgQueueShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 6),
    _RlPolicyPortCfgQueueShaperStatus_Type()
)
rlPolicyPortCfgQueueShaperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgQueueShaperStatus.setStatus("current")
_RlPolicyPortCfgCirQueueShaper_Type = ObjectIdentifier
_RlPolicyPortCfgCirQueueShaper_Object = MibTableColumn
rlPolicyPortCfgCirQueueShaper = _RlPolicyPortCfgCirQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 7),
    _RlPolicyPortCfgCirQueueShaper_Type()
)
rlPolicyPortCfgCirQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCirQueueShaper.setStatus("current")
_RlPolicyPortCfgCbsQueueShaper_Type = ObjectIdentifier
_RlPolicyPortCfgCbsQueueShaper_Object = MibTableColumn
rlPolicyPortCfgCbsQueueShaper = _RlPolicyPortCfgCbsQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 8),
    _RlPolicyPortCfgCbsQueueShaper_Type()
)
rlPolicyPortCfgCbsQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCbsQueueShaper.setStatus("current")
_RlPolicyPortCfgPortShaperStatus_Type = TruthValue
_RlPolicyPortCfgPortShaperStatus_Object = MibTableColumn
rlPolicyPortCfgPortShaperStatus = _RlPolicyPortCfgPortShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 9),
    _RlPolicyPortCfgPortShaperStatus_Type()
)
rlPolicyPortCfgPortShaperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgPortShaperStatus.setStatus("current")
_RlPolicyPortCfgCirPortShaper_Type = Integer32
_RlPolicyPortCfgCirPortShaper_Object = MibTableColumn
rlPolicyPortCfgCirPortShaper = _RlPolicyPortCfgCirPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 10),
    _RlPolicyPortCfgCirPortShaper_Type()
)
rlPolicyPortCfgCirPortShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCirPortShaper.setStatus("current")
_RlPolicyPortCfgCbsPortShaper_Type = Integer32
_RlPolicyPortCfgCbsPortShaper_Object = MibTableColumn
rlPolicyPortCfgCbsPortShaper = _RlPolicyPortCfgCbsPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 11),
    _RlPolicyPortCfgCbsPortShaper_Type()
)
rlPolicyPortCfgCbsPortShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCbsPortShaper.setStatus("current")


class _RlPolicyPortCfgPortRateLimitStatus_Type(TruthValue):
    """Custom type rlPolicyPortCfgPortRateLimitStatus based on TruthValue"""


_RlPolicyPortCfgPortRateLimitStatus_Object = MibTableColumn
rlPolicyPortCfgPortRateLimitStatus = _RlPolicyPortCfgPortRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 12),
    _RlPolicyPortCfgPortRateLimitStatus_Type()
)
rlPolicyPortCfgPortRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgPortRateLimitStatus.setStatus("current")


class _RlPolicyPortCfgCirPortRateLimit_Type(Integer32):
    """Custom type rlPolicyPortCfgCirPortRateLimit based on Integer32"""
    defaultValue = 0


_RlPolicyPortCfgCirPortRateLimit_Object = MibTableColumn
rlPolicyPortCfgCirPortRateLimit = _RlPolicyPortCfgCirPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 13),
    _RlPolicyPortCfgCirPortRateLimit_Type()
)
rlPolicyPortCfgCirPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCirPortRateLimit.setStatus("current")


class _RlPolicyPortCfgCbsPortRateLimit_Type(Integer32):
    """Custom type rlPolicyPortCfgCbsPortRateLimit based on Integer32"""
    defaultValue = 0


_RlPolicyPortCfgCbsPortRateLimit_Object = MibTableColumn
rlPolicyPortCfgCbsPortRateLimit = _RlPolicyPortCfgCbsPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 6, 1, 14),
    _RlPolicyPortCfgCbsPortRateLimit_Type()
)
rlPolicyPortCfgCbsPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortCfgCbsPortRateLimit.setStatus("current")
_RlPolicyDropProfileTable_Object = MibTable
rlPolicyDropProfileTable = _RlPolicyDropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7)
)
if mibBuilder.loadTexts:
    rlPolicyDropProfileTable.setStatus("current")
_RlPolicyDropProfileEntry_Object = MibTableRow
rlPolicyDropProfileEntry = _RlPolicyDropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1)
)
rlPolicyDropProfileEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDropProfileIndex"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDropProfileQueueNumber"),
)
if mibBuilder.loadTexts:
    rlPolicyDropProfileEntry.setStatus("current")
_RlPolicyDropProfileIndex_Type = Integer32
_RlPolicyDropProfileIndex_Object = MibTableColumn
rlPolicyDropProfileIndex = _RlPolicyDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 1),
    _RlPolicyDropProfileIndex_Type()
)
rlPolicyDropProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDropProfileIndex.setStatus("current")
_RlPolicyDropProfileQueueNumber_Type = Integer32
_RlPolicyDropProfileQueueNumber_Object = MibTableColumn
rlPolicyDropProfileQueueNumber = _RlPolicyDropProfileQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 2),
    _RlPolicyDropProfileQueueNumber_Type()
)
rlPolicyDropProfileQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDropProfileQueueNumber.setStatus("current")
_RlPolicyDropProfileTdThersholdDp0_Type = Integer32
_RlPolicyDropProfileTdThersholdDp0_Object = MibTableColumn
rlPolicyDropProfileTdThersholdDp0 = _RlPolicyDropProfileTdThersholdDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 3),
    _RlPolicyDropProfileTdThersholdDp0_Type()
)
rlPolicyDropProfileTdThersholdDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileTdThersholdDp0.setStatus("current")
_RlPolicyDropProfileTdThersholdDp1_Type = Integer32
_RlPolicyDropProfileTdThersholdDp1_Object = MibTableColumn
rlPolicyDropProfileTdThersholdDp1 = _RlPolicyDropProfileTdThersholdDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 4),
    _RlPolicyDropProfileTdThersholdDp1_Type()
)
rlPolicyDropProfileTdThersholdDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileTdThersholdDp1.setStatus("current")
_RlPolicyDropProfileTdThersholdDp2_Type = Integer32
_RlPolicyDropProfileTdThersholdDp2_Object = MibTableColumn
rlPolicyDropProfileTdThersholdDp2 = _RlPolicyDropProfileTdThersholdDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 5),
    _RlPolicyDropProfileTdThersholdDp2_Type()
)
rlPolicyDropProfileTdThersholdDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileTdThersholdDp2.setStatus("current")
_RlPolicyDropProfileRedMinDp0_Type = Integer32
_RlPolicyDropProfileRedMinDp0_Object = MibTableColumn
rlPolicyDropProfileRedMinDp0 = _RlPolicyDropProfileRedMinDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 6),
    _RlPolicyDropProfileRedMinDp0_Type()
)
rlPolicyDropProfileRedMinDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMinDp0.setStatus("current")
_RlPolicyDropProfileRedMaxDp0_Type = Integer32
_RlPolicyDropProfileRedMaxDp0_Object = MibTableColumn
rlPolicyDropProfileRedMaxDp0 = _RlPolicyDropProfileRedMaxDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 7),
    _RlPolicyDropProfileRedMaxDp0_Type()
)
rlPolicyDropProfileRedMaxDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMaxDp0.setStatus("current")
_RlPolicyDropProfileRedProbDp0_Type = Integer32
_RlPolicyDropProfileRedProbDp0_Object = MibTableColumn
rlPolicyDropProfileRedProbDp0 = _RlPolicyDropProfileRedProbDp0_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 8),
    _RlPolicyDropProfileRedProbDp0_Type()
)
rlPolicyDropProfileRedProbDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedProbDp0.setStatus("current")
_RlPolicyDropProfileRedMinDp1_Type = Integer32
_RlPolicyDropProfileRedMinDp1_Object = MibTableColumn
rlPolicyDropProfileRedMinDp1 = _RlPolicyDropProfileRedMinDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 9),
    _RlPolicyDropProfileRedMinDp1_Type()
)
rlPolicyDropProfileRedMinDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMinDp1.setStatus("current")
_RlPolicyDropProfileRedMaxDp1_Type = Integer32
_RlPolicyDropProfileRedMaxDp1_Object = MibTableColumn
rlPolicyDropProfileRedMaxDp1 = _RlPolicyDropProfileRedMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 10),
    _RlPolicyDropProfileRedMaxDp1_Type()
)
rlPolicyDropProfileRedMaxDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMaxDp1.setStatus("current")
_RlPolicyDropProfileRedProbDp1_Type = Integer32
_RlPolicyDropProfileRedProbDp1_Object = MibTableColumn
rlPolicyDropProfileRedProbDp1 = _RlPolicyDropProfileRedProbDp1_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 11),
    _RlPolicyDropProfileRedProbDp1_Type()
)
rlPolicyDropProfileRedProbDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedProbDp1.setStatus("current")
_RlPolicyDropProfileRedMinDp2_Type = Integer32
_RlPolicyDropProfileRedMinDp2_Object = MibTableColumn
rlPolicyDropProfileRedMinDp2 = _RlPolicyDropProfileRedMinDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 12),
    _RlPolicyDropProfileRedMinDp2_Type()
)
rlPolicyDropProfileRedMinDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMinDp2.setStatus("current")
_RlPolicyDropProfileRedMaxDp2_Type = Integer32
_RlPolicyDropProfileRedMaxDp2_Object = MibTableColumn
rlPolicyDropProfileRedMaxDp2 = _RlPolicyDropProfileRedMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 13),
    _RlPolicyDropProfileRedMaxDp2_Type()
)
rlPolicyDropProfileRedMaxDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedMaxDp2.setStatus("current")
_RlPolicyDropProfileRedProbDp2_Type = Integer32
_RlPolicyDropProfileRedProbDp2_Object = MibTableColumn
rlPolicyDropProfileRedProbDp2 = _RlPolicyDropProfileRedProbDp2_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 14),
    _RlPolicyDropProfileRedProbDp2_Type()
)
rlPolicyDropProfileRedProbDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedProbDp2.setStatus("current")
_RlPolicyDropProfileRedQweight_Type = Integer32
_RlPolicyDropProfileRedQweight_Object = MibTableColumn
rlPolicyDropProfileRedQweight = _RlPolicyDropProfileRedQweight_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 15),
    _RlPolicyDropProfileRedQweight_Type()
)
rlPolicyDropProfileRedQweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileRedQweight.setStatus("current")
_RlPolicyDropProfileStatus_Type = RowStatus
_RlPolicyDropProfileStatus_Object = MibTableColumn
rlPolicyDropProfileStatus = _RlPolicyDropProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 7, 1, 16),
    _RlPolicyDropProfileStatus_Type()
)
rlPolicyDropProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDropProfileStatus.setStatus("current")
_RlPolicyVlanConfigurationTable_Object = MibTable
rlPolicyVlanConfigurationTable = _RlPolicyVlanConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8)
)
if mibBuilder.loadTexts:
    rlPolicyVlanConfigurationTable.setStatus("current")
_RlPolicyVlanCfgEntry_Object = MibTableRow
rlPolicyVlanCfgEntry = _RlPolicyVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1)
)
rlPolicyVlanCfgEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyVlanCfgVlanId"),
)
if mibBuilder.loadTexts:
    rlPolicyVlanCfgEntry.setStatus("current")
_RlPolicyVlanCfgVlanId_Type = VlanId
_RlPolicyVlanCfgVlanId_Object = MibTableColumn
rlPolicyVlanCfgVlanId = _RlPolicyVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1, 1),
    _RlPolicyVlanCfgVlanId_Type()
)
rlPolicyVlanCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyVlanCfgVlanId.setStatus("current")


class _RlPolicyVlanCfgPortRateLimitStatus_Type(TruthValue):
    """Custom type rlPolicyVlanCfgPortRateLimitStatus based on TruthValue"""


_RlPolicyVlanCfgPortRateLimitStatus_Object = MibTableColumn
rlPolicyVlanCfgPortRateLimitStatus = _RlPolicyVlanCfgPortRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1, 2),
    _RlPolicyVlanCfgPortRateLimitStatus_Type()
)
rlPolicyVlanCfgPortRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyVlanCfgPortRateLimitStatus.setStatus("current")
_RlPolicyVlanCfgCirPortRateLimit_Type = Integer32
_RlPolicyVlanCfgCirPortRateLimit_Object = MibTableColumn
rlPolicyVlanCfgCirPortRateLimit = _RlPolicyVlanCfgCirPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1, 3),
    _RlPolicyVlanCfgCirPortRateLimit_Type()
)
rlPolicyVlanCfgCirPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyVlanCfgCirPortRateLimit.setStatus("current")
_RlPolicyVlanCfgCbsPortRateLimit_Type = Integer32
_RlPolicyVlanCfgCbsPortRateLimit_Object = MibTableColumn
rlPolicyVlanCfgCbsPortRateLimit = _RlPolicyVlanCfgCbsPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1, 4),
    _RlPolicyVlanCfgCbsPortRateLimit_Type()
)
rlPolicyVlanCfgCbsPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyVlanCfgCbsPortRateLimit.setStatus("current")
_RlPolicyVlanCfgStatus_Type = RowStatus
_RlPolicyVlanCfgStatus_Object = MibTableColumn
rlPolicyVlanCfgStatus = _RlPolicyVlanCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 6, 8, 1, 5),
    _RlPolicyVlanCfgStatus_Type()
)
rlPolicyVlanCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyVlanCfgStatus.setStatus("current")
_RlPolicyDiffServ_ObjectIdentity = ObjectIdentity
rlPolicyDiffServ = _RlPolicyDiffServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7)
)
_RlPolicyDiffServPlatDependParams_ObjectIdentity = ObjectIdentity
rlPolicyDiffServPlatDependParams = _RlPolicyDiffServPlatDependParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 1)
)


class _RlDiffservModeSupported_Type(Integer32):
    """Custom type rlDiffservModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlDiffservModeSupported_Type.__name__ = "Integer32"
_RlDiffservModeSupported_Object = MibScalar
rlDiffservModeSupported = _RlDiffservModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 1, 1),
    _RlDiffservModeSupported_Type()
)
rlDiffservModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDiffservModeSupported.setStatus("current")


class _RlDiffservModeEnabled_Type(Integer32):
    """Custom type rlDiffservModeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RlDiffservModeEnabled_Type.__name__ = "Integer32"
_RlDiffservModeEnabled_Object = MibScalar
rlDiffservModeEnabled = _RlDiffservModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 2),
    _RlDiffservModeEnabled_Type()
)
rlDiffservModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDiffservModeEnabled.setStatus("current")
_RlDiffservBoundaryTable_Object = MibTable
rlDiffservBoundaryTable = _RlDiffservBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 3)
)
if mibBuilder.loadTexts:
    rlDiffservBoundaryTable.setStatus("current")
_RlDiffservBoundaryEntry_Object = MibTableRow
rlDiffservBoundaryEntry = _RlDiffservBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 3, 1)
)
rlDiffservBoundaryEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlDiffservBoundaryIfIndex"),
)
if mibBuilder.loadTexts:
    rlDiffservBoundaryEntry.setStatus("current")


class _RlDiffservBoundaryIfIndex_Type(Integer32):
    """Custom type rlDiffservBoundaryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlDiffservBoundaryIfIndex_Type.__name__ = "Integer32"
_RlDiffservBoundaryIfIndex_Object = MibTableColumn
rlDiffservBoundaryIfIndex = _RlDiffservBoundaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 3, 1, 1),
    _RlDiffservBoundaryIfIndex_Type()
)
rlDiffservBoundaryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDiffservBoundaryIfIndex.setStatus("current")


class _RlDiffservBoundaryPortType_Type(Integer32):
    """Custom type rlDiffservBoundaryPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boundary", 1),
          ("interior", 2))
    )


_RlDiffservBoundaryPortType_Type.__name__ = "Integer32"
_RlDiffservBoundaryPortType_Object = MibTableColumn
rlDiffservBoundaryPortType = _RlDiffservBoundaryPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 3, 1, 2),
    _RlDiffservBoundaryPortType_Type()
)
rlDiffservBoundaryPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDiffservBoundaryPortType.setStatus("current")
_RlDiffservBoundaryStatus_Type = RowStatus
_RlDiffservBoundaryStatus_Object = MibTableColumn
rlDiffservBoundaryStatus = _RlDiffservBoundaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 7, 3, 1, 3),
    _RlDiffservBoundaryStatus_Type()
)
rlDiffservBoundaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDiffservBoundaryStatus.setStatus("current")
_RlPolicyGlobalParams_ObjectIdentity = ObjectIdentity
rlPolicyGlobalParams = _RlPolicyGlobalParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9)
)


class _RlPolicyGlobalOperationEnabled_Type(Integer32):
    """Custom type rlPolicyGlobalOperationEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RlPolicyGlobalOperationEnabled_Type.__name__ = "Integer32"
_RlPolicyGlobalOperationEnabled_Object = MibScalar
rlPolicyGlobalOperationEnabled = _RlPolicyGlobalOperationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 1),
    _RlPolicyGlobalOperationEnabled_Type()
)
rlPolicyGlobalOperationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalOperationEnabled.setStatus("current")
_RlPolicyGlobalDefaultForwarding_Type = TruthValue
_RlPolicyGlobalDefaultForwarding_Object = MibScalar
rlPolicyGlobalDefaultForwarding = _RlPolicyGlobalDefaultForwarding_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 2),
    _RlPolicyGlobalDefaultForwarding_Type()
)
rlPolicyGlobalDefaultForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalDefaultForwarding.setStatus("current")


class _RlPolicyGlobalAdminTrapfrequency_Type(Integer32):
    """Custom type rlPolicyGlobalAdminTrapfrequency based on Integer32"""
    defaultValue = 0


_RlPolicyGlobalAdminTrapfrequency_Object = MibScalar
rlPolicyGlobalAdminTrapfrequency = _RlPolicyGlobalAdminTrapfrequency_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 3),
    _RlPolicyGlobalAdminTrapfrequency_Type()
)
rlPolicyGlobalAdminTrapfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalAdminTrapfrequency.setStatus("current")
_RlPolicyGlobalOperTrapElapsedTime_Type = Integer32
_RlPolicyGlobalOperTrapElapsedTime_Object = MibScalar
rlPolicyGlobalOperTrapElapsedTime = _RlPolicyGlobalOperTrapElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 4),
    _RlPolicyGlobalOperTrapElapsedTime_Type()
)
rlPolicyGlobalOperTrapElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalOperTrapElapsedTime.setStatus("current")
_RlPolicyGlobalQosMode_Type = RlPolicyQosMode
_RlPolicyGlobalQosMode_Object = MibScalar
rlPolicyGlobalQosMode = _RlPolicyGlobalQosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 5),
    _RlPolicyGlobalQosMode_Type()
)
rlPolicyGlobalQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalQosMode.setStatus("current")
_RlPolicyGlobalTrustMode_Type = RlPolicyTrustTypes
_RlPolicyGlobalTrustMode_Object = MibScalar
rlPolicyGlobalTrustMode = _RlPolicyGlobalTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 6),
    _RlPolicyGlobalTrustMode_Type()
)
rlPolicyGlobalTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalTrustMode.setStatus("current")


class _RlPolicyGlobalDeviceQosOperationTypes_Type(Integer32):
    """Custom type rlPolicyGlobalDeviceQosOperationTypes based on Integer32"""
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
        *(("advanced", 2),
          ("all", 3),
          ("basic", 1),
          ("notSupported", 4),
          ("service", 5))
    )


_RlPolicyGlobalDeviceQosOperationTypes_Type.__name__ = "Integer32"
_RlPolicyGlobalDeviceQosOperationTypes_Object = MibScalar
rlPolicyGlobalDeviceQosOperationTypes = _RlPolicyGlobalDeviceQosOperationTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 7),
    _RlPolicyGlobalDeviceQosOperationTypes_Type()
)
rlPolicyGlobalDeviceQosOperationTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalDeviceQosOperationTypes.setStatus("current")
_RlPolicyGlobalDscpMutationSupported_Type = TruthValue
_RlPolicyGlobalDscpMutationSupported_Object = MibScalar
rlPolicyGlobalDscpMutationSupported = _RlPolicyGlobalDscpMutationSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 8),
    _RlPolicyGlobalDscpMutationSupported_Type()
)
rlPolicyGlobalDscpMutationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalDscpMutationSupported.setStatus("current")
_RlPolicyGlobalClassifyIpPrecedenceSupported_Type = TruthValue
_RlPolicyGlobalClassifyIpPrecedenceSupported_Object = MibScalar
rlPolicyGlobalClassifyIpPrecedenceSupported = _RlPolicyGlobalClassifyIpPrecedenceSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 9),
    _RlPolicyGlobalClassifyIpPrecedenceSupported_Type()
)
rlPolicyGlobalClassifyIpPrecedenceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalClassifyIpPrecedenceSupported.setStatus("current")


class _RlPolicyGlobalDeviceShapingTypeSupported_Type(Integer32):
    """Custom type rlPolicyGlobalDeviceShapingTypeSupported based on Integer32"""
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
        *(("notSupported", 4),
          ("portAndQueueShaper", 3),
          ("portShaper", 1),
          ("queueShaper", 2))
    )


_RlPolicyGlobalDeviceShapingTypeSupported_Type.__name__ = "Integer32"
_RlPolicyGlobalDeviceShapingTypeSupported_Object = MibScalar
rlPolicyGlobalDeviceShapingTypeSupported = _RlPolicyGlobalDeviceShapingTypeSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 10),
    _RlPolicyGlobalDeviceShapingTypeSupported_Type()
)
rlPolicyGlobalDeviceShapingTypeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalDeviceShapingTypeSupported.setStatus("current")
_RlPolicyGlobalDscpRemarkingSupported_Type = TruthValue
_RlPolicyGlobalDscpRemarkingSupported_Object = MibScalar
rlPolicyGlobalDscpRemarkingSupported = _RlPolicyGlobalDscpRemarkingSupported_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 11),
    _RlPolicyGlobalDscpRemarkingSupported_Type()
)
rlPolicyGlobalDscpRemarkingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalDscpRemarkingSupported.setStatus("current")


class _RlPolicyGlobalqueueSchedulerPerDeviceOrPort_Type(Integer32):
    """Custom type rlPolicyGlobalqueueSchedulerPerDeviceOrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("port", 2))
    )


_RlPolicyGlobalqueueSchedulerPerDeviceOrPort_Type.__name__ = "Integer32"
_RlPolicyGlobalqueueSchedulerPerDeviceOrPort_Object = MibScalar
rlPolicyGlobalqueueSchedulerPerDeviceOrPort = _RlPolicyGlobalqueueSchedulerPerDeviceOrPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 9, 12),
    _RlPolicyGlobalqueueSchedulerPerDeviceOrPort_Type()
)
rlPolicyGlobalqueueSchedulerPerDeviceOrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalqueueSchedulerPerDeviceOrPort.setStatus("current")
_RlPolicyMapping_ObjectIdentity = ObjectIdentity
rlPolicyMapping = _RlPolicyMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10)
)
_RlPolicyDscpServiceClassTable_Object = MibTable
rlPolicyDscpServiceClassTable = _RlPolicyDscpServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 1)
)
if mibBuilder.loadTexts:
    rlPolicyDscpServiceClassTable.setStatus("current")
_RlPolicyDscpServiceClassEntry_Object = MibTableRow
rlPolicyDscpServiceClassEntry = _RlPolicyDscpServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 1, 1)
)
rlPolicyDscpServiceClassEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDscpIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyDscpServiceClassEntry.setStatus("current")


class _RlPolicyDscpIndex_Type(Integer32):
    """Custom type rlPolicyDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyDscpIndex_Type.__name__ = "Integer32"
_RlPolicyDscpIndex_Object = MibTableColumn
rlPolicyDscpIndex = _RlPolicyDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 1, 1, 1),
    _RlPolicyDscpIndex_Type()
)
rlPolicyDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDscpIndex.setStatus("current")


class _RlPolicyServiceClassValue_Type(Integer32):
    """Custom type rlPolicyServiceClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlPolicyServiceClassValue_Type.__name__ = "Integer32"
_RlPolicyServiceClassValue_Object = MibTableColumn
rlPolicyServiceClassValue = _RlPolicyServiceClassValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 1, 1, 2),
    _RlPolicyServiceClassValue_Type()
)
rlPolicyServiceClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyServiceClassValue.setStatus("current")
_RlPolicyDscpServiceClassStatus_Type = RowStatus
_RlPolicyDscpServiceClassStatus_Object = MibTableColumn
rlPolicyDscpServiceClassStatus = _RlPolicyDscpServiceClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 1, 1, 3),
    _RlPolicyDscpServiceClassStatus_Type()
)
rlPolicyDscpServiceClassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDscpServiceClassStatus.setStatus("current")
_RlPolicyTcpUdpPortServiceClassTable_Object = MibTable
rlPolicyTcpUdpPortServiceClassTable = _RlPolicyTcpUdpPortServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2)
)
if mibBuilder.loadTexts:
    rlPolicyTcpUdpPortServiceClassTable.setStatus("current")
_RlPolicyTcpUdpPortServiceClassEntry_Object = MibTableRow
rlPolicyTcpUdpPortServiceClassEntry = _RlPolicyTcpUdpPortServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2, 1)
)
rlPolicyTcpUdpPortServiceClassEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyProtocolType"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTcpUdpPort"),
)
if mibBuilder.loadTexts:
    rlPolicyTcpUdpPortServiceClassEntry.setStatus("current")
_RlPolicyProtocolType_Type = L4ProtType
_RlPolicyProtocolType_Object = MibTableColumn
rlPolicyProtocolType = _RlPolicyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2, 1, 1),
    _RlPolicyProtocolType_Type()
)
rlPolicyProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyProtocolType.setStatus("current")


class _RlPolicyTcpUdpPort_Type(Integer32):
    """Custom type rlPolicyTcpUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicyTcpUdpPort_Type.__name__ = "Integer32"
_RlPolicyTcpUdpPort_Object = MibTableColumn
rlPolicyTcpUdpPort = _RlPolicyTcpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2, 1, 2),
    _RlPolicyTcpUdpPort_Type()
)
rlPolicyTcpUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyTcpUdpPort.setStatus("current")
_RlPolicyMappedServiceClass_Type = Integer32
_RlPolicyMappedServiceClass_Object = MibTableColumn
rlPolicyMappedServiceClass = _RlPolicyMappedServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2, 1, 3),
    _RlPolicyMappedServiceClass_Type()
)
rlPolicyMappedServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyMappedServiceClass.setStatus("current")
_RlPolicyTcpUdpPortServiceClassStatus_Type = RowStatus
_RlPolicyTcpUdpPortServiceClassStatus_Object = MibTableColumn
rlPolicyTcpUdpPortServiceClassStatus = _RlPolicyTcpUdpPortServiceClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 2, 1, 4),
    _RlPolicyTcpUdpPortServiceClassStatus_Type()
)
rlPolicyTcpUdpPortServiceClassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTcpUdpPortServiceClassStatus.setStatus("current")
_RlPolicyDscpRemarkTable_Object = MibTable
rlPolicyDscpRemarkTable = _RlPolicyDscpRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 3)
)
if mibBuilder.loadTexts:
    rlPolicyDscpRemarkTable.setStatus("current")
_RlPolicyDscpRemarkEntry_Object = MibTableRow
rlPolicyDscpRemarkEntry = _RlPolicyDscpRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 3, 1)
)
rlPolicyDscpRemarkEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyRmOldDscp"),
)
if mibBuilder.loadTexts:
    rlPolicyDscpRemarkEntry.setStatus("current")


class _RlPolicyRmOldDscp_Type(Integer32):
    """Custom type rlPolicyRmOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyRmOldDscp_Type.__name__ = "Integer32"
_RlPolicyRmOldDscp_Object = MibTableColumn
rlPolicyRmOldDscp = _RlPolicyRmOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 3, 1, 1),
    _RlPolicyRmOldDscp_Type()
)
rlPolicyRmOldDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyRmOldDscp.setStatus("current")


class _RlPolicyRmNewDscp_Type(Integer32):
    """Custom type rlPolicyRmNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyRmNewDscp_Type.__name__ = "Integer32"
_RlPolicyRmNewDscp_Object = MibTableColumn
rlPolicyRmNewDscp = _RlPolicyRmNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 3, 1, 2),
    _RlPolicyRmNewDscp_Type()
)
rlPolicyRmNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyRmNewDscp.setStatus("current")
_RlPolicyDscpRemarkStatus_Type = RowStatus
_RlPolicyDscpRemarkStatus_Object = MibTableColumn
rlPolicyDscpRemarkStatus = _RlPolicyDscpRemarkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 3, 1, 3),
    _RlPolicyDscpRemarkStatus_Type()
)
rlPolicyDscpRemarkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDscpRemarkStatus.setStatus("current")
_RlPolicyDscpMutationTable_Object = MibTable
rlPolicyDscpMutationTable = _RlPolicyDscpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 4)
)
if mibBuilder.loadTexts:
    rlPolicyDscpMutationTable.setStatus("current")
_RlPolicyDscpMutationEntry_Object = MibTableRow
rlPolicyDscpMutationEntry = _RlPolicyDscpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 4, 1)
)
rlPolicyDscpMutationEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyOldDscp"),
)
if mibBuilder.loadTexts:
    rlPolicyDscpMutationEntry.setStatus("current")


class _RlPolicyOldDscp_Type(Integer32):
    """Custom type rlPolicyOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyOldDscp_Type.__name__ = "Integer32"
_RlPolicyOldDscp_Object = MibTableColumn
rlPolicyOldDscp = _RlPolicyOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 4, 1, 1),
    _RlPolicyOldDscp_Type()
)
rlPolicyOldDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOldDscp.setStatus("current")


class _RlPolicyNewDscp_Type(Integer32):
    """Custom type rlPolicyNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyNewDscp_Type.__name__ = "Integer32"
_RlPolicyNewDscp_Object = MibTableColumn
rlPolicyNewDscp = _RlPolicyNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 4, 1, 2),
    _RlPolicyNewDscp_Type()
)
rlPolicyNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyNewDscp.setStatus("current")
_RlPolicyDscpMutationStatus_Type = RowStatus
_RlPolicyDscpMutationStatus_Object = MibTableColumn
rlPolicyDscpMutationStatus = _RlPolicyDscpMutationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 4, 1, 3),
    _RlPolicyDscpMutationStatus_Type()
)
rlPolicyDscpMutationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDscpMutationStatus.setStatus("current")
_RlPolicyTrustModeTable_Object = MibTable
rlPolicyTrustModeTable = _RlPolicyTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 5)
)
if mibBuilder.loadTexts:
    rlPolicyTrustModeTable.setStatus("current")
_RlPolicyTrustModeEntry_Object = MibTableRow
rlPolicyTrustModeEntry = _RlPolicyTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 5, 1)
)
rlPolicyTrustModeEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTrustModePortNumber"),
)
if mibBuilder.loadTexts:
    rlPolicyTrustModeEntry.setStatus("current")
_RlPolicyTrustModePortNumber_Type = Integer32
_RlPolicyTrustModePortNumber_Object = MibTableColumn
rlPolicyTrustModePortNumber = _RlPolicyTrustModePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 5, 1, 1),
    _RlPolicyTrustModePortNumber_Type()
)
rlPolicyTrustModePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyTrustModePortNumber.setStatus("current")


class _RlPolicyTrustModePortState_Type(Integer32):
    """Custom type rlPolicyTrustModePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RlPolicyTrustModePortState_Type.__name__ = "Integer32"
_RlPolicyTrustModePortState_Object = MibTableColumn
rlPolicyTrustModePortState = _RlPolicyTrustModePortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 5, 1, 2),
    _RlPolicyTrustModePortState_Type()
)
rlPolicyTrustModePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTrustModePortState.setStatus("current")
_RlPolicyDscpVptTable_Object = MibTable
rlPolicyDscpVptTable = _RlPolicyDscpVptTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 6)
)
if mibBuilder.loadTexts:
    rlPolicyDscpVptTable.setStatus("current")
_RlPolicyDscpVptEntry_Object = MibTableRow
rlPolicyDscpVptEntry = _RlPolicyDscpVptEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 6, 1)
)
rlPolicyDscpVptEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDscpValue"),
)
if mibBuilder.loadTexts:
    rlPolicyDscpVptEntry.setStatus("current")


class _RlPolicyDscpValue_Type(Integer32):
    """Custom type rlPolicyDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyDscpValue_Type.__name__ = "Integer32"
_RlPolicyDscpValue_Object = MibTableColumn
rlPolicyDscpValue = _RlPolicyDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 6, 1, 1),
    _RlPolicyDscpValue_Type()
)
rlPolicyDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDscpValue.setStatus("current")


class _RlPolicyVptValue_Type(Integer32):
    """Custom type rlPolicyVptValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicyVptValue_Type.__name__ = "Integer32"
_RlPolicyVptValue_Object = MibTableColumn
rlPolicyVptValue = _RlPolicyVptValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 6, 1, 2),
    _RlPolicyVptValue_Type()
)
rlPolicyVptValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyVptValue.setStatus("current")
_RlPolicyDscpVptStatus_Type = RowStatus
_RlPolicyDscpVptStatus_Object = MibTableColumn
rlPolicyDscpVptStatus = _RlPolicyDscpVptStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 6, 1, 3),
    _RlPolicyDscpVptStatus_Type()
)
rlPolicyDscpVptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDscpVptStatus.setStatus("current")
_RlPolicyDscpToDpTable_Object = MibTable
rlPolicyDscpToDpTable = _RlPolicyDscpToDpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 7)
)
if mibBuilder.loadTexts:
    rlPolicyDscpToDpTable.setStatus("current")
_RlPolicyDscpToDpEntry_Object = MibTableRow
rlPolicyDscpToDpEntry = _RlPolicyDscpToDpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 7, 1)
)
rlPolicyDscpToDpEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDscp"),
)
if mibBuilder.loadTexts:
    rlPolicyDscpToDpEntry.setStatus("current")


class _RlPolicyDscp_Type(Integer32):
    """Custom type rlPolicyDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlPolicyDscp_Type.__name__ = "Integer32"
_RlPolicyDscp_Object = MibTableColumn
rlPolicyDscp = _RlPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 7, 1, 1),
    _RlPolicyDscp_Type()
)
rlPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDscp.setStatus("current")


class _RlPolicyDp_Type(Integer32):
    """Custom type rlPolicyDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RlPolicyDp_Type.__name__ = "Integer32"
_RlPolicyDp_Object = MibTableColumn
rlPolicyDp = _RlPolicyDp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 7, 1, 2),
    _RlPolicyDp_Type()
)
rlPolicyDp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDp.setStatus("current")
_RlPolicyDscpToDpStatus_Type = RowStatus
_RlPolicyDscpToDpStatus_Object = MibTableColumn
rlPolicyDscpToDpStatus = _RlPolicyDscpToDpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 10, 7, 1, 3),
    _RlPolicyDscpToDpStatus_Type()
)
rlPolicyDscpToDpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDscpToDpStatus.setStatus("current")
_RlPolicyDefaultForwardingTable_Object = MibTable
rlPolicyDefaultForwardingTable = _RlPolicyDefaultForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11)
)
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingTable.setStatus("current")
_RlPolicyDefaultForwardingEntry_Object = MibTableRow
rlPolicyDefaultForwardingEntry = _RlPolicyDefaultForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1)
)
rlPolicyDefaultForwardingEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyDefaultForwardingIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingEntry.setStatus("current")
_RlPolicyDefaultForwardingIndex_Type = Integer32
_RlPolicyDefaultForwardingIndex_Object = MibTableColumn
rlPolicyDefaultForwardingIndex = _RlPolicyDefaultForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 1),
    _RlPolicyDefaultForwardingIndex_Type()
)
rlPolicyDefaultForwardingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingIndex.setStatus("current")
_RlPolicyDefaultForwardingPortList_Type = PortList
_RlPolicyDefaultForwardingPortList_Object = MibTableColumn
rlPolicyDefaultForwardingPortList = _RlPolicyDefaultForwardingPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 2),
    _RlPolicyDefaultForwardingPortList_Type()
)
rlPolicyDefaultForwardingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingPortList.setStatus("current")
_RlPolicyDefaultForwardingVlanId1To1024_Type = OctetString
_RlPolicyDefaultForwardingVlanId1To1024_Object = MibTableColumn
rlPolicyDefaultForwardingVlanId1To1024 = _RlPolicyDefaultForwardingVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 3),
    _RlPolicyDefaultForwardingVlanId1To1024_Type()
)
rlPolicyDefaultForwardingVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingVlanId1To1024.setStatus("current")
_RlPolicyDefaultForwardingVlanId1025To2048_Type = OctetString
_RlPolicyDefaultForwardingVlanId1025To2048_Object = MibTableColumn
rlPolicyDefaultForwardingVlanId1025To2048 = _RlPolicyDefaultForwardingVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 4),
    _RlPolicyDefaultForwardingVlanId1025To2048_Type()
)
rlPolicyDefaultForwardingVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingVlanId1025To2048.setStatus("current")
_RlPolicyDefaultForwardingVlanId2049To3072_Type = OctetString
_RlPolicyDefaultForwardingVlanId2049To3072_Object = MibTableColumn
rlPolicyDefaultForwardingVlanId2049To3072 = _RlPolicyDefaultForwardingVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 5),
    _RlPolicyDefaultForwardingVlanId2049To3072_Type()
)
rlPolicyDefaultForwardingVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingVlanId2049To3072.setStatus("current")
_RlPolicyDefaultForwardingVlanId3073To4096_Type = OctetString
_RlPolicyDefaultForwardingVlanId3073To4096_Object = MibTableColumn
rlPolicyDefaultForwardingVlanId3073To4096 = _RlPolicyDefaultForwardingVlanId3073To4096_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 6),
    _RlPolicyDefaultForwardingVlanId3073To4096_Type()
)
rlPolicyDefaultForwardingVlanId3073To4096.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingVlanId3073To4096.setStatus("current")


class _RlPolicyDefaultForwardingLayer_Type(Integer32):
    """Custom type rlPolicyDefaultForwardingLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2),
          ("l3-ipv6", 3))
    )


_RlPolicyDefaultForwardingLayer_Type.__name__ = "Integer32"
_RlPolicyDefaultForwardingLayer_Object = MibTableColumn
rlPolicyDefaultForwardingLayer = _RlPolicyDefaultForwardingLayer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 7),
    _RlPolicyDefaultForwardingLayer_Type()
)
rlPolicyDefaultForwardingLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingLayer.setStatus("current")


class _RlPolicyDefaultForwardingAction_Type(Integer32):
    """Custom type rlPolicyDefaultForwardingAction based on Integer32"""
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


_RlPolicyDefaultForwardingAction_Type.__name__ = "Integer32"
_RlPolicyDefaultForwardingAction_Object = MibTableColumn
rlPolicyDefaultForwardingAction = _RlPolicyDefaultForwardingAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 8),
    _RlPolicyDefaultForwardingAction_Type()
)
rlPolicyDefaultForwardingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingAction.setStatus("current")
_RlPolicyDefaultForwardingStatus_Type = RowStatus
_RlPolicyDefaultForwardingStatus_Object = MibTableColumn
rlPolicyDefaultForwardingStatus = _RlPolicyDefaultForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 9),
    _RlPolicyDefaultForwardingStatus_Type()
)
rlPolicyDefaultForwardingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingStatus.setStatus("current")


class _RlPolicyDefaultForwardingProtocol_Type(Integer32):
    """Custom type rlPolicyDefaultForwardingProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bpdu", 1),
          ("icmpv6", 2),
          ("none", 255))
    )


_RlPolicyDefaultForwardingProtocol_Type.__name__ = "Integer32"
_RlPolicyDefaultForwardingProtocol_Object = MibTableColumn
rlPolicyDefaultForwardingProtocol = _RlPolicyDefaultForwardingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 11, 1, 10),
    _RlPolicyDefaultForwardingProtocol_Type()
)
rlPolicyDefaultForwardingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyDefaultForwardingProtocol.setStatus("current")
_RlPolicyStatistics_ObjectIdentity = ObjectIdentity
rlPolicyStatistics = _RlPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12)
)
_RlPolicyPortPolicyStatisticsTable_Object = MibTable
rlPolicyPortPolicyStatisticsTable = _RlPolicyPortPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1)
)
if mibBuilder.loadTexts:
    rlPolicyPortPolicyStatisticsTable.setStatus("current")
_RlPolicyPortPolicyStatisticsEntry_Object = MibTableRow
rlPolicyPortPolicyStatisticsEntry = _RlPolicyPortPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1)
)
rlPolicyPortPolicyStatisticsEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyPortPolicyStatisticsIfIndex"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyPortPolicyStatisticsCntrType"),
)
if mibBuilder.loadTexts:
    rlPolicyPortPolicyStatisticsEntry.setStatus("current")
_RlPolicyPortPolicyStatisticsIfIndex_Type = Integer32
_RlPolicyPortPolicyStatisticsIfIndex_Object = MibTableColumn
rlPolicyPortPolicyStatisticsIfIndex = _RlPolicyPortPolicyStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1, 1),
    _RlPolicyPortPolicyStatisticsIfIndex_Type()
)
rlPolicyPortPolicyStatisticsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPortPolicyStatisticsIfIndex.setStatus("current")
_RlPolicyPortPolicyStatisticsCntrType_Type = StatisticsCntrType
_RlPolicyPortPolicyStatisticsCntrType_Object = MibTableColumn
rlPolicyPortPolicyStatisticsCntrType = _RlPolicyPortPolicyStatisticsCntrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1, 2),
    _RlPolicyPortPolicyStatisticsCntrType_Type()
)
rlPolicyPortPolicyStatisticsCntrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyPortPolicyStatisticsCntrType.setStatus("current")
_RlPolicyPolicyStatisticsCntrSize_Type = StatisticsCntrNumOfBitsType
_RlPolicyPolicyStatisticsCntrSize_Object = MibTableColumn
rlPolicyPolicyStatisticsCntrSize = _RlPolicyPolicyStatisticsCntrSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1, 3),
    _RlPolicyPolicyStatisticsCntrSize_Type()
)
rlPolicyPolicyStatisticsCntrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyPolicyStatisticsCntrSize.setStatus("current")


class _RlPolicyPolicyStatisticsEnableCounting_Type(TruthValue):
    """Custom type rlPolicyPolicyStatisticsEnableCounting based on TruthValue"""


_RlPolicyPolicyStatisticsEnableCounting_Object = MibTableColumn
rlPolicyPolicyStatisticsEnableCounting = _RlPolicyPolicyStatisticsEnableCounting_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1, 4),
    _RlPolicyPolicyStatisticsEnableCounting_Type()
)
rlPolicyPolicyStatisticsEnableCounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyPolicyStatisticsEnableCounting.setStatus("current")
_RlPolicyPolicyStatisticsCounterValue_Type = Counter64
_RlPolicyPolicyStatisticsCounterValue_Object = MibTableColumn
rlPolicyPolicyStatisticsCounterValue = _RlPolicyPolicyStatisticsCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 1, 1, 5),
    _RlPolicyPolicyStatisticsCounterValue_Type()
)
rlPolicyPolicyStatisticsCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyPolicyStatisticsCounterValue.setStatus("current")
_RlPolicyOutQueueStatisticsTable_Object = MibTable
rlPolicyOutQueueStatisticsTable = _RlPolicyOutQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2)
)
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsTable.setStatus("current")
_RlPolicyOutQueueStatisticsEntry_Object = MibTableRow
rlPolicyOutQueueStatisticsEntry = _RlPolicyOutQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1)
)
rlPolicyOutQueueStatisticsEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyOutQueueStatisticsCountrID"),
)
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsEntry.setStatus("current")
_RlPolicyOutQueueStatisticsCountrID_Type = Integer32
_RlPolicyOutQueueStatisticsCountrID_Object = MibTableColumn
rlPolicyOutQueueStatisticsCountrID = _RlPolicyOutQueueStatisticsCountrID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 1),
    _RlPolicyOutQueueStatisticsCountrID_Type()
)
rlPolicyOutQueueStatisticsCountrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsCountrID.setStatus("current")
_RlPolicyOutQueueStatisticsIfIndexList_Type = PortList
_RlPolicyOutQueueStatisticsIfIndexList_Object = MibTableColumn
rlPolicyOutQueueStatisticsIfIndexList = _RlPolicyOutQueueStatisticsIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 2),
    _RlPolicyOutQueueStatisticsIfIndexList_Type()
)
rlPolicyOutQueueStatisticsIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsIfIndexList.setStatus("current")


class _RlPolicyOutQueueStatisticsPortAll_Type(TruthValue):
    """Custom type rlPolicyOutQueueStatisticsPortAll based on TruthValue"""


_RlPolicyOutQueueStatisticsPortAll_Object = MibTableColumn
rlPolicyOutQueueStatisticsPortAll = _RlPolicyOutQueueStatisticsPortAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 3),
    _RlPolicyOutQueueStatisticsPortAll_Type()
)
rlPolicyOutQueueStatisticsPortAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsPortAll.setStatus("current")
_RlPolicyOutQueueStatisticsVlan_Type = Integer32
_RlPolicyOutQueueStatisticsVlan_Object = MibTableColumn
rlPolicyOutQueueStatisticsVlan = _RlPolicyOutQueueStatisticsVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 4),
    _RlPolicyOutQueueStatisticsVlan_Type()
)
rlPolicyOutQueueStatisticsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsVlan.setStatus("current")


class _RlPolicyOutQueueStatisticsVlanAll_Type(TruthValue):
    """Custom type rlPolicyOutQueueStatisticsVlanAll based on TruthValue"""


_RlPolicyOutQueueStatisticsVlanAll_Object = MibTableColumn
rlPolicyOutQueueStatisticsVlanAll = _RlPolicyOutQueueStatisticsVlanAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 5),
    _RlPolicyOutQueueStatisticsVlanAll_Type()
)
rlPolicyOutQueueStatisticsVlanAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsVlanAll.setStatus("current")


class _RlPolicyOutQueueStatisticsQueue_Type(Integer32):
    """Custom type rlPolicyOutQueueStatisticsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlPolicyOutQueueStatisticsQueue_Type.__name__ = "Integer32"
_RlPolicyOutQueueStatisticsQueue_Object = MibTableColumn
rlPolicyOutQueueStatisticsQueue = _RlPolicyOutQueueStatisticsQueue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 6),
    _RlPolicyOutQueueStatisticsQueue_Type()
)
rlPolicyOutQueueStatisticsQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsQueue.setStatus("current")


class _RlPolicyOutQueueStatisticsQueueAll_Type(TruthValue):
    """Custom type rlPolicyOutQueueStatisticsQueueAll based on TruthValue"""


_RlPolicyOutQueueStatisticsQueueAll_Object = MibTableColumn
rlPolicyOutQueueStatisticsQueueAll = _RlPolicyOutQueueStatisticsQueueAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 7),
    _RlPolicyOutQueueStatisticsQueueAll_Type()
)
rlPolicyOutQueueStatisticsQueueAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsQueueAll.setStatus("current")
_RlPolicyOutQueueStatisticsDP_Type = StatisticsDPType
_RlPolicyOutQueueStatisticsDP_Object = MibTableColumn
rlPolicyOutQueueStatisticsDP = _RlPolicyOutQueueStatisticsDP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 8),
    _RlPolicyOutQueueStatisticsDP_Type()
)
rlPolicyOutQueueStatisticsDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsDP.setStatus("current")


class _RlPolicyOutQueueStatisticsDPAll_Type(TruthValue):
    """Custom type rlPolicyOutQueueStatisticsDPAll based on TruthValue"""


_RlPolicyOutQueueStatisticsDPAll_Object = MibTableColumn
rlPolicyOutQueueStatisticsDPAll = _RlPolicyOutQueueStatisticsDPAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 9),
    _RlPolicyOutQueueStatisticsDPAll_Type()
)
rlPolicyOutQueueStatisticsDPAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsDPAll.setStatus("current")
_RlPolicyOutQueueStatisticsCounterTailDropValue_Type = Counter64
_RlPolicyOutQueueStatisticsCounterTailDropValue_Object = MibTableColumn
rlPolicyOutQueueStatisticsCounterTailDropValue = _RlPolicyOutQueueStatisticsCounterTailDropValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 10),
    _RlPolicyOutQueueStatisticsCounterTailDropValue_Type()
)
rlPolicyOutQueueStatisticsCounterTailDropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsCounterTailDropValue.setStatus("current")
_RlPolicyOutQueueStatisticsCounterAllValue_Type = Counter64
_RlPolicyOutQueueStatisticsCounterAllValue_Object = MibTableColumn
rlPolicyOutQueueStatisticsCounterAllValue = _RlPolicyOutQueueStatisticsCounterAllValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 11),
    _RlPolicyOutQueueStatisticsCounterAllValue_Type()
)
rlPolicyOutQueueStatisticsCounterAllValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsCounterAllValue.setStatus("current")
_RlPolicyOutQueueStatisticsCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlPolicyOutQueueStatisticsCntrNumOfBits_Object = MibTableColumn
rlPolicyOutQueueStatisticsCntrNumOfBits = _RlPolicyOutQueueStatisticsCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 12),
    _RlPolicyOutQueueStatisticsCntrNumOfBits_Type()
)
rlPolicyOutQueueStatisticsCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsCntrNumOfBits.setStatus("current")
_RlPolicyOutQueueStatisticsStatus_Type = RowStatus
_RlPolicyOutQueueStatisticsStatus_Object = MibTableColumn
rlPolicyOutQueueStatisticsStatus = _RlPolicyOutQueueStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 2, 1, 13),
    _RlPolicyOutQueueStatisticsStatus_Type()
)
rlPolicyOutQueueStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyOutQueueStatisticsStatus.setStatus("current")
_RlPolicyGlobalStatisticsCntrsTable_Object = MibTable
rlPolicyGlobalStatisticsCntrsTable = _RlPolicyGlobalStatisticsCntrsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3)
)
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsCntrsTable.setStatus("current")
_RlPolicyGlobalStatisticsCntrsEntry_Object = MibTableRow
rlPolicyGlobalStatisticsCntrsEntry = _RlPolicyGlobalStatisticsCntrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3, 1)
)
rlPolicyGlobalStatisticsCntrsEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyGlobalStatisticsCntrsType"),
)
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsCntrsEntry.setStatus("current")
_RlPolicyGlobalStatisticsCntrsType_Type = StatisticsCntrType
_RlPolicyGlobalStatisticsCntrsType_Object = MibTableColumn
rlPolicyGlobalStatisticsCntrsType = _RlPolicyGlobalStatisticsCntrsType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3, 1, 1),
    _RlPolicyGlobalStatisticsCntrsType_Type()
)
rlPolicyGlobalStatisticsCntrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsCntrsType.setStatus("current")
_RlPolicyGlobalStatisticsCntrsNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlPolicyGlobalStatisticsCntrsNumOfBits_Object = MibTableColumn
rlPolicyGlobalStatisticsCntrsNumOfBits = _RlPolicyGlobalStatisticsCntrsNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3, 1, 2),
    _RlPolicyGlobalStatisticsCntrsNumOfBits_Type()
)
rlPolicyGlobalStatisticsCntrsNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsCntrsNumOfBits.setStatus("current")
_RlPolicyGlobalStatisticsCntrsCounterValue_Type = Counter64
_RlPolicyGlobalStatisticsCntrsCounterValue_Object = MibTableColumn
rlPolicyGlobalStatisticsCntrsCounterValue = _RlPolicyGlobalStatisticsCntrsCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3, 1, 3),
    _RlPolicyGlobalStatisticsCntrsCounterValue_Type()
)
rlPolicyGlobalStatisticsCntrsCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsCntrsCounterValue.setStatus("current")
_RlPolicyGlobalStatisticsStatus_Type = RowStatus
_RlPolicyGlobalStatisticsStatus_Object = MibTableColumn
rlPolicyGlobalStatisticsStatus = _RlPolicyGlobalStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 3, 1, 4),
    _RlPolicyGlobalStatisticsStatus_Type()
)
rlPolicyGlobalStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGlobalStatisticsStatus.setStatus("current")
_RlPolicyClearCounters_Type = Integer32
_RlPolicyClearCounters_Object = MibScalar
rlPolicyClearCounters = _RlPolicyClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 12, 4),
    _RlPolicyClearCounters_Type()
)
rlPolicyClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyClearCounters.setStatus("current")
_RlPolicyClassifierUtilization_ObjectIdentity = ObjectIdentity
rlPolicyClassifierUtilization = _RlPolicyClassifierUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13)
)
_RlPolicyClassifierUtilizationTable_Object = MibTable
rlPolicyClassifierUtilizationTable = _RlPolicyClassifierUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13, 1)
)
if mibBuilder.loadTexts:
    rlPolicyClassifierUtilizationTable.setStatus("current")
_RlPolicyClassifierUtilizationEntry_Object = MibTableRow
rlPolicyClassifierUtilizationEntry = _RlPolicyClassifierUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13, 1, 1)
)
rlPolicyClassifierUtilizationEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyClassifierUtilizationUnitId"),
)
if mibBuilder.loadTexts:
    rlPolicyClassifierUtilizationEntry.setStatus("current")


class _RlPolicyClassifierUtilizationUnitId_Type(Unsigned32):
    """Custom type rlPolicyClassifierUtilizationUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlPolicyClassifierUtilizationUnitId_Type.__name__ = "Unsigned32"
_RlPolicyClassifierUtilizationUnitId_Object = MibTableColumn
rlPolicyClassifierUtilizationUnitId = _RlPolicyClassifierUtilizationUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13, 1, 1, 1),
    _RlPolicyClassifierUtilizationUnitId_Type()
)
rlPolicyClassifierUtilizationUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPolicyClassifierUtilizationUnitId.setStatus("current")


class _RlPolicyClassifierUtilizationPercent_Type(Unsigned32):
    """Custom type rlPolicyClassifierUtilizationPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlPolicyClassifierUtilizationPercent_Type.__name__ = "Unsigned32"
_RlPolicyClassifierUtilizationPercent_Object = MibTableColumn
rlPolicyClassifierUtilizationPercent = _RlPolicyClassifierUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13, 1, 1, 2),
    _RlPolicyClassifierUtilizationPercent_Type()
)
rlPolicyClassifierUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierUtilizationPercent.setStatus("current")


class _RlPolicyClassifierUtilizationRulesNumber_Type(Unsigned32):
    """Custom type rlPolicyClassifierUtilizationRulesNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlPolicyClassifierUtilizationRulesNumber_Type.__name__ = "Unsigned32"
_RlPolicyClassifierUtilizationRulesNumber_Object = MibTableColumn
rlPolicyClassifierUtilizationRulesNumber = _RlPolicyClassifierUtilizationRulesNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 13, 1, 1, 3),
    _RlPolicyClassifierUtilizationRulesNumber_Type()
)
rlPolicyClassifierUtilizationRulesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyClassifierUtilizationRulesNumber.setStatus("current")
_RlPolicyIsTCAvailable_Type = Unsigned32
_RlPolicyIsTCAvailable_Object = MibScalar
rlPolicyIsTCAvailable = _RlPolicyIsTCAvailable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 14),
    _RlPolicyIsTCAvailable_Type()
)
rlPolicyIsTCAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyIsTCAvailable.setStatus("current")
_RlPolicyTimeBasedAcl_ObjectIdentity = ObjectIdentity
rlPolicyTimeBasedAcl = _RlPolicyTimeBasedAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15)
)
_RlPolicyTimeBasedAclTable_Object = MibTable
rlPolicyTimeBasedAclTable = _RlPolicyTimeBasedAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1)
)
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclTable.setStatus("current")
_RlPolicyTimeBasedAclEntry_Object = MibTableRow
rlPolicyTimeBasedAclEntry = _RlPolicyTimeBasedAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1)
)
rlPolicyTimeBasedAclEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTimeBasedAclRangeIndex"),
)
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclEntry.setStatus("current")
_RlPolicyTimeBasedAclRangeIndex_Type = Integer32
_RlPolicyTimeBasedAclRangeIndex_Object = MibTableColumn
rlPolicyTimeBasedAclRangeIndex = _RlPolicyTimeBasedAclRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1, 1),
    _RlPolicyTimeBasedAclRangeIndex_Type()
)
rlPolicyTimeBasedAclRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclRangeIndex.setStatus("current")


class _RlPolicyTimeBasedAclRangeName_Type(DisplayString):
    """Custom type rlPolicyTimeBasedAclRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlPolicyTimeBasedAclRangeName_Type.__name__ = "DisplayString"
_RlPolicyTimeBasedAclRangeName_Object = MibTableColumn
rlPolicyTimeBasedAclRangeName = _RlPolicyTimeBasedAclRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1, 2),
    _RlPolicyTimeBasedAclRangeName_Type()
)
rlPolicyTimeBasedAclRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclRangeName.setStatus("current")


class _RlPolicyTimeBasedAclAbsStart_Type(DisplayString):
    """Custom type rlPolicyTimeBasedAclAbsStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_RlPolicyTimeBasedAclAbsStart_Type.__name__ = "DisplayString"
_RlPolicyTimeBasedAclAbsStart_Object = MibTableColumn
rlPolicyTimeBasedAclAbsStart = _RlPolicyTimeBasedAclAbsStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1, 3),
    _RlPolicyTimeBasedAclAbsStart_Type()
)
rlPolicyTimeBasedAclAbsStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclAbsStart.setStatus("current")


class _RlPolicyTimeBasedAclAbsEnd_Type(DisplayString):
    """Custom type rlPolicyTimeBasedAclAbsEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_RlPolicyTimeBasedAclAbsEnd_Type.__name__ = "DisplayString"
_RlPolicyTimeBasedAclAbsEnd_Object = MibTableColumn
rlPolicyTimeBasedAclAbsEnd = _RlPolicyTimeBasedAclAbsEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1, 4),
    _RlPolicyTimeBasedAclAbsEnd_Type()
)
rlPolicyTimeBasedAclAbsEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclAbsEnd.setStatus("current")
_RlPolicyTimeBasedAclStatus_Type = RowStatus
_RlPolicyTimeBasedAclStatus_Object = MibTableColumn
rlPolicyTimeBasedAclStatus = _RlPolicyTimeBasedAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 1, 1, 5),
    _RlPolicyTimeBasedAclStatus_Type()
)
rlPolicyTimeBasedAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclStatus.setStatus("current")
_RlPolicyTimeBasedAclPeriodicTable_Object = MibTable
rlPolicyTimeBasedAclPeriodicTable = _RlPolicyTimeBasedAclPeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2)
)
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicTable.setStatus("current")
_RlPolicyTimeBasedAclPeriodicEntry_Object = MibTableRow
rlPolicyTimeBasedAclPeriodicEntry = _RlPolicyTimeBasedAclPeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1)
)
rlPolicyTimeBasedAclPeriodicEntry.setIndexNames(
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTimeBasedAclPeriodicIndex"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTimeBasedAclPeriodicWeekList"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTimeBasedAclPeriodicStart"),
    (0, "DLINK-3100-POLICY-MIB", "rlPolicyTimeBasedAclPeriodicEnd"),
)
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicEntry.setStatus("current")
_RlPolicyTimeBasedAclPeriodicIndex_Type = Integer32
_RlPolicyTimeBasedAclPeriodicIndex_Object = MibTableColumn
rlPolicyTimeBasedAclPeriodicIndex = _RlPolicyTimeBasedAclPeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1, 1),
    _RlPolicyTimeBasedAclPeriodicIndex_Type()
)
rlPolicyTimeBasedAclPeriodicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicIndex.setStatus("current")
_RlPolicyTimeBasedAclPeriodicWeekList_Type = RlPolicyTimeBasedAclWeekPeriodicList
_RlPolicyTimeBasedAclPeriodicWeekList_Object = MibTableColumn
rlPolicyTimeBasedAclPeriodicWeekList = _RlPolicyTimeBasedAclPeriodicWeekList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1, 2),
    _RlPolicyTimeBasedAclPeriodicWeekList_Type()
)
rlPolicyTimeBasedAclPeriodicWeekList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicWeekList.setStatus("current")


class _RlPolicyTimeBasedAclPeriodicStart_Type(DisplayString):
    """Custom type rlPolicyTimeBasedAclPeriodicStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_RlPolicyTimeBasedAclPeriodicStart_Type.__name__ = "DisplayString"
_RlPolicyTimeBasedAclPeriodicStart_Object = MibTableColumn
rlPolicyTimeBasedAclPeriodicStart = _RlPolicyTimeBasedAclPeriodicStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1, 3),
    _RlPolicyTimeBasedAclPeriodicStart_Type()
)
rlPolicyTimeBasedAclPeriodicStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicStart.setStatus("current")


class _RlPolicyTimeBasedAclPeriodicEnd_Type(DisplayString):
    """Custom type rlPolicyTimeBasedAclPeriodicEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_RlPolicyTimeBasedAclPeriodicEnd_Type.__name__ = "DisplayString"
_RlPolicyTimeBasedAclPeriodicEnd_Object = MibTableColumn
rlPolicyTimeBasedAclPeriodicEnd = _RlPolicyTimeBasedAclPeriodicEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1, 4),
    _RlPolicyTimeBasedAclPeriodicEnd_Type()
)
rlPolicyTimeBasedAclPeriodicEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicEnd.setStatus("current")
_RlPolicyTimeBasedAclPeriodicStatus_Type = RowStatus
_RlPolicyTimeBasedAclPeriodicStatus_Object = MibTableColumn
rlPolicyTimeBasedAclPeriodicStatus = _RlPolicyTimeBasedAclPeriodicStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 15, 2, 1, 5),
    _RlPolicyTimeBasedAclPeriodicStatus_Type()
)
rlPolicyTimeBasedAclPeriodicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyTimeBasedAclPeriodicStatus.setStatus("current")
_RlPolicyCPUSafeGuardEnable_Type = Integer32
_RlPolicyCPUSafeGuardEnable_Object = MibScalar
rlPolicyCPUSafeGuardEnable = _RlPolicyCPUSafeGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 59, 16),
    _RlPolicyCPUSafeGuardEnable_Type()
)
rlPolicyCPUSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyCPUSafeGuardEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-POLICY-MIB",
    **{"InterfaceType": InterfaceType,
       "StatisticsCntrNumOfBitsType": StatisticsCntrNumOfBitsType,
       "StatisticsDPType": StatisticsDPType,
       "StatisticsClearActionType": StatisticsClearActionType,
       "StatisticsCntrType": StatisticsCntrType,
       "RlPolicyGroupType": RlPolicyGroupType,
       "RlPolicyClassifierDiffservIfType": RlPolicyClassifierDiffservIfType,
       "RlPolicyTrustTypes": RlPolicyTrustTypes,
       "RlPolicyQosMode": RlPolicyQosMode,
       "L4ProtType": L4ProtType,
       "RlPolicyTimeBasedAclWeekPeriodicList": RlPolicyTimeBasedAclWeekPeriodicList,
       "rlPolicy": rlPolicy,
       "rlPolicyMibVersion": rlPolicyMibVersion,
       "rlPolicyClassifier": rlPolicyClassifier,
       "rlPolicyClassifierPlatDependParams": rlPolicyClassifierPlatDependParams,
       "rlPolicyFlowClassificationOffsetsGroupScheme": rlPolicyFlowClassificationOffsetsGroupScheme,
       "rlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup": rlPolicyNumberOfOffsetsPerFlowClassificationOffsetGroup,
       "rlPolicyFlowClassificationOffsetGroupMaximumOffset": rlPolicyFlowClassificationOffsetGroupMaximumOffset,
       "rlPolicyNumberOfOffsetsPerOmpcGroup": rlPolicyNumberOfOffsetsPerOmpcGroup,
       "rlPolicyOmpcMaximumOffset": rlPolicyOmpcMaximumOffset,
       "rlPolicyOMPCPermittedOperators": rlPolicyOMPCPermittedOperators,
       "rlPolicyMaxOMPCLengthForBiggerSmallerOperation": rlPolicyMaxOMPCLengthForBiggerSmallerOperation,
       "rlPolicyClassifierAdditionalCriteriaSupported": rlPolicyClassifierAdditionalCriteriaSupported,
       "rlPolicyClassifierAdditionalCriteriaUsedInOffsetCount": rlPolicyClassifierAdditionalCriteriaUsedInOffsetCount,
       "rlPolicyClassifierPermittedOffsetTypes": rlPolicyClassifierPermittedOffsetTypes,
       "rlPolicyClassifierOMPCActions": rlPolicyClassifierOMPCActions,
       "rlPolicyFlowClassificationOffsetsTable": rlPolicyFlowClassificationOffsetsTable,
       "rlPolicyFlowClassificationOffsetsGroupEntry": rlPolicyFlowClassificationOffsetsGroupEntry,
       "rlPolicyFlowClassificationOffsetsGroupType": rlPolicyFlowClassificationOffsetsGroupType,
       "rlPolicyFlowClassificationOffsetsGroupOffset": rlPolicyFlowClassificationOffsetsGroupOffset,
       "rlPolicyFlowClassificationOffsetsGroupOffsetType": rlPolicyFlowClassificationOffsetsGroupOffsetType,
       "rlPolicyFlowClassificationOffsetsGroupMask": rlPolicyFlowClassificationOffsetsGroupMask,
       "rlPolicyFlowClassificationOffsetsGroupUseInputInterface": rlPolicyFlowClassificationOffsetsGroupUseInputInterface,
       "rlPolicyFlowClassificationOffsetsGroupUseOutputInterface": rlPolicyFlowClassificationOffsetsGroupUseOutputInterface,
       "rlPolicyFlowClassificationOffsetsGroupUseVlanId": rlPolicyFlowClassificationOffsetsGroupUseVlanId,
       "rlPolicyFlowClassificationOffsetsGroupStatus": rlPolicyFlowClassificationOffsetsGroupStatus,
       "rlPolicyFlowClassificationOffsetsGroupUseVPTId": rlPolicyFlowClassificationOffsetsGroupUseVPTId,
       "rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId": rlPolicyFlowClassificationOffsetsGroupUseEtherTypeId,
       "rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId": rlPolicyFlowClassificationOffsetsGroupUseInnerVlanId,
       "rlPolicyOMPCTable": rlPolicyOMPCTable,
       "rlPolicyOMPCEntry": rlPolicyOMPCEntry,
       "rlPolicyOMPCGroupType": rlPolicyOMPCGroupType,
       "rlPolicyOMPCIndex": rlPolicyOMPCIndex,
       "rlPolicyOMPCOffset": rlPolicyOMPCOffset,
       "rlPolicyOMPCOffsetType": rlPolicyOMPCOffsetType,
       "rlPolicyOMPCMask": rlPolicyOMPCMask,
       "rlPolicyOMPCPattern": rlPolicyOMPCPattern,
       "rlPolicyOMPCCondition": rlPolicyOMPCCondition,
       "rlPolicyOMPCDescription": rlPolicyOMPCDescription,
       "rlPolicyOMPCStatus": rlPolicyOMPCStatus,
       "rlPolicyClassifierTable": rlPolicyClassifierTable,
       "rlPolicyClassifierEntry": rlPolicyClassifierEntry,
       "rlPolicyClassifierType": rlPolicyClassifierType,
       "rlPolicyClassifierIndex": rlPolicyClassifierIndex,
       "rlPolicyClassifierOmpcList": rlPolicyClassifierOmpcList,
       "rlPolicyClassifierInIfIndex": rlPolicyClassifierInIfIndex,
       "rlPolicyClassifierOutIfIndex": rlPolicyClassifierOutIfIndex,
       "rlPolicyClassifierVID": rlPolicyClassifierVID,
       "rlPolicyClassifierDiffservInIfType": rlPolicyClassifierDiffservInIfType,
       "rlPolicyClassifierDiffservOutIfType": rlPolicyClassifierDiffservOutIfType,
       "rlPolicyClassifierStatus": rlPolicyClassifierStatus,
       "rlPolicyClassifierInIfIndexList": rlPolicyClassifierInIfIndexList,
       "rlPolicyClassifierOutIfIndexList": rlPolicyClassifierOutIfIndexList,
       "rlPolicyClassifierVPTID": rlPolicyClassifierVPTID,
       "rlPolicyClassifierVPTIDMask": rlPolicyClassifierVPTIDMask,
       "rlPolicyClassifierEtherTypeID": rlPolicyClassifierEtherTypeID,
       "rlPolicyClassifierInnerVID": rlPolicyClassifierInnerVID,
       "rlPolicyRules": rlPolicyRules,
       "rlPolicyRulesPlatDependParams": rlPolicyRulesPlatDependParams,
       "rlPolicyDroppedPacketCountSupported": rlPolicyDroppedPacketCountSupported,
       "rlPolicyFilterActionOptions": rlPolicyFilterActionOptions,
       "rlPolicyIngressMeteringSupported": rlPolicyIngressMeteringSupported,
       "rlPolicyEgressMeteringSupported": rlPolicyEgressMeteringSupported,
       "rlPolicyRulesTable": rlPolicyRulesTable,
       "rlPolicyRulesEntry": rlPolicyRulesEntry,
       "rlPolicyRulesTableType": rlPolicyRulesTableType,
       "rlPolicyRulesInterfaceDirection": rlPolicyRulesInterfaceDirection,
       "rlPolicyRulesIndex": rlPolicyRulesIndex,
       "rlPolicyRulesClassifierPointer": rlPolicyRulesClassifierPointer,
       "rlPolicyRulesFilteringAction": rlPolicyRulesFilteringAction,
       "rlPolicyRulesDroppedPackets": rlPolicyRulesDroppedPackets,
       "rlPolicyRulesFurtherRefPointer": rlPolicyRulesFurtherRefPointer,
       "rlPolicyRulesDescription": rlPolicyRulesDescription,
       "rlPolicyRulesStatus": rlPolicyRulesStatus,
       "rlPolicyRulesCounterEnable": rlPolicyRulesCounterEnable,
       "rlPolicyRulesCounter": rlPolicyRulesCounter,
       "rlPolicyRulesActionPointer": rlPolicyRulesActionPointer,
       "rlPolicyRulesTimeRange1": rlPolicyRulesTimeRange1,
       "rlPolicyRulesTimeRange2": rlPolicyRulesTimeRange2,
       "rlPolicyRulesDownloadMarker": rlPolicyRulesDownloadMarker,
       "rlPolicyMeterClass": rlPolicyMeterClass,
       "rlPolicyMeterPlatDependParams": rlPolicyMeterPlatDependParams,
       "rlPolicyMeterDepth": rlPolicyMeterDepth,
       "rlPolicyMeterClassTable": rlPolicyMeterClassTable,
       "rlPolicyMeteringClassEntry": rlPolicyMeteringClassEntry,
       "rlPolicyMeteringClassIndex": rlPolicyMeteringClassIndex,
       "rlPolicyMeteringClassAlwaysConform": rlPolicyMeteringClassAlwaysConform,
       "rlPolicyMeteringClassAggregateMeterRate": rlPolicyMeteringClassAggregateMeterRate,
       "rlPolicyMeteringClassAggregateMeterBurstSize": rlPolicyMeteringClassAggregateMeterBurstSize,
       "rlPolicyMeteringClassPerSessionMeteringRate": rlPolicyMeteringClassPerSessionMeteringRate,
       "rlPolicyMeteringClassMaxSessionLimit": rlPolicyMeteringClassMaxSessionLimit,
       "rlPolicyMeteringClassActionPointer": rlPolicyMeteringClassActionPointer,
       "rlPolicyMeteringClassFailMeterPointer": rlPolicyMeteringClassFailMeterPointer,
       "rlPolicyMeteringClassStatus": rlPolicyMeteringClassStatus,
       "rlPolicyMeteringCounterEnable": rlPolicyMeteringCounterEnable,
       "rlPolicyMeteringClassInProfileCounter": rlPolicyMeteringClassInProfileCounter,
       "rlPolicyMeteringClassOutProfileCounter": rlPolicyMeteringClassOutProfileCounter,
       "rlPolicyAction": rlPolicyAction,
       "rlPolicyActionPlatDependParams": rlPolicyActionPlatDependParams,
       "rlPolicyActionMREDSupported": rlPolicyActionMREDSupported,
       "rlPolicyActionDroppedPacketCountSupported": rlPolicyActionDroppedPacketCountSupported,
       "rlPolicyActionDroppedDropPrecedenceSupported": rlPolicyActionDroppedDropPrecedenceSupported,
       "rlPolicyActionInProfileDropPrecedence": rlPolicyActionInProfileDropPrecedence,
       "rlPolicyActionOutProfileDropPrecedence": rlPolicyActionOutProfileDropPrecedence,
       "rlPolicyActionDscpSupport": rlPolicyActionDscpSupport,
       "rlPolicyActionDsQueueManagmentSupported": rlPolicyActionDsQueueManagmentSupported,
       "rlPolicyActionTable": rlPolicyActionTable,
       "rlPolicyActionEntry": rlPolicyActionEntry,
       "rlPolicyActionIndex": rlPolicyActionIndex,
       "rlPolicyActionNewDscp": rlPolicyActionNewDscp,
       "rlPolicyActionChangeDscp": rlPolicyActionChangeDscp,
       "rlPolicyActionMinThreshold": rlPolicyActionMinThreshold,
       "rlPolicyActionMaxThreshold": rlPolicyActionMaxThreshold,
       "rlPolicyActionDropPolicy": rlPolicyActionDropPolicy,
       "rlPolicyActionDroppedPackets": rlPolicyActionDroppedPackets,
       "rlPolicyActionNonDsInProfileDropPrecedence": rlPolicyActionNonDsInProfileDropPrecedence,
       "rlPolicyActionNonDsOutProfileDropPrecedence": rlPolicyActionNonDsOutProfileDropPrecedence,
       "rlPolicyActionChangeVpt": rlPolicyActionChangeVpt,
       "rlPolicyActionNewVpt": rlPolicyActionNewVpt,
       "rlPolicyActionServiceClassPointer": rlPolicyActionServiceClassPointer,
       "rlPolicyActionStatus": rlPolicyActionStatus,
       "rlPolicyActionChangeDscpNonConform": rlPolicyActionChangeDscpNonConform,
       "rlPolicyActionChangeNewDscpNonConform": rlPolicyActionChangeNewDscpNonConform,
       "rlPolicyActionAdvancedTrustMode": rlPolicyActionAdvancedTrustMode,
       "rlPolicyActionNewIpPrecedence": rlPolicyActionNewIpPrecedence,
       "rlPolicyActionChangeIpPrecedence": rlPolicyActionChangeIpPrecedence,
       "rlPolicyActionReDirect": rlPolicyActionReDirect,
       "rlPolicyActionCopyPort": rlPolicyActionCopyPort,
       "rlPolicyActionChangeVid": rlPolicyActionChangeVid,
       "rlPolicyActionNewVid": rlPolicyActionNewVid,
       "rlPolicyServiceClass": rlPolicyServiceClass,
       "rlPolicyServiceClassPlatDependParams": rlPolicyServiceClassPlatDependParams,
       "rlPolicyNumberOfServiceClassesSupported": rlPolicyNumberOfServiceClassesSupported,
       "rlPolicyBoundedPriorityQueueSupport": rlPolicyBoundedPriorityQueueSupport,
       "rlPolicyDefaultServiceClass": rlPolicyDefaultServiceClass,
       "rlPolicyActiveServiceClassTable": rlPolicyActiveServiceClassTable,
       "rlPolicyServiceClassTentativeTable": rlPolicyServiceClassTentativeTable,
       "rlPolicyServiceClassTentativeEntry": rlPolicyServiceClassTentativeEntry,
       "rlPolicyServiceClassTentativeIndex": rlPolicyServiceClassTentativeIndex,
       "rlPolicyServiceClassTentativeName": rlPolicyServiceClassTentativeName,
       "rlPolicyServiceClassTentativePhbType": rlPolicyServiceClassTentativePhbType,
       "rlPolicyServiceClassTentativeMinRate": rlPolicyServiceClassTentativeMinRate,
       "rlPolicyServiceClassTentativeMaxRate": rlPolicyServiceClassTentativeMaxRate,
       "rlPolicyServiceClassTentativePriority": rlPolicyServiceClassTentativePriority,
       "rlPolicyServiceClassTentative8021DPri": rlPolicyServiceClassTentative8021DPri,
       "rlPolicyServiceClassTentativeStatus": rlPolicyServiceClassTentativeStatus,
       "rlPolicyServiceClassTentativeTdThersholdDp0": rlPolicyServiceClassTentativeTdThersholdDp0,
       "rlPolicyServiceClassTentativeTdThersholdDp1": rlPolicyServiceClassTentativeTdThersholdDp1,
       "rlPolicyServiceClassTentativeTdThersholdDp2": rlPolicyServiceClassTentativeTdThersholdDp2,
       "rlPolicyServiceClassTentativeRedMinDp0": rlPolicyServiceClassTentativeRedMinDp0,
       "rlPolicyServiceClassTentativeRedMaxDp0": rlPolicyServiceClassTentativeRedMaxDp0,
       "rlPolicyServiceClassTentativeRedProbDp0": rlPolicyServiceClassTentativeRedProbDp0,
       "rlPolicyServiceClassTentativeRedMinDp1": rlPolicyServiceClassTentativeRedMinDp1,
       "rlPolicyServiceClassTentativeRedMaxDp1": rlPolicyServiceClassTentativeRedMaxDp1,
       "rlPolicyServiceClassTentativeRedProbDp1": rlPolicyServiceClassTentativeRedProbDp1,
       "rlPolicyServiceClassTentativeRedMinDp2": rlPolicyServiceClassTentativeRedMinDp2,
       "rlPolicyServiceClassTentativeRedMaxDp2": rlPolicyServiceClassTentativeRedMaxDp2,
       "rlPolicyServiceClassTentativeRedProbDp2": rlPolicyServiceClassTentativeRedProbDp2,
       "rlPolicyServiceClassTentativeRedQweight": rlPolicyServiceClassTentativeRedQweight,
       "rlPolicyServiceClassTentativeShaperStatus": rlPolicyServiceClassTentativeShaperStatus,
       "rlPolicyServiceClassTentativeCirQueueShaper": rlPolicyServiceClassTentativeCirQueueShaper,
       "rlPolicyServiceClassTentativeCbsQueueShaper": rlPolicyServiceClassTentativeCbsQueueShaper,
       "rlPolicyServiceClassActiveTable": rlPolicyServiceClassActiveTable,
       "rlPolicyServiceClassActiveEntry": rlPolicyServiceClassActiveEntry,
       "rlPolicyServiceClassActiveIndex": rlPolicyServiceClassActiveIndex,
       "rlPolicyServiceClassActiveName": rlPolicyServiceClassActiveName,
       "rlPolicyServiceClassActivePhbType": rlPolicyServiceClassActivePhbType,
       "rlPolicyServiceClassActiveMinRate": rlPolicyServiceClassActiveMinRate,
       "rlPolicyServiceClassActiveMaxRate": rlPolicyServiceClassActiveMaxRate,
       "rlPolicyServiceClassActivePriority": rlPolicyServiceClassActivePriority,
       "rlPolicyServiceClassActive8021DPri": rlPolicyServiceClassActive8021DPri,
       "rlPolicyServiceClassActiveTdThersholdDp0": rlPolicyServiceClassActiveTdThersholdDp0,
       "rlPolicyServiceClassActiveTdThersholdDp1": rlPolicyServiceClassActiveTdThersholdDp1,
       "rlPolicyServiceClassActiveTdThersholdDp2": rlPolicyServiceClassActiveTdThersholdDp2,
       "rlPolicyServiceClassActiveRedMinDp0": rlPolicyServiceClassActiveRedMinDp0,
       "rlPolicyServiceClassActiveRedMaxDp0": rlPolicyServiceClassActiveRedMaxDp0,
       "rlPolicyServiceClassActiveRedProbDp0": rlPolicyServiceClassActiveRedProbDp0,
       "rlPolicyServiceClassActiveRedMinDp1": rlPolicyServiceClassActiveRedMinDp1,
       "rlPolicyServiceClassActiveRedMaxDp1": rlPolicyServiceClassActiveRedMaxDp1,
       "rlPolicyServiceClassActiveRedProbDp1": rlPolicyServiceClassActiveRedProbDp1,
       "rlPolicyServiceClassActiveRedMinDp2": rlPolicyServiceClassActiveRedMinDp2,
       "rlPolicyServiceClassActiveRedMaxDp2": rlPolicyServiceClassActiveRedMaxDp2,
       "rlPolicyServiceClassActiveRedProbDp2": rlPolicyServiceClassActiveRedProbDp2,
       "rlPolicyServiceClassActiveRedQweight": rlPolicyServiceClassActiveRedQweight,
       "rlPolicyServiceClassActiveShaperStatus": rlPolicyServiceClassActiveShaperStatus,
       "rlPolicyServiceClassActiveCirQueueShaper": rlPolicyServiceClassActiveCirQueueShaper,
       "rlPolicyServiceClassActiveCbsQueueShaper": rlPolicyServiceClassActiveCbsQueueShaper,
       "rlPolicyPortConfigurationTable": rlPolicyPortConfigurationTable,
       "rlPolicyPortCfgEntry": rlPolicyPortCfgEntry,
       "rlPolicyPortCfgIfIndex": rlPolicyPortCfgIfIndex,
       "rlPolicyPortCfgMinimalBandwidth": rlPolicyPortCfgMinimalBandwidth,
       "rlPolicyPortCfgMaximalBandwidth": rlPolicyPortCfgMaximalBandwidth,
       "rlPolicyPortCfgStatus": rlPolicyPortCfgStatus,
       "rlpolicyDropProfilePointer": rlpolicyDropProfilePointer,
       "rlPolicyPortCfgQueueShaperStatus": rlPolicyPortCfgQueueShaperStatus,
       "rlPolicyPortCfgCirQueueShaper": rlPolicyPortCfgCirQueueShaper,
       "rlPolicyPortCfgCbsQueueShaper": rlPolicyPortCfgCbsQueueShaper,
       "rlPolicyPortCfgPortShaperStatus": rlPolicyPortCfgPortShaperStatus,
       "rlPolicyPortCfgCirPortShaper": rlPolicyPortCfgCirPortShaper,
       "rlPolicyPortCfgCbsPortShaper": rlPolicyPortCfgCbsPortShaper,
       "rlPolicyPortCfgPortRateLimitStatus": rlPolicyPortCfgPortRateLimitStatus,
       "rlPolicyPortCfgCirPortRateLimit": rlPolicyPortCfgCirPortRateLimit,
       "rlPolicyPortCfgCbsPortRateLimit": rlPolicyPortCfgCbsPortRateLimit,
       "rlPolicyDropProfileTable": rlPolicyDropProfileTable,
       "rlPolicyDropProfileEntry": rlPolicyDropProfileEntry,
       "rlPolicyDropProfileIndex": rlPolicyDropProfileIndex,
       "rlPolicyDropProfileQueueNumber": rlPolicyDropProfileQueueNumber,
       "rlPolicyDropProfileTdThersholdDp0": rlPolicyDropProfileTdThersholdDp0,
       "rlPolicyDropProfileTdThersholdDp1": rlPolicyDropProfileTdThersholdDp1,
       "rlPolicyDropProfileTdThersholdDp2": rlPolicyDropProfileTdThersholdDp2,
       "rlPolicyDropProfileRedMinDp0": rlPolicyDropProfileRedMinDp0,
       "rlPolicyDropProfileRedMaxDp0": rlPolicyDropProfileRedMaxDp0,
       "rlPolicyDropProfileRedProbDp0": rlPolicyDropProfileRedProbDp0,
       "rlPolicyDropProfileRedMinDp1": rlPolicyDropProfileRedMinDp1,
       "rlPolicyDropProfileRedMaxDp1": rlPolicyDropProfileRedMaxDp1,
       "rlPolicyDropProfileRedProbDp1": rlPolicyDropProfileRedProbDp1,
       "rlPolicyDropProfileRedMinDp2": rlPolicyDropProfileRedMinDp2,
       "rlPolicyDropProfileRedMaxDp2": rlPolicyDropProfileRedMaxDp2,
       "rlPolicyDropProfileRedProbDp2": rlPolicyDropProfileRedProbDp2,
       "rlPolicyDropProfileRedQweight": rlPolicyDropProfileRedQweight,
       "rlPolicyDropProfileStatus": rlPolicyDropProfileStatus,
       "rlPolicyVlanConfigurationTable": rlPolicyVlanConfigurationTable,
       "rlPolicyVlanCfgEntry": rlPolicyVlanCfgEntry,
       "rlPolicyVlanCfgVlanId": rlPolicyVlanCfgVlanId,
       "rlPolicyVlanCfgPortRateLimitStatus": rlPolicyVlanCfgPortRateLimitStatus,
       "rlPolicyVlanCfgCirPortRateLimit": rlPolicyVlanCfgCirPortRateLimit,
       "rlPolicyVlanCfgCbsPortRateLimit": rlPolicyVlanCfgCbsPortRateLimit,
       "rlPolicyVlanCfgStatus": rlPolicyVlanCfgStatus,
       "rlPolicyDiffServ": rlPolicyDiffServ,
       "rlPolicyDiffServPlatDependParams": rlPolicyDiffServPlatDependParams,
       "rlDiffservModeSupported": rlDiffservModeSupported,
       "rlDiffservModeEnabled": rlDiffservModeEnabled,
       "rlDiffservBoundaryTable": rlDiffservBoundaryTable,
       "rlDiffservBoundaryEntry": rlDiffservBoundaryEntry,
       "rlDiffservBoundaryIfIndex": rlDiffservBoundaryIfIndex,
       "rlDiffservBoundaryPortType": rlDiffservBoundaryPortType,
       "rlDiffservBoundaryStatus": rlDiffservBoundaryStatus,
       "rlPolicyGlobalParams": rlPolicyGlobalParams,
       "rlPolicyGlobalOperationEnabled": rlPolicyGlobalOperationEnabled,
       "rlPolicyGlobalDefaultForwarding": rlPolicyGlobalDefaultForwarding,
       "rlPolicyGlobalAdminTrapfrequency": rlPolicyGlobalAdminTrapfrequency,
       "rlPolicyGlobalOperTrapElapsedTime": rlPolicyGlobalOperTrapElapsedTime,
       "rlPolicyGlobalQosMode": rlPolicyGlobalQosMode,
       "rlPolicyGlobalTrustMode": rlPolicyGlobalTrustMode,
       "rlPolicyGlobalDeviceQosOperationTypes": rlPolicyGlobalDeviceQosOperationTypes,
       "rlPolicyGlobalDscpMutationSupported": rlPolicyGlobalDscpMutationSupported,
       "rlPolicyGlobalClassifyIpPrecedenceSupported": rlPolicyGlobalClassifyIpPrecedenceSupported,
       "rlPolicyGlobalDeviceShapingTypeSupported": rlPolicyGlobalDeviceShapingTypeSupported,
       "rlPolicyGlobalDscpRemarkingSupported": rlPolicyGlobalDscpRemarkingSupported,
       "rlPolicyGlobalqueueSchedulerPerDeviceOrPort": rlPolicyGlobalqueueSchedulerPerDeviceOrPort,
       "rlPolicyMapping": rlPolicyMapping,
       "rlPolicyDscpServiceClassTable": rlPolicyDscpServiceClassTable,
       "rlPolicyDscpServiceClassEntry": rlPolicyDscpServiceClassEntry,
       "rlPolicyDscpIndex": rlPolicyDscpIndex,
       "rlPolicyServiceClassValue": rlPolicyServiceClassValue,
       "rlPolicyDscpServiceClassStatus": rlPolicyDscpServiceClassStatus,
       "rlPolicyTcpUdpPortServiceClassTable": rlPolicyTcpUdpPortServiceClassTable,
       "rlPolicyTcpUdpPortServiceClassEntry": rlPolicyTcpUdpPortServiceClassEntry,
       "rlPolicyProtocolType": rlPolicyProtocolType,
       "rlPolicyTcpUdpPort": rlPolicyTcpUdpPort,
       "rlPolicyMappedServiceClass": rlPolicyMappedServiceClass,
       "rlPolicyTcpUdpPortServiceClassStatus": rlPolicyTcpUdpPortServiceClassStatus,
       "rlPolicyDscpRemarkTable": rlPolicyDscpRemarkTable,
       "rlPolicyDscpRemarkEntry": rlPolicyDscpRemarkEntry,
       "rlPolicyRmOldDscp": rlPolicyRmOldDscp,
       "rlPolicyRmNewDscp": rlPolicyRmNewDscp,
       "rlPolicyDscpRemarkStatus": rlPolicyDscpRemarkStatus,
       "rlPolicyDscpMutationTable": rlPolicyDscpMutationTable,
       "rlPolicyDscpMutationEntry": rlPolicyDscpMutationEntry,
       "rlPolicyOldDscp": rlPolicyOldDscp,
       "rlPolicyNewDscp": rlPolicyNewDscp,
       "rlPolicyDscpMutationStatus": rlPolicyDscpMutationStatus,
       "rlPolicyTrustModeTable": rlPolicyTrustModeTable,
       "rlPolicyTrustModeEntry": rlPolicyTrustModeEntry,
       "rlPolicyTrustModePortNumber": rlPolicyTrustModePortNumber,
       "rlPolicyTrustModePortState": rlPolicyTrustModePortState,
       "rlPolicyDscpVptTable": rlPolicyDscpVptTable,
       "rlPolicyDscpVptEntry": rlPolicyDscpVptEntry,
       "rlPolicyDscpValue": rlPolicyDscpValue,
       "rlPolicyVptValue": rlPolicyVptValue,
       "rlPolicyDscpVptStatus": rlPolicyDscpVptStatus,
       "rlPolicyDscpToDpTable": rlPolicyDscpToDpTable,
       "rlPolicyDscpToDpEntry": rlPolicyDscpToDpEntry,
       "rlPolicyDscp": rlPolicyDscp,
       "rlPolicyDp": rlPolicyDp,
       "rlPolicyDscpToDpStatus": rlPolicyDscpToDpStatus,
       "rlPolicyDefaultForwardingTable": rlPolicyDefaultForwardingTable,
       "rlPolicyDefaultForwardingEntry": rlPolicyDefaultForwardingEntry,
       "rlPolicyDefaultForwardingIndex": rlPolicyDefaultForwardingIndex,
       "rlPolicyDefaultForwardingPortList": rlPolicyDefaultForwardingPortList,
       "rlPolicyDefaultForwardingVlanId1To1024": rlPolicyDefaultForwardingVlanId1To1024,
       "rlPolicyDefaultForwardingVlanId1025To2048": rlPolicyDefaultForwardingVlanId1025To2048,
       "rlPolicyDefaultForwardingVlanId2049To3072": rlPolicyDefaultForwardingVlanId2049To3072,
       "rlPolicyDefaultForwardingVlanId3073To4096": rlPolicyDefaultForwardingVlanId3073To4096,
       "rlPolicyDefaultForwardingLayer": rlPolicyDefaultForwardingLayer,
       "rlPolicyDefaultForwardingAction": rlPolicyDefaultForwardingAction,
       "rlPolicyDefaultForwardingStatus": rlPolicyDefaultForwardingStatus,
       "rlPolicyDefaultForwardingProtocol": rlPolicyDefaultForwardingProtocol,
       "rlPolicyStatistics": rlPolicyStatistics,
       "rlPolicyPortPolicyStatisticsTable": rlPolicyPortPolicyStatisticsTable,
       "rlPolicyPortPolicyStatisticsEntry": rlPolicyPortPolicyStatisticsEntry,
       "rlPolicyPortPolicyStatisticsIfIndex": rlPolicyPortPolicyStatisticsIfIndex,
       "rlPolicyPortPolicyStatisticsCntrType": rlPolicyPortPolicyStatisticsCntrType,
       "rlPolicyPolicyStatisticsCntrSize": rlPolicyPolicyStatisticsCntrSize,
       "rlPolicyPolicyStatisticsEnableCounting": rlPolicyPolicyStatisticsEnableCounting,
       "rlPolicyPolicyStatisticsCounterValue": rlPolicyPolicyStatisticsCounterValue,
       "rlPolicyOutQueueStatisticsTable": rlPolicyOutQueueStatisticsTable,
       "rlPolicyOutQueueStatisticsEntry": rlPolicyOutQueueStatisticsEntry,
       "rlPolicyOutQueueStatisticsCountrID": rlPolicyOutQueueStatisticsCountrID,
       "rlPolicyOutQueueStatisticsIfIndexList": rlPolicyOutQueueStatisticsIfIndexList,
       "rlPolicyOutQueueStatisticsPortAll": rlPolicyOutQueueStatisticsPortAll,
       "rlPolicyOutQueueStatisticsVlan": rlPolicyOutQueueStatisticsVlan,
       "rlPolicyOutQueueStatisticsVlanAll": rlPolicyOutQueueStatisticsVlanAll,
       "rlPolicyOutQueueStatisticsQueue": rlPolicyOutQueueStatisticsQueue,
       "rlPolicyOutQueueStatisticsQueueAll": rlPolicyOutQueueStatisticsQueueAll,
       "rlPolicyOutQueueStatisticsDP": rlPolicyOutQueueStatisticsDP,
       "rlPolicyOutQueueStatisticsDPAll": rlPolicyOutQueueStatisticsDPAll,
       "rlPolicyOutQueueStatisticsCounterTailDropValue": rlPolicyOutQueueStatisticsCounterTailDropValue,
       "rlPolicyOutQueueStatisticsCounterAllValue": rlPolicyOutQueueStatisticsCounterAllValue,
       "rlPolicyOutQueueStatisticsCntrNumOfBits": rlPolicyOutQueueStatisticsCntrNumOfBits,
       "rlPolicyOutQueueStatisticsStatus": rlPolicyOutQueueStatisticsStatus,
       "rlPolicyGlobalStatisticsCntrsTable": rlPolicyGlobalStatisticsCntrsTable,
       "rlPolicyGlobalStatisticsCntrsEntry": rlPolicyGlobalStatisticsCntrsEntry,
       "rlPolicyGlobalStatisticsCntrsType": rlPolicyGlobalStatisticsCntrsType,
       "rlPolicyGlobalStatisticsCntrsNumOfBits": rlPolicyGlobalStatisticsCntrsNumOfBits,
       "rlPolicyGlobalStatisticsCntrsCounterValue": rlPolicyGlobalStatisticsCntrsCounterValue,
       "rlPolicyGlobalStatisticsStatus": rlPolicyGlobalStatisticsStatus,
       "rlPolicyClearCounters": rlPolicyClearCounters,
       "rlPolicyClassifierUtilization": rlPolicyClassifierUtilization,
       "rlPolicyClassifierUtilizationTable": rlPolicyClassifierUtilizationTable,
       "rlPolicyClassifierUtilizationEntry": rlPolicyClassifierUtilizationEntry,
       "rlPolicyClassifierUtilizationUnitId": rlPolicyClassifierUtilizationUnitId,
       "rlPolicyClassifierUtilizationPercent": rlPolicyClassifierUtilizationPercent,
       "rlPolicyClassifierUtilizationRulesNumber": rlPolicyClassifierUtilizationRulesNumber,
       "rlPolicyIsTCAvailable": rlPolicyIsTCAvailable,
       "rlPolicyTimeBasedAcl": rlPolicyTimeBasedAcl,
       "rlPolicyTimeBasedAclTable": rlPolicyTimeBasedAclTable,
       "rlPolicyTimeBasedAclEntry": rlPolicyTimeBasedAclEntry,
       "rlPolicyTimeBasedAclRangeIndex": rlPolicyTimeBasedAclRangeIndex,
       "rlPolicyTimeBasedAclRangeName": rlPolicyTimeBasedAclRangeName,
       "rlPolicyTimeBasedAclAbsStart": rlPolicyTimeBasedAclAbsStart,
       "rlPolicyTimeBasedAclAbsEnd": rlPolicyTimeBasedAclAbsEnd,
       "rlPolicyTimeBasedAclStatus": rlPolicyTimeBasedAclStatus,
       "rlPolicyTimeBasedAclPeriodicTable": rlPolicyTimeBasedAclPeriodicTable,
       "rlPolicyTimeBasedAclPeriodicEntry": rlPolicyTimeBasedAclPeriodicEntry,
       "rlPolicyTimeBasedAclPeriodicIndex": rlPolicyTimeBasedAclPeriodicIndex,
       "rlPolicyTimeBasedAclPeriodicWeekList": rlPolicyTimeBasedAclPeriodicWeekList,
       "rlPolicyTimeBasedAclPeriodicStart": rlPolicyTimeBasedAclPeriodicStart,
       "rlPolicyTimeBasedAclPeriodicEnd": rlPolicyTimeBasedAclPeriodicEnd,
       "rlPolicyTimeBasedAclPeriodicStatus": rlPolicyTimeBasedAclPeriodicStatus,
       "rlPolicyCPUSafeGuardEnable": rlPolicyCPUSafeGuardEnable}
)
