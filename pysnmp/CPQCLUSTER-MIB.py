# SNMP MIB module (CPQCLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQCLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:15 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqCluster_ObjectIdentity = ObjectIdentity
cpqCluster = _CpqCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15)
)
_CpqClusterMibRev_ObjectIdentity = ObjectIdentity
cpqClusterMibRev = _CpqClusterMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 1)
)


class _CpqClusterMibRevMajor_Type(Integer32):
    """Custom type cpqClusterMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqClusterMibRevMajor_Type.__name__ = "Integer32"
_CpqClusterMibRevMajor_Object = MibScalar
cpqClusterMibRevMajor = _CpqClusterMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 1, 1),
    _CpqClusterMibRevMajor_Type()
)
cpqClusterMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterMibRevMajor.setStatus("mandatory")


class _CpqClusterMibRevMinor_Type(Integer32):
    """Custom type cpqClusterMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqClusterMibRevMinor_Type.__name__ = "Integer32"
_CpqClusterMibRevMinor_Object = MibScalar
cpqClusterMibRevMinor = _CpqClusterMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 1, 2),
    _CpqClusterMibRevMinor_Type()
)
cpqClusterMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterMibRevMinor.setStatus("mandatory")


class _CpqClusterMibCondition_Type(Integer32):
    """Custom type cpqClusterMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterMibCondition_Type.__name__ = "Integer32"
_CpqClusterMibCondition_Object = MibScalar
cpqClusterMibCondition = _CpqClusterMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 1, 3),
    _CpqClusterMibCondition_Type()
)
cpqClusterMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterMibCondition.setStatus("mandatory")
_CpqClusterComponent_ObjectIdentity = ObjectIdentity
cpqClusterComponent = _CpqClusterComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2)
)
_CpqClusterInterface_ObjectIdentity = ObjectIdentity
cpqClusterInterface = _CpqClusterInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1)
)
_CpqClusterOsCommon_ObjectIdentity = ObjectIdentity
cpqClusterOsCommon = _CpqClusterOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4)
)


class _CpqClusterOsCommonPollFreq_Type(Integer32):
    """Custom type cpqClusterOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqClusterOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqClusterOsCommonPollFreq_Object = MibScalar
cpqClusterOsCommonPollFreq = _CpqClusterOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 1),
    _CpqClusterOsCommonPollFreq_Type()
)
cpqClusterOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqClusterOsCommonPollFreq.setStatus("mandatory")
_CpqClusterOsCommonModuleTable_Object = MibTable
cpqClusterOsCommonModuleTable = _CpqClusterOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleTable.setStatus("deprecated")
_CpqClusterOsCommonModuleEntry_Object = MibTableRow
cpqClusterOsCommonModuleEntry = _CpqClusterOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1)
)
cpqClusterOsCommonModuleEntry.setIndexNames(
    (0, "CPQCLUSTER-MIB", "cpqClusterOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleEntry.setStatus("deprecated")


class _CpqClusterOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqClusterOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqClusterOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqClusterOsCommonModuleIndex_Object = MibTableColumn
cpqClusterOsCommonModuleIndex = _CpqClusterOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1, 1),
    _CpqClusterOsCommonModuleIndex_Type()
)
cpqClusterOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleIndex.setStatus("deprecated")


class _CpqClusterOsCommonModuleName_Type(DisplayString):
    """Custom type cpqClusterOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqClusterOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqClusterOsCommonModuleName_Object = MibTableColumn
cpqClusterOsCommonModuleName = _CpqClusterOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1, 2),
    _CpqClusterOsCommonModuleName_Type()
)
cpqClusterOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleName.setStatus("deprecated")


class _CpqClusterOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqClusterOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqClusterOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqClusterOsCommonModuleVersion_Object = MibTableColumn
cpqClusterOsCommonModuleVersion = _CpqClusterOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1, 3),
    _CpqClusterOsCommonModuleVersion_Type()
)
cpqClusterOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleVersion.setStatus("deprecated")


class _CpqClusterOsCommonModuleDate_Type(OctetString):
    """Custom type cpqClusterOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqClusterOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqClusterOsCommonModuleDate_Object = MibTableColumn
cpqClusterOsCommonModuleDate = _CpqClusterOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1, 4),
    _CpqClusterOsCommonModuleDate_Type()
)
cpqClusterOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterOsCommonModuleDate.setStatus("deprecated")


class _CpqClusterOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqClusterOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqClusterOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqClusterOsCommonModulePurpose_Object = MibTableColumn
cpqClusterOsCommonModulePurpose = _CpqClusterOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 1, 4, 2, 1, 5),
    _CpqClusterOsCommonModulePurpose_Type()
)
cpqClusterOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterOsCommonModulePurpose.setStatus("deprecated")
_CpqClusterInfo_ObjectIdentity = ObjectIdentity
cpqClusterInfo = _CpqClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2)
)


class _CpqClusterName_Type(DisplayString):
    """Custom type cpqClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqClusterName_Type.__name__ = "DisplayString"
_CpqClusterName_Object = MibScalar
cpqClusterName = _CpqClusterName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 1),
    _CpqClusterName_Type()
)
cpqClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqClusterName.setStatus("mandatory")


class _CpqClusterCondition_Type(Integer32):
    """Custom type cpqClusterCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterCondition_Type.__name__ = "Integer32"
_CpqClusterCondition_Object = MibScalar
cpqClusterCondition = _CpqClusterCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 2),
    _CpqClusterCondition_Type()
)
cpqClusterCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterCondition.setStatus("mandatory")


class _CpqClusterIpAddress_Type(DisplayString):
    """Custom type cpqClusterIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterIpAddress_Type.__name__ = "DisplayString"
_CpqClusterIpAddress_Object = MibScalar
cpqClusterIpAddress = _CpqClusterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 3),
    _CpqClusterIpAddress_Type()
)
cpqClusterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterIpAddress.setStatus("mandatory")
_CpqClusterQuorumResource_Type = Integer32
_CpqClusterQuorumResource_Object = MibScalar
cpqClusterQuorumResource = _CpqClusterQuorumResource_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 4),
    _CpqClusterQuorumResource_Type()
)
cpqClusterQuorumResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterQuorumResource.setStatus("mandatory")
_CpqClusterMajorVersion_Type = Integer32
_CpqClusterMajorVersion_Object = MibScalar
cpqClusterMajorVersion = _CpqClusterMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 5),
    _CpqClusterMajorVersion_Type()
)
cpqClusterMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterMajorVersion.setStatus("mandatory")
_CpqClusterMinorVersion_Type = Integer32
_CpqClusterMinorVersion_Object = MibScalar
cpqClusterMinorVersion = _CpqClusterMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 6),
    _CpqClusterMinorVersion_Type()
)
cpqClusterMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterMinorVersion.setStatus("mandatory")


class _CpqClusterCSDVersion_Type(DisplayString):
    """Custom type cpqClusterCSDVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterCSDVersion_Type.__name__ = "DisplayString"
_CpqClusterCSDVersion_Object = MibScalar
cpqClusterCSDVersion = _CpqClusterCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 7),
    _CpqClusterCSDVersion_Type()
)
cpqClusterCSDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterCSDVersion.setStatus("mandatory")


class _CpqClusterVendorId_Type(DisplayString):
    """Custom type cpqClusterVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterVendorId_Type.__name__ = "DisplayString"
_CpqClusterVendorId_Object = MibScalar
cpqClusterVendorId = _CpqClusterVendorId_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 8),
    _CpqClusterVendorId_Type()
)
cpqClusterVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterVendorId.setStatus("mandatory")


class _CpqClusterResourceAggregateCondition_Type(Integer32):
    """Custom type cpqClusterResourceAggregateCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterResourceAggregateCondition_Type.__name__ = "Integer32"
_CpqClusterResourceAggregateCondition_Object = MibScalar
cpqClusterResourceAggregateCondition = _CpqClusterResourceAggregateCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 9),
    _CpqClusterResourceAggregateCondition_Type()
)
cpqClusterResourceAggregateCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceAggregateCondition.setStatus("mandatory")


class _CpqClusterNetworkAggregateCondition_Type(Integer32):
    """Custom type cpqClusterNetworkAggregateCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterNetworkAggregateCondition_Type.__name__ = "Integer32"
_CpqClusterNetworkAggregateCondition_Object = MibScalar
cpqClusterNetworkAggregateCondition = _CpqClusterNetworkAggregateCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 2, 10),
    _CpqClusterNetworkAggregateCondition_Type()
)
cpqClusterNetworkAggregateCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkAggregateCondition.setStatus("mandatory")
_CpqClusterNode_ObjectIdentity = ObjectIdentity
cpqClusterNode = _CpqClusterNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3)
)
_CpqClusterNodeTable_Object = MibTable
cpqClusterNodeTable = _CpqClusterNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqClusterNodeTable.setStatus("mandatory")
_CpqClusterNodeEntry_Object = MibTableRow
cpqClusterNodeEntry = _CpqClusterNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1, 1)
)
cpqClusterNodeEntry.setIndexNames(
    (0, "CPQCLUSTER-MIB", "cpqClusterNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqClusterNodeEntry.setStatus("mandatory")


class _CpqClusterNodeIndex_Type(Integer32):
    """Custom type cpqClusterNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqClusterNodeIndex_Type.__name__ = "Integer32"
_CpqClusterNodeIndex_Object = MibTableColumn
cpqClusterNodeIndex = _CpqClusterNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1, 1, 1),
    _CpqClusterNodeIndex_Type()
)
cpqClusterNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNodeIndex.setStatus("mandatory")


class _CpqClusterNodeName_Type(DisplayString):
    """Custom type cpqClusterNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterNodeName_Type.__name__ = "DisplayString"
_CpqClusterNodeName_Object = MibTableColumn
cpqClusterNodeName = _CpqClusterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1, 1, 2),
    _CpqClusterNodeName_Type()
)
cpqClusterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNodeName.setStatus("mandatory")


class _CpqClusterNodeStatus_Type(Integer32):
    """Custom type cpqClusterNodeStatus based on Integer32"""
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
        *(("nodeDown", 3),
          ("nodeJoining", 5),
          ("nodePaused", 4),
          ("nodeUp", 2),
          ("other", 1))
    )


_CpqClusterNodeStatus_Type.__name__ = "Integer32"
_CpqClusterNodeStatus_Object = MibTableColumn
cpqClusterNodeStatus = _CpqClusterNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1, 1, 3),
    _CpqClusterNodeStatus_Type()
)
cpqClusterNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNodeStatus.setStatus("mandatory")


class _CpqClusterNodeCondition_Type(Integer32):
    """Custom type cpqClusterNodeCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterNodeCondition_Type.__name__ = "Integer32"
_CpqClusterNodeCondition_Object = MibTableColumn
cpqClusterNodeCondition = _CpqClusterNodeCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 3, 1, 1, 4),
    _CpqClusterNodeCondition_Type()
)
cpqClusterNodeCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNodeCondition.setStatus("mandatory")
_CpqClusterResource_ObjectIdentity = ObjectIdentity
cpqClusterResource = _CpqClusterResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4)
)
_CpqClusterResourceTable_Object = MibTable
cpqClusterResourceTable = _CpqClusterResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqClusterResourceTable.setStatus("mandatory")
_CpqClusterResourceEntry_Object = MibTableRow
cpqClusterResourceEntry = _CpqClusterResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1)
)
cpqClusterResourceEntry.setIndexNames(
    (0, "CPQCLUSTER-MIB", "cpqClusterResourceIndex"),
)
if mibBuilder.loadTexts:
    cpqClusterResourceEntry.setStatus("mandatory")


class _CpqClusterResourceIndex_Type(Integer32):
    """Custom type cpqClusterResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqClusterResourceIndex_Type.__name__ = "Integer32"
_CpqClusterResourceIndex_Object = MibTableColumn
cpqClusterResourceIndex = _CpqClusterResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 1),
    _CpqClusterResourceIndex_Type()
)
cpqClusterResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceIndex.setStatus("mandatory")


class _CpqClusterResourceName_Type(DisplayString):
    """Custom type cpqClusterResourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceName_Type.__name__ = "DisplayString"
_CpqClusterResourceName_Object = MibTableColumn
cpqClusterResourceName = _CpqClusterResourceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 2),
    _CpqClusterResourceName_Type()
)
cpqClusterResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceName.setStatus("mandatory")


class _CpqClusterResourceType_Type(DisplayString):
    """Custom type cpqClusterResourceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceType_Type.__name__ = "DisplayString"
_CpqClusterResourceType_Object = MibTableColumn
cpqClusterResourceType = _CpqClusterResourceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 3),
    _CpqClusterResourceType_Type()
)
cpqClusterResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceType.setStatus("mandatory")


class _CpqClusterResourceState_Type(Integer32):
    """Custom type cpqClusterResourceState based on Integer32"""
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
        *(("failed", 4),
          ("offline", 3),
          ("offlinePending", 6),
          ("online", 2),
          ("onlinePending", 5),
          ("other", 1))
    )


_CpqClusterResourceState_Type.__name__ = "Integer32"
_CpqClusterResourceState_Object = MibTableColumn
cpqClusterResourceState = _CpqClusterResourceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 4),
    _CpqClusterResourceState_Type()
)
cpqClusterResourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceState.setStatus("mandatory")


class _CpqClusterResourceOwnerNode_Type(DisplayString):
    """Custom type cpqClusterResourceOwnerNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceOwnerNode_Type.__name__ = "DisplayString"
_CpqClusterResourceOwnerNode_Object = MibTableColumn
cpqClusterResourceOwnerNode = _CpqClusterResourceOwnerNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 5),
    _CpqClusterResourceOwnerNode_Type()
)
cpqClusterResourceOwnerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceOwnerNode.setStatus("mandatory")


class _CpqClusterResourcePhysId_Type(DisplayString):
    """Custom type cpqClusterResourcePhysId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourcePhysId_Type.__name__ = "DisplayString"
_CpqClusterResourcePhysId_Object = MibTableColumn
cpqClusterResourcePhysId = _CpqClusterResourcePhysId_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 6),
    _CpqClusterResourcePhysId_Type()
)
cpqClusterResourcePhysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourcePhysId.setStatus("mandatory")


class _CpqClusterResourceCondition_Type(Integer32):
    """Custom type cpqClusterResourceCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterResourceCondition_Type.__name__ = "Integer32"
_CpqClusterResourceCondition_Object = MibTableColumn
cpqClusterResourceCondition = _CpqClusterResourceCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 7),
    _CpqClusterResourceCondition_Type()
)
cpqClusterResourceCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceCondition.setStatus("mandatory")


class _CpqClusterResourceDriveLetter_Type(DisplayString):
    """Custom type cpqClusterResourceDriveLetter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceDriveLetter_Type.__name__ = "DisplayString"
_CpqClusterResourceDriveLetter_Object = MibTableColumn
cpqClusterResourceDriveLetter = _CpqClusterResourceDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 8),
    _CpqClusterResourceDriveLetter_Type()
)
cpqClusterResourceDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceDriveLetter.setStatus("mandatory")


class _CpqClusterResourceIpAddress_Type(DisplayString):
    """Custom type cpqClusterResourceIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceIpAddress_Type.__name__ = "DisplayString"
_CpqClusterResourceIpAddress_Object = MibTableColumn
cpqClusterResourceIpAddress = _CpqClusterResourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 9),
    _CpqClusterResourceIpAddress_Type()
)
cpqClusterResourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceIpAddress.setStatus("mandatory")


class _CpqClusterResourceGroupName_Type(DisplayString):
    """Custom type cpqClusterResourceGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterResourceGroupName_Type.__name__ = "DisplayString"
_CpqClusterResourceGroupName_Object = MibTableColumn
cpqClusterResourceGroupName = _CpqClusterResourceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 4, 1, 1, 10),
    _CpqClusterResourceGroupName_Type()
)
cpqClusterResourceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterResourceGroupName.setStatus("mandatory")
_CpqClusterInterconnect_ObjectIdentity = ObjectIdentity
cpqClusterInterconnect = _CpqClusterInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5)
)
_CpqClusterInterconnectTable_Object = MibTable
cpqClusterInterconnectTable = _CpqClusterInterconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqClusterInterconnectTable.setStatus("mandatory")
_CpqClusterInterconnectEntry_Object = MibTableRow
cpqClusterInterconnectEntry = _CpqClusterInterconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1)
)
cpqClusterInterconnectEntry.setIndexNames(
    (0, "CPQCLUSTER-MIB", "cpqClusterInterconnectIndex"),
)
if mibBuilder.loadTexts:
    cpqClusterInterconnectEntry.setStatus("mandatory")


class _CpqClusterInterconnectIndex_Type(Integer32):
    """Custom type cpqClusterInterconnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqClusterInterconnectIndex_Type.__name__ = "Integer32"
_CpqClusterInterconnectIndex_Object = MibTableColumn
cpqClusterInterconnectIndex = _CpqClusterInterconnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 1),
    _CpqClusterInterconnectIndex_Type()
)
cpqClusterInterconnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectIndex.setStatus("mandatory")


class _CpqClusterInterconnectPhysId_Type(DisplayString):
    """Custom type cpqClusterInterconnectPhysId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterInterconnectPhysId_Type.__name__ = "DisplayString"
_CpqClusterInterconnectPhysId_Object = MibTableColumn
cpqClusterInterconnectPhysId = _CpqClusterInterconnectPhysId_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 2),
    _CpqClusterInterconnectPhysId_Type()
)
cpqClusterInterconnectPhysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectPhysId.setStatus("mandatory")


class _CpqClusterInterconnectTransport_Type(DisplayString):
    """Custom type cpqClusterInterconnectTransport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterInterconnectTransport_Type.__name__ = "DisplayString"
_CpqClusterInterconnectTransport_Object = MibTableColumn
cpqClusterInterconnectTransport = _CpqClusterInterconnectTransport_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 3),
    _CpqClusterInterconnectTransport_Type()
)
cpqClusterInterconnectTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectTransport.setStatus("mandatory")


class _CpqClusterInterconnectAddress_Type(DisplayString):
    """Custom type cpqClusterInterconnectAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterInterconnectAddress_Type.__name__ = "DisplayString"
_CpqClusterInterconnectAddress_Object = MibTableColumn
cpqClusterInterconnectAddress = _CpqClusterInterconnectAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 4),
    _CpqClusterInterconnectAddress_Type()
)
cpqClusterInterconnectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectAddress.setStatus("mandatory")


class _CpqClusterInterconnectNetworkName_Type(DisplayString):
    """Custom type cpqClusterInterconnectNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterInterconnectNetworkName_Type.__name__ = "DisplayString"
_CpqClusterInterconnectNetworkName_Object = MibTableColumn
cpqClusterInterconnectNetworkName = _CpqClusterInterconnectNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 5),
    _CpqClusterInterconnectNetworkName_Type()
)
cpqClusterInterconnectNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectNetworkName.setStatus("mandatory")


class _CpqClusterInterconnectNodeName_Type(DisplayString):
    """Custom type cpqClusterInterconnectNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterInterconnectNodeName_Type.__name__ = "DisplayString"
_CpqClusterInterconnectNodeName_Object = MibTableColumn
cpqClusterInterconnectNodeName = _CpqClusterInterconnectNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 6),
    _CpqClusterInterconnectNodeName_Type()
)
cpqClusterInterconnectNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectNodeName.setStatus("mandatory")


class _CpqClusterInterconnectRole_Type(Integer32):
    """Custom type cpqClusterInterconnectRole based on Integer32"""
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
        *(("client", 2),
          ("clientAndInternal", 4),
          ("internal", 3),
          ("none", 1))
    )


_CpqClusterInterconnectRole_Type.__name__ = "Integer32"
_CpqClusterInterconnectRole_Object = MibTableColumn
cpqClusterInterconnectRole = _CpqClusterInterconnectRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 5, 1, 1, 7),
    _CpqClusterInterconnectRole_Type()
)
cpqClusterInterconnectRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterInterconnectRole.setStatus("mandatory")
_CpqClusterNetwork_ObjectIdentity = ObjectIdentity
cpqClusterNetwork = _CpqClusterNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6)
)
_CpqClusterNetworkTable_Object = MibTable
cpqClusterNetworkTable = _CpqClusterNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqClusterNetworkTable.setStatus("mandatory")
_CpqClusterNetworkEntry_Object = MibTableRow
cpqClusterNetworkEntry = _CpqClusterNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1)
)
cpqClusterNetworkEntry.setIndexNames(
    (0, "CPQCLUSTER-MIB", "cpqClusterNetworkIndex"),
)
if mibBuilder.loadTexts:
    cpqClusterNetworkEntry.setStatus("mandatory")


class _CpqClusterNetworkIndex_Type(Integer32):
    """Custom type cpqClusterNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqClusterNetworkIndex_Type.__name__ = "Integer32"
_CpqClusterNetworkIndex_Object = MibTableColumn
cpqClusterNetworkIndex = _CpqClusterNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 1),
    _CpqClusterNetworkIndex_Type()
)
cpqClusterNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkIndex.setStatus("mandatory")


class _CpqClusterNetworkName_Type(DisplayString):
    """Custom type cpqClusterNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterNetworkName_Type.__name__ = "DisplayString"
_CpqClusterNetworkName_Object = MibTableColumn
cpqClusterNetworkName = _CpqClusterNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 2),
    _CpqClusterNetworkName_Type()
)
cpqClusterNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkName.setStatus("mandatory")


class _CpqClusterNetworkAddressMask_Type(DisplayString):
    """Custom type cpqClusterNetworkAddressMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqClusterNetworkAddressMask_Type.__name__ = "DisplayString"
_CpqClusterNetworkAddressMask_Object = MibTableColumn
cpqClusterNetworkAddressMask = _CpqClusterNetworkAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 3),
    _CpqClusterNetworkAddressMask_Type()
)
cpqClusterNetworkAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkAddressMask.setStatus("mandatory")


class _CpqClusterNetworkDescription_Type(DisplayString):
    """Custom type cpqClusterNetworkDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqClusterNetworkDescription_Type.__name__ = "DisplayString"
_CpqClusterNetworkDescription_Object = MibTableColumn
cpqClusterNetworkDescription = _CpqClusterNetworkDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 4),
    _CpqClusterNetworkDescription_Type()
)
cpqClusterNetworkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkDescription.setStatus("mandatory")


class _CpqClusterNetworkRole_Type(Integer32):
    """Custom type cpqClusterNetworkRole based on Integer32"""
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
        *(("client", 2),
          ("clientAndInternal", 4),
          ("internal", 3),
          ("none", 1))
    )


_CpqClusterNetworkRole_Type.__name__ = "Integer32"
_CpqClusterNetworkRole_Object = MibTableColumn
cpqClusterNetworkRole = _CpqClusterNetworkRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 5),
    _CpqClusterNetworkRole_Type()
)
cpqClusterNetworkRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkRole.setStatus("mandatory")


class _CpqClusterNetworkState_Type(Integer32):
    """Custom type cpqClusterNetworkState based on Integer32"""
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
        *(("offline", 3),
          ("online", 2),
          ("other", 1),
          ("partitioned", 4),
          ("unavailable", 5))
    )


_CpqClusterNetworkState_Type.__name__ = "Integer32"
_CpqClusterNetworkState_Object = MibTableColumn
cpqClusterNetworkState = _CpqClusterNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 6),
    _CpqClusterNetworkState_Type()
)
cpqClusterNetworkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkState.setStatus("mandatory")


class _CpqClusterNetworkCondition_Type(Integer32):
    """Custom type cpqClusterNetworkCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqClusterNetworkCondition_Type.__name__ = "Integer32"
_CpqClusterNetworkCondition_Object = MibTableColumn
cpqClusterNetworkCondition = _CpqClusterNetworkCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 15, 2, 6, 1, 1, 7),
    _CpqClusterNetworkCondition_Type()
)
cpqClusterNetworkCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqClusterNetworkCondition.setStatus("mandatory")
_CpqClusterTrap_ObjectIdentity = ObjectIdentity
cpqClusterTrap = _CpqClusterTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 15, 3)
)

# Managed Objects groups


# Notification objects

cpqClusterDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15001)
)
cpqClusterDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterName"))
)
if mibBuilder.loadTexts:
    cpqClusterDegraded.setStatus(
        ""
    )

cpqClusterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15002)
)
cpqClusterFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterName"))
)
if mibBuilder.loadTexts:
    cpqClusterFailed.setStatus(
        ""
    )

cpqClusterNodeDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15003)
)
cpqClusterNodeDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterNodeName"))
)
if mibBuilder.loadTexts:
    cpqClusterNodeDegraded.setStatus(
        ""
    )

cpqClusterNodeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15004)
)
cpqClusterNodeFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterNodeName"))
)
if mibBuilder.loadTexts:
    cpqClusterNodeFailed.setStatus(
        ""
    )

cpqClusterResourceDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15005)
)
cpqClusterResourceDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterResourceName"))
)
if mibBuilder.loadTexts:
    cpqClusterResourceDegraded.setStatus(
        ""
    )

cpqClusterResourceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15006)
)
cpqClusterResourceFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterResourceName"))
)
if mibBuilder.loadTexts:
    cpqClusterResourceFailed.setStatus(
        ""
    )

cpqClusterNetworkDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15007)
)
cpqClusterNetworkDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterNetworkName"))
)
if mibBuilder.loadTexts:
    cpqClusterNetworkDegraded.setStatus(
        ""
    )

cpqClusterNetworkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 15008)
)
cpqClusterNetworkFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQCLUSTER-MIB", "cpqClusterNetworkName"))
)
if mibBuilder.loadTexts:
    cpqClusterNetworkFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQCLUSTER-MIB",
    **{"cpqClusterDegraded": cpqClusterDegraded,
       "cpqClusterFailed": cpqClusterFailed,
       "cpqClusterNodeDegraded": cpqClusterNodeDegraded,
       "cpqClusterNodeFailed": cpqClusterNodeFailed,
       "cpqClusterResourceDegraded": cpqClusterResourceDegraded,
       "cpqClusterResourceFailed": cpqClusterResourceFailed,
       "cpqClusterNetworkDegraded": cpqClusterNetworkDegraded,
       "cpqClusterNetworkFailed": cpqClusterNetworkFailed,
       "cpqCluster": cpqCluster,
       "cpqClusterMibRev": cpqClusterMibRev,
       "cpqClusterMibRevMajor": cpqClusterMibRevMajor,
       "cpqClusterMibRevMinor": cpqClusterMibRevMinor,
       "cpqClusterMibCondition": cpqClusterMibCondition,
       "cpqClusterComponent": cpqClusterComponent,
       "cpqClusterInterface": cpqClusterInterface,
       "cpqClusterOsCommon": cpqClusterOsCommon,
       "cpqClusterOsCommonPollFreq": cpqClusterOsCommonPollFreq,
       "cpqClusterOsCommonModuleTable": cpqClusterOsCommonModuleTable,
       "cpqClusterOsCommonModuleEntry": cpqClusterOsCommonModuleEntry,
       "cpqClusterOsCommonModuleIndex": cpqClusterOsCommonModuleIndex,
       "cpqClusterOsCommonModuleName": cpqClusterOsCommonModuleName,
       "cpqClusterOsCommonModuleVersion": cpqClusterOsCommonModuleVersion,
       "cpqClusterOsCommonModuleDate": cpqClusterOsCommonModuleDate,
       "cpqClusterOsCommonModulePurpose": cpqClusterOsCommonModulePurpose,
       "cpqClusterInfo": cpqClusterInfo,
       "cpqClusterName": cpqClusterName,
       "cpqClusterCondition": cpqClusterCondition,
       "cpqClusterIpAddress": cpqClusterIpAddress,
       "cpqClusterQuorumResource": cpqClusterQuorumResource,
       "cpqClusterMajorVersion": cpqClusterMajorVersion,
       "cpqClusterMinorVersion": cpqClusterMinorVersion,
       "cpqClusterCSDVersion": cpqClusterCSDVersion,
       "cpqClusterVendorId": cpqClusterVendorId,
       "cpqClusterResourceAggregateCondition": cpqClusterResourceAggregateCondition,
       "cpqClusterNetworkAggregateCondition": cpqClusterNetworkAggregateCondition,
       "cpqClusterNode": cpqClusterNode,
       "cpqClusterNodeTable": cpqClusterNodeTable,
       "cpqClusterNodeEntry": cpqClusterNodeEntry,
       "cpqClusterNodeIndex": cpqClusterNodeIndex,
       "cpqClusterNodeName": cpqClusterNodeName,
       "cpqClusterNodeStatus": cpqClusterNodeStatus,
       "cpqClusterNodeCondition": cpqClusterNodeCondition,
       "cpqClusterResource": cpqClusterResource,
       "cpqClusterResourceTable": cpqClusterResourceTable,
       "cpqClusterResourceEntry": cpqClusterResourceEntry,
       "cpqClusterResourceIndex": cpqClusterResourceIndex,
       "cpqClusterResourceName": cpqClusterResourceName,
       "cpqClusterResourceType": cpqClusterResourceType,
       "cpqClusterResourceState": cpqClusterResourceState,
       "cpqClusterResourceOwnerNode": cpqClusterResourceOwnerNode,
       "cpqClusterResourcePhysId": cpqClusterResourcePhysId,
       "cpqClusterResourceCondition": cpqClusterResourceCondition,
       "cpqClusterResourceDriveLetter": cpqClusterResourceDriveLetter,
       "cpqClusterResourceIpAddress": cpqClusterResourceIpAddress,
       "cpqClusterResourceGroupName": cpqClusterResourceGroupName,
       "cpqClusterInterconnect": cpqClusterInterconnect,
       "cpqClusterInterconnectTable": cpqClusterInterconnectTable,
       "cpqClusterInterconnectEntry": cpqClusterInterconnectEntry,
       "cpqClusterInterconnectIndex": cpqClusterInterconnectIndex,
       "cpqClusterInterconnectPhysId": cpqClusterInterconnectPhysId,
       "cpqClusterInterconnectTransport": cpqClusterInterconnectTransport,
       "cpqClusterInterconnectAddress": cpqClusterInterconnectAddress,
       "cpqClusterInterconnectNetworkName": cpqClusterInterconnectNetworkName,
       "cpqClusterInterconnectNodeName": cpqClusterInterconnectNodeName,
       "cpqClusterInterconnectRole": cpqClusterInterconnectRole,
       "cpqClusterNetwork": cpqClusterNetwork,
       "cpqClusterNetworkTable": cpqClusterNetworkTable,
       "cpqClusterNetworkEntry": cpqClusterNetworkEntry,
       "cpqClusterNetworkIndex": cpqClusterNetworkIndex,
       "cpqClusterNetworkName": cpqClusterNetworkName,
       "cpqClusterNetworkAddressMask": cpqClusterNetworkAddressMask,
       "cpqClusterNetworkDescription": cpqClusterNetworkDescription,
       "cpqClusterNetworkRole": cpqClusterNetworkRole,
       "cpqClusterNetworkState": cpqClusterNetworkState,
       "cpqClusterNetworkCondition": cpqClusterNetworkCondition,
       "cpqClusterTrap": cpqClusterTrap}
)
