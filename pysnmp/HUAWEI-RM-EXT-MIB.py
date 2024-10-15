# SNMP MIB module (HUAWEI-RM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:44 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwRmExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145)
)
hwRmExt.setRevisions(
        ("2014-12-11 00:00",
         "2014-12-10 00:00",
         "2014-12-09 00:00",
         "2014-06-30 00:00",
         "2014-06-20 00:00",
         "2013-06-09 00:00",
         "2013-04-22 15:26",
         "2010-11-25 00:00",
         "2010-08-20 00:00",
         "2008-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRmExtObjects_ObjectIdentity = ObjectIdentity
hwRmExtObjects = _HwRmExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1)
)
_HwStaticRouteTable_Object = MibTable
hwStaticRouteTable = _HwStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1)
)
if mibBuilder.loadTexts:
    hwStaticRouteTable.setStatus("current")
_HwStaticRouteEntry_Object = MibTableRow
hwStaticRouteEntry = _HwStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1)
)
hwStaticRouteEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteSourceVpnName"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteDestIpAddr"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteDestMaskAddr"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteDestVpnName"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteNextHop"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteOutIfIndex"),
)
if mibBuilder.loadTexts:
    hwStaticRouteEntry.setStatus("current")


class _HwStaticRouteSourceVpnName_Type(OctetString):
    """Custom type hwStaticRouteSourceVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwStaticRouteSourceVpnName_Type.__name__ = "OctetString"
_HwStaticRouteSourceVpnName_Object = MibTableColumn
hwStaticRouteSourceVpnName = _HwStaticRouteSourceVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 1),
    _HwStaticRouteSourceVpnName_Type()
)
hwStaticRouteSourceVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteSourceVpnName.setStatus("current")
_HwStaticRouteDestIpAddr_Type = IpAddress
_HwStaticRouteDestIpAddr_Object = MibTableColumn
hwStaticRouteDestIpAddr = _HwStaticRouteDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 2),
    _HwStaticRouteDestIpAddr_Type()
)
hwStaticRouteDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteDestIpAddr.setStatus("current")
_HwStaticRouteDestMaskAddr_Type = IpAddress
_HwStaticRouteDestMaskAddr_Object = MibTableColumn
hwStaticRouteDestMaskAddr = _HwStaticRouteDestMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 3),
    _HwStaticRouteDestMaskAddr_Type()
)
hwStaticRouteDestMaskAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteDestMaskAddr.setStatus("current")


class _HwStaticRouteDestVpnName_Type(OctetString):
    """Custom type hwStaticRouteDestVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwStaticRouteDestVpnName_Type.__name__ = "OctetString"
_HwStaticRouteDestVpnName_Object = MibTableColumn
hwStaticRouteDestVpnName = _HwStaticRouteDestVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 4),
    _HwStaticRouteDestVpnName_Type()
)
hwStaticRouteDestVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteDestVpnName.setStatus("current")
_HwStaticRouteNextHop_Type = IpAddress
_HwStaticRouteNextHop_Object = MibTableColumn
hwStaticRouteNextHop = _HwStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 5),
    _HwStaticRouteNextHop_Type()
)
hwStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteNextHop.setStatus("current")
_HwStaticRouteOutIfIndex_Type = Unsigned32
_HwStaticRouteOutIfIndex_Object = MibTableColumn
hwStaticRouteOutIfIndex = _HwStaticRouteOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 6),
    _HwStaticRouteOutIfIndex_Type()
)
hwStaticRouteOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteOutIfIndex.setStatus("current")


class _HwStaticRouteBfdName_Type(OctetString):
    """Custom type hwStaticRouteBfdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwStaticRouteBfdName_Type.__name__ = "OctetString"
_HwStaticRouteBfdName_Object = MibTableColumn
hwStaticRouteBfdName = _HwStaticRouteBfdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 7),
    _HwStaticRouteBfdName_Type()
)
hwStaticRouteBfdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteBfdName.setStatus("current")


class _HwStaticRoutePrefer_Type(Integer32):
    """Custom type hwStaticRoutePrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwStaticRoutePrefer_Type.__name__ = "Integer32"
_HwStaticRoutePrefer_Object = MibTableColumn
hwStaticRoutePrefer = _HwStaticRoutePrefer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 8),
    _HwStaticRoutePrefer_Type()
)
hwStaticRoutePrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRoutePrefer.setStatus("current")


class _HwStaticRouteDescrip_Type(OctetString):
    """Custom type hwStaticRouteDescrip based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwStaticRouteDescrip_Type.__name__ = "OctetString"
_HwStaticRouteDescrip_Object = MibTableColumn
hwStaticRouteDescrip = _HwStaticRouteDescrip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 9),
    _HwStaticRouteDescrip_Type()
)
hwStaticRouteDescrip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteDescrip.setStatus("current")
_HwStaticRouteRowStatus_Type = RowStatus
_HwStaticRouteRowStatus_Object = MibTableColumn
hwStaticRouteRowStatus = _HwStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 1, 1, 10),
    _HwStaticRouteRowStatus_Type()
)
hwStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteRowStatus.setStatus("current")
_HwRouteStatTable_Object = MibTable
hwRouteStatTable = _HwRouteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2)
)
if mibBuilder.loadTexts:
    hwRouteStatTable.setStatus("current")
_HwRouteStatEntry_Object = MibTableRow
hwRouteStatEntry = _HwRouteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1)
)
hwRouteStatEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwRouteStatVpnName"),
    (0, "HUAWEI-RM-EXT-MIB", "hwRouteStatProtocolId"),
)
if mibBuilder.loadTexts:
    hwRouteStatEntry.setStatus("current")


class _HwRouteStatVpnName_Type(OctetString):
    """Custom type hwRouteStatVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwRouteStatVpnName_Type.__name__ = "OctetString"
_HwRouteStatVpnName_Object = MibTableColumn
hwRouteStatVpnName = _HwRouteStatVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 1),
    _HwRouteStatVpnName_Type()
)
hwRouteStatVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouteStatVpnName.setStatus("current")


class _HwRouteStatProtocolId_Type(Integer32):
    """Custom type hwRouteStatProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("direct", 1),
          ("isis", 6),
          ("ospf", 3),
          ("rip", 7),
          ("static", 2))
    )


_HwRouteStatProtocolId_Type.__name__ = "Integer32"
_HwRouteStatProtocolId_Object = MibTableColumn
hwRouteStatProtocolId = _HwRouteStatProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 2),
    _HwRouteStatProtocolId_Type()
)
hwRouteStatProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouteStatProtocolId.setStatus("current")
_HwRouteStatTotal_Type = Unsigned32
_HwRouteStatTotal_Object = MibTableColumn
hwRouteStatTotal = _HwRouteStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 3),
    _HwRouteStatTotal_Type()
)
hwRouteStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteStatTotal.setStatus("current")
_HwRouteStatActive_Type = Unsigned32
_HwRouteStatActive_Object = MibTableColumn
hwRouteStatActive = _HwRouteStatActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 4),
    _HwRouteStatActive_Type()
)
hwRouteStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteStatActive.setStatus("current")
_HwRouteStatAdded_Type = Unsigned32
_HwRouteStatAdded_Object = MibTableColumn
hwRouteStatAdded = _HwRouteStatAdded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 5),
    _HwRouteStatAdded_Type()
)
hwRouteStatAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteStatAdded.setStatus("current")
_HwRouteStatDeleted_Type = Unsigned32
_HwRouteStatDeleted_Object = MibTableColumn
hwRouteStatDeleted = _HwRouteStatDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 6),
    _HwRouteStatDeleted_Type()
)
hwRouteStatDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteStatDeleted.setStatus("current")
_HwRouteStatFreed_Type = Unsigned32
_HwRouteStatFreed_Object = MibTableColumn
hwRouteStatFreed = _HwRouteStatFreed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 2, 1, 7),
    _HwRouteStatFreed_Type()
)
hwRouteStatFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteStatFreed.setStatus("current")
_HwIpv6RouteStatTable_Object = MibTable
hwIpv6RouteStatTable = _HwIpv6RouteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3)
)
if mibBuilder.loadTexts:
    hwIpv6RouteStatTable.setStatus("current")
_HwIpv6RouteStatEntry_Object = MibTableRow
hwIpv6RouteStatEntry = _HwIpv6RouteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1)
)
hwIpv6RouteStatEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatVpnName"),
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatProtocolId"),
)
if mibBuilder.loadTexts:
    hwIpv6RouteStatEntry.setStatus("current")


class _HwIpv6RouteStatVpnName_Type(OctetString):
    """Custom type hwIpv6RouteStatVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpv6RouteStatVpnName_Type.__name__ = "OctetString"
_HwIpv6RouteStatVpnName_Object = MibTableColumn
hwIpv6RouteStatVpnName = _HwIpv6RouteStatVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 1),
    _HwIpv6RouteStatVpnName_Type()
)
hwIpv6RouteStatVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6RouteStatVpnName.setStatus("current")


class _HwIpv6RouteStatProtocolId_Type(Integer32):
    """Custom type hwIpv6RouteStatProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("direct", 1),
          ("isis", 6),
          ("ospf", 3),
          ("rip", 7),
          ("static", 2))
    )


_HwIpv6RouteStatProtocolId_Type.__name__ = "Integer32"
_HwIpv6RouteStatProtocolId_Object = MibTableColumn
hwIpv6RouteStatProtocolId = _HwIpv6RouteStatProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 2),
    _HwIpv6RouteStatProtocolId_Type()
)
hwIpv6RouteStatProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6RouteStatProtocolId.setStatus("current")
_HwIpv6RouteStatTotal_Type = Unsigned32
_HwIpv6RouteStatTotal_Object = MibTableColumn
hwIpv6RouteStatTotal = _HwIpv6RouteStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 3),
    _HwIpv6RouteStatTotal_Type()
)
hwIpv6RouteStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6RouteStatTotal.setStatus("current")
_HwIpv6RouteStatActive_Type = Unsigned32
_HwIpv6RouteStatActive_Object = MibTableColumn
hwIpv6RouteStatActive = _HwIpv6RouteStatActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 4),
    _HwIpv6RouteStatActive_Type()
)
hwIpv6RouteStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6RouteStatActive.setStatus("current")
_HwIpv6RouteStatAdded_Type = Unsigned32
_HwIpv6RouteStatAdded_Object = MibTableColumn
hwIpv6RouteStatAdded = _HwIpv6RouteStatAdded_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 5),
    _HwIpv6RouteStatAdded_Type()
)
hwIpv6RouteStatAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6RouteStatAdded.setStatus("current")
_HwIpv6RouteStatDeleted_Type = Unsigned32
_HwIpv6RouteStatDeleted_Object = MibTableColumn
hwIpv6RouteStatDeleted = _HwIpv6RouteStatDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 6),
    _HwIpv6RouteStatDeleted_Type()
)
hwIpv6RouteStatDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6RouteStatDeleted.setStatus("current")
_HwIpv6RouteStatFreed_Type = Unsigned32
_HwIpv6RouteStatFreed_Object = MibTableColumn
hwIpv6RouteStatFreed = _HwIpv6RouteStatFreed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 3, 1, 7),
    _HwIpv6RouteStatFreed_Type()
)
hwIpv6RouteStatFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6RouteStatFreed.setStatus("current")
_HwStaticRouteExtTable_Object = MibTable
hwStaticRouteExtTable = _HwStaticRouteExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4)
)
if mibBuilder.loadTexts:
    hwStaticRouteExtTable.setStatus("current")
_HwStaticRouteExtEntry_Object = MibTableRow
hwStaticRouteExtEntry = _HwStaticRouteExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1)
)
hwStaticRouteExtEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteSourceVpnNameExt"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteDestIpAddrExt"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteDestMaskAddrExt"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteNextHopExt"),
    (0, "HUAWEI-RM-EXT-MIB", "hwStaticRouteOutIfIndexExt"),
)
if mibBuilder.loadTexts:
    hwStaticRouteExtEntry.setStatus("current")


class _HwStaticRouteSourceVpnNameExt_Type(OctetString):
    """Custom type hwStaticRouteSourceVpnNameExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwStaticRouteSourceVpnNameExt_Type.__name__ = "OctetString"
_HwStaticRouteSourceVpnNameExt_Object = MibTableColumn
hwStaticRouteSourceVpnNameExt = _HwStaticRouteSourceVpnNameExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 1),
    _HwStaticRouteSourceVpnNameExt_Type()
)
hwStaticRouteSourceVpnNameExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteSourceVpnNameExt.setStatus("current")
_HwStaticRouteDestIpAddrExt_Type = IpAddress
_HwStaticRouteDestIpAddrExt_Object = MibTableColumn
hwStaticRouteDestIpAddrExt = _HwStaticRouteDestIpAddrExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 2),
    _HwStaticRouteDestIpAddrExt_Type()
)
hwStaticRouteDestIpAddrExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteDestIpAddrExt.setStatus("current")
_HwStaticRouteDestMaskAddrExt_Type = IpAddress
_HwStaticRouteDestMaskAddrExt_Object = MibTableColumn
hwStaticRouteDestMaskAddrExt = _HwStaticRouteDestMaskAddrExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 3),
    _HwStaticRouteDestMaskAddrExt_Type()
)
hwStaticRouteDestMaskAddrExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteDestMaskAddrExt.setStatus("current")
_HwStaticRouteNextHopExt_Type = IpAddress
_HwStaticRouteNextHopExt_Object = MibTableColumn
hwStaticRouteNextHopExt = _HwStaticRouteNextHopExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 4),
    _HwStaticRouteNextHopExt_Type()
)
hwStaticRouteNextHopExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteNextHopExt.setStatus("current")
_HwStaticRouteOutIfIndexExt_Type = Unsigned32
_HwStaticRouteOutIfIndexExt_Object = MibTableColumn
hwStaticRouteOutIfIndexExt = _HwStaticRouteOutIfIndexExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 5),
    _HwStaticRouteOutIfIndexExt_Type()
)
hwStaticRouteOutIfIndexExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaticRouteOutIfIndexExt.setStatus("current")


class _HwStaticRouteDestVpnNameExt_Type(OctetString):
    """Custom type hwStaticRouteDestVpnNameExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwStaticRouteDestVpnNameExt_Type.__name__ = "OctetString"
_HwStaticRouteDestVpnNameExt_Object = MibTableColumn
hwStaticRouteDestVpnNameExt = _HwStaticRouteDestVpnNameExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 6),
    _HwStaticRouteDestVpnNameExt_Type()
)
hwStaticRouteDestVpnNameExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteDestVpnNameExt.setStatus("current")


class _HwStaticRouteBfdNameExt_Type(OctetString):
    """Custom type hwStaticRouteBfdNameExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwStaticRouteBfdNameExt_Type.__name__ = "OctetString"
_HwStaticRouteBfdNameExt_Object = MibTableColumn
hwStaticRouteBfdNameExt = _HwStaticRouteBfdNameExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 7),
    _HwStaticRouteBfdNameExt_Type()
)
hwStaticRouteBfdNameExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteBfdNameExt.setStatus("current")


class _HwStaticRoutePreferExt_Type(Unsigned32):
    """Custom type hwStaticRoutePreferExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwStaticRoutePreferExt_Type.__name__ = "Unsigned32"
_HwStaticRoutePreferExt_Object = MibTableColumn
hwStaticRoutePreferExt = _HwStaticRoutePreferExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 8),
    _HwStaticRoutePreferExt_Type()
)
hwStaticRoutePreferExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRoutePreferExt.setStatus("current")


class _HwStaticRouteDescripExt_Type(OctetString):
    """Custom type hwStaticRouteDescripExt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwStaticRouteDescripExt_Type.__name__ = "OctetString"
_HwStaticRouteDescripExt_Object = MibTableColumn
hwStaticRouteDescripExt = _HwStaticRouteDescripExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 9),
    _HwStaticRouteDescripExt_Type()
)
hwStaticRouteDescripExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteDescripExt.setStatus("current")
_HwStaticRouteRowStatusExt_Type = RowStatus
_HwStaticRouteRowStatusExt_Object = MibTableColumn
hwStaticRouteRowStatusExt = _HwStaticRouteRowStatusExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 10),
    _HwStaticRouteRowStatusExt_Type()
)
hwStaticRouteRowStatusExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteRowStatusExt.setStatus("current")


class _HwStaticRoutePermanentExt_Type(Integer32):
    """Custom type hwStaticRoutePermanentExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("permanent", 1))
    )


_HwStaticRoutePermanentExt_Type.__name__ = "Integer32"
_HwStaticRoutePermanentExt_Object = MibTableColumn
hwStaticRoutePermanentExt = _HwStaticRoutePermanentExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 11),
    _HwStaticRoutePermanentExt_Type()
)
hwStaticRoutePermanentExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRoutePermanentExt.setStatus("current")


class _HwStaticRouteLdpSyncExt_Type(Integer32):
    """Custom type hwStaticRouteLdpSyncExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ldpsync", 1),
          ("none", 0))
    )


_HwStaticRouteLdpSyncExt_Type.__name__ = "Integer32"
_HwStaticRouteLdpSyncExt_Object = MibTableColumn
hwStaticRouteLdpSyncExt = _HwStaticRouteLdpSyncExt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 4, 1, 12),
    _HwStaticRouteLdpSyncExt_Type()
)
hwStaticRouteLdpSyncExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticRouteLdpSyncExt.setStatus("current")
_HwIpv6StaticRouteTable_Object = MibTable
hwIpv6StaticRouteTable = _HwIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5)
)
if mibBuilder.loadTexts:
    hwIpv6StaticRouteTable.setStatus("current")
_HwIpv6StaticRouteEntry_Object = MibTableRow
hwIpv6StaticRouteEntry = _HwIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1)
)
hwIpv6StaticRouteEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteSourceVpnName"),
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteDestIpAddr"),
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6StaticRoutePrefixLen"),
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteNextHop"),
    (0, "HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteOutIfIndex"),
)
if mibBuilder.loadTexts:
    hwIpv6StaticRouteEntry.setStatus("current")


class _HwIpv6StaticRouteSourceVpnName_Type(OctetString):
    """Custom type hwIpv6StaticRouteSourceVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpv6StaticRouteSourceVpnName_Type.__name__ = "OctetString"
_HwIpv6StaticRouteSourceVpnName_Object = MibTableColumn
hwIpv6StaticRouteSourceVpnName = _HwIpv6StaticRouteSourceVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 1),
    _HwIpv6StaticRouteSourceVpnName_Type()
)
hwIpv6StaticRouteSourceVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteSourceVpnName.setStatus("current")
_HwIpv6StaticRouteDestIpAddr_Type = Ipv6Address
_HwIpv6StaticRouteDestIpAddr_Object = MibTableColumn
hwIpv6StaticRouteDestIpAddr = _HwIpv6StaticRouteDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 2),
    _HwIpv6StaticRouteDestIpAddr_Type()
)
hwIpv6StaticRouteDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteDestIpAddr.setStatus("current")
_HwIpv6StaticRoutePrefixLen_Type = Unsigned32
_HwIpv6StaticRoutePrefixLen_Object = MibTableColumn
hwIpv6StaticRoutePrefixLen = _HwIpv6StaticRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 3),
    _HwIpv6StaticRoutePrefixLen_Type()
)
hwIpv6StaticRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6StaticRoutePrefixLen.setStatus("current")
_HwIpv6StaticRouteNextHop_Type = Ipv6Address
_HwIpv6StaticRouteNextHop_Object = MibTableColumn
hwIpv6StaticRouteNextHop = _HwIpv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 4),
    _HwIpv6StaticRouteNextHop_Type()
)
hwIpv6StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteNextHop.setStatus("current")
_HwIpv6StaticRouteOutIfIndex_Type = Unsigned32
_HwIpv6StaticRouteOutIfIndex_Object = MibTableColumn
hwIpv6StaticRouteOutIfIndex = _HwIpv6StaticRouteOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 5),
    _HwIpv6StaticRouteOutIfIndex_Type()
)
hwIpv6StaticRouteOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteOutIfIndex.setStatus("current")


class _HwIpv6StaticRouteDestVpnName_Type(OctetString):
    """Custom type hwIpv6StaticRouteDestVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpv6StaticRouteDestVpnName_Type.__name__ = "OctetString"
_HwIpv6StaticRouteDestVpnName_Object = MibTableColumn
hwIpv6StaticRouteDestVpnName = _HwIpv6StaticRouteDestVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 6),
    _HwIpv6StaticRouteDestVpnName_Type()
)
hwIpv6StaticRouteDestVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteDestVpnName.setStatus("current")


class _HwIpv6StaticRouteBfdName_Type(OctetString):
    """Custom type hwIpv6StaticRouteBfdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwIpv6StaticRouteBfdName_Type.__name__ = "OctetString"
_HwIpv6StaticRouteBfdName_Object = MibTableColumn
hwIpv6StaticRouteBfdName = _HwIpv6StaticRouteBfdName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 7),
    _HwIpv6StaticRouteBfdName_Type()
)
hwIpv6StaticRouteBfdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteBfdName.setStatus("current")


class _HwIpv6StaticRouteNqaAdminName_Type(OctetString):
    """Custom type hwIpv6StaticRouteNqaAdminName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIpv6StaticRouteNqaAdminName_Type.__name__ = "OctetString"
_HwIpv6StaticRouteNqaAdminName_Object = MibTableColumn
hwIpv6StaticRouteNqaAdminName = _HwIpv6StaticRouteNqaAdminName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 8),
    _HwIpv6StaticRouteNqaAdminName_Type()
)
hwIpv6StaticRouteNqaAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteNqaAdminName.setStatus("current")


class _HwIpv6StaticRouteNqaTestName_Type(OctetString):
    """Custom type hwIpv6StaticRouteNqaTestName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIpv6StaticRouteNqaTestName_Type.__name__ = "OctetString"
_HwIpv6StaticRouteNqaTestName_Object = MibTableColumn
hwIpv6StaticRouteNqaTestName = _HwIpv6StaticRouteNqaTestName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 9),
    _HwIpv6StaticRouteNqaTestName_Type()
)
hwIpv6StaticRouteNqaTestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteNqaTestName.setStatus("current")


class _HwIpv6StaticRoutePrefer_Type(Unsigned32):
    """Custom type hwIpv6StaticRoutePrefer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwIpv6StaticRoutePrefer_Type.__name__ = "Unsigned32"
_HwIpv6StaticRoutePrefer_Object = MibTableColumn
hwIpv6StaticRoutePrefer = _HwIpv6StaticRoutePrefer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 10),
    _HwIpv6StaticRoutePrefer_Type()
)
hwIpv6StaticRoutePrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRoutePrefer.setStatus("current")
_HwIpv6StaticRouteTag_Type = Unsigned32
_HwIpv6StaticRouteTag_Object = MibTableColumn
hwIpv6StaticRouteTag = _HwIpv6StaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 11),
    _HwIpv6StaticRouteTag_Type()
)
hwIpv6StaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteTag.setStatus("current")


class _HwIpv6StaticRouteDescr_Type(OctetString):
    """Custom type hwIpv6StaticRouteDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwIpv6StaticRouteDescr_Type.__name__ = "OctetString"
_HwIpv6StaticRouteDescr_Object = MibTableColumn
hwIpv6StaticRouteDescr = _HwIpv6StaticRouteDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 12),
    _HwIpv6StaticRouteDescr_Type()
)
hwIpv6StaticRouteDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteDescr.setStatus("current")
_HwIpv6StaticRouteRowStatus_Type = RowStatus
_HwIpv6StaticRouteRowStatus_Object = MibTableColumn
hwIpv6StaticRouteRowStatus = _HwIpv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 5, 1, 13),
    _HwIpv6StaticRouteRowStatus_Type()
)
hwIpv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpv6StaticRouteRowStatus.setStatus("current")
_HwRmInfo_ObjectIdentity = ObjectIdentity
hwRmInfo = _HwRmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 6)
)
_HwIpv4PrefixNum_Type = Unsigned32
_HwIpv4PrefixNum_Object = MibScalar
hwIpv4PrefixNum = _HwIpv4PrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 6, 1),
    _HwIpv4PrefixNum_Type()
)
hwIpv4PrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv4PrefixNum.setStatus("current")
_HwIpv6PrefixNum_Type = Unsigned32
_HwIpv6PrefixNum_Object = MibScalar
hwIpv6PrefixNum = _HwIpv6PrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 1, 6, 2),
    _HwIpv6PrefixNum_Type()
)
hwIpv6PrefixNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6PrefixNum.setStatus("current")
_HwRmExtConformance_ObjectIdentity = ObjectIdentity
hwRmExtConformance = _HwRmExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2)
)
_HwRmExtCompliances_ObjectIdentity = ObjectIdentity
hwRmExtCompliances = _HwRmExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 1)
)
_HwRmExtGroups_ObjectIdentity = ObjectIdentity
hwRmExtGroups = _HwRmExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2)
)
_HwTunnelExtObjects_ObjectIdentity = ObjectIdentity
hwTunnelExtObjects = _HwTunnelExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3)
)
_HwTnl2L3vpnTable_Object = MibTable
hwTnl2L3vpnTable = _HwTnl2L3vpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 1)
)
if mibBuilder.loadTexts:
    hwTnl2L3vpnTable.setStatus("current")
_HwTnl2L3vpnEntry_Object = MibTableRow
hwTnl2L3vpnEntry = _HwTnl2L3vpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 1, 1)
)
hwTnl2L3vpnEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwL3vpnTnlId"),
    (0, "HUAWEI-RM-EXT-MIB", "hwVpnIndex"),
)
if mibBuilder.loadTexts:
    hwTnl2L3vpnEntry.setStatus("current")
_HwL3vpnTnlId_Type = Unsigned32
_HwL3vpnTnlId_Object = MibTableColumn
hwL3vpnTnlId = _HwL3vpnTnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 1, 1, 1),
    _HwL3vpnTnlId_Type()
)
hwL3vpnTnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL3vpnTnlId.setStatus("current")


class _HwVpnIndex_Type(Unsigned32):
    """Custom type hwVpnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwVpnIndex_Type.__name__ = "Unsigned32"
_HwVpnIndex_Object = MibTableColumn
hwVpnIndex = _HwVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 1, 1, 2),
    _HwVpnIndex_Type()
)
hwVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVpnIndex.setStatus("current")


class _HwVpnName_Type(OctetString):
    """Custom type hwVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVpnName_Type.__name__ = "OctetString"
_HwVpnName_Object = MibTableColumn
hwVpnName = _HwVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 1, 1, 3),
    _HwVpnName_Type()
)
hwVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnName.setStatus("current")
_HwTnl2VplsTable_Object = MibTable
hwTnl2VplsTable = _HwTnl2VplsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2)
)
if mibBuilder.loadTexts:
    hwTnl2VplsTable.setStatus("current")
_HwTnl2VplsEntry_Object = MibTableRow
hwTnl2VplsEntry = _HwTnl2VplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1)
)
hwTnl2VplsEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwVplsTnlId"),
    (0, "HUAWEI-RM-EXT-MIB", "hwVplsVcId"),
)
if mibBuilder.loadTexts:
    hwTnl2VplsEntry.setStatus("current")
_HwVplsTnlId_Type = Unsigned32
_HwVplsTnlId_Object = MibTableColumn
hwVplsTnlId = _HwVplsTnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 1),
    _HwVplsTnlId_Type()
)
hwVplsTnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsTnlId.setStatus("current")
_HwVplsVcId_Type = Unsigned32
_HwVplsVcId_Object = MibTableColumn
hwVplsVcId = _HwVplsVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 2),
    _HwVplsVcId_Type()
)
hwVplsVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsVcId.setStatus("current")
_HwVsiIndex_Type = Unsigned32
_HwVsiIndex_Object = MibTableColumn
hwVsiIndex = _HwVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 3),
    _HwVsiIndex_Type()
)
hwVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsiIndex.setStatus("current")
_HwVsiId_Type = Unsigned32
_HwVsiId_Object = MibTableColumn
hwVsiId = _HwVsiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 4),
    _HwVsiId_Type()
)
hwVsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsiId.setStatus("current")


class _HwVsiName_Type(OctetString):
    """Custom type hwVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVsiName_Type.__name__ = "OctetString"
_HwVsiName_Object = MibTableColumn
hwVsiName = _HwVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 5),
    _HwVsiName_Type()
)
hwVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsiName.setStatus("current")
_HwVplsVcType_Type = Unsigned32
_HwVplsVcType_Object = MibTableColumn
hwVplsVcType = _HwVplsVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 6),
    _HwVplsVcType_Type()
)
hwVplsVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsVcType.setStatus("current")
_HwVplsPeerIp_Type = IpAddress
_HwVplsPeerIp_Object = MibTableColumn
hwVplsPeerIp = _HwVplsPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 2, 1, 7),
    _HwVplsPeerIp_Type()
)
hwVplsPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVplsPeerIp.setStatus("current")
_HwTnl2Pwe3VllTable_Object = MibTable
hwTnl2Pwe3VllTable = _HwTnl2Pwe3VllTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3)
)
if mibBuilder.loadTexts:
    hwTnl2Pwe3VllTable.setStatus("current")
_HwTnl2Pwe3VllEntry_Object = MibTableRow
hwTnl2Pwe3VllEntry = _HwTnl2Pwe3VllEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1)
)
hwTnl2Pwe3VllEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwPwVllTnlId"),
    (0, "HUAWEI-RM-EXT-MIB", "hwAcIndex"),
)
if mibBuilder.loadTexts:
    hwTnl2Pwe3VllEntry.setStatus("current")
_HwPwVllTnlId_Type = Unsigned32
_HwPwVllTnlId_Object = MibTableColumn
hwPwVllTnlId = _HwPwVllTnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 1),
    _HwPwVllTnlId_Type()
)
hwPwVllTnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwVllTnlId.setStatus("current")
_HwAcIndex_Type = Unsigned32
_HwAcIndex_Object = MibTableColumn
hwAcIndex = _HwAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 2),
    _HwAcIndex_Type()
)
hwAcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAcIndex.setStatus("current")


class _HwPwVllIfName_Type(OctetString):
    """Custom type hwPwVllIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPwVllIfName_Type.__name__ = "OctetString"
_HwPwVllIfName_Object = MibTableColumn
hwPwVllIfName = _HwPwVllIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 3),
    _HwPwVllIfName_Type()
)
hwPwVllIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVllIfName.setStatus("current")
_HwMasterSlaveFlag_Type = Unsigned32
_HwMasterSlaveFlag_Object = MibTableColumn
hwMasterSlaveFlag = _HwMasterSlaveFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 4),
    _HwMasterSlaveFlag_Type()
)
hwMasterSlaveFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMasterSlaveFlag.setStatus("current")
_HwPwVllPeerIp_Type = IpAddress
_HwPwVllPeerIp_Object = MibTableColumn
hwPwVllPeerIp = _HwPwVllPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 5),
    _HwPwVllPeerIp_Type()
)
hwPwVllPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVllPeerIp.setStatus("current")
_HwPwVllVcId_Type = Unsigned32
_HwPwVllVcId_Object = MibTableColumn
hwPwVllVcId = _HwPwVllVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 6),
    _HwPwVllVcId_Type()
)
hwPwVllVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVllVcId.setStatus("current")
_HwPwVllSvcFlag_Type = Unsigned32
_HwPwVllSvcFlag_Object = MibTableColumn
hwPwVllSvcFlag = _HwPwVllSvcFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 7),
    _HwPwVllSvcFlag_Type()
)
hwPwVllSvcFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVllSvcFlag.setStatus("current")


class _HwPwVcType_Type(Integer32):
    """Custom type hwPwVcType based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5PduVccTransport", 14),
          ("atmAal5SduVccTransport", 2),
          ("atmN2OneVccCellTransport", 9),
          ("atmN2OneVpcCellTransport", 10),
          ("atmOne2OneVccCellMode", 12),
          ("atmOne2OneVpcCellMode", 13),
          ("atmTransparentCellTransport", 3),
          ("cESoPsnBasicMode", 21),
          ("cem", 8),
          ("cep", 16),
          ("ethernet", 5),
          ("frameRelayDlci", 25),
          ("frameRelayDlciMartini", 1),
          ("frameRelayPortMode", 15),
          ("hdlc", 6),
          ("ipInterworking", 64),
          ("ipLayer2Transport", 11),
          ("l2VpnCESoPSNTDMwithCAS", 23),
          ("l2VpnTDMoIPTDMwithCAS", 24),
          ("ppp", 7),
          ("saE1oP", 17),
          ("saE3oP", 19),
          ("saT1oP", 18),
          ("saT3oP", 20),
          ("tDMoIPbasicMode", 22),
          ("unknown", 255),
          ("vlan", 4))
    )


_HwPwVcType_Type.__name__ = "Integer32"
_HwPwVcType_Object = MibTableColumn
hwPwVcType = _HwPwVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 8),
    _HwPwVcType_Type()
)
hwPwVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwVcType.setStatus("current")
_HwSvcReceiveLabel_Type = Unsigned32
_HwSvcReceiveLabel_Object = MibTableColumn
hwSvcReceiveLabel = _HwSvcReceiveLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 9),
    _HwSvcReceiveLabel_Type()
)
hwSvcReceiveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcReceiveLabel.setStatus("current")
_HwSvcTransmitLabel_Type = Unsigned32
_HwSvcTransmitLabel_Object = MibTableColumn
hwSvcTransmitLabel = _HwSvcTransmitLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 3, 1, 10),
    _HwSvcTransmitLabel_Type()
)
hwSvcTransmitLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSvcTransmitLabel.setStatus("current")
_HwTnlIf2TnlIdTable_Object = MibTable
hwTnlIf2TnlIdTable = _HwTnlIf2TnlIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 4)
)
if mibBuilder.loadTexts:
    hwTnlIf2TnlIdTable.setStatus("current")
_HwTnlIf2TnlIdEntry_Object = MibTableRow
hwTnlIf2TnlIdEntry = _HwTnlIf2TnlIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 4, 1)
)
hwTnlIf2TnlIdEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwTunnelIf"),
)
if mibBuilder.loadTexts:
    hwTnlIf2TnlIdEntry.setStatus("current")


class _HwTunnelIf_Type(OctetString):
    """Custom type hwTunnelIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwTunnelIf_Type.__name__ = "OctetString"
_HwTunnelIf_Object = MibTableColumn
hwTunnelIf = _HwTunnelIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 4, 1, 1),
    _HwTunnelIf_Type()
)
hwTunnelIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTunnelIf.setStatus("current")
_HwTunnelId_Type = Unsigned32
_HwTunnelId_Object = MibTableColumn
hwTunnelId = _HwTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 4, 1, 2),
    _HwTunnelId_Type()
)
hwTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnelId.setStatus("current")
_HwTnl2MultiHopPwe3Table_Object = MibTable
hwTnl2MultiHopPwe3Table = _HwTnl2MultiHopPwe3Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5)
)
if mibBuilder.loadTexts:
    hwTnl2MultiHopPwe3Table.setStatus("current")
_HwTnl2MultiHopPwe3Entry_Object = MibTableRow
hwTnl2MultiHopPwe3Entry = _HwTnl2MultiHopPwe3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5, 1)
)
hwTnl2MultiHopPwe3Entry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwMultiHopPwe3TnlId"),
    (0, "HUAWEI-RM-EXT-MIB", "hwMultiHopPwe3VcType"),
    (0, "HUAWEI-RM-EXT-MIB", "hwMultiHopPwe3VcId"),
)
if mibBuilder.loadTexts:
    hwTnl2MultiHopPwe3Entry.setStatus("current")
_HwMultiHopPwe3TnlId_Type = Unsigned32
_HwMultiHopPwe3TnlId_Object = MibTableColumn
hwMultiHopPwe3TnlId = _HwMultiHopPwe3TnlId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5, 1, 1),
    _HwMultiHopPwe3TnlId_Type()
)
hwMultiHopPwe3TnlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMultiHopPwe3TnlId.setStatus("current")
_HwMultiHopPwe3VcType_Type = Unsigned32
_HwMultiHopPwe3VcType_Object = MibTableColumn
hwMultiHopPwe3VcType = _HwMultiHopPwe3VcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5, 1, 2),
    _HwMultiHopPwe3VcType_Type()
)
hwMultiHopPwe3VcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMultiHopPwe3VcType.setStatus("current")
_HwMultiHopPwe3VcId_Type = Unsigned32
_HwMultiHopPwe3VcId_Object = MibTableColumn
hwMultiHopPwe3VcId = _HwMultiHopPwe3VcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5, 1, 3),
    _HwMultiHopPwe3VcId_Type()
)
hwMultiHopPwe3VcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMultiHopPwe3VcId.setStatus("current")
_HwMultiHopPwe3PeerIp_Type = IpAddress
_HwMultiHopPwe3PeerIp_Object = MibTableColumn
hwMultiHopPwe3PeerIp = _HwMultiHopPwe3PeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 3, 5, 1, 4),
    _HwMultiHopPwe3PeerIp_Type()
)
hwMultiHopPwe3PeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMultiHopPwe3PeerIp.setStatus("current")
_HwTunnelExtConformance_ObjectIdentity = ObjectIdentity
hwTunnelExtConformance = _HwTunnelExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4)
)
_HwTunnelExtCompliances_ObjectIdentity = ObjectIdentity
hwTunnelExtCompliances = _HwTunnelExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 1)
)
_HwTunnelExtGroups_ObjectIdentity = ObjectIdentity
hwTunnelExtGroups = _HwTunnelExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2)
)
_HwTnlGroupTrapObjects_ObjectIdentity = ObjectIdentity
hwTnlGroupTrapObjects = _HwTnlGroupTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 5)
)
_HwTnlDestination_Type = IpAddress
_HwTnlDestination_Object = MibScalar
hwTnlDestination = _HwTnlDestination_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 5, 1),
    _HwTnlDestination_Type()
)
hwTnlDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTnlDestination.setStatus("current")


class _HwTnlPolicy_Type(OctetString):
    """Custom type hwTnlPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_HwTnlPolicy_Type.__name__ = "OctetString"
_HwTnlPolicy_Object = MibScalar
hwTnlPolicy = _HwTnlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 5, 2),
    _HwTnlPolicy_Type()
)
hwTnlPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTnlPolicy.setStatus("current")
_HwTnlGroupTraps_ObjectIdentity = ObjectIdentity
hwTnlGroupTraps = _HwTnlGroupTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 6)
)
_HwTnlGroupTrapConformance_ObjectIdentity = ObjectIdentity
hwTnlGroupTrapConformance = _HwTnlGroupTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 7)
)
_HwIpv4PrefixLimitTrapObjects_ObjectIdentity = ObjectIdentity
hwIpv4PrefixLimitTrapObjects = _HwIpv4PrefixLimitTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 8)
)
_HwCurIpv4PrefixNum_Type = Unsigned32
_HwCurIpv4PrefixNum_Object = MibScalar
hwCurIpv4PrefixNum = _HwCurIpv4PrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 8, 1),
    _HwCurIpv4PrefixNum_Type()
)
hwCurIpv4PrefixNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCurIpv4PrefixNum.setStatus("current")
_HwIpv4PrefixLimitValue_Type = Unsigned32
_HwIpv4PrefixLimitValue_Object = MibScalar
hwIpv4PrefixLimitValue = _HwIpv4PrefixLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 8, 2),
    _HwIpv4PrefixLimitValue_Type()
)
hwIpv4PrefixLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpv4PrefixLimitValue.setStatus("current")
_HwIpv6PrefixLimitTrapObjects_ObjectIdentity = ObjectIdentity
hwIpv6PrefixLimitTrapObjects = _HwIpv6PrefixLimitTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 9)
)
_HwCurIpv6PrefixNum_Type = Unsigned32
_HwCurIpv6PrefixNum_Object = MibScalar
hwCurIpv6PrefixNum = _HwCurIpv6PrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 9, 1),
    _HwCurIpv6PrefixNum_Type()
)
hwCurIpv6PrefixNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCurIpv6PrefixNum.setStatus("current")
_HwIpv6PrefixLimitValue_Type = Unsigned32
_HwIpv6PrefixLimitValue_Object = MibScalar
hwIpv6PrefixLimitValue = _HwIpv6PrefixLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 9, 2),
    _HwIpv6PrefixLimitValue_Type()
)
hwIpv6PrefixLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpv6PrefixLimitValue.setStatus("current")


class _HwIpv6PrefixLimitVpnName_Type(OctetString):
    """Custom type hwIpv6PrefixLimitVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpv6PrefixLimitVpnName_Type.__name__ = "OctetString"
_HwIpv6PrefixLimitVpnName_Object = MibScalar
hwIpv6PrefixLimitVpnName = _HwIpv6PrefixLimitVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 9, 3),
    _HwIpv6PrefixLimitVpnName_Type()
)
hwIpv6PrefixLimitVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpv6PrefixLimitVpnName.setStatus("current")
_HwIpv4PrefixLimitTraps_ObjectIdentity = ObjectIdentity
hwIpv4PrefixLimitTraps = _HwIpv4PrefixLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 10)
)
_HwIpv6PrefixLimitTraps_ObjectIdentity = ObjectIdentity
hwIpv6PrefixLimitTraps = _HwIpv6PrefixLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 11)
)
_HwIpv4PrefixLimitConformance_ObjectIdentity = ObjectIdentity
hwIpv4PrefixLimitConformance = _HwIpv4PrefixLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 12)
)
_HwIpv6PrefixLimitConformance_ObjectIdentity = ObjectIdentity
hwIpv6PrefixLimitConformance = _HwIpv6PrefixLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 13)
)
_HwRmGresmTokenObjects_ObjectIdentity = ObjectIdentity
hwRmGresmTokenObjects = _HwRmGresmTokenObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14)
)
_HwGresmTokenTable_Object = MibTable
hwGresmTokenTable = _HwGresmTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14, 1)
)
if mibBuilder.loadTexts:
    hwGresmTokenTable.setStatus("current")
_HwGresmTokenEntry_Object = MibTableRow
hwGresmTokenEntry = _HwGresmTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14, 1, 1)
)
hwGresmTokenEntry.setIndexNames(
    (0, "HUAWEI-RM-EXT-MIB", "hwGresmTokenMode"),
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwGresmTokenEntry.setStatus("current")


class _HwGresmTokenMode_Type(Integer32):
    """Custom type hwGresmTokenMode based on Integer32"""
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
        *(("global1", 1),
          ("global2", 2),
          ("global3", 3),
          ("global4", 4),
          ("perborad", 5))
    )


_HwGresmTokenMode_Type.__name__ = "Integer32"
_HwGresmTokenMode_Object = MibTableColumn
hwGresmTokenMode = _HwGresmTokenMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14, 1, 1, 1),
    _HwGresmTokenMode_Type()
)
hwGresmTokenMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGresmTokenMode.setStatus("current")
_HwGresmTokenUsedNum_Type = Integer32
_HwGresmTokenUsedNum_Object = MibTableColumn
hwGresmTokenUsedNum = _HwGresmTokenUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14, 1, 1, 2),
    _HwGresmTokenUsedNum_Type()
)
hwGresmTokenUsedNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGresmTokenUsedNum.setStatus("current")
_HwGresmTokenMaxValue_Type = Integer32
_HwGresmTokenMaxValue_Object = MibTableColumn
hwGresmTokenMaxValue = _HwGresmTokenMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 14, 1, 1, 3),
    _HwGresmTokenMaxValue_Type()
)
hwGresmTokenMaxValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGresmTokenMaxValue.setStatus("current")
_HwGresmTokenTraps_ObjectIdentity = ObjectIdentity
hwGresmTokenTraps = _HwGresmTokenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 15)
)
_HwGresmTokenTrapConformance_ObjectIdentity = ObjectIdentity
hwGresmTokenTrapConformance = _HwGresmTokenTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 16)
)
_HwRmExtRouteObjects_ObjectIdentity = ObjectIdentity
hwRmExtRouteObjects = _HwRmExtRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 17)
)
_HwRmExtRouteTrapObjects_ObjectIdentity = ObjectIdentity
hwRmExtRouteTrapObjects = _HwRmExtRouteTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 18)
)
_HwRmExtRouteTraps_ObjectIdentity = ObjectIdentity
hwRmExtRouteTraps = _HwRmExtRouteTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19)
)
_HwPublicIpv4PrefixLimitTraps_ObjectIdentity = ObjectIdentity
hwPublicIpv4PrefixLimitTraps = _HwPublicIpv4PrefixLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 1)
)
_HwPublicIpv6PrefixLimitTraps_ObjectIdentity = ObjectIdentity
hwPublicIpv6PrefixLimitTraps = _HwPublicIpv6PrefixLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 2)
)
_HwL3vpnIpv6PrefixLimitTraps_ObjectIdentity = ObjectIdentity
hwL3vpnIpv6PrefixLimitTraps = _HwL3vpnIpv6PrefixLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 3)
)
_HwRmExtRouteConformance_ObjectIdentity = ObjectIdentity
hwRmExtRouteConformance = _HwRmExtRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20)
)
_HwRmExtRouteGroup_ObjectIdentity = ObjectIdentity
hwRmExtRouteGroup = _HwRmExtRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2)
)
_HwPublicIpv4PrefixLimitGroup_ObjectIdentity = ObjectIdentity
hwPublicIpv4PrefixLimitGroup = _HwPublicIpv4PrefixLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 1)
)
_HwPublicIpv6PrefixLimitGroup_ObjectIdentity = ObjectIdentity
hwPublicIpv6PrefixLimitGroup = _HwPublicIpv6PrefixLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 2)
)
_HwL3vpnIpv6PrefixLimitGroup_ObjectIdentity = ObjectIdentity
hwL3vpnIpv6PrefixLimitGroup = _HwL3vpnIpv6PrefixLimitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 3)
)
_HwEvpnMacObjects_ObjectIdentity = ObjectIdentity
hwEvpnMacObjects = _HwEvpnMacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21)
)


class _HwMacLimitEvpnName_Type(OctetString):
    """Custom type hwMacLimitEvpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMacLimitEvpnName_Type.__name__ = "OctetString"
_HwMacLimitEvpnName_Object = MibScalar
hwMacLimitEvpnName = _HwMacLimitEvpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21, 1),
    _HwMacLimitEvpnName_Type()
)
hwMacLimitEvpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacLimitEvpnName.setStatus("current")
_HwCurMacNum_Type = Unsigned32
_HwCurMacNum_Object = MibScalar
hwCurMacNum = _HwCurMacNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21, 2),
    _HwCurMacNum_Type()
)
hwCurMacNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCurMacNum.setStatus("current")
_HwEvpnMacUpperLimitValue_Type = Unsigned32
_HwEvpnMacUpperLimitValue_Object = MibScalar
hwEvpnMacUpperLimitValue = _HwEvpnMacUpperLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21, 3),
    _HwEvpnMacUpperLimitValue_Type()
)
hwEvpnMacUpperLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEvpnMacUpperLimitValue.setStatus("current")
_HwEvpnMacLowerLimitValue_Type = Unsigned32
_HwEvpnMacLowerLimitValue_Object = MibScalar
hwEvpnMacLowerLimitValue = _HwEvpnMacLowerLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21, 4),
    _HwEvpnMacLowerLimitValue_Type()
)
hwEvpnMacLowerLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEvpnMacLowerLimitValue.setStatus("current")
_HwEvpnMacLimitValue_Type = Unsigned32
_HwEvpnMacLimitValue_Object = MibScalar
hwEvpnMacLimitValue = _HwEvpnMacLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 21, 5),
    _HwEvpnMacLimitValue_Type()
)
hwEvpnMacLimitValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEvpnMacLimitValue.setStatus("current")
_HwEvpnMacLimitTraps_ObjectIdentity = ObjectIdentity
hwEvpnMacLimitTraps = _HwEvpnMacLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 22)
)
_HwEvpnMacLimitConformance_ObjectIdentity = ObjectIdentity
hwEvpnMacLimitConformance = _HwEvpnMacLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 23)
)

# Managed Objects groups

hwStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 1)
)
hwStaticRouteGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwStaticRouteBfdName"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRoutePrefer"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteDescrip"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    hwStaticRouteGroup.setStatus("current")

hwRouteStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 2)
)
hwRouteStatGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwRouteStatTotal"),
        ("HUAWEI-RM-EXT-MIB", "hwRouteStatActive"),
        ("HUAWEI-RM-EXT-MIB", "hwRouteStatAdded"),
        ("HUAWEI-RM-EXT-MIB", "hwRouteStatDeleted"),
        ("HUAWEI-RM-EXT-MIB", "hwRouteStatFreed"))
)
if mibBuilder.loadTexts:
    hwRouteStatGroup.setStatus("current")

hwIpv6RouteStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 3)
)
hwIpv6RouteStatGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatTotal"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatActive"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatAdded"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatDeleted"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6RouteStatFreed"))
)
if mibBuilder.loadTexts:
    hwIpv6RouteStatGroup.setStatus("current")

hwStaticRouteExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 4)
)
hwStaticRouteExtGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwStaticRouteDestVpnNameExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteBfdNameExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRoutePreferExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteRowStatusExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteDescripExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRoutePermanentExt"),
        ("HUAWEI-RM-EXT-MIB", "hwStaticRouteLdpSyncExt"))
)
if mibBuilder.loadTexts:
    hwStaticRouteExtGroup.setStatus("current")

hwIpv6StaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 5)
)
hwIpv6StaticRouteGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteDestVpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteBfdName"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRoutePrefer"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteTag"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteRowStatus"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteNqaAdminName"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteNqaTestName"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6StaticRouteDescr"))
)
if mibBuilder.loadTexts:
    hwIpv6StaticRouteGroup.setStatus("current")

hwRmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 2, 6)
)
hwRmInfoGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixNum"))
)
if mibBuilder.loadTexts:
    hwRmInfoGroup.setStatus("current")

hwTnl2L3vpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2, 1)
)
hwTnl2L3vpnGroup.setObjects(
    ("HUAWEI-RM-EXT-MIB", "hwVpnName")
)
if mibBuilder.loadTexts:
    hwTnl2L3vpnGroup.setStatus("current")

hwTnl2VplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2, 2)
)
hwTnl2VplsGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwVsiIndex"),
        ("HUAWEI-RM-EXT-MIB", "hwVsiId"),
        ("HUAWEI-RM-EXT-MIB", "hwVsiName"),
        ("HUAWEI-RM-EXT-MIB", "hwVplsVcType"),
        ("HUAWEI-RM-EXT-MIB", "hwVplsPeerIp"))
)
if mibBuilder.loadTexts:
    hwTnl2VplsGroup.setStatus("current")

hwTnl2Pwe3VllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2, 3)
)
hwTnl2Pwe3VllGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMasterSlaveFlag"),
        ("HUAWEI-RM-EXT-MIB", "hwPwVllIfName"),
        ("HUAWEI-RM-EXT-MIB", "hwPwVllVcId"),
        ("HUAWEI-RM-EXT-MIB", "hwPwVllSvcFlag"),
        ("HUAWEI-RM-EXT-MIB", "hwPwVcType"),
        ("HUAWEI-RM-EXT-MIB", "hwSvcReceiveLabel"),
        ("HUAWEI-RM-EXT-MIB", "hwSvcTransmitLabel"),
        ("HUAWEI-RM-EXT-MIB", "hwPwVllPeerIp"))
)
if mibBuilder.loadTexts:
    hwTnl2Pwe3VllGroup.setStatus("current")

hwTnlIf2TnlIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2, 4)
)
hwTnlIf2TnlIdGroup.setObjects(
    ("HUAWEI-RM-EXT-MIB", "hwTunnelId")
)
if mibBuilder.loadTexts:
    hwTnlIf2TnlIdGroup.setStatus("current")

hwTnl2MultiHopPwe3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 2, 5)
)
hwTnl2MultiHopPwe3Group.setObjects(
    ("HUAWEI-RM-EXT-MIB", "hwMultiHopPwe3PeerIp")
)
if mibBuilder.loadTexts:
    hwTnl2MultiHopPwe3Group.setStatus("current")

hwTnlGroupObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 7, 2)
)
hwTnlGroupObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwTnlDestination"),
        ("HUAWEI-RM-EXT-MIB", "hwTnlPolicy"))
)
if mibBuilder.loadTexts:
    hwTnlGroupObjectGroup.setStatus("current")

hwIpv4PrefixLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 12, 2)
)
hwIpv4PrefixLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixLimitObjectGroup.setStatus("current")

hwIpv6PrefixLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 13, 2)
)
hwIpv6PrefixLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixLimitObjectGroup.setStatus("current")

hwGresmTokenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 16, 2)
)
hwGresmTokenGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwGresmTokenMode"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenUsedNum"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenMaxValue"))
)
if mibBuilder.loadTexts:
    hwGresmTokenGroup.setStatus("current")

hwPublicIpv4PrefixLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 1, 2)
)
hwPublicIpv4PrefixLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixLimitObjectGroup.setStatus("current")

hwPublicIpv6PrefixLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 2, 2)
)
hwPublicIpv6PrefixLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixLimitObjectGroup.setStatus("current")

hwL3vpnIpv6PrefixLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 3, 2)
)
hwL3vpnIpv6PrefixLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitVpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwL3vpnIpv6PrefixLimitObjectGroup.setStatus("current")

hwEvpnMacLimitObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 23, 2)
)
hwEvpnMacLimitObjectGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMacLimitEvpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurMacNum"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacUpperLimitValue"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLowerLimitValue"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLimitValue"))
)
if mibBuilder.loadTexts:
    hwEvpnMacLimitObjectGroup.setStatus("current")


# Notification objects

hwTunnelGroupUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 6, 1)
)
hwTunnelGroupUp.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwTnlDestination"),
        ("HUAWEI-RM-EXT-MIB", "hwTnlPolicy"))
)
if mibBuilder.loadTexts:
    hwTunnelGroupUp.setStatus(
        "current"
    )

hwTunnelGroupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 6, 2)
)
hwTunnelGroupDown.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwTnlDestination"),
        ("HUAWEI-RM-EXT-MIB", "hwTnlPolicy"))
)
if mibBuilder.loadTexts:
    hwTunnelGroupDown.setStatus(
        "current"
    )

hwIpv4PrefixExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 10, 1)
)
hwIpv4PrefixExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixExceed.setStatus(
        "current"
    )

hwIpv4PrefixExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 10, 2)
)
hwIpv4PrefixExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixExceedClear.setStatus(
        "current"
    )

hwIpv4PrefixThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 10, 3)
)
hwIpv4PrefixThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixThresholdExceed.setStatus(
        "current"
    )

hwIpv4PrefixThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 10, 4)
)
hwIpv4PrefixThresholdExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixThresholdExceedClear.setStatus(
        "current"
    )

hwIpv6PrefixExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 11, 1)
)
hwIpv6PrefixExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixExceed.setStatus(
        "current"
    )

hwIpv6PrefixExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 11, 2)
)
hwIpv6PrefixExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixExceedClear.setStatus(
        "current"
    )

hwIpv6PrefixThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 11, 3)
)
hwIpv6PrefixThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixThresholdExceed.setStatus(
        "current"
    )

hwIpv6PrefixThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 11, 4)
)
hwIpv6PrefixThresholdExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixThresholdExceedClear.setStatus(
        "current"
    )

hwGresmTokenExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 15, 1)
)
hwGresmTokenExceed.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenUsedNum"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenMaxValue"))
)
if mibBuilder.loadTexts:
    hwGresmTokenExceed.setStatus(
        "current"
    )

hwGresmTokenExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 15, 2)
)
hwGresmTokenExceedClear.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenUsedNum"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenMaxValue"))
)
if mibBuilder.loadTexts:
    hwGresmTokenExceedClear.setStatus(
        "current"
    )

hwGresmTokenThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 15, 3)
)
hwGresmTokenThresholdExceed.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenUsedNum"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenMaxValue"))
)
if mibBuilder.loadTexts:
    hwGresmTokenThresholdExceed.setStatus(
        "current"
    )

hwGresmTokenThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 15, 4)
)
hwGresmTokenThresholdExceedClear.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenUsedNum"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenMaxValue"))
)
if mibBuilder.loadTexts:
    hwGresmTokenThresholdExceedClear.setStatus(
        "current"
    )

hwPublicIpv4PrefixExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 1, 1)
)
hwPublicIpv4PrefixExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixExceed.setStatus(
        "current"
    )

hwPublicIpv4PrefixExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 1, 2)
)
hwPublicIpv4PrefixExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixExceedClear.setStatus(
        "current"
    )

hwPublicIpv4PrefixThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 1, 3)
)
hwPublicIpv4PrefixThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixThresholdExceed.setStatus(
        "current"
    )

hwPublicIpv4PrefixThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 1, 4)
)
hwPublicIpv4PrefixThresholdExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv4PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixThresholdExceedClear.setStatus(
        "current"
    )

hwPublicIpv6PrefixExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 2, 1)
)
hwPublicIpv6PrefixExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixExceed.setStatus(
        "current"
    )

hwPublicIpv6PrefixExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 2, 2)
)
hwPublicIpv6PrefixExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixExceedClear.setStatus(
        "current"
    )

hwPublicIpv6PrefixThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 2, 3)
)
hwPublicIpv6PrefixThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixThresholdExceed.setStatus(
        "current"
    )

hwPublicIpv6PrefixThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 2, 4)
)
hwPublicIpv6PrefixThresholdExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixThresholdExceedClear.setStatus(
        "current"
    )

hwL3vpnIpv6PrefixExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 3, 1)
)
hwL3vpnIpv6PrefixExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitVpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwL3vpnIpv6PrefixExceed.setStatus(
        "current"
    )

hwL3vpnIpv6PrefixExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 3, 2)
)
hwL3vpnIpv6PrefixExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitVpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwL3vpnIpv6PrefixExceedClear.setStatus(
        "current"
    )

hwL3vpnIpv6PrefixThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 19, 3, 3)
)
hwL3vpnIpv6PrefixThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitVpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurIpv6PrefixNum"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixLimitValue"))
)
if mibBuilder.loadTexts:
    hwL3vpnIpv6PrefixThresholdExceed.setStatus(
        "current"
    )

hwEvpnMacExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 22, 1)
)
hwEvpnMacExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMacLimitEvpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurMacNum"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLimitValue"))
)
if mibBuilder.loadTexts:
    hwEvpnMacExceed.setStatus(
        "current"
    )

hwEvpnMacExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 22, 2)
)
hwEvpnMacExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMacLimitEvpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurMacNum"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLimitValue"))
)
if mibBuilder.loadTexts:
    hwEvpnMacExceedClear.setStatus(
        "current"
    )

hwEvpnMacThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 22, 3)
)
hwEvpnMacThresholdExceed.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMacLimitEvpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurMacNum"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLimitValue"))
)
if mibBuilder.loadTexts:
    hwEvpnMacThresholdExceed.setStatus(
        "current"
    )

hwEvpnMacThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 22, 4)
)
hwEvpnMacThresholdExceedClear.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwMacLimitEvpnName"),
        ("HUAWEI-RM-EXT-MIB", "hwCurMacNum"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacLimitValue"))
)
if mibBuilder.loadTexts:
    hwEvpnMacThresholdExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwTnlGroupNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 7, 1)
)
hwTnlGroupNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwTunnelGroupUp"),
        ("HUAWEI-RM-EXT-MIB", "hwTunnelGroupDown"))
)
if mibBuilder.loadTexts:
    hwTnlGroupNotificationGroup.setStatus(
        "current"
    )

hwIpv4PrefixLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 12, 1)
)
hwIpv4PrefixLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv4PrefixThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwIpv4PrefixLimitNotificationGroup.setStatus(
        "current"
    )

hwIpv6PrefixLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 13, 1)
)
hwIpv6PrefixLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwIpv6PrefixThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwIpv6PrefixLimitNotificationGroup.setStatus(
        "current"
    )

hwGresmTokenNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 16, 1)
)
hwGresmTokenNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwGresmTokenExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwGresmTokenThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwGresmTokenNotificationGroup.setStatus(
        "current"
    )

hwPublicIpv4PrefixLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 1, 1)
)
hwPublicIpv4PrefixLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwPublicIpv4PrefixExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv4PrefixExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv4PrefixThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv4PrefixThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwPublicIpv4PrefixLimitNotificationGroup.setStatus(
        "current"
    )

hwPublicIpv6PrefixLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 2, 1)
)
hwPublicIpv6PrefixLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwPublicIpv6PrefixExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv6PrefixExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv6PrefixThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwPublicIpv6PrefixThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwPublicIpv6PrefixLimitNotificationGroup.setStatus(
        "current"
    )

hwL3vpnIpv6PrefixLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 2, 3, 1)
)
hwL3vpnIpv6PrefixLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwL3vpnIpv6PrefixExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwL3vpnIpv6PrefixExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwL3vpnIpv6PrefixThresholdExceed"))
)
if mibBuilder.loadTexts:
    hwL3vpnIpv6PrefixLimitNotificationGroup.setStatus(
        "current"
    )

hwEvpnMacLimitNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 23, 1)
)
hwEvpnMacLimitNotificationGroup.setObjects(
      *(("HUAWEI-RM-EXT-MIB", "hwEvpnMacExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacExceedClear"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacThresholdExceed"),
        ("HUAWEI-RM-EXT-MIB", "hwEvpnMacThresholdExceedClear"))
)
if mibBuilder.loadTexts:
    hwEvpnMacLimitNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRmExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwRmExtCompliance.setStatus(
        "current"
    )

hwTunnelExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwTunnelExtCompliance.setStatus(
        "current"
    )

hwRmExtRouteCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 145, 20, 1)
)
if mibBuilder.loadTexts:
    hwRmExtRouteCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RM-EXT-MIB",
    **{"hwRmExt": hwRmExt,
       "hwRmExtObjects": hwRmExtObjects,
       "hwStaticRouteTable": hwStaticRouteTable,
       "hwStaticRouteEntry": hwStaticRouteEntry,
       "hwStaticRouteSourceVpnName": hwStaticRouteSourceVpnName,
       "hwStaticRouteDestIpAddr": hwStaticRouteDestIpAddr,
       "hwStaticRouteDestMaskAddr": hwStaticRouteDestMaskAddr,
       "hwStaticRouteDestVpnName": hwStaticRouteDestVpnName,
       "hwStaticRouteNextHop": hwStaticRouteNextHop,
       "hwStaticRouteOutIfIndex": hwStaticRouteOutIfIndex,
       "hwStaticRouteBfdName": hwStaticRouteBfdName,
       "hwStaticRoutePrefer": hwStaticRoutePrefer,
       "hwStaticRouteDescrip": hwStaticRouteDescrip,
       "hwStaticRouteRowStatus": hwStaticRouteRowStatus,
       "hwRouteStatTable": hwRouteStatTable,
       "hwRouteStatEntry": hwRouteStatEntry,
       "hwRouteStatVpnName": hwRouteStatVpnName,
       "hwRouteStatProtocolId": hwRouteStatProtocolId,
       "hwRouteStatTotal": hwRouteStatTotal,
       "hwRouteStatActive": hwRouteStatActive,
       "hwRouteStatAdded": hwRouteStatAdded,
       "hwRouteStatDeleted": hwRouteStatDeleted,
       "hwRouteStatFreed": hwRouteStatFreed,
       "hwIpv6RouteStatTable": hwIpv6RouteStatTable,
       "hwIpv6RouteStatEntry": hwIpv6RouteStatEntry,
       "hwIpv6RouteStatVpnName": hwIpv6RouteStatVpnName,
       "hwIpv6RouteStatProtocolId": hwIpv6RouteStatProtocolId,
       "hwIpv6RouteStatTotal": hwIpv6RouteStatTotal,
       "hwIpv6RouteStatActive": hwIpv6RouteStatActive,
       "hwIpv6RouteStatAdded": hwIpv6RouteStatAdded,
       "hwIpv6RouteStatDeleted": hwIpv6RouteStatDeleted,
       "hwIpv6RouteStatFreed": hwIpv6RouteStatFreed,
       "hwStaticRouteExtTable": hwStaticRouteExtTable,
       "hwStaticRouteExtEntry": hwStaticRouteExtEntry,
       "hwStaticRouteSourceVpnNameExt": hwStaticRouteSourceVpnNameExt,
       "hwStaticRouteDestIpAddrExt": hwStaticRouteDestIpAddrExt,
       "hwStaticRouteDestMaskAddrExt": hwStaticRouteDestMaskAddrExt,
       "hwStaticRouteNextHopExt": hwStaticRouteNextHopExt,
       "hwStaticRouteOutIfIndexExt": hwStaticRouteOutIfIndexExt,
       "hwStaticRouteDestVpnNameExt": hwStaticRouteDestVpnNameExt,
       "hwStaticRouteBfdNameExt": hwStaticRouteBfdNameExt,
       "hwStaticRoutePreferExt": hwStaticRoutePreferExt,
       "hwStaticRouteDescripExt": hwStaticRouteDescripExt,
       "hwStaticRouteRowStatusExt": hwStaticRouteRowStatusExt,
       "hwStaticRoutePermanentExt": hwStaticRoutePermanentExt,
       "hwStaticRouteLdpSyncExt": hwStaticRouteLdpSyncExt,
       "hwIpv6StaticRouteTable": hwIpv6StaticRouteTable,
       "hwIpv6StaticRouteEntry": hwIpv6StaticRouteEntry,
       "hwIpv6StaticRouteSourceVpnName": hwIpv6StaticRouteSourceVpnName,
       "hwIpv6StaticRouteDestIpAddr": hwIpv6StaticRouteDestIpAddr,
       "hwIpv6StaticRoutePrefixLen": hwIpv6StaticRoutePrefixLen,
       "hwIpv6StaticRouteNextHop": hwIpv6StaticRouteNextHop,
       "hwIpv6StaticRouteOutIfIndex": hwIpv6StaticRouteOutIfIndex,
       "hwIpv6StaticRouteDestVpnName": hwIpv6StaticRouteDestVpnName,
       "hwIpv6StaticRouteBfdName": hwIpv6StaticRouteBfdName,
       "hwIpv6StaticRouteNqaAdminName": hwIpv6StaticRouteNqaAdminName,
       "hwIpv6StaticRouteNqaTestName": hwIpv6StaticRouteNqaTestName,
       "hwIpv6StaticRoutePrefer": hwIpv6StaticRoutePrefer,
       "hwIpv6StaticRouteTag": hwIpv6StaticRouteTag,
       "hwIpv6StaticRouteDescr": hwIpv6StaticRouteDescr,
       "hwIpv6StaticRouteRowStatus": hwIpv6StaticRouteRowStatus,
       "hwRmInfo": hwRmInfo,
       "hwIpv4PrefixNum": hwIpv4PrefixNum,
       "hwIpv6PrefixNum": hwIpv6PrefixNum,
       "hwRmExtConformance": hwRmExtConformance,
       "hwRmExtCompliances": hwRmExtCompliances,
       "hwRmExtCompliance": hwRmExtCompliance,
       "hwRmExtGroups": hwRmExtGroups,
       "hwStaticRouteGroup": hwStaticRouteGroup,
       "hwRouteStatGroup": hwRouteStatGroup,
       "hwIpv6RouteStatGroup": hwIpv6RouteStatGroup,
       "hwStaticRouteExtGroup": hwStaticRouteExtGroup,
       "hwIpv6StaticRouteGroup": hwIpv6StaticRouteGroup,
       "hwRmInfoGroup": hwRmInfoGroup,
       "hwTunnelExtObjects": hwTunnelExtObjects,
       "hwTnl2L3vpnTable": hwTnl2L3vpnTable,
       "hwTnl2L3vpnEntry": hwTnl2L3vpnEntry,
       "hwL3vpnTnlId": hwL3vpnTnlId,
       "hwVpnIndex": hwVpnIndex,
       "hwVpnName": hwVpnName,
       "hwTnl2VplsTable": hwTnl2VplsTable,
       "hwTnl2VplsEntry": hwTnl2VplsEntry,
       "hwVplsTnlId": hwVplsTnlId,
       "hwVplsVcId": hwVplsVcId,
       "hwVsiIndex": hwVsiIndex,
       "hwVsiId": hwVsiId,
       "hwVsiName": hwVsiName,
       "hwVplsVcType": hwVplsVcType,
       "hwVplsPeerIp": hwVplsPeerIp,
       "hwTnl2Pwe3VllTable": hwTnl2Pwe3VllTable,
       "hwTnl2Pwe3VllEntry": hwTnl2Pwe3VllEntry,
       "hwPwVllTnlId": hwPwVllTnlId,
       "hwAcIndex": hwAcIndex,
       "hwPwVllIfName": hwPwVllIfName,
       "hwMasterSlaveFlag": hwMasterSlaveFlag,
       "hwPwVllPeerIp": hwPwVllPeerIp,
       "hwPwVllVcId": hwPwVllVcId,
       "hwPwVllSvcFlag": hwPwVllSvcFlag,
       "hwPwVcType": hwPwVcType,
       "hwSvcReceiveLabel": hwSvcReceiveLabel,
       "hwSvcTransmitLabel": hwSvcTransmitLabel,
       "hwTnlIf2TnlIdTable": hwTnlIf2TnlIdTable,
       "hwTnlIf2TnlIdEntry": hwTnlIf2TnlIdEntry,
       "hwTunnelIf": hwTunnelIf,
       "hwTunnelId": hwTunnelId,
       "hwTnl2MultiHopPwe3Table": hwTnl2MultiHopPwe3Table,
       "hwTnl2MultiHopPwe3Entry": hwTnl2MultiHopPwe3Entry,
       "hwMultiHopPwe3TnlId": hwMultiHopPwe3TnlId,
       "hwMultiHopPwe3VcType": hwMultiHopPwe3VcType,
       "hwMultiHopPwe3VcId": hwMultiHopPwe3VcId,
       "hwMultiHopPwe3PeerIp": hwMultiHopPwe3PeerIp,
       "hwTunnelExtConformance": hwTunnelExtConformance,
       "hwTunnelExtCompliances": hwTunnelExtCompliances,
       "hwTunnelExtCompliance": hwTunnelExtCompliance,
       "hwTunnelExtGroups": hwTunnelExtGroups,
       "hwTnl2L3vpnGroup": hwTnl2L3vpnGroup,
       "hwTnl2VplsGroup": hwTnl2VplsGroup,
       "hwTnl2Pwe3VllGroup": hwTnl2Pwe3VllGroup,
       "hwTnlIf2TnlIdGroup": hwTnlIf2TnlIdGroup,
       "hwTnl2MultiHopPwe3Group": hwTnl2MultiHopPwe3Group,
       "hwTnlGroupTrapObjects": hwTnlGroupTrapObjects,
       "hwTnlDestination": hwTnlDestination,
       "hwTnlPolicy": hwTnlPolicy,
       "hwTnlGroupTraps": hwTnlGroupTraps,
       "hwTunnelGroupUp": hwTunnelGroupUp,
       "hwTunnelGroupDown": hwTunnelGroupDown,
       "hwTnlGroupTrapConformance": hwTnlGroupTrapConformance,
       "hwTnlGroupNotificationGroup": hwTnlGroupNotificationGroup,
       "hwTnlGroupObjectGroup": hwTnlGroupObjectGroup,
       "hwIpv4PrefixLimitTrapObjects": hwIpv4PrefixLimitTrapObjects,
       "hwCurIpv4PrefixNum": hwCurIpv4PrefixNum,
       "hwIpv4PrefixLimitValue": hwIpv4PrefixLimitValue,
       "hwIpv6PrefixLimitTrapObjects": hwIpv6PrefixLimitTrapObjects,
       "hwCurIpv6PrefixNum": hwCurIpv6PrefixNum,
       "hwIpv6PrefixLimitValue": hwIpv6PrefixLimitValue,
       "hwIpv6PrefixLimitVpnName": hwIpv6PrefixLimitVpnName,
       "hwIpv4PrefixLimitTraps": hwIpv4PrefixLimitTraps,
       "hwIpv4PrefixExceed": hwIpv4PrefixExceed,
       "hwIpv4PrefixExceedClear": hwIpv4PrefixExceedClear,
       "hwIpv4PrefixThresholdExceed": hwIpv4PrefixThresholdExceed,
       "hwIpv4PrefixThresholdExceedClear": hwIpv4PrefixThresholdExceedClear,
       "hwIpv6PrefixLimitTraps": hwIpv6PrefixLimitTraps,
       "hwIpv6PrefixExceed": hwIpv6PrefixExceed,
       "hwIpv6PrefixExceedClear": hwIpv6PrefixExceedClear,
       "hwIpv6PrefixThresholdExceed": hwIpv6PrefixThresholdExceed,
       "hwIpv6PrefixThresholdExceedClear": hwIpv6PrefixThresholdExceedClear,
       "hwIpv4PrefixLimitConformance": hwIpv4PrefixLimitConformance,
       "hwIpv4PrefixLimitNotificationGroup": hwIpv4PrefixLimitNotificationGroup,
       "hwIpv4PrefixLimitObjectGroup": hwIpv4PrefixLimitObjectGroup,
       "hwIpv6PrefixLimitConformance": hwIpv6PrefixLimitConformance,
       "hwIpv6PrefixLimitNotificationGroup": hwIpv6PrefixLimitNotificationGroup,
       "hwIpv6PrefixLimitObjectGroup": hwIpv6PrefixLimitObjectGroup,
       "hwRmGresmTokenObjects": hwRmGresmTokenObjects,
       "hwGresmTokenTable": hwGresmTokenTable,
       "hwGresmTokenEntry": hwGresmTokenEntry,
       "hwGresmTokenMode": hwGresmTokenMode,
       "hwGresmTokenUsedNum": hwGresmTokenUsedNum,
       "hwGresmTokenMaxValue": hwGresmTokenMaxValue,
       "hwGresmTokenTraps": hwGresmTokenTraps,
       "hwGresmTokenExceed": hwGresmTokenExceed,
       "hwGresmTokenExceedClear": hwGresmTokenExceedClear,
       "hwGresmTokenThresholdExceed": hwGresmTokenThresholdExceed,
       "hwGresmTokenThresholdExceedClear": hwGresmTokenThresholdExceedClear,
       "hwGresmTokenTrapConformance": hwGresmTokenTrapConformance,
       "hwGresmTokenNotificationGroup": hwGresmTokenNotificationGroup,
       "hwGresmTokenGroup": hwGresmTokenGroup,
       "hwRmExtRouteObjects": hwRmExtRouteObjects,
       "hwRmExtRouteTrapObjects": hwRmExtRouteTrapObjects,
       "hwRmExtRouteTraps": hwRmExtRouteTraps,
       "hwPublicIpv4PrefixLimitTraps": hwPublicIpv4PrefixLimitTraps,
       "hwPublicIpv4PrefixExceed": hwPublicIpv4PrefixExceed,
       "hwPublicIpv4PrefixExceedClear": hwPublicIpv4PrefixExceedClear,
       "hwPublicIpv4PrefixThresholdExceed": hwPublicIpv4PrefixThresholdExceed,
       "hwPublicIpv4PrefixThresholdExceedClear": hwPublicIpv4PrefixThresholdExceedClear,
       "hwPublicIpv6PrefixLimitTraps": hwPublicIpv6PrefixLimitTraps,
       "hwPublicIpv6PrefixExceed": hwPublicIpv6PrefixExceed,
       "hwPublicIpv6PrefixExceedClear": hwPublicIpv6PrefixExceedClear,
       "hwPublicIpv6PrefixThresholdExceed": hwPublicIpv6PrefixThresholdExceed,
       "hwPublicIpv6PrefixThresholdExceedClear": hwPublicIpv6PrefixThresholdExceedClear,
       "hwL3vpnIpv6PrefixLimitTraps": hwL3vpnIpv6PrefixLimitTraps,
       "hwL3vpnIpv6PrefixExceed": hwL3vpnIpv6PrefixExceed,
       "hwL3vpnIpv6PrefixExceedClear": hwL3vpnIpv6PrefixExceedClear,
       "hwL3vpnIpv6PrefixThresholdExceed": hwL3vpnIpv6PrefixThresholdExceed,
       "hwRmExtRouteConformance": hwRmExtRouteConformance,
       "hwRmExtRouteCompliances": hwRmExtRouteCompliances,
       "hwRmExtRouteGroup": hwRmExtRouteGroup,
       "hwPublicIpv4PrefixLimitGroup": hwPublicIpv4PrefixLimitGroup,
       "hwPublicIpv4PrefixLimitNotificationGroup": hwPublicIpv4PrefixLimitNotificationGroup,
       "hwPublicIpv4PrefixLimitObjectGroup": hwPublicIpv4PrefixLimitObjectGroup,
       "hwPublicIpv6PrefixLimitGroup": hwPublicIpv6PrefixLimitGroup,
       "hwPublicIpv6PrefixLimitNotificationGroup": hwPublicIpv6PrefixLimitNotificationGroup,
       "hwPublicIpv6PrefixLimitObjectGroup": hwPublicIpv6PrefixLimitObjectGroup,
       "hwL3vpnIpv6PrefixLimitGroup": hwL3vpnIpv6PrefixLimitGroup,
       "hwL3vpnIpv6PrefixLimitNotificationGroup": hwL3vpnIpv6PrefixLimitNotificationGroup,
       "hwL3vpnIpv6PrefixLimitObjectGroup": hwL3vpnIpv6PrefixLimitObjectGroup,
       "hwEvpnMacObjects": hwEvpnMacObjects,
       "hwMacLimitEvpnName": hwMacLimitEvpnName,
       "hwCurMacNum": hwCurMacNum,
       "hwEvpnMacUpperLimitValue": hwEvpnMacUpperLimitValue,
       "hwEvpnMacLowerLimitValue": hwEvpnMacLowerLimitValue,
       "hwEvpnMacLimitValue": hwEvpnMacLimitValue,
       "hwEvpnMacLimitTraps": hwEvpnMacLimitTraps,
       "hwEvpnMacExceed": hwEvpnMacExceed,
       "hwEvpnMacExceedClear": hwEvpnMacExceedClear,
       "hwEvpnMacThresholdExceed": hwEvpnMacThresholdExceed,
       "hwEvpnMacThresholdExceedClear": hwEvpnMacThresholdExceedClear,
       "hwEvpnMacLimitConformance": hwEvpnMacLimitConformance,
       "hwEvpnMacLimitNotificationGroup": hwEvpnMacLimitNotificationGroup,
       "hwEvpnMacLimitObjectGroup": hwEvpnMacLimitObjectGroup}
)
