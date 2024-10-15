# SNMP MIB module (BROCADE-VCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BROCADE-VCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:35 2024
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

(bcsiModules,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules")

(FcWwn,) = mibBuilder.importSymbols(
    "Brocade-TC",
    "FcWwn")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

brocadeVcsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6)
)
brocadeVcsMIB.setRevisions(
        ("2015-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VcsConfigMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distributed", 2),
          ("local", 1))
    )



class VcsOperationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fabricCluster", 1),
          ("logicalChassis", 2))
    )



class VcsIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )



class VcsRbridgeId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )



class VcsClusterCondition(Integer32, TextualConvention):
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
        *(("degraded", 2),
          ("error", 3),
          ("good", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BrocadeVcsMIBObjects_ObjectIdentity = ObjectIdentity
brocadeVcsMIBObjects = _BrocadeVcsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1)
)
_VcsConfigMode_Type = VcsConfigMode
_VcsConfigMode_Object = MibScalar
vcsConfigMode = _VcsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 1),
    _VcsConfigMode_Type()
)
vcsConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsConfigMode.setStatus("current")
_VcsModeOfOperation_Type = VcsOperationMode
_VcsModeOfOperation_Object = MibScalar
vcsModeOfOperation = _VcsModeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 2),
    _VcsModeOfOperation_Type()
)
vcsModeOfOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsModeOfOperation.setStatus("current")
_VcsIdentifier_Type = VcsIdentifier
_VcsIdentifier_Object = MibScalar
vcsIdentifier = _VcsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 3),
    _VcsIdentifier_Type()
)
vcsIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsIdentifier.setStatus("current")
_VcsVirtualIpV4Address_Type = InetAddress
_VcsVirtualIpV4Address_Object = MibScalar
vcsVirtualIpV4Address = _VcsVirtualIpV4Address_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 4),
    _VcsVirtualIpV4Address_Type()
)
vcsVirtualIpV4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpV4Address.setStatus("current")
_VcsVirtualIpV6Address_Type = InetAddress
_VcsVirtualIpV6Address_Object = MibScalar
vcsVirtualIpV6Address = _VcsVirtualIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 5),
    _VcsVirtualIpV6Address_Type()
)
vcsVirtualIpV6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpV6Address.setStatus("current")
_VcsVirtualIpAssociatedRbridgeId_Type = VcsRbridgeId
_VcsVirtualIpAssociatedRbridgeId_Object = MibScalar
vcsVirtualIpAssociatedRbridgeId = _VcsVirtualIpAssociatedRbridgeId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 6),
    _VcsVirtualIpAssociatedRbridgeId_Type()
)
vcsVirtualIpAssociatedRbridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpAssociatedRbridgeId.setStatus("current")
_VcsVirtualIpInterfaceId_Type = Unsigned32
_VcsVirtualIpInterfaceId_Object = MibScalar
vcsVirtualIpInterfaceId = _VcsVirtualIpInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 7),
    _VcsVirtualIpInterfaceId_Type()
)
vcsVirtualIpInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpInterfaceId.setStatus("current")


class _VcsVirtualIpV4OperStatus_Type(Integer32):
    """Custom type vcsVirtualIpV4OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VcsVirtualIpV4OperStatus_Type.__name__ = "Integer32"
_VcsVirtualIpV4OperStatus_Object = MibScalar
vcsVirtualIpV4OperStatus = _VcsVirtualIpV4OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 8),
    _VcsVirtualIpV4OperStatus_Type()
)
vcsVirtualIpV4OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpV4OperStatus.setStatus("current")


class _VcsVirtualIpV6OperStatus_Type(Integer32):
    """Custom type vcsVirtualIpV6OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VcsVirtualIpV6OperStatus_Type.__name__ = "Integer32"
_VcsVirtualIpV6OperStatus_Object = MibScalar
vcsVirtualIpV6OperStatus = _VcsVirtualIpV6OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 9),
    _VcsVirtualIpV6OperStatus_Type()
)
vcsVirtualIpV6OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsVirtualIpV6OperStatus.setStatus("current")
_VcsNumNodesInCluster_Type = Unsigned32
_VcsNumNodesInCluster_Object = MibScalar
vcsNumNodesInCluster = _VcsNumNodesInCluster_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 10),
    _VcsNumNodesInCluster_Type()
)
vcsNumNodesInCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsNumNodesInCluster.setStatus("current")
_VcsClusterCondition_Type = VcsClusterCondition
_VcsClusterCondition_Object = MibScalar
vcsClusterCondition = _VcsClusterCondition_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 11),
    _VcsClusterCondition_Type()
)
vcsClusterCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsClusterCondition.setStatus("current")
_VcsFabricIslTable_Object = MibTable
vcsFabricIslTable = _VcsFabricIslTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12)
)
if mibBuilder.loadTexts:
    vcsFabricIslTable.setStatus("current")
_VcsFabricIslEntry_Object = MibTableRow
vcsFabricIslEntry = _VcsFabricIslEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1)
)
vcsFabricIslEntry.setIndexNames(
    (0, "BROCADE-VCS-MIB", "vcsFabricIslIndex"),
)
if mibBuilder.loadTexts:
    vcsFabricIslEntry.setStatus("current")
_VcsFabricIslIndex_Type = Unsigned32
_VcsFabricIslIndex_Object = MibTableColumn
vcsFabricIslIndex = _VcsFabricIslIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 1),
    _VcsFabricIslIndex_Type()
)
vcsFabricIslIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcsFabricIslIndex.setStatus("current")
_VcsFabricIslIntfName_Type = DisplayString
_VcsFabricIslIntfName_Object = MibTableColumn
vcsFabricIslIntfName = _VcsFabricIslIntfName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 2),
    _VcsFabricIslIntfName_Type()
)
vcsFabricIslIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslIntfName.setStatus("current")
_VcsFabricIslNbrIntfName_Type = DisplayString
_VcsFabricIslNbrIntfName_Object = MibTableColumn
vcsFabricIslNbrIntfName = _VcsFabricIslNbrIntfName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 3),
    _VcsFabricIslNbrIntfName_Type()
)
vcsFabricIslNbrIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslNbrIntfName.setStatus("current")
_VcsFabricIslNbrWWN_Type = FcWwn
_VcsFabricIslNbrWWN_Object = MibTableColumn
vcsFabricIslNbrWWN = _VcsFabricIslNbrWWN_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 4),
    _VcsFabricIslNbrWWN_Type()
)
vcsFabricIslNbrWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslNbrWWN.setStatus("current")
_VcsFabricIslNbrName_Type = DisplayString
_VcsFabricIslNbrName_Object = MibTableColumn
vcsFabricIslNbrName = _VcsFabricIslNbrName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 5),
    _VcsFabricIslNbrName_Type()
)
vcsFabricIslNbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslNbrName.setStatus("current")
_VcsFabricIslBW_Type = Unsigned32
_VcsFabricIslBW_Object = MibTableColumn
vcsFabricIslBW = _VcsFabricIslBW_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 6),
    _VcsFabricIslBW_Type()
)
vcsFabricIslBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslBW.setStatus("current")
if mibBuilder.loadTexts:
    vcsFabricIslBW.setUnits("megabytes")
_VcsFabricIslIsTrunk_Type = TruthValue
_VcsFabricIslIsTrunk_Object = MibTableColumn
vcsFabricIslIsTrunk = _VcsFabricIslIsTrunk_Object(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 7),
    _VcsFabricIslIsTrunk_Type()
)
vcsFabricIslIsTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcsFabricIslIsTrunk.setStatus("current")
_BrocadeVcsMIBConformance_ObjectIdentity = ObjectIdentity
brocadeVcsMIBConformance = _BrocadeVcsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2)
)
_BrocadeVcsConformanceGroups_ObjectIdentity = ObjectIdentity
brocadeVcsConformanceGroups = _BrocadeVcsConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1)
)
_BrocadeVcsCompliances_ObjectIdentity = ObjectIdentity
brocadeVcsCompliances = _BrocadeVcsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2)
)

# Managed Objects groups

brocadeVcsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1, 1)
)
brocadeVcsObjectsGroup.setObjects(
      *(("BROCADE-VCS-MIB", "vcsConfigMode"),
        ("BROCADE-VCS-MIB", "vcsModeOfOperation"),
        ("BROCADE-VCS-MIB", "vcsIdentifier"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpV4Address"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpV6Address"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpAssociatedRbridgeId"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpInterfaceId"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpV4OperStatus"),
        ("BROCADE-VCS-MIB", "vcsVirtualIpV6OperStatus"),
        ("BROCADE-VCS-MIB", "vcsNumNodesInCluster"),
        ("BROCADE-VCS-MIB", "vcsClusterCondition"),
        ("BROCADE-VCS-MIB", "vcsFabricIslIndex"),
        ("BROCADE-VCS-MIB", "vcsFabricIslIntfName"),
        ("BROCADE-VCS-MIB", "vcsFabricIslNbrIntfName"),
        ("BROCADE-VCS-MIB", "vcsFabricIslNbrWWN"),
        ("BROCADE-VCS-MIB", "vcsFabricIslNbrName"),
        ("BROCADE-VCS-MIB", "vcsFabricIslBW"),
        ("BROCADE-VCS-MIB", "vcsFabricIslIsTrunk"))
)
if mibBuilder.loadTexts:
    brocadeVcsObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

brocadeVcsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    brocadeVcsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-VCS-MIB",
    **{"VcsConfigMode": VcsConfigMode,
       "VcsOperationMode": VcsOperationMode,
       "VcsIdentifier": VcsIdentifier,
       "VcsRbridgeId": VcsRbridgeId,
       "VcsClusterCondition": VcsClusterCondition,
       "brocadeVcsMIB": brocadeVcsMIB,
       "brocadeVcsMIBObjects": brocadeVcsMIBObjects,
       "vcsConfigMode": vcsConfigMode,
       "vcsModeOfOperation": vcsModeOfOperation,
       "vcsIdentifier": vcsIdentifier,
       "vcsVirtualIpV4Address": vcsVirtualIpV4Address,
       "vcsVirtualIpV6Address": vcsVirtualIpV6Address,
       "vcsVirtualIpAssociatedRbridgeId": vcsVirtualIpAssociatedRbridgeId,
       "vcsVirtualIpInterfaceId": vcsVirtualIpInterfaceId,
       "vcsVirtualIpV4OperStatus": vcsVirtualIpV4OperStatus,
       "vcsVirtualIpV6OperStatus": vcsVirtualIpV6OperStatus,
       "vcsNumNodesInCluster": vcsNumNodesInCluster,
       "vcsClusterCondition": vcsClusterCondition,
       "vcsFabricIslTable": vcsFabricIslTable,
       "vcsFabricIslEntry": vcsFabricIslEntry,
       "vcsFabricIslIndex": vcsFabricIslIndex,
       "vcsFabricIslIntfName": vcsFabricIslIntfName,
       "vcsFabricIslNbrIntfName": vcsFabricIslNbrIntfName,
       "vcsFabricIslNbrWWN": vcsFabricIslNbrWWN,
       "vcsFabricIslNbrName": vcsFabricIslNbrName,
       "vcsFabricIslBW": vcsFabricIslBW,
       "vcsFabricIslIsTrunk": vcsFabricIslIsTrunk,
       "brocadeVcsMIBConformance": brocadeVcsMIBConformance,
       "brocadeVcsConformanceGroups": brocadeVcsConformanceGroups,
       "brocadeVcsObjectsGroup": brocadeVcsObjectsGroup,
       "brocadeVcsCompliances": brocadeVcsCompliances,
       "brocadeVcsCompliance": brocadeVcsCompliance}
)
