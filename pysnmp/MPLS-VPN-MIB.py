# SNMP MIB module (MPLS-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:04 2024
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 experimental,
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
    "experimental",
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

(VPNId,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNId")


# MODULE-IDENTITY

mplsVpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 118)
)
mplsVpnMIB.setRevisions(
        ("2011-03-26 12:00",
         "2001-02-28 12:00",
         "2002-01-26 12:00",
         "2001-11-13 12:00",
         "2001-10-15 12:00",
         "2001-10-05 12:00",
         "2001-07-17 12:00",
         "2001-07-10 12:00",
         "2001-06-19 12:00",
         "2001-05-30 12:00",
         "2000-09-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsVpnName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class MplsVpnRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_MplsVpnNotifications_ObjectIdentity = ObjectIdentity
mplsVpnNotifications = _MplsVpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 0)
)
_MplsVpnObjects_ObjectIdentity = ObjectIdentity
mplsVpnObjects = _MplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1)
)
_MplsVpnScalars_ObjectIdentity = ObjectIdentity
mplsVpnScalars = _MplsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 1)
)
_MplsVpnConfiguredVrfs_Type = Unsigned32
_MplsVpnConfiguredVrfs_Object = MibScalar
mplsVpnConfiguredVrfs = _MplsVpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 1),
    _MplsVpnConfiguredVrfs_Type()
)
mplsVpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnConfiguredVrfs.setStatus("current")
_MplsVpnActiveVrfs_Type = Unsigned32
_MplsVpnActiveVrfs_Object = MibScalar
mplsVpnActiveVrfs = _MplsVpnActiveVrfs_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 2),
    _MplsVpnActiveVrfs_Type()
)
mplsVpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnActiveVrfs.setStatus("current")
_MplsVpnConnectedInterfaces_Type = Unsigned32
_MplsVpnConnectedInterfaces_Object = MibScalar
mplsVpnConnectedInterfaces = _MplsVpnConnectedInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 3),
    _MplsVpnConnectedInterfaces_Type()
)
mplsVpnConnectedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnConnectedInterfaces.setStatus("current")


class _MplsVpnNotificationEnable_Type(TruthValue):
    """Custom type mplsVpnNotificationEnable based on TruthValue"""


_MplsVpnNotificationEnable_Object = MibScalar
mplsVpnNotificationEnable = _MplsVpnNotificationEnable_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 4),
    _MplsVpnNotificationEnable_Type()
)
mplsVpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsVpnNotificationEnable.setStatus("current")
_MplsVpnVrfConfMaxPossibleRoutes_Type = Unsigned32
_MplsVpnVrfConfMaxPossibleRoutes_Object = MibScalar
mplsVpnVrfConfMaxPossibleRoutes = _MplsVpnVrfConfMaxPossibleRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 5),
    _MplsVpnVrfConfMaxPossibleRoutes_Type()
)
mplsVpnVrfConfMaxPossibleRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMaxPossibleRoutes.setStatus("current")


class _MplsVpnVrfConfRouteMaxThreshTime_Type(Unsigned32):
    """Custom type mplsVpnVrfConfRouteMaxThreshTime based on Unsigned32"""
    defaultValue = 600


_MplsVpnVrfConfRouteMaxThreshTime_Object = MibScalar
mplsVpnVrfConfRouteMaxThreshTime = _MplsVpnVrfConfRouteMaxThreshTime_Object(
    (1, 3, 6, 1, 3, 118, 1, 1, 6),
    _MplsVpnVrfConfRouteMaxThreshTime_Type()
)
mplsVpnVrfConfRouteMaxThreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfConfRouteMaxThreshTime.setStatus("current")
if mibBuilder.loadTexts:
    mplsVpnVrfConfRouteMaxThreshTime.setUnits("seconds")
_MplsVpnConf_ObjectIdentity = ObjectIdentity
mplsVpnConf = _MplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 2)
)
_MplsVpnIfConfTable_Object = MibTable
mplsVpnIfConfTable = _MplsVpnIfConfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsVpnIfConfTable.setStatus("current")
_MplsVpnIfConfEntry_Object = MibTableRow
mplsVpnIfConfEntry = _MplsVpnIfConfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1)
)
mplsVpnIfConfEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnIfConfIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnIfConfEntry.setStatus("current")
_MplsVpnIfConfIndex_Type = InterfaceIndex
_MplsVpnIfConfIndex_Object = MibTableColumn
mplsVpnIfConfIndex = _MplsVpnIfConfIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 1),
    _MplsVpnIfConfIndex_Type()
)
mplsVpnIfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnIfConfIndex.setStatus("current")


class _MplsVpnIfLabelEdgeType_Type(Integer32):
    """Custom type mplsVpnIfLabelEdgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customerEdge", 2),
          ("providerEdge", 1))
    )


_MplsVpnIfLabelEdgeType_Type.__name__ = "Integer32"
_MplsVpnIfLabelEdgeType_Object = MibTableColumn
mplsVpnIfLabelEdgeType = _MplsVpnIfLabelEdgeType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 2),
    _MplsVpnIfLabelEdgeType_Type()
)
mplsVpnIfLabelEdgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnIfLabelEdgeType.setStatus("current")


class _MplsVpnIfVpnClassification_Type(Integer32):
    """Custom type mplsVpnIfVpnClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("carrierOfCarrier", 1),
          ("enterprise", 2),
          ("interProvider", 3))
    )


_MplsVpnIfVpnClassification_Type.__name__ = "Integer32"
_MplsVpnIfVpnClassification_Object = MibTableColumn
mplsVpnIfVpnClassification = _MplsVpnIfVpnClassification_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 3),
    _MplsVpnIfVpnClassification_Type()
)
mplsVpnIfVpnClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnIfVpnClassification.setStatus("current")


class _MplsVpnIfVpnRouteDistProtocol_Type(Bits):
    """Custom type mplsVpnIfVpnRouteDistProtocol based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 1),
          ("isis", 4),
          ("none", 0),
          ("ospf", 2),
          ("other", 5),
          ("rip", 3))
    )

_MplsVpnIfVpnRouteDistProtocol_Type.__name__ = "Bits"
_MplsVpnIfVpnRouteDistProtocol_Object = MibTableColumn
mplsVpnIfVpnRouteDistProtocol = _MplsVpnIfVpnRouteDistProtocol_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 4),
    _MplsVpnIfVpnRouteDistProtocol_Type()
)
mplsVpnIfVpnRouteDistProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnIfVpnRouteDistProtocol.setStatus("current")
_MplsVpnIfConfStorageType_Type = StorageType
_MplsVpnIfConfStorageType_Object = MibTableColumn
mplsVpnIfConfStorageType = _MplsVpnIfConfStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 5),
    _MplsVpnIfConfStorageType_Type()
)
mplsVpnIfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnIfConfStorageType.setStatus("current")
_MplsVpnIfConfRowStatus_Type = RowStatus
_MplsVpnIfConfRowStatus_Object = MibTableColumn
mplsVpnIfConfRowStatus = _MplsVpnIfConfRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 1, 1, 6),
    _MplsVpnIfConfRowStatus_Type()
)
mplsVpnIfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnIfConfRowStatus.setStatus("current")
_MplsVpnVrfTable_Object = MibTable
mplsVpnVrfTable = _MplsVpnVrfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsVpnVrfTable.setStatus("current")
_MplsVpnVrfEntry_Object = MibTableRow
mplsVpnVrfEntry = _MplsVpnVrfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1)
)
mplsVpnVrfEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfEntry.setStatus("current")
_MplsVpnVrfName_Type = MplsVpnName
_MplsVpnVrfName_Object = MibTableColumn
mplsVpnVrfName = _MplsVpnVrfName_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 1),
    _MplsVpnVrfName_Type()
)
mplsVpnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfName.setStatus("current")
_MplsVpnVrfVpnId_Type = VPNId
_MplsVpnVrfVpnId_Object = MibTableColumn
mplsVpnVrfVpnId = _MplsVpnVrfVpnId_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 2),
    _MplsVpnVrfVpnId_Type()
)
mplsVpnVrfVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfVpnId.setStatus("current")
_MplsVpnVrfDescription_Type = SnmpAdminString
_MplsVpnVrfDescription_Object = MibTableColumn
mplsVpnVrfDescription = _MplsVpnVrfDescription_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 3),
    _MplsVpnVrfDescription_Type()
)
mplsVpnVrfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfDescription.setStatus("current")
_MplsVpnVrfRouteDistinguisher_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteDistinguisher_Object = MibTableColumn
mplsVpnVrfRouteDistinguisher = _MplsVpnVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 4),
    _MplsVpnVrfRouteDistinguisher_Type()
)
mplsVpnVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDistinguisher.setStatus("current")
_MplsVpnVrfCreationTime_Type = TimeStamp
_MplsVpnVrfCreationTime_Object = MibTableColumn
mplsVpnVrfCreationTime = _MplsVpnVrfCreationTime_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 5),
    _MplsVpnVrfCreationTime_Type()
)
mplsVpnVrfCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfCreationTime.setStatus("current")


class _MplsVpnVrfOperStatus_Type(Integer32):
    """Custom type mplsVpnVrfOperStatus based on Integer32"""
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


_MplsVpnVrfOperStatus_Type.__name__ = "Integer32"
_MplsVpnVrfOperStatus_Object = MibTableColumn
mplsVpnVrfOperStatus = _MplsVpnVrfOperStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 6),
    _MplsVpnVrfOperStatus_Type()
)
mplsVpnVrfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfOperStatus.setStatus("current")
_MplsVpnVrfActiveInterfaces_Type = Unsigned32
_MplsVpnVrfActiveInterfaces_Object = MibTableColumn
mplsVpnVrfActiveInterfaces = _MplsVpnVrfActiveInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 7),
    _MplsVpnVrfActiveInterfaces_Type()
)
mplsVpnVrfActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfActiveInterfaces.setStatus("current")
_MplsVpnVrfAssociatedInterfaces_Type = Unsigned32
_MplsVpnVrfAssociatedInterfaces_Object = MibTableColumn
mplsVpnVrfAssociatedInterfaces = _MplsVpnVrfAssociatedInterfaces_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 8),
    _MplsVpnVrfAssociatedInterfaces_Type()
)
mplsVpnVrfAssociatedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfAssociatedInterfaces.setStatus("current")
_MplsVpnVrfConfMidRouteThreshold_Type = Unsigned32
_MplsVpnVrfConfMidRouteThreshold_Object = MibTableColumn
mplsVpnVrfConfMidRouteThreshold = _MplsVpnVrfConfMidRouteThreshold_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 9),
    _MplsVpnVrfConfMidRouteThreshold_Type()
)
mplsVpnVrfConfMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMidRouteThreshold.setStatus("current")
_MplsVpnVrfConfHighRouteThreshold_Type = Unsigned32
_MplsVpnVrfConfHighRouteThreshold_Object = MibTableColumn
mplsVpnVrfConfHighRouteThreshold = _MplsVpnVrfConfHighRouteThreshold_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 10),
    _MplsVpnVrfConfHighRouteThreshold_Type()
)
mplsVpnVrfConfHighRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfHighRouteThreshold.setStatus("current")
_MplsVpnVrfConfMaxRoutes_Type = Unsigned32
_MplsVpnVrfConfMaxRoutes_Object = MibTableColumn
mplsVpnVrfConfMaxRoutes = _MplsVpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 11),
    _MplsVpnVrfConfMaxRoutes_Type()
)
mplsVpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMaxRoutes.setStatus("current")
_MplsVpnVrfConfLastChanged_Type = TimeStamp
_MplsVpnVrfConfLastChanged_Object = MibTableColumn
mplsVpnVrfConfLastChanged = _MplsVpnVrfConfLastChanged_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 12),
    _MplsVpnVrfConfLastChanged_Type()
)
mplsVpnVrfConfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfConfLastChanged.setStatus("current")
_MplsVpnVrfConfRowStatus_Type = RowStatus
_MplsVpnVrfConfRowStatus_Object = MibTableColumn
mplsVpnVrfConfRowStatus = _MplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 13),
    _MplsVpnVrfConfRowStatus_Type()
)
mplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfRowStatus.setStatus("current")
_MplsVpnVrfConfStorageType_Type = StorageType
_MplsVpnVrfConfStorageType_Object = MibTableColumn
mplsVpnVrfConfStorageType = _MplsVpnVrfConfStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 2, 1, 14),
    _MplsVpnVrfConfStorageType_Type()
)
mplsVpnVrfConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfStorageType.setStatus("current")
_MplsVpnVrfRouteTargetTable_Object = MibTable
mplsVpnVrfRouteTargetTable = _MplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetTable.setStatus("current")
_MplsVpnVrfRouteTargetEntry_Object = MibTableRow
mplsVpnVrfRouteTargetEntry = _MplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1)
)
mplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTargetIndex"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTargetType"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetEntry.setStatus("current")
_MplsVpnVrfRouteTargetIndex_Type = Unsigned32
_MplsVpnVrfRouteTargetIndex_Object = MibTableColumn
mplsVpnVrfRouteTargetIndex = _MplsVpnVrfRouteTargetIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 2),
    _MplsVpnVrfRouteTargetIndex_Type()
)
mplsVpnVrfRouteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetIndex.setStatus("current")


class _MplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type mplsVpnVrfRouteTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("export", 2),
          ("import", 1))
    )


_MplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_MplsVpnVrfRouteTargetType_Object = MibTableColumn
mplsVpnVrfRouteTargetType = _MplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 3),
    _MplsVpnVrfRouteTargetType_Type()
)
mplsVpnVrfRouteTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetType.setStatus("current")
_MplsVpnVrfRouteTarget_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteTarget_Object = MibTableColumn
mplsVpnVrfRouteTarget = _MplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 4),
    _MplsVpnVrfRouteTarget_Type()
)
mplsVpnVrfRouteTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTarget.setStatus("current")
_MplsVpnVrfRouteTargetDescr_Type = DisplayString
_MplsVpnVrfRouteTargetDescr_Object = MibTableColumn
mplsVpnVrfRouteTargetDescr = _MplsVpnVrfRouteTargetDescr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 5),
    _MplsVpnVrfRouteTargetDescr_Type()
)
mplsVpnVrfRouteTargetDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetDescr.setStatus("current")
_MplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_MplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
mplsVpnVrfRouteTargetRowStatus = _MplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 3, 1, 6),
    _MplsVpnVrfRouteTargetRowStatus_Type()
)
mplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetRowStatus.setStatus("current")
_MplsVpnVrfBgpNbrAddrTable_Object = MibTable
mplsVpnVrfBgpNbrAddrTable = _MplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrTable.setStatus("current")
_MplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
mplsVpnVrfBgpNbrAddrEntry = _MplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1)
)
mplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnIfConfIndex"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfBgpNbrIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_MplsVpnVrfBgpNbrIndex_Type = Unsigned32
_MplsVpnVrfBgpNbrIndex_Object = MibTableColumn
mplsVpnVrfBgpNbrIndex = _MplsVpnVrfBgpNbrIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 1),
    _MplsVpnVrfBgpNbrIndex_Type()
)
mplsVpnVrfBgpNbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrIndex.setStatus("current")


class _MplsVpnVrfBgpNbrRole_Type(Integer32):
    """Custom type mplsVpnVrfBgpNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ce", 1),
          ("pe", 2))
    )


_MplsVpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_MplsVpnVrfBgpNbrRole_Object = MibTableColumn
mplsVpnVrfBgpNbrRole = _MplsVpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 2),
    _MplsVpnVrfBgpNbrRole_Type()
)
mplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRole.setStatus("current")
_MplsVpnVrfBgpNbrType_Type = InetAddressType
_MplsVpnVrfBgpNbrType_Object = MibTableColumn
mplsVpnVrfBgpNbrType = _MplsVpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 3),
    _MplsVpnVrfBgpNbrType_Type()
)
mplsVpnVrfBgpNbrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrType.setStatus("current")
_MplsVpnVrfBgpNbrAddr_Type = InetAddress
_MplsVpnVrfBgpNbrAddr_Object = MibTableColumn
mplsVpnVrfBgpNbrAddr = _MplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 4),
    _MplsVpnVrfBgpNbrAddr_Type()
)
mplsVpnVrfBgpNbrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddr.setStatus("current")
_MplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_MplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
mplsVpnVrfBgpNbrRowStatus = _MplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 5),
    _MplsVpnVrfBgpNbrRowStatus_Type()
)
mplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRowStatus.setStatus("current")
_MplsVpnVrfBgpNbrStorageType_Type = StorageType
_MplsVpnVrfBgpNbrStorageType_Object = MibTableColumn
mplsVpnVrfBgpNbrStorageType = _MplsVpnVrfBgpNbrStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 4, 1, 6),
    _MplsVpnVrfBgpNbrStorageType_Type()
)
mplsVpnVrfBgpNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrStorageType.setStatus("current")
_MplsVpnVrfBgpNbrPrefixTable_Object = MibTable
mplsVpnVrfBgpNbrPrefixTable = _MplsVpnVrfBgpNbrPrefixTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrPrefixTable.setStatus("current")
_MplsVpnVrfBgpNbrPrefixEntry_Object = MibTableRow
mplsVpnVrfBgpNbrPrefixEntry = _MplsVpnVrfBgpNbrPrefixEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1)
)
mplsVpnVrfBgpNbrPrefixEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrPrefixEntry.setStatus("current")
_MplsVpnVrfBgpPAtrPeer_Type = InetAddress
_MplsVpnVrfBgpPAtrPeer_Object = MibTableColumn
mplsVpnVrfBgpPAtrPeer = _MplsVpnVrfBgpPAtrPeer_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 1),
    _MplsVpnVrfBgpPAtrPeer_Type()
)
mplsVpnVrfBgpPAtrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrPeer.setStatus("current")
_MplsVpnVrfBgpPAtrIpAddrPrefixLen_Type = Integer32
_MplsVpnVrfBgpPAtrIpAddrPrefixLen_Object = MibTableColumn
mplsVpnVrfBgpPAtrIpAddrPrefixLen = _MplsVpnVrfBgpPAtrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 2),
    _MplsVpnVrfBgpPAtrIpAddrPrefixLen_Type()
)
mplsVpnVrfBgpPAtrIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrIpAddrPrefixLen.setStatus("current")


class _MplsVpnVrfBgpPAtrIpAddrPrefix_Type(InetAddress):
    """Custom type mplsVpnVrfBgpPAtrIpAddrPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_MplsVpnVrfBgpPAtrIpAddrPrefix_Type.__name__ = "InetAddress"
_MplsVpnVrfBgpPAtrIpAddrPrefix_Object = MibTableColumn
mplsVpnVrfBgpPAtrIpAddrPrefix = _MplsVpnVrfBgpPAtrIpAddrPrefix_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 3),
    _MplsVpnVrfBgpPAtrIpAddrPrefix_Type()
)
mplsVpnVrfBgpPAtrIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrIpAddrPrefix.setStatus("current")


class _MplsVpnVrfBgpPAtrOrigin_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_MplsVpnVrfBgpPAtrOrigin_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrOrigin_Object = MibTableColumn
mplsVpnVrfBgpPAtrOrigin = _MplsVpnVrfBgpPAtrOrigin_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 4),
    _MplsVpnVrfBgpPAtrOrigin_Type()
)
mplsVpnVrfBgpPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrOrigin.setStatus("current")


class _MplsVpnVrfBgpPAtrASPathSegment_Type(OctetString):
    """Custom type mplsVpnVrfBgpPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_MplsVpnVrfBgpPAtrASPathSegment_Type.__name__ = "OctetString"
_MplsVpnVrfBgpPAtrASPathSegment_Object = MibTableColumn
mplsVpnVrfBgpPAtrASPathSegment = _MplsVpnVrfBgpPAtrASPathSegment_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 5),
    _MplsVpnVrfBgpPAtrASPathSegment_Type()
)
mplsVpnVrfBgpPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrASPathSegment.setStatus("current")
_MplsVpnVrfBgpPAtrNextHop_Type = InetAddress
_MplsVpnVrfBgpPAtrNextHop_Object = MibTableColumn
mplsVpnVrfBgpPAtrNextHop = _MplsVpnVrfBgpPAtrNextHop_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 6),
    _MplsVpnVrfBgpPAtrNextHop_Type()
)
mplsVpnVrfBgpPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrNextHop.setStatus("current")


class _MplsVpnVrfBgpPAtrMultiExitDisc_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPAtrMultiExitDisc_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrMultiExitDisc_Object = MibTableColumn
mplsVpnVrfBgpPAtrMultiExitDisc = _MplsVpnVrfBgpPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 7),
    _MplsVpnVrfBgpPAtrMultiExitDisc_Type()
)
mplsVpnVrfBgpPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrMultiExitDisc.setStatus("current")


class _MplsVpnVrfBgpPAtrLocalPref_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPAtrLocalPref_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrLocalPref_Object = MibTableColumn
mplsVpnVrfBgpPAtrLocalPref = _MplsVpnVrfBgpPAtrLocalPref_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 8),
    _MplsVpnVrfBgpPAtrLocalPref_Type()
)
mplsVpnVrfBgpPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrLocalPref.setStatus("current")


class _MplsVpnVrfBgpPAtrAtomicAggregate_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteSelected", 2),
          ("lessSpecificRrouteNotSelected", 1))
    )


_MplsVpnVrfBgpPAtrAtomicAggregate_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrAtomicAggregate_Object = MibTableColumn
mplsVpnVrfBgpPAtrAtomicAggregate = _MplsVpnVrfBgpPAtrAtomicAggregate_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 9),
    _MplsVpnVrfBgpPAtrAtomicAggregate_Type()
)
mplsVpnVrfBgpPAtrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrAtomicAggregate.setStatus("current")


class _MplsVpnVrfBgpPAtrAggregatorAS_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsVpnVrfBgpPAtrAggregatorAS_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrAggregatorAS_Object = MibTableColumn
mplsVpnVrfBgpPAtrAggregatorAS = _MplsVpnVrfBgpPAtrAggregatorAS_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 10),
    _MplsVpnVrfBgpPAtrAggregatorAS_Type()
)
mplsVpnVrfBgpPAtrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrAggregatorAS.setStatus("current")
_MplsVpnVrfBgpPAtrAggregatorAddr_Type = InetAddress
_MplsVpnVrfBgpPAtrAggregatorAddr_Object = MibTableColumn
mplsVpnVrfBgpPAtrAggregatorAddr = _MplsVpnVrfBgpPAtrAggregatorAddr_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 11),
    _MplsVpnVrfBgpPAtrAggregatorAddr_Type()
)
mplsVpnVrfBgpPAtrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrAggregatorAddr.setStatus("current")


class _MplsVpnVrfBgpPAtrCalcLocalPref_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MplsVpnVrfBgpPAtrCalcLocalPref_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrCalcLocalPref_Object = MibTableColumn
mplsVpnVrfBgpPAtrCalcLocalPref = _MplsVpnVrfBgpPAtrCalcLocalPref_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 12),
    _MplsVpnVrfBgpPAtrCalcLocalPref_Type()
)
mplsVpnVrfBgpPAtrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrCalcLocalPref.setStatus("current")


class _MplsVpnVrfBgpPAtrBest_Type(Integer32):
    """Custom type mplsVpnVrfBgpPAtrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MplsVpnVrfBgpPAtrBest_Type.__name__ = "Integer32"
_MplsVpnVrfBgpPAtrBest_Object = MibTableColumn
mplsVpnVrfBgpPAtrBest = _MplsVpnVrfBgpPAtrBest_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 13),
    _MplsVpnVrfBgpPAtrBest_Type()
)
mplsVpnVrfBgpPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrBest.setStatus("current")


class _MplsVpnVrfBgpPAtrUnknown_Type(OctetString):
    """Custom type mplsVpnVrfBgpPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MplsVpnVrfBgpPAtrUnknown_Type.__name__ = "OctetString"
_MplsVpnVrfBgpPAtrUnknown_Object = MibTableColumn
mplsVpnVrfBgpPAtrUnknown = _MplsVpnVrfBgpPAtrUnknown_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 5, 1, 14),
    _MplsVpnVrfBgpPAtrUnknown_Type()
)
mplsVpnVrfBgpPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPAtrUnknown.setStatus("current")
_MplsVpnVrfSecTable_Object = MibTable
mplsVpnVrfSecTable = _MplsVpnVrfSecTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsVpnVrfSecTable.setStatus("current")
_MplsVpnVrfSecEntry_Object = MibTableRow
mplsVpnVrfSecEntry = _MplsVpnVrfSecEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfSecEntry.setStatus("current")
_MplsVpnVrfSecIllegalLblVltns_Type = Counter32
_MplsVpnVrfSecIllegalLblVltns_Object = MibTableColumn
mplsVpnVrfSecIllegalLblVltns = _MplsVpnVrfSecIllegalLblVltns_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1, 1),
    _MplsVpnVrfSecIllegalLblVltns_Type()
)
mplsVpnVrfSecIllegalLblVltns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfSecIllegalLblVltns.setStatus("current")
_MplsVpnVrfSecIllegalLblRcvThrsh_Type = Unsigned32
_MplsVpnVrfSecIllegalLblRcvThrsh_Object = MibTableColumn
mplsVpnVrfSecIllegalLblRcvThrsh = _MplsVpnVrfSecIllegalLblRcvThrsh_Object(
    (1, 3, 6, 1, 3, 118, 1, 2, 6, 1, 2),
    _MplsVpnVrfSecIllegalLblRcvThrsh_Type()
)
mplsVpnVrfSecIllegalLblRcvThrsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfSecIllegalLblRcvThrsh.setStatus("current")
_MplsVpnPerf_ObjectIdentity = ObjectIdentity
mplsVpnPerf = _MplsVpnPerf_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 3)
)
_MplsVpnVrfPerfTable_Object = MibTable
mplsVpnVrfPerfTable = _MplsVpnVrfPerfTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfPerfTable.setStatus("current")
_MplsVpnVrfPerfEntry_Object = MibTableRow
mplsVpnVrfPerfEntry = _MplsVpnVrfPerfEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfPerfEntry.setStatus("current")
_MplsVpnVrfPerfRoutesAdded_Type = Counter32
_MplsVpnVrfPerfRoutesAdded_Object = MibTableColumn
mplsVpnVrfPerfRoutesAdded = _MplsVpnVrfPerfRoutesAdded_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 1),
    _MplsVpnVrfPerfRoutesAdded_Type()
)
mplsVpnVrfPerfRoutesAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfRoutesAdded.setStatus("current")
_MplsVpnVrfPerfRoutesDeleted_Type = Counter32
_MplsVpnVrfPerfRoutesDeleted_Object = MibTableColumn
mplsVpnVrfPerfRoutesDeleted = _MplsVpnVrfPerfRoutesDeleted_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 2),
    _MplsVpnVrfPerfRoutesDeleted_Type()
)
mplsVpnVrfPerfRoutesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfRoutesDeleted.setStatus("current")
_MplsVpnVrfPerfCurrNumRoutes_Type = Unsigned32
_MplsVpnVrfPerfCurrNumRoutes_Object = MibTableColumn
mplsVpnVrfPerfCurrNumRoutes = _MplsVpnVrfPerfCurrNumRoutes_Object(
    (1, 3, 6, 1, 3, 118, 1, 3, 1, 1, 3),
    _MplsVpnVrfPerfCurrNumRoutes_Type()
)
mplsVpnVrfPerfCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfPerfCurrNumRoutes.setStatus("current")
_MplsVpnRoute_ObjectIdentity = ObjectIdentity
mplsVpnRoute = _MplsVpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 1, 4)
)
_MplsVpnVrfRouteTable_Object = MibTable
mplsVpnVrfRouteTable = _MplsVpnVrfRouteTable_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTable.setStatus("current")
_MplsVpnVrfRouteEntry_Object = MibTableRow
mplsVpnVrfRouteEntry = _MplsVpnVrfRouteEntry_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1)
)
mplsVpnVrfRouteEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteDest"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteMask"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteTos"),
    (0, "MPLS-VPN-MIB", "mplsVpnVrfRouteNextHop"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteEntry.setStatus("current")
_MplsVpnVrfRouteDest_Type = InetAddress
_MplsVpnVrfRouteDest_Object = MibTableColumn
mplsVpnVrfRouteDest = _MplsVpnVrfRouteDest_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 1),
    _MplsVpnVrfRouteDest_Type()
)
mplsVpnVrfRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDest.setStatus("current")
_MplsVpnVrfRouteDestAddrType_Type = InetAddressType
_MplsVpnVrfRouteDestAddrType_Object = MibTableColumn
mplsVpnVrfRouteDestAddrType = _MplsVpnVrfRouteDestAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 2),
    _MplsVpnVrfRouteDestAddrType_Type()
)
mplsVpnVrfRouteDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDestAddrType.setStatus("current")
_MplsVpnVrfRouteMask_Type = InetAddress
_MplsVpnVrfRouteMask_Object = MibTableColumn
mplsVpnVrfRouteMask = _MplsVpnVrfRouteMask_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 3),
    _MplsVpnVrfRouteMask_Type()
)
mplsVpnVrfRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMask.setStatus("current")
_MplsVpnVrfRouteMaskAddrType_Type = InetAddressType
_MplsVpnVrfRouteMaskAddrType_Object = MibTableColumn
mplsVpnVrfRouteMaskAddrType = _MplsVpnVrfRouteMaskAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 4),
    _MplsVpnVrfRouteMaskAddrType_Type()
)
mplsVpnVrfRouteMaskAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMaskAddrType.setStatus("current")
_MplsVpnVrfRouteTos_Type = Unsigned32
_MplsVpnVrfRouteTos_Object = MibTableColumn
mplsVpnVrfRouteTos = _MplsVpnVrfRouteTos_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 5),
    _MplsVpnVrfRouteTos_Type()
)
mplsVpnVrfRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTos.setStatus("current")
_MplsVpnVrfRouteNextHop_Type = InetAddress
_MplsVpnVrfRouteNextHop_Object = MibTableColumn
mplsVpnVrfRouteNextHop = _MplsVpnVrfRouteNextHop_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 6),
    _MplsVpnVrfRouteNextHop_Type()
)
mplsVpnVrfRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHop.setStatus("current")
_MplsVpnVrfRouteNextHopAddrType_Type = InetAddressType
_MplsVpnVrfRouteNextHopAddrType_Object = MibTableColumn
mplsVpnVrfRouteNextHopAddrType = _MplsVpnVrfRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 7),
    _MplsVpnVrfRouteNextHopAddrType_Type()
)
mplsVpnVrfRouteNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHopAddrType.setStatus("current")
_MplsVpnVrfRouteIfIndex_Type = InterfaceIndexOrZero
_MplsVpnVrfRouteIfIndex_Object = MibTableColumn
mplsVpnVrfRouteIfIndex = _MplsVpnVrfRouteIfIndex_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 8),
    _MplsVpnVrfRouteIfIndex_Type()
)
mplsVpnVrfRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteIfIndex.setStatus("current")


class _MplsVpnVrfRouteType_Type(Integer32):
    """Custom type mplsVpnVrfRouteType based on Integer32"""
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
        *(("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_MplsVpnVrfRouteType_Type.__name__ = "Integer32"
_MplsVpnVrfRouteType_Object = MibTableColumn
mplsVpnVrfRouteType = _MplsVpnVrfRouteType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 9),
    _MplsVpnVrfRouteType_Type()
)
mplsVpnVrfRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteType.setStatus("current")


class _MplsVpnVrfRouteProto_Type(Integer32):
    """Custom type mplsVpnVrfRouteProto based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoEigrp", 16),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esIs", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isIs", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_MplsVpnVrfRouteProto_Type.__name__ = "Integer32"
_MplsVpnVrfRouteProto_Object = MibTableColumn
mplsVpnVrfRouteProto = _MplsVpnVrfRouteProto_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 10),
    _MplsVpnVrfRouteProto_Type()
)
mplsVpnVrfRouteProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteProto.setStatus("current")
_MplsVpnVrfRouteAge_Type = Unsigned32
_MplsVpnVrfRouteAge_Object = MibTableColumn
mplsVpnVrfRouteAge = _MplsVpnVrfRouteAge_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 11),
    _MplsVpnVrfRouteAge_Type()
)
mplsVpnVrfRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteAge.setStatus("current")
_MplsVpnVrfRouteInfo_Type = ObjectIdentifier
_MplsVpnVrfRouteInfo_Object = MibTableColumn
mplsVpnVrfRouteInfo = _MplsVpnVrfRouteInfo_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 12),
    _MplsVpnVrfRouteInfo_Type()
)
mplsVpnVrfRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteInfo.setStatus("current")
_MplsVpnVrfRouteNextHopAS_Type = Unsigned32
_MplsVpnVrfRouteNextHopAS_Object = MibTableColumn
mplsVpnVrfRouteNextHopAS = _MplsVpnVrfRouteNextHopAS_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 13),
    _MplsVpnVrfRouteNextHopAS_Type()
)
mplsVpnVrfRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHopAS.setStatus("current")
_MplsVpnVrfRouteMetric1_Type = Integer32
_MplsVpnVrfRouteMetric1_Object = MibTableColumn
mplsVpnVrfRouteMetric1 = _MplsVpnVrfRouteMetric1_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 14),
    _MplsVpnVrfRouteMetric1_Type()
)
mplsVpnVrfRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric1.setStatus("current")
_MplsVpnVrfRouteMetric2_Type = Integer32
_MplsVpnVrfRouteMetric2_Object = MibTableColumn
mplsVpnVrfRouteMetric2 = _MplsVpnVrfRouteMetric2_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 15),
    _MplsVpnVrfRouteMetric2_Type()
)
mplsVpnVrfRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric2.setStatus("current")
_MplsVpnVrfRouteMetric3_Type = Integer32
_MplsVpnVrfRouteMetric3_Object = MibTableColumn
mplsVpnVrfRouteMetric3 = _MplsVpnVrfRouteMetric3_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 16),
    _MplsVpnVrfRouteMetric3_Type()
)
mplsVpnVrfRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric3.setStatus("current")
_MplsVpnVrfRouteMetric4_Type = Integer32
_MplsVpnVrfRouteMetric4_Object = MibTableColumn
mplsVpnVrfRouteMetric4 = _MplsVpnVrfRouteMetric4_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 17),
    _MplsVpnVrfRouteMetric4_Type()
)
mplsVpnVrfRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric4.setStatus("current")
_MplsVpnVrfRouteMetric5_Type = Integer32
_MplsVpnVrfRouteMetric5_Object = MibTableColumn
mplsVpnVrfRouteMetric5 = _MplsVpnVrfRouteMetric5_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 18),
    _MplsVpnVrfRouteMetric5_Type()
)
mplsVpnVrfRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMetric5.setStatus("current")
_MplsVpnVrfRouteRowStatus_Type = RowStatus
_MplsVpnVrfRouteRowStatus_Object = MibTableColumn
mplsVpnVrfRouteRowStatus = _MplsVpnVrfRouteRowStatus_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 19),
    _MplsVpnVrfRouteRowStatus_Type()
)
mplsVpnVrfRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteRowStatus.setStatus("current")
_MplsVpnVrfRouteStorageType_Type = StorageType
_MplsVpnVrfRouteStorageType_Object = MibTableColumn
mplsVpnVrfRouteStorageType = _MplsVpnVrfRouteStorageType_Object(
    (1, 3, 6, 1, 3, 118, 1, 4, 1, 1, 20),
    _MplsVpnVrfRouteStorageType_Type()
)
mplsVpnVrfRouteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteStorageType.setStatus("current")
_MplsVpnConformance_ObjectIdentity = ObjectIdentity
mplsVpnConformance = _MplsVpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3)
)
_MplsVpnGroups_ObjectIdentity = ObjectIdentity
mplsVpnGroups = _MplsVpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3, 1)
)
_MplsVpnCompliances_ObjectIdentity = ObjectIdentity
mplsVpnCompliances = _MplsVpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 118, 3, 2)
)
mplsVpnVrfEntry.registerAugmentions(
    ("MPLS-VPN-MIB",
     "mplsVpnVrfSecEntry")
)
mplsVpnVrfSecEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())
mplsVpnVrfEntry.registerAugmentions(
    ("MPLS-VPN-MIB",
     "mplsVpnVrfPerfEntry")
)
mplsVpnVrfPerfEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())

# Managed Objects groups

mplsVpnScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 1)
)
mplsVpnScalarGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnConfiguredVrfs"),
        ("MPLS-VPN-MIB", "mplsVpnActiveVrfs"),
        ("MPLS-VPN-MIB", "mplsVpnConnectedInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnNotificationEnable"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMaxPossibleRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfRouteMaxThreshTime"))
)
if mibBuilder.loadTexts:
    mplsVpnScalarGroup.setStatus("current")

mplsVpnVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 2)
)
mplsVpnVrfGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfVpnId"),
        ("MPLS-VPN-MIB", "mplsVpnVrfDescription"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteDistinguisher"),
        ("MPLS-VPN-MIB", "mplsVpnVrfCreationTime"),
        ("MPLS-VPN-MIB", "mplsVpnVrfOperStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfActiveInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnVrfAssociatedInterfaces"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMidRouteThreshold"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMaxRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfLastChanged"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfGroup.setStatus("current")

mplsVpnIfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 3)
)
mplsVpnIfGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnIfLabelEdgeType"),
        ("MPLS-VPN-MIB", "mplsVpnIfVpnClassification"),
        ("MPLS-VPN-MIB", "mplsVpnIfVpnRouteDistProtocol"),
        ("MPLS-VPN-MIB", "mplsVpnIfConfStorageType"),
        ("MPLS-VPN-MIB", "mplsVpnIfConfRowStatus"))
)
if mibBuilder.loadTexts:
    mplsVpnIfGroup.setStatus("current")

mplsVpnPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 4)
)
mplsVpnPerfGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfPerfRoutesAdded"),
        ("MPLS-VPN-MIB", "mplsVpnVrfPerfRoutesDeleted"),
        ("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"))
)
if mibBuilder.loadTexts:
    mplsVpnPerfGroup.setStatus("current")

mplsVpnVrfBgpNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 5)
)
mplsVpnVrfBgpNbrGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrRole"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrAddr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpNbrStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrGroup.setStatus("current")

mplsVpnVrfBgpPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 6)
)
mplsVpnVrfBgpPrefixGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrOrigin"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrASPathSegment"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrNextHop"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrMultiExitDisc"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrLocalPref"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrAtomicAggregate"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrAggregatorAS"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrAggregatorAddr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrCalcLocalPref"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrBest"),
        ("MPLS-VPN-MIB", "mplsVpnVrfBgpPAtrUnknown"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpPrefixGroup.setStatus("current")

mplsVpnSecGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 7)
)
mplsVpnSecGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfSecIllegalLblVltns"),
        ("MPLS-VPN-MIB", "mplsVpnVrfSecIllegalLblRcvThrsh"))
)
if mibBuilder.loadTexts:
    mplsVpnSecGroup.setStatus("current")

mplsVpnVrfRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 8)
)
mplsVpnVrfRouteGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfRouteDestAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMaskAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteNextHop"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteNextHopAddrType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteIfIndex"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteType"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteProto"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteAge"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteInfo"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteNextHopAS"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric1"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric2"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric3"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric4"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteMetric5"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteStorageType"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteGroup.setStatus("current")

mplsVpnVrfRouteTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 9)
)
mplsVpnVrfRouteTargetGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfRouteTargetDescr"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteTarget"),
        ("MPLS-VPN-MIB", "mplsVpnVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetGroup.setStatus("current")


# Notification objects

mplsVrfIfUp = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 1)
)
mplsVrfIfUp.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnIfConfRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfOperStatus"))
)
if mibBuilder.loadTexts:
    mplsVrfIfUp.setStatus(
        "current"
    )

mplsVrfIfDown = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 2)
)
mplsVrfIfDown.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnIfConfRowStatus"),
        ("MPLS-VPN-MIB", "mplsVpnVrfOperStatus"))
)
if mibBuilder.loadTexts:
    mplsVrfIfDown.setStatus(
        "current"
    )

mplsNumVrfRouteMidThreshExceeded = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 3)
)
mplsNumVrfRouteMidThreshExceeded.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfMidRouteThreshold"))
)
if mibBuilder.loadTexts:
    mplsNumVrfRouteMidThreshExceeded.setStatus(
        "current"
    )

mplsNumVrfRouteMaxThreshExceeded = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 4)
)
mplsNumVrfRouteMaxThreshExceeded.setObjects(
      *(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"),
        ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
)
if mibBuilder.loadTexts:
    mplsNumVrfRouteMaxThreshExceeded.setStatus(
        "current"
    )

mplsNumVrfSecIllglLblThrshExcd = NotificationType(
    (1, 3, 6, 1, 3, 118, 0, 5)
)
mplsNumVrfSecIllglLblThrshExcd.setObjects(
    ("MPLS-VPN-MIB", "mplsVpnVrfSecIllegalLblVltns")
)
if mibBuilder.loadTexts:
    mplsNumVrfSecIllglLblThrshExcd.setStatus(
        "current"
    )


# Notifications groups

mplsVpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 118, 3, 1, 10)
)
mplsVpnNotificationGroup.setObjects(
      *(("MPLS-VPN-MIB", "mplsVrfIfUp"),
        ("MPLS-VPN-MIB", "mplsVrfIfDown"),
        ("MPLS-VPN-MIB", "mplsNumVrfRouteMidThreshExceeded"),
        ("MPLS-VPN-MIB", "mplsNumVrfRouteMaxThreshExceeded"),
        ("MPLS-VPN-MIB", "mplsNumVrfSecIllglLblThrshExcd"))
)
if mibBuilder.loadTexts:
    mplsVpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsVpnModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 118, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsVpnModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-VPN-MIB",
    **{"MplsVpnName": MplsVpnName,
       "MplsVpnRouteDistinguisher": MplsVpnRouteDistinguisher,
       "mplsVpnMIB": mplsVpnMIB,
       "mplsVpnNotifications": mplsVpnNotifications,
       "mplsVrfIfUp": mplsVrfIfUp,
       "mplsVrfIfDown": mplsVrfIfDown,
       "mplsNumVrfRouteMidThreshExceeded": mplsNumVrfRouteMidThreshExceeded,
       "mplsNumVrfRouteMaxThreshExceeded": mplsNumVrfRouteMaxThreshExceeded,
       "mplsNumVrfSecIllglLblThrshExcd": mplsNumVrfSecIllglLblThrshExcd,
       "mplsVpnObjects": mplsVpnObjects,
       "mplsVpnScalars": mplsVpnScalars,
       "mplsVpnConfiguredVrfs": mplsVpnConfiguredVrfs,
       "mplsVpnActiveVrfs": mplsVpnActiveVrfs,
       "mplsVpnConnectedInterfaces": mplsVpnConnectedInterfaces,
       "mplsVpnNotificationEnable": mplsVpnNotificationEnable,
       "mplsVpnVrfConfMaxPossibleRoutes": mplsVpnVrfConfMaxPossibleRoutes,
       "mplsVpnVrfConfRouteMaxThreshTime": mplsVpnVrfConfRouteMaxThreshTime,
       "mplsVpnConf": mplsVpnConf,
       "mplsVpnIfConfTable": mplsVpnIfConfTable,
       "mplsVpnIfConfEntry": mplsVpnIfConfEntry,
       "mplsVpnIfConfIndex": mplsVpnIfConfIndex,
       "mplsVpnIfLabelEdgeType": mplsVpnIfLabelEdgeType,
       "mplsVpnIfVpnClassification": mplsVpnIfVpnClassification,
       "mplsVpnIfVpnRouteDistProtocol": mplsVpnIfVpnRouteDistProtocol,
       "mplsVpnIfConfStorageType": mplsVpnIfConfStorageType,
       "mplsVpnIfConfRowStatus": mplsVpnIfConfRowStatus,
       "mplsVpnVrfTable": mplsVpnVrfTable,
       "mplsVpnVrfEntry": mplsVpnVrfEntry,
       "mplsVpnVrfName": mplsVpnVrfName,
       "mplsVpnVrfVpnId": mplsVpnVrfVpnId,
       "mplsVpnVrfDescription": mplsVpnVrfDescription,
       "mplsVpnVrfRouteDistinguisher": mplsVpnVrfRouteDistinguisher,
       "mplsVpnVrfCreationTime": mplsVpnVrfCreationTime,
       "mplsVpnVrfOperStatus": mplsVpnVrfOperStatus,
       "mplsVpnVrfActiveInterfaces": mplsVpnVrfActiveInterfaces,
       "mplsVpnVrfAssociatedInterfaces": mplsVpnVrfAssociatedInterfaces,
       "mplsVpnVrfConfMidRouteThreshold": mplsVpnVrfConfMidRouteThreshold,
       "mplsVpnVrfConfHighRouteThreshold": mplsVpnVrfConfHighRouteThreshold,
       "mplsVpnVrfConfMaxRoutes": mplsVpnVrfConfMaxRoutes,
       "mplsVpnVrfConfLastChanged": mplsVpnVrfConfLastChanged,
       "mplsVpnVrfConfRowStatus": mplsVpnVrfConfRowStatus,
       "mplsVpnVrfConfStorageType": mplsVpnVrfConfStorageType,
       "mplsVpnVrfRouteTargetTable": mplsVpnVrfRouteTargetTable,
       "mplsVpnVrfRouteTargetEntry": mplsVpnVrfRouteTargetEntry,
       "mplsVpnVrfRouteTargetIndex": mplsVpnVrfRouteTargetIndex,
       "mplsVpnVrfRouteTargetType": mplsVpnVrfRouteTargetType,
       "mplsVpnVrfRouteTarget": mplsVpnVrfRouteTarget,
       "mplsVpnVrfRouteTargetDescr": mplsVpnVrfRouteTargetDescr,
       "mplsVpnVrfRouteTargetRowStatus": mplsVpnVrfRouteTargetRowStatus,
       "mplsVpnVrfBgpNbrAddrTable": mplsVpnVrfBgpNbrAddrTable,
       "mplsVpnVrfBgpNbrAddrEntry": mplsVpnVrfBgpNbrAddrEntry,
       "mplsVpnVrfBgpNbrIndex": mplsVpnVrfBgpNbrIndex,
       "mplsVpnVrfBgpNbrRole": mplsVpnVrfBgpNbrRole,
       "mplsVpnVrfBgpNbrType": mplsVpnVrfBgpNbrType,
       "mplsVpnVrfBgpNbrAddr": mplsVpnVrfBgpNbrAddr,
       "mplsVpnVrfBgpNbrRowStatus": mplsVpnVrfBgpNbrRowStatus,
       "mplsVpnVrfBgpNbrStorageType": mplsVpnVrfBgpNbrStorageType,
       "mplsVpnVrfBgpNbrPrefixTable": mplsVpnVrfBgpNbrPrefixTable,
       "mplsVpnVrfBgpNbrPrefixEntry": mplsVpnVrfBgpNbrPrefixEntry,
       "mplsVpnVrfBgpPAtrPeer": mplsVpnVrfBgpPAtrPeer,
       "mplsVpnVrfBgpPAtrIpAddrPrefixLen": mplsVpnVrfBgpPAtrIpAddrPrefixLen,
       "mplsVpnVrfBgpPAtrIpAddrPrefix": mplsVpnVrfBgpPAtrIpAddrPrefix,
       "mplsVpnVrfBgpPAtrOrigin": mplsVpnVrfBgpPAtrOrigin,
       "mplsVpnVrfBgpPAtrASPathSegment": mplsVpnVrfBgpPAtrASPathSegment,
       "mplsVpnVrfBgpPAtrNextHop": mplsVpnVrfBgpPAtrNextHop,
       "mplsVpnVrfBgpPAtrMultiExitDisc": mplsVpnVrfBgpPAtrMultiExitDisc,
       "mplsVpnVrfBgpPAtrLocalPref": mplsVpnVrfBgpPAtrLocalPref,
       "mplsVpnVrfBgpPAtrAtomicAggregate": mplsVpnVrfBgpPAtrAtomicAggregate,
       "mplsVpnVrfBgpPAtrAggregatorAS": mplsVpnVrfBgpPAtrAggregatorAS,
       "mplsVpnVrfBgpPAtrAggregatorAddr": mplsVpnVrfBgpPAtrAggregatorAddr,
       "mplsVpnVrfBgpPAtrCalcLocalPref": mplsVpnVrfBgpPAtrCalcLocalPref,
       "mplsVpnVrfBgpPAtrBest": mplsVpnVrfBgpPAtrBest,
       "mplsVpnVrfBgpPAtrUnknown": mplsVpnVrfBgpPAtrUnknown,
       "mplsVpnVrfSecTable": mplsVpnVrfSecTable,
       "mplsVpnVrfSecEntry": mplsVpnVrfSecEntry,
       "mplsVpnVrfSecIllegalLblVltns": mplsVpnVrfSecIllegalLblVltns,
       "mplsVpnVrfSecIllegalLblRcvThrsh": mplsVpnVrfSecIllegalLblRcvThrsh,
       "mplsVpnPerf": mplsVpnPerf,
       "mplsVpnVrfPerfTable": mplsVpnVrfPerfTable,
       "mplsVpnVrfPerfEntry": mplsVpnVrfPerfEntry,
       "mplsVpnVrfPerfRoutesAdded": mplsVpnVrfPerfRoutesAdded,
       "mplsVpnVrfPerfRoutesDeleted": mplsVpnVrfPerfRoutesDeleted,
       "mplsVpnVrfPerfCurrNumRoutes": mplsVpnVrfPerfCurrNumRoutes,
       "mplsVpnRoute": mplsVpnRoute,
       "mplsVpnVrfRouteTable": mplsVpnVrfRouteTable,
       "mplsVpnVrfRouteEntry": mplsVpnVrfRouteEntry,
       "mplsVpnVrfRouteDest": mplsVpnVrfRouteDest,
       "mplsVpnVrfRouteDestAddrType": mplsVpnVrfRouteDestAddrType,
       "mplsVpnVrfRouteMask": mplsVpnVrfRouteMask,
       "mplsVpnVrfRouteMaskAddrType": mplsVpnVrfRouteMaskAddrType,
       "mplsVpnVrfRouteTos": mplsVpnVrfRouteTos,
       "mplsVpnVrfRouteNextHop": mplsVpnVrfRouteNextHop,
       "mplsVpnVrfRouteNextHopAddrType": mplsVpnVrfRouteNextHopAddrType,
       "mplsVpnVrfRouteIfIndex": mplsVpnVrfRouteIfIndex,
       "mplsVpnVrfRouteType": mplsVpnVrfRouteType,
       "mplsVpnVrfRouteProto": mplsVpnVrfRouteProto,
       "mplsVpnVrfRouteAge": mplsVpnVrfRouteAge,
       "mplsVpnVrfRouteInfo": mplsVpnVrfRouteInfo,
       "mplsVpnVrfRouteNextHopAS": mplsVpnVrfRouteNextHopAS,
       "mplsVpnVrfRouteMetric1": mplsVpnVrfRouteMetric1,
       "mplsVpnVrfRouteMetric2": mplsVpnVrfRouteMetric2,
       "mplsVpnVrfRouteMetric3": mplsVpnVrfRouteMetric3,
       "mplsVpnVrfRouteMetric4": mplsVpnVrfRouteMetric4,
       "mplsVpnVrfRouteMetric5": mplsVpnVrfRouteMetric5,
       "mplsVpnVrfRouteRowStatus": mplsVpnVrfRouteRowStatus,
       "mplsVpnVrfRouteStorageType": mplsVpnVrfRouteStorageType,
       "mplsVpnConformance": mplsVpnConformance,
       "mplsVpnGroups": mplsVpnGroups,
       "mplsVpnScalarGroup": mplsVpnScalarGroup,
       "mplsVpnVrfGroup": mplsVpnVrfGroup,
       "mplsVpnIfGroup": mplsVpnIfGroup,
       "mplsVpnPerfGroup": mplsVpnPerfGroup,
       "mplsVpnVrfBgpNbrGroup": mplsVpnVrfBgpNbrGroup,
       "mplsVpnVrfBgpPrefixGroup": mplsVpnVrfBgpPrefixGroup,
       "mplsVpnSecGroup": mplsVpnSecGroup,
       "mplsVpnVrfRouteGroup": mplsVpnVrfRouteGroup,
       "mplsVpnVrfRouteTargetGroup": mplsVpnVrfRouteTargetGroup,
       "mplsVpnNotificationGroup": mplsVpnNotificationGroup,
       "mplsVpnCompliances": mplsVpnCompliances,
       "mplsVpnModuleCompliance": mplsVpnModuleCompliance}
)
