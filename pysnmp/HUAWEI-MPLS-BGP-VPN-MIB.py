# SNMP MIB module (HUAWEI-MPLS-BGP-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLS-BGP-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:05 2024
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

(huaweiMgmt,
 hwMpls) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huaweiMgmt",
    "hwMpls")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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


# MODULE-IDENTITY

hwMplsVpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3)
)
hwMplsVpn.setRevisions(
        ("2001-07-20 12:00",
         "2001-07-17 12:00",
         "2001-07-10 12:00",
         "2001-06-19 12:00",
         "2001-05-30 12:00",
         "2000-09-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsVpnId(OctetString, TextualConvention):
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

_MplsVpnObjects_ObjectIdentity = ObjectIdentity
mplsVpnObjects = _MplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1)
)
_MplsVpnScalars_ObjectIdentity = ObjectIdentity
mplsVpnScalars = _MplsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 1)
)
_MplsVpnConfiguredVrfs_Type = Unsigned32
_MplsVpnConfiguredVrfs_Object = MibScalar
mplsVpnConfiguredVrfs = _MplsVpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 1, 1),
    _MplsVpnConfiguredVrfs_Type()
)
mplsVpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnConfiguredVrfs.setStatus("current")
_MplsVpnActiveVrfs_Type = Unsigned32
_MplsVpnActiveVrfs_Object = MibScalar
mplsVpnActiveVrfs = _MplsVpnActiveVrfs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 1, 2),
    _MplsVpnActiveVrfs_Type()
)
mplsVpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnActiveVrfs.setStatus("current")
_MplsVpnConf_ObjectIdentity = ObjectIdentity
mplsVpnConf = _MplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2)
)
_MplsVpnInterfaceConfTable_Object = MibTable
mplsVpnInterfaceConfTable = _MplsVpnInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfTable.setStatus("current")
_MplsVpnInterfaceConfEntry_Object = MibTableRow
mplsVpnInterfaceConfEntry = _MplsVpnInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1)
)
mplsVpnInterfaceConfEntry.setIndexNames(
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfEntry.setStatus("current")
_MplsVpnInterfaceConfIndex_Type = InterfaceIndex
_MplsVpnInterfaceConfIndex_Object = MibTableColumn
mplsVpnInterfaceConfIndex = _MplsVpnInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 1),
    _MplsVpnInterfaceConfIndex_Type()
)
mplsVpnInterfaceConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfIndex.setStatus("current")


class _MplsVpnInterfaceLabelEdgeType_Type(Integer32):
    """Custom type mplsVpnInterfaceLabelEdgeType based on Integer32"""
    defaultValue = 1

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


_MplsVpnInterfaceLabelEdgeType_Type.__name__ = "Integer32"
_MplsVpnInterfaceLabelEdgeType_Object = MibTableColumn
mplsVpnInterfaceLabelEdgeType = _MplsVpnInterfaceLabelEdgeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 2),
    _MplsVpnInterfaceLabelEdgeType_Type()
)
mplsVpnInterfaceLabelEdgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnInterfaceLabelEdgeType.setStatus("current")


class _MplsVpnInterfaceVpnClassification_Type(Integer32):
    """Custom type mplsVpnInterfaceVpnClassification based on Integer32"""
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


_MplsVpnInterfaceVpnClassification_Type.__name__ = "Integer32"
_MplsVpnInterfaceVpnClassification_Object = MibTableColumn
mplsVpnInterfaceVpnClassification = _MplsVpnInterfaceVpnClassification_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 3),
    _MplsVpnInterfaceVpnClassification_Type()
)
mplsVpnInterfaceVpnClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnInterfaceVpnClassification.setStatus("current")
_MplsVpnInterfaceIpAddress_Type = InetAddress
_MplsVpnInterfaceIpAddress_Object = MibTableColumn
mplsVpnInterfaceIpAddress = _MplsVpnInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 4),
    _MplsVpnInterfaceIpAddress_Type()
)
mplsVpnInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceIpAddress.setStatus("current")
_MplsVpnInterfaceIpAddressMask_Type = InetAddress
_MplsVpnInterfaceIpAddressMask_Object = MibTableColumn
mplsVpnInterfaceIpAddressMask = _MplsVpnInterfaceIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 5),
    _MplsVpnInterfaceIpAddressMask_Type()
)
mplsVpnInterfaceIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceIpAddressMask.setStatus("current")
_MplsVpnInterfaceConfRowStatus_Type = RowStatus
_MplsVpnInterfaceConfRowStatus_Object = MibTableColumn
mplsVpnInterfaceConfRowStatus = _MplsVpnInterfaceConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 1, 1, 6),
    _MplsVpnInterfaceConfRowStatus_Type()
)
mplsVpnInterfaceConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnInterfaceConfRowStatus.setStatus("current")
_MplsVpnVrfConfTable_Object = MibTable
mplsVpnVrfConfTable = _MplsVpnVrfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsVpnVrfConfTable.setStatus("current")
_MplsVpnVrfConfEntry_Object = MibTableRow
mplsVpnVrfConfEntry = _MplsVpnVrfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1)
)
mplsVpnVrfConfEntry.setIndexNames(
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfConfEntry.setStatus("current")
_MplsVpnVrfName_Type = MplsVpnId
_MplsVpnVrfName_Object = MibTableColumn
mplsVpnVrfName = _MplsVpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 1),
    _MplsVpnVrfName_Type()
)
mplsVpnVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfName.setStatus("current")
_MplsVpnVrfRouteDistinguisher_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteDistinguisher_Object = MibTableColumn
mplsVpnVrfRouteDistinguisher = _MplsVpnVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 2),
    _MplsVpnVrfRouteDistinguisher_Type()
)
mplsVpnVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDistinguisher.setStatus("current")


class _MplsVpnVrfNetPrefixType_Type(Integer32):
    """Custom type mplsVpnVrfNetPrefixType based on Integer32"""
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
        *(("bgp", 5),
          ("isis", 4),
          ("ospf", 3),
          ("other", 1),
          ("rip", 2),
          ("static", 6))
    )


_MplsVpnVrfNetPrefixType_Type.__name__ = "Integer32"
_MplsVpnVrfNetPrefixType_Object = MibTableColumn
mplsVpnVrfNetPrefixType = _MplsVpnVrfNetPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 3),
    _MplsVpnVrfNetPrefixType_Type()
)
mplsVpnVrfNetPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfNetPrefixType.setStatus("current")
_MplsVpnVrfNetPrefix_Type = InetAddress
_MplsVpnVrfNetPrefix_Object = MibTableColumn
mplsVpnVrfNetPrefix = _MplsVpnVrfNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 4),
    _MplsVpnVrfNetPrefix_Type()
)
mplsVpnVrfNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfNetPrefix.setStatus("current")
_MplsVpnVrfIpRouteRedistributeConn_Type = TruthValue
_MplsVpnVrfIpRouteRedistributeConn_Object = MibTableColumn
mplsVpnVrfIpRouteRedistributeConn = _MplsVpnVrfIpRouteRedistributeConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 5),
    _MplsVpnVrfIpRouteRedistributeConn_Type()
)
mplsVpnVrfIpRouteRedistributeConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfIpRouteRedistributeConn.setStatus("current")
_MplsVpnVrfIpRouteRedistributeStatic_Type = TruthValue
_MplsVpnVrfIpRouteRedistributeStatic_Object = MibTableColumn
mplsVpnVrfIpRouteRedistributeStatic = _MplsVpnVrfIpRouteRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 6),
    _MplsVpnVrfIpRouteRedistributeStatic_Type()
)
mplsVpnVrfIpRouteRedistributeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfIpRouteRedistributeStatic.setStatus("current")
_MplsVpnVrfIpRouteRedistributeRip_Type = TruthValue
_MplsVpnVrfIpRouteRedistributeRip_Object = MibTableColumn
mplsVpnVrfIpRouteRedistributeRip = _MplsVpnVrfIpRouteRedistributeRip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 7),
    _MplsVpnVrfIpRouteRedistributeRip_Type()
)
mplsVpnVrfIpRouteRedistributeRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfIpRouteRedistributeRip.setStatus("current")
_MplsVpnVrfConfHighRouteThreshold_Type = Unsigned32
_MplsVpnVrfConfHighRouteThreshold_Object = MibTableColumn
mplsVpnVrfConfHighRouteThreshold = _MplsVpnVrfConfHighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 8),
    _MplsVpnVrfConfHighRouteThreshold_Type()
)
mplsVpnVrfConfHighRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfHighRouteThreshold.setStatus("current")
_MplsVpnVrfConfIsWarnOnly_Type = TruthValue
_MplsVpnVrfConfIsWarnOnly_Object = MibTableColumn
mplsVpnVrfConfIsWarnOnly = _MplsVpnVrfConfIsWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 9),
    _MplsVpnVrfConfIsWarnOnly_Type()
)
mplsVpnVrfConfIsWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfIsWarnOnly.setStatus("current")
_MplsVpnVrfConfMaxRoutes_Type = Unsigned32
_MplsVpnVrfConfMaxRoutes_Object = MibTableColumn
mplsVpnVrfConfMaxRoutes = _MplsVpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 10),
    _MplsVpnVrfConfMaxRoutes_Type()
)
mplsVpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfMaxRoutes.setStatus("current")
_MplsVpnVrfConfRowStatus_Type = RowStatus
_MplsVpnVrfConfRowStatus_Object = MibTableColumn
mplsVpnVrfConfRowStatus = _MplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 2, 1, 11),
    _MplsVpnVrfConfRowStatus_Type()
)
mplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfConfRowStatus.setStatus("current")
_MplsVpnVrfRouteTargetTable_Object = MibTable
mplsVpnVrfRouteTargetTable = _MplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetTable.setStatus("current")
_MplsVpnVrfRouteTargetEntry_Object = MibTableRow
mplsVpnVrfRouteTargetEntry = _MplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 3, 1)
)
mplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTarget"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTargetType"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetEntry.setStatus("current")
_MplsVpnVrfRouteTarget_Type = MplsVpnRouteDistinguisher
_MplsVpnVrfRouteTarget_Object = MibTableColumn
mplsVpnVrfRouteTarget = _MplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 3, 1, 1),
    _MplsVpnVrfRouteTarget_Type()
)
mplsVpnVrfRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTarget.setStatus("current")


class _MplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type mplsVpnVrfRouteTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_MplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_MplsVpnVrfRouteTargetType_Object = MibTableColumn
mplsVpnVrfRouteTargetType = _MplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 3, 1, 2),
    _MplsVpnVrfRouteTargetType_Type()
)
mplsVpnVrfRouteTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetType.setStatus("current")
_MplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_MplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
mplsVpnVrfRouteTargetRowStatus = _MplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 3, 1, 3),
    _MplsVpnVrfRouteTargetRowStatus_Type()
)
mplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTargetRowStatus.setStatus("current")
_MplsVpnVrfBgpNbrAddrTable_Object = MibTable
mplsVpnVrfBgpNbrAddrTable = _MplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrTable.setStatus("current")
_MplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
mplsVpnVrfBgpNbrAddrEntry = _MplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1)
)
mplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_MplsVpnVrfBgpNbrAddr_Type = InetAddress
_MplsVpnVrfBgpNbrAddr_Object = MibTableColumn
mplsVpnVrfBgpNbrAddr = _MplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 1),
    _MplsVpnVrfBgpNbrAddr_Type()
)
mplsVpnVrfBgpNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAddr.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 2),
    _MplsVpnVrfBgpNbrRole_Type()
)
mplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRole.setStatus("current")
_MplsVpnVrfBgpNbrType_Type = InetAddressType
_MplsVpnVrfBgpNbrType_Object = MibTableColumn
mplsVpnVrfBgpNbrType = _MplsVpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 3),
    _MplsVpnVrfBgpNbrType_Type()
)
mplsVpnVrfBgpNbrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrType.setStatus("current")
_MplsVpnVrfBgpNbrAsNumber_Type = Unsigned32
_MplsVpnVrfBgpNbrAsNumber_Object = MibTableColumn
mplsVpnVrfBgpNbrAsNumber = _MplsVpnVrfBgpNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 4),
    _MplsVpnVrfBgpNbrAsNumber_Type()
)
mplsVpnVrfBgpNbrAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAsNumber.setStatus("current")


class _MplsVpnVrfBgpNbrAdminStatus_Type(Integer32):
    """Custom type mplsVpnVrfBgpNbrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mplsVpnVrfBgpNbrSetDown", 2),
          ("mplsVpnVrfBgpNbrSetUp", 1))
    )


_MplsVpnVrfBgpNbrAdminStatus_Type.__name__ = "Integer32"
_MplsVpnVrfBgpNbrAdminStatus_Object = MibTableColumn
mplsVpnVrfBgpNbrAdminStatus = _MplsVpnVrfBgpNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 5),
    _MplsVpnVrfBgpNbrAdminStatus_Type()
)
mplsVpnVrfBgpNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrAdminStatus.setStatus("current")
_MplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_MplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
mplsVpnVrfBgpNbrRowStatus = _MplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 2, 4, 1, 6),
    _MplsVpnVrfBgpNbrRowStatus_Type()
)
mplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfBgpNbrRowStatus.setStatus("current")
_MplsVpnRoute_ObjectIdentity = ObjectIdentity
mplsVpnRoute = _MplsVpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3)
)
_MplsVpnVrfRouteTable_Object = MibTable
mplsVpnVrfRouteTable = _MplsVpnVrfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteTable.setStatus("current")
_MplsVpnVrfRouteEntry_Object = MibTableRow
mplsVpnVrfRouteEntry = _MplsVpnVrfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1)
)
mplsVpnVrfRouteEntry.setIndexNames(
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteDest"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteMask"),
    (0, "HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteNextHop"),
)
if mibBuilder.loadTexts:
    mplsVpnVrfRouteEntry.setStatus("current")
_MplsVpnVrfRouteDest_Type = InetAddress
_MplsVpnVrfRouteDest_Object = MibTableColumn
mplsVpnVrfRouteDest = _MplsVpnVrfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 1),
    _MplsVpnVrfRouteDest_Type()
)
mplsVpnVrfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteDest.setStatus("current")
_MplsVpnVrfRouteMask_Type = InetAddress
_MplsVpnVrfRouteMask_Object = MibTableColumn
mplsVpnVrfRouteMask = _MplsVpnVrfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 2),
    _MplsVpnVrfRouteMask_Type()
)
mplsVpnVrfRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteMask.setStatus("current")
_MplsVpnVrfRouteNextHop_Type = InetAddress
_MplsVpnVrfRouteNextHop_Object = MibTableColumn
mplsVpnVrfRouteNextHop = _MplsVpnVrfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 3),
    _MplsVpnVrfRouteNextHop_Type()
)
mplsVpnVrfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteNextHop.setStatus("current")
_MplsVpnVrfRouteIfIndex_Type = InterfaceIndex
_MplsVpnVrfRouteIfIndex_Object = MibTableColumn
mplsVpnVrfRouteIfIndex = _MplsVpnVrfRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 4),
    _MplsVpnVrfRouteIfIndex_Type()
)
mplsVpnVrfRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteIfIndex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 5),
    _MplsVpnVrfRouteProto_Type()
)
mplsVpnVrfRouteProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteProto.setStatus("current")
_MplsVpnVrfRouteRowStatus_Type = RowStatus
_MplsVpnVrfRouteRowStatus_Object = MibTableColumn
mplsVpnVrfRouteRowStatus = _MplsVpnVrfRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 3, 1, 3, 1, 1, 6),
    _MplsVpnVrfRouteRowStatus_Type()
)
mplsVpnVrfRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsVpnVrfRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLS-BGP-VPN-MIB",
    **{"MplsVpnId": MplsVpnId,
       "MplsVpnRouteDistinguisher": MplsVpnRouteDistinguisher,
       "hwMplsVpn": hwMplsVpn,
       "mplsVpnObjects": mplsVpnObjects,
       "mplsVpnScalars": mplsVpnScalars,
       "mplsVpnConfiguredVrfs": mplsVpnConfiguredVrfs,
       "mplsVpnActiveVrfs": mplsVpnActiveVrfs,
       "mplsVpnConf": mplsVpnConf,
       "mplsVpnInterfaceConfTable": mplsVpnInterfaceConfTable,
       "mplsVpnInterfaceConfEntry": mplsVpnInterfaceConfEntry,
       "mplsVpnInterfaceConfIndex": mplsVpnInterfaceConfIndex,
       "mplsVpnInterfaceLabelEdgeType": mplsVpnInterfaceLabelEdgeType,
       "mplsVpnInterfaceVpnClassification": mplsVpnInterfaceVpnClassification,
       "mplsVpnInterfaceIpAddress": mplsVpnInterfaceIpAddress,
       "mplsVpnInterfaceIpAddressMask": mplsVpnInterfaceIpAddressMask,
       "mplsVpnInterfaceConfRowStatus": mplsVpnInterfaceConfRowStatus,
       "mplsVpnVrfConfTable": mplsVpnVrfConfTable,
       "mplsVpnVrfConfEntry": mplsVpnVrfConfEntry,
       "mplsVpnVrfName": mplsVpnVrfName,
       "mplsVpnVrfRouteDistinguisher": mplsVpnVrfRouteDistinguisher,
       "mplsVpnVrfNetPrefixType": mplsVpnVrfNetPrefixType,
       "mplsVpnVrfNetPrefix": mplsVpnVrfNetPrefix,
       "mplsVpnVrfIpRouteRedistributeConn": mplsVpnVrfIpRouteRedistributeConn,
       "mplsVpnVrfIpRouteRedistributeStatic": mplsVpnVrfIpRouteRedistributeStatic,
       "mplsVpnVrfIpRouteRedistributeRip": mplsVpnVrfIpRouteRedistributeRip,
       "mplsVpnVrfConfHighRouteThreshold": mplsVpnVrfConfHighRouteThreshold,
       "mplsVpnVrfConfIsWarnOnly": mplsVpnVrfConfIsWarnOnly,
       "mplsVpnVrfConfMaxRoutes": mplsVpnVrfConfMaxRoutes,
       "mplsVpnVrfConfRowStatus": mplsVpnVrfConfRowStatus,
       "mplsVpnVrfRouteTargetTable": mplsVpnVrfRouteTargetTable,
       "mplsVpnVrfRouteTargetEntry": mplsVpnVrfRouteTargetEntry,
       "mplsVpnVrfRouteTarget": mplsVpnVrfRouteTarget,
       "mplsVpnVrfRouteTargetType": mplsVpnVrfRouteTargetType,
       "mplsVpnVrfRouteTargetRowStatus": mplsVpnVrfRouteTargetRowStatus,
       "mplsVpnVrfBgpNbrAddrTable": mplsVpnVrfBgpNbrAddrTable,
       "mplsVpnVrfBgpNbrAddrEntry": mplsVpnVrfBgpNbrAddrEntry,
       "mplsVpnVrfBgpNbrAddr": mplsVpnVrfBgpNbrAddr,
       "mplsVpnVrfBgpNbrRole": mplsVpnVrfBgpNbrRole,
       "mplsVpnVrfBgpNbrType": mplsVpnVrfBgpNbrType,
       "mplsVpnVrfBgpNbrAsNumber": mplsVpnVrfBgpNbrAsNumber,
       "mplsVpnVrfBgpNbrAdminStatus": mplsVpnVrfBgpNbrAdminStatus,
       "mplsVpnVrfBgpNbrRowStatus": mplsVpnVrfBgpNbrRowStatus,
       "mplsVpnRoute": mplsVpnRoute,
       "mplsVpnVrfRouteTable": mplsVpnVrfRouteTable,
       "mplsVpnVrfRouteEntry": mplsVpnVrfRouteEntry,
       "mplsVpnVrfRouteDest": mplsVpnVrfRouteDest,
       "mplsVpnVrfRouteMask": mplsVpnVrfRouteMask,
       "mplsVpnVrfRouteNextHop": mplsVpnVrfRouteNextHop,
       "mplsVpnVrfRouteIfIndex": mplsVpnVrfRouteIfIndex,
       "mplsVpnVrfRouteProto": mplsVpnVrfRouteProto,
       "mplsVpnVrfRouteRowStatus": mplsVpnVrfRouteRowStatus}
)
