# SNMP MIB module (QOS-POLICY-IP-PIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOS-POLICY-IP-PIB
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

qosPolicyIpPib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class PolicyInstanceIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class QosInterfaceQueueCount(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_QosPolicyGenPibClasses_ObjectIdentity = ObjectIdentity
qosPolicyGenPibClasses = _QosPolicyGenPibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1)
)
_QosIfParameters_ObjectIdentity = ObjectIdentity
qosIfParameters = _QosIfParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1)
)
_QosInterfaceTypeTable_Object = MibTable
qosInterfaceTypeTable = _QosInterfaceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qosInterfaceTypeTable.setStatus("current")
_QosInterfaceTypeEntry_Object = MibTableRow
qosInterfaceTypeEntry = _QosInterfaceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1)
)
qosInterfaceTypeEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosInterfaceTypeId"),
)
if mibBuilder.loadTexts:
    qosInterfaceTypeEntry.setStatus("current")
_QosInterfaceTypeId_Type = PolicyInstanceId
_QosInterfaceTypeId_Object = MibTableColumn
qosInterfaceTypeId = _QosInterfaceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 1),
    _QosInterfaceTypeId_Type()
)
qosInterfaceTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosInterfaceTypeId.setStatus("current")
_QosInterfaceTypeRoles_Type = RoleCombination
_QosInterfaceTypeRoles_Object = MibTableColumn
qosInterfaceTypeRoles = _QosInterfaceTypeRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 2),
    _QosInterfaceTypeRoles_Type()
)
qosInterfaceTypeRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceTypeRoles.setStatus("current")
_QosInterfaceTypeQueueSet_Type = PolicyInstanceId
_QosInterfaceTypeQueueSet_Object = MibTableColumn
qosInterfaceTypeQueueSet = _QosInterfaceTypeQueueSet_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 3),
    _QosInterfaceTypeQueueSet_Type()
)
qosInterfaceTypeQueueSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceTypeQueueSet.setStatus("current")


class _QosInterfaceTypeCapabilities_Type(Bits):
    """Custom type qosInterfaceTypeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hybridQueuingDiscipline", 6),
          ("input802Classification", 3),
          ("inputIpClassification", 1),
          ("other", 0),
          ("output802Classification", 4),
          ("outputIpClassification", 2),
          ("singleQueuingDiscipline", 5))
    )

_QosInterfaceTypeCapabilities_Type.__name__ = "Bits"
_QosInterfaceTypeCapabilities_Object = MibTableColumn
qosInterfaceTypeCapabilities = _QosInterfaceTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 4),
    _QosInterfaceTypeCapabilities_Type()
)
qosInterfaceTypeCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceTypeCapabilities.setStatus("current")


class _QosInterfaceTypeStorageType_Type(StorageType):
    """Custom type qosInterfaceTypeStorageType based on StorageType"""


_QosInterfaceTypeStorageType_Object = MibTableColumn
qosInterfaceTypeStorageType = _QosInterfaceTypeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 5),
    _QosInterfaceTypeStorageType_Type()
)
qosInterfaceTypeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceTypeStorageType.setStatus("current")
_QosInterfaceTypeStatus_Type = RowStatus
_QosInterfaceTypeStatus_Object = MibTableColumn
qosInterfaceTypeStatus = _QosInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 1, 1, 6),
    _QosInterfaceTypeStatus_Type()
)
qosInterfaceTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosInterfaceTypeStatus.setStatus("current")
_QosIfQueueTable_Object = MibTable
qosIfQueueTable = _QosIfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qosIfQueueTable.setStatus("current")
_QosIfQueueEntry_Object = MibTableRow
qosIfQueueEntry = _QosIfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1)
)
qosIfQueueEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosIfQueueId"),
)
if mibBuilder.loadTexts:
    qosIfQueueEntry.setStatus("current")
_QosIfQueueId_Type = PolicyInstanceId
_QosIfQueueId_Object = MibTableColumn
qosIfQueueId = _QosIfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 1),
    _QosIfQueueId_Type()
)
qosIfQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfQueueId.setStatus("current")


class _QosIfQueueSetId_Type(Integer32):
    """Custom type qosIfQueueSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QosIfQueueSetId_Type.__name__ = "Integer32"
_QosIfQueueSetId_Object = MibTableColumn
qosIfQueueSetId = _QosIfQueueSetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 2),
    _QosIfQueueSetId_Type()
)
qosIfQueueSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueSetId.setStatus("current")
_QosIfQueueIndex_Type = QosInterfaceQueueCount
_QosIfQueueIndex_Object = MibTableColumn
qosIfQueueIndex = _QosIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 3),
    _QosIfQueueIndex_Type()
)
qosIfQueueIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueIndex.setStatus("current")


class _QosIfQueueGenDiscipline_Type(Integer32):
    """Custom type qosIfQueueGenDiscipline based on Integer32"""
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
        *(("fifo", 2),
          ("fq", 4),
          ("other", 1),
          ("pq", 3),
          ("wfq", 5))
    )


_QosIfQueueGenDiscipline_Type.__name__ = "Integer32"
_QosIfQueueGenDiscipline_Object = MibTableColumn
qosIfQueueGenDiscipline = _QosIfQueueGenDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 4),
    _QosIfQueueGenDiscipline_Type()
)
qosIfQueueGenDiscipline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueGenDiscipline.setStatus("current")
_QosIfQueueExtDiscipline_Type = ObjectIdentifier
_QosIfQueueExtDiscipline_Object = MibTableColumn
qosIfQueueExtDiscipline = _QosIfQueueExtDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 5),
    _QosIfQueueExtDiscipline_Type()
)
qosIfQueueExtDiscipline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueExtDiscipline.setStatus("current")
_QosIfQueueDrainSize_Type = Unsigned32
_QosIfQueueDrainSize_Object = MibTableColumn
qosIfQueueDrainSize = _QosIfQueueDrainSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 6),
    _QosIfQueueDrainSize_Type()
)
qosIfQueueDrainSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueDrainSize.setStatus("current")
_QosIfQueueAbsBandwidth_Type = Unsigned32
_QosIfQueueAbsBandwidth_Object = MibTableColumn
qosIfQueueAbsBandwidth = _QosIfQueueAbsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 7),
    _QosIfQueueAbsBandwidth_Type()
)
qosIfQueueAbsBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueAbsBandwidth.setStatus("current")


class _QosIfQueueBandwidthAllocation_Type(Integer32):
    """Custom type qosIfQueueBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("relative", 2))
    )


_QosIfQueueBandwidthAllocation_Type.__name__ = "Integer32"
_QosIfQueueBandwidthAllocation_Object = MibTableColumn
qosIfQueueBandwidthAllocation = _QosIfQueueBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 8),
    _QosIfQueueBandwidthAllocation_Type()
)
qosIfQueueBandwidthAllocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueBandwidthAllocation.setStatus("current")
_QosIfQueueServiceOrder_Type = QosInterfaceQueueCount
_QosIfQueueServiceOrder_Object = MibTableColumn
qosIfQueueServiceOrder = _QosIfQueueServiceOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 9),
    _QosIfQueueServiceOrder_Type()
)
qosIfQueueServiceOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueServiceOrder.setStatus("current")
_QosIfQueueSize_Type = Integer32
_QosIfQueueSize_Object = MibTableColumn
qosIfQueueSize = _QosIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 10),
    _QosIfQueueSize_Type()
)
qosIfQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueSize.setStatus("current")


class _QosIfQueueStorageType_Type(StorageType):
    """Custom type qosIfQueueStorageType based on StorageType"""


_QosIfQueueStorageType_Object = MibTableColumn
qosIfQueueStorageType = _QosIfQueueStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 11),
    _QosIfQueueStorageType_Type()
)
qosIfQueueStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueStorageType.setStatus("current")
_QosIfQueueStatus_Type = RowStatus
_QosIfQueueStatus_Object = MibTableColumn
qosIfQueueStatus = _QosIfQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 2, 1, 12),
    _QosIfQueueStatus_Type()
)
qosIfQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfQueueStatus.setStatus("current")
_QosIfDscpAssignmentTable_Object = MibTable
qosIfDscpAssignmentTable = _QosIfDscpAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentTable.setStatus("current")
_QosIfDscpAssignmentEntry_Object = MibTableRow
qosIfDscpAssignmentEntry = _QosIfDscpAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1)
)
qosIfDscpAssignmentEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosIfDscpAssignmentId"),
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentEntry.setStatus("current")
_QosIfDscpAssignmentId_Type = PolicyInstanceId
_QosIfDscpAssignmentId_Object = MibTableColumn
qosIfDscpAssignmentId = _QosIfDscpAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 1),
    _QosIfDscpAssignmentId_Type()
)
qosIfDscpAssignmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentId.setStatus("current")
_QosIfDscpAssignmentRoles_Type = RoleCombination
_QosIfDscpAssignmentRoles_Object = MibTableColumn
qosIfDscpAssignmentRoles = _QosIfDscpAssignmentRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 2),
    _QosIfDscpAssignmentRoles_Type()
)
qosIfDscpAssignmentRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentRoles.setStatus("current")
_QosIfDscpAssignmentDscp_Type = Dscp
_QosIfDscpAssignmentDscp_Object = MibTableColumn
qosIfDscpAssignmentDscp = _QosIfDscpAssignmentDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 3),
    _QosIfDscpAssignmentDscp_Type()
)
qosIfDscpAssignmentDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentDscp.setStatus("current")
_QosIfDscpAssignmentQueue_Type = QosInterfaceQueueCount
_QosIfDscpAssignmentQueue_Object = MibTableColumn
qosIfDscpAssignmentQueue = _QosIfDscpAssignmentQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 4),
    _QosIfDscpAssignmentQueue_Type()
)
qosIfDscpAssignmentQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentQueue.setStatus("current")


class _QosIfDscpAssignmentStorageType_Type(StorageType):
    """Custom type qosIfDscpAssignmentStorageType based on StorageType"""


_QosIfDscpAssignmentStorageType_Object = MibTableColumn
qosIfDscpAssignmentStorageType = _QosIfDscpAssignmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 5),
    _QosIfDscpAssignmentStorageType_Type()
)
qosIfDscpAssignmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentStorageType.setStatus("current")
_QosIfDscpAssignmentStatus_Type = RowStatus
_QosIfDscpAssignmentStatus_Object = MibTableColumn
qosIfDscpAssignmentStatus = _QosIfDscpAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 1, 3, 1, 6),
    _QosIfDscpAssignmentStatus_Type()
)
qosIfDscpAssignmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentStatus.setStatus("current")
_QosMeter_ObjectIdentity = ObjectIdentity
qosMeter = _QosMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2)
)
_QosMeterTable_Object = MibTable
qosMeterTable = _QosMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qosMeterTable.setStatus("current")
_QosMeterEntry_Object = MibTableRow
qosMeterEntry = _QosMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1)
)
qosMeterEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosMeterId"),
)
if mibBuilder.loadTexts:
    qosMeterEntry.setStatus("current")
_QosMeterId_Type = PolicyInstanceId
_QosMeterId_Object = MibTableColumn
qosMeterId = _QosMeterId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 1),
    _QosMeterId_Type()
)
qosMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosMeterId.setStatus("current")


class _QosMeterDataSpecification_Type(Integer32):
    """Custom type qosMeterDataSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("committedData", 2),
          ("noMeterData", 1),
          ("peakData", 3))
    )


_QosMeterDataSpecification_Type.__name__ = "Integer32"
_QosMeterDataSpecification_Object = MibTableColumn
qosMeterDataSpecification = _QosMeterDataSpecification_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 2),
    _QosMeterDataSpecification_Type()
)
qosMeterDataSpecification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterDataSpecification.setStatus("current")


class _QosMeterCommittedRate_Type(Unsigned32):
    """Custom type qosMeterCommittedRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QosMeterCommittedRate_Type.__name__ = "Unsigned32"
_QosMeterCommittedRate_Object = MibTableColumn
qosMeterCommittedRate = _QosMeterCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 3),
    _QosMeterCommittedRate_Type()
)
qosMeterCommittedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterCommittedRate.setStatus("current")


class _QosMeterCommittedBurst_Type(Unsigned32):
    """Custom type qosMeterCommittedBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QosMeterCommittedBurst_Type.__name__ = "Unsigned32"
_QosMeterCommittedBurst_Object = MibTableColumn
qosMeterCommittedBurst = _QosMeterCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 4),
    _QosMeterCommittedBurst_Type()
)
qosMeterCommittedBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterCommittedBurst.setStatus("current")


class _QosMeterPeakRate_Type(Unsigned32):
    """Custom type qosMeterPeakRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QosMeterPeakRate_Type.__name__ = "Unsigned32"
_QosMeterPeakRate_Object = MibTableColumn
qosMeterPeakRate = _QosMeterPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 5),
    _QosMeterPeakRate_Type()
)
qosMeterPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterPeakRate.setStatus("current")


class _QosMeterPeakBurst_Type(Unsigned32):
    """Custom type qosMeterPeakBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_QosMeterPeakBurst_Type.__name__ = "Unsigned32"
_QosMeterPeakBurst_Object = MibTableColumn
qosMeterPeakBurst = _QosMeterPeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 6),
    _QosMeterPeakBurst_Type()
)
qosMeterPeakBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterPeakBurst.setStatus("current")
_QosMeterHighConfAction_Type = PolicyInstanceIdOrZero
_QosMeterHighConfAction_Object = MibTableColumn
qosMeterHighConfAction = _QosMeterHighConfAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 7),
    _QosMeterHighConfAction_Type()
)
qosMeterHighConfAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterHighConfAction.setStatus("current")
_QosMeterMedConfAction_Type = PolicyInstanceIdOrZero
_QosMeterMedConfAction_Object = MibTableColumn
qosMeterMedConfAction = _QosMeterMedConfAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 8),
    _QosMeterMedConfAction_Type()
)
qosMeterMedConfAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterMedConfAction.setStatus("current")
_QosMeterLowConfAction_Type = PolicyInstanceIdOrZero
_QosMeterLowConfAction_Object = MibTableColumn
qosMeterLowConfAction = _QosMeterLowConfAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 9),
    _QosMeterLowConfAction_Type()
)
qosMeterLowConfAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterLowConfAction.setStatus("current")


class _QosMeterStorageType_Type(StorageType):
    """Custom type qosMeterStorageType based on StorageType"""


_QosMeterStorageType_Object = MibTableColumn
qosMeterStorageType = _QosMeterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 10),
    _QosMeterStorageType_Type()
)
qosMeterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterStorageType.setStatus("current")
_QosMeterStatus_Type = RowStatus
_QosMeterStatus_Object = MibTableColumn
qosMeterStatus = _QosMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 11),
    _QosMeterStatus_Type()
)
qosMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterStatus.setStatus("current")


class _QosMeterLabel_Type(SnmpAdminString):
    """Custom type qosMeterLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QosMeterLabel_Type.__name__ = "SnmpAdminString"
_QosMeterLabel_Object = MibTableColumn
qosMeterLabel = _QosMeterLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 2, 1, 1, 12),
    _QosMeterLabel_Type()
)
qosMeterLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMeterLabel.setStatus("current")
_QosAction_ObjectIdentity = ObjectIdentity
qosAction = _QosAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3)
)
_QosActionTable_Object = MibTable
qosActionTable = _QosActionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qosActionTable.setStatus("current")
_QosActionEntry_Object = MibTableRow
qosActionEntry = _QosActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1)
)
qosActionEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosActionId"),
)
if mibBuilder.loadTexts:
    qosActionEntry.setStatus("current")
_QosActionId_Type = PolicyInstanceId
_QosActionId_Object = MibTableColumn
qosActionId = _QosActionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 1),
    _QosActionId_Type()
)
qosActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosActionId.setStatus("current")
_QosActionDrop_Type = TruthValue
_QosActionDrop_Object = MibTableColumn
qosActionDrop = _QosActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 2),
    _QosActionDrop_Type()
)
qosActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionDrop.setStatus("current")


class _QosActionUpdateDSCP_Type(Integer32):
    """Custom type qosActionUpdateDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_QosActionUpdateDSCP_Type.__name__ = "Integer32"
_QosActionUpdateDSCP_Object = MibTableColumn
qosActionUpdateDSCP = _QosActionUpdateDSCP_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 3),
    _QosActionUpdateDSCP_Type()
)
qosActionUpdateDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionUpdateDSCP.setStatus("current")
_QosActionMeter_Type = PolicyInstanceId
_QosActionMeter_Object = MibTableColumn
qosActionMeter = _QosActionMeter_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 4),
    _QosActionMeter_Type()
)
qosActionMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionMeter.setStatus("current")


class _QosActionStorageType_Type(StorageType):
    """Custom type qosActionStorageType based on StorageType"""


_QosActionStorageType_Object = MibTableColumn
qosActionStorageType = _QosActionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 5),
    _QosActionStorageType_Type()
)
qosActionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionStorageType.setStatus("current")
_QosActionStatus_Type = RowStatus
_QosActionStatus_Object = MibTableColumn
qosActionStatus = _QosActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 6),
    _QosActionStatus_Type()
)
qosActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionStatus.setStatus("current")


class _QosActionLabel_Type(SnmpAdminString):
    """Custom type qosActionLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QosActionLabel_Type.__name__ = "SnmpAdminString"
_QosActionLabel_Object = MibTableColumn
qosActionLabel = _QosActionLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 1, 1, 7),
    _QosActionLabel_Type()
)
qosActionLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosActionLabel.setStatus("current")
_QosTargetTable_Object = MibTable
qosTargetTable = _QosTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qosTargetTable.setStatus("current")
_QosTargetEntry_Object = MibTableRow
qosTargetEntry = _QosTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1)
)
qosTargetEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosTargetId"),
)
if mibBuilder.loadTexts:
    qosTargetEntry.setStatus("current")
_QosTargetId_Type = PolicyInstanceId
_QosTargetId_Object = MibTableColumn
qosTargetId = _QosTargetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 1),
    _QosTargetId_Type()
)
qosTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosTargetId.setStatus("current")
_QosTargetAclId_Type = PolicyInstanceId
_QosTargetAclId_Object = MibTableColumn
qosTargetAclId = _QosTargetAclId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 2),
    _QosTargetAclId_Type()
)
qosTargetAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetAclId.setStatus("current")
_QosTargetAclType_Type = ObjectIdentifier
_QosTargetAclType_Object = MibTableColumn
qosTargetAclType = _QosTargetAclType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 3),
    _QosTargetAclType_Type()
)
qosTargetAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetAclType.setStatus("current")
_QosTargetInterfaceRoles_Type = RoleCombination
_QosTargetInterfaceRoles_Object = MibTableColumn
qosTargetInterfaceRoles = _QosTargetInterfaceRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 4),
    _QosTargetInterfaceRoles_Type()
)
qosTargetInterfaceRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetInterfaceRoles.setStatus("current")


class _QosTargetInterfaceDirection_Type(Integer32):
    """Custom type qosTargetInterfaceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_QosTargetInterfaceDirection_Type.__name__ = "Integer32"
_QosTargetInterfaceDirection_Object = MibTableColumn
qosTargetInterfaceDirection = _QosTargetInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 5),
    _QosTargetInterfaceDirection_Type()
)
qosTargetInterfaceDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetInterfaceDirection.setStatus("current")
_QosTargetOrder_Type = Unsigned32
_QosTargetOrder_Object = MibTableColumn
qosTargetOrder = _QosTargetOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 6),
    _QosTargetOrder_Type()
)
qosTargetOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetOrder.setStatus("current")
_QosTargetMeter_Type = PolicyInstanceIdOrZero
_QosTargetMeter_Object = MibTableColumn
qosTargetMeter = _QosTargetMeter_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 7),
    _QosTargetMeter_Type()
)
qosTargetMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetMeter.setStatus("current")


class _QosTargetStorageType_Type(StorageType):
    """Custom type qosTargetStorageType based on StorageType"""


_QosTargetStorageType_Object = MibTableColumn
qosTargetStorageType = _QosTargetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 8),
    _QosTargetStorageType_Type()
)
qosTargetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetStorageType.setStatus("current")
_QosTargetStatus_Type = RowStatus
_QosTargetStatus_Object = MibTableColumn
qosTargetStatus = _QosTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 9),
    _QosTargetStatus_Type()
)
qosTargetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetStatus.setStatus("current")


class _QosTargetShapingParams_Type(PolicyInstanceIdOrZero):
    """Custom type qosTargetShapingParams based on PolicyInstanceIdOrZero"""
    defaultValue = 0


_QosTargetShapingParams_Object = MibTableColumn
qosTargetShapingParams = _QosTargetShapingParams_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 10),
    _QosTargetShapingParams_Type()
)
qosTargetShapingParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetShapingParams.setStatus("current")


class _QosTargetShapingGroup_Type(Unsigned32):
    """Custom type qosTargetShapingGroup based on Unsigned32"""
    defaultValue = 0


_QosTargetShapingGroup_Object = MibTableColumn
qosTargetShapingGroup = _QosTargetShapingGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 11),
    _QosTargetShapingGroup_Type()
)
qosTargetShapingGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetShapingGroup.setStatus("current")


class _QosTargetLabel_Type(SnmpAdminString):
    """Custom type qosTargetLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QosTargetLabel_Type.__name__ = "SnmpAdminString"
_QosTargetLabel_Object = MibTableColumn
qosTargetLabel = _QosTargetLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 12),
    _QosTargetLabel_Type()
)
qosTargetLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetLabel.setStatus("current")


class _QosTargetInProfileAction_Type(PolicyInstanceIdOrZero):
    """Custom type qosTargetInProfileAction based on PolicyInstanceIdOrZero"""
    defaultValue = 0


_QosTargetInProfileAction_Object = MibTableColumn
qosTargetInProfileAction = _QosTargetInProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 13),
    _QosTargetInProfileAction_Type()
)
qosTargetInProfileAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetInProfileAction.setStatus("current")


class _QosTargetOutOfProfileAction_Type(PolicyInstanceIdOrZero):
    """Custom type qosTargetOutOfProfileAction based on PolicyInstanceIdOrZero"""
    defaultValue = 0


_QosTargetOutOfProfileAction_Object = MibTableColumn
qosTargetOutOfProfileAction = _QosTargetOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 1, 3, 2, 1, 14),
    _QosTargetOutOfProfileAction_Type()
)
qosTargetOutOfProfileAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTargetOutOfProfileAction.setStatus("current")
_QosPolicyIpPibClasses_ObjectIdentity = ObjectIdentity
qosPolicyIpPibClasses = _QosPolicyIpPibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2)
)
_QosIpQos_ObjectIdentity = ObjectIdentity
qosIpQos = _QosIpQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1)
)
_QosIpAceTable_Object = MibTable
qosIpAceTable = _QosIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qosIpAceTable.setStatus("current")
_QosIpAceEntry_Object = MibTableRow
qosIpAceEntry = _QosIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1)
)
qosIpAceEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosIpAceId"),
)
if mibBuilder.loadTexts:
    qosIpAceEntry.setStatus("current")
_QosIpAceId_Type = PolicyInstanceId
_QosIpAceId_Object = MibTableColumn
qosIpAceId = _QosIpAceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 1),
    _QosIpAceId_Type()
)
qosIpAceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIpAceId.setStatus("current")
_QosIpAceDstAddr_Type = IpAddress
_QosIpAceDstAddr_Object = MibTableColumn
qosIpAceDstAddr = _QosIpAceDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 2),
    _QosIpAceDstAddr_Type()
)
qosIpAceDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceDstAddr.setStatus("current")
_QosIpAceDstAddrMask_Type = IpAddress
_QosIpAceDstAddrMask_Object = MibTableColumn
qosIpAceDstAddrMask = _QosIpAceDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 3),
    _QosIpAceDstAddrMask_Type()
)
qosIpAceDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceDstAddrMask.setStatus("current")
_QosIpAceSrcAddr_Type = IpAddress
_QosIpAceSrcAddr_Object = MibTableColumn
qosIpAceSrcAddr = _QosIpAceSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 4),
    _QosIpAceSrcAddr_Type()
)
qosIpAceSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceSrcAddr.setStatus("current")
_QosIpAceSrcAddrMask_Type = IpAddress
_QosIpAceSrcAddrMask_Object = MibTableColumn
qosIpAceSrcAddrMask = _QosIpAceSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 5),
    _QosIpAceSrcAddrMask_Type()
)
qosIpAceSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceSrcAddrMask.setStatus("current")


class _QosIpAceDscp_Type(Integer32):
    """Custom type qosIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_QosIpAceDscp_Type.__name__ = "Integer32"
_QosIpAceDscp_Object = MibTableColumn
qosIpAceDscp = _QosIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 6),
    _QosIpAceDscp_Type()
)
qosIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceDscp.setStatus("current")


class _QosIpAceProtocol_Type(Integer32):
    """Custom type qosIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosIpAceProtocol_Type.__name__ = "Integer32"
_QosIpAceProtocol_Object = MibTableColumn
qosIpAceProtocol = _QosIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 7),
    _QosIpAceProtocol_Type()
)
qosIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceProtocol.setStatus("current")


class _QosIpAceDstL4PortMin_Type(Integer32):
    """Custom type qosIpAceDstL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceDstL4PortMin_Type.__name__ = "Integer32"
_QosIpAceDstL4PortMin_Object = MibTableColumn
qosIpAceDstL4PortMin = _QosIpAceDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 8),
    _QosIpAceDstL4PortMin_Type()
)
qosIpAceDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceDstL4PortMin.setStatus("current")


class _QosIpAceDstL4PortMax_Type(Integer32):
    """Custom type qosIpAceDstL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceDstL4PortMax_Type.__name__ = "Integer32"
_QosIpAceDstL4PortMax_Object = MibTableColumn
qosIpAceDstL4PortMax = _QosIpAceDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 9),
    _QosIpAceDstL4PortMax_Type()
)
qosIpAceDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceDstL4PortMax.setStatus("current")


class _QosIpAceSrcL4PortMin_Type(Integer32):
    """Custom type qosIpAceSrcL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceSrcL4PortMin_Type.__name__ = "Integer32"
_QosIpAceSrcL4PortMin_Object = MibTableColumn
qosIpAceSrcL4PortMin = _QosIpAceSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 10),
    _QosIpAceSrcL4PortMin_Type()
)
qosIpAceSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceSrcL4PortMin.setStatus("current")


class _QosIpAceSrcL4PortMax_Type(Integer32):
    """Custom type qosIpAceSrcL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceSrcL4PortMax_Type.__name__ = "Integer32"
_QosIpAceSrcL4PortMax_Object = MibTableColumn
qosIpAceSrcL4PortMax = _QosIpAceSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 11),
    _QosIpAceSrcL4PortMax_Type()
)
qosIpAceSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceSrcL4PortMax.setStatus("current")
_QosIpAcePermit_Type = TruthValue
_QosIpAcePermit_Object = MibTableColumn
qosIpAcePermit = _QosIpAcePermit_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 12),
    _QosIpAcePermit_Type()
)
qosIpAcePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAcePermit.setStatus("current")


class _QosIpAceStorageType_Type(StorageType):
    """Custom type qosIpAceStorageType based on StorageType"""


_QosIpAceStorageType_Object = MibTableColumn
qosIpAceStorageType = _QosIpAceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 13),
    _QosIpAceStorageType_Type()
)
qosIpAceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceStorageType.setStatus("current")
_QosIpAceStatus_Type = RowStatus
_QosIpAceStatus_Object = MibTableColumn
qosIpAceStatus = _QosIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 1, 1, 14),
    _QosIpAceStatus_Type()
)
qosIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAceStatus.setStatus("current")
_QosIpAclDefinitionTable_Object = MibTable
qosIpAclDefinitionTable = _QosIpAclDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionTable.setStatus("current")
_QosIpAclDefinitionEntry_Object = MibTableRow
qosIpAclDefinitionEntry = _QosIpAclDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1)
)
qosIpAclDefinitionEntry.setIndexNames(
    (0, "QOS-POLICY-IP-PIB", "qosIpAclDefinitionId"),
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionEntry.setStatus("current")
_QosIpAclDefinitionId_Type = PolicyInstanceId
_QosIpAclDefinitionId_Object = MibTableColumn
qosIpAclDefinitionId = _QosIpAclDefinitionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 1),
    _QosIpAclDefinitionId_Type()
)
qosIpAclDefinitionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIpAclDefinitionId.setStatus("current")
_QosIpAclDefinitionAclId_Type = PolicyInstanceId
_QosIpAclDefinitionAclId_Object = MibTableColumn
qosIpAclDefinitionAclId = _QosIpAclDefinitionAclId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 2),
    _QosIpAclDefinitionAclId_Type()
)
qosIpAclDefinitionAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionAclId.setStatus("current")
_QosIpAclDefinitionAceId_Type = PolicyInstanceId
_QosIpAclDefinitionAceId_Object = MibTableColumn
qosIpAclDefinitionAceId = _QosIpAclDefinitionAceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 3),
    _QosIpAclDefinitionAceId_Type()
)
qosIpAclDefinitionAceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionAceId.setStatus("current")
_QosIpAclDefinitionAceOrder_Type = Unsigned32
_QosIpAclDefinitionAceOrder_Object = MibTableColumn
qosIpAclDefinitionAceOrder = _QosIpAclDefinitionAceOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 4),
    _QosIpAclDefinitionAceOrder_Type()
)
qosIpAclDefinitionAceOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionAceOrder.setStatus("current")


class _QosIpAclDefinitionStorageType_Type(StorageType):
    """Custom type qosIpAclDefinitionStorageType based on StorageType"""


_QosIpAclDefinitionStorageType_Object = MibTableColumn
qosIpAclDefinitionStorageType = _QosIpAclDefinitionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 5),
    _QosIpAclDefinitionStorageType_Type()
)
qosIpAclDefinitionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionStorageType.setStatus("current")
_QosIpAclDefinitionStatus_Type = RowStatus
_QosIpAclDefinitionStatus_Object = MibTableColumn
qosIpAclDefinitionStatus = _QosIpAclDefinitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 6),
    _QosIpAclDefinitionStatus_Type()
)
qosIpAclDefinitionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionStatus.setStatus("current")


class _QosIpAclDefinitionLabel_Type(SnmpAdminString):
    """Custom type qosIpAclDefinitionLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QosIpAclDefinitionLabel_Type.__name__ = "SnmpAdminString"
_QosIpAclDefinitionLabel_Object = MibTableColumn
qosIpAclDefinitionLabel = _QosIpAclDefinitionLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 2, 1, 2, 1, 7),
    _QosIpAclDefinitionLabel_Type()
)
qosIpAclDefinitionLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIpAclDefinitionLabel.setStatus("current")
_QosPolicyIpPibConformance_ObjectIdentity = ObjectIdentity
qosPolicyIpPibConformance = _QosPolicyIpPibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3)
)
_QosPolicyIpPibCompliances_ObjectIdentity = ObjectIdentity
qosPolicyIpPibCompliances = _QosPolicyIpPibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 1)
)
_QosPolicyIpPibGroups_ObjectIdentity = ObjectIdentity
qosPolicyIpPibGroups = _QosPolicyIpPibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2)
)

# Managed Objects groups

qosInterfaceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 1)
)
qosInterfaceTypeGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosInterfaceTypeRoles"),
        ("QOS-POLICY-IP-PIB", "qosInterfaceTypeQueueSet"),
        ("QOS-POLICY-IP-PIB", "qosInterfaceTypeCapabilities"),
        ("QOS-POLICY-IP-PIB", "qosInterfaceTypeStorageType"),
        ("QOS-POLICY-IP-PIB", "qosInterfaceTypeStatus"))
)
if mibBuilder.loadTexts:
    qosInterfaceTypeGroup.setStatus("current")

qosIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 2)
)
qosIfQueueGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosIfQueueSetId"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueIndex"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueGenDiscipline"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueExtDiscipline"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueDrainSize"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueAbsBandwidth"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueBandwidthAllocation"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueServiceOrder"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueSize"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueStorageType"),
        ("QOS-POLICY-IP-PIB", "qosIfQueueStatus"))
)
if mibBuilder.loadTexts:
    qosIfQueueGroup.setStatus("current")

qosIfDscpAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 3)
)
qosIfDscpAssignmentGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosIfDscpAssignmentRoles"),
        ("QOS-POLICY-IP-PIB", "qosIfDscpAssignmentDscp"),
        ("QOS-POLICY-IP-PIB", "qosIfDscpAssignmentQueue"),
        ("QOS-POLICY-IP-PIB", "qosIfDscpAssignmentStorageType"),
        ("QOS-POLICY-IP-PIB", "qosIfDscpAssignmentStatus"))
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentGroup.setStatus("current")

qosMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 4)
)
qosMeterGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosMeterDataSpecification"),
        ("QOS-POLICY-IP-PIB", "qosMeterCommittedRate"),
        ("QOS-POLICY-IP-PIB", "qosMeterCommittedBurst"),
        ("QOS-POLICY-IP-PIB", "qosMeterPeakRate"),
        ("QOS-POLICY-IP-PIB", "qosMeterPeakBurst"),
        ("QOS-POLICY-IP-PIB", "qosMeterHighConfAction"),
        ("QOS-POLICY-IP-PIB", "qosMeterMedConfAction"),
        ("QOS-POLICY-IP-PIB", "qosMeterLowConfAction"),
        ("QOS-POLICY-IP-PIB", "qosMeterStorageType"),
        ("QOS-POLICY-IP-PIB", "qosMeterStatus"),
        ("QOS-POLICY-IP-PIB", "qosMeterLabel"))
)
if mibBuilder.loadTexts:
    qosMeterGroup.setStatus("current")

qosActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 5)
)
qosActionGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosActionDrop"),
        ("QOS-POLICY-IP-PIB", "qosActionUpdateDSCP"),
        ("QOS-POLICY-IP-PIB", "qosActionMeter"),
        ("QOS-POLICY-IP-PIB", "qosActionStorageType"),
        ("QOS-POLICY-IP-PIB", "qosActionStatus"),
        ("QOS-POLICY-IP-PIB", "qosActionLabel"))
)
if mibBuilder.loadTexts:
    qosActionGroup.setStatus("current")

qosTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 6)
)
qosTargetGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosTargetAclId"),
        ("QOS-POLICY-IP-PIB", "qosTargetAclType"),
        ("QOS-POLICY-IP-PIB", "qosTargetInterfaceRoles"),
        ("QOS-POLICY-IP-PIB", "qosTargetInterfaceDirection"),
        ("QOS-POLICY-IP-PIB", "qosTargetOrder"),
        ("QOS-POLICY-IP-PIB", "qosTargetMeter"),
        ("QOS-POLICY-IP-PIB", "qosTargetStorageType"),
        ("QOS-POLICY-IP-PIB", "qosTargetStatus"),
        ("QOS-POLICY-IP-PIB", "qosTargetShapingParams"),
        ("QOS-POLICY-IP-PIB", "qosTargetShapingGroup"),
        ("QOS-POLICY-IP-PIB", "qosTargetLabel"),
        ("QOS-POLICY-IP-PIB", "qosTargetInProfileAction"),
        ("QOS-POLICY-IP-PIB", "qosTargetOutOfProfileAction"))
)
if mibBuilder.loadTexts:
    qosTargetGroup.setStatus("current")

qosIpAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 7)
)
qosIpAceGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosIpAceDstAddr"),
        ("QOS-POLICY-IP-PIB", "qosIpAceDstAddrMask"),
        ("QOS-POLICY-IP-PIB", "qosIpAceSrcAddr"),
        ("QOS-POLICY-IP-PIB", "qosIpAceSrcAddrMask"),
        ("QOS-POLICY-IP-PIB", "qosIpAceDscp"),
        ("QOS-POLICY-IP-PIB", "qosIpAceProtocol"),
        ("QOS-POLICY-IP-PIB", "qosIpAceDstL4PortMin"),
        ("QOS-POLICY-IP-PIB", "qosIpAceDstL4PortMax"),
        ("QOS-POLICY-IP-PIB", "qosIpAceSrcL4PortMin"),
        ("QOS-POLICY-IP-PIB", "qosIpAceSrcL4PortMax"),
        ("QOS-POLICY-IP-PIB", "qosIpAcePermit"),
        ("QOS-POLICY-IP-PIB", "qosIpAceStorageType"),
        ("QOS-POLICY-IP-PIB", "qosIpAceStatus"))
)
if mibBuilder.loadTexts:
    qosIpAceGroup.setStatus("current")

qosIpAclDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 2, 8)
)
qosIpAclDefinitionGroup.setObjects(
      *(("QOS-POLICY-IP-PIB", "qosIpAclDefinitionAclId"),
        ("QOS-POLICY-IP-PIB", "qosIpAclDefinitionAceId"),
        ("QOS-POLICY-IP-PIB", "qosIpAclDefinitionAceOrder"),
        ("QOS-POLICY-IP-PIB", "qosIpAclDefinitionStorageType"),
        ("QOS-POLICY-IP-PIB", "qosIpAclDefinitionStatus"),
        ("QOS-POLICY-IP-PIB", "qosIpAclDefinitionLabel"))
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qosPolicyIpPibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qosPolicyIpPibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOS-POLICY-IP-PIB",
    **{"Dscp": Dscp,
       "PolicyInstanceIdOrZero": PolicyInstanceIdOrZero,
       "QosInterfaceQueueCount": QosInterfaceQueueCount,
       "qosPolicyIpPib": qosPolicyIpPib,
       "qosPolicyGenPibClasses": qosPolicyGenPibClasses,
       "qosIfParameters": qosIfParameters,
       "qosInterfaceTypeTable": qosInterfaceTypeTable,
       "qosInterfaceTypeEntry": qosInterfaceTypeEntry,
       "qosInterfaceTypeId": qosInterfaceTypeId,
       "qosInterfaceTypeRoles": qosInterfaceTypeRoles,
       "qosInterfaceTypeQueueSet": qosInterfaceTypeQueueSet,
       "qosInterfaceTypeCapabilities": qosInterfaceTypeCapabilities,
       "qosInterfaceTypeStorageType": qosInterfaceTypeStorageType,
       "qosInterfaceTypeStatus": qosInterfaceTypeStatus,
       "qosIfQueueTable": qosIfQueueTable,
       "qosIfQueueEntry": qosIfQueueEntry,
       "qosIfQueueId": qosIfQueueId,
       "qosIfQueueSetId": qosIfQueueSetId,
       "qosIfQueueIndex": qosIfQueueIndex,
       "qosIfQueueGenDiscipline": qosIfQueueGenDiscipline,
       "qosIfQueueExtDiscipline": qosIfQueueExtDiscipline,
       "qosIfQueueDrainSize": qosIfQueueDrainSize,
       "qosIfQueueAbsBandwidth": qosIfQueueAbsBandwidth,
       "qosIfQueueBandwidthAllocation": qosIfQueueBandwidthAllocation,
       "qosIfQueueServiceOrder": qosIfQueueServiceOrder,
       "qosIfQueueSize": qosIfQueueSize,
       "qosIfQueueStorageType": qosIfQueueStorageType,
       "qosIfQueueStatus": qosIfQueueStatus,
       "qosIfDscpAssignmentTable": qosIfDscpAssignmentTable,
       "qosIfDscpAssignmentEntry": qosIfDscpAssignmentEntry,
       "qosIfDscpAssignmentId": qosIfDscpAssignmentId,
       "qosIfDscpAssignmentRoles": qosIfDscpAssignmentRoles,
       "qosIfDscpAssignmentDscp": qosIfDscpAssignmentDscp,
       "qosIfDscpAssignmentQueue": qosIfDscpAssignmentQueue,
       "qosIfDscpAssignmentStorageType": qosIfDscpAssignmentStorageType,
       "qosIfDscpAssignmentStatus": qosIfDscpAssignmentStatus,
       "qosMeter": qosMeter,
       "qosMeterTable": qosMeterTable,
       "qosMeterEntry": qosMeterEntry,
       "qosMeterId": qosMeterId,
       "qosMeterDataSpecification": qosMeterDataSpecification,
       "qosMeterCommittedRate": qosMeterCommittedRate,
       "qosMeterCommittedBurst": qosMeterCommittedBurst,
       "qosMeterPeakRate": qosMeterPeakRate,
       "qosMeterPeakBurst": qosMeterPeakBurst,
       "qosMeterHighConfAction": qosMeterHighConfAction,
       "qosMeterMedConfAction": qosMeterMedConfAction,
       "qosMeterLowConfAction": qosMeterLowConfAction,
       "qosMeterStorageType": qosMeterStorageType,
       "qosMeterStatus": qosMeterStatus,
       "qosMeterLabel": qosMeterLabel,
       "qosAction": qosAction,
       "qosActionTable": qosActionTable,
       "qosActionEntry": qosActionEntry,
       "qosActionId": qosActionId,
       "qosActionDrop": qosActionDrop,
       "qosActionUpdateDSCP": qosActionUpdateDSCP,
       "qosActionMeter": qosActionMeter,
       "qosActionStorageType": qosActionStorageType,
       "qosActionStatus": qosActionStatus,
       "qosActionLabel": qosActionLabel,
       "qosTargetTable": qosTargetTable,
       "qosTargetEntry": qosTargetEntry,
       "qosTargetId": qosTargetId,
       "qosTargetAclId": qosTargetAclId,
       "qosTargetAclType": qosTargetAclType,
       "qosTargetInterfaceRoles": qosTargetInterfaceRoles,
       "qosTargetInterfaceDirection": qosTargetInterfaceDirection,
       "qosTargetOrder": qosTargetOrder,
       "qosTargetMeter": qosTargetMeter,
       "qosTargetStorageType": qosTargetStorageType,
       "qosTargetStatus": qosTargetStatus,
       "qosTargetShapingParams": qosTargetShapingParams,
       "qosTargetShapingGroup": qosTargetShapingGroup,
       "qosTargetLabel": qosTargetLabel,
       "qosTargetInProfileAction": qosTargetInProfileAction,
       "qosTargetOutOfProfileAction": qosTargetOutOfProfileAction,
       "qosPolicyIpPibClasses": qosPolicyIpPibClasses,
       "qosIpQos": qosIpQos,
       "qosIpAceTable": qosIpAceTable,
       "qosIpAceEntry": qosIpAceEntry,
       "qosIpAceId": qosIpAceId,
       "qosIpAceDstAddr": qosIpAceDstAddr,
       "qosIpAceDstAddrMask": qosIpAceDstAddrMask,
       "qosIpAceSrcAddr": qosIpAceSrcAddr,
       "qosIpAceSrcAddrMask": qosIpAceSrcAddrMask,
       "qosIpAceDscp": qosIpAceDscp,
       "qosIpAceProtocol": qosIpAceProtocol,
       "qosIpAceDstL4PortMin": qosIpAceDstL4PortMin,
       "qosIpAceDstL4PortMax": qosIpAceDstL4PortMax,
       "qosIpAceSrcL4PortMin": qosIpAceSrcL4PortMin,
       "qosIpAceSrcL4PortMax": qosIpAceSrcL4PortMax,
       "qosIpAcePermit": qosIpAcePermit,
       "qosIpAceStorageType": qosIpAceStorageType,
       "qosIpAceStatus": qosIpAceStatus,
       "qosIpAclDefinitionTable": qosIpAclDefinitionTable,
       "qosIpAclDefinitionEntry": qosIpAclDefinitionEntry,
       "qosIpAclDefinitionId": qosIpAclDefinitionId,
       "qosIpAclDefinitionAclId": qosIpAclDefinitionAclId,
       "qosIpAclDefinitionAceId": qosIpAclDefinitionAceId,
       "qosIpAclDefinitionAceOrder": qosIpAclDefinitionAceOrder,
       "qosIpAclDefinitionStorageType": qosIpAclDefinitionStorageType,
       "qosIpAclDefinitionStatus": qosIpAclDefinitionStatus,
       "qosIpAclDefinitionLabel": qosIpAclDefinitionLabel,
       "qosPolicyIpPibConformance": qosPolicyIpPibConformance,
       "qosPolicyIpPibCompliances": qosPolicyIpPibCompliances,
       "qosPolicyIpPibCompliance": qosPolicyIpPibCompliance,
       "qosPolicyIpPibGroups": qosPolicyIpPibGroups,
       "qosInterfaceTypeGroup": qosInterfaceTypeGroup,
       "qosIfQueueGroup": qosIfQueueGroup,
       "qosIfDscpAssignmentGroup": qosIfDscpAssignmentGroup,
       "qosMeterGroup": qosMeterGroup,
       "qosActionGroup": qosActionGroup,
       "qosTargetGroup": qosTargetGroup,
       "qosIpAceGroup": qosIpAceGroup,
       "qosIpAclDefinitionGroup": qosIpAclDefinitionGroup}
)
