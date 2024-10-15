# SNMP MIB module (HPN-ICF-MPLS-BGP-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLS-BGP-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:09 2024
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

(hpnicfMpls,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfMpls")

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

hpnicfMplsVpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3)
)
hpnicfMplsVpn.setRevisions(
        ("2001-07-20 12:00",
         "2001-07-17 12:00",
         "2001-07-10 12:00",
         "2001-06-19 12:00",
         "2001-05-30 12:00",
         "2000-09-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMplsVpnId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class HpnicfMplsVpnRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfmplsVpnObjects_ObjectIdentity = ObjectIdentity
hpnicfmplsVpnObjects = _HpnicfmplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1)
)
_HpnicfmplsVpnScalars_ObjectIdentity = ObjectIdentity
hpnicfmplsVpnScalars = _HpnicfmplsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 1)
)
_HpnicfmplsVpnConfiguredVrfs_Type = Unsigned32
_HpnicfmplsVpnConfiguredVrfs_Object = MibScalar
hpnicfmplsVpnConfiguredVrfs = _HpnicfmplsVpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 1, 1),
    _HpnicfmplsVpnConfiguredVrfs_Type()
)
hpnicfmplsVpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnConfiguredVrfs.setStatus("current")
_HpnicfmplsVpnActiveVrfs_Type = Unsigned32
_HpnicfmplsVpnActiveVrfs_Object = MibScalar
hpnicfmplsVpnActiveVrfs = _HpnicfmplsVpnActiveVrfs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 1, 2),
    _HpnicfmplsVpnActiveVrfs_Type()
)
hpnicfmplsVpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnActiveVrfs.setStatus("current")
_HpnicfmplsVpnConf_ObjectIdentity = ObjectIdentity
hpnicfmplsVpnConf = _HpnicfmplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2)
)
_HpnicfmplsVpnInterfaceConfTable_Object = MibTable
hpnicfmplsVpnInterfaceConfTable = _HpnicfmplsVpnInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceConfTable.setStatus("current")
_HpnicfmplsVpnInterfaceConfEntry_Object = MibTableRow
hpnicfmplsVpnInterfaceConfEntry = _HpnicfmplsVpnInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1)
)
hpnicfmplsVpnInterfaceConfEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfName"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceConfEntry.setStatus("current")
_HpnicfmplsVpnInterfaceConfIndex_Type = InterfaceIndex
_HpnicfmplsVpnInterfaceConfIndex_Object = MibTableColumn
hpnicfmplsVpnInterfaceConfIndex = _HpnicfmplsVpnInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 1),
    _HpnicfmplsVpnInterfaceConfIndex_Type()
)
hpnicfmplsVpnInterfaceConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceConfIndex.setStatus("current")


class _HpnicfmplsVpnInterfaceLabelEdgeType_Type(Integer32):
    """Custom type hpnicfmplsVpnInterfaceLabelEdgeType based on Integer32"""
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


_HpnicfmplsVpnInterfaceLabelEdgeType_Type.__name__ = "Integer32"
_HpnicfmplsVpnInterfaceLabelEdgeType_Object = MibTableColumn
hpnicfmplsVpnInterfaceLabelEdgeType = _HpnicfmplsVpnInterfaceLabelEdgeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 2),
    _HpnicfmplsVpnInterfaceLabelEdgeType_Type()
)
hpnicfmplsVpnInterfaceLabelEdgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceLabelEdgeType.setStatus("current")


class _HpnicfmplsVpnInterfaceVpnClassification_Type(Integer32):
    """Custom type hpnicfmplsVpnInterfaceVpnClassification based on Integer32"""
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


_HpnicfmplsVpnInterfaceVpnClassification_Type.__name__ = "Integer32"
_HpnicfmplsVpnInterfaceVpnClassification_Object = MibTableColumn
hpnicfmplsVpnInterfaceVpnClassification = _HpnicfmplsVpnInterfaceVpnClassification_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 3),
    _HpnicfmplsVpnInterfaceVpnClassification_Type()
)
hpnicfmplsVpnInterfaceVpnClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceVpnClassification.setStatus("current")
_HpnicfmplsVpnInterfaceIpAddress_Type = InetAddress
_HpnicfmplsVpnInterfaceIpAddress_Object = MibTableColumn
hpnicfmplsVpnInterfaceIpAddress = _HpnicfmplsVpnInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 4),
    _HpnicfmplsVpnInterfaceIpAddress_Type()
)
hpnicfmplsVpnInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceIpAddress.setStatus("current")
_HpnicfmplsVpnInterfaceIpAddressMask_Type = InetAddress
_HpnicfmplsVpnInterfaceIpAddressMask_Object = MibTableColumn
hpnicfmplsVpnInterfaceIpAddressMask = _HpnicfmplsVpnInterfaceIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 5),
    _HpnicfmplsVpnInterfaceIpAddressMask_Type()
)
hpnicfmplsVpnInterfaceIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceIpAddressMask.setStatus("current")
_HpnicfmplsVpnInterfaceConfRowStatus_Type = RowStatus
_HpnicfmplsVpnInterfaceConfRowStatus_Object = MibTableColumn
hpnicfmplsVpnInterfaceConfRowStatus = _HpnicfmplsVpnInterfaceConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 1, 1, 6),
    _HpnicfmplsVpnInterfaceConfRowStatus_Type()
)
hpnicfmplsVpnInterfaceConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnInterfaceConfRowStatus.setStatus("current")
_HpnicfmplsVpnVrfConfTable_Object = MibTable
hpnicfmplsVpnVrfConfTable = _HpnicfmplsVpnVrfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfTable.setStatus("current")
_HpnicfmplsVpnVrfConfEntry_Object = MibTableRow
hpnicfmplsVpnVrfConfEntry = _HpnicfmplsVpnVrfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1)
)
hpnicfmplsVpnVrfConfEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfEntry.setStatus("current")
_HpnicfmplsVpnVrfName_Type = HpnicfMplsVpnId
_HpnicfmplsVpnVrfName_Object = MibTableColumn
hpnicfmplsVpnVrfName = _HpnicfmplsVpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 1),
    _HpnicfmplsVpnVrfName_Type()
)
hpnicfmplsVpnVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfName.setStatus("current")
_HpnicfmplsVpnVrfRouteDistinguisher_Type = HpnicfMplsVpnRouteDistinguisher
_HpnicfmplsVpnVrfRouteDistinguisher_Object = MibTableColumn
hpnicfmplsVpnVrfRouteDistinguisher = _HpnicfmplsVpnVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 2),
    _HpnicfmplsVpnVrfRouteDistinguisher_Type()
)
hpnicfmplsVpnVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteDistinguisher.setStatus("current")


class _HpnicfmplsVpnVrfNetPrefixType_Type(Integer32):
    """Custom type hpnicfmplsVpnVrfNetPrefixType based on Integer32"""
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


_HpnicfmplsVpnVrfNetPrefixType_Type.__name__ = "Integer32"
_HpnicfmplsVpnVrfNetPrefixType_Object = MibTableColumn
hpnicfmplsVpnVrfNetPrefixType = _HpnicfmplsVpnVrfNetPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 3),
    _HpnicfmplsVpnVrfNetPrefixType_Type()
)
hpnicfmplsVpnVrfNetPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfNetPrefixType.setStatus("current")
_HpnicfmplsVpnVrfNetPrefix_Type = InetAddress
_HpnicfmplsVpnVrfNetPrefix_Object = MibTableColumn
hpnicfmplsVpnVrfNetPrefix = _HpnicfmplsVpnVrfNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 4),
    _HpnicfmplsVpnVrfNetPrefix_Type()
)
hpnicfmplsVpnVrfNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfNetPrefix.setStatus("current")
_HpnicfmplsVpnVrfIpRouteRedistributeConn_Type = TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeConn_Object = MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeConn = _HpnicfmplsVpnVrfIpRouteRedistributeConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 5),
    _HpnicfmplsVpnVrfIpRouteRedistributeConn_Type()
)
hpnicfmplsVpnVrfIpRouteRedistributeConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfIpRouteRedistributeConn.setStatus("current")
_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Type = TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Object = MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeStatic = _HpnicfmplsVpnVrfIpRouteRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 6),
    _HpnicfmplsVpnVrfIpRouteRedistributeStatic_Type()
)
hpnicfmplsVpnVrfIpRouteRedistributeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfIpRouteRedistributeStatic.setStatus("current")
_HpnicfmplsVpnVrfIpRouteRedistributeRip_Type = TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeRip_Object = MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeRip = _HpnicfmplsVpnVrfIpRouteRedistributeRip_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 7),
    _HpnicfmplsVpnVrfIpRouteRedistributeRip_Type()
)
hpnicfmplsVpnVrfIpRouteRedistributeRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfIpRouteRedistributeRip.setStatus("current")
_HpnicfmplsVpnVrfConfHighRouteThreshold_Type = Unsigned32
_HpnicfmplsVpnVrfConfHighRouteThreshold_Object = MibTableColumn
hpnicfmplsVpnVrfConfHighRouteThreshold = _HpnicfmplsVpnVrfConfHighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 8),
    _HpnicfmplsVpnVrfConfHighRouteThreshold_Type()
)
hpnicfmplsVpnVrfConfHighRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfHighRouteThreshold.setStatus("current")
_HpnicfmplsVpnVrfConfIsWarnOnly_Type = TruthValue
_HpnicfmplsVpnVrfConfIsWarnOnly_Object = MibTableColumn
hpnicfmplsVpnVrfConfIsWarnOnly = _HpnicfmplsVpnVrfConfIsWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 9),
    _HpnicfmplsVpnVrfConfIsWarnOnly_Type()
)
hpnicfmplsVpnVrfConfIsWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfIsWarnOnly.setStatus("current")
_HpnicfmplsVpnVrfConfMaxRoutes_Type = Unsigned32
_HpnicfmplsVpnVrfConfMaxRoutes_Object = MibTableColumn
hpnicfmplsVpnVrfConfMaxRoutes = _HpnicfmplsVpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 10),
    _HpnicfmplsVpnVrfConfMaxRoutes_Type()
)
hpnicfmplsVpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfMaxRoutes.setStatus("current")
_HpnicfmplsVpnVrfConfRowStatus_Type = RowStatus
_HpnicfmplsVpnVrfConfRowStatus_Object = MibTableColumn
hpnicfmplsVpnVrfConfRowStatus = _HpnicfmplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 2, 1, 11),
    _HpnicfmplsVpnVrfConfRowStatus_Type()
)
hpnicfmplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfConfRowStatus.setStatus("current")
_HpnicfmplsVpnVrfRouteTargetTable_Object = MibTable
hpnicfmplsVpnVrfRouteTargetTable = _HpnicfmplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTargetTable.setStatus("current")
_HpnicfmplsVpnVrfRouteTargetEntry_Object = MibTableRow
hpnicfmplsVpnVrfRouteTargetEntry = _HpnicfmplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 3, 1)
)
hpnicfmplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfName"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfRouteTarget"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfRouteTargetType"),
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTargetEntry.setStatus("current")
_HpnicfmplsVpnVrfRouteTarget_Type = HpnicfMplsVpnRouteDistinguisher
_HpnicfmplsVpnVrfRouteTarget_Object = MibTableColumn
hpnicfmplsVpnVrfRouteTarget = _HpnicfmplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 3, 1, 1),
    _HpnicfmplsVpnVrfRouteTarget_Type()
)
hpnicfmplsVpnVrfRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTarget.setStatus("current")


class _HpnicfmplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type hpnicfmplsVpnVrfRouteTargetType based on Integer32"""
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


_HpnicfmplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_HpnicfmplsVpnVrfRouteTargetType_Object = MibTableColumn
hpnicfmplsVpnVrfRouteTargetType = _HpnicfmplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 3, 1, 2),
    _HpnicfmplsVpnVrfRouteTargetType_Type()
)
hpnicfmplsVpnVrfRouteTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTargetType.setStatus("current")
_HpnicfmplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_HpnicfmplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
hpnicfmplsVpnVrfRouteTargetRowStatus = _HpnicfmplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 3, 1, 3),
    _HpnicfmplsVpnVrfRouteTargetRowStatus_Type()
)
hpnicfmplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTargetRowStatus.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrAddrTable_Object = MibTable
hpnicfmplsVpnVrfBgpNbrAddrTable = _HpnicfmplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrAddrTable.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
hpnicfmplsVpnVrfBgpNbrAddrEntry = _HpnicfmplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1)
)
hpnicfmplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfName"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrAddr_Type = InetAddress
_HpnicfmplsVpnVrfBgpNbrAddr_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrAddr = _HpnicfmplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 1),
    _HpnicfmplsVpnVrfBgpNbrAddr_Type()
)
hpnicfmplsVpnVrfBgpNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrAddr.setStatus("current")


class _HpnicfmplsVpnVrfBgpNbrRole_Type(Integer32):
    """Custom type hpnicfmplsVpnVrfBgpNbrRole based on Integer32"""
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


_HpnicfmplsVpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_HpnicfmplsVpnVrfBgpNbrRole_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrRole = _HpnicfmplsVpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 2),
    _HpnicfmplsVpnVrfBgpNbrRole_Type()
)
hpnicfmplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrRole.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrType_Type = InetAddressType
_HpnicfmplsVpnVrfBgpNbrType_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrType = _HpnicfmplsVpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 3),
    _HpnicfmplsVpnVrfBgpNbrType_Type()
)
hpnicfmplsVpnVrfBgpNbrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrType.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrAsNumber_Type = Unsigned32
_HpnicfmplsVpnVrfBgpNbrAsNumber_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrAsNumber = _HpnicfmplsVpnVrfBgpNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 4),
    _HpnicfmplsVpnVrfBgpNbrAsNumber_Type()
)
hpnicfmplsVpnVrfBgpNbrAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrAsNumber.setStatus("current")


class _HpnicfmplsVpnVrfBgpNbrAdminStatus_Type(Integer32):
    """Custom type hpnicfmplsVpnVrfBgpNbrAdminStatus based on Integer32"""
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


_HpnicfmplsVpnVrfBgpNbrAdminStatus_Type.__name__ = "Integer32"
_HpnicfmplsVpnVrfBgpNbrAdminStatus_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrAdminStatus = _HpnicfmplsVpnVrfBgpNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 5),
    _HpnicfmplsVpnVrfBgpNbrAdminStatus_Type()
)
hpnicfmplsVpnVrfBgpNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrAdminStatus.setStatus("current")
_HpnicfmplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_HpnicfmplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
hpnicfmplsVpnVrfBgpNbrRowStatus = _HpnicfmplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 2, 4, 1, 6),
    _HpnicfmplsVpnVrfBgpNbrRowStatus_Type()
)
hpnicfmplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfBgpNbrRowStatus.setStatus("current")
_HpnicfmplsVpnRoute_ObjectIdentity = ObjectIdentity
hpnicfmplsVpnRoute = _HpnicfmplsVpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3)
)
_HpnicfmplsVpnVrfRouteTable_Object = MibTable
hpnicfmplsVpnVrfRouteTable = _HpnicfmplsVpnVrfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteTable.setStatus("current")
_HpnicfmplsVpnVrfRouteEntry_Object = MibTableRow
hpnicfmplsVpnVrfRouteEntry = _HpnicfmplsVpnVrfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1)
)
hpnicfmplsVpnVrfRouteEntry.setIndexNames(
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfName"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfRouteDest"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfRouteMask"),
    (0, "HPN-ICF-MPLS-BGP-VPN-MIB", "hpnicfmplsVpnVrfRouteNextHop"),
)
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteEntry.setStatus("current")
_HpnicfmplsVpnVrfRouteDest_Type = InetAddress
_HpnicfmplsVpnVrfRouteDest_Object = MibTableColumn
hpnicfmplsVpnVrfRouteDest = _HpnicfmplsVpnVrfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 1),
    _HpnicfmplsVpnVrfRouteDest_Type()
)
hpnicfmplsVpnVrfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteDest.setStatus("current")
_HpnicfmplsVpnVrfRouteMask_Type = InetAddress
_HpnicfmplsVpnVrfRouteMask_Object = MibTableColumn
hpnicfmplsVpnVrfRouteMask = _HpnicfmplsVpnVrfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 2),
    _HpnicfmplsVpnVrfRouteMask_Type()
)
hpnicfmplsVpnVrfRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteMask.setStatus("current")
_HpnicfmplsVpnVrfRouteNextHop_Type = InetAddress
_HpnicfmplsVpnVrfRouteNextHop_Object = MibTableColumn
hpnicfmplsVpnVrfRouteNextHop = _HpnicfmplsVpnVrfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 3),
    _HpnicfmplsVpnVrfRouteNextHop_Type()
)
hpnicfmplsVpnVrfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteNextHop.setStatus("current")
_HpnicfmplsVpnVrfRouteIfIndex_Type = InterfaceIndex
_HpnicfmplsVpnVrfRouteIfIndex_Object = MibTableColumn
hpnicfmplsVpnVrfRouteIfIndex = _HpnicfmplsVpnVrfRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 4),
    _HpnicfmplsVpnVrfRouteIfIndex_Type()
)
hpnicfmplsVpnVrfRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteIfIndex.setStatus("current")


class _HpnicfmplsVpnVrfRouteProto_Type(Integer32):
    """Custom type hpnicfmplsVpnVrfRouteProto based on Integer32"""
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


_HpnicfmplsVpnVrfRouteProto_Type.__name__ = "Integer32"
_HpnicfmplsVpnVrfRouteProto_Object = MibTableColumn
hpnicfmplsVpnVrfRouteProto = _HpnicfmplsVpnVrfRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 5),
    _HpnicfmplsVpnVrfRouteProto_Type()
)
hpnicfmplsVpnVrfRouteProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteProto.setStatus("current")
_HpnicfmplsVpnVrfRouteRowStatus_Type = RowStatus
_HpnicfmplsVpnVrfRouteRowStatus_Object = MibTableColumn
hpnicfmplsVpnVrfRouteRowStatus = _HpnicfmplsVpnVrfRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3, 1, 3, 1, 1, 6),
    _HpnicfmplsVpnVrfRouteRowStatus_Type()
)
hpnicfmplsVpnVrfRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfmplsVpnVrfRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLS-BGP-VPN-MIB",
    **{"HpnicfMplsVpnId": HpnicfMplsVpnId,
       "HpnicfMplsVpnRouteDistinguisher": HpnicfMplsVpnRouteDistinguisher,
       "hpnicfMplsVpn": hpnicfMplsVpn,
       "hpnicfmplsVpnObjects": hpnicfmplsVpnObjects,
       "hpnicfmplsVpnScalars": hpnicfmplsVpnScalars,
       "hpnicfmplsVpnConfiguredVrfs": hpnicfmplsVpnConfiguredVrfs,
       "hpnicfmplsVpnActiveVrfs": hpnicfmplsVpnActiveVrfs,
       "hpnicfmplsVpnConf": hpnicfmplsVpnConf,
       "hpnicfmplsVpnInterfaceConfTable": hpnicfmplsVpnInterfaceConfTable,
       "hpnicfmplsVpnInterfaceConfEntry": hpnicfmplsVpnInterfaceConfEntry,
       "hpnicfmplsVpnInterfaceConfIndex": hpnicfmplsVpnInterfaceConfIndex,
       "hpnicfmplsVpnInterfaceLabelEdgeType": hpnicfmplsVpnInterfaceLabelEdgeType,
       "hpnicfmplsVpnInterfaceVpnClassification": hpnicfmplsVpnInterfaceVpnClassification,
       "hpnicfmplsVpnInterfaceIpAddress": hpnicfmplsVpnInterfaceIpAddress,
       "hpnicfmplsVpnInterfaceIpAddressMask": hpnicfmplsVpnInterfaceIpAddressMask,
       "hpnicfmplsVpnInterfaceConfRowStatus": hpnicfmplsVpnInterfaceConfRowStatus,
       "hpnicfmplsVpnVrfConfTable": hpnicfmplsVpnVrfConfTable,
       "hpnicfmplsVpnVrfConfEntry": hpnicfmplsVpnVrfConfEntry,
       "hpnicfmplsVpnVrfName": hpnicfmplsVpnVrfName,
       "hpnicfmplsVpnVrfRouteDistinguisher": hpnicfmplsVpnVrfRouteDistinguisher,
       "hpnicfmplsVpnVrfNetPrefixType": hpnicfmplsVpnVrfNetPrefixType,
       "hpnicfmplsVpnVrfNetPrefix": hpnicfmplsVpnVrfNetPrefix,
       "hpnicfmplsVpnVrfIpRouteRedistributeConn": hpnicfmplsVpnVrfIpRouteRedistributeConn,
       "hpnicfmplsVpnVrfIpRouteRedistributeStatic": hpnicfmplsVpnVrfIpRouteRedistributeStatic,
       "hpnicfmplsVpnVrfIpRouteRedistributeRip": hpnicfmplsVpnVrfIpRouteRedistributeRip,
       "hpnicfmplsVpnVrfConfHighRouteThreshold": hpnicfmplsVpnVrfConfHighRouteThreshold,
       "hpnicfmplsVpnVrfConfIsWarnOnly": hpnicfmplsVpnVrfConfIsWarnOnly,
       "hpnicfmplsVpnVrfConfMaxRoutes": hpnicfmplsVpnVrfConfMaxRoutes,
       "hpnicfmplsVpnVrfConfRowStatus": hpnicfmplsVpnVrfConfRowStatus,
       "hpnicfmplsVpnVrfRouteTargetTable": hpnicfmplsVpnVrfRouteTargetTable,
       "hpnicfmplsVpnVrfRouteTargetEntry": hpnicfmplsVpnVrfRouteTargetEntry,
       "hpnicfmplsVpnVrfRouteTarget": hpnicfmplsVpnVrfRouteTarget,
       "hpnicfmplsVpnVrfRouteTargetType": hpnicfmplsVpnVrfRouteTargetType,
       "hpnicfmplsVpnVrfRouteTargetRowStatus": hpnicfmplsVpnVrfRouteTargetRowStatus,
       "hpnicfmplsVpnVrfBgpNbrAddrTable": hpnicfmplsVpnVrfBgpNbrAddrTable,
       "hpnicfmplsVpnVrfBgpNbrAddrEntry": hpnicfmplsVpnVrfBgpNbrAddrEntry,
       "hpnicfmplsVpnVrfBgpNbrAddr": hpnicfmplsVpnVrfBgpNbrAddr,
       "hpnicfmplsVpnVrfBgpNbrRole": hpnicfmplsVpnVrfBgpNbrRole,
       "hpnicfmplsVpnVrfBgpNbrType": hpnicfmplsVpnVrfBgpNbrType,
       "hpnicfmplsVpnVrfBgpNbrAsNumber": hpnicfmplsVpnVrfBgpNbrAsNumber,
       "hpnicfmplsVpnVrfBgpNbrAdminStatus": hpnicfmplsVpnVrfBgpNbrAdminStatus,
       "hpnicfmplsVpnVrfBgpNbrRowStatus": hpnicfmplsVpnVrfBgpNbrRowStatus,
       "hpnicfmplsVpnRoute": hpnicfmplsVpnRoute,
       "hpnicfmplsVpnVrfRouteTable": hpnicfmplsVpnVrfRouteTable,
       "hpnicfmplsVpnVrfRouteEntry": hpnicfmplsVpnVrfRouteEntry,
       "hpnicfmplsVpnVrfRouteDest": hpnicfmplsVpnVrfRouteDest,
       "hpnicfmplsVpnVrfRouteMask": hpnicfmplsVpnVrfRouteMask,
       "hpnicfmplsVpnVrfRouteNextHop": hpnicfmplsVpnVrfRouteNextHop,
       "hpnicfmplsVpnVrfRouteIfIndex": hpnicfmplsVpnVrfRouteIfIndex,
       "hpnicfmplsVpnVrfRouteProto": hpnicfmplsVpnVrfRouteProto,
       "hpnicfmplsVpnVrfRouteRowStatus": hpnicfmplsVpnVrfRouteRowStatus}
)
