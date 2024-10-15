# SNMP MIB module (HH3C-MPLS-BGP-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLS-BGP-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:10 2024
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

(hh3cMpls,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cMpls")

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

hh3cMplsVpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3)
)
hh3cMplsVpn.setRevisions(
        ("2001-07-20 12:00",
         "2001-07-17 12:00",
         "2001-07-10 12:00",
         "2001-06-19 12:00",
         "2001-05-30 12:00",
         "2000-09-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMplsVpnId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class Hh3cMplsVpnRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cmplsVpnObjects_ObjectIdentity = ObjectIdentity
hh3cmplsVpnObjects = _Hh3cmplsVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1)
)
_Hh3cmplsVpnScalars_ObjectIdentity = ObjectIdentity
hh3cmplsVpnScalars = _Hh3cmplsVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 1)
)
_Hh3cmplsVpnConfiguredVrfs_Type = Unsigned32
_Hh3cmplsVpnConfiguredVrfs_Object = MibScalar
hh3cmplsVpnConfiguredVrfs = _Hh3cmplsVpnConfiguredVrfs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 1, 1),
    _Hh3cmplsVpnConfiguredVrfs_Type()
)
hh3cmplsVpnConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnConfiguredVrfs.setStatus("current")
_Hh3cmplsVpnActiveVrfs_Type = Unsigned32
_Hh3cmplsVpnActiveVrfs_Object = MibScalar
hh3cmplsVpnActiveVrfs = _Hh3cmplsVpnActiveVrfs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 1, 2),
    _Hh3cmplsVpnActiveVrfs_Type()
)
hh3cmplsVpnActiveVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnActiveVrfs.setStatus("current")
_Hh3cmplsVpnConf_ObjectIdentity = ObjectIdentity
hh3cmplsVpnConf = _Hh3cmplsVpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2)
)
_Hh3cmplsVpnInterfaceConfTable_Object = MibTable
hh3cmplsVpnInterfaceConfTable = _Hh3cmplsVpnInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceConfTable.setStatus("current")
_Hh3cmplsVpnInterfaceConfEntry_Object = MibTableRow
hh3cmplsVpnInterfaceConfEntry = _Hh3cmplsVpnInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1)
)
hh3cmplsVpnInterfaceConfEntry.setIndexNames(
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfName"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnInterfaceConfIndex"),
)
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceConfEntry.setStatus("current")
_Hh3cmplsVpnInterfaceConfIndex_Type = InterfaceIndex
_Hh3cmplsVpnInterfaceConfIndex_Object = MibTableColumn
hh3cmplsVpnInterfaceConfIndex = _Hh3cmplsVpnInterfaceConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 1),
    _Hh3cmplsVpnInterfaceConfIndex_Type()
)
hh3cmplsVpnInterfaceConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceConfIndex.setStatus("current")


class _Hh3cmplsVpnInterfaceLabelEdgeType_Type(Integer32):
    """Custom type hh3cmplsVpnInterfaceLabelEdgeType based on Integer32"""
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


_Hh3cmplsVpnInterfaceLabelEdgeType_Type.__name__ = "Integer32"
_Hh3cmplsVpnInterfaceLabelEdgeType_Object = MibTableColumn
hh3cmplsVpnInterfaceLabelEdgeType = _Hh3cmplsVpnInterfaceLabelEdgeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 2),
    _Hh3cmplsVpnInterfaceLabelEdgeType_Type()
)
hh3cmplsVpnInterfaceLabelEdgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceLabelEdgeType.setStatus("current")


class _Hh3cmplsVpnInterfaceVpnClassification_Type(Integer32):
    """Custom type hh3cmplsVpnInterfaceVpnClassification based on Integer32"""
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


_Hh3cmplsVpnInterfaceVpnClassification_Type.__name__ = "Integer32"
_Hh3cmplsVpnInterfaceVpnClassification_Object = MibTableColumn
hh3cmplsVpnInterfaceVpnClassification = _Hh3cmplsVpnInterfaceVpnClassification_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 3),
    _Hh3cmplsVpnInterfaceVpnClassification_Type()
)
hh3cmplsVpnInterfaceVpnClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceVpnClassification.setStatus("current")
_Hh3cmplsVpnInterfaceIpAddress_Type = InetAddress
_Hh3cmplsVpnInterfaceIpAddress_Object = MibTableColumn
hh3cmplsVpnInterfaceIpAddress = _Hh3cmplsVpnInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 4),
    _Hh3cmplsVpnInterfaceIpAddress_Type()
)
hh3cmplsVpnInterfaceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceIpAddress.setStatus("current")
_Hh3cmplsVpnInterfaceIpAddressMask_Type = InetAddress
_Hh3cmplsVpnInterfaceIpAddressMask_Object = MibTableColumn
hh3cmplsVpnInterfaceIpAddressMask = _Hh3cmplsVpnInterfaceIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 5),
    _Hh3cmplsVpnInterfaceIpAddressMask_Type()
)
hh3cmplsVpnInterfaceIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceIpAddressMask.setStatus("current")
_Hh3cmplsVpnInterfaceConfRowStatus_Type = RowStatus
_Hh3cmplsVpnInterfaceConfRowStatus_Object = MibTableColumn
hh3cmplsVpnInterfaceConfRowStatus = _Hh3cmplsVpnInterfaceConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 1, 1, 6),
    _Hh3cmplsVpnInterfaceConfRowStatus_Type()
)
hh3cmplsVpnInterfaceConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnInterfaceConfRowStatus.setStatus("current")
_Hh3cmplsVpnVrfConfTable_Object = MibTable
hh3cmplsVpnVrfConfTable = _Hh3cmplsVpnVrfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfTable.setStatus("current")
_Hh3cmplsVpnVrfConfEntry_Object = MibTableRow
hh3cmplsVpnVrfConfEntry = _Hh3cmplsVpnVrfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1)
)
hh3cmplsVpnVrfConfEntry.setIndexNames(
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfEntry.setStatus("current")
_Hh3cmplsVpnVrfName_Type = Hh3cMplsVpnId
_Hh3cmplsVpnVrfName_Object = MibTableColumn
hh3cmplsVpnVrfName = _Hh3cmplsVpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 1),
    _Hh3cmplsVpnVrfName_Type()
)
hh3cmplsVpnVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfName.setStatus("current")
_Hh3cmplsVpnVrfRouteDistinguisher_Type = Hh3cMplsVpnRouteDistinguisher
_Hh3cmplsVpnVrfRouteDistinguisher_Object = MibTableColumn
hh3cmplsVpnVrfRouteDistinguisher = _Hh3cmplsVpnVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 2),
    _Hh3cmplsVpnVrfRouteDistinguisher_Type()
)
hh3cmplsVpnVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteDistinguisher.setStatus("current")


class _Hh3cmplsVpnVrfNetPrefixType_Type(Integer32):
    """Custom type hh3cmplsVpnVrfNetPrefixType based on Integer32"""
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


_Hh3cmplsVpnVrfNetPrefixType_Type.__name__ = "Integer32"
_Hh3cmplsVpnVrfNetPrefixType_Object = MibTableColumn
hh3cmplsVpnVrfNetPrefixType = _Hh3cmplsVpnVrfNetPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 3),
    _Hh3cmplsVpnVrfNetPrefixType_Type()
)
hh3cmplsVpnVrfNetPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfNetPrefixType.setStatus("current")
_Hh3cmplsVpnVrfNetPrefix_Type = InetAddress
_Hh3cmplsVpnVrfNetPrefix_Object = MibTableColumn
hh3cmplsVpnVrfNetPrefix = _Hh3cmplsVpnVrfNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 4),
    _Hh3cmplsVpnVrfNetPrefix_Type()
)
hh3cmplsVpnVrfNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfNetPrefix.setStatus("current")
_Hh3cmplsVpnVrfIpRouteRedistributeConn_Type = TruthValue
_Hh3cmplsVpnVrfIpRouteRedistributeConn_Object = MibTableColumn
hh3cmplsVpnVrfIpRouteRedistributeConn = _Hh3cmplsVpnVrfIpRouteRedistributeConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 5),
    _Hh3cmplsVpnVrfIpRouteRedistributeConn_Type()
)
hh3cmplsVpnVrfIpRouteRedistributeConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfIpRouteRedistributeConn.setStatus("current")
_Hh3cmplsVpnVrfIpRouteRedistributeStatic_Type = TruthValue
_Hh3cmplsVpnVrfIpRouteRedistributeStatic_Object = MibTableColumn
hh3cmplsVpnVrfIpRouteRedistributeStatic = _Hh3cmplsVpnVrfIpRouteRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 6),
    _Hh3cmplsVpnVrfIpRouteRedistributeStatic_Type()
)
hh3cmplsVpnVrfIpRouteRedistributeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfIpRouteRedistributeStatic.setStatus("current")
_Hh3cmplsVpnVrfIpRouteRedistributeRip_Type = TruthValue
_Hh3cmplsVpnVrfIpRouteRedistributeRip_Object = MibTableColumn
hh3cmplsVpnVrfIpRouteRedistributeRip = _Hh3cmplsVpnVrfIpRouteRedistributeRip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 7),
    _Hh3cmplsVpnVrfIpRouteRedistributeRip_Type()
)
hh3cmplsVpnVrfIpRouteRedistributeRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfIpRouteRedistributeRip.setStatus("current")
_Hh3cmplsVpnVrfConfHighRouteThreshold_Type = Unsigned32
_Hh3cmplsVpnVrfConfHighRouteThreshold_Object = MibTableColumn
hh3cmplsVpnVrfConfHighRouteThreshold = _Hh3cmplsVpnVrfConfHighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 8),
    _Hh3cmplsVpnVrfConfHighRouteThreshold_Type()
)
hh3cmplsVpnVrfConfHighRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfHighRouteThreshold.setStatus("current")
_Hh3cmplsVpnVrfConfIsWarnOnly_Type = TruthValue
_Hh3cmplsVpnVrfConfIsWarnOnly_Object = MibTableColumn
hh3cmplsVpnVrfConfIsWarnOnly = _Hh3cmplsVpnVrfConfIsWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 9),
    _Hh3cmplsVpnVrfConfIsWarnOnly_Type()
)
hh3cmplsVpnVrfConfIsWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfIsWarnOnly.setStatus("current")
_Hh3cmplsVpnVrfConfMaxRoutes_Type = Unsigned32
_Hh3cmplsVpnVrfConfMaxRoutes_Object = MibTableColumn
hh3cmplsVpnVrfConfMaxRoutes = _Hh3cmplsVpnVrfConfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 10),
    _Hh3cmplsVpnVrfConfMaxRoutes_Type()
)
hh3cmplsVpnVrfConfMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfMaxRoutes.setStatus("current")
_Hh3cmplsVpnVrfConfRowStatus_Type = RowStatus
_Hh3cmplsVpnVrfConfRowStatus_Object = MibTableColumn
hh3cmplsVpnVrfConfRowStatus = _Hh3cmplsVpnVrfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 2, 1, 11),
    _Hh3cmplsVpnVrfConfRowStatus_Type()
)
hh3cmplsVpnVrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfConfRowStatus.setStatus("current")
_Hh3cmplsVpnVrfRouteTargetTable_Object = MibTable
hh3cmplsVpnVrfRouteTargetTable = _Hh3cmplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTargetTable.setStatus("current")
_Hh3cmplsVpnVrfRouteTargetEntry_Object = MibTableRow
hh3cmplsVpnVrfRouteTargetEntry = _Hh3cmplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 3, 1)
)
hh3cmplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfName"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfRouteTarget"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfRouteTargetType"),
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTargetEntry.setStatus("current")
_Hh3cmplsVpnVrfRouteTarget_Type = Hh3cMplsVpnRouteDistinguisher
_Hh3cmplsVpnVrfRouteTarget_Object = MibTableColumn
hh3cmplsVpnVrfRouteTarget = _Hh3cmplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 3, 1, 1),
    _Hh3cmplsVpnVrfRouteTarget_Type()
)
hh3cmplsVpnVrfRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTarget.setStatus("current")


class _Hh3cmplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type hh3cmplsVpnVrfRouteTargetType based on Integer32"""
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


_Hh3cmplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_Hh3cmplsVpnVrfRouteTargetType_Object = MibTableColumn
hh3cmplsVpnVrfRouteTargetType = _Hh3cmplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 3, 1, 2),
    _Hh3cmplsVpnVrfRouteTargetType_Type()
)
hh3cmplsVpnVrfRouteTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTargetType.setStatus("current")
_Hh3cmplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_Hh3cmplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
hh3cmplsVpnVrfRouteTargetRowStatus = _Hh3cmplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 3, 1, 3),
    _Hh3cmplsVpnVrfRouteTargetRowStatus_Type()
)
hh3cmplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTargetRowStatus.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrAddrTable_Object = MibTable
hh3cmplsVpnVrfBgpNbrAddrTable = _Hh3cmplsVpnVrfBgpNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrAddrTable.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrAddrEntry_Object = MibTableRow
hh3cmplsVpnVrfBgpNbrAddrEntry = _Hh3cmplsVpnVrfBgpNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1)
)
hh3cmplsVpnVrfBgpNbrAddrEntry.setIndexNames(
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfName"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrAddrEntry.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrAddr_Type = InetAddress
_Hh3cmplsVpnVrfBgpNbrAddr_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrAddr = _Hh3cmplsVpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 1),
    _Hh3cmplsVpnVrfBgpNbrAddr_Type()
)
hh3cmplsVpnVrfBgpNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrAddr.setStatus("current")


class _Hh3cmplsVpnVrfBgpNbrRole_Type(Integer32):
    """Custom type hh3cmplsVpnVrfBgpNbrRole based on Integer32"""
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


_Hh3cmplsVpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_Hh3cmplsVpnVrfBgpNbrRole_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrRole = _Hh3cmplsVpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 2),
    _Hh3cmplsVpnVrfBgpNbrRole_Type()
)
hh3cmplsVpnVrfBgpNbrRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrRole.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrType_Type = InetAddressType
_Hh3cmplsVpnVrfBgpNbrType_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrType = _Hh3cmplsVpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 3),
    _Hh3cmplsVpnVrfBgpNbrType_Type()
)
hh3cmplsVpnVrfBgpNbrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrType.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrAsNumber_Type = Unsigned32
_Hh3cmplsVpnVrfBgpNbrAsNumber_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrAsNumber = _Hh3cmplsVpnVrfBgpNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 4),
    _Hh3cmplsVpnVrfBgpNbrAsNumber_Type()
)
hh3cmplsVpnVrfBgpNbrAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrAsNumber.setStatus("current")


class _Hh3cmplsVpnVrfBgpNbrAdminStatus_Type(Integer32):
    """Custom type hh3cmplsVpnVrfBgpNbrAdminStatus based on Integer32"""
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


_Hh3cmplsVpnVrfBgpNbrAdminStatus_Type.__name__ = "Integer32"
_Hh3cmplsVpnVrfBgpNbrAdminStatus_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrAdminStatus = _Hh3cmplsVpnVrfBgpNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 5),
    _Hh3cmplsVpnVrfBgpNbrAdminStatus_Type()
)
hh3cmplsVpnVrfBgpNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrAdminStatus.setStatus("current")
_Hh3cmplsVpnVrfBgpNbrRowStatus_Type = RowStatus
_Hh3cmplsVpnVrfBgpNbrRowStatus_Object = MibTableColumn
hh3cmplsVpnVrfBgpNbrRowStatus = _Hh3cmplsVpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 2, 4, 1, 6),
    _Hh3cmplsVpnVrfBgpNbrRowStatus_Type()
)
hh3cmplsVpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfBgpNbrRowStatus.setStatus("current")
_Hh3cmplsVpnRoute_ObjectIdentity = ObjectIdentity
hh3cmplsVpnRoute = _Hh3cmplsVpnRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3)
)
_Hh3cmplsVpnVrfRouteTable_Object = MibTable
hh3cmplsVpnVrfRouteTable = _Hh3cmplsVpnVrfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteTable.setStatus("current")
_Hh3cmplsVpnVrfRouteEntry_Object = MibTableRow
hh3cmplsVpnVrfRouteEntry = _Hh3cmplsVpnVrfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1)
)
hh3cmplsVpnVrfRouteEntry.setIndexNames(
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfName"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfRouteDest"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfRouteMask"),
    (0, "HH3C-MPLS-BGP-VPN-MIB", "hh3cmplsVpnVrfRouteNextHop"),
)
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteEntry.setStatus("current")
_Hh3cmplsVpnVrfRouteDest_Type = InetAddress
_Hh3cmplsVpnVrfRouteDest_Object = MibTableColumn
hh3cmplsVpnVrfRouteDest = _Hh3cmplsVpnVrfRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 1),
    _Hh3cmplsVpnVrfRouteDest_Type()
)
hh3cmplsVpnVrfRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteDest.setStatus("current")
_Hh3cmplsVpnVrfRouteMask_Type = InetAddress
_Hh3cmplsVpnVrfRouteMask_Object = MibTableColumn
hh3cmplsVpnVrfRouteMask = _Hh3cmplsVpnVrfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 2),
    _Hh3cmplsVpnVrfRouteMask_Type()
)
hh3cmplsVpnVrfRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteMask.setStatus("current")
_Hh3cmplsVpnVrfRouteNextHop_Type = InetAddress
_Hh3cmplsVpnVrfRouteNextHop_Object = MibTableColumn
hh3cmplsVpnVrfRouteNextHop = _Hh3cmplsVpnVrfRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 3),
    _Hh3cmplsVpnVrfRouteNextHop_Type()
)
hh3cmplsVpnVrfRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteNextHop.setStatus("current")
_Hh3cmplsVpnVrfRouteIfIndex_Type = InterfaceIndex
_Hh3cmplsVpnVrfRouteIfIndex_Object = MibTableColumn
hh3cmplsVpnVrfRouteIfIndex = _Hh3cmplsVpnVrfRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 4),
    _Hh3cmplsVpnVrfRouteIfIndex_Type()
)
hh3cmplsVpnVrfRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteIfIndex.setStatus("current")


class _Hh3cmplsVpnVrfRouteProto_Type(Integer32):
    """Custom type hh3cmplsVpnVrfRouteProto based on Integer32"""
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


_Hh3cmplsVpnVrfRouteProto_Type.__name__ = "Integer32"
_Hh3cmplsVpnVrfRouteProto_Object = MibTableColumn
hh3cmplsVpnVrfRouteProto = _Hh3cmplsVpnVrfRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 5),
    _Hh3cmplsVpnVrfRouteProto_Type()
)
hh3cmplsVpnVrfRouteProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteProto.setStatus("current")
_Hh3cmplsVpnVrfRouteRowStatus_Type = RowStatus
_Hh3cmplsVpnVrfRouteRowStatus_Object = MibTableColumn
hh3cmplsVpnVrfRouteRowStatus = _Hh3cmplsVpnVrfRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3, 1, 3, 1, 1, 6),
    _Hh3cmplsVpnVrfRouteRowStatus_Type()
)
hh3cmplsVpnVrfRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cmplsVpnVrfRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLS-BGP-VPN-MIB",
    **{"Hh3cMplsVpnId": Hh3cMplsVpnId,
       "Hh3cMplsVpnRouteDistinguisher": Hh3cMplsVpnRouteDistinguisher,
       "hh3cMplsVpn": hh3cMplsVpn,
       "hh3cmplsVpnObjects": hh3cmplsVpnObjects,
       "hh3cmplsVpnScalars": hh3cmplsVpnScalars,
       "hh3cmplsVpnConfiguredVrfs": hh3cmplsVpnConfiguredVrfs,
       "hh3cmplsVpnActiveVrfs": hh3cmplsVpnActiveVrfs,
       "hh3cmplsVpnConf": hh3cmplsVpnConf,
       "hh3cmplsVpnInterfaceConfTable": hh3cmplsVpnInterfaceConfTable,
       "hh3cmplsVpnInterfaceConfEntry": hh3cmplsVpnInterfaceConfEntry,
       "hh3cmplsVpnInterfaceConfIndex": hh3cmplsVpnInterfaceConfIndex,
       "hh3cmplsVpnInterfaceLabelEdgeType": hh3cmplsVpnInterfaceLabelEdgeType,
       "hh3cmplsVpnInterfaceVpnClassification": hh3cmplsVpnInterfaceVpnClassification,
       "hh3cmplsVpnInterfaceIpAddress": hh3cmplsVpnInterfaceIpAddress,
       "hh3cmplsVpnInterfaceIpAddressMask": hh3cmplsVpnInterfaceIpAddressMask,
       "hh3cmplsVpnInterfaceConfRowStatus": hh3cmplsVpnInterfaceConfRowStatus,
       "hh3cmplsVpnVrfConfTable": hh3cmplsVpnVrfConfTable,
       "hh3cmplsVpnVrfConfEntry": hh3cmplsVpnVrfConfEntry,
       "hh3cmplsVpnVrfName": hh3cmplsVpnVrfName,
       "hh3cmplsVpnVrfRouteDistinguisher": hh3cmplsVpnVrfRouteDistinguisher,
       "hh3cmplsVpnVrfNetPrefixType": hh3cmplsVpnVrfNetPrefixType,
       "hh3cmplsVpnVrfNetPrefix": hh3cmplsVpnVrfNetPrefix,
       "hh3cmplsVpnVrfIpRouteRedistributeConn": hh3cmplsVpnVrfIpRouteRedistributeConn,
       "hh3cmplsVpnVrfIpRouteRedistributeStatic": hh3cmplsVpnVrfIpRouteRedistributeStatic,
       "hh3cmplsVpnVrfIpRouteRedistributeRip": hh3cmplsVpnVrfIpRouteRedistributeRip,
       "hh3cmplsVpnVrfConfHighRouteThreshold": hh3cmplsVpnVrfConfHighRouteThreshold,
       "hh3cmplsVpnVrfConfIsWarnOnly": hh3cmplsVpnVrfConfIsWarnOnly,
       "hh3cmplsVpnVrfConfMaxRoutes": hh3cmplsVpnVrfConfMaxRoutes,
       "hh3cmplsVpnVrfConfRowStatus": hh3cmplsVpnVrfConfRowStatus,
       "hh3cmplsVpnVrfRouteTargetTable": hh3cmplsVpnVrfRouteTargetTable,
       "hh3cmplsVpnVrfRouteTargetEntry": hh3cmplsVpnVrfRouteTargetEntry,
       "hh3cmplsVpnVrfRouteTarget": hh3cmplsVpnVrfRouteTarget,
       "hh3cmplsVpnVrfRouteTargetType": hh3cmplsVpnVrfRouteTargetType,
       "hh3cmplsVpnVrfRouteTargetRowStatus": hh3cmplsVpnVrfRouteTargetRowStatus,
       "hh3cmplsVpnVrfBgpNbrAddrTable": hh3cmplsVpnVrfBgpNbrAddrTable,
       "hh3cmplsVpnVrfBgpNbrAddrEntry": hh3cmplsVpnVrfBgpNbrAddrEntry,
       "hh3cmplsVpnVrfBgpNbrAddr": hh3cmplsVpnVrfBgpNbrAddr,
       "hh3cmplsVpnVrfBgpNbrRole": hh3cmplsVpnVrfBgpNbrRole,
       "hh3cmplsVpnVrfBgpNbrType": hh3cmplsVpnVrfBgpNbrType,
       "hh3cmplsVpnVrfBgpNbrAsNumber": hh3cmplsVpnVrfBgpNbrAsNumber,
       "hh3cmplsVpnVrfBgpNbrAdminStatus": hh3cmplsVpnVrfBgpNbrAdminStatus,
       "hh3cmplsVpnVrfBgpNbrRowStatus": hh3cmplsVpnVrfBgpNbrRowStatus,
       "hh3cmplsVpnRoute": hh3cmplsVpnRoute,
       "hh3cmplsVpnVrfRouteTable": hh3cmplsVpnVrfRouteTable,
       "hh3cmplsVpnVrfRouteEntry": hh3cmplsVpnVrfRouteEntry,
       "hh3cmplsVpnVrfRouteDest": hh3cmplsVpnVrfRouteDest,
       "hh3cmplsVpnVrfRouteMask": hh3cmplsVpnVrfRouteMask,
       "hh3cmplsVpnVrfRouteNextHop": hh3cmplsVpnVrfRouteNextHop,
       "hh3cmplsVpnVrfRouteIfIndex": hh3cmplsVpnVrfRouteIfIndex,
       "hh3cmplsVpnVrfRouteProto": hh3cmplsVpnVrfRouteProto,
       "hh3cmplsVpnVrfRouteRowStatus": hh3cmplsVpnVrfRouteRowStatus}
)
