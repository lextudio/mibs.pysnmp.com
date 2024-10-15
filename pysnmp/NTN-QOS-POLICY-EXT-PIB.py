# SNMP MIB module (NTN-QOS-POLICY-EXT-PIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTN-QOS-POLICY-EXT-PIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:39 2024
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

(PolicyInstanceId,
 RoleCombination) = mibBuilder.importSymbols(
    "POLICY-FRAMEWORK-PIB",
    "PolicyInstanceId",
    "RoleCombination")

(QosIeee802Cos,
 qos802AceEntry,
 qos802DscpMappingEntry) = mibBuilder.importSymbols(
    "QOS-POLICY-802-PIB",
    "QosIeee802Cos",
    "qos802AceEntry",
    "qos802DscpMappingEntry")

(QosInterfaceQueueCount,
 qosActionEntry,
 qosInterfaceTypeEntry) = mibBuilder.importSymbols(
    "QOS-POLICY-IP-PIB",
    "QosInterfaceQueueCount",
    "qosActionEntry",
    "qosInterfaceTypeEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

ntnQosPolicyExtPib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4)
)
ntnQosPolicyExtPib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DropPrecedence(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_NtnQosPolicyExtPibClasses_ObjectIdentity = ObjectIdentity
ntnQosPolicyExtPibClasses = _NtnQosPolicyExtPibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1)
)
_NtnQosIfParametersExt_ObjectIdentity = ObjectIdentity
ntnQosIfParametersExt = _NtnQosIfParametersExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1)
)
_NtnQosIfPriAssignmentTable_Object = MibTable
ntnQosIfPriAssignmentTable = _NtnQosIfPriAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentTable.setStatus("current")
_NtnQosIfPriAssignmentEntry_Object = MibTableRow
ntnQosIfPriAssignmentEntry = _NtnQosIfPriAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1)
)
ntnQosIfPriAssignmentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentId"),
)
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentEntry.setStatus("current")
_NtnQosIfPriAssignmentId_Type = PolicyInstanceId
_NtnQosIfPriAssignmentId_Object = MibTableColumn
ntnQosIfPriAssignmentId = _NtnQosIfPriAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 1),
    _NtnQosIfPriAssignmentId_Type()
)
ntnQosIfPriAssignmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentId.setStatus("current")
_NtnQosIfPriAssignmentRoles_Type = RoleCombination
_NtnQosIfPriAssignmentRoles_Object = MibTableColumn
ntnQosIfPriAssignmentRoles = _NtnQosIfPriAssignmentRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 2),
    _NtnQosIfPriAssignmentRoles_Type()
)
ntnQosIfPriAssignmentRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentRoles.setStatus("current")
_NtnQosIfPriAssignmentPri_Type = QosIeee802Cos
_NtnQosIfPriAssignmentPri_Object = MibTableColumn
ntnQosIfPriAssignmentPri = _NtnQosIfPriAssignmentPri_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 3),
    _NtnQosIfPriAssignmentPri_Type()
)
ntnQosIfPriAssignmentPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentPri.setStatus("current")
_NtnQosIfPriAssignmentQueue_Type = QosInterfaceQueueCount
_NtnQosIfPriAssignmentQueue_Object = MibTableColumn
ntnQosIfPriAssignmentQueue = _NtnQosIfPriAssignmentQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 4),
    _NtnQosIfPriAssignmentQueue_Type()
)
ntnQosIfPriAssignmentQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentQueue.setStatus("current")


class _NtnQosIfPriAssignmentStorageType_Type(StorageType):
    """Custom type ntnQosIfPriAssignmentStorageType based on StorageType"""


_NtnQosIfPriAssignmentStorageType_Object = MibTableColumn
ntnQosIfPriAssignmentStorageType = _NtnQosIfPriAssignmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 5),
    _NtnQosIfPriAssignmentStorageType_Type()
)
ntnQosIfPriAssignmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentStorageType.setStatus("current")
_NtnQosIfPriAssignmentStatus_Type = RowStatus
_NtnQosIfPriAssignmentStatus_Object = MibTableColumn
ntnQosIfPriAssignmentStatus = _NtnQosIfPriAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 1, 1, 6),
    _NtnQosIfPriAssignmentStatus_Type()
)
ntnQosIfPriAssignmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentStatus.setStatus("current")
_NtnQosInterfaceTypeExtTable_Object = MibTable
ntnQosInterfaceTypeExtTable = _NtnQosInterfaceTypeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeExtTable.setStatus("current")
_NtnQosInterfaceTypeExtEntry_Object = MibTableRow
ntnQosInterfaceTypeExtEntry = _NtnQosInterfaceTypeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeExtEntry.setStatus("current")


class _NtnQosInterfaceTypeExtIfClass_Type(Integer32):
    """Custom type ntnQosInterfaceTypeExtIfClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("core", 1))
    )


_NtnQosInterfaceTypeExtIfClass_Type.__name__ = "Integer32"
_NtnQosInterfaceTypeExtIfClass_Object = MibTableColumn
ntnQosInterfaceTypeExtIfClass = _NtnQosInterfaceTypeExtIfClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 2, 1, 1),
    _NtnQosInterfaceTypeExtIfClass_Type()
)
ntnQosInterfaceTypeExtIfClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeExtIfClass.setStatus("current")
_NtnQosIfDscpMappingExtTable_Object = MibTable
ntnQosIfDscpMappingExtTable = _NtnQosIfDscpMappingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ntnQosIfDscpMappingExtTable.setStatus("current")
_NtnQosIfDscpMappingExtEntry_Object = MibTableRow
ntnQosIfDscpMappingExtEntry = _NtnQosIfDscpMappingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntnQosIfDscpMappingExtEntry.setStatus("current")
_NtnQosIfDscpMappingExtDropPrec_Type = DropPrecedence
_NtnQosIfDscpMappingExtDropPrec_Object = MibTableColumn
ntnQosIfDscpMappingExtDropPrec = _NtnQosIfDscpMappingExtDropPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 1, 3, 1, 1),
    _NtnQosIfDscpMappingExtDropPrec_Type()
)
ntnQosIfDscpMappingExtDropPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfDscpMappingExtDropPrec.setStatus("current")
_NtnQosActionExt_ObjectIdentity = ObjectIdentity
ntnQosActionExt = _NtnQosActionExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2)
)
_NtnQosActionExtTable_Object = MibTable
ntnQosActionExtTable = _NtnQosActionExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntnQosActionExtTable.setStatus("current")
_NtnQosActionExtEntry_Object = MibTableRow
ntnQosActionExtEntry = _NtnQosActionExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosActionExtEntry.setStatus("current")


class _NtnQosActionExtAssignFlowId_Type(Integer32):
    """Custom type ntnQosActionExtAssignFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_NtnQosActionExtAssignFlowId_Type.__name__ = "Integer32"
_NtnQosActionExtAssignFlowId_Object = MibTableColumn
ntnQosActionExtAssignFlowId = _NtnQosActionExtAssignFlowId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 1),
    _NtnQosActionExtAssignFlowId_Type()
)
ntnQosActionExtAssignFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtAssignFlowId.setStatus("current")
_NtnQosActionExtCopyToCpu_Type = TruthValue
_NtnQosActionExtCopyToCpu_Object = MibTableColumn
ntnQosActionExtCopyToCpu = _NtnQosActionExtCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 2),
    _NtnQosActionExtCopyToCpu_Type()
)
ntnQosActionExtCopyToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtCopyToCpu.setStatus("current")
_NtnQosActionExtMirrorFrame_Type = TruthValue
_NtnQosActionExtMirrorFrame_Object = MibTableColumn
ntnQosActionExtMirrorFrame = _NtnQosActionExtMirrorFrame_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 3),
    _NtnQosActionExtMirrorFrame_Type()
)
ntnQosActionExtMirrorFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtMirrorFrame.setStatus("current")


class _NtnQosActionExtSetDropPrec_Type(Integer32):
    """Custom type ntnQosActionExtSetDropPrec based on Integer32"""
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
        *(("dropPrec1", 1),
          ("dropPrec2", 2),
          ("dropPrec3", 3),
          ("dropPrec4", 4),
          ("dropPrec5", 5),
          ("dropPrec6", 6),
          ("dropPrec7", 7),
          ("dropPrec8", 8),
          ("ignore", 10),
          ("useDefault", 9),
          ("useEgressMap", 11))
    )


_NtnQosActionExtSetDropPrec_Type.__name__ = "Integer32"
_NtnQosActionExtSetDropPrec_Object = MibTableColumn
ntnQosActionExtSetDropPrec = _NtnQosActionExtSetDropPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 4),
    _NtnQosActionExtSetDropPrec_Type()
)
ntnQosActionExtSetDropPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtSetDropPrec.setStatus("current")


class _NtnQosActionExtUpdatePri_Type(Integer32):
    """Custom type ntnQosActionExtUpdatePri based on Integer32"""
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
        *(("ignore", 10),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8),
          ("useDefault", 9),
          ("useEgressMap", 11))
    )


_NtnQosActionExtUpdatePri_Type.__name__ = "Integer32"
_NtnQosActionExtUpdatePri_Object = MibTableColumn
ntnQosActionExtUpdatePri = _NtnQosActionExtUpdatePri_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 5),
    _NtnQosActionExtUpdatePri_Type()
)
ntnQosActionExtUpdatePri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtUpdatePri.setStatus("current")


class _NtnQosActionExtMirrorDirection_Type(Integer32):
    """Custom type ntnQosActionExtMirrorDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_NtnQosActionExtMirrorDirection_Type.__name__ = "Integer32"
_NtnQosActionExtMirrorDirection_Object = MibTableColumn
ntnQosActionExtMirrorDirection = _NtnQosActionExtMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 2, 1, 1, 6),
    _NtnQosActionExtMirrorDirection_Type()
)
ntnQosActionExtMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosActionExtMirrorDirection.setStatus("current")
_NtnQos802FilterExt_ObjectIdentity = ObjectIdentity
ntnQos802FilterExt = _NtnQos802FilterExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3)
)
_NtnQos802FilterExtTable_Object = MibTable
ntnQos802FilterExtTable = _NtnQos802FilterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntnQos802FilterExtTable.setStatus("current")
_NtnQos802FilterExtEntry_Object = MibTableRow
ntnQos802FilterExtEntry = _NtnQos802FilterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQos802FilterExtEntry.setStatus("current")


class _NtnQos802FilterDscp_Type(Integer32):
    """Custom type ntnQos802FilterDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_NtnQos802FilterDscp_Type.__name__ = "Integer32"
_NtnQos802FilterDscp_Object = MibTableColumn
ntnQos802FilterDscp = _NtnQos802FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 1),
    _NtnQos802FilterDscp_Type()
)
ntnQos802FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterDscp.setStatus("current")


class _NtnQos802FilterProtocol_Type(Integer32):
    """Custom type ntnQos802FilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQos802FilterProtocol_Type.__name__ = "Integer32"
_NtnQos802FilterProtocol_Object = MibTableColumn
ntnQos802FilterProtocol = _NtnQos802FilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 2),
    _NtnQos802FilterProtocol_Type()
)
ntnQos802FilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterProtocol.setStatus("current")


class _NtnQos802FilterDstL4PortMin_Type(Integer32):
    """Custom type ntnQos802FilterDstL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQos802FilterDstL4PortMin_Type.__name__ = "Integer32"
_NtnQos802FilterDstL4PortMin_Object = MibTableColumn
ntnQos802FilterDstL4PortMin = _NtnQos802FilterDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 3),
    _NtnQos802FilterDstL4PortMin_Type()
)
ntnQos802FilterDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterDstL4PortMin.setStatus("current")


class _NtnQos802FilterDstL4PortMax_Type(Integer32):
    """Custom type ntnQos802FilterDstL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQos802FilterDstL4PortMax_Type.__name__ = "Integer32"
_NtnQos802FilterDstL4PortMax_Object = MibTableColumn
ntnQos802FilterDstL4PortMax = _NtnQos802FilterDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 4),
    _NtnQos802FilterDstL4PortMax_Type()
)
ntnQos802FilterDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterDstL4PortMax.setStatus("current")


class _NtnQos802FilterSrcL4PortMin_Type(Integer32):
    """Custom type ntnQos802FilterSrcL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQos802FilterSrcL4PortMin_Type.__name__ = "Integer32"
_NtnQos802FilterSrcL4PortMin_Object = MibTableColumn
ntnQos802FilterSrcL4PortMin = _NtnQos802FilterSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 5),
    _NtnQos802FilterSrcL4PortMin_Type()
)
ntnQos802FilterSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterSrcL4PortMin.setStatus("current")


class _NtnQos802FilterSrcL4PortMax_Type(Integer32):
    """Custom type ntnQos802FilterSrcL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQos802FilterSrcL4PortMax_Type.__name__ = "Integer32"
_NtnQos802FilterSrcL4PortMax_Object = MibTableColumn
ntnQos802FilterSrcL4PortMax = _NtnQos802FilterSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 6),
    _NtnQos802FilterSrcL4PortMax_Type()
)
ntnQos802FilterSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterSrcL4PortMax.setStatus("current")


class _NtnQos802FilterVlanIdSet_Type(OctetString):
    """Custom type ntnQos802FilterVlanIdSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NtnQos802FilterVlanIdSet_Type.__name__ = "OctetString"
_NtnQos802FilterVlanIdSet_Object = MibTableColumn
ntnQos802FilterVlanIdSet = _NtnQos802FilterVlanIdSet_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 1, 3, 1, 1, 7),
    _NtnQos802FilterVlanIdSet_Type()
)
ntnQos802FilterVlanIdSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQos802FilterVlanIdSet.setStatus("current")
_NtnQosPolicyExtPibConformance_ObjectIdentity = ObjectIdentity
ntnQosPolicyExtPibConformance = _NtnQosPolicyExtPibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2)
)
_NtnQosPolicyExtPibCompliances_ObjectIdentity = ObjectIdentity
ntnQosPolicyExtPibCompliances = _NtnQosPolicyExtPibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 1)
)
_NtnQosPolicyExtPibGroups_ObjectIdentity = ObjectIdentity
ntnQosPolicyExtPibGroups = _NtnQosPolicyExtPibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2)
)
qosInterfaceTypeEntry.registerAugmentions(
    ("NTN-QOS-POLICY-EXT-PIB",
     "ntnQosInterfaceTypeExtEntry")
)
ntnQosInterfaceTypeExtEntry.setIndexNames(*qosInterfaceTypeEntry.getIndexNames())
qos802DscpMappingEntry.registerAugmentions(
    ("NTN-QOS-POLICY-EXT-PIB",
     "ntnQosIfDscpMappingExtEntry")
)
ntnQosIfDscpMappingExtEntry.setIndexNames(*qos802DscpMappingEntry.getIndexNames())
qosActionEntry.registerAugmentions(
    ("NTN-QOS-POLICY-EXT-PIB",
     "ntnQosActionExtEntry")
)
ntnQosActionExtEntry.setIndexNames(*qosActionEntry.getIndexNames())
qos802AceEntry.registerAugmentions(
    ("NTN-QOS-POLICY-EXT-PIB",
     "ntnQos802FilterExtEntry")
)
ntnQos802FilterExtEntry.setIndexNames(*qos802AceEntry.getIndexNames())

# Managed Objects groups

ntnQosIfPriAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2, 1)
)
ntnQosIfPriAssignmentGroup.setObjects(
      *(("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentRoles"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentPri"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentQueue"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentStorageType"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfPriAssignmentStatus"))
)
if mibBuilder.loadTexts:
    ntnQosIfPriAssignmentGroup.setStatus("current")

ntnQosInterfaceTypeExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2, 2)
)
ntnQosInterfaceTypeExtGroup.setObjects(
    ("NTN-QOS-POLICY-EXT-PIB", "ntnQosInterfaceTypeExtIfClass")
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeExtGroup.setStatus("current")

ntnQosIfDscpMappingExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2, 3)
)
ntnQosIfDscpMappingExtGroup.setObjects(
    ("NTN-QOS-POLICY-EXT-PIB", "ntnQosIfDscpMappingExtDropPrec")
)
if mibBuilder.loadTexts:
    ntnQosIfDscpMappingExtGroup.setStatus("current")

ntnQosActionExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2, 4)
)
ntnQosActionExtGroup.setObjects(
      *(("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtAssignFlowId"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtCopyToCpu"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtMirrorFrame"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtSetDropPrec"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtUpdatePri"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQosActionExtMirrorDirection"))
)
if mibBuilder.loadTexts:
    ntnQosActionExtGroup.setStatus("current")

ntnQos802FilterExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 2, 5)
)
ntnQos802FilterExtGroup.setObjects(
      *(("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterDscp"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterProtocol"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterDstL4PortMin"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterDstL4PortMax"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterSrcL4PortMin"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterSrcL4PortMax"),
        ("NTN-QOS-POLICY-EXT-PIB", "ntnQos802FilterVlanIdSet"))
)
if mibBuilder.loadTexts:
    ntnQos802FilterExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntnQosPolicyExtPibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosPolicyExtPibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTN-QOS-POLICY-EXT-PIB",
    **{"DropPrecedence": DropPrecedence,
       "ntnQosPolicyExtPib": ntnQosPolicyExtPib,
       "ntnQosPolicyExtPibClasses": ntnQosPolicyExtPibClasses,
       "ntnQosIfParametersExt": ntnQosIfParametersExt,
       "ntnQosIfPriAssignmentTable": ntnQosIfPriAssignmentTable,
       "ntnQosIfPriAssignmentEntry": ntnQosIfPriAssignmentEntry,
       "ntnQosIfPriAssignmentId": ntnQosIfPriAssignmentId,
       "ntnQosIfPriAssignmentRoles": ntnQosIfPriAssignmentRoles,
       "ntnQosIfPriAssignmentPri": ntnQosIfPriAssignmentPri,
       "ntnQosIfPriAssignmentQueue": ntnQosIfPriAssignmentQueue,
       "ntnQosIfPriAssignmentStorageType": ntnQosIfPriAssignmentStorageType,
       "ntnQosIfPriAssignmentStatus": ntnQosIfPriAssignmentStatus,
       "ntnQosInterfaceTypeExtTable": ntnQosInterfaceTypeExtTable,
       "ntnQosInterfaceTypeExtEntry": ntnQosInterfaceTypeExtEntry,
       "ntnQosInterfaceTypeExtIfClass": ntnQosInterfaceTypeExtIfClass,
       "ntnQosIfDscpMappingExtTable": ntnQosIfDscpMappingExtTable,
       "ntnQosIfDscpMappingExtEntry": ntnQosIfDscpMappingExtEntry,
       "ntnQosIfDscpMappingExtDropPrec": ntnQosIfDscpMappingExtDropPrec,
       "ntnQosActionExt": ntnQosActionExt,
       "ntnQosActionExtTable": ntnQosActionExtTable,
       "ntnQosActionExtEntry": ntnQosActionExtEntry,
       "ntnQosActionExtAssignFlowId": ntnQosActionExtAssignFlowId,
       "ntnQosActionExtCopyToCpu": ntnQosActionExtCopyToCpu,
       "ntnQosActionExtMirrorFrame": ntnQosActionExtMirrorFrame,
       "ntnQosActionExtSetDropPrec": ntnQosActionExtSetDropPrec,
       "ntnQosActionExtUpdatePri": ntnQosActionExtUpdatePri,
       "ntnQosActionExtMirrorDirection": ntnQosActionExtMirrorDirection,
       "ntnQos802FilterExt": ntnQos802FilterExt,
       "ntnQos802FilterExtTable": ntnQos802FilterExtTable,
       "ntnQos802FilterExtEntry": ntnQos802FilterExtEntry,
       "ntnQos802FilterDscp": ntnQos802FilterDscp,
       "ntnQos802FilterProtocol": ntnQos802FilterProtocol,
       "ntnQos802FilterDstL4PortMin": ntnQos802FilterDstL4PortMin,
       "ntnQos802FilterDstL4PortMax": ntnQos802FilterDstL4PortMax,
       "ntnQos802FilterSrcL4PortMin": ntnQos802FilterSrcL4PortMin,
       "ntnQos802FilterSrcL4PortMax": ntnQos802FilterSrcL4PortMax,
       "ntnQos802FilterVlanIdSet": ntnQos802FilterVlanIdSet,
       "ntnQosPolicyExtPibConformance": ntnQosPolicyExtPibConformance,
       "ntnQosPolicyExtPibCompliances": ntnQosPolicyExtPibCompliances,
       "ntnQosPolicyExtPibCompliance": ntnQosPolicyExtPibCompliance,
       "ntnQosPolicyExtPibGroups": ntnQosPolicyExtPibGroups,
       "ntnQosIfPriAssignmentGroup": ntnQosIfPriAssignmentGroup,
       "ntnQosInterfaceTypeExtGroup": ntnQosInterfaceTypeExtGroup,
       "ntnQosIfDscpMappingExtGroup": ntnQosIfDscpMappingExtGroup,
       "ntnQosActionExtGroup": ntnQosActionExtGroup,
       "ntnQos802FilterExtGroup": ntnQos802FilterExtGroup}
)
