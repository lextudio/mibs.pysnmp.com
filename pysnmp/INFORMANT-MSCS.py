# SNMP MIB module (INFORMANT-MSCS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-MSCS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:16 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(InstanceName,
 WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "InstanceName",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

mscs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31)
)
mscs.setRevisions(
        ("2005-04-29 17:51",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscsCluster_ObjectIdentity = ObjectIdentity
mscsCluster = _MscsCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1)
)
if mibBuilder.loadTexts:
    mscsCluster.setStatus("current")
_MscsClusterBuildNumber_Type = Integer32
_MscsClusterBuildNumber_Object = MibScalar
mscsClusterBuildNumber = _MscsClusterBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 1),
    _MscsClusterBuildNumber_Type()
)
mscsClusterBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterBuildNumber.setStatus("current")
_MscsClusterHighestVersion_Type = Integer32
_MscsClusterHighestVersion_Object = MibScalar
mscsClusterHighestVersion = _MscsClusterHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 2),
    _MscsClusterHighestVersion_Type()
)
mscsClusterHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterHighestVersion.setStatus("current")
_MscsClusterLowestVersion_Type = Integer32
_MscsClusterLowestVersion_Object = MibScalar
mscsClusterLowestVersion = _MscsClusterLowestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 3),
    _MscsClusterLowestVersion_Type()
)
mscsClusterLowestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterLowestVersion.setStatus("current")
_MscsClusterCSDVersion_Type = WtcsDisplayString
_MscsClusterCSDVersion_Object = MibScalar
mscsClusterCSDVersion = _MscsClusterCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 4),
    _MscsClusterCSDVersion_Type()
)
mscsClusterCSDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterCSDVersion.setStatus("current")
_MscsClusterFlags_Type = Integer32
_MscsClusterFlags_Object = MibScalar
mscsClusterFlags = _MscsClusterFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 5),
    _MscsClusterFlags_Type()
)
mscsClusterFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterFlags.setStatus("current")
_MscsClusterMajorVersion_Type = Integer32
_MscsClusterMajorVersion_Object = MibScalar
mscsClusterMajorVersion = _MscsClusterMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 6),
    _MscsClusterMajorVersion_Type()
)
mscsClusterMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterMajorVersion.setStatus("current")
_MscsClusterMinorVersion_Type = Integer32
_MscsClusterMinorVersion_Object = MibScalar
mscsClusterMinorVersion = _MscsClusterMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 7),
    _MscsClusterMinorVersion_Type()
)
mscsClusterMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterMinorVersion.setStatus("current")
_MscsClusterMixedVersion_Type = TruthValue
_MscsClusterMixedVersion_Object = MibScalar
mscsClusterMixedVersion = _MscsClusterMixedVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 8),
    _MscsClusterMixedVersion_Type()
)
mscsClusterMixedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterMixedVersion.setStatus("current")
_MscsClusterName_Type = WtcsDisplayString
_MscsClusterName_Object = MibScalar
mscsClusterName = _MscsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 9),
    _MscsClusterName_Type()
)
mscsClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterName.setStatus("current")
_MscsClusterQuorumLogSize_Type = Integer32
_MscsClusterQuorumLogSize_Object = MibScalar
mscsClusterQuorumLogSize = _MscsClusterQuorumLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 10),
    _MscsClusterQuorumLogSize_Type()
)
mscsClusterQuorumLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterQuorumLogSize.setStatus("current")
_MscsClusterQuorumPath_Type = WtcsDisplayString
_MscsClusterQuorumPath_Object = MibScalar
mscsClusterQuorumPath = _MscsClusterQuorumPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 11),
    _MscsClusterQuorumPath_Type()
)
mscsClusterQuorumPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterQuorumPath.setStatus("current")
_MscsClusterVendorId_Type = WtcsDisplayString
_MscsClusterVendorId_Object = MibScalar
mscsClusterVendorId = _MscsClusterVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 12),
    _MscsClusterVendorId_Type()
)
mscsClusterVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterVendorId.setStatus("current")


class _MscsClusterDefaultNetworkRole_Type(Integer32):
    """Custom type mscsClusterDefaultNetworkRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientAccess", 2),
          ("internalAndClient", 3),
          ("internalUse", 1),
          ("none", 0))
    )


_MscsClusterDefaultNetworkRole_Type.__name__ = "Integer32"
_MscsClusterDefaultNetworkRole_Object = MibScalar
mscsClusterDefaultNetworkRole = _MscsClusterDefaultNetworkRole_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 13),
    _MscsClusterDefaultNetworkRole_Type()
)
mscsClusterDefaultNetworkRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterDefaultNetworkRole.setStatus("current")
_MscsClusterDescription_Type = WtcsDisplayString
_MscsClusterDescription_Object = MibScalar
mscsClusterDescription = _MscsClusterDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 1, 14),
    _MscsClusterDescription_Type()
)
mscsClusterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterDescription.setStatus("current")
_MscsClusterPropertiesTable_Object = MibTable
mscsClusterPropertiesTable = _MscsClusterPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 2)
)
if mibBuilder.loadTexts:
    mscsClusterPropertiesTable.setStatus("current")
_MscsClusterPropertiesEntry_Object = MibTableRow
mscsClusterPropertiesEntry = _MscsClusterPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 2, 1)
)
mscsClusterPropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsClusterPropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsClusterPropertiesEntry.setStatus("current")


class _MscsClusterPropertiesIndex_Type(Integer32):
    """Custom type mscsClusterPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsClusterPropertiesIndex_Type.__name__ = "Integer32"
_MscsClusterPropertiesIndex_Object = MibTableColumn
mscsClusterPropertiesIndex = _MscsClusterPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 2, 1, 1),
    _MscsClusterPropertiesIndex_Type()
)
mscsClusterPropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterPropertiesIndex.setStatus("current")
_MscsClusterPropertiesName_Type = WtcsDisplayString
_MscsClusterPropertiesName_Object = MibTableColumn
mscsClusterPropertiesName = _MscsClusterPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 2, 1, 2),
    _MscsClusterPropertiesName_Type()
)
mscsClusterPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterPropertiesName.setStatus("current")
_MscsClusterPropertiesValue_Type = WtcsDisplayString
_MscsClusterPropertiesValue_Object = MibTableColumn
mscsClusterPropertiesValue = _MscsClusterPropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 2, 1, 3),
    _MscsClusterPropertiesValue_Type()
)
mscsClusterPropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsClusterPropertiesValue.setStatus("current")
_MscsNetInterfaceTable_Object = MibTable
mscsNetInterfaceTable = _MscsNetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3)
)
if mibBuilder.loadTexts:
    mscsNetInterfaceTable.setStatus("current")
_MscsNetInterfaceEntry_Object = MibTableRow
mscsNetInterfaceEntry = _MscsNetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1)
)
mscsNetInterfaceEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNetInterfaceNameIndex"),
)
if mibBuilder.loadTexts:
    mscsNetInterfaceEntry.setStatus("current")
_MscsNetInterfaceNameIndex_Type = InstanceName
_MscsNetInterfaceNameIndex_Object = MibTableColumn
mscsNetInterfaceNameIndex = _MscsNetInterfaceNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 1),
    _MscsNetInterfaceNameIndex_Type()
)
mscsNetInterfaceNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceNameIndex.setStatus("current")
_MscsNetInterfaceNameFull_Type = WtcsDisplayString
_MscsNetInterfaceNameFull_Object = MibTableColumn
mscsNetInterfaceNameFull = _MscsNetInterfaceNameFull_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 2),
    _MscsNetInterfaceNameFull_Type()
)
mscsNetInterfaceNameFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceNameFull.setStatus("current")


class _MscsNetInterfaceState_Type(Integer32):
    """Custom type mscsNetInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("unavailable", 0),
          ("unknown", -1),
          ("unreachable", 2),
          ("up", 3))
    )


_MscsNetInterfaceState_Type.__name__ = "Integer32"
_MscsNetInterfaceState_Object = MibTableColumn
mscsNetInterfaceState = _MscsNetInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 3),
    _MscsNetInterfaceState_Type()
)
mscsNetInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceState.setStatus("current")
_MscsNetInterfaceAdapter_Type = WtcsDisplayString
_MscsNetInterfaceAdapter_Object = MibTableColumn
mscsNetInterfaceAdapter = _MscsNetInterfaceAdapter_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 4),
    _MscsNetInterfaceAdapter_Type()
)
mscsNetInterfaceAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceAdapter.setStatus("current")
_MscsNetInterfaceAddress_Type = WtcsDisplayString
_MscsNetInterfaceAddress_Object = MibTableColumn
mscsNetInterfaceAddress = _MscsNetInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 5),
    _MscsNetInterfaceAddress_Type()
)
mscsNetInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceAddress.setStatus("current")
_MscsNetInterfaceDescription_Type = WtcsDisplayString
_MscsNetInterfaceDescription_Object = MibTableColumn
mscsNetInterfaceDescription = _MscsNetInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 6),
    _MscsNetInterfaceDescription_Type()
)
mscsNetInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceDescription.setStatus("current")
_MscsNetInterfaceNetwork_Type = WtcsDisplayString
_MscsNetInterfaceNetwork_Object = MibTableColumn
mscsNetInterfaceNetwork = _MscsNetInterfaceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 7),
    _MscsNetInterfaceNetwork_Type()
)
mscsNetInterfaceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceNetwork.setStatus("current")
_MscsNetInterfaceNode_Type = WtcsDisplayString
_MscsNetInterfaceNode_Object = MibTableColumn
mscsNetInterfaceNode = _MscsNetInterfaceNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 3, 1, 8),
    _MscsNetInterfaceNode_Type()
)
mscsNetInterfaceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfaceNode.setStatus("current")
_MscsNetInterfacePropertiesTable_Object = MibTable
mscsNetInterfacePropertiesTable = _MscsNetInterfacePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 4)
)
if mibBuilder.loadTexts:
    mscsNetInterfacePropertiesTable.setStatus("current")
_MscsNetInterfacePropertiesEntry_Object = MibTableRow
mscsNetInterfacePropertiesEntry = _MscsNetInterfacePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 4, 1)
)
mscsNetInterfacePropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNetInterfaceNameIndex"),
    (0, "INFORMANT-MSCS", "mscsNetInterfacePropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsNetInterfacePropertiesEntry.setStatus("current")


class _MscsNetInterfacePropertiesIndex_Type(Integer32):
    """Custom type mscsNetInterfacePropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsNetInterfacePropertiesIndex_Type.__name__ = "Integer32"
_MscsNetInterfacePropertiesIndex_Object = MibTableColumn
mscsNetInterfacePropertiesIndex = _MscsNetInterfacePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 4, 1, 1),
    _MscsNetInterfacePropertiesIndex_Type()
)
mscsNetInterfacePropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfacePropertiesIndex.setStatus("current")
_MscsNetInterfacePropertiesName_Type = WtcsDisplayString
_MscsNetInterfacePropertiesName_Object = MibTableColumn
mscsNetInterfacePropertiesName = _MscsNetInterfacePropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 4, 1, 2),
    _MscsNetInterfacePropertiesName_Type()
)
mscsNetInterfacePropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfacePropertiesName.setStatus("current")
_MscsNetInterfacePropertiesValue_Type = WtcsDisplayString
_MscsNetInterfacePropertiesValue_Object = MibTableColumn
mscsNetInterfacePropertiesValue = _MscsNetInterfacePropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 4, 1, 3),
    _MscsNetInterfacePropertiesValue_Type()
)
mscsNetInterfacePropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetInterfacePropertiesValue.setStatus("current")
_MscsNetworkTable_Object = MibTable
mscsNetworkTable = _MscsNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5)
)
if mibBuilder.loadTexts:
    mscsNetworkTable.setStatus("current")
_MscsNetworkEntry_Object = MibTableRow
mscsNetworkEntry = _MscsNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1)
)
mscsNetworkEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNetworkNameIndex"),
)
if mibBuilder.loadTexts:
    mscsNetworkEntry.setStatus("current")
_MscsNetworkNameIndex_Type = InstanceName
_MscsNetworkNameIndex_Object = MibTableColumn
mscsNetworkNameIndex = _MscsNetworkNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 1),
    _MscsNetworkNameIndex_Type()
)
mscsNetworkNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkNameIndex.setStatus("current")
_MscsNetworkNameFull_Type = WtcsDisplayString
_MscsNetworkNameFull_Object = MibTableColumn
mscsNetworkNameFull = _MscsNetworkNameFull_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 2),
    _MscsNetworkNameFull_Type()
)
mscsNetworkNameFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkNameFull.setStatus("current")
_MscsNetworkNetInterfaces_Type = WtcsDisplayString
_MscsNetworkNetInterfaces_Object = MibTableColumn
mscsNetworkNetInterfaces = _MscsNetworkNetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 3),
    _MscsNetworkNetInterfaces_Type()
)
mscsNetworkNetInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkNetInterfaces.setStatus("current")
_MscsNetworkNetworkID_Type = WtcsDisplayString
_MscsNetworkNetworkID_Object = MibTableColumn
mscsNetworkNetworkID = _MscsNetworkNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 4),
    _MscsNetworkNetworkID_Type()
)
mscsNetworkNetworkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkNetworkID.setStatus("current")


class _MscsNetworkState_Type(Integer32):
    """Custom type mscsNetworkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("partitioned", 2),
          ("unavailable", 0),
          ("unknown", -1),
          ("up", 3))
    )


_MscsNetworkState_Type.__name__ = "Integer32"
_MscsNetworkState_Object = MibTableColumn
mscsNetworkState = _MscsNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 5),
    _MscsNetworkState_Type()
)
mscsNetworkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkState.setStatus("current")
_MscsNetworkAddress_Type = WtcsDisplayString
_MscsNetworkAddress_Object = MibTableColumn
mscsNetworkAddress = _MscsNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 6),
    _MscsNetworkAddress_Type()
)
mscsNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkAddress.setStatus("current")
_MscsNetworkAddressMask_Type = WtcsDisplayString
_MscsNetworkAddressMask_Object = MibTableColumn
mscsNetworkAddressMask = _MscsNetworkAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 7),
    _MscsNetworkAddressMask_Type()
)
mscsNetworkAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkAddressMask.setStatus("current")
_MscsNetworkDescription_Type = WtcsDisplayString
_MscsNetworkDescription_Object = MibTableColumn
mscsNetworkDescription = _MscsNetworkDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 8),
    _MscsNetworkDescription_Type()
)
mscsNetworkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkDescription.setStatus("current")


class _MscsNetworkRole_Type(Integer32):
    """Custom type mscsNetworkRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientAccess", 2),
          ("internalAndClient", 3),
          ("none", 0),
          ("unternalUse", 1))
    )


_MscsNetworkRole_Type.__name__ = "Integer32"
_MscsNetworkRole_Object = MibTableColumn
mscsNetworkRole = _MscsNetworkRole_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 5, 1, 9),
    _MscsNetworkRole_Type()
)
mscsNetworkRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkRole.setStatus("current")
_MscsNetworkPropertiesTable_Object = MibTable
mscsNetworkPropertiesTable = _MscsNetworkPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 6)
)
if mibBuilder.loadTexts:
    mscsNetworkPropertiesTable.setStatus("current")
_MscsNetworkPropertiesEntry_Object = MibTableRow
mscsNetworkPropertiesEntry = _MscsNetworkPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 6, 1)
)
mscsNetworkPropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNetworkNameIndex"),
    (0, "INFORMANT-MSCS", "mscsNetworkPropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsNetworkPropertiesEntry.setStatus("current")


class _MscsNetworkPropertiesIndex_Type(Integer32):
    """Custom type mscsNetworkPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsNetworkPropertiesIndex_Type.__name__ = "Integer32"
_MscsNetworkPropertiesIndex_Object = MibTableColumn
mscsNetworkPropertiesIndex = _MscsNetworkPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 6, 1, 1),
    _MscsNetworkPropertiesIndex_Type()
)
mscsNetworkPropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkPropertiesIndex.setStatus("current")
_MscsNetworkPropertiesName_Type = WtcsDisplayString
_MscsNetworkPropertiesName_Object = MibTableColumn
mscsNetworkPropertiesName = _MscsNetworkPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 6, 1, 2),
    _MscsNetworkPropertiesName_Type()
)
mscsNetworkPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkPropertiesName.setStatus("current")
_MscsNetworkPropertiesValue_Type = WtcsDisplayString
_MscsNetworkPropertiesValue_Object = MibTableColumn
mscsNetworkPropertiesValue = _MscsNetworkPropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 6, 1, 3),
    _MscsNetworkPropertiesValue_Type()
)
mscsNetworkPropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNetworkPropertiesValue.setStatus("current")
_MscsNodeTable_Object = MibTable
mscsNodeTable = _MscsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7)
)
if mibBuilder.loadTexts:
    mscsNodeTable.setStatus("current")
_MscsNodeEntry_Object = MibTableRow
mscsNodeEntry = _MscsNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1)
)
mscsNodeEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNodeNameIndex"),
)
if mibBuilder.loadTexts:
    mscsNodeEntry.setStatus("current")
_MscsNodeNameIndex_Type = InstanceName
_MscsNodeNameIndex_Object = MibTableColumn
mscsNodeNameIndex = _MscsNodeNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 1),
    _MscsNodeNameIndex_Type()
)
mscsNodeNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeNameIndex.setStatus("current")
_MscsNodeNameFull_Type = WtcsDisplayString
_MscsNodeNameFull_Object = MibTableColumn
mscsNodeNameFull = _MscsNodeNameFull_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 2),
    _MscsNodeNameFull_Type()
)
mscsNodeNameFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeNameFull.setStatus("current")
_MscsNodeNetInterfaces_Type = WtcsDisplayString
_MscsNodeNetInterfaces_Object = MibTableColumn
mscsNodeNetInterfaces = _MscsNodeNetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 3),
    _MscsNodeNetInterfaces_Type()
)
mscsNodeNetInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeNetInterfaces.setStatus("current")
_MscsNodeNodeID_Type = WtcsDisplayString
_MscsNodeNodeID_Object = MibTableColumn
mscsNodeNodeID = _MscsNodeNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 4),
    _MscsNodeNodeID_Type()
)
mscsNodeNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeNodeID.setStatus("current")


class _MscsNodeState_Type(Integer32):
    """Custom type mscsNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("joining", 3),
          ("paused", 2),
          ("unknown", -1),
          ("up", 0))
    )


_MscsNodeState_Type.__name__ = "Integer32"
_MscsNodeState_Object = MibTableColumn
mscsNodeState = _MscsNodeState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 5),
    _MscsNodeState_Type()
)
mscsNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeState.setStatus("current")
_MscsNodeBuildNumber_Type = Gauge32
_MscsNodeBuildNumber_Object = MibTableColumn
mscsNodeBuildNumber = _MscsNodeBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 6),
    _MscsNodeBuildNumber_Type()
)
mscsNodeBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeBuildNumber.setStatus("current")
_MscsNodeCSDVersion_Type = WtcsDisplayString
_MscsNodeCSDVersion_Object = MibTableColumn
mscsNodeCSDVersion = _MscsNodeCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 7),
    _MscsNodeCSDVersion_Type()
)
mscsNodeCSDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeCSDVersion.setStatus("current")
_MscsNodeDescription_Type = WtcsDisplayString
_MscsNodeDescription_Object = MibTableColumn
mscsNodeDescription = _MscsNodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 8),
    _MscsNodeDescription_Type()
)
mscsNodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeDescription.setStatus("current")
_MscsNodeEnableEventLogReplicate_Type = TruthValue
_MscsNodeEnableEventLogReplicate_Object = MibTableColumn
mscsNodeEnableEventLogReplicate = _MscsNodeEnableEventLogReplicate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 9),
    _MscsNodeEnableEventLogReplicate_Type()
)
mscsNodeEnableEventLogReplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeEnableEventLogReplicate.setStatus("current")
_MscsNodeMajorVersion_Type = Gauge32
_MscsNodeMajorVersion_Object = MibTableColumn
mscsNodeMajorVersion = _MscsNodeMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 10),
    _MscsNodeMajorVersion_Type()
)
mscsNodeMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeMajorVersion.setStatus("current")
_MscsNodeMinorVersion_Type = Gauge32
_MscsNodeMinorVersion_Object = MibTableColumn
mscsNodeMinorVersion = _MscsNodeMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 11),
    _MscsNodeMinorVersion_Type()
)
mscsNodeMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeMinorVersion.setStatus("current")
_MscsNodeHighestVersion_Type = Gauge32
_MscsNodeHighestVersion_Object = MibTableColumn
mscsNodeHighestVersion = _MscsNodeHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 12),
    _MscsNodeHighestVersion_Type()
)
mscsNodeHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeHighestVersion.setStatus("current")
_MscsNodeLowestVersion_Type = Gauge32
_MscsNodeLowestVersion_Object = MibTableColumn
mscsNodeLowestVersion = _MscsNodeLowestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 7, 1, 13),
    _MscsNodeLowestVersion_Type()
)
mscsNodeLowestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodeLowestVersion.setStatus("current")
_MscsNodePropertiesTable_Object = MibTable
mscsNodePropertiesTable = _MscsNodePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 8)
)
if mibBuilder.loadTexts:
    mscsNodePropertiesTable.setStatus("current")
_MscsNodePropertiesEntry_Object = MibTableRow
mscsNodePropertiesEntry = _MscsNodePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 8, 1)
)
mscsNodePropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsNodeNameIndex"),
    (0, "INFORMANT-MSCS", "mscsNodePropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsNodePropertiesEntry.setStatus("current")


class _MscsNodePropertiesIndex_Type(Integer32):
    """Custom type mscsNodePropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsNodePropertiesIndex_Type.__name__ = "Integer32"
_MscsNodePropertiesIndex_Object = MibTableColumn
mscsNodePropertiesIndex = _MscsNodePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 8, 1, 1),
    _MscsNodePropertiesIndex_Type()
)
mscsNodePropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodePropertiesIndex.setStatus("current")
_MscsNodePropertiesName_Type = WtcsDisplayString
_MscsNodePropertiesName_Object = MibTableColumn
mscsNodePropertiesName = _MscsNodePropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 8, 1, 2),
    _MscsNodePropertiesName_Type()
)
mscsNodePropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodePropertiesName.setStatus("current")
_MscsNodePropertiesValue_Type = WtcsDisplayString
_MscsNodePropertiesValue_Object = MibTableColumn
mscsNodePropertiesValue = _MscsNodePropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 8, 1, 3),
    _MscsNodePropertiesValue_Type()
)
mscsNodePropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsNodePropertiesValue.setStatus("current")
_MscsResGroupTable_Object = MibTable
mscsResGroupTable = _MscsResGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9)
)
if mibBuilder.loadTexts:
    mscsResGroupTable.setStatus("current")
_MscsResGroupEntry_Object = MibTableRow
mscsResGroupEntry = _MscsResGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1)
)
mscsResGroupEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsResGroupNameIndex"),
)
if mibBuilder.loadTexts:
    mscsResGroupEntry.setStatus("current")
_MscsResGroupNameIndex_Type = InstanceName
_MscsResGroupNameIndex_Object = MibTableColumn
mscsResGroupNameIndex = _MscsResGroupNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 1),
    _MscsResGroupNameIndex_Type()
)
mscsResGroupNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupNameIndex.setStatus("current")
_MscsResGroupNameFull_Type = WtcsDisplayString
_MscsResGroupNameFull_Object = MibTableColumn
mscsResGroupNameFull = _MscsResGroupNameFull_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 2),
    _MscsResGroupNameFull_Type()
)
mscsResGroupNameFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupNameFull.setStatus("current")
_MscsResGroupOwnerNode_Type = WtcsDisplayString
_MscsResGroupOwnerNode_Object = MibTableColumn
mscsResGroupOwnerNode = _MscsResGroupOwnerNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 3),
    _MscsResGroupOwnerNode_Type()
)
mscsResGroupOwnerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupOwnerNode.setStatus("current")
_MscsResGroupResources_Type = WtcsDisplayString
_MscsResGroupResources_Object = MibTableColumn
mscsResGroupResources = _MscsResGroupResources_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 4),
    _MscsResGroupResources_Type()
)
mscsResGroupResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupResources.setStatus("current")


class _MscsResGroupState_Type(Integer32):
    """Custom type mscsResGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("offline", 1),
          ("online", 0),
          ("partialOnline", 3),
          ("pending", 4),
          ("unknown", -1))
    )


_MscsResGroupState_Type.__name__ = "Integer32"
_MscsResGroupState_Object = MibTableColumn
mscsResGroupState = _MscsResGroupState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 5),
    _MscsResGroupState_Type()
)
mscsResGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupState.setStatus("current")
_MscsResGroupAntiAffinityClassNam_Type = WtcsDisplayString
_MscsResGroupAntiAffinityClassNam_Object = MibTableColumn
mscsResGroupAntiAffinityClassNam = _MscsResGroupAntiAffinityClassNam_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 6),
    _MscsResGroupAntiAffinityClassNam_Type()
)
mscsResGroupAntiAffinityClassNam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupAntiAffinityClassNam.setStatus("current")


class _MscsResGroupAutoFailbackType_Type(Integer32):
    """Custom type mscsResGroupAutoFailbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowFailback", 1),
          ("failbackTypeCount", 2),
          ("preventFailback", 0))
    )


_MscsResGroupAutoFailbackType_Type.__name__ = "Integer32"
_MscsResGroupAutoFailbackType_Object = MibTableColumn
mscsResGroupAutoFailbackType = _MscsResGroupAutoFailbackType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 7),
    _MscsResGroupAutoFailbackType_Type()
)
mscsResGroupAutoFailbackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupAutoFailbackType.setStatus("current")
_MscsResGroupDescription_Type = WtcsDisplayString
_MscsResGroupDescription_Object = MibTableColumn
mscsResGroupDescription = _MscsResGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 8),
    _MscsResGroupDescription_Type()
)
mscsResGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupDescription.setStatus("current")


class _MscsResGroupFailbackWindowEnd_Type(Integer32):
    """Custom type mscsResGroupFailbackWindowEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_MscsResGroupFailbackWindowEnd_Type.__name__ = "Integer32"
_MscsResGroupFailbackWindowEnd_Object = MibTableColumn
mscsResGroupFailbackWindowEnd = _MscsResGroupFailbackWindowEnd_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 9),
    _MscsResGroupFailbackWindowEnd_Type()
)
mscsResGroupFailbackWindowEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupFailbackWindowEnd.setStatus("current")
if mibBuilder.loadTexts:
    mscsResGroupFailbackWindowEnd.setUnits("hours")


class _MscsResGroupFailbackWindowStart_Type(Integer32):
    """Custom type mscsResGroupFailbackWindowStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_MscsResGroupFailbackWindowStart_Type.__name__ = "Integer32"
_MscsResGroupFailbackWindowStart_Object = MibTableColumn
mscsResGroupFailbackWindowStart = _MscsResGroupFailbackWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 10),
    _MscsResGroupFailbackWindowStart_Type()
)
mscsResGroupFailbackWindowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupFailbackWindowStart.setStatus("current")
if mibBuilder.loadTexts:
    mscsResGroupFailbackWindowStart.setUnits("hours")


class _MscsResGroupFailoverPeriod_Type(Integer32):
    """Custom type mscsResGroupFailoverPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1193),
    )


_MscsResGroupFailoverPeriod_Type.__name__ = "Integer32"
_MscsResGroupFailoverPeriod_Object = MibTableColumn
mscsResGroupFailoverPeriod = _MscsResGroupFailoverPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 11),
    _MscsResGroupFailoverPeriod_Type()
)
mscsResGroupFailoverPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupFailoverPeriod.setStatus("current")
if mibBuilder.loadTexts:
    mscsResGroupFailoverPeriod.setUnits("hours")
_MscsResGroupFailoverThreshold_Type = Gauge32
_MscsResGroupFailoverThreshold_Object = MibTableColumn
mscsResGroupFailoverThreshold = _MscsResGroupFailoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 12),
    _MscsResGroupFailoverThreshold_Type()
)
mscsResGroupFailoverThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupFailoverThreshold.setStatus("current")
_MscsResGroupPersistentState_Type = TruthValue
_MscsResGroupPersistentState_Object = MibTableColumn
mscsResGroupPersistentState = _MscsResGroupPersistentState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 9, 1, 13),
    _MscsResGroupPersistentState_Type()
)
mscsResGroupPersistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupPersistentState.setStatus("current")
_MscsResGroupPropertiesTable_Object = MibTable
mscsResGroupPropertiesTable = _MscsResGroupPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 10)
)
if mibBuilder.loadTexts:
    mscsResGroupPropertiesTable.setStatus("current")
_MscsResGroupPropertiesEntry_Object = MibTableRow
mscsResGroupPropertiesEntry = _MscsResGroupPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 10, 1)
)
mscsResGroupPropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsResGroupNameIndex"),
    (0, "INFORMANT-MSCS", "mscsResGroupPropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsResGroupPropertiesEntry.setStatus("current")


class _MscsResGroupPropertiesIndex_Type(Integer32):
    """Custom type mscsResGroupPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsResGroupPropertiesIndex_Type.__name__ = "Integer32"
_MscsResGroupPropertiesIndex_Object = MibTableColumn
mscsResGroupPropertiesIndex = _MscsResGroupPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 10, 1, 1),
    _MscsResGroupPropertiesIndex_Type()
)
mscsResGroupPropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupPropertiesIndex.setStatus("current")
_MscsResGroupPropertiesName_Type = WtcsDisplayString
_MscsResGroupPropertiesName_Object = MibTableColumn
mscsResGroupPropertiesName = _MscsResGroupPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 10, 1, 2),
    _MscsResGroupPropertiesName_Type()
)
mscsResGroupPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupPropertiesName.setStatus("current")
_MscsResGroupPropertiesValue_Type = WtcsDisplayString
_MscsResGroupPropertiesValue_Object = MibTableColumn
mscsResGroupPropertiesValue = _MscsResGroupPropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 10, 1, 3),
    _MscsResGroupPropertiesValue_Type()
)
mscsResGroupPropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResGroupPropertiesValue.setStatus("current")
_MscsResourceTable_Object = MibTable
mscsResourceTable = _MscsResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11)
)
if mibBuilder.loadTexts:
    mscsResourceTable.setStatus("current")
_MscsResourceEntry_Object = MibTableRow
mscsResourceEntry = _MscsResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1)
)
mscsResourceEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsResourceNameIndex"),
)
if mibBuilder.loadTexts:
    mscsResourceEntry.setStatus("current")
_MscsResourceNameIndex_Type = InstanceName
_MscsResourceNameIndex_Object = MibTableColumn
mscsResourceNameIndex = _MscsResourceNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 1),
    _MscsResourceNameIndex_Type()
)
mscsResourceNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceNameIndex.setStatus("current")
_MscsResourceNameFull_Type = WtcsDisplayString
_MscsResourceNameFull_Object = MibTableColumn
mscsResourceNameFull = _MscsResourceNameFull_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 2),
    _MscsResourceNameFull_Type()
)
mscsResourceNameFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceNameFull.setStatus("current")
_MscsResourceDependencies_Type = WtcsDisplayString
_MscsResourceDependencies_Object = MibTableColumn
mscsResourceDependencies = _MscsResourceDependencies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 3),
    _MscsResourceDependencies_Type()
)
mscsResourceDependencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceDependencies.setStatus("current")
_MscsResourceDependents_Type = WtcsDisplayString
_MscsResourceDependents_Object = MibTableColumn
mscsResourceDependents = _MscsResourceDependents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 4),
    _MscsResourceDependents_Type()
)
mscsResourceDependents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceDependents.setStatus("current")
_MscsResourceGroup_Type = WtcsDisplayString
_MscsResourceGroup_Object = MibTableColumn
mscsResourceGroup = _MscsResourceGroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 5),
    _MscsResourceGroup_Type()
)
mscsResourceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceGroup.setStatus("current")
_MscsResourceOwnerNode_Type = WtcsDisplayString
_MscsResourceOwnerNode_Object = MibTableColumn
mscsResourceOwnerNode = _MscsResourceOwnerNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 6),
    _MscsResourceOwnerNode_Type()
)
mscsResourceOwnerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceOwnerNode.setStatus("current")
_MscsResourcePossibleOwnerNodes_Type = WtcsDisplayString
_MscsResourcePossibleOwnerNodes_Object = MibTableColumn
mscsResourcePossibleOwnerNodes = _MscsResourcePossibleOwnerNodes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 7),
    _MscsResourcePossibleOwnerNodes_Type()
)
mscsResourcePossibleOwnerNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePossibleOwnerNodes.setStatus("current")


class _MscsResourceState_Type(Integer32):
    """Custom type mscsResourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              128,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("inherited", 0),
          ("initializing", 1),
          ("offline", 3),
          ("offlinePending", 130),
          ("online", 2),
          ("onlinePending", 129),
          ("pending", 128),
          ("unknown", -1))
    )


_MscsResourceState_Type.__name__ = "Integer32"
_MscsResourceState_Object = MibTableColumn
mscsResourceState = _MscsResourceState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 8),
    _MscsResourceState_Type()
)
mscsResourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceState.setStatus("current")
_MscsResourceTypeName_Type = WtcsDisplayString
_MscsResourceTypeName_Object = MibTableColumn
mscsResourceTypeName = _MscsResourceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 9),
    _MscsResourceTypeName_Type()
)
mscsResourceTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceTypeName.setStatus("current")
_MscsResourceDebugPrefix_Type = WtcsDisplayString
_MscsResourceDebugPrefix_Object = MibTableColumn
mscsResourceDebugPrefix = _MscsResourceDebugPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 10),
    _MscsResourceDebugPrefix_Type()
)
mscsResourceDebugPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceDebugPrefix.setStatus("current")
_MscsResourceDescription_Type = WtcsDisplayString
_MscsResourceDescription_Object = MibTableColumn
mscsResourceDescription = _MscsResourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 11),
    _MscsResourceDescription_Type()
)
mscsResourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceDescription.setStatus("current")
_MscsResourceIsAlivePollInterval_Type = Gauge32
_MscsResourceIsAlivePollInterval_Object = MibTableColumn
mscsResourceIsAlivePollInterval = _MscsResourceIsAlivePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 12),
    _MscsResourceIsAlivePollInterval_Type()
)
mscsResourceIsAlivePollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceIsAlivePollInterval.setStatus("current")
if mibBuilder.loadTexts:
    mscsResourceIsAlivePollInterval.setUnits("Milliseconds")
_MscsResourceLooksAlivePollIntrvl_Type = Gauge32
_MscsResourceLooksAlivePollIntrvl_Object = MibTableColumn
mscsResourceLooksAlivePollIntrvl = _MscsResourceLooksAlivePollIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 13),
    _MscsResourceLooksAlivePollIntrvl_Type()
)
mscsResourceLooksAlivePollIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceLooksAlivePollIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    mscsResourceLooksAlivePollIntrvl.setUnits("Milliseconds")
_MscsResourcePendingTimeout_Type = Gauge32
_MscsResourcePendingTimeout_Object = MibTableColumn
mscsResourcePendingTimeout = _MscsResourcePendingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 14),
    _MscsResourcePendingTimeout_Type()
)
mscsResourcePendingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePendingTimeout.setStatus("current")
_MscsResourcePersistentState_Type = TruthValue
_MscsResourcePersistentState_Object = MibTableColumn
mscsResourcePersistentState = _MscsResourcePersistentState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 15),
    _MscsResourcePersistentState_Type()
)
mscsResourcePersistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePersistentState.setStatus("current")


class _MscsResourceRestartAction_Type(Integer32):
    """Custom type mscsResourceRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dontRestart", 0),
          ("restartActionCount", 3),
          ("restartNoNotify", 1),
          ("restartNotify", 2))
    )


_MscsResourceRestartAction_Type.__name__ = "Integer32"
_MscsResourceRestartAction_Object = MibTableColumn
mscsResourceRestartAction = _MscsResourceRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 16),
    _MscsResourceRestartAction_Type()
)
mscsResourceRestartAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceRestartAction.setStatus("current")
_MscsResourceRestartPeriod_Type = Gauge32
_MscsResourceRestartPeriod_Object = MibTableColumn
mscsResourceRestartPeriod = _MscsResourceRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 17),
    _MscsResourceRestartPeriod_Type()
)
mscsResourceRestartPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceRestartPeriod.setStatus("current")
_MscsResourceRestartThreshold_Type = Gauge32
_MscsResourceRestartThreshold_Object = MibTableColumn
mscsResourceRestartThreshold = _MscsResourceRestartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 18),
    _MscsResourceRestartThreshold_Type()
)
mscsResourceRestartThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceRestartThreshold.setStatus("current")
_MscsResourceRetryPeriodOnFailure_Type = Gauge32
_MscsResourceRetryPeriodOnFailure_Object = MibTableColumn
mscsResourceRetryPeriodOnFailure = _MscsResourceRetryPeriodOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 19),
    _MscsResourceRetryPeriodOnFailure_Type()
)
mscsResourceRetryPeriodOnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceRetryPeriodOnFailure.setStatus("current")
_MscsResourceSeparateMonitor_Type = TruthValue
_MscsResourceSeparateMonitor_Object = MibTableColumn
mscsResourceSeparateMonitor = _MscsResourceSeparateMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 20),
    _MscsResourceSeparateMonitor_Type()
)
mscsResourceSeparateMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceSeparateMonitor.setStatus("current")
_MscsResourceType_Type = WtcsDisplayString
_MscsResourceType_Object = MibTableColumn
mscsResourceType = _MscsResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 11, 1, 21),
    _MscsResourceType_Type()
)
mscsResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourceType.setStatus("current")
_MscsResourcePropertiesTable_Object = MibTable
mscsResourcePropertiesTable = _MscsResourcePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 12)
)
if mibBuilder.loadTexts:
    mscsResourcePropertiesTable.setStatus("current")
_MscsResourcePropertiesEntry_Object = MibTableRow
mscsResourcePropertiesEntry = _MscsResourcePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 12, 1)
)
mscsResourcePropertiesEntry.setIndexNames(
    (0, "INFORMANT-MSCS", "mscsResourceNameIndex"),
    (0, "INFORMANT-MSCS", "mscsResourcePropertiesIndex"),
)
if mibBuilder.loadTexts:
    mscsResourcePropertiesEntry.setStatus("current")


class _MscsResourcePropertiesIndex_Type(Integer32):
    """Custom type mscsResourcePropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MscsResourcePropertiesIndex_Type.__name__ = "Integer32"
_MscsResourcePropertiesIndex_Object = MibTableColumn
mscsResourcePropertiesIndex = _MscsResourcePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 12, 1, 1),
    _MscsResourcePropertiesIndex_Type()
)
mscsResourcePropertiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePropertiesIndex.setStatus("current")
_MscsResourcePropertiesName_Type = WtcsDisplayString
_MscsResourcePropertiesName_Object = MibTableColumn
mscsResourcePropertiesName = _MscsResourcePropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 12, 1, 2),
    _MscsResourcePropertiesName_Type()
)
mscsResourcePropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePropertiesName.setStatus("current")
_MscsResourcePropertiesValue_Type = WtcsDisplayString
_MscsResourcePropertiesValue_Object = MibTableColumn
mscsResourcePropertiesValue = _MscsResourcePropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 31, 12, 1, 3),
    _MscsResourcePropertiesValue_Type()
)
mscsResourcePropertiesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscsResourcePropertiesValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-MSCS",
    **{"mscs": mscs,
       "mscsCluster": mscsCluster,
       "mscsClusterBuildNumber": mscsClusterBuildNumber,
       "mscsClusterHighestVersion": mscsClusterHighestVersion,
       "mscsClusterLowestVersion": mscsClusterLowestVersion,
       "mscsClusterCSDVersion": mscsClusterCSDVersion,
       "mscsClusterFlags": mscsClusterFlags,
       "mscsClusterMajorVersion": mscsClusterMajorVersion,
       "mscsClusterMinorVersion": mscsClusterMinorVersion,
       "mscsClusterMixedVersion": mscsClusterMixedVersion,
       "mscsClusterName": mscsClusterName,
       "mscsClusterQuorumLogSize": mscsClusterQuorumLogSize,
       "mscsClusterQuorumPath": mscsClusterQuorumPath,
       "mscsClusterVendorId": mscsClusterVendorId,
       "mscsClusterDefaultNetworkRole": mscsClusterDefaultNetworkRole,
       "mscsClusterDescription": mscsClusterDescription,
       "mscsClusterPropertiesTable": mscsClusterPropertiesTable,
       "mscsClusterPropertiesEntry": mscsClusterPropertiesEntry,
       "mscsClusterPropertiesIndex": mscsClusterPropertiesIndex,
       "mscsClusterPropertiesName": mscsClusterPropertiesName,
       "mscsClusterPropertiesValue": mscsClusterPropertiesValue,
       "mscsNetInterfaceTable": mscsNetInterfaceTable,
       "mscsNetInterfaceEntry": mscsNetInterfaceEntry,
       "mscsNetInterfaceNameIndex": mscsNetInterfaceNameIndex,
       "mscsNetInterfaceNameFull": mscsNetInterfaceNameFull,
       "mscsNetInterfaceState": mscsNetInterfaceState,
       "mscsNetInterfaceAdapter": mscsNetInterfaceAdapter,
       "mscsNetInterfaceAddress": mscsNetInterfaceAddress,
       "mscsNetInterfaceDescription": mscsNetInterfaceDescription,
       "mscsNetInterfaceNetwork": mscsNetInterfaceNetwork,
       "mscsNetInterfaceNode": mscsNetInterfaceNode,
       "mscsNetInterfacePropertiesTable": mscsNetInterfacePropertiesTable,
       "mscsNetInterfacePropertiesEntry": mscsNetInterfacePropertiesEntry,
       "mscsNetInterfacePropertiesIndex": mscsNetInterfacePropertiesIndex,
       "mscsNetInterfacePropertiesName": mscsNetInterfacePropertiesName,
       "mscsNetInterfacePropertiesValue": mscsNetInterfacePropertiesValue,
       "mscsNetworkTable": mscsNetworkTable,
       "mscsNetworkEntry": mscsNetworkEntry,
       "mscsNetworkNameIndex": mscsNetworkNameIndex,
       "mscsNetworkNameFull": mscsNetworkNameFull,
       "mscsNetworkNetInterfaces": mscsNetworkNetInterfaces,
       "mscsNetworkNetworkID": mscsNetworkNetworkID,
       "mscsNetworkState": mscsNetworkState,
       "mscsNetworkAddress": mscsNetworkAddress,
       "mscsNetworkAddressMask": mscsNetworkAddressMask,
       "mscsNetworkDescription": mscsNetworkDescription,
       "mscsNetworkRole": mscsNetworkRole,
       "mscsNetworkPropertiesTable": mscsNetworkPropertiesTable,
       "mscsNetworkPropertiesEntry": mscsNetworkPropertiesEntry,
       "mscsNetworkPropertiesIndex": mscsNetworkPropertiesIndex,
       "mscsNetworkPropertiesName": mscsNetworkPropertiesName,
       "mscsNetworkPropertiesValue": mscsNetworkPropertiesValue,
       "mscsNodeTable": mscsNodeTable,
       "mscsNodeEntry": mscsNodeEntry,
       "mscsNodeNameIndex": mscsNodeNameIndex,
       "mscsNodeNameFull": mscsNodeNameFull,
       "mscsNodeNetInterfaces": mscsNodeNetInterfaces,
       "mscsNodeNodeID": mscsNodeNodeID,
       "mscsNodeState": mscsNodeState,
       "mscsNodeBuildNumber": mscsNodeBuildNumber,
       "mscsNodeCSDVersion": mscsNodeCSDVersion,
       "mscsNodeDescription": mscsNodeDescription,
       "mscsNodeEnableEventLogReplicate": mscsNodeEnableEventLogReplicate,
       "mscsNodeMajorVersion": mscsNodeMajorVersion,
       "mscsNodeMinorVersion": mscsNodeMinorVersion,
       "mscsNodeHighestVersion": mscsNodeHighestVersion,
       "mscsNodeLowestVersion": mscsNodeLowestVersion,
       "mscsNodePropertiesTable": mscsNodePropertiesTable,
       "mscsNodePropertiesEntry": mscsNodePropertiesEntry,
       "mscsNodePropertiesIndex": mscsNodePropertiesIndex,
       "mscsNodePropertiesName": mscsNodePropertiesName,
       "mscsNodePropertiesValue": mscsNodePropertiesValue,
       "mscsResGroupTable": mscsResGroupTable,
       "mscsResGroupEntry": mscsResGroupEntry,
       "mscsResGroupNameIndex": mscsResGroupNameIndex,
       "mscsResGroupNameFull": mscsResGroupNameFull,
       "mscsResGroupOwnerNode": mscsResGroupOwnerNode,
       "mscsResGroupResources": mscsResGroupResources,
       "mscsResGroupState": mscsResGroupState,
       "mscsResGroupAntiAffinityClassNam": mscsResGroupAntiAffinityClassNam,
       "mscsResGroupAutoFailbackType": mscsResGroupAutoFailbackType,
       "mscsResGroupDescription": mscsResGroupDescription,
       "mscsResGroupFailbackWindowEnd": mscsResGroupFailbackWindowEnd,
       "mscsResGroupFailbackWindowStart": mscsResGroupFailbackWindowStart,
       "mscsResGroupFailoverPeriod": mscsResGroupFailoverPeriod,
       "mscsResGroupFailoverThreshold": mscsResGroupFailoverThreshold,
       "mscsResGroupPersistentState": mscsResGroupPersistentState,
       "mscsResGroupPropertiesTable": mscsResGroupPropertiesTable,
       "mscsResGroupPropertiesEntry": mscsResGroupPropertiesEntry,
       "mscsResGroupPropertiesIndex": mscsResGroupPropertiesIndex,
       "mscsResGroupPropertiesName": mscsResGroupPropertiesName,
       "mscsResGroupPropertiesValue": mscsResGroupPropertiesValue,
       "mscsResourceTable": mscsResourceTable,
       "mscsResourceEntry": mscsResourceEntry,
       "mscsResourceNameIndex": mscsResourceNameIndex,
       "mscsResourceNameFull": mscsResourceNameFull,
       "mscsResourceDependencies": mscsResourceDependencies,
       "mscsResourceDependents": mscsResourceDependents,
       "mscsResourceGroup": mscsResourceGroup,
       "mscsResourceOwnerNode": mscsResourceOwnerNode,
       "mscsResourcePossibleOwnerNodes": mscsResourcePossibleOwnerNodes,
       "mscsResourceState": mscsResourceState,
       "mscsResourceTypeName": mscsResourceTypeName,
       "mscsResourceDebugPrefix": mscsResourceDebugPrefix,
       "mscsResourceDescription": mscsResourceDescription,
       "mscsResourceIsAlivePollInterval": mscsResourceIsAlivePollInterval,
       "mscsResourceLooksAlivePollIntrvl": mscsResourceLooksAlivePollIntrvl,
       "mscsResourcePendingTimeout": mscsResourcePendingTimeout,
       "mscsResourcePersistentState": mscsResourcePersistentState,
       "mscsResourceRestartAction": mscsResourceRestartAction,
       "mscsResourceRestartPeriod": mscsResourceRestartPeriod,
       "mscsResourceRestartThreshold": mscsResourceRestartThreshold,
       "mscsResourceRetryPeriodOnFailure": mscsResourceRetryPeriodOnFailure,
       "mscsResourceSeparateMonitor": mscsResourceSeparateMonitor,
       "mscsResourceType": mscsResourceType,
       "mscsResourcePropertiesTable": mscsResourcePropertiesTable,
       "mscsResourcePropertiesEntry": mscsResourcePropertiesEntry,
       "mscsResourcePropertiesIndex": mscsResourcePropertiesIndex,
       "mscsResourcePropertiesName": mscsResourcePropertiesName,
       "mscsResourcePropertiesValue": mscsResourcePropertiesValue}
)
